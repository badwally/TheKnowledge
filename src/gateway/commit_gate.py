"""CommitGate — Librarian Phase 1 (T1.4).

The CommitGate owns the single serial commit (design §5, decision 1). This is
the highest-risk surface, so the protocol is concrete, not "re-validate against
HEAD":

- **Commit mutex.** All commits serialize on ``locking.file_lock("librarian-commit")``
  — the §4 migration delta (the commit mutex replaces the global ``wiki-author``
  barrier for the commit step). Authoring runs concurrently elsewhere; only this
  step is serial.
- **MVCC compare-and-swap (§5.1).** For each written page, compare the page's git
  blob OID at the authored snapshot (``AuthoredIntent.base_oid``) against current
  HEAD. Three cases: (1) no overlap → commit; (2) same page, mergeable → rebase
  onto HEAD, bounded by «commit.max_rebase_attempts» before dead-lettering
  ``contention`` (C4); (3) same page, contradictory → dead-letter.
- **Idempotency keyed off committed state (§5.4, C2).** The ``intent_id`` is
  written into the commit (a ``Intent-Id:`` trailer + an ``applied_intents``
  record committed in the same commit). ``commit()`` resolves a redelivery by
  scanning committed history (``git log --grep``), which cannot lag the commit —
  the queue status file can lag by one crash.
- **Fencing (§3.2, C3).** Reject any commit whose fencing token is not the highest
  issued for that ``intent_id`` — a resurrected slow worker cannot overwrite the
  reclaimer's commit.
- **Crash recovery (§5.5, C1).** ``recover()`` = ``git reset --hard HEAD`` +
  ``git clean -fd`` then reclaim expired claims. Because markdown is canonical and
  indexes are derived, no index state needs recovery.

It generalizes ``discharge_orphans._git_commit_synthesis_drafts`` (always
``git add -- <explicit>``, never ``-A``) into the one committer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import subprocess

from gateway import locking, paths
from gateway.core import OperationResult, write_atomic
from gateway.intent_queue import Intent, IntentQueue


# «commit.max_rebase_attempts» (ledger §1.1).
DEFAULT_MAX_REBASE_ATTEMPTS = 8


@dataclass(frozen=True)
class AuthoredIntent:
    """A claimed intent that has been authored to canonical form on a worker."""

    intent: Intent
    writes: dict[str, str]   # {relative_path: file_content}
    base_oid: str            # the snapshot the authoring ran against
    decision_basis: dict = field(default_factory=dict)


class CommitGate:
    """The single serial commit gate."""

    class RebaseConflict(Exception):
        """Raised by the rebase/merge step when a mergeable case cannot reconcile."""

    def __init__(
        self,
        root: Path | None = None,
        queue: IntentQueue | None = None,
        provenance=None,
        max_rebase_attempts: int = DEFAULT_MAX_REBASE_ATTEMPTS,
    ):
        self._root = root or paths.knowledge_root()
        self._queue = queue or IntentQueue()
        self._provenance = provenance
        self._max_rebase = max_rebase_attempts

    # --- git helpers ----------------------------------------------------

    def _git(self, *args, check=True):
        return subprocess.run(
            ["git", *args],
            cwd=self._root,
            capture_output=True,
            text=True,
            check=check,
        )

    def _head_blob_oid(self, rel_path: str) -> str | None:
        """Blob OID of ``rel_path`` at HEAD, or None if absent."""
        r = self._git("rev-parse", f"HEAD:{rel_path}", check=False)
        if r.returncode != 0:
            return None
        return r.stdout.strip()

    def _already_committed(self, intent_id: str) -> str | None:
        """Return the commit SHA that applied ``intent_id``, or None (C2)."""
        r = self._git(
            "log", "--all", "--format=%H", f"--grep=Intent-Id: {intent_id}",
            check=False,
        )
        if r.returncode != 0:
            return None
        lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
        return lines[0] if lines else None

    # --- CAS classification --------------------------------------------

    def _blob_exists(self, oid: str) -> bool:
        """True if ``oid`` names a real object in this repo's history."""
        if not oid or set(oid) == {"0"}:
            return False
        return self._git("cat-file", "-e", oid, check=False).returncode == 0

    def _classify(self, authored: AuthoredIntent) -> str:
        """Return one of: 'commit', 'rebase', 'contradictory' (§5.1).

        - No HEAD blob for the path, or HEAD blob == authored base → no overlap.
        - Overlap where the authoring snapshot's base is a real ancestor blob →
          a concurrent edit on a shared lineage → mergeable (rebase, case 2).
        - Overlap where the base never existed (phantom: authored thought the
          path was absent, but HEAD has it) → contradictory (case 3).
        """
        verdict = "commit"
        for rel, _content in authored.writes.items():
            head_oid = self._head_blob_oid(rel)
            if head_oid is None:
                continue  # new path at HEAD — no overlap
            if head_oid == authored.base_oid:
                continue  # unchanged since the authoring snapshot — no overlap
            # Overlap: HEAD moved out from under the authoring snapshot.
            if self._blob_exists(authored.base_oid):
                verdict = "rebase"
            else:
                return "contradictory"
        return verdict

    def _merge_rebase(self, authored: AuthoredIntent) -> dict[str, str]:
        """Re-apply the authored payload onto current HEAD (§5.1 case 2).

        Phase 1 ships the bounded-attempt scaffold; the structured-claim merge
        is Phase 3. Here a mergeable case re-reads HEAD and unions the authored
        addition. Raises RebaseConflict if it cannot reconcile.
        """
        merged: dict[str, str] = {}
        for rel, content in authored.writes.items():
            head_content = self._git("show", f"HEAD:{rel}", check=False).stdout
            if head_content and head_content not in content:
                raise self.RebaseConflict(rel)
            merged[rel] = content
        return merged

    # --- the gate -------------------------------------------------------

    def commit(self, authored: AuthoredIntent, fencing_token: int) -> OperationResult:
        intent_id = authored.intent.intent_id
        with locking.file_lock("librarian-commit"):
            # (C2) Idempotency from committed state — scan history first.
            prior = self._already_committed(intent_id)
            if prior is not None:
                result = self._queue.get_result(intent_id)
                return OperationResult(
                    success=True,
                    no_op=True,
                    intent_id=intent_id,
                    disposition="committed",
                    canonical_path=(
                        Path(result["canonical_path"])
                        if result.get("canonical_path") else None
                    ),
                    summary=f"{intent_id}: already committed at {prior[:8]}",
                )

            # (C3) Fencing — reject a stale (non-highest) token.
            current = self._queue.fencing_token(intent_id)
            if current is not None and fencing_token < current:
                self._queue.set_result(
                    intent_id, {"reason": "stale-fencing-token"}
                )
                return OperationResult(
                    success=False,
                    intent_id=intent_id,
                    disposition="rejected",
                    errors=["stale fencing token"],
                    summary=f"{intent_id}: rejected (stale fencing token "
                            f"{fencing_token} < {current})",
                )

            # (§5.1) MVCC compare-and-swap.
            verdict = self._classify(authored)
            writes = authored.writes
            rebase_branch = "no-overlap"

            if verdict == "contradictory":
                self._queue.set_state(
                    intent_id, "dead_lettered", result={"reason": "contradictory-edit"}
                )
                return OperationResult(
                    success=False,
                    intent_id=intent_id,
                    disposition="dead_lettered",
                    errors=["contradictory edit at HEAD"],
                    summary=f"{intent_id}: dead-lettered (contradictory edit)",
                )

            if verdict == "rebase":
                rebase_branch = "rebase"
                attempts = 0
                while True:
                    attempts += 1
                    try:
                        writes = self._merge_rebase(authored)
                        # Re-classify after rebase; if it now commits, proceed.
                        if self._classify(
                            AuthoredIntent(
                                intent=authored.intent, writes=writes,
                                base_oid=self._head_blob_oid(
                                    next(iter(writes))) or authored.base_oid,
                            )
                        ) != "contradictory":
                            break
                    except self.RebaseConflict:
                        pass
                    if attempts >= self._max_rebase:
                        self._queue.set_state(
                            intent_id, "dead_lettered",
                            result={"reason": "contention"},
                        )
                        return OperationResult(
                            success=False,
                            intent_id=intent_id,
                            disposition="dead_lettered",
                            errors=["max rebase attempts exceeded"],
                            summary=f"{intent_id}: dead-lettered (contention)",
                        )

            # Apply writes (per-file atomic; the git commit is the atomic boundary).
            touched: list[Path] = []
            for rel, content in writes.items():
                abs_path = self._root / rel
                write_atomic(abs_path, content)
                touched.append(abs_path)

            # Idempotency is keyed off committed state via the `Intent-Id:` commit
            # trailer (C2, §5.4), resolved by `git log --grep` on redelivery. The
            # trailer cannot lag the commit (the queue status file can lag by one
            # crash). An `applied_intents` record is intentionally NOT written to
            # the gitignored `.knowledge/` tree — the trailer is the source of truth.
            self._git("add", "--", *[str(p) for p in touched])
            canonical_rel = next(iter(writes))
            msg = (
                f"feat(librarian-commit): {canonical_rel}\n\n"
                f"Intent-Id: {intent_id}\n"
            )
            self._git("commit", "-qm", msg)
            sha = self._git("rev-parse", "HEAD").stdout.strip()

            canonical_path = self._root / canonical_rel
            self._queue.set_state(
                intent_id, "committed",
                result={"canonical_path": str(canonical_path), "commit": sha},
            )

            # (decision 3) Operational-provenance node — recorded inside the gate.
            if self._provenance is not None:
                basis = {
                    "policy_version": authored.decision_basis.get("policy_version"),
                    "dedup_score": authored.decision_basis.get("dedup_score"),
                    "dedup_candidates": authored.decision_basis.get("dedup_candidates", []),
                    "merge_rebase_branch": rebase_branch,
                    "commit": sha,
                    "canonical_path": str(canonical_path),
                }
                self._provenance.record(intent_id, basis)

            return OperationResult(
                success=True,
                intent_id=intent_id,
                disposition="committed",
                canonical_path=canonical_path,
                paths_touched=touched,
                summary=f"{intent_id}: committed {canonical_rel} at {sha[:8]}",
            )

    # --- recovery -------------------------------------------------------

    def recover(self, *, now: float | None = None) -> list[str]:
        """Reset the working tree to HEAD and reclaim expired claims (C1)."""
        self._git("reset", "--hard", "HEAD")
        # Exclude the durable internal state (queue, provenance, applied-intents
        # log) from the clean — it is gitignored canonical operational state,
        # not torn working-tree content. Without the exclude, `git clean -fd`
        # would wipe the queue we are about to reclaim from.
        self._git("clean", "-fd", "-e", ".knowledge")
        return self._queue.reclaim_expired(now=now)
