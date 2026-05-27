---
schema_version: 1
type: concept
slug: protocol-registered-resource
canonical_name: Protocol-registered resource
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Protocol-registered resource

## Summary

In the Autogenesis Protocol, a passive, first-class, versioned resource — instance of one of the five RSPL entity types (prompt, agent, tool, environment, memory) — that is registered with the protocol and exposes explicit state, lifecycle, and versioned interfaces rather than being embedded as a tightly coupled internal component of an agent [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Key claims

- Most existing agent frameworks adopt architectures in which prompts, tools, and memory are embedded as tightly coupled internal components, with tools commonly treated as fixed functional modules manually curated and integrated into the agent pipeline; this design limits systematic reuse and controlled adaptation [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- A protocol-registered resource decouples these capability bundles from agent core logic, transforming them into passive, independently managed entities with explicit interfaces and state representations, enabling dynamic instantiation and controlled refinement during execution [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Each instance is formalized as a resource entity e_{ω,i} = (n_{ω,i}, d_{ω,i}, ε_{ω,i}, g_{ω,i}, m_{ω,i}), where n is a unique resource name, d is a short description, ε is an input-to-output mapping ε: X_ω → Y_ω, g ∈ {0,1} is a trainable marker indicating whether the resource is evolvable, and m is an auxiliary metadata dictionary [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- A resource registration record c_{ω,i} = (e_{ω,i}, v_{ω,i}, ϑ_{ω,i}, ϖ_{ω,i}, F_{ω,i}) extends the entity with versioning and serialization data and is supported by a small set of functionally grouped operators for lifecycle and registration (init, build), retrieval and inspection (list, get_state), evolution and versioning (update, restore), execution and contract (run, load_contract), and serialization/deserialization [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].
- Tool resources in RSPL encompass native tool scripts, MCP tools (Anthropic, 2025a), and agent skills (Anthropic, 2025b), unifying them under a single protocol-level interface [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]].

## Sources

- [[sources/pdf-wentao-zhang-2026-autogenesis-a-self]]

## Related

- [[concepts/resource-substrate-protocol-layer]]
- [[concepts/self-evolution-protocol-layer]]
- [[entities/autogenesis-protocol]]
