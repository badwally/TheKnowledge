# Backlog: DemandLedger.cluster() has no production driver

**Status:** open · **Severity:** Important (decision-11 loop is documented-but-dead until wired) · **Surfaced:** 2026-06-19 Phase-5 whole-branch review (I1)

## What

The demand loop is schema-closed but driver-open:
- **Producer (live):** `ops/retrieve.py` / `ops/answer.py` record a corpus-miss gap via `DemandLedger.record_gap()` → `.knowledge/demand/gaps.jsonl` (gitignored). Schema/path match what `cluster()` reads.
- **Consumer (no caller):** `DemandLedger.cluster()` — which clusters gaps, applies cold-start + recurrence-mass gating, and submits exactly one canonicalization (synthesis) CommitGate intent per qualifying cluster — is invoked only by tests. No CLI subcommand, scheduler hook, or poller calls it in production. Gaps accumulate forever; the canonicalization trigger never fires in a running system.

This is the "passes unit tests, inert in production" pattern that recurred across Phase 5 — here it is scoped (T4 built the mechanism, not a driver) so it is a tracked follow-up, not a Phase-5 gate failure.

## Trigger to revive

Either of:
- `.knowledge/demand/gaps.jsonl` accumulates ≥ «demand.recurrence_mass» (5) occurrences of any single clustered gap (i.e. there is real demand to canonicalize), OR
- the next time the scheduler (`com.knowledge.scheduler`) is installed/touched.

## Fix

Add a `wiki demand-cluster` CLI subcommand (build-tier) that calls `DemandLedger.cluster()`, and/or wire `cluster()` into the scheduler on a cadence. Bound the work (see [[librarian-demand-ledger-unbounded-growth]]). Verify a recurring gap triggers exactly one synthesis intent end-to-end.
