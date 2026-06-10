---
schema_version: 1
type: concept
slug: competitor-data-sharing-tradeoff
canonical_name: Competitor Data Sharing Trade-Off
domains:
- data-collectives
created_at: '2026-06-10T22:01:17Z'
last_updated: '2026-06-10T22:01:17Z'
draft: true
draft_started_at: '2026-06-10T22:01:17Z'
draft_unresolved_claims: 0
---

# Competitor Data Sharing Trade-Off

## Summary

The competitor data sharing trade-off is the firm-level dilemma at the core of collaborative learning between competitors: pooling training data with rivals can improve one's own machine learning model, but the same shared data also improves rivals' models and may erode the firm's product-market profits [[sources/arxiv-2305.16052]]. Tsoy and Konstantinov (NeurIPS 2023) introduce a general three-component framework to analyze this trade-off, comprising the firms' production decisions, the effect of additional data on model quality, and the data-sharing negotiation process [[sources/arxiv-2305.16052]].

## Key claims

- Collaborative learning techniques have advanced in recent years to enable private model training across multiple organizations, but firms still face a dilemma when considering data sharing with competitors [[sources/arxiv-2305.16052]].
- The dilemma has two opposing effects: collaboration improves a company's ML model, while the same collaboration also benefits competitors and may reduce profits [[sources/arxiv-2305.16052]].
- A general framework for analyzing the trade-off can be decomposed into three components — production decisions, the effect of additional data on model quality, and the data-sharing negotiation process — that can be modeled and varied independently [[sources/arxiv-2305.16052]].
- An instantiation of the framework based on a conventional market model from economic theory identifies key factors that affect collaboration incentives [[sources/arxiv-2305.16052]].
- Market conditions have a profound impact on data-sharing incentives, not merely an incremental one [[sources/arxiv-2305.16052]].

## Sources

- [[sources/arxiv-2305.16052]] — Strategic Data Sharing between Competitors (Tsoy & Konstantinov, NeurIPS 2023)

## Related

- [[entities/strategic-data-sharing-competitors]] — paper formalizing this trade-off
- [[concepts/product-differentiation-collaboration]] — specific market condition that shifts the trade-off toward sharing
- [[concepts/antitrust-risks-data-sharing]] — regulatory risk that conditions any resolution of the trade-off toward sharing
- [[concepts/blockchain-data-sharing]] — infrastructure pattern used when firms resolve the trade-off toward sharing
