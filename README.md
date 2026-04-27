# Document Generator Workflow using Agent Framework

This project is a document-processing and drafting workflow for generating Section 2 content (can be extended to all sections) for a Business Requirements Document from project source material. It ingests mixed-format evidence, builds a grounded context bundle, uses Azure AI Foundry-hosted models to draft and review the section, and produces a short BCM-oriented project brief plus a BCM impact review.

## Author
This repository was authored by Azadeh Nia.

## Purpose

This project is designed to support a business analyst. It reduces manual effort in early BRD preparation by:

- loading project evidence from a configured input folder
- extracting text from markdown, text, JSON, CSV-like text files, PDF, and DOCX inputs
- prioritizing higher-value business documents over technical sample files
- generating a BRD Section 2 draft using only the supplied evidence
- reviewing the draft for unsupported claims and missing evidence
- producing a concise project brief for downstream analysis
- checking likely BCM impacts against a configured BCM reference PDF

The goal is a repeatable, evidence-grounded workflow for internal project documentation rather than open-ended content generation.

## How It Works

The workflow in [backend/app.py](backend/app.py) runs four main stages:

1. Ingest source documents from `INPUT_FOLDER_PATH`.
2. Rank and filter documents so business-facing sources are prioritized.
3. Build a bounded context bundle and send it to a Foundry-backed writer and reviewer workflow.
4. Save generated markdown outputs for the draft, review, project brief, and BCM review.

Supporting modules:

- [backend/document_ingestion.py](backend/document_ingestion.py): discovers files and extracts text from supported formats
- [backend/context_builder.py](backend/context_builder.py): trims and packages evidence into model-ready context
- [PromptTemplates](PromptTemplates): prompt templates used to structure the BRD and review workflow

## Repository Structure

- [backend](backend): application code, environment config, requirements, and generated outputs
- [data](data): input and output working data used by the workflow
- [PromptTemplates](PromptTemplates): reusable BRD and review prompt templates


## Configuration

Runtime settings are loaded from [backend/.env.example](backend/.env.example). The main variables are:

- `FOUNDRY_PROJECT_ENDPOINT`: Azure AI Foundry project endpoint
- `FOUNDRY_MODEL`: model deployment name, currently configured for GPT-5.4
- `INPUT_FOLDER_PATH`: relative or absolute path to the project evidence folder
- `OUTPUT_FOLDER_PATH`: relative or absolute path for generated markdown outputs
- `BCM_PDF_PATH`: path to the BCM reference PDF used by the reviewer tool
- `INPUT_EXTENSIONS`: allowed file extensions for ingestion
- `INPUT_MAX_FILES`: maximum number of source files to ingest
- `INPUT_MAX_CHARS`: maximum evidence size passed into the drafting workflow

Relative paths are resolved from the repository root.

## Running The Project

From the repository root:

```powershell
pip install -r backend/requirements.txt
python backend/app.py
```

Generated outputs are written to the configured output folder and typically include:

- `section-02-draft.md`
- `section-02-review.md`
- `section-02-project-brief.md`
- `section-02-bcm-review.md`


The project reflects a practical authoring approach focused on:

- grounded document generation instead of speculative output
- structured review and traceability
- reusable prompt-driven workflows for BRD production
- automation of evidence ingestion and BCM-oriented analysis

If you want this README to present your full professional profile, add your preferred name, title, team, and contact details here.

## Notes

- The `data` directory contents are synthetic.
- The workflow depends on Azure authentication and a valid Foundry project configuration.
- DOCX extraction uses the `mammoth` library and PDF extraction uses `pypdf`.