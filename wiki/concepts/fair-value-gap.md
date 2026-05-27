---
schema_version: 1
type: concept
slug: fair-value-gap
canonical_name: Fair Value Gap
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Fair Value Gap

## Summary

A fair value gap (FVG) — used interchangeably with "imbalance" in the ICT-derived order-block vocabulary — is a price area left behind by an energetic displacement that traders treat as a future entry/exit zone; FVGs are typically found alongside order blocks and obey the same liquidity-driven logic [[sources/pdf-69a1f97797ce]], they are the central qualified-entry zone in TTrades's Models 1–4, where the trade is taken at "FVG In Discount" (longs) or "FVG In Premium" (shorts) [[sources/pdf-c57b9a32c399]], and the canonical MMXM PDF lists FVGs alongside order blocks as the canonical re-accumulation (MMBM) or re-distribution (MMSM) zones inside the model [[sources/pdf-d7094631fbf1]]; Ali Khan's "The ICT Bible" (2023) adds the BISI/SIBI taxonomy, the three-pass redelivery/rebalancing lifecycle, three internal support/resistance levels (premium, discount, and consequent encroachment), and distinguishes FVGs from volume imbalances (V.I.) and gap imbalances (G.I.) [[sources/pdf-ali-khan-2023-the-ict-bible]].

## Key claims

- An FVG / imbalance is created when price aggressively displaces and leaves a price area behind, e.g., when price runs recent lows and "aggressively displaces up" creating an imbalance/FVG and an OB demand zone [[sources/pdf-69a1f97797ce]].
- FVGs are used the same way as order blocks — as zones where the trader looks to enter and/or close positions [[sources/pdf-69a1f97797ce]].
- After a setup is validated by displacement + MSS, the trader looks to add long (or short) in the small FVG and/or OB the displacement leaves behind [[sources/pdf-69a1f97797ce]].
- The same liquidity logic that explains why order blocks work is also used for FVGs, which are usually found with order blocks [[sources/pdf-69a1f97797ce]].
- Retracements that take price back into prior FVGs and OBs and produce new OBs are described as a sign of trend — e.g., a bullish PD Array forming during a bullish trend [[sources/pdf-69a1f97797ce]].
- The lesson's summary checklist groups Imbalance/OB/FVG together as the entry-zone primitive, sitting after MSS and before Target Liquidity [[sources/pdf-69a1f97797ce]].
- In TTrades's framework, the FVG appears at two scales: an HTF FVG inside the "HTF LIQ GRAB / FVG / POI" premise, and an LTF FVG produced by the BOS + Displacement + FVG entry trigger; the LTF FVG is the actual entry zone [[sources/pdf-c57b9a32c399]].
- The TTrades trade is taken only when the LTF FVG sits in discount of the swing (longs, "FVG In Discount") or in premium (shorts, "FVG In Premium"), making FVG location relative to swing equilibrium a hard filter on entry [[sources/pdf-c57b9a32c399]].
- The MMXM PDF treats FVGs (alongside OBs) as the retracement zones into which longs re-accumulate (in an MMBM) or shorts re-distribute (in an MMSM), and ties their formation to the displacement leg that creates the model's market structure shift [[sources/pdf-d7094631fbf1]].
- Per the MMXM PDF, FVGs are one of the inefficiency types (alongside SIBI, BISI, voids, gaps) that count as a draw on liquidity in higher-timeframe analysis [[sources/pdf-d7094631fbf1]].
- Per Ali Khan, IPDA may reprice too quickly in one direction, leaving an inefficiency in price delivery (a FVG); in order for IPDA to maintain its fair value parameters, it will reprice to rebalance the inefficient price action to offer fair value to both sides of the market [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, a BISI (Buyside Imbalance, Sellside Inefficiency) occurs when IPDA has repriced to buyside too quickly, leaving a buyside imbalance — the wicks offer both buying and selling in the up and down movement, but the body where no wicks overlap is all buyside delivery and inefficient of any sellside delivery [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, a SIBI (Sellside Imbalance, Buyside Inefficiency) occurs when IPDA has repriced to sellside too quickly, leaving a sellside imbalance — the body where no wicks overlap is all sellside delivery and inefficient of any buyside delivery [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, when buyside movement is redelivered back through a sellside imbalance, the inefficient sellside imbalance has been matched with buyside price delivery, offering a balanced price range of both buyside and sellside delivery [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, when price passes back through this range for a 3rd time and leaves it, the whole range has been rebalanced; any upward movement back through this range should be met with strong resistance (in a bearish market) [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, an FVG has three levels of true support and resistance: the PREMIUM level (high) offers support in a bullish market if price has closed above it, the DISCOUNT level (low) offers resistance in a bearish market if price has closed below it, and the CONSEQUENT ENCROACHMENT (C.E.) is the midpoint or 50% equilibrium level [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, the premium/discount FVG levels become even stronger as support/resistance if the FVG has been balanced/rebalanced [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, an FVG can indicate that IPDA is in a hurry to move price in one direction over another — "an algorithmic footprint that we can see in price action" [[sources/pdf-ali-khan-2023-the-ict-bible]].
- Per Ali Khan, ICT uses the analogy of an elephant stepping into a children's pool — since the size and mass of the elephant's foot is so large, we see a displacement of water — drawing a comparison to larger institutions with "deep pockets" entering the marketplace [[sources/pdf-ali-khan-2023-the-ict-bible]].

## Sources

- [[sources/pdf-69a1f97797ce]]
- [[sources/pdf-c57b9a32c399]]
- [[sources/pdf-d7094631fbf1]]
- [[sources/pdf-ali-khan-2023-the-ict-bible]]

## Related

- [[concepts/order-block]]
- [[concepts/displacement]]
- [[concepts/market-structure-shift]]
- [[concepts/liquidity-grab]]
- [[concepts/htf-point-of-interest]]
- [[concepts/htf-poi]]
- [[concepts/liquidity-void]]
- [[concepts/discount-and-premium]]
- [[concepts/ttrades-entry-models]]
- [[concepts/market-maker-buy-model]]
- [[concepts/market-maker-sell-model]]
- [[concepts/draw-on-liquidity]]
- [[concepts/balanced-price-range]]
- [[concepts/consequent-encroachment]]
- [[concepts/volume-imbalance]]
- [[concepts/gap-imbalance]]
- [[concepts/ipda]]
- [[concepts/market-efficiency-paradigm]]
- [[entities/ttrades]]
- [[entities/ali-khan]]