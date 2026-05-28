---
schema_version: 1
type: entity
slug: bigquery
canonical_name: BigQuery
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T14:04:50Z'
last_updated: '2026-05-28T14:04:50Z'
---

# BigQuery

## Summary

BigQuery is Google Cloud's data warehouse, accessed via the Google Cloud Platform console and organized around datasets and tables [[sources/yt-3JqJkRF0_yU]]. Third-party ETL platforms such as Coupler.io can write data from SaaS applications like HubSpot into BigQuery on a configurable schedule, authenticating with a service-account JSON key [[sources/yt-3JqJkRF0_yU]].

## Key facts

- Vendor: Google Cloud Platform [[sources/yt-3JqJkRF0_yU]].
- Data model: datasets and tables; a write destination is fully specified by dataset name plus table name [[sources/yt-3JqJkRF0_yU]].
- Authentication for external writers: Google Cloud service-account JSON key file [[sources/yt-3JqJkRF0_yU]].
- Minimum write roles for an ETL service account: `BigQuery data editor` and `BigQuery job user` [[sources/yt-3JqJkRF0_yU]].
- Service-account key creation path in the GCP console: IAM & Admin → Service accounts → create account → Manage keys → Add key → Create new key → JSON type [[sources/yt-3JqJkRF0_yU]].

## Sources

- [[sources/yt-3JqJkRF0_yU]] — Coupler.io Academy: "How to Set up HubSpot to BigQuery integration | Tutorial"

## Related

- [[entities/coupler-io]]
- [[entities/hubspot]]
