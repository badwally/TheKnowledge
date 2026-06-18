---
schema_version: 1
id: arxiv-1909.02930
type: arxiv
title: Structured Query Construction via Knowledge Graph Embedding
url: https://arxiv.org/abs/1909.02930
authors:
- Ruijie Wang
- Meng Wang
- Jun Liu
- Michael Cochez
- Stefan Decker
ingested_at: '2026-06-17T20:56:27Z'
content_hash: sha256:d260a7d17a0049442dacee90be6bb4bf9cadbfade629d996321f38ff0a6c8ac7
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1909.02930'
  categories:
  - cs.AI
  - cs.CL
  - cs.LG
  doi: 10.1007/s10115-019-01401-x
  primary_category: cs.AI
  journal_ref: 'Knowledge and information Systems 62 (2020): 1819-1846'
  comment: ''
  abstract_only: true
published_at: '2019-09-06'
filter:
  score: 0.75
---
In order to facilitate the accesses of general users to knowledge graphs, an increasing effort is being exerted to construct graph-structured queries of given natural language questions. At the core of the construction is to deduce the structure of the target query and determine the vertices/edges which constitute the query. Existing query construction methods rely on question understanding and conventional graph-based algorithms which lead to inefficient and degraded performances facing complex natural language questions over knowledge graphs with large scales. In this paper, we focus on this problem and propose a novel framework standing on recent knowledge graph embedding techniques. Our framework first encodes the underlying knowledge graph into a low-dimensional embedding space by leveraging generalized local knowledge graphs. Given a natural language question, the learned embedding representations of the knowledge graph are utilized to compute the query structure and assemble vertices/edges into the target query. Extensive experiments were conducted on the benchmark dataset, and the results demonstrate that our framework outperforms state-of-the-art baseline models regarding effectiveness and efficiency.
