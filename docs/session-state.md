# Session state — 2026-05-26

Last updated: 2026-05-26 (M94 complete — TOOL-15 wiki ask-corpus)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` for ~61 synthesis pages (lint ERROR).
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.

---

## Files mid-edit

None. main is clean at m94-phase7-round-f. 1750 tests passing.
Phase 7 delivery log in BUILD.md § 15.

---

## Decisions made this session

- M89: AGT-8 filter calibrator monthly cron. 1705 tests.
- M90: TOOL-11 inbox triage web view. 1716 tests.
- M91: ONT-12 tags codification. 1726 tests.
- M92: ONT-14 question page type. 1740 tests.
- M93: TOOL-10 shell completion + help examples. 1740 tests.
- M94: TOOL-15 wiki ask-corpus (thin wrapper over query() op). 1750 tests.

---

## Rejected approaches

- ONT-9 (domain hierarchy): deferred — 22 MOCs manageable flat.
- QUAL-8/ARCH-12/ONT-1: deferred — all L-effort, no forcing function.
- Separate NLM notebook_query op for TOOL-15: not needed — query() already does this.

---

## Next atomic step

Phase 7 continues. Remaining candidates from backlog:
- ONT-15 (rename synthesizes → wasDerivedFrom): S effort, cosmetic, low priority
- QUAL-4 follow-up checks or new quality cluster
- wiki schedule list / enable / disable subcommands (schedule management UX)
