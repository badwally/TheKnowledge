"""nlm/notebooks.yaml: domain ↔ NotebookLM notebook ID map per WIKI § 13.1.

The registry is the single record of which NotebookLM notebook backs each
domain. `wiki nlm-add` consults it to find the right corpus; `wiki nlm-slides`
et al. use it to know which notebook to ask. The file is human-readable and
git-tracked.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from gateway import paths


def notebooks_yaml_path() -> Path:
    return paths.nlm_dir() / "notebooks.yaml"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class NotebookEntry:
    domain: str
    notebook_id: str
    created_at: str
    sources_count: int = 0
    last_sync: str = ""


def load() -> dict[str, NotebookEntry]:
    """Load the registry. Empty file/dict is fine; returns {} in that case."""
    path = notebooks_yaml_path()
    if not path.exists():
        return {}

    data = yaml.safe_load(path.read_text()) or {}
    notebooks = data.get("notebooks", {}) or {}
    out: dict[str, NotebookEntry] = {}
    for domain, fields in notebooks.items():
        if not isinstance(fields, dict):
            continue
        out[domain] = NotebookEntry(
            domain=domain,
            notebook_id=str(fields.get("notebook_id", "")),
            created_at=str(fields.get("created_at", "")),
            sources_count=int(fields.get("sources_count", 0)),
            last_sync=str(fields.get("last_sync", "")),
        )
    return out


def save(entries: dict[str, NotebookEntry]) -> None:
    """Atomically write the registry."""
    path = notebooks_yaml_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data: dict[str, Any] = {"notebooks": {}}
    for domain, entry in sorted(entries.items()):
        data["notebooks"][domain] = {
            "notebook_id": entry.notebook_id,
            "created_at": entry.created_at,
            "sources_count": entry.sources_count,
            "last_sync": entry.last_sync,
        }
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(yaml.safe_dump(data, sort_keys=False, default_flow_style=False))
    tmp.rename(path)


def get_notebook_id(domain: str) -> str | None:
    entry = load().get(domain)
    return entry.notebook_id if entry else None


def register(domain: str, notebook_id: str) -> NotebookEntry:
    """Add (or overwrite) a notebook entry for a domain."""
    entries = load()
    entry = NotebookEntry(
        domain=domain,
        notebook_id=notebook_id,
        created_at=entries[domain].created_at if domain in entries else _now_iso(),
        sources_count=entries[domain].sources_count if domain in entries else 0,
        last_sync=_now_iso(),
    )
    entries[domain] = entry
    save(entries)
    return entry


def increment_sources(domain: str, by: int = 1) -> None:
    entries = load()
    if domain not in entries:
        return
    entries[domain].sources_count += by
    entries[domain].last_sync = _now_iso()
    save(entries)


def update_last_sync(domain: str) -> None:
    entries = load()
    if domain not in entries:
        return
    entries[domain].last_sync = _now_iso()
    save(entries)
