---
type: concept
slug: all-in-all-out-strategy
canonical_name: All-in / all-out strategy
domains:
  - trading-and-markets
---

# All-in / all-out strategy

## Summary

An all-in / all-out strategy is a trading rule in which the investor's entire wealth is at any time fully invested in the stock or fully in a risk-free bank account, with no fractional positions; Dai, Yang, Zhang, and Zhu (2015) take this restriction as the strategy class within which they prove the optimality of trend-following in a bull-bear switching market [[sources/pdf-05df32dcb03e]].

## Key claims

- Under an all-in / all-out strategy the investor is either long — entire wealth invested in the stock — or flat — all wealth in a bank account drawing the risk-free rate; this binary state is the only choice variable [[sources/pdf-05df32dcb03e]].
- When buying, the investor fills the position with the entire account balance; when selling, the investor closes the entire position [[sources/pdf-05df32dcb03e]].
- A moving-average trading strategy is generally in all-in / all-out form but is difficult to justify theoretically; designing and justifying an alternative all-in / all-out strategy with rigorous mathematical analysis is the explicit motivation for Dai et al.'s work [[sources/pdf-05df32dcb03e]].
- This is a relaxation of the more restrictive Dai et al. [5] companion paper, which allowed only a single share to be traded over time and therefore yielded a wealth process that is not self-financing [[sources/pdf-05df32dcb03e]].
- The reward function in the all-in / all-out setup accounts for the percentage gain or loss of each trade — desirable in actual trading — and between trades the entire balance earns the risk-free interest rate ρ [[sources/pdf-05df32dcb03e]].
- All long positions must be liquidated at the terminal time T; transactions at t > T do not affect the payoff, signified by the indicator I_{τ_n < T} in the reward function [[sources/pdf-05df32dcb03e]].
- Chen et al. [1] subsequently extended this work to a Merton-style portfolio optimization problem in which the investor may choose an optimal fraction of wealth invested in the stock [[sources/pdf-05df32dcb03e]].

## Sources

- [[sources/pdf-05df32dcb03e]]

## Related

- [[concepts/trend-following-trading-rule]]
- [[concepts/bull-bear-switching-model]]
- [[concepts/contra-trend-strategy]]
