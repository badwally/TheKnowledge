---
id: arxiv-2603.21389
type: arxiv
title: 'Task-Specific Efficiency Analysis: When Small Language Models Outperform Large
  Language Models'
url: http://arxiv.org/abs/2603.21389v1
authors:
- Jinghan Cao
- Yu Ma
- Xinjin Li
- Qingyang Ren
- Xiangyun Chen
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:ba206262b1eecf83cdfd3aa5a987af5293e144a45a55e5fce0354b293f99ac1d
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2603.21389.md
  legacy_slug: arxiv_2603.21389
published_at: '2026-03-22'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Task-Specific Efficiency Analysis: When Small Language Models Outperform Large Language Models

**Authors:** Jinghan Cao, Yu Ma, Xinjin Li, Qingyang Ren, Xiangyun Chen  
**Published:** 2026-03-22T20:19:45Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2603.21389v1.pdf

## Abstract

Large Language Models achieve remarkable performance but incur substantial computational costs unsuitable for resource-constrained deployments. This paper presents the first comprehensive task-specific efficiency analysis comparing 16 language models across five diverse NLP tasks. We introduce the Performance-Efficiency Ratio (PER), a novel metric integrating accuracy, throughput, memory, and latency through geometric mean normalization. Our systematic evaluation reveals that small models (0.5--3B parameters) achieve superior PER scores across all given tasks. These findings establish quantitative foundations for deploying small models in production environments prioritizing inference efficiency over marginal accuracy gains.

## Relevance

**Score:** 3/5  
Presents a systematic task-specific efficiency analysis of 16 language models using a novel Performance-Efficiency Ratio (PER) integrating accuracy, throughput, memory, and latency, demonstrating that small models (0.5–3B) dominate in resource-constrained deployment scenarios. Directly useful for edge model selection decisions.
