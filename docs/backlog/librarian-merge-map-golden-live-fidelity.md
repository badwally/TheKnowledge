# Backlog: merge-map golden records nn_distances the live encoder doesn't produce

**Filed:** 2026-06-20
**Source:** #1 of the gate-tests-what-ships pass (as-built review follow-up)
**Priority:** Medium (gate-fidelity gap; the gate passes, but in a distance regime the encoder never produces)

## What

`.knowledge/eval/dedup/golden.yaml` records a per-case `nn_distance` that
`merge_map_eval` feeds to `dedup.adjudicate` directly (its header: "judges the
adjudicator's decision directly — NOT embedding geometry"). The recorded values
are meant to be "the lexical-fallback encoder's ACTUAL distance for the pair."
They are not, for the disjoint-surface cases.

Measured against the live `LexicalFallbackEncoder` (2026-06-20), using the
production identity text (canonical_name + aliases, which is what
`embedding_index._identity_text` embeds and `commit_gate._dedup_recheck`
queries):

| golden case | recorded `nn_distance` | live (name only) | live (name+aliases, production basis) |
|---|---|---|---|
| brand-generic-same-drug (Ozempic/Semaglutide) | 1.0 | ~1.0 | **0.276** |
| abbrev-expansion (GLP-1 RA / expansion) | 0.9 | — | ~0.29 |
| near-related-link (food-noise/reward-blunting) | 0.12 | **1.0** | 1.0 |
| type1-vs-type2-distinct | 0.198 | 0.198 | 0.198 (faithful) |
| fed-branches-distinct | 0.25 | 0.285 | 0.285 (close) |

Two rows are materially unfaithful:

- **brand-generic** records 1.0 but the production path scores **0.276** (the
  alias overlap gives shared surface). The recorded 1.0 is the canonical-name-only
  distance, which the production path never uses.
- **near-related-link** records 0.12 but the live encoder scores **1.0** — the
  lexical encoder cannot see two disjoint surfaces as related, so the `link`
  verdict in the golden is unreachable on the live encoder.

## Impact

`merge_map_eval` exercises `adjudicate` in a distance regime the live encoder
does not produce, so it can stay green while the live commit-time dedup behaves
differently. It is not wrong about adjudicator *logic* — but it is not a faithful
end-to-end check of the live merge decision. The new live-recall guard
(`test_live_entity_embedding_recall_surfaces_alias_merge` in
`tests/integration/test_lifecycle_flow.py`) covers the alias-merge recall path
end to end; the `link` path has no faithful live case (no disjoint-surface pair
reaches `blocking_band` on this encoder).

## Resolution (options)

1. **Re-record** each golden `nn_distance` from the live encoder using the
   production identity text, and drop/replace the `near-related-link` case with a
   pair the lexical encoder actually scores `≤ blocking_band` (0.15) — or accept
   that `link` is only reachable under a future neural encoder and mark the case
   as encoder-conditional.
2. **Drive `merge_map_eval` with live distances** (compute `nn_distance` from the
   real index per case instead of reading the recorded value), so the eval is a
   faithful end-to-end check. Heavier; changes a gate floor — needs the same
   before/after `eval-retrieval`-style guard so it doesn't silently shift the
   merge-map baseline.

## Trigger

Next merge-map golden touch, or when a neural encoder replaces the lexical
fallback (the `link`-path cases become reachable then). Until then, the live
alias-merge recall guard is the end-to-end sentinel; this doc records that the
recorded distances are a logic fixture, not a live-faithful one.
