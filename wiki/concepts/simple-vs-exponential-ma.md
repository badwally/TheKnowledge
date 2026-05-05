---
type: concept
slug: simple-vs-exponential-ma
canonical_name: Simple vs. Exponential Moving Averages
domains:
  - trading-and-markets
---

# Simple vs. Exponential Moving Averages

## Summary

The two principal flavors of moving average — simple (a straight average of closing prices over the window) and exponential (a weighted average that gives recent prices more weight) — produce visually similar lines, but the exponential variant tracks recent price action more closely and so gives a slightly faster read on near-term trend, which is why Scott Redler uses EMAs throughout his trading framework [[sources/pdf-a0072c763cf8]].

## Key claims

- A simple moving average is a straight average of the stock price over the specified window [[sources/pdf-a0072c763cf8]].
- An exponential moving average gives recent prices a bigger weight, so it does a better job of measuring recent momentum [[sources/pdf-a0072c763cf8]].
- On NVDA, the 50 day SMA (blue) and 50 day EMA (pink) plot close together, but the EMA is a bit closer to the current price [[sources/pdf-a0072c763cf8]].
- Redler uses exponential moving averages because they are more sensitive to recent action and give a slightly better read on the near-term trend [[sources/pdf-a0072c763cf8]].
- All moving averages in Redler's eBook from page 9 onward are exponential — he treats the EMA as the default and the SMA as an alternative he has tested but does not use [[sources/pdf-a0072c763cf8]].
- A daily moving average is the average of a stock's daily closing prices over a specified number of days; it is called "moving" because every day the newest closing price replaces the oldest [[sources/pdf-a0072c763cf8]].

## Sources

- [[sources/pdf-a0072c763cf8]]

## Related

- [[entities/scott-redler]]
- [[concepts/8-21-day-ema-roadmap]]
- [[concepts/moving-average-as-roadmap]]
