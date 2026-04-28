"""Shared pytest fixtures for gateway tests."""

from datetime import datetime, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway import validator


@pytest.fixture
def kb_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Override KNOWLEDGE_ROOT to a temp directory for the duration of the test."""
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    # Pre-create the well-known directories the gateway expects
    for sub in ("raw", "wiki", "wiki/sources", "nlm", ".knowledge", ".knowledge/locks"):
        (tmp_path / sub).mkdir(parents=True, exist_ok=True)
    for src_type in paths.SOURCE_TYPES:
        (tmp_path / "raw" / src_type).mkdir(parents=True, exist_ok=True)
    return tmp_path


def make_canonical_source(
    *,
    type_: str = "youtube",
    id_: str = "yt-testABC_123",
    title: str = "Test source",
    body: str = "Body content for the test source.\n",
    url: str = "https://www.youtube.com/watch?v=testABC_123",
    authors: list[str] | None = None,
    published_at: str = "2026-01-15",
    domains: list[str] | None = None,
    meta: dict | None = None,
    extra_front: dict | None = None,
) -> str:
    """Build a valid canonical source markdown string with correct content_hash."""
    front: dict = {
        "id": id_,
        "type": type_,
        "title": title,
        "url": url,
        "authors": authors if authors is not None else ["Test Author"],
        "published_at": published_at,
        "ingested_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "content_hash": validator.compute_content_hash(body),
        "domains": domains if domains is not None else [],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": meta if meta is not None else {"channel": "Test Channel", "duration_seconds": 600},
    }
    if extra_front:
        front.update(extra_front)
    return fm.serialize(front, body)


@pytest.fixture
def make_source():
    """Test helper available as a fixture."""
    return make_canonical_source
