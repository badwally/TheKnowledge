---
schema_version: 1
type: concept
slug: per-chunk-page-context
canonical_name: Per-Chunk Page Context
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:03Z'
last_updated: '2026-05-28T20:24:03Z'
---

# Per-Chunk Page Context

## Summary

Per-chunk page context is an ingestion technique in which each source chunk is embedded and used to retrieve the top-K most semantically similar existing pages; that list is then shown to the LLM so it can decide whether to UPDATE an existing page or CREATE a new one — reducing duplicate page creation without any code-side merging [[sources/web-2026-04-11-879]].

## Key claims

- During WikiLoom's synthesis loop, each chunk is embedded and the top-K most semantically similar existing pages are retrieved [[sources/web-2026-04-11-879]].
- The LLM sees that retrieved list when deciding whether to UPDATE an existing page or CREATE a new one, which reduces duplicate page creation without any code-side merging [[sources/web-2026-04-11-879]].
- The mechanism can be disabled per-run via `wikiloom ingest <file> --no-page-context` or per-project via `[ingest] use_page_context = false` [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
- [[concepts/deterministic-linking]]
