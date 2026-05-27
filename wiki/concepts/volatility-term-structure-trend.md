---
schema_version: 1
type: concept
slug: volatility-term-structure-trend
canonical_name: Volatility term structure and trend-following performance
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Volatility term structure and trend-following performance

## Summary

The relationship — established by Dao et al. (2016) — between the performance of a trend-following strategy and the term structure of realized volatility: the trend's performance is positive when long-term volatility is larger than short-term volatility, so trend followers must risk-manage short-term volatility to retain positive skewness and convexity [[sources/pdf-5a6062a63a4b]].

## Key claims

- Dao et al. (2016) showed that "the performance of the trend is positive when the long-term volatility is larger than the short-term volatility" [[sources/pdf-5a6062a63a4b]].
- A direct implication of the result is that trend followers have to risk-manage the short-term volatility in order to exhibit a positive skewness and a positive convexity [[sources/pdf-5a6062a63a4b]].
- Using the same framework, Dao et al. (2016) replicated the cumulative performance of the SGA CTA Index, the benchmark used by professionals for analyzing CTA hedge funds [[sources/pdf-5a6062a63a4b]].
- Dao et al. (2016) further demonstrated that the payoff of the trend-following strategy is similar to the payoff of an equally-weighted portfolio of ATM strangles, providing an explicit option-portfolio analog to the trend strategy [[sources/pdf-5a6062a63a4b]].
- The Amundi 2017 paper builds on Dao et al. (2016) when studying the optimal estimation of the trend frequency and decomposing the P&L of trend-following into low- and high-frequency components [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/trend-following-strategy]]
- [[concepts/momentum-risk-premium]]
- [[concepts/trend-following-hedging-properties]]
- [[concepts/lookback-straddle-trend-payoff]]
- [[entities/tung-lam-dao]]
