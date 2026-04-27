from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


DEFAULT_EXTENSIONS = {
    ".csv",
    ".dat",
    ".docx",
    ".ini",
    ".json",
    ".log",
    ".md",
    ".pdf",
    ".txt",
    ".xml",
}


@dataclass(slots=True)
class DocumentRecord:
    source_path: str
    source_type: str
    title: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SkippedDocument:
    source_path: str
    reason: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class IngestionResult:
    documents: list[DocumentRecord]
    skipped: list[SkippedDocument]


def discover_input_files(root: Path, extensions: Iterable[str] | None = None) -> list[Path]:
    allowed = {ext.lower() for ext in (extensions or DEFAULT_EXTENSIONS)}
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.name.lower() in {"desktop.ini"} or path.name.startswith("~$"):
            continue
        if path.suffix.lower() in allowed:
            files.append(path)
    return files


def load_documents(
    root: Path,
    *,
    extensions: Iterable[str] | None = None,
    max_files: int | None = None,
) -> IngestionResult:
    if not root.exists():
        raise RuntimeError(f"Input directory does not exist: {root}")

    discovered = discover_input_files(root, extensions)
    if max_files is not None:
        discovered = discovered[:max_files]

    documents: list[DocumentRecord] = []
    skipped: list[SkippedDocument] = []
    for path in discovered:
        try:
            record = extract_document(path, root)
        except Exception as exc:
            skipped.append(
                SkippedDocument(
                    source_path=str(path),
                    reason=str(exc),
                    metadata={
                        "relative_path": path.relative_to(root).as_posix(),
                        "extension": path.suffix.lower(),
                    },
                )
            )
            continue
        if record.content.strip():
            documents.append(record)
        else:
            skipped.append(
                SkippedDocument(
                    source_path=str(path),
                    reason="Empty extracted content",
                    metadata={
                        "relative_path": path.relative_to(root).as_posix(),
                        "extension": path.suffix.lower(),
                    },
                )
            )
    return IngestionResult(documents=documents, skipped=skipped)


def extract_document(path: Path, root: Path) -> DocumentRecord:
    suffix = path.suffix.lower()
    if suffix == ".json":
        content = _read_json(path)
    elif suffix == ".docx":
        content = _read_docx(path)
    elif suffix == ".pdf":
        content = _read_pdf(path)
    else:
        content = _read_text(path)

    relative_path = path.relative_to(root).as_posix()
    return DocumentRecord(
        source_path=str(path),
        source_type=suffix.lstrip("."),
        title=path.stem,
        content=content.strip(),
        metadata={
            "relative_path": relative_path,
            "extension": suffix,
        },
    )


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_json(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    return json.dumps(data, indent=2, ensure_ascii=False)


def _read_docx(path: Path) -> str:
    import mammoth

    with path.open("rb") as handle:
        result = mammoth.convert_to_markdown(handle)
    return result.value


def _read_pdf(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n\n".join(page.strip() for page in pages if page.strip())