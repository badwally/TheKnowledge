---
type: concept
slug: mixed-predictive-distribution
canonical_name: Mixed predictive distribution
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 2
---

# Mixed predictive distribution

## Summary

The mixed predictive distribution for a hierarchical Bayesian model uses the marginal likelihood — integrating cluster-level latent variables over their prior — to predict new observations. It corresponds to predictions for a new unit in a new cluster, rather than a new unit in an existing cluster.

## Key claims

- The mixed predictive distribution uses the marginal likelihood instead of the conditional likelihood; expanding the marginal likelihood as an integral shows that the cluster-level latent variables ζ are drawn from the prior rather than learned from the data for cluster j [[sources/yt-WJ1BvfOm-94]].
- Effectively, the mixed predictive distribution is a prediction for a new unit in a new cluster [[sources/yt-WJ1BvfOm-94]].
- The mixed predictive distribution was introduced by Gelman and others in 1996 [[sources/yt-WJ1BvfOm-94]].
- For posterior predictive checking using the mixed predictive distribution, one would not use posterior samples of ζ for the existing clusters but rather generate fresh ζ values from their prior before generating new y [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/posterior-predictive-distribution]]
- [[concepts/marginal-vs-conditional-likelihood]]
- [[concepts/widely-applicable-information-criterion]]
