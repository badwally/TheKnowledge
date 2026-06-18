---
schema_version: 1
id: arxiv-2312.15626
type: arxiv
title: 'RDF-star2Vec: RDF-star Graph Embeddings for Data Mining'
url: https://arxiv.org/abs/2312.15626
authors:
- Shusaku Egami
- Takanori Ugai
- Masateru Oota
- Kyoumoto Matsushita
- Takahiro Kawamura
- Kouji Kozaki
- Ken Fukuda
ingested_at: '2026-06-17T18:08:08Z'
content_hash: sha256:f25318333cc743ec36b25d4778b8836f9e2c2fc67310c879747da03e6cccc5a4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2312.15626'
  categories:
  - cs.AI
  - cs.CL
  - cs.IR
  - cs.LG
  doi: 10.1109/ACCESS.2023.3341029
  primary_category: cs.AI
  journal_ref: IEEE Access, Volume 11, pp.142030-142042, 2023
  comment: 13 pages, 6 figures, and this paper has been accepted by IEEE Access
  abstract_only: true
published_at: '2023-12-25'
filter:
  score: 0.7
---
Knowledge Graphs (KGs) such as Resource Description Framework (RDF) data represent relationships between various entities through the structure of triples (<subject, predicate, object>). Knowledge graph embedding (KGE) is crucial in machine learning applications, specifically in node classification and link prediction tasks. KGE remains a vital research topic within the semantic web community. RDF-star introduces the concept of a quoted triple (QT), a specific form of triple employed either as the subject or object within another triple. Moreover, RDF-star permits a QT to act as compositional entities within another QT, thereby enabling the representation of recursive, hyper-relational KGs with nested structures. However, existing KGE models fail to adequately learn the semantics of QTs and entities, primarily because they do not account for RDF-star graphs containing multi-leveled nested QTs and QT-QT relationships. This study introduces RDF-star2Vec, a novel KGE model specifically designed for RDF-star graphs. RDF-star2Vec introduces graph walk techniques that enable probabilistic transitions between a QT and its compositional entities. Feature vectors for QTs, entities, and relations are derived from generated sequences through the structured skip-gram model. Additionally, we provide a dataset and a benchmarking framework for data mining tasks focused on complex RDF-star graphs. Evaluative experiments demonstrated that RDF-star2Vec yielded superior performance compared to recent extensions of RDF2Vec in various tasks including classification, clustering, entity relatedness, and QT similarity.
