---
schema_version: 1
id: arxiv-2508.10467
type: arxiv
title: 'FIRESPARQL: A LLM-based Framework for SPARQL Query Generation over Scholarly
  Knowledge Graphs'
url: https://arxiv.org/abs/2508.10467
authors:
- Xueli Pan
- Victor de Boer
- Jacco van Ossenbruggen
ingested_at: '2026-06-17T21:00:29Z'
content_hash: sha256:6453ac09a5dfee7568cc269ef6449d0d6764dbdceb35b407a1f5647d9d931d63
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2508.10467'
  categories:
  - cs.AI
  - cs.DL
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: Accepted at 17th International Joint Conference on Knowledge Discovery,
    Knowledge Engineering and Knowledge Management (IC3K)
  abstract_only: true
published_at: '2025-08-14'
filter:
  score: 0.85
---
Question answering over Scholarly Knowledge Graphs (SKGs) remains a challenging task due to the complexity of scholarly content and the intricate structure of these graphs. Large Language Model (LLM) approaches could be used to translate natural language questions (NLQs) into SPARQL queries; however, these LLM-based approaches struggle with SPARQL query generation due to limited exposure to SKG-specific content and the underlying schema. We identified two main types of errors in the LLM-generated SPARQL queries: (i) structural inconsistencies, such as missing or redundant triples in the queries, and (ii) semantic inaccuracies, where incorrect entities or properties are shown in the queries despite a correct query structure. To address these issues, we propose FIRESPARQL, a modular framework that supports fine-tuned LLMs as a core component, with optional context provided via retrieval-augmented generation (RAG) and a SPARQL query correction layer. We evaluate the framework on the SciQA Benchmark using various configurations (zero-shot, zero-shot with RAG, one-shot, fine-tuning, and fine-tuning with RAG) and compare the performance with baseline and state-of-the-art approaches. We measure query accuracy using BLEU and ROUGE metrics, and query result accuracy using relaxed exact match(RelaxedEM), with respect to the gold standards containing the NLQs, SPARQL queries, and the results of the queries. Experimental results demonstrate that fine-tuning achieves the highest overall performance, reaching 0.90 ROUGE-L for query accuracy and 0.85 RelaxedEM for result accuracy on the test set.
