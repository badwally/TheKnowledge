---
type: concept
slug: pre-flight-budget-check
canonical_name: Pre-Flight Budget Check
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
---

# Pre-Flight Budget Check

## Summary

A pre-flight budget check is a cost-control mechanism that estimates the token cost of an ingest run before any LLM calls are made, refusing the run if month-to-date spend would exceed a configured budget [[sources/web-2026-04-11-879]]. It is the only enforcement point — overruns mid-run are warned via stderr but not aborted.

## Key claims

- Before running synthesis, ingest estimates the token cost and refuses if it would exceed `[llm] monthly_budget_usd` in `wikiloom.toml` [[sources/web-2026-04-11-879]].
- The default `monthly_budget_usd` is $50 [[sources/web-2026-04-11-879]].
- After the run, if month-to-date spend exceeds the budget, a stderr warning fires; there is no mid-run abort because pre-flight is the only enforcement point [[sources/web-2026-04-11-879]].
- The check can be disabled with `[ingest] enable_budget_check = false` [[sources/web-2026-04-11-879]].
- WikiLoom recommends configuring a cheaper `ingest_model` and a stronger `query_model` separately in `wikiloom.toml` for cost optimization [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
