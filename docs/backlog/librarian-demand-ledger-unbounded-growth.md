# Backlog: DemandLedger gaps.jsonl unbounded growth + O(n²) re-cluster

**Status:** open · **Severity:** Low (resource exhaustion only; no corpus-integrity impact) · **Surfaced:** 2026-06-19 Phase-5 security review

## What

`DemandLedger.record_gap()` appends to `.knowledge/demand/gaps.jsonl` without bound, and `cluster()` reads the full file and re-derives clusters from scratch on every call (O(n²) over all gaps). `record_gap` is reachable from the read-tier `retrieve`/`answer` demand-recording seam, so a caller that floods queries grows the file without limit and makes each `cluster()` quadratic. Resource exhaustion only — no privilege or corpus-integrity impact.

## Trigger to revive

When the demand-cluster driver ships ([[librarian-demand-cluster-driver]]) OR `.knowledge/demand/gaps.jsonl` exceeds a few MB / cluster() latency becomes noticeable.

## Fix

Bound retained gaps: a rolling window (drop gaps older than the recurrence horizon), a max-line cap with compaction, and/or incremental clustering that doesn't re-read the whole file each call. Tie the bound to «demand.recurrence_mass» / cold-start horizon so dropped gaps can't have been trigger-eligible.
