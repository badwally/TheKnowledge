# Session review — 2026-06-19 — Librarian Phase 5 (Lifecycle & demand governance)

Scope: the full Phase-5 build, subagent-driven (6 tasks, T1–T6), gate, merge (PR #31 → `ee97cc9e`). Diff `dbf4888b..ee97cc9e`: 50 files, +8,706/−35 (~3,524 src / ~5,200 test, ≈1.5:1). `commit_gate.py` +684/−10. Coordinator ran lean; all build/review/fix in subagents.

---

## § 1 — Code and coding quality

**[High → RESOLVED, note the systemic risk] The recurring "inert in production" defect class.** The independent reviewer≠author gate caught a defect in **all six tasks**, clustered into one failure mode: code that passed the author's own green tests but did nothing / the wrong thing on real data — inert de-path op (T2, `remediate.py` enqueued a payload with no gate apply-branch), dead cold-start gate (T4, `demand_ledger.py` — `mass>=3` subsumed by `mass>=5`), tautological I4 test (T4, `_BumpedEncoder` called the real encoder → identical vectors), inert cascade-depth detector (T5, read a sidecar nothing wrote), gate that matched one hardcoded string instead of the proposed policy (T6, `_apply_policy_edit`/`merge_map_eval`), and a provenance lint reading `node.get("basis")` when the key was `decision_basis` (T6). All fixed TDD with RED-on-old proof. *Residual risk:* fixes were verified by reviewers driving real data; the next phase must keep that — unit tests alone did not surface any of these.

**[Medium] `commit_gate.py` is now the concentration point for all gate dispatch** (`src/gateway/commit_gate.py:339-351` + `_apply_reversal`/`_apply_depath`/`_apply_reverse_merge`/`_apply_policy_edit`/`_apply_revert_resolution`, ~lines 1067-1480; +684 this phase). The dispatch is coherent and mutually-exclusive (whole-branch review confirmed) and the four reversal kinds share `_commit_reversal_writes` (one atomic+containment boundary — good). But the file now holds deposit/dedup/contradiction/CAS/recovery + 5 reversal/policy branches. *Fix (next time it's touched):* extract the reversal/policy apply-helpers into a `commit_gate_reversals.py` mixin/module; the shared `_commit_reversal_writes` boundary makes this a clean cut.

**[Medium] Demand loop is schema-closed but driver-open.** `DemandLedger.cluster()` (`src/gateway/demand_ledger.py`) has no production caller — the corpus-miss→cluster→canonicalize loop never fires in a running system. Tracked: `docs/backlog/librarian-demand-cluster-driver.md`. Acceptable (T4 scoped the mechanism), but it is decision-11 documented-but-dead until wired.

**[Low] Tracked backlog of bounded-correctness items** (all in `docs/backlog/` or `.git/sdd/progress.md`): `act_id` second-granularity collision; contradiction-revert O(pages) first-match scan (only first page reverted if a loser disputes on multiple pages); fragmentation lint O(n²); A4 suppression = any shared >3-char word (same-caller); demand-ledger `gaps.jsonl` unbounded growth. Each has a revival trigger. None merge-blocking.

**Checked and clean:** test:source ratio ~1.5:1; every destructive op routes through the gate with provenance + a containment guard (`_rel_escapes_root`); `yaml.safe_load` throughout, `_git` uses argv lists (no shell injection); read-tier server registers exactly the read allowlist (policy-edit/remediate/revert absent); RED→GREEN was genuine on the fixes (reviewers reverted the fix and watched the test fail).

---

## § 2 — Token efficiency

**[Medium] `eval-retrieval --compare` run 3× due to output truncation.** `tail -20` then `grep recall` then a third `grep` for retriever labels — the first `tail` cut off the recall numbers; the comparison has two arms (fts 0.926 / grep 0.000) and I needed the labels to confirm the 0.000 was the grep baseline, not a regression. *~2 excess calls.* Alternative: first call should have been `… | grep -iE "Retriever:|recall@|MRR"` to capture arms + metrics together.

**[Medium] `timeout` not found on macOS → 3 failed lint calls re-run.** The first lint batch prefixed `timeout 120 wiki lint …`; macOS has no `timeout` (it's `gtimeout`), so all three failed and were re-run without it. *3 wasted calls.* Precondition: scoped lints were already known (from the contp) to complete in seconds — the `timeout` wrapper was unnecessary defensiveness, and `timeout` itself was an unverified-on-darwin dependency.

**[Low] `SendMessage` schema retries (2×).** First call missing required `summary`; second had `summary` >200 chars. *2 retries.* `SendMessage` is a deferred tool whose schema wasn't loaded; the second failure surfaced the full schema. Alternative: `ToolSearch select:SendMessage` once up front, or keep summaries terse from the start.

**[Low] Session-state `Edit` retries (2×).** One "file not read" (state tracking lost across a long gap), one emoji/unicode match failure on a large `old_string` block → fell back to smaller targeted edits. *~2 excess calls + 1 re-read.* Alternative: for emoji-laden blocks, edit small unique emoji-free substrings from the start.

**[Low] Over-wide session-state read at session start.** Opening read returned lines 1–599 (~28k tokens, truncated) when the contp named the exact section needed (the Phase-4 checkpoint, ~lines 207–261). The rest of the file is historical phase logs. *~25k tokens loaded, ~2k used.* Alternative: `grep -n "PHASE 4"` then a targeted offset read.

**[Low] ~8 session-state checkpoint commits** driven by the 15-edit checkpoint hook firing on subagent edit volume. Each is cheap, but the cadence was finer than the natural seam (one task ≈ one checkpoint). Raising `CLAUDE_CHECKPOINT_THRESHOLD` to ~40 would have matched task boundaries and cut ~4 interruptions. *Note:* the frequent checkpoints did keep recovery state fresh — a defensible tradeoff, not pure waste.

**Not waste (largest spend, correctly spent):** 6 × (implement → review → fix → re-review), several with multiple fix rounds (T6: 6 fix commits). This is the discipline that caught the §1 defects; the per-task brief/report/diff file-handoffs kept the coordinator window lean throughout.

---

## § 3 — Prompt and context engineering

**[Medium] My own plan under-specified two behavioral bars → review-round cost.** (a) `reverse_merge_plan` was scoped plan-only, but the G8 gate demands restoration *behavior* — caught at T1 review, cost a fix round. (b) The C1 defect: the plan + test fixtures assumed `.knowledge/policies/` is gitignored; it is git-tracked (753 files), so policy-edit left a dangling uncommitted write — masked by the test fixture's blanket `.gitignore=.knowledge/`, only caught at whole-branch review. *Lesson:* both are Verify-Before-Act-on-operations gaps — during planning I should have (i) tested the actual gitignore status of write targets, (ii) cross-checked every "produces X" against the gate's "X must behave like Y." Reinforces `[[feedback_inert_in_production_pattern]]`.

**[Medium] Subagents wrote/committed `session-state.md`.** A T6 run committed a premature "T6 complete — all shipped" session-state (`7d965221`) before the security + fix rounds ran; the checkpoint hook fired inside the subagent. Caught + corrected on the next coordinator checkpoint. *Lesson (captured as memory `[[feedback_subagents_dont_own_session_state]]`):* dispatch prompts must scope subagent reports to `.git/sdd/` and forbid session-state writes; coordinator owns it.

**[Low] Security/trust-model changes were relayed without explicit user-authorization context.** Three subagents flagged "coordinator-relayed claims carry no user authority" when asked to change fail-closed/identity behavior; they proceeded only because the changes were technically sound + branch-isolated. The work was correct, but dispatches that direct security-critical changes should carry the authorization basis (e.g. "this closes an automated-security-review HIGH" — which they did) so the worker isn't adjudicating authority. Minor; the subagents' caution was correct behavior.

**Strong (keep):** reviewer prompts aimed at *specific* risks (the explicit "inert in production / does it fire on real data" framing is what caught the dead cold-start, inert cascade-depth, and string-match gate); opus reviewers reserved for destructive/governance/subtle tasks (T1/T2/T4/T6) and the final gate, sonnet for additive (T3/T5) and implementers — right model for the difficulty; per-task `task-brief`/report/`review-package` file handoffs; Verify-Before-Act Step 0 in every dispatch touching recorded schemas; the scope-decision consultation (4→6 tasks) surfaced before building.

---

## § 4 — Session-state checkpoint

- **In-flight / open contracts:** NONE. The 5-phase Librarian multi-agent RAG build is COMPLETE. Phase 5 merged via PR #31 (merge commit `ee97cc9e`, 2026-06-19) to `origin/main`; remote+local branch `docs/librarian-phase5` deleted; local `main` == `origin/main` (0/0).
- **Decisions made:** (1) Scope expanded 4→6 tasks (added T5 G2 detectors, T6 G7+I3) + reconciled ledger §4 gate to test them — "gate green" must mean complete (`[[feedback_gate_tests_what_ships]]`). (2) Policy-edit trust model (user-ratified 2026-06-19): CLI-only (off all MCP surfaces), privilege from server-sourced `GATEWAY_POLICY_PRINCIPAL` (env/`.knowledge/secrets.env`), unset→fail-closed, principal stamped for audit. (3) `.knowledge/policies/` is git-tracked → policy writes commit through the gate's atomic boundary (Intent-Id trailer), not a bare write. (4) Reversal/de-path/policy share `_commit_reversal_writes` (fail-closed + `_rel_escapes_root` containment).
- **Rejected approaches:** Option A "declare G2/G7/I3 satisfied via existing mechanisms" (writes false green); plan-only reverse-merge (gate needs restoration behavior); full-union `aliases_unioned` (over-restored pre-existing aliases); request-borne policy-edit identity (spoofable); in-request allowlist as a hard boundary (a full-Bash agent shells out anyway).
- **Current system state:** `main` @ `ee97cc9e`, full suite **2354 passed**, `eval-retrieval --compare` fts recall@10 **0.926** (== baseline), scoped lints at baseline (orphans 758 / schema-drift 191 / broken-wikilinks 1). Working tree: only watcher-owned `index.md`/`log.md` modified + pre-existing untracked `docs/260618_librarian-rag-design-session-brief.md`. `wiki watch` daemon expected running.
- **Next atomic step:** NONE required — build complete, no Phase 6. Optional, trigger-gated only: 4 backlog follow-ups under `docs/backlog/` (policy-edit op migration, demand-cluster driver, reverse-merge producer op, demand-ledger DoS bound), each with a revival signal; do not action without the trigger.

> Note: `docs/session-state.md` on `main` still reads "PR #31 open, awaiting merge" (committed `c3e9b744` before merge). Not corrected on `main` because the global rule is branch-first on the default branch and a one-line doc fix doesn't warrant PR ceremony; git/`gh` are authoritative (PR #31 = MERGED). Next session: refresh that line.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Prompt/§3 | Plan under-specified behavioral bars + assumed gitignore status (reverse-merge plan-only; policy.yaml "gitignored") → 2 review-round costs | At plan time, Verify-Before-Act on operations: test actual gitignore/persistence of every write target; cross-check each "produces X" against the gate's "X must behave like Y" |
| 2 | Code/§1 | "Inert in production" defect class hit all 6 tasks; only reviewers-on-real-data caught them | Keep reviewer≠author + drive-on-real-data as a hard gate; require implementer tests to exercise the real production data path (real recorder/encoder/gate), per `[[feedback_inert_in_production_pattern]]` |
| 3 | Prompt/§3 | Subagent committed premature/false `session-state.md` | Dispatches forbid subagent session-state writes; scope reports to `.git/sdd/`; coordinator reconciles (`[[feedback_subagents_dont_own_session_state]]`) |
| 4 | Token/§2 | `timeout` (absent on darwin) + truncated eval output → ~5 avoidable failed/re-run calls | Don't wrap fast scoped commands in `timeout`; on darwin use `gtimeout` only if needed; grep eval output for `Retriever:|recall@|MRR` in one pass |
| 5 | Code/§1 | `commit_gate.py` +684 — all gate dispatch concentrated in one file | When next touched, extract reversal/policy apply-helpers to a module behind the shared `_commit_reversal_writes` boundary |
