"""nlm/notebooks.yaml: domain ↔ NotebookLM notebook ID map per WIKI § 13.1.

The registry is the single record of which NotebookLM notebooks back each
domain. A domain has:

- exactly one **persistent** notebook (the long-lived corpus; what
  `wiki nlm-add` and the artifact ops target), and
- zero or more **session** notebooks (ephemeral spin-ups for a focused
  query; see `notebook_query`). Each session tracks status (`ephemeral`,
  `promoted`, `abandoned`), so callers can list active sessions, mark them
  promoted (rolling sources back to the persistent corpus) or abandoned.

The on-disk schema is nested under each domain:

    obesity:
      persistent:
        notebook_id: nb_abc123
        created_at: 2025-12-01
        sources_count: 47
        last_sync: 2026-04-29T14:00:00Z
      sessions:
        - session_id: 2026-04-29-glp1-cardiovascular
          notebook_id: nb_xyz789
          query: "..."
          created_at: 2026-04-29T14:00:00Z
          status: ephemeral   # ephemeral | promoted | abandoned
          sources_count: 12
          promoted_at: null

For backwards compatibility, the loader also accepts the legacy flat
schema (notebook_id/created_at/sources_count/last_sync at the domain
level) and treats it as the persistent entry. The next write normalizes
the file to the nested schema.

`wiki nlm-add` consults this registry to find the right corpus;
`wiki nlm-slides` et al. use it to know which notebook to ask. The file
is human-readable and git-tracked.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from gateway import paths
from gateway.locking import file_lock


# --- valid session statuses -----------------------------------------------

EPHEMERAL = "ephemeral"
PROMOTED = "promoted"
ABANDONED = "abandoned"
_VALID_STATUSES: frozenset[str] = frozenset({EPHEMERAL, PROMOTED, ABANDONED})

# Lock name for any write to the registry. Reads are unlocked.
_REGISTRY_LOCK = "nlm-registry"


def notebooks_yaml_path() -> Path:
    return paths.nlm_dir() / "notebooks.yaml"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --- in-memory model -------------------------------------------------------


@dataclass
class NotebookEntry:
    """The persistent entry for a domain.

    Kept as a flat dataclass so existing callers can keep using
    `entry.notebook_id`, `entry.sources_count`, `entry.last_sync`, etc.
    """

    domain: str
    notebook_id: str
    created_at: str
    sources_count: int = 0
    last_sync: str = ""


@dataclass
class SessionEntry:
    """An ephemeral session notebook for a domain."""

    session_id: str
    notebook_id: str
    query: str
    created_at: str
    status: str = EPHEMERAL
    sources_count: int = 0
    promoted_at: str | None = None


@dataclass
class DomainRecord:
    """Full registry record for a domain: persistent + sessions."""

    domain: str
    persistent: NotebookEntry | None = None
    sessions: list[SessionEntry] = field(default_factory=list)


# --- low-level read/write -------------------------------------------------


def _coerce_persistent(domain: str, fields: dict[str, Any]) -> NotebookEntry:
    return NotebookEntry(
        domain=domain,
        notebook_id=str(fields.get("notebook_id", "")),
        created_at=str(fields.get("created_at", "")),
        sources_count=int(fields.get("sources_count", 0) or 0),
        last_sync=str(fields.get("last_sync", "")),
    )


def _coerce_session(fields: dict[str, Any]) -> SessionEntry | None:
    session_id = fields.get("session_id")
    notebook_id = fields.get("notebook_id")
    if not session_id or not notebook_id:
        return None
    status = str(fields.get("status", EPHEMERAL))
    if status not in _VALID_STATUSES:
        status = EPHEMERAL
    promoted_at = fields.get("promoted_at")
    return SessionEntry(
        session_id=str(session_id),
        notebook_id=str(notebook_id),
        query=str(fields.get("query", "")),
        created_at=str(fields.get("created_at", "")),
        status=status,
        sources_count=int(fields.get("sources_count", 0) or 0),
        promoted_at=str(promoted_at) if promoted_at else None,
    )


def _load_records() -> dict[str, DomainRecord]:
    """Read raw YAML and build DomainRecord per domain.

    Accepts both the legacy flat schema and the new nested schema.
    """
    path = notebooks_yaml_path()
    if not path.exists():
        return {}

    data = yaml.safe_load(path.read_text()) or {}
    notebooks = data.get("notebooks", {}) or {}
    out: dict[str, DomainRecord] = {}
    for domain, fields in notebooks.items():
        if not isinstance(fields, dict):
            continue

        record = DomainRecord(domain=domain)

        if "persistent" in fields or "sessions" in fields:
            # New nested schema.
            persistent_fields = fields.get("persistent")
            if isinstance(persistent_fields, dict) and persistent_fields.get("notebook_id"):
                record.persistent = _coerce_persistent(domain, persistent_fields)
            sessions_field = fields.get("sessions") or []
            if isinstance(sessions_field, list):
                for sf in sessions_field:
                    if not isinstance(sf, dict):
                        continue
                    sess = _coerce_session(sf)
                    if sess is not None:
                        record.sessions.append(sess)
        else:
            # Legacy flat schema: domain-level keys are the persistent entry.
            if fields.get("notebook_id"):
                record.persistent = _coerce_persistent(domain, fields)

        out[domain] = record
    return out


def _serialize_records(records: dict[str, DomainRecord]) -> dict[str, Any]:
    data: dict[str, Any] = {"notebooks": {}}
    for domain, record in sorted(records.items()):
        domain_block: dict[str, Any] = {}
        if record.persistent is not None:
            domain_block["persistent"] = {
                "notebook_id": record.persistent.notebook_id,
                "created_at": record.persistent.created_at,
                "sources_count": record.persistent.sources_count,
                "last_sync": record.persistent.last_sync,
            }
        if record.sessions:
            domain_block["sessions"] = [
                {
                    "session_id": s.session_id,
                    "notebook_id": s.notebook_id,
                    "query": s.query,
                    "created_at": s.created_at,
                    "status": s.status,
                    "sources_count": s.sources_count,
                    "promoted_at": s.promoted_at,
                }
                for s in record.sessions
            ]
        data["notebooks"][domain] = domain_block
    return data


def _write_records(records: dict[str, DomainRecord]) -> None:
    """Atomically write the registry. Caller holds the registry lock."""
    path = notebooks_yaml_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data = _serialize_records(records)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(yaml.safe_dump(data, sort_keys=False, default_flow_style=False))
    tmp.rename(path)


# --- public API: persistent notebooks (legacy-compatible) -----------------


def load() -> dict[str, NotebookEntry]:
    """Load the registry as a domain → persistent-entry map.

    Preserved verbatim from the original API. Domains that exist only as
    a session-bearing record (no persistent notebook yet) are omitted, as
    they were under the old schema.
    """
    return {
        domain: record.persistent
        for domain, record in _load_records().items()
        if record.persistent is not None
    }


def save(entries: dict[str, NotebookEntry]) -> None:
    """Write a domain → persistent-entry map.

    Sessions for any domain present in `entries` are preserved; sessions
    for domains absent from `entries` are dropped (matching old `save`
    semantics where the argument was the full registry).
    """
    with file_lock(_REGISTRY_LOCK):
        existing = _load_records()
        out: dict[str, DomainRecord] = {}
        for domain, entry in entries.items():
            prev = existing.get(domain)
            sessions = prev.sessions if prev is not None else []
            out[domain] = DomainRecord(
                domain=domain,
                persistent=entry,
                sessions=sessions,
            )
        _write_records(out)


def get_notebook_id(domain: str) -> str | None:
    """Return persistent notebook_id for the domain, else None."""
    return get_persistent(domain)


def get_persistent(domain: str) -> str | None:
    """Return persistent notebook_id for the domain, else None."""
    record = _load_records().get(domain)
    if record is None or record.persistent is None:
        return None
    return record.persistent.notebook_id or None


def register(domain: str, notebook_id: str) -> NotebookEntry:
    """Add (or overwrite) the persistent notebook for a domain."""
    with file_lock(_REGISTRY_LOCK):
        records = _load_records()
        prev = records.get(domain)
        prev_persistent = prev.persistent if prev is not None else None
        entry = NotebookEntry(
            domain=domain,
            notebook_id=notebook_id,
            created_at=prev_persistent.created_at if prev_persistent else _now_iso(),
            sources_count=prev_persistent.sources_count if prev_persistent else 0,
            last_sync=_now_iso(),
        )
        record = prev if prev is not None else DomainRecord(domain=domain)
        record.persistent = entry
        records[domain] = record
        _write_records(records)
        return entry


def increment_sources(domain: str, by: int = 1) -> None:
    with file_lock(_REGISTRY_LOCK):
        records = _load_records()
        record = records.get(domain)
        if record is None or record.persistent is None:
            return
        record.persistent.sources_count += by
        record.persistent.last_sync = _now_iso()
        _write_records(records)


def update_last_sync(domain: str) -> None:
    with file_lock(_REGISTRY_LOCK):
        records = _load_records()
        record = records.get(domain)
        if record is None or record.persistent is None:
            return
        record.persistent.last_sync = _now_iso()
        _write_records(records)


# --- public API: sessions --------------------------------------------------


def _session_to_dict(s: SessionEntry) -> dict[str, Any]:
    return {
        "session_id": s.session_id,
        "notebook_id": s.notebook_id,
        "query": s.query,
        "created_at": s.created_at,
        "status": s.status,
        "sources_count": s.sources_count,
        "promoted_at": s.promoted_at,
    }


def get_session(domain: str, session_id: str) -> dict[str, Any] | None:
    """Return session dict for (domain, session_id), else None."""
    record = _load_records().get(domain)
    if record is None:
        return None
    for s in record.sessions:
        if s.session_id == session_id:
            return _session_to_dict(s)
    return None


def list_sessions(
    domain: str, *, status: str | None = None
) -> list[dict[str, Any]]:
    """List sessions for a domain, optionally filtered by status."""
    if status is not None and status not in _VALID_STATUSES:
        raise ValueError(
            f"invalid status {status!r}; expected one of {sorted(_VALID_STATUSES)}"
        )
    record = _load_records().get(domain)
    if record is None:
        return []
    sessions: Iterable[SessionEntry] = record.sessions
    if status is not None:
        sessions = (s for s in sessions if s.status == status)
    return [_session_to_dict(s) for s in sessions]


def register_session(
    domain: str,
    session_id: str,
    notebook_id: str,
    *,
    query: str,
) -> None:
    """Register a new ephemeral session notebook for a domain.

    Raises ValueError if a session with the same id already exists for the
    domain. The domain need not already have a persistent notebook.
    """
    with file_lock(_REGISTRY_LOCK):
        records = _load_records()
        record = records.get(domain) or DomainRecord(domain=domain)
        for s in record.sessions:
            if s.session_id == session_id:
                raise ValueError(
                    f"session {session_id!r} already registered for domain {domain!r}"
                )
        record.sessions.append(
            SessionEntry(
                session_id=session_id,
                notebook_id=notebook_id,
                query=query,
                created_at=_now_iso(),
                status=EPHEMERAL,
                sources_count=0,
                promoted_at=None,
            )
        )
        records[domain] = record
        _write_records(records)


def mark_promoted(domain: str, session_id: str, *, sources_added: int) -> None:
    """Mark a session promoted; bump persistent sources_count by sources_added.

    Raises KeyError if the session (or domain) does not exist.
    """
    with file_lock(_REGISTRY_LOCK):
        records = _load_records()
        record = records.get(domain)
        if record is None:
            raise KeyError(f"unknown domain {domain!r}")
        target: SessionEntry | None = None
        for s in record.sessions:
            if s.session_id == session_id:
                target = s
                break
        if target is None:
            raise KeyError(
                f"unknown session {session_id!r} for domain {domain!r}"
            )
        target.status = PROMOTED
        target.promoted_at = _now_iso()
        if record.persistent is not None:
            record.persistent.sources_count += sources_added
            record.persistent.last_sync = _now_iso()
        _write_records(records)


def mark_abandoned(domain: str, session_id: str) -> None:
    """Mark a session abandoned. Raises KeyError if not found."""
    with file_lock(_REGISTRY_LOCK):
        records = _load_records()
        record = records.get(domain)
        if record is None:
            raise KeyError(f"unknown domain {domain!r}")
        target: SessionEntry | None = None
        for s in record.sessions:
            if s.session_id == session_id:
                target = s
                break
        if target is None:
            raise KeyError(
                f"unknown session {session_id!r} for domain {domain!r}"
            )
        target.status = ABANDONED
        _write_records(records)


def increment_session_sources(
    domain: str, session_id: str, *, n: int = 1
) -> None:
    """Bump sources_count on a session entry. Raises KeyError if not found."""
    with file_lock(_REGISTRY_LOCK):
        records = _load_records()
        record = records.get(domain)
        if record is None:
            raise KeyError(f"unknown domain {domain!r}")
        for s in record.sessions:
            if s.session_id == session_id:
                s.sources_count += n
                _write_records(records)
                return
        raise KeyError(
            f"unknown session {session_id!r} for domain {domain!r}"
        )
