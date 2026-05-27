---
schema_version: 1
type: concept
slug: iron-condor-dealer-positioning
canonical_name: Iron Condor dealer positioning
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Iron Condor dealer positioning

## Summary

When a customer places an Iron Condor, the dealer takes the other side of both legs — leaving the dealer short the upper-strike calls 2–3 strikes above current price with a long delta exposure that must be hedged, while sitting short gamma at current price [[sources/pdf-ea646c451aae]].

## Key claims

- Large positive gamma exposure 2–3 strikes above the current price corresponds to the long call leg of an Iron Condor placed earlier in the day [[sources/pdf-ea646c451aae]].
- Dealers are short those calls, meaning they hold a long delta exposure that they must hedge [[sources/pdf-ea646c451aae]].
- A spike in volume at the upper call strike can represent either buyers closing their short calls (if those calls were part of the Iron Condor) or buying outright in anticipation of a breakout [[sources/pdf-ea646c451aae]].
- Combined with massive negative gamma at current price, the Iron Condor leaves dealers short gamma at the body of the structure with positive gamma at the wings — the configuration that drives the end-of-day squeeze dynamic [[sources/pdf-ea646c451aae]].

## Sources

- [[sources/pdf-ea646c451aae]]

## Related

- [[concepts/dealer-short-gamma-mechanics]]
- [[concepts/gamma-squeeze-into-close]]
