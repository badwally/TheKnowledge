"""WS4: retrieval eval harness correctness + FTS-beats-grep on paraphrases."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, search_index
from gateway.evaluate import retrieval_eval as rev


def _page(slug: str, title: str, body: str, domain: str = "d") -> None:
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": title,
        "domains": [domain],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-05-01T00:00:00Z",
    }
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def _seed(kb_root: Path) -> None:
    _page(
        "fair-value-gap", "Fair Value Gap",
        "An imbalance gap in candlestick price left by aggressive orders.",
    )
    _page(
        "order-block", "Order Block",
        "An institutional order block marks where price action originated.",
    )
    _page("noise", "Unrelated", "Totally unrelated filler content about cats.")
    search_index.refresh(rebuild=True)


def test_recall_and_mrr_math():
    rep = rev.EvalReport(retriever="fts")
    rep.results = [
        rev.QueryResult("q1", ["a"], ["a", "b"], best_rank=1),
        rev.QueryResult("q2", ["c"], ["x", "y", "c"], best_rank=3),
        rev.QueryResult("q3", ["z"], ["x", "y"], best_rank=None),
    ]
    assert rep.recall_at(1) == pytest.approx(1 / 3)
    assert rep.recall_at(5) == pytest.approx(2 / 3)
    assert rep.mrr == pytest.approx((1.0 + 1 / 3 + 0.0) / 3)
    assert len(rep.misses_at(5)) == 1


def test_fts_finds_paraphrase_that_grep_misses(kb_root: Path):
    _seed(kb_root)
    goldens = [
        rev.GoldenQuery(q="imbalance gap in candlestick price", expect=["fair-value-gap"], domain="d"),
        rev.GoldenQuery(q="institutional order block price action", expect=["order-block"], domain="d"),
    ]
    fts = rev.evaluate("fts", goldens=goldens, k=5)
    grep = rev.evaluate("grep", goldens=goldens, k=5)
    # Paraphrase queries: FTS recalls, literal-substring grep cannot.
    assert fts.recall_at(5) > grep.recall_at(5)
    assert fts.recall_at(5) == 1.0


def test_load_goldens_roundtrip(kb_root: Path, tmp_path: Path):
    p = tmp_path / "g.yaml"
    p.write_text(
        "queries:\n"
        "  - q: 'one'\n    expect: solo-slug\n"
        "  - q: 'two'\n    domain: d\n    expect: [a, b]\n"
    )
    gs = rev.load_goldens(p)
    assert gs[0].expect == ["solo-slug"]
    assert gs[1].domain == "d" and gs[1].expect == ["a", "b"]


def test_evaluate_handles_no_match(kb_root: Path):
    _seed(kb_root)
    goldens = [rev.GoldenQuery(q="quantum chromodynamics", expect=["nonexistent"], domain="d")]
    rep = rev.evaluate("fts", goldens=goldens, k=5)
    assert rep.recall_at(5) == 0.0
    assert rep.mrr == 0.0
