"""`wiki ingest` — ingest a single source into the canonical knowledge base.

M1: input is an already-canonical markdown file.
M2: URL inputs dispatched to converters.
M3: semantic filter runs after validation; gates wiki-page creation by threshold.
M6: agent-driven multi-page authorship layered on top.
"""

from __future__ import annotations

from pathlib import Path

from gateway import converters, frontmatter as fm
from gateway import index, log, paths, validator
from gateway.core import OperationResult, write_atomic
from gateway.filter import (
    FilterError,
    PolicyError,
    load_all,
    load_policy,
    policy_exists,
    score as filter_score,
    select as select_examples,
)
from gateway.filter.semantic import FilterClient
from gateway.locking import file_lock


# --- public entry points -----------------------------------------------------


def ingest(
    source: str | Path,
    *,
    domain: str | None = None,
    filter_client: FilterClient | None = None,
) -> OperationResult:
    """Top-level dispatcher. Accepts a URL string or a filesystem path."""
    if isinstance(source, str) and source.startswith(("http://", "https://")):
        return ingest_url(source, domain=domain, filter_client=filter_client)
    path = Path(source).expanduser() if isinstance(source, str) else source
    return ingest_canonical(path, domain=domain, filter_client=filter_client)


def ingest_canonical(
    input_path: Path,
    *,
    domain: str | None = None,
    filter_client: FilterClient | None = None,
) -> OperationResult:
    """Ingest from a canonical markdown file path."""
    if not input_path.exists():
        return OperationResult(
            success=False,
            errors=[f"input not found: {input_path}"],
        )
    return _ingest_canonical_text(
        input_path.read_text(),
        domain=domain,
        filter_client=filter_client,
    )


def ingest_url(
    url: str,
    *,
    domain: str | None = None,
    filter_client: FilterClient | None = None,
) -> OperationResult:
    """Ingest from a URL via converter dispatch."""
    try:
        converter = converters.dispatch(url)
    except converters.NoConverterError as e:
        return OperationResult(success=False, errors=[str(e)])

    try:
        text = converter.convert(url)
    except converters.ConversionError as e:
        return OperationResult(success=False, errors=[f"conversion failed: {e}"])

    return _ingest_canonical_text(
        text,
        domain=domain,
        filter_client=filter_client,
    )


# --- core ingest logic -------------------------------------------------------


def _ingest_canonical_text(
    text: str,
    *,
    domain: str | None = None,
    filter_client: FilterClient | None = None,
) -> OperationResult:
    """Validate canonical markdown, run filter, commit to raw/ + (if passed) wiki/sources/."""
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
        # Idempotency / immutability check against existing raw file
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

        # Run the semantic filter (if domain available)
        effective_domain, filter_decision, filter_warnings = _run_filter(
            front=front,
            body=body,
            explicit_domain=domain,
            client=filter_client,
        )

        canonical_text = fm.serialize(front, body)
        write_atomic(raw_target, canonical_text)

        wiki_written = False
        if filter_decision in ("included", "no-domain"):
            write_atomic(wiki_target, _make_source_page(front))
            index.update_for(
                source_id=source_id,
                source_type=source_type,
                title=front.get("title", "(untitled)"),
                domains=front.get("domains", []),
            )
            wiki_written = True

        log_fields = {
            "id": source_id,
            "type": source_type,
            "domains": ",".join(front.get("domains", []) or []) or "-",
            "filter": filter_decision,
        }
        if effective_domain:
            log_fields["domain"] = effective_domain
        score_value = (front.get("filter") or {}).get("score")
        if score_value is not None:
            log_fields["score"] = score_value

        log.append(
            op="ingest",
            fields=log_fields,
            summary=(
                f"raw={raw_target.relative_to(paths.knowledge_root())}"
                + (
                    f" wiki={wiki_target.relative_to(paths.knowledge_root())}"
                    if wiki_written
                    else " (wiki not written: filter decision={})".format(filter_decision)
                )
            ),
        )

        paths_touched = [raw_target, paths.log_path()]
        if wiki_written:
            paths_touched.extend([wiki_target, paths.index_path()])

        summary = f"ingested: {source_id} ({source_type})"
        if filter_decision in ("review", "rejected"):
            summary += f" — wiki page not created ({filter_decision})"

        return OperationResult(
            success=True,
            paths_touched=paths_touched,
            summary=summary,
            warnings=filter_warnings,
        )


# --- filter integration -----------------------------------------------------


def _run_filter(
    *,
    front: dict,
    body: str,
    explicit_domain: str | None,
    client: FilterClient | None,
) -> tuple[str | None, str, list[str]]:
    """Run the filter if a domain is available. Mutates front to add filter: block.

    Returns (effective_domain, decision, warnings) where decision is one of:
    - "included":   score >= threshold_include — wiki page should be written
    - "review":     threshold_review <= score < threshold_include — no wiki page
    - "rejected":   score < threshold_review — no wiki page
    - "no-domain":  no domain available; filter skipped, wiki page proceeds anyway
    - "skipped":    domain set but no policy file; no wiki page
    - "errored":    filter call failed; no wiki page
    """
    warnings: list[str] = []
    effective_domain = explicit_domain or _first_domain(front)

    if not effective_domain:
        warnings.append(
            "no domain in frontmatter and no --domain flag; filter skipped, "
            "source ingested with wiki page (low-stakes incremental path)"
        )
        return None, "no-domain", warnings

    if not policy_exists(effective_domain):
        warnings.append(
            f"domain {effective_domain!r} has no policy file; filter skipped, "
            "wiki page not written"
        )
        return effective_domain, "skipped", warnings

    try:
        policy = load_policy(effective_domain)
    except PolicyError as e:
        warnings.append(f"policy load failed for {effective_domain!r}: {e}")
        return effective_domain, "errored", warnings

    examples = select_examples(load_all(effective_domain), policy)

    try:
        result = filter_score(front, body, policy, examples, client=client)
    except FilterError as e:
        warnings.append(f"filter call failed: {e}")
        return effective_domain, "errored", warnings

    front["filter"] = result.to_frontmatter_block()

    # Ensure the source's domains list includes the domain the filter ran against
    domains = list(front.get("domains") or [])
    if effective_domain not in domains:
        domains.append(effective_domain)
        front["domains"] = domains

    if result.score >= policy.threshold_include:
        return effective_domain, "included", warnings
    if result.score >= policy.threshold_review:
        return effective_domain, "review", warnings
    return effective_domain, "rejected", warnings


def _first_domain(front: dict) -> str | None:
    domains = front.get("domains") or []
    return str(domains[0]) if domains else None


# --- wiki source page generation --------------------------------------------


def _make_source_page(front: dict) -> str:
    """Build a minimal wiki/sources/<id>.md page from raw frontmatter."""
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
