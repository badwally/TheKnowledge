---
schema_version: 1
type: concept
slug: negative-gamma-exposure
canonical_name: Negative gamma exposure (NGE)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Negative gamma exposure (NGE)

## Summary

Negative gamma exposure (NGE) is a direct proxy for option market makers' aggregate net-short gamma position in an underlying index; Baltussen, Da, Lammers, and Martens (2020) use it as an identification variable to test whether market intraday momentum strengthens when dealers' aggregate hedging pressure is more severe [[sources/pdf-2742492120a8]]. SqueezeMetrics' foundational framework shows that aggregate SPX gamma exposure (GEX) is very rarely negative, and when it is negative, it has never been below -$200 million per SPX point — but the rare occurrence of negative GEX is precisely what allows other liquidity-taking factors to dominate and produce extreme volatility [[sources/pdf-sqzme-2020-the-implied-order]].

## Key claims

- Option market makers need to trade in the same direction as the underlying movement of the S&P 500 index if they have negative gamma exposure; the more negative their gamma exposure, the more aggressively they must trade [[sources/pdf-2742492120a8]].
- Using a direct proxy of S&P 500 option market makers' negative gamma exposure, Baltussen et al. confirm that market intraday momentum is present for the index when NGE is negative and becomes stronger when NGE becomes more negative [[sources/pdf-2742492120a8]].
- This NGE-conditional pattern is the paper's first piece of novel empirical evidence linking the hedging-demand channel to the documented rest-of-day to last-half-hour predictability [[sources/pdf-2742492120a8]].
- The authors thank SqueezeMetrics for providing the data underlying these tests [[sources/pdf-2742492120a8]].
- A thorough analysis of SPX GEX back to 2004 reveals that GEX is very rarely negative — in the vast majority of cases, SPX option dealers are providing substantial stabilizing liquidity to the index, sometimes over $1 billion per point [[sources/pdf-sqzme-2020-the-implied-order]].
- Even when GEX is negative, it has never been below -$200 million per SPX point [[sources/pdf-sqzme-2020-the-implied-order]].
- Extreme volatility has only ever occurred when GEX was near zero, but near-zero GEX also coexists with typical non-volatile returns — zero GEX "allows" other liquidity-taking factors to dominate rather than directly causing volatility [[sources/pdf-sqzme-2020-the-implied-order]].
- A scatterplot of GEX against 1-day close-to-close S&P 500 returns shows a clear pattern: higher GEX means tighter returns, empirically confirming the stabilizing-liquidity thesis [[sources/pdf-sqzme-2020-the-implied-order]].

## Sources

- [[sources/pdf-2742492120a8]]
- [[sources/pdf-sqzme-2020-the-implied-order]]

## Related

- [[concepts/short-gamma-hedging]]
- [[concepts/market-intraday-momentum]]
- [[concepts/gamma-reflexivity]]
- [[concepts/gamma-exposure-gex]]
- [[concepts/implied-order-book]]
- [[entities/squeezemetrics]]
