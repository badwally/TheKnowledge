---
schema_version: 1
type: concept
slug: weighted-moving-average-of-price-changes
canonical_name: Weighted moving average of price changes
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Weighted moving average of price changes

## Summary

The canonical reinterpretation, established by Zakamulin (2016), of every moving-average market-timing indicator as the computation of a weighted moving average of price changes — making the weighting function over price changes the single object that determines the indicator's value and, therefore, the trading rule's performance [[sources/pdf-ec9fdef2193c]].

## Key claims

- The computation of every technical trading indicator covered in the paper — across momentum, price-minus-moving-average, change-of-direction, and double-crossover rules — can equivalently be interpreted as the computation of a weighted moving average of price changes [[sources/pdf-ec9fdef2193c]].
- A weighted moving average of prices at month-end t with k lagged prices is defined formally as MA_t(k) = Σ_{j=0}^{k} w_{t-j} P_{t-j} / Σ_{j=0}^{k} w_{t-j}, where w_{t-j} is the weight of price P_{t-j} in the computation of the weighted moving average [[sources/pdf-ec9fdef2193c]].
- To compute a moving average one must use at least one lagged price, so k ≥ 1; when k = 0 the moving average degenerates to the last closing price (MA_t(0) = P_t) [[sources/pdf-ec9fdef2193c]].
- Once each rule is rewritten in this representation, the only real difference between diverse market-timing rules coupled with various moving-average types lies in the shape of the weighting function used to compute the moving average of price changes [[sources/pdf-ec9fdef2193c]].
- This reframing reduces the search problem from "which rule × which moving-average type × which window size" to "which weighting-function shape" [[sources/pdf-ec9fdef2193c]].

## Sources

- [[sources/pdf-ec9fdef2193c]]

## Related

- [[concepts/anatomy-of-moving-average-rules]]
- [[concepts/weighting-function-shape-determines-performance]]
- [[concepts/moving-average-types]]
- [[concepts/momentum-rule]]
- [[concepts/price-minus-moving-average-rule]]
- [[concepts/moving-average-change-of-direction-rule]]
- [[concepts/double-crossover-method]]
- [[entities/valeriy-zakamulin]]
