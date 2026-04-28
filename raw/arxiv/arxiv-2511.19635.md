---
id: arxiv-2511.19635
type: arxiv
title: 'Agint: Agentic Graph Compilation for Software Engineering Agents'
url: http://arxiv.org/abs/2511.19635v1
authors:
- Abhi Chivukula
- Jay Somasundaram
- Vijay Somasundaram
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:f1f0d2188fcfb7dc9e0437d0dc581dea1a4c90b857d806e405ebf683e9fcdd0f
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2511.19635.md
  legacy_slug: arxiv_2511.19635
published_at: '2025-11-24'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Agint: Agentic Graph Compilation for Software Engineering Agents

**Authors:** Abhi Chivukula, Jay Somasundaram, Vijay Somasundaram  
**Published:** 2025-11-24T19:10:47Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2511.19635v1.pdf

## Abstract

LLM-based coding agents are increasingly common but still face challenges in context management, latency, reliability, reproducibility, and scalability. We present Agint, an agentic graph compiler, interpreter, and runtime that incrementally and hierarchically converts natural-language instructions into typed, effect-aware code DAGs. Agint introduces explicit type floors (text to data to spec to code) grounded in semantic graph transformations and a hybrid LLM and function-based JIT runtime. This enables dynamic graph refinement, reproducible and optimizable execution, speculative evaluation, and interoperability with existing developer tools. Agint's typed graph bindings improve reliability and allow concurrent composition of concurrent codebases by construction, supporting accelerated development with smaller and faster models, lower latency, efficient context utilization, and higher throughput. Hierarchical compilation allows scalable graph edits, while the graph structure suppor...

## Relevance

**Score:** 3/5  
Agint is an agentic graph compiler with speculative evaluation, smaller/faster model support, and lower latency through typed DAG compilation; the efficiency focus — accelerated development with smaller models and lower context overhead — is directly relevant to edge deployment constraints.
