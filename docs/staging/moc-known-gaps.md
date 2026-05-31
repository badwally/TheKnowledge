Filed at `docs/M46-followup-items.md`:

- NLM crawler bot-block on Substack/custom-domain pages (11 of 18 substack URLs in raw/ but missing from NLM)
- Bootstrap-domain policy too strict for industry-context inclusion (mitigated mid-session via threshold lowering + 2 new inclusion criteria)
- arxiv + YouTube search adapters fail hard on HTTP 429 instead of backoff
- Stale auto-MoC across reruns (this MoC was hand-authored as a one-time exception)
- Citation chain renders `[[sources/<num>]]` instead of `[[sources/<slug>]]` for some refs (pre-existing M46 #2 — affects citation finalize)
- Session `register_session` blocks ephemeral re-runs (pre-existing M46 #3 — hit and worked around via `mark_abandoned`)
