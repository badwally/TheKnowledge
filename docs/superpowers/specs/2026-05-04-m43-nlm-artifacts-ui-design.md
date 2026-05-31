# M43 — NLM Artifacts UI (Design)

**Status:** Brainstormed and locked. Ready for implementation planning.
**Date:** 2026-05-04
**Scope:** Wrap the existing `wiki nlm-{add,briefing,audio,slides,revise}` CLI ops in HTTP endpoints and surface them on a new Artifacts page under the Domains sidebar group. Confirmation gates on every LLM-calling op (per the artifact-generation-is-opt-in memory rule). Async generation via TaskStore polling. Bulk actions, filter/search within review tabs, and obsidian:// deep-links remain deferred to M44+.

---

## Goal

Add a single Artifacts page (`/domains/artifacts`) where the user picks a domain from a dropdown, optionally adds raw sources to its NotebookLM corpus, and triggers briefing / audio / slides generation. Each long-running op shows a confirmation modal before kickoff, then submits via TaskStore and polls for completion. Existing artifacts for the selected domain are listed at the bottom; slide decks have a Revise button that opens a per-slide modal.

---

## § 1. Architecture

Adds:
- `gateway.web.routes.nlm` — 5 endpoints: nlm-add (sync), briefing/audio/slides (async, return 202+task_id), revise (async), and a GET artifacts list per domain
- New "Artifacts" sidebar entry under the Domains group
- New React page `web/src/pages/domains/Artifacts.tsx` + supporting components
- Reuses existing `gateway.ops.nlm.{nlm_add,nlm_briefing,nlm_audio,nlm_slides,nlm_revise}` functions verbatim — no gateway-side changes
- Reuses M40 TaskStore for async ops

No changes to the underlying nlm ops. The discipline gate (only `wiki nlm-*` may invoke NotebookLM, never the bare `nlm` CLI in committed wiki content) remains intact — the web layer is just one more sanctioned caller.

---

## § 2. Backend endpoints

### Verified existing op signatures

```python
gateway.ops.nlm.nlm_add(domain: str, source_id: str, *, client=None) -> OperationResult
gateway.ops.nlm.nlm_sync(domain: str, *, dry_run=False, limit=None, client=None, progress=None) -> OperationResult
gateway.ops.nlm.nlm_briefing(domain: str, *, client=None) -> OperationResult
gateway.ops.nlm.nlm_audio(domain: str, topic: str, *, client=None) -> OperationResult
gateway.ops.nlm.nlm_slides(domain: str, topic: str, *, client=None) -> OperationResult
gateway.ops.nlm.nlm_revise(artifact_slug: str, instructions: list[str], *, client=None) -> OperationResult
```

`nlm_revise` is slide-only. Instructions are strings in `"slide N: <instructions>"` format parsed by `_parse_revisions`.

### Endpoints

```
POST /api/nlm/domains/{slug}/add               body: {source_id}                       → sync, returns OperationResult
POST /api/nlm/domains/{slug}/sync              body: {dry_run?, limit?}                 → 202 + task_id (bulk add)
POST /api/nlm/domains/{slug}/briefing          body: {}                                → 202 + task_id
POST /api/nlm/domains/{slug}/audio             body: {topic}                            → 202 + task_id
POST /api/nlm/domains/{slug}/slides            body: {topic}                            → 202 + task_id
POST /api/nlm/artifacts/{slug}/revise          body: {instructions: list[str]}          → 202 + task_id
GET  /api/nlm/domains/{slug}/artifacts         → [{slug, type, title, generated_at, domain}, ...]
```

`nlm-sync` is bulk and async (can take minutes for large domains). It's idempotent — sources already in the corpus are skipped — so retries are safe. The sync card on the page surfaces the same confirmation modal as artifact-generation since it's a bulk LLM-adjacent op.

The first four endpoints take a domain slug (path parameter) and follow the M40 sync/async pattern. Revise takes an artifact slug. The artifacts list endpoint enumerates `wiki/artifacts/{briefings,audio,slides}/*.md`, parses frontmatter, filters by `domain` field, and returns sorted-newest-first.

### Pydantic schemas

```python
class NlmAddRequest(BaseModel):
    source_id: str

class NlmSyncRequest(BaseModel):
    dry_run: bool = False
    limit: int | None = None

class NlmBriefingRequest(BaseModel):  # empty for now; reserved for future flags
    pass

class NlmAudioRequest(BaseModel):
    topic: str

class NlmSlidesRequest(BaseModel):
    topic: str

class NlmReviseRequest(BaseModel):
    instructions: list[str]  # each line: "slide N: <text>"

class ArtifactSummary(BaseModel):
    slug: str
    type: str  # "briefing" | "audio" | "slides"
    title: str
    generated_at: str
    domain: str
    nlm_artifact_url: str | None = None
```

---

## § 3. Frontend

```
web/src/pages/domains/
└── Artifacts.tsx              # the whole page; uses sub-components for forms + modals + list
```

(Single file is acceptable here — the page is ~250 lines; splitting into sub-components is YAGNI.)

### Routing

- `/domains/artifacts` → Artifacts page (no per-domain URL state in M43; dropdown holds the active domain in component state)

### Sidebar

Adds an "Artifacts" entry under the existing Domains group:

```
Domains:
  Bootstrap
  Discover
  Promote
  Artifacts   ← new
```

### Page layout

```
[domain dropdown — populated from /api/domains, filtered to those with has_notebook=true]

──── Add source to corpus ────
[source_id input] [Add button (sync)]
[Sync all sources for this domain] (async; opens confirmation modal — idempotent bulk add)

──── Generate artifact ────
┌─ Briefing ─────────────────┐
│ Generate a corpus-wide     │
│ briefing doc.              │
│ [Generate] (opens modal)   │
└────────────────────────────┘
┌─ Audio overview ───────────┐
│ Topic: [____________]      │
│ [Generate] (opens modal)   │
└────────────────────────────┘
┌─ Slide deck ───────────────┐
│ Topic: [____________]      │
│ [Generate] (opens modal)   │
└────────────────────────────┘

──── Existing artifacts ────
[table: slug · type · title · generated · Revise (slides only)]
```

### Confirmation modals

All four LLM-calling ops (briefing/audio/slides/revise) open a confirmation modal before submission:

```
┌────────────────────────────────────────────────┐
│ Generate <type> for <domain>?                  │
│                                                │
│ This calls NotebookLM and may take             │
│ 1-5 minutes. Confirm to proceed.               │
│                                                │
│           [Cancel] [Confirm & generate]        │
└────────────────────────────────────────────────┘
```

The generated request shows a running spinner while the TaskStore polls. On completion, the result panel shows the wiki page path and the artifact's `nlm_artifact_url` (if returned by the op).

### Revise modal

Per slide-artifact row, a Revise button opens:

```
┌────────────────────────────────────────────────┐
│ Revise <artifact-slug>                         │
│                                                │
│ Slide N: [_________________________________]   │
│                                                │
│ [+ Add another revision]                       │
│                                                │
│           [Cancel] [Confirm & revise]          │
└────────────────────────────────────────────────┘
```

Each row is one revision in `"slide N: <text>"` format. The Confirm button packs them into the `instructions` list.

### TaskRunner reuse

The same M40 `<TaskRunner>` component handles the async polling for briefing/audio/slides/revise. Each card has its own TaskRunner instance; they don't interfere because each task has a unique task_id.

---

## § 4. Async pattern

Reuses M40 exactly:

1. POST → 202 with `{task_id, status: "queued"}`
2. Backend `store.run_in_thread(task_id, lambda: nlm_op(...))` starts the work
3. Frontend `<TaskRunner>` polls `GET /api/tasks/{id}` every 3s
4. On terminal state (`done` or `failed`), TaskRunner renders the OperationResult via `<ResultPanel>`

Long-running ops are 1-5 minute NotebookLM calls. The user can navigate away during the run; the daemon thread completes regardless.

---

## § 5. Out of scope

- Bulk actions on review tabs — defer to M44 if friction emerges
- Filter/search within review tabs — same deferral
- Obsidian:// deep-links — same deferral; the artifacts page shows wiki paths, user opens in editor
- Custom artifact types beyond briefing/audio/slides — limited by NotebookLM's API
- Scheduled/recurring artifact generation — YAGNI
- Multi-slide revise UX with rich slide-content preview — instructions textareas suffice for M43
- Audio playback in browser — wiki/artifacts/audio/<slug>.md links to the artifact, user opens in browser/Obsidian
- Slide deck rendering — same; artifact pages link to NotebookLM URL

---

## § 6. Risks & tradeoffs

1. **NotebookLM API rate limits.** Generating 4 artifacts in quick succession could hit rate limits. The existing CLI ops surface NLM errors; the UI just renders them. No new mitigation needed.

2. **Long-running tasks lost on server restart.** TaskStore is in-memory (M40 design). A 5-minute artifact generation lost mid-flight is acceptable since the underlying NLM artifact may still exist in NotebookLM (and would be discovered by `wiki nlm-sync` in a future op). Document the limitation.

3. **Topic input ambiguity.** "audio overview topic" and "slide deck topic" are freeform strings passed to NotebookLM. The user can type anything; quality depends on what the underlying NLM call does with it. Outside M43's scope to validate.

4. **Revise is slide-only.** The CLI op only revises slide decks. Briefing and audio artifacts have no revise flow in M43. The artifacts list shows a Revise button only on slide rows.

5. **No artifact deletion.** M43 doesn't add a "delete artifact" button. To delete, the user removes the wiki page directly. Deferred until use cases emerge.

---

## § 7. Acceptance criteria

M43 is shipped when:

1. POST endpoints for nlm-add (sync) and briefing/audio/slides/revise (async) round-trip to existing gateway ops, with TestClient coverage of happy path and 4xx/5xx error paths.
2. GET `/api/nlm/domains/{slug}/artifacts` returns artifacts filtered by domain, sorted newest-first.
3. Artifacts sidebar entry navigates to `/domains/artifacts`. Domain dropdown lists domains with persistent notebooks (filtered from `/api/domains` by `has_notebook=true`).
4. Selecting a domain loads its artifact list. Add Source form round-trips to nlm-add.
5. Each of briefing/audio/slides Generate buttons opens a confirmation modal before submission. After confirm, TaskRunner polls and renders the result.
6. Slide-deck rows in the artifacts list show a Revise button. Clicking opens the slide-revision modal; confirming submits the instructions list to nlm-revise.
7. BUILD.md M43 entry; CLAUDE.md / TUTORIAL.md mention `/domains/artifacts`.
8. Hand-test: open `wiki serve`, navigate to /domains/artifacts, pick a domain with a corpus (e.g., `glp1-reward-modulation`), verify the artifact list renders existing artifacts, and confirm the modals appear before any Generate submission. (Skip live NLM generation in the hand-test to avoid burning quota; the round-trip tests cover that path with stubs.)
