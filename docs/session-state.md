# Session state — 2026-05-26

Last updated: 2026-05-26 (M73 complete; Phase 5 Round F merged)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 user action: run `wiki backfill-synthesizes` to auto-populate missing `synthesizes:` on ~56 synthesis pages. Lint now reports these as ERROR.
- ANTHROPIC_API_KEY_RESEARCH needed for eval runs.
- WIKI.md § 9 hard-rule-1 invariant documentation deferred.
- RSS enclosure → podcast pipeline (INT-2 + INT-3 extension) deferred.

---

## Files mid-edit

None. Branch phase5-round-f ready to merge; M74 not yet started.

---

## Decisions made this session

- M70: PodcastConverter detects http/https audio URLs; VoiceConverter detects local files — non-overlapping.
- M71: fm.serialize() injects schema_version: 1 as first key (preserves explicit values).
- M71: ONT-11 lint escalated WARNING → ERROR since backfill helper now ships.
- M72: ONT-13 scope = statute + standard only; STALE_DAYS = 365; unparseable → ERROR.
- M73: ARCH-13 — status field is planned/executed/abandoned; archive threshold = 90 days.
- M73: QUAL-7 — PubMed uses eFetch XML + CommentsCorrections check; arXiv uses Atom API + version number comparison; both use per-source cursors with RECHECK_DAYS = 30.
- M73: retracted-citations lint scope = all wiki pages (not just synthesis).

---

## Rejected approaches this session

- Injecting schema_version in write_atomic() — frontmatter.serialize() is the right injection point.
- feedparser for RSS parsing — not in venv; use stdlib xml.etree.ElementTree.
- ET.Element or-chains — ET.Element falsy when childless; use `is None`.
- Gmail MCP tools from Python gateway code — use imaplib instead.
- QUAL-7 via retraction flag on wiki/sources pages — flag lives on raw sources (frontmatter mutation allowed per hard rule §6); lint reads raw frontmatter.

---

## Next atomic step

M74 — Phase 5 Round G. Next outstanding items from Phase 3 review doc:
- AGT-13 (M): per-domain skill auto-emit (`wiki skill-emit <domain>`) — deps AGT-12 ✓
- DOC-5 (M): log.md rotation — deps K4 ✓ (scheduler)
- QUAL-10 (M): held-out gold set replaces n=5 filter-calibration — deps QUAL-12 ✓
- ARCH-13 ✓ (done M73), QUAL-7 ✓ (done M73)
Recommended grouping: AGT-13 + DOC-5 (one code + one infra item, both M-effort).
