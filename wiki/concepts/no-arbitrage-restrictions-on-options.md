---
type: concept
slug: no-arbitrage-restrictions-on-options
canonical_name: No-Arbitrage Restrictions on Options
domains:
  - trading-and-markets
---

# No-Arbitrage Restrictions on Options

## Summary

Set of inequalities that the cross-section of European option prices and their implied volatilities must satisfy to preclude arbitrage; per Allan Malz (2014), processing-induced violations of these restrictions are a key failure mode of RND-estimation pipelines, and avoiding them — rather than handling them after the fact — is the main design goal of his technique [[sources/pdf-a25e1c0d5f08]].

## Key claims

- Per Malz (2014), processing of option data can induce violations of no-arbitrage restrictions on the volatility smile that lead to negative probabilities and other implausible results, and the paper's stated aim is a technique that is robust to and avoids such violations [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the discretized risk-neutral density estimate π̃_t(X) ≈ (1/Δ²) e^(rτ) [c(t,X+Δ,τ) + c(t,X−Δ,τ) − 2 c(t,X,τ)] converges to the true RND as Δ → 0, but "the propensity for negative probabilities increases" as Δ shrinks [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the differencing step size Δ is therefore treated as a user setting, chosen so that the resulting density function is non-negative — one of two key features of the technique that simplify computation without generating anomalies [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the second key feature is the use of a clamped cubic spline (zero-slope boundary) to interpolate and, more importantly, extrapolate the volatility smile, since natural cubic splines extrapolate linearly with non-zero slope and that behavior "may induce violations of the no-arbitrage bounds on the volatility smile" [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the underlying design principle is preservative: "if the input implied volatility data don't violate no-arbitrage restrictions, why should the interpolating function?" — i.e., processing should not introduce new violations not present in the input data [[sources/pdf-a25e1c0d5f08]].

## Sources

- [[sources/pdf-a25e1c0d5f08]]

## Related

- [[concepts/risk-neutral-distribution]]
- [[concepts/option-implied-volatility-smile]]
- [[concepts/clamped-cubic-spline-interpolation]]
- [[concepts/breeden-litzenberger-theorem]]
- [[entities/allan-malz]]
