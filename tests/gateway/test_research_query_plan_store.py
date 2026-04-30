"""Tests for `gateway.research.query_plan_store`."""

from __future__ import annotations

import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest
import yaml

from gateway.research import query_plan_store as qps


def _plan(
    *,
    session_id: str = "2026-04-30-test",
    domain: str = "edge-ai-agentic",
    prompt: str = "test prompt",
    when: datetime | None = None,
    queries: dict | None = None,
    edited: bool = False,
) -> qps.QueryPlan:
    return qps.QueryPlan(
        session_id=session_id,
        domain=domain,
        prompt=prompt,
        generated_at=when or datetime(2026, 4, 30, 12, 0, 0, tzinfo=timezone.utc),
        queries=queries or {"youtube": ["q1", "q2"], "arxiv": ["a1"]},
        target_counts={"youtube": 20, "arxiv": 8},
        plan_client_model="claude-opus-4-7",
        edited=edited,
    )


def test_save_and_load_round_trip(kb_root: Path) -> None:
    plan = _plan()
    target = qps.save(plan)

    assert target == kb_root / "nlm" / "query_plans" / "2026-04-30-test.yaml"
    assert target.is_file()

    loaded = qps.load(plan.session_id)
    assert loaded.session_id == plan.session_id
    assert loaded.domain == plan.domain
    assert loaded.prompt == plan.prompt
    assert loaded.queries == plan.queries
    assert loaded.target_counts == plan.target_counts
    assert loaded.plan_client_model == "claude-opus-4-7"
    assert loaded.edited is False
    assert loaded.generated_at == plan.generated_at


def test_save_creates_query_plans_directory(kb_root: Path) -> None:
    qpdir = kb_root / "nlm" / "query_plans"
    assert not qpdir.exists()
    qps.save(_plan())
    assert qpdir.is_dir()


def test_load_missing_raises(kb_root: Path) -> None:
    with pytest.raises(qps.QueryPlanError, match="no query plan"):
        qps.load("does-not-exist")


def test_load_malformed_raises(kb_root: Path) -> None:
    target = kb_root / "nlm" / "query_plans" / "bad.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("not: valid: yaml: at: all:\n  - [")
    with pytest.raises(qps.QueryPlanError):
        qps.load("bad")


def test_exists(kb_root: Path) -> None:
    assert qps.exists("missing") is False
    qps.save(_plan(session_id="here"))
    assert qps.exists("here") is True


def test_is_edited_flag_takes_precedence(kb_root: Path) -> None:
    qps.save(_plan(session_id="flagged", edited=True))
    assert qps.is_edited("flagged") is True


def test_is_edited_via_mtime(kb_root: Path) -> None:
    """Plan written 10s ago, mtime now → mtime > generated_at by >2s slack."""
    past = datetime.now(timezone.utc) - timedelta(seconds=30)
    qps.save(_plan(session_id="stale", when=past))

    # Touch the file to push mtime to "now"
    target = qps.path_for("stale")
    now_ts = time.time()
    os.utime(target, (now_ts, now_ts))

    assert qps.is_edited("stale") is True


def test_is_edited_false_when_fresh(kb_root: Path) -> None:
    """Save now → mtime ≈ generated_at → not considered edited."""
    qps.save(_plan(session_id="fresh", when=datetime.now(timezone.utc)))
    assert qps.is_edited("fresh") is False


def test_is_edited_returns_false_for_missing(kb_root: Path) -> None:
    assert qps.is_edited("nope") is False


def test_recent_edited_filters_by_domain_and_flag(kb_root: Path) -> None:
    qps.save(_plan(session_id="a", domain="edge-ai-agentic", edited=True,
                   when=datetime(2026, 4, 1, tzinfo=timezone.utc)))
    qps.save(_plan(session_id="b", domain="edge-ai-agentic", edited=False,
                   when=datetime(2026, 4, 2, tzinfo=timezone.utc)))
    qps.save(_plan(session_id="c", domain="other-domain", edited=True,
                   when=datetime(2026, 4, 3, tzinfo=timezone.utc)))
    qps.save(_plan(session_id="d", domain="edge-ai-agentic", edited=True,
                   when=datetime(2026, 4, 4, tzinfo=timezone.utc)))

    result = qps.recent_edited("edge-ai-agentic")
    assert [p.session_id for p in result] == ["d", "a"]


def test_recent_edited_caps_at_n(kb_root: Path) -> None:
    for i in range(7):
        qps.save(
            _plan(
                session_id=f"s{i}",
                edited=True,
                when=datetime(2026, 4, 1, tzinfo=timezone.utc) + timedelta(days=i),
            )
        )
    result = qps.recent_edited("edge-ai-agentic", n=3)
    assert len(result) == 3
    # newest first
    assert [p.session_id for p in result] == ["s6", "s5", "s4"]


def test_recent_edited_empty_when_dir_missing(kb_root: Path) -> None:
    assert qps.recent_edited("edge-ai-agentic") == []


def test_yaml_layout_is_human_friendly(kb_root: Path) -> None:
    """Sanity-check the on-disk YAML shape so hand-edits are predictable."""
    qps.save(_plan())
    raw = (kb_root / "nlm" / "query_plans" / "2026-04-30-test.yaml").read_text()
    parsed = yaml.safe_load(raw)
    assert parsed["version"] == 1
    assert parsed["domain"] == "edge-ai-agentic"
    assert parsed["queries"]["youtube"] == ["q1", "q2"]
    assert parsed["edited"] is False
    # Field ordering is preserved (sort_keys=False) so users see
    # session_id/domain/prompt at the top, queries below.
    keys = list(parsed.keys())
    assert keys.index("session_id") < keys.index("queries")
