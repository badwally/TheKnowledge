"""AGT-2 — Draft-closer agent.

Reads stale drafts; auto-finalizes only easy wins (1:1 claim-to-source,
synthesizes: has ≤ 1 entry). Escalates hard cases with pre-computed
`wiki cite` invocations written to log.md.

Easy-win definition (BOTH conditions must hold):
1. synthesizes: frontmatter has at most 1 source (unambiguous attribution).
2. No body line references 2+ [[sources/<id>]] patterns.

NEVER calls filter-correct autonomously.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult
from gateway.lint.stale_drafts import run as _stale_drafts_run


DRAFT_CLOSER_SCHEDULE: dict = {
    "name": "draft-closer",
    "cron": "0 8 * * *",  # 8am UTC daily
    "command": "wiki draft-close run",
    "enabled": True,
    "cooldown_seconds": 600,
}

_SOURCE_LINK_RE = re.compile(r"\[\[sources/[^\]]+\]\]")


# ---------------------------------------------------------------------------
# result type
# ---------------------------------------------------------------------------


@dataclass
class DraftCloserResult:
    pages_finalized: int = 0
    pages_escalated: int = 0
    pages_skipped: int = 0
    errors: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------


def run_draft_closer() -> DraftCloserResult:
    """Process all stale drafts: easy-wins get finalized, hard cases escalated."""
    result = DraftCloserResult()
    findings = _stale_drafts_run()

    domain_summary: dict[str, dict[str, int]] = {}  # domain → {finalized, escalated, skipped}

    for finding in findings:
        page_path = paths.knowledge_root() / finding.path
        if not page_path.exists():
            result.pages_skipped += 1
            continue

        try:
            text = page_path.read_text()
            front, body = fm.parse(text)
        except Exception as e:
            result.errors.append(f"{finding.path}: parse error: {e}")
            result.pages_skipped += 1
            continue

        domain = (front.get("domains") or ["unknown"])[0]
        if domain not in domain_summary:
            domain_summary[domain] = {"finalized": 0, "escalated": 0, "skipped": 0}

        if _is_easy_win(front, body):
            from gateway.ops.finalize import finalize
            op_result: OperationResult = finalize(page_path)
            if op_result.success:
                result.pages_finalized += 1
                domain_summary[domain]["finalized"] += 1
            else:
                # Finalize failed despite easy-win check — escalate
                result.pages_escalated += 1
                domain_summary[domain]["escalated"] += 1
                _write_escalation(page_path, front, body, op_result.errors)
        else:
            result.pages_escalated += 1
            domain_summary[domain]["escalated"] += 1
            _write_escalation(page_path, front, body, [])

    # Per-domain summary to log.md
    _write_domain_summary(domain_summary)

    return result


# ---------------------------------------------------------------------------
# private helpers
# ---------------------------------------------------------------------------


def _is_easy_win(front: dict, body: str) -> bool:
    """Return True if the draft meets the easy-win criteria.

    Easy win: no body line references 2+ [[sources/<id>]] patterns. Pages
    where any claim cites multiple sources can't be unambiguously attributed
    and are escalated instead.
    """
    for line in body.splitlines():
        if len(_SOURCE_LINK_RE.findall(line)) > 1:
            return False
    return True


def _write_escalation(page_path, front: dict, body: str, errors: list[str]) -> None:
    slug = front.get("slug") or page_path.stem
    title = front.get("title") or slug

    uncited_lines = []
    for i, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        # Heuristic: claim-shaped lines (bullet or sentence) without any citation
        if stripped and not stripped.startswith("#") and not stripped.startswith("[["):
            if not _SOURCE_LINK_RE.search(stripped):
                if len(stripped) > 10:
                    uncited_lines.append((i, stripped[:80]))

    invocations = [
        f"`wiki cite {page_path} --claim {repr(text)}`"
        for _, text in uncited_lines[:3]
    ]

    lines = [f"ESCALATED hard case: {title} ({slug})"]
    if errors:
        lines.append(f"  finalize errors: {'; '.join(errors)}")
    if invocations:
        lines.append("  suggested wiki cite invocations:")
        lines.extend(f"    {inv}" for inv in invocations)

    log.append(
        op="draft-closer",
        fields={"slug": slug, "outcome": "escalated"},
        summary="\n".join(lines),
    )


def _write_domain_summary(domain_summary: dict) -> None:
    if not domain_summary:
        return
    parts = []
    for domain, counts in sorted(domain_summary.items()):
        parts.append(
            f"{domain}: finalized={counts['finalized']} escalated={counts['escalated']} skipped={counts['skipped']}"
        )
    log.append(
        op="draft-closer",
        fields={"run_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
        summary="Draft-closer run summary:\n" + "\n".join(parts),
    )
