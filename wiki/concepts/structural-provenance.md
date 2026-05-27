---
schema_version: 1
type: concept
slug: structural-provenance
canonical_name: Structural Provenance
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Structural Provenance

## Summary

Structural provenance is the practice of tracing every claim in a knowledge base back to a specific chunk of a specific source document via stable, content-addressed chunk identifiers [[sources/web-2026-04-11-879]]. It complements citation-grounding by making the underlying source text retrievable, not just referenced.

## Key claims

- Every chunk of a source document is persisted to a SQLite cache with a stable `chunk_id` derived from `sha256(source_hash + chunk_index)` [[sources/web-2026-04-11-879]].
- Pages reference their contributing chunks under each entry in their `sources` frontmatter array — every source dict carries its own `chunk_ids` list [[sources/web-2026-04-11-879]].
- The original chunk text is retrievable via `wikiloom source <chunk_id>` [[sources/web-2026-04-11-879]].
- Contributing sources for a page are inspectable via `wikiloom show <page> --field sources`, which can flatten across sources [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
