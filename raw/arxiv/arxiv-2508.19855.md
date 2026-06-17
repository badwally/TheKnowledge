---
schema_version: 1
id: arxiv-2508.19855
type: arxiv
title: 'Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Augmented Complex
  Reasoning'
url: https://arxiv.org/abs/2508.19855
authors:
- Junnan Dong
- Siyu An
- Yifei Yu
- Qian-Wen Zhang
- Linhao Luo
- Xiao Huang
- Yunsheng Wu
- Di Yin
- Xing Sun
ingested_at: '2026-06-17T18:16:45Z'
content_hash: sha256:5560bf86bf2196acd9ca35669424df9ad350b1ecdea7044ae33fd746a09b25f4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2508.19855'
  categories:
  - cs.IR
  doi: ''
  primary_category: cs.IR
  journal_ref: ''
  comment: 19 pages, 7 figures, 6 tables
  abstract_only: true
published_at: '2025-08-27'
filter:
  score: 0.75
---
Graph retrieval-augmented generation (GraphRAG) has effectively enhanced large language models in complex reasoning by organizing fragmented knowledge into explicitly structured graphs. Prior efforts have been made to improve either graph construction or graph retrieval in isolation, yielding suboptimal performance, especially when domain shifts occur. In this paper, we propose a vertically unified agentic paradigm, Youtu-GraphRAG, to jointly connect the entire framework as an intricate integration. Specifically, (i) a seed graph schema is introduced to bound the automatic extraction agent with targeted entity types, relations and attribute types, also continuously expanded for scalability over unseen domains; (ii) To obtain higher-level knowledge upon the schema, we develop novel dually-perceived community detection, fusing structural topology with subgraph semantics for comprehensive knowledge organization. This naturally yields a hierarchical knowledge tree that supports both top-down filtering and bottom-up reasoning with community summaries; (iii) An agentic retriever is designed to interpret the same graph schema to transform complex queries into tractable and parallel sub-queries. It iteratively performs reflection for more advanced reasoning; (iv) To alleviate the knowledge leaking problem in pre-trained LLM, we propose a tailored anonymous dataset and a novel 'Anonymity Reversion' task that deeply measures the real performance of the GraphRAG frameworks. Extensive experiments across six challenging benchmarks demonstrate the robustness of Youtu-GraphRAG, remarkably moving the Pareto frontier with up to 90.71% saving of token costs and 16.62% higher accuracy over state-of-the-art baselines. The results indicate our adaptability, allowing seamless domain transfer with minimal intervention on schema.
