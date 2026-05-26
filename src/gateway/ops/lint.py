"""`wiki lint` orchestrator.

Composes all 10 checks per WIKI § 12.2 and writes a structured report to
.knowledge/lint/<UTC-timestamp>.md. Cheap checks default; LLM-heavy ones
are stubs in v1.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from gateway import log, paths
from gateway.core import OperationResult
from gateway.lint import LintFinding
from gateway.lint import (
    broken_wikilinks,
    citation_chains,
    citation_density,
    contradiction_pages,
    contradictions,
    domain_purity,
    filter_calibration,
    idempotency,
    inbox_pending,
    link_rot,
    long_slugs,
    missing_pages,
    nlm_pending,
    orphans,
    retracted_citations,
    schema_drift,
    stale_claims,
    stale_drafts,
    stale_verified,
    synthesizes_coverage,
    untagged_sources,
)


# Each check entry: (slug, runner). Order is the report order.
_CHECKS: list[tuple[str, Callable[[], list[LintFinding]]]] = [
    ("orphans", orphans.run),
    ("stale-drafts", stale_drafts.run),
    ("stale-claims", stale_claims.run),
    ("contradictions", contradictions.run),
    ("missing-pages", missing_pages.run),
    ("citation-density", citation_density.run),
    ("citation-chains", citation_chains.run),
    ("schema-drift", schema_drift.run),
    ("filter-calibration", filter_calibration.run),
    ("inbox-pending", inbox_pending.run),
    ("nlm-pending", nlm_pending.run),
    ("untagged-sources", untagged_sources.run),
    ("idempotency", idempotency.run),
    ("broken-wikilinks", broken_wikilinks.run),
    ("long-slugs", long_slugs.run),
    ("contradiction-pages", contradiction_pages.run),
    ("synthesizes-coverage", synthesizes_coverage.run),
    ("stale-verified", stale_verified.run),
    ("retracted-citations", retracted_citations.run),
    ("domain-purity", domain_purity.run),
    ("link-rot", link_rot.run),
]

KNOWN_CHECKS = {slug for slug, _ in _CHECKS}


@dataclass
class LintReport:
    timestamp: str
    counts: dict[str, int]
    findings: list[LintFinding] = field(default_factory=list)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _now_path_token() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")


def lint(*, scope: str | None = None) -> OperationResult:
    """Run all configured checks (or just `scope`) and write a report."""
    if scope is not None and scope not in KNOWN_CHECKS:
        return OperationResult(
            success=False,
            errors=[
                f"unknown lint scope {scope!r}; "
                f"known checks: {sorted(KNOWN_CHECKS)}"
            ],
        )

    report = LintReport(timestamp=_now_iso(), counts={})

    for slug, runner in _CHECKS:
        if scope is not None and slug != scope:
            continue
        try:
            findings = runner() or []
        except Exception as e:  # never let one check kill the rest
            findings = [
                LintFinding(
                    check=slug,
                    severity="error",
                    message=f"check raised an exception: {e!r}",
                )
            ]
        report.counts[slug] = len(findings)
        report.findings.extend(findings)

    report_path = _write_report(report, scope=scope)

    log.append(
        op="lint",
        fields={"scope": scope or "all", **report.counts},
        summary=f"report={report_path.relative_to(paths.knowledge_root())}",
    )

    summary_lines = [f"lint: {sum(report.counts.values())} finding(s)"]
    summary_lines.extend(
        f"  {slug}: {count}" for slug, count in report.counts.items() if count > 0
    )
    summary_lines.append(f"report: {report_path}")

    return OperationResult(
        success=True,
        paths_touched=[report_path, paths.log_path()],
        summary="\n".join(summary_lines),
    )


def _write_report(report: LintReport, *, scope: str | None) -> Path:
    """Persist the report as a Markdown summary."""
    target_dir = paths.lint_dir()
    target_dir.mkdir(parents=True, exist_ok=True)

    name = f"{_now_path_token()}{('-' + scope) if scope else ''}.md"
    target = target_dir / name

    lines: list[str] = [
        f"# Lint Report — {report.timestamp}",
        "",
        f"Scope: {scope or 'all'}",
        "",
        "## Summary",
        "",
    ]
    for slug, _ in _CHECKS:
        if slug not in report.counts:
            continue
        lines.append(f"- {slug}: {report.counts[slug]}")
    lines.append("")

    by_check: dict[str, list[LintFinding]] = {slug: [] for slug, _ in _CHECKS}
    for f in report.findings:
        by_check.setdefault(f.check, []).append(f)

    for slug, _ in _CHECKS:
        items = by_check.get(slug) or []
        if not items:
            continue
        lines.append(f"## {slug}")
        lines.append("")
        for f in items:
            line = f"- [{f.severity}] {f.message}"
            if f.path:
                line += f" — `{f.path}`"
            lines.append(line)
        lines.append("")

    target.write_text("\n".join(lines))
    return target
