---
schema_version: 1
type: concept
slug: ttrades-entry-models
canonical_name: TTrades Entry Models
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# TTrades Entry Models

## Summary

TTrades Entry Models is a smart-money trade-entry framework first published as a 2022 5-page PDF reference card cataloguing four trigger-stack models [[sources/pdf-c57b9a32c399]] and expanded in a 2023 6-page revision that adds a fifth "Box Setup" model [[sources/pdf-3a510f58854c]]; Models 1–4 share a common HTF-premise / LTF-trigger scaffold and stack ingredients in a fixed order (BOS+FVG → +IDM → +OTE → +IDM+OTE), while Model 5 is a structurally distinct consolidation-and-retest pattern that can optionally be traded without an HTF point-of-interest [[sources/pdf-3a510f58854c]].

## Key claims

- The 2022 reference card defined four models — Model 1 (HTF + BOS + FVG), Model 2 (HTF + BOS + IDM + FVG), Model 3 (HTF + BOS + FVG + OTE, labeled "Model 1 + OTE"), and Model 4 (HTF + BOS + IDM + FVG + OTE, labeled "Model 2 + OTE") [[sources/pdf-c57b9a32c399]]; the 2023 reference card kept these and added a fifth, Model 5 (Box Setup) [[sources/pdf-3a510f58854c]].
- Models 1–4 share an identical scaffold: HTF POI → HTF LIQ GRAB / FVG / POI → LTF Liquidity Grab → BOS + Displacement + FVG → entry qualified as FVG In Discount (longs) or FVG In Premium (shorts) → "Good Risk : Reward" gate [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].
- The progression from Model 1 to Model 4 is additive and orthogonal: Model 2 adds Internal Liquidity (IDM) confluence, Model 3 adds OTE .62–.79 fibonacci refinement, and Model 4 stacks both [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].
- In the 2022 version, the variations of OTE-extended Models 3 and 4 are labeled "Model 1 Variation" and "Model 2 Variation" respectively rather than "Model 3 Variation" and "Model 4 Variation," signaling that OTE is a refinement on top of the parent rather than an independent model [[sources/pdf-c57b9a32c399]].
- Each of Models 1–4 is published in two directions (bullish, bearish) and with two named variations (Failed swing, SMT), yielding 16 trade-shape diagrams across the four trigger-stack models [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].
- Model 5 (Box Setup) is the structural outlier introduced in 2023: bullish geometry is HTF POI / Low → Original Consolidation Range → Aggressive Down → Aggressive Up → Retest of Original Consolidation Low, with the bearish version mirrored, and an experimental "No POI" variation explicitly permitted [[sources/pdf-3a510f58854c]].
- A "Good Risk : Reward" check is the final gate on every model in the framework, framing R:R as the deciding filter once structural ingredients are present [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].
- The framework is presented as a checklist rather than a discretionary teaching: each model is a fixed sequence of named ingredients, and a setup is either present or not present rather than subjectively interpreted [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].

## Sources

- [[sources/pdf-c57b9a32c399]]
- [[sources/pdf-3a510f58854c]]

## Related

- [[concepts/break-of-structure]]
- [[concepts/htf-poi]]
- [[concepts/optimal-trade-entry]]
- [[concepts/failed-swing]]
- [[concepts/box-setup]]
- [[concepts/liquidity-grab]]
- [[concepts/fair-value-gap]]
- [[concepts/displacement]]
- [[concepts/internal-range-liquidity]]
- [[concepts/smt-divergence]]
- [[entities/ttrades]]
- [[entities/inner-circle-trader]]
