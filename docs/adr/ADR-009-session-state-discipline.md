# ADR-009: Session-state discipline via docs/session-state.md

**Status:** Accepted
**Date:** 2026-05-25

## Context

Claude Code sessions have a finite context window. When the context compacts, prior conversation is summarized and in-progress work can be lost or misrepresented. Long build sessions across multiple milestones compound this: open contracts, mid-edit files, and rejected approaches from hours ago disappear from context. Without a durable record, each compaction risks re-litigating settled decisions or abandoning in-flight work.

## Decision

`docs/session-state.md` is a load-bearing file that records: open contracts (work started but not committed), files mid-edit, decisions made this session, rejected approaches with reasons, and the next atomic step. The agent re-reads this file at the start of any plan-or-write action if its mtime is newer than the session start. At milestone boundaries and before context-consuming refactors, the agent checkpoints proactively. Pre-compact and session-start hooks enforce the re-read discipline.

Trusting the context window alone was rejected: summarization loses the specificity of rejected approaches and mid-edit states, which are exactly what future actions depend on. A shared external database (Notion, Linear) was considered for persistence but rejected — it adds a network dependency and out-of-band write path to a system that deliberately minimizes those.

## Consequences

Every milestone boundary requires a session-state update before merging. The file can become stale if the agent forgets to checkpoint; the hooks mitigate this but do not eliminate the risk. The discipline is opt-in per project (the file must exist; absence means the project has not opted in).
