---
type: concept
slug: widely-applicable-information-criterion
canonical_name: Widely Applicable Information Criterion (WAIC)
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 1
---

# Widely Applicable Information Criterion (WAIC)

## Summary

The Widely Applicable Information Criterion (WAIC), also known as the Watanabe–Akaike Information Criterion, is a Bayesian model-evaluation criterion that estimates expected log pointwise predictive density by integrating over the full posterior, and is asymptotically equivalent to leave-one-out cross-validation.

## Key claims

- WAIC's target is the expectation over future data of minus twice the log pointwise predictive density (LPPD) [[sources/yt-WJ1BvfOm-94]].
- WAIC is more principled than DIC because it integrates over the full posterior rather than plugging in the posterior mean, at the cost of using pointwise predictive densities [[sources/yt-WJ1BvfOm-94]].
- WAIC uses the in-sample log pointwise predictive density and compensates by adding a penalty of 2·pW, where pW is the effective number of parameters approximated by the sum of posterior variances of the log pointwise predictive densities [[sources/yt-WJ1BvfOm-94]].
- The posterior variances are evaluated as the sample variance of the log pointwise predictive density across MCMC draws [[sources/yt-WJ1BvfOm-94]].
- WAIC is asymptotically equivalent to leave-one-out cross-validation because both target minus twice the expected log pointwise predictive density [[sources/yt-WJ1BvfOm-94]].
- For hierarchical Bayesian models, two versions of WAIC arise depending on which predictive distribution is used: the posterior predictive distribution (conditioning on the cluster-level latent variables learned from data) or the mixed predictive distribution (integrating those latent variables over their prior) [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/predictive-information-criteria]]
- [[concepts/deviance-information-criterion]]
- [[concepts/leave-one-out-cross-validation]]
- [[concepts/posterior-predictive-distribution]]
- [[concepts/mixed-predictive-distribution]]
- [[concepts/hierarchical-bayesian-modelling]]
