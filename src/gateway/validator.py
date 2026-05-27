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
    "podcast",
    "note",
    "csv",
    "docx",
    "xlsx",
    "pptx",
    "image",
    "other",
}

REQUIRED_CORE_FIELDS: set[str] = {
    "id",
    "type",
    "title",
    "ingested_at",
    "content_hash",
}

# ONT-3: controlled vocabularies for contradiction wiki pages.
CONTRADICTION_SEVERITY_ENUM: frozenset[str] = frozenset({"major", "minor", "methodological"})
CONTRADICTION_STATUS_ENUM: frozenset[str] = frozenset({"open", "investigating", "resolved", "wontfix"})

# ONT-4: controlled vocabulary for entity_kind on entity wiki pages.
ENTITY_KIND_ENUM: frozenset[str] = frozenset({
    "person",
    "organization",
    "paper",
    "drug",
    "dataset",
    "product",
    "software",
    "statute",
    "standard",
    "place",
    "event",
    "other",
})

ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "youtube": re.compile(r"^yt-[A-Za-z0-9_-]+$"),
    "arxiv": re.compile(r"^arxiv-\d{4}\.\d{4,5}(v\d+)?$"),
    "pubmed": re.compile(r"^pubmed-\d+$"),
    "pdf": re.compile(r"^pdf-[a-z0-9-]+$"),
    "web": re.compile(r"^web-\d{4}-\d{2}-\d{2}-[a-z0-9]+$"),
    "voice": re.compile(r"^voice-\d{4}-\d{2}-\d{2}T\d{4}$"),
    "audiobook": re.compile(r"^audio-[a-z0-9-]+$"),
    "podcast": re.compile(r"^podcast-[a-z0-9-]+$"),
    "note": re.compile(r"^note-[a-z0-9-]+-[A-Za-z0-9_-]+$"),
    "csv": re.compile(r"^csv-[a-f0-9]{12}$"),
    "docx": re.compile(r"^docx-[a-z0-9-]+$"),
    "xlsx": re.compile(r"^xlsx-[a-z0-9-]+$"),
    "pptx": re.compile(r"^pptx-[a-z0-9-]+$"),
    "image": re.compile(r"^image-\d{4}-\d{2}-\d{2}-[a-f0-9]{12}$"),
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


CURRENT_SCHEMA_VERSION: int = 1


def validate_source_frontmatter(front: dict) -> ValidationResult:
    """Check required core fields, type enum, ID format, and schema_version."""
    result = ValidationResult()

    if "schema_version" not in front:
        result.warnings.append(
            ValidationError(
                "schema-version",
                f"missing schema_version; expected {CURRENT_SCHEMA_VERSION} — "
                "re-ingest or touch via gateway to stamp automatically",
                "schema_version",
            )
        )

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


# Keys that pipeline stages may update after ingest (§ 11.5).
MUTABLE_SOURCE_FIELDS: frozenset[str] = frozenset(
    {
        "filter",
        "nlm_corpus_ids",
        "wiki_pages",
        "domains",
        "contested",
        # QUAL-7: retraction / revision monitoring
        "retracted",
        "retracted_at",
        "arxiv_revised",
        "arxiv_current_version",
        "arxiv_baseline_version",
        # QUAL-14: supersedence linking
        "superseded_by",
        "supersedes",
    }
)


def validate_source_frontmatter_diff(old: dict, new: dict) -> ValidationResult:
    """Reject mutations to source frontmatter keys outside MUTABLE_SOURCE_FIELDS.

    Compares old and new frontmatter dicts. Any key whose value changed —
    including keys added or removed — is flagged unless it is in the
    pipeline-stage allowlist defined by § 11.5.
    """
    result = ValidationResult()
    all_keys = set(old) | set(new)
    for key in sorted(all_keys):
        if old.get(key) != new.get(key) and key not in MUTABLE_SOURCE_FIELDS:
            result.errors.append(
                ValidationError(
                    "frontmatter-mutation",
                    f"field {key!r} may not be mutated after ingest; "
                    f"only {sorted(MUTABLE_SOURCE_FIELDS)} are mutable",
                    key,
                )
            )
    return result


# === M6: wiki page validation =============================================

from gateway import citations as _citations  # noqa: E402  (kept here so M1 module is self-contained above)
from gateway import wiki_pages as _wiki_pages  # noqa: E402


_MAX_SLUG_LEN = 80  # ONT-8: hard limit on new slug length
_TIMESTAMP_PAGE_TYPES = frozenset({"entity", "concept", "synthesis"})  # ONT-6


def validate_wiki_page_frontmatter(
    front: dict,
    page_type: str,
    *,
    force_long_slug: bool = False,
) -> ValidationResult:
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

    # ONT-8: new slugs longer than 80 chars are rejected. --force-long-slug
    # downgrades to a warning for exceptional cases.
    if slug is not None and len(str(slug)) > _MAX_SLUG_LEN:
        msg = (
            f"slug is {len(str(slug))} chars (max {_MAX_SLUG_LEN}); "
            "use --force-long-slug to override"
        )
        if force_long_slug:
            result.warnings.append(ValidationError("slug-too-long", msg, "slug"))
        else:
            result.errors.append(ValidationError("slug-too-long", msg, "slug"))

    # ONT-4: entity_kind must be a known enum value on entity pages.
    if schema.type_name == "entity":
        entity_kind = front.get("entity_kind")
        if entity_kind is not None and entity_kind not in ENTITY_KIND_ENUM:
            result.errors.append(
                ValidationError(
                    "entity-kind-unknown",
                    f"entity_kind {entity_kind!r} is not in the controlled vocabulary; "
                    f"expected one of: {', '.join(sorted(ENTITY_KIND_ENUM))}",
                    "entity_kind",
                )
            )
        # ONT-5: paper entities require canonical_source
        if entity_kind == "paper" and not front.get("canonical_source"):
            result.warnings.append(
                ValidationError(
                    "paper-missing-canonical-source",
                    "entity_kind: paper requires canonical_source pointing to an ingested source ID; "
                    "add canonical_source: <source-id> (e.g. arxiv-2401-12345 or pdf-lastname2024)",
                    "canonical_source",
                )
            )

    # ONT-7: confidence field must be one of the 3-tier GRADE values
    confidence = front.get("confidence")
    if confidence is not None:
        _CONFIDENCE_TIERS = frozenset({"established", "tentative", "speculative"})
        if str(confidence).lower() not in _CONFIDENCE_TIERS:
            result.errors.append(
                ValidationError(
                    "confidence-invalid",
                    f"confidence {confidence!r} is not a valid tier; "
                    "expected: established | tentative | speculative",
                    "confidence",
                )
            )

    # ONT-6: timestamp format for entity/concept/synthesis
    if schema.type_name in _TIMESTAMP_PAGE_TYPES:
        result.merge(validate_timestamps(front))

    return result


def validate_timestamps(front: dict) -> ValidationResult:
    """ONT-6: verify created_at and last_updated are parseable ISO-8601."""
    result = ValidationResult()
    for field in ("created_at", "last_updated"):
        value = front.get(field)
        if value is None:
            continue
        if not isinstance(value, str):
            result.errors.append(
                ValidationError(
                    "timestamp-format",
                    f"{field} must be a string, got {type(value).__name__}",
                    field,
                )
            )
            continue
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            result.errors.append(
                ValidationError(
                    "timestamp-format",
                    f"{field} {value!r} is not parseable as ISO-8601",
                    field,
                )
            )
    return result


def validate_contradiction_frontmatter(front: dict) -> ValidationResult:
    """ONT-3: validate contradiction-specific frontmatter fields."""
    result = ValidationResult()
    severity = front.get("severity")
    status = front.get("status")
    parties = front.get("parties")

    if not parties:
        result.errors.append(
            ValidationError(
                "contradiction-parties-missing",
                "contradiction page requires at least one entry in 'parties'",
                "parties",
            )
        )

    if severity is not None and severity not in CONTRADICTION_SEVERITY_ENUM:
        result.errors.append(
            ValidationError(
                "contradiction-severity-unknown",
                f"severity {severity!r} is not valid; expected one of: {', '.join(sorted(CONTRADICTION_SEVERITY_ENUM))}",
                "severity",
            )
        )

    if status is not None and status not in CONTRADICTION_STATUS_ENUM:
        result.errors.append(
            ValidationError(
                "contradiction-status-unknown",
                f"status {status!r} is not valid; expected one of: {', '.join(sorted(CONTRADICTION_STATUS_ENUM))}",
                "status",
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
    front: dict | None = None,
    body_line_offset: int = 0,
) -> ValidationResult:
    """Per § 5.2: every claim sentence in entity / concept / source / synthesis
    pages must be followed by a `[[sources/<id>]]` citation.

    Draft mode (`--draft` ingest, `draft: true` frontmatter) downgrades the
    rule from rejection to a warning so partial work can be committed.

    M45: when `front` carries `synthesizes:` (≥2 entries) and `body` has
    `## Included works` mirroring that list, the first claim-shaped line
    of each `## ` section that matches the aggregate-framing opener
    allowlist is exempted (handled inside `_citations.uncited_claims`).

    K1 / D2: `body_line_offset` (default 0) is added to each reported
    line number so messages can be file-relative (matching `wiki cite`'s
    convention). Callers compute it via `frontmatter.body_line_offset`
    when they have the original text. Default 0 keeps pre-K1 callers
    (lint pass-throughs, tests) emitting body-relative lines without
    change.
    """
    result = ValidationResult()
    schema = _wiki_pages.schema_for_type(page_type)
    if schema is None or not schema.citation_grounded:
        return result

    uncited = _citations.uncited_claims(body, front)
    if not uncited:
        return result

    for c in uncited:
        ve = ValidationError(
            "citation-grounding",
            f"line {c.line_no + body_line_offset}: claim has no citation: {c.text[:120]}",
        )
        if draft:
            result.warnings.append(ve)
        else:
            result.errors.append(ve)
    return result


def validate_synthesizes_integrity(front: dict, body: str) -> ValidationResult:
    """M45: when `synthesizes:` is present on a page, verify its shape.

    Checks:
    - every entry matches `(sources|synthesis)/<slug>` format
    - all entries are same tier (one-level strict typing; M45 § 3.6 inv. 1)
    - `## Included works` section exists and mirrors the list 1:1

    Does NOT verify on-disk existence — that's a `wiki lint --scope
    citation-chains` concern (cross-page integrity, not in-page shape).
    """
    result = ValidationResult()
    synth = front.get("synthesizes") if isinstance(front, dict) else None
    if synth is None:
        return result
    if not isinstance(synth, list):
        result.errors.append(
            ValidationError(
                "synthesizes-shape",
                f"`synthesizes:` must be a list, got {type(synth).__name__}",
                "synthesizes",
            )
        )
        return result
    if len(synth) == 0:
        return result  # empty list is no-op; treat as if field absent

    bad_entries = [
        e for e in synth
        if not isinstance(e, str) or not _citations._SYNTHESIZES_ENTRY_RE.match(e)
    ]
    if bad_entries:
        result.errors.append(
            ValidationError(
                "synthesizes-shape",
                f"`synthesizes:` entries must be `sources/<slug>` or `synthesis/<slug>`; "
                f"invalid: {bad_entries[:3]!r}",
                "synthesizes",
            )
        )
        return result

    tiers = {e.split("/", 1)[0] for e in synth}
    if len(tiers) != 1:
        result.errors.append(
            ValidationError(
                "synthesizes-mixed-tier",
                f"`synthesizes:` must be all `sources/` or all `synthesis/`, "
                f"never mixed (got both: {sorted(tiers)})",
                "synthesizes",
            )
        )
        return result

    if not _citations._included_works_mirrors_synthesizes(body, synth):
        result.errors.append(
            ValidationError(
                "synthesizes-included-works-drift",
                "`## Included works` section is missing or its wikilinks "
                "do not mirror the `synthesizes:` frontmatter list 1:1",
                "synthesizes",
            )
        )
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


def validate_citation_verbs(body: str) -> ValidationResult:
    """ONT-2: warn when an aliased [[sources/<id>|verb]] uses an unknown CiTO verb.

    Known verbs are in `citations._CITO_VERBS`. Plain [[sources/<id>]] (no alias)
    is never flagged — this check is purely additive.
    """
    result = ValidationResult()
    for m in _citations._ALIASED_SOURCE_RE.finditer(body):
        verb = m.group(1).strip()
        if verb and verb not in _citations._CITO_VERBS:
            result.warnings.append(
                ValidationError(
                    "citation-verb-unknown",
                    f"unknown citation verb '{verb}'; "
                    f"expected one of: {', '.join(sorted(_citations._CITO_VERBS))}",
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
    force_long_slug: bool = False,
    body_line_offset: int = 0,
) -> ValidationResult:
    """One-shot validation of a wiki page: frontmatter + sections + citations + slug.

    K1 / D2: ``body_line_offset`` (default 0) propagates to citation-grounding
    so reported line numbers can be file-relative when the caller has the
    original text. Compute via ``frontmatter.body_line_offset(text)``.
    """
    result = ValidationResult()
    result.merge(validate_wiki_page_frontmatter(front, page_type, force_long_slug=force_long_slug))
    result.merge(validate_wiki_page_sections(body, page_type))

    # ONT-3: contradiction-specific validation
    if page_type == "contradiction":
        result.merge(validate_contradiction_frontmatter(front))

    # Honor `draft: true` in frontmatter OR an explicit caller flag. To force
    # strict mode (e.g., during finalize), strip the draft fields from front
    # before calling.
    is_draft = draft or bool(front.get("draft"))
    result.merge(
        validate_citation_grounding(
            body,
            page_type,
            draft=is_draft,
            front=front,
            body_line_offset=body_line_offset,
        )
    )
    result.merge(validate_synthesizes_integrity(front, body))
    result.merge(validate_citation_verbs(body))

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
