"""Filter-calibration check (stub).

Per WIKI § 12.2: random sample of past filter decisions re-scored against
the current policy version; report mean delta and outliers. Requires the
filter to be invokable per-source — implementation deferred to a follow-up
milestone.
"""

from __future__ import annotations

from gateway.lint import LintFinding


def run() -> list[LintFinding]:
    return []
