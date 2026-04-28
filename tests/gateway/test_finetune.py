"""Tests for M20: filter fine-tuning trigger + distilled-prompt extraction."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import paths
from gateway.filter import examples as example_bank
from gateway.ops.example_bank import backfill_policy
from gateway.ops.finetune import (
    DistillError,
    distill_prompt,
    policy_versions_dir,
    trigger_state,
    trigger_states_all,
)


# --- helpers ---------------------------------------------------------------


def _seed_policy(domain: str, *, topic: str = "topic", inclusion=None, exclusion=None) -> Path:
    body = {
        "domain": {"topic": topic},
        "inclusion_criteria": inclusion or ["a", "b"],
        "exclusion_criteria": exclusion or ["c"],
    }
    legacy = paths.policies_dir() / f"_legacy_{domain}.yaml"
    legacy.parent.mkdir(parents=True, exist_ok=True)
    legacy.write_text(yaml.safe_dump(body))
    return backfill_policy(legacy, domain)


def _pin(domain: str, source_id: str, *, decision: str = "include", score: float = 0.9) -> None:
    example_bank.pin(
        source_id=source_id,
        domain=domain,
        decision=decision,
        score=score,
        policy_version=f"{domain}-v1",
        rationale=f"rationale for {source_id}",
        pinned_by="legacy-backfill",
        frontmatter_snapshot={"title": f"Title {source_id}"},
        content_excerpt=f"excerpt for {source_id}",
    )


class _StubClient:
    def __init__(self, response: str):
        self.response = response
        self.prompts: list[str] = []

    def call(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return self.response


# --- trigger_state ---------------------------------------------------------


def test_trigger_state_below_threshold(kb_root):
    _seed_policy("d-x")
    _pin("d-x", "yt-1")
    state = trigger_state("d-x", threshold=10)
    assert state.count == 1
    assert state.threshold == 10
    assert state.ready is False


def test_trigger_state_at_or_above_threshold(kb_root):
    _seed_policy("d-x")
    for i in range(5):
        _pin("d-x", f"yt-{i}")
    state = trigger_state("d-x", threshold=5)
    assert state.count == 5
    assert state.ready is True


def test_trigger_state_no_examples_returns_zero(kb_root):
    _seed_policy("d-x")
    state = trigger_state("d-x", threshold=10)
    assert state.count == 0
    assert state.ready is False


def test_trigger_states_all_lists_each_domain(kb_root):
    _seed_policy("d-x")
    _seed_policy("d-y")
    _pin("d-x", "yt-1")
    states = trigger_states_all(threshold=10)
    by_d = {s.domain: s for s in states}
    assert by_d["d-x"].count == 1
    assert by_d["d-y"].count == 0


def test_trigger_states_all_skips_dirs_without_policy_yaml(kb_root):
    # An "examples-only" dir without policy.yaml must not appear.
    (paths.policies_dir() / "lonely-domain" / "examples").mkdir(parents=True)
    states = trigger_states_all(threshold=10)
    assert all(s.domain != "lonely-domain" for s in states)


# --- distill_prompt --------------------------------------------------------


_GOOD_RESPONSE = (
    '{"inclusion_criteria": ["refined inc 1", "refined inc 2"],'
    ' "exclusion_criteria": ["refined exc 1"],'
    ' "summary": "patterns indicate that includes are X and excludes are Y."}'
)


def test_distill_prompt_writes_candidate_and_does_not_overwrite_live(kb_root):
    _seed_policy("d-x", topic="t", inclusion=["i1"], exclusion=["e1"])
    for i in range(6):
        _pin("d-x", f"yt-{i}", decision="include")
    for i in range(4):
        _pin("d-x", f"yt-x{i}", decision="exclude")

    client = _StubClient(response=_GOOD_RESPONSE)
    result = distill_prompt("d-x", client=client, threshold=5)

    assert result.examples_used == 10
    assert result.candidate_path.exists()
    assert result.candidate_path.parent == policy_versions_dir("d-x")
    # Live policy.yaml is unchanged in shape.
    live = yaml.safe_load((paths.policies_dir() / "d-x" / "policy.yaml").read_text())
    assert live["inclusion_criteria"] == ["i1"]
    # Candidate carries the distilled criteria + provenance.
    cand = yaml.safe_load(result.candidate_path.read_text())
    assert cand["inclusion_criteria"] == ["refined inc 1", "refined inc 2"]
    assert cand["exclusion_criteria"] == ["refined exc 1"]
    assert cand["distilled"]["from_examples"] == 10
    assert cand["distilled"]["from_policy_version"] == "v1"
    assert cand["distilled"]["summary"]
    assert cand["domain"]["topic"] == "t"
    assert cand["version"] == "v2"


def test_distill_prompt_below_threshold_raises(kb_root):
    _seed_policy("d-x")
    _pin("d-x", "yt-1")
    with pytest.raises(DistillError, match="below distillation threshold"):
        distill_prompt("d-x", client=_StubClient(_GOOD_RESPONSE), threshold=10)


def test_distill_prompt_force_skips_threshold_check(kb_root):
    _seed_policy("d-x")
    _pin("d-x", "yt-1")
    result = distill_prompt(
        "d-x",
        client=_StubClient(_GOOD_RESPONSE),
        threshold=10,
        enforce_threshold=False,
    )
    assert result.candidate_path.exists()


def test_distill_prompt_no_policy_raises(kb_root):
    with pytest.raises(DistillError, match="no policy.yaml"):
        distill_prompt(
            "d-missing",
            client=_StubClient(_GOOD_RESPONSE),
            threshold=1,
            enforce_threshold=False,
        )


def test_distill_prompt_no_examples_raises(kb_root):
    _seed_policy("d-x")
    with pytest.raises(DistillError, match="no examples"):
        distill_prompt(
            "d-x",
            client=_StubClient(_GOOD_RESPONSE),
            threshold=0,
            enforce_threshold=False,
        )


def test_distill_prompt_unparseable_response_raises(kb_root):
    _seed_policy("d-x")
    _pin("d-x", "yt-1")
    with pytest.raises(DistillError, match="unparseable"):
        distill_prompt(
            "d-x",
            client=_StubClient("not json at all"),
            threshold=1,
            enforce_threshold=False,
        )


def test_distill_prompt_includes_examples_in_prompt(kb_root):
    _seed_policy("d-x", topic="cool topic")
    _pin("d-x", "yt-included-1", decision="include")
    _pin("d-x", "yt-excluded-1", decision="exclude")

    client = _StubClient(response=_GOOD_RESPONSE)
    distill_prompt("d-x", client=client, threshold=1, enforce_threshold=False)

    p = client.prompts[0]
    assert "Domain 'd-x'" in p or "domain 'd-x'" in p
    assert "yt-included-1" in p
    assert "yt-excluded-1" in p
    assert "INCLUDED" in p
    assert "EXCLUDED" in p
