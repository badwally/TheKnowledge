"""Canonical enumeration of CommitGate reversal kinds.

Single source of truth shared by the gate dispatch (`commit_gate._apply_reversal`)
and the producer-side cross-reference test (`test_inert_invariants`). Each value
is a `payload["reversal_type"]` a producer op enqueues and the gate applies:

- ``contradiction-resolution`` — ``ops/revert_resolution`` → ``_apply_contradiction_revert``
- ``depath``                   — ``ops/remediate``         → ``_apply_depath``
- ``restore-depath``           — ``ops/reverse_merge``     → ``_apply_restore_depath``
- ``reverse-merge``            — ``ops/reverse_merge``     → ``_apply_reverse_merge``

Adding a value here without a gate handler (or vice versa) is a defect the
inert-invariant cross-reference test surfaces (hunt #1).
"""

from __future__ import annotations

REVERSAL_TYPES: frozenset[str] = frozenset(
    {
        "contradiction-resolution",
        "depath",
        "restore-depath",
        "reverse-merge",
    }
)
