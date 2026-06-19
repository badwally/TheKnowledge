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
from gateway.embedding_index import REBUILD_LOCK
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

            # (§6 I1) Deterministic LLM-free dedup re-check, inside the held
            # commit mutex. A `merge` verdict re-targets the deposit's claims onto
            # the canonical page (no duplicate-referent slug minted). The verdict
            # basis is recorded into provenance for replay.
            dedup_disposition = "committed"
            verdict_dedup = self._dedup_recheck(authored)
            if verdict_dedup.decision == "merge" and verdict_dedup.target_slug:
                authored = self._retarget_to_canonical(
                    authored, verdict_dedup.target_slug
                )
                dedup_disposition = "merged"
            authored.decision_basis.setdefault("dedup_verdict", {
                "decision": verdict_dedup.decision, "rule": verdict_dedup.rule,
                "target": verdict_dedup.target_slug, "basis": verdict_dedup.basis,
            })

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
                disposition=dedup_disposition,
                canonical_path=canonical_path,
                paths_touched=touched,
                summary=f"{intent_id}: {dedup_disposition} {canonical_rel} at {sha[:8]}",
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

    def _dedup_recheck(self, authored: "AuthoredIntent"):
        """Deterministic, LLM-free dedup at the serial gate (§6 I1). Reads the entity
        namespace as of HEAD (recall-only) under REBUILD_LOCK quiesce so a concurrent
        shadow-swap cannot show a half-state (entry gate 2). Returns a replayable
        Verdict; NEVER calls a model."""
        from gateway import dedup

        ident_d = authored.intent.identity or {}
        if ident_d.get("page_type") not in ("entity", "concept"):
            return dedup.Verdict("distinct", None, "not-an-entity-deposit", {})
        identity = dedup.DepositIdentity(
            entity_kind=ident_d.get("entity_kind", ""),
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
                candidates.append(dedup.Candidate(
                    slug=Path(rel).stem,
                    entity_kind=front.get("entity_kind", ""),
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
        """Merge-reattachment (§5.3): rewrite the deposit so its claims land on the
        existing canonical page instead of minting the deposited slug. The deposit's
        ``## Claims`` lines are unioned onto the canonical page's current body. The
        deposited slug is never written (no duplicate-referent page)."""
        from gateway import frontmatter as fm

        target_rel = f"wiki/entities/{target_slug}.md"
        target_abs = self._root / target_rel
        if not target_abs.exists():
            # No canonical page on disk to attach to — fall back to minting as-is.
            return authored
        target_content = target_abs.read_text()

        # Extract the deposit's claim bullet lines (under a ## Claims heading).
        reattached: list[str] = []
        for _rel, content in authored.writes.items():
            try:
                _front, body = fm.parse(content)
            except Exception:
                body = content
            in_claims = False
            for line in body.splitlines():
                stripped = line.strip()
                if stripped.lower().startswith("## claims"):
                    in_claims = True
                    continue
                if stripped.startswith("## "):
                    in_claims = False
                    continue
                if in_claims and stripped.startswith("- "):
                    reattached.append(stripped)

        new_target = target_content.rstrip()
        if reattached:
            existing = set()
            for line in target_content.splitlines():
                s = line.strip()
                if s.startswith("- "):
                    existing.add(s)
            additions = [c for c in reattached if c not in existing]
            if additions:
                if "## Claims" not in target_content:
                    new_target += "\n\n## Claims\n"
                new_target = new_target.rstrip() + "\n" + "\n".join(additions)
            new_target += "\n"
        else:
            new_target += "\n"

        # Base the rewritten write on the target's current HEAD blob so the CAS
        # classifies it as a same-page concurrent edit (rebase), not a phantom.
        head_oid = self._head_blob_oid(target_rel)
        return AuthoredIntent(
            intent=authored.intent,
            writes={target_rel: new_target},
            base_oid=authored.base_oid,
            base_oids={target_rel: head_oid},
            decision_basis=dict(authored.decision_basis),
        )

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
