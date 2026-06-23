# Backlog: Index-time grounding-worthiness flag (the principled form of the Hole 1 content-gate)

**Category:** RAG / retrieval substrate
**Priority:** Low (the Hole 1 fix already makes the curated layer reachable; this is the cleaner mechanism, not a missing capability)
**Effort:** ~half a day (FTS schema column + populate at index build + teach `search_fts`/`retrieve` to use it; re-run the eval/merge-map/embedding gates)
**Trigger to action:** ANY of — (a) `wiki search` is observed surfacing placeholder-stub sections (the search path does NOT carry the retrieve-side section content-gate, so it can still return `_(...)_` stubs); (b) a second consumer of section text needs the same stub suppression (e.g. a future hybrid/embedding retriever); (c) the `_(...)_` structural predicate produces a false positive/negative on a new placeholder convention; (d) a dedicated retrieval-quality pass.

---

## Problem

The Hole 1 fix (`docs/260622_rag-retrieval-draft-visibility-brief.md`, branch
`fix/rag-draft-visibility`) gates placeholder-stub *sections* out of grounding context
at **retrieve-assembly time**: `is_placeholder_section()` in `gateway/ops/retrieve.py`
skips a section whose stripped body is solely a lone italic-parenthetical `_(...)_`
placeholder (the legacy/M6 marker family, ~1,090 occurrences).

That predicate is correct and well-tested, but it lives on the **retrieve path only**.
Two consequences:

1. **`wiki search` is not gated.** `search_fts` returns the best-matching section per
   page; a placeholder section can still be the BM25 winner for a placeholder-token query
   and `wiki search` will surface it. Today that is acceptable (search is an
   agent/inspection tool, not the grounding path), but it is the same stub-pollution the
   retrieve fix exists to prevent, in a different surface.
2. **Grounding-worthiness is recomputed per read.** The predicate runs at assembly time on
   live section text. It is cheap, but it is a per-query string check rather than a
   materialized property.

Grounding-worthiness is genuinely a **section** property (does this section have real,
citable content?). The data model only has a **page**-level `draft` flag, which is why the
hybrid legacy pages (real lede/Methods + placeholder Summary/Key-claims) cannot be
expressed by `draft` alone. The retrieve-time predicate is a lightweight stand-in for the
property the index should carry.

## Proposed solution

Compute grounding-worthiness once, at index build, and store it on the section row:

- Add a `sections.placeholder` (or `sections.grounding_worthy`) boolean column to the FTS5
  schema in `search_index.py`, populated when sections are split/indexed using the same
  `is_placeholder_section()` predicate (move it to a shared module so both index build and
  any retrieve fallback import it from one place).
- `search_fts` excludes (or de-prioritizes) placeholder sections via SQL, so BOTH
  `wiki search` and `wiki retrieve` inherit the gate from one source of truth — and the
  best-section-per-page dedup can fall back to the next non-placeholder section instead of
  dropping the page.
- Keep the retrieve-time predicate as a defense-in-depth backstop, or delete it once the
  index column is authoritative (decide at implementation time).

## Verification

- The Hole 1 instrument carries over unchanged: `scripts/probe_retrieve.py` (G-POS recall,
  G-NEG-1 placeholder-pollution == 0) plus `tests/gateway/test_ws2_retrieve.py` (predicate
  truth table + section-gate + demotion + annotation).
- Add a `wiki search` negative-control test asserting a placeholder-token query does not
  return the stub section.
- Re-run the pre-merge gate (`gateway.scripts.gate`): FTS recall@10 ≥ 0.90 must hold; the
  embedding/merge-map gates are untouched (this is FTS-index-shape only).

## Out of scope

This does not finalize or cull the perma-draft backlog itself (Hole 3) — that is the
parallel `wiki finalize` curation track. This item only moves the grounding-worthiness
*signal* from a per-read predicate to a materialized index property.
