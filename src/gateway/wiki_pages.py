"""Wiki page type schemas and section requirements per WIKI § 4.

Seven page types live under wiki/:
- entity          (wiki/entities/<slug>.md)
- concept         (wiki/concepts/<slug>.md)
- source          (wiki/sources/<id>.md)
- synthesis       (wiki/synthesis/<slug>.md)
- moc             (wiki/mocs/<slug>.md)
- artifact        (wiki/artifacts/<type>/<slug>.md)
- domain-proposal (wiki/proposals/<slug>.md)  [M36 — bottom-up domain discovery]

Each has a required-fields/required-sections schema. The validator
(M6) enforces these on every wiki write.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class PageTypeSchema:
    type_name: str
    directory: str
    required_fields: tuple[str, ...]
    required_sections: tuple[str, ...]
    citation_grounded: bool       # if True, body claims must cite [[sources/...]]


PAGE_SCHEMAS: dict[str, PageTypeSchema] = {
    "entity": PageTypeSchema(
        type_name="entity",
        directory="wiki/entities",
        required_fields=("type", "slug", "canonical_name", "entity_kind", "domains", "created_at", "last_updated"),
        required_sections=("Summary", "Key facts", "Sources", "Related"),
        citation_grounded=True,
    ),
    "concept": PageTypeSchema(
        type_name="concept",
        directory="wiki/concepts",
        required_fields=("type", "slug", "canonical_name", "domains", "created_at", "last_updated"),
        required_sections=("Summary", "Key claims", "Sources", "Related"),
        citation_grounded=True,
    ),
    "source": PageTypeSchema(
        type_name="source",
        directory="wiki/sources",
        required_fields=("type", "source_id", "source_type", "title", "ingested_at"),
        required_sections=("Summary", "Key claims", "Cross-references"),
        citation_grounded=True,
    ),
    "synthesis": PageTypeSchema(
        type_name="synthesis",
        directory="wiki/synthesis",
        required_fields=("type", "slug", "title", "domains", "question", "created_at", "last_updated", "sources_count"),
        required_sections=("Synthesis", "Sources cited"),
        citation_grounded=True,
    ),
    "moc": PageTypeSchema(
        type_name="moc",
        directory="wiki/mocs",
        required_fields=("type", "slug", "domain"),
        required_sections=("Overview", "Key entities", "Key concepts", "Synthesis pages"),
        citation_grounded=False,
    ),
    "artifact": PageTypeSchema(
        type_name="artifact",
        directory="wiki/artifacts",
        required_fields=(
            "type",
            "artifact_type",
            "slug",
            "title",
            "domain",
            "nlm_notebook_id",
            "nlm_artifact_url",
            "local_file",
        ),
        required_sections=("Local file", "NotebookLM (live, editable)", "Sources used"),
        citation_grounded=False,
    ),
    "domain-proposal": PageTypeSchema(
        type_name="domain-proposal",
        directory="wiki/proposals",
        required_fields=(
            "type",
            "slug",
            "title",
            "proposed_domain",
            "status",
            "member_sources",
            "rationale",
        ),
        required_sections=("Rationale", "Member sources"),
        citation_grounded=False,
    ),
    "contradiction": PageTypeSchema(
        type_name="contradiction",
        directory="wiki/contradictions",
        required_fields=("type", "slug", "parties", "severity", "status"),
        required_sections=("Summary",),
        citation_grounded=False,
    ),
}


_SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def is_valid_slug(slug: str) -> bool:
    return bool(_SLUG_RE.match(slug))


def levenshtein(a: str, b: str) -> int:
    """Classic Levenshtein distance — used for slug-similarity warnings."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr = [i] + [0] * len(b)
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            curr[j] = min(curr[j - 1] + 1, prev[j] + 1, prev[j - 1] + cost)
        prev = curr
    return prev[-1]


def page_type_for_path(rel_path: Path | str) -> str | None:
    """Infer the wiki page type from a wiki-relative path. Returns None if
    the path doesn't point at a known page type directory.
    """
    p = Path(rel_path).as_posix()
    for type_name, schema in PAGE_SCHEMAS.items():
        prefix = schema.directory + "/"
        if p.startswith(prefix):
            return type_name
    return None


def schema_for_type(type_name: str) -> PageTypeSchema | None:
    return PAGE_SCHEMAS.get(type_name)


_SECTION_HEADER_RE = re.compile(r"^\s*##\s+(.+?)\s*$", re.MULTILINE)


def section_headers(body: str) -> list[str]:
    """Return all `## Section` titles in body order."""
    return [m.group(1).strip() for m in _SECTION_HEADER_RE.finditer(body)]


def missing_sections(body: str, required: tuple[str, ...]) -> list[str]:
    headers_lower = {h.lower() for h in section_headers(body)}
    return [s for s in required if s.lower() not in headers_lower]
