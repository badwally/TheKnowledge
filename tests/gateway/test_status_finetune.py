"""Tests for QUAL-5: fine-tune readiness block in `wiki status`."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from gateway import paths
from gateway.filter.examples import pin as pin_example
from gateway.ops.status import status


def _write_policy(domain: str) -> None:
    pol_dir = paths.knowledge_root() / ".knowledge" / "policies" / domain
    pol_dir.mkdir(parents=True, exist_ok=True)
    (pol_dir / "policy.yaml").write_text(
        yaml.safe_dump({
            "version": "v1",
            "domain": {"slug": domain, "topic": domain, "field": "test"},
            "filter": {
                "threshold_include": 0.7,
                "threshold_review": 0.5,
                "example_count_in_prompt": 0,
                "example_strategy": "balanced",
            },
            "inclusion_criteria": ["test"],
            "exclusion_criteria": [],
            "quality_signals": {},
        })
    )


def _write_examples(domain: str, n: int) -> None:
    """Write N example decisions for domain into the example bank."""
    for i in range(n):
        pin_example(
            source_id=f"web-2026-01-01-ex{i:04d}",
            domain=domain,
            decision="include",
            score=0.9,
            policy_version=f"{domain}-v1",
            rationale="test",
            pinned_by="high-confidence",
            frontmatter_snapshot={"type": "web", "title": f"Example {i}"},
            content_excerpt="excerpt",
        )


def test_status_shows_finetune_readiness_line(kb_root: Path):
    _write_policy("dom-alpha")
    _write_examples("dom-alpha", 268)

    result = status()
    text = result.summary
    assert "Fine-tune readiness" in text
    assert "dom-alpha" in text
    assert "268/500" in text
    assert "54%" in text or "53%" in text  # rounding


def test_status_finetune_not_ready_shows_count(kb_root: Path):
    _write_policy("dom-beta")
    _write_examples("dom-beta", 10)

    result = status()
    text = result.summary
    assert "dom-beta" in text
    assert "10/500" in text


def test_status_finetune_ready_shows_ready(kb_root: Path):
    _write_policy("dom-gamma")
    _write_examples("dom-gamma", 500)

    result = status()
    text = result.summary
    assert "dom-gamma" in text
    assert "500/500" in text


def test_status_finetune_empty_when_no_policies(kb_root: Path):
    result = status()
    text = result.summary
    # No policies → fine-tune block absent or shows "none"
    assert "Fine-tune readiness" not in text or "none" in text.lower()


def test_status_logs_eighty_percent_threshold_crossing(kb_root: Path, monkeypatch):
    """Crossing 80% (400/500) triggers a log entry (one-shot)."""
    _write_policy("dom-delta")
    _write_examples("dom-delta", 400)

    import gateway.log as _log
    logged_ops = []
    original_append = _log.append

    def _capture_append(op, *, fields=None, summary=""):
        logged_ops.append(op)
        original_append(op, fields=fields or {}, summary=summary)

    monkeypatch.setattr(_log, "append", _capture_append)

    status()
    assert any("finetune-milestone" in op or "finetune" in op for op in logged_ops)


def test_status_eighty_percent_not_re_fired(kb_root: Path, monkeypatch):
    """Second status() call with same count does not re-log the 80% crossing."""
    _write_policy("dom-eps")
    _write_examples("dom-eps", 400)

    import gateway.log as _log
    logged_ops: list[str] = []
    original_append = _log.append

    def _capture_append(op, *, fields=None, summary=""):
        logged_ops.append(op)
        original_append(op, fields=fields or {}, summary=summary)

    monkeypatch.setattr(_log, "append", _capture_append)

    status()  # first call → should log
    first_count = sum(1 for op in logged_ops if "finetune" in op)
    status()  # second call → should NOT re-log
    second_count = sum(1 for op in logged_ops if "finetune" in op)
    assert first_count == 1
    assert second_count == 1  # no new entry
