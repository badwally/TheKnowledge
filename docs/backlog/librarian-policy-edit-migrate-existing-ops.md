# Backlog: Migrate existing domain ops onto the policy-edit channel

**Status:** deferred — triggered backlog  
**Added:** 2026-06-19 (T6 / Phase 5 gate)  
**Constraint IDs:** G7 migration delta

---

## What this is

The three existing domain ops write `policy.yaml` directly to disk without
routing through the privileged CommitGate intent path:

| Op | File | Write point |
|----|------|-------------|
| `bootstrap_domain` | `src/gateway/ops/bootstrap_domain.py` | `target.write_text(...)` |
| `promote_domain` | `src/gateway/ops/promote_domain.py` | direct `policy_path(slug).write_text(...)` |
| `demote_domain` | `src/gateway/ops/demote_domain.py` | direct policy file deletion |

These direct writes will be flagged by `wiki lint --scope policy-provenance`
immediately, because they leave no `policy-edit` provenance node.

## Why deferred

Migrating these ops is a named "migration delta" in the Phase 5 spec (§ Scope
boundary). The regression risk is real: all three ops are live production paths
used in every domain bootstrap and domain promotion workflow. Cutting them over
to the policy-edit intent path requires:

1. Each op must enqueue a `policy-edit` CommitGate intent instead of writing
   directly — meaning the domain must exist before the first policy is written
   (currently bootstrap creates the policy file as its primary output).
2. The CommitGate worker must be running (not a concern for the normal flow,
   but a sequencing dependency that does not exist today).
3. The gate (`eval-retrieval --compare` + `merge_map_eval`) must complete
   within acceptable latency for an interactive CLI op.

## Trigger conditions (revival signals)

Activate this backlog item when **any** of the following occurs:

- **Next substantive edit to `bootstrap_domain.py`, `promote_domain.py`, or
  `demote_domain.py`** — any meaningful change to those files is the natural
  seam to also migrate them onto the change-control path.
- **First out-of-band policy edit flagged by `wiki lint --scope policy-provenance`
  in production** — indicates a real out-of-band edit occurred and the gap
  between the lint signal and the enforced gate is non-zero.

## Migration plan (when triggered)

1. **`bootstrap_domain`**: After generating the policy content (the LLM call),
   enqueue a `policy-edit` intent rather than writing to disk. The intent
   carries the generated policy as `policy_data`. The CommitGate worker applies
   the gate. The CLI caller polls `wiki_intent_status` for the terminal
   disposition. If the gate dead-letters (regression), surface the metric to
   the user.

2. **`promote_domain`**: Same pattern — enqueue `policy-edit` for the promoted
   domain's policy. Since promote is already a multi-step op (tag sources, write
   policy, write MOC), the intent becomes the final step.

3. **`demote_domain`**: Deletion of a policy is currently a direct `unlink`.
   Model as a `policy-edit` with `policy_data = {}` (empty = mark deleted) or
   add a `policy-delete` typed intent variant if the CommitGate needs to
   distinguish. Either way, it must route through the gate and record provenance.

4. **Content-hash provenance**: The current `policy_provenance` lint detects the
   ABSENCE of a node but does not verify the node was recorded for the current
   file content. Add a `policy_content_hash` field to the provenance basis (SHA-256
   of the YAML content at write time) and update the lint to compare it against
   the on-disk hash. This closes the "node exists but content drifted" gap.

## Notes

- Hardcoded threshold constants (`commit_gate.py:COMMIT_LOCK_ACQUIRE_TIMEOUT`,
  `deposit.py:MAX_BACKLOG`) are NOT in scope for this migration. They are gated
  by code-review and merge, not the runtime policy-edit path. This is documented
  in `lint/policy_provenance.py` and `ops/policy_edit.py`.
- The existing 16 domains that produce policy-provenance findings today are
  legacy — they predate the change-control gate and can be cleaned up as part
  of the migration or suppressed with a one-time provenance backfill.
