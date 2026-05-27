---
schema_version: 1
type: concept
slug: llm-wiki-pattern
canonical_name: LLM Wiki Pattern
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:48Z'
draft_unresolved_claims: 0
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# LLM Wiki Pattern

## Summary

The LLM wiki pattern is a knowledge-base architecture in which an LLM ingests source documents and writes structured wiki pages, treating the LLM as the judgment layer (extracting claims, assessing confidence) while keeping linking, indexing, and persistence deterministic . WikiLoom positions this as an alternative to naive RAG, building a persistent, human-readable knowledge graph instead of an opaque vector store .

## Key claims

- The LLM handles judgment — reading sources, extracting claims, assessing confidence — while everything after the LLM call (linking, backlink graph, index regeneration, git commit) is deterministic .
- The pattern produces a persistent, human-readable knowledge graph rather than re-embedding documents into an opaque vector store .
- Andrej Karpathy's LLM wiki gist is the cited design inspiration .
- Pages are written as markdown so the entire knowledge base remains human-readable and git-trackable .

## Sources

- — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[entities/karpathy-llm-wiki-gist]]
- [[concepts/deterministic-linking]]
- [[concepts/structural-provenance]]
