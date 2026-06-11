---
schema_version: 1
type: concept
slug: cross-silo-federated-learning
canonical_name: Cross-Silo Federated Learning
domains:
- data-collectives
created_at: '2026-06-10T22:23:53Z'
last_updated: '2026-06-10T22:23:53Z'
draft: true
draft_started_at: '2026-06-10T22:23:53Z'
draft_unresolved_claims: 0
---

# Cross-Silo Federated Learning

## Summary

Cross-silo federated learning is a federated learning regime whose participating parties are a small number of organizations (silos) — each contributing a substantial dataset — rather than a large population of end-user devices [[sources/arxiv-2206.03317]]. In this regime, a single data subject can appear in multiple silos, so privacy threats and defenses behave differently than in the cross-device case [[sources/arxiv-2206.03317]].

## Key claims

- In cross-silo federated learning, a single subject's data can be embodied by multiple records spread across multiple participating organizations [[sources/arxiv-2206.03317]].
- Because a subject is not necessarily co-located in one silo, neither item-level nor user-level privacy guarantees protect the subject in cross-silo federated learning, motivating subject-level privacy as the appropriate granularity [[sources/arxiv-2206.03317]].
- Subject-membership-inference risk in cross-silo federated learning depends on properties of the data, the model design and training, and the federation itself; Suri et al. (2022) systematically study these factors across several hundred synthetic federation configurations [[sources/arxiv-2206.03317]].

## Sources

- [[sources/arxiv-2206.03317]]

## Related

- [[concepts/subject-level-privacy]]
- [[concepts/subject-membership-inference-attack]]
- [[concepts/competitor-data-sharing-tradeoff]]
- [[entities/subject-membership-inference-paper]]
