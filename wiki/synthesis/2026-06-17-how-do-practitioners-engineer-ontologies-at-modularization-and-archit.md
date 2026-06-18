---
schema_version: 1
type: synthesis
slug: 2026-06-17-how-do-practitioners-engineer-ontologies-at-modularization-and-archit
title: Modularization and Architecture — investigation (2026-06-17-how-do-practitioners-engineer-ontologies-at)
domains:
- semantic-models
question: 'How do practitioners engineer ontologies at production quality? Cover:
  established methodologies (METHONTOLOGY, NeOn, SAMOD, agile and competency-question-driven
  design); ontology design patterns (content patterns, logical patterns, the ODP catalog)
  and anti-patterns; modularization and ontology reuse; ontology alignment and matching
  (techniques, the OAEI evaluation campaigns, precision and recall tradeoffs); upper
  and foundational ontologies (BFO, DOLCE, SUMO, gist) and when to commit to one;
  and ontology lifecycle, versioning, and governance. Include foundational methodology
  papers, the ontology-design-pattern literature, OAEI results, and current engineering
  practice.'
created_at: '2026-06-17T20:07:18Z'
synthesizes:
- sources/web-1995-01-01-faa
last_updated: '2026-06-17T20:07:20Z'
sources_count: 6
draft: true
draft_started_at: '2026-06-17T20:07:20Z'
draft_unresolved_claims: 14
---
# Modularization and Architecture — investigation

**Origin question:** How do practitioners engineer ontologies at production quality? Cover: established methodologies (METHONTOLOGY, NeOn, SAMOD, agile and competency-question-driven design); ontology design patterns (content patterns, logical patterns, the ODP catalog) and anti-patterns; modularization and ontology reuse; ontology alignment and matching (techniques, the OAEI evaluation campaigns, precision and recall tradeoffs); upper and foundational ontologies (BFO, DOLCE, SUMO, gist) and when to commit to one; and ontology lifecycle, versioning, and governance. Include foundational methodology papers, the ontology-design-pattern literature, OAEI results, and current engineering practice.
**Session:** 2026-06-17-how-do-practitioners-engineer-ontologies-at
**Branch:** Modularization and Architecture

## Synthesis

### Specifics

Based on the provided sources, several specific frameworks, principles, and mechanisms emerge regarding the modularization and architectural design of production ontologies.

## The Hub-and-Spokes Architecture
This architectural approach structures large-scale, multi-domain ontology initiatives to promote reuse, divide labor, and ensure future-proofing.
*   **Name and Key Claim**: The Hub-and-Spokes Architecture (advocated by the OBO Foundry and BFO) claims that ontology development should be organized concentrically to separate highly abstract concepts from localized, domain-specific data.
*   **Core Approach**: A very general upper ontology (such as the Basic Formal Ontology, or BFO) sits at the center as the "hub" [1, 2]. From this hub, developers branch outward to build general reference ontologies (e.g., a generic Protein Ontology), which are designed to be reused over and over [1]. Finally, at the outermost edges (the "spokes"), practitioners build highly specific application ontologies tied to local project data (e.g., an ontology representing subjects in a specific mouse experiment) [1]. 
*   **Concrete Details**: This architecture relies on the principle of "orthogonality" to divide labor logically; for example, by creating a distinct reference ontology just for proteins, the architecture naturally attracts protein experts as maintainers while preventing their work from overlapping or conflicting with other domains [1, 2].

## Domain-Driven Design (Avoiding the "Kitchen Sink")
Enterprise environments frequently suffer from ontologies that are tightly coupled to legacy database schemas, a problem solved by strict domain-driven design.
*   **Name and Key Claim**: Domain-Driven Design claims that an ontology must model real-world reality and semantic entities, not the quirks of the source systems supplying the data [3, 4].
*   **Core Approach**: Practitioners must separate the fundamental identity of an object from observations or events related to it [4]. Developers are instructed to never map source data columns 1:1 into ontology properties, a practice Palantir identifies as the "Kitchen Sink" anti-pattern [4, 5].
*   **Concrete Details**: As a concrete example, if a source CSV contains columns for `order_id`, `customer_name`, `customer_email`, `product_sku`, and `quantity`, the ontology should represent this as at least three distinct real-world entities (an Order, a Customer, and a Product) with semantic links between them, rather than a single monolithic "Order" object type [5]. Naming conventions should also reflect human business language (e.g., using `lastInspectionDate` rather than a technical API name like `dtLastInspMod`) [4, 5].

## Composition Over Deep Hierarchies
To keep models pluggable and extensible, ontology architecture should borrow compositional inheritance strategies from software engineering.
*   **Name and Key Claim**: Composition over Deep Hierarchies claims that flexible multiple inheritance through focused interfaces is vastly superior to rigid, deep single-inheritance chains [6, 7].
*   **Core Approach**: When an entity requires multiple capabilities, developers should implement multiple distinct interfaces rather than inserting the entity into a deep taxonomic tree [7]. Workflows and applications should then target these interfaces rather than the underlying objects [7].
*   **Concrete Details**: Developers should avoid creating "combination" types, such as `SchedulableBuilding` or `InspectableVehicle` [6]. Instead, they should model focused capability interfaces like `Inspectable`, `Schedulable`, or `Billable` [7]. By doing so, an enterprise workflow built to operate on the `SchedulableResource` interface will seamlessly function for arenas, conference rooms, and vehicles without requiring any modification to the workflow itself [7].

## The Open-Closed Principle and The Rule of Three
Production ontologies must balance the need for architectural stability with the demand for continuous expansion.
*   **Name and Key Claim**: "Open for extension, closed for modification" and "Don't repeat yourself (Rule of Three)" dictate that core models must be strictly protected while remaining accessible for specialized extension by other teams [8, 9].
*   **Core Approach**: Once an object type or interface is in production, its core structure is locked down [9]. If new use cases arise, builders must extend the ontology by creating new linked object types, implementing new interfaces, or utilizing new property namespaces rather than modifying the core entity [10]. To prevent duplicate extensions, the "Rule of Three" acts as a trigger: one instance of a model is a coincidence, two is a pattern, but if three teams build the same workflow or object type, it must be refactored into a single canonical representation [8].
*   **Concrete Details**: Modifying core models is treated as an anti-pattern because it causes frequent breaking changes that cascade across dependent enterprise applications [9]. Enforcing this boundary also ensures that extending an ontology for a specific team does not inadvertently widen security access for other consumers relying on the core model [10].

## Automated Modularization via Community Detection
Because large ontologies can become incomprehensible "knowledge soups", researchers have developed methods to automatically extract and group architectural modules.
*   **Name and Key Claim**: Ontology summarization and modularization via Community Detection claims that large ontologies can be structurally understood by isolating the dense topological groupings of their Ontology Design Patterns (ODPs) [11, 12].
*   **Core Approach**: The method translates an ontology into an intentional graph and applies community detection algorithms (like Clauset-Newman-Moore) to identify non-overlapping clusters [13, 14]. To capture the context of use, intermediate nodes are injected to represent contextualized properties, enabling the algorithm to find overlapping communities and group related terms into "conceptual components" based on their terminology [14, 15].
*   **Concrete Details**: When applied to a Cultural Heritage corpus containing 43 ontologies, the algorithm successfully extracted over 1,000 distinct communities (averaging 30 communities per ontology) representing conceptual components like "categorization" or "membership" [16, 17]. This automated extraction is highly relevant for ontology engineering because modern editors (like Protégé) generally lack a native function to import only a specific pattern or module, frequently forcing engineers to import entire monolithic ontologies or manually redefine the axioms they need [18, 19].

[^1]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^2]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^3]: [[sources/Ontology design: Best practices • Palantir]]
[^4]: [[sources/Ontology design: Best practices • Palantir]]
[^5]: [[sources/Ontology design: Best practices • Palantir]]
[^6]: [[sources/Ontology design: Best practices • Palantir]]
[^7]: [[sources/Ontology design: Best practices • Palantir]]
[^8]: [[sources/Ontology design: Best practices • Palantir]]
[^9]: [[sources/Ontology design: Best practices • Palantir]]
[^10]: [[sources/Ontology design: Best practices • Palantir]]
[^11]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^12]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^13]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^14]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^15]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^16]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^17]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^18]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^19]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]] [^8]: [[sources/web-1995-01-01-faa]] [^9]: [[sources/web-1995-01-01-faa]] [^10]: [[sources/web-1995-01-01-faa]] [^11]: [[sources/web-1995-01-01-faa]] [^12]: [[sources/web-1995-01-01-faa]] [^13]: [[sources/web-1995-01-01-faa]] [^14]: [[sources/web-1995-01-01-faa]] [^15]: [[sources/web-1995-01-01-faa]] [^16]: [[sources/web-1995-01-01-faa]] [^17]: [[sources/web-1995-01-01-faa]] [^18]: [[sources/web-1995-01-01-faa]] [^19]: [[sources/web-1995-01-01-faa]]

### Comparisons

Based on the provided sources, several distinct architectural comparisons emerge regarding how practitioners scale, organize, and modularize ontologies for production use. 

## Architectural Paradigms for Scalability
When structuring large-scale ontologies, practitioners must choose between strictly hierarchical modularity and flatter, compositional modularity to ensure the system remains extensible.
*   **Items Compared:** The Hub-and-Spokes Architecture (advocated by the OBO Foundry and BFO) versus Composition Over Deep Hierarchies (advocated by Palantir).
*   **Differences in Evidence and Outcomes:** The Hub-and-Spokes architecture organizes ontology modules concentrically, maintaining a highly abstract "hub" at the center (like the Basic Formal Ontology) which branches outward into reusable domain reference ontologies, and ultimately into highly specific application ontologies at the "spokes" [1]. Palantir’s guidelines argue against relying on deep taxonomic chains, instead promoting a compositional approach that uses focused interfaces (e.g., `Inspectable`, `Schedulable`) to aggregate specific behaviors across otherwise unrelated object types via multiple inheritance [2].
*   **Trade-offs and Contexts:** The Hub-and-Spokes architecture is best suited for massive, federated environments (such as the biological sciences), where strict orthogonality—the principle that domain modules must not overlap—is required to successfully divide labor among disparate expert groups [3]. Conversely, the compositional interface approach applies best in dynamic enterprise environments where objects frequently acquire new capabilities and where workflows must operate seamlessly across disparate entities (e.g., scheduling both a conference room and a vehicle) [4].
*   **Strengths and Weaknesses:** A major strength of the Hub-and-Spokes model is its ability to future-proof an ontology by ensuring high discoverability and preventing duplicated effort across large scientific communities [5]. Its weakness is the risk of enterprise developers producing "combination" types to merge concepts, which results in brittle, single-inheritance taxonomies [6]. The strength of the compositional approach is its extreme flexibility; it keeps the core model pluggable, allowing the ontology to remain open for extension but closed for core modification [7]. Its weakness is that it requires strict, centralized governance, such as the "Rule of Three" (refactoring duplicated properties into a canonical interface only after three instances are observed), to prevent the proliferation of redundant interfaces [8].

## Ontology Construction vs. Deconstruction
When dealing with the complexity of domain representation, practitioners face a sharp divide between manual, proactive modeling and automated, retroactive extraction.
*   **Items Compared:** Manual Domain-Driven Design versus Automated Modularization via Community Detection.
*   **Differences in Evidence and Outcomes:** Domain-Driven Design dictates that developers must manually engineer object types to reflect real-world semantic entities, rather than mapping source database columns 1-to-1 into the ontology [9]. In contrast, automated modularization acknowledges that many existing ontologies are already poorly structured "knowledge soups"; it applies community detection algorithms (like Clauset-Newman-Moore) to intentional graphs to reverse-engineer and automatically extract densely connected Ontology Design Patterns (ODPs) [10].
*   **Trade-offs and Contexts:** Manual Domain-Driven Design is intended for the active development of new ontologies or the refactoring of enterprise systems where engineers have the authority to separate core identities from observational events [11]. Automated community detection applies in contexts where developers must evaluate, comprehend, or reuse massive legacy ontologies, bypassing the need for manual inspection [12]. It is particularly critical because modern editors, such as Protégé, lack working mechanisms to import partial patterns, forcing engineers to either import entire monolithic modules or extract the required components automatically [13]. 
*   **Strengths and Weaknesses:** The strength of manual Domain-Driven Design is its semantic purity, resulting in intuitive models that utilize human business language [14]. Its weakness is that it is highly labor-intensive and prone to failure if engineers succumb to the "Kitchen Sink" anti-pattern of merely mirroring source schemas [15]. The strength of automated community detection is its ability to rapidly parse immense networks, successfully extracting over 1,000 distinct semantic communities from a Cultural Heritage corpus [16]. Its primary weakness is its absolute dependence on the original ontology's formal axiomatization; when applied to ontologies lacking property restrictions or domain/range declarations, the algorithm fails to identify meaningful boundaries and instead returns massive, semantically incoherent clusters [17].

[^1]: [[sources/Building Ontologies with Basic Formal Ontology: | Guide books | ACM Digital Library]]
[^2]: [[sources/Ontology design: Best practices • Palantir]]
[^3]: [[sources/Building Ontologies with Basic Formal Ontology: | Guide books | ACM Digital Library]]
[^4]: [[sources/Ontology design: Best practices • Palantir]]
[^5]: [[sources/Building Ontologies with Basic Formal Ontology: | Guide books | ACM Digital Library]]
[^6]: [[sources/Ontology design: Best practices • Palantir]]
[^7]: [[sources/Ontology design: Best practices • Palantir]]
[^8]: [[sources/Ontology design: Best practices • Palantir]]
[^9]: [[sources/Ontology design: Best practices • Palantir]]
[^10]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^11]: [[sources/Ontology design: Best practices • Palantir]]
[^12]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^13]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^14]: [[sources/Ontology design: Best practices • Palantir]]
[^15]: [[sources/Ontology design: Best practices • Palantir]]
[^16]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^17]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]] [^8]: [[sources/web-1995-01-01-faa]] [^9]: [[sources/web-1995-01-01-faa]] [^10]: [[sources/web-1995-01-01-faa]] [^11]: [[sources/web-1995-01-01-faa]] [^12]: [[sources/web-1995-01-01-faa]] [^13]: [[sources/web-1995-01-01-faa]] [^14]: [[sources/web-1995-01-01-faa]] [^15]: [[sources/web-1995-01-01-faa]] [^16]: [[sources/web-1995-01-01-faa]] [^17]: [[sources/web-1995-01-01-faa]]

### Gaps

Based on the provided sources, several limitations, gaps, and unanswered tensions emerge regarding the modularization and architectural design of ontologies.

## The Lack of Modern Tooling for Partial Module Imports
Based on the provided sources, a major limitation in modern ontology architecture is the lack of software support for granular module reuse.
*   **The Limitation:** While architectural best practices encourage the reuse of small modules and patterns, modern ontology editors like Protégé force users to import entire ontology files rather than specific, isolated modules [1]. 
*   **The Unanswered Question:** Historical solutions, such as the NeOn toolkit's plugins for extracting or cloning specific patterns from a larger module, have been dismissed and lost to software obsolescence [1]. The corpus does not explain how current practitioners can practically implement compositional architectures—reusing only specific interfaces or patterns—without being forced to either manually redefine axioms from scratch or inherit massive, unwanted logical dependencies [1].

## Ambiguity in Defining Module Boundaries
Based on the provided sources, the automated extraction and definition of ontology modules rely on imperfect heuristics rather than formalized standards.
*   **The Limitation:** When using automated methods like community detection to modularize large legacy ontologies, algorithms fail to find meaningful boundaries in poorly axiomatized ontologies (such as those lacking strict domain/range or property restrictions), resulting in overly broad or "bad" communities [1]. Furthermore, researchers admit their boundary-drawing rules are basic heuristics that risk missing components or generating mere approximations of the module's true scope [1].
*   **The Unanswered Question:** A careful reader would note that the corpus does not provide a formal, reliable methodology for defining exact module boundaries when retroactively structuring an ontology [1]. Additionally, it leaves unanswered how to effectively incorporate instance data to improve boundary detection, which researchers explicitly acknowledge remains an unsolved area of future work [1].

## The Tension Between Formal Orthogonality and Enterprise Pragmatism
Based on the provided sources, there is a stark, unresolved ideological conflict regarding how strictly modular boundaries must be enforced.
*   **The Tension:** Proponents of foundational architectures like BFO and the OBO Foundry mandate strict "orthogonality" (non-overlapping modules) and claim that "mappings never work," requiring developers to get the module completely right from the start rather than relying on retroactive alignments [2]. Conversely, enterprise guidelines explicitly embrace "pragmatism and tradeoffs," advising developers to accept technical debt and deploy "slightly imperfect" ontologies to meet rapid production deadlines [3]. 
*   **The Unanswered Question:** The corpus leaves a gap regarding how an ontology engineer should reconcile these opposing directives in a real-world production environment [2, 3]. Specifically, the sources do not provide a framework or metrics to quantify technical debt, leaving it entirely subjective as to when a pragmatic architectural shortcut crosses the line into a fatal structural anti-pattern [3].

[^1]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^2]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^3]: [[sources/Ontology design: Best practices • Palantir]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]]

## Sources cited

- [[sources/web-1995-01-01-faa]]

## Included works

- [[sources/web-1995-01-01-faa]]
