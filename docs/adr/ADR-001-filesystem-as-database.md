# ADR-001: Filesystem as Database

**Status:** Accepted
**Date:** 2026-05-25

## Context

The knowledge base needs durable, inspectable persistence for sources (`raw/`) and synthesized pages (`wiki/`). The system is operated by a single user on a personal machine. Content must survive tool changes, remain readable without running software, and integrate with version control for history and rollback.

## Decision

All persistent state lives in Markdown files with YAML frontmatter on the local filesystem, committed to git. No relational database, no document store, no embedded key-value store is used.

Rejected: SQLite for structured metadata. SQLite would enable fast queries over frontmatter fields but makes the corpus opaque without a schema viewer, complicates conflict resolution in git, and requires schema migrations as the frontmatter spec evolves. The query advantage is real but secondary — orientation and debuggability matter more at this scale.

Rejected: A hybrid store where body content stays in Markdown but metadata is extracted into a database. This creates a dual source of truth. Keeping them in sync adds failure modes without eliminating the migration problem.

Rejected: A hosted document store (Notion, Airtable). These add network dependency, API rate limits, and vendor lock-in. The corpus is not large enough to justify the operational overhead.

## Consequences

Every file is human-readable and diffable. Git history is the audit trail. Standard shell tools (`grep`, `find`, `jq` via `yq`) suffice for ad-hoc queries. Frontmatter schema changes are handled with migration scripts rather than schema ALTER statements. If page counts cross ~10k, a derived BM25 or vector index can be layered on top without changing the canonical representation.
