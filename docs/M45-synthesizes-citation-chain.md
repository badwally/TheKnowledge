# M45 — `synthesizes:` and the followable citation chain

**Status:** Shipped 2026-05-13. M45.1 (`--draft` default on `wiki research`, 3 new structural-frame labels) shipped same day after the fresh-prompt end-to-end run surfaced residual opener variants outside the M45 allowlist.
**Owner:** badwally
**Predecessors:** M44 / M44.1 / M44.2 / M44.3 — established the synthesis path through `wiki research`; M44.3 surfaced the residual problem of "framing-prose" claims that cite no specific source
**Successors:** post-M45 wiki finalize / lint chain validators; informs the future `wiki cite` op (re: open question in `gateway_edit_path_open_question.md`)

## M45.1 — `--draft` default + structural-label extensions (2026-05-13)

The fresh-prompt end-to-end validation (b7zzthxfj, 2026-05-13 ML-models-for-reserve-studies) confirmed M45's mechanism worked (orchestrator emitted `synthesizes:` + `## Included works`) but rejected at apply_plan due to **3 rejection categories the M45 allowlist didn't cover**:

1. **New opener variants** — NotebookLM emitted `"The provided sources detail…"`, `"The provided text illustrates…"`, `"There is an unanswered tension…"`, `"A significant gap in the provided literature…"`, `"When comparing the contexts where…"`, etc. None matched the M45 `_AGGREGATE_FRAMING_OPENERS_RE` allowlist (which keys on `"Based on the…"` / `"Across the…"` / `"Looking across…"`). Extending the allowlist further is whack-a-mole.
2. **3 new structural-frame labels** — `**Gap Identified:**`, `**Limitation Identified:**`, `**Tension Identified:**` (NotebookLM's sub-headers under Gaps/Limitations/Tensions sections). These ARE genuinely structural metadata; safe to add to the M44.2 allowlist.
3. **Mid-section interpretive prose** that isn't an opener (e.g., `"Markov processes serve as a foundational mathematical architecture…"`). M45's exemption is bounded to one opener per section by design; it cannot help here even with a broader allowlist.

**Fix split:**

1. **`wiki research` default to `--draft` mode.** CLI uses `argparse.BooleanOptionalAction` with default `True`. Pass `--no-draft` to opt into strict validation (recommended only when you have prior reason to believe the run will produce cleanly-cited prose, e.g., narrow firm-explainer queries). The cheap whack-a-mole alternative — extending the opener allowlist with each new NotebookLM phrasing — was rejected per the user's `feedback_survey_formal_practice_before_design.md` discipline ("don't spawn garbage").
2. **3 new structural-frame labels** added to `_STRUCTURAL_FRAME_LABELS` (Gap/Limitation/Tension Identified). These are real metadata, same category as M44.2's allowlist; small surface, low risk.

**What this does NOT change:** the M45 mechanism stays. `synthesizes:` + `## Included works` + the aggregate-framing exemption + `wiki lint --scope citation-chains` all remain. The default flip + 3 labels just acknowledge that NotebookLM's prose style is more varied than the allowlist can keep up with, and the cleaner workflow is draft-first + manual `wiki cite` + `wiki finalize`.

**Files:** `src/gateway/cli.py` (BooleanOptionalAction on --draft), `src/gateway/citations.py` (3 labels added), `WIKI.md` § 5.2 (label list updated) and § 5.5 (default flip documented), `tests/gateway/test_authorship.py` (pinned-allowlist test updated).

**Tests:** 793 passing (unchanged count; pinned-allowlist test now asserts the 14-label set).

---

## 1. TL;DR

The `wiki research` pipeline produces synthesis pages that include legitimate *aggregate observations* across the page's source corpus — claims like *"Based on the provided sources, four primary anchors emerge…"*. The strict per-source `citation-grounding` rule rejects them because they cannot point at a single source. M44.3's `--draft` workaround defers the problem; M45 resolves it by adopting **Cochrane / PRISMA's load-bearing convention**: explicitly enumerate every constituent work, then derive aggregate claims from that enumerated set.

The mechanism:

1. **`synthesizes:` frontmatter field** on synthesis pages — an explicit list of `sources/<id>` (for first-derivative) OR `synthesis/<slug>` (for cross-cutting) — never both, never `[[corpus]]`.
2. **`## Included works` required section** mirroring the `synthesizes:` list.
3. **Validator rule**: framing-prose claims at section openings are exempt from per-claim citation **only when** the page has `synthesizes:` with ≥2 entries and `## Included works` mirrors that list.
4. **`wiki lint --scope citation-chains`**: traverses `synthesizes:` graphs; reports dangling refs, missing `## Included works`, framing-claims on pages without `synthesizes:`.

Downstream pages (MOCs, cross-cutting syntheses) cite the synthesis page itself, not the corpus. The chain `MOC → cross-cutting synthesis → per-theme synthesis → raw sources` is mechanically followable end to end.

---

## 2. Motivation

### 2.1 What M44.3 left unresolved

M44.3 cleared the structural-frame bullet rejections via an allowlist + multi-line continuation tracking. The end-to-end synthesis run (`2026-05-13`, 05-11 methodology plan, draft mode) produced 5 committable pages but with **6 uncited claims across 3 pages**, all of pattern *"Based on the provided sources, the corpus presents…"*. The `--draft` flag lets these pages commit with `draft: true`; the path to `wiki finalize` remains unclear because there's nothing to cite the framing prose to.

### 2.2 The phenomenon: second-derivative claims

When research moves source → synthesis → cross-cutting synthesis, each layer adds interpretive distance:

| Layer | Example claim | Natural citation |
|---|---|---|
| Source | *"Drug X causes Y in trial Z."* | `[[sources/<id>]]` |
| **First-derivative synthesis** | *"GLP-1 binding shows a dose-response pattern across trials."* | `[[sources/<id1>]] [[sources/<id2>]]` etc. |
| **Second-derivative synthesis** | *"Four primary anchors emerge across these binding patterns."* | the **synthesis pages themselves** that the claim aggregates over |

The strict per-source rule was calibrated for the first two layers. Second-derivative claims fail it predictably, not accidentally. The question is whether to handle the predictable case as a first-class concept (the gateway recognizes synthesis tiers) or keep papering over each instance as it surfaces.

### 2.3 Why a survey changed the design

The user's initial sketch was a `derivative: 1|2` frontmatter integer plus a `[[corpus]]` aggregate-citation token. Web research across (a) academic scholarly-publishing convention and (b) PKM tooling surfaced material that materially improved the design:

| Finding | Source | Design implication |
|---|---|---|
| No formal "aggregate citation primitive" exists in any established ontology (CiTO, FaBiO, BiRO, BIBO, FRBR) | [SPAR ontologies](https://sparontologies.github.io/cito/current/cito.html); Shotton 2010 | A `[[corpus]]` token would be invented dialect interoperable with nothing |
| Cochrane / PRISMA load-bearing convention is **explicit enumeration**: a "Characteristics of included studies" table lists every constituent work; aggregate claims are mechanically computed from that set; the review becomes a new citable work at a higher tier | [Cochrane Handbook ch. 14](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14), [PRISMA 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8007028/) | Adopt the enumerated-set pattern verbatim; aggregate claims back-reference the enumeration |
| **Citation laundering / unfollowable aggregate citation** is the documented failure mode across academic publishing — the reader cannot reach constituents without redoing the search | [USC library guide](https://guides.library.sc.edu/navigating-research-fraud/citation-manipulation); [Information laundering](https://en.wikipedia.org/wiki/Information_laundering) | `[[corpus]]` is exactly that anti-pattern; reject it |
| No PKM tool encodes derivation depth as an integer. Obsidian's MOC, Zettelkasten's structure notes, Tana's supertags — all flat, navigational | Andy Matuschak's notes; Zettelkasten forum; Tana docs; Obsidian community | Drop `derivative: 1\|2`; not interoperable, no precedent |
| PKM failure mode #1 is "taxonomy bloat without enforcement" — ship new schema only if the validator can mechanically reject misuse | sudoscience.blog 2025; turbulencegains.com; medium.com PKM critiques | Every new field must come with validator + lint enforcement |

This survey is itself recorded as a memory: `feedback_survey_formal_practice_before_design.md` — the gating function "survey formal practice before designing any methodological structure."

---

## 3. Design

### 3.1 Schema changes

**Synthesis page frontmatter gains one new required field:**

```yaml
type: synthesis
slug: ...
title: ...
domains: [...]
question: ...
synthesizes:           # NEW (M45) — explicit enumeration of constituent works
  - sources/web-2026-05-08-123        # OR
  - synthesis/2026-05-11-cost-and-financial-framing
# (mixed types NOT allowed — see § 3.6 invariant)
```

**Synthesis page body gains one new required section:**

```markdown
## Included works

- [[sources/web-2026-05-08-123]] — Author (year). Title.
- [[sources/arxiv-2603.11884]] — Author (year). Title.
```

The `## Included works` list must mirror `synthesizes:` 1:1 — order doesn't matter, but the sets must be equal. The validator computes the symmetric difference; non-empty means rejection (or warning in draft mode).

### 3.2 Validator changes (`gateway/validator.py` + `gateway/citations.py`)

**New rule: aggregate-framing exemption.**

A claim sentence is "grounded" if:
1. It has a `[[sources/<id>]]` or `[[synthesis/<slug>]]` citation on its line (existing rule), **OR**
2. It has a footnote ref `[N]` resolving to a `[^N]: [[sources/<id>]]` definition (existing rule), **OR**
3. **(NEW)** It is the first claim sentence of a `## ` section in a page where:
   - frontmatter has `synthesizes:` with ≥2 entries
   - `## Included works` exists and mirrors `synthesizes:` exactly
   - the claim matches the *aggregate-framing-opener* pattern (`Based on the (provided sources|corpus|previous thematic analysis)`, `Across the corpus`, `Looking across`, `Aggregating across`)

The aggregate-framing pattern is a small allowlist (see `_AGGREGATE_FRAMING_OPENERS_RE` below), pinned by tests, extended only as new patterns are observed. Exemption is bounded: **only one claim per section** — the framing opener. Subsequent claims in the same paragraph still need direct citation (`[[sources/<id>]]` or `[[synthesis/<slug>]]`).

**New rule: `synthesizes:` integrity.**

For pages with `synthesizes:`:
- Every entry must exist on disk (`sources/<id>.md` for source entries, `wiki/synthesis/<slug>.md` for synthesis entries)
- `## Included works` body wikilinks must equal the `synthesizes:` frontmatter set
- Mixed types within a single `synthesizes:` list are rejected (see § 3.6)

### 3.3 New code

| Path | Purpose |
|---|---|
| `src/gateway/citations.py` | Add `_AGGREGATE_FRAMING_OPENERS_RE` allowlist (replaces M44.2's deprecated `_CITATION_DIRECTIVE` approach which didn't change NotebookLM behavior). Add `aggregate_framing_exempt(line, page_front) -> bool`. Extend `find_claim_sentences` to consult it. |
| `src/gateway/validator.py` | Add `validate_synthesizes_integrity(front, body)` — verifies frontmatter list and `## Included works` section agree. Wire into `validate_wiki_page`. |
| `src/gateway/wiki_pages.py` | Add `synthesizes` to the synthesis page schema's required fields. Add `Included works` to required sections. |
| `src/gateway/lint/citation_chains.py` | New lint scope. Traverses `synthesizes:` graph; reports dangling refs, missing `## Included works`, aggregate-framing claims on pages without `synthesizes:`, claims attempting `synthesis/` ref from a page whose own `synthesizes:` is `sources/` (mixed-tier violation). |
| `src/gateway/cli.py` | Register `citation-chains` scope for `wiki lint --scope citation-chains`. |

### 3.4 Author-side changes (orchestrator + analysis prompts)

| Path | Change |
|---|---|
| `src/gateway/research/orchestrator.py` | `_make_branch_synthesis_update` must emit `synthesizes:` (list of source IDs the branch's analysis drew from) and an `## Included works` section. For cross-cutting / shared-anchors / recurring-tradeoffs branches, `synthesizes:` enumerates the per-theme synthesis page slugs being aggregated over. |
| `src/gateway/research/analysis.py` | Update `_RECURRING_PATTERNS_PROMPT` / `_SHARED_ANCHORS_PROMPT` / `_RECURRING_TRADEOFFS_PROMPT` to instruct: opening framing sentence may aggregate across the corpus without inline citation IF the page has `synthesizes:` ≥ 2; subsequent claims must cite specific entries from `synthesizes:` (`[[sources/<id>]]` or `[[synthesis/<slug>]]` depending on tier). Drop the M44.2 footnote-ref directive — observed not to change NotebookLM behavior on framing prose. |

### 3.5 New CLI surface

```
wiki lint --scope citation-chains       # NEW M45
wiki lint --scope synthesizes-integrity # NEW M45 (or roll into citation-chains)
```

No new top-level commands. `wiki finalize` automatically enforces the M45 rules at exit-draft time.

### 3.6 Invariants (load-bearing)

1. **One-level strict typing**: a synthesis page's `synthesizes:` lists either all `sources/<id>` (first-derivative) or all `synthesis/<slug>` (second-derivative). Never mixed. Forces deliberate climbing of the tier ladder; transitive closure is computable from the graph when needed, but not encoded in individual pages.
2. **Enumeration mirrors body**: `synthesizes:` frontmatter and `## Included works` must match. The body section is the human-readable rendering of the structural enumeration; drift between them is the citation-laundering anti-pattern. Validator enforces.
3. **Aggregate exemption is bounded**: at most one framing-opener sentence per `## ` section is exempt. Subsequent claims need direct citation. Prevents the exemption from swallowing whole sections.
4. **Allowlist, not heuristic**: the aggregate-framing opener patterns are an explicit small set, pinned by tests. New patterns are added as observed (same discipline as M44.2's `_STRUCTURAL_FRAME_LABELS`).
5. **No `[[corpus]]` token**: ever. The unfollowable-aggregate anti-pattern is forbidden by design. Validator rejects `[[corpus]]` as an unknown wikilink target.

### 3.7 What this changes about M44.3

M44.3's `--draft` workflow remains valid as the *temporary* path: a research run that emits framing prose without `synthesizes:` still commits in draft mode. M45 adds the *permanent* path: a research run that emits `synthesizes:` + `## Included works` + properly-bounded framing prose can `wiki finalize` cleanly without manual citation work.

M44.2's allowlist (`_STRUCTURAL_FRAME_LABELS`) and M44.3's multi-line continuation tracking remain in force — they handle the *non-claim structural metadata* layer. M45 handles the *aggregate-claim* layer. The two are orthogonal.

---

## 4. Files plan

### New
- `src/gateway/lint/citation_chains.py`
- `tests/gateway/test_citation_chains.py`
- (sections within existing files: see § 3.3)

### Modified
- `src/gateway/citations.py` — aggregate-framing allowlist + exemption rule
- `src/gateway/validator.py` — synthesizes-integrity validator
- `src/gateway/wiki_pages.py` — synthesis schema gains `synthesizes` + `Included works`
- `src/gateway/research/orchestrator.py` — `_make_branch_synthesis_update` emits `synthesizes:` and `## Included works`
- `src/gateway/research/analysis.py` — prompt updates for aggregate-framing convention
- `src/gateway/cli.py` — register new lint scope
- `tests/gateway/test_authorship.py` — aggregate-framing exemption tests; synthesizes-integrity tests
- `tests/gateway/test_research_analysis.py` — verify new prompt directive
- `tests/gateway/test_research_orchestrator.py` — verify `synthesizes:` emission per branch
- `WIKI.md` § 3 (synthesis page schema gains `synthesizes:` field and `## Included works` section)
- `WIKI.md` § 5.2 / § 5.5 — aggregate-framing exemption rule documented; replaces M44.3's `--draft`-as-permanent-workflow paragraph
- `BUILD.md` § 10 — `### M45 — synthesizes: and the followable citation chain` entry post-delivery

### Reused (do not touch)
- M44 / M44.1 / M44.2 / M44.3 mechanisms (Haiku filter, parallel filter, structural-frame allowlist, multi-line continuation) remain in force unchanged
- `FilterClient` / `PlanClient` / `VLMClient` Protocols — untouched
- `--draft` flow — preserved as the temporary path

---

## 5. Verification

### 5.1 Unit tests

- Aggregate-framing exemption: pinned per-pattern (one test per opener regex; mirror M44.2's allowlist-pinning style)
- Aggregate-framing exemption is bounded (only first claim per section)
- Exemption only fires when `synthesizes:` ≥ 2 AND `## Included works` mirrors
- `synthesizes:` integrity: rejects dangling refs, drift between frontmatter and body, mixed-tier lists
- `[[corpus]]` token: validator rejects as unknown link target
- Orchestrator emits `synthesizes:` correctly per branch type (per-theme → `sources/<id>` list; cross-cutting → `synthesis/<slug>` list)

### 5.2 Integration / hand-test

Re-run the 2026-05-11 methodology plan **without `--draft`**. Expected:
- All 5 synthesis pages commit non-draft
- `wiki lint --scope citation-chains` reports clean for the new pages
- `wiki finalize` is a no-op (already finalized at apply_plan time)

### 5.3 Backfill (one-time)

The 5 draft pages from the M44.3 validation run (in `wiki/synthesis/2026-05-11-…`) need `synthesizes:` + `## Included works` added before they can be finalized. Two paths:
1. **Manual**: edit each draft, add the frontmatter and section, `wiki finalize`.
2. **Migration script**: a one-off `scripts/m45_backfill_synthesizes.py` that reads each draft's body, infers constituent sources from the `[[sources/<id>]]` references already present, writes `synthesizes:` and `## Included works`, then runs `wiki finalize` per page.

Recommend the migration script; pure mechanics, no judgment calls.

---

## 6. Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| NotebookLM doesn't comply with the new prompt — keeps emitting framing prose without producing the matching `synthesizes:` enumeration | Medium | Medium | Orchestrator constructs `synthesizes:` itself from the branch's known constituent sources, not from NotebookLM output. NotebookLM only writes the prose body; the structural metadata is machine-generated. |
| Aggregate-framing allowlist grows unbounded over time | Low | Low | Same discipline as M44.2: pinned test per pattern; new pattern requires test addition. Cap-by-review, not cap-by-count. |
| `synthesizes:` integrity rule trips on hand-edited pages where the user wants to revise body without touching frontmatter | Medium | Low | Validator emits a clear `synthesizes-drift` rule-name; downgraded to warning in draft mode (consistent with citation-grounding's draft treatment). |
| Backfill script mis-infers `synthesizes:` for the 5 existing M44.3 draft pages (e.g., a source is referenced but not actually a constituent) | Low | Medium | Backfill script is one-off; output reviewed manually before finalize. |
| Mixed-tier rejection feels too strict (user wants a "best of both worlds" page citing both raw sources and other syntheses) | Medium | Low | Open question (§ 7). Strict-first; relax only if real authorship hits the wall. |

---

## 7. Open questions

1. **One-level strict vs. mixed-tier `synthesizes:`** — current proposal forbids mixing `sources/<id>` and `synthesis/<slug>` in one list (§ 3.6 invariant 1). Cochrane is strict; MOC-of-MOCs naturally wants mixed. Lean strict initially; revisit if real authorship hits a wall.
2. **`wiki cite` / `wiki edit` op for hand-editing `synthesizes:` and `## Included works`** — relates to `gateway_edit_path_open_question.md` memory. M45 introduces a real use case (backfilling existing draft pages) for an LLM-or-human edit path that doesn't go through `wiki research` or `wiki ingest`.
3. **Lint warnings vs. errors for `synthesizes-drift`** — same treatment as citation-grounding (warning in draft, rejection in normal)? Or always warning since drift is recoverable?
4. **Default `synthesizes:` for non-synthesis pages** — entity / concept pages don't need this. Confirm validator only checks `synthesizes` on `type: synthesis`.

---

## 8. Out of scope

- Source ranking / weighting within `synthesizes:` (Cochrane has quality assessment via GRADE; we don't)
- `cito:` predicate typing on individual citations (interesting but heavyweight; the binary cited/uncited distinction plus the new aggregate-exemption is sufficient)
- N-derivative transitive closure baked into individual pages (§ 3.6 invariant 1)
- Replacing the `--draft` workflow (M44.3 stays as the temporary path)
- Backfilling all historical synthesis pages predating M45 — only the 5 M44.3 drafts that are currently mid-draft. Older synthesis pages stay as they are; lint surfaces them but doesn't gate.

---

## 9. Glossary

| Term | Definition |
|---|---|
| **First-derivative synthesis** | Synthesis page whose `synthesizes:` lists raw `sources/<id>`. Direct synthesis from primary sources. Strict per-source citation. |
| **Second-derivative synthesis** | Synthesis page whose `synthesizes:` lists `synthesis/<slug>` entries. Cross-cutting / shared-anchors / recurring-tradeoffs branches. Aggregate claims allowed at section openers, bounded by the enumeration. |
| **Aggregate-framing opener** | A predictable opening sentence pattern (`Based on the provided sources...`, `Across the corpus...`, etc.) that aggregates across the page's `synthesizes:` set. Exempt from per-claim citation when the enumeration is present. |
| **Citation chain** | The directed graph implied by `synthesizes:` references: `synthesis/A → [sources/x, sources/y]` and `synthesis/B → [synthesis/A, synthesis/C]`. `wiki lint --scope citation-chains` traverses it. |
| **Citation laundering** | The documented anti-pattern where an aggregate citation cannot be followed back to constituents. `[[corpus]]` would have re-introduced it. Forbidden by design. |
| **`## Included works`** | Required body section on pages with `synthesizes:`. Renders the structural enumeration as human-readable wikilinks. Validator enforces 1:1 correspondence with `synthesizes:` frontmatter. |

---

## 10. References

- Cochrane Handbook for Systematic Reviews — [ch. 14 "Completing 'Summary of findings' tables"](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14)
- PRISMA 2020 statement — [PMC8007028](https://pmc.ncbi.nlm.nih.gov/articles/PMC8007028/)
- Shotton 2010, "CiTO, the Citation Typing Ontology" — [J Biomed Semantics](https://jbiomedsem.biomedcentral.com/articles/10.1186/2041-1480-1-S1-S6); [spec](https://sparontologies.github.io/cito/current/cito.html)
- USC library guide on citation manipulation — [guides.library.sc.edu](https://guides.library.sc.edu/navigating-research-fraud/citation-manipulation)
- Andy Matuschak's working notes on note types — [notes.andymatuschak.org](https://notes.andymatuschak.org/Taxonomy_of_note_types)
- WIKI.md § 5.2 (citation grounding rule); § 5.5 (draft lifecycle)
- M44 design doc — `docs/M44-token-efficient-llm-clients.md`
- Memory: `feedback_survey_formal_practice_before_design.md` — the gating function that produced this design
