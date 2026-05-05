---
type: concept
slug: flow-induced-price-impact
canonical_name: Flow-induced price impact
domains:
  - trading-and-markets
---

# Flow-induced price impact

## Summary

Flow-induced price impact is the non-fundamental component of underlying-security returns generated when a fund mechanically reinvests inflows (or sells to meet redemptions) in its existing positions; estimated at high frequency by van der Beck, Bouchaud, and Villamaina (2024) using the ETF arbitrage mechanism as a laboratory [[sources/pdf-806192f007eb]].

## Key claims

- ETFs are ideally suited as a laboratory for measuring flow-induced price impact because their portfolio holdings and flows are observable at a daily frequency, and because the vast majority of ETFs perfectly reinvest flows in their existing positions on the same day [[sources/pdf-806192f007eb]].
- A positive correlation between ETF flows and ETF returns can come either from price discovery (flows correlated with fundamental news) or from price impact in the underlying securities; the paper distinguishes the two using a difference-in-difference estimator that conditions the price impact of fund flows on fund illiquidity [[sources/pdf-806192f007eb]].
- Intuition for the difference-in-difference: if the correlation between returns and flows is stronger when fund illiquidity is high, this suggests price impact rather than fundamental information [[sources/pdf-806192f007eb]].
- Around 50% of the initial daily price impact from flow-induced trades reverts in the subsequent 5–10 days, in line with Bucci et al. (2018) on impact relaxation in single stocks [[sources/pdf-806192f007eb]].
- A square-root specification of price impact, with demand shocks scaled by daily volatility, strongly dominates the linear specification at a daily frequency [[sources/pdf-806192f007eb]].
- Building on Lou (2012), the paper takes flow-induced price pressure as the channel through which active funds mechanically affect the cross-section of underlying-security returns [[sources/pdf-806192f007eb]].

## Sources

- [[sources/pdf-806192f007eb]]

## Related

- [[concepts/self-inflated-returns]]
- [[concepts/fund-illiquidity]]
- [[concepts/etf-arbitrage-mechanism]]
