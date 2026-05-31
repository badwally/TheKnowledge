# M40 — Web UI Foundation (Design)

**Status:** Brainstormed and locked. Ready for implementation planning.
**Date:** 2026-05-04
**Scope:** Medium (foundation + simple ops + domain ops + lint).

---

## Goal

Ship `wiki serve` — a local browser front-end that wraps the gateway's daily operations (ingest, query, finalize, filter-correct) plus all domain operations (bootstrap, discover, promote, demote, reject) and a lint dashboard. The UI complements Obsidian (which retains wiki browsing); it does not visualize wiki content. Research orchestration and review consoles are deferred to M41/M42.

---

## § 1. Architecture & deployment

**Backend.** New module `src/gateway/web/` containing a FastAPI app. Endpoints are thin adapters around existing `gateway.ops.*` functions — no new business logic. The gateway stays the only thing that mutates `wiki/` and `raw/`; the web layer just exposes its operations over HTTP.

**Frontend.** New top-level `web/` directory containing a Vite + React + TypeScript SPA. Built artifacts (`web/dist/`) are checked into the repo and served by FastAPI as static files at `/`. The build is a manual `npm run build` step, not invoked by `wiki serve` — production-style deployment, no Node runtime needed at runtime.

**Entry point.** New CLI command `wiki serve [--port 7474] [--bind 127.0.0.1]` that starts uvicorn against the FastAPI app. Default binds to localhost only; `--bind 0.0.0.0` opt-in if iPad/laptop access on the local network is needed.

**Trust boundary.** No auth — same as the gateway CLI itself. Anyone with shell access to the machine can run `wiki ingest`; anyone who reaches `localhost:7474` can do the same through the web UI. Documented in the README; no login screens in M40.

**Dependency cost.** FastAPI + uvicorn are the only new Python deps (pin versions in `pyproject.toml`). Frontend adds Vite/React/TypeScript as build-time-only deps under `web/package.json`, isolated from Python.

---

## § 2. Backend layout

```
src/gateway/web/
├── __init__.py
├── app.py              # FastAPI app construction, router registration, static-file mount
├── tasks.py            # Background task registry: in-memory dict[task_id → TaskRecord]
├── routes/
│   ├── __init__.py
│   ├── status.py       # GET /api/status, /api/log, /api/lint
│   ├── domains.py      # GET /api/domains, POST /api/domains/{slug}/promote, ...
│   ├── ops.py          # POST /api/ops/ingest, /api/ops/query, /api/ops/finalize, /api/ops/filter-correct
│   ├── bootstrap.py    # POST /api/ops/bootstrap-domain
│   └── tasks.py        # GET /api/tasks/{id}
└── schemas.py          # Pydantic models for requests/responses
```

**Task store.** `tasks.py` holds an in-memory `dict[task_id → TaskRecord]` keyed by UUID. Each record carries `status` (queued/running/done/failed), `op_name`, `started_at`, `finished_at`, `result_payload`, `error`. Long-running ops dispatch via `asyncio.create_task` wrapping `asyncio.to_thread(gateway_op, ...)` so the synchronous gateway call doesn't block the event loop. The store is process-local — restarting `wiki serve` drops in-flight tasks. Acceptable for a single-user tool: the gateway's writes are atomic, so a dropped task means "submit again." `log.md` provides durable history.

**CLI wiring.** `src/gateway/cli.py` gets a new subparser `wiki serve` and a `_run_serve(ns)` dispatcher that invokes `uvicorn.run("gateway.web.app:app", host=ns.bind, port=ns.port)`.

**Tests.** New `tests/gateway/test_web_app.py` exercises every endpoint via FastAPI's `TestClient`. Each endpoint test asserts: (a) request shape matches Pydantic schema, (b) the underlying `gateway.ops.*` function gets called with expected args (mocked), (c) response shape matches the documented return. Async-op endpoints additionally test queued → running → done state transitions via the task record.

---

## § 3. Frontend layout & screens

```
web/
├── package.json
├── vite.config.ts
├── tsconfig.json
├── index.html
└── src/
    ├── main.tsx
    ├── App.tsx                # layout shell (sidebar + content) + route table
    ├── api.ts                 # fetch wrappers, task polling helper
    ├── types.ts               # mirrors backend Pydantic schemas
    ├── components/
    │   ├── Sidebar.tsx
    │   ├── StatCard.tsx
    │   ├── ActivityFeed.tsx
    │   ├── OpForm.tsx         # generic form shell with submit + inline result panel
    │   ├── TaskRunner.tsx     # wraps an op page; submit → poll /api/tasks/{id} → render result
    │   └── ResultPanel.tsx    # green/red banner + monospace payload
    └── pages/
        ├── Dashboard.tsx
        ├── Ingest.tsx
        ├── Query.tsx
        ├── Finalize.tsx
        ├── FilterCorrect.tsx
        ├── Bootstrap.tsx
        ├── Discover.tsx
        ├── Promote.tsx        # promote / demote / reject as tabs
        └── Lint.tsx
```

**Routes (client-side):**
- `/` → Dashboard
- `/ops/ingest`, `/ops/query`, `/ops/finalize`, `/ops/filter-correct`
- `/domains/bootstrap`, `/domains/discover`, `/domains/promote`
- `/system/lint`

**Sidebar groups:**
- **Wiki:** Dashboard, Ingest, Query, Finalize, Filter correct
- **Domains:** Bootstrap, Discover, Promote/Demote/Reject
- **System:** Lint, Logs

**Dashboard (hierarchical layout).** Top row: 4 stat cards — Watcher (running/stopped + heartbeat age), Inbox (pending + failed counts), Drafts (count + age-warning if any > 7 days), Sources (total + domain count). Below: monospace activity feed showing last 20 log entries. Refresh button in top-right. Status colors: green border for healthy, amber for "needs attention," red for failure.

**Form pattern.** Each op page is a dedicated route. The form lives at the top; on submit, the form disables and a result panel appears below. Result panel has a colored left border (green = success, red = failure, amber = no-op or partial) and shows the operation's `summary`, `paths_touched`, `authorship_report` (if any), `warnings`, and `errors` in monospace.

**Shared `<TaskRunner>` component.** Accepts the form schema and result renderer as props. Handles submit → POST → receive `task_id` → poll `/api/tasks/{id}` every 3s → render `<ResultPanel>` with success/error styling. Eight near-identical op pages reduce to ~30 lines each.

**Styling.** Plain CSS modules per component, no Tailwind or component library. Color palette: slate sidebar (`#2a3142`), white content, green (`#0a8a3e`) / amber (`#d97706`) / red (`#dc2626`) status accents.

**No state management library.** React's `useState`/`useEffect` only. Task polling is local to each page. Dashboard data fetches on mount and on manual refresh.

---

## § 4. Async task model

**Endpoint pattern for long-running ops** (`ingest --with-plan`, `bootstrap-domain`, `query`, `discover-domains`):

```
POST /api/ops/<name>           → 202 Accepted, body: {task_id, status: "queued"}
GET  /api/tasks/<task_id>      → {task_id, status, started_at, finished_at?, result?, error?}
```

**Status states:** `queued` → `running` → `done` | `failed`. The frontend's `<TaskRunner>` polls every 3s while status ∈ {queued, running}; on terminal state it renders the result and stops polling.

**Result payload.** For successful ops, `result` is the gateway's `OperationResult` serialized as `{success, summary, paths_touched, warnings, authorship_report?, no_op}`. The frontend renders `paths_touched` as monospace lines and `authorship_report` (when present, from `wiki ingest --with-plan`) using the `format_summary()` and `format_detail()` outputs from M38.

**Short ops bypass the task model.** `wiki status`, `wiki lint --scope <fast>`, `wiki filter-correct`, and read-only endpoints (`/api/domains`, `/api/log`) execute synchronously and return inline. The boundary is "if it might exceed 5 seconds, it's a task."

**Task store lifetime.** Records persist for the lifetime of the `wiki serve` process. No disk persistence in M40 — restart loses in-flight task history. The activity feed is sourced from `log.md`, so completed-task history survives restarts independently.

**No cancellation in M40.** Submitted tasks run to completion or failure. The gateway ops aren't designed to be interrupted mid-flight (atomic-write semantics make cancellation cosmetic). Defer to M41.

---

## § 5. Endpoint inventory

**Read-only (synchronous):**

```
GET  /api/status                      → {watcher, inbox, drafts, sources, domains}
GET  /api/log?lines=50                → [{timestamp, op, fields, summary}, ...]
GET  /api/lint?scope=<scope>          → {report_path, issues: [...]}
GET  /api/domains                     → [{slug, topic, sources_count, has_notebook, last_activity}, ...]
GET  /api/proposals                   → [{slug, status, member_sources, rationale}, ...]
GET  /api/tasks/<id>                  → {task_id, status, started_at, finished_at?, result?, error?}
```

**Short ops (synchronous, return OperationResult inline):**

```
POST /api/ops/filter-correct          body: {source_id, decision, rationale}
POST /api/ops/finalize                body: {page_path, abandon}
POST /api/domains/<slug>/promote      body: {}
POST /api/domains/<slug>/demote       body: {}
POST /api/domains/<slug>/reject       body: {}
```

**Long-running ops (async, return task_id):**

```
POST /api/ops/ingest                  body: {input, domain?, with_plan, draft, plan_timeout?}
POST /api/ops/query                   body: {question, domain, draft}
POST /api/ops/bootstrap-domain        body: {description, slug, force}
POST /api/ops/discover-domains        body: {scope?, since?, untagged}
```

**Static:**

```
GET  /                                → web/dist/index.html
GET  /assets/*                        → web/dist/assets/* (Vite-bundled JS/CSS)
```

**Reserved for M41/M42 (not implemented in M40):** `POST /api/ops/research`, `POST /api/ops/nlm-*`, `GET /api/drafts`, `GET /api/contradictions`, `GET /api/orphans`, `GET /api/filter-band`.

---

## § 6. Defaults & open implementation choices

- **Port:** 7474 (matches no commonly used service; close to `:8080`'s memorability range without colliding).
- **Bind:** `127.0.0.1` default; `--bind 0.0.0.0` opt-in.
- **Markdown rendering:** plain text in M40. File paths in result panels are not clickable. M41 may add a markdown-to-HTML renderer for log summaries and source previews.
- **Frontend bundle freshness:** the developer rebuilds `web/dist/` and commits the artifacts when frontend code changes. Add a CI check (or pre-commit hook) that fails if `web/src/` is dirty relative to `web/dist/`.
- **Toast / global notification surface:** none in M40. Result panel on the active page is the only feedback channel.
- **Settings/preferences:** none in M40. No light/dark mode toggle, no display options.
- **Error responses from FastAPI:** structured JSON `{detail: "<message>"}` with appropriate HTTP status (400 for validation, 404 for missing, 500 for unexpected). Frontend renders these in the result panel.

---

## § 7. Out of scope (deferred to later milestones)

**M41 (Research orchestration UI):**
- `wiki research` flow with `--review` gate (multi-step: prompt → query plan → user edits → execute)
- `wiki nlm-*` artifact triggers (briefing, audio, slides, revise) with explicit-confirmation gates per the opt-in memory rule

**M42 (Review consoles):**
- Drafts list (with age, finalize/abandon buttons)
- Authorship contradictions list (recent runs, severity, click-through to source/page)
- Source orphans list (sources with no inbound citations)
- Filter-band sources (between review and include thresholds, click-through to filter-correct)

**Indefinite defer:**
- Wiki content browsing (Obsidian owns this)
- Citation graph visualization (Obsidian owns this)
- Multi-user, auth, TLS

---

## § 8. Risks & tradeoffs

1. **npm toolchain on a pure-Python project.** Vite/React adds Node-side dependency maintenance. Mitigation: pin versions hard, no auto-upgrade, treat the frontend bundle as a vendored artifact rebuilt only when intentionally changing UI.
2. **In-memory task store loses state on restart.** A submitted long-running op (e.g., 5min discover-domains) is lost if `wiki serve` is killed. Acceptable for M40 single-user; revisit if the tool starts running unattended.
3. **Static frontend bundle in git.** `web/dist/` is checked in to avoid requiring Node at runtime. Cost: bundle size grows commit history; large diffs on rebuilds. Mitigation: `.gitattributes` markers to suppress diff noise on bundle files; `npm run build` is reproducible so rebuilds are deterministic.
4. **Redundancy with MCP server.** `wiki mcp-serve` already exposes gateway ops as `wiki_*` tools for agents. The FastAPI layer duplicates this for humans. Two surfaces to maintain. Acceptable: different consumers, different ergonomics.
5. **No cancellation.** A 5-minute discover-domains run can't be aborted mid-flight from the UI. User must wait or kill the server. M41 candidate if research orchestration makes cancellation important.

---

## § 9. Acceptance criteria

A milestone counts as M40-shipped when:

1. `wiki serve` starts a server on `127.0.0.1:7474` by default.
2. The Dashboard route loads, shows watcher state from `wiki status`, recent log entries from `log.md`, and a working manual-refresh button.
3. The Ingest, Query, Finalize, and Filter-correct pages each submit successfully via the web UI, with results matching `wiki ingest`/`wiki query`/etc. CLI output (verified by side-by-side comparison).
4. The Bootstrap-domain, Discover-domains, and Promote/Demote/Reject pages each round-trip successfully, with the same atomic-write and validation guarantees as the CLI versions.
5. Long-running ops (ingest --with-plan, query, bootstrap, discover) return a task_id, the page polls `/api/tasks/<id>`, and the result panel updates without a manual refresh.
6. The Lint page runs `wiki lint --scope <selectable>` and renders the report.
7. All new endpoints have FastAPI `TestClient` tests; full gateway test suite still passes (currently 481 → expected 500-510 after additions).
8. `BUILD.md § 10` has an M40 delivery record.
9. README, CLAUDE.md, TUTORIAL.md document the new `wiki serve` command.
10. Hand-test: launch `wiki serve`, exercise each op page through the browser, confirm wiki/raw state matches CLI behavior.

---

**Brainstorm artifacts.** Mockups under `.superpowers/brainstorm/<session>/content/` (gitignored). Decisions captured: navigation pattern (sidebar), dashboard layout (hierarchical), form pattern (dedicated page + inline result), async pattern (submit-then-poll on active page).
