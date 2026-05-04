---
type: entity
slug: gpt-4-turbo
canonical_name: GPT-4 Turbo
entity_kind: organization
domains:
  - trading-and-markets
  - ai-and-agents
---

# GPT-4 Turbo

## Summary

OpenAI large language model used by Kim, Muhn, and Nikolaev (2024) as the test subject for whether a general-purpose LLM can perform financial statement analysis comparable to a professional human analyst; with a chain-of-thought prompt, GPT-4 Turbo achieves 60% accuracy at predicting direction of next-period earnings — surpassing the median analyst and matching a specialized ANN [[sources/pdf-2329b8b436f2]].

## Key facts

- Identified by the paper as "the large language model, GPT 4.0 Turbo," to which standardized balance sheets and income statements are passed for analysis [[sources/pdf-2329b8b436f2]].
- With a "simple" non-CoT prompt, GPT-4 Turbo achieves 52% accuracy on direction-of-earnings prediction, below the 53% accuracy of first-month analyst consensus forecasts [[sources/pdf-2329b8b436f2]].
- With a chain-of-thought prompt that emulates human analyst reasoning, GPT-4 Turbo achieves 60% accuracy — comfortably dominating median analyst performance [[sources/pdf-2329b8b436f2]].
- The model's predictive performance does not stem from training memory; the paper's anonymization design rules this out, and the model instead generates useful narrative insights about a company's future performance [[sources/pdf-2329b8b436f2]].
- A Companion App built on GPT-4 Turbo for the paper requires a ChatGPT Plus subscription and uses a different prompt that integrates narrative context while processing 10-Ks and 10-Qs step-by-step [[sources/pdf-2329b8b436f2]].
- The paper warns that the Companion App version is more prone to retrieval errors and that the accuracy of information must be verified [[sources/pdf-2329b8b436f2]].

## Sources

- [[sources/pdf-2329b8b436f2]]

## Related

- [[concepts/llm-financial-statement-analysis]]
- [[concepts/chain-of-thought-prompting-finance]]
- [[concepts/anonymized-financial-statements]]
- [[entities/alex-kim]]
- [[entities/maximilian-muhn]]
- [[entities/valeri-nikolaev]]
