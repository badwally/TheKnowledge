# ADR-003: NotebookLM as Gateway-Mediated Service

**Status:** Accepted
**Date:** 2026-05-25

## Context

NotebookLM provides high-quality synthesis (audio overviews, slide decks, briefing documents) that would be costly to replicate locally. It requires a notebook-per-domain organization and expects sources to be uploaded explicitly. Artifacts it produces (audio files, slide decks) need to be filed back into the wiki with bidirectional links to remain traceable. Without mediation, artifacts can be generated but never make it back into the corpus.

## Decision

All NotebookLM operations go through gateway commands (`wiki nlm-*`). The MCP tools for NotebookLM are never called directly by agents or scripts. The gateway is responsible for: syncing sources to the appropriate corpus, invoking generation, polling for completion, downloading artifacts, and filing them back to `wiki/artifacts/` with frontmatter linking the artifact to its domain and originating sources.

Rejected: Calling NotebookLM MCP tools directly from LLM sessions. This is the highest-probability path to an artifact existing in NotebookLM but not in the wiki — the generation succeeds, the session ends, and there is no record. Discipline Gate exists because the failure mode is silent.

Rejected: A post-generation webhook or polling daemon that detects new NotebookLM artifacts and files them. Webhooks require a network-accessible endpoint on a personal machine. A polling daemon adds operational complexity. The gateway mediation pattern achieves the same guarantee without infrastructure.

Rejected: Treating NotebookLM artifacts as ephemeral outputs not worth filing. Synthesis artifacts are the primary output of research workflows; losing them undermines the purpose of the system.

## Consequences

Every NotebookLM artifact is represented in `wiki/artifacts/` with a stable slug and full frontmatter provenance. The corpus is the system of record; NotebookLM is a computation service, not a storage service. The constraint is that artifact generation requires intentional invocation — it is never triggered automatically as a side effect of ingest.
