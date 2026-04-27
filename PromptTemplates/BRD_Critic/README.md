# BRD Critic Prompt Templates

These prompt templates are designed to review a completed or partially completed BRD against the attached source materials and assess whether the content is a good fit for the template and the underlying project evidence.

Recommended usage order:

1. Run `00-master-review.prompt.md`
2. If needed, run the matching section-specific review prompt
3. Revise the BRD draft
4. Re-run the relevant review prompt for validation

Files:

- `00-master-review.prompt.md`: Full-document review prompt
- `01-introduction-review.prompt.md`: Review section 1 only
- `02-context-review.prompt.md`: Review section 2 only
- `03-business-requirements-review.prompt.md`: Review section 3 only
- `04-non-functional-requirements-review.prompt.md`: Review section 4 only
- `05-documentation-review.prompt.md`: Review section 5 only
- `06-appendix-review.prompt.md`: Review appendix only

Usage notes:

- Attach the BRD template, the BRD draft being reviewed, and all available project context files.
- Ask the model to return review findings in markdown.
- Require the model to distinguish supported, weakly supported, and unsupported content.
- Ask for concrete edits, not generic commentary.
- Prefer evidence-backed criticism over style-only feedback.
