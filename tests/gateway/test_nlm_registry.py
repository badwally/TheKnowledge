"""Tests for the hybrid (persistent + sessions) notebook registry.

Schema migration: the registry must transparently read both the legacy
flat schema (`notebook_id`, `created_at`, etc. at the domain level) and
the new nested schema (`persistent: {...}, sessions: [...]`). On first
write, the file is normalized to the nested schema.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway import nlm_registry


# --- helpers --------------------------------------------------------------


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, default_flow_style=False))


def _read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


# --- legacy schema reads --------------------------------------------------


def test_legacy_flat_schema_read_via_get_notebook_id(kb_root):
    _write_yaml(
        nlm_registry.notebooks_yaml_path(),
        {
            "notebooks": {
                "obesity": {
                    "notebook_id": "nb_legacy_obesity",
                    "created_at": "2025-12-01",
                    "sources_count": 47,
                    "last_sync": "2026-04-01T00:00:00Z",
                }
            }
        },
    )
    assert nlm_registry.get_notebook_id("obesity") == "nb_legacy_obesity"
    assert nlm_registry.get_persistent("obesity") == "nb_legacy_obesity"
    # load() still returns the persistent NotebookEntry shape
    entries = nlm_registry.load()
    assert entries["obesity"].notebook_id == "nb_legacy_obesity"
    assert entries["obesity"].sources_count == 47


def test_legacy_schema_normalized_on_next_write(kb_root):
    _write_yaml(
        nlm_registry.notebooks_yaml_path(),
        {
            "notebooks": {
                "obesity": {
                    "notebook_id": "nb_legacy_obesity",
                    "created_at": "2025-12-01",
                    "sources_count": 47,
                    "last_sync": "2026-04-01T00:00:00Z",
                }
            }
        },
    )
    nlm_registry.update_last_sync("obesity")

    raw = _read_yaml(nlm_registry.notebooks_yaml_path())
    block = raw["notebooks"]["obesity"]
    assert "persistent" in block
    assert block["persistent"]["notebook_id"] == "nb_legacy_obesity"
    assert block["persistent"]["sources_count"] == 47
    # No legacy keys left at the domain level
    assert "notebook_id" not in block
    assert "created_at" not in block


# --- register / increment / sync round-trips ------------------------------


def test_register_creates_nested_schema(kb_root):
    nlm_registry.register("d1", "nb-1")
    raw = _read_yaml(nlm_registry.notebooks_yaml_path())
    assert raw["notebooks"]["d1"]["persistent"]["notebook_id"] == "nb-1"
    assert nlm_registry.get_notebook_id("d1") == "nb-1"


def test_increment_sources_round_trip(kb_root):
    nlm_registry.register("d1", "nb-1")
    nlm_registry.increment_sources("d1", by=3)
    nlm_registry.increment_sources("d1")
    entries = nlm_registry.load()
    assert entries["d1"].sources_count == 4


def test_register_idempotent_preserves_created_at(kb_root):
    first = nlm_registry.register("d1", "nb-1")
    again = nlm_registry.register("d1", "nb-1")
    assert again.created_at == first.created_at


# --- sessions: register + list -------------------------------------------


def test_register_session_then_list(kb_root):
    nlm_registry.register("obesity", "nb_persist")
    nlm_registry.register_session(
        "obesity",
        "2026-04-29-glp1-cardiovascular",
        "nb_session_xyz",
        query="What does GLP-1 do to cardiovascular outcomes?",
    )
    sessions = nlm_registry.list_sessions("obesity")
    assert len(sessions) == 1
    s = sessions[0]
    assert s["session_id"] == "2026-04-29-glp1-cardiovascular"
    assert s["notebook_id"] == "nb_session_xyz"
    assert s["status"] == nlm_registry.EPHEMERAL
    assert s["sources_count"] == 0
    assert s["promoted_at"] is None
    assert s["query"].startswith("What does GLP-1")


def test_register_session_without_persistent_notebook_ok(kb_root):
    nlm_registry.register_session(
        "newdomain",
        "sess-1",
        "nb_sess",
        query="exploring",
    )
    assert nlm_registry.get_persistent("newdomain") is None
    assert len(nlm_registry.list_sessions("newdomain")) == 1


def test_register_session_duplicate_id_raises(kb_root):
    nlm_registry.register("d1", "nb-1")
    nlm_registry.register_session("d1", "sess-a", "nb-a", query="q")
    with pytest.raises(ValueError, match="already registered"):
        nlm_registry.register_session("d1", "sess-a", "nb-b", query="q2")


def test_register_session_replaces_abandoned_entry(kb_root):
    """Convergent re-registration: abandoning then re-registering a session
    with the same id is allowed (matches the convergent-ops principle —
    re-running `wiki research --execute X` should not crash on a prior
    abandoned attempt)."""
    nlm_registry.register("d1", "nb-1")
    nlm_registry.register_session("d1", "sess-x", "nb-old", query="q-old")
    nlm_registry.mark_abandoned("d1", "sess-x")

    nlm_registry.register_session("d1", "sess-x", "nb-fresh", query="q-fresh")

    sess = nlm_registry.get_session("d1", "sess-x")
    assert sess is not None
    assert sess["notebook_id"] == "nb-fresh"
    assert sess["query"] == "q-fresh"
    assert sess["status"] == nlm_registry.EPHEMERAL


def test_register_session_refuses_active_duplicate(kb_root):
    """An ephemeral (in-flight) session of the same id must NOT be silently
    overwritten — that could clobber an in-progress run."""
    nlm_registry.register("d1", "nb-1")
    nlm_registry.register_session("d1", "sess-y", "nb-active", query="q")
    with pytest.raises(ValueError, match="already registered"):
        nlm_registry.register_session("d1", "sess-y", "nb-other", query="q2")


def test_get_session_returns_none_when_missing(kb_root):
    nlm_registry.register("d1", "nb-1")
    assert nlm_registry.get_session("d1", "nope") is None
    assert nlm_registry.get_session("nodomain", "anything") is None


def test_list_sessions_filter_by_status(kb_root):
    nlm_registry.register("d1", "nb-1")
    nlm_registry.register_session("d1", "s-a", "nb-a", query="qa")
    nlm_registry.register_session("d1", "s-b", "nb-b", query="qb")
    nlm_registry.mark_abandoned("d1", "s-b")

    eph = nlm_registry.list_sessions("d1", status=nlm_registry.EPHEMERAL)
    assert [s["session_id"] for s in eph] == ["s-a"]

    aban = nlm_registry.list_sessions("d1", status=nlm_registry.ABANDONED)
    assert [s["session_id"] for s in aban] == ["s-b"]


def test_list_sessions_invalid_status_raises(kb_root):
    nlm_registry.register("d1", "nb-1")
    with pytest.raises(ValueError):
        nlm_registry.list_sessions("d1", status="bogus")


# --- promote / abandon ----------------------------------------------------


def test_mark_promoted_flips_status_and_bumps_persistent(kb_root):
    nlm_registry.register("d1", "nb-1")
    nlm_registry.increment_sources("d1", by=5)  # baseline persistent count
    nlm_registry.register_session("d1", "sess-x", "nb-x", query="q")

    nlm_registry.mark_promoted("d1", "sess-x", sources_added=12)

    sess = nlm_registry.get_session("d1", "sess-x")
    assert sess is not None
    assert sess["status"] == nlm_registry.PROMOTED
    assert sess["promoted_at"] is not None and sess["promoted_at"] != ""

    persistent_count = nlm_registry.load()["d1"].sources_count
    assert persistent_count == 5 + 12


def test_mark_promoted_without_persistent_does_not_crash(kb_root):
    nlm_registry.register_session("d1", "sess-x", "nb-x", query="q")
    nlm_registry.mark_promoted("d1", "sess-x", sources_added=4)
    sess = nlm_registry.get_session("d1", "sess-x")
    assert sess is not None and sess["status"] == nlm_registry.PROMOTED
    # No persistent entry was synthesized
    assert nlm_registry.get_persistent("d1") is None


def test_mark_promoted_unknown_session_raises(kb_root):
    nlm_registry.register("d1", "nb-1")
    with pytest.raises(KeyError):
        nlm_registry.mark_promoted("d1", "nope", sources_added=1)
    with pytest.raises(KeyError):
        nlm_registry.mark_promoted("nodomain", "nope", sources_added=1)


def test_mark_abandoned_flips_status(kb_root):
    nlm_registry.register("d1", "nb-1")
    nlm_registry.register_session("d1", "sess-y", "nb-y", query="q")
    nlm_registry.mark_abandoned("d1", "sess-y")
    sess = nlm_registry.get_session("d1", "sess-y")
    assert sess is not None and sess["status"] == nlm_registry.ABANDONED
    assert "sess-y" in [
        s["session_id"]
        for s in nlm_registry.list_sessions("d1", status=nlm_registry.ABANDONED)
    ]


def test_mark_abandoned_unknown_raises(kb_root):
    nlm_registry.register("d1", "nb-1")
    with pytest.raises(KeyError):
        nlm_registry.mark_abandoned("d1", "nope")


# --- per-session source counter ------------------------------------------


def test_increment_session_sources_bumps_only_target_session(kb_root):
    nlm_registry.register("d1", "nb-1")
    nlm_registry.register_session("d1", "s-a", "nb-a", query="qa")
    nlm_registry.register_session("d1", "s-b", "nb-b", query="qb")

    nlm_registry.increment_session_sources("d1", "s-a", n=3)
    nlm_registry.increment_session_sources("d1", "s-a")

    a = nlm_registry.get_session("d1", "s-a")
    b = nlm_registry.get_session("d1", "s-b")
    assert a is not None and b is not None
    assert a["sources_count"] == 4
    assert b["sources_count"] == 0


def test_increment_session_sources_unknown_raises(kb_root):
    nlm_registry.register("d1", "nb-1")
    with pytest.raises(KeyError):
        nlm_registry.increment_session_sources("d1", "nope")


# --- backwards-compat invariants -----------------------------------------


def test_existing_callers_unaffected(kb_root):
    """Replicates the smoke test from test_nlm.py to guarantee compat."""
    assert nlm_registry.get_notebook_id("d1") is None
    nlm_registry.register("d1", "nb-1")
    assert nlm_registry.get_notebook_id("d1") == "nb-1"
    nlm_registry.increment_sources("d1", by=3)
    entry = nlm_registry.load()["d1"]
    assert entry.sources_count == 3


def test_save_preserves_existing_sessions(kb_root):
    """save() with a domain → persistent map should not wipe sessions."""
    nlm_registry.register("d1", "nb-1")
    nlm_registry.register_session("d1", "sess-a", "nb-a", query="q")

    # Take the persistent map, modify it, save it back. Sessions must survive.
    entries = nlm_registry.load()
    entries["d1"].sources_count = 99
    nlm_registry.save(entries)

    assert nlm_registry.load()["d1"].sources_count == 99
    sessions = nlm_registry.list_sessions("d1")
    assert len(sessions) == 1
    assert sessions[0]["session_id"] == "sess-a"
