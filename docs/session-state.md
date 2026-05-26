# Session state — 2026-05-26

Last updated: 2026-05-26 (M78 complete; phase5-round-k merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` to auto-populate missing `synthesizes:` on ~61 synthesis pages. Lint reports these as ERROR.
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- RSS enclosure → podcast pipeline (INT-2 + INT-3 extension) deferred.
- QUAL-7 pollers need live network (pubmed-retractions, arxiv-revisions).
- QUAL-10 calibration sets for production domains not yet populated (need manual labelling).
- QUAL-8 (semantic citation-claim coherence) deferred — L-effort standalone item.
- Slack source poller — remaining "queued" poller from CLAUDE.md forward-looking notes.
- INT-18 hand-test deferred to user (requires live NOTION_TOKEN + configured workspace).

---

## Files mid-edit

None. M78 merged to main as m78-phase5-round-k. 1541 tests passing.

---

## Decisions made this session

- M75: QUAL-10 — calibration set at `.knowledge/policies/<d>/calibration_set.yaml`; score_calibration() uses injectable client; reads raw/ for excerpts; writes only to .knowledge/policies/; ARCH-14 allowlist updated.
- M75: DOC-8 — CHANGELOG.md at repo root; BUILD.md remains the exhaustive record.
- M76: QUAL-9 confirmed already implemented — no new code needed.
- M77: ingest imported at module level in reingest.py for monkeypatch compatibility.
- M77: OperationResult.data: dict field added (default {}) for structured reingest return.
- M77: MUTABLE_SOURCE_FIELDS retroactively includes QUAL-7 fields that were missing.
- M78: Notion poller uses note-notion-<sha256(page_id)[:12]> slug; injectable client for tests.
- M78: notion_client.py extended with read ops (get_page, get_page_blocks, search_pages, blocks_to_markdown, _rich_text_to_md).

---

## Rejected approaches this session

- Local import of ingest inside reingest() function body — breaks monkeypatch; must be module-level.
- MagicMock for gateway stubs — auto-creates call_split_with_usage, triggers K5 telemetry path.
- QUAL-8 semantic coherence in M77 — L-effort, deferred.

---

## Next atomic step

Post-M78 remaining Phase 5 candidates:
- Slack source poller (INT-19): M effort, follows same Poller contract; needs OAuth token (SLACK_BOT_TOKEN).
- QUAL-8 (semantic coherence): L effort, deferred.
- ARCH-12 (second NLM backend): L effort, deferred.
- TOK-10 (Sonnet route for authorship): minor optimization, current spend manageable.
- ONT-5/7/9: academic modeling improvements, low daily-use impact.

Next recommended: Slack source poller (INT-19) — completes the CLAUDE.md "queued" poller set.
