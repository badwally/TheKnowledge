---
schema_version: 1
type: entity
slug: hubspot-admin-skills
canonical_name: HubSpot Admin Skills (SyntaxGTM)
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T04:05:19Z'
last_updated: '2026-05-28T04:05:19Z'
---

# HubSpot Admin Skills (SyntaxGTM)

## Summary

HubSpot Admin Skills is Tom Granot's open repository of Claude Code skills targeting HubSpot CRM administration via direct REST API calls, designed around a plan/before/execute/after workflow with explicit rollback awareness [[sources/yt-ZUIprPSbYO4]].

## Key facts

- Built to fill the gap left by HubSpot's read-only MCP server and developer-only CLI — i.e., to enable safe write/mutate operations on a HubSpot portal from outside the UI [[sources/yt-ZUIprPSbYO4]].
- Skill catalogue includes: **HubSpot audit** (portal walkthrough → recommendations), **HubSpot implementation plan** (built from the audit output, with an internal PowerPoint generator for client meetings), **database hygiene**, **data enrichment**, **ICP tiers + lead scoring**, **automation workflow hygiene**, and **ongoing property maintenance** [[sources/yt-ZUIprPSbYO4]].
- Designed to be **community-extensible**: each user's audit can surface portal-specific issues that get converted into new shareable skills, with anonymization as a precondition for upstream contribution [[sources/yt-ZUIprPSbYO4]].
- Every skill carries an explicit **prerequisites section** so the plan stage can check whether the operator has the HubSpot permissions required (notably super-admin) before proceeding [[sources/yt-ZUIprPSbYO4]].
- Routines that run on a cadence — weekly cleanup, quarterly deep cleanup — are encoded as skills meant to be **manually triggered**, not auto-scheduled [[sources/yt-ZUIprPSbYO4]].
- Skills generate **before scripts** in Python (using the `uv` runner) to snapshot the current state of properties, contacts, and companies before any mutation [[sources/yt-ZUIprPSbYO4]].
- For workflow creation specifically, the repo punts on the unstable Workflows API and instead emits **manual UI build instructions** that the operator (or Claude Code's Chrome browser-use feature) executes [[sources/yt-ZUIprPSbYO4]].

## Sources

- [[sources/yt-ZUIprPSbYO4]]

## Related

- [[entities/tom-granot]]
- [[entities/hubspot]]
- [[entities/claude-code]]
- [[concepts/plan-before-execute-after]]
- [[concepts/icp-tiering]]
- [[concepts/hubspot-data-hygiene]]
