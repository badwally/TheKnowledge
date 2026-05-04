---
type: concept
slug: bruder-gaussel-framework
canonical_name: Bruder-Gaussel framework
domains:
  - trading-and-markets
---

# Bruder-Gaussel framework

## Summary

A continuous-time analytical framework for dynamic investment strategies introduced by Bruder and Gaussel (2011) that decomposes the P&L of a strategy into an option profile (the intrinsic value of an embedded option) and a trading impact (analogous to the time value); the framework is the analytical engine that the Amundi 2017 paper extends to the multivariate case to characterize the momentum risk premium [[sources/pdf-5a6062a63a4b]].

## Key claims

- The framework models the asset price S as a geometric Brownian motion with constant volatility but time-varying trend µ_t; the trend is unobservable and estimated via filtering, with µ̂_t = E[µ_t | F_t] [[sources/pdf-5a6062a63a4b]].
- The framework is general — applicable to dynamic strategies including stop-loss, contrarian, averaging, and trend-following — not specifically a trend-following model [[sources/pdf-5a6062a63a4b]].
- The P&L of any dynamic strategy is decomposed into an option profile and a trading impact; the option profile is the intrinsic value of the option, and the trading impact is equivalent to its time value [[sources/pdf-5a6062a63a4b]].
- Applied to a continuous-time trend-following strategy, the framework reproduces the option-like results of Fung and Hsieh (2001) and Potters and Bouchaud (2006): the option profile is convex, skewness is positive, the hit ratio is lower than 50%, and the average gain is larger than the average loss [[sources/pdf-5a6062a63a4b]].
- Two parameters are foregrounded: the Sharpe ratio and the moving-average duration; a necessary condition for positive expected return is that the absolute value of the Sharpe ratio is greater than the inverse of the moving-average duration [[sources/pdf-5a6062a63a4b]].
- The trading impact has a negative vega; the loss of the trend-following strategy is bounded and is proportional to the square of the volatility [[sources/pdf-5a6062a63a4b]].
- The Amundi 2017 paper extends the framework to the multivariate case, deriving statistical properties for trend-following applied to a multi-asset universe and analyzing the impact of asset correlations on performance — yielding three governing parameters: the vector of Sharpe ratios, the covariance matrix of asset returns, and the frequency matrix of the moving-average estimator [[sources/pdf-5a6062a63a4b]].
- Bruder and Gaussel (2011) is one of four research works the Amundi paper identifies as essential for understanding trend-following dynamics, alongside Fung and Hsieh (2001), Potters and Bouchaud (2006), and Dao et al. (2016) [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/trend-following-strategy]]
- [[concepts/momentum-risk-premium]]
- [[concepts/option-profile-vs-trading-impact]]
- [[concepts/lookback-straddle-trend-payoff]]
- [[concepts/trend-following-hit-ratio]]
- [[concepts/multivariate-trend-following]]
