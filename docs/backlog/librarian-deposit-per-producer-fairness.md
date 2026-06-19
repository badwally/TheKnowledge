# Backlog: Deposit Backlog Ceiling Has No Per-Producer Fairness

**Category:** Gateway / Librarian (Phase 4 — deposit consumer contract)
**Priority:** Medium
**Effort:** ~2-3 hours
**Trigger to action:** When more than one independent producer identity deposits concurrently in production (multi-tenant / multi-agent fan-out where one producer's volume could starve another). Until then the single-producer behavior is correct and this is latent.

---

## Problem

`ops/deposit.py` sheds load when `IntentQueue.depth() >= MAX_BACKLOG` (256).
`depth()` (`intent_queue.py:383-388`) counts **all** `submitted/*.json` globally with
no producer attribution, and `MAX_BACKLOG` is a single shared global. One producer
submitting 256 distinct deposits (distinct payloads bypass the content-addressed
dedup) wedges the queue at the ceiling and **denies all other producers** until the
serial committer drains it.

Surfaced by the Phase-4 independent security review (2026-06-19, Finding 2, Medium).
It requires deposit (build-tier) privilege, so it is a privileged-producer-vs-
privileged-producer **fairness** gap, not an unprivileged escalation — hence Medium,
not High. `depth()`'s `glob("*.json")` does not follow symlinks and excludes the
queue's own `.{name}.json.*.tmp` atomic temp files, so the count itself is not
inflatable by the queue machinery.

## Proposed Solution

Track per-producer-identity depth and shed per-producer, e.g. a per-identity
sub-ceiling `ceil(MAX_BACKLOG / active_producers)` in addition to (not instead of)
the global ceiling. The producer identity is already on the deposit (`identity`
dict). Add a `«deposit.max_backlog_per_producer»` ledger key alongside the existing
`«deposit.max_backlog»` (global) key.

## Acceptance criteria

- [ ] A single producer cannot push the queue past its per-producer sub-ceiling while other producers still get `queued`.
- [ ] The global ceiling still applies (aggregate protection).
- [ ] Negative control: a lone producer below its sub-ceiling still queues normally.
- [ ] Adversarial test: producer A floods to its sub-ceiling; producer B's deposit still returns `queued`, not `rejected:overloaded`.
