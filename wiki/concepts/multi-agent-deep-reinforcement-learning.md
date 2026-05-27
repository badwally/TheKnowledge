---
schema_version: 1
type: concept
slug: multi-agent-deep-reinforcement-learning
canonical_name: Multi-agent deep reinforcement learning
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Multi-agent deep reinforcement learning

## Summary

Multi-agent deep reinforcement learning (MADRL) extends single-agent deep reinforcement learning by treating each entity in a distributed system as its own learning agent that cooperates with — or competes against — other agents, enabling adaptive control in environments where a centralized agent would face an explosive joint action space [[sources/pdf-f4016087ee51]].

## Key claims

- Traditional deep reinforcement learning typically uses a single centralized learning agent, which is infeasible for massively distributed problem settings such as edge caching, where the joint action space across edges grows explosively [[sources/pdf-f4016087ee51]].
- MADRL addresses this by treating each distributed entity (e.g., each edge base station) as its own learning agent, with cooperations facilitated among neighboring agents to achieve collaborative intelligence [[sources/pdf-f4016087ee51]].
- In MacoCache, MADRL is instantiated with the advantage actor-critic method per agent: an actor network outputs caching-replacement actions and a critic network provides feedback on the selected action [[sources/pdf-f4016087ee51]].
- LSTM units are integrated with the actor-critic model so that each agent can adapt to the sequential characteristics of historical requests and handle time-series dynamics and diversity [[sources/pdf-f4016087ee51]].
- A core design issue in MADRL is that each agent's environment is partially observable and non-stationary because other agents are simultaneously updating their own policies; MacoCache addresses this by sharing a represented policy fingerprint among neighborhoods and scaling down neighborhood rewards so each agent remains locally focused [[sources/pdf-f4016087ee51]].
- Real trace-driven evaluation of the MADRL-based MacoCache framework reports an average 21% latency and 26% cost reduction relative to the state-of-the-art learning-based caching baseline, evidence that MADRL can outperform centralized or independent learners on massively distributed control problems [[sources/pdf-f4016087ee51]].

## Sources

- [[sources/pdf-f4016087ee51]]

## Related

- [[entities/macocache]]
- [[concepts/cooperative-edge-caching]]
- [[concepts/independent-q-learning]]
- [[concepts/policy-fingerprint]]
- [[concepts/mobile-edge-caching]]
