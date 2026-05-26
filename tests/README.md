# tests/

Pytest suite for the `gateway` package. All tests run under `.venv/` — never use the system Python.

## Quick start

```bash
# Full suite
.venv/bin/python -m pytest tests/

# Single file
.venv/bin/python -m pytest tests/gateway/test_finetune.py

# One test
.venv/bin/python -m pytest tests/gateway/test_finetune.py::test_distill_prompt_writes_candidate_and_does_not_overwrite_live

# By keyword
.venv/bin/python -m pytest -k "calibration"

# Verbose with short tracebacks
.venv/bin/python -m pytest -v --tb=short
```

## Layout

```
tests/
├── gateway/           # gateway package tests — mirrors src/gateway/ structure
│   ├── conftest.py    # shared fixtures
│   ├── evaluate/      # evaluation framework tests
│   └── test_*.py      # one file per module or feature
├── test_llm_config.py
├── test_nlm_client.py
└── test_research_adapter_*.py
```

## The `kb_root` fixture

Every test that touches the filesystem must use the `kb_root` fixture from `tests/gateway/conftest.py`. It monkeypatches `KNOWLEDGE_ROOT` to a `tmp_path` directory for the duration of the test, ensuring tests are isolated and never touch real wiki content.

```python
def test_my_op(kb_root: Path) -> None:
    # write setup files under kb_root
    (kb_root / "wiki" / "sources" / "test.md").write_text("...")
    # call op under test
    result = my_op()
    assert result.success
```

## Stub vs real LLM calls

**Default:** all LLM calls are stubbed. Tests inject `StubClient`, `StubFilterClient`, `StubPlanClient`, etc., or use the injectable `client=` / `fetch_fn=` / `filter_client=` parameters on gateway ops.

**Real LLM calls are never made in the test suite.** Operations that make network or subprocess calls (filter scoring, plan generation, NLM artifacts, poller HTTP fetches) are covered by:
1. Injectable `client=` / `fetch_fn=` parameters receiving a stub
2. `monkeypatch` on the subprocess/HTTP layer
3. Hand-test notes in the milestone doc (for operations too expensive or side-effectful to automate)

## Deferred hand-tests

Some operations produce results that depend on external state or are expensive/side-effectful:
- Real `claude -p` calls (filter scoring, plan generation)
- NotebookLM artifact creation
- Apple Notes JXA scraping
- PubMed / arXiv HTTP fetches for retraction/revision pollers

These are marked with a comment like `# hand-test deferred` and tested via stub. The corresponding milestone doc records what the real hand-test verified.

## Mocking conventions

| Scenario | Pattern |
|----------|---------|
| Filter client (LLM) | `client=StubFilterClient("include", 0.9)` |
| Plan client (LLM) | `client=StubPlanClient(plan)` |
| VLM client | `client=StubVLMClient("description text")` |
| HTTP fetch in pollers | `fetch_fn=lambda url: "<fixed-xml>"` |
| Subprocess (claude -p) | `monkeypatch.setattr(subprocess, "run", ...)` |
| KNOWLEDGE_ROOT | `kb_root` fixture (always) |

Never use `MagicMock` for gateway protocol stubs. `MagicMock` auto-creates attributes (including `call_split_with_usage`) that trigger unexpected code paths in the K5 telemetry system. Use a plain stub class instead.

## Test naming conventions

| File | What it covers |
|------|----------------|
| `test_<module>.py` | Module-level unit tests |
| `test_<ticket>_<feature>.py` | Ticket-scoped feature tests (e.g. `test_qual10_calibration.py`) |
| `test_arch14_hard_rule_1.py` | Structural invariant guards (CI-enforced hard rules) |
| `test_lint.py` | Lint check registry; KNOWN_CHECKS set |
| `test_status_*.py` | `wiki status` output for a specific subsystem |

## Adding a new test file

1. Mirror the module path: `src/gateway/ops/my_op.py` → `tests/gateway/test_my_op.py`
2. Use `kb_root` for all filesystem access
3. Stub all LLM/network calls
4. Update `KNOWN_CHECKS` in `test_lint.py` when adding a new lint check
5. Update `_ALLOWED_WRITE_TEXT` in `test_arch14_hard_rule_1.py` if your op writes to non-wiki/raw paths

## Running in CI

```bash
.venv/bin/python -m pytest tests/ -q --tb=short
```

Expected: all tests pass in under 60 seconds. Tests that approach the time budget are likely making real network calls — investigate.
