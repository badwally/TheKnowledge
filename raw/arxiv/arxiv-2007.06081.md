---
id: arxiv-2007.06081
type: arxiv
title: 'VAFL: a Method of Vertical Asynchronous Federated Learning'
url: http://arxiv.org/abs/2007.06081v1
authors:
- Tianyi Chen
- Xiao Jin
- Yuejiao Sun
- Wotao Yin
ingested_at: '2026-04-28T15:31:58Z'
content_hash: sha256:77fea62e1d27a025954669399235d374b25b19b2495563ed300561112f07fadb
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2007.06081.md
  legacy_slug: arxiv_2007.06081
published_at: '2020-07-12'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:58Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# VAFL: a Method of Vertical Asynchronous Federated Learning

**Authors:** Tianyi Chen, Xiao Jin, Yuejiao Sun, Wotao Yin  
**Published:** 2020-07-12T20:09:25Z  
**Venue:** Proc. of ICML Workshop on Federated Learning for User Privacy and Data Confidentiality, July 2020  
**PDF:** http://arxiv.org/pdf/2007.06081v1.pdf

## Abstract

Horizontal Federated learning (FL) handles multi-client data that share the same set of features, and vertical FL trains a better predictor that combine all the features from different clients. This paper targets solving vertical FL in an asynchronous fashion, and develops a simple FL method. The new method allows each client to run stochastic gradient algorithms without coordination with other clients, so it is suitable for intermittent connectivity of clients. This method further uses a new technique of perturbed local embedding to ensure data privacy and improve communication efficiency. Theoretically, we present the convergence rate and privacy level of our method for strongly convex, nonconvex and even nonsmooth objectives separately. Empirically, we apply our method to FL on various image and healthcare datasets. The results compare favorably to centralized and synchronous FL methods.

## Relevance

**Score:** 3/5  
VAFL enables vertical federated learning with asynchronous updates suitable for intermittent client connectivity, using perturbed local embeddings for privacy; directly relevant to federated edge AI with convergence guarantees and privacy analysis.
