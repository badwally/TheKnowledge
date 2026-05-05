---
type: entity
slug: autogenesis-protocol
canonical_name: Autogenesis Protocol (AGP)
entity_kind: paper
domains:
  - ai-and-agents
---

# Autogenesis Protocol (AGP)

## Summary

A two-layer self-evolution protocol introduced in Wentao Zhang's 2026 paper "Autogenesis: A Self-Evolving Agent Protocol," designed to decouple "what evolves" from "how evolution occurs" in LLM-based agent systems and to support modular, traceable, safety-preserving evolution across heterogeneous agent components [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Key facts

- Architected as two layers: Layer 1 is the Resource Substrate Protocol Layer (RSPL), which models prompts, agents, tools, environments, and memory as protocol-registered resources with explicit state, lifecycle, and versioned interfaces; Layer 2 is the Self-Evolution Protocol Layer (SEPL), which specifies a closed-loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Motivated as a response to a conceptual mismatch with existing connectivity protocols such as Anthropic's Model Context Protocol (MCP) and Google's Agent-to-Agent (A2A), which standardize model–tool invocation and inter-agent communication but leave the internal state of agents and resources opaque and do not specify mechanisms for managing resource lifecycles, tracking version lineage, or constraining state mutations over time [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Identifies three essential problems any self-evolution protocol must address: Decoupling (resources abstracted from agent core logic), Safety & Auditability (strict version control and rollback), and Formalism (a standardized operator set such as reflect/propose/verify governing the evolution process) [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Defines five RSPL entity types — PROMPT, AGENT, TOOL, ENV, MEM — chosen as a minimal yet expressive substrate that captures a common denominator across modern agent stacks; tools encompass native tool scripts, MCP tools, and agent skills [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- A resource entity is formalized as e_{ω,i} = (n, d, ε, g, m), where n is a unique resource name, d is a short description, ε is an input-to-output mapping, g ∈ {0,1} is a trainable marker indicating whether the resource is evolvable, and m is an auxiliary metadata dictionary [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Each resource also has a serializable registration record c_{ω,i} = (e, v, ϑ, ϖ, F) supporting lifecycle and registration (init/build), retrieval and inspection (list/get_state), evolution and versioning (update/restore), execution and contract (run/load_contract), and serialization/deserialization [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- AGP is presented as an enabler of automated protocol engineering — a shift away from manual prompt engineering — by exposing standardized self-repair and evolution capabilities at the protocol level [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Sources

- [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]] — Autogenesis: A Self-Evolving Agent Protocol

## Related

- [[entities/wentao-zhang]]
- [[entities/nanyang-technological-university]]
- [[concepts/autogenesis-system]]
- [[concepts/resource-substrate-protocol-layer]]
- [[concepts/self-evolution-protocol-layer]]
- [[concepts/protocol-registered-resource]]
- [[concepts/closed-loop-evolution-operators]]
- [[concepts/connectivity-vs-evolution-protocols]]
- [[concepts/self-evolving-agent]]
