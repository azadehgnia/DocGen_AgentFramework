# BRD Prompt Templates

These prompt templates are designed to fill [Input/BRD-Template_Plain_01.md](c:/Users/azghafar/OneDrive%20-%20Microsoft/Code/AI_Projects/AgentFramework/Input/BRD-Template_Plain_01.md) section by section using attached user context files.

Recommended usage order:

1. Run `00-master-orchestration.prompt.md`
2. If the source material is weak or noisy, run `00-strict-grounded.prompt.md` instead of the standard master prompt
3. If needed, refine outputs with `01-introduction.prompt.md`
4. If needed, refine outputs with `02-context.prompt.md`
5. If needed, refine outputs with `03-business-requirements.prompt.md`
6. If needed, refine outputs with `04-non-functional-requirements.prompt.md`
7. If needed, refine outputs with `05-documentation.prompt.md`
8. If needed, refine outputs with `06-appendix.prompt.md`

Usage notes:

- Attach the BRD template and all available project context files.
- Ask the model to return markdown only.
- Require the model to preserve headings and tables.
- Require unsupported fields to remain blank or be marked `[To be confirmed]`.
- Prefer grounded content over inferred content.

Files:

- `00-master-orchestration.prompt.md`: Full-document orchestration prompt
- `00-strict-grounded.prompt.md`: Full-document orchestration prompt with stricter anti-hallucination controls
- `01-introduction.prompt.md`: Section 1 only
- `02-context.prompt.md`: Section 2 only
- `03-business-requirements.prompt.md`: Section 3 only
- `04-non-functional-requirements.prompt.md`: Section 4 only
- `05-documentation.prompt.md`: Section 5 only
- `06-appendix.prompt.md`: Appendix only

When to use the strict prompt:

- Source files are incomplete, ambiguous, or inconsistent.
- You want the model to prefer blanks over speculative wording.
- You want every populated statement to be explicitly grounded in attached evidence.

