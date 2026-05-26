"""QUAL-10: Held-out calibration set for filter policy evaluation."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import paths
from gateway.ops.calibration import (
    CalibrationEntry,
    CalibrationMetrics,
    add_calibration_entry,
    calibration_path,
    load_calibration_set,
    score_calibration,
)


# --- fixtures / helpers -------------------------------------------------------


def _write_calibration(kb_root: Path, domain: str, entries: list[dict]) -> Path:
    p = calibration_path(domain)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump(entries, allow_unicode=True), encoding="utf-8")
    return p


class _StubClient:
    """Returns a fixed decision for every call."""

    def __init__(self, response: str = "include"):
        self._response = response

    def call(self, prompt: str) -> str:
        return self._response


class _CyclingClient:
    """Alternates between responses for a list of answers."""

    def __init__(self, answers: list[str]):
        self._answers = answers
        self._idx = 0

    def call(self, prompt: str) -> str:
        ans = self._answers[self._idx % len(self._answers)]
        self._idx += 1
        return ans


# --- load_calibration_set -----------------------------------------------------


def test_load_calibration_set_missing_returns_empty(kb_root: Path) -> None:
    assert load_calibration_set("no-such-domain") == []


def test_load_calibration_set_parses_entries(kb_root: Path) -> None:
    _write_calibration(
        kb_root,
        "test-domain",
        [
            {"source_id": "src-a", "decision": "include", "rationale": "Good"},
            {"source_id": "src-b", "decision": "exclude", "rationale": "Off-topic"},
        ],
    )
    entries = load_calibration_set("test-domain")
    assert len(entries) == 2
    assert entries[0].source_id == "src-a"
    assert entries[0].decision == "include"
    assert entries[1].decision == "exclude"


def test_load_calibration_set_skips_invalid_decision(kb_root: Path) -> None:
    _write_calibration(
        kb_root,
        "test-domain",
        [
            {"source_id": "src-a", "decision": "include"},
            {"source_id": "src-b", "decision": "maybe"},  # invalid
        ],
    )
    entries = load_calibration_set("test-domain")
    assert len(entries) == 1
    assert entries[0].source_id == "src-a"


def test_load_calibration_set_empty_file_returns_empty(kb_root: Path) -> None:
    p = calibration_path("test-domain")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("", encoding="utf-8")
    assert load_calibration_set("test-domain") == []


# --- add_calibration_entry ----------------------------------------------------


def test_add_calibration_entry_creates_file(kb_root: Path) -> None:
    entry = CalibrationEntry(source_id="src-x", decision="include", rationale="Fits")
    add_calibration_entry("test-domain", entry)

    entries = load_calibration_set("test-domain")
    assert len(entries) == 1
    assert entries[0].source_id == "src-x"


def test_add_calibration_entry_appends(kb_root: Path) -> None:
    add_calibration_entry("test-domain", CalibrationEntry("src-a", "include", ""))
    add_calibration_entry("test-domain", CalibrationEntry("src-b", "exclude", ""))

    entries = load_calibration_set("test-domain")
    assert len(entries) == 2


def test_add_calibration_entry_idempotent(kb_root: Path) -> None:
    entry = CalibrationEntry("src-a", "include", "Fits")
    add_calibration_entry("test-domain", entry)
    add_calibration_entry("test-domain", entry)  # duplicate

    entries = load_calibration_set("test-domain")
    assert len(entries) == 1


# --- score_calibration --------------------------------------------------------


def test_score_calibration_returns_none_when_no_set(kb_root: Path) -> None:
    result = score_calibration(
        "no-such-domain",
        ["Discusses X"],
        ["Off-topic"],
        client=_StubClient("include"),
    )
    assert result is None


def test_score_calibration_perfect_score(kb_root: Path) -> None:
    _write_calibration(
        kb_root,
        "test-domain",
        [
            {"source_id": "src-a", "decision": "include", "rationale": ""},
            {"source_id": "src-b", "decision": "include", "rationale": ""},
        ],
    )
    # Stub always returns "include" — matches both ground truths
    result = score_calibration(
        "test-domain", ["Discusses X"], [], client=_StubClient("include")
    )
    assert result is not None
    assert result.correct == 2
    assert result.incorrect == 0
    assert result.accuracy == 1.0
    assert result.precision == 1.0
    assert result.recall == 1.0
    assert result.f1 == 1.0


def test_score_calibration_zero_score(kb_root: Path) -> None:
    _write_calibration(
        kb_root,
        "test-domain",
        [
            {"source_id": "src-a", "decision": "include", "rationale": ""},
            {"source_id": "src-b", "decision": "include", "rationale": ""},
        ],
    )
    # Stub always returns "exclude" — mismatches both
    result = score_calibration(
        "test-domain", ["Discusses X"], [], client=_StubClient("exclude")
    )
    assert result is not None
    assert result.correct == 0
    assert result.incorrect == 2
    assert result.accuracy == 0.0
    assert result.recall == 0.0


def test_score_calibration_mixed(kb_root: Path) -> None:
    _write_calibration(
        kb_root,
        "test-domain",
        [
            {"source_id": "src-a", "decision": "include", "rationale": ""},
            {"source_id": "src-b", "decision": "include", "rationale": ""},
            {"source_id": "src-c", "decision": "exclude", "rationale": ""},
            {"source_id": "src-d", "decision": "exclude", "rationale": ""},
        ],
    )
    # Alternates include/exclude: correct on src-a and src-c, wrong on src-b and src-d
    client = _CyclingClient(["include", "exclude", "exclude", "include"])
    result = score_calibration("test-domain", [], [], client=client)
    assert result is not None
    assert result.n_examples == 4
    assert result.correct == 2
    assert result.incorrect == 2
    assert result.accuracy == pytest.approx(0.5)


def test_score_calibration_f1_formula(kb_root: Path) -> None:
    # 2 TP, 1 FP, 1 FN → precision=2/3, recall=2/3, f1=2/3
    _write_calibration(
        kb_root,
        "test-domain",
        [
            {"source_id": "src-a", "decision": "include", "rationale": ""},  # TP
            {"source_id": "src-b", "decision": "include", "rationale": ""},  # TP
            {"source_id": "src-c", "decision": "exclude", "rationale": ""},  # FP (pred include)
            {"source_id": "src-d", "decision": "include", "rationale": ""},  # FN (pred exclude)
        ],
    )
    client = _CyclingClient(["include", "include", "include", "exclude"])
    result = score_calibration("test-domain", [], [], client=client)
    assert result is not None
    assert result.true_positives == 2
    assert result.false_positives == 1
    assert result.false_negatives == 1
    assert result.precision == pytest.approx(2 / 3, abs=1e-3)
    assert result.recall == pytest.approx(2 / 3, abs=1e-3)
    assert result.f1 == pytest.approx(2 / 3, abs=1e-3)


def test_calibration_metrics_to_dict(kb_root: Path) -> None:
    m = CalibrationMetrics(
        n_examples=10,
        correct=8,
        incorrect=2,
        true_positives=6,
        false_positives=1,
        false_negatives=1,
        precision=0.857,
        recall=0.857,
        f1=0.857,
        accuracy=0.8,
    )
    d = m.to_dict()
    assert d["n_examples"] == 10
    assert d["f1"] == pytest.approx(0.857, abs=1e-3)
    assert "true_positives" not in d  # internal, not serialized


# --- distill_prompt integration -----------------------------------------------


def test_distill_includes_calibration_metrics_in_candidate(kb_root: Path) -> None:
    """When a calibration set exists, distill writes calibration_metrics to the candidate."""
    import yaml as _yaml

    from gateway.ops.finetune import distill_prompt
    from gateway.filter.examples import Example

    # Write policy + examples (enough to pass threshold with enforce=False)
    policy_dir = kb_root / ".knowledge" / "policies" / "test-domain"
    policy_dir.mkdir(parents=True, exist_ok=True)
    policy = {
        "version": "v1",
        "domain": {"slug": "test-domain", "topic": "Test"},
        "filter": {"threshold_include": 0.7},
        "inclusion_criteria": ["Discusses test"],
        "exclusion_criteria": [],
    }
    (policy_dir / "policy.yaml").write_text(
        _yaml.safe_dump(policy, allow_unicode=True), encoding="utf-8"
    )

    # Write a few examples
    examples_dir = policy_dir / "examples"
    examples_dir.mkdir(exist_ok=True)
    ex = {
        "source_id": "web-2026-01-01-abc",
        "domain": "test-domain",
        "decision": "include",
        "score": 0.9,
        "policy_version": "v1",
        "rationale": "Relevant",
        "pinned_at": "2026-01-01T00:00:00Z",
        "pinned_by": "high-confidence",
        "frontmatter_snapshot": {},
        "content_excerpt": "",
    }
    (examples_dir / "web-2026-01-01-abc.yaml").write_text(
        _yaml.safe_dump(ex, allow_unicode=True), encoding="utf-8"
    )

    # Write calibration set
    _write_calibration(
        kb_root,
        "test-domain",
        [{"source_id": "web-2026-01-01-abc", "decision": "include", "rationale": ""}],
    )

    class _StubDistillClient:
        def call(self, prompt: str) -> str:
            return '{"inclusion_criteria": ["Discusses test"], "exclusion_criteria": [], "summary": "ok"}'

    result = distill_prompt("test-domain", client=_StubDistillClient(), enforce_threshold=False)

    assert result.calibration_f1 is not None
    candidate = _yaml.safe_load(result.candidate_path.read_text())
    assert "calibration_metrics" in candidate
    assert "f1" in candidate["calibration_metrics"]
    assert "scored_at" in candidate["calibration_metrics"]


def test_distill_no_calibration_set_skips_metrics(kb_root: Path) -> None:
    """When no calibration set exists, distill still succeeds with no calibration_metrics."""
    import yaml as _yaml

    from gateway.ops.finetune import distill_prompt

    policy_dir = kb_root / ".knowledge" / "policies" / "no-cal-domain"
    policy_dir.mkdir(parents=True, exist_ok=True)
    policy = {
        "version": "v1",
        "domain": {"slug": "no-cal-domain", "topic": "Test"},
        "filter": {"threshold_include": 0.7},
        "inclusion_criteria": ["Discusses X"],
        "exclusion_criteria": [],
    }
    (policy_dir / "policy.yaml").write_text(_yaml.safe_dump(policy, allow_unicode=True))
    examples_dir = policy_dir / "examples"
    examples_dir.mkdir(exist_ok=True)
    ex = {
        "source_id": "web-2026-01-01-xyz",
        "domain": "no-cal-domain",
        "decision": "include",
        "score": 0.9,
        "policy_version": "v1",
        "rationale": "ok",
        "pinned_at": "2026-01-01T00:00:00Z",
        "pinned_by": "high-confidence",
        "frontmatter_snapshot": {},
        "content_excerpt": "",
    }
    (examples_dir / "web-2026-01-01-xyz.yaml").write_text(_yaml.safe_dump(ex, allow_unicode=True))

    class _StubDistillClient:
        def call(self, prompt: str) -> str:
            return '{"inclusion_criteria": ["Discusses X"], "exclusion_criteria": [], "summary": "ok"}'

    result = distill_prompt("no-cal-domain", client=_StubDistillClient(), enforce_threshold=False)

    assert result.calibration_f1 is None
    candidate = _yaml.safe_load(result.candidate_path.read_text())
    assert "calibration_metrics" not in candidate
