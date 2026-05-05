---
id: arxiv-2603.28622
type: arxiv
title: Trust-Aware Routing for Distributed Generative AI Inference at the Edge
url: http://arxiv.org/abs/2603.28622v1
authors:
- Chanh Nguyen
- Erik Elmroth
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:a01528245272125a1a941c370e76d5de2c637a3131aa0424a469b5be51abc78a
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2603.28622.md
  legacy_slug: arxiv_2603.28622
published_at: '2026-03-30'
filter:
  score: 1.0
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Trust-Aware Routing for Distributed Generative AI Inference at the Edge

**Authors:** Chanh Nguyen, Erik Elmroth  
**Published:** 2026-03-30T16:07:11Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2603.28622v1.pdf

## Abstract

Emerging deployments of Generative AI increasingly execute inference across decentralized and heterogeneous edge devices rather than on a single trusted server. In such environments, a single device failure or misbehavior can disrupt the entire inference process, making traditional best-effort peer-to-peer routing insufficient. Coordinating distributed generative inference therefore requires mechanisms that explicitly account for reliability, performance variability, and trust among participating peers.   In this paper, we present G-TRAC, a trust-aware coordination framework that integrates algorithmic path selection with system-level protocol design to ensure robust distributed inference. First, we formulate the routing problem as a \textit{Risk-Bounded Shortest Path} computation and introduce a polynomial-time solution that combines trust-floor pruning with Dijkstra's search, achieving sub-millisecond median routing latency at practical edge scales, and remaining below 10 ms at la...

## Relevance

**Score:** 5/5  
G-TRAC directly addresses trust-aware routing for distributed generative AI inference across heterogeneous edge devices, with a polynomial-time Risk-Bounded Shortest Path algorithm achieving sub-millisecond median routing latency; this is a precise technical contribution at the edge+agentic inference intersection with benchmarks.
