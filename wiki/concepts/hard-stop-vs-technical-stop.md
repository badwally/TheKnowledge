---
schema_version: 1
type: concept
slug: hard-stop-vs-technical-stop
canonical_name: Hard Percentage Stop vs Technical Stop
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Hard Percentage Stop vs Technical Stop

## Summary

Risk-management lesson distilled from BobaTrader's transition from a rigid hard 15% stop loss applied to every options trade to a stop placed where the technicals dictate — a shift driven by the empirical observation that the hard percentage stop was getting triggered too often on trades that ended up going his way almost immediately afterward [[sources/pdf-9613f301a3b5]].

## Key claims

- BobaTrader implemented a hard stop at 15% on every trade, no matter what — never moved, never adjusted, and let the trades play out — for about two months as the first formal risk-management discipline he ever applied [[sources/pdf-9613f301a3b5]].
- Outcome of the experiment: losses were kept small, but the stop was getting triggered too much, especially on trades that ended up going his way almost immediately after he was stopped out [[sources/pdf-9613f301a3b5]].
- Conclusion: a 15% hard stop "doesnt always work," and the better discipline is to rely mostly on the technicals to tell where to cut the trade [[sources/pdf-9613f301a3b5]].
- Identified as the inflection point in the trader's development of risk-management instincts: keeping losses small only matters if the stops are not so tight that winning trades are cut prematurely [[sources/pdf-9613f301a3b5]].

## Sources

- [[sources/pdf-9613f301a3b5]]

## Related

- [[entities/bobatrader]]
- [[concepts/morning-sd-zone-reversal]]
