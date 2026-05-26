# Session state — 2026-05-26

Last updated: 2026-05-26 (M81 complete; phase5-round-n merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` for ~61 synthesis pages (lint ERROR).
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- RSS enclosure → podcast pipeline (INT-2 + INT-3 extension) deferred.
- QUAL-7 pollers need live network.
- QUAL-10 calibration sets for production domains need manual labelling.
- QUAL-8 (semantic citation-claim coherence) deferred — L-effort.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.

---

## Files mid-edit

None. M81 merged to main as m81-phase5-round-n. 1596 tests passing.

---

## Decisions made this session

- M81: SRCH-2 wiki index --rebuild — used explicit `_DIR_TO_TYPE` dict (not `rstrip("s")`); MCP tool named `wiki_index` to satisfy parity convention; `write_atomic` from `core`.
- M80: SRCH-1 wiki search — score 3/2/1 title/slug/body; no external deps.
- M79: Slack poller — min_length filter + thread ingest; injectable fetch callables.
- M78: Notion poller — note-notion-<sha256(page_id)[:12]> slug; injectable client.

---

## Rejected approaches this session

- M81: `locking.write_atomic` — module has no such function; used `core.write_atomic`.
- M81: `rstrip("s")` for dir→type mapping — corrupts "synthesis" → "synthesi".
- M81: MCP tool named `wiki_index_rebuild` — parity test expects `wiki_{cli_op}` = `wiki_index`.

---

## Next atomic step

Phase 5 substantially complete. M81 closes the last "stub" item noted in CLAUDE.md.

Remaining engineering options in priority order:
1. TOK-10: minor optimization (Sonnet authorship cost reduction) — S effort
2. ONT-5/7/9: academic modeling ops — low daily impact
3. ARCH-12: deferred — L effort
4. Phase 5 closeout / milestone checkpoint

Highest-value next item: TOK-10 or Phase 5 closeout checkpoint.
