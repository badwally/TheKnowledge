---
schema_version: 1
type: concept
slug: semi-markov-decision-process
canonical_name: Semi-Markov decision process (SMDP)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:01:10Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T21:12:40Z'
last_updated: '2026-05-20T21:12:40Z'
---

# Semi-Markov decision process (SMDP)

## Summary

A semi-Markov decision process (SMDP) is a sequential-decision framework in which sojourn times between state transitions are general (not exponential) and that Wang et al. (2025) use to cast a predictive maintenance problem for nonstationary gamma degradation as the search for optimal preventive-maintenance thresholds and a maximum number of repairs minimizing expected average cost over an infinite horizon.

## Key claims

- Wang et al. (2025) address their predictive maintenance optimization for nonstationary gamma degradation as a semi-Markov decision problem [[sources/web-2025-04-07-e6e]].
- Within the SMDP formulation, the decision variables include the maximum number of repairs and the thresholds for preventive maintenance [[sources/web-2025-04-07-e6e]].
- The objective of the SMDP is to minimize the expected average cost in an infinite time horizon [[sources/web-2025-04-07-e6e]].
- Wang et al. (2025) develop an optimization algorithm to find the optimal values of the SMDP decision variables [[sources/web-2025-04-07-e6e]].

## Sources

- [[sources/web-2025-04-07-e6e]]

## Related

- [[entities/optimal-pdm-nonstationary-gamma-paper]]
- [[entities/rui-zheng]]
- [[concepts/nonstationary-gamma-process]]
- [[concepts/predictive-maintenance-policy]]
- [[concepts/preventive-maintenance-threshold]]
