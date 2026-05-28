---
schema_version: 1
type: concept
slug: llm-wiki-pattern
canonical_name: LLM Wiki Pattern
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:00Z'
last_updated: '2026-05-28T20:24:00Z'
---

# LLM Wiki Pattern

## Summary

The LLM wiki pattern uses a language model to read raw documents and write structured, human-readable wiki pages, building a persistent knowledge graph instead of an opaque vector store [[sources/web-2026-04-11-879]]. The pattern was popularized by Andrej Karpathy's LLM wiki gist and is the architecture WikiLoom implements [[sources/web-2026-04-11-879]].

## Key claims

- The pattern positions itself against naive RAG: rather than re-embedding documents into an opaque vector store, the LLM writes structured wiki pages that compound into a persistent, human-readable knowledge graph with deterministic wikilinking and structural provenance back to source chunks [[sources/web-2026-04-11-879]].
- In this pattern the LLM owns judgment work — reading sources, extracting claims, assessing confidence — while downstream operations (linking, backlink graph, index regeneration, git commit) are deterministic [[sources/web-2026-04-11-879]].
- WikiLoom is one concrete implementation of the pattern, explicitly inspired by Andrej Karpathy's LLM wiki gist [[sources/web-2026-04-11-879]].
- Implementations of the pattern typically bind every state-modifying operation to an atomic git commit so the knowledge graph has a durable, auditable history [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[entities/karpathy-llm-wiki-gist]]
- [[concepts/deterministic-linking]]
- [[concepts/structural-provenance]]
- [[concepts/auto-commit-pattern]]
