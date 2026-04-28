---
id: arxiv-2601.00848
type: arxiv
title: 'Temporal Attack Pattern Detection in Multi-Agent AI Workflows: An Open Framework
  for Training Trace-Based Security Models'
url: http://arxiv.org/abs/2601.00848v1
authors:
- Ron F. Del Rosario
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:b90900e69a86f083f416bf59c71e870a7d4a37877cfc6e6eab5c0ea16417f0ae
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2601.00848.md
  legacy_slug: arxiv_2601.00848
published_at: '2025-12-29'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Temporal Attack Pattern Detection in Multi-Agent AI Workflows: An Open Framework for Training Trace-Based Security Models

**Authors:** Ron F. Del Rosario  
**Published:** 2025-12-29T09:41:22Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2601.00848v1.pdf

## Abstract

We present an openly documented methodology for fine-tuning language models to detect temporal attack patterns in multi-agent AI workflows using OpenTelemetry trace analysis. We curate a dataset of 80,851 examples from 18 public cybersecurity sources and 35,026 synthetic OpenTelemetry traces. We apply iterative QLoRA fine-tuning on resource-constrained ARM64 hardware (NVIDIA DGX Spark) through three training iterations with strategic augmentation. Our custom benchmark accuracy improves from 42.86% to 74.29%, a statistically significant 31.4-point gain. Targeted examples addressing specific knowledge gaps outperform indiscriminate scaling. Key contributions include: (1) synthetic trace generation methodology for multi-agent coordination attacks and regulatory violations, (2) empirical evidence that training data composition fundamentally determines behavior, and (3) complete open release of datasets, training scripts, and evaluation benchmarks on HuggingFace. While practical deployme...

## Relevance

**Score:** 3/5  
Demonstrates QLoRA fine-tuning of security models for detecting attack patterns in multi-agent workflow traces on resource-constrained ARM64 hardware; addresses agentic AI security with on-device training relevance, though depth is limited by single-author preprint quality.
