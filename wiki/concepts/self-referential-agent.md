---
schema_version: 1
type: concept
slug: self-referential-agent
canonical_name: Self-Referential Agent
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Self-Referential Agent

## Summary

An AI system able to analyze, modify, and evaluate itself; Zhang et al. (2026) argue this property is necessary for unbounded self-improvement, since a system whose meta-level mechanism is fixed is bounded by its initial design and cannot be rescued by adding further meta-levels [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Key claims

- A self-referential system is one able to analyze, modify, and evaluate itself, following Kirsch and Schmidhuber (2022) and Zhang et al. (2025b) [[sources/pdf-jenny-zhang-2026-hyperagents]].
- To overcome the limitation that a base system can only be improved within the boundaries defined by a fixed meta agent's design, the system must be self-referential rather than relying on additional meta-levels [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Self-referential meta-learning has prior instantiations in neural networks (Kirsch and Schmidhuber, 2022; Jackson et al., 2024) and in evolutionary methods (Lu et al., 2023) [[sources/pdf-jenny-zhang-2026-hyperagents]].
- More recent work explores self-referential improvement using foundation-model-based agents, including the Darwin Gödel Machine and its successors, but those systems improve at improving primarily within the coding domain [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The hyperagent is a specific instantiation of self-referential AI in which the task agent and the meta agent are combined into one editable program, so any part of the system — including its self-modification procedure — can be modified [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Sources

- [[sources/pdf-jenny-zhang-2026-hyperagents]]

## Related

- [[concepts/hyperagent]]
- [[concepts/metacognitive-self-modification]]
- [[concepts/recursive-self-improvement]]
- [[concepts/darwin-godel-machine]]
