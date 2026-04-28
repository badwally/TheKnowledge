---
id: arxiv-2510.27051
type: arxiv
title: 'Adaptive Data Flywheel: Applying MAPE Control Loops to AI Agent Improvement'
url: http://arxiv.org/abs/2510.27051v1
authors:
- Aaditya Shukla
- Sidney Knowles
- Meenakshi Madugula
- Dave Farris
- Ryan Angilly
- Santiago Pombo
- Anbang Xu
- Lu An
- Abhinav Balasubramanian
- Tan Yu
- Jiaxiang Ren
- Rama Akkiraju
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:5c001b2e52673a9ab1fe9c23ce07a638f97d5240aadfd4c56192b3944ba84a85
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2510.27051.md
  legacy_slug: arxiv_2510.27051
published_at: '2025-10-30'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Adaptive Data Flywheel: Applying MAPE Control Loops to AI Agent Improvement

**Authors:** Aaditya Shukla, Sidney Knowles, Meenakshi Madugula, Dave Farris, Ryan Angilly, Santiago Pombo, Anbang Xu, Lu An, Abhinav Balasubramanian, Tan Yu, Jiaxiang Ren, Rama Akkiraju  
**Published:** 2025-10-30T23:41:06Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2510.27051v1.pdf

## Abstract

Enterprise AI agents must continuously adapt to maintain accuracy, reduce latency, and remain aligned with user needs. We present a practical implementation of a data flywheel in NVInfo AI, NVIDIA's Mixture-of-Experts (MoE) Knowledge Assistant serving over 30,000 employees. By operationalizing a MAPE-driven data flywheel, we built a closed-loop system that systematically addresses failures in retrieval-augmented generation (RAG) pipelines and enables continuous learning. Over a 3-month post-deployment period, we monitored feedback and collected 495 negative samples. Analysis revealed two major failure modes: routing errors (5.25\%) and query rephrasal errors (3.2\%). Using NVIDIA NeMo microservices, we implemented targeted improvements through fine-tuning. For routing, we replaced a Llama 3.1 70B model with a fine-tuned 8B variant, achieving 96\% accuracy, a 10x reduction in model size, and 70\% latency improvement. For query rephrasal, fine-tuning yielded a 3.7\% gain in accuracy a...

## Relevance

**Score:** 3/5  
Presents a MAPE-driven data flywheel for continuous improvement of NVIDIA's enterprise AI agent system (NVInfo), achieving 10x model size reduction (70B to 8B) and 70% latency improvement through fine-tuning. Demonstrates closed-loop MLOps patterns for agentic AI with quantitative deployment results relevant to edge-adjacent model efficiency.
