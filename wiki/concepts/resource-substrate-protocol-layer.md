---
type: concept
slug: resource-substrate-protocol-layer
canonical_name: Resource Substrate Protocol Layer (RSPL)
domains:
  - ai-and-agents
---

# Resource Substrate Protocol Layer (RSPL)

## Summary

Layer 1 of the Autogenesis Protocol; defines the evolvable substrate as a set of protocol-registered resources with explicit state, lifecycle, and version lineage, covering prompts, agents, tools, environments, and memory [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Key claims

- RSPL specifies which resources may change and how they are represented, versioned, and accessed, separating the definition of evolvable resources from the mechanisms that govern their evolution [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- The substrate is composed of five entity types — PROMPT (instructions), AGENT (decision policies), TOOL (actuation interfaces, including native tool scripts, MCP tools, and agent skills), ENV (task/world dynamics), and MEM (persistent state) — chosen as a minimal yet expressive set that provides a uniform target space on which SEPL can operate [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Resources in RSPL are passive: they encapsulate no optimization logic and cannot self-modify; all observations and state transitions occur only through controlled, interface-mediated operations invoked by higher layers [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Externalizing prompts, tools, and memory as first-class, versioned resources with standardized interfaces lets the same tool-calling agent policy be paired with different prompts and toolsets and deployed unchanged across tasks and environments [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- A resource entity in RSPL is formalized as e_{ω,i} = (n, d, ε, g, m), where ε is the input-to-output mapping and g ∈ {0,1} marks whether the resource is evolvable [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Sources

- [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]]

## Related

- [[entities/autogenesis-protocol]]
- [[concepts/protocol-registered-resource]]
- [[concepts/self-evolution-protocol-layer]]
- [[concepts/closed-loop-evolution-operators]]
