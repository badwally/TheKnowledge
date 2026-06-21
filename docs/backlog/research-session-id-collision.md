# Backlog: `wiki research` session status overstates success on quota-failed runs

**Category:** Gateway / Research Efficiency
**Priority:** Low (was Medium) · **Effort:** ~1-2 hours
**Trigger to action:** When a research run's synthesis is wholly error stubs (e.g. NLM `RESOURCE_EXHAUSTED`) yet the session is still marked `promoted`, and lint/retry logic needs to tell real syntheses from quota casualties.

---

## RESOLVED (2026-06-21, PR — research papercuts): the re-run hard-error

The recurring pain — a re-run of the same prompt hard-erroring on session-id
collision and forcing a manual `--abandon` — is fixed. `wiki research --retry`
(`--force`) threads `force=True` to `register_session`, replacing the prior
session; on collision *without* `--retry`, `research()` now returns a clean
`OperationResult` pointing at `--retry` instead of an uncaught raise. (Acceptance
criteria 1 + 3 below are met.)

## REMAINING (criterion 2 only): status accuracy

`status=promoted` reflects **source** promotion (N sources copied into the
persistent corpus), not **synthesis** success — so a run whose synthesis was
100% `RESOURCE_EXHAUSTED` but still promoted its sources reads as `promoted`.
Distinguishing this needs the synthesis-quality signal threaded from the analysis
layer (detect an all-error-stub synthesis) into a new `failed`/`partial` terminal
status — deeper than the retry papercut, hence deferred. When built, a `failed`
session should auto-replace on re-run like `abandoned` does today.

## Problem (original)

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
