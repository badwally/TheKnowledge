---
type: concept
slug: winner-takes-all-microstructure
canonical_name: Winner-Takes-All Microstructure
domains:
  - trading-and-markets
---

# Winner-Takes-All Microstructure

## Summary

The empirical pattern observed in exchange order books during major information releases where a small number of large aggressor orders — arriving within microseconds of each other — sweep all resting limit orders in the book, followed by a long lull in activity until a new equilibrium is reached; described by Zaatour and Tyč as a "very good example of the winner takes all game" in their analysis of trading immediately after the September 18, 2013 FOMC "no taper" announcement [[sources/pdf-fa83c61dfa2d]].

## Key claims

- On Nasdaq GLD, most trading activity after the September 18, 2013 FOMC announcement occurred on a single nanosecond timestamp (14:00:00.000330613), with a large cumulated volume and a 0.91% price increase from 126.83 to 127.98 [[sources/pdf-fa83c61dfa2d]].
- Subsequent GLD trades took place only more than 160 ms later, with negligible cumulated impact on price — consistent with the first few aggressors capturing all available resting liquidity [[sources/pdf-fa83c61dfa2d]].
- All initial GLD trades were probably spawned by a small number of large aggressor orders with a highest limit price of 127.98, sweeping all resting orders in the book [[sources/pdf-fa83c61dfa2d]].
- The paper notes there were "probably many more trying to buy at almost the same time but only the first few executed their trades" [[sources/pdf-fa83c61dfa2d]].
- After the initial matching events there was a lull in GLD activity lasting up to 3 seconds before a new equilibrium was reached [[sources/pdf-fa83c61dfa2d]].
- On Nasdaq SPY, 155 trades were timestamped at 14:00:00.000390009 with a cumulated volume of 60,726 and a 0.39% price increase, followed by subsequent trades only after more than 10 ms [[sources/pdf-fa83c61dfa2d]].
- On CME Gold futures (GCZ3), the first 20 trades timestamped 1 ms after 2:00 pm caused a price increase from 1313.5 to 1316.8; on E-mini futures (ESZ3), 104 trades timestamped 2 ms after 2:00 pm caused the price to increase from 1695.75 to 1696.50 [[sources/pdf-fa83c61dfa2d]].
- Regarding the volume and impact of these trades, they are "clearly motivated by the no-taper information" — confirming that the information was received by the submitting servers before 2:00 pm + 330 microseconds [[sources/pdf-fa83c61dfa2d]].
- The pattern implies a single-shot competition among algorithmic traders: the fastest to parse the news and submit orders captures the resting book, while slower participants arrive to an empty book and must wait for a new equilibrium [[sources/pdf-fa83c61dfa2d]].

## Sources

- [[sources/pdf-fa83c61dfa2d]]

## Related

- [[entities/quincy-data]]
- [[concepts/fomc-news-release-mechanism]]
- [[concepts/speed-of-light-latency-constraint]]
