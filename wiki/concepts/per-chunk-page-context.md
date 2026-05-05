---
type: concept
slug: per-chunk-page-context
canonical_name: Per-Chunk Page Context
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
---

# Per-Chunk Page Context

## Summary

Per-chunk page context is an ingest-time technique in which each chunk of a new source is embedded and used to retrieve the top-K most semantically similar existing pages, giving the LLM the candidate set when deciding whether to UPDATE an existing page or CREATE a new one [[sources/web-2026-04-11-879]]. The mechanism reduces duplicate page creation without any code-side merging logic.

## Key claims

- During ingest, each chunk is embedded and the top-K most semantically similar existing pages are retrieved [[sources/web-2026-04-11-879]].
- The LLM sees this list when choosing UPDATE versus CREATE for each candidate page [[sources/web-2026-04-11-879]].
- The mechanism reduces duplicate page creation without any code-side merging [[sources/web-2026-04-11-879]].
- The behavior can be disabled per-run with `wikiloom ingest <file> --no-page-context` or per-project via `[ingest] use_page_context = false` [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
