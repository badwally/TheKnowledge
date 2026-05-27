---
schema_version: 1
type: concept
slug: pre-flight-budget-check
canonical_name: Pre-Flight Budget Check
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Pre-Flight Budget Check

## Summary

A pre-flight budget check is a cost-control mechanism that estimates the token cost of an ingest run before any LLM calls are made, refusing the run if month-to-date spend would exceed a configured budget . It is the only enforcement point — overruns mid-run are warned via stderr but not aborted.

## Key claims

- Before running synthesis, ingest estimates the token cost and refuses if it would exceed `[llm] monthly_budget_usd` in `wikiloom.toml` .
- The default `monthly_budget_usd` is $50 .
- After the run, if month-to-date spend exceeds the budget, a stderr warning fires; there is no mid-run abort because pre-flight is the only enforcement point .
- The check can be disabled with `[ingest] enable_budget_check = false` .
- WikiLoom recommends configuring a cheaper `ingest_model` and a stronger `query_model` separately in `wikiloom.toml` for cost optimization .

## Sources

- — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
