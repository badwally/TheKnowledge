# Session state — 2026-05-26

Last updated: 2026-05-26 (M90 complete — TOOL-11 inbox web view)

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

None. main is clean at m90-phase7-round-b. 1716 tests passing.
Phase 7 delivery log in BUILD.md § 15.

---

## Decisions made this session

- Phase 6 complete: M85 (TOOL-8), M86 (AGT-7), M87 (ONT-5), M88 (ONT-7).
- ONT-8 confirmed already shipped.
- M89: AGT-8 filter calibrator monthly cron. 1705 tests.
- M90: TOOL-11 inbox triage web view. 1716 tests.

---

## Rejected approaches

- ONT-9 (domain hierarchy): deferred — 22 MOCs manageable flat.
- QUAL-8/ARCH-12/ONT-1: deferred — all L-effort, no forcing function.

---

## Next atomic step

Phase 7 continues. Candidates:
- TOOL-15 (`wiki ask-corpus <domain> "<q>"`) — S effort, hits NLM notebook_query → draft synthesis
- ONT-12 (codify or remove `tags:`) — S effort
- ONT-14 (optional `question` page type) — unknown effort
- TOOL-10 (shell completion via argcomplete) — S effort
