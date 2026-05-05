---
id: arxiv-2601.20655
type: arxiv
title: 'OnePiece: A Large-Scale Distributed Inference System with RDMA for Complex
  AI-Generated Content (AIGC) Workflows'
url: http://arxiv.org/abs/2601.20655v1
authors:
- June Chen
- Neal Xu
- Gragas Huang
- Bok Zhou
- Stephen Liu
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:84c665afe64fd21bd5e103f4589f4b84479eee25ad31da2f5b872f504896db45
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2601.20655.md
  legacy_slug: arxiv_2601.20655
published_at: '2026-01-28'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# OnePiece: A Large-Scale Distributed Inference System with RDMA for Complex AI-Generated Content (AIGC) Workflows

**Authors:** June Chen, Neal Xu, Gragas Huang, Bok Zhou, Stephen Liu  
**Published:** 2026-01-28T14:38:16Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2601.20655v1.pdf

## Abstract

The rapid growth of AI-generated content (AIGC) has enabled high-quality creative production across diverse domains, yet existing systems face critical inefficiencies in throughput, resource utilization, and scalability under concurrent workloads. This paper introduces OnePiece, a large-scale distributed inference system with RDMA optimized for multi-stage AIGC workflows. By decomposing pipelines into fine-grained microservices and leveraging one-sided RDMA communication, OnePiece significantly reduces inter-node latency and CPU overhead while improving GPU utilization. The system incorporates a novel double-ring buffer design to resolve deadlocks in RDMA-aware memory access without CPU involvement. Additionally, a dynamic Node Manager allocates resources elastically across workflow stages in response to real-time load. Experimental results demonstrate that OnePiece reduces GPU resource consumption by 16x in Wan2.1 image-to-video generation compared to monolithic inference pipelines...

## Relevance

**Score:** 3/5  
OnePiece is a distributed inference system using RDMA and microservice decomposition for multi-stage AIGC workflows, achieving 16x GPU resource reduction; addresses distributed inference infrastructure with concrete hardware-level optimizations relevant to edge serving.
