"""`wiki nlm-*` operations.

Every NotebookLM interaction goes through this module. Each operation:

1. Validates inputs.
2. Resolves (or creates) the domain's notebook in nlm/notebooks.yaml.
3. Calls the injected `NlmClient` (defaults to `NlmCLIClient` shelling out).
4. Downloads the artifact (if applicable) into wiki/artifacts/<type>/.
5. Writes a wiki artifact page with bidirectional links per WIKI § 4.6.
6. Updates referenced source pages' `wiki_pages:` frontmatter and corpus IDs.
7. Appends a log.md entry.
8. Returns a structured `OperationResult`.

This is the architectural Discipline Gate.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import time

from gateway import frontmatter as fm
from gateway import log, nlm_registry, paths
from gateway.core import OperationResult, write_atomic
from gateway.locking import file_lock
from gateway.nlm_client import (
    ArtifactInfo,
    NlmClient,
    NlmCLIClient,
    NlmError,
    notebook_artifact_url,
    notebook_url,
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def _slugify(topic: str, *, max_words: int = 6) -> str:
    """Lowercase, hyphenate, drop punctuation, cap word count."""
    cleaned = _SLUG_STRIP.sub("-", topic.lower()).strip("-")
    words = [w for w in cleaned.split("-") if w]
    return "-".join(words[:max_words]) or "untitled"


def _artifact_slug(topic: str, *, suffix: str) -> str:
    return f"{_today_str()}-{_slugify(topic)}-{suffix}"


# --- shared helpers ---------------------------------------------------------


def _resolve_or_create_notebook(
    domain: str, *, client: NlmClient, auto_create: bool = True
) -> str:
    """Return the notebook_id for `domain`, creating one if needed."""
    notebook_id = nlm_registry.get_notebook_id(domain)
    if notebook_id:
        return notebook_id
    if not auto_create:
        raise NlmError(f"no notebook registered for domain {domain!r}; run `wiki nlm-add` first")

    title = f"{domain} (knowledge base)"
    notebook_id = client.notebook_create(title)
    nlm_registry.register(domain, notebook_id)
    return notebook_id


def _find_source(source_id: str) -> tuple[str, Path] | None:
    for source_type in paths.SOURCE_TYPES:
        candidate = paths.raw_source_path(source_type, source_id)
        if candidate.exists():
            return source_type, candidate
    return None


def _build_artifact_page(
    *,
    artifact_type: str,
    slug: str,
    title: str,
    domain: str,
    notebook_id: str,
    artifact_info: ArtifactInfo,
    local_file: Path,
    question: str,
    sources_used: list[str] | None = None,
) -> str:
    """Build a wiki/artifacts/<type>/<slug>.md page per WIKI § 4.6."""
    page_front = {
        "type": "artifact",
        "artifact_type": artifact_type,
        "slug": slug,
        "title": title,
        "domain": domain,
        "created_at": _now_iso(),
        "nlm_notebook_id": notebook_id,
        "nlm_artifact_id": artifact_info.artifact_id or None,
        "nlm_artifact_url": notebook_artifact_url(notebook_id, artifact_info.artifact_id),
        "local_file": str(local_file.relative_to(paths.knowledge_root())),
        "question": question,
    }
    # Prune None values for clean YAML
    page_front = {k: v for k, v in page_front.items() if v is not None}

    sources_section = "\n".join(
        f"- [[sources/{sid}]]" for sid in (sources_used or [])
    ) or "_(no source pages cited explicitly; see notebook for source list)_"

    body_lines = [
        f"# {title}",
        "",
        f"**Created:** {_now_iso()}",
        f"**Domain:** {domain}",
        f"**Origin question:** {question}",
        "",
        "## Local file",
        "",
        f"[[{local_file.relative_to(paths.knowledge_root())}]]",
        "",
        "## NotebookLM (live, editable)",
        "",
        f"<{notebook_artifact_url(notebook_id, artifact_info.artifact_id)}>",
        "",
        "## Sources used",
        "",
        sources_section,
        "",
    ]
    return fm.serialize(page_front, "\n".join(body_lines))


def _add_artifact_to_source_pages(artifact_path_rel: str, source_ids: list[str]) -> None:
    """Append the artifact page to each source's `wiki_pages:` for backlink integrity."""
    for source_id in source_ids:
        found = _find_source(source_id)
        if not found:
            continue
        _, raw_path = found
        try:
            front, body = fm.parse(raw_path.read_text())
        except fm.FrontmatterError:
            continue
        wiki_pages = list(front.get("wiki_pages") or [])
        if artifact_path_rel not in wiki_pages:
            wiki_pages.append(artifact_path_rel)
            front["wiki_pages"] = wiki_pages
            write_atomic(raw_path, fm.serialize(front, body))


# --- nlm-add ----------------------------------------------------------------


def nlm_add(
    domain: str,
    source_id: str,
    *,
    client: NlmClient | None = None,
) -> OperationResult:
    """Add a source already in raw/ to the domain's NotebookLM corpus."""
    client = client or NlmCLIClient()

    found = _find_source(source_id)
    if found is None:
        return OperationResult(success=False, errors=[f"no raw source found with id {source_id!r}"])
    source_type, raw_path = found

    try:
        front, body = fm.parse(raw_path.read_text())
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    url = front.get("url")
    has_body = bool(body and body.strip())
    sidecar_rel = front.get("source_path")
    sidecar_path: Path | None = None
    if sidecar_rel:
        candidate = paths.knowledge_root() / str(sidecar_rel)
        if candidate.exists():
            sidecar_path = candidate
    if not url and not has_body and sidecar_path is None:
        return OperationResult(
            success=False,
            errors=[
                f"source {source_id} has no `url`, no sidecar binary, and empty body; "
                "nothing to add to NotebookLM"
            ],
        )

    try:
        notebook_id = _resolve_or_create_notebook(domain, client=client)
    except NlmError as e:
        return OperationResult(success=False, errors=[f"notebook setup: {e}"])

    existing_corpus_ids = list(front.get("nlm_corpus_ids") or [])
    if notebook_id in existing_corpus_ids:
        return OperationResult(
            success=True,
            no_op=True,
            summary=f"already in {domain} corpus ({notebook_id})",
        )

    with file_lock(f"ingest-{source_id}"):
        title = str(front.get("title") or source_id)
        if url:
            url_err: NlmError | None = None
            try:
                client.source_add_url(notebook_id, url)
                log_summary = f"url={url}"
            except NlmError as e:
                url_err = e
            if url_err is not None:
                # M46-followup Fix B: NotebookLM's URL crawler is blocked by
                # some publishers (Substack, Cloudflare bot-protection). The
                # raw markdown body is what NLM ultimately indexes anyway, so
                # fall back to --text when --url fails. Only attempt the
                # fallback if the body is non-empty — otherwise there's
                # nothing to send and we surface the URL failure.
                if body.strip():
                    try:
                        client.source_add_text(notebook_id, body, title=title)
                        log_summary = (
                            f"url-failed-fell-back-to-text url={url} text={len(body)}b"
                        )
                    except NlmError as text_err:
                        return OperationResult(
                            success=False,
                            errors=[
                                f"nlm add url failed: {url_err}",
                                f"nlm add text fallback also failed: {text_err}",
                            ],
                        )
                else:
                    return OperationResult(
                        success=False,
                        errors=[f"nlm add url failed: {url_err}"],
                    )
        elif sidecar_path is not None:
            # M37 preferred path for PDF/docx/xlsx/pptx/image/voice: upload
            # the sidecar binary so NotebookLM gets layout, figures, and
            # native processing rather than just the gateway's extracted text.
            try:
                client.source_add_file(notebook_id, sidecar_path, title=title)
            except NlmError as e:
                return OperationResult(success=False, errors=[f"nlm add file failed: {e}"])
            log_summary = f"file={sidecar_path.name} title={title!r}"
        else:
            # M37 fallback: source has only the canonical extracted text
            # (note, web-no-url, etc.). Send body as a text source.
            try:
                client.source_add_text(notebook_id, body, title=title)
            except NlmError as e:
                return OperationResult(success=False, errors=[f"nlm add text failed: {e}"])
            log_summary = f"text={len(body)}b title={title!r}"

        front["nlm_corpus_ids"] = existing_corpus_ids + [notebook_id]
        domains = list(front.get("domains") or [])
        if domain not in domains:
            domains.append(domain)
            front["domains"] = domains
        write_atomic(raw_path, fm.serialize(front, body))

        nlm_registry.increment_sources(domain)

        log.append(
            op="nlm-add",
            fields={
                "id": source_id,
                "domain": domain,
                "notebook_id": notebook_id,
                "type": source_type,
            },
            summary=log_summary,
        )

    return OperationResult(
        success=True,
        paths_touched=[raw_path, nlm_registry.notebooks_yaml_path()],
        summary=f"added: {source_id} → {domain} ({notebook_id})",
    )


# --- nlm-sync --------------------------------------------------------------


def _iter_sources_for_domain(domain: str) -> list[tuple[str, Path, str]]:
    """Walk raw/ and return [(source_id, raw_path, source_type)] for every
    source whose frontmatter `domains:` list contains `domain`.

    Sorted by (source_type, source_id) so dry-run output is stable.
    """
    matches: list[tuple[str, Path, str]] = []
    for source_type in paths.SOURCE_TYPES:
        type_dir = paths.raw_dir_for(source_type)
        if not type_dir.is_dir():
            continue
        for raw_path in sorted(type_dir.glob("*.md")):
            try:
                front, _ = fm.parse(raw_path.read_text())
            except (OSError, fm.FrontmatterError):
                continue
            domains = front.get("domains") or []
            if not isinstance(domains, list):
                continue
            if domain in domains:
                matches.append((raw_path.stem, raw_path, source_type))
    matches.sort(key=lambda t: (t[2], t[0]))
    return matches


_ARXIV_ID_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")
_YT_ID_RE = re.compile(r"[?&]v=([A-Za-z0-9_-]{11})|youtu\.be/([A-Za-z0-9_-]{11})")


def _signatures_for(front: dict) -> list[str]:
    """Identifying substrings to look for in NotebookLM-side titles when
    deciding whether a raw source has already been loaded. arxiv and
    youtube are precise; everything else falls back to a long title prefix
    which is good enough for partial matches."""
    sigs: list[str] = []
    url = str(front.get("url") or "")
    if (m := _ARXIV_ID_RE.search(url)):
        sigs.append(m.group(1))
    if (m := _YT_ID_RE.search(url)):
        sigs.append(m.group(1) or m.group(2))
    title = str(front.get("title") or "").strip()
    if len(title) >= 16:
        sigs.append(title[:48])
    return [s for s in sigs if s]


def _reconcile_already_loaded(
    domain: str,
    notebook_id: str,
    sources: list[tuple[str, Path, str]],
    client: NlmClient,
) -> int:
    """For each raw source whose URL/title signature appears in the
    notebook's existing source list, add the notebook_id to its
    `nlm_corpus_ids` frontmatter so the main loop skips it. Returns the
    number reconciled. Best-effort: if we can't fetch the NotebookLM-side
    list, returns 0 and the main loop proceeds (which may create duplicates).
    """
    try:
        nlm_sources = client.notebook_sources(notebook_id)
    except NlmError:
        return 0
    nlm_blob = "\n".join(
        f"{s.get('title', '')} {s.get('url', '')}" for s in nlm_sources
    )
    if not nlm_blob.strip():
        return 0

    reconciled = 0
    for source_id, raw_path, _ in sources:
        try:
            front, body = fm.parse(raw_path.read_text())
        except (OSError, fm.FrontmatterError):
            continue
        if notebook_id in (front.get("nlm_corpus_ids") or []):
            continue
        sigs = _signatures_for(front)
        if not sigs or not any(sig in nlm_blob for sig in sigs):
            continue
        front["nlm_corpus_ids"] = list(front.get("nlm_corpus_ids") or []) + [notebook_id]
        domains = list(front.get("domains") or [])
        if domain not in domains:
            domains.append(domain)
            front["domains"] = domains
        write_atomic(raw_path, fm.serialize(front, body))
        nlm_registry.increment_sources(domain)
        reconciled += 1
    return reconciled


def nlm_sync(
    domain: str,
    *,
    dry_run: bool = False,
    limit: int | None = None,
    client: NlmClient | None = None,
    progress=None,
) -> OperationResult:
    """Sync every raw source tagged with `domain` into the domain's
    persistent NotebookLM notebook.

    Idempotent: each source is added only if its frontmatter doesn't
    already list the persistent notebook in `nlm_corpus_ids`. Resumable:
    a Ctrl+C mid-run leaves committed sources tagged so a re-run skips
    them. Per-source failures are collected and the loop continues so
    one bad source can't block the rest.

    `progress(idx, total, source_id, status, detail)` is called once per
    source if provided; the CLI uses this to print live output.
    """
    if not domain:
        return OperationResult(success=False, errors=["domain is required"])

    sources = _iter_sources_for_domain(domain)
    if not sources:
        return OperationResult(
            success=True,
            no_op=True,
            summary=f"no raw sources tagged with domain {domain!r}",
        )

    if limit is not None and limit > 0:
        sources = sources[:limit]

    if dry_run:
        lines = [f"would sync {len(sources)} source(s) to {domain!r}:"]
        for source_id, _, source_type in sources[:50]:
            lines.append(f"  {source_type}/{source_id}")
        if len(sources) > 50:
            lines.append(f"  ... and {len(sources) - 50} more")
        return OperationResult(success=True, summary="\n".join(lines))

    client = client or NlmCLIClient()

    # Reconcile against NotebookLM-side state first: sources whose URL/title
    # signature already appears in the notebook get their frontmatter updated
    # in-place so the main loop counts them as skipped (no duplicate adds).
    reconciled = 0
    notebook_id = nlm_registry.get_notebook_id(domain)
    if notebook_id:
        reconciled = _reconcile_already_loaded(domain, notebook_id, sources, client)

    added = 0
    skipped = 0
    failed: list[str] = []
    paths_touched: list[Path] = []

    for idx, (source_id, _raw_path, _source_type) in enumerate(sources, start=1):
        try:
            r = nlm_add(domain, source_id, client=client)
        except Exception as e:  # noqa: BLE001 — never let one source kill the run
            failed.append(f"{source_id}: {e}")
            if progress:
                progress(idx, len(sources), source_id, "failed", str(e))
            continue

        if not r.success:
            failed.append(f"{source_id}: {'; '.join(r.errors)}")
            if progress:
                progress(idx, len(sources), source_id, "failed", "; ".join(r.errors))
            continue

        if r.no_op:
            skipped += 1
            if progress:
                progress(idx, len(sources), source_id, "skipped", r.summary or "")
        else:
            added += 1
            if progress:
                progress(idx, len(sources), source_id, "added", r.summary or "")
            paths_touched.extend(r.paths_touched or [])

    summary_parts = [
        f"sync {domain}: {added} added",
        f"{skipped} already in corpus",
    ]
    if reconciled:
        summary_parts.append(f"{reconciled} reconciled (already in NotebookLM)")
    summary_parts.append(f"{len(failed)} failed")
    summary_parts.append(f"(out of {len(sources)} candidates)")
    summary = ", ".join(summary_parts[:-1]) + " " + summary_parts[-1]
    return OperationResult(
        success=len(failed) == 0,
        summary=summary,
        errors=failed,
        paths_touched=paths_touched,
    )


# --- nlm-slides / nlm-audio / nlm-briefing ---------------------------------


def _create_artifact(
    *,
    domain: str,
    topic: str,
    artifact_type: str,                 # "slides" | "audio" | "briefing"
    suffix: str,                        # filename suffix
    extension: str,                     # ".pdf" / ".m4a" / ".md"
    create_fn,                          # client method that creates
    download_fn,                        # client method that downloads
    client: NlmClient,
) -> OperationResult:
    notebook_id = nlm_registry.get_notebook_id(domain)
    if not notebook_id:
        return OperationResult(
            success=False,
            errors=[
                f"no notebook registered for domain {domain!r}; "
                f"add at least one source via `wiki nlm-add` first"
            ],
        )

    try:
        info: ArtifactInfo = create_fn(notebook_id)
    except NlmError as e:
        return OperationResult(success=False, errors=[f"create failed: {e}"])

    slug = _artifact_slug(topic, suffix=suffix)
    artifact_dir = paths.wiki_dir() / "artifacts" / artifact_type
    artifact_dir.mkdir(parents=True, exist_ok=True)
    local_file = artifact_dir / f"{slug}{extension}"

    # M37: poll artifact status before downloading. Audio can take 5+ min
    # to generate; slides 2-4 min; briefings sub-minute. Status values
    # observed in the wild: "in_progress", "completed", "unknown" (often
    # an early-state quirk that resolves to completed), "failed".
    poll_deadline = time.monotonic() + 600.0   # 10 min hard cap
    poll_delay = 10.0
    last_status = ""
    while time.monotonic() < poll_deadline:
        try:
            last_status = client.artifact_status(notebook_id, info.artifact_id or "")
        except NlmError:
            last_status = ""
        if last_status == "completed":
            break
        if last_status == "failed":
            return OperationResult(
                success=False,
                errors=[
                    f"{artifact_type} generation failed on NotebookLM "
                    f"(notebook={notebook_id} artifact={info.artifact_id})"
                ],
            )
        time.sleep(poll_delay)
        poll_delay = min(poll_delay * 1.5, 30.0)
    if last_status != "completed":
        return OperationResult(
            success=False,
            errors=[
                f"{artifact_type} did not reach 'completed' within 10min "
                f"(last status={last_status!r}, artifact={info.artifact_id})"
            ],
        )

    try:
        download_fn(notebook_id, local_file, artifact_id=info.artifact_id or None)
    except NlmError as e:
        return OperationResult(success=False, errors=[f"download failed: {e}"])

    page_path = artifact_dir / f"{slug}.md"
    artifact_page = _build_artifact_page(
        artifact_type=artifact_type,
        slug=slug,
        title=topic if artifact_type != "briefing" else f"{domain} briefing — {topic}",
        domain=domain,
        notebook_id=notebook_id,
        artifact_info=info,
        local_file=local_file,
        question=topic,
        sources_used=[],
    )
    write_atomic(page_path, artifact_page)
    nlm_registry.update_last_sync(domain)

    log.append(
        op=f"nlm-{artifact_type}",
        fields={
            "domain": domain,
            "notebook_id": notebook_id,
            "artifact_id": info.artifact_id or "?",
            "topic": topic,
        },
        summary=f"local={local_file.relative_to(paths.knowledge_root())} url={notebook_artifact_url(notebook_id, info.artifact_id)}",
    )

    return OperationResult(
        success=True,
        paths_touched=[local_file, page_path, paths.log_path()],
        summary=f"{artifact_type}: {slug} (notebook={notebook_id})",
    )


def nlm_slides(domain: str, topic: str, *, client: NlmClient | None = None) -> OperationResult:
    client = client or NlmCLIClient()
    return _create_artifact(
        domain=domain,
        topic=topic,
        artifact_type="slides",
        suffix="slides",
        extension=".pdf",
        create_fn=lambda nb: client.slides_create(nb, focus=topic),
        download_fn=client.download_slides,
        client=client,
    )


def nlm_audio(domain: str, topic: str, *, client: NlmClient | None = None) -> OperationResult:
    client = client or NlmCLIClient()
    return _create_artifact(
        domain=domain,
        topic=topic,
        artifact_type="audio",
        suffix="audio",
        extension=".m4a",
        create_fn=lambda nb: client.audio_create(nb, focus=topic),
        download_fn=client.download_audio,
        client=client,
    )


def nlm_briefing(domain: str, *, client: NlmClient | None = None) -> OperationResult:
    client = client or NlmCLIClient()
    return _create_artifact(
        domain=domain,
        topic=f"{domain} briefing doc",
        artifact_type="briefing",
        suffix="briefing",
        extension=".md",
        create_fn=lambda nb: client.report_create(nb, format="Briefing Doc"),
        download_fn=client.download_report,
        client=client,
    )


# --- nlm-revise -------------------------------------------------------------


_REVISION_RE = re.compile(r"^\s*(\d+)\s+(.+?)\s*$")


def _parse_revisions(instructions: list[str]) -> list[tuple[int, str]]:
    """Parse list of "<slide-num> <instruction>" strings into tuples."""
    out: list[tuple[int, str]] = []
    for raw in instructions:
        match = _REVISION_RE.match(raw)
        if not match:
            raise NlmError(f"could not parse revision {raw!r}; expected: '<slide-num> <instruction>'")
        out.append((int(match.group(1)), match.group(2)))
    return out


def nlm_revise(
    artifact_slug: str,
    instructions: list[str],
    *,
    client: NlmClient | None = None,
) -> OperationResult:
    """Revise an existing slide deck. Files the revised deck as a NEW wiki artifact page.

    `artifact_slug` is the slug of an existing wiki/artifacts/slides/<slug>.md
    page; we read its frontmatter to find the nlm_artifact_id.
    """
    client = client or NlmCLIClient()

    page_path = paths.wiki_dir() / "artifacts" / "slides" / f"{artifact_slug}.md"
    if not page_path.exists():
        return OperationResult(success=False, errors=[f"no slide artifact at {page_path}"])

    try:
        front, _ = fm.parse(page_path.read_text())
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"artifact frontmatter: {e}"])

    artifact_id = front.get("nlm_artifact_id")
    domain = front.get("domain")
    if not artifact_id or not domain:
        return OperationResult(
            success=False,
            errors=[
                f"artifact {artifact_slug} is missing nlm_artifact_id or domain; "
                "cannot revise (try regenerating from scratch)"
            ],
        )

    try:
        revisions = _parse_revisions(instructions)
    except NlmError as e:
        return OperationResult(success=False, errors=[str(e)])

    try:
        info = client.slides_revise(artifact_id, revisions)
    except NlmError as e:
        return OperationResult(success=False, errors=[f"revise failed: {e}"])

    notebook_id = nlm_registry.get_notebook_id(domain)
    if not notebook_id:
        return OperationResult(
            success=False,
            errors=[f"no notebook registered for domain {domain!r}"],
        )

    new_slug = _artifact_slug(
        f"{front.get('question', artifact_slug)} (rev)",
        suffix="slides-rev",
    )
    artifact_dir = paths.wiki_dir() / "artifacts" / "slides"
    new_local = artifact_dir / f"{new_slug}.pdf"
    try:
        client.download_slides(notebook_id, new_local, artifact_id=info.artifact_id or None)
    except NlmError as e:
        return OperationResult(success=False, errors=[f"download of revised deck failed: {e}"])

    new_page_path = artifact_dir / f"{new_slug}.md"
    new_page = _build_artifact_page(
        artifact_type="slides",
        slug=new_slug,
        title=f"{front.get('title', artifact_slug)} (revised)",
        domain=domain,
        notebook_id=notebook_id,
        artifact_info=info,
        local_file=new_local,
        question=f"Revision of {artifact_slug}: {'; '.join(instructions)}",
        sources_used=[],
    )
    write_atomic(new_page_path, new_page)

    log.append(
        op="nlm-revise",
        fields={
            "domain": domain,
            "original_artifact_slug": artifact_slug,
            "new_artifact_slug": new_slug,
            "revisions": len(revisions),
        },
        summary=f"local={new_local.relative_to(paths.knowledge_root())}",
    )

    return OperationResult(
        success=True,
        paths_touched=[new_local, new_page_path, paths.log_path()],
        summary=f"revised: {artifact_slug} → {new_slug}",
    )
