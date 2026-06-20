# End-to-end challenge cases

**Filed:** 2026-06-20

Ten adversarial, full-pipeline scenarios for challenging the knowledge gateway end to
end. Each crosses multiple subsystems, drives the **real** producer (not a fabricated
fixture for the data a detector/consumer reads), and names the failure mode it exists to
catch. Run them by hand or scaffold into `tests/e2e/` as RED-first pytest.

**Cardinal rule (from the inert-in-production hunt list, `docs/MULTI-AGENT-BUILD-PLAYBOOK.md`):**
drive the real producer — real `wiki_deposit`, real `commit-worker`, real lint registry,
real corpus — never a stub standing in for the data the consumer reads. That substitution
is what made past green tests lie.

---

## E2E-1 — Ingest → filter → convert → wiki page (the spine)

- **Challenges:** converter detect/convert, two-pass filter, `raw/` immutability, watcher /
  `wiki ingest` pickup, source-page authoring.
- **Setup:** a real URL with full-text HTML and a known sparse counterpart (a PubMed
  abstract stub).
- **Action:** `wiki ingest <url> --domain X --with-plan`, then `wiki ingest <abstract-url> --domain X`.
- **Pass:** rich source lands in `raw/<type>/` + a `wiki/sources/<id>.md` summary with
  `[[sources/<id>]]` grounding; sparse source is filtered out (or accepted only via
  `--force-include`). `raw/` body is byte-identical to ingest after later pipeline stages
  touch frontmatter.
- **Catches:** filter source-type blindness (YouTube/abstract under-representation), silent
  convert-failure-as-success, frontmatter writes mutating immutable body.

## E2E-2 — Citation grounding gate is not bypassable

- **Challenges:** validator hard-rule #3, `--draft` downgrade, `wiki finalize`.
- **Setup:** author a synthesis page with one cited claim and one deliberately uncited
  claim sentence.
- **Action:** attempt commit non-draft; then `--draft`; then `wiki finalize`.
- **Pass:** non-draft is **rejected** for the uncited claim; draft commits with `draft:true`
  (lint warning, not error); `finalize` fails until the claim is cited. No path lets an
  uncited claim reach a finalized page.
- **Catches:** the recurring confabulation / under-attribution failure — a finalize path
  that backstops uncited lines (the YouTube-corpus wall).

## E2E-3 — Cross-domain retrieval quota balancing

- **Challenges:** `wiki retrieve --domains a,b`, FTS5/BM25 + graph authority, per-domain
  round-robin quota.
- **Setup:** two domains where one is lexically dominant (many keyword-dense pages) and one
  sparse but relevant.
- **Action:** `wiki retrieve "<question spanning both>" --domains a,b --k 10`.
- **Pass:** the context block contains ≥ `ceil(k/N)` sections from the minority domain (not
  collapsed to the dominant one); every section retains its `[[sources/<id>]]`.
- **Catches:** the single-global-k-window collapse toward the lexically-dominant domain that
  `--domains` exists to fix.

## E2E-4 — Retrieval recall floor under content growth

- **Challenges:** index self-heal (mtime/size), golden eval, the pre-merge gate's recall floor.
- **Setup:** baseline golden set (recall@10 0.926).
- **Action:** ingest 20+ new sources across existing domains, `wiki index --rebuild`, then
  `wiki eval-retrieval --compare`.
- **Pass:** recall@10 ≥ 0.90 and no MRR regression vs. baseline; the derived index rebuilt
  from canonical markdown matches a cold rebuild.
- **Catches:** ranking regressions hidden by additive content; derived-state drift from
  canonical.

## E2E-5 — Concurrent same-slug deposits: union, never overwrite

- **Challenges:** async `wiki_deposit` → `wiki commit-worker`, MVCC CAS, `_union_same_slug`,
  fencing.
- **Setup:** two agents deposit different bullet content targeting the **same** slug; one
  carries a stale base.
- **Action:** submit both, run `wiki commit-worker --once` (or concurrent drainers).
- **Pass:** the committed page is the **union** of both bullet sets (no lost write); a
  non-bullet structural collision **dead-letters** `needs-manual-merge` (fail-safe), never a
  silent overwrite. Stale-fenced intent is rejected / retry-later, intent stays durable.
- **Catches:** silent same-slug overwrite; a serialized "race" that never actually contends
  (the P3 plan defect).

## E2E-6 — Phantom-base contradictory write dead-letters

- **Challenges:** CommitGate CAS case-3, dead-letter routing, repo non-mutation on reject.
- **Setup:** author intent with `base_oid=None` for a path that HEAD already has.
- **Action:** commit.
- **Pass:** `disposition == "dead_lettered"`, repo tree unchanged, no partial write; a genuine
  fresh-path write (negative control) commits cleanly with an `Intent-Id` trailer.
- **Catches:** corruption from blind-overwrite on a contradictory base; a gate that fails open.

## E2E-7 — Dedup adjudication on the hard cases

- **Challenges:** deterministic `dedup.adjudicate` (I1), alias/canonical authority, embeddings
  recall-only, cross-kind-never-merge.
- **Setup:** deposit `Ozempic` then `Semaglutide` (brand↔generic alias); separately
  `Type 1 diabetes` and `Type 2 diabetes` (shared surface, distinct referents); and an entity
  vs. a concept of similar name.
- **Action:** drive each through the commit path.
- **Pass:** brand/generic **merge** (alias authority) with a `merged_into:` tombstone + alias
  union + body carried; shared-prefix siblings stay **distinct**; cross-kind never merges.
  Decision is replayable from logged inputs (no model call in the held lock).
- **Catches:** geometry-only false merges/splits the lexical-fallback encoder gets backwards;
  non-determinism in the keystone.

## E2E-8 — Lint registry integrity + cold-start resilience

- **Challenges:** every `--scope` emits under its registered slug; lint runs on a bare repo.
- **Setup:** (a) a repo with one real triggering signal per check; (b) a repo missing `raw/` /
  `wiki/` entirely.
- **Action:** `wiki lint --scope <each>`; then run all checks on the bare repo.
- **Pass:** every finding's `check` equals the `--scope` slug it was requested under (the
  `f.check == slug` tripwire); no check raises on missing directories (the
  `superseded_citations` cold-start guard). Report summary counts and detail section headers
  agree.
- **Catches:** slug-mismatch silent-empty consumers (the `citation-chains` / `long-slugs`
  defects); cold-start `FileNotFoundError`; summary/detail keying drift.

## E2E-9 — NotebookLM synthesis refuses to confabulate on a sparse corpus

- **Challenges:** `wiki research --execute` preconditions, `corpus_quality` gate,
  `index_settle` check.
- **Setup:** a candidate corpus that is majority PubMed abstracts / paywall stubs
  (median < 300 words, > 60% sparse).
- **Action:** run the research pipeline to execute.
- **Pass:** the `corpus_quality` step **blocks** the run (or it surfaces `distinct_sources: 1–2`
  at `index_settle` and halts) rather than generating a confident synthesis attributed to the
  single richest source.
- **Catches:** the corpus-quality confabulation trap — NLM filling from training data and
  mis-attributing provenance.

## E2E-10 — Tier privilege boundary + retraction cascade (governance)

- **Challenges:** read-tier vs build-tier MCP surface (A2), policy-edit CLI-only +
  `GATEWAY_POLICY_PRINCIPAL` fail-closed, retraction cascade (G3/G4), `retracted-citations` lint.
- **Setup:** a retracted source cited by N wiki pages; a read-tier MCP client.
- **Action:** enumerate the read-tier tool set; attempt `wiki_deposit` / `wiki_remediate` /
  policy-edit from read tier; attempt policy-edit via MCP with no principal; mark the source
  retracted and run the lifecycle + `wiki lint --scope retracted-citations`.
- **Pass:** read-tier exposes **only** side-effect-free, token-free ops (no deposit / remediate
  / policy-edit); policy-edit with unset principal **fails closed**; retraction flags all N
  citing pages with a live-computed cascade depth (not a sidecar nobody writes).
- **Catches:** privilege-tier misclassification (the `agents` / `lint` / `status` mis-as-read
  defect); spoofable policy identity; a cascade detector reading a file no producer writes.

---

## Priority

The proven-fragile seams are **#5 / #6** (committer concurrency — the keystone; every
concurrency defect this build shipped lived on a silent no-exception path) and **#7** (dedup —
the lexical-fallback encoder fails the hard alias cases by design, so the alias-authority
fallback is the only thing between you and false merges). **#2** and **#9** are the
confabulation guards that have repeatedly failed past green tests. **#8** is cheap insurance
against exactly the slug-mismatch class just fixed.

If you only run three, run **5, 7, 9** — the ones most likely to be inert-in-production while
passing a naive happy-path test.
