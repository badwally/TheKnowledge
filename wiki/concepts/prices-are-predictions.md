---
schema_version: 1
type: concept
slug: prices-are-predictions
canonical_name: Prices Are Predictions
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Prices Are Predictions

## Summary

Framing, central to Kelly and Xiu's 2023 financial-machine-learning survey, that the prevailing price of any asset is, by construction, a prediction of its discounted future payoffs — and therefore that the statistical tools to study prices are forecasting models [[sources/pdf-e2068d89c2a7]].

## Key claims

- The modern analysis of financial markets centers on the Euler equation P_{i,t} = E[M_{t+1} X_{i,t+1} | I_t], derived from the generic optimality condition of an investor [[sources/pdf-e2068d89c2a7]].
- In words, the prevailing price of an asset reflects investors' valuation of its future payoffs, discounted by their preferences (summarized as future realized marginal rates of substitution) and conditioned on their information set [[sources/pdf-e2068d89c2a7]].
- "Prices are predictions—they reflect investors' best guesses for the (discounted) future payoffs shed by an asset" [[sources/pdf-e2068d89c2a7]].
- Because prices are predictions, the statistical tools to study prices are forecasting models, which makes machine learning a natural fit for the research program [[sources/pdf-e2068d89c2a7]].
- The price equation has an equivalent expected-return ("discount rate") representation E[R_{i,t+1} | I_t] = β_{i,t} λ_t, normalized by the time-t price [[sources/pdf-e2068d89c2a7]].
- The literature typically opts for the discount-rate representation because prices are often non-stationary while discount rates are often stationary, and uninteresting payoff-scale differences carry into prices but not into discount rates [[sources/pdf-e2068d89c2a7]].
- The expected return is described as a critical input to allocation decisions: "If we manage to isolate an empirical model for this expectation that closely fits the data, we have achieved a better understanding of market functionality and simultaneously derived a tool to improve resource allocations going forward" [[sources/pdf-e2068d89c2a7]].
- Kelly and Xiu describe this duality as "a fine example of duality in applied social science research: A good model both elevates scientific understanding and improves real-world decision-making" [[sources/pdf-e2068d89c2a7]].

## Sources

- [[sources/pdf-e2068d89c2a7]]

## Related

- [[concepts/large-conditioning-information-sets]]
- [[concepts/functional-form-ambiguity]]
- [[concepts/financial-machine-learning-definition]]
- [[entities/bryan-kelly]]
- [[entities/dacheng-xiu]]
