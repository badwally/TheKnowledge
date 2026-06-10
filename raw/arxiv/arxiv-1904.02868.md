---
schema_version: 1
id: arxiv-1904.02868
type: arxiv
title: 'Data Shapley: Equitable Valuation of Data for Machine Learning'
url: https://arxiv.org/abs/1904.02868
authors:
- Amirata Ghorbani
- James Zou
ingested_at: '2026-06-10T21:57:46Z'
content_hash: sha256:35e1ca3ab81f15cd2172a7b6fdb44ab112eea133e29977d1844dfde9a661ad43
domains:
- data-collectives
nlm_corpus_ids: []
wiki_pages:
- wiki/concepts/data-shapley.md
- wiki/entities/data-shapley-paper.md
meta:
  arxiv_id: '1904.02868'
  categories:
  - stat.ML
  - cs.AI
  - cs.LG
  doi: ''
  primary_category: stat.ML
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2019-04-05'
filter:
  score: 0.3
  policy_version: data-collectives-v1
  rationale: High-quality peer-reviewed research on individual data-point valuation
    in centralized ML training, but addresses a different problem domain than the
    policy scope. The paper does not discuss governance structures, incentive design,
    or regulatory frameworks for inter-organizational data pooling (inclusion criteria
    1, 3, 4, 6); instead, it proposes a technical methodology for valuing individual
    training data to a single learner. Shapley-based valuation could theoretically
    inform data-collective compensation mechanisms, but the paper contains no reference
    to consortia, cooperatives, trusts, or multi-party pooling arrangements—making
    it tangentially related to data economics but out of scope for this domain.
  decided_at: '2026-06-10T21:58:15Z'
  user_correction:
    decided_at: '2026-06-10T22:01:17Z'
    score: 1.0
    rationale: 'Ghorbani & Zou, ''Data Shapley: Equitable Valuation of Data for ML''
      (ICML 2019) — the canonical method for valuing and attributing each contributor''s
      marginal data value; directly serves criterion 1 (how member contributions are
      valued and access/payoff allocated).'
---
As data becomes the fuel driving technological and economic growth, a fundamental challenge is how to quantify the value of data in algorithmic predictions and decisions. For example, in healthcare and consumer markets, it has been suggested that individuals should be compensated for the data that they generate, but it is not clear what is an equitable valuation for individual data. In this work, we develop a principled framework to address data valuation in the context of supervised machine learning. Given a learning algorithm trained on $n$ data points to produce a predictor, we propose data Shapley as a metric to quantify the value of each training datum to the predictor performance. Data Shapley value uniquely satisfies several natural properties of equitable data valuation. We develop Monte Carlo and gradient-based methods to efficiently estimate data Shapley values in practical settings where complex learning algorithms, including neural networks, are trained on large datasets. In addition to being equitable, extensive experiments across biomedical, image and synthetic data demonstrate that data Shapley has several other benefits: 1) it is more powerful than the popular leave-one-out or leverage score in providing insight on what data is more valuable for a given learning task; 2) low Shapley value data effectively capture outliers and corruptions; 3) high Shapley value data inform what type of new data to acquire to improve the predictor.
