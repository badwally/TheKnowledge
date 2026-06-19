"""Keep-worthiness fields + orient-vs-ground gate on deposit._validate.

The orient-vs-ground gate rejects a deposit where:
- durable=True AND
- the body has no [[sources/<id>]] wikilink that resolves to a real raw/ page

Volatile deposits (volatile=True) are accepted but carry data={"canonicalize": False}.

Keep-worthiness fields (half_life, load_bearing, domain_core, recurrence, durable,
volatile) are optional and nullable; wrong type yields rejection.

Named negative controls:
- NEGATIVE-URL: durable claim with only a bare URL (not [[sources/<id>]]) → rejected.
- NEGATIVE-BROKEN-WIKILINK: durable claim with [[sources/no-such-id]] that has no raw/ page → rejected.
- NEGATIVE-WRONG-TYPE: half_life=True (wrong type, should be str/None) → rejected.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import paths
from gateway.ops.deposit import deposit


# ---------------------------------------------------------------------------
# Fixture: tmp_queue_env (mirrors test_deposit.py)
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_queue_env(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    (tmp_path / ".knowledge").mkdir(parents=True, exist_ok=True)
    return tmp_path


# ---------------------------------------------------------------------------
# Helper: write a real raw/ source page so [[sources/<id>]] resolves
# ---------------------------------------------------------------------------

def _seed_raw_source(tmp_path: Path, source_id: str, source_type: str = "web") -> Path:
    """Create raw/<type>/<id>.md so [[sources/<id>]] resolves to a real file."""
    raw_dir = tmp_path / "raw" / source_type
    raw_dir.mkdir(parents=True, exist_ok=True)
    p = raw_dir / f"{source_id}.md"
    p.write_text(
        f"---\nid: {source_id}\ntype: {source_type}\ntitle: Test Source\n---\n\nBody.\n"
    )
    return p


# ---------------------------------------------------------------------------
# Orient-vs-ground gate — durable claim with non-ingested URL (Step 5 RED)
# ---------------------------------------------------------------------------

def test_durable_claim_with_non_ingested_url_rejected(tmp_queue_env):
    """NEGATIVE-URL: durable=True + bare URL (no [[sources/...]]) → rejected."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "X",
            "body": "Durable claim. See https://example.com/article",
            "durable": True,
        },
        {"canonical_name": "X", "domains": ["med"]},
    )
    assert res.disposition == "rejected"
    assert any("ingested source" in e for e in (res.errors or []))


def test_durable_claim_with_broken_wikilink_rejected(tmp_queue_env):
    """NEGATIVE-BROKEN-WIKILINK: [[sources/no-such-id]] has no raw/ file → rejected."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "X",
            "body": "Durable claim [[sources/no-such-id]].",
            "durable": True,
        },
        {"canonical_name": "X", "domains": ["med"]},
    )
    assert res.disposition == "rejected"
    assert any("ingested source" in e for e in (res.errors or []))


# ---------------------------------------------------------------------------
# Orient-vs-ground gate — durable claim with real ingested source → accepted
# ---------------------------------------------------------------------------

def test_durable_claim_with_ingested_source_accepted(tmp_queue_env):
    """Durable claim backed by a real raw/ source is accepted."""
    _seed_raw_source(tmp_queue_env, "web-1", "web")
    res = deposit(
        {
            "page_type": "concept",
            "title": "X",
            "body": "Durable claim [[sources/web-1]].",
            "durable": True,
        },
        {"canonical_name": "X", "domains": ["med"]},
    )
    assert res.disposition == "queued", f"errors={res.errors}"


# ---------------------------------------------------------------------------
# Volatile gate — accepted, not canonicalized
# ---------------------------------------------------------------------------

def test_volatile_deposit_not_canonicalized(tmp_queue_env):
    """volatile=True deposit is accepted and carries data.canonicalize=False."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "X",
            "body": "Fast-moving note, may change.",
            "volatile": True,
        },
        {"canonical_name": "X", "domains": ["med"]},
    )
    assert res.disposition == "queued", f"errors={res.errors}"
    assert res.data is not None
    assert res.data.get("canonicalize") is False


# ---------------------------------------------------------------------------
# Keep-worthiness fields — type validation
# ---------------------------------------------------------------------------

def test_keep_worthiness_valid_fields_accepted(tmp_queue_env):
    """All keep-worthiness fields with valid types are accepted."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "Y",
            "body": "Stable claim.",
            "half_life": "long",
            "load_bearing": True,
            "domain_core": True,
            "recurrence": 3,
            "durable": False,
            "volatile": False,
        },
        {"canonical_name": "Y", "domains": ["med"]},
    )
    assert res.disposition == "queued", f"errors={res.errors}"


def test_keep_worthiness_nullable_fields_accepted(tmp_queue_env):
    """Keep-worthiness fields explicitly set to None are accepted (nullable)."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "Z",
            "body": "Some claim.",
            "half_life": None,
            "load_bearing": None,
            "domain_core": None,
            "recurrence": None,
            "durable": None,
            "volatile": None,
        },
        {"canonical_name": "Z", "domains": ["med"]},
    )
    assert res.disposition == "queued", f"errors={res.errors}"


def test_keep_worthiness_wrong_type_rejected(tmp_queue_env):
    """NEGATIVE-WRONG-TYPE: half_life=True (bool when str/None expected) → rejected."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "W",
            "body": "Some claim.",
            "half_life": True,  # wrong: should be str or None
        },
        {"canonical_name": "W", "domains": ["med"]},
    )
    assert res.disposition == "rejected"
    assert any("half_life" in e for e in (res.errors or []))


def test_keep_worthiness_load_bearing_wrong_type_rejected(tmp_queue_env):
    """NEGATIVE-WRONG-TYPE: load_bearing='yes' (str when bool/None expected) → rejected."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "W2",
            "body": "Some claim.",
            "load_bearing": "yes",  # wrong: should be bool or None
        },
        {"canonical_name": "W2", "domains": ["med"]},
    )
    assert res.disposition == "rejected"
    assert any("load_bearing" in e for e in (res.errors or []))


def test_keep_worthiness_recurrence_wrong_type_rejected(tmp_queue_env):
    """NEGATIVE-WRONG-TYPE: recurrence='often' (str when int/None expected) → rejected."""
    res = deposit(
        {
            "page_type": "concept",
            "title": "W3",
            "body": "Some claim.",
            "recurrence": "often",  # wrong: should be int or None
        },
        {"canonical_name": "W3", "domains": ["med"]},
    )
    assert res.disposition == "rejected"
    assert any("recurrence" in e for e in (res.errors or []))


def test_keep_worthiness_recurrence_bool_rejected(tmp_queue_env):
    """NEGATIVE-BOOL-AS-INT: recurrence=True (bool is int subclass) → rejected.

    bool subclasses int, so a naive isinstance(True, (int,)) check would pass
    silently and inflate the T4 DemandLedger recurrence counts. An int-typed
    keep-worthiness field must reject bool.
    """
    res = deposit(
        {
            "page_type": "concept",
            "title": "W4",
            "body": "Some claim.",
            "recurrence": True,  # wrong: bool must not satisfy the int field
        },
        {"canonical_name": "W4", "domains": ["med"]},
    )
    assert res.disposition == "rejected"
    assert any("recurrence" in e for e in (res.errors or []))
