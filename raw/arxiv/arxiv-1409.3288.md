---
schema_version: 1
id: arxiv-1409.3288
type: arxiv
title: Reconciliation of RDF* and Property Graphs
url: https://arxiv.org/abs/1409.3288
authors:
- Olaf Hartig
ingested_at: '2026-06-17T18:07:59Z'
content_hash: sha256:523f39ecebd9bff5ba448f2e0b6e4dd81ad6e8acf64f785e33235c403d716ae4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1409.3288'
  categories:
  - cs.DB
  doi: ''
  primary_category: cs.DB
  journal_ref: ''
  comment: slightly changed the definition of PGs and added the notion of property
    uniqueness
  abstract_only: true
published_at: '2014-09-11'
filter:
  score: 0.85
---
Both the notion of Property Graphs (PG) and the Resource Description Framework (RDF) are commonly used models for representing graph-shaped data. While there exist some system-specific solutions to convert data from one model to the other, these solutions are not entirely compatible with one another and none of them appears to be based on a formal foundation. In fact, for the PG model, there does not even exist a commonly agreed-upon formal definition.
  The aim of this document is to reconcile both models formally. To this end, the document proposes a formalization of the PG model and introduces well-defined transformations between PGs and RDF. As a result, the document provides a basis for the following two innovations: On one hand, by implementing the RDF-to-PG transformations defined in this document, PG-based systems can enable their users to load RDF data and make it accessible in a compatible, system-independent manner using, e.g., the graph traversal language Gremlin or the declarative graph query language Cypher. On the other hand, the PG-to-RDF transformation in this document enables RDF data management systems to support compatible, system-independent queries over the content of Property Graphs by using the standard RDF query language SPARQL. Additionally, this document represents a foundation for systematic research on relationships between the two models and between their query languages.
