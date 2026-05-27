---
schema_version: 1
type: concept
slug: contra-trend-strategy
canonical_name: Contra-trend strategy
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Contra-trend strategy

## Summary

A contra-trend strategy is a trading rule that bets on mean reversion — buying when price falls to a low level and selling when it rebounds; it is the foil against which Dai, Yang, Zhang, and Zhu (2015) define trend-following, and arises endogenously from utility maximization under standard assumptions about the price process [[sources/pdf-05df32dcb03e]].

## Key claims

- A contra-trend trader purchases a stock when its price falls to some low level and bets on an eventual rebound, taking advantage of mean-reversion-type market behaviors [[sources/pdf-05df32dcb03e]].
- There is an extensive literature devoted to contra-trend strategies; Merton (1969) pioneered continuous-time portfolio selection with utility maximization, and the framework was subsequently extended to incorporate transaction costs by Magil and Constantinidies (1976), Davis and Norman (1990), Shreve and Soner (1994), Liu and Loewenstein (2002), Dai and Yi (2009), and others [[sources/pdf-05df32dcb03e]].
- Assuming no leverage or short selling, the resulting strategies turn out to be contra-trend because the investor is risk averse and the stock market is assumed to follow a geometric Brownian motion with constant drift and volatility — a setting without regime change [[sources/pdf-05df32dcb03e]].
- Zhang and Zhang (2008) showed that the optimal trading strategy in a mean-reverting market is also contra-trend; other work in this line includes Dai et al. [2], Song et al. [18], and Zervors et al. [20] [[sources/pdf-05df32dcb03e]].
- The bull-bear regime-switching market that motivates trend-following is incompatible with the constant-drift geometric Brownian motion assumed in the contra-trend literature — different price dynamics, different optimal rule [[sources/pdf-05df32dcb03e]].

## Sources

- [[sources/pdf-05df32dcb03e]]

## Related

- [[concepts/trend-following-trading-rule]]
- [[concepts/bull-bear-switching-model]]
