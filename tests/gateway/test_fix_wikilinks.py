"""M97: fix_wikilinks — repair broken wikilinks in wiki pages."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_wiki_page(
    kb_root: Path,
    page_type: str,
    slug: str,
    body: str,
) -> Path:
    from gateway import wiki_pages

    schema = wiki_pages.PAGE_SCHEMAS[page_type]
    d = paths.knowledge_root() / schema.directory
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": page_type,
        "slug": slug,
        "title": slug,
        "domains": ["test"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if page_type == "concept":
        front["aliases"] = []
    if page_type == "synthesis":
        front["sources_count"] = 0
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


# ---------------------------------------------------------------------------
# Core logic tests (fix_body)
# ---------------------------------------------------------------------------


def test_removes_broken_source_link(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import _fix_body

    body = "Some text [[sources/web-does-not-exist]] and more text.\n"
    fixed, removed, downgraded = _fix_body(body, paths.knowledge_root())

    assert removed == 1
    assert downgraded == 0
    assert "[[sources/web-does-not-exist]]" not in fixed


def test_downgrades_broken_entity_link(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import _fix_body

    body = "See [[entities/missing-entity]] for details.\n"
    fixed, removed, downgraded = _fix_body(body, paths.knowledge_root())

    assert removed == 0
    assert downgraded == 1
    assert "[[entities/missing-entity|missing-entity]]" in fixed


def test_downgrades_broken_concept_link(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import _fix_body

    body = "Related: [[concepts/missing-concept]].\n"
    fixed, removed, downgraded = _fix_body(body, paths.knowledge_root())

    assert downgraded == 1
    assert "[[concepts/missing-concept|missing-concept]]" in fixed


def test_skips_existing_target(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import _fix_body

    # Create an entity page so the link resolves
    wiki_dir = paths.knowledge_root() / "wiki" / "entities"
    wiki_dir.mkdir(parents=True, exist_ok=True)
    (wiki_dir / "real-entity.md").write_text("---\ntype: entity\n---\n# Real\n")

    body = "See [[entities/real-entity]] for details.\n"
    fixed, removed, downgraded = _fix_body(body, paths.knowledge_root())

    assert removed == 0
    assert downgraded == 0
    assert "[[entities/real-entity]]" in fixed


def test_skips_aliased_link(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import _fix_body

    body = "See [[entities/missing|display name]] for details.\n"
    fixed, removed, downgraded = _fix_body(body, paths.knowledge_root())

    assert removed == 0
    assert downgraded == 0
    assert "[[entities/missing|display name]]" in fixed


def test_skips_nlm_links(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import _fix_body

    body = "[[nlm:some-uuid-here]] reference.\n"
    fixed, removed, downgraded = _fix_body(body, paths.knowledge_root())

    assert removed == 0
    assert downgraded == 0


def test_deduplicates_same_broken_link(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import _fix_body

    body = "[[sources/dead-src]] text [[sources/dead-src]] again.\n"
    fixed, removed, downgraded = _fix_body(body, paths.knowledge_root())

    assert removed == 1  # counted once despite appearing twice
    assert "sources/dead-src" not in fixed


# ---------------------------------------------------------------------------
# Integration: fix_wikilinks op
# ---------------------------------------------------------------------------


def test_fix_wikilinks_dry_run_no_write(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import fix_wikilinks

    p = _write_wiki_page(
        kb_root, "concept", "test-concept",
        "## Summary\n\nSee [[sources/ghost-source]].\n\n## Context\n"
    )
    original = p.read_text()

    result = fix_wikilinks(dry_run=True)

    assert "dry-run" in result.summary
    assert p.read_text() == original


def test_fix_wikilinks_removes_source_on_write(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import fix_wikilinks

    p = _write_wiki_page(
        kb_root, "concept", "w-concept",
        "## Summary\n\nSee [[sources/ghost]].\n\n## Context\n"
    )

    result = fix_wikilinks()

    assert result.success
    _, body = fm.parse(p.read_text())
    assert "[[sources/ghost]]" not in body


def test_fix_wikilinks_downgrades_entity_link(kb_root: Path) -> None:
    from gateway.ops.fix_wikilinks import fix_wikilinks

    p = _write_wiki_page(
        kb_root, "concept", "e-concept",
        "## Summary\n\nSee [[entities/ghost-ent]].\n\n## Context\n"
    )

    fix_wikilinks()

    _, body = fm.parse(p.read_text())
    assert "[[entities/ghost-ent|ghost-ent]]" in body


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------


def test_cli_registered() -> None:
    from gateway.cli import SUBCOMMANDS, IMPLEMENTED

    assert "fix-wikilinks" in SUBCOMMANDS
    assert "fix-wikilinks" in IMPLEMENTED


def test_cli_dry_run_parse() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["fix-wikilinks", "--dry-run"])
    assert ns.dry_run is True
