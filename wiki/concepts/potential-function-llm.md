---
schema_version: 1
type: concept
slug: potential-function-llm
canonical_name: LLM agent potential function (V_T)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# LLM agent potential function (V_T)

## Summary

In Song et al. (2026)'s framework, V_T : C → ℝ is a scalar-valued potential function over an LLM-driven agent's state space C that quantifies each state's "quality" — informally "how far the LLM perceives it to be from the goal" — and whose ordering organizes the LLM's preferred transitions, providing a global cognitive map for the agent that the authors hypothesize the LLM has implicitly learned [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].

## Key claims

- V_T is hypothesized because LLM-driven agents' state transitions are not entirely random but exhibit a structured preference: agents tend to transition from the current state f to states g that are "better" from the agent's perspective [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- V_T informally evaluates the intrinsic properties of any given state, such as "how far the LLM perceives it to be from the goal," giving the agent a global awareness that lets it converge to optimal states and effectively avoid repetitive cycles in state space [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The paper's central hypothesis is that LLMs implicitly learn V_T for specific tasks within their vast parameter space, rather than memorizing specific rule sets and strategies — which the authors argue would explain the stronger generalization observed compared with mere strategy-set learning [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- V_T can be estimated empirically: in Claude-4 and Gemini-2.5-flash, the variational condition can be solved analytically; for Claude-4 the transition process can be plotted ordered by V_T, with transitions tending to move toward states of lower potential [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- States with β V_T(f) > log(20,000) ≈ 10 in the Conditioned Word Generation experiment are precisely those where the equilibrium condition cannot be strictly satisfied within 20,000 samples, providing a sample-size-aware notion of which V_T values are reliably estimated [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].
- The authors interpret the same V_T as potentially transcending different LLM architectures and prompt templates — i.e., the same task is described by the same underlying potential regardless of the model implementing it — though this is presented as an empirical conjecture motivated by the cross-model observation of detailed balance [[sources/pdf-zhuo-yang-2026-detailed-balance-in]].

## Sources

- [[sources/pdf-zhuo-yang-2026-detailed-balance-in]]

## Related

- [[concepts/detailed-balance-in-llm-agents]]
- [[concepts/least-action-principle-llm]]
- [[concepts/macroscopic-dynamics-of-llms]]
- [[concepts/exploration-exploitation-llm]]
