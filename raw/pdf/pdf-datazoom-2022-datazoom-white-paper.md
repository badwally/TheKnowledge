---
id: pdf-datazoom-2022-datazoom-white-paper
type: pdf
title: Datazoom_White Paper_Fall2021_Final (Final)
url: ''
authors:
- Datazoom
ingested_at: '2026-04-29T16:12:42Z'
content_hash: sha256:9baa82bcae9379c57d5c7d54965c776095c2d52b20d2c4c8bd83cd5593ef05e2
source_path: raw/pdf/pdf-datazoom-2022-datazoom-white-paper.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 31
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: DAEo463I3mg,BAAYh539-nY
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/Datazoom_White Paper_Fall2021.pdf
published_at: '2022'
---
Advanced Streaming Observability
and the Video Data Platform
Leveraging Multi-Point, Standardized, Correlated
Data for Exceptional QoE
White Paper
By Josh Evans, CTO at Datazoom
Fall 2021

Advanced Streaming Observability
and the Video Data Platform
Table of Contents
03 | Introduction
03 | Terminology
04 | State of the Industry
06 | What is Observability?
06 | Observability Defined
06 | The Three Pillars
09 | Industry Observability Challenges
11 | Challenge 1: Metrics Over Events
12 | Challenge 2: Data Diversity & Silos
14 | Challenge 3: Data Latency
15 | Industry Observability Trends
15 | CDN Log Streaming
15 | CTA-5004 Common Media Client Data
16 | End-to-End Workflow Monitoring
17 | Distributed Request Tracing
18 | The Elements of Advanced Observability
18 | Ubiquitous, Low-Latency Event Logging
18 | Multi-Point Data Collection
19 | Multi-Point Data Correlation
20 | Domain Data Standardization
20 | Real-time Enrichment
21 | Content Request Tracing
22 | Data Sharing
22 | Smart Sampling
23 | Flexible Analytics
24 | The Video Data Platform
25 | Undifferentiated Heavy Lifting
25 | Data Dictionaries
25 | Integrated Sampling
26 | Pluggable Analytics
26 | Dynamic Configuration
27 | Observability Data Exchanges
27 | Lightweight Integrations
28 | Achieving Exceptional QoE with a VDP
28 | The OODA Loop and MTTR
28 | Rapid Root Cause Analysis
28 | Self-healing Systems
29 | Service Optimization
30 | Beyond QoE: Business & Product Optimization
31 | Conclusion
//02
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Introduction
The streaming video industry is moving from its infancy to a new phase of its development which
can best be described as “the awkward teenage years”. And, while technology and knowledge
about streaming video has advanced dramatically over the last twenty years, the fundamental
challenges of observability and mastery of the end-user experience remain elusive. This lack of
mastery can negatively impact viewer satisfaction and engagement over time, hindering business
growth and, ultimately, profitability.
In this paper, we’ll examine the state of streaming video observability, delve into the observability
challenges which plague streaming operators, and articulate a set of innovative solutions which
can help address those obstacles. More specifically, we’ll propose a vision for advanced
streaming video observability and an integrated platform approach designed to support that
vision.
Terminology
Within the technical industry at large the terms Quality of Experience (QoE) and Quality of Service
are sometimes used interchangeably. However, they have distinct definitions which are relevant
to this document.
Quality of Experience “is a measure of the delight or annoyance of a customer's experiences
with a service.”
True QoE measurement would require a direct understanding of viewer’s perceptions and
experiences, but collecting such data in a systemic, scalable way is highly impractical, if not
impossible. As a result, we seek proxy measurements for this experience in the form of data
collected from the end-user application. In this document, we will refer to this data collectively as
QoE Telemetry. QoE telemetry is typically collected by the content publisher or a third party
vendor that provides application and player support.
Quality of Service “is the description or measurement of the overall performance of a service,
such as a telephony or computer network or a cloud computing service, particularly the
performance seen by the users of the network.”
In this case, the focus is not on the end-user’s experience as measured by an application but
rather the performance (throughput, latency, efficiency, error rates, etc.) of supporting services
and their component parts.
QoS data is collected by third party service providers to maintain service level objectives (uptime,
//03
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
latency, etc.). These service providers typically do not have access to the QoE telemetry collected
by their enterprise customers (e.g. content publishers or streaming operators). This means that
while they may know the health of their own systems they do not necessarily have an
understanding of how their service is ultimately experienced by end-users.
State of the Industry
Simon Wardly has defined a staged model for technical evolution (Wardley Maps) using the terms
pioneers, settlers, and town planners. Each stage moves closer to technical maturity. While the
model is quite sophisticated the stages are equally intuitive. So, we’ll take some license here and
loosely apply the model to frame the state of the streaming video industry.
Pioneers take on a poorly understood domain and navigate that uncertainty by iteratively
experimenting and inventing new solutions.
Settlers leverage an ecosystem of maturing components with an eye to continuous
improvement, feature differentiation, and growth.
Town Planners leverage well-defined, mature standards and technologies. Problems are well
understood and solutions are robust. The focus turns to nuanced analysis, modeling, and
efficiency.
Pioneers
During the birth of streaming video, pioneers like Netflix and YouTube found many of the tools
and frameworks they needed to be insufficient or non-existent. This presented a daunting
challenge: they had to design and build many of the technical components themselves, from
streaming video players to manifest generation services to encoding pipelines. On the positive
side, this led to significant, vertically integrated technical investments designed to satisfy user
needs and provide an exceptional viewing experience. For example, Netflix chose to abandon
1
third party CDNs for their own purpose-built, hybrid, streaming CDN to achieve exceptional
quality of service while reducing cost of delivery.
Although these investments were substantial, and paid off handsomely, they represent only the tip
of the iceberg. In their journey towards exceptional end-user QoE these pioneers have the distinct
advantage of owning and integrating virtually all of the services which generate observability data
for operational purposes. This data is delivered to analytics platforms within seconds, driving
functional feedback loops which programmatically alter the state of the services being monitored.
1The Netflix CDN is a mix of traditional caching PoPs in global internet exchanges and embedded
caches in ISP networks for the most popular content. Embedded caches reduce ISP network
investments (and peering costs) by providing highly efficient last mile delivery. They also provide
an optimized, low-latency, end-user experience.
//04
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
For example, Netflix has a very precise CDN architecture where content manifests direct the
player to a specific cache. Netflix already knows exactly which content is on each cache and, just
as importantly, the health of that cache in real-time. So, when a customer presses play on a piece
of content the manifest generated will automatically exclude unhealthy caches. It is this integration
of data and functionality which makes Netflix and YouTube gold standards when it comes to
streaming video QoE.
Settlers
Today’s settlers, such as content providers offering streaming platforms (e.g. Peacock, Disney+,
ViacomCBS) and newly emerging streaming services (e.g. DAZN, Discovery+, and FuboTV)
definitely have it easier than the pioneers did. Instead of having to build the entire workflow
themselves, settlers can choose from a myriad of companies and services which obviates much of
the technical investment that Netflix and Youtube had to make. Players, CDNs, origin services,
media pipelines, and related tools can all be found for purchase or as open source projects.
What’s more, these services continue to evolve, providing continuous improvements.
But, due to inconsistent access to log data, lack of common data standards, and interoperability
challenges at the ecosystem level, these settlers are beset with significant observability
challenges created by the very services which allow them to innovate quickly. Fragmentation, lack
of deep integration between services, and, in some cases, lack of focus on enterprise customer
needs, prevent streaming operators from building coherent views of operational health. This
manifests as a lack of access to logging data for many services or a lack of standardization across
similar services when the data is available. To express this more generally, services that are
designed independently without standards or an eye to cross-service integration do not tend to
interoperate well with each other.
These challenges impede streaming operators’ ability to create the holistic operational view of
their service which Netflix and Youtube take for granted. Even if settlers are able to get their
hands on telemetry from some of their service providers, integrating the data into a cohesive
operational view is virtually impossible. When attempts along these lines are made, the effort can
be significant, taking valuable engineering resources away from mission critical tasks. And then,
of course, there are the challenges associated with live streaming which involves many additional
moving parts in the real-time workflow.
Town Planners
In this paper we’ll dig into the observability challenges faced by today’s settlers (content providers
and streaming operators), review industry investments that seek to improve the
situation, and establish a vision for advanced observability that moves us towards town planner
maturity.
//05
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
What is Observability?
Observability Defined
A concise, modern, and relevant definition of observability can be found on the IBM cloud site.
While it is anchored in cloud computing it is highly relevant to any distributed system, including
one comprised of multiple services to support streaming video:
In general, observability is the extent to which you can understand the internal state or
condition of a complex system based only on knowledge of its external outputs. The more
observable a system, the more quickly and accurately you can navigate from an identified
performance problem to its root cause, without additional testing or coding. In cloud
computing, observability also refers to software tools and practices for aggregating,
correlating and analyzing a steady stream of performance data from a distributed application
and the hardware it runs on, in order to more effectively monitor, troubleshoot and debug
the application to meet customer experience expectations, service level agreements (SLAs)
and other business requirements.
In short, observability is about insight, understanding, tools, and practices. The goal is to meet or
exceed operational commitments to a business and its customers. So how do we gain that insight
and understanding? What tools and practices matter?
The Three Pillars
In February 2017, Peter Bourgon
attended the 2017 Distributed Tracing
Summit. During a discussion of
distributed request tracing scope the
question came up about the relationship
between distributed request tracing and
logging. He came up with this Venn
diagram and definitions which clarified
the relationships between metrics,
tracing, and logging, the three pillars of
observability.
//06
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Event Logs
In Bourgon’s words “the defining characteristic of logging is that it deals with discrete events.”
Examples include syslogs, audit-trail events, or request-specific dimensions. Event logging is fine-
grained and therefore suitable for deep, flexible analysis.
To add some color, event log data typically includes the name of the event, an event timestamp,
and a variety of dimensions (i.e. state at the time of event capture) relevant to the event. For
example, a streaming video player may emit a Stall Start event when it’s buffer has insufficient
data to continue streaming. Examples of relevant dimensions that might be logged along with
events include the Playhead Position or Rendition Video Bitrate at the time of the stall.
Metrics (and Measurements)
Bourgen defines metrics as follows: “the defining characteristic of metrics is that they are
aggregatable: they are the atoms that compose into a single logical gauge, counter, or histogram
over a span of time.”
In this paper, we’ll seek more precision in our nomenclature, distinguishing between simple
measurements at a point in time and the aggregation of those measurements. We’ll use the term
Measures for point in time measurements and Metrics for aggregation of measures or other
dimensions over some period of time. Metrics can be calculated at different levels or scopes. For
example, when discussing streaming video, aggregates can be calculated at the individual play
session level or across play sessions for a broader perspective.
To illustrate the distinction here is an example. A telemetry collector integrated with a video
application may be configured to capture the current playing Rendition Video Bitrate every minute
during a play session. This is a measure, a granular, event-level, numeric value captured at a
point in time. Therefore, during a one-hour play session there could be sixty such measures
captured and used to calculate a metric representing the average bitrate for the full session. To
illustrate the distinction here is an example. A telemetry collector integrated with a video
application may be configured to capture the current playing Rendition Video Bitrate every minute
during a play session. This is a measure, a granular, event-level, numeric value captured at a
point in time. Therefore, during a one-hour play session there could be sixty such measures
captured and used to calculate a metric representing the average bitrate for the full session.
Finally, a set of bitrate measures from multiple play sessions can be grouped by geographic
region (or a variety of other dimensions) and summarized during a traffic peak to define an
average bitrate metric served across sessions when a streaming service is under heavy load.
//07
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Traces
Finally Bourgen talks about traces by declaring “the single defining
characteristic of tracing, then, is that it deals with information that is
request-scoped.
Tracing, and more specifically distributed request tracing, provides
granular insight into the flow of HTTP requests as they traverse a
distributed system (e.g. a cloud-based, microservice architecture).
Traces are in truth complex event logs or sets of discrete events,
captured at the request level exposing service dependencies and
performance bottlenecks. This makes it far easier to isolate the cause
(or causes) of cascading failures or latency spikes than traditional log
and metrics analysis.
A Powerful Combination
The three pillars are deeply interdependent. Monitoring any complex distributed system involves
the creation of high level metrics which act as signals, triggering alerts when predefined (or
inferred) thresholds are exceeded. These metrics are derived from events, measures, and
dimensions. This includes event logging from players or servers or, potentially, distributed request
traces.
Once an alert fires the focus moves to correlation with other metrics looking for patterns and
clues. However, in order to determine the root cause of an issue, events and traces may be
required again. Referring to our stall event scenario - an alert may fire in response to an increase
in P95 stall rates across all play sessions over the last five minutes. One possible cause for a high
stall rate might be latency between two nodes in a distributed request sequence (player to CDN,
intra-CDN, CDN to origin, etc). By looking at the average latency between each node in the
distributed graph it may be possible to pinpoint the specific set of servers involved. Furthermore,
ad hoc metrics and log analysis of a specific server or service may expose performance issues or
exceptions, pinpointing root cause.
There are three fundamental QoE observability challenges facing the streaming video industry:
Metrics Over Events: metrics are calculated and collected at the source, not the events,
measures, and dimensions from which those metrics are derived.
Data Diversity and Silos: telemetry is non-standardized and isolated across domains making it
difficult to correlate.
Data Latency: telemetry is delivered too late to have the desired impact
//08
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Industry Observability Challenges
To illustrate these challenges the diagram below shows the potential pipeline of stages and
services which support a single streaming video session. Fully understanding the QoE for an end-
user (i.e. the viewer) requires data from each stage in the workflow.
Application
Internet Client
Encoder Transcoder Packager Origin Sti A tc d her CDN N T e r t a w n o si r t k P S r e o r v v i i d c e e r P E re q m ui i p s . e Player
Required Stages Digital
Rights
Mgmt.
Optional Stages
Ad
Server
Working from left to right here is a description 2 of each element in the workflow:
Encoder compresses master audio and video sources for distribution over IP networks.
Transcoder creates bitrate variants for an adaptive bit rate (ABR) ladder.
Packager creates formatted segments of transcoded video for delivery. The packager creates
delivery manifests.
Origin stores and serves packaged video for distribution via CDNs.
Ad Stitcher dynamically inserts ads into a delivered content stream. Ad stitching may be
performed during packaging or after delivery to origin depending on implementation specifics.
Content Delivery Network (CDN) delivers video files to the end-user/viewer.
Transit network delivers video content to the ISP, on behalf of the CDN, when a CDN does
not have a direct peering agreement with an ISP.
Internet Service Provider (ISP) provides end-user/viewer connectivity to the internet.
Client Premise Equipment is in-home or in-office hardware (modems, routers, cabling) and
software which connects end-user devices to an ISP network.
Application/Player is the software running on consumer or business user devices and
interacts with remote streaming services to provide the end-user experience.
Ad Server delivers ad metadata to assist in delivery of ad content to end-users/viewers. The
ad server may be called for client-side or server-side ad insertion.
DRM is an encryption/decryption mechanism which restricts content access to authorized
viewers (i.e., paying viewers).
2
Note: the descriptions of the workflow components are not based on industry definitions but
rather functional descriptions of the component as they relate to streaming video delivery.
//09
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Challenge 1: Metrics Over Events
The dominant streaming video analytics solutions to date have largely focused on the collection
and delivery of predetermined metrics, not the events, measures, and dimensions from which
those metrics are derived. These metrics are then delivered and shared with their customers
(streaming operators) where they are leveraged for alerting, visualization, and analysis. Although
this approach is efficient in terms of data collection (reducing the amount of data which needs to
be captured, stored, and processed) it does have serious limitations.
Poor Root Cause Analysis Support
When a high level signal indicates a problem, engineers may require
observability at the finest level of granularity to perform effective root cause
analysis. This implies the ability to drill down into individual play sessions and
event sequences with supporting measures and dimensions. When metrics are
the only telemetry collected at the source (player, CDN, etc.) or event-level
data is not made available, it significantly hinders root cause analysis.
Poor Transparency and Verification Capabilities
When metrics are calculated without the ability to inspect the events from which those metrics are
derived, it is impossible to independently verify the definition and accuracy of those metrics. This
is often the case with “black box” services: the math and logic behind the calculations is hidden.
What’s more, when metrics from one source fail to align with other data sources there is no way to
determine why. This erodes confidence in the metrics and makes them less useful.
Configuration Lock-in
When metrics alone are collected at the source or exposed through service
interfaces it isn’t possible to customize the metrics after the fact. Changing
metrics, in this case, can involve significant software development, integration,
and testing. However, streaming operators need the ability to freely change
these calculations as new questions arise or requirements change. A metric
answers only one question, whereas a dataset of events, measures, and
dimensions can answer many.
Limited Analysis Options
Beyond the lack of ability to control how metrics are calculated, streaming operators frequently
can’t choose the tools they use to perform analysis. They are boxed into closed systems without
the ability to select the best tool for the type of analysis they want to perform. Analysis may
require specialized visualization or dashboarding capabilities. They may want to join event-level
telemetry with other data sources not available in the closed system. Or a streaming operator
may simply need to create new metrics and dashboards to better understand an issue exposed
by the metrics already in place. Unlocking observability requires unfettered exploration of log-
level telemetry.
//10
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Limited Analysis Options
Beyond the lack of ability to control how metrics are calculated, streaming operators frequently
can’t choose the tools they use to perform analysis. They are boxed into closed systems without
the ability to select the best tool for the type of analysis they want to perform. Analysis may
require specialized visualization or dashboarding capabilities. They may want to join event-level
telemetry with other data sources not available in the closed system. Or a streaming operator may
simply need to create new metrics and dashboards to better understand an issue exposed by the
metrics already in place. Unlocking observability requires unfettered exploration of log-level
telemetry.
Uncorrelated Data Sources
Finally, metrics collection (without supporting events, measures, and dimensions) at the source
makes it impossible to correlate telemetry across services. For example, if you want to
understand the relationship between player-reported QoE and CDN QoS performance telemetry
you may need to join session-level player events and supporting dimensions with the CDN log
events related to that session. This would allow content providers to do things like correlate slow
play start or stall events with CDN cache misses for the same sessions, indicating configuration or
service availability issues.
Correlation is also relevant in scenarios where telemetry data must be enriched with additional
context from other sources. Enrichment of telemetry messages also requires a common identifier
between the telemetry data and enrichment data to perform correlation. We’ll talk more about this
later.
Challenge 2: Data Diversity & Silos
The problem of data diversity and silos is common with big data regardless of the industry.
Bringing data together across multiple sources with different semantics, nomenclature, and
processes can be extremely challenging even when it’s all managed within the same organization.
Naming conventions must be aligned, semantics must be translated or abstracted away, and
identifiers must be correlated across silos to answer questions which span domains.
Within streaming video, that challenge is magnified exponentially. Where traditional enterprises
might have multiple internal data sources to reconcile, streaming providers potentially have to
contend with multiple external providers for each stage of the workflow. What’s more, each
service provider's solution may be (and frequently is) unique relative to other solutions in the
same domain. Imagine the complexity involved in bringing all the relevant data from the streaming
workflow together into a single, manageable dataset. Doing so requires extensive and continuous
software development which takes resources away from developing innovative capabilities or
providing exceptional product experiences.
//11
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
More specifically, data diversity and silos present the following challenges:
Poor Standardization
In simple scenarios, streaming operators could theoretically use only one player, CDN, origin,
encoder, packager, etc. But this is almost never the case, especially over time. In fact, it is
common for streaming operators to use multiple players across multiple device platforms with
multiple CDNs, each with its own unique nomenclature, semantics, and processes. And even if
streaming operators use components implemented by the same company or open source team as
part of a multi-platform strategy, there is no guarantee that those components will behave in the
same way, or that the data will be represented in exactly the same way. Much of the time there
are differences.
As a result of this situation, building a single set of consistent metrics, dashboards, and
operational methods becomes quite difficult. Each player or service may require a custom
approach and ongoing maintenance to preserve observability as new versions are released or
new services are adopted.
Poor Data Correlation
One of the primary challenges with data silos is finding ways to integrate distinct data sets to build
a larger, more comprehensive view. The key to breaking down silos is to find common identifiers
which support correlation from one source with another.
For example, player-generated telemetry helps support an understanding of the end-user
experience. You can observe how long it took to start playback after the user pressed play; you
can observe how many times a stall occurred and how much time the user spent watching a
spinning wheel or frozen frame; and, separately, you can look at CDN cache logs to understand
where and how often there is a cache miss at an edge PoP or if an origin service is experiencing
performance issues. But what if a streaming operator wants to examine and understand the
relationship between play delay or video stalls within a single play session and specific activities
within the services which supported that session? The goal is to be able to answer critical
operational questions. For example, in the case of slow video start times:
Was it primary content or an ad that was being requested?
Was there a CDN cache miss when the video was slow to start?
Did the CDN request have to go all the way back to origin?
Was the origin responsive or was there high latency? Was there a failure?
Was there network congestion between a user’s ISP and the CDN?
Answering these kinds of questions requires correlation of telemetry across components in the
streaming video workflow. But even with correlation of player-generated telemetry with CDN logs
or other sources, isolating the root cause of a QoE issue and understanding its cascading effects
requires a deeper level of precision.
//12
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Limited Root Cause and Cascading Effects Analysis
Root cause analysis can frequently require a deep understanding of a distributed system and its
dependencies. This kind of information is not readily available to streaming operators today. For
example, even with player-generated telemetry correlated with CDN log lines, streaming operators
still have limited insight into the sequence of events which fulfill content requests and the
performance at each node in a chain of such requests. They may receive cache logs but those
logs don’t expose enough information about the end-to-end chain of hosts or PoPs to provide the
full picture. What’s required is clear, actionable insight into triggering events and their cascading
effects at every hop to efficiently zero in on the problem.
Consider this: a streaming operator observes a high stall rate (frequent and/or long video
interruptions). How do they determine the triggering event? Stalls could be a result of performance
issues with the player, home/ISP/transit networking, multiple levels of CDN caches or PoPs, origin
services, dynamic packaging services, etc. Knowing where the problem started (with some level
of precision) and how downstream services responded to that delay would alleviate a significant
blindspot for the streaming operator.
Consider another scenario: in an ad-supported streaming service, the ad fill rates are low and not
generating expected revenues. How does the operator discover the root cause? Is the gap due to
ad server errors, content defects, delivery failures, or perceptual quality issues? And, again, if it’s
a delivery or perceptual quality issue, what is the root cause? The problem could be deep in the
workflow service chain, requiring relevant QoS data from the service provider to efficiently resolve
the issue.
The challenge of understanding end-to-end performance in distributed systems is not new, and
solutions exist. More specifically, distributed request tracing has been in use for many years to
observe and troubleshoot cloud-based, microservice architectures. But it is typically done within
the confines of a single service or services owned by a common entity. Frequently it’s done within
a single network or a set of related networks.
For streaming operators employing third-party services for CDN, Origin, DRM, encoding, ad
technologies, and a vast array of other services, having the ability to trace individual HTTP
requests through the stacks of their service providers might seem like science fiction. But if those
streaming operators want to achieve the QoE which companies like Netflix and Youtube provide
on their own proprietary architectures, this is a nut the industry must crack.
//13
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Challenge 3: Data Latency
Finally, for engineers (SREs, DevOps, etc), whose job is to protect service availability and end-
user QoE, time is of the essence. The more severe the impact on the viewer’s experience the
more urgent it is to resolve. Engineers and automated responses must have relevant telemetry
within seconds or minutes at most, not hours or days. Therefore this data must be available as
close to real-time as possible. And the data must paint a complete story (as much as possible) so
correlations with other relevant data sets must also be done within seconds or minutes.
Today this is not the case for the vast majority of streaming
operators. At best they may get alerts which signal a
problem in minutes, but getting to the underlying data that
informed the alert or data from multiple sources across
multiple providers, may not be readily available. And
without real time correlation of diverse datasets, root cause
analysis may take the primitive form of emails, phone calls,
Slack messages, or an all-hands-on-deck war room. This
shotgun approach is quite common but frequently doesn’t
yield the desired results. More systematic and effective
methods are necessary to achieve even exceptional QoE.
//14
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Industry Observability Challenges
The streaming industry has recently begun to embrace more advanced forms of observability,
especially as leading analytics services like Datadog, Tableau, and Looker have enabled such in
their tools. Organizations of all kinds are realizing the importance of real-time access to data from
multiple, correlated data sources when making critical business decisions quickly. For streaming
operators having such observability can mean the difference between a happy viewer and a
churning subscriber. As such, there are a number of trends within the streaming industry which
foster more advanced forms of observability.
CDN Log Streaming
Over the last decade, CDNs have recognized the need for streaming operators to have insight
into the performance of the services and components which support delivery of their content. As a
result, many CDNs have developed log streaming capabilities. By leveraging these services, CDN
customers can stream content request logs to other services for analysis. In many cases these
logs are delivered in near real-time, within seconds or (at most) a few minutes. These services
can also send data to storage services like S3 or BigQuery for analysis in a variety of tools or all-
in-one analytics platforms like Splunk or Datadog.
CTA-5004: Common Media Client Data
The need for real-time operational data sharing between players and CDNs has come to the
forefront with the release of CTA-5004 - Common Media Client Data (CMCD). This standard
defines a set of player measurements and data points, conveyed by piggybacking onto content
requests from player to CDN, which CDNs can use to optimize delivery performance.
But, just as importantly, it defines a more general method for players to convey data to CDNs,
leveraging a standardized set of HTTP headers and querystring conventions. CMCD key/value
pairs are then logged by CDN caches and associated with incoming HTTP requests at the logline
level. As a result, CMCD has enabled correlation between player QoE and CDN QoS telemetry.
For example, the CMCD key called “sid” (session ID) identifies the playback session for a
particular piece of content. Recording this key/value pair in both player and CDN logs allows
correlation across the two log streams. With this data in hand it is far easier to answer questions
about the impact of CDN cache performance on the end-user playback experience.her for
integrated analysis.
//15
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Leveraging CMCD to join player and CDN data:
1.Identifiers are set by the player as HTTP request headers or querystring arguments for each
content request and stored in CDN logs.
2. CDN logs and player telemetry are captured & stored together for integrated analysis.
End-to-End Workflow Monitoring
In 2020, the Streaming Video Alliance (SVA) released Best Practices for End-to-End Workflow
Monitoring , which promotes end-to-end, multi-point, asset-correlated monitoring to drive a more
holistic approach to streaming video observability. The goal of this framework is to help
stakeholders quickly and efficiently detect and diagnose impacts to the viewer experience and
help identify root causes of QoE impacts across the video workflow.
The premise of the Alliance’s effort is that any stage in the process can cause downstream effects
which negatively impact the end-user experience. Therefore, it is necessary to be able to observe
the full set of activity logs at every stage, and group those stages together for each streaming
video asset. To be more specific, a given piece of content will go through the stages of ingestion
from source, encoding (compression), transcoding (recompression into one or more quality
variants), packaging, origin storage, and delivery from origin to CDN to the end-user device. To
track content performance across all stages, the streaming operator needs to correlate assets and
activities in logs via common identifiers.
The flow above may seem relatively simple, but it can get a lot more complicated. If the content is
3
This SVA document is recommended reading for this whitepaper.
//16
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
encrypted, then DRM services and libraries will be employed to encrypt and decrypt content as
needed. Integrating DRM service logs would be helpful in this situation. Or, if server-side ad
insertion (SSAI) is in use, then content will be dynamically integrated into active streams via ad
selection and stitching software. In this case, beyond normal QoE events and dimensions, it may
be necessary to integrate telemetry from those services as well to determine root cause of ad
performance issues. To answer a given question only a subset of stages may need to be
represented. But to answer the full spectrum of QoE-related questions, telemetry from all stages
must be accessible.
Distributed Request Tracing
Building on the Alliance’s End-to-End Workflow efforts, the SVA’s Measurement/QoE Working
Group has an active Distributed Request Tracing initiative which, if successful, will vastly improve
streaming video observability and, with the proper investments, end-user QoE. The goal of this
effort is to bring the powerful capabilities of request tracing, which is normally implemented within
a single company’s production environment, to the chaotic, multi-service, multi-company
architectures common to most streaming video services.
The broader technical industry also sees the need for multi-service tracing as evidenced by the
recent formation of the W3C Distributed Tracing Working Group which is addressing
interoperability between different distributed tracing tools for this very purpose. Realistically, to
build request spans across services owned by different companies you must accommodate and
integrate a variety of tools and frameworks.
Success for the SVA initiative means that new methods and services emerge which allow
streaming operators to rapidly troubleshoot streaming video issues like long play delays, frequent
stalls, or low bitrate renditions down to player, DRM, networking, CDN, origin, or other contributing
factors.
//17
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Industry Observability Challenges
Now that we have a sense of the observability challenges and trends in the streaming video
industry, let's articulate the elements of advanced observability necessary to deliver exceptional
viewer experiences. What’s required to move the industry from the settler stage to town planner
stage of maturity?
Ubiquitous, Low-latency Event Logging
As an industry we must abandon solutions focused exclusively on metrics to one focused on
events, measures, and dimensions. Doing so unlocks vast opportunities to improve observability
spanning real time operations, audience measurement, ad display verification, content strategy,
service optimization, etc. As previously stated: a metric answers only one question, whereas a
dataset of events, measures, and dimensions can answer many.
In fact, by moving to a model which relies on event-level logging many metrics-based player
collectors become obsolete. This is a huge side-benefit. The vast majority of player collectors
redundantly gather and/or perform calculations on the same data within the same application. This
leads to SDK bloat with numerous plugins and/or libraries. If event-level telemetry is collected at
the source and propagated to all the platforms that require it, video application development and
the applications themselves would be more efficient. And, adoption of new services that leverage
the data would be simple and straightforward, requiring little or no integration for the streaming
operator.
Multi-Point Data Collection
It’s not enough to collect telemetry from the player to fully understand the viewer’s experience,
especially when things go wrong. Every service in the workflow which supports streaming video
can contribute to the larger observability story. Therefore, as an industry, we should collect event-
level telemetry from every stage in the workflow and from every major provider for those services.
There are two categories of telemetry which require distinct collection strategies: player data and
service data.
Player Data Collection
Telemetry collection from streaming video players requires the integration of SDK libraries which
gather player events, measures, and dimensions. The SDKs must be embedded in the end-user
application and deliver data, in near real-time, to storage or analytics platforms.
Service Data Collection
Ideally, services which are leveraged during the delivery of streaming video will have real-time log
streaming capabilities that can route telemetry to configurable endpoints. This allows a streaming
perator to determine where and when they want data delivered for analysis. It also allows them
//18
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
to co-locate service log data with player telemetry for integrated analysis. Services for all of the
stages of the streaming video workflow (CDNs, origins, packagers, transcoders, encoders, DRM,
and networks at each hop along the way.) are candidates for data collection.
Multi-Point Data Correlation
End-to-end, multi-point correlation is the clear path forward to eliminate blind spots which hinder
rapid response to operational issues and contribute to longer cycles of continuous improvement.
Correlation is only possible when telemetry contains common identifiers which allow logs from
one stage in the workflow to be joined with related log data from another stage.
For example, referring to the SVA’s workflow construct of correlated assets, a streaming operator
may want to understand the perceptual quality (or other performance dimensions) of a specific
piece of content in their catalog. Getting the full picture requires a content identifier to be
propagated throughout the logs of systems which touch that content (from origin through encoding
and transcoding to CDN delivery and, finally, to playout). With identifiers linking the data sources
together a streaming operator can more efficiently pinpoint possible causes of degradation in
perceptual quality.
But content assets are only one of many dimensions of interest. Suppose real-time monitoring
systems alert about increased play delay and stalls in a specific region. A streaming operator
would want to know if that delay is caused by CDN caching issues, origin slowness, network
connectivity/capacity issues, or a combination of issues. In this case, it would be helpful to identify
the end-user play sessions which demonstrate the symptoms in question and join player telemetry
with the log lines from CDN edge caches, middle tier/shield caches, and origins which were
specifically involved in that play session. Joining this data requires a common session ID to be
propagated and stored in relevant log lines for each source.
Identifier Propagation
There are a number of interesting dimensions which operations, engineering, and business
people need to answer common and frequently urgent questions. Below are a few examples of
useful identifiers.
Content Session ID - identifies playback of a specific piece of content at a
specific point in time by a specific end-user.
App Session ID - identifies a continuous session streaming content, which
can include multiple Content Session IDs.
Content ID - identifies the content being viewed.
Customer ID - identifies the customer viewing content.
Device ID - identifies the specific device being used to view content.
Device Type ID - identifies the type of device being used to watch content.
//19
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
These identifiers can be set and conveyed by an application through the embedded player and on
to the CDN by piggybacking on manifest and segment HTTP requests using CMCD-style
querystring parameters or header arguments.
Data Co-location
By placing the data from different stages in the workflow into a single database or storage service
and joining that data across domains via common identifiers, streaming operators can now
efficiently ask and answer specific, meaningful questions based on a reliable dataset.
Domain Data Standardization
One of the major challenges to observability, as mentioned previously, is data fragmentation:
different data conventions and semantics from different sources.
Players, CDNs, origins, DRM services, packagers, and more all have a unique job, log different
data, and implement different semantics. And, of course, each implementation can be unique
within the same domain. One transcoding provider may do something entirely different with
respect to event logging than a competitor or open-source alternative. Assuming streaming
operators are likely to rely on multiple providers for the same type of service, either in parallel or
over time, means hat a method for normalizing the data is critical to achieving data insight, to
making sense of the combined information and, ultimately, robust observability.
One solution is to define a set of domain-specific data translations (i.e. a standardized set of
key/value pairs which represent events, measures, and dimensions). These translations must
precisely describe the possible keys and acceptable values for each data point. For a streaming
operator to leverage telemetry collected from different sources, collectors must also act as
translators. Once delivered for analysis engineers and data scientists can build consistent,
reliable, and meaningful, metrics, dashboards, and reports for each domain because everything
from that domain has been validated and mapped to known definitions.
Real-time Enrichment
In addition to real time telemetry which describes a play session across services, there are offline
or less real time data sources which can provide additional context. The data from these sources
may be used to augment log messages which contain specific key/value pairs. If appropriate
identifiers exist then these sources can be correlated with real time telemetry messages as they
are processed. Separately it may be helpful to perform certain calculations as data is processed to
simplify analysis at a later stage. This kind of on-the-fly transformation is important for two
reasons. First, some analytics platforms may not be able to perform certain kinds of joins or
calculations at query time. Second, even if they can perform the necessary operations, doing so
can take precious time impacting real time use cases.
//20
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Summarizations of quality information along relevant axes can assist root cause analysis efforts.
For example, if a large ISP provides packet loss, jitter, or other degraded signals by ASN and
individual play session IP address data is converted to ASN (for anonymization and matching
purposes) the ISP data could be used to enrich play session telemetry with what is known about a
viewer’s ASN at that point in time.
Enrichment via metadata can also be equally powerful. For example, ad campaign metadata,
which may identify the CPM value, advertiser, or other financially-relevant data can augment play
session messages related to video ad playback to understand the ad revenue associated with a
given viewer. This can be extremely useful when optimizing campaigns, defining new campaign
strategies, or understanding the impact of degraded experiences on ad performance.
Finally, some analytics platforms may not readily support certain calculations that a streaming
operator needs for their business. Addressing this gap would require some kind of additional data
processing. For example, determining how far a viewer made it through a piece of content during
a playback session may require sorting a set playback events by event timestamp to get the
playhead position of the last event. Fabricating an end-of-session event which is easily identified
with summary information would simplify subsequent data processing and analysis.
Content Request Tracing
In addition to events and metrics, advanced streaming video observability requires the insight that
only distributed request tracing can provide, especially when making content requests to CDNs.
This observability must span multiple services, delineating sufficient architectural granularity within
each service to pinpoint the source and contributing factors to latency, degradations, and hard
failures.
For example, in a VOD scenario, if a streaming operator wants to pinpoint the contributing factors
//21
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
to increased play delay and low video quality, it is helpful to understand the latency from player to
CDN edge, from CDN edge to CDN middle tier, and from CDN middle tier to origin. By looking at
latency at each hop compared to historical latency for those same hops, it is easier to determine
where latency has increased and where to investigate.
To achieve this, streaming applications and players require the following capabilities:
Support for generation and end-to-end propagation of request identifiers from player to CDN
and so forth on a request-by-request basis.
Support for the collection of request and response data for each stage in the workflow (player,
CDN, origin, etc.). Ideally, such data would include request id, request duration, and http
response codes for each request/hop at a minimum.
The ability to correlate HTTP requests with the specific types of objects being requested by
the player (manifests, chunks, byte ranges, breakouts of muxed a/v vs. audio vs. video, vs.
timed text).
Analytics support in the form of metrics, alerts, and visualizations which leverage trace data.
Data Sharing
While streaming operators are the most invested in the QoE of their own viewers,
they are not the only party involved in service delivery who would benefit from
QoE telemetry. In fact, service providers such as CDNs struggle to infer viewer
QoE based on their own QoS telemetry. So, just as streaming operators need
insight into the services which support them (via offerings like CDN log streaming),
service providers need insight into the viewer experience they support on behalf of
their streaming operator customers.
Standardization makes data sharing and analysis across similar services scalable and efficient.
Metrics and visualizations can be built once and leveraged across any number of services of the
same type. This advantage goes both ways. Streaming operators can observe the performance of
their service providers in isolation or compared to one another. Likewise, third party service
providers, if given access to anonymized or sanitized player QoE data from the streaming
operator, can build generalized metrics, alerts, and dashboards across customers and player
implementations they support. This first-hand, real-time data source would enable new
opportunities for service improvement not currently possible.
Smart Sampling
Collecting, standardizing, enriching, and delivering all event log data from every streaming
application and supporting services in the workflow can be expensive at scale. It also may be
unnecessary. At low volumes of data, QoE signals can be erratic or noisy. In this case a streaming
operator may want as much data as possible to determine if there is a broad degradation of
//22
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
experience. However, as usage and scale increase, statistically significant signals can be derived
from a subset of the overall data set.
In addition, some analytics and storage platforms have hard limits on request rates and storage
which hinder full data capture
Sampling is an obvious solution, but it must be done in a way which does not prevent analysis of
playback sessions and correlated logs from supporting services. Therefore, sampling must be
done at the playback session-level such that all log data is collected, standardized, and delivered
from the player, CDN, and backing services for selected play sessions.
Flexible Analytics
Once we shift from collecting metrics to collecting event logs, the possibilities for analysis are
endless. Player telemetry can be used to analyze anything from audience size for a live event to
content popularity across many pieces of content, to ad delivery verification and measurement, to
service performance optimization, to real-time production incident troubleshooting. And the tools
best suited for those tasks will vary depending on the use cases and types of analysis relevant to
each function. Furthermore, many companies make big investments into specific analytics
platforms and they want to leverage those investments as fully as possible.
Finally, it is virtually impossible for streaming operators to predict in advance all of the data points
they will need collected for analysis. And collecting all possible data points all the time could
become expensive quickly. Therefore, streaming operators need the ability to easily change the
events, measures, and dimensions they require to build their metrics and dashboards. This allows
for iterative exploration and learning, which can unlock powerful insights and opportunities for
service improvement.
All of these conditions point to the need for flexibility when it comes to analytics platforms. It will
rarely be one-size-fits-all. Flexibility is key.
//23
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
The Video Data Platform
While streaming operators and their service providers may try to build the capabilities above
independently, it’s a heavy lift. Of course, it happens a lot in enterprise software development: the
belief that critical aspects should be built in-house. But an observability solution isn’t a competitive
differentiator without continuous, significant investment. A streaming operator would be much
better served by outsourcing this function to focus on what matters - differentiated, engaging
product experiences, exceptional content quality, and a variety of investments that directly drive
business growth. Only the streaming operator can affect these areas of concern.
As such, allocating development and engineering resources to build an ecosystem of services
around observability data could be a bad business decision. The ideal scenario is that the
functionality necessary to collect, standardize, enrich, and deliver streaming video QoE and QoS
telemetry is provided as a building block for streaming applications, a layer in the streaming video
technology stack.
This layer, the Video Data Platform
(VDP), is a low latency, highly
scalable service which integrates
data from all stages of streaming
video ecosystem. The VDP
provides the full spectrum of
functionality necessary to meet
modern observability challenges:
Standardized data dictionaries for each stage in the workflow
Plugable player collectors for player/platform variations
Log collection for integrated services (CDNs, origins, encoders/transcoders, ad stitchers, etc.)
Data delivery services that propagate telemetry to popular analytics and cloud storage targets.
Log collection for integrated services (CDNs, origins, encoders/transcoders, ad stitchers, etc.)
Data delivery services that propagate telemetry to popular analytics and cloud storage targets.
Data delivery services that propagate telemetry to popular analytics and cloud storage targets.
Enrichment data source integrations with live message augmentation
Data correlation mechanisms
Smart sampling capabilities
Data summarization capabilities
Distributed request tracing support
//24
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
A broad set of player telemetry collectors
A broad set of CDN log streaming integrations
Integrations with other workflow services like encoders, packagers, DRM, etc.
A broad set of storage and analytics integrations
Configurable collector, connector, and data point configuration
Undifferentiated Heavy Lifting
As previously mentioned, successful businesses focus on leveraging the unique skills and
investments which differentiate them from their competitors. If you’re a streaming operator, that
means creating or licensing compelling content, building innovative user experiences, or
optimizing internal costs to increase profit margins. And then there’s everything else - the
investments which every streaming company makes just to be in business. In other words, table
stakes.
Werner Vogels, CTO of AWS, coined the term “undifferentiated heavy lifting” to describe the
common work of building data centers and providing virtualized services to leverage them. Being
good at building data centers does not differentiate one streaming operator from another,
assuming the same level of technical competence and commitment. This is why so many
companies have moved to the cloud and why no startup today considers building their own data
centers unless they have a very compelling reason to do so. The Video Data Platform provides
the undifferentiated heavy lifting for streaming operator observability data.
Defining streaming telemetry standards and translators for every stage in the workflow (players,
CDNs, packages, encoders, DRM, etc.) then building out collectors for major platforms in each
domain is a daunting task for any company. Quite arguably, this is work which can and should be
done once and leveraged repeatedly. The same is true for generalized enrichment and correlation
mechanisms which make the data more useful, or data delivery to common third party analytics
providers. To better understand the leverage provided by a VDP, let’s explore what it means to
provide data collection, standardization, correlation, enrichment and delivery as an integrated
service.
Data Dictionaries
As previously mentioned, observability for the streaming industry involves a Wild West of
platforms and services. There are emerging standards which seek to reign in the chaos, but
implementations still vary and innovation frequently outpaces standards initiatives. It’s a moving
target at best. In the face of this reality, the most viable solution is to create consistent translations
within a single platform, in the form of well-defined data dictionaries, partner with key firms in each
streaming workflow domain, and foster an ecosystem of data integrations.
//25
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Integrated Sampling
When streaming operators reach a certain scale, there is the potential for collecting a massive
amount of data across many stages in the workflow. Sampling becomes critical to the
management of costs and capacity. However, the sampling must be smart, which means it must
be consistent across the stages in the workflow. Whole sessions must be collected and when a
play session is selected for sampling, all correlated logs lines from all integrated services should
be collected as well. This means that sampling algorithms must align across all collectors. Doing
so within a single integrated platform increases the likelihood for success by providing a well
orchestrated suite of correlation, selection, and validation mechanisms.
Pluggable Analytics
As previously mentioned, streaming operators must be able to choose the best analytics
tool for the job. In some cases the same company may want to use multiple analytics tools
depending on the users and their specific areas of concern.
To address this need the VDP must have pluggable analytics. In other words, it must
provide to streaming operators the ability to easily configure delivery to one or more third
party services for storage and analysis. These services may provide object storage (e.g. S3,
GCS, Azure Blob Storage) which can be leveraged by multiple analytics tools (e.g. Looker,
Tableau, Snowflake) or integrated storage and analytics (e.g. Splunk, Datadog, Sumologic).
In order to support pluggable analytics the VDP must perform the following operations:
Data packaging and formatting to conform to each target service’s APIs and data
formats.
Deliver data to storage/analytics services in compliance with their service-specific
batching, rate limiting, and quota requirements.
Delivery of different data points to multiple targets with variable sampling configurations.
The flexibility outlined above will ensure the right data goes to the right tool for the job for
each stakeholder, maximizing their effectiveness.
Dynamic Configuration
Observability is frequently a process of discovery. The data points and dimensions required for
various constituencies will change over time as new opportunities, issues, or questions arise. In
the case of production incidents, collecting additional data points may be urgently needed to
isolate root cause. To accommodate this need the VDP should allow data point collection,
standardization, enrichment, and delivery to be configurable such that changes take effect within
minutes.
//26
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Observability Data Exchanges
Once streaming operators and their service providers are participating in the same VDP, exciting
opportunities emerge. Player telemetry, which informs viewer QoE and consumption habits can
be shared with any of their service providers to drive internal improvements and better support. Of
course, care must be taken to protect consumer privacy and proprietary data, but this is
achievable with appropriate controls.
Example Opportunities:
CDNs can use QoE data in combination with existing QoS data to tune alerting and
build more responsive failover or recovery mechanisms.
Encoding services can leverage QoE data to uncover perceptual quality or audio/visual
sync issues.
Dynamic transcoding and packaging services can adjust bit rate ladders on the fly to
best fit the viewer’s ecosystem of devices and network types.
ISPs can share summarized network performance data to enrich player telemetry for
streaming operators which may lead to more efficiency for both parties.
Synthetic monitoring data can be combined with runtime data sources to build more
accurate detection, alerting, and troubleshooting mechanisms.
Advertisers can access campaign monitoring dashboards or reports directly from
Content Operators for more granular, real-time understanding of audience engagement
and campaign performance.
Of course, that list is just a small sample. The possibilities are endless when the ecosystem
of real-time, event-level, correlated data is collected, standardized, enriched, and delivered
wherever it’s needed.
Lightweight Integration
Since one of the primary goals of the VDP is to provide undifferentiated heavy lifting the
integration of the VDP itself must be simple and lightweight. Streaming operators should be able
to easily tap into the VDP ecosystem by:
Integrating and configuring pre-built player collector SDKs into their applications.
Integrating player to CDN session correlation via methods provided by the VDP.
Configuring CDNs and other services to stream log data to the VDP.
Configuring storage and analytics services to receive standardized telemetry.
Configuring the VDP to route standardized, enriched data to selected storage or analytics
targets.
//27
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Achieving Exceptional QoE with a VDP
The OODA Loop and MTTR
The OODA loop is the cycle of observe–orient–decide–act, developed by military strategist and
United States Air Force Colonel John Boyd. Boyd determined that fighter pilots who could rapidly
observe their environment, orient themselves (who is friend and who is foe, where are those
entities located, where are they going, how fast are they moving), make a decision (attack, retreat,
regroup), and act, were the most likely to succeed and survive.
This model applies equally well in the realm of streaming video operations where engineers are
tasked with defending and preserving viewer QoE which can ultimately have an impact on churn
rates, subscription revenue, ad delivery, and ad revenue. And having real-time, reliable,
intelligible, integrated telemetry accelerates their ability to iterate through the OODA loop and
drive down mean time to recovery (MTTR) for end-user impacting issues.
Rapid Root Cause Analysis
One way that MTTR can be reduced is by enabling more efficient and effective root cause
analysis (RCA). Effectively integrating data from as many stages in the workflow as possible
provides operations engineers opportunities to more rapidly triangulate an issue and isolate its
root cause. This is especially true if efforts to introduce distributed request tracing into the
streaming video delivery workflow are successful. In that case, latency and error rate metrics for
each hop in the delivery chain can quickly expose the weakest link. However, even without trace
data, having additional, well-structured context from each stage in the workflow can only bolster
observability and accelerate the discovery process.
Self-healing Systems
When data is reliable, intelligible, actionable, and timely it’s possible to consider automated ways
of reducing MTTR. What’s required is being able to determine, with confidence, that specific
patterns in telemetry indicate a specific underlying cause. Once such a relationship is established,
it’s possible to engineer a response which is comparable to the actions that would be taken by an
operations engineer from a runbook.
Here are a few examples:
Automatic rollback of a new version of web player deployment based on comparison of old
and new versions in production and a correlation of release timing with increased error rates.
If QoS data from supporting services do not indicate upstreaming problems then the rollback
can likely be done with confidence.
//28
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Automated removal of a DSP from the advertising chain when it returns ads with high latency
and error rates.
Failover from CDN A to CDN B in region X based on lower-than-expected bitrate selections
from player telemetry and CDN logs indicating connectivity issues through a peered
connection to a local ISP.
Dynamic removal of one bitrate in the bitrate ladder from a content manifest based on
correlation between increased runtime playback errors and errors in encoding logs for the
same content.
In addition to the simple automation described above, the VDP can enable more sophisticated
self-healing mechanisms for common use cases by leveraging machine learning pattern-matching
algorithms. The aggregate effect is that operations engineers can focus on new problems that
haven’t been automated and proactive service optimization rather than repeatedly fighting well
understood fires.
Service Optimization
In addition to operational use cases, the same telemetry can be used for longer term service
improvements. For example, a streaming operator may be migrating from Exoplayer to an Android
native application with a new set of encodes specific to the new player implementation. By
analyzing player, CDN, and encoding log telemetry in an A/B testing scenario, the operator can
best determine which implementation performs better.
And service providers which support streaming operators can also benefit from VDP-supported
observability. For example, once CDNs have access to their customer’s QoE data, they can start
to identify patterns in their own system logs with outcomes for the viewer. This may lead to
architectural or policy changes which improve the delivery experience, drive efficiencies, and lead
to greater profitability.
//29
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Beyond QoE: Business & Product
Optimization
While this document has been primarily focused on QoE, the very same data used to analyze and
improve the viewer experience can also be used to answer countless other questions. In fact,
event-level player telemetry can easily be leveraged to determine content popularity, audience
size, ad profitability, drop off rates, successful ad deliveries, and more. And, as previously
mentioned, with the full set of event-level data delivered to a VDP from a uniformly designed
collector SDKs, these functions could be addressed centrally via cloud services, with greater
flexibility, deeper levels of insight, and leaner, high performance applications.
In addition, collected telemetry can also be directly leveraged in product features to improve the
viewer experience. For example historical per-device-bandwidth and selected bitrate information
can be collected and fed into a personalized algorithm which predicts the best starting bitrate for
the next session. If a viewer has a DTV at home that has the bandwidth to play 4k content on a
regular basis then it makes sense to start the next title at 4k rather than starting at a lower bitrate
and ramping up each time. This provides an overall higher quality viewing experience.
//30
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.

Advanced Streaming Observability
and the Video Data Platform
Conclusion
In this paper we’ve laid out the challenges facing the streaming industry settlers: pre-summarized,
latent, siloed, uncorrelated telemetry simply doesn’t provide what’s necessary to enable a
competitive, high quality viewer experience in today’s streaming marketplace. The industry as a
whole must embrace event-level, real-time, correlated, enriched data to maximize observability,
learning, and actionability. In terms of data analysis, streaming operators benefit from the ability to
choose the right tool for the job at hand. Much of the time that means different tools for different
use cases or constituencies. Flexibility is key.
We have also explored the vision of a unifying video data platform which provides the services
necessary to capture, standardize, enrich, and deliver telemetry wherever and whenever content
providers choose. Such a platform acts as a nexus for an ecosystem of services and data which
mutually support each other in achieving exceptional QoE and QoS for all involved. This is what
the town planner stage looks like for the streaming video industry.
Datazoom is the first Video Data Platform. Check out our website to learn more.
//31
Copyright © 2021, Datazoom Inc. and/or its affiliates. All Rights Reserved.
