---
schema_version: 1
type: concept
slug: autogenesis-system
canonical_name: Autogenesis System (AGS)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Autogenesis System (AGS)

## Summary

A self-evolving multi-agent system built on the Autogenesis Protocol that dynamically instantiates, retrieves, and refines protocol-registered resources during execution, evaluated on long-horizon planning and tool-use benchmarks and reported to consistently improve over strong baselines [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Key claims

- AGS dynamically instantiates, retrieves, and refines protocol-registered resources during execution, rather than relying on hard-coded components [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- The system is composed of multiple specialized sub-agents — including a PlanningAgent that decomposes user tasks into sub-tasks, a DeepResearcherAgent, a DeepAnalyzerAgent, a ToolGeneratorAgent for tool creation and reuse, and a ReporterAgent and BrowserUseAgent for action execution and reporting — coordinated through the AGP server interface and context manager [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- AGS is evaluated on multiple challenging benchmarks that require long-horizon planning and tool use across heterogeneous resources, including GPQA (Rein et al., 2024), AIME, GAIA (Mialon et al., 2023), and LeetCode, with results demonstrating consistent improvements over strong baselines [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- The reported improvements are presented as evidence for the effectiveness of agent resource management and closed-loop self-evolution as architectural principles [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Significance: the work illustrates a potential shift from manual prompt engineering to automated protocol engineering, providing a foundational paradigm for building agent systems capable of sustained autonomous adaptation in complex environments [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Sources

- [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]]

## Related

- [[entities/autogenesis-protocol]]
- [[concepts/self-evolving-agent]]
- [[concepts/resource-substrate-protocol-layer]]
- [[concepts/self-evolution-protocol-layer]]
- [[concepts/closed-loop-evolution-operators]]
