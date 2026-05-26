# gateway.pollers

Pollers serve API-only sources that cannot be expressed as a single URL or local file — sources where content is fetched incrementally via a vendor API (Apple Notes, Readwise, GitHub repo metadata). A poller's sole job is to write canonical markdown files to `raw/<type>/`; it does not call the ingest pipeline directly. The watcher (`gateway.watcher`) or a manual `wiki ingest <path>` picks up from there, giving pollers the same downstream guarantee as converters. Cursor state (last-synced timestamp or ID) lives at `.knowledge/pollers/<name>/cursor.yaml` so re-runs only fetch new items.

See `ARCHITECTURE.md` for how pollers relate to converters and the watcher.

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Registry: `get_poller(name)`, `list_pollers()`, `UnknownPollerError` |
| `base.py` | `Poller` ABC: `run()`, `read_cursor()`, `write_cursor()`, `write_raw()`; `PollerResult` dataclass |
| `apple_notes.py` | `AppleNotesPoller` — fetches from local Apple Notes via AppleScript |
| `readwise.py` | `ReadwisePoller` — fetches highlights from the Readwise v3 API |
| `repo_metadata.py` | `RepoMetadataPoller` — fetches GitHub repo metadata for tracked repos |

## Adding a new poller (5-step contract)

1. Subclass `Poller` from `base.py`. Set the `name` class attribute (this becomes the registry key and the cursor directory name) and `source_type` (one of `paths.SOURCE_TYPES`).
2. Implement `run() -> PollerResult`: call `self.read_cursor()` to get the last-sync state, fetch new items from the vendor API, call `self.write_raw(canonical_id, canonical_text)` for each item, then call `self.write_cursor({...})` with updated state. Return a `PollerResult` with `fetched` and `skipped` counts.
3. Register the class in `pollers/__init__._REGISTRY`: add `MyPoller.name: MyPoller` to the dict and import the class at the top of `__init__.py`.
4. If the poller should run on a schedule or respond to an event, add a subscription YAML at `.knowledge/agents/<name>.yaml` with the trigger and interval.
5. Write tests at `tests/gateway/test_pollers_<name>.py`. Mock the vendor API; assert that `write_raw` is called with correctly-formed canonical markdown and that the cursor is updated.

### You're done when:

- [ ] `pytest tests/gateway/test_pollers_<name>.py` passes with mocked API
- [ ] `wiki poll <name>` runs without error on a live account (manual smoke test)
- [ ] `wiki lint` reports no new errors after a run that produces items

## Worked example: running the Apple Notes poller

```
Input:  $ wiki poll apple-notes
Call chain:
1. cli.py → ops/status.py or direct poller dispatch
2. pollers.get_poller("apple-notes") → AppleNotesPoller()
3. poller.run() is called
4. poller.read_cursor() → {"last_modified": "2026-05-20T10:00:00Z"}
5. AppleScript fetches notes modified after cursor timestamp
6. For each new note:
   a. Build canonical_id: e.g. "apple-note-20260525-my-note-title"
   b. Build canonical markdown with id, type="note", title, body
   c. poller.write_raw(canonical_id, text)
      → writes raw/note/apple-note-20260525-my-note-title.md
7. poller.write_cursor({"last_modified": "2026-05-25T09:00:00Z"})
   → writes .knowledge/pollers/apple-notes/cursor.yaml
8. Returns PollerResult(success=True, fetched=3, skipped=0)

Failure modes:
- AppleScript permission denied → PollerResult(success=False, errors=["osascript: ..."])
- Note body fails frontmatter schema → write_raw succeeds but downstream
  validator rejects at ingest time; poller itself does not validate
- Cursor file corrupt → read_cursor() returns {} (safe fallback, full re-fetch)
```
