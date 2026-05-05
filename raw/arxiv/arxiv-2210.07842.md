---
id: arxiv-2210.07842
type: arxiv
title: 'ENTS: An Edge-native Task Scheduling System for Collaborative Edge Computing'
url: http://arxiv.org/abs/2210.07842v1
authors:
- Mingjin Zhang
- Jiannong Cao
- Lei Yang
- Liang Zhang
- Yuvraj Sahni
- Shan Jiang
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:0c711b0f45584288073aa64ff0fcf758774562a4930335abce11b6a523900614
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2210.07842.md
  legacy_slug: arxiv_2210.07842
published_at: '2022-10-14'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# ENTS: An Edge-native Task Scheduling System for Collaborative Edge Computing

**Authors:** Mingjin Zhang, Jiannong Cao, Lei Yang, Liang Zhang, Yuvraj Sahni, Shan Jiang  
**Published:** 2022-10-14T14:13:35Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2210.07842v1.pdf

## Abstract

Collaborative edge computing (CEC) is an emerging paradigm enabling sharing of the coupled data, computation, and networking resources among heterogeneous geo-distributed edge nodes. Recently, there has been a trend to orchestrate and schedule containerized application workloads in CEC, while Kubernetes has become the de-facto standard broadly adopted by the industry and academia. However, Kubernetes is not preferable for CEC because its design is not dedicated to edge computing and neglects the unique features of edge nativeness. More specifically, Kubernetes primarily ensures resource provision of workloads while neglecting the performance requirements of edge-native applications, such as throughput and latency. Furthermore, Kubernetes neglects the inner dependencies of edge-native applications and fails to consider data locality and networking resources, leading to inferior performance. In this work, we design and develop ENTS, the first edge-native task scheduling system, to man...

## Relevance

**Score:** 3/5  
ENTS is an edge-native task scheduling system addressing latency, throughput, and data locality for containerized workloads at the edge; technically substantive (Kubernetes gaps, edge-native design) but predates AI inference workloads as the primary use case.
