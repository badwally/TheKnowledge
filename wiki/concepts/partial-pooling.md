---
schema_version: 1
type: concept
slug: partial-pooling
canonical_name: Partial Pooling
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:46Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T19:28:24Z'
last_updated: '2026-05-20T19:28:24Z'
---

# Partial Pooling

## Summary

A hierarchical Bayesian estimation strategy that shares information across related units (e.g. tracks) without fully merging them, used to improve parameter estimates when per-unit data is sparse and unevenly distributed.

## Key claims

- Partial pooling of unevenly distributed inspection data is used in the Khalaj et al. hierarchical Bayesian Homogeneous Poisson Process model to improve arrival-rate parameter estimates across rail tracks with sparse and unequal records [[sources/web-2026-03-04-157]].
- The motivation for partial pooling in this application is that inspection data is sparse relative to the size of the rail network and the diversity of operating conditions such as speeds and climate [[sources/web-2026-03-04-157]].

## Sources

- [[sources/web-2026-03-04-157]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[entities/rail-surface-defect-hbm-paper]]
