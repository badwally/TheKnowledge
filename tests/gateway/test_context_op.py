"""Tests for the wiki context op (M51 INT-11)."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway.ops.context_op import (
    _resolve_target,
    _walk_neighbors,
    _render_markdown,
    _render_json,
    context_op,
    AmbiguousQueryError,
    NoMatchError,
)


def _write_page(kb_root: Path, kind: str, slug: str, title: str = "",
                body: str = "") -> Path:
    page = kb_root / "wiki" / kind / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(
        {"type": kind.rstrip("s") or kind, "slug": slug,
         "title": title or slug, "domains": ["test-domain"]},
        body or f"# {slug}\n\nBody for {slug}.\n",
    ))
    return page


def test_resolve_target_by_slug_prefixed(kb_root):
    _write_page(kb_root, "entities", "alpha-co")
    p = _resolve_target("entities/alpha-co")
    assert p == kb_root / "wiki" / "entities" / "alpha-co.md"


def test_resolve_target_by_full_path(kb_root):
    _write_page(kb_root, "entities", "alpha-co")
    p = _resolve_target("wiki/entities/alpha-co.md")
    assert p == kb_root / "wiki" / "entities" / "alpha-co.md"


def test_resolve_target_by_title_substring_fallback(kb_root):
    _write_page(kb_root, "entities", "alpha-co", title="Alpha Corporation Inc")
    p = _resolve_target("Alpha Corporation")
    assert p == kb_root / "wiki" / "entities" / "alpha-co.md"


def test_resolve_target_ambiguous_title_raises(kb_root):
    _write_page(kb_root, "entities", "alpha-1", title="Alpha")
    _write_page(kb_root, "entities", "alpha-2", title="Alpha (other)")
    with pytest.raises(AmbiguousQueryError) as excinfo:
        _resolve_target("Alpha")
    assert "alpha-1" in str(excinfo.value)
    assert "alpha-2" in str(excinfo.value)


def test_resolve_target_no_match_raises(kb_root):
    with pytest.raises(NoMatchError):
        _resolve_target("definitely-does-not-exist")


def test_walk_depth_zero_returns_root_only(kb_root):
    root = _write_page(kb_root, "entities", "root-page")
    visited = _walk_neighbors(root, depth=0)
    assert visited == [root]


def test_walk_depth_one_follows_wikilinks(kb_root):
    src = _write_page(kb_root, "sources", "web-2026-01-01-aaa", title="Src",
                      body="# Src\n\nBody.\n")
    other = _write_page(kb_root, "entities", "other-entity", title="Other",
                        body="# Other\n\nBody.\n")
    root = _write_page(
        kb_root, "concepts", "rooty",
        body="# rooty\n\nMentions [[sources/web-2026-01-01-aaa]] and [[entities/other-entity]].\n",
    )

    visited = _walk_neighbors(root, depth=1)
    assert root in visited
    assert src in visited
    assert other in visited


def test_walk_skips_missing_targets(kb_root):
    root = _write_page(
        kb_root, "concepts", "rooty",
        body="# rooty\n\nMentions [[sources/does-not-exist]].\n",
    )
    visited = _walk_neighbors(root, depth=1)
    # Only the root; missing target silently skipped
    assert visited == [root]


def test_walk_avoids_cycles(kb_root):
    a = _write_page(kb_root, "concepts", "a-loop",
                    body="# a\n\n[[concepts/b-loop]]\n")
    b = _write_page(kb_root, "concepts", "b-loop",
                    body="# b\n\n[[concepts/a-loop]]\n")
    visited = _walk_neighbors(a, depth=5)
    # Both visited exactly once
    assert visited.count(a) == 1
    assert visited.count(b) == 1


def test_walk_strips_anchor_and_display_text(kb_root):
    target = _write_page(kb_root, "sources", "web-foo", title="Foo source")
    root = _write_page(
        kb_root, "concepts", "rooty",
        body="# rooty\n\n[[sources/web-foo#para3]] and [[sources/web-foo|Foo Display]].\n",
    )
    visited = _walk_neighbors(root, depth=1)
    assert target in visited
    # Visited once despite two references
    assert visited.count(target) == 1


def test_walk_does_not_follow_nlm_corpus_refs(kb_root):
    root = _write_page(
        kb_root, "synthesis", "rooty",
        body="# rooty\n\n[[nlm:a17f0b4f-ba96-46b0-b4e1-6be759219e89]]\n",
    )
    visited = _walk_neighbors(root, depth=1)
    # Only the root; nlm refs not followed
    assert visited == [root]
