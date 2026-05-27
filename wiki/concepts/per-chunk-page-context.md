---
schema_version: 1
type: concept
slug: per-chunk-page-context
canonical_name: Per-Chunk Page Context
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Per-Chunk Page Context

## Summary

Per-chunk page context is an ingest-time technique in which each chunk of a new source is embedded and used to retrieve the top-K most semantically similar existing pages, giving the LLM the candidate set when deciding whether to UPDATE an existing page or CREATE a new one . The mechanism reduces duplicate page creation without any code-side merging logic.

## Key claims

- During ingest, each chunk is embedded and the top-K most semantically similar existing pages are retrieved .
- The LLM sees this list when choosing UPDATE versus CREATE for each candidate page .
- The mechanism reduces duplicate page creation without any code-side merging .
- The behavior can be disabled per-run with `wikiloom ingest <file> --no-page-context` or per-project via `[ingest] use_page_context = false` .

## Sources

- — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
