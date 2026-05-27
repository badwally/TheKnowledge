---
schema_version: 1
type: concept
slug: discount-and-premium
canonical_name: Discount and premium
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Discount and premium

## Summary

In the Power of 3 framework, "discount" and "premium" describe price's location relative to the open of the candle's range: a discount sits below the open (where bulls accumulate), a premium sits above (where bears distribute); the bullish OLHC template seeks a discount before expanding up, the bearish OHLC template seeks a premium before expanding down [[sources/pdf-075e9932265b]].

## Key claims

- In the bullish OLHC template, price will seek a discount of a previous price range, which is the optimal trade entry zone inside an FVG or OB [[sources/pdf-075e9932265b]].
- In the bearish OHLC template, price will seek a premium of a previous price range, which is the OTE zone inside an FVG or OB [[sources/pdf-075e9932265b]].
- On weekly candles, a bullish week opens and seeks a discount under the weekly open before moving up; a bearish week seeks a premium over the open before moving down [[sources/pdf-075e9932265b]].
- On daily candles anchored to the midnight open, bullish days seek a discount under the open and bearish days seek a premium over the open [[sources/pdf-075e9932265b]].
- A "deep discount" is the daily PO3 scenario where price drops well below the midnight open before reversing — visible in the bullish OLHC daily example as the OPEN → LOW phase preceding the displacement up [[sources/pdf-075e9932265b]].
- The discount or premium of a previous range (previous day, previous week, previous month) is the specific zone where the OTE inside an FVG or OB is sought [[sources/pdf-075e9932265b]].

## Sources

- [[sources/pdf-075e9932265b]]

## Related

- [[concepts/power-of-3]]
- [[concepts/optimal-trade-entry]]
- [[concepts/buyside-liquidity]]
- [[concepts/sellside-liquidity]]
- [[concepts/fair-value-gap]]
- [[concepts/order-block]]
