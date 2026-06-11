---
schema_version: 1
type: concept
slug: privacy-budget
canonical_name: Privacy Budget (ε, δ)
domains:
- data-collectives
created_at: '2026-06-10T22:25:30Z'
last_updated: '2026-06-10T22:25:30Z'
draft: true
draft_started_at: '2026-06-10T22:25:30Z'
draft_unresolved_claims: 0
---

# Privacy Budget (ε, δ)

## Summary

The privacy budget is the principal tuning parameter of a differential-privacy mechanism: ε quantifies the level of privacy protection provided by a randomized algorithm satisfying (ε, δ)-DP, with smaller ε implying stronger privacy [[sources/web-2025-08-21-f21]]. Because a tighter privacy bound requires more random perturbation in the algorithm's output, the choice of ε embodies a direct tradeoff between the strength of the privacy guarantee and the utility of the resulting model or query [[sources/web-2025-08-21-f21]].

## Key claims

- ε ≥ 0; a smaller ε enhances privacy protection but increases the noise introduced during the query/training process, thereby degrading utility [[sources/web-2025-08-21-f21]].
- δ is the additive slack term in the (ε, δ)-DP definition, bounding the probability of privacy failures outside the ε-bound [[sources/web-2025-08-21-f21]].
- Adaptive privacy-budget allocation is identified as an active research direction in DP for deep learning, alongside hybrid privacy frameworks that combine DP with other techniques [[sources/web-2025-08-21-f21]].
- Balancing privacy and utility — operationalized through the choice of ε — is identified as one of the principal open challenges in applying DP to AI systems [[sources/web-2025-08-21-f21]].

## Sources

- [[sources/web-2025-08-21-f21]] — Zhang, X. & Zhang, Q. (2025). Defending against attacks in deep learning with differential privacy: a survey.

## Related

- [[concepts/differential-privacy]]
- [[concepts/privacy-utility-tradeoff]]
- [[concepts/dynamic-model-perturbation]]
- [[entities/zhang-2025-dp-survey]]
