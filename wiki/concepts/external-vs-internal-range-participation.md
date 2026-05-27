---
schema_version: 1
type: concept
slug: external-vs-internal-range-participation
canonical_name: External-vs-Internal Range Participation
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# External-vs-Internal Range Participation

## Summary

A participation filter that distinguishes the high-probability act of engaging external-range liquidity (the range high as buyside liquidity, the range low as sellside liquidity) from the low-probability act of trading inside the consolidated internal range; AMtrades uses this dichotomy as the through-line connecting daily consolidation, engineering liquidity, and inside-day rules [[sources/pdf-46c6dd54d41e]].

## Key claims

- External range high is treated as buyside liquidity; external range low is treated as sellside liquidity — the two boundaries the trader is willing to engage [[sources/pdf-46c6dd54d41e]].
- The internal portion of a consolidated range is explicitly avoided for participation [[sources/pdf-46c6dd54d41e]].
- Engaging external liquidity is high-probability; engineering liquidity inside the range is low-probability — the two are framed as inverses of each other [[sources/pdf-46c6dd54d41e]].
- After external liquidity is engaged with no further drive, the read is counter-narrative and the target is range equilibrium [[sources/pdf-46c6dd54d41e]].
- After external liquidity is purged with directional follow-through, the read is directional-narrative and the target is the opposite end of the range plus expansion continuation [[sources/pdf-46c6dd54d41e]].
- The same principle is applied at the daily level (avoid internal consolidated daily range; wait for external range engagement) and at the inside-day level (avoid trading within the previous day's range when H1+ PD arrays are absent) [[sources/pdf-46c6dd54d41e]].

## Sources

- [[sources/pdf-46c6dd54d41e]]

## Related

- [[entities/amtrades]]
- [[concepts/daily-consolidation-profile]]
- [[concepts/engineering-liquidity]]
- [[concepts/inside-day-trapped-order-flow]]
