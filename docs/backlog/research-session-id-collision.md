# Backlog: `wiki research` Re-Run Collides on Session ID

**Category:** Gateway / Research Efficiency
**Priority:** Medium
**Effort:** ~2-3 hours
**Trigger to action:** Any retry of a research query whose synthesis failed (e.g. NLM `RESOURCE_EXHAUSTED`) and needs regeneration

---

## Problem

`wiki research "<prompt>"` derives the session ID deterministically from the
prompt's leading words. Re-running the same (or a similar) prompt — the normal
thing to do when the first run's synthesis failed on quota — collides with the
already-registered session and aborts before doing any work. The operator must
manually run `wiki research --abandon <session-id>` first, which requires
knowing the exact derived ID.

This violates the idempotent-and-convergent ops principle: re-running a *failed*
op should converge, not hard-error.

## Evidence

```
ValueError: session '2026-05-30-what-sets-the-ceiling-on-representational'
already registered for domain 'convergent-ai-brain' (status=promoted);
abandon it first or pass force=True
```

The prior session carried `status=promoted` even though its synthesis was 100%
`RESOURCE_EXHAUSTED` (zero usable pages) — so "promoted" overstates success and
blocks the obvious retry.

## Proposed Solution

Pick one (or combine):

1. **Auto-suffix** the session ID on collision (`...-r2`, `...-r3`).
2. Expose the `force=True` path as a CLI flag (`--retry` / `--force`).
3. **Auto-converge:** if the colliding session produced zero non-error synthesis
   pages, abandon-and-recreate automatically instead of erroring.

Option 3 is the most aligned with the convergent-ops rule; (1) or (2) are cheap
stopgaps. Separately, `status=promoted` should not be set when every synthesis
page is an error stub — add a `status=failed` (or `partial`) terminal state so
lint/retry logic can distinguish real syntheses from quota casualties.

## Acceptance criteria

- [ ] Re-running a failed research query does not hard-error on session-ID collision
- [ ] A session whose synthesis wholly failed is not marked `status=promoted`
- [ ] Operator can retry without manually looking up and abandoning the session ID
