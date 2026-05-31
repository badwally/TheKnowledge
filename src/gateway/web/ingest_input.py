"""Validation for network-supplied ingest targets.

Product-readiness review (260530) finding #3: the web ingest endpoints
resolved any non-http(s) input as a local filesystem path and read it
server-side, letting an API caller exfiltrate arbitrary files the server
process can read (``/etc/passwd``, ``~/.ssh/*``, …) by ingesting them into
the wiki.

Over the HTTP API, ingest accepts ONLY:
  - an http(s) URL, or
  - a multipart file upload (handled separately in the cloud route, written
    to a server-controlled temp file).

Local filesystem paths are rejected. Operator-driven local-file ingest
remains available via the ``wiki ingest`` CLI, which is not network-exposed.
This helper is the single chokepoint both ingest routes call so the rule
cannot drift between them.
"""

from __future__ import annotations

from fastapi import HTTPException

_ALLOWED_SCHEMES = ("http://", "https://")


def validate_remote_url(raw: str) -> str:
    """Return ``raw`` if it is an http(s) URL; otherwise raise HTTPException(400).

    Validation is synchronous at request time so a rejected input returns a
    400 to the caller rather than failing inside a background task after a 202.
    """
    if isinstance(raw, str) and raw.startswith(_ALLOWED_SCHEMES):
        return raw
    raise HTTPException(
        status_code=400,
        detail=(
            "ingest over the API accepts only http(s) URLs or an uploaded "
            "file; local filesystem paths are not allowed. Use the `wiki "
            "ingest` CLI for local files."
        ),
    )
