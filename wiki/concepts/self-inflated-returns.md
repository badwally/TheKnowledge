---
schema_version: 1
type: concept
slug: self-inflated-returns
canonical_name: Self-inflated returns
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Self-inflated returns

## Summary

Self-inflated returns are the component of an active fund's realized returns driven by the fund's own price impact on its underlying holdings, as opposed to fundamental information; introduced and operationalized by van der Beck, Bouchaud, and Villamaina (2024) as the central object in their decomposition of fund returns [[sources/pdf-806192f007eb]].

## Key claims

- Self-inflated returns are given analytically by fund flows interacted with fund illiquidity, scaled by price impact [[sources/pdf-806192f007eb]].
- The paper decomposes fund returns into a price-pressure (self-inflated) component and a fundamental component, and shows that investors are unable to identify whether realized returns are self-inflated or fundamental [[sources/pdf-806192f007eb]].
- Self-inflated returns explain about 8% of the time-series variation in returns for funds that are both large and hold concentrated portfolios; their importance in explaining overall fund returns increases monotonically in both portfolio size and concentration [[sources/pdf-806192f007eb]].
- Self-inflated returns are realized returns to earlier investors in the affected securities, so when later investors chase them they trigger further price pressure and an endogenous capital reallocation from late to early investors [[sources/pdf-806192f007eb]].
- The capital reallocation from self-inflated returns unravels once the price impact in the underlying securities reverts and investors stop misinterpreting self-inflated returns as managerial skill [[sources/pdf-806192f007eb]].
- The paper's title "Ponzi Funds" refers to this self-inflated mechanism, not to the SEC's definition of a Ponzi scheme as investment fraud — the wealth transfer happens indirectly via observable market prices, not direct capital transfers [[sources/pdf-806192f007eb]].

## Sources

- [[sources/pdf-806192f007eb]] — Ponzi Funds (van der Beck, Bouchaud, Villamaina 2024)

## Related

- [[concepts/fund-illiquidity]]
- [[concepts/ponzi-flows]]
- [[concepts/flow-induced-price-impact]]
- [[concepts/endogenous-price-spiral]]
- [[concepts/flow-performance-relationship]]
- [[entities/philippe-van-der-beck]]
