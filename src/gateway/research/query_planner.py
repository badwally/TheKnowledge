"""Per-adapter query planner for `wiki research`.

Calls the configured `PlanClient` (Claude) with the research prompt,
domain policy excerpt, adapter manifest, and optional few-shot examples
of past curated plans, and returns a per-adapter list of search queries.

The orchestrator then iterates each adapter's query list at fan-out
time. The plan is persisted via `query_plan_store` so the user can
review or edit it post-hoc; subsequent runs in the same domain pick up
edited plans as few-shot seeds via `recent_edited`.

Backwards compatibility: the orchestrator still accepts a `None`
`plan_client`, in which case query planning is skipped and the prompt
is dispatched verbatim to every adapter (M37 behavior). This module is
only invoked on the new path.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass

from gateway.filter.policy import Policy
from gateway.plan import PlanClient
from gateway.research.query_plan_store import QueryPlan


__all__ = [
    "DEFAULT_TARGET_COUNTS",
    "PlannerError",
    "plan_per_adapter_queries",
]


# Default per-adapter query count. Overridable via `target_counts` on the
# call site. PubMed is small because most domains aren't biomedical;
# the prompt instructs the planner to return [] when not applicable.
DEFAULT_TARGET_COUNTS: dict[str, int] = {
    "youtube": 20,
    "arxiv": 8,
    "web": 15,
    "pubmed": 5,
    "local": 0,  # local-files adapter takes user-supplied paths, not queries
}


_ADAPTER_GUIDANCE: dict[str, str] = {
    "youtube": (
        "short keyword phrases (3-7 words). target authoritative talks: "
        "university lectures and course series, conference keynotes and "
        "seminars, named research labs, and recognized practitioners. anchor "
        "on institutions, events, and speaker names (e.g. Stanford, MIT, "
        "NeurIPS, a named lab or researcher) and named frameworks. avoid "
        "tutorial and vendor-demo phrasing and full sentences."
    ),
    "arxiv": (
        "paper-language phrases. prefer noun phrases like "
        '"X for Y", "Z optimization", or specific technical terms. '
        "avoid product names — they don't appear in titles."
    ),
    "web": (
        "named vendor/blog terms, framework names, deployment patterns, "
        "documentation queries. medium-length (4-10 words)."
    ),
    "pubmed": (
        "biomedical mesh-style terms. return [] if the domain is not "
        "biomedical."
    ),
    "local": (
        "(unused by adapter; ignore — local-files takes paths, not queries)"
    ),
}


_OBJECT_RE = re.compile(r"\{[\s\S]*\}")


class PlannerError(RuntimeError):
    """Raised when the plan_client returns an unparseable or invalid response."""


@dataclass
class PlannerResult:
    """Carries both the queries and the source-of-truth metadata."""

    queries: dict[str, list[str]]
    target_counts: dict[str, int]
    plan_client_model: str | None  # filled when discoverable


def plan_per_adapter_queries(
    prompt: str,
    *,
    domain: str,
    policy: Policy,
    adapter_names: list[str],
    plan_client: PlanClient,
    history_examples: list[QueryPlan] | None = None,
    target_counts: dict[str, int] | None = None,
) -> PlannerResult:
    """Generate per-adapter query lists for one research run.

    `adapter_names` should match the names of the adapters the
    orchestrator will fan out to (e.g. ``["arxiv", "youtube", "web",
    "pubmed"]``). Adapters present here but absent from the planner's
    response yield an empty list.

    `history_examples` are past edited plans for `domain`; the planner
    surfaces up to all of them as good-example seeds. The orchestrator
    is expected to call `query_plan_store.recent_edited(domain, n=...)`
    and pass the result here.

    Raises `PlannerError` on:
      - empty response
      - response that doesn't contain a JSON object
      - JSON object that isn't a mapping
      - any single adapter value that isn't a list of strings
    """
    if not prompt or not prompt.strip():
        raise PlannerError("prompt must be non-empty")
    if not adapter_names:
        raise PlannerError("at least one adapter required")

    counts = {**DEFAULT_TARGET_COUNTS, **(target_counts or {})}
    counts = {a: counts.get(a, 10) for a in adapter_names}

    rendered = _build_prompt(
        prompt=prompt,
        domain=domain,
        policy=policy,
        adapter_names=adapter_names,
        target_counts=counts,
        history_examples=history_examples or [],
    )

    # K5 telemetry: use call_with_usage when available; stubs fall back to call().
    call_with_usage = getattr(plan_client, "call_with_usage", None)
    if callable(call_with_usage):
        from gateway.log import log_llm_call

        result = call_with_usage(rendered)
        log_llm_call("plan_query_planner", result)
        raw = result.text
    else:
        raw = plan_client.call(rendered)
    queries = _parse_response(raw, adapter_names=adapter_names)

    return PlannerResult(
        queries=queries,
        target_counts=counts,
        plan_client_model=None,  # current PlanClient protocol doesn't expose it
    )


# --- prompt construction ---------------------------------------------------


def _build_prompt(
    *,
    prompt: str,
    domain: str,
    policy: Policy,
    adapter_names: list[str],
    target_counts: dict[str, int],
    history_examples: list[QueryPlan],
) -> str:
    inclusion = policy.inclusion_criteria[:8]
    inclusion_block = (
        "\n".join(f"- {c}" for c in inclusion) or "(no inclusion criteria specified)"
    )

    adapter_lines = []
    for adapter in adapter_names:
        guidance = _ADAPTER_GUIDANCE.get(adapter, "(no per-adapter guidance)")
        adapter_lines.append(
            f"- {adapter} (~{target_counts[adapter]} queries): {guidance}"
        )
    adapter_block = "\n".join(adapter_lines)

    few_shot_block = _render_few_shot(history_examples, adapter_names)

    schema_obj = "{\n" + ",\n".join(f'  "{a}": ["...", ...]' for a in adapter_names) + "\n}"

    return _PROMPT_TEMPLATE.format(
        domain=domain,
        topic=policy.domain_topic or "(no topic specified)",
        field=policy.domain_field or "(no field specified)",
        inclusion_block=inclusion_block,
        prompt=prompt.strip(),
        adapter_block=adapter_block,
        few_shot_block=few_shot_block,
        schema_obj=schema_obj,
    )


def _render_few_shot(examples: list[QueryPlan], adapter_names: list[str]) -> str:
    if not examples:
        return "(no curated examples yet for this domain)"
    blocks: list[str] = []
    for i, ex in enumerate(examples, 1):
        lines = [
            f"### Example {i} — past edited plan",
            f"prompt: {ex.prompt.strip()[:300]}",
        ]
        for adapter in adapter_names:
            qs = ex.queries.get(adapter, [])
            if not qs:
                continue
            lines.append(f"{adapter}:")
            for q in qs:
                lines.append(f"  - {q}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


_PROMPT_TEMPLATE = """\
You generate per-adapter search queries for a research orchestrator.
Output JSON only. No prose, no surrounding text, no markdown fences.

# Domain
{domain}: {topic}
{field}

# Inclusion criteria (top items)
{inclusion_block}

# Research prompt
{prompt}

# Adapters and target query counts
{adapter_block}

# Past curated examples for this domain
{few_shot_block}

# Output schema
{schema_obj}
"""


# --- response parsing ------------------------------------------------------


def _parse_response(text: str, *, adapter_names: list[str]) -> dict[str, list[str]]:
    if not text or not text.strip():
        raise PlannerError("plan_client returned empty response")

    cleaned = text.strip()
    # Strip markdown code fences if present.
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    obj = None
    try:
        obj = json.loads(cleaned)
    except json.JSONDecodeError:
        match = _OBJECT_RE.search(cleaned)
        if match:
            try:
                obj = json.loads(match.group(0))
            except json.JSONDecodeError as e:
                raise PlannerError(
                    f"could not parse JSON in plan_client response: {e}"
                ) from e

    if not isinstance(obj, dict):
        raise PlannerError(
            f"plan_client response was not a JSON object: {cleaned[:200]!r}"
        )

    out: dict[str, list[str]] = {}
    for adapter in adapter_names:
        raw_list = obj.get(adapter, [])
        if raw_list is None:
            raw_list = []
        if not isinstance(raw_list, list):
            raise PlannerError(
                f"queries.{adapter} must be a list, got {type(raw_list).__name__}"
            )
        out[adapter] = [str(q).strip() for q in raw_list if str(q).strip()]
    return out
