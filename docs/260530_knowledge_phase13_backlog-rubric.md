# Knowledge Phase 13 Backlog Rubric — 2026-05-30

## § 1 — Current state vs. build plan

**Knowledge: Phase 13 (unwritten scope) — 7 untracked deliverables shipped since Phase 12 exit; synthesizes-coverage regression at 304 ERRORs**

Phase 12 closed cleanly at `3a76920` (M111+M112). Since then, a substantial amount of work has shipped outside the formal milestone plan: `convergent-ai-brain` domain bootstrapped with two research harvests (H1a/H1b), discoverability surface (`wiki list-domains`, `list-concepts`, `moc-add` + 5 curated MOC pages), discharge-orphans parallelization (4× speedup), `entity_kind` vocab expansion, and 700+ synthesis drafts across three domains. The skew is the same pattern Phase 12 rubric flagged: high operational throughput with a worsening lint signal. The synthesizes-coverage ERROR count grew 74 → 304 since the rubric was written, and the wiki-page orphan count is *higher* now (726) than when discharge began (~589), because new synthesis pages generate no inbound MOC links. Running the orphan-discharge operation is making the orphan metric worse.

---

## § 2 — Unshipped items, bucketed

| Bucket | Items | Count |
|---|---|---|
| **Lint regression** | `synthesizes-included-works-drift` 304 ERRORs (was 74 at Phase 12 rubric, 0 at Phase 10 exit) | 304 pages |
| **Orphan wave** | wiki-page orphan count 726 (up from ~589 at Phase 12 exit despite 700+ discharge runs — synthesis pages are themselves orphaned) | 726 pages |
| **Code quality — gateway gaps** | `wiki nlm-register` CLI (YAML-edit workaround used twice); `NoteConverter` for `.md`/`.txt` (pandoc workaround used 4× this week); `_build_inbound_index` self-citation exclusion | 3 items |
| **Untracked deliverables** | `convergent-ai-brain` (3 commits), `discoverability` features (1 commit), `perf(discharge-orphans)` (1 commit), `feat(ont4)` (1 commit), `feat(wikiloom)` (1 commit) — not logged in BUILD.md | 7 items |
| **Operational — finalize** | ~460 escalated drafts; no auto-appliable suggestions (no source backing for researcher entities) | ~460 items |
| **Operational — schema drift** | ~208 items (entity_kind, slug length, canonical_name) | ~208 items |
| **Operational — edge-ai notebook** | ~15 YouTube sources permanently `RESOURCE_EXHAUSTED` on edge-ai notebook; same IDs fail every round; domain effectively blocked | ~15 stuck sources |
| **L-effort roadmap** | QUAL-8 (citation coherence judge), ARCH-12 (second NLM backend), ONT-1 (1000 reclassifications), ONT-15 (synthesizes rename) | 4 items |

---

## § 3 — Phase exit criteria

Phase 13 has no formally written criteria. Derived from Phase 12 carry-forward and the current regression:

- ✗ `wiki lint --scope synthesizes-coverage` returns 0 ERRORs — 304 ERRORs; worsened significantly since Phase 12 rubric (74 → 304); root cause unconfirmed (discharge pages don't have `synthesizes:` frontmatter per `query.py`, so the source is likely research-workflow pages from `convergent-ai-brain` harvests or prior sessions)
- ✗ Wiki-page orphan count trending downward — 726 now vs ~589 at Phase 12 exit; discharge is generating orphaned synthesis pages faster than MOC linking can absorb them
- ✓ `wiki evaluate --all-domains` clean — all 4 domains scoring (ai-native=0.942, edge-ai=0.697, condo=0.632, glp1=0.538)
- ✗ BUILD.md reflects shipped work — 7 commits since Phase 12 exit not logged (convergent-ai-brain, discoverability, perf/ont4/wikiloom fixes)
- ✗ edge-ai discharge unblocked — ~15 YouTube sources permanently failing; no fix attempted

---

## § 4 — Rubric for backlog decisions

Refining Phase 12 rubric (3 days old, <7 days). Dimensions 1–5 unchanged:

1. **Does it change daily operational outcomes?** Scheduled agents and monitors compound permanently.
2. **Is the bottleneck engineering or human judgment?** Per-domain calibration, per-page LLM review are human-bottlenecked.
3. **Is effort proportionate to the actual use case?** L-effort items need a concrete forcing function.
4. **Are dependencies satisfied?** Items blocked on things that have since shipped should be re-evaluated.
5. **Does it restore eval signal fidelity for a structurally ceilinged domain?** Validated by M103.

**Candidate Dim 6 — not yet adopted:** *Does it close the loop between discharge volume and the lint/orphan metrics it generates?* Discharge-orphans now runs at scale (700+ drafts), but the operation inverts the metrics it's meant to improve: orphan count goes up because synthesis pages have no inbound MOC links; synthesizes-coverage count may be driven by research-workflow pages that lack `## Included works`. A closed-loop design would auto-link synthesis pages into their domain MOC on creation. This surfaces because the pattern has now recurred across 3 separate discharge sessions.

---

## § 5 — Applying the rubric

| Item | Bucket | Trigger to revive | Rubric reason |
|---|---|---|---|
| Root-cause `synthesizes-included-works-drift` 304 ERRORs | Lint regression | **Active** — 304 ERRORs is a noisy daily signal; was 0 at Phase 10 exit | Dim 1: lint noise drowns real regressions; S-effort diagnosis (grep `synthesizes:` in pages failing the check, confirm source) |
| Auto-link synthesis pages into domain MOC on creation | Orphan wave | **Active** — orphan count inverting; candidate Dim 6 | Dim 1: compounding; each discharge run adds ~20 orphaned pages; S-effort in `query.py` to append slug to domain MOC |
| Log untracked deliverables in BUILD.md | Untracked deliverables | **Active** — 7 commits since Phase 12 exit unlogged; plan is diverging from reality | Dim 1: BUILD.md is the project's audit trail; inaccurate plan erodes future rubric reliability |
| Diagnose edge-ai RESOURCE_EXHAUSTED sources | Operational — edge-ai | **Active** — ~15 sources permanently failing; edge-ai notebook blocked | Dim 4: unblocks a domain; S-effort (check if sources need re-sync to notebook or have been removed by YouTube) |
| `wiki nlm-register <domain> <notebook_id>` CLI | Code quality | Third manual YAML edit on the same path | Dim 1: low but recurrence is the trigger; S-effort |
| `NoteConverter` for `.md`/`.txt` | Code quality | Next cross-project ingest with local markdown | Dim 1: recurring friction; S-effort |
| `_build_inbound_index` self-citation exclusion | Code quality | Stale draft spared by self-citation observed | Dim 3: no confirmed failure; defer |
| ~460 escalated finalize-batch drafts | Operational — finalize | Source ingestion sprint for researcher entity pages | Dim 2: human-bottlenecked (source ingestion); engineering fully unblocked |
| Schema-drift ~208 | Operational — schema | User editorial sprint; entity_kind errors spike above 100 | Dim 2: human-judgment calls |
| QUAL-8, ARCH-12, ONT-1, ONT-15 | L-effort roadmap | Concrete failure or external forcing function | Dims 2+3: L-effort, no current forcing function |

---

## § 6 — Proposed next-phase scope

Session state (`docs/session-state.md`) records "resume discharge-orphans on condo + glp1 + ai-native; R3 retry; iOS Shortcut" as next steps. This is correct as far as it goes but understates the lint/orphan regression — those are now the Phase 13 gate items, not optional polish. The right frame for Phase 13 is: close the discharge loop (fix the metrics that discharge worsens), then continue discharge at scale.

| Item | Effort | Rationale |
|---|---|---|
| Root-cause synthesizes-coverage 304 ERRORs | S | Gate item: confirms whether discharge or research pages are the source; fix is template change or `## Included works` backfill |
| Auto-link synthesis pages into domain MOC on `query()` creation | S | Closes the orphan loop; every discharge run currently adds orphans |
| Log 7 untracked deliverables in BUILD.md | S | Plan integrity; inaccurate BUILD.md breaks future checkpoints |
| Diagnose edge-ai RESOURCE_EXHAUSTED (try notebook re-sync or source removal) | S | Unblocks the domain; low-risk diagnostic |
| `wiki nlm-register` CLI | S | Third recurrence; S-effort |

**Phase 13 exit criteria:**
- `wiki lint --scope synthesizes-coverage` returns 0 ERRORs (or root cause documented with explicit deferral)
- Wiki-page orphan count trending downward across two consecutive discharge sessions
- BUILD.md delivery log current through all shipped work
