---
type: concept
slug: opening-range-breakout-strategy
canonical_name: Opening Range Breakout (ORB) Strategy
domains:
  - trading-and-markets
---

# Opening Range Breakout (ORB) Strategy

## Summary

A day-trading strategy that bets on a directional breakout from the price range established during the first n minutes of the trading session. In its 5-minute, simplified form — used by Zarattini and Aziz (2023) on QQQ — the trader enters at the open of the second 5-minute candle in the same direction as the first candle, places the stop at the opposite extreme of the first candle (defining `$R`), and targets either 10R or end-of-day (whichever comes first); over January 1, 2016 to February 17, 2023 this implementation produced an annualized alpha of 33% net of commissions versus a passive QQQ benchmark [[sources/pdf-e63407c2b4f4]].

## Key claims

- The n-minute ORB strategy involves identifying the high and low of a stock during the first n minutes of trading and then buying or selling when the stock breaks out of this range [[sources/pdf-e63407c2b4f4]].
- A more simplistic version of the strategy can be obtained by buying or selling at the open of the second candle in the same direction as the first n-minute candle [[sources/pdf-e63407c2b4f4]].
- In Zarattini and Aziz's 5-minute QQQ implementation: if the first 5-minute candle is up, take a long position at the second candle's open; if down, take a short position; if a doji (open ~ close), no position [[sources/pdf-e63407c2b4f4]].
- The stop loss is placed at the low of the first 5-minute candle for a long trade, and at the high of the first 5-minute candle for a short trade; the distance between entry price and stop is labeled `$R` [[sources/pdf-e63407c2b4f4]].
- The profit target is set at 10R; if not reached by end of day, the position is liquidated at market close [[sources/pdf-e63407c2b4f4]].
- Trade size is calibrated such that hitting the stop loses 1% of capital, with the share count formula `Shares = integer(min(A·0.01/$R, 4·A/P))`, where `A` is account size, `$R` is risk per share, and `P` is the entry price [[sources/pdf-e63407c2b4f4]].
- Over the period January 1, 2016 to February 17, 2023, an ORB QQQ portfolio starting at $25,000 grew to $192,806 net of commissions — a total return of 675% — versus the QQQ benchmark at $67,307 (169% total return) [[sources/pdf-e63407c2b4f4]].
- Daily-returns regression `Ret_ORB_QQQ = α + β·Ret_QQQ` produced annualized alpha of 33% (p-value 0.0025), with beta not statistically different from zero — the strategy is essentially uncorrelated with passive QQQ exposure [[sources/pdf-e63407c2b4f4]].
- Annualized Sharpe Ratio was 1.12 and annualized rate of return was 31% [[sources/pdf-e63407c2b4f4]].
- Out of 1,795 trades, 51% were long and 49% were short — the rough symmetry is what drove the near-zero beta [[sources/pdf-e63407c2b4f4]].
- Win rate was 24%, average PnL per trade was 0.13R; low accuracy was compensated by asymmetry between gains (capped at 10R) and losses (capped at –1R, slightly worse due to commissions) [[sources/pdf-e63407c2b4f4]].
- The authors deliberately did not optimize parameters; the goal was empirical comparison with a simple buy-and-hold benchmark, not a high-performance trading algorithm [[sources/pdf-e63407c2b4f4]].

## Sources

- [[sources/pdf-e63407c2b4f4]]

## Related

- [[entities/carlo-zarattini]]
- [[entities/andrew-aziz]]
- [[concepts/leveraged-etf-amplification]]
- [[concepts/intraday-leverage-constraint]]
- [[concepts/asymmetric-risk-reward-ratio]]
