---
schema_version: 1
type: concept
slug: market-net-flow
canonical_name: Market Net Flow (MNF)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Market Net Flow (MNF)

## Summary

The Market Net Flow (MNF) tool by Tradytics visualizes how option participants are affecting dealers — forcing them to hedge — via a call line (green) and put line (red) plotted relative to a zero line; Matthew Ryan uses divergences between the two lines as a confluence overlay on his 2-Day AVWAP trend rule, refusing to trade when no divergence is present [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Key claims

- MNF shows how option participants affect dealers and force them to hedge — Ryan describes dealer hedging as too extensive to cover in his manual but recommends an advanced understanding of Gamma/Vanna levels [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Bullish MNF: calls (green line) above puts (red line) with puts below the zero line [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Bearish MNF: puts (red line) above calls (green line) with calls below the zero line [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- No-divergence MNF: no divergence of either calls or puts — when paired with price between both VWAPs, this is an explicit no-trade signal [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Sometimes price is above (or below) both VWAPs without MNF confluence; in those cases Ryan recommends waiting for divergence before placing trades because divergence can show up at any time of day [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Sources

- [[sources/pdf-2248d6cdc39f]]
- [[sources/pdf-6ba2dc608ac8]]

## Related

- [[entities/tradytics]]
- [[concepts/trend-confluence]]
- [[concepts/two-day-avwap-rule]]
- [[entities/matthew-ryan]]
