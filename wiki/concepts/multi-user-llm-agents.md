---
schema_version: 1
type: concept
slug: multi-user-llm-agents
canonical_name: Multi-User LLM Agents
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Multi-User LLM Agents

## Summary

A class of LLM-based agent deployments in which a single agent serves multiple users simultaneously — each with distinct roles, preferences, authority levels, and private contexts — so that the agent must reason over heterogeneous, potentially conflicting objectives, asymmetric information, and per-user privacy constraints rather than satisfying one dominant user [[sources/pdf-shu-yang-2026-multi-user-large]].

## Key claims

- Most existing LLM systems are implicitly optimized for a single-principal interaction paradigm, in which the model is designed to satisfy the objectives of one dominant user whose instructions are treated as the sole source of authority and utility [[sources/pdf-shu-yang-2026-multi-user-large]].
- As LLM-based agents are integrated into team workflows and organizational tools, they are increasingly required to serve multiple users with distinct roles, preferences, and authority levels, leading to multi-user, multi-principal settings with unavoidable conflicts, information asymmetry, and privacy constraints [[sources/pdf-shu-yang-2026-multi-user-large]].
- Yang et al. (2026) present the first systematic study of multi-user LLM agents, formalizing multi-user interaction as a multi-principal decision problem and introducing a unified multi-user interaction protocol [[sources/pdf-shu-yang-2026-multi-user-large]].
- The paper designs three targeted stress-testing scenarios to evaluate current LLMs on multi-user instruction following, cross-user access control (privacy preservation), and sequential coordination [[sources/pdf-shu-yang-2026-multi-user-large]].
- Empirical findings: frontier LLMs frequently fail to maintain stable prioritization under conflicting user objectives, exhibit increasing privacy violations over multi-turn interactions, and suffer efficiency bottlenecks when coordination requires iterative information gathering [[sources/pdf-shu-yang-2026-multi-user-large]].
- Although recent work has begun to explore settings involving multiple users, these efforts still largely remain within the single-principal paradigm — auxiliary users mainly serve as information providers, and their instructions are typically flattened into a serialized format under a single user role [[sources/pdf-shu-yang-2026-multi-user-large]].
- LLM-based agent systems still lack a native protocol to explicitly distinguish different user roles, enforce information boundaries, or resolve benefit conflicts across users, substantially limiting their applicability in realistic multi-user multi-principal scenarios [[sources/pdf-shu-yang-2026-multi-user-large]].
- Extending LLMs from single principal–agent to genuine multi-principal settings is described as not a superficial generalization but a qualitative shift in problem formulation, requiring rethinking both training objectives and evaluation protocols [[sources/pdf-shu-yang-2026-multi-user-large]].

## Sources

- [[sources/pdf-shu-yang-2026-multi-user-large]]

## Related

- [[concepts/multi-principal-decision-problem]]
- [[concepts/principal-agent-problem]]
- [[concepts/single-user-chat-template]]
- [[concepts/selective-context-visibility]]
- [[entities/shu-yang]]
- [[entities/jiaxin-pei]]
