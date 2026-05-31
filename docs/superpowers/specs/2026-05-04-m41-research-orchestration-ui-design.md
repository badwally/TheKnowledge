# M41 — Research Orchestration UI (Design)

**Status:** Brainstormed and locked. Ready for implementation planning.
**Date:** 2026-05-04
**Scope:** Research orchestration UI only. NLM artifact triggers and review consoles are deferred to M42.

---

## Goal

Add a Research sidebar entry to `wiki serve` that exposes the existing `wiki research` orchestrator (M37/M37.1) over HTTP. The page uses a sessions-list + detail two-pane layout. Each session walks through three phases: prompt+domain → query plan (structured per-adapter editor) → execute. Long-running execution shows per-step progress sourced from filtered `log.md` entries, terminal states show the resulting synthesis pages.

---

## § 1. Architecture & integration with M40

Adds a Research sidebar entry between Wiki and Domains groups. New page at `/research` with the two-pane sessions-list + detail layout. No new top-level architecture — reuses the FastAPI + React + TaskRunner foundation. New backend module `src/gateway/web/routes/research.py`. New frontend pages in `web/src/pages/research/` (split into multiple files since the wizard has phase-specific components). The orchestrator's behavior is unchanged; M41 only adds an HTTP surface.

Trust boundary unchanged: same localhost-only `wiki serve` process. Per the M40 task pattern, execute runs in a daemon thread; per-step progress is read from the durable `log.md` rather than carried in TaskStore state.

---

## § 2. Session lifecycle states

A session is in exactly one state at any time, derived from on-disk state (no new persistence layer):

| State | How it's detected | UI affordance |
|---|---|---|
| `plan_only` | YAML exists; no execute log entry | "Execute" button enabled |
| `edited` | YAML mtime > `generated_at` + 2s; no execute log entry | "Execute" button enabled; "edited: true" badge |
| `running` | TaskStore has an active task for this session_id | Disabled; per-step progress visible |
| `done` | Promoted to persistent (in `nlm_registry.get_session(domain, session_id).status == 'promoted'`) | Synthesis pages link list visible |
| `abandoned` | Status field on the session entry in `nlm_registry` | Reason shown; "Retry" button (creates a fresh session_id from the same prompt+plan) |

The list-pane query enumerates `nlm/query_plans/*.yaml`, joins each with `nlm_registry.get_session(...)` for promote/abandon state, and detects `running` from the in-memory TaskStore. No new on-disk state is introduced.

---

## § 3. Backend endpoints

```
GET  /api/research/sessions                      → [{session_id, prompt, domain, state, generated_at, query_count, ...}]
GET  /api/research/sessions/{session_id}         → {session_id, prompt, domain, plan: {...}, state, edited, last_log_summary?, ...}
POST /api/research/sessions                      body: {prompt, domain?, max_results?, include_local?, trust_local?}
                                                 → 202 + {task_id} (planner runs the per-adapter expansion)
PUT  /api/research/sessions/{session_id}/plan    body: {queries: {arxiv:[...], youtube:[...], web:[...], pubmed:[...]}}
                                                 → 200 + updated plan (writes YAML; mtime bump triggers `edited: true` on next load)
POST /api/research/sessions/{session_id}/execute body: {dry_run?: bool, draft?: bool}
                                                 → 202 + {task_id}
GET  /api/research/sessions/{session_id}/progress → {steps: [{name, status, started_at?, finished_at?, summary?}, ...]}
```

The progress endpoint parses `log.md` for entries matching `op="research"` and `fields.session_id == session_id`, mapping each log entry's `step` field to one of the 13 named pipeline stages (per-adapter search counts as one named entry per adapter).

**Reused infrastructure.** Plan creation and execute both use the M40 TaskStore (`run_in_thread`). The OperationResult from `apply_plan` flows through `_serialize_op_result` and renders in the existing `<ResultPanel>` on completion.

---

## § 4. Frontend layout

```
web/src/pages/research/
├── Research.tsx              # top-level page, two-pane layout
├── SessionsList.tsx          # left pane: list of sessions with status indicators
├── NewSessionForm.tsx        # inline form at top of list (prompt + domain + advanced flags)
├── SessionDetail.tsx         # right pane: phase-aware container
├── PlanEditor.tsx            # structured per-adapter editor (used in plan_only / edited states)
└── ProgressView.tsx          # per-step progress (used in running state); polls /progress every 3s
```

**Routing:** `/research` (list visible, no detail), `/research/:session_id` (list + detail). Selecting a session in the list pushes the URL.

**SessionsList:** sorted by `generated_at` descending (newest-first). Each row shows session_id, status badge (color-coded), domain, query count or sources count depending on state. "+ New" button at top opens `NewSessionForm` inline above the list (form expands; existing rows scroll below).

**NewSessionForm:** prompt textarea + domain input (with hint "leave blank to infer") + advanced collapsible (max_results, include_local glob list, trust_local checkbox, draft, dry_run). Submit → POST creates a planning task → on completion the new session appears in the list and is auto-selected.

**SessionDetail (phase-aware):**
- `plan_only` / `edited`: header (session_id + prompt + domain) + `<PlanEditor>` + `[Save plan]` `[Execute →]` row
- `running`: header + `<ProgressView>` (polls `/progress` every 3s)
- `done`: header + result block (sources_added count + list of synthesis page paths with click-to-open-in-Obsidian links via `obsidian://open?path=...`)
- `abandoned`: header + reason from registry + `[Retry]` button (creates a new session from the same prompt+plan)

**PlanEditor:** four sections (arxiv, youtube, web, pubmed). Each section is `[label] [count] [+ add]` and a list of editable rows. Rows have an inline text input + `×` delete. Edited rows get amber border. `[Save plan]` PUT-s the queries dict; success refreshes the session.

**ProgressView:** vertical list of named steps (search·arxiv, search·youtube, search·web, search·pubmed, dedup, filter, materialize, nlm_session, push_sources, source_map, analysis, apply_plan, promote). Each row: state icon (✓/⟳/○/✗) + name + summary (e.g., "24 candidates · 3s" for completed steps). Polls `/api/research/sessions/{id}/progress` every 3s while the task is running.

---

## § 5. Per-step progress data flow

The orchestrator already calls `log.append("research", fields={"session_id": ..., "step": ...}, summary=...)` at every meaningful step. M41 doesn't change orchestrator code; it adds a server-side parser.

**Server-side parser** (in `routes/research.py`):
1. Read `log.md` once per request (cheap; 4000 lines, ~150KB at current scale).
2. Filter entries to `op="research"` AND `fields.session_id == session_id`.
3. Group by `step` field. For each known step name, take the latest entry (success > error > start).
4. Map to a 13-element fixed list of expected steps. Steps without a log entry yet → `queued`. Steps with a `start` entry but no `complete` entry → `running`. Steps with a `complete`/`error` entry → `done`/`failed`.

**Step name mapping** (orchestrator → UI label):
- `search.arxiv` → "search · arxiv"
- `search.youtube` → "search · youtube"
- `search.web` → "search · web"
- `search.pubmed` → "search · pubmed"
- `dedup` → "merge & dedup"
- `filter` → "filter"
- `materialize` → "materialize"
- `nlm_session_create` → "notebooklm session"
- `push_sources` → "push sources"
- `source_map` → "source map"
- `analysis` → "analysis"
- `apply_plan` → "apply plan"
- `promote_session` → "promote"

If the orchestrator's actual log step names don't match this list, M41 includes a small targeted refactor of the orchestrator to emit canonical names. (Verified during plan-writing.)

---

## § 6. New-session form

Inline expandable form at the top of the sessions list. Fields:

- **prompt** (textarea, required): "On-device RAG for proprietary data..."
- **domain** (input, optional): leave blank to infer; if blank, the planner's domain inference runs first
- **Advanced** (collapsible):
  - max_results (number, default 50)
  - include_local (list of globs, optional)
  - trust_local (checkbox, default false)
  - draft (checkbox, default false)
  - dry_run (checkbox, default false)

Submit → POST `/api/research/sessions` returns a task_id. Polling shows planner progress as a single spinner ("generating per-adapter queries..."). On completion, the new session enters the list as `plan_only` and is auto-selected. The form collapses back to "+ New" button state.

Defaults match the CLI: planner enabled, no `--no-plan` toggle in the form (always use the planner — that's the entire point of the UI). `--queries` import (load external YAML) deferred indefinitely; rare enough to keep the CLI as the only path.

---

## § 7. Out of scope (deferred or rejected)

**M42:**
- NLM artifact triggers (briefing, audio, slides, revise) — per-domain page with confirmation modals
- Review consoles (drafts, contradictions, orphans, filter-band sources)

**M41 deliberate exclusions:**
- No `--no-plan` toggle in the form. The whole point of the UI is using the planner.
- No `--queries` external YAML import. Rare; CLI suffices.
- No live SSE/WebSocket for progress. Manual refresh + 3s polling on the active progress view is sufficient.
- No NLM artifact buttons on `done` sessions. Those live on the per-domain page in M42.
- No session deletion. Plans accumulate in `nlm/query_plans/`; manage via filesystem or a future `wiki research-clean` op.
- No multi-domain research session. The orchestrator assumes one domain per session; M41 inherits that.

---

## § 8. Risks & tradeoffs

1. **Step name canonicalization.** If the orchestrator emits step names that don't match the M41 fixed list, the progress view will have unmapped steps. Mitigation: a one-time small refactor of the orchestrator's `log.append` calls during M41 to use canonical names; tested by a snapshot test that runs a real research session against a stub plan client.

2. **Log parsing cost.** Reading the full log.md per progress poll is O(file-size) per request. At 5,000 lines / ~200KB the cost is sub-millisecond, fine for now. If `log.md` grows to 100k+ lines, switch to tail-only parsing keyed off file offset.

3. **Browser tab left open during execute.** The orchestrator runs in a daemon thread; the user can close the tab without losing the run. The activity feed on Dashboard catches the completion. Reopening `/research/:session_id` reconstructs progress from log.md.

4. **Edit detection race.** The plan editor's PUT bumps the YAML mtime; the orchestrator's `--execute` then sees `mtime > generated_at + 2s slack` and stamps `edited: true`. If a user clicks Execute within 2s of saving, the slack window may register the plan as not-edited. Acceptable: the CLI has the same property, the bookkeeping is informational, no behavior depends on it.

5. **Inline form vs modal.** Inline form expands within the list pane, which can push selected sessions off-screen. Mitigation: the form has a `[Cancel]` button that collapses it back. If this proves annoying in practice, swap to a modal in M41.1 — the form's component is self-contained.

---

## § 9. Acceptance criteria

M41 is shipped when:

1. The Research sidebar entry navigates to `/research`. Sidebar position: between Wiki and Domains groups.
2. The sessions list shows all existing `nlm/query_plans/*.yaml` files with their derived state (plan_only / edited / running / done / abandoned), sorted newest-first.
3. Clicking "+ New" opens an inline form. Submitting a prompt + domain creates a new session (planning task), and the new session appears in the list as `plan_only` on completion.
4. Selecting a session in `plan_only` or `edited` state shows the structured per-adapter editor with arxiv/youtube/web/pubmed sections; Save persists changes (mtime bumps, `edited: true` triggers on next refresh); Execute kicks off the run.
5. While executing, the progress view shows the 13-step pipeline with state indicators that update via 3s polling. Steps light up green/red/amber as the orchestrator advances.
6. On completion (`done`), the detail pane shows the synthesis page paths with `obsidian://` open links and a sources_added count.
7. On abandonment, the detail pane shows the failure reason and a Retry button that creates a new session_id from the same prompt+plan.
8. All endpoints have FastAPI TestClient tests covering: list, get, create, plan PUT, execute, progress.
9. BUILD.md has an M41 delivery record.
10. CLAUDE.md / README.md / TUTORIAL.md mention Research in operation tables where appropriate.
11. Hand-test: open `wiki serve`, create a new research session via the UI for a small dry-run, edit the plan, execute, watch progress, see the result. Compare against the same flow run via CLI.
