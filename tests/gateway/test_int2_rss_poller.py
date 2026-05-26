"""INT-2: RSS/Atom feed poller tests."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.pollers.rss import RSSPoller, _parse_date, _parse_feed, _strip_tags


# --- helper: minimal RSS/Atom XML blobs -------------------------------------


_RSS_SINGLE = b"""<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <title>Test Feed</title>
    <item>
      <title>Article One</title>
      <link>https://example.com/article-one</link>
      <guid>https://example.com/article-one</guid>
      <pubDate>Mon, 26 May 2026 08:00:00 +0000</pubDate>
      <description>Summary of article one.</description>
      <author>author@example.com</author>
    </item>
  </channel>
</rss>
"""

_RSS_TWO_ITEMS = b"""<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <item>
      <title>First</title>
      <link>https://example.com/first</link>
      <guid>guid-001</guid>
      <pubDate>Mon, 25 May 2026 08:00:00 +0000</pubDate>
      <description>First item.</description>
    </item>
    <item>
      <title>Second</title>
      <link>https://example.com/second</link>
      <guid>guid-002</guid>
      <pubDate>Tue, 26 May 2026 08:00:00 +0000</pubDate>
      <description>Second item.</description>
    </item>
  </channel>
</rss>
"""

_ATOM_SINGLE = b"""<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Atom Test</title>
  <entry>
    <id>https://example.com/atom-entry-1</id>
    <title>Atom Entry One</title>
    <link href="https://example.com/atom-entry-1"/>
    <published>2026-05-26T08:00:00Z</published>
    <summary>Atom summary here.</summary>
    <author><name>Jane Doe</name></author>
  </entry>
</feed>
"""

_EMPTY_RSS = b"""<?xml version="1.0"?>
<rss version="2.0"><channel></channel></rss>
"""


# --- unit tests for helpers -------------------------------------------------


def test_parse_date_rfc2822():
    iso, ymd = _parse_date("Mon, 26 May 2026 08:00:00 +0000")
    assert iso.startswith("2026-05-26")
    assert ymd == "2026-05-26"


def test_parse_date_iso8601():
    iso, ymd = _parse_date("2026-05-26T08:00:00Z")
    assert iso.startswith("2026-05-26")
    assert ymd == "2026-05-26"


def test_parse_date_empty_returns_now():
    iso, ymd = _parse_date("")
    assert len(iso) > 0
    assert len(ymd) == 10  # YYYY-MM-DD


def test_strip_tags():
    assert _strip_tags("<p>Hello <b>world</b></p>") == "Hello world"
    assert _strip_tags("plain text") == "plain text"


def test_parse_feed_rss():
    entries = _parse_feed(_RSS_SINGLE)
    assert len(entries) == 1
    assert entries[0]["title"] == "Article One"
    assert "example.com/article-one" in entries[0]["link"]
    assert "Summary of article one" in entries[0]["summary"]


def test_parse_feed_rss_two_items():
    entries = _parse_feed(_RSS_TWO_ITEMS)
    assert len(entries) == 2


def test_parse_feed_atom():
    entries = _parse_feed(_ATOM_SINGLE)
    assert len(entries) == 1
    assert entries[0]["title"] == "Atom Entry One"
    assert entries[0]["author"] == "Jane Doe"


def test_parse_feed_empty():
    entries = _parse_feed(_EMPTY_RSS)
    assert entries == []


def test_parse_feed_bad_xml():
    entries = _parse_feed(b"not xml at all <unclosed")
    assert entries == []


# --- RSSPoller integration tests --------------------------------------------


def _write_feeds_config(kb_root: Path, feeds: list[dict]) -> None:
    import yaml
    p = paths.knowledge_internal() / "pollers" / "rss" / "feeds.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump({"feeds": feeds}))


def test_poller_no_config_returns_success(kb_root):
    result = RSSPoller().run()
    assert result.success
    assert "no feeds configured" in result.summary


def test_poller_fetches_rss_item(kb_root):
    _write_feeds_config(kb_root, [{"name": "test-feed", "url": "https://example.com/feed.xml", "domain": "tech"}])

    with patch.object(RSSPoller, "_fetch_feed", return_value=_RSS_SINGLE):
        result = RSSPoller().run()

    assert result.success
    assert result.fetched == 1

    files = list((paths.raw_dir() / "web").glob("*.md"))
    assert len(files) == 1
    front, body = fm.parse(files[0].read_text())
    assert front["meta"]["source_app"] == "rss"
    assert front["meta"]["feed_name"] == "test-feed"
    assert front["domains"] == ["tech"]
    assert "Summary of article one" in body


def test_poller_fetches_atom_item(kb_root):
    _write_feeds_config(kb_root, [{"name": "atom-feed", "url": "https://example.com/atom.xml", "domain": ""}])

    with patch.object(RSSPoller, "_fetch_feed", return_value=_ATOM_SINGLE):
        result = RSSPoller().run()

    assert result.success
    assert result.fetched == 1


def test_poller_skips_duplicate_slugs(kb_root):
    _write_feeds_config(kb_root, [{"name": "feed", "url": "https://example.com/feed.xml", "domain": ""}])

    with patch.object(RSSPoller, "_fetch_feed", return_value=_RSS_SINGLE):
        first = RSSPoller().run()
    with patch.object(RSSPoller, "_fetch_feed", return_value=_RSS_SINGLE):
        second = RSSPoller().run()

    assert first.fetched == 1
    assert second.fetched == 0
    assert second.skipped >= 1


def test_poller_cursor_written_after_fetch(kb_root):
    _write_feeds_config(kb_root, [{"name": "myfeed", "url": "https://x.com/feed", "domain": ""}])

    with patch.object(RSSPoller, "_fetch_feed", return_value=_RSS_SINGLE):
        RSSPoller().run()

    cursor = RSSPoller().read_cursor()
    assert "myfeed" in cursor
    assert cursor["myfeed"].get("last_guid")


def test_poller_fetch_error_reported(kb_root):
    _write_feeds_config(kb_root, [{"name": "bad-feed", "url": "https://bad.example/feed", "domain": ""}])

    with patch.object(RSSPoller, "_fetch_feed", side_effect=Exception("timeout")):
        result = RSSPoller().run()

    assert not result.success
    assert any("fetch error" in e for e in result.errors)


def test_poller_multiple_feeds(kb_root):
    _write_feeds_config(kb_root, [
        {"name": "feed-a", "url": "https://a.com/feed", "domain": ""},
        {"name": "feed-b", "url": "https://b.com/feed", "domain": ""},
    ])

    feed_b = b"""<?xml version="1.0"?>
<rss version="2.0"><channel>
  <item>
    <title>From Feed B</title>
    <link>https://b.com/unique-article</link>
    <guid>https://b.com/unique-article</guid>
    <pubDate>Mon, 26 May 2026 10:00:00 +0000</pubDate>
    <description>Feed B unique content.</description>
  </item>
</channel></rss>"""

    responses = {"https://a.com/feed": _RSS_SINGLE, "https://b.com/feed": feed_b}

    def _side_effect(url):
        return responses[url]

    with patch.object(RSSPoller, "_fetch_feed", side_effect=_side_effect):
        result = RSSPoller().run()

    assert result.success
    assert result.fetched == 2


def test_poller_registered():
    from gateway.pollers import list_pollers
    assert "rss" in list_pollers()
