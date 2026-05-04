---
type: concept
slug: agentic-data-synthesis
canonical_name: Agentic data synthesis
domains:
  - ai-and-agents
---

# Agentic data synthesis

## Summary

Agentic data synthesis is the post-training pattern of programmatically generating high-fidelity tool-use trajectories — diverse tools, agents, tasks, and verifiably-correct interactions — via simulated and real-world environments, used to bootstrap multi-step reasoning, long-term planning, and tool use that are rare in naturally occurring text data; the Kimi K2 technical report names a large-scale instance of this pipeline as one of its three core contributions [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- The Kimi Team frames the central post-training challenge as bridging the gap between general-purpose pre-training priors and actionable agentic behaviors, on the grounds that capabilities such as multi-step reasoning, long-term planning, and tool use are rare in natural data and costly to scale [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- They introduce a large-scale agentic data synthesis pipeline that systematically generates tool-use demonstrations via simulated and real-world environments [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- The pipeline is described as constructing diverse tools, agents, tasks, and trajectories to create high-fidelity, verifiably correct agentic interactions at scale [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- Together with a joint RL stage that combines verifiable rewards (RLVR) with self-critique rubric rewards, this synthesis pipeline is credited with Kimi K2's strong agentic-benchmark results, including 66.1 on Tau2-bench, 76.5 on ACEBench (En), 65.8 on SWE-bench Verified, and 47.3 on SWE-bench Multilingual under non-thinking evaluation [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/verifiable-rewards-rl]]
- [[concepts/self-critique-rubric-reward]]
- [[entities/kimi-k2]]
