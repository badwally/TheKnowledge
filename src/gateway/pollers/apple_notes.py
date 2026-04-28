"""Apple Notes poller (proof-of-pattern stub).

A real implementation would call `osascript` against AppleScript to enumerate
notes modified since the last cursor and write each as canonical markdown.
This v1 ships the structural skeleton — `run()` can be invoked but performs
no AppleScript calls; integration is a follow-up.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib

from gateway import frontmatter as fm
from gateway import validator
from gateway.pollers.base import Poller, PollerResult


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slug_for(remote_id: str) -> str:
    digest = hashlib.sha256(remote_id.encode("utf-8")).hexdigest()[:8]
    return f"note-apple-{digest}"


class AppleNotesPoller(Poller):
    """Iterates Apple Notes via AppleScript when wired up.

    The poller framework's contract: read cursor → fetch new items → write
    each into `raw/note/`. The watcher picks them up. New items only — the
    cursor records `last_modified_iso` so re-runs are cheap.
    """

    name = "apple-notes"
    source_type = "note"

    def fetch_notes_since(self, cursor: str | None) -> list[dict]:
        """Return a list of {id, title, body, modified_at, folder} dicts.

        The default implementation returns an empty list; subclasses (or a
        future real implementation) shell out to AppleScript here.
        """
        return []

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
            remote_id = str(note.get("id") or "")
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
