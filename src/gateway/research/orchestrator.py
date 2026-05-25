"""`wiki research <prompt>` — corpus-constructive research orchestrator.

Wires the existing pieces together:

  adapters → semantic filter → converters → NotebookLM session →
  analysis (taxonomy / per-branch / cross-cutting) → wiki Plan →
  promote-into-persistent

Every meaningful step calls `log.append("research", fields={"session_id": ..., "step": ...}, summary=...)`
so a whole run is grep-able by session id from `log.md`.

Failures in steps 8-16 trigger `session.abandon` so the registry has
forensic state for the operator. Failures in steps 1-7 short-circuit
before any NotebookLM resource is created.

This module performs no direct writes to `wiki/` or `raw/` — sources go
through the existing `write_atomic` helpers, wiki pages go through
`apply_plan`. CLAUDE.md hard rule #1.
"""

from __future__ import annotations

import concurrent.futures as _futures
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING

from gateway import converters, frontmatter as fm
from gateway import log, nlm_registry, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter import policy as _policy
from gateway.filter.semantic import (
    FilterClient,
    FilterError,
    build_system_prompt as _build_filter_system_prompt,
    score as filter_score,
)
from gateway.filter import load_all as _load_examples, select as _select_examples
from gateway.locking import file_lock
from gateway.ops.apply_plan import apply_plan
from gateway.plan import Plan, PlanClient, WikiUpdate
from gateway.research import query_plan_store as _qp_store
from gateway.research import query_planner as _query_planner
from gateway.research import session as _session
from gateway.research import source_map as _source_map
from gateway.research.adapters import (
    CandidateItem,
    SearchAdapter,
    enabled_adapters,
)
from gateway.research.adapters.base import AdapterError

# `analysis` is shipped by a parallel agent; gate the import so this
# module loads (and its skeleton tests run) even when analysis isn't
# present yet. Without it, step 12 raises a clear error and the
# orchestrator marks the session abandoned.
try:
    from gateway.research import analysis as _analysis  # type: ignore[attr-defined]
except ImportError:  # pragma: no cover — defensive; analysis lands alongside
    _analysis = None  # type: ignore[assignment]

if TYPE_CHECKING:
    from gateway.nlm_client import NlmClient


__all__ = ["research"]


# --- domain inference -------------------------------------------------------


_DOMAIN_INFERENCE_PROMPT = """\
You are routing a research prompt to one of the registered domain slugs.
Respond with EXACTLY one slug from the list below — no surrounding text,
no explanation. If none of the slugs is a reasonable match, respond with
the literal string `none`.

## Registered domain slugs

{slug_list}

## Research prompt

{prompt}
"""


def _registered_domain_slugs() -> list[str]:
    """List domain slugs that have a policy file on disk."""
    pols = paths.policies_dir()
    if not pols.is_dir():
        return []
    return sorted(
        d.name
        for d in pols.iterdir()
        if d.is_dir() and (d / "policy.yaml").exists()
    )


def _infer_domain(prompt: str, plan_client: PlanClient | None) -> str | None:
    """Use a plan client to pick a registered domain slug for `prompt`."""
    if plan_client is None:
        return None
    slugs = _registered_domain_slugs()
    if not slugs:
        return None
    formatted = _DOMAIN_INFERENCE_PROMPT.format(
        slug_list="\n".join(f"- {s}" for s in slugs),
        prompt=prompt,
    )
    # K5 telemetry: this is a tiny one-shot call but recording it gives
    # complete coverage across all Anthropic invocations.
    call_with_usage = getattr(plan_client, "call_with_usage", None)
    try:
        if callable(call_with_usage):
            from gateway.log import log_llm_call

            result = call_with_usage(formatted)
            log_llm_call("plan_domain_inference", result)
            raw = result.text.strip()
        else:
            raw = plan_client.call(formatted).strip()
    except Exception:  # noqa: BLE001 — agent failure is non-fatal
        return None
    candidate = raw.split()[0].strip().strip("`").strip(".") if raw else ""
    if candidate in slugs:
        return candidate
    return None


# --- candidate handling -----------------------------------------------------


@dataclass
class _MaterializedSource:
    """An accepted candidate that has been written to `raw/`."""

    item: CandidateItem
    raw_path: str           # canonical relative form, e.g. "raw/web/<slug>"
    front: dict
    score: float


def _fan_out_search(
    adapters: list[SearchAdapter],
    query_plan: dict[str, list[str]],
    *,
    max_results_per_adapter: int,
    session_id: str,
) -> list[CandidateItem]:
    """Run every adapter in a thread pool; merge results, dedup by URL.

    `query_plan` maps adapter name → list of search queries. Each adapter
    is invoked once per query; per-query result cap is computed so the
    aggregate stays under `max_results_per_adapter`. The local-files
    adapter ignores the query string (it enumerates user-supplied paths)
    and is invoked exactly once if present, regardless of plan.

    A single adapter raising `AdapterError` (or any other exception) is
    logged to stderr + log.md and dropped — the rest of the run
    continues. This matches the SearchAdapter docstring contract.
    """
    if not adapters:
        return []

    work: list[tuple[SearchAdapter, list[str], int]] = []
    for adapter in adapters:
        if adapter.name == "local":
            # local enumerates paths; the query is unused. One call.
            work.append((adapter, [""], max_results_per_adapter))
            continue
        queries = query_plan.get(adapter.name, [])
        if not queries:
            log.append(
                "research",
                fields={
                    "session_id": session_id,
                    "step": "search",
                    "adapter": adapter.name,
                    "n": 0,
                },
                summary=f"adapter {adapter.name} skipped (no queries in plan)",
            )
            continue
        per_query = max(5, max_results_per_adapter // len(queries))
        work.append((adapter, queries, per_query))

    if not work:
        return []

    candidates: list[CandidateItem] = []
    with _futures.ThreadPoolExecutor(max_workers=max(1, len(work))) as pool:
        future_to_adapter = {
            pool.submit(_safe_search, adapter, queries, per_query): adapter
            for adapter, queries, per_query in work
        }
        for fut in _futures.as_completed(future_to_adapter):
            adapter = future_to_adapter[fut]
            try:
                items = fut.result()
            except Exception as e:  # noqa: BLE001
                _emit_step_error(session_id, "search", adapter.name, str(e))
                continue
            log.append(
                "research",
                fields={
                    "session_id": session_id,
                    "step": "search",
                    "adapter": adapter.name,
                    "n": len(items),
                },
                summary=f"adapter {adapter.name} returned {len(items)} candidates",
            )
            candidates.extend(items)

    # URL-keyed dedup; first wins.
    seen: set[str] = set()
    unique: list[CandidateItem] = []
    for item in candidates:
        key = item.url or f"{item.source_type}:{item.item_id}"
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def _safe_search(
    adapter: SearchAdapter,
    queries: list[str],
    per_query_max: int,
) -> list[CandidateItem]:
    """Iterate `queries` against one adapter. Reraises on adapter failure."""
    out: list[CandidateItem] = []
    for q in queries:
        out.extend(adapter.search(q, max_results=per_query_max))
    return out


# --- filter -----------------------------------------------------------------


_FILTER_MAX_WORKERS = int(os.environ.get("WIKI_FILTER_MAX_WORKERS", "8"))


def _run_filter(
    candidates: list[CandidateItem],
    *,
    domain: str,
    policy: _policy.Policy,
    trust_local: bool,
    filter_client: FilterClient | None,
    session_id: str,
    max_workers: int | None = None,
) -> list[tuple[CandidateItem, float]]:
    """Score every candidate in parallel; keep only those clearing `threshold_include`.

    `trust_local=True` waves through items with `source_type == "local"`
    or `file://` URLs without a model call. Useful for pre-vetted local
    archives the user is folding into a search.

    M44.1: each candidate's filter call runs in its own `ThreadPoolExecutor`
    worker so 100+ candidates don't serialize at ~15–45s per Haiku call.
    Defaults to 8 workers (set via `WIKI_FILTER_MAX_WORKERS`); turn down if
    you hit Max-plan rate limits. Accepted candidates are returned in the
    same order as `candidates` to keep logging and downstream behaviour
    deterministic.
    """
    examples = _select_examples(_load_examples(domain), policy)
    # TOK-3: build once for the whole batch — policy+examples are identical
    # across all candidates in this run, so N candidates → 1 build, not N.
    prebuilt_system = _build_filter_system_prompt(policy, examples)
    scores: list[float | None] = [None] * len(candidates)
    workers = max(1, max_workers if max_workers is not None else _FILTER_MAX_WORKERS)

    def _score_one(idx: int, item: CandidateItem) -> tuple[int, float | None]:
        if trust_local and _is_local(item):
            return idx, 1.0
        front = _candidate_front(item, domain)
        body_head = item.description or item.title
        try:
            result = filter_score(
                front, body_head, policy, examples,
                client=filter_client,
                _prebuilt_system=prebuilt_system,
            )
        except FilterError as e:
            _emit_step_error(session_id, "filter", item.url, str(e))
            return idx, None
        return idx, result.score

    if not candidates:
        return []

    with _futures.ThreadPoolExecutor(max_workers=min(workers, len(candidates))) as pool:
        futures = [pool.submit(_score_one, i, item) for i, item in enumerate(candidates)]
        for fut in _futures.as_completed(futures):
            idx, score = fut.result()
            scores[idx] = score

    return [
        (candidates[i], score)
        for i, score in enumerate(scores)
        if score is not None and score >= policy.threshold_include
    ]


def _is_local(item: CandidateItem) -> bool:
    return item.source_type == "local" or item.url.startswith("file://")


def _candidate_front(item: CandidateItem, domain: str) -> dict:
    """Build a frontmatter-shaped dict so the filter prompt has structure."""
    return {
        "type": item.source_type,
        "title": item.title,
        "url": item.url,
        "authors": item.authors,
        "published_at": item.publish_date or "",
        "domains": [domain],
        "meta": dict(item.source_metadata or {}),
    }


# --- materialization --------------------------------------------------------


def _materialize(
    accepted: list[tuple[CandidateItem, float]],
    *,
    session_id: str,
) -> list[_MaterializedSource]:
    """Run each accepted candidate through the converter family; write raw/.

    Failures are logged and the candidate is dropped; this is the same
    posture the rest of the gateway takes (one bad source shouldn't sink
    a whole batch).
    """
    out: list[_MaterializedSource] = []
    for item, score in accepted:
        # Local-files adapter emits `file://<absolute-path>`; converters
        # take a filesystem path, so unwrap before dispatch.
        convert_target = item.url
        if convert_target.startswith("file://"):
            convert_target = convert_target[len("file://"):]

        try:
            converter = converters.dispatch(convert_target)
        except converters.NoConverterError as e:
            _emit_step_error(session_id, "convert", item.url, str(e))
            continue
        try:
            text = converter.convert(convert_target)
        except converters.ConversionError as e:
            _emit_step_error(session_id, "convert", item.url, str(e))
            continue

        try:
            front, _body = fm.parse(text)
        except fm.FrontmatterError as e:
            _emit_step_error(session_id, "convert", item.url, str(e))
            continue

        source_id = front.get("id")
        source_type = front.get("type")
        if not source_id or not source_type:
            _emit_step_error(
                session_id,
                "convert",
                item.url,
                "converter output missing id/type frontmatter",
            )
            continue

        raw_path = paths.raw_source_path(str(source_type), str(source_id))
        # Write the filter score into the frontmatter before persisting.
        front["filter"] = {"score": round(score, 3)}
        text = fm.serialize(front, _body)

        # Acquire per-source lock so concurrent research-vs-ingest calls
        # for the same source_id don't interleave writes.
        with file_lock(f"ingest-{source_id}"):
            # Respect source-immutability: if the same content_hash is
            # already on disk, leave the file alone.
            if not raw_path.exists():
                write_atomic(raw_path, text)

        rel = f"raw/{source_type}/{source_id}"
        out.append(
            _MaterializedSource(
                item=item,
                raw_path=rel,
                front=front,
                score=score,
            )
        )

    return out


# --- plan construction ------------------------------------------------------


def _make_moc_update(
    domain: str,
    taxonomy: dict,
    materialized: list[_MaterializedSource],
) -> WikiUpdate:
    """Build the MoC create/update for the domain.

    The MoC is `kind=update` if a page already exists; otherwise create.
    On update we *replace* the body wholesale with the freshly-derived
    taxonomy — the previous content was either stale or itself a prior
    research-run snapshot. This is documented in the orchestrator
    docstring; manual hand-edits to `wiki/mocs/<domain>.md` are
    overwritten by the next `wiki research` run for the same domain.
    """
    rel = f"wiki/mocs/{domain}.md"
    target = paths.knowledge_root() / rel
    kind = "update" if target.exists() else "create"

    front = {
        "type": "moc",
        "slug": domain,
        "domain": domain,
        "last_updated": _now_iso(),
    }
    body_lines = [
        f"# {domain} — Map of Content",
        "",
        "## Overview",
        "",
        f"Auto-generated from the corpus-constructive research loop. "
        f"Anchored on the most recent `wiki research` run.",
        "",
        "## Key entities",
        "",
    ]
    # Best-effort: list a handful of materialized sources as anchors.
    sample = materialized[:10]
    if sample:
        for ms in sample:
            slug = ms.raw_path.rsplit("/", 1)[-1]
            body_lines.append(f"- [[sources/{slug}]] — {ms.item.title}")
    else:
        body_lines.append("_(no entity-typed pages yet)_")
    body_lines.extend(["", "## Key concepts", ""])

    branches = taxonomy.get("branches") or []
    if branches:
        for branch in branches:
            name = branch.get("name", "(unnamed)")
            desc = branch.get("description", "")
            body_lines.append(f"- **{name}** — {desc}")
            for sub in branch.get("sub_branches", []) or []:
                sub_name = sub.get("name", "(unnamed)")
                points = ", ".join(sub.get("points") or sub.get("methods") or []) or "(no points listed)"
                body_lines.append(f"  - {sub_name}: {points}")
    else:
        body_lines.append("_(taxonomy empty — analysis returned no branches)_")
    body_lines.extend(["", "## Synthesis pages", ""])
    body_lines.append("_(populated as `wiki research` and `wiki query` runs file syntheses)_")
    body_lines.append("")

    return WikiUpdate(
        target_path=rel,
        update_kind=kind,
        content=fm.serialize(front, "\n".join(body_lines)),
        rationale=f"refreshed MoC from research session taxonomy",
    )


def _collect_constituent_sources(
    findings: dict,
    source_map: dict[str, str],
) -> list[str]:
    """M45: enumerate the `sources/<slug>` constituent set for a synthesis
    page, deduplicated and sorted. Used to fill `synthesizes:` frontmatter
    on first-derivative (per-branch) synthesis pages.

    `findings` may be either a single finding dict (`{answer, citations,
    sources_used}`) or a dict of named findings.
    """
    seen: set[str] = set()
    pool: list[dict]
    if "answer" in findings or "citations" in findings:
        pool = [findings]
    else:
        pool = [v for v in findings.values() if isinstance(v, dict)]
    for finding in pool:
        cites = _coerce_citations(finding.get("citations", {}))
        resolved = _source_map.resolve_citations(cites, source_map)
        for link in resolved.values():
            # link looks like `[[sources/<slug>]]` or `[[nlm:<id>]]`
            if link.startswith("[[sources/") and link.endswith("]]"):
                seen.add(link[2:-2])
    return sorted(seen)


def _make_branch_synthesis_update(
    *,
    domain: str,
    session_id: str,
    branch_name: str,
    branch_findings: dict,
    research_query: str,
    source_map: dict[str, str],
) -> WikiUpdate:
    """Per-branch (first-derivative) synthesis page.

    M45: emits `synthesizes:` listing the source pages this branch drew
    from, plus a `## Included works` section mirroring that list. Enables
    the aggregate-framing exemption at validate-time (M45 § 3.2) so
    NotebookLM's opening framing sentences pass citation grounding.
    """
    branch_slug = _slugify(branch_name) or "branch"
    rel = f"wiki/synthesis/{session_id}-{branch_slug}.md"

    constituents = _collect_constituent_sources(branch_findings, source_map)

    front = {
        "type": "synthesis",
        "slug": f"{session_id}-{branch_slug}",
        "title": f"{branch_name} — investigation ({session_id})",
        "domains": [domain],
        "question": research_query,
        "created_at": _now_iso(),
    }
    if constituents:
        front["synthesizes"] = constituents

    sections = [
        f"# {branch_name} — investigation",
        "",
        f"**Origin question:** {research_query}",
        f"**Session:** {session_id}",
        f"**Branch:** {branch_name}",
        "",
        "## Synthesis",
        "",
    ]
    for label, key in (
        ("Specifics", "specifics"),
        ("Comparisons", "comparisons"),
        ("Gaps", "gaps"),
    ):
        sections.append(f"### {label}")
        sections.append("")
        sections.append(_render_finding_block(branch_findings.get(key, {}), source_map))
        sections.append("")

    sections.append("## Sources cited")
    sections.append("")
    sections.extend(_render_sources_cited(branch_findings, source_map))
    sections.append("")

    if constituents:
        sections.append("## Included works")
        sections.append("")
        for target in constituents:
            sections.append(f"- [[{target}]]")
        sections.append("")

    return WikiUpdate(
        target_path=rel,
        update_kind="create",
        content=fm.serialize(front, "\n".join(sections)),
        rationale=f"per-branch synthesis: {branch_name}",
    )


def _make_cross_cutting_update(
    *,
    domain: str,
    session_id: str,
    research_query: str,
    synthesis: dict[str, dict],
    source_map: dict[str, str],
    branch_names: list[str] | None = None,
) -> WikiUpdate:
    """One synthesis page covering the corpus-wide cross-cutting queries.

    M45: cross-cutting is a second-derivative synthesis — it aggregates
    across the per-branch synthesis pages, not directly across raw
    sources. `synthesizes:` therefore lists `synthesis/<slug>` entries
    (the per-branch pages produced by `_make_branch_synthesis_update`),
    matching one-level strict typing (M45 § 3.6 invariant 1).
    """
    rel = f"wiki/synthesis/{session_id}-cross-cutting.md"

    constituents: list[str] = []
    if branch_names:
        constituents = sorted({
            f"synthesis/{session_id}-{_slugify(name) or 'branch'}"
            for name in branch_names
        })

    front = {
        "type": "synthesis",
        "slug": f"{session_id}-cross-cutting",
        "title": f"Cross-cutting themes ({session_id})",
        "domains": [domain],
        "question": research_query,
        "created_at": _now_iso(),
    }
    if len(constituents) >= 2:
        front["synthesizes"] = constituents

    sections = [
        f"# Cross-cutting themes — {session_id}",
        "",
        f"**Origin question:** {research_query}",
        "",
        "## Synthesis",
        "",
    ]
    for query_name, finding in synthesis.items():
        pretty = query_name.replace("_", " ").title()
        sections.append(f"### {pretty}")
        sections.append("")
        sections.append(_render_finding_block(finding, source_map))
        sections.append("")

    sections.append("## Sources cited")
    sections.append("")
    sections.extend(_render_sources_cited(synthesis, source_map))
    sections.append("")

    if len(constituents) >= 2:
        sections.append("## Included works")
        sections.append("")
        for target in constituents:
            sections.append(f"- [[{target}]]")
        sections.append("")

    return WikiUpdate(
        target_path=rel,
        update_kind="create",
        content=fm.serialize(front, "\n".join(sections)),
        rationale="cross-cutting synthesis",
    )


_NLM_SOURCES_FOOTNOTE_DEF_RE = re.compile(
    r"^\s*\[\^\d+\]:\s*\[\[sources/[^\]\s]+\]\]\s*$",
    re.MULTILINE,
)


def _strip_nlm_emitted_sources_footnotes(answer: str) -> str:
    """Drop `[^N]: [[sources/<anything>]]` footnote-def lines from the answer.

    NotebookLM is prompted to emit `[^N]: [[sources/<id>]]` definitions
    at the end of its response (so unattributed prose looks attributed
    on the NLM side). It doesn't know the gateway-side wiki slugs, so
    it substitutes either the citation number (`[[sources/1]]`) or the
    raw NLM source UUID (`[[sources/nlm-uuid-aaaa]]`) — both of which
    are broken wikilinks against `wiki/sources/<gateway-slug>.md`.

    The orchestrator's own resolve_citations + cite_line append-pass is
    authoritative: it uses the source_map to emit the correct
    `[^N]: [[sources/<gateway-slug>]]` (or `[[nlm:<id>]]` fallback per
    source_map docstring). So we strip the NLM-emitted defs first to
    avoid a parallel broken footnote block on the rendered page.

    Surgical: only strips lines that match the footnote-def shape;
    bullets, headings, and prose containing `[[sources/...]]` inline
    are preserved untouched.
    """
    return _NLM_SOURCES_FOOTNOTE_DEF_RE.sub("", answer)


def _render_finding_block(
    finding: dict | None,
    source_map: dict[str, str],
) -> str:
    """Render one analysis-finding dict (answer + citations) into markdown."""
    if not finding:
        return "_(no answer)_"
    if "error" in finding:
        return f"_Error during analysis: {finding['error']}_"
    answer = (finding.get("answer") or "").strip()
    if not answer:
        return "_(empty answer)_"

    answer = _strip_nlm_emitted_sources_footnotes(answer).strip()

    resolved = _source_map.resolve_citations(
        _coerce_citations(finding.get("citations", {})),
        source_map,
    )
    if resolved:
        cite_line = " ".join(f"[^{n}]: {link}" for n, link in sorted(resolved.items()))
        return f"{answer}\n\n{cite_line}"
    return answer


def _render_sources_cited(
    findings: dict,
    source_map: dict[str, str],
) -> list[str]:
    """Flatten every citation across `findings` into a deduped bullet list."""
    seen: set[str] = set()
    out: list[str] = []
    # `findings` may be either a single finding dict or a dict of named findings.
    pool: list[dict]
    if "answer" in findings or "citations" in findings:
        pool = [findings]
    else:
        pool = [v for v in findings.values() if isinstance(v, dict)]

    for finding in pool:
        cites = _coerce_citations(finding.get("citations", {}))
        resolved = _source_map.resolve_citations(cites, source_map)
        for link in resolved.values():
            if link in seen:
                continue
            seen.add(link)
            out.append(f"- {link}")
    if not out:
        out.append("_(no sources cited)_")
    return out


def _coerce_citations(raw: dict) -> dict[int, str]:
    """Tolerate either int or str-int citation keys from NotebookLM."""
    out: dict[int, str] = {}
    for k, v in (raw or {}).items():
        try:
            num = int(k)
        except (TypeError, ValueError):
            continue
        if isinstance(v, str) and v:
            out[num] = v
    return out


# --- query plan resolution --------------------------------------------------


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def _resolve_query_plan(
    *,
    prompt: str,
    domain: str,
    policy: _policy.Policy,
    adapters: list[SearchAdapter],
    plan_client: PlanClient | None,
    session_id: str,
    resumed_plan: _qp_store.QueryPlan | None,
    is_execute: bool,
) -> tuple[_qp_store.QueryPlan, bool]:
    """Pick a query plan for this run.

    Returns ``(plan, plan_was_generated)``. ``plan_was_generated`` is
    True when the orchestrator just produced the plan (and should
    therefore persist it post-resolution); False when we resumed from
    disk.

    Resolution order:
      1. ``--execute`` (resumed_plan + is_execute=True) — reuse the
         persisted plan; if its mtime exceeds ``generated_at``, stamp
         ``edited: true`` and re-save so future few-shot scans pick
         it up.
      2. ``--queries`` (resumed_plan + is_execute=False) — adopt the
         external YAML's queries, but rewrite ``session_id`` /
         ``prompt`` / ``domain`` / ``generated_at`` so the artifact
         lands as a fresh plan in this session's slot.
      3. ``plan_client`` present — call the planner; fresh plan.
      4. ``plan_client`` is None — M37 backwards-compat: synthesize a
         single-query-per-adapter plan with the verbatim prompt. Not
         persisted (preserves M37 behavior of not creating
         ``nlm/query_plans/`` for offline runs).
    """
    if resumed_plan and is_execute:
        # --execute path. Mark edited if the YAML was touched after generation.
        target = _qp_store.path_for(session_id)
        edited = resumed_plan.edited
        if not edited and target.is_file():
            mtime = datetime.fromtimestamp(
                target.stat().st_mtime, tz=timezone.utc
            )
            if (mtime - resumed_plan.generated_at).total_seconds() > 2.0:
                edited = True
        if edited and not resumed_plan.edited:
            resumed_plan.edited = True
            try:
                _qp_store.save(resumed_plan)
            except OSError:
                # Stamping is best-effort; the run continues.
                pass
        return resumed_plan, False

    if resumed_plan and not is_execute:
        # --queries path. Adopt queries; rebrand as this session's plan.
        new_plan = _qp_store.QueryPlan(
            session_id=session_id,
            domain=domain,
            prompt=prompt,
            generated_at=_now_utc(),
            queries=dict(resumed_plan.queries),
            target_counts=dict(resumed_plan.target_counts),
            plan_client_model=resumed_plan.plan_client_model,
            edited=False,
        )
        return new_plan, True

    non_local = [a.name for a in adapters if a.name != "local"]

    if plan_client is not None and non_local:
        history = _qp_store.recent_edited(domain, n=5)
        try:
            result = _query_planner.plan_per_adapter_queries(
                prompt,
                domain=domain,
                policy=policy,
                adapter_names=non_local,
                plan_client=plan_client,
                history_examples=history,
            )
        except _query_planner.PlannerError as e:
            log.append(
                "research",
                fields={"session_id": session_id, "step": "plan", "n": 0},
                summary=f"planner failed; falling back to verbatim: {e}",
            )
            queries = {name: [prompt] for name in non_local}
            target_counts: dict[str, int] = {}
        else:
            queries = result.queries
            target_counts = result.target_counts
        plan = _qp_store.QueryPlan(
            session_id=session_id,
            domain=domain,
            prompt=prompt,
            generated_at=_now_utc(),
            queries=queries,
            target_counts=target_counts,
        )
        return plan, True

    # No plan_client and no resumed plan — verbatim fallback. Build an
    # in-memory plan but do not persist it (M37 parity for offline runs).
    fallback = _qp_store.QueryPlan(
        session_id=session_id,
        domain=domain,
        prompt=prompt,
        generated_at=_now_utc(),
        queries={name: [prompt] for name in non_local},
        target_counts={},
    )
    return fallback, False


def _load_external_plan(path: str) -> _qp_store.QueryPlan:
    """Read a hand-authored query plan YAML from an arbitrary path.

    Reuses the same parser as `query_plan_store.load` but bypasses the
    `nlm/query_plans/<session-id>.yaml` path convention so users can
    keep curated plans wherever they want.
    """
    import yaml as _yaml

    target = Path(path).expanduser()
    if not target.is_file():
        raise _qp_store.QueryPlanError(f"no query plan at {target}")
    try:
        raw = _yaml.safe_load(target.read_text(encoding="utf-8"))
    except _yaml.YAMLError as e:
        raise _qp_store.QueryPlanError(
            f"malformed query plan {target}: {e}"
        ) from e
    if not isinstance(raw, dict):
        raise _qp_store.QueryPlanError(
            f"query plan {target} is not a mapping"
        )
    return _qp_store._parse(raw, source=target)  # noqa: SLF001 — internal reuse


# --- public entry point -----------------------------------------------------


def research(
    prompt: str | None,
    *,
    domain: str | None = None,
    include_local: list[str] | None = None,
    trust_local: bool = False,
    max_results_per_adapter: int = 50,
    nlm_client: "NlmClient | None" = None,
    plan_client: PlanClient | None = None,
    filter_client: FilterClient | None = None,
    draft: bool = False,
    dry_run: bool = False,
    review: bool = False,
    execute_session: str | None = None,
    external_plan_path: str | None = None,
) -> OperationResult:
    """Run the full corpus-constructive research loop. See module docstring."""
    # Resume modes: --execute loads a persisted plan; --queries loads an
    # external YAML. In both cases the prompt and (for --execute) domain
    # come from the plan file, not the call args.
    resumed_plan: _qp_store.QueryPlan | None = None
    if execute_session and external_plan_path:
        return OperationResult(
            success=False,
            errors=["--execute and --queries are mutually exclusive"],
        )
    if execute_session:
        try:
            resumed_plan = _qp_store.load(execute_session)
        except _qp_store.QueryPlanError as e:
            return OperationResult(
                success=False,
                errors=[f"could not load query plan for --execute: {e}"],
            )
        prompt = resumed_plan.prompt
        domain = resumed_plan.domain
    elif external_plan_path:
        try:
            resumed_plan = _load_external_plan(external_plan_path)
        except _qp_store.QueryPlanError as e:
            return OperationResult(
                success=False,
                errors=[f"could not load --queries file: {e}"],
            )
        # external plans contribute queries; prompt/domain still come
        # from call args (validated below).

    if not prompt or not prompt.strip():
        return OperationResult(
            success=False,
            errors=["research prompt must be non-empty"],
        )

    # Step 1 — domain.
    effective_domain = domain or _infer_domain(prompt, plan_client)
    if not effective_domain:
        return OperationResult(
            success=False,
            errors=[
                "could not infer a domain for this prompt; pass --domain or "
                "run `wiki discover-domains` to register one"
            ],
        )
    if not _policy.policy_exists(effective_domain):
        return OperationResult(
            success=False,
            errors=[
                f"no policy for domain {effective_domain!r}; "
                "run `wiki discover-domains` to register it"
            ],
        )

    # Step 2 — load policy.
    try:
        policy = _policy.load_policy(effective_domain)
    except _policy.PolicyError as e:
        return OperationResult(
            success=False,
            errors=[f"policy load failed for {effective_domain!r}: {e}"],
        )

    # Step 3 — session id. On --execute we reuse the plan's session id so
    # all log lines remain grep-able by the same key.
    session_id = (
        execute_session
        if execute_session
        else _session.make_session_id(prompt)
    )
    log.append(
        "research",
        fields={"session_id": session_id, "step": "start", "domain": effective_domain},
        summary=f"start research session for prompt {prompt!r}",
    )

    # Step 3.5 — query plan: generate (default), load (--execute), import
    # (--queries), or fall back to verbatim (no plan_client).
    adapters = enabled_adapters(include_local=include_local)
    plan, plan_was_generated = _resolve_query_plan(
        prompt=prompt,
        domain=effective_domain,
        policy=policy,
        adapters=adapters,
        plan_client=plan_client,
        session_id=session_id,
        resumed_plan=resumed_plan,
        is_execute=bool(execute_session),
    )
    if plan_was_generated:
        try:
            _qp_store.save(plan)
            log.append(
                "research",
                fields={
                    "session_id": session_id,
                    "step": "plan",
                    "n": sum(len(v) for v in plan.queries.values()),
                },
                summary=f"query plan written to nlm/query_plans/{session_id}.yaml",
            )
        except OSError as e:
            return OperationResult(
                success=False,
                errors=[f"persist query plan: {e}"],
            )

    if review:
        path = _qp_store.path_for(session_id)
        return OperationResult(
            success=True,
            paths_touched=[path],
            summary=(
                f"review-gate: query plan written to {path.relative_to(paths.knowledge_root())}; "
                f"edit and resume with `wiki research --execute {session_id}`"
            ),
        )

    # Step 4 — fan out search using the resolved plan.
    candidates = _fan_out_search(
        adapters,
        plan.queries,
        max_results_per_adapter=max_results_per_adapter,
        session_id=session_id,
    )
    log.append(
        "research",
        fields={"session_id": session_id, "step": "merge", "n": len(candidates)},
        summary=f"merged {len(candidates)} candidate(s) across adapters",
    )

    if not candidates:
        return OperationResult(
            success=True,
            no_op=True,
            summary="no candidates returned by any adapter",
        )

    # Step 5/6 — filter.
    accepted = _run_filter(
        candidates,
        domain=effective_domain,
        policy=policy,
        trust_local=trust_local,
        filter_client=filter_client,
        session_id=session_id,
    )
    log.append(
        "research",
        fields={"session_id": session_id, "step": "filter", "n": len(accepted)},
        summary=f"{len(accepted)} candidate(s) cleared threshold",
    )
    if not accepted:
        return OperationResult(
            success=True,
            no_op=True,
            summary="no candidates met threshold",
        )

    # Step 7 — materialize.
    materialized = _materialize(accepted, session_id=session_id)
    log.append(
        "research",
        fields={
            "session_id": session_id,
            "step": "materialize",
            "n": len(materialized),
        },
        summary=f"materialized {len(materialized)} source(s) to raw/",
    )
    if not materialized:
        return OperationResult(
            success=True,
            no_op=True,
            summary="no candidates survived materialization",
        )

    if dry_run:
        return _dry_run_result(session_id, effective_domain, prompt, materialized)

    # Step 8 — persistent notebook.
    if nlm_client is None:
        from gateway.nlm_client import NlmCLIClient

        nlm_client = NlmCLIClient()

    persistent_id = nlm_registry.get_persistent(effective_domain)
    if not persistent_id:
        try:
            persistent_id = nlm_client.notebook_create(
                f"{effective_domain} (knowledge base)"
            )
        except Exception as e:  # noqa: BLE001
            return OperationResult(
                success=False,
                errors=[f"create persistent notebook: {e}"],
            )
        nlm_registry.register(effective_domain, persistent_id)
    log.append(
        "research",
        fields={
            "session_id": session_id,
            "step": "nlm_persistent",
            "notebook_id": persistent_id,
        },
        summary=f"persistent notebook {persistent_id}",
    )

    # Step 9 — session notebook.
    try:
        session_nb_id = nlm_client.notebook_create(
            f"{effective_domain} - session {session_id}"
        )
    except Exception as e:  # noqa: BLE001
        return OperationResult(
            success=False,
            errors=[f"create session notebook: {e}"],
        )
    nlm_registry.register_session(
        effective_domain, session_id, session_nb_id, query=prompt
    )
    log.append(
        "research",
        fields={
            "session_id": session_id,
            "step": "nlm_session",
            "notebook_id": session_nb_id,
        },
        summary=f"created session notebook {session_nb_id}",
    )

    # Through apply_plan, any failure marks the session abandoned. After
    # apply_plan succeeds, the wiki pages are on disk and the post-apply
    # promote step (step 16) is best-effort — its failures become warnings,
    # not abandons.
    try:
        # Step 10 — push sources to session notebook.
        # Per-source failures (e.g. private/removed YouTube videos, dead
        # URLs, NotebookLM rate-limit hiccups) are logged and skipped —
        # one bad source must not sink the whole research run.
        pushed_n = 0
        skipped_n = 0
        for ms in materialized:
            url = ms.front.get("url") or ""
            try:
                if isinstance(url, str) and url:
                    nlm_client.source_add_url(session_nb_id, url)
                else:
                    target = paths.knowledge_root() / f"{ms.raw_path}.md"
                    content = target.read_text() if target.exists() else ""
                    title = ms.front.get("title") or ms.raw_path
                    nlm_client.source_add_text(
                        session_nb_id, content, title=title
                    )
            except Exception as e:  # noqa: BLE001 — per-source isolation
                _emit_step_error(
                    session_id, "source_add", url or ms.raw_path, str(e)
                )
                skipped_n += 1
                continue
            nlm_registry.increment_session_sources(
                effective_domain, session_id, n=1
            )
            pushed_n += 1

        if pushed_n == 0:
            raise RuntimeError(
                f"step 10: no sources successfully pushed "
                f"({skipped_n} failed, 0 succeeded)"
            )
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "source_add",
                "n": pushed_n,
                "skipped": skipped_n,
            },
            summary=(
                f"pushed {pushed_n} source(s) to session notebook "
                f"({skipped_n} skipped)"
            ),
        )

        # Step 11 — source map.
        smap = _source_map.build_source_map(session_nb_id, client=nlm_client)
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "source_map",
                "n": len(smap or {}),
            },
            summary=f"built source map ({len(smap or {})} entries)",
        )

        # Step 12 — analysis.
        if _analysis is None:
            raise RuntimeError(
                "gateway.research.analysis is not importable; "
                "ensure the parallel agent's port has landed"
            )
        analysis_result = _analysis.analyze(
            session_nb_id,
            domain=effective_domain,
            research_query=prompt,
            client=nlm_client,
        )
        branch_count = len(analysis_result.findings or {})
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "analysis",
                "branches": branch_count,
            },
            summary=f"analysis complete ({branch_count} branch(es))",
        )

        # Step 13/14 — build the plan with citations resolved.
        plan = _build_plan(
            domain=effective_domain,
            session_id=session_id,
            prompt=prompt,
            materialized=materialized,
            analysis=analysis_result,
            source_map=smap,
        )

        # Step 15 — apply.
        plan_result = apply_plan(plan, draft=draft)
        if not plan_result.success:
            raise RuntimeError(
                "apply_plan rejected the synthesis: "
                + "; ".join(plan_result.errors)
            )
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "apply_plan",
                "pages": len(plan_result.paths_touched),
            },
            summary=f"applied plan: {plan_result.summary}",
        )
    except Exception as e:  # noqa: BLE001
        try:
            _session.abandon(
                effective_domain, session_id, nlm_registry=nlm_registry
            )
        except Exception:  # noqa: BLE001 — best-effort
            pass
        log.append(
            "research",
            fields={"session_id": session_id, "step": "abandon"},
            summary=f"abandoned session: {e}",
        )
        return OperationResult(
            success=False,
            errors=[f"research session {session_id} aborted: {e}"],
        )

    # Step 16 — promote (post-apply_plan).
    #
    # apply_plan has succeeded; wiki pages are on disk and the session is
    # semantically complete. Promotion (copying session sources into the
    # persistent domain corpus) is a best-effort enrichment — failures here
    # (stale URLs, NotebookLM rate limits, transient network errors) must
    # NOT trigger session abandon, because that would leave the wiki pages
    # orphaned in disk-vs-registry disagreement.
    promote_warnings: list[str] = []
    promoted_n = 0
    promoted_failed: list[tuple[str, str]] = []
    try:
        promoted_n, promoted_failed = _session.promote(
            effective_domain,
            session_id,
            persistent_notebook_id=persistent_id,
            session_notebook_id=session_nb_id,
            client=nlm_client,
            nlm_registry=nlm_registry,
        )
    except Exception as e:  # noqa: BLE001 — promote failures are non-fatal
        promote_warnings.append(f"promote: {e}")
        log.append(
            "research",
            fields={"session_id": session_id, "step": "promote_failed"},
            summary=f"promote failed but wiki was authored: {e}",
        )
    else:
        for target, err in promoted_failed:
            promote_warnings.append(f"promote source {target}: {err}")
        log.append(
            "research",
            fields={
                "session_id": session_id,
                "step": "promoted",
                "added": promoted_n,
                "failed": len(promoted_failed),
            },
            summary=(
                f"promoted {promoted_n} source(s) into persistent notebook"
                + (
                    f" ({len(promoted_failed)} failed)"
                    if promoted_failed
                    else ""
                )
            ),
        )

    summary_lines = [
        f"research session {session_id} ({effective_domain})",
        f"  candidates: {len(candidates)} → accepted: {len(accepted)} → materialized: {len(materialized)}",
        f"  branches: {len(analysis_result.findings)}",
        f"  promoted to persistent: {promoted_n}",
    ]
    return OperationResult(
        success=True,
        paths_touched=plan_result.paths_touched,
        summary="\n".join(summary_lines),
        warnings=list(plan_result.warnings)
        + list(analysis_result.errors)
        + promote_warnings,
    )


# --- dry-run path -----------------------------------------------------------


def _dry_run_result(
    session_id: str,
    domain: str,
    prompt: str,
    materialized: list[_MaterializedSource],
) -> OperationResult:
    """Return a structured summary of what `research` would have done."""
    planned_pages = [
        paths.knowledge_root() / f"wiki/mocs/{domain}.md",
        paths.knowledge_root() / f"wiki/synthesis/{session_id}-cross-cutting.md",
    ]
    summary_lines = [
        f"[dry-run] research session {session_id} ({domain})",
        f"  prompt: {prompt}",
        f"  materialized sources: {len(materialized)}",
        "  planned pages:",
        *[f"    - {p.relative_to(paths.knowledge_root())}" for p in planned_pages],
    ]
    return OperationResult(
        success=True,
        paths_touched=planned_pages,
        summary="\n".join(summary_lines),
    )


# --- plan composition -------------------------------------------------------


def _build_plan(
    *,
    domain: str,
    session_id: str,
    prompt: str,
    materialized: list[_MaterializedSource],
    analysis,
    source_map: dict[str, str],
) -> Plan:
    """Compose the multi-page Plan from the analysis result."""
    updates: list[WikiUpdate] = [
        _make_moc_update(domain, analysis.taxonomy or {}, materialized),
    ]
    for branch_name, branch_findings in (analysis.findings or {}).items():
        updates.append(
            _make_branch_synthesis_update(
                domain=domain,
                session_id=session_id,
                branch_name=branch_name,
                branch_findings=branch_findings,
                research_query=prompt,
                source_map=source_map,
            )
        )
    updates.append(
        _make_cross_cutting_update(
            domain=domain,
            session_id=session_id,
            research_query=prompt,
            synthesis=analysis.synthesis or {},
            source_map=source_map,
            branch_names=list((analysis.findings or {}).keys()),
        )
    )
    return Plan(
        source_id=f"research-{session_id}",
        rationale=f"corpus-constructive research session for {domain}",
        updates=updates,
    )


# --- helpers ----------------------------------------------------------------


def _slugify(text: str, *, max_words: int = 6) -> str:
    import re

    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    words = [w for w in cleaned.split("-") if w]
    return "-".join(words[:max_words])


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _emit_step_error(session_id: str, step: str, target: str, msg: str) -> None:
    """Log an error to log.md and stderr; do not raise."""
    print(
        f"[research:{session_id}] {step} failed for {target}: {msg}",
        file=sys.stderr,
    )
    log.append(
        "research",
        fields={"session_id": session_id, "step": step, "target": target},
        summary=f"error: {msg}",
    )
