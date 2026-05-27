---
schema_version: 1
type: concept
slug: pd-array
canonical_name: Price Delivery Array (PD Array)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Price Delivery Array (PD Array)

## Summary

A labeled dealing range — the price range between a swing high and a swing low where displacement and a market structure shift (MSS) have occurred — classified as either bullish or bearish, within which order blocks, fair value gaps, and the equilibrium level define trade entries, stops, and targets [[sources/pdf-f2565310670c]]; Ali Khan's "The ICT Bible" (2023) expands the concept by defining PD Arrays as data points stored within IPDA's repricing logic that become active when time aligns with price, and publishes the PD Array Matrix — a ranked hierarchy of premium and discount arrays that includes old highs/lows, rejection blocks, order blocks, breaker blocks, mitigation blocks, and FVGs [[sources/pdf-ali-khan-2023-the-ict-bible]].

## Key claims

- A PD Array is the dealing range defined by a swing low/high and a swing high/low with displacement and MSS between them [[sources/pdf-f2565310670c]].
- A Bullish PD Array runs from a swing low (where upward displacement begins) to a swing high (where displacement ends); the trader buys in the discount zone and sells in the premium zone or above [[sources/pdf-f2565310670c]].
- What makes a PD Array bullish: yearly lows (liquidity) have been run, there is a failure to displace down, price displaces up creating MSS and supportive structure for longs, with targets at old swing highs or FVGs [[sources/pdf-f2565310670c]].
- A Bearish PD Array runs from a swing high (where downward displacement begins) to a swing low (where displacement ends); the trader sells in the premium zone and buys back in the discount zone or below to exit shorts [[sources/pdf-f2565310670c]].
- What makes a PD Array bearish: yearly highs (liquidity) have been run, there is a failure to displace up, price displaces down creating MSS and supportive structure for shorts, with targets at old swing lows or FVGs [[sources/pdf-f2565310670c]].
- The Fibonacci tool is applied across the PD Array to find the 0.5 equilibrium, dividing it into discount (below 0.5) and premium (above 0.5) [[sources/pdf-f2565310670c]].
- Inside a PD Array, order blocks and fair value gaps serve as specific entry zones with defined stops and targets [[sources/pdf-f2565310670c]].
- Using the Fibonacci tool on a PD Array allows the trader to define the range, recognize market structure supporting longs or shorts, label the array as bullish or bearish, identify entry zones in discount or premium, and establish defined stops and targets [[sources/pdf-f2565310670c]].
- Typical targets are the most recent swing point that creates the PD Array boundary and then swing points outside the range (external liquidity) [[sources/pdf-f2565310670c]].
- Per Ali Khan, arrays are "data points that are stored within a program" — key price levels stored in IPDA's repricing logic, relative to a premium/discount market, that will be referred back to at later dates [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, these arrays become active when time aligns with price — "We do not have zones in ICT logic. Each array has specific levels, which can be graded and calibrated" [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, there will be different arrays present in each swing that can offer support/resistance; monitoring how price reacts at these key levels can help gauge order flow in a bullish or bearish market environment [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, the PD Array Matrix ranks arrays from premium to discount as follows (from outermost to market price): Old High/Low, Rejection Block, Order Block, Breaker Block, Mitigation Block, FVG — with the same hierarchy mirrored on both the premium and discount side of market price [[sources/pdf-ali-khan-2023-the-ict-bible]].

## Sources

- [[sources/pdf-f2565310670c]]
- [[sources/pdf-ali-khan-2023-the-ict-bible]]

## Related

- [[concepts/equilibrium-discount-premium]]
- [[concepts/internal-vs-external-liquidity]]
- [[concepts/po3-dealing-range]]
- [[concepts/order-block]]
- [[concepts/breaker-block]]
- [[concepts/fair-value-gap]]
- [[concepts/ipda]]
- [[concepts/killzones]]
- [[concepts/displacement]]
- [[concepts/market-structure-shift]]
- [[entities/ali-khan]]