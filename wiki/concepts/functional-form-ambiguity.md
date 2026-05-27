---
schema_version: 1
type: concept
slug: functional-form-ambiguity
canonical_name: Functional Form Ambiguity in Finance
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Functional Form Ambiguity in Finance

## Summary

Observation, central to Kelly and Xiu's 2023 financial-machine-learning survey, that the Euler equation underlying asset pricing is broad enough to accommodate many structural forms — and since no consensus exists on which structural formulation is viable, empirical research benefits from the flexible, nonparametric tools of machine learning [[sources/pdf-e2068d89c2a7]].

## Key claims

- The traditional econometric approach (e.g., Hansen and Singleton, 1982) first specifies a functional form for a return-forecasting model motivated by a theoretical economic model, then estimates parameters within the confines of that chosen model [[sources/pdf-e2068d89c2a7]].
- The Euler equation P = E[M X | I] is broad enough to encompass a wide variety of structural economic assumptions, and "this generality is warranted because there is no consensus about which specific structural formulations are viable" [[sources/pdf-e2068d89c2a7]].
- Early consumption-based models fail to match market price data by most measures (e.g., Mehra and Prescott, 1985) [[sources/pdf-e2068d89c2a7]].
- Modern structural models match price data somewhat better if the measure of success is sufficiently forgiving (e.g., Chen et al., 2022a), but the scope of phenomena they describe tends to be limited to a few assets and is typically evaluated only on an in-sample basis [[sources/pdf-e2068d89c2a7]].
- Most empirical work in the last two decades has opted away from structural assumptions to less rigid "reduced-form" or "no-arbitrage" frameworks, but these typically still impose statistical structure (e.g., low-dimensional factor models or other parametric assumptions) [[sources/pdf-e2068d89c2a7]].
- Kelly and Xiu argue it is worth exploring the benefits of flexible models that can accommodate many different functional forms and varying degrees of nonlinearity and variable interactions — and that "machine learning methods are explicitly designed to approximate unknown data generating functions" [[sources/pdf-e2068d89c2a7]].
- They argue that just as researchers should be circumspect in their consideration of conditioning information, they must be "equally circumspect in [their] consideration of functional forms" because investors use information in ways that researchers cannot know explicitly and thus cannot exhaustively specify in a parametric statistical model [[sources/pdf-e2068d89c2a7]].

## Sources

- [[sources/pdf-e2068d89c2a7]]

## Related

- [[concepts/prices-are-predictions]]
- [[concepts/large-conditioning-information-sets]]
- [[concepts/financial-machine-learning-definition]]
- [[entities/bryan-kelly]]
- [[entities/dacheng-xiu]]
