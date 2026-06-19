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
from dataclasses import dataclass
from pathlib import Path

import pytest

from gateway import paths, frontmatter as fm, search_index
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.ops.answer import answer_op
from gateway.ops.retrieve import retrieve_op


# ---------------------------------------------------------------------------
# Stub LLM client for answer_op (mirrors test_ws6_answer.py)
# ---------------------------------------------------------------------------

@dataclass
class _StubResult:
    text: str
    output_tokens: int = 42
    input_tokens: int = 100
    cache_read_tokens: int = 0


class _StubClient:
    """Records the prompt and returns a canned grounded answer."""

    def __init__(self, reply: str):
        self.reply = reply
        self.calls: list[dict] = []

    def call_with_usage(self, **kwargs):
        self.calls.append(kwargs)
        return _StubResult(text=self.reply)


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


# ---------------------------------------------------------------------------
# answer_op telemetry (SPEC GAP 2) — shares _a4_suppressed with retrieve_op
# ---------------------------------------------------------------------------

def _last_answer_entry(log_text: str) -> str:
    """Return the text of the last `answer` log entry."""
    # Entries start with "## ["; the last answer entry is the final one mentioning op=answer.
    entries = ["##" + e for e in log_text.split("##") if e.strip()]
    answer_entries = [e for e in entries if "] answer " in e or "] answer\n" in e]
    return answer_entries[-1] if answer_entries else ""


def test_answer_miss_logs_corpus_miss(kb_root):
    """answer_op with no wiki context logs corpus_miss=1 (no LLM call needed)."""
    client = _StubClient("unused")
    res = answer_op("nothing matches xyzzy", domain="med", caller="agent-1", client=client)
    assert not res.success
    # No grounding context → the stub client is never called.
    assert client.calls == []
    log_text = _log_text(kb_root)
    assert "corpus_miss=1" in log_text


def test_answer_hit_logs_no_miss(kb_root):
    """answer_op with grounding context logs corpus_miss=0 on its success entry."""
    _seed_wiki_page(kb_root, "gastric-emptying", "Gastric emptying slows with GLP-1 [[sources/pubmed-1]].")
    search_index.refresh(rebuild=True)

    client = _StubClient("Gastric emptying slows [[sources/pubmed-1]].")
    res = answer_op("gastric emptying", domain="med", caller="agent-1", client=client)
    assert res.success
    log_text = _log_text(kb_root)
    last = _last_answer_entry(log_text)
    assert "corpus_miss=0" in last
    assert "corpus_miss=1" not in last


def test_answer_a4_suppression(kb_root):
    """NEGATIVE-A4: answer_op miss suppressed when the same caller has an outstanding deposit."""
    _enqueue_deposit(kb_root, "agent-1", "pending topic")
    client = _StubClient("unused")
    res = answer_op("pending topic", domain="med", caller="agent-1", client=client)
    assert not res.success
    assert client.calls == []
    log_text = _log_text(kb_root)
    assert "corpus_miss=1" not in log_text
    assert "suppressed_a4=1" in log_text


# ---------------------------------------------------------------------------
# DEMAND-LOOP WIRING — a genuine corpus miss feeds the DemandLedger
# ---------------------------------------------------------------------------

def _recorded_gaps(kb_root: Path) -> list[str]:
    """Read the raw gap texts recorded by the DemandLedger."""
    p = kb_root / ".knowledge" / "demand" / "gaps.jsonl"
    if not p.exists():
        return []
    out = []
    for line in p.read_text().splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line)["text"])
    return out


def test_retrieve_genuine_miss_records_demand_gap(kb_root):
    """A genuine retrieve miss (corpus_miss=1, not A4-suppressed) records a gap
    in the DemandLedger — wiring the demand loop's producer."""
    retrieve_op("totally novel uncovered topic alpha", domain="med", caller="agent-1")
    gaps = _recorded_gaps(kb_root)
    assert "totally novel uncovered topic alpha" in gaps


def test_retrieve_a4_suppressed_miss_records_no_demand_gap(kb_root):
    """NEGATIVE-A4: an A4-suppressed miss records NO demand gap (the agent already
    has work in flight; it is not an open demand signal)."""
    _enqueue_deposit(kb_root, "agent-1", "pending topic")
    retrieve_op("pending topic", domain="med", caller="agent-1")
    gaps = _recorded_gaps(kb_root)
    assert "pending topic" not in gaps


def test_retrieve_hit_records_no_demand_gap(kb_root):
    """NEGATIVE-HIT: a successful retrieve records NO demand gap."""
    _seed_wiki_page(kb_root, "gastric-emptying", "Gastric emptying rate slows with GLP-1.")
    search_index.refresh(rebuild=True)
    retrieve_op("gastric emptying", domain="med", caller="agent-1")
    gaps = _recorded_gaps(kb_root)
    assert "gastric emptying" not in gaps


def test_answer_genuine_miss_records_demand_gap(kb_root):
    """answer_op genuine miss also records a demand gap."""
    client = _StubClient("unused")
    answer_op("another uncovered novel topic beta", domain="med",
              caller="agent-1", client=client)
    gaps = _recorded_gaps(kb_root)
    assert "another uncovered novel topic beta" in gaps


def test_answer_a4_suppressed_miss_records_no_demand_gap(kb_root):
    """NEGATIVE-A4: answer_op A4-suppressed miss records NO demand gap."""
    _enqueue_deposit(kb_root, "agent-1", "pending topic")
    client = _StubClient("unused")
    answer_op("pending topic", domain="med", caller="agent-1", client=client)
    gaps = _recorded_gaps(kb_root)
    assert "pending topic" not in gaps
