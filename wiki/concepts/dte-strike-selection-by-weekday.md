---
schema_version: 1
type: concept
slug: dte-strike-selection-by-weekday
canonical_name: Day-of-Week Options Strike and Expiration Selection
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Day-of-Week Options Strike and Expiration Selection

## Summary

Heuristic for choosing options contract expiration and strike based on the calendar day on which the trade is taken, codified in BobaTrader's 2022 daytrading guide as a way to keep residual time-to-expiration roughly constant across the trading week and to bias strike distance to the current price based on how much room remains until expiry [[sources/pdf-9613f301a3b5]].

## Key claims

- Monday–Wednesday rule: take the same-week Friday expiration, at the money (closer to the current price of the stock) [[sources/pdf-9613f301a3b5]].
- Worked example for the Monday rule: on 10/18/21 (a Monday), the trade entered the 10/22/21 (same-week Friday) $444 Calls — $0.50 out of the money [[sources/pdf-9613f301a3b5]].
- Thursday–Friday rule: take the next-week expiration, slightly out the money (a bit farther from the current price of the stock) [[sources/pdf-9613f301a3b5]].
- Worked example for the Friday rule: on 1/28/22 (a Friday), when $SPY hit the entry, the trade picked up the next-week Friday expiration (2/4/22) $430 Calls — $2 out of the money [[sources/pdf-9613f301a3b5]].

## Sources

- [[sources/pdf-9613f301a3b5]]

## Related

- [[entities/bobatrader]]
- [[concepts/morning-sd-zone-reversal]]
