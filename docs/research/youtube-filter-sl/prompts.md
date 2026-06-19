# YouTube filter supervised-improvement — 12 research prompts

**Domain:** `semantic-models`
**Split:** 8 train / 4 validate (validate held out from all tuning — spec §5, §9).
**Date:** 2026-06-19

Each prompt below is a research question over a `semantic-models` subtopic, paired
with the `youtube:` queries used to surface candidates. Queries are authored in the
**institution / conference / researcher-anchored register** (KGC, ISWC, ESWC,
Connected Data London, VLDB, NeurIPS, named researchers) because the semantic
filter scores pre-fetch metadata — the query must surface authoritative talks, not
tutorials ([[feedback_filter_source_type_awareness]]).

The machine-readable query files are `queries-train.yaml` (these 8) and
`queries-validate.yaml` (the 4 held-out). To cross-check against the live planner,
run `wiki research "<prompt>" --domain semantic-models --review` (writes the query
plan only — no fan-out) and compare the emitted `youtube:` queries; the hand-authored
set is the authority for this exercise so the pool is reproducible.

---

## Train (8) — used to derive filter/prompt improvements

### T1 — KG construction
**Prompt:** What are the dominant architectures and engineering practices for constructing knowledge graphs at scale, and how do construction pipelines differ across enterprise and research settings?
**Queries:** see `kg-construction` in queries-train.yaml.

### T2 — Query languages & engines
**Prompt:** How do graph query languages (SPARQL, Cypher, GQL) and their execution engines differ in design, and what drives query-engine performance over large graphs?
**Queries:** see `query-languages-engines`.

### T3 — Reasoning & inference
**Prompt:** What reasoning and inference capabilities do description logics and OWL provide over knowledge graphs, and what are the practical limits of automated reasoning engines?
**Queries:** see `reasoning-inference`.

### T4 — SHACL / shape validation
**Prompt:** How are shape-based constraint languages (SHACL, ShEx) used to validate and govern the quality of RDF knowledge graphs?
**Queries:** see `shacl-shape-validation`.

### T5 — Storage architectures
**Prompt:** How are triplestores and graph databases architected internally, and what storage-engine choices govern the scalability of knowledge graphs?
**Queries:** see `storage-architectures`.

### T6 — KG embeddings
**Prompt:** What are the major families of knowledge-graph embedding models, and how is graph representation learning applied to link prediction and downstream tasks?
**Queries:** see `kg-embeddings`.

### T7 — Ontology engineering methodologies
**Prompt:** What methodologies guide the engineering of ontologies (e.g. NeOn, competency-question-driven development), and how is the development process structured?
**Queries:** see `ontology-engineering-methodologies`.

### T8 — The semantic layer
**Prompt:** What is the modern "semantic layer" in data architecture (metrics layer, headless BI), and how does it relate to ontologies and knowledge graphs?
**Queries:** see `semantic-layer`.

---

## Validate (4) — HELD OUT; never used for tuning

### V1 — Ontology design patterns
**Prompt:** What are ontology design patterns (content patterns, ODPs), and how are they reused to build well-structured ontologies?
**Queries:** see `ontology-design-patterns` in queries-validate.yaml.

### V2 — Alignment & matching
**Prompt:** How are ontology alignment and schema matching performed to integrate heterogeneous knowledge graphs (e.g. OAEI techniques)?
**Queries:** see `alignment-matching`.

### V3 — Upper / foundational ontologies
**Prompt:** What role do upper/foundational ontologies (BFO, DOLCE, UFO) play, and how do they constrain and ground domain ontologies?
**Queries:** see `upper-foundational-ontologies`.

### V4 — OBDA / virtual knowledge graphs
**Prompt:** How does ontology-based data access (OBDA) expose relational data as a virtual knowledge graph, and what is the role of mappings (e.g. Ontop)?
**Queries:** see `obda-virtual-kg`.
