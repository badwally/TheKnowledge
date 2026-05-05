"""Apple Notes poller via JXA (JavaScript for Automation) over `osascript`.

Enumerates all notes across every account in Notes.app, filters by the
cursor's `last_modified_iso`, strips the HTML body to plain text, and
writes each new/updated note as canonical markdown into `raw/note/`. The
watcher (M4) or `wiki ingest` picks up from there.

macOS only. The first run prompts macOS for Automation access to Notes;
re-runs are silent. Cursor state lives at
`.knowledge/pollers/apple-notes/cursor.yaml`.

The Apple Notes `body` is HTML; we strip tags via a minimal stdlib
parser (no extra deps). Heading / paragraph / list-item tags become
newlines so the resulting text preserves structural breaks.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser

from gateway import frontmatter as fm
from gateway import validator
from gateway.pollers.base import Poller, PollerResult


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slug_for(remote_id: str) -> str:
    digest = hashlib.sha256(remote_id.encode("utf-8")).hexdigest()[:8]
    return f"note-apple-{digest}"


# JXA script: enumerate all notes, return JSON. UTC ISO datetimes for
# `modified` so Python can compare lexicographically against the cursor.
_JXA_SCRIPT = r"""
ObjC.import('Foundation');
const Notes = Application('Notes');
Notes.includeStandardAdditions = false;

const formatter = $.NSDateFormatter.alloc.init;
formatter.setDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
formatter.setTimeZone($.NSTimeZone.timeZoneWithAbbreviation('UTC'));

const out = [];
const allNotes = Notes.notes();
const n = allNotes.length;
for (let i = 0; i < n; i++) {
    const note = allNotes[i];
    let folderName = '';
    try {
        const c = note.container();
        if (c) folderName = c.name();
    } catch (e) { /* note may have no container */ }
    out.push({
        id: note.id(),
        title: note.name(),
        folder: folderName,
        modified: formatter.stringFromDate(note.modificationDate()),
        body: note.body(),
    });
}
JSON.stringify(out);
""".strip()


class _HTMLToText(HTMLParser):
    """Minimal HTML → plain-text stripper (no external deps).

    Block-level tags (p, div, h1-6, li) emit newlines so the output
    preserves visual structure. Inline tags collapse to their text.
    """

    BLOCK_OPEN = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6"}
    BLOCK_BREAK = {"br", "li", "tr"}
    BLOCK_CLOSE = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li"}

    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self._parts.append(data)

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in self.BLOCK_OPEN or tag in self.BLOCK_BREAK:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.BLOCK_CLOSE:
            self._parts.append("\n")

    def get_text(self) -> str:
        text = "".join(self._parts)
        # Collapse runs of whitespace within lines, drop empty lines
        cleaned = "\n".join(line.strip() for line in text.split("\n") if line.strip())
        return cleaned


def _strip_html(html: str) -> str:
    parser = _HTMLToText()
    parser.feed(html or "")
    parser.close()
    return parser.get_text()


def _run_osascript(script: str, timeout_s: float = 60.0) -> str:
    """Run a JXA script via osascript and return stdout. Raises on failure.

    Monkeypatched in tests so no actual osascript invocation occurs.
    """
    try:
        result = subprocess.run(
            ["osascript", "-l", "JavaScript"],
            input=script,
            capture_output=True,
            text=True,
            timeout=timeout_s,
            check=False,
        )
    except FileNotFoundError as e:
        raise RuntimeError("osascript not available; this poller requires macOS") from e
    except subprocess.TimeoutExpired as e:
        raise RuntimeError(f"osascript timed out after {timeout_s}s") from e
    if result.returncode != 0:
        raise RuntimeError(
            f"osascript exited {result.returncode}: {result.stderr.strip()[:300]}"
        )
    return result.stdout


class AppleNotesPoller(Poller):
    """Real-implementation Apple Notes poller (macOS).

    Reads cursor → enumerate all notes via JXA → filter to those modified
    after the cursor → strip HTML body → write canonical markdown into
    `raw/note/`. Updates cursor to the latest modification timestamp seen.
    """

    name = "apple-notes"
    source_type = "note"

    def fetch_notes_since(self, cursor: str | None) -> list[dict]:
        """Return list of {id, title, body, modified_at, folder} for notes
        whose modification timestamp is strictly greater than `cursor`.

        `cursor` is an ISO-8601 UTC timestamp string (or None for first run).
        Comparison is lexicographic on the normalized ISO format.
        """
        raw = _run_osascript(_JXA_SCRIPT)
        if not raw.strip():
            return []
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"could not parse JXA output as JSON: {e}") from e
        if not isinstance(payload, list):
            raise RuntimeError(f"expected JSON array from JXA, got {type(payload).__name__}")

        out: list[dict] = []
        for item in payload:
            if not isinstance(item, dict):
                continue
            modified = str(item.get("modified") or "")
            if cursor and modified <= cursor:
                continue
            body_html = str(item.get("body") or "")
            out.append({
                "id": str(item.get("id") or ""),
                "title": str(item.get("title") or ""),
                "folder": str(item.get("folder") or ""),
                "modified_at": modified,
                "body": _strip_html(body_html),
            })
        return out

    def run(self) -> PollerResult:
        cursor_data = self.read_cursor()
        last = cursor_data.get("last_modified_iso")
        try:
            notes = self.fetch_notes_since(last)
        except Exception as e:
            return PollerResult(success=False, errors=[f"fetch failed: {e}"])

        fetched = 0
        skipped = 0
        latest_modified = last
        for note in notes:
            remote_id = note.get("id") or ""
            body = (note.get("body") or "").strip()
            if not remote_id or not body:
                skipped += 1
                continue
            body = body + "\n"
            slug = _slug_for(remote_id)
            front = {
                "id": slug,
                "type": "note",
                "title": note.get("title") or remote_id,
                "url": "",
                "authors": [],
                "ingested_at": _now_iso(),
                "content_hash": validator.compute_content_hash(body),
                "domains": [],
                "nlm_corpus_ids": [],
                "wiki_pages": [],
                "meta": {
                    "source_app": "apple-notes",
                    "source_id": remote_id,
                    "folder": note.get("folder", ""),
                    "modified_at": note.get("modified_at", ""),
                },
            }
            self.write_raw(slug, fm.serialize(front, body))
            fetched += 1
            modified = note.get("modified_at") or ""
            if not latest_modified or modified > latest_modified:
                latest_modified = modified

        if latest_modified and latest_modified != last:
            self.write_cursor({"last_modified_iso": latest_modified})

        return PollerResult(
            success=True,
            fetched=fetched,
            skipped=skipped,
            summary=f"apple-notes: fetched={fetched} skipped={skipped}",
        )
