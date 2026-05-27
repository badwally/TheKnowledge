---
schema_version: 1
type: concept
slug: predictive-maintenance-policy
canonical_name: Predictive maintenance policy
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T21:01:10Z'
draft_unresolved_claims: 2
created_at: '2026-05-20T21:12:40Z'
last_updated: '2026-05-20T21:12:40Z'
---

# Predictive maintenance policy

## Summary

A predictive maintenance policy specifies when and what kind of maintenance action to take on a degrading system as a function of observed state; Wang et al. (2025) propose a policy that synthesizes age, degradation, and count of completed preventive maintenance actions to govern multiple types of maintenance actions for a nonstationary gamma process.

## Key claims

- Wang et al. (2025) propose a predictive maintenance policy that involves various types of maintenance actions for a nonstationary gamma process [[sources/web-2025-04-07-e6e]].
- The policy uses periodic inspections that fully reveal the degradation level of the system [[sources/web-2025-04-07-e6e]].
- Decision-making in the policy synthesizes information on age, degradation, and the number of conducted preventive maintenance actions, which the authors argue distinguishes their model from most existing models that consider only degradation states [[sources/web-2025-04-07-e6e]].
- The policy is parameterized by the maximum number of repairs and the preventive maintenance thresholds, which are jointly optimized to minimize expected average cost in an infinite horizon [[sources/web-2025-04-07-e6e]].
- The effectiveness of the policy is verified by a coating system case study [[sources/web-2025-04-07-e6e]].

## Sources

- [[sources/web-2025-04-07-e6e]]

## Related

- [[entities/optimal-pdm-nonstationary-gamma-paper]]
- [[concepts/nonstationary-gamma-process]]
- [[concepts/semi-markov-decision-process]]
- [[concepts/preventive-maintenance-threshold]]
- [[concepts/coating-system-degradation]]
