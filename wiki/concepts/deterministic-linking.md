---
schema_version: 1
type: concept
slug: deterministic-linking
canonical_name: Deterministic Linking
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:01Z'
last_updated: '2026-05-28T20:24:01Z'
---

# Deterministic Linking

## Summary

Deterministic linking is the practice of scoring potential wikilinks against a fixed numeric scale and acting on those scores by configured thresholds, so that link-insertion outcomes are reproducible across runs and the LLM is restricted to upstream judgment work [[sources/web-2026-04-11-879]].

## Key claims

- WikiLoom's linker scores each potential wikilink on a 0–100 scale and bands the outcomes: ≥95 auto-inserted into the page body, ≥85 auto-inserted and flagged in `backlinks.json`, ≥70 deferred to `pending.json` for review, below 70 ignored [[sources/web-2026-04-11-879]].
- The thresholds are configurable under `[linking]` in `wikiloom.toml` [[sources/web-2026-04-11-879]].
- Pending low-confidence link candidates can be reviewed interactively via `wikiloom review`, accepted in bulk with `--accept-all`, or discarded with `--clear` [[sources/web-2026-04-11-879]].
- Deterministic linking is half of WikiLoom's separation of concerns: the LLM handles judgment, while the linker and downstream tooling produce the same output given the same inputs [[sources/web-2026-04-11-879]].
- The pattern is paired with a `wikiloom relink` command that re-runs the linker across every page when new pages are added that earlier pages should now link to [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/llm-wiki-pattern]]
- [[concepts/structural-provenance]]
