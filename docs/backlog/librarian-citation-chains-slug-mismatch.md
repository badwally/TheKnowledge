# Backlog: citation-chains registry slug mismatch

**RESOLVED 2026-06-20** (branch `fix/lint-registry-slug-mismatch`). Took the
"rename the emitted `check=` to match the registered slug" direction (not the
Option-2 split below — `citation_chains.run()` emits two distinct sub-checks and
the unification kept a single public `--scope citation-chains` name). Both
`LintFinding(check=...)` calls now emit `"citation-chains"`; the dangling-vs-
aggregate sub-type is preserved in `metadata["kind"]`. Positive-coverage tests
unmasked (`test_inert_invariants.py`, `test_lint_citation_chains.py`); the
`assert f.check == slug` tripwire at `test_inert_invariants.py:~194` now holds
for this slug. No `LINT_BASELINES` change (citation-chains is not a gate baseline).

**Filed:** 2026-06-20
**Source:** Task P2 (T6 Step-1 lint positive coverage), test_inert_invariants.py
**Priority:** Medium (silent mismatch; parametrized negative control masks it)

## What

`ops/lint.py` registers the module as `("citation-chains", citation_chains.run)` but the
module (`lint/citation_chains.py`) emits findings with two different check slugs:

- `check="dangling-synthesizes-ref"` — for `synthesizes:` entries that resolve to no
  page on disk
- `check="aggregate-framing-without-synthesizes"` — for synthesis pages that use
  aggregate framing without a `synthesizes:` list

Neither matches `"citation-chains"`.

## Impact

The parametrized negative control (`test_lint_check_fires_on_real_signal[citation-chains]`)
passes because an empty repo produces no findings — the slug mismatch is never checked.
If `citation_chains.run()` produces findings on a real repo (e.g., after ingesting sources),
the `for f in findings_clean: assert f.check == slug` guard at `test_inert_invariants.py:193`
would fire on those findings — but only if findings are produced during the EMPTY-repo run,
which they won't be.

The positive-signal test (`test_citation_chains_fires_on_dangling_synthesizes_ref`) correctly
asserts `f.check == "dangling-synthesizes-ref"` (the actual behavior), not `"citation-chains"`.

## Resolution

Two options:

1. **Fix the module**: change the `LintFinding(check=...)` calls in `citation_chains.py` to
   emit `"citation-chains"` as the slug, replacing the current `"dangling-synthesizes-ref"`
   and `"aggregate-framing-without-synthesizes"` sub-slugs. This is a breaking change to any
   callers that filter on the sub-slug strings.

2. **Split into separate registrations**: register each sub-check as its own entry in `_CHECKS`:
   ```python
   ("dangling-synthesizes-ref", lambda: citation_chains.run_dangling()),
   ("aggregate-framing-without-synthesizes", lambda: citation_chains.run_aggregate()),
   ```
   This removes the "citation-chains" umbrella entry and requires splitting the `run()` fn.

Option 2 is cleaner and aligns with how `claim_confidence` already exposes two separate
runners (`run_distribution` / `run_propagation`).

## Trigger

Implement when refactoring the lint orchestrator (e.g., adding per-check scope selectors or
severity filters), or when `citation-chains` needs to be distinguished from its sub-checks
in `LINT_BASELINES` in `gate.py`.
