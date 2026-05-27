---
schema_version: 1
type: concept
slug: data-driven-rul-prediction
canonical_name: Data-driven RUL prediction
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:18:42Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T19:22:56Z'
last_updated: '2026-05-20T19:22:56Z'
---

# Data-driven RUL prediction

## Summary

Data-driven Remaining Useful Life (RUL) prediction infers a system's end-of-life distribution directly from observed performance data, without simulating explicit physical state transitions in a state-space model. The Diaz-Gonzalez et al. (2025) particle filter approach is an example: it borrows particle-filter machinery from model-based prognostics but applies it to a stochastic degradation process governed by performance metrics.

## Key claims

- Diaz-Gonzalez et al. (2025) describe their method as a data-driven approach to RUL prediction that also quantifies uncertainty, drawing inspiration from model-based particle filtering techniques [[sources/web-2025-11-10-fd9]].
- Instead of simulating system state transitions, the authors model degradation as a stochastic process governed by performance metrics and use a Bayesian particle filtering framework to infer its underlying parameters [[sources/web-2025-11-10-fd9]].
- The approach explicitly bypasses traditional state-space modeling by directly estimating the end-of-life distribution from observed performance data [[sources/web-2025-11-10-fd9]].
- To improve uncertainty capture, the propagation noise and observation correction strength of the filter are adapted over time based on current observations and past predictive performance [[sources/web-2025-11-10-fd9]].
- "Data-driven methods" is one of the listed keywords of the Diaz-Gonzalez et al. (2025) paper, alongside remaining useful life, particle filter methods, system-level prognostics, and performance metrics [[sources/web-2025-11-10-fd9]].

## Sources

- [[sources/web-2025-11-10-fd9]]

## Related

- [[concepts/remaining-useful-life]]
- [[concepts/particle-filter-methods]]
- [[concepts/system-level-prognostics]]
- [[entities/particle-filter-rul-paper]]
