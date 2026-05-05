"""KNOWLEDGE_ROOT resolution and well-known subpaths.

Paths are computed lazily from `KNOWLEDGE_ROOT` (env var, default ~/code/knowledge/)
so tests can override via `monkeypatch.setenv("KNOWLEDGE_ROOT", ...)`.
"""

import os
from pathlib import Path

SOURCE_TYPES: tuple[str, ...] = (
    "youtube",
    "arxiv",
    "pubmed",
    "pdf",
    "web",
    "voice",
    "audiobook",
    "note",
    "csv",
    "docx",
    "xlsx",
    "pptx",
    "image",
    "other",
)


def knowledge_root() -> Path:
    return Path(os.environ.get("KNOWLEDGE_ROOT", str(Path.home() / "code" / "knowledge")))


def raw_dir() -> Path:
    return knowledge_root() / "raw"


def wiki_dir() -> Path:
    return knowledge_root() / "wiki"


def nlm_dir() -> Path:
    return knowledge_root() / "nlm"


def knowledge_internal() -> Path:
    return knowledge_root() / ".knowledge"


def locks_dir() -> Path:
    return knowledge_internal() / "locks"


def lint_dir() -> Path:
    return knowledge_internal() / "lint"


def policies_dir() -> Path:
    return knowledge_internal() / "policies"


def index_path() -> Path:
    return knowledge_root() / "index.md"


def log_path() -> Path:
    return knowledge_root() / "log.md"


def raw_dir_for(source_type: str) -> Path:
    if source_type not in SOURCE_TYPES:
        raise ValueError(f"unknown source type: {source_type!r}")
    return raw_dir() / source_type


def raw_source_path(source_type: str, source_id: str) -> Path:
    return raw_dir_for(source_type) / f"{source_id}.md"


def wiki_source_path(source_id: str) -> Path:
    return wiki_dir() / "sources" / f"{source_id}.md"
