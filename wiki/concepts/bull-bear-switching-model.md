---
type: concept
slug: bull-bear-switching-model
canonical_name: Bull-bear switching model
domains:
  - trading-and-markets
---

# Bull-bear switching model

## Summary

The bull-bear switching model is a geometric Brownian motion with regime-switching drift driven by a hidden two-state Markov chain; Dai, Yang, Zhang, and Zhu (2015) use it as the market primitive on which they prove the optimality of a trend-following trading rule under partial information [[sources/pdf-05df32dcb03e]].

## Key claims

- The stock price S_r satisfies dS_r = S_r[μ(α_r)dr + σdB_r], where α_r ∈ {1,2} is a two-state Markov chain, μ(i) ≡ μ_i is the expected return rate in regime i, σ > 0 is the constant volatility, and B_r is a standard Brownian motion [[sources/pdf-05df32dcb03e]].
- α_r = 1 indicates a bull market (uptrend) and α_r = 2 indicates a bear market (downtrend); the generator of α_r is Q with off-diagonal switching intensities λ_1 (bull→bear) and λ_2 (bear→bull), both positive [[sources/pdf-05df32dcb03e]].
- The Markov chain is assumed to be not directly observable, so trading decisions must be based purely on observed stock prices — a partial-information setup [[sources/pdf-05df32dcb03e]].
- {α_r} and {B_r} are independent, and the stock is assumed to pay no dividends; if dividends existed they could be re-invested in the stock and absorbed into S_r [[sources/pdf-05df32dcb03e]].
- To exclude trivial cases the paper assumes μ_2 − σ²/2 < ρ < μ_1 − σ²/2, where ρ is the risk-free rate; otherwise the investor would always sell or never buy [[sources/pdf-05df32dcb03e]].
- The setup follows Dai et al. [5] in modeling the trend with regime-switching geometric Brownian motion and partial information; this paper (2015) extends the earlier work by allowing self-financing trading rather than restricting trades to a single share at a time [[sources/pdf-05df32dcb03e]].

## Sources

- [[sources/pdf-05df32dcb03e]]

## Related

- [[concepts/trend-following-trading-rule]]
- [[concepts/wonham-filter]]
- [[concepts/optimal-trading-thresholds]]
