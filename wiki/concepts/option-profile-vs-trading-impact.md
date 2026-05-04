---
type: concept
slug: option-profile-vs-trading-impact
canonical_name: Option profile vs trading impact (P&L decomposition)
domains:
  - trading-and-markets
---

# Option profile vs trading impact (P&L decomposition)

## Summary

A decomposition of the P&L of a dynamic strategy, introduced by Bruder and Gaussel (2011), into an option profile (the intrinsic value of an embedded option) and a trading impact (analogous to the time value of that option); for trend-following strategies the option profile is convex with positive skewness, while the trading impact has a negative vega and bounds the strategy's loss [[sources/pdf-5a6062a63a4b]].

## Key claims

- Bruder and Gaussel (2011) decomposed the P&L of a dynamic investment strategy — including stop-loss, contrarian, averaging, and trend-following — into an option profile and a trading impact [[sources/pdf-5a6062a63a4b]].
- The option profile is interpreted as the intrinsic value of the embedded option; the trading impact is equivalent to its time value [[sources/pdf-5a6062a63a4b]].
- For trend-following, the option profile is convex, the skewness is positive, the hit ratio is lower than 50%, and the average gain is larger than the average loss — reproducing within a unified framework the results of Fung and Hsieh (2001) and Potters and Bouchaud (2006) [[sources/pdf-5a6062a63a4b]].
- A necessary condition to obtain a positive return on a trend-following strategy is that the absolute value of the Sharpe ratio is greater than the inverse of the moving-average duration [[sources/pdf-5a6062a63a4b]].
- The trading impact has a negative vega: rising volatility erodes the trading impact component [[sources/pdf-5a6062a63a4b]].
- The loss of the trend-following strategy is bounded, and is proportional to the square of the volatility [[sources/pdf-5a6062a63a4b]].
- The Amundi 2017 paper derives new results concerning the statistical properties of the trading impact and analyzes the impact of leverage on the ruin probability within this decomposition [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/bruder-gaussel-framework]]
- [[concepts/trend-following-strategy]]
- [[concepts/lookback-straddle-trend-payoff]]
- [[concepts/trend-following-hit-ratio]]
- [[concepts/momentum-risk-premium]]
