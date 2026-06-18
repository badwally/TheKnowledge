"""Session lifecycle helpers for `wiki research`.

A "session" is a short-lived NotebookLM notebook spun up for one research
prompt. It pulls in fresh search-adapter results, runs the analysis loop,
and — on success — its sources are *promoted* into the persistent
domain notebook so future queries see them.

The lifecycle states live in `gateway.nlm_registry`:

- `ephemeral` — registered, not yet finished
- `promoted`  — analysis succeeded, sources rolled into the domain corpus
- `abandoned` — analysis or filing failed; session stays for forensics

The orchestrator drives these transitions; this module isolates the
session-id derivation, the dedup-by-URL promotion, and the abandon path
so they can be unit-tested without spinning up the whole orchestrator.

Per CLAUDE.md the gateway is the only sanctioned path to NotebookLM,
which is why `promote` takes an `NlmClient` (the same Protocol the rest
of the gateway speaks) rather than shelling out itself.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from gateway.research import source_map as _source_map

if TYPE_CHECKING:
    from gateway.nlm_client import NlmClient


__all__ = ["make_session_id", "promote", "abandon"]


# --- session id ------------------------------------------------------------


_SLUG_RE = re.compile(r"[^a-z0-9]+")
_DEFAULT_DATE_FN = lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d")  # noqa: E731


def make_session_id(prompt: str, *, today: str | None = None) -> str:
    """Build a stable, dated, slugged session id.

    Format: ``<YYYY-MM-DD>-<slug-of-prompt>``, e.g.
    ``2026-04-29-glp1-cardiovascular``.

    The slug is lowercase, hyphenated, punctuation-stripped, and capped
    at six words. An empty prompt falls back to ``query`` so the id is
    always well-formed.

    `today` is injectable for deterministic tests; production callers
    should leave it unset.
    """
    date = today or _DEFAULT_DATE_FN()
    cleaned = _SLUG_RE.sub("-", prompt.lower()).strip("-")
    words = [w for w in cleaned.split("-") if w]
    slug = "-".join(words[:6]) or "query"
    return f"{date}-{slug}"


# --- promotion -------------------------------------------------------------


def promote(
    domain: str,
    session_id: str,
    *,
    persistent_notebook_id: str,
    session_notebook_id: str,
    client: "NlmClient",
    nlm_registry,
) -> tuple[int, list[tuple[str, str]]]:
    """Push session sources into the persistent notebook. Dedup by URL.

    Steps:
      1. Fetch the session-notebook source list (via `source_map.fetch_nlm_sources`).
      2. Fetch the persistent-notebook source list.
      3. For each session source not already in the persistent corpus
         (URL-keyed where available, title-keyed otherwise), call
         `client.source_add_url` (or `source_add_text` for sources
         without a URL). Per-source failures are collected, not raised —
         one stale URL must not sink promotion of the remaining N-1.
      4. Mark the session promoted in the registry, bumping the
         persistent corpus's `sources_count` by the number actually added.

    Returns ``(added, failed)`` where ``added`` is the count of
    newly-added sources and ``failed`` is a list of ``(target, error)``
    pairs (target = url or title).

    Fundamental failures (e.g. fetch_nlm_sources / mark_promoted raising)
    propagate to the caller.
    """
    session_sources = _source_map.fetch_nlm_sources(session_notebook_id)
    persistent_sources = _source_map.fetch_nlm_sources(persistent_notebook_id)

    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    for src in persistent_sources:
        url = src.get("url")
        if isinstance(url, str) and url:
            seen_urls.add(url)
        title = src.get("title")
        if isinstance(title, str) and title:
            seen_titles.add(title)

    # NLM's `source list` drops the `url` field for some source types
    # (YouTube especially), so a session source can arrive URL-less even
    # though its materialized raw/ page carries the canonical URL. Resolve
    # those raw pages by title in one tree walk so we can recover the URL
    # (and, failing that, the real body content) — otherwise the text
    # fallback below sends an empty source and NLM rejects it with "Please
    # specify a source".
    urlless_titles: list[str] = []
    for src in session_sources:
        url = src.get("url")
        if isinstance(url, str) and url:
            continue
        title = src.get("title")
        if isinstance(title, str) and title:
            urlless_titles.append(title)
    recovered = _source_map.resolve_raw_sources_by_title(urlless_titles)

    added = 0
    failed: list[tuple[str, str]] = []
    for src in session_sources:
        url = src.get("url")
        if not (isinstance(url, str) and url):
            url = None
        title = src.get("title")
        if not (isinstance(title, str) and title):
            title = None

        # Recover a URL — and, as a second resort, real body content — from
        # the raw page NLM round-tripped, keyed by title.
        recovered_content: str | None = None
        if url is None and title is not None:
            raw_url, raw_text = recovered.get(title, (None, None))
            if raw_url:
                url = raw_url
            elif raw_text:
                recovered_content = raw_text

        if url is not None:
            if url in seen_urls:
                continue
            try:
                client.source_add_url(persistent_notebook_id, url)
            except Exception as e:  # noqa: BLE001 — per-source isolation
                failed.append((url, str(e)))
                continue
            seen_urls.add(url)
            added += 1
            continue
        # No URL — fall back to title-keyed dedup + text add. Prefer the
        # real raw content; title-only (content="") remains the last resort
        # for NLM-native sources with no raw/ page.
        if title is not None:
            if title in seen_titles:
                continue
            try:
                client.source_add_text(
                    persistent_notebook_id,
                    content=recovered_content or "",
                    title=title,
                )
            except Exception as e:  # noqa: BLE001 — per-source isolation
                failed.append((title, str(e)))
                continue
            seen_titles.add(title)
            added += 1

    nlm_registry.mark_promoted(domain, session_id, sources_added=added)
    return added, failed


# --- abandon ---------------------------------------------------------------


def abandon(domain: str, session_id: str, *, nlm_registry) -> None:
    """Mark a session abandoned in the registry.

    The NotebookLM notebook itself is *not* deleted — that is reserved
    for a future `wiki nlm-cleanup` op (out of scope here). Keeping the
    notebook around lets the user inspect what was loaded when a run
    fails partway through.
    """
    nlm_registry.mark_abandoned(domain, session_id)
