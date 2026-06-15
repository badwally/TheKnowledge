# Session review — 2026-06-15 (force-include fix + cross-domain brief + slug cleanup)

Covers work **since `docs/260611_session-review.md`**: the `wiki ingest --force-include`
gateway feature (`82324776`), the comprehensive cross-domain brief (`a60efa9f`), and
its slug rename (`e3a701cc`). Excludes commits authored outside this conversation
(the `--domains` retrieval PR #15, the Adrienne entity fix, orita-cmo) — not this
session's work. Evidence is primarily the conversation's tool-call sequence.

---

## § 1 — Code and coding quality

**Medium — two iterations of over-broad string replacement in `src/gateway/ops/ingest.py`.**
The `force_include` threading was applied by blanket `.replace()` first (substring
`draft=draft,` matched across 8- and 12-space indents → doubled insertions →
`SyntaxError: keyword argument repeated`), then by line-anchored regex which *still*
matched `draft=draft,` inside the two `_invoke_plan_and_apply(...)` calls (which don't
take the kwarg → `TypeError`). Two failed passes of the same class before the
per-line-number deletion fixed it. Root cause: a file-wide mechanical edit over a
file with several near-identical call sites, without scoping to the five target
functions. Fix: edit per-function (or, after a multi-site mechanical edit, run an
`ast.parse` + import smoke *before* the full test suite — I had the syntax check but
only after the first failure). Caught by the regression run; no shipped defect.

**Positive (checked, clean):** the feature itself is well-built — `force_include`
threaded correctly through all five ingest functions, an auditable forced filter
block (`policy_version: force-include`, score 1.0), and a **strong RED test** that
asserts the filter client *raises if called* (proves bypass, not just outcome).
282 ingest/filter/batch/authorship tests green; the normal-ingest path is untouched.
Checked: signatures, call sites, the bypass branch, the `_invoke_plan_and_apply`
exclusion, test assertions.

---

## § 2 — Token efficiency

**High — ran `wiki answer --domains` twice, both truncating at §3.** The first call
truncated mid-§3 (output caps at ~3 dense sections). I then **re-ran it** with a
terse-7-section directive — which truncated at §3 *again* — before pivoting to
hand-authoring. The second expensive multi-domain LLM call (+ two `--abandon` ops)
was pure waste: the first truncation already established the output cap. Excess: ~1
large LLM call + 2 abandons. Lesson: one truncation is the signal; pivot, don't retry
the same tool expecting a different length.

**Medium — the slug round-trip.** The brief was filed via a *minimal-question*
scaffold (clean single `## Synthesis`, but an ugly `in-one-sentence-what-is-a` slug),
then cleaned up later as a separate rename + `wiki index --rebuild` (~34s) + commit.
Picking a clean declarative scaffold question up front — or fixing the slug before
finalize — would have saved an entire commit and the full index rebuild. Excess: ~3
calls + a commit + a 34s rebuild.

**Medium — fragmented reads of `ingest.py`.** Read across ~6 separate `sed`/grep
Bash calls (imports, dispatcher, `ingest_file`, core 215–375, 375–470, `_run_filter`,
141–216). Two wider section reads would have sufficed. Excess: ~4 calls.

---

## § 3 — Prompt and context engineering

**High — repeat validator failure I had already solved this session.** `wiki finalize`
rejected the cross-domain brief on uncited meta-sentences (the intro framing + a
closing flourish). This is the **exact** failure I hit and documented on the
policy/market synthesis page earlier in this same session (synthesis bodies: every
sentence needs a `[[sources/]]` or must be a question/heading). The lesson wasn't
carried forward two pages later — I authored an uncited intro + flourish again,
forcing a re-edit + re-finalize. Fix: apply the known rule at authoring time, not
after the validator rejects.

**High — still one continuous session, now spanning 2026-06-10 → 06-15.** The #1
finding of the *last* review was "run long work as fresh-session iterations" — a rule
I then wrote into CLAUDE.md and a memory. It was **not applied to this very session**,
which has run five days across the foundation, fixes, the brief, and cleanup in one
swelling window. The `contp` skill (built this session for exactly this handoff) went
unused until the user invoked it. The rule exists; the behavior didn't change.

**Medium — output-length cap not anticipated.** The `wiki answer --domains` question
was well-formed, but I didn't pre-account for the ~3-section output ceiling; knowing
it would have routed straight to hand-authoring (with `--domains` retrieval as the
grounding harvester), skipping both truncated calls.

**Positive:** the brief's cross-domain content is strong and the user's new `--domains`
retrieval was used well; surface-anchor discipline held (foundation stayed neutral,
condo specifics confined to the brief); the `force-include` RED test design (assert
the dependency is *not* called) is exemplary.

---

## Priority (impact ÷ effort)

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | §3 Context | Still one 5-day session; the fresh-session rule (from last review) went unapplied; `contp` unused | Actually `/clear` at seams and resume via `contp` — stop running multi-day work in one window |
| 2 | §3 Prompt | Re-hit the "every synthesis sentence cited or is a question" validator rule already learned this session | Apply it at authoring time; pre-cite intro + reframe ledgers as questions before finalize |
| 3 | §2 Token | Re-ran `wiki answer --domains` after the first truncation; both wasted | Treat one truncation as the signal; pivot to hand-author; know the ~3-section output cap |
| 4 | §1/§2 Code | Two over-broad string-replace passes before the kwarg threading worked | Scope multi-site edits per-function; `ast.parse`+import smoke before the full suite |
| 5 | §2 Token | Minimal-scaffold slug forced a rename + index-rebuild round-trip | Use a clean declarative scaffold question (or fix slug pre-finalize) |

**One-line POV:** the substantive output (the feature, the brief) was strong, but the
session keeps re-paying for two known, already-documented lessons — *don't run
everything in one endless window*, and *every synthesis sentence must be grounded* —
both of which I'd written down earlier in this very session and then didn't apply.
The cheapest win is behavioral, not technical: honor the fresh-session rule.
