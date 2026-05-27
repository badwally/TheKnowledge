# Session state — 2026-05-27

Last updated: 2026-05-27 (M99 complete — Phase 8 complete)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` for ~61 synthesis pages (lint ERROR).
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.
- schema-drift: 225 remaining (all editorial-only: invalid entity_kind, missing sections, long slugs, missing canonical_name — requires per-entity human review).
- broken-wikilinks: 82 remaining (all WARNINGs — forward-references to entity/concept pages not yet authored).

---

## Files mid-edit

None. main is clean at m99-phase8-round-d. 1812 tests passing.
Phase 8 exit checkpoint written in BUILD.md § 18.

---

## Decisions made this session

- M96: Schema debt clearance (4597 → 225 schema-drift). 1777 tests.
- M97: Broken-wikilink repair (277 ERRORs → 82 WARNINGs). 1789 tests.
- M98: Stale-draft auto-abandonment (wiki abandon-stale-drafts, >30d + no inbound citations). 1800 tests.
- M99: Orphan discharge routine (wiki routine discharge-orphans --domain --limit). 1812 tests.
- Phase 8 exit checkpoint: criteria 2+3 met; schema-drift criterion not met (225 editorial tail, not automatable).

---

## Next atomic step

Phase 9 to be scoped. Candidates from BUILD.md § 18 carry-forward:
- Editorial schema-drift: 225 items (entity_kind reclassification, missing sections, long slugs) — tooling to assist human review
- QUAL-8: citation-claim coherence judge (needs forcing function)
- ONT-11: backfill-synthesizes for 61 synthesis pages (user-action, not engineering)
- Source-orphan discharge: run wiki routine discharge-orphans on each domain

Await user direction.
