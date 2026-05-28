---
schema_version: 1
type: concept
slug: model-context-protocol
canonical_name: Model Context Protocol (MCP)
domains:
- orita-cmo
created_at: '2026-05-28T04:05:16Z'
last_updated: '2026-05-28T04:05:16Z'
---

# Model Context Protocol (MCP)

## Summary

Model Context Protocol (MCP) is a standardized way for agents built with large language models to securely request information from, and take action in, external systems; HubSpot describes it as "a secure language or set of rules that allows an AI to ask for context… from HubSpot or even to take action in the account" [[sources/web-2026-01-01-0e1]]. In the HubSpot deployment, MCP servers function as secure gateways through which authorized LLM-based clients fetch real-time CRM data or invoke account-level actions in a controlled manner [[sources/web-2026-01-01-0e1]].

## Key claims

- MCP is positioned as a standardized protocol — not a HubSpot-specific construct — that any MCP-compatible AI tool or agent can speak to interoperate with external systems exposing an MCP server [[sources/web-2026-01-01-0e1]].
- The protocol covers both context retrieval ("give me the recent activity for Contact X") and action invocation (writing records, deploying changes), not just read-only data access [[sources/web-2026-01-01-0e1]].
- HubSpot's deployment pattern distinguishes Remote MCP servers (network-reachable, OAuth-authenticated, used for production CRM access) from Local MCP servers (CLI-installed, authenticated through the local tool, used for developer workflows) [[sources/web-2026-01-01-0e1]].
- The MCP specification is moving from OAuth 2.0 to OAuth 2.1 with PKCE and single-use refresh-token rotation; HubSpot has committed to that alignment later in 2025, signaling that PKCE + refresh-token rotation is the spec direction for remote MCP servers generally [[sources/web-2026-01-01-0e1]].
- Scope control in MCP deployments is delegated to the host system's existing authorization model — in HubSpot's case, user-level applications with explicit CRM scopes and admin-first connection — rather than being defined at the protocol layer [[sources/web-2026-01-01-0e1]].
- Vendors deploying MCP servers can carve out classes of data (e.g. HubSpot excludes Custom Sensitive Data Properties / PHI) that the protocol is not permitted to surface, independent of the underlying scope grants [[sources/web-2026-01-01-0e1]].

## Sources

- [[sources/web-2026-01-01-0e1]] — HubSpot MCP Server product page, including its FAQ definition of MCP

## Related

- [[entities/hubspot-mcp]] — HubSpot's two-server MCP implementation
- [[entities/claude-code]] — MCP client runtime
- [[entities/claude-desktop]] — MCP client runtime
- [[entities/hubspot-admin-skills]] — direct-REST alternative to MCP for HubSpot administration
