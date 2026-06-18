---
schema_version: 1
id: arxiv-2504.02112
type: arxiv
title: 'PolyG: Adaptive Graph Traversal for Diverse GraphRAG Questions'
url: https://arxiv.org/abs/2504.02112
authors:
- Renjie Liu
- Haitian Jiang
- Xiao Yan
- Bo Tang
- Jinyang Li
ingested_at: '2026-06-17T20:56:18Z'
content_hash: sha256:b0daefaa5adb6ae504e44307f0ba8dfa682662bc7539ab43f10b1a9f7141964f
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2504.02112'
  categories:
  - cs.LG
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2025-04-02'
filter:
  score: 0.75
---
GraphRAG enhances large language models (LLMs) to generate quality answers for user questions by retrieving related facts from external knowledge graphs. However, current GraphRAG methods are primarily evaluated on and overly tailored for knowledge graph question answering (KGQA) benchmarks, which are biased towards a few specific question patterns and do not reflect the diversity of real-world questions. To better evaluate GraphRAG methods, we propose a complete four-class taxonomy to categorize the basic patterns of knowledge graph questions and use it to create PolyBench, a new GraphRAG benchmark encompassing a comprehensive set of graph questions. With the new benchmark, we find that existing GraphRAG methods fall short in effectiveness (i.e., quality of the generated answers) and/or efficiency (i.e., response time or token usage) because they adopt either a fixed graph traversal strategy or free-form exploration by LLMs for fact retrieval. However, different question patterns require distinct graph traversal strategies and context formation. To facilitate better retrieval, we propose PolyG, an adaptive GraphRAG approach by decomposing and categorizing the questions according to our proposed question taxonomy. Built on top of a unified interface and execution engine, PolyG dynamically prompts an LLM to generate a graph database query to retrieve the context for each decomposed basic question. Compared with SOTA GraphRAG methods, PolyG achieves a higher win rate in generation quality and has a low response latency and token cost. Our code and benchmark are open-source at https://github.com/Liu-rj/PolyG.
