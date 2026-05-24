"""Tests for the Golden / EvalResult schema (M50 Phase A)."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway.evaluate.schema import (
    Golden,
    EvalResult,
    EvalRunSummary,
    load_goldens,
    save_goldens,
    SchemaError,
)


def test_golden_roundtrip_yaml(tmp_path):
    path = tmp_path / "goldens.yaml"
    goldens = [
        Golden(
            id="q01",
            question="Does GLP-1 reduce food-cue reactivity in the ventral striatum?",
            must_cite=["pubmed-12345", "pubmed-67890"],
            must_assert=[
                "GLP-1 receptor agonists reduce food-cue reactivity",
                "The effect is most pronounced in the ventral striatum",
            ],
            must_not_assert=["GLP-1 has no effect on reward circuitry"],
            rubric_weight={"cite": 0.4, "assert": 0.5, "anti": 0.1},
        )
    ]
    save_goldens(path, goldens)
    loaded = load_goldens(path)
    assert len(loaded) == 1
    g = loaded[0]
    assert g.id == "q01"
    assert g.must_cite == ["pubmed-12345", "pubmed-67890"]
    assert g.must_assert[0].startswith("GLP-1 receptor agonists")
    assert g.must_not_assert == ["GLP-1 has no effect on reward circuitry"]
    assert g.rubric_weight["cite"] == 0.4


def test_golden_missing_id_raises_schema_error(tmp_path):
    path = tmp_path / "goldens.yaml"
    path.write_text(
        "goldens:\n"
        "  - question: q?\n"
        "    must_cite: []\n"
        "    must_assert: []\n"
        "    must_not_assert: []\n"
    )
    with pytest.raises(SchemaError, match="missing required field: id"):
        load_goldens(path)


def test_golden_duplicate_id_raises(tmp_path):
    path = tmp_path / "goldens.yaml"
    save_goldens(path, [
        Golden(id="dup", question="a", must_cite=[], must_assert=[], must_not_assert=[]),
        Golden(id="dup", question="b", must_cite=[], must_assert=[], must_not_assert=[]),
    ])
    with pytest.raises(SchemaError, match="duplicate id"):
        load_goldens(path)


def test_scaffold_writes_template_with_one_example(tmp_path):
    from gateway.evaluate.schema import scaffold_template

    target = tmp_path / "eval" / "test-domain" / "goldens.yaml"
    written = scaffold_template(target, domain="test-domain")

    assert written == target
    assert target.exists()
    goldens = load_goldens(target)
    assert len(goldens) == 1
    assert "test-domain" in goldens[0].question or "EXAMPLE" in goldens[0].question
    assert goldens[0].id == "q01"


def test_scaffold_refuses_to_overwrite(tmp_path):
    from gateway.evaluate.schema import scaffold_template

    target = tmp_path / "goldens.yaml"
    scaffold_template(target, domain="d1")
    with pytest.raises(FileExistsError):
        scaffold_template(target, domain="d1")
