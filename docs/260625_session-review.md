# Session review — 2026-06-25 (RAG Hole-2 hybrid activation → merged)

Scope: this session resumed from `/clear` + continuation prompt and completed the Hole-2 hybrid-retrieval activation. Two authored commits — `f206543c` (w=2 bake + hybrid default-ON + D1 carry-forward) and `f383ea95` (production-activation gap: config-file encoder default + dim/embed guard + test insulation) — plus a production 4B index rebuild, probe re-score, two green gate runs, and **PR #61 merged to main `df271bd7`** (merge 2026-06-26 01:43 UTC). No subagent or gateway-LLM calls this session; work was direct edits + background rebuild.

Changeset (this session): 9 files, +267/−17. Src: `ops/retrieve.py`, `retrieval_encoder.py`, `retrieval_index.py`. Config: `.knowledge/retrieval.yaml`. Tests: `test_ws2_retrieve.py`, `test_retrieval_encoder.py`, `test_retrieval_index.py`, `conftest.py`. Full suite 2637 → 2643.

---

## § 1 — Code and coding quality

**[High] Draft gate is only half-applied in the hybrid path — `include_drafts` is honored on the lexical leg but the dense leg ignores it.** `src/gateway/ops/retrieve.py:215-240`, `src/gateway/retrieval_index.py:dense_section_hits`. `_hybrid_hits` now threads `include_drafts` into `search_fts` (the carry-forward fix), but `dense_section_hits(query, k*2)` has no draft awareness — its hits are only *placeholder*-gated downstream (`is_placeholder_section`), not *draft*-gated. So a caller passing `retrieve(q, include_drafts=False, hybrid=True)` still gets substantive draft sections back via the dense leg, silently violating the opt-out. Currently dormant because the default is `include_drafts=True` (Hole-1 decision), but it is a latent correctness asymmetry and a trap for any future exclude-drafts caller. **Fix:** filter dense hits by the page's `draft` flag when `include_drafts=False` (the `dense_meta`/`by_id` hits already carry page metadata — gate there before fusion), and add a test: `include_drafts=False, hybrid=True` admits no draft section from either leg. The docstring currently *documents* the gap ("dense hits are content-gated downstream") rather than closing it.

**[Medium] Broad `except Exception` around the encoder embed can mask genuine encoder bugs as silent lexical-only degradation.** `src/gateway/retrieval_index.py:67-75`. The catch-all is the right resilience posture for "mlx absent / model fails to load," but it also swallows logic errors inside a real encoder (a bad tensor op, an API drift in `mlx_embeddings`) — they degrade to lexical-only with a single WARNING rather than surfacing. The warn-once dedup makes it quieter still. It is *logged*, so not fully silent, and `except Exception` correctly leaves `KeyboardInterrupt`/`SystemExit` uncaught. Acceptable trade-off, but worth a code comment that this deliberately trades fail-loud for serve-degraded, and consider a counter/metric so repeated degradation is visible in aggregate, not just one log line.

**[Low] `_DENSE_WARNED` warn-once dedup is untested.** `src/gateway/retrieval_index.py:16, 68-83`. The two guard tests assert `hits == []` (the load-bearing contract — good, and the dim guard is teeth-verified by mutation), but nothing exercises the warn-once keying. A mutation that always-warns or never-warns, or that collides the `("dim", …)` / `("embed", …)` key namespaces, passes green. Logging isn't load-bearing, so Low — but a `caplog`-based assertion (warns once across two calls, again after `.clear()`) would close it. Note the tests already depend on `_DENSE_WARNED.clear()` for isolation, so the symbol is effectively part of the test contract.

**[Low] Lazy `import yaml` / `from gateway import paths` inside `_resolve_encoder_spec` drifts from codebase convention.** `src/gateway/retrieval_encoder.py:91-99`. `yaml` is a hard project dependency imported at module level elsewhere (`bakeoff.py`, `scheduler.py`), and `paths` has no import cycle with `retrieval_encoder`. The in-function imports add no safety and read as defensive boilerplate. Top-level imports would match the surrounding modules. Trivial.

**Checked and clean:** the w=2 default is pinned by a dedicated test so a change is deliberate; the hybrid default-flip was blast-radius-tested (full suite 2643, no regressions); the dim guard is teeth-verified by mutation; the config resolver has precedence + malformed-config + fallback tests; the autouse stub fixture is a behavioral no-op today (env-unset already meant stub) so it cannot mask existing assertions. No dead code, no commented-out blocks introduced.

---

## § 2 — Token efficiency

**`nohup` detour on the background rebuild — ~3 excess tool calls + a discarded warmup.** I first launched the 159-min rebuild via `nohup … &` inside a `run_in_background` Bash, then realized the harness tracks only the *launcher* (which exited immediately), not the detached `nohup` child — so no completion notification would fire. I killed PID 32798 and relaunched the script directly as a `run_in_background` Bash (harness-tracked). Cost: the nohup launch, the kill, a re-verify, and a repeated 3.4s model warmup. **Avoided by:** the precondition that `run_in_background` already detaches and notifies — `nohup` is redundant and actively breaks tracking. Launch long jobs directly via the background tool, no `nohup`. (Memory-atom candidate below.)

**Full suite ran ~4×; ~2 standalone runs were redundant with the gate's Step 1.** After each commit I ran `pytest tests/` (52s) *and then* `gateway.scripts.gate` (which re-runs the full suite). The standalone runs gave faster pre-commit feedback (52s vs ~2-min gate), which is defensible — but running the standalone suite *immediately* before a gate run on the same tree duplicates Step 1. ~1–2 redundant full-suite executions (compute/wall-time, not tool calls). **Cheaper:** commit on the fast standalone green, run the gate once as the final merge bar — or skip the standalone when the next action is the gate anyway.

**Generally efficient elsewhere:** initial orientation batched (session-state Read ∥ git-status Bash in one turn); reads were targeted greps + section-reads, not full-file dumps; the pre-edit reads of `retrieval_encoder.py`/`retrieval_index.py` were genuine "verify before asserting the prod hazard," not waste; the rebuild status polls were user-requested ("status"), not self-inflicted.

---

## § 3 — Prompt and context engineering

**Strongest lesson — the production-activation gap surfaced one prompt *after* the first PR, not at the default-flip that caused it.** When I flipped `hybrid=False→True` (commit `f206543c`) and opened PR #61, the gate was green and I reported done. Only when the user asked "what's the best next step" did I reason that the production index is 2560-dim (4B) while the default encoder is the 256-dim stub → `mat @ qv` crashes in prod, invisible to a gate that runs stub-on-stub. The facts were all in context at the flip; the audit fired late, costing a second commit, a second gate run, and a PR-comment round. **The check "does this default-flip have production-only preconditions the gate can't see?" should fire AT the moment of making a path the default**, not after. This is the [[feedback_inert_in_production_pattern]] / [[feedback_gate_tests_what_ships]] lesson at a sharper trigger. (Memory-atom candidate.)

**Context seeding prevented a CI-breaking design.** The session-state gotcha "do NOT hard-default the mlx 4B encoder in code — breaks every stub-based CI test" was loaded before I designed the config-file default, so the resolver came out env-`>`-config-`>`-stub with an autouse stub fixture, not a hard 4B default. Rework avoided by reading the constraint first. Good.

**Drift detection win.** Caught that the branch name `feat/hole2-0.6b-activation` was a surface-anchor misnomer (model locked to 4B) and named the PR branch `feat/hole2-hybrid-activate-4b` accurately — [[feedback_general_purpose_inherits_surface_anchors]] applied to a branch label.

**Session continuity validated.** The `/clear` + continuation-prompt resume worked with zero re-derivation: session-state's "next atomic steps" were precise enough to execute directly, and the open-contracts-vs-tree verification at start caught nothing amiss. No boundary rework — a clean datapoint for the session-state discipline.

**AskUserQuestion quality.** Three decision-gated questions (concurrency handling, activation mechanism, cleanup ownership) were each scoped to a genuine fork with a recommended-first option; each returned a clean, actionable choice with no follow-up clarification. No over-asking (the w=2 value and 4B lock were already settled, so I didn't re-ask them).

---

## § 4 — Session-state checkpoint

- **Status:** Hole-2 hybrid retrieval **DONE + MERGED** — PR #61 → main `df271bd7` (merge 2026-06-26 01:43 UTC). Both remote feature branches deleted; no `hole2` branches remain on origin.
- **Verified working now:** model locked **4B-4bit-DWQ (2560-dim)**; `_DENSE_RRF_WEIGHT=2.0`; hybrid default-ON; `include_drafts` threaded through `_hybrid_hits`; config-file encoder default + dim/embed guard + autouse stub fixture; production 4B index rebuilt (4034 pages / 19,317 vectors / 166 min); probe re-score **hybrid@10 0.857, @20 0.905, 0 leaks**; full suite 2643; pre-merge gate PASSED twice.
- **Open contract (deferred by user to a main-checkout session):** main checkout `~/code/knowledge` sits at local-only commit `157524bc` (journal reconcile, unpushed) while origin/main is `df271bd7` (based on `8cef137c`) — a `git pull` there is a merge across a divergence (no session-state conflict expected; #61 never touched `session-state.md`). Run IN `~/code/knowledge`: `git fetch origin && git pull --no-rebase origin main`; fold this session's Hole-2-DONE journal section into that checkout's `docs/session-state.md` + commit (main-checkout only); `git worktree remove ../knowledge-wt-rag-draft-visibility` (`--force` discards this worktree's uncommitted journal edit — transplant first).
- **Activation timing:** the 4B encoder activates in the main checkout only once `~/code/knowledge/.knowledge/retrieval.yaml` lands there via the pull; until then it resolves to stub → dim-guard → lexical-only (safe, not a crash).
- **Decisions (one-line why):** 4B over 8B (8B gain within quant noise + 2-4× ingest tax, recall@10 unmoved by an optimistic 8B rerank test); w=2 (robust knee, easy goldens un-regressed); guard+config-file activation (durable prod default without per-shell export, CI stays stub); new PR branch not force-push (stale shared remote, classifier-blocked force, user defers to branch+PR).
- **Rejected:** running 8B to completion; reviving the reranker (HARMS); hard-defaulting 4B in code (breaks CI); force-pushing the stale shared remote; committing `session-state.md` on the feature branch.
- **Next atomic step:** none blocking — Hole-2 is shipped. The main-checkout housekeeping above, then (separate fresh session) **Hole-3 curation**: lay-vocab content-enrich the 2 short draft pages `reward-deficit-and-anhedonia` + `mesolimbic-dopamine-system-modulation` (real fix for the 2 residual flat-at-all-k probe misses); broader perma-draft finalize/cull.

---

## § 5 — Memory-atom candidates (proposal, gated)

### Candidate A

```markdown
---
name: feedback_audit_prod_preconditions_at_default_flip
description: when flipping a code path to default-ON, immediately audit its production-only preconditions the CI gate can't see
metadata:
  type: feedback
  scope: global
  confidence: high
  domain: testing
  evidence: "2026-06-25 — flipped retrieve hybrid=False→True; the 2560-dim prod index vs 256-dim stub default crash surfaced a PR late, invisible to a stub-on-stub gate"
---
**Trigger:** when a change makes a previously-opt-in path the default (a `default=False→True` flag, a new default branch, an always-on feature).
**Action:** before reporting done, audit that path's production-only preconditions — env vars, model/index dimension match, deployment config, file presence — that the CI gate runs on stubs/fixtures and therefore structurally cannot exercise.
**Why:** the gate green on stub-on-stub fixtures says nothing about a prod-only mismatch (e.g. a 2560-dim index against a 256-dim stub encoder crashes the matmul). The facts are usually already in context at the flip; the audit just has to fire there, not a prompt later.
**How to apply:** at the default-flip, ask "what does this path now require at runtime that the test fixtures don't provide?" Add a guard that degrades safely on mismatch AND a config/deployment seam that supplies the real precondition; drive both with a test that forces the mismatch.
[[feedback_inert_in_production_pattern]] [[feedback_gate_tests_what_ships]]
```

### Candidate B

```markdown
---
name: feedback_no_nohup_for_tracked_background_jobs
description: launch long background jobs via the harness background tool directly, never wrapped in nohup
metadata:
  type: feedback
  scope: global
  confidence: high
  domain: orchestration
  evidence: "2026-06-25 — wrapped a 159-min rebuild in nohup inside run_in_background; harness tracked only the launcher, no completion notification fired; had to kill + relaunch"
---
**Trigger:** when starting a long-running job you want a completion notification for.
**Action:** launch the command directly with the harness `run_in_background` option; do NOT wrap it in `nohup … &`.
**Why:** `run_in_background` already detaches and re-invokes the agent on exit. Wrapping in `nohup` detaches the real work into an orphan the harness can't see, so the tracked "launcher" exits immediately and no completion event ever fires — forcing a kill + relaunch (and a discarded warmup).
**How to apply:** `Bash(command=<the job>, run_in_background=true)` with the bare command. Reserve `nohup` only for jobs that must outlive the whole session intentionally and that you'll poll for by hand.
```

Both are durable and evidence-backed this session. Candidate A is a refinement/sharper-trigger sibling of two existing atoms (cross-linked, not a duplicate); Candidate B is a clean new tooling lesson. Awaiting approval before writing.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Code (High) | Hybrid dense leg ignores `include_drafts` — draft gate half-applied | Draft-gate dense hits when `include_drafts=False`; add the `hybrid=True, include_drafts=False` exclusion test |
| 2 | Prompt/context | Prod-activation gap found a PR late, not at the default-flip | Adopt Candidate A: audit prod-only preconditions at the moment of any default-flip |
| 3 | Tokens | `nohup` broke harness tracking → kill+relaunch | Adopt Candidate B: bare command via `run_in_background`, no `nohup` |
| 4 | Code (Med) | Broad `except` masks real encoder bugs as silent degrade | Comment the fail-loud→serve-degraded trade-off; add a degradation counter/metric |
| 5 | Code (Low) | Warn-once `_DENSE_WARNED` dedup untested | Add a `caplog` test: warns once, re-warns after `.clear()` |
