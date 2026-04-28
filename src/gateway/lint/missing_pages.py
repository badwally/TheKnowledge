"""Missing-pages check (stub).

Per WIKI § 12.2: terms appearing in 3+ pages without a dedicated entity
or concept page. Implementing this well requires noun-phrase extraction
and disambiguation — deferred to a follow-up milestone. Stub returns no
findings so the orchestrator stays uniform.
"""

from __future__ import annotations

from gateway.lint import LintFinding


def run() -> list[LintFinding]:
    return []
