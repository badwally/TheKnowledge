---
schema_version: 1
id: arxiv-2506.05690
type: arxiv
title: 'When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented
  Generation'
url: https://arxiv.org/abs/2506.05690
authors:
- Zhishang Xiang
- Chuanjie Wu
- Qinggang Zhang
- Shengyuan Chen
- Zijin Hong
- Xiao Huang
- Jinsong Su
ingested_at: '2026-06-17T18:14:56Z'
content_hash: sha256:525dfe7958a8869c292af2854c6a0fe17ed3f447e381f608503f68d5f53fc392
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2506.05690'
  categories:
  - cs.CL
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: All resources and analyses are collected at https://github.com/GraphRAG-Bench/GraphRAG-Benchmark
  abstract_only: true
published_at: '2025-06-06'
filter:
  score: 0.75
---
Graph retrieval-augmented generation (GraphRAG) has emerged as a powerful paradigm for enhancing large language models (LLMs) with external knowledge. It leverages graphs to model the hierarchical structure between specific concepts, enabling more coherent and effective knowledge retrieval for accurate reasoning.Despite its conceptual promise, recent studies report that GraphRAG frequently underperforms vanilla RAG on many real-world tasks. This raises a critical question: Is GraphRAG really effective, and in which scenarios do graph structures provide measurable benefits for RAG systems? To address this, we propose GraphRAG-Bench, a comprehensive benchmark designed to evaluate GraphRAG models onboth hierarchical knowledge retrieval and deep contextual reasoning. GraphRAG-Bench features a comprehensive dataset with tasks of increasing difficulty, coveringfact retrieval, complex reasoning, contextual summarization, and creative generation, and a systematic evaluation across the entire pipeline, from graph constructionand knowledge retrieval to final generation. Leveraging this novel benchmark, we systematically investigate the conditions when GraphRAG surpasses traditional RAG and the underlying reasons for its success, offering guidelines for its practical application. All related resources and analyses are collected for the community at https://github.com/GraphRAG-Bench/GraphRAG-Benchmark.
