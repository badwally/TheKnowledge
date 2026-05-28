"""Gateway core: shared write primitives and operation result type.

Per WIKI.md § 9.2, every gateway operation:
1. Validates inputs.
2. Acquires a write lock if writing.
3. Executes.
4. Validates outputs.
5. Applies writes atomically.
6. Updates backlinks.
7. Appends a log entry.
8. Releases the lock.
9. Returns a structured result.

This module supplies the shared primitives (atomic write, OperationResult, parse_iso).
Operation modules under `gateway/ops/` implement the specific contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import os
from pathlib import Path
import tempfile
from typing import TYPE_CHECKING


def claude_cli_env() -> dict[str, str]:
    """Return a copy of ``os.environ`` suitable for ``claude -p`` subprocesses.

    By default, strips ``ANTHROPIC_API_KEY`` so the Claude CLI falls back
    to the user's Max-plan OAuth session instead of billing against API
    credits. Without this, every ``claude -p`` invocation routes through
    the API even when a Max plan is available — at meaningful cost during
    multi-hundred-call research runs (filter, plan, VLM all shell out per
    item).

    Opt-in override: set ``WIKI_ALLOW_API_KEY=1`` in the parent env to
    preserve ``ANTHROPIC_API_KEY`` and use API credits intentionally
    (e.g., to bypass Max-plan rate limits during a one-off bulk run).
    """
    env = os.environ.copy()
    if env.get("WIKI_ALLOW_API_KEY") != "1":
        env.pop("ANTHROPIC_API_KEY", None)
    return env

if TYPE_CHECKING:
    from gateway.plan import Contradiction


@dataclass
class AuthorshipReport:
    """Structured summary of what the authorship agent did."""

    pages_created: list[str] = field(default_factory=list)
    pages_updated: list[str] = field(default_factory=list)
    contradictions: list["Contradiction"] = field(default_factory=list)

    def format_summary(self) -> str:
        parts = [
            f"{len(self.pages_created)} created",
            f"{len(self.pages_updated)} updated",
        ]
        if self.contradictions:
            parts.append(f"{len(self.contradictions)} contradiction(s) found")
        return ", ".join(parts)

    def format_detail(self) -> list[str]:
        """Return lines suitable for CLI output."""
        lines: list[str] = []
        for p in self.pages_created:
            lines.append(f"  + {p}")
        for p in self.pages_updated:
            lines.append(f"  ~ {p}")
        for c in self.contradictions:
            lines.append(
                f"  ! CONTRADICTION ({c.severity}) in {c.existing_page}:"
            )
            lines.append(f"    existing: {c.existing_claim[:120]}")
            lines.append(f"    new:      {c.new_claim[:120]}")
        return lines


@dataclass
class OperationResult:
    """Structured return value from any gateway operation."""

    success: bool
    paths_touched: list[Path] = field(default_factory=list)
    summary: str = ""
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    no_op: bool = False  # True when idempotent re-run skipped writes
    authorship_report: AuthorshipReport | None = None
    data: dict = field(default_factory=dict)

    def __str__(self) -> str:  # pragma: no cover — debug aid
        if self.success:
            tag = "no-op" if self.no_op else "ok"
            return f"[{tag}] {self.summary}"
        return f"[fail] {'; '.join(self.errors) or self.summary}"


def parse_iso(value: object) -> datetime | None:
    """Parse an ISO-8601 datetime string, returning None on any failure.

    Handles: Z suffix, naive datetimes (assume UTC), date-only strings,
    non-string/None input.  Never raises.
    """
    if not isinstance(value, str) or not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError):
        return None


def write_atomic(path: Path, content: str) -> None:
    """POSIX-atomic write via temp file + rename.

    The temp file is created in the same directory as the target so
    `os.rename` is atomic on the same filesystem. On failure the temp
    file is removed.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    fd, tmp_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    tmp_path = Path(tmp_name)
    try:
        with open(fd, "w") as f:
            f.write(content)
        tmp_path.rename(path)
    except Exception:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass
        raise
