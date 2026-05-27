---
schema_version: 1
type: entity
slug: macocache
canonical_name: MacoCache
entity_kind: paper
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# MacoCache

## Summary

MacoCache is an intelligent mobile-edge video-caching framework that frames each base-station edge server as a cooperating reinforcement-learning agent and uses multi-agent deep reinforcement learning (MADRL) with an LSTM-augmented advantage actor-critic to minimize content access latency and traffic cost in massively distributed, dynamic edge environments [[sources/pdf-f4016087ee51]].

## Key facts

- Authored by Fangxin Wang, Feng Wang, Jiangchuan Liu, Ryan Shea, and Lifeng Sun, spanning Simon Fraser University (School of Computing Science), the University of Mississippi (Department of Computer and Information Science), and Tsinghua University (Department of Computer Science and Technology) [[sources/pdf-f4016087ee51]].
- Motivated by a large-scale trace analysis on iQiYi mobile-user video-watching data from Beijing, covering about 17 million sessions over two weeks in May, which the authors use to argue that edge caching environments are far more dynamic and diverse than CDN caching environments [[sources/pdf-f4016087ee51]].
- Adopts the state-of-the-art advantage actor-critic method as the per-agent learner: an actor network outputs caching-replacement actions, and a critic network provides feedback on the selected action [[sources/pdf-f4016087ee51]].
- Integrates a long short-term memory (LSTM) network with the actor-critic model to capture sequential characteristics of historical request streams and adapt to time-series dynamics and diversity [[sources/pdf-f4016087ee51]].
- Stabilizes multi-agent learning by sharing each agent's represented policy fingerprint with its neighborhood and scaling down neighborhood rewards so that each agent stays more locally focused [[sources/pdf-f4016087ee51]].
- Critiques independent Q-learning (IQL) as the simple-but-popular cooperative baseline, noting it produces a partially observable and non-stationary environment because all agents update their policies simultaneously, motivating MacoCache's policy-fingerprint sharing [[sources/pdf-f4016087ee51]].
- In real trace-driven evaluation, MacoCache reports an average reduction of 21% latency and 26% cost relative to the state-of-the-art learning-based caching solution [[sources/pdf-f4016087ee51]].

## Sources

- [[sources/pdf-f4016087ee51]] — Intelligent Video Caching at Network Edge: A Multi-Agent Deep Reinforcement Learning Approach

## Related

- [[entities/fangxin-wang]]
- [[entities/jiangchuan-liu]]
- [[entities/simon-fraser-university]]
- [[entities/iqiyi]]
- [[concepts/mobile-edge-caching]]
- [[concepts/multi-agent-deep-reinforcement-learning]]
- [[concepts/cooperative-edge-caching]]
- [[concepts/independent-q-learning]]
- [[concepts/policy-fingerprint]]
