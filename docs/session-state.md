# Session state — 2026-05-26

Last updated: 2026-05-26 (M76 complete; Phase 5 Round I merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` to auto-populate missing `synthesizes:` on ~56 synthesis pages. Lint now reports these as ERROR.
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- RSS enclosure → podcast pipeline (INT-2 + INT-3 extension) deferred.
- QUAL-7 pollers need actual API access to run (pubmed-retractions and arxiv-revisions check external HTTP APIs); not run during milestone since no live network in tests.
- QUAL-10 calibration sets for production domains not yet populated (need manual labelling of 30-50 examples per domain at `.knowledge/policies/<d>/calibration_set.yaml`).

---

## Files mid-edit

None. Branch phase5-round-i merged; M77 not yet started.

---

## Decisions made this session

- M75: QUAL-10 — calibration set at `.knowledge/policies/<d>/calibration_set.yaml`; score_calibration() uses injectable client (same FilterClient protocol); reads raw/ for source excerpts; writes only to .knowledge/policies/; ARCH-14 allowlist updated.
- M75: DOC-8 — CHANGELOG.md at repo root; one-line entries M0-M75; BUILD.md remains the exhaustive record.
- M76: DOC-9/10/11/12 — tests/README.md, docs/MCP_API.md, docs/RUNBOOK.md, docs/superpowers/README.md; SESSION_TRANSCRIPT.md historical header added.
- M76: QUAL-9 confirmed already implemented (lint/domain_purity.py + tests).

---

## Rejected approaches this session

(none new)

---

## Next atomic step

M77 — remaining Phase 5 items with deps met:
- QUAL-14 (M): `supersedes`/`superseded_by` re-ingest — deps QUAL-1 ✓, QUAL-7 ✓
- ARCH-12 (L): Second NlmClient backend — large effort; skip unless user flags priority
- ONT-10 (M): Decision + execution on source-page stubs — decision required from user
- ARCH-15 (S): `schema_version: 1` on all existing pages — backfill migration

Recommended next: QUAL-14 (M, good quality item, deps met).
