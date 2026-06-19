"""Gap-routing ladder: corpus-miss telemetry + A4 carry-forward suppression.

Tests that retrieve_op / answer_op log corpus_miss=1 on empty results and
corpus_miss=0 on hits. A4 suppression: when the SAME caller has an outstanding
deposit (submitted/claimed/authored) for a topic, a miss does NOT log
corpus_miss=1 — it logs corpus_miss=0 + suppressed_a4=1.

Negative controls are named:
- NEGATIVE-DIFF-CALLER: a different caller's outstanding deposit does NOT suppress.
- NEGATIVE-NO-DEPOSIT: no deposit in queue → genuine corpus_miss=1.
- NEGATIVE-HIT: a successful retrieve → corpus_miss=0, no suppressed_a4.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from gateway import paths, frontmatter as fm
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.ops.retrieve import retrieve_op


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _seed_wiki_page(kb_root: Path, slug: str, body_text: str) -> None:
    """Write a minimal wiki concept page so the FTS index can find it."""
    wiki_concepts = kb_root / "wiki" / "concepts"
    wiki_concepts.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    content = fm.serialize(front, f"# {front['title']}\n\n{body_text}\n")
    (wiki_concepts / f"{slug}.md").write_text(content)


def _enqueue_deposit(kb_root: Path, caller: str, title: str) -> str:
    """Submit a deposit intent by the given caller and return intent_id."""
    payload = {
        "page_type": "concept",
        "title": title,
        "body": f"Claim about {title}.",
    }
    identity = {"caller": caller, "canonical_name": title, "domains": ["med"]}
    iid = compute_intent_id(payload, identity, semantics="deposit")
    intent = Intent(intent_id=iid, payload=payload, identity=identity)
    q = IntentQueue()
    q.submit(intent)
    return iid


def _log_text(kb_root: Path) -> str:
    lp = paths.log_path()
    if not lp.exists():
        return ""
    return lp.read_text()


# ---------------------------------------------------------------------------
# Corpus-miss on empty results (Step 1 RED target)
# ---------------------------------------------------------------------------

def test_retrieve_miss_logs_corpus_miss(kb_root):
    """An empty retrieve result logs corpus_miss=1 in log.md."""
    res = retrieve_op("nothing matches this query xyzzy", domain="med", caller="agent-1")
    assert not res.success
    log_text = _log_text(kb_root)
    assert "corpus_miss=1" in log_text


# ---------------------------------------------------------------------------
# No miss on a hit
# ---------------------------------------------------------------------------

def test_retrieve_hit_logs_no_miss(kb_root):
    """A retrieve that returns sections logs corpus_miss=0 in the last log entry."""
    # Seed a page that will match the query
    _seed_wiki_page(kb_root, "gastric-emptying", "Gastric emptying rate slows with GLP-1.")
    # Rebuild index so the new page is findable
    from gateway import search_index
    search_index.refresh(rebuild=True)

    res = retrieve_op("gastric emptying", domain="med", caller="agent-1")
    assert res.success
    # The LAST log entry should not contain corpus_miss=1
    log_text = _log_text(kb_root)
    last_line = log_text.splitlines()[-3] if log_text else ""  # header line of last entry
    # Any line in the last entry should have corpus_miss=0
    last_entry_lines = log_text.rsplit("##", 1)[-1] if "##" in log_text else ""
    assert "corpus_miss=1" not in last_entry_lines
    assert "corpus_miss=0" in log_text


# ---------------------------------------------------------------------------
# A4 suppression — SAME caller has outstanding deposit (Step 1 RED target)
# ---------------------------------------------------------------------------

def test_a4_requery_of_own_outstanding_deposit_logs_no_miss(kb_root):
    """Agent re-querying its own outstanding deposit topic logs no corpus_miss=1.

    A4 carry-forward suppression: if agent-1 has a submitted deposit whose
    topic overlaps the query, a miss must NOT produce corpus_miss=1.
    Instead it logs corpus_miss=0 + suppressed_a4=1.
    """
    # Enqueue a deposit by agent-1 for "pending topic"
    _enqueue_deposit(kb_root, "agent-1", "pending topic")

    res = retrieve_op("pending topic", domain="med", caller="agent-1")
    # The retrieve finds nothing (no wiki pages), but should NOT log corpus_miss=1
    assert not res.success
    log_text = _log_text(kb_root)
    assert "corpus_miss=1" not in log_text
    assert "suppressed_a4=1" in log_text


# ---------------------------------------------------------------------------
# NEGATIVE-DIFF-CALLER: different caller's outstanding deposit does NOT suppress
# ---------------------------------------------------------------------------

def test_a4_different_caller_deposit_does_not_suppress(kb_root):
    """NEGATIVE-DIFF-CALLER: agent-2's outstanding deposit does not suppress agent-1's miss."""
    # agent-2 has a deposit, but agent-1 is querying
    _enqueue_deposit(kb_root, "agent-2", "pending topic")

    res = retrieve_op("pending topic", domain="med", caller="agent-1")
    assert not res.success
    log_text = _log_text(kb_root)
    # A different caller's deposit does NOT trigger suppression → must log corpus_miss=1
    assert "corpus_miss=1" in log_text
    assert "suppressed_a4=1" not in log_text


# ---------------------------------------------------------------------------
# NEGATIVE-NO-DEPOSIT: no deposit in queue → genuine corpus_miss=1
# ---------------------------------------------------------------------------

def test_retrieve_miss_no_deposit_logs_corpus_miss(kb_root):
    """NEGATIVE-NO-DEPOSIT: no outstanding deposit → genuine corpus_miss=1."""
    res = retrieve_op("completely unknown topic xyzzy", domain="med", caller="agent-1")
    assert not res.success
    log_text = _log_text(kb_root)
    assert "corpus_miss=1" in log_text
    assert "suppressed_a4=1" not in log_text
