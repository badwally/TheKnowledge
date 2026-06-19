"""Typed deposit tool + concurrent authorship (Phase-3 Task 8, decision 3/4).

Deposits enqueue durably BEFORE ack; authoring is not serialized on a global
lock (two deposits overlap); a synthesis deposit cites only its declared sources.
"""

from __future__ import annotations

import threading
import time

import pytest

from gateway import paths
from gateway.ops.deposit import deposit
from gateway.intent_queue import IntentQueue


@pytest.fixture
def tmp_queue_env(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    (tmp_path / ".knowledge").mkdir(parents=True, exist_ok=True)
    return tmp_path


def test_deposit_enqueues_durably_before_ack(tmp_queue_env):
    res = deposit(
        {"page_type": "entity", "title": "Ozempic",
         "body": "...claim [[sources/s1]]"},
        {"entity_kind": "drug", "canonical_name": "Ozempic", "domains": ["med"]},
    )
    assert res.disposition == "queued"
    assert res.intent_id
    assert res.retry_after
    # the intent file exists on disk (durable) at ack time
    assert IntentQueue().get_state(res.intent_id) == "submitted"


def test_deposit_rejects_unknown_page_type(tmp_queue_env):
    res = deposit({"page_type": "wormhole", "title": "X", "body": "y"}, {})
    assert res.disposition == "rejected"
    assert not res.success
    assert IntentQueue().get_state(res.intent_id) is None  # never enqueued


def test_deposit_rejects_missing_grounding_fields(tmp_queue_env):
    res = deposit({"page_type": "entity", "title": "", "body": ""}, {})
    assert res.disposition == "rejected"


def test_two_deposits_enqueue_concurrently_without_global_lock(tmp_queue_env):
    # Authoring/enqueue must not serialize on a global wiki-author lock — two
    # deposits for different domains overlap in time.
    spans = []

    def _dep(title, dom):
        t0 = time.perf_counter()
        deposit({"page_type": "entity", "title": title,
                 "body": f"claim [[sources/{title}]]"},
                {"entity_kind": "drug", "canonical_name": title, "domains": [dom]})
        spans.append((t0, time.perf_counter()))

    t1 = threading.Thread(target=_dep, args=("AlphaDrug", "med"))
    t2 = threading.Thread(target=_dep, args=("BetaCoin", "econ"))
    t1.start(); t2.start(); t1.join(); t2.join()
    # both durably enqueued, distinct intents
    subs = list((paths.intents_dir() / "submitted").glob("*.json"))
    assert len(subs) == 2, subs
    # overlapping spans → not serialized behind one lock
    (a0, a1), (b0, b1) = spans
    assert a0 < b1 and b0 < a1, spans


def test_synthesis_deposit_cites_only_declared_sources(tmp_queue_env):
    res = deposit(
        {"page_type": "synthesis", "title": "T", "synthesizes": ["s1", "s2"],
         "body": "... [[sources/s1]] ... [[sources/s2]]"},
        {"domains": ["med"]},
    )
    assert res.disposition == "queued"
    # The enqueued payload declares exactly the submitted sources — no fabricated
    # ones are introduced at deposit time (canonicalization, not re-synthesis).
    rec_path = paths.intents_dir() / "submitted" / f"{res.intent_id}.json"
    import json
    rec = json.loads(rec_path.read_text())
    assert set(rec["payload"]["synthesizes"]) == {"s1", "s2"}


def test_synthesis_requires_synthesizes_list(tmp_queue_env):
    res = deposit({"page_type": "synthesis", "title": "T", "body": "x"},
                  {"domains": ["med"]})
    assert res.disposition == "rejected"
