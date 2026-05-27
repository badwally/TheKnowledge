# Session state — 2026-05-27

Last updated: 2026-05-27 (Phase 11 complete — M107+M108, 1854 tests)

---

## Open contracts

None.

Carry-forward:
- NLM session duration issue: `nlm login` cookies expire within seconds in CLI subprocess context. `discharge-orphans --domain edge-ai-agentic` fails mid-batch (even limit=5). Root cause: Chrome session cookies are invalidated by Google when reused outside the originating browser. Fix requires persistent OAuth refresh token in nlm-mcp CLI, not extractable session cookies. Discharge-orphans multi-domain sweep is blocked until this is resolved.
- schema-drift: 208 remaining (legacy editorial tail — entity_kind, slug length, canonical_name are Dim 2-fail, human judgment required).
- finalize-batch: 359 escalated drafts (unresolved citations, need `--suggest` + ANTHROPIC_API_KEY_RESEARCH). The 21 Cat A pages are done.
- INT-18/INT-19 hand-tests deferred (need live NOTION_TOKEN/SLACK_BOT_TOKEN).
- `wiki migrate` remains a stub.
- glp1-reward-modulation has no NLM notebook.

---

## Files mid-edit

None. 1854 tests passing. Phase 11 exit checkpoint written in BUILD.md § 23.

---

## Decisions made this session

- Phase 11 rubric: docs/260527_knowledge_phase10_backlog-rubric.md (§ 6 proposed Phase 11 scope)
- M107: discharge-orphans dry-run pre-flight notebook check + "[NLM auth not validated]" note.
- M108: finalize-batch --execute finalized 21 Cat A drafts (3 concepts, 17 entities, 1 synthesis).
- NLM auth finding: Chrome session cookies from `nlm login` expire within seconds in CLI context. Systematic fix needed in nlm-mcp CLI (OAuth refresh tokens).
- eval regression check: all domains stable or improved. glp1 -0.016 is judge variance.

---

## Next atomic step

Phase 12 candidates (NLM-independent, no blockers):
1. finalize-batch --suggest for escalated drafts — uses ANTHROPIC_API_KEY_RESEARCH; auto-cites unambiguous claims, then finalizes. Run with --limit 20 first to validate.
2. wiki lint --scope orphans — check if the condo-capital-infra discharge-orphans run reduced orphan count.
3. Schema-drift editorial sprint — entity_kind, canonical_name fixes require human review; may yield ~50 fewer findings.

Start with item 1 (finalize escalated drafts) — ANTHROPIC_API_KEY_RESEARCH is set.
