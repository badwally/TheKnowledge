---
schema_version: 1
type: concept
slug: plan-before-execute-after
canonical_name: Plan / Before / Execute / After Pattern
domains:
- orita-cmo
created_at: '2026-05-28T04:05:19Z'
last_updated: '2026-05-28T04:05:19Z'
---

# Plan / Before / Execute / After Pattern

## Summary

Plan / Before / Execute / After is a four-stage workflow pattern for safely mutating expensive-to-recover CRM data with an AI agent, originated by Tom Granot in his HubSpot admin skills repository and designed so that each stage produces auditable artifacts and atomic, reversible operations [[sources/yt-ZUIprPSbYO4]].

## Key claims

- The motivating premise is that CRM data is **expensive and hard to get back** — mutations need to be plannable, auditable, and reversible at the level of individual atomic operations [[sources/yt-ZUIprPSbYO4]].
- **Plan stage**: a dedicated planning skill enumerates the target API endpoints, the scripts that will run, the retry logic, and the rollback story for each atomic operation; it also checks prerequisites (e.g. whether the operator has the required HubSpot permissions) [[sources/yt-ZUIprPSbYO4]].
- **Before stage**: a generated script queries the current state — properties, contacts, companies in scope — to capture a baseline that downstream verification can compare against [[sources/yt-ZUIprPSbYO4]].
- **Execute stage**: the mutation scripts run, with the agent fixing breakage encountered along the way [[sources/yt-ZUIprPSbYO4]].
- **After stage**: a verification script checks whether the system has converged to the expected post-state; critically, if completion depends on HubSpot-side workflow propagation (which can take hours on 100k contacts), the after stage records the *expected* completion time and re-checks rather than declaring success prematurely [[sources/yt-ZUIprPSbYO4]].
- Generated scripts are preferred over MCP tool calls because they (a) are not bound by what tools the MCP exposes and (b) can reach external resources mid-flow, where MCPs are typically scoped to a single platform instance [[sources/yt-ZUIprPSbYO4]].
- Operationally backed by a **ticket-per-skill** discipline in a task tracker: each stage appends a status comment to the ticket, and the ticket is closed only when the after stage verifies success [[sources/yt-ZUIprPSbYO4]].

## Sources

- [[sources/yt-ZUIprPSbYO4]]

## Related

- [[entities/tom-granot]]
- [[entities/hubspot-admin-skills]]
- [[entities/claude-code]]
- [[entities/hubspot]]
- [[concepts/hubspot-data-hygiene]]
- [[concepts/agent-escalation-levels]]
