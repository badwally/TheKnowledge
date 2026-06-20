# Session review — 2026-06-19/20 — Committer + Test-Harness build (T4/T6/G1 + final gate)

Scope: the **coordinator** session that executed the final 3 of 8 tasks (T4 surface E2E, T6 inert-invariants, G1 gate script) plus the final gate (whole-branch + security review) of the Production Committer + Multi-Agent Test Harness build on `test/multi-agent-test-harness`. The implementation/test code was written and per-task-reviewed by subagents; this session's *work product* is the orchestration, the fix-loop adjudications, and the merge decision. Findings below weight that.

Branch HEAD reviewed: `1a4f932c` (merge-base `0a688378`, 23 commits). Both final reviews passed: security **SHIP IT (0 HIGH)**, whole-branch **READY TO MERGE**.

---

## § 1 — Code and coding quality

The session added no code by hand; it drove subagents. The code-level findings worth recording are the two real defects the harness *surfaced* (the build's reason to exist) and the deferred Minors.

- **High (caught + fixed, not residual) — T2 keystone routing gap.** `committer.drain_once` dead-lettered 3 enqueued intent types (policy-edit, contradiction-resolution, depath reversals) — they were enqueued but had no apply-branch in the committer. Fixed at the COMMITTER (`_is_gate_dispatched` classifier, `2b5729b9`), not the test. This is hunt-list #1 manifest in production code; the integration tier caught it. Verified clean across the producer↔gate↔committer seam by the whole-branch review.
- **High (caught + fixed) — T6 cold-start crash.** `superseded_citations.run()` (`src/gateway/lint/superseded_citations.py:18-20`) called `paths.raw_dir().iterdir()` with no existence guard → `FileNotFoundError` on a fresh clone; the only 1 of 32 lint checks unguarded. Fixed with `if not raw.exists(): return []`. **The sharp lesson: the first T6 cut MASKED this crash in the test fixture** (pre-creating `raw/`), reproducing the exact anti-pattern T6 exists to kill — the inert-in-production test was itself inert. The opus meta-gate review caught it and forced the production fix + fixture unmask, with RED-on-revert proof.
- **Medium — T6 Step 5 was self-referential.** The hunt-#1 invariant enumerated reversal_types from the same `_apply_reversal` it asserted against → structurally could never go RED on the defect it targets. Rewritten to cross-reference PRODUCER op source files vs gate dispatch; teeth proven by mutation (inject fake type → RED). A property test that derives its expectation from the unit under test proves nothing — same family as the masked-fixture defect.
- **Low / deferred (see ledger ## Minors, all triaged DEFER by whole-branch review):** D0 same-slug union body-parity (fail-safe); T2 DRY duplication in `drain_once` (`/simplify` candidate); T6 Step-1 positive coverage 5/32 (27 negative-control-only); G1 playbook B6 doc simplification of the embedding condition; T3 concurrent-same-slug-race no longer driven (honor the caveat — do not claim S1/S2 cover it).

Test coverage of the new paths: strong. Every tier drives the real producer (mutation-verified by the T6 and whole-branch reviewers). No paper-over-the-symptom fixes survived review.

---

## § 2 — Token efficiency

Coordination was lean — file handoffs (briefs/reports/diffs under `.git/sdd/`), no pasted history into dispatches, status-only returns. Two real inefficiencies:

- **Reviewer idle-without-verdict, ×2 (~2 extra round-trips).** `t4-review` and `final-wholebranch` both finished their analysis but emitted only an `idle_notification` — no `SendMessage` of the verdict to main. Each cost a `SendMessage` prompt + a wait to extract the result that already existed. **Fix:** the reviewer dispatch prompt should make the delivery contract explicit — "post your verdict to main via your final message; do not go idle without sending it." Estimated ~2–3 avoidable tool calls + latency. This is the one recurring coordination tax this session.
- **Belt-and-suspenders gate re-run (accepted cost).** G1 already ran the full gate end-to-end (2485 tests) and the ledger recorded the PASS at the exact reviewed HEAD; the final gate re-run repeats it. Justified here (it's the pre-PR verification on the precise tree being merged, and it ran in the background concurrent with session-review, so no wall-clock serialized) — but worth flagging as a deliberate redundancy, not a free check.
- **No redundant reads / no retry loops of note.** Briefs were read once; the SDD scripts were located in one probe; the merge-base computed once. The verified-interfaces block in each brief prevented re-verification of signatures (paid off — only 2 interface mismatches surfaced, both at implementer runtime, not via coordinator re-reads).

---

## § 3 — Prompt and context engineering

- **Dispatch precision was high.** Zero NEEDS_CONTEXT / BLOCKED returns across 3 implementers + 4 reviewers + 2 final reviews. Every implementer produced first-pass-usable output; the only follow-ups were review-driven fixes, not clarification rounds. The brief-as-single-source-of-requirements pattern (interfaces + constraints verbatim, exact values only in the brief file) held.
- **Plan-time Verify-Before-Act gap (the G1 embedding deviation).** The G1 brief specified the embedding check as `all namespaces .passed`. The real I2 production contract is `passed OR (fallback_active AND fallback_falsifiable)` — the entity namespace is *intentionally* below floor (lexical encoder can't do brand↔generic). Coding to the brief literally would have made the gate permanently red. The implementer caught it and corrected to the real condition; the reviewer adjudicated it legitimate with retained teeth. **Generalizable:** this is a Part-B2 (plan-time verify-before-act) miss — the brief author asserted a gate-acceptance condition without verifying it against the production gate's own test contract (`test_embedding_adequacy.py`). Cross-check every "must pass X" in a plan against the system's existing definition of passing X. Cost: one fix round, absorbed cleanly because the implementer verified rather than transcribed.
- **Adversarial reviewer framing produced the catches.** The two highest-value review outcomes (T6 masked-fixture Critical; G1 fail-open Minor → fixed) came from prompts that named the specific risk to hunt (drive the real producer; does the relaxed gate still have teeth) without pre-judging the verdict. The skill's "never tell the reviewer what not to flag" rule was honored and earned its keep — the opus T6 reviewer surfaced exactly the masked-fixture defect the dispatch asked it to look for.
- **No surface-anchor / framing drift** observed across the dispatches.

---

## § 4 — Session-state checkpoint

- **In-flight / open contracts:** All 8 tasks DONE + both final reviews passed. Remaining final-gate steps when this brief was written: (a) fold this session-review's generalizable findings into `docs/MULTI-AGENT-BUILD-PLAYBOOK.md` Part C; (b) fold untracked `docs/backlog/librarian-committer-samelslug-union-parity.md` into the branch + add the security hardening note to `docs/backlog/librarian-t6-reversal-type-producer-enum.md`; (c) update BUILD.md / ledger; (d) push branch + open PR to main (user merges). Background gate run `by3hk7159` in flight (was ~57% through the suite).
- **Decisions made:** Embedding gate uses the real I2 condition, not `all .passed` (the brief was inaccurate). G1 lint check made fail-closed (None sentinel + returncode check) — a fail-open inside the gate contradicts the gate's purpose, so fixed despite being rated Minor. All ## Minors deferred with triggers (whole-branch review confirmed none blocks merge).
- **Rejected approaches:** (T6) masking the cold-start crash in the test fixture — rejected, fixed production + unmasked. (T6 Step 5) enumerating reversal_types from the gate's own dispatch — rejected as self-referential, switched to producer-side cross-reference.
- **Current system state:** Branch `test/multi-agent-test-harness` @ `1a4f932c`, working tree clean of src/test drift (only watcher-owned index.md/log.md modified + untracked docs). G1 gate end-to-end PASS recorded @ this HEAD: 2485 tests, recall@10 0.926, 0 merge-map regressions, embedding OK, lints at baseline (orphans 758 / schema-drift 191 / broken-wikilinks 1). Nothing on main yet.
- **Next atomic step:** Append the §3 plan-time-verify and the "even the inert-in-production test can be inert" lessons to MULTI-AGENT-BUILD-PLAYBOOK (Part A2 + Part C evidence list), commit the two backlog docs + BUILD.md update, then `git push` the branch and open the PR.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Prompt eng. | Reviewer subagents finish analysis but go idle without sending the verdict to main (×2 this session) | Add an explicit delivery contract to the reviewer dispatch template ("post verdict to main as your final message; do not idle without sending") |
| 2 | Code quality | The inert-in-production test (T6) was itself inert in its first cut — masked the production crash in its fixture | Fold into PLAYBOOK Part A2: "drive the real producer" applies to the meta-gate too; a property test must not satisfy itself from its own fixture or from the unit under test |
| 3 | Prompt eng. | Plan asserted an embedding gate-acceptance condition that contradicted the production I2 contract | PLAYBOOK Part B2: cross-check every "must pass X" in a plan against the system's existing definition of passing X before writing the gate |
| 4 | Code quality | A gate's own lint check failed OPEN (returned 0 on broken subprocess) | Pattern note: verification code must fail CLOSED — can't-verify ≠ pass; rate fail-open-in-a-gate above Minor |
| 5 | Token eff. | Final gate re-runs the full suite G1 already ran at the same HEAD | Accept as pre-PR verification, but run it in the background concurrent with other close-out work (done this session) |
