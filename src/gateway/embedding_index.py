"""Derived embedding index over wiki/ (Librarian Phase 2, design §13).

Adds ALONGSIDE the FTS index (`search_index.py`) with the same discipline:
the store at `.index/embeddings.db` is **derived state** — gitignored,
rebuildable from canonical markdown at any time, and never canonical. Markdown
stays the source of truth.

Unlike the FTS index, the embedding index **cannot self-heal lazily per query**:
commit-time dedup READS this index, so the committer upserts a committed page's
rows current-as-of-HEAD as part of the commit flow (an incremental upsert on
commit, not a lazy rebuild — see `commit_gate.py`). A lazy half-built index
would make a write (dedup) wrong.

Three namespaces at three granularities (decision 13, one encoder / three spaces):

- ``section``  — markdown section, query→passage relevance for retrieval.
- ``entity``   — entity/concept identity text, co-reference identity for dedup.
- ``question`` — gap-signature / question, topical-gap for demand clustering.

Each has its own operating-point threshold (`thresholds()`) and its own adequacy
gate (`evaluate.embedding_eval`).

**Encoder.** Pluggable behind a small protocol so a neural encoder can drop in
later behind «embed.model_version». The ACTIVE default is the I2 lexical fallback
(`LexicalFallbackEncoder`, `lexical-fallback-v1`): a deterministic,
pure-numpy hashed lexical vector (token-set + char-3-gram), L2-normalized. It is
honest and falsifiable — starting infrastructure, not a correctness guarantee.

**Rebuild concurrency (A6).** ``rebuild_from_canonical`` writes a complete fresh
index to a shadow location and atomically swaps it in (``os.replace``), so a
concurrent reader sees old-complete or new-complete, never half. Commits quiesce
on the ``librarian-embedding-rebuild`` lock for the swap window only.

**Rebuild-and-diff equivalence (F2).** ``diff_against_live`` rebuilds into the
shadow and diffs against the live store; any divergence is the §16
``index-rebuild-divergence`` bad state.
"""

from __future__ import annotations

import hashlib
import os
import re
import sqlite3
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol, Sequence, runtime_checkable

import numpy as np

from gateway import locking, paths

_SCHEMA_VERSION = 1
_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)

NAMESPACES: tuple[str, ...] = ("section", "entity", "question")

# Page types whose identity belongs in the `entity` (dedup) namespace.
_ENTITY_PAGE_TYPES = frozenset({"entity", "concept"})

REBUILD_LOCK = "librarian-embedding-rebuild"


# --- threshold operating points (§1.2; calibrated Phase 2, bound to model_version)

def thresholds() -> dict[str, float]:
    """Per-namespace cosine-DISTANCE operating points (match := dist <= threshold).

    Three operating points / threshold keys, not one (design §13):
    - section  → «embed.retrieval_relevance_threshold» (query→passage relevance)
    - entity   → «embed.dedup_identity_threshold» (strict co-reference identity)
    - question → «embed.demand_gap_threshold» (coarse topical-gap)
    """
    return {
        "section": 0.55,    # «embed.retrieval_relevance_threshold»
        "entity": 0.30,     # «embed.dedup_identity_threshold» (strictest)
        "question": 0.70,   # «embed.demand_gap_threshold» (coarsest)
    }


# --- pluggable encoder ---------------------------------------------------


@runtime_checkable
class Encoder(Protocol):
    model_version: str
    dim: int

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        ...


class LexicalFallbackEncoder:
    """Deterministic pure-numpy lexical encoder (I2 fallback, `lexical-fallback-v1`).

    Hashes word tokens and char-3-grams into a fixed-dim vector, then L2-normalizes.
    Same text → same vector (byte-stable across rebuilds); paraphrases share most
    n-grams so they land close; unrelated strings land far. No heavy ML deps.
    """

    model_version = "lexical-fallback-v1"
    dim = 256

    def _features(self, text: str) -> list[str]:
        norm = text.lower()
        tokens = _TOKEN_RE.findall(norm)
        feats: list[str] = list(tokens)
        # char-3-grams over the token-joined normalized text (paraphrase tolerance)
        joined = " ".join(tokens)
        feats.extend(joined[i : i + 3] for i in range(max(0, len(joined) - 2)))
        return feats

    def _hash_bucket(self, feature: str) -> tuple[int, float]:
        h = hashlib.blake2b(feature.encode("utf-8"), digest_size=8).digest()
        idx = int.from_bytes(h[:4], "big") % self.dim
        sign = 1.0 if (h[4] & 1) else -1.0  # signed hashing reduces collisions
        return idx, sign

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        out: list[list[float]] = []
        for text in texts:
            vec = np.zeros(self.dim, dtype=np.float32)
            for feat in self._features(text):
                idx, sign = self._hash_bucket(feat)
                vec[idx] += sign
            norm = float(np.linalg.norm(vec))
            if norm > 0.0:
                vec = vec / norm
            out.append(vec.astype(np.float32).tolist())
        return out


def default_encoder() -> Encoder:
    return LexicalFallbackEncoder()


# --- data shapes ---------------------------------------------------------


@dataclass
class NNHit:
    key: str
    distance: float


@dataclass
class RebuildStats:
    pages: int = 0
    rows: int = 0
    wall_seconds: float = 0.0
    model_version: str = ""


@dataclass
class DivergenceReport:
    missing: list[str] = field(default_factory=list)        # in live, not in rebuild
    extra: list[str] = field(default_factory=list)          # in rebuild, not in live
    vector_mismatch: list[str] = field(default_factory=list)

    @property
    def divergent(self) -> bool:
        return bool(self.missing or self.extra or self.vector_mismatch)


# --- the index -----------------------------------------------------------


class EmbeddingIndex:
    def __init__(self, encoder: Encoder | None = None, db_path: Path | None = None):
        self._encoder = encoder or default_encoder()
        self._db_path = db_path or paths.embedding_db_path()

    # -- connection / schema --

    def _connect(self, db_path: Path | None = None) -> sqlite3.Connection:
        path = db_path or self._db_path
        paths.index_dir().mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(path, timeout=10.0)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=10000")
        self._init_schema(conn)
        return conn

    def _init_schema(self, conn: sqlite3.Connection) -> None:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE IF NOT EXISTS vectors (
                namespace TEXT NOT NULL,
                key TEXT NOT NULL,
                dim INTEGER NOT NULL,
                vec BLOB NOT NULL,
                model_version TEXT NOT NULL,
                PRIMARY KEY (namespace, key)
            );
            CREATE INDEX IF NOT EXISTS idx_vec_ns ON vectors(namespace);
            """
        )
        conn.execute(
            "INSERT OR REPLACE INTO meta (key, value) VALUES ('schema_version', ?)",
            (str(_SCHEMA_VERSION),),
        )
        conn.execute(
            "INSERT OR IGNORE INTO meta (key, value) VALUES ('model_version', ?)",
            (self._encoder.model_version,),
        )

    def model_version(self) -> str:
        return self._encoder.model_version

    # -- write --

    def upsert(self, namespace: str, key: str, text: str) -> None:
        if namespace not in NAMESPACES:
            raise ValueError(f"unknown namespace: {namespace!r}")
        vec = self._encoder.embed([text])[0]
        blob = np.asarray(vec, dtype=np.float32).tobytes()
        conn = self._connect()
        try:
            conn.execute(
                "INSERT OR REPLACE INTO vectors "
                "(namespace, key, dim, vec, model_version) VALUES (?,?,?,?,?)",
                (namespace, key, len(vec), blob, self._encoder.model_version),
            )
            conn.commit()
        finally:
            conn.close()

    def _upsert_many(
        self, conn: sqlite3.Connection, rows: list[tuple[str, str, str]]
    ) -> None:
        """Batch upsert (namespace, key, text) on an open connection (rebuild path)."""
        if not rows:
            return
        vecs = self._encoder.embed([t for _ns, _k, t in rows])
        payload = [
            (ns, key, len(v), np.asarray(v, dtype=np.float32).tobytes(),
             self._encoder.model_version)
            for (ns, key, _t), v in zip(rows, vecs)
        ]
        conn.executemany(
            "INSERT OR REPLACE INTO vectors "
            "(namespace, key, dim, vec, model_version) VALUES (?,?,?,?,?)",
            payload,
        )

    def upsert_page(self, rel_path: str, content: str, front: dict) -> None:
        """Route a committed page's content into the relevant namespaces.

        - section: each markdown section → key ``rel_path#heading``.
        - entity:  entity/concept pages → key ``rel_path``, identity text =
          title + aliases + canonical_name (the identity surface, not the body).
        The ``question`` namespace is fed by the DemandLedger (Phase 5), not pages.
        """
        from gateway import frontmatter as fm

        _front, body = fm.parse(content)
        rows: list[tuple[str, str, str]] = []

        for heading, sec_body in _split_sections(body):
            sec_text = f"{heading}\n{sec_body}".strip()
            if sec_text:
                rows.append(("section", f"{rel_path}#{heading}", sec_text))

        ptype = str(front.get("type", ""))
        if ptype in _ENTITY_PAGE_TYPES:
            rows.append(("entity", rel_path, _identity_text(front)))

        if not rows:
            return
        conn = self._connect()
        try:
            self._upsert_many(conn, rows)
            conn.commit()
        finally:
            conn.close()

    # -- read --

    def nn(self, namespace: str, text: str, k: int = 5) -> list[NNHit]:
        """k nearest neighbors in a namespace by cosine distance (ascending)."""
        if namespace not in NAMESPACES:
            raise ValueError(f"unknown namespace: {namespace!r}")
        if not self._db_path.exists():
            return []
        q = np.asarray(self._encoder.embed([text])[0], dtype=np.float32)
        conn = self._connect()
        try:
            rows = conn.execute(
                "SELECT key, vec FROM vectors WHERE namespace = ?", (namespace,)
            ).fetchall()
        finally:
            conn.close()
        if not rows:
            return []
        keys = [r[0] for r in rows]
        mat = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
        # vectors are unit-norm; cosine distance = 1 - dot
        sims = mat @ q
        dists = 1.0 - sims
        order = np.argsort(dists)[:k]
        return [NNHit(key=keys[i], distance=float(dists[i])) for i in order]

    # -- rebuild (Task 4) --

    def _scan_canonical(self) -> list[tuple[str, str, dict]]:
        """(rel_path, content, front) for every canonical wiki page."""
        from gateway import frontmatter as fm

        root = paths.knowledge_root()
        wiki = paths.wiki_dir()
        out: list[tuple[str, str, dict]] = []
        if not wiki.exists():
            return out
        for p in sorted(wiki.rglob("*.md")):
            if any(part.startswith(".") for part in p.relative_to(root).parts):
                continue
            try:
                content = p.read_text(errors="replace")
            except OSError:
                continue
            try:
                front, _ = fm.parse(content)
            except Exception:
                front = {}
            out.append((str(p.relative_to(root)), content, front))
        return out

    def _build_into(self, db_path: Path) -> tuple[int, int]:
        """Build a complete index into ``db_path`` from canonical markdown.

        Returns (pages, rows). Does NOT swap — caller owns the swap.
        """
        if db_path.exists():
            db_path.unlink()
        for ext in ("-wal", "-shm"):
            side = db_path.with_name(db_path.name + ext)
            if side.exists():
                side.unlink()
        conn = self._connect(db_path)
        pages = 0
        rows_total = 0
        try:
            for rel_path, content, front in self._scan_canonical():
                from gateway import frontmatter as fm

                _front, body = fm.parse(content)
                rows: list[tuple[str, str, str]] = []
                for heading, sec_body in _split_sections(body):
                    sec_text = f"{heading}\n{sec_body}".strip()
                    if sec_text:
                        rows.append(("section", f"{rel_path}#{heading}", sec_text))
                if str(front.get("type", "")) in _ENTITY_PAGE_TYPES:
                    rows.append(("entity", rel_path, _identity_text(front)))
                if rows:
                    self._upsert_many(conn, rows)
                    rows_total += len(rows)
                pages += 1
            conn.commit()
        finally:
            conn.close()
        return pages, rows_total

    def rebuild_from_canonical(self) -> RebuildStats:
        """Shadow-swap rebuild (A6): build a complete index into the shadow
        location, then atomically swap it in. A concurrent reader sees
        old-complete or new-complete, never half.
        """
        shadow = paths.embedding_shadow_db_path()
        t0 = time.monotonic()
        pages, rows = self._build_into(shadow)
        # Atomic swap under the rebuild lock — the only quiesce window.
        with locking.file_lock(REBUILD_LOCK):
            # WAL side files were checkpointed on close; replace the main db file.
            os.replace(shadow, self._db_path)
            for ext in ("-wal", "-shm"):
                live_side = self._db_path.with_name(self._db_path.name + ext)
                if live_side.exists():
                    live_side.unlink()
        wall = time.monotonic() - t0
        return RebuildStats(
            pages=pages, rows=rows, wall_seconds=wall,
            model_version=self._encoder.model_version,
        )

    def _all_rows(self, db_path: Path) -> dict[str, bytes]:
        """{namespace\\x00key: vec_bytes} for every row in ``db_path``."""
        if not db_path.exists():
            return {}
        conn = self._connect(db_path)
        try:
            rows = conn.execute(
                "SELECT namespace, key, vec FROM vectors"
            ).fetchall()
        finally:
            conn.close()
        return {f"{ns}\x00{key}": vec for ns, key, vec in rows}

    def diff_against_live(self) -> DivergenceReport:
        """Rebuild into the shadow and diff against the live store (F2).

        Any divergence is the §16 ``index-rebuild-divergence`` bad state. Does
        NOT swap — this is a non-destructive equivalence check.
        """
        shadow = paths.embedding_shadow_db_path()
        self._build_into(shadow)
        live = self._all_rows(self._db_path)
        rebuilt = self._all_rows(shadow)
        # cleanup the shadow probe
        if shadow.exists():
            shadow.unlink()
        for ext in ("-wal", "-shm"):
            side = shadow.with_name(shadow.name + ext)
            if side.exists():
                side.unlink()

        report = DivergenceReport()
        for k in live.keys() - rebuilt.keys():
            report.missing.append(k.replace("\x00", "#"))
        for k in rebuilt.keys() - live.keys():
            report.extra.append(k.replace("\x00", "#"))
        for k in live.keys() & rebuilt.keys():
            if live[k] != rebuilt[k]:
                report.vector_mismatch.append(k.replace("\x00", "#"))
        report.missing.sort()
        report.extra.sort()
        report.vector_mismatch.sort()
        return report


# --- helpers -------------------------------------------------------------


def _identity_text(front: dict) -> str:
    parts: list[str] = []
    for key in ("title", "canonical_name"):
        v = front.get(key)
        if v:
            parts.append(str(v))
    aliases = front.get("aliases") or []
    if not isinstance(aliases, list):
        aliases = [aliases]
    parts.extend(str(a) for a in aliases if a)
    return " ".join(parts) if parts else str(front.get("title", ""))


def _split_sections(body: str) -> list[tuple[str, str]]:
    """Split a markdown body into (heading, text) sections (mirrors search_index)."""
    matches = list(_HEADING_RE.finditer(body))
    if not matches:
        return [("", body)] if body.strip() else []
    sections: list[tuple[str, str]] = []
    preamble = body[: matches[0].start()]
    if preamble.strip():
        sections.append(("", preamble))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        text = body[m.end():end]
        sections.append((m.group(2).strip(), text))
    return sections
