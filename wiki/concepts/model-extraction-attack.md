---
schema_version: 1
type: concept
slug: model-extraction-attack
canonical_name: Model Extraction Attack
domains:
- data-collectives
created_at: '2026-06-10T22:25:30Z'
last_updated: '2026-06-10T22:25:30Z'
draft: true
draft_started_at: '2026-06-10T22:25:30Z'
draft_unresolved_claims: 0
---

# Model Extraction Attack

## Summary

A model extraction attack is a privacy attack in which an adversary uses query access to a deployed deep learning model to reconstruct an approximate copy of the model itself — its parameters, its functionality, or both [[sources/web-2025-08-21-f21]]. Where membership inference and model inversion target training data, model extraction targets the model as the asset of interest; all three are surveyed together as the principal categories of privacy threats motivating DP-based defenses [[sources/web-2025-08-21-f21]].

## Key claims

- Model extraction attacks aim to recover an approximation of the target model's parameters or functionality through query access [[sources/web-2025-08-21-f21]].
- Model extraction is identified as one of the principal privacy threats to deployed deep learning systems, alongside membership inference and model inversion [[sources/web-2025-08-21-f21]].
- Differential privacy is a candidate defense against model extraction by perturbing model outputs sufficiently that they leak less information about the underlying parameters [[sources/web-2025-08-21-f21]].

## Sources

- [[sources/web-2025-08-21-f21]] — Zhang, X. & Zhang, Q. (2025). Defending against attacks in deep learning with differential privacy: a survey.

## Related

- [[concepts/membership-inference-attack]]
- [[concepts/model-inversion-attack]]
- [[concepts/differential-privacy]]
- [[entities/zhang-2025-dp-survey]]
