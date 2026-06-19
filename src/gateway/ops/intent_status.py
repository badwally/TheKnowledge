"""Status-query op — Librarian Phase 1 (T1.3, A1).

Maps an ``intent_id`` to its terminal disposition union (design §3):

    committed     -> path (canonical_path)
    merged        -> canonical-path (a *different* page than the agent named)
    rejected      -> rule (reason in summary)
    quarantined   -> queue (reason in summary)
    dead_lettered -> reason (reason in summary)

On a non-terminal state (submitted / claimed / authored) it returns a
``retry_after`` poll-interval hint («deposit.max_wait»). There is no
push/callback in the stdio MCP surface — the agent polls; after a bounded total
wait it proceeds on carried-forward content (§12). A read-tier op: it never
takes the commit mutex.
"""

from __future__ import annotations

from pathlib import Path

from gateway.core import OperationResult
from gateway.intent_queue import IntentQueue


# «deposit.max_wait» (ledger §1.1) — the poll-interval hint on non-terminal status.
DEFAULT_RETRY_AFTER = 30

_NON_TERMINAL = {"submitted", "claimed", "authored"}


def intent_status(
    intent_id: str, *, queue: IntentQueue | None = None
) -> OperationResult:
    """Return the typed disposition for ``intent_id``."""
    q = queue or IntentQueue()
    state = q.get_state(intent_id)
    if state is None:
        return OperationResult(
            success=False,
            intent_id=intent_id,
            errors=[f"unknown intent_id: {intent_id}"],
            summary=f"no intent {intent_id}",
        )

    result = q.get_result(intent_id)

    if state in _NON_TERMINAL:
        return OperationResult(
            success=True,
            intent_id=intent_id,
            disposition=state,
            retry_after=DEFAULT_RETRY_AFTER,
            summary=f"{intent_id}: {state} (poll again in {DEFAULT_RETRY_AFTER}s)",
        )

    if state == "committed":
        # A merge sets result.disposition='merged' with a canonical_path that
        # differs from the deposited target.
        disposition = result.get("disposition", "committed")
        canonical = result.get("canonical_path")
        return OperationResult(
            success=True,
            intent_id=intent_id,
            disposition=disposition,
            canonical_path=Path(canonical) if canonical else None,
            summary=f"{intent_id}: {disposition} -> {canonical or '(no path)'}",
        )

    # rejected / dead_lettered (and any quarantine modeled via result reason).
    reason = result.get("reason", result.get("disposition", state))
    return OperationResult(
        success=True,
        intent_id=intent_id,
        disposition=state,
        summary=f"{intent_id}: {state} ({reason})",
    )
