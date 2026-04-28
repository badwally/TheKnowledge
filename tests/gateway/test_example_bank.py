"""Tests for M19: example bank + policy backfill from legacy artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from gateway import paths
from gateway.filter import examples as example_bank
from gateway.filter.policy import load_policy
from gateway.ops.example_bank import (
    backfill,
    backfill_examples,
    backfill_policy,
)


# --- policy backfill -------------------------------------------------------


def _write_legacy_config(tmp_path: Path, *, body: dict) -> Path:
    target = tmp_path / "config" / "domains" / "test-domain.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(yaml.safe_dump(body))
    return target


def test_backfill_policy_writes_canonical_schema(kb_root, tmp_path):
    legacy = _write_legacy_config(
        tmp_path,
        body={
            "version": "0.2.0",
            "domain": {
                "topic": "test topic",
                "field": "test field",
                "description": "long description here",
            },
            "inclusion_criteria": {
                "required": ["item one", "item two"],
            },
            "exclusion_criteria": {
                "hard_exclude": ["bad thing"],
            },
            "quality_signals": {
                "channel_authority": {"positive_signals": ["a"]},
            },
        },
    )
    target = backfill_policy(legacy, "d-x")

    policy_obj = load_policy("d-x")
    assert policy_obj.domain_slug == "d-x"
    assert policy_obj.domain_topic == "test topic"
    assert policy_obj.inclusion_criteria == ["item one", "item two"]
    assert policy_obj.exclusion_criteria == ["bad thing"]
    assert policy_obj.threshold_include == 0.70
    assert policy_obj.threshold_review == 0.50
    assert policy_obj.quality_signals["channel_authority"]["positive_signals"] == ["a"]
    assert target == paths.policies_dir() / "d-x" / "policy.yaml"


def test_backfill_policy_handles_flat_criteria_lists(kb_root, tmp_path):
    legacy = _write_legacy_config(
        tmp_path,
        body={
            "domain": {"topic": "t"},
            "inclusion_criteria": ["a", "b"],
            "exclusion_criteria": ["c"],
        },
    )
    backfill_policy(legacy, "d-flat")
    policy_obj = load_policy("d-flat")
    assert policy_obj.inclusion_criteria == ["a", "b"]
    assert policy_obj.exclusion_criteria == ["c"]


def test_backfill_policy_missing_file_raises(kb_root, tmp_path):
    with pytest.raises(FileNotFoundError):
        backfill_policy(tmp_path / "nope.yaml", "d-x")


# --- example-bank backfill -------------------------------------------------


def _write_legacy_json(path: Path, payload) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload))
    return path


def test_backfill_examples_pubmed_arxiv_youtube(kb_root, tmp_path):
    payload = [
        {
            "item_id": "pmid:22128031",
            "source_type": "pubmed",
            "title": "GLP-1 NTS projections",
            "authors": ["A", "B"],
            "publish_date": "2011-11-29",
            "relevance_score": 5,
            "included": True,
            "inclusion_rationale": "central paper",
            "description": "Abstract of pubmed paper.",
        },
        {
            "item_id": "arxiv:2404.01358v2",
            "source_type": "arxiv",
            "title": "GLP-1 in mesolimbic circuitry",
            "authors": ["C"],
            "publish_date": "2024-04-02",
            "relevance_score": 3,
            "included": False,
            "inclusion_rationale": "tangential",
            "description": "Arxiv abstract.",
        },
        {
            "video_id": "_5qjj2CzBSw",
            "title": "Ozempic and the Brain",
            "channel_name": "Show",
            "publish_date": "2026-01-14T15:30:23Z",
            "relevance_score": 4,
            "included": True,
            "inclusion_rationale": "credible synthesis",
            "description": "Video description text.",
            "url": "https://youtube.com/watch?v=_5qjj2CzBSw",
        },
    ]
    json_path = _write_legacy_json(tmp_path / "scored.json", payload)

    report = backfill_examples([json_path], "d-x")
    assert report.written == 3
    assert report.skipped == 0
    assert report.errors == []

    examples = example_bank.load_all("d-x")
    by_id = {e.source_id: e for e in examples}
    assert set(by_id.keys()) == {"pubmed-22128031", "arxiv-2404.01358", "yt-_5qjj2CzBSw"}
    assert by_id["pubmed-22128031"].decision == "include"
    assert by_id["pubmed-22128031"].score == 1.0
    assert by_id["arxiv-2404.01358"].decision == "exclude"
    assert by_id["arxiv-2404.01358"].score == 0.6
    assert by_id["yt-_5qjj2CzBSw"].decision == "include"
    assert by_id["yt-_5qjj2CzBSw"].score == 0.8
    for e in examples:
        assert e.pinned_by == "legacy-backfill"
        assert e.policy_version == "d-x-legacy-v1"


def test_backfill_examples_handles_dict_payload_with_videos_list(kb_root, tmp_path):
    payload = {
        "metadata": {"x": 1},
        "videos": [
            {
                "video_id": "abc12345678",
                "title": "T",
                "publish_date": "2024-01-01T00:00:00Z",
                "relevance_score": 5,
                "included": True,
                "inclusion_rationale": "ok",
                "description": "d",
            }
        ],
    }
    p = _write_legacy_json(tmp_path / "vids.json", payload)
    report = backfill_examples([p], "d-y")
    assert report.written == 1
    assert example_bank.load_all("d-y")[0].source_id == "yt-abc12345678"


def test_backfill_examples_skips_records_without_decision(kb_root, tmp_path):
    payload = [
        {
            "item_id": "pmid:1",
            "relevance_score": 5,
            "title": "T",
        }
    ]
    p = _write_legacy_json(tmp_path / "scored.json", payload)
    report = backfill_examples([p], "d-z")
    assert report.written == 0
    assert report.skipped == 1


def test_backfill_examples_invalid_json_recorded_as_error(kb_root, tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{not valid json")
    report = backfill_examples([p], "d-z")
    assert report.written == 0
    assert any("invalid JSON" in e for e in report.errors)


def test_backfill_examples_unknown_id_shape_skipped(kb_root, tmp_path):
    payload = [
        {
            "item_id": "doi:10.1234/abc",
            "relevance_score": 4,
            "included": True,
            "inclusion_rationale": "x",
            "title": "Doi paper",
        }
    ]
    p = _write_legacy_json(tmp_path / "scored.json", payload)
    report = backfill_examples([p], "d-z")
    assert report.written == 0
    assert report.skipped == 1


def test_backfill_examples_url_fallback_for_youtube(kb_root, tmp_path):
    payload = [
        {
            "url": "https://www.youtube.com/watch?v=Zyx_8a-bC4D",
            "title": "URL-only YT",
            "relevance_score": 4,
            "included": True,
            "inclusion_rationale": "ok",
            "description": "desc",
        }
    ]
    p = _write_legacy_json(tmp_path / "yt.json", payload)
    report = backfill_examples([p], "d-yt")
    assert report.written == 1
    assert example_bank.load_all("d-yt")[0].source_id == "yt-Zyx_8a-bC4D"


# --- top-level convenience driver -----------------------------------------


def test_backfill_runs_both_policy_and_examples(kb_root, tmp_path):
    legacy = _write_legacy_config(
        tmp_path,
        body={
            "domain": {"topic": "x"},
            "inclusion_criteria": ["a"],
            "exclusion_criteria": ["b"],
        },
    )
    json_path = _write_legacy_json(
        tmp_path / "items.json",
        [
            {
                "item_id": "pmid:1",
                "title": "T",
                "publish_date": "2020-01-01",
                "relevance_score": 4,
                "included": True,
                "inclusion_rationale": "ok",
            }
        ],
    )
    summary = backfill(
        domain_slug="d-z",
        legacy_config_path=legacy,
        json_paths=[json_path],
    )
    assert summary["domain"] == "d-z"
    assert summary["examples_written"] == 1
    assert load_policy("d-z").domain_topic == "x"
