# Session Review — Librarian Phase 4 (Tiered Agent Surface)

**Date:** 2026-06-19
**Branch:** `docs/librarian-phase4` (9 commits off `main` @ `d931e568`; PR pending)
**Scope:** 5 feature/fix code commits + 4 doc commits. Full suite 2182 passed (2163 baseline + 19 new). eval-retrieval fts recall@10 0.926 (unmoved). Whole-branch review GO; security review ship-it.

---

## § 1 — Code and coding quality

**[High → resolved] T1 read-tier allowlist mis-classified 3 side-effecting ops.** `src/gateway/tier.py` READ_OPS initially included `agents`, `lint`, `status` — all of which write `.knowledge/` state and/or spend model tokens (`agents` runs write-effecting batch agents). On a "read tier" whose entire security premise is a provably-safe subset, this was a privilege-boundary hole. Caught by the task reviewer (verified against op implementations, not the plan's say-so), fixed in `9d0fb655` (dropped to build tier). Root cause was the PLAN, not the implementer — see §3.

**[Medium → resolved] `commit_gate.commit()` let `LockTimeout` escape uncaught.** T2 added a bounded acquire to the commit barrier (`commit_gate.py:299`), but the first pass let `locking.LockTimeout` propagate out of `commit()` as an exception — every other path returns an `OperationResult`, and the task's own contract said "left for a later pass, not hung." Fixed in `b39c0ea1`: outer `try/except locking.LockTimeout` → `disposition="retry-later"` + `retry_after`, no queue-state mutation (intent stays durable). Verified the except can only catch a barrier-acquisition timeout (inner REBUILD_LOCK uses `timeout=None`, cannot raise). This is a root-cause fix, not a symptom patch.

**[Low → resolved] Doc overstatement in the security-critical tier rationale.** My own comment-tightening edit (`f4deeff2`) overstated the read-tier guarantee — claimed read ops never write "the FTS/embedding index," but `retrieve`/`search`/`context`/`related` trigger a self-healing FTS upsert to the gitignored `.knowledge/wiki.db` on read. The security guarantee holds (no corpus mutation, no tokens); the comment asserted more than the code delivers. Security review flagged it (F1); fixed `f12e0a66`. Lesson: a "tightening" edit on a security rationale needs the same verification as the code — I introduced an inaccuracy while removing one.

**[Low → deferred] `provenance.alarms()` division guard.** `alarms()` is safe against div-by-zero only because `min_volume` defaults to 5; a caller passing `thresholds={"min_volume": 0}` would `ZeroDivisionError`. A `if total == 0: continue` guard makes it unconditionally safe. Deferred (no caller passes 0) — logged in the SDD ledger for opportunistic fix.

**Test coverage: strong.** Each task shipped negative controls (read-tier excludes build tools; free-lock acquires immediately; healthy traffic fires no alarm; below-min_volume can't trip a spike). The bounded-acquire test uses a real second-thread holder + real `fcntl` — no monkeypatch of the path under test (honored the standing Phase-1/3 rule). Concurrency claim independently re-verified by the whole-branch + security reviewers.

**Convention: clean.** New code matches existing gateway patterns (OperationResult dispositions, `file_lock` keyword-only addition preserving 30+ positional call sites, module-constant thresholds with `«ledger-key»` comments). No dead code, no language-rule violations.

---

## § 2 — Token efficiency

**[High] Lint hung 1h28m and was launched 2–3× concurrently.** The biggest waste this session. I launched `wiki lint` (unscoped) which has no per-check timeout and stalls on network checks (`link-rot`/`nlm-pending` over ~4000 pages). I then launched it a SECOND time (the foreground re-run that got auto-backgrounded) without killing the first, so two full lints contended on `file_lock("log")` for ~1.5h. Excess: ~2 wasted background slots + several polling round-trips. **Avoidance:** for a code-only diff, lint corpus health is unchanged by construction — I should have run the fast scoped checks first (orphans/schema-drift/broken-wikilinks complete in seconds) and never launched an unscoped full lint at all. Backlog item written (`wiki-lint-unscoped-unbounded-slow.md`).

**[Low] Repeated lint-output polling.** ~5 tool calls poking at empty buffered output files before realizing Python buffers stdout under redirection. A single `pgrep`-based `until` waiter (which I eventually used) should have been the first move, not the fourth.

**Efficient: subagent file-handoffs.** Briefs/reports/diffs moved as files (`task-brief`, `review-package`), keeping the controller window lean across 3 implement + 3 review + 3 fix dispatches + 2 whole-branch reviews. The main window never loaded a subagent transcript. This is the pattern working as intended.

**Efficient: targeted interface grounding.** PLAN-phase reads were section-scoped (locking.py whole — it's 88 lines; deposit.py whole — 80 lines; targeted offsets elsewhere), not full-file sweeps. The FastMCP enumeration API was verified with a 6-line probe rather than reading the mcp library.

---

## § 3 — Prompt and context engineering

**[High] The PLAN classified ops into a privilege tier without verifying each op's side effects — the session's one real process gap.** I authored `tier.READ_OPS` with `agents`/`lint`/`status` as read-tier based on the op NAMES and the master plan's affirmative list, without reading each op's implementation. The task reviewer caught all three. For a **security-critical allowlist**, the PLAN step must apply Verify-Before-Act to each entry (read the op, confirm no write/no model call) — name-based classification is a guess. This is the generalizable finding: when a plan sorts things into a trust boundary, the sorting itself is the high-risk decision and must be grounded, not the implementation that transcribes it. (Captured in session-state for Phase 5.)

**[Medium] One design fork was resolved unilaterally mid-plan — correctly, but worth noting.** The deposit "load signal" (queue-depth shed vs bounded-admission) is a genuine fork with a ledger-key consequence (`«deposit.max_backlog»`). I resolved it on merit (queue-depth: async-clean, deterministically testable) and surfaced it to the user rather than blocking. That matched the `act_after_evaluating` memory, and the user did not object. The judgment call was sound; the surfacing was the right hedge.

**Strong: reviewer prompts carried the security premise as the attention lens.** Each task-reviewer dispatch copied the binding constraint verbatim (default-deny is a security property; over-inclusion is the defect, under-inclusion merely a cost) and gave the reviewer repo read access to verify classification against implementations — which is exactly what caught the mis-classification. No "do not flag" pre-judging. The security review prompt was framed adversarially ("find a way to abuse the new surface, not confirm it looks fine"), which produced 3 substantive findings including the doc overstatement.

**Strong: model tiering.** Implementers/task-reviewers on sonnet (transcription + scoped review from complete-code briefs); whole-branch + security reviews on opus (architecture/security judgment). No call inherited an over-powered default.

**No surface-anchor leakage.** The plan's "honest"-family and throat-clearing bans held across all subagent dispatches and code/comments.

---

## § 4 — Session-state checkpoint

- **In-flight / open contracts:** PR for `docs/librarian-phase4` → `main` NOT yet opened (the next atomic step). One clean full `wiki lint` is running in the background (`/tmp/p4_fulllint.txt`) for the aggregate RC — confirmatory only; per-scope evidence already conclusive. SDD ledger at `.git/sdd/progress.md` shows T1/T2/T3 all `[x]` clean.
- **Decisions made:** (1) Branch cut fresh as `docs/librarian-phase4` off `main` (stale contp named the deleted `docs/librarian-rag-design`). (2) Deposit backpressure = queue-depth shed (`«deposit.max_backlog»`=256), not bounded-admission — deposit holds no commit lock, authoring is concurrent. (3) A3 bounded acquire wires into the COMMIT barrier, not deposit. (4) `agents`/`lint`/`status` are build-tier (write `.knowledge/` / spend tokens). (5) A read-tier op may append log.md + self-heal the gitignored FTS index — not disqualifying.
- **Rejected approaches:** bounded-admission backpressure for deposit (flakier to test, contradicts concurrent-authoring); including `agents`/`lint`/`status`/`answer`/`cite` in the read tier (not provably side-effect-free + token-free — default-deny).
- **Current system state:** branch `docs/librarian-phase4` @ `5c960807`, working tree clean (watcher-owned `index.md`/`log.md` + a pre-existing untracked `docs/260618_…session-brief.md` not staged). Full suite 2182 passed. eval recall@10 0.926. Per-scope lint at pre-existing baseline. Whole-branch review GO + security review ship-it. 3 backlog items written (deposit fairness, file_lock path-traversal, unscoped-lint slowness).
- **Next atomic step:** open the PR (`docs/librarian-phase4` → `main`) with a body summarizing the 3 tasks + gate evidence + deferred-findings backlog; then `/clear`. Phase 5 (Lifecycle & demand governance) runs in a FRESH session via the Phase-5 contp in the master build-plan.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Prompt/process | PLAN classified ops into a privilege tier by name, not verified side effects (reviewer caught 3) | Phase 5+: any plan step that sorts into a trust boundary must Verify-Before-Act each entry against its implementation |
| 2 | Token | Unscoped `wiki lint` hung 1h28m, run 2× concurrently | Use scoped checks for code-only diffs; never launch unscoped full lint as a gate; backlog written to add per-check timeout |
| 3 | Code | `commit()` LockTimeout escaped uncaught (resolved) | Pattern: when adding a bound to a previously-unbounded primitive, audit every caller that could now raise the new exception |
| 4 | Code | Read-tier doc comment overstated the guarantee (resolved) | A "tightening" edit on a security rationale needs the same verification rigor as code |
| 5 | Token | Polled buffered lint output ~5× before using a waiter | Reach for a `pgrep`/`until` completion waiter first for any backgrounded long job |
