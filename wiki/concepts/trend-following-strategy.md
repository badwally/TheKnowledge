---
schema_version: 1
type: concept
slug: trend-following-strategy
canonical_name: Trend-following strategy
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Trend-following strategy

## Summary

A dynamic investment strategy that estimates the trend of an asset price (typically with an exponentially weighted moving average) and takes long or short exposure proportional to the estimated Sharpe ratio; the main component of momentum-style management and the dominant strategy class for commodity trading advisors (CTAs) and managed futures, with returns characterized by a convex option-like payoff, positive skewness, hit ratio below 50%, and an average gain larger than the average loss [[sources/pdf-5a6062a63a4b]].

## Key claims

- Trend-following strategies have non-linear, option-like trading characteristics; Fung and Hsieh (2001) showed that a trend-following strategy is similar to a lookback straddle option, exhibits a convex payoff, and has positive skewness, and noticed a relationship between trend-following and a long-volatility strategy [[sources/pdf-5a6062a63a4b]].
- Potters and Bouchaud (2006) derived the analytical shape of the corresponding probability distribution function and showed that the P&L of trend-following has an asymmetric right-skewed distribution; the average gain is larger than the average loss, confirming the convex option profile of the momentum risk premium [[sources/pdf-5a6062a63a4b]].
- Bruder and Gaussel (2011) decomposed the P&L of a dynamic strategy into an option profile (the intrinsic value of the option) and a trading impact (equivalent to its time value), confirming that for trend-following the option profile is convex, the skewness is positive, the hit ratio is lower than 50%, and the average gain is larger than the average loss [[sources/pdf-5a6062a63a4b]].
- Bruder and Gaussel (2011) highlighted the important role of the Sharpe ratio and the moving-average duration in understanding P&L; a necessary condition to obtain a positive return is that the absolute value of the Sharpe ratio is greater than the inverse of the moving-average duration [[sources/pdf-5a6062a63a4b]].
- Bruder and Gaussel (2011) showed that the trading impact has a negative vega, that the loss of the trend-following strategy is bounded, and that the loss is proportional to the square of the volatility [[sources/pdf-5a6062a63a4b]].
- Dao et al. (2016) established that the performance of the trend is positive when long-term volatility is larger than short-term volatility, so trend followers must risk-manage short-term volatility to exhibit positive skewness and convexity [[sources/pdf-5a6062a63a4b]].
- The Amundi 2017 paper extends Bruder-Gaussel to the multivariate case to analyze the impact of asset correlations on performance, noting that diversification in a long/short approach is more complex than for a long-only portfolio [[sources/pdf-5a6062a63a4b]].
- A significant part of CTA and trend-following allocations is now motivated by risk management rather than performance — Dao et al. (2016) argue that trend-following is a much cheaper way to hedge long-only exposures than buying options, even if options provide a better hedge [[sources/pdf-5a6062a63a4b]].
- Investment-industry analysis of these strategies is generally dominated by the "syndrome of backtesting"; the Amundi paper argues that academic and theoretical literature is essential for institutional investors to understand the dynamics of these strategies beyond overall performance [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/momentum-risk-premium]]
- [[concepts/bruder-gaussel-framework]]
- [[concepts/lookback-straddle-trend-payoff]]
- [[concepts/trend-following-hit-ratio]]
- [[concepts/option-profile-vs-trading-impact]]
- [[concepts/volatility-term-structure-trend]]
- [[concepts/trend-following-hedging-properties]]
- [[concepts/multivariate-trend-following]]
- [[concepts/trend-following-trading-rule]]
