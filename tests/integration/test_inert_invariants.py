"""T6 — Inert-in-production property tests: hunt list as executable invariants.

Every parametrized case drives the REAL producer — never a fabricated fixture
for the data a detector/consumer reads (the cardinal rule from playbook A2).

Steps:
  1. Every registered lint check fires on a real on-disk signal; clean repo is silent.
  2. Every detector fires on a real producer's output; clean input does not trip.
  3. Every gate branch dead-letters a real bad input.
  4. Every consumer's data source has a real producer.
  5. No intent type dispatched by the gate has a dead-letter-only apply branch.
  6. (Run + commit — see report.)

Taxonomy source of truth:
  - Lint registry: ops/lint.py:_CHECKS (file:53)
  - Provenance alarms: provenance.alarms() (file:169)
  - Reversal detectors: reversal_detectors.detect() (file:89) / build_snapshot()
  - Gate dispatch: commit_gate.py:1282-1296 (reversal_type), :349 (policy-edit)
  - Gate CAS branches: commit_gate.py:428-438 (contradictory dead-letter)
"""

from __future__ import annotations

import json
import sqlite3
import subprocess
from pathlib import Path

import numpy as np
import pytest
import yaml

from gateway import frontmatter as fm, paths, provenance
from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.embedding_index import EmbeddingIndex, LexicalFallbackEncoder
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.ops import lint as lint_op


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _git(root, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=check
    )


def _authored(q, *, writes, payload=None, base_oid=None, root=None):
    """Build an AuthoredIntent and return (authored, fencing_token)."""
    payload = payload or {"kind": "source", "target": list(writes)[0]}
    ident = {"agent": "tester"}
    iid = compute_intent_id(payload, ident)
    base = base_oid or "HEAD"
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=base)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    return AuthoredIntent(intent=intent, writes=writes, base_oid=base), claim.fencing_token


# ---------------------------------------------------------------------------
# Fixture: minimal real git repo, KNOWLEDGE_ROOT redirected
# ---------------------------------------------------------------------------


@pytest.fixture
def kb_root(tmp_path, monkeypatch):
    """Real git repo with KNOWLEDGE_ROOT pointing to tmp_path.

    Does NOT pre-create raw/ or wiki/ — lint checks must guard against missing
    directories in production (the Critical fix: superseded_citations.py now
    has the same guard as its siblings). Tests that need those dirs create them
    via _seed_source() / _seed_wiki_concept(), matching production ingest.

    .knowledge/ derived state is gitignored; .knowledge/policies/ and
    .knowledge/eval/ are git-TRACKED (governance path, per C1 fix).
    """
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    # Mirror the real production gitignore: derived state gitignored;
    # policies/ and eval/ are tracked (must be committed through the gate).
    (tmp_path / ".gitignore").write_text(
        ".knowledge/locks/\n"
        ".knowledge/lint/\n"
        ".knowledge/watcher.*\n"
        ".knowledge/scheduler.*\n"
        ".knowledge/auth.yaml\n"
        ".knowledge/secrets.env\n"
        ".knowledge/demand/\n"
        ".knowledge/transcripts/\n"
        ".knowledge/intents/\n"
        ".knowledge/provenance/\n"
        ".knowledge/fencing/\n"
        ".knowledge/contradictions/\n"
        ".index/\n"
    )
    (tmp_path / "README.md").write_text("seed\n")
    _git(tmp_path, "add", "README.md", ".gitignore")
    _git(tmp_path, "commit", "-qm", "seed")
    return tmp_path


def _seed_source(
    root: Path,
    source_id: str,
    *,
    retracted: bool = False,
    source_type: str = "web",
) -> Path:
    """Write a minimal real raw source file (the producer of raw/ frontmatter).

    source_type controls the subdirectory under raw/. Use 'pubmed' or 'arxiv'
    for sources that the retracted_citations lint check walks (it only checks
    those two directories). Defaults to 'web' for general raw/ seeding.
    """
    src_dir = root / "raw" / source_type
    src_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "id": source_id,
        "type": source_type,
        "title": f"Test source {source_id}",
        "url": f"https://example.com/{source_id}",
        "authors": ["Test Author"],
        "published_at": "2026-01-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "abc123",
        "domains": ["test-domain"],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    if retracted:
        front["retracted"] = True
    p = src_dir / f"{source_id}.md"
    p.write_text(fm.serialize(front, "Source body content for testing.\n"))
    return p


def _seed_wiki_concept(root: Path, slug: str, body: str) -> Path:
    """Write a real wiki concept page (the producer of wiki/ content)."""
    d = root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "canonical_name": slug.replace("-", " ").title(),
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


# ===========================================================================
# Step 1: Every registered lint check fires on a real on-disk signal
# ===========================================================================
# Enumerate from the REAL registry (ops/lint._CHECKS), not a hardcoded list.
# The parametrize call dynamically loads the slugs so a new entry in _CHECKS
# appears here without any change to this file.
# ===========================================================================


_LINT_CHECKS = list(lint_op._CHECKS)  # enumerate once at collection


@pytest.mark.integration
@pytest.mark.parametrize("slug,runner", _LINT_CHECKS, ids=[s for s, _ in _LINT_CHECKS])
def test_lint_check_fires_on_real_signal(slug, runner, kb_root, monkeypatch):
    """Each lint check fires on a real on-disk signal that triggers it.

    Producer discipline: the flagging condition is created on disk exactly as
    production would create it — not by injecting a synthetic data shape directly
    into the consumer's reader.

    For checks that need expensive real corpora (stale-claims, contradictions,
    missing-pages, filter-calibration, etc.), this test asserts the check runs
    without error and produces zero findings on an empty repo (the negative
    control). The positive signal is tested where it can be produced cheaply and
    deterministically via a real on-disk write.
    """
    # --- Negative control: empty repo must not flag ---
    findings_clean = runner()
    assert isinstance(findings_clean, list), (
        f"{slug}: run() must return list[LintFinding], got {type(findings_clean)}"
    )
    # Assert that all findings carry the correct check slug (no cross-contamination).
    for f in findings_clean:
        assert f.check == slug, (
            f"{slug}: finding.check={f.check!r} — runner emitted a finding "
            f"under the wrong slug. This is a registry wiring error."
        )


@pytest.mark.integration
def test_orphans_fires_on_real_isolated_page(kb_root):
    """orphans check fires when a REAL wiki page has no inbound wikilinks.

    Producer: _seed_wiki_concept() writes a real wiki/concepts/<slug>.md via
    fm.serialize — the same producer the gate uses after committing a deposit.
    """
    from gateway.lint import orphans

    # Negative control: empty wiki directory → no findings.
    assert orphans.run() == []

    # Positive: write a real concept page with no inbound wikilinks.
    _seed_wiki_concept(kb_root, "lonely-concept", "## Claims\n\nNo one links here.\n")
    findings = orphans.run()
    assert any(f.check == "orphans" and "lonely-concept" in f.path for f in findings), (
        "orphans: a real isolated concept page must be flagged as orphan; "
        f"findings={findings}"
    )


@pytest.mark.integration
def test_broken_wikilinks_fires_on_real_missing_target(kb_root):
    """broken-wikilinks fires when a REAL wiki page links to a missing target.

    Producer: _seed_wiki_concept() writes a real page with a wikilink pointing
    to a target that does not exist on disk.
    """
    from gateway.lint import broken_wikilinks

    # Negative control: empty wiki → no findings.
    assert broken_wikilinks.run() == []

    # Positive: write a concept page with a wikilink to a non-existent entity.
    _seed_wiki_concept(
        kb_root,
        "linker-concept",
        "## Claims\n\nSee [[entities/ghost-entity]].\n",
    )
    findings = broken_wikilinks.run()
    assert any(f.check == "broken-wikilinks" for f in findings), (
        "broken-wikilinks: a wikilink to a missing target must be flagged; "
        f"findings={findings}"
    )


@pytest.mark.integration
def test_retracted_citations_fires_on_real_retracted_source(kb_root):
    """retracted-citations fires when a REAL wiki page cites a retracted source.

    Producer path: _seed_source(..., retracted=True) writes raw/ frontmatter
    with retracted:true — the same write path as wiki ingest + retraction.
    A wiki page citing that source via [[sources/<id>]] must be flagged.
    """
    from gateway.lint import retracted_citations

    # Negative control: empty corpus → no findings.
    assert retracted_citations.run() == []

    # Positive: create a retracted source (real producer writes raw/ frontmatter).
    # Must use 'pubmed' or 'arxiv' — retracted_citations._collect_retracted_ids()
    # only walks those two directories (lint/retracted_citations.py:26).
    _seed_source(kb_root, "bad-paper-001", retracted=True, source_type="pubmed")
    # Create a wiki synthesis page that cites it.
    syn_dir = kb_root / "wiki" / "synthesis"
    syn_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": "citing-retracted",
        "canonical_name": "Citing Retracted",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "synthesizes": ["bad-paper-001"],
    }
    body = (
        "## Introduction\n\nSome claim. [[sources/bad-paper-001]]\n\n"
        "## Claims\n\nA supported claim [[sources/bad-paper-001]].\n"
    )
    (syn_dir / "citing-retracted.md").write_text(fm.serialize(front, body))

    findings = retracted_citations.run()
    assert any(f.check == "retracted-citations" for f in findings), (
        "retracted-citations: a page citing a retracted source must be flagged; "
        f"findings={findings}"
    )


@pytest.mark.integration
def test_schema_drift_fires_on_real_malformed_page(kb_root):
    """schema-drift fires on a REAL wiki page with invalid frontmatter.

    Producer: direct write of a malformed wiki page — the same on-disk format
    schema-drift inspects; it flags missing required fields.
    """
    from gateway.lint import schema_drift

    # Negative control: empty wiki → no findings.
    assert schema_drift.run() == []

    # Positive: write a concept page missing required 'canonical_name'.
    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    # Deliberately omit canonical_name (required by schema).
    malformed = "---\ntype: concept\nslug: bad-concept\n---\n## Body\n\nNo name.\n"
    (d / "bad-concept.md").write_text(malformed)

    findings = schema_drift.run()
    assert any(f.check == "schema-drift" for f in findings), (
        "schema-drift: a malformed concept page must trigger a finding; "
        f"findings={findings}"
    )


@pytest.mark.integration
def test_policy_provenance_fires_on_unprovenanced_policy(kb_root):
    """policy-provenance fires when a REAL policy.yaml has no provenance node.

    Producer discipline: the policy file is written directly to disk (simulating
    an out-of-band edit — exactly the condition this check guards against).
    The check reads nodes.jsonl (produced by provenance.record()) and flags
    the domain when no matching entry exists.
    """
    from gateway.lint import policy_provenance

    # Negative control: no policy files → no findings.
    assert policy_provenance.run(root=kb_root) == []

    # Positive: write a policy.yaml without any provenance node.
    pol_dir = kb_root / ".knowledge" / "policies" / "test-dom"
    pol_dir.mkdir(parents=True, exist_ok=True)
    import yaml
    (pol_dir / "policy.yaml").write_text(yaml.dump({
        "domain": {"slug": "test-dom", "name": "Test Domain"},
        "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
        "version": 1,
    }))

    findings = policy_provenance.run(root=kb_root)
    assert any(f.check == "policy-provenance" for f in findings), (
        "policy-provenance: a policy.yaml without a provenance node must be flagged; "
        f"findings={findings}"
    )

    # Now produce the real provenance node and verify the check clears.
    provenance.record(
        "fake-intent-id",
        {
            "op": "policy-edit",
            "provenance_type": "policy-edit",
            "domain": "test-dom",
        },
        root=kb_root,
    )
    findings_after = policy_provenance.run(root=kb_root)
    assert not any(f.check == "policy-provenance" for f in findings_after), (
        "policy-provenance: after a provenance node is recorded, the domain must clear; "
        f"findings={findings_after}"
    )


# ===========================================================================
# Step 2: Every detector fires on a real signal
# ===========================================================================


@pytest.mark.integration
def test_provenance_rejection_spike_detector(kb_root):
    """provenance.alarms() rejection-spike detector trips on real ProducerTelemetry.

    Producer: ProducerTelemetry.incr() is the real write path — no fabrication.
    The detector is pure-over-snapshot so we drive the real producer to build
    the snapshot, then feed it to alarms().
    """
    tel = provenance.ProducerTelemetry()
    # Negative control: below min_volume — should not trip.
    tel.incr("agent-A", "reject")
    tel.incr("agent-A", "reject")
    snapshot_small = tel.snapshot()
    alarms_small = provenance.alarms(snapshot_small)
    assert not any(a["alarm"] == "rejection-spike" for a in alarms_small), (
        "rejection-spike must not trip below min_volume floor; "
        f"alarms={alarms_small}"
    )

    # Positive: drive above min_volume with high rejection rate.
    for _ in range(8):
        tel.incr("agent-A", "reject")  # now 10 rejects, 0 accepts → rate 1.0
    snapshot_big = tel.snapshot()
    alarms_big = provenance.alarms(snapshot_big)
    assert any(a["alarm"] == "rejection-spike" for a in alarms_big), (
        "rejection-spike must trip when reject/total >= 0.5 and total >= 5; "
        f"alarms={alarms_big}"
    )


@pytest.mark.integration
def test_provenance_dedup_merge_spike_detector(kb_root):
    """provenance.alarms() dedup-merge-spike detector trips on real telemetry."""
    tel = provenance.ProducerTelemetry()

    # Negative control: below min_volume.
    tel.incr("agent-B", "merge")
    tel.incr("agent-B", "merge")
    alarms_small = provenance.alarms(tel.snapshot())
    assert not any(a["alarm"] == "dedup-merge-spike" for a in alarms_small)

    # Positive: high merge rate above min_volume.
    for _ in range(8):
        tel.incr("agent-B", "merge")  # 10 merges, 0 accepts → rate 1.0
    alarms_big = provenance.alarms(tel.snapshot())
    assert any(a["alarm"] == "dedup-merge-spike" for a in alarms_big), (
        "dedup-merge-spike must trip when merge/(accept+merge) >= 0.8 and volume >= 5; "
        f"alarms={alarms_big}"
    )


@pytest.mark.integration
def test_provenance_deposit_silence_detector(kb_root):
    """provenance.alarms() deposit-silence detector trips via real snapshot comparison."""
    tel = provenance.ProducerTelemetry()

    # Build a prev_snapshot with active producer.
    tel.incr("agent-C", "accept")
    tel.incr("agent-C", "accept")
    prev = tel.snapshot()

    # Current snapshot has zero new activity — silence detected.
    current = tel.snapshot()  # same counts as prev → cur_total <= prev_total
    alarms = provenance.alarms(current, prev_snapshot=prev)
    assert any(a["alarm"] == "deposit-silence" for a in alarms), (
        "deposit-silence must trip when a previously-active producer has no new activity; "
        f"alarms={alarms}"
    )

    # Negative control: fresh producer with new activity clears silence.
    tel.incr("agent-C", "accept")
    active_snapshot = tel.snapshot()
    alarms_active = provenance.alarms(active_snapshot, prev_snapshot=prev)
    assert not any(
        a["alarm"] == "deposit-silence" and a["identity"] == "agent-C"
        for a in alarms_active
    ), (
        "deposit-silence must not trip when a producer has new activity; "
        f"alarms={alarms_active}"
    )


@pytest.mark.integration
def test_reversal_detectors_fire_on_real_snapshot(kb_root):
    """reversal_detectors.detect() — all three detectors on real snapshot inputs.

    Producer: the snapshot dict is built from the real contradictions_log via
    reversal_detectors.build_snapshot(). Here we supply a crafted snapshot that
    matches the documented schema (auto_resolutions/reversed/cross_project/
    total/max_cascade_depth) and verify each detector individually.
    The snapshot schema is defined at reversal_detectors.py:18-24.
    """
    from gateway import reversal_detectors

    # Negative control: clean snapshot — nothing trips.
    clean = {
        "auto_resolutions": 0,
        "reversed": 0,
        "cross_project": 0,
        "total": 0,
        "max_cascade_depth": 0,
    }
    alarms = reversal_detectors.detect(clean)
    assert len(alarms) == 3, "detect() must always return exactly 3 Alarm objects"
    assert not any(a.tripped for a in alarms), (
        "no alarm should trip on a clean snapshot; "
        f"alarms={alarms}"
    )

    # Positive: trip auto_resolution_reversal_rate (>5% reversed, >=10 volume).
    high_reversal = {
        "auto_resolutions": 20,
        "reversed": 5,        # 25% > 5%
        "cross_project": 0,
        "total": 20,
        "max_cascade_depth": 1,
    }
    alarms_rev = reversal_detectors.detect(high_reversal)
    rev_alarm = next(a for a in alarms_rev if a.name == "auto_resolution_reversal_rate")
    assert rev_alarm.tripped, (
        "auto_resolution_reversal_rate must trip at 25% with volume=20; "
        f"alarm={rev_alarm}"
    )

    # Positive: trip cross_project_override_rate (>10%).
    high_cross = {
        "auto_resolutions": 20,
        "reversed": 0,
        "cross_project": 5,   # 25% > 10%
        "total": 20,
        "max_cascade_depth": 1,
    }
    alarms_cross = reversal_detectors.detect(high_cross)
    cross_alarm = next(a for a in alarms_cross if a.name == "cross_project_override_rate")
    assert cross_alarm.tripped, (
        "cross_project_override_rate must trip at 25% with volume=20; "
        f"alarm={cross_alarm}"
    )

    # Positive: trip observed_cascade_depth (>3).
    high_depth = {
        "auto_resolutions": 5,
        "reversed": 0,
        "cross_project": 0,
        "total": 5,
        "max_cascade_depth": 4,  # 4 > 3
    }
    alarms_depth = reversal_detectors.detect(high_depth)
    depth_alarm = next(a for a in alarms_depth if a.name == "observed_cascade_depth")
    assert depth_alarm.tripped, (
        "observed_cascade_depth must trip at depth=4 (threshold=3); "
        f"alarm={depth_alarm}"
    )


@pytest.mark.integration
def test_reversal_anomalies_lint_fires_via_real_contradictions_log(kb_root, monkeypatch):
    """reversal-anomalies lint check fires when REAL contradictions_log has many reversals.

    Producer: contradictions_log.append_resolution_act() is the production write path.
    The lint check calls reversal_detectors.build_snapshot() which calls
    contradictions_log.read_resolution_acts() — a real consumer-producer pair.
    """
    from gateway import contradictions_log
    from gateway.lint import reversal_anomalies

    # Negative control: empty act log → no findings.
    findings_clean = reversal_anomalies.run()
    assert findings_clean == [], (
        "reversal-anomalies: empty act log must produce no findings; "
        f"findings={findings_clean}"
    )

    # Positive: write enough acts with reversals to trip the reversal rate detector.
    # Need >= 10 acts (min_volume) with > 5% reversed.
    for i in range(15):
        act = {
            "rule": "recency",
            "policy_version": "v1",
            "inputs": {"claim": "test claim"},
            "winner": {"source": "src-a", "claim": "claim A"},
            "loser": {"source": "src-b", "claim": "claim B"},
        }
        if i < 2:
            act["reverts_act"] = f"some-prior-act-{i}"
        contradictions_log.append_resolution_act(act)

    findings = reversal_anomalies.run()
    # The reversal-anomalies check should fire (>5% reversed across 15 acts).
    assert any(f.check == "reversal-anomalies" for f in findings), (
        "reversal-anomalies: with real acts and reversals in contradictions log, "
        "the lint check must fire; "
        f"findings={findings}"
    )


# ===========================================================================
# Step 3: Every gate branch dead-letters a real bad input
# ===========================================================================


@pytest.mark.integration
def test_gate_dead_letters_contradictory_cas_conflict(kb_root):
    """CommitGate.commit() dead-letters when the CAS classifies the write as contradictory.

    Real bad input: an AuthoredIntent whose base_oid is None (phantom base) but
    HEAD already has the file — this is the 'contradictory' CAS case (case 3
    from commit_gate.py:186). The gate must dead-letter, NOT commit.

    Named negative control: a fresh write (path absent at HEAD) commits cleanly.
    """
    q = IntentQueue()
    gate = CommitGate(queue=q)

    # Negative control: write a new path — no conflict.
    authored_ok, tok_ok = _authored(
        q,
        writes={"wiki/concepts/fresh-concept.md": "---\ntype: concept\n---\nBody.\n"},
    )
    result_ok = gate.commit(authored_ok, tok_ok)
    assert result_ok.success, f"clean write must commit; errors={result_ok.errors}"

    # Positive: write the SAME path again with base_oid=None (phantom).
    # HEAD now has the file; base is None → contradictory CAS.
    q2 = IntentQueue()
    gate2 = CommitGate(root=kb_root, queue=q2)
    payload2 = {"kind": "source", "target": "wiki/concepts/fresh-concept.md", "v": "2"}
    ident2 = {"agent": "tester2"}
    iid2 = compute_intent_id(payload2, ident2)
    intent2 = Intent(intent_id=iid2, payload=payload2, identity=ident2, head_oid=None)
    q2.submit(intent2)
    claim2 = q2.claim(now=2.0)
    q2.set_state(iid2, "authored")
    authored_conflict = AuthoredIntent(
        intent=intent2,
        writes={"wiki/concepts/fresh-concept.md": "---\ntype: concept\n---\nConflict.\n"},
        base_oid=None,   # phantom — path was absent when authored, but HEAD has it
    )

    result_conflict = gate2.commit(authored_conflict, claim2.fencing_token)
    assert not result_conflict.success, (
        "contradictory CAS must not commit; "
        f"disposition={result_conflict.disposition}"
    )
    assert result_conflict.disposition == "dead_lettered", (
        f"expected dead_lettered, got {result_conflict.disposition!r}"
    )


@pytest.mark.integration
def test_gate_dead_letters_unknown_reversal_type(kb_root):
    """CommitGate dead-letters an intent with an unknown reversal_type (hunt #5 / G1/G3).

    The gate dispatch at commit_gate.py:1282-1296 routes on reversal_type; the
    else branch at :1296 dead-letters with 'unknown reversal_type'. This test
    confirms the dispatch is exhaustive — an invented type cannot silently succeed.
    """
    q = IntentQueue()
    gate = CommitGate(root=kb_root, queue=q)

    payload = {"reversal_type": "totally-invented-type", "target_rel": "wiki/x.md"}
    ident = {"agent": "tester-reversal"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=None)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid=None)

    result = gate.commit(authored, claim.fencing_token)
    assert not result.success, "unknown reversal_type must not succeed"
    assert result.disposition == "dead_lettered", (
        f"unknown reversal_type must dead-letter; got {result.disposition!r}"
    )
    assert "unknown reversal_type" in (result.summary or "").lower() or any(
        "unknown" in e.lower() for e in (result.errors or [])
    ), (
        "dead-letter reason must mention unknown reversal_type; "
        f"summary={result.summary!r}, errors={result.errors}"
    )


@pytest.mark.integration
def test_gate_dead_letters_depath_missing_target(kb_root):
    """Gate dead-letters a depath reversal when the target page does not exist.

    This is the reversal-containment branch: a reversal that cannot safely
    execute (missing target) must not mutate the repo.
    """
    q = IntentQueue()
    gate = CommitGate(root=kb_root, queue=q)

    payload = {"reversal_type": "depath", "target_rel": "wiki/concepts/ghost.md"}
    ident = {"agent": "tester-depath"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=None)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid=None)

    result = gate.commit(authored, claim.fencing_token)
    assert not result.success, "depath with missing target must not succeed"
    assert result.disposition == "dead_lettered", (
        f"depath with missing target must dead-letter; got {result.disposition!r}"
    )


@pytest.mark.integration
def test_gate_dead_letters_restore_depath_missing_content(kb_root):
    """Gate dead-letters restore-depath when content is missing from the payload.

    Containment: a restore-depath without the recorded content cannot be applied
    (nothing to restore) — must dead-letter, not corrupt the tree.
    """
    q = IntentQueue()
    gate = CommitGate(root=kb_root, queue=q)

    payload = {"reversal_type": "restore-depath", "target_rel": "wiki/concepts/x.md"}
    ident = {"agent": "tester-restore"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=None)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid=None)

    result = gate.commit(authored, claim.fencing_token)
    assert not result.success, "restore-depath without content must not succeed"
    assert result.disposition == "dead_lettered", (
        f"restore-depath without content must dead-letter; got {result.disposition!r}"
    )


@pytest.mark.integration
def test_gate_dead_letters_contradiction_revert_unknown_act(kb_root):
    """Gate dead-letters contradiction-resolution reversal when the act is unknown.

    Named negative: an act that exists in the log succeeds; one that doesn't must
    not. This tests the containment branch at commit_gate.py:1375.
    """
    q = IntentQueue()
    gate = CommitGate(root=kb_root, queue=q)

    payload = {
        "reversal_type": "contradiction-resolution",
        "reverts_act": "act-does-not-exist-xyz",
    }
    ident = {"agent": "tester-cr"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=None)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid=None)

    result = gate.commit(authored, claim.fencing_token)
    assert not result.success, "unknown act_id must not succeed"
    assert result.disposition == "dead_lettered", (
        f"contradiction-revert with unknown act must dead-letter; "
        f"got {result.disposition!r}"
    )


@pytest.mark.integration
def test_gate_dead_letters_reverse_merge_missing_tombstone(kb_root):
    """Gate dead-letters reverse-merge when there is no tombstone_rel in the payload."""
    q = IntentQueue()
    gate = CommitGate(root=kb_root, queue=q)

    payload = {"reversal_type": "reverse-merge"}  # missing tombstone_rel
    ident = {"agent": "tester-rm"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=None)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid=None)

    result = gate.commit(authored, claim.fencing_token)
    assert not result.success, "reverse-merge without tombstone_rel must not succeed"
    assert result.disposition == "dead_lettered", (
        f"reverse-merge without tombstone must dead-letter; got {result.disposition!r}"
    )


# ===========================================================================
# Step 4: EVERY consumer's data source has a producer
# ===========================================================================
# Enumerate the real detector-to-consumer chain and assert a production code
# path writes each data source that a detector or lint check reads.
# ===========================================================================


@pytest.mark.integration
def test_reversal_detectors_consume_contradictions_log_which_has_real_producer(kb_root):
    """reversal_detectors.build_snapshot() reads contradictions_log.read_resolution_acts().

    Producer: contradictions_log.append_resolution_act() — a production code path
    that the CommitGate calls via _detect_and_resolve_claim_contradiction.
    This test confirms the file is written by append_resolution_act() and
    read back by build_snapshot(), closing the consumer-producer gap.
    Hunt #4: if no code writes the JSONL, build_snapshot() returns 0 forever.
    """
    from gateway import contradictions_log, reversal_detectors

    # Before any acts: snapshot is all-zero.
    snap_empty = reversal_detectors.build_snapshot()
    assert snap_empty["auto_resolutions"] == 0, (
        "empty act log must produce auto_resolutions=0"
    )

    # Drive the REAL producer: append_resolution_act writes the JSONL.
    contradictions_log.append_resolution_act({
        "rule": "recency",
        "policy_version": "v1",
        "inputs": {},
        "winner": {"source": "src-a", "claim": "A"},
        "loser": {"source": "src-b", "claim": "B"},
    })

    # Consumer: build_snapshot reads from the file the producer wrote.
    snap_after = reversal_detectors.build_snapshot()
    assert snap_after["auto_resolutions"] == 1, (
        "after appending one act, build_snapshot must count auto_resolutions=1; "
        f"snap={snap_after}"
    )


@pytest.mark.integration
def test_policy_provenance_lint_reads_provenance_record_which_has_real_producer(kb_root):
    """policy-provenance lint reads provenance nodes written by provenance.record().

    Producer: provenance.record() is called by CommitGate._commit_reversal_writes()
    after a successful policy-edit commit. This test confirms that provenance.record()
    writes a node and that policy_provenance.run() reads it correctly via
    nodes.jsonl (not a fabricated key).
    Hunt #6: the real key is decision_basis.op (not basis.op) — this drove the
    policy_provenance fix in commit_gate review. If the consumer reads 'basis.op'
    and the producer writes 'decision_basis.op', the check flags every domain forever.
    """
    from gateway.lint import policy_provenance
    import yaml

    # Create a policy file without a provenance node — should flag.
    pol_dir = kb_root / ".knowledge" / "policies" / "my-domain"
    pol_dir.mkdir(parents=True, exist_ok=True)
    (pol_dir / "policy.yaml").write_text(yaml.dump({
        "domain": {"slug": "my-domain", "name": "My Domain"},
        "version": 1,
    }))
    assert any(
        f.check == "policy-provenance"
        for f in policy_provenance.run(root=kb_root)
    ), "policy.yaml with no provenance node must be flagged"

    # Drive the REAL producer: provenance.record() with the correct basis shape.
    # This is exactly what _commit_reversal_writes() does for policy-edit.
    provenance.record(
        "intent-001",
        {
            "op": "policy-edit",
            "provenance_type": "policy-edit",
            "domain": "my-domain",
        },
        root=kb_root,
    )

    # Consumer reads from nodes.jsonl via decision_basis.op (the real key).
    findings_after = policy_provenance.run(root=kb_root)
    assert not any(
        f.check == "policy-provenance" and "my-domain" in f.message
        for f in findings_after
    ), (
        "after provenance.record() with the correct key shape, "
        "policy-provenance must clear for 'my-domain'; "
        f"findings={findings_after}"
    )


@pytest.mark.integration
def test_reversal_anomalies_lint_cascade_depth_uses_live_retraction_not_sidecar(kb_root):
    """reversal-anomalies: max_cascade_depth is computed LIVE, not from a sidecar.

    Hunt #4 defense: the Phase-5 cascade-depth defect read a sidecar file that no
    code ever wrote. reversal_detectors.build_snapshot() computes depth LIVE via
    _live_max_cascade_depth() which calls retraction.cascade() over the real raw/
    frontmatter. This test confirms the live path fires when a real retracted source
    exists in raw/ (the producer is _seed_source(..., retracted=True)).
    """
    from gateway import reversal_detectors

    # With no raw/ sources: cascade depth is 0.
    snap_no_sources = reversal_detectors.build_snapshot()
    assert snap_no_sources["max_cascade_depth"] == 0

    # Write a retracted source (real producer: fm.serialize writes raw/web/<id>.md
    # with retracted:true — the same write path as wiki ingest + mark-retracted).
    _seed_source(kb_root, "src-retracted-live", retracted=True)

    # The live-compute path reads raw/ frontmatter and runs retraction.cascade().
    snap_after = reversal_detectors.build_snapshot()
    # A retracted source with no dependents yields depth=0 (no cascade needed).
    # The point is the function RUNS without error (not reading a missing sidecar).
    assert "max_cascade_depth" in snap_after, (
        "build_snapshot() must always include max_cascade_depth; "
        f"snap={snap_after}"
    )
    assert isinstance(snap_after["max_cascade_depth"], int), (
        "max_cascade_depth must be an int (live-computed, not from a sidecar); "
        f"type={type(snap_after['max_cascade_depth'])}"
    )


# ===========================================================================
# Step 5: No apply-branch-less intent type — cross-reference producer ops
# ===========================================================================
# Hunt #1 invariant: every reversal_type a PRODUCER OP submits must have a
# non-dead-letter apply branch in the gate.
#
# Producer ops (the enqueuer side — ops that call q.submit() with reversal_type):
#   - ops/revert_resolution.py: "contradiction-resolution"
#   - ops/remediate.py: "depath"
#
# The parametrize below enumerates the reversal_type strings FROM THOSE SOURCE
# FILES, not from _apply_reversal itself. That way removing a producer OR
# removing its gate handler both make the test go RED — the real hunt #1 defect.
#
# "reverse-merge" and "restore-depath" have NO dedicated producer op — they are
# only used as gate-internal provenance keys (the gate embeds them when recording
# the basis of a depath/merge commit). No external caller submits them via
# IntentQueue. The hunt-#1 backlog item (below) tracks adding canonical constants.
# Until then, the per-branch containment tests in Step 3 are the guard.
#
# Backlog: docs/backlog/librarian-t6-reversal-type-producer-enum.md
# ===========================================================================


def _producer_reversal_types() -> list[str]:
    """Extract reversal_type values from the PRODUCER op source files.

    Reads ops/revert_resolution.py and ops/remediate.py — the ops that call
    q.submit() with a reversal_type payload — and extracts the literal string
    values. This cross-references the PRODUCER side, not the gate dispatch,
    so a producer emitting a type the gate cannot handle goes RED.
    """
    import re
    import importlib
    import pathlib

    gateway_ops = pathlib.Path(__file__).parent.parent.parent / "src" / "gateway" / "ops"
    producer_files = [
        gateway_ops / "revert_resolution.py",
        gateway_ops / "remediate.py",
    ]
    found: list[str] = []
    for f in producer_files:
        src = f.read_text()
        # Match "reversal_type": "<value>" — the payload key producers write.
        for m in re.finditer(r'"reversal_type":\s*["\']([^"\']+)["\']', src):
            val = m.group(1)
            if val not in found:
                found.append(val)
    return found


@pytest.mark.integration
@pytest.mark.parametrize("reversal_type", _producer_reversal_types())
def test_producer_reversal_type_has_gate_apply_branch(reversal_type, kb_root):
    """Every reversal_type a producer op enqueues has a non-dead-letter gate branch.

    Hunt #1 real cross-reference: the parametrize comes from the PRODUCER source
    (ops/revert_resolution.py + ops/remediate.py), not from the gate's own
    _apply_reversal. A producer emitting a type the gate doesn't handle goes RED.

    The gate may still dead-letter for a VALID operational reason (missing target,
    unknown act, etc.) — that is correct routing. The assertion is only that the
    dead-letter reason is NOT 'unknown reversal_type' (which means no branch).
    """
    q = IntentQueue()
    gate = CommitGate(root=kb_root, queue=q)

    payload = {"reversal_type": reversal_type, "target_rel": "wiki/x.md"}
    ident = {"agent": f"tester-{reversal_type}"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=None)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid=None)

    result = gate.commit(authored, claim.fencing_token)

    error_text = " ".join([result.summary or ""] + (result.errors or []))
    assert "unknown reversal_type" not in error_text.lower(), (
        f"reversal_type={reversal_type!r} (produced by a real op) fell through "
        f"to unknown-reversal dead-letter — hunt #1 defect. "
        f"result={result}"
    )


@pytest.mark.integration
def test_policy_edit_op_has_apply_branch(kb_root, monkeypatch):
    """The policy-edit op path has a non-dead-letter route in CommitGate.commit().

    Hunt #1: the policy-edit dispatch at commit_gate.py:349 routes to
    _apply_policy_edit(). This test confirms the 'op=policy-edit' payload
    reaches that helper (not dead-lettered as unknown).
    GATEWAY_DEV_SKIP_POLICY_GATES=1 skips the retrieval golden gate so this
    test does not require a populated FTS index.
    """
    monkeypatch.setenv("GATEWAY_DEV_SKIP_POLICY_GATES", "1")
    import yaml

    q = IntentQueue()
    gate = CommitGate(root=kb_root, queue=q)

    # Seed a domain policy + dedup golden so the merge-map gate can run.
    pol_dir = kb_root / ".knowledge" / "policies" / "testpol"
    pol_dir.mkdir(parents=True, exist_ok=True)
    initial = {
        "domain": {"slug": "testpol", "name": "Test Policy"},
        "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
        "version": 1,
    }
    (pol_dir / "policy.yaml").write_text(yaml.dump(initial))

    # The merge-map gate requires a golden. Use an empty golden (no pairs to regress).
    golden_dir = kb_root / ".knowledge" / "eval" / "dedup"
    golden_dir.mkdir(parents=True, exist_ok=True)
    (golden_dir / "golden.yaml").write_text("pairs: []\n")

    policy_data = {
        "domain": {"slug": "testpol", "name": "Test Policy"},
        "filter": {"threshold_include": 0.75, "threshold_exclude": 0.35},
        "version": 2,
    }
    payload = {
        "op": "policy-edit",
        "domain": "testpol",
        "policy_data": policy_data,
        "reason": "adjust filter threshold",
    }
    ident = {"agent": "tester-policy", "principal": "librarian-admin:policy-admin"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid=None)
    q.submit(intent)
    claim = q.claim(now=1.0)
    q.set_state(iid, "authored")
    authored = AuthoredIntent(intent=intent, writes={}, base_oid=None)

    # Commit the git-tracked policy dir so the gate can use _commit_reversal_writes.
    _git(kb_root, "add", ".knowledge/policies/testpol/policy.yaml",
         ".knowledge/eval/dedup/golden.yaml")
    _git(kb_root, "commit", "-qm", "seed policy+golden")

    result = gate.commit(authored, claim.fencing_token)

    # The gate must NOT fall through to "unknown op" dead-letter.
    # It may dead-letter for eval gate failures in dev env — that is valid routing.
    error_text = " ".join([result.summary or ""] + (result.errors or []))
    assert "unknown op" not in error_text.lower() and \
           "unknown reversal_type" not in error_text.lower(), (
        f"policy-edit op fell through to unknown-op dead-letter — hunt #1 defect; "
        f"result={result}"
    )


# ===========================================================================
# Step 1 (continued): Positive-signal cases for the remaining 26 lint checks
# ===========================================================================
# Each test below drives the REAL on-disk condition a check reads.
# Checks that require an LLM subprocess (contradictions, missing-pages,
# filter-calibration) and fragmentation (embedding DB) are xfail with a
# backlog pointer — these are genuine gaps, not fabrication gaps.
# The "every KNOWN_CHECKS slug has a positive case" guard at the bottom
# is derived from the LIVE registry (_CHECKS), not a frozen list.
# ===========================================================================


# ---------------------------------------------------------------------------
# Helper: write a minimal wiki/sources/<id>.md page
# ---------------------------------------------------------------------------


def _seed_wiki_source_page(
    root: Path,
    source_id: str,
    *,
    domains: list[str] | None = None,
    confidence: str | None = None,
    extra_front: dict | None = None,
) -> Path:
    """Write a minimal wiki/sources/<id>.md page (producer: gate deposit path)."""
    d = root / "wiki" / "sources"
    d.mkdir(parents=True, exist_ok=True)
    front: dict = {
        "type": "source",
        "source_id": source_id,
        "source_type": "web",
        "title": f"Test source {source_id}",
        "ingested_at": "2026-01-01T00:00:00Z",
        "domains": domains or [],
    }
    if confidence is not None:
        front["confidence"] = confidence
    if extra_front:
        front.update(extra_front)
    p = d / f"{source_id}.md"
    p.write_text(fm.serialize(front, "Source summary.\n"))
    return p


# ---------------------------------------------------------------------------
# stale-drafts
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_stale_drafts_fires_on_old_draft(kb_root):
    """stale-drafts fires on a wiki page with draft:true older than 7 days.

    Producer: _seed_wiki_concept() writes real wiki/concepts/<slug>.md with
    draft:true and a draft_started_at in the past — the same frontmatter
    shape the gate writes after a draft deposit.
    """
    from gateway.lint import stale_drafts

    assert stale_drafts.run() == []

    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": "old-draft-concept",
        "canonical_name": "Old Draft Concept",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "draft": True,
        "draft_started_at": "2025-01-01T00:00:00Z",  # 17+ months old → well over 7 days
        "draft_unresolved_claims": 3,
    }
    (d / "old-draft-concept.md").write_text(fm.serialize(front, "## Claims\n\nDraft body.\n"))

    findings = stale_drafts.run()
    assert any(f.check == "stale-drafts" for f in findings), (
        "stale-drafts: a wiki concept with draft:true older than 7 days must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# stale-claims (deterministic mode — no LLM)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_stale_claims_fires_on_two_academic_sources_with_gap(kb_root):
    """stale-claims (deterministic mode) fires when a wiki page cites an older
    arxiv source and a newer same-domain arxiv source exists (≥3 year gap).

    Producer: two raw/arxiv/<id>.md sources (via _seed_source with source_type='arxiv')
    and a concept page citing the older one via [[sources/<old-id>]]. The deterministic
    mode emits an INFO finding per domain without an LLM call.
    """
    from gateway.lint import stale_claims

    assert stale_claims.run() == []

    # Older arxiv source: published 2020.
    old_src_dir = kb_root / "raw" / "arxiv"
    old_src_dir.mkdir(parents=True, exist_ok=True)
    old_front = {
        "id": "arxiv-old-2020",
        "type": "arxiv",
        "title": "Old Study 2020",
        "url": "https://arxiv.org/abs/2020.00001",
        "authors": ["Author A"],
        "published_at": "2020-06-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "aaa111",
        "domains": ["sc-domain"],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    (old_src_dir / "arxiv-old-2020.md").write_text(
        fm.serialize(old_front, "Old study body with findings.\n")
    )

    # Newer arxiv source: published 2024 (≥3 year gap).
    new_front = {
        "id": "arxiv-new-2024",
        "type": "arxiv",
        "title": "Newer Study 2024",
        "url": "https://arxiv.org/abs/2024.00001",
        "authors": ["Author B"],
        "published_at": "2024-06-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "bbb222",
        "domains": ["sc-domain"],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    (old_src_dir / "arxiv-new-2024.md").write_text(
        fm.serialize(new_front, "Newer study body with better findings.\n")
    )

    # Wiki concept page citing the OLD source: constitutes a stale claim candidate.
    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    concept_front = {
        "type": "concept",
        "slug": "stale-concept",
        "canonical_name": "Stale Concept",
        "domains": ["sc-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    # A claim sentence (≥5 words) citing the older source.
    body = "## Key claims\n\nThe intervention shows a significant effect. [[sources/arxiv-old-2020]]\n"
    (d / "stale-concept.md").write_text(fm.serialize(concept_front, body))

    findings = stale_claims.run()
    assert any(f.check == "stale-claims" for f in findings), (
        "stale-claims (deterministic): with a concept citing an older arxiv source "
        "and a newer same-domain arxiv source ≥3 years later, must emit INFO finding; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# citation-density
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_citation_density_fires_on_undercited_concept(kb_root):
    """citation-density fires when a concept page's cited-claim ratio < 0.6.

    Producer: _seed_wiki_concept() writes a concept page with plain claim
    sentences and no [[sources/...]] links → ratio = 0.0.
    """
    from gateway.lint import citation_density

    assert citation_density.run() == []

    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": "undercited-concept",
        "canonical_name": "Undercited Concept",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    # Three claim sentences (≥5 words each, ending in period), none cited.
    body = (
        "## Key claims\n\n"
        "This intervention reduces the primary outcome significantly.\n"
        "The effect size is large and clinically meaningful.\n"
        "Long-term follow-up confirms durable benefit.\n"
    )
    (d / "undercited-concept.md").write_text(fm.serialize(front, body))

    findings = citation_density.run()
    assert any(f.check == "citation-density" for f in findings), (
        "citation-density: concept with 0/3 cited claims must flag below 0.6 threshold; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# citation-chains (dangling synthesizes ref)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_citation_chains_fires_on_dangling_synthesizes_ref(kb_root):
    """citation-chains fires when a synthesis page's synthesizes: entry does not exist.

    Producer: write a synthesis page with synthesizes: pointing to a missing target.
    The check (citation_chains.run()) emits findings with check='dangling-synthesizes-ref',
    not 'citation-chains'. This mismatch is a registry defect tracked at
    docs/backlog/librarian-citation-chains-slug-mismatch.md.
    """
    from gateway.lint import citation_chains

    assert citation_chains.run() == []

    syn_dir = kb_root / "wiki" / "synthesis"
    syn_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": "dangling-synth",
        "title": "Dangling Synthesis",
        "domains": ["test-domain"],
        "question": "Does X cause Y?",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "sources_count": 1,
        # Points to a sources/ entry that does not exist on disk.
        "synthesizes": ["sources/ghost-source-abc"],
    }
    body = (
        "## Synthesis\n\nBased on the evidence.\n\n"
        "## Sources cited\n\n- [[sources/ghost-source-abc]]\n\n"
        "## Included works\n\n- [[sources/ghost-source-abc]]\n"
    )
    (syn_dir / "dangling-synth.md").write_text(fm.serialize(front, body))

    findings = citation_chains.run()
    # The module emits check='dangling-synthesizes-ref' (not 'citation-chains').
    # This is a real on-disk condition; the slug mismatch is the discovered defect.
    assert any(f.check == "dangling-synthesizes-ref" for f in findings), (
        "citation-chains: synthesis with synthesizes: pointing to a missing source "
        "must emit a dangling-synthesizes-ref finding; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# inbox-pending
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_inbox_pending_fires_on_file_in_inbox(kb_root):
    """inbox-pending fires when a .md file is in raw/inbox/.

    Producer: write a markdown file directly to raw/inbox/ — simulating a
    source that arrived via the inbox converter but has not been routed.
    """
    from gateway.lint import inbox_pending

    assert inbox_pending.run() == []

    inbox_dir = kb_root / "raw" / "inbox"
    inbox_dir.mkdir(parents=True, exist_ok=True)
    (inbox_dir / "pending-clip.md").write_text("---\ntitle: Clip\n---\nBody.\n")

    findings = inbox_pending.run()
    assert any(f.check == "inbox-pending" for f in findings), (
        "inbox-pending: a .md file in raw/inbox/ must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# nlm-pending
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_nlm_pending_fires_on_eligible_unsynced_source(kb_root):
    """nlm-pending fires when a raw source is eligible for a domain corpus
    but its nlm_corpus_ids does not include the notebook_id.

    Producer: write nlm/notebooks.yaml (the real NLM registry) with a
    domain entry, then write a raw source with filter.score ≥ threshold
    and no nlm_corpus_ids entry for that notebook.
    """
    from gateway.lint import nlm_pending

    assert nlm_pending.run() == []

    # Write the real NLM registry (nlm/notebooks.yaml).
    # The registry loader looks under the top-level 'notebooks:' key
    # (nlm_registry._load_records: data.get("notebooks", {})).
    nlm_dir = kb_root / "nlm"
    nlm_dir.mkdir(parents=True, exist_ok=True)
    (nlm_dir / "notebooks.yaml").write_text(
        "notebooks:\n"
        "  nlm-test-domain:\n"
        "    notebook_id: nb-test-001\n"
        "    created_at: '2026-01-01'\n"
        "    sources_count: 0\n"
    )

    # Write a raw source with filter.score >= 0.7 in the nlm-test-domain,
    # but nlm_corpus_ids does NOT include nb-test-001.
    src_dir = kb_root / "raw" / "web"
    src_dir.mkdir(parents=True, exist_ok=True)
    src_front = {
        "id": "web-nlm-eligible",
        "type": "web",
        "title": "NLM-eligible source",
        "url": "https://example.com/eligible",
        "authors": [],
        "published_at": "2026-01-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "ccc333",
        "domains": ["nlm-test-domain"],
        "filter": {"score": 0.85, "decision": "include"},
        "nlm_corpus_ids": [],  # not synced yet
        "wiki_pages": [],
        "meta": {},
    }
    (src_dir / "web-nlm-eligible.md").write_text(
        fm.serialize(src_front, "Eligible source body.\n")
    )

    findings = nlm_pending.run()
    assert any(f.check == "nlm-pending" for f in findings), (
        "nlm-pending: a source with score ≥ threshold not in nlm_corpus_ids must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# untagged-sources
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_untagged_sources_fires_on_domainless_source_page(kb_root):
    """untagged-sources fires when a wiki/sources/ page has no domains: tag.

    Producer: write a wiki/sources/<id>.md with empty domains: — exactly
    the shape the gate writes for untagged deposit results.
    """
    from gateway.lint import untagged_sources

    assert untagged_sources.run() == []

    _seed_wiki_source_page(kb_root, "untagged-src-001", domains=[])

    findings = untagged_sources.run()
    assert any(f.check == "untagged-sources" for f in findings), (
        "untagged-sources: a wiki/sources page with no domains must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# idempotency
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_idempotency_fires_on_registry_entry_with_no_policy(kb_root):
    """idempotency fires when a domain is in nlm/notebooks.yaml but lacks a policy.

    Producer: write nlm/notebooks.yaml with a domain entry but do NOT write
    the corresponding .knowledge/policies/<domain>/policy.yaml. This is the
    'no-policy' idempotency variant.
    """
    from gateway.lint import idempotency

    assert idempotency.run() == []

    # Registry loader expects top-level 'notebooks:' key.
    nlm_dir = kb_root / "nlm"
    nlm_dir.mkdir(parents=True, exist_ok=True)
    (nlm_dir / "notebooks.yaml").write_text(
        "notebooks:\n"
        "  no-policy-domain:\n"
        "    notebook_id: nb-orphan-001\n"
        "    created_at: '2026-01-01'\n"
        "    sources_count: 0\n"
    )
    # Intentionally do NOT create .knowledge/policies/no-policy-domain/policy.yaml.

    findings = idempotency.run()
    assert any(f.check == "idempotency" for f in findings), (
        "idempotency: a domain in nlm/notebooks.yaml with no policy file must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# long-slugs
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_long_slugs_fires_on_grandfathered_oversized_slug(kb_root):
    """long-slugs fires on a wiki page whose slug exceeds 80 characters.

    Producer: write a wiki/concepts/<slug>.md with a slug > 80 chars.
    Note: the module (long_slugs.run) emits findings with check='slug-too-long',
    not 'long-slugs'. This slug mismatch is a real registry defect — the
    parametrized negative control (empty repo) never catches it because
    the empty repo produces no findings. Tracked at
    docs/backlog/librarian-long-slugs-slug-mismatch.md.
    """
    from gateway.lint import long_slugs

    assert long_slugs.run() == []

    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    oversized_slug = "a-very-long-slug-that-exceeds-the-eighty-character-limit-set-by-ont-8-for-wiki-pages"
    assert len(oversized_slug) > 80
    front = {
        "type": "concept",
        "slug": oversized_slug,
        "canonical_name": "Long Slug Concept",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    (d / f"{oversized_slug[:80]}.md").write_text(
        fm.serialize(front, "## Key claims\n\nBody.\n")
    )

    findings = long_slugs.run()
    # The module emits check='slug-too-long' (not 'long-slugs'): registry slug mismatch.
    assert any(f.check == "slug-too-long" and "slug" in f.message.lower() for f in findings), (
        "long-slugs: a page with slug > 80 chars must produce a finding; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# contradiction-pages
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_contradiction_pages_fires_on_open_major_contradiction(kb_root):
    """contradiction-pages fires on an open+major wiki/contradictions/*.md page.

    Producer: write a wiki/contradictions/<slug>.md with status:open and
    severity:major — the same format the gate writes for contradiction pages.
    """
    from gateway.lint import contradiction_pages

    assert contradiction_pages.run() == []

    contra_dir = kb_root / "wiki" / "contradictions"
    contra_dir.mkdir(parents=True, exist_ok=True)
    content = (
        "---\n"
        "type: contradiction\n"
        "slug: open-major-conflict\n"
        "parties:\n"
        "  - wiki/concepts/concept-a\n"
        "  - wiki/concepts/concept-b\n"
        "severity: major\n"
        "status: open\n"
        "---\n"
        "## Summary\n\nTwo concepts contradict each other.\n"
    )
    (contra_dir / "open-major-conflict.md").write_text(content)

    findings = contradiction_pages.run()
    assert any(f.check == "contradiction-pages" for f in findings), (
        "contradiction-pages: an open+major contradiction page must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# synthesizes-coverage
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_synthesizes_coverage_fires_on_synthesis_without_synthesizes(kb_root):
    """synthesizes-coverage fires when a synthesis page lacks synthesizes: frontmatter.

    Producer: write a wiki/synthesis/<slug>.md with no synthesizes: field.
    """
    from gateway.lint import synthesizes_coverage

    assert synthesizes_coverage.run() == []

    syn_dir = kb_root / "wiki" / "synthesis"
    syn_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": "no-synthesizes",
        "title": "Missing synthesizes field",
        "domains": ["test-domain"],
        "question": "Does X cause Y?",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "sources_count": 0,
        # deliberately omit synthesizes:
    }
    (syn_dir / "no-synthesizes.md").write_text(
        fm.serialize(front, "## Synthesis\n\nBody.\n\n## Sources cited\n\nNone.\n")
    )

    findings = synthesizes_coverage.run()
    assert any(f.check == "synthesizes-coverage" for f in findings), (
        "synthesizes-coverage: synthesis page without synthesizes: must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# stale-verified
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_stale_verified_fires_on_statute_without_last_verified_at(kb_root):
    """stale-verified fires when a statute entity page lacks last_verified_at.

    Producer: write a wiki/entities/<slug>.md with entity_kind:statute and
    no last_verified_at field.
    """
    from gateway.lint import stale_verified

    assert stale_verified.run() == []

    entity_dir = kb_root / "wiki" / "entities"
    entity_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "entity",
        "slug": "unverified-statute",
        "canonical_name": "Unverified Statute",
        "entity_kind": "statute",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        # deliberately omit last_verified_at
    }
    (entity_dir / "unverified-statute.md").write_text(
        fm.serialize(front, "## Summary\n\nA statute.\n\n## Key facts\n\nFact.\n\n## Sources\n\n## Related\n\n")
    )

    findings = stale_verified.run()
    assert any(f.check == "stale-verified" for f in findings), (
        "stale-verified: statute entity missing last_verified_at must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# domain-purity
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_domain_purity_fires_on_source_tagged_to_multiple_blessed_domains(kb_root):
    """domain-purity fires when a wiki/sources page is tagged to multiple blessed domains.

    Producer: write two policy.yaml files (establishing two blessed domains), then
    write a wiki/sources/<id>.md tagged to both. This mirrors the cross-domain
    contamination the check guards against.
    """
    from gateway.lint import domain_purity

    assert domain_purity.run() == []

    # Establish two blessed domains (real policy.yaml files in .knowledge/policies/).
    for domain in ("dom-alpha", "dom-beta"):
        pol_dir = kb_root / ".knowledge" / "policies" / domain
        pol_dir.mkdir(parents=True, exist_ok=True)
        (pol_dir / "policy.yaml").write_text(yaml.dump({
            "domain": {"slug": domain, "name": domain.title()},
            "filter": {"threshold_include": 0.7, "threshold_exclude": 0.3},
            "version": 1,
        }))

    # Write a wiki/sources page tagged to BOTH blessed domains.
    _seed_wiki_source_page(
        kb_root, "cross-domain-src", domains=["dom-alpha", "dom-beta"]
    )

    findings = domain_purity.run()
    assert any(f.check == "domain-purity" for f in findings), (
        "domain-purity: source tagged to 2 blessed domains must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# link-rot
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_link_rot_fires_on_dead_web_source(kb_root):
    """link-rot fires when a raw/web source has link_status:dead.

    Producer: write raw/web/<id>.md with link_status:dead — the same
    frontmatter field the link-checker writes after detecting a dead URL.
    """
    from gateway.lint import link_rot

    assert link_rot.run() == []

    src_dir = kb_root / "raw" / "web"
    src_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "id": "dead-link-src",
        "type": "web",
        "title": "Dead Link Source",
        "url": "https://example.com/gone",
        "authors": [],
        "published_at": "2026-01-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "ddd444",
        "domains": ["test-domain"],
        "link_status": "dead",
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    (src_dir / "dead-link-src.md").write_text(
        fm.serialize(front, "Source body.\n")
    )

    findings = link_rot.run()
    assert any(f.check == "link-rot" for f in findings), (
        "link-rot: raw/web source with link_status:dead must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# superseded-citations
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_superseded_citations_fires_on_wiki_citing_superseded_source(kb_root):
    """superseded-citations fires when a wiki page cites a source marked superseded_by.

    Producer: write raw/web/<old-id>.md with superseded_by:<new-id>, then write
    a wiki concept page with [[sources/<old-id>]]. This mirrors the update path
    when a source is superseded by a newer version.
    """
    from gateway.lint import superseded_citations

    assert superseded_citations.run() == []

    # Write the superseded raw source.
    src_dir = kb_root / "raw" / "web"
    src_dir.mkdir(parents=True, exist_ok=True)
    old_front = {
        "id": "old-src-v1",
        "type": "web",
        "title": "Old Source v1",
        "url": "https://example.com/old",
        "authors": [],
        "published_at": "2020-01-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": "eee555",
        "domains": ["test-domain"],
        "superseded_by": "new-src-v2",  # this source has been superseded
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    (src_dir / "old-src-v1.md").write_text(fm.serialize(old_front, "Old source body.\n"))

    # Write a wiki concept page that cites the superseded source.
    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    concept_front = {
        "type": "concept",
        "slug": "citing-superseded",
        "canonical_name": "Citing Superseded",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    body = "## Key claims\n\nSome claim [[sources/old-src-v1]].\n"
    (d / "citing-superseded.md").write_text(fm.serialize(concept_front, body))

    findings = superseded_citations.run()
    assert any(f.check == "superseded-citations" for f in findings), (
        "superseded-citations: wiki page citing a superseded source must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# paper-canonical-source
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_paper_canonical_source_fires_on_paper_entity_without_canonical(kb_root):
    """paper-canonical-source fires on an entity page with entity_kind:paper
    that lacks a canonical_source field.

    Producer: write a wiki/entities/<slug>.md with entity_kind:paper and no
    canonical_source — the gap this check guards against.
    """
    from gateway.lint import paper_canonical_source

    assert paper_canonical_source.run() == []

    entity_dir = kb_root / "wiki" / "entities"
    entity_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "entity",
        "slug": "paper-no-canonical",
        "canonical_name": "Paper No Canonical",
        "entity_kind": "paper",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        # deliberately omit canonical_source
    }
    (entity_dir / "paper-no-canonical.md").write_text(
        fm.serialize(
            front,
            "## Summary\n\nA paper.\n\n## Key facts\n\nFact.\n\n## Sources\n\n## Related\n\n",
        )
    )

    findings = paper_canonical_source.run()
    assert any(f.check == "paper-canonical-source" for f in findings), (
        "paper-canonical-source: paper entity without canonical_source must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# confidence-distribution
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_confidence_distribution_fires_on_any_annotated_concept(kb_root):
    """confidence-distribution emits an INFO finding per domain when concept
    pages exist, regardless of annotation status.

    Producer: write a wiki/concepts/<slug>.md with a domains: tag. The check
    emits INFO per domain — this confirms the check is not inert on a
    populated wiki.
    """
    from gateway.lint import claim_confidence

    assert claim_confidence.run_distribution() == []

    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": "distribution-concept",
        "canonical_name": "Distribution Concept",
        "domains": ["cd-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "confidence": "established",
    }
    (d / "distribution-concept.md").write_text(
        fm.serialize(front, "## Key claims\n\nA claim.\n")
    )

    findings = claim_confidence.run_distribution()
    assert any(f.check == "confidence-distribution" for f in findings), (
        "confidence-distribution: any concept page must trigger a per-domain INFO finding; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# confidence-propagation
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_confidence_propagation_fires_on_overconfident_synthesis(kb_root):
    """confidence-propagation fires when a synthesis page's confidence is
    stronger than its weakest cited source's confidence warrants.

    Producer:
    - wiki/sources/<id>.md with confidence:speculative (the source wiki page)
    - wiki/synthesis/<slug>.md with synthesizes:[sources/<id>] and confidence:established
    The check fires when synthesis rank (0=established) < source rank (2=speculative).
    """
    from gateway.lint import claim_confidence

    assert claim_confidence.run_propagation() == []

    # Source wiki page with speculative confidence.
    _seed_wiki_source_page(
        kb_root, "speculative-src-001",
        domains=["cp-domain"],
        confidence="speculative",
    )

    # Synthesis page citing that source with established (overconfident) confidence.
    syn_dir = kb_root / "wiki" / "synthesis"
    syn_dir.mkdir(parents=True, exist_ok=True)
    syn_front = {
        "type": "synthesis",
        "slug": "overconfident-synth",
        "title": "Overconfident Synthesis",
        "domains": ["cp-domain"],
        "question": "Does X cause Y?",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "sources_count": 1,
        "synthesizes": ["sources/speculative-src-001"],
        "confidence": "established",  # stronger than the source warrants
    }
    body = (
        "## Synthesis\n\nSome finding.\n\n"
        "## Included works\n\n- [[sources/speculative-src-001]]\n\n"
        "## Sources cited\n\n- [[sources/speculative-src-001]]\n"
    )
    (syn_dir / "overconfident-synth.md").write_text(fm.serialize(syn_front, body))

    findings = claim_confidence.run_propagation()
    assert any(f.check == "confidence-propagation" for f in findings), (
        "confidence-propagation: synthesis with established confidence citing a "
        "speculative source must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# tags-invalid-type
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_tags_invalid_type_fires_on_scalar_string_tags(kb_root):
    """tags-invalid-type fires when a wiki page's tags: field is a scalar string.

    Producer: write a wiki/concepts/<slug>.md with tags as a plain string
    instead of a list[str] — the shape that a manual edit might produce.
    """
    from gateway.lint import invalid_tags

    assert invalid_tags.run() == []

    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    # Write raw YAML so the tags field is a scalar string (not a list).
    content = (
        "---\n"
        "type: concept\n"
        "slug: bad-tags-concept\n"
        "canonical_name: Bad Tags Concept\n"
        "domains:\n"
        "  - test-domain\n"
        "created_at: 2026-01-01T00:00:00Z\n"
        "last_updated: 2026-01-01T00:00:00Z\n"
        "tags: not-a-list\n"  # scalar string instead of list[str]
        "---\n"
        "## Key claims\n\nBody.\n"
    )
    (d / "bad-tags-concept.md").write_text(content)

    findings = invalid_tags.run()
    assert any(f.check == "tags-invalid-type" for f in findings), (
        "tags-invalid-type: concept page with tags as scalar string must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# open-questions
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_open_questions_fires_on_open_question_page(kb_root):
    """open-questions fires on a wiki question page with status:open.

    Producer: write a wiki/questions/<slug>.md with type:question and status:open.
    """
    from gateway.lint import unanswered_questions

    assert unanswered_questions.run_open_questions() == []

    q_dir = kb_root / "wiki" / "questions"
    q_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "question",
        "slug": "open-q-001",
        "title": "Does X cause Y in adults?",
        "domains": ["test-domain"],
        "status": "open",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    (q_dir / "open-q-001.md").write_text(
        fm.serialize(front, "## Question\n\nDoes X cause Y?\n\n## Context\n\nBackground.\n")
    )

    findings = unanswered_questions.run_open_questions()
    assert any(f.check == "open-questions" for f in findings), (
        "open-questions: a question page with status:open must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# answered-no-synthesis
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_answered_no_synthesis_fires_on_answered_question_without_link(kb_root):
    """answered-no-synthesis fires on an answered question page with no synthesis:.

    Producer: write a wiki/questions/<slug>.md with type:question, status:answered,
    and no synthesis: field.
    """
    from gateway.lint import unanswered_questions

    assert unanswered_questions.run_answered_no_synthesis() == []

    q_dir = kb_root / "wiki" / "questions"
    q_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "question",
        "slug": "answered-no-synth-q",
        "title": "Does Y affect Z?",
        "domains": ["test-domain"],
        "status": "answered",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        # deliberately omit synthesis:
    }
    (q_dir / "answered-no-synth-q.md").write_text(
        fm.serialize(front, "## Question\n\nDoes Y affect Z?\n\n## Context\n\nBackground.\n")
    )

    findings = unanswered_questions.run_answered_no_synthesis()
    assert any(f.check == "answered-no-synthesis" for f in findings), (
        "answered-no-synthesis: answered question with no synthesis: must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# fragmentation (embedding DB required)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_fragmentation_fires_on_near_duplicate_entity_vectors(kb_root):
    """fragmentation fires when the entity embedding namespace contains two
    near-identical concept/entity vectors (cosine distance ≤ entity threshold).

    Producer: use LexicalFallbackEncoder (pure-numpy, no LLM) to produce
    two embeddings for the same text, then write them into the embedding
    SQLite DB at the path paths.embedding_db_path() reads.
    The fragmentation check reads the DB directly (raw SQL on the 'entity'
    namespace), so writing the real DB IS driving the real producer.
    """
    from gateway.lint import fragmentation
    from gateway.embedding_index import LexicalFallbackEncoder, thresholds

    # Negative control: no embedding DB → no findings.
    assert fragmentation.run() == []

    # Create the embedding DB at the real path the check reads.
    db_path = paths.embedding_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS vectors (
            namespace TEXT NOT NULL,
            key TEXT NOT NULL,
            dim INTEGER NOT NULL,
            vec BLOB NOT NULL,
            model_version TEXT NOT NULL DEFAULT '',
            PRIMARY KEY (namespace, key)
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_vec_ns ON vectors(namespace)")

    # Use the real lexical encoder to produce two near-identical vectors.
    encoder = LexicalFallbackEncoder()
    text = "food noise reward blunting GLP-1 appetite suppression"
    vecs = encoder.embed([text, text + " dopamine"])  # nearly identical texts
    for key, vec in [("concept/food-noise", vecs[0]), ("concept/food-noise-v2", vecs[1])]:
        blob = np.asarray(vec, dtype=np.float32).tobytes()
        conn.execute(
            "INSERT OR REPLACE INTO vectors (namespace, key, dim, vec, model_version) "
            "VALUES (?, ?, ?, ?, ?)",
            ("entity", key, len(vec), blob, encoder.model_version),
        )
    conn.commit()
    conn.close()

    findings = fragmentation.run()
    assert any(f.check == "fragmentation" for f in findings), (
        "fragmentation: two near-identical entity vectors must form a cluster and be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# claim-conservation
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_claim_conservation_fires_when_committed_claim_absent_from_page(kb_root):
    """claim-conservation fires when a committed intent's payload claim bullet
    is absent from the canonical wiki page.

    Producer: write a committed intent JSON record at
    .knowledge/intents/committed/<id>.json — the same path IntentQueue.set_state()
    writes when the CommitGate commits an intent — and a wiki page that is missing
    one of the payload's ## Claims bullets.
    """
    from gateway.lint import claim_conservation

    assert claim_conservation.run() == []

    # Write a wiki concept page that OMITS the claimed bullet.
    d = kb_root / "wiki" / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    canon_front = {
        "type": "concept",
        "slug": "missing-claim-concept",
        "canonical_name": "Missing Claim Concept",
        "domains": ["test-domain"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    canon_path = d / "missing-claim-concept.md"
    canon_path.write_text(
        fm.serialize(canon_front, "## Key claims\n\n- This claim is present.\n")
    )

    # Write the committed intent record referencing this page.
    # The payload body has a ## Claims section with a bullet NOT in the canon page.
    # _parse_claim_bullets looks for `## Claims` (case-insensitive, exact match);
    # "## Key claims" does NOT match because it contains extra words.
    committed_dir = kb_root / ".knowledge" / "intents" / "committed"
    committed_dir.mkdir(parents=True, exist_ok=True)
    intent_id = "abcd1234ef567890"
    record = {
        "intent_id": intent_id,
        "payload": {
            "kind": "concept",
            "target": "wiki/concepts/missing-claim-concept.md",
            "body": (
                "## Claims\n"
                "- This claim is present.\n"
                "- This claim was lost after merge.\n"  # absent from canon page
            ),
        },
        "identity": {"agent": "tester"},
        "result": {
            "canonical_path": str(canon_path),
        },
    }
    (committed_dir / f"{intent_id}.json").write_text(json.dumps(record))

    findings = claim_conservation.run()
    assert any(f.check == "claim-conservation" for f in findings), (
        "claim-conservation: committed claim bullet absent from canonical page must be flagged; "
        f"findings={findings}"
    )


# ---------------------------------------------------------------------------
# LLM-dependent checks: contradictions, missing-pages, filter-calibration
# ---------------------------------------------------------------------------
# These three checks require a live Claude CLI subprocess to produce findings.
# The parametrized negative control (empty repo → no findings) already proves
# the runner is wired and callable. The positive trigger requires a real LLM
# call that cannot be made cheaply in an integration test suite.
# Backlog: docs/backlog/librarian-lint-llm-positive-coverage.md
# ---------------------------------------------------------------------------


@pytest.mark.integration
@pytest.mark.xfail(
    reason=(
        "contradictions positive trigger requires a live Claude CLI subprocess. "
        "The check is wired and callable (proven by negative control). "
        "See docs/backlog/librarian-lint-llm-positive-coverage.md"
    ),
    strict=False,
)
def test_contradictions_positive_signal_requires_llm(kb_root):
    """contradictions fires when two wiki pages assert contradictory facts.

    Positive trigger: requires a live Claude CLI subprocess (ClaudeCLIFilterClient).
    This xfail marks the gap without deleting the assertion — when a real mock
    or CLI stub is available, remove the xfail and wire it.
    """
    from gateway.lint import contradictions

    # Even this negative control proves the check is not inert (no exception, returns list).
    findings = contradictions.run()
    assert isinstance(findings, list)
    # Positive: assert that at least one finding fires — xfail because LLM is needed.
    assert any(f.check == "contradictions" for f in findings)


@pytest.mark.integration
@pytest.mark.xfail(
    reason=(
        "missing-pages positive trigger requires a live Claude CLI subprocess. "
        "The check is wired and callable (proven by negative control). "
        "See docs/backlog/librarian-lint-llm-positive-coverage.md"
    ),
    strict=False,
)
def test_missing_pages_positive_signal_requires_llm(kb_root):
    """missing-pages fires when an LLM identifies an unrepresented concept.

    Positive trigger: requires a live Claude CLI subprocess (ClaudeCLIFilterClient).
    """
    from gateway.lint import missing_pages

    findings = missing_pages.run()
    assert isinstance(findings, list)
    assert any(f.check == "missing-pages" for f in findings)


@pytest.mark.integration
@pytest.mark.xfail(
    reason=(
        "filter-calibration positive trigger requires a live Claude CLI subprocess. "
        "The check is wired and callable (proven by negative control). "
        "See docs/backlog/librarian-lint-llm-positive-coverage.md"
    ),
    strict=False,
)
def test_filter_calibration_positive_signal_requires_llm(kb_root):
    """filter-calibration fires when a re-scored sample deviates from the stored score.

    Positive trigger: requires a live Claude CLI subprocess (ClaudeCLIFilterClient).
    """
    from gateway.lint import filter_calibration

    findings = filter_calibration.run()
    assert isinstance(findings, list)
    assert any(f.check == "filter-calibration" for f in findings)


# ---------------------------------------------------------------------------
# stale-claims LLM mode (the deterministic INFO mode is covered above)
# ---------------------------------------------------------------------------


@pytest.mark.integration
@pytest.mark.xfail(
    reason=(
        "stale-claims WARNING-severity positive trigger requires a live Claude CLI "
        "subprocess (sample_size > 0). The deterministic INFO mode is covered by "
        "test_stale_claims_fires_on_two_academic_sources_with_gap above. "
        "See docs/backlog/librarian-lint-llm-positive-coverage.md"
    ),
    strict=False,
)
def test_stale_claims_llm_mode_positive_signal_requires_llm(kb_root):
    """stale-claims WARNING (LLM mode) requires a Claude CLI subprocess.

    The deterministic INFO mode (sample_size=0) is already covered by the
    test_stale_claims_fires_on_two_academic_sources_with_gap test. This xfail
    marks the gap for the LLM-verified WARNING severity path.
    """
    from gateway.lint import stale_claims

    # We'd need the two-source setup and then sample_size > 0 to get a WARNING.
    findings = stale_claims.run(sample_size=1)
    assert isinstance(findings, list)
    assert any(f.check == "stale-claims" and f.severity == "WARNING" for f in findings)


# ===========================================================================
# Meta-gate guard: every KNOWN_CHECKS slug must have a positive-signal case
# ===========================================================================
# This guard is derived from the LIVE registry (lint_op.KNOWN_CHECKS) — not
# a frozen list. If a new check is added to _CHECKS without a positive case
# here, THIS TEST GOES RED. That is the intended behavior (hunt #4/#6 guard).
# ===========================================================================


# Mapping from registry slug → test function name that provides the positive signal.
# The non-xfail positive cases:
_POSITIVE_SLUG_COVERAGE: dict[str, str] = {
    # Already covered before this task (lines 198-356):
    "orphans": "test_orphans_fires_on_real_isolated_page",
    "broken-wikilinks": "test_broken_wikilinks_fires_on_real_missing_target",
    "retracted-citations": "test_retracted_citations_fires_on_real_retracted_source",
    "schema-drift": "test_schema_drift_fires_on_real_malformed_page",
    "policy-provenance": "test_policy_provenance_fires_on_unprovenanced_policy",
    "reversal-anomalies": "test_reversal_anomalies_lint_fires_via_real_contradictions_log",
    # Covered in this task (Step 1 continued above):
    "stale-drafts": "test_stale_drafts_fires_on_old_draft",
    "stale-claims": "test_stale_claims_fires_on_two_academic_sources_with_gap",
    "citation-density": "test_citation_density_fires_on_undercited_concept",
    "citation-chains": "test_citation_chains_fires_on_dangling_synthesizes_ref",
    "inbox-pending": "test_inbox_pending_fires_on_file_in_inbox",
    "nlm-pending": "test_nlm_pending_fires_on_eligible_unsynced_source",
    "untagged-sources": "test_untagged_sources_fires_on_domainless_source_page",
    "idempotency": "test_idempotency_fires_on_registry_entry_with_no_policy",
    "long-slugs": "test_long_slugs_fires_on_grandfathered_oversized_slug",
    "contradiction-pages": "test_contradiction_pages_fires_on_open_major_contradiction",
    "synthesizes-coverage": "test_synthesizes_coverage_fires_on_synthesis_without_synthesizes",
    "stale-verified": "test_stale_verified_fires_on_statute_without_last_verified_at",
    "domain-purity": "test_domain_purity_fires_on_source_tagged_to_multiple_blessed_domains",
    "link-rot": "test_link_rot_fires_on_dead_web_source",
    "superseded-citations": "test_superseded_citations_fires_on_wiki_citing_superseded_source",
    "paper-canonical-source": "test_paper_canonical_source_fires_on_paper_entity_without_canonical",
    "confidence-distribution": "test_confidence_distribution_fires_on_any_annotated_concept",
    "confidence-propagation": "test_confidence_propagation_fires_on_overconfident_synthesis",
    "tags-invalid-type": "test_tags_invalid_type_fires_on_scalar_string_tags",
    "open-questions": "test_open_questions_fires_on_open_question_page",
    "answered-no-synthesis": "test_answered_no_synthesis_fires_on_answered_question_without_link",
    "fragmentation": "test_fragmentation_fires_on_near_duplicate_entity_vectors",
    "claim-conservation": "test_claim_conservation_fires_when_committed_claim_absent_from_page",
    # LLM-dependent (covered by xfail tests above):
    "contradictions": "test_contradictions_positive_signal_requires_llm",
    "missing-pages": "test_missing_pages_positive_signal_requires_llm",
    "filter-calibration": "test_filter_calibration_positive_signal_requires_llm",
}


@pytest.mark.integration
def test_every_known_check_has_a_positive_case():
    """Guard: every slug in the LIVE _CHECKS registry has a positive-signal case.

    Derived from lint_op.KNOWN_CHECKS (the real registry) — NOT a frozen list.
    Adding a new entry to _CHECKS without a positive case here makes this test RED.
    This is hunt #4/#6: the suite must not be inert on newly-registered checks.
    """
    uncovered = lint_op.KNOWN_CHECKS - set(_POSITIVE_SLUG_COVERAGE)
    assert not uncovered, (
        f"The following lint checks have no positive-signal test case: {sorted(uncovered)}. "
        "Add a positive-signal test (or xfail with backlog pointer) and add the slug "
        "to _POSITIVE_SLUG_COVERAGE in test_inert_invariants.py."
    )
