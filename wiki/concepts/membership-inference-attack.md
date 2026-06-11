---
schema_version: 1
type: concept
slug: membership-inference-attack
canonical_name: Membership Inference Attack
domains:
- data-collectives
created_at: '2026-06-10T22:25:30Z'
last_updated: '2026-06-10T22:25:30Z'
draft: true
draft_started_at: '2026-06-10T22:25:30Z'
draft_unresolved_claims: 0
---

# Membership Inference Attack

## Summary

A membership inference (MI) attack is a privacy attack against a machine-learning model that aims to determine whether a particular data point was part of the model's training dataset [[sources/web-2025-08-21-f21]]. MI attacks succeed because deep learning models — even when trained centrally rather than in a federated setting — tend to memorize features of their training data, leaving observable signals in model outputs that distinguish training-set members from non-members [[sources/web-2025-08-21-f21]].

## Key claims

- MI attacks aim to determine whether a particular data point is part of a neural network's training dataset [[sources/web-2025-08-21-f21]].
- Even centralized (non-federated) deep learning poses MI risk, because deep learning models tend to memorize features of the training data [[sources/web-2025-08-21-f21]].
- MI is one of the three principal privacy threats to deep learning surveyed alongside model inversion and model extraction [[sources/web-2025-08-21-f21]].
- Differential privacy is a primary defense against MI: by bounding the influence of any single training record on the model's output distribution, DP directly attacks the signal MI relies on [[sources/web-2025-08-21-f21]].
- DP-based defenses against MI are surveyed alongside random-noise mitigations for related inference attacks [[sources/web-2025-08-21-f21]].

## Sources

- [[sources/web-2025-08-21-f21]] — Zhang, X. & Zhang, Q. (2025). Defending against attacks in deep learning with differential privacy: a survey.

## Related

- [[concepts/subject-membership-inference-attack]]
- [[concepts/model-inversion-attack]]
- [[concepts/model-extraction-attack]]
- [[concepts/differential-privacy]]
- [[entities/zhang-2025-dp-survey]]
- [[entities/subject-membership-inference-paper]]
