# ADR-004: Plan Before Write for Incremental Ingest

**Status:** Accepted
**Date:** 2026-05-25

## Context

Incremental ingest (single-source, agent-driven) can silently create duplicate pages, cross-domain contamination, or citation chains that skip intermediate sources. These problems are hard to detect after the fact and compound over time. A planning step gives the operator visibility into what the agent intends before any writes occur.

## Decision

For incremental ingest, the gateway logs a written plan before any `wiki/` page is created or updated. The plan names: which source pages will be created, which existing pages will be updated, and which cross-references will be added. The plan is logged to `log.md`. The `--with-plan` flag surfaces the plan to the user for review when invoked interactively. Batch ingest (50+ sources, code-driven) does not require interactive plan review but logs the plan programmatically.

Rejected: Write-first, then surface a diff for review. This requires the operator to understand what changed rather than what was intended. Diffs are hard to evaluate when the change set is large; plans are easier to scan.

Rejected: No planning step — just ingest and validate. The validator catches structural errors (missing citation, wrong frontmatter) but cannot detect semantic problems (wrong domain assignment, a synthesis page that should have been a source summary instead). A plan catches semantic misalignments before they enter the corpus.

Rejected: A preview mode that writes to a staging area for approval. Staging adds complexity (two copies of files, promotion logic) and solves the same problem the log-first plan already solves.

## Consequences

Every non-trivial ingest is preceded by a logged plan. Operators can audit `log.md` to understand the sequence of decisions, not just the sequence of writes. The plan discipline also constrains agent behavior: the agent must articulate what it will do before doing it, which surfaces misunderstandings early.
