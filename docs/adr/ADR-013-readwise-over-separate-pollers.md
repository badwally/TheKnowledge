# ADR-013: Readwise v3 over separate Gmail/RSS/Podcast pollers

**Status:** Accepted
**Date:** 2026-05-25

## Context

Phase 2 originally planned three separate pollers: INT-1 (Gmail digest), INT-2 (RSS/web reader), INT-3 (Podcast/audio). Each would require its own authentication, pagination logic, and ID scheme. The user subscribes to Readwise, which consolidates highlights from Kindle, Pocket, Instapaper, Twitter saves, and web articles via a single v3 Export API endpoint.

## Decision

INT-9 (Readwise v3 poller) replaces INT-1/INT-2/INT-3. One poller, one API token (`READWISE_TOKEN`), one pagination scheme (`next` URL chaining). The v3 Export API returns all document types (articles, books, tweets, podcasts) in a uniform shape, so no per-type converter is needed. Highlights are included inline in the document response.

Building three separate pollers was rejected: each would have required its own auth setup (Gmail OAuth, RSS polling logic, podcast feed parsing) with minimal shared infrastructure. The Gmail poller additionally required navigating complex OAuth scopes. Readwise covers the same capture surface with a single token.

## Consequences

The system depends on the user maintaining a Readwise subscription. Documents not captured by Readwise (private PDFs, internal wikis) still need to be ingested via `wiki ingest`. If the Readwise API changes or the subscription lapses, the poller stops working and captured content must be ingested via other paths. The Readwise ID (`<type>-<readwise_id>`) is stable as long as the Readwise account is active.
