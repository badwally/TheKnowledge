# Session state — 2026-05-26

Last updated: 2026-05-26 (M75 complete; Phase 5 Round H merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` to auto-populate missing `synthesizes:` on ~56 synthesis pages. Lint now reports these as ERROR.
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- WIKI.md § 9 hard-rule-1 invariant documentation deferred.
- RSS enclosure → podcast pipeline (INT-2 + INT-3 extension) deferred.
- QUAL-7 pollers need actual API access to run (pubmed-retractions and arxiv-revisions check external HTTP APIs); not run during milestone since no live network in tests.
- QUAL-10 calibration sets for production domains not yet populated (need manual labelling of 30-50 examples per domain at `.knowledge/policies/<d>/calibration_set.yaml`).

---

## Files mid-edit

None. Branch phase5-round-h merged; M76 not yet started.

---

## Decisions made this session

- M75: QUAL-10 — calibration set at `.knowledge/policies/<d>/calibration_set.yaml`; score_calibration() uses injectable client (same FilterClient protocol); reads raw/ for source excerpts; writes only to .knowledge/policies/; ARCH-14 allowlist updated.
- M75: QUAL-10 — DistillResult.calibration_f1 is float | None (None when no calibration set exists); distill still succeeds without one.
- M75: DOC-8 — CHANGELOG.md at repo root; one-line entries M0-M75; BUILD.md remains the exhaustive record.

---

## Rejected approaches this session

(none new beyond carry-forward from prior sessions)

---

## Next atomic step

M76 — next Phase 5 items with deps met:
- DOC-9 (S): Tests README at `tests/README.md`
- DOC-10 (S): MCP API reference doc
- DOC-11 (S): Operational runbook
- DOC-12 (S): Historical-doc indexing
- ARCH-12 (L): Second NlmClient backend (large effort; skip unless user flags as priority)
- QUAL-9 (S): Cross-domain contamination quarantine in promote-domain (no deps)
- QUAL-14 (M): `supersedes`/`superseded_by` re-ingest — deps QUAL-1 ✓, QUAL-7 ✓

Recommended next: DOC-9/10/11/12 (small doc items, can batch) or QUAL-9 (S, good quality item).
