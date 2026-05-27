---
schema_version: 1
type: concept
slug: macroscopic-dynamics-of-llms
canonical_name: Macroscopic dynamics theory of LLM-driven agents
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Macroscopic dynamics theory of LLM-driven agents

## Summary

A research program articulated by Song, Cao, Luo, and Zhu (2026) to elevate the study of LLM-driven agents from a collection of engineering practices to a predictable, quantifiable science by treating coarse-grained agent states as the unit of dynamics and identifying physics-style universal laws — such as detailed balance — that hold independently of model and prompt details [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].

## Key claims

- Existing theoretical understanding of LLMs operates largely at the level of token statistical properties and microscopic generative mechanisms, which makes it difficult to explain the macroscopic dynamics of LLMs as complex systems [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The behavior of LLM-driven agents is often viewed as a direct product of complex internal engineering — prompt templates, memory modules, tool calls — leaving their dynamic characteristics a black box [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The paper proposes a coarse-grained "agent-level" description in which the LLM is treated as a Markov transition kernel between standardized agent states (task objectives, historical summaries, code, file systems, API return values, etc.) [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The agent-level description is positioned as a physics-style approach: discover macroscopic laws that "transcend different LLM architectures and prompt templates" and hold despite the diversity of underlying engineering [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The stated aim is to establish "a macroscopic dynamics theory of complex AI systems" built on "effective measurements that are predictable and quantifiable," elevating AI agents from a collection of engineering practices to a quantitative science [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The first concrete instance of such a law in this program is the empirical observation that LLM-generated state transitions satisfy detailed balance at the agent level, with the corresponding underlying potential function recoverable via a least-action principle [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The framing is contrasted with two limit cases: traditional rule-based programs (deterministic) and naive random search (unstructured); LLM generation is described as a hybrid dynamics between random search and deterministic planning that nonetheless admits an equilibrium-style description at the agent level [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].

## Sources

- [[sources/pdf-zhuo-yang-2026-detailed-balance-in]]

## Related

- [[concepts/detailed-balance-in-llm-agents]]
- [[concepts/least-action-principle-llm]]
- [[concepts/potential-function-llm]]
- [[concepts/agentic-ai]]
