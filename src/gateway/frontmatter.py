"""YAML frontmatter parser and serializer.

A canonical document is `---\\n<yaml>\\n---\\n<body>`. Both parts are required
and well-defined. Frontmatter must be a YAML mapping.
"""

from typing import Tuple

import yaml

DELIM = "---"


class FrontmatterError(ValueError):
    """Raised when frontmatter is missing, malformed, or not a mapping."""


def body_line_offset(text: str) -> int:
    """Return the file-line offset of the first body line in `text`.

    Used by validators to translate body-relative line numbers (what
    `_citations.uncited_claims()` emits) into file-relative ones so error
    messages match `wiki cite`'s file-line numbering convention.

    Returns 0 when `text` has no recognizable frontmatter (the validator
    then degrades silently to body-relative lines, preserving pre-K1
    behavior for callers that don't have the original text).
    """
    if not text.startswith(DELIM):
        return 0
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i] == DELIM:
            # body starts at lines[i + 1]; file-line of body-line 1 is i + 2.
            # The "offset" we add to a body-line is i + 1.
            return i + 1
    return 0


def parse(text: str) -> Tuple[dict, str]:
    """Split a markdown document into (frontmatter dict, body string).

    The body excludes the closing delimiter line and the leading newline
    that follows it. Trailing newlines in the body are preserved verbatim.
    """
    if not text.startswith(DELIM):
        raise FrontmatterError("missing frontmatter (no leading '---')")

    lines = text.split("\n")
    if lines[0] != DELIM:
        raise FrontmatterError("opening '---' must be on its own line")

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i] == DELIM:
            end_idx = i
            break

    if end_idx is None:
        raise FrontmatterError("missing closing '---' delimiter")

    yaml_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1:])

    try:
        front = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        raise FrontmatterError(f"invalid YAML in frontmatter: {e}") from e

    if front is None:
        front = {}
    if not isinstance(front, dict):
        raise FrontmatterError(
            f"frontmatter must be a YAML mapping, got {type(front).__name__}"
        )

    return front, body


def serialize(front: dict, body: str) -> str:
    """Combine frontmatter + body back into a markdown document.

    Body is written verbatim. A single newline separates the closing
    delimiter from the body.
    """
    yaml_text = yaml.safe_dump(
        front,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
    ).rstrip("\n")
    return f"---\n{yaml_text}\n---\n{body}"
