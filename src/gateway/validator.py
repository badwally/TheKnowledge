"""Validator rules per WIKI.md § 11.

M1 subset:
- Required core frontmatter fields (§ 11.1).
- Source ID format per type (§ 6.1).
- Type in allowed enum.
- ingested_at parseable as ISO-8601.
- content_hash matches body (§ 11.1).
- Well-formed wikilinks: balanced brackets (cheap subset of § 11.2).
- Source immutability when re-ingesting (§ 11.5).

Deferred:
- Full citation grounding rule with draft-mode downgrade (M6).
- Bidirectional backlink integrity (M6).
- Slug Levenshtein similarity (M6).
- Wikilink target resolution (M6, when there are targets to resolve against).
"""

from dataclasses import dataclass, field
from datetime import datetime
import hashlib
import re

ALLOWED_SOURCE_TYPES: set[str] = {
    "youtube",
    "arxiv",
    "pubmed",
    "pdf",
    "web",
    "voice",
    "audiobook",
    "note",
    "csv",
    "docx",
    "xlsx",
    "other",
}

REQUIRED_CORE_FIELDS: set[str] = {
    "id",
    "type",
    "title",
    "ingested_at",
    "content_hash",
}

ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "youtube": re.compile(r"^yt-[A-Za-z0-9_-]+$"),
    "arxiv": re.compile(r"^arxiv-\d{4}\.\d{4,5}(v\d+)?$"),
    "pubmed": re.compile(r"^pubmed-\d+$"),
    "pdf": re.compile(r"^pdf-[a-z0-9-]+$"),
    "web": re.compile(r"^web-\d{4}-\d{2}-\d{2}-[a-z0-9]+$"),
    "voice": re.compile(r"^voice-\d{4}-\d{2}-\d{2}T\d{4}$"),
    "audiobook": re.compile(r"^audio-[a-z0-9-]+$"),
    "note": re.compile(r"^note-[a-z0-9-]+-[A-Za-z0-9_-]+$"),
    "csv": re.compile(r"^csv-[a-f0-9]{12}$"),
    "docx": re.compile(r"^docx-[a-z0-9-]+$"),
    "xlsx": re.compile(r"^xlsx-[a-z0-9-]+$"),
    "other": re.compile(r"^.+$"),
}


@dataclass
class ValidationError:
    rule: str
    message: str
    field_name: str | None = None

    def __str__(self) -> str:
        prefix = f"[{self.rule}]"
        if self.field_name:
            prefix += f" {self.field_name}:"
        return f"{prefix} {self.message}"


@dataclass
class ValidationResult:
    errors: list[ValidationError] = field(default_factory=list)
    warnings: list[ValidationError] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def merge(self, other: "ValidationResult") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


def compute_content_hash(body: str) -> str:
    """Canonical content hash format: 'sha256:<64-hex>'."""
    h = hashlib.sha256(body.encode("utf-8")).hexdigest()
    return f"sha256:{h}"


def validate_source_frontmatter(front: dict) -> ValidationResult:
    """Check required core fields, type enum, and ID format."""
    result = ValidationResult()

    missing = REQUIRED_CORE_FIELDS - front.keys()
    for f in sorted(missing):
        result.errors.append(
            ValidationError("required-field", f"missing required field: {f}", f)
        )

    type_ = front.get("type")
    if type_ is not None and type_ not in ALLOWED_SOURCE_TYPES:
        result.errors.append(
            ValidationError(
                "type-enum",
                f"type {type_!r} not in allowed enum {sorted(ALLOWED_SOURCE_TYPES)}",
                "type",
            )
        )

    id_ = front.get("id")
    if id_ is not None and isinstance(type_, str) and type_ in ID_PATTERNS:
        pattern = ID_PATTERNS[type_]
        if not pattern.match(str(id_)):
            result.errors.append(
                ValidationError(
                    "id-format",
                    f"id {id_!r} does not match expected pattern for type {type_!r} ({pattern.pattern})",
                    "id",
                )
            )

    ts = front.get("ingested_at")
    if ts is not None:
        if isinstance(ts, datetime):
            pass  # already a datetime
        elif isinstance(ts, str):
            try:
                datetime.fromisoformat(ts.replace("Z", "+00:00"))
            except ValueError:
                result.errors.append(
                    ValidationError(
                        "ingested-at-format",
                        f"ingested_at {ts!r} is not parseable as ISO-8601",
                        "ingested_at",
                    )
                )
        else:
            result.errors.append(
                ValidationError(
                    "ingested-at-format",
                    f"ingested_at must be a string or datetime, got {type(ts).__name__}",
                    "ingested_at",
                )
            )

    return result


def validate_content_hash(front: dict, body: str) -> ValidationResult:
    """Confirm the declared content_hash matches the body."""
    result = ValidationResult()
    declared = front.get("content_hash")
    if declared is None:
        return result  # required-field already reported

    actual = compute_content_hash(body)
    if declared != actual:
        result.errors.append(
            ValidationError(
                "content-hash-mismatch",
                f"declared content_hash {declared!r} != computed {actual!r}",
                "content_hash",
            )
        )
    return result


_WIKILINK_OPEN = "[["
_WIKILINK_CLOSE = "]]"


def validate_wikilinks(text: str) -> ValidationResult:
    """Cheap balanced-brackets check.

    Resolution checking (do targets exist?) lands in M6 once there are
    populated wiki/ subdirectories to resolve against.
    """
    result = ValidationResult()
    open_count = text.count(_WIKILINK_OPEN)
    close_count = text.count(_WIKILINK_CLOSE)
    if open_count != close_count:
        result.errors.append(
            ValidationError(
                "wikilink-malformed",
                f"unbalanced wikilink brackets: {open_count} '[[' vs {close_count} ']]'",
            )
        )
    return result


def validate_source_immutability(existing_body: str, new_body: str) -> ValidationResult:
    """A source body must not change after first ingest (§ 11.5).

    Frontmatter mutations are allowed (filter score, nlm_corpus_ids, wiki_pages,
    domains) — those are checked by separate rules. Body changes are not.
    """
    result = ValidationResult()
    if existing_body != new_body:
        result.errors.append(
            ValidationError(
                "source-immutability",
                "source body has changed since previous ingest; "
                "sources in raw/ are immutable after creation",
            )
        )
    return result


# === M6: wiki page validation =============================================

from gateway import citations as _citations  # noqa: E402  (kept here so M1 module is self-contained above)
from gateway import wiki_pages as _wiki_pages  # noqa: E402


def validate_wiki_page_frontmatter(front: dict, page_type: str) -> ValidationResult:
    """Verify required fields per § 4 page type schema."""
    result = ValidationResult()
    schema = _wiki_pages.schema_for_type(page_type)
    if schema is None:
        result.errors.append(
            ValidationError(
                "wiki-page-type-unknown",
                f"unknown wiki page type {page_type!r}; expected one of "
                f"{sorted(_wiki_pages.PAGE_SCHEMAS)}",
                "type",
            )
        )
        return result

    declared_type = front.get("type")
    if declared_type != schema.type_name:
        result.errors.append(
            ValidationError(
                "wiki-page-type-mismatch",
                f"frontmatter type {declared_type!r} does not match expected {schema.type_name!r}",
                "type",
            )
        )

    for field_name in schema.required_fields:
        if front.get(field_name) in (None, "", []):
            result.errors.append(
                ValidationError(
                    "wiki-page-required-field",
                    f"missing required field for {schema.type_name} page: {field_name}",
                    field_name,
                )
            )

    slug = front.get("slug")
    if slug is not None and not _wiki_pages.is_valid_slug(str(slug)):
        result.errors.append(
            ValidationError(
                "wiki-page-slug-format",
                f"slug {slug!r} must be lowercase letters/digits/hyphens, no leading hyphen",
                "slug",
            )
        )

    return result


def validate_wiki_page_sections(body: str, page_type: str) -> ValidationResult:
    """Verify the page contains every required section header."""
    result = ValidationResult()
    schema = _wiki_pages.schema_for_type(page_type)
    if schema is None:
        return result

    missing = _wiki_pages.missing_sections(body, schema.required_sections)
    for s in missing:
        result.errors.append(
            ValidationError(
                "wiki-page-section-missing",
                f"{schema.type_name} page is missing required section: '## {s}'",
            )
        )
    return result


def validate_citation_grounding(
    body: str,
    page_type: str,
    *,
    draft: bool = False,
) -> ValidationResult:
    """Per § 5.2: every claim sentence in entity / concept / source / synthesis
    pages must be followed by a `[[sources/<id>]]` citation.

    Draft mode (`--draft` ingest, `draft: true` frontmatter) downgrades the
    rule from rejection to a warning so partial work can be committed.
    """
    result = ValidationResult()
    schema = _wiki_pages.schema_for_type(page_type)
    if schema is None or not schema.citation_grounded:
        return result

    uncited = _citations.uncited_claims(body)
    if not uncited:
        return result

    for c in uncited:
        ve = ValidationError(
            "citation-grounding",
            f"line {c.line_no}: claim has no citation: {c.text[:120]}",
        )
        if draft:
            result.warnings.append(ve)
        else:
            result.errors.append(ve)
    return result


_SLUG_SIMILARITY_THRESHOLD = 2  # Levenshtein distance


def validate_slug_uniqueness(
    new_slug: str,
    existing_slugs: list[str],
    *,
    force_new: bool = False,
) -> ValidationResult:
    """Reject exact-duplicate slugs; warn on near-duplicates (Levenshtein ≤ 2).

    `force_new=True` (the `--force-new-slug` flag) downgrades near-duplicate
    rejection so users can intentionally introduce a similar slug.
    """
    result = ValidationResult()
    if new_slug in existing_slugs:
        result.errors.append(
            ValidationError(
                "wiki-page-slug-duplicate",
                f"slug {new_slug!r} already exists",
                "slug",
            )
        )
        return result

    similar = [
        s
        for s in existing_slugs
        if 0 < _wiki_pages.levenshtein(new_slug, s) <= _SLUG_SIMILARITY_THRESHOLD
    ]
    if similar and not force_new:
        result.warnings.append(
            ValidationError(
                "wiki-page-slug-similar",
                f"slug {new_slug!r} is near-duplicate of: {', '.join(similar)} "
                f"(use --force-new-slug to override)",
                "slug",
            )
        )
    return result


def validate_wiki_page(
    front: dict,
    body: str,
    page_type: str,
    *,
    draft: bool = False,
    existing_slugs: list[str] | None = None,
    force_new_slug: bool = False,
) -> ValidationResult:
    """One-shot validation of a wiki page: frontmatter + sections + citations + slug."""
    result = ValidationResult()
    result.merge(validate_wiki_page_frontmatter(front, page_type))
    result.merge(validate_wiki_page_sections(body, page_type))

    # Honor `draft: true` in frontmatter OR an explicit caller flag. To force
    # strict mode (e.g., during finalize), strip the draft fields from front
    # before calling.
    is_draft = draft or bool(front.get("draft"))
    result.merge(validate_citation_grounding(body, page_type, draft=is_draft))

    slug = front.get("slug")
    if slug and existing_slugs is not None:
        result.merge(
            validate_slug_uniqueness(
                str(slug),
                [s for s in existing_slugs if s != slug],
                force_new=force_new_slug,
            )
        )

    return result
