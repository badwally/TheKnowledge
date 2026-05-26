# ADR-011: Source immutability — body never mutated post-ingest

**Status:** Accepted
**Date:** 2026-05-25

## Context

Sources in `raw/` are the ground truth for all wiki citations. If source bodies could be edited after ingest, the provenance chain would be unreliable: a wiki page citing `[[sources/web-2026-01-01-abc]]` could silently refer to different content after the source was corrected. This is the same problem that makes git history rewriting dangerous in shared repos.

## Decision

The body content of `raw/` files is never modified after ingest. `MUTABLE_SOURCE_FIELDS` in `validator.py` enumerates the frontmatter fields that pipeline stages may update (filter score, NLM corpus IDs, wiki backlinks, contested flag). The `ingest.py` skip-if-exists guard prevents re-ingesting a source with the same ID. If a source contains an error, the correct response is to ingest a corrected version as a new source with a new ID.

In-place source correction was rejected: it breaks the citation chain retroactively and makes `git diff` on the raw file misleading. A content-addressable store (hash-as-ID) was considered as an alternative but rejected — human-readable IDs (`web-YYYY-MM-DD-hash8`) are more debuggable and the collision risk at this scale is negligible.

## Consequences

Correcting a factual error in a source requires ingesting a new document and updating all wiki citations that referenced the old source. This is intentionally friction-producing — it forces explicit acknowledgment of source changes. The `MUTABLE_SOURCE_FIELDS` list must be carefully maintained; adding a new pipeline stage that writes to source frontmatter requires a deliberate addition to the allowlist.
