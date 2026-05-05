---
id: arxiv-2509.02121
type: arxiv
title: Batch Query Processing and Optimization for Agentic Workflows
url: http://arxiv.org/abs/2509.02121v2
authors:
- Junyi Shen
- Noppanat Wadlom
- Yao Lu
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:03bfaa343c4cb2f4d92e24767f7ecc61f8ad30b28fdf8dfd8caaa549a8ee1d31
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2509.02121.md
  legacy_slug: arxiv_2509.02121
published_at: '2025-09-02'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Batch Query Processing and Optimization for Agentic Workflows

**Authors:** Junyi Shen, Noppanat Wadlom, Yao Lu  
**Published:** 2025-09-02T09:17:40Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2509.02121v2.pdf

## Abstract

Large Language Models (LLMs) in agentic workflows combine multi-step reasoning, heterogeneous tool use, and collaboration across multiple specialized agents. Existing LLM serving engines optimize individual calls in isolation, while multi-agent frameworks focus on orchestration without system-level performance planning. As a result, repeated prompts, overlapping contexts, and fragmented CPU-GPU execution create substantial redundancy and poor hardware utilization, especially in batch analytics scenarios. We introduce Halo, a system that brings batch query processing and optimization into agentic LLM workflows. Halo represents each workflow as a structured query plan DAG and constructs a consolidated graph for batched queries that exposes shared computation. Guided by a cost model that jointly considers heterogeneous resource constraints, prefill and decode costs, cache reuse, and GPU placement, Halo performs plan-level optimization to minimize redundant execution. The Processor inte...

## Relevance

**Score:** 4/5  
Halo brings batch query processing and DAG-level optimization to agentic LLM workflows, with a cost model covering heterogeneous resource constraints, cache reuse, and GPU placement; system-level contributions directly applicable to efficient agentic serving at the edge.
