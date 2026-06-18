---
schema_version: 1
id: arxiv-2409.08820
type: arxiv
title: A RAG Approach for Generating Competency Questions in Ontology Engineering
url: https://arxiv.org/abs/2409.08820
authors:
- Xueli Pan
- Jacco van Ossenbruggen
- Victor de Boer
- Zhisheng Huang
ingested_at: '2026-06-17T19:25:52Z'
content_hash: sha256:10964986a5f24533f08e06eaec01ee652084e6b2f76672f933adf2d4f4d98ce7
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2409.08820'
  categories:
  - cs.AI
  doi: ''
  primary_category: cs.AI
  journal_ref: 18th International Conference on Metadata and Semantics Research (MTSR2024)
  comment: ''
  abstract_only: true
published_at: '2024-09-13'
filter:
  score: 0.78
---
Competency question (CQ) formulation is central to several ontology development and evaluation methodologies. Traditionally, the task of crafting these competency questions heavily relies on the effort of domain experts and knowledge engineers which is often time-consuming and labor-intensive. With the emergence of Large Language Models (LLMs), there arises the possibility to automate and enhance this process. Unlike other similar works which use existing ontologies or knowledge graphs as input to LLMs, we present a retrieval-augmented generation (RAG) approach that uses LLMs for the automatic generation of CQs given a set of scientific papers considered to be a domain knowledge base. We investigate its performance and specifically, we study the impact of different number of papers to the RAG and different temperature setting of the LLM. We conduct experiments using GPT-4 on two domain ontology engineering tasks and compare results against ground-truth CQs constructed by domain experts. Empirical assessments on the results, utilizing evaluation metrics (precision and consistency), reveal that compared to zero-shot prompting, adding relevant domain knowledge to the RAG improves the performance of LLMs on generating CQs for concrete ontology engineering tasks.
