---
schema_version: 1
type: concept
slug: market-intraday-momentum
canonical_name: Market intraday momentum
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Market intraday momentum

## Summary

Market intraday momentum is time-series momentum at the market level within a single trading day — specifically, the empirical regularity that the return during the last 30 minutes before market close is positively and significantly predicted by the return during the rest of the day [[sources/pdf-2742492120a8]].

## Key claims

- Baltussen, Da, Lammers, and Martens (2020) define the trading day as the 24-hour period from close on day t-1 to close on day t and partition it into overnight (ON), first half-hour (FH), middle (M), second-to-last half-hour (SLH), and last half-hour (LH); the rest-of-day (ROD = ON + FH + M + SLH) return is the focal predictor and the LH return the focal predicted variable [[sources/pdf-2742492120a8]].
- ROD positively and significantly predicts LH across all major asset classes and markets — 17 developed equity-index futures, 16 bond futures, 21 commodity futures, and 8 currency futures — using December 1974 to May 2020 data [[sources/pdf-2742492120a8]].
- A simple trading strategy that exploits this signal produces consistent returns over time, with annualized Sharpe ratios between 0.87 and 1.73 at the asset-class level [[sources/pdf-2742492120a8]].
- The effect is distinct from the cross-sectional intraday return seasonality of Heston et al. (2010) and is robust over time across the 1974-2020 sample period [[sources/pdf-2742492120a8]].
- ROD predicts LH better than the first-half-hour return alone (the predictor used in Gao et al. 2018 for ten US ETFs): ROD has higher out-of-sample R-squared, and when ROD and ONFH disagree in sign, ROD does the better job predicting LH [[sources/pdf-2742492120a8]].
- Last-half-hour returns mean-revert over the next three days for equities, bonds, and commodities — a transitory-price-pressure signature consistent with hedging rather than informed trading [[sources/pdf-2742492120a8]].

## Sources

- [[sources/pdf-2742492120a8]]

## Related

- [[concepts/short-gamma-hedging]]
- [[concepts/negative-gamma-exposure]]
- [[concepts/leveraged-etf-rebalancing-demand]]
- [[concepts/u-shape-intraday-volume]]
- [[concepts/transitory-price-pressure]]
- [[concepts/gamma-reflexivity]]
- [[entities/guido-baltussen]]
- [[entities/zhi-da]]
- [[entities/sten-lammers]]
- [[entities/martin-martens]]
