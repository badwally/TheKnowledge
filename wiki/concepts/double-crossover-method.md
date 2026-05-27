---
schema_version: 1
type: concept
slug: double-crossover-method
canonical_name: Double-crossover method
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Double-crossover method

## Summary

A market-timing rule that generates Buy/Sell signals from the crossing of two moving averages of different lookback lengths over the price series; in Zakamulin's anatomy it is one of the four canonical moving-average rules whose trading indicator reduces to a weighted moving average of price changes [[sources/pdf-ec9fdef2193c]].

## Key claims

- The double-crossover method is one of the four main moving-average market-timing rules considered in Zakamulin (2016), alongside the momentum rule, the price-minus-moving-average rule, and the change-of-direction rule [[sources/pdf-ec9fdef2193c]].
- Like every other moving-average rule in the anatomy framework, its trading indicator can equivalently be interpreted as a weighted moving average of price changes [[sources/pdf-ec9fdef2193c]].
- It can be presented as a weighted average of momentum rules computed using different averaging periods, since every trading rule in the anatomy admits this representation [[sources/pdf-ec9fdef2193c]].

## Sources

- [[sources/pdf-ec9fdef2193c]]

## Related

- [[concepts/anatomy-of-moving-average-rules]]
- [[concepts/weighted-moving-average-of-price-changes]]
- [[concepts/momentum-rule]]
- [[concepts/price-minus-moving-average-rule]]
- [[concepts/moving-average-change-of-direction-rule]]
- [[entities/valeriy-zakamulin]]
