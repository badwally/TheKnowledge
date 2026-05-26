"""TOOL-14: contradiction drift — nightly JSON snapshot + diff.

Runs wiki lint --scope contradictions, serializes findings to stable JSON,
diffs against yesterday's snapshot, and writes the diff as a new snapshot.

Output: .knowledge/lint/drift-<date>.json
Weekly digest: last 7 drift files are summarized in the response summary.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from gateway import log, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter.semantic import FilterClient


def _today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _drift_dir() -> Path:
    return paths.knowledge_internal() / "lint"


def _drift_path(date_str: str) -> Path:
    return _drift_dir() / f"drift-{date_str}.json"


def _serialize_findings(findings: list) -> list[dict]:
    """Convert LintFindings to stable, sortable dicts for JSON diff."""
    out = []
    for f in findings:
        if f.check != "contradictions":
            continue
        out.append({
            "domain": f.metadata.get("domain", ""),
            "a_page": f.metadata.get("a_page", ""),
            "b_page": f.metadata.get("b_page", ""),
            "rationale": f.metadata.get("rationale", ""),
        })
    # Sort for stable diff
    return sorted(out, key=lambda x: (x["domain"], x["a_page"], x["b_page"]))


def _finding_key(item: dict) -> str:
    return f"{item['domain']}|{item['a_page']}|{item['b_page']}"


def _diff(previous: list[dict], current: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return (new_items, resolved_items) by key comparison."""
    prev_keys = {_finding_key(x) for x in previous}
    curr_keys = {_finding_key(x) for x in current}
    new = [x for x in current if _finding_key(x) not in prev_keys]
    resolved = [x for x in previous if _finding_key(x) not in curr_keys]
    return new, resolved


def _load_snapshot(date_str: str) -> list[dict]:
    p = _drift_path(date_str)
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text())
        return data.get("findings", [])
    except Exception:
        return []


def _weekly_digest(today: str) -> str:
    """Summarize new contradictions from the last 7 drift snapshots."""
    lines = ["### Contradiction drift — last 7 days", ""]
    total_new = 0
    for i in range(7):
        dt = datetime.fromisoformat(today) - timedelta(days=i)
        date_str = dt.strftime("%Y-%m-%d")
        p = _drift_path(date_str)
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text())
        except Exception:
            continue
        new_count = len(data.get("new", []))
        resolved_count = len(data.get("resolved", []))
        total_new += new_count
        lines.append(f"- {date_str}: {new_count} new, {resolved_count} resolved")
    lines.append(f"\nTotal new contradictions (7d): {total_new}")
    return "\n".join(lines)


def run_contradiction_drift(
    *,
    client: FilterClient | None = None,
    date_str: str | None = None,
    include_digest: bool = False,
) -> OperationResult:
    """Run contradictions lint, save JSON snapshot, diff against yesterday."""
    from gateway.lint.contradictions import run as contradictions_run

    today = date_str or _today_str()
    yesterday = (datetime.fromisoformat(today) - timedelta(days=1)).strftime("%Y-%m-%d")

    findings = contradictions_run(client=client)
    current = _serialize_findings(findings)
    previous = _load_snapshot(yesterday)
    new, resolved = _diff(previous, current)

    snapshot = {
        "date": today,
        "total": len(current),
        "new": new,
        "resolved": resolved,
        "findings": current,
    }

    out_path = _drift_path(today)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(out_path, json.dumps(snapshot, indent=2))

    log.append(
        op="contradiction-drift",
        fields={"date": today, "total": len(current), "new": len(new), "resolved": len(resolved)},
        summary=f"drift-{today}: {len(current)} total, {len(new)} new, {len(resolved)} resolved",
    )

    summary_parts = [
        f"contradiction-drift {today}: {len(current)} total, "
        f"{len(new)} new, {len(resolved)} resolved → {out_path.name}"
    ]
    if include_digest:
        summary_parts.append(_weekly_digest(today))

    return OperationResult(
        success=True,
        paths_touched=[out_path, paths.log_path()],
        summary="\n".join(summary_parts),
    )
