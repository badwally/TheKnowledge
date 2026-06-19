"""Append-only JSONL log of authorship contradictions (M42).

Each line is one Contradiction record with a `recorded_at` timestamp.
The Review console's Contradictions tab reads this log; M38's
apply_plan writes to it on every successful plan that has contradictions.

POSIX guarantees writes < PIPE_BUF (~4KB) appended via O_APPEND are
atomic; each record fits well under 4KB. No locking needed.
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
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


def resolution_acts_path():
    return (
        paths.knowledge_root() / ".knowledge" / "contradictions"
        / "resolution_acts.jsonl"
    )


def _compute_act_id(record: dict) -> str:
    """Content-addressed, stable id for a resolution act (Phase 5 T1, G1/G3).

    Derived from the winner+loser sources/claims and the resolved_at timestamp
    so a given resolution has one stable handle the reversal can name. SHA-256
    prefix; collision-resistant enough for the act population."""
    winner = record.get("winner", {}) or {}
    loser = record.get("loser", {}) or {}
    basis = json.dumps(
        {
            "winner": [winner.get("source"), winner.get("claim")],
            "loser": [loser.get("source"), loser.get("claim")],
            "resolved_at": record.get("resolved_at"),
            "policy_version": record.get("policy_version"),
        },
        sort_keys=True,
        ensure_ascii=True,
    )
    return "act-" + hashlib.sha256(basis.encode("utf-8")).hexdigest()[:16]


def append_resolution_act(act: dict) -> None:
    """Append one reversible auto-resolution act (Phase-3 Task 7, decision 6).

    Append-only JSONL: the act records inputs, the rule, the policy version, the
    winner and loser, and a timestamp — enough to reverse the resolution. A stable
    content-addressed ``act_id`` is stamped so the reversal can name it (G1/G3).
    POSIX O_APPEND of a < PIPE_BUF record is atomic; no locking needed."""
    target = resolution_acts_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    record = dict(act)
    record.setdefault(
        "resolved_at",
        datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
    record.setdefault("act_id", _compute_act_id(record))
    with target.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def find_act(act_id: str) -> dict | None:
    """Return the resolution act with the given act_id, or None."""
    for act in read_resolution_acts():
        if act.get("act_id") == act_id:
            return act
    return None


def mark_act_reverted(act_id: str, revert_intent_id: str) -> bool:
    """Rewrite the matched act in place to mark it reverted (G3 re-open).

    Adds a ``reverts_act`` marker so ``retraction.acts_to_reopen`` no longer
    re-returns it. The JSONL is gitignored derived state, so an in-place rewrite
    (read-all → mutate → atomic replace) is acceptable. Returns True if a matching
    act was found and updated."""
    target = resolution_acts_path()
    if not target.is_file():
        return False
    lines = target.read_text(encoding="utf-8").splitlines()
    found = False
    out: list[str] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            out.append(line)
            continue
        if isinstance(obj, dict) and obj.get("act_id") == act_id and "reverts_act" not in obj:
            obj["reverts_act"] = revert_intent_id
            found = True
        out.append(json.dumps(obj, ensure_ascii=False))
    if not found:
        return False
    # Atomic replace
    fd, tmp_name = tempfile.mkstemp(dir=target.parent, prefix=f".{target.name}.", suffix=".tmp")
    try:
        with open(fd, "w", encoding="utf-8") as f:
            f.write("\n".join(out) + "\n")
        os.replace(tmp_name, target)
    except Exception:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise
    return True


def read_resolution_acts() -> list[dict]:
    target = resolution_acts_path()
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
    return out


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
