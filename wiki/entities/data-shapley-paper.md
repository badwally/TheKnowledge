---
schema_version: 1
type: entity
slug: data-shapley-paper
canonical_name: 'Data Shapley: Equitable Valuation of Data for Machine Learning (Ghorbani
  & Zou, 2019)'
entity_kind: paper
domains:
- data-collectives
created_at: '2026-06-10T21:57:46Z'
last_updated: '2026-06-10T21:57:46Z'
draft: true
draft_started_at: '2026-06-10T21:57:46Z'
draft_unresolved_claims: 4
---

# Data Shapley: Equitable Valuation of Data for Machine Learning (Ghorbani & Zou, 2019)

## Summary

"Data Shapley: Equitable Valuation of Data for Machine Learning" is a 2019 paper by Amirata Ghorbani and James Zou that develops a principled framework for valuing individual training data in supervised machine learning, proposing the Data Shapley value as the metric that uniquely satisfies several natural axioms of equitable data valuation [[sources/arxiv-1904.02868]]. The paper is the canonical introduction of Data Shapley and is widely treated as the reference method for marginal-contribution attribution in pooled-data settings [[sources/arxiv-1904.02868]].

## Key facts

- Authors: Amirata Ghorbani and James Zou [[sources/arxiv-1904.02868]].
- Posted to arXiv on 5 April 2019 as arXiv:1904.02868 under the primary category stat.ML (cross-listed cs.AI and cs.LG) [[sources/arxiv-1904.02868]].
- The paper proposes Data Shapley as a metric that quantifies, for a learning algorithm trained on n data points to produce a predictor, the value of each training datum to that predictor's performance [[sources/arxiv-1904.02868]].
- The paper's motivating framing is that in healthcare and consumer markets it has been suggested that individuals should be compensated for the data they generate, but no equitable valuation method existed [[sources/arxiv-1904.02868]].
- The paper develops Monte Carlo and gradient-based estimators for Data Shapley that work in practical settings where complex learning algorithms, including neural networks, are trained on large datasets [[sources/arxiv-1904.02868]].
- The paper's experiments span biomedical, image, and synthetic datasets and report three benefits: (1) Data Shapley is more powerful than leave-one-out or leverage score; (2) low-Shapley-value data captures outliers and corruptions; (3) high-Shapley-value data informs what new data to acquire to improve the predictor [[sources/arxiv-1904.02868]].

## Sources

- [[sources/arxiv-1904.02868]] — the paper itself; arXiv:1904.02868, ingested 2026-06-10.

## Related

- [[concepts/data-shapley]] — the metric and method this paper introduces.
- [[entities/strategic-data-sharing-competitors]] — a downstream paper on competitor data pooling for which marginal-contribution attribution mechanisms (such as Data Shapley) are directly relevant.
- [[concepts/competitor-data-sharing-tradeoff]] — the firm-level pooling dilemma where contributor valuation governs incentive design.
- [[concepts/data-cooperative]] — the organizational form where equitable member-contribution accounting is a load-bearing function.
