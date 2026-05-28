---
schema_version: 1
type: concept
slug: retrieval-augmented-generation
canonical_name: Retrieval-Augmented Generation
domains:
- orita-cmo
created_at: '2026-05-28T01:45:53Z'
last_updated: '2026-05-28T01:45:53Z'
---

# Retrieval-Augmented Generation

## Summary

In the context of Orita's Claude Code buildout, Retrieval-Augmented Generation (RAG) is framed as a pre-processing step that vectorizes a large corpus into an addressable bundle so Claude can retrieve from it efficiently in-session rather than re-ingesting the natural-language source each time [[sources/pdf-4931157e130a]].

## Key claims

- Andrew Grant's framing: RAG sits alongside skills, agents, and MCP calls as one of the four primary building blocks of a Claude Code harness [[sources/pdf-4931157e130a]].
- Worked example used in session: take the full California state statutory code, vectorize it, and let Claude query the resulting bundle directly rather than perform natural-language inference over the entire corpus per question [[sources/pdf-4931157e130a]].
- Stated benefit: RAG reduces inference cost and works around Claude's limited in-session memory by letting the model "hit that bundle of sticks" instead of re-reading everything [[sources/pdf-4931157e130a]].
- Caveat noted by Andrew: most of the RAG plumbing is handled by the system itself, so it is "orthogonal" to the skill-and-agent development that should be Adrian's primary focus [[sources/pdf-4931157e130a]].

## Sources

- [[sources/pdf-4931157e130a]]

## Related

- [[entities/claude-code]]
- [[concepts/voice-of-the-customer]]
