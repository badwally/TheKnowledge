# Session state — 2026-05-27

Last updated: 2026-05-27 (M100 complete — Phase 9 in progress)

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

None. main is clean at M100. 1822 tests passing.

---

## Decisions made this session

- Phase 9 rubric written: docs/260527_knowledge_phase9_backlog-rubric.md
- M100: _synthesis_question quality — domain topic + source preview (abstract → excerpt → body fallback). 1812 → 1822 tests (+10).

---

## Phase 9 scope (from rubric)

| # | Item | Effort | Status |
|---|------|--------|--------|
| M100 | `_synthesis_question` quality improvement | S | DONE (commit 02716fe) |
| M101 | Multi-domain evaluation run + eval scheduling | S/M | next |
| M102 | `_parse_iso` consolidation | S | pending |

---

## Next atomic step

M101: Multi-domain evaluation run + eval scheduling.

- Run `wiki evaluate` on edge-ai-agentic and 1+ additional domains.
- Wire AGT-8-style cron for periodic eval re-runs (so eval runs on a schedule, not just manually).
- File results in BUILD.md.

Start by reading the eval op and eval framework to understand current cron wiring.
