"""Stale-drafts check per WIKI § 5.5 / § 12.2.

Flags wiki pages with `draft: true` whose `draft_started_at` is older
than the staleness threshold (default 7 days).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from gateway import paths
from gateway.core import parse_iso
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


DEFAULT_STALENESS_DAYS = 7


def run(*, threshold_days: int = DEFAULT_STALENESS_DAYS) -> list[LintFinding]:
    findings: list[LintFinding] = []
    threshold = timedelta(days=threshold_days)
    now = datetime.now(timezone.utc)

    for type_name, path, front, body in walk_wiki_pages():
        if not front.get("draft"):
            continue
        started_raw = front.get("draft_started_at")
        if not started_raw:
            continue
        started = parse_iso(str(started_raw))
        if started is None:
            continue
        age = now - started
        if age > threshold:
            unresolved = front.get("draft_unresolved_claims", "?")
            findings.append(
                LintFinding(
                    check="stale-drafts",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"draft is {age.days} days old (threshold {threshold_days}); "
                        f"unresolved claims: {unresolved}"
                    ),
                    path=str(path.relative_to(paths.knowledge_root())),
                    metadata={
                        "age_days": age.days,
                        "unresolved_claims": unresolved,
                        "started_at": str(started_raw),
                    },
                )
            )
    return findings
