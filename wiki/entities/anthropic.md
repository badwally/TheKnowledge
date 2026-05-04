---
type: entity
slug: anthropic
canonical_name: Anthropic
entity_kind: organization
domains:
  - ai-and-agents
---

# Anthropic

## Summary

AI safety company that develops the Claude model family and ships a Research feature implemented as a multi-agent system; published the engineering postmortem "How we built our multi-agent research system" describing the architecture, prompt engineering, and evaluation approach behind that feature [[sources/pdf-f478e5f11837]].

## Key facts

- Operates an Engineering blog at which the multi-agent research system postmortem was published on June 13, 2025 [[sources/pdf-f478e5f11837]].
- Ships a Research feature in Claude that searches across the web, Google Workspace, and other integrations to accomplish complex tasks; the feature is implemented as a multi-agent system rather than a single-agent loop [[sources/pdf-f478e5f11837]].
- Reports an internal research evaluation in which a multi-agent system using Claude Opus 4 as the lead and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% [[sources/pdf-f478e5f11837]].
- Reports that agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chat interactions [[sources/pdf-f478e5f11837]].
- Identifies that, in their BrowseComp analysis, three factors explained 95% of the performance variance: token usage alone explained 80%, with the number of tool calls and the model choice as the other two explanatory factors [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]] — How we built our multi-agent research system

## Related

- [[concepts/multi-agent-system]]
- [[concepts/orchestrator-worker-pattern]]
- [[concepts/agentic-ai]]
