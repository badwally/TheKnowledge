# ADR-005: Citation Grounding Mandatory

**Status:** Accepted
**Date:** 2026-05-25

## Context

LLM-authored wiki pages are the primary synthesis layer. Without enforced provenance, pages accumulate confident-sounding claims with no traceable source. Over time the wiki becomes a corpus of plausible-but-unverifiable assertions. In a personal knowledge base used for research, the difference between a claim grounded in a specific paper and a hallucination synthesized from training data is not visible without explicit citation.

## Decision

Every claim in every finalized wiki page must be followed by a `[[sources/<id>]]` wikilink. The validator enforces this at commit time for pages where `draft: false` (or where the `draft` field is absent). Pages flagged `draft: true` receive a lint warning, not a hard error.

Rejected: Numeric footnote-style citations (e.g., `[1]`). Footnotes require a bibliography section to be interpretable. Wikilinks are immediately navigable in Obsidian and in the web UI, and they make the citation graph machine-readable without parsing a bibliography block.

Rejected: Citation as a best-effort convention rather than a validated constraint. Convention-only citations erode under time pressure. The validator exists precisely because "try to cite things" has a known failure mode: it works until it doesn't and there is no signal when it stops.

Rejected: Source IDs embedded in frontmatter only (e.g., a `sources:` list), with no inline citation. Frontmatter-only sourcing does not indicate which specific claim is supported by which source. Inline citations are required for the citation graph to be semantically useful.

## Consequences

The citation graph is machine-readable and enforced. `wiki lint --scope orphans` gives an accurate count of sources not yet referenced by any wiki page. The standing constraint is that draft pages accumulate uncited claims silently — the 7-day draft-aging rule in lint is the backstop that keeps drafts from becoming permanent.
