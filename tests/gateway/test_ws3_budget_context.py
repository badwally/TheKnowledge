"""WS3: budget-aware wiki context."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, search_index
from gateway.ops.context_op import context_op


def _page(slug: str, title: str, body: str, kind: str = "concept",
          domain: str = "d") -> None:
    d = paths.wiki_dir() / f"{kind}s"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": kind, "slug": slug, "title": title, "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def _seed_root_with_neighbors(kb_root: Path) -> None:
    links = " ".join(f"[[concepts/n{i}]]" for i in range(5))
    _page("root", "Root page", f"## Body\n\nroot content. {links}\n")
    for i in range(5):
        _page(f"n{i}", f"Neighbor {i}", "## B\n\n" + ("filler " * 300) + "\n")
    search_index.refresh(rebuild=True)


def test_no_budget_returns_full(kb_root: Path):
    _seed_root_with_neighbors(kb_root)
    result = context_op("concepts/root", caller="t")
    assert result.success
    # All 6 pages present, untruncated.
    assert "[truncated for budget]" not in result.summary
    assert result.summary.count("## ") >= 6


def test_budget_truncates_under_pressure(kb_root: Path):
    _seed_root_with_neighbors(kb_root)
    result = context_op("concepts/root", caller="t", budget=2500)
    assert result.success
    assert len(result.summary) <= 2500 + 500  # last block may overshoot slightly
    assert "[truncated for budget]" in result.summary


def test_budget_above_size_returns_full(kb_root: Path):
    _seed_root_with_neighbors(kb_root)
    result = context_op("concepts/root", caller="t", budget=10_000_000)
    assert "[truncated for budget]" not in result.summary


def test_budget_keeps_root_first(kb_root: Path):
    _seed_root_with_neighbors(kb_root)
    result = context_op("concepts/root", caller="t", budget=1500)
    # Root rendered first, before any neighbor.
    assert result.summary.startswith("## wiki/concepts/root.md")


def test_budget_ranks_higher_authority_neighbor_first(kb_root: Path):
    # Root links 3 neighbors; one of them is cited by many others (high authority).
    _page("root", "Root", "## B\n\n[[concepts/hi]] [[concepts/lo1]] [[concepts/lo2]]\n")
    _page("hi", "High authority", "## B\n\n" + ("alpha " * 200) + "\n")
    _page("lo1", "Low one", "## B\n\n" + ("beta " * 200) + "\n")
    _page("lo2", "Low two", "## B\n\n" + ("gamma " * 200) + "\n")
    # Give "hi" inbound authority.
    for i in range(4):
        _page(f"citer{i}", f"Citer {i}", "## B\n\nsee [[concepts/hi]].\n")
    search_index.refresh(rebuild=True)
    result = context_op("concepts/root", caller="t", budget=2000)
    # Under tight budget, the high-authority neighbor is kept before low ones.
    assert "concepts/hi.md" in result.summary
    pos_hi = result.summary.find("concepts/hi.md")
    pos_lo1 = result.summary.find("concepts/lo1.md")
    if pos_lo1 != -1:
        assert pos_hi < pos_lo1


def test_budget_rejects_nonpositive(kb_root: Path):
    _seed_root_with_neighbors(kb_root)
    result = context_op("concepts/root", caller="t", budget=0)
    assert not result.success


def test_budget_ignored_for_json(kb_root: Path):
    _seed_root_with_neighbors(kb_root)
    result = context_op("concepts/root", caller="t", fmt="json", budget=100)
    assert result.success
    # JSON still includes all neighbors (budget does not apply).
    import json
    data = json.loads(result.summary)
    assert len(data["neighbors"]) == 5
