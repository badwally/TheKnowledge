"""Inbox-pending check per WIKI § 12.2.

Counts files in raw/inbox/ awaiting routing (excluding the _failed/
quarantine directory and dotfiles). Severity is info — pending files are
not a problem, but visibility helps.
"""

from __future__ import annotations

from gateway import paths
from gateway.lint import LintFinding, SEVERITY_INFO


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    inbox = paths.raw_dir() / "inbox"
    if not inbox.exists():
        return findings

    pending = [
        p
        for p in sorted(inbox.iterdir())
        if p.is_file() and p.suffix == ".md" and not p.name.startswith(".")
    ]
    if pending:
        findings.append(
            LintFinding(
                check="inbox-pending",
                severity=SEVERITY_INFO,
                message=f"{len(pending)} markdown file(s) in raw/inbox/ awaiting routing",
                metadata={"files": [p.name for p in pending], "count": len(pending)},
            )
        )

    failed_dir = inbox / "_failed"
    if failed_dir.exists():
        failed_count = sum(
            1
            for p in failed_dir.iterdir()
            if p.is_file() and p.suffix == ".md"
        )
        if failed_count > 0:
            findings.append(
                LintFinding(
                    check="inbox-pending",
                    severity=SEVERITY_INFO,
                    message=f"{failed_count} file(s) quarantined in raw/inbox/_failed/",
                    metadata={"count": failed_count, "kind": "failed"},
                )
            )

    return findings
