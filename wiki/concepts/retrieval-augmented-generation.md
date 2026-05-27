---
schema_version: 1
type: concept
slug: retrieval-augmented-generation
canonical_name: Retrieval Augmented Generation (RAG)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Retrieval Augmented Generation (RAG)

## Summary

A static-retrieval pattern in which a system fetches the chunks most similar to an input query and uses them to generate a response; contrasted by Anthropic with the multi-step, dynamic search used by their multi-agent Research feature, which adapts to new findings and analyzes results to formulate higher-quality answers [[sources/pdf-f478e5f11837]].

## Key claims

- Traditional approaches using Retrieval Augmented Generation (RAG) use static retrieval — they fetch some set of chunks that are most similar to an input query and use these chunks to generate a response [[sources/pdf-f478e5f11837]].
- Anthropic's Research architecture, by contrast, uses a multi-step search that dynamically finds relevant information, adapts to new findings, and analyzes results to formulate high-quality answers [[sources/pdf-f478e5f11837]].
- The contrast frames RAG as a baseline rather than an endpoint: Research replaces static retrieval with iterative, agent-driven exploration in which subagents progressively narrow focus based on intermediate results [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/multi-agent-system]]
- [[concepts/orchestrator-worker-pattern]]
