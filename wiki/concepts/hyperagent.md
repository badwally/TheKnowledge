---
type: concept
slug: hyperagent
canonical_name: Hyperagent
domains:
  - ai-and-agents
---

# Hyperagent

## Summary

A self-referential AI agent introduced by Zhang et al. (2026) that combines a task agent (which solves a target task) and a meta agent (which modifies agents and generates new ones) into a single editable program — such that the mechanism responsible for generating improvements is itself subject to modification, enabling improvement of both task-solving behavior and the procedure that produces future improvements [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Key claims

- A hyperagent is a self-referential agent that integrates a task agent and a meta agent into a single editable program [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Within this framing, an "agent" is any computable program, optionally including calls to foundation models, external tools, or learned components; the task agent solves a given task, and the meta agent modifies agents and generates new ones [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The defining property of a hyperagent is that the meta-level modification procedure is itself editable — a property the authors call metacognitive self-modification [[sources/pdf-jenny-zhang-2026-hyperagents]].
- As a result, a hyperagent can improve not only how it solves tasks (the task agent) but also how it generates and applies future modifications (the meta agent) [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Because its self-modification mechanism is fully modifiable and not tied to any particular task domain, a hyperagent can in principle self-improve for any computable task [[sources/pdf-jenny-zhang-2026-hyperagents]].
- This drops the assumption — required by prior recursive-self-improvement systems like the Darwin Gödel Machine — that task-solving skill must align with self-modification skill, an assumption that holds in coding (where both evaluation and self-modification are coding tasks) but not in general [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The authors summarize the agenda as systems that "do not merely search for better solutions, but continually improve their search for how to improve" [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The DGM-Hyperagents (DGM-H) system is the first concrete instantiation of the hyperagent framework [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Sources

- [[sources/pdf-jenny-zhang-2026-hyperagents]]

## Related

- [[concepts/dgm-hyperagents]]
- [[concepts/darwin-godel-machine]]
- [[concepts/metacognitive-self-modification]]
- [[concepts/self-referential-agent]]
- [[concepts/recursive-self-improvement]]
- [[concepts/open-ended-self-improvement]]
