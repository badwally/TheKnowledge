---
title: Architecting the Agentic Data Cloud | Google Cloud Blog
source: https://cloud.google.com/transform/shift-system-of-action-architecting-the-agentic-data-cloud-AI
author:
  - "[[Andi Gutmans]]"
published: 2026-04-22
created: 2026-05-28
description: What is an agentic data cloud? The Agentic Data Cloud transforms enterprise data from a passive repository into a proactive System of Action designed for autonomous AI agents.
tags:
  - clippings
  - agentic-data
  - googles-edge-ai-stack
type: concept
---
Data Analytics

## The shift to a System of Action: Architecting the Agentic Data Cloud

##### Andi Gutmans

VP/GM, Data Cloud, Google Cloud

#### The Agentic Data Cloud transforms enterprise data from a passive repository into a proactive System of Action designed for autonomous AI agents.

##### Contact Sales

Discuss your cloud needs with our sales team.

[Contact us](https://cloud.google.com/contact?utm_source=google&utm_medium=blog)

AI is reengineering the global economy. In the agentic era, businesses are being supercharged by autonomous agents that perceive, reason, and act to unleash human potential. This introduces three major shifts that flip the script on how we think about data powering AI.

First, we are moving from **human scale to agent scale**. Practitioners are becoming orchestrators of agents, which is giving them superpowers. But this also means you will face orders of magnitude more workload as agents monitor and operate your business around the clock at digital speed. Your data platform now needs to support always-on, high-velocity, and autonomous operations.

Second is a shift from **reactive** **intelligence to proactive action**. Previously, we built reactive architectures to tell us what happened yesterday, or at most tried to forecast from the past and present. But agents can be proactive, executing in the moment and shaping the future. Now, your agents must act on your behalf, and do so accurately.

Third is a shift from **data to knowledge**. It is no longer enough just to discover and query your data. You must elevate this data with a knowledge flywheel that understands the relationship between data assets, semantics, and how the data is commonly used. An agent needs to tell the difference between “revenue” and “projected revenue” without guesswork. You also need to be able to activate all your data, including the [90% of dark data](https://cloud.google.com/transform/from-dark-data-to-bright-insights-how-ai-agents-make-data-simple-gen-ai) hidden in contracts, product specs, emails, images, and videos. Without a deep understanding of the full data estate, both structured and unstructured, you do not have the quality and trust to activate agents on behalf of your business at scale.

Many vendors talk about their data platforms as a System of Intelligence. But really, those are the last generation of data platforms. A System of Intelligence is reactive, mostly reporting the news as opposed to making the news. It waits for a human to ask a question, or it sits as a prediction from a forecasting model waiting to be acted on. In the agentic era, that is simply not enough.

The goal is no longer just to know. The goal is to act. To do this, you need a **System of Action** that is proactive and can operate on your behalf, allowing agents to drive trusted outcomes.

### Why legacy architectures break at agent scale

The so-called “modern” data stacks — those glued together with disjointed parts — were not built for the agentic era. When we analyze these legacy architectures under agentic load, we see they break because of four structural issues.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Modern_Data_Stacks_Break.max-1700x1700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Modern_Data_Stacks_Break.max-1700x1700.jpg)

The fragmented stack

**The walled garden**: Vendors demand you move your estate into their siloed lakehouses to get intelligence. But when you do this, you not only create data silos, but also fracture your security. When your open data is locked away in a walled garden and you try to step out, your governance perimeter dissolves. Your access controls, identity management, and lineage get left behind. Walled gardens force you to recreate your governance and security policies from scratch. For an agent to operate safely across your business, it needs a unified perimeter.

**The trust gap**: Previous generation platforms provide you with a catalog, a technical list of where things are. But agents need rich context, not just a list of inventory. They need to understand not just where data lives, but what it means, the relationships between data, and how it is being accessed. Without best-in-class AI and knowledge, an agent acts on raw data without business understanding, leading to hallucinations and invalid outcomes. These are mistakes you simply cannot afford.

**The time factor**: Agents need to respond at the speed of business. To have sound judgment, an agent needs to reason over your analytical history and your operational reality. And to take action, it needs to touch those operational systems in real time. All of this must happen in a single, fast, and trusted reasoning loop. Legacy stacks break this loop. They separate the thinking from the doing by severing the link between operational and analytical systems, or they try to force you into a one-size-fits-all architecture. When an agent can’t tap into all the relevant data sources in real-time, it misses the window to act.

**The cost spiral**: Autonomous agents are processing data at a volume and frequency we have never seen. If you scale your agents on a fragmented stack that is not deeply optimized for AI workloads, your costs explode. At agent scale, your AI should be your greatest asset, not an unpredictable financial liability.

Why are these failures so prevalent? The "modern” data stack was never designed to be a unified and hyper-optimized system. It is a patchwork where no single provider owns the outcome. Other hyperscalers own the infrastructure but rent the models. AI labs own the models but rent the infrastructure. Between them sit data vendors acting as general contractors, stitching these borrowed infrastructure and AI components together. This fragmentation is fatal for a cost-effective agentic architecture.

### The new paradigm: Meet the Agentic Data Cloud

You need a new architecture: an **Agentic Data Cloud.**

An Agentic Data Cloud is a **System of Action**. It evolves the enterprise data platform from a static data repository into a dynamic data reasoning engine. It closes the gap between thinking and doing for agents, merging your analytical insights with transactional power in one seamless, closed loop. And it moves beyond the dashboard to a world where your data does not just tell you there is a problem, but it actually fixes it.

This architecture reimagines the practitioner experience, enabling agent-first workflows where you simply define the outcome and agents orchestrate, generate, and validate them.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2026-04-21_at_4.02.00PM.max-1600x1600.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2026-04-21_at_4.02.00PM.max-1600x1600.png)

The Agentic Data Cloud

An Agentic Data Cloud meets three requirements:

**It must be AI-native**: To survive agent-scale, efficient AI needs to be infused into every layer, from the hardware to the software. This is the best way to process multimodal data and complex reasoning in real time, at the needed scale, and without costs spiraling.

**It must be flexible**:It needs to tear down walled gardens, giving your agents the freedom to activate data across open formats, clouds, or native engines, without forcing costly modernization projects.

**It must be trusted**: The bridge between intelligence and action is trust. You cannot allow an agent to execute a transaction unless it operates within strict boundaries and fully understands the business context. Governance needs to provide active oversight, ensuring every automated action is permissioned, explainable, compliant, and safe.

### The world’s first Agentic Data Cloud

**Today, we are introducing the world’s first Agentic Data Cloud.**

We deliver this because we do not bundle other providers’ pieces. This lets us deliver the structural efficiency and seamless performance required for the agentic era in ways others do not do today.

**Solving the cost spiral with vertical integration**

We do not bolt AI onto a legacy database. We harmonize the full stack, from our efficient AI infrastructure and models to our differentiated data systems, benefiting from Google’s cross-company innovation. By integrating the model directly with the data infrastructure, we eliminate extra network hops and the complexities of managing cost, scale, and security.

**Solving the walled garden with a cross-cloud lakehouse**

Our Agentic Data Cloud is open and flexible, enabling you to activate your data with AI, whether it is hosted on Google Cloud or not. Our [Lakehouse for Apache Iceberg](https://cloud.google.com/products/lakehouse) unifies your data foundation. It offers Google’s powerful engines alongside open standards, whether you use BigQuery and Spanner, the Lightning Engine for Apache Spark, or AlloyDB for PostgreSQL. Our Omni technology unchains core engines to run across clouds, on-premises, and at the edge. All of this makes our Lakehouse a borderless foundation where agents use data across AWS as if it were local to Google Cloud, removing cross-cloud latency and eliminating massive egress fees.

**Solving the trust gap with universal context**

We are building a knowledge flywheel to deliver the quality and trust that you need to be successful in the agentic era. At its center is the [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog/), which provides universal context by aggregating data, continuously enriching its meaning, and enabling high-precision search. We use the LookML Agent and BigQuery Measures to automatically generate these semantics, while zero-copy federation integrates additional business context from applications like SAP and Salesforce Data360. To continuously enrich this foundation, the Knowledge Catalog uses Smart Storage and Gemini to automatically extract meaning from unstructured files. Tapping into decades of Google Search innovation, the catalog ensures agents instantly retrieve the right context. These capabilities evolve the catalog from a passive inventory into an active layer that improves agent effectiveness and accuracy.

Finally, as you reach agent-scale, the platform must deliver another step up in security, scalability, reliability, and price performance. We can uniquely deliver on agent scale because our Agentic Data Cloud is built on Google’s differentiated infrastructure, which we continue to evolve.

Google’s Agentic Data Cloud

### The architecture of autonomy

For the past two years, Google has been quietly and fundamentally rearchitecting our entire data portfolio to natively support autonomous workflows. We have embedded deep agentic capabilities across four architectural layers:

- **The agentic workforce:** We have moved from toilsome tools to a platform with automation built in. This includes the Data Science agent, the Data Engineering agent, the Database Observability agent, and significantly advanced Conversational Analytics. Central to this workforce is the Google Cloud Data Agent Kit, which enables practitioners with Model Context Protocol (MCP) tools, skills, and extensions that enhance the workspaces they love to natively understand Google’s Agentic Data Cloud.
- **Context and memory:** Agents require long-term recall and deep enterprise understanding to be trusted. We evolved the Knowledge Catalogto master business semantics and context, alongside the Agent Platform Memory Bank for stateful agent recall. This is underpinned by AgentOps, providing visibility into agent "thought processes" through real-time reasoning telemetry.
- **Unified orchestration and tooling:** To move from thinking to doing, agents must bridge the gap between your analytical history and your operational reality. We’ve standardized on the open MCP, providing agents with a universal toolbox to trigger actions. And we have introduced specific tools across Spanner, AlloyDB, Cloud SQL, Looker, and BigQuery to create a unified action plane where you can trigger transactions and update operational systems the moment an analytical insight is reached.
- **Active, multimodel engines:** We reengineered the core engines themselves to be the core of the operation. By bringing graph, vector, search, and multimodal data processing natively into the database and powering them with integrated **r** easoning engines, we’ve created a platform that doesn't just store data, it perceives and reasons. With real-time AI functions, our engines process data as it arrives and trigger autonomous actions the moment your business changes.

### The Agentic Data Cloud in production

The shift to this new architecture is already underway. It is clear our own customers are not just storing data, but activating it with AI at massive scale.

- Our AI-powered data migration services have translated more than **1 billion queries**, **more than** **doubling year over year**, as companies rip out the last generation’s “intelligent” data platforms.
- We have seen more than **30x growth** **year-over-year** in BigQuery data processed by Gemini as companies activate for the agentic era.
- We have seen over **20x growth over the past six months** in customer use of MCP Server with BigQuery as companies build their agentic futures.

“To secure the AI era, we needed a foundation that could think as fast as the threats evolve. Google's Agentic Data Cloud acts as the core reasoning engine for our security products. Leveraging Spanner’s unified graph and non-graph capabilities, we can now provide our customers with a seamless, highly scalable identity posture that enables AI agents to perceive and act on security gaps in real time.”  
**Sreejith Rajkumar, Director of Engineering, Palo Alto Networks**

“Our partnership with Google Cloud is focused on building a smarter, faster exchange. Google’s Agentic Data Cloud allows us to dismantle the legacy silos and technical debt that once slowed us down. By integrating the operational reliability of Cloud SQL with the deep reasoning of BigQuery, we’ve created a data ecosystem where our developers and AI agents can validate, optimize, and innovate in real time.”  
**Kristofer Shane Sikora, Executive Director, Cloud Data Engineering, CME Group**

“To deliver AI that actually works across HR, payroll, and workforce operations, you need a consistent, real-time data layer. With the power of Google’s Agentic Data Cloud, People Fabric is the backbone of UKG’s Workforce Operating Platform — turning fragmented systems into a single source of truth that powers intelligent, agent-driven experiences.”  
**Radhi Chagarlamudi, Group Vice President, Product Engineering,** **UKG**

### The future is active

When you build on Google Cloud, you benefit from the same technology that runs Google.

Long before the agentic era, we solved many at-scale complexities to run our own business. We invented real-time indexing for Search, bent the cost curve of storage for Gmail, and solved global latency for Ads. When you choose Google Cloud, you plug into the same engines that power nine Google products with over a billion users each.

Your agents inherit the innovation of [DeepMind’s research](https://deepmind.google/research/) and the AI infrastructure that was used to drive groundbreaking AI innovation. You get native access to specialized models like [TimesFM](https://cloud.google.com/blog/products/data-analytics/timesfm-models-in-bigquery-and-alloydb) and [WeatherNext](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/weathernext-2/), and curated datasets from Earth Engine, Weather, and Google Trends, so your agents can correlate business data with global signals, letting them understand the real world. You deploy on a foundation that uses the Site Reliability Engineering (SRE) model we invented to keep the internet running.

This is why [**9 of the top 10 AI labs use Google Cloud**](https://cloud.google.com/blog/topics/startups/differentiated-ai-tech-stack-drives-startup-innovation-google-builders-forum). They know that in the agentic era, they need a foundation that has already survived the scaling challenges they face today.

The era of passive observation is over. The future belongs to the System of Action, made possible by an Agentic Data Cloud.

**Ready to see what an Agentic Data Cloud can do for your business?  
**[Sign up today for a strategy workshop](https://cloud.google.com/resources/offers/data-strategy-workshop?e=48754805) on how to get your data ready to fuel autonomous agents through a System of Action.

Posted in
- [Data Analytics](https://cloud.google.com/blog/products/data-analytics)