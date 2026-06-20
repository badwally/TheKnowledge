# Backlog: same-slug deposit union — full cross-slug parity

**Status:** deferred (filed 2026-06-19, committer-test-harness build, D0 re-review NEW-1 + NEW-3).
**Current behavior (shipped, safe):** when a deposit renders to a slug whose page already exists, `author_deposit` → `_union_same_slug` unions the **net-new `- ` bullet lines** from the new body into the existing page's `## Claims` and refreshes `last_updated`. If the new body carries non-bullet structural content (preamble, new `##` sections, prose), `_union_same_slug` returns `None` → `ValueError` → the intent **dead-letters `needs-manual-merge`**. No silent data loss.

## The gap (two Minors, both fail-safe)

- **NEW-1 — body parity.** The cross-slug merge path (`_retarget_to_canonical` / `_claim_union` + the Phase-3 B1 fix) carries body, frontmatter aliases, and `## Merged context` preamble across a merge. The same-slug path only unions bullets and dead-letters on anything else. So same-slug and cross-slug merges behave **inconsistently** — same-slug is strictly more restrictive. The user's D0 decision was "union into existing page, same `_claim_union`/merge semantics as the cross-slug path"; the shipped behavior meets the no-data-loss core (dead-letters rather than dropping) but not full semantic parity.
- **NEW-3 — categorization.** `_union_same_slug` appends any `- ` line under `## Claims` regardless of which heading it appeared under in the new body. A bullet that belonged under a different section is mis-filed under Claims.

## Why deferred (not fixed now)

Both are fail-safe — no silent data loss (the restrictive cases dead-letter for manual reconciliation). Unifying same-slug and cross-slug onto one merge implementation (reuse `_claim_union`/`_retarget_to_canonical` rather than the parallel `_union_same_slug`) is the correct fix but touches the gate's merge core, which is out of the committer's task scope. D0's keystone contract (autonomous commit, no data loss, dedup/merge fires in production) is met.

## Revival trigger (any one)

1. A reader/operator complaint about a same-slug update being dead-lettered when it should have merged (structural body change on a legitimate page update).
2. The next change to the gate's merge core (`_retarget_to_canonical` / `_claim_union`) — unify the two paths in the same pass rather than maintaining a parallel `_union_same_slug`.
3. A measured rate of `needs-manual-merge` dead-letters from same-slug deposits exceeding an operational threshold.

When revived: replace `_union_same_slug` with the shared cross-slug merge semantics so same-slug deposits carry body/frontmatter/preamble identically, and file bullets under their source heading.
