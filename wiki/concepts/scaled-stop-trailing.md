---
schema_version: 1
type: concept
slug: scaled-stop-trailing
canonical_name: Scaled Stop Trailing (50% / 75% Rule)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Scaled Stop Trailing

## Summary

A mechanical stop-loss management protocol taught in ICT's 2022 mentorship and recapped by Trader Theory: when price reaches 50% of the take-profit target, raise (long) or lower (short) the stop by 25% of the entry price; when price reaches 75% of the target, move the stop to entry; and if the take-profit is not hit within the session in which the trade was taken, collapse the trade at the session close [[sources/pdf-a98b496e5936]].

## Key claims

- 50%-to-target action: "When prices reach 50% of your target, raise/lower your SL by 25% of the entry price" [[sources/pdf-a98b496e5936]].
- 75%-to-target action: "When the price reaches 75% of your target, move SL to entry" [[sources/pdf-a98b496e5936]].
- End-of-session action: "If your TP isn't hit during the session you take the trade, then collapse the trade" [[sources/pdf-a98b496e5936]].
- Locks in incremental gains as the trade matures and bounds time-in-market to a single session — consistent with the methodology's NY AM (8:30–12:00) and NY PM (13:00–16:30) session focus [[sources/pdf-a98b496e5936]].

## Sources

- [[sources/pdf-a98b496e5936]]

## Related

- [[concepts/halving-risk-after-loss]]
- [[concepts/fvg-selection-and-stops]]
- [[entities/trader-theory]]
- [[entities/inner-circle-trader]]
