# Backlog: long-slugs registry slug mismatch

**RESOLVED 2026-06-20** (branch `fix/lint-registry-slug-mismatch`). Took Option 1
(rename the emitted `check=`): `long_slugs.run()` now emits `check="long-slugs"`
to match the registry key, leaving the public `--scope long-slugs` name and
`LINT_BASELINES` untouched. Also removes the confusing name-collision with the
unrelated validator rule `slug-too-long` (validator.py — a separate subsystem,
left as-is). Positive-coverage tests unmasked (`test_inert_invariants.py`,
`test_validator.py`); the `assert f.check == slug` tripwire now holds for this slug.

**Filed:** 2026-06-20
**Source:** Task P2 (T6 Step-1 lint positive coverage), test_inert_invariants.py
**Priority:** Low (functionally correct; cosmetic inconsistency)

## What

`ops/lint.py` registers the module as `("long-slugs", long_slugs.run)` but the module
(`lint/long_slugs.py`) emits findings with `check="slug-too-long"` (line 30).

## Impact

The parametrized negative control (`test_lint_check_fires_on_real_signal[long-slugs]`)
passes because an empty repo produces no findings — the slug mismatch is never checked.
If `long_slugs.run()` produces findings, the slug-consistency guard at
`test_inert_invariants.py:193` (`assert f.check == slug`) would fail because
`f.check == "slug-too-long"` but `slug == "long-slugs"`.

The positive-signal test (`test_long_slugs_fires_on_grandfathered_oversized_slug`) correctly
asserts `f.check == "slug-too-long"` (the actual behavior) and documents the mismatch.

## Resolution

Two options:

1. **Fix the module**: change `LintFinding(check="slug-too-long", ...)` in `long_slugs.py`
   to emit `check="long-slugs"` to match the registry key.

2. **Rename the registry key**: change `("long-slugs", long_slugs.run)` in `ops/lint.py` to
   `("slug-too-long", long_slugs.run)`. This is a breaking change to `LINT_BASELINES` in
   `gate.py` and any external callers that filter on the `"long-slugs"` slug.

Option 1 is lower-impact (only the lint module changes; the registry key is unchanged).

## Trigger

Implement at next `long_slugs.py` touch. The parametrized invariant test would then
catch any future regression.
