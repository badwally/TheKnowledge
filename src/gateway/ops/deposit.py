"""Typed deposit op — the build-tier agent entrypoint (Phase-3 Task 8, decision 3/4).

A deposit is validated for its typed Intent shape, enqueued DURABLY to the queue's
``submitted/`` directory BEFORE the call returns (so a crash after ack never loses
the intent), and acknowledged with an async receipt (``disposition="queued"`` +
``intent_id`` + ``retry_after``). Authoring runs concurrently on workers (no global
``wiki-author`` lock); only the commit step is serial (CommitGate). The caller polls
``wiki_intent_status`` for the terminal disposition.
"""

from __future__ import annotations

from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id


# Valid deposit page types (typed shape). Unknown types are rejected before enqueue.
_DEPOSIT_PAGE_TYPES = frozenset({"entity", "concept", "source", "synthesis"})

# Default poll-interval hint (seconds) on the async receipt.
_RETRY_AFTER = 2


def _validate(payload: dict) -> list[str]:
    """Return a list of validation errors for the typed deposit shape (empty = ok)."""
    errors: list[str] = []
    ptype = payload.get("page_type")
    if ptype not in _DEPOSIT_PAGE_TYPES:
        errors.append(
            f"unknown page_type {ptype!r}; expected one of "
            f"{sorted(_DEPOSIT_PAGE_TYPES)}"
        )
        return errors
    if not str(payload.get("title", "")).strip():
        errors.append("deposit requires a non-empty title")
    if not str(payload.get("body", "")).strip() and ptype != "synthesis":
        errors.append("deposit requires a non-empty body")
    if ptype == "synthesis":
        syn = payload.get("synthesizes")
        if not isinstance(syn, list) or not syn:
            errors.append("synthesis deposit requires a non-empty synthesizes list")
    return errors


def deposit(
    payload: dict,
    identity: dict,
    *,
    depends_on: str | None = None,
    queue: IntentQueue | None = None,
) -> OperationResult:
    """Validate, durably enqueue, and acknowledge a typed deposit (async)."""
    errors = _validate(payload)
    if errors:
        return OperationResult(
            success=False,
            disposition="rejected",
            errors=errors,
            summary=f"deposit rejected: {errors[0]}",
        )

    q = queue or IntentQueue()
    # Carry the page_type into identity so the CommitGate's dedup re-check + domain
    # resolution + contradiction detection can read it without re-parsing payload.
    ident = dict(identity)
    ident.setdefault("page_type", payload["page_type"])
    iid = compute_intent_id(payload, ident, semantics="deposit")
    intent = Intent(
        intent_id=iid, payload=payload, identity=ident, depends_on=depends_on
    )
    # Durable: submit() writes to submitted/ before returning (decision 3).
    q.submit(intent)
    return OperationResult(
        success=True,
        intent_id=iid,
        disposition="queued",
        retry_after=_RETRY_AFTER,
        summary=f"deposit queued as {iid}",
    )
