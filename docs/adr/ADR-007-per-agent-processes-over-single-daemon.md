# ADR-007: Per-Agent Processes over Single Daemon

**Status:** Accepted
**Date:** 2026-05-25

## Context

Gateway operations (ingest, filter, NLM sync) can be long-running and are invoked by multiple consumers: the CLI, scheduled tasks, and evaluation scripts. A daemon model would centralize state management and allow concurrent operations. A per-invocation model keeps each operation independent but requires each caller to handle its own lifecycle.

## Decision

Each gateway operation runs as an independent process invoked via the CLI or directly via the ops module. There is no long-running gateway daemon. Scheduled operations use the OS scheduler (cron / launchd). Concurrency within a single operation is handled at the operation level (e.g., parallel HTTP fetches during batch ingest), not via a shared process.

Rejected: A persistent gateway daemon with a socket-based IPC interface. A daemon requires a supervisor process (launchd plist or systemd unit), crash recovery logic, and a health-check mechanism. For a personal knowledge base operated by a single user, this operational overhead is not justified by the concurrency benefit.

Rejected: A message queue (e.g., Redis Streams) that decouples producers (pollers, CLI) from the gateway consumer. A queue adds a network or local service dependency and complicates the debugging story. Problems become: "why is the queue stalled?" rather than "why did this command fail?"

Rejected: Threading within a shared daemon process. Python's GIL limits true parallelism for CPU-bound work. For I/O-bound operations (HTTP, disk), `asyncio` within a single invocation is sufficient without the complexity of a daemon.

## Consequences

Each invocation is independently debuggable: logs are scoped to the process, and a crashed operation does not affect other operations. Scheduled tasks appear in cron/launchd logs directly. The trade-off is that two simultaneous CLI invocations can race on the same file; the validator's slug-uniqueness check catches the most common collision, but a file lock is not enforced.
