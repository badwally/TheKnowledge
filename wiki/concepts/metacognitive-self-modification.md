---
type: concept
slug: metacognitive-self-modification
canonical_name: Metacognitive Self-Modification
domains:
  - ai-and-agents
---

# Metacognitive Self-Modification

## Summary

The property — named by Zhang et al. (2026) — of an AI system that can modify not only how it solves tasks but also the procedure by which it generates and applies future modifications, so that the mechanism of improvement is itself subject to improvement [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Key claims

- Because a hyperagent's self-improvement mechanism is itself modifiable, the authors call this property metacognitive self-modification [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Metacognitive self-modification entails improvement of not only task-solving behavior (the task agent) but also the mechanism that generates future improvements (the meta agent) [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Most existing self-improvement architectures rely on a fixed meta agent — a higher-level system that modifies a base system — which means the base system can only be improved within boundaries defined by the meta agent's design [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Adding a meta-meta system to improve the meta agent does not solve the problem; it merely shifts the issue upward and ultimately leads to an infinite regress of meta-levels [[sources/pdf-jenny-zhang-2026-hyperagents]].
- The authors argue that, when the mechanism of improvement is itself subject to improvement, progress can become self-accelerating and potentially unbounded (citing Lu et al., 2023) [[sources/pdf-jenny-zhang-2026-hyperagents]].
- Empirically, DGM-H exhibits metacognitive self-modification by learning transferable meta-level mechanisms (e.g., persistent memory, performance tracking) that improve its ability to generate better agents across domains and accumulate across runs [[sources/pdf-jenny-zhang-2026-hyperagents]].

## Sources

- [[sources/pdf-jenny-zhang-2026-hyperagents]]

## Related

- [[concepts/hyperagent]]
- [[concepts/dgm-hyperagents]]
- [[concepts/self-referential-agent]]
- [[concepts/recursive-self-improvement]]
- [[concepts/open-ended-self-improvement]]
