# Session state — 2026-05-26

Last updated: 2026-05-26 (M72 complete; Phase 5 Round E merged)

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

None. Branch phase5-round-e ready to merge; M73 not yet started.

---

## Decisions made this session

- M70: PodcastConverter detects http/https audio URLs; VoiceConverter detects local files — non-overlapping.
- M70: Six-step source type contract applied; `podcast-<slug>-<sha10>` ID format; sidecar at raw/podcast/.
- M71: fm.serialize() injects schema_version: 1 as first key (preserves explicit values).
- M71: ONT-11 lint escalated WARNING → ERROR since backfill helper now ships.
- M71: Mixed-tier synthesizes (sources/ + synthesis/ mixed) → sources/ wins (mixed is invalid per validator).
- M72: ONT-13 scope = statute + standard only (both time-sensitive; person/drug/etc. do not require last_verified_at).
- M72: Unparseable last_verified_at → ERROR not WARNING (bad data same severity as absent data).
- M72: STALE_DAYS = 365 (1 year threshold).
- INT-8 confirmed already complete (repo_metadata.py + 11 tests existed before this session).
- ARCH-6/7/8, QUAL-4/5/9/13, TOK-7 all confirmed already done in prior milestones.

---

## Rejected approaches this session

- Injecting schema_version in write_atomic() — frontmatter.serialize() is the right injection point.
- feedparser for RSS parsing — not in venv; use stdlib xml.etree.ElementTree.
- ET.Element or-chains — ET.Element falsy when childless; use `is None`.
- Gmail MCP tools from Python gateway code — use imaplib instead.

---

## Next atomic step

M73 — Phase 5 Round F. Check BUILD.md backlog for next S-effort items (QUAL-7 retraction monitor, TOK-12 salvage, or other Phase 5 items not yet confirmed done).
