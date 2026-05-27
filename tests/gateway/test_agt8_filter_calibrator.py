"""AGT-8: Monthly filter calibrator routine."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import paths
from gateway.filter.examples import pin as pin_example
from gateway.ops.filter_calibrator import run_filter_calibrator


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #


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


# --------------------------------------------------------------------------- #
# Tests                                                                        #
# --------------------------------------------------------------------------- #


def test_no_policies_returns_success(kb_root: Path) -> None:
    result = run_filter_calibrator()
    assert result.success
    assert "no domains" in result.summary


def test_below_threshold_no_log_event(kb_root: Path, tmp_path: Path) -> None:
    _write_policy("alpha")
    _write_examples("alpha", 10)  # well below 500
    result = run_filter_calibrator()
    assert result.success
    assert "alpha" in result.summary
    # No distill-ready event should be logged
    log_text = (paths.knowledge_root() / "log.md").read_text() if (paths.knowledge_root() / "log.md").exists() else ""
    assert "calibration-distill-ready" not in log_text


def test_above_threshold_emits_log_event(kb_root: Path) -> None:
    _write_policy("beta")
    _write_examples("beta", 500)  # exactly at threshold
    result = run_filter_calibrator()
    assert result.success
    log_path = paths.knowledge_root() / "log.md"
    assert log_path.exists()
    log_text = log_path.read_text()
    assert "calibration-distill-ready" in log_text
    assert "beta" in log_text
    assert "wiki finetune --distill --domain beta" in log_text


def test_above_threshold_summary_says_ready(kb_root: Path) -> None:
    _write_policy("gamma")
    _write_examples("gamma", 600)
    result = run_filter_calibrator()
    assert "ready" in result.summary
    assert "gamma" in result.summary


def test_already_logged_not_emitted_twice(kb_root: Path) -> None:
    _write_policy("delta")
    _write_examples("delta", 500)
    # First run — should log
    run_filter_calibrator()
    log_path = paths.knowledge_root() / "log.md"
    first_log = log_path.read_text() if log_path.exists() else ""
    count_before = first_log.count("calibration-distill-ready")
    # Second run — should not log again
    run_filter_calibrator()
    second_log = log_path.read_text() if log_path.exists() else ""
    count_after = second_log.count("calibration-distill-ready")
    assert count_after == count_before


def test_multiple_domains_below_threshold(kb_root: Path) -> None:
    _write_policy("d1")
    _write_policy("d2")
    _write_examples("d1", 100)
    _write_examples("d2", 200)
    result = run_filter_calibrator()
    assert result.success
    assert "d1" in result.summary
    assert "d2" in result.summary
    log_text = (paths.knowledge_root() / "log.md").read_text() if (paths.knowledge_root() / "log.md").exists() else ""
    assert "calibration-distill-ready" not in log_text


def test_result_is_operation_result(kb_root: Path) -> None:
    result = run_filter_calibrator()
    assert hasattr(result, "success")
    assert hasattr(result, "summary")


def test_schedule_entry_exists() -> None:
    schedule_path = paths.knowledge_root() / ".knowledge" / "schedule.yaml"
    assert schedule_path.exists(), "schedule.yaml must exist"
    data = yaml.safe_load(schedule_path.read_text())
    names = [j["name"] for j in data.get("jobs", [])]
    assert "filter-calibrator" in names


def test_schedule_entry_is_monthly() -> None:
    schedule_path = paths.knowledge_root() / ".knowledge" / "schedule.yaml"
    data = yaml.safe_load(schedule_path.read_text())
    job = next(j for j in data["jobs"] if j["name"] == "filter-calibrator")
    # Monthly cron: day-of-month field (index 2) must be 1, not *
    parts = job["cron"].split()
    assert len(parts) == 5
    assert parts[2] == "1", f"expected day-of-month=1, got {parts[2]!r}"
    assert parts[3] == "*", "month field should be *"


def test_cli_routine_filter_calibrator(kb_root: Path) -> None:
    from gateway.cli import main
    rc = main(["routine", "filter-calibrator"])
    assert rc == 0
