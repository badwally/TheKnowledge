"""Map NotebookLM source IDs back to canonical `raw/<type>/<slug>` pages.

NotebookLM exposes its own opaque source IDs in artifact citations. Wiki
pages must cite their own `[[sources/<slug>]]` (citation-grounding rule
in CLAUDE.md), so we need a translation table.

Strategy:

1. Pull the notebook's source list from NotebookLM (`nlm notebook source
   list <id> --json`).
2. Walk every `raw/<type>/<slug>.md` and index its frontmatter `url` and
   `title`. URL is the strong key; title is a fallback (titles drift, get
   truncated, or collide; URLs are canonical).
3. Match each NLM source by URL first, falling back to title.
4. Cache the resulting map under `nlm/source_maps/<notebook_id>.json` so
   subsequent renders / artifact resolutions don't re-walk `raw/`.

This is a port of `~/code/research-notebook/src/output/source_map.py`,
which matched on title alone. URL-first is strictly more reliable: two
different sources can share a title (e.g., common review paper names
across journals), but URLs are canonical per source.
"""

from __future__ import annotations

import json
import subprocess
from collections.abc import Iterable
from pathlib import Path
from typing import TYPE_CHECKING

from gateway import frontmatter as fm
from gateway import paths

if TYPE_CHECKING:
    from gateway.nlm_client import NlmClient


NLM_CMD: tuple[str, ...] = ("nlm",)
"""Argv prefix for invoking the `nlm` CLI.

Kept as a module-level so tests can monkeypatch it if the executable
location ever needs to change. Production assumes `nlm` is on PATH (same
contract as `NlmCLIClient`).
"""

_FETCH_TIMEOUT_S: float = 30.0

_FILENAME_EXTS: tuple[str, ...] = ("pdf", "md", "m4a", "m4b", "mp3", "wav")
"""Extensions a NotebookLM source title may echo as (the uploaded filename
rather than the human-readable frontmatter title)."""


class SourceMapError(RuntimeError):
    """Raised when the NLM source list cannot be fetched or parsed."""


# --- NLM source listing ----------------------------------------------------


def fetch_nlm_sources(notebook_id: str) -> list[dict]:
    """Return the list of sources in a NotebookLM notebook.

    Each item is the raw JSON dict returned by `nlm notebook source list
    <id> --json` — at minimum `id` and `title`; URL may also be present
    but is not required for matching (we match `raw/` URLs against the
    NLM-side title-or-URL and trust either side).
    """
    args = [*NLM_CMD, "source", "list", notebook_id, "--json"]
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=_FETCH_TIMEOUT_S,
            check=False,
        )
    except FileNotFoundError as e:
        raise SourceMapError(
            f"`{NLM_CMD[0]}` not found on PATH; install notebooklm-mcp-cli"
        ) from e
    except subprocess.TimeoutExpired as e:
        raise SourceMapError(
            f"`{' '.join(args)}` timed out after {_FETCH_TIMEOUT_S}s"
        ) from e

    if result.returncode != 0:
        raise SourceMapError(
            f"`{' '.join(args)}` exited {result.returncode}: "
            f"{result.stderr.strip()[:500] or result.stdout.strip()[:500]}"
        )

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise SourceMapError(
            f"could not parse `{' '.join(args)}` output as JSON: {e}"
        ) from e

    if not isinstance(data, list):
        raise SourceMapError(
            f"expected JSON array from notebook source list, got {type(data).__name__}"
        )
    return data


# --- raw/ index -------------------------------------------------------------


def _index_raw_pages() -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """Walk `raw/<type>/<slug>.md` and bucket by URL, title, and filename.

    Returns `(url_to_path, title_to_path, filename_to_path)`, where each
    path is the canonical relative form `raw/<type>/<slug>` (no extension,
    forward slashes — wikilink-ready).

    The filename index maps patterns like ``<slug>.pdf`` and ``<slug>.md``
    to their path, since NotebookLM titles are often the uploaded filename
    rather than the human-readable title from frontmatter.

    Pages without a parseable frontmatter are skipped silently rather
    than aborting the whole map build; one malformed source shouldn't
    poison every artifact.
    """
    url_to_path: dict[str, str] = {}
    title_to_path: dict[str, str] = {}
    filename_to_path: dict[str, str] = {}

    raw_root = paths.raw_dir()
    if not raw_root.is_dir():
        return url_to_path, title_to_path, filename_to_path

    for source_type in paths.SOURCE_TYPES:
        type_dir = raw_root / source_type
        if not type_dir.is_dir():
            continue
        for md_path in sorted(type_dir.glob("*.md")):
            try:
                front, _ = fm.parse(md_path.read_text(encoding="utf-8"))
            except (fm.FrontmatterError, OSError, UnicodeDecodeError):
                continue

            slug = md_path.stem
            rel = f"raw/{source_type}/{slug}"

            url = front.get("url")
            if isinstance(url, str) and url:
                url_to_path.setdefault(url, rel)

            title = front.get("title")
            if isinstance(title, str) and title:
                title_to_path.setdefault(title, rel)

            for ext in _FILENAME_EXTS:
                filename_to_path.setdefault(f"{slug}.{ext}", rel)

    return url_to_path, title_to_path, filename_to_path


def resolve_raw_sources_by_title(
    titles: Iterable[str],
) -> dict[str, tuple[str | None, str]]:
    """Resolve raw/ pages for `titles` in a single tree walk.

    For each requested title that matches a raw page — by frontmatter
    `title`, else by uploaded filename (``<slug>.<ext>``) — returns
    ``{title: (url, full_text)}``. ``url`` is the frontmatter URL when
    present and non-empty, else None; ``full_text`` is the entire file
    (frontmatter + body), matching what the orchestrator's step-10 push
    sends NotebookLM for URL-less sources. Unmatched titles are absent.

    Exists because NLM's `source list` drops the `url` field for some source
    types (YouTube especially): a promoted session source can arrive
    URL-less even though its materialized raw/ page carries the canonical
    URL. `session.promote` passes the titles of URL-less sources and
    recovers the URL — or, failing that, the real body — so the source is
    added properly rather than as an empty text stub NLM rejects with
    "Please specify a source". Batched (one walk for all titles) so a
    YouTube-heavy promote doesn't re-walk raw/ per source.
    """
    want = set(titles)
    out: dict[str, tuple[str | None, str]] = {}
    if not want:
        return out

    raw_root = paths.raw_dir()
    if not raw_root.is_dir():
        return out

    for source_type in paths.SOURCE_TYPES:
        type_dir = raw_root / source_type
        if not type_dir.is_dir():
            continue
        for md_path in sorted(type_dir.glob("*.md")):
            try:
                text = md_path.read_text(encoding="utf-8")
                front, _ = fm.parse(text)
            except (fm.FrontmatterError, OSError, UnicodeDecodeError):
                continue

            keys: list[str] = []
            title = front.get("title")
            if isinstance(title, str) and title in want:
                keys.append(title)
            slug = md_path.stem
            for ext in _FILENAME_EXTS:
                fn = f"{slug}.{ext}"
                if fn in want:
                    keys.append(fn)
            if not keys:
                continue

            url = front.get("url")
            if not (isinstance(url, str) and url):
                url = None
            for key in keys:
                out.setdefault(key, (url, text))
            if len(out) == len(want):
                return out

    return out


# --- public API -------------------------------------------------------------


def build_source_map(
    notebook_id: str,
    *,
    client: "NlmClient | None" = None,
) -> dict[str, str]:
    """Map NLM source IDs to `raw/<type>/<slug>` paths.

    `client` is accepted for API symmetry with the rest of the gateway
    (every NotebookLM-touching function takes an injectable client) but
    is not used yet — `nlm notebook source list` is not part of the
    `NlmClient` Protocol. When it lands, this function will prefer the
    client over the subprocess call. Until then, passing a mock client
    is a no-op and the subprocess path runs.

    Result is also written to `nlm/source_maps/<notebook_id>.json` so
    subsequent calls can use `load_cached_source_map` instead of
    re-shelling out.
    """
    del client  # reserved for the protocol-bearing future

    nlm_sources = fetch_nlm_sources(notebook_id)
    url_to_path, title_to_path, filename_to_path = _index_raw_pages()

    source_map: dict[str, str] = {}
    for src in nlm_sources:
        nlm_id = src.get("id")
        if not isinstance(nlm_id, str) or not nlm_id:
            continue

        url = src.get("url")
        if isinstance(url, str) and url and url in url_to_path:
            source_map[nlm_id] = url_to_path[url]
            continue

        title = src.get("title")
        if isinstance(title, str) and title:
            if title in title_to_path:
                source_map[nlm_id] = title_to_path[title]
                continue
            if title in filename_to_path:
                source_map[nlm_id] = filename_to_path[title]

    _write_cache(notebook_id, source_map)
    return source_map


def load_cached_source_map(notebook_id: str) -> dict[str, str] | None:
    """Return the cached map for `notebook_id`, or None if absent."""
    cache_path = _cache_path(notebook_id)
    if not cache_path.is_file():
        return None
    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if not isinstance(data, dict):
        return None
    return {str(k): str(v) for k, v in data.items()}


def resolve_citations(
    citations: dict[int, str],
    source_map: dict[str, str],
) -> dict[int, str]:
    """Translate `{citation_num: nlm_source_id}` to `{citation_num: wikilink}`.

    A resolved citation produces `[[sources/<slug>]]` (matches the
    citation-grounding rule in CLAUDE.md — every claim must link to a
    `sources/` page). The slug is the last path component of the
    `raw/<type>/<slug>` entry; the canonical wiki location for every
    raw source is `wiki/sources/<slug>` (one summary per ingested
    source — see CLAUDE.md "Where things live").

    An unresolved citation produces `[[nlm:<source_id>]]`. This is an
    intentional broken wikilink: `wiki lint` can grep for `[[nlm:` and
    surface the gap, and reviewers see the unresolved ID rather than a
    silent drop.
    """
    resolved: dict[int, str] = {}
    for num, nlm_id in citations.items():
        rel = source_map.get(nlm_id)
        if rel:
            slug = rel.rsplit("/", 1)[-1]
            resolved[num] = f"[[sources/{slug}]]"
        else:
            resolved[num] = f"[[nlm:{nlm_id}]]"
    return resolved


# --- cache helpers ----------------------------------------------------------


def _cache_path(notebook_id: str) -> Path:
    return paths.knowledge_root() / "nlm" / "source_maps" / f"{notebook_id}.json"


def _write_cache(notebook_id: str, source_map: dict[str, str]) -> None:
    cache_path = _cache_path(notebook_id)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps(source_map, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
