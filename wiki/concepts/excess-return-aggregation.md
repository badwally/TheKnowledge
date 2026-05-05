---
type: concept
slug: excess-return-aggregation
canonical_name: Excess Return Aggregation in Multi-Manager Funds
domains:
  - trading-and-markets
---

# Excess Return Aggregation in Multi-Manager Funds

## Summary

The accounting identity that decomposes a multi-manager fund's total return into the sum of the excess returns of its constituent strategies plus the risk-free return — explaining why a fund holding the combined positions of two strategies returns less than the simple sum of their total returns, because cash earns interest only once [[sources/pdf-7663c24d3159]].

## Key claims

- Excess return is defined as the return earned above the risk-free return (generally considered to be the return of short-term Treasury bills); specifically, the excess returns are the returns earned from the trading P&L of the strategies within the fund [[sources/pdf-7663c24d3159]].
- For ClearAlpha's worked example, excess returns are the trading P&L minus the commissions and financing costs in the case where all trading strategies within a fund are fully funded — i.e., incur the costs of financing the positions the strategies hold [[sources/pdf-7663c24d3159]].
- Using 3% as the interest earned on short-term Treasury bills as the risk-free rate, Fund A (8% total) has 5% excess return and Fund B (10% total) has 7% excess return [[sources/pdf-7663c24d3159]].
- The multi-manager fund holding the combined positions of Funds A and B earns 15% total = 5% + 7% + 3% — the sum of the two excess returns plus the risk-free interest rate, not the 18% naive sum of total returns [[sources/pdf-7663c24d3159]].
- Each fund earns interest only once: holding the sum of the positions of two underlying funds does not let the multi-manager fund earn interest on its cash twice [[sources/pdf-7663c24d3159]].

## Sources

- [[sources/pdf-7663c24d3159]]

## Related

- [[concepts/multi-manager-fund]]
- [[concepts/cash-efficient-implementation]]
