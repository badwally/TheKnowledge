"""`wiki finalize-batch` -- daily batch closer for stale drafts (M49, AGT-2).

Reads `lint --scope stale-drafts`. For each finding:
  Cat A: `unresolved_claims == 0` -> finalize (when `--execute`).
  Cat B: validator re-run shows 0 unresolved claims -> finalize.
  Other: skip in deterministic mode; in `--suggest` mode (Phase C/D),
         call cite-suggest; in `--suggest --execute` (Aggressive),
         auto-apply unambiguous + verified suggestions and finalize.

Defaults to dry-run. Pass `execute=True` to actually finalize / apply cites.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from gateway import frontmatter as fm
from gateway import log
from gateway import paths
from gateway.core import OperationResult
from gateway.lint import stale_drafts as stale_drafts_check
from gateway.ops.cite import cite as cite_one
from gateway.ops.cite_suggest import suggest_cites
from gateway.ops.finalize import finalize as finalize_one


@dataclass
class _Outcome:
    page: str
    category: str  # "cat_a" | "cat_b" | "suggest_applied" | "escalated"
    finalized: bool
    note: str = ""
    suggested_cites: list[str] = field(default_factory=list)


def finalize_batch(
    *,
    domain: str | None = None,
    limit: int | None = None,
    execute: bool = False,
    suggest: bool = False,
) -> OperationResult:
    findings = stale_drafts_check.run()
    outcomes: list[_Outcome] = []

    for finding in findings:
        if limit is not None and len(outcomes) >= limit:
            break

        rel = finding.path

        if domain is not None:
            page_abs = paths.knowledge_root() / rel
            try:
                front, _ = fm.parse(page_abs.read_text())
            except Exception:
                continue
            if domain not in (front.get("domains") or []):
                continue

        meta = finding.metadata or {}
        unresolved = meta.get("unresolved_claims")

        # Cat A: deterministic finalize candidate.
        if unresolved == 0:
            if execute:
                page_abs = paths.knowledge_root() / rel
                sub = finalize_one(page_abs)
                if sub.success:
                    outcomes.append(_Outcome(page=rel, category="cat_a", finalized=True))
                else:
                    outcomes.append(_Outcome(
                        page=rel, category="escalated", finalized=False,
                        note="finalize failed: " + "; ".join(sub.errors or []),
                    ))
            else:
                outcomes.append(_Outcome(page=rel, category="cat_a", finalized=False,
                                         note="dry-run"))
            continue

        # Cat B / suggest path
        page_abs = paths.knowledge_root() / rel

        if not suggest:
            outcomes.append(_Outcome(
                page=rel, category="escalated", finalized=False,
                note=f"unresolved_claims={unresolved!r} (no --suggest)",
            ))
            continue

        # --suggest active
        try:
            suggestions = suggest_cites(page_abs)
        except Exception as e:
            outcomes.append(_Outcome(
                page=rel, category="escalated", finalized=False,
                note=f"cite-suggest failed: {e}",
            ))
            continue

        appliable = [s for s in suggestions if s.auto_appliable]
        escalations = [s for s in suggestions if not s.auto_appliable]
        escalation_strs = [
            f"# line={s.line} source={s.source_id} reason={s.skip_reason!r}"
            for s in escalations
        ]

        if not appliable:
            outcomes.append(_Outcome(
                page=rel, category="escalated", finalized=False,
                note="no auto-appliable suggestions",
                suggested_cites=escalation_strs,
            ))
            continue

        if not execute:
            invocation_strs = [
                f"wiki cite {rel} {s.line}:{s.source_id}"
                for s in appliable
            ]
            outcomes.append(_Outcome(
                page=rel, category="suggest_applied", finalized=False,
                note=f"{len(appliable)} appliable, {len(escalations)} escalated",
                suggested_cites=invocation_strs + escalation_strs,
            ))
            continue

        # Aggressive: apply each appliable suggestion, then finalize.
        additions = [(s.line, s.source_id) for s in appliable]
        cite_result = cite_one(page_abs, additions)
        if not cite_result.success:
            outcomes.append(_Outcome(
                page=rel, category="escalated", finalized=False,
                note=f"cite failed: {'; '.join(cite_result.errors or [])}",
                suggested_cites=escalation_strs,
            ))
            continue

        finalize_result = finalize_one(page_abs)
        if finalize_result.success:
            outcomes.append(_Outcome(
                page=rel, category="suggest_applied", finalized=True,
                note=f"applied {len(appliable)} cite(s); {len(escalations)} escalated",
                suggested_cites=escalation_strs,
            ))
        else:
            outcomes.append(_Outcome(
                page=rel, category="escalated", finalized=False,
                note=f"cite applied ({len(appliable)}), finalize failed — page is half-mutated, recover via git: {'; '.join(finalize_result.errors or [])}",
                suggested_cites=escalation_strs,
            ))

    n_finalized = sum(1 for o in outcomes if o.finalized)
    n_total = len(outcomes)
    summary_lines = [
        f"finalize-batch: {n_total} candidate(s), {n_finalized} finalized "
        f"(execute={execute}, suggest={suggest})",
    ]
    for o in outcomes:
        mark = "FINALIZED" if o.finalized else o.category
        summary_lines.append(f"  [{mark}] {o.page}{(' -- ' + o.note) if o.note else ''}")
    warnings = [
        f"escalated: {o.page} -- {o.note}"
        for o in outcomes if o.category == "escalated"
    ]

    report_path = _write_run_report(outcomes, dry_run=not execute)
    log.append(
        op="finalize-batch",
        fields={
            "candidates": len(outcomes),
            "finalized": sum(1 for o in outcomes if o.finalized),
            "escalated": sum(1 for o in outcomes if o.category == "escalated"),
            "execute": execute,
            "suggest": suggest,
        },
        summary=(
            f"finalize-batch: {len(outcomes)} candidates, "
            f"{sum(1 for o in outcomes if o.finalized)} finalized "
            f"(execute={execute}, suggest={suggest})"
        ),
    )

    return OperationResult(
        success=True,
        paths_touched=[report_path, paths.log_path()],
        summary="\n".join(summary_lines),
        warnings=warnings,
    )


def _write_run_report(outcomes: list[_Outcome], *, dry_run: bool) -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    report_dir = paths.knowledge_internal() / "finalize-batch"
    report_dir.mkdir(parents=True, exist_ok=True)
    report = report_dir / f"{ts}.md"

    cat_a = [o for o in outcomes if o.category == "cat_a"]
    suggest_applied = [o for o in outcomes if o.category == "suggest_applied"]
    escalated = [o for o in outcomes if o.category == "escalated"]

    lines = [
        f"# finalize-batch run — {ts}",
        "",
        f"Mode: {'dry-run' if dry_run else 'execute'}",
        "",
        "## Summary",
        f"- cat_a (deterministic): {len(cat_a)} ({sum(1 for o in cat_a if o.finalized)} finalized)",
        f"- suggest_applied (LLM): {len(suggest_applied)} ({sum(1 for o in suggest_applied if o.finalized)} finalized)",
        f"- escalated: {len(escalated)}",
        "",
    ]
    if cat_a:
        lines += ["## Cat A (deterministic)", ""]
        for o in cat_a:
            mark = "FINALIZED" if o.finalized else "candidate"
            lines.append(f"- {mark}: `{o.page}` — {o.note}" if o.note else f"- {mark}: `{o.page}`")
        lines.append("")
    if suggest_applied:
        lines += ["## Suggest-applied (LLM)", ""]
        for o in suggest_applied:
            mark = "FINALIZED" if o.finalized else "candidate"
            lines.append(f"- {mark}: `{o.page}` — {o.note}" if o.note else f"- {mark}: `{o.page}`")
            for sc in o.suggested_cites:
                lines.append(f"  - {sc}")
        lines.append("")
    if escalated:
        lines += ["## Escalated", ""]
        for o in escalated:
            lines.append(f"- `{o.page}` — {o.note}")
            for sc in o.suggested_cites:
                lines.append(f"  - {sc}")
        lines.append("")

    report.write_text("\n".join(lines))
    return report
