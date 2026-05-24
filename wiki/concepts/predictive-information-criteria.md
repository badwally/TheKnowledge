---
type: concept
slug: predictive-information-criteria
canonical_name: Predictive information criteria
domains:
- risksystems
draft: true
draft_started_at: '2026-05-20T17:36:45Z'
draft_unresolved_claims: 2
---

# Predictive information criteria

## Summary

Predictive information criteria are model-evaluation measures that estimate a fitted model's expected out-of-sample prediction error. The principal Bayesian variants are the Deviance Information Criterion (DIC), the Widely Applicable (Watanabe–Akaike) Information Criterion (WAIC), and leave-one-out cross-validation (LOO).

## Key claims

- The goal of predictive information criteria is to assess how well a model predicts future or out-of-sample data not used for fitting [[sources/yt-WJ1BvfOm-94]].
- A standard summary of prediction error is the deviance, defined as minus twice the log of the likelihood evaluated at the out-of-sample data [[sources/yt-WJ1BvfOm-94]].
- DIC handles the unknown parameter vector θ by plugging the posterior mean of θ into the deviance for new data, yielding a plug-in deviance [[sources/yt-WJ1BvfOm-94]].
- WAIC is more principled than DIC because it integrates over the full posterior rather than plugging in the posterior mean, at the cost of using pointwise predictive densities [[sources/yt-WJ1BvfOm-94]].
- The shared target of DIC and WAIC is the expectation of these prediction errors over the distribution of future data, which is generally unknown [[sources/yt-WJ1BvfOm-94]].
- Because the future data-generating distribution is typically unknown and validation data are usually unavailable, the in-sample plug-in deviance (or in-sample log pointwise predictive density) is used and corrected by adding a penalty term that compensates for using the data twice [[sources/yt-WJ1BvfOm-94]].
- DIC's penalty is the effective number of parameters pD, defined as the posterior expectation of the deviance minus the deviance evaluated at the posterior expectation of the parameters [[sources/yt-WJ1BvfOm-94]].
- WAIC's penalty is twice pW, where pW is the effective number of parameters approximated by the sum of posterior variances of the log pointwise predictive densities [[sources/yt-WJ1BvfOm-94]].
- WAIC is asymptotically equivalent to leave-one-out cross-validation because both target minus twice the expected log pointwise predictive density [[sources/yt-WJ1BvfOm-94]].

## Sources

- [[sources/yt-WJ1BvfOm-94]]

## Related

- [[concepts/deviance-information-criterion]]
- [[concepts/widely-applicable-information-criterion]]
- [[concepts/leave-one-out-cross-validation]]
- [[concepts/hierarchical-bayesian-modelling]]
- [[concepts/pareto-smoothed-importance-sampling]]
