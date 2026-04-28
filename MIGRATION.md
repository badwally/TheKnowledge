# MIGRATION.md — Legacy Obsidian vault → canonical schema

Plan for converting the three legacy research-notebook Obsidian vaults into the canonical knowledge base at `~/code/knowledge/`. Pair with `WIKI.md` (canonical schema) and `CLAUDE.md` (agent control surface).

This document is a planning artifact, not the migration script itself. The actual migration runs through the gateway as `wiki batch-ingest --legacy-import <vault-path>` once gateway is stable. The script lives at `~/code/knowledge/migrations/0001-import-legacy-vaults.py`. It reads from `~/code/research-notebook/data/obsidian*/` (research-notebook stays put as a frozen historical artifact) and writes to `~/code/knowledge/`.

## Table of contents

1. Goals
2. Legacy vault inventory
3. Sequence (phases)
4. Legacy → canonical mapping
5. Gateway requirements (`--legacy-import` mode)
6. Slug mapping rules
7. Source body recovery strategy
8. Citation rewrite strategy
9. NotebookLM corpus mapping
10. Filter score and example bank backfill
11. Concept vs entity classification
12. Validation and rollback
13. Retirement of legacy vaults
14. Open questions

---

## 1. Goals

1. Preserve all human-curated wiki content (concepts, synthesis, MOCs) verbatim.
2. Reconstruct `raw/<type>/<id>.md` files for all migrated sources via re-fetch where feasible.
3. Backfill the example bank with past filter decisions from JSON checkpoints.
4. Map existing NotebookLM corpora to their canonical domains; preserve `nlm_corpus_ids` on migrated sources.
5. Eliminate the dual-system fork: after migration, `~/code/knowledge/` is the single source of truth.
6. Idempotent migration: re-running the script must be a no-op on unchanged input.

## 2. Legacy vault inventory

| Vault path | Domain (canonical slug) | Sources | Concepts | MOCs | Synthesis | Status |
|---|---|---|---|---|---|---|
| `~/code/research-notebook/data/obsidian/` | `ai-temporal-video` | 86 | 46 | 5 | 3 | Complete |
| `~/code/research-notebook/data/obsidian_glp1/` | `glp1-reward-modulation` | 127 | 28 | 5 | 3 | Complete |
| `~/code/research-notebook/data/obsidian_edge_ai/` | `edge-ai-agentic` | TBD | TBD | TBD | TBD | Legacy run to be completed before migration |

JSON checkpoints (filter decisions):

- `~/code/research-notebook/data/staged/*ai_temporal_video*.json`
- `~/code/research-notebook/data/staged/*glp1*.json`
- `~/code/research-notebook/data/staged/*edge_ai*.json` (after legacy run completion)

Domain configs (filter policy seed):

- `~/code/research-notebook/config/domains/ai_temporal_video.yaml`
- `~/code/research-notebook/config/domains/glp1_reward_modulation.yaml`
- `~/code/research-notebook/config/domains/edge_ai_agentic.yaml`
- `~/code/research-notebook/config/editorial_policy.md` (seed of the per-domain `policy.yaml`)

NotebookLM corpora: existing notebook IDs to be discovered via `nlm` CLI listing or extracted from research-notebook's `data/research/` outputs (which reference the notebook).

## 3. Sequence (phases)

| Phase | Action | Trigger |
|---|---|---|
| 1 | Gateway build complete: `wiki ingest`, validator, log, watcher, `--legacy-import` mode | Gateway design stable |
| 2 | Migrate `obsidian/` → `ai-temporal-video` (smallest complete vault, 86 sources) | Phase 1 done |
| 3 | Migrate `obsidian_glp1/` → `glp1-reward-modulation` (largest complete vault, 127 sources) | Phase 2 lessons folded back |
| 4 | Finish legacy `edge_ai` pipeline run on existing research-notebook code; commit | Phases 2 and 3 done |
| 5 | Migrate `obsidian_edge_ai/` → `edge-ai-agentic` | Phase 4 commit landed |
| 6 | Retire legacy vaults: move to `~/code/research-notebook/data/legacy_obsidian_archive_<YYYY-MM>/`; remove from active reads | Phase 5 lint passes clean |

**Why this order:** AI temporal video first because it is the smallest complete vault — exercises migration end-to-end, lessons fold into GLP-1 migration without redoing the larger one. edge_ai last because the user chose to finish the legacy run first; that completion is independent of phases 2–3.

Each phase is a git branch on `~/code/knowledge/`; merged to main after lint passes clean and a 10% sample audit confirms content fidelity.

## 4. Legacy → canonical mapping

| Legacy file or artifact | Canonical destination |
|---|---|
| `data/<vault>/sources/<long-slug>.md` (summary page) | `wiki/sources/<canonical-id>.md` (summary, schema-compliant) |
| Source body for above (currently absent from disk) | `raw/<type>/<canonical-id>.md` (re-fetched via § 7) |
| `data/<vault>/concepts/<slug>.md` | `wiki/concepts/<slug>.md` OR `wiki/entities/<slug>.md` (per § 11) |
| `data/<vault>/mocs/<slug>.md` | `wiki/mocs/<domain>.md` |
| `data/<vault>/synthesis/<slug>.md` | `wiki/synthesis/<slug>.md` |
| `data/<vault>/_tags.md` | merged into `index.md` and `.knowledge/policies/<domain>/policy.yaml` (controlled vocabulary) |
| `data/staged/<domain>_*.json` | `.knowledge/policies/<domain>/examples/<source-id>.yaml` (filter decisions, § 10) |
| `data/research/<domain>_*.json` | Discarded. Intermediate findings already captured in synthesis pages; no need to preserve raw research outputs. |
| `config/domains/<domain>.yaml` + `config/editorial_policy.md` | seed of `.knowledge/policies/<domain>/policy.yaml` (canonical policy schema, § 10.4 of WIKI.md) |
| Existing NotebookLM corpus | recorded in `nlm/notebooks.yaml`; corpus left intact (live link from migrated artifact pages preserves bidirectional access) |

## 5. Gateway requirements (`--legacy-import` mode)

The migration drives specific gateway capabilities. These should be in scope for the gateway build (not bolted on later).

### 5.1 `wiki ingest --legacy-import <path>` (single file)

Behavior:

1. Detect legacy file format (heuristic: descriptive slug + simpler frontmatter; or explicit `--from-legacy-vault`).
2. Identify source type via § 6 detection rules.
3. Generate canonical ID (§ 6 mapping).
4. Reconstruct raw body via § 7 recovery strategy.
5. Generate canonical frontmatter (core + per-type meta).
6. Generate canonical wiki source page (summary preserved verbatim from legacy).
7. Rewrite internal wikilinks (§ 8).
8. Set `nlm_corpus_ids` from § 9 mapping if applicable.
9. Set `filter:` block from § 10 backfill if checkpoint data available.
10. Run validator; reject if any rule fails.

### 5.2 `wiki batch-ingest --legacy-import <vault-path>` (whole vault)

Behavior:

1. Build slug map for the entire vault first (legacy slug → canonical ID for every source).
2. For each source: invoke single-file path with shared slug map for citation rewrites.
3. After source pass: migrate concepts, synthesis, MOCs (citation rewrites use the slug map).
4. Apply concept-vs-entity classification (§ 11).
5. Backfill example bank from JSON checkpoints.
6. Set up `policy.yaml` from legacy config + editorial policy.
7. Update `nlm/notebooks.yaml` with corpus mapping.
8. Update `index.md`.
9. Run lint; report.

### 5.3 Required flags

- `--dry-run` — print the slug map and migration plan; no writes.
- `--phase <ai-temporal-video|glp1-reward-modulation|edge-ai-agentic>` — restrict to one domain.
- `--accept-summary-as-body` — when re-fetch fails, use legacy summary as raw body with `meta.legacy_recovery: "summary-only"` flag.
- `--audit-sample <N>` — emit N random migrated pages alongside their legacy origins for human review.

### 5.4 Idempotency

- Source ID derived from stable identifier (video ID, arXiv ID, PMID, DOI, hash) — not from filename.
- Content hash recomputed on every run; unchanged hash → skip.
- Re-running migration on a partially-migrated vault must complete cleanly.

## 6. Slug mapping rules

Detection per source type (in priority order):

| Source type | Detection signal | Canonical ID format | Notes |
|---|---|---|---|
| YouTube | `url:` contains `youtube.com/watch?v=<id>` or `youtu.be/<id>` | `yt-<videoId>` | Most reliable. |
| arXiv | `url:` contains `arxiv.org/abs/<id>` OR frontmatter `arxiv_id` | `arxiv-<id>` (dot preserved, e.g. `arxiv-2403.12345`) | Direct extraction. |
| PubMed | `url:` contains `pubmed.ncbi.nlm.nih.gov/<pmid>` OR frontmatter `pmid` | `pubmed-<pmid>` | Direct extraction. |
| PDF (with DOI) | `doi:` in frontmatter or content | `pdf-<author>-<year>-<short-name>` | e.g. `pdf-kaufmann-2024-incretin`. |
| PDF (no DOI) | filename, summary content | `pdf-<sha256-prefix-12>` | Hash-based fallback. |
| Web | `url:` (any other URL) | `web-<YYYY-MM-DD>-<3-char-hash>` | Date from `published_at` or ingestion timestamp; hash from URL. |
| Unknown | none of above | flagged in dry-run; requires manual mapping | Surface in audit output. |

Existing legacy vault has frontmatter with `url:`, `source:`, or similar — extraction handles all variants.

## 7. Source body recovery strategy

| Source type | Recovery | Fallback |
|---|---|---|
| YouTube | Re-fetch transcript via `youtube-transcript-api` (no auth required). | If transcript unavailable: accept legacy summary with `meta.legacy_recovery: "summary-only"`. |
| arXiv | Re-fetch abstract from arXiv API (free); full text via PDF download is optional. | Abstract is sufficient body for ingestion-stage content. |
| PubMed | Re-fetch abstract from PubMed API (free). | Abstract sufficient. |
| PDF | Locate original under `~/code/research-notebook/data/` or `~/Downloads/`; if missing, flag for re-acquisition (likely manual). | `--accept-summary-as-body` gates this. |
| Web | If URL resolves, fetch and convert via Web Clipper readability logic. | Web rot — accept legacy summary. |

Re-fetch is per-source-cheap (sub-second for transcripts and abstracts). Total migration cost: minutes, not hours.

For all `legacy_recovery: "summary-only"` cases, lint flags them as `lossy-migration` so they can be re-acquired later if needed.

## 8. Citation rewrite strategy

Two-pass per vault:

1. **Build slug map.** For every source in the vault, derive its canonical ID and record `legacy_slug → canonical_id`. Persist to `.knowledge/migrations/<domain>-slug-map.yaml` for audit.
2. **Rewrite links.** Walk all `wiki/` and `raw/` files; replace `[[<legacy-slug>]]` with `[[sources/<canonical-id>]]` where the legacy slug is in the source map. Concept and MOC links (`[[concepts/<slug>]]`, `[[mocs/<slug>]]`) remain as-is unless the slug itself needs canonicalization.

Rewrite is mechanical and exhaustive. Lint after migration confirms zero broken wikilinks.

## 9. NotebookLM corpus mapping

Existing notebooks map to canonical domains. Recovery:

1. List existing notebooks via `nlm notebook list`.
2. For each domain, identify the corresponding notebook by name match or by source overlap with the staged JSON.
3. Record in `~/code/knowledge/nlm/notebooks.yaml`:

```yaml
notebooks:
  ai-temporal-video:
    notebook_id: <id>
    sources_count: 86
    last_sync: "<migration-timestamp>"
    legacy_imported_at: "<migration-timestamp>"
  glp1-reward-modulation:
    notebook_id: <id>
    sources_count: 127
    last_sync: "<migration-timestamp>"
    legacy_imported_at: "<migration-timestamp>"
  edge-ai-agentic:
    notebook_id: <id>
    sources_count: <after-completion>
    last_sync: "<migration-timestamp>"
    legacy_imported_at: "<migration-timestamp>"
```

For every migrated source, set its `nlm_corpus_ids` to include the notebook ID for its domain. The existing corpus contents do not need to change — only the wiki side records the relationship.

## 10. Filter score and example bank backfill

For each entry in `data/staged/<domain>_*.json`:

1. Extract: source ID (mapped via § 6), score, rationale, policy version.
2. Set `filter:` block on `raw/<type>/<id>.md` frontmatter:

```yaml
filter:
  score: 0.92
  policy_version: "legacy-v1"      # backfilled label; new decisions use versioned policy.yaml
  rationale: "<original rationale>"
  decided_at: "<original timestamp from JSON checkpoint>"
  user_correction: null             # null unless user marks one during phase 6 audit
```

3. If `score >= 0.85` (high confidence): pin to `.knowledge/policies/<domain>/examples/<source-id>.yaml`:

```yaml
source_id: <id>
domain: <domain>
decision: include
score: 0.92
policy_version: "legacy-v1"
rationale: "<original rationale>"
pinned_at: "<migration-timestamp>"
pinned_by: "legacy-backfill"
frontmatter_snapshot: {...}
content_excerpt: "<first 500 chars>"
```

4. Generate canonical `.knowledge/policies/<domain>/policy.yaml` from `config/domains/<domain>.yaml` + `config/editorial_policy.md`. Label initial version `<domain>-v1`. Record under `policy_versions/legacy-v1.yaml` for traceability.

The example bank gets seeded with hundreds of high-quality past decisions on day one. Filter calls from day one onward have meaningful priors.

## 11. Concept vs entity classification

The legacy vault has `concepts/` only. Canonical schema splits into `entities/` (real-world things: drugs, people, organizations, papers, places) and `concepts/` (abstract ideas: mechanisms, phenomena, frameworks).

Migration approach:

1. For each legacy concept page, run an LLM classification call: given the page title + first 500 chars, classify as `entity | concept` with confidence score and entity-kind if entity.
2. High-confidence (>= 0.85): auto-route to `wiki/entities/` or `wiki/concepts/`.
3. Low-confidence: stage in `wiki/concepts/` with `entity_classification_pending: true` frontmatter; surface in lint for human review.

Classification is per-domain (domain context helps disambiguation). Reuses the same Claude call surface as the filter — accumulated decisions become a small classification example bank for future ingests.

## 12. Validation and rollback

Each phase:

1. Branch from `main`: `migration/phase-<N>-<domain>`.
2. Run migration with `--dry-run`; commit the slug map and migration plan.
3. Run migration for real; commit results in logical chunks (sources, then wiki pages, then policies).
4. Run `wiki lint`. Required pass: zero broken wikilinks, zero malformed pages, zero schema-drift, citation density within threshold.
5. Random 10% sample audit: agent + human compare migrated page against legacy original. Content fidelity confirmed.
6. Merge to `main`; tag release `migration-phase-<N>`.

Rollback: `git revert` the merge commit. Migration is reversible at the phase level until the next phase begins.

## 13. Retirement of legacy vaults

After Phase 5 lint passes clean, no archive move is needed: research-notebook stays put as a frozen historical artifact. The legacy vaults remain in their original locations under `~/code/research-notebook/data/` indefinitely; the entire repo is read-only from M0 onward.

What changes after Phase 5:

1. Update research-notebook's project memory to record that legacy vaults are now superseded by `~/code/knowledge/`.
2. Add a `STATUS.md` at `~/code/research-notebook/` marking the repo as a historical artifact, with a pointer to `~/code/knowledge/`.
3. No file moves, no deletions, no `git rm`.

The legacy NotebookLM corpora remain live (canonical wiki pages link to them via `nlm_artifact_url`). Do not delete the corpora; they are the canonical synthesis service for those domains.

## 14. Open questions

1. **PDFs without DOI in legacy vaults**: where to look for source files? Suggest an audit pass during Phase 1 to inventory all PDF sources and their recoverability before running the migration.
2. **Concept-vs-entity classification confidence threshold**: 0.85 is a starting guess. May need tuning after Phase 2 results.
3. **Should partial edge_ai content (pre-completion) be staged in `~/code/knowledge/` during Phases 2 and 3?** Default: no. Stays in research-notebook until Phase 4. Avoids dual-state.
4. **Do we want an explicit `legacy_provenance:` frontmatter field on every migrated source/page?** Captures origin path, migration timestamp, audit status. Default: yes. Cheap; useful for debugging and trust.
5. **Synthesis page citation density**: legacy synthesis pages may not meet the canonical citation density threshold. Two options: (a) ingest as draft (`draft: true`) and finalize after augmentation, or (b) accept as-is with a per-domain density override. Default: option (a) — drafts are exactly the right fit for "imported but needs citation work."

These are flagged for review during Phase 1, not blocking.
