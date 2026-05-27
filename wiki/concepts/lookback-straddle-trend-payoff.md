---
schema_version: 1
type: concept
slug: lookback-straddle-trend-payoff
canonical_name: Lookback-straddle payoff of trend-following
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Lookback-straddle payoff of trend-following

## Summary

The characterization of a trend-following strategy's terminal payoff as similar to a lookback straddle option, introduced by Fung and Hsieh (2001); the result implies a convex P&L, positive skewness, and a connection to a long-volatility strategy, and marks the empirical break in the trend-following literature from backtest-driven analysis to option-theoretic decomposition [[sources/pdf-5a6062a63a4b]].

## Key claims

- Fung and Hsieh (2001) developed a general methodology to show that "trend followers have nonlinear, option-like trading strategies" [[sources/pdf-5a6062a63a4b]].
- Specifically, Fung and Hsieh showed that a trend-following strategy is similar to a lookback straddle option and exhibits a convex payoff; from convexity they deduced positive skewness [[sources/pdf-5a6062a63a4b]].
- They noticed a relationship between a trend-following strategy and a long-volatility strategy [[sources/pdf-5a6062a63a4b]].
- By developing a theoretical framework and connecting their results to empirical facts, the paper marks a break with previous academic studies and has strongly influenced later research on the momentum risk premium [[sources/pdf-5a6062a63a4b]].
- The characterization is reproduced and extended by Bruder and Gaussel (2011) — who confirmed convex profile, positive skewness, hit ratio under 50%, average gain larger than average loss — and by Potters and Bouchaud (2006), who derived the analytical probability distribution function of the trend-following P&L [[sources/pdf-5a6062a63a4b]].
- Dao et al. (2016) extend the option analogy by demonstrating that the payoff of the trend-following strategy is similar to the payoff of an equally-weighted portfolio of ATM strangles [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/trend-following-strategy]]
- [[concepts/momentum-risk-premium]]
- [[concepts/bruder-gaussel-framework]]
- [[concepts/option-profile-vs-trading-impact]]
- [[concepts/trend-following-hedging-properties]]
