"""Derived retrieval index over wiki/ and raw/ (WS1, 2026-06-09 RAG review).

SQLite FTS5 database at `.index/wiki.db`. Markdown stays canonical; the
index is derived state — gitignored, rebuildable at any time with
`wiki index --rebuild`, and self-healing: every query first runs a cheap
mtime/size diff against the filesystem and upserts only changed files.
There is deliberately no write-path hook — coupling page writes to index
health would let an index failure break an ingest.

Granularity is the markdown section (ATX-heading delimited), so callers
can retrieve the relevant section of a page rather than the whole body.

Ranking: BM25 over weighted columns (title > slug > heading > body),
surfaced two ways:
  - `score` keeps the SRCH-1 integer-tier contract (3 = all query tokens
    in title, 2 = all in slug, 1 = body match) so existing consumers and
    ordering semantics survive.
  - `rank` is the raw BM25 relevance (higher = better) for callers that
    want pure lexical ordering (`order="bm25"`).
The tiered-vs-bm25 choice is adjudicated by the retrieval eval (WS4).
"""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from gateway import frontmatter as fm, paths

_SCHEMA_VERSION = 1

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")

# bm25() column weights, in column order:
# rel_path (unindexed), heading, body, title, slug_text
_BM25_WEIGHTS = "0.0, 2.0, 1.0, 5.0, 3.0"

_SNIPPET_TOKENS = 18


@dataclass
class IndexHit:
    rel_path: str          # e.g. "wiki/concepts/food-noise.md"
    slug: str
    title: str
    page_type: str
    domain: str            # first domain, or ""
    heading: str           # section heading the best match landed in
    snippet: str
    score: int             # SRCH-1 tier: 3 title, 2 slug, 1 body
    rank: float            # BM25 relevance, higher = better
    inbound_count: int = 0


@dataclass
class IndexStats:
    indexed: int = 0
    removed: int = 0
    unchanged: int = 0
    total_pages: int = 0


def available() -> bool:
    """True if the index database exists (built at least once)."""
    return paths.search_db_path().exists()


def _connect() -> sqlite3.Connection:
    paths.index_dir().mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(paths.search_db_path(), timeout=10.0)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=10000")
    return conn


def _init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
        CREATE TABLE IF NOT EXISTS pages (
            rel_path TEXT PRIMARY KEY,
            root TEXT NOT NULL,          -- 'wiki' | 'raw'
            slug TEXT NOT NULL,
            page_type TEXT NOT NULL DEFAULT '',
            title TEXT NOT NULL DEFAULT '',
            entity_kind TEXT NOT NULL DEFAULT '',
            draft INTEGER NOT NULL DEFAULT 0,
            mtime REAL NOT NULL,
            size INTEGER NOT NULL,
            last_updated TEXT NOT NULL DEFAULT ''
        );
        CREATE TABLE IF NOT EXISTS page_domains (
            rel_path TEXT NOT NULL,
            domain TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_pd_domain ON page_domains(domain);
        CREATE INDEX IF NOT EXISTS idx_pd_path ON page_domains(rel_path);
        CREATE TABLE IF NOT EXISTS links (
            src_rel TEXT NOT NULL,
            target_rel TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_links_target ON links(target_rel);
        CREATE INDEX IF NOT EXISTS idx_links_src ON links(src_rel);
        CREATE VIRTUAL TABLE IF NOT EXISTS sections USING fts5(
            rel_path UNINDEXED, heading, body, title, slug_text,
            tokenize='unicode61'
        );
        """
    )
    conn.execute(
        "INSERT OR REPLACE INTO meta (key, value) VALUES ('schema_version', ?)",
        (str(_SCHEMA_VERSION),),
    )


def _split_sections(body: str) -> list[tuple[str, str]]:
    """Split a markdown body into (heading, text) sections.

    Text before the first heading gets heading "".
    """
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


def _wikilink_targets(body: str) -> set[str]:
    """Resolve [[...]] links in a body to wiki rel_paths."""
    targets: set[str] = set()
    for raw in _WIKILINK_RE.findall(body):
        name = raw.strip()
        if not name or name.startswith("nlm:"):
            continue
        if "/" in name:
            targets.add(f"wiki/{name}.md" if not name.startswith("wiki/") else f"{name}.md")
        # bare links ([[food-noise]]) are ambiguous across kinds; skip in v1
    return {t for t in targets if t.endswith(".md")}


def _index_file(conn: sqlite3.Connection, path: Path, root_name: str, rel: str) -> None:
    try:
        text = path.read_text(errors="replace")
        stat = path.stat()
    except OSError:
        return
    try:
        front, body = fm.parse(text)
    except Exception:
        front, body = {}, text

    title = str(front.get("title") or front.get("canonical_name") or "")
    page_type = str(front.get("type", ""))
    entity_kind = str(front.get("entity_kind", ""))
    draft = 1 if front.get("draft") else 0
    last_updated = str(front.get("last_updated") or front.get("ingested_at") or "")
    slug = path.stem

    raw_domains = front.get("domains") or []
    if not isinstance(raw_domains, list):
        raw_domains = [raw_domains]
    single = front.get("domain")
    if single and single not in raw_domains:
        raw_domains.append(single)
    domains = [str(d) for d in raw_domains if d]

    aliases = front.get("aliases") or []
    if not isinstance(aliases, list):
        aliases = [aliases]
    slug_text = " ".join([slug, *[str(a) for a in aliases]])

    _remove_file(conn, rel)
    conn.execute(
        "INSERT INTO pages (rel_path, root, slug, page_type, title, entity_kind,"
        " draft, mtime, size, last_updated) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (rel, root_name, slug, page_type, title, entity_kind, draft,
         stat.st_mtime, stat.st_size, last_updated),
    )
    conn.executemany(
        "INSERT INTO page_domains (rel_path, domain) VALUES (?,?)",
        [(rel, d) for d in domains],
    )
    conn.executemany(
        "INSERT INTO links (src_rel, target_rel) VALUES (?,?)",
        [(rel, t) for t in _wikilink_targets(body)],
    )
    conn.executemany(
        "INSERT INTO sections (rel_path, heading, body, title, slug_text)"
        " VALUES (?,?,?,?,?)",
        [(rel, heading, sec_body, title, slug_text)
         for heading, sec_body in _split_sections(body)],
    )


def _remove_file(conn: sqlite3.Connection, rel: str) -> None:
    conn.execute("DELETE FROM pages WHERE rel_path = ?", (rel,))
    conn.execute("DELETE FROM page_domains WHERE rel_path = ?", (rel,))
    conn.execute("DELETE FROM links WHERE src_rel = ?", (rel,))
    conn.execute("DELETE FROM sections WHERE rel_path = ?", (rel,))


def _scan_files() -> dict[str, tuple[Path, str, float, int]]:
    """Map rel_path -> (abs_path, root, mtime, size) for all indexable files."""
    root = paths.knowledge_root()
    out: dict[str, tuple[Path, str, float, int]] = {}
    for base, name in ((paths.wiki_dir(), "wiki"), (paths.raw_dir(), "raw")):
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            if any(part.startswith(".") for part in p.relative_to(root).parts):
                continue
            try:
                stat = p.stat()
            except OSError:
                continue
            rel = str(p.relative_to(root))
            out[rel] = (p, name, stat.st_mtime, stat.st_size)
    return out


def refresh(*, rebuild: bool = False) -> IndexStats:
    """Bring the index in line with the filesystem.

    Cheap when nothing changed (one stat per file plus one SQL read).
    `rebuild=True` drops all rows and re-indexes from scratch.
    """
    stats = IndexStats()
    conn = _connect()
    try:
        _init_schema(conn)
        if rebuild:
            conn.execute("DELETE FROM pages")
            conn.execute("DELETE FROM page_domains")
            conn.execute("DELETE FROM links")
            conn.execute("DELETE FROM sections")

        on_disk = _scan_files()
        in_db = {
            rel: (mtime, size)
            for rel, mtime, size in conn.execute(
                "SELECT rel_path, mtime, size FROM pages"
            )
        }

        for rel, (abs_path, root_name, mtime, size) in on_disk.items():
            known = in_db.get(rel)
            if known and abs(known[0] - mtime) < 1e-6 and known[1] == size:
                stats.unchanged += 1
                continue
            _index_file(conn, abs_path, root_name, rel)
            stats.indexed += 1

        for rel in set(in_db) - set(on_disk):
            _remove_file(conn, rel)
            stats.removed += 1

        conn.commit()
        stats.total_pages = conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0]
    finally:
        conn.close()
    return stats


def _match_expr(query: str) -> str:
    """Build an FTS5 MATCH expression: prefix-match each token, OR-joined.

    OR (not AND) so partial coverage still surfaces, with BM25 ranking
    multi-token coverage higher. Prefix (*) preserves the substring
    behavior agents rely on for slug fragments.
    """
    tokens = _TOKEN_RE.findall(query.lower())
    return " OR ".join(f'"{t}" *' for t in tokens)


def _tier(tokens: list[str], title: str, slug_text: str) -> int:
    title_l, slug_l = title.lower(), slug_text.lower()
    if tokens and all(t in title_l for t in tokens):
        return 3
    if tokens and all(t in slug_l for t in tokens):
        return 2
    return 1


def search_fts(
    query: str,
    *,
    scope: str = "all",
    domain: str | None = None,
    page_type: str | None = None,
    limit: int = 20,
    order: str = "tiered",
    include_drafts: bool = True,
) -> list[IndexHit]:
    """BM25-ranked section search. Refreshes the index first (self-healing).

    Returns the best-matching section per page, at most `limit` pages.
    `order="tiered"` sorts by SRCH-1 tier then BM25; `order="bm25"` by
    BM25 alone.
    """
    expr = _match_expr(query)
    if not expr:
        return []
    refresh()

    tokens = _TOKEN_RE.findall(query.lower())
    where = ["sections MATCH ?"]
    params: list = [expr]
    if scope in ("wiki", "raw"):
        where.append("p.root = ?")
        params.append(scope)
    if page_type:
        where.append("p.page_type = ?")
        params.append(page_type)
    if domain:
        where.append(
            "p.rel_path IN (SELECT rel_path FROM page_domains WHERE domain = ?)"
        )
        params.append(domain)
    if not include_drafts:
        where.append("p.draft = 0")

    sql = f"""
        SELECT sections.rel_path, sections.heading,
               bm25(sections, {_BM25_WEIGHTS}) AS r,
               snippet(sections, 2, '', '', '…', {_SNIPPET_TOKENS}),
               p.slug, p.title, p.page_type,
               (SELECT domain FROM page_domains pd
                 WHERE pd.rel_path = p.rel_path LIMIT 1),
               (SELECT COUNT(*) FROM links l
                 WHERE l.target_rel = p.rel_path)
        FROM sections
        JOIN pages p ON p.rel_path = sections.rel_path
        WHERE {' AND '.join(where)}
        ORDER BY r
        LIMIT ?
    """
    # Over-fetch sections so best-section-per-page dedup still fills `limit`.
    params.append(max(limit * 4, 80))

    conn = _connect()
    try:
        rows = conn.execute(sql, params).fetchall()
    finally:
        conn.close()

    best: dict[str, IndexHit] = {}
    for rel, heading, r, snip, slug, title, ptype, dom, inbound in rows:
        if rel in best:
            continue
        slug_text = slug  # aliases already folded into the indexed column
        best[rel] = IndexHit(
            rel_path=rel,
            slug=slug,
            title=title or slug,
            page_type=ptype,
            domain=dom or "",
            heading=heading,
            snippet=(snip or "").strip(),
            score=_tier(tokens, title or "", slug_text),
            rank=-float(r),  # sqlite bm25 is lower-is-better; flip it
            inbound_count=int(inbound),
        )

    hits = list(best.values())
    if order == "bm25":
        hits.sort(key=lambda h: (-h.rank, h.title.lower()))
    else:
        hits.sort(key=lambda h: (-h.score, -h.rank, h.title.lower()))
    return hits[:limit]


def section_text(rel_path: str, heading: str) -> str:
    """Return the body text of the named section of a page (live read).

    Content is read from the file, not the index, so callers never serve
    stale section bodies. Matches the first section whose heading equals
    `heading` (the preamble section has heading "").
    """
    path = paths.knowledge_root() / rel_path
    try:
        _front, body = fm.parse(path.read_text(errors="replace"))
    except Exception:
        return ""
    for h, text in _split_sections(body):
        if h == heading:
            return text.strip()
    return ""


def top_pages_for_domain(
    domain: str,
    *,
    query: str | None = None,
    kinds: tuple[str, ...] = ("entities", "concepts", "synthesis", "mocs"),
    limit: int = 30,
) -> list[str]:
    """Rank a domain's wiki pages for plan context (TOK-4 follow-up).

    With a query (e.g. the incoming source title): FTS relevance order.
    Without: inbound-link count desc, then recency. Returns rel_paths.
    """
    refresh()
    prefixes = tuple(f"wiki/{k}/" for k in kinds)

    selected: list[str] = []
    if query and _match_expr(query):
        for hit in search_fts(query, scope="wiki", domain=domain, limit=limit * 2):
            if hit.rel_path.startswith(prefixes) and hit.rel_path not in selected:
                selected.append(hit.rel_path)
            if len(selected) >= limit:
                return selected

    conn = _connect()
    try:
        rows = conn.execute(
            """
            SELECT p.rel_path,
                   (SELECT COUNT(*) FROM links l WHERE l.target_rel = p.rel_path) AS inbound
            FROM pages p
            JOIN page_domains pd ON pd.rel_path = p.rel_path
            WHERE pd.domain = ? AND p.root = 'wiki'
            ORDER BY inbound DESC, p.last_updated DESC
            """,
            (domain,),
        ).fetchall()
    finally:
        conn.close()

    for rel, _inbound in rows:
        if rel.startswith(prefixes) and rel not in selected:
            selected.append(rel)
        if len(selected) >= limit:
            break
    return selected
