"""Append-only JSONL log of authorship contradictions (M42).

Each line is one Contradiction record with a `recorded_at` timestamp.
The Review console's Contradictions tab reads this log; M38's
apply_plan writes to it on every successful plan that has contradictions.

POSIX guarantees writes < PIPE_BUF (~4KB) appended via O_APPEND are
atomic; each record fits well under 4KB. No locking needed.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Iterable, TYPE_CHECKING

from gateway import paths

if TYPE_CHECKING:
    from gateway.plan import Contradiction


def log_path():
    return paths.knowledge_root() / ".knowledge" / "contradictions" / "log.jsonl"


def append_contradictions(contradictions: "Iterable[Contradiction]") -> int:
    """Append one JSONL record per contradiction. Returns count appended."""
    items = list(contradictions)
    if not items:
        return 0

    target = log_path()
    target.parent.mkdir(parents=True, exist_ok=True)

    recorded_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with target.open("a", encoding="utf-8") as f:
        for c in items:
            record = {
                "source_id": c.source_id,
                "existing_page": c.existing_page,
                "existing_claim": c.existing_claim,
                "new_claim": c.new_claim,
                "severity": c.severity,
                "recorded_at": recorded_at,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(items)


def read_records() -> list[dict]:
    """Read all records from the log. Tolerates malformed lines (skips them).

    Returns records sorted by `recorded_at` descending (newest first).
    """
    target = log_path()
    if not target.is_file():
        return []
    out: list[dict] = []
    for line in target.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            out.append(obj)
    out.sort(key=lambda r: r.get("recorded_at", ""), reverse=True)
    return out
