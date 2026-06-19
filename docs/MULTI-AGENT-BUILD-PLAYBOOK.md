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

General rule behind all six: **a test that builds its own fixture for the data the feature consumes proves nothing about production.** Drive the real producer (real merge, real gate commit, real recorder, genuinely-different encoder); make the negative control go RED on the pre-fix code.

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

### B3. Gate tests what ships
*(see [[feedback_gate_tests_what_ships]])* — when the traceability/spec lists a constraint the phase "lands" but the green-gate doesn't test it, that is a **gate defect**. Build + test it (add the gate row) or carve an explicit triggered-backlog item. Never silently declare it "satisfied via existing mechanisms" — that writes false green into the ledger. (Phase-5: G2/G7/I3 were listed-but-untested; reconciled by building them + adding §4 rows.)

### B4. Subagent handoff hygiene
- **File handoffs, not pasted text.** Per-task `task-brief` → implementer; report to a `.git/sdd/` file; `review-package` diff to a file. The coordinator relays status, not content — keeps the main window under its context ceiling across a long build.
- **A dispatch describes one task, not session history.** Never paste accumulated prior-task summaries into a later dispatch.
- **Subagents must NOT write `session-state.md`.** *(see [[feedback_subagents_dont_own_session_state]])* — a Phase-5 subagent committed a premature "all tasks shipped" state before reviews ran. Scope subagent reports to `.git/sdd/`; the coordinator owns and reconciles session-state, and diffs its predictions against git+tests at each seam.
- **Durable progress ledger** at `$(git rev-parse --git-path sdd)/progress.md` — tasks marked complete there are DONE; resume from it after compaction, trusting the ledger + `git log` over recollection.

### B5. Token-tactical (small, mechanical, recurring)
- **Don't wrap fast scoped commands in `timeout`** — and `timeout` is absent on darwin (it's `gtimeout`). Phase-5 wasted 3 lint calls on this.
- **Capture command output in one pass.** `eval-retrieval --compare` was run 3× because `tail -20` truncated the recall numbers; `grep -iE "Retriever:|recall@|MRR"` gets arms + metrics in one call.
- **Targeted reads over wide reads.** Opening a long `session-state.md` with a full read cost ~25k tokens for ~2k of use; `grep -n` the section, then offset-read.
- **Load deferred-tool schemas before calling** (e.g. `ToolSearch select:SendMessage`) to avoid validation-retry loops; keep `SendMessage` summaries ≤200 chars.

---

## Part C — Maintenance (so this doesn't ossify)

This playbook is only useful if it stays current. **After each phase's `/session-review`:** fold any new, generalizable finding into Part A/B here, and add the session-review to the evidence list below. A finding that recurs across two phases is promoted from a session-review note to a Part-B discipline. If a discipline here stops earning its keep, cut it — a bloated playbook nobody finishes reading is itself an inert artifact (hunt-question #1, applied to docs).

## Evidence (per-phase session-reviews)
- Phase 1–4: see `docs/session-state.md` per-phase sections + `.git/sdd/progress.md` history.
- Phase 5: `docs/260619_session-review-2.md` (the review that produced this playbook).
- Failure-mode catalog: the inert-in-production taxonomy (Part A2) is the canonical hunt list; extend it as new modes appear.
