---
schema_version: 1
id: arxiv-2512.14277
type: arxiv
title: 'SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions'
url: https://arxiv.org/abs/2512.14277
authors:
- Panayiotis Smeros
- Vincent Emonet
- Ruijie Wang
- Ana-Claudia Sima
- Tarcisio Mendes de Farias
ingested_at: '2026-06-17T20:56:15Z'
content_hash: sha256:0c7c1a471cdfc64b9c1a4a977b3b747745b6ed6be4f17c4b4ffcb16a04dfd713
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2512.14277'
  categories:
  - cs.IR
  - cs.AI
  - cs.CL
  doi: ''
  primary_category: cs.IR
  journal_ref: ''
  comment: 17 pages, 8 figures, 1 table. Under Review
  abstract_only: true
published_at: '2025-12-16'
filter:
  score: 0.85
---
The advent of large language models is contributing to the emergence of novel approaches that promise to better tackle the challenge of generating structured queries, such as SPARQL queries, from natural language. However, these new approaches mostly focus on response accuracy over a single source while ignoring other evaluation criteria, such as federated query capability over distributed data stores, as well as runtime and cost to generate SPARQL queries. Consequently, they are often not production-ready or easy to deploy over (potentially federated) knowledge graphs with good accuracy. To mitigate these issues, in this paper, we extend our previous work and describe and systematically evaluate SPARQL-LLM, an open-source and triplestore-agnostic approach, powered by lightweight metadata, that generates SPARQL queries from natural language text. First, we describe its architecture, which consists of dedicated components for metadata indexing, prompt building, and query generation and execution. Then, we evaluate it based on a state-of-the-art challenge with multilingual questions, and a collection of questions from three of the most prevalent knowledge graphs within the field of bioinformatics. Our results demonstrate a substantial increase of 24% in the F1 Score on the state-of-the-art challenge, adaptability to high-resource languages such as English and Spanish, as well as ability to form complex and federated bioinformatics queries. Furthermore, we show that SPARQL-LLM is up to 36x faster than other systems participating in the challenge, while costing a maximum of $0.01 per question, making it suitable for real-time, low-cost text-to-SPARQL applications. One such application deployed over real-world decentralized knowledge graphs can be found at https://www.expasy.org/chat.
