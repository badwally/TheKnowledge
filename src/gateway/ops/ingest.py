"""`wiki ingest` — ingest a single source into the canonical knowledge base.

M1: input is an already-canonical markdown file (frontmatter shape per WIKI.md § 3).
M2: input may also be a URL — dispatched to a converter that returns canonical text.
M3: filter runs between validation and wiki-page write.
M6: agent-driven multi-page authorship layered on top.
"""

from __future__ import annotations

from pathlib import Path

from gateway import converters, frontmatter as fm
from gateway import index, log, paths, validator
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock


# --- public entry points -----------------------------------------------------


def ingest(source: str | Path) -> OperationResult:
    """Top-level dispatcher. Accepts a URL string or a filesystem path."""
    if isinstance(source, str) and source.startswith(("http://", "https://")):
        return ingest_url(source)
    path = Path(source).expanduser() if isinstance(source, str) else source
    return ingest_canonical(path)


def ingest_canonical(input_path: Path) -> OperationResult:
    """Ingest from a canonical markdown file path (M1 path)."""
    if not input_path.exists():
        return OperationResult(
            success=False,
            errors=[f"input not found: {input_path}"],
        )
    return _ingest_canonical_text(input_path.read_text())


def ingest_url(url: str) -> OperationResult:
    """Ingest from a URL via converter dispatch (M2 path)."""
    try:
        converter = converters.dispatch(url)
    except converters.NoConverterError as e:
        return OperationResult(success=False, errors=[str(e)])

    try:
        text = converter.convert(url)
    except converters.ConversionError as e:
        return OperationResult(success=False, errors=[f"conversion failed: {e}"])

    return _ingest_canonical_text(text)


# --- core ingest logic -------------------------------------------------------


def _ingest_canonical_text(text: str) -> OperationResult:
    """Validate canonical markdown text and commit to raw/ + wiki/sources/."""
    try:
        front, body = fm.parse(text)
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    result = validator.validate_source_frontmatter(front)
    result.merge(validator.validate_content_hash(front, body))
    result.merge(validator.validate_wikilinks(body))

    if not result.ok:
        return OperationResult(
            success=False,
            errors=[str(e) for e in result.errors],
            warnings=[str(w) for w in result.warnings],
        )

    source_id = front["id"]
    source_type = front["type"]
    raw_target = paths.raw_source_path(source_type, source_id)
    wiki_target = paths.wiki_source_path(source_id)

    with file_lock(f"ingest-{source_id}"):
        if raw_target.exists():
            existing_text = raw_target.read_text()
            try:
                existing_front, existing_body = fm.parse(existing_text)
            except fm.FrontmatterError as e:
                return OperationResult(
                    success=False,
                    errors=[f"existing raw file has malformed frontmatter: {e}"],
                )

            imm = validator.validate_source_immutability(existing_body, body)
            if not imm.ok:
                return OperationResult(
                    success=False,
                    errors=[str(e) for e in imm.errors],
                )

            if existing_front.get("content_hash") == front["content_hash"]:
                return OperationResult(
                    success=True,
                    no_op=True,
                    summary=f"already ingested (no-op): {source_id}",
                )

        canonical_text = fm.serialize(front, body)
        write_atomic(raw_target, canonical_text)
        write_atomic(wiki_target, _make_source_page(front))

        index.update_for(
            source_id=source_id,
            source_type=source_type,
            title=front.get("title", "(untitled)"),
            domains=front.get("domains", []),
        )

        domains = front.get("domains") or []
        log.append(
            op="ingest",
            fields={
                "id": source_id,
                "type": source_type,
                "domains": ",".join(domains) if domains else "-",
            },
            summary=(
                f"raw={raw_target.relative_to(paths.knowledge_root())} "
                f"wiki={wiki_target.relative_to(paths.knowledge_root())}"
            ),
        )

        return OperationResult(
            success=True,
            paths_touched=[
                raw_target,
                wiki_target,
                paths.index_path(),
                paths.log_path(),
            ],
            summary=f"ingested: {source_id} ({source_type})",
        )


# --- wiki source page generation --------------------------------------------


def _make_source_page(front: dict) -> str:
    """Build a minimal wiki/sources/<id>.md page from raw frontmatter.

    M3 fills filter rationale. M6 has the agent populate Summary / Key claims /
    Cross-references with proper citations.
    """
    page_front = {
        "type": "source",
        "source_id": front["id"],
        "source_type": front["type"],
        "title": front["title"],
        "domains": front.get("domains", []),
        "ingested_at": front["ingested_at"],
    }

    if "filter" in front and isinstance(front["filter"], dict):
        page_front["filter_score"] = front["filter"].get("score")
    if front.get("nlm_corpus_ids"):
        page_front["nlm_corpus_ids"] = front["nlm_corpus_ids"]

    raw_link = f"raw/{front['type']}/{front['id']}"
    url = front.get("url", "")
    authors = ", ".join(front.get("authors", [])) or "(unknown)"
    published = front.get("published_at", "")

    header_bits = [f"[[{raw_link}]]", front["type"]]
    if url:
        header_bits.append(f"[original]({url})")
    if published:
        header_bits.append(str(published))
    source_header = "**Source:** " + " · ".join(header_bits)

    lines = [
        f"# {front['title']}",
        "",
        source_header,
        f"**Authors:** {authors}",
    ]

    if "filter" in front and isinstance(front["filter"], dict):
        f_score = front["filter"].get("score")
        f_pol = front["filter"].get("policy_version", "")
        f_rat = front["filter"].get("rationale", "")
        lines.append(f"**Filter:** {f_score} ({f_pol}) — {f_rat}")

    lines.extend([
        "",
        "## Summary",
        "",
        "_(summary not yet generated — agent-driven authorship lands in M6)_",
        "",
        "## Key claims",
        "",
        "_(claims not yet extracted)_",
        "",
        "## Cross-references",
        "",
        "_(no cross-references yet)_",
        "",
    ])

    body = "\n".join(lines)
    return fm.serialize(page_front, body)
