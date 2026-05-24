# M50 — QUAL-12 Eval Framework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a per-domain eval framework so every future milestone can prove (or disprove) "the system got better." v1 reads per-domain golden Q/A pairs (`.knowledge/eval/<domain>/goldens.yaml`), runs each question against the live wiki state (mode B — no new synthesis), scores via Sonnet 4.6 LLM-as-judge against a hybrid rubric (source-id `must_cite` + natural-language `must_assert`/`must_not_assert`), persists per-run results + a trend CSV, and surfaces last-eval scores in `wiki status`.

**Architecture:** Five focused modules under `src/gateway/evaluate/`: `schema` (Golden / EvalResult dataclasses + YAML I/O), `wiki_context` (assembles relevant wiki pages for the judge prompt), `judge` (Sonnet 4.6 call via TOK-1 `AnthropicAPIClient` with `cache_control` on the rubric block), `runner` (orchestrator: walks goldens, calls judge per Q, accumulates results), `persistence` (per-run YAML + append to trend CSV). One gateway op (`gateway.ops.evaluate_op`) wraps the runner for `wiki evaluate` CLI + `wiki_evaluate` MCP tool. Hand-authored 15 Q/A seed set for `glp1-reward-modulation` is the bootstrap content.

**Tech Stack:** Python 3.12, `anthropic` SDK (already shipped in M49), PyYAML, existing `gateway.frontmatter` / `gateway.paths` / `gateway.log`, `pytest`.

---

## Background

**Why XL in the review, M-sized in v1.** The review sized QUAL-12 as XL because it gates the downstream work (QUAL-6 link-rot, QUAL-8 semantic citation coherence, QUAL-10 filter calibration) and unlocks regression detection forever. The shipped v1 is narrower: schema + runner + 15 goldens for one domain. Subsequent milestones add CI hook, retraining loop, more domains, judge prompt tuning, trend visualization.

**Why mode B (wiki-state-only).** Mode A (re-run `wiki query`) would exercise the full synthesis pipeline but is slow (~30s per Q), expensive, writes draft pages on every run, and pollutes the wiki. Mode B reads the existing wiki and judges against current state. It reflects the surface downstream consumers (chief-of-staff, ai-tutor, newbiz) will actually hit. Mode A can be added later as `--mode=query` if needed.

**Why hybrid scoring.** Pure source-id matching is too rigid; pure semantic matching loses cite-grounding discipline. Hybrid: `must_cite` is source-id-strict, `must_assert`/`must_not_assert` is LLM-judged semantic match.

**Why glp1-reward-modulation as seed.** Most synthesized content in the wiki + the user's deepest prior knowledge to author goldens against. Other domains follow once the framework proves out.

---

## File Structure

**Create (source):**
- `src/gateway/evaluate/__init__.py` — package init, exports
- `src/gateway/evaluate/schema.py` — `Golden`, `EvalResult`, `EvalRunSummary` dataclasses + YAML load/save + scaffold helper
- `src/gateway/evaluate/wiki_context.py` — `load_wiki_context(domain) -> str` assembles synthesis pages + sources for one domain
- `src/gateway/evaluate/judge.py` — `Judge` class wrapping `AnthropicAPIClient`; `judge.score(golden, wiki_context) -> EvalResult`
- `src/gateway/evaluate/runner.py` — `run_evaluate(domain, limit, client) -> EvalRunSummary` orchestrator
- `src/gateway/evaluate/persistence.py` — write per-run YAML; append to trend CSV
- `src/gateway/ops/evaluate_op.py` — gateway op (name `evaluate_op` to avoid Python-`eval` security-hook collision): `evaluate_op(domain, limit, scaffold) -> OperationResult`

**Create (tests):**
- `tests/gateway/evaluate/__init__.py`, `tests/gateway/evaluate/test_schema.py`, `tests/gateway/evaluate/test_wiki_context.py`, `tests/gateway/evaluate/test_judge.py`, `tests/gateway/evaluate/test_runner.py`, `tests/gateway/evaluate/test_persistence.py`, `tests/gateway/test_evaluate_op.py`

**Create (content):**
- `.knowledge/eval/glp1-reward-modulation/goldens.yaml` — 15 hand-authored Q/A (Phase H, user-authored)

**Modify:**
- `src/gateway/cli.py` — add `eval` subcommand (positional optional `domain` arg, `--limit`, `--scaffold <domain>`)
- `src/gateway/mcp_server.py` — add `wiki_evaluate` MCP tool (K2 parity)
- `src/gateway/ops/status.py` — last-eval-score line per domain
- `src/gateway/llm/config.py` — add `evaluate_judge` stage (Sonnet 4.6 default)
- `WIKI.md` — Gateway Operations table + new § on eval framework
- `BUILD.md` — append M50 row to § 10
- `docs/milestones/M50.md` — milestone delivery doc

**Test count target:** 924 → ≥ 960 (~36 new tests).

---

## Open Decisions (resolved before plan write)

1. **Mode** — B (wiki-state-only). Mode A deferred.
2. **Scoring** — Hybrid. `must_cite` source-id-strict; `must_assert`/`must_not_assert` LLM-judged.
3. **Surface** — Single `wiki evaluate [domain] [--limit N] [--scaffold <domain>]`. No sub-actions.
4. **Judge model** — Sonnet 4.6 via TOK-1 `AnthropicAPIClient` with `cache_control` on rubric.
5. **Seed domain** — `glp1-reward-modulation`. 15 Q/A.
6. **Persistence** — `.knowledge/eval/<domain>/runs/<UTC-ts>.yaml` per-run + `.knowledge/eval/<domain>/trend.csv` time series.
7. **`wiki status`** — show last-eval score per domain. Trend viz deferred.
8. **CI hook** — deferred.
9. **Op module name** — `gateway.ops.evaluate_op` (not `eval`) to avoid the global Write hook that flags `eval()`-like patterns.

---

# Phase A — Schema, dataclasses, scaffold

### Task A1: Failing tests for `Golden` schema

Files: create `tests/gateway/evaluate/__init__.py` (empty), create `tests/gateway/evaluate/test_schema.py` covering:
- YAML round-trip preserves all fields (`id`, `question`, `must_cite`, `must_assert`, `must_not_assert`, `rubric_weight`).
- Missing required field raises `SchemaError`.
- Duplicate id raises `SchemaError`.

Run `pytest tests/gateway/evaluate/test_schema.py -v`, expect ImportError.

### Task A2: Implement `schema.py`

Dataclasses: `Golden(id, question, must_cite, must_assert, must_not_assert, rubric_weight)`, `EvalResult(golden_id, question, score, cite_hits, cite_misses, assertion_hits, assertion_misses, anti_assertion_violations, judge_reasoning, input_tokens, output_tokens, cache_read_tokens)`, `EvalRunSummary(domain, timestamp, n_questions, mean_score, results, total_input_tokens, total_output_tokens, total_cache_read_tokens)`.

Functions: `load_goldens(path) -> list[Golden]` (validate required fields + duplicate ids), `save_goldens(path, list[Golden])`.

Exception: `SchemaError(ValueError)`.

Default `rubric_weight = {"cite": 0.4, "assert": 0.5, "anti": 0.1}`.

Re-run tests, expect 3 PASS.

### Task A3: Add `evaluate_judge` stage to `gateway.llm.config`

Add `"evaluate_judge"` to `Stage` Literal; `DEFAULT_EVALUATE_JUDGE_MODEL = "claude-sonnet-4-6"`; new branch in `model_for`. Add a test `test_model_for_evaluate_judge_returns_sonnet` to `tests/test_llm_config.py`.

### Task A4: `scaffold_template(path, *, domain)` helper

Add to `schema.py`: writes a goldens.yaml with one placeholder entry (id `q01`, question containing the literal word "EXAMPLE" and the domain name, placeholder must_cite/must_assert/must_not_assert). Raises `FileExistsError` if path exists.

Test: scaffolding writes one placeholder; loading round-trips.

### Task A5: Commit Phase A

```
git add src/gateway/evaluate/ src/gateway/llm/config.py tests/gateway/evaluate/ tests/test_llm_config.py
git commit -m "feat(m50): eval framework schema + scaffold + judge stage registration"
```

Run `pytest tests/ -q --tb=no | tail -3` first to confirm no regressions.

---

# Phase B — Wiki context assembly

### Task B1: Failing tests for `load_wiki_context`

`tests/gateway/evaluate/test_wiki_context.py`: cover (a) loads domain synthesis pages + their source bodies, (b) excludes other-domain pages, (c) raises `ContextTooLargeError` when assembled size > `max_chars`.

### Task B2: Implement `wiki_context.py`

`load_wiki_context(domain, *, max_chars=500_000) -> str` assembles:
1. All synthesis pages whose frontmatter `domains:` includes `domain`.
2. All concept pages (first 20 lines each) for that domain.
3. All entity pages (first 15 lines each) for that domain.
4. Raw source bodies for every `synthesizes:` entry collected from those synthesis pages.

Each block wrapped in XML-tagged sections (`<page>...</page>`, `<source>...</source>`) to harden against prompt injection per M49 discipline.

Strip `sources/` prefix when looking up raw files (same fix as M49 commit `f1c27f2`).

Raises `ContextTooLargeError` if total chars > `max_chars`.

### Task B3: Commit Phase B

```
git add src/gateway/evaluate/wiki_context.py tests/gateway/evaluate/test_wiki_context.py
git commit -m "feat(m50): eval wiki_context loader — domain-scoped page + source assembly"
```

---

# Phase C — LLM-as-judge

### Task C1: Failing tests for `Judge`

`tests/gateway/evaluate/test_judge.py` with mocked `AnthropicAPIClient`:
- Parses structured JSON output into `EvalResult` (score, cite_hits, cite_misses, assertion_hits, anti_violations, reasoning).
- Malformed JSON returns score 0.0 with diagnostic in `judge_reasoning` (warns, doesn't raise).
- Telemetry fields (`input_tokens`, `output_tokens`, `cache_read_tokens`) surface from `CallResult` onto `EvalResult`.

### Task C2: Implement `judge.py`

`Judge.__init__(*, client=None, max_tokens=4096)`; `Judge.score(*, golden, wiki_context) -> EvalResult`.

System prompt embeds the rubric — long stable text, gets `cache_control={"type": "ephemeral"}` automatically via `AnthropicAPIClient` default (`cache_system_prompt=True`).

User prompt: WIKI CONTEXT block, QUESTION, GOLDEN EXPECTATIONS (must_cite / must_assert / must_not_assert / rubric_weight as JSON).

Judge outputs strictly:
`{"score": <float>, "cite_hits": [...], "cite_misses": [...], "assertion_hits": [...], "assertion_misses": [...], "anti_assertion_violations": [...], "reasoning": "..."}`

Parse with code-fence tolerance (same pattern as `cite_suggest`). Log warning on JSON decode failure.

Commit:
```
git add src/gateway/evaluate/judge.py tests/gateway/evaluate/test_judge.py
git commit -m "feat(m50): judge — Sonnet 4.6 LLM-as-judge with cached rubric prefix"
```

---

# Phase D — Persistence

### Task D1: Failing tests for `persistence.py`

Cover: `write_run` creates `.knowledge/eval/<domain>/runs/<ts>.yaml` with full summary serialized; `append_to_trend` creates trend.csv with header on first call, appends on subsequent calls; `read_trend` returns list of dict rows.

### Task D2: Implement `persistence.py`

Functions: `eval_dir_for(domain)`, `runs_dir_for(domain)`, `trend_path_for(domain)`, `goldens_path_for(domain)`, `write_run(summary)`, `append_to_trend(summary)`, `read_trend(domain)`.

CSV columns: `timestamp, n_questions, mean_score, total_input_tokens, total_output_tokens, total_cache_read_tokens`.

Commit:
```
git add src/gateway/evaluate/persistence.py tests/gateway/evaluate/test_persistence.py
git commit -m "feat(m50): eval persistence — per-run YAML + trend CSV"
```

---

# Phase E — Runner

### Task E1: Failing tests for `runner.py`

Cover: `run_evaluate(domain)` dispatches one judge call per golden; `--limit` caps; missing goldens raises `NoGoldensError`; result writes both YAML + trend CSV; mean score computed correctly.

### Task E2: Implement `runner.py`

`run_evaluate(domain, *, limit=None, client=None) -> EvalRunSummary`. Flow:
1. Load goldens (`NoGoldensError` if missing).
2. Slice by `limit` if provided.
3. Load wiki context for domain once (reused across all judge calls).
4. Instantiate Judge once (so cache benefit accrues across questions).
5. For each golden, call `judge.score`. Collect results.
6. Compute mean. Build `EvalRunSummary`.
7. Call `write_run` + `append_to_trend`.

Commit:
```
git add src/gateway/evaluate/runner.py tests/gateway/evaluate/test_runner.py
git commit -m "feat(m50): eval runner — orchestrator + persistence wiring"
```

---

# Phase F — Gateway op + CLI + MCP

### Task F1: Implement `gateway.ops.evaluate_op`

`evaluate_op(*, domain, limit, scaffold) -> OperationResult`:
- If `scaffold`: call `scaffold_template`. Return success or `FileExistsError`.
- Else if no `domain`: error.
- Else: call `run_evaluate`. Catch `NoGoldensError`. Append log entry with `fields={domain, n_questions, mean_score, input_tokens, cache_read_tokens}`. Return summary with `paths_touched=[run-yaml, trend.csv, log.md]`.

Test in `tests/gateway/test_evaluate_op.py`: scaffold path, missing-domain path, runs-and-returns-mean path.

### Task F2: Wire CLI

In `src/gateway/cli.py`:
- SUBCOMMANDS entry: `"eval": "Run the per-domain eval (M50)..."`.
- Add to `IMPLEMENTED` set.
- Argparse: `domain` (nargs="?"), `--limit` (int), `--scaffold` (str, metavar="DOMAIN").
- `_run_evaluate(ns)` calls `gateway.ops.evaluate_op.evaluate_op(...)`.

### Task F3: MCP parity

In `src/gateway/mcp_server.py` add `wiki_evaluate(domain=None, limit=None, scaffold=None)` mirroring CLI; call `evaluate_op()`; serialize result. Run `pytest tests/gateway/test_mcp_parity.py` to confirm parity test passes.

Commit:
```
git add src/gateway/ops/evaluate_op.py tests/gateway/test_evaluate_op.py src/gateway/cli.py src/gateway/mcp_server.py
git commit -m "feat(m50): wiki evaluate gateway op + CLI + MCP parity"
```

---

# Phase G — `wiki status` integration

### Task G1: Add eval block to `wiki status`

Read existing `src/gateway/ops/status.py`. Add a helper that iterates `.knowledge/eval/*/trend.csv` files; for each domain shows the most recent row's `mean_score` + delta vs prior row (e.g., `+0.05` or `-0.03`); empty trend produces no row.

Hand-test: `.venv/bin/wiki status` shows new "Eval scores" section (empty until Phase H runs).

Commit:
```
git add src/gateway/ops/status.py tests/gateway/test_status.py
git commit -m "feat(m50): wiki status — last-eval score per domain + delta"
```

---

# Phase H — Seed goldens + live hand-test

### Task H1 (controller-driven, NOT a subagent task)

User must hand-author the 15 goldens because they encode domain expertise. Steps:

1. `.venv/bin/wiki evaluate --scaffold glp1-reward-modulation` — writes the placeholder.
2. Edit `.knowledge/eval/glp1-reward-modulation/goldens.yaml`: replace `q01` placeholder with 15 real Q/A entries. Each: `id` (q01..q15), `question`, `must_cite` (bare source-ids the wiki must reference), `must_assert` (2-4 natural-language facts), `must_not_assert` (1-2 wrong-statement traps), optional per-entry `rubric_weight`.
3. Commit:
   ```
   git add .knowledge/eval/glp1-reward-modulation/goldens.yaml
   git commit -m "data(m50): 15-Q/A seed goldens for glp1-reward-modulation"
   ```

### Task H2: Live hand-test

1. `.venv/bin/wiki evaluate glp1-reward-modulation` — 15 Sonnet 4.6 judge calls. Wall time ~2-5 min. Cost ~$0.50-$1.00 (cache amortizes after Q1). Per-run YAML + trend.csv + log entry created.
2. Inspect: `cat .knowledge/eval/glp1-reward-modulation/runs/<UTC-ts>.yaml`; `wiki status`.
3. Record findings in `docs/milestones/M50.md` (Phase I).

---

# Phase I — Docs + tag

### Task I1: WIKI.md

Append two rows to Gateway Operations table. Add a new § on the eval framework (schema, where results live, when to add goldens).

### Task I2: BUILD.md row + M50 milestone doc

Mirror M49.md shape. Cover goal, components, modules, test delta, acceptance, hand-test results, follow-ups (CI hook, more domains, mode-A query re-runs, judge prompt tuning).

### Task I3: Tag + push

`pytest tests/ -q | tail -3` → expect ≥ 960.
`git tag m50-qual12-eval-framework`.
`git push origin main && git push origin m50-qual12-eval-framework`.

---

## Self-Review

1. **Spec coverage:** schema ✓ (A1-A5), wiki_context ✓ (B1-B3), judge ✓ (C1-C2), persistence ✓ (D1-D2), runner ✓ (E1-E2), CLI/MCP ✓ (F1-F3), status ✓ (G1), seed goldens ✓ (H1), hand-test ✓ (H2), docs ✓ (I1-I3).
2. **Placeholder scan:** none.
3. **Type consistency:** `EvalResult` shape consistent across schema/judge/runner/persistence. `Golden` consistent across schema/runner/op/hand-authored YAML.
4. **Known unknowns:**
   - Wiki context may exceed 500k chars for a large domain. v1 raises `ContextTooLargeError`; v2 chunked/retrieval. Punt.
   - Sonnet 4.6 structured-output reliability at this prompt size hasn't been measured. The malformed-JSON path returns score=0.0 with reason. Observe failure rate in hand-test, tighten if needed.
   - Cache hit ratio: v1 caches only system prompt. Future: also `cache_control` the wiki_context block.

---

## Execution Handoff

Plan saved. Two options:
1. **Subagent-driven (recommended)** — same protocol as M49.
2. **Inline** — execute in this session.

Which?
