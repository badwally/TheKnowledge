---
schema_version: 1
type: synthesis
slug: 2026-06-17-what-are-the-current-architecture-and-evaluation-of-agent-over-graph-
title: Evaluation of Agent-Over-Graph Systems — investigation (2026-06-17-what-are-the-current-architecture-and)
domains:
- agentic-data-layer
question: What are the current architecture and engineering patterns for AI agents
  that query, construct, and validate knowledge graphs and semantic data layers at
  runtime? Cover GraphRAG and knowledge-graph retrieval, text-to-query (SPARQL/Cypher),
  MCP and tool design over graph and triple-store backends, SHACL-constrained generation
  and validation, and evaluation of agent-over-graph systems.
created_at: '2026-06-17T21:29:50Z'
synthesizes:
- sources/web-2013-01-18-6fc
- sources/yt-S5ezVVJhQmE
last_updated: '2026-06-17T21:29:53Z'
sources_count: 6
draft: true
draft_started_at: '2026-06-17T21:29:53Z'
draft_unresolved_claims: 9
---
# Evaluation of Agent-Over-Graph Systems — investigation

**Origin question:** What are the current architecture and engineering patterns for AI agents that query, construct, and validate knowledge graphs and semantic data layers at runtime? Cover GraphRAG and knowledge-graph retrieval, text-to-query (SPARQL/Cypher), MCP and tool design over graph and triple-store backends, SHACL-constrained generation and validation, and evaluation of agent-over-graph systems.
**Session:** 2026-06-17-what-are-the-current-architecture-and
**Branch:** Evaluation of Agent-Over-Graph Systems

## Synthesis

### Specifics

## Evaluation of Agent-Over-Graph Systems

Based on the provided sources, several frameworks, benchmarks, and empirical phenomena emerge regarding the evaluation of agent-over-graph architectures, focusing on complex reasoning, faithfulness, and the interplay between parametric memory and retrieved context.

*   **Name and Key Claim:** RAGAS Evaluation of IoT Network Security (The Accuracy-Faithfulness Gap)
    *   **Core Approach:** Evaluates 30 human expert-validated IoT compliance scenarios against ETSI EN 303 645 provisions by comparing rule-based heuristic scoring, dense Vector RAG, and knowledge graph traversal (Graph RAG) using the Retrieval-Augmented Generation Assessment Suite (RAGAS) with an LLM-as-a-judge [1].
    *   **Concrete Details:** Graph RAG achieved the highest faithfulness (0.570) and near-perfect Context Precision (0.996) compared to Vector RAG (0.509 faithfulness, 0.856 precision) and rule-based retrieval (0.524 faithfulness, 0.814 precision) [2]. However, the evaluation exposed a severe "accuracy-faithfulness gap": despite the underlying intrusion detection system achieving an F1 score above 0.97, over 40% of the LLMs' generated compliance statements were hallucinated parametric knowledge completely unsupported by the retrieved graph context [3]. Furthermore, all retrieval methods suffered from low Context Recall (≤22.4%), indicating that flow-level network features inherently limit the total available evidence coverage regardless of the retrieval strategy [4].

*   **Name and Key Claim:** Spider4SPARQL Benchmark
    *   **Core Approach:** Addresses the simplicity of existing knowledge graph benchmarks (like LC-QuAD 1.0 and 2.0) by automatically translating the complex, multi-domain Spider Text-to-SQL dataset into SPARQL queries mapped against automatically generated ontologies using an Ontology-Based Data Access (OBDA) approach [5]. 
    *   **Concrete Details:** Spider4SPARQL contains 9,693 manually generated natural language questions and 4,721 unique, complex SPARQL queries spanning 138 domains (including queries with up to 3 aggregations and 5 subqueries) [6]. When evaluated against this complex benchmark, state-of-the-art models struggled heavily: T5-Small achieved 27% execution accuracy, T5-Base achieved 42%, and GPT-3.5 achieved only 8% in zero-shot and 45% (±4.41%) in 10-shot learning configurations [7]. This highlights a significant drop from the ~92% accuracy these same models achieve on simpler, pattern-based benchmarks [8].

*   **Name and Key Claim:** Federated KGQA (FKGQA) Benchmark
    *   **Core Approach:** Extends the Spider4SPARQL dataset specifically to test agentic federated querying by using horizontal, vertical, and class-based partitioning to distribute 19 datasets across 118 distinct database shards [9]. It tests an agent's ability to autonomously perform endpoint discovery and formulate distributed `SERVICE` subqueries [10].
    *   **Concrete Details:** High-capacity frontier models like GPT-5.2 achieved 42.1% to 45.4% accuracy, successfully discovering endpoints and generating valid syntax [11]. In contrast, smaller models like Qwen3-8B achieved only ~13% accuracy, suffering a 41.5% to 61.1% syntactic error rate [12]. The benchmark also measured "trivial queries" (where an agent blindly queries all available endpoints unnecessarily); it revealed that providing agents with simple, high-level natural language endpoint descriptions—rather than highly detailed VoID schema metadata—effectively reduced GPT-5.2's trivial query rate from 90.2% down to 11.0% [13].

*   **Name and Key Claim:** LLM-KG-Bench Framework
    *   **Core Approach:** An automated benchmarking framework that assesses out-of-the-box LLMs across four quantitative dimensions: SPARQL Syntax Fixing (SSF), Text-to-SPARQL (T2S), SPARQL-to-Answer (S2A), and Text-to-Answer (T2A) [14]. It executes a multi-turn feedback dialog loop where LLMs are given database runtime error messages to correct their queries across up to three iterations [15].
    *   **Concrete Details:** The framework found that LLMs easily fix basic syntax errors (over 80% correct on the first try), but struggle consistently to author semantically correct queries [16]. The evaluation demonstrated extreme variance depending on the graph serialization format: for example, GPT-4's performance spiked to an impressive 0.7 F1 score when the CoyPu-Mini knowledge graph was presented in JSON-LD format, whereas Claude and Gemini models performed significantly worse on JSON-LD compared to Turtle syntax [17].

*   **Name and Key Claim:** Foundation AgenticOS (FAOS) and The Inverse Parametric Knowledge Effect
    *   **Core Approach:** A large-scale empirical evaluation of 1,800 runs across five regulated enterprise industries (including English and Vietnamese domains) comparing ungrounded LLMs, document-based RAG, and ontology-coupled agents [18]. It evaluated Terminological Fidelity (TF), Metric Accuracy (MA), Regulatory Compliance (RC), and Role Consistency (RS) [19].
    *   **Concrete Details:** The study proved that the value of ontological grounding is inversely proportional to an LLM's pre-trained memory [20]. Specialized Vietnamese industries saw massive performance lifts (up to +0.29 delta), doubling the improvement seen in English domains because the LLM lacked internal knowledge of localized regulations [21]. Conversely, for widely known public concepts (like computing an insurance "combined ratio"), aggressively injecting structured ontological context actively degraded the LLM's performance (e.g., TF dropping from 0.81 to 0.50) [22]. This "contextual interference" happens when the structured prompt displaces the model's robust internal parametric knowledge, resulting in measurable semantic entropy increases for well-known domains [23].

*   **Name and Key Claim:** CypherBench Dataset
    *   **Core Approach:** A large-scale benchmark specifically designed to evaluate LLM-based question answering over full-schema labeled property graphs (LPGs) using the Cypher query language [24]. 
    *   **Concrete Details:** The dataset encompasses 7.8 million entities and 11 subject domains extracted from Wikidata [25]. When testing a Multi-Agent GraphRAG framework on 150 question-answer pairs across five diverse graphs (art, flight accident, company, geography, fictional character), the agentic approach improved Gemini 2.5 Pro's query accuracy from 67.00% (in a linear single-pass) to 77.23% (agentic), utilizing a separate LLM-as-a-judge (GigaChat 2 MAX) to evaluate semantic equivalence between the predicted and ground truth outcomes [26].

[^1]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^2]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^3]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^4]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]




[^9]: [[sources/Agentic SPARQL: Evaluating SPARQL-MCP-powered Intelligent Agents on the Federated KGQA Benchmark]]
[^10]: [[sources/Agentic SPARQL: Evaluating SPARQL-MCP-powered Intelligent Agents on the Federated KGQA Benchmark]]
[^11]: [[sources/Agentic SPARQL: Evaluating SPARQL-MCP-powered Intelligent Agents on the Federated KGQA Benchmark]]
[^12]: [[sources/Agentic SPARQL: Evaluating SPARQL-MCP-powered Intelligent Agents on the Federated KGQA Benchmark]]
[^13]: [[sources/Agentic SPARQL: Evaluating SPARQL-MCP-powered Intelligent Agents on the Federated KGQA Benchmark]]




[^18]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^19]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^20]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^21]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^22]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^23]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^24]: [[sources/[2511.08274] Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs]]
[^25]: [[sources/[2511.08274] Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs]]
[^26]: [[sources/[2511.08274] Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs]]

[^1]: [[sources/yt-S5ezVVJhQmE]] [^2]: [[sources/yt-S5ezVVJhQmE]] [^3]: [[sources/web-2013-01-18-6fc]] [^4]: [[sources/web-2013-01-18-6fc]] [^5]: [[sources/web-2013-01-18-6fc]] [^6]: [[sources/web-2013-01-18-6fc]] [^7]: [[sources/web-2013-01-18-6fc]] [^8]: [[sources/web-2013-01-18-6fc]] [^9]: [[sources/web-2013-01-18-6fc]] [^10]: [[sources/web-2013-01-18-6fc]] [^11]: [[sources/web-2013-01-18-6fc]] [^12]: [[sources/web-2013-01-18-6fc]] [^13]: [[sources/web-2013-01-18-6fc]] [^14]: [[sources/web-2013-01-18-6fc]] [^15]: [[sources/web-2013-01-18-6fc]] [^16]: [[sources/web-2013-01-18-6fc]] [^17]: [[sources/web-2013-01-18-6fc]] [^18]: [[sources/web-2013-01-18-6fc]] [^19]: [[sources/web-2013-01-18-6fc]] [^20]: [[sources/web-2013-01-18-6fc]] [^21]: [[sources/web-2013-01-18-6fc]] [^22]: [[sources/web-2013-01-18-6fc]] [^23]: [[sources/web-2013-01-18-6fc]] [^24]: [[sources/web-2013-01-18-6fc]] [^25]: [[sources/web-2013-01-18-6fc]] [^26]: [[sources/web-2013-01-18-6fc]]

### Comparisons

## Pattern-Based Benchmarks vs. Complex Multi-Domain Benchmarks

Based on the provided sources, a major comparative theme in evaluation is the necessary shift from simple, template-driven datasets to highly complex, multi-domain benchmarks.

**Items Compared:** Traditional datasets (LC-QuAD 1.0, LC-QuAD 2.0, DBNQA) versus modern complex benchmarks (Spider4SPARQL, CypherBench).

*   **Differences in Evidence and Outcomes:** Traditional benchmarks like LC-QuAD rely heavily on template-based question generation, allowing state-of-the-art models to achieve high execution accuracies around 91% to 92% [1]. In contrast, Spider4SPARQL translates the multi-domain Spider dataset into 4,721 complex SPARQL queries executable against 166 knowledge graphs [2]. When tested on Spider4SPARQL, even powerful LLMs struggle immensely; GPT-3.5 achieved only 8% accuracy in a zero-shot setting and 45% in a few-shot setting [3]. Similarly, CypherBench challenges models on Labeled Property Graphs containing 7.8 million entities, where single-pass LLM baselines yield accuracies ranging only from 41.23% to 67.00% [4]. 
*   **Strengths and Weaknesses:** The primary weakness of traditional benchmarks is their reliance on templates that often embed the exact database entity names into the natural language query, transforming the complex translation task into simple Named Entity Recognition [5]. The strength of modern benchmarks like Spider4SPARQL and CypherBench is their inclusion of realistic, human-authored questions featuring complex aggregations, set operations, and multi-hop reasoning requirements across diverse domains [6]. 
*   **Contexts and Trade-offs:** While older benchmarks are useful for training models on basic graph query syntax, they create a false impression that text-to-query generation is a solved problem [7]. Modern complex benchmarks accurately reflect real-world enterprise environments, demonstrating that current LLMs remain far from deployment-ready for autonomous database querying without significant multi-agent or retrieval-augmented scaffolding [8].

## Detection Accuracy vs. Explanation Faithfulness

Evaluating knowledge-graph-powered agents requires distinguishing between a model's ability to classify an outcome and its ability to prove its reasoning.

**Items Compared:** Traditional classification metrics (e.g., F1 scores) versus RAGAS faithfulness and context metrics.

*   **Differences in Evidence and Outcomes:** In the domain of IoT network security, traditional graph-based intrusion detection systems achieve F1 scores exceeding 0.97 [9]. However, when evaluating the explanations generated by LLMs to justify these detections, RAGAS evaluations reveal a severe "accuracy-faithfulness gap" [10]. Even when the classification is correct, over 40% of the statements in the LLM-generated compliance answers are hallucinated from the model's parametric memory rather than being grounded in the retrieved network evidence [11].
*   **Strengths and Weaknesses:** Classification metrics (like F1 or precision) have the strength of measuring raw predictive performance, but their weakness is that they provide no insight into whether the model is guessing or reasoning based on facts [12]. RAGAS metrics—specifically measuring Context Precision, Context Recall, and Faithfulness—provide the strength of verifying statement-level grounding [13]. A critical weakness revealed by RAGAS testing is that all retrieval methods (graph, vector, and rule-based) suffer from extremely low Context Recall (≤22.4%) on network flow data, forcing the LLM to hallucinate to fill the void [14].
*   **Contexts and Trade-offs:** Relying solely on accuracy metrics is acceptable for low-stakes automated filtering, but faithfulness evaluation is mandatory for responsible AI in security and regulatory auditing [15]. A legally defensible audit trail requires every claim to be traceable to retrieved graph evidence, meaning system designers must trade off some fluency or generative completeness to guarantee strict factual faithfulness [16].

## Constructive Grounding vs. Destructive Interference

Empirical evaluations of enterprise agents reveal that injecting ontological graph context does not universally improve LLM performance.

**Items Compared:** Agent performance on localized, low-resource domains (e.g., Vietnamese regulatory frameworks) versus universally known public domains (e.g., English insurance metrics).

*   **Differences in Evidence and Outcomes:** A 1,800-run empirical evaluation across five regulated industries discovered an "inverse parametric knowledge effect" [17]. For highly specialized topics like Vietnamese banking regulations, ontological grounding provided a massive performance lift (up to +0.29 delta), which was twice the improvement seen in English-language domains [18]. Conversely, when the LLM was fed structured ontological context for broadly known public concepts—such as computing a standard insurance "combined ratio"—its performance actively degraded, with Terminological Fidelity dropping from 0.81 down to 0.50 [19].
*   **Strengths and Weaknesses:** The strength of knowledge graph grounding is its ability to supply formal, enterprise-specific facts (like internal KPI thresholds or local regulations) that are entirely absent from the LLM's pre-training data [20]. However, its weakness is that injecting structured ontological formats (like property-value pairs and metric ranges) for well-understood topics consumes token budget and introduces "contextual interference," actively displacing the model's robust internal parametric knowledge [21].
*   **Contexts and Trade-offs:** This effect creates a distinct design trade-off for GraphRAG architectures. Blanket injection of graph context for every query is suboptimal [22]. Instead, systems should ideally estimate the LLM's baseline parametric confidence and selectively suppress graph retrieval for well-known domains, reserving the context window strictly for specialized knowledge where the graph provides constructive interference [23].

## Serialization Formats and Subgraph Provisioning

Automated benchmarking frameworks highlight how the specific presentation of graph data radically alters LLM reasoning success.

**Items Compared:** Graph serialization formats (Turtle vs. JSON-LD) and contextual scope (Full Knowledge Graph vs. Schema vs. exact IRIs).

*   **Differences in Evidence and Outcomes:** In tests conducted via the LLM-KG-Bench framework, providing different serialization formats yielded highly model-dependent outcomes [24]. For example, GPT-4's performance spiked to an impressive 0.7 F1 score when the CoyPu-Mini knowledge graph was presented in JSON-LD format, whereas Claude and Gemini models performed significantly worse on JSON-LD compared to Turtle syntax [25]. Furthermore, providing the exact required IRIs to the model yielded a relatively high query generation score (0.76 F1), but simply providing the graph schema caused performance to plummet to 0.19 F1 [26].
*   **Strengths and Weaknesses:** Providing LLMs with explicit IRIs plays to their strengths in syntax formulation, allowing them to easily construct executable queries [27]. However, forcing the LLM to deduce the correct entities from a raw schema exposes a severe weakness in their semantic reasoning capabilities [28]. The Turtle format has the strength of being syntactically concise, which generally leads to a higher number of parseable queries across most models [29].
*   **Contexts and Trade-offs:** When evaluating or deploying text-to-query agents, engineers face a trade-off between the realism of the task and the success rate of the model. Giving the model pre-filtered IRIs ensures high success but ignores the realistic difficulty of schema linking [30]. Furthermore, developers must select graph serialization formats that align with their specific foundation model's pre-training biases (e.g., JSON-LD for GPT-4, Turtle for Claude) to optimize accuracy [31].



[^4]: [[sources/[2511.08274] Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs]]

[^6]: [[sources/https://digitalcollection.zhaw.ch/bitstreams/830ed7ae-4b65-4366-8a06-86be8f0d7d75/download]], [[sources/[2511.08274] Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs]]


[^9]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^10]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^11]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^12]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^13]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^14]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^15]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^16]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^17]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^18]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^19]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^20]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^21]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^22]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^23]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]

[^1]: [[sources/yt-S5ezVVJhQmE]] [^2]: [[sources/yt-S5ezVVJhQmE]] [^3]: [[sources/web-2013-01-18-6fc]] [^4]: [[sources/web-2013-01-18-6fc]] [^5]: [[sources/web-2013-01-18-6fc]] [^6]: [[sources/web-2013-01-18-6fc]] [^7]: [[sources/web-2013-01-18-6fc]] [^8]: [[sources/web-2013-01-18-6fc]] [^9]: [[sources/web-2013-01-18-6fc]] [^10]: [[sources/web-2013-01-18-6fc]] [^11]: [[sources/web-2013-01-18-6fc]] [^12]: [[sources/web-2013-01-18-6fc]] [^13]: [[sources/web-2013-01-18-6fc]] [^14]: [[sources/web-2013-01-18-6fc]] [^15]: [[sources/web-2013-01-18-6fc]] [^16]: [[sources/web-2013-01-18-6fc]] [^17]: [[sources/web-2013-01-18-6fc]] [^18]: [[sources/web-2013-01-18-6fc]] [^19]: [[sources/web-2013-01-18-6fc]] [^20]: [[sources/web-2013-01-18-6fc]] [^21]: [[sources/web-2013-01-18-6fc]] [^22]: [[sources/web-2013-01-18-6fc]] [^23]: [[sources/web-2013-01-18-6fc]] [^24]: [[sources/web-2013-01-18-6fc]] [^25]: [[sources/web-2013-01-18-6fc]] [^26]: [[sources/web-2013-01-18-6fc]] [^27]: [[sources/web-2013-01-18-6fc]] [^28]: [[sources/web-2013-01-18-6fc]] [^29]: [[sources/web-2013-01-18-6fc]] [^30]: [[sources/web-2013-01-18-6fc]] [^31]: [[sources/web-2013-01-18-6fc]]

### Gaps

## The LLM-as-a-Judge Reliability Gap

A major unresolved tension across the corpus is the heavy reliance on LLMs to evaluate other LLMs, particularly when auditing complex or regulated domains. 

*   **Unvalidated Expert Agreement:** Frameworks evaluating enterprise and security agents often deploy an "LLM-as-a-judge" (e.g., using GPT-4o-mini or Claude Sonnet 4) to verify semantic equivalence and faithfulness [1, 2]. However, researchers note a severe limitation: agreement between human Subject Matter Experts (SMEs) and LLM judges reaches only 64% to 68% on expert knowledge tasks [1]. Current studies explicitly lack formal inter-rater reliability validation (such as Cohen's Kappa) against actual human domain experts to prove the automated judge is scoring accurately [1].
*   **Inter-Judge Variability and Decomposition Flaws:** Evaluating "faithfulness" requires the judge model to decompose a generated answer into atomic claims and verify them against retrieved context [2]. The literature leaves inter-judge reliability unexamined, acknowledging that switching the judge from OpenAI models to Gemini or Claude could yield entirely different absolute faithfulness scores due to variations in how these models follow instructions and extract claims [2].

## Statistical Underpowering and Benchmark Contamination

The literature identifies significant gaps regarding the statistical validity and integrity of the datasets used to evaluate agent-over-graph systems.

*   **Bottlenecks in Ground Truth Creation:** Generating realistic, expert-validated scenarios for specific domains (like network security compliance) requires immense manual effort from domain specialists [3]. As a result, experimental sample sizes are often too small (e.g., 75 to 112 valid evaluations per method) to achieve statistical significance [3]. These underpowered studies (achieving only ~30% statistical power) fail to definitively prove whether one retrieval method is mathematically superior to another or if the variance is merely due to sampling noise [3, 4].
*   **Data Contamination on Public Benchmarks:** The corpus warns that evaluating models on popular, publicly available datasets (such as LC-QuAD) introduces a high risk of data contamination [5, 6]. Because frontier LLMs are pre-trained on vast portions of the web, they have likely memorized these benchmarks, meaning high evaluation scores may reflect dataset memorization rather than genuine zero-shot reasoning or text-to-query capabilities [5, 6]. 
*   **Ambiguities in Test Sets:** Existing benchmarks frequently contain ambiguities and unresolvable paraphrasing issues that actively hinder proper automated evaluation [5].

## Token Volume Confounds and Curated Baselines

There are unanswered questions regarding whether the performance lift observed in GraphRAG systems is due to their structural advantages or simply due to unequal experimental testing conditions.

*   **The Token Count Confound:** When comparing ontology-grounded agents against standard RAG baselines, systems inject structured knowledge (section headers, property-value pairs, metric ranges) that consumes significantly more tokens [7]. In enterprise evaluations, ontology injections consumed 2,800 to 3,200 tokens, whereas the RAG baseline consumed only 2,000 tokens—a 40% to 60% overhead [7]. The literature notes it remains unresolved whether the performance advantage comes from the ontological *structure* or simply the higher *volume* of context tokens, requiring future experiments that strictly equalize token budgets to isolate the effect [7].
*   **Artificially Clean RAG Baselines:** In comparative evaluations, the "unstructured" chunks provided to the baseline RAG systems are often manually curated from the exact same ontology blueprints used to build the graph [7, 8]. The corpus notes this creates an artificially well-organized baseline that fails to reflect the noisy, heterogeneous, and contradictory document collections agents actually face in production environments [7, 8].

## Generalizability to Complex Topologies and Empty Results

The corpus highlights significant gaps in evaluating how well agents generalize across different structural schemas and edge cases.

*   **Lack of Diverse Regulatory Topologies:** While GraphRAG shows promise on specific regulatory structures (like the ETSI EN 303 645 standard), the literature acknowledges these findings may not generalize to standards with fundamentally different topological properties [9]. For example, the corpus does not address how agents handle massive hierarchical capability models (like IEC 62443), threat models focusing on manufacturer actions rather than device behaviors (NISTIR 8259A), or standards requiring explicit temporal reasoning like quarterly vulnerability scans (PCI DSS) [9].
*   **Evaluating "Empty" Query Results:** In Text-to-SPARQL generation, there is a recognized methodological gap in evaluating queries that return an empty result set when executed [10]. Researchers flag that it is currently difficult to automatically discern whether a query returned no results because it was semantically flawed, or because it was a perfectly constructed query asking for information that simply did not exist in the database [10].
*   **Lack of Domain-Native Faithfulness Metrics:** Current faithfulness evaluations (like RAGAS) rely on semantic entailment metrics originally designed for natural language corpora [9]. The corpus notes an unaddressed need to develop domain-specific faithfulness metrics capable of verifying claims directly against raw, structured ground truth (such as raw network protocol packet data) rather than relying on textual summaries [9, 11].

[^1]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^2]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^3]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]
[^4]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]


[^7]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^8]: [[sources/Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
[^9]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]

[^11]: [[sources/Towards Responsible AI for IoT Network Security Auditing Using Knowledge Graph and RAGAS]]

[^1]: [[sources/yt-S5ezVVJhQmE]] [^2]: [[sources/yt-S5ezVVJhQmE]] [^3]: [[sources/yt-S5ezVVJhQmE]] [^4]: [[sources/yt-S5ezVVJhQmE]] [^5]: [[sources/yt-S5ezVVJhQmE]] [^6]: [[sources/web-2013-01-18-6fc]] [^7]: [[sources/web-2013-01-18-6fc]] [^8]: [[sources/web-2013-01-18-6fc]] [^9]: [[sources/web-2013-01-18-6fc]] [^10]: [[sources/web-2013-01-18-6fc]] [^11]: [[sources/web-2013-01-18-6fc]]

## Sources cited

- [[sources/yt-S5ezVVJhQmE]]
- [[sources/web-2013-01-18-6fc]]

## Included works

- [[sources/web-2013-01-18-6fc]]
- [[sources/yt-S5ezVVJhQmE]]
