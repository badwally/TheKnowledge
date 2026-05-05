---
type: concept
slug: constant-risk-trend-signal
canonical_name: Constant-risk trend signal (Lempérière et al. 2014)
domains:
  - trading-and-markets
---

# Constant-risk trend signal (Lempérière et al. 2014)

## Summary

The trend indicator used by Lempérière, Deremble, Seager, Potters, and Bouchaud (2014) to test the trend-following anomaly: at the start of each month t, the signal is the deviation of the previous price from an exponential moving average of past prices (with decay rate n months), normalized by an exponential moving average of absolute monthly price changes — defined this way so that the resulting strategy simulates a constant-risk position rather than a constant-notional one [[sources/pdf-be69dd282a8c]].

## Key claims

- The signal s_n(t) = (p(t-1) − ⟨p_n,t-1⟩) / σ_n(t-1), where ⟨p_n⟩ is an exponential moving average of past prices excluding p(t) with decay rate n months and σ_n is an exponential moving average of absolute monthly price changes with the same decay [[sources/pdf-be69dd282a8c]].
- The corresponding fictitious strategy buys or sells a quantity ±σ_n^{-1} of the underlying contract, scaling exposure inversely with realized volatility — a constant-risk trading strategy [[sources/pdf-be69dd282a8c]].
- The paper focuses on n = 5 months, but the Sharpe ratio and t-stat are only weakly dependent on n, with t-stats above 4 across n ∈ {2, 3, 5, 7, 10, 15} and dropping toward 3.3 only at n = 20 [[sources/pdf-be69dd282a8c]].
- The Sharpe ratio is defined as average return divided by volatility (both annualized); since the futures P&L does not include interest on capital and futures are self-financed instruments, the risk-free rate is not subtracted [[sources/pdf-be69dd282a8c]].
- The t-stat of the P&L is given by the Sharpe ratio times √N, where N is the number of years over which the strategy is active [[sources/pdf-be69dd282a8c]].
- The paper notes the general conclusions are extremely robust against changes of the statistical test or of the implemented strategy [[sources/pdf-be69dd282a8c]].

## Sources

- [[sources/pdf-be69dd282a8c]]

## Related

- [[concepts/trend-following-strategy]]
- [[concepts/two-centuries-trend-anomaly]]
- [[concepts/trend-saturation-effect]]
