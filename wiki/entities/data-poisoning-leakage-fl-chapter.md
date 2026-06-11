---
schema_version: 1
type: entity
slug: data-poisoning-leakage-fl-chapter
canonical_name: Data Poisoning and Leakage Analysis in Federated Learning (Wei et
  al., 2024)
entity_kind: paper
domains:
- data-collectives
created_at: '2026-06-10T22:24:13Z'
last_updated: '2026-06-10T22:24:13Z'
draft: true
draft_started_at: '2026-06-10T22:24:13Z'
draft_unresolved_claims: 0
---

# Data Poisoning and Leakage Analysis in Federated Learning (Wei et al., 2024)

## Summary

"Data Poisoning and Leakage Analysis in Federated Learning" is a 2024 book chapter in the *Handbook of Trustworthy Federated Learning* by Wenqi Wei, Tiansheng Huang, Zachary Yahn, Anoop Singhal, Margaret Loper, and Ling Liu, with Anoop Singhal of NIST as a co-author [[sources/arxiv-2409.13004]]. It analyzes the two threats the authors treat as dominant for federated learning deployment — training data privacy intrusion via gradient leakage, and training data poisoning leading to model Trojan attacks — and argues for dynamic model perturbation as a unified defense aimed at jointly preserving privacy, poisoning resilience, and model utility [[sources/arxiv-2409.13004]].

## Key facts

- Chapter of the *Handbook of Trustworthy Federated Learning* (Springer, 2024), DOI 10.1007/978-3-031-58923-2_3 [[sources/arxiv-2409.13004]].
- Authors: Wenqi Wei, Tiansheng Huang, Zachary Yahn, Anoop Singhal (NIST), Margaret Loper, Ling Liu [[sources/arxiv-2409.13004]].
- Posted to arXiv 2024-09-19 as 2409.13004; primary category cs.LG [[sources/arxiv-2409.13004]].
- Identifies two dominant threats to federated learning: training-data privacy intrusion (gradient leakage) and training-data poisoning that can install model Trojans [[sources/arxiv-2409.13004]].
- Proposes gradient perturbation — controlled randomized noise added to the raw gradient update before sharing during each FL round — as the primary defense against gradient leakage [[sources/arxiv-2409.13004]].
- Identifies the *amount* of noise and the *location* at which noise is added as the two design knobs that determine effectiveness of gradient perturbation [[sources/arxiv-2409.13004]].
- Categorizes representative data-poisoning attacks and compares the effectiveness of their respective mitigation techniques rather than offering a single universal defense [[sources/arxiv-2409.13004]].
- Advances dynamic model perturbation as a defense that targets privacy protection, poisoning resilience, and model performance jointly, on empirical grounds [[sources/arxiv-2409.13004]].
- Names skewness (non-IID data), data and algorithmic biases, and training-data misinformation as additional federated-learning risk factors beyond poisoning and leakage [[sources/arxiv-2409.13004]].

## Sources

- [[sources/arxiv-2409.13004]] — Data Poisoning and Leakage Analysis in Federated Learning (2024)

## Related

- [[concepts/gradient-inversion-attack]]
- [[concepts/gradient-inversion-defense]]
- [[concepts/training-data-poisoning]]
- [[concepts/model-trojan-attack]]
- [[concepts/dynamic-model-perturbation]]
- [[concepts/cross-silo-federated-learning]]
- [[entities/subject-membership-inference-paper]]
