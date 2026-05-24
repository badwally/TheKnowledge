# M44 — Token-Efficient LLM Clients for Research Runs

**Status:** Shipped 2026-05-12. M44.1 (parallel filter) shipped same day. M44.2 (synthesis citation-grounding) and M44.3 (multi-line continuation + draft workflow for framing prose) shipped 2026-05-13.
**Owner:** badwally
**Predecessors:** M37 (research orchestrator), M41 (research UI), M43 (NLM artifacts UI)
**Successors:** filter fine-tuning loop (WIKI § 10.4 trigger detection), eventual open-weight classifier (≥1000 decisions/domain)

## M44.3 — Multi-line structural continuation + draft workflow (2026-05-13)

The M44.2 validation run on the methodology plan (2026-05-13) cleared yesterday's structural-frame rejections but surfaced two residual patterns:

1. **Multi-line structural content.** NotebookLM sometimes splits `**Which themes use it:**` onto one line and the value (a semicolon-separated theme list like `Component-Level Degradation Modeling; Cost and Financial Framing.`) onto the next, with or without a blank line between. The M44.2 single-line allowlist regex only catches the label line; the value line still got flagged.

2. **Framing prose** like *"Based on the provided sources, the corpus presents…"* that NotebookLM emits as the opening sentence of synthesis sections. These are interpretive claims that genuinely should be cited; the M44.2 prompt directive didn't change NotebookLM's behavior here.

**Fix split:**

1. **Validator: one-slot continuation tracking** in `gateway.citations.find_claim_sentences`. When a line is exempted as a structural-frame label — either an inline `**Label:** content` whose label is in the allowlist, or a fully-bold `**Label:**` line whose inner text ends with `:` and is in the allowlist — set an `expect_continuation` flag. The next non-blank line is also exempted, then the flag clears. Blank lines do NOT clear the flag (markdown often inserts a blank between label and value). Any other non-blank line consumes-and-clears.

2. **Framing prose → `--draft` workflow.** No code change. WIKI.md § 5.5 now documents `wiki research --draft` as the recommended path for synthesis-heavy runs; the validator stays strict because framing prose IS a claim. Per-page `wiki cite` / `wiki finalize` finishes the attribution after the fact.

**Files:** `src/gateway/citations.py` (stateful continuation), `WIKI.md` § 5.2 (continuation note) + § 5.5 (`wiki research --draft` recommendation), `tests/gateway/test_authorship.py` (5 new tests: value-on-next-line, value-after-blank-line, no-cascade, non-allowlisted-bold-doesn't-arm, consecutive-labels-chain).

**Validation:** unit-test only (766 passing). End-to-end re-run on the same 05-11 plan is the user's next call — Category A.2 patterns should now be exempt; Category B framing prose still rejects in normal mode but a `--draft` re-run is the expected path.

## M44.2 — Synthesis citation-grounding fixes (2026-05-13)

The 2026-05-12 M44.1 validation run on the methodology plan completed the orchestrator pipeline through analysis but `apply_plan` rejected the synthesis pages: NotebookLM's structural-frame bullets (`**Themes Used In:**`, `**Items Compared:**`, `**Which themes draw on it:**`, etc.) tripped the `citation-grounding` validator even though they're metadata about the analysis frame, not claims about the world. A second class of failure — interpretive cross-source prose like *"A major tension exists between simplified vs complex methods"* — were genuine claims that lacked footnote refs.

Two-part fix:

1. **Validator: explicit allowlist of structural-frame labels** (`gateway/citations.py:_STRUCTURAL_FRAME_LABELS`). Lines matching `**<label>:** <content>` where `<label>` is in the allowlist skip the claim check. Allowlist (not heuristic) so `**Finding:** Drug X causes Y` is still flagged. WIKI.md § 5.2 updated.

2. **Prompts: explicit footnote-ref directive** appended to every claim-emitting prompt in `gateway/research/analysis.py` (`_SPECIFICS_TEMPLATE`, `_COMPARISONS_TEMPLATE`, `_GAPS_TEMPLATE`, `_RECURRING_PATTERNS_PROMPT`, `_SHARED_ANCHORS_PROMPT`, `_RECURRING_TRADEOFFS_PROMPT`). Tells NotebookLM that interpretive sentences must end with `[N]` resolving to `[^N]: [[sources/<id>]]` definitions in the response.

Files: `src/gateway/citations.py`, `src/gateway/research/analysis.py`, `WIKI.md` § 5.2, `tests/gateway/test_authorship.py` (3 new tests: allowlist coverage, strict-allowlist negative case, every-label pin), `tests/gateway/test_research_analysis.py` (3 new tests: directive injected into branch + synthesis prompts, custom queries without placeholder still work).

Expected outcome on re-running 2026-05-11 plan: structural-frame lines no longer rejected; interpretive prose now arrives with footnote refs from NotebookLM.

## M44.1 — Parallel filter (2026-05-12)

The first M44 end-to-end run (2026-05-12, condo-capital-infra reserve-study-firms plan, 178 candidates) surfaced that `_run_filter` was a single `for` loop. Token cost dropped per call but wall-clock per N candidates didn't — Haiku at ~16s/call × 178 sequential = 47 min for filter alone.

`src/gateway/research/orchestrator.py:_run_filter` now uses a `ThreadPoolExecutor` (same pattern as the search-adapter fan-out at `orchestrator.py:178`) with 8 workers by default, configurable via `WIKI_FILTER_MAX_WORKERS`. Per-item `FilterError` is isolated (one bad candidate doesn't sink the batch) and accepted candidates are returned in input order so logs stay deterministic.

Expected on the same 178-candidate run: 47 min → ~6 min (8× speedup). Confirmed in unit tests via a `threading.Barrier(9)` that 8 workers enter `filter_score` simultaneously — the test would deadlock if filtering were still sequential.

Files: `src/gateway/research/orchestrator.py` (`_run_filter` refactor), `tests/gateway/test_research_orchestrator.py` (4 new tests: order preservation, true concurrency via barrier, per-item error isolation, empty input).

---

## 1. TL;DR

A `wiki research` run spawns 100+ `claude -p` subprocesses, each of which is a full Claude Code agent invocation. The agent harness alone (system prompt, tool declarations, CLAUDE.md auto-discovery) costs an estimated 5–10 KB of input tokens per call — paid 100+ times even though filter is a binary triage task that needs none of it. Filter also runs on Opus 4.7, an unnecessarily expensive model for the decision being made.

**M44 introduces a shared `gateway.llm` subprocess wrapper that invokes `claude -p` with these efficiency-targeted flags on every research-run call:**

1. `--tools ""` — strips all built-in tool declarations (the bulk of agent-harness tokens). For VLM, `--tools "Read"` is used instead so Claude Code can attach the image referenced by absolute path.
2. `--system-prompt <static_prefix>` — supplies a compact, task-specific system prompt instead of inheriting Claude Code's default.
3. `--no-session-persistence` — avoids writing a session record per call (~100 sessions per research run would otherwise accumulate on disk and slow startup).
4. `--model claude-haiku-4-5-20251001` for filter only — Haiku for triage; Opus 4.7 stays for plan and VLM.

**`--bare` was evaluated and rejected.** Per `claude --help`: with `--bare`, "Anthropic auth is strictly `ANTHROPIC_API_KEY` or `apiKeyHelper` via `--settings` (OAuth and keychain are never read)." That bypasses Max billing entirely. The wins from `--bare` (skipping hook discovery, plugin sync, CLAUDE.md auto-discovery) are real but cost less than the Max-billing constraint is worth. The remaining flags above still eliminate the bulk of the agent-harness token tax.

The change preserves the `FilterClient` / `PlanClient` / `VLMClient` Protocols, so orchestrator wiring is untouched. The expected outcome is a ≥30% wall-clock reduction per filter call from harness elimination alone, plus a further large cost reduction from Haiku routing.

The user is on Claude Max. **Anthropic API key billing, the SDK, and `cache_control` prompt caching are explicitly out of scope** — they require switching billing modes, which the user has declined for this milestone.

---

## 2. Motivation

### 2.1 The cost profile of a research run today

A single `wiki research "<prompt>" --domain <slug>` invocation drives the following per-item LLM operations through `src/gateway/research/orchestrator.py`:

| Stage | Where | Per-run call count | Per-call payload |
|---|---|---|---|
| Filter | `_run_filter` (line 229–264) → `filter_score` (`semantic.py`) | ~100 (one per candidate source) | system prompt + policy YAML + examples bank + per-source frontmatter + body head (≤16 KB) |
| Materialize / VLM | image conversion inside per-source materialize step | variable (per image found) | system prompt + describe prompt + image |
| Query planning | `_query_planner.plan_per_adapter_queries` (line 668) | 1 per run | system prompt + research prompt + adapter list |
| Plan | `plan.py` `ClaudeCLIPlanClient` | invoked during ingest path (per source) | system prompt + source fulltext + relevant existing wiki pages |
| Analysis / synthesis | step 12 (line 1049) | once per run, multi-source | aggregated source summaries |

Filter dominates by frequency. Every filter call today is:

```
claude -p "<concatenated_template_with_policy_examples_source>"
```

Where the prompt template at `src/gateway/filter/semantic.py:113-143` interpolates everything — policy YAML, formatted examples, source frontmatter, body head — into one monolithic string.

### 2.2 Three sources of waste

**(a) Agent-harness tax.** `claude -p` without any flags loads the full Claude Code agent system prompt: tool inventory (Bash, Edit, Read, Write, Grep, …), permission rules, communication preferences, MCP integration descriptions, plus auto-discovered `CLAUDE.md` from cwd and ancestors. For this repo, that pulls in the project `CLAUDE.md` plus the global one — together roughly 5–10 KB of tokens unrelated to the actual filter task.

**(b) Repeated static prefix.** The policy YAML and examples bank are identical across all candidates in a single run, but `build_prompt` rebuilds and resends them per-call. Without prompt caching (which is API-key-only — see §3), this is unavoidable *unless* we minimize the prefix's payload and accept the per-call retransmission.

**(c) Model overkill.** Filter answers "score 0.0–1.0 with one-sentence rationale" against a clear policy. This is the canonical Haiku use case. Opus 4.7's reasoning capability is wasted here.

### 2.3 Why now

M37–M43 stabilized the research orchestrator and UI. Filter call counts grew with each new search adapter, and recent multi-hundred-candidate runs (e.g., `nlm/query_plans/2026-05-08-how-should-a-condo-hoa-integrate.yaml`, `2026-05-09-best-practices-for-proactive-and-preventive.yaml`) made the per-call overhead visible. The long-term path is a local classifier (WIKI § 10.4, triggered at ~1000 pinned decisions per domain), but that's many runs away. M44 is the bridge.

---

## 3. Constraints

| Constraint | Reason | Consequence |
|---|---|---|
| **Stay on Claude Max billing.** No switch to metered Anthropic API key billing. | User directive in design session (2026-05-10). | `cache_control` prompt caching is unavailable — it requires `claude auth login --console` (API-key auth). The Anthropic Python SDK is out of scope. All wins must come from `claude -p` CLI flags. |
| **Preserve `FilterClient` / `PlanClient` / `VLMClient` Protocols.** | These are the orchestrator's injection surface; consumers in `research/orchestrator.py` and elsewhere depend on them. | Implementation changes are confined to the client classes and their prompt-assembly helpers. No churn to `_run_filter` or other orchestrator code. |
| **No regression on filter decision quality.** | A/B regression against pinned `wiki filter-correct` decisions is mandatory. | Haiku routing must clear ≥95% agreement on the pinned-corrections set before rollout. |
| **No new external services or dependencies.** | Minimize surface area. | Implementation uses only `subprocess` and stdlib; no new pip packages. |
| **Auto-mode-safe rollout.** | User runs autonomously between sessions. | Falls back gracefully if a flag is unsupported on the installed `claude` CLI version (detect and warn, don't crash mid-run). |

---

## 4. Goals & non-goals

### Goals

1. Eliminate the Claude Code agent-harness tax on every research-run LLM call.
2. Route filter to Haiku 4.5; keep plan and VLM on Opus 4.7.
3. Centralize subprocess invocation, retry, and error mapping into one place (currently triplicated across `semantic.py:80-107`, `plan.py:174-200`, `vlm.py:29-74`).
4. Preserve per-item isolation in filter — every candidate gets its own scored decision and rationale, feeding the existing `wiki filter-correct` fine-tuning bank.

### Non-goals

- **Prompt caching** — requires API-key billing (excluded by §3).
- **Multi-item batching** (pack N candidates per call) — defers per-item isolation and complicates the fine-tuning bank; revisit only if §11 monitoring shows post-rollout cost remains uncomfortable.
- **Anthropic SDK migration** — same billing constraint.
- **Replacing the local-classifier endgame** — the long-term path remains a fine-tuned classifier per WIKI § 10.4.
- **Changes to NotebookLM-side operations** — out of scope; those route through a separate MCP path.
- **Re-architecting the analysis / synthesis stage** — its call volume is O(1) per run, not the bottleneck.

---

## 5. Design

### 5.1 The three levers, in detail

#### 5.1.1 `--tools ""` (and the `--bare` trap)

`--tools ""` disables every built-in tool (Bash, Read, Edit, Write, Grep, Glob, etc.), which also removes their declarations from the system prompt. This is the largest single saving — the tool inventory is the bulk of the agent-harness token tax.

Trade-off: nothing the filter / plan stages do today uses Claude Code's tools. They send a prompt, expect text or JSON back, parse it. No tool calls happen mid-response. So stripping the tool layer is pure overhead removal.

**VLM exception:** the image-description path needs the Read tool to attach the image referenced by absolute path. VLM passes `--tools "Read"` plus `--dangerously-skip-permissions` (the path is outside cwd; the prompt is constrained to image description; stdout is captured).

**Why not `--bare`?** It looks tempting (skips hooks, plugin sync, CLAUDE.md, auto-memory) but per `claude --help`: "Anthropic auth is strictly `ANTHROPIC_API_KEY` or `apiKeyHelper` via `--settings` (OAuth and keychain are never read)." On a Max plan with no API credit, `--bare` makes every call fail with "Credit balance is too low" even though the user has Max entitlement. Discovered the hard way during M44 sanity-check; documented here for future reference.

#### 5.1.2 `--system-prompt <static_prefix>`

Today, `build_prompt` produces one monolithic string. We split it:

- **System prefix (stable within a run):**
  - Filter: `_PROMPT_TEMPLATE` header + policy YAML + formatted examples bank + instructions section
  - Plan: the system prompt block at `plan.py:206-320` (conventions, schema, task instructions)
  - VLM: the system prompt + caller-supplied describe directive

- **User positional (varies per item):**
  - Filter: source frontmatter + body head
  - Plan: source fulltext + relevant existing wiki pages
  - VLM: image attachment

Passing the prefix via `--system-prompt` rather than as a literal positional has two effects:

1. It replaces (not appends to) Claude Code's default system prompt — combined with `--tools ""`, the model receives our task-specific system prompt without the tool inventory.
2. The user positional becomes much smaller and cleaner — easier to debug, easier to log.

Note: we cannot rely on the prefix being cached across calls (caching requires API billing). The benefit is structural — minimize total input, make the call shape predictable — not cache-based.

#### 5.1.3 `--model claude-haiku-4-5-20251001` for filter

Plan and VLM keep Opus 4.7. Filter goes to Haiku 4.5. The exact model ID is pinned (not the alias `haiku`) so the model is stable across CLI updates.

Quality validation: §10.3 regression check requires ≥95% decision agreement against pinned `wiki filter-correct` corrections before rollout. If Haiku falls short on a specific domain's policy, fall back to Opus for that domain only (per-domain model override via config).

### 5.2 Final argv shape per stage

```
# Filter
claude -p \
  --no-session-persistence \
  --tools "" \
  --model claude-haiku-4-5-20251001 \
  --system-prompt "<filter system + policy + examples + instructions>" \
  "<source frontmatter + body head>"

# Plan
claude -p \
  --no-session-persistence \
  --tools "" \
  --model claude-opus-4-7 \
  --system-prompt "<plan system + conventions + schema>" \
  "<source fulltext + relevant existing pages>"

# VLM (Read tool kept for image attachment)
claude -p \
  --no-session-persistence \
  --tools "Read" \
  --dangerously-skip-permissions \
  --model claude-opus-4-7 \
  --system-prompt "<VLM system + describe directive>" \
  "Image path: <abs_path>"
```

`--no-session-persistence` prevents `claude -p` from writing a session record per call (~100 sessions per research run is noise on the user's machine and slows startup over time).

### 5.3 Why a shared client

Today, retry/backoff and error mapping are duplicated:

- `src/gateway/filter/semantic.py:80-107` (`ClaudeCLIFilterClient.call` — 3 retries, exponential backoff)
- `src/gateway/plan.py:174-200` (`ClaudeCLIPlanClient.call`)
- `src/gateway/vlm.py:29-74` (`ClaudeCLIVLMClient.describe` — 180s timeout, no retry)

M44 consolidates these into `gateway.llm.client.ClaudeCLIClient`, exposing:

```python
class ClaudeCLIClient:
    def call(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: str,
        max_retries: int = 3,
        timeout: int = 180,
        output_format: Literal["text", "json"] = "text",
    ) -> str: ...
```

Each per-stage client (`ClaudeCLIFilterClient`, `ClaudeCLIPlanClient`, `ClaudeCLIVLMClient`) becomes a thin shim that builds `system_prompt` + `user_prompt` and calls into this shared client. The Protocols (`FilterClient`, etc.) stay unchanged.

---

## 6. File plan

### 6.1 New files

| Path | Purpose |
|---|---|
| `src/gateway/llm/__init__.py` | Public surface: `ClaudeCLIClient`, `LLMError` |
| `src/gateway/llm/client.py` | The shared subprocess wrapper. Argv construction, retry/backoff, error mapping, optional structured-output parsing (`--output-format json` when caller passes `output_format="json"`). |
| `src/gateway/llm/config.py` | Model selection per stage (defaults: filter=Haiku 4.5, plan=Opus 4.7, VLM=Opus 4.7) and per-domain override hooks. |
| `tests/gateway/test_llm_client.py` | Unit tests: argv assembly (asserts `--tools ""`, `--no-session-persistence`, `--model`, `--system-prompt` present and correctly ordered; asserts `--bare` is **never** present), retry behavior under transient failure, error mapping, timeout. Mocks `subprocess.run`. |

### 6.2 Modified files

| Path | Change |
|---|---|
| `src/gateway/filter/semantic.py` | `ClaudeCLIFilterClient.call` delegates to `ClaudeCLIClient` with `model=` from `llm/config.py`. `build_prompt` is split into two functions: `build_filter_system_prompt(policy, examples) -> str` and `build_filter_user_prompt(front, body_head) -> str`. The original monolithic `_PROMPT_TEMPLATE` is decomposed but each piece survives — the wording doesn't change, only where each piece lands in the argv. |
| `src/gateway/plan.py` | Same pattern: split `build_plan_prompt` into `build_plan_system_prompt` (the instructions block at lines 206–320) and `build_plan_user_prompt` (source fulltext + existing pages). `ClaudeCLIPlanClient.call` becomes a shim around `ClaudeCLIClient`. |
| `src/gateway/vlm.py` | `ClaudeCLIVLMClient.describe` delegates to `ClaudeCLIClient`. The describe-prompt that the caller provides becomes part of the system prompt; the image path is the user positional. |
| `tests/gateway/test_filter.py` | Update mocks to patch `gateway.llm.client.ClaudeCLIClient.call`. Add argv-shape assertions. |
| `tests/gateway/test_plan.py` (if exists) and `tests/gateway/test_ingest.py` | Same updates. |
| `tests/gateway/test_query_via_nlm.py` | Verify analysis path still works; no model change here. |

### 6.3 Files explicitly untouched

| Path | Why |
|---|---|
| `src/gateway/research/orchestrator.py` | The `_run_filter` loop and all other orchestration are agnostic to client internals. Injection via `client=` parameter (line 255) continues to work. |
| `FilterClient` / `PlanClient` / `VLMClient` Protocols | Public contracts; consumers depend on shapes. |
| `WIKI.md` | No conventions change. M44 is an internal efficiency play. |
| `BUILD.md` § 9 | Update post-delivery, not pre. |

### 6.4 Configuration touch points

`src/gateway/llm/config.py` exposes:

```python
DEFAULT_FILTER_MODEL = "claude-haiku-4-5-20251001"
DEFAULT_PLAN_MODEL = "claude-opus-4-7"
DEFAULT_VLM_MODEL = "claude-opus-4-7"

# Per-domain override (loaded from .knowledge/policies/<domain>/model.yaml if present)
def model_for(stage: Stage, domain: str | None) -> str: ...
```

Per-domain override mechanism is included as a forward-compatible hook but defaults are sufficient — no domain currently needs an override at rollout. If §10.3 finds a domain where Haiku falls short on filter, that domain's `model.yaml` gets a one-line override.

---

## 7. Backwards compatibility & rollout

### 7.1 No flag-gating

The change is applied directly. Reasons:

- The Protocols are preserved, so callers don't know which CLI flags the client uses internally.
- The argv changes are additive (`--tools`, `--no-session-persistence`) plus one model selection (`--model`). All are documented Claude Code CLI flags as of 2026-05.
- A `claude` CLI version too old to support these flags will fail loudly on the first call with stderr surfaced by the shared client's error mapping (§5.3).

### 7.2 Sequence

1. Land the shared `gateway.llm.client.ClaudeCLIClient` and its tests in isolation.
2. Migrate filter (`ClaudeCLIFilterClient`) to the shared client. Run §10.3 regression. Commit.
3. Migrate plan (`ClaudeCLIPlanClient`). Commit.
4. Migrate VLM (`ClaudeCLIVLMClient`). Commit.
5. Hand-test a full `wiki research` run end to end against a known prompt.
6. Update `BUILD.md` § 10 with a `### M44` section.

Each step is its own PR-shaped change. Rollback is a `git revert` of the relevant commit.

### 7.3 Telemetry

The shared client logs (at debug level) the model, system-prompt length, user-prompt length, and wall-clock per call. After rollout, an ad-hoc inspection of `log.md` and the orchestrator's debug output confirms the argv is correct and Haiku is being invoked.

---

## 8. Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Haiku underperforms on filter for some domain's policy | Medium | High (filter accept/reject quality degrades) | §10.3 regression against pinned `wiki filter-correct` set on every supported domain before rollout. Per-domain override in `llm/config.py` for fallback. |
| Hooks or CLAUDE.md auto-discovery inject context that conflicts with our `--system-prompt` | Low | Low | `--system-prompt` replaces (not appends to) the default. Hand-tested on one real filter call (reserve study, 2026-05-12) — Haiku scored 1.00 with on-policy rationale. |
| `--system-prompt` interacts unexpectedly with Claude Code's prompt assembly | Low | Low | Hand-tested on the filter sanity check; rationale was coherent and policy-grounded. |
| `claude` CLI version mismatch (older version missing a flag) | Low | Low | Loud error on first call (§7.1). User runs `claude update` and retries. |
| Multi-hundred-candidate runs trigger session-persistence path despite `--no-session-persistence` and slow over time | Very low | Low | Telemetry watches startup time per call; alert if drift. |
| Cost regression on plan/VLM because some prompts get *bigger* when split (system prompt and user prompt are both sent) | Very low | Negligible | The split is purely positional reorganization, not content addition. Token totals are unchanged (minus the harness savings). |

---

## 9. Open questions (deferred, not blocking M44)

1. **Multi-item batching for filter.** Pack 10–20 candidates per call and request a JSON array of decisions. Would amortize per-call fixed costs further. Compromises per-item isolation and complicates the fine-tuning bank. Revisit only if post-rollout monitoring shows filter cost still uncomfortable.
2. **API-key billing for cache.** Re-evaluate if the user's research-run volume grows substantially, since cache discount (90% off cached tokens) on policy + examples would be larger than Haiku's discount. Currently declined by user preference for Max billing simplicity.
3. **Gateway `wiki cite` / `wiki edit` ops.** Per `gateway_edit_path_open_question` memory — unrelated to M44 but the LLM client work might surface a clean place to hook those ops.

---

## 10. Verification

### 10.1 Unit tests

```bash
pytest tests/gateway/test_llm_client.py \
       tests/gateway/test_filter.py \
       tests/gateway/test_ingest.py \
       -q
```

Required assertions in `test_llm_client.py`:

- argv contains, in order: `claude`, `-p`, `--no-session-persistence`, `--tools`, `""`, `--model`, `<expected_model>`, `--system-prompt`, `<expected_prefix>`, `<expected_user_prompt>`
- argv must **not** contain `--bare` (would force API-key auth and break Max billing)
- retry triggers on transient subprocess failure (exit code != 0)
- timeout maps to `LLMError`
- structured-output parsing path returns parsed JSON when `output_format="json"`

### 10.2 Integration hand-test

1. Choose a previously-run research prompt with ~100 candidates. Recent options:
   - `nlm/query_plans/2026-05-08-how-should-a-condo-hoa-integrate.yaml`
   - `nlm/query_plans/2026-05-09-best-practices-for-proactive-and-preventive.yaml`
2. Run end-to-end:
   ```bash
   wiki research "<prompt>" --domain condo
   ```
3. Verify in debug log:
   - Filter argv contains `--model claude-haiku-4-5-20251001`
   - Plan and VLM argv contain `--model claude-opus-4-7`
   - All three contain `--no-session-persistence` and `--tools` (`""` for filter/plan, `"Read"` for VLM); none contain `--bare`
4. Compare reported wall-clock and Claude Code usage counters against pre-change baseline captured from a prior run in `log.md`.

### 10.3 A/B regression (decision-quality gate)

For each domain with pinned `wiki filter-correct` decisions:

1. Replay the last 20 pinned decisions through the new Haiku-routed filter.
2. Compute agreement rate against the pinned label.
3. Required: ≥95% agreement.
4. If a domain falls short, set its `policies/<domain>/model.yaml` to `filter_model: claude-opus-4-7` and document in §11 follow-up.

### 10.4 Acceptance criteria

- All filter subprocess invocations during `wiki research` use the new argv with Haiku.
- All plan and VLM invocations use the new argv with Opus.
- `FilterClient` / `PlanClient` / `VLMClient` Protocols are untouched.
- `wiki lint` and `wiki lint --scope orphans` clean.
- A/B regression ≥95% agreement across every domain with ≥20 pinned decisions.
- `BUILD.md` § 10 has an `### M44 — Token-efficient LLM clients` entry summarizing delivery, hand-test outcomes, and any per-domain overrides set.

---

## 11. Glossary & references

| Term | Definition |
|---|---|
| **Agent harness** | Claude Code's default system prompt + tool declarations + CLAUDE.md auto-discovery context, loaded into every `claude -p` call by default. |
| **Filter** | The gateway stage that scores each candidate source against an editorial policy on a 0.0–1.0 relevance scale (`src/gateway/filter/semantic.py`). |
| **Plan** | The gateway stage that proposes which wiki pages to create/update per ingested source (`src/gateway/plan.py`). |
| **VLM** | Vision-language-model wrapper for image descriptions during source conversion (`src/gateway/vlm.py`). |
| **Pinned decision** | A filter decision corrected by the user via `wiki filter-correct`, feeding the fine-tuning examples bank. |
| **Editorial policy** | The YAML at `.knowledge/policies/<domain>/policy.yaml` that defines inclusion/exclusion criteria for a research domain. |
| **MAX billing** | Claude Max subscription, in which `claude -p` charges against the subscription rather than per-token API metering. |

### References

- `CLAUDE.md` (project root) — gateway operating rules
- `WIKI.md` § 10.4 — long-term local-classifier path
- `BUILD.md` § 10 — milestone history (M37–M43 delivered; M44 to be added post-implementation)
- `src/gateway/research/orchestrator.py:229-264` — `_run_filter` injection site
- `src/gateway/filter/semantic.py:113-143` — current monolithic prompt template
- Claude Code CLI flags — `claude --help`; particularly `--tools`, `--system-prompt`, `--model`, `--no-session-persistence`. **Avoid `--bare`**: it forces API-key auth and is incompatible with Max billing.
