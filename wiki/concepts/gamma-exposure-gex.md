---
schema_version: 1
type: concept
slug: gamma-exposure-gex
canonical_name: Gamma exposure (GEX)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Gamma exposure (GEX)

## Summary

Gamma exposure (GEX) is a dollar-denominated measure of SPX option dealers' aggregate delta sensitivity to a one-point change in the underlying index price; positive GEX means customers have net sold options, causing dealers to provide stabilizing liquidity, while negative GEX means customers are net long options, causing dealers to take liquidity and destabilize the market [[sources/pdf-sqzme-2020-the-implied-order]].

## Key claims

- GEX for a single option contract is computed by taking the Black-Scholes delta at the current underlying price, then recomputing it at a price one point lower (or higher), converting the delta change to dollar terms — for example, a 2900-strike put with SPX at 3000, 30 DTE, 20% IV has a delta of 27, meaning the dealer must be long $81,000 of the index to be flat delta [[sources/pdf-sqzme-2020-the-implied-order]].
- When the index falls one point to 2999, the same option requires the dealer to buy approximately $393 of additional SPX exposure; this $393 is the GEX of that single put contract [[sources/pdf-sqzme-2020-the-implied-order]].
- Due to the nature of gamma, selling an option causes the dealer to provide liquidity both on the way up and the way down — the dealer buys when the index falls and sells when it rises, stabilizing the market [[sources/pdf-sqzme-2020-the-implied-order]].
- Total GEX for the SPX option universe is computed by performing the single-contract GEX calculation for every contract in dealer directional open interest (DDOI) and summing the results [[sources/pdf-sqzme-2020-the-implied-order]].
- GEX can be positive or negative: positive means customers sold enough options to cause stabilizing dealer hedging; negative means customers are net long more options, causing dealers to be "short gamma" and to always take liquidity, which is destabilizing [[sources/pdf-sqzme-2020-the-implied-order]].
- A thorough analysis of SPX GEX back to 2004 reveals that GEX is very rarely negative, and even when negative it has never been below -$200 million per SPX point [[sources/pdf-sqzme-2020-the-implied-order]].
- In the vast majority of cases, GEX shows dealers providing substantial liquidity — sometimes over $1 billion per point, equivalent to approximately 6,666 E-mini S&P 500 futures per point at SPX 3000 [[sources/pdf-sqzme-2020-the-implied-order]].
- A scatterplot of GEX against 1-day close-to-close S&P 500 returns shows a clear pattern: higher GEX means tighter returns, confirming the stabilizing-liquidity thesis [[sources/pdf-sqzme-2020-the-implied-order]].
- Extreme volatility has only ever occurred when GEX was near zero, but near-zero GEX also coexists with many non-volatile return observations — zero GEX "allows" other liquidity-taking factors to dominate but does not itself cause volatility [[sources/pdf-sqzme-2020-the-implied-order]].
- There are two reasons GEX can be near zero: dealers have a very small or balanced option inventory (benign), or implied volatilities are high enough to push gammas toward zero (the dangerous case that motivates introducing VEX) [[sources/pdf-sqzme-2020-the-implied-order]].
- When implied volatilities go up, gammas and thus GEX move toward zero — since high IV is associated with high realized volatility, this points to a causal mechanism linking IV to actual liquidity withdrawal [[sources/pdf-sqzme-2020-the-implied-order]].

## Sources

- [[sources/pdf-sqzme-2020-the-implied-order]]

## Related

- [[entities/squeezemetrics]]
- [[concepts/implied-order-book]]
- [[concepts/vanna-exposure-vex]]
- [[concepts/dealer-directional-open-interest]]
- [[concepts/negative-gamma-exposure]]
- [[concepts/short-gamma-hedging]]
- [[concepts/dealer-short-gamma-mechanics]]
- [[concepts/gamma-reflexivity]]
