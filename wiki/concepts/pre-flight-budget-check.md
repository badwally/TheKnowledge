---
schema_version: 1
type: concept
slug: pre-flight-budget-check
canonical_name: Pre-Flight Budget Check
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:03Z'
last_updated: '2026-05-28T20:24:03Z'
---

# Pre-Flight Budget Check

## Summary

A pre-flight budget check estimates the token cost of an LLM operation before any paid API call is made and refuses the run if it would exceed a configured monthly cap — making cost overruns a hard, predictable failure rather than a silent post-hoc surprise [[sources/web-2026-04-11-879]].

## Key claims

- Before running synthesis, WikiLoom's ingest step estimates the token cost and refuses to proceed if it would exceed `[llm] monthly_budget_usd` in `wikiloom.toml` [[sources/web-2026-04-11-879]].
- The default monthly budget is $50/month [[sources/web-2026-04-11-879]].
- Pre-flight is the only enforcement point: after the run, if month-to-date spend exceeds the budget, a stderr warning fires but there is no mid-run abort [[sources/web-2026-04-11-879]].
- The check can be disabled via `[ingest] enable_budget_check = false` [[sources/web-2026-04-11-879]].
- For cost optimization, WikiLoom recommends configuring a cheap model for ingest (the token-heavy operation) and a stronger model for query reasoning — e.g. `ingest_model = "claude-haiku-4-5-20251001"` paired with `query_model = "claude-sonnet-4-6"` [[sources/web-2026-04-11-879]].
- `wikiloom cost` reports token usage and spend by event type with monthly budget percentage [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
