"""Librarian Phase 2 (T4) — shadow-swap rebuild + quiesce + rebuild-and-diff.

Adversarial concurrency tests. The rebuild builds a COMPLETE index into a shadow
location then atomically swaps via os.replace, so a concurrent reader sees
old-complete or new-complete, never half. We exercise the REAL rebuild path with
REAL threads — os.replace is NOT monkeypatched. A slow encoder (real sleep in
embed()) widens the build window so a concurrent reader actually overlaps it.

Negative control: a deliberately non-atomic "rebuild" (build directly into the
live db) DOES expose a partial count to a concurrent reader — proving the test
can detect half-state, so the atomic path's clean reads are meaningful.
"""

from __future__ import annotations

import threading
import time

import pytest

from gateway import locking, paths
from gateway.embedding_index import (
    EmbeddingIndex,
    LexicalFallbackEncoder,
    REBUILD_LOCK,
)


@pytest.fixture
def wiki(tmp_path, monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_ROOT", str(tmp_path))
    w = tmp_path / "wiki" / "entities"
    w.mkdir(parents=True)
    return tmp_path


def _write_entity(root, slug, title, aliases=()):
    al = "[" + ", ".join(aliases) + "]" if aliases else "[]"
    (root / "wiki" / "entities" / f"{slug}.md").write_text(
        f"---\ntype: entity\ntitle: {title}\naliases: {al}\n---\n"
        f"# Overview\nAbout {title}.\n\n# Detail\nMore on {title}.\n"
    )


class _SlowEncoder(LexicalFallbackEncoder):
    """Real encoder that sleeps per-batch to widen the rebuild build window."""

    def __init__(self, delay=0.05):
        self._delay = delay

    def embed(self, texts):
        time.sleep(self._delay)
        return super().embed(texts)


def test_rebuild_lock_registered():
    assert REBUILD_LOCK in locking.LOCK_NAMES


def test_rebuild_shadow_swap_complete(wiki):
    for i in range(5):
        _write_entity(wiki, f"e{i}", f"Entity {i}")
    idx = EmbeddingIndex()
    stats = idx.rebuild_from_canonical()

    assert stats.pages == 5
    assert stats.rows > 0
    assert stats.wall_seconds > 0.0
    assert stats.model_version == "lexical-fallback-v1"

    # complete: every entity is searchable
    for i in range(5):
        hits = idx.nn("entity", f"Entity {i}", k=5)
        assert any(h.key == f"wiki/entities/e{i}.md" for h in hits)

    # mutate a page, rebuild → reflects the mutation, still complete, no orphan
    _write_entity(wiki, "e0", "Entity Zero Renamed")
    stats2 = idx.rebuild_from_canonical()
    assert stats2.pages == 5
    hits = idx.nn("entity", "Entity Zero Renamed", k=5)
    assert hits[0].key == "wiki/entities/e0.md"


def _count_entity_rows(idx):
    """Total entity-namespace rows visible to a fresh read (the live store)."""
    conn = idx._connect()
    try:
        return conn.execute(
            "SELECT COUNT(*) FROM vectors WHERE namespace='entity'"
        ).fetchone()[0]
    finally:
        conn.close()


def test_concurrent_read_during_rebuild_no_half_state(wiki):
    """REAL concurrency: while a rebuild runs (slow encoder), a reader polls the
    entity row count repeatedly. Every observation is either the full old count
    or the full new count — never a partial in-progress count."""
    n_old = 4
    for i in range(n_old):
        _write_entity(wiki, f"old{i}", f"Old {i}")

    # Seed the live store with the old set.
    EmbeddingIndex().rebuild_from_canonical()
    assert _count_entity_rows(EmbeddingIndex()) == n_old

    # Now add more pages so the rebuild changes the count.
    n_new = n_old + 6
    for i in range(n_old, n_new):
        _write_entity(wiki, f"old{i}", f"Old {i}")

    observed: list[int] = []
    errors: list[Exception] = []
    stop = threading.Event()

    def reader():
        rd = EmbeddingIndex()
        while not stop.is_set():
            try:
                observed.append(_count_entity_rows(rd))
            except Exception as e:  # a torn db would raise here
                errors.append(e)
            time.sleep(0.002)

    rt = threading.Thread(target=reader)
    rt.start()
    try:
        # Slow encoder → the build window is long enough to overlap the reader.
        EmbeddingIndex(encoder=_SlowEncoder(delay=0.03)).rebuild_from_canonical()
        time.sleep(0.05)  # let the reader sample the post-swap state
    finally:
        stop.set()
        rt.join()

    assert not errors, errors
    assert observed, "reader never sampled"
    # Every sample is a COMPLETE count — old-complete or new-complete, never half.
    assert set(observed) <= {n_old, n_new}, sorted(set(observed))
    assert n_new in observed, "reader never saw the post-swap complete state"


def test_nonatomic_rebuild_exposes_half_state_negative_control(wiki):
    """Negative control: a deliberately NON-atomic rebuild (incremental upserts
    directly into the live store) DOES expose partial counts to an external
    reader — proving the half-state detector in the atomic test above is real.

    Deterministic by construction: an external reader index (a separate
    instance, fresh connection per read) samples the live store after EVERY
    single upsert, so the partial counts are observed without depending on
    thread-scheduling timing. The prior concurrent-reader form was flaky — under
    GIL/SQLite contention the poller could sample only the 0 and n endpoints and
    miss every intermediate state (saw `[0, 12]`), failing spuriously."""
    n = 12
    for i in range(n):
        _write_entity(wiki, f"e{i}", f"Entity {i}")

    from gateway import frontmatter as fm

    writer = EmbeddingIndex()
    reader = EmbeddingIndex()  # a SEPARATE index instance — an external reader

    observed: list[int] = []
    for i in range(n):
        p = wiki / "wiki" / "entities" / f"e{i}.md"
        content = p.read_text()
        front, _ = fm.parse(content)
        # Non-atomic: commit one page at a time into the LIVE store.
        writer.upsert_page(f"wiki/entities/e{i}.md", content, front)
        # The external reader sees the live store mid-rebuild, after each commit.
        observed.append(_count_entity_rows(reader))

    # Every strictly-partial count 1..n-1 was visible to the external reader —
    # the non-atomic path leaks half-state (unlike the atomic shadow-swap, which
    # the test above proves never exposes a partial).
    partials = [c for c in observed if 0 < c < n]
    assert partials, f"expected partial counts, saw {sorted(set(observed))}"
    assert _count_entity_rows(reader) == n, "full set not visible after rebuild"


class _GatedRebuildEncoder(LexicalFallbackEncoder):
    """Real encoder whose FIRST embed() call (the rebuild's build phase) blocks
    until ``release`` is set, signalling ``in_build`` first. Lets a test land a
    concurrent commit-upsert squarely inside the rebuild's scan→swap window
    WITHOUT monkeypatching os.replace or the core path under test."""

    def __init__(self, in_build, release):
        self._in_build = in_build
        self._release = release
        self._gated = False

    def embed(self, texts):
        if not self._gated:
            self._gated = True
            self._in_build.set()
            self._release.wait(timeout=5.0)
        return super().embed(texts)


def _git_init_with_entities(wiki, n=4, prefix="seed"):
    import subprocess

    def _git(*args):
        return subprocess.run(["git", *args], cwd=wiki, capture_output=True, text=True, check=True)

    _git("init", "-q")
    _git("config", "user.email", "t@t")
    _git("config", "user.name", "t")
    (wiki / ".gitignore").write_text(".knowledge/\n.index/\n")
    _git("add", ".gitignore")
    _git("commit", "-qm", "seed")
    for i in range(n):
        _write_entity(wiki, f"{prefix}{i}", f"Seed {i}")
    _git("add", "wiki")
    _git("commit", "-qm", "seed entities")


def _commit_late_entity(wiki):
    """Run a real commit through the CommitGate for `wiki/entities/late.md`,
    upserting its embedding rows on the commit path. Returns the OperationResult."""
    from gateway.commit_gate import AuthoredIntent, CommitGate
    from gateway.intent_queue import Intent, IntentQueue, compute_intent_id

    q = IntentQueue()
    gate = CommitGate(queue=q, embedding_index=EmbeddingIndex())
    page = "---\ntype: entity\ntitle: Late Entity\naliases: []\n---\n# Overview\nx\n"
    payload = {"kind": "entity", "target": "wiki/entities/late.md"}
    ident = {"agent": "t"}
    iid = compute_intent_id(payload, ident)
    intent = Intent(intent_id=iid, payload=payload, identity=ident, head_oid="HEAD")
    q.submit(intent)
    q.claim(now=1.0)
    q.set_state(iid, "authored")
    token = q.fencing_token(iid)
    authored = AuthoredIntent(
        intent=intent, writes={"wiki/entities/late.md": page}, base_oid="HEAD"
    )
    return gate.commit(authored, token)


def test_commit_during_rebuild_row_survives_without_rebuild(wiki):
    """Finding 1 (lost-row rebuild race). A REAL commit upserts a page into the
    LIVE store while a REAL rebuild is mid-flight; the rebuild's scan ran BEFORE
    the commit landed, so its shadow lacks the late page. After both join, with
    NO intervening rebuild, the committed row MUST still be in the live store.

    No monkeypatch of os.replace. The gated encoder pins the rebuild inside its
    build window (after scan, before swap) so the commit upsert lands during it —
    the exact interleaving that the scan→swap window must be mutually exclusive
    against. RED on current code (swap clobbers the upsert); GREEN once the
    rebuild holds REBUILD_LOCK across scan+build+swap."""
    _git_init_with_entities(wiki, n=4)
    EmbeddingIndex().rebuild_from_canonical()

    in_build = threading.Event()
    release = threading.Event()
    rebuild_done = threading.Event()

    def do_rebuild():
        EmbeddingIndex(
            encoder=_GatedRebuildEncoder(in_build, release)
        ).rebuild_from_canonical()
        rebuild_done.set()

    t = threading.Thread(target=do_rebuild)
    t.start()
    try:
        # Wait until the rebuild is inside its build phase (scan already done).
        assert in_build.wait(timeout=5.0), "rebuild never entered build phase"
        # Land a real commit-upsert into the live store. With the fix, this blocks
        # on REBUILD_LOCK until the rebuild fully completes; without the fix it
        # races and the impending swap clobbers it.
        commit_thread_result: list = []

        def do_commit():
            commit_thread_result.append(_commit_late_entity(wiki))

        ct = threading.Thread(target=do_commit)
        ct.start()
        # Give the commit a beat to reach (and, on broken code, pass) its upsert.
        time.sleep(0.1)
    finally:
        release.set()
        t.join(timeout=10.0)
        ct.join(timeout=10.0)

    assert rebuild_done.is_set()
    assert commit_thread_result and commit_thread_result[0].success, commit_thread_result

    # No intervening rebuild — the committed row must already be in the LIVE store.
    hits = EmbeddingIndex().nn("entity", "Late Entity", k=5)
    assert any(h.key == "wiki/entities/late.md" for h in hits), (
        "committed row was clobbered by the rebuild swap (lost-row race)"
    )


def test_commit_quiesced_during_rebuild(wiki, monkeypatch):
    """A commit's embedding upsert and a rebuild swap serialize on the rebuild
    lock; post-state is consistent regardless of interleaving (real thread+lock).

    Finding 1b: assert the late row survives in the LIVE store WITHOUT any
    intervening rebuild (the prior version did a final rebuild and accepted
    'recoverable by a fresh rebuild', which masked the lost-row race)."""
    _git_init_with_entities(wiki, n=4)

    idx = EmbeddingIndex()
    idx.rebuild_from_canonical()

    # Start a slow rebuild in the background (holds the lock across scan→swap).
    rebuild_done = threading.Event()

    def do_rebuild():
        EmbeddingIndex(encoder=_SlowEncoder(delay=0.02)).rebuild_from_canonical()
        rebuild_done.set()

    t = threading.Thread(target=do_rebuild)
    t.start()
    r = _commit_late_entity(wiki)  # blocks on the rebuild lock if mid-rebuild
    t.join()

    assert r.success, r.errors
    assert rebuild_done.is_set()
    # The committed page survived in the LIVE store with NO intervening rebuild.
    hits = EmbeddingIndex().nn("entity", "Late Entity", k=5)
    assert any(h.key == "wiki/entities/late.md" for h in hits)


def test_rebuild_and_diff_detects_divergence(wiki):
    """F2: diff_against_live reports divergence, binds the index-rebuild-divergence
    bad state. Empty on a fresh-equal store; reports the exact corrupted/missing key."""
    for i in range(4):
        _write_entity(wiki, f"e{i}", f"Entity {i}")
    idx = EmbeddingIndex()
    idx.rebuild_from_canonical()

    # equal: no divergence
    report = idx.diff_against_live()
    assert not report.divergent, (report.missing, report.extra, report.vector_mismatch)

    # corrupt one live vector → exactly that key reported as vector_mismatch
    conn = idx._connect()
    try:
        bad = b"\x00" * (4 * 256)  # 256 float32 zeros
        target = conn.execute(
            "SELECT key FROM vectors WHERE namespace='entity' ORDER BY key LIMIT 1"
        ).fetchone()[0]
        conn.execute(
            "UPDATE vectors SET vec=? WHERE namespace='entity' AND key=?",
            (bad, target),
        )
        conn.commit()
    finally:
        conn.close()
    report = idx.diff_against_live()
    assert report.vector_mismatch == [f"entity#{target}"], report.vector_mismatch
    # negative control: an unrelated key is NOT reported
    assert not report.missing and not report.extra

    # delete one live row → canonical still has it → it's EXTRA (in rebuild,
    # absent from live = live is stale-missing a row).
    conn = idx._connect()
    try:
        gone = conn.execute(
            "SELECT key FROM vectors WHERE namespace='entity' AND key != ? "
            "ORDER BY key LIMIT 1",
            (target,),
        ).fetchone()[0]
        conn.execute(
            "DELETE FROM vectors WHERE namespace='entity' AND key=?", (gone,)
        )
        conn.commit()
    finally:
        conn.close()
    report = idx.diff_against_live()
    assert f"entity#{gone}" in report.extra, report.extra
    assert f"entity#{target}" in report.vector_mismatch


def test_rebuild_and_diff_detects_orphan_missing(wiki):
    """A live row whose canonical page was deleted is reported as MISSING (in
    live, absent from a fresh rebuild) — the stale-orphan-row bad state."""
    for i in range(3):
        _write_entity(wiki, f"e{i}", f"Entity {i}")
    idx = EmbeddingIndex()
    idx.rebuild_from_canonical()
    assert not idx.diff_against_live().divergent

    # Delete the canonical markdown but leave the live embedding row in place.
    (wiki / "wiki" / "entities" / "e1.md").unlink()
    report = idx.diff_against_live()
    assert "entity#wiki/entities/e1.md" in report.missing, report.missing
    # the section rows of the deleted page are also missing
    assert any(m.startswith("section#wiki/entities/e1.md") for m in report.missing)
    # negative control: surviving pages are not flagged
    assert "entity#wiki/entities/e0.md" not in report.missing
