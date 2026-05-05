---
id: pdf-0a9b334e1c2d
type: pdf
title: FallbackPDF__0a9b334e
url: ''
authors:
- Walter Andrew Grant
ingested_at: '2026-04-29T16:13:25Z'
content_hash: sha256:4c86638cee1dabd4082ba781b473aeffd52b3d141533651dc8b008d9d39f29d4
source_path: raw/pdf/pdf-0a9b334e1c2d.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 4
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__0a9b334e.pdf
published_at: '2025'
---
DMC – Disney Streaming Services
8 November 2021
Joe Inzerillo, EVP and CTO of Disney Streaming
Dolby Attendees
Giles Baker
Jeff Riedmiller
Cherylene McKinney
Guo Huang
Andrew Grant
We met today with Joe Inzerillo, EVP and CTO of Disney Streaming. The main objective was to
introduce DMC (specifically xCD-1) and get Joe’s feedback on (1) our product approach, (2)
potential integration points within Disney’s infrastructure, and (3) understand his perspective
on the utility of xCD-1 in their dynamic delivery and playback infrastructure with the intention
of a limited trial. The secondary objectives included placing DMC in the context of Dolby’s
expanded cloud priorities, revealing the new org structure, and creating an executive-level
connection between Joe and Giles. While we did not have time to generate detail on product
integration, Joe did provide detailed feedback on his interpretation of our multi-source, multi-
path approach to optimizing QoS and QoE. In short, we need to get very clear on CDN caching
behavior as it related to object size: small objects are problematic at scale.
Overall, his feedback was candid and highly valuable: he saw our approach to delivery
enhancement as potentially beneficial to smaller-scale services, characterized our logic about
the connection between quality improvements and subscriber retention as ‘sound’, and
detailed at length the technical challenges that sit at the intersection of audience scale, object
size, and cache logic. He also said that we may have something to productize if we can combine
xCD, an intelligent encoding system, and a cache logic by which block size changes based on
understanding of cache behavior.
It was clear by the end of the meeting that, while accepting the logic of our system and the
results at small scale, Joe perceives a series of system behaviors related to object size, audience
scale, and cache behavior that we would need to sort out before engaging Disney. We will need
to better educate him on xCD (possibly with a white paper or deeper dive with his network
engineering leads like Nick Brookins) and come to the table with solutions to his perceived
problems and a specific test hypothesis if we want to test our system at Disney scale.
Overall, Joe was open to provide brief feedback as we investigate and address these issues,
leaving the door open for future engagement with Disney.
Full transcript is here:
More detailed notes:

1. Disney has experimented with ‘similar’ approaches from companies like Swarmcast in
the past and identified significant scaling challenges related to cache behavior within
and across content delivery networks. Size matters for objects or segments, as small
objects create complications. (Some of his response reflects a partial misunderstanding
of xCD-1, but the detail is valuable nevertheless).
a. Small objects – like his perception of the functionally-equivalent blocks created
as part of the xCD process – may start up quickly, but fulfilling from cache carries
a transactional overhead that compounds as traffic increases, with an increasing
volume of TCP ‘discussions’ that impart a high resource cost to a given cache
node.
b. Cache ROT
i. (is this related to the Resident Object Table, essentially the lookup table
that a system uses to locate and access an object in cache memory or
used to refer to a segment in cache that is only partially consumed and
then sits there, rotting?) If the former, does that mean small objects
creates a significant load on cache node as small object transactions
increase.
ii. He noted that this is why people like DASH, as it looks like a big singular
object in mid-tier cache but breaks up into smaller segments as that asset
is pulled across to the edge.
c. Disney uses an approach he called “segment fluidity” to deal with this problem
of over-serving, using an example of session abandonment to illustrate.
i. A user bailing after 3 minutes changes the ballistics (IS THIS THE HIT
RATE?) on a given CDN. If you have large segments, you end up wasting
resources if (for example) a user watches a show for 2 minutes but the
object size (consisting of segments?) means the CDN resources are on
hold for 3 minutes. (with the remainder ‘rotting’)
ii. They start with very small segments, and then build into larger segments
during the course of a session. One assumes that they are able to deal
with this probabilistically, with the odds of a larger segment being fully
‘consumed’ improving as a user progresses deeper into a given movie or
episode.
iii. The benefit of larger objects is fewer transactions. The challenge of small
objects is that it creates challenges with the hashing algorithm a CDN
uses to runt the load balancer for the cluster of servers at the edge. The
more files you have, the more servers you are likely resident on within a
given cluster.
1. For an asset that is not hot, you are playing (in his words) “Russian
Roulette” as any given server in the cluster may have a problem
or purge their cache independently.
2. The challenge he perceived in our system is that we are dealing
with small objects (not necessarily true), so when a server starts
to purge objects it ends up that the cluster is ‘like swiss cheese;/

iv. Given the fact that every CDN has different hashing algorithms, different
wear patterns, etc they are going to have different approaches to cluster
management.
1. We won’t know what is happening with our functionally
equivalent blocks at any given time.
2. He noted ‘self-reinforcing behavior’ at scale, which was not clear
to me.
d. Overall, Jeff and Ove should give us a perspective on the extent to which Joe was
misinterpreting our approach and the impact of how the distribution of our
blocks across a given set of CDNs (or cache clusters within a given CDN) would
cause problems.
2. They implemented a prior solution on their own that focused on coding but was not
successful. This
a. Sony Network DVR and the need to store unique versions of every individually
‘DVR’d’ show to abide by the terms of the Cablevision ruling.
i. Used URL parameters to delineate the unique chunks.
ii. Observed a different network effect on the CDNs when running this
approach with small ‘objects’ or files.
b. “Punching holes in the cache” for big audiences in a single region means that a
cache miss on a small object results in a potentially long r/t back to origin, which
introduces latency.
3. They have a new method (with IP filed) that involves visual quality assessment of
individual chunks (via, e.g. something like PSNR) in order to reduce the number of
chunks for a given asset. This links encoding with delivery.
a. They eliminate the bitrates that result in a similar score, allowing them to reduce
chunks in the network by up to 30%
i. For example, if in a given scene the 3mbps gives the same score as
5mbps, eliminate the 5mbps chunk and go with the 3.
ii. 30% reduction of objects drove a 25% increase in overall system
performance [in a given region ?]
4. CDNs are using public pipes to move objects through the multiple tiers of a caching
infrastructure, so there is a constant competiton for resources. This creates a risk of
multiple blocks moving down the same TCP connection and effectively clotting as small
objects get stuck behind large objects. These problems will become far more likely at
scale, with Joe anticipating that we will see issues ~1M simultaneous.
a. When a client receives a manifest and requests a block, there is a queue matrix
across all the TCP connections. The mid-tier may deliver the first segment before
the second, and small segments may stack up behind the large ones.
i. This is “segment jitter’
b. This appears to support the xCD value thesis as we would naturally route around
these TCP congestions or big-small queue competition.
i. Worth following up, esp. in the context of intra-CDN utility for xCD
c. Given the multi-tenant nature of a cDN (and of transit) there is basically an equal
probability of a large and small file being requested. Since it takes longer to

deliver a larger file (or object), that means it is also highly probable that a large
number of smaller objects will get backed up, even if a normal distribution of
large and small across the network.
i. Probably need to back-check this.
5. We are likely to see challenges at scale (and we haven’t figured out how to test our
system at scale yet) and given the different ABR logic on each device platform. To solve
this, we need to scale up our testing capability.
a. Switching a lot between CDNs is a bad thing at scale.
b. Roku: “Swimming and Nibbling” destroys edge caching. As opposed to Apple,
which oscillates segment size based on prior segment behavior, Roku has a
tendency to terminate connections just before the completion of a segment. This
creates negative caching effects.
i. We need to consider this in the context of xCD blocks?
ii. Roku also tends to compromise aggregate client behavior on their
platform in pursuit of improvements on any one client. (E.g. firmware
updates).
c. They run multivariate tests with different ABR algorithms using components on
the client and the server.
i. Explore relationships: segment size vs adaptation, startup time and
stream resiliency, etc.
6. Other notes
a. CMAF is missing from our Toy example and he called that out.
b. Live quality improves over a session as the cache resource is used more
effectively.
