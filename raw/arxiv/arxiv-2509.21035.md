---
schema_version: 1
id: arxiv-2509.21035
type: arxiv
title: 'CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable
  Context Engineering'
url: https://arxiv.org/abs/2509.21035
authors:
- Yang Zhao
- Chengxiao Dai
- Wei Zhuo
- Yue Xiu
- Dusit Niyato
ingested_at: '2026-06-17T21:00:04Z'
content_hash: sha256:8aff801628f3037b53d73ff7b1a6b01e34fd009d03da92447257c77aea65bb19
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2509.21035'
  categories:
  - cs.AI
  - cs.CL
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2025-09-25'
filter:
  score: 0.85
---
Knowledge graphs provide structured context for multi-hop question answering, but deployed systems must balance answer accuracy with strict latency and cost targets while preserving provenance. Static k-hop expansions and "think-longer" prompting often over-retrieve, inflate context, and yield unpredictable runtime. We introduce CLAUSE, an agentic three-agent neuro-symbolic framework that treats context construction as a sequential decision process over knowledge graphs, deciding what to expand, which paths to follow or backtrack, what evidence to keep, and when to stop. Latency (interaction steps) and prompt cost (selected tokens) are exposed as user-specified budgets or prices, allowing per-query adaptation to trade-offs among accuracy, latency, and cost without retraining. CLAUSE employs the proposed Lagrangian-Constrained Multi-Agent Proximal Policy Optimization (LC-MAPPO) algorithm to coordinate three agents: Subgraph Architect, Path Navigator, and Context Curator, so that subgraph construction, reasoning-path discovery, and evidence selection are jointly optimized under per-query resource budgets on edge edits, interaction steps, and selected tokens. Across HotpotQA, MetaQA, and FactKG, CLAUSE yields higher EM@1 while reducing subgraph growth and end-to-end latency at equal or lower token budgets. On MetaQA-2-hop, relative to the strongest RAG baseline (GraphRAG), CLAUSE achieves +39.3 EM@1 with 18.6% lower latency and 40.9% lower edge growth. The resulting contexts are compact, provenance-preserving, and deliver predictable performance under deployment constraints.
