# Backlog: DemandLedger.cluster() has no production driver

**Status:** partially resolved (manual driver shipped; scheduled driver deferred) · **Severity:** Low (was Important — the decision-11 loop can now be driven on demand) · **Surfaced:** 2026-06-19 Phase-5 whole-branch review (I1) · **Updated:** 2026-06-20 (committer/test-harness build, task D1)

## Resolved by D1 (manual driver)

Task **D1** (`wiki demand-cluster`, commits `6b020a74` + `599130c2` + `5094831c`, merged to `main` in PR #35) shipped the build-tier CLI driver:
- `wiki demand-cluster` (no flag) = report-only: clusters gaps and prints qualifying clusters, submits nothing.
- `wiki demand-cluster --trigger` = submits exactly one canonicalization (synthesis) CommitGate intent per qualifying cluster, to the correctly-rooted production queue.

`DemandLedger.cluster()` now has a real production caller. The loop is no longer "documented-but-dead" — an operator (or any build-tier agent) can run it on demand. Verified end-to-end in T2 integration tests.

## What remains (scheduled/automatic driver)

The **automatic** half is still deferred: nothing invokes `wiki demand-cluster --trigger` on a cadence, so in a running system with no operator action, gaps still accumulate and the canonicalization trigger never fires on its own. This is the same gate as the committer daemon — see [[librarian-committer-daemon-install.md]] (Option B scheduler-cron preferred). Wiring it is a one-line scheduler entry once that decision lands.

## Trigger to revive (the scheduled driver)

Either of:
- `.knowledge/demand/gaps.jsonl` accumulates ≥ «demand.recurrence_mass» (5) occurrences of any single clustered gap (i.e. there is real demand to canonicalize) and no operator is running `wiki demand-cluster --trigger`, OR
- the next time the scheduler (`com.knowledge.scheduler`) is installed/touched — add a `demand-cluster --trigger` cadence entry at the same time.

## Fix (remaining)

Wire `wiki demand-cluster --trigger` into the scheduler on a cadence. Bound the work (see [[librarian-demand-ledger-unbounded-growth]]). The CLI driver and the end-to-end "recurring gap → exactly one synthesis intent" path are already built and tested (D1 + T2); only the cadence trigger is outstanding.
