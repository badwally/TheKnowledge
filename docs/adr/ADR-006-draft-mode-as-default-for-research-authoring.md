# ADR-006: Draft Mode as Default for Research Authoring

**Status:** Accepted
**Date:** 2026-05-25

## Context

Research authoring is iterative. An agent writing a synthesis page from a partially-ingested domain may produce a structurally valid page with good claims but incomplete citations — because not all source pages exist yet to link to. Requiring full citation compliance at first write would block useful incremental progress. But suppressing the citation requirement entirely allows pages to linger indefinitely without provenance.

## Decision

Pages written by `wiki query` and `wiki ingest` carry `draft: true` in frontmatter by default. In draft mode, missing citations are lint warnings rather than validator errors. The `wiki finalize` command removes the draft flag and runs the full validator; pages that fail validation are not finalized. Drafts older than 7 days are flagged by `wiki lint` as aged drafts requiring attention.

Rejected: No draft mode — every page must pass full validation on creation. This makes iterative ingest workflows impractical: the operator would need to supply every citation at the moment of page creation rather than building up citation coverage as more sources are ingested.

Rejected: Draft mode as opt-in (`--draft` flag required). Research authoring is almost always iterative. Requiring the flag means operators forget it and get validator errors on the first write of every new synthesis page.

Rejected: A soft-lock that prevents reading draft pages until finalized. Drafts are useful as working documents. The goal is eventual citation compliance, not access restriction.

## Consequences

Agents can write useful synthesis pages early in a domain's development, before all source pages exist. The 7-day aging rule creates accountability without a hard deadline. `wiki finalize` is the explicit promotion step that enforces the citation contract. The standing constraint is that lint must be run regularly to prevent draft pages from accumulating silently.
