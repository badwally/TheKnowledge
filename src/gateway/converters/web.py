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
import ipaddress
import os
import re
import socket
import urllib.request
from urllib.parse import urljoin, urlparse

import requests
import trafilatura

from gateway import frontmatter as fm
from gateway import validator
from gateway.converters.base import ConversionError, Converter


# --- SSRF guard --------------------------------------------------------------
#
# Ingest accepts arbitrary http(s) URLs from network consumers (the web API).
# Without a guard, a URL whose host resolves to an internal address — loopback
# (http://localhost:7474), link-local cloud metadata (http://169.254.169.254),
# or RFC-1918 ranges (http://10.x, http://192.168.x) — would be fetched
# server-side, an SSRF that can read internal services or instance metadata.
# `_assert_public_url` resolves the host and refuses non-public targets.
# `WIKI_ALLOW_PRIVATE_FETCH=1` overrides for trusted operator ingest of
# genuinely internal URLs (off by default — secure by default).


def _resolve_ips(host: str) -> list[str]:
    """Resolve `host` to its IP literal(s). Thin seam so tests can inject."""
    return [info[4][0] for info in socket.getaddrinfo(host, None)]


def _is_blocked_ip(ip: ipaddress._BaseAddress) -> bool:
    return (
        ip.is_private
        or ip.is_loopback
        or ip.is_link_local
        or ip.is_multicast
        or ip.is_reserved
        or ip.is_unspecified
    )


def _assert_public_url(url: str) -> None:
    """Raise ConversionError if `url` is not an http(s) URL whose host resolves
    exclusively to public addresses. No-op when WIKI_ALLOW_PRIVATE_FETCH is set."""
    if os.environ.get("WIKI_ALLOW_PRIVATE_FETCH"):
        return
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ConversionError(f"refusing to fetch non-http(s) URL: {url}")
    host = parsed.hostname
    if not host:
        raise ConversionError(f"refusing to fetch URL with no host: {url}")
    try:
        ips = _resolve_ips(host)
    except OSError as exc:
        raise ConversionError(f"could not resolve host {host!r}: {exc}") from exc
    if not ips:
        raise ConversionError(f"could not resolve host {host!r}")
    for raw_ip in ips:
        try:
            ip = ipaddress.ip_address(raw_ip.split("%")[0])  # drop v6 scope id
        except ValueError as exc:
            raise ConversionError(
                f"unparseable address {raw_ip!r} for host {host!r}"
            ) from exc
        if _is_blocked_ip(ip):
            raise ConversionError(
                f"refusing to fetch {url}: host {host!r} resolves to non-public "
                f"address {ip}. Set WIKI_ALLOW_PRIVATE_FETCH=1 to allow trusted "
                f"internal URLs."
            )


# --- fetch (redirect-validating; monkeypatch target in tests) ----------------

_FETCH_TIMEOUT = 20  # seconds
_MAX_REDIRECTS = 5
_USER_AGENT = "knowledge-gateway/1.0"


def _fetch(url: str) -> str | None:
    """Fetch `url`, validating EVERY hop against the SSRF guard.

    Redirects are not auto-followed: each ``Location`` is re-checked with
    `_assert_public_url` before we connect to it, so a public host cannot
    redirect the fetch to an internal address (the redirect-bypass class of
    SSRF). DNS rebinding between check and connect remains a residual — see
    the module note — but the redirect vector is closed.
    """
    current = url
    for _ in range(_MAX_REDIRECTS + 1):
        _assert_public_url(current)
        try:
            resp = requests.get(
                current,
                timeout=_FETCH_TIMEOUT,
                allow_redirects=False,
                headers={"User-Agent": _USER_AGENT},
            )
        except requests.RequestException as exc:
            raise ConversionError(f"could not fetch {url}: {exc}") from exc

        if resp.is_redirect or resp.status_code in (301, 302, 303, 307, 308):
            location = resp.headers.get("Location")
            if not location:
                raise ConversionError(f"redirect without Location fetching {url}")
            current = urljoin(current, location)
            continue
        if resp.status_code >= 400:
            raise ConversionError(f"HTTP {resp.status_code} fetching {url}")
        return resp.text

    raise ConversionError(f"too many redirects fetching {url}")


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
