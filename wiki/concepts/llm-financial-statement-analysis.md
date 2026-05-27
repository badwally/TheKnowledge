---
schema_version: 1
type: concept
slug: llm-financial-statement-analysis
canonical_name: LLM Financial Statement Analysis
domains:
- trading-and-markets
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# LLM Financial Statement Analysis

## Summary

The use of a general-purpose large language model — without fine-tuning, narrative context, or industry-specific training — to analyze standardized balance sheets and income statements and produce predictions about a firm's future earnings direction. Kim, Muhn, and Nikolaev (2024) probe this capability with GPT-4 Turbo and find that, when guided by a chain-of-thought prompt that emulates human financial analysts, the LLM dominates median analyst forecasts and matches a specialized ANN [[sources/pdf-2329b8b436f2]].

## Key claims

- The research design passes a balance sheet and income statement in standardized form to GPT-4 Turbo and asks the model to determine whether earnings will grow or decline in the following period [[sources/pdf-2329b8b436f2]].
- The design deliberately withholds textual information (e.g., Management Discussion and Analysis) to isolate the LLM's ability to analyze and synthesize purely financial numbers [[sources/pdf-2329b8b436f2]].
- A "simple" non-CoT prompt yields GPT prediction accuracy of 52%, lower than first-month analyst forecasts (53%) [[sources/pdf-2329b8b436f2]].
- A chain-of-thought prompt that instructs the model to identify trends, compute key ratios (operating efficiency, liquidity, leverage), synthesize the information, and form expectations raises GPT accuracy to 60% — comfortably dominating the median financial analyst [[sources/pdf-2329b8b436f2]].
- This 60% accuracy is in the range of state-of-the-art earnings prediction models, including a specialized artificial neural network trained on 59 financial-statement predictors [[sources/pdf-2329b8b436f2]].
- LLM prediction does not stem from training memory; instead the LLM generates useful narrative insights about a company's future performance [[sources/pdf-2329b8b436f2]].
- The LLM exhibits a relative advantage over human analysts in situations where analysts tend to struggle, including instances where human forecasts are prone to bias or do not incorporate information rationally [[sources/pdf-2329b8b436f2]].
- Human analysts retain incremental value because their forecasts contain useful soft information about future performance not captured by GPT [[sources/pdf-2329b8b436f2]].
- Trading strategies based on GPT predictions yield higher Sharpe ratios and alphas than strategies based on the other models in the paper's comparison [[sources/pdf-2329b8b436f2]].

## Sources

- [[sources/pdf-2329b8b436f2]]

## Related

- [[entities/alex-kim]]
- [[entities/maximilian-muhn]]
- [[entities/valeri-nikolaev]]
- [[entities/gpt-4-turbo]]
- [[concepts/chain-of-thought-prompting-finance]]
- [[concepts/direction-of-earnings-changes-prediction]]
- [[concepts/anonymized-financial-statements]]
- [[concepts/ann-earnings-prediction]]
