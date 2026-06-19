"""Production committer: author_deposit + drain_once + run_worker (D0).

On-demand drain of the IntentQueue → CommitGate pipeline.

Usage:
    wiki commit-worker --once   # drain submitted queue to empty, then exit
    wiki commit-worker --loop   # foreground poll until SIGINT / KeyboardInterrupt

Design:
- author_deposit() is a thin renderer: body passes through VERBATIM; frontmatter
  mirrors the _authored_entity fixture convention (fm.serialize + slug from title).
- drain_once() claims one intent, authors it, commits via CommitGate, returns
  DrainResult. Returns None when the queue is empty.
- run_worker() loops drain_once() until empty (once=True) or until signalled
  (once=False). Each iteration is independent — a poison intent dead-letters via
  the gate's own handler (not via a loop-level swallow), but a backstop except
  prevents one bad record from killing the loop.
"""

from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone

from gateway import frontmatter as fm
from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.core import OperationResult

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Page-type directory map
# ---------------------------------------------------------------------------

_PAGE_TYPE_DIR: dict[str, str] = {
    "entity": "wiki/entities",
    "concept": "wiki/concepts",
    "source": "wiki/sources",
    "synthesis": "wiki/synthesis",
}


# ---------------------------------------------------------------------------
# Public return type
# ---------------------------------------------------------------------------


@dataclass
class DrainResult:
    """Result of a single drain_once() cycle."""

    disposition: str                   # committed / merged / dead_lettered / retry-later / ...
    intent_id: str
    detail: str = ""
    errors: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------


def _title_to_slug(title: str) -> str:
    """Lowercase, replace non-alphanumeric runs with hyphens, strip leading/trailing."""
    cleaned = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return cleaned


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# author_deposit
# ---------------------------------------------------------------------------


def author_deposit(intent: Intent, gate: CommitGate | None = None) -> AuthoredIntent:
    """Render a deposit intent into an AuthoredIntent (writes dict).

    Body is passed through VERBATIM (agent-supplied markdown).
    Frontmatter mirrors the _authored_entity fixture: fm.serialize over the
    canonical key set per page_type, slug derived from title.

    If ``gate`` is provided, the real HEAD blob OID for the target file is
    captured at authoring time so the CAS can classify a concurrent edit as a
    mergeable "rebase" rather than a "contradictory" phantom (write-skew path).

    Supports: entity, concept, synthesis. (source deposits via CommitGate are
    uncommon; not rendered here — raise ValueError so the gate dead-letters.)
    """
    payload = intent.payload
    page_type = payload.get("page_type")
    title = str(payload.get("title", "")).strip()
    body = str(payload.get("body", ""))

    if not title:
        raise ValueError(f"author_deposit: empty title in intent {intent.intent_id!r}")
    if page_type not in _PAGE_TYPE_DIR:
        raise ValueError(
            f"author_deposit: unsupported page_type {page_type!r} in intent {intent.intent_id!r}"
        )

    slug = _title_to_slug(title)
    now = _now_iso()
    page_dir = _PAGE_TYPE_DIR[page_type]
    rel = f"{page_dir}/{slug}.md"

    if page_type == "entity":
        front: dict = {
            "type": "entity",
            "slug": slug,
            "canonical_name": title,
            "entity_kind": payload.get("entity_kind") or "drug",
            "domains": list(payload.get("domains") or []),
            "created_at": now,
            "last_updated": now,
        }
        aliases = list(payload.get("aliases") or [])
        if aliases:
            front["aliases"] = aliases

    elif page_type == "concept":
        front = {
            "type": "concept",
            "slug": slug,
            "canonical_name": title,
            "domains": list(payload.get("domains") or []),
            "created_at": now,
            "last_updated": now,
        }
        aliases = list(payload.get("aliases") or [])
        if aliases:
            front["aliases"] = aliases

    elif page_type == "synthesis":
        synthesizes = list(payload.get("synthesizes") or [])
        front = {
            "type": "synthesis",
            "slug": slug,
            "title": title,
            "domains": list(payload.get("domains") or []),
            "question": title,
            "created_at": now,
            "last_updated": now,
            "sources_count": len(synthesizes),
            "synthesizes": synthesizes,
        }

    else:
        raise ValueError(
            f"author_deposit: page_type {page_type!r} not renderable by thin renderer"
        )

    content = fm.serialize(front, body)

    # Capture the real HEAD blob OID for this file at authoring time.
    # This enables the CAS to classify a concurrent edit as "rebase" (mergeable)
    # rather than "contradictory" (phantom) when two deposits target the same page.
    base_blob: str | None = None
    if gate is not None:
        base_blob = gate._head_blob_oid(rel)

    authored = AuthoredIntent(
        intent=intent,
        writes={rel: content},
        base_oid="HEAD",
        base_oids={rel: base_blob},
    )
    return authored


# ---------------------------------------------------------------------------
# drain_once
# ---------------------------------------------------------------------------


def drain_once(
    queue: IntentQueue,
    gate: CommitGate,
    *,
    lease_ttl: float = 120.0,
) -> DrainResult | None:
    """Claim one intent, author it, commit it. Return DrainResult or None if empty.

    Disposition values mirror CommitGate.commit() OperationResult.disposition:
    committed / merged / dead_lettered / retry-later / quarantined / rejected.
    """
    claim = queue.claim(lease_ttl=lease_ttl)
    if claim is None:
        return None

    intent = claim.intent
    intent_id = intent.intent_id

    try:
        authored = author_deposit(intent, gate)
    except Exception as exc:
        # author_deposit raised (e.g. empty title, unsupported page_type).
        # Dead-letter manually: record via CommitGate's _dead_letter path by
        # building a minimal AuthoredIntent with no writes and committing it;
        # or directly set queue state to dead_lettered.
        log.warning("author_deposit failed for %s: %s", intent_id, exc)
        try:
            queue.set_state(intent_id, "dead_lettered", result={"error": str(exc)})
        except Exception as inner:
            log.error("could not dead-letter %s: %s", intent_id, inner)
        return DrainResult(
            disposition="dead_lettered",
            intent_id=intent_id,
            detail=str(exc),
            errors=[str(exc)],
        )

    result: OperationResult = gate.commit(authored, claim.fencing_token)
    disposition = result.disposition or ("committed" if result.success else "failed")

    return DrainResult(
        disposition=disposition,
        intent_id=intent_id,
        detail=result.summary,
        errors=list(result.errors),
    )


# ---------------------------------------------------------------------------
# run_worker
# ---------------------------------------------------------------------------


def run_worker(
    *,
    once: bool = False,
    poll_interval: float = 2.0,
    queue: IntentQueue | None = None,
    gate: CommitGate | None = None,
) -> None:
    """Drain the queue once (once=True) or poll indefinitely (once=False).

    Each iteration is independent. A poison intent dead-letters (either via the
    gate's own CAS pipeline or via the backstop in drain_once), and the loop
    CONTINUES — it does not abort.

    The backstop except here is a final safety net for unexpected drain_once
    failures (e.g. a completely malformed record that drain_once itself cannot
    handle). Normal bad intents dead-letter via the gate, not via this catch.
    """
    q = queue or IntentQueue()
    g = gate or CommitGate(queue=q)

    if once:
        while True:
            try:
                result = drain_once(q, g)
            except Exception as exc:
                log.error("drain_once raised unexpectedly: %s", exc)
                # Brief pause to avoid a tight spin on a persistently broken record.
                time.sleep(0.1)
                continue
            if result is None:
                break
            log.info("drained %s → %s", result.intent_id, result.disposition)
    else:
        try:
            while True:
                try:
                    result = drain_once(q, g)
                except Exception as exc:
                    log.error("drain_once raised unexpectedly: %s", exc)
                    time.sleep(poll_interval)
                    continue
                if result is not None:
                    log.info("drained %s → %s", result.intent_id, result.disposition)
                else:
                    time.sleep(poll_interval)
        except KeyboardInterrupt:
            log.info("commit-worker interrupted; exiting.")
