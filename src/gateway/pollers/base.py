"""Poller ABC for API-only sources (Apple Notes, Notion, Slack, Gmail, …).

A `Poller` runs on a schedule (cron / launchd) and fetches new items from a
source API, writing each to `raw/<type>/<canonical-id>.md`. The watcher (M4)
or `wiki ingest` then picks up from there — pollers do not call the
gateway's ingest pipeline directly; they just produce canonical markdown
files in `raw/`, which is the same contract converters use.

Cursor state (last-synced timestamp/ID per source) lives at
`.knowledge/pollers/<source-name>/cursor.yaml` so re-runs only fetch what's
new.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from gateway import paths


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class PollerResult:
    success: bool
    fetched: int = 0
    skipped: int = 0
    errors: list[str] = None  # type: ignore[assignment]
    summary: str = ""

    def __post_init__(self) -> None:
        if self.errors is None:
            self.errors = []


class Poller(ABC):
    """Subclasses implement `name`, `source_type`, and `run()`.

    `run()` returns a `PollerResult`. Cursor state read/written via
    `read_cursor()` / `write_cursor()`.
    """

    name: str = ""
    source_type: str = ""  # one of paths.SOURCE_TYPES

    @abstractmethod
    def run(self) -> PollerResult: ...

    # --- cursor helpers ----------------------------------------------------

    def cursor_path(self) -> Path:
        return paths.knowledge_internal() / "pollers" / self.name / "cursor.yaml"

    def read_cursor(self) -> dict[str, Any]:
        path = self.cursor_path()
        if not path.exists():
            return {}
        try:
            data = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError:
            return {}
        return data if isinstance(data, dict) else {}

    def write_cursor(self, data: dict[str, Any]) -> None:
        path = self.cursor_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {**data, "updated_at": _now_iso()}
        path.write_text(yaml.safe_dump(payload, sort_keys=False, default_flow_style=False))

    # --- writing items into raw/ ------------------------------------------

    def write_raw(self, canonical_id: str, canonical_text: str) -> Path:
        """Write `canonical_text` to `raw/<source_type>/<canonical_id>.md`."""
        target = paths.raw_source_path(self.source_type, canonical_id)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(canonical_text)
        return target
