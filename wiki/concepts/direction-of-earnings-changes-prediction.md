---
schema_version: 1
type: concept
slug: direction-of-earnings-changes-prediction
canonical_name: Direction-of-Earnings-Changes Prediction
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Direction-of-Earnings-Changes Prediction

## Summary

A binary forecasting task — will next-period earnings increase or decrease relative to the current period — used as a benchmark for comparing financial-statement analysis methods including human analysts, logistic regression, artificial neural networks, and large language models [[sources/pdf-2329b8b436f2]].

## Key claims

- Predicting changes in EPS is a highly complex task because the EPS time series is approximated by a random walk and contains a large unpredictable component [[sources/pdf-2329b8b436f2]].
- Focusing on direction provides a specific and measurable objective consistent with prior literature (Ou and Penman 1989; Chen et al. 2022); the binary framing is also motivated by Kahneman's observation that most key human decisions are binary [[sources/pdf-2329b8b436f2]].
- A naive model that extrapolates the prior year's change achieves 49% accuracy on the task [[sources/pdf-2329b8b436f2]].
- First-month analyst consensus forecasts achieve 53% accuracy, dominating the naive baseline (Bradshaw et al. 2012) [[sources/pdf-2329b8b436f2]].
- Three-month and six-month-ahead consensus forecasts achieve 56% and 57% accuracy respectively, reflecting the additional information acquired during the year — though those benchmarks disadvantage the LLM by incorporating later information [[sources/pdf-2329b8b436f2]].
- Stepwise logistic regression with 59 predictors (Ou and Penman 1989) achieves 52.94% accuracy and 57.23% F1-score on the entire Compustat sample, on par with human analysts [[sources/pdf-2329b8b436f2]].
- An artificial neural network trained on the same 59 predictors achieves 60.45% accuracy and 61.62 F1-score, in the range of state-of-the-art earnings prediction models [[sources/pdf-2329b8b436f2]].
- GPT-4 Turbo with chain-of-thought prompting achieves 60% accuracy, comfortably dominating median analyst forecasts and matching the specialized ANN [[sources/pdf-2329b8b436f2]].

## Sources

- [[sources/pdf-2329b8b436f2]]

## Related

- [[concepts/llm-financial-statement-analysis]]
- [[concepts/chain-of-thought-prompting-finance]]
- [[concepts/ann-earnings-prediction]]
- [[concepts/anonymized-financial-statements]]
