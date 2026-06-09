"""WS5: graph-aware authority ranking + co-citation related op."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, search_index
from gateway.ops.retrieve import related_op


def _page(slug: str, title: str, body: str, kind: str = "concept",
          domain: str = "d", draft: bool = False) -> None:
    d = paths.wiki_dir() / f"{kind}s" if kind != "moc" else paths.wiki_dir() / "mocs"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": kind, "slug": slug, "title": title, "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    if draft:
        front["draft"] = True
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def test_authority_lifts_canonical_over_mentions(kb_root: Path):
    # Canonical page: term in title, cited by many others.
    _page("order-block", "Order Block", "## Def\n\nThe canonical order block definition.\n")
    # Mention pages: term only in body, cite the canonical page (giving it authority).
    for i in range(4):
        _page(
            f"mention{i}", f"Strategy {i}",
            f"## S\n\nThis strategy uses an order block [[concepts/order-block]] heavily.\n",
        )
    search_index.refresh(rebuild=True)

    bm25 = search_index.search_fts("order block", scope="wiki", order="bm25")
    auth = search_index.search_fts("order block", scope="wiki", order="authority")
    # Authority must rank the canonical page first; BM25 alone need not.
    assert auth[0].slug == "order-block"


def test_authority_demotes_drafts(kb_root: Path):
    _page("final-x", "Final widget", "## B\n\nwidget content alpha.\n")
    _page("draft-x", "Draft widget", "## B\n\nwidget content alpha alpha alpha.\n", draft=True)
    search_index.refresh(rebuild=True)
    auth = search_index.search_fts("widget content", scope="wiki", order="authority")
    slugs = [h.slug for h in auth]
    # Even though the draft is denser, the finalized page ranks ahead.
    assert slugs.index("final-x") < slugs.index("draft-x")


def test_related_by_shared_citations(kb_root: Path):
    _page("hub-a", "Hub A", "## x\n\ncontent.\n")
    _page("hub-b", "Hub B", "## x\n\ncontent.\n")
    _page("p1", "Page one", "## x\n\n[[concepts/hub-a]] and [[concepts/hub-b]].\n")
    _page("p2", "Page two", "## x\n\n[[concepts/hub-a]] and [[concepts/hub-b]] too.\n")
    _page("p3", "Page three", "## x\n\nonly [[concepts/hub-a]] here.\n")
    search_index.refresh(rebuild=True)

    result = related_op("concepts/p1")
    assert result.success
    rel = {r["slug"]: r["shared"] for r in result.data["related"]}
    # p2 shares 2 targets with p1; p3 shares 1.
    assert rel.get("p2") == 2
    assert rel.get("p3") == 1
    # p2 (more shared) ranks before p3.
    order = [r["slug"] for r in result.data["related"]]
    assert order.index("p2") < order.index("p3")


def test_related_no_links_returns_empty(kb_root: Path):
    _page("lonely", "Lonely page", "## x\n\nno outbound links here.\n")
    search_index.refresh(rebuild=True)
    result = related_op("concepts/lonely")
    assert result.success
    assert result.data["related"] == []


def test_related_unresolved_target(kb_root: Path):
    search_index.refresh(rebuild=True)
    result = related_op("does-not-exist-anywhere")
    assert not result.success


def test_mcp_wiki_related_registered():
    from gateway import mcp_server
    assert hasattr(mcp_server, "wiki_related")


def test_authority_beats_tiered_on_synthetic_set(kb_root: Path):
    """Regression floor: authority ordering must not rank a low-authority
    mention page above the canonical page on a controlled set."""
    _page("canonical", "Widget protocol", "## Def\n\nthe widget protocol spec.\n")
    for i in range(5):
        _page(f"m{i}", f"Note {i}",
              "## n\n\nbrief aside about the widget protocol [[concepts/canonical]].\n")
    search_index.refresh(rebuild=True)
    from gateway.evaluate import retrieval_eval as rev
    goldens = [rev.GoldenQuery(q="widget protocol", expect=["canonical"], domain="d")]
    # search_fts authority order should place canonical first.
    hits = search_index.search_fts("widget protocol", scope="wiki", order="authority")
    assert hits[0].slug == "canonical"
