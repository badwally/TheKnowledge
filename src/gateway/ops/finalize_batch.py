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

from gateway import frontmatter as fm
from gateway import paths
from gateway.core import OperationResult
from gateway.lint import stale_drafts as stale_drafts_check
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

        # Phase C/D: suggest path lives here. Stub for now: escalate.
        outcomes.append(_Outcome(
            page=rel, category="escalated", finalized=False,
            note=f"unresolved_claims={unresolved!r} (suggest not yet wired)",
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

    return OperationResult(
        success=True,
        summary="\n".join(summary_lines),
        warnings=warnings,
    )
