"""Slack source poller (INT-19).

Reads messages from configured Slack channels and writes threaded
conversations to raw/note/ as canonical note sources.

Auth:
  SLACK_BOT_TOKEN — Slack Bot token (xoxb-...) with scopes:
                    channels:history, groups:history (private channels),
                    channels:read, groups:read

Config: .knowledge/pollers/slack/config.yaml
  channels:
    - channel_id: "C12345ABC"
      name: "knowledge-notes"   # for display/slug only
      domain: "research"        # optional wiki domain tag
  min_length: 200               # min body chars to ingest a standalone msg
  include_threads: true         # append thread replies to message body
  max_messages: 100             # per channel per run (default 100)

Cursor: .knowledge/pollers/slack/cursor.yaml
  <channel_id>: <Slack message ts string>

Slug format: note-slack-<sha256(channel_id + ts)[:12]> matching WIKI.md § 6.1.

Rate limiting: Slack Tier 3 allows ~50 req/min for conversations.history.
The poller adds no explicit sleep; short per-channel page counts stay within
safe limits for typical config sizes.
"""

from __future__ import annotations

import hashlib
import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from gateway import frontmatter as fm, paths, validator
from gateway.pollers.base import Poller, PollerResult


_API_BASE = "https://slack.com/api"
_DEFAULT_MIN_LENGTH = 200
_DEFAULT_MAX_MESSAGES = 100


class SlackError(Exception):
    """Raised on Slack API errors."""


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _ts_to_iso(ts: str) -> str:
    """Convert Slack message timestamp (Unix float string) to ISO-8601."""
    try:
        unix_sec = float(ts)
        return datetime.fromtimestamp(unix_sec, tz=timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
    except (ValueError, OSError):
        return _now_iso()


def _ts_to_date(ts: str) -> str:
    try:
        unix_sec = float(ts)
        return datetime.fromtimestamp(unix_sec, tz=timezone.utc).strftime("%Y-%m-%d")
    except (ValueError, OSError):
        return _now_iso()[:10]


def _build_note_id(channel_id: str, ts: str) -> str:
    key = f"{channel_id}:{ts}"
    digest = hashlib.sha256(key.encode()).hexdigest()[:12]
    return f"note-slack-{digest}"


def _slack_get(path: str, token: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    """Make a Slack Web API GET call and return the parsed JSON."""
    query = ""
    if params:
        parts = "&".join(f"{k}={urllib.request.quote(str(v))}" for k, v in params.items())
        query = f"?{parts}"
    url = f"{_API_BASE}/{path}{query}"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode(errors="replace")
        raise SlackError(f"Slack API {path} → {e.code}: {body_text}") from e
    except Exception as e:
        raise SlackError(f"Slack API {path} → {e!r}") from e

    if not data.get("ok"):
        raise SlackError(f"Slack API {path} error: {data.get('error', 'unknown')}")
    return data


def _fetch_history(
    channel_id: str,
    token: str,
    oldest: str = "",
    limit: int = 100,
) -> list[dict[str, Any]]:
    """Fetch messages from a channel since `oldest` (Slack ts string)."""
    params: dict[str, str] = {"channel": channel_id, "limit": str(min(limit, 200))}
    if oldest:
        params["oldest"] = oldest
    messages: list[dict[str, Any]] = []
    while True:
        data = _slack_get("conversations.history", token, params)
        messages.extend(data.get("messages", []))
        if not data.get("has_more") or len(messages) >= limit:
            break
        cursor = data.get("response_metadata", {}).get("next_cursor", "")
        if not cursor:
            break
        params["cursor"] = cursor
    return messages[:limit]


def _fetch_replies(channel_id: str, thread_ts: str, token: str) -> list[dict[str, Any]]:
    """Fetch all replies in a thread (excluding the root message)."""
    params = {"channel": channel_id, "ts": thread_ts, "limit": "200"}
    data = _slack_get("conversations.replies", token, params)
    all_msgs = data.get("messages", [])
    return [m for m in all_msgs if m.get("ts") != thread_ts]


def _msg_text(msg: dict[str, Any]) -> str:
    return msg.get("text", "").strip()


class SlackSourcePoller(Poller):
    """Fetches Slack channel messages into raw/note/ for wiki ingest."""

    name = "slack"
    source_type = "note"

    def _config_path(self) -> Path:
        return paths.knowledge_internal() / "pollers" / "slack" / "config.yaml"

    def _load_config(self) -> dict[str, Any]:
        p = self._config_path()
        if not p.exists():
            return {
                "channels": [],
                "min_length": _DEFAULT_MIN_LENGTH,
                "include_threads": True,
                "max_messages": _DEFAULT_MAX_MESSAGES,
            }
        data = yaml.safe_load(p.read_text()) or {}
        data.setdefault("channels", [])
        data.setdefault("min_length", _DEFAULT_MIN_LENGTH)
        data.setdefault("include_threads", True)
        data.setdefault("max_messages", _DEFAULT_MAX_MESSAGES)
        return data

    def run(
        self,
        *,
        fetch_history: Any = None,
        fetch_replies: Any = None,
    ) -> PollerResult:
        token = os.environ.get("SLACK_BOT_TOKEN", "")
        if not token and fetch_history is None:
            return PollerResult(
                success=False,
                errors=["SLACK_BOT_TOKEN environment variable not set"],
                summary="skipped: no SLACK_BOT_TOKEN",
            )

        _hist = fetch_history or (lambda ch, oldest, limit: _fetch_history(ch, token, oldest, limit))
        _replies = fetch_replies or (lambda ch, ts: _fetch_replies(ch, ts, token))

        config = self._load_config()
        min_length: int = int(config.get("min_length", _DEFAULT_MIN_LENGTH))
        include_threads: bool = bool(config.get("include_threads", True))
        max_messages: int = int(config.get("max_messages", _DEFAULT_MAX_MESSAGES))

        cursor = self.read_cursor()

        fetched = 0
        skipped = 0
        errors: list[str] = []

        for entry in config.get("channels", []):
            channel_id = str(entry.get("channel_id", "")).strip()
            if not channel_id:
                errors.append("config: missing channel_id in channels entry")
                continue
            domain = str(entry.get("domain", ""))
            channel_name = str(entry.get("name", channel_id))
            oldest = cursor.get(channel_id, "")

            try:
                messages = _hist(channel_id, oldest, max_messages)
            except SlackError as e:
                errors.append(f"conversations.history({channel_id}): {e}")
                continue

            latest_ts = oldest
            for msg in messages:
                ts = msg.get("ts", "")
                if not ts:
                    continue
                if ts <= oldest:
                    skipped += 1
                    continue

                text = _msg_text(msg)
                reply_count: int = msg.get("reply_count", 0)
                is_thread_root = reply_count > 0
                is_long_enough = len(text) >= min_length

                if not is_thread_root and not is_long_enough:
                    skipped += 1
                    if not latest_ts or ts > latest_ts:
                        latest_ts = ts
                    continue

                body_parts = [text]
                if include_threads and is_thread_root:
                    try:
                        replies = _replies(channel_id, ts)
                        for r in replies:
                            r_text = _msg_text(r)
                            if r_text:
                                body_parts.append(f"\n> {r_text}")
                    except SlackError as e:
                        errors.append(f"conversations.replies({channel_id}, {ts}): {e}")

                body_md = "\n".join(body_parts).strip()
                note_id = _build_note_id(channel_id, ts)
                msg_iso = _ts_to_iso(ts)
                msg_date = _ts_to_date(ts)

                title = f"#{channel_name} — {msg_date}"
                raw = _render_raw(
                    note_id=note_id,
                    title=title,
                    channel_id=channel_id,
                    channel_name=channel_name,
                    ts=ts,
                    source_app="slack",
                    domain=domain,
                    posted_at=msg_iso,
                    date=msg_date,
                    body_md=body_md,
                )
                self.write_raw(note_id, raw)
                fetched += 1

                if not latest_ts or ts > latest_ts:
                    latest_ts = ts

            if latest_ts and latest_ts != oldest:
                cursor[channel_id] = latest_ts

        self.write_cursor(cursor)

        n_err = len(errors)
        summary = f"fetched {fetched}, skipped {skipped}" + (
            f", {n_err} error(s)" if errors else ""
        )
        return PollerResult(
            success=n_err == 0 or fetched > 0,
            fetched=fetched,
            skipped=skipped,
            errors=errors,
            summary=summary,
        )


def _render_raw(
    *,
    note_id: str,
    title: str,
    channel_id: str,
    channel_name: str,
    ts: str,
    source_app: str,
    domain: str,
    posted_at: str,
    date: str,
    body_md: str,
) -> str:
    meta: dict[str, Any] = {
        "id": note_id,
        "title": title,
        "type": "note",
        "source_app": source_app,
        "content_hash": validator.compute_content_hash(body_md),
        "ingested_at": _now_iso(),
        "date": date,
        "slack_channel_id": channel_id,
        "slack_channel_name": channel_name,
        "slack_ts": ts,
        "posted_at": posted_at,
    }
    if domain:
        meta["domains"] = [domain]
    return fm.serialize(meta, body_md)
