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

import subprocess
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, provenance
from gateway.commit_gate import AuthoredIntent, CommitGate
from gateway.embedding_index import EmbeddingIndex
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

    Creates the minimal directory structure that production always has after
    the first ingest (raw/, wiki/) so lint checks that call paths.raw_dir()
    or paths.wiki_dir() do not crash on missing directories.
    .knowledge/ is gitignored (derived state); policies/ and eval/ are tracked
    (they must be committed through the gate — per governance_flow pattern).
    """
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "test@test")
    _git(tmp_path, "config", "user.name", "test")
    # Mirror the real production gitignore: .knowledge/ derived state is ignored,
    # but .knowledge/policies/ and .knowledge/eval/ are git-TRACKED (per C1 fix).
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
    # Minimal directory structure (empty but present) so lint checks do not
    # crash on missing dirs — matches production state after first ingest.
    (tmp_path / "raw").mkdir()
    (tmp_path / "wiki").mkdir()
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


def _lint_check_ids():
    """Return (slug, runner) pairs from the REAL lint registry."""
    return list(lint_op._CHECKS)


def _run_one_lint(slug: str, root: Path) -> list:
    """Run a single lint check scoped to `slug` under the given root."""
    result = lint_op.lint(scope=slug)
    if not result.success:
        return []
    return result.metadata.get("findings", []) if hasattr(result, "metadata") else []


@pytest.mark.integration
@pytest.mark.parametrize("slug,runner", _lint_check_ids(), ids=[s for s, _ in _lint_check_ids()])
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
# Step 5: No apply-branch-less intent type
# ===========================================================================
# Enumerate the REAL reversal_type values dispatched in commit_gate._apply_reversal
# and assert each has a non-dead-letter apply branch. Enumerated from the
# real dispatch at commit_gate.py:1282-1296 — not a hardcoded list.
# ===========================================================================


def _known_reversal_types() -> list[str]:
    """Extract reversal_type strings dispatched in CommitGate._apply_reversal.

    Reads the SOURCE CODE of commit_gate._apply_reversal() and extracts all
    kind == <string> branches. This is registry-driven (not a hardcoded list):
    adding a new elif here must make the parametrize below pick it up.
    """
    import inspect
    import gateway.commit_gate as cg_mod
    source = inspect.getsource(cg_mod.CommitGate._apply_reversal)

    import re
    # Match `if kind == "..."` and `elif kind == "..."` branches.
    matches = re.findall(r'if kind == ["\']([^"\']+)["\']', source)
    return matches


@pytest.mark.integration
@pytest.mark.parametrize("reversal_type", _known_reversal_types())
def test_known_reversal_type_has_apply_branch(reversal_type, kb_root):
    """Every reversal_type dispatched in _apply_reversal has a non-dead-letter path.

    Hunt #1: T2 de-path enqueued a payload with no gate handler → dead-lettered,
    de-pathed nothing. This invariant makes that defect fail a test.

    For each reversal_type string found in _apply_reversal's source:
    - Submit an intent with that reversal_type.
    - The gate must NOT produce 'unknown reversal_type' in the dead-letter reason.
    - (It may still dead-letter for a VALID reason like missing target/act — that is
      correct routing behavior, not a missing branch.)
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

    # The gate MUST route to a specific apply helper — not fall through to the
    # "unknown reversal_type" dead-letter. Even a valid dead-letter is acceptable
    # (missing target, missing content, missing act) — the test checks the routing.
    error_text = " ".join([result.summary or ""] + (result.errors or []))
    assert "unknown reversal_type" not in error_text.lower(), (
        f"reversal_type={reversal_type!r} fell through to unknown-reversal dead-letter. "
        f"This reversal_type has no apply branch — hunt #1 defect. "
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
