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

## Related hardening — confine reversal/restore writes to an allowlisted subtree

**Filed by:** final security review of `test/multi-agent-test-harness` (2026-06-19, SHIP IT / 0 HIGH — this is a deferred hardening note, not a finding).

`_rel_escapes_root` (the containment guard on the deposit/reversal/policy write sinks) blocks absolute paths and `..` traversal but does **not** confine writes to `wiki/` + `.knowledge/policies/`. Verified empirically: `.knowledge/policies/foo/policy.yaml` and `.git/hooks/post-commit` PASS the guard; `../etc/passwd`, `/etc/passwd`, `wiki/../.git/config` are REJECTED. This only matters for `restore-depath` / `reverse-merge`, whose `target_rel` + `content` are fully payload-controlled — and those two have **no production producer** (reaching them requires a direct FS write to `.knowledge/intents/submitted/`, i.e. someone who could already write `.git/hooks/post-commit` directly). No escalation beyond the documented enqueue-only trust model.

**What to do when the trigger above fires** (i.e. when `restore-depath`/`reverse-merge` get a real producer op, removing the direct-FS-write precondition): add a positive-allowlist containment check that confines reversal/restore write targets to `wiki/` + `.knowledge/policies/` (reject anything else, including `.git/`), rather than relying on `_rel_escapes_root`'s non-escaping check alone. Pair it with a negative-control test that a `.git/hooks/...` target dead-letters.
