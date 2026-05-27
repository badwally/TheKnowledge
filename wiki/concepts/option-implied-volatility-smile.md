---
schema_version: 1
type: concept
slug: option-implied-volatility-smile
canonical_name: Option-Implied Volatility Smile
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Option-Implied Volatility Smile

## Summary

Cross-section of Black-Scholes implied volatilities for European options of a given tenor across a range of exercise prices; per Allan Malz (2014), it is the canonical input data for option-based risk-neutral distribution estimation and can be thought of as a slice through the maturity axis of a time-t Black-Scholes volatility surface σ(t,X,τ) [[sources/pdf-a25e1c0d5f08]].

## Key claims

- Per Malz (2014), the data needed for option-based RND extraction are Black-Scholes volatilities for European options of a given tenor τ across a range of exercise prices, focusing on a single tenor rather than the entire surface [[sources/pdf-a25e1c0d5f08]].
- Per Malz, although Black-Scholes volatilities are expressed in a metric drawn from a particular option-pricing model, they are associated with market- rather than model-based prices — the volatility surface translates into the time-t market price schedule of European calls via c(t,X,τ) = v[S_t, X, τ, σ(t,X,τ), r_t, q_t], where v is the standard Black-Scholes call formula [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the call valuation function takes an observed or estimated market-adjusted Black-Scholes volatility and returns an estimated market call price; c(t,X,τ) and σ(t,X,τ) can be viewed as simply two different metrics for expressing the market values of options [[sources/pdf-a25e1c0d5f08]].
- Per Malz, implied volatilities can be expressed in various other units such as Black or normalized volatilities, and exercise prices can be expressed as ratio or spread to the current spot or forward price or as the option delta — but under all conventions, implied volatilities can be transformed into option prices in currency units for given exercise prices [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the technique has been developed for three input data structures: exchange-traded products use Black-Scholes volatilities (pct. p.a.) versus ratio to spot; currencies and gold use Black-Scholes volatilities (pct. p.a.) versus spot delta; swaptions use Black volatilities (pct. p.a.) versus bps from forward [[sources/pdf-a25e1c0d5f08]].
- Per Malz, one of the main challenges in fitting RNDs is the diversity of option data and the difficulty of working with it — the Malz (2014) technique does not solve that problem but instead seeks an easier way to process the option data into an estimated RND while minimizing added assumptions [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the data used in the paper are obtained from Bloomberg Financial LP, which aggregates and processes quotes, end-of-day prices, and indicative prices from a range of dealers and exchanges, and the data are subjected to a set of quality diagnostics; while flaws do occasionally appear in the data, the overall quality is good [[sources/pdf-a25e1c0d5f08]].

## Sources

- [[sources/pdf-a25e1c0d5f08]]

## Related

- [[concepts/risk-neutral-distribution]]
- [[concepts/breeden-litzenberger-theorem]]
- [[concepts/clamped-cubic-spline-interpolation]]
- [[concepts/no-arbitrage-restrictions-on-options]]
- [[entities/allan-malz]]
