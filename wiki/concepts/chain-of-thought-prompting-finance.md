---
schema_version: 1
type: concept
slug: chain-of-thought-prompting-finance
canonical_name: Chain-of-Thought Prompting for Financial Analysis
domains:
- trading-and-markets
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Chain-of-Thought Prompting for Financial Analysis

## Summary

A prompting technique in which an LLM is instructed to follow the same step-by-step reasoning a financial analyst would apply — identifying trends, computing key ratios, synthesizing the information, and forming expectations — before delivering a final earnings prediction. In Kim, Muhn, and Nikolaev (2024), this prompt is the difference between GPT-4 Turbo underperforming analysts and decisively beating them [[sources/pdf-2329b8b436f2]].

## Key claims

- Chain-of-thought prompts are known to enhance a model's problem-solving capability and induce human-like reasoning (Wei et al. 2022); the paper applies this technique to financial statement analysis [[sources/pdf-2329b8b436f2]].
- The CoT prompt implements the analyst thought process by instructing the model to identify notable trends in financial-statement line items, compute key financial ratios (operating efficiency, liquidity, leverage), synthesize the information, and form expectations about future earnings [[sources/pdf-2329b8b436f2]].
- The structure follows the analyst process described in Bouwman et al. (1987), ultimately making a determination of whether next year's earnings will increase or decrease compared to the current year [[sources/pdf-2329b8b436f2]].
- A simple non-CoT prompt yields GPT-4 Turbo accuracy of 52% on direction-of-earnings prediction, below human analyst forecasts at 53% [[sources/pdf-2329b8b436f2]].
- Switching to the CoT prompt raises GPT-4 Turbo accuracy to 60%, which the paper says "comfortably dominates" the performance of the median financial analyst [[sources/pdf-2329b8b436f2]].
- The CoT performance is on par with a specialized ANN earnings-prediction model trained on the same information set (income statement and balance sheet) [[sources/pdf-2329b8b436f2]].

## Sources

- [[sources/pdf-2329b8b436f2]]

## Related

- [[concepts/llm-financial-statement-analysis]]
- [[concepts/direction-of-earnings-changes-prediction]]
- [[entities/gpt-4-turbo]]
- [[entities/alex-kim]]
