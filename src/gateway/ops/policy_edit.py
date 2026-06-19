"""G7 — privileged-intent policy-edit path.

Policy changes govern dedup/trust/contradiction behaviour corpus-wide. They
route through the CommitGate as a PRIVILEGED, typed intent — never a direct
file write. This module handles the enqueue side (allowlist check → validate
shape → submit intent); the CommitGate handles the apply side (eval-compare +
merge-map golden gate → write or dead-letter).

Allowlist
---------
The build-time allowlist is an explicit set of (agent, role) pairs. Adding a
new entry requires a code-review + merge — there is no runtime API to extend
it. This is intentional: privileged access to life-critical policy paths must
be gated by human review, not by a config file that an agent could update.

Hardcoded threshold constants (e.g. commit_gate.py's COMMIT_LOCK_ACQUIRE_TIMEOUT,
deposit.py's MAX_BACKLOG) are NOT gated by this runtime path; they require a
code-review and merge. This is documented here and in the lint/policy_provenance
message so the boundary is explicit, not silent.
"""

from __future__ import annotations

from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id

# ---------------------------------------------------------------------------
# Build-time allowlist for policy-edit privilege.
# An identity is allowed iff its (agent, role) pair appears in this set.
# Adding an entry requires code-review + merge — there is no runtime extension.
# ---------------------------------------------------------------------------
_ALLOWLIST: frozenset[tuple[str, str]] = frozenset(
    {
        ("librarian-admin", "policy-admin"),
    }
)

# Default poll-interval hint (seconds) on the async receipt.
_RETRY_AFTER = 2


def _is_allowlisted(identity: dict) -> bool:
    """Return True iff the identity's (agent, role) is on the build-time allowlist."""
    agent = identity.get("agent", "")
    role = identity.get("role", "")
    return (agent, role) in _ALLOWLIST


def _validate(domain: str, policy_data: dict, reason: str) -> list[str]:
    """Return a list of validation errors for the policy-edit shape (empty = ok)."""
    errors: list[str] = []
    if not domain or not isinstance(domain, str):
        errors.append("domain must be a non-empty string")
    if not policy_data or not isinstance(policy_data, dict):
        errors.append("policy_data must be a non-empty dict")
    if not reason or not isinstance(reason, str) or not reason.strip():
        errors.append("reason must be a non-empty string documenting the change motivation")
    return errors


def policy_edit(
    domain: str,
    policy_data: dict,
    *,
    identity: dict,
    reason: str,
    queue: IntentQueue | None = None,
) -> OperationResult:
    """Validate and enqueue a privileged policy-edit CommitGate intent.

    Parameters
    ----------
    domain:
        The domain slug whose policy.yaml will be updated.
    policy_data:
        The full new policy mapping (must be a non-empty dict).
    identity:
        Caller identity. Must match a build-time allowlist entry
        ``(agent, role)``; non-allowlisted identities are rejected before
        enqueue.
    reason:
        Human-readable motivation for the change (required; the CommitGate
        records it in the provenance node).
    queue:
        Optional IntentQueue override (defaults to the live queue).

    Returns
    -------
    OperationResult
        ``disposition="queued"`` on success.
        ``disposition="rejected"`` if identity is not allowlisted or
        validation fails.
    """
    q = queue or IntentQueue()

    # --- Allowlist check (must be first — before any other processing) ---
    if not _is_allowlisted(identity):
        agent = identity.get("agent", "<none>")
        role = identity.get("role", "<none>")
        return OperationResult(
            success=False,
            disposition="rejected",
            errors=[
                f"identity ({agent!r}, {role!r}) is not on the policy-edit allowlist; "
                "this is a privileged operation — add the (agent, role) pair to the "
                "build-time allowlist in ops/policy_edit.py via code-review"
            ],
            summary=f"policy-edit rejected: {agent!r} not allowlisted",
        )

    # --- Shape validation ---
    errors = _validate(domain, policy_data, reason)
    if errors:
        return OperationResult(
            success=False,
            disposition="rejected",
            errors=errors,
            summary=f"policy-edit validation failed: {errors[0]}",
        )

    # --- Compute policy_version: current + 1 (monotone bump) ---
    current_version = int(policy_data.get("version", 1))
    policy_version = current_version

    # --- Enqueue the typed CommitGate intent ---
    payload: dict = {
        "op": "policy-edit",
        "domain": domain,
        "policy_data": policy_data,
        "reason": reason,
        "policy_version": policy_version,
    }
    iid = compute_intent_id(payload, identity, semantics=f"policy-edit:{domain}")
    intent = Intent(
        intent_id=iid,
        payload=payload,
        identity=identity,
        head_oid="HEAD",
    )
    q.submit(intent)

    return OperationResult(
        success=True,
        intent_id=iid,
        disposition="queued",
        retry_after=_RETRY_AFTER,
        summary=f"policy-edit enqueued for domain {domain!r} ({reason!r})",
    )
