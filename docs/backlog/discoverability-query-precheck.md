# Backlog: wiki query Pre-check Against Existing Synthesis

**Category:** Gateway Feature
**Priority:** High
**Effort:** ~half day
**Trigger to action:** When duplicate synthesis pages are observed in `wiki lint` output, or when `wiki list-concepts --kind synthesis` shows pages that clearly overlap with recent `wiki query` calls

---

## Problem

`wiki query` synthesises from scratch every time — even when the wiki already contains a synthesis page that answers the question. With 330+ synthesis pages across 12 domains, the probability that a query duplicates existing work is non-trivial. Each duplicate costs an LLM synthesis call and creates a page that clutters the corpus.

The user has no convenient way to check before querying. `wiki list-concepts --kind synthesis` lists all synthesis pages but doesn't score them against the incoming question. The mental burden of checking is high enough that it rarely happens.

## Proposed behaviour

Before synthesising, `wiki query` checks for existing synthesis pages whose `question:` frontmatter or `title:` overlaps significantly with the incoming query. If overlap exceeds a threshold, it surfaces the candidate and prompts:

```
$ wiki query "what mechanisms explain GLP-1 suppression of food noise?" --domain glp1

Found similar existing synthesis (no LLM call made):
  wiki/synthesis/2026-04-12-glp1-food-noise-mechanisms.md
  similarity: 0.87  |  question: "What mechanisms underlie GLP-1 food-noise suppression?"
  created: 2026-04-12  |  sources: 8

Use existing page? [y = open in context / n = synthesise anyway / v = view summary]
```

In non-interactive mode (e.g. MCP calls from agents), the threshold check runs silently and the candidate is returned in the result payload as `existing_match` — the caller decides whether to use it.

## Implementation notes

**Similarity scoring:** token-overlap (Jaccard or TF-IDF cosine) over question + title text. No LLM call required. The scoring function compares the incoming `question` string against `question:` and `title:` frontmatter fields of all synthesis pages in the target domain. This is fast enough to run inline for any domain with <500 synthesis pages.

**Threshold:** 0.75 similarity as default skip-and-prompt. Configurable via `--similarity-threshold` flag. Below threshold: proceed silently. Above threshold: surface candidates.

**Scope:** Only scan synthesis pages in the specified `--domain`. Cross-domain scan is too slow and generates spurious matches.

**Non-interactive fallback (`--no-check`):** Flag to skip the pre-check entirely for scripted/batch use.

**Data model change:** None. `question:` is already a required frontmatter field on synthesis pages (validator-enforced). The pre-check reads existing frontmatter; no schema changes needed.

## Sketch

```python
# ops/query.py — before calling the LLM synthesis pipeline

def _find_similar_synthesis(question: str, domain: str, threshold: float = 0.75
                             ) -> list[tuple[Path, float]]:
    """Return synthesis pages in `domain` with similarity >= threshold."""
    synth_dir = paths.knowledge_root() / "wiki" / "synthesis"
    candidates = []
    for p in synth_dir.glob("*.md"):
        front, _ = fm.parse(p.read_text())
        if domain and domain not in (front.get("domains") or []):
            continue
        existing_q = str(front.get("question", "") or front.get("title", ""))
        score = _token_overlap(question, existing_q)
        if score >= threshold:
            candidates.append((p, score))
    return sorted(candidates, key=lambda x: x[1], reverse=True)
```

The interactive prompt lives in `cli.py`'s `_run_query`; the MCP path skips the prompt and returns the match in `result.data["existing_match"]`.

## Related

- `wiki list-concepts --kind synthesis` — manual pre-check (ships in current release)
- `docs/backlog/discoverability-moc-pages.md` — MOC pages reduce the need for this check by making domain synthesis inventory visible before querying
