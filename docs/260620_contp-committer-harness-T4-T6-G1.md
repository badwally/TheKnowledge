# Continuation prompt — Committer + Test Harness: T4 / T6 / G1 + final gate

Paste the block below into a FRESH session (after `/clear`). The first 5 of 8 tasks (D0, D1, M1, T2, T3) are DONE and committed on the branch; this resumes at T4.

---

```
Fresh session. Resume the Production Committer + Multi-Agent Test Harness build on branch test/multi-agent-test-harness (verify `git branch --show-current`; if not on it, `git checkout test/multi-agent-test-harness`). HEAD should be ~7cd303a5 (a docs checkpoint); 5 of 8 tasks are committed and DONE.

FIRST, READ (binding inputs, in order):
1. docs/MULTI-AGENT-BUILD-PLAYBOOK.md — the build discipline (reviewer≠author dispatch, inert-in-production hunt list, file handoffs, gate-tests-what-ships).
2. docs/session-state.md — the top "PRODUCTION COMMITTER + MULTI-AGENT TEST HARNESS" section (state, decisions, next atomic step).
3. .git/sdd/progress.md — the SDD ledger: every task's commit SHAs + verdicts (DONE tasks must NOT be re-dispatched), plus the ## Minors list for final-review triage.
4. docs/plans/2026-06-19-librarian-committer-test-harness-build-plan.md — the plan (task specs).

STATE: D0 (committer: author_deposit + drain_once + run_worker + `wiki commit-worker`, routes deposit + policy-edit + reversal_type intents to the gate), D1 (`wiki demand-cluster`), M1 (pytest markers + --strict-markers + docs/TESTING.md), T2 (integration flows — lifecycle/demand/governance), T3 (N-agent soak) are all DONE, reviewed, fixed, on the branch. Full suite was 2398 passing at T3 close. HEADLINE: T2 surfaced a REAL D0 inert-in-production defect (committer dead-lettered 3 enqueued intent types — policy-edit + contradiction-resolution + depath reversals); we fixed the COMMITTER (`_is_gate_dispatched()` classifier, commit 2b5729b9), not the test. Security re-check SHIP IT (MEDIUM-2 = privilege-at-enqueue-only, accepted as documented Phase-5 model).

REMAINING — 3 tasks, run via subagent-driven-development (one implementer at a time; per-task brief at .git/sdd/task-<T>-brief.md already exists; review-package + task-brief scripts in the superpowers/subagent-driven-development skill dir):
- T4 surface E2E (sonnet impl + sonnet review): MCP read-tier allowlist EXACT-set + build-only tools ABSENT + deposit round-trip; CLI E2E (`cli.main([...])`) against a real git repo asserting on-disk + git state for remediate/revert-resolution/policy-edit/demand-cluster/commit-worker. Brief: .git/sdd/task-T4-brief.md.
- T6 inert-in-production property tests (sonnet impl + OPUS review — this is the meta-gate): parametrized invariants — every lint check + detector fires on a real signal; every gate dead-letters a real bad input; EVERY enqueued intent type has a committer apply-branch (the policy-edit/reversal routing fixed in D0-reopen — make it an executable invariant); EVERY consumer's data source has a producer; no apply-branch-less intent type. If a real gap is found, FAIL/xfail + file backlog — do NOT delete the assertion. Brief: .git/sdd/task-T6-brief.md.
- G1 pre-merge gate script (sonnet impl + sonnet review): full suite + new tiers + eval floors (retrieval_eval fts recall@10 ≥ 0.90 [baseline 0.926]; merge_map_eval no regressions; embedding_eval.evaluate_all all pass) + scoped lints; wire to a script; document in playbook + CLAUDE.md. Brief: .git/sdd/task-G1-brief.md.

PER TASK: record base SHA → dispatch implementer (sonnet) with the brief file + scene-setting + report path → on DONE generate review-package(BASE,HEAD) → dispatch reviewer (opus for T6, sonnet for T4/G1) → fix loop (re-review after every fix) → mark complete in .git/sdd/progress.md. Keep the coordinator window lean (file handoffs, not pasted text); checkpoint session-state at each task close.

HARD RULES: .venv/bin/python + .venv/bin/wiki ONLY. Guard `git branch --show-current`==test/multi-agent-test-harness before EVERY commit; NEVER `git add -A`/`-u`; never stage watcher-owned index.md/log.md/.knowledge/. Scoped lints only (orphans/schema-drift/broken-wikilinks — never unscoped, it hangs ~1h28m). Don't wrap fast commands in timeout (absent on darwin).

FINAL GATE (after T4/T6/G1 all Approved): (1) whole-branch opus review (review-package merge-base→HEAD) + (2) independent security review (committer now applies privileged ops autonomously — verify the boundary) + (3) /session-review → fold generalizable findings into MULTI-AGENT-BUILD-PLAYBOOK Part C → (4) fold untracked backlog docs into the branch (docs/backlog/librarian-committer-samelslug-union-parity.md) → (5) update BUILD.md / ledger → (6) push branch + PR to main (the user merges). A failing eval OR review HALTS.

OPEN MINORS to carry into final-review triage (in .git/sdd/progress.md ## Minors): D0 NEW-1/NEW-3 (same-slug union body-parity → docs/backlog/librarian-committer-samelslug-union-parity.md); D0 NEW-1 DRY (disposition-mapping duplicated across drain_once branches — /simplify candidate); M1 TESTING.md:55 stale eval path; T2 M3 (provenance hand-seed producer↔consumer); T3 concurrent-same-slug-race coverage (add when T6/soak touches test_soak.py); MEDIUM-2 security trust-property (folded into daemon backlog). Daemon stays on-demand only (launchd deferred → docs/backlog/librarian-committer-daemon-install.md, Option B scheduler-cron preferred).
```

---

## State at handoff (for the human)
- Branch `test/multi-agent-test-harness`, HEAD `7cd303a5`. 5/8 tasks DONE + committed; full suite 2398 green at T3 close.
- Commits: D0 `3f7762eb`+`a5149421`, D1 `6b020a74`+`599130c2`+`5094831c`, M1 `08b481ff`, T2/D0-reopen `80ba33bb`+`2b5729b9`, T3 `741b04aa`+`2c62417c`, plus docs checkpoints.
- Nothing on main yet; merge is the user's call (push-branch + PR).
- Untracked: `docs/260618_librarian-rag-design-session-brief.md` (pre-existing, not this build), `docs/backlog/librarian-committer-samelslug-union-parity.md` (fold into branch).
