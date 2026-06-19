# Backlog: Unscoped `wiki lint` Is Unboundedly Slow / Effectively Hangs

**Category:** Gateway / Lint
**Priority:** Low-Medium (operational — blocks using unscoped lint as a fast gate)
**Effort:** ~2-3 hours
**Trigger to action:** Next time a phase gate or CI wants a single full-corpus `wiki lint` pass to complete in bounded time, OR when the corpus grows further. Until then, run scoped checks (`wiki lint --scope <check>`) which each complete in seconds.

---

## Problem

`wiki lint` (no `--scope`) runs all ~29 checks over the full corpus (~4000 pages).
On 2026-06-19 it ran for **1h28m without completing** and had to be killed. Running
two full lints concurrently (a mistake) made it worse, but a single full pass is
already minutes-to-unbounded because several checks do **live network I/O without a
per-check timeout** — `link-rot` HEAD-checks every external URL (733 findings),
`nlm-pending` hits the NotebookLM API, and others. One slow/unresponsive host stalls
the whole aggregate.

Each check runs FAST in isolation (verified 2026-06-19): orphans 758, schema-drift
191, broken-wikilinks 1 (the pre-existing "File name too long" OSError), link-rot
733, long-slugs 50, missing-pages 0 — all return in < 90s scoped. The aggregate is
the problem, not any single check's logic.

## Proposed Solution

- Add a per-check timeout in the lint runner so one stalled network check cannot
  hang the aggregate; report the timed-out check as `skipped (timeout)` rather than
  blocking.
- Optionally split lint into a fast tier (corpus-structure checks: orphans,
  schema-drift, broken-wikilinks, long-slugs, missing-pages — no network) and a slow
  tier (link-rot, nlm-pending — network), so a gate can run the fast tier in seconds
  and schedule the slow tier separately.
- Cache `link-rot` results with a TTL so repeated full lints don't re-hit every URL.

## Acceptance criteria

- [ ] `wiki lint` (unscoped) completes in bounded time (a stalled network check times out, does not hang the run).
- [ ] A fast structural-only lint mode returns in seconds for a CI/phase gate.
- [ ] Timed-out checks are reported explicitly (`skipped (timeout)`), never silently dropped.
