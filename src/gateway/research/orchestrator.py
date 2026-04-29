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
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from gateway import converters, frontmatter as fm
from gateway import log, nlm_registry, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter import policy as _policy
from gateway.filter.semantic import FilterClient, FilterError, score as filter_score
from gateway.filter import load_all as _load_examples, select as _select_examples
from gateway.ops.apply_plan import apply_plan
from gateway.plan import Plan, PlanClient, WikiUpdate
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
    try:
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
    prompt: str,
    *,
    max_results_per_adapter: int,
    session_id: str,
) -> list[CandidateItem]:
    """Run every adapter in a thread pool; merge results, dedup by URL.

    A single adapter raising `AdapterError` (or any other exception) is
    logged to stderr + log.md and dropped — the rest of the run
    continues. This matches the SearchAdapter docstring contract.
    """
    if not adapters:
        return []

    candidates: list[CandidateItem] = []
    with _futures.ThreadPoolExecutor(max_workers=max(1, len(adapters))) as pool:
        future_to_adapter = {
            pool.submit(
                _safe_search,
                adapter,
                prompt,
                max_results_per_adapter,
            ): adapter
            for adapter in adapters
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
    prompt: str,
    max_results: int,
) -> list[CandidateItem]:
    """Wrap one adapter call. Reraises so the executor surfaces it."""
    return list(adapter.search(prompt, max_results=max_results))


# --- filter -----------------------------------------------------------------


def _run_filter(
    candidates: list[CandidateItem],
    *,
    domain: str,
    policy: _policy.Policy,
    trust_local: bool,
    filter_client: FilterClient | None,
    session_id: str,
) -> list[tuple[CandidateItem, float]]:
    """Score every candidate; keep only those clearing `threshold_include`.

    `trust_local=True` waves through items with `source_type == "local"`
    or `file://` URLs without a model call. Useful for pre-vetted local
    archives the user is folding into a search.
    """
    examples = _select_examples(_load_examples(domain), policy)
    accepted: list[tuple[CandidateItem, float]] = []

    for item in candidates:
        if trust_local and _is_local(item):
            accepted.append((item, 1.0))
            continue

        front = _candidate_front(item, domain)
        body_head = item.description or item.title
        try:
            result = filter_score(
                front, body_head, policy, examples, client=filter_client
            )
        except FilterError as e:
            _emit_step_error(session_id, "filter", item.url, str(e))
            continue

        if result.score >= policy.threshold_include:
            accepted.append((item, result.score))
    return accepted


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
                methods = ", ".join(sub.get("methods", []) or []) or "(no methods listed)"
                body_lines.append(f"  - {sub_name}: {methods}")
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


def _make_branch_synthesis_update(
    *,
    domain: str,
    session_id: str,
    branch_name: str,
    branch_findings: dict,
    research_query: str,
    source_map: dict[str, str],
) -> WikiUpdate:
    """Per-branch synthesis page — Methods / Comparisons / Open Problems."""
    branch_slug = _slugify(branch_name) or "branch"
    rel = f"wiki/synthesis/{session_id}-{branch_slug}.md"

    front = {
        "type": "synthesis",
        "slug": f"{session_id}-{branch_slug}",
        "title": f"{branch_name} — investigation ({session_id})",
        "domains": [domain],
        "question": research_query,
        "created_at": _now_iso(),
    }

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
        ("Methods", "methods"),
        ("Comparisons", "comparisons"),
        ("Open Problems", "open_problems"),
    ):
        sections.append(f"### {label}")
        sections.append("")
        sections.append(_render_finding_block(branch_findings.get(key, {}), source_map))
        sections.append("")

    sections.append("## Sources cited")
    sections.append("")
    sections.extend(_render_sources_cited(branch_findings, source_map))
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
) -> WikiUpdate:
    """One synthesis page covering the corpus-wide cross-cutting queries."""
    rel = f"wiki/synthesis/{session_id}-cross-cutting.md"
    front = {
        "type": "synthesis",
        "slug": f"{session_id}-cross-cutting",
        "title": f"Cross-cutting themes ({session_id})",
        "domains": [domain],
        "question": research_query,
        "created_at": _now_iso(),
    }

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

    return WikiUpdate(
        target_path=rel,
        update_kind="create",
        content=fm.serialize(front, "\n".join(sections)),
        rationale="cross-cutting synthesis",
    )


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


# --- public entry point -----------------------------------------------------


def research(
    prompt: str,
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
) -> OperationResult:
    """Run the full corpus-constructive research loop. See module docstring."""
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

    # Step 3 — session id.
    session_id = _session.make_session_id(prompt)
    log.append(
        "research",
        fields={"session_id": session_id, "step": "start", "domain": effective_domain},
        summary=f"start research session for prompt {prompt!r}",
    )

    # Step 4 — fan out search.
    adapters = enabled_adapters(include_local=include_local)
    candidates = _fan_out_search(
        adapters,
        prompt,
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

    # From here on out, any failure must mark the session abandoned.
    try:
        # Step 10 — push sources to session notebook.
        for ms in materialized:
            url = ms.front.get("url") or ""
            if isinstance(url, str) and url:
                nlm_client.source_add_url(session_nb_id, url)
            else:
                # Source has no URL; push the canonical text body.
                target = paths.knowledge_root() / f"{ms.raw_path}.md"
                content = target.read_text() if target.exists() else ""
                title = ms.front.get("title") or ms.raw_path
                nlm_client.source_add_text(session_nb_id, content, title=title)
            nlm_registry.increment_session_sources(
                effective_domain, session_id, n=1
            )

        # Step 11 — source map.
        smap = _source_map.build_source_map(session_nb_id, client=nlm_client)

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

        # Step 16 — promote.
        try:
            promoted_n = _session.promote(
                effective_domain,
                session_id,
                persistent_notebook_id=persistent_id,
                session_notebook_id=session_nb_id,
                client=nlm_client,
                nlm_registry=nlm_registry,
            )
        except Exception as e:  # noqa: BLE001
            raise RuntimeError(f"promote: {e}") from e
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

    log.append(
        "research",
        fields={
            "session_id": session_id,
            "step": "promoted",
            "added": promoted_n,
        },
        summary=f"promoted {promoted_n} source(s) into persistent notebook",
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
        warnings=list(plan_result.warnings) + list(analysis_result.errors),
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
