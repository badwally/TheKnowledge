# Semantic-Models Research Loop — Execution Plan

**Created:** 2026-06-17
**Domain:** `semantic-models` (bootstrapped + tuned this session)
**Mode:** Autonomous multi-stream loop, auto-mode on.

## Objective

Build an authoritative reference corpus for the **modeling + architecture core**
of semantic data models. Scope locked with the user:

- **In scope:** knowledge-representation formalisms (RDF/RDFS/OWL/description
  logics/property graphs/conceptual modeling), ontology engineering, knowledge
  graphs (construction/storage/query/reasoning), semantic layers & enterprise
  semantic architecture.
- **Altitude:** foundations → implementation (W3C/ISO specs + formal theory +
  reference architectures + tooling/vendor docs + engineering practice). Not
  gated on academic peer-review rigor.
- **Deferred to sibling domains (NOT this filter):** corpus development &
  licensing; the agentic application layer (how agents consume/produce semantic
  structures at runtime). The agentic thread is the intended first sibling once
  this core corpus exists.

## Adapter set

`arxiv, web (Firecrawl), youtube, semantic_scholar, local`. **pubmed excluded**
(slow E-utilities; zero biomedical relevance). Exclusion is belt-and-suspenders:
the query planner emits `pubmed: []` from the policy, and we additionally strip
`pubmed` from `target_counts` in every plan YAML before `--execute`.

## Throttle strategy (over-saturation guards)

- `--max-results 12` per adapter (default 50). Caps per-adapter aggregate fetch.
- `WIKI_FILTER_MAX_WORKERS=4` (default 8) — eases filter-LLM concurrency.
- **Trim each stream's plan to ~5–6 in-lane sub-queries per adapter** (the planner
  over-generates ~15–20 broad ones). Keeps streams non-overlapping and cuts
  adapter calls ~3×.
- Adapter concurrency is per-adapter (each runs its sub-queries *sequentially*
  with its own throttle: S2 1.1s interval/4 retries; arxiv 3s backoff; youtube
  inter-query sleep + quota-aware backoff). Risk is moderate, not parallel-per-query.
- Run `--execute` **in the background** and monitor — the full pipeline (fan-out →
  filter → convert → NLM index → synthesis) exceeds a single 10-min Bash timeout.
- **On adapter rejection (429/403):** re-run that stream's `--execute` after a
  cooldown, or trim the offending adapter's sub-queries further. S2 was IP-throttling
  earlier (transient) — arxiv covers the academic core if S2 stays down.
- Corpus-quality gate left at defaults (`RESEARCH_CORPUS_MIN_MEDIAN=300`,
  `SPARSE_FRAC=0.60`) — keep the sparse-corpus safety floor active.

## Streams (pillar-decomposed)

Each stream = one `wiki research` session = one NLM notebook = one synthesis page
(filed `--draft`), plus its accepted source pages.

### Stream 1 — Formalisms & knowledge representation
Top query: foundational formalisms — RDF/RDFS/OWL stack & OWL profiles; description
logics (expressivity/decidability/complexity); property-graph vs RDF (RDF-star/RDF
1.2, ISO GQL); conceptual/logical modeling lineage (ER/UML); formalism-selection
criteria. Specs + foundational DL/Semantic-Web sources + practitioner RDF-vs-LPG
comparisons.

### Stream 2 — Ontology engineering
Top query: production-quality ontology engineering — methodologies (METHONTOLOGY,
NeOn, SAMOD, competency-question-driven); design patterns & anti-patterns;
modularization & reuse; alignment/matching (OAEI, precision/recall); upper
ontologies (BFO/DOLCE/SUMO/gist); lifecycle/versioning/governance.

### Stream 3 — Knowledge graphs
Top query: KG architecture & engineering — construction (R2RML/RML, text
extraction); storage (triple stores vs native LPG DBs, indexing/scaling); query
languages/engines (SPARQL 1.1, Cypher, ISO GQL); reasoning at scale
(materialization vs query-rewriting, OWL-profile reasoners); embeddings;
validation (SHACL/ShEx).

### Stream 4 — Semantic layers & enterprise semantic architecture
Top query: semantic modeling as enterprise architecture — semantic/metrics layer
(universal semantic layer, headless BI, dbt SL, Cube, AtScale) vs formal
ontologies; linked-data publishing & schema.org; data-fabric/data-mesh semantics
(KG-backed metadata, active metadata, canonical data models); semantic integration
patterns; where RDF/OWL meets pragmatic enterprise modeling.

## Per-stream recipe

1. `wiki research "<top query>" --domain semantic-models --review` → plan YAML.
2. Edit the YAML: strip `pubmed` from `target_counts`; trim each adapter's
   `queries:` to ~5–6 in-lane sub-queries.
3. `WIKI_FILTER_MAX_WORKERS=4 wiki research --execute <session-id> --max-results 12`
   in the **background**; monitor.
4. **Check work:** scan logs for `step=corpus_quality`, convert-failure rate,
   `step=index_settle` (`distinct_sources`), AdapterError (429/403). Re-run
   adapter/stream with adjusted throttle if rejected.
5. Verify pages filed (`wiki status`, `git status` on wiki/sources + wiki/synthesis).
6. Commit (staging hygiene: never `git add -u wiki/`; stage this stream's files by
   content match + the session artifacts) + checkpoint `docs/session-state.md`.
7. Next stream.

## Completion criteria

All 4 streams executed; each has accepted source pages + a filed synthesis draft;
corpus-quality/convert/index_settle checked per stream; commits + session-state
checkpoints landed. Stale-draft finalize (`wiki cite` + `wiki finalize`) and an
optional domain MoC are follow-ups, not part of this loop's completion.

## Staging discipline (from prior multi-stream work)

Working tree carries a pre-existing condo/orita backlog of modified+untracked
wiki pages — **leave alone**. Stage ONLY this loop's files explicitly: the
session's new `raw/` + `wiki/sources/` + `wiki/synthesis/` pages, the plan YAMLs,
`.knowledge/policies/semantic-models/`, this plan doc, `index.md`, `log.md`,
`docs/session-state.md`.
