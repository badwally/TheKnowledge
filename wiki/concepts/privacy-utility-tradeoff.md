---
schema_version: 1
type: concept
slug: privacy-utility-tradeoff
canonical_name: Privacy–Utility Tradeoff
domains:
- data-collectives
created_at: '2026-06-10T22:25:30Z'
last_updated: '2026-06-10T22:25:30Z'
draft: true
draft_started_at: '2026-06-10T22:25:30Z'
draft_unresolved_claims: 0
---

# Privacy–Utility Tradeoff

## Summary

The privacy–utility tradeoff is the central design tension in any differentially-private machine learning system: tighter privacy guarantees (smaller ε in (ε, δ)-DP) require more random perturbation during training or inference, which degrades model accuracy and other measures of utility [[sources/web-2025-08-21-f21]]. Balancing privacy against utility is identified as one of the principal open challenges in the survey literature on DP for AI and deep learning [[sources/web-2025-08-21-f21]].

## Key claims

- A smaller privacy budget ε enhances privacy protection but increases the noise injected during the query/training process, thereby lowering model utility [[sources/web-2025-08-21-f21]].
- Balancing privacy and utility is a recurring theme across DP-for-ML surveys; adaptive privacy-budget allocation and hybrid privacy frameworks are proposed future directions for improving the achievable Pareto frontier [[sources/web-2025-08-21-f21]].
- For pooled-data and federated-model settings — including the survey's running example of multiple hospitals jointly training an online medical service via federated learning — the tradeoff specifically governs whether the privacy-protected joint model retains enough utility to justify the pooling arrangement [[sources/web-2025-08-21-f21]].
- Beyond accuracy, DP perturbation has secondary positive effects on generalization (reduced overfitting) and adversarial robustness, complicating any utility accounting that looks only at clean-test accuracy [[sources/web-2025-08-21-f21]].

## Sources

- [[sources/web-2025-08-21-f21]] — Zhang, X. & Zhang, Q. (2025). Defending against attacks in deep learning with differential privacy: a survey.

## Related

- [[concepts/differential-privacy]]
- [[concepts/privacy-budget]]
- [[concepts/cross-silo-federated-learning]]
- [[concepts/dynamic-model-perturbation]]
- [[entities/zhang-2025-dp-survey]]
