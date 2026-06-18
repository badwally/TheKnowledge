---
schema_version: 1
id: arxiv-2509.00710
type: arxiv
title: 'On Verifiable Legal Reasoning: A Multi-Agent Framework with Formalized Knowledge
  Representations'
url: https://arxiv.org/abs/2509.00710
authors:
- Albert Sadowski
- Jarosław A. Chudziak
ingested_at: '2026-06-17T18:08:15Z'
content_hash: sha256:d09c67ef28df39137488660c0f6904c8654ac9d82a5060faf747c121135fa5ee
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2509.00710'
  categories:
  - cs.AI
  - cs.CL
  doi: 10.1145/3746252.3761057
  primary_category: cs.AI
  journal_ref: 'CIKM ''25: Proceedings of the 34th ACM International Conference on
    Information and Knowledge Management (2025) 2535-2545'
  comment: Accepted for publication at the 34th ACM International Conference on Information
    and Knowledge Management (CIKM '25)
  abstract_only: true
published_at: '2025-08-31'
filter:
  score: 0.78
---
Legal reasoning requires both precise interpretation of statutory language and consistent application of complex rules, presenting significant challenges for AI systems. This paper introduces a modular multi-agent framework that decomposes legal reasoning into distinct knowledge acquisition and application stages. In the first stage, specialized agents extract legal concepts and formalize rules to create verifiable intermediate representations of statutes. The second stage applies this knowledge to specific cases through three steps: analyzing queries to map case facts onto the ontology schema, performing symbolic inference to derive logically entailed conclusions, and generating final answers using a programmatic implementation that operationalizes the ontological knowledge. This bridging of natural language understanding with symbolic reasoning provides explicit and verifiable inspection points, significantly enhancing transparency compared to end-to-end approaches. Evaluation on statutory tax calculation tasks demonstrates substantial improvements, with foundational models achieving 76.4\% accuracy compared to 18.8\% baseline performance, effectively narrowing the performance gap between reasoning and foundational models. These findings suggest that modular architectures with formalized knowledge representations can make sophisticated legal reasoning more accessible through computationally efficient models while enhancing consistency and explainability in AI legal reasoning, establishing a foundation for future research into more transparent, trustworthy, and effective AI systems for legal domain.
