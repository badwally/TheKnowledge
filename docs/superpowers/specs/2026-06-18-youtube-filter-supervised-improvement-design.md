# YouTube filter/prompt supervised-improvement exercise — design

**Date:** 2026-06-18
**Status:** Design approved; spec under review
**Domain:** `semantic-models`

---

## 1. Goal

Raise the **precision of YouTube source selection** — both the queries that surface
candidates and the semantic filter that accepts them — for the `semantic-models`
domain, using a human-labeled gold set as ground truth. Produce a reusable gold
set and a measurable before/after precision figure.

## 2. Non-goals (explicit)

This exercise targets source *selection* only. It does **not** address:

- **NLM under-attribution** — the dominant cause of the 2026-06-18 17/25 draft
  abandonment was NotebookLM generating `### Specifics` prose with no inline
  citations. A better filter cannot fix NLM's citation behavior.
- **Transcript IP-throttle** — a separate infra constraint on transcript fetches.
- **Resurrecting the 17 abandoned drafts.**

Reduced abandonment is a plausible *secondary* benefit (a more on-topic, higher-quality
corpus grounds better), not the headline claim.

## 3. Background & the key mechanic

The 17/25 abandonment was multi-causal; the filter/prompts were a contributing, not
dominant, factor. This exercise is still warranted: it improves a real, measurable
lever and yields a gold set the system currently lacks.

**The filter scores pre-fetch metadata** (title / channel / description), not the
transcript ([[feedback_filter_source_type_awareness]]). So a human "best-fit"
judgment — made by actually watching/assessing the videos — is exactly the gold
signal for the question *"can metadata predict content quality?"*

Disagreements between the human gold and the filter split into **two separately
fixable levers**:

- **Filter lever** — a good video *is* in the candidate pool but the filter ranks
  it low (false negative), or a weak video ranks high (false positive). Fix:
  `policy.yaml` inclusion/exclusion criteria + quality signals
  (`channel_authority` / `speaker_expertise`) + `wiki filter-correct` examples.
- **Query/prompt lever** — a good video is *not in the pool at all* because no query
  surfaced it (coverage gap). Fix: the `query_planner` YouTube register / prompt
  wording.

precision@k measures the filter lever only (ranking within the pool it was given);
the query lever is captured via human "expected-but-missing" flags (§6).

## 4. Mechanism (verified)

- `wiki research --review` returns at `orchestrator.py:1167`, persisting only the
  **query plan** (the emitted `youtube:` queries) — *before* fan-out and filter. It
  gives the prompting half but no scored candidates.
- To obtain a scored candidate pool **without materialization**, a small read-only
  harness calls the search + filter-scoring stages directly
  (`_fan_out_search` → per-candidate filter scoring). It performs **no transcript
  fetch** and **no writes to `raw/` or `wiki/`** — so the transcript IP-throttle does
  not block it, and no gateway hard rule is touched. The harness writes only scratch
  artifacts under `docs/` (or a tmp path).
- Whether the harness is a throwaway script or a promoted `wiki` subcommand is an
  implementation decision (YAGNI: start as a script; promote if the loop recurs).

## 5. Prompt set

I author **12 research prompts** spanning `semantic-models` subtopics (e.g. KG
construction, query languages/engines, reasoning/inference, SHACL/shape validation,
storage architectures, KG embeddings, ontology engineering methodologies, ontology
design patterns, alignment/matching, upper/foundational ontologies, the semantic
layer, OBDA, foundational formalisms). Split **8 train / 4 validate** (validate held
out from all tuning).

For each prompt, the planner's emitted `youtube:` queries are captured for the
prompting-lever analysis.

## 6. Candidate pool & labeling

- The harness runs the train prompts' YouTube queries → **dedups into one candidate
  pool (~50 items)** → scores each via the semantic filter. It emits two artifacts:
  - **(a) Blind pool (for the user):** title / channel / URL / description,
    **no scores**, **grouped by subtopic/prompt** (not one flat shuffled list), so
    the user can assess per-subtopic coverage. Order within a subtopic is shuffled.
  - **(b) Scored pool (for analysis):** each candidate's filter score + tier
    (accept / review / reject).
- **User labeling (train):**
  1. Pick the **10 best-fit videos overall** from the blind pool (global, across
     subtopics).
  2. Per subtopic, flag any **"expected but missing"** items — talks/channels the
     user would expect for that subtopic that are absent from the pool
     (query-coverage gaps). Optional per subtopic: "coverage looks complete" is a
     valid answer.

## 7. Analysis

- **precision@10** = |user's 10 ∩ filter's top-10| / 10 (filter top-10 = the 10
  highest-scored pool items).
- Disagreements bucketed:
  - **Filter false-positives** — in the filter's top-10, not in the user's 10.
  - **Filter false-negatives** — in the user's 10, ranked outside the filter's top-10.
  - **Query-coverage gaps** — the user's per-subtopic "missing" flags.

## 8. Improvement (derive + apply)

- Filter false-positives → `wiki filter-correct --exclude` (negative examples) +
  tighten `exclusion_criteria` / negative quality signals.
- Filter false-negatives → `wiki filter-correct --include` (positive examples) +
  strengthen `inclusion_criteria` / positive quality signals.
- Query-coverage gaps → revise the `query_planner` YouTube register (institution /
  conference / researcher-anchored query templates) and/or prompt wording.

All changes land via PR (gateway-authored; `policy.yaml` edits where no gateway op
exists are minimal and reviewed).

## 9. Validation (held-out)

Run the **4 validate prompts** through the harness with improvements applied → the
user does a lighter judgment on the new filter top-k → report **precision@10 before
vs after on data not used for tuning**. This guards against overfitting to the 10
train labels.

## 10. Deliverables

- Gold set (user labels + missing-flags) saved under `docs/` (e.g.
  `docs/research/youtube-filter-sl/`).
- `policy.yaml` + example-bank + `query_planner` changes (PR).
- A short results write-up: precision@10 train, precision@10 validate before/after,
  the disagreement buckets, and which lever each fix addressed.

## 11. Preconditions

- **YouTube adapter key idle** — no concurrent live research session (the harness
  hits YouTube *search* on our key). Transcript fetch is not invoked, so the
  IP-throttle does not block; but search-side rate limits still apply, so do not run
  concurrently with another adapter-hitting session
  ([[feedback_s2_shared_key_concurrency]] is the analogous lesson).
- Use `.venv/bin/python` / `.venv/bin/wiki` only.

## 12. Risks

- **Small gold set (10 labels):** mitigated by the held-out validate round; claims
  stay qualitative ("precision moved from X→Y on held-out") not statistical.
- **YouTube search nondeterminism:** controlled by the shared-pool protocol (user
  labels the exact pool the harness produced; no independent re-run).
- **Overfitting the filter to one domain:** changes to `query_planner` register are
  reviewed for cross-domain effect; `semantic-models` policy/example changes are
  domain-scoped by construction.
