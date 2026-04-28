---
id: arxiv-2509.11079
type: arxiv
title: Difficulty-Aware Agentic Orchestration for Query-Specific Multi-Agent Workflows
url: http://arxiv.org/abs/2509.11079v5
authors:
- Jinwei Su
- Qizhen Lan
- Yinghui Xia
- Lifan Sun
- Weiyou Tian
- Tianyu Shi
- Xinyuan Song
- Lewei He
- Yang Jingsong
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:c1b7ee5faf8639b36f5ca6c28c5535dc628ce6a3f388b31b0ac4d33706aa857c
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2509.11079.md
  legacy_slug: arxiv_2509.11079
published_at: '2025-09-14'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Difficulty-Aware Agentic Orchestration for Query-Specific Multi-Agent Workflows

**Authors:** Jinwei Su, Qizhen Lan, Yinghui Xia, Lifan Sun, Weiyou Tian, Tianyu Shi, Xinyuan Song, Lewei He, Yang Jingsong  
**Published:** 2025-09-14T03:57:43Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2509.11079v5.pdf

## Abstract

Large Language Model (LLM)-based agentic systems have shown strong capabilities across various tasks. However, existing multi-agent frameworks often rely on static or task-level workflows, which either over-process simple queries or underperform on complex ones, while also neglecting the efficiency-performance trade-offs across heterogeneous LLMs. To address these limitations, we propose Difficulty-Aware Agentic Orchestration (DAAO), which can dynamically generate query-specific multi-agent workflows guided by predicted query difficulty. DAAO comprises three interdependent modules: a variational autoencoder (VAE) for difficulty estimation, a modular operator allocator, and a cost- and performance-aware LLM router. A self-adjusting policy updates difficulty estimates based on workflow success, enabling simpler workflows for easy queries and more complex strategies for harder ones. Experiments on six benchmarks demonstrate that DAAO surpasses prior multi-agent systems in both accuracy...

## Relevance

**Score:** 3/5  
DAAO dynamically generates query-specific multi-agent workflows using difficulty estimation, a modular operator allocator, and a cost- and performance-aware LLM router; addresses efficiency-performance tradeoffs across heterogeneous LLMs relevant to constrained deployment settings.
