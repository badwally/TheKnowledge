# Session state — 2026-05-26

Last updated: 2026-05-26 (M77 complete; phase5-round-j merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` to auto-populate missing `synthesizes:` on ~56 synthesis pages. Lint reports these as ERROR.
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- RSS enclosure → podcast pipeline (INT-2 + INT-3 extension) deferred.
- QUAL-7 pollers need live network (pubmed-retractions, arxiv-revisions check external HTTP APIs); not run during milestone since no live network in tests.
- QUAL-10 calibration sets for production domains not yet populated (need manual labelling of 30-50 examples per domain at `.knowledge/policies/<d>/calibration_set.yaml`).
- QUAL-8 (semantic citation-claim coherence on affected reingest pages) deferred — L-effort standalone item.

---

## Files mid-edit

None. M77 merged to main as m77-phase5-round-j. 1503 tests passing.

---

## Decisions made this session

- M75: QUAL-10 — calibration set at `.knowledge/policies/<d>/calibration_set.yaml`; score_calibration() uses injectable client (same FilterClient protocol); reads raw/ for source excerpts; writes only to .knowledge/policies/; ARCH-14 allowlist updated.
- M75: DOC-8 — CHANGELOG.md at repo root; one-line entries M0-M75; BUILD.md remains the exhaustive record.
- M76: DOC-9/10/11/12 — tests/README.md, docs/MCP_API.md, docs/RUNBOOK.md, docs/superpowers/README.md; SESSION_TRANSCRIPT.md historical header added.
- M76: QUAL-9 confirmed already implemented (lint/domain_purity.py + tests) — no new code needed.
- M77: ingest imported at module level in reingest.py (not local) for monkeypatch compatibility.
- M77: OperationResult.data: dict field added (default {}) for structured reingest return.
- M77: wiki_reingest added as MCP tool (not CLI_ONLY).
- M77: MUTABLE_SOURCE_FIELDS retroactively includes QUAL-7 fields (retracted, retracted_at, arxiv_revised, arxiv_current_version, arxiv_baseline_version) that were missing — silent bug fixed.

---

## Rejected approaches this session

- Local import of ingest inside reingest() function body — breaks monkeypatch; must be module-level.
- MagicMock for gateway stubs — auto-creates call_split_with_usage, triggers K5 telemetry path.
- QUAL-8 semantic coherence in M77 — L-effort standalone item, deferred.

---

## Next atomic step

Post-M77 Phase 5 candidates (check BUILD.md backlog for open items):
- ARCH-12 (L): Second NlmClient backend — large effort; skip unless user flags priority.
- ONT-10 (M): Source-page stubs decision — needs user input on approach.
- ARCH-15 (S): `schema_version: 1` on all existing pages backfill — deps ARCH-15 ✓ (M71 injected on new pages).
- Any remaining S-effort items from Phase 5 backlog without deps.

Read BUILD.md § 9 and review backlog for next S/M items to deliver.
