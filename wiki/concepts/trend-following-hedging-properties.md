---
type: concept
slug: trend-following-hedging-properties
canonical_name: Hedging properties of trend-following
domains:
  - trading-and-markets
---

# Hedging properties of trend-following

## Summary

The ability of a trend-following overlay to provide downside protection on a long-only exposure without paying a hedging premium; Dao et al. (2016) showed the trend-following payoff resembles an equally-weighted portfolio of ATM strangles, and the Amundi 2017 paper formalizes the cross-hedging case (one asset hedged by another) and the value-at-risk of mixed long-only / trend-following portfolios [[sources/pdf-5a6062a63a4b]].

## Key claims

- A significant part of investments in CTAs and trend-following programs is motivated by a risk-management approach, not only by performance considerations; some investors use CTAs as a hedging program without paying a hedging premium [[sources/pdf-5a6062a63a4b]].
- Dao et al. (2016) demonstrated that the payoff of the trend-following strategy is similar to the payoff of an equally-weighted portfolio of ATM strangles, and compared the two approaches for hedging a long-only exposure [[sources/pdf-5a6062a63a4b]].
- A strangle portfolio pays a fixed price for short-term volatility, whereas the trend-following strategy is directly exposed to short-term volatility; the premium paid on options markets is high, so Dao et al. (2016) concluded that "even if options provide a better hedge, trend-following is a much cheaper way to hedge long-only exposures" [[sources/pdf-5a6062a63a4b]].
- The Amundi 2017 paper extends the analysis by mixing long-only and trend-following exposures to measure the hedging quality of the momentum strategy and to evaluate it as a tool for tail-risk management and downside protection [[sources/pdf-5a6062a63a4b]].
- The paper analyzes the single-asset case, calculating the analytical probability distribution and the value-at-risk of the hedged portfolio [[sources/pdf-5a6062a63a4b]].
- The multivariate case is also considered, particularly the cross-hedging strategy in which one asset is hedged by another, and the behavior of the trend-following strategy in the presence of skewness events is illustrated [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/trend-following-strategy]]
- [[concepts/lookback-straddle-trend-payoff]]
- [[concepts/volatility-term-structure-trend]]
- [[concepts/momentum-risk-premium]]
- [[concepts/multivariate-trend-following]]
- [[entities/tung-lam-dao]]
