"""INT-19: Slack source poller tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from gateway import frontmatter as fm, paths, validator
from gateway.pollers.slack import (
    SlackSourcePoller,
    _build_note_id,
    _msg_text,
    _render_raw,
    _ts_to_date,
    _ts_to_iso,
)


# --- helper utilities -------------------------------------------------------


def test_ts_to_iso_valid():
    iso = _ts_to_iso("1716758400.000000")  # 2024-05-27
    assert iso.startswith("2024-05-")


def test_ts_to_iso_invalid():
    iso = _ts_to_iso("not-a-ts")
    assert len(iso) == 20  # fallback to _now_iso()


def test_ts_to_date_valid():
    date = _ts_to_date("1716758400.000000")
    assert date.startswith("2024-05-")


def test_build_note_id_format():
    nid = _build_note_id("C12345", "1716758400.000000")
    assert nid.startswith("note-slack-")
    assert len(nid) == len("note-slack-") + 12


def test_build_note_id_stable():
    assert _build_note_id("C12345", "1.23") == _build_note_id("C12345", "1.23")


def test_build_note_id_different():
    assert _build_note_id("C12345", "1.23") != _build_note_id("C12345", "4.56")
    assert _build_note_id("C12345", "1.23") != _build_note_id("C99999", "1.23")


def test_msg_text():
    assert _msg_text({"text": "  hello  "}) == "hello"
    assert _msg_text({}) == ""


# --- _render_raw ------------------------------------------------------------


def test_render_raw_valid_frontmatter(kb_root: Path):
    raw = _render_raw(
        note_id="note-slack-abc123def456",
        title="#general — 2026-05-26",
        channel_id="C12345",
        channel_name="general",
        ts="1716758400.000000",
        source_app="slack",
        domain="research",
        posted_at="2024-05-27T00:00:00Z",
        date="2024-05-27",
        body_md="This is a meaningful Slack message with sufficient length.",
    )
    front, body = fm.parse(raw)
    result = validator.validate_source_frontmatter(front)
    assert not result.errors, result.errors
    assert front["type"] == "note"
    assert front["source_app"] == "slack"
    assert front["slack_channel_id"] == "C12345"
    assert front["slack_channel_name"] == "general"
    assert front["domains"] == ["research"]


def test_render_raw_no_domain(kb_root: Path):
    raw = _render_raw(
        note_id="note-slack-abc123def456",
        title="#general — 2026-05-26",
        channel_id="C12345",
        channel_name="general",
        ts="1716758400.000000",
        source_app="slack",
        domain="",
        posted_at="2024-05-27T00:00:00Z",
        date="2024-05-27",
        body_md="content",
    )
    front, _ = fm.parse(raw)
    assert "domains" not in front


# --- poller run() -----------------------------------------------------------


def _make_msg(ts: str, text: str, reply_count: int = 0) -> dict[str, Any]:
    return {"ts": ts, "text": text, "reply_count": reply_count}


def _make_config(channels: list[dict], min_length: int = 200, max_messages: int = 100):
    return {"channels": channels, "min_length": min_length, "include_threads": True, "max_messages": max_messages}


def _stub_hist(msgs: list[dict]):
    def _fn(channel_id, oldest, limit):
        return [m for m in msgs if not oldest or m["ts"] > oldest][:limit]
    return _fn


def _stub_replies(reply_map: dict[str, list[dict]]):
    def _fn(channel_id, ts):
        return reply_map.get(ts, [])
    return _fn


def test_run_no_token(kb_root: Path):
    import os
    backup = os.environ.pop("SLACK_BOT_TOKEN", None)
    try:
        poller = SlackSourcePoller()
        result = poller.run()
        assert not result.success
        assert "SLACK_BOT_TOKEN" in result.errors[0]
    finally:
        if backup is not None:
            os.environ["SLACK_BOT_TOKEN"] = backup


def test_run_empty_config(kb_root: Path):
    poller = SlackSourcePoller()
    result = poller.run(fetch_history=_stub_hist([]), fetch_replies=_stub_replies({}))
    assert result.success
    assert result.fetched == 0


def test_run_ingests_long_message(kb_root: Path):
    long_text = "A" * 250
    channel_id = "C001"
    ts = "1716758400.000000"
    config = _make_config([{"channel_id": channel_id, "name": "notes", "domain": "research"}], min_length=200)
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    msgs = [_make_msg(ts, long_text)]
    result = poller.run(fetch_history=_stub_hist(msgs), fetch_replies=_stub_replies({}))
    assert result.fetched == 1
    note_id = _build_note_id(channel_id, ts)
    raw_path = paths.raw_source_path("note", note_id)
    assert raw_path.exists()
    front, body = fm.parse(raw_path.read_text())
    assert front["slack_channel_id"] == channel_id
    assert long_text in body


def test_run_skips_short_non_thread(kb_root: Path):
    channel_id = "C002"
    ts = "1716758401.000000"
    config = _make_config([{"channel_id": channel_id, "name": "noise", "domain": ""}], min_length=200)
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    msgs = [_make_msg(ts, "ok", reply_count=0)]  # short, no thread
    result = poller.run(fetch_history=_stub_hist(msgs), fetch_replies=_stub_replies({}))
    assert result.fetched == 0
    assert result.skipped >= 1


def test_run_ingests_thread_root(kb_root: Path):
    channel_id = "C003"
    ts = "1716758402.000000"
    reply_ts = "1716758403.000000"
    config = _make_config([{"channel_id": channel_id, "name": "threads", "domain": ""}], min_length=200)
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    msgs = [_make_msg(ts, "Short parent", reply_count=1)]
    replies = {ts: [_make_msg(reply_ts, "Reply content")]}
    result = poller.run(fetch_history=_stub_hist(msgs), fetch_replies=_stub_replies(replies))
    assert result.fetched == 1
    note_id = _build_note_id(channel_id, ts)
    raw_path = paths.raw_source_path("note", note_id)
    front, body = fm.parse(raw_path.read_text())
    assert "Reply content" in body


def test_run_cursor_skips_old_messages(kb_root: Path):
    channel_id = "C004"
    old_ts = "1716758400.000000"
    new_ts = "1716758500.000000"
    config = _make_config([{"channel_id": channel_id, "name": "c4", "domain": ""}], min_length=0)
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    poller.write_cursor({channel_id: old_ts})
    msgs = [_make_msg(old_ts, "old" * 100), _make_msg(new_ts, "new" * 100)]
    result = poller.run(fetch_history=_stub_hist(msgs), fetch_replies=_stub_replies({}))
    assert result.fetched == 1
    note_id = _build_note_id(channel_id, new_ts)
    assert paths.raw_source_path("note", note_id).exists()


def test_run_cursor_updated(kb_root: Path):
    channel_id = "C005"
    ts1 = "1716758400.000000"
    ts2 = "1716758500.000000"
    config = _make_config([{"channel_id": channel_id, "name": "c5", "domain": ""}], min_length=0)
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    msgs = [_make_msg(ts1, "msg1" * 60), _make_msg(ts2, "msg2" * 60)]
    poller.run(fetch_history=_stub_hist(msgs), fetch_replies=_stub_replies({}))
    cursor = poller.read_cursor()
    assert cursor.get(channel_id) == ts2


def test_run_missing_channel_id(kb_root: Path):
    config = _make_config([{"name": "no-id", "domain": ""}])
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    result = poller.run(fetch_history=_stub_hist([]), fetch_replies=_stub_replies({}))
    assert len(result.errors) > 0


def test_run_history_error(kb_root: Path):
    channel_id = "C006"
    config = _make_config([{"channel_id": channel_id, "name": "c6", "domain": ""}])
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))

    from gateway.pollers.slack import SlackError
    def bad_hist(ch, oldest, limit):
        raise SlackError("not_in_channel")

    result = poller.run(fetch_history=bad_hist, fetch_replies=_stub_replies({}))
    assert len(result.errors) > 0
    assert result.fetched == 0


def test_run_replies_error_continues(kb_root: Path):
    channel_id = "C007"
    ts = "1716758400.000000"
    config = _make_config([{"channel_id": channel_id, "name": "c7", "domain": ""}], min_length=0)
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    msgs = [_make_msg(ts, "parent message", reply_count=1)]

    from gateway.pollers.slack import SlackError
    def bad_replies(ch, t):
        raise SlackError("no_access")

    result = poller.run(fetch_history=_stub_hist(msgs), fetch_replies=bad_replies)
    assert result.fetched == 1  # still ingests despite reply error
    assert len(result.errors) > 0


def test_run_max_messages_limit(kb_root: Path):
    channel_id = "C008"
    config = _make_config([{"channel_id": channel_id, "name": "c8", "domain": ""}], min_length=0, max_messages=3)
    poller = SlackSourcePoller()
    poller._config_path().parent.mkdir(parents=True, exist_ok=True)
    poller._config_path().write_text(yaml.safe_dump(config))
    msgs = [_make_msg(f"171675840{i}.000000", "x" * 250) for i in range(6)]

    def capped_hist(ch, oldest, limit):
        return msgs[:limit]

    result = poller.run(fetch_history=capped_hist, fetch_replies=_stub_replies({}))
    assert result.fetched <= 3


def test_poller_registered():
    from gateway.pollers import _REGISTRY
    assert "slack" in _REGISTRY
