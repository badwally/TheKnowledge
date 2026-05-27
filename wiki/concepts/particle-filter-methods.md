---
schema_version: 1
type: concept
slug: particle-filter-methods
canonical_name: Particle filter methods
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T18:18:42Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T19:22:56Z'
last_updated: '2026-05-20T19:22:56Z'
---

# Particle filter methods

## Summary

Particle filter methods are sequential Monte Carlo techniques for Bayesian inference, used in prognostics to infer the parameters of a stochastic degradation process and propagate uncertainty about a system's future state and Remaining Useful Life (RUL). In Diaz-Gonzalez et al. (2025), a Bayesian particle filter is repurposed as a data-driven prognostics engine rather than as a model-based state-space filter.

## Key claims

- Diaz-Gonzalez et al. (2025) describe their RUL prediction method as drawing inspiration from model-based particle filtering techniques, while replacing simulated system state transitions with a stochastic process governed by performance metrics [[sources/web-2025-11-10-fd9]].
- They use a Bayesian particle filtering framework to infer the underlying parameters of the degradation process from observed performance data [[sources/web-2025-11-10-fd9]].
- Two key characteristics of the filter — propagation noise and observation correction strength — are adapted over time based on current observations and past predictive performance, which the authors argue improves the filter's ability to capture future uncertainty [[sources/web-2025-11-10-fd9]].
- In this formulation, the particle filter directly estimates the end-of-life distribution from observed performance data rather than simulating state-space transitions [[sources/web-2025-11-10-fd9]].

## Sources

- [[sources/web-2025-11-10-fd9]]

## Related

- [[concepts/remaining-useful-life]]
- [[concepts/data-driven-rul-prediction]]
- [[concepts/system-level-prognostics]]
- [[entities/particle-filter-rul-paper]]
