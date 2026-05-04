---
type: concept
slug: moving-average-types
canonical_name: Moving-average weighting types (SMA, LMA, EMA, REMA)
domains:
  - trading-and-markets
---

# Moving-average weighting types (SMA, LMA, EMA, REMA)

## Summary

A taxonomy of the moving-average weighting schemes used in technical-trading market-timing rules, comprising the Simple Moving Average (SMA), the Linearly weighted Moving Average (LMA), the Exponentially weighted Moving Average (EMA), and the Reverse Exponential Moving Average (REMA), as catalogued in Zakamulin (2016) — each defined by how it weights the last closing price and the k lagged prices in the rolling lookback window [[sources/pdf-ec9fdef2193c]].

## Key claims

- The Simple Moving Average (SMA) at month-end t with k lagged prices weights every observation equally: SMA_t(k) = (1/(k+1)) Σ_{j=0}^{k} P_{t-j} [[sources/pdf-ec9fdef2193c]].
- The Linearly weighted Moving Average (LMA) weights each observation by an arithmetically decreasing integer: in LMA(k) the latest observation has weight k+1, the second latest k, and so on down to one [[sources/pdf-ec9fdef2193c]].
- A disadvantage of the LMA is that the weighting scheme is too rigid relative to schemes whose decay rate can be tuned [[sources/pdf-ec9fdef2193c]].
- The Exponentially weighted Moving Average (EMA) uses a decay factor 0 < λ ≤ 1 so that EMA_t(k) = Σ_{j=0}^{k} λ^j P_{t-j} / Σ_{j=0}^{k} λ^j; varying λ adjusts how much weight is placed on the most recent price [[sources/pdf-ec9fdef2193c]].
- The EMA satisfies two limit properties: lim_{λ→1} EMA_t(k) = SMA_t(k) and lim_{λ→0} EMA_t(k) = P_t [[sources/pdf-ec9fdef2193c]].
- The Reverse Exponential Moving Average (REMA) inverts the weighting, assigning greater weight to the oldest prices and less to the most recent: REMA_t(k) = Σ_{j=0}^{k} λ^{k-j} P_{t-j} / Σ_{j=0}^{k} λ^{k-j} [[sources/pdf-ec9fdef2193c]].
- The REMA satisfies the limit properties lim_{λ→1} REMA_t(k) = SMA_t(k) and lim_{λ→0} REMA_t(k) = P_{t-k} [[sources/pdf-ec9fdef2193c]].
- The usual justification for using LMA or EMA over SMA is the widespread belief that the most recent stock prices contain more relevant information on the future direction of the stock price than earlier prices [[sources/pdf-ec9fdef2193c]].
- Some traders use "moving averages of moving averages" — Triangular Moving Average, Double Exponential Moving Average, Triple Exponential Moving Average — but Zakamulin omits these to streamline presentation while noting the same anatomy methodology applies to them [[sources/pdf-ec9fdef2193c]].
- Zakamulin follows the standard practice of using prices not adjusted for dividends in the computation of moving averages and all technical trading indicators [[sources/pdf-ec9fdef2193c]].

## Sources

- [[sources/pdf-ec9fdef2193c]]

## Related

- [[concepts/weighted-moving-average-of-price-changes]]
- [[concepts/anatomy-of-moving-average-rules]]
- [[concepts/weighting-function-shape-determines-performance]]
- [[entities/valeriy-zakamulin]]
