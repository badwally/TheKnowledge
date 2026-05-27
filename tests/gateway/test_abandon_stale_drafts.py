"""M98: abandon_stale_drafts — auto-abandon orphaned stale draft wiki pages."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_NOW = datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_draft(
    kb_root: Path,
    page_type: str,
    slug: str,
    *,
    age_days: int,
    body: str = "## Summary\n\nDraft content.\n\n## Context\n",
) -> Path:
    from gateway import wiki_pages

    schema = wiki_pages.PAGE_SCHEMAS[page_type]
    d = paths.knowledge_root() / schema.directory
    d.mkdir(parents=True, exist_ok=True)
    started = _NOW - timedelta(days=age_days)
    front = {
        "type": page_type,
        "slug": slug,
        "title": slug,
        "domains": ["test"],
        "created_at": _iso(started),
        "last_updated": _iso(started),
        "draft": True,
        "draft_started_at": _iso(started),
        "draft_unresolved_claims": 2,
    }
    if page_type == "concept":
        front["aliases"] = []
    if page_type == "synthesis":
        front["sources_count"] = 0
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


def _write_concept(kb_root: Path, slug: str) -> Path:
    from gateway import wiki_pages

    schema = wiki_pages.PAGE_SCHEMAS["concept"]
    d = paths.knowledge_root() / schema.directory
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": slug,
        "domains": ["test"],
        "aliases": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, "## Summary\n\nContent.\n\n## Context\n"))
    return p


# ---------------------------------------------------------------------------
# Core logic tests
# ---------------------------------------------------------------------------


def test_abandons_old_orphan_draft(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts

    p = _write_draft(kb_root, "concept", "old-orphan", age_days=31)
    assert p.exists()

    result = abandon_stale_drafts(min_age_days=30)

    assert result.success
    assert "1 abandoned" in result.summary
    assert not p.exists()


def test_skips_draft_below_threshold(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts

    p = _write_draft(kb_root, "concept", "fresh-draft", age_days=10)

    result = abandon_stale_drafts(min_age_days=30)

    assert result.success
    assert "0 abandoned" in result.summary
    assert p.exists()


def test_skips_draft_with_inbound_citation(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts

    p = _write_draft(kb_root, "concept", "cited-draft", age_days=31)
    # Another concept that cites the draft
    _write_concept(kb_root, "citing-concept")
    citing = paths.knowledge_root() / "wiki" / "concepts" / "citing-concept.md"
    text = citing.read_text() + "\nSee [[concepts/cited-draft]] for more.\n"
    citing.write_text(text)

    result = abandon_stale_drafts(min_age_days=30)

    assert result.success
    assert "0 abandoned" in result.summary
    assert p.exists()


def test_skips_finalized_pages(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts
    from gateway import wiki_pages

    schema = wiki_pages.PAGE_SCHEMAS["concept"]
    d = paths.knowledge_root() / schema.directory
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": "finalized-page",
        "title": "finalized-page",
        "domains": ["test"],
        "aliases": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "finalized_at": "2026-01-15T00:00:00Z",
    }
    p = d / "finalized-page.md"
    p.write_text(fm.serialize(front, "## Summary\n\nContent.\n\n## Context\n"))

    result = abandon_stale_drafts(min_age_days=30)

    assert p.exists()
    assert "0 abandoned" in result.summary


def test_dry_run_does_not_delete(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts

    p = _write_draft(kb_root, "concept", "dry-run-draft", age_days=31)

    result = abandon_stale_drafts(min_age_days=30, dry_run=True)

    assert result.success
    assert "dry-run" in result.summary
    assert "1 abandoned" in result.summary
    assert p.exists()  # not deleted


def test_skips_draft_missing_started_at(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts
    from gateway import wiki_pages

    schema = wiki_pages.PAGE_SCHEMAS["concept"]
    d = paths.knowledge_root() / schema.directory
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": "no-started-at",
        "title": "no-started-at",
        "domains": ["test"],
        "aliases": [],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "draft": True,
        # draft_started_at intentionally absent
    }
    p = d / "no-started-at.md"
    p.write_text(fm.serialize(front, "## Summary\n\nDraft.\n\n## Context\n"))

    result = abandon_stale_drafts(min_age_days=30)

    assert p.exists()
    assert "0 abandoned" in result.summary


def test_custom_min_age_days(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts

    p_old = _write_draft(kb_root, "concept", "old-enough", age_days=8)
    p_young = _write_draft(kb_root, "concept", "too-young", age_days=5)

    result = abandon_stale_drafts(min_age_days=7)

    assert not p_old.exists()
    assert p_young.exists()
    assert "1 abandoned" in result.summary


def test_abandons_multiple_orphans(kb_root: Path) -> None:
    from gateway.ops.abandon_stale_drafts import abandon_stale_drafts

    p1 = _write_draft(kb_root, "concept", "orphan-a", age_days=35)
    p2 = _write_draft(kb_root, "concept", "orphan-b", age_days=40)

    result = abandon_stale_drafts(min_age_days=30)

    assert result.success
    assert "2 abandoned" in result.summary
    assert not p1.exists()
    assert not p2.exists()


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------


def test_cli_registered() -> None:
    from gateway.cli import SUBCOMMANDS, IMPLEMENTED

    assert "abandon-stale-drafts" in SUBCOMMANDS
    assert "abandon-stale-drafts" in IMPLEMENTED


def test_cli_dry_run_parse() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["abandon-stale-drafts", "--dry-run"])
    assert ns.dry_run is True


def test_cli_min_age_days_parse() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["abandon-stale-drafts", "--min-age-days", "14"])
    assert ns.min_age_days == 14
