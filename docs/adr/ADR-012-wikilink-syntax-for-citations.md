# ADR-012: Wikilink syntax for citations

**Status:** Accepted
**Date:** 2026-05-25

## Context

Wiki pages must link claims to their source documents. Two common citation syntaxes exist in Markdown-based systems: numeric footnotes (`[1]` → `[^1]: ...`) and wikilinks (`[[sources/id]]`). The choice affects how citations are parsed, validated, and rendered in Obsidian and the web UI.

## Decision

Citations use the wikilink syntax `[[sources/<id>]]` (with optional CiTO verb alias: `[[sources/<id>|confirms]]`). This is the same syntax Obsidian uses for links, making every citation a navigable graph edge in the knowledge base. The validator parses `[[sources/...]]` patterns directly without a separate footnote registry.

Numeric footnotes (`[1]`, `[^1]: ...`) were rejected: they require maintaining a numbering scheme per page, break when paragraphs are reordered, and are not native graph edges in Obsidian. Chicago/APA citation styles were rejected as too verbose for inline use and not machine-parseable by a simple regex.

## Consequences

Citations are Obsidian-navigable and appear as backlinks on source pages. The validator's citation grounding check is a regex scan (`[[sources/...]]`) rather than a footnote registry lookup — simpler but also simpler to spoof. CiTO verb aliases (`confirms`, `disputes`, `extends`) enable typed citations but require a versioned allowlist (`citations_allowlist.yaml`) to prevent drift.
