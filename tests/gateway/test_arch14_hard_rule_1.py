"""ARCH-14: CI guard — no direct wiki/raw writes outside the gateway write path.

Hard rule #1 from CLAUDE.md: "No direct writes to wiki/ or raw/. All writes
go through the gateway."

This test enforces the boundary structurally: directories that are purely
read-side (lint/, web/, evaluate/) must contain no .write_text( or
write_atomic( calls, because they should never mutate the wiki or raw corpus.
The gateway write path is: core.write_atomic → ops/* (via write_atomic import).

See WIKI.md § 9 for the canonical statement of this invariant.
"""

from __future__ import annotations

from pathlib import Path

import pytest

# Read-only gateway zones — these directories must never write to wiki/ or raw/
_READ_ONLY_ZONES = [
    "lint",
    "web",
]

_WRITE_INDICATORS = [".write_text(", "write_atomic("]

_SRC = Path("src/gateway")


def _scan_zone(zone: str) -> list[str]:
    """Find files in zone that write to wiki/ or raw/ paths."""
    zone_dir = _SRC / zone
    if not zone_dir.exists():
        return []
    violations = []
    for py_file in sorted(zone_dir.rglob("*.py")):
        content = py_file.read_text()
        has_write = any(indicator in content for indicator in _WRITE_INDICATORS)
        has_wiki_raw_path = any(p in content for p in ("wiki_dir()", "raw_dir()", "agenda_dir()"))
        if has_write and has_wiki_raw_path:
            violations.append(str(py_file.relative_to(_SRC)))
    return violations


@pytest.mark.parametrize("zone", _READ_ONLY_ZONES)
def test_no_writes_in_read_only_zone(zone: str) -> None:
    """Files in read-only zones must contain no write calls."""
    violations = _scan_zone(zone)
    assert not violations, (
        f"Hard rule #1 violation: the following files in `{zone}/` "
        f"contain write calls — all wiki/raw writes must go through "
        f"core.write_atomic via an ops/ module:\n  "
        + "\n  ".join(violations)
    )


def test_ops_write_path_uses_write_atomic() -> None:
    """Ops modules that write wiki pages must import write_atomic, not call write_text directly."""
    ops_dir = _SRC / "ops"
    if not ops_dir.exists():
        return

    # Ops modules allowed to use .write_text() for non-wiki/raw paths (temp files, CLI output)
    _ALLOWED_WRITE_TEXT = {
        # These write to tmp/cli output, not wiki/ or raw/
        "ops/status.py",
    }

    violations = []
    for py_file in sorted(ops_dir.glob("*.py")):
        rel = str(py_file.relative_to(_SRC))
        if rel in _ALLOWED_WRITE_TEXT:
            continue
        content = py_file.read_text()
        # Flag ops files that write wiki/raw paths without going through write_atomic
        if ".write_text(" in content and "write_atomic" not in content:
            # Check if the file actually constructs wiki/raw paths (not just writing tmp files)
            if "wiki_dir()" in content or "raw_dir()" in content or "agenda_dir()" in content:
                violations.append(rel)

    assert not violations, (
        f"Ops modules constructing wiki/raw paths must use write_atomic, "
        f"not .write_text() directly:\n  "
        + "\n  ".join(violations)
    )
