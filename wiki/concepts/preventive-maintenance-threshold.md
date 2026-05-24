---
type: concept
slug: preventive-maintenance-threshold
canonical_name: Preventive maintenance threshold
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:01:10Z'
draft_unresolved_claims: 2
---

# Preventive maintenance threshold

## Summary

A preventive maintenance threshold is a decision-theoretic control limit on observed degradation (or composite state) above which a preventive maintenance action is triggered; Wang et al. (2025) treat such thresholds, together with the maximum admissible number of repairs, as the decision variables of their semi-Markov decision-process formulation for nonstationary gamma degradation.

## Key claims

- In Wang et al. (2025), the decision variables for the predictive maintenance policy are the maximum number of repairs and the best thresholds for preventive maintenance [[sources/web-2025-04-07-e6e]].
- The thresholds are chosen by minimizing the expected average cost in an infinite time horizon [[sources/web-2025-04-07-e6e]].
- Wang et al. (2025) develop an optimization algorithm specifically to find the optimal values of the threshold-based decision variables [[sources/web-2025-04-07-e6e]].

## Sources

- [[sources/web-2025-04-07-e6e]]

## Related

- [[entities/optimal-pdm-nonstationary-gamma-paper]]
- [[concepts/predictive-maintenance-policy]]
- [[concepts/semi-markov-decision-process]]
- [[concepts/nonstationary-gamma-process]]
