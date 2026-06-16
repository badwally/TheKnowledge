"""Load background-agent secrets from `.knowledge/secrets.env`.

launchd agents (the `watch` and `schedule run` daemons) start from a minimal
environment — they do NOT inherit the interactive shell, so secrets exported
in a shell profile (`FIRECRAWL_API_KEY`, `WIKI_WEB_SCRAPER`, …) are invisible
to them. `load_secrets_env` bridges that gap: it reads a gitignored env file
once at process start and applies each entry with `os.environ.setdefault`, so a
real environment variable always wins over the file.

Call it at the CLI entrypoint (`cli.main`); every subcommand — interactive
ingest and the background daemons alike — then sees the same secrets.
"""

import os
from pathlib import Path

from . import paths


def _parse_line(line: str) -> tuple[str, str] | None:
    """Parse one `KEY=value` line. Returns None for blanks, comments, and
    lines without an `=`. Strips an optional leading `export ` and matching
    surrounding quotes on the value."""
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    if stripped.startswith("export "):
        stripped = stripped[len("export ") :].lstrip()
    if "=" not in stripped:
        return None
    key, value = stripped.split("=", 1)
    key = key.strip()
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        value = value[1:-1]
    if not key:
        return None
    return key, value


def load_secrets_env(path: Path | None = None) -> dict[str, str]:
    """Populate `os.environ` from `path` (default `.knowledge/secrets.env`).

    Returns the mapping of keys actually applied — i.e. those not already set
    in the environment. A missing file is a silent no-op (returns ``{}``).
    """
    if path is None:
        path = paths.knowledge_internal() / "secrets.env"
    if not path.exists():
        return {}

    applied: dict[str, str] = {}
    for line in path.read_text().splitlines():
        parsed = _parse_line(line)
        if parsed is None:
            continue
        key, value = parsed
        if not value:
            # An empty value (`KEY=` or `KEY=""`) is treated as "not provided":
            # writing it would let an empty FIRECRAWL_API_KEY win over no-key and
            # suppress the trafilatura fallback. Omit the line to unset, not blank.
            continue
        if key in os.environ:
            continue
        os.environ[key] = value
        applied[key] = value
    return applied
