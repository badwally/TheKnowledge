# ADR-010: Filter as Haiku-tier LLM (not Sonnet/Opus)

**Status:** Accepted
**Date:** 2026-05-25

## Context

The semantic filter scores every ingested source against a domain policy. In bulk ingest scenarios, filter calls outnumber all other LLM calls by an order of magnitude. Using a Sonnet or Opus-tier model for filtering would make bulk ingestion prohibitively expensive and slow (~30-60s per source vs ~5s for Haiku).

## Decision

`ClaudeCLIFilterClient` (the default filter backend) targets Haiku via a `call_split(system, user)` path that sends the policy as a system prompt. The policy + examples prefix is cached when prompt caching is enabled. Filter accuracy at Haiku tier is sufficient for the binary include/review/reject decision: the rationale string is stored with the score so human reviewers can audit decisions that matter.

Using Sonnet for borderline cases (score 0.5-0.7) was considered and rejected: implementing a tiered routing scheme adds complexity and the review band already catches borderline sources for human inspection. Fully automated classification without LLM was also considered and rejected: keyword overlap alone produces too many false positives for the domains in use.

## Consequences

Filter decisions are less nuanced than a Sonnet-tier judgment. The review band (0.50–0.70 by default) partially compensates — borderline sources go to the triage queue rather than being auto-rejected. Policy examples must be carefully curated because Haiku is more sensitive to example quality than larger models.
