---
schema_version: 1
id: arxiv-2606.00062
type: arxiv
title: 'Graph-Augmented Retrieval for Cross-Entity Financial Sentiment Analysis: A
  Comparative Study'
url: https://arxiv.org/abs/2606.00062
authors:
- Rajan Bastakoti
- Sagar Bhetwal
- Nirajan Acharya
- Gaurav Kumar Gupta
ingested_at: '2026-06-17T21:00:12Z'
content_hash: sha256:c0c992ee1fd5a59f5a1099e217b9a89a3a6951a9605bc761e81a325643636c01
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2606.00062'
  categories:
  - cs.CL
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2026-05-19'
filter:
  score: 0.8
---
Retrieval-Augmented Generation (RAG) has become foundational for grounding large language models in domain-specific corpora, yet conventional vector-based RAG systems are fundamentally limited in their ability to capture the structured, multi-entity relationships that underpin financial market analysis. This paper presents a comprehensive comparative study of a novel two-hop Graph-RAG architecture versus a standard vector-only baseline for cross-entity financial sentiment analysis. Our system constructs a sentiment-weighted knowledge graph of 59 equity entities from 255 news articles covering 10 major technology stocks, then augments dense retrieval with intensity-filtered graph traversal over INFLUENCES edges to surface relational evidence inaccessible to vector search alone.
  We evaluate both architectures on 100 grounded queries (30 Direct, 70 Relational) using semantic similarity, entity recall, RAGAS metrics, latency benchmarks, and ablation studies. Graph-RAG achieves a statistically significant improvement in entity recall (+6.4%, p < 0.001, Wilcoxon signed-rank) and delivers substantially more relevant answers for complex multi-entity queries (+11.7% Answer Relevancy), with gains concentrating in relational question types (+16.1%). Critically, these improvements come at no measurable cost to answer quality (delta = +0.001 semantic similarity, Cohen's d = 0.078), with a modest 22.6% increase in mean latency offset by an 80% reduction in latency variance.
  An ablation study on the graph traversal intensity threshold reveals an inverted-U relationship with answer quality, identifying tau = 0.5 as optimal over the production default of tau = 0.7. These findings characterize a precision-for-coverage trade-off inherent to graph-augmented retrieval and provide actionable architectural guidance for practitioners building RAG systems for multi-entity financial analysis.
