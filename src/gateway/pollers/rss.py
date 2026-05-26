"""RSS poller (INT-2).

Fetches entries from one or more RSS/Atom feeds configured in
.knowledge/pollers/rss/feeds.yaml and writes each new item to raw/web/.
Uses stdlib urllib.request + xml.etree.ElementTree (no feedparser dep).

Feed config: .knowledge/pollers/rss/feeds.yaml
  feeds:
    - name: stratechery
      url: https://stratechery.com/feed/
      domain: tech-strategy    # optional default domain tag
    - name: acmqueue
      url: https://queue.acm.org/rss/feeds/queuefeatures.xml
      domain: ""

Cursor: .knowledge/pollers/rss/cursor.yaml
  <feed-name>:
    last_guid: <str>
    last_pubdate: <ISO-8601>

Slug format: web-<YYYY-MM-DD>-<sha256[:3]> matching WIKI.md § 6.1.
"""

from __future__ import annotations

import hashlib
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

import yaml

from gateway import frontmatter as fm, paths, validator
from gateway.pollers.base import Poller, PollerResult


_REQUEST_TIMEOUT = 20


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_web_id(url: str, date_str: str) -> str:
    url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:3]
    return f"web-{date_str}-{url_hash}"


def _parse_date(value: str) -> tuple[str, str]:
    """Parse RSS/Atom date string. Returns (iso_str, ymd_str)."""
    if not value:
        now = datetime.now(timezone.utc)
        return now.strftime("%Y-%m-%dT%H:%M:%SZ"), now.strftime("%Y-%m-%d")
    # Try RFC-2822 (RSS) first
    try:
        dt = parsedate_to_datetime(value)
        dt = dt.astimezone(timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ"), dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    # Try ISO-8601 (Atom)
    try:
        clean = re.sub(r"Z$", "+00:00", value)
        dt = datetime.fromisoformat(clean).astimezone(timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ"), dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%SZ"), now.strftime("%Y-%m-%d")


def _strip_tags(text: str) -> str:
    """Remove HTML/XML tags from a string."""
    return re.sub(r"<[^>]+>", "", text).strip()


def _ns(tag: str, namespaces: dict[str, str]) -> list[str]:
    """Expand tag with each namespace prefix; return all variants."""
    variants = [tag]
    for uri in namespaces.values():
        variants.append(f"{{{uri}}}{tag}")
    return variants


def _text(elem: ET.Element | None) -> str:
    if elem is None:
        return ""
    return (elem.text or "").strip()


def _find_text(parent: ET.Element, *tags: str) -> str:
    for tag in tags:
        child = parent.find(tag)
        if child is not None and child.text:
            return child.text.strip()
    return ""


def _parse_feed(xml_bytes: bytes) -> list[dict[str, str]]:
    """Parse RSS 2.0 or Atom 1.0 XML. Return list of entry dicts."""
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return []

    tag = root.tag.lower()
    # Strip namespace from root tag
    local = re.sub(r"\{[^}]+\}", "", root.tag).lower()

    entries: list[dict[str, str]] = []

    if local == "feed":
        # Atom 1.0
        for entry in root.iter():
            entry_local = re.sub(r"\{[^}]+\}", "", entry.tag).lower()
            if entry_local != "entry":
                continue
            guid = _find_text(entry, "id", "{http://www.w3.org/2005/Atom}id")
            title_elem = entry.find("{http://www.w3.org/2005/Atom}title")
            if title_elem is None:
                title_elem = entry.find("title")
            title = _strip_tags(_text(title_elem))
            link_elem = entry.find("{http://www.w3.org/2005/Atom}link")
            if link_elem is None:
                link_elem = entry.find("link")
            link = ""
            if link_elem is not None:
                link = link_elem.get("href") or _text(link_elem)
            pub_elem = entry.find("{http://www.w3.org/2005/Atom}published")
            if pub_elem is None:
                pub_elem = entry.find("{http://www.w3.org/2005/Atom}updated")
            if pub_elem is None:
                pub_elem = entry.find("published")
            if pub_elem is None:
                pub_elem = entry.find("updated")
            pubdate = _text(pub_elem)
            summary_elem = entry.find("{http://www.w3.org/2005/Atom}summary")
            if summary_elem is None:
                summary_elem = entry.find("{http://www.w3.org/2005/Atom}content")
            if summary_elem is None:
                summary_elem = entry.find("summary")
            if summary_elem is None:
                summary_elem = entry.find("content")
            summary = _strip_tags(_text(summary_elem))
            author_elem = entry.find("{http://www.w3.org/2005/Atom}author")
            author = ""
            if author_elem is not None:
                name_elem = author_elem.find("{http://www.w3.org/2005/Atom}name")
                if name_elem is None:
                    name_elem = author_elem.find("name")
                author = _text(name_elem)
            entries.append({
                "guid": guid or link,
                "title": title,
                "link": link,
                "pubdate": pubdate,
                "summary": summary,
                "author": author,
            })
    else:
        # RSS 2.0 — items are inside channel
        channel = root.find("channel") or root
        for item in channel.findall("item"):
            guid_elem = item.find("guid")
            guid = _text(guid_elem) if guid_elem is not None else ""
            title = _strip_tags(_find_text(item, "title"))
            link = _find_text(item, "link")
            pubdate = _find_text(item, "pubDate", "published", "date")
            desc_elem = item.find("description")
            if desc_elem is None:
                desc_elem = item.find("content:encoded")
            summary = _strip_tags(_text(desc_elem))
            author = _find_text(item, "author", "dc:creator", "creator")
            entries.append({
                "guid": guid or link,
                "title": title,
                "link": link,
                "pubdate": pubdate,
                "summary": summary,
                "author": author,
            })

    return entries


class RSSPoller(Poller):
    name = "rss"
    source_type = "web"

    def _feeds_config_path(self) -> Path:
        return paths.knowledge_internal() / "pollers" / "rss" / "feeds.yaml"

    def _load_feeds(self) -> list[dict[str, Any]]:
        p = self._feeds_config_path()
        if not p.exists():
            return []
        try:
            data = yaml.safe_load(p.read_text()) or {}
        except yaml.YAMLError:
            return []
        return data.get("feeds") or []

    def _fetch_feed(self, url: str) -> bytes:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "wiki-rss-poller/1.0"},
        )
        with urllib.request.urlopen(req, timeout=_REQUEST_TIMEOUT) as resp:
            return resp.read()

    def run(self) -> PollerResult:
        feeds = self._load_feeds()
        if not feeds:
            return PollerResult(
                success=True,
                summary="rss: no feeds configured — add entries to .knowledge/pollers/rss/feeds.yaml",
            )

        cursor = self.read_cursor()
        total_fetched = 0
        total_skipped = 0
        errors: list[str] = []
        new_cursor: dict[str, Any] = dict(cursor)

        for feed_cfg in feeds:
            feed_name = str(feed_cfg.get("name") or "")
            feed_url = str(feed_cfg.get("url") or "")
            domain = str(feed_cfg.get("domain") or "")
            if not feed_url:
                errors.append(f"feed {feed_name!r}: missing url")
                continue

            feed_cursor = cursor.get(feed_name) or {}
            last_guid = str(feed_cursor.get("last_guid") or "")
            last_pubdate = str(feed_cursor.get("last_pubdate") or "")

            try:
                xml_bytes = self._fetch_feed(feed_url)
            except Exception as e:
                errors.append(f"feed {feed_name!r}: fetch error — {e!r}")
                continue

            entries = _parse_feed(xml_bytes)
            fetched = 0
            skipped = 0
            latest_guid = last_guid
            latest_pubdate = last_pubdate

            for entry in entries:
                guid = entry.get("guid") or entry.get("link") or ""
                if not guid:
                    skipped += 1
                    continue

                # Skip entries we've already seen by GUID
                if guid == last_guid:
                    skipped += 1
                    continue
                pubdate_raw = entry.get("pubdate") or ""
                iso_pub, ymd = _parse_date(pubdate_raw)

                # Skip entries older than last_pubdate
                if last_pubdate and iso_pub <= last_pubdate and guid != "":
                    skipped += 1
                    continue

                title = entry.get("title") or "Untitled"
                link = entry.get("link") or guid
                summary = entry.get("summary") or ""
                author = entry.get("author") or ""

                slug = _build_web_id(link or guid, ymd)
                body = f"## Summary\n\n{summary}\n" if summary else "## Summary\n\n_(no summary)_\n"

                front: dict[str, Any] = {
                    "id": slug,
                    "type": "web",
                    "title": title,
                    "url": link,
                    "authors": [author] if author else [],
                    "published_at": ymd,
                    "ingested_at": _now_iso(),
                    "content_hash": validator.compute_content_hash(body),
                    "domains": [domain] if domain else [],
                    "nlm_corpus_ids": [],
                    "wiki_pages": [],
                    "meta": {
                        "source_app": "rss",
                        "feed_name": feed_name,
                        "feed_url": feed_url,
                        "guid": guid,
                    },
                }

                target = paths.raw_source_path("web", slug)
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    skipped += 1
                else:
                    self.write_raw(slug, fm.serialize(front, body))
                    fetched += 1

                if not latest_pubdate or iso_pub > latest_pubdate:
                    latest_pubdate = iso_pub
                    latest_guid = guid

            new_cursor[feed_name] = {
                "last_guid": latest_guid,
                "last_pubdate": latest_pubdate,
            }
            total_fetched += fetched
            total_skipped += skipped

        self.write_cursor(new_cursor)

        return PollerResult(
            success=len(errors) == 0,
            fetched=total_fetched,
            skipped=total_skipped,
            errors=errors,
            summary=f"rss: {total_fetched} fetched, {total_skipped} skipped, {len(errors)} errors",
        )
