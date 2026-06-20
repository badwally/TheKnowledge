"""Production committer: author_deposit + drain_once + run_worker (D0).

On-demand drain of the IntentQueue → CommitGate pipeline.

Usage:
    wiki commit-worker --once   # drain submitted queue to empty, then exit
    wiki commit-worker --loop   # foreground poll until SIGINT / KeyboardInterrupt

Design:
- author_deposit() is a thin renderer: body passes through VERBATIM; frontmatter
  mirrors the _authored_entity fixture convention (fm.serialize + slug from title).
  When the target page already exists (same-slug second deposit), the new deposit's
  claims are unioned into the existing page rather than overwriting it.
- drain_once() reclaims expired leases before claiming (crash recovery), then
  claims one intent, authors it, commits via CommitGate, returns DrainResult.
  Returns None when the queue is empty.
- run_worker() calls gate.recover() at startup (crash recovery: revert partial
  writes, reclaim), then loops drain_once() until empty (once) or until signalled
  (loop). Each iteration is independent — a poison intent dead-letters via the
  gate's own handler (not via a loop-level swallow), but a backstop except
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
from gateway.intent_queue import Intent, IntentQueue
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
# Same-slug union helper
# ---------------------------------------------------------------------------


def _union_same_slug(existing_content: str, new_body: str) -> str | None:
    """Union new_body's ``## Claims`` bullets into existing_content's body.

    Returns the merged full document (frontmatter + unioned body), or None if
    the union cannot be applied cleanly (new_body contains non-bullet lines
    beyond a Claims section header, which would be a structural change that
    requires manual merge).

    Strategy: extract net-new bullet lines from new_body (lines starting with
    "- " that are not already in existing_body) and append them to the existing
    body. Non-bullet content in new_body (beyond the ## Claims header) is
    rejected → caller dead-letters (needs-manual-merge).

    The existing page's frontmatter is preserved with last_updated refreshed.
    """
    try:
        existing_front, existing_body = fm.parse(existing_content)
    except Exception:
        return None

    # Update last_updated in-place so the merged page reflects the new write time.
    existing_front["last_updated"] = _now_iso()

    # Parse new_body: accept only bullet additions (lines starting with "- ")
    # and ## Claims section headers. Any other non-empty, non-whitespace line
    # is a structural change → cannot union blindly.
    existing_lines = existing_body.splitlines()
    existing_set = set(existing_lines)

    new_lines = new_body.splitlines()
    net_new_bullets: list[str] = []
    for ln in new_lines:
        stripped = ln.strip()
        if not stripped:
            continue  # blank line — skip
        if stripped.lower().startswith("## claims"):
            continue  # Claims section header — skip (may already be present)
        if stripped.startswith("- "):
            if ln not in existing_set:
                net_new_bullets.append(ln)
        else:
            # Non-bullet, non-header content in the new body — structural change.
            return None

    if not net_new_bullets:
        # All new claims already present — idempotent; return existing unchanged.
        return fm.serialize(existing_front, existing_body)

    # Append net-new bullets; ensure a ## Claims section exists.
    merged_lines = list(existing_lines)
    if not any(ln.strip().lower().startswith("## claims") for ln in merged_lines):
        merged_lines += ["", "## Claims"]
    merged_lines += net_new_bullets
    merged_body = "\n".join(merged_lines)
    if not merged_body.endswith("\n"):
        merged_body += "\n"

    return fm.serialize(existing_front, merged_body)


# ---------------------------------------------------------------------------
# author_deposit
# ---------------------------------------------------------------------------


def author_deposit(intent: Intent, gate: CommitGate | None = None) -> AuthoredIntent:
    """Render a deposit intent into an AuthoredIntent (writes dict).

    Body is passed through VERBATIM (agent-supplied markdown).
    Frontmatter mirrors the _authored_entity fixture: fm.serialize over the
    canonical key set per page_type, slug derived from title.

    When gate is provided:
    - The real HEAD blob OID for the target file is captured at authoring time
      so the CAS can classify a concurrent edit as "rebase" rather than
      "contradictory" (write-skew path for cross-slug dedup union).
    - If the target file ALREADY EXISTS (same-slug second deposit), the new
      deposit's body claims are unioned into the existing page. This prevents
      silent overwrite of earlier claims. If the union fails (non-bullet
      contradiction), a ValueError is raised so the gate dead-letters.

    Supports: entity, concept, synthesis. (source deposits are uncommon;
    not rendered here — raise ValueError so the gate dead-letters.)

    Raises ValueError for: empty title, empty slug (all-punctuation title),
    unsupported page_type, or un-unionable same-slug body.
    """
    payload = intent.payload
    page_type = payload.get("page_type")
    title = str(payload.get("title", "")).strip()
    body = str(payload.get("body", ""))

    if not title:
        raise ValueError(f"author_deposit: empty title in intent {intent.intent_id!r}")
    if page_type not in _PAGE_TYPE_DIR:
        raise ValueError(
            f"author_deposit: unsupported page_type {page_type!r} "
            f"in intent {intent.intent_id!r}"
        )

    slug = _title_to_slug(title)
    if not slug:
        raise ValueError(
            f"author_deposit: title {title!r} produces empty slug "
            f"in intent {intent.intent_id!r}"
        )

    now = _now_iso()
    page_dir = _PAGE_TYPE_DIR[page_type]
    rel = f"{page_dir}/{slug}.md"

    if page_type == "entity":
        front: dict = {
            "type": "entity",
            "slug": slug,
            "canonical_name": title,
            "domains": list(payload.get("domains") or []),
            "created_at": now,
            "last_updated": now,
        }
        entity_kind = payload.get("entity_kind")
        if entity_kind:
            front["entity_kind"] = entity_kind
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
    base_blob: str | None = None
    if gate is not None:
        base_blob = gate._head_blob_oid(rel)

    if base_blob is not None:
        # The target page already exists in the committed tree (same-slug second deposit).
        # Union the new deposit's claims into the existing page rather than overwriting.
        existing_content = gate._blob_content(base_blob)
        if existing_content is not None:
            merged = _union_same_slug(existing_content, body)
            if merged is None:
                raise ValueError(
                    f"author_deposit: same-slug body union failed for {rel!r} "
                    f"in intent {intent.intent_id!r} — non-bullet change or contradiction; "
                    f"intent dead-lettered (needs-manual-merge)"
                )
            content = merged
        # After same-slug union, set base_oids[rel] = base_blob so the CAS
        # sees head_oid == base (no external change between authoring and commit)
        # and classifies as "commit" — clean apply of the merged content.

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


def _is_gate_dispatched(payload: dict) -> bool:
    """Return True if the intent should be routed directly to gate.commit() without
    going through author_deposit().

    The gate dispatches two non-deposit intent classes before reaching the deposit/
    dedup/contradiction pipeline:
      - ``reversal_type`` present  → gate._apply_reversal()     (Phase 5 T1/G1/G3/G8)
      - ``op == "policy-edit"``    → gate._apply_policy_edit()  (Phase 5 T6/G7)

    These intents carry no normal write set; the gate constructs their own writes
    internally. They must bypass author_deposit() (which requires page_type/title)
    and be handed to gate.commit() as an AuthoredIntent with writes={}.
    """
    if payload.get("reversal_type"):
        return True
    if payload.get("op") == "policy-edit":
        return True
    return False


def drain_once(
    queue: IntentQueue,
    gate: CommitGate,
    *,
    lease_ttl: float = 120.0,
) -> DrainResult | None:
    """Claim one intent, author it, commit it. Return DrainResult or None if empty.

    Reclaims expired leases from claimed/ before claiming so a crashed worker's
    intent is not permanently stranded (crash-reclaim production path, CRITICAL #1).

    Disposition values mirror CommitGate.commit() OperationResult.disposition:
    committed / merged / dead_lettered / retry-later / quarantined / rejected.

    A retry-later intent is moved back to submitted/ so a later pass can retry it.

    Intent routing (post-T2 D0 reopen):
      - reversal_type present or op=="policy-edit" → gate-dispatched: skips
        author_deposit and calls gate.commit() with AuthoredIntent(writes={}).
        The gate's own dispatch in commit() (commit_gate.py:333–351) routes to
        _apply_reversal / _apply_policy_edit, which construct their own writes.
      - page_type present (deposit) → author_deposit() → gate.commit() (existing path).
      - Neither: genuinely unknown → author_deposit raises ValueError → dead-letters.
    """
    # Crash recovery: return any expired leases to submitted/ before we try to claim.
    queue.reclaim_expired()

    claim = queue.claim(lease_ttl=lease_ttl)
    if claim is None:
        return None

    intent = claim.intent
    intent_id = intent.intent_id
    payload = intent.payload or {}

    if _is_gate_dispatched(payload):
        # Non-deposit gate-dispatched intent: build an empty-writes AuthoredIntent
        # and hand it to gate.commit(). The gate's dispatch block (commit_gate.py:333–351)
        # will route to _apply_reversal or _apply_policy_edit based on the payload keys.
        # The gate constructs the actual filesystem writes internally.
        authored = AuthoredIntent(
            intent=intent,
            writes={},
            base_oid="HEAD",
        )
        result: OperationResult = gate.commit(authored, claim.fencing_token)
        disposition = result.disposition or ("committed" if result.success else "failed")
        # retry-later: return to submitted/ for a future pass.
        if disposition == "retry-later":
            try:
                queue.set_state(intent_id, "submitted")
            except Exception as inner:
                log.error("could not re-queue retry-later intent %s: %s", intent_id, inner)
        return DrainResult(
            disposition=disposition,
            intent_id=intent_id,
            detail=result.summary,
            errors=list(result.errors),
        )

    try:
        authored = author_deposit(intent, gate)
    except Exception as exc:
        # author_deposit raised (e.g. empty title, empty slug, unsupported page_type,
        # or same-slug body-union failure). Dead-letter the intent.
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

    result = gate.commit(authored, claim.fencing_token)
    disposition = result.disposition or ("committed" if result.success else "failed")

    # For retry-later: move the intent back to submitted/ so the next worker pass
    # can retry it. The gate does not move it — the committer owns that transition.
    if disposition == "retry-later":
        try:
            queue.set_state(intent_id, "submitted")
        except Exception as inner:
            log.error("could not re-queue retry-later intent %s: %s", intent_id, inner)

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
    embedding_index=None,
    sink=None,
) -> None:
    """Drain the queue once (once=True) or poll indefinitely (once=False).

    Accepts an optional ``embedding_index`` so the production CLI path can wire
    in ``EmbeddingIndex()`` and enable ``_dedup_recheck`` (the merge path).

    Accepts an optional ``sink`` callable for production observability (P6).
    When provided, the drain loop calls ``sink(record)`` after each intent with
    a dict containing stable structured keys::

        {
            "intent_id":   str,   # the claimed intent's ID
            "disposition": str,   # committed / merged / dead_lettered / retry-later / ...
            "reason":      str,   # detail / error text (from DrainResult.detail/errors)
        }

    ``sink`` is **default-off**: when not provided the loop is byte-identical to
    the pre-P6 path (zero behavior change). The sink is called AFTER the existing
    ``log.info`` line; it must not swallow or mask any exception.

    At startup, calls ``gate.recover()`` to revert any partial writes from a
    crashed prior worker and reclaim their intents (crash recovery).

    Each iteration is independent. A poison intent dead-letters (either via the
    gate's own CAS pipeline or via the backstop in drain_once), and the loop
    CONTINUES — it does not abort.

    The backstop except here is a final safety net for unexpected drain_once
    failures (e.g. a completely malformed record that drain_once itself cannot
    handle). Normal bad intents dead-letter via the gate, not via this catch.
    """
    q = queue or IntentQueue()
    if gate is None:
        gate = CommitGate(queue=q, embedding_index=embedding_index)
    g = gate

    # Crash recovery: revert partial writes from prior crashed worker and
    # reclaim their intents back to submitted/ before we start draining.
    try:
        g.recover()
    except Exception as exc:
        log.error("gate.recover() failed at startup: %s", exc)

    def _emit(result) -> None:
        # Emit stable structured keys only — no payload/body/credentials.
        # reason: prefer detail (the human-readable summary); fall back to
        # the first error string when detail is empty (dead-letter path).
        if sink is not None:
            reason = result.detail or (result.errors[0] if result.errors else "")
            sink({
                "intent_id": result.intent_id,
                "disposition": result.disposition,
                "reason": reason,
            })

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
            _emit(result)
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
                    _emit(result)
                else:
                    time.sleep(poll_interval)
        except KeyboardInterrupt:
            log.info("commit-worker interrupted; exiting.")
