---
schema_version: 1
type: concept
slug: htf-poi
canonical_name: Higher-Timeframe Point of Interest (HTF POI)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Higher-Timeframe Point of Interest (HTF POI)

## Summary

In ICT trading, a higher-timeframe point of interest (HTF POI) is a price level on a higher timeframe — typically an external liquidity pool or premium/discount array — that price targets during the manipulation phase of a Power of 3 setup before reversing into distribution [[sources/pdf-a3789262265a]]; in TTrades's framework, the HTF POI is the directional premise at the top of every Models 1–4 scaffold, paired interchangeably with an HTF liquidity grab or HTF FVG [[sources/pdf-c57b9a32c399]].

## Key claims

- In a bearish PO3, price will look to reprice higher to an HTF POI before setting up a market maker model that favors the sell-side [[sources/pdf-a3789262265a]].
- In a bullish PO3, price will look to reprice lower to an HTF POI before setting up a market maker model that favors the buy-side [[sources/pdf-a3789262265a]].
- HTF POIs include both premiums of an array and external liquidity — price manipulates toward whichever is more relevant before setting up the market maker model [[sources/pdf-a3789262265a]].
- TTrades places the HTF POI at the apex of all four trigger-stack models, framed as the "H" in "HTF + BOS + FVG" / "HTF + BOS + IDM + FVG" / "HTF + BOS + FVG + OTE" / "HTF + BOS + IDM + FVG + OTE" [[sources/pdf-c57b9a32c399]].
- TTrades treats the HTF POI, HTF liquidity grab, and HTF FVG as substitutes that can establish the same directional premise — the scaffold reads "HTF LIQ GRAB / FVG / POI" with slashes denoting interchangeability [[sources/pdf-c57b9a32c399]].
- In the Failed swing and SMT variations of Models 1–4, the HTF POI premise is preserved while the upstream LTF liquidity-grab leg is replaced — confirming that the HTF POI is the framework's anchor, not the liquidity-grab variant [[sources/pdf-c57b9a32c399]].

## Sources

- [[sources/pdf-a3789262265a]]
- [[sources/pdf-c57b9a32c399]]

## Related

- [[concepts/amd-cycle]]
- [[concepts/market-maker-sell-model]]
- [[concepts/market-maker-buy-model]]
- [[concepts/buyside-sellside-liquidity]]
- [[concepts/ttrades-entry-models]]
- [[concepts/break-of-structure]]
- [[concepts/liquidity-grab]]
- [[concepts/fair-value-gap]]
- [[entities/ttrades]]
