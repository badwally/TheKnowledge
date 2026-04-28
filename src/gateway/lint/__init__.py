"""Lint checks per WIKI.md § 12.

One submodule per check. Each exports `run() -> list[LintFinding]` so the
orchestrator can compose them. Findings carry a check name, severity,
message, optional path, and a metadata dict for structured detail.

M9 v1 ships six cheap checks (orphans, stale-drafts, citation-density,
schema-drift, inbox-pending, nlm-pending) and four stubs for the
LLM-driven / heuristic-heavy checks (missing-pages, stale-claims,
contradictions, filter-calibration). Stubs return empty lists; they
become real implementations in a follow-up milestone.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


SEVERITY_INFO = "info"
SEVERITY_WARNING = "warning"
SEVERITY_ERROR = "error"


@dataclass
class LintFinding:
    check: str
    severity: str
    message: str
    path: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "check": self.check,
            "severity": self.severity,
            "message": self.message,
            "path": self.path,
            "metadata": self.metadata,
        }


__all__ = [
    "LintFinding",
    "SEVERITY_ERROR",
    "SEVERITY_INFO",
    "SEVERITY_WARNING",
]
