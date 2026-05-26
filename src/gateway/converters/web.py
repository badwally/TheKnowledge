"""Web converter: URL → canonical markdown via trafilatura readability.

Detects HTTP(S) URLs. Fetches the page, extracts main content as markdown,
pulls out title/author/date metadata, and assembles a canonical source per
WIKI.md § 3 (type=web).

Binary sidecars are not produced (web pages are text-only). Image handling
is deferred — see WIKI.md tips on image clipping for future work.

Trafilatura calls go through the small `_fetch / _extract_markdown /
_extract_metadata` helpers in this module so tests can monkeypatch them
without touching trafilatura globally.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import re
import urllib.request
from urllib.parse import urlparse

import trafilatura

from gateway import frontmatter as fm
from gateway import validator
from gateway.converters.base import ConversionError, Converter


# --- thin trafilatura adapters (monkeypatch targets in tests) ----------------

def _fetch(url: str) -> str | None:
    return trafilatura.fetch_url(url)


# --- Wayback Machine adapter (monkeypatch target in tests) -------------------

_WAYBACK_SAVE = "https://web.archive.org/save/{url}"
_WAYBACK_TIMEOUT = 15  # seconds


def _wayback_snapshot(url: str) -> str | None:
    """POST to Wayback Machine save API; return the archive URL or None on failure."""
    try:
        save_url = _WAYBACK_SAVE.format(url=url)
        req = urllib.request.Request(save_url, method="POST")
        req.add_header("User-Agent", "knowledge-gateway/1.0")
        with urllib.request.urlopen(req, timeout=_WAYBACK_TIMEOUT) as resp:
            return resp.geturl()
    except Exception:
        return None


def _extract_markdown(html: str) -> str | None:
    return trafilatura.extract(
        html,
        output_format="markdown",
        include_comments=False,
        include_tables=True,
    )


def _extract_metadata(html: str):  # returns trafilatura Document or None
    return trafilatura.extract_metadata(html)


# -----------------------------------------------------------------------------


_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")


def _normalize_date(raw: str | None) -> str | None:
    """Coerce trafilatura's date string into 'YYYY-MM-DD' or return None."""
    if not raw:
        return None
    m = _DATE_RE.match(str(raw))
    if not m:
        return None
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"


def _build_id(url: str, published_at: str | None) -> str:
    """Generate a canonical web ID per WIKI.md § 6.1: web-<YYYY-MM-DD>-<3hex>."""
    date_str = published_at or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:3]
    return f"web-{date_str}-{url_hash}"


def _site_from_url(url: str) -> str:
    return urlparse(url).netloc.lstrip("www.") or url


def _coerce_authors(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x) for x in value if x]
    return [str(value)]


def _reading_time_minutes(body: str) -> int:
    words = len(body.split())
    return max(1, round(words / 220))  # rough average reading speed


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class WebConverter(Converter):
    type_name = "web"

    def detect(self, source: str) -> bool:
        return source.startswith(("http://", "https://"))

    def convert(self, source: str) -> str:
        html = _fetch(source)
        if not html:
            raise ConversionError(f"could not fetch {source}")

        body = _extract_markdown(html)
        if not body or not body.strip():
            raise ConversionError(f"no extractable content at {source}")
        body = body.rstrip("\n") + "\n"

        meta = _extract_metadata(html)
        meta_dict = meta.as_dict() if hasattr(meta, "as_dict") else (meta or {})

        title = meta_dict.get("title") or source
        published_at = _normalize_date(meta_dict.get("date"))
        authors = _coerce_authors(meta_dict.get("author"))
        excerpt = (meta_dict.get("description") or "").strip()
        if len(excerpt) > 400:
            excerpt = excerpt[:397] + "..."

        source_id = _build_id(source, published_at)

        archive_url = _wayback_snapshot(source)  # graceful: None on failure

        meta_block: dict = {
            "source_app": "trafilatura",
            "site": _site_from_url(source),
            "excerpt": excerpt,
            "reading_time_minutes": _reading_time_minutes(body),
        }
        if archive_url:
            meta_block["archive_url"] = archive_url

        front = {
            "id": source_id,
            "type": "web",
            "title": title,
            "url": source,
            "authors": authors,
            "published_at": published_at,
            "ingested_at": _now_iso(),
            "content_hash": validator.compute_content_hash(body),
            "domains": [],
            "nlm_corpus_ids": [],
            "wiki_pages": [],
            "meta": meta_block,
        }
        # Drop None published_at (it's optional; emitting null in YAML is ugly)
        if front["published_at"] is None:
            del front["published_at"]

        return fm.serialize(front, body)
