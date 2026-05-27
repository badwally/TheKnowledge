---
schema_version: 1
type: concept
slug: independent-q-learning
canonical_name: Independent Q-learning
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Independent Q-learning

## Summary

Independent Q-learning (IQL) is a simple multi-agent reinforcement-learning baseline in which each agent learns its own Q-function independently while treating the other agents as part of a fixed environment — popular for its simplicity but prone to instability because the assumed environment is in fact non-stationary [[sources/pdf-f4016087ee51]].

## Key claims

- In IQL, each agent learns its own policy independently by modeling other agents as part of the environment, making it a simple yet popular approach to multi-agent learning [[sources/pdf-f4016087ee51]].
- The MacoCache authors note that IQL leads to a partially observable and non-stationary environment from any single agent's point of view, because all other agents are updating their own policies simultaneously [[sources/pdf-f4016087ee51]].
- This non-stationarity is the specific limitation that MacoCache addresses by sharing represented policy fingerprints among neighboring agents and scaling down neighborhood rewards, in order to stabilize the learning environment relative to a pure IQL baseline [[sources/pdf-f4016087ee51]].

## Sources

- [[sources/pdf-f4016087ee51]]

## Related

- [[entities/macocache]]
- [[concepts/multi-agent-deep-reinforcement-learning]]
- [[concepts/policy-fingerprint]]
