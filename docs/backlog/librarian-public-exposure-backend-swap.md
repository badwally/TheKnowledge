# Backlog: Public / multi-tenant exposure and the commit-substrate swap

**Category:** Architecture / Scope evaluation
**Priority:** Low (evaluate before any external-exposure commitment)
**Effort:** Evaluation first (~half day to enumerate use cases + threat model); re-architecture is large if pursued
**Trigger to action:** A decision to expose the wiki beyond the single operator — shared access, external agents, or a hosted/public surface — OR commit-gate latency crossing its ledger alarm threshold at scale.

---

## Context

The librarian multi-agent RAG design (`docs/plans/2026-06-18-librarian-multi-agent-rag-design-prompt.md`) makes markdown canonical and the FTS/embedding indexes derived and rebuildable. This preserves optionality: the commit substrate (git today) is swappable for an embedded DB with a real WAL **without touching the knowledge model**. That swap is a separate, unevaluated problem.

## The question to evaluate (do not pre-solve)

1. **Use cases.** What would actually drive exposure beyond the single operator? Enumerate concretely (shared team corpus; external agents grounding against it; a hosted product surface; read-only public publication vs read/write). Each has a different cost.
2. **Does the serial git committer become the binding constraint?** Probably not first. The single committer has large throughput headroom for a single-operator fleet, and it scales to more writers because the gate is cheap. Under genuine public write load it *could* exceed single-committer throughput — that is where the DB-WAL swap or domain-sharded commit earns evaluation. But note: the commit-time global invariants (dedup, contradiction) are what make sharding hard (an entity spans domains), so public scale-out is a re-architecture, not a parameter change.

## Sharpening (the real trigger is the threat model, not scale)

What breaks **first** under public/multi-tenant exposure is not the commit substrate — it is the trust model. The design currently assumes originating identity is self-declared and cooperative-not-adversarial (single operator). Public exposure invalidates that and co-fires several currently-deferred items together:

- **Project/domain isolation** (deferred in design §15 — trigger was "third-party-confidential material"; public exposure is a superset).
- **Authenticated identity** (the panel flagged self-declared identity; telemetry becomes authz).
- **Rate-limiting / abuse / poison-intent defense** at the deposit gate.
- **The commit-substrate swap** (git → embedded DB + WAL) only if write throughput actually binds.

Treat "public exposure" as the single decision that activates this cluster, and evaluate them as a set, not piecemeal.

## Do NOT do now

Do not build any of this speculatively. The current architecture's value is that it does not foreclose the swap. Capture the trigger, monitor commit-gate latency (already a ledger metric), and revisit only on an explicit exposure decision.
