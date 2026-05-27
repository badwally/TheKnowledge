# Session state — 2026-05-26

Last updated: 2026-05-26 (Phase 7 complete — M95, exit checkpoint written)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` for ~61 synthesis pages (lint ERROR).
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.
- schema-drift: 4597 entity pages from legacy migration missing created_at/last_updated (pre-existing, not a regression).

---

## Files mid-edit

None. main is clean at m95-phase7-round-g. 1769 tests passing.
Phase 7 exit checkpoint in BUILD.md § 16.

---

## Decisions made this session

- M89: AGT-8 filter calibrator monthly cron. 1705 tests.
- M90: TOOL-11 inbox triage web view. 1716 tests.
- M91: ONT-12 tags codification. 1726 tests.
- M92: ONT-14 question page type. 1740 tests.
- M93: TOOL-10 shell completion + help examples. 1740 tests.
- M94: TOOL-15 wiki ask-corpus (thin wrapper over query() op). 1750 tests.
- M95: TOOL-16 wiki question new/list management commands. 1769 tests.
- Phase 7 exit: all S/M backlog items exhausted. Remaining backlog is L-effort or impractical.

---

## Rejected approaches

- ONT-9 (domain hierarchy): deferred — 22 MOCs manageable flat.
- QUAL-8/ARCH-12/ONT-1: deferred — all L-effort, no forcing function.
- ONT-15 (rename synthesizes → wasDerivedFrom): 282 code references + 46 wiki pages, not S effort.

---

## Next atomic step

Phase 7 is complete. Options for Phase 8:
- New feature requests from user
- QUAL-8 if a forcing function appears (LLM-heavy citation coherence)
- Source orphan discharge via `wiki query` synthesis loops (user-driven)
- Schema backfill for entity pages (created_at/last_updated on 2298+ legacy entities)
