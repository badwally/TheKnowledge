---
type: concept
slug: anchored-vwap
canonical_name: Anchored VWAP (AVWAP)
domains:
  - trading-and-markets
---

# Anchored VWAP (AVWAP)

## Summary

An Anchored VWAP is a volume-weighted average price calculation that begins from a specific user-chosen anchor point (e.g., the open of a particular trading day) rather than the start of the standard session, and is used as a trend-state reference: in trending conditions, price reacts favorably to the AVWAP line, so multiple AVWAPs anchored to different days form the basis of Matthew Ryan's 2-Day AVWAP trend rule [[sources/pdf-2248d6cdc39f]].

## Key claims

- AVWAP is anchored to a user-chosen point such as the open of the previous trading day or the open of the current trading day [[sources/pdf-2248d6cdc39f]].
- Price reacts favorably to VWAP in trending conditions, which is the empirical observation that motivates using AVWAP as a trend filter [[sources/pdf-2248d6cdc39f]].
- Ryan combines two AVWAPs — one anchored to the previous day's open and one anchored to the current day's open — to determine intraday trend state [[sources/pdf-2248d6cdc39f]].

## Sources

- [[sources/pdf-2248d6cdc39f]]

## Related

- [[concepts/two-day-avwap-rule]]
- [[concepts/trend-confluence]]
- [[entities/matthew-ryan]]
