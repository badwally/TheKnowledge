"""CommitGate — Librarian Phase 1 (T1.4).

The CommitGate owns the single serial commit (design §5, decision 1). This is
the highest-risk surface, so the protocol is concrete, not "re-validate against
HEAD":

- **Commit mutex.** All commits serialize on ``locking.file_lock("librarian-commit")``
  — the §4 migration delta (the commit mutex replaces the global ``wiki-author``
  barrier for the commit step). Authoring runs concurrently elsewhere; only this
  step is serial.
- **MVCC compare-and-swap (§5.1).** For each written page, compare that page's
  real git blob OID at the authored snapshot (``AuthoredIntent.base_oids[path]``,
  captured via ``git rev-parse HEAD:<path>``) against that path's current HEAD
  blob. Three cases, classified PER PATH: (1) no overlap → commit; (2) same page,
  mergeable → rebase onto HEAD, re-CAS the whole write set, bounded by
  «commit.max_rebase_attempts» before dead-lettering ``contention`` (C4); (3) same
  page, contradictory → dead-letter. The Phase-1 merge scaffold FAILS SAFE: any
  real overlap it cannot trivially reconcile dead-letters ``needs-merge`` rather
  than blind-overwriting a concurrent change (F1; structured merge is Phase 3).
- **Idempotency keyed off committed state (§5.4, C2).** The ``intent_id`` is
  written into the commit as an ``Intent-Id:`` trailer. ``commit()`` resolves a
  redelivery by reading the trailer VALUE exactly from committed history (not an
  unanchored substring ``--grep``, which is prefix-collidable), which cannot lag
  the commit — the queue status file can lag by one crash.
- **Fencing (§3.2, C3).** Reject any commit whose fencing token is not the highest
  issued for that ``intent_id`` — a resurrected slow worker cannot overwrite the
  reclaimer's commit. The highest-issued token is durable per-intent state that
  survives a crash that loses the queue record.
- **Crash recovery (§5.5, C1).** ``recover()`` reverts ONLY each in-flight
  intent's durably-recorded declared write set (tracked → ``git checkout --``,
  untracked → ``rm`` the specific file), then reclaims expired claims. It never
  ``git reset --hard`` / ``git clean -fd`` the shared tree — that would destroy
  other sessions' and the watcher's uncommitted/untracked work. Because markdown
  is canonical and indexes are derived, no index state needs recovery.

It generalizes ``discharge_orphans._git_commit_synthesis_drafts`` (always
``git add -- <explicit>``, never ``-A``) into the one committer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import logging
import os
from pathlib import Path
import subprocess

from gateway import locking, paths
from gateway.core import OperationResult, write_atomic
from gateway.intent_queue import Intent, IntentQueue

log = logging.getLogger(__name__)


# «commit.max_rebase_attempts» (ledger §1.1).
DEFAULT_MAX_REBASE_ATTEMPTS = 8


@dataclass(frozen=True)
class AuthoredIntent:
    """A claimed intent that has been authored to canonical form on a worker.

    ``base_oid`` is the legacy single-snapshot field. The CAS (§5.1) compares
    per-path blob OIDs, so the authoritative provenance is ``base_oids``:
    ``{relative_path: blob_oid_or_None}`` captured at authoring time via
    ``git rev-parse HEAD:<path>`` (None if the path was new at that snapshot).
    When ``base_oids`` lacks an entry for a written path, the gate falls back to
    ``base_oid`` for that path (backward compatibility).
    """

    intent: Intent
    writes: dict[str, str]   # {relative_path: file_content}
    base_oid: str            # legacy single-snapshot fallback
    base_oids: dict[str, str | None] = field(default_factory=dict)
    decision_basis: dict = field(default_factory=dict)

    def base_for(self, rel: str) -> str | None:
        """The per-path base blob OID for ``rel`` (or the legacy fallback)."""
        if rel in self.base_oids:
            return self.base_oids[rel]
        return self.base_oid


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
        """Return the commit SHA that applied ``intent_id``, or None (C2).

        BLOCKER-3: resolve the ``Intent-Id`` trailer VALUE exactly, never a
        substring grep. ``--grep=Intent-Id: <id>`` is unanchored, so a redelivered
        intent whose id is a hex prefix of an already-committed one (e.g.
        ``abcd1234`` vs ``abcd1234ef``) would falsely resolve as already-committed.
        We emit ``%H<NUL>%(trailers:key=Intent-Id,valueonly)`` and compare the
        full trailer value to ``intent_id`` in Python.
        """
        r = self._git(
            "log", "--all",
            "--format=%H%x00%(trailers:key=Intent-Id,valueonly,separator=%x00)",
            check=False,
        )
        if r.returncode != 0:
            return None
        for line in r.stdout.splitlines():
            if not line.strip():
                continue
            sha, _, rest = line.partition("\x00")
            # rest may hold one or more trailer values (NUL-separated).
            values = [v.strip() for v in rest.split("\x00") if v.strip()]
            if intent_id in values:
                return sha
        return None

    # --- CAS classification --------------------------------------------

    def _blob_exists(self, oid: str) -> bool:
        """True if ``oid`` names a real object in this repo's history."""
        if not oid or set(oid) == {"0"}:
            return False
        return self._git("cat-file", "-e", oid, check=False).returncode == 0

    def _classify(self, authored: AuthoredIntent) -> str:
        """Return one of: 'commit', 'rebase', 'contradictory' (§5.1).

        BLOCKER-2 / CORRECTNESS-5: classify EACH written path against THAT path's
        own fresh HEAD blob OID and THAT path's authored base blob OID — not a
        single shared base. The literal string ``"HEAD"`` is never a valid blob
        OID; a path whose base is the unresolved ``"HEAD"`` sentinel and whose
        HEAD blob differs is treated as an overlap (it can never CAS-match).

        Per path:
        - No HEAD blob (path absent at HEAD) → no overlap for this path.
        - HEAD blob == this path's authored base → unchanged → no overlap.
        - Overlap where the authored base is a real ancestor blob → concurrent
          edit on shared lineage → mergeable (rebase, case 2).
        - Overlap where the authored base never existed (phantom: authored thought
          the path was absent, but HEAD has it) → contradictory (case 3).
        """
        verdict = "commit"
        for rel, _content in authored.writes.items():
            head_oid = self._head_blob_oid(rel)
            base = authored.base_for(rel)
            if head_oid is None:
                continue  # new path at HEAD — no overlap
            if base is not None and head_oid == base:
                continue  # unchanged since the authoring snapshot — no overlap
            # Overlap: HEAD blob differs from this path's authored base.
            if base is not None and self._blob_exists(base):
                verdict = "rebase"
            else:
                # base is None / the "HEAD" sentinel / a phantom that never
                # existed, yet HEAD has the path with different content → the
                # authoring snapshot's view of this path is contradicted.
                return "contradictory"
        return verdict

    def _merge_rebase(self, authored: AuthoredIntent) -> dict[str, str]:
        """Re-apply the authored payload onto current HEAD (§5.1 case 2).

        SILENT-CORRUPTION-4: the Phase-1 scaffold MUST fail safe. The structured
        three-way claim merge is Phase 3; until then the only mergeable case we
        accept without dropping a concurrent change is one where HEAD's current
        content for the path is byte-identical to what the authoring snapshot saw
        — i.e. nothing concurrent actually changed this page's body, so the
        authored content can be applied. Any real divergence (HEAD now differs
        from the authored base) is a potential lost update and is raised as a
        RebaseConflict, which the commit loop dead-letters as ``needs-merge``
        rather than blind-overwriting (the old ``head_content in content``
        substring test silently dropped the concurrent edit, F1).
        """
        merged: dict[str, str] = {}
        for rel, content in authored.writes.items():
            head_oid = self._head_blob_oid(rel)
            base = authored.base_for(rel)
            if head_oid is None:
                # Path absent at HEAD — no concurrent body to lose.
                merged[rel] = content
                continue
            if base is not None and head_oid == base:
                # HEAD unchanged vs the authoring snapshot — safe to apply.
                merged[rel] = content
                continue
            # HEAD's blob differs from the authored base. A trivial scaffold
            # cannot reconcile two divergent bodies without risking a lost
            # update — fail safe to dead-letter.
            raise self.RebaseConflict(rel)
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
                    except self.RebaseConflict:
                        # SILENT-CORRUPTION-4 / F1: a real overlap the Phase-1
                        # scaffold cannot reconcile. Fail safe — dead-letter as
                        # needs-merge rather than blind-overwrite a concurrent
                        # change. Spinning attempts cannot help (HEAD is stable
                        # within the held commit mutex), so dead-letter now.
                        self._queue.set_state(
                            intent_id, "dead_lettered",
                            result={"reason": "needs-merge"},
                        )
                        return OperationResult(
                            success=False,
                            intent_id=intent_id,
                            disposition="dead_lettered",
                            errors=["concurrent overlapping change requires merge"],
                            summary=f"{intent_id}: dead-lettered (needs-merge)",
                        )
                    # CORRECTNESS-5: re-CAS the WHOLE merged write set against
                    # each path's fresh HEAD blob. After _merge_rebase, every
                    # path is HEAD-unchanged or absent, so the rebased payload
                    # CAS-matches and we proceed.
                    rebased = AuthoredIntent(
                        intent=authored.intent,
                        writes=writes,
                        base_oid=authored.base_oid,
                        base_oids={
                            rel: self._head_blob_oid(rel) for rel in writes
                        },
                    )
                    if self._classify(rebased) == "commit":
                        break
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

            # BLOCKER-1: durably record the declared write set BEFORE touching
            # the tree, so crash recovery can scope its revert to exactly these
            # paths (tracked → `git checkout --`; untracked → `rm`) instead of a
            # tree-wide `reset --hard` / `clean -fd` that would destroy unrelated
            # sessions' and the watcher's uncommitted work.
            try:
                self._queue.set_declared_writes(intent_id, list(writes))
            except KeyError:
                pass  # queue record may legitimately be absent (idempotent path)

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

    def _is_tracked(self, rel: str) -> bool:
        """True if ``rel`` is tracked at HEAD (has a blob), else untracked."""
        return self._head_blob_oid(rel) is not None

    def recover(self, *, now: float | None = None) -> list[str]:
        """Revert ONLY in-flight intents' partial writes, then reclaim (C1).

        BLOCKER-1: never ``git reset --hard`` / ``git clean -fd`` the shared
        tree — that destroys other sessions' and the watcher's uncommitted and
        untracked work. Instead, scope the revert to the declared write set of
        each in-flight (claimed/authored, uncommitted) intent:

        - a path tracked at HEAD that the intent modified → ``git checkout --``
          (restore the committed blob);
        - a path the intent newly created (untracked at HEAD) → ``rm`` only that
          specific file.

        Unrelated tracked modifications and untracked files are left untouched.
        """
        root_resolved = self._root.resolve()
        for intent_id in self._queue.in_flight_intents():
            for rel in self._queue.declared_writes(intent_id):
                # Defense-in-depth (recovery DELETES files): declared paths are
                # self-declared by the producer. Even though set_declared_writes
                # validates at write time, re-verify containment at the use site
                # before any destructive op — never checkout/unlink a path that
                # resolves outside the root.
                abs_path = (self._root / rel).resolve()
                if not (
                    abs_path == root_resolved
                    or str(abs_path).startswith(str(root_resolved) + os.sep)
                ):
                    log.warning("declared write escapes root, skipping: %s", rel)
                    continue
                if self._is_tracked(rel):
                    # Restore the committed version of a path the intent dirtied.
                    self._git("checkout", "--", rel, check=False)
                else:
                    # Remove only the specific file the intent newly created.
                    try:
                        if abs_path.is_file():
                            abs_path.unlink()
                    except OSError:
                        pass
        return self._queue.reclaim_expired(now=now)
