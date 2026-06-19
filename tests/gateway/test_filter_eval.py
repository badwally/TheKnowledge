"""Tests for the `wiki filter-eval` subcommand (ops.filter_eval).

Unit tests only — no live network or model calls. The Mode-1 pool builder's
search + filter seams are dependency-injected; the Mode-2 scorer is pure.
"""

from gateway.ops import filter_eval


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
