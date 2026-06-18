---
schema_version: 1
type: moc
slug: semantic-models
domain: semantic-models
last_updated: '2026-06-18T00:31:33Z'
draft: true
draft_started_at: '2026-06-18T00:31:33Z'
draft_unresolved_claims: 15
---
# semantic-models — Map of Content

## Overview

Auto-generated from the corpus-constructive research loop. Anchored on the most recent `wiki research` run.

## Key entities

- [[sources/web-2026-06-17-e93]] — Quickstart for the dbt Semantic Layer and Snowflake
- [[sources/web-2024-08-22-f1d]] — Data Catalog Vocabulary (DCAT) - Version 3 - W3C
- [[sources/web-2020-02-04-078]] — Data Catalog Vocabulary (DCAT) - Version 2 - W3C
- [[sources/web-2026-06-18-169]] — The W3C Data Catalog Vocabulary, Version 2: Rationale, Design ...
- [[sources/web-2000-01-15-24d]] — DCAT-US Schema v3.0 | resources.data.gov
- [[sources/web-2026-06-18-314]] — [PDF] Ontology-Based Data Access: A Survey - IJCAI
- [[sources/web-2026-06-18-cba]] — [PDF] Ontology Based Data Access in Statoil
- [[sources/web-2026-06-18-de3]] — [PDF] Ontology-Based Data Access and Integration
- [[sources/web-2026-06-18-836]] — Chapter 4. Publishing Patterns
- [[sources/web-2010-11-10-ec4]] — Linked Data: Evolving the Web into a Global Data Space

## Key concepts

- **The Semantic Layer and Metrics-Layer Pattern** — The pragmatic abstraction of physical data platform schemas to provide a centralized, code-driven definition of business metrics and entities for downstream analytics.
  - dbt Semantic Layer Architecture: Semantic models are structured using "Entities" (primary or foreign keys acting as unique identifiers for joins), "Dimensions" (categorical or temporal attributes for grouping and filtering), and "Simple metrics" (aggregations over a single column) [1-3]., Metrics can be extended beyond simple aggregations into conversion, cumulative, derived, or ratio metrics to support complex business logic, and these are compiled into a `semantic_manifest.json` file for query execution [4, 5].
- **Data-Fabric and Data-Mesh Semantics** — The use of knowledge-graph-backed active metadata catalogs and canonical data models to manage discoverability and interoperability across decentralized enterprise systems.
  - Data Catalog Vocabulary (DCAT) Standard: The core DCAT schema organizes metadata by connecting abstract conceptual `dcat:Dataset` entities with their concrete physical `dcat:Distribution` access points (like CSV or JSON files) and programmatic `dcat:DataService` APIs [6, 7]., Modern enterprise implementations, such as the DCAT-US Schema v3.0, actively enforce these semantics using strict JSON Schema validation, converting previously unstructured text strings into structured, formal objects (e.g., `Location` and `PeriodOfTime`) [8, 9].
  - Linked-Data Publishing and Schema.org Interoperability: To maximize interoperability with external tools like Google Dataset Search, the DCAT specification explicitly aligns with Schema.org, mapping `dcat:Dataset` to `sdo:Dataset` and `dcat:DataService` to `sdo:WebAPI` [10-13]., Linked Data publishing replaces local database keys with dereferenceable HTTP URIs, employing "303 Redirects" to disambiguate abstract real-world objects from the concrete web documents describing them, and "Hash URIs" to group vocabulary terms [14-16].
- **Semantic Integration and Mapping Patterns** — Standardized declarative languages and materialization systems used to transform heterogeneous physical data sources into formal RDF knowledge graphs.
  - R2RML for Relational Databases: R2RML relies on an `rr:TriplesMap` that links a logical SQL table to RDF triples using an `rr:subjectMap` (to generate entity IRIs, typically from primary keys) and multiple `rr:predicateObjectMap` instances to translate columns [17, 18]., Foreign key relationships between tables are handled using an `rr:parentTriplesMap` and an `rr:joinCondition` that links child and parent columns [19, 20].
  - RML for Heterogeneous Sources: RML replaces SQL-specific table references with a generic `rml:LogicalSource` and specifies an `rml:referenceFormulation` [21, 22]., RML applies path languages specific to the source format type, using `ql:XPath` to iterate through XML elements and `ql:JSONPath` for JSON payloads [22, 23].
  - Materialization Engines (ETL KGC): Materialization engines like SDM-RDFizer utilize specialized physical data structures (Predicate Tuple Tables) to efficiently execute joins and remove duplicate triples during the ETL process [24]., Engines like RMLMapper and Chimera use in-memory caches and multi-thread safe procedures to optimize the parsing and materialization of JSON, XML, and CSV files [25, 26].
- **Ontology-Based Data Access (OBDA)** — A pragmatic enterprise architecture that virtualizes formal semantics directly over relational databases, enabling end-users to query data via domain ontologies without requiring data materialization.
  - Formal Semantics and FO-Rewritability: OBDA architectures restrict ontologies to the OWL 2 QL profile (based on the DL-Lite family), ensuring "FO-rewritability" where any SPARQL query over the ontology can be perfectly rewritten into standard SQL [27, 28]., Query processing involves a rewriting phase (compiling ontology axioms into a union of conjunctive queries using clausal resolution) followed by an unfolding phase that maps the rewritten query into SQL via R2RML mappings [29-31].
  - Semantic Query Optimization: Unfolding SPARQL into SQL natively generates highly inefficient queries filled with redundant self-joins and unions due to the mismatch of mapping abstract URIs to physical database tuples [32, 33]., Semantic optimization relies on "OBDA Constraints" (modeling exact predicates and virtual functional dependencies) that represent enterprise domain logic not captured by physical SQL schema constraints, allowing the engine to prune redundant joins and drastically reduce execution times [34, 35].
  - Practitioner Account of OBDA Adoption: Because manual semantic mapping is cost-prohibitive for massive enterprise systems (e.g., Statoil's EPDS database has 37,000 columns), Statoil utilized the BootOX tool to automatically bootstrap initial OWL 2 QL vocabularies and R2RML mappings directly from database schema constraints [36-38]., To remove the IT bottleneck, geologists bypassed SQL entirely by using OptiqueVQS, a visual query system that translates graph-based, form-based, and map-based user interactions directly into executable SPARQL queries [39-41].

## Synthesis pages

_(populated as `wiki research` and `wiki query` runs file syntheses)_
