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

    def _fencing_dir(self) -> Path:
        """Durable per-intent fencing counter (C3, ROBUSTNESS-6).

        The highest issued fencing token is persisted here, OUTSIDE the
        per-state queue record, so the stale-token rejection still holds after a
        crash that loses the queue record. ``claim()`` advances it atomically;
        ``fencing_token()`` reads it.
        """
        return self._root / "fencing"

    def _next_fencing_token(self, intent_id: str) -> int:
        """Atomically advance and return the durable fencing counter (C3).

        Implemented as an O_CREAT|O_EXCL bump under the commit-side never sees a
        lower value: read current durable max, write max+1 via a rename, retry on
        a concurrent writer. The durable file survives queue-record deletion.
        """
        fdir = self._fencing_dir()
        fdir.mkdir(parents=True, exist_ok=True)
        counter = fdir / f"{intent_id}.txt"
        while True:
            current = self._durable_fencing(intent_id)
            nxt = current + 1
            fd, tmp_name = tempfile.mkstemp(dir=fdir, prefix=f".{intent_id}.", suffix=".tmp")
            tmp_path = Path(tmp_name)
            try:
                with open(fd, "w") as f:
                    f.write(str(nxt))
                # os.replace is atomic; last writer wins. Re-read to confirm we
                # did not regress below a concurrent claimer's value.
                tmp_path.replace(counter)
            except Exception:
                if tmp_path.exists():
                    try:
                        tmp_path.unlink()
                    except OSError:
                        pass
                raise
            if self._durable_fencing(intent_id) >= nxt:
                return nxt

    def _durable_fencing(self, intent_id: str) -> int:
        """Highest fencing token ever issued for ``intent_id``, or 0."""
        counter = self._fencing_dir() / f"{intent_id}.txt"
        try:
            return int(counter.read_text().strip())
        except (OSError, ValueError):
            return 0

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
        """Claim the oldest submitted intent; issue fencing token + lease (C3).

        The acquire primitive is ``os.replace`` of the submitted intent file
        into ``claimed/`` (SILENT-CORRUPTION-7): rename is atomic, so exactly one
        of N concurrent claimers wins the move and the losers get
        ``FileNotFoundError`` and try the next candidate. The fencing token is
        derived from durable monotonic state (``_next_fencing_token``), advanced
        only by the winner, never from an ``old+1`` of a shared concurrent read.
        """
        now = time.time() if now is None else now
        sub_dir = self._state_dir("submitted")
        claimed_dir = self._state_dir("claimed")
        if not sub_dir.exists():
            return None
        claimed_dir.mkdir(parents=True, exist_ok=True)

        def _mtime(p: Path) -> float:
            # A concurrent claimer may move p between glob and stat; treat a
            # vanished candidate as oldest so it is tried (and skipped) first.
            try:
                return p.stat().st_mtime
            except OSError:
                return -1.0

        candidates = sorted(
            (p for p in sub_dir.glob("*.json") if not p.name.startswith(".")),
            key=_mtime,
        )
        for src in candidates:
            dst = claimed_dir / src.name
            try:
                # Atomic acquire: exactly one concurrent claimer wins this rename.
                os.replace(src, dst)
            except (FileNotFoundError, OSError):
                continue  # lost the race for this candidate; try the next one.
            try:
                with open(dst) as f:
                    rec = json.load(f)
            except FileNotFoundError:
                continue
            intent_id = rec["intent_id"]
            # Monotonic fencing token from durable state — survives record loss.
            token = self._next_fencing_token(intent_id)
            rec["fencing_token"] = token
            rec["lease_deadline"] = now + lease_ttl
            _atomic_write_json(dst, rec)
            return Claim(
                intent=self._to_intent(rec),
                fencing_token=token,
                lease_deadline=rec["lease_deadline"],
            )
        return None

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

    def set_declared_writes(self, intent_id: str, rel_paths: list[str]) -> None:
        """Durably record the write set an intent is about to apply (BLOCKER-1).

        The commit gate records this BEFORE touching the working tree so crash
        recovery can scope its revert to exactly these paths — never a tree-wide
        ``reset --hard`` / ``clean -fd`` that would destroy unrelated sessions'
        and the watcher's uncommitted/untracked work.
        """
        found = self._find(intent_id)
        if found is None:
            raise KeyError(intent_id)
        _, path = found
        with open(path) as f:
            rec = json.load(f)
        rec["declared_writes"] = list(rel_paths)
        _atomic_write_json(path, rec)

    def declared_writes(self, intent_id: str) -> list[str]:
        """Return the durably-recorded declared write set for ``intent_id``."""
        read = self._read(intent_id)
        return list(read[1].get("declared_writes", [])) if read else []

    def in_flight_intents(self) -> list[str]:
        """Intent ids currently claimed or authored (mid-flight, not committed)."""
        ids: list[str] = []
        for state in ("claimed", "authored"):
            d = self._state_dir(state)
            if not d.exists():
                continue
            for p in d.glob("*.json"):
                if not p.name.startswith("."):
                    ids.append(p.stem)
        return ids

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
        """Highest fencing token issued for ``intent_id`` (C3, ROBUSTNESS-6).

        Reads the durable per-intent counter, which survives a crash that loses
        the queue record — so the stale-token rejection in the commit gate still
        holds for a resurrected worker even after the record is gone. Returns
        ``None`` only if no token was ever issued (and no record exists).
        """
        durable = self._durable_fencing(intent_id)
        if durable > 0:
            return durable
        read = self._read(intent_id)
        return int(read[1].get("fencing_token", 0)) if read else None
