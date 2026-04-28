"""Contradictions check (stub).

Per WIKI § 12.2: LLM-driven scan for contradictory claims across wiki
pages, scoped per domain. Each pass costs Claude calls per domain;
implementation deferred to a follow-up milestone.
"""

from __future__ import annotations

from gateway.lint import LintFinding


def run() -> list[LintFinding]:
    return []
