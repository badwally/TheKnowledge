---
schema_version: 1
id: arxiv-1912.06229
type: arxiv
title: Optimal Two-Sided Market Mechanism Design for Large-Scale Data Sharing and
  Trading in Massive IoT Networks
url: https://arxiv.org/abs/1912.06229
authors:
- Tao Zhang
- Quanyan Zhu
ingested_at: '2026-06-11T05:05:16Z'
content_hash: sha256:e46dcbdb43b84d1be718351f530e0f60dc6320b0c85b39da9c8441a487388a99
domains:
- data-collectives
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1912.06229'
  categories:
  - cs.DB
  - cs.SI
  - eess.SY
  doi: ''
  primary_category: cs.DB
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2019-12-12'
filter:
  score: 0.4
  policy_version: data-collectives-v1
  rationale: 'This mechanism-design paper addresses incentive structures for two-sided
    data trading in IoT networks, which touches on criterion 1 (incentive design).
    However, it appears to describe a data-broker matching platform rather than a
    data collective or cooperative: the ''service'' is the marketplace mechanism itself,
    not a shared model/output produced from pooled data. The policy explicitly excludes
    ''pure data-resale or data-broker marketplaces where no shared model is produced
    from pooled data.'' The abstract-only status, absence of named organizations,
    and lack of discussion of governance structures (cooperatives vs. trusts), regulatory
    frameworks, or real-world consortia further limit relevance. Marginal; requires
    full-text review to determine if the paper addresses collective pooling dynamics.'
  decided_at: '2026-06-11T05:05:43Z'
  user_correction: null
---
The development of the Internet of Things (IoT) generates a significant amount of data that contains valuable knowledge for system operations and business opportunities. Since the data is the property of the IoT data owners, the access to the data requires permission from the data owners, which gives rise to a potential market opportunity for the IoT data sharing and trading to create economic values and market opportunities for both data owners and buyers. In this work, we leverage optimal mechanism design theory to develop a monopolist matching platform for data trading over massive IoT networks. The proposed mechanism is composed of a pair of matching and payment rules for each side of the market. We analyze the incentive compatibility of the market and characterize the optimal mechanism with a class of cut-off matching rules for both welfare-maximization and revenue-maximization mechanisms and study three matching behaviors including complete-matched, bottom-eliminated, and top-reserved.
