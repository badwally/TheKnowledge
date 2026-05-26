# ADR-002: Gateway as Single Mutator

**Status:** Accepted
**Date:** 2026-05-25

## Context

Multiple consumers touch the knowledge base: the CLI, scheduled agents, evaluation scripts, and ad-hoc LLM sessions. Without a single point of control, each consumer must independently enforce citation validation, slug uniqueness, frontmatter schema compliance, and the source immutability constraint. Enforcement drift across consumers is a near-certainty in a system under active development.

## Decision

All writes to `raw/` and `wiki/` go through `src/gateway/ops/` (the gateway). No other code path, script, or agent writes to these directories directly. The gateway is the only place that runs the validator, logs operations to `log.md`, and enforces the source-immutability guard.

Rejected: Each consumer validating its own writes. This duplicates validation logic and means a bug in one consumer silently corrupts the corpus. The validator is complex enough that duplication is a maintenance burden, not just a convenience cost.

Rejected: A write-ahead log that consumers write to, with a background daemon flushing to disk. This is architecturally cleaner for concurrency but adds operational complexity (daemon lifecycle, crash recovery) that is not warranted for a single-user personal system.

Rejected: Allowing direct writes for "trusted" callers (e.g., migration scripts) with a bypass flag. Experience has shown that bypass flags become the default for anything inconvenient, and the hard guarantee erodes. Migrations run through the gateway; if the gateway cannot express the migration cleanly, the gateway ops are extended.

## Consequences

The validator, logging, and immutability guard are implemented once and enforced unconditionally. Adding a new operation means adding a new gateway op, not a new consumer-side write path. The trade-off is that gateway ops must be expressive enough to cover all legitimate write patterns — gaps result in pressure to bypass, which is itself a signal to extend the op set.
