"""Gmail newsletter poller (INT-1).

Connects to Gmail via IMAP (imaplib stdlib). Fetches newsletters from
configured senders and writes each message to raw/web/ as a canonical
web source with meta.source_app: gmail-newsletter.

Auth:
  GMAIL_ADDRESS        — full Gmail address
  GMAIL_APP_PASSWORD   — 16-char App Password (Gmail Settings → Security →
                         App Passwords; requires 2FA enabled)

Sender config: .knowledge/pollers/gmail-newsletters/config.yaml
  senders:
    - address: newsletter@substack.com
      domain: my-domain       # optional default domain tag
    - address: digest@example.com
      domain: ""
  label: INBOX               # optional; default INBOX
  max_messages: 50           # per run; default 50

Cursor: .knowledge/pollers/gmail-newsletters/cursor.yaml
  last_uid: <int>            # highest UID fetched so far

Slug format: web-<YYYY-MM-DD>-<sha256[:3]> matching WIKI.md § 6.1.
"""

from __future__ import annotations

import email as _email
import email.header
import email.utils
import hashlib
import imaplib
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from gateway import frontmatter as fm, paths, validator
from gateway.pollers.base import Poller, PollerResult


_IMAP_HOST = "imap.gmail.com"
_IMAP_PORT = 993
_DEFAULT_MAX = 50


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_web_id(url: str, date_str: str) -> str:
    url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:3]
    return f"web-{date_str}-{url_hash}"


def _decode_header(value: str) -> str:
    """Decode a potentially RFC-2047-encoded email header value."""
    parts = email.header.decode_header(value)
    out = []
    for raw, charset in parts:
        if isinstance(raw, bytes):
            out.append(raw.decode(charset or "utf-8", errors="replace"))
        else:
            out.append(str(raw))
    return "".join(out)


def _date_to_iso(date_str: str) -> str:
    """Convert email Date header to ISO-8601 UTC string."""
    try:
        parsed = email.utils.parsedate_to_datetime(date_str)
        return parsed.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return _now_iso()


def _date_to_ymd(date_str: str) -> str:
    try:
        parsed = email.utils.parsedate_to_datetime(date_str)
        return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _extract_text(msg) -> str:
    """Extract plain-text body from an email.message.Message."""
    if msg.is_multipart():
        parts = []
        for part in msg.walk():
            ct = part.get_content_type()
            if ct == "text/plain" and not part.get("Content-Disposition"):
                payload = part.get_payload(decode=True)
                if payload:
                    charset = part.get_content_charset() or "utf-8"
                    parts.append(payload.decode(charset, errors="replace"))
        return "\n\n".join(parts)
    payload = msg.get_payload(decode=True)
    if payload:
        charset = msg.get_content_charset() or "utf-8"
        return payload.decode(charset, errors="replace")
    return ""


def _sender_address(from_: str) -> str:
    """Extract bare email address from From header."""
    _, addr = email.utils.parseaddr(from_)
    return addr.lower().strip()


class GmailNewsletterPoller(Poller):
    name = "gmail-newsletters"
    source_type = "web"

    def _config_path(self) -> Path:
        return paths.knowledge_internal() / "pollers" / self.name / "config.yaml"

    def _load_config(self) -> dict[str, Any]:
        p = self._config_path()
        if not p.exists():
            return {}
        try:
            return yaml.safe_load(p.read_text()) or {}
        except yaml.YAMLError:
            return {}

    def _sender_set(self, config: dict) -> dict[str, str]:
        """Return {email_address: domain} from config.senders."""
        senders = config.get("senders") or []
        out: dict[str, str] = {}
        for entry in senders:
            if isinstance(entry, dict):
                addr = str(entry.get("address") or "").lower().strip()
                domain = str(entry.get("domain") or "")
                if addr:
                    out[addr] = domain
        return out

    def run(self) -> PollerResult:
        address = os.environ.get("GMAIL_ADDRESS", "").strip()
        password = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
        if not address or not password:
            return PollerResult(
                success=False,
                errors=["GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set"],
                summary="gmail-newsletters: missing credentials",
            )

        config = self._load_config()
        sender_map = self._sender_set(config)
        label = str(config.get("label") or "INBOX")
        max_messages = int(config.get("max_messages") or _DEFAULT_MAX)

        cursor = self.read_cursor()
        last_uid = int(cursor.get("last_uid") or 0)

        try:
            imap = imaplib.IMAP4_SSL(_IMAP_HOST, _IMAP_PORT)
            imap.login(address, password)
            imap.select(label, readonly=True)
        except Exception as e:
            return PollerResult(
                success=False,
                errors=[f"IMAP connect/login failed: {e!r}"],
                summary=f"gmail-newsletters: IMAP error — {e}",
            )

        try:
            return self._fetch(imap, sender_map, last_uid, max_messages)
        finally:
            try:
                imap.logout()
            except Exception:
                pass

    def _fetch(
        self,
        imap: imaplib.IMAP4_SSL,
        sender_map: dict[str, str],
        last_uid: int,
        max_messages: int,
    ) -> PollerResult:
        uid_filter = f"UID {last_uid + 1}:*" if last_uid else "ALL"
        _typ, data = imap.uid("SEARCH", None, uid_filter)  # type: ignore[arg-type]
        if not data or not data[0]:
            return PollerResult(success=True, summary="gmail-newsletters: no new messages")

        uid_list = data[0].split()
        # newest-first so we respect max_messages while picking up the latest
        uid_list = uid_list[-max_messages:]

        fetched = 0
        skipped = 0
        errors: list[str] = []
        highest_uid = last_uid

        for raw_uid in uid_list:
            uid_int = int(raw_uid)
            try:
                _typ2, msg_data = imap.uid("FETCH", raw_uid, "(RFC822)")  # type: ignore[arg-type]
                if not msg_data or not msg_data[0]:
                    skipped += 1
                    continue
                raw_bytes = msg_data[0][1] if isinstance(msg_data[0], tuple) else b""
                if not raw_bytes:
                    skipped += 1
                    continue
                msg = _email.message_from_bytes(raw_bytes)
            except Exception as e:
                errors.append(f"UID {uid_int}: fetch error — {e!r}")
                continue

            from_ = msg.get("From") or ""
            sender = _sender_address(from_)

            # If sender_map is configured, only accept listed senders
            if sender_map and sender not in sender_map:
                skipped += 1
                highest_uid = max(highest_uid, uid_int)
                continue

            domain = sender_map.get(sender, "") if sender_map else ""

            subject = _decode_header(msg.get("Subject") or "No subject")
            date_raw = msg.get("Date") or ""
            ingested_at = _date_to_iso(date_raw)
            ymd = _date_to_ymd(date_raw)

            # Stable URL: reconstruct as a mailto-derived identifier
            msg_id = (msg.get("Message-ID") or "").strip()
            url = msg_id if msg_id else f"gmail:{uid_int}"

            slug = _build_web_id(url, ymd)
            text_body = _extract_text(msg).strip()
            if not text_body:
                skipped += 1
                highest_uid = max(highest_uid, uid_int)
                continue
            body = text_body + "\n"

            front: dict[str, Any] = {
                "id": slug,
                "type": "web",
                "title": subject,
                "url": url,
                "authors": [sender],
                "published_at": ymd,
                "ingested_at": ingested_at,
                "content_hash": validator.compute_content_hash(body),
                "domains": [domain] if domain else [],
                "nlm_corpus_ids": [],
                "wiki_pages": [],
                "meta": {
                    "source_app": "gmail-newsletter",
                    "sender": sender,
                    "message_id": msg_id,
                    "imap_uid": uid_int,
                },
            }

            target = paths.raw_source_path("web", slug)
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                # idempotent: same slug = same message; skip without error
                skipped += 1
                highest_uid = max(highest_uid, uid_int)
                continue

            self.write_raw(slug, fm.serialize(front, body))
            fetched += 1
            highest_uid = max(highest_uid, uid_int)

        if highest_uid > last_uid:
            self.write_cursor({"last_uid": highest_uid})

        return PollerResult(
            success=len(errors) == 0,
            fetched=fetched,
            skipped=skipped,
            errors=errors,
            summary=f"gmail-newsletters: {fetched} fetched, {skipped} skipped, {len(errors)} errors",
        )
