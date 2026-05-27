# Session state — 2026-05-27

Last updated: 2026-05-27 (Phase 11 complete — M107+M108, 1854 tests; Phase 12 work stalled)

---

## Open contracts

None.

Carry-forward:
- **NLM session duration**: `nlm login` cookies expire within seconds in CLI subprocess context. `discharge-orphans` on edge-ai-agentic fails mid-batch (even limit=5). Root cause: Chrome session cookies are invalidated by Google when reused outside the originating browser. Fix requires persistent OAuth refresh token in nlm-mcp CLI. Discharge-orphans multi-domain sweep is blocked until this is resolved.
- **finalize-batch escalated**: 379 escalated drafts (uncited claims, sources not in corpus). `--suggest` found no auto-appliable citations for entity pages — claims reference researchers not yet ingested as sources. These require manual source ingestion + citation work (human editorial, Dim 2-fail).
- schema-drift: 208 remaining (legacy editorial tail — Dim 2-fail, human judgment).
- orphans: 541 wiki-page orphans (no inbound wikilinks). Reduced by finalize converting drafts; slightly increased by new discharge-orphans synthesis page.
- glp1-reward-modulation has no NLM notebook.
- INT-18/INT-19 hand-tests deferred.
- `wiki migrate` stub remains.

---

## Files mid-edit

None. 1854 tests passing. Phase 11 exit checkpoint in BUILD.md § 23.

---

## Decisions made this session

- Phase 11: M107 (discharge dry-run fix), M108 (finalize-batch 21 Cat A).
- finalize-batch --suggest finding: entity pages for legacy-import researchers have no source material in corpus; cite-suggest returns "no auto-appliable suggestions." Human editorial needed.
- Orphan count (541) is wiki-page-level (no inbound links), not source-level. discharge-orphans reduces source orphans; wiki-page orphans are driven by cross-linking.

---

## Next atomic step

Phase 12 is in human-editorial territory. Engineering options remaining:
1. Ingest sources for the researcher entity pages (per-researcher web pages, papers) so cite-suggest can cite them → THEN finalize-batch --suggest --execute
2. Build glp1-reward-modulation NLM notebook (`wiki research` on that domain) → THEN discharge-orphans can run
3. Continue schema-drift cleanup (entity_kind, slug, canonical_name) — requires per-entity human decisions

Lowest-friction next step: `wiki research "<question>" --domain glp1-reward-modulation` to create a NLM notebook, then discharge-orphans. User direction needed for which domain/topic to research next.
