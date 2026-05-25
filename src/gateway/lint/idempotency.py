"""Idempotency drift check — state-file vs on-disk consistency.

Surfaces cases where the registry (nlm/notebooks.yaml) records sessions
or domain entries that are inconsistent with on-disk state:

- `stale-session`: sessions with `ephemeral` status older than 24h.
  These likely represent crashed runs that were never abandoned.
  Resolution: `wiki nlm-abandon <domain> <session_id>` or re-run.

- `no-policy`: domains in the registry with no corresponding policy file
  at `.knowledge/policies/<domain>/policy.yaml`.
  Resolution: `wiki bootstrap-domain` or remove the registry entry.
"""

from __future__ import annotations

from datetime import datetime, timezone

from gateway import nlm_registry, paths
from gateway.filter.policy import policy_exists
from gateway.lint import LintFinding, SEVERITY_INFO, SEVERITY_WARNING

# Sessions that have been ephemeral longer than this threshold are flagged.
_STALE_SESSION_HOURS = 24


def _hours_since(created_at: str) -> float | None:
    try:
        ts = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        delta = datetime.now(timezone.utc) - ts
        return delta.total_seconds() / 3600
    except (ValueError, TypeError):
        return None


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []
    registry = nlm_registry.load()
    if not registry:
        return findings

    for domain, entry in registry.items():
        # Check for missing policy file.
        if not policy_exists(domain):
            findings.append(
                LintFinding(
                    check="idempotency",
                    severity=SEVERITY_WARNING,
                    message=(
                        f"domain {domain!r} is registered in nlm/notebooks.yaml "
                        f"but has no policy file at "
                        f".knowledge/policies/{domain}/policy.yaml"
                    ),
                    path=f"nlm/notebooks.yaml",
                    metadata={"domain": domain, "kind": "no-policy"},
                )
            )

        # Check for stale ephemeral sessions.
        for session_dict in nlm_registry.list_sessions(domain, status=nlm_registry.EPHEMERAL):
            created_at = session_dict.get("created_at", "")
            hours = _hours_since(created_at)
            if hours is not None and hours > _STALE_SESSION_HOURS:
                findings.append(
                    LintFinding(
                        check="idempotency",
                        severity=SEVERITY_INFO,
                        message=(
                            f"session {session_dict.get('session_id')!r} for domain "
                            f"{domain!r} has been ephemeral for "
                            f"{hours:.0f}h (>{_STALE_SESSION_HOURS}h threshold); "
                            f"consider abandoning or force-re-registering"
                        ),
                        path="nlm/notebooks.yaml",
                        metadata={
                            "domain": domain,
                            "session_id": session_dict.get("session_id"),
                            "created_at": created_at,
                            "hours_stale": round(hours, 1),
                            "kind": "stale-session",
                        },
                    )
                )

    return findings
