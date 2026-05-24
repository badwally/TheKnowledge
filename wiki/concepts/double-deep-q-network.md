---
type: concept
slug: double-deep-q-network
canonical_name: Double Deep Q-Network
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:21:02Z'
draft_unresolved_claims: 2
---

# Double Deep Q-Network

## Summary

The Double Deep Q-Network (DDQN) is a deep reinforcement-learning architecture that extends the Deep Q-Network by decoupling action selection from action evaluation across two networks, reducing the overestimation bias of single-network Q-learning. It supports value-based RL in continuous or high-dimensional state spaces.

## Key claims

- A Double Deep Q-Network architecture has been used to construct a reinforcement-learning agent that generates maintenance policies for deteriorating systems modelled by a gamma degradation process with increasingly imperfect repairs [[sources/arxiv-2505.20725]].
- DDQN-based maintenance agents can operate over a continuous degradation state space and learn flexible policies without requiring a predefined preventive threshold [[sources/arxiv-2505.20725]].
- A DDQN-based maintenance policy is reported to significantly improve long-run cost compared with other common maintenance strategies on a gamma-degradation, increasingly-imperfect-repairs environment [[sources/arxiv-2505.20725]].

## Sources

- [[sources/arxiv-2505.20725]]

## Related

- [[concepts/reinforcement-learning-maintenance]]
- [[concepts/gamma-degradation-process]]
- [[concepts/imperfect-repairs]]
- [[entities/rl-imperfect-repairs-paper]]
