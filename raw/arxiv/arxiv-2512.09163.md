---
id: arxiv-2512.09163
type: arxiv
title: 'WTNN: Weibull-Tailored Neural Networks for survival analysis'
url: https://arxiv.org/abs/2512.09163
authors:
- Gabrielle Rives
- Olivier Lopez
- Nicolas Bousquet
ingested_at: '2026-05-20T17:36:37Z'
content_hash: sha256:03dab3dfdc8b3ee0721a2338b68500ec19935923174402d96a58ccdc2596144c
domains:
- risksystems
nlm_corpus_ids:
- dee0eae4-b11f-4df2-a418-d10fffd42c7e
wiki_pages:
- wiki/entities/wtnn-paper.md
- wiki/concepts/weibull-tailored-neural-networks.md
- wiki/entities/gabrielle-rives.md
- wiki/entities/olivier-lopez.md
- wiki/entities/nicolas-bousquet.md
- wiki/concepts/engineering-fleet-management.md
meta:
  arxiv_id: '2512.09163'
  categories:
  - stat.ML
  - cs.LG
  - stat.AP
  - stat.ME
  doi: ''
  primary_category: stat.ML
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2025-12-09'
---
The Weibull distribution is a commonly adopted choice for modeling the survival of systems subject to maintenance over time. When only proxy indicators and censored observations are available, it becomes necessary to express the distribution's parameters as functions of time-dependent covariates. Deep neural networks provide the flexibility needed to learn complex relationships between these covariates and operational lifetime, thereby extending the capabilities of traditional regression-based models. Motivated by the analysis of a fleet of military vehicles operating in highly variable and demanding environments, as well as by the limitations observed in existing methodologies, this paper introduces WTNN, a new neural network-based modeling framework specifically designed for Weibull survival studies. The proposed architecture is specifically designed to incorporate qualitative prior knowledge regarding the most influential covariates, in a manner consistent with the shape and structure of the Weibull distribution. Through numerical experiments, we show that this approach can be reliably trained on proxy and right-censored data, and is capable of producing robust and interpretable survival predictions that can improve existing approaches.
