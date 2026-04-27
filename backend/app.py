import asyncio
import os
import re
from functools import lru_cache
from pathlib import Path

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

from agent_framework import (
    Agent,
    AgentExecutor,
    AgentExecutorRequest,
    AgentExecutorResponse,
    InMemoryHistoryProvider,
    Message,
    WorkflowBuilder,
    WorkflowContext,
    WorkflowRunState,
    executor,
)

from context_builder import build_context_bundle
from document_ingestion import DEFAULT_EXTENSIONS, load_documents

from azure.ai.projects import AIProjectClient
from pypdf import PdfReader

load_dotenv()


WORKFLOW_ARTIFACTS: dict[str, str] = {}


REPO_ROOT = Path(__file__).resolve().parents[1]


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


credential = AzureCliCredential()


def _resolve_env_path(value: str) -> Path:
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _resolve_input_root() -> Path:
    if input_folder_path := os.getenv("INPUT_FOLDER_PATH"):
        return _resolve_env_path(input_folder_path)

    raise RuntimeError("Provide INPUT_FOLDER_PATH.")


def _default_output_dir() -> Path:
    if output_folder_path := os.getenv("OUTPUT_FOLDER_PATH"):
        return _resolve_env_path(output_folder_path)
    raise RuntimeError("Provide OUTPUT_FOLDER_PATH.")


def _default_bcm_pdf_path() -> Path:
    if bcm_pdf_path := os.getenv("BCM_PDF_PATH"):
        return _resolve_env_path(bcm_pdf_path)
    raise RuntimeError("Provide BCM_PDF_PATH.")

def _parse_extensions(value: str | None) -> set[str]:
    if not value:
        return DEFAULT_EXTENSIONS
    return {f".{item.strip().lstrip('.').lower()}" for item in value.split(",") if item.strip()}


def _last_agent_text(messages: list, agent_name: str) -> str | None:
    for message in reversed(messages):
        if message.author_name == agent_name and message.text:
            return message.text
    return None


def _write_markdown_output(path: Path, content: str | None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text((content or "").strip() + "\n", encoding="utf-8")


def _document_priority(document) -> tuple[int, str]:
    relative_path = str(document.metadata.get("relative_path", document.source_path)).lower()
    extension = str(document.metadata.get("extension", "")).lower()

    score = 0
    if "investment brief" in relative_path:
        score += 100
    if "one-pager" in relative_path or "one pager" in relative_path:
        score += 90
    if "process catalogue" in relative_path:
        score += 80
    if "approved process" in relative_path:
        score += 70
    if extension in {".pdf", ".docx", ".pptx", ".md", ".txt"}:
        score += 20
    if "pre reads/sample input and output files" in relative_path:
        score -= 80
    if "/results/" in relative_path or "input_output/1a_outputs" in relative_path:
        score -= 60
    if extension in {".csv", ".ini", ".json", ".xml", ".dat", ".log"}:
        score -= 15

    return score, relative_path


def _select_writer_documents(documents: list) -> list:
    ranked = sorted(documents, key=_document_priority, reverse=True)
    primary = [document for document in ranked if _document_priority(document)[0] >= 40]
    if primary:
        return primary[:8]
    return ranked[:8]


def _agent_response_text(messages: Message | list[Message] | None, empty_text: str) -> str:
    if not messages:
        return empty_text
    if isinstance(messages, list):
        text = "\n\n".join(message.text for message in messages if message.text)
        return text or empty_text
    return messages.text or empty_text


@lru_cache(maxsize=4)
def _load_pdf_pages(pdf_path: str) -> list[str]:
    reader = PdfReader(pdf_path)
    return [" ".join((page.extract_text() or "").split()) for page in reader.pages]


def _build_bcm_snippet(page_text: str, query_terms: list[str], window: int = 700) -> str:
    if not page_text:
        return ""

    lower_text = page_text.lower()
    positions = [lower_text.find(term) for term in query_terms if lower_text.find(term) >= 0]
    if not positions:
        return page_text[:window]

    start = max(min(positions) - 180, 0)
    end = min(start + window, len(page_text))
    return page_text[start:end].strip()


def search_bcm_pdf(query: str, max_results: int = 5) -> str:
    """Search the configured BCM PDF and return the most relevant excerpts with page numbers."""
    pdf_path = Path(os.getenv("BCM_PDF_PATH", str(_default_bcm_pdf_path())))
    if not pdf_path.exists():
        return f"BCM PDF not found: {pdf_path}"

    query_terms = [term.lower() for term in re.findall(r"\w+", query) if len(term) > 2]
    if not query_terms:
        return "Provide a more specific BCM search query."

    scored_pages: list[tuple[int, int, str]] = []
    for page_number, page_text in enumerate(_load_pdf_pages(str(pdf_path)), start=1):
        lower_text = page_text.lower()
        score = sum(lower_text.count(term) for term in query_terms)
        if score > 0:
            scored_pages.append((score, page_number, _build_bcm_snippet(page_text, query_terms)))

    if not scored_pages:
        return f"No matching BCM content found in {pdf_path.name} for query: {query}"

    scored_pages.sort(key=lambda item: (-item[0], item[1]))
    excerpts = [
        f"[Page {page_number}] {snippet}"
        for _, page_number, snippet in scored_pages[:max_results]
        if snippet
    ]
    return f"BCM source: {pdf_path.name}\n\n" + "\n\n".join(excerpts)

def _load_prompt_template() -> str:
    template_path = (
        REPO_ROOT
        / "PromptTemplates"
        / "BRD"
        / "02-context.prompt.md"
    )
    return template_path.read_text(encoding="utf-8")

# agent = client.as_agent(
#     name=os.getenv("AGENT_NAME", "DocsAgent"),
#     instructions=os.getenv(
#         "AGENT_INSTRUCTIONS",
#         "You are a friendly assistant. Keep your answers brief.",
#     ),
# )


@executor(id="prepare_reviewer_request")
async def prepare_reviewer_request(
    agent_response: AgentExecutorResponse, ctx: WorkflowContext[AgentExecutorRequest]
) -> None:
    review_text = _agent_response_text(
        agent_response.agent_response.messages,
        "[Writer produced no draft output.]",
    )
    WORKFLOW_ARTIFACTS["writer_draft"] = review_text

    await ctx.send_message(
        AgentExecutorRequest(
            messages=[
                Message(
                    role="user",
                    contents=[
                        "Review the following Section 2 draft. Return markdown using exactly these top-level headings in this order: Findings, Unsupported claims, Missing evidence, Proposed edits. Under each heading, use bullet points only. If a heading has nothing to report, write '- None'.\n\n"
                        f"Writer draft:\n\n{review_text}"
                    ],
                )
            ]
        )
    )


@executor(id="prepare_brief_request")
async def prepare_brief_request(
    agent_response: AgentExecutorResponse, ctx: WorkflowContext[AgentExecutorRequest]
) -> None:
    reviewer_text = _agent_response_text(
        agent_response.agent_response.messages,
        "[Reviewer produced no output.]",
    )
    WORKFLOW_ARTIFACTS["review_findings"] = reviewer_text
    writer_draft = WORKFLOW_ARTIFACTS.get("writer_draft", "[Writer produced no draft output.]")

    await ctx.send_message(
        AgentExecutorRequest(
            messages=[
                Message(
                    role="user",
                    contents=[
                        "Create a concise project brief from the BRD draft below so it can be used by a BCM capability-mapping agent. Return markdown using exactly these top-level headings in this order: Project summary, Business objective, In-scope themes, Key evidence, BCM mapping cues. Under each heading, use bullet points only. If a heading has nothing to report, write '- None'. Keep the brief short, evidence-based, and focused on BCM mapping.\n\n"
                        f"BRD draft:\n\n{writer_draft}\n\n"
                        f"Reviewer findings:\n\n{reviewer_text}"
                    ],
                )
            ]
        )
    )


@executor(id="prepare_bcm_reviewer_request")
async def prepare_bcm_reviewer_request(
    agent_response: AgentExecutorResponse, ctx: WorkflowContext[AgentExecutorRequest]
) -> None:
    brief_text = _agent_response_text(
        agent_response.agent_response.messages,
        "[Brief agent produced no output.]",
    )
    WORKFLOW_ARTIFACTS["project_brief"] = brief_text

    await ctx.send_message(
        AgentExecutorRequest(
            messages=[
                Message(
                    role="user",
                    contents=[
                        "Use the project brief below to identify impacted BCM capabilities. Use the search_bcm_pdf tool to look up the BCM reference PDF before making claims. Return markdown with exactly these top-level headings in this order: Impacted capabilities, Evidence gaps. Under each heading, use bullet points only. If there is nothing to report for a heading, write '- None'.\n\n"
                        f"Project brief:\n\n{brief_text}"
                    ],
                )
            ]
        )
    )

async def main() -> None:
    input_root = _resolve_input_root()
    output_dir = Path(os.getenv("OUTPUT_DIR", str(_default_output_dir())))
    input_extensions = _parse_extensions(os.getenv("INPUT_EXTENSIONS"))
    max_files = int(os.getenv("INPUT_MAX_FILES", "12"))
    max_context_chars = int(os.getenv("INPUT_MAX_CHARS", "666000"))

    ingestion = load_documents(
        input_root,
        extensions=input_extensions,
        max_files=max_files,
    )
    documents = ingestion.documents
    writer_documents = _select_writer_documents(documents)
    context_bundle = build_context_bundle(
        writer_documents,
        max_total_chars=max_context_chars,
        max_chars_per_document=8000,
    )

    client = FoundryChatClient(
        project_endpoint=_require_env("FOUNDRY_PROJECT_ENDPOINT"),
        model=os.getenv("FOUNDRY_MODEL", "gpt-5.4"),
        credential=credential,
    )

#web search agent
    project_client = AIProjectClient(
    endpoint=_require_env("FOUNDRY_PROJECT_ENDPOINT"),
    credential=credential,
    )

    websearch_agent = "BRD-Drafter"
    ws_version = "3"
    openai_client = project_client.get_openai_client()

    # Reference the agent to get a response
    # response = openai_client.responses.create(
    #     input=[{"role": "user", "content": "Tell me what you can help with."}],
    #     extra_body={"agent_reference": {"name": websearch_agent, "version": ws_version, "type": "agent_reference"}},
    # )

    # print(f"Response output: {response.output_text}")
#end web search agent

    shared_history = InMemoryHistoryProvider()

    writer = Agent(
        client=client,
        instructions=(
        "You are a senior business analyst drafting Business Requirements Documents. "
        "Your task is to produce Section 2 of a BRD using only the provided evidence. "
        "Prioritize project-level documents such as the investment brief, one-pager, approved process material, and process catalogue over technical sample input/output files. "
        "Treat sample CSV, INI, and result files as supplemental evidence only, not as the primary description of the project purpose. "
        "Do not invent facts, names, dates, stakeholders, risks, or scope items. "
        "If evidence is missing, write [To be confirmed] or leave table cells blank where appropriate. "
        "Keep the tone formal, concise, and suitable for stakeholder review. "
        "Preserve the requested markdown headings and table structure exactly."
        ),
        name="writer",
                context_providers=[shared_history],
    )

    reviewer = Agent(
        client=client,
        instructions=(
        "You are a BRD reviewer. Review Section 2 of the BRD for evidence fit, "
            "completeness, structure, and unsupported claims. Review the writer's draft, not the source evidence alone. "
            "Identify missing supported content, weak assumptions, contradictions, and any statement that is not grounded in the provided evidence. "
            "Return your review in markdown using exactly these top-level headings and in this order: Findings, Unsupported claims, Missing evidence, Proposed edits. "
            "Under each heading, use bullet points only. If there is nothing to report for a heading, write a single bullet that says None. "
            "In Proposed edits, provide concrete replacement text or precise edit instructions for Section 2 items that need correction. "
            "Do not rewrite the full section unless a specific edit requires it. Do not add any headings before, after, or between the required sections."
      ),
        name="reviewer",
                context_providers=[shared_history],
    )

    brief_agent = Agent(
        client=client,
        instructions=(
        "You create concise project briefs from BRD drafts for downstream analysis agents. "
            "Summarize only evidence-backed information from the BRD draft and reviewer findings. "
            "Return markdown with exactly these top-level headings in this order: Project summary, Business objective, In-scope themes, Key evidence, BCM mapping cues. "
            "Under each heading, use bullet points only. If there is nothing to report for a heading, write a single bullet that says None. "
            "The BCM mapping cues section should highlight the strongest candidate terms, activities, systems, or process themes that a BCM agent should search for."
      ),
        name="brief_agent",
        context_providers=[shared_history],
    )

    BCM_reviewer = Agent(
        client=client,
        instructions=(
        "You are a BCM impact reviewer for BRD Section 2. Use the supplied project brief and the search_bcm_pdf tool to inspect the BCM PDF before identifying impacted capabilities. "
            "Only list capabilities that are supported by the BRD content and the BCM PDF excerpts returned by the tool. "
            "Return markdown with exactly these top-level headings in this order: Impacted capabilities, Evidence gaps. "
            "Under each heading, use bullet points only. If there is nothing to report for a heading, write a single bullet that says None. "
            "For each impacted capability bullet, use this format: - Capability Name (Reasoning for impact; cite the BCM page number when available)."
      ),
        name="BCM_reviewer",
        tools=[search_bcm_pdf],
        context_providers=[shared_history],
    )

    # Create the shared session
    shared_session = writer.create_session()
    writer_executor = AgentExecutor(writer, session=shared_session)
    reviewer_executor = AgentExecutor(reviewer, session=shared_session)
    brief_executor = AgentExecutor(brief_agent, session=shared_session)
    bcm_reviewer_executor = AgentExecutor(BCM_reviewer, session=shared_session)

    prompt_template = _load_prompt_template()

    workflow_input = (
        f"{prompt_template}\n\n"
        f"Project evidence:\n\n"
        f"{context_bundle}"
    )

    workflow = (
        WorkflowBuilder(start_executor=writer_executor)
        .add_chain([
            writer_executor,
            prepare_reviewer_request,
            reviewer_executor,
            prepare_brief_request,
            brief_executor,
            prepare_bcm_reviewer_request,
            bcm_reviewer_executor,
        ])
        .build()
    )

    # prompt = os.getenv("AGENT_PROMPT", "Write a tagline for a budget-friendly eBike.")
    # workflow_input = (
    #     f"Task:\n{prompt}\n\n"
    #     f"Use only the evidence below. If the evidence is insufficient, say so.\n\n"
    #     f"Evidence:\n{context_bundle}"
    # )

    result = await workflow.run(workflow_input)

    assert result.get_final_state() == WorkflowRunState.IDLE

    print(f"Loaded {len(documents)} input document(s) from {input_root}")
    print(f"Selected {len(writer_documents)} prioritized document(s) for writer context")
    if ingestion.skipped:
        print(f"Skipped {len(ingestion.skipped)} input document(s):")
        for skipped in ingestion.skipped:
            relative_path = skipped.metadata.get("relative_path", skipped.source_path)
            print(f"- {relative_path}: {skipped.reason}")
    memory_state = shared_session.state.get(InMemoryHistoryProvider.DEFAULT_SOURCE_ID, {})
    session_messages = memory_state.get("messages", [])

    draft_path = output_dir / "section-02-draft.md"
    review_path = output_dir / "section-02-review.md"
    brief_path = output_dir / "section-02-project-brief.md"
    bcm_review_path = output_dir / "section-02-bcm-review.md"
    _write_markdown_output(draft_path, _last_agent_text(session_messages, "writer"))
    _write_markdown_output(review_path, _last_agent_text(session_messages, "reviewer"))
    _write_markdown_output(brief_path, _last_agent_text(session_messages, "brief_agent"))
    _write_markdown_output(bcm_review_path, _last_agent_text(session_messages, "BCM_reviewer"))

    print(f"Saved writer draft to {draft_path}")
    print(f"Saved reviewer output to {review_path}")
    print(f"Saved project brief to {brief_path}")
    print(f"Saved BCM reviewer output to {bcm_review_path}")
    print("=== Shared Session Conversation ===")
    for message in session_messages:
        if not message.text or not message.text.strip():
            continue
        print(f"{message.author_name or message.role}: {message.text}")



if __name__ == "__main__":
    asyncio.run(main())