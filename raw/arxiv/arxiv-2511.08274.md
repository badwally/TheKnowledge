---
schema_version: 1
id: arxiv-2511.08274
type: arxiv
title: 'Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs'
url: https://arxiv.org/abs/2511.08274
authors:
- Anton Gusarov
- Anastasia Volkova
- Valentin Khrulkov
- Andrey Kuznetsov
- Evgenii Maslov
- Ivan Oseledets
ingested_at: '2026-06-17T20:58:14Z'
content_hash: sha256:5bb5ad94317086478997b58a038ebe3ba5ccc6cc399f980cac3d5bf2fe242363
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2511.08274'
  categories:
  - cs.AI
  - cs.CL
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: Code to be released
  abstract_only: true
published_at: '2025-11-11'
filter:
  score: 0.75
---
While Retrieval-Augmented Generation (RAG) methods commonly draw information from unstructured documents, the emerging paradigm of GraphRAG aims to leverage structured data such as knowledge graphs. Most existing GraphRAG efforts focus on Resource Description Framework (RDF) knowledge graphs, relying on triple representations and SPARQL queries. However, the potential of Cypher and Labeled Property Graph (LPG) databases to serve as scalable and effective reasoning engines within GraphRAG pipelines remains underexplored in current research literature. To fill this gap, we propose Multi-Agent GraphRAG, a modular LLM agentic system for text-to-Cypher query generation serving as a natural language interface to LPG-based graph data. Our proof-of-concept system features an LLM-based workflow for automated Cypher queries generation and execution, using Memgraph as the graph database backend. Iterative content-aware correction and normalization, reinforced by an aggregated feedback loop, ensures both semantic and syntactic refinement of generated queries. We evaluate our system on the CypherBench graph dataset covering several general domains with diverse types of queries. In addition, we demonstrate performance of the proposed workflow on a property graph derived from the IFC (Industry Foundation Classes) data, representing a digital twin of a building. This highlights how such an approach can bridge AI with real-world applications at scale, enabling industrial digital automation use cases.
