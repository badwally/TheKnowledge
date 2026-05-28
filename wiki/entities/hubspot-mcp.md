---
schema_version: 1
type: entity
slug: hubspot-mcp
canonical_name: HubSpot MCP
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T04:05:18Z'
last_updated: '2026-05-28T14:59:10Z'
---

# HubSpot MCP

## Summary

HubSpot MCP is an official Model Context Protocol server published by HubSpot that exposes CRM operations — record creation, record updates, record retrieval, and cross-object queries — to MCP-compatible AI clients [[sources/web-2026-01-01-0e1]]. HubSpot actually ships two distinct MCP servers under this product family: the **HubSpot MCP Server (Remote)**, which gives any MCP-compatible AI tool or agent secure read/write access to a HubSpot CRM account, and the **Developer MCP Server (Local)**, a CLI-based server that lets agentic development tools interact with the HubSpot Developer Platform [[sources/web-2026-01-01-0e1]]. Both require the latest HubSpot Developer Platform version [[sources/web-2026-01-01-0e1]].

## Key facts

- Two-server architecture: the Remote MCP server for CRM data access and a Local Developer MCP server for the HubSpot Developer Platform CLI; HubSpot frames the offering as "one for connecting any MCP-compatible AI tool or agent to your CRM, and one for building on the HubSpot Developer Platform" [[sources/web-2026-01-01-0e1]].
- The remote server is reached at the `mcp.hubspot.com` endpoint via OAuth credentials issued by a user-level HubSpot application with the appropriate CRM read scopes [[sources/web-2026-01-01-0e1]].
- The remote server currently supports OAuth 2.0; HubSpot has committed to aligning with MCP-spec OAuth 2.1 later in 2025, which will require MCP clients to implement PKCE (Proof Key for Code Exchange) and single-use refresh-token rotation [[sources/web-2026-01-01-0e1]].
- Read and write scope of the remote server covers CRM objects (contacts, companies, deals, tickets, carts, products, orders, line items, invoices, quotes, subscriptions, and segments/lists) and engagements (calls, emails, meetings, notes, and tasks) [[sources/web-2026-01-01-0e1]].
- Read-only scope covers organizational context (users, teams, reporting structures, owners, roles, seats) and marketing/content (campaigns and campaign metrics, landing pages, website pages, blog posts) [[sources/web-2026-01-01-0e1]].
- Custom Sensitive Data Properties — including Personal Health Information and other Highly Sensitive Data — are explicitly excluded from MCP access by design [[sources/web-2026-01-01-0e1]].
- Admin-first onboarding: the HubSpot account admin must connect first before other users in the account can connect [[sources/web-2026-01-01-0e1]].
- Apps built on the HubSpot MCP server are subject to the same distribution limits as other HubSpot apps [[sources/web-2026-01-01-0e1]].
- The Developer MCP Server is installed via `hs mcp setup` in the HubSpot CLI and requires Developer Platform v2025.2; it operates fully locally and authenticates through the CLI, though HubSpot signals this may change [[sources/web-2026-01-01-0e1]].
- Surface examples HubSpot documents include remote-server prompts like "Get me the latest update about Acme Inc.", "Summarize all deals in the 'Decision maker bought in' stage with value > $1000", and "Fetch 100 part records and tell me the data type of a custom 'Serial number' property"; developer-server prompts include "Create a HubSpot UI Extension project" and "deploy this change to my account" [[sources/web-2026-01-01-0e1]].
- Primary audience is developers, technical teams, and companies building custom LLM-integrated applications or integrations against HubSpot CRM and Developer Platform data [[sources/web-2026-01-01-0e1]].
- Scope of tools exposed is expected to expand over time as HubSpot adds more MCP tools [[sources/web-2026-01-01-0e1]].

## Sources

- [[sources/web-2026-01-01-0e1]] — "HubSpot MCP Server" official product page (developers.hubspot.com/mcp)

## Related

- [[concepts/model-context-protocol]] — the underlying open protocol
- [[entities/hubspot]] — the parent CRM platform
- [[entities/breeze]] — HubSpot's adjacent in-platform AI product family
- [[entities/claude-code]] — agentic MCP client runtime
- [[entities/claude-desktop]] — end-user MCP client runtime
- [[entities/hubspot-admin-skills]] — alternative direct-REST approach to HubSpot CRM automation by Tom Granot
