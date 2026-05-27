# Session state — 2026-05-26

Last updated: 2026-05-26 (M95 complete — TOOL-16 wiki question management)

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

None. main is clean at m95-phase7-round-g. 1769 tests passing.
Phase 7 delivery log in BUILD.md § 15.

---

## Decisions made this session

- M89: AGT-8 filter calibrator monthly cron. 1705 tests.
- M90: TOOL-11 inbox triage web view. 1716 tests.
- M91: ONT-12 tags codification. 1726 tests.
- M92: ONT-14 question page type. 1740 tests.
- M93: TOOL-10 shell completion + help examples. 1740 tests.
- M94: TOOL-15 wiki ask-corpus (thin wrapper over query() op). 1750 tests.
- M95: TOOL-16 wiki question new/list management commands. 1769 tests.

---

## Rejected approaches

- ONT-9 (domain hierarchy): deferred — 22 MOCs manageable flat.
- QUAL-8/ARCH-12/ONT-1: deferred — all L-effort, no forcing function.
- ONT-15 (rename synthesizes → wasDerivedFrom): 282 code references + 46 wiki pages, not S effort.

---

## Next atomic step

Phase 7 continues. Remaining candidates from backlog:
- QUAL-8 (citation-claim coherence): L effort, needs forcing function — skip
- Source-orphan tail: discharge via `wiki query` synthesis loops (manual/user-driven)
- Any new S/M items identified from operational use
