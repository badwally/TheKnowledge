# Session review — Test-Harness Expansion build (2026-06-20)

Scope: subagent-driven execution of the 6-task test-harness expansion (PR #38, merged `485427ad`) + the playbook B2 follow-up (PR #39, merged `02c73ca9`). Baseline full suite **2491** → final **≈2534** (+43; ±1 from the order-dependent `test_doc5_rotate_log` flaky, unrelated to this build). All 6 tasks reviewed (opus on P1/P2/P3/P6, sonnet on P4/P5), 3 fix rounds, whole-branch opus review READY TO MERGE, P6 security SHIP IT (0 HIGH), exit gate green (recall@10 0.926, merge-map 0 regressions, embedding OK, lints 758/191/1).

This review is read-only with respect to the work; it records findings and a resume checkpoint. The verbatim per-task review transcripts lived in the worktree's `.git/.../sdd/` and were discarded on worktree removal — their substance is preserved in `docs/session-state.md` and below.

---

## § 1 — Code and coding quality

**1.1 — High (correctness, deferred): two real production lint-registry defects surfaced but not fixed.**
`src/gateway/ops/lint.py` registers checks under slugs `citation-chains` and `long-slugs`, but those modules emit findings under different `check=` names (`dangling-synthesizes-ref`/`aggregate-framing-without-synthesizes`; `slug-too-long`). A production `wiki lint --scope citation-chains` consumer that filters on the registered slug silently gets nothing. Backlogged (`docs/backlog/librarian-citation-chains-slug-mismatch.md`, `…-long-slugs-slug-mismatch.md`) because the fix is a registry-wiring change touching `LINT_BASELINES`, out of P2's test-only scope. Correctly deferred, but these are real bugs — highest-value follow-up. They were masked for the whole prior committer/test-harness build by empty-repo negative controls; the P2 meta-gate is what exposed them.

**1.2 — Medium (test coverage, documented limitation): P3 outcome-B never exercised.**
`tests/integration/test_soak.py` S7 deterministically produces outcome A (one committed + one dead-lettered) under the 3 concurrent drainers; the union outcome B branch of the assertion is present but never taken (S5 covers union separately). Acceptable — both branches are asserted and S5 carries the union case — but the assertion has an untested branch. Documented in the docstring.

**1.3 — Low (test coverage): P4 outcome-A loser claim-text not asserted on-page.**
`tests/gateway/test_property_invariants.py` property 3 and `test_soak.py` S7 assert the loser's *disposition* (non-empty dead-letter record) but not its claim *text* — correct semantics (a CAS-rejected write is correctly absent from the page; the durable dead-letter is the survival evidence), but worth the explicit note the implementer already added.

**1.4 — Low (convention, resolved in-session): P6 emit duplication.**
The trace emit was duplicated byte-identically across `run_worker`'s once/loop branches; DRY'd into a local helper in the fix-wave (`committer.py`). No residue.

What was checked and is clean: no monkeypatching of any unit under test (verified by every reviewer); plain-class stubs over MagicMock (P2 `_StubClient`); live-registry-derived guards (P2); real producers driven end-to-end (P1 MCP protocol, P3 real fcntl locks, P4 real IntentQueue, P6 real DrainResult).

---

## § 2 — Token efficiency

**2.1 — Retry loop: worktree venv parity discovered after a failed commit (~3 excess calls + 1 failed commit).**
Sequence: `python -m venv` → `pip install -e .[dev]` → first commit BLOCKED by the pre-commit `wiki lint` hook with `ModuleNotFoundError: numpy` (numpy is imported by `embedding_index.py` but not a declared dependency) → diff `pip freeze` main-vs-worktree → install main's full 173-pkg freeze → retry commit. The precondition was knowable up front: a project whose runtime imports exceed its declared `dependencies` will not run from `.[dev]` alone. Replicating the parent venv's `pip freeze` *before* the first commit attempt would have skipped the failed-commit round. Generalizable — folds into the playbook (below).

**2.2 — Redundant gate run: ran the pre-merge gate twice (~1 excess full gate, several minutes).**
Ran a pre-flight gate on `ec09c1b8` (concurrent with the whole-branch review — good parallelism) AND the binding gate on `3c2a44a7` after the fix-wave. Since the fix-wave was already triaged as "all defer-safe Minors" and certain to run, the pre-flight gate was a de-risk that the binding run repeated. Could have deferred the single gate run to after the fix-wave. Mild — the parallelism partly justified it (it overlapped review wait-time), but it was strictly one extra full gate.

**2.3 — Over-install: the worktree venv pulled the heavy `whisper` extra (torch/mlx/lightning) it never needed.**
Copying main's full freeze (2.1's fix) installed ~96 packages including the whisper ML stack, none exercised by the test suite. Faster than per-failure discovery, but a leaner parity set (numpy + the actually-imported transitive deps) would have sufficed. Acceptable trade (pip cache made it fast); noted for completeness.

What was efficient: file-based subagent handoffs (briefs/reports/review-packages as files, never pasted) kept the coordinator window lean across 6 tasks + 3 fix rounds + 4 reviews; verifying the P4 "2410" miscount myself (full-suite run → real 2526) was a justified check that caught a reporting discrepancy, not waste.

---

## § 3 — Prompt and context engineering

**3.1 — Context seeding (the session's one plan defect, already remediated): P3 brief carried a drain mechanism that can't produce the contention the test targets.**
The P3 brief's Step 1 said "fire concurrently via the real queue + `run_worker`"; `run_worker(once=True)` is a single-threaded sequential drainer, so the same-slug race serialized and the CAS-contradiction path was unreachable. Caught by the opus reviewer *instrumenting the outcome distribution*, not by reading the test green. Already folded into playbook B2 (PR #39). The generative lesson: when a dispatch hands an implementer a mechanism for a concurrency test, verify at brief-authoring time that the mechanism produces the contention — the higher-priority Global Constraint governs an inconsistent step.

**3.2 — Delivery contract not always honored on fix dispatches.**
Despite every dispatch carrying "post your verdict as your final message; do not go idle," `fix-P2` went idle without posting its status, costing one `SendMessage` round-trip to extract a result that already existed. The B4 reviewer-delivery-contract instruction is necessary but not sufficient for fix subagents. Low — the round-trip is cheap and the harness re-prompt is the backstop — but worth knowing the instruction has a non-zero miss rate.

**3.3 — Tooling/prompt mismatch: the `task-brief` script assumes numeric task IDs.**
`scripts/task-brief PLAN_FILE N` matches `^#+\s+Task\s+[0-9]+`; this plan used alpha-prefixed IDs (`Task P1`), so the script errored and the briefs were extracted with an inline awk workaround. Minor; either the SDD script should accept alphanumeric IDs or plans should use numeric task headers.

What was well-engineered: model selection matched task difficulty (sonnet implementers, opus for concurrency/governance/keystone + security reviews) per the plan; the independent-review gate ran adversarially (each reviewer ran the tests + mutations, not just diff-reading) and BLOCKed 3 of 3 non-trivial tasks for genuine inertness — the highest-leverage practice, paying off again; subagent prompts copied binding constraints verbatim and never pre-judged findings.

---

## § 4 — Session-state checkpoint

- **In-flight / open contracts:** None for this build — PR #38 + #39 both MERGED to `main` (`02c73ca9`). Local `main` pulled and level with origin. This documentation branch (`docs/test-harness-expansion-writeup`) holds the session-review + BUILD.md section, pending its own PR.
- **Decisions made:**
  - Worktree got its own venv (editable install resolves `gateway` to worktree src) so P6's source edits were testable in isolation — main's venv points at main's src.
  - All 6 Minors triaged defer-safe by the whole-branch review; 4 mechanical ones cleaned in one fix-wave commit, 2 (P6 test-13, P6 LOW title-reflection) left as no-action.
  - 2 slug-mismatch lint defects + 4 LLM-coverage notes backlogged, not fixed (out of test-only scope).
- **Rejected approaches:** `run_worker(once=True)` for the P3 contention test (serializes the race → concurrent `drain_once` drainers). Using main's venv from the worktree (editable points at main's src).
- **Current system state:** `main` @ `02c73ca9` — full build merged, exit gate green (suite ≈2534, recall@10 0.926, merge-map 0 regressions, embedding OK, lints 758/191/1). Worktree removed; both merged branches deleted. `hypothesis>=6.0` now in the `[dev]` extra. `scripts/pre-push` exists but is NOT installed (manual symlink, by design).
- **Next atomic step:** Open the PR for this `docs/test-harness-expansion-writeup` branch (session-review + BUILD.md section). After merge, the open follow-up is the 2 lint slug-mismatch registry fixes (their backlog docs name the trigger).

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Code (§1.1) | Two real lint-registry slug-mismatch bugs surfaced + backlogged | Fix the registry/emitted-slug mismatch (touches `LINT_BASELINES`) — highest-value, real production correctness |
| 2 | Prompt (§3.1) | Plan named a drain mechanism that can't produce the tested contention | DONE — folded into playbook B2 (PR #39); apply the check at brief-authoring for future concurrency tasks |
| 3 | Token (§2.1) | Worktree venv failed first commit on missing transitive dep (numpy) | Fold "replicate parent `pip freeze` before first commit when imports exceed declared deps" into the playbook setup notes |
| 4 | Token (§2.2) | Pre-merge gate run twice (pre-flight + binding) when a fix-wave was certain | Sequence fix-wave before the single binding gate when remaining work is already triaged |
| 5 | Prompt (§3.3) | `task-brief` script breaks on alpha-prefixed task IDs (`P1`) | Accept alphanumeric IDs in the SDD script, or use numeric task headers in plans |
