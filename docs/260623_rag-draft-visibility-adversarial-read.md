# Adversarial read — RAG draft-visibility handoff (brief + contp)

**Date:** 2026-06-23 · **Reviews:** `docs/260622_rag-retrieval-draft-visibility-brief.md` + `…-contp.md`
**Method:** read both as if executing cold, trying to make the fix produce a false green or waste gate work. Code refs verified against main @ `305b4136`.

Findings ordered by severity. **1–5 are folded into the contp** (validation preconditions + Q1/Q3 framing + the include_drafts mechanics note). **6–8 live only here.**

## Verified before writing
- `retrieve.py:160` `include_drafts: bool = False`; `retrieve_op` (~282) never overrides it. ✓
- `search_index.py:356` `include_drafts: bool = True`; `:384-385` `if not include_drafts: where.append("p.draft = 0")`. ✓
- `search_index.py:460-465` `_authority_key` / `_DRAFT_PENALTY` / `_TYPE_BOOST`. ✓
- `retrieve.py:195` empty-section skip is `if not text: continue` — drops EMPTY text only. ✓ (load-bearing for finding 4)

The mechanism the brief pins is real. The fix premise holds. The problems below are in the *validation design* and *framing*, not the diagnosis.

---

## Severe — one-sided validation (false-green risk)

### Finding 1 — no negative control for stub pollution / displacement
All 21 probe goldens measure recall ("did the draft concept surface"). Nothing measures the downside the fix introduces: admitting ~1,100 drafts can (a) float empty/placeholder stubs into the block, or (b) displace a finalized page that should have won. The `eval-retrieval --compare ≥0.90` regression runs on lexically-easy goldens and won't exercise paraphrased stub-pollution. **A fix that surfaces good drafts AND pollutes results passes every gate in the contp.**
**Fix:** add negative-control queries — a finalized page is the right answer and a draft stub must NOT outrank it; plus ≥1 query targeting a placeholder stub to confirm it stays down. → folded into contp Validate.

### Finding 2 — probe `expect:` slugs are unverified
Goldens were hand-built in an ephemeral session. A non-existent `expect` slug reads MISS before AND after the fix, silently dragging the score and masking real improvement. The verbose synthesis-style slugs (e.g. `the-clinical-application-of-bupropion-…`) are the obvious risk.
**Fix:** confirm every `expect` slug resolves to a real page before trusting any before/after delta; fix or drop non-resolvers. → folded into contp Validate.

### Finding 3 — Q3 "wire into the gate" measures the wrong layer
Both docs state `eval-retrieval` scores the FTS layer, not the retrieve assembly — but the fix is *in* the retrieve assembly. Persisting `semantic_mismatch.yaml` into `eval-retrieval`/`gate.py` would gate the layer that wasn't changed. The only instrument that tests the fix is the ad-hoc Appendix-B script, which isn't a harness and isn't gate-integrated. "Persist the yaml" is cheap; "wire into the gate so it can't regress" means promoting the Appendix-B retrieve-path scorer into the eval harness — real work.
**Fix:** keep Q3 open but split it — persist (cheap) vs gate-wire (scoped work, not a one-liner). → folded into contp Q3.

---

## Moderate — framing that misleads the implementer

### Finding 4 — option A's "stubs already handled" claim is false
The brief leans on the empty-section skip (`retrieve.py:195`) to argue A-alone is stub-safe. That skip drops only *empty* text. Legacy stubs read `_(needs population from legacy import)_` — non-empty — so A-alone WILL surface them. The brief admits this under option D but not where it recommends A. Net: A+D is more load-bearing than the recommendation implies; this bears directly on the open Q1.
**Fix:** Q1 framing notes A-alone is not stub-safe. → folded into contp Q1.

### Finding 5 — A and B are nearly the same mechanism
Option A *requires* flipping `include_drafts→True` on the retrieve path — that is the only way drafts enter the candidate pool — then trusting `_DRAFT_PENALTY` to demote them. A is "B plus the penalty (plus optional content-gate)." "Do not blind-flip B" can be misread as "avoid touching include_drafts," which is impossible for A. The real distinction: flip it AND verify stubs stay down.
**Fix:** mechanics note in the implement step. → folded into contp.

---

## Minor — notes (here only, not folded)

### Finding 6 — `wiki answer` inheritance is subtler than "confirm acceptable"
Drafts are drafts because their citation grounding is a downgraded lint warning (hard rule #3). Letting them into `wiki answer`'s LLM context means grounded answers can now cite pages whose own provenance is unfinalized. Possibly fine, but it's a citation-fidelity judgment, not a one-line checkbox. Decide it explicitly when settling Q2 (the draft-annotation question is the natural place — an annotated draft citation is more defensible than a silent one).

### Finding 7 — "~0.33 FTS ceiling" is a soft reference, not a pass bar
Measured on `wiki search` (tiered/bm25 order). Post-fix `retrieve` uses `_authority_key` + `_DRAFT_PENALTY` (different ranking), so a correct fix may land below 0.33. Don't treat <0.33 as failure if controls flip and drafts surface. → also noted in contp Validate.

### Finding 8 — blast-radius counts are ephemeral
382/335/400 (concepts/entities/synthesis drafts), "~1,100", were computed in the ephemeral session. Re-verify against the current tree before quoting; ingests since 06-22 may have moved them. Mechanism unaffected either way.

---

## Bottom line
The diagnosis and pinned mechanism are sound — implement with confidence. The risk is entirely in proving the fix worked: the handoff's validation only measures the upside (recall) and trusts hand-built goldens. Add the negative control (1), verify the goldens resolve (2), and don't mistake the FTS eval for a test of the retrieve fix (3). Everything else is framing.
