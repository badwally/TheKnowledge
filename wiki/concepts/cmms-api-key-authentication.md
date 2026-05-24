---
type: concept
slug: cmms-api-key-authentication
canonical_name: CMMS API Three-Key Authentication and Account-Backed Authorization
domains:
  - condo-software
---

# CMMS API Three-Key Authentication and Account-Backed Authorization

## Summary

The three-key + account-backed authorization pattern is a CMMS API authentication design in which API access requires three independent credentials — an Application Key identifying the integration, an Access Key authenticating the API client, and a Secret Key proving possession — and the API user is itself a real CMMS user account whose permissions transitively scope what the integration can do. The Fiix CMMS API documents this pattern explicitly and recommends scoping the backing account to least-privilege rather than running integrations as administrator [[sources/web-2025-01-01-880]].

## Key claims

- Fiix CMMS API access requires three distinct credentials issued together: Application Key, Access Key, and Secret Key [[sources/web-2025-01-01-880]].
- The credentials are minted from the CMMS Settings > Connect Management > MA Connect API Application Settings page after registering a new API Application [[sources/web-2025-01-01-880]].
- The Secret Key is one-time-retrievable on initial display; Fiix explicitly warns that the value cannot be retrieved later and must be stored securely by the integrator [[sources/web-2025-01-01-880]].
- API keys are associated with a particular backing user account; any access via that key flows through the backing account's permissions [[sources/web-2025-01-01-880]].
- Fiix recommends customizing the backing account's permissions — for example, reassigning the API user from "administrators" to "technicians" — to fine-tune access rules to how the integration is intended to interact with the CMMS [[sources/web-2025-01-01-880]].
- The account-backed authorization model means that hardening the integration's blast radius is a customer-configuration responsibility, not a vendor-enforced default [[sources/web-2025-01-01-880]].
- The same authentication credentials apply to both production and Sandbox tenants; the integrator chooses which by registering the API Application in the corresponding instance [[sources/web-2025-01-01-880]].

## Sources

- [[sources/web-2025-01-01-880]] — Fiix CMMS API Developer's Guide (fiixlabs.github.io/api-documentation/guide.html, January 1, 2025)

## Related

- [[entities/fiix-cmms]]
