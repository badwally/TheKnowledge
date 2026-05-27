---
schema_version: 1
type: concept
slug: two-day-avwap-rule
canonical_name: 2-Day AVWAP Rule
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# 2-Day AVWAP Rule

## Summary

The 2-Day AVWAP Rule is Matthew Ryan's intraday trend-classification mechanic: anchor one VWAP to the previous trading day's open and a second VWAP to the current trading day's open, then classify the market as uptrend, downtrend, or no-trend based on price's position relative to both lines, with a strict no-trade rule when price is between them [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Key claims

- If price is ABOVE both VWAPs, the market is in a potential uptrend and only bullish A+ setups should be considered [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- If price is BELOW both VWAPs, the market is in a potential downtrend and only bearish A+ setups should be considered [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- If price is IN BETWEEN both VWAPs, no trend is established and trades must not be taken — codified as "no trend, no trade" [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Ryan emphasizes that committing these rules to memory is essential because they must be followed during times of heightened emotion when the trader is most likely to override them [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Sources

- [[sources/pdf-2248d6cdc39f]]
- [[sources/pdf-6ba2dc608ac8]]

## Related

- [[concepts/anchored-vwap]]
- [[concepts/trend-confluence]]
- [[concepts/stochastic-momentum-signal]]
- [[entities/matthew-ryan]]
