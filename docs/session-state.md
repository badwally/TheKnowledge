# Session state — 2026-05-26

Last updated: 2026-05-26 (checkpoint after M81+M82; user requested)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` for ~61 synthesis pages (lint ERROR).
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.

Deferred (L-effort or low-impact):
- QUAL-8 (semantic citation-claim coherence) — L effort
- ARCH-12 (second NLM backend) — L effort
- TOK-10 (Sonnet route for authorship) — M effort, spend manageable
- ONT-5/7/9 (academic modeling) — M effort, low daily impact
- ONT-1 (1000 concept reclassifications) — L effort + human-bottlenecked

---

## Files mid-edit

None. main is clean at m82-phase5-round-o. 1615 tests passing.

---

## Decisions made this session

- M81: SRCH-2 wiki index --rebuild — explicit _DIR_TO_TYPE dict (avoids rstrip("s") → "synthesi" bug); wiki_index MCP name (parity convention); write_atomic from core (not locking module).
- M82: TOOL-12 daily-domain-digest — FilterClient injection for testability; synthesizes: + ## Included works generated to pass validate_synthesizes_integrity; draft: true always; daily cron 0 6 * * *; wiki_routine MCP tool (single tool handles all routine names).
- Session-state checkpointing: proactive after each milestone merge, not waiting for precompact hook.

---

## Rejected approaches this session

- M81: locking.write_atomic doesn't exist — use core.write_atomic; rstrip("s") corrupts "synthesis" → "synthesi" — use explicit _DIR_TO_TYPE dict; wiki_index_rebuild MCP name — parity test expects wiki_{cli_op} = wiki_index.
- M82: AGT-6 skipped (conflicts with hard rule: artifact generation opt-in applies to nlm-briefing); QUAL-1 already done in M66; AGT-12 already done in M65.

---

## Next atomic step

Phase 5 substantially complete (M68–M82, 15 milestones). All proposed Phase 4+5 items from the 2026-05-26 rubric doc have been delivered.

Remaining options in priority order:
1. TOOL-13 (source-explorer web view, `/sources` route) — S effort, no deps
2. TOK-10 (Sonnet authorship route) — M effort, minor cost optimization
3. Phase 5 exit checkpoint / BUILD.md phase summary
4. L-effort items (QUAL-8, ARCH-12, ONT-1) — need forcing function
