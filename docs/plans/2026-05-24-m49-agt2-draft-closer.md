# M49 — AGT-2 Draft Closer + TOK-1 Anthropic API Client Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a daily-running batch draft closer that auto-finalizes deterministic cases and uses an LLM (via a new Anthropic API client with prompt caching) to suggest citations on the harder cases — auto-applying unambiguous LLM suggestions in Aggressive mode.

**Architecture:** Two coupled components: (1) `AnthropicAPIClient` parallel to the existing `ClaudeCLIClient`, using the `anthropic` Python SDK with `cache_control` markers to cut per-call cost on repeated prompt prefixes; (2) `wiki finalize-batch [--suggest] [--execute]` op that walks `lint --scope stale-drafts`, auto-finalizes drafts with `unresolved_claims == 0`, and (when `--suggest`) calls a new `gateway.ops.cite_suggest` module that uses the API client to propose `wiki cite` invocations per unresolved claim. Aggressive mode auto-applies any LLM suggestion that emits exactly one source per claim line AND passes evidence-quote verification (the proposed source's raw body must literally contain the LLM-quoted evidence).

**Tech Stack:** Python 3.12, `anthropic` SDK (new dep), existing `gateway.lint.stale_drafts`, existing `gateway.ops.{cite, finalize}`, existing `gateway.scheduler` (K4), `pytest`.

---

## Background

**Why bundled.** AGT-2 alone was sized S, but the LLM-driven `wiki cite --suggest` half is the cost-sensitive path. TOK-1 (separate API key for caching) was decided on 2026-05-24 and is the unlock. Landing both together means `--suggest` ships once with caching enabled rather than landing twice.

**Current draft inventory.** 587 drafts total in the wiki; 223 stale per `lint --scope stale-drafts`. Approximately half of stale drafts are entity pages with `unresolved_claims: 0` (deterministic Cat A), the rest are concept/synthesis pages with `unresolved_claims: ?` (need validator re-evaluation, and where the LLM suggest path is most valuable).

**Mode = Aggressive.** Decided 2026-05-24. The scheduled run auto-finalizes Cat A AND any draft where `--suggest` produces an unambiguous single-source-per-claim-line result with verified evidence quotes. Multi-candidate or unverifiable cases escalate to the run report — they are listed with pre-computed `wiki cite` invocation strings the user can apply manually after review.

**Safety nets.**
1. Git is the rollback path — every batch run is a single commit.
2. Validator catches any case where a finalize would leave unresolved claims (the cite op only adds tokens; the finalize op re-runs the strict validator).
3. Evidence-quote verification means a wrong cite from the LLM requires the LLM to both hallucinate a source AND hallucinate a quote that happens to be substring-present in that source's raw body — vanishingly unlikely.
4. Per-run report at `.knowledge/finalize-batch/<timestamp>.md` is the human audit trail.

---

## File Structure

**Create:**
- `src/gateway/llm/api_client.py` — `AnthropicAPIClient` (TOK-1).
- `src/gateway/ops/cite_suggest.py` — LLM-driven citation suggestion (pure logic).
- `src/gateway/ops/finalize_batch.py` — batch driver (uses `cite_suggest` when `--suggest`).
- `tests/gateway/test_anthropic_client.py` — TOK-1 client tests, mocked SDK.
- `tests/gateway/test_cite_suggest.py` — cite-suggest logic + prompt assembly.
- `tests/gateway/test_finalize_batch.py` — batch driver, dry-run vs execute, Aggressive integration.
- `docs/milestones/M49.md` — milestone delivery doc.

**Modify:**
- `src/gateway/llm/config.py` — add `cite_suggest` to `Stage` literal, register Sonnet 4.6 default.
- `src/gateway/llm/__init__.py` — export `AnthropicAPIClient`.
- `src/gateway/cli.py` — add `finalize-batch` subcommand; extend `cite` subcommand with `--suggest`.
- `src/gateway/mcp_server.py` — add `wiki_finalize_batch` MCP tool per K2 parity discipline.
- `WIKI.md` — append `finalize-batch` and `cite --suggest` to Gateway Operations table.
- `BUILD.md` — append M49 row to § 10.
- `pyproject.toml` — add `anthropic` to dependencies.
- `.knowledge/schedule.yaml` — add daily `finalize-batch --suggest --execute` job (via `wiki schedule add`).

**Test count target:** 901 → ≥ 935 (≈ 34 new tests across the three new test files).

---

## Open Decisions (resolved before plan write)

1. **Mode aggressiveness** — Aggressive (auto-apply unambiguous LLM cites).
2. **Surface** — Single op `wiki finalize-batch [--suggest] [--execute]`. No separate `wiki agent` namespace. Per `feature_general_purpose_inherits_surface_anchors` discipline, we don't introduce an "agents" directory just to host one driver; if AGT-1 (inbox triage) wants to share infra later, we extract then.
3. **Selection between Claude CLI and API client** — per-call-site. `cite_suggest` instantiates `AnthropicAPIClient` directly; filter/plan/VLM stay on `ClaudeCLIClient`. No global flag.
4. **Model for `cite_suggest`** — Sonnet 4.6. Attribution-matching is well within Sonnet's reasoning band, and the cost delta vs Opus is the entire reason for using the API client.
5. **Evidence-quote verification** — required. LLM emits `{line, source_id, evidence_quote}`; verifier checks the raw source body contains the quote as a substring (whitespace-normalized). Unverified suggestions never auto-apply; they appear in the report only.
6. **Report location** — `.knowledge/finalize-batch/<UTC-timestamp>.md`. Matches the lint-report convention (`.knowledge/lint/...`).

---

# Phase A — TOK-1: AnthropicAPIClient

### Task A1: Add the `anthropic` SDK dependency

**Files:**
- Modify: `pyproject.toml`

- [ ] **Step 1: Inspect current dependencies**

Run: `grep -n "dependencies\|anthropic" pyproject.toml`
Expected: dependencies list visible; `anthropic` not present.

- [ ] **Step 2: Add `anthropic>=0.40` to the dependencies array**

Edit `pyproject.toml`, locate the `dependencies = [...]` block, add a line:
```
    "anthropic>=0.40",
```

- [ ] **Step 3: Install into the project venv**

Run: `.venv/bin/pip install "anthropic>=0.40"`
Expected: installs cleanly. Note the resolved version.

- [ ] **Step 4: Verify import**

Run: `.venv/bin/python -c "import anthropic; print(anthropic.__version__)"`
Expected: version string prints; no errors.

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml
git commit -m "deps(m49): add anthropic SDK for TOK-1 API client"
```

---

### Task A2: Write failing test for `AnthropicAPIClient.call_with_usage()`

**Files:**
- Create: `tests/gateway/test_anthropic_client.py`

- [ ] **Step 1: Create the test file with a single failing test**

```python
"""Tests for AnthropicAPIClient (TOK-1, M49).

Mocks the `anthropic.Anthropic` client so tests are hermetic. Real-network
verification is via the hand-test in docs/milestones/M49.md.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from gateway.llm.api_client import AnthropicAPIClient
from gateway.llm import LLMError


def _mock_message(text: str = "ok", input_tokens: int = 10, output_tokens: int = 2,
                  cache_read: int = 0, cache_creation: int = 0,
                  model: str = "claude-sonnet-4-6") -> MagicMock:
    """Build a mock anthropic.types.Message matching the SDK shape."""
    msg = MagicMock()
    msg.content = [MagicMock(type="text", text=text)]
    msg.usage = MagicMock(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_read_input_tokens=cache_read,
        cache_creation_input_tokens=cache_creation,
    )
    msg.model = model
    msg.stop_reason = "end_turn"
    return msg


def test_call_with_usage_returns_text_and_telemetry(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message(
            text="hello", input_tokens=42, output_tokens=7
        )

        client = AnthropicAPIClient()
        result = client.call_with_usage(
            user_prompt="say hello",
            system_prompt="be brief",
            model="claude-sonnet-4-6",
        )

    assert result.text == "hello"
    assert result.input_tokens == 42
    assert result.output_tokens == 7
    assert result.model == "claude-sonnet-4-6"
```

- [ ] **Step 2: Run the test to confirm failure**

Run: `.venv/bin/pytest tests/gateway/test_anthropic_client.py::test_call_with_usage_returns_text_and_telemetry -v`
Expected: ImportError or ModuleNotFoundError on `gateway.llm.api_client`.

---

### Task A3: Implement `AnthropicAPIClient` (minimum to pass A2)

**Files:**
- Create: `src/gateway/llm/api_client.py`

- [ ] **Step 1: Write the client module**

```python
"""TOK-1 (M49): Anthropic SDK client for prompt-caching-eligible call sites.

Parallel to ``ClaudeCLIClient`` (which uses ``claude -p`` subprocess against
the user's Max-plan OAuth). This client uses the Anthropic Python SDK
against a separate API key (``ANTHROPIC_API_KEY_RESEARCH``) with a
console-side spend cap. The reason for parallel rather than overloading
``ClaudeCLIClient`` is that the two billing/auth paths are mutually
exclusive — Max OAuth refuses the API key, and the API key path enables
caching that ``claude -p`` does not currently surface as a controllable
lever.

Selection per call site:
- Filter / plan / VLM / research: ``ClaudeCLIClient`` (Max OAuth, no cache)
- ``wiki cite --suggest``: ``AnthropicAPIClient`` (API key, cached)
"""

from __future__ import annotations

import os
import threading
import time
from typing import Callable

import anthropic

from gateway.llm.telemetry import CallResult


class APIKeyMissingError(RuntimeError):
    """Raised when ``ANTHROPIC_API_KEY_RESEARCH`` is not set."""


class AnthropicAPIClient:
    """Anthropic SDK client with prompt caching on the system prompt.

    Reads ``ANTHROPIC_API_KEY_RESEARCH`` once at construction time. Uses
    the same min-interval throttle pattern as ``ClaudeCLIClient`` so
    parallel callers across both clients share rate-limit headroom.
    """

    _throttle_lock = threading.Lock()
    _last_call_monotonic: float = float("-inf")

    def __init__(
        self,
        *,
        timeout_s: float = 120.0,
        max_retries: int = 3,
        retry_base_s: float = 5.0,
        min_interval_s: float = 0.0,
        sleep: Callable[[float], None] = time.sleep,
        monotonic: Callable[[], float] = time.monotonic,
    ):
        api_key = os.environ.get("ANTHROPIC_API_KEY_RESEARCH", "")
        if not api_key:
            raise APIKeyMissingError(
                "ANTHROPIC_API_KEY_RESEARCH not set; configure a separate API "
                "key for research subprocesses (see memory: "
                "separate_api_key_for_caching)"
            )
        self._client = anthropic.Anthropic(api_key=api_key, timeout=timeout_s)
        self._timeout = timeout_s
        self._max_retries = max_retries
        self._retry_base_s = retry_base_s
        self._min_interval_s = max(0.0, min_interval_s)
        self._sleep = sleep
        self._monotonic = monotonic

    def _throttle(self) -> None:
        if self._min_interval_s <= 0:
            return
        with AnthropicAPIClient._throttle_lock:
            now = self._monotonic()
            elapsed = now - AnthropicAPIClient._last_call_monotonic
            wait = self._min_interval_s - elapsed
            if wait > 0:
                self._sleep(wait)
            AnthropicAPIClient._last_call_monotonic = self._monotonic()

    def call_with_usage(
        self,
        *,
        user_prompt: str,
        system_prompt: str | None = None,
        model: str,
        max_tokens: int = 4096,
        cache_system_prompt: bool = True,
    ) -> CallResult:
        """Call the API and return a ``CallResult``.

        When ``cache_system_prompt`` is True (default) and a system prompt
        is provided, applies ``cache_control={"type": "ephemeral"}`` to
        the system prompt block. Subsequent calls within the 5-minute
        cache TTL with the same system prompt re-use the cached prefix.
        """
        system_blocks: list[dict] | str | None = None
        if system_prompt is not None:
            if cache_system_prompt:
                system_blocks = [
                    {
                        "type": "text",
                        "text": system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    }
                ]
            else:
                system_blocks = system_prompt

        last_err: Exception | None = None
        for attempt in range(self._max_retries + 1):
            self._throttle()
            try:
                kwargs = {
                    "model": model,
                    "max_tokens": max_tokens,
                    "messages": [{"role": "user", "content": user_prompt}],
                }
                if system_blocks is not None:
                    kwargs["system"] = system_blocks
                msg = self._client.messages.create(**kwargs)
                return self._to_result(msg)
            except (anthropic.RateLimitError, anthropic.APIStatusError) as e:
                last_err = e
                if attempt < self._max_retries:
                    self._sleep(self._retry_base_s * (2 ** attempt))
                    continue
                break

        from gateway.llm import LLMError
        raise LLMError(
            f"AnthropicAPIClient failed after {self._max_retries + 1} attempts: {last_err}"
        )

    @staticmethod
    def _to_result(msg) -> CallResult:
        # msg.content is a list of content blocks; collect text-typed ones.
        text_parts: list[str] = []
        for block in msg.content:
            if getattr(block, "type", None) == "text":
                text_parts.append(getattr(block, "text", ""))
        text = "".join(text_parts)

        usage = msg.usage
        return CallResult(
            text=text,
            input_tokens=int(getattr(usage, "input_tokens", 0) or 0),
            output_tokens=int(getattr(usage, "output_tokens", 0) or 0),
            cache_read_tokens=int(getattr(usage, "cache_read_input_tokens", 0) or 0),
            cache_creation_tokens=int(getattr(usage, "cache_creation_input_tokens", 0) or 0),
            model=str(getattr(msg, "model", "unknown") or "unknown"),
            stop_reason=str(getattr(msg, "stop_reason", "unknown") or "unknown"),
            duration_ms=0,  # SDK does not surface this; left at 0
            total_cost_usd=0.0,  # caller can derive from tokens if needed
        )
```

- [ ] **Step 2: Run the A2 test to confirm it now passes**

Run: `.venv/bin/pytest tests/gateway/test_anthropic_client.py::test_call_with_usage_returns_text_and_telemetry -v`
Expected: PASS.

---

### Task A4: Test that the env-var is required

**Files:**
- Modify: `tests/gateway/test_anthropic_client.py`

- [ ] **Step 1: Add the failing test**

```python
def test_raises_when_key_missing(monkeypatch):
    from gateway.llm.api_client import APIKeyMissingError

    monkeypatch.delenv("ANTHROPIC_API_KEY_RESEARCH", raising=False)
    with pytest.raises(APIKeyMissingError):
        AnthropicAPIClient()
```

- [ ] **Step 2: Run + verify it passes (implementation already covers this in A3)**

Run: `.venv/bin/pytest tests/gateway/test_anthropic_client.py -v`
Expected: both tests PASS.

---

### Task A5: Test cache_control marker is sent on the system prompt

**Files:**
- Modify: `tests/gateway/test_anthropic_client.py`

- [ ] **Step 1: Add the test**

```python
def test_cache_control_applied_to_system_prompt(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message()

        client = AnthropicAPIClient()
        client.call_with_usage(
            user_prompt="q",
            system_prompt="long stable prefix",
            model="claude-sonnet-4-6",
        )

        kwargs = mock_client.messages.create.call_args.kwargs
        assert kwargs["system"] == [
            {
                "type": "text",
                "text": "long stable prefix",
                "cache_control": {"type": "ephemeral"},
            }
        ]


def test_cache_control_can_be_disabled(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message()

        client = AnthropicAPIClient()
        client.call_with_usage(
            user_prompt="q",
            system_prompt="prefix",
            model="claude-sonnet-4-6",
            cache_system_prompt=False,
        )

        kwargs = mock_client.messages.create.call_args.kwargs
        assert kwargs["system"] == "prefix"  # plain string, no cache_control
```

- [ ] **Step 2: Run**

Run: `.venv/bin/pytest tests/gateway/test_anthropic_client.py -v`
Expected: 4 tests PASS.

---

### Task A6: Test cache_read tokens roll through telemetry

**Files:**
- Modify: `tests/gateway/test_anthropic_client.py`

- [ ] **Step 1: Add the test**

```python
def test_cache_read_tokens_surface_in_call_result(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message(
            input_tokens=5,
            output_tokens=3,
            cache_read=2000,
            cache_creation=0,
        )

        client = AnthropicAPIClient()
        result = client.call_with_usage(
            user_prompt="q",
            system_prompt="long prefix",
            model="claude-sonnet-4-6",
        )

    assert result.cache_read_tokens == 2000
    assert result.input_tokens == 5
```

- [ ] **Step 2: Run**

Run: `.venv/bin/pytest tests/gateway/test_anthropic_client.py -v`
Expected: 5 tests PASS.

---

### Task A7: Add `cite_suggest` stage to model config

**Files:**
- Modify: `src/gateway/llm/config.py`
- Modify: `tests/gateway/test_llm_client.py` (verify exists; if not, create a focused config test in a new file)

- [ ] **Step 1: Add `cite_suggest` to `Stage` literal and the default-model dispatch**

Edit `src/gateway/llm/config.py`:
- Add `"cite_suggest"` to the `Stage = Literal[...]` enum.
- Add `DEFAULT_CITE_SUGGEST_MODEL = "claude-sonnet-4-6"` constant.
- In `model_for`, add: `if stage == "cite_suggest": return DEFAULT_CITE_SUGGEST_MODEL`.

- [ ] **Step 2: Add a unit test for `model_for("cite_suggest")`**

Create `tests/gateway/test_llm_config.py` (or extend an existing config test if one exists — grep first):
```python
from gateway.llm.config import model_for


def test_cite_suggest_stage_returns_sonnet():
    assert model_for("cite_suggest") == "claude-sonnet-4-6"
```

- [ ] **Step 3: Run**

Run: `.venv/bin/pytest tests/gateway/test_llm_config.py -v`
Expected: PASS.

---

### Task A8: Export `AnthropicAPIClient` from `gateway.llm`

**Files:**
- Modify: `src/gateway/llm/__init__.py`

- [ ] **Step 1: Add export**

Edit `src/gateway/llm/__init__.py`:
```python
from gateway.llm.api_client import AnthropicAPIClient, APIKeyMissingError
```
and add both names to `__all__`.

- [ ] **Step 2: Verify import path**

Run: `.venv/bin/python -c "from gateway.llm import AnthropicAPIClient, APIKeyMissingError; print('ok')"`
Expected: `ok`.

- [ ] **Step 3: Commit Phase A**

```bash
git add src/gateway/llm/ tests/gateway/test_anthropic_client.py tests/gateway/test_llm_config.py
git commit -m "feat(m49): add AnthropicAPIClient with prompt caching (TOK-1)"
```

---

# Phase B — `wiki finalize-batch` deterministic engine

### Task B1: Write failing test for the dry-run summary

**Files:**
- Create: `tests/gateway/test_finalize_batch.py`

- [ ] **Step 1: Create the test file**

```python
"""Tests for `wiki finalize-batch` (M49, AGT-2).

Three layers:
- Deterministic Cat A: drafts where stale-drafts metadata says
  `unresolved_claims == 0` → auto-finalize.
- Suggest path (Phase C/D): uses AnthropicAPIClient — mocked here.
- Aggressive integration: auto-applies single-source-per-line LLM cites
  with verified evidence quotes.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.finalize_batch import finalize_batch


def _write_draft_entity(kb_root: Path, slug: str, *, age_days: int = 12,
                        unresolved: int = 0, body: str = "") -> Path:
    page = kb_root / "wiki" / "entities" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    started = (datetime.now(timezone.utc) - timedelta(days=age_days)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    front = {
        "type": "entity",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "entity_kind": "organization",
        "domains": ["test-domain"],
        "draft": True,
        "draft_started_at": started,
        "draft_unresolved_claims": unresolved,
    }
    page.write_text(fm.serialize(front, body or f"# {slug}\n\nDescription.\n"))
    return page


def test_dry_run_lists_cat_a_drafts_but_does_not_finalize(kb_root):
    p = _write_draft_entity(kb_root, "acme-corp", age_days=12, unresolved=0)

    result = finalize_batch(execute=False, suggest=False)

    assert result.success
    # Dry-run reports it as a candidate, but the file is still a draft.
    front_after, _ = fm.parse(p.read_text())
    assert front_after.get("draft") is True
    assert "acme-corp" in result.summary or any(
        "acme-corp" in s for s in (result.notes or [])
    )
```

- [ ] **Step 2: Run to confirm import failure**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py -v`
Expected: ImportError on `gateway.ops.finalize_batch`.

---

### Task B2: Implement minimal `finalize_batch` (dry-run only)

**Files:**
- Create: `src/gateway/ops/finalize_batch.py`

- [ ] **Step 1: Skeleton with dry-run only**

```python
"""`wiki finalize-batch` — daily batch closer for stale drafts (M49, AGT-2).

Reads `lint --scope stale-drafts`. For each finding:
  Cat A: `unresolved_claims == 0` → finalize (when `--execute`).
  Cat B: validator re-run shows 0 unresolved claims → finalize.
  Other: skip in deterministic mode; in `--suggest` mode, call
         `gateway.ops.cite_suggest` to propose cites; in
         `--suggest --execute` (Aggressive), auto-apply unambiguous +
         verified suggestions and then finalize.

Defaults to dry-run. Pass `--execute` to actually finalize / apply cites.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from gateway import log, paths
from gateway.core import OperationResult
from gateway.lint import stale_drafts as stale_drafts_check
from gateway.ops.finalize import finalize as finalize_one


@dataclass
class _Outcome:
    page: str
    category: str  # "cat_a" | "cat_b" | "suggest_applied" | "escalated"
    finalized: bool
    note: str = ""
    suggested_cites: list[str] = field(default_factory=list)


def finalize_batch(
    *,
    domain: str | None = None,
    limit: int | None = None,
    execute: bool = False,
    suggest: bool = False,
) -> OperationResult:
    findings = stale_drafts_check.run()

    outcomes: list[_Outcome] = []
    for finding in findings:
        if limit is not None and len(outcomes) >= limit:
            break

        rel = finding.path
        meta = finding.metadata or {}
        unresolved = meta.get("unresolved_claims")
        # Cat A: deterministic finalize candidate.
        if unresolved == 0:
            outcomes.append(_Outcome(page=rel, category="cat_a", finalized=False))
            continue
        # Other categories live in Phase C/D.
        outcomes.append(
            _Outcome(page=rel, category="escalated", finalized=False,
                     note=f"unresolved_claims={unresolved!r}")
        )

    notes = [f"{o.category}: {o.page}" for o in outcomes]
    return OperationResult(
        success=True,
        summary=(f"finalize-batch dry-run: {len(outcomes)} candidates "
                 f"(execute=False, suggest={suggest})"),
        notes=notes,
    )
```

If `OperationResult` doesn't have a `notes` field, check `gateway.core`:

Run: `grep -n "class OperationResult\|notes" src/gateway/core.py | head -10`

If `notes` is absent, swap to a structured field that does exist (e.g., extend `summary` with the full list, or add a dedicated dataclass `BatchReport` returned alongside).

- [ ] **Step 2: Run the B1 test**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py::test_dry_run_lists_cat_a_drafts_but_does_not_finalize -v`
Expected: PASS.

---

### Task B3: Test `--execute` actually finalizes Cat A

**Files:**
- Modify: `tests/gateway/test_finalize_batch.py`

- [ ] **Step 1: Add test**

```python
def test_execute_finalizes_cat_a(kb_root):
    p = _write_draft_entity(kb_root, "beta-corp", age_days=12, unresolved=0)

    result = finalize_batch(execute=True, suggest=False)

    assert result.success
    front_after, _ = fm.parse(p.read_text())
    assert "draft" not in front_after
    assert "finalized_at" in front_after
```

- [ ] **Step 2: Run, expect FAIL**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py::test_execute_finalizes_cat_a -v`
Expected: FAIL — the implementation still doesn't act on Cat A.

- [ ] **Step 3: Implement the execute path**

In `finalize_batch`, replace the Cat A branch:

```python
if unresolved == 0:
    if execute:
        page_abs = paths.knowledge_root() / rel
        sub = finalize_one(page_abs)
        if sub.success:
            outcomes.append(_Outcome(page=rel, category="cat_a", finalized=True))
        else:
            outcomes.append(_Outcome(
                page=rel, category="escalated", finalized=False,
                note="finalize failed: " + "; ".join(sub.errors or []),
            ))
    else:
        outcomes.append(_Outcome(page=rel, category="cat_a", finalized=False,
                                 note="dry-run"))
    continue
```

- [ ] **Step 4: Re-run**

Expected: B1 and B3 PASS.

---

### Task B4: Test `--domain` filter

**Files:**
- Modify: `tests/gateway/test_finalize_batch.py`
- Modify: `src/gateway/ops/finalize_batch.py`

- [ ] **Step 1: Add test**

```python
def test_domain_filter_skips_other_domains(kb_root):
    a = _write_draft_entity(kb_root, "alpha-co", age_days=12, unresolved=0)
    # Build a second entity in another domain.
    b_path = kb_root / "wiki" / "entities" / "other-co.md"
    started = (datetime.now(timezone.utc) - timedelta(days=12)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    b_path.write_text(fm.serialize(
        {
            "type": "entity",
            "slug": "other-co",
            "title": "Other Co",
            "entity_kind": "organization",
            "domains": ["other-domain"],
            "draft": True,
            "draft_started_at": started,
            "draft_unresolved_claims": 0,
        },
        "# Other\n",
    ))

    result = finalize_batch(domain="test-domain", execute=True, suggest=False)

    a_front, _ = fm.parse(a.read_text())
    b_front, _ = fm.parse(b_path.read_text())
    assert "draft" not in a_front  # finalized
    assert b_front.get("draft") is True  # untouched
```

- [ ] **Step 2: Run, expect FAIL**

- [ ] **Step 3: Implement domain filter**

In `finalize_batch`, before the Cat A branch, add:

```python
if domain is not None:
    # Load page frontmatter to check domain membership.
    page_abs = paths.knowledge_root() / rel
    try:
        text = page_abs.read_text()
        front, _ = __import__("gateway.frontmatter", fromlist=["parse"]).parse(text)
    except Exception:
        continue
    page_domains = front.get("domains") or []
    if domain not in page_domains:
        continue
```

Or, more cleanly, import `from gateway import frontmatter as fm` at the top of the module.

- [ ] **Step 4: Re-run all tests**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py -v`
Expected: 3 PASS.

---

### Task B5: Wire `finalize-batch` into the CLI

**Files:**
- Modify: `src/gateway/cli.py`

- [ ] **Step 1: Add to SUBCOMMANDS dict (~line 29 area)**

```python
"finalize-batch": "Batch-finalize stale drafts (dry-run by default; --execute to apply; --suggest enables LLM cite-suggest for Cat B)",
```

- [ ] **Step 2: Add to canonical list (~line 67 area)**

In the ordered subcommand list, add `"finalize-batch"` adjacent to `"finalize"`.

- [ ] **Step 3: Add argparse subparser**

In the section near `p_finalize = subparsers.add_parser("finalize", ...)`:

```python
p_finalize_batch = subparsers.add_parser(
    "finalize-batch", help=SUBCOMMANDS["finalize-batch"]
)
p_finalize_batch.add_argument("--domain", default=None)
p_finalize_batch.add_argument("--limit", type=int, default=None)
p_finalize_batch.add_argument("--execute", action="store_true",
                              help="Actually finalize (default is dry-run).")
p_finalize_batch.add_argument("--suggest", action="store_true",
                              help="Run LLM cite-suggest on Cat B drafts.")
```

- [ ] **Step 4: Add dispatch (~line 695 area)**

```python
if ns.subcommand == "finalize-batch":
    from gateway.ops.finalize_batch import finalize_batch
    return finalize_batch(
        domain=ns.domain,
        limit=ns.limit,
        execute=ns.execute,
        suggest=ns.suggest,
    )
```

- [ ] **Step 5: Sanity check the CLI surface**

Run: `.venv/bin/wiki finalize-batch --help`
Expected: help text prints; `--execute`, `--suggest`, `--domain`, `--limit` flags visible.

Run: `.venv/bin/wiki finalize-batch --domain test-domain` (dry-run)
Expected: prints a summary; no draft files change.

---

### Task B6: Commit Phase B

- [ ] **Step 1: Verify all Phase B tests pass**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py tests/gateway/test_anthropic_client.py tests/gateway/test_llm_config.py -v`
Expected: ALL PASS.

- [ ] **Step 2: Run the full suite, check no regression**

Run: `.venv/bin/pytest tests/ -q`
Expected: All pre-existing tests still pass. New count ≈ 901 + (new tests so far).

- [ ] **Step 3: Commit**

```bash
git add src/gateway/ops/finalize_batch.py src/gateway/cli.py tests/gateway/test_finalize_batch.py
git commit -m "feat(m49): wiki finalize-batch deterministic engine (Cat A)"
```

---

# Phase C — `gateway.ops.cite_suggest` LLM-driven module

### Task C1: Define the suggestion data shape and write failing test

**Files:**
- Create: `tests/gateway/test_cite_suggest.py`

- [ ] **Step 1: Write the first test using a stubbed LLM client**

```python
"""Tests for cite_suggest (M49 Phase C).

Mocks AnthropicAPIClient so tests are hermetic. Real-network verification
is done in the M49 hand-test (see docs/milestones/M49.md).
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

from gateway import frontmatter as fm
from gateway.llm.telemetry import CallResult
from gateway.ops.cite_suggest import (
    CiteSuggestion,
    suggest_cites,
)


def _write_concept_draft_with_one_claim(kb_root: Path, slug: str,
                                        source_ids: list[str]) -> Path:
    page = kb_root / "wiki" / "concepts" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "domains": ["test-domain"],
        "draft": True,
        "draft_started_at": "2026-05-12T00:00:00Z",
        "sources": source_ids,
    }
    body = "# title\n\n## Summary\n\nThe unique claim X requires citation.\n"
    page.write_text(fm.serialize(front, body))
    return page


def _write_raw_source(kb_root: Path, source_id: str, body_text: str,
                      source_type: str = "web") -> Path:
    raw = kb_root / "raw" / source_type / f"{source_id}.md"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw_front = {
        "id": source_id,
        "type": source_type,
        "title": f"Source {source_id}",
        "url": f"https://example.com/{source_id}",
        "domains": ["test-domain"],
    }
    raw.write_text(fm.serialize(raw_front, body_text))

    wiki_src = kb_root / "wiki" / "sources" / f"{source_id}.md"
    wiki_src.parent.mkdir(parents=True, exist_ok=True)
    wiki_src.write_text(fm.serialize(
        {
            "type": "source",
            "source_id": source_id,
            "source_type": source_type,
            "title": f"Source {source_id}",
            "domains": ["test-domain"],
        },
        f"# {source_id}\n",
    ))
    return raw


def test_suggest_returns_unambiguous_when_single_source_quotes_claim(kb_root):
    source_id = "web-2026-01-01-aaa"
    _write_raw_source(kb_root, source_id, "Claim X is documented here.\n")
    page = _write_concept_draft_with_one_claim(kb_root, "concept-a", [source_id])

    # The LLM returns exactly one suggestion: line N, this source, with a
    # quote that appears verbatim in the source body.
    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"suggestions": [{"line": 6, "source_id": "web-2026-01-01-aaa", '
            '"evidence_quote": "Claim X is documented here."}]}'
        ),
        input_tokens=100, output_tokens=20, model="claude-sonnet-4-6",
    )

    results = suggest_cites(page, client=fake_client)

    assert len(results) == 1
    s: CiteSuggestion = results[0]
    assert s.line == 6
    assert s.source_id == source_id
    assert s.unambiguous is True
    assert s.evidence_verified is True
```

- [ ] **Step 2: Run, expect failure**

Run: `.venv/bin/pytest tests/gateway/test_cite_suggest.py -v`
Expected: ImportError on `gateway.ops.cite_suggest`.

---

### Task C2: Implement `cite_suggest` minimum to pass C1

**Files:**
- Create: `src/gateway/ops/cite_suggest.py`

- [ ] **Step 1: Implement**

```python
"""LLM-driven citation suggestion for `wiki cite --suggest` (M49 AGT-2).

Reads a wiki draft + its declared sources, asks Sonnet 4.6 (via
``AnthropicAPIClient`` with prompt caching) to propose
``{line, source_id, evidence_quote}`` triples for unresolved claims,
then verifies each triple's evidence quote is a substring of the
proposed source's raw body. Unverified or multi-candidate suggestions
are flagged for escalation rather than auto-applied.

The Aggressive caller (``finalize-batch --suggest --execute``) applies
only suggestions with ``unambiguous=True`` and ``evidence_verified=True``.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re

from gateway import frontmatter as fm
from gateway import paths
from gateway.llm.api_client import AnthropicAPIClient
from gateway.llm.config import model_for


@dataclass(frozen=True)
class CiteSuggestion:
    line: int
    source_id: str
    evidence_quote: str
    unambiguous: bool
    evidence_verified: bool
    skip_reason: str = ""  # populated when not auto-appliable

    @property
    def auto_appliable(self) -> bool:
        return self.unambiguous and self.evidence_verified


_SYSTEM_PROMPT = (
    "You are a citation assistant for a knowledge wiki. The user will "
    "give you a draft wiki page (with line numbers) and the raw bodies of "
    "the sources the draft was authored from. Your job: for each line "
    "containing a substantive claim that lacks a `[[sources/<id>]]` "
    "citation, identify which single source supports the claim and emit "
    "a JSON object of the form:\n\n"
    '{"suggestions": [{"line": <int>, "source_id": "<id>", '
    '"evidence_quote": "<verbatim substring from that source>"}]}\n\n'
    "Rules:\n"
    "- Only emit a suggestion when exactly one source supports the claim. "
    "If more than one source could support it, OMIT the line entirely.\n"
    "- The `evidence_quote` must be a verbatim substring of the named "
    "source's body (preserving capitalization, punctuation, and spaces "
    "as much as possible).\n"
    "- Use 1-indexed line numbers matching the file shown to you.\n"
    "- Output strictly the JSON object — no prose, no markdown."
)


def _normalize_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _read_source_body(kb_root: Path, source_id: str) -> str | None:
    """Find the raw source file for ``source_id`` and return its body
    (frontmatter stripped). Returns None if not found / unparseable."""
    for st in paths.SOURCE_TYPES:
        candidate = kb_root / "raw" / st / f"{source_id}.md"
        if candidate.exists():
            try:
                _, body = fm.parse(candidate.read_text())
                return body
            except fm.FrontmatterError:
                return None
    return None


def _verify_quote(quote: str, source_body: str) -> bool:
    return _normalize_whitespace(quote) in _normalize_whitespace(source_body)


def suggest_cites(page_path: str | Path, *,
                  client: AnthropicAPIClient | None = None) -> list[CiteSuggestion]:
    """Run cite-suggest on one draft. Returns a list of suggestions —
    callers (the Aggressive batch driver) decide which to auto-apply.

    `client` is injectable for testing. If omitted, instantiates a fresh
    ``AnthropicAPIClient`` reading ``ANTHROPIC_API_KEY_RESEARCH``.
    """
    kb_root = paths.knowledge_root()
    target = Path(page_path)
    if not target.is_absolute():
        target = (kb_root / target).resolve()

    text = target.read_text()
    front, _body = fm.parse(text)
    source_ids = list(front.get("sources") or []) + list(front.get("synthesizes") or [])

    # Load source bodies for verification later, AND to include in prompt.
    source_bodies: dict[str, str] = {}
    for sid in source_ids:
        body = _read_source_body(kb_root, sid)
        if body is not None:
            source_bodies[sid] = body

    user_prompt = _build_user_prompt(text, source_bodies)

    if client is None:
        client = AnthropicAPIClient()
    result = client.call_with_usage(
        user_prompt=user_prompt,
        system_prompt=_SYSTEM_PROMPT,
        model=model_for("cite_suggest"),
        max_tokens=2048,
    )

    return _parse_and_verify(result.text, source_bodies)


def _build_user_prompt(file_text: str, source_bodies: dict[str, str]) -> str:
    numbered = "\n".join(
        f"{i + 1:4}: {line}"
        for i, line in enumerate(file_text.splitlines())
    )
    sources_block = "\n\n".join(
        f"--- SOURCE {sid} ---\n{body}"
        for sid, body in source_bodies.items()
    )
    return (
        "DRAFT WIKI PAGE (line-numbered):\n\n"
        f"{numbered}\n\n"
        "SOURCES:\n\n"
        f"{sources_block}\n\n"
        "Emit the JSON object now."
    )


def _parse_and_verify(raw_text: str,
                      source_bodies: dict[str, str]) -> list[CiteSuggestion]:
    raw_text = raw_text.strip()
    # Be tolerant of code-fence wrapping the LLM might emit.
    if raw_text.startswith("```"):
        raw_text = re.sub(r"^```(?:json)?\s*", "", raw_text)
        raw_text = re.sub(r"\s*```\s*$", "", raw_text)

    try:
        payload = json.loads(raw_text)
    except json.JSONDecodeError:
        return []

    raw_suggestions = payload.get("suggestions") or []
    # Detect ambiguity by counting how many suggestions hit the same line.
    line_counts: dict[int, int] = {}
    for s in raw_suggestions:
        ln = int(s.get("line", 0))
        if ln <= 0:
            continue
        line_counts[ln] = line_counts.get(ln, 0) + 1

    out: list[CiteSuggestion] = []
    for s in raw_suggestions:
        try:
            line = int(s["line"])
            source_id = str(s["source_id"])
            quote = str(s["evidence_quote"])
        except (KeyError, TypeError, ValueError):
            continue

        unambiguous = line_counts.get(line, 0) == 1
        body = source_bodies.get(source_id, "")
        verified = bool(body) and _verify_quote(quote, body)

        skip_reason = ""
        if not unambiguous:
            skip_reason = "multi-candidate line"
        elif not verified:
            skip_reason = "evidence quote not found in source body"

        out.append(CiteSuggestion(
            line=line,
            source_id=source_id,
            evidence_quote=quote,
            unambiguous=unambiguous,
            evidence_verified=verified,
            skip_reason=skip_reason,
        ))

    return out
```

- [ ] **Step 2: Run C1**

Run: `.venv/bin/pytest tests/gateway/test_cite_suggest.py::test_suggest_returns_unambiguous_when_single_source_quotes_claim -v`
Expected: PASS.

---

### Task C3: Test ambiguous case — two suggestions on the same line are both flagged

**Files:**
- Modify: `tests/gateway/test_cite_suggest.py`

- [ ] **Step 1: Add test**

```python
def test_two_suggestions_on_same_line_are_marked_ambiguous(kb_root):
    sid1 = "web-2026-01-01-aaa"
    sid2 = "web-2026-01-02-bbb"
    _write_raw_source(kb_root, sid1, "Claim X is documented in source one.\n")
    _write_raw_source(kb_root, sid2, "Claim X is documented in source two.\n")
    page = _write_concept_draft_with_one_claim(kb_root, "concept-b", [sid1, sid2])

    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"suggestions": ['
            f'{{"line": 6, "source_id": "{sid1}", "evidence_quote": "Claim X is documented in source one."}},'
            f'{{"line": 6, "source_id": "{sid2}", "evidence_quote": "Claim X is documented in source two."}}'
            ']}'
        ),
        input_tokens=100, output_tokens=40, model="claude-sonnet-4-6",
    )

    results = suggest_cites(page, client=fake_client)

    assert len(results) == 2
    assert all(not s.auto_appliable for s in results)
    assert all(s.skip_reason == "multi-candidate line" for s in results)
```

- [ ] **Step 2: Run**

Expected: PASS (the `line_counts` logic handles this).

---

### Task C4: Test unverified evidence quote is rejected

**Files:**
- Modify: `tests/gateway/test_cite_suggest.py`

- [ ] **Step 1: Add test**

```python
def test_unverified_evidence_quote_marks_suggestion_not_appliable(kb_root):
    sid = "web-2026-01-01-ccc"
    _write_raw_source(kb_root, sid, "Real text only.\n")
    page = _write_concept_draft_with_one_claim(kb_root, "concept-c", [sid])

    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"suggestions": [{"line": 6, "source_id": "%s", '
            '"evidence_quote": "HALLUCINATED QUOTE NOT IN SOURCE"}]}' % sid
        ),
        input_tokens=80, output_tokens=15, model="claude-sonnet-4-6",
    )

    results = suggest_cites(page, client=fake_client)

    assert len(results) == 1
    s = results[0]
    assert s.unambiguous is True
    assert s.evidence_verified is False
    assert s.auto_appliable is False
    assert "not found" in s.skip_reason
```

- [ ] **Step 2: Run**

Expected: PASS.

---

### Task C5: Wire `--suggest` flag into existing `wiki cite` CLI

**Files:**
- Modify: `src/gateway/cli.py`

- [ ] **Step 1: Locate the `wiki cite` argparse block (~line 216)**

Find `p_cite = subparsers.add_parser("cite", ...)`. Currently it accepts `page_path` + `LINE:SOURCE_ID` positionals. We need to make `LINE:SOURCE_ID` optional and add `--suggest`.

- [ ] **Step 2: Modify to accept `--suggest`**

```python
p_cite = subparsers.add_parser("cite", help=SUBCOMMANDS["cite"])
p_cite.add_argument("page_path", help="...")
p_cite.add_argument(
    "additions",
    metavar="LINE:SOURCE_ID",
    nargs="*",
    help="One or more LINE:SOURCE_ID pairs (omit when using --suggest).",
)
p_cite.add_argument(
    "--suggest", action="store_true",
    help="Use LLM to propose cite invocations for this page; emits stdout.",
)
```

(Adjust the exact lines; preserve any existing help/usage strings.)

- [ ] **Step 3: Update dispatch (~line 697)**

```python
if ns.subcommand == "cite":
    if ns.suggest:
        from gateway.ops.cite_suggest import suggest_cites
        suggestions = suggest_cites(ns.page_path)
        # Emit one `wiki cite` invocation per auto-appliable suggestion,
        # plus a commented escalation block for the rest.
        for s in suggestions:
            if s.auto_appliable:
                print(f"wiki cite {ns.page_path} {s.line}:{s.source_id}  # quote: {s.evidence_quote[:60]}")
            else:
                print(f"# ESCALATED line={s.line} source={s.source_id} reason=\"{s.skip_reason}\"")
        return OperationResult(success=True, summary=f"emitted {len(suggestions)} suggestion(s)")
    # ... existing cite path (parse LINE:SOURCE_ID into additions list) ...
```

- [ ] **Step 4: Verify `wiki cite --help` shows `--suggest`**

Run: `.venv/bin/wiki cite --help`
Expected: `--suggest` visible.

---

### Task C6: Commit Phase C

- [ ] **Step 1: Run all relevant tests**

Run: `.venv/bin/pytest tests/gateway/test_cite_suggest.py tests/gateway/test_cite.py tests/gateway/test_finalize_batch.py -v`
Expected: ALL PASS.

- [ ] **Step 2: Commit**

```bash
git add src/gateway/ops/cite_suggest.py src/gateway/cli.py tests/gateway/test_cite_suggest.py
git commit -m "feat(m49): wiki cite --suggest with evidence-quote verification"
```

---

# Phase D — Aggressive integration in finalize-batch

### Task D1: Write failing test — `--suggest --execute` applies unambiguous cites and finalizes

**Files:**
- Modify: `tests/gateway/test_finalize_batch.py`

- [ ] **Step 1: Add test**

```python
from unittest.mock import patch
from gateway.llm.telemetry import CallResult
from gateway.ops.cite_suggest import CiteSuggestion


def _write_draft_concept_with_unresolved(kb_root: Path, slug: str,
                                         source_id: str) -> Path:
    page = kb_root / "wiki" / "concepts" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    started = (datetime.now(timezone.utc) - timedelta(days=20)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    front = {
        "type": "concept",
        "slug": slug,
        "title": slug.title(),
        "domains": ["test-domain"],
        "draft": True,
        "draft_started_at": started,
        "draft_unresolved_claims": 1,
        "sources": [source_id],
    }
    page.write_text(fm.serialize(
        front,
        "# title\n\n## Summary\n\nA cited fact appears in source one.\n",
    ))
    return page


def test_aggressive_applies_unambiguous_suggestion_then_finalizes(kb_root):
    sid = "web-2026-01-01-zzz"
    # Wiki source page (cite op requires this to exist)
    wiki_src = kb_root / "wiki" / "sources" / f"{sid}.md"
    wiki_src.parent.mkdir(parents=True, exist_ok=True)
    wiki_src.write_text(fm.serialize(
        {"type": "source", "source_id": sid, "source_type": "web",
         "title": "Z", "domains": ["test-domain"]},
        "# Z\n",
    ))
    # Raw source body containing the evidence quote
    raw = kb_root / "raw" / "web" / f"{sid}.md"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(fm.serialize(
        {"id": sid, "type": "web", "title": "Z",
         "url": "https://example.com/z", "domains": ["test-domain"]},
        "A cited fact appears in source one.\n",
    ))

    page = _write_draft_concept_with_unresolved(kb_root, "test-concept", sid)

    with patch("gateway.ops.finalize_batch.suggest_cites") as mock_suggest:
        mock_suggest.return_value = [CiteSuggestion(
            line=6,
            source_id=sid,
            evidence_quote="A cited fact appears in source one.",
            unambiguous=True,
            evidence_verified=True,
        )]
        result = finalize_batch(execute=True, suggest=True)

    assert result.success
    front_after, body_after = fm.parse(page.read_text())
    assert "draft" not in front_after
    assert f"[[sources/{sid}]]" in body_after
```

- [ ] **Step 2: Run, expect FAIL**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py::test_aggressive_applies_unambiguous_suggestion_then_finalizes -v`
Expected: FAIL — finalize_batch ignores `suggest=True` in Cat B path.

---

### Task D2: Implement the Aggressive path

**Files:**
- Modify: `src/gateway/ops/finalize_batch.py`

- [ ] **Step 1: Import the cite-suggest module and the cite op at the top**

```python
from gateway.ops.cite import cite as cite_one
from gateway.ops.cite_suggest import suggest_cites, CiteSuggestion
```

- [ ] **Step 2: Replace the escalation branch with the Aggressive flow**

In the main loop, after the Cat A short-circuit, replace the catch-all `outcomes.append(...escalated...)` with:

```python
# Cat B / suggest path: validator might be 0-unresolved already; or we
# call cite-suggest to propose cites; or we escalate.
page_abs = paths.knowledge_root() / rel

if not suggest:
    outcomes.append(_Outcome(
        page=rel, category="escalated", finalized=False,
        note=f"unresolved_claims={unresolved!r} (no --suggest)",
    ))
    continue

# --suggest active
try:
    suggestions = suggest_cites(page_abs)
except Exception as e:
    outcomes.append(_Outcome(
        page=rel, category="escalated", finalized=False,
        note=f"cite-suggest failed: {e}",
    ))
    continue

appliable = [s for s in suggestions if s.auto_appliable]
escalations = [s for s in suggestions if not s.auto_appliable]
escalation_strs = [
    f"# line={s.line} source={s.source_id} reason=\"{s.skip_reason}\""
    for s in escalations
]

if not appliable:
    outcomes.append(_Outcome(
        page=rel, category="escalated", finalized=False,
        note="no auto-appliable suggestions",
        suggested_cites=escalation_strs,
    ))
    continue

if not execute:
    # Suggest-only / dry-run: emit invocation strings, do not apply.
    invocation_strs = [
        f"wiki cite {rel} {s.line}:{s.source_id}"
        for s in appliable
    ]
    outcomes.append(_Outcome(
        page=rel, category="suggest_applied", finalized=False,
        note=f"{len(appliable)} appliable, {len(escalations)} escalated",
        suggested_cites=invocation_strs + escalation_strs,
    ))
    continue

# Execute: apply each appliable suggestion via the cite op, then finalize.
additions = [(s.line, s.source_id) for s in appliable]
cite_result = cite_one(page_abs, additions)
if not cite_result.success:
    outcomes.append(_Outcome(
        page=rel, category="escalated", finalized=False,
        note=f"cite failed: {'; '.join(cite_result.errors or [])}",
        suggested_cites=escalation_strs,
    ))
    continue

finalize_result = finalize_one(page_abs)
if finalize_result.success:
    outcomes.append(_Outcome(
        page=rel, category="suggest_applied", finalized=True,
        note=f"applied {len(appliable)} cite(s); {len(escalations)} escalated",
        suggested_cites=escalation_strs,
    ))
else:
    outcomes.append(_Outcome(
        page=rel, category="escalated", finalized=False,
        note=f"finalize after cite failed: {'; '.join(finalize_result.errors or [])}",
        suggested_cites=escalation_strs,
    ))
```

- [ ] **Step 3: Run D1**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py::test_aggressive_applies_unambiguous_suggestion_then_finalizes -v`
Expected: PASS.

---

### Task D3: Test escalation — ambiguous suggestions not applied

**Files:**
- Modify: `tests/gateway/test_finalize_batch.py`

- [ ] **Step 1: Add test**

```python
def test_ambiguous_suggestion_not_applied(kb_root):
    sid1 = "web-2026-01-01-yyy"
    page = _write_draft_concept_with_unresolved(kb_root, "concept-amb", sid1)

    with patch("gateway.ops.finalize_batch.suggest_cites") as mock_suggest:
        mock_suggest.return_value = [
            CiteSuggestion(line=6, source_id=sid1, evidence_quote="q1",
                           unambiguous=False, evidence_verified=True,
                           skip_reason="multi-candidate line"),
            CiteSuggestion(line=6, source_id="other",
                           evidence_quote="q2",
                           unambiguous=False, evidence_verified=True,
                           skip_reason="multi-candidate line"),
        ]
        result = finalize_batch(execute=True, suggest=True)

    assert result.success
    front_after, body_after = fm.parse(page.read_text())
    assert front_after.get("draft") is True  # not finalized
    # No cite was applied
    assert "[[sources/" not in body_after
```

- [ ] **Step 2: Run + verify pass**

Expected: PASS.

---

### Task D4: Write the per-run report file

**Files:**
- Modify: `src/gateway/ops/finalize_batch.py`
- Modify: `tests/gateway/test_finalize_batch.py`

- [ ] **Step 1: Add report-writing helper**

In `finalize_batch.py`, after the main loop and before the return, add:

```python
def _write_run_report(outcomes: list[_Outcome], *, dry_run: bool) -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    report_dir = paths.knowledge_internal() / "finalize-batch"
    report_dir.mkdir(parents=True, exist_ok=True)
    report = report_dir / f"{ts}.md"

    cat_a = [o for o in outcomes if o.category == "cat_a"]
    suggest_applied = [o for o in outcomes if o.category == "suggest_applied"]
    escalated = [o for o in outcomes if o.category == "escalated"]

    lines = [
        f"# finalize-batch run — {ts}",
        "",
        f"Mode: {'dry-run' if dry_run else 'execute'}",
        "",
        "## Summary",
        f"- cat_a (deterministic): {len(cat_a)} ({sum(1 for o in cat_a if o.finalized)} finalized)",
        f"- suggest_applied (LLM): {len(suggest_applied)} ({sum(1 for o in suggest_applied if o.finalized)} finalized)",
        f"- escalated: {len(escalated)}",
        "",
    ]
    if cat_a:
        lines += ["## Cat A (deterministic)", ""]
        for o in cat_a:
            mark = "FINALIZED" if o.finalized else "candidate"
            lines.append(f"- {mark}: `{o.page}` — {o.note}")
        lines.append("")
    if suggest_applied:
        lines += ["## Suggest-applied (LLM)", ""]
        for o in suggest_applied:
            mark = "FINALIZED" if o.finalized else "candidate"
            lines.append(f"- {mark}: `{o.page}` — {o.note}")
            for sc in o.suggested_cites:
                lines.append(f"  - {sc}")
        lines.append("")
    if escalated:
        lines += ["## Escalated", ""]
        for o in escalated:
            lines.append(f"- `{o.page}` — {o.note}")
            for sc in o.suggested_cites:
                lines.append(f"  - {sc}")
        lines.append("")

    report.write_text("\n".join(lines))
    return report
```

In `finalize_batch`, before returning, call `report_path = _write_run_report(outcomes, dry_run=not execute)` and include `paths_touched=[report_path, paths.log_path()]` in the return value. Also append a log.md entry via `log.append(op="finalize-batch", ...)`.

- [ ] **Step 2: Add test**

```python
def test_report_file_written_with_outcome_categories(kb_root):
    _write_draft_entity(kb_root, "rep-co", age_days=12, unresolved=0)

    result = finalize_batch(execute=True, suggest=False)

    assert result.success
    report_dir = kb_root / ".knowledge" / "finalize-batch"
    assert report_dir.is_dir()
    reports = list(report_dir.glob("*.md"))
    assert len(reports) == 1
    text = reports[0].read_text()
    assert "rep-co" in text
    assert "cat_a" in text
```

- [ ] **Step 3: Run all Phase D tests**

Run: `.venv/bin/pytest tests/gateway/test_finalize_batch.py -v`
Expected: ALL PASS.

---

### Task D5: Commit Phase D

- [ ] **Step 1: Full-suite regression check**

Run: `.venv/bin/pytest tests/ -q`
Expected: All PASS.

- [ ] **Step 2: Commit**

```bash
git add src/gateway/ops/finalize_batch.py tests/gateway/test_finalize_batch.py
git commit -m "feat(m49): Aggressive integration — auto-apply unambiguous LLM cites then finalize"
```

---

# Phase E — MCP parity (K2) + scheduler entry (K4)

### Task E1: Add `wiki_finalize_batch` MCP tool

**Files:**
- Modify: `src/gateway/mcp_server.py`
- Modify: `tests/gateway/test_mcp_parity.py` (or `test_mcp.py` if parity test lives there)

- [ ] **Step 1: Locate where MCP tools are registered**

Run: `grep -n "wiki_finalize\|wiki_cite\|register_tool\|@mcp\.tool" src/gateway/mcp_server.py | head -10`

- [ ] **Step 2: Add a `wiki_finalize_batch` tool that mirrors the CLI**

Pattern after the existing `wiki_finalize` MCP tool. Args: `domain` (optional), `limit` (optional int), `execute` (bool, default False), `suggest` (bool, default False). Body calls `gateway.ops.finalize_batch.finalize_batch(...)` and returns the `OperationResult`.

- [ ] **Step 3: Update parity test**

If `tests/gateway/test_mcp_parity.py` enumerates expected CLI ops with MCP equivalents, add `finalize-batch` to the expected list.

Run: `.venv/bin/pytest tests/gateway/test_mcp_parity.py -v`
Expected: PASS.

- [ ] **Step 4: Commit**

```bash
git add src/gateway/mcp_server.py tests/gateway/test_mcp_parity.py
git commit -m "feat(m49): MCP parity for wiki_finalize_batch (K2 discipline)"
```

---

### Task E2: Add the daily scheduler entry

**Files:**
- Modify: `.knowledge/schedule.yaml` (via `wiki schedule add`)

- [ ] **Step 1: Add the job**

Run: `.venv/bin/wiki schedule add daily-finalize-batch "30 4 * * *" "wiki finalize-batch --suggest --execute"`
Expected: confirmation; `.knowledge/schedule.yaml` updated.

- [ ] **Step 2: Inspect the file**

Run: `cat .knowledge/schedule.yaml`
Expected: a `jobs:` entry with `name: daily-finalize-batch`, the cron expression, and the command.

- [ ] **Step 3: Dry-run the scheduler tick**

Run: `.venv/bin/wiki schedule run dry-run`
Expected: lists `daily-finalize-batch` as a would-run candidate (if cron is satisfied) or as skipped.

- [ ] **Step 4: Commit**

```bash
git add .knowledge/schedule.yaml
git commit -m "ops(m49): schedule daily finalize-batch --suggest --execute at 04:30 UTC"
```

---

# Phase F — Documentation & milestone wrap-up

### Task F1: Update WIKI.md ops table

**Files:**
- Modify: `WIKI.md`

- [ ] **Step 1: Find the Gateway Operations table**

Run: `grep -n "Gateway operations\|finalize-batch\|wiki cite --suggest" WIKI.md | head -10`

- [ ] **Step 2: Add two rows**

Append after the existing `wiki cite` and `wiki finalize` rows:

| `wiki finalize-batch [--suggest] [--execute] [--domain X] [--limit N]` | Batch-close stale drafts; deterministic Cat A + LLM-driven Cat B with verified evidence quotes |
| `wiki cite --suggest <page>` | LLM proposes `wiki cite` invocations; emits stdout; never modifies the page (the batch driver applies) |

- [ ] **Step 3: Commit**

```bash
git add WIKI.md
git commit -m "docs(m49): WIKI.md ops table — finalize-batch + cite --suggest"
```

---

### Task F2: Append M49 row to BUILD.md § 10

**Files:**
- Modify: `BUILD.md`

- [ ] **Step 1: Find § 10**

Run: `grep -n "^## 10\|M48 " BUILD.md | head -5`

- [ ] **Step 2: Add the M49 row matching the existing table shape**

(The exact structure depends on what's there; mirror the M48 row's columns. Typical: milestone, theme, acceptance, modules touched, test delta.)

- [ ] **Step 3: Commit**

```bash
git add BUILD.md
git commit -m "docs(m49): BUILD.md § 10 — M49 delivery row"
```

---

### Task F3: Create `docs/milestones/M49.md`

**Files:**
- Create: `docs/milestones/M49.md`

- [ ] **Step 1: Author the milestone doc**

Mirror M48's shape (load `docs/milestones/M48.md` for the template).

Sections to include:
- Goal (one paragraph)
- Components shipped (TOK-1 client, finalize-batch, cite --suggest, scheduler entry, MCP tool)
- Modules touched
- Test delta (e.g., 901 → final count)
- Acceptance criteria checklist (one bullet per criterion from the plan's Background)
- Hand-test results (filled in during the hand-test step)
- Follow-ups (e.g., the `auto-detect-corpus-shared-prefix` cache optimization, AGT-2.x extensions)
- Memory updates expected (none beyond [[separate_api_key_for_caching]] which is already written)

- [ ] **Step 2: Commit**

```bash
git add docs/milestones/M49.md
git commit -m "docs(m49): milestone delivery doc"
```

---

### Task F4: Hand-test against a real draft

This is the load-bearing validation step before declaring M49 shipped.

- [ ] **Step 1: Pick a Cat A draft**

Run: `.venv/bin/wiki finalize-batch --domain condo --limit 3`
Expected: prints 3 candidates from the condo domain; no files change.

- [ ] **Step 2: Execute against Cat A, deterministic only**

Run: `.venv/bin/wiki finalize-batch --domain condo --limit 3 --execute`
Expected: 3 drafts finalized; report file appears under `.knowledge/finalize-batch/`; log.md updated.

Verify: `git diff wiki/entities/<one-of-the-finalized>.md` shows `draft:` and `draft_started_at:` removed, `finalized_at:` added.

- [ ] **Step 3: Pick a Cat B draft and try --suggest dry-run**

Run: `.venv/bin/wiki finalize-batch --domain condo --limit 1 --suggest`
Expected: emits `wiki cite ...` invocation strings + escalations in the report. No files changed.

This call WILL hit the Anthropic API and consume budget. Monitor the console for spend.

- [ ] **Step 4: Aggressive — execute with --suggest on a small batch**

Run: `.venv/bin/wiki finalize-batch --domain condo --limit 5 --suggest --execute`
Expected: some drafts get cites applied + finalized; some escalate. Report enumerates both.

Verify the changes are correct by reading 2-3 of the auto-applied cites — does the LLM's source choice make sense?

- [ ] **Step 5: If hand-test passes, append findings to docs/milestones/M49.md**

Fill in the Hand-test results section: per-batch outcomes, any surprising LLM decisions, cost observed (from `total_cost_usd` if surfaced, otherwise from the Anthropic console).

- [ ] **Step 6: Commit the hand-test results**

```bash
git add docs/milestones/M49.md log.md .knowledge/finalize-batch/
git commit -m "data(m49): hand-test results — N drafts finalized across deterministic + Aggressive paths"
```

---

### Task F5: Tag the milestone

- [ ] **Step 1: Final regression check**

Run: `.venv/bin/pytest tests/ -q`
Expected: All PASS; test count ≥ 935.

- [ ] **Step 2: Tag**

```bash
git tag m49-agt2-draft-closer
```

- [ ] **Step 3: Push branch + tag**

```bash
git push origin main
git push origin m49-agt2-draft-closer
```

---

## Self-Review (run by plan author after writing)

1. **Spec coverage:**
   - TOK-1 client (env-var read, SDK call, cache_control, telemetry passthrough) → Phase A ✓
   - Deterministic Cat A finalize → Phase B ✓
   - LLM-driven cite-suggest with evidence verification → Phase C ✓
   - Aggressive integration (auto-apply unambiguous + verified) → Phase D ✓
   - Per-domain summary in log.md + per-run report → Phase D Task D4 ✓
   - MCP parity (K2) → Phase E Task E1 ✓
   - Scheduler entry (K4) → Phase E Task E2 ✓
   - Docs (WIKI/BUILD/milestone) → Phase F ✓
   - Hand-test → Phase F Task F4 ✓

2. **Placeholder scan:** none found. Task B2's `OperationResult.notes` field check has a real fallback instruction.

3. **Type consistency:** `CiteSuggestion` shape used identically in C1, C3, C4, D1, D3, D4. `_Outcome.suggested_cites` is list[str] everywhere.

4. **Risks / known unknowns:**
   - Anthropic SDK version pinning: `>=0.40` is a guess based on cache_control API stability. Verify against the SDK actually installed (Task A1 Step 4).
   - Cache TTL is 5 min — for a batch of 587 drafts processed in one run, the system prompt stays cached for the run. Per-draft user prompts are not cached.
   - The `wiki schedule add` syntax in E2 assumes a `subcommand` value of `add`; verify against `grep "schedule" src/gateway/cli.py` if it errors.

---

## Execution Handoff

Plan complete and saved to `docs/plans/2026-05-24-m49-agt2-draft-closer.md`. Two execution options:

**1. Subagent-Driven (recommended)** — dispatch a fresh subagent per task, two-stage review between tasks, fast iteration.

**2. Inline Execution** — execute tasks in this session with batch checkpoints.
