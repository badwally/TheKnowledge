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

This module supplies the shared primitives (atomic write, OperationResult).
Operation modules under `gateway/ops/` implement the specific contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import tempfile
from typing import TYPE_CHECKING

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

    def __str__(self) -> str:  # pragma: no cover — debug aid
        if self.success:
            tag = "no-op" if self.no_op else "ok"
            return f"[{tag}] {self.summary}"
        return f"[fail] {'; '.join(self.errors) or self.summary}"


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
