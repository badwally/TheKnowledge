"""Tests for wiki_context loader (M50 Phase B)."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway.evaluate.wiki_context import load_wiki_context, ContextTooLargeError


def _write_synthesis(kb_root: Path, slug: str, domain: str,
                     synthesizes: list[str]) -> Path:
    page = kb_root / "wiki" / "synthesis" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(
        {
            "type": "synthesis",
            "slug": slug,
            "title": slug,
            "domains": [domain],
            "synthesizes": synthesizes,
        },
        f"# {slug}\n\nSynthesis body content about {domain}.\n",
    ))
    return page


def _write_raw_source(kb_root: Path, source_id: str, body: str) -> Path:
    raw = kb_root / "raw" / "web" / f"{source_id}.md"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(fm.serialize(
        {"id": source_id, "type": "web", "title": source_id,
         "url": f"https://example.com/{source_id}", "domains": ["test-domain"]},
        body,
    ))
    return raw


def test_loads_domain_synthesis_pages_and_their_sources(kb_root):
    _write_raw_source(kb_root, "web-2026-01-01-aaa", "Source A body content.")
    _write_synthesis(kb_root, "synth-a", "test-domain", ["sources/web-2026-01-01-aaa"])

    ctx = load_wiki_context("test-domain")

    assert "synth-a" in ctx
    assert "Synthesis body content about test-domain" in ctx
    assert "Source A body content" in ctx


def test_excludes_other_domain_pages(kb_root):
    _write_synthesis(kb_root, "wanted", "test-domain", [])
    _write_synthesis(kb_root, "unwanted", "other-domain", [])

    ctx = load_wiki_context("test-domain")

    assert "wanted" in ctx
    assert "unwanted" not in ctx


def test_context_too_large_raises(kb_root):
    page = kb_root / "wiki" / "synthesis" / "huge.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(fm.serialize(
        {"type": "synthesis", "slug": "huge", "title": "h",
         "domains": ["test-domain"], "synthesizes": []},
        "A" * 2_000_000,
    ))

    with pytest.raises(ContextTooLargeError):
        load_wiki_context("test-domain", max_chars=500_000)


def test_concept_and_entity_pages_are_truncated_by_head_lines(kb_root):
    """Concept/entity pages may be plentiful and verbose — load only the
    first N lines of each to keep the prompt bounded."""
    concept = kb_root / "wiki" / "concepts" / "big-concept.md"
    concept.parent.mkdir(parents=True, exist_ok=True)
    body_lines = [f"Line {i} of a long concept page." for i in range(100)]
    concept.write_text(fm.serialize(
        {"type": "concept", "slug": "big-concept", "title": "Big Concept",
         "domains": ["test-domain"]},
        "\n".join(body_lines) + "\n",
    ))

    ctx = load_wiki_context("test-domain")

    assert "Line 0 of a long concept page." in ctx
    # Line 99 should not appear — truncated
    assert "Line 99 of a long concept page." not in ctx


def test_strips_sources_prefix_when_resolving_raw_files(kb_root):
    """`synthesizes:` frontmatter entries are stored as `sources/<id>`;
    raw files live at `raw/<type>/<id>.md` without the prefix. Same
    convention M49 (cite_suggest) had to normalize."""
    sid = "web-2026-02-02-bbb"
    _write_raw_source(kb_root, sid, "Body of source with prefix-handling.")
    _write_synthesis(kb_root, "synth-b", "test-domain", [f"sources/{sid}"])

    ctx = load_wiki_context("test-domain")

    assert "Body of source with prefix-handling" in ctx


def test_empty_domain_returns_empty_string(kb_root):
    """Domain with no pages returns empty context (not an error)."""
    ctx = load_wiki_context("nonexistent-domain")
    assert ctx == ""


def test_source_body_over_cap_is_excluded(kb_root):
    """Source bodies exceeding max_source_body_chars are silently skipped so
    large PDFs or statutory texts don't exhaust the context budget."""
    _write_raw_source(kb_root, "web-small", "Small body content.")
    _write_raw_source(kb_root, "web-large", "X" * 50_000)
    _write_synthesis(kb_root, "synth-c", "test-domain",
                     ["sources/web-small", "sources/web-large"])

    ctx = load_wiki_context("test-domain", max_source_body_chars=30_000)

    assert "Small body content" in ctx
    assert "X" * 100 not in ctx  # large source excluded


def test_source_body_at_cap_boundary_is_included(kb_root):
    """A source body exactly at the cap is included."""
    body = "Y" * 30_000
    _write_raw_source(kb_root, "web-exact", body)
    _write_synthesis(kb_root, "synth-d", "test-domain", ["sources/web-exact"])

    ctx = load_wiki_context("test-domain", max_source_body_chars=30_000)

    assert "Y" * 100 in ctx  # body present


def test_default_cap_filters_very_large_sources(kb_root):
    """Default cap (30k) keeps the context sane for domains with large PDFs."""
    _write_raw_source(kb_root, "web-giant", "Z" * 60_000)
    _write_synthesis(kb_root, "synth-e", "test-domain", ["sources/web-giant"])

    ctx = load_wiki_context("test-domain")

    assert "Z" * 100 not in ctx  # default 30k cap excluded it
