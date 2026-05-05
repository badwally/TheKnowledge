---
id: arxiv-2405.00839
type: arxiv
title: Communication-Efficient Training Workload Balancing for Decentralized Multi-Agent
  Learning
url: http://arxiv.org/abs/2405.00839v1
authors:
- Seyed Mahmoud Sajjadi Mohammadabadi
- Lei Yang
- Feng Yan
- Junshan Zhang
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:56781baa79a3a7b5639fde8f2d4100177796fafe19e733e917d0528c884151fd
domains:
- edge-ai-agentic
nlm_corpus_ids:
- e7f21255-0787-4091-ab69-5f79669e1501
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2405.00839.md
  legacy_slug: arxiv_2405.00839
published_at: '2024-05-01'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Communication-Efficient Training Workload Balancing for Decentralized Multi-Agent Learning

**Authors:** Seyed Mahmoud Sajjadi Mohammadabadi, Lei Yang, Feng Yan, Junshan Zhang  
**Published:** 2024-05-01T20:03:37Z  
**Venue:** 2024 IEEE 44th International Conference on Distributed Computing Systems (ICDCS)  
**PDF:** http://arxiv.org/pdf/2405.00839v1.pdf

## Abstract

Decentralized Multi-agent Learning (DML) enables collaborative model training while preserving data privacy. However, inherent heterogeneity in agents' resources (computation, communication, and task size) may lead to substantial variations in training time. This heterogeneity creates a bottleneck, lengthening the overall training time due to straggler effects and potentially wasting spare resources of faster agents. To minimize training time in heterogeneous environments, we present a Communication-Efficient Training Workload Balancing for Decentralized Multi-Agent Learning (ComDML), which balances the workload among agents through a decentralized approach. Leveraging local-loss split training, ComDML enables parallel updates, where slower agents offload part of their workload to faster agents. To minimize the overall training time, ComDML optimizes the workload balancing by jointly considering the communication and computation capacities of agents, which hinges upon integer progra...

## Relevance

**Score:** 3/5  
ComDML balances training workloads across heterogeneous decentralized agents in edge computing, enabling faster agents to absorb slower agents' compute via local-loss split training; published at ICDCS 2024 with edge computing and federated learning keywords.
