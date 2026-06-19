"""G7 — policy-provenance lint check: out-of-band policy-edit detector.

Flags any live policy.yaml whose last change lacks a ``policy-edit`` provenance
node. This is the runtime guard against out-of-band edits (direct file writes
that bypass the privileged CommitGate intent path).

Severity: error — an unprovenanced policy edit circumvents the change-control
that guards life-critical corpus behaviour (dedup/trust/contradiction).

Boundary note (hardcoded threshold constants):
    Threshold constants (e.g. commit_gate.COMMIT_LOCK_ACQUIRE_TIMEOUT,
    deposit.MAX_BACKLOG) are NOT in scope for this runtime check. They are
    embedded in source code and are gated by code-review and merge — not by
    the policy-edit intent path. This lint checks policy.yaml files only.
    If you need to update a threshold constant, open a PR and get code-review
    approval; the merge is the gate.

Detection heuristic:
    For each live policy.yaml in ``.knowledge/policies/<domain>/``, check
    whether any provenance node in ``nodes.jsonl`` carries
    ``basis.op == "policy-edit"`` AND ``basis.domain == <domain>``. If none,
    the policy file is considered unprovenanced and a finding is emitted.

    Limitation: this heuristic detects the ABSENCE of a provenance node —
    it does not verify that the node was recorded for the current content of
    the file. A full content-hash check would require storing the hash in
    the provenance node at write time (tracked in the migration backlog at
    docs/backlog/librarian-policy-edit-migrate-existing-ops.md).
"""

from __future__ import annotations

import json
from pathlib import Path

from gateway import paths
from gateway.lint import LintFinding, SEVERITY_ERROR


def run(*, root: Path | None = None) -> list[LintFinding]:
    """Check all live policy.yaml files for policy-edit provenance coverage.

    Parameters
    ----------
    root:
        Optional KB root override (defaults to ``paths.knowledge_root()``).
        Passed by tests to avoid touching the real KB.

    Returns
    -------
    list[LintFinding]
        One ERROR finding per domain whose policy.yaml lacks a
        ``policy-edit`` provenance node.
    """
    kb_root = root or paths.knowledge_root()
    policies_dir = kb_root / ".knowledge" / "policies"
    nodes_path = kb_root / ".knowledge" / "provenance" / "nodes.jsonl"

    # --- Load provenance nodes for domains with policy-edit ops ---
    provenanced_domains: set[str] = set()
    if nodes_path.exists():
        with open(nodes_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    node = json.loads(line)
                except json.JSONDecodeError:
                    continue
                basis = node.get("basis") or {}
                if (
                    basis.get("op") == "policy-edit"
                    and basis.get("provenance_type") == "policy-edit"
                ):
                    domain = basis.get("domain")
                    if domain:
                        provenanced_domains.add(domain)

    # --- Check each live policy.yaml ---
    findings: list[LintFinding] = []
    if not policies_dir.exists():
        return findings

    for domain_dir in sorted(policies_dir.iterdir()):
        if not domain_dir.is_dir():
            continue
        policy_file = domain_dir / "policy.yaml"
        if not policy_file.exists():
            continue
        domain = domain_dir.name
        if domain not in provenanced_domains:
            findings.append(
                LintFinding(
                    check="policy-provenance",
                    severity=SEVERITY_ERROR,
                    message=(
                        f"domain {domain!r}: policy.yaml has no policy-edit provenance node "
                        f"— this indicates an out-of-band edit that bypassed the privileged "
                        f"CommitGate intent path. Run `wiki policy-edit` to re-apply via the "
                        f"change-control path. Note: hardcoded threshold constants "
                        f"(commit_gate.py, deposit.py) are gated by code-review, not this "
                        f"runtime path — update them via PR."
                    ),
                    path=str(policy_file.relative_to(kb_root)),
                    metadata={"domain": domain},
                )
            )

    return findings
