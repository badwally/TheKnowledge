---
schema_version: 1
type: concept
slug: short-gamma-hedging
canonical_name: Short gamma hedging
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Short gamma hedging

## Summary

Short gamma hedging is the trading activity required of a market participant who is net short gamma in a derivative or leveraged product: to keep their position delta-neutral, they must buy the underlying when its price is rising and sell when it is falling — trading in the direction of the price movement and thereby exacerbating swings [[sources/pdf-2742492120a8]].

## Key claims

- Gamma measures how much the price of a derivative accelerates when the underlying security price moves; market makers in products with gamma exposure such as options and leveraged ETFs are commonly net short these products [[sources/pdf-2742492120a8]].
- Consequently, hedging short gamma forces the market maker to buy additional securities when prices are rising and sell when prices are falling in order to ensure positions stay delta-neutral, which exacerbates market swings and produces "market intraday momentum" [[sources/pdf-2742492120a8]].
- During the last week of February 2020, JPMorgan Chase estimated that more than $100 billion in stock selling during the first two days of the week was due to such short-gamma hedging activities — a real-world illustration cited at the opening of Baltussen, Da, Lammers, and Martens (2020) [[sources/pdf-2742492120a8]].
- The same hedging logic has existed for a long time and includes dynamic hedging programs like portfolio insurance (Leland and Rubinstein 1976) and the hedging of variable annuities by insurers; volatility-targeting strategies, variance swaps, and levered or inverse ETFs all conduct similar hedging trades [[sources/pdf-2742492120a8]].
- Baltussen et al. argue that hedging is concentrated at the end of the trading day for five reasons: optimal-partial-hedging under fixed transaction costs (Clewlow and Hodges 1997), liquidity (the U-shape volume pattern), overnight-risk protection (Brock and Kleidon 1992; Hong and Wang 2000), capital and margin frictions on overnight positions (Bogousslavsky 2020), and the structural fact that LETFs and variance-swap dealers settle off the close [[sources/pdf-2742492120a8]].

## Sources

- [[sources/pdf-2742492120a8]]

## Related

- [[concepts/market-intraday-momentum]]
- [[concepts/negative-gamma-exposure]]
- [[concepts/leveraged-etf-rebalancing-demand]]
- [[concepts/transitory-price-pressure]]
- [[concepts/gamma-reflexivity]]
- [[concepts/portfolio-insurance]]
