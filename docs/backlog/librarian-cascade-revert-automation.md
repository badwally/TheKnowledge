# Backlog: Automatic transitive cascade-revert (Option B) — Plan of Record, deferred

**Category:** Architecture / Governance
**Priority:** POR (plan of record) — committed direction, deferred build
**Effort:** Large (the highest-blast-radius subsystem in the design)
**Depends on:** Option A — the `revert-resolution` primitive and complete decision-basis recording — both built in the initial design.
**Trigger to action:** Any of the measured signals crossing its ledger threshold — auto-resolution-reversal rate, cross-project-override rate, or observed cascade-depth — i.e., bad auto-resolutions becoming frequent or deep; OR public / multi-tenant exposure (see `librarian-public-exposure-backend-swap.md`).

---

## Decision

The librarian auto-resolves contradictions by policy rule (trust-tier precedence, then recency) over an OPEN shared corpus. A wrong auto-win — or a correct win whose source is later retracted — can silently poison another project's grounding and compound through the synthesis graph. The initial build ships **Option A**: a provenanced `revert-resolution` primitive (un-suppress the loser, re-open the edge, re-run the rule) plus detectors and metrics that make every poison discoverable and every single node fixable with one command. Deep cleanup under A is hands-on: the detectors surface downstream dependents from the provenance graph, but the operator reverts each layer.

**Option B — automatic transitive cascade-revert — is the plan of record, deferred.** On revert (or on retraction of a winning source), the system walks the operational-provenance graph, finds every downstream resolution and synthesis page that depended on the changed claim, and re-evaluates them to a fixpoint, bounded by the graph rather than the whole corpus.

## Why deferred (not rejected)

- **No evidence of need yet.** Single-operator fleet; bad-resolution volume and depth are expected to be low and shallow, and the operator is in the loop. A's metrics (reversal rate, override rate, cascade depth) are precisely the instrumentation that will tell us whether B is warranted — build it on data, not speculation.
- **A → B is additive, not a rewrite.** A builds the reversal primitive and the decision-basis recording B sits on top of. Choosing A does not foreclose B; it sequences it behind a measured trigger. Same preserved-optionality logic as the commit-substrate swap.
- **B is the riskiest thing to build early.** It requires a complete, queryable dependency record on every resolution and synthesis, a correct re-evaluation/re-authoring engine, termination and cycle handling, and it competes as a large multi-entity write at the commit gate. A buggy cascade-revert is itself a corruption vector. YAGNI and the start-boring restraint both say wait.

## What B adds over A

One command self-heals the corpus to any depth after a bad win or a retracted winner, with no manual layer-by-layer cleanup. This is the answer for many concurrent writers you cannot trust to clean up by hand — the eventual multi-tenant world, not today's single operator.

## Do NOT do now

Build A (primitive + detectors + metrics). Watch the metrics. Revisit B when they cross threshold or on an exposure decision.
