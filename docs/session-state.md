# Session state — 2026-05-27

Last updated: 2026-05-27 (precompact snapshot — M98 next)

---

## Open contracts

None. M97 merged clean at m97-phase8-round-b. 1789 tests.

---

## Files mid-edit

None. All M97 files committed. M98 not yet started.

---

## Decisions made this session

- M94: TOOL-15 wiki ask-corpus — thin wrapper over query(). 1750 tests.
- M95: TOOL-16 wiki question new/list + MCP auxiliaries. 1769 tests.
- Phase 7 exit checkpoint written (BUILD.md § 16).
- Phase 8 rubric written (docs/260527_knowledge_phase8_backlog-rubric.md).
- Auto-mode feedback: do not stop at phase boundaries or skill save prompts.
- M96: schema debt clearance (backfill-timestamps 2191 pages + backfill-sources-count 99 pages). schema-drift 4597 → 210. 1777 tests.
- M97: fix-wikilinks (195 source removals + 82 entity/concept downgrades). broken-wikilinks 277 ERRORs → 82 WARNINGs. 1789 tests.
- Remaining schema-drift 210 are editorial-only (invalid entity_kind 58, missing sections 68, long slugs 50, missing canonical_name 34).
- Remaining broken-wikilinks 82 are WARNINGs (intentional forward-references to unauthed pages).

---

## Rejected approaches this session

- ONT-9 (domain hierarchy): deferred — 22 MOCs manageable flat.
- QUAL-8/ARCH-12/ONT-1: deferred — all L-effort, no forcing function.
- ONT-15 (synthesizes → wasDerivedFrom rename): 282 code references + 46 wiki pages, not S effort.
- Stopping at phase boundaries and skill save prompts in auto mode: corrected per user feedback.

---

## Next atomic step

Implement M98: `wiki abandon-stale-drafts [--min-age-days 30] [--dry-run]` op in `src/gateway/ops/abandon_stale_drafts.py`. Logic: walk wiki pages with `draft: true` frontmatter older than N days; check zero inbound citations (no other wiki page has `[[<type>/<slug>]]` pointing to it); call `finalize(path, abandon=True)` on qualifying pages. Wire to CLI (SUBCOMMANDS, IMPLEMENTED, parser, dispatch, handler) and CLI_ONLY in mcp_server. Write 8+ tests. Run full suite. Commit tagged `m98-phase8-round-c` and push.
