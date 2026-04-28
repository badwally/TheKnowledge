---
id: arxiv-2401.12350
type: arxiv
title: Scaling Up Quantization-Aware Neural Architecture Search for Efficient Deep
  Learning on the Edge
url: http://arxiv.org/abs/2401.12350v1
authors:
- Yao Lu
- Hiram Rayo Torres Rodriguez
- Sebastian Vogel
- Nick van de Waterlaat
- Pavol Jancura
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:40e6ec57fc3dda322f4e03852f7e705b08552a0479dd8dbb01c74de237a84cb3
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2401.12350.md
  legacy_slug: arxiv_2401.12350
published_at: '2024-01-22'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Scaling Up Quantization-Aware Neural Architecture Search for Efficient Deep Learning on the Edge

**Authors:** Yao Lu, Hiram Rayo Torres Rodriguez, Sebastian Vogel, Nick van de Waterlaat, Pavol Jancura  
**Published:** 2024-01-22T20:32:31Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2401.12350v1.pdf

## Abstract

Neural Architecture Search (NAS) has become the de-facto approach for designing accurate and efficient networks for edge devices. Since models are typically quantized for edge deployment, recent work has investigated quantization-aware NAS (QA-NAS) to search for highly accurate and efficient quantized models. However, existing QA-NAS approaches, particularly few-bit mixed-precision (FB-MP) methods, do not scale to larger tasks. Consequently, QA-NAS has mostly been limited to low-scale tasks and tiny networks. In this work, we present an approach to enable QA-NAS (INT8 and FB-MP) on large-scale tasks by leveraging the block-wise formulation introduced by block-wise NAS. We demonstrate strong results for the semantic segmentation task on the Cityscapes dataset, finding FB-MP models 33% smaller and INT8 models 17.6% faster than DeepLabV3 (INT8) without compromising task performance.

## Relevance

**Score:** 3/5  
Quantization-aware NAS (QA-NAS) scaled to large tasks for edge deployment, presented at CODAI workshop; provides concrete benchmark results on mixed-precision models for edge-targeted semantic segmentation.
