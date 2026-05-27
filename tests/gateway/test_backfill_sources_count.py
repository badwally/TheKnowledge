"""M96: backfill_sources_count — stamp missing sources_count on synthesis pages."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_synthesis(kb_root: Path, slug: str, body: str, sources_count=None) -> Path:
    synth_dir = paths.knowledge_root() / "wiki" / "synthesis"
    synth_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": slug,
        "domains": ["test"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if sources_count is not None:
        front["sources_count"] = sources_count
    p = synth_dir / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_backfill_stamps_missing_sources_count(kb_root: Path) -> None:
    from gateway.ops.backfill_sources_count import backfill_sources_count

    body = "## Synthesis\n\nSome text [[sources/web-abc]] and [[sources/pdf-xyz]].\n"
    _write_synthesis(kb_root, "test-synth", body)

    result = backfill_sources_count()

    assert result.success
    assert "1 updated" in result.summary
    p = paths.knowledge_root() / "wiki" / "synthesis" / "test-synth.md"
    front, _ = fm.parse(p.read_text())
    assert front["sources_count"] == 2


def test_backfill_counts_unique_sources(kb_root: Path) -> None:
    from gateway.ops.backfill_sources_count import backfill_sources_count

    body = "[[sources/web-abc]] [[sources/web-abc]] [[sources/pdf-xyz]]\n"
    _write_synthesis(kb_root, "dup-synth", body)

    backfill_sources_count()

    p = paths.knowledge_root() / "wiki" / "synthesis" / "dup-synth.md"
    front, _ = fm.parse(p.read_text())
    assert front["sources_count"] == 2


def test_backfill_zero_when_no_sources(kb_root: Path) -> None:
    from gateway.ops.backfill_sources_count import backfill_sources_count

    _write_synthesis(kb_root, "empty-synth", "## Synthesis\n\nNo sources here.\n")

    backfill_sources_count()

    p = paths.knowledge_root() / "wiki" / "synthesis" / "empty-synth.md"
    front, _ = fm.parse(p.read_text())
    assert front["sources_count"] == 0


def test_backfill_skips_pages_with_existing_count(kb_root: Path) -> None:
    from gateway.ops.backfill_sources_count import backfill_sources_count

    _write_synthesis(kb_root, "already-counted", "[[sources/web-abc]]\n", sources_count=99)

    result = backfill_sources_count()

    assert "0 updated" in result.summary
    assert "1 skipped" in result.summary
    p = paths.knowledge_root() / "wiki" / "synthesis" / "already-counted.md"
    front, _ = fm.parse(p.read_text())
    assert front["sources_count"] == 99


def test_backfill_dry_run_does_not_write(kb_root: Path) -> None:
    from gateway.ops.backfill_sources_count import backfill_sources_count

    _write_synthesis(kb_root, "dry-synth", "[[sources/web-abc]]\n")

    result = backfill_sources_count(dry_run=True)

    assert "dry-run" in result.summary
    p = paths.knowledge_root() / "wiki" / "synthesis" / "dry-synth.md"
    front, _ = fm.parse(p.read_text())
    assert "sources_count" not in front


def test_backfill_no_synthesis_dir_returns_success(kb_root: Path) -> None:
    from gateway.ops.backfill_sources_count import backfill_sources_count

    result = backfill_sources_count()
    assert result.success


def test_cli_registered(kb_root: Path) -> None:
    from gateway.cli import SUBCOMMANDS, IMPLEMENTED

    assert "backfill-sources-count" in SUBCOMMANDS
    assert "backfill-sources-count" in IMPLEMENTED


def test_cli_dry_run_parse(kb_root: Path) -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["backfill-sources-count", "--dry-run"])
    assert ns.dry_run is True
