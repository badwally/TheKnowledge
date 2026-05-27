---
schema_version: 1
type: concept
slug: po3-dealing-range
canonical_name: Power of 3 (PO3) Dealing Range
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Power of 3 (PO3) Dealing Range

## Summary

A Power of 3 (PO3) dealing range is a price segment, sized as a power of three (3, 9, 27, 81, 243, 729, ...) in pips or points, in which swings are expected to occur and price tends to consolidate before breaking out to the adjacent partition; introduced by Hopiplaka as the price-side mechanic that maps ICT dealing-range concepts onto the Tesla 3-6-9 numerical framework [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].

## Key claims

- In Hopiplaka's framework, dealing ranges are made of powers of the number three — 3, 9, 27, 81, 243, 729, 2187, etc. — calculated as 3^n and expressed in pips for FX or points for index futures (e.g., a 243-pip EURUSD range or an 81-point Nasdaq futures range) [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- A dealing range is a piece of price action where swings are expected; it has a dealing-range low and a dealing-range high, and price tends to stay inside it unless it breaks out into the next partition [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- Partitions are computed from base 0.0: e.g., for PO3 = 27, partitions run 0–27, 27–54, 54–81, ..., contiguously across the price axis [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- The dealing-range low is computed as `floor(current_price / optimal_PO3) * optimal_PO3`, where the floor function takes only the integer part of the division and the price input drops the decimal point (first 5 digits for FX, integer part for indices/crypto) [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]].
- Each PO3 power maps to a trader profile: 3 for stop runs, 9 for stop runs / scalping, 27 for intraday/session traders, 81 for daily range, 243 for weekly range, 729 for monthly range, 2187 for yearly range; 6561 / 19683 / 59049 / 177147 extend the table for higher powers [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- The optimal PO3 size for an asset is determined by visually inspecting a 4-hour chart for obvious recurring swing sizes [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]]; Version 1.1.3 adds an alternative computational method using the Average Daily Range (20-day setting) or Average Weekly Range (12-week setting) rounded to the nearest power of three, with ties resolved in favor of the higher PO3 [[sources/pdf-1ab14c833d75]].
- Hopiplaka illustrates the framework on a Microsoft chart using PO3 = 27, showing partitions at 0–27, 27–54, 54–81, ..., with price typically dwelling inside one partition before transitioning [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- A correctly-chosen dealing range is verified by observing that major swings occur around its extremes (high/low or external range demarker) and equilibrium [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].

## Sources

- [[sources/pdf-930894c4fbad]]
- [[sources/pdf-94cecf7a170a]]
- [[sources/pdf-1ab14c833d75]]

## Related

- [[entities/hopiplaka]]
- [[entities/inner-circle-trader]]
- [[concepts/power-of-3]]
- [[concepts/goldbach-levels]]
- [[concepts/fractal-po3]]
- [[concepts/tesla-vortex-3-6-9]]
- [[concepts/hippo-look-back]]
