---
schema_version: 1
type: concept
slug: selective-context-visibility
canonical_name: Selective Context Visibility (Multi-User LLMs)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Selective Context Visibility (Multi-User LLMs)

## Summary

A core requirement of multi-user LLM agent settings in which each user's private context C_i is visible to the shared agent only under an access-control policy, so that the agent must reason about which information may be disclosed in any output action without violating per-user privacy constraints [[sources/pdf-shu-yang-2026-multi-user-large]].

## Key claims

- In any principal-agent scenario, information asymmetry arises because the agent often has access to more information than each principal — in multi-user LLM settings, the agent observes a selectively shared context C_share derived from {C_i} under an access-control policy [[sources/pdf-shu-yang-2026-multi-user-large]].
- Multi-user formulations introduce access-control constraints that restrict which information from a user's private context C_i may be revealed through the agent's action a (e.g., a response, tool call, or disclosure decision) [[sources/pdf-shu-yang-2026-multi-user-large]].
- An essential requirement of multi-user LLMs is that the agent must reliably identify distinct users and model their individualized objectives and preferences, including which constraints — such as privacy requirements or organizational priorities — govern their requests [[sources/pdf-shu-yang-2026-multi-user-large]].
- This becomes increasingly difficult as the interaction grows longer and the number of users increases: more participants introduce more heterogeneous goals and more opportunities for conflict, while longer contexts increase the burden of maintaining stable user attribution and preference tracking over time [[sources/pdf-shu-yang-2026-multi-user-large]].
- Empirically, frontier LLMs in Yang et al.'s stress tests exhibit increasing privacy violations over multi-turn interactions, indicating that privacy and access control begin to break down as interaction rounds increase [[sources/pdf-shu-yang-2026-multi-user-large]].

## Sources

- [[sources/pdf-shu-yang-2026-multi-user-large]]

## Related

- [[concepts/multi-user-llm-agents]]
- [[concepts/multi-principal-decision-problem]]
