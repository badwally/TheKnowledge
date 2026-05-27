---
schema_version: 1
type: concept
slug: self-critique-rubric-reward
canonical_name: Self-critique rubric reward
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Self-critique rubric reward

## Summary

A self-critique rubric reward is a reinforcement-learning signal in which a language model evaluates its own outputs against a rubric and the resulting critique is used as the reward, allowing alignment to extend from tasks with externally verifiable answers to open-ended domains; in the Kimi K2 technical report it is paired with verifiable rewards (RLVR) inside a joint RL stage [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Key claims

- The Kimi K2 framework introduces a self-critique rubric reward mechanism that lets the model learn from evaluating its own outputs, in addition to externally defined verifiable tasks [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- This mechanism is described as the means by which alignment is extended from static to open-ended domains [[sources/pdf-kimi-team-2026-kimi-k2-open]].
- It is composed with reinforcement learning from verifiable rewards (RLVR) into a single general RL framework rather than used independently [[sources/pdf-kimi-team-2026-kimi-k2-open]].

## Sources

- [[sources/pdf-kimi-team-2026-kimi-k2-open]]

## Related

- [[concepts/verifiable-rewards-rl]]
- [[concepts/agentic-data-synthesis]]
- [[entities/kimi-k2]]
