---
schema_version: 1
type: concept
slug: trend-confluence
canonical_name: Trend confluence
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Trend confluence

## Summary

In Matthew Ryan's framework, trend confluence is the requirement that two independent indicators agree on direction before a trade is taken — specifically, the 2-Day Anchored VWAP rule and Tradytics Market Net Flow must both signal the same direction (or both signal "no trend") — and is the gating condition that elevates entry probability when paired with Momentum-Signal timing [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Key claims

- Bullish confluence: when price is above both VWAPs (uptrend), pair with bullish MNF (calls above puts, puts below zero line) — this is the configuration in which long entries are sought [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Bearish confluence: when price is below both VWAPs (downtrend), pair with bearish MNF (puts above calls, calls below zero line) — this is the configuration in which short entries are sought [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- No-divergence confluence: when price is between both VWAPs and MNF shows no divergence, do not take trades — explicit no-trade configuration [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Price can be above or below both VWAPs without MNF confluence; in those cases Ryan recommends waiting for MNF divergence to materialize before placing trades because divergence can appear at any time of day [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- When confluence is achieved, only buy at %K oversold (bullish) or only sell at %K overbought (bearish) — confluence is necessary but not sufficient, since Momentum Signal positioning still gates the entry [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Sources

- [[sources/pdf-2248d6cdc39f]]
- [[sources/pdf-6ba2dc608ac8]]

## Related

- [[concepts/two-day-avwap-rule]]
- [[concepts/market-net-flow]]
- [[concepts/stochastic-momentum-signal]]
- [[entities/matthew-ryan]]
