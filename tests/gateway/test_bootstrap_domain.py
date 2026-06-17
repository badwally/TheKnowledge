"""Tests for `wiki bootstrap-domain`."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from gateway import frontmatter as fm
from gateway import paths
from gateway.filter.policy import policy_path
from gateway.ops.bootstrap_domain import bootstrap_domain


class StubPlanClient:
    def __init__(self, response):
        self._responses = [response] if isinstance(response, str) else list(response)
        self._idx = 0
        self.last_prompt = None
        self.calls = 0

    def call(self, prompt):
        self.last_prompt = prompt
        self.calls += 1
        idx = min(self._idx, len(self._responses) - 1)
        self._idx += 1
        return self._responses[idx]


def _good_policy_response(slug="test-domain"):
    payload = {
        "version": "v1",
        "policy_schema_version": 1,
        "domain": {
            "slug": slug,
            "topic": "Testing the bootstrap pipeline",
            "field": "Software testing and validation",
            "description": "A fictional domain about validating bootstrap-domain.",
        },
        "filter": {
            "threshold_include": 0.7,
            "threshold_review": 0.5,
            "example_count_in_prompt": 12,
            "example_strategy": "balanced",
        },
        "inclusion_criteria": [
            "Discusses end-to-end gateway operations with concrete code examples",
            "Covers schema validation patterns with measurable acceptance criteria",
            "Examines test fixture design and atomic write semantics in real systems",
        ],
        "exclusion_criteria": [
            "Pure marketing material without technical substance",
        ],
        "quality_signals": {
            "publication_venue": {
                "positive_signals": ["Peer-reviewed venue", "Reputable engineering blog"],
                "negative_signals": ["Predatory journal", "Anonymous post"],
            },
            "content_depth": {
                "positive_signals": ["Reports measurements", "Includes code excerpts"],
                "negative_signals": ["Hand-wave only", "Surface skim"],
            },
        },
    }
    return json.dumps(payload)


def test_bootstrap_happy_path(kb_root):
    client = StubPlanClient(_good_policy_response("test-domain"))
    result = bootstrap_domain(
        description="A test domain for validating the bootstrap pipeline with adequate length",
        slug="test-domain",
        plan_client=client,
    )
    assert result.success, result.errors

    written = policy_path("test-domain")
    assert written.exists()

    data = yaml.safe_load(written.read_text())
    assert data["domain"]["slug"] == "test-domain"
    assert len(data["inclusion_criteria"]) >= 3
    assert data["policy_schema_version"] == 1

    examples_dir = paths.policies_dir() / "test-domain" / "examples"
    assert examples_dir.is_dir()


def test_bootstrap_rejects_invalid_slug(kb_root):
    client = StubPlanClient("(unused)")
    result = bootstrap_domain(
        description="some description",
        slug="Bad_Slug",
        plan_client=client,
    )
    assert not result.success
    assert any("slug" in e.lower() for e in result.errors)
    assert client.calls == 0


def test_bootstrap_refuses_existing_policy_without_force(kb_root):
    target = policy_path("existing")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("version: v1\ndomain:\n  slug: existing\n")
    client = StubPlanClient(_good_policy_response("existing"))
    result = bootstrap_domain(
        description="x", slug="existing", plan_client=client
    )
    assert not result.success
    assert any("already exists" in e.lower() for e in result.errors)


def test_bootstrap_refuses_promoted_policy_even_with_force(kb_root):
    target = policy_path("promoted")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        "version: v0.1.0-auto\nauto_generated_from_proposal: true\n"
        "domain:\n  slug: promoted\n"
    )
    client = StubPlanClient(_good_policy_response("promoted"))
    result = bootstrap_domain(
        description="x", slug="promoted", plan_client=client, force=False
    )
    assert not result.success
    joined = " ".join(result.errors).lower()
    assert "demote-domain" in joined


def test_bootstrap_refuses_when_proposal_exists(kb_root):
    proposal = paths.wiki_dir() / "proposals" / "open-proposal.md"
    proposal.parent.mkdir(parents=True, exist_ok=True)
    proposal.write_text(
        fm.serialize(
            {"type": "domain-proposal", "status": "draft", "proposed_domain": "open-proposal"},
            "## Rationale\n\nx\n",
        )
    )
    client = StubPlanClient(_good_policy_response("open-proposal"))
    result = bootstrap_domain(
        description="x", slug="open-proposal", plan_client=client, force=True
    )
    assert not result.success
    joined = " ".join(result.errors).lower()
    assert "promote-domain" in joined or "reject-proposal" in joined


def test_bootstrap_retries_on_underspecified_response(kb_root):
    bad = json.dumps(
        {
            "version": "v1",
            "policy_schema_version": 1,
            "domain": {
                "slug": "retry-domain",
                "topic": "x",
                "field": "x",
                "description": "x",
            },
            "filter": {"threshold_include": 0.7, "threshold_review": 0.5},
            "inclusion_criteria": ["only one"],
            "exclusion_criteria": [],
            "quality_signals": {},
        }
    )
    good = _good_policy_response("retry-domain")
    client = StubPlanClient([bad, good])

    result = bootstrap_domain(
        description="A retry test domain with enough words to clear the short threshold",
        slug="retry-domain",
        plan_client=client,
    )
    assert result.success, result.errors
    assert client.calls == 2


def test_bootstrap_saves_draft_when_retry_fails(kb_root):
    bad1 = json.dumps(
        {
            "version": "v1",
            "policy_schema_version": 1,
            "domain": {"slug": "draft-domain", "topic": "x", "field": "x", "description": "x"},
            "filter": {"threshold_include": 0.7, "threshold_review": 0.5},
            "inclusion_criteria": ["only one"],
            "exclusion_criteria": [],
            "quality_signals": {},
        }
    )
    client = StubPlanClient([bad1, bad1])

    result = bootstrap_domain(
        description="A failed retry test domain with enough length to satisfy the threshold",
        slug="draft-domain",
        plan_client=client,
    )
    assert not result.success
    draft = paths.policies_dir() / "draft-domain" / "policy.draft.yaml"
    assert draft.exists()
    final = policy_path("draft-domain")
    assert not final.exists()


def test_bootstrap_rejects_unparseable_response(kb_root):
    client = StubPlanClient("not json at all")
    result = bootstrap_domain(
        description="x", slug="bad-domain", plan_client=client
    )
    assert not result.success


def test_bootstrap_warns_on_short_description(kb_root):
    client = StubPlanClient(_good_policy_response("short-desc"))
    result = bootstrap_domain(
        description="too short",
        slug="short-desc",
        plan_client=client,
    )
    assert result.success
    assert any("description" in w.lower() for w in result.warnings)


def test_bootstrap_synthetic_reference_in_prompt_not_in_output(kb_root):
    client = StubPlanClient(_good_policy_response("anti-cargo-cult"))
    result = bootstrap_domain(
        description="A fully unrelated domain about something else entirely with enough words",
        slug="anti-cargo-cult",
        plan_client=client,
    )
    assert result.success
    assert "Patagonian" in (client.last_prompt or "")
    final = policy_path("anti-cargo-cult").read_text()
    assert "Patagonian" not in final
    assert "glacier" not in final.lower()


def test_bootstrap_prompt_instructs_channel_authority_for_video_domains(kb_root):
    """Video/talk-heavy domains need channel_authority + speaker_expertise
    quality_signals so the filter weights source authority over thin video
    metadata. The policy-gen prompt must carry that instruction (the model
    decides whether the domain is video-likely and emits the signals)."""
    client = StubPlanClient(_good_policy_response("video-domain"))
    result = bootstrap_domain(
        description="A domain that draws heavily on recorded conference talks, "
        "seminars, and lecture series with enough descriptive words",
        slug="video-domain",
        plan_client=client,
    )
    assert result.success, result.errors

    prompt = client.last_prompt or ""
    # The two signal categories the filter relies on for video sources.
    assert "channel_authority" in prompt
    assert "speaker_expertise" in prompt
    # The trigger condition (video/talk sources) and its rationale.
    assert "video" in prompt.lower()
    assert "lecture" in prompt.lower() or "talk" in prompt.lower()
    # Domain-agnostic: must not hard-code AI-specific venues/institutions
    # (no surface-anchor leakage from the agentic-data-layer policy).
    assert "NeurIPS" not in prompt
    assert "Stanford" not in prompt


def test_bootstrap_force_overwrites_non_promoted_policy(kb_root):
    target = policy_path("forceable")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("version: v1\ndomain:\n  slug: forceable\n")
    client = StubPlanClient(_good_policy_response("forceable"))
    result = bootstrap_domain(
        description="A forceable target description with enough length to be specific",
        slug="forceable",
        plan_client=client,
        force=True,
    )
    assert result.success, result.errors
    data = yaml.safe_load(target.read_text())
    assert len(data["inclusion_criteria"]) >= 3
