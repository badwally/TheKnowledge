# Backlog: reverse-merge / restore-depath reversal kinds have no producer op

**Status:** open · **Severity:** Important (recovery affordance is gate-ready but not operator-reachable) · **Surfaced:** 2026-06-19 Phase-5 whole-branch review (I2)

## What

The CommitGate `_apply_reversal` dispatch handles four reversal kinds. Two are reachable end-to-end through a gateway op; two are not:
- **Reachable:** `depath` (from `ops/remediate`), `contradiction-resolution` (from `ops/revert_resolution`).
- **No producer op:** `reverse-merge` (G8 — restore a canonical from the recorded B-only reattachment set + delete the tombstone) and `restore-depath` (re-create a de-pathed page from recorded content). The apply helpers + `reverse_merge_plan` exist and are tested through a hand-built intent, but no CLI/MCP op submits these.

G8 reverse-merge restoration is a manual/recovery affordance; the gate machinery is correct and reachable via a hand-built intent. It is not wired to an operator command.

## Trigger to revive

The first time a merge needs to be undone in practice (a bad dedup merge is observed and must be reversed), OR when building any operator-facing "undo" surface.

## Fix

Add a build-tier CLI op (e.g. `wiki reverse-merge <tombstone>` / `wiki restore-depath <rel>`) that submits the corresponding reversal intent. NOTE the SEC-High guard already landed: `_commit_reversal_writes` rejects `..`/absolute/out-of-root rels for all reversal kinds, so a caller-supplied `tombstone_rel` is contained — but add the named traversal negative-control test for the new producer at its own layer too.
