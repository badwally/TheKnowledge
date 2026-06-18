---
schema_version: 1
type: synthesis
slug: 2026-06-17-how-do-practitioners-engineer-ontologies-at-cross-cutting
title: Cross-cutting themes (2026-06-17-how-do-practitioners-engineer-ontologies-at)
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
- synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-lifecycle-versioning-and-
- synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-methodologies-and-require
- synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-modularization-and-archit
- synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-ontology-alignment-and-ma
- synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-ontology-design-patterns-
- synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-upper-and-foundational-on
last_updated: '2026-06-18T21:55:59Z'
sources_count: 17
finalized_at: '2026-06-18T21:55:59Z'
---
# Cross-cutting themes — 2026-06-17-how-do-practitioners-engineer-ontologies-at

**Origin question:** How do practitioners engineer ontologies at production quality? Cover: established methodologies (METHONTOLOGY, NeOn, SAMOD, agile and competency-question-driven design); ontology design patterns (content patterns, logical patterns, the ODP catalog) and anti-patterns; modularization and ontology reuse; ontology alignment and matching (techniques, the OAEI evaluation campaigns, precision and recall tradeoffs); upper and foundational ontologies (BFO, DOLCE, SUMO, gist) and when to commit to one; and ontology lifecycle, versioning, and governance. Include foundational methodology papers, the ontology-design-pattern literature, OAEI results, and current engineering practice.

## Synthesis

### Recurring Patterns

Based on the provided sources, several overarching frameworks and principles traverse multiple domains of ontology engineering.

## Ontology Design Patterns (ODPs) as Structural Anchors
**Themes Used In:** Methodologies, Ontology Design Patterns, Modularization.
*   Methodologies: The eXtreme Design (XD) agile framework explicitly brings software engineering practices to ontologies by centering its entire incremental, test-driven development cycle on the application of reusable ODPs [1].
*   Ontology Design Patterns: When implementing these patterns, practitioners face a strict architectural tradeoff; employing a class-oriented strategy simplifies data integration but harms reasoning speed, whereas a property-oriented strategy (creating dedicated subproperties for the pattern) vastly improves reasoner performance [2].
*   Modularization: Because legacy ontologies are frequently monolithic and lack native support for partial pattern imports, researchers use intentional graphs and community detection algorithms to automatically extract and reverse-engineer ODPs from large "knowledge soups" [3].

## The Hub-and-Spokes Architecture
**Themes Used In:** Modularization and Architecture, Upper and Foundational Ontologies.
*   Modularization: To organize large-scale modeling efforts, practitioners employ a concentric hub-and-spokes architecture to ensure orthogonality, which prevents duplicated effort among different domain experts [4]. 
*   Upper Ontologies: Foundational ontologies, such as the Basic Formal Ontology (BFO), are specifically designed to act as the abstract "hub" at the center of this architecture [5]. Domain experts then build outward from the hub to create generalized reference ontologies, and ultimately design highly specific application ontologies at the "spokes" that tie directly to local project data [4].

## Large Language Models (LLMs) and Deep Learning
**Themes Used In:** Methodologies and Requirements Specification, Ontology Alignment and Matching.
*   Methodologies: Because manually drafting natural language requirements is a major bottleneck, engineers now use Retrieval-Augmented Generation (RAG) and LLMs to automatically generate Competency Questions (CQs) directly from domain literature [6]. 
*   Ontology Alignment and Matching: Traditional syntactic matching systems frequently fail to detect complex semantic nuances, so developers have integrated LLM-generated embeddings into tools like CANARD to discover complex multi-entity correspondences, improving F-measures by up to 45% [7]. Additionally, AI agents like Agent-OM are being deployed to successfully generate alignments in challenging cross-lingual tasks where older lexical systems fail [8].

## Composition over Deep Hierarchies and Domain-Driven Design
**Themes Used In:** Ontology Design Patterns and Anti-Patterns, Modularization and Architecture, Methodologies.
*   Anti-Patterns: Enterprise guidelines warn developers against structural anti-patterns, specifically the "Kitchen Sink" (mapping database columns directly into ontology properties) and deep single-inheritance chains (creating brittle combination types like `SchedulableBuilding`) [9].
*   Modularization: To counter these anti-patterns, architects apply composition over deep hierarchies by defining entities through focused capability interfaces (e.g., modeling `Schedulable` or `Inspectable` as separate traits) [10]. This domain-driven approach keeps the core models closed to modification but open to extension, allowing workflows to operate flexibly across diverse entities [10].
*   Methodologies: Foundational guides, such as Ontology 101, natively support this compositional flexibility by encouraging multiple inheritance, noting that a single entity (like Port wine) can naturally inherit from multiple parent classes (Red wine and Dessert wine) to aggregate diverse property restrictions [11].

## Background Knowledge as Mediators
**Themes Used In:** Ontology Alignment and Matching, Upper and Foundational Ontologies.
*   Ontology Alignment and Matching: To avoid the massive memory costs of $O(n^2)$ string comparisons, efficient matching systems like AgreementMakerLight (AML) rely heavily on external background knowledge ontologies (like UBERON) to act as semantic mediators [12]. If two distinct source and target concepts both map to the same mediator class, the system successfully infers a correspondence between them [12]. 
*   Upper Ontologies: Foundational ontologies are explicitly designed to fulfill this mediating role across divergent datasets [13]. For example, the DOLCE+D&S Ultralite (DUL) upper ontology has been used extensively as a mediator to integrate and repair massive public data resources, fixing inconsistencies in DBpedia and reorganizing the lexical structure of WordNet [13].

## Permanent URIs and Semantic Stability
**Themes Used In:** Lifecycle/Versioning/Governance, Upper and Foundational Ontologies.
*   Lifecycle and Governance: To satisfy FAIR accessibility principles and prevent link rot, governance protocols require ontologies to use permanent proxy URIs (such as `w3id.org` or `purl.org`) rather than institutional server addresses [14]. Furthermore, semantic versioning rules dictate that this core Ontology URI must remain permanently stable across updates, while distinct `owl:versionIRI` identifiers are minted for each new release to prevent downstream instance data from breaking [15].
*   Upper Ontologies: Modern enterprise ontologies actively implement these governance protocols; for instance, the *gist* upper ontology exclusively utilizes the `w3id.org` namespace to guarantee that its term IRIs remain stable and persistent regardless of how the developers' internal hosting arrangements change [16].


[^3]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^4]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^5]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^6]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]


[^9]: [[sources/Ontology design: Best practices • Palantir]]
[^10]: [[sources/Ontology design: Best practices • Palantir]]


[^13]: [[sources/[2308.01597] DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering]]


[^16]: [[sources/GitHub - semanticarts/gist: Semantic Arts gist upper enterprise ontology · GitHub]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]] [^8]: [[sources/web-1995-01-01-faa]] [^9]: [[sources/web-1995-01-01-faa]] [^10]: [[sources/web-1995-01-01-faa]] [^11]: [[sources/web-1995-01-01-faa]] [^12]: [[sources/web-1995-01-01-faa]] [^13]: [[sources/web-1995-01-01-faa]] [^14]: [[sources/web-1995-01-01-faa]] [^15]: [[sources/web-1995-01-01-faa]] [^16]: [[sources/web-1995-01-01-faa]]

### Shared Anchors

Based on the provided sources, several primary standards, methodologies, and datasets serve as foundational anchors that recur across multiple sub-domains of ontology engineering.

## Basic Formal Ontology (BFO) and the ISO/IEC 21838 Standard
**What it is and what it contains:**
BFO is a domain-neutral, realist top-level ontology that divides entities strictly into continuants (objects/qualities that endure) and occurrents (processes that unfold in time) [1, 2]. It is formally standardized as ISO/IEC 21838-2, which requires the ontology to be axiomatized in First-Order Logic and proven capable of covering maximal, domain-general data [1, 3].

**Themes Used In:**
*   Upper and Foundational Ontologies
*   Modularization and Architecture

**Why it is treated as foundational or load-bearing for those themes:**
In the context of "Upper and Foundational Ontologies," BFO is treated as the gold standard for scientific and realist modeling, actively rejecting concepts that only exist "in people's heads" in favor of strict empirical reality [1, 4]. Because it enforces a strict monohierarchy (where every node has at most one asserted parent), it provides the rigid scaffolding required for "Modularization and Architecture" [4, 5]. It acts as the ultimate "hub" in the hub-and-spokes architecture advocated by the OBO Foundry, allowing disparate domain experts to build specialized, non-overlapping application ontologies (the "spokes") that successfully interoperate because they share BFO's top-level logic [1, 4].

## The W3C Web Ontology Language (OWL) and RDF Specifications
**What it is and what it contains:**
The Resource Description Framework (RDF) and Web Ontology Language (OWL) are the formal W3C standards that define the syntax, description logic, and metadata properties used to represent knowledge graphs and ontologies on the Semantic Web [6, 7].

**Themes Used In:**
*   Ontology Design Patterns and Anti-Patterns
*   Ontology Alignment and Matching
*   Lifecycle, Versioning, and Governance

**Why it is foundational or load-bearing for those themes:**
These standards dictate the hard technical constraints that shape how practitioners design and evaluate models. In "Ontology Design Patterns," the computational limits of OWL reasoners (such as Pellet) dictate strategy; developers must avoid using `owl:someValuesFrom` (existential restrictions) on classes because it causes severe performance bottlenecks compared to defining new subproperties [8]. In "Ontology Alignment and Matching," the structural limitations of RDF—specifically its inability to natively support $n$-ary relationships—force developers to model complex relationships (like pharmacogenomic drug-gene-phenotype interactions) as reified, label-less blank nodes, which causes traditional string-matching systems to fail entirely [9, 10]. Finally, in "Lifecycle, Versioning, and Governance," OWL metadata properties such as `owl:versionIRI`, `owl:priorVersion`, and `owl:deprecated` provide the exact formal mechanisms practitioners must use to implement backwards-compatible semantic versioning [7, 11].

## The OAEI Anatomy and Conference Benchmarks
**What it is and what it contains:**
These are standardized test sets and reference alignments maintained by the Ontology Alignment Evaluation Initiative [12, 13]. The Anatomy track contains two biomedical ontologies (Adult Mouse Anatomy and NCI Thesaurus) alongside a manually curated reference alignment, while the Conference track contains a suite of moderately expressive ontologies detailing the organization of academic conferences [10, 14].

**Themes Used In:**
*   Ontology Alignment and Matching
*   Modularization and Architecture

**Why it is foundational or load-bearing for those themes:**
These datasets provide the universally accepted baseline for evaluating algorithmic performance. In "Ontology Alignment and Matching," the Anatomy and Conference datasets are the primary arenas where systems like AgreementMakerLight, LogMap, and Matcha prove their precision, recall, and F-measure, pushing the field to optimize hashing techniques or integrate Large Language Models (LLMs) to beat historic baselines [10, 15]. Beyond alignment, these datasets are repurposed in "Modularization and Architecture" research; for instance, the Conference dataset is used as a standard corpus to evaluate whether automated community detection algorithms can successfully extract distinct conceptual modules and Ontology Design Patterns from overlapping schemas [16].

## The NeOn Methodology and eXtreme Design (XD)
**What it is and what it contains:**
The NeOn Methodology is a scenario-based framework for collaboratively building ontology networks by reusing and re-engineering existing resources [17]. eXtreme Design (XD) is an agile, test-driven subset of this methodology that adapts practices from software engineering (like eXtreme Programming) directly to ontology development [18, 19].

**Themes Used In:**
*   Methodologies and Requirements Specification
*   Ontology Design Patterns and Anti-Patterns

**Why it is foundational or load-bearing for those themes:**
NeOn shifts the paradigm of "Methodologies" away from building ontologies from scratch, providing nine specific scenarios to guide practitioners in reusing non-ontological resources, localizing requirements, and mapping domains [17, 20]. eXtreme Design serves as the active engine for "Ontology Design Patterns and Anti-Patterns" by defining the exact workflow for integrating Content Ontology Design Patterns (CODPs) [18]. It provides the guided tools necessary to step non-experts through specializing leaf classes and properties safely, significantly lowering the introduction of logical inconsistencies and anti-patterns [18, 19].

## The FAIR Data Principles
**What it is and what it contains:**
The FAIR principles are high-level guidelines stipulating that scientific data and digital artifacts must be Findable, Accessible, Interoperable, and Reusable by both humans and machines [6, 21].

**Themes Used In:**
*   Lifecycle, Versioning, and Governance
*   Methodologies and Requirements Specification

**Why it is foundational or load-bearing for those themes:**
The FAIR principles shift the engineering focus from local ontology design to long-term web infrastructure. In "Lifecycle, Versioning, and Governance," the FAIR mandate for "Accessibility" and "Findability" requires practitioners to abandon institutional URLs in favor of permanent proxy namespaces (like `w3id.org`), to deploy HTTP 303 redirects so that raw RDF and human-readable HTML can be served from the same URI, and to register their schemas in public catalogues [6, 22]. In "Methodologies and Requirements Specification," FAIR provides the ultimate set of requirements that end-to-end continuous integration platforms (like OnToology) are built to satisfy [6, 23].

[^1]: [[sources/Basic Formal Ontology Tutorial (2025)]]


[^4]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^5]: [[sources/Basic Formal Ontology Tutorial (2025)]]






[^12]: [[sources/Ontology Alignment Evaluation Initiative::2025]]
[^13]: [[sources/Results of the Ontology Alignment Evaluation Initiative 2025. - Welcome to DTU Research Database]]
[^14]: [[sources/Ontology Alignment Evaluation Initiative::2025]]

[^16]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^17]: [[sources/The NeOn Methodology]]

[^19]: [[sources/[2206.02485] Automatically Drafting Ontologies from Competency Questions with FrODO]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]] [^8]: [[sources/web-1995-01-01-faa]] [^9]: [[sources/web-1995-01-01-faa]] [^10]: [[sources/web-1995-01-01-faa]] [^11]: [[sources/web-1995-01-01-faa]] [^12]: [[sources/web-1995-01-01-faa]] [^13]: [[sources/web-1995-01-01-faa]] [^14]: [[sources/web-1995-01-01-faa]] [^15]: [[sources/web-1995-01-01-faa]] [^16]: [[sources/web-1995-01-01-faa]] [^17]: [[sources/web-1995-01-01-faa]] [^18]: [[sources/web-1995-01-01-faa]] [^19]: [[sources/web-1995-01-01-faa]] [^20]: [[sources/web-1995-01-01-faa]] [^21]: [[sources/web-1995-01-01-faa]] [^22]: [[sources/web-1995-01-01-faa]] [^23]: [[sources/web-1995-01-01-faa]]

### Recurring Tradeoffs

Based on the provided sources, several recurring trade-offs and tensions emerge across the various themes of ontology engineering.

## Computational Performance vs. Modeling Simplicity
Based on the provided sources, a recurring tension exists between structuring ontologies for efficient machine reasoning and structuring them for straightforward data integration.
*   **Themes Used In:** Ontology Design Patterns, Ontology Alignment and Matching.
*   In Ontology Design Pattern (ODP) specialization, practitioners must choose between a class-oriented strategy and a property-oriented strategy [1, 2]. The class-oriented strategy favors simple data integration by reusing existing ODP object properties and applying local existential restrictions to classes [3, 4]. However, this severely degrades reasoner performance due to the computational burden of processing multiple existential quantifications [4]. In contrast, the property-oriented strategy requires creating entirely new subproperties with specific domains and ranges, which is less intuitive for data integration but drastically improves realization speeds in OWL reasoners [5-7]. 
*   In Ontology Alignment, this trade-off manifests in the selection of matching algorithms [8, 9]. Exhaustive pairwise matching compares every source concept to every target concept in $O(n^2)$ time, which allows for deep structural and string similarity metrics but hits severe memory bottlenecks on large biomedical ontologies [8, 10, 11]. To scale, systems like AgreementMakerLight (AML) trade exhaustive comparison for speed by using hash-based primary matchers that execute in $O(n)$ time [8, 10, 11]. This relies on inverted indices to achieve high scalability, but risks missing complex non-literal matches unless secondary, computationally heavy algorithms are specifically targeted at the vicinity of already mapped classes [8, 10, 11].

## Formal Rigor vs. Enterprise Pragmatism
Based on the provided sources, a fundamental conflict emerges between adhering to strict philosophical or logical formalisms and deploying pragmatic, functional models in rapid enterprise environments.
*   **Themes Used In:** Upper and Foundational Ontologies, Modularization and Architecture, Lifecycle and Governance.
*   In the realm of upper ontologies, the Basic Formal Ontology (BFO) enforces a strict realist metaphysics, demanding that ontologies only represent entities that actually exist in the physical world [12, 13]. This creates a severe tension for enterprise engineers who need to model "dummy instances" of unbuilt engineering designs, simulations, or alternative conceptual blueprints [14-17]. BFO proponents argue that modeling unbuilt designs as instances puts "falsehoods in the mouths of engineers," requiring practitioners to rely instead on complex intersections of types [13, 18]. Conversely, enterprise-focused upper ontologies like *gist* completely discard this academic philosophy, intentionally avoiding complex abstractions to provide a minimalist framework using everyday business language [19, 20].
*   This tension extends to architecture and lifecycle governance [21]. While academic standards advocate for formal perfection and strict backwards compatibility, enterprise guidelines explicitly embrace accepting technical debt [21]. Palantir's best practices state that a "slightly imperfect Ontology that is in use and generating value is better than a theoretically perfect one that is still being designed," urging engineers to cut corners on implementation details if necessary to meet immediate production deadlines [21].

## Manual Expert Curation vs. Automated Extraction
Based on the provided sources, ontology engineers continuously balance the high semantic quality of manual human modeling against the scalability of automated generation methods.
*   **Themes Used In:** Methodologies and Requirements Specification, Modularization.
*   When specifying requirements, manually defining Competency Questions (CQs) ensures high-quality scoping and stakeholder communication, but it is intensely labor-consuming and subject to severe time constraints [22-24]. To alleviate this bottleneck, researchers have introduced Retrieval-Augmented Generation (RAG) pipelines that use Large Language Models (LLMs) to automatically draft CQs from domain literature [25]. While automation accelerates the process, it introduces new risks, such as LLM hallucinations and decreased precision when dealing with highly abstract foundational ontologies compared to manual or zero-shot expert drafting [26-28].
*   Similarly, in modularization, manual Domain-Driven Design produces intuitive, semantically pure object types that avoid the "Kitchen Sink" anti-pattern of mirroring source databases [29-31]. However, manually curating these boundaries across massive, legacy enterprise systems is often unfeasible [32, 33]. To automate this, researchers apply community detection algorithms to intentional graphs to reverse-engineer and extract ontology design patterns from existing data [34]. The trade-off is that this automated extraction blindly relies on the existing logical topology; if the original ontology suffers from poor axiomatization, the automated algorithm produces "bad" semantic communities lacking conceptual unity [35, 36].

## Hierarchical Deep Modeling vs. Flat Compositional Extensibility
Based on the provided sources, practitioners must choose between rigid, centralized hierarchies and flexible, compositional architectures when scaling ontologies.
*   **Themes Used In:** Modularization and Architecture, Ontology Design Patterns and Anti-Patterns.
*   In standard ontology development, engineers often default to creating deep single-inheritance taxonomic chains to merge concepts, creating combination entities like `SchedulableBuilding` [37, 38]. While this tightly binds properties to specific classes, it results in a combinatorial explosion of brittle types that cannot be easily extended [38].
*   To combat this, architectural best practices mandate "composition over deep hierarchies" [37, 39]. This approach flattens the model by using focused interfaces (e.g., `Inspectable` or `Schedulable`) and relying on multiple inheritance [37, 39]. This trade-off sacrifices the simplicity of a single unified tree for a modular architecture that remains closed to core modification but open for continuous extension [39-41]. A workflow built to target a compositional interface can operate on entirely disparate real-world objects seamlessly, without requiring changes to the core object types [39].

[^3]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^6]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^31]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^32]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^84]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^102]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^103]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^114]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^115]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^116]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^117]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^166]: [[sources/GitHub - semanticarts/gist: Semantic Arts gist upper enterprise ontology · GitHub]]
[^169]: [[sources/GitHub - semanticarts/gist: Semantic Arts gist upper enterprise ontology · GitHub]]
[^191]: [[sources/Ontology design: Best practices • Palantir]]
[^192]: [[sources/Ontology design: Best practices • Palantir]]
[^194]: [[sources/Ontology design: Best practices • Palantir]]
[^197]: [[sources/Ontology design: Best practices • Palantir]]
[^199]: [[sources/Ontology design: Best practices • Palantir]]
[^200]: [[sources/Ontology design: Best practices • Palantir]]
[^201]: [[sources/Ontology design: Best practices • Palantir]]
[^202]: [[sources/Ontology design: Best practices • Palantir]]
[^203]: [[sources/Ontology design: Best practices • Palantir]]
[^217]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^218]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^222]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^225]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^226]: [[sources/STLab Seminar - Extraction of common conceptual components from multiple ontologies]]
[^335]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]

[^1]: [[sources/web-2026-06-17-3f8]] [^2]: [[sources/web-2026-06-17-3f8]] [^3]: [[sources/web-2026-06-17-3f8]] [^4]: [[sources/web-2026-06-17-3f8]] [^5]: [[sources/web-2026-06-17-3f8]] [^6]: [[sources/web-2026-06-17-3f8]] [^7]: [[sources/web-2026-06-17-3f8]] [^8]: [[sources/web-2026-06-17-e24]] [^9]: [[sources/web-2026-06-17-e24]] [^10]: [[sources/web-2026-06-17-e24]] [^11]: [[sources/web-2026-06-17-e24]] [^12]: [[sources/yt-GWkk5AfRCpM]] [^13]: [[sources/yt-GWkk5AfRCpM]] [^14]: [[sources/yt-GWkk5AfRCpM]] [^15]: [[sources/yt-GWkk5AfRCpM]] [^16]: [[sources/yt-GWkk5AfRCpM]] [^17]: [[sources/yt-GWkk5AfRCpM]] [^18]: [[sources/yt-GWkk5AfRCpM]] [^19]: [[sources/web-2017-05-19-0ff]] [^20]: [[sources/web-2017-05-19-0ff]] [^21]: [[sources/web-2021-12-14-47f]] [^22]: [[sources/web-2026-06-17-1b0]] [^23]: [[sources/web-2026-06-17-1b0]] [^24]: [[sources/web-2026-06-17-1b0]] [^25]: [[sources/arxiv-2409.08820]] [^26]: [[sources/web-1995-01-01-faa]] [^27]: [[sources/web-1995-01-01-faa]] [^28]: [[sources/web-1995-01-01-faa]] [^29]: [[sources/web-2021-12-14-47f]] [^30]: [[sources/web-2021-12-14-47f]] [^31]: [[sources/web-2021-12-14-47f]] [^32]: [[sources/yt-dyw0VgSrs2A]] [^33]: [[sources/yt-dyw0VgSrs2A]] [^34]: [[sources/yt-dyw0VgSrs2A]] [^35]: [[sources/yt-dyw0VgSrs2A]] [^36]: [[sources/yt-dyw0VgSrs2A]] [^37]: [[sources/web-2021-12-14-47f]] [^38]: [[sources/web-2021-12-14-47f]] [^39]: [[sources/web-2021-12-14-47f]] [^40]: [[sources/web-2021-12-14-47f]] [^41]: [[sources/web-2021-12-14-47f]]

## Sources cited

- [[sources/web-1995-01-01-faa]]
- [[sources/web-2026-06-17-3f8]]
- [[sources/web-2026-06-17-e24]]
- [[sources/yt-GWkk5AfRCpM]]
- [[sources/web-2017-05-19-0ff]]
- [[sources/web-2021-12-14-47f]]
- [[sources/web-2026-06-17-1b0]]
- [[sources/arxiv-2409.08820]]
- [[sources/yt-dyw0VgSrs2A]]

## Included works

- [[synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-lifecycle-versioning-and-]]
- [[synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-methodologies-and-require]]
- [[synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-modularization-and-archit]]
- [[synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-ontology-alignment-and-ma]]
- [[synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-ontology-design-patterns-]]
- [[synthesis/2026-06-17-how-do-practitioners-engineer-ontologies-at-upper-and-foundational-on]]
