# Session state — 2026-05-27

Last updated: 2026-05-27 (M96 complete — schema debt clearance)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` for ~61 synthesis pages (lint ERROR).
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.
- schema-drift: 210 remaining (editorial-only: invalid entity_kind 58, missing sections 68, long slugs 50, missing canonical_name 34).

---

## Files mid-edit

None. main is clean at m96-phase8-round-a. 1777 tests passing.
Phase 8 delivery log in BUILD.md § 17.

---

## Decisions made this session

- M89–M95: Phase 7 (AGT-8, TOOL-11, ONT-12, ONT-14, TOOL-10, TOOL-15, TOOL-16). 1695 → 1769 tests.
- M96: Schema debt clearance. backfill-timestamps (2191 pages) + backfill-sources-count (99 pages). schema-drift 4597 → 210. 1769 → 1777 tests.

---

## Rejected approaches

- ONT-9 (domain hierarchy): deferred — 22 MOCs manageable flat.
- QUAL-8/ARCH-12/ONT-1: deferred — all L-effort, no forcing function.
- ONT-15 (rename synthesizes → wasDerivedFrom): 282 code references + 46 wiki pages, not S effort.

---

## Next atomic step

Phase 8 continues. Next candidates:
- M97: Broken-wikilink repair op (`wiki fix-wikilinks`) — 277 findings, partially automatable
- M98: Stale-draft abandonment policy — 224 stale drafts, auto-abandon >30 days with no inbound citations
- M99: Orphan discharge routine (`wiki routine discharge-orphans`) — batch `wiki ask-corpus` per domain
