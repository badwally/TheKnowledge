---
schema_version: 1
id: arxiv-2604.20795
type: arxiv
title: Automatic Ontology Construction Using LLMs as an External Layer of Memory,
  Verification, and Planning for Hybrid Intelligent Systems
url: https://arxiv.org/abs/2604.20795
authors:
- Pavel Salovskii
- Iuliia Gorshkova
ingested_at: '2026-06-17T20:59:55Z'
content_hash: sha256:7d9cabba963005a2365e95c765f6e9445e6f12f3b60033c7679409ad004812d6
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2604.20795'
  categories:
  - cs.AI
  doi: 10.5281/zenodo.19696042
  primary_category: cs.AI
  journal_ref: ''
  comment: Artificial Intelligence; Knowledge Representation and Reasoning; Information
    Retrieval; Machine Learning
  abstract_only: true
published_at: '2026-04-22'
filter:
  score: 0.75
---
This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning.
  The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction.
  Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline.
  The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.
