---
schema_version: 1
type: concept
slug: homogeneous-poisson-process
canonical_name: Homogeneous Poisson Process
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:46Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T19:28:24Z'
last_updated: '2026-05-20T19:28:24Z'
---

# Homogeneous Poisson Process

## Summary

A stochastic point process in which event arrivals occur at a constant rate independent of system age, used by Khalaj et al. (2026) to model rail surface defect arrivals when precise installation dates are unknown.

## Key claims

- A Homogeneous Poisson Process (HPP) assumes the defect arrival rate is constant and independent of the rail installation date [[sources/web-2026-03-04-157]].
- Under an HPP, the expected number of defect arrivals on a track between two cumulated-tonnage points is a linear function of the tonnage interval scaled by the arrival rate, and the probability of observing a given count of defects over a tonnage interval follows a Poisson distribution [[sources/web-2026-03-04-157]].
- Khalaj et al. adopt HPP rather than a non-homogeneous Poisson process for rail surface defect arrivals because non-homogeneous modelling is highly dependent on the precise rail installation date, which is poorly known for long-lived tracks [[sources/web-2026-03-04-157]].
- HPP allows full probability distributions to be derived for defect arrivals, providing a precise view of the risk of delaying an inspection [[sources/web-2026-03-04-157]].

## Sources

- [[sources/web-2026-03-04-157]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/rail-surface-defects]]
- [[concepts/inspection-planning-decision-support]]
- [[entities/rail-surface-defect-hbm-paper]]
