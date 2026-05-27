---
schema_version: 1
type: concept
slug: darwin-godel-machine
canonical_name: Darwin Gödel Machine (DGM)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Darwin Gödel Machine (DGM)

## Summary

A 2025 system from Zhang et al. that demonstrates open-ended self-improvement is achievable in coding: starting from a single coding agent, it repeatedly generates and evaluates self-modified variants, retaining successful variants in a growing archive of "stepping stones" for further improvement [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Key claims

- The Darwin Gödel Machine (Zhang et al., 2025b) demonstrates that open-ended self-improvement is achievable in the coding domain [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Starting from a single coding agent, the DGM repeatedly generates and evaluates self-modified variants, forming a growing archive of stepping stones for future improvement [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Because both the evaluation task and the self-modification process involve coding, gains in coding ability translate directly into gains in self-improvement ability — an alignment property that does not generally hold beyond coding [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The DGM relies on a handcrafted, fixed mechanism to produce self-improvement instructions: the mechanism analyzes past evaluation results and the agent's current codebase to generate an instruction directing where the agent should self-improve [[sources/pdf-jenny-zhang-2026-hyperagents]].
- That instruction-generation mechanism is not modifiable, so the DGM's capacity for self-improvement is bottlenecked by this fixed step — the limitation that the HyperAgents follow-up work targets [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The DGM's ability to improve at improving relies on a limiting assumption: that the skills required to solve the evaluation tasks are the same as those required for effective self-reflection and self-modification — an assumption the authors argue is unlikely to hold outside coding domains [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The DGM is identified by the authors as the most established prior self-improving algorithm and the closest baseline for the DGM-Hyperagents system [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Sources

- [[sources/pdf-jenny-zhang-2026-hyperagents]]

## Related

- [[concepts/hyperagent]]
- [[concepts/dgm-hyperagents]]
- [[concepts/recursive-self-improvement]]
- [[concepts/open-ended-self-improvement]]
- [[entities/jenny-zhang]]
