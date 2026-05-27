---
schema_version: 1
type: concept
slug: connectivity-vs-evolution-protocols
canonical_name: Connectivity vs evolution protocols
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Connectivity vs evolution protocols

## Summary

A conceptual distinction drawn by the Autogenesis paper between agent protocols that standardize invocation and message passing — connectivity protocols such as Anthropic's Model Context Protocol (MCP) and Google's Agent-to-Agent (A2A) — and protocols that govern persistent state mutation, resource lifecycle, and version lineage in self-evolving systems [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Key claims

- Anthropic's Model Context Protocol (MCP) provides a unified interface for connecting language models to external tools and data sources, while Google's Agent-to-Agent (A2A) protocol aims to standardize communication primitives for collaboration among multiple agents [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- These protocols primarily address interoperability at the level of invocation and message passing — they specify how agents and tools interact but largely leave the internal state of agents and resources opaque [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- In particular, connectivity protocols do not define mechanisms for managing resource lifecycles, tracking version lineage, or constraining state mutations over time, and therefore do not directly support the persistent state evolution required by self-modifying agent systems [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Applying connectivity protocols directly to self-evolution scenarios presents a conceptual mismatch: the core of self-evolution lies not in invocation, but in state mutation and management [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- A specialized evolution protocol must therefore address three problems that connectivity protocols leave open — Decoupling (resources from agent logic), Safety & Auditability (version control and rollback), and Formalism (a standardized operator set governing evolution) [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Sources

- [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]]

## Related

- [[entities/autogenesis-protocol]]
- [[concepts/self-evolving-agent]]
- [[concepts/resource-substrate-protocol-layer]]
- [[entities/anthropic]]
