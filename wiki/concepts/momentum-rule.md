---
type: concept
slug: momentum-rule
canonical_name: Momentum trading rule
domains:
  - trading-and-markets
---

# Momentum trading rule

## Summary

A market-timing rule that generates a Buy/Sell signal from the sign of the change in price over a fixed lookback window; in Zakamulin's anatomy it is the elementary rule from which more elaborate moving-average rules can be constructed, since every trading rule examined can be presented as a weighted average of the momentum rules computed using different averaging periods [[sources/pdf-ec9fdef2193c]].

## Key claims

- The momentum rule is one of the four main moving-average market-timing rules considered in Zakamulin (2016), alongside the price-minus-moving-average rule, the change-of-direction rule, and the double-crossover method [[sources/pdf-ec9fdef2193c]].
- Every market-timing rule prescribes investing in the stocks (the market) when a Buy signal is generated and moving to cash or shorting the market when a Sell signal is generated [[sources/pdf-ec9fdef2193c]].
- The trading-strategy return in the absence of transaction costs is r_t = δ_{t|t-1} · r_{Mt} + (1 − δ_{t|t-1}) · r_{ft}, where δ_{t|t-1} ∈ {0,1} is the trading signal generated at the end of month t-1 (0 = Sell, 1 = Buy) [[sources/pdf-ec9fdef2193c]].
- In each rule, signal generation is a two-step process: first compute a technical trading indicator from the last closing price and k lagged prices, then derive the Buy/Sell signal from the indicator [[sources/pdf-ec9fdef2193c]].
- In Zakamulin's anatomy, the momentum rule is treated as the elementary trading rule on the basis of which one can construct more elaborate rules, because every trading rule can be presented as a weighted average of momentum rules computed using different averaging periods [[sources/pdf-ec9fdef2193c]].

## Sources

- [[sources/pdf-ec9fdef2193c]]

## Related

- [[concepts/anatomy-of-moving-average-rules]]
- [[concepts/weighted-moving-average-of-price-changes]]
- [[concepts/price-minus-moving-average-rule]]
- [[concepts/moving-average-change-of-direction-rule]]
- [[concepts/double-crossover-method]]
- [[entities/valeriy-zakamulin]]
