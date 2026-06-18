---
schema_version: 1
type: synthesis
slug: 2026-06-17-how-do-practitioners-engineer-ontologies-at-upper-and-foundational-on
title: Upper and Foundational Ontologies — investigation (2026-06-17-how-do-practitioners-engineer-ontologies-at)
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
- sources/web-2026-06-17-2bb
- sources/yt-GWkk5AfRCpM
- sources/yt-joC4NZgLtqA
last_updated: '2026-06-17T20:07:21Z'
sources_count: 8
draft: true
draft_started_at: '2026-06-17T20:07:21Z'
draft_unresolved_claims: 15
---
# Upper and Foundational Ontologies — investigation

**Origin question:** How do practitioners engineer ontologies at production quality? Cover: established methodologies (METHONTOLOGY, NeOn, SAMOD, agile and competency-question-driven design); ontology design patterns (content patterns, logical patterns, the ODP catalog) and anti-patterns; modularization and ontology reuse; ontology alignment and matching (techniques, the OAEI evaluation campaigns, precision and recall tradeoffs); upper and foundational ontologies (BFO, DOLCE, SUMO, gist) and when to commit to one; and ontology lifecycle, versioning, and governance. Include foundational methodology papers, the ontology-design-pattern literature, OAEI results, and current engineering practice.
**Session:** 2026-06-17-how-do-practitioners-engineer-ontologies-at
**Branch:** Upper and Foundational Ontologies

## Synthesis

### Specifics

Based on the provided sources, several distinct foundational ontologies and standardization frameworks emerge, each offering a different paradigm for establishing semantic interoperability.

## BFO (Basic Formal Ontology) and Realist Metaphysics
BFO represents a top-level ontology engineered to enforce strict realist principles across scientific domains, particularly within biology and biomedicine.
*   **Name and Key Claim**: Basic Formal Ontology (BFO) claims that a successful upper ontology must track reality (what actually exists in the physical world) rather than concepts (what exists in people's heads or language) [1]. 
*   **Core Approach**: BFO strictly divides the world into two mutually exclusive categories: *continuants* (entities that endure over time, such as objects and qualities) and *occurrents* (entities that unfold in time, such as processes) [1, 2]. It mandates a strict monohierarchy (where every node has at most one asserted parent) and dictates that every term in an ontology must be a singular noun or noun phrase to ensure that terms represent true universals [1, 2].
*   **Concrete Details**: BFO is extremely small and avoids domain-specific terms completely [3]. It serves as the top-level "hub" for the OBO Foundry and over 300 other ontology projects globally, providing an architecture where domain-specific reference ontologies (the "spokes", such as the Protein Ontology) can be built concurrently by different expert groups without overlapping [1, 3]. 

## DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering)
DOLCE provides an alternative foundational paradigm driven by human cognition, language, and social practices rather than strict physical realism.
*   **Name and Key Claim**: DOLCE is a foundational ontology based on descriptive metaphysics, aiming to model a commonsense view of reality as it is perceived and exploited in everyday human practices [4].
*   **Core Approach**: Rather than claiming to represent strict physical reality, DOLCE treats universals as "conceptual containers" [3]. It relies heavily on the OntoClean methodology for evaluating the meta-properties of classes, and it employs "quality spaces" based on Gärdenfors' conceptual spaces [5].
*   **Concrete Details**: To bridge the gap between heavy first-order logic and Semantic Web applications, practitioners developed DOLCE+D&S Ultralite (DUL), an OWL-oriented version that provides a lighter axiomatization and more intuitive terminology (e.g., using "Object" and "Event" instead of "Endurant" and "Perdurant") [5]. DUL has been used practically to reorganize the WordNet top-level lexicon and to find and fix millions of hidden inconsistencies within the DBpedia knowledge graph [5].

## SUMO (Suggested Upper Merged Ontology)
SUMO takes a fundamentally different structural approach by prioritizing massive size and extensive domain coverage.
*   **Name and Key Claim**: The Suggested Upper Merged Ontology (SUMO) acts as a comprehensive starter document and foundation, originally proposed by the IEEE Standard Upper Ontology Working Group [6].
*   **Core Approach**: Instead of remaining strictly top-level and domain-neutral, SUMO merges various existing ontologies into a single massive structure, effectively bridging abstract foundational concepts with specific domain vocabulary [3, 6].
*   **Concrete Details**: SUMO contains thousands of terms, making it significantly larger than both BFO and DOLCE [3]. Because of this size, it incorporates specific, everyday domain concepts such as "fruit", "vegetable", and "body covering" directly into the upper ontology structure [3].

## The gist Enterprise Upper Ontology
For corporate and industrial environments, minimalist upper ontologies discard academic philosophy in favor of practical business applications.
*   **Name and Key Claim**: Semantic Arts' *gist* is a minimalist upper ontology that claims to provide maximum coverage of typical enterprise business concepts with the fewest number of primitives and the least ambiguity [7].
*   **Core Approach**: Unlike BFO or DOLCE, *gist* deliberately avoids complex philosophical abstractions (such as endurant, perdurant, or qualia) in favor of accessible, everyday business language like *person*, *organization*, and *agreement* [7]. To reduce cognitive load and redundancy for enterprise developers, it uses domain and range specifications sparingly and completely avoids defining inverse properties [7].
*   **Concrete Details**: The ontology defines approximately 100 classes and 100 properties [7]. To ensure stability in production systems, *gist* utilizes permanent, stable identifiers within the `w3id.org` domain (e.g., `https://w3id.org/semanticarts/ns/ontology/gist/`) [7].

## ISO/IEC 21838 Standardization for Top-Level Ontologies
The community has formalized what technically qualifies as a top-level ontology through rigorous international standards.
*   **Name and Key Claim**: The ISO/IEC 21838 standard establishes the strict formal criteria that a semantic framework must meet to be officially recognized and utilized as a top-level ontology [1].
*   **Core Approach**: The standard demands rigorous mathematical formalization, requiring that the ontology not only provide textual definitions and an OWL2 axiomatization, but also a full First-Order Logic (FOL) axiomatization [1]. 
*   **Concrete Details**: To prove it satisfies the standard's requirement for "maximal generality" (meaning it covers everything that exists), an ontology must successfully demonstrate how it handles data across 12 distinct domains [1]. BFO has successfully met these requirements and is formally recognized as the ISO/IEC 21838-2 standard, while DOLCE is also being integrated into the standard [1, 5].

[^1]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^2]: [[sources/Building Ontologies with Basic Formal Ontology]]

[^4]: [[sources/[2308.01597] DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering]]

[^6]: [[sources/Towards a standard upper ontology | Proceedings of the international conference on Formal Ontology in Information Systems - Volume 2001]]
[^7]: [[sources/GitHub - semanticarts/gist: Semantic Arts gist upper enterprise ontology · GitHub]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]]

### Comparisons

Based on the provided sources, several distinct comparisons emerge regarding the philosophical underpinnings, structural sizes, and intended application contexts of upper and foundational ontologies.

## Realist Metaphysics vs. Descriptive Metaphysics
When selecting a foundational ontology, practitioners must choose between modeling the physical world as it objectively exists versus modeling the world as human beings cognitively perceive and talk about it.
*   **Items Compared:** Basic Formal Ontology (BFO) vs. Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE).
*   **Differences in Evidence, Outcomes, or Stated Claims:** BFO explicitly claims to be a realist ontology that tracks physical reality, strictly dividing the world into continuants (entities that endure, like objects) and occurrents (entities that happen, like processes) [1, 2]. It refuses to model what "goes on in people's heads" or fictional entities, asserting that its universals are the kinds of things empirical scientists study [3, 4]. Conversely, DOLCE is rooted in descriptive metaphysics, aiming to capture human commonsense, linguistic categories, and social practices [5]. It treats universals as "conceptual containers" rather than strict physical realities, allowing it to seamlessly model cultural and cognitive constructs without drawing a hard line between physical reality and myth [6, 7].
*   **Trade-offs or Contexts:** BFO is specifically tailored for the hard sciences, such as biology, biomedicine, and manufacturing, where capturing objective, material truth is paramount to the domain [8, 9]. DOLCE is highly suited for socio-technical systems, legal domains, financial transactions, and cultural heritage, where human perception, language, and social roles define the environment [5, 10]. 
*   **Strengths and Weaknesses:** A major strength of BFO is its massive, active user base (such as the OBO Foundry) and an extensive product-service support system that provides expert consultation and documentation for its users [11, 12]. A core strength of DOLCE is its ability to map easily to linguistic and lexical resources; for example, it has been successfully used to reorganize the top level of WordNet and fix millions of inconsistencies in DBpedia [5, 13]. However, from the perspective of BFO's advocates, DOLCE's weakness is that it lacks a dedicated service support infrastructure for ontology developers, and its focus on language means it diverges from the strict empirical needs of hard scientists [12, 14].

## Foundational Minimalism vs. Domain Expansion
Practitioners must balance the desire for a small, easily learned foundation against the convenience of having thousands of pre-built, domain-specific concepts readily available.
*   **Items Compared:** BFO and DOLCE vs. Suggested Upper Merged Ontology (SUMO).
*   **Differences in Evidence, Outcomes, or Stated Claims:** Both BFO and DOLCE are extremely small, strictly top-level ontologies that deliberately avoid including domain-specific terms [15, 16]. In stark contrast, SUMO is a massive starter document created by merging several existing ontologies [17]. It bridges high-level abstractions with specific domain vocabulary, directly incorporating thousands of everyday terms like "fruit", "vegetable", and "body covering" [15, 17].
*   **Trade-offs or Contexts:** BFO and DOLCE function strictly as abstract "hubs" in a hub-and-spokes architecture, requiring domain experts to build out the specialized "spokes" (e.g., a specific Protein Ontology or Event ontology) [18]. SUMO applies in contexts where developers want a comprehensive, all-in-one foundation that already provides substantial mid-level and domain-level vocabulary [17]. 
*   **Strengths and Weaknesses:** The strength of the minimalist approach (BFO/DOLCE) is that the ontologies are highly structured and easier to learn, allowing a cadre of developers to apply them repeatedly and consistently across widely different projects [15]. The weakness of SUMO is its massive size; because it contains thousands of terms, the corpus notes it is much harder for developers to learn and apply properly [15].

## Academic Rigor vs. Enterprise Pragmatism
There is a sharp divide between the rigorous philosophical formalisms required by international standards and the practical simplicity demanded by corporate software developers.
*   **Items Compared:** BFO and DOLCE vs. *gist* Enterprise Upper Ontology.
*   **Differences in Evidence, Outcomes, or Stated Claims:** BFO and DOLCE rely heavily on complex philosophical and metaphysical abstractions, employing terms such as "endurant", "perdurant", "continuant", and "qualia" [2, 5, 19]. The *gist* upper ontology is deliberately minimalist and explicitly eschews these philosophical abstractions [19, 20]. Instead, it relies on everyday, accessible business language, utilizing ordinary concepts like "person", "organization", and "agreement" to build its models [19, 20]. 
*   **Trade-offs or Contexts:** BFO and DOLCE are utilized in academic, scientific, and highly standardized environments. BFO, for instance, complies with the rigorous ISO/IEC 21838 standard, which requires First-Order Logic axiomatization and proofs of "maximal generality" across diverse data domains [21, 22]. *gist* applies directly to enterprise information systems, corporate data governance, and business intelligence, where rapid adoption by developers and straightforward semantic clarity are preferred over deep metaphysical perfection [20, 23].
*   **Strengths and Weaknesses:** The strength of BFO and DOLCE is their mathematical rigor and standardized validation, ensuring profound semantic interoperability for complex domains [5, 21]. Their weakness in a business context is the steep cognitive load and unfamiliar terminology imposed on enterprise developers [19, 20]. The strength of *gist* is its high practical expressiveness combined with minimal ambiguity; by defining only around 100 classes and 100 properties, it provides a lightweight semantic foundation that seamlessly integrates into existing corporate systems [20, 23].

[^1]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^2]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^3]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^4]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^5]: [[sources/[2308.01597] DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering]]
[^6]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^7]: [[sources/[2308.01597] DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering]]
[^8]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^9]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^10]: [[sources/[2308.01597] DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering]]
[^11]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^12]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^13]: [[sources/[2308.01597] DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering]]
[^14]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^15]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^16]: [[sources/[2308.01597] DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering]]
[^17]: [[sources/Towards a standard upper ontology | Proceedings of the international conference on Formal Ontology in Information Systems - Volume 2001]]
[^18]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^19]: [[sources/GitHub - semanticarts/gist: Semantic Arts gist upper enterprise ontology · GitHub]]
[^20]: [[sources/GitHub - semanticarts/gist: Semantic Arts gist upper enterprise ontology · GitHub]]
[^21]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^22]: [[sources/Basic Formal Ontology Tutorial (2025)]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]] [^8]: [[sources/web-1995-01-01-faa]] [^9]: [[sources/web-1995-01-01-faa]] [^10]: [[sources/web-1995-01-01-faa]] [^11]: [[sources/web-1995-01-01-faa]] [^12]: [[sources/web-1995-01-01-faa]] [^13]: [[sources/web-1995-01-01-faa]] [^14]: [[sources/web-1995-01-01-faa]] [^15]: [[sources/web-1995-01-01-faa]] [^16]: [[sources/web-1995-01-01-faa]] [^17]: [[sources/web-1995-01-01-faa]] [^18]: [[sources/web-1995-01-01-faa]] [^19]: [[sources/web-1995-01-01-faa]] [^20]: [[sources/web-1995-01-01-faa]] [^21]: [[sources/web-1995-01-01-faa]] [^22]: [[sources/web-1995-01-01-faa]] [^23]: [[sources/web-1995-01-01-faa]]

### Gaps

Based on the provided sources, several limitations, gaps, and unanswered tensions emerge regarding the application and completeness of upper and foundational ontologies, particularly concerning the Basic Formal Ontology (BFO).

## The Representation of Liquids and Amorphous Matter
The corpus reveals a known architectural gap in how BFO categorizes material entities, specifically regarding mass nouns and substances that lack solid boundaries.
*   **The Gap:** BFO formally divides material entities into three categories: objects, fiat object parts, and object aggregates [1, 2]. However, the ontology currently lacks distinct native categories to represent liquids, gases, and plasmas [3, 4]. 
*   **Unresolved Questions:** The creators of BFO acknowledge that they "don't know where to put" items like ice cubes or portions of liquid, stating that a fourth or fifth category may be needed for plasmas and liquids [4]. While practitioners are currently instructed to place these entities under the broader `material entity` parent class, the literature notes that this is an unsatisfying workaround and that structural granularity for non-object matter remains an unresolved area of future work [4, 5].

## Identity Conditions for Information Artifacts
There is an unresolved philosophical and practical tension regarding how to track the identity of information over time within BFO's framework.
*   **The Tension:** BFO uses Generically Dependent Continuants (GDCs) and Information Content Entities (ICEs) to model patterns, documents, and data [6, 7]. However, tracking the provenance of a document as it matures requires knowing when a change creates a fundamentally new piece of information versus when it is merely a modification of an existing one [8, 9]. 
*   **Unanswered Questions:** A careful reader would note that the ontology creators admit they "don't have fully characterized identity conditions for GDCs" [9]. For example, the sources leave unanswered the question of whether changing a single word (like "to" to "a") in a document results in entirely new information or if the original GDC persists [10]. The creators suggest that while this is a fascinating philosophical question, BFO does not yet provide firm identity conditions or constraints to resolve it at the high-level modeling stage [11].

## The "Experimental" Handling of Process Measurements
BFO enforces a strict structural rule that prohibits assigning qualities to processes, creating a gap in how practitioners can natively record measurement data.
*   **The Gap:** In BFO, continuants (like objects) can have qualities (like mass or temperature), but occurrents (like processes) cannot have qualities because processes do not change in the same way objects do [12, 13]. This creates a problem for annotating process measurement data, such as a heart beating at 72 beats per minute, because BFO does not recognize a `process quality` category [12].
*   **Unresolved Questions:** To bypass this limitation, BFO 2.0 introduced the concept of "process profiles" (e.g., a "beat profile") to handle rate and speed measurements without violating the rule against process qualities [14]. However, the specification document explicitly states that this solution is "to be treated as experimental," leaving practitioners without a finalized, mathematically proven mechanism for representing process measurements [14]. 

## The Tension Between Realism and Unrealized Engineering Designs
A severe tension exists between BFO's commitment to strict realist metaphysics and the practical needs of enterprise engineers who model simulations, workflows, and unbuilt designs.
*   **The Tension:** Because BFO only models the reality that physically exists, it forbids the creation of "dummy instances" to represent products that are merely in the design phase and may never actually be manufactured [15-17]. Engineers argue that this makes it exceedingly difficult to query historical provenance, compare alternative conceptual designs, or reason about why one unbuilt methodology was chosen over another [18-21].
*   **Unanswered Questions:** BFO advocates instruct engineers to avoid "dummy instances" because they put "false words in the mouth of engineers" by asserting the existence of fictions [17, 22]. Instead, BFO requires using a complex intersection of ICEs, relational roles, and types that would be instantiated *if* the object were built [23, 24]. However, the corpus leaves open how enterprise practitioners can effectively implement these highly abstract, type-level workarounds into everyday engineering software, with domain experts noting that this strict realism creates a gap for those who just want to "log and collect stuff" seamlessly in their workflows [25].

[^90]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^92]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^106]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^107]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^111]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^112]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^113]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^115]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^117]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^118]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^119]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^120]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^121]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^122]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^123]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^125]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^127]: [[sources/Basic Formal Ontology Tutorial (2025)]]
[^157]: [[sources/Building Ontologies with Basic Formal Ontology]]
[^158]: [[sources/Building Ontologies with Basic Formal Ontology]]

[^1]: [[sources/web-2026-06-17-2bb]] [^2]: [[sources/web-2026-06-17-2bb]] [^3]: [[sources/yt-GWkk5AfRCpM]] [^4]: [[sources/yt-joC4NZgLtqA]] [^5]: [[sources/web-2026-06-17-2bb]] [^6]: [[sources/yt-GWkk5AfRCpM]] [^7]: [[sources/yt-joC4NZgLtqA]] [^8]: [[sources/yt-GWkk5AfRCpM]] [^9]: [[sources/yt-GWkk5AfRCpM]] [^10]: [[sources/yt-GWkk5AfRCpM]] [^11]: [[sources/yt-GWkk5AfRCpM]] [^12]: [[sources/web-2026-06-17-2bb]] [^13]: [[sources/web-2026-06-17-2bb]] [^14]: [[sources/web-2026-06-17-2bb]] [^15]: [[sources/yt-GWkk5AfRCpM]] [^16]: [[sources/yt-GWkk5AfRCpM]] [^17]: [[sources/yt-GWkk5AfRCpM]] [^18]: [[sources/yt-GWkk5AfRCpM]] [^19]: [[sources/yt-GWkk5AfRCpM]] [^20]: [[sources/yt-GWkk5AfRCpM]] [^21]: [[sources/yt-GWkk5AfRCpM]] [^22]: [[sources/yt-GWkk5AfRCpM]] [^23]: [[sources/yt-GWkk5AfRCpM]] [^24]: [[sources/yt-GWkk5AfRCpM]] [^25]: [[sources/yt-GWkk5AfRCpM]]

## Sources cited

- [[sources/web-1995-01-01-faa]]
- [[sources/web-2026-06-17-2bb]]
- [[sources/yt-GWkk5AfRCpM]]
- [[sources/yt-joC4NZgLtqA]]

## Included works

- [[sources/web-1995-01-01-faa]]
- [[sources/web-2026-06-17-2bb]]
- [[sources/yt-GWkk5AfRCpM]]
- [[sources/yt-joC4NZgLtqA]]
