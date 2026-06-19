"""Tests for retraction.cascade (G4), retraction.acts_to_reopen (G3),
and retraction.reverse_merge_plan (G8).

Step 0 verified schemas (see retraction.py header comment):
- Resolution act keys: rule, policy_version, inputs, winner, loser, resolved_at
  winner/loser each have: source, claim, trust
- Tombstone frontmatter keys: type, title, merged_into (target_slug), redirect (wikilink)
- Provenance decision_basis["merge_reattachment"]: target, tombstone, aliases_unioned,
  sections_carried, claims_unioned
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from gateway import retraction
from gateway import frontmatter as fm
from gateway import paths
from gateway import contradictions_log


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _synth(slug: str, synthesizes: list[str], body_extra: str = "") -> None:
    d = paths.wiki_dir() / "synthesis"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": slug.replace("-", " "),
        "synthesizes": list(synthesizes),
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    body = (
        f"# {slug}\n\n"
        "## Included works\n"
        + "".join(f"- [[{s}]]\n" for s in synthesizes)
        + f"\n## Analysis\n\nLoad-bearing claim [[{synthesizes[0]}]].\n{body_extra}"
    )
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def _raw_source(source_id: str, *, retracted: bool = False) -> None:
    """Write a minimal raw/pubmed/<id>.md (used by acts_to_reopen and retracted-citations lint)."""
    raw_dir = paths.raw_dir() / "pubmed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "pubmed",
        "id": source_id,
        "title": f"Paper {source_id}",
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
    }
    if retracted:
        front["retracted"] = True
    body = f"# Paper {source_id}\n\nAbstract content.\n"
    (raw_dir / f"{source_id}.md").write_text(fm.serialize(front, body))


# ===========================================================================
# G4 — transitive synthesizes: cascade
# ===========================================================================

def test_cascade_flags_transitive_dependents_to_fixpoint(kb_root):
    # source pubmed-1 -> A synthesizes it -> B synthesizes A
    _synth("a", ["sources/pubmed-1"])
    _synth("b", ["synthesis/a"])
    res = retraction.cascade({"pubmed-1"})
    flagged = set(res.flagged)
    assert "wiki/synthesis/a.md" in flagged
    assert "wiki/synthesis/b.md" in flagged   # transitive
    assert res.depth >= 2


def test_cascade_terminates_on_cycle(kb_root):
    _synth("x", ["synthesis/y", "sources/pubmed-1"])
    _synth("y", ["synthesis/x"])
    res = retraction.cascade({"pubmed-1"})
    assert res.terminated_on_cycle is True
    assert {"wiki/synthesis/x.md", "wiki/synthesis/y.md"} <= set(res.flagged)


def test_cascade_negative_control_unrelated_page_not_flagged(kb_root):
    _synth("a", ["sources/pubmed-1"])
    _synth("unrelated", ["sources/pubmed-2"])   # cites a DIFFERENT, non-retracted source
    res = retraction.cascade({"pubmed-1"})
    assert "wiki/synthesis/unrelated.md" not in set(res.flagged)


def test_cascade_empty_retracted_set_returns_no_flagged(kb_root):
    """Negative control: empty input yields empty result."""
    _synth("a", ["sources/pubmed-1"])
    res = retraction.cascade(set())
    assert res.flagged == []
    assert res.depth == 0
    assert res.terminated_on_cycle is False


def test_cascade_single_level_source_citation(kb_root):
    """A page that cites a retracted source via [[sources/X]] in body is flagged."""
    _synth("direct", ["sources/retracted-99"])
    res = retraction.cascade({"retracted-99"})
    assert "wiki/synthesis/direct.md" in set(res.flagged)
    assert res.depth >= 1


def test_cascade_multiple_retracted_sources(kb_root):
    """Multiple retracted sources union their dependent sets."""
    _synth("a1", ["sources/pub-1"])
    _synth("a2", ["sources/pub-2"])
    _synth("b", ["synthesis/a1", "synthesis/a2"])
    res = retraction.cascade({"pub-1", "pub-2"})
    flagged = set(res.flagged)
    assert "wiki/synthesis/a1.md" in flagged
    assert "wiki/synthesis/a2.md" in flagged
    assert "wiki/synthesis/b.md" in flagged


def test_cascade_returns_deterministic_order(kb_root):
    """flagged list is deterministic across calls (sorted by rel_path)."""
    _synth("alpha", ["sources/pubmed-1"])
    _synth("beta", ["sources/pubmed-1"])
    res1 = retraction.cascade({"pubmed-1"})
    res2 = retraction.cascade({"pubmed-1"})
    assert res1.flagged == res2.flagged


# ===========================================================================
# G3 — acts_to_reopen
# ===========================================================================

def test_acts_to_reopen_returns_acts_for_retracted_winner(kb_root):
    """acts_to_reopen returns acts where the winner's source was retracted."""
    # Write a real resolution act
    act = {
        "rule": "trust-tier-then-recency",
        "policy_version": "contradiction-policy-v1",
        "inputs": {
            "a": {"source": "pubmed-winner", "claim": "X reduces Y", "source_type": "pubmed"},
            "b": {"source": "arxiv-loser", "claim": "X does not reduce Y", "source_type": "arxiv"},
        },
        "winner": {"source": "pubmed-winner", "claim": "X reduces Y", "trust": 0.9},
        "loser": {"source": "arxiv-loser", "claim": "X does not reduce Y", "trust": 0.5},
    }
    contradictions_log.append_resolution_act(act)

    result = retraction.acts_to_reopen({"pubmed-winner"})
    assert len(result) == 1
    assert result[0]["winner"]["source"] == "pubmed-winner"
    assert "resolved_at" in result[0]  # appended by append_resolution_act


def test_acts_to_reopen_negative_control_unrelated_source(kb_root):
    """acts_to_reopen returns [] when the retracted source is not a winner."""
    act = {
        "rule": "trust-tier-then-recency",
        "policy_version": "contradiction-policy-v1",
        "inputs": {"a": {}, "b": {}},
        "winner": {"source": "pubmed-winner", "claim": "X reduces Y", "trust": 0.9},
        "loser": {"source": "arxiv-loser", "claim": "X does not reduce Y", "trust": 0.5},
    }
    contradictions_log.append_resolution_act(act)

    result = retraction.acts_to_reopen({"arxiv-loser"})
    assert result == []


def test_acts_to_reopen_empty_when_no_acts(kb_root):
    """Empty JSONL → empty result (no crash)."""
    result = retraction.acts_to_reopen({"pubmed-1"})
    assert result == []


def test_acts_to_reopen_skips_already_reverted_acts(kb_root):
    """Acts carrying a reverts_act marker (already reversed) are excluded."""
    act = {
        "rule": "trust-tier-then-recency",
        "policy_version": "contradiction-policy-v1",
        "inputs": {"a": {}, "b": {}},
        "winner": {"source": "pubmed-winner", "claim": "X reduces Y", "trust": 0.9},
        "loser": {"source": "arxiv-loser", "claim": "No.", "trust": 0.5},
        "reverts_act": "some-prior-revert",  # already reverted marker
    }
    contradictions_log.append_resolution_act(act)

    result = retraction.acts_to_reopen({"pubmed-winner"})
    assert result == []


def test_acts_to_reopen_multiple_acts_filters_correctly(kb_root):
    """Only acts where winner.source ∈ retracted_ids are returned."""
    for winner_src in ("pub-A", "pub-B", "pub-C"):
        act = {
            "rule": "trust-tier-then-recency",
            "policy_version": "contradiction-policy-v1",
            "inputs": {"a": {}, "b": {}},
            "winner": {"source": winner_src, "claim": "claim", "trust": 0.9},
            "loser": {"source": "loser-X", "claim": "counter", "trust": 0.3},
        }
        contradictions_log.append_resolution_act(act)

    result = retraction.acts_to_reopen({"pub-A", "pub-C"})
    winner_sources = {a["winner"]["source"] for a in result}
    assert winner_sources == {"pub-A", "pub-C"}


# ===========================================================================
# G8 — reverse_merge_plan (realistic payloads)
# ===========================================================================

def _write_entity(rel: str, front: dict, body: str, *, kb_root: Path) -> None:
    p = kb_root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fm.serialize(front, body))


def _write_tombstone(rel: str, merged_into: str, title: str, *, kb_root: Path) -> None:
    """Write a realistic tombstone as commit_gate.py produces it."""
    target_rel = f"wiki/entities/{merged_into}.md"
    front = {
        "type": "entity",
        "title": title,
        "merged_into": merged_into,
        "redirect": f"[[{target_rel[len('wiki/'):-len('.md')]}]]",
    }
    body = (
        f"# {title}\n\n"
        f"Merged into [[{target_rel[len('wiki/'):-len('.md')]}]] "
        f"(dedup §5.3). This page is a redirect tombstone.\n"
    )
    p = kb_root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fm.serialize(front, body))


def _write_provenance_node(
    intent_id: str,
    merge_reattachment: dict,
    *,
    kb_root: Path,
) -> None:
    """Write a minimal provenance node with a merge_reattachment basis."""
    nodes_path = kb_root / ".knowledge" / "provenance" / "nodes.jsonl"
    nodes_path.parent.mkdir(parents=True, exist_ok=True)
    node = {
        "node_id": f"prov-{intent_id}",
        "intent_id": intent_id,
        "decision_basis": {
            "merge_reattachment": merge_reattachment,
        },
        "recorded_at": "2026-01-01T00:00:00Z",
    }
    with nodes_path.open("a") as f:
        f.write(json.dumps(node) + "\n")


def test_reverse_merge_plan_realistic_payload(kb_root):
    """reverse_merge_plan returns a plan carrying aliases, sections, and claims from B."""
    canonical_rel = "wiki/entities/semaglutide.md"
    tombstone_rel = "wiki/entities/ozempic-brand.md"

    # Write the canonical entity (the merge target)
    can_front = {
        "type": "entity",
        "slug": "semaglutide",
        "title": "Semaglutide",
        "aliases": ["GLP-1 agonist"],
        "entity_kind": "drug",
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
    }
    can_body = (
        "# Semaglutide\n\n"
        "Semaglutide is a GLP-1 receptor agonist [[sources/pubmed-1]].\n\n"
        "## Mechanism\n\nActs on GLP-1R [[sources/pubmed-2]].\n\n"
        "## Claims\n"
        "- Reduces HbA1c [[sources/pubmed-1]]\n"
        "- Weight loss of 15% [[sources/pubmed-3]]\n"
    )
    _write_entity(canonical_rel, can_front, can_body, kb_root=kb_root)

    # Write the tombstone (the merged deposit B)
    _write_tombstone(tombstone_rel, "semaglutide", "Ozempic Brand", kb_root=kb_root)

    # Write a provenance node recording what B contributed
    _write_provenance_node(
        "intent-merge-001",
        {
            "target": canonical_rel,
            "tombstone": tombstone_rel,
            "aliases_unioned": ["Ozempic", "semaglutide injection"],
            "sections_carried": ["## Side Effects"],
            "claims_unioned": [
                "Nausea in 20% of patients [[sources/pubmed-4]]",
                "Injection-site reactions [[sources/pubmed-5]]",
            ],
        },
        kb_root=kb_root,
    )

    plan = retraction.reverse_merge_plan(tombstone_rel)

    assert plan.canonical_rel == canonical_rel
    assert plan.tombstone_to_delete == tombstone_rel
    assert set(plan.aliases_to_remove) == {"Ozempic", "semaglutide injection"}
    assert "## Side Effects" in plan.sections_to_remove
    assert len(plan.claims_to_remove) == 2


def test_reverse_merge_plan_non_tombstone_raises(kb_root):
    """A canonical page (no merged_into) yields ValueError, not a spurious plan."""
    canonical_rel = "wiki/entities/semaglutide.md"
    can_front = {
        "type": "entity",
        "slug": "semaglutide",
        "title": "Semaglutide",
        "entity_kind": "drug",
        "domains": ["med"],
    }
    can_body = "# Semaglutide\n\nA drug.\n"
    _write_entity(canonical_rel, can_front, can_body, kb_root=kb_root)

    with pytest.raises((ValueError, KeyError)):
        retraction.reverse_merge_plan(canonical_rel)


def test_reverse_merge_plan_missing_file_raises(kb_root):
    """A nonexistent rel_path yields an error, not a silent empty plan."""
    with pytest.raises((FileNotFoundError, ValueError, KeyError)):
        retraction.reverse_merge_plan("wiki/entities/does-not-exist.md")
