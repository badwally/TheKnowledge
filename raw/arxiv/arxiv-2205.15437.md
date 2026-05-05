---
id: arxiv-2205.15437
type: arxiv
title: 'AMED: Automatic Mixed-Precision Quantization for Edge Devices'
url: http://arxiv.org/abs/2205.15437v2
authors:
- Moshe Kimhi
- Tal Rozen
- Avi Mendelson
- Chaim Baskin
ingested_at: '2026-04-28T15:31:58Z'
content_hash: sha256:fe05a4206de021b05214ba96f115fd77c1d50a305e3805ad5dc4b84c0190398c
domains:
- edge-ai-agentic
nlm_corpus_ids:
- e7f21255-0787-4091-ab69-5f79669e1501
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:58Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2205.15437.md
  legacy_slug: arxiv_2205.15437
published_at: '2022-05-30'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:58Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# AMED: Automatic Mixed-Precision Quantization for Edge Devices

**Authors:** Moshe Kimhi, Tal Rozen, Avi Mendelson, Chaim Baskin  
**Published:** 2022-05-30T21:23:22Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2205.15437v2.pdf

## Abstract

Quantized neural networks are well known for reducing the latency, power consumption, and model size without significant harm to the performance. This makes them highly appropriate for systems with limited resources and low power capacity. Mixed-precision quantization offers better utilization of customized hardware that supports arithmetic operations at different bitwidths. Quantization methods either aim to minimize the compression loss given a desired reduction or optimize a dependent variable for a specified property of the model (such as FLOPs or model size); both make the performance inefficient when deployed on specific hardware, but more importantly, quantization methods assume that the loss manifold holds a global minimum for a quantized model that copes with the global minimum of the full precision counterpart. Challenging this assumption, we argue that the optimal minimum changes as the precision changes, and thus, it is better to look at quantization as a random process,...

## Relevance

**Score:** 3/5  
AMED automates mixed-precision quantization targeting specific edge hardware constraints, challenging the assumption of a shared loss manifold across precisions; published in an edge ML special issue.
