---
schema_version: 1
type: concept
slug: llm-as-judge-evaluation
canonical_name: LLM-as-Judge Evaluation
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# LLM-as-Judge Evaluation

## Summary

An evaluation pattern in which an LLM grades the free-form text outputs of another model against a structured rubric, used by Anthropic to evaluate their multi-agent Research feature on dimensions like factual accuracy, citation accuracy, completeness, and source quality where programmatic evaluation does not work [[sources/pdf-f478e5f11837]].

## Key claims

- Research outputs are difficult to evaluate programmatically because they are free-form text and rarely have a single correct answer, which makes LLMs a natural fit for grading outputs [[sources/pdf-f478e5f11837]].
- Anthropic used an LLM judge that evaluated each output against criteria in a rubric covering factual accuracy (do claims match sources?), citation accuracy (do the cited sources match the claims?), completeness (are all requested aspects covered?), and source quality [[sources/pdf-f478e5f11837]].
- LLM-as-judge evaluation scales when done well, and complements small-sample human evaluations during early agent development [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/agent-evaluation]]
- [[concepts/multi-agent-system]]
