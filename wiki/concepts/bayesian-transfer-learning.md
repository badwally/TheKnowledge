---
type: concept
slug: bayesian-transfer-learning
canonical_name: Bayesian Transfer Learning
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:07:43Z'
draft_unresolved_claims: 1
---

# Bayesian Transfer Learning

## Summary

Bayesian transfer learning uses posterior dependencies between related inference problems to transfer information from data-rich to data-poor problems, with the transfer governed by explicit statistical correlations rather than learned representations.

## Key claims

- In the Bull et al. fleet framework, statistical correlations between asset sub-groups in a hierarchical Bayesian model are the mechanism that enables knowledge transfer — Bayesian transfer learning is realised as a property of the joint posterior, not as a separate training stage [[sources/arxiv-2204.12404]].
- Because the transfer is governed by inferred correlations, those correlations can be inspected to determine which assets share information for which specific effect or parameter, giving engineers an interpretable account of where transfer is occurring [[sources/arxiv-2204.12404]].
- Bayesian transfer learning via hierarchical correlations was shown to improve survival analysis of a truck fleet and power prediction in a wind farm, with sub-fleets that have sparse data borrowing strength from richer sub-fleets at higher levels of the hierarchy [[sources/arxiv-2204.12404]].

## Sources

- [[sources/arxiv-2204.12404]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/multitask-learning]]
- [[concepts/partial-pooling]]
