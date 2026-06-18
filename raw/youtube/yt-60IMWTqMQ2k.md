---
schema_version: 1
id: yt-60IMWTqMQ2k
type: youtube
title: Delivering reliable AI with the dbt Semantic Layer and dbt MCP Server
url: https://www.youtube.com/watch?v=60IMWTqMQ2k
authors:
- dbt Labs
ingested_at: '2026-06-17T20:57:02Z'
content_hash: sha256:5ee85498536e9a9714622f5d38e45ed0e36c23049853cf7b08a2deddfb09a245
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: dbt Labs
  channel_url: https://www.youtube.com/@dbt-labs
  duration_seconds: 2561
  caption_track: fetched
  snippet_count: 999
filter:
  score: 0.7
---
[2] Hey everyone and welcome in. Um my name
[5] is Stephen Rob. I'm a partner solution
[7] architect here at DBT calling in from
[10] San Francisco. And today we're going to
[12] talk a little bit about delivering AI uh
[15] and how DBT kind of makes that a little
[18] bit more accessible and possible. Uh I'm
[20] going to be joined today by two other
[22] speakers. You're going to see Dustin and
[24] Dakota from PH Data. If you've seen a
[27] couple of our past webinars, you
[29] understand how this goes, but I've had
[30] the pleasure of working with them a few
[31] times now.
[34] So, now let's cover some basic
[35] housekeeping. Uh, so we're going to have
[38] a Q&A tab for all of your questions
[40] where a DBT product expert uh will be
[43] able to answer them. For the chat, feel
[45] free to throw in some banter, connect
[48] with people, highlight what you've
[49] learned from the presentation, or just
[51] share where you're from, too. uh
[54] etiquette. Just, you know, be uh be
[57] respectful and be inclusive. Feel free
[59] to ask tough questions, provide some
[61] feedback. We'll send out the recording
[63] after 24 hours after this event, and
[66] then uh we'll also share a survey to let
[68] us know how we're doing.
[71] So for the agenda today, uh we're going
[73] to start by covering the AI context gap.
[77] Kind of some of the challenges that we
[78] see DBT being able to assist with as we
[81] kind of move into this AI uh workflow
[85] work AI world really. We're then going
[88] to have a customer journey and a demo uh
[90] from uh PH data. Then I'll share a
[93] little bit about what's coming next in
[95] 2026 with DBT agents and some next steps
[98] for some additional webinars kind of on
[100] the on their way.
[102] So first let's get started with this
[104] data engineering in the AI uh era. So AI
[109] is changing how we use data at a pace
[111] we've never seen before. Like we all
[114] know like there's a new tool every day.
[115] You got to redo your entire workflow.
[118] We've never had to learn as much as fast
[120] as as as this. I feel like data
[122] engineering teams once kind of focused
[125] solely on the pipelines and the
[127] transformations are now really on the
[129] front lines of AI strategy. They're
[132] expected to deliver uh intelligent
[135] reliable data products and do it faster
[138] than ever before. And somehow at the
[140] same time they need to make sure those
[142] systems are trustworthy, scalable and
[144] secure.
[145] So just as dbt revolutionized data
[149] transformation in the cloud era um by
[151] adding all these better processes around
[155] the ETL you know like modular version
[158] controlled testable workflows
[161] um now we're trying to do the same thing
[162] in the AI space so we're becoming this
[165] standard for delivering AI ready data
[168] infrastructure in this kind of new era
[172] and so while our customers are moving
[174] incredibly fast building everything from
[176] agentic workflows and internal co-pilots
[179] for kind of like customerf facing chat
[181] bots the underlying kind of AI stack is
[186] changing even faster so each week
[188] there's a new breakthrough there's a new
[191] model smarter framework or even a new
[194] vector store and so like that velocity
[198] really means that AI and data teams are
[201] constantly adapting from going from
[203] cloud to cursor
[205] pine cone semantic layers and re uh
[208] retraining systems just to kind of keep
[210] up. So each of these shifts is
[214] introducing friction, new integrations,
[217] rewrites, tuning, duplication. Uh
[220] there's a lot of time risk and uh really
[224] just slowing of innovation caused by
[226] these like wide variety of tools.
[230] But uh at the end of the day, a lot of
[232] the kind of fundamental questions are
[234] the same. So like what does this metric
[237] mean? Is this definition still up to
[240] date? Where did this number come from?
[242] Or even like can we trust this data
[245] really? Uh for enterprise AI, the
[248] bottleneck isn't compute power or data
[250] volume. Um we would argue that it's
[253] context
[254] and basically like structured governed
[257] context. So large language models can't
[260] just reason over raw or fragmented data.
[263] They need that strong foundation. So
[266] like without those structured
[267] definitions and shared business logic,
[270] these AI systems uh kind of have to do
[272] like what an intern would do and they
[274] get kind of stuck guessing and when they
[276] guess they start hallucinating and
[279] that's where you see all the data
[280] problems of asking a question and
[281] getting the wrong answer.
[284] So for example, take like an internal
[286] chatbot. You might have a user that
[288] says, "What's our revenue for enterprise
[291] customers in Q2?"
[294] And to be able to answer that question,
[296] the model has to understand a few
[297] things. What defines an enterprise
[300] customer? Which up-to-date table or
[303] model includes revenue logic? And does
[307] that revenue table have cancellations,
[309] ticket sales, or returns? Or even is
[312] there any other things that needs to
[313] take into consideration for how you
[315] answer that question? So without that
[318] structured governed context, the large
[320] language model might generate SQL that
[323] runs, but it might also return the
[325] complete wrong answer with complete
[327] confidence. So you would think that the
[330] machine is correct without you actually
[332] being able to validate it. Or consider
[335] an agentic workflow generating an entire
[338] weekly order summary without a version
[341] control definition of order. It could be
[343] pulling that definition from the wrong
[345] table. It could be double counting some
[347] of those returns or just blatantly
[350] missing critical logic. Um, and so
[353] basically again giving you incorrect
[355] results with with the question as simple
[357] as what was my revenue last quarter.
[361] And so what we found is that what's
[365] needed isn't necessarily more tools.
[368] It's kind of like a unifying control
[370] plane for your system, your AI systems.
[373] So really it's going to be one place
[375] where your business logic, your
[377] transformations, your tests, and really
[380] your documentation live. Structure it
[383] once and then apply it everywhere. And
[386] that's where we kind of see DBT fitting
[388] in. With DBT as the control plane for
[391] your AI, you structure your data once
[393] and you're able to then use AI
[395] everywhere.
[396] So as we just kind of said, these AI
[399] systems need access to structured
[401] context. And really at the end of the
[403] day, that's primarily what DBT is, is
[406] the ability for you to be able to create
[408] data about your data that can then be
[411] used for querying, for AI, for all these
[414] other use cases. Um, and those AI
[418] systems are going to be able to pull
[420] that context so that basically we can
[422] get to a a more centralized governed
[426] platform and workflow.
[428] Um the idea there is that we can remove
[430] a lot of that context that exists in
[433] fragments or tribal knowledge and now
[436] lock it down in code so it's reliable
[437] across your entire organization. And so
[440] while DBT is already the standard for
[443] creating highquality governed data sets
[446] from your warehouse, it captures rich
[449] metadata, model lineage, test coverage,
[452] centralized metric definitions, all
[454] those kinds of important things that we
[456] talk about.
[457] It's also bringing something else. Um,
[460] it's bringing performance and cost
[461] efficiency.
[463] So rather than connecting each AI
[465] workflow to its kind of own source, let
[468] DUT centralize those transformations,
[471] those metrics, those documentation all
[473] in one layer which should reduce you
[476] know a bunch of your queries. It should
[478] you should have less compute spend
[481] because now we have a unified model
[482] where you can uh apply some like state
[485] of orchestration and some other features
[487] and you should also have a faster
[489] response time for your end users. It
[491] should become much easier for you to
[493] develop additional kind of workflows
[495] because you now have a unified platform
[497] to ask questions on that and with
[499] something like dbt you do get that
[502] crossplatform flexibility. So like as
[504] you know DBT works across Snowflake,
[507] Data Bricks, BigQuery. So you're going
[510] to be able to build fast across your
[511] entire stack without sacrificing any
[514] consistency.
[515] Um, another really important thing to
[518] note there is security and governance.
[521] It's one of the big things holding back
[523] I'd say a lot of AI projects and DBT is
[527] going to help close that gap in that
[528] with every model test and transformation
[531] we can validate that that's going to be
[533] logged. It's going to be versioned and
[535] it's going to be auditable. Um which
[537] really means we can meet a lot of those
[538] enterprisegrade requirements for
[540] compliance and data protection with AI.
[544] And then lastly, uh, as as far as kind
[547] of AI powered workflows goes, you're
[549] going to be able to leverage this
[550] context to build better agents and
[554] better overall AI experiences faster
[556] than ever.
[559] And uh, another thing to kind of bring
[561] up here is our MCP server. So while
[566] everything we've said so far has been
[568] more about providing the context that's
[570] required, how does DBT make it really
[573] easy for your tools um to now actually
[576] integrate exactly with DBT? And that's
[580] where the MCP fits in is tools like lane
[583] chain and semantic kernel can directly
[586] query DBT semantic layer lineage and
[588] tested models via API so that your AI
[591] systems don't just access the data they
[593] also understand it. And so while the AI
[596] tools may change, you know, GBT4 to
[600] claude, chatbots to agents, your
[603] foundation shouldn't change or doesn't
[606] at least doesn't have to if you're using
[607] DBT.
[609] And so this is a nice little diagram
[612] here of MCP and and kind of what it is.
[615] Feel free to check out our GitHub
[617] repository for it. And what it's going
[621] to do, like I said, is really just unify
[623] all of the different DBT assets and AI
[627] applications.
[629] And we make that accessible for you in
[631] two different ways. Both a local
[633] connection and a remote connection. Uh
[635] with the local uh it's it's pretty
[638] self-explanatory. It runs on your laptop
[640] alongside your DBT project. It's a
[642] fantastic option for local development
[644] with something like Cursor or Cloud. And
[647] it means that your agent is going to
[649] make uh be more empowered than ever to
[652] basically create your DBT code uh right
[654] on your machine. And then the second
[657] option is to run it remotely. So we have
[660] an incredibly straightforward setup
[662] where you can now plug and play uh your
[664] your uh DBT MCP server directly with any
[668] of your different AI tools and access
[670] them by any sort of like web
[672] application. So, it just means that you
[674] can connect multi- aents, multi-user
[676] systems easier than ever before. And
[679] you're going to see a wide variety of
[681] MCP kind of integrations with a lot of
[683] our partners coming into the future. And
[686] then lastly here, before I turn it over
[688] to PH Data, uh a lot of what we've had
[691] so far has been kind of theoretical
[692] conversation, but I also wanted to
[695] support that with a real case study. So
[697] by introducing DBT MCP, M1 Finance was
[701] able to reduce their engineering
[702] bottlenecks and dramatically improve
[705] their efficiency. So their teams didn't
[707] really have to wait on specialized
[709] resources to move their projects
[710] forward. It gave them a really clear
[713] path to be able to reduce some of the
[716] biggest blockers of why they had failed
[718] to adopt AI. Um basically
[722] hallucinations. So with structured
[724] validated access to those systems, the
[726] AI could act on some real authoritative
[728] data. And with that additional context,
[730] they were able to finally be confident
[733] that the answers and outputs they were
[735] getting were accur accurate, reliable,
[737] and safe. Um really letting them kind of
[739] unlock that that true scale and not just
[742] like a P or an experiment. And so with
[745] that, I'm now going to hand things over
[747] to PH Data who's going to walk us
[749] through how this works in practice with
[751] kind of the sample company workflow.
[755] >> All right, thanks Stephen. Appreciate
[757] the um information to carry over and
[760] appreciate everyone here for joining us.
[761] Happy to be with you all. Um my name is
[764] Dustin Dorsy. I'm with the PH Data team.
[766] I'm a director of data engineering here
[768] and one of our practice leads and I'm
[770] here with my colleague Dakota. kind of
[772] if you want to introduce yourself and PH
[774] Data.
[775] >> Yeah, it's nice to meet everyone. I'm
[776] Dakota Kelly, one of the principal
[778] solution architects here at PH Data.
[780] Excited to be chatting with all of you
[782] about this topic. Just as a real quick
[784] introduction on who PH Data is in case
[786] you don't know us, we are one of the top
[790] consulting firms out there to help
[792] implement, work through, and partner
[794] with your technology. We focus purely on
[798] data. Whether that's helping you set up
[800] a data strategy, data engineering, data
[803] analytics, creating fusion teams,
[806] machine learning agents, all the
[809] different hot topics inside of data. We
[811] cover all across the spectrum and
[813] partner with the top technologies out
[814] there including being the three-time
[818] backto-back DBT partner of the year on
[820] top of partner of the year with
[822] Snowflake many times and four-time
[824] partner of the year with Fiverr,
[826] etc. And so with that, I'll hand it over
[829] to Dustin to start to talk about this
[831] customer story that we're going to go
[832] over and give you a demo of.
[836] >> Sounds good. All right, let's dive into
[838] it. So what we're going to do here is
[839] kind of carrying over Stephen gave some
[842] of the fundamentals related to what
[844] we're going to talk about. What we're
[845] going to do is we're going to give you a
[846] customer example of a fictional story
[848] that we created just for this
[851] presentation.
[852] Um and then we're going to show you a
[854] demo of this actually being in action.
[856] But we're going to start over the next
[858] little bit just walking through who this
[860] customer is and um and um then we'll
[865] dive into the demo here. So here we have
[868] a company G Galaxy's Edge Travel
[871] Company. They're the largest tourism
[873] operator in the Outer Rim. They offer a
[876] wide range of services including Star
[878] Cruiser vacation packages, droid
[880] assisted lodging experiences,
[883] light speeded enabled transformation,
[885] and hollow table concier services. Um,
[888] imagine this company existing in your
[891] favorite space themed world of Star
[894] Wars, Star Trek or Starfield for the
[897] gamers out there of existing in this
[900] environment. And what they want to do,
[903] they have a goal or they've reached out
[905] to a company like PH Data to say, "Hey,
[907] we want to build an AI concierge or a
[910] hollow guide, if you will. Think of this
[912] as a way cooler version of an Alexa or
[915] Siri um or Google. Um and this hollow
[919] guide can answer any questions
[921] instantly. So things like pricing,
[924] availability, loyalty points, packaging
[926] rules, bundling, recommendations,
[929] whatever you want to ask it, you just
[930] ask it what you want to know and then it
[933] spits out the answers immediately to you
[936] and always be consistent. The challenge
[938] is they have the data for all of these
[940] systems, but it's scattered across
[943] multiple systems. So, think of think of
[946] things like they have Star Cruiser
[948] manifest, which is JSON events that's
[951] captured from their hyperspace travel
[953] system. They have droid service logs,
[956] which are semistructured information
[958] that they're loading up and getting into
[960] a structured format. resort booking
[962] information which is stored in
[964] structured tables and then loyalty
[966] points balances which come through
[968] micros service API dumps. While likely
[973] no one on this call works for an
[974] intergalactic travel tourism operator,
[978] some of these systems that exist here
[980] probably resonate with systems in your
[982] environment. So hopefully as we go
[984] through this scenario here, you're
[985] thinking, "Oh yeah, we have a system
[987] that does that that we need to pull in
[989] here.
[992] All right. So, let's talk about the
[994] context gap. Stephen gave some
[996] information on this earlier and now we
[998] want to make it a little more practical
[1000] um and understand here. So, the hollow
[1004] guide that we're building doesn't
[1006] understand the business. So, it's a
[1009] brand new it's an AI system. It can show
[1011] up, but it doesn't know anything about
[1013] our system.
[1014] This isn't because the AI is bad, but
[1017] this is just because our enterprise
[1019] context is a mess. If we just go and we
[1021] take all of this data in disparit
[1023] systems and put an AI on top of it, it's
[1026] not going to produce very good results.
[1029] For instance, calculations like
[1031] something like total cry uh trip cost is
[1034] calculated differently across multiple
[1036] systems and so it can produce varying
[1039] degrees of results.
[1041] room names. Like if you're booking a
[1043] room on one of our Star Cruiser
[1044] packages, you may have some that are
[1047] deluxe- pod d-pod or pod deluxe. And
[1052] these could all indicate the exact same
[1054] room, but AI doesn't know that unless we
[1057] provide context to let it know that
[1059] that's true. Um, also loyalty tiers
[1062] aren't joined correctly. This this
[1064] causes the AI to hallucinate discounts
[1066] and so we're not getting consistent
[1068] pricing. And then lastly, packaging
[1071] availability depends on arcane business
[1073] logic. And so all of these things have
[1076] to be taken into account to make sure
[1078] that our hollow guide produces the right
[1081] results and it's consistent um with it.
[1085] So the organization realizes as we're
[1087] going through talking through this that
[1089] AI is only as good as the structured
[1091] context that we feed it. So what they
[1094] need is a data control plane in a
[1096] structured context layer built on
[1098] something like DBT to provide that
[1102] information to them.
[1105] Agreed. And that context is so important
[1108] because that, like stated before, really
[1112] allows the AI and the agents to truly be
[1114] able to answer these questions and allow
[1117] us to scale the data products we're
[1119] building out to larger teams, allowing
[1122] people if they have a one-off question
[1124] to just ask it and get that answer
[1126] instead of needing to request a new bash
[1129] dashboard to answer a very small
[1131] question.
[1133] >> Yeah, absolutely. And think about it
[1135] like we don't want our customers who are
[1138] who are coming here speaking to our
[1139] hollow guide asking for something like a
[1142] ch child friendly activity and then
[1144] getting sent to a Sith temple for those
[1146] of you who are Star Wars fan because
[1148] it's probably we're not going to be very
[1149] child-friendly. So those are things we
[1152] we're trying to solve for. All right. So
[1155] why DBT? Where does DBT fit in here? Why
[1158] now? Well, Galaxy's Edge Travel needs to
[1162] pair to power their AI concierge with a
[1166] few different things. First is the data
[1169] modeling. And if you have followed these
[1171] these sort of sessions that me, Stephen,
[1173] and Dakota have done over the past
[1175] several months, the last session that we
[1178] did was specifically on modeling, which
[1180] is really a prerequisite to be able to
[1182] get to to having this hollow guide that
[1184] we need to build. So the modeling is
[1187] creating consistent facts and dimensions
[1190] for our trips, packages, customers,
[1192] android services. We need to curate this
[1195] data. We need to put it in a um easy to
[1197] understand manner by breaking our data
[1199] up in within facts and dimensions.
[1202] The second thing is we need to create a
[1205] semantic layer. We need to define
[1207] metrics like total trip cost you know
[1210] just to give an example like a total
[1212] trip cost occupancy rate and loyalty
[1215] eligible balance that are always
[1216] correct. So we need to put that on top
[1219] of it. The semantic layer will also um
[1222] is a place where we can define the joins
[1224] for our model to help it understand how
[1225] the joins are made. we can add business
[1227] friendly naming and then obviously we
[1229] can store um calculations and metrics um
[1234] within the the semantic layer and then
[1236] lastly with the MCP server this is how
[1240] we expose govern DBT context directly to
[1243] the AI agent and in this case it's our
[1246] hollow guide so that when someone asks
[1248] the question how many loy loyalty points
[1251] will I earn if I add the holocron
[1253] discovery tour to my three night star
[1256] cruiser today we produce again produce
[1259] accurate results.
[1261] So AI must be reliable um to be able to
[1265] answer these questions. So in order to
[1267] be reliable what it needs to do is it
[1269] needs to first of all it needs to know
[1271] the definition of what a hollowocron
[1273] discovery tour is. It needs to pull
[1276] semantic metrics on cost loyalty acral
[1279] and discount rules. It needs to join it
[1282] to our customer profile or customer
[1284] dimension and then it needs to apply
[1286] real business logic to it and so it
[1288] needs the context to be able to do that.
[1292] If you look at these things they're
[1293] almost like layers of maturity within
[1296] your data products once you've built the
[1298] model. It's not enough to just provide
[1300] the fact and dims and call it a day. The
[1302] semantic layer like was stated allows us
[1305] to explain how these things are joined
[1307] and what these things mean. on top of we
[1309] can add other more valuable metadata.
[1312] It's not just here's a metric and here's
[1314] what it means, but we can also go so far
[1316] as to say hey here's multiple synonyms
[1318] for this type of metric and here's what
[1321] people across the business or across the
[1324] galaxy might call this but mean the same
[1326] thing. You build up that context and it
[1329] allows the AI to avoid those
[1331] hallucinations.
[1334] All right. So,
[1336] let's talk about what we're going to
[1338] demo. So, now that we've established our
[1341] customer and what our customer is trying
[1343] to solve for and what they want to try
[1344] to do, now we want to actually show it
[1346] to you in action. Like, how did these
[1348] components actually come together? So,
[1351] we're going to build an intelligent
[1353] contextaware AI travel concierge and
[1356] we're going to do it through three
[1357] steps. First, we're going to focus on
[1360] the data modeling aspect. We're going to
[1361] build a small mart with a couple a few
[1364] fact tables and a few dimensions just to
[1367] give something to work with. And then
[1369] we're going to put a curated model for
[1371] the demo on top of it that standardizes
[1373] all of our package rules based cost
[1375] dynamic fees. So we're just going to
[1377] create a base level model and Dakota is
[1379] going to show this here in just a
[1380] minute. Then we're going to put a
[1382] semantic layer on top of it in which
[1383] we're going to define some of the
[1384] business me metrics that the AI will
[1386] consume. specifically things like total
[1388] trip cost, package revenue, etc. Um, so
[1392] we'll show those. And then lastly, we're
[1394] going to show you the MCP integration.
[1396] So, Hollow Guide AI will use the DBTs
[1399] MCP server to browse the semantic model,
[1402] ask for a metric, query for the curated
[1405] models, and then generate human ready
[1407] answers. And so then we're going to show
[1410] you the power of it by asking some
[1413] questions and getting results from it of
[1415] what our really cool hollow guide would
[1418] actually produce here. And so with that,
[1421] I'm going to kick it over to Dakota
[1422] who's going to jump into the demo and
[1424] show you guys this stuff in action.
[1428] >> All right. Thank you, Dustin, as we get
[1432] ready to kick off this demo. Again, as a
[1435] big part of this demo, we're going to
[1437] dive into using UCP. And we're not just
[1440] going to use it with Visual Studios
[1441] Code. We're actually going to have a
[1443] very simple textbased chatbot going as
[1446] well.
[1448] But the core of this entire presentation
[1452] is how MCP
[1456] can improve the context of our LMS,
[1459] these other things. But for it to do
[1461] that
[1463] we need to first understand what is our
[1465] source data model. What transformations
[1467] have we built? What's our final data
[1469] model? What documentation exists? How do
[1473] we document and ensure that that context
[1475] exists in a way that can help facilitate
[1480] the AI agent and the AI tools and LLM
[1484] making the correct decisions.
[1486] And to do that, just like we talked
[1488] about, the very important first step is
[1491] understanding source data
[1494] as well as what our final data model is.
[1498] You can see here we have a rough erd put
[1500] together of what our source data looks
[1503] like. We have a set of customers.
[1506] Those customers have loyalty accounts
[1510] which can be a part of a loyalty tier.
[1512] That customer also can have
[1514] reservations. Those reservations
[1516] have rooms. They can come from a
[1518] reservation package. They can have items
[1521] attached to them as well as we have
[1523] service logs of the droids that have
[1525] gone in and then clean up on these
[1527] different rooms. And as we start
[1530] thinking about the type of questions we
[1531] might want to ask as business users as
[1534] well as what our customers might want to
[1535] ask, we start to think, okay, probably
[1539] one of the most important things is
[1541] information about reservations. What
[1543] reservations are available because the
[1545] room is not booked?
[1548] How
[1549] clean is the room? Are we having
[1551] problems with our droids not being able
[1553] to properly service the rooms and take
[1554] care of them? How do we make sure that
[1557] those in the loyalty tiers are filling
[1560] sufficient enough
[1563] discounts and other things to want to
[1565] remain as a part of the loyalty account
[1567] in the loy uh in their loyalty tiers.
[1570] Those different pieces of information
[1573] are extremely important.
[1576] Because of that, we need to build out a
[1577] data model that facilitates that type of
[1580] analysis.
[1582] And you can see in here we have created
[1584] a data model with a set of dims around
[1586] rooms and customers,
[1589] facts around our trips,
[1591] around our trip pricing, as well as the
[1594] packages that they're part of.
[1597] When we create out this set of dant
[1599] facts, it becomes very easy for us to
[1601] one put the semantic layer on top and
[1604] use the semantic layer to define these
[1606] different relationships, the joins that
[1609] need to exist, what data exists, why it
[1613] exists, what its purpose is, what the
[1615] context of that is. That provides us an
[1618] easy interface to query and get results
[1621] and start to ask questions of our data
[1625] and start to provide a natural language
[1627] interface
[1629] for getting results and understanding
[1631] what's in our data while at the same
[1633] time reducing things such as the
[1637] hallucinations.
[1640] By understanding what our begin state
[1643] is, which is the transaction system, and
[1646] what our end state is,
[1649] we can start to visualize and put
[1651] together what is the path to get to that
[1654] end in state.
[1656] That's where we start to build out our
[1657] DVT project. You'll see it's a fairly
[1659] standard project. We've got staging
[1661] layers of all of our source data. Those
[1664] get brought into intermediate layers to
[1667] bring the data together which then
[1670] culminates in the set of facts and dims
[1674] that we've created as well as a set of
[1676] semantic models. These semantic models
[1679] define things like trip as well as our
[1683] trips pricing
[1685] things like the rooms, the customers
[1688] etc.
[1690] With this context in place, we can do a
[1694] number of extremely interesting things
[1697] inside of our DBT project.
[1700] We start to build out those layers of
[1703] transformation, provide the context,
[1706] provide the standards, provide the
[1708] understanding of our models,
[1711] integrate that in with something like
[1713] DBT's MCP server, which is able to
[1716] communicate with your cloud instance,
[1718] understand your DBT artifacts,
[1720] understand the queries, the semantic
[1723] that exists, etc. help us provide an
[1725] interface to improve our development
[1728] workflow as well as how we're querying
[1731] thinking about our data.
[1735] So what is that difference? Well, if you
[1739] have the DBT ZP server set up in your
[1742] local environment, you can do something
[1745] as simple as going on over to your
[1749] chatbot here.
[1752] With this chatbot,
[1755] we can ask it to do a myriad of
[1757] different things to help us understand
[1759] our DBT project. Again, you'll see up
[1762] here, if we look at the top, we have a
[1764] very simple setup for how to activate
[1767] our MCP as well as our environment
[1769] variable with our environment file with
[1772] all the different appropriate variables
[1774] to connect to our instance and
[1776] understand what to do.
[1778] Now we can do things like come in here
[1782] and you'll notice I forgot to create my
[1785] semantic layer for fact packages. I
[1788] could come in here and say
[1790] I would like to create a semantic layer
[1796] for my fact packages model. This
[1802] semantic there should follow the naming
[1808] conventions
[1809] and structure
[1812] of the rest of the semantic layer files
[1818] in semantic models.
[1822] When I do that, this is going to connect
[1824] to the DBT MCP and use that to help it
[1828] understand the different things that are
[1830] part of this repo. Help it understand
[1833] those different patterns and generate
[1837] the actual semantic file that is needed
[1841] for us to be able to do semantic work
[1844] with the packages.
[1846] And what's nice is we've already
[1848] provided a decent amount of context
[1851] for fact packages because well
[1856] if we go look in our YAML we've already
[1858] provided things like descriptions, tests
[1861] and other things like that to provide as
[1864] context. We can see it already coming
[1866] through in
[1869] the different descriptions.
[1872] We can use this to create new semantic
[1875] models. We can use this to help us
[1877] improve our performance. We can automate
[1879] some of the minor boring things or at
[1883] least start to put things in place that
[1885] help us move faster.
[1888] But that's not all the MCP server does.
[1890] Again, it takes all that context and we
[1893] can start asking it
[1896] about our data.
[1899] What sort of things might we want to
[1900] know? Well, let's go see how our droids
[1903] are doing when it comes to interacting
[1906] and cleaning up the different rooms. I'm
[1909] going to ask it.
[1911] And by the way, this is connected to
[1913] GitHub Copilot.
[1916] Um, using the semantic layer, what
[1920] are the droid success and failure rates
[1925] for
[1926] servicing trips?
[1930] One of the things you'll see is it's
[1932] going to actually query the semantic
[1934] layer. It's going to ask me
[1936] if I like that query. We're going to let
[1938] it go ahead run the query. It's going to
[1941] provide this. And we see that we're
[1944] actually having quite a high failure
[1945] rate on actually servicing and taking
[1947] care of the rooms. About one in every
[1950] five, almost a 20% failure rate. It's
[1953] not great. That could mean we have
[1955] unclean rooms. They're not getting taken
[1957] care of.
[1958] um could mean that there's problems with
[1960] our droids and we should take care of
[1962] them so that way rooms can be serviced
[1964] for those who come
[1967] to see us.
[1970] This is a great way for us to find and
[1972] identify these sort of things fairly
[1974] quickly. And if we take a look here,
[1977] we'll see that a lot of this is tied to
[1979] just having the semantic layer in place,
[1983] having those things executed inside of
[1985] DBT, having those artifacts exposed out
[1988] there for the MCP server to go
[1989] communicate with that server
[1992] and bring those results back.
[1998] But this isn't the only one that we
[2000] could do this for. We could also ask
[2005] Using the semantic layer, what is the
[2010] average base cabin cost, package,
[2014] revenue, tax, fees,
[2018] and loyalty discount
[2021] applied for each loyalty tier.
[2027] Again, we can build out this very
[2029] complex set of calculations. We can see
[2032] it's able to go over there. It's
[2034] returning and going, hey, here's the
[2035] command for me to go query the
[2037] semantically for me to go return those
[2039] results and group them up appropriately.
[2043] We have it grouping them, breaking them
[2045] down, providing those results. We can
[2048] see it even generating a set of insights
[2051] based off of what it's seeing in that
[2053] chart. You know, what are the different
[2055] loyalty tiers? What are they paying?
[2059] What's their package? what's the tax
[2061] that they're spending, the average fees,
[2064] and the discounts those are receiving.
[2066] Well, you can see here that for the most
[2068] part, the loyalty discount seems to be
[2072] heaviest once you get into the Jedi
[2073] master area.
[2076] And so, we need to make sure that we
[2079] are letting those in Padawan realize how
[2081] much they're missing out on by not
[2082] paying to be in these upper tiers of the
[2085] loyalty service.
[2087] This helps us identify those types of
[2089] things. And again, it's able to do this
[2091] due to all the context that exists. And
[2095] you're probably seeing this and going,
[2096] "That's great, but that's in my IDE. It
[2099] has nothing to do with the hollow
[2101] chatbot." The chatbot isn't the only
[2104] place we have to do this. This DBT MCP
[2109] is a package out on Pi. We can install
[2113] it. We can utilize it with other things
[2115] like lang chain or open AI and these
[2118] different tooling whether it's strands
[2121] etc. pull these together to create chat
[2124] interfaces that we can communicate with.
[2128] As an example I threw together a very
[2131] very simple
[2133] chatbot here and there's examples of
[2134] these inside of the dbt MCP
[2139] repo.
[2142] If I go ahead and run my chatbot here,
[2144] it's going to start up my environment. I
[2147] have a little terminal. This is the
[2149] hollow hollow chatbot that we were
[2152] talking about.
[2154] Well, what is this made of? If we come
[2156] down here, we actually have bunch of
[2159] different
[2161] parts of MCP that have been brought in
[2164] and OpenAI. And this one's using OpenAI
[2167] to just interact and create a chat
[2169] stream, interacting with MCP,
[2173] feeding information between the two, and
[2176] allowing me to have a chat interface.
[2182] This allows me to start to ask similar
[2184] questions that we could start to put in
[2186] the hands of our business users
[2190] or into our customers
[2194] using the semantic layer.
[2198] What loyalty
[2200] it helps if I spell it correctly tier
[2204] receives the best discount?
[2208] Again, this is using totally different
[2210] interface. This is using open AI.
[2212] Ideally, we see a similar thing that
[2214] master is the one that comes back as
[2218] having the best
[2222] loyalty tier. We can see it interacting,
[2225] calling the different parts of the MCP
[2227] server, returning the metrics, analyzing
[2229] which metric to use.
[2234] As it's going through this, it will
[2237] return a set of results
[2240] and it is saying that there is roughly a
[2243] 15% discount rate for master and it
[2246] recommends that as the best loyalty
[2249] tier. Now, we don't get the 15% discount
[2252] rate by looking at our average base
[2256] cabins
[2258] information over here, but we do see
[2260] that master is the highest. And so we
[2262] are seeing these things are relating.
[2265] They're making sense. The results that
[2268] we're getting from the bot line up with
[2269] what we see out here. As well as if I go
[2271] query the data.
[2273] This allows us to generate that
[2275] interface by using DBT's MCP server
[2279] to understand the context of our DBT
[2281] project.
[2283] Connect to the environment.
[2286] Query the DBT semantic layer. Do
[2288] searches and lookups on those things.
[2291] and understand what is out there and
[2294] what is available to us.
[2297] Provide answers
[2300] utilizing our transformations and all
[2302] the context we've put in place on that
[2305] by again utilizing the semantic layer to
[2309] explain how does our final data set
[2312] connect? How does the different
[2315] attributes across the dims and the facts
[2318] join up? How do we wish to calculate
[2321] those different metrics that we want to
[2324] utilize? What is the documentation
[2328] of that information?
[2331] Relaying
[2332] what exists,
[2334] why it exists, what its purpose is. This
[2338] helps us provide governed answers
[2342] while reducing our hallucinations
[2345] with our data sets.
[2347] All utilizing DBT's MCP server. Again,
[2351] connecting to our DBT instance,
[2355] executing our code locally to help us be
[2359] more efficient with our workload,
[2363] and help us provide better context to
[2366] the large language models that we use.
[2369] Regardless of whether we're using
[2370] something like a co-pilot
[2373] to improve our development workflow or
[2376] trying to create a new unique customer
[2378] experience that makes it easier for our
[2381] customers to get answers and understand
[2383] what is going on, such as whether or not
[2386] they should upgrade their loyalty tier
[2389] and if the upgraded discount will be
[2392] worth it.
[2394] And so with that, I know there's a lot
[2396] of stuff here. There's a lot of things
[2398] to see here. Go look out at the DBTMCP
[2403] repository. You'll see an examples
[2406] folder with a lot of these different
[2407] examples out here that you can start to
[2409] experiment with and see what it's like
[2410] to utilize
[2412] the DBT MCP server to create
[2417] that context needed to start to build
[2420] out an agent that serves the needs of
[2424] your organization
[2426] and can actually begin to calculate
[2430] the different
[2433] metrics
[2434] and provide insights efficiently and
[2438] effectively.
[2440] And with that, I will hand it over to
[2443] Rob for
[2445] one last connect. Thank you everyone.
[2450] All right, just wanted to thank Dakota
[2452] and the PH data team for that fantastic
[2454] uh kind of walkthrough. The last thing I
[2457] just want to cover before we kind of end
[2459] this webinar today is DBT agents. And so
[2464] while we talked earlier about the DBT
[2466] MCP server, DBT is also DBT platform is
[2471] also working on uh building several
[2473] agents directly inside of the platform.
[2476] And so what that means is that we're
[2478] going to have tools such as an analyst
[2480] agent, discovery agent, observability
[2482] agent, developer agent, and even more
[2485] over the upcoming months that are going
[2487] to be able to solve specific parts of
[2489] the ADLC directly inside the platform.
[2493] Um, the first one I've tried is uh the
[2495] insights which uh lets you naturally use
[2500] natural language uh querying to generate
[2503] SQL and get results. Um, but these are
[2506] really exciting in that it's going to be
[2507] one of the easiest and most powerful
[2509] ways to use the new DBT AI uh directly
[2512] inside DBT platform.
[2515] But, um,
[2517] thanks for joining us and please
[2519] continue to ask your questions in the
[2521] chat so we can get them answered for
[2523] you. And we've got a couple of next
[2525] steps for you. If you'd like to connect
[2527] with DBT experts from DBT Labs or PH
[2529] Data, feel free to click on the talk to
[2532] an expert button. Join us in January for
[2535] a webinar with Omni on using the DBT
[2537] semantic layer to deliver AI agents. Uh
[2541] there's gonna be a link in the chat. You
[2542] can register now. And then lastly,
[2544] there's a survey that I also sent in the
[2546] chat. So, please take the the two-minute
[2548] survey for us. We really appreciate your
[2550] feedback and want to improve our virtual
[2552] event uh events for y'all. And then
[2555] thank you again for joining us. I hope
[2556] you had a great day and uh happy
[2558] holidays.
