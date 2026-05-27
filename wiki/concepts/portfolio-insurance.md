---
schema_version: 1
type: concept
slug: portfolio-insurance
canonical_name: Portfolio insurance
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Portfolio insurance

## Summary

A dynamic-hedging product developed by LOR Associates (Leland, O'Brien, and Rubinstein) in the 1980s that replicated the payoff of a purchased index put for institutional clients by systematically selling futures as the market declined; Ambrus Capital invokes it as the historical analog to modern dealer gamma hedging [[sources/pdf-04854302f962]], and Andrew Constan's firsthand account from the Brady Commission confirms that two major institutional sellers using the technique dominated the selling on Black Monday (October 19, 1987), with the strategy's covering of short futures on the way up likely partly causal for the 39% YTD rally that preceded the crash [[sources/pdf-f139d7bd1924]].

## Key claims

- Created by Leland, O'Brien, and Rubinstein (LOR) at a time when index options were only six years old (since 1981), because low institutional liquidity in options made direct put purchasing impractical [[sources/pdf-f139d7bd1924]].
- The technique replicated the payoff of a purchased index put — "exactly the same as a dealer who has sold a put to a client would use to dynamically hedge their exposure" — requiring only a liquid hedging market and moderate realized volatility [[sources/pdf-f139d7bd1924]].
- Portfolio insurance strategies start with a short futures position; as the market rallies, the portfolio insurer covers the short, which likely contributed to the 39% YTD rally in the SPX before the August 1987 peak [[sources/pdf-f139d7bd1924]].
- As the market fell from late August 1987, portfolio insurers began selling; through the Friday before the crash the SPX had already fallen 16% [[sources/pdf-f139d7bd1924]].
- Two major institutional sellers using portfolio insurance dominated the selling on 10/19/1987 (Black Monday) — "it's very clear from their activities on 10/19 that they caused the extreme move that day" [[sources/pdf-f139d7bd1924]].
- "Portfolio insurance is by definition a deleveraging" [[sources/pdf-f139d7bd1924]].
- LOR Associates sold a product labeled "portfolio insurance" whose mechanism was to systematically sell assets when the market fell below a certain level, in order to exit positions quickly and prevent larger losses [[sources/pdf-04854302f962]].
- On paper the design sounded sensible, but when the product was adopted en masse it created a suction of liquidity by producing a profile of sellers that grossly outweighed buyers at the pre-set exit prices [[sources/pdf-04854302f962]].
- It is generally acknowledged that portfolio insurance was one of the reasons for the 1987 stock-market crash, when the market fell more than 20% in a single day [[sources/pdf-04854302f962]].
- Ambrus Capital argues that today's market structure has different participants and different titles, but the liquidity implications are eerily similar — price-insensitive gamma hedging is mechanically very similar to the LOR strategy in pulling liquidity when prices go down [[sources/pdf-04854302f962]].
- Per Constan, today's parallel: long-only investors lever and delever with futures, hedge via purchasing puts whose liquidity has massively improved, but this leaves dealers with "Portfolio Insurance" dynamic hedging to do in a downdraft — with circuit breakers (introduced based on Brady Commission recommendations) as the main structural difference from 1987 [[sources/pdf-f139d7bd1924]].
- The 2010 Flash Crash was also "a portfolio insurance strategy that broke its algo" — a severe reaction not dissimilar to the August 4–5, 2024 price action [[sources/pdf-f139d7bd1924]].

## Sources

- [[sources/pdf-04854302f962]]
- [[sources/pdf-f139d7bd1924]]

## Related

- [[concepts/gamma-reflexivity]]
- [[concepts/market-fragility]]
- [[concepts/deleveraging-framework]]
- [[entities/lor-associates]]
- [[entities/andrew-constan]]
- [[entities/brady-commission]]
