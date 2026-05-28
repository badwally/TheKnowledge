---
schema_version: 1
type: entity
slug: karpathy-llm-wiki-gist
canonical_name: Karpathy LLM Wiki Gist
entity_kind: artifact
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:00Z'
last_updated: '2026-05-28T20:24:00Z'
---

# Karpathy LLM Wiki Gist

## Summary

Andrej Karpathy's LLM wiki gist is the design inspiration cited by WikiLoom for the pattern in which an LLM reads source documents and writes structured, persistent wiki pages rather than producing opaque vector embeddings [[sources/web-2026-04-11-879]].

## Key facts

- WikiLoom explicitly credits Andrej Karpathy's LLM wiki gist as its conceptual inspiration [[sources/web-2026-04-11-879]].
- The gist describes the pattern WikiLoom implements: ingest a source, have the LLM write structured wiki pages, and treat the wiki as canonical persistent state rather than re-embedding into a vector store [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
