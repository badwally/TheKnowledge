---
id: yt-ZpdxjlxbEwY
type: youtube
title: How to decide – Build or buy AI infrastructure
url: https://www.youtube.com/watch?v=ZpdxjlxbEwY
authors:
- Nutrient
ingested_at: '2026-05-23T18:54:51Z'
content_hash: sha256:871818b8c9976cd99b9a7a9dc24b50823e70de0a87ce48d3f3b96af8c43bd312
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Nutrient
  channel_url: https://www.youtube.com/@nutrientdocs
  duration_seconds: 373
  caption_track: fetched
  snippet_count: 116
---
[9] Every team building AI on documents
eventually hits the same wall.
[14] Not because the AI failed,
not because the pipeline broke.
[18] Because the documents, the one
your customers actually live and work
[22] in every day, demand, more than any open
source library was built to give.
[26] Most teams try to build it.
[28] But two of the fastest growing
AI companies found a faster answer.
[32] Harvey is an AI legal intelligence
platform with over a thousand
[36] customers, tens of thousands of users
across 60 countries.
[40] In law, documents aren't just files.
[43] Every page has a price tag.
[45] Athena Intelligence builds
autonomous AI agents for fortune
[49] 500 companies in finance, legal
and professional services.
[53] A small team serving some of the most
regulated organizations in the world.
[57] Both companies grew fast.
[59] Both depended on documents
at the core of their product,
[62] and both faced the same decision.
[64] In the early days.
[65] Both teams did what most developers do.
[67] Reached for open source.
[69] It worked until it didn't it?
[71] Enterprise
customers started asking for redactions.
[73] Comparison views
and on premise deployment.
[76] The team had to stop
and ask a hard question.
[79] Do we build this ourselves
Or find someone who already solved it?
[83] The team at Athena describes
the exact moment.
[86] We had customers from finance
who wanted to do redaction specifically,
[90] and then we were like,
oh, so do we build it on our own
[92] or do we just find a vendor
that supports it and then use?
[96] So as the customer requests
grew for enterprise use cases,
[100] we wanted like vendors
who either have these built in already
[104] or vendors who know the enterprise as and
[108] have their software optimized
or built with that idea in mind.
[111] on Harvey's side.
[112] The decision came with some history
behind it.
[115] The head of project engineering had used
nutrient before at a different company,
[119] and had been with us long enough
to remember our old name, SPD's kit.
[123] So when Harvey hit the same wall,
he knew exactly what to do.
[126] But now is the time
we are running into issues.
[128] We are hitting the walls
doesn't do what we want to do.
[131] Let's bring out the hammer.
We bring out the hammer, PSPDFKit.
[134] and oh my god experience blown away
[138] The build versus buy decision always looks
cheaper on paper than it is in practice.
[142] Building a competitive document
layer means 6 to 12 months of development.
[147] Engineers learning a 1500 page PDF
standard
[150] and maintenance that never goes away.
[152] For a 13 person team. That math is brutal.
[155] but I feel like
if you're building this from scratch,
[157] you would have to assign at least 2 or 3
engineers only for document capabilities,
[162] and that for six months or one year
that having like, super hard But, it's
[166] going to be a significant amount
of maintenance and development,
[170] which would not have been sustainable
for a small startup.
[173] at ours stage There's another cost
that's easy to underestimate.
[177] Compliance.
[178] Every vendor in your stack has to pass
the security
[181] review of every enterprise customer
you want to close.
[184] Harvey was selling
to the largest law firms in the world.
[187] One more good part here is compliance.
[189] It's all in our infrastructure.
[190] I mean we never get a question about it
like, you know, it's just so good
[194] from a compliance perspective Biggest law
firms in the world and from a compliance
[197] standpoint they look at this stuff
and it just checks out.
[200] Right.
And it was just so easy for decisions.
[203] For Athena, the bar was just as high.
[205] Their customers
data couldn't leave their cloud at all.
[208] Almost all these enterprises we talk with
basically under regulated industries
[213] and so their primary concern is, oh,
[215] we don't want our data
to be leaving our, cloud.
[218] So what we do is we deploy our complete
stack within their servers
[222] with their own instances.
[224] And so we couldn't, like,
randomly dependent on a npm library
[227] or there we wanted
[228] someone who understands us properly
and are willing to go on prem, with us.
[233] So all this, soc2 HIPAA,
it's like all those are super core,
[238] to us for, for these kind of deployments
that we do with our customers.
[242] for both companies.
[243] The most critical one was citations.
[246] When an AI references a source.
[248] Users need to see exactly where it came
from.
[250] The right page.
[251] The right sentence
highlighted in real time.
[254] This is easier said than built.
[256] You guys did some groundbreaking work
Specifically highlighting what we deliver
[261] is dynamically changing your highlights
based on the citation you click.
[266] And we change the opacity.
[268] go to the right page And you click it
and it's near real time performance.
[273] There's no lag anything.
[275] I have talked to other folks like, hey,
this is under the radar company.
[280] Everybody uses it.
[281] They have quite an interesting tech
that I haven't seen anywhere else.
[284] Athena built the same experience
into their agent platform.
[288] For example, one of the core
parts of our app is, citations.
[292] So anytime the agent uses
a set of documents or answers,
[297] it gives a rich citation source
and on click it takes us
[300] to the particular document scrolls
to the page number that shows highlighting
[303] of the exact sentence,
that it used to reference, which is huge.
[307] Nutrient crushed those like the citation
stuff is heavily dependent on how
[311] Nutrient sets the scroll-to functions
or the highlight things.
[315] So that just was phenomenal for us.
[317] Harvey's document volume grew
50% month over month.
[320] The infrastructure stayed flat.
[322] It was the one piece of the stack
that they never had to think about.
[326] the volume, we are
[326] put into the system 50% month over month
and you don't think about it at all
[331] like PSPDFKit (Nutrient) we dont
think about it, it just works
[334] that's the best operational systems,
[336] you can have
when you kind of forget about them.
[339] the best work is the one that is silent.
At Athena, the feeling was similar.
[344] we wanted a document SDK system
[346] that we could trust
and we know we could build on top of.
[350] we stayed
because it kind of grew with this,
[352] you know, from PDF viewing to citations
to any other workflows,
[355] it kind of became like a core foundational
infrastructure of our stack.
[359] If you're building AI workflows
that need to handle documents
[363] at scale inside regulated enterprises
with compliance built in from day one.
[368] Nutrient is the document
infrastructure layer.
[370] Your team doesn't have to build,
maintain, or think about.
