"""ONT-13: last_verified_at coverage and staleness check for time-sensitive entities.

Entity pages whose `entity_kind` is 'statute' or 'standard' must carry a
`last_verified_at` timestamp — the date a human last confirmed the record is
still accurate. Statutes are amended; standards are revised; stale entries
silently mislead downstream synthesis.

Severity contract:
- ERROR: statute/standard page missing `last_verified_at` entirely.
- WARNING: `last_verified_at` present but older than STALE_DAYS days (365).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from gateway import frontmatter as fm, paths
from gateway.core import parse_iso
from gateway.lint import LintFinding, SEVERITY_ERROR, SEVERITY_WARNING

STALE_DAYS: int = 365
_TIME_SENSITIVE_KINDS: frozenset[str] = frozenset({"statute", "regulation", "standard"})


def run() -> list[LintFinding]:
    entity_dir = paths.wiki_dir() / "entities"
    if not entity_dir.exists():
        return []

    now = datetime.now(tz=timezone.utc)
    cutoff = now - timedelta(days=STALE_DAYS)
    findings: list[LintFinding] = []

    for p in sorted(entity_dir.glob("*.md")):
        try:
            front, _ = fm.parse(p.read_text())
        except Exception:
            continue

        entity_kind = front.get("entity_kind")
        if entity_kind not in _TIME_SENSITIVE_KINDS:
            continue

        slug = front.get("slug", p.stem)
        rel = str(p.relative_to(paths.knowledge_root()))
        raw_value = front.get("last_verified_at")

        if raw_value is None:
            findings.append(
                LintFinding(
                    check="stale-verified",
                    severity=SEVERITY_ERROR,
                    message=(
                        f"{entity_kind} entity '{slug}' missing `last_verified_at` — "
                        "add the date you last confirmed this record is current "
                        "(ONT-13)"
                    ),
                    path=rel,
                    metadata={"slug": slug, "entity_kind": entity_kind},
                )
            )
            continue

        verified_at = parse_iso(raw_value)
        if verified_at is None:
            findings.append(
                LintFinding(
                    check="stale-verified",
                    severity=SEVERITY_ERROR,
                    message=(
                        f"{entity_kind} entity '{slug}' has unparseable "
                        f"`last_verified_at`: {raw_value!r} — use ISO-8601 "
                        "(e.g. 2025-01-15T00:00:00Z)"
                    ),
                    path=rel,
                    metadata={"slug": slug, "entity_kind": entity_kind, "raw_value": str(raw_value)},
                )
            )
            continue

        if verified_at < cutoff:
            days_ago = (now - verified_at).days
            findings.append(
                LintFinding(
                    check="stale-verified",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"{entity_kind} entity '{slug}' last verified {days_ago} days ago "
                        f"(>{STALE_DAYS}d) — re-verify and update `last_verified_at` "
                        "(ONT-13)"
                    ),
                    path=rel,
                    metadata={
                        "slug": slug,
                        "entity_kind": entity_kind,
                        "last_verified_at": raw_value,
                        "days_since_verified": days_ago,
                    },
                )
            )

    return findings
