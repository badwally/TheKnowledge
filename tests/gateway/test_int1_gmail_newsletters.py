"""INT-1: Gmail newsletter poller tests."""

from __future__ import annotations

import email as _email
import email.mime.multipart
import email.mime.text
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.pollers.gmail_newsletters import (
    GmailNewsletterPoller,
    _build_web_id,
    _date_to_ymd,
    _decode_header,
    _extract_text,
    _sender_address,
)


# --- helper: build a minimal RFC-822 bytes message --------------------------


def _make_email(
    subject: str = "Test Newsletter",
    from_: str = "author@substack.com",
    date: str = "Mon, 26 May 2026 08:00:00 +0000",
    body: str = "Newsletter body text.\n",
    msg_id: str = "<test-001@mail.gmail.com>",
) -> bytes:
    msg = _email.mime.text.MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = from_
    msg["Date"] = date
    msg["Message-ID"] = msg_id
    return msg.as_bytes()


def _make_multipart_email(plain: str, html: str) -> bytes:
    msg = _email.mime.multipart.MIMEMultipart("alternative")
    msg["Subject"] = "Multipart Newsletter"
    msg["From"] = "sender@example.com"
    msg["Date"] = "Mon, 26 May 2026 08:00:00 +0000"
    msg.attach(_email.mime.text.MIMEText(plain, "plain"))
    msg.attach(_email.mime.text.MIMEText(html, "html"))
    return msg.as_bytes()


# --- unit tests for helper functions ----------------------------------------


def test_decode_header_plain():
    assert _decode_header("Hello World") == "Hello World"


def test_sender_address_bare():
    assert _sender_address("user@example.com") == "user@example.com"


def test_sender_address_display_name():
    assert _sender_address("Newsletter <news@sub.com>") == "news@sub.com"


def test_date_to_ymd_rfc2822():
    assert _date_to_ymd("Mon, 26 May 2026 08:00:00 +0000") == "2026-05-26"


def test_extract_text_plain():
    raw = _make_email(body="Hello from plain text.\n")
    msg = _email.message_from_bytes(raw)
    text = _extract_text(msg)
    assert "Hello from plain text" in text


def test_extract_text_multipart_picks_plain():
    raw = _make_multipart_email("Plain text body.", "<p>HTML body</p>")
    msg = _email.message_from_bytes(raw)
    text = _extract_text(msg)
    assert "Plain text body" in text
    assert "<p>" not in text


def test_build_web_id_format():
    slug = _build_web_id("https://example.com/article", "2026-05-26")
    assert slug.startswith("web-2026-05-26-")
    assert len(slug) == len("web-2026-05-26-") + 3


# --- GmailNewsletterPoller integration tests --------------------------------


def _mock_imap(messages: list[bytes], uids: list[int]):
    """Build a mock IMAP object that returns given messages."""
    imap = MagicMock()
    uid_bytes = b" ".join(str(u).encode() for u in uids)
    imap.uid.side_effect = _make_imap_uid_side_effect(messages, uids, uid_bytes)
    return imap


def _make_imap_uid_side_effect(messages, uids, uid_bytes):
    call_count = {"n": 0}

    def side_effect(command, *args):
        if command == "SEARCH":
            if uid_bytes:
                return ("OK", [uid_bytes])
            return ("OK", [b""])
        if command == "FETCH":
            idx = call_count["n"] % len(messages)
            call_count["n"] += 1
            raw_uid = args[0]
            uid_int = int(raw_uid)
            msg_bytes = messages[uids.index(uid_int)]
            return ("OK", [(b"", msg_bytes)])
        return ("OK", [])

    return side_effect


def test_poller_missing_credentials(kb_root, monkeypatch):
    monkeypatch.delenv("GMAIL_ADDRESS", raising=False)
    monkeypatch.delenv("GMAIL_APP_PASSWORD", raising=False)
    result = GmailNewsletterPoller().run()
    assert not result.success
    assert "GMAIL_ADDRESS" in result.errors[0]


def test_poller_imap_connect_failure(kb_root, monkeypatch):
    monkeypatch.setenv("GMAIL_ADDRESS", "user@gmail.com")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "testpass")
    with patch("gateway.pollers.gmail_newsletters.imaplib.IMAP4_SSL", side_effect=Exception("Connection refused")):
        result = GmailNewsletterPoller().run()
    assert not result.success
    assert "IMAP" in result.errors[0]


def test_poller_fetches_message(kb_root, monkeypatch):
    monkeypatch.setenv("GMAIL_ADDRESS", "user@gmail.com")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "testpass")

    raw_msg = _make_email(
        subject="My Newsletter",
        from_="author@substack.com",
        body="Newsletter content here.\n",
        msg_id="<unique-001@mail.gmail.com>",
    )

    imap = MagicMock()
    imap.uid.side_effect = [
        ("OK", [b"42"]),
        ("OK", [(b"42 (RFC822 {123})", raw_msg)]),
    ]

    with patch("gateway.pollers.gmail_newsletters.imaplib.IMAP4_SSL", return_value=imap):
        result = GmailNewsletterPoller().run()

    assert result.success
    assert result.fetched == 1

    # Verify the raw file was written
    raw_web = paths.raw_dir() / "web"
    files = list(raw_web.glob("*.md"))
    assert len(files) == 1
    front, body = fm.parse(files[0].read_text())
    assert front["meta"]["source_app"] == "gmail-newsletter"
    assert "Newsletter content here" in body


def test_poller_skips_non_configured_senders(kb_root, monkeypatch):
    monkeypatch.setenv("GMAIL_ADDRESS", "user@gmail.com")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "testpass")

    # Configure to only accept from allowed@example.com
    config_path = paths.knowledge_internal() / "pollers" / "gmail-newsletters" / "config.yaml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text("senders:\n  - address: allowed@example.com\n    domain: test\n")

    raw_msg = _make_email(from_="unknown@other.com", body="Unwanted.\n")
    imap = MagicMock()
    imap.uid.side_effect = [
        ("OK", [b"10"]),
        ("OK", [(b"10 (RFC822 {100})", raw_msg)]),
    ]

    with patch("gateway.pollers.gmail_newsletters.imaplib.IMAP4_SSL", return_value=imap):
        result = GmailNewsletterPoller().run()

    assert result.success
    assert result.fetched == 0
    assert result.skipped == 1


def test_poller_cursor_advances(kb_root, monkeypatch):
    monkeypatch.setenv("GMAIL_ADDRESS", "user@gmail.com")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "testpass")

    raw_msg = _make_email(body="Body.\n", msg_id="<msg-99@gmail.com>")
    imap = MagicMock()
    imap.uid.side_effect = [
        ("OK", [b"99"]),
        ("OK", [(b"99 (RFC822 {100})", raw_msg)]),
    ]

    with patch("gateway.pollers.gmail_newsletters.imaplib.IMAP4_SSL", return_value=imap):
        GmailNewsletterPoller().run()

    poller = GmailNewsletterPoller()
    cursor = poller.read_cursor()
    assert cursor.get("last_uid") == 99


def test_poller_no_messages(kb_root, monkeypatch):
    monkeypatch.setenv("GMAIL_ADDRESS", "user@gmail.com")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "testpass")

    imap = MagicMock()
    imap.uid.return_value = ("OK", [b""])
    imap.uid.side_effect = None

    with patch("gateway.pollers.gmail_newsletters.imaplib.IMAP4_SSL", return_value=imap):
        result = GmailNewsletterPoller().run()

    assert result.success
    assert result.fetched == 0


def test_poller_registered():
    from gateway.pollers import list_pollers
    assert "gmail-newsletters" in list_pollers()
