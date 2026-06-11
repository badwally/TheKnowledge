---
schema_version: 1
type: concept
slug: dynamic-model-perturbation
canonical_name: Dynamic Model Perturbation
domains:
- data-collectives
created_at: '2026-06-10T22:24:13Z'
last_updated: '2026-06-10T22:24:13Z'
draft: true
draft_started_at: '2026-06-10T22:24:13Z'
draft_unresolved_claims: 0
---

# Dynamic Model Perturbation

## Summary

Dynamic model perturbation is a defense for federated learning that adds controlled randomized noise to model parameters or gradient updates during training, with the noise schedule varying across rounds and locations rather than being applied uniformly [[sources/arxiv-2409.13004]]. Wei et al. (2024) propose it as a unified defense aimed at providing privacy protection, poisoning resilience, and model performance simultaneously, rather than treating these three objectives as strictly traded off against one another [[sources/arxiv-2409.13004]].

## Key claims

- Dynamic model perturbation generalizes static gradient perturbation: the noise is parameterized by both *amount* and *location* (which layer or update, which round) and varies across the training trajectory [[sources/arxiv-2409.13004]].
- The mechanism is argued to defend against both gradient-leakage attacks on privacy and data-poisoning attacks on integrity within a single perturbation regime [[sources/arxiv-2409.13004]].
- Wei et al. claim, on empirical grounds, an attainable joint operating point where privacy protection, poisoning resilience, and model performance coexist — positioned against the conventional view that these three objectives only trade off pairwise [[sources/arxiv-2409.13004]].

## Sources

- [[sources/arxiv-2409.13004]] — Data Poisoning and Leakage Analysis in Federated Learning (2024)

## Related

- [[concepts/gradient-inversion-defense]]
- [[concepts/training-data-poisoning]]
- [[concepts/model-trojan-attack]]
- [[concepts/cross-silo-federated-learning]]
- [[entities/data-poisoning-leakage-fl-chapter]]
