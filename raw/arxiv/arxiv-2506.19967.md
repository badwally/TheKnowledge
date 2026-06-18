---
schema_version: 1
id: arxiv-2506.19967
type: arxiv
title: 'Inference Scaled GraphRAG: Improving Multi Hop Question Answering on Knowledge
  Graphs'
url: https://arxiv.org/abs/2506.19967
authors:
- Travis Thompson
- Seung-Hwan Lim
- Paul Liu
- Ruoying He
- Dongkuan Xu
ingested_at: '2026-06-17T20:56:21Z'
content_hash: sha256:042b3a5b0c0b8050e89b3874b52145344904392061c3b3a01eeebde1a081d1df
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2506.19967'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2025-06-24'
filter:
  score: 0.71
---
Large Language Models (LLMs) have achieved impressive capabilities in language understanding and generation, yet they continue to underperform on knowledge-intensive reasoning tasks due to limited access to structured context and multi-hop information. Retrieval-Augmented Generation (RAG) partially mitigates this by grounding generation in retrieved context, but conventional RAG and GraphRAG methods often fail to capture relational structure across nodes in knowledge graphs. We introduce Inference-Scaled GraphRAG, a novel framework that enhances LLM-based graph reasoning by applying inference-time compute scaling. Our method combines sequential scaling with deep chain-of-thought graph traversal, and parallel scaling with majority voting over sampled trajectories within an interleaved reasoning-execution loop. Experiments on the GRBench benchmark demonstrate that our approach significantly improves multi-hop question answering performance, achieving substantial gains over both traditional GraphRAG and prior graph traversal baselines. These findings suggest that inference-time scaling is a practical and architecture-agnostic solution for structured knowledge reasoning with LLMs
