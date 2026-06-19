# Librarian Phase 3 — Commit-time Invariants Build Report

**Date:** 2026-06-18
**Branch:** `docs/librarian-rag-design`
**Base commit:** `e5736650`
**Plan:** `docs/plans/2026-06-18-librarian-phase3-build-plan.md`

All 8 tasks implemented TDD (RED → GREEN → commit per task). Full suite green; eval gate held at baseline; build-tier deposit tool shipped.

## Per-task commits

| Task | SHA | Title |
|---|---|---|
| T1 | `a3835f63` | harden entity golden; entity gate reflects alias-authority fallback (I2, entry-gate 1a) |
| T2 | `e4c0bc7c` | deterministic LLM-free adjudicator — alias authority, NN recall-only (I1, entry-gate 1b) |
| T3 | `f8d0237f` | human-curated merge/link/distinct golden + falsifiability control (I3) |
| T4 | `1d173b0c` | wire adjudicator into serial commit — C5 write-skew, phantom-collision attach, concurrent-rebuild consistency (entry-gate 2) |
| T5 | `785547cd` | multi-label domain resolution; empty-set quarantine (decision 6) |
| T6 | `d9398e4b` | server-derived trust down-weight + eligibility floor (G5); recall@10 0.926→0.926 |
| T7 | `5af548cc` | claim-level auto-resolve by policy, reversible act, disputes edge (decision 6, G5) |
| T8 | `140aac74` | typed deposit tool + concurrent authorship workers (decision 3/4) |

## RED/GREEN evidence (per task)

- **T1:** Measured the lexical encoder on the 4 hard pairs — all 4 scored wrong (Ozempic/Semaglutide dist=1.0, GLP-1 abbrev/expansion dist=0.44, Type1/Type2 dist=0.198, Fed NY/SF dist=0.285). Hardened golden drops entity precision to 8/12 < floor 1.0; the old `test_entity_gate_strictest_threshold_distinguishes_merge` (asserted value==1.0) was retired in favor of the I2-honest gate. GREEN: 11 passed.
- **T2:** RED = `ModuleNotFoundError: gateway.dedup`. GREEN: 6 adjudicator + 2 replay tests pass.
- **T3:** RED = golden mis-scored `[type1-vs-type2 → link, fed-branches → link]`. The golden is authority; fixed by tightening RULE 3's link gate (see Deviations). GREEN: golden precision 1.0 + falsifiability control (≥2 mismatches under a geometry-only merger).
- **T4:** RED = phantom collision minted 2 pages (assert 2==1). GREEN: 4 tests — phantom-collision attaches to canonical, C5 write-skew unions both claims, genuinely-conflicting claims dead-letter (negative control), concurrent-rebuild keeps one canonical page with a REAL rebuild thread (no monkeypatch).
- **T5:** RED = unresolvable deposit committed instead of quarantined. GREEN: 7 tests (5 unit + 2 integration).
- **T6:** RED = `ModuleNotFoundError: gateway.trust`. GREEN: 5 tests. Eval gate held (see below).
- **T7:** GREEN on first run: 3 tests — auto-resolve records a reversible act (pubmed wins by server trust), G5 negative control (self-reported trust=1.0 cannot flip the winner), and a non-contradicting negative control.
- **T8:** RED = `ModuleNotFoundError: gateway.ops.deposit`. GREEN: 6 tests — durable enqueue-before-ack, rejects unknown page_type / missing grounding / empty synthesizes, concurrent enqueue overlap, synthesis cites only declared sources.

## Deviations from the plan's code blocks

1. **T1 — `embedding_eval.py` not modified.** The plan's Step 5 said "ensure when entity precision < floor, the report sets fallback_active=True and fallback_falsifiable=True." The existing Phase-2 machinery already sets `fallback_active` purely from `model_version == "lexical-fallback-v1"` (independent of value) and `fallback_falsifiable` from a one-label-flip re-score that stays < floor. Both flags were already honest on the hardened set, so no source change was needed; only the test assertions were reconciled. The old `test_entity_gate_strictest_threshold_distinguishes_merge` was replaced by `test_entity_gate_hard_cases_force_alias_authority_fallback`, and the "lexical fallback clears its operating point" assertion was narrowed to section+question (entity rides the active+falsifiable fallback by design).

2. **T2/T3 — adjudicator RULE 3 link gate uses `blocking_band`, not `identity_threshold`.** The plan's `dedup.py` proposed a same-kind link when `nn_distance <= identity_threshold` (0.30). That mis-scored the T3 golden: Type-1/Type-2 diabetes (0.198) and the two Fed branches (0.285) are *distinct sibling referents* that must stay `distinct`, but they fell inside 0.30 and were linked. The golden is authority. Fixed by gating the link on the tighter `blocking_band` (0.15): the genuine related link (reward-blunting / food-noise at 0.12) survives, the distinct siblings stay `distinct`. The merge-candidacy geometry window (`identity_threshold`) is retained as the recall net, but merge still requires alias authority. The `dedup.py` change was folded into the T3 commit (golden-driven).

3. **T2 — `cross-kind-never-merge` rule string.** The plan's `dedup.py` RULE 1 only `continue`d on a cross-kind candidate (falling through to distinct/link with no named rule), but the plan's Step-1 test asserts `v.rule == "cross-kind-never-merge"`. Adapted: a cross-kind candidate that shares an exact/normalized name is recorded as a `cross_kind_name_collision` and returned as `Verdict("distinct", None, "cross-kind-never-merge", …)`.

4. **T4 — empty-diff merge uses `git commit --allow-empty`.** A phantom-collision merge whose claims are all already present produces no staged diff; `git commit` would abort. Added an empty-diff check (`git diff --cached --quiet`) and `--allow-empty` so the `Intent-Id` trailer (idempotency/provenance) is still recorded and the disposition stays `merged`.

5. **T4 — structured claim-union in `_merge_rebase`.** Implemented `_claim_union` (three-way union of appended `## Claims` bullets): both the concurrent HEAD change and the authored change relative to base must be pure ADDITIONS of distinct bullets, else `RebaseConflict` → dead-letter. This is the C5 write-skew fix the plan specified by behavior. The test fixtures pass real base-blob OIDs (via `gate._head_blob_oid`) so the rebase lineage is recognized.

6. **T5 — `quarantined` added to `intent_queue.STATES`.** The queue's `_state_dir` rejects states not in `STATES`; added `quarantined` as a terminal state (not scanned by `in_flight_intents`).

7. **T6 — schema migration for the new `pages.trust` column.** `CREATE TABLE IF NOT EXISTS` cannot add a column to a pre-existing DB. Bumped `_SCHEMA_VERSION` 1→2 and added a version-mismatch guard in `_init_schema` that drops the data tables (pages/page_domains/links/sections) when the stored version is older, so the gitignored derived index self-heals with the new column on the next refresh. Trust is derived at index time from `source_type` + `filter_score` (neutral 0.5 for authored pages), read into `IndexHit.trust`, and applied as a centered down-weight `_W_TRUST * (trust - 0.5)` with `_W_TRUST = 0.5`.

8. **T7 — contradiction detection is subject-based.** The deposit carries `claim_subject` in identity; the gate scans the target page (HEAD) for an existing claim with the same subject prefix but a different object. On contradiction it calls `ops/contradiction.auto_resolve` (server-trust desc → recency desc; self-report never read), appends a reversible act to `.knowledge/contradictions/resolution_acts.jsonl`, materializes a `[[sources/<id>|disputes]]` CiTO edge under a `## Contested` heading, and keeps BOTH claims (loser retrievable). Source-type for the existing side is read from the source page frontmatter, falling back to the id prefix.

9. **T8 — concurrent-authorship & synthesis tests scoped to deterministic contracts.** The plan's Step-4/5 sketches assumed a provenance-span worker pool and a `_drive_to_commit` harness that do not exist as infrastructure. The tests instead assert the load-bearing properties honestly: two deposits enqueue with overlapping wall-clock spans (no global author lock) and both land durably in `submitted/`; a synthesis deposit's enqueued payload declares exactly its submitted sources (canonicalization at deposit time, no fabricated sources). `wiki_deposit` was added to the mcp-parity `expected_auxiliary` set (build-tier, no CLI parity by design).

## Final verification

- **Full suite:** `2158 passed` (`.venv/bin/python -m pytest -q`). Baseline was ~2037; the increase is the new Phase-3 tests. Two sqlite-WAL-lock timing flakes (`test_embedding_rebuild::test_nonatomic_rebuild_exposes_half_state_negative_control`, `test_doc5_rotate_log::test_rotate_log_archives_old_entries`) appeared once under full-suite contention and cleared on isolated + full re-run; neither touches Phase-3 code paths.
- **Phase-3 green-gate list:** `46 passed` (the 9 named test modules).
- **Eval gate (MANDATORY):** `wiki eval-retrieval --compare` → fts **recall@10 = 0.926** (≥ 0.90, baseline 0.926, no regression), recall@5 = 0.852, MRR = 0.690. The trust down-weight does not move retrieval because golden-corpus pages are mostly neutral-trust authored pages and `_W_TRUST` (0.5) is small relative to BM25 + tier/authority.
- **Lint:** see below.

## DONE_WITH_CONCERNS items

None that block. Notes:
- The two timing flakes above are pre-existing concurrency sensitivity in the embedding/index sqlite stores, not Phase-3 regressions.
- `_claim_union` and contradiction detection are deliberately minimal (append-bullet add/add union; subject-prefix matching). They cover the Phase-3 invariants and negative controls but are not a general NLP claim-merge — heavier reattachment/merge semantics remain future work.

## Review fixes (independent review → GO-WITH-FIXES)

Three findings fixed TDD (RED that catches the bug → fix → GREEN → commit). Same branch, same staging discipline.

| Fix | SHA | Title |
|---|---|---|
| I1 | `fb21cdb9` | point disputes edge at policy-resolved loser, not new claim |
| I2 | `4e76a5cd` | concept merge targets wiki/concepts; normalize merge-kind so concepts merge |
| B1 | `a1e4c509` | merge preserves aliases/body/wikilinks + writes tombstone; needs-manual-merge on body collision |

**I1 (disputes edge backwards + dead code).** RED: `test_disputes_edge_points_at_loser_when_new_claim_wins` — committed the low-trust `web-9` claim first, then the high-trust `pubmed-1` claim (the NEW claim wins). Against the old code the edge read `[[sources/pubmed-1|disputes]]` (mislabeling the winner as contested). FIX: direct the edge at `act["loser"]["source"]`/`["claim"]` from the returned auto-resolve act; deleted the dead `front2`/`body2`. GREEN: edge now cites `web-9` (the loser); `pubmed-1` is not in any disputes edge.

**I2 (concept merge mis-targets entities/).** RED: `test_concept_merge_targets_concepts_dir_not_entities` — two concept pages in `wiki/concepts/` with an alias-authority match; the old hardcoded `wiki/entities/<slug>.md` target hit the not-exists fallback and minted a duplicate (2 pages). FIX (two parts): (a) `_retarget_to_canonical` resolves the target by searching `wiki/entities/` then `wiki/concepts/` for the real page; (b) added `_merge_kind(page_type, entity_kind)` so a concept compares as kind `concept` (concept pages omit `entity_kind`, so the deposit and candidate previously read as cross-kind and never merged). Cross-kind protection preserved (drug vs concept still differ). GREEN: exactly one live concept page; no `entities/` duplicate.

**B1 (BLOCKING — merge silently dropped body/wikilinks/aliases).** RED: `test_merge_preserves_aliases_body_and_writes_tombstone` — a deposit with a `## Mechanism` section, an `[[entities/glp1]]` wikilink, and frontmatter `aliases: [Ozempic, Wegovy]` merged into `ozempic.md`; the old code kept only the `## Claims` bullets (Mechanism prose, wikilink, and the `Wegovy` alias all gone, no tombstone). FIX: `_retarget_to_canonical` now (a) unions the deposit's `aliases` + `canonical_name`/`title` into the canonical frontmatter (preserving dedup-recall surfaces); (b) carries the deposit's non-Claims sections (with wikilinks) onto the canonical page when it lacks that heading, and raises `RebaseConflict` → dead-letter `needs-manual-merge` on a heading collision with differing content (no silent drop); (c) writes a `merged_into:`/`redirect:` tombstone at the deposited slug so inbound `[[entities/<slug>]]` links resolve and the merge is reversible; the reattachment set is recorded in `decision_basis.merge_reattachment`. The phantom-collision, concurrent-rebuild, and concept tests were updated to count LIVE pages (excluding tombstones) and to assert the tombstone exists. GREEN.

### Post-fix verification

- **Full suite:** `2161 passed` (was 2158; +3 review-fix tests). The two earlier sqlite-WAL timing flakes did not recur.
- **Eval gate:** `wiki eval-retrieval --compare` → fts **recall@10 = 0.926** (≥ 0.90, no regression), recall@5 0.852, MRR 0.690.
- **Lint:** `wiki lint --scope broken-wikilinks` → 1 finding, the SAME pre-existing `OSError(63, 'File name too long')` check-infrastructure error on the live corpus (not a dangling link from the tombstones; the `dedup` scope does not exist — `broken-wikilinks` is the dedup-integrity check). The B1 tombstone assertion is the per-merge dangling-link guard.

### Review fix N1 (residual silent-drop — preamble)

**N1 (IMPORTANT) — merge silently discarded the deposit preamble.** `_retarget_to_canonical`'s `if not h: continue` dropped everything before the first `## ` heading, assuming it was an inert stub — losing a unique preamble wikilink. Same silent-drop class as B1.

- **SHA:** `6790772f` — carry novel merge preamble content, no silent drop (review N1).
- **RED:** `test_merge_preserves_preamble_wikilink_or_dead_letters` — a deposit whose PREAMBLE carries `[[entities/glp1-receptor]]` merged into `ozempic.md`; the old code dropped the link (no exception). FIX: compute the canonical preamble's non-blank line set; deposit-preamble lines NOT already present are carried onto the canonical page under a `## Merged context` heading; an empty / byte-equal / subset preamble (the `# Overview\nstub.` boilerplate) stays inert. GREEN: the preamble wikilink survives.
- **Negative control:** `test_inert_stub_preamble_merges_cleanly_no_dead_letter` — an identical `# Overview\nstub.` preamble still merges cleanly with no false dead-letter (passed before and after the fix).

### Post-fix verification (N1)

- **Full suite:** `2163 passed` (was 2161; +2 N1 tests).
- **Eval gate:** fts **recall@10 = 0.926** (≥ 0.90, no regression), recall@5 0.852, MRR 0.690.
- N2 (cosmetic double-citation on the disputes-edge line) left as a tracked MINOR, not fixed (per review instruction).
