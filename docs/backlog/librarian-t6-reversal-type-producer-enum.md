# Backlog: Canonical reversal_type enum for producer-side cross-reference

**Filed by:** T6 inert-invariants review (2026-06-19)
**Revival trigger:** Next time any producer op (`remediate.py`, `revert_resolution.py`, or a new op) is modified to add or rename a `reversal_type` value, OR when a new reversal_type is added to `commit_gate._apply_reversal`.

## What this covers

`reverse-merge` and `restore-depath` have no dedicated producer op — they are only written as gate-internal provenance keys inside `commit_gate._commit_reversal_writes()` (after a successful depath or merge commit). No external caller submits them via `IntentQueue.submit()` with these `reversal_type` values in the payload.

As a result, the T6 Step-5 cross-reference parametrize (`test_producer_reversal_type_has_gate_apply_branch`) covers only `"contradiction-resolution"` and `"depath"` — the types with real producer ops. `"reverse-merge"` and `"restore-depath"` are guarded only by the Step-3 per-branch dead-letter tests.

## What to do when the trigger fires

1. Add a `REVERSAL_TYPES` constant (frozenset or enum) in a shared location — e.g. `gateway/ops/_reversal_types.py` — listing all four values:
   ```python
   REVERSAL_TYPES = frozenset({
       "contradiction-resolution",
       "depath",
       "restore-depath",
       "reverse-merge",
   })
   ```
2. Import `REVERSAL_TYPES` in:
   - `commit_gate._apply_reversal()` — replace the if/elif chain with a dispatch dict keyed on this set.
   - `tests/integration/test_inert_invariants.py:_producer_reversal_types()` — replace the source-grep with `sorted(REVERSAL_TYPES)`.
3. The T6 Step-5 parametrize then covers all four types from a single authoritative source. Adding a type to `REVERSAL_TYPES` without a gate handler makes the test go RED immediately (hunt #1).

## Why this was deferred

The missing canonical constant is a convenience/coupling issue, not a correctness defect. The per-branch containment tests in Step 3 (`test_gate_dead_letters_*`) cover all four branches independently. The gap is that adding a new reversal_type without a gate handler does not auto-fail a test until the enum exists.
