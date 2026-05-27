# Session state — 2026-05-27

Last updated: 2026-05-27 (post-Phase-9: condo-capital-infra eval fix committed)

---

## Open contracts

None.

Carry-forward (not blocking anything):
- ONT-11 RESOLVED: `wiki backfill-synthesizes` ran 2026-05-27, 50 pages updated, 0 errors. 63 synthesizes-coverage ERRORs cleared.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.
- schema-drift: 225 remaining (all editorial-only: invalid entity_kind, missing sections, long slugs, missing canonical_name — requires per-entity human review).
- broken-wikilinks: 82 remaining (all WARNINGs — forward-references to entity/concept pages not yet authored).
- condo-capital-infra eval ceiling at 0.459: q09 (web-2025-10-29-056 24-month rule) and q10
  (10-15% Full vs Baseline specific claim) need raw source bodies that exceed 500k context
  budget. Fix path: wiki nlm-add condo-capital-infra for these 2 sources + targeted wiki query.
- ai-native-business: mean=0.889 at --max-chars 750000; q08 previously 0.00 due to judge JSON
  truncation, now rescued via regex fallback. evaluate-weekly cron updated to --max-chars 750000.

---

## Files mid-edit

None. 1837 tests passing. Phase 9 exit checkpoint written in BUILD.md § 19.
Post-phase: 50 synthesis pages modified by backfill-synthesizes (synthesizes: frontmatter populated). Uncommitted.

---

## Decisions made this session

- Phase 9 rubric: docs/260527_knowledge_phase9_backlog-rubric.md
- M100: _synthesis_question quality (domain policy + source preview). 1812 → 1822 tests (+10).
- M101: wiki evaluate --all-domains + evaluate-weekly cron. 1822 → 1830 tests (+8).
- M102: parse_iso consolidation (6 duplicates → gateway.core). 1830 → 1837 tests (+7).
- Phase 9 exit checkpoint: criteria 1+3 met; criterion 2 infrastructure-met (ANTHROPIC_API_KEY_RESEARCH is user action).
- condo-capital-infra eval fix (post-Phase-9): root cause = 7 web sources missing domain tag,
  absent from NLM corpus, no synthesis context for those sources. Fix: tagged raw sources with
  condo-capital-infra, added cross-cutting synthesis to domain, created 3 draft synthesis pages,
  added synthesizes entry for web-2022-07-07-3bd. Score: 0.100 → 0.459. Commit: 2987571.

---

## Next atomic step

Phase 10 to be scoped. Candidates:

- Editorial schema-drift tooling (225 items, entity_kind reclassification) — M effort, only if user confirms editorial backlog priority
- QUAL-8 citation-claim coherence judge — deferred (no forcing function)
- Source-orphan live discharge — run wiki routine discharge-orphans on live domains once ANTHROPIC_API_KEY_RESEARCH is set (triggers M101 work)
- Fine-tune threshold reach (glp1 at 268/500) — user-paced, not engineering

Await user direction or run /build-checkpoint.
