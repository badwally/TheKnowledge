---
schema_version: 1
type: concept
slug: verifiable-rewards-rl
canonical_name: Reinforcement learning from verifiable rewards (RLVR)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Reinforcement learning from verifiable rewards (RLVR)

## Summary

RLVR (reinforcement learning with verifiable rewards) is a post-training pattern in which the reward signal comes from programmatically checkable correctness of model outputs (e.g., unit tests passing, tool calls succeeding) rather than learned preference models; the Kimi K2 technical report uses RLVR as one half of a joint RL stage, paired with a self-critique rubric reward to extend the framework into open-ended domains [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- Kimi K2's general reinforcement learning framework explicitly combines verifiable rewards (RLVR) with a self-critique rubric reward mechanism rather than relying on either signal alone [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- The motivation given is that the model should learn not only from externally defined tasks but also from evaluating its own outputs, extending alignment from static to open-ended domains [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- This joint RL stage operates on top of agentic-data-synthesis pre/SFT outputs and is credited, alongside the synthesis pipeline, with Kimi K2's frontier agentic, coding, and reasoning benchmark results under non-thinking evaluation [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/self-critique-rubric-reward]]
- [[concepts/agentic-data-synthesis]]
- [[entities/kimi-k2]]
