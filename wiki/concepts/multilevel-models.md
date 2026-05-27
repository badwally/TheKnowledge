---
schema_version: 1
type: concept
slug: multilevel-models
canonical_name: Multilevel models
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 3
created_at: '2026-05-20T19:49:54Z'
last_updated: '2026-05-20T19:49:54Z'
---

# Multilevel models

## Summary

Multilevel (mixed) models are hierarchical statistical models for clustered data in which lower-level units (e.g. students) are nested within higher-level clusters (e.g. schools), with cluster-specific intercepts or coefficients drawn from a population distribution.

## Key claims

- Multilevel models are one of the canonical examples of hierarchical Bayesian models for clustered data, alongside structural equation models and item response theory [[sources/yt-WJ1BvfOm-94]].
- A three-stage multilevel model has, at the observation stage, a normal observation model y_ij = α + ζ_j + ε_ij with cluster-specific intercept ζ_j; ζ_j is itself given a normal prior with variance ψ; and ψ is given a hyperprior [[sources/yt-WJ1BvfOm-94]].
- The varying parameter ζ_j (a varying intercept in this example) can be extended to vector-valued varying coefficients in the more general multivariate case [[sources/yt-WJ1BvfOm-94]].
- In non-Bayesian usage ζ_j is often called a 'random effect'; the speaker observes that treating it as a random variable rather than a parameter is what allows non-Bayesians to accommodate the additional latent term [[sources/yt-WJ1BvfOm-94]].
- For random-intercept multilevel models the marginal likelihood has a closed form: the responses for a single cluster are multivariate normal with mean α, marginal variance ψ + σ², and within-cluster covariance ψ; the within-cluster correlation is the intraclass correlation ψ / (ψ + σ²) [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/marginal-vs-conditional-likelihood]]
- [[concepts/item-response-theory]]
