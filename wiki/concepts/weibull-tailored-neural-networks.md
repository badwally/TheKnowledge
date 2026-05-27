---
schema_version: 1
type: concept
slug: weibull-tailored-neural-networks
canonical_name: Weibull-Tailored Neural Networks (WTNN)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:37Z'
draft_unresolved_claims: 1
created_at: '2026-05-20T19:11:34Z'
last_updated: '2026-05-20T19:11:34Z'
---

# Weibull-Tailored Neural Networks (WTNN)

## Summary

Weibull-Tailored Neural Networks (WTNN) is a neural-network-based survival-analysis framework that expresses Weibull distribution parameters as functions of time-dependent covariates, with the network architecture constrained to reflect qualitative prior knowledge about the most influential covariates and to remain consistent with the shape and structure of the Weibull distribution.

## Key claims

- The Weibull distribution is commonly adopted for modeling the survival of systems subject to maintenance over time, and WTNN is positioned as an extension of this distributional choice to settings where parameters must be expressed as functions of time-dependent covariates [[sources/arxiv-2512.09163]].
- When only proxy indicators and censored observations are available, the WTNN framework uses deep neural networks to provide the flexibility needed to learn complex relationships between covariates and operational lifetime, thereby extending the capabilities of traditional regression-based survival models [[sources/arxiv-2512.09163]].
- The WTNN architecture is specifically designed to incorporate qualitative prior knowledge regarding the most influential covariates, in a manner consistent with the shape and structure of the Weibull distribution [[sources/arxiv-2512.09163]].
- Numerical experiments reported in the introducing paper show that WTNN can be reliably trained on proxy and right-censored data and produces robust and interpretable survival predictions that the authors argue can improve on existing approaches [[sources/arxiv-2512.09163]].

## Sources

- [[sources/arxiv-2512.09163]]

## Related

- [[entities/wtnn-paper]]
- [[concepts/engineering-fleet-management]]
- [[concepts/expert-elicitation]]
