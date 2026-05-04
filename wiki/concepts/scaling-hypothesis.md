---
type: concept
slug: scaling-hypothesis
canonical_name: Scaling Hypothesis
domains:
  - ai-and-agents
---

# Scaling Hypothesis

## Summary

The hypothesis that "scaling is all you need" — that progressively training neural models on larger datasets and with more compute yields general-purpose intelligence; Belle and Marcus (AAAI-26) explicitly argue against this hypothesis and point to persistent challenges in reliable symbolic reasoning with deep and large models [[sources/pdf-vaishak-belle-2026-the-future-is]].

## Key claims

- The "scaling is all you need" framing is the question of whether scaling neural models to train over larger and larger datasets leads to general-purpose intelligence — i.e., whether scaling will eventually "hit a wall" in terms of model abilities (Marcus 2018, 2022; Chollet 2017) [[sources/pdf-vaishak-belle-2026-the-future-is]].
- Belle and Marcus (AAAI-26) explicitly argue against the scaling hypothesis, citing persistent challenges in reliable symbolic reasoning with deep and large models [[sources/pdf-vaishak-belle-2026-the-future-is]].
- Empirical work cited in support of the critique includes Valmeekam et al. (2022), which finds that LLMs' ability to reason about mathematical and symbolic truths is brittle and unreliable [[sources/pdf-vaishak-belle-2026-the-future-is]].
- The increasing use of symbolic systems such as code interpreters within LLM-based systems is itself a neuro-symbolic concession; Marcus (2025b) argues that this training regime is not always acknowledged, leading the wider community to believe LLM systems have powerful reasoning capabilities despite not having any inbuilt symbolic manipulation engines [[sources/pdf-vaishak-belle-2026-the-future-is]].
- The inability of stochastic learners to understand causal relationships, together with the tendency of large models to hallucinate (or, more accurately, confabulate), is cited as evidence that background expert-led knowledge is crucial for trustworthiness [[sources/pdf-vaishak-belle-2026-the-future-is]].

## Sources

- [[sources/pdf-vaishak-belle-2026-the-future-is]]

## Related

- [[entities/gary-marcus]]
- [[concepts/neuro-symbolic-ai]]
- [[concepts/distribution-drift]]
