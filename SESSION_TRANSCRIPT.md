# SESSION_TRANSCRIPT.md — Design and build of the canonical knowledge base, v1

Single sustained session that took the user from "compare these two patterns" through full architectural design, schema specification, migration plan, and a working v1 of every gateway component. This document is the chronological narrative — the *why* and *how* behind each commit. Verbatim conversation transcripts are not stored; this is the load-bearing record.

**Session goal stated by the user**: review Karpathy's "LLM Wiki" gist (`442a6bf555914893e9891c11519de94f`) against the existing `~/code/research-notebook/` system; design a comprehensive knowledge management system with a simple agent interface for deep research; expand source diversity; make the KB efficiently available to agents working on `~/code/*` projects.

**Outcome**: a feature-complete personal KB at `~/code/knowledge/` with 11 commits (M0–M10), 217 passing tests, ~7,800 LOC, real hand-tests against Wikipedia / arXiv / GLP-1 vault / `claude -p` / NotebookLM CLI surface.

---

## Phase 1 — Comparative analysis

The user asked for a SWOT comparison of Karpathy's LLM Wiki pattern vs. the research-notebook acquisition pipeline given the stated use case.

**Key insight surfaced**: the two systems are *stacked layers*, not competitors. Research-notebook is a high-fidelity *acquisition pipeline* (search → semantic filter → NotebookLM corpus → Obsidian vault). The LLM Wiki is a *living-knowledge substrate* (compounding markdown wiki maintained by an agent). The current Obsidian output is a **terminal artifact**, not a living one. Migration target: keep research-notebook's strengths (multi-source search, semantic filter, NotebookLM synthesis), but invert the relationship — the wiki is canonical; everything else feeds into it.

Detailed SWOT and overlap/distinction analysis produced inline. Recommendation: adopt Karpathy's pattern as the frontend; keep research-notebook as one of several backends.

---

## Phase 2 — Architectural decisions via `AskUserQuestion`

The user requested structured walk-through. Eight foundational decisions, asked one at a time, each with options + rejected alternatives.

### Decision 1: Canonical KB location
**Locked**: single root at `~/code/knowledge/` (one canonical wiki across all `~/code/*` projects).

### Decision 2: Synthesis substrate
User clarified the tradeoffs first ("would we need to rebuild RAG?"). Honest answer surfaced: leaving NotebookLM means either accepting lower synthesis quality at hundreds-of-sources scale, or adopting `qmd`-class infrastructure (~weeks of work).

**Locked**: hybrid — wiki canonical, NotebookLM as service. Bidirectional links (wiki page → live NotebookLM artifact URL + local archive). NotebookLM dependency acceptable for now; replaceable behind the gateway interface later.

User added a hard constraint: **"I don't want to be the weak link in any workflow tying NotebookLM outputs back to the wiki."** This forced the *Discipline Gate* — architectural enforcement, not behavioral discipline.

### Decision 3: Gateway surface
**Locked**: CLI + MCP, single backend. CLI for cron/scripts; MCP for in-session Claude Code agents. Same `gateway/ops/*.py` functions; thin shims on top.

### Decision 4: Source format
User asked for technical depth and a sustainability assessment of filesystem-as-database. Answered with full directory layout, frontmatter schema, sample use cases (Substack via Web Clipper, voice memo via AirDrop), and a clear-eyed view of FS-as-DB ceilings (works to ~10k pages without changes; `qmd` handles the next ceiling without data migration).

**Locked**: markdown + YAML frontmatter, universal. Adapters become *converters*, not pipeline stages.

### Decision 5: Trigger mechanism
**Locked**: filesystem watcher daemon as primary; API-only-source pollers (Apple Notes, Notion) bolt on later via the same converter contract.

### Decision 6: Filter learning
**Locked**: versioned policy YAML + accumulating example bank (corrections pinned). Fine-tuning loop captured as roadmap (trigger ~500–1000 high-quality decisions per domain).

### Decision 7: Wiki authorship
User asked specifically about mitigating "sloppy agent work resulting in either low-fidelity output or patently incorrect source selection." Detailed mitigation stack surfaced: citation grounding rule, gateway-mediated writes, validator on every commit, plan-before-write, lookup-before-create, lint, git audit trail, hybrid routing (high-stakes → batch path).

**Locked**: hybrid authorship — agent for incremental, code for batch. Layered guardrails make malformed/unsupported output structurally impossible; substantive accuracy still requires occasional human review.

### Decision 8: Code location and repo strategy
User pushed back on initial recommendation to put gateway code in research-notebook. Cleaner answer: single repo at `~/code/knowledge/`, package `src/gateway/` (avoiding the collision with `wiki/` content directory). Research-notebook stays put as a frozen historical artifact (no archive move, no deletion).

---

## Phase 3 — Schema documents

Wrote the full contract before any code:

- **`CLAUDE.md`** (84 lines) — agent control surface. Hard rules, operation guide, when-to-use-which authorship path, forward-looking notes.
- **`WIKI.md`** (891 lines) — the conventions reference. 14 sections: architecture, directory layout, frontmatter schema, six page types with templates, citation rules + draft mode, slug conventions, index.md/log.md formats, gateway operations, filter and learning, validator rules, lint operations, NotebookLM integration, forward-looking notes including migration script path and qmd ceiling.
- **`MIGRATION.md`** (282 lines) — 6-phase legacy vault migration plan, mapping legacy slugs to canonical IDs, citation rewrite strategy, NotebookLM corpus mapping, validation/rollback gates.
- **`BUILD.md`** (529 lines) — 11-milestone gateway build plan with module responsibilities, acceptance criteria, dependencies, and 5 open decisions with recommended defaults.

User pushed back on one BUILD.md detail (citation grounding rule): added `--draft` flag escape valve. Surfaced one architectural improvement during the rewrite: avoid `src/wiki/` vs `wiki/` (content) collision by naming the package `src/gateway/`.

---

## Phase 4 — Memory updates

Project memories saved to the auto-loaded paths so future sessions in either repo retain context:

- `~/code/knowledge/`-keyed memory: `architecture_rationale.md`, `user_constraints.md`, `legacy_vault_migration_pending.md`, plus `MEMORY.md` index.
- `~/code/research-notebook/`-keyed memory: `knowledge_base_relationship.md` ("frozen historical artifact; canonical system at ~/code/knowledge/").

User caught my initial mistake of defaulting these to research-notebook's path; corrected to the canonical-system path.

---

## Phase 5 — The build (M0–M10)

Each milestone landed as a single commit on `main`. Auto mode active throughout — user said "go" or "go go go" between milestones.

### M0 — Repo bootstrap (`48a7ac3`)

- `git init`, `pyproject.toml`, `pip install -e .`, `wiki` CLI stub on PATH.
- Copied `src/filter/` and `src/search/{arxiv,youtube,normalize,queries}.py` from research-notebook (read-only — RN's working tree unchanged).
- Added "historical artifact" note to research-notebook's `CLAUDE.md` (the only mutation).
- 4 smoke tests passing.
- Caught: `tests/gateway/__init__.py` shadowed the real `gateway` package; removed it and added `[tool.pytest.ini_options]`.
- Caught: system Python is 3.9; rebuilt venv with `/opt/homebrew/bin/python3.11`.

### M1 — Gateway spine (`1939233`)

- `gateway/{paths,frontmatter,validator,locking,log,index,core}.py` and `ops/ingest.py`.
- `wiki ingest <canonical-md>` works end-to-end: validates → writes raw + wiki/sources/ → updates index.md → appends log.md, all atomically with file locking and content-hash idempotency.
- Validator subset: required core fields, type enum, ID format per WIKI § 6.1, content_hash match, balanced wikilinks, source immutability.
- Hand-test: hand-crafted YouTube-shaped source ingested cleanly; re-run was no-op; malformed input rejected with structured error.
- 30 tests passing.

### M2 — Converter framework + web converter (`1ffb11f`)

- `gateway/converters/{base,web,__init__}.py` with lazy registry and trafilatura-backed web extraction.
- `wiki ingest <substack-url>` works; local `.md` paths bypass converters.
- Refactored `ingest` into top-level dispatcher + `ingest_canonical(path)` + `ingest_url(url)` + core `_ingest_canonical_text(text)`.
- Hand-test: `https://en.wikipedia.org/wiki/Memex` end-to-end. Idempotent on second run; page-change immutability rejection works.
- 45 tests passing (15 new). Trafilatura wrappers (`_fetch`, `_extract_markdown`, `_extract_metadata`) are monkeypatchable.

### M3 — Semantic filter integration (`0c2445a`)

- `gateway/filter/{policy,examples,semantic,__init__}.py` and `gateway/ops/{filter_op,filter_correct}.py`.
- `FilterClient` Protocol; `ClaudeCLIFilterClient` shells out to `claude -p` (Max-plan auth, no API key). `StubClient` for tests.
- Filter decision is five-valued: `included`, `review`, `rejected`, `no-domain`, `skipped`, `errored`. Source always lands in raw/; wiki page gating is filter-driven.
- `wiki filter-correct` pins corrected examples with `pinned_by: user-correction`.
- Hand-test against real `claude -p` with bootstrapped GLP-1 policy.yaml: high-relevance RCT discussion → 0.95 with detailed receptor-pharmacology rationale; influencer testimonial → 0.00 with multi-criteria exclusion rationale. Filter is doing real semantic reasoning.
- 67 tests passing (22 new).

### M4 — Filesystem watcher daemon (`2d7493b`)

- `gateway/watcher.py` (WatcherDaemon with settle-debounced ingest, `raw/inbox/_failed/<ts>-<name>` quarantine, PID file + heartbeat).
- `gateway/ops/status.py` (`wiki status` reports watcher state, inbox counts, recent log entries).
- `scripts/install_watcher.sh` generates and loads `~/Library/LaunchAgents/com.knowledge.watcher.plist`.
- Hand-test: started in background, dropped a real markdown file, ingested in ~3s; malformed file went to `_failed/` with `.reason.txt`; SIGTERM produced clean shutdown logs (`events=1 ingested=1 failed=0`).
- 78 tests passing (11 new). End-to-end test runs a real `watchdog.Observer` in a thread.

### M5 — NotebookLM gateway (Discipline Gate) (`44d9195`)

- `gateway/nlm_client.py` (`NlmClient` Protocol + `NlmCLIClient` subprocess wrapper around `nlm` CLI).
- `gateway/nlm_registry.py` (`nlm/notebooks.yaml` management).
- `gateway/ops/nlm.py` (`nlm-add`, `nlm-slides`, `nlm-audio`, `nlm-briefing`, `nlm-revise`).
- Every NotebookLM artifact gets a wiki artifact page with `nlm_artifact_url` (live portal) + `local_file` (archive). Source frontmatter `nlm_corpus_ids` is the single record of corpus membership.
- Tests use `MockNlmClient` exclusively — real NotebookLM artifact creation deferred (would create real artifacts; 5–15 min each).
- 98 tests passing (20 new).

### M6 — Incremental wiki authorship + draft mode + query (`738f01f`)

- `gateway/citations.py` (wikilink parser, claim-sentence detection, density math).
- `gateway/wiki_pages.py` (six page-type schemas, Levenshtein util, `page_type_for_path`).
- `gateway/plan.py` (`Plan` / `WikiUpdate` dataclasses, JSON parser tolerant of code fences and prose, `PlanClient` Protocol with subprocess default, prompt builder).
- `gateway/ops/{apply_plan,finalize,query}.py` (atomic two-phase apply; finalize re-validates strict by stripping draft fields from a copy; query does keyword-overlap scoping + plan-driven synthesis).
- Validator extensions: `validate_wiki_page` composite, citation grounding (with draft-mode downgrade), slug Levenshtein similarity (warning at distance ≤ 2; `--force-new-slug` override).
- One bug caught and fixed during testing: `validate_wiki_page` was OR-ing the explicit `draft` parameter with `front.get("draft")`, so finalize couldn't force strict mode. Fixed by having finalize strip draft fields from a *copy* of frontmatter before validation; on-disk file keeps `draft: true` until validation actually passes.
- 134 tests passing (36 new).

### M7 — MCP server (`4cdd0be`)

- `gateway/mcp_server.py` using FastMCP. 11 `wiki_*` tools registered, each delegating to its matching `gateway/ops/*.py` function.
- `_serialize(OperationResult) → dict` makes results JSON-friendly.
- `scripts/install_mcp.sh` writes a `knowledge` entry to `~/.claude/mcp_servers.json` pointing at this repo's `.venv/bin/wiki`.
- Hand-test: `wiki mcp-serve` starts and shuts down cleanly under SIGTERM.
- 152 tests passing (18 new). Tool registration + serializer + per-tool dispatch covered.

### M8 — Legacy migration support (`54f1021`)

- `gateway/slugmap.py` (legacy source detection: video_id → `yt-<id>`, arxiv_<id>/source_type:arxiv → `arxiv-<id>` with version stripped, pmid_<id>/source_type:pubmed → `pubmed-<id>`).
- `citations.rewrite_wikilinks` (bulk rewrite preserving aliases and anchors).
- `gateway/ops/migrate.py` (vault-level orchestrator: dry-run halts after slug-map persistence; real run writes raw + wiki source pages, ports concepts/synthesis/MOCs with citation rewrite + draft flag + section backfill, logs).
- `gateway/ops/batch_ingest.py` (top-level dispatcher; M8 supports `--legacy-import`, future modes layer on).
- `migrations/0001-import-legacy-vaults.py` (3-phase script, defaults to `--dry-run`).
- Filter score conversion: legacy `relevance_score: 1-5` → canonical `filter.score: 0.0-1.0` with `policy_version: <domain>-legacy-v1`.
- Hand-test against the real GLP-1 vault (read-only dry-run): 127 sources detected (matches user's stated count), correctly typed (48 youtube + 77 pubmed + 2 arxiv), slug map written. Research-notebook untouched.
- One process slip: I accidentally ran `git add -A` in research-notebook before noticing the wrong directory; caught immediately via `git reset HEAD`. RN's working tree unchanged from session start.
- 172 tests passing (20 new).

### M9 — Lint orchestrator + 6 cheap checks + pre-commit hook (`5bb5d81`)

- `gateway/lint/{__init__,_walk}.py` and per-check modules: `orphans`, `stale_drafts`, `citation_density`, `schema_drift`, `inbox_pending`, `nlm_pending` (real); `missing_pages`, `stale_claims`, `contradictions`, `filter_calibration` (stubs).
- `gateway/ops/lint.py` orchestrator with per-check exception containment and Markdown report at `.knowledge/lint/<UTC>.md`.
- `scripts/install_pre_commit_hook.sh` rejects commits with raw `nlm <cmd>` calls in `wiki/*.md` (Discipline Gate at the git layer) or that fail `wiki lint --scope schema-drift`.
- Hand-test: `wiki lint` on the empty live wiki produced a clean report, 0 findings across all 10 checks.
- 193 tests passing (21 new).

### M10 — Remaining converters and pollers (`bebf319`)

- `gateway/converters/{youtube,arxiv,pubmed,pdf}.py`.
- `gateway/pollers/{base,apple_notes}.py` (Poller ABC with cursor read/write + raw-write helpers; Apple Notes proof-of-pattern stub).
- Ingest dispatcher extended: URLs → URL converter family; local `.md` → canonical ingest; local non-`.md` files → `ingest_file` → file converter.
- Real arXiv hand-test: `https://arxiv.org/abs/2403.05530` (Gemini 1.5 paper) ingested with full author list and abstract.
- Real PDF hand-test: synthesized 1-page PDF → `raw/pdf/<id>.md` + sidecar PDF preserved bit-for-bit.
- Voice / audiobook converters intentionally deferred (Whisper is a 2-5GB dep; needs per-env config).
- 217 tests passing (24 new).

---

## Hand-test record across the build

| Milestone | Hand-test | Result |
|---|---|---|
| M2 | `https://en.wikipedia.org/wiki/Memex` | Clean canonical markdown; idempotent re-run |
| M3 | Real `claude -p` on GLP-1 RCT discussion | Score 0.95 with mechanistic rationale citing same paper as the source |
| M3 | Real `claude -p` on celebrity testimonial | Score 0.00 with multi-criteria exclusion rationale |
| M4 | Drop file in `raw/inbox/` | Ingested in ~3s; malformed file quarantined |
| M4 | SIGTERM watcher | Clean shutdown: `events=1 ingested=1 failed=0` |
| M7 | `wiki mcp-serve` | Starts, awaits stdio, exits cleanly |
| M8 | Real GLP-1 vault dry-run | 127 sources mapped; types match expectations; RN untouched |
| M9 | `wiki lint` on empty wiki | 0 findings across all 10 checks; report written |
| M10 | `https://arxiv.org/abs/2403.05530` | Gemini 1.5 paper ingested with full abstract + 47 authors |
| M10 | Synthesized PDF | Sidecar preserved; canonical markdown extracted |

---

## Process notes worth preserving

### What worked
- Locking architecture before code (Phase 2 + Phase 3) — every milestone had clear acceptance criteria. Zero "what should this do?" mid-build moments.
- Single backend / two surfaces (CLI + MCP) — every CLI feature became an MCP tool for free at M7.
- Mocking the expensive things (`MockNlmClient`, `StubPlanClient`, `StubClient` for filter, monkeypatched trafilatura/E-utils/oEmbed) — full suite runs in 2.4s.
- Hand-testing once per milestone against a real external surface — caught what tests can't.
- One-commit-per-milestone — clean reviewable history; rollback granularity if needed.

### What was caught during build
- Test/package directory shadowing (M0 — `tests/gateway/__init__.py` masked the real package).
- Default Python being 3.9 instead of 3.11+ (M0).
- `make_source` fixture default `domains` field broke M1 tests after M3 filter integration (had to drop default to `[]`).
- "Smoke test asserts X is a stub" pattern broke when X got implemented; updated three times across M3/M6/M9 to a still-stub command.
- M6 validator OR-ing `draft` parameter with `front.get("draft")` — finalize couldn't force strict; fixed by stripping fields from a copy.
- Legacy arXiv `authors: [{"name": ...}]` (dict-with-name) crashed `", ".join(...)`; added `_coerce_authors` helper.
- Accidentally ran `git add -A` in research-notebook (instead of knowledge); caught immediately via `git reset HEAD`.

### User constraints that drove decisions
- "Don't degrade the fidelity of the semantic filter" (M3 design)
- "I don't want to be the weak link" (M5 Discipline Gate, M9 pre-commit hook)
- "No limitations on source content" (M2/M10 universal converter contract)
- "Bidirectional NotebookLM linking" (M5 artifact pages with both local file and live URL)
- "Research-notebook stays as historical artifact, never retired" (M0/M8 read-only access only)
- "Architectural decisions warrant consultation before implementation" (Phase 2 — eight `AskUserQuestion` walks)

---

## Final state

- 11 commits on `main`: `48a7ac3` → `bebf319`
- 217/217 tests pass in 2.4s
- ~7,800 LOC under `src/gateway/`
- 4 planning docs (CLAUDE.md, WIKI.md, MIGRATION.md, BUILD.md) totaling ~1,800 lines
- 3 install scripts (watcher, MCP, pre-commit hook)
- 1 migration script (defaults to `--dry-run`)
- Project memories saved at the canonical-system path

The user invoked `/loop`-style "go" / "go go go" between milestones in auto mode; the session ran from architectural exploration to feature-complete v1 in a single continuous arc.
