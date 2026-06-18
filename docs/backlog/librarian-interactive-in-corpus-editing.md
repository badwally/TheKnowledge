# Backlog: Interactive turn-by-turn editing inside the canonical store

**Category:** Architecture / Use-case evaluation
**Priority:** Low (defer until a concrete workload demands it)
**Effort:** Unknown until a use case is named; potentially significant (cuts against the async-write model)
**Trigger to action:** A concrete agent workload that needs to build a structured artifact *inside the canonical store*, writing a piece and reading it back before writing the next, in a tight synchronous loop.

---

## Context

The librarian design makes writes asynchronous and eventually-consistent by default (producer-of-intent; the librarian enacts; read-your-writes is not guaranteed via the read tier). For everything described so far — research then deposit for the next consumer; ground on existing knowledge — this is free, because the deposit is never on the agent's critical path.

## Where it bites

It only bites if an agent wants to author an artifact turn-by-turn in the canonical store itself, reading each section back as it writes the next. The async model makes that awkward: the agent would have to carry returned content forward or block on intent status between every step.

## The current answer (and why it is probably correct)

This workload is interactive *editing*, which belongs in agent scratch space and gets deposited as a finished intent when complete — not performed live against the canonical store. The async surface is arguably the wrong tool for it by design, not by limitation.

## What to evaluate IF a real case appears

- Is the case genuinely interactive-in-canonical-store, or can it be satisfied by scratch-then-deposit?
- If genuinely needed: a synchronous read-your-writes path (design §15 already defers "stronger read-your-writes" with a trigger) — scope it then, against the real workload, not speculatively.

## Do NOT do now

No action. Recorded so the limitation is conscious, not discovered.
