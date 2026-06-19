# Testing Guide

## Marker contract

Four pytest markers are registered in `pyproject.toml [tool.pytest.ini_options]`. `--strict-markers` is set — an unregistered or typo'd marker is an ERROR, not a silent no-op.

| Marker | Meaning | Speed |
|---|---|---|
| _(none)_ | Equivalent to `unit` — fast, no I/O, no external deps | <1s per test |
| `unit` | Fast, no I/O, no external deps — pure logic | <1s per test |
| `integration` | Touches real files, git repos, or gateway state — requires fixtures | seconds |
| `e2e` | Full CLI or MCP round-trip end-to-end — gates release | seconds–minutes |
| `slow` | Takes >5s or exercises a soak/load path | >5s |

Unmarked tests are treated as `unit` by convention (they run in every mode). Use `@pytest.mark.unit` explicitly only when the distinction matters for clarity.

## Invocation recipes

```bash
# Fast inner loop — excludes slow and e2e tiers
.venv/bin/python -m pytest -m "not slow and not e2e"

# Full suite — all tiers
.venv/bin/python -m pytest

# Integration only
.venv/bin/python -m pytest -m integration

# E2E only
.venv/bin/python -m pytest -m e2e

# Slow soak tests only
.venv/bin/python -m pytest -m slow
```

Always use `.venv/bin/python -m pytest` — never the system `python`. The system interpreter lacks the gateway package.

## Test tiers (as implemented by M1–M6)

| Tier | Marker | Description |
|---|---|---|
| T1 | _(existing, unmarked)_ | Unit tests already in `tests/` |
| T2 | `integration` | Gateway lifecycle tests (deposit, commit gate, dedup, retraction) |
| T3 | `slow` + `integration` | Soak / concurrency tests |
| T4 | `e2e` | CLI and MCP end-to-end round-trips |
| T5 | _(eval gate, separate)_ | Retrieval eval — run via `wiki eval-retrieval` |
| T6 | `unit` / `integration` | Property-based tests (Hypothesis) |

## Eval floor

The retrieval eval floor is **recall@10 ≥ 0.90** (baseline 0.926). Do not merge changes that regress it.

```bash
# Run retrieval eval
.venv/bin/python -m pytest tests/gateway/evaluate/ -m "not slow"
# Or via wiki CLI
.venv/bin/wiki eval-retrieval
```

A failing eval **halts the build** — do not advance to the next milestone with a regression outstanding.
