Review the attached BRD draft end to end and assess whether it is a good fit for the BRD template and the attached project context files.

Inputs:

- The BRD markdown template
- The BRD draft to review
- All attached project context files provided by the user

Primary objective:

- Evaluate whether the BRD draft is accurate, appropriately structured, and well-supported by the source files.

Review workflow:

1. Read the BRD template, the BRD draft, and all attached source files.
2. Compare the draft against the expected BRD structure and the available evidence.
3. Assess each major section for fit, quality, completeness, and evidence support.
4. Identify where the draft is strong, weak, speculative, incomplete, or off-template.
5. Recommend specific improvements.

Review criteria:

- Structural fit: Does the draft align with the BRD template headings, tables, and intended section purpose?
- Evidence fit: Is the content supported by the attached files?
- Business fit: Is the wording appropriate for a formal BRD rather than informal notes or technical design?
- Completeness: Are important supported points missing?
- Precision: Are requirements, assumptions, risks, dependencies, and glossary entries stated clearly?
- Caution: Does the draft overstate certainty where the source files are weak?

Output format:

- Return markdown only.
- Use these sections:
  - `Overall Assessment`
  - `Findings By Section`
  - `Unsupported Or Weakly Supported Content`
  - `Missing But Supported Content`
  - `Recommended Edits`
  - `Final Fit Verdict`
- In `Final Fit Verdict`, rate the draft as one of:
  - `Good fit`
  - `Mostly good fit with revisions`
  - `Weak fit`

Important constraints:

- Ground every finding in the attached files or the template.
- Prefer precise, actionable feedback over vague advice.
- Call out speculative text explicitly.
- Do not rewrite the entire BRD unless necessary; focus on review and recommended changes.
