---
id: arxiv-2506.20000
type: arxiv
title: Can One Safety Loop Guard Them All? Agentic Guard Rails for Federated Computing
url: http://arxiv.org/abs/2506.20000v1
authors:
- Narasimha Raghavan Veeraragavan
- Jan Franz Nygård
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:f522a794b6025698c751d972914c66a5b1340dba29a664cdcb1f50660b682571
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2506.20000.md
  legacy_slug: arxiv_2506.20000
published_at: '2025-06-24'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Can One Safety Loop Guard Them All? Agentic Guard Rails for Federated Computing

**Authors:** Narasimha Raghavan Veeraragavan, Jan Franz Nygård  
**Published:** 2025-06-24T20:39:49Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2506.20000v1.pdf

## Abstract

We propose Guardian-FC, a novel two-layer framework for privacy preserving federated computing that unifies safety enforcement across diverse privacy preserving mechanisms, including cryptographic back-ends like fully homomorphic encryption (FHE) and multiparty computation (MPC), as well as statistical techniques such as differential privacy (DP). Guardian-FC decouples guard-rails from privacy mechanisms by executing plug-ins (modular computation units), written in a backend-neutral, domain-specific language (DSL) designed specifically for federated computing workflows and interchangeable Execution Providers (EPs), which implement DSL operations for various privacy back-ends. An Agentic-AI control plane enforces a finite-state safety loop through signed telemetry and commands, ensuring consistent risk management and auditability. The manifest-centric design supports fail-fast job admission and seamless extensibility to new privacy back-ends. We present qualitative scenarios illustra...

## Relevance

**Score:** 3/5  
Guardian-FC introduces a two-layer agentic AI safety framework for federated computing with FHE, MPC, and differential privacy backends; addresses agentic AI control planes in distributed privacy-preserving environments with concrete DSL and EP design.
