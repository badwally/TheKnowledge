---
type: concept
slug: deterministic-linking
canonical_name: Deterministic Linking
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:48Z'
draft_unresolved_claims: 0
---

# Deterministic Linking

## Summary

Deterministic linking is a wiki-graph construction approach in which each candidate wikilink is scored on a numeric scale, with thresholds determining whether the link is auto-inserted, flagged for review, deferred for manual review, or ignored — making graph construction reproducible and reviewable rather than dependent on opaque embedding similarity [[sources/web-2026-04-11-879]].

## Key claims

- WikiLoom's linker scores each potential wikilink on a 0–100 scale [[sources/web-2026-04-11-879]].
- Scores ≥ 95 are auto-inserted into the page body [[sources/web-2026-04-11-879]].
- Scores ≥ 85 are auto-inserted but flagged in `backlinks.json` [[sources/web-2026-04-11-879]].
- Scores ≥ 70 are deferred to `pending.json` for review via `wikiloom review` [[sources/web-2026-04-11-879]].
- Scores below 70 are ignored [[sources/web-2026-04-11-879]].
- Thresholds are configurable in `wikiloom.toml` under the `[linking]` section [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
