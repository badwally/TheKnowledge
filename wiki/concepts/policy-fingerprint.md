---
type: concept
slug: policy-fingerprint
canonical_name: Policy fingerprint
domains:
  - ai-and-agents
---

# Policy fingerprint

## Summary

A policy fingerprint is a compact representation of a reinforcement-learning agent's current policy that is shared with its neighboring agents, used in MacoCache to stabilize multi-agent learning by giving each agent partial visibility into how its neighbors will act [[sources/pdf-f4016087ee51]].

## Key claims

- MacoCache shares the represented policy fingerprint of each agent among its neighborhood as a stabilization mechanism for multi-agent learning, addressing the non-stationarity that arises when neighboring agents update their policies simultaneously [[sources/pdf-f4016087ee51]].
- In addition to fingerprint sharing, MacoCache scales down neighborhood rewards so that each agent remains more locally focused while still benefiting from neighbor-policy information [[sources/pdf-f4016087ee51]].
- Together, policy-fingerprint sharing and scaled-down neighborhood rewards are MacoCache's answer to the partially observable, non-stationary failure mode of independent Q-learning baselines in distributed edge-caching settings [[sources/pdf-f4016087ee51]].

## Sources

- [[sources/pdf-f4016087ee51]]

## Related

- [[entities/macocache]]
- [[concepts/multi-agent-deep-reinforcement-learning]]
- [[concepts/independent-q-learning]]
- [[concepts/cooperative-edge-caching]]
