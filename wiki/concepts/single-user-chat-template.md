---
schema_version: 1
type: concept
slug: single-user-chat-template
canonical_name: Single-User Chat Template
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Single-User Chat Template

## Summary

The standard message-schema convention used by modern LLM training pipelines, in which a conversation is represented as a sequence of messages under a single "user" role alongside system and assistant roles, restricting the model from natively representing multiple distinct users with their own identities, roles, or authority levels [[sources/pdf-shu-yang-2026-multi-user-large]].

## Key claims

- Instruction tuning typically adopts a chat template that represents interaction as a sequence of messages under a single user role, with messages of the form {role: system, ...}, {role: user, ...}, {role: assistant, ...} (Taori et al., 2023, as cited) [[sources/pdf-shu-yang-2026-multi-user-large]].
- Some frameworks extend this schema by introducing an additional developer role in addition to system and user, but the template still does not natively represent multiple distinct users [[sources/pdf-shu-yang-2026-multi-user-large]].
- Even in multi-user settings, existing LLM interfaces typically serialize inputs from different users into a single user role (e.g., "userA says: ... userB says: ..."), preventing explicit modeling of user identities, roles, and authority information [[sources/pdf-shu-yang-2026-multi-user-large]].
- A native multi-user template would assign distinct roles per user (e.g., {role: userA, ...}, {role: userB, ...}); Yang et al. propose this as the schema needed for genuine multi-principal interaction [[sources/pdf-shu-yang-2026-multi-user-large]].
- The single-user template fundamentally constrains what LLMs can learn during training: SFT is framed as supervised learning over a single conditional distribution p_ω(y|x), and RLHF learns a single scalar reward r_ε(x, y) that conflates user-specific desiderata into one shared objective [[sources/pdf-shu-yang-2026-multi-user-large]].
- Because standard SFT data collapses all user inputs into a single user role and provides supervision for one assistant completion, the resulting model is naturally optimized for a single-principal interaction setting in which the LLM is designed to satisfy a single user's objective [[sources/pdf-shu-yang-2026-multi-user-large]].
- The learned reward in RLHF reflects what an "average" or aggregated user would consider a better response in context x, making it difficult for the resulting agent to explicitly represent multiple principals, reason about cross-user trade-offs, or enforce user-specific constraints under conflict (Ouyang et al., 2022, as cited) [[sources/pdf-shu-yang-2026-multi-user-large]].

## Sources

- [[sources/pdf-shu-yang-2026-multi-user-large]]

## Related

- [[concepts/multi-user-llm-agents]]
- [[concepts/multi-principal-decision-problem]]
- [[concepts/principal-agent-problem]]
