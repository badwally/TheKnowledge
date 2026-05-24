---
type: concept
slug: marginal-vs-conditional-likelihood
canonical_name: Marginal vs conditional likelihood
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 2
---

# Marginal vs conditional likelihood

## Summary

In hierarchical Bayesian models for clustered data, the likelihood can be expressed either conditionally on cluster-level latent variables (the conditional likelihood) or marginally over their prior distribution (the marginal likelihood). The choice has direct consequences for the form of information criteria such as DIC and WAIC.

## Key claims

- The conditional likelihood is the likelihood conditional on the cluster-level latent variables ζ_j; for clustered data it factorises into a product of cluster contributions, and within each cluster into a product of unit contributions because units within a cluster are conditionally independent given the latent variable [[sources/yt-WJ1BvfOm-94]].
- The conditional likelihood is the natural definition in Stan and similar Bayesian software, where the model block expresses the likelihood of y conditional on ζ [[sources/yt-WJ1BvfOm-94]].
- The marginal likelihood integrates out the latent variables using their prior; it is the likelihood used in maximum likelihood estimation of hierarchical models such as those fit with R's lme4 package [[sources/yt-WJ1BvfOm-94]].
- In the marginal-likelihood view, only ω and ψ are parameters; the latent variables ζ_j are treated as missing data rather than parameters [[sources/yt-WJ1BvfOm-94]].
- For a random-intercept multilevel model, the marginal distribution of a cluster's responses is multivariate normal with mean α, marginal variance ψ + σ², and within-cluster covariance ψ, yielding an intraclass correlation of ψ / (ψ + σ²) [[sources/yt-WJ1BvfOm-94]].
- Because two likelihoods exist, two versions of DIC are well-defined: conditional DIC uses the conditional likelihood and is produced by default in most Bayesian software, while marginal DIC uses the marginal likelihood and requires additional computation; the latter has been implemented by Edgar Merkle in the R package blavaan [[sources/yt-WJ1BvfOm-94]].
- When the marginal likelihood is not analytically tractable (e.g., for binary responses), it can be evaluated with adaptive quadrature; an efficient variant has been developed that exploits available MCMC draws [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/deviance-information-criterion]]
- [[concepts/widely-applicable-information-criterion]]
- [[concepts/posterior-predictive-distribution]]
- [[concepts/mixed-predictive-distribution]]
- [[entities/edgar-merkle]]
