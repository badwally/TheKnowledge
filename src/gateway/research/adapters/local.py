"""Local-files search adapter for `wiki research`.

Enumerates user-supplied paths (directories or globs) and emits one
`CandidateItem` per file that has a registered converter. Unsupported
files are silently skipped — the user-curated set acts as a hand-picked
input; the relevance filter runs downstream against file *content*, so
the adapter does not need to score by query.

Contract notes:
- The `query` argument is intentionally unused. The adapter enumerates
  the curated set; the semantic filter narrows it later.
- `max_results=None` means unlimited (do not cap user-curated input).
- Each emitted item carries `source_type` matching the converter that
  will materialize it, so the orchestrator can dispatch without a
  second round of detection.
"""

from __future__ import annotations

import glob
import hashlib
from pathlib import Path

from gateway import converters
from gateway.research.adapters.base import CandidateItem


def _hash_path(absolute_path: str, length: int = 12) -> str:
    """Stable short id derived from the absolute path."""
    return hashlib.sha1(absolute_path.encode("utf-8")).hexdigest()[:length]


def _is_glob(pattern: str) -> bool:
    return any(ch in pattern for ch in ("*", "?", "[")) or "**" in pattern


def _expand(path: str) -> list[Path]:
    """Expand a single user-supplied path entry to a list of files.

    Rules:
    - A glob pattern (contains `*`, `?`, or `[`) is matched via `glob.glob`
      with `recursive=True` so `**` works as expected.
    - A directory is walked recursively.
    - A file is returned as-is.
    - Non-existent entries yield no files.
    """
    expanded = Path(path).expanduser()
    if _is_glob(str(expanded)):
        matches = glob.glob(str(expanded), recursive=True)
        return [Path(m) for m in matches if Path(m).is_file()]
    if expanded.is_dir():
        return [p for p in expanded.rglob("*") if p.is_file()]
    if expanded.is_file():
        return [expanded]
    return []


def _converter_for(path: Path):
    """Return the converter that handles `path`, or None if unsupported.

    Uses the same `dispatch` registry the ingest pipeline does so the
    adapter can never disagree with downstream materialization about
    which converter owns a file extension.
    """
    try:
        return converters.dispatch(str(path))
    except converters.NoConverterError:
        return None


class LocalAdapter:
    """Enumerate user-supplied local files into CandidateItems.

    `paths` is the list passed via `--include-local` (repeatable); each
    entry may be a directory, file, or glob pattern.
    """

    name = "local"

    def __init__(self, paths: list[str]) -> None:
        self.paths = list(paths)

    def search(
        self,
        query: str,
        *,
        filter_hints: dict | None = None,
        max_results: int | None = None,
    ) -> list[CandidateItem]:
        seen: set[str] = set()
        items: list[CandidateItem] = []

        for entry in self.paths:
            for raw_path in _expand(entry):
                try:
                    abs_path = str(raw_path.resolve())
                except OSError:
                    continue
                if abs_path in seen:
                    continue
                seen.add(abs_path)

                converter = _converter_for(raw_path)
                if converter is None:
                    continue

                source_type = getattr(converter, "type_name", "") or "other"
                try:
                    size_bytes = raw_path.stat().st_size
                except OSError:
                    size_bytes = 0

                title = raw_path.stem or raw_path.name

                items.append(
                    CandidateItem(
                        item_id=_hash_path(abs_path),
                        source_type=source_type,
                        url=f"file://{abs_path}",
                        title=title,
                        authors=[],
                        publish_date=None,
                        description="",
                        content_type=source_type,
                        source_metadata={
                            "absolute_path": abs_path,
                            "size_bytes": size_bytes,
                        },
                    )
                )

                if max_results is not None and len(items) >= max_results:
                    return items

        return items


__all__ = ["LocalAdapter"]
