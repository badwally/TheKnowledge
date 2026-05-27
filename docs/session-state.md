# Session state — 2026-05-26

Last updated: 2026-05-26 (M91 complete — ONT-12 tags codification)

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

None. main is clean at m91-phase7-round-c. 1726 tests passing.
Phase 7 delivery log in BUILD.md § 15.

---

## Decisions made this session

- M89: AGT-8 filter calibrator monthly cron. 1705 tests.
- M90: TOOL-11 inbox triage web view. 1716 tests.
- M91: ONT-12 tags codification (keep as list[str], validator + lint). 1726 tests.

---

## Rejected approaches

- ONT-9 (domain hierarchy): deferred — 22 MOCs manageable flat.
- QUAL-8/ARCH-12/ONT-1: deferred — all L-effort, no forcing function.
- TOOL-15 (wiki ask-corpus): deferred — NLM notebook_query op doesn't exist yet.

---

## Next atomic step

Phase 7 continues. Remaining S/M candidates:
- ONT-14 (optional `question` page type) — new page type with status field
- TOOL-10 (shell completion via argcomplete) — docs + setup, no gateway logic
- TOOL-15 (wiki ask-corpus) — blocked on NLM notebook_query op
