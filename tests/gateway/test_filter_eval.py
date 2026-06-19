"""Tests for the `wiki filter-eval` subcommand (ops.filter_eval).

Unit tests only — no live network or model calls. The Mode-1 pool builder's
search + filter seams are dependency-injected; the Mode-2 scorer is pure.
"""

import json

import pytest

from gateway.ops import filter_eval
from gateway.research.adapters.base import CandidateItem


def _yt_candidate(vid, title, channel, desc):
    # Realistic payload: full title/channel/description + source_metadata,
    # matching the real YouTubeAdapter shape (NOT a minimal stub).
    return CandidateItem(
        item_id=f"yt:{vid}",
        source_type="youtube",
        url=f"https://www.youtube.com/watch?v={vid}",
        title=title,
        authors=[channel],
        publish_date="2024-05-01T00:00:00Z",
        description=desc,
        content_type="video",
        source_metadata={"video_id": vid, "channel_name": channel, "view_count": 4200},
    )


class _StubFilterClient:
    """Returns a fixed score keyed by a title substring. No model call.

    gateway.filter.semantic.score() has no call_split on this stub, so it
    falls back to .call(system + "\\n" + user). parse_response() expects a
    JSON object {"score", "rationale"}, so that is what we return.
    """

    def __init__(self, scores_by_title):
        self._scores = scores_by_title

    def call(self, prompt: str) -> str:
        for needle, sc in self._scores.items():
            if needle in prompt:
                return json.dumps({"score": sc, "rationale": f"stub decision for {needle}"})
        return json.dumps({"score": 0.0, "rationale": "stub default"})


def _pool_item(url, score, *, subtopic="kg-construction", title=None, channel="ACME Talks"):
    return {
        "url": url,
        "item_id": "yt:" + url[-4:],
        "title": title or f"Talk {url[-4:]}",
        "channel": channel,
        "description": "A conference talk about knowledge graphs.",
        "subtopic": subtopic,
        "score": score,
        "tier": "accept" if score >= 0.7 else "review" if score >= 0.4 else "reject",
    }


def test_score_pool_precision_and_buckets():
    # 12 candidates, scores descending by url suffix number.
    pool = [_pool_item(f"https://yt/v{i:02d}", 0.95 - i * 0.05) for i in range(12)]
    # User's 10 best-fit: 8 of them are in the filter top-10 (v00..v07 + v10, v11),
    # 2 are outside it (v10, v11 -> filter false-negatives).
    best_fit = [f"https://yt/v{i:02d}" for i in range(8)] + ["https://yt/v10", "https://yt/v11"]
    labels = {"best_fit": best_fit, "missing": {"kg-construction": ["A keynote by X that is absent"]}}

    report = filter_eval.score_pool(pool, labels, k=10)

    assert report["k"] == 10
    assert report["precision_at_k"] == 0.8  # 8 of the user's 10 are in filter top-10
    # filter top-10 = v00..v09; user did NOT pick v08, v09 -> false positives
    fp_urls = {c["url"] for c in report["filter_false_positives"]}
    assert fp_urls == {"https://yt/v08", "https://yt/v09"}
    # user picked v10, v11 which are ranked 11th/12th -> false negatives
    fn_urls = {c["url"] for c in report["filter_false_negatives"]}
    assert fn_urls == {"https://yt/v10", "https://yt/v11"}
    assert report["query_coverage_gaps"] == {"kg-construction": ["A keynote by X that is absent"]}
    assert report["label_warnings"] == []


def test_score_pool_warns_when_best_fit_url_not_in_pool():
    pool = [_pool_item("https://yt/v00", 0.9)]
    labels = {"best_fit": ["https://yt/NOT-IN-POOL"], "missing": {}}
    report = filter_eval.score_pool(pool, labels, k=10)
    assert any("NOT-IN-POOL" in w for w in report["label_warnings"])


def test_score_pool_is_deterministic_under_score_ties():
    # Two candidates tie on score; ranking must break ties by url so the
    # top-k membership is stable (no nondeterministic precision).
    pool = [_pool_item("https://yt/vB", 0.5), _pool_item("https://yt/vA", 0.5)]
    pool += [_pool_item(f"https://yt/p{i}", 0.1) for i in range(20)]
    labels = {"best_fit": ["https://yt/vA"], "missing": {}}
    r1 = filter_eval.score_pool(pool, labels, k=1)
    r2 = filter_eval.score_pool(list(reversed(pool)), labels, k=1)
    assert r1["hits"] == r2["hits"]  # tie-break stable regardless of input order


# --- Task A2: build_pool (Mode-1) -----------------------------------------


def test_build_pool_scores_and_tags_every_candidate():
    # Two subtopics; subtopic A surfaces a strong + a weak video, B a mid one.
    pool_by_subtopic = {
        "kg-construction": [
            _yt_candidate("AAA1", "Building Knowledge Graphs at Scale (KGC keynote)", "KGConf", "Keynote on KG construction pipelines."),
            _yt_candidate("AAA2", "10 SEO tricks for 2024", "GrowthHacks", "Clickbait marketing video."),
        ],
        "query-languages": [
            _yt_candidate("BBB1", "SPARQL 1.2 deep dive (Connected Data London)", "CDL", "Conference talk on SPARQL engines."),
        ],
    }

    def fake_search(queries, *, max_results):
        # The op calls search_fn once per subtopic; route by the query text.
        for sub, items in pool_by_subtopic.items():
            if any(sub in q for q in queries):
                return items
        return []

    stub_client = _StubFilterClient({
        "Building Knowledge Graphs": 0.9,
        "10 SEO tricks": 0.1,
        "SPARQL 1.2": 0.6,
    })

    scored = filter_eval.build_pool(
        "semantic-models",
        {"kg-construction": ["kg-construction talks"], "query-languages": ["query-languages talks"]},
        max_results_per_query=15,
        search_fn=fake_search,
        filter_client=stub_client,
    )

    by_url = {c["url"]: c for c in scored}
    assert len(scored) == 3  # all candidates scored, none dropped
    assert by_url["https://www.youtube.com/watch?v=AAA1"]["subtopic"] == "kg-construction"
    assert by_url["https://www.youtube.com/watch?v=AAA1"]["channel"] == "KGConf"
    assert by_url["https://www.youtube.com/watch?v=AAA1"]["tier"] == "accept"
    assert by_url["https://www.youtube.com/watch?v=AAA2"]["tier"] == "reject"
    assert by_url["https://www.youtube.com/watch?v=BBB1"]["subtopic"] == "query-languages"


def test_build_pool_dedups_across_subtopics_first_subtopic_wins():
    shared = _yt_candidate("DUP1", "Ontology alignment survey (ISWC)", "ISWC", "Survey talk.")

    def fake_search(queries, *, max_results):
        return [shared]  # same video surfaces for every subtopic query

    stub_client = _StubFilterClient({"Ontology alignment": 0.8})
    scored = filter_eval.build_pool(
        "semantic-models",
        {"alignment": ["alignment q"], "ontology-engineering": ["onto q"]},
        search_fn=fake_search,
        filter_client=stub_client,
    )
    assert len(scored) == 1  # deduped by url
    assert scored[0]["subtopic"] == "alignment"  # first subtopic in file order wins


def test_build_pool_raises_when_no_youtube_adapter(monkeypatch):
    # Negative control: the real default search path must fail loudly when
    # the youtube adapter is unavailable, not silently return an empty pool.
    monkeypatch.setattr(filter_eval, "enabled_adapters", lambda **_: [])
    with pytest.raises(filter_eval.FilterEvalError):
        filter_eval.default_youtube_search(["q"], max_results=5)
