"""Typed deposit op — the build-tier agent entrypoint (Phase-3 Task 8, decision 3/4).

A deposit is validated for its typed Intent shape, enqueued DURABLY to the queue's
``submitted/`` directory BEFORE the call returns (so a crash after ack never loses
the intent), and acknowledged with an async receipt (``disposition="queued"`` +
``intent_id`` + ``retry_after``). Authoring runs concurrently on workers (no global
``wiki-author`` lock); only the commit step is serial (CommitGate). The caller polls
``wiki_intent_status`` for the terminal disposition.
"""

from __future__ import annotations

import re

from gateway import paths
from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id

# --- Keep-worthiness field schema -------------------------------------------
#
# These optional fields encode a deposit's expected durability and importance.
# Each entry is (field_name, allowed_non-None-types, description):
#   half_life:   str or None   — "short"/"medium"/"long"/... — how long the claim stays valid
#   load_bearing: bool or None — True if removing this claim breaks downstream pages
#   domain_core:  bool or None — True if the claim is part of the domain's core knowledge
#   recurrence:   int or None  — how many times this topic has recurred (demand signal)
#   durable:      bool or None — True if the claim is intended to persist long-term
#   volatile:     bool or None — True if the claim is fast-moving / not for canonicalization
#
# Wrong type (not None, not an allowed type) → rejected.

_KEEP_WORTHINESS_SCHEMA: dict[str, tuple[type, ...]] = {
    "half_life": (str,),
    "load_bearing": (bool,),
    "domain_core": (bool,),
    "recurrence": (int,),
    "durable": (bool,),
    "volatile": (bool,),
}

# Wikilink pattern for [[sources/<id>]] — used by the orient-vs-ground gate.
_SOURCE_WIKILINK_RE = re.compile(r"\[\[sources/([^\]\|#]+?)(?:[#|][^\]]+)?\]\]")


# Valid deposit page types (typed shape). Unknown types are rejected before enqueue.
_DEPOSIT_PAGE_TYPES = frozenset({"entity", "concept", "source", "synthesis"})

# Default poll-interval hint (seconds) on the async receipt.
_RETRY_AFTER = 2

# Server-side shed ceiling «deposit.max_backlog»: when the submitted backlog is at
# or above this, deposit sheds load (A1 backpressure) so producers back off rather
# than growing an unbounded queue. «deposit.max_wait» (agent total-wait bound) is a
# separate, agent-facing contract surfaced via retry_after.
MAX_BACKLOG = 256


def _has_ingested_source(body: str) -> bool:
    """Return True if body contains [[sources/<id>]] resolving to a real raw/ page.

    Resolution: source ID encodes the type as a prefix (e.g. "web-1" → raw/web/web-1.md,
    "pubmed-19528002" → raw/pubmed/pubmed-19528002.md). We try each SOURCE_TYPES prefix
    to resolve the id.
    """
    raw_dir = paths.raw_dir()
    for m in _SOURCE_WIKILINK_RE.finditer(body):
        source_id = m.group(1).strip()
        # Determine the source type from the id prefix (the part before the first dash-digit).
        # Source types: see paths.SOURCE_TYPES. We try each as a directory prefix.
        for src_type in paths.SOURCE_TYPES:
            candidate = raw_dir / src_type / f"{source_id}.md"
            if candidate.is_file():
                return True
    return False


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
    body = str(payload.get("body", ""))
    if not body.strip() and ptype != "synthesis":
        errors.append("deposit requires a non-empty body")
    if ptype == "synthesis":
        syn = payload.get("synthesizes")
        if not isinstance(syn, list) or not syn:
            errors.append("synthesis deposit requires a non-empty synthesizes list")

    # --- Keep-worthiness field type validation ---
    for field_name, allowed_types in _KEEP_WORTHINESS_SCHEMA.items():
        if field_name not in payload:
            continue  # field absent → ok (optional)
        value = payload[field_name]
        if value is None:
            continue  # None is always allowed (nullable)
        # bool subclasses int, so isinstance(True, (int,)) is True. Reject bool
        # for int-typed fields (e.g. recurrence=True) — it would silently inflate
        # the T4 DemandLedger recurrence counts. bool is only accepted when bool
        # is itself an allowed type for the field.
        is_bool = isinstance(value, bool)
        bool_allowed = bool in allowed_types
        type_ok = isinstance(value, allowed_types) and (bool_allowed or not is_bool)
        if not type_ok:
            type_names = "/".join(t.__name__ for t in allowed_types)
            errors.append(
                f"{field_name} must be {type_names} or None, got {type(value).__name__!r}"
            )

    # --- Orient-vs-ground gate ---
    # A durable claim must be backed by at least one [[sources/<id>]] resolving
    # to a real raw/ page. A bare URL or a broken [[sources/...]] wikilink is
    # NOT sufficient — the source must have been ingested first.
    durable = payload.get("durable")
    if durable and not errors:  # skip gate if already invalid
        if not _has_ingested_source(body):
            errors.append(
                "durable claim requires at least one ingested source "
                "([[sources/<id>]] resolving to a real raw/ page); "
                "ingest the source first or use durable=False"
            )

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

    if q.depth() >= MAX_BACKLOG:
        return OperationResult(
            success=False,
            disposition="rejected:overloaded",
            retry_after=_RETRY_AFTER,
            errors=["deposit queue is at capacity; retry after backoff"],
            summary="deposit shed: queue overloaded",
        )

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

    # Volatile deposits are not canonicalized — surface this to the caller so
    # downstream workers skip the CommitGate canonicalization step.
    extra_data: dict | None = None
    if payload.get("volatile"):
        extra_data = {"canonicalize": False}

    return OperationResult(
        success=True,
        intent_id=iid,
        disposition="queued",
        retry_after=_RETRY_AFTER,
        summary=f"deposit queued as {iid}",
        data=extra_data,
    )
