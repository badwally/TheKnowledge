"""revert-resolution op — Phase 5 Task 1, G1.

A revert-resolution is a provenanced, reversible CommitGate intent that
undoes an auto_resolve act. It is build-tier (enqueues a mutation) — never
a direct in-place mutation.

Pattern mirrors ops/deposit.py:
  validate → compute_intent_id → Intent → queue.submit → OperationResult(queued).

The CommitGate apply-path for reversal_type="contradiction-resolution" is
wired in commit_gate.py (keyed on payload["reversal_type"]). The gate removes
the ## Contested / disputes edge and restores the claim's open status, then
records a provenance node with reverts_act set.
"""

from __future__ import annotations

from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id


_REVERSAL_POLICY_VERSION = "contradiction-reversal-policy-v1"
_RETRY_AFTER = 2


def revert_resolution(
    act_id: str,
    identity: dict,
    *,
    queue: IntentQueue | None = None,
) -> OperationResult:
    """Validate and durably enqueue a contradiction-resolution reversal intent.

    Args:
        act_id: The resolved_at act id to revert (must be non-empty).
        identity: Caller-supplied identity dict (agent, session, etc.). The
            operation key is injected automatically.
        queue: Optional IntentQueue override (for testing). Defaults to
            IntentQueue() which resolves via KNOWLEDGE_ROOT.

    Returns:
        OperationResult with disposition="queued" on success, or
        disposition="rejected" if validation fails.
    """
    if not str(act_id).strip():
        return OperationResult(
            success=False,
            disposition="rejected",
            errors=["revert-resolution requires a non-empty act_id"],
            summary="revert-resolution rejected: empty act_id",
        )

    payload = {
        "reversal_type": "contradiction-resolution",
        "reverts_act": act_id,
        "policy_version": _REVERSAL_POLICY_VERSION,
    }

    # Inject the operation name into identity (mirrors deposit.py's page_type inject)
    ident = dict(identity)
    ident["operation"] = "revert-resolution"

    iid = compute_intent_id(payload, ident, semantics="revert")

    q = queue or IntentQueue()
    intent = Intent(intent_id=iid, payload=payload, identity=ident)
    q.submit(intent)

    return OperationResult(
        success=True,
        intent_id=iid,
        disposition="queued",
        retry_after=_RETRY_AFTER,
        summary=f"revert-resolution queued as {iid} (reverts act {act_id!r})",
    )
