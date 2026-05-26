"""QUAL-14: wiki reingest — source-decay re-ingest policy."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import frontmatter as fm, paths
from gateway.ops.reingest import (
    _affected_wiki_pages,
    _next_version_id,
    _version_base,
    reingest,
)
from gateway.lint import superseded_citations


# --- helpers ------------------------------------------------------------------


def _write_raw_source(kb_root: Path, source_id: str, **extra_front) -> Path:
    """Write a minimal valid canonical source to raw/<type>/<id>.md."""
    source_type = source_id.split("-")[0]
    if source_type not in paths.SOURCE_TYPES:
        source_type = "web"
    from gateway import validator

    body = f"Body content for {source_id}.\n"
    front: dict = {
        "id": source_id,
        "type": source_type,
        "title": f"Title for {source_id}",
        "url": f"https://example.com/{source_id}",
        "authors": ["Test Author"],
        "published_at": "2026-01-15",
        "ingested_at": "2026-01-15T00:00:00Z",
        "content_hash": validator.compute_content_hash(body),
        "domains": [],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
        "schema_version": 1,
    }
    front.update(extra_front)
    p = paths.raw_source_path(source_type, source_id)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fm.serialize(front, body), encoding="utf-8")
    return p


def _write_wiki_source(kb_root: Path, source_id: str, body: str = "") -> Path:
    d = kb_root / "wiki" / "sources"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{source_id}.md"
    p.write_text(body or f"[[sources/{source_id}]]\n", encoding="utf-8")
    return p


# --- _version_base ------------------------------------------------------------


def test_version_base_no_suffix():
    assert _version_base("web-2026-01-15-abc") == ("web-2026-01-15-abc", 1)


def test_version_base_v2():
    assert _version_base("web-2026-01-15-abc-v2") == ("web-2026-01-15-abc", 2)


def test_version_base_v10():
    assert _version_base("arxiv-2403-12345-v10") == ("arxiv-2403-12345", 10)


# --- _next_version_id ---------------------------------------------------------


def test_next_version_id_base():
    assert _next_version_id("web-abc") == "web-abc-v2"


def test_next_version_id_v2():
    assert _next_version_id("web-abc-v2") == "web-abc-v3"


# --- _affected_wiki_pages -----------------------------------------------------


def test_affected_wiki_pages_finds_citation(kb_root: Path) -> None:
    source_id = "web-2026-01-15-abc"
    wiki_dir = kb_root / "wiki" / "synthesis"
    wiki_dir.mkdir(parents=True, exist_ok=True)
    (wiki_dir / "test-synth.md").write_text(
        f"Some claim [[sources/{source_id}]] that references something.\n"
    )
    affected = _affected_wiki_pages(source_id)
    assert any("test-synth.md" in p for p in affected)


def test_affected_wiki_pages_none(kb_root: Path) -> None:
    assert _affected_wiki_pages("web-nonexistent") == []


# --- reingest integration tests -----------------------------------------------


def test_reingest_fails_when_source_not_found(kb_root: Path) -> None:
    result = reingest("web-nonexistent", "https://example.com/new")
    assert not result.success
    assert "not found" in result.errors[0]


def test_reingest_fails_when_already_superseded(kb_root: Path) -> None:
    _write_raw_source(kb_root, "web-2026-01-15-abc", superseded_by="web-2026-01-15-abc-v2")
    result = reingest("web-2026-01-15-abc", "https://example.com/v2")
    assert not result.success
    assert "already superseded" in result.errors[0]


def test_reingest_stamps_superseded_by_on_old_source(kb_root: Path, monkeypatch) -> None:
    _write_raw_source(kb_root, "web-2026-01-15-abc")

    # Stub the ingest call so no network access is needed
    from gateway.core import OperationResult

    new_path = paths.raw_source_path("web", "web-2026-01-15-abc-v2")

    def _fake_ingest(input_path, **kwargs):
        # Write a stub new source file
        from gateway import validator

        body = "New body content.\n"
        front = {
            "id": "web-2026-01-15-abc-v2",
            "type": "web",
            "title": "New version",
            "url": "https://example.com/v2",
            "authors": ["Test Author"],
            "published_at": "2026-03-01",
            "ingested_at": "2026-03-01T00:00:00Z",
            "content_hash": validator.compute_content_hash(body),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {},
            "schema_version": 1,
        }
        new_path.parent.mkdir(parents=True, exist_ok=True)
        new_path.write_text(fm.serialize(front, body), encoding="utf-8")
        return OperationResult(
            success=True,
            paths_touched=[new_path],
            summary="ingested web-2026-01-15-abc-v2",
        )

    monkeypatch.setattr("gateway.ops.reingest.ingest", _fake_ingest)

    result = reingest("web-2026-01-15-abc", "https://example.com/v2")

    assert result.success
    old_path = paths.raw_source_path("web", "web-2026-01-15-abc")
    old_front, _ = fm.parse(old_path.read_text())
    assert old_front.get("superseded_by") == "web-2026-01-15-abc-v2"


def test_reingest_stamps_supersedes_on_new_source(kb_root: Path, monkeypatch) -> None:
    _write_raw_source(kb_root, "web-2026-01-15-abc")

    from gateway.core import OperationResult

    new_path = paths.raw_source_path("web", "web-2026-01-15-abc-v2")

    def _fake_ingest(input_path, **kwargs):
        from gateway import validator

        body = "New body content.\n"
        front = {
            "id": "web-2026-01-15-abc-v2",
            "type": "web",
            "title": "New version",
            "url": "https://example.com/v2",
            "authors": ["Test Author"],
            "published_at": "2026-03-01",
            "ingested_at": "2026-03-01T00:00:00Z",
            "content_hash": validator.compute_content_hash(body),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {},
            "schema_version": 1,
        }
        new_path.parent.mkdir(parents=True, exist_ok=True)
        new_path.write_text(fm.serialize(front, body), encoding="utf-8")
        return OperationResult(success=True, paths_touched=[new_path], summary="ok")

    monkeypatch.setattr("gateway.ops.reingest.ingest", _fake_ingest)

    reingest("web-2026-01-15-abc", "https://example.com/v2")

    new_front, _ = fm.parse(new_path.read_text())
    assert "web-2026-01-15-abc" in (new_front.get("supersedes") or [])


def test_reingest_returns_affected_pages(kb_root: Path, monkeypatch) -> None:
    _write_raw_source(kb_root, "web-2026-01-15-abc")
    # Wiki page citing the old source
    synth = kb_root / "wiki" / "synthesis" / "my-analysis.md"
    synth.parent.mkdir(parents=True, exist_ok=True)
    synth.write_text("Claim [[sources/web-2026-01-15-abc]].\n")

    from gateway.core import OperationResult

    new_path = paths.raw_source_path("web", "web-2026-01-15-abc-v2")

    def _fake_ingest(input_path, **kwargs):
        from gateway import validator

        body = "New.\n"
        front = {
            "id": "web-2026-01-15-abc-v2",
            "type": "web",
            "title": "v2",
            "url": "https://example.com/v2",
            "authors": ["A"],
            "published_at": "2026-03-01",
            "ingested_at": "2026-03-01T00:00:00Z",
            "content_hash": validator.compute_content_hash(body),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {},
            "schema_version": 1,
        }
        new_path.parent.mkdir(parents=True, exist_ok=True)
        new_path.write_text(fm.serialize(front, body), encoding="utf-8")
        return OperationResult(success=True, paths_touched=[new_path], summary="ok")

    monkeypatch.setattr("gateway.ops.reingest.ingest", _fake_ingest)

    result = reingest("web-2026-01-15-abc", "https://example.com/v2")

    assert result.success
    affected = (result.data or {}).get("affected_pages", [])
    assert any("my-analysis.md" in p for p in affected)


def test_reingest_result_summary(kb_root: Path, monkeypatch) -> None:
    _write_raw_source(kb_root, "web-2026-01-15-abc")

    from gateway.core import OperationResult

    new_path = paths.raw_source_path("web", "web-2026-01-15-abc-v2")

    def _fake_ingest(input_path, **kwargs):
        from gateway import validator

        body = "New.\n"
        front = {
            "id": "web-2026-01-15-abc-v2",
            "type": "web",
            "title": "v2",
            "url": "https://example.com/v2",
            "authors": ["A"],
            "published_at": "2026-03-01",
            "ingested_at": "2026-03-01T00:00:00Z",
            "content_hash": validator.compute_content_hash(body),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": {},
            "schema_version": 1,
        }
        new_path.parent.mkdir(parents=True, exist_ok=True)
        new_path.write_text(fm.serialize(front, body), encoding="utf-8")
        return OperationResult(success=True, paths_touched=[new_path], summary="ok")

    monkeypatch.setattr("gateway.ops.reingest.ingest", _fake_ingest)

    result = reingest("web-2026-01-15-abc", "https://example.com/v2")

    assert "web-2026-01-15-abc" in result.summary
    assert "web-2026-01-15-abc-v2" in result.summary


# --- superseded_citations lint ------------------------------------------------


def test_superseded_citations_lint_empty_when_no_superseded(kb_root: Path) -> None:
    _write_raw_source(kb_root, "web-2026-01-15-abc")
    findings = superseded_citations.run()
    assert findings == []


def test_superseded_citations_lint_finds_citing_page(kb_root: Path) -> None:
    _write_raw_source(
        kb_root, "web-2026-01-15-abc", superseded_by="web-2026-01-15-abc-v2"
    )
    synth = kb_root / "wiki" / "synthesis" / "my-synth.md"
    synth.parent.mkdir(parents=True, exist_ok=True)
    synth.write_text("Claim [[sources/web-2026-01-15-abc]] from old.\n")

    findings = superseded_citations.run()
    assert len(findings) == 1
    assert findings[0].check == "superseded-citations"
    assert "web-2026-01-15-abc" in findings[0].message
    assert "web-2026-01-15-abc-v2" in findings[0].message


def test_superseded_citations_lint_no_finding_when_not_cited(kb_root: Path) -> None:
    _write_raw_source(
        kb_root, "web-2026-01-15-abc", superseded_by="web-2026-01-15-abc-v2"
    )
    # Wiki page cites the NEW source, not the old
    synth = kb_root / "wiki" / "synthesis" / "my-synth.md"
    synth.parent.mkdir(parents=True, exist_ok=True)
    synth.write_text("Claim [[sources/web-2026-01-15-abc-v2]] from new.\n")

    findings = superseded_citations.run()
    assert findings == []
