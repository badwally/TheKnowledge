---
schema_version: 1
type: concept
slug: model-inversion-attack
canonical_name: Model Inversion Attack
domains:
- data-collectives
created_at: '2026-06-10T22:25:30Z'
last_updated: '2026-06-10T22:25:30Z'
draft: true
draft_started_at: '2026-06-10T22:25:30Z'
draft_unresolved_claims: 0
---

# Model Inversion Attack

## Summary

A model inversion attack is a privacy attack that reconstructs features or representative samples of the training data from access to a trained model — its parameters, gradients, or output API [[sources/web-2025-08-21-f21]]. Model inversion is one of the three principal categories of privacy attacks on deep learning models surveyed in the DP defense literature, alongside membership inference and model extraction [[sources/web-2025-08-21-f21]].

## Key claims

- Model inversion attacks aim to recover features of the training data — including, in some settings, reconstructions of individual training examples — from access to a trained deep learning model [[sources/web-2025-08-21-f21]].
- Model inversion is identified by recent surveys as one of the major privacy risks facing deep learning, alongside membership inference and model extraction [[sources/web-2025-08-21-f21]].
- Differential privacy provides a formal defense against model inversion by bounding how much any single training record can influence the model's outputs, which in turn limits how much can be reconstructed about that record [[sources/web-2025-08-21-f21]].
- Model inversion is conceptually adjacent to gradient inversion in the federated setting — both seek to reconstruct training inputs — but classic model inversion targets the trained model rather than per-step gradients [[sources/web-2025-08-21-f21]].

## Sources

- [[sources/web-2025-08-21-f21]] — Zhang, X. & Zhang, Q. (2025). Defending against attacks in deep learning with differential privacy: a survey.

## Related

- [[concepts/gradient-inversion-attack]]
- [[concepts/gradient-inversion-defense]]
- [[concepts/membership-inference-attack]]
- [[concepts/model-extraction-attack]]
- [[concepts/differential-privacy]]
- [[entities/zhang-2025-dp-survey]]
- [[entities/gradient-inversion-survey]]
