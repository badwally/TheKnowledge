"""`wiki filter-eval` — score a candidate pool against human gold labels.

Two modes:
  pool  — run YouTube search + per-candidate filter scoring (no transcript
          fetch, no writes to raw/ or wiki/); emit a blind pool (for the
          user to label) + a scored pool (for analysis).
  score — pure function over the scored pool + the user's labels; report
          precision@k and the three disagreement buckets.

Vertical-agnostic: domain is always a parameter, never hardcoded.
"""

from __future__ import annotations


def score_pool(scored_pool: list[dict], labels: dict, *, k: int = 10) -> dict:
    """Pure: precision@k + disagreement buckets. No I/O, no network.

    `scored_pool` items need at least {"url", "score"}; `labels` is
    {"best_fit": [url, ...], "missing": {subtopic: [str, ...]}}.
    Join key between labels and pool is the canonical `url`.
    """
    best_fit = list(labels.get("best_fit") or [])
    best_fit_set = set(best_fit)
    missing = labels.get("missing") or {}

    pool_urls = {c["url"] for c in scored_pool}
    label_warnings: list[str] = []
    for url in best_fit:
        if url not in pool_urls:
            label_warnings.append(
                f"best_fit url not present in scored pool (label error?): {url}"
            )
    if len(best_fit) != k:
        label_warnings.append(
            f"best_fit has {len(best_fit)} entries; precision@{k} denominator is {k}"
        )

    # Deterministic ranking: score desc, tie-break url asc.
    ranked = sorted(scored_pool, key=lambda c: (-float(c["score"]), c["url"]))
    top_k = ranked[:k]
    top_k_urls = {c["url"] for c in top_k}

    hits = best_fit_set & top_k_urls
    precision_at_k = len(hits) / k if k else 0.0

    false_positives = [c for c in top_k if c["url"] not in best_fit_set]
    false_negatives = [
        c for c in scored_pool
        if c["url"] in best_fit_set and c["url"] not in top_k_urls
    ]

    return {
        "precision_at_k": precision_at_k,
        "k": k,
        "hits": sorted(hits),
        "filter_false_positives": false_positives,
        "filter_false_negatives": false_negatives,
        "query_coverage_gaps": missing,
        "label_warnings": label_warnings,
    }
