---
schema_version: 1
type: concept
slug: fractal-po3
canonical_name: Fractal PO3
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Fractal PO3

## Summary

Fractal PO3 is the multi-timeframe application of Power of 3 dealing ranges in Hopiplaka's framework: traders watch the optimal PO3 size for the chart, plus one PO3 level higher (long-term context) and one PO3 level lower (range-expansion or contraction signal), so the same dealing-range structure recurses across scales [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].

## Key claims

- Hopiplaka recommends viewing a chart at one PO3 level higher than the optimal size to follow the longer-term picture, typically on a 4H or daily chart (e.g., using a PO3 = 729 chart when the optimal range is 243) [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- He also recommends monitoring one PO3 level lower (e.g., PO3 = 81 when the optimal is 243) to detect when range expansion (use the larger PO3 number) or range contraction (use the lower PO3 number) is appropriate [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- A fractal PO3 stack therefore consists of three coordinated dealing-range views — current, higher, lower — each computed as 3^n in pips or points [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- Fractal PO3 also operates intra-range: PO3 stop runs and PO3 liquidity dynamics recur at smaller scales inside the active dealing range [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- Range expansion and range contraction are explicit operations on the fractal stack: when price aggressively trades through partition levels, traders move up to the next PO3 number; when activity compresses, they move down [[sources/pdf-930894c4fbad]] [[sources/pdf-94cecf7a170a]] [[sources/pdf-1ab14c833d75]].
- The PO3 DR Shifting technique — covered in the book's Miscellaneous chapter in Version 1.1.3 — adjusts where the partition's base is anchored, providing a complementary degree of freedom on top of the fractal stack [[sources/pdf-1ab14c833d75]].

## Sources

- [[sources/pdf-930894c4fbad]]
- [[sources/pdf-94cecf7a170a]]
- [[sources/pdf-1ab14c833d75]]

## Related

- [[entities/hopiplaka]]
- [[concepts/po3-dealing-range]]
- [[concepts/tesla-vortex-3-6-9]]
- [[concepts/goldbach-levels]]
