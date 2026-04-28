---
id: arxiv-2603.16104
type: arxiv
title: 'Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective'
url: http://arxiv.org/abs/2603.16104v1
authors:
- Noppanat Wadlom
- Junyi Shen
- Yao Lu
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:532c7fe125d80ef005597999abc24e2efd28e7983bd81c5dd059cb9684bbde87
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2603.16104.md
  legacy_slug: arxiv_2603.16104
published_at: '2026-03-17'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective

**Authors:** Noppanat Wadlom, Junyi Shen, Yao Lu  
**Published:** 2026-03-17T04:03:18Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2603.16104v1.pdf

## Abstract

Agentic workflows are composed of sequences of interdependent Large Language Model (LLM) calls, and they have become a dominant workload in modern AI systems. These workflows exhibit extensive redundancy from overlapping prompts and intermediate results due to speculative and parallel exploration. Existing LLM serving systems, such as vLLM, focus on optimizing individual inference calls and overlook cross-call dependencies, leading to significant inefficiencies. This paper rethinks LLM and agent serving from a data systems perspective and introduces Helium, a workflow-aware serving framework that models agentic workloads as query plans and treats LLM invocations as first-class operators. Helium integrates proactive caching and cache-aware scheduling to maximize reuse across prompts, KV states, and workflows. Through these techniques, Helium bridges classic query optimization principles with LLM serving, achieving up to 1.56x speedup over state-of-the-art agent serving systems on var...

## Relevance

**Score:** 4/5  
Helium is a workflow-aware LLM serving framework that treats agentic workloads as query plans with proactive caching, cache-aware scheduling, and KV state reuse across calls, achieving 1.56x speedup; directly addresses serving efficiency for agentic workflows with system-level innovations applicable to resource-constrained edge deployments.
