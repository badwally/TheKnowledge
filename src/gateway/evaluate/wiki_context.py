"""Wiki context loader for the M50 judge (Phase B).

For a given domain, assembles into one prompt-ready string:
1. All synthesis pages whose `domains:` includes the target domain (full body).
2. Concept and entity pages tagged with the domain (truncated to the first
   N lines each to keep total context bounded).
3. Raw source bodies for each `synthesizes:` entry of those synthesis pages
   (the `sources/<id>` prefix is stripped before resolving to `raw/<type>/<id>.md`).

Each block is wrapped in XML-style tags (`<page>...</page>`, `<source>...</source>`)
to harden against prompt injection — same convention M49 cite_suggest established.

Bounded by `max_chars` — raises `ContextTooLargeError` so callers can surface
the actionable error (split goldens by sub-topic, or upgrade to retrieval
augmented context).
"""

from __future__ import annotations

from pathlib import Path

from gateway import frontmatter as fm
from gateway import paths


class ContextTooLargeError(RuntimeError):
    """Assembled context exceeds the LLM-prompt budget."""


_DEFAULT_MAX_CHARS = 750_000
_DEFAULT_MAX_SOURCE_BODY_CHARS = 30_000


def _strip_sources_prefix(source_id: str) -> str:
    """Strip the `sources/` prefix from `synthesizes:` / `sources:` entries.
    Same normalization M49 cite_suggest established (commit f1c27f2)."""
    if source_id.startswith("sources/"):
        return source_id[len("sources/"):]
    return source_id


def load_wiki_context(domain: str, *,
                      max_chars: int = _DEFAULT_MAX_CHARS,
                      max_source_body_chars: int = _DEFAULT_MAX_SOURCE_BODY_CHARS) -> str:
    """Assemble the wiki context block for `domain`.

    ``max_source_body_chars`` caps individual raw source bodies; bodies exceeding
    this limit are silently skipped so large PDFs / statutory texts don't consume
    the entire context budget.
    """
    kb_root = paths.knowledge_root()

    syntheses = _collect_pages(kb_root / "wiki" / "synthesis", domain)
    concepts = _collect_pages(kb_root / "wiki" / "concepts", domain)
    entities = _collect_pages(kb_root / "wiki" / "entities", domain)

    source_ids = _collect_source_ids(syntheses)
    source_bodies = _read_source_bodies(kb_root, source_ids,
                                        max_body_chars=max_source_body_chars)

    sections: list[str] = []
    if syntheses:
        sections.append("## Synthesis pages\n\n" + _render_pages(syntheses))
    if concepts:
        sections.append("## Concept pages\n\n" + _render_pages(concepts, head_lines=20))
    if entities:
        sections.append("## Entity pages\n\n" + _render_pages(entities, head_lines=15))
    if source_bodies:
        sections.append("## Source bodies\n\n" + _render_sources(source_bodies))

    ctx = "\n\n".join(sections)
    if len(ctx) > max_chars:
        raise ContextTooLargeError(
            f"wiki context for domain {domain!r} is {len(ctx)} chars, "
            f"exceeds budget {max_chars}. Consider splitting goldens by "
            f"sub-topic or upgrading to retrieval-augmented context."
        )
    return ctx


def _collect_pages(directory: Path, domain: str) -> list[tuple[Path, dict, str]]:
    out: list[tuple[Path, dict, str]] = []
    if not directory.exists():
        return out
    for p in sorted(directory.glob("*.md")):
        try:
            front, body = fm.parse(p.read_text())
        except fm.FrontmatterError:
            continue
        if domain in (front.get("domains") or []):
            out.append((p, front, body))
    return out


def _collect_source_ids(syntheses: list[tuple[Path, dict, str]]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for _, front, _ in syntheses:
        for entry in front.get("synthesizes") or []:
            sid = _strip_sources_prefix(str(entry))
            if sid not in seen:
                seen.add(sid)
                out.append(sid)
    return out


def _read_source_bodies(kb_root: Path, source_ids: list[str], *,
                        max_body_chars: int = _DEFAULT_MAX_SOURCE_BODY_CHARS) -> dict[str, str]:
    bodies: dict[str, str] = {}
    for sid in source_ids:
        for st in paths.SOURCE_TYPES:
            candidate = kb_root / "raw" / st / f"{sid}.md"
            if candidate.exists():
                try:
                    _, body = fm.parse(candidate.read_text())
                    if len(body) <= max_body_chars:
                        bodies[sid] = body
                except fm.FrontmatterError:
                    pass
                break
    return bodies


def _render_pages(pages: list[tuple[Path, dict, str]],
                  head_lines: int | None = None) -> str:
    parts = []
    for p, front, body in pages:
        rel = p.relative_to(paths.knowledge_root())
        slug = front.get("slug", p.stem)
        if head_lines is not None:
            body = "\n".join(body.splitlines()[:head_lines])
        parts.append(f"<page slug={slug!r} path={str(rel)!r}>\n{body}\n</page>")
    return "\n\n".join(parts)


def _render_sources(bodies: dict[str, str]) -> str:
    parts = []
    for sid, body in bodies.items():
        parts.append(f"<source id={sid!r}>\n{body}\n</source>")
    return "\n\n".join(parts)
