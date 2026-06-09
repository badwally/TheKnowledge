"""WS1: SQLite FTS5 derived retrieval index tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, search_index


def _wiki_page(
    page_type: str,
    slug: str,
    title: str,
    body: str,
    domain: str = "test-domain",
    aliases: list[str] | None = None,
    draft: bool = False,
    extra: dict | None = None,
) -> Path:
    type_dir = paths.wiki_dir() / f"{page_type}s"
    type_dir.mkdir(parents=True, exist_ok=True)
    p = type_dir / f"{slug}.md"
    front: dict = {
        "type": page_type,
        "slug": slug,
        "title": title,
        "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-05-01T00:00:00Z",
    }
    if aliases:
        front["aliases"] = aliases
    if draft:
        front["draft"] = True
    if extra:
        front.update(extra)
    p.write_text(fm.serialize(front, body))
    return p


def test_refresh_indexes_pages(kb_root: Path):
    _wiki_page("concept", "food-noise", "Food noise", "Intrusive thoughts about food.")
    _wiki_page("entity", "semaglutide", "Semaglutide", "A GLP-1 receptor agonist.")
    stats = search_index.refresh()
    assert stats.indexed == 2
    assert stats.total_pages == 2
    assert search_index.available()


def test_refresh_is_incremental(kb_root: Path):
    _wiki_page("concept", "alpha", "Alpha", "First page.")
    search_index.refresh()
    _wiki_page("concept", "beta", "Beta", "Second page.")
    stats = search_index.refresh()
    assert stats.indexed == 1      # only the new page
    assert stats.unchanged == 1


def test_refresh_removes_deleted(kb_root: Path):
    p = _wiki_page("concept", "gone", "Gone", "Soon deleted.")
    search_index.refresh()
    p.unlink()
    stats = search_index.refresh()
    assert stats.removed == 1
    assert search_index.search_fts("gone") == []


def test_title_match_scores_highest(kb_root: Path):
    _wiki_page("concept", "reward", "Reward blunting", "Discussion of dopamine.")
    hits = search_index.search_fts("reward blunting")
    assert hits
    assert hits[0].score == 3
    assert hits[0].slug == "reward"


def test_body_match_returns_section(kb_root: Path):
    body = "## Mechanism\n\nThe drug delays gastric emptying.\n\n## Effects\n\nWeight loss.\n"
    _wiki_page("entity", "drugx", "Drug X", body)
    hits = search_index.search_fts("gastric emptying")
    assert hits
    assert hits[0].heading == "Mechanism"
    assert "gastric" in hits[0].snippet.lower()


def test_domain_filter(kb_root: Path):
    _wiki_page("concept", "a1", "Shared term one", "content", domain="dom-a")
    _wiki_page("concept", "b1", "Shared term two", "content", domain="dom-b")
    hits = search_index.search_fts("shared term", domain="dom-a")
    assert {h.slug for h in hits} == {"a1"}


def test_page_type_filter(kb_root: Path):
    _wiki_page("concept", "c1", "Typed thing", "content")
    _wiki_page("entity", "e1", "Typed thing", "content")
    hits = search_index.search_fts("typed thing", page_type="entity")
    assert {h.slug for h in hits} == {"e1"}


def test_alias_matches_slug_tier(kb_root: Path):
    _wiki_page("entity", "ozempic", "Ozempic", "Brand name.", aliases=["wegovy"])
    hits = search_index.search_fts("wegovy")
    assert hits
    assert hits[0].slug == "ozempic"


def test_exclude_drafts(kb_root: Path):
    _wiki_page("concept", "draftpage", "Draft term here", "content", draft=True)
    _wiki_page("concept", "finalpage", "Final term here", "content")
    hits = search_index.search_fts("term here", include_drafts=False)
    assert {h.slug for h in hits} == {"finalpage"}


def test_inbound_count_populated(kb_root: Path):
    _wiki_page("concept", "target", "Target page", "Cited often.")
    _wiki_page(
        "synthesis", "citer", "Citer page",
        "See [[concepts/target]] for detail.",
    )
    search_index.refresh()
    hits = search_index.search_fts("target page")
    target = next(h for h in hits if h.slug == "target")
    assert target.inbound_count == 1


def test_rebuild_clears_stale(kb_root: Path):
    _wiki_page("concept", "x", "X term", "content")
    search_index.refresh()
    stats = search_index.refresh(rebuild=True)
    assert stats.indexed == 1
    assert stats.total_pages == 1


def test_top_pages_for_domain_by_inbound(kb_root: Path):
    _wiki_page("concept", "hub", "Hub", "Central concept.", domain="d")
    _wiki_page("entity", "leaf", "Leaf", "[[concepts/hub]] reference.", domain="d")
    search_index.refresh()
    ranked = search_index.top_pages_for_domain("d")
    assert ranked[0] == "wiki/concepts/hub.md"


def test_empty_query_returns_empty(kb_root: Path):
    _wiki_page("concept", "a", "A", "content")
    assert search_index.search_fts("") == []
    assert search_index.search_fts("   ") == []
