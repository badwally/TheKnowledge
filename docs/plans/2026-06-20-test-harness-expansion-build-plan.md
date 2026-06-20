# Test-Harness Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task (one implementer at a time — the knowledge working tree is shared). Steps use checkbox (`- [ ]`) syntax. Read `docs/MULTI-AGENT-BUILD-PLAYBOOK.md` before dispatching: the inert-in-production hunt list (Part A2) and the reviewer dispatch template (Part A1) bind every task here.

**Goal:** Close the known coverage seams left by the Production Committer + Multi-Agent Test Harness build (merged PR #35/#36) and add the one missing end-to-end capability — a real multi-agent deposit→commit→read round-trip through the production surfaces.

**Architecture:** Six independent, mostly-additive test tasks plus one small production observability change. Each leverages capabilities the prior build already shipped: the marker-tiered suite (`docs/TESTING.md`), the `tests/gateway/conftest.py` fixtures (`kb_root`, `make_canonical_source`, `auth_token`, `client`), the real-lock soak harness (`tests/integration/test_soak.py`), the MCP/CLI surface harness (`tests/e2e/`), the inert-invariant registry tests (`tests/integration/test_inert_invariants.py`), and the pre-merge gate (`src/gateway/scripts/gate.py`). No new heavyweight deps except `hypothesis` (lightweight, test-only — see P4 decision flag).

**Tech Stack:** Python, pytest (markers: `unit`/`integration`/`e2e`/`slow`, `--strict-markers`), `mcp.shared.memory.create_connected_server_and_client_session`, real git repos + fcntl locks, `hypothesis` (new, P4).

## Global Constraints

*(Every task's requirements implicitly include this section. Copied from the prior build's binding constraints — they have not changed.)*

- **`.venv/bin/python` and `.venv/bin/wiki` ONLY** — never system `python` (it lacks the gateway package).
- **Never `git add -A` / `git add -u`.** Stage explicit paths only. Guard `git branch --show-current` is the working branch before EVERY commit. Never stage watcher-owned `index.md` / `log.md` / `.knowledge/` runtime state / `.claude/scheduled_tasks.lock`.
- **No monkeypatching the core path under test.** Real fcntl locks, real git repos, real gate commits, real encoders. Redirect only `paths.*` dirs / `KNOWLEDGE_ROOT` to tmp (use the `kb_root` fixture).
- **Merge/transform/reversal tests use REALISTIC payloads** — full multi-section body, frontmatter aliases, inbound + body wikilinks, non-empty preamble — never claims-only stubs.
- **Adversarial tests with NAMED negative controls** for every concurrency / destructive / idempotency / merge path. The negative control must go RED on the broken condition.
- **Drive the REAL producer, never a fabricated fixture for the data the feature consumes** (hunt list Part A2 + hunt-question #7: a property test must not derive its expectation from the unit under test).
- **Scoped lints only** (`orphans` / `schema-drift` / `broken-wikilinks`) — never unscoped (it hangs ~1h28m).
- **Eval floor:** `retrieval_eval.evaluate("fts").recall_at(10) ≥ 0.90` (baseline 0.926). `merge_map_eval` no regressions. `embedding_eval.evaluate_all()` per the real I2 contract.
- **No `timeout`/`gtimeout` wrapping fast commands** (absent on darwin).
- **Every task runs an INDEPENDENT review** (reviewer ≠ author). A failing eval **or** review HALTS — no advance.
- **Branch + PR to `main`; the user merges.** Never reconcile locally on the shared tree.

## Verified interfaces (re-confirmed against source 2026-06-20 by adversarial plan review — these supersede any prior brief)

> **Lesson (playbook B2):** the first draft of this block copied signatures from the prior build's briefs and got six of them wrong. An adversarial review caught them against source. The signatures below are the CORRECTED, source-verified set. Still: if a call doesn't match when you build it, REPORT the mismatch — don't paper over it.

- **Committer module is `src/gateway/ops/committer.py`** (NOT `src/gateway/committer.py` — that path does not exist). Import: `from gateway.ops.committer import run_worker, drain_once, author_deposit, _is_gate_dispatched, _union_same_slug`.
- **`run_worker(*, once=False, queue=None, ...) -> None`** — it returns **None**. Do NOT assert on its return value; assert on post-drain state (disk / git / `queue.depth()`). Real callers: `tests/e2e/test_mcp_surface.py:173`, governance/soak flows.
- **`drain_once(...) -> DrainResult`** — `DrainResult(disposition, intent_id, detail, errors)` is built at every terminal path (`ops/committer.py:356,373,391`); the `run_worker` loop currently logs then DISCARDS each `DrainResult` (`ops/committer.py:451`). Dead-letter reason flows from `set_state(..., result={"error": str(exc)})` (`:370`).
- **`_union_same_slug(existing_content: str, new_body: str) -> str | None`** (`ops/committer.py:86`). Arg 2 is a **bullet-only `## Claims` body**, NOT a full page — the fn `.splitlines()` it and returns `None` on the first non-blank line that isn't `## Claims`/`- ` (`:117-128`). Unioning content whose net-new bullets are already present returns the existing page unchanged (idempotent no-op, `:130-132`).
- `deposit()` `src/gateway/ops/deposit.py:133`; payload fields `page_type` (entity/concept/source/synthesis), `title`, `body`, `aliases`, `domains`, `synthesizes`, `durable`, `volatile`. (`durable` truthy REQUIRES a real `[[sources/<id>]]` link — `deposit.py:121`. Leave `durable` unset for fixtures that don't seed a source.)
- `IntentQueue.submit()`; `.claim(*, lease_ttl=120.0, now=None) -> Claim | None` (`intent_queue.py:222`); `.depth()`; root attribute is `_root` (`:113`); monotonic fencing (`:266`).
- `CommitGate.commit(authored: AuthoredIntent, fencing_token: int) -> OperationResult` `commit_gate.py:298`. `AuthoredIntent.writes: dict[rel, str]` (already-rendered; `commit()` does NOT render).
- `DemandLedger.cluster() -> list[GapCluster]`; `.record_gap(text, *, caller=None) -> GapRecord`.
- **MCP — verified pattern (mirror `tests/e2e/test_mcp_surface.py`):** build server `mcp_server.mcp`; `build_read_tier_server()`; `tier.read_tier_tool_names()`; `from mcp.shared.memory import create_connected_server_and_client_session` (pass the FastMCP directly; yields a **single `ClientSession`**). **Async idiom: a SYNC test that wraps an `async def _inner()` in `asyncio.run(_inner())`** — there is NO `pytest-asyncio`/`anyio` dep, and `--strict-markers` makes `@pytest.mark.asyncio` a collection ERROR (`test_mcp_surface.py:64,72,112,164`). **Deposit call shape:** `await client.call_tool("wiki_deposit", {"payload": {...deposit fields...}, "identity": {"agent": "..."}})`; receipt = `json.loads(result.content[0].text)` (`test_mcp_surface.py:144-167`). Build tools are prefixed `wiki_`; `commit-worker`/`policy-edit` are `CLI_ONLY`.
- CLI: `cli.main(argv: list[str] | None) -> int`. Existing e2e: `tests/e2e/test_cli_surface.py` (uses a local `_git(repo, ...)` helper) and `tests/e2e/test_mcp_surface.py`.
- Eval: `retrieval_eval.evaluate(retriever="fts", *, goldens=None, k=10) -> EvalReport`; `EvalReport.recall_at(k) -> float`; `merge_map_eval(golden_path, *, root=None, ...) -> MergeMapResult(precision, recall, regressions)` (field shape not independently re-opened — verify at use site); `embedding_eval.evaluate_all(encoder=None) -> dict[ns, NamespaceGateReport(passed, fallback_active, fallback_falsifiable)]` (`embedding_eval.py:36-43,184`).
- **Lint registry: `src/gateway/ops/lint._CHECKS` is a `list[tuple[str, Callable]]`** (NOT a dict), with `KNOWN_CHECKS = {slug for slug, _ in _CHECKS}` already defined at `ops/lint.py:88`. `test_inert_invariants.py:166` already does `list(lint_op._CHECKS)`.
- Gate: `src/gateway/scripts/gate.py` — `run_gate(*, skip_suite=False) -> int`; `check_recall_floor`, `check_merge_map`, `check_embedding_namespaces`, `check_lint_counts`; `RECALL_FLOOR=0.90`; `LINT_BASELINES={orphans:758, schema-drift:191, broken-wikilinks:1}`; CLI flag `--skip-suite`.
- **`retrieve` read-after-commit is SAFE with no rebuild step:** `wiki retrieve` → `search_fts()` calls `refresh()` (mtime/size self-heal upsert) before querying (`search_index.py:358,369,267-293`). A freshly-committed page is retrievable, PROVIDED `KNOWLEDGE_ROOT` is set at retrieve-call time so refresh indexes the tmp repo.
- **Fixtures (`tests/gateway/conftest.py`) are dir-scoped to `tests/gateway/` ONLY** — there is no `tests/conftest.py` or `tests/e2e/conftest.py`, so `kb_root`/`make_canonical_source`/`auth_token`/`client` are **NOT visible in `tests/e2e/`**. E2E tests must define their OWN `KNOWLEDGE_ROOT`/git-repo fixture (mirror the local one in `tests/e2e/test_mcp_surface.py:41-51`).
- **pyproject extra is `[dev]`** (NOT `test`); `hypothesis` is absent (P4 adds it there).

---

### Task P1: E2E multi-agent deposit→commit→read round-trip

**Why first:** the flagship gap. The whole build exists to make async multi-agent deposit→commit→read safe, yet no test drives that full path through the real surfaces. Highest value-per-effort.

**Files:**
- Create: `tests/e2e/test_multiagent_flow.py` (marked `e2e`)

**Interfaces:**
- Consumes: `mcp_server.mcp`, `create_connected_server_and_client_session`, `run_worker` (from `gateway.ops.committer`), `cli.main` for `wiki retrieve`. Defines its OWN `KNOWLEDGE_ROOT`/git fixture (conftest is NOT visible in `tests/e2e/` — mirror `test_mcp_surface.py:41-51`).
- Produces: nothing downstream (leaf test task).

> **Pre-build read (do this first):** open `tests/e2e/test_mcp_surface.py` and reuse verbatim its (a) local `KNOWLEDGE_ROOT`/git-repo fixture, (b) `asyncio.run(_inner())` sync-wrapper idiom, (c) `call_tool("wiki_deposit", {"payload": {...}, "identity": {...}})` shape + `json.loads(result.content[0].text)` receipt parse, (d) post-drain commit assertions (`_git(repo, "log", ...)`, `Intent-Id:` trailer, page `exists()`). The skeleton below is illustrative — the surface details must match that file.

- [ ] **Step 1: Write the failing test — concurrent MCP deposits all commit and are readable.**

```python
import asyncio, json
import pytest
from mcp.shared.memory import create_connected_server_and_client_session
from gateway.ops.committer import run_worker
from gateway.mcp_server import mcp

pytestmark = pytest.mark.e2e

def test_n_agent_deposit_drain_read_round_trip(e2e_repo):  # e2e_repo = own fixture, sets KNOWLEDGE_ROOT to a real git tmp repo
    """N concurrent MCP deposits -> run_worker(once) drains -> every page is
    committed (disk + git Intent-Id) AND retrievable via the real read path."""
    n = 6
    titles = [f"Multiagent Entity {i}" for i in range(n)]

    async def _deposit_all() -> None:
        async with create_connected_server_and_client_session(mcp) as session:
            await asyncio.gather(*[
                session.call_tool("wiki_deposit", {
                    "payload": {
                        "page_type": "entity", "title": t,
                        "body": f"# Overview\n{t} is a test entity.\n\n# Detail\nMore about {t}.\n",
                        "aliases": [t.lower().replace(" ", "-")],
                        "domains": ["test-domain"],
                        # NOTE: durable unset — no [[sources/...]] needed (deposit.py:121).
                    },
                    "identity": {"agent": f"agent-{i}"},
                }) for i, t in enumerate(titles)
            ])

    asyncio.run(_deposit_all())

    run_worker(once=True)  # returns None — assert on state, not return value
    # Assert n pages committed under wiki/entities/ (disk) + each commit carries an
    # Intent-Id: trailer (git log), mirroring test_mcp_surface.py's commit checks.

    # Read through the REAL retrieve path (refresh() self-heals the index, no rebuild):
    rc = cli.main(["retrieve", "Multiagent Entity 3", "--domain", "test-domain"])  # capture stdout
    assert rc == 0
    # assert the captured retrieve output contains the slug for "Multiagent Entity 3"
```

- [ ] **Step 2: Run it; expect FAIL** until the fixture + on-disk/git assertions are filled in from `test_mcp_surface.py`. Confirm the deposits land in the SAME queue `run_worker` drains (both resolve `KNOWLEDGE_ROOT` set by the fixture).
- [ ] **Step 3: Add the negative control** — `test_deposit_without_drain_is_not_readable`: fire the deposits, do NOT call `run_worker`, assert the pages are NOT on disk and `wiki retrieve` does not surface them (proves the round-trip asserts the COMMIT, not just the enqueue — `run_worker` returning None means the disk/git assertion IS the proof of commit).
- [ ] **Step 4: Run the e2e tier green** — `.venv/bin/python -m pytest tests/e2e/ -q`.
- [ ] **Step 5: Commit** — stage only `tests/e2e/test_multiagent_flow.py`.

**Reviewer dispatch (opus — concurrency + the build's keystone path):** confirm the deposits go through the real MCP protocol with the correct `{"payload","identity"}` shape (not the Python fn), that `run_worker(once=True)` drains the SAME queue the MCP server wrote (KNOWLEDGE_ROOT resolved at call time), that the commit is proven by disk+git state (run_worker returns None), that the read assertion uses the real retrieve path, and that the negative control goes RED if drain is skipped.

---

### Task P2: Close T6 Step-1 to 32/32 positive lint coverage

**Files:**
- Modify: `tests/integration/test_inert_invariants.py`

**Interfaces:**
- Consumes: `ops/lint._CHECKS` — a **`list[tuple[str, Callable]]`** (NOT a dict); `KNOWN_CHECKS = {slug for slug, _ in _CHECKS}` already exists at `ops/lint.py:88`; `test_inert_invariants.py:166` already does `list(lint_op._CHECKS)`. The test file is in `tests/integration/` — confirm whether `kb_root` is available there or define a local equivalent (conftest is `tests/gateway/`-scoped; the existing inert-invariant tests use their own `kb_root` helper — reuse it).
- Produces: nothing downstream.

Current state: Step 1 asserts the *negative* control (clean repo → no flag) for all 32 checks, but a *positive* real-signal flag for only 5. This task drives a real on-disk condition for the remaining checks so every one is proven to fire (hunt #4: producer writes what the consumer reads).

- [ ] **Step 1: Enumerate the gap.** Run the existing parametrized test; list which check slugs currently have a positive-signal assertion vs negative-only. (The 5 covered, at `test_inert_invariants.py:204-320`: orphans, broken-wikilinks, retracted-citations, schema-drift, policy-provenance.)
- [ ] **Step 2: For each remaining check, write a positive-signal case** that constructs the REAL on-disk condition the check flags (drive the real producer — e.g. for `superseded-citations`, write a real superseded citation; for `link-rot`, a real dead link). Build a `slug -> positive-fixture` mapping and assert `KNOWN_CHECKS - set(mapping)` is empty — so a newly-registered check without a positive case FAILS, derived from the live registry (`KNOWN_CHECKS`), never a frozen list.
- [ ] **Step 3: Per check, add the negative control** (clean repo → that check does not flag) if not already present.
- [ ] **Step 4: Run** `.venv/bin/python -m pytest tests/integration/test_inert_invariants.py -v`; all green; confirm the "every check has a positive case" guard would RED if you delete one case.
- [ ] **Step 5: Commit** — stage only the test file (+ any backlog doc if a check is found genuinely un-triggerable, per the brief's surfaced-gap rule: backlog + xfail, never delete the assertion).

**Reviewer dispatch (opus — this is meta-gate coverage):** confirm each positive case drives a REAL producer (not a fabricated fixture for the data the check reads — hunt #6), and that the "every `_CHECKS` key has a positive case" guard is derived from the live registry, not a frozen list.

---

### Task P3: Concurrent same-slug race variant in the soak harness

**Files:**
- Modify: `tests/integration/test_soak.py`

**Interfaces:**
- Consumes: the existing soak harness (real fcntl locks, `IntentQueue`, `CommitGate`, `run_worker` from `gateway.ops.committer`, `_union_same_slug`), the `threading.Event` rendezvous pattern already in the file (`test_soak.py:245`), the S5 union test for the bullet-body payload shape (`test_soak.py:345,406-415`).
- Produces: nothing downstream.

The T3 S5 fix replaced the concurrent same-slug pair with deterministic ordering, so concurrent same-slug-RACE safety is no longer driven. Restore it as an explicit property. **Heed the S5 comment (`test_soak.py:225-227`):** a non-deterministic concurrent construction cannot guarantee a both-survive ordering — assert the disposition SET is valid, not a specific winner.

- [ ] **Step 1: Write the failing test** `test_concurrent_same_slug_all_terminal_no_torn_write`: N depositors (e.g. 5), ~2 sharing one slug, fire concurrently via the real queue + `run_worker`. Assert: every intent reaches a terminal state (committed or dead-lettered, none stranded); the shared-slug page on disk is well-formed (no torn write — parses as valid frontmatter + body); the outcome is one of {both unioned, one committed + one dead-lettered needs-manual-merge} — never silent loss.
- [ ] **Step 2: Run; expect FAIL** until assertions are tightened. Use the file's existing rendezvous helpers; do NOT add sleeps as the synchronization (deterministic barrier, per the flaky-test lesson in the playbook).
- [ ] **Step 3: Concrete negative control** — reuse the existing torn-write guard the file already documents at `test_soak.py:138` ("goes RED on a torn write / malformed YAML"): in a sibling guard test, deliberately truncate a written page mid-frontmatter and assert the frontmatter-parse check the main test relies on actually fails (proving the "well-formed" assertion has teeth). Do not leave the negative control hand-wavy.
- [ ] **Step 4: Run** `.venv/bin/python -m pytest tests/integration/test_soak.py -m slow -q`.
- [ ] **Step 5: Commit** — stage only `tests/integration/test_soak.py`.

**Reviewer dispatch (opus — concurrency):** confirm the race is real (two intents genuinely contend on one slug under the real lock, not serialized by the harness), the no-torn-write assertion parses the actual on-disk bytes, and "no silent loss" is asserted (every depositor's content is accounted for in some terminal disposition).

---

### Task P4: Real Hypothesis property tests (+ make TESTING.md honest)

**Decision flag (ratify before building):** this adds `hypothesis` to the test/dev dependency set. It is lightweight and test-only (not an ML/runtime dep), but it is a new dependency — confirm with the user before adding. If declined, this task is dropped and `docs/TESTING.md:47` is instead edited to remove the "(Hypothesis)" claim (turning T6's label honest the other way).

**Files:**
- Modify: `pyproject.toml` (add `hypothesis` to the **`[dev]`** extra — there is no `test` extra)
- Create: `tests/gateway/test_property_invariants.py` (marked `unit`)
- Modify: `docs/TESTING.md` (the T6 row already says "property-based (Hypothesis)" — this task makes that true)

**Interfaces:**
- Consumes: `_union_same_slug` (from `gateway.ops.committer`), the slug-canonicalization helper used by `author_deposit`, `IntentQueue` fencing-token monotonicity.
- Produces: nothing downstream.

- [ ] **Step 1: Add `hypothesis` to the `[dev]` extra in `pyproject.toml`** (`[project.optional-dependencies] dev = [...]`, `pyproject.toml:31`); install with `.venv/bin/python -m pip install -e '.[dev]'`; confirm `import hypothesis` works under `.venv/bin/python`.
- [ ] **Step 2: Write the failing property test** for `_union_same_slug` idempotence. **CRITICAL — arg shapes (the first draft of this plan got this wrong):** `_union_same_slug(existing_content, new_body)` — arg 1 is a FULL page, arg 2 is a **bullet-only `## Claims` body** (it `.splitlines()` arg 2 and returns `None` on any line that isn't `## Claims`/`- `). Passing a full page as arg 2 returns `None`. The idempotence property is: unioning an existing page with a `new_body` whose bullets are already present returns the existing page UNCHANGED (`ops/committer.py:130-132`).

```python
from hypothesis import given, strategies as st
from gateway.ops import committer

_bullet = st.text(min_size=1, max_size=40).filter(lambda s: "\n" not in s and not s.startswith(("#", "-")))

@given(bullets=st.lists(_bullet, min_size=1, max_size=8, unique=True))
def test_union_same_slug_idempotent_when_bullets_already_present(bullets):
    """Unioning an existing page with a body whose bullets it already has is a no-op."""
    existing = _render_claims_page(bullets)              # full page: frontmatter + ## Claims + bullets
    new_body = "## Claims\n" + "\n".join(f"- {b}" for b in bullets)  # bullet-only body (arg 2 shape)
    result = committer._union_same_slug(existing, new_body)
    assert result is not None                             # not the None reject path
    assert _claims(result) == set(bullets)                # no duplication, no loss
```

- [ ] **Step 3: Run; expect FAIL** until `_render_claims_page` (full page with `## Claims` + `- ` bullets, matching the shape `test_soak.py:406-415` uses) and `_claims` (parse the `- ` lines back to a set) are correct. Confirm against `ops/committer.py:86,117-132` before asserting.
- [ ] **Step 4: Add two more properties** — slug-canonicalization (same title → same slug; canonical form is a fixed point) and fencing-token monotonicity (`IntentQueue.claim` never returns a token ≤ a previously issued one across a sequence of claims). Each with a realistic generator.
- [ ] **Step 5: Run** `.venv/bin/python -m pytest tests/gateway/test_property_invariants.py -q`; confirm Hypothesis actually explores (no `@example`-only). Update `docs/TESTING.md` if the T6 row wording needs aligning (T6 stays parametrized; the new file is the Hypothesis tier).
- [ ] **Step 6: Commit** — stage `pyproject.toml`, the new test file, `docs/TESTING.md`.

**Reviewer dispatch (sonnet):** confirm Hypothesis genuinely generates (not a disguised parametrize), the generators produce realistic inputs (not empty/degenerate only), and each property asserts a real invariant of the production function (drives `_union_same_slug`/the real slug helper/the real `IntentQueue`, not a reimplementation).

---

### Task P5: Wire the pre-merge gate into an enforceable hook

**Files:**
- Create: `scripts/pre-push` (or document the git hook install) + a thin installer note
- Modify: `docs/MULTI-AGENT-BUILD-PLAYBOOK.md` (B6 — note the gate is now hook-enforceable), `CLAUDE.md` (install instruction)
- Test: `tests/test_gate_hook.py` (asserts the hook invokes `gateway.scripts.gate` and propagates its exit code)

**Interfaces:**
- Consumes: `python -m gateway.scripts.gate` (exit 0 = pass), its `--skip-suite` flag.
- Produces: nothing downstream.

The gate exists but nothing runs it automatically. Make the floor non-bypassable on push.

- [ ] **Step 1: Write the failing test** — a unit test that runs the hook script with a stubbed `gate` returning non-zero and asserts the hook exits non-zero (and conversely 0→0). Do NOT run the real full suite inside this unit test (stub the gate invocation).
- [ ] **Step 2: Write `scripts/pre-push`** — calls `.venv/bin/python -m gateway.scripts.gate` and exits with its code; document that the developer symlinks it into `.git/hooks/pre-push` (hooks are not version-controlled, so this is install-on-clone, like the existing PreCompact/SessionStart hooks). Offer a `--skip-suite` fast variant for local pushes with a clear comment that CI runs the full gate.
- [ ] **Step 3: Run** the hook test; green. Manually dry-run `scripts/pre-push` once against the current clean tree to confirm it passes end-to-end (this is the integration; the test covers the exit-code logic).
- [ ] **Step 4: Document** install in `CLAUDE.md` + a B6 note in the playbook.
- [ ] **Step 5: Commit** — stage the script, the test, and the two docs.

**Reviewer dispatch (sonnet):** confirm the hook propagates the gate's non-zero exit (a hook that always exits 0 is inert — hunt #1), the unit test does not silently shell out to the real suite, and the install instructions are accurate (hooks are not auto-installed by clone).

---

### Task P6: `commit-worker` trace mode (production observability)

**Files:**
- Modify: `src/gateway/ops/committer.py` (drain loop emits a per-intent disposition trace when verbose), `src/gateway/cli.py` (add `--verbose`/`--trace` to `commit-worker`)
- Test: the committer's existing test file (find it — likely `tests/gateway/test_committer*.py`) + `tests/e2e/test_cli_surface.py` (CLI flag e2e)

**Interfaces:**
- Consumes: `drain_once` (returns `DrainResult(disposition, intent_id, detail, errors)`, built at every terminal path `ops/committer.py:356,373,391`) / `run_worker`. The dead-letter reason is already on the result via `set_state(..., result={"error": str(exc)})` (`:370`) — read it, do NOT fabricate it (hunt #5).
- Produces: a structured per-intent trace line (stable keys: `intent_id`, `op`/`reversal_type`, `disposition`, `reason`) — usable by future tooling.

This is the one missing observability piece for the new autonomous actor: today, diagnosing a stuck/dead-lettering drain means hand-reading `.knowledge/intents/` JSONL. **Key implementation fact:** `drain_once` ALREADY returns a full `DrainResult`; the `run_worker` loop currently logs then **DISCARDS** it (`ops/committer.py:451`). The trace sink captures that already-computed value at that site — the disposition + reason data is present, the loop just drops it today. This is why "default-off = zero behavior change" holds (the only change is an emit on an existing value).

- [ ] **Step 1: Write the failing test** — drive `run_worker(once=True, verbose=True)` (or a passed sink) over a queue containing one good deposit + one deliberately-bad intent (e.g. unknown `reversal_type`); assert the trace records BOTH with their real dispositions and that the dead-letter trace carries the real `reason` read from the `DrainResult` (drive the real dead-letter path — hunt #5, do not fabricate the reason string).
- [ ] **Step 2: Run; expect FAIL** (flag/sink not implemented).
- [ ] **Step 3: Implement minimally** — add a `verbose`/sink param to `run_worker`; at the loop site that currently discards the `DrainResult` (`:451`), emit one structured line per intent from its already-computed disposition+reason. Do NOT alter `drain_once`'s logic. Default off (no behavior change when unset — confirm existing committer tests unchanged).
- [ ] **Step 4: Add the CLI flag** `wiki commit-worker --once --verbose` and an e2e assertion in `test_cli_surface.py` that the trace appears in output with the Intent-Id and disposition.
- [ ] **Step 5: Run** the committer unit tests + `tests/e2e/test_cli_surface.py` + the fast tier; all green.
- [ ] **Step 6: Commit** — stage `committer.py`, `cli.py`, the two test files.

**Reviewer dispatch (opus — touches the autonomous committer drain loop):** confirm the trace defaults OFF with zero behavior change (the drain logic is untouched when verbose is unset), the dead-letter `reason` is read from the real disposition (not a fabricated string), and no trace path swallows an exception that the non-verbose path would raise.

---

## Traceability (gate tests what ships)

| Seam (source) | Closed by | Gate row |
|---|---|---|
| No full multi-agent deposit→commit→read e2e | P1 | e2e tier |
| T6 Step-1 positive coverage 5/32 (ledger Minor) | P2 | integration tier |
| T3 concurrent same-slug race no longer driven (ledger Minor) | P3 | slow tier |
| TESTING.md "Hypothesis" claim vs parametrized impl (doc drift) | P4 | unit tier |
| Gate exists but nothing runs it automatically | P5 | (hook/CI) |
| No drain-loop observability for the autonomous committer | P6 | unit + e2e |

Items deliberately NOT in scope (remain triggered-backlog): the committer launchd/scheduler daemon, the demand-cluster scheduled trigger, same-slug union body-parity, reverse-merge producer op, demand-ledger DoS bound. Each has a revival trigger in `docs/backlog/` — do not pull them in without the trigger firing.

## Exit gate (run before the PR)

Run `.venv/bin/python -m gateway.scripts.gate` on a clean checkout. Required: full suite green (capture the pre-P1 baseline count fresh at build start — do NOT hardcode; it was ~2491 at plan time but the watcher/other work may move it — then assert new = baseline + P1–P6 additions), recall@10 ≥ 0.90, merge-map 0 regressions, embedding I2 OK, scoped lints at baseline (758/191/1). Whole-branch opus review READY + (because P6 touches the privileged committer) a security spot-check that the trace mode exposes no secret/payload content and changes no privilege boundary. A failing eval OR review HALTS.

## Self-review notes

- **Spec coverage:** all six advised items (P1–P6) map to the capabilities review; the two doc drifts are absorbed (P4 resolves the Hypothesis label; TESTING.md:55 path was verified correct, no action).
- **Dependency flag:** P4 adds `hypothesis` — ratify before building; fallback is a doc-only fix.
- **Production-touch tasks:** only P6 changes production code; it is additive (default-off trace) and gets opus + a security spot-check.
- **Ordering:** P1 first (highest value, flushes any e2e-fixture friction early); P2/P3 close logged Minors; P4/P5/P6 are net-new and independent — can run in any order after P1.
