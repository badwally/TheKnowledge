# Multi-Agent Build Playbook

Distilled from the 5-phase Librarian multi-agent RAG build (2026-06-18/19). The disciplines here were not theorized — each was paid for by a real defect that shipped past an implementer's green test suite and was caught only by an independent reviewer. **Read this before authoring a phase plan or fanning out a subagent-driven build.**

> **Load trigger.** This is the deep checklist behind the always-on memories. Open it at two moments: (1) when writing a phase plan (`writing-plans`), and (2) when dispatching the build (`subagent-driven-development`). The knowledge-repo `CLAUDE.md` points here. Always-on hooks live in memory: [[feedback_inert_in_production_pattern]], [[feedback_gate_tests_what_ships]], [[feedback_subagents_dont_own_session_state]].

---

## Part A — Operational templates (use these directly)

### A1. The independent reviewer dispatch

The single highest-leverage practice. Across 5 phases the reviewer≠author gate caught a real defect in **every task** — each one invisible to the implementer's own passing tests. The reviewer's job is to **drive the feature on real data through the real path**, not read the diff.

Paste-and-fill skeleton (model: opus for destructive/governance/concurrency/subtle; sonnet for additive):

```
You are an INDEPENDENT reviewer (you did not write this code) for <TASK> in <repo>.
Two verdicts: (A) SPEC COMPLIANCE — built exactly what's required, nothing missing/extra;
(B) CODE QUALITY.

READ: <task-brief path>, <implementer report path>, <review-package diff path>.
BINDING CONSTRAINTS (verbatim from the spec): <copy the exact invariants/values>.

REVIEW METHOD — adversarial, on the highest-risk paths:
- For EACH feature/detector/gate, TRACE it to its real production data source and answer:
  can this fire / does this actually do its job on real data in production? (Run it.)
- Drive the destructive/concurrency/governance path on a real fixture (no monkeypatch
  of the unit under test). Construct the input that would break it.
- Confirm negative controls actually fail-safe; confirm RED→GREEN was real (revert the
  fix, watch the test fail).
- Distinguish exploitable/real from theoretical.

OUTPUT: Verdict A (✅/❌, specifics) · Verdict B (Critical/Important/Minor, file:line) ·
"⚠️ Cannot verify from diff" items separately. Adjudicate the named high-risk questions
explicitly; any "no" on a behavioral bar is Critical.
```

Rules that made it work:
- **Never pre-judge for the reviewer.** No "treat as Minor," no "the plan chose X, don't flag." Let them raise it; adjudicate in the loop.
- **Hand the diff as a file** (`review-package BASE HEAD`), not pasted — keeps the coordinator window lean.
- **Re-review after every fix.** The fix introduces its own risk (Phase-4 T4: the parameterization fix reopened a fail-open; Phase-5 T1: a fix surfaced a linked latent defect).
- **Keep the background/commit security review** for any destructive or privilege-bearing surface. It found 2 HIGH on the Phase-5 governance path the code review didn't frame for.

### A2. The inert-in-production hunt list

The dominant failure mode: **code that passes the author's happy-path unit tests but is inert or wrong against real data.** Caught in all six Phase-5 tasks. For every feature, the reviewer (and the implementer's own tests) must answer these — each maps to a real defect that shipped past green tests:

| # | Hunt question | The defect it catches (real example) |
|---|---|---|
| 1 | Does the op's intent have an **apply-branch** that actually executes? | T2: de-path enqueued a payload with no gate handler → dead-lettered, de-pathed nothing; the `reversible` flag was decorative. |
| 2 | Does this gate/threshold **change behavior**, or is it dead under the other conditions? | T4: cold-start gate (`mass>=3`) fully subsumed by `mass>=5` → zero effect. |
| 3 | Does the test's "different" input **actually differ**, and does the asserted property **depend on what changed**? | T4: the I4 "bumped" encoder called the real encoder → identical vectors; the metric never touched vectors. Tautology. |
| 4 | Does the consumer read a data source that a **producer actually writes** in production? | T5: cascade-depth detector read a sidecar file no code ever wrote → 0 forever, never trips. |
| 5 | Does the gate evaluate the **real input**, or match a hardcoded proxy? | T6: policy gate matched the literal string `"geometry-only"` instead of evaluating the proposed policy → a disguised regressing policy committed. |
| 6 | Does the code read the **real on-disk key/schema**, or a fabricated one the test invented? | T6: provenance lint read `node.get("basis")`; the real key is `decision_basis`. Test fixture fabricated `{"basis":...}` so it passed for the wrong reason. |
| 7 | Does the property/invariant test derive its **expectation** from an independent source, or from the unit under test? | Committer/harness T6: the hunt-#1 invariant enumerated `reversal_type`s from the same `_apply_reversal` it asserted against → removing an apply-branch dropped both the dispatch *and* the test case, so it could never go RED on the defect it targets. Fixed by cross-referencing the **producer** ops against the gate dispatch (two independent sources). A property test that reads its own answer key is vacuous. |

General rule behind all seven: **a test that builds its own fixture for the data the feature consumes proves nothing about production.** Drive the real producer (real merge, real gate commit, real recorder, genuinely-different encoder); make the negative control go RED on the pre-fix code.

> **The meta-gate can itself be inert.** The first cut of the committer/harness T6 (the inert-in-production property suite) *masked* a real production crash — `superseded_citations.run()` crashed with `FileNotFoundError` on a missing `raw/` dir (cold-start / fresh-clone), the only one of 32 lint checks unguarded — by pre-creating the directory in its own fixture. That reproduced the exact anti-pattern T6 exists to kill. When the test of "does this fire on real data" goes green by fixing the *fixture*, the fix is almost always in the wrong place: drive the real cold-start state and fix production. Apply hunt-question #4 and the general rule to the meta-gate with the same rigor as to the features it guards. (The opus reviewer caught this only by reverting the production guard and watching the negative control go RED — see A1 "re-review after every fix.")

---

## Part B — Disciplines

### B1. Standing build rule (binds every phase)
*(migrated here from `session-state.md` — this is the single source.)*

- Every builder writes **adversarial tests with named negative controls** for every concurrency / destructive-op / idempotency / merge-reattachment path.
- **Do NOT monkeypatch the core path under test.** (Phase-1 violation: an isolated-repo recovery test asserted the *unsafe* behavior as correct because it patched the core.)
- **Merge / transform / reattachment / reverse tests MUST use realistic payloads** — full multi-section body, frontmatter aliases, inbound + body wikilinks, non-empty preamble — never claims-only stubs. (Every Phase-3 silent-corruption defect hid behind a minimal fixture; the Phase-5 T1 alias over-restore hid behind a *fabricated* reattachment record.)
- **Every gate runs an INDEPENDENT review** (reviewer ≠ author) + the security review on destructive/privileged surfaces.
- A failing eval **or** review **HALTS** the phase — no advance.

### B2. Plan-time Verify-Before-Act
The two Phase-5 review rounds the *plan author* caused were both plan-time verification gaps. Apply Verify-Before-Act while **authoring the plan**, not just at execution (the global `~/code/CLAUDE.md` rule, applied earlier in the lifecycle):

- **Verify the persistence/gitignore status of every write target before the plan assumes it.** (`git check-ignore` is the cheapest precondition.) Phase-5 C1: the plan + test fixtures assumed `.knowledge/policies/` was gitignored; it is git-tracked (753 files), so policy-edit left a dangling uncommitted write — masked by a fixture's blanket `.gitignore`.
- **Cross-check every "produces X" in the plan against the gate's "X must *behave* like Y."** Phase-5 T1: the plan scoped `reverse_merge_plan` as plan-only, but the G8 gate demanded restoration *behavior* — a plan-internal inconsistency that cost a fix round.
- **Verify CLI subcommands/scope names exist before the plan references them** (Phase-3: plan cited a non-existent `wiki lint --scope dedup`).
- **Cross-check every "the gate must pass when X" against the system's *existing* definition of passing X.** Committer/harness G1: the plan specified the embedding check as "all namespaces `.passed`", but the production I2 contract (`test_embedding_adequacy.py`) defines acceptance as `passed OR (fallback_active AND fallback_falsifiable)` — the entity namespace is *intentionally* below its precision floor (the lexical encoder can't do brand↔generic identity). Coding the gate to the plan literally would have made it permanently red. The implementer caught it by reading the real contract instead of transcribing the plan; a gate built on an invented pass-condition is either always-red (useless) or, worse, relaxed-to-green with no teeth.

### B3. Gate tests what ships
*(see [[feedback_gate_tests_what_ships]])* — when the traceability/spec lists a constraint the phase "lands" but the green-gate doesn't test it, that is a **gate defect**. Build + test it (add the gate row) or carve an explicit triggered-backlog item. Never silently declare it "satisfied via existing mechanisms" — that writes false green into the ledger. (Phase-5: G2/G7/I3 were listed-but-untested; reconciled by building them + adding §4 rows.)

### B4. Subagent handoff hygiene
- **File handoffs, not pasted text.** Per-task `task-brief` → implementer; report to a `.git/sdd/` file; `review-package` diff to a file. The coordinator relays status, not content — keeps the main window under its context ceiling across a long build.
- **A dispatch describes one task, not session history.** Never paste accumulated prior-task summaries into a later dispatch.
- **Subagents must NOT write `session-state.md`.** *(see [[feedback_subagents_dont_own_session_state]])* — a Phase-5 subagent committed a premature "all tasks shipped" state before reviews ran. Scope subagent reports to `.git/sdd/`; the coordinator owns and reconciles session-state, and diffs its predictions against git+tests at each seam.
- **Durable progress ledger** at `$(git rev-parse --git-path sdd)/progress.md` — tasks marked complete there are DONE; resume from it after compaction, trusting the ledger + `git log` over recollection.
- **Make the reviewer's delivery contract explicit.** A reviewer subagent that finishes its analysis but returns nothing (goes idle without posting the verdict to the coordinator) costs a round-trip to extract a result that already exists — it happened twice in the committer/harness final gate (`t4-review`, `final-wholebranch`). Put the delivery instruction in the dispatch: "post your verdict as your final message to the coordinator; do not go idle without sending it." Lead the verdict with the decision word (Approved / READY TO MERGE / SHIP IT / BLOCK) so the coordinator can branch on the first line.

### B5. Token-tactical (small, mechanical, recurring)
- **Don't wrap fast scoped commands in `timeout`** — and `timeout` is absent on darwin (it's `gtimeout`). Phase-5 wasted 3 lint calls on this.
- **Capture command output in one pass.** `eval-retrieval --compare` was run 3× because `tail -20` truncated the recall numbers; `grep -iE "Retriever:|recall@|MRR"` gets arms + metrics in one call.
- **Targeted reads over wide reads.** Opening a long `session-state.md` with a full read cost ~25k tokens for ~2k of use; `grep -n` the section, then offset-read.
- **Load deferred-tool schemas before calling** (e.g. `ToolSearch select:SendMessage`) to avoid validation-retry loops; keep `SendMessage` summaries ≤200 chars.

### B6. Pre-merge gate (standing requirement for every merge to main)

Every merge to `main` must pass the pre-merge gate. Run it as:

```bash
.venv/bin/python -m gateway.scripts.gate
```

The gate exits non-zero on the FIRST failure and runs these steps in order:

| Step | What it checks | Failure = |
|---|---|---|
| 1 | Full pytest suite (`pytest -q`) | Any test failure |
| 2 | Fast + new tiers (`-m "not slow and not e2e"`) | Any unit/integration/property failure |
| 3 | `retrieval_eval` fts recall@10 | < 0.90 (floor) |
| 4 | `merge_map_eval` regressions | `regressions != []` |
| 5 | `embedding_eval` all namespaces (real I2 contract) | A namespace fails the I2 acceptance `passed OR (fallback_active AND fallback_falsifiable)` — i.e. below floor with no active fallback, or an active-but-non-falsifiable (rubber-stamp) fallback. The entity namespace is *intentionally* below its precision floor under the lexical encoder; the gate accepts it only because its fallback is falsifiable. |
| 6 | Scoped lints: orphans / schema-drift / broken-wikilinks | Count exceeds baseline |

Baselines (update in `gateway/scripts/gate.py:LINT_BASELINES` when a scope genuinely improves):

| Scope | Baseline |
|---|---|
| orphans | 758 |
| schema-drift | 191 |
| broken-wikilinks | 1 |

**The recall floor is `>= 0.90` exactly** (baseline 0.926). Do not lower it; do not skip the gate for "minor" changes — a gate that always exits 0 is inert (hunt #1).

The floor-check logic is in `check_recall_floor()` (`src/gateway/scripts/gate.py`) — importable and unit-tested in `tests/test_gate_script.py` without running the full suite. The unit tests include named negative controls (below-floor input must return `passed=False`).

**The gate is now hook-enforceable** via `scripts/pre-push`. Install once per clone:

```bash
ln -sf "$(pwd)/scripts/pre-push" .git/hooks/pre-push
```

After install, every `git push` runs the gate automatically. Hooks are NOT version-controlled (they live in `.git/hooks/`, which is not tracked); the symlink step is manual, like the existing PreCompact and SessionStart hooks. The hook honours a `GATE_CMD` env-var override so unit tests can stub the gate invocation without running the full suite — see `tests/test_gate_hook.py`. A fast local variant (`--skip-suite`) skips steps 1–2; CI runs the full gate unconditionally.

---

## Part C — Maintenance (so this doesn't ossify)

This playbook is only useful if it stays current. **After each phase's `/session-review`:** fold any new, generalizable finding into Part A/B here, and add the session-review to the evidence list below. A finding that recurs across two phases is promoted from a session-review note to a Part-B discipline. If a discipline here stops earning its keep, cut it — a bloated playbook nobody finishes reading is itself an inert artifact (hunt-question #1, applied to docs).

## Evidence (per-phase session-reviews)
- Phase 1–4: see `docs/session-state.md` per-phase sections + `.git/sdd/progress.md` history.
- Phase 5: `docs/260619_session-review-2.md` (the review that produced this playbook).
- Production Committer + Multi-Agent Test Harness (8 tasks, branch `test/multi-agent-test-harness`): `docs/260619_session-review-3.md`. Produced hunt-question #7 (property test reading its own answer key), the "meta-gate can itself be inert" note in A2, the B2 "verify the gate's pass-condition against the system's existing definition" rule, the B4 reviewer-delivery-contract item, and B6 (the pre-merge gate itself). The harness earned its keep: it surfaced two real production defects past green per-task tests — the keystone committer routing gap (3 intent types dead-lettered) and the `superseded_citations` cold-start crash.
- Failure-mode catalog: the inert-in-production taxonomy (Part A2) is the canonical hunt list; extend it as new modes appear.
