---
schema_version: 1
type: concept
slug: data-shapley
canonical_name: Data Shapley
domains:
- data-collectives
created_at: '2026-06-10T21:57:46Z'
last_updated: '2026-06-10T21:57:46Z'
draft: true
draft_started_at: '2026-06-10T21:57:46Z'
draft_unresolved_claims: 4
---

# Data Shapley

## Summary

Data Shapley is a principled metric that quantifies the marginal value of each training datum to the performance of a predictor produced by a supervised learning algorithm, derived by applying the cooperative-game-theoretic Shapley value to the data-valuation setting [[sources/arxiv-1904.02868]]. It is proposed as an equitable answer to the question of how much each contributor's data is worth — a question that arises whenever individuals or organizations contribute data to a shared learning task and expect compensation or attribution proportional to contribution [[sources/arxiv-1904.02868]].

## Key claims

- Data Shapley uniquely satisfies several natural axiomatic properties of equitable data valuation, inheriting the uniqueness result of the Shapley value from cooperative game theory [[sources/arxiv-1904.02868]].
- The motivating problem statement is explicitly framed around healthcare and consumer markets where it has been proposed that individuals should be compensated for the data they generate, but no principled answer to "what is an equitable valuation" had existed [[sources/arxiv-1904.02868]].
- Exact computation of Data Shapley scales combinatorially with the number of training points; the paper develops Monte Carlo and gradient-based estimators that make it tractable for complex learners — including neural networks — trained on large datasets [[sources/arxiv-1904.02868]].
- Empirically, Data Shapley is more powerful than the popular leave-one-out and leverage-score baselines for ranking which training points are most valuable to a given learning task [[sources/arxiv-1904.02868]].
- Low-Shapley-value training points effectively capture outliers and label corruptions, giving Data Shapley a secondary use as a data-quality diagnostic [[sources/arxiv-1904.02868]].
- High-Shapley-value training points inform what type of new data to acquire to improve the predictor, giving Data Shapley a third use as an active-acquisition signal [[sources/arxiv-1904.02868]].
- The empirical evaluation spans biomedical, image, and synthetic datasets, demonstrating that the value rankings transfer across modalities [[sources/arxiv-1904.02868]].

## Sources

- [[sources/arxiv-1904.02868]] — Ghorbani & Zou, "Data Shapley: Equitable Valuation of Data for Machine Learning" (ICML 2019), the paper that introduces the metric and the estimation methods.

## Related

- [[entities/data-shapley-paper]] — the canonical paper introducing this concept.
- [[concepts/competitor-data-sharing-tradeoff]] — Data Shapley is one candidate mechanism for valuing each firm's marginal contribution in pooled-training collaborations.
- [[concepts/data-cooperative]] — member-contribution valuation and payoff allocation is a load-bearing operation in cooperatives.
- [[concepts/citizen-directed-data]] — individual compensation for personal data, the motivating use case in the paper's healthcare/consumer-market framing.
