"""Stale-claims check (stub).

Per WIKI § 12.2: claims whose cited source has been superseded by a newer
source on the same topic. Implementing this requires entity-overlap +
recency comparison across sources — deferred to a follow-up milestone.
"""

from __future__ import annotations

from gateway.lint import LintFinding


def run() -> list[LintFinding]:
    return []
