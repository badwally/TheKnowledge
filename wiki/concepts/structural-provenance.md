---
schema_version: 1
type: concept
slug: structural-provenance
canonical_name: Structural Provenance
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:01Z'
last_updated: '2026-05-28T20:24:01Z'
---

# Structural Provenance

## Summary

Structural provenance means every claim on a wiki page can be traced back to a specific chunk of a specific source document via stable identifiers, rather than being attributed loosely to a document as a whole [[sources/web-2026-04-11-879]].

## Key claims

- WikiLoom persists every chunk of a source to a SQLite cache with a stable `chunk_id` derived from `sha256(source_hash + chunk_index)` [[sources/web-2026-04-11-879]].
- Pages reference their contributing chunks via a `sources` frontmatter array in which each source dict carries its own `chunk_ids` list, so every claim is traceable to a specific chunk of a specific document [[sources/web-2026-04-11-879]].
- The CLI exposes the trace explicitly: `wikiloom show <page> --field sources` lists the contributing sources, and `wikiloom source <chunk_id>` prints the exact chunk text the LLM saw [[sources/web-2026-04-11-879]].
- Structural provenance is positioned as a key differentiator over naive RAG, where retrieval is opaque and chunk-level attribution is not preserved in the resulting artifact [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
- [[concepts/deterministic-linking]]
