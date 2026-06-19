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

from gateway.filter import (
    load_all,
    load_policy,
    policy_exists,
    score as filter_score,
    select,
)
from gateway.filter.policy import Policy
from gateway.filter.semantic import FilterClient, FilterError
from gateway.research.adapters import enabled_adapters
from gateway.research.adapters.base import CandidateItem
from gateway.research.orchestrator import _fan_out_search


class FilterEvalError(RuntimeError):
    """Raised when the eval cannot run (missing adapter, missing policy)."""


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


# --- Mode 1: pool generation ----------------------------------------------


def _tier(score: float, policy: Policy) -> str:
    if score >= policy.threshold_include:
        return "accept"
    if score >= policy.threshold_review:
        return "review"
    return "reject"


def _front(item: CandidateItem, domain: str) -> dict:
    """Frontmatter-shaped dict for the filter prompt (mirrors
    orchestrator._candidate_front so scores match the live pipeline)."""
    return {
        "type": item.source_type,
        "title": item.title,
        "url": item.url,
        "authors": item.authors,
        "published_at": item.publish_date or "",
        "domains": [domain],
        "meta": dict(item.source_metadata or {}),
    }


def _pool_row(item: CandidateItem, subtopic: str, score: float, tier: str) -> dict:
    return {
        "item_id": item.item_id,
        "url": item.url,
        "title": item.title,
        "channel": (item.source_metadata or {}).get("channel_name", "")
                   or (item.authors[0] if item.authors else ""),
        "description": item.description,
        "subtopic": subtopic,
        "score": round(float(score), 4),
        "tier": tier,
    }


def default_youtube_search(
    queries: list[str], *, max_results: int, session_id: str = "filter-eval"
) -> list[CandidateItem]:
    """Real network seam: youtube-only fan-out. Raises if the adapter is gone."""
    adapters = [a for a in enabled_adapters() if a.name == "youtube"]
    if not adapters:
        raise FilterEvalError(
            "youtube adapter unavailable (is YOUTUBE_API_KEY set?)"
        )
    return _fan_out_search(
        adapters,
        {"youtube": queries},
        max_results_per_adapter=max_results,
        session_id=session_id,
    )


def build_pool(
    domain: str,
    queries_by_subtopic: dict[str, list[str]],
    *,
    max_results_per_query: int = 15,
    search_fn=None,
    filter_client: FilterClient | None = None,
) -> list[dict]:
    """Run search per subtopic, dedup across subtopics (first wins), score
    every candidate. Returns the scored pool (the shape score_pool consumes)."""
    if not policy_exists(domain):
        raise FilterEvalError(f"no policy file for domain {domain!r}")
    policy = load_policy(domain)
    examples = select(load_all(domain), policy)
    search = search_fn or default_youtube_search

    seen: set[str] = set()
    tagged: list[tuple[str, CandidateItem]] = []  # (subtopic, item)
    for subtopic, queries in queries_by_subtopic.items():
        items = search(queries, max_results=max_results_per_query)
        for item in items:
            if item.url in seen:
                continue
            seen.add(item.url)
            tagged.append((subtopic, item))

    scored: list[dict] = []
    for subtopic, item in tagged:
        front = _front(item, domain)
        body_head = item.description or item.title
        try:
            result = filter_score(front, body_head, policy, examples, client=filter_client)
        except FilterError:
            # Score failures are recorded as reject-tier with score 0 so the
            # candidate stays visible in the pool rather than vanishing.
            scored.append(_pool_row(item, subtopic, 0.0, "reject"))
            continue
        scored.append(_pool_row(item, subtopic, result.score, _tier(result.score, policy)))
    return scored
