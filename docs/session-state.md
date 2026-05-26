# Session state — 2026-05-26

Last updated: 2026-05-26 (M74 complete; Phase 5 Round G merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` to auto-populate missing `synthesizes:` on ~56 synthesis pages. Lint now reports these as ERROR.
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- WIKI.md § 9 hard-rule-1 invariant documentation deferred.
- RSS enclosure → podcast pipeline (INT-2 + INT-3 extension) deferred.
- QUAL-7 pollers need actual API access to run (pubmed-retractions and arxiv-revisions check external HTTP APIs); not run during milestone since no live network in tests.

---

## Files mid-edit

None. Branch phase5-round-g merged; M75 not yet started.

---

## Decisions made this session

- M70: PodcastConverter detects http/https audio URLs; VoiceConverter detects local files — non-overlapping.
- M71: fm.serialize() injects schema_version: 1 as first key (preserves explicit values).
- M71: ONT-11 lint escalated WARNING → ERROR since backfill helper now ships.
- M72: ONT-13 scope = statute + standard only; STALE_DAYS = 365; unparseable → ERROR.
- M73: ARCH-13 — status field is planned/executed/abandoned; archive threshold = 90 days.
- M73: QUAL-7 — PubMed uses eFetch XML + CommentsCorrections check; arXiv uses Atom API + version number comparison; both use per-source cursors with RECHECK_DAYS = 30.
- M73: retracted-citations lint scope = all wiki pages (not just synthesis).
- M74: AGT-13 — skill output file is .claude/skills/wiki-<domain>/SKILL.md (not wiki/); does not use write_atomic (writes to .claude/ not wiki/raw/); added to ARCH-14 allowlist.
- M74: DOC-5 — rotate-log keeps 90 days by default; quarterly archive naming (YYYY-Q); CLI_ONLY in MCP; weekly Sunday 03:00 UTC cron.

---

## Rejected approaches this session

- Injecting schema_version in write_atomic() — frontmatter.serialize() is the right injection point.
- feedparser for RSS parsing — not in venv; use stdlib xml.etree.ElementTree.
- ET.Element or-chains — ET.Element falsy when childless; use `is None`.
- Gmail MCP tools from Python gateway code — use imaplib instead.
- QUAL-7 via retraction flag on wiki/sources pages — flag lives on raw sources (frontmatter mutation allowed per hard rule §6).

---

## Next atomic step

M75 — Phase 5 Round H. Outstanding Phase 3 items with deps met:
- QUAL-10 (M): held-out gold set for filter-calibration (30-50 examples per domain at .knowledge/policies/<d>/calibration_set.yaml; wiki finetune --distill re-scores; policy YAML carries calibration_metrics block) — deps QUAL-12 ✓
- ARCH-12 (L): second NlmClient backend (Gemini-direct or Claude-with-loaded-corpus) — large effort, skip for now
- ARCH-13 ✓, DOC-5 ✓, AGT-13 ✓, QUAL-7 ✓ (all done)
- DOC-8 (M): Split BUILD.md → frozen plan + milestones + CHANGELOG.md — deps DOC-7 ✓
- DOC-9/10/11/12 (S each): Tests README, MCP API ref, runbook, historical-doc indexing
Recommended next: QUAL-10 + DOC-8 (one quality + one doc item).
