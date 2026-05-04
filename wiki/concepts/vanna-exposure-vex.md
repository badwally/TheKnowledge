---
type: concept
slug: vanna-exposure-vex
canonical_name: Vanna exposure (VEX)
domains:
  - trading-and-markets
---

# Vanna exposure (VEX)

## Summary

Vanna exposure (VEX) is a dollar-denominated measure of SPX option dealers' aggregate delta sensitivity to changes in implied volatility; it complements gamma exposure (GEX) by capturing the liquidity impact of volatility changes — when IV rises, out-of-the-money option deltas increase (forcing dealers long those options to add hedge positions) while in-the-money option deltas decrease (forcing dealers to reduce hedge positions), making VEX a more dynamic and directionally complex measure than GEX [[sources/pdf-sqzme-2020-the-implied-order]].

## Key claims

- VEX is motivated by the puzzle that GEX near zero sometimes precedes extreme volatility and sometimes does not — the missing variable is implied volatility, which when high pushes gammas toward zero and simultaneously triggers vanna-driven hedging flows [[sources/pdf-sqzme-2020-the-implied-order]].
- In the same way that GEX measures a provable, logical, and clearly causal relationship between dealer gamma exposure and SPX liquidity, there is also a causal relationship between vanna exposure and SPX liquidity [[sources/pdf-sqzme-2020-the-implied-order]].
- VEX is computed using the same Black-Scholes delta function as GEX, but varying the implied volatility input (V) instead of the underlying price input (S) [[sources/pdf-sqzme-2020-the-implied-order]].
- For an out-of-the-money put (K=2900, SPX at 3000, 30 DTE, IV=20%), a rise in IV from 20% to 25% increases delta from 27 to 30, requiring the dealer to buy an additional $9,000 of SPX exposure — demonstrating that VEX has a smaller per-unit dollar impact than GEX [[sources/pdf-sqzme-2020-the-implied-order]].
- VEX is more dynamic than GEX because the direction of the hedging flow depends on whether the option is out-of-the-money or in-the-money: for an OTM option held long by the dealer, rising IV increases delta and forces buying; for an ITM option, the effect reverses [[sources/pdf-sqzme-2020-the-implied-order]].
- Option delta has three sensitivities — gamma (sensitivity to underlying price), vanna (sensitivity to implied volatility), and charm (sensitivity to time) — but charm constitutes too small an effect to have practical utility, leaving GEX and VEX as the two operationally relevant exposures [[sources/pdf-sqzme-2020-the-implied-order]].

## Sources

- [[sources/pdf-sqzme-2020-the-implied-order]]

## Related

- [[entities/squeezemetrics]]
- [[concepts/implied-order-book]]
- [[concepts/gamma-exposure-gex]]
- [[concepts/dealer-directional-open-interest]]
- [[concepts/negative-gamma-exposure]]
