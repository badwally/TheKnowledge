---
schema_version: 1
type: concept
slug: mit-open-algorithms
canonical_name: MIT Open Algorithms (OPAL)
domains:
- data-collectives
created_at: '2026-06-10T21:35:00Z'
last_updated: '2026-06-10T21:35:00Z'
draft: true
draft_started_at: '2026-06-10T21:35:00Z'
draft_unresolved_claims: 0
---

# MIT Open Algorithms (OPAL)

## Summary

MIT Open Algorithms (OPAL) is a privacy-preserving data-access design developed at MIT in which queriers submit algorithms and queries to a data trustee (e.g. a data cooperative) to be executed against the trustee-held data, rather than receiving copies of the data themselves [[sources/web-2024-04-04-ad6]].

## Key claims

- OPAL inverts the conventional access pattern by moving the code to the data instead of the data to the code, so that raw cooperative data never leaves the cooperative's control [[sources/web-2024-04-04-ad6]].
- This design preserves members' ability to revoke access at any time, because no copies of the underlying data have been distributed to queriers [[sources/web-2024-04-04-ad6]].
- OPAL prevents queriers from linking cooperative data to external datasets, a key mitigation against re-identification of members [[sources/web-2024-04-04-ad6]].
- The approach was developed by researchers including Hardjono and Pentland and is cited as a foundational architecture for data cooperatives [[sources/web-2024-04-04-ad6]].
- OPAL pairs with a requirement that querier algorithms be vetted to ensure member safety, consent, and absence of bias before execution [[sources/web-2024-04-04-ad6]].

## Sources

- [[sources/web-2024-04-04-ad6]]

## Related

- [[concepts/data-cooperative]]
- [[concepts/citizen-directed-data]]
- [[concepts/secondary-use-personal-data]]
- [[entities/midata]]
- [[entities/sandy-pentland]]
