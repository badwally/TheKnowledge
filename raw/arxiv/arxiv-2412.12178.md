---
id: arxiv-2412.12178
type: arxiv
title: Activation Sparsity Opportunities for Compressing General Large Language Models
url: http://arxiv.org/abs/2412.12178v2
authors:
- Nobel Dhar
- Bobin Deng
- Md Romyull Islam
- Kazi Fahim Ahmad Nasif
- Liang Zhao
- Kun Suo
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:c1295f5d27132270b1f222481c8e7c333d6c1f4eb3771b57c62a12e700d94280
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2412.12178.md
  legacy_slug: arxiv_2412.12178
published_at: '2024-12-13'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Activation Sparsity Opportunities for Compressing General Large Language Models

**Authors:** Nobel Dhar, Bobin Deng, Md Romyull Islam, Kazi Fahim Ahmad Nasif, Liang Zhao, Kun Suo  
**Published:** 2024-12-13T02:26:54Z  
**Venue:** 2024 IEEE International Performance, Computing, and Communications Conference (IPCCC), Orlando, FL, USA, 2024  
**PDF:** http://arxiv.org/pdf/2412.12178v2.pdf

## Abstract

Deploying local AI models, such as Large Language Models (LLMs), to edge devices can substantially enhance devices' independent capabilities, alleviate the server's burden, and lower the response time. Owing to these tremendous potentials, many big tech companies have released several lightweight Small Language Models (SLMs) to bridge this gap. However, we still have huge motivations to deploy more powerful (LLMs) AI models on edge devices and enhance their smartness level. Unlike the conventional approaches for AI model compression, we investigate activation sparsity. The activation sparsity method is orthogonal and combinable with existing techniques to maximize the compression rate while maintaining great accuracy. LLMs' Feed-Forward Network (FFN) components, which typically comprise a large proportion of parameters (around 2/3), ensure that our FFN optimizations would have a better chance of achieving effective compression. Moreover, our findings are beneficial to general LLMs a...

## Relevance

**Score:** 4/5  
Directly targets LLM deployment on edge devices by exploiting activation sparsity in FFN layers, which comprise ~2/3 of parameters. Orthogonal to quantization/pruning and applicable to general LLMs, with peer-reviewed results at IEEE IPCCC 2024.
