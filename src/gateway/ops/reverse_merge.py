"""Producer ops for the two recovery reversal kinds — ``reverse-merge`` (G8) and
``restore-depath``.

These are the operator-facing counterparts to the gate's ``_apply_reverse_merge``
/ ``_apply_restore_depath`` apply branches, which were previously reachable only
via a hand-built intent (the I2 gap: recovery affordance gate-ready but not
operator-reachable).

Mirror ``remediate.py`` / ``revert_resolution.py``: validate → build an ``Intent``
carrying a ``reversal_type`` payload → ``IntentQueue.submit`` → return an
``OperationResult`` describing the queued intent. The CommitGate apply-path does
the actual restore on drain (``wiki commit-worker``).

Containment (defense in depth):
- The gate's ``_commit_reversal_writes`` confines every reversal write to
  ``wiki/`` + ``.knowledge/policies/`` and rejects ``..``/absolute/escaping rels.
- This producer ALSO rejects traversal/absolute rels up front (fail fast — never
  enqueue a doomed intent), per the backlog's named-negative-control requirement.
- ``restore-depath`` content is pulled from the recorded de-path provenance node,
  never caller-supplied, so a caller cannot inject arbitrary page content here.
"""

from __future__ import annotations

from pathlib import Path

from gateway import provenance
from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id


def _is_unsafe_rel(rel: str) -> bool:
    """True if ``rel`` is empty, absolute, contains a ``..`` traversal part, or
    carries a backslash (a Windows separator POSIX ``Path`` would treat as a
    literal filename — reject it rather than let a `wiki\\..\\.git` form slip the
    POSIX-only ``..`` check)."""
    if not rel or "\\" in rel:
        return True
    p = Path(rel)
    return p.is_absolute() or ".." in p.parts


def reverse_merge(
    tombstone_rel: str,
    identity: dict | None = None,
    *,
    queue: IntentQueue | None = None,
    policy_version: str = "reverse-merge-recovery-v1",
) -> OperationResult:
    """Submit a reverse-merge intent for ``tombstone_rel`` (G8 recovery).

    The gate rebuilds the reattachment plan from the tombstone + provenance and
    restores the canonical; the operator supplies only the tombstone path."""
    if _is_unsafe_rel(tombstone_rel):
        return OperationResult(
            success=False,
            errors=[
                f"unsafe tombstone_rel {tombstone_rel!r}: absolute/traversal rejected"
            ],
        )
    payload = {
        "reversal_type": "reverse-merge",
        "tombstone_rel": tombstone_rel,
        "policy_version": policy_version,
    }
    ident = identity or {"agent": "cli", "operation": "reverse-merge"}
    iid = compute_intent_id(payload, ident, semantics="reverse-merge")
    intent = Intent(intent_id=iid, payload=payload, identity=ident)
    (queue or IntentQueue()).submit(intent)
    return OperationResult(
        success=True,
        intent_id=iid,
        summary=f"queued reverse-merge for {tombstone_rel}",
        data={"intent_id": iid, "tombstone_rel": tombstone_rel},
    )


def _recorded_depath_content(target_rel: str, *, root: Path | None = None) -> str | None:
    """Most-recently recorded ``depathed_content`` for ``target_rel``, or None."""
    for node in reversed(provenance.read_nodes(root=root)):
        basis = node.get("decision_basis", {}) or {}
        if basis.get("reversal_type") == "depath" and basis.get("target") == target_rel:
            content = basis.get("depathed_content")
            if content:
                return content
    return None


def restore_depath(
    target_rel: str,
    identity: dict | None = None,
    *,
    queue: IntentQueue | None = None,
    root: Path | None = None,
    policy_version: str = "restore-depath-recovery-v1",
) -> OperationResult:
    """Submit a restore-depath intent recreating a previously de-pathed page.

    Content is looked up from the de-path provenance node — never caller-supplied.
    Fails (enqueues nothing) when no recorded content exists for ``target_rel``."""
    if _is_unsafe_rel(target_rel):
        return OperationResult(
            success=False,
            errors=[f"unsafe target_rel {target_rel!r}: absolute/traversal rejected"],
        )
    content = _recorded_depath_content(target_rel, root=root)
    if not content:
        return OperationResult(
            success=False,
            errors=[
                f"no recorded de-path content for {target_rel!r}; cannot restore"
            ],
        )
    payload = {
        "reversal_type": "restore-depath",
        "target_rel": target_rel,
        "content": content,
        "policy_version": policy_version,
    }
    ident = identity or {"agent": "cli", "operation": "restore-depath"}
    iid = compute_intent_id(payload, ident, semantics="restore-depath")
    intent = Intent(intent_id=iid, payload=payload, identity=ident)
    (queue or IntentQueue()).submit(intent)
    return OperationResult(
        success=True,
        intent_id=iid,
        summary=f"queued restore-depath for {target_rel}",
        data={"intent_id": iid, "target_rel": target_rel},
    )
