---
schema_version: 1
type: concept
slug: bayesian-hierarchical-aft-model
canonical_name: Bayesian hierarchical Accelerated Failure Time model
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:01:07Z'
draft_unresolved_claims: 3
created_at: '2026-05-20T21:16:32Z'
last_updated: '2026-05-20T21:16:32Z'
---

# Bayesian hierarchical Accelerated Failure Time model

## Summary

A Bayesian hierarchical Accelerated Failure Time (AFT) model is a survival-analysis framework in which time-to-failure is modelled with covariates that multiplicatively accelerate or decelerate lifetime, combined with hierarchical priors that pool information across groups (e.g. manufacturers) while letting each group retain its own baseline. As applied to wind turbine reliability, the formulation is designed to disentangle intrinsic design variability from environmental drivers of failure.

## Key claims

- Jacquet, Haus, Hermoso, and Pulikollu propose a Bayesian hierarchical Accelerated Failure Time model for wind turbine gearbox reliability that explicitly captures manufacturer-specific baseline reliability while estimating the influence of environmental covariates [[sources/web-2026-05-01-6b7]].
- The motivation for the hierarchical AFT framing is that large-scale datasets aggregate turbines exposed to heterogeneous environmental conditions, creating confounding between intrinsic design variability and wind-driven effects that must be disentangled for robust reliability inference [[sources/web-2026-05-01-6b7]].
- The framework is presented as providing a rigorous basis for fleet-scale reliability assessment, maintenance planning, and long-term asset management in wind energy systems [[sources/web-2026-05-01-6b7]].
- When fitted to over 8,000 gearboxes and 64,000 cumulative operating years, the model attributes the dominant share of the failure signal to intrinsic design differences rather than to environmental covariates [[sources/web-2026-05-01-6b7]].

## Sources

- [[sources/web-2026-05-01-6b7]]

## Related

- [[entities/wind-turbine-bayesian-aft-paper]]
- [[concepts/wind-turbine-gearbox-reliability]]
- [[concepts/fleet-scale-reliability-assessment]]
- [[concepts/capacity-factor-fatigue-degradation]]
