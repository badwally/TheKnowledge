---
type: concept
slug: ann-earnings-prediction
canonical_name: ANN Earnings Prediction
domains:
  - trading-and-markets
---

# ANN Earnings Prediction

## Summary

An artificial neural network trained specifically to predict the direction of future earnings using a panel of financial-statement variables; in Kim, Muhn, and Nikolaev (2024) it serves as the state-of-the-art specialized-ML benchmark against which GPT-4 financial statement analysis is compared [[sources/pdf-2329b8b436f2]].

## Key claims

- The ANN benchmark uses the same 59 financial-statement predictors as the Ou-and-Penman (1989) stepwise logistic regression but additionally leverages non-linearities and interactions among them [[sources/pdf-2329b8b436f2]].
- The paper trains the model each year on five years of historical Compustat data; all forecasts are out of sample [[sources/pdf-2329b8b436f2]].
- A second ANN variant is trained on the restricted information set of only income-statement and balance-sheet items — the same data passed to GPT — to ensure consistency between the two model classes [[sources/pdf-2329b8b436f2]].
- On the Compustat sample, the full-feature ANN achieves 60.45% accuracy and an F1-score of 61.62, in the range of state-of-the-art earnings prediction models [[sources/pdf-2329b8b436f2]].
- The ANN dominates the stepwise logistic regression (52.94% accuracy, 57.23% F1) and is on par with GPT-4 Turbo chain-of-thought predictions [[sources/pdf-2329b8b436f2]].
- A specialized ANN's training advantage — learning deep interactions and important cues a general-purpose LLM cannot easily gather — would normally place an LLM at a serious disadvantage in this comparison; the paper's finding that GPT matches the ANN is therefore a stronger result than beating analysts alone [[sources/pdf-2329b8b436f2]].

## Sources

- [[sources/pdf-2329b8b436f2]]

## Related

- [[concepts/llm-financial-statement-analysis]]
- [[concepts/direction-of-earnings-changes-prediction]]
