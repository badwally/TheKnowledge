"""Tests for the wiki context op (M51 INT-11)."""

from __future__ import annotations

import json
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


def test_resolve_target_by_canonical_name(kb_root):
    # Concept and entity pages use canonical_name, not title.
    page = kb_root / "wiki" / "concepts" / "long-covid.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(
        {"type": "concept", "slug": "long-covid",
         "canonical_name": "Long COVID", "domains": ["health"]},
        "# Long COVID\n\nBody.\n",
    ))
    p = _resolve_target("Long COVID")
    assert p == page


def test_resolve_target_slug_with_spaces(kb_root):
    # "long covid" (spaces) should resolve to concepts/long-covid.md via
    # slug normalisation before the expensive title-scan.
    page = kb_root / "wiki" / "concepts" / "long-covid.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(
        {"type": "concept", "slug": "long-covid",
         "canonical_name": "Long COVID", "domains": ["health"]},
        "# Long COVID\n\nBody.\n",
    ))
    p = _resolve_target("long covid")
    assert p == page


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


def test_render_markdown_emits_one_section_per_page(kb_root):
    a = _write_page(kb_root, "entities", "a-ent", body="# A\n\nBody A.\n")
    b = _write_page(kb_root, "sources", "src-x", body="# X\n\nBody X.\n")
    text = _render_markdown([a, b])
    assert "wiki/entities/a-ent.md" in text
    assert "wiki/sources/src-x.md" in text
    assert "Body A" in text
    assert "Body X" in text


def test_render_json_returns_structured_envelope(kb_root):
    a = _write_page(kb_root, "entities", "a-ent", title="Alpha", body="# A\n\nBody A.\n")
    b = _write_page(kb_root, "sources", "src-x", title="Src X", body="# X\n\nBody X.\n")
    blob = _render_json([a, b])
    data = json.loads(blob)
    assert data["root"]["path"].endswith("entities/a-ent.md")
    assert data["root"]["slug"] == "a-ent"
    assert len(data["neighbors"]) == 1
    assert data["neighbors"][0]["slug"] == "src-x"


def test_context_op_requires_caller(kb_root):
    result = context_op("anything")
    assert not result.success
    assert "caller" in (result.errors[0]).lower()


def test_context_op_rejects_invalid_format(kb_root):
    _write_page(kb_root, "entities", "e1")
    result = context_op("entities/e1", caller="test", fmt="yaml")
    assert not result.success
    assert "format" in (result.errors[0]).lower()


def test_context_op_returns_markdown_summary_for_a_page(kb_root):
    _write_page(kb_root, "entities", "alpha-co", title="Alpha", body="# Alpha\n\nDetails.\n")
    result = context_op("entities/alpha-co", caller="test-caller")
    assert result.success
    assert "Alpha" in result.summary
    assert "Details" in result.summary


def test_context_op_logs_caller(kb_root):
    _write_page(kb_root, "entities", "alpha-co")
    context_op("entities/alpha-co", caller="chief-of-staff")
    log_text = (kb_root / "log.md").read_text()
    assert "caller='chief-of-staff'" in log_text or 'caller="chief-of-staff"' in log_text
