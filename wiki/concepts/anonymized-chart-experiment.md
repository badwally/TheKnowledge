---
type: concept
slug: anonymized-chart-experiment
canonical_name: Anonymized chart experiment
domains:
  - trading-and-markets
---

# Anonymized chart experiment

## Summary

The anonymized chart experiment is the bias-free experimental setup designed by Zarattini and Stamatoudis (2024) to isolate the effect of trader intuition on overnight-gap trading: the discretionary trader sees only a two-year price-history chart with all identifying metadata stripped, and decisions must be made purely from visual price-pattern inspection [[sources/pdf-1662a4368954]].

## Key claims

- The experimental setup is designed to be unbiased by anonymizing charts and stripping away specific dates, ticker symbols, sectors, news, specific prices, and volumes [[sources/pdf-1662a4368954]].
- The sole basis for decision-making is the visual inspection of historical price behavior over a two-year price history, isolating the effect of trader intuition [[sources/pdf-1662a4368954]].
- The primary objective is to evaluate how a discretionary trader, uninfluenced by external information, performs in selecting trades purely from a price-pattern perspective [[sources/pdf-1662a4368954]].
- The trader's role within the setup is to restrict the algorithm to trade only those stocks whose daily charts appear more promising, allowing the experiment to measure the profitability improvement contributed by discretionary judgment [[sources/pdf-1662a4368954]].
- A separate micromanagement layer assesses the effect of position management — including precise entries, stop losses, and partial exits at predetermined intervals — also conducted in a bias-free environment by analyzing daily and intraday price action following the overnight gap [[sources/pdf-1662a4368954]].
- The setup is the methodological device through which the paper provides empirical evidence on intuition-driven trading's effectiveness without contamination by knowledge of company identity, headlines, or absolute price levels [[sources/pdf-1662a4368954]].

## Sources

- [[sources/pdf-1662a4368954]]

## Related

- [[concepts/trader-intuition]]
- [[concepts/discretionary-vs-algorithmic-trading]]
- [[concepts/trade-micromanagement]]
- [[concepts/overnight-gap]]
