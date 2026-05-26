"""ONT-6: timestamp backfill op tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.backfill_timestamps import backfill_timestamps


# --- helpers ----------------------------------------------------------------


def _make_page(
    kb_root: Path,
    page_type: str,
    slug: str,
    *,
    with_created: bool = True,
    with_updated: bool = True,
) -> Path:
    type_dirs = {"entity": "entities", "concept": "concepts", "synthesis": "synthesis"}
    d = paths.wiki_dir() / type_dirs[page_type]
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"

    front: dict = {"type": page_type, "slug": slug, "domains": ["test"]}
    if page_type == "entity":
        front["canonical_name"] = f"Entity {slug}"
        front["entity_kind"] = "drug"
    elif page_type == "concept":
        front["canonical_name"] = f"Concept {slug}"
    elif page_type == "synthesis":
        front["title"] = f"Synthesis {slug}"
        front["question"] = "What is X?"
        front["sources_count"] = 0

    if with_created:
        front["created_at"] = "2026-01-01T00:00:00Z"
    if with_updated:
        front["last_updated"] = "2026-01-01T00:00:00Z"

    p.write_text(fm.serialize(front, "Body.\n"))
    return p


# --- unit tests -------------------------------------------------------------


def test_backfill_skips_pages_with_both_timestamps(kb_root: Path) -> None:
    _make_page(kb_root, "entity", "has-both")
    result = backfill_timestamps()
    assert result.success
    assert "1 skipped" in result.summary
    assert "0 updated" in result.summary


def test_backfill_stamps_missing_created_at(kb_root: Path) -> None:
    p = _make_page(kb_root, "entity", "missing-created", with_created=False)
    backfill_timestamps()
    front, _ = fm.parse(p.read_text())
    assert front.get("created_at")
    # Should be a valid ISO-8601 string
    from datetime import datetime
    datetime.fromisoformat(front["created_at"].replace("Z", "+00:00"))


def test_backfill_stamps_missing_last_updated(kb_root: Path) -> None:
    p = _make_page(kb_root, "concept", "missing-updated", with_updated=False)
    backfill_timestamps()
    front, _ = fm.parse(p.read_text())
    assert front.get("last_updated")


def test_backfill_stamps_both_when_both_missing(kb_root: Path) -> None:
    p = _make_page(kb_root, "synthesis", "missing-both", with_created=False, with_updated=False)
    backfill_timestamps()
    front, _ = fm.parse(p.read_text())
    assert front.get("created_at")
    assert front.get("last_updated")


def test_backfill_preserves_existing_created_at(kb_root: Path) -> None:
    p = _make_page(kb_root, "entity", "keep-created", with_updated=False)
    backfill_timestamps()
    front, _ = fm.parse(p.read_text())
    assert front["created_at"] == "2026-01-01T00:00:00Z"


def test_backfill_handles_all_three_page_types(kb_root: Path) -> None:
    _make_page(kb_root, "entity", "e1", with_created=False)
    _make_page(kb_root, "concept", "c1", with_created=False)
    _make_page(kb_root, "synthesis", "s1", with_created=False)
    result = backfill_timestamps()
    assert result.success
    assert "3 updated" in result.summary


def test_backfill_skips_non_targeted_types(kb_root: Path) -> None:
    # source pages should not be touched
    source_dir = paths.wiki_dir() / "sources"
    source_dir.mkdir(parents=True, exist_ok=True)
    source_p = source_dir / "src-001.md"
    source_p.write_text("---\ntype: source\nsource_id: src-001\nsource_type: web\ntitle: T\ningested_at: '2026-01-01T00:00:00Z'\n---\nBody.\n")
    result = backfill_timestamps()
    assert result.success
    assert "0 updated" in result.summary


def test_backfill_is_idempotent(kb_root: Path) -> None:
    p = _make_page(kb_root, "entity", "idempotent", with_created=False)
    backfill_timestamps()
    front_after_first, _ = fm.parse(p.read_text())
    backfill_timestamps()
    front_after_second, _ = fm.parse(p.read_text())
    assert front_after_first["created_at"] == front_after_second["created_at"]
    assert front_after_first["last_updated"] == front_after_second["last_updated"]


def test_backfill_dry_run_does_not_write(kb_root: Path) -> None:
    p = _make_page(kb_root, "entity", "dry-run-test", with_created=False)
    original_text = p.read_text()
    result = backfill_timestamps(dry_run=True)
    assert "(dry-run)" in result.summary
    assert p.read_text() == original_text


def test_backfill_empty_wiki_returns_success(kb_root: Path) -> None:
    result = backfill_timestamps()
    assert result.success
    assert "0 updated" in result.summary


def test_backfill_summary_shows_skipped_and_updated(kb_root: Path) -> None:
    _make_page(kb_root, "entity", "complete", with_created=True, with_updated=True)
    _make_page(kb_root, "concept", "incomplete", with_created=False, with_updated=False)
    result = backfill_timestamps()
    assert "1 updated" in result.summary
    assert "1 skipped" in result.summary
