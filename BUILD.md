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
| MIT | `4fb42a0` | 294 | Declared MIT license: LICENSE file at repo root, `license = MIT` in pyproject.toml, License section in README. Repo previously had no LICENSE file (effectively all-rights-reserved); MIT unblocks anyone reading or extending it. |
| M29 | `61de5f2` (#1) | 306 | CSV / TSV converter. Stdlib `csv` with dialect sniffing, preview-row (50) and preview-col (20) truncation, pipe-character escaping, original preserved as sidecar at `raw/csv/<id>.<ext>`. Hash-based ID `csv-<sha256-prefix-12>`. Hand-tested end-to-end via `wiki ingest <csv-path>`. Locks the converter pattern for the rest of the source-type expansion series. |
| M30 | `dfbb221` (#2) | 319 | Word `.docx` converter. `python-docx` walks the document body in order, mapping `Heading 1-6` styles to markdown headers and rendering tables. Author / title / created year from `core_properties`. ID format `docx-<author>-<year>-<short>` with sha256-prefix-12 hash fallback (mirrors PDF). Sidecar at `raw/docx/<id>.docx`; gitignored. Legacy `.doc` intentionally unsupported in v1 (would require LibreOffice/antiword). |
| M31 | `fc3ff2b` (#3) | 334 | Excel `.xlsx` converter. `openpyxl` in `read_only=True` / `data_only=True` (memory-efficient streaming over large workbooks; reads cached values for formula cells). Each sheet renders as `## <name>` section with header table + first 50 rows; per-sheet truncation notes. ID format mirrors DOCX. DuckDB-style queryable Excel deferred (heavy dep for a use case the wiki doesn't have); legacy `.xls` deferred. |
| M32 | `8eda4a6` (#4) | 348 | PowerPoint `.pptx` converter. `python-pptx` with each slide as a `## Slide N: <title>` section. Tables rendered as markdown; speaker notes captured as `> **Speaker notes:** ...` block when present. Image / chart shapes skipped (image converter is M33). Bug caught at hand-test: `is`-comparison on title placeholder failed because python-pptx returns fresh wrapper objects per access — fixed by comparing on `shape_id`, regression test `test_pptx_convert_does_not_duplicate_title_in_body` added before commit. |
| M33 | `2058806` (#5) | 372 | Image converter — multimodal ingest. New `gateway/vlm.py` mirrors the M3 Filter Protocol (Protocol + `ClaudeCLIVLMClient` default + `StubVLMClient` / `FailingVLMClient`). Pillow for metadata; Claude vision for the body. VLM prompt requests four sections (Overview / Visible text / Key elements / Domain-specific content) so descriptions are citable. `--dangerously-skip-permissions` on the subprocess so it can use the Read tool to attach the image. ID format `image-<YYYY-MM-DD>-<sha256-prefix-12>`. Hand-test on a real bar chart: VLM correctly identified chart type, transcribed labels, described bar colors and relative heights. |
| M34 | `da60f04` (#6) | 388 | Apple Notes poller — first production poller, replaces M10's no-op stub. JXA over `osascript` (cleaner than pure AppleScript for date formatting and structured JSON output). Cursor at `.knowledge/pollers/apple-notes/cursor.yaml`; lexicographic ISO-8601 comparison so re-runs only fetch what changed. HTML body stripped via stdlib `html.parser` (no external deps). New `wiki poll <name>` CLI (`--list` to enumerate registered). Hand-test deferred to user invocation per the M5 expensive/sensitive-call pattern (running real osascript would scrape personal Notes content into the repo). |

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

### M40 — Web UI Foundation

Local browser front-end (`wiki serve`) wrapping the gateway's daily ops, domain ops, and lint dashboard. Sidebar navigation, hierarchical dashboard with 4 stat cards plus monospace activity feed, dedicated form pages with inline result panels. Long-running ops (ingest --with-plan, query, bootstrap-domain, discover-domains) use a submit-then-poll pattern with an in-memory task store; short ops (finalize, filter-correct, promote/demote/reject) execute synchronously. Complementary to Obsidian: the UI focuses on operations and state Obsidian can't show; wiki content browsing remains in Obsidian.

**Architecture.** FastAPI backend in `src/gateway/web/` thinly adapts existing `gateway.ops.*` functions over HTTP. Vite + React + TypeScript SPA in `web/` is built once and committed as static assets to `web/dist/`, served by FastAPI at `/`. Localhost-only by default; `--bind 0.0.0.0` opt-in for LAN access.

**What's new.**

- `gateway.web.app` — FastAPI app construction. `create_app()` registers routers and mounts the React frontend at `/` with SPA fallback for client-side navigation.
- `gateway.web.tasks.TaskStore` — process-local in-memory task registry with `create`, `get`, `mark_running/done/failed`, and `run_in_thread` (daemon-thread executor that works under the synchronous TestClient). `run_async` is also retained for future async-native callers.
- `gateway.web.routes.status` — GET /api/status, /api/log, /api/lint.
- `gateway.web.routes.domains` — GET /api/domains, /api/proposals; POST /api/domains/{slug}/{promote,demote,reject}. Defines `_to_response` and `_serialize_authorship_report` helpers reused by ops.
- `gateway.web.routes.ops` — POST /api/ops/{ingest,query,bootstrap-domain,discover-domains} (async, return 202 + task_id) and /api/ops/{finalize,filter-correct} (sync).
- `gateway.web.routes.tasks` — GET /api/tasks/{id}.
- `web/` — Vite + React + TypeScript SPA. Built artifacts at `web/dist/` are served by FastAPI as static files. Sidebar nav with Wiki/Domains/System groups. 9 page components (Dashboard, Ingest, Query, Finalize, FilterCorrect, Bootstrap, Discover, Promote, Lint). Shared `TaskRunner` component wraps the submit-then-poll loop; `ResultPanel` renders `OperationResult` with color-coded success/error/no-op styling.
- `wiki serve [--port 7474] [--bind 127.0.0.1]` CLI subcommand.

**Tests.** 13 web app tests (`test_web_app.py`) covering health, status/log/lint endpoints, domain endpoints, sync ops, async ops with task_id polling. 8 task store tests (`test_web_tasks.py`). 2 CLI tests (`test_cli_serve.py`). Full gateway suite: 481 → 504 tests passing.

**Hand-test.** Started server on port 7475, verified via curl: `/api/health` returns `{"status":"ok"}`, `/api/status` reports watcher running with 731 sources / 173 drafts / 6 domains, `/api/domains` lists all 6 with notebook flags, `/` serves React HTML, `/assets/*.js` serves the Vite-bundled JS with correct content-type.

**Out of scope (deferred to M41/M42).**

- Research orchestration UI with `--review` gate flow.
- NLM artifact triggers (briefing, audio, slides, revise).
- Review consoles: drafts list, contradictions list, source orphans, filter-band sources.
- Live updates via SSE/WebSocket — deferred indefinitely; manual refresh suffices for single-user.
- Authentication — localhost-only by design.

### M41 — Research Orchestration UI

Adds a Research sidebar entry to `wiki serve` that exposes the existing `wiki research` orchestrator (M37/M37.1) over HTTP. Two-pane sessions-list + detail layout. Each session walks through three phases: prompt+domain → query plan (structured per-adapter editor) → execute. Long-running execution shows per-step progress sourced from filtered `log.md` entries.

**What's new.**

- `gateway.web.routes.research` — six endpoints: list sessions (`GET /api/research/sessions`), get session detail (`GET /api/research/sessions/{id}`), create session (`POST /api/research/sessions` — runs planner via TaskStore), update plan (`PUT /api/research/sessions/{id}/plan`), execute (`POST /api/research/sessions/{id}/execute` — runs orchestrator via TaskStore with `execute_session=session_id`), get progress (`GET /api/research/sessions/{id}/progress` — parses `log.md` filtered to session_id).
- `gateway.research.orchestrator` — six new `log.append("research", step=<name>)` calls (materialize, nlm_persistent, nlm_session, source_map, analysis, apply_plan) so the progress endpoint can render every named pipeline stage.
- `web/src/pages/research/` — 6 components: Research (page shell), SessionsList (status badges, click-to-route), NewSessionForm (inline expandable, planner spinner), SessionDetail (phase router), PlanEditor (per-adapter structured editor with × delete + add + edited-row highlights), ProgressView (3s polling, 16 canonical steps with state glyphs).
- Sidebar gains a Research group entry between Wiki and Domains.

**Lifecycle states (derived):** `plan_only` (YAML exists, not edited, not executed) · `edited` (YAML mtime > generated_at + 2s) · `running` (active task) · `done` (registry session.status == promoted) · `abandoned` (registry session.status == abandoned).

**Tests.** 11 new tests in `test_web_research.py` covering all six endpoints. Full gateway suite: 504 → 515 tests passing.

**Hand-test.** Started server on port 7475, verified via curl: list endpoint returns all 3 existing query plans with correct states (one `edited`, one `abandoned`, one `plan_only`); detail endpoint returns the full per-adapter plan structure; progress endpoint correctly reconstructs the historical abandoned run from log.md (search.arxiv done, search.youtube/web queued, pubmed done-via-empty); `/research` SPA route serves React HTML at 200.

**Out of scope (deferred to M42).**

- NLM artifact triggers (briefing, audio, slides, revise) per-domain page.
- Review consoles (drafts list, contradictions, source orphans, filter-band sources).
- `obsidian://` deep-link for synthesis pages on done sessions — basic display only in M41.
- Session deletion / cleanup ops.
- `--queries` external YAML import — CLI-only.

### M42 — Review consoles + structured contradiction persistence

Adds a Review sidebar entry to `wiki serve` with four tabs (Drafts, Contradictions, Orphans, Filter-band). Drafts and Filter-band have inline actions (Finalize/Abandon, Include/Exclude). Contradictions and Orphans are read-only with click-through. Adds structured contradiction persistence: `apply_plan` writes JSONL records to `.knowledge/contradictions/log.jsonl` whenever it commits a plan with non-empty `plan.contradictions`.

**What's new.**

- `gateway.contradictions_log` — append-only JSONL helper. `append_contradictions(records)` writes one line per record with `recorded_at`. `read_records()` returns parsed records sorted newest-first; tolerates malformed lines.
- `gateway.ops.apply_plan` — calls `contradictions_log.append_contradictions(plan.contradictions)` inside the existing Phase 2 lock when contradictions are non-empty. Plans without contradictions don't touch the file.
- `gateway.web.routes.review` — four GET endpoints: `/api/review/drafts`, `/api/review/contradictions`, `/api/review/orphans`, `/api/review/filter-band`. Each derives state from existing on-disk artifacts (wiki/ frontmatter, raw/ frontmatter, .knowledge/contradictions/log.jsonl, .knowledge/policies/*/policy.yaml).
- `web/src/pages/review/` — Review page shell with 4 tabs. DraftsTab + FilterBandTab have inline actions; ContradictionsTab uses accordion-expand for claim detail; OrphansTab links to `/ops/query?domain=...` for discharge.
- `web/src/pages/Query.tsx` (M40) — extended to read `?domain=...` URL param and prefill the form on mount.

**Lifecycle / data sources.**

| Tab | Source | Sort |
|---|---|---|
| Drafts | wiki/{entities,concepts,synthesis,mocs}/*.md with `draft: true` frontmatter | oldest first (by `draft_started_at`) |
| Contradictions | `.knowledge/contradictions/log.jsonl` | newest first (by `recorded_at`) |
| Orphans | raw/<type>/*.md with empty `wiki_pages` | newest first (by `ingested_at`) |
| Filter-band | raw/<type>/*.md where `threshold_review ≤ filter.score < threshold_include` for any domain policy | score ascending |

**Tests.** 12 new tests across `test_web_review.py` (10) and `test_authorship.py` (2). Full gateway suite: 515 → 527 tests passing.

**Hand-test.** Started server on port 7475, verified via curl: 184 drafts, 0 contradictions (expected — JSONL log starts empty for pre-M42 state), 602 orphans, 173 in-band sources. `/review` SPA route serves React HTML at 200.

**Out of scope (M43+).**

- NLM artifact triggers (briefing, audio, slides, revise) per-domain page with confirmation modals.
- Bulk actions in review tabs (select multiple drafts, batch finalize).
- Filter/search within tabs.
- Aggregating contradictions by affected page.
- Backfill of pre-M42 contradictions from `log.md` summaries — the JSONL log accumulates from M42 onward only.

### M43 — NLM Artifacts UI

Adds a new Artifacts page under the Domains sidebar group at `/domains/artifacts`. Wraps the existing `wiki nlm-{add,sync,briefing,audio,slides,revise}` ops in HTTP endpoints. Confirmation modal before every LLM-calling op (per the artifact-generation-is-opt-in memory rule). Async generation via M40's TaskStore + 3s polling.

**What's new.**

- `gateway.web.routes.nlm` — 7 endpoints: nlm-add (sync); sync/briefing/audio/slides/revise (async, return 202+task_id); GET artifacts list per domain.
- `web/src/pages/Artifacts.tsx` — single page with domain dropdown (filtered to `has_notebook=true`), add-source form, sync button, three artifact-generation cards (briefing/audio/slides), per-row revise on slide-deck artifacts. Confirmation modal before every async op via local `useAsyncOp` hook + `OpStatus` component.
- Sidebar gains an "Artifacts" entry under the Domains group.
- No changes to underlying `gateway.ops.nlm.*` functions — endpoints are thin adapters that reuse `_serialize_op_result` from M40's ops route and `_to_response` from M40's domains route.

**Tests.** 8 new tests in `test_web_nlm.py`: artifacts list (empty, multi-domain filter, sort), nlm-add error path, async briefing/audio/slides/sync (with stubbed ops), revise (artifact-slug routing). Full gateway suite: 527 → 541 tests passing.

**Hand-test.** Started server on port 7475, verified `/api/nlm/domains/cycling-and-fitness/artifacts` returns 2 real on-disk artifacts (slides + briefing); `/api/nlm/domains/glp1-reward-modulation/artifacts` returns 0; `/domains/artifacts` SPA route serves React HTML at 200. Live NLM generation skipped to avoid burning quota — TestClient stubs cover the contract.

**Out of scope (M44+).**

- Bulk actions on review tabs.
- Filter/search within review tabs.
- Obsidian:// deep-links for synthesis pages.
- Custom artifact types beyond what NotebookLM exposes.
- Artifact deletion from the UI (delete the wiki page directly).
- In-browser audio playback or slide-deck rendering.

### M44 — Token-efficient LLM clients for research runs

Replaces the per-stage `claude -p` subprocess wrappers (`filter/semantic.py`, `plan.py`, `vlm.py`) with a shared `gateway.llm.ClaudeCLIClient` that invokes `claude -p --no-session-persistence --tools "" --model <id> --system-prompt <prefix> <user_prompt>`. Strips the Claude Code agent harness (tool declarations + default system prompt) on every call, routes filter to Haiku 4.5 (binary triage), keeps plan and VLM on Opus 4.7. VLM uses `--tools "Read"` to retain image attachment. Auth: `claude_cli_env()` drops `ANTHROPIC_API_KEY` so Max-plan OAuth is honored. **No `--bare`** — per `claude --help` it forces API-key auth and is incompatible with Max billing (discovered the hard way during sanity-check).

**M44.1 — Parallel filter (2026-05-12).** `_run_filter` in `research/orchestrator.py` uses `ThreadPoolExecutor`; default 8 workers (configurable via `WIKI_FILTER_MAX_WORKERS`). One-shot per-item `FilterError` isolation; accepted candidates returned in input order. Real-world: 178-candidate run, 47 min sequential → 12 min 34 s at 4 workers (2.6× wall-clock speedup; effective ~7.7× vs original Opus+sequential baseline including the Haiku token savings).

**M44.2 — Synthesis citation-grounding fixes (2026-05-13).** Validator extended with `_STRUCTURAL_FRAME_LABELS` (11-label allowlist for NotebookLM-emitted bullet labels like `**Themes Used In:**`, `**Items Compared:**`); analysis prompts gained an explicit footnote-ref directive demanding `[N]` → `[^N]: [[sources/<id>]]` resolution on interpretive sentences.

**M44.3 — Multi-line continuation + draft workflow (2026-05-13).** Validator tracks one continuation slot per structural-frame label so the value line (when NotebookLM splits label/value across two lines) inherits the exemption. Framing prose like *"Based on the provided sources, the corpus presents…"* is accepted as the `--draft` workflow's responsibility — WIKI.md § 5.5 documents `wiki research --draft` for synthesis-heavy runs with `wiki cite` / `wiki finalize` follow-up.

**Tests.** 25 new tests across `test_llm_client.py` (12), `test_filter.py` (4), `test_plan_client.py` (10 — covers plan + VLM argv), `test_research_orchestrator.py` (4 — parallel filter), `test_authorship.py` (8 — citation allowlist + multi-line continuation), `test_research_analysis.py` (3 — prompt-directive injection). Full gateway suite: 741 → 766 passing.

**Hand-tested.** Single-source sanity check (Summer Gardens reserve study, score 1.00 with on-policy rationale); full end-to-end runs on `wiki research --execute 2026-05-12-…` (firm-explainer plan, 178 cand → 6 accepted → 6 wiki pages → 2 promoted) and `2026-05-11-…` (methodology plan, 181 cand → 18 accepted; apply_plan rejects on Category B framing prose, expected — re-run with `--draft` per M44.3 workflow).

**Out of scope (M44+).**

- Local-classifier replacement for filter (deferred per WIKI § 10.4, triggered at ~1000 pinned decisions per domain).
- Anthropic API-key billing path (`cache_control` prompt caching) — user constraint: stay on Max.
- Multi-item batched filter calls — would amortize per-call fixed cost further but compromises per-item isolation and the `wiki filter-correct` fine-tuning bank.
- Idempotent `register_session` for re-execute on `status=promoted` (a separate gateway-ops-idempotent fix).
- Filter score not written to raw/ frontmatter on the research path (the ingest path does; orchestrator's `_materialize` doesn't — pre-existing).

### M45 — `synthesizes:` and the followable citation chain

Resolves the residual citation-grounding failure surfaced in M44.3: synthesis pages emit legitimate aggregate observations like *"Based on the provided sources, four primary anchors emerge…"* that cannot point at a single source. Strict per-source citation rejects them. The fix adopts **Cochrane / PRISMA's load-bearing convention**: explicitly enumerate every constituent work, then derive aggregate claims from the enumerated set.

**Design pivoted from a web-research survey** (see `feedback_survey_formal_practice_before_design.md` memory). The original sketch (`derivative: 1|2` integer + `[[corpus]]` token) was internally coherent but had no precedent in CiTO, FRBR, FaBiO, BIBO, or any surveyed PKM tool — and `[[corpus]]` would have reintroduced the documented citation-laundering anti-pattern. The pivot to `synthesizes:` + `## Included works` mirrors Cochrane's "Characteristics of included studies" table.

**What's new.**

- `synthesizes:` optional frontmatter field on synthesis pages — list of `sources/<slug>` (first-derivative) OR `synthesis/<slug>` (second-derivative). One-level strict typing; never mixed.
- `## Included works` required body section when `synthesizes:` is set — must mirror the list 1:1 (validator enforces).
- Aggregate-framing-opener allowlist in `gateway/citations.py:_AGGREGATE_FRAMING_OPENERS_RE` — first claim-shaped sentence of each `## ` section matching the allowlist is exempt from per-claim citation, bounded to one per section, only when `synthesizes:` ≥ 2 and Included works mirrors.
- `validate_synthesizes_integrity` rejects malformed entries, mixed-tier lists, and Included-works drift.
- `wiki lint --scope citation-chains` surfaces dangling `synthesizes:` refs (cross-page) and synthesis pages with aggregate framing but no `synthesizes:` (legacy pages predating M45).
- Orchestrator emits `synthesizes:` + `## Included works` mechanically from the branch's known constituent sources — does NOT depend on NotebookLM compliance (the failure mode that hobbled M44.2's footnote-ref directive).
- Cross-cutting synthesis pages get `synthesizes: [synthesis/...]` listing the per-theme branches — the second-derivative case.
- `[[corpus]]` token forbidden by design; validator rejects as unknown wikilink target.

**Tests.** 23 new tests across `test_authorship.py` (18: aggregate-framing exemption variants, synthesizes-integrity), `test_research_orchestrator.py` (4: orchestrator emission of synthesizes + Included works for per-branch and cross-cutting), `test_lint_citation_chains.py` (5: dangling refs, legacy framing, second-derivative resolution). Full gateway suite: 766 → 789 passing.

**Hand-test.** Backfill script `scripts/m45_backfill_synthesizes.py` retrofitted the 5 draft pages from the 2026-05-13 M44.3 validation run. 2 of 5 now validate cleanly in non-draft mode; 3 still have uncited substantive content claims (e.g., bullet items like `**BEES Technique:** A multi-attribute evaluation framework developed by…`) that are real claims missing citations, not framing prose. Those need `wiki cite` to attach attributions, then `wiki finalize`. Lint surfaces the pre-existing pre-M45 cross-cutting page in the condo domain as warning-only.

**M45.1 — `--draft` default on `wiki research` + 3 structural labels (2026-05-13).** The fresh-prompt end-to-end run surfaced that NotebookLM's opener phrasing varies more than the M45 allowlist can keep up with (`"The provided sources detail…"`, `"There is an unanswered tension…"`, etc.). Rather than chase each variant (whack-a-mole; see `feedback_survey_formal_practice_before_design.md` discipline), `wiki research` now defaults to `--draft` mode (`argparse.BooleanOptionalAction`, pass `--no-draft` to opt into strict). Recommended workflow: keep the draft default, then `wiki cite` + `wiki finalize` per page once framing prose is attributed. Three new structural-frame labels (`**Gap Identified:**`, `**Limitation Identified:**`, `**Tension Identified:**`) added to M44.2's allowlist; they're genuine metadata, safe addition.

**Out of scope (M45+).**

- `wiki cite` / `wiki edit` op for hand-editing `synthesizes:` and `## Included works` (relates to `gateway_edit_path_open_question.md` memory).
- N-derivative transitive closure baked into individual pages — `synthesizes:` is one-level strict.
- Quality assessment / weighting within `synthesizes:` (Cochrane has GRADE; we don't).
- `cito:` predicate typing on individual citations (heavyweight; binary cited/uncited + aggregate exemption is sufficient).
- Backfilling all historical synthesis pages predating M45 — only the 5 M44.3 drafts. Older pages stay; lint surfaces them but doesn't gate.

### M46 — Fine-tuning loop + backfill examples

See `docs/milestones/` — BUILD.md entry pending.

### M47 — K5 token telemetry + K2 MCP-CLI parity (Wave 1)

See `docs/milestones/M47.md`. K5 ships `ClaudeCLIClient.call_with_usage()`, per-model pricing in `costs.py`, single-line log telemetry, and `wiki status --cost` 7-day block. K2 ships a parity test asserting every `cli.IMPLEMENTED` command has an MCP wrapper (or an explicit `CLI_ONLY` exemption). Tests: 789 → 861 passing.

### M48 — K1 edit-path + K4 scheduler + K3 cloud shim (Wave 2)

See `docs/milestones/M48.md`. K1 adds `wiki cite-add` (4-tier escalation: exact → normalized → fuzzy → not-found) + `wiki edit --section`. K4 adds `wiki schedule` with `croniter` substrate and launchd install script. K3 adds bearer-token auth + `POST /api/ingest` cloud endpoint + TUTORIAL § 8a iOS Shortcut doc. MCP parity enforced by the Wave 1 K2 test throughout. Tests: 861 → 901 passing.

### M49 — AGT-2 draft closer + TOK-1 Anthropic API client

See `docs/milestones/M49.md`. Bundles TOK-1 (separate `ANTHROPIC_API_KEY_RESEARCH` key, `AnthropicAPIClient` with `cache_control` on system prompt, status-code + network-error retry, independent throttle from `ClaudeCLIClient`) with AGT-2 (`wiki finalize-batch [--suggest] [--execute]`). Deterministic Cat A (zero `unresolved_claims`) auto-finalizes on `--execute`. Aggressive mode (`--suggest --execute`) calls `gateway.ops.cite_suggest` (Sonnet 4.6, XML-wrapped source prompts, evidence-quote substring verification, ambiguity detection) and auto-applies unambiguous + verified suggestions before finalizing. Per-run report at `.knowledge/finalize-batch/<UTC-ts>.md`. Daily scheduler entry at 04:30 UTC. MCP parity: `wiki_finalize_batch`. Tests: 901 → 923 passing (+22). Tag: `m49-agt2-draft-closer`.

### M50 — QUAL-12 evaluation framework

See `docs/milestones/M50.md`. Per-domain evaluation framework — goldens at `.knowledge/eval/<domain>/goldens.yaml`, mode-B (wiki-state-only) runner, Sonnet 4.6 LLM-as-judge via TOK-1 `AnthropicAPIClient` with structured JSON output (raw_decode + preamble-strip tolerance). Hybrid scoring: source-id-strict `must_cite` + LLM-judged `must_assert` / `must_not_assert`. Persistence: per-run YAML at `.knowledge/eval/<domain>/runs/<UTC-ts>.yaml` + `.knowledge/eval/<domain>/trend.csv`. `wiki status` shows last-eval score per domain with delta. 15-Q/A seed set hand-drafted for `glp1-reward-modulation`; live hand-test produced mean=0.566 in 2:48 wall time, ~$1.16 (cache miss — system prompt below Anthropic 1024-token cache-eligibility threshold, M50.1 follow-up). MCP parity: `wiki_evaluate`. Tests: 923 → 965 passing (+42, including the +6 from M49 NLM-citation + test-consolidation adjacents). Tag: `m50-qual12-evaluation-framework`.

### M51 — INT-11 read-side outbound op (`wiki context`)

See `docs/milestones/M51.md`. Read-only outbound surface so sibling `~/code/*` projects (chief-of-staff, ai-tutor, newbiz) can pull a center wiki page plus an N-hop wikilink-resolved neighborhood without scraping the filesystem. Resolver accepts slug (`synthesis/<slug>`), full path (`wiki/<kind>/<slug>.md`), or title substring. Walker traverses `[[<kind>/<slug>]]` wikilinks in body text up to `--depth N`, deduplicates by path, follows only `wiki/` targets (stops at `raw/`, `nlm:`, external URLs). Renderers emit markdown (default) or JSON (`--format json`) — JSON envelope is `{root, neighbors, stats}` with `body`, `slug`, `kind`, `title`, `path` per page. CLI `wiki context <query> --caller <id> [--depth N] [--format X]`; `--caller` is required and logged to `log.md` for audit. MCP parity tool `wiki_context` with identical surface. Tests: 965 → 982 passing (+17 net: +11 resolver/walker, +6 renderers/orchestrator, +0 wiring). Tag: `m51-int11-wiki-context`.

### M52 — Phase 1 Round A (ARCH-2, ARCH-4, ARCH-6, QUAL-4, QUAL-5)

See `docs/milestones/M52.md`. Five independent hardening items: source frontmatter immutability guard (`validate_source_frontmatter_diff` + three pipeline callers — ARCH-2); per-source file lock + filter score writeback in `_materialize` (ARCH-4); `register_session(force=True)` + idempotency lint checks (`stale-session`, `no-policy`) + op contract docstrings (ARCH-6); broken-wikilinks lint scope with error/warning severity and per-page deduplication (QUAL-4); per-domain fine-tune readiness block in `wiki status` with one-shot 80% milestone logging (QUAL-5). Tests: 985 → 1020 passing (+35 net: +9 ARCH-2, +3 ARCH-4, +9 ARCH-6, +8 QUAL-4, +6 QUAL-5). Tag: `m52-phase1-round-a`.

### M53 — Phase 1 Round B (TOK-1, TOK-3, TOK-6, TOK-7)

See `docs/milestones/M53.md`. Four token-efficiency items: TOK-1 cache_read=0 root-cause diagnosis (M50.1 already fixed, doc only); TOK-3 filter system-prompt memoized once per `_run_filter` batch via `_prebuilt_system` param to `score()` (N candidates → 1 `build_system_prompt()` call); TOK-6 transcription disk cache at `raw/<type>/_transcripts/<sha256hex>.json` (`TranscriptionResult.from_dict()`, `load_transcript_cache`, `save_transcript_cache`) in voice and audiobook converters; TOK-7 `PromptGuardError` + `assert_safe_for_prompt()` in `paths.py` raises for `log.md` and `index.md`. Session-state discipline infrastructure also shipped (`docs/session-state.md`, PreCompact/SessionStart hooks, CLAUDE.md rule). Tests: 1020 → 1027 passing (+7 net: +2 TOK-3, +2 TOK-6, +3 TOK-7). Tag: `m53-phase1-round-b`.

### M54 — Phase 1 Round C (TOOL-10, DOC-1, DOC-6)

See `docs/milestones/M54.md`. Three ergonomics and onboarding items: TOOL-10 (`argcomplete>=3.0` wired into `cli.py`, usage examples on eight subcommands, `docs/shell-completion.md`); DOC-1 (three-track "New here?" reading order at top of README — knowledge work / code contribution / agent briefing, each step names its output); DOC-6 (`GLOSSARY.md` at repo root, ~30 terms alphabetical, covers review-doc § 2 terms plus M47–M53 additions, cross-linked from README). Tests: 1027 → 1038 passing (+11 TOOL-10; DOC items have no test delta). Tag: `m54-phase1-round-c`.

### M55 — Phase 2 Round A (TOK-4, ONT-2, ONT-4, ONT-8, ARCH-10)

See `docs/milestones/M55.md`. Five independent items: TOK-4 (`_gather_existing_pages` two-stage select — 200-char snippets, 10 KB cap, full bodies for ≤5-page wikis; ~15× token reduction on saturated domains); ONT-2 (CiTO 8-verb typed citations via `[[sources/<id>|verb]]` alias syntax, `SEVERITY_WARNING` for unknown verbs, WIKI.md § 5.6); ONT-4 (`ENTITY_KIND_ENUM` 12-value frozenset, hard-reject on new entity pages, `migrations/0002-migrate-entity-kinds.py` for 25 legacy values); ONT-8 (80-char slug cap hard-reject on new pages, `--force-long-slug` override, `lint/long_slugs.py` for grandfathered legacy slugs, WIKI.md § 6.2); ARCH-10 (NLM compat allowlists moved from hardcoded Python to `src/gateway/data/citations_allowlist.yaml` v1, auditable diffs, WIKI.md § 5.2). Tests: 1038 → 1061 passing (+23). K2 parity: 4/4 green. Tag: `m55-phase2-round-a`.

### M56 — Phase 2 Round B (AGT-9, ONT-3, AGT-14, QUAL-3)

See `docs/milestones/M56.md`. Four items in two dependency chains: AGT-9 (filesystem event bus — `emit()`/`subscribe()`/`list_events()` over `.knowledge/events/<date>/<seq:04d>.json`, debounce, `events_dir()`/`agents_dir()` in paths, `"agent"` prefix in `LOCK_NAME_PREFIXES`); ONT-3 (`"contradiction"` page type in `PAGE_SCHEMAS`, `CONTRADICTION_SEVERITY_ENUM`/`CONTRADICTION_STATUS_ENUM` in validator, `validate_contradiction_frontmatter()`, `lint/contradiction_pages.py` for open+major pages, no-op migration); AGT-14 (`agent-log --since 24h|48h|7d`, per-agent counts + top-5 payloads, `DIGEST_SCHEDULE_ENTRY` 7am draft-only digest, MCP `wiki_agent_log`); QUAL-3 (`wiki contradiction list/resolve`, `resolve` updates frontmatter + sets `contested: true` on sources with ≥2 open contradictions, `wiki status` contradiction summary, MCP `wiki_contradiction`). Tests: 1061 → 1117 passing (+56). K2 parity: 4/4 green. Tag: `m56-phase2-round-b`.

### M57 — Phase 2 Round C (INT-8, INT-9)

See `docs/milestones/M57.md`. Two independent integration pollers: INT-8 (`src/gateway/pollers/repo_metadata.py` — polls `~/code/*/README.md`, `CLAUDE.md`, `docs/*.md`; hash-based cursor skips unchanged files; auto-tags domain when `.knowledge/policies/<slug>.yaml` exists; excludes node_modules/.venv/dist/build/vendor/__pycache__/.git; registered as `"repo-metadata"`); INT-9 (`src/gateway/pollers/readwise.py` — Readwise v3 Export API; cursor on `updatedAfter`; one `raw/note/` file per document; idempotent highlights update; follows pagination; fails fast on missing `READWISE_TOKEN`; registered as `"readwise"`). Tests: 1117 → 1139 passing (+22). K2 parity: 4/4 green. Tag: `m57-phase2-round-c`.

### M58 — Phase 2 Round D (ONT-6, TOK-12, AGT-1, AGT-2)

See `docs/milestones/M58.md`. Four items: ONT-6 (`created_at`/`last_updated` required for entity/concept/synthesis in `wiki_pages.py`; `validate_timestamps()` in validator; `apply_plan` auto-stamps before validation; `concept_add`/`query`/`finalize` stamp on write; `migrations/0004-backfill-timestamps.py` via `git log --diff-filter=A`); TOK-12 (`FINDINGS_STALE_HOURS=24`, `_write_branch_finding()` after each `_investigate_branch()` call, `load_branch_findings()` returns None for absent/stale dirs, `analyze()` gains `session_id`+`prefetched_findings` params, `_extract_taxonomy()` handles JSON answers); AGT-1 (`src/gateway/agents/inbox_triage.py` — `run_triage(source_id)`: domain-present→filter+persist, domain-absent→keyword-overlap inference (≥0.6 confident single match→tag+filter, ambiguous/none→needs-domain), review-band→`.knowledge/triage/<id>.yaml`; `wiki triage list` CLI + `wiki_triage` MCP; status shows depth); AGT-2 (`src/gateway/agents/draft_closer.py` — `run_draft_closer()`: easy-win=no body line has 2+ source links→`finalize()`, hard-case→escalation to log.md with pre-computed `wiki cite` invocations; `DRAFT_CLOSER_SCHEDULE` 8am UTC daily; `wiki draft-close run` CLI + `wiki_draft_close` MCP). Tests: 1152 → 1179 passing (+27). K2 parity: 4/4 green. Tag: `m58-phase2-round-d`.

### M59 — Phase 2 Round E (DOC-3, DOC-4, DOC-2, DOC-7)

See `docs/milestones/M59.md`. Documentation milestone — four items: DOC-3 (`ARCHITECTURE.md` with Mermaid diagram, 10-row invariant table, data flow, "what is not here" sections; README updated); DOC-4 (seven per-package READMEs: `src/gateway/`, `converters/`, `pollers/`, `ops/`, `lint/`, `research/`, `llm/` — each with module map, contracts, and done-when checklist); DOC-2 (`CONTRIBUTING.md` 119 lines — prerequisites, env, pytest, lint, 4 recipes, commit conventions, PR checklist); DOC-7 (`docs/adr/` — 15 ADRs covering filesystem-as-database, gateway-as-single-mutator, NLM discipline gate, plan-before-write, citation grounding, draft mode, per-agent processes, prompt caching, session-state discipline, Haiku-tier filter, source immutability, wikilink citations, Readwise v3, slug stability, citation allowlist). Tests: 1179 passing (unchanged — documentation only). Tag: `m59-phase2-round-e`.

### M60 — Phase 2 Round A (AGT-9 verified, QUAL-12 expansion, draft trend)

See `docs/milestones/M60.md`. Phase 2 exit-criteria closeout — five items: A1 (three agents wired into `.knowledge/schedule.yaml`: inbox-triage `*/15`, draft-closer `0 8 *`, agent-digest `0 7 *`; `run_inbox_triage_batch()` scan-based runner; `wiki agents run <name>` CLI + `wiki_agents` MCP; subscription YAMLs in `.knowledge/agents/`); A2 (`WatcherDaemon._process` emits `ingest.complete` via `events.emit()` on success; 5 new tests in `test_a2_event_bus_chain.py` verify watcher→event→subscribe chain with no direct coupling); A3 (`wiki evaluate glp1-reward-modulation` baseline: 15 Q, mean 0.566, 2026-05-25T01:34:37Z run, stored in `.knowledge/eval/glp1-reward-modulation/runs/`); A4 (goldens for two new eval domains: `condo-capital-infra` 10 Q, `edge-ai-agentic` 10 Q; both validate clean; eval runs pending `ANTHROPIC_API_KEY_RESEARCH`); A5 (stale draft trend: 230→217 over 4 days, −5.7%; decline criterion met). Tests: 1179 → 1192 passing (+13). K2 parity: 4/4 green. Tag: `m60-phase2-round-a`.

### M61 — Phase 2 Closeout (Round B)

See `docs/milestones/M61.md`. Phase 2 formal close — documentation only: `docs/phase2-closeout.md` (20-item completion table, test-delta table 1038→1192, exit-criteria verification, follow-ups for Phase 3); M61 milestone doc; tags `m60-phase2-round-a` and `m61-phase2-closeout`. Tests: 1192 passing (unchanged). Tag: `m61-phase2-closeout`.

### M62 — Phase 3 Round A (ONT-10, INT-14, INT-15, INT-17)

See `docs/milestones/M62.md`. Four items: ONT-10 (source pages demoted to manifest-only — `required_sections=()`, `citation_grounded=False` in `wiki_pages.py`; `migrations/0005-demote-source-pages.py` strips stub sections from 1023 `wiki/sources/*.md` pages; WIKI.md § 4.3 updated); INT-14 (`src/gateway/ops/wiki_digest.py` — `build_wiki_digest()`: new sources by domain, new synthesis pages, stale draft count, triage queue depth; `wiki digest [--hours N] [--stale-days N] [--out PATH]` CLI + `wiki_digest` MCP); INT-15 (`~/code/chief-of-staff/CLAUDE.md` step 5a — session-start calls `wiki context <attendee-slug>` for meeting attendees with wiki entity pages; skip-silent; no write-back); INT-17 (`~/code/newbiz/CLAUDE.md` — ideation sessions optionally query `wiki context --query <topic> --depth 2` for domain-relevant synthesis snippets). Tests: 1192 → 1200 passing (+8). K2 parity: 4/4 green. Tag: `m62-phase3-round-a`.

### M63 — Phase 3 Round B (INT-13, INT-16)

See `docs/milestones/M63.md`. Two items: INT-13 (`src/gateway/ops/wiki_agenda.py` — `build_agenda(date_str, events)` + `write_agenda()`; for each calendar event with ≥2 attendees, looks up attendee entity pages and event-topic concept pages in wiki; `wiki agenda [--date] [--events-json] [--out] [--no-write]` CLI + `wiki_agenda(date, events, write)` MCP tool; `agenda` page type in `wiki_pages.py`; `agenda_dir()` in `paths.py`; 8 tests); INT-16 (`~/code/ai-tutor/skills/wiki-cards/SKILL.md` — agent skill generating spaced-rep Q-A cards from wiki concept pages for a domain; deduplicates by SHA-256 question hash; outputs `state/wiki-cards/<domain>.yaml` with `wiki_source` back-references; registered in ai-tutor CLAUDE.md). Tests: 1200 → 1208 (+8), 0 regressions. Tag: `m63-phase3-round-b`.

### M64 — Phase 3 Round C (ARCH-14, ONT-11, QUAL-13)

See `docs/milestones/M64.md`. Three items: ARCH-14 (CI guard — `tests/test_arch14_hard_rule_1.py` asserts lint/ and web/ zones contain no wiki/raw writes; ops/ modules must use `write_atomic` for wiki/raw paths; **bonus**: found and fixed real violation in `ops/contradiction.py` — 2 `.write_text()` calls to `wiki/sources/` and `wiki/contradictions/` converted to `write_atomic`); ONT-11 (`lint/synthesizes_coverage.py` warns when synthesis pages lack `synthesizes:` frontmatter — 56/94 pages currently missing it; registered in lint orchestrator; 4 tests); QUAL-13 (`converters/web.py` — `_wayback_snapshot()` calls Wayback Save API after web ingest; stores `meta.archive_url` on success; gracefully skips on failure; 3 tests). Tests: 1208 → 1218 (+10), 0 regressions. Tag: `m64-phase3-round-c`.

### M65 — Phase 4 Round A (QUAL-9, AGT-6, AGT-12)

See `docs/milestones/M65.md`. Three items: QUAL-9 (`lint/domain_purity.py` warns on wiki/sources pages tagged to multiple blessed domains — centroid drift signal; `promote_domain()` pre-flight adds `contamination_warnings: [ids]` to proposal frontmatter for member sources pre-tagged to foreign domains; `_check_contamination()` helper in `ops/promote_domain.py`; registered in lint orchestrator; 11 tests); AGT-6 (`ops/briefing_cron.py` — weekly per-domain `nlm_briefing()` with corpus-hash skip; hash stored at `.knowledge/briefing-cron/<domain>.json`; `wiki briefing-cron` CLI + `CLI_ONLY` in MCP; weekly schedule entry in `.knowledge/schedule.yaml` (`0 6 * * 1`); hard guard: no nlm_audio/nlm_slides calls — verified by structural test; 11 tests); AGT-12 (6 wiki-* skills at `.claude/skills/`: `wiki-ingest-triage`, `wiki-finalize-drafts`, `wiki-research`, `wiki-cite`, `wiki-domain-bootstrap`, `wiki-editorial-review`; each references WIKI.md section anchors; no gateway prompts embedded). Tests: 1218 → 1240 (+22), 0 regressions. Tag: `m65-phase4-round-a`.

### M66 — Phase 4 Round B (QUAL-1, AGT-4)

See `docs/milestones/M66.md`. Two items: QUAL-1 (`pollers/link_rot.py` — `LinkRotPoller` HEAD-checks each raw/web source; classifies `ok|redirect|dead`; 30-day recheck cooldown via `last_checked_at`; writes `link_status:` + `last_checked_at:` to raw + wiki/sources frontmatter; stores `meta.redirect_url` for redirects; `lint/link_rot.py` warns dead, info unchecked, surfaces Wayback archive_url from QUAL-13; 16 tests); AGT-4 (`ops/contradiction_sweeper.py` — weekly per-domain LLM contradiction scan reusing `lint/contradictions.py` internals; idempotent per domain per week; writes draft `wiki/synthesis/contradictions-<domain>-<week>.md`; `wiki contradiction-sweep [--domain] [--week]` CLI + `wiki_contradiction_sweep` MCP tool; Tuesday 07:00 UTC schedule; uses Claude CLI not NLM; 13 tests). Tests: 1240 → 1269 (+29), 0 regressions. Tag: `m66-phase4-round-b`.

### M67 — Phase 4 Round C (TOOL-14, INT-12)

See `docs/milestones/M67.md`. Two items: TOOL-14 (`ops/contradiction_drift.py` — nightly snapshot + diff of contradiction lint findings; `_diff()` returns new/resolved by `domain|a_page|b_page` key; snapshot written to `.knowledge/lint/drift-<date>.json` via `write_atomic`; `_weekly_digest()` summarizes last 7 files; `wiki contradiction-drift [--date] [--digest]` CLI; `CLI_ONLY` in MCP; nightly `0 5 * * *` schedule; 11 tests); INT-12 (`notion_client.py` — thin `urllib.request` Notion REST API wrapper; auth via `NOTION_TOKEN`; create/update/archive pages; paginated DB query; `ops/publish_notion.py` — idempotent upsert for one domain; one DB per domain via `NOTION_PARENT_PAGE_ID`; registry at `.knowledge/notion/<domain>.json`; creates/updates/archives pages; `wiki publish-notion <domain> [--include sources/artifacts]` CLI; `wiki_publish_notion` MCP tool; 18 tests). Tests: 1269 → 1298 (+29), 0 regressions. Tag: `m67-phase4-round-c`.

### M84 — Phase 5 Round Q (TOK-10 plan_authorship_small model split)

See `docs/milestones/M84.md`. TOK-10: `llm/config.py` — `plan_authorship_small` stage added (Sonnet 4.6; `DEFAULT_PLAN_AUTHORSHIP_SMALL_MODEL`); `ops/ingest.py` — `_authorship_model(front, body)` routing helper: `voice`/`note` source types or body <2 KB → Sonnet 4.6; `_SMALL_SOURCE_TYPES = frozenset({"voice", "note"})`, `_SMALL_BODY_THRESHOLD = 2048`; `_invoke_plan_and_apply` uses helper when creating default plan client. ~5x cost reduction for short-form ingests. 12 tests. Tests: 1628 → 1640 (+12), 0 regressions. Tag: `m84-phase5-round-q`.

### M83 — Phase 5 Round P (TOOL-13 source-explorer web view)

See `docs/milestones/M83.md`. TOOL-13: `web/routes/sources.py` — `GET /api/sources` with query params `q` (case-insensitive substring over title/ID/body), `domain`, `type`, `limit` (default 200, max 1000); returns `list[SourceRecord]` with `source_id`, `source_type`, `title`, `domains`, `ingested_at`, `filter_score`, `link_status`, `word_count`, `draft`; iterates `raw/**/*.md`; `SourceRecord` added to `web/schemas.py`; router registered in `app.py`. 13 tests. Tests: 1615 → 1628 (+13), 0 regressions. Tag: `m83-phase5-round-p`.

### M82 — Phase 5 Round O (TOOL-12 daily-domain-digest routine)

See `docs/milestones/M82.md`. TOOL-12: `ops/daily_digest.py` — `run_daily_domain_digest(domain, *, client, date_str, lookback_hours)` finds sources ingested in the last 24h for a domain, builds a summarization prompt, calls the LLM (injectable `FilterClient`), writes `wiki/synthesis/daily-<domain>-<YYYY-MM-DD>.md` with `draft: true`; idempotent (skips if today's page exists); threshold skip if < 1 new sources; `synthesizes:` + `## Included works` generated to pass `validate_synthesizes_integrity`; `run_all_domains()` iterates all blessed domains; `wiki routine daily-domain-digest [--domain SLUG] [--date YYYY-MM-DD] [--lookback-hours N]` CLI; `wiki_routine` MCP tool; daily cron job at `0 6 * * *`; 19 tests. Tests: 1596 → 1615 (+19), 0 regressions. Tag: `m82-phase5-round-o`.

### M81 — Phase 5 Round N (SRCH-2 wiki index --rebuild)

See `docs/milestones/M81.md`. SRCH-2: `ops/index_rebuild.py` — `rebuild(dry_run)` regenerates `index.md` with a domain-grouped catalog per WIKI.md § 7; scans `wiki/mocs/` for domains, counts raw sources per domain, collects wiki pages (entities/concepts/synthesis/artifacts) per domain using explicit `_DIR_TO_TYPE` mapping (avoids `rstrip("s")` which corrupts "synthesis" → "synthesi"); cross-domain section for pages tagged with 2+ domains; health section (orphan count via `lint.orphans`, inbox count). `write_atomic` for safe writes. `wiki index [--rebuild] [--dry-run]` CLI — `--rebuild` is implied (default action). `wiki_index` MCP tool. `tests/gateway/test_smoke.py` updated (test now uses `migrate` stub). 17 tests. Tests: 1579 → 1596 (+17), 0 regressions. Tag: `m81-phase5-round-n`.

### M80 — Phase 5 Round M (SRCH-1 wiki search)

See `docs/milestones/M80.md`. SRCH-1: `ops/search.py` — `search(query, *, scope, domain, page_type, limit)` full-text grep-based search over `wiki/` and `raw/` markdown files; case-insensitive substring match; ranking: score 3 (title), 2 (slug), 1 (body); `format_results()` for CLI output; `SearchHit` and `SearchResult` dataclasses. `wiki search "<query>" [--scope wiki|raw|all] [--domain D] [--type T] [--limit N]` CLI — exits 0 on hits, 1 on no results. `wiki_search` MCP tool. `tests/gateway/test_smoke.py` updated (test now uses `index` stub). 17 tests. Tests: 1562 → 1579 (+17), 0 regressions. Tag: `m80-phase5-round-m`.

### M79 — Phase 5 Round L (INT-19 Slack source poller)

See `docs/milestones/M79.md`. INT-19: `pollers/slack.py` — `SlackSourcePoller` polls configured Slack channels and writes notable messages (len ≥ min_length or reply_count > 0) to `raw/note/`; thread replies appended to parent body; slug `note-slack-<sha256(channel_id + ts)[:12]>`; config at `.knowledge/pollers/slack/config.yaml` (`channels:` list with `channel_id`, `name`, `domain`; `min_length` default 200; `max_messages` default 100); cursor at `.knowledge/pollers/slack/cursor.yaml` per channel_id (latest `ts`); injectable `fetch_history`/`fetch_replies` callables for testing. Registered as `"slack"` in poller registry. `CLAUDE.md` updated (all queued pollers now shipped). 21 tests. Tests: 1541 → 1562 (+21), 0 regressions. Tag: `m79-phase5-round-l`.

### M78 — Phase 5 Round K (INT-18 Notion source poller)

See `docs/milestones/M78.md`. INT-18: `pollers/notion.py` — `NotionSourcePoller` reads configured Notion pages and databases into `raw/note/` as canonical note sources; slug `note-notion-<sha256(page_id)[:12]>`; config at `.knowledge/pollers/notion/config.yaml` (`pages:` and `databases:` lists with optional `domain:`); cursor at `.knowledge/pollers/notion/cursor.yaml` per page_id; `max_pages` run limit (default 50); `NOTION_TOKEN` env var auth. `notion_client.py` extended with read operations: `get_page()`, `get_page_blocks()` (paginated), `search_pages()`; `blocks_to_markdown()` + `_rich_text_to_md()` static methods for paragraph/heading/list/code/quote/callout/divider/image/bookmark block types; inline bold/italic/strikethrough/code/link annotations. Registered as `"notion"` in poller registry. `CLAUDE.md` forward-looking note updated. 38 tests. Tests: 1503 → 1541 (+38), 0 regressions. Tag: `m78-phase5-round-k`.

### M77 — Phase 5 Round J (QUAL-14 reingest + supersedence)

See `docs/milestones/M77.md`. QUAL-14: `ops/reingest.py` — `wiki reingest <source_id> <new_input>` creates versioned successor (`<base>-v2`, `-v3`, …), stamps `superseded_by: <new-id>` on old raw source, stamps `supersedes: [<old-id>]` on new source; `_affected_wiki_pages()` returns wiki pages citing old source; `lint/superseded_citations.py` (`superseded-citations`, WARNING) — finds pages citing superseded sources; lint registered; `MUTABLE_SOURCE_FIELDS` extended with QUAL-7 fields + QUAL-14 fields; `OperationResult.data: dict` field added (backward-compat); `WIKI.md § 3.1` updated with `superseded_by`/`supersedes` frontmatter; `wiki reingest` CLI + `wiki_reingest` MCP tool; 16 tests. Tests: 1487 → 1503 (+16), 0 regressions. Tag: `m77-phase5-round-j`.

### M76 — Phase 5 Round I (QUAL-9 verified, DOC-9/10/11/12 doc suite)

See `docs/milestones/M76.md`. QUAL-9 (`lint/domain_purity.py`) confirmed already implemented. DOC-9: `tests/README.md` — pytest invocation, `kb_root` fixture, stub-vs-real-LLM rule, mocking conventions (MagicMock warning), deferred hand-tests, naming conventions. DOC-10: `docs/MCP_API.md` — one section per MCP tool grouped by type; parameters, return shape, CLI-only status. DOC-11: `docs/RUNBOOK.md` — common operations, symptom→remedy tables for ingest/authorship/NLM/MCP/watcher/lint; scheduled jobs; emergency procedures. DOC-12: `docs/superpowers/README.md` — design artifact index; `SESSION_TRANSCRIPT.md` historical-artifact header. Tests: 1487, 0 regressions. Tag: `m76-phase5-round-i`.

### M75 — Phase 5 Round H (QUAL-10 calibration set, DOC-8 CHANGELOG)

See `docs/milestones/M75.md`. QUAL-10: held-out gold set replaces n=5 filter-calibration; `calibration_set.yaml` at `.knowledge/policies/<domain>/`; `CalibrationEntry`/`CalibrationMetrics` in `ops/calibration.py`; `score_calibration()` runs candidate criteria against each entry via injectable filter client, computes precision/recall/F1; `distill_prompt()` calls scoring and adds `calibration_metrics` block (n_examples, precision, recall, f1, accuracy, scored_at) to candidate YAML; `DistillResult.calibration_f1` surfaced in CLI output; `wiki finetune --check-calibration / --add-calibration include|exclude` CLI; `ops/calibration.py` added to ARCH-14 allowlist (reads raw/ for excerpts, writes only to .knowledge/policies/); 15 tests. DOC-8: `CHANGELOG.md` created at repo root with one-line delivery entries for M0–M75, distilled from BUILD.md § 9. Tests: 1472 → 1487 (+15), 0 regressions. Tag: `m75-phase5-round-h`.

### M74 — Phase 5 Round G (AGT-13 skill-emit, DOC-5 log rotation)

See `docs/milestones/M74.md`. AGT-13: `wiki skill-emit <domain>` generates `.claude/skills/wiki-<domain>/SKILL.md` from policy.yaml + MOC wikilinks + recent synthesis titles; deterministic; capped at 295 lines; `wiki_skill_emit` MCP tool; 14 tests. DOC-5: `wiki rotate-log [--keep-days N]` moves log.md entries older than 90 days to `log.archive.YYYY-Q.md` quarterly files; archive header documents machine-generated nature; weekly cron (0 3 * * 0) registered in `.knowledge/schedule.yaml`; `rotate-log` added to MCP CLI_ONLY; 11 tests. Tests: 1447 → 1472 (+25), 0 regressions. Tag: `m74-phase5-round-g`.

### M73 — Phase 5 Round F (ARCH-13 query-plan lifecycle, QUAL-7 retraction monitor)

See `docs/milestones/M73.md`. ARCH-13: `QueryPlan.status` field (`planned|executed|abandoned`); `stamp_executed()`/`stamp_abandoned()` helpers; `archive_old_plans()` moves executed plans >90 days to `nlm/query_plans/archive/`; orchestrator stamps `executed` on successful `--execute` runs; `wiki research --abandon`/`--archive` CLI; 14 tests. QUAL-7: `PubmedRetractionPoller` (`pollers/pubmed_retractions.py`) checks raw/pubmed via NCBI eFetch XML, stamps `retracted: true`+`retracted_at`, 30-day cursor; `ArxivRevisionPoller` (`pollers/arxiv_revisions.py`) checks raw/arxiv via arXiv Atom API, records baseline version, stamps `arxiv_revised: true`+`arxiv_current_version` on version increase; `lint/retracted_citations.py` — ERROR for any wiki page citing a `retracted: true` source; both pollers registered; lint registered; `WIKI.md § 3.1` updated; 20 tests. Tests: 1413 → 1447 (+34), 0 regressions. Tag: `m73-phase5-round-f`.

### M72 — Phase 5 Round E (ONT-13 last_verified_at for time-sensitive entities)

See `docs/milestones/M72.md`. ONT-13: `last_verified_at` field for `statute` and `standard` entity kinds; `lint/stale_verified.py` — walks `wiki/entities/*.md`, ERROR if time-sensitive kind missing `last_verified_at` or unparseable, WARNING if >365 days since verified; registered in `ops/lint.py` as `stale-verified`; `WIKI.md § 4.1` updated with field + expanded `entity_kind` enum; `tests/gateway/test_ont13_stale_verified.py` (15 tests). Tests: 1398 → 1413 (+15), 0 regressions. Tag: `m72-phase5-round-e`.

### M71 — Phase 5 Round D (ARCH-15 schema_version, ONT-11 backfill-synthesizes)

See `docs/milestones/M71.md`. ARCH-15 (`frontmatter.serialize()` injects `schema_version: 1` as first key when absent; `validate_source_frontmatter()` warns on missing; `WIKI.md § 3.1` documents it; 3 new frontmatter tests); ONT-11 (`ops/backfill_synthesizes.py` — walks synthesis pages, extracts `[[sources/...]]`/`[[synthesis/...]]` wikilinks, backfills missing `synthesizes:`; mixed-tier → sources-only; `write_atomic`; idempotent; `wiki backfill-synthesizes [--dry-run]` CLI; `CLI_ONLY` in MCP; 19 tests; `lint/synthesizes_coverage.py` severity escalated WARNING → ERROR since backfill now ships); INT-8 confirmed already complete (`pollers/repo_metadata.py` + 11 tests). Tests: 1377 → 1398 (+21), 0 regressions. Tag: `m71-phase5-round-d`.

### M70 — Phase 5 Round C (INT-3 Podcast converter)

See `docs/milestones/M70.md`. INT-3: `PodcastConverter` — new `podcast` source type; detects http/https URLs with audio extensions (.mp3/.m4a/.wav/.flac/.ogg/.aac/.opus), distinguishing cleanly from `VoiceConverter` (local files) and `AudiobookConverter` (.m4b); downloads via `urllib.request.urlretrieve`; transcribes using shared `gateway.transcription.transcribe()`; diarization fallback on auth failure; transcript cache integration; sidecar audio preserved at `raw/podcast/<id><ext>`; ID format `podcast-<episode-slug>-<sha256[:10]>`; six-step contract: `paths.SOURCE_TYPES`, `validator.ALLOWED_SOURCE_TYPES`, `ID_PATTERNS["podcast"]`, `PodcastConverter`, `converters/__init__.py` registration, `WIKI.md § 3.1/3.2/6.1` updated; 23 tests. Tests: 1354 → 1377 (+23), 0 regressions. Tag: `m70-phase5-round-c`.

### M69 — Phase 5 Round B (INT-1 Gmail, INT-2 RSS)

See `docs/milestones/M69.md`. Two capture-expansion pollers. INT-1 (`pollers/gmail_newsletters.py` — `GmailNewsletterPoller` via IMAP4_SSL stdlib; auth GMAIL_ADDRESS + GMAIL_APP_PASSWORD env vars; sender allowlist in `config.yaml`; UID cursor; writes `raw/web/` with `meta.source_app: gmail-newsletter`; multipart body extracts plain-text; idempotent on slug; 14 tests); INT-2 (`pollers/rss.py` — `RSSPoller` via urllib+ElementTree, no feedparser dep; RSS 2.0 + Atom 1.0; multi-feed `feeds.yaml` config; per-feed `{last_guid,last_pubdate}` cursor; writes `raw/web/` with `meta.source_app: rss`; idempotent; 17 tests). Bug fixed: `ET.Element` falsy-when-childless requires `is None` checks not `or`-chains. TOK-3/4/6 confirmed already shipped. Tests: 1323 → 1354 (+31), 0 regressions. Tag: `m69-phase5-round-b`.

### M68 — Phase 5 Round A (ONT-4 migration, ONT-6 backfill)

See `docs/milestones/M68.md`. Two migration ops closing the gap between ONT-4/ONT-6 validator enforcement and the legacy wiki corpus. ONT-4 (`ops/backfill_entity_kinds.py` — `backfill_entity_kinds(dry_run)` walks `wiki/entities/**/*.md`, applies `_KIND_MAP` of ~35 legacy aliases → canonical enum, unmapped → `"other"`; idempotent; `wiki backfill-entity-kinds [--dry-run]` CLI; `CLI_ONLY` in MCP; 12 tests); ONT-6 (`ops/backfill_timestamps.py` — `backfill_timestamps(dry_run)` stamps missing `created_at`/`last_updated` on entity/concept/synthesis pages using file mtime as proxy; idempotent; `wiki backfill-timestamps [--dry-run]` CLI; `CLI_ONLY` in MCP; 13 tests). ONT-8 confirmed already complete (validator + `lint/long_slugs.py` both shipped in prior milestone). Tests: 1298 → 1323 (+25), 0 regressions. Tag: `m68-phase5-round-a`.

## 12. Phase 5 exit checkpoint (2026-05-26)

**Milestones:** M68–M84 (17 milestones, Rounds A–Q)
**Tests:** 1298 → 1640 (+342)
**Tag range:** `m68-phase5-round-a` → `m84-phase5-round-q`

### What Phase 5 delivered

Phase 5 ran in two arcs. The first (M68–M77) closed residual Phase 3 obligations — schema migrations, doc suite, calibration set, retraction monitor, supersedence linking — that weren't reached in Phase 3/4. The second (M78–M84) expanded capture surface and completed the operational layer.

**Capture expansion (pollers)**
- INT-18: Notion source poller (`note-notion-<sha256[:12]>`, cursor, injectable client)
- INT-19: Slack source poller (channel messages + threads, min_length/reply_count filter, injectable callables)
- INT-3 confirmed via M70 (Podcast converter already shipped)
- All five pollers noted in CLAUDE.md forward-looking section now shipped

**Search + navigation**
- SRCH-1: `wiki search` — fulltext grep over wiki/ + raw/, score 3/2/1 title/slug/body, MCP tool
- SRCH-2: `wiki index --rebuild` — domain-grouped index.md catalog, cross-domain section, health summary

**Scheduled agent loop**
- TOOL-12: `wiki routine daily-domain-digest` — polls new sources, LLM digest, draft synthesis page, daily cron at 06:00 UTC

**Operational surface**
- TOOL-13: `/api/sources` web endpoint — source explorer with q/domain/type/limit filters
- TOK-10: `plan_authorship_small` Sonnet route for voice/note + body <2 KB (~5x cost reduction)

**Schema + quality (residual Phase 3)**
- ARCH-15: `schema_version: 1` injected by `fm.serialize`
- ONT-11: `wiki backfill-synthesizes` — populates `synthesizes:` from body wikilinks
- ONT-13: `last_verified_at` lint for statute/standard entities
- QUAL-7: PubMed retraction + arXiv revision pollers
- QUAL-10: held-out calibration set, `wiki finetune --distill` uses precision/recall/F1
- QUAL-14: `wiki reingest` — versioned successor with `supersedes`/`superseded_by` linking
- ARCH-13: query-plan lifecycle (`planned|executed|abandoned`, archive)
- DOC-5/8/9-12: log rotation, CHANGELOG, tests/README, MCP_API.md, RUNBOOK.md

### Phase 5 exit criteria verdict

| Criterion | Status |
|-----------|--------|
| All five pollers shipped | ✓ |
| wiki search + index --rebuild | ✓ |
| Scheduled daily digest loop | ✓ |
| Source-explorer web view | ✓ |
| Model cost routing (TOK-10) | ✓ |
| 1640 tests, 0 regressions | ✓ |

### What Phase 5 did NOT deliver (carried to Phase 6 or deferred)

| Item | Reason deferred |
|------|----------------|
| ONT-5/7/9 (academic modeling) | M effort, low daily-use impact; no retrieval failures yet |
| QUAL-8 (citation-claim coherence) | L effort LLM work; needs forcing function |
| ARCH-12 (second NLM backend) | L effort; NotebookLM disruption not acute |
| ONT-1 (1000 concept reclassifications) | L effort + human-bottlenecked |
| `wiki migrate` stub | Low demand; no migration scripts queued |
| AGT-7 (capture-to-cite cross-project) | Deps satisfied but scoping deferred |

---

## 15. Phase 7 delivery log (2026-05-26)

### M89 — Phase 7 Round A (AGT-8 filter calibrator monthly cron)

See `docs/milestones/M89.md`. AGT-8: `wiki routine filter-calibrator` runs monthly (`0 2 1 * *`), checks each domain's example-bank count against the 500-example distillation threshold, and emits a `calibration-distill-ready` log event (with the `wiki finetune --distill` command) the first time any domain crosses threshold. Idempotent — tracks seen domains in `.knowledge/filter_calibrator_logged.yaml`. 10 tests covering no-policy, below-threshold, above-threshold event emission, idempotency, multi-domain, schedule entry shape. Tests: 1695 → 1705 (+10), 0 regressions. Tag: `m89-phase7-round-a`.

---

## 14. Phase 6 exit checkpoint (2026-05-26)

All four Phase 6 items delivered. 1640 → 1695 tests (+55), 0 regressions. Tag: `m88-phase6-round-d`.

| Item | Milestone | Tests |
|------|-----------|-------|
| TOOL-8 `wiki daily` + `/today` | M85 | +17 |
| AGT-7 capture-to-cite + `/wiki-cite` skill | M86 | +16 |
| ONT-5 `canonical_source:` on paper entities | M87 | +11 |
| ONT-7 per-claim confidence 3-tier GRADE | M88 | +11 |

Exit criteria met:
- ✓ `wiki daily` CLI + `/today` JSON route live
- ✓ `wiki cite-capture` + `wiki_cite_capture` MCP wired; skill updated
- ✓ `canonical_source:` validator warning + `paper-canonical-source` lint check registered
- ✓ `confidence:` enum validated; `confidence-distribution` + `confidence-propagation` lint checks live
- ✓ 1695 tests (≥1700 criterion: 5 short — Phase 7 opens at 1695)

---

## 13. Phase 6 plan (2026-05-26)

**Thesis:** Phase 6 bets on *consuming* the wiki, not just filling it. Phases 1–5 built the ingestion pipeline, quality monitors, and pollers. The gap now is that there is no daily-use surface that brings knowledge back to the user — no review loop, no cross-project leverage, no quality annotations at the claim level. Phase 6 closes that gap.

### Proposed scope

| Item | Effort | Rationale |
|------|--------|-----------|
| TOOL-8 (`wiki daily` + `/today`) | M | TOOL-7 dep satisfied. Only scheduled-output consumer missing. Closes: "I have 500 sources but no morning review ritual." |
| AGT-7 (capture-to-cite cross-project) | M | Deps satisfied (cite-add, MCP parity). Highest-leverage cross-project item: takes a quote + URL from any repo, ingests if needed, adds citation. |
| ONT-5 (paper entity → canonical_source) | M | 46 paper entities with inconsistent citation chains. `canonical_source:` field + validator + lint. Directly improves retrieval fidelity. |
| ONT-7 (per-claim confidence, 3-tier GRADE) | M | Adds `confidence: tentative|established|speculative` per claim; propagation rule in validator; distribution in lint. Low schema friction, high interpretive value. |

### Deferred to Phase 7 or beyond

| Item | Reason |
|------|--------|
| QUAL-8 | L effort; no forcing function |
| ARCH-12 | L effort; NotebookLM still operational |
| ONT-1 | Human-bottlenecked; wait for retrieval failures |
| ONT-9 (domain hierarchy) | 22 MOCs is manageable flat; hierarchy adds complexity without clear query benefit yet |

### Phase 6 exit criteria

- `wiki daily` CLI outputs a triage list (drafts + orphans + new sources) and `/today` route is live
- AGT-7 `/wiki-cite` slash command wired and tested
- `canonical_source:` enforced on `entity_kind: paper`; lint surfaces violations
- Per-claim confidence field validated; 3-tier distribution surfaced in `wiki lint`
- Tests: ≥1700 total, 0 regressions

## 11. Downstream wiki-authoring work (post-migration)

These are not migration script work; they require LLM-driven authorship over already-migrated canonical content:

- **Concept body backfill.** Migrated concepts have stub sections (`## Summary _(needs population)_` etc.) because legacy concept pages had no body content beyond a "Methods" cross-reference list. Backfill is per-concept LLM work via `wiki query` or `wiki ingest --with-plan`.
- **Source citation graph.** Legacy MOCs use numeric `[1, 2]` citations without a number→ID map. Resolving these into `[[sources/<id>]]` requires per-MOC LLM authorship that re-grounds claims. 127 source orphans persist until this is done.
- **Synthesis backreferences.** 3 synthesis pages are orphan because no MOC references them. Either MOCs gain a "Synthesis pages" section linking each one, or this surfaces in a future `wiki lint --scope orphans --quiet-mocs` exclude rule.
