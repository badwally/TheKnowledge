---
id: arxiv-2403.17154
type: arxiv
title: On the Impact of Black-box Deployment Strategies for Edge AI on Latency and
  Model Performance
url: http://arxiv.org/abs/2403.17154v4
authors:
- Jaskirat Singh
- Emad Fallahzadeh
- Bram Adams
- Ahmed E. Hassan
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:efa646d817ff6a8894c9981b6cc596a93e558c809cc3bbdebdbb7ff7d8d47c74
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2403.17154.md
  legacy_slug: arxiv_2403.17154
published_at: '2024-03-25'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# On the Impact of Black-box Deployment Strategies for Edge AI on Latency and Model Performance

**Authors:** Jaskirat Singh, Emad Fallahzadeh, Bram Adams, Ahmed E. Hassan  
**Published:** 2024-03-25T20:09:46Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2403.17154v4.pdf

## Abstract

Deciding what combination of operators to use across the Edge AI tiers to achieve specific latency and model performance requirements is an open question for MLOps engineers. This study aims to empirically assess the accuracy vs inference time trade-off of different black-box Edge AI deployment strategies, i.e., combinations of deployment operators and deployment tiers. In this paper, we conduct inference experiments involving 3 deployment operators (i.e., Partitioning, Quantization, Early Exit), 3 deployment tiers (i.e., Mobile, Edge, Cloud) and their combinations on four widely used Computer-Vision models to investigate the optimal strategies from the point of view of MLOps developers. Our findings suggest that Edge deployment using the hybrid Quantization + Early Exit operator could be preferred over non-hybrid operators (Quantization/Early Exit on Edge, Partition on Mobile-Edge) when faster latency is a concern at medium accuracy loss. However, when minimizing accuracy loss is a...

## Relevance

**Score:** 4/5  
Empirically evaluates combinations of partitioning, quantization, and early exit operators across mobile/edge/cloud tiers on CV models; provides actionable MLOps guidance for edge AI deployment trade-offs with latency and accuracy data.
