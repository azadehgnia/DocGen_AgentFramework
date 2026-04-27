from __future__ import annotations

from typing import Iterable

from document_ingestion import DocumentRecord


def build_context_bundle(
    documents: Iterable[DocumentRecord],
    *,
    max_total_chars: int = 16000,
    max_chars_per_document: int = 4000,
) -> str:
    parts: list[str] = []
    current_size = 0

    for document in documents:
        body = _truncate(document.content, max_chars_per_document)
        block = (
            f"[Source: {document.metadata.get('relative_path', document.source_path)}]\n"
            f"[Type: {document.source_type}]\n"
            f"[Title: {document.title}]\n\n"
            f"{body}"
        )
        projected = current_size + len(block) + 2
        if projected > max_total_chars:
            break
        parts.append(block)
        current_size = projected

    return "\n\n".join(parts)


def _truncate(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 15].rstrip() + "\n\n[Truncated]"