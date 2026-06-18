---
schema_version: 1
id: arxiv-2412.15235
type: arxiv
title: 'OG-RAG: Ontology-Grounded Retrieval-Augmented Generation For Large Language
  Models'
url: https://arxiv.org/abs/2412.15235
authors:
- Kartik Sharma
- Peeyush Kumar
- Yunqing Li
ingested_at: '2026-06-17T21:00:07Z'
content_hash: sha256:98eed293556ec109bed564e52955a552e9e218576ab5df142de7169a15a6b29b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2412.15235'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2024-12-12'
filter:
  score: 0.75
---
This paper presents OG-RAG, an Ontology-Grounded Retrieval Augmented Generation method designed to enhance LLM-generated responses by anchoring retrieval processes in domain-specific ontologies. While LLMs are widely used for tasks like question answering and search, they struggle to adapt to specialized knowledge, such as industrial workflows or knowledge work, without expensive fine-tuning or sub-optimal retrieval methods. Existing retrieval-augmented models, such as RAG, offer improvements but fail to account for structured domain knowledge, leading to suboptimal context generation. Ontologies, which conceptually organize domain knowledge by defining entities and their interrelationships, offer a structured representation to address this gap. OG-RAG constructs a hypergraph representation of domain documents, where each hyperedge encapsulates clusters of factual knowledge grounded using domain-specific ontology. An optimization algorithm then retrieves the minimal set of hyperedges that constructs a precise, conceptually grounded context for the LLM. This method enables efficient retrieval while preserving the complex relationships between entities. OG-RAG applies to domains where fact-based reasoning is essential, particularly in tasks that require workflows or decision-making steps to follow predefined rules and procedures. These include industrial workflows in healthcare, legal, and agricultural sectors, as well as knowledge-driven tasks such as news journalism, investigative research, consulting and more. Our evaluations demonstrate that OG-RAG increases the recall of accurate facts by 55% and improves response correctness by 40% across four different LLMs. Additionally, OG-RAG enables 30% faster attribution of responses to context and boosts fact-based reasoning accuracy by 27% compared to baseline methods.
