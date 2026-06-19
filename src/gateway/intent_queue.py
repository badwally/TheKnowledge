"""Durable intent queue — Librarian Phase 1 (T1.1).

The intent queue is the deposit path (C7) and the durable lifecycle state
machine (design §3.2). It generalizes ``raw/inbox/`` into a watched directory
of intent files, but encodes the lifecycle states as **durable on-disk facts**
(one subdirectory per state) — NOT in-memory like ``watcher.py``'s ``_pending``
dict (``watcher.py:78``), which loses acked work on a crash (decision 14).

Storage layout (under ``.knowledge/intents/``)::

    submitted/<intent_id>.json
    claimed/<intent_id>.json
    authored/<intent_id>.json
    committed/<intent_id>.json
    rejected/<intent_id>.json
    dead_lettered/<intent_id>.json

State transitions move the JSON file between subdirectories with ``os.replace``
(atomic within a filesystem). Each intent file carries its fencing token
(monotonic per intent_id, C3) and lease deadline («commit.lease_ttl»).

This module holds NO threshold constants beyond the documented defaults
(«commit.lease_ttl» = 120s); callers pass policy values in.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import os
from pathlib import Path
import tempfile
import time
from typing import Any

from gateway import paths


STATES: tuple[str, ...] = (
    "submitted",
    "claimed",
    "authored",
    "committed",
    "rejected",
    "dead_lettered",
)

# Default «commit.lease_ttl» (ledger §1.1). Callers may override.
DEFAULT_LEASE_TTL = 120.0


@dataclass(frozen=True)
class Intent:
    """A declarative, immutable, content-addressed deposit record (design §3)."""

    intent_id: str
    payload: dict
    identity: dict
    head_oid: str | None = None
    depends_on: str | None = None


@dataclass(frozen=True)
class Claim:
    """The result of claiming a submitted intent: intent + fencing + lease."""

    intent: Intent
    fencing_token: int
    lease_deadline: float


def _canonical(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def compute_intent_id(
    payload: dict, identity: dict, *, semantics: str = "deposit"
) -> str:
    """Content-addressed id over (payload, identity, semantics).

    The idempotency key (decision 3, C2): re-presenting the same logical
    deposit yields the same ``intent_id``.
    """
    digest = hashlib.sha256(
        _canonical([semantics, payload, identity]).encode("utf-8")
    ).hexdigest()
    return digest[:16]


def _atomic_write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    tmp_path = Path(tmp_name)
    try:
        with open(fd, "w") as f:
            json.dump(obj, f, sort_keys=True)
        tmp_path.replace(path)
    except Exception:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass
        raise


class IntentQueue:
    """Durable, restart-surviving intent queue."""

    def __init__(self, root: Path | None = None):
        self._root = root or paths.intents_dir()

    # --- layout ---------------------------------------------------------

    def _state_dir(self, state: str) -> Path:
        if state not in STATES:
            raise ValueError(f"unknown intent state: {state!r}")
        return self._root / state

    def _find(self, intent_id: str) -> tuple[str, Path] | None:
        for state in STATES:
            p = self._state_dir(state) / f"{intent_id}.json"
            if p.exists():
                return state, p
        return None

    # --- serialization --------------------------------------------------

    @staticmethod
    def _to_record(intent: Intent, *, fencing_token: int = 0,
                   lease_deadline: float = 0.0,
                   result: dict | None = None) -> dict:
        return {
            "intent_id": intent.intent_id,
            "payload": intent.payload,
            "identity": intent.identity,
            "head_oid": intent.head_oid,
            "depends_on": intent.depends_on,
            "fencing_token": fencing_token,
            "lease_deadline": lease_deadline,
            "result": result or {},
        }

    @staticmethod
    def _to_intent(rec: dict) -> Intent:
        return Intent(
            intent_id=rec["intent_id"],
            payload=rec["payload"],
            identity=rec["identity"],
            head_oid=rec.get("head_oid"),
            depends_on=rec.get("depends_on"),
        )

    def _read(self, intent_id: str) -> tuple[str, dict] | None:
        found = self._find(intent_id)
        if found is None:
            return None
        state, path = found
        with open(path) as f:
            return state, json.load(f)

    # --- API ------------------------------------------------------------

    def submit(self, intent: Intent) -> str:
        """Durably enqueue an intent to ``submitted/`` before returning (decision 3)."""
        rec = self._to_record(intent)
        path = self._state_dir("submitted") / f"{intent.intent_id}.json"
        _atomic_write_json(path, rec)
        return intent.intent_id

    def claim(self, *, lease_ttl: float = DEFAULT_LEASE_TTL,
              now: float | None = None) -> Claim | None:
        """Claim the oldest submitted intent; issue fencing token + lease (C3)."""
        now = time.time() if now is None else now
        sub_dir = self._state_dir("submitted")
        if not sub_dir.exists():
            return None
        candidates = sorted(
            (p for p in sub_dir.glob("*.json") if not p.name.startswith(".")),
            key=lambda p: p.stat().st_mtime,
        )
        if not candidates:
            return None
        src = candidates[0]
        with open(src) as f:
            rec = json.load(f)
        rec["fencing_token"] = int(rec.get("fencing_token", 0)) + 1
        rec["lease_deadline"] = now + lease_ttl
        dst = self._state_dir("claimed") / src.name
        _atomic_write_json(dst, rec)
        src.unlink()
        return Claim(
            intent=self._to_intent(rec),
            fencing_token=rec["fencing_token"],
            lease_deadline=rec["lease_deadline"],
        )

    def renew(self, intent_id: str, *, lease_ttl: float = DEFAULT_LEASE_TTL,
              now: float | None = None) -> bool:
        """Heartbeat-renew a claimed intent's lease so live work is not reclaimed."""
        now = time.time() if now is None else now
        found = self._find(intent_id)
        if found is None or found[0] != "claimed":
            return False
        _, path = found
        with open(path) as f:
            rec = json.load(f)
        rec["lease_deadline"] = now + lease_ttl
        _atomic_write_json(path, rec)
        return True

    def reclaim_expired(self, *, now: float | None = None) -> list[str]:
        """Return claimed intents whose lease expired to ``submitted`` (C3 reclaim)."""
        now = time.time() if now is None else now
        reclaimed: list[str] = []
        claimed_dir = self._state_dir("claimed")
        if not claimed_dir.exists():
            return reclaimed
        for path in list(claimed_dir.glob("*.json")):
            if path.name.startswith("."):
                continue
            with open(path) as f:
                rec = json.load(f)
            if float(rec.get("lease_deadline", 0.0)) < now:
                dst = self._state_dir("submitted") / path.name
                _atomic_write_json(dst, rec)
                path.unlink()
                reclaimed.append(rec["intent_id"])
        return reclaimed

    def set_state(self, intent_id: str, state: str,
                  *, result: dict | None = None) -> None:
        """Move an intent to ``state`` (durable transition)."""
        found = self._find(intent_id)
        if found is None:
            raise KeyError(intent_id)
        cur, path = found
        with open(path) as f:
            rec = json.load(f)
        if result is not None:
            rec["result"] = {**rec.get("result", {}), **result}
        dst = self._state_dir(state) / path.name
        if dst != path:
            _atomic_write_json(dst, rec)
            path.unlink()
        else:
            _atomic_write_json(path, rec)

    def set_result(self, intent_id: str, result: dict) -> None:
        """Merge terminal-disposition metadata into the intent record."""
        found = self._find(intent_id)
        if found is None:
            raise KeyError(intent_id)
        _, path = found
        with open(path) as f:
            rec = json.load(f)
        rec["result"] = {**rec.get("result", {}), **result}
        _atomic_write_json(path, rec)

    def get_state(self, intent_id: str) -> str | None:
        found = self._find(intent_id)
        return found[0] if found else None

    def load(self, intent_id: str) -> Intent | None:
        read = self._read(intent_id)
        return self._to_intent(read[1]) if read else None

    def get_result(self, intent_id: str) -> dict:
        read = self._read(intent_id)
        return dict(read[1].get("result", {})) if read else {}

    def fencing_token(self, intent_id: str) -> int | None:
        read = self._read(intent_id)
        return int(read[1].get("fencing_token", 0)) if read else None
