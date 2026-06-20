# Backlog: Positive coverage for LLM-dependent lint checks

**Filed:** 2026-06-20
**Source:** Task P2 (T6 Step-1 lint positive coverage), test_inert_invariants.py
**Priority:** Low (negative control already proves wiring; LLM mock needed)

## What

Three lint checks and one lint mode cannot be driven to produce a positive finding
in the integration test suite without a live Claude CLI subprocess:

| Check slug | Module | Why LLM required |
|---|---|---|
| `contradictions` | `lint/contradictions.py` | Sends a claim-comparison prompt to Claude via `ClaudeCLIFilterClient` |
| `missing-pages` | `lint/missing_pages.py` | Sends a missing-concept suggestion prompt to Claude |
| `filter-calibration` | `lint/filter_calibration.py` | Sends a filter re-score prompt to Claude |
| `stale-claims` (WARNING mode) | `lint/stale_claims.py` | `sample_size > 0` sends supersede-verification prompts to Claude |

The deterministic INFO mode of `stale-claims` (sample_size=0) IS covered by
`test_stale_claims_fires_on_two_academic_sources_with_gap` in `test_inert_invariants.py`.

## Current state

These four cases are `xfail` in `test_inert_invariants.py` with `strict=False`. The
negative control (empty repo → no findings, runner is callable) is proven by the
parametrized `test_lint_check_fires_on_real_signal[<slug>]` tests, which already pass.

## Resolution path

Two options:

1. **Injectable stub client**: Add a `StubFilterClient` to the test suite that returns a
   pre-baked response JSON (e.g., `{"contradictions": [{"a": 1, "b": 2, "rationale": "..."}]}`).
   All three checks accept `client: FilterClient | None = None` as an argument, making
   this straightforward. This is the preferred path — no real LLM call, no network.

2. **Live integration test tier**: Mark these tests `@pytest.mark.slow` and run them only
   on a CI tier that has ANTHROPIC_API_KEY set. Costs ~1-3 Claude calls per run.

Option 1 is preferred because it keeps the suite fast and hermetic.

## Trigger

Implement when adding a `StubFilterClient` to `tests/gateway/conftest.py` or a new
`tests/stubs.py` module. The xfail tests in `test_inert_invariants.py` should then be
updated to use the stub and the `strict=False` xfail removed.
