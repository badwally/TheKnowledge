# Backlog: Unsanitized Lock-Name → Path Interpolation in `file_lock`

**Category:** Gateway / Locking primitive
**Priority:** Low (pre-existing; latent path-traversal)
**Effort:** ~1-2 hours (the fix is small; the cost is sweeping the 30+ call sites)
**Trigger to action:** The next edit to any `file_lock(...)` call site that interpolates user/external input into the lock name (e.g. `ingest-{source_id}`, `schedule-{job.name}`, `concept-add-{slug}`), OR a dedicated lock-hardening pass. "Next touched" applies because Phase 4 already added the `timeout` keyword to this primitive.

---

## Problem

`locking.file_lock(name)` builds `locks / f"{name}.lock"` with **no sanitization**
(`locking.py`). Several call sites interpolate IDs / slugs / job-names into the name:
`ingest-{source_id}` (`ops/ingest.py:257`), `schedule-{job.name}` (`scheduler.py:213`),
`concept-add-{slug}` (`ops/concept_add.py:101`), `moc-add-{slug}`, `migrate-{domain_slug}`,
and others. A `source_id` / `slug` / `job.name` containing `../` would write a `.lock`
file **outside** `.knowledge/locks/`.

`is_known_lock_name()` (`locking.py:55-67`) validates a name surface but is explicitly
**not enforced** at the `file_lock` call site (its own docstring says so). So the guard
exists but does nothing today.

Surfaced by the Phase-4 independent security review (2026-06-19, Finding 3, Low). It
**predates Phase 4** — the Phase-4 diff only added the `timeout` keyword and introduced
no new user-input-to-name path (the `librarian-commit` name is a constant). Flagged
because it is a latent path-traversal in the locking primitive the Librarian builds on,
and it is the same class as the Phase-1 scoped-recovery path-traversal the security
review caught then.

## Proposed Solution

In `file_lock`, reject a `name` containing `/`, `..`, or absolute-path markers (raise
`ValueError`), OR turn on `is_known_lock_name()` enforcement at the call site. The
former is lower-risk (it does not require enumerating every legitimate name) but must
be validated against the existing per-resource prefix names that legitimately contain
`-` and `.` (e.g. `ingest-arxiv-2403.12345`). Sweep the 30+ call sites to confirm no
legitimate name trips the new guard.

## Acceptance criteria

- [ ] `file_lock("../../etc/evil")` (and absolute paths) raise rather than write outside `.knowledge/locks/`.
- [ ] Every existing legitimate lock name (incl. dotted IDs like `ingest-arxiv-2403.12345`) still acquires.
- [ ] Adversarial test: a lock name with `..` cannot create a file outside the locks dir (sentinel-file check, mirror the Phase-1 path-traversal test).
