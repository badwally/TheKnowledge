"""Evaluation runner orchestrator (M50 Phase E).

Walks goldens for a domain, dispatches each to the Judge (mode B —
wiki-state-only, no new synthesis), accumulates EvalResults into an
EvalRunSummary, persists per-run YAML + appends to trend CSV.

One Judge instance per run so the cached system-prompt prefix benefits
all questions within the 5-minute Anthropic cache TTL.
"""

from __future__ import annotations

from datetime import datetime, timezone

from gateway.evaluate.judge import Judge
from gateway.evaluate.persistence import (
    append_to_trend,
    goldens_path_for,
    write_run,
)
from gateway.evaluate.schema import (
    EvalResult,
    EvalRunSummary,
    load_goldens,
)
from gateway.evaluate.wiki_context import load_wiki_context
from gateway.llm.api_client import AnthropicAPIClient


class NoGoldensError(FileNotFoundError):
    """The domain has no goldens.yaml file. Run `wiki evaluate --scaffold <d>`."""


def run_evaluate(domain: str, *,
                 limit: int | None = None,
                 max_chars: int | None = None,
                 client: AnthropicAPIClient | None = None) -> EvalRunSummary:
    """Run the evaluation for `domain`. Returns an EvalRunSummary (also persisted)."""
    goldens_path = goldens_path_for(domain)
    if not goldens_path.exists():
        raise NoGoldensError(
            f"no goldens at {goldens_path}; run `wiki evaluate --scaffold {domain}`"
        )

    goldens = load_goldens(goldens_path)
    if limit is not None:
        goldens = goldens[:limit]

    ctx_kwargs = {"max_chars": max_chars} if max_chars is not None else {}
    wiki_context = load_wiki_context(domain, **ctx_kwargs)

    judge = Judge(client=client)
    results: list[EvalResult] = []
    for g in goldens:
        result = judge.score(golden=g, wiki_context=wiki_context)
        results.append(result)

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    mean = (sum(r.score for r in results) / len(results)) if results else 0.0
    summary = EvalRunSummary(
        domain=domain,
        timestamp=ts,
        n_questions=len(results),
        mean_score=mean,
        results=results,
        total_input_tokens=sum(r.input_tokens for r in results),
        total_output_tokens=sum(r.output_tokens for r in results),
        total_cache_read_tokens=sum(r.cache_read_tokens for r in results),
    )

    write_run(summary)
    append_to_trend(summary)
    return summary
