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
import re
import subprocess

from gateway import locking, paths
from gateway.core import OperationResult, write_atomic
from gateway.embedding_index import REBUILD_LOCK
from gateway.intent_queue import Intent, IntentQueue

log = logging.getLogger(__name__)


# «commit.max_rebase_attempts» (ledger §1.1).
DEFAULT_MAX_REBASE_ATTEMPTS = 8

# Bounded acquisition for the serial commit barrier (A3): the committer must
# never block indefinitely. On timeout the intent is left for a later pass
# (re-queue / retry), not hung.
COMMIT_LOCK_ACQUIRE_TIMEOUT = 30.0  # «commit.lock_acquire_timeout»
COMMIT_LOCK_RETRY_AFTER = 5  # seconds — poll-interval hint returned on barrier contention


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
        embedding_index=None,
    ):
        self._root = root or paths.knowledge_root()
        self._queue = queue or IntentQueue()
        self._provenance = provenance
        self._max_rebase = max_rebase_attempts
        # Librarian Phase 2 (§13): the committer upserts a committed page's
        # embedding rows current-as-of-HEAD, so the next intent in the same
        # serialization window can NN-search the entity namespace and see it
        # (incremental upsert on commit — commit-time dedup reads this index, so
        # a lazy per-query rebuild would make a write wrong). None → no-op,
        # preserving Phase-1 back-compat.
        self._embedding_index = embedding_index

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

    def _blob_content(self, oid: str | None) -> str | None:
        """Content of a blob OID, or None if it cannot be read."""
        if not oid or set(oid) == {"0"} or oid == "HEAD":
            return None
        r = self._git("cat-file", "-p", oid, check=False)
        if r.returncode != 0:
            return None
        return r.stdout

    @staticmethod
    def _claim_union(base: str, head: str, authored: str) -> str | None:
        """Three-way union of appended ``## Claims`` bullet lines (§5.1 Phase-3).

        Returns the merged body when BOTH the HEAD change and the authored change
        relative to ``base`` are pure ADDITIONS of distinct claim bullets (no line
        removed, no existing bullet rewritten). Otherwise returns None → the caller
        dead-letters as ``needs-merge`` (a genuine conflict — e.g. the same claim
        rewritten to a contradictory object — is NOT blind-merged; Task 7 handles
        contradiction)."""
        base_lines = base.splitlines()
        head_lines = head.splitlines()
        auth_lines = authored.splitlines()
        base_set = set(base_lines)

        def _added_bullets(new_lines):
            added = [ln for ln in new_lines if ln not in base_set]
            # every change must be an ADDED bullet line (not a removal or a
            # non-bullet body rewrite)
            if any(ln not in set(new_lines) for ln in base_lines):
                return None  # a base line was removed → not a pure addition
            for ln in added:
                if ln.strip() and not ln.strip().startswith("- "):
                    return None  # a non-bullet line changed → not claim-only
            return added

        head_add = _added_bullets(head_lines)
        auth_add = _added_bullets(auth_lines)
        if head_add is None or auth_add is None:
            return None

        # Start from HEAD (it already includes the concurrent addition), then
        # append the authored bullets HEAD doesn't yet have.
        head_set = set(head_lines)
        new_bullets = [ln for ln in auth_add if ln not in head_set]
        if not new_bullets:
            return head if head.endswith("\n") else head + "\n"
        merged_lines = list(head_lines)
        # ensure there is a Claims section to append under
        if not any(ln.strip().lower().startswith("## claims") for ln in merged_lines):
            merged_lines += ["", "## Claims"]
        merged_lines += new_bullets
        out = "\n".join(merged_lines)
        return out + "\n" if not out.endswith("\n") else out

    def _merge_rebase(self, authored: AuthoredIntent) -> dict[str, str]:
        """Re-apply the authored payload onto current HEAD (§5.1 case 2).

        Phase-1 failed safe (any divergence → dead-letter). Phase-3 adds a
        structured claim-union: when both the concurrent HEAD change and the
        authored change relative to the authored base are pure additions of
        distinct ``## Claims`` bullets, union them onto HEAD (C5 write-skew — both
        claims survive). Any other divergence (a base line removed, a non-bullet
        body rewrite, or the same claim rewritten to a contradictory object) is a
        potential lost update / contradiction and is raised as RebaseConflict,
        which the commit loop dead-letters as ``needs-merge`` (F1).
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
            # HEAD's blob differs from the authored base. Attempt a structured
            # claim-union; fail safe to dead-letter if it is not a clean add/add.
            head_content = self._blob_content(head_oid)
            base_content = self._blob_content(base)
            if head_content is None or base_content is None:
                raise self.RebaseConflict(rel)
            unioned = self._claim_union(base_content, head_content, content)
            if unioned is None:
                raise self.RebaseConflict(rel)
            merged[rel] = unioned
        return merged

    # --- the gate -------------------------------------------------------

    def commit(self, authored: AuthoredIntent, fencing_token: int) -> OperationResult:
        intent_id = authored.intent.intent_id
        try:
            with locking.file_lock("librarian-commit", timeout=COMMIT_LOCK_ACQUIRE_TIMEOUT):
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

                # (Phase 5 T1, G1/G3/G8) Reversal-type dispatch. A reversal intent
                # un-canonicalizes a prior action — it carries no normal write set and
                # must NOT flow through the deposit/dedup/contradiction pipeline. Route
                # it to a bounded apply helper that computes its own writes/deletes,
                # commits provenanced, and returns. Reversibility invariant: every
                # reversal records a provenance act and never destroys a cited page.
                reversal_type = (authored.intent.payload or {}).get("reversal_type")
                if reversal_type:
                    return self._apply_reversal(authored, intent_id, fencing_token)

                # (Phase 5 T6, G7) Privileged policy-edit dispatch. A policy-edit
                # intent carries the new policy in its payload (not in `writes`) and
                # writes to the gitignored .knowledge/policies/ tree. It bypasses the
                # deposit/dedup/contradiction pipeline and routes to a dedicated apply
                # helper that gates on eval-retrieval recall + merge-map golden
                # precision BEFORE writing the policy file.
                payload_op = (authored.intent.payload or {}).get("op")
                if payload_op == "policy-edit":
                    return self._apply_policy_edit(authored, intent_id)

                # (§6 I1) Deterministic LLM-free dedup re-check, inside the held
                # commit mutex. A `merge` verdict re-targets the deposit's claims onto
                # the canonical page (no duplicate-referent slug minted). The verdict
                # basis is recorded into provenance for replay.
                dedup_disposition = "committed"
                verdict_dedup = self._dedup_recheck(authored)
                if verdict_dedup.decision == "merge" and verdict_dedup.target_slug:
                    try:
                        authored = self._retarget_to_canonical(
                            authored, verdict_dedup.target_slug
                        )
                    except self.RebaseConflict:
                        # A merge whose body cannot be cleanly unioned (section heading
                        # collision with differing content) must NOT silently drop the
                        # deposit's body — dead-letter for manual merge (review B1).
                        self._queue.set_state(
                            intent_id, "dead_lettered",
                            result={"reason": "needs-manual-merge"},
                        )
                        return OperationResult(
                            success=False,
                            intent_id=intent_id,
                            disposition="dead_lettered",
                            errors=["merge body requires manual reconciliation"],
                            summary=f"{intent_id}: dead-lettered (needs-manual-merge)",
                        )
                    dedup_disposition = "merged"
                authored.decision_basis.setdefault("dedup_verdict", {
                    "decision": verdict_dedup.decision, "rule": verdict_dedup.rule,
                    "target": verdict_dedup.target_slug, "basis": verdict_dedup.basis,
                })

                # (decision 6, Task 7) Claim-level contradiction auto-resolve. A
                # deposit whose claim contradicts a committed claim on the same
                # referent is resolved by policy (server trust desc, then recency),
                # records a reversible act, and materializes a CiTO `disputes` edge —
                # the loser stays retrievable (never deleted).
                resolved_intent = self._detect_and_resolve_claim_contradiction(authored)
                if resolved_intent is not None:
                    authored = resolved_intent
                    authored.decision_basis.setdefault("contradiction_resolved", True)

                # (decision 6) Multi-label domain resolution + quarantine-on-empty.
                # A deposit that NAMES domains but resolves to none live is
                # quarantined — never committed untagged. A deposit with no domain
                # hint at all is left untouched (back-compat).
                ident_d = authored.intent.identity or {}
                named = ident_d.get("domains") or (
                    [ident_d["domain"]] if ident_d.get("domain") else []
                )
                if named:
                    from gateway import domain_resolve

                    resolved = domain_resolve.resolve_domains(
                        ident_d, domain_resolve.live_domains()
                    )
                    if not resolved:
                        self._queue.set_state(
                            intent_id, "quarantined",
                            result={"reason": "no-resolvable-domain"},
                        )
                        return OperationResult(
                            success=False,
                            intent_id=intent_id,
                            disposition="quarantined",
                            errors=["no resolvable live domain"],
                            summary=f"{intent_id}: quarantined (no resolvable domain)",
                        )
                    authored.decision_basis.setdefault("resolved_domains", resolved)

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
                # A merge-reattachment whose claims are all already present produces no
                # staged diff. That is a successful idempotent attach, not an error —
                # `git commit` would abort on an empty tree. Use --allow-empty so the
                # Intent-Id trailer is still recorded (idempotency/provenance) and the
                # disposition stays `merged`.
                empty = self._git(
                    "diff", "--cached", "--quiet", check=False
                ).returncode == 0
                msg = (
                    f"feat(librarian-commit): {canonical_rel}\n\n"
                    f"Intent-Id: {intent_id}\n"
                )
                commit_args = ["commit", "-qm", msg]
                if empty:
                    commit_args.insert(1, "--allow-empty")
                self._git(*commit_args)
                sha = self._git("rev-parse", "HEAD").stdout.strip()

                canonical_path = self._root / canonical_rel
                self._queue.set_state(
                    intent_id, "committed",
                    result={"canonical_path": str(canonical_path), "commit": sha,
                            "dedup": dedup_disposition},
                )

                # (§13, A6) Incremental upsert on commit — AFTER the git commit (the
                # atomic boundary), so the embedding rows are current-as-of-HEAD for
                # the next intent's dedup. Quiesce on the embedding-rebuild lock so a
                # concurrent shadow-swap never interleaves with this write. Derived
                # state: a failure here self-heals on the next upsert/rebuild and must
                # not fail an already-committed intent.
                if self._embedding_index is not None:
                    self._upsert_embeddings(writes)

                # (decision 3) Operational-provenance node — recorded inside the gate.
                # The merge_reattachment record (set by _retarget_to_canonical) is
                # load-bearing for reverse-merge (G8), so it MUST be carried into the
                # node and the node MUST be recorded even when no provenance recorder
                # was injected (reversibility invariant). Fall back to the module-level
                # recorder; both write the same .knowledge/provenance/nodes.jsonl.
                basis = {
                    "policy_version": authored.decision_basis.get("policy_version"),
                    "dedup_score": authored.decision_basis.get("dedup_score"),
                    "dedup_candidates": authored.decision_basis.get("dedup_candidates", []),
                    "merge_rebase_branch": rebase_branch,
                    "commit": sha,
                    "canonical_path": str(canonical_path),
                }
                if "merge_reattachment" in authored.decision_basis:
                    basis["merge_reattachment"] = authored.decision_basis["merge_reattachment"]
                if self._provenance is not None:
                    self._provenance.record(intent_id, basis)
                elif "merge_reattachment" in basis:
                    # No injected recorder, but a merge happened — persist the
                    # reattachment record so the merge stays reversible.
                    from gateway import provenance as _prov
                    _prov.record(intent_id, basis, root=self._root)

                return OperationResult(
                    success=True,
                    intent_id=intent_id,
                    disposition=dedup_disposition,
                    canonical_path=canonical_path,
                    paths_touched=touched,
                    summary=f"{intent_id}: {dedup_disposition} {canonical_rel} at {sha[:8]}",
                )
        except locking.LockTimeout:
            return OperationResult(
                success=False,
                intent_id=intent_id,
                disposition="retry-later",
                retry_after=COMMIT_LOCK_RETRY_AFTER,
                errors=["commit barrier busy; retry later"],
                summary=f"{intent_id}: commit deferred (commit-barrier contention)",
            )

    # --- dedup re-check (Phase 3, §6 I1) -------------------------------

    def _page_front(self, rel: str) -> dict:
        """Parse the committed page's frontmatter (current-as-of-HEAD)."""
        from gateway import frontmatter as fm

        abs_path = self._root / rel
        try:
            front, _ = fm.parse(abs_path.read_text())
        except Exception:
            return {}
        return front or {}

    @staticmethod
    def _merge_kind(page_type: str, entity_kind: str) -> str:
        """The kind used for the cross-kind merge guard. A concept page is its own
        kind (`concept`); an entity page is its declared `entity_kind` (e.g.
        `drug`). This keeps cross-kind protection (drug vs concept never merge)
        while letting concept-vs-concept merge even when the page omits
        `entity_kind` (review I2)."""
        if page_type == "concept":
            return "concept"
        return entity_kind or page_type

    def _dedup_recheck(self, authored: "AuthoredIntent"):
        """Deterministic, LLM-free dedup at the serial gate (§6 I1). Reads the entity
        namespace as of HEAD (recall-only) under REBUILD_LOCK quiesce so a concurrent
        shadow-swap cannot show a half-state (entry gate 2). Returns a replayable
        Verdict; NEVER calls a model."""
        from gateway import dedup

        ident_d = authored.intent.identity or {}
        page_type = ident_d.get("page_type")
        if page_type not in ("entity", "concept"):
            return dedup.Verdict("distinct", None, "not-an-entity-deposit", {})
        # Normalized merge kind: a concept page rarely sets `entity_kind`, so the
        # deposit and the candidate must compare on the SAME basis or every concept
        # reads as cross-kind and never merges (review I2). For concepts the kind is
        # the page type; for entities it is the declared entity_kind.
        identity = dedup.DepositIdentity(
            entity_kind=self._merge_kind(page_type, ident_d.get("entity_kind", "")),
            canonical_name=ident_d.get("canonical_name", ""),
            aliases=tuple(ident_d.get("aliases", ()) or ()),
            domains=tuple(ident_d.get("domains", ()) or ()),
        )
        candidates: list[dedup.Candidate] = []
        if self._embedding_index is not None:
            text = " ".join([identity.canonical_name, *identity.aliases]).strip()
            with locking.file_lock(REBUILD_LOCK):  # quiesce vs shadow-swap (entry gate 2)
                hits = self._embedding_index.nn("entity", text, k=10) if text else []
            for h in hits:
                rel = h.key
                # Skip the deposit's own slug (it is not yet committed, but defensive).
                if rel in authored.writes:
                    continue
                front = self._page_front(rel)
                cand_type = str(front.get("type", ""))
                candidates.append(dedup.Candidate(
                    slug=Path(rel).stem,
                    entity_kind=self._merge_kind(
                        cand_type, front.get("entity_kind", "")
                    ),
                    canonical_name=front.get("canonical_name", front.get("title", "")),
                    aliases=tuple(front.get("aliases", ()) or ()),
                    domains=tuple(front.get("domains", ()) or ()),
                    nn_distance=h.distance,
                ))
        band = 0.15   # «dedup.blocking_nn_threshold»
        thr = 0.30    # «embed.dedup_identity_threshold»
        return dedup.adjudicate(
            identity, candidates, blocking_band=band, identity_threshold=thr
        )

    def _retarget_to_canonical(
        self, authored: "AuthoredIntent", target_slug: str
    ) -> "AuthoredIntent":
        """Merge-reattachment (§5.3): rewrite the deposit so its content lands on
        the existing canonical page instead of minting the deposited slug.

        On merge the gate must NOT silently drop the deposit's body, wikilinks, or
        identity surfaces (review B1):

        - the deposit's frontmatter ``aliases`` + ``canonical_name`` are unioned
          into the canonical page's alias set (those surfaces are how future
          deposits find the referent — dropping them regresses dedup recall);
        - the deposit's non-``## Claims`` sections (with their wikilinks) are
          carried onto the canonical page when the canonical page lacks that
          heading; if a section heading collides with non-identical content the
          merge dead-letters (``needs-manual-merge``) rather than dropping body;
        - ``## Claims`` bullets are unioned (existing behavior);
        - a tombstone with ``merged_into:`` is written at the deposited slug so
          inbound ``[[entities/<slug>]]`` links resolve and the merge is reversible.
        """
        from gateway import frontmatter as fm

        # Resolve the canonical page's REAL location. _dedup_recheck admits both
        # entity and concept deposits and the entity namespace indexes concept
        # pages, so the canonical page may live under wiki/concepts/ — never
        # hardcode wiki/entities/ (review I2: a concept would hit the not-exists
        # fallback and mint a duplicate).
        target_rel = None
        for sub in ("entities", "concepts"):
            cand_rel = f"wiki/{sub}/{target_slug}.md"
            if (self._root / cand_rel).exists():
                target_rel = cand_rel
                break
        if target_rel is None:
            # No canonical page on disk to attach to — fall back to minting as-is.
            return authored

        # The deposit is exactly one write (the deposited slug).
        dep_rel, dep_content = next(iter(authored.writes.items()))
        target_abs = self._root / target_rel
        target_content = target_abs.read_text()

        try:
            tgt_front, tgt_body = fm.parse(target_content)
        except Exception:
            tgt_front, tgt_body = {}, target_content
        try:
            dep_front, dep_body = fm.parse(dep_content)
        except Exception:
            dep_front, dep_body = {}, dep_content

        # (a) Union identity surfaces (aliases + canonical_name) into the canonical
        #     frontmatter so the merged-away surfaces stay discoverable.
        def _as_list(v):
            if v is None:
                return []
            return list(v) if isinstance(v, (list, tuple)) else [v]

        preexisting_aliases = list(_as_list(tgt_front.get("aliases")))
        alias_set = list(preexisting_aliases)
        # B-only aliases: the surfaces this deposit CONTRIBUTED (added beyond the
        # canonical's pre-existing set). Recorded for reverse-merge so the reverse
        # removes only B's contributions — never an alias that predated the merge
        # (review CRITICAL: aliases_unioned must be B-only, matching how
        # claims_unioned/sections_carried already record B-only).
        aliases_contributed: list[str] = []
        for a in (*_as_list(dep_front.get("aliases")),
                  dep_front.get("canonical_name"), dep_front.get("title")):
            if a and a not in alias_set and a != tgt_front.get("canonical_name") \
                    and a != tgt_front.get("title"):
                alias_set.append(a)
                aliases_contributed.append(a)
        if alias_set:
            tgt_front = dict(tgt_front)
            tgt_front["aliases"] = alias_set

        # (b) Split both bodies into (heading -> section text). Carry the deposit's
        #     non-Claims sections that the canonical page lacks; a heading collision
        #     with differing content is a real merge → dead-letter, not a drop.
        def _sections(body: str) -> "list[tuple[str, str]]":
            out: list[tuple[str, str]] = []
            cur_h = ""
            cur: list[str] = []
            for line in body.splitlines():
                if line.strip().startswith("## "):
                    out.append((cur_h, "\n".join(cur)))
                    cur_h = line.strip()
                    cur = []
                else:
                    cur.append(line)
            out.append((cur_h, "\n".join(cur)))
            return out

        tgt_sections = _sections(tgt_body)
        tgt_headings = {h.lower() for h, _ in tgt_sections if h}
        dep_sections = _sections(dep_body)

        # Canonical preamble (text before the first ## heading), normalized to a
        # set of non-blank lines for subset comparison.
        tgt_preamble = next((t for h, t in tgt_sections if not h), "")
        tgt_pre_lines = {
            ln.strip() for ln in tgt_preamble.splitlines() if ln.strip()
        }

        carried: list[tuple[str, str]] = []
        dep_claim_bullets: list[str] = []
        for h, text in dep_sections:
            hl = h.lower()
            if hl.startswith("## claims"):
                dep_claim_bullets += [
                    ln.strip() for ln in text.splitlines()
                    if ln.strip().startswith("- ")
                ]
                continue
            if not h:
                # Preamble (before the first ## heading). A non-empty preamble that
                # introduces content NOT already on the canonical preamble must not
                # be silently dropped (review N1, same class as B1): carry the
                # novel lines onto the canonical page under a heading. An empty /
                # byte-equal / subset preamble (the common `# Overview\nstub.`
                # case) stays inert — no false dead-letter.
                novel = [
                    ln for ln in text.splitlines()
                    if ln.strip() and ln.strip() not in tgt_pre_lines
                ]
                if novel:
                    carried.append(("## Merged context", "\n".join(novel)))
                continue
            if hl in tgt_headings:
                # Heading collision: only safe if byte-identical, else dead-letter.
                tgt_text = next(
                    (t for hh, t in tgt_sections if hh.lower() == hl), ""
                )
                if text.strip() and text.strip() != tgt_text.strip():
                    raise self.RebaseConflict(target_rel)  # → needs-manual-merge
                continue
            carried.append((h, text))

        # Reassemble the canonical body: existing body + carried sections + unioned
        # claims.
        tgt_existing_bullets = {
            ln.strip() for ln in tgt_body.splitlines()
            if ln.strip().startswith("- ")
        }
        new_body = tgt_body.rstrip()
        for h, text in carried:
            new_body = new_body.rstrip() + "\n\n" + h + "\n" + text.rstrip() + "\n"
        new_claims = [b for b in dep_claim_bullets if b not in tgt_existing_bullets]
        if new_claims:
            if "## Claims" not in new_body:
                new_body = new_body.rstrip() + "\n\n## Claims\n"
            new_body = new_body.rstrip() + "\n" + "\n".join(new_claims) + "\n"
        if not new_body.endswith("\n"):
            new_body += "\n"

        new_target = fm.serialize(tgt_front, new_body)

        # (c) Tombstone at the deposited slug so inbound wikilinks resolve and the
        #     merge is reversible.
        tomb_front = {
            "type": dep_front.get("type", "entity"),
            "title": dep_front.get("title") or dep_front.get("canonical_name") or "",
            "merged_into": target_slug,
            "redirect": f"[[{target_rel[len('wiki/'):-len('.md')]}]]",
        }
        tomb_body = (
            f"# {tomb_front['title']}\n\n"
            f"Merged into [[{target_rel[len('wiki/'):-len('.md')]}]] "
            f"(dedup §5.3). This page is a redirect tombstone.\n"
        )
        tombstone = fm.serialize(tomb_front, tomb_body)

        # Record the reattachment set in provenance (consistent with §5.3).
        basis = dict(authored.decision_basis)
        basis.setdefault("merge_reattachment", {
            "target": target_rel,
            "tombstone": dep_rel,
            # B-ONLY aliases (contributed by this deposit), NOT the full union —
            # reverse-merge strips exactly these, leaving pre-merge aliases intact.
            "aliases_unioned": aliases_contributed,
            "sections_carried": [h for h, _ in carried],
            "claims_unioned": new_claims,
        })

        head_oid = self._head_blob_oid(target_rel)
        return AuthoredIntent(
            intent=authored.intent,
            writes={target_rel: new_target, dep_rel: tombstone},
            base_oid=authored.base_oid,
            base_oids={target_rel: head_oid, dep_rel: None},
            decision_basis=basis,
        )

    # --- reversal apply-path (Phase 5 T1, G1/G3/G8) --------------------

    def _commit_reversal_writes(
        self,
        intent_id: str,
        writes: dict[str, str],
        deletes: list[str],
        basis: dict,
        summary: str,
    ) -> OperationResult:
        """Apply a reversal's writes + deletes as one provenanced git commit.

        Mirrors the deposit commit boundary: durably declare the write set,
        apply per-file atomic writes, stage adds + removals, commit with the
        Intent-Id trailer, set committed state, record provenance. Shared by
        both reversal kinds so the atomic boundary is identical."""
        declared = list(writes) + list(deletes)
        try:
            self._queue.set_declared_writes(intent_id, declared)
        except KeyError:
            pass

        touched: list[Path] = []
        for rel, content in writes.items():
            abs_path = self._root / rel
            write_atomic(abs_path, content)
            touched.append(abs_path)
        for rel in deletes:
            abs_path = self._root / rel
            if abs_path.exists():
                abs_path.unlink()

        add_paths = [str(self._root / rel) for rel in writes]
        if add_paths:
            self._git("add", "--", *add_paths)
        for rel in deletes:
            self._git("rm", "-q", "--ignore-unmatch", "--", rel, check=False)

        canonical_rel = next(iter(writes)) if writes else (deletes[0] if deletes else "")
        empty = self._git("diff", "--cached", "--quiet", check=False).returncode == 0
        msg = f"revert(librarian-commit): {canonical_rel}\n\nIntent-Id: {intent_id}\n"
        commit_args = ["commit", "-qm", msg]
        if empty:
            commit_args.insert(1, "--allow-empty")
        self._git(*commit_args)
        sha = self._git("rev-parse", "HEAD").stdout.strip()

        self._queue.set_state(
            intent_id, "committed",
            result={"commit": sha, "disposition": "reverted"},
        )
        # Reversibility invariant: a reversal MUST record a provenance node. Use
        # the injected provenance if present, else the module-level recorder (both
        # write the same .knowledge/provenance/nodes.jsonl).
        prov_basis = {**basis, "commit": sha}
        if self._provenance is not None:
            self._provenance.record(intent_id, prov_basis)
        else:
            from gateway import provenance as _prov
            _prov.record(intent_id, prov_basis, root=self._root)

        canonical_path = (self._root / canonical_rel) if canonical_rel else None
        return OperationResult(
            success=True,
            intent_id=intent_id,
            disposition="committed",
            canonical_path=canonical_path,
            paths_touched=touched,
            summary=f"{intent_id}: {summary} at {sha[:8]}",
        )

    # --- Policy-edit gate (Phase 5 T6, G7) -----------------------------------

    @staticmethod
    def _derive_dedup_params(proposed_dedup: dict):
        """Map a proposed policy's ``dedup`` block to adjudication parameters.

        Returns ``(blocking_band, identity_threshold, adjudicator_or_None)``.

        The dedup parameters that govern adjudication are read FROM the proposed
        policy so the gate evaluates the proposed policy (not a fixed config):
          - ``blocking_band`` / ``identity_threshold`` — passed to the real
            ``dedup.adjudicate`` (defaults to the production baseline if absent).
          - ``nn_distance_threshold`` — a loose policy often expresses the
            candidate-net width here; map it onto ``blocking_band`` when no
            explicit ``blocking_band`` is given (a wide net turns DISTINCT
            sibling pairs into spurious links — a merge-map regression).
          - ``strategy == "geometry-only"`` — a fundamentally different
            adjudication model (merge by geometry alone, ignoring alias
            authority); simulated with a dedicated adjudicator since it cannot
            be expressed via the real ``adjudicate`` params.

        Any other strategy flows through the real ``adjudicate`` under the
        derived params, so a corrupting policy is caught by the golden
        regardless of how it is named.
        """
        from gateway.evaluate.merge_map_eval import (
            DEFAULT_BLOCKING_BAND,
            DEFAULT_IDENTITY_THRESHOLD,
        )

        strategy = proposed_dedup.get("strategy")

        # nn_distance_threshold, when present, widens the candidate net — map it
        # onto blocking_band unless an explicit blocking_band is given.
        nn_threshold = proposed_dedup.get("nn_distance_threshold")
        blocking_band = proposed_dedup.get("blocking_band")
        if blocking_band is None:
            blocking_band = (
                float(nn_threshold) if nn_threshold is not None
                else DEFAULT_BLOCKING_BAND
            )
        else:
            blocking_band = float(blocking_band)

        identity_threshold = proposed_dedup.get("identity_threshold")
        identity_threshold = (
            float(identity_threshold) if identity_threshold is not None
            else DEFAULT_IDENTITY_THRESHOLD
        )

        if strategy == "geometry-only":
            from gateway.dedup import Candidate, DepositIdentity
            geo_threshold = (
                float(nn_threshold) if nn_threshold is not None else identity_threshold
            )

            def _geometry_only(identity: DepositIdentity, candidates: list) -> str:
                if not candidates:
                    return "distinct"
                return "merge" if candidates[0].nn_distance <= geo_threshold else "distinct"

            return blocking_band, identity_threshold, _geometry_only

        return blocking_band, identity_threshold, None

    # Strict domain-slug regex (HIGH 2: path-traversal guard). A domain slug
    # is computed into a filesystem path; an unvalidated slug like "../../etc/x"
    # escapes the policies root. The same regex is enforced at the policy_edit()
    # enqueue layer — this is the defense-in-depth backstop at the gate.
    _DOMAIN_SLUG_RE = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}")

    def _apply_policy_edit(
        self, authored: "AuthoredIntent", intent_id: str
    ) -> OperationResult:
        """Apply a privileged policy-edit intent with dual-gate non-regression check.

        Gate protocol (order matters — all must pass before any write):
          1. eval-retrieval --compare (fts recall@10 ≥ RECALL_FLOOR=0.90).
          2. merge_map_eval on the curated dedup golden (no regressions in
             merge precision — guards alias-authority discipline).
          2b. If the policy proposes a ``dedup.strategy``, simulate it against
             the merge-map golden and reject if it regresses (e.g. geometry-only).

        FAIL-CLOSED (HIGH 1): a gate-eval exception DEAD-LETTERS the intent
        (policy NOT written). The gate must never fail open — an error in the
        eval path is treated as a gate failure, not a skip. The ONLY legitimate
        skip is for a missing golden/retrieval set in a dev/test environment,
        and that is gated on the explicit ``GATEWAY_DEV_SKIP_POLICY_GATES`` env
        marker, never a blanket exception catch.

        PATH-TRAVERSAL (HIGH 2): the domain slug is validated against a strict
        regex, and the resolved target path is asserted to be contained within
        the policies root, before any write.

        Policy files live under .knowledge/policies/ (gitignored). This method
        writes them directly (no git add) and records a provenance node. The
        intent is marked "committed" in the queue on success.

        Note: hardcoded threshold constants (COMMIT_LOCK_ACQUIRE_TIMEOUT,
        deposit.py MAX_BACKLOG) are gated by code-review/PR, not this runtime
        path. The boundary is documented in lint/policy_provenance.py.
        """
        RECALL_FLOOR = 0.90
        dev_skip = bool(os.environ.get("GATEWAY_DEV_SKIP_POLICY_GATES"))

        payload = authored.intent.payload or {}
        domain = payload.get("domain")
        policy_data = payload.get("policy_data")
        reason = payload.get("reason", "")

        if not domain or not isinstance(domain, str):
            return self._dead_letter(intent_id, "policy-edit missing domain")
        # HIGH 2: reject a domain slug that is not a strict slug (path-traversal guard).
        if not self._DOMAIN_SLUG_RE.fullmatch(domain):
            return self._dead_letter(
                intent_id,
                f"policy-edit: invalid domain slug {domain!r} "
                f"(must match [a-z0-9][a-z0-9_-]{{0,63}}) — possible path traversal",
            )
        if not policy_data or not isinstance(policy_data, dict):
            return self._dead_letter(intent_id, "policy-edit missing policy_data")

        # --- Gate 1: eval-retrieval --compare (recall@10 ≥ RECALL_FLOOR) ---
        # FAIL-CLOSED: any eval exception dead-letters. The only skip is a
        # missing golden under the explicit dev-skip marker.
        try:
            from gateway.evaluate import retrieval_eval as _rev
            goldens = _rev.load_goldens()
            report = _rev.evaluate("fts", goldens=goldens, k=10)
            recall = report.recall_at(10)
            if recall < RECALL_FLOOR:
                return self._dead_letter(
                    intent_id,
                    f"policy-edit gate: fts recall@10={recall:.3f} < floor {RECALL_FLOOR}"
                    f" — policy not written",
                )
        except FileNotFoundError as exc:
            if not dev_skip:
                return self._dead_letter(
                    intent_id,
                    f"policy-edit gate: retrieval goldens not found ({exc!r}) — "
                    f"failing closed (set GATEWAY_DEV_SKIP_POLICY_GATES to skip in dev)",
                )
            log.warning("policy-edit: eval-retrieval gate dev-skipped (%s)", exc)
        except Exception as exc:
            return self._dead_letter(
                intent_id,
                f"policy-edit gate: eval-retrieval failed ({exc!r}) — failing closed",
            )

        # --- Gate 2: merge-map golden under the PROPOSED policy's dedup params ---
        # CRITICAL: the gate must EVALUATE THE PROPOSED POLICY, not a fixed
        # config. We derive the dedup adjudication parameters from policy_data
        # and simulate adjudication with THOSE params against the golden. Any
        # merge-map regression (a decision that no longer matches the golden's
        # ground truth) under the proposed params dead-letters — for ALL
        # strategies, not a single hardcoded string.
        #
        # FAIL-CLOSED: any eval exception dead-letters; missing golden only
        # skips under the dev marker.
        golden_path = self._root / ".knowledge" / "eval" / "dedup" / "golden.yaml"
        if not golden_path.exists():
            if not dev_skip:
                return self._dead_letter(
                    intent_id,
                    f"policy-edit gate: dedup golden not found at {golden_path} — "
                    f"failing closed (set GATEWAY_DEV_SKIP_POLICY_GATES to skip in dev)",
                )
            log.warning("policy-edit: merge-map golden gate dev-skipped (missing golden)")
        else:
            blocking_band, identity_threshold, custom_adjudicator = (
                self._derive_dedup_params(policy_data.get("dedup") or {})
            )
            try:
                from gateway.evaluate.merge_map_eval import merge_map_eval
                mm_result = merge_map_eval(
                    golden_path,
                    root=self._root,
                    adjudicator=custom_adjudicator,
                    blocking_band=blocking_band,
                    identity_threshold=identity_threshold,
                )
            except Exception as exc:
                return self._dead_letter(
                    intent_id,
                    f"policy-edit gate: merge-map golden eval failed ({exc!r}) — failing closed",
                )
            if mm_result.regressions:
                return self._dead_letter(
                    intent_id,
                    f"policy-edit gate: proposed policy regresses merge-map golden "
                    f"precision — {len(mm_result.regressions)} case(s) mis-scored "
                    f"(precision={mm_result.precision:.3f}); policy NOT written: "
                    f"{mm_result.regressions}",
                )

        # --- All gates passed — write the policy file ---
        import yaml as _yaml
        from gateway.filter.policy import policy_path as _policy_path
        target = _policy_path(domain)

        # HIGH 2 (defense in depth): assert the resolved target is contained
        # within the policies root before writing — even though the slug passed
        # the regex, a symlinked or otherwise unexpected policies dir could let
        # a write escape. Containment is the load-bearing invariant.
        policies_root = (self._root / ".knowledge" / "policies").resolve()
        resolved_target = target.resolve()
        if not (
            resolved_target == policies_root
            or str(resolved_target).startswith(str(policies_root) + os.sep)
        ):
            return self._dead_letter(
                intent_id,
                f"policy-edit: resolved path {resolved_target} escapes policies root "
                f"{policies_root} — refusing to write",
            )

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(_yaml.dump(policy_data, allow_unicode=True))

        # Record provenance node.
        basis: dict = {
            "op": "policy-edit",
            "domain": domain,
            "reason": reason,
            "policy_version": payload.get("policy_version"),
            "provenance_type": "policy-edit",
        }
        try:
            self._queue.set_state(
                intent_id, "committed",
                result={"domain": domain, "policy_path": str(target)},
            )
        except KeyError:
            pass

        if self._provenance is not None:
            self._provenance.record(intent_id, basis)
        else:
            from gateway import provenance as _prov
            _prov.record(intent_id, basis, root=self._root)

        return OperationResult(
            success=True,
            intent_id=intent_id,
            disposition="committed",
            canonical_path=target,
            summary=f"{intent_id}: policy-edit committed for domain {domain!r}",
        )

    def _dead_letter(self, intent_id: str, reason: str) -> OperationResult:
        """Dead-letter a reversal that cannot apply, without touching the corpus."""
        try:
            self._queue.set_state(intent_id, "dead_lettered", result={"reason": reason})
        except KeyError:
            pass
        return OperationResult(
            success=False,
            intent_id=intent_id,
            disposition="dead_lettered",
            errors=[reason],
            summary=f"{intent_id}: dead-lettered ({reason})",
        )

    def _apply_reversal(
        self, authored: "AuthoredIntent", intent_id: str, fencing_token: int
    ) -> OperationResult:
        """Dispatch a reversal intent to its kind-specific apply helper."""
        payload = authored.intent.payload or {}
        kind = payload.get("reversal_type")
        if kind == "contradiction-resolution":
            return self._apply_contradiction_revert(payload, intent_id)
        if kind == "reverse-merge":
            return self._apply_reverse_merge(payload, intent_id)
        if kind == "depath":
            return self._apply_depath(payload, intent_id)
        if kind == "restore-depath":
            return self._apply_restore_depath(payload, intent_id)
        return self._dead_letter(intent_id, f"unknown reversal_type {kind!r}")

    def _apply_depath(self, payload: dict, intent_id: str) -> OperationResult:
        """De-path an orphaned uncited page through the gate (G6, Phase 5 Task 2).

        Removes the target page via the commit machinery (tracked git delete),
        recording the page CONTENT in the provenance node so a ``restore-depath``
        intent can bring it back. Reversibility invariant: the de-path is a
        provenanced act and never destroys a page whose content is unrecoverable.
        A missing target dead-letters (no mutation)."""
        target_rel = payload.get("target_rel")
        if not target_rel:
            return self._dead_letter(intent_id, "depath missing target_rel")

        abs_path = self._root / target_rel
        if not abs_path.exists():
            return self._dead_letter(
                intent_id, f"depath target {target_rel!r} does not exist"
            )

        # Capture content BEFORE deletion so the act is reversible (the restore
        # intent re-creates the page from this recorded content — never a guess).
        try:
            depathed_content = abs_path.read_text()
        except OSError as e:
            return self._dead_letter(intent_id, f"cannot read depath target: {e}")

        basis = {
            "reversal_type": "depath",
            "target": target_rel,
            "depathed_content": depathed_content,
            "policy_version": payload.get("policy_version"),
        }
        return self._commit_reversal_writes(
            intent_id, {}, [target_rel], basis,
            summary=f"de-pathed {target_rel}",
        )

    def _apply_restore_depath(
        self, payload: dict, intent_id: str
    ) -> OperationResult:
        """Restore a previously de-pathed page (reverse of de-path, G6).

        Re-creates the page from the content carried in the intent payload (the
        de-path provenance node's ``depathed_content``). Missing content →
        dead-letter (cannot restore without the recorded body)."""
        target_rel = payload.get("target_rel")
        content = payload.get("content")
        if not target_rel:
            return self._dead_letter(intent_id, "restore-depath missing target_rel")
        if not content:
            return self._dead_letter(
                intent_id, "restore-depath missing content (nothing to restore)"
            )

        basis = {
            "reversal_type": "restore-depath",
            "target": target_rel,
            "policy_version": payload.get("policy_version"),
        }
        return self._commit_reversal_writes(
            intent_id, {target_rel: content}, [], basis,
            summary=f"restored de-pathed page {target_rel}",
        )

    def _apply_contradiction_revert(
        self, payload: dict, intent_id: str
    ) -> OperationResult:
        """Undo a claim-contradiction auto-resolve (G1, G3).

        Reads the named act, locates the page carrying the materialized
        ``## Contested`` edge (cites the loser source), strips that section, and
        marks the act reverted so ``acts_to_reopen`` no longer returns it. Both
        claims survive (the loser was never deleted). Unknown act → dead-letter."""
        from gateway import contradictions_log, frontmatter as fm

        act_id = payload.get("reverts_act")
        act = contradictions_log.find_act(act_id) if act_id else None
        if act is None:
            return self._dead_letter(intent_id, f"unknown act {act_id!r}")

        loser = act.get("loser", {}) or {}
        loser_src = str(loser.get("source") or "")
        edge_token = f"[[sources/{loser_src}|disputes]]"

        # Locate the page whose body carries the ## Contested edge citing the loser.
        wiki = self._root / "wiki"
        target_rel: str | None = None
        target_body: str | None = None
        target_front: dict | None = None
        if wiki.exists():
            for p in sorted(wiki.rglob("*.md")):
                try:
                    front, body = fm.parse(p.read_text())
                except Exception:
                    continue
                if "## Contested" in body and edge_token in body:
                    target_rel = str(p.relative_to(self._root))
                    target_body = body
                    target_front = front
                    break

        if target_rel is None:
            return self._dead_letter(
                intent_id, f"no page carries the contested edge for act {act_id!r}"
            )

        # Strip the ## Contested section (from its header to the next ## or EOF).
        new_body = self._strip_section(target_body, "## Contested")
        new_content = fm.serialize(target_front, new_body)

        basis = {
            "reversal_type": "contradiction-resolution",
            "reverts_act": act_id,
            "policy_version": payload.get("policy_version"),
            "target": target_rel,
        }
        result = self._commit_reversal_writes(
            intent_id, {target_rel: new_content}, [], basis,
            summary=f"reverted contradiction act {act_id}",
        )
        if result.success:
            contradictions_log.mark_act_reverted(act_id, intent_id)
        return result

    @staticmethod
    def _strip_section(body: str, header: str) -> str:
        """Remove a markdown section (its header line through the line before the
        next same-or-higher-level header, or EOF). Trailing whitespace normalized."""
        lines = body.splitlines()
        out: list[str] = []
        i = 0
        n = len(lines)
        while i < n:
            if lines[i].strip() == header:
                # skip until the next top-level (## ) header or EOF
                i += 1
                while i < n and not lines[i].lstrip().startswith("## "):
                    i += 1
                continue
            out.append(lines[i])
            i += 1
        text = "\n".join(out).rstrip() + "\n"
        return text

    def _apply_reverse_merge(self, payload: dict, intent_id: str) -> OperationResult:
        """Restore a deduped page from the recorded reattachment set (G8).

        Builds the reverse_merge_plan from the tombstone + provenance node, strips
        the unioned aliases/sections/claims B contributed off the canonical, and
        deletes the tombstone. Uses the RECORDED reattachment set (never a diff
        guess — drops hide in diffs, Phase-3 lesson). Non-tombstone → dead-letter."""
        from gateway import retraction, frontmatter as fm

        tombstone_rel = payload.get("tombstone_rel")
        if not tombstone_rel:
            return self._dead_letter(intent_id, "reverse-merge missing tombstone_rel")

        try:
            plan = retraction.reverse_merge_plan(tombstone_rel, root=self._root)
        except (FileNotFoundError, ValueError, KeyError) as e:
            return self._dead_letter(intent_id, f"no reverse-merge plan: {e}")

        canon_abs = self._root / plan.canonical_rel
        if not canon_abs.exists():
            return self._dead_letter(
                intent_id, f"canonical {plan.canonical_rel} absent"
            )
        try:
            front, body = fm.parse(canon_abs.read_text())
        except Exception as e:
            return self._dead_letter(intent_id, f"cannot parse canonical: {e}")

        # Strip the aliases B contributed (frontmatter aliases: list).
        aliases = list(front.get("aliases", []) or [])
        to_remove = set(plan.aliases_to_remove)
        front["aliases"] = [a for a in aliases if a not in to_remove]

        # Strip the sections B carried.
        for header in plan.sections_to_remove:
            body = self._strip_section(body, header)

        # Strip the claims B contributed (exact bullet-line match, citation-tolerant).
        claim_lines = {c.strip() for c in plan.claims_to_remove}
        kept: list[str] = []
        for line in body.splitlines():
            if line.strip() in claim_lines:
                continue
            kept.append(line)
        body = "\n".join(kept).rstrip() + "\n"

        new_content = fm.serialize(front, body)
        basis = {
            "reversal_type": "reverse-merge",
            "tombstone": tombstone_rel,
            "target": plan.canonical_rel,
            "aliases_removed": plan.aliases_to_remove,
            "sections_removed": plan.sections_to_remove,
            "claims_removed": plan.claims_to_remove,
            "policy_version": payload.get("policy_version"),
        }
        return self._commit_reversal_writes(
            intent_id,
            {plan.canonical_rel: new_content},
            [plan.tombstone_to_delete],
            basis,
            summary=f"reverse-merged {tombstone_rel} into {plan.canonical_rel}",
        )

    # --- claim-level contradiction (Phase 3, Task 7) -------------------

    @staticmethod
    def _claim_object(line: str, subject: str) -> str | None:
        """The object part of a ``- <subject> <object> [[sources/..]]`` bullet,
        or None if the bullet does not assert ``subject``."""
        s = line.strip().lstrip("- ").strip()
        sub = subject.strip().lower()
        if not s.lower().startswith(sub):
            return None
        rest = s[len(sub):].strip()
        # drop the trailing citation so the object compares cleanly
        rest = re.sub(r"\[\[sources/[^\]]+\]\]", "", rest).strip()
        return rest

    def _detect_and_resolve_claim_contradiction(
        self, authored: "AuthoredIntent"
    ) -> "AuthoredIntent | None":
        """If the deposit asserts a claim whose subject already has a different
        object on the target page (HEAD), auto-resolve by policy (§6 Task 7).

        Records a reversible act, materializes a CiTO ``disputes`` edge into the
        page body, and keeps BOTH claims (loser stays retrievable). Returns a
        rewritten AuthoredIntent (with the disputes edge) on contradiction, else
        None (no contradiction → caller proceeds normally)."""
        from gateway import frontmatter as fm
        from gateway.ops import contradiction as contra
        from gateway import trust as _trust

        ident_d = authored.intent.identity or {}
        subject = str(ident_d.get("claim_subject") or "")
        if not subject or ident_d.get("page_type") not in ("entity", "concept"):
            return None
        if len(authored.writes) != 1:
            return None
        rel, content = next(iter(authored.writes.items()))
        target_abs = self._root / rel
        if not target_abs.exists():
            return None  # first mint — nothing to contradict

        # Find the deposit's new claim (present in content, absent at HEAD).
        head_text = target_abs.read_text()
        head_lines = set(head_text.splitlines())
        try:
            _f, dep_body = fm.parse(content)
        except Exception:
            dep_body = content
        new_obj = None
        new_line = None
        for line in dep_body.splitlines():
            if line in head_lines:
                continue
            obj = self._claim_object(line, subject)
            if obj is not None:
                new_obj, new_line = obj, line.strip()
                break
        if new_obj is None:
            return None

        # Find an existing claim on the page asserting the same subject.
        existing_obj = None
        existing_line = None
        for line in head_text.splitlines():
            obj = self._claim_object(line, subject)
            if obj is not None:
                existing_obj, existing_line = obj, line.strip()
                break
        if existing_obj is None or existing_obj == new_obj:
            return None  # no prior assertion, or same object → not a contradiction

        # Resolve by policy. Sources + server-derived trust; self-report ignored.
        def _src(line):
            m = re.search(r"\[\[sources/([^\]|]+)", line or "")
            return m.group(1).strip() if m else ""

        side_existing = {
            "source": _src(existing_line),
            "source_type": self._source_type_of(_src(existing_line)),
            "claim": existing_line,
            "committed_at": "old",
        }
        side_new = {
            "source": _src(new_line),
            "source_type": str(ident_d.get("source_type", "")),
            "claim": new_line,
            "committed_at": "new",
        }
        act = contra.auto_resolve(side_existing, side_new)

        # Materialize a CiTO `disputes` edge and keep BOTH claims (loser stays
        # retrievable — down-weighted by trust at retrieval, never deleted). The
        # edge cites the LOSER's source (resolved by policy), not blindly the new
        # claim — when the new claim is the higher-trust winner the existing claim
        # is the contested one.
        loser_src = str((act.get("loser") or {}).get("source") or "")
        loser_claim = str((act.get("loser") or {}).get("claim") or "")
        edge = f"\n## Contested\n- [[sources/{loser_src}|disputes]] {loser_claim}\n"
        new_content = content.rstrip() + "\n" + edge
        return AuthoredIntent(
            intent=authored.intent,
            writes={rel: new_content},
            base_oid=authored.base_oid,
            base_oids=dict(authored.base_oids),
            decision_basis=dict(authored.decision_basis),
        )

    def _source_type_of(self, source_id: str) -> str:
        """Read a source page's ``source_type`` (for the precedence input)."""
        if not source_id:
            return ""
        src_abs = self._root / "wiki" / "sources" / f"{source_id}.md"
        front = self._page_front(f"wiki/sources/{source_id}.md")
        st = str(front.get("source_type", ""))
        if st:
            return st
        # Fall back to inferring from the id prefix (pubmed-1 → pubmed, web-9 → web).
        prefix = source_id.split("-", 1)[0]
        return prefix

    def _upsert_embeddings(self, writes: dict[str, str]) -> None:
        """Upsert committed pages into the embedding namespaces, current-as-of-HEAD.

        Quiesces on the embedding-rebuild lock (A6) so a concurrent shadow-swap
        never interleaves. Derived state: any failure self-heals on the next
        upsert/rebuild and never fails an already-committed intent.
        """
        from gateway import frontmatter as fm
        from gateway.embedding_index import REBUILD_LOCK

        try:
            with locking.file_lock(REBUILD_LOCK):
                for rel, content in writes.items():
                    try:
                        front, _ = fm.parse(content)
                    except Exception:
                        front = {}
                    self._embedding_index.upsert_page(rel, content, front)
        except Exception:  # pragma: no cover - derived index never blocks a commit
            log.warning("embedding upsert-on-commit failed (will self-heal)", exc_info=True)

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
