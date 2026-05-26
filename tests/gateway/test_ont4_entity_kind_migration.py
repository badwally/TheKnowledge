"""ONT-4: entity_kind backfill migration tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.backfill_entity_kinds import _canonical_kind, backfill_entity_kinds
from gateway.validator import ENTITY_KIND_ENUM


# --- _canonical_kind unit tests ---------------------------------------------


def test_canonical_kind_already_in_enum():
    for kind in ENTITY_KIND_ENUM:
        assert _canonical_kind(kind) == kind


def test_canonical_kind_paper_variants():
    for alias in ("publication", "journal-issue", "journal_issue", "periodical",
                   "article", "preprint", "report", "book"):
        assert _canonical_kind(alias) == "paper", f"Expected 'paper' for {alias!r}"


def test_canonical_kind_statute_variants():
    for alias in ("policy_document", "policy-document", "policy", "regulation", "law", "legislation"):
        assert _canonical_kind(alias) == "statute", f"Expected 'statute' for {alias!r}"


def test_canonical_kind_standard_variants():
    for alias in ("guideline", "guidance", "protocol"):
        assert _canonical_kind(alias) == "standard", f"Expected 'standard' for {alias!r}"


def test_canonical_kind_unknown_falls_back_to_other():
    assert _canonical_kind("some-made-up-kind") == "other"
    assert _canonical_kind("widget") == "other"


# --- backfill_entity_kinds integration tests --------------------------------


def _make_entity(kb_root: Path, slug: str, entity_kind: str) -> Path:
    p = paths.wiki_dir() / "entities" / f"{slug}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "entity",
        "slug": slug,
        "canonical_name": f"Entity {slug}",
        "entity_kind": entity_kind,
        "domains": ["test"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    p.write_text(fm.serialize(front, "## Summary\n\nBody.\n"))
    return p


def test_backfill_skips_valid_kinds(kb_root: Path) -> None:
    _make_entity(kb_root, "drug-a", "drug")
    _make_entity(kb_root, "person-b", "person")
    result = backfill_entity_kinds()
    assert result.success
    assert "2 skipped" in result.summary
    assert "0 updated" in result.summary


def test_backfill_remaps_publication_to_paper(kb_root: Path) -> None:
    p = _make_entity(kb_root, "paper-old", "publication")
    backfill_entity_kinds()
    front, _ = fm.parse(p.read_text())
    assert front["entity_kind"] == "paper"


def test_backfill_remaps_policy_document_to_statute(kb_root: Path) -> None:
    p = _make_entity(kb_root, "policy-old", "policy_document")
    backfill_entity_kinds()
    front, _ = fm.parse(p.read_text())
    assert front["entity_kind"] == "statute"


def test_backfill_remaps_unknown_to_other(kb_root: Path) -> None:
    p = _make_entity(kb_root, "weird-thing", "made-up-kind")
    backfill_entity_kinds()
    front, _ = fm.parse(p.read_text())
    assert front["entity_kind"] == "other"


def test_backfill_is_idempotent(kb_root: Path) -> None:
    p = _make_entity(kb_root, "paper-pub", "publication")
    backfill_entity_kinds()
    backfill_entity_kinds()
    front, _ = fm.parse(p.read_text())
    assert front["entity_kind"] == "paper"


def test_backfill_dry_run_does_not_write(kb_root: Path) -> None:
    p = _make_entity(kb_root, "paper-pub", "publication")
    original_text = p.read_text()
    result = backfill_entity_kinds(dry_run=True)
    assert "(dry-run)" in result.summary
    assert p.read_text() == original_text


def test_backfill_no_entities_dir_returns_success(kb_root: Path) -> None:
    result = backfill_entity_kinds()
    assert result.success


def test_backfill_skips_entity_without_entity_kind(kb_root: Path) -> None:
    p = paths.wiki_dir() / "entities" / "no-kind.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "entity",
        "slug": "no-kind",
        "canonical_name": "No Kind",
        "domains": ["test"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    p.write_text(fm.serialize(front, "Body.\n"))
    result = backfill_entity_kinds()
    assert result.success
    assert "1 skipped" in result.summary


def test_backfill_mixed_batch(kb_root: Path) -> None:
    _make_entity(kb_root, "valid-drug", "drug")
    _make_entity(kb_root, "old-pub", "publication")
    _make_entity(kb_root, "odd-one", "made-up")
    result = backfill_entity_kinds()
    assert result.success
    assert "1 skipped" in result.summary
    assert "2 updated" in result.summary
