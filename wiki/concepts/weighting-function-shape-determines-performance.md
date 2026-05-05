---
type: concept
slug: weighting-function-shape-determines-performance
canonical_name: Weighting-function shape determines performance
domains:
  - trading-and-markets
---

# Weighting-function shape determines performance

## Summary

The central practical consequence of Zakamulin's (2016) anatomy of moving-average trading rules: once every rule is rewritten as a weighted moving average of price changes, the performance of any moving-average trading rule depends exclusively on the shape of the weighting function for price changes — collapsing the joint search over rule, moving-average type, and window size into a one-dimensional search over weighting-function shapes [[sources/pdf-ec9fdef2193c]].

## Key claims

- The performance of any moving average trading rule depends exclusively on the shape of the weighting function for price changes [[sources/pdf-ec9fdef2193c]].
- This dramatically simplifies the search procedure compared to the prior literature, where a researcher would have to perform tests of all possible combinations of trading rule × moving-average weighting scheme × window length to find the best performer — "a daunting and next to impossible task" [[sources/pdf-ec9fdef2193c]].
- Under the anatomy, finding the best trading rule reduces to testing various shapes of the weighting function rather than enumerating every combination [[sources/pdf-ec9fdef2193c]].
- Zakamulin operationalizes this collapse by evaluating the out-of-sample performance of 300 various shapes of the weighting function for price changes using historical data on four financial market indices [[sources/pdf-ec9fdef2193c]].
- The 300 shapes are chosen to represent different variations of a few of the most typical shapes of the weighting functions used in market timing with moving averages [[sources/pdf-ec9fdef2193c]].
- The test design is intended to suggest answers to long-standing questions about optimal types of moving averages and whether the best-performing trading rule can beat the passive counterpart in out-of-sample tests [[sources/pdf-ec9fdef2193c]].
- Prior conclusions about the profitability of market-timing rules cannot be generalized to the entire universe of all potential combinations of trading rules with moving-average weighting schemes, because earlier studies tested only an arbitrary and limited set of "most popular combinations" [[sources/pdf-ec9fdef2193c]].
- Zakamulin notes that, to the best knowledge of the author, only two prior papers — Sullivan, Timmermann, and White (1999) and Zakamulin (2014) — implement out-of-sample tests of profitability of trading rules in the stock market [[sources/pdf-ec9fdef2193c]].

## Sources

- [[sources/pdf-ec9fdef2193c]]

## Related

- [[concepts/anatomy-of-moving-average-rules]]
- [[concepts/weighted-moving-average-of-price-changes]]
- [[concepts/moving-average-types]]
- [[concepts/momentum-rule]]
- [[concepts/price-minus-moving-average-rule]]
- [[concepts/moving-average-change-of-direction-rule]]
- [[concepts/double-crossover-method]]
- [[entities/valeriy-zakamulin]]
