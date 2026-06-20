# Session state — 2026-06-17

Last updated: 2026-06-20 (AS-BUILT REVIEW FOLLOW-UPS in flight. Merged this session: PR #41 lint-slug-mismatch, #42 dev-deps note, #43 e2e-challenge-cases. Open: PR #44 committer-drain-determinism; branch `chore/gate-tests-what-ships` (3-item gate hardening, stacked on #44).)

---

## 🔧 AS-BUILT REVIEW FOLLOW-UPS (IN FLIGHT 2026-06-20)

Driven by `docs/260620_librarian-rag-as-built-review.md`. Reviewed it, verified its one live finding, fixed it, then took the 3 gate-design weaknesses it surfaced.

### Open contracts
- **PR #44 `fix/committer-drain-determinism` (OPEN, gate-green @ 2535):** the flaky merge-direction
  test. Root cause was NOT the review's "timestamp in intent id" (it's a pure content hash) — it was
  `IntentQueue.claim()` sorting by mtime alone, ties → nondeterministic `os.scandir` order. Fix:
  `(mtime, name)` total order + RED-first unit test + direction-agnostic committer assertion. 20/20
  unpinned, all pinned seeds pass.
- **Branch `chore/gate-tests-what-ships` (stacked on #44), 3 items — gate now green:**
  - **#1 live entity-recall guard** — `test_lifecycle_flow.py` 2 new tests drive the REAL EmbeddingIndex
    → `_dedup_recheck` → adjudicate on the alias-merge; explicit distance floor (live 0.276, RED at ~1.0)
    + disjoint negative control (0.955). Teeth-verified. Finding: the merge-map golden RECORDS distances
    the live encoder doesn't produce (brand/generic 1.0 vs 0.276; link 0.12 vs 1.0) → backlog
    `docs/backlog/librarian-merge-map-golden-live-fidelity.md`.
  - **#2 concurrency repetition** — new `concurrency` pytest marker on 5 order/contention tests; gate
    `step_concurrency_repeat` re-runs `-m concurrency` ×5 (CONCURRENCY_REPEAT=5, ~3s); RED-first unit
    tests in `test_gate_script.py`. A 1/3 flake now clears the gate at ~0.4%, not 33%.
  - **#3 read-tier carry-forward E2E** — `test_mcp_surface.py` 2 new e2e: deposit via build mount →
    run_worker → read own write THROUGH `build_read_tier_server().call_tool("wiki_retrieve")` (the
    contract the deterministic harness substitutes for) + pre-drain negative control; boundary test
    proves the read mount rejects `wiki_deposit` (isError, enqueues nothing). Confirmed the write
    boundary HOLDS (not a defect — initial test logic was wrong).

### Files mid-edit
- None. All edits complete; gate re-run finishing. Then commit `chore/gate-tests-what-ships` (base the
  PR on `fix/committer-drain-determinism` — stacked; GitHub auto-retargets to main when #44 merges).

### Decisions made this session
- Drain determinism via `(mtime, name)` tiebreak (user chose "claim() tiebreak + test" over test-only/
  semantic-rule). Lowest-risk; only ADDS order where there was a nondeterministic tie.
- #3 scoped to an AUTOMATED e2e (user chose) — no production-wiki mutation; runs in seeded temp root.
- #1 guards the alias-merge RECALL path live (faithful, distance 0.276); the `link` path has no
  faithful live case on the lexical encoder (disjoint surfaces score 1.0) → documented, not forced.

### Rejected approaches this session
- Review's stated root cause (timestamp in content-addressed intent id) — wrong; corrected to mtime-tie.
- Re-recording / live-driving the merge-map golden distances now — touches a gate floor; deferred to
  the backlog doc (trigger: next golden touch or neural-encoder swap).
- Repeating the SLOW soak tests ×5 — instead marked the fast order-sensitive subset (~1.5s) for cheap
  repetition; the soak tests already stress contention in a single run.

### Next atomic step
Confirm gate exit 0, commit the 3-item work on `chore/gate-tests-what-ships`, push, open PR (base
`fix/committer-drain-determinism`). User merges #44 then this. No production-wiki writes occurred.

---

## 🔧 LINT-REGISTRY SLUG-MISMATCH FIX (IN FLIGHT 2026-06-20)

**Branch:** `fix/lint-registry-slug-mismatch` (off main `c22b8bb1`). Closes the two
production bugs backlogged from P2: lint checks registered under a slug they don't emit,
so a `wiki lint --scope <slug>` consumer filtering on the registered slug got nothing.

### Open contracts
- **Direction decided:** rename the emitted `check=` to match the registered slug for BOTH
  checks (preserves public `--scope citation-chains`/`long-slugs` names; the only single-slug
  option for citation-chains short of a split, which the brief excluded).
- **citation_chains.py** — both findings now emit `check="citation-chains"`; dangling-vs-
  aggregate sub-type preserved in `metadata["kind"]`. **long_slugs.py** — emits `check="long-slugs"`.
- **Tests (TDD RED→GREEN):** updated `test_inert_invariants.py` (2 positive tests, comments
  removed), `test_lint_citation_chains.py` (filter on slug + metadata kind), `test_validator.py:355`.
  The `assert f.check == slug` tripwire (`test_inert_invariants.py:~194`) now holds for both slugs.
- **Verified live:** `--scope citation-chains` → 28 findings under `## citation-chains`;
  `--scope long-slugs` → 50 under `## long-slugs` (== historical M96 count). No `LINT_BASELINES`
  change (citation-chains/long-slugs are not gate baselines; orphans/schema-drift/broken-wikilinks
  unchanged). Both backlog docs marked RESOLVED.
- **Gate PASSED** @ commit `f83dfc3e`: 2534 passed; recall@10 0.926; merge-map 0 regressions;
  embedding OK; scoped lints at baseline (758/191/1). First run failed at Step 1 — main's `.venv`
  lacked `hypothesis` (declared `[dev]` dep added by merged P4, never synced into this checkout);
  installed `hypothesis>=6.0` and re-ran green. (Heads-up: any FRESH main checkout needs
  `pip install -e '.[dev]'` before the gate's full suite can collect `test_property_invariants.py`.)
- **PR #41 OPEN** (https://github.com/badwally/TheKnowledge/pull/41) — awaiting user merge.

### Files mid-edit
- None. All work shipped in PR #41 (commit `f83dfc3e`); awaiting user merge.

### Decisions made this session
- Rename emitted→registered (not registry→emitted, not split). Preserves public scope names;
  lowest blast radius. Sub-type kept in `metadata["kind"]` so no information lost in the collapse.
- Also fixes a latent report inconsistency: `_write_report` summary was keyed by registry slug
  but detail sections by emitted `f.check` — now both agree.

### Rejected approaches this session
- Option-2 split (two registrations for citation-chains): excluded by the brief's two-direction
  framing; would change the public `--scope` name and require splitting `run()`.
- Touching validator.py's `slug-too-long` ValidationError rule: separate subsystem, left as-is.

### Next atomic step
NONE on my side — PR #41 is open and gate-green; user merges. After merge, both backlog docs are
RESOLVED and no follow-up is triggered. (If a fresh main checkout is used next, run
`pip install -e '.[dev]'` so the gate's full suite can collect the hypothesis-dependent tests.)

---

## ✅ TEST-HARNESS EXPANSION (MERGED 2026-06-20)

**MERGED to `main` @ `02c73ca9`** (PR #38 build `485427ad`; PR #39 playbook B2 `02c73ca9`). Worktree REMOVED; both merged branches deleted; local main pulled level. Plan: `docs/plans/2026-06-20-test-harness-expansion-build-plan.md`. Mode was subagent-driven-development, one implementer at a time, opus review on P1/P2/P3/P6 + sonnet on P4/P5. NOTE: the per-task SDD ledger lived in the worktree's `.git/.../sdd/` and was discarded on worktree removal — the per-task summary below + `docs/260620_session-review.md` are the durable record.

### Open contracts
- **Baseline:** full suite **2491 passed** @ `1fae97da` (fresh, not hardcoded). chore `1fae97da` = gitignore .claude/worktrees/.
- **P1 (e2e deposit→commit→read) — DONE.** Commit `3e048e53`. Opus Approved (A+B PASS; 3 mutations confirmed RED→GREEN). Suite 2493.
- **P2 (T6 32/32 positive lint coverage) — DONE.** Commits `f02fe244`..`22f33f08` (review clean after 1 fix round). Opus BLOCKed round-1 (4 LLM checks lazily xfailed despite injectable `run(client=)` seam); fix wired plain-class `_StubClient` driving all 4 real producers, 0 xfail; re-review Approved. Suite 2521. 2 real production defects backlogged (citation-chains/long-slugs registry-slug-vs-emitted mismatch — meta-gate working).
- **P3 (concurrent same-slug race in soak) — DONE.** Commits `755579da`..`341013d2` (review clean after 1 fix round). Opus BLOCKed round-1 (single-threaded `run_worker` serialized the race — Critical); fix = 3 concurrent `drain_once` drainers (mirror S1), genuine CAS contention; re-review Approved (20-trial probe confirmed `contradictory-edit` dead-letter under real contention). Suite 2523.
- **P4 (Hypothesis property tests) — DONE.** Commits `39f15b9f`..`2176a719` (review clean after 1 fix round). `hypothesis>=6.0` in `[dev]`. Sonnet Approved-with-Important round-1 (property 3 disguised parametrize, 5 examples); fix widened to titles×n_rounds → 150 genuine examples; re-review Approved (per-intent-id fencing invariant faithful — implementer's source pushback correct). Coordinator-verified full suite **2526**.
- **P5 (pre-push gate hook) — DONE.** Commit `61f40400`. `scripts/pre-push` propagates gate exit (set -euo pipefail + terminal eval); 5 tests both directions + teeth-verified inert-hook negative control via GATE_CMD stub; docs in CLAUDE.md + playbook B6. Sonnet Approved (1 Minor → fix-wave).
- **P6 (commit-worker trace mode — privileged committer, ONLY prod-code task) — DONE.** Commit `ec09c1b8`. `run_worker` gains `sink=None`; emits per-intent `DrainResult` trace (intent_id/disposition/reason) at the previously-discarded site; `drain_once` byte-unchanged; CLI `commit-worker --verbose`. Opus Approved (mutation-confirmed default-off byte-identical + real-reason-from-DrainResult). Security **SHIP IT 0 HIGH** (pure observability, privilege boundary unchanged, ephemeral stdout, body never leaks; 1 LOW theoretical no-action). Suite 2533.
- **ALL 6 TASKS DONE + MERGED.** Whole-branch opus review READY TO MERGE; fix-wave `3c2a44a7` cleaned 4 defer-safe Minors; binding exit gate PASSED on `3c2a44a7` (suite ≈2534, recall@10 0.926, merge-map 0 regressions, embedding OK, lints 758/191/1). Merged via PR #38 (`485427ad`). Playbook B2 lesson + Evidence folded via PR #39 (`02c73ca9`). `docs/260620_session-review.md` written.

### Files mid-edit
- None for the build. In flight: `docs/test-harness-expansion-writeup` branch (this session-state refresh + `docs/260620_session-review.md` + BUILD.md delivery section + playbook B5 venv-parity note), pending its own PR.

### Decisions made this session
- Worktree gets its OWN venv (editable install resolves `gateway` to worktree src) so P6's source edits are testable in isolation — main's venv points at main's src.
- Backlog-not-fix for P2's 2 slug-mismatch defects + 4 LLM-dependent checks (production lint changes are out of P2's test-only scope).

### Rejected approaches this session
- Using main's venv from the worktree (rejected): its editable install points at main's src, so P6's source edits would be invisible — built a dedicated worktree venv instead.
- run_worker(once=True) for the P3 same-slug contention test (rejected, was the BLOCKed round-1): single-threaded sequential drain serializes the race; replaced with concurrent drain_once drainers (the brief's Step-1 wording was the plan defect — higher-bar Global Constraint governs).

### Plan defects (for session-review / playbook B2)
- P3 brief Step 1 said "via run_worker" — internally inconsistent with the plan's own "drive the REAL producer, not serialized" bar. run_worker is a single-threaded drainer; same-slug intents never contend. Caught by opus review instrumenting the outcome distribution. Lesson: when a plan step names a drain mechanism, verify it actually produces the contention the task is testing.

### Next atomic step
Open the PR for `docs/test-harness-expansion-writeup` (session-review + BUILD.md delivery section + playbook B5 venv-parity note). After merge, the one open follow-up is the 2 lint slug-mismatch registry fixes (`docs/backlog/librarian-citation-chains-slug-mismatch.md`, `…-long-slugs-slug-mismatch.md`) — real production bugs touching `LINT_BASELINES`; act when their trigger fires. P2 LLM-coverage note also open under docs/backlog/.

---

## 🔨 PRODUCTION COMMITTER + MULTI-AGENT TEST HARNESS (IN PROGRESS, 2026-06-19)

**Branch:** `test/multi-agent-test-harness` (cut off main @ `0a688378`; HEAD pre-build was `bd6e5f1e` contp doc). Plan: `docs/plans/2026-06-19-librarian-committer-test-harness-build-plan.md`. Contp: `docs/260619_contp-multi-agent-test-harness.md`. SDD ledger: `.git/sdd/progress.md` (per-task briefs/reports/diffs under `.git/sdd/`). Playbook binding: `docs/MULTI-AGENT-BUILD-PLAYBOOK.md`.

**Objective:** close the keystone gap (async deposit→commit has NO production drainer) by building the REAL committer (Option 2, ratified — NOT a simulator) + a 6-tier test harness driving the real system. 8 tasks: D0 committer, D1 demand-cluster CLI, M1 pytest markers, T2 integration flows, T3 N-agent soak, T4 surface E2E, T6 inert-in-production property tests, G1 pre-merge gate script.

### Open contracts
- **D0 (KEYSTONE) — DONE.** Build `3f7762eb` + fix `a5149421`. Opus review found 2 Critical (crash-reclaim inert in prod; dedup/merge inert in prod CLI — `CommitGate(embedding_index=None)`) + 2 Important (same-slug silent-overwrite; retry-later strand) + 2 Minor (entity_kind="drug" leak; empty-slug dotfile) + security LOW-1 (`_rel_escapes_root`) — ALL FIXED; re-review **Approved**; sec-D0 **SHIP IT** (0 HIGH). Full suite 2285. 3 fail-safe re-review Minors → backlog (NEW-1/NEW-3 union-parity; NEW-2 retry-later direct-test routed to T3 soak coverage).
- **D1 (demand-cluster CLI) — DONE.** Build `6b020a74` + fix `599130c2` (Critical: inert `--trigger` gate — `cluster()` always auto-submits, no dry-run; redesigned trigger=False=report-only no-op / trigger=True submits to correctly-rooted queue) + help-fix `5094831c`. Re-review Approved. MCP-tool build-tier adjudicated correct (== remediate).
- **M1 (pytest markers) — DONE.** Commit `08b481ff`. 4 markers + `--strict-markers` + `docs/TESTING.md`; split verified (2377/2375). Approved (1 Minor: stale doc path TESTING.md:55).
- **T2 (integration flows) + D0 reopen — DONE.** Commit `80ba33bb` (T2 build) + `2b5729b9` (D0 routing fix + T2 un-mask). Opus review confirmed real D0 inert-in-production defect (policy-edit, reversal_type, depath intents all enqueued but dead-lettered by author_deposit). Fixed in committer.py: `_is_gate_dispatched()` classifier routes non-deposit gate-dispatched intents to `gate.commit(AuthoredIntent(writes={}))` bypassing `author_deposit`. Principal flow confirmed safe (server-side principal stamped at enqueue, not re-resolved at drain). Governance tests rewritten to drive `run_worker(once=True)`. Lifecycle: renamed same-slug test + added cross-slug dedup-merge asserting `disposition=="merged"` exactly (I1). Demand: tightened centroid-slug assertion (M1). Full suite 2392. T2 = complete.
- **T3 (N-agent soak) — DONE.** Build `741b04aa` + fix `2c62417c`. 6 soak tests on real fcntl locks: all-terminal/no-torn-write, stale-fencing-reject, backpressure@MAX_BACKLOG=256, retry-later re-queue (closes D0 retry-later coverage gap), write-skew both-survive. S5 under-assertion fixed (deterministic both-survive via real `_union_same_slug`, RED-on-drop verified); M2 real-validator caught a latent test-payload bug. Re-review **Approved**. Full suite 2398 (coordinator-confirmed green). 1 non-blocking Minor backlogged (concurrent same-slug-race coverage — see ledger ## Minors).
- **T4 (surface E2E) — DONE.** Build `d1729739` + fix `9b7c4e07` (commits `8b19bf3a..9b7c4e07`). 9 e2e tests (`tests/e2e/test_mcp_surface.py` + `test_cli_surface.py`). Step1 exact-set `==` on `read_tier_tool_names()` (read=11 vs build=60) + negative control (build server HAS wiki_deposit/wiki_remediate). Step2 MCP deposit round-trip COMMITS (call_tool→run_worker(once)→disk+git+Intent-Id trailer). Step3 CLI E2E all 5 cmds assert disk+git state. Sonnet review: Spec ✅ Approved, 0 Critical; 1 Important (disjunctive git assertion → FIXED to Intent-Id trailer match) + 2 Minors (import hoisted; tmp_path Minor → ledger). Adjacent 19 green.
- **T6 (inert-in-production property tests, meta-gate) — DONE.** Build `5f67eb08` + fix `a4c3d785` (commits `9b7c4e07..a4c3d785`). Opus review 1 Critical + 1 Important — both FIXED + opus re-review **APPROVED** with adversarial RED-on-revert evidence. **HEADLINE: the meta-gate surfaced + fixed a REAL production crash** — `superseded_citations.run()` FileNotFoundError on missing `raw/` (cold-start), only 1 of 32 lint checks unguarded → PRODUCTION guard added (`superseded_citations.py:18-20`) + fixture unmasked. Step 5 hunt-#1 invariant was self-referential → rewritten to cross-ref PRODUCER ops vs gate dispatch (teeth proven: inject fake reversal_type → RED). reverse-merge/restore-depath gate-internal → `docs/backlog/librarian-t6-reversal-type-producer-enum.md`. Integration 54 pass; lint subset 131 pass.
- **G1 (pre-merge gate script) — DONE.** Build `4457f72a` + fix `1a4f932c` (commits `a4c3d785..1a4f932c`). `src/gateway/scripts/gate.py` — 6 fail-fast checks (full suite / fast tiers / recall@10≥0.90 / merge-map no-regress / embedding I2 / scoped lints vs baseline). End-to-end PASS: 2485 tests, recall 0.926. Documented in PLAYBOOK B6 + CLAUDE.md. Sonnet review Spec ✅ 0 Critical/Important; embedding deviation (`all .passed` → real I2 `passed OR valid-falsifiable-fallback`) adjudicated LEGITIMATE + teeth-retaining; 1 Minor (lint fail-OPEN) → FIXED fail-closed (None sentinel + returncode check). 30 unit tests green.
- **ALL 8 TASKS DONE + FINAL GATE PASSED.** Whole-branch opus review **READY TO MERGE** (cross-task coherence verified; all ## Minors triaged → DEFER, none mislabeled). Independent security review **SHIP IT, 0 HIGH** (autonomous-apply boundary sound; enqueue-only model intact; 1 deferred hardening note folded into T6 reversal-type backlog). /session-review → `docs/260619_session-review-3.md`; generalizable findings folded into PLAYBOOK (hunt-#7, meta-gate-can-be-inert, B2 gate-pass-condition cross-check, B4 reviewer-delivery-contract). Pre-merge gate **PASS @ `c59cb0d1`**: 2491 passed, recall@10 0.926, 0 merge-map regressions, embedding OK, lints baseline. A pre-existing flaky negative-control (`test_nonatomic_rebuild_exposes_half_state`, untouched Phase-2 code, ~4/5 fail in isolation) that intermittently reddened the gate was made DETERMINISTIC (external-reader-samples-after-each-upsert, 0/20 fail) — `c59cb0d1`. BUILD.md § 24 updated. **Remaining: commit the doc bundle (PLAYBOOK + BUILD.md + T6 backlog note + session-state + session-review-3) → push branch → open PR to main (user merges).**
- G1 — NOT STARTED.

### Files mid-edit
- None. D0+D1 commits clean. Untracked (fold into branch at a checkpoint): `docs/backlog/librarian-committer-samelslug-union-parity.md`. (Plan + daemon-backlog already committed at `aeda02a5`.) `.git/sdd/` briefs/reports/reviews/diffs are git-internal (not tracked).

### Decisions made this session
- Committer ships **on-demand only** (`wiki commit-worker --once`/`--loop`); launchd daemon deferred → `docs/backlog/librarian-committer-daemon-install.md`. **Option B (scheduler-cron `wiki schedule add ... commit-worker --once`) preferred over a launchd daemon when revived** — bounded drain, no standing unattended git-committer on a shared branch-switching tree. Revival trigger: security clears the committer surface AND a dedicated-checkout/branch-pin story exists.
- `author_deposit` is the THIN renderer (body verbatim, frontmatter mirrors `_authored_entity`). Richer page-type rendering = triggered backlog.
- **Same-slug deposit (two deposits → same slug): UNION into the existing page** (user decision) — no silent overwrite. Shipped as `_union_same_slug` (net-new bullet union; dead-letters needs-manual-merge on non-bullet structural change — fail-safe, no data loss). Full cross-slug parity deferred → `docs/backlog/librarian-committer-samelslug-union-parity.md`.
- Reviews: opus on every concurrency/destructive/governance task + background security review on the privileged committer surface. Sonnet implementers + sonnet review on additive tasks.

### Rejected approaches this session
- **Test-reference simulator (Option 1)** — rejected by user ratification: testing a simulator while production lacks the drainer = the inert-in-production trap this exercise exists to kill.
- **Launchd always-on committer daemon now** — rejected: unattended git-committer on a working tree shared with branch-switching sessions could land commits on the wrong branch; brand-new privileged code shouldn't run unattended before baking. (Watcher is immune — untracked writes only; committer is not.)

### Next atomic step
**6 of 8 tasks complete (D0,D1,M1,T2,T3,T4). T6 IN FLIGHT (implementer dispatched, opus review pending). Remaining after T6: G1 + final gate.** T6 base `9b7c4e07`, brief `.git/sdd/task-T6-brief.md` — encodes the inert-in-production hunt list as executable invariants over real registries (every lint check / detector / gate branch / intent type fires/dead-letters on real signal; every consumer has a producer). OPUS review (meta-gate): confirm each case drives the REAL producer (not a fabricated fixture) and step4/5 enumerate the real registry, not a stale hardcoded list. If a real gap surfaces → backlog doc + xfail, don't delete the assertion. Then G1 (pre-merge gate script: full suite + eval floors recall@10≥0.90 + merge-map no-regress + embedding gates + scoped lints, sonnet impl + sonnet review; base = HEAD after T6). One implementer at a time (shared tree). Final gate: whole-branch opus review + independent security review (committer applies privileged ops autonomously) + /session-review → fold findings into MULTI-AGENT-BUILD-PLAYBOOK Part C → fold `docs/backlog/librarian-committer-samelslug-union-parity.md` into branch → update BUILD.md/ledger → push branch + PR to main (user merges). Open Minors for final-review triage: `.git/sdd/progress.md` ## Minors. A failing eval OR review HALTS.

---

## 🔨 LIBRARIAN PHASE 5 — LIFECYCLE & DEMAND GOVERNANCE (IN PROGRESS, 2026-06-19)

**Branch:** `docs/librarian-phase5` (cut off post-#30 `main` @ `a4450eee` base; HEAD includes the unpushed `dbf4888b` session-state commit that rides into Phase 5's PR per Phase-3 precedent). Plan: `docs/plans/2026-06-19-librarian-phase5-build-plan.md`. Ledger: `docs/plans/2026-06-18-librarian-multi-agent-rag-checkpoints.md` §4 Phase 5. SDD progress ledger: `.git/sdd/progress.md` (per-task SHAs + Minors).

**Execution mode:** subagent-driven-development — fresh implementer per task (sonnet) + independent task review (opus on destructive/subtle tasks) + fix loop, coordinator window kept lean. Per-task briefs/reports/diffs handed off as files under `.git/sdd/`.

### Open contracts
- **6-task build** (scope expanded from 4 → 6 by the 2026-06-19 scope decision, committed `a4450eee`): T1 retraction/reversal (G1/G3/G4/G8) ✅ `1b9ac9bd..80246a96`; T2 remediation+conservation (G6/F1) ✅ `c3fd4a12..1ddd99a6`; T3 gap-routing+keep-worthiness (dec10/A4) ✅ `b47722f1..d6a0a3c2`; T4 DemandLedger+preflight (dec11/12/I4) ✅ `38c8a548..9927a3c8`; T5 reversal/anomaly detectors (G2) ✅ `11dfd554..1419c7ae`; T6 policy-edit privileged-intent path + merge-map golden gate (G7/I3) — build+per-task-review clean `2f708f7f..a9889614` (6 fix rounds: security HIGHs, 2 inertness Criticals, version-bump, malformed-dedup fail-open).
- **ALL 6 TASKS build+per-task-review clean.** PHASE GATE: full suite 2354 pass; eval fts recall@10 0.926 (==baseline); scoped lints at baseline (orphans 758/schema-drift 191/broken-wikilinks 1).
- **Whole-branch + security review found 3 merge-blockers — ALL FIXED, closure re-reviews running:** C1 policy wrote a git-TRACKED file (`.knowledge/policies/`, 753 files; test fixture's blanket `.knowledge/` gitignore masked it) w/ no commit → now commits through gate w/ Intent-Id trailer (`9acd9247`); SEC-Critical spoofable policy-edit identity → CLI-ONLY + server-sourced `GATEWAY_POLICY_PRINCIPAL` fail-closed (`6d4eef12`); SEC-High reversal-delete no containment → `_rel_escapes_root` (`9acd9247`).
- **Triggered backlog files** (`3d4c393f`): G7 migration delta, I1 no cluster() driver, I2 no reverse-merge producer, demand-ledger DoS.

### Files mid-edit
- None build-wise. Two closure re-reviews in flight: whole-branch `a3ca65a1dfb8430f4` (confirm C1) + security `ae26441f21455fba8` (confirm SEC-Critical/High). HEAD `3d4c393f`. (NOTE: subagents twice wrote/overwrote this session-state — a first T6 run committed a premature "T6 complete" at `7d965221`; corrected. Lesson for memory: subagents shouldn't own session-state.)

### Decisions made this session (T6-specific)
- Reused `.knowledge/eval/dedup/golden.yaml` as merge_map source (no separate file — duplication adds zero signal).
- **C1 correction:** `.knowledge/policies/` is git-TRACKED (NOT gitignored — only locks/lint/watcher/scheduler/auth/secrets/demand/transcripts are). `_apply_policy_edit` commits the policy write through the gate's atomic boundary (`_commit_reversal_writes`: git add + Intent-Id-trailer commit + provenance), not a bare write_text. Whole-branch review confirmed C1 closed + no pipeline interference.
- **Policy-edit trust model (user delegated to me; FLAG FOR PR/user ratification):** CLI-ONLY (removed from all MCP surfaces, CLI_ONLY like demote-domain); privilege from server-sourced `GATEWAY_POLICY_PRINCIPAL` (env/.knowledge/secrets.env), unset→fail-closed; resolved principal stamped for audit. Rationale: a full-Bash build-tier agent can shell out anyway, so an in-request allowlist was never a hard boundary; G7's real job = keep op off agent tool surfaces + change-control gate + unspoofable audit.
- **Cosmetic cleanups pending** (whole-branch review, non-blocking): stale docstring `commit_gate.py:1080-1082` ("gitignored/no git add" — now false); policy-edit commit subject reads `revert(...)` (reuses `_commit_reversal_writes`).
- **Gate (post-fix, `eadda916`):** the policy-edit gate DERIVES dedup params (blocking_band/identity_threshold/strategy) from the PROPOSED policy_data and runs a parameterized `merge_map_eval`; dead-letters on ANY golden regression for all strategies (was an inert hardcoded `"geometry-only"` string-match before the fix). FAILS CLOSED on any gate-eval exception (`f86c6365`); domain slug-validated + path-containment-checked at both layers.
- `policy_provenance` lint reads `decision_basis` (the real provenance key, fixed `757c08b5`); detects absence of a policy-edit provenance node; content-hash match is a backlog hardening item.

### Next atomic step
NONE — Phase 5 MERGED (PR #31 → `ee97cc9e`), branch deleted, local main == origin/main, trust model ratified. The 5-phase Librarian multi-agent RAG build is COMPLETE; no Phase 6. Optional, trigger-gated only: 4 backlog follow-ups under `docs/backlog/` (policy-edit op migration, demand-cluster driver, reverse-merge producer, demand-ledger DoS bound) — action only when each file's revival trigger fires. Session-review findings: docs/260619_session-review-2.md.

---

## ✅ LIBRARIAN PHASE 1 — COMMIT FOUNDATION (2026-06-18) — DONE

**Branch:** `docs/librarian-rag-design`. Plan: `docs/plans/2026-06-18-librarian-phase1-build-plan.md`.
All five tasks shipped TDD, per-task commits: T1.1 intent queue (durable dir,
fencing+lease, C3/C7), T1.2 OperationResult async fields + _serialize (A5),
T1.3 intent-status op + CLI/MCP (A1), T1.4 CommitGate — commit mutex + MVCC CAS +
idempotency-from-history + fencing + crash recovery (C1/C2/C3/C4, decision 1),
T1.5 operational-provenance log + C7 watcher routing + A7 telemetry stub.

**Gate:** pytest 1994 passed (baseline 1960; +34 new). eval-retrieval recall@10
0.926 (unmoved — no retrieval code touched). Ledger §4 Phase-1 green-gate all [x];
§5 four Phase-1 rows = green. C1/C2/C3/C7 detector tests named in §4.

**Phase-1 hardened + GATE FULLY PASSED (2026-06-18).** Independent review found 3 BLOCKING +
silent-corruption defects (tree-wide destructive recovery → scoped; CAS vs literal "HEAD" →
real per-path blob OIDs; substring Intent-Id grep → exact trailer compare; blind-overwrite merge
→ fail-safe dead-letter; non-atomic claim → os.replace + durable monotonic fencing; watcher
coverage-marker) — all fixed TDD; independent re-review returned **GO**. Then background security
review found a MEDIUM path-traversal in scoped-recovery `unlink`/`checkout` (test confirmed it was
exploitable — sentinel deleted) → guarded at use site + `set_declared_writes` rejects `..`/abs.
**Gateway suite 2002 passed; recall@10 0.926 unmoved.** Gate: eval ✓, independent code-review GO ✓,
security ✓.

**STANDING BUILD RULE → MIGRATED.** The standing build rule (adversarial tests + named negative
controls, no monkeypatching the core path, realistic merge/reattachment payloads, independent
reviewer≠author gate + security review, failing eval/review HALTS) now lives — with the reviewer
dispatch template and the inert-in-production hunt list — in the evergreen
**`docs/MULTI-AGENT-BUILD-PLAYBOOK.md`** (single source; read it before any phase plan or build).

**Phase-3 carry-forward (residual, non-blocking):** (a) the fail-safe rebase branch in `commit_gate`
is where Phase 3's structured-claim merge plugs in (§5.1 case-2 mergeable rebase currently
dead-letters `needs-merge`); (b) `git log --all` scans in `_already_committed`/`coverage_gap` are
O(history) — scale-watch.

**Next atomic step:** Phase 2 — Identity substrate (embedding index, 3 namespaces, upsert-on-commit
off the now-green CommitGate, shadow-swap rebuild, per-namespace adequacy gates I2, rebuild-and-diff
detector F2). ENCODER FORK (resolve in-build, do NOT add heavyweight ML deps autonomously): build a
pluggable encoder interface + the three-namespace machinery; default the ACTIVE path to the design's
lexical fallback (I2: dedup→alias/lexical, demand→lexical-canonicalized) so the gate passes honestly
without a 2GB torch dep; a neural encoder is a later opt-in decision. Record whichever is active in
«embed.model_version».

---

## ✅ LIBRARIAN PHASE 2 — IDENTITY SUBSTRATE (2026-06-18) — DONE

**Branch:** `docs/librarian-rag-design`. Plan: `docs/plans/2026-06-18-librarian-phase2-build-plan.md`.
Embedding index added ALONGSIDE the FTS index (derived/gitignored/rebuildable). Per-task commits:
T1/T2 `embedding_index.py` (pluggable `Encoder` protocol + active `LexicalFallbackEncoder` =
`lexical-fallback-v1`, dim 256, pure-numpy hashed token-set + char-3-gram; three namespaces
section/entity/question with distinct cosine-distance operating points 0.55/0.30/0.70), T3
incremental upsert-on-commit in `commit_gate.py` (freshness — earlier-in-window page visible to the
next intent's entity-NN; `embedding_index=None` back-compat no-op; quiesce on
`librarian-embedding-rebuild` lock), T4 shadow-swap rebuild (`os.replace` atomic) + rebuild-and-diff
(F2, `index-rebuild-divergence`), T5 per-namespace adequacy gates + golden sets under
`.knowledge/eval/embedding/` (I2; all three PASS at floor 1.0, falsifiable).

**Gate PASSED:** pytest 2034 passed (baseline 1998 + 4 recovered flakes + 32 new Phase-2 tests; the
4 `test_doc5_rotate_log` baseline flakes pass in a full clean run — order-dependent, unrelated).
eval-retrieval recall@10 = 0.926 (unmoved — no FTS retrieval touched). `wiki lint` RC=0 (758
pre-existing source-orphans, not Phase-2). Adversarial: concurrent-read-during-rebuild + non-atomic
negative control; constant-encoder negative control fails the entity gate. Ledger §4 Phase-2 gate
all [x]; §5 EMB row green; §1.2 «embed.*» calibrated + bound; §3 rebuild row = 7.26s / 4023 pages.

**Review fixes (2026-06-18):** Finding 1 lost-row race fixed — `rebuild_from_canonical` now holds `REBUILD_LOCK` across scan+build+swap (was swap-only), so a commit upsert can no longer be clobbered (test `test_commit_during_rebuild_row_survives_without_rebuild`; 1b masking test strengthened to assert survival with NO intervening rebuild). Finding 3 F2 chain tested — swallowed commit upsert reported as `extra` by `diff_against_live` (`test_swallowed_commit_upsert_is_caught_by_diff_against_live` + clean negative control). Finding 4 "honest" family removed from Phase-2 code/docstrings. pytest 2037 passed; recall@10 = 0.926.

**Independent review: GO (conditional).** No blocking defect for Phase 2 itself; substrate
correctly built + honestly tested (shadow-swap atomicity, upsert freshness, F2 all verified;
adequacy-gate falsifiability mechanism real via constant-encoder negative control). The two
conditional items: #1 rebuild race — FIXED above. #2 → carried as a Phase-3 ENTRY GATE (below).

**⚠ PHASE-3 ENTRY GATES (must hold before Phase-3 dedup ships — review-surfaced):**
1. **Entity golden set is too easy.** It omits the hard dedup cases; the active `lexical-fallback-v1`
   encoder gets them backwards — Ozempic vs Semaglutide (brand↔generic) at cosine dist 1.0 (false
   no-merge), "Type 1 diabetes" vs "Type 2 diabetes" at 0.198 (false merge), shared-prefix Fed
   branches at 0.25 (false merge). The «embed.dedup_identity_threshold»=0.30 sits in dead space, so
   the gate passes without proving fitness. Phase 3 MUST: (a) harden `.knowledge/eval/embedding/entity.yaml`
   with hard positives (brand/generic, abbrev/expansion) + hard negatives (shared-prefix distinct
   referents), AND (b) wire alias/canonical-name exact-match as dedup AUTHORITY with embeddings
   recall-only (design §13 I2 fallback + I1 adjudicator: aliases authoritative, cross-kind never
   merge) — do NOT trust embedding-NN geometry alone for the merge decision.
2. **Confirm the rebuild-race fix under concurrent dedup load** — Phase-3 dedup reads the entity
   namespace at commit; verify a commit-time dedup during a rebuild sees a consistent namespace.

**Next atomic step:** Phase 3 — Commit-time invariants (domain resolution; LLM-free replayable dedup
I1 = deterministic precedence over entity_kind + alias/canonical exact-match + domain overlap +
blocking-NN band, plugging into the `commit_gate` fail-safe rebase branch; claim-level contradiction
auto-resolve «contradiction.precedence»; trust tiering on `_authority_key` eval-gated; write-skew
C5/F1; phantom-collision; merge-reattachment; merge-map golden I3; policy change-control G7; lost-update
F1). Honor the entry gates above first. The entity namespace + freshness from Phase 2 are the inputs
Phase-3 dedup blocks against. contp in the Phase-3 section of the master build-plan.

**CONTEXT-MANAGEMENT SEAM:** This window has run Phases 1–2 (build+review+fix each). Per the hard 50%
ceiling + fresh-session-per-phase rule, Phase 3 (the 11-task dedup keystone, highest-risk) should run
in a FRESH session via the Phase-3 contp. This is the agreed context discipline, not a blocker.

---

## ✅ LIBRARIAN PHASE 3 — COMMIT-TIME INVARIANTS (2026-06-18) — DONE

**Branch:** `docs/librarian-rag-design`. Plan: `docs/plans/2026-06-18-librarian-phase3-build-plan.md`
(PLAN→EXECUTE→GATE; build report `...-phase3-build-report.md`). Ran one fresh window: PLAN
(writing-plans, 8 bite-sized tasks grounded in real interfaces) → EXECUTE (one cohesive build
subagent, fresh context, TDD + per-task commit) → GATE (independent review + fix loop). The dedup
adjudicator is DETERMINISTIC + LLM-free at commit (I1) — pure `dedup.adjudicate`, no model call, no
index access in the held `librarian-commit` lock; replayable from logged inputs.

**Shipped (8 build commits `a3835f63`..`140aac74`, 4 review-fix commits `fb21cdb9`/`4e76a5cd`/`a1e4c509`/`6790772f`):**
- **T1 entry-gate 1a** — hardened `.knowledge/eval/embedding/entity.yaml` with genuinely-hard cases
  (disjoint-surface positives Ozempic↔Semaglutide / GLP-1↔expansion; shared-surface negatives Type1↔Type2,
  Fed-NY↔Fed-SF). Entity adequacy gate now honestly rides the active+falsifiable alias-authority fallback
  (I2) instead of asserting `value==1.0` in dead space.
- **T2 entry-gate 1b / KEYSTONE I1** — `src/gateway/dedup.py`: deterministic precedence
  {merge,link,distinct}. Merge AUTHORITY = alias/canonical exact-or-normalized match + same `entity_kind`;
  embeddings RECALL-ONLY (NN never merges on geometry alone); cross-kind NEVER merges. Total order
  `(round(nn,6), slug)` → replayable.
- **T3 I3** — `.knowledge/eval/dedup/golden.yaml` human-curated merge/link/distinct set + geometry-only
  falsifiability negative control. (Deviation: RULE-3 link gate tightened `identity_threshold`→`blocking_band`
  so distinct siblings stay `distinct`, not spuriously linked — golden is authority.)
- **T4 C5/F1/entry-gate 2** — adjudicator wired into the commit serial re-check; write-skew (both claims
  survive via `_claim_union` three-way add/add), phantom collision (merge into canonical, no duplicate),
  concurrent-dedup-during-rebuild reads a consistent namespace (REBUILD_LOCK quiesce; REAL rebuild, no
  monkeypatch). Negative control: genuinely-conflicting claims dead-letter.
- **T5** — `domain_resolve.py`: multi-label domain resolution; empty set → `quarantined` (never silent-untag).
- **T6 G5 (EVAL-GATED)** — `trust.py` server-derived tier (source-type + filter score; NO self-report arg);
  `_authority_key` down-weight `_W_TRUST*(trust-0.5)`, `_W_TRUST=0.5` < tier/authority weights; eligibility
  floor keeps low-trust pages retrievable. (Deviation: `_SCHEMA_VERSION` 1→2 drop-on-mismatch to add
  `pages.trust` to the derived, gitignored, self-healing index — reviewer-verified safe.)
- **T7** — `ops/contradiction.auto_resolve`: claim-level CiTO `disputes` edge + reversible provenance act
  (rule + policy version), precedence = server trust-tier then recency; loser down-weighted, stays
  retrievable. G5 negative control: self-reported trust cannot flip the winner.
- **T8** — `ops/deposit.py` typed deposit op (durable enqueue-before-ack, async receipt) + MCP build-tier
  `wiki_deposit` tool; authoring concurrent, only commit serial.

**GATE PASSED:** full suite **2163 passed** (baseline ~2037 + Phase-3 + review-fix tests; clean re-runs).
eval-retrieval fts recall@10 **0.926** (== baseline; trust down-weight added ZERO ranking regression),
recall@5 0.852, MRR 0.690. Lint: `broken-wikilinks` clean except 1 pre-existing `OSError: File name too
long` infra finding (not Phase-3). Ledger §4 Phase-3 all [x]; §5 both Phase-3 rows green; §1.2/§1.4 keys
exercised («dedup.blocking_nn_threshold»=0.15, «embed.dedup_identity_threshold»=0.30,
«trust.weight_coefficient»=0.5, «contradiction.precedence»).

**Independent review (reviewer ≠ author): GO-WITH-FIXES → all blocking+important closed → effectively GO.**
Verified correct first-pass: the keystone (determinism/alias-authority/recall-only), the 3 concurrency
tests (real paths, no monkeypatch), golden falsifiability, trust/G5, quarantine, T6 migration. Findings
fixed TDD (RED-before, re-reviewed): **B1 (BLOCKING)** merge silently dropped deposit body/wikilinks/aliases,
no tombstone → unions aliases + carries body + `merged_into:` tombstone + dead-letter `needs-manual-merge`
on collision; **N1** same drop via the preamble → carried under `## Merged context`; **I2** concept merge
mis-targeted `entities/` → real-rel-path target; **I1** disputes edge pointed at the new claim even when it
won → points at the policy-resolved loser.

**SESSION-REVIEW FINDINGS (capture, apply next phase):**
1. **Builder self-tests under-cover silent-corruption (no-exception) paths — AGAIN.** All 4 dedup defects
   lived on the merge-reattachment path and were invisible to the builder's tests because every test
   deposit body was *claims-only*. Minimal/stub fixtures hide invariant violations on transform/merge
   paths. SHARPEN the standing rule: **merge/transform/reattachment tests MUST use realistic payloads
   (full multi-section body, frontmatter aliases, inbound+body wikilinks, non-empty preamble), not minimal
   stubs.** The independent review + re-review caught every one — the reviewer≠author gate remains
   load-bearing and paid for itself a third phase running.
2. **The discipline works where the plan mandates it at the right granularity.** The keystone, concurrency,
   trust/G5, and golden-falsifiability paths were honestly built first-pass *because* the plan specified
   adversarial tests + named negative controls per task. The gap was only where the plan's example test
   bodies were simplified — i.e. the failure was in fixture realism, not in test-discipline intent.
3. **Plan referenced a non-existent CLI scope** (`wiki lint --scope dedup`); the real dedup-integrity check
   is `broken-wikilinks`. Minor; the builder used the right check. Lesson: verify CLI subcommand/scope
   names before a plan references them (Verify-Before-Act on operations, not just code).

**Tracked MINOR (N2, non-blocking):** the materialized `disputes`-edge line double-cites the loser source
(the loser claim text already carries its own `[[sources/…]]`; the edge prepends a `…|disputes` link to the
same source). Cosmetic, functionally correct. Revival trigger: any CiTO-edge rendering pass or a reader
complaint about duplicated citations.

**MERGED TO MAIN — 2026-06-19.** Phase 1+2+3 (whole `docs/librarian-rag-design` arc, 57 files / ~10,330
insertions) merged via **PR #29** (`feat(librarian): multi-agent RAG — Phases 1–3`), merge commit
`8a509406` on `origin/main`. N1 fix `6790772f` confirmed ancestor of `origin/main`. Merge-commit strategy
(per-task/per-fix SHAs preserved for BUILD.md/ledger refs). Branch `docs/librarian-rag-design` **deleted**
(remote + local) — fully merged, 0 commits not in main, verified before delete. No git work pending; the
8 task commits + 4 review-fix commits (B1 `a1e4c509`, I1 `fb21cdb9`, I2 `4e76a5cd`, N1 `6790772f`) are all
on main. Working tree clean on `main`. **Phase 4 still = FRESH SESSION via the Phase-4 contp (below).**

**Phase-4 carry-forward (residual, non-blocking):** (a) `_merge_kind` normalization treats all
`wiki/concepts/` pages as kind `concept` — if a concept page ever carries a finer `entity_kind`, revisit;
(b) `auto_resolve` is called from the commit path WITHOUT `filter_score`, so contradiction trust there is
source-type-only (the filter-score blend in `trust.server_trust_tier` is inert on that path — wire it when
the deposit carries a filter score); (c) the Phase-1 O(history) `git log --all` scans in
`_already_committed`/`coverage_gap` remain a scale-watch.

**Next atomic step:** Phase 4 — Tiered agent surface (read/build tier split = two MCP entrypoints + op→tier
table A2; deposit consumer contract A1 = the wait/backpressure loop an agent author codes from spec, typed
disposition union + `retry_after`; bounded lock acquisition A3 off `flock` no-timeout; per-producer telemetry
alarms A7 = rejection-spike / dedup-merge-spike / deposit-silence detectors). The `wiki_deposit` tool + the
async receipt + `intent_status` from Phases 1+3 are the inputs Phase 4's consumer contract builds on. contp
in the Phase-4 section of the master build-plan (`...-multi-agent-rag-build-plan.md`), reproduced below.

**CONTEXT-MANAGEMENT SEAM:** This window ran Phase-3 PLAN→EXECUTE→GATE (build subagent + independent
review + 2 fix loops) and stayed lean by keeping the build/review/fix in subagents. Per the fresh-session-
per-phase rule, **Phase 4 runs in a FRESH session via the Phase-4 contp.**

---

## ✅ LIBRARIAN PHASE 4 — TIERED AGENT SURFACE (2026-06-19) — MERGED to main (PR #30, `5517f1f7`)

**Branch:** `docs/librarian-phase4` (cut off `main` @ `d931e568` — the stale contp named the deleted
`docs/librarian-rag-design`; deviation flagged + corrected). Plan: `docs/plans/2026-06-19-librarian-phase4-build-plan.md`.
Ran PLAN (writing-plans, 3 tasks grounded in real interfaces) → EXECUTE (subagent-driven-development: fresh
implementer + task-review + fix per task) → GATE (whole-branch review + security review). Stayed lean: all
build/review/fix in subagents.

**Shipped (7 commits `9fa43ac1`..`f12e0a66`, + doc commit `58aa73c5`):**
- **T1 (A2, decision 7)** — `src/gateway/tier.py`: op→tier classification, DEFAULT-DENY (read-tier only if
  provably side-effect-free AND token-free; else build). `mcp_server.build_read_tier_server()` = 2nd FastMCP
  registering exactly `tier.read_tier_tool_names()`. READ_OPS = {retrieve, search, context, related,
  intent-status, list-concepts, list-domains, agent-log} + aux {poll-list, question-list}. **Task-review caught
  3 mis-classified ops** (`agents`/`lint`/`status` write `.knowledge/` state or spend tokens) → dropped to build
  (`9d0fb655`). A read-tier op MAY append log.md + trigger the self-healing FTS upsert (gitignored, no corpus
  mutation, no tokens) — that is not disqualifying (comments `f4deeff2`/`f12e0a66`).
- **T2 (A1, A3)** — `locking.file_lock(name, *, timeout=None)`: bounded acquire (`LOCK_EX|LOCK_NB`+deadline→
  `LockTimeout`); `timeout=None` byte-identical blocking back-compat for 30+ call sites. `commit_gate` barrier
  uses 30s bound; on `LockTimeout` returns `disposition="retry-later"` (no queue-state mutation — intent stays
  durable; fix `b39c0ea1`). `IntentQueue.depth()`; `deposit()` sheds `rejected:overloaded`+`retry_after` at
  `depth()≥MAX_BACKLOG=256` (queue-depth backpressure — deposit holds NO commit lock; authoring concurrent).
- **T3 (A7)** — `provenance.alarms()`: pure function, 3 detectors (rejection-spike / dedup-merge-spike /
  deposit-silence) + negative controls.

**GATE PASSED:** full suite **2182 passed** (2163 baseline + 19); `eval-retrieval --compare` fts recall@10
**0.926** (== baseline — no retrieval code touched); per-scope lint at pre-existing baseline (orphans 758 /
schema-drift 191 / broken-wikilinks 1 = the known "File name too long" OSError / link-rot 733 — NONE Phase-4,
which added zero corpus content). Independent whole-branch review (opus): **GO** (no Critical/Important; 3 Minors
deferred). Independent security review (opus): **ship it** — boundary holds, lock safe, no new exploit. Ledger
§4 Phase-4 all [x] w/ evidence; §5 tier+consumer rows green; §1.1 new «deposit.max_backlog» row.

**Security/review findings → backlog (concrete triggers):** F1 (Low, doc) — my comment overstated read-tier
(claimed no FTS-index write, but read ops self-heal the gitignored FTS db) → FIXED `f12e0a66`. F2 (Medium,
build-tier DoS) — global `MAX_BACKLOG` no per-producer fairness → `docs/backlog/librarian-deposit-per-producer-fairness.md`
(trigger: >1 concurrent producer in prod). F3 (Low, pre-existing) — `file_lock` name→path unsanitized
(path-traversal) → `docs/backlog/locking-lockname-path-traversal.md` (trigger: next lock-name call-site edit).
Plus `docs/backlog/wiki-lint-unscoped-unbounded-slow.md` (unscoped lint hung 1h28m — network checks no
per-check timeout; trigger: when a gate needs bounded full-lint).

**SESSION-REVIEW FINDING (apply next phase):** the task-review gate caught the 3 mis-classified read ops the
plan's own affirmative READ_OPS list got wrong — I authored the plan with `agents`/`lint`/`status` as read
WITHOUT verifying each against its op implementation. **Verify-Before-Act on a security-critical allowlist:
when a plan classifies ops into a privilege tier, the PLAN step must check each op's actual side effects, not
assert from the op name.** The reviewer≠author gate paid for itself a 4th phase running.

**MERGED 2026-06-19.** PR #30 (`feat(librarian): multi-agent RAG — Phase 4`) merged to `origin/main` via
merge commit `5517f1f7` (merge-commit strategy — per-task SHAs preserved). Remote + local branch
`docs/librarian-phase4` deleted. Local main fast-forwarded to `5517f1f7`; working tree clean. The stray full
`wiki lint` runs were killed (the watcher daemon `wiki watch` PID 1157 left running — it's supposed to be).

**Next atomic step:** `/clear`, then **Phase 5 = FRESH session** via the Phase-5 contp in the master build-plan
(Lifecycle & demand governance — retraction cascade G3/G4/G8, revert-resolution G1, corpus-rot governance §8,
DemandLedger I4, gap-routing §10, planner/executor pre-flight). Cut `docs/librarian-phase5` off the post-#30
main. This session-state update is the only unpushed local-main commit and rides into Phase 5's PR (Phase-3
precedent).

---

## ✅ LIBRARIAN MULTI-AGENT RAG DESIGN GENERATION (2026-06-19) — DONE (all 3 passes)

**Branch:** `docs/librarian-rag-design` (NOT main; inputs were committed here as
`e38b8c4e`). Running as a self-paced single-window loop (3 short iterations —
sanctioned by CLAUDE.md "single-window loops fine for ≤2–3 iterations"). User asked
to "loop through the development process per plan."

**Runbook:** `docs/plans/2026-06-18-librarian-rag-generation-runbook.md`.
**Inputs (authoritative):** `docs/plans/2026-06-18-librarian-multi-agent-rag-design-prompt.md`,
`...-constraints.md` (register: C1–C7, I1–I4, A1–A7, G1–G8, F1–F2),
`docs/backlog/librarian-cascade-revert-automation.md` (Option B POR, G1).
**Outputs:** `docs/plans/2026-06-18-librarian-multi-agent-rag-design.md` (design,
evergreen) + `...-checkpoints.md` (ledger, mutable — Pass C).

**Golden baseline (close-out guard):** recall@5 0.852 / recall@10 0.926 / MRR 0.690
(n=27, fts). Generation must not touch it; Pass C re-runs `eval-retrieval --compare`.

**Pass B — DONE.** Appended design §§9–16 (lifecycle/retraction cascade G3/G4/G8 +
revert-resolution Option A; gap-routing + keep-worthiness; DemandLedger I4; three-namespace
vector index I2/A6 + pre-commit embedding chicken/egg; placement + change-control G7;
§15 deferred incl. Option B trigger; §16 verification: merge-map golden redefinition I3,
dedup-precision/demand-purity/grounding-faithfulness axes via judge.py, full failure-mode
taxonomy table — F1/F2 + 9 bad states each with detector+bounded recovery; tested
rebuild-from-canonical per derived component). Design doc COMPLETE. IDs added in Pass B:
G1–G4, G7, G8, I2, I3, I4, A6, F2 (+ G5/G6/F1/A7 reinforced).

**Pass A — DONE.** Wrote design §0 + §§1–8 (dependency map + 5-phase cut: Commit
foundation → Identity substrate → Commit-time invariants → Tiered agent surface →
Lifecycle & demand governance; 2 mermaid). Attachment points grounded in real code:
`CommitGate` generalizes `discharge_orphans._git_commit_synthesis_drafts`; `wiki-author`
global flock (`locking.py:27/75`, no-timeout) is the narrow-or-replace delta; flat
`FastMCP` (`mcp_server.py:37`) → two entrypoints; `_authority_key` (`search_index.py:422`)
gets trust down-weight, eval-gated; `validator.validate_citation_grounding/_slug_uniqueness/_citation_verbs`;
`OperationResult`/`_serialize` extended for async receipt (A5). IDs resolved in Pass A:
C1–C7, I1, A1–A5, A7, G5, G6, G7(partial), F1.

**Surface-anchor correction applied:** prompt says "honest model/restatement";
rendered as "accurate/plain" per global language ban on the "honest" family.

**Pass C — DONE.** Wrote the ledger `...-checkpoints.md` (20 threshold rows = one per design
«»-key + 3 mandated extras [recall.floor_at_k, corpus.untagged/orphan ceilings]; corpus-health
metrics; liveness/backpressure incl. per-component rebuild-time + per-failure-mode counters;
5 phase-boundary checkpoints keyed to §0 names; live-progress table). Self-checks all PASS:
(1) classification — every runtime component maps to {commit-gate / typed deposit tool / demand
ledger / embedding index / intent-queue / policy key}; 3 are compositions/config NOT new
subsystems (read/build tier split = MCP registration partition; planner/executor pre-flight =
read-tier composition; verification harness = test infra) — none invented. (2) «»-keys: 20/20
have ledger rows, 0 missing (grep-verified). (3) per-ID coverage: all 28 constraint IDs
(C1–C7, I1–I4, A1–A7, G1–G8, F1–F2) resolved with a §-anchor; G1's Option-B portion explicitly
deferred §15 with trigger. Each §16-taxonomy bad state has a detector + bounded recovery.

**Close-out guard PASSED:** `eval-retrieval --compare` fts unmoved at recall@5 0.852 /
recall@10 0.926 / MRR 0.690 (== baseline; generation touched no retrieval code).

**Outputs on `docs/librarian-rag-design`:** design `...-design.md` (§0–16, evergreen) +
ledger `...-checkpoints.md` (mutable). Commits: Pass A `321c8a13`, Pass B `5f0cf527`, Pass C
(this). **Loop COMPLETE** — ran as a single-window 3-iteration self-paced loop (no scheduled
wakeups; no external wait between passes).

**Build plan — DERIVED + reviewed (2026-06-18/19).** `docs/plans/2026-06-18-librarian-multi-agent-rag-build-plan.md`
(597 lines) is the master roadmap = the LOOP PROGRAM. It sequences the 5 phases (Commit
foundation → Identity substrate → Commit-time invariants → Tiered agent surface → Lifecycle &
demand governance) per design §0, each with goal/components/build-order, verbatim ledger §4
green-gate, right-sized task table (files + interfaces + constraint-IDs + «ledger-keys»), and a
paste-ready per-phase contp. Loop protocol: one FRESH session per phase, PLAN (writing-plans,
phase-scoped) → EXECUTE (subagent-driven-development) → GATE = (1) eval green-gate +
`eval-retrieval --compare` ≥ recall.floor_at_k + lints + failure-mode detector tests, (2)
`code-review` skill on diff, (3) `/session-review`, (4) `/contp` + checkpoint + commit + `/clear`.
A failing eval OR code review HALTS (no advance). Hard rule: main window never exceeds 50% context
(fresh-session-per-phase + /clear at gates + subagent-driven execution). All 28 constraint IDs
land (traceability table). NOTE: file was authored by a parallel session (shared tree); this
session reviewed it (read-only Explore agent) and patched 3 defects — added C6 to the Phase-1
traceability row; corrected the false "Phase 1 plan already written" claim (it is written at
Phase 1's session start, like every phase); fixed the Phase 1 contp to WRITE its bite-sized plan
via writing-plans rather than assume it exists.

**Next: execute Phase 1 (Commit foundation)** as the first loop iteration — FRESH session via the
Phase 1 contp in the build plan. It will PLAN (write `...-librarian-phase1-build-plan.md`) →
EXECUTE → GATE. Do this after a context-management step (the user flagged 26% now; /clear before
Phase 1 to start clean). Branch is NOT main; merge `docs/librarian-rag-design` → main is the
user's call (push-branch+PR). Carried-in `log.md` change is watcher-daemon-owned; never staged.

---

## ✅ YOUTUBE CORPUS-GAP REMEDIATION + GROUPED-CITATION FIX (2026-06-18) — ALL MERGED

Three PRs shipped to `origin/main` this session (squash-merged, branches deleted):
- **#23 `256bcf3b`** — grouped-citation renderer fix (`query.py`).
- **#21 `87fb0099`** — WS-1 YouTube backfill (31 talks → 3 domains).
- **#22 `56c75bb8`** — WS-2 stand up `ai-temporal-video` (86 sources synced + synthesis + MOC).

Plan: `docs/plans/2026-06-17-youtube-corpus-gap-remediation.md`.

**WS-1 (#21):** 31 YouTube talks backfilled via `nlm-add` URL-recovery: `convergent-ai-brain` +27
(corpus 90→117), `risksystems` +2, `ai-native-business` +2. Convergent synthesis
`wiki/synthesis/2026-06-18-what-sets-the-ceiling-on-representational.md` regenerated with the grouped-citation
fix then **finalized** (0 uncited, 15 sources). Manifest quality finding: plan estimated ~14 convergent YT;
ground truth 27 (plan's source_map attribution was stale — used content match instead).

**WS-2 (#22):** `ai-temporal-video` was already bootstrapped (2026-04-28 legacy migrate — policy + 83
examples + 46 concepts + tagged sources all present), NOT "never bootstrapped" as the plan assumed. Kept the
calibrated policy (user call); the real gap was a missing NLM notebook. `nlm-sync` auto-created notebook
`2560f247-…`, synced **86/86** (0 failed). Synthesis
`wiki/synthesis/2026-06-18-what-are-the-dominant-method-families.md` regenerated + **finalized** (0 uncited,
24 sources). Authored the missing MOC `wiki/mocs/ai-temporal-video.md` (fixed a broken index.md link).
Memory written: [[feedback_verify_domain_artifacts_before_rebootstrap]].

**Grouped-citation fix (#23):** root cause of the "NLM drafts won't finalize" wall was NOT citations.py — it
was `query.py` `_inline_citations` matching only single `[N]` markers, leaving NLM's grouped citations
(`[4-6]`, `[7, 8]`) bare. Fixed the renderer to expand grouped markers → `[[sources/...]]` (6 TDD tests, no
validator change, hard rule #3 stays strict). The two existing query drafts were regenerated with the fix
active and finalized; residual NLM section-intro definitional lines were cited to in-section sources (per-page,
no policy change — user call).

**Abbrev-fix + research-draft finalize (#25 `d8863948`):** investigated the S3/S4 research drafts directly
(NOT trusting the prior note). There were **25** semantic-models 2026-06-17 drafts (not "12"), 209 uncited
claims. The prior "one citations.py fix unblocks all" framing was WRONG: 0 pages were fixable by
structural-label/aggregate-opener exemption alone. Real breakdown — (1) claim-detector FALSE POSITIVES: the
sentence splitter broke on abbreviation periods (`vs.`, `e.g.`, `i.e.`), flagging "X vs. Y" comparison items
as claims → fixed with `citations._split_sentences()` (abbreviation-masked split, 2 TDD tests, 1960 suite
green); (2) genuine **under-attribution**: NLM's `### Specifics` sections generate substantive claims
(`**Name and Key Claim**`, `**Core Approach**`) from sparse corpora with ZERO inline citations.
**8 finalized** (4 already 0-uncited + 4 after trimming non-citable `## Gaps in Coverage` meta-openers).
**17 left as drafts** — genuinely under-attributed; finalizing would fabricate provenance (hard rule #3 +
`test_query_does_not_backstop_uncited_lines`). The gate is working correctly.

**Distinct-formats note (resolved):** `wiki query` pages use `[N]` + `## Sources cited` (fixed by #23);
`wiki research` pages use `[N]` + `[^N]:` defs (those resolve fine — the blocker was the abbrev false-positive
+ under-attribution, NOT structural-label matching as the old note guessed).

**17 under-attributed drafts — ABANDONED (#27 `5fafbd05`, user call).** They fail the quality gate
(NLM `### Specifics` prose from sparse/low-quality transcripts, no inline citations) and the user knew the
source transcripts were weak when pulling them. Deleted via `wiki finalize --abandon` rather than
force-passed; raw sources untouched. Net for the S3/S4 run: 8 finalized, 17 removed, 0 left as drafts.

**Deferred (need explicit go):** (a) fresh-discovery expansion of ai-temporal-video beyond the 86 (gated
behind any live YouTube-adapter session); (b) 46 ai-temporal-video concept stubs have empty `title`
frontmatter (migration artifact); (c) risksystems/ai-native-business re-synthesis (+2 each, marginal —
skipped).

---

## ✅ SEMANTIC-MODELS RESEARCH LOOP — STREAMS 3+4 SHIPPED (2026-06-17)

**Status: COMPLETE + on `origin/main`.** Merged via **PR #20 → `a7f4275e`**. Commits on main:
`fd2acd09` cache-seam code/infra (youtube.py + test + .gitignore), `23037bb2` research corpus
broad cut (311 files — sm streams 3+4 + same-day agentic-data-layer tail; condo/orita/obsidian
backlog excluded), `6f6c9a33` session-state. docs/YT-failed-transcript-table/ RTF originals (2.8M)
gitignored.

**Git tree cleaned (2026-06-17):** `main` = `origin/main` (0/0, clean worktree). Stale branches
`refactor/promote-public-title-resolver` + `semantic-models-loop` deleted (were fully on origin/main;
remote semantic-models-loop auto-deleted on merge). Other-projects' WIP restored to
`wip/condo-orita-restore` (current working branch, ~227 files vs main). `keep/local-main-20260617`
preserves the parallel session's unpushed `89a63954` (acceptance-gate contp doc) — leave until that
session pushes/discards it. NOTE: the cherry-pick that first diverged local main was the wrong move
(it skipped `4bcf938f` = user's PR #19); resolved via push-branch+PR. See memories
`feedback_defer_to_git_best_practices` + `feedback_verify_branch_before_commit_shared_tree`.

**Review brief:** `docs/260617_session-review-5.md`.

Plan: `docs/plans/2026-06-17-semantic-models-research-loop.md`. Streams 1+2 ran earlier
(executed); this session ran **streams 3 (knowledge graphs) + 4 (semantic layers)** with
the improved YouTube protocol applied first.

**Improved-protocol gaps closed before executing (the plans + policy predated the YT fixes):**
- `.knowledge/policies/semantic-models/policy.yaml` — added `channel_authority` +
  `speaker_expertise` quality signals (mirrors agentic-data-layer; semantic-web/KG venues).
- Stream 3+4 plan YAMLs — rewrote `youtube:` queries from tutorial→conference/lecture/keynote
  register. (Runtime fixes — filter per-source-type guidance, promote-recover-URL — are on
  main and applied automatically at `--execute`.)

**Stream results:** S3 `2026-06-17-what-are-the-architecture-and-engineering` — 105→59
accepted→37 promoted, 7 synthesis drafts, corpus median 790w, distinct_sources 27. S4
`2026-06-17-how-is-semantic-modeling-applied-as` — 104→26→11 promoted, 5 synthesis drafts,
median 7084w, distinct_sources 10. Both `status: executed`. **Protocol validated:** ~17 (S3)
+ ~12 (S4) authoritative conference/keynote videos were *accepted* (vs 0 pre-fix) — KGC
keynotes (McGuinness, Berners-Lee), Connected Data London, Calvanese OBDA, AtScale/Cube.dev.

**YouTube transcript IP-block + recovery (NEW reusable infra):** all accepted YT videos
failed transcript convert — YouTube IP-throttles this connection (HTTP 429) across
youtube-transcript-api AND yt-dlp, authenticated or not. Built a **transcript-cache seam**:
`converters/youtube.py` `convert()` now checks `.knowledge/transcripts/<id>.{txt,vtt}`
(overridable via `WIKI_TRANSCRIPT_CACHE`) before the network; parses plain text,
YouTube-panel `M:SS`-interleaved copy, and WebVTT. 6 new tests (`test_converters_youtube_cache.py`)
+ converter regression green. `.knowledge/transcripts/` gitignored. Doubles as the permanent
yt-dlp fallback once the IP unthrottles. User manually captured transcripts (RTF via TextEdit)
→ `textutil` converted → **25 ingested** via `wiki ingest --force-include --domain semantic-models`
(raw/youtube/yt-*.md + wiki/sources/yt-*.md, `caption_track: cached`). 4 NOT recovered, DROPPED
(do NOT re-queue): `9G4539pngVM`, `THekUSlGMyo`, `Ve6lavTtnQ8` (foreign-language or low-value
video per user), `8cl9IGY4A9E` (paste error — duplicated 6-OdjYdEpeU; removed). Content is
rough ASR auto-captions — landed in the local
RAG layer only; the S3/S4 NLM synthesis drafts were NOT regenerated (decision: ASR noise >
incremental insight; web/arxiv core already grounds them).

**FINALIZE — DEFERRED (user decision 2026-06-17), gateway-fix-gated.** The 12 S3/S4 synthesis
drafts (committed, `draft: true`) do NOT finalize: `wiki research` NLM-synthesis output is not
finalize-compatible. Substantive bullets ARE grounded — the validator accepts footnote refs
(`[N]` inline + `[^N]: [[sources/id]]` map; `citations.py` `_FOOTNOTE_REF_RE`/`_FOOTNOTE_DEF_RE`).
Blockers: (1) NLM emits structural labels as `*   **Name and Key Claim**: X` (title-case, colon
OUTSIDE the bold, bullet-prefixed) — `_STRUCTURAL_FRAME_LABEL_RE` expects `**Label:** ` and the
allowlist has lowercase `"Name and key claim"`, so they miss; (2) aggregate-framing openers
("Based on the provided sources, several patterns emerge…") ARE in the allowlist but the M45
exemption is GATED on `synthesizes:` (≥2) + `## Included works`, which `wiki research` pages lack;
(3) ~15 genuinely uncited cross-cutting/limitations prose sentences (no `[N]` at all). TRIGGER to
revive: scoped TDD fix in `citations.py` (match NLM's bulleted `**X**:` label form; ungate
aggregate-opener exemption for synthesizes-less pages) + cite-add the ~15 genuine claims — fixes
ALL future research syntheses, not just these 12. Batch tools (`finalize-batch`, `draft-close run`)
only target STALE drafts (>7d); these are today's, so they won't pick them up regardless. Memory
candidate (not yet written): "wiki research synthesis output is not finalize-compatible".

**OPEN — commit + staging decision (user call, NOT yet done):** working tree is a large mixed
pile (244 today-mtime untracked raw pages = semantic-models loop + agentic-data-layer tail;
plus the protected condo/orita/clippings/obsidian backlog). No reliable per-domain handle
(raw frontmatter `domains: []`, bodies never name the domain, source_maps UUID-keyed).
Cleanly-identifiable sm artifacts: 20 wiki/synthesis `2026-06-17-{architecture-and-engineering,
semantic-modeling-applied,foundational-formalisms,engineer-ontologies}*.md`, 25 `yt-*`
raw+source pages, policy.yaml, 4 plan YAMLs, plan doc, `docs/YT-failed-transcript-table.md`.
Code/infra commit (youtube.py + test + .gitignore) is clean+separable — land it first.
`docs/YT-failed-transcript-table/` holds 2.8M of RTF originals — do NOT commit. Never
`git add -u`/`-A`.

---

## ✅ AGENTIC-DATA-LAYER DOMAIN + YOUTUBE-AWARE FILTER (2026-06-17) — merged a4b11ac2

**What shipped:**
- New citation-grounded domain `agentic-data-layer` (sibling to `semantic-models`), vertical-agnostic — the runtime agent↔semantic-structure interface. Bootstrapped + corpus committed `559412b7`: 27-source NLM corpus, 13 synthesis pages, MOC. Plans 1 (consumption) + 2 (production/validation) ran as fan-outs; Plan 3 (architecture/failure-modes) as post-hoc `wiki query` synthesis.
- YouTube-aware filter fix, merged `a4b11ac2` (branch `feat/youtube-aware-filter`, deleted): per-source-type guidance in `semantic.py`, `channel_authority`/`speaker_expertise` signals in the `agentic-data-layer` policy, lecture/talk query register in `query_planner.py`. 220 tests pass. Plan: `docs/plans/2026-06-17-youtube-aware-filter.md`. SDD ledger: `.git/sdd/progress.md`.

**Decisions:** new domain not expansion of `ai-and-agents`/`semantic-models` (which excludes this layer by design); vertical-agnostic (anchoring to longspan would bias filter/examples); YouTube fix = restore metadata-based awareness, NOT score-post-materialization (research-notebook proved metadata-first works; NLM gets the transcript via `source_add_url` regardless).

**Rejected:** "drop YouTube" (0-accepts was a filter regression, not absent signal); "score post-materialization" (over-engineered — transcript already reaches NLM via URL).

**Open / next (user-trigger):**
- **Acceptance gate — PASSED 2026-06-17 (session `2026-06-17-what-are-the-current-architecture-and`).** YouTube-heavy re-run with S2 idle: 230 candidates → 77 accepted (33%, vs prior ~11%); planner emitted institution/conference-anchored YouTube queries (Stanford/NeurIPS/KGC/Connected Data London); **31 YouTube sources materialized (vs 0 accepted across prior plans)**, 3 cited in synthesis with full transcripts (1.3k–19k words) — conference keynotes (Eifrem GraphRAG, KGC 2024, NeurIPS'24). semantic_scholar recovered (48 candidates, no 429). corpus_quality median 2512w, distinct_sources 20. The fix works end-to-end.
  - **RESOLVED 2026-06-18 — confirmation re-run SKIPPED (user call).** The contp (`docs/260617_contp-acceptance-gate-rerun.md`) gated a confirmation re-run on both gates idle; on 2026-06-18 they were. Evaluated and skipped — a third run adds nothing. The fix is confirmed **twice across two domains**: (1) this acceptance gate (33% accept, 31 YT materialized, 3 cited w/ full transcripts); (2) independent re-validation on semantic-models S3+S4 (~17+~12 authoritative conference/keynote videos accepted vs 0 pre-fix — KGC keynotes, Connected Data London, Calvanese OBDA, AtScale/Cube.dev). Fix `a4b11ac2` + all four follow-ups merged to `main`; clean tree, 0/0. Contp obsolete — no further runs.
- **RESOLVED 2026-06-17 (PR #17 merged to main `7cd021b4`; fix `d005d17d`).** The promote-to-persistent path dropped sources lacking a `url` in the NLM-side session record into `source_add_text(content="", title=...)` → "Please specify a source" (31 YouTube sources failed persistent-promote, 33/72 promoted). Root cause: NLM's `source list --json` omits `url` for some source types (YouTube especially), so the URL was lost on the round-trip even though raw/ carries it. Fix: `session.promote()` now indexes raw/ by title once (`source_map._index_raw_pages`) and, for any URL-less session source, recovers the canonical URL from the matching raw page → `source_add_url`, or the real body content as a second resort → `source_add_text` with content, falling back to title-only text add for NLM-native sources with no raw page. Recovered URLs still dedup against the persistent corpus. 3 new tests + full gateway suite 1950 passed.
- Deferred follow-ups — **both RESOLVED 2026-06-17:** (1) `wiki bootstrap-domain` now auto-emits `channel_authority` signals for video-heavy domains (`feat/bootstrap-channel-authority`, merged `dc61eb6b`; doc `170f44d8`); (2) YouTube converter transcript capture verified for local `wiki retrieve` parity (`verify/youtube-transcript-capture`, merged `c0177d86`; doc `cec017e7`).
- **Memory — WRITTEN (OK'd 2026-06-17):** (1) `feedback_s2_shared_key_concurrency`; (2) `feedback_filter_source_type_awareness` (links `feedback_general_purpose_inherits_surface_anchors`). Both already present + indexed in MEMORY.md.

**Do NOT touch:** the working tree holds the parallel project's uncommitted `wiki/`+`raw/` files and pre-existing session-start edits (condo/quebec wiki, gateway converters, docx) — not this session's work; never `git add -A`/`git add -u`.

Review brief: `docs/260617_session-review.md`.

---

## ✅ DAILY-REVIEW SKILL (2026-06-15) — built via skillify, deployed, pushed

Cross-session arc: turned the ad-hoc "daily review" request into a reusable skill.
Lives in `~/code/claude-config` (not knowledge), but tracked here as session work.

**Sequence:** re-authored the user's loose prompt to Anthropic best practices →
ran the full skillify cycle (qualify → RED → write → GREEN → deploy).
- **Skill:** `~/code/claude-config/skills/daily-review/SKILL.md` (commit `3a0226c`,
  `origin/master`). Six-section cross-project work journal (where/why/accomplished/
  lessons/priorities/next); defers code/token/prompt analysis to `session-review`.
- **RED→GREEN proof:** GREEN out-performed a hand-written review — the cross-project
  rule caught 2 repos (Condo, local-inference) a single-repo glance missed. Live
  invocation later caught a 4th (claude-config itself) + the doc's own commit.
- **Deploy:** symlinked into `~/.claude/skills/daily-review` (user-global → invocable
  from any repo). README skills table updated.
- **Bootstrap:** `install.sh` (commit `cff22bb`) — idempotent one-step relink of ALL
  skills into `~/.claude/skills/` (links new, repoints stale, never clobbers a real
  dir; `--dry-run`). Closes the machine-local-symlink gap; README points at it.
- **Today's doc:** `docs/260615_daily-review.md` (commits `f468f17f`, `920bfae7`) —
  the live deliverable, cross-project across knowledge/Condo/local-inference/claude-config.

**Lesson logged in the doc:** run the daily review LAST — it goes stale by its own tail
(the skill commit + doc commit landed after the first draft).

**Open / deferred:** none. Multi-machine relink is solved (`install.sh`); no per-machine
script beyond it is needed (YAGNI until a new machine).

---

## ✅ FIRECRAWL SECRETS REACH BACKGROUND DAEMONS (2026-06-15) — shipped, tested

**Problem:** launchd agents (`com.knowledge.watcher`, running; `com.knowledge.scheduler`,
script only — not installed) start from a minimal environment (plist gave only
`KNOWLEDGE_ROOT` + `PATH`). So `FIRECRAWL_API_KEY` / `WIKI_WEB_SCRAPER` — exported in
the interactive shell — were invisible to background ingest. Every watcher-ingested
URL silently degraded to trafilatura-only and 403'd on biorXiv/PNAS with no error
(the converter swallows Firecrawl misses by design). Same latent gap in the scheduler.

**Fix (Option B — env-file loader, chosen over baking into the plist):**
- `src/gateway/secrets_env.py` — `load_secrets_env(path=None)`: reads
  `.knowledge/secrets.env`, applies each `KEY=value` with `os.environ.setdefault`
  (real env wins), strips `export `/quotes, skips comments/blank/malformed, no-op on
  missing file. Returns the applied mapping.
- `src/gateway/cli.py` — `main()` calls `secrets_env.load_secrets_env()` first thing,
  so BOTH daemons (both dispatch through `main`) and interactive ingest see the secrets.
- `.knowledge/secrets.env` (gitignored) — `FIRECRAWL_API_KEY` + `WIKI_WEB_SCRAPER=fallback`.
- `.gitignore` — `.knowledge/secrets.env`.
- `tests/gateway/conftest.py` — suite-wide autouse `os.environ` snapshot/restore
  (root-cause fix: `main()` loading a real on-disk file is a global side effect; the
  suite had no env isolation, so any `main()`-calling test leaked the vars).
- Watcher reloaded (PID 1744 → 57803), now on the loader code.

**Eval (TDD, all GREEN):** 9 loader unit tests + `main()` integration test; baseline
repro (trafilatura 403); post-fix live eval — daemon-minimal env → loader → `fallback`
escalates 403 → Firecrawl, 22,966 words; `env -i` launchd-minimal entrypoint proof;
full gateway suite **1942 passed, 0 failed**.

**Benefit of Option B:** plists stay clean → key rotation is a one-line file edit, no
reinstall; the not-yet-installed scheduler inherits the fix for free on install.

**Shipped + follow-ups (all on `origin/main`):**
- PR #16 merged → `a71d59bb`. NOTE: the PR branch was cut from a local `main` that
  was 6 commits ahead of origin, so the squash also swept the unpushed orita-cmo arc
  (55 files) under the firecrawl commit message. No content lost (origin is a superset);
  local main soft-reset to origin to reconcile. LESSON: in this repo cut branches from
  `origin/main`, not local `main` (local routinely runs ahead).
- Follow-up fix `4cf76a13` (session-review #4): empty-value guard in the loader — a
  `KEY=` / `KEY=""` line no longer writes `""` (an empty FIRECRAWL_API_KEY would win
  over no-key via set-if-absent and suppress the trafilatura fallback). +2 tests.
- DECISION (#3): loader stays in `main()` = **global** (all CLI invocations, not just
  daemons). Parity (URL works in watcher AND by hand) > blast radius; firecrawl only
  fires after trafilatura already 403'd, so no happy-path spend. REVISIT TRIGGER: when
  a non-firecrawl secret is added to `secrets.env`, scope that key rather than narrow
  the loader.

**Open / deferred:** none. The scheduler is still script-only (not loaded in launchctl);
when installed it works without an installer change. Phase-1 firecrawl-scrape plan
(`docs/plans/2026-06-15-firecrawl-scrape-phase1.md`) is the broader arc this unblocks.

---

## ✅ ORITA-CMO DOMAIN MOC + ORITA.MD FINALIZE (2026-06-15) — pushed

Rode alongside the firecrawl work in the same session.
- **MOC** `wiki/mocs/orita-cmo.md` (commit `8f94e49a`): canonical single-read domain hub
  authored via `wiki moc-add` (gateway path; `citation_grounded=False`). Overview frames
  Orita's **upstream-only** audience-intelligence position and the **own-execution-vs-
  Klaviyo-partnership fork**; grouped+glossed entity/concept/synthesis links (0 broken),
  source clusters, open threads. Built from committed wiki content via an Explore subagent
  (operating-model arc + 20-concept toolkit) + direct spine reads. Interim narrative doc
  `docs/research/orita-cmo/domain-synthesis.md` was written then **deleted** (MOC supersedes).
- **Finalize** `wiki/entities/orita.md` (commit `feb19e46`): draft → finalized; passed the
  citation-grounding gate; `finalized_at` set. Closes the one stale-draft item the MOC flagged.
- Session review filed: `docs/260615_session-review-firecrawl-moc.md`.

---

## ✅ ORITA-CMO COMPETITIVE INTELLIGENCE (2026-06-15) — built, finalized, synthesized

Arc began from "draft a synthesis for orita-cmo" → the competitive-positioning
synthesis was impossible (empty competitor corpus; the grounded model correctly
refused). Built the corpus end-to-end, then synthesized.

**What was delivered (all committed to `main`):**
- **Discovery** (`docs/research/orita-cmo/competitive-set.md`): harvested 237
  youtube+web results via direct adapters (outside the analyst-grade ingest gate,
  which rejected 159/160 survey-tier candidates); enumerated ~50 competitors
  across Orita's 5 channels (email/ESP, deliverability/bot, SMS, programmatic
  direct mail, ad-audience, CDP/agentic). Commit 3ef47911.
- **Phase 1 direct tier**: ingested 5 direct competitors + adjacents — entities
  `black-crow-ai, monocle (+ OuterSignal M&A), clustie (+ full-venue), enalito,
  aampe (+ offerfit, movable-ink, hightouch)` + concepts
  `agentic-personalization-platform, martech-consolidation`. Commit 72e38682.
- **Blocked-aggregator access solved**: firecrawl→Capterra→`wiki ingest
  --force-include` pipeline (CB Insights account-gated; F6S hCaptcha — both
  unreachable). Built canonical sources via gateway id/hash helpers. Commits
  f7a5b517 (Black Crow) + b5e01bac (9 incumbents: klaviyo, attentive, postscript,
  drip, bloomreach, omnisend, yotpo, simon-ai, listrak — real ratings/features/
  pricing/integration catalogs).
- **Finalize**: all 25 competitor/adjacent pages citation-cleaned + finalized
  (Related-section annotations → bare links; Clustie pricing cited). Commit
  (chore finalize).
- **Synthesis** (`wiki/synthesis/2026-06-16-map-the-competitive-landscape-orita-operates.md`):
  complete 14-competitor landscape map + "Where Orita Sits" conclusion. Reframed
  prescriptive→descriptive (corpus grounds facts, not strategy). Regenerated at
  4000-token budget after the first version truncated at the 1500 cap. Commit
  71283c43.

**Domain state now:** orita-cmo has 2 synthesis pages (operating-model 2026-06-15
+ competitive-landscape 2026-06-16), ~25 finalized competitor entities (much
benchmark-grounded), `competitive-set.md` discovery inventory.

**Open / deferred (explicit-trigger only):**
- **Prescriptive positioning** doc (how Orita *should* position) needs Orita's own
  strategy material in the corpus — not a retrieval task; deferred until requested.
- **Blocked sources**: CB Insights "Orita alternatives" (needs paid account) +
  F6S (hCaptcha) — the richest curated competitor lists, still unreachable.
- **`answer.py` 1500-token cap** is a latent limit for wide syntheses — worked
  around via in-process override; a `--max-tokens` CLI flag would productize it.

---

## ✅ STAGE 2 COMPLETE (2026-06-11) — data-collectives project DONE

Foundation loop COMPLETE (Tasks 1–10, committed c3eaee04..3989c841). **Stage 2 —
condo application leg — now COMPLETE.** Deliverable filed:
`docs/research/data-collectives/stage2-condo-collective.md` — feasibility + design
position for a reserve-study data collective among engineering firms / PMs / HOAs.
Pure synthesis over the two grounded domains (data-collectives foundation +
condo-capital-infra); no re-research; spend cap respected.

**Verdict: Qualified GO** as governance-and-network infrastructure pooling the
non-rivalrous component-condition signal, Canada-first, reserve-study value (not
agentic demand) carrying the P&L. Key insight: condo is the STRONGEST application
of the foundation because the engine is *data-bound* — pooled cross-firm failure
observations are the binding input to its accuracy ceiling, making contribution
rational on narrow self-interest. 3 load-bearing assumptions, full risk set
(cold-start/SME, downstream-model liability resolved via "engine informs, PEng
firm certifies/owns stamp", substitutes trap, agentic bet), and exit cross-ref to
condo's ADR-0004 acquirer thesis (CINC/Associa; the co-op caps what an acquirer can
capture → sell the administrator/workflow layer, not the data).

Stage 2 wiki-grounding (Task 3) DONE 2026-06-11 (user requested). Grounded synthesis
page FILED + finalized: wiki/synthesis/2026-06-11-is-a-data-collective-among-condo.md
(via wiki answer --file scaffold → wiki edit grounded body → wiki finalize, mirroring
the foundation page recipe). 19 sources cited across BOTH domains (condo engine
docx-818ed0a0ce55/bf4965d0d33a + NS studies + acquirer/PropTech sources; foundation
fraud-utility/substitutes/legal/Catena-X/data-moat sources). finalize passed the
citation-grounding gate. ANTHROPIC_API_KEY_RESEARCH valid; one small answer call.

---

## Open contracts

**data-collectives research foundation — IN PROGRESS (self-paced loop).**
Spec: `docs/superpowers/specs/2026-06-10-data-collectives-research-foundation-design.md`.
Plan: `docs/superpowers/plans/2026-06-10-data-collectives-research-foundation.md`.

New citation-grounded wiki domain `data-collectives`, forked from `condo-capital-infra`.
Policy/market-structure spine; Approach C (agentic dimensional fan-out). Executed as a
self-paced loop, one plan Task per iteration: deep-research → `wiki ingest --with-plan`
the verified sources → author concept/synthesis pages → verify grounding → commit →
checkpoint here → schedule next.

**Task ledger (loop tracks progress here):**
- [x] Task 1 — bootstrap `data-collectives` domain (policy.yaml created, verified)
- [x] Task 2 — Stream 0 precedent census (seed) — 7 source pages + 8 concept pages + entities grounded; analytical note at docs/research/data-collectives/stream-0-precedent-census.md
- [x] Task 3 — Stream 1 economic/incentive — grounded: nonrivalry-of-data, data-shapley, competitor-data-sharing-tradeoff, product-differentiation-collaboration (+ Jones&Tonetti, Tsoy&Konstantinov, Data Shapley sources). Vives 1984 + Farboodi-Veldkamp verified but full-text won't convert (noted in stream-1 note). KEY: substitutes in same market have weak/negative pooling incentive (Vives Cournot PD).
- [x] Task 4 — Stream 2 technical/architecture — GROUNDED. 6 source pages live (FL gradient-inversion, subject MIA, DP-FL, DP survey, Azure Confidential Clean Rooms, NIST US-UK PETs Prize) via filter-correct + re-ingest. ACM-Queue + OPAL chapter still need alt URLs (cited by reference in note). KEY: agentic-layer gap (zero verified precedent — see note).
- [x] Task 5 — Stream 3 legal — GROUNDED. 6 sources: US DOJ safety-zone withdrawal (Arnold&Porter), Canada Competitor Collaboration Guidelines + draft ACCA, PIPEDA/C-27 de-id, property-in-data (Hastings), data-trust entity forms (Ada Lovelace). KEY: Feb-2023 DOJ withdrawal removed US bright-line safe harbors → case-by-case only; Canada two-track clearer (legal-certainty edge for Canada-first). No property in data → rights are contractual.
- [x] Task 6 — Stream 4 regulatory — GROUNDED. 7 sources (Canada Consumer-Driven Banking + PIPEDA data-mobility right, US info-blocking/TEFCA, ISED Voluntary GenAI Code, AIDA-death, Ag Data Transparent, EU Data Act ref). KEY: NO regulation compels/funds cross-competitor pooling — only consumer/holder-directed PORTABILITY exists. AIDA dead; Canada has no binding AI statute; US deregulatory. 'Why Canada' must rest on the economy-wide data-mobility right + strategy/funding, NOT regulatory compulsion.
- [x] Task 7 — Stream 5 governmental/policy (SPINE) — GROUNDED. 7 sources (Sovereign Compute Strategy, Pan-Canadian Phase 2, C.D. Howe missing-pillar, FNIGC/OCAP, Scale AI, NAIRR US-contrast, IAPP data-mobility). VERDICT: Canada funds talent/commercialization/COMPUTE, NOT data infrastructure — no funded mechanism for a data collective. 'Why Canada' rests on (a) CAN/DGSI 100-7 governance standard, (b) economy-wide data-mobility right, (c) data-sovereignty framing — NOT funding/mandate. Compute strategy is a distraction for a data play. Validates user's rhetoric-vs-mechanism skepticism.
- [x] Task 8 — Stream 6 academic — GROUNDED. 6 sources (GKC/Constructing-Commons, Ostrom 8 principles, data-as-labor AEA, Vincent 2025 collective bargaining, Jonker + Duncan critiques). VERDICT: strong theory, near-absent empirics, every org form has a distinct fragility; collectives solving collective-action was REFUTED in verification. Enabling regulation may be a precondition (Jonker). Convergent with S0 failures + S1 substitutes.
- [x] Task 9 — Stream 7 industrial — GROUNDED. 6 sources (Early Warning Services + Cifas = genuine fraud-utility pooling; LexisNexis = aggregation contrast; a16z data-moat debate; Datavault aspirational; Catena-X SME stall ref). KEY: real cross-competitor pooling concentrates in FRAUD/AML utilities (pool the non-rivalrous signal). Agentic zero-precedent now CONFIRMED across 3 streams (0,2,7). Stream 7 verification partly truncated by Anthropic spend cap.
- [x] Task 10 — synthesis COMPLETE (analysis). docs/research/synthesis-policy-market.md answers the north-star + full confidence/uncertainty ledger. DEFERRED (external cap, not blocking): the citation-grounded wiki synthesis PAGE via wiki query — file on Anthropic spend-cap reset. wiki answer stays 401-blocked. Agentic targeted pass cancelled (zero-precedent confirmed 3x).
- [x] Task 11 / Stage 2 (condo application leg) — COMPLETE 2026-06-11. Deliverable: docs/research/data-collectives/stage2-condo-collective.md. Qualified GO. See top block.

**Guardrails (every Task):** foundation pages domain-neutral (no reserve-study /
condo / Longspan terms — that is Stage 2); citations mandatory (`[[sources/<id>]]`,
`--draft` then `wiki finalize`); adversarial verification before filing load-bearing
claims; date precedents, flag pre-2023 for AI-model claims; `wiki retrieve`/`context`
only, never dump index.md/log.md.

**Per-stream recipe (learned in Task 2 — REUSE):**
1. deep-research workflow → verified findings + source URLs.
2. `wiki ingest "<url>" --with-plan --draft --domain data-collectives` per source
   (authorship path = Max-OAuth `claude -p`, WORKS).
3. For obviously-in-domain sources the strict filter put in review/rejected:
   `wiki filter-correct <id> --include --rationale "…" --domain data-collectives`
   then RE-INGEST `--with-plan` (correction alone does not author the source page).
4. Grounded concept/entity/source pages = the canonical stream deliverable.
5. Preserve the analytical findings + adversarial caveats + open questions in
   `docs/research/data-collectives/stream-N-*.md` (project doc, NOT wiki — avoids
   direct-write violation; feeds Task 10 + condo Stage 2).
6. Verify with `wiki retrieve`; commit. STAGING DISCIPLINE: never `git add -u wiki/`
   or `git add wiki/` — the working tree has a pre-existing condo backlog of
   modified/untracked pages (leave alone). Stage ONLY this stream's files by content
   match: `git ls-files --others --exclude-standard wiki/ raw/ | grep -lE data-collectives`
   plus the specific source IDs; add docs/research note + session-state + index.md +
   log.md + .knowledge/policies/data-collectives explicitly.

**AUTH CONSTRAINT (blocks `wiki answer` / SDK path):** `ANTHROPIC_API_KEY_RESEARCH`
returns 401 (invalid). So `wiki answer` and any SDK-cached call FAIL. Do NOT use
`wiki answer` per stream. The Max-OAuth `claude -p` path (filter / plan / --with-plan
authorship) WORKS. Final synthesis (Task 10) goes through `wiki query` (NotebookLM,
separate browser auth) once the corpus is rich — corpus-quality gate first.
Known authorship friction: the LLM sometimes picks entity_kind values outside the
controlled enum (consortium/proposal/project) → that entity page fails but the
source + other pages still commit. Not blocking.

---

## RESOLVED

**RAG retrieval build — DONE and MERGED to main (2026-06-09).** All 6 workstreams
landed; 2002 tests pass; recall@5 0.889 / recall@10 0.926 / MRR 0.722. Deferred WS7
hybrid vector retrieval (trigger: golden recall@10 < ~0.8 or ~10k pages — unmet).
`main` was 9 ahead of `origin/main` at that checkpoint; push remains the user's call.

Carry-forward (pre-existing, untouched): schema-drift ~208; finalize-batch ~460;
orphans (condo-capital-infra, glp1-reward-modulation, ai-native-business); edge-ai
notebook quota; `wiki migrate` stub; orita-cmo R3/R2; iOS Shortcut; web-API hardening.

---

## Files mid-edit

None. Working tree carries pre-existing untracked gateway-managed `nlm/`/`raw/`/`wiki/`
content (gateway-owned — leave alone).

---

## Next atomic step

**RESOLVED 2026-06-18: git cleanup DONE.** Working tree is clean on canonical `main` (= `origin/main` @ `97eef751`, 0/0 ahead/behind). Chose the tidy path ("just clean tree on main"). Preservation net intact, nothing deleted: `wip/condo-orita-restore` @ `7ba01392` holds the full 228-file / ~474k-line snapshot (condo / orita / semantic-models + agentic-data-layer tails — restore any file via `git checkout wip/condo-orita-restore -- <path>`); `keep/local-main-20260617` @ `6f6c9a33` is the old divergent local main. The redundant branches (`refactor/promote-public-title-resolver`, `semantic-models-loop`) were already deleted before this session; the only remaining step was `git switch main` off the snapshot branch. No git work pending.

_(Superseded reconcile note, kept for trail:)_ the 3 promote follow-ups merged to `origin/main`: #17 fix (`7cd021b4`), #18 test isolation (`aec29611`), #19 resolver refactor (`4bcf938f`). Review #3: `docs/260617_session-review-3.md` (meta-finding: loaded-constraint-not-applied gap; optional code cleanup: extract `_walk_raw_pages()` to dedupe the two source_map walk loops).

**Test-isolation follow-up — RESOLVED 2026-06-17 (PR #18, branch `test/isolate-promote-fixtures`, commit `c61bf3bb`, merged `aec29611`).** The promote URL-drop fix (PR #17, `7cd021b4`) added a `_source_map._index_raw_pages()` call to `session.promote()` that globs the live `raw/` tree; the 5 pre-existing promote tests lacked `kb_root`, so module tests regressed 0.02s → 7.96s with a real-filesystem dependency. Fix: added `kb_root` to all 5 tests (empty tmp tree) — **14 passed in 0.06s**, no assertion changes. Full analysis: `docs/260617_session-review-2.md`. **Public-resolver cleanup — RESOLVED 2026-06-17 (PR #19, commit `4bcf938f`, merged to main).** Added public `source_map.resolve_raw_sources_by_title(titles) -> {title: (url, full_text)}` (batched — single-title would re-walk raw/ per source, 31× on a YouTube-heavy promote); `promote()` calls it once; `_read_raw` + private-API reach into `_index_raw_pages` removed; `_FILENAME_EXTS` extracted/shared. 5 new resolver tests; full gateway suite 1961 passed. **Do NOT start autonomous work — the user is driving the `semantic-models` research loop in a separate window.**

**YouTube-aware filter acceptance gate — PASSED 2026-06-17** (see top block; promote bug found there is now RESOLVED via PR #17). Earlier review: `docs/260617_session-review.md`.

**data-collectives project COMPLETE (foundation + Stage 2).** No open work.

**Cross-domain synthesis gap — RESOLVED 2026-06-11 (PR #15, merged to main at
089dac39).** `wiki retrieve`/`wiki answer` now take `--domains a,b`: per-domain
quota merge (ceil(k/N) each, round-robin-interleaved, dedup by path) so balance
survives budget truncation; `answer` files list-valued `domains:` frontmatter
(fixes the old single-valued `answer.py:222`). Mirrored on the `wiki_retrieve`/
`wiki_answer` MCP tools. Golden set unchanged (recall@5 0.889 / recall@10 0.926 /
MRR 0.722 — single/global paths untouched); 1924 gateway tests pass; live smoke
test cited both domains. Spec/plan: `docs/superpowers/{specs,plans}/2026-06-11-
multi-domain-balanced-retrieval*.md`.

Remaining items are explicit-user-trigger only:
1. **Wiki-grounding backfill (both stages), cap-gated.** On Anthropic spend-cap
   reset or explicit request: file/finalize citation-grounded wiki synthesis pages
   for the foundation (from synthesis-policy-market.md) and Stage 2 (from
   stage2-condo-collective.md) via `wiki answer --file` (key now valid) or
   `wiki query` (corpus-quality gate first).
2. Optional source backfill: ACM-Queue + OPAL alt URLs (Stream 2); Truveta/Datavant
   health-pooling cases (Stream 7, truncated by cap).

**Carry-forward finding (still load-bearing):** privacy-preserving pooling substrate
is mature; the agentic layer on top is greenfield — no verified 2023–2026 precedent.
In Stage 2 this is the explicit unproven bet; the condo P&L closes on reserve-study
value without it.
