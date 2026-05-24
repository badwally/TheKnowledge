# K1–K5 keystone implementation plan

## Context

The 2026-05-23 comprehensive review identified five keystone unlocks (K1–K5) that gate the next ~60 findings on the roadmap. Each is a single-week scope on its own; together they shift the wiki from "single-machine, hand-driven, mostly-blind" to "remotely accessible, agent-drivable, observable, scheduled, with a real edit path." Without K1 the draft-debt backlog cannot be discharged. Without K2 the agent surface is permanently narrower than the human surface. Without K3 capture is laptop-only. Without K4 nothing runs unattended. Without K5 cost and latency decisions stay faith-based.

This plan locks the architectural decisions, sequences execution into two waves, names the critical files, and defines hand-test verification per keystone.

## Decisions locked (from gating consultation)

| # | Decision | Choice |
|---|---|---|
| D1 | Sequencing | Two waves: K5+K2 foundation → K1+K4+K3 parallel functionality |
| D2 | Cite line-number fix direction | Change validator to report file-line numbers (single fix point in `validator.py`) |
| D3 | `wiki_research` MCP shape | Mirror all CLI flags as one `wiki_research` tool |
| D4 | `/api/ingest` mode | Synchronous via TaskStore (mirror `/api/ops/ingest` pattern) |
| D5 | `wiki cite-add` resolver | Internal escalation: exact → normalized substring → optional fuzzy LLM (off by default, `--fuzzy` flag) |
| D6 | iOS Shortcut deliverable | **In scope this cycle as a discrete K3 sub-deliverable** (see K3 § iOS Shortcut). Split: detailed build doc + curl verification script delivered by Claude Code in this session; .shortcut binary exported by Andrew from his phone after following the doc, then committed to `scripts/`. |
| D7 | Token telemetry rollout | New `call_with_usage()` method; migrate all known LLM call sites this milestone |

## Decisions committed in this plan (object on review if needed)

| # | Decision | Choice | Rationale |
|---|---|---|---|
| C1 | `wiki edit` scope | Constrained section-replace only (`--section <name>` + new body) | No current caller needs broader; expand on demand |
| C2 | Bearer-token storage | Hashed in `.knowledge/auth.yaml`; plaintext printed once on `wiki auth add`; file `.gitignore`'d | Standard hygiene; matches global CLAUDE.md secrets rule |
| C3 | Default scheduler jobs | Empty `.knowledge/schedule.yaml`; TUTORIAL.md documents a recommended starter set the user opts in to | Avoids surprise scheduled runs; user explicitly enables each |
| C4 | Expose destructive MCP ops | Expose `wiki_reject_proposal` (deletes drafts only); **omit** `wiki_demote_domain` (cross-page write impact); document the omission | Match Message Send Gate spirit for destructive cross-state actions |
| C5 | Cost-USD in `wiki status` | Tokens always; USD estimate behind a `--cost` flag on `wiki status` | Tokens are factual; USD is an estimate that diverges from Max-plan billing reality |
| C6 | `wiki_cite` MCP signature for additions | `list[{line: int, source_id: str}]` | JSON-friendly; types are typed |
| C7 | Branch strategy | One feature branch per wave: `wave-1/k5-k2`, then `wave-2/k1-k4-k3` rebased on merged wave-1 | Two PRs total; reviewable; matches two-wave sequencing |
| C8 | Test discipline | TDD for new ops (`cite_add`, `edit_section`, scheduler dispatch, telemetry parsing); test-after for mechanical MCP wrappers | Cost-of-tests matches risk |
| C9 | Hand-tests per Kn | Each Kn ships with hand-test notes in `docs/milestones/M47.md` (wave 1) and `docs/milestones/M48.md` (wave 2); per memory entry `collaboration_style.md` | Established convention |
| C10 | Locking discipline | All new write paths use `file_lock(...)` from `gateway/locking.py`; new lock names registered in a `LOCK_NAMES` constant (also closes `ARCH-1`/`ARCH-8` opportunistically while we're in the area) | Avoid silently inheriting the racy log/index bug |

## Sequencing

```
wave 1 (K5 + K2)         wave 2 (K1 + K4 + K3, parallel)
─────────────────        ──────────────────────────────
 K5 telemetry            K1 edit-path
 K2 MCP parity   ────►   K4 scheduler
                         K3 cloud shim
```

Wave 1 must merge before wave 2 starts because:
- K5 establishes the `call_with_usage()` contract that wave-2 ops will use when they make LLM calls
- K2 establishes the MCP-parity CI test that will force-fail K1 if K1 omits MCP wrappers for its new ops
- K2 cleans up `mcp_server.py` so K1 can append two new tool registrations to a stable file without merge conflict

Wave 2's three keystones touch disjoint files (K1 → ops + validator + cli + mcp_server; K4 → new scheduler module + cli + scripts; K3 → web/) and run truly in parallel.

## Wave 1 — K5 + K2

### K5 — Token telemetry

**Files to create:**
- `src/gateway/llm/telemetry.py` — `CallResult` dataclass (`text`, `input_tokens`, `output_tokens`, `cache_read_tokens`, `cache_creation_tokens`, `model`, `stop_reason`, `duration_ms`)
- `src/gateway/costs.py` — pricing table per model + `estimate_cost(model, usage)` helper

**Files to modify:**
- `src/gateway/llm/client.py` — add `call_with_usage(...) -> CallResult` that invokes `claude -p --output-format=json` and parses usage. Existing `call(...) -> str` unchanged.
- `src/gateway/log.py` — add `log_llm_call(op, result: CallResult, session_id=None)` that appends a single-line entry under `file_lock("log")` (closes the racy-log bug from `ARCH-1` as a side-effect)
- `src/gateway/locking.py` — register `"log"` and `"index"` lock names in `LOCK_NAMES` constant
- `src/gateway/filter/semantic.py` — `ClaudeCLIFilterClient` gains `call_with_usage()`; `_run_filter` in research orchestrator switches to it
- `src/gateway/plan.py` — `ClaudeCLIPlanClient` gains `call_with_usage()`; `ops/ingest.py` plan-authorship path switches to it
- `src/gateway/vlm.py` — `ClaudeCLIVLMClient` gains `describe_with_usage()`
- `src/gateway/research/orchestrator.py`, `src/gateway/research/analysis.py` — switch to `call_with_usage` for the LLM call sites already identified by exploration
- `src/gateway/ops/status.py` — render a "LLM usage (last 7 days)" block; aggregate via new helper `_aggregate_llm_usage(log_text, days)`; reads tokens by parsing the new log line format

**Log line format (one per LLM call):**
```
## [<ISO-Z>] llm-call | op=<op> | model=<model> | in_tokens=<n> | out_tokens=<n> | cache_read=<n> | cache_creation=<n> | duration_ms=<n>
```

**Edge cases to handle:**
- `claude -p --output-format=json` not supported on the installed CLI version → degrade gracefully (warn once, fall back to `call()` text-only). Detect via stderr parse on first probe call at startup.
- Cache fields missing in JSON → default to 0 (do not log `null`)
- Subprocess timeout / non-zero exit → log the call attempt with `error=<reason>` and `duration_ms=<elapsed>` so failed calls are still observable

**Hand-test (K5):**
1. Run `wiki ingest <pdf-url> --with-plan` and inspect log.md for new `llm-call` entries with non-zero token counts
2. Run `wiki status` and confirm the 7-day LLM usage block renders
3. Run `wiki status --cost` (C5) and confirm USD estimate
4. Run a filter-heavy `wiki research "<small prompt>"` and confirm all 8 parallel filter workers emit telemetry

### K2 — MCP-CLI parity

**Files to modify:**
- `src/gateway/mcp_server.py` — add 12 new `@mcp.tool()` functions following the existing `_serialize()` pattern. New tools:
  - `wiki_research(prompt, domain, include_local, trust_local, max_results, draft, dry_run, review, execute_session, external_plan_path, no_plan)` — mirror all CLI flags (per D3)
  - `wiki_lint(scope)` — read-only
  - `wiki_batch_ingest(vault, legacy_import, domain, dry_run)`
  - `wiki_bootstrap_domain(description, slug, force)`
  - `wiki_discover_domains(scope, since, untagged, timeout)`
  - `wiki_promote_domain(proposal_slug)`
  - `wiki_reject_proposal(proposal_slug)` (per C4; `wiki_demote_domain` omitted with explicit comment in source)
  - `wiki_cite(page_path, additions: list[{line: int, source_id: str}])` (per C6)
  - `wiki_backfill_examples(domain, legacy_config, json_paths, policy_version)`
  - `wiki_finetune(domain, check, distill, threshold, force)`
  - `wiki_poll(name)` plus `wiki_poll_list()` for registry inspection
- `tests/gateway/test_mcp_parity.py` — new file implementing the parity assertion: every entry in `cli.IMPLEMENTED` (excluding documented `CLI_ONLY` allowlist) has a matching `wiki_*` MCP tool. This is the forcing function for K1.

**Pattern to follow** (from `mcp_server.py` lines 66–274 — every existing `@mcp.tool` follows it):
```python
@mcp.tool()
def wiki_<op>(<args>) -> dict[str, Any]:
    """One-line summary; flag semantics if non-trivial."""
    from gateway.ops.<module> import <op_func>
    return _serialize(<op_func>(<resolved_args>))
```

**Hand-test (K2):**
1. `pytest tests/gateway/test_mcp_parity.py` — must pass
2. From a Claude Code session in `~/code/chief-of-staff/`, invoke `wiki_research` MCP tool with a small prompt + `dry_run=True` and confirm it returns a plan structure
3. Invoke `wiki_lint` MCP tool with `scope="orphans"` and confirm it returns expected structured output
4. Confirm `wiki_demote_domain` is NOT in the MCP tool listing (per C4); confirm `wiki demote-domain` CLI still works

### Wave 1 merge gate

- All 793+ existing tests pass
- New parity test passes
- `wiki status` shows token usage block
- One end-to-end research run produces telemetry for every LLM stage
- Branch `wave-1/k5-k2` merged to main; tag `m47-keystones-wave-1`
- `docs/milestones/M47.md` written with hand-test results

---

## Wave 2 — K1 + K4 + K3 (parallel)

These three are file-disjoint and merge-independent. They can be implemented in three parallel branches rebased on wave-1's merge.

### K1 — Gateway edit-path

**Files to create:**
- `src/gateway/ops/cite_add.py` — new op. Internal escalation per D5:
  1. Exact substring match in page body
  2. If 0 hits: normalized match (unicode-normalize NFKC + casefold + collapse internal whitespace + strip trailing punctuation)
  3. If 0 hits AND `fuzzy=True`: invoke LLM via `call_with_usage` (logged through K5 telemetry) with prompt "given this claim, find the best matching line in this body"; LLM returns line number or null
  4. At any step: 1 hit → cite via underlying `cite()` op; 2+ hits → return ambiguity error with line numbers; 0 hits at final step → error with 3 nearest-by-edit-distance suggestions
  - Internally delegates to existing `cite()` after resolving line number, so frontmatter mutation + backlink updates + log append are inherited
- `src/gateway/ops/edit_section.py` — new op. Constrained section-replace (per C1). Parses markdown headers, identifies section by `## <name>` (case-insensitive), replaces body between this header and next `##` of equal-or-higher level, runs full validator on the result, logs through gateway, acquires `file_lock("wiki-author")`

**Files to modify:**
- `src/gateway/validator.py` — fix the line-number reporting bug per D2. The fix:
  - Helper: `_file_line_offset(text: str) -> int` returns frontmatter line count (lines from `---` to closing `---` inclusive plus 1 blank-line separator if present)
  - In `validate_citation_grounding()` (lines 291–327) and any other validator that reports body-relative line numbers via `c.line_no`, add the offset before formatting the error message
  - All validator error messages now use file-relative line numbers consistent with `wiki cite`'s expectation
- `src/gateway/ops/cite.py` — no API change; the underlying line-number semantics are now consistent with what validator emits, so no docstring update needed beyond confirming "line numbers are file-relative (including frontmatter)"
- `src/gateway/cli.py` — add `cite-add` and `edit` subcommand parsers + `_run_cite_add()` and `_run_edit_section()` dispatchers. `cite-add` takes `<page> <claim-text> <source-id> [--fuzzy]`. `edit` takes `<page> --section <name> --body-file <path>` (read new body from a file to avoid shell-escaping a markdown blob)
- `src/gateway/mcp_server.py` — add `wiki_cite_add(page_path, claim_text, source_id, fuzzy=False)` and `wiki_edit(page_path, section, new_body)` tool registrations. These land last because the K2 parity test would otherwise fail when CI catches the missing wrappers.

**Files to add tests in:**
- `tests/gateway/test_cite_add.py` — exact/normalized/fuzzy resolution; ambiguity error; idempotency (re-citing same claim is no-op)
- `tests/gateway/test_edit_section.py` — happy path; non-existent section rejected; replacement that breaks schema rejected; lock contention
- `tests/gateway/test_validator_line_numbers.py` — fixture: page with N-line frontmatter, claim on body line 5 → validator reports file-line N+5+1

**Hand-test (K1):**
1. Pick a draft synthesis page; run `wiki lint --scope drafts` and copy a "line N: claim not cited" error message
2. Run `wiki cite-add <page> "<exact claim text from page>" <source-id>` → confirm it cites the right line; confirm re-run is a no-op
3. Run `wiki cite-add <page> "<paraphrased claim>" <source-id>` (no `--fuzzy`) → confirm it returns "claim not found" with nearest matches
4. Re-run with `--fuzzy` → confirm it resolves via LLM, cites the right line, and the call appears in K5 telemetry
5. Run `wiki edit <page> --section "Summary" --body-file /tmp/new-summary.md` → confirm replacement; confirm validator re-runs and rejects if the new body removes required citations

### K4 — Scheduler substrate

**Files to create:**
- `src/gateway/scheduler.py` — new module. Public surface:
  - `ScheduleJob` dataclass: `name`, `cron`, `command`, `enabled`, `last_run`, `last_exit_code`, `last_duration_seconds`, `max_retries`
  - `load_schedule() / save_schedule(jobs)` — YAML at `.knowledge/schedule.yaml`
  - `is_job_due(job, now)` — uses `croniter`
  - `run_job(job)` — subprocess.run with `shell=True`, `cwd=KB_ROOT`, env propagated from launchd plist (PATH + KNOWLEDGE_ROOT). Subprocess execution per shell-out model (not in-process op dispatch) so arbitrary commands work, not just `wiki *` ones.
  - `run_all_due(dry_run=False)` — tick entry point; per-job `file_lock(f"schedule-{name}")`; updates `last_run` + `last_exit_code` on completion; skips if last failed run was < cooldown_seconds ago
- `scripts/install_scheduler.sh` — mirrors `scripts/install_watcher.sh`. Generates `~/Library/LaunchAgents/com.knowledge.scheduler.plist` with `StartInterval=60` (60s tick → minute-resolution cron), `RunAtLoad=true`, `KeepAlive=true`, logs to `.knowledge/scheduler.{out,err}.log`

**Files to modify:**
- `pyproject.toml` — add `croniter>=2.0` (already justified by exploration)
- `src/gateway/cli.py` — add `schedule` subcommand with sub-actions: `list / add / remove / enable / disable / run / dry-run`. `wiki schedule run` is what launchd invokes.
- `src/gateway/locking.py` — register `"schedule-<name>"` pattern in `LOCK_NAMES` (paired with the K5 lock-registry work)
- `.gitignore` — already covers `.knowledge/` per project conventions; confirm `schedule.yaml` is not separately ignored (it should not be — the schedule itself is durable config worth committing)

**Cron format:** UTC. Document explicitly in TUTORIAL.md. No local-timezone support in v1 (users wanting local-time scheduling write a shell wrapper that converts).

**Crash-loop guard:** Per-job `cooldown_seconds: int = 600` (default 10 min). If `last_exit_code != 0` and `now - last_run < cooldown`, skip this tick.

**Hand-test (K4):**
1. `wiki schedule add test-job "*/2 * * * *" "echo hello >> /tmp/wiki-test.log"` → confirm `.knowledge/schedule.yaml` updated
2. `./scripts/install_scheduler.sh` → confirm launchd plist created and loaded; `launchctl list | grep com.knowledge.scheduler`
3. Wait 3 minutes; confirm `/tmp/wiki-test.log` has ≥1 line; confirm `wiki schedule list` shows `last_run` updated
4. `wiki schedule disable test-job`; wait another 3 minutes; confirm no new log lines
5. Add a deliberately-failing job (`wiki nonexistent-command`); confirm cooldown kicks in (next tick skips after first failure)
6. `wiki schedule remove test-job`; confirm cleanup

### K3 — Cloud shim (Tailscale + bound serve + `/api/ingest`)

**Files to create:**
- `src/gateway/web/auth.py` — bearer-token verification. `verify_bearer_token(authorization: str | None) -> str` raises `HTTPException(401)` if header missing or token doesn't hash-match an entry in `.knowledge/auth.yaml`. Returns the token's `name` field on success (for audit logging).
- `src/gateway/web/routes/cloud.py` — new router with `POST /api/ingest` (per D4):
  - Accepts multipart upload OR JSON `{url, domain, draft, with_plan}`
  - Requires bearer token via FastAPI dependency
  - Wraps `ingest()` call in TaskStore daemon thread (mirror of `routes/ops.py` line 72–90 pattern)
  - Returns 202 with `task_id`
- `scripts/wiki-auth-add.sh` — convenience wrapper for `wiki auth add` (creates an entry in `.knowledge/auth.yaml`, prints the plaintext token once)

**Files to modify:**
- `src/gateway/web/app.py` — mount the new `cloud_routes.router`; auth dependency is per-route (not global middleware) so existing routes are unaffected
- `src/gateway/web/schemas.py` — add `CloudIngestRequest` pydantic model
- `src/gateway/cli.py` — add `wiki auth add <name>` + `wiki auth list` + `wiki auth revoke <name>` subcommands. Token generation: 32 bytes from `secrets.token_urlsafe`. Storage: sha256 hash in YAML; plaintext echoed once.
- `.gitignore` — add `.knowledge/auth.yaml` explicitly (defense-in-depth even though `.knowledge/` is already covered)
- `TUTORIAL.md` — new section "Remote capture (Tailscale)" with the curl-based test recipe (defer iOS Shortcut per D6)

**`.knowledge/auth.yaml` schema:**
```yaml
tokens:
  - name: ios-shortcut-andrew-iphone
    token_hash: sha256:abc123...
    created_at: 2026-05-24T15:00:00Z
    last_used_at: null
```

**`/api/ingest` body shapes:**
- Multipart form: `file` field (binary), optional `domain`, `draft`, `with_plan` form fields
- JSON: `{url: "https://...", domain?: "...", draft?: bool, with_plan?: bool}`
- Both return `{task_id: "<uuid>", status: "queued"}`; poll via existing `GET /api/tasks/{task_id}`

#### iOS Shortcut sub-deliverable (per D6 amendment)

**Why this is split delivery.** A `.shortcut` file is a binary plist exported by Apple's Shortcuts app. The app is GUI-only on macOS; the `shortcuts` CLI runs Shortcuts but does not author them. There is no reliable path to hand-construct a trusted `.shortcut` binary from a Claude Code session. The realistic delivery model: I write a precise build doc + a curl-based verification script; Andrew follows the doc on his iPhone, exports the resulting Shortcut to a `.shortcut` file via iOS Share → Save to Files / iCloud Drive, transfers it to the repo, and commits it. The Shortcut then becomes installable by anyone who clones the repo (one-tap import on iOS).

**Files to create (in K3 by Claude Code):**
- `TUTORIAL.md` § "Remote capture from iOS" — step-by-step build doc:
  1. Prerequisites: Tailscale on iPhone signed into same tailnet; bearer token from `wiki auth add` saved to iCloud Keychain or Notes
  2. Open Shortcuts app → New Shortcut → name "Wiki Capture"
  3. Configure trigger: "Share Sheet" + accepted input types (URL, Text, Files)
  4. Action 1: "Get Contents of URL" — URL: `https://<tailnet-hostname>/api/ingest`, method POST, headers `Authorization: Bearer <token>`, `Content-Type: application/json`, body: JSON dict with `url` = Shortcut Input
  5. Action 2: "Get Dictionary Value" — key `task_id` from response
  6. Action 3: "Show Notification" with task_id (so user sees confirmation)
  7. Test with a Safari Share → Wiki Capture
  8. Export: Shortcut details → Share → Save to Files → repo `scripts/` directory
  9. Commit `scripts/wiki-capture.shortcut` to repo
- `scripts/test-ingest-curl.sh` — curl invocation matching the Shortcut's HTTP call exactly. Verifies the endpoint accepts the request shape the Shortcut sends. Sourced from `.knowledge/auth.yaml` (read first token) and the local `wiki serve` URL; configurable via env vars `WIKI_URL` and `WIKI_TOKEN` to target a Tailscale hostname.

**Files committed by Andrew (after following the doc):**
- `scripts/wiki-capture.shortcut` — the exported Shortcut binary. Anyone cloning the repo can import it on iOS by tapping the file.

**Verification of the Shortcut path (within this K3 cycle):**
- `scripts/test-ingest-curl.sh` runs green from the laptop locally (proves endpoint contract).
- Andrew runs through the TUTORIAL.md steps 1–8 on his phone; the Shortcut posts to `/api/ingest` successfully; task_id notification appears.
- The exported `.shortcut` file is committed.
- Hand-test step 7 in the K3 hand-test below is the moment of truth.

**Risks / constraints captured:**
- Tailscale must be configured on iPhone before the Shortcut works. Step 1 of the doc is the gate.
- The Shortcut hardcodes the tailnet hostname + bearer token at build time. Token rotation (`wiki auth revoke`) requires editing the Shortcut. Document this.
- Multipart file uploads from Shortcuts are possible but more configuration-heavy. v1 of the Shortcut supports URL + text only (covers the common iOS share-sheet cases: Safari URLs, Notes selections); file uploads via the Shortcut are a follow-up.

**Hand-test (K3):**
1. `wiki auth add test-token` → save the plaintext output
2. `wiki serve --bind 0.0.0.0 --port 7474` (foreground)
3. From the same machine: `curl -X POST http://localhost:7474/api/ingest -H "Authorization: Bearer <plaintext>" -d '{"url": "https://example.com/test", "draft": true}'` → confirm 202 + task_id
4. `curl http://localhost:7474/api/tasks/<task_id>` → confirm status moves queued → running → done
5. Confirm `raw/web/web-2026-05-24-*.md` was created and validator-clean
6. Test auth failure: same curl without `Authorization` header → 401
7. **iOS Shortcut end-to-end (per D6 amendment).** Configure Tailscale on iPhone if not already done. Follow TUTORIAL.md § "Remote capture from iOS" to build the "Wiki Capture" Shortcut. From Safari on the phone, Share a test URL → Wiki Capture → confirm the success notification with task_id. Confirm `raw/web/web-2026-05-24-*.md` appears on the laptop. Export the Shortcut to `scripts/wiki-capture.shortcut` and commit. As a separate verification, re-import the exported `.shortcut` file on a freshly-reset Shortcut instance (or just delete + re-import) to confirm portability.
8. `wiki auth revoke test-token` → confirm subsequent curl AND Shortcut calls 401 (Shortcut surfaces a non-200 error in the notification).

### Wave 2 merge gate

- All tests pass including the new K1/K4/K3 tests
- K2 parity test still passes (K1's new ops have MCP wrappers)
- One end-to-end iOS-equivalent test: curl-from-laptop POST to `/api/ingest` results in a fully-ingested wiki source
- All three branches merged to main; tag `m48-keystones-wave-2`
- `docs/milestones/M48.md` written with per-K hand-test results

---

## Cross-cutting

- **Locking:** every new write op acquires the appropriate `file_lock(...)` from `gateway/locking.py`. The K5 log fix and K4 per-job lock both register their names in the new `LOCK_NAMES` constant per C10.
- **OperationResult shape:** every new op (`cite_add`, `edit_section`, `auth_add/list/revoke`, `schedule_*`) returns `OperationResult` per the existing convention in `core.py`. MCP wrappers serialize via existing `_serialize()` helper.
- **Log discipline:** every gateway op appends one structured log line. K5 telemetry adds the `llm-call` op label. K4 schedule runs add a `schedule` op label with `name=<job>` and `exit_code=<n>` fields.
- **Test discipline:** TDD per C8 for new ops; existing test conventions per `tests/gateway/` apply (Protocol-injected stubs for LLM clients; real filesystem under pytest tmp_path).
- **Hand-tests per C9:** captured in `docs/milestones/M47.md` (wave 1) and `docs/milestones/M48.md` (wave 2). One markdown section per Kn with the test recipe and observed output.

## Existing utilities to reuse (do NOT reinvent)

| Need | Reuse | Location |
|---|---|---|
| Atomic write | `core.write_atomic` | `src/gateway/core.py` |
| File locking | `locking.file_lock` | `src/gateway/locking.py` |
| OperationResult | `core.OperationResult` | `src/gateway/core.py` |
| MCP serialization | `mcp_server._serialize` | `src/gateway/mcp_server.py` |
| TaskStore (async wrapper) | `web/tasks.TaskStore.run_in_thread` | `src/gateway/web/tasks.py` |
| Log append | `log.append` (extend with K5 telemetry helper) | `src/gateway/log.py` |
| Frontmatter parse | `frontmatter.parse` | `src/gateway/frontmatter.py` |
| Citation token format | `citations.format_citation` | `src/gateway/citations.py` |
| LLM client | `ClaudeCLIClient` (extend with `call_with_usage`) | `src/gateway/llm/client.py` |
| Cron parsing | `croniter` (new dep) | external |
| Launchd plist pattern | existing watcher install script | `scripts/install_watcher.sh` |

## Verification (end-to-end, post-merge)

After both waves merge:

1. **K5 telemetry on a real research run.** `wiki research "<small prompt>" --domain glp1-reward-modulation --dry-run`. Inspect `log.md`: every LLM call appears as an `llm-call` line with non-zero tokens and a duration. `wiki status` → "LLM usage (last 7 days)" block shows aggregated numbers grouped by op. `wiki status --cost` adds USD column.
2. **K2 parity test.** `pytest tests/gateway/test_mcp_parity.py` passes. From another `~/code/*` project's Claude Code session, invoke `wiki_research`, `wiki_lint`, `wiki_cite_add`, `wiki_edit` MCP tools and confirm they execute and return structured results.
3. **K1 edit-path.** Pick one stale draft from `wiki lint --scope drafts`; close it with `wiki cite-add` and/or `wiki edit`; `wiki finalize <page>` succeeds. Validator error messages now use file-relative line numbers (verify by inspection of one rejection).
4. **K4 scheduler.** A test job (per K4 hand-test above) runs on schedule. Add a real recommended job from the TUTORIAL starter set (e.g., nightly `wiki lint`) and confirm it runs overnight.
5. **K3 cloud shim.** Configure Tailscale on iPhone. Visit `https://<tailnet>/api/health` from phone Safari → 200. Use any HTTP-capable iOS tool (Shortcuts app, Working Copy, etc.) to POST to `/api/ingest` with a tested bearer token; confirm the source lands in `raw/` and produces a wiki page (or draft).

## Out of scope (followups, not blockers)

- **iOS Shortcut multipart file uploads** — v1 Shortcut supports URL + text input (covers Safari share, Notes selection). Sharing a PDF or image directly from iOS into Wiki Capture is a follow-up; the user can still upload files via `/api/ingest` multipart from any HTTP client that supports it.
- **Migration of every existing `wiki cite` invocation** — D2's line-number fix is in the validator, not in `cite.py`. Existing callers of `cite` (scripts, prior workflows) keep working with file-line numbers as before. Only the *displayed validator errors* change.
- **Closing all 540 drafts.** K1's edit-path makes draft closure *possible*; `QUAL-2` (draft-debt batch finalizer + auto-abandon policy) is the actual remediation and lives in Phase 2 of the roadmap.
- **Surface-anchor audit for Track B Phase 0.** Separate workstream.
- **`wiki_demote_domain` MCP exposure** (per C4) — kept CLI-only; revisit if a use case emerges.
- **Per-job timezone support in scheduler** — UTC only in v1.
- **iOS / browser Push notifications when scheduled jobs fail** — out of scope.

## Risks

1. **`claude -p --output-format=json` availability.** If the installed CLI version doesn't support the flag, K5's graceful-degrade path kicks in and telemetry stays empty until the user updates. Mitigation: probe at startup; log the degradation; document in M47 milestone doc.
2. **K2 parity test fails after K1 lands if K1's MCP wrappers are forgotten.** Mitigation: the test is the forcing function. K1 cannot merge until it adds `wiki_cite_add` + `wiki_edit` MCP wrappers.
3. **Validator line-number fix breaks downstream tooling that parses validator output.** Mitigation: search the repo for any script that consumes validator stderr; one-line grep before merging. No external consumers known.
4. **Scheduler subprocess execution under launchd has different environment than interactive shell.** Mitigation: scheduler plist replicates the watcher's `EnvironmentVariables` block (PATH + KNOWLEDGE_ROOT); hand-test step 1 catches this.
5. **`.knowledge/auth.yaml` accidentally committed.** Mitigation: explicit `.gitignore` entry (C2) plus `wiki auth add` refuses to write the file if it isn't gitignored.
6. **Tailscale not configured before testing K3.** Mitigation: K3 hand-test starts with `curl` against `localhost:7474`; Tailscale-from-phone is the last step, gated by a one-line "if Tailscale installed" check.
7. **Race between watcher pickup of `raw/inbox/` and TaskStore-triggered `ingest()` writes.** Mitigation: per-source `file_lock(f"ingest-{id}")` is already acquired by `ingest()` (existing code); no new race introduced.

## Critical files index

For wave 1:
- `src/gateway/llm/client.py`, `src/gateway/llm/telemetry.py` (new), `src/gateway/log.py`, `src/gateway/locking.py`, `src/gateway/costs.py` (new), `src/gateway/filter/semantic.py`, `src/gateway/plan.py`, `src/gateway/vlm.py`, `src/gateway/ops/status.py`, `src/gateway/research/orchestrator.py`, `src/gateway/research/analysis.py`, `src/gateway/mcp_server.py`, `tests/gateway/test_mcp_parity.py` (new)

For wave 2:
- K1: `src/gateway/ops/cite_add.py` (new), `src/gateway/ops/edit_section.py` (new), `src/gateway/validator.py`, `src/gateway/cli.py`, `src/gateway/mcp_server.py`, `tests/gateway/test_cite_add.py` (new), `tests/gateway/test_edit_section.py` (new), `tests/gateway/test_validator_line_numbers.py` (new)
- K4: `src/gateway/scheduler.py` (new), `scripts/install_scheduler.sh` (new), `src/gateway/cli.py`, `pyproject.toml`, `TUTORIAL.md`
- K3: `src/gateway/web/auth.py` (new), `src/gateway/web/routes/cloud.py` (new), `src/gateway/web/app.py`, `src/gateway/web/schemas.py`, `src/gateway/cli.py`, `scripts/wiki-auth-add.sh` (new), `scripts/test-ingest-curl.sh` (new), `.gitignore`, `TUTORIAL.md` (incl. "Remote capture from iOS" section), `scripts/wiki-capture.shortcut` (committed by Andrew after on-phone build per D6)

Documentation:
- `docs/milestones/M47.md` (wave 1 hand-test results — new)
- `docs/milestones/M48.md` (wave 2 hand-test results — new)
- `docs/M46-followup-items.md` (update: items #3 and #6 resolved; new item `K3-followup-ios-shortcut`)
