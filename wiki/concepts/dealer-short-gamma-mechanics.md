---
schema_version: 1
type: concept
slug: dealer-short-gamma-mechanics
canonical_name: Dealer short-gamma mechanics
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Dealer short-gamma mechanics

## Summary

When option dealers are net short gamma at the current underlying price, their delta exposure shifts rapidly as the underlying moves — so they must buy into rallies and sell into drops, mechanically reinforcing volatility rather than dampening it [[sources/pdf-ea646c451aae]].

## Key claims

- When dealers are short gamma at current price, they must buy into rallies and sell into drops, reinforcing volatility [[sources/pdf-ea646c451aae]].
- Because dealers are already short gamma, their delta exposure shifts rapidly as the underlying rises, forcing them to buy more futures as price moves up and accelerating the rally [[sources/pdf-ea646c451aae]].
- The hedging behavior is self-reinforcing — dealer trades create the price move that triggers further dealer hedging in the same direction [[sources/pdf-ea646c451aae]].
- The framing is described as "a classic dealer hedging-driven price action setup, where dealer positioning and gamma dynamics create a self-reinforcing move into expiration" [[sources/pdf-ea646c451aae]].

## Sources

- [[sources/pdf-ea646c451aae]]

## Related

- [[concepts/gamma-squeeze-into-close]]
- [[concepts/iron-condor-dealer-positioning]]
- [[concepts/pinning-at-strike-expiration]]
- [[concepts/blow-off-top-into-close]]
