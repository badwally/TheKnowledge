# BUILD.md — Gateway build plan

Decomposition of the gateway implementation into reviewable milestones with module responsibilities. Pair with `WIKI.md` (canonical schema), `CLAUDE.md` (agent control surface), and `MIGRATION.md` (legacy migration plan).

This is a planning artifact. Each milestone is a reviewable, mergeable unit of work that delivers a working slice. No code is written until this plan is approved.

## Table of contents

1. Approach
2. Where the code lives
3. Module layout
4. Milestone overview
5. Milestone details (M0–M10)
6. Cross-cutting concerns
7. Dependencies and packaging
8. Open decisions

---

## 1. Approach

**Smallest safe step at every milestone.** Each milestone is independently mergeable, leaves the system in a working state, and unlocks a specific user-facing capability. No milestone is so large it can't be reviewed in one sitting.

**Build the spine first; layer features.** M1 establishes the Gateway/Validator/Log/Index spine on a single `wiki ingest` operation. Every subsequent milestone adds capabilities by extending the spine, not rebuilding it.

**Validate fidelity early.** The semantic filter (M3) and NotebookLM gateway (M5) come before the convenience layers (incremental authorship, MCP, lint, migration). Both are user-flagged high-leverage components — proving them early de-risks the rest.

**Migration is downstream.** Migration support (M8) layers on a stable gateway. The gateway gets exercised on hand-crafted sources during M1–M7; M8 turns the migration into a thin script.

**No new abstractions for hypothetical futures.** YAGNI governs scope. Each module has a single concrete responsibility. Premature interface design is a risk; we pay the cost when a second concrete need shows up, not before.

## 2. Where the code lives

Single repository at `~/code/knowledge/`. Code, content, planning docs, tests, scripts, and migrations all live in one git repo with one Python project. The same pattern as the existing research-notebook repo (`src/` + `data/` together), applied to the new system.

**Code package**: `src/gateway/`. The implementation of the gateway, validator, converters, watcher, MCP server, and operations.

**CLI**: `wiki` (user-facing command, installed via `pip install -e .`). The package implementing it is named `gateway` to avoid collision with the content directory `wiki/`.

**Content layer**: `raw/`, `wiki/`, `nlm/`, `index.md`, `log.md`, `.knowledge/` — all at the top level of the same repo. The gateway operates on these via absolute paths resolved through `gateway/paths.py`.

**Research-notebook is preserved as a historical artifact.** It stays at `~/code/research-notebook/` indefinitely as a frozen reference — git history, design specs, original pipeline code, legacy data vaults all kept intact. The migration script (M8) reads from research-notebook's `data/obsidian*/` and `data/staged/` paths but never writes to them. After M8 lint passes clean, research-notebook receives no further changes.

This implies: still-useful modules (`src/filter/`, `src/search/{arxiv,pubmed,youtube}.py`) are **copied** into `~/code/knowledge/src/gateway/` during M0, not moved. The copies are refactored to fit the canonical schema (policy.yaml, example bank, frontmatter contract). The originals stay in research-notebook unchanged.

## 3. Module layout

```
~/code/knowledge/
├── CLAUDE.md, WIKI.md, MIGRATION.md, BUILD.md, README.md
├── pyproject.toml, .venv/, .git/
├── src/
│   └── gateway/
│       ├── __init__.py
│       ├── cli.py               # `wiki <subcommand>` entry point
│       ├── core.py              # Gateway class — orchestrates every op
│       ├── paths.py             # KNOWLEDGE_ROOT resolution and well-known subpaths
│       ├── frontmatter.py       # YAML frontmatter parse/validate/mutate
│       ├── validator.py         # WIKI.md § 11 rules as composable functions
│       ├── citations.py         # parse [[wikilinks]], resolve, rewrite, density
│       ├── slugmap.py           # source-type detection, ID generation, similarity
│       ├── locking.py           # file locks under .knowledge/locks/
│       ├── log.py               # log.md append + read API
│       ├── index.py             # index.md rebuild + incremental update
│       ├── filter/              # semantic filter (copied + refactored from research-notebook)
│       │   ├── __init__.py
│       │   ├── policy.py        # canonical policy.yaml loader
│       │   ├── examples.py      # example bank manager
│       │   └── semantic.py      # filter call; loads policy + examples
│       ├── ops/                 # one module per gateway operation
│       │   ├── __init__.py
│       │   ├── ingest.py
│       │   ├── batch_ingest.py
│       │   ├── query.py
│       │   ├── filter_op.py
│       │   ├── nlm.py           # nlm-add, nlm-query, nlm-slides, nlm-audio, nlm-briefing, nlm-revise
│       │   ├── finalize.py
│       │   ├── lint.py
│       │   ├── search.py
│       │   ├── status.py
│       │   ├── filter_correct.py
│       │   └── migrate.py       # --legacy-import + slug map orchestration
│       ├── converters/          # input → canonical markdown
│       │   ├── __init__.py      # registry; dispatches by detected type
│       │   ├── base.py          # Converter ABC
│       │   ├── web.py
│       │   ├── youtube.py       # uses _search/youtube.py for transcript fetch
│       │   ├── arxiv.py         # uses _search/arxiv.py for abstract fetch
│       │   ├── pubmed.py        # uses _search/pubmed.py for abstract fetch
│       │   ├── pdf.py
│       │   ├── voice.py
│       │   └── _search/         # API helpers copied from research-notebook
│       │       ├── arxiv.py
│       │       ├── pubmed.py
│       │       └── youtube.py
│       ├── nlm_client.py        # subprocess wrapper around `nlm` CLI
│       ├── watcher.py           # filesystem watcher daemon (raw/inbox/)
│       ├── mcp_server.py        # MCP surface — delegates to gateway ops
│       └── pollers/             # API-only-source pollers (M10+)
├── tests/
│   └── gateway/
│       ├── fixtures/
│       ├── test_ingest.py
│       ├── test_validator.py
│       ├── test_filter_integration.py
│       ├── test_nlm.py
│       ├── test_migration.py
│       └── ...
├── scripts/
│   └── install_watcher.sh       # generates and loads launchd plist
├── migrations/
│   └── 0001-import-legacy-vaults.py
├── index.md, log.md             # content layer begins here
├── raw/
│   ├── web/, youtube/, arxiv/, pubmed/, pdf/, voice/, audiobook/, note/, inbox/
├── wiki/
│   ├── entities/, concepts/, sources/, synthesis/, mocs/, artifacts/
├── nlm/
│   └── notebooks.yaml
└── .knowledge/
    ├── policies/                # editorial policies per domain (with example bank)
    ├── locks/                   # file locks for concurrency safety
    ├── lint/                    # lint reports
    └── migrations/              # slug maps and migration audit trails
```

## 4. Milestone overview

| # | Milestone | User-facing capability | Blocked by |
|---|---|---|---|
| M0 | Repo bootstrap | git repo, pyproject, `wiki` CLI on PATH (no-op stub), filter/search modules copied from research-notebook | — |
| M1 | Gateway spine | `wiki ingest <canonical-markdown>` writes to raw/ + wiki/sources/, updates index.md, logs to log.md | M0 |
| M2 | Converter framework + web converter | `wiki ingest <substack-url>` ingests via readability extraction | M1 |
| M3 | Semantic filter integration | Ingest runs filter; populates filter: block; gates wiki-authorship by threshold | M1 (M2 helpful) |
| M4 | Filesystem watcher | Drop a markdown file in raw/inbox/, it gets ingested automatically | M1 |
| M5 | NotebookLM gateway | `wiki nlm-add`, `wiki nlm-slides`, `wiki nlm-audio`, `wiki nlm-briefing`, `wiki nlm-revise` — all atomically file artifacts back as wiki pages with bidirectional links | M1 |
| M6 | Incremental wiki authorship | `wiki ingest` updates entity/concept/synthesis pages via agent-driven authorship; plan-before-write, citation grounding, draft mode all enforced | M1, M3 |
| M7 | MCP server | All gateway operations available as native Claude Code tools alongside CLI | M1 (more useful after M5/M6) |
| M8 | Migration support | `wiki batch-ingest --legacy-import <vault>` runs MIGRATION.md phases | M1, M3, plus youtube/arxiv/pubmed converters |
| M9 | Full lint pass | `wiki lint` runs all 9 checks; report at .knowledge/lint/ | M1, M5, M6 |
| M10 | Remaining converters and pollers | voice, audiobook, pdf converters; future API-only pollers (Apple Notes, Notion) bolt on via the same converter contract | M2 |

Milestones M1–M5 should land before M6–M10. Within those bands, M3 and M5 are the highest-fidelity validations.

## 5. Milestone details

### M0 — Repo bootstrap

**Goal.** A new git repo at `~/code/knowledge/` with a working Python project skeleton. `wiki` CLI on PATH (stub: prints "not yet implemented" for every subcommand). Still-useful modules from research-notebook copied into the new package layout. No data moved; research-notebook untouched.

**Tasks.**

- `git init` at `~/code/knowledge/`. Initial commit captures the existing planning docs (`CLAUDE.md`, `WIKI.md`, `MIGRATION.md`, `BUILD.md`).
- Create `~/code/knowledge/.venv/` and activate.
- `pyproject.toml` with `[project.scripts] wiki = "gateway.cli:main"` and basic dependency list (yaml, pytest).
- `pip install -e .` so `wiki` is on PATH.
- `src/gateway/__init__.py`, `src/gateway/cli.py` (argparse stub with subcommands listed; each prints "not yet implemented").
- Copy `~/code/research-notebook/src/filter/` → `~/code/knowledge/src/gateway/filter/`. Light refactoring to fit the canonical policy.yaml schema (defer real policy loader to M3).
- Copy `~/code/research-notebook/src/search/{arxiv.py,pubmed.py,youtube.py}` → `~/code/knowledge/src/gateway/converters/_search/`. Used as helpers by converters in M2/M8.
- Add `~/code/research-notebook/CLAUDE.md` note: this codebase is now a frozen historical artifact; active development is at `~/code/knowledge/`.
- Initial pytest config; `tests/gateway/test_smoke.py` confirms `wiki --version` runs.

**Acceptance criteria.**

- `which wiki` resolves to the new venv binary.
- `wiki --help` lists all planned subcommands (per BUILD.md table).
- `pytest tests/gateway/` passes (smoke test only).
- Research-notebook `git status` clean — no changes there.
- `git log` in `~/code/knowledge/` shows initial commits.

**Out of scope.** Any actual gateway logic. M0 is pure scaffolding.

**Estimated scope.** ~150–250 LOC + smoke tests.

---

### M1 — Gateway spine

**Goal.** A working `wiki ingest <path-to-canonical-markdown>` that validates, writes, logs, and indexes — proving the architectural pattern end-to-end on a hand-crafted source.

**Modules.**

- `gateway/cli.py` — argparse-based CLI; `ingest` subcommand wired to real implementation.
- `gateway/core.py` — `Gateway.execute(operation, args)` implements the WIKI.md § 9.2 contract (validate input, lock, execute, validate output, write atomically, update backlinks, log, release lock, return).
- `gateway/paths.py` — `KNOWLEDGE_ROOT = Path(os.environ.get("KNOWLEDGE_ROOT", Path.home() / "code" / "knowledge"))`; subpath constants.
- `gateway/frontmatter.py` — `parse(text) -> (frontmatter, body)`, `serialize(frontmatter, body) -> text`, `validate_against_schema(frontmatter, type)`.
- `gateway/validator.py` — initial subset: required core fields (§ 11.1), source immutability check (§ 11.5), well-formed wikilinks (cheap subset of § 11.2). Citation grounding and Levenshtein checks deferred to later milestones.
- `gateway/locking.py` — `with file_lock(path): ...` context manager.
- `gateway/log.py` — `append(op, fields, summary)` writes a § 8 entry to `log.md`.
- `gateway/index.py` — `rebuild()` and `update_for(path)`; M1 only does `update_for` (single source added); `rebuild` deferred.
- `gateway/ops/ingest.py` — orchestrates: parse input → write `raw/<type>/<id>.md` → write `wiki/sources/<id>.md` summary page → return.

**Acceptance criteria.**

- `wiki ingest tests/gateway/fixtures/sample-canonical.md` succeeds: raw file copied, source page written, index.md updated, log.md appended.
- Re-running on the same file is a no-op (content_hash idempotency).
- Validator rejection on malformed frontmatter halts the operation with a structured error; no partial writes.
- `pytest tests/gateway/test_ingest.py` passes (5–10 tests covering happy path, malformed frontmatter, content-hash idempotency, lock contention).

**Out of scope.** Converters, filter integration, watcher, NotebookLM, agent-driven page updates beyond source page, full lint, MCP server, migration.

**Estimated scope.** ~500–800 LOC, ~100–200 LOC tests.

---

### M2 — Converter framework + web converter

**Goal.** `wiki ingest https://example.substack.com/p/article` works via readability-style extraction, producing canonical markdown in `raw/web/`.

**Modules.**

- `gateway/converters/__init__.py` — `register(converter)`, `dispatch(input) -> Converter` (selects by URL pattern, file extension, or explicit `--type` flag).
- `gateway/converters/base.py` — `Converter` ABC: `detect(input) -> bool`, `convert(input) -> Path` (returns path to canonical markdown written to `raw/<type>/`).
- `gateway/converters/web.py` — uses `trafilatura` or `readability-lxml` for content extraction; produces frontmatter (URL, title, authors via meta tags, published_at, content_hash) + body.
- `gateway/ops/ingest.py` — extended: if input is not already in raw/, dispatch to a converter first; converter writes to raw/, then ingest proceeds as in M1.

**Acceptance criteria.**

- `wiki ingest <substack-url>` produces a canonical markdown file in `raw/web/` and a wiki source page.
- `wiki ingest /path/to/clipped-article.md` (already canonical) bypasses converters.
- Content extraction is faithful (test against 5 real URLs in test fixtures).
- `pytest tests/gateway/test_converters_web.py` passes.

**Out of scope.** Other source types (deferred to later milestones).

**Estimated scope.** ~300–400 LOC + tests.

---

### M3 — Semantic filter integration

**Goal.** Every ingest runs the semantic filter against the source frontmatter + body head, populates the `filter:` frontmatter block, and gates wiki-page creation by `threshold_include`. Below `threshold_review`, the source stays in `raw/` with rationale; above the threshold, ingest proceeds to wiki.

**Modules.**

- `gateway/filter/policy.py` — refactored from research-notebook copy: load `.knowledge/policies/<domain>/policy.yaml` (canonical schema per WIKI.md § 10.1).
- `gateway/filter/examples.py` — NEW: `load_examples(domain, count, strategy) -> list[Example]`, `pin_example(domain, source_id, decision, rationale)`, `prune(domain, max_count)`.
- `gateway/filter/semantic.py` — refactored: `score(frontmatter, body, domain) -> FilterResult` constructs prompt from policy + examples, calls Claude, parses response.
- `gateway/ops/filter_op.py` — `wiki filter <path> [--domain <slug>]` for ad-hoc scoring (read-only, no wiki write).
- `gateway/ops/filter_correct.py` — `wiki filter-correct <source-id> --include|--exclude --rationale "..."` updates source frontmatter and pins the corrected example.
- `gateway/ops/ingest.py` — extended: after converter, before wiki-page creation, run filter; populate frontmatter `filter:` block; if score below threshold, halt before wiki write.

**Acceptance criteria.**

- `wiki ingest <url>` for a high-relevance source results in `filter.score >= threshold_include`, source page in `wiki/sources/`, source frontmatter has `filter:` populated.
- `wiki ingest <url>` for a low-relevance source results in `filter.score < threshold_review`, raw/ file persisted with rationale, no wiki page written.
- `wiki filter-correct <id> --include` flips the decision, pins example, updates frontmatter.
- Example bank persists across runs (re-running ingest on a different source uses the bank).
- `pytest tests/gateway/test_filter_integration.py` passes (4–8 tests).

**Out of scope.** Fine-tuning loop (per WIKI.md § 10.4 roadmap; not v1).

**Estimated scope.** ~400–600 LOC + tests. Reuses copied filter logic from research-notebook substantially.

---

### M4 — Filesystem watcher

**Goal.** A drop in `raw/inbox/` triggers ingest within seconds. macOS launchd daemon.

**Modules.**

- `gateway/watcher.py` — uses `watchdog` (Python) for filesystem events. On new file in `raw/inbox/`, spawn `wiki ingest <path>` subprocess. Deduplication: compute content hash before spawn; skip if hash already in raw/.
- `scripts/install_watcher.sh` — generates and loads a launchd plist (`~/Library/LaunchAgents/com.user.knowledge-watcher.plist`).
- `gateway/ops/status.py` — extended: shows watcher state (running, last event, queue depth).

**Acceptance criteria.**

- `wiki status` reports watcher running.
- `cp test.md ~/code/knowledge/raw/inbox/` triggers ingest within 5 seconds.
- Watcher survives ingest failures (logs error, continues watching).
- `launchctl unload com.user.knowledge-watcher` cleanly stops the daemon.

**Out of scope.** API-only-source pollers (M10).

**Estimated scope.** ~200–300 LOC + integration tests.

---

### M5 — NotebookLM gateway

**Goal.** Every NotebookLM operation is mediated by `wiki nlm-*` commands that atomically file artifacts back as wiki pages. The Discipline Gate is enforced.

**Modules.**

- `gateway/nlm_client.py` — wraps `nlm` CLI via `subprocess`. Methods: `notebook_list()`, `notebook_create(domain)`, `source_add(notebook_id, raw_path)`, `query(notebook_id, question)`, `slides_create(notebook_id, topic)`, `audio_create(notebook_id, topic)`, `briefing_create(notebook_id)`, `artifact_revise(artifact_id, instructions)`, `artifact_download(artifact_id, dest)`. Stateless. All operations return structured results.
- `gateway/ops/nlm.py` — implements each `wiki nlm-*` operation. Each:
  1. Resolves domain → notebook_id via `nlm/notebooks.yaml`.
  2. Calls nlm_client method.
  3. Downloads artifact (where applicable) to `wiki/artifacts/<type>/`.
  4. Writes wiki artifact page (per WIKI.md § 4.6) with bidirectional link (local file path + nlm_artifact_url).
  5. Updates referenced source pages' `wiki_pages:` frontmatter.
  6. Logs to log.md.
  7. Returns structured result with paths and URLs.
- `nlm/notebooks.yaml` — initialized empty; populated by `wiki nlm-add` (auto-creates notebook on first add per domain) or by migration (Phase 1 inventory).

**Acceptance criteria.**

- `wiki nlm-add glp1-reward-modulation <source-id>` adds the source to the domain's NotebookLM corpus, updates `nlm_corpus_ids` on the source frontmatter, logs.
- `wiki nlm-slides <domain> "<topic>"` generates slides, downloads to `wiki/artifacts/slides/<slug>.marp.md`, writes wiki artifact page with bidirectional link, logs.
- Direct calls to `nlm` CLI in committed wiki content fail CI grep check (pre-commit hook in M9).
- `pytest tests/gateway/test_nlm.py` passes (mocked `nlm_client`, 6–10 tests).

**Out of scope.** `wiki query` with NotebookLM corpus (deferred to M6 because it depends on agent-driven synthesis-page authorship).

**Estimated scope.** ~600–800 LOC + tests.

---

### M6 — Incremental wiki authorship

**Goal.** Single-source ingest flows through the gateway to update entity/concept/synthesis pages with agent-driven authorship. Plan-before-write, citation grounding, draft mode all enforced. Closes the wiki-authorship loop.

**Modules.**

- `gateway/validator.py` — extended with full WIKI.md § 11.2 rules: citation grounding (with draft-mode downgrade), bidirectional backlink integrity. Slug Levenshtein check (§ 11.3).
- `gateway/ops/ingest.py` — extended: after source page is written, agent is invoked with source content + relevant existing wiki pages + schema; agent returns a Plan (pages to create + pages to update + cross-references); gateway validates the plan, applies writes atomically, logs.
- `gateway/ops/finalize.py` — `wiki finalize <page-path> [--abandon]` per WIKI.md § 5.5.
- `gateway/ops/query.py` — `wiki query "<question>"`: agent searches wiki via index.md + grep, may invoke `wiki nlm-query` for large-corpus questions, files good answers as synthesis pages.
- `gateway/citations.py` — extended: citation density check, claim-sentence detection.

**Acceptance criteria.**

- `wiki ingest <url>` for a high-quality source produces source page + entity/concept page updates; plan is logged; citation grounding enforced.
- `wiki ingest --draft <url>` produces partial pages with `draft: true`; lint surfaces unresolved-claim count; `wiki finalize <page>` succeeds when citations are added.
- `wiki query "<question>"` against an established domain returns a synthesis page filed under `wiki/synthesis/`.
- Plan-before-write rejection: ingest call without plan halts.
- `pytest tests/gateway/test_authorship.py` passes (8–12 tests).

**Out of scope.** Migration-mode authorship (M8, code-driven not agent-driven).

**Estimated scope.** ~700–1000 LOC + tests. The largest milestone — touches the most architectural surface.

---

### M7 — MCP server

**Goal.** Every gateway operation available as an MCP tool. Claude Code agents in any project use native tools instead of shelling out to CLI.

**Modules.**

- `gateway/mcp_server.py` — uses Anthropic MCP SDK. One MCP tool per gateway operation. Each tool delegates to the same `Gateway.execute()` as the CLI — no logic duplication.
- `gateway/cli.py` — extended: `wiki mcp-serve` command starts the MCP server.
- `~/.claude/mcp_servers.json` (or equivalent) — config snippet for adding the wiki MCP server.

**Acceptance criteria.**

- Claude Code session in `~/code/wyckoff-423/` can call `wiki_query` MCP tool and get a result from the canonical knowledge base.
- All `wiki_*` tools work end-to-end with the same semantics as their CLI counterparts.
- `pytest tests/gateway/test_mcp.py` passes (per-tool integration tests).

**Out of scope.** Authentication (single-user local server; no auth needed in v1).

**Estimated scope.** ~300–500 LOC + tests.

---

### M8 — Migration support

**Goal.** `wiki batch-ingest --legacy-import <vault-path>` runs MIGRATION.md phases. AI temporal video and GLP-1 vaults migrated. edge_ai migrated after legacy run finishes.

**Modules.**

- `gateway/converters/youtube.py` — full transcript fetch via `youtube-transcript-api`; timestamp anchors. Uses `gateway/converters/_search/youtube.py` (copied from research-notebook).
- `gateway/converters/arxiv.py` — abstract via arXiv API. Uses `gateway/converters/_search/arxiv.py`.
- `gateway/converters/pubmed.py` — abstract via PubMed E-utilities. Uses `gateway/converters/_search/pubmed.py`.
- `gateway/slugmap.py` — extended: legacy slug detection, type inference, canonical ID generation per MIGRATION.md § 6.
- `gateway/citations.py` — extended: bulk rewrite given a slug map.
- `gateway/ops/migrate.py` — orchestrates: build slug map → run sources through ingest with `--legacy-import` flag → migrate concepts/entities (with classification call) → migrate MOCs and synthesis with citation rewrite → backfill example bank from JSON checkpoints → set up policy.yaml from legacy config → update notebooks.yaml.
- `gateway/ops/batch_ingest.py` — new: handles whole-vault and `--legacy-import` modes.
- `migrations/0001-import-legacy-vaults.py` — script that invokes `wiki batch-ingest --legacy-import` per vault per phase. Reads from `~/code/research-notebook/data/obsidian*/` (research-notebook stays put).

**Acceptance criteria.**

- `wiki batch-ingest --legacy-import ~/code/research-notebook/data/obsidian/ --dry-run` produces a slug map at `.knowledge/migrations/ai-temporal-video-slug-map.yaml` plus a migration plan; no writes.
- Real run completes; lint passes clean (zero broken citations, zero malformed pages).
- 10% sample audit shows content fidelity vs. legacy.
- All three legacy vaults migrated end-to-end. NotebookLM corpus IDs recorded. Example bank populated.
- Research-notebook is unchanged after migration runs (read-only access only).
- `pytest tests/gateway/test_migration.py` passes (per-phase tests with vault fixtures).

**Out of scope.** Archive moves of legacy vaults (not happening — research-notebook stays as historical artifact per project decision).

**Estimated scope.** ~700–1000 LOC + tests. Heavy reuse of the `_search/` API helpers.

---

### M9 — Full lint pass

**Goal.** `wiki lint` runs all 9 checks per WIKI.md § 12.2; report at `.knowledge/lint/<timestamp>.md`. Cheap checks integrated into every ingest; full pass on demand.

**Modules.**

- `gateway/ops/lint.py` — orchestrator. Each check is a function in a sub-module:
  - `gateway/lint/orphans.py` — wiki pages with no inbound wikilinks.
  - `gateway/lint/stale_drafts.py` — pages with `draft: true` older than threshold.
  - `gateway/lint/stale_claims.py` — claims whose cited source has been superseded.
  - `gateway/lint/contradictions.py` — LLM-driven scan for contradictory claims.
  - `gateway/lint/missing_pages.py` — terms in 3+ pages without their own page.
  - `gateway/lint/citation_density.py` — per-page density vs. threshold.
  - `gateway/lint/schema_drift.py` — frontmatter / section drift.
  - `gateway/lint/filter_calibration.py` — re-score sample of past decisions; flag drift.
  - `gateway/lint/inbox_pending.py` — count of `raw/inbox/` files awaiting routing.
  - `gateway/lint/nlm_pending.py` — sources eligible for NotebookLM but not yet synced.
- Pre-commit hook in `~/code/knowledge/.git/hooks/pre-commit` — fast checks (broken wikilinks, schema, source immutability) plus grep for raw `nlm` calls in committed content.

**Acceptance criteria.**

- `wiki lint` produces a structured report at `.knowledge/lint/<timestamp>.md` matching WIKI.md § 12.3.
- `wiki lint --scope orphans` runs only one check.
- Pre-commit hook blocks commits that fail the cheap checks.
- `pytest tests/gateway/test_lint.py` passes (one test per check).

**Out of scope.** Scheduled lint via launchd (manual `wiki lint` is sufficient v1; scheduling can be added trivially later).

**Estimated scope.** ~600–900 LOC + tests.

---

### M10 — Remaining converters and pollers

**Goal.** Source diversity matches the user's stated requirement: Web, YouTube, arXiv, PubMed, PDF, voice, audiobook all supported. API-only-source poller pattern established (template for Apple Notes, Notion, etc.).

**Modules.**

- `gateway/converters/pdf.py` — `pdfplumber` or `marker`. Sidecar PDF preserved.
- `gateway/converters/voice.py` — Whisper local or API. Sidecar audio preserved.
- `gateway/converters/audiobook.py` — Whisper-large for long audio; chapter index sidecar.
- `gateway/pollers/` — `Poller` ABC, scheduled (cron/launchd) modules per source. M10 ships only the framework + a stub for one API source (e.g., Apple Notes via AppleScript) as proof of pattern.

**Acceptance criteria.**

- `wiki ingest <pdf-path>` produces canonical markdown + sidecar PDF.
- `wiki ingest <m4a-path>` produces transcript + sidecar audio.
- One poller (Apple Notes) runs on schedule and writes to `raw/note/`.
- `pytest tests/gateway/test_converters_*.py` passes.

**Out of scope.** Full poller suite (Notion, Slack, Gmail) — additive in future work.

**Estimated scope.** ~500–800 LOC + tests.

---

## 6. Cross-cutting concerns

### 6.1 Testing strategy

- **Unit tests** for pure functions: validator rules, frontmatter parser, citation parser, slug map.
- **Integration tests** for gateway operations: hand-crafted input, observed output, side effects checked (log, index, frontmatter mutations).
- **Fixture corpus**: `tests/gateway/fixtures/sources/` with 5–10 hand-crafted canonical markdown files of different types. Used across milestones.
- **End-to-end tests** in M5+ exercising full ingest + filter + wiki authorship flow (with mocked Claude calls for determinism).
- **Migration tests** in M8 use a small synthetic legacy vault under `tests/gateway/fixtures/legacy_vault/` to validate migration without touching real data.

`pytest -v tests/gateway/` runs the full suite. CI on commit: green required.

### 6.2 Atomic write pattern (used everywhere)

```python
def write_atomic(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content)
    tmp.rename(path)  # POSIX atomic
```

All writes go through this helper. Half-written files are impossible.

### 6.3 Idempotency

Every operation that writes computes content hashes against existing state and skips no-ops. Running `wiki ingest <same-path>` twice is safe and silent.

### 6.4 Error model

- Validator failures: structured `ValidationError` with rule name, file path, offending content. CLI exits non-zero with the rule details.
- Operational errors (network, NotebookLM unavailable, lock contention): `OperationalError` with retry guidance.
- Schema violations on existing files (out-of-band edits): caught by validator on read; reported via lint.

### 6.5 Logging

Two layers:

- `~/code/knowledge/log.md` — domain-level event log (ingests, queries, lint passes); user-readable.
- Standard Python `logging` to stderr — debug/info for development; gated by `--verbose` CLI flag.

## 7. Dependencies and packaging

### 7.1 Python dependencies (in pyproject.toml)

- `pyyaml` (frontmatter parsing)
- `watchdog` (M4, filesystem events)
- `trafilatura` or `readability-lxml` (M2, web content extraction)
- `youtube-transcript-api` (M8, YouTube transcripts)
- `pdfplumber` (M10, PDF extraction)
- `openai-whisper` or `faster-whisper` (M10, voice transcription)
- `mcp` (M7, MCP SDK)
- `pytest` (dev)

External binaries:

- `nlm` (NotebookLM CLI) — already installed.
- `fswatch` (optional; `watchdog` pure-Python suffices on macOS).
- `ffmpeg` (M10 voice/audiobook).

### 7.2 Packaging

- `pyproject.toml` defines `[project.scripts] wiki = "gateway.cli:main"` so `wiki` is on PATH after `pip install -e .`.
- `~/code/knowledge/.venv/` is the canonical environment. Research-notebook keeps its own `.venv/` for historical reproducibility.

### 7.3 Configuration

- `KNOWLEDGE_ROOT` env var points to wiki content (default `~/code/knowledge/`). Lets the gateway be tested against a fixture root in CI.
- `~/code/knowledge/.knowledge/config.yaml` (M1+) for runtime settings: thresholds, watcher inclusions, lint cadence. Schema additive.

## 8. Open decisions

1. **Web extraction library**: `trafilatura` (heavier, better quality on edge cases) vs. `readability-lxml` (lighter, well-known). Suggest `trafilatura` for fidelity.
2. **MCP SDK**: official Anthropic Python MCP SDK once stable, or a lightweight in-house implementation. Default: official SDK.
3. **Watcher daemon framework**: pure-Python `watchdog` + launchd, or shell out to `fswatch`. Default: `watchdog` (one less moving part).
4. **Per-domain lint frequency**: weekly `wiki lint` is enough? Or do we need automated runs? Default: manual until we feel pain.
5. **Pre-commit hook scope**: just structural lints (cheap), or also run the full validator on touched files? Default: structural only, full lint on demand.

These are non-blocking. Defaults above carry unless the review pushes back.

---

## Estimated total scope

~5,000–7,000 LOC + ~1,500–2,500 LOC of tests across all 11 milestones (M0 through M10).

**Wall-clock estimate (LLM-paced execution against a locked-up-front architecture):** a single sustained session. Actual: M0–M10 shipped in one continuous build (see § 9 commit hashes). Drafting this plan with "multi-week" was a copy-paste from human-developer pacing heuristics — wrong for the actual constraints. The real cost drivers were:

1. **Real-world hand-tests** — wall-clock latency on `claude -p`, arXiv API, Wikipedia, NotebookLM CLI, watchdog settle delays. ~1–3 minutes per milestone, not days.
2. **Context window** — the limiting resource for an AI-paced build is conversation context, not engineer-hours. M0–M10 fit comfortably; the docs pass at the end started bumping up against it.
3. **Architecture-up-front** — Phase 2 + Phase 3 (decisions + schema docs) ate the design cost before any code. Build phase was almost entirely mechanical translation of locked decisions into modules.
4. **Mocking the expensive things** — full pytest suite runs in ~2.4s because NotebookLM, Whisper, and `claude -p` are all behind `*Client` Protocols with stub implementations.

A future AI-paced rebuild of similar scope should be estimated by:
- conversation context budget (build until context pressure forces a break)
- count of distinct external surfaces requiring real hand-tests
- count of human-decision forks that need pause-and-confirm

NOT by LOC × developer-day rate. That heuristic is for a different mode of work.

The plan is intentionally aggressive on architecture and conservative on features. Every milestone delivers a working slice; every milestone is reviewable and reversible.

---

## 9. Delivered status (post-build record)

v1 (M0–M10) shipped in a single sustained session. M11+ tracks operational milestones: real legacy migrations, follow-up on deferred stubs. 217 passing tests, ~7,800 LOC under `src/gateway/`. Each milestone landed as one commit on `main`.

| # | Commit | Tests | Hand-test |
|---|---|---|---|
| M0 | `48a7ac3` | 4 smoke | venv, CLI on PATH, `wiki --version` |
| M1 | `1939233` | 30 | YouTube-shaped sample → raw/+ wiki/sources/, idempotent |
| M2 | `1ffb11f` | 45 | `wiki ingest https://en.wikipedia.org/wiki/Memex` end-to-end |
| M3 | `0c2445a` | 67 | Real `claude -p`: GLP-1 RCT 0.95, influencer testimonial 0.00 |
| M4 | `2d7493b` | 78 | Drop file in `raw/inbox/`; ingested in ~3s; quarantine works |
| M5 | `44d9195` | 98 | NotebookLM ops mocked end-to-end; subprocess wrapper smoke-tested |
| M6 | `738f01f` | 134 | Plan → apply → finalize cycle with `StubPlanClient`; query files synthesis |
| M7 | `4cdd0be` | 152 | `wiki mcp-serve` starts and exits cleanly under SIGTERM |
| M8 | `54f1021` | 172 | Real GLP-1 vault dry-run: 127 sources mapped (48 yt / 77 pubmed / 2 arxiv) |
| M9 | `5bb5d81` | 193 | `wiki lint` on empty wiki → 0 findings across all 10 checks; report written |
| M10 | `bebf319` | 217 | `wiki ingest https://arxiv.org/abs/2403.05530` → real Gemini 1.5 paper ingested; synthesized PDF preserved as sidecar |
| M11 | `5c507eb` | 217 | Real legacy migration phase 2 (GLP-1): 127 sources + 28 concepts + 5 MOCs + 3 synthesis written into `~/code/knowledge/`; 13/13 spot-check audit pass on title/authors/url/filter-score/body-content; research-notebook untouched |
| M12 | `87fb338` | 221 | Wikilink canonicalization across migrated content: 158 → 130 lint orphans (Δ-28; all concept orphans resolved); migration idempotency for creation-moment timestamps verified by re-running phase 2 with zero raw/ or wiki/sources/ churn |
| M13 | `db91f68` | 221 | Real legacy migration phase 1 (ai-temporal-video): 86 youtube sources + 46 concepts + 5 MOCs + 3 synthesis added to `~/code/knowledge/`; 9/9 spot-check audit pass; zero cross-domain wiki collisions with phase 2; zero concept orphans (M12 canonicalization works on phase 1 data); research-notebook untouched |
| M14 | `fd2b140` | 222 | Real legacy migration phase 3 (edge-ai-agentic): 150 sources written + 213 pre-existing skipped (legacy edge_ai vault was a strict superset of phases 1+2 sources). Skip-if-canonical-exists guard added to source migration; cross-domain sources retain their original domain marker. 15/15 spot-check audit pass on phase-3-unique sources. 75 concepts + 8 MOCs + 4 synthesis added (concept/MOC/synthesis layer is fully disjoint from phases 1+2). Zero concept orphans across the 150 concepts now in canonical KB |
| M15 | `ad8b677` | 230 | Lint stub `missing-pages` implemented: per-domain LLM call identifies entities/concepts appearing across pages without dedicated wiki pages. Real `claude -p` hand-test against the migrated KB produced 16 findings in 45s across 3 domains — Semaglutide / Liraglutide / Exendin-4 / GLP-1 receptor agonists / ActivityNet / Mamba / Graph Neural Networks — all genuine wiki-authoring gaps |
| M16 | `a704707` | 237 | Lint stub `filter-calibration` implemented: sample-based re-scoring of past filter decisions per domain; reports mean delta + per-source outliers (\|delta\| > 0.20). Honest "no policy" finding when `.knowledge/policies/<domain>/policy.yaml` is absent — current state for all 3 domains until M19 backfill lands |
| M17 | `96c2f7e` | 244 | Lint stub `contradictions` implemented: extracts claim sentences per domain, batches up to 80 claims per Claude call, asks for contradictory pairs, emits one warning per validated pair. Real hand-test deferred (~12 calls, ~6 min wall against the M14-migrated KB) per the M5 expensive-real-call pattern |
| M18 | `5147215` | 252 | Lint stub `stale-claims` implemented: hybrid mode. Default `run()` is deterministic — gathers academic-citation claims with same-domain candidates published ≥ 3 years later, emits per-domain count (cheap, no LLM). `run(sample_size=N)` enables LLM verification per claim. Default mode against M14-migrated KB returns 0 findings (legacy MOCs use numeric `[N]` citations rather than `[[sources/X]]` wikilinks; scaffolding ready for downstream wiki-authoring work) |
| M19 | `28df4c5` | 262 | Policy + example-bank backfill from research-notebook legacy artifacts (`gateway/ops/example_bank.py`, `wiki backfill-examples` CLI). Real hand-test populated all 3 domains: 268 GLP-1 examples (127 include / 141 exclude) + 82 ai-temporal-video (all include) + 150 edge-ai-agentic (all include) + 3 canonical `policy.yaml` files. M16 filter-calibration now has data to operate on |
| M20 | `739cfde` | 274 | Filter fine-tuning loop: trigger detection + distilled-prompt extraction (`gateway/ops/finetune.py`, `wiki finetune --check / --distill`). Default trigger threshold 500 examples per domain; below threshold the check reports state; above (or with `--force`) the distill mode asks Claude to produce a tightened candidate `policy_versions/<timestamp>.yaml`. Live `policy.yaml` is never overwritten. Real hand-test on GLP-1 (268 examples, --force): 1 LLM call (~60s) produced a v2 candidate with VTA/NAc circuitry specificity, compound list, non-food-reward extensions, and concrete dosing-strategy criteria — significantly tighter than the v1 legacy import |
| M21 | `a9fb9bc` | 294 | Voice + audiobook converters (item D). `gateway/transcription.py` wraps mlx-whisper (Apple Metal) + pyannote.audio diarization, both gated behind the optional `[whisper]` extra. VoiceConverter handles m4a/mp3/wav/flac/ogg/aac/opus; AudiobookConverter handles m4b with embedded chapters via mutagen. Diarization gracefully falls back to transcript-only when HF token absent. Real hand-test (combined 12.7s say-generated audio): warm-cache 5.5× real-time on M3 Max with `mlx-community/whisper-large-v3-turbo`. Diarization hand-test deferred (requires user-side `huggingface-cli login` + accepting `pyannote/speaker-diarization-3.1` model terms) |
| M22 | `25b19a9` | 294 | Whisper dep-graph pin: pyannote.audio 4.x's `speaker-diarization-3.1` pipeline added a `pyannote/speaker-diarization-community-1` indirection requiring an additional terms-acceptance gate. Pinned `pyannote.audio<4.0` for the simpler single-gate path. Also pinned `huggingface_hub<1.0` (1.x dropped the `use_auth_token` kwarg pyannote 3.x passes through) and `torchaudio<2.5` (2.5+ removed `AudioMetaData`). Added kwarg-fallback in `_pyannote_diarize` so the loader works across pyannote 3.x / 4.x and old/new hub versions. Real diarization hand-test now passes: 12.7s two-voice clip → SPEAKER_00 / SPEAKER_01 correctly attributed at 1.36× real-time end-to-end |
| M23 | `3d42d34` | 294 | First real wiki-authoring loop: `wiki query` gained a `--draft` flag (mirrors `wiki ingest --draft`) that pipes through to `apply_plan(draft=True)`. Real claude-driven hand-test on the migrated GLP-1 corpus produced a 16-citation synthesis page (`wiki/synthesis/what-is-known-about-glp-1.md`) covering anatomical substrate, animal-model reward evidence, human fMRI evidence, and corpus-coverage limitations — exactly the citation graph the migration was missing. Confirms the M11–M14 migrated content is usable as wiki authoring substrate |
| M24 | `0c1a36b` | 294 | GLP-1 citation-graph build-out: 4 additional synthesis queries covering substance-use disorders (18 cites), dosing strategies (26 cites), mental-health side effects (18 cites), and neuroprotection / cardiovascular outcomes (3 cites). 5 query-driven syntheses now cite **51 unique GLP-1 sources** from the M11-M14-migrated corpus (40% coverage of 127). Lint source orphans dropped 363 → 312 (Δ-51, exact match). ~7 min of `claude -p` time total, no manual claim extraction needed |
| M25 | `8f9b8d8` | 294 | Citation-graph build-out for the other two domains: 4 synthesis queries on `ai-temporal-video` (temporal action detection, video-language grounding, long-form reasoning, object tracking) and 4 on `edge-ai-agentic` (on-device LLM inference, agentic workflows, edge inference infrastructure, transformer model compression). After all three domains: **148/363 sources cited overall (41%)** — ai-temporal 49%, GLP-1 40%, edge-ai 37%. Source orphans 312 → 215 (Δ-97). ~13 min `claude -p` total |
| M26 | `ebd6237` | 294 | Documentation pass for the post-M25 state. New `TUTORIAL.md` — day-1 human-facing usage guide covering the mental model, the three ingest paths, the synthesis loop, cross-project use via MCP, and operational habits. README + CLAUDE refreshed; memory updated. (Note: M27 walked back the state-snapshot leakage from this milestone — see § 9 next row.) |
| M27 | `7f24da2` | 294 | Doc hygiene: removed point-in-time state snapshots from `README.md` and `CLAUDE.md` (they belong in `wiki status` / `index.md` / BUILD.md, not in system docs). Generalized illustrative file paths in `TUTORIAL.md` from a specific synthesis slug to `<slug>` placeholders. Memory entries left intact — they're scoped as point-in-time records by design. The principle: system documentation describes invariants; per-milestone delivery records describe state at delivery; live state lives in the system itself |
| M28 | _this commit_ | 294 | Doc framing fix: prior README/CLAUDE intros described the system in isolation. NotebookLM and Obsidian are load-bearing integrations, not competitors — NotebookLM is the heavy-synthesis service behind the gateway (`wiki nlm-*` artifacts file back to the vault); Obsidian is the knowledge-graph visualization engine over the same wikilinks the validator enforces. Updated README + CLAUDE intros + TUTORIAL mental-model section to lead with this integration story |

### Key architectural properties locked in

- **Plan-before-write** (M6): the agent's only path to `wiki/{entities,concepts,synthesis,mocs}` is to return a `Plan`; `apply_plan` validates atomically.
- **Discipline Gate** (M5): `nlm` CLI is forbidden in committed wiki content; the `wiki nlm-*` family is the only sanctioned NotebookLM surface. Pre-commit hook (M9) greps for violations.
- **Filter as injectable client** (M3): `FilterClient` Protocol; `ClaudeCLIFilterClient` default backend uses `claude -p` (Max-plan auth, no API key required); tests inject `StubClient`.
- **Source immutability** (M1): once a source is in `raw/<type>/<id>.md`, the body cannot change. Frontmatter mutations are restricted to `filter:`, `nlm_corpus_ids`, `wiki_pages`, `domains`. Lint enforces.
- **Atomic writes** (M1): every `wiki/` and `raw/` write goes through `core.write_atomic` (POSIX temp-then-rename).
- **Idempotency by content hash** (M1): re-running any operation with unchanged inputs is a silent no-op.
- **Single-backend, two-surface CLI/MCP** (M7): the same `gateway/ops/*.py` functions back both the `wiki` CLI and the `wiki_*` MCP tools — no behavioral drift possible.
- **Filesystem-as-database** (whole build): markdown + YAML frontmatter is canonical; all retrieval primitives (`grep`, file walk, frontmatter parse) work without an SDK.

### Hand-tests deferred (intentional)

- M5 real NotebookLM artifact creation (would create real artifacts in user's account; ~5–15 min per artifact)
- M6 real `claude -p` plan generation (~10–30s per source; mocks cover gateway logic)
- M11 / phase 1 (ai-temporal-video) and phase 3 (edge-ai-agentic) — held until phase 2 lessons applied (see § 10)

### Stubs and follow-up work

- **Lint stubs** (M9): `missing-pages`, `stale-claims`, `contradictions`, `filter-calibration` are registered but return `[]`. Real implementations are LLM-heavy or require sampling logic; deferred.
- **Voice / audiobook converters** (M10): Whisper is a 2–5GB dep; user can wire in OpenAI's API or a local Whisper install when needed.
- **Apple Notes AppleScript integration** (M10): poller framework ships; the AppleScript adapter is platform-specific follow-up.
- **CLI stubs**: `index`, `search`, `migrate` (the migration command is replaced by `batch-ingest --legacy-import`; index and search are quality-of-life ops over the same content).
- **Filter fine-tuning loop**: roadmap per WIKI § 10.4. Trigger threshold ~500–1000 high-quality decisions per domain.

---

## 10. Operational milestones (M11+)

**M11 — Phase 2 GLP-1 migration** (`5c507eb`). First real `--commit` run of `wiki batch-ingest --legacy-import` against `~/code/research-notebook/data/obsidian_glp1/`. 127 raw + 127 wiki/sources + 28 concepts + 5 MOCs + 3 synthesis written; 13/13 spot-check audit pass (title/authors/url/filter-score/body); research-notebook untouched. Initial lint reported 158 orphans driven by legacy bare-slug wikilinks.

**M12 — Wikilink canonicalization + migration idempotency.** Extended `gateway/slugmap.py` with `wiki_page_mapping(legacy_vault_path)` returning `{bare-slug → type-prefixed-target}` from the legacy vault's `concepts/`, `synthesis/`, `mocs/` (and singular `moc/`) directories. `gateway/ops/migrate.py` merges this map into `citation_map` before concept/synthesis/MOC migration; source-slug entries override on collision. Re-running phase 2 dropped lint findings from 158 → 130 (Δ-28; all concept orphans resolved). Remaining orphans: 127 sources (legacy MOCs use numeric `[1, 2]` citations, no `[[sources/X]]` wikilinks) and 3 synthesis (legacy MOCs don't link them). Both are downstream wiki-authoring work, not migration scope.

Also addressed a migration-idempotency defect surfaced by the M12 re-run: `_now_iso()` was called on every migration run, rotating `ingested_at`, `legacy_provenance.imported_at`, `filter.decided_at`, `draft_started_at` across all migrated files (254 timestamp-only diffs on a re-run of phase 2). Added `_preserved_at(target, dotted_key, default)` helper that returns the existing file's value when present; used in all four migrate helpers (source / concept / synthesis / MOC). Tested by `test_migrate_vault_idempotent_for_creation_timestamps`. Re-run after the fix produced exactly 40 changed files (the legitimate wikilink-rewrite content delta), zero timestamp churn.

**M13 — Phase 1 ai-temporal-video** (`db91f68`). 86 youtube + 46 concepts + 5 MOCs + 3 synthesis; 9/9 audit pass; fully additive over phase 2 (zero collisions); zero concept orphans.

**M14 — Phase 3 edge-ai-agentic.** Surfaced legacy data contamination: the edge_ai_agentic legacy vault contained 363 source files, of which 213 were pre-existing duplicates of phases 1 (86) and 2 (127). The 150 phase-3-unique sources are correctly scoped to edge-AI/agentic content (LLM inference, transformer compression, NPU mini PCs, blockchain edge computing). Added a "skip if canonical raw target exists" guard to `_migrate_source` enforcing source-immutability across cross-domain re-imports — sources retain the domain marker of the first phase that migrated them. 15/15 spot-check audit on phase-3-unique sources; concepts/MOCs/synthesis layer disjoint from prior phases (75 + 8 + 4 added cleanly). Future enhancement candidate: legitimate cross-domain sources (a single source belonging to multiple research domains) would benefit from `domains:` merging rather than skip; deferred until a real use case appears.

**M36 — Bottom-up domain discovery.** Closes the gap between "ingest a pile of unsorted sources" and "grow the citation graph against named domains." Surfaced by a hand-test that bulk-ingested 360 PDFs from Apple Notes attachments without `--domain` and without `--with-plan` (cost-aware), producing 360 graph-island source pages with no concept extraction and no domain affiliation — the existing tooling assumed top-down authorship (human picks domain → policy → sources land *under* that policy → agent extracts claims into entity/concept pages). M36 adds the inverse path: discover candidate domains from an untagged corpus, bless the useful ones, back-tag member sources atomically, and reverse on demand.

Page type added: `domain-proposal` (`wiki/proposals/<slug>.md`) with required fields `proposed_domain`, `status` (draft|blessed|rejected), `member_sources`, `rationale` and required sections `Rationale` / `Member sources`. Not citation-grounded — proposals describe clusters, not claims. Four new ops:

- `wiki discover-domains [--scope GLOB] [--since DATE] [--untagged] [--timeout SECONDS]` — single-shot LLM clustering pass. Reuses `apply_plan()` so all proposals validate before any write — atomicity is automatic. Default 300s plan-client timeout is tight for 200+ source corpora; pass `--timeout 1500` for the full 360-PDF case.
- `wiki promote-domain <proposal-slug>` — writes minimal-viable `policy.yaml` (marked `auto_generated_from_proposal: true`, default thresholds, empty inclusion criteria pending hand-authoring), back-tags every member source's `domains:` in BOTH `raw/<type>/<id>.md` and `wiki/sources/<id>.md` (frontmatter-only mutation; body bytes preserved → source-immutability holds), flips proposal `status: draft → blessed`. Atomic across all writes.
- `wiki demote-domain <domain-slug>` — exact inverse of promote. Removes `<slug>` from every source's `domains:`, deletes the auto-generated policy, flips matching blessed proposal back to draft. Refuses to delete a policy lacking `auto_generated_from_proposal: true` (protects hand-authored work).
- `wiki reject-proposal <proposal-slug>` — deletes a draft proposal page. Refuses blessed; caller must demote first.

Lint: new scope `untagged-sources` walks `wiki/sources/*.md` and reports the count of pages with empty/missing `domains:` plus a remediation hint pointing at `wiki discover-domains --untagged`.

Reversibility levels (per "make it reversible if it fails" requirement):
1. **In-flight** — every op stages writes in memory, validates the full set, then commits under the `wiki-author` lock. Validation failure → zero on-disk changes.
2. **Post-success** — `wiki demote-domain` + `wiki reject-proposal` reverse promotion / discovery cleanly.
3. **Code-level** — all M36 work landed on branch `m36-domain-discovery` with each step in its own commit; broken state recoverable via `git reset` to any prior commit.
4. **Corpus-level** — the 360-PDF bulk-ingest was committed as its own commit (`5fed394`) before any M36 code, so the corpus and the M36 toolchain are independently revertable.

Hand-test: 32-source subset (`--scope 'wiki/sources/pdf-a*'`) → LLM produced 6 sensible clusters (trading-markets, cycling-endurance, ai-ml-research, philosophy-human-rights, health-medical, miscellany), each with 4-8 members and human-readable rationale. Reject + promote + demote round-tripped cleanly.

Full 360-PDF run (`--scope 'wiki/sources/pdf-*' --untagged --timeout 3600`): 8 clusters, **100% coverage** (every source assigned to exactly one cluster), single LLM call. Distribution:

| Cluster | Members |
|---|---|
| miscellany | 143 |
| trading-and-markets | 95 |
| health-and-longevity | 29 |
| ai-and-agents | 26 |
| audio-and-streaming-tech | 22 |
| cold-plunge-and-home-build | 18 |
| philosophy-spirituality-psychology | 15 |
| cycling-and-fitness | 12 |

Trading and miscellany dominate (40% + 26%) but the niche clusters are sharp. Notably the LLM annotated `trading-and-markets` with "should likely split later into sub-domains (ICT methodology, trading psychology, macro outlooks, academic finance) once volume warrants it" — the cluster discovery output flagged its own next decomposition step. The 300s default `claude -p` timeout was insufficient for 360 sources; the run completed inside the 3600s `--timeout` budget.

Tests: 19 new (4 schema + 5 discover + 11 promote/demote/reject + 3 untagged-sources lint). 309 → 331.

Out of scope for M36: embedding-based clustering for corpora that exceed the single-shot prompt budget (deferred to M37 if needed); per-cluster `--with-plan` graph-growing (separate milestone). The TB-scale sidecar crawler (Dropbox/Drive/iCloud → cluster manifests → gateway) is a separate `~/code/archivist/` project, not a gateway milestone.

**Commit-history disambiguation.** Two commits on this branch carry an "M37" prefix:
- `f51fb19 M37: nlm-add fallback to source_add_text for non-URL sources` — **misnamed; this is an M36 hand-test fix**, not a new milestone. It surfaced when `wiki nlm-add` choked on the cycling-and-fitness PDF (no `url:` frontmatter). Same fix-loop produced `7c0f08a M36 hand-test fix: poll artifact status before download` (correctly labeled).
- `14f372e M37: Corpus-constructive research orchestrator` — **the real M37**, separate workstream parallel to M36. Adds `wiki research` op + `gateway/research/` module + persistent NotebookLM corpus query path.

A `git rebase -i ... reword` of the misnamed commit was attempted and aborted (CLAUDE.md forbids `-i`; non-interactive cherry-pick alternative tangled on a working-tree race). Leaving the misnamed commit as-is; this paragraph is the canonical disambiguation.

**M37 hand-test findings (2026-04-30).** Two limitations surfaced when attempting a wide scoping `wiki research --dry-run` against `edge-ai-agentic`:

1. *No per-adapter query planning.* The orchestrator at `gateway/research/orchestrator.py:619` passes the user's research prompt verbatim through `_fan_out_search` → `_safe_search` → `adapter.search(prompt, …)`. The `policy.yaml` schema has no query block; the `plan_client` (Claude) is plumbed in but only used for `_infer_domain` (slug routing). The result is that every adapter receives the same prompt as its literal search query, with no per-adapter idiom adaptation and no expansion into multiple queries. Anything beyond a ~10–15-word focused question collapses recall (YouTube `search.list` returns 0; arXiv times out at 30s; Firecrawl gets a degraded query). Workaround: hand-condense to a short focused question. Permanent fix is M37.1 — runtime per-adapter query expansion via `plan_client`, with persistence at `nlm/query_plans/<session-id>.yaml` for ad-hoc review and improvement, and a few-shot loop from edited plans. Plan: `~/.claude/plans/m37.1-runtime-query-expansion.md`.
2. *Local-files adapter cannot survey existing `raw/`.* `gateway.research.adapters.local.LocalAdapter._converter_for` dispatches via `gateway.converters.dispatch`, which only registers handlers for unconverted source types (`.pdf`, `.mp3`, etc.). Already-ingested `raw/<type>/*.md` files are silently skipped, so `--include-local 'raw/pdf/*.md'` cannot be used for an internal-corpus scoping pass. An "inventory existing raw/ against a thesis" workflow would need a different surface — e.g., a `wiki research --inventory-only` mode or a new `wiki survey` op. Out of scope for M37.1.

### M37.1 — Runtime per-adapter query expansion

Closes the load-bearing M37 gap (above, finding #1) by adding a runtime query-planning step to `wiki research`. The user's research prompt is no longer dispatched verbatim to every adapter; instead `plan_client` (Claude) generates idiomatic per-adapter query lists from the prompt + domain policy + recent curated examples.

**What's new.**

- `gateway.research.query_plan_store` — persistent store for `QueryPlan` artifacts at `nlm/query_plans/<session-id>.yaml`. Surfaces `save`, `load`, `exists`, `is_edited`, `recent_edited(domain, n)`. The `is_edited` check is filesystem-aware: a YAML whose mtime exceeds its `generated_at` by more than 2s is treated as user-edited. The `recent_edited` scan returns plans with `edited: true` for use as few-shot seeds in subsequent runs.

- `gateway.research.query_planner.plan_per_adapter_queries` — calls the configured `PlanClient` with the prompt, a policy excerpt (topic/field/top inclusion criteria), the adapter manifest, target counts (default: youtube=20, arxiv=8, web=15, pubmed=5, local=0), and any few-shot examples from `recent_edited`. Per-adapter idiom guidance is baked into the planner prompt: short keyword phrases for YouTube, paper-language for arXiv, vendor/framework terms for web, biomedical mesh-style for PubMed (with explicit instruction to return `[]` when not applicable). Response parsing tolerates markdown fences and leading prose.

- `wiki research` orchestrator (`research()` in `orchestrator.py`) gains a new step between policy-load and fan-out: resolve a query plan via one of four paths:
  1. `--execute <session-id>` → load the persisted plan; if mtime > `generated_at`, stamp `edited: true` and re-save so future few-shot scans can pick it up.
  2. `--queries <path>` → adopt an external YAML's queries; rebrand under this session's id/prompt/domain.
  3. default with `plan_client` available → call the planner; persist the new plan; auto-advance to fan-out.
  4. `--no-plan` (or `plan_client=None`) → M37 verbatim fallback; no plan persisted.

  `--review` returns immediately after persistence with a summary pointing at the YAML path; user edits, then resumes via `--execute`.

- `_fan_out_search` and `_safe_search` refactored to take a query plan (`dict[adapter_name, list[query]]`) instead of a single prompt. Each non-local adapter is invoked once per query in its list with `per_query_max = max(5, max_results_per_adapter // len(queries))` so the global cap holds. The local adapter is special-cased — it ignores queries (it enumerates user-supplied paths) and is invoked exactly once.

- Planner failure (malformed JSON, empty response, etc.) logs and falls back to verbatim. Slop-but-running beats hard-fail.

- New CLI flags on `wiki research`: `--review`, `--execute SESSION_ID`, `--queries PATH`, `--no-plan`. The positional `prompt` is now `nargs='?'` since `--execute` loads it from the persisted plan. Default behavior instantiates `ClaudeCLIPlanClient()` so the planner activates without extra config.

**Hand-test (dry-run).** `wiki research "RAG over proprietary first-party data on edge devices" --domain edge-ai-agentic --review` produced a 48-query plan in ~12s (8 arxiv + 20 youtube + 15 web + 0 pubmed) with high-quality idiomatic queries per adapter — `"on-device RAG llama.cpp"`, `"federated retrieval augmented generation"`, `"LanceDB edge deployment"`, etc. Hand-edited one query to `"EDITED MCP enterprise integration patterns"`, advanced mtime, then ran `wiki research --execute <session-id> --no-plan --dry-run`. Result: plan loaded cleanly, `edited: true` stamped, fan-out hit arxiv with all 8 queries (returned 48 candidates → 33 after merge dedup → 3 cleared filter threshold). YouTube and Firecrawl skipped due to missing API keys (expected); orchestrator continued without them. Materialized 3 sources to `raw/arxiv/`.

**Hand-test (live external + NotebookLM).** Deferred. The Firecrawl key the user disclosed in the M37 hand-test session was flagged for rotation; live-run validation is a supervised step after rotation. Note that the live path tests M37's NotebookLM session/promotion machinery, not M37.1's new code — the dry-run hand-test already validates the full M37.1 surface (planner, persistence, review-gate, --execute, edit detection, fan-out cardinality).

**Tests.** 38 new tests across three files:
- `tests/gateway/test_research_query_plan_store.py` (13): round-trip, missing/malformed handling, mtime-based edit detection, domain+flag filtering, on-disk YAML layout.
- `tests/gateway/test_research_query_planner.py` (15): happy path, fence stripping, prose extraction, missing keys, malformed shapes, target overrides, few-shot rendering, inclusion criteria propagation, adapter idiom guidance presence.
- `tests/gateway/test_research_orchestrator.py` (10 new): planner generates and persists plan, review-gate stops before fan-out, --execute resume, edit-detection stamping, --queries import, mutual exclusion, missing-plan error, plan_client=None fallback, planner-failure fallback, history-seeding.

All 8 pre-existing M37 orchestrator tests pass unchanged (backwards-compat invariant). Full gateway suite: 410 → 448 tests passing.

**Out of scope for M37.1.**

- A `wiki query-plan-pin` op for promoting curated queries into `policy.yaml` (the alternative-feedback-loop path C from the design discussion). Few-shot from edited plans is M37.1's chosen feedback path; pin-to-policy can be a future M37.2 if few-shot proves insufficient.
- A `wiki survey` op for inventorying `raw/` against a thesis (M37 hand-test finding #2). Separate concern, separate milestone.
- Per-adapter query-quality telemetry (which queries returned the highest-filter-score candidates). Useful but not load-bearing.
- A long-form integration test that exercises real adapters end-to-end. The dry-run hand-test covers it; the regression suite covers it; an automated end-to-end test would be useful but not gating.

### M38 — Smart authorship: contradiction detection + post-ingest feedback

Addresses two weaknesses identified in a panel-of-experts UX review (W2: no connection between new source and existing knowledge at ingest time; W7: post-ingest feedback doesn't communicate knowledge impact). The authorship agent now detects contradictions between new sources and existing wiki claims, prioritizes updating existing pages over creating new ones, and emits a structured report of everything it did.

**What's new.**

- `gateway.plan.Contradiction` — new dataclass representing a conflict between a new source's claim and an existing wiki page. Fields: `existing_page`, `existing_claim`, `new_claim`, `source_id`, `severity` (minor/moderate/major). Carried on `Plan.contradictions` and parsed from the agent's JSON response; malformed items are skipped gracefully.

- `gateway.core.AuthorshipReport` — structured summary attached to `OperationResult.authorship_report`. Tracks `pages_created`, `pages_updated`, `contradictions`. Provides `format_summary()` (one-liner: "2 created, 1 updated, 1 contradiction(s) found") and `format_detail()` (CLI-renderable lines with `+`/`~`/`!` prefixes for created/updated/contradictions).

- `apply_plan()` builds the report from plan execution results and passes it through to the caller. Log entries now include `created`, `updated`, and `contradictions` counts.

- `_emit_result()` in `cli.py` renders the authorship report when present: summary line + detail lines showing exactly what pages were created/updated and any contradictions detected.

- `ingest()` propagates `authorship_report` from the plan result to the ingest result, so `wiki ingest --with-plan` shows the full report.

- Authorship prompt rewritten with three explicit instructions: (1) prioritize updating existing pages over creating new ones, with merge guidance; (2) detect and report all contradictions with severity classification; (3) return contradictions in the JSON response alongside updates.

**Tests.** 11 new tests in `test_authorship.py`: contradiction parsing (2), AuthorshipReport formatting (3), apply_plan report population (2), log entry with contradictions (1), ingest report propagation (1), full end-to-end flow (1), prompt content verification (2). Full authorship suite: 40 → 51 tests passing.

**Commits.** `19545d0`..`2a09b13` (7 commits).

**Files modified.** `plan.py` (Contradiction + prompt), `core.py` (AuthorshipReport + OperationResult field), `apply_plan.py` (report construction + log fields), `cli.py` (report rendering), `ingest.py` (report propagation), `test_authorship.py` (11 tests).

### M39 — Top-down domain bootstrap

Restores the predecessor's green-field research workflow. Before M39, starting research on a new domain required either accumulating sources first and running `wiki discover-domains` → `wiki promote-domain` (which produced empty-criteria auto-policies), or hand-editing `.knowledge/policies/<slug>/policy.yaml` directly. M39 adds `wiki bootstrap-domain "<description>" <slug>` which has Claude draft a starter policy from a natural-language description.

**What's new.**

- `gateway.ops.bootstrap_domain` — calls the plan client with the user's description, a single synthetic reference policy ("Patagonian glacier hydrology" — fictional, prevents cargo-culting from real domains), and a strict requirement schema. Validates the response, retries once on under-specified output, draft-saves to `policy.draft.yaml` if the retry also fails.

- `gateway.ops.policy_validator` — strict + lenient modes. Strict enforces minimum specificity (≥3 inclusion criteria, ≥1 exclusion, ≥2 quality_signals categories with ≥2 signals each), threshold ranges, slug regex, schema version. Lenient runs structural checks only — used for legacy policy load (existing `auto_generated_from_proposal` policies don't need migration).

- `_bootstrap_reference_policy.yaml` — checked-in synthetic example used as the only few-shot in the bootstrap prompt. A round-trip test (`test_reference_policy_passes_strict_validation`) ensures schema additions break the test until the reference is updated, preventing schema drift from silently accumulating.

- Collision handling: refuses if `auto_generated_from_proposal: true` exists at the target path (points at `wiki demote-domain`); refuses if a draft proposal exists at `wiki/proposals/<slug>.md` (points at `wiki promote-domain` or `wiki reject-proposal`); allows `--force` only for non-promoted, non-proposal collisions.

- `policy_schema_version: 1` stamped on every bootstrap output. `bootstrapped_from_description_hash` records a SHA-prefix of the description for re-run idempotency tracking.

**Tests.** 21 new tests across `test_policy_validator.py` (10) and `test_bootstrap_domain.py` (11). Full gateway suite: 460 → 481 tests passing.

**Commits.** `6dc531f`..`cae1acd` (4 commits + a test-fix commit `38e2f29` for stale `nlm` argv expectations from the earlier source_map fix).

**Out of scope for M39.**

- `wiki refine-domain` (re-run bootstrap against existing policy as the reference) — natural follow-up but separate milestone.
- Auto-bootstrapping a NotebookLM persistent notebook on first `wiki research --domain <slug>` — already handled by the research orchestrator.
- Migrating legacy `auto_generated_from_proposal` policies to the new schema — lenient validator keeps them loading; explicit migration deferred.

## 11. Downstream wiki-authoring work (post-migration)

These are not migration script work; they require LLM-driven authorship over already-migrated canonical content:

- **Concept body backfill.** Migrated concepts have stub sections (`## Summary _(needs population)_` etc.) because legacy concept pages had no body content beyond a "Methods" cross-reference list. Backfill is per-concept LLM work via `wiki query` or `wiki ingest --with-plan`.
- **Source citation graph.** Legacy MOCs use numeric `[1, 2]` citations without a number→ID map. Resolving these into `[[sources/<id>]]` requires per-MOC LLM authorship that re-grounds claims. 127 source orphans persist until this is done.
- **Synthesis backreferences.** 3 synthesis pages are orphan because no MOC references them. Either MOCs gain a "Synthesis pages" section linking each one, or this surfaces in a future `wiki lint --scope orphans --quiet-mocs` exclude rule.
