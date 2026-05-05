---
id: pdf-ff720bad942e
type: pdf
title: FallbackPDF__ff720bad
url: ''
authors:
- Baker
- Giles
ingested_at: '2026-04-29T16:21:33Z'
content_hash: sha256:dbe7b190a59e66d6fd7bcaa2bf3df3de7f10bbb135c728214edab7267e4f1637
source_path: raw/pdf/pdf-ff720bad942e.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 4
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__ff720bad.pdf
published_at: '2025'
---
xCD-1: GB questions about phase 1
DRAFT RESPONSES _ AG_ 06192019
General
1. Is the business envisaged for phase 1 independent of other Dolby businesses? Can we
think of it as a standalone investment in productizing a new innovation? How defensible
is it on its own?
• xCD focuses on the development of a “network-centric” multimedia coding and delivery
capability by integrating source and network coding1 along with cloud-based experience
monitoring supporting on-demand live and file-based media experiences delivered over
unmanaged and managed IP networks.
• Our goal is to offer improved media-powered experiences at lower operational costs
through more effective use of network storage, network utilization and delivery capacity
as well as OTT media services delivered over them.
• We will build and grow xCD-1 as an independent, standalone business for Dolby. In
Phase One, we will offer OTT and vMVPD services a content delivery and analytics
solution focused on material improvements in Quality of Experience. xCD is a standalone
investment to build and scale a defensible solution to measurable industry problems
related to content delivery efficiency and effectiveness through use of an innovative
new network-aware media format build on Dolby Source Coding and Random Linear
Network Coding (RLNC). The business is reasonably defensible given the unique
methods derived from the combination of Dolby IP and a non-exclusive license to RLNC
IP from CodeOn. However, the space is generally attractive and should be considered
competitive.
• The OTT overlay solution will be comprised of a software network coding solutions,
streaming playback modules for various device platforms, a cloud service for real-time
monitoring of the end user experience, and machine-learning2 powered optimization
service to deliver the best experience at the lowest cost.
2. Paragraph one talks about codec-agnostic delivery etc.; paragraph two describes a new
multi-path-multi-source media format. It’s not clear to me how Dolby vs non-Dolby
codecs fit in – is there any advantage to using a Dolby codec?
• xCD-1 will bring to market a new, network-aware media format that is generally codec-
agnostic and deployed in the just-in-time xCD-1 Encoder that processes finished assets
(e.g. output from Hybrik) using Dolby source coding innovations. The xCD-1 Decoder will
1 xCD-1 is envisioned to utilize RLNC from Code On – Random Linear Network Coding [RLNC] provides network utilization and
throughput improvements, improved robustness, decentralization, reduces transmission latency, simplifies connection state
management and allows successive coding operations without increasing overhead..
2 Part of research plan

be integrated into device playback frameworks (e.g. commercially available players such
as JW Player, exoplayer, etc.).
• We believe that the early phases of business growth call for a generally agnostic
approach to codecs. However, integration into Dolby playback tools such as MSx is open
for evaluation. As we move to Phase Two and beyond, deeper integration with Dolby
codec ecosystems (e.g. AC-4…) offers the opportunity to develop advantages around
hyper-personalization and hyper-efficiency as we develop a data-driven experience and
resource management system deployed as a software-based overlay at the network
edge. Phase One will also include a cloud-based Experience Monitoring Database (EMD)
that serves as both a control plane and analytics hub. Over time, aggregation of service-
network-device data in the EMD, individual, endpoint, and environment sensor and
heuristic data, and encoding metadata will create material strategic product
development options beyond network resource optimization. These include rich media
analytics and hyper-personalized content discovery services.
3. What are the major assumptions about product, value proposition, and customer needs
that we are making that would jeopardize the opportunity if they were incorrect?
• We believe that we will be first or near-first to market with a solution based on source
coding and RLNC. In the event that this type of technology solution is brought to market
more quickly and at lower costs (either as a platform feature or through standardization
in (e.g.) 3GPP by Huawei or others) we could lose our advantage in the market.
• We are basing our assessment of willingness to pay on a limited sample set and a few
early-stage discovery engagements with services. Indications that services would value
our QoE improvements as an 8-12% premium on CDN costs may not hold true.
• We have not yet scoped the integration costs with additional playback environments;
the complexity of this development may escalate costs well-beyond early estimates.
• We believe that Dolby’s credibility as the provider of “quality first” media ecosystems
will transfer into this new space and allow us to onboard customers quickly and at
moderate acquisition cost following the Proof of Concept phase.
• We believe that we will be able to develop (1) a network operations capability and (2) a
robust data science expertise in a reasonable period to support this product.
• We have not yet fully identified the contractual risks inherent to operating a network-
services business, including by not exclusive to Service Level Agreements and
indemnification. So, we don’t know if the expectations of the market will align to
Dolby’s historic appetite for indemnification risk.
•
Customers

4. Who are the first customers and what makes them attractive? What do they have in
common? How are they different from the next round of customers (trying to get at
what might make scaling hard)
• Our bottoms-up analysis sized the near-term SAM based on a limited list of OTT and
vMVPD services not developing in-house CDN solutions. These early potential customers
- ranging from OTT pure-play Curiosity Stream, OTT programmers Showtime and HBO,
OTT services such as Hulu - generally share the following characteristics: (1) more than
1M subscribers, (2) a multi-CDN delivery strategy, (3) weighted emphasis on VOD
content in quality ranges up to UHD, (4) a level of technical sophistication that makes
the xCD-1 proposition intrinsically interesting to a technical decision maker.
5. Who needs to sign off at the target customers? (One of the nice things about Hybrik is
they’ve been able to sell without having to talk to senior folks and getting wrapped up
into strategic decisions. There are pros and cons though.)
• VP level (+/-) responsible for video delivery and CDN contracts.
6. Where are the friction points for a target customer to adopt the anticipated solution?
Connecting to their current solution, integrating into player, etc.?
• Integration of their Origin library to the xCD Encoder
• Player integration (native or not is non-issue)
• Integration of analytics feed into their business management solutions
• Integration of their CDN contracts for business rule integration
• Displacement or bake-off with current CDN management solutions – we need to
overcome switching costs with a significant margin of improvement on the traditional
QoE KPIs (
Product
What is the envisaged product offering? The paper says “delivery and analytics as-a-service”
but that doesn’t give much info about how it will be packaged and delivered. Do we host some
of it, they host some it, who uses it, what info does it need/provide, etc.
xCD is a player-intelligence infrastructure.
Does phase 1 require a dual-ended approach, with our technology somehow in the player? How
do we expect that to be achieved?
XCD is a dual0ended system with tech embedded in the player to manage the NWcoding
components, etc.
Execution
What new capabilities do we require in order to create this vs ones we already have? Sales,
support, product, engineering, business, legal terms, etc.

Data analytics, data platform, NW operations (managed cloud data platform), Inside sales,
outside sales, support, field engineering, player engineering (SW); SLAs, indemnification.
Business
Can you explain the pricing model? What are the major levers that drive it?
Premium on top of CDN cost, likely indexed to the industry average $/GB delivered; tiered;
caps.
Competition? DLVR is one company that has come up as an overlay offering. Different
technology, but similar sounding benefits. Others? How do we compare? Are any of the
competitors good acquisition targets? We’ve kicked around the idea of DLVR but not in a great
deal of detail.
Conviva, Cedexis (Citrix), MediaMelon,
XCD sits on top of CDNS
Defensibility
The combination of interferex and RLNC, plus ongoing innovation, moves further out on the
spectrum of defensibility
1. DLB + INF + INNOVATION
2. DLB + INF + INNOVATION + RLNCne
3. DLB + INF + INNOVATION + RLNCe
We leave open in the future the potential for further engagements with CodeOne to continue
to augment our capabilities.
IP Position
3 patents re: Interferex, non issues - applications
2 additional new provisionals – one on flow control. RLNC will benefit from both of these filings.
Working with RLNC, we will develop new IP that is solely applicable to further solutions that are
RLNC specific.
Overall defensible solution which include several things for which we have blocking coverage.
The reason codeon makes this defensible is that without it we risk an alternate developer
implementing that IP and putting it to work against us.
CodeOn is time urgent. They are acquiring tech. they are cash poor. They need a license to fund
growth. If we wait too long, they will take action elsewhere.
