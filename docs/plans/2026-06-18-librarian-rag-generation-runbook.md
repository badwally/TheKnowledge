# Runbook — generating the Librarian multi-agent RAG design (CLI)

Operator guide for running the design-generation prompt in Claude Code. The thinking is settled and persisted; this is mechanical execution of a self-contained spec in three clean passes.

## Inputs
- Prompt: `docs/plans/2026-06-18-librarian-multi-agent-rag-design-prompt.md`
- Constraints register (authoritative, resolve every ID): `docs/plans/2026-06-18-librarian-multi-agent-rag-constraints.md`
- Deferred POR (Option B, register G1): `docs/backlog/librarian-cascade-revert-automation.md`

## Outputs
- Design doc: `docs/plans/2026-06-18-librarian-multi-agent-rag-design.md`
- Checkpoint/threshold ledger: `docs/plans/2026-06-18-librarian-multi-agent-rag-checkpoints.md`

## Why three passes
The design is 17 sections + diagrams + a failure-mode taxonomy + a full ledger. One generation truncates the novel late sections. Run each pass in its own clean window, checkpoint to `docs/session-state.md`, commit, then `/clear` and resume — the repo's standard fresh-session-per-stream discipline (CLAUDE.md § Session-state).

## Prerequisites (once, before Pass A)
- `cd ~/code/knowledge`; working tree clean (`git status`).
- Venv healthy: `.venv/bin/wiki status` runs. (If the interpreter is broken, recreate per README before starting.)
- Baseline the golden set so build work can't silently regress it: `.venv/bin/wiki eval-retrieval` and note recall@k / MRR.

## Pass sequence (paste one prompt per clean window)

**Pass A — design §0 + §§1–8**
```
Execute Pass A of the librarian RAG design generation. Read docs/plans/2026-06-18-librarian-multi-agent-rag-design-prompt.md in full, the constraints register it points to, and the codebase attachment points it names (locking.py, mcp_server.py, watcher.py, search_index.py, evaluate/). Produce ONLY design §0 + §§1–8 into docs/plans/2026-06-18-librarian-multi-agent-rag-design.md. Each component section: attachment point, extends/wraps/adds-alongside, migration deltas, inline evergreen acceptance criteria. Then checkpoint to docs/session-state.md (Pass A done; next: Pass B §§9–16) and commit. Do NOT start Pass B.
```
Then: review the §0 dependency map + phase cut, `git commit`, `/clear`.

**Pass B — design §§9–16**
```
Resume the librarian RAG design generation, Pass B. Re-read docs/session-state.md, the prompt, and the constraints register. Append design §§9–16 to docs/plans/2026-06-18-librarian-multi-agent-rag-design.md (lifecycle/retraction cascade, gap-routing, demand canonicalization, vector index, placement, deferred choices, verification model + failure-mode taxonomy with detectors and recoveries). Checkpoint to session-state (Pass B done; next: Pass C ledger + self-checks) and commit. Do NOT start Pass C.
```
Then: `git commit`, `/clear`.

**Pass C — ledger + self-checks**
```
Resume the librarian RAG design generation, Pass C. Re-read session-state, the prompt, the constraints register, and one docs/*backlog-rubric.md for structure. Write the ledger at docs/plans/2026-06-18-librarian-multi-agent-rag-checkpoints.md (thresholds with rationale+revisit-trigger+change-control, corpus-health metrics, liveness/backpressure, phase-boundary checkpoints keyed to the §0 phase names, live progress). Then run the three self-checks against the persisted files and report results: (1) classify every component into {commit-gate, typed deposit tool, demand ledger, embedding index, intent-queue mechanism, policy key} — flag any that fit none; (2) grep the design for « tokens and diff against ledger rows, printing the token list and matches; (3) a per-ID constraints-register coverage table (each ID resolved with a design §-anchor, or deferred with a trigger). Reconcile gaps, checkpoint, and commit.
```

## Close-out
- Re-run `.venv/bin/wiki eval-retrieval --compare` — confirm the golden baseline is unmoved (generation should not touch it; this is a guard).
- Sanity-read the §0 dependency map + phase cut against the body: the build plan derives from these, so they must be consistent.
- The design + ledger are now ready to derive a phased build plan (separate step).

## Troubleshooting
- **Late sections thin/truncated:** the pass was too large — split that pass further (e.g. §§9–12, then §§13–16) and resume.
- **Self-check (2) fails (orphan « keys):** add the missing ledger row or remove the stray key; keys and rows must be 1:1.
- **A constraints-register ID has no detector/recovery:** that is a defect per the prompt's success criteria — resolve before declaring the pass done.
- **Agent re-narrates the agreed architecture:** remind it the architecture block is input, not output; value-add is attachment point + migration delta + acceptance criterion.
