---
type: entity
slug: rl-imperfect-repairs-paper
canonical_name: A reinforcement learning agent for maintenance of deteriorating systems
  with increasingly imperfect repairs
entity_kind: paper
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T19:21:01Z'
draft_unresolved_claims: 1
---

# A reinforcement learning agent for maintenance of deteriorating systems with increasingly imperfect repairs

## Summary

A 2024 *Reliability Engineering & System Safety* paper proposing a gamma degradation process together with a novel maintenance model in which the beneficial effect of repairs decreases as more repairs are performed, and developing a Double Deep Q-Network reinforcement-learning agent that generates maintenance policies for this setting without a predefined preventive threshold.

## Key facts

- The paper is authored by Alberto Pliego Marugán, Jesús M. Pinar-Pérez, and Fausto Pedro García Márquez and was published in *Reliability Engineering & System Safety*, volume 252, article 110466, December 2024 (DOI 10.1016/j.ress.2024.110466) [[sources/arxiv-2505.20725]].
- The arXiv preprint identifier is 2505.20725, classified under cs.LG (primary) with cross-listing in math.OC [[sources/arxiv-2505.20725]].
- The paper proposes a gamma degradation process together with a novel maintenance model in which repairs are increasingly imperfect — the beneficial effect of system repairs decreases as more repairs are performed, reflecting the degradational behavior of real-world systems [[sources/arxiv-2505.20725]].
- To generate maintenance policies for this system, the authors developed a reinforcement-learning-based agent using a Double Deep Q-Network architecture [[sources/arxiv-2505.20725]].
- The authors claim two advantages for the agent: it works without a predefined preventive threshold, and it can operate in a continuous degradation state space [[sources/arxiv-2505.20725]].
- The authors performed an analysis of how changes in the main parameters of the environment affect the maintenance policy proposed by the agent, claiming the agent shows great flexibility across scenarios [[sources/arxiv-2505.20725]].
- The proposed approach is reported to significantly improve long-run cost compared with other common maintenance strategies [[sources/arxiv-2505.20725]].
- The motivation is framed in terms of Industry 4.0 driving a need for new paradigms of maintenance optimization, with reinforcement learning identified by the authors as one of the most promising machine-learning techniques for this purpose [[sources/arxiv-2505.20725]].

## Sources

- [[sources/arxiv-2505.20725]]

## Related

- [[entities/alberto-pliego-marugan]]
- [[entities/jesus-pinar-perez]]
- [[entities/fausto-garcia-marquez]]
- [[concepts/gamma-degradation-process]]
- [[concepts/imperfect-repairs]]
- [[concepts/reinforcement-learning-maintenance]]
- [[concepts/double-deep-q-network]]
