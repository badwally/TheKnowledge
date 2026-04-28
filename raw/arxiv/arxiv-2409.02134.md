---
id: arxiv-2409.02134
type: arxiv
title: 'Edge AI: Evaluation of Model Compression Techniques for Convolutional Neural
  Networks'
url: http://arxiv.org/abs/2409.02134v1
authors:
- Samer Francy
- Raghubir Singh
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:b84518db3d3ec931f80f90bf21e0b68ac13d70f135588e5ccb8ca358627da053
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2409.02134.md
  legacy_slug: arxiv_2409.02134
published_at: '2024-09-02'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Edge AI: Evaluation of Model Compression Techniques for Convolutional Neural Networks

**Authors:** Samer Francy, Raghubir Singh  
**Published:** 2024-09-02T11:48:19Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2409.02134v1.pdf

## Abstract

This work evaluates the compression techniques on ConvNeXt models in image classification tasks using the CIFAR-10 dataset. Structured pruning, unstructured pruning, and dynamic quantization methods are evaluated to reduce model size and computational complexity while maintaining accuracy. The experiments, conducted on cloud-based platforms and edge device, assess the performance of these techniques. Results show significant reductions in model size, with up to 75% reduction achieved using structured pruning techniques. Additionally, dynamic quantization achieves a reduction of up to 95% in the number of parameters. Fine-tuned models exhibit improved compression performance, indicating the benefits of pre-training in conjunction with compression techniques. Unstructured pruning methods reveal trends in accuracy and compression, with limited reductions in computational complexity. The combination of OTOV3 pruning and dynamic quantization further enhances compression performance, resu...

## Relevance

**Score:** 3/5  
Evaluates structured pruning, unstructured pruning, and dynamic quantization on edge devices for ConvNeXt models; provides direct edge deployment benchmarks with compression ratios and accuracy trade-offs.
