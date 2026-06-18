---
schema_version: 1
type: synthesis
slug: 2026-06-17-how-do-practitioners-engineer-ontologies-at-methodologies-and-require
title: Methodologies and Requirements Specification — investigation (2026-06-17-how-do-practitioners-engineer-ontologies-at)
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
last_updated: '2026-06-17T20:07:19Z'
sources_count: 3
draft: true
draft_started_at: '2026-06-17T20:07:19Z'
draft_unresolved_claims: 13
---
# Methodologies and Requirements Specification — investigation

**Origin question:** How do practitioners engineer ontologies at production quality? Cover: established methodologies (METHONTOLOGY, NeOn, SAMOD, agile and competency-question-driven design); ontology design patterns (content patterns, logical patterns, the ODP catalog) and anti-patterns; modularization and ontology reuse; ontology alignment and matching (techniques, the OAEI evaluation campaigns, precision and recall tradeoffs); upper and foundational ontologies (BFO, DOLCE, SUMO, gist) and when to commit to one; and ontology lifecycle, versioning, and governance. Include foundational methodology papers, the ontology-design-pattern literature, OAEI results, and current engineering practice.
**Session:** 2026-06-17-how-do-practitioners-engineer-ontologies-at
**Branch:** Methodologies and Requirements Specification

## Synthesis

### Specifics

Based on the provided sources, several distinct methodologies and techniques emerge for structuring the ontology engineering process.

## METHONTOLOGY
METHONTOLOGY moves ontology development from an ad-hoc craft to an engineering discipline through a structured, evolving life cycle.
*   **Name and Key Claim**: METHONTOLOGY is a structured methodology for building ontologies from scratch that proposes an "evolving prototype" life cycle [1].
*   **Core Approach**: It divides the development process into defined activities—planify, specify, acquire knowledge, conceptualize, formalize, integrate, implement, evaluate, document, and maintain—allowing the ontologist to go back, modify, add, or remove definitions at any stage [1]. It recommends a "middle-out approach" to identify primary concepts before specializing or generalizing them [1].
*   **Concrete Details**: The methodology utilizes specific intermediate representations during the conceptualization phase, including a Glossary of Terms (GT), Data Dictionaries, Tables of Instance Attributes, and Concepts Classification Trees [1].

## The NeOn Methodology
The NeOn methodology shifts focus from building ontologies from scratch to leveraging existing resources in collaborative environments.
*   **Name and Key Claim**: The NeOn Methodology is a scenario-based framework for collaboratively building ontology networks, emphasizing the dynamic evolution and reuse of resources [2].
*   **Core Approach**: It provides methodological guidelines for reusing and re-engineering both ontological and non-ontological resources (NORs) [2].
*   **Concrete Details**: The framework defines exactly nine development scenarios, such as developing from scratch (Scenario 1), re-engineering non-ontological resources into ontologies (Scenario 2), reusing Ontology Design Patterns (Scenario 7), and localizing ontological resources into multiple languages (Scenario 9) [2].

## Ontology Development 101
Ontology Development 101 provides foundational guidelines for creating frame-based ontologies through iterative design.
*   **Name and Key Claim**: Ontology Development 101 offers a simple knowledge-engineering methodology built on the principle that there is no single correct way to model a domain [3].
*   **Core Approach**: The process is highly iterative, involving determining scope, enumerating terms, and choosing between top-down, bottom-up, or combination approaches for class hierarchy design [3]. It stresses the importance of separating domain knowledge from operational knowledge [3].
*   **Concrete Details**: It introduces the use of natural-language Competency Questions to sketch out and functionally test the ontology's scope [3]. It also advocates for strict naming conventions (e.g., Space, CamelCase, or Delimiters) to avoid modeling mistakes and maintain consistency across the team [3].

## Competency Question (CQ) Driven Design & Survey Findings
Recent surveys capture the real-world application, benefits, and hurdles of utilizing Competency Questions in practice.
*   **Name and Key Claim**: A 2023 survey of 63 ontology engineers evaluated the state of practice for Competency-Question-Driven Design, finding that while CQs are recognized as highly useful, their practical management remains difficult [4].
*   **Core Approach**: Practitioners primarily define CQs iteratively, starting with terminology closer to the domain users and gradually refining them to match the formal ontology terminology [4]. CQs are drafted to focus on both the universe of concepts and instances to guide domain modeling and ontology testing [4].
*   **Concrete Details**: The survey found that 90.5% of practitioners use CQs for requirements elicitation and 68.3% for verification and testing [4]. While 92.1% reported CQs help define scope, 77.8% struggled to ensure the CQs were necessary and sufficient [4]. 84.1% of respondents reported a lack of specialized tools to support CQ formulation, and 27% cited time constraints as the primary barrier to using them [4]. The most frequently adopted methodologies among respondents were SABiO (47.6%), METHONTOLOGY (25.4%), and NeOn (23.8%) [4].

## Automating CQ Generation via RAG & LLMs
Retrieval-Augmented Generation provides a modern mechanism to accelerate the extraction of Competency Questions directly from domain literature.
*   **Name and Key Claim**: A RAG-based approach for generating Competency Questions uses Large Language Models (LLMs) to automatically craft CQs from scientific papers, solving the labor-intensive bottleneck of manual CQ drafting [5].
*   **Core Approach**: Domain documents are chunked and embedded in a vector database, then retrieved to provide context to an LLM, allowing it to generate CQs based on up-to-date and specialized knowledge rather than existing knowledge graphs [5].
*   **Concrete Details**: Tested using GPT-4 on the KG-EmpiRE and HCIO datasets, researchers found that adding more domain papers ($N_{paper}$) to the RAG pipeline consistently improved precision over zero-shot prompting [5]. The system utilizes a zero-shot prompt template containing four configurable variables: domain name, purpose of the ontology, definition of CQs, and the desired number of CQs [5].

## FrODO (Frame-based Ontology Design Outlet)
FrODO automates the transition from informal natural-language requirements to formalized ontology drafts.
*   **Name and Key Claim**: FrODO is a novel method and tool that automatically drafts ontologies directly from Competency Questions [6].
*   **Core Approach**: It leverages frame semantics to process the Resource Description Framework (RDF) outputs produced by the FRED tool from natural-language CQs, drawing domain-relevant boundaries to generate ontology drafts [6].
*   **Concrete Details**: FrODO specifically supports agile ontology engineering methodologies, such as eXtreme Design (XD) and SAMOD [6]. A user-based study confirmed that the resulting ontology drafts are qualitative and effective for design tasks [6].

## Agile Methodologies (eXtreme Design / SAMOD)
The eXtreme Design methodology brings agile software engineering practices into the ontology design lifecycle.
*   **Name and Key Claim**: eXtreme Design (XD) is a collaborative, agile ontology development methodology based on the application and exploitation of Ontology Design Patterns (ODPs) [7].
*   **Core Approach**: Influenced by eXtreme Programming, XD emphasizes incremental development, continuous requirements management, test-driven development, and pair design in iterating loops [7].
*   **Concrete Details**: XD is heavily supported by the XD Tools plugin for the NeOn Toolkit, which provides a guided wizard for specializing ODPs [7]. The wizard steps users through specializing leaf classes, subproperties, and local domains/ranges, and validates the output by generating natural-language axioms for the user to approve or reject [7].

[^2]: [[sources/The NeOn Methodology]]


[^5]: [[sources/A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^6]: [[sources/[2206.02485] Automatically Drafting Ontologies from Competency Questions with FrODO]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]]

### Comparisons

Based on the provided sources, several distinct points of comparison emerge when evaluating how practitioners approach methodologies and requirements specification for ontology engineering.

## Lifecycle and Architectural Trade-offs
Established methodologies offer competing paradigms for structuring the ontology lifecycle, balancing the need for rigorous specification with the realities of distributed reuse and dynamic requirements.
*   **METHONTOLOGY vs. NeOn Methodology**: METHONTOLOGY is primarily designed to guide the construction of ontologies from scratch, employing an "evolving prototype" lifecycle that permits the inclusion, removal, or modification of definitions at any stage to avoid the rigidity of a waterfall model [1, 2]. In contrast, the NeOn Methodology operates on the premise that modern ontologies are rarely built in isolation; it utilizes a scenario-based framework containing nine distinct scenarios heavily focused on the collaborative reuse, merging, and re-engineering of existing ontological and non-ontological resources (NORs) [3, 4]. 
*   **Agile vs. Traditional Prototyping**: Agile methodologies, such as eXtreme Design (XD) and SAMOD, depart from both METHONTOLOGY and NeOn by borrowing directly from eXtreme Programming [5]. XD relies on continuous requirements management, test-driven development, and a divide-and-conquer strategy that explicitly centers on the rapid integration of reusable Ontology Design Patterns (ODPs) [5, 6]. While METHONTOLOGY treats knowledge acquisition and evaluation as support activities spanning the lifecycle [2], Agile methods enforce short, highly iterative loops tailored to rapidly changing environments where testing and refactoring are constant [5].

## Concept Elicitation Strategies
When initially defining the terms and scope of an ontology, frameworks diverge on the most effective cognitive approach for domain modeling.
*   **Middle-out vs. Developer Preference**: METHONTOLOGY strongly advocates for a "middle-out" approach, arguing that starting with the most salient primary concepts before generalizing or specializing yields more stable terms, requires less rework, and guarantees the conciseness of the specification document [7, 8]. The "Ontology Development 101" guide, conversely, claims there is no single correct way to model a domain and states that developers should freely choose between top-down, bottom-up, or middle-out strategies depending on their personal view of the domain [9, 10]. However, it concedes that the middle-out approach is frequently the easiest in practice, as middle-level concepts tend to be cognitively the most descriptive [10].

## Competency Question Generation and Management
Competency Questions (CQs) are universally recognized as a mechanism for scoping and evaluating ontologies, but approaches contrast sharply between manual engineering and automated generation.
*   **Manual Elicitation Strengths and Weaknesses**: A 2023 survey of ontology engineers confirms that manual CQ elicitation is highly effective for defining ontology scope (reported by 92.1% of respondents) and aiding in ontology evaluation (82.5%) [11]. However, practitioners face significant weaknesses with manual approaches: 27% of respondents cite severe time constraints as the primary barrier to using CQs, and 77.8% struggle to ensure their manually drafted CQs are both necessary and sufficient [12]. Furthermore, 84.1% of practitioners report operating without specialized tooling, relying instead on generic text editors or spreadsheets to manage CQs [13].
*   **Automated CQ Generation via RAG**: To address the manual bottleneck, researchers have proposed Retrieval-Augmented Generation (RAG) approaches that utilize Large Language Models (LLMs) to automatically draft CQs directly from domain literature [14, 15]. The trade-off in this approach relates to the abstraction level of the target domain [16]. For highly concrete ontologies (like those detailing specific requirements engineering methods), feeding scientific papers into a RAG pipeline significantly outperforms zero-shot LLM prompting because the task requires dense, up-to-date domain knowledge [16, 17]. Conversely, for highly abstract, foundational reference ontologies (such as core Human-Computer Interaction concepts), zero-shot prompting actually yields marginally higher precision than RAG, as the LLM's pre-trained knowledge is sufficient and less prone to the noise of retrieved documents [16, 17].
*   **From CQs to Formal Drafts**: While RAG targets the generation of informal CQs from text, the FrODO (Frame-based Ontology Design Outlet) framework addresses the subsequent transition from natural language questions to formal ontology models [18]. FrODO automates this transition by leveraging frame semantics to process RDF outputs derived from CQs, automatically drafting domain boundaries [18]. This tool is explicitly designed to offset the labor weaknesses of manual CQ formalization, directly supporting the rapid iteration required by Agile methodologies like XD and SAMOD [18].


[^3]: [[sources/The NeOn Methodology]]
[^4]: [[sources/The NeOn Methodology]]









[^14]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^15]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^16]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^17]: [[sources/[2409.08820] A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^18]: [[sources/[2206.02485] Automatically Drafting Ontologies from Competency Questions with FrODO]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]] [^5]: [[sources/web-1995-01-01-faa]] [^6]: [[sources/web-1995-01-01-faa]] [^7]: [[sources/web-1995-01-01-faa]] [^8]: [[sources/web-1995-01-01-faa]] [^9]: [[sources/web-1995-01-01-faa]] [^10]: [[sources/web-1995-01-01-faa]] [^11]: [[sources/web-1995-01-01-faa]] [^12]: [[sources/web-1995-01-01-faa]] [^13]: [[sources/web-1995-01-01-faa]] [^14]: [[sources/web-1995-01-01-faa]] [^15]: [[sources/web-1995-01-01-faa]] [^16]: [[sources/web-1995-01-01-faa]] [^17]: [[sources/web-1995-01-01-faa]] [^18]: [[sources/web-1995-01-01-faa]]

### Gaps

Based on the provided sources, several limitations, gaps, and unanswered tensions emerge regarding methodologies and requirements specification in ontology engineering.

## The Theory-Practice Gap in Competency Question (CQ) Definition
Although established methodologies prescribe the use of CQs, practitioners report that existing guidelines are insufficient to bridge the gap between theory and practice [1]. Because CQ definition relies heavily on the ontology engineer's tacit knowledge and experience, the process is fraught with subjectivity and bias [1]. A careful reader would want to know precisely *how* to guarantee that a defined set of CQs is both necessary and sufficient for the ontology, a challenge reported by 77.8% of surveyed practitioners [1]. Furthermore, the corpus does not provide standardized solutions for identifying CQs that truly represent the ontology's scope or for avoiding inconsistencies and redundancies among a large set of CQs [1].

## Lack of Specialized Tooling and Management Frameworks
While ontology implementation environments like Protégé exist, there is a severe absence of specialized tools dedicated specifically to requirements elicitation and CQ management [1]. The vast majority of surveyed practitioners (84.1%) rely on generic software like text editors or spreadsheets, which fail to support automated tasks such as grouping CQs, extracting candidate terms, or tracing requirements [1]. The sources leave unanswered how enterprise teams should systematically manage, version, and collaboratively edit requirements at scale [1].

## Tensions in Formalizing and Verifying Competency Questions
A significant tension exists between the informal natural language CQs understood by domain experts and the formal logic required by machines [1, 2]. While experimental frameworks like FrODO attempt to bridge this by automatically drafting ontology boundaries from CQs, the broader problem of translating informal CQs into formal queries (e.g., SPARQL-OWL) remains a recognized hurdle [2, 3]. The corpus lacks comprehensive strategies for the automatic checking of CQs against the implemented ontology, leaving practitioners to rely on labor-intensive manual verification [1].

## Limitations of LLM-Assisted CQ Generation
Recent attempts to automate CQ generation using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) introduce new unanswered questions. The proposed RAG pipelines rely on the premise that LLMs can act as domain experts when fed scientific papers, but researchers explicitly acknowledge the persistent risk of LLM hallucinations [2]. Additionally, the RAG experiments have only been evaluated on two specific tasks (KG-EmpiRE and HCIO) using a single closed-source model (GPT-4o), leaving a gap in understanding how these methods generalize across other domains or how they perform using open-source alternatives [2]. Finally, the approach raises unresolved questions about the financial token costs associated with processing large knowledge bases for enterprise-scale ontology engineering [2].

## Empirical Comparison of Divergent Methodologies
The literature presents diverse methodologies—ranging from the evolving prototypes of METHONTOLOGY to the collaborative scenarios of NeOn and the agile, pattern-driven frameworks like eXtreme Design—but fails to provide rigorous comparative evaluations. While surveys capture which methodologies are most popular in practice (e.g., SABiO and METHONTOLOGY), there is a gap in empirical guidance on *when* to choose a specific methodology based on project scale, domain complexity, or team expertise [1]. A careful reader would want an evidence-based framework to decide whether a top-down, middle-out, or agile approach is strictly optimal for their specific production constraints, rather than relying on the general sentiment that "there is no one correct way" to model a domain [1, 4].

[^2]: [[sources/A RAG Approach for Generating Competency Questions in Ontology Engineering]]
[^3]: [[sources/[2206.02485] Automatically Drafting Ontologies from Competency Questions with FrODO]]

[^1]: [[sources/web-1995-01-01-faa]] [^2]: [[sources/web-1995-01-01-faa]] [^3]: [[sources/web-1995-01-01-faa]] [^4]: [[sources/web-1995-01-01-faa]]

## Sources cited

- [[sources/web-1995-01-01-faa]]

## Included works

- [[sources/web-1995-01-01-faa]]
