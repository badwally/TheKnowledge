---
schema_version: 1
id: yt-lvu_p-oZ_Zc
type: youtube
title: 'Stop Hallucinating: Improving AI Safety With Stardog Safety RAG'
url: https://www.youtube.com/watch?v=lvu_p-oZ_Zc
authors:
- Stardog
ingested_at: '2026-06-17T20:57:03Z'
content_hash: sha256:0efb1dbcbb6983f7a6f37917b405b7ad746a74f0976e787077b9118ac7e95dd2
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Stardog
  channel_url: https://www.youtube.com/@stardog-union
  duration_seconds: 2947
  caption_track: fetched
  snippet_count: 1199
filter:
  score: 0.75
---
[0] Uh good morning, good afternoon. My name
[2] is Naveen Chararma and I'm the head of
[4] product here at Stardog. Excited to
[7] bring uh a topic that's top of mind for
[11] a lot of folks, especially in the
[13] context of Gen AI, all about
[15] hallucinations and what we can do to
[17] help improve on that from an AI safety
[20] perspective with a very unique approach
[23] that uh we've taken here at Stardog. Uh
[26] so excited to bring uh some of my
[30] thoughts uh and and of course point of
[32] views uh and look forward to uh hearing
[36] from you and your questions. And for
[37] those that do have questions, please use
[39] the Q&A uh channel to uh put in your
[42] questions and as I go through my slides
[45] u and into my demonstration, I will take
[48] a moment to look through those questions
[50] and answer as quickly as I can. Uh so
[53] again, let's get started. So I know um
[56] this topic uh comes up pretty much uh
[61] every uh a conversation I have with
[64] large enterprise organizations that are
[66] embarking on and looking to bring Gen AI
[70] into the enterprise. Um and one of the
[72] topics uh certainly for those in those
[75] in regulated industries tends to be
[76] around AI safety.
[79] But we also know uh clearly at this
[83] stage that uh every industry
[87] will look to empower their knowledge
[90] workers with AI but the key to that
[93] enabling and empowering is going to be
[95] AI that's grounded in trusted data and
[98] those are the companies that will be the
[99] winners in the in their respective
[101] industries. Of course, at the same time,
[104] we also know that um many of the large
[106] enterprise organizations are certainly
[110] limited by
[112] where they are in their own data journey
[115] um in terms of uh you know data being
[118] fragmented uh as a challenge that
[120] they're dealing with. Um, data lacks
[124] meaning because it lacks context
[126] oftentimes, especially when it gets
[128] ripped out from its source system and in
[131] onto some sort of a data lake uh or or
[134] or a lakehouse. Uh, and and I and then
[138] of course there's a constant struggle
[140] with skill set requirements and the cost
[143] of technology infrastructure to enable
[145] gen AI inside of the enterprise. And we
[148] know that AI hinges on trusted
[149] enterprise knowledge
[151] and and and that's critical given the
[154] era we're in and given what we're
[156] learning with this fastm moving very
[158] exciting space in the market.
[161] Um but we also know that there is
[164] general anxiety about Genai out there in
[168] the enterprise and it's no surprise uh
[171] given what we are hearing in the news
[174] pretty much on a daily basis. Uh this is
[177] a few of those headlines where a lawyer
[180] used the chat GPT in court and cited
[182] fake cases to the point where the judge
[185] was actually considering sanctions.
[188] We also know u that beyond
[191] hallucinations
[193] uh we we find that uh the reliance on
[196] large language models for answers tend
[199] to be static in nature uh and of course
[202] generalized uh in that sense that it's
[205] all about general knowledge not
[207] knowledge about your enterprise and it's
[209] knowledge that's perhaps a little old
[212] and this kind of brought out that point
[214] that I wanted to make with the Bing AI
[216] chatbot where someone actually asked for
[219] movies that were playing on the weekend.
[221] Uh which despite using the right sources
[224] for the information, it persisted on
[227] presenting movie names that were movies
[230] from 2021.
[232] Uh so you can kind of imagine the
[234] distrust and uh and and of course the
[238] hallucinations just make the make the
[240] make those issues uh top of mind and
[243] paramount for for enterprise
[244] organizations you know trying to to
[246] bring this type of technology inhouse.
[249] Um this in fact was in the news even
[250] with uh Google and and their Gemini roll
[254] out when someone asked uh you know the
[256] best way to stick cheese onto the pizza
[258] bread and pizza dough and Gemini shot
[261] back you have to use glue. Um so no
[264] surprise uh that anxiety uh there's a
[267] good reason for that anxiety
[269] uh and the and the healthy skepticism is
[271] always good and of course we know now
[274] that as we engage and embark in in some
[277] of these initiatives inside the large
[278] enterprises uh there's a popular
[280] architectural pattern that's starting to
[282] take hold uh especially in the context
[284] of what's called retrieval augmented
[286] generation or rag
[289] um and if you think about what rag
[291] essentially is it's essentially
[293] the ability for organizations to break
[297] down large text corpuses uh documents
[300] into
[301] sizable chunks that get indexed to help
[305] with retrieval. Uh making the retrieval
[308] process easier utilizing what's called
[311] vector-based semantic search. uh
[314] ultimately presenting the retrieved
[318] specific retrieved set of text chunks to
[321] the LLM to be then the to become then
[324] the final arbiter uh in terms of helping
[328] it reduce hallucinations with additional
[331] or better context
[333] and that's great. Um the key words here
[336] emphasis on documents and reducing
[339] hallucinations.
[340] Of course, at this stage, many of you
[343] should already be further down in your
[346] own journeys. And for those that are
[347] just getting onboarded and learning, uh
[350] perhaps these limitations
[353] uh may give you a bit of pause before
[355] you consider going down a path and
[357] investing a lot of time. Uh we do know
[359] that rag have rag rag implementations do
[362] have limitations. Number one, they're
[364] still very much limited documents. Um so
[367] when it comes to asking questions of
[370] data that sits inside of your trusted
[373] sources, your proprietary data sources
[374] like databases or applications,
[377] uh rag doesn't really help much. Number
[380] two, you saw the word reducing
[384] hallucinations. Now reducing
[386] hallucinations we all know is not the
[388] same as eliminating hallucinations.
[390] Great. I have reduced the amount of
[392] hallucinations I generate by accessing
[396] information directly from the large
[397] language model. But ultimately even
[399] after the rag approach uh where you're
[402] presenting it relevant context with
[405] chunked text you still find that there
[408] are sufficient amount of hallucinations
[410] that might give you pause especially in
[412] regular industries and the fact that
[414] you're still relying on the large
[416] language model to be the final arbiter.
[419] Third, we know that there are still
[421] challenges with dynamic knowledge. Um,
[425] and what that means is at this stage, we
[427] are still relying on information that's
[430] old, outdated, not real time in order to
[433] answer a question. And the dynamic
[436] nature of enterprise data, it's always
[437] constantly changing.
[439] And then last, there's limited context.
[442] um because the context still centers
[444] around this notion of nearest neighbor
[447] searches to the specific set of concepts
[451] that are referenced in a particular
[452] question that helps me identify the
[456] right text. But what I don't have is
[458] this sort of deep crossdmain knowledge
[461] where data is is dense uh and data
[464] exists across domains and that connected
[468] nature of data the relationship between
[469] data is intrinsic and sometimes not
[473] picked up by these vector-based semantic
[476] approaches. And so those limitations
[479] certainly hinder your ability to provide
[481] accurate contextually relevant
[483] information.
[486] Of course, it is no surprise then that
[488] Gartner uh has started to really call
[492] out uh in their own review of the the
[495] technology landscape and what they find
[499] has been working well in terms of um
[502] genai applications
[504] is the usage of AI
[507] and along with knowledge graphs. uh and
[511] the idea of knowledge graphs has been
[513] around for for some time. You know, it
[516] started with uh the the sort of the the
[520] advent of uh evolution of search by
[522] Google and to the extent that we're now
[525] in this universe where Genai is becoming
[528] increasingly important to and you know
[531] enabling your knowledge workers to to
[533] answer questions about uh your business
[536] data. knowledge graphs really sort of
[539] shine because they deliver trusted and
[542] verified facts to the outputs that are
[545] needed in order to generate a response
[547] from large language models. Um and so
[550] being that this center of this bullseye
[553] means that this is a widely adopted
[557] pattern. Gartner is beginning to
[559] recognize talking to their growing use
[563] of enterprise uh organizations and
[566] members inside of those organizations.
[569] So why knowledge graphs? We know
[572] knowledge graphs are great at capturing
[575] business context. those that crossdomain
[578] knowledge
[580] and why it's especially important is
[582] because it's abstracted away from your
[584] data estate. So think about all the
[587] tables that you that are sitting inside
[590] and locked up inside of your enterprise
[592] systems from data links, multiple data
[594] links to data warehouses, multiple data
[596] warehouses to applications to multiple
[598] applications
[600] and not fully recognizing the
[603] relationships across those domains
[606] silos, across those data silos, uh
[609] across those application silos. And so
[612] by abstracting and modeling information
[615] in the way it needs to be understood and
[618] consumed in a knowledge graph, you are
[621] essentially establishing that
[623] cross-domain context that is important
[626] for the consumer in this case the genai
[630] application to fully comprehend and
[632] understand in order to be uh in a
[634] position to accurately respond and more
[636] importantly to ground itself in
[639] enterprise truth. And so here's a very
[641] simplistic example of domains across
[644] customer systems, policy systems, claim
[647] systems being articulated in this
[650] right-hand image as the semantic data
[653] model representation
[656] of what information means to the
[658] business and the business use case uh
[660] that you're trying to enable. uh
[662] regardless of where the data sits,
[664] regardless of where how the data is
[666] structured uh and regardless of where
[668] the data is located
[671] and and that manifests it itself in you
[674] know across multiple industries. So you
[676] can think about cross domain knowledge
[677] you know what does that really mean? You
[678] know, here's an example of supply chain
[681] where there's a severe quality note for
[684] a fender burn associated with a
[686] particular vehicle VIN number and that
[689] needs to trigger a shop ship stop
[691] shipment in the factory. And so the
[693] questions that you want to ask is the
[694] knowledge workers, the frontline worker,
[697] what are all the quality notes
[698] associated with this particular vehicle?
[700] You know, were there a res was there a
[702] resolution for the quality notes that
[703] was logged? Was there material that was
[706] made up that impacted the component?
[709] Were those materials being shipped or
[710] supplied by one supplier or many
[712] suppliers? Are there orders actually
[715] currently in play that are potentially
[718] impacted? And so you can imagine in this
[720] scenario, you're now looking across
[724] multiple
[725] organizational
[727] functional
[729] data silos.
[730] uh and this domain knowledge needs to be
[733] brought together quickly in order to
[734] respond and answer those questions. Same
[737] is true what you think about it from a
[739] pharmaceutical perspective right drug
[741] repurposing.
[742] I am trying to study the interaction of
[745] a particular drug oxytocin related to
[747] autism and see if there might be
[750] opportunities for a new drug. Right? So
[752] what are the genetic conditions that are
[754] suitable to treating autism? What
[757] compounds actually have been tested in
[759] similar conditions with similar
[760] treatments? Is there a gene expression
[762] that can be used as a biioarker to
[764] understand their the drug that we're
[767] presenting is delivering the desired
[768] effect or which manufacturers supply the
[771] raw ingredients? Uh because I might want
[773] to look at uh an additional supply and
[776] what other studies might be relevant to
[778] answering those questions and again you
[779] can imagine this sort of cross domain
[781] cross application
[783] uh information uh that may not be
[786] readily available or connected in order
[788] to answer these questions. Same thing
[790] with financial services. You know,
[792] trying to understand if certain board
[794] members for companies are being
[796] investigated uh based on uh you know
[799] their their relationship with the
[801] organizations that they sit on and you
[803] can kind of understand you want to
[805] understand the affiliation of these
[806] individuals. You want to understand the
[808] financial stake of these individuals.
[810] Maybe you want to understand what other
[811] companies uh they are they connected
[813] with. Where are those companies located?
[815] What are those transactions between
[817] those companies between those
[818] individuals? Are there subsidiaries? Are
[820] there shell companies? That can really
[823] get complex. And again, information that
[825] comes from across systems, across
[827] functional areas in order to be uh
[830] visible and viable for for someone to be
[832] able to answer deep domain contextually
[835] relevant questions.
[837] And so knowledge graphs really start to
[840] address those limitations of rag and
[843] sometimes labeled as graph rag which is
[847] further reducing hallucinations
[851] helping reason over connected data based
[854] on business logic versus reasoning that
[857] LLMs
[859] that tend to sound like they're
[862] reasoning over data but really they're
[864] predicting based on probabilities of
[866] words. What's the next set of words that
[869] make sense based on the word that's
[871] that's in front of me? That's not quite
[873] reasoning over your data, over your
[876] enterprise data, based on your business
[878] logic.
[880] And then of course the the knowledge
[882] graphs really shine when it comes to
[884] enhancing the accuracy of the answers
[887] because they encapsulate that deep
[889] crossdain
[890] business knowledge that's important to
[892] answering the questions that I just
[894] highlighted with some of the use cases
[895] above.
[898] With Stardog, we have taken an approach
[901] that brings all the benefits of a
[904] knowledge graph plus more. And so what
[907] is that plus more? And we call this this
[909] notion of a safety rag. Number one, it's
[913] a fully integrated out- of-the-box
[915] experience for organizations that are
[918] trying to prove out genai use cases. And
[922] this fully integrated out-of-the-box
[924] experience comes with prescriptive
[925] industry use case-based ontologies or
[927] semantic models.
[930] So you don't have to start something
[931] from scratch. You can leverage these
[934] industry ontology models as a jumping
[936] off point to
[938] mapping out information against your
[940] data landscape and enabling Gen AI
[944] application for your knowledge workers,
[946] frontline workers to begin to ask
[948] natural language questions to again get
[950] natural language answers.
[952] Number two, the limitations of rag is
[956] and even graph rag for that matter is
[958] still focused on documents. And so
[961] Stardog with its safety rag approach
[963] allows you to operate over both
[965] structured and unstructured data
[967] sources. And these could be data sources
[969] that are data links, these could be data
[972] sources that are data warehouses, this
[974] could be application data sources,
[975] semi-structured databases as well. and
[978] and and to that extent we uh uh
[980] integrate over 150 plus data sources
[984] and and our approach is key here because
[988] one of the limitations of rag and even
[990] graph rag for that matter has always
[992] been the fact that you're still relying
[994] on uh point in time data right now data
[998] is is dynamic uh fast changing at times
[1002] and we utilize this this approach that
[1005] is hybrid approach utilizing data
[1007] virtualization a combination of data
[1009] virtualization and materialization so
[1011] that when we are answering the question
[1013] we are accessing the most up-to-date
[1015] dynamic real-time information within
[1017] your enterprise.
[1019] And last but not least and this is the
[1021] the the critical point from a safety
[1022] rack perspective is
[1025] all answers are grounded based on the
[1027] ontology of the model
[1029] and the and the final answer that is
[1032] generated comes from your enterprise
[1033] sources and not the large language
[1035] model. And so what that means is we're
[1039] eliminating hallucinations and ensuring
[1042] there's trust with full traceability
[1045] from from where we got the answers. Uh
[1048] and that's a key differentiation fact
[1050] differentiating factor is that the the
[1052] reliance on large language model is not
[1054] to generate the answer in our case and
[1057] I'll talk through this in in in the
[1058] demonstration as well. In our case,
[1061] we're relying on the large language
[1062] model that we have fine-tuned for our
[1064] purposes to generate a structured query
[1067] and then we execute that query in a
[1068] federated manner against your enterprise
[1070] sources and get those answers directly
[1073] from your enterprise sources in order to
[1075] answer the question based on the
[1078] grounding that comes from the ontology
[1080] of the semantic model that I shared
[1081] earlier.
[1083] So what that allows you to do then is
[1087] basically enable your knowledge workers
[1089] to ask any question about any data and
[1092] get timely, accurate and explainable
[1093] answers. And this is utilizing the
[1096] combination of enterprise knowledge
[1098] graphs and generative AI to deliver a
[1101] powerful knowledge worker based chat
[1105] interface to to your enterprise data
[1108] where you know data is accurate, timely,
[1110] secure and hallucination free.
[1114] And again I'll I'll showcase how this
[1116] all comes along. But more importantly
[1118] what's what you need to know is that
[1121] this of course for many companies is a
[1123] journey and so while you may not be
[1126] ready to ena you know enable your
[1129] knowledge workers with a natural
[1131] language interface to start asking
[1133] business questions of your enterprise
[1135] data on day one. What's important for
[1137] you to understand is that knowledge
[1139] graphs
[1141] and and enterprise knowledge graphs from
[1144] uh providers like Stardog specifically
[1147] allow you to create this modern data
[1150] foundation so that your data is geni
[1152] ready
[1154] by essentially creating a flexible
[1156] semantic data layer that sits between
[1159] where your data lives and where your
[1161] data gets consumed. It harmonizes data
[1164] based on business meaning that's
[1166] abstracted away from all your data
[1168] estate and it utilizes the benefit of
[1172] these the sort of onto ontological based
[1175] concepts or informationational models
[1176] business information models to abstract
[1179] and attach meaning to the data and more
[1181] importantly it limits data sprawl so
[1183] you're not constantly moving data in
[1185] order to answer and enable those
[1187] questions that I shared with you earlier
[1189] you're leaving data in place and so at
[1192] query time that computation can gets
[1194] gets uh pushed down to the source system
[1197] if need be from a federated data access
[1200] perspective and more importantly you're
[1202] now enabling your citizen data users to
[1205] self-s serve and doing so with a
[1207] foundation that facilitates reuse and
[1210] sharing through open standards and
[1211] that's critical for you to understand
[1214] this is widely now adopted across many
[1216] many European companies and in very
[1219] specific industries like public sector
[1222] uh where we're working very closely with
[1224] the intelligence community as an example
[1227] of the type of standards that we're
[1228] trying to bring to improve data sharing
[1232] uh across uh multiple agencies. Uh and I
[1235] know that's the same same is true for
[1237] for organizations inside
[1239] uh functional areas uh within an
[1241] organization where they want to
[1243] facilitate reuse and sharing uh through
[1246] open standards. So this M modern data
[1248] foundation is sort of almost like a
[1251] layup for what we're really trying to
[1254] enable in the Genai scenario sort of
[1256] this agent-based architecture that can
[1258] then operate on that knowledge graph
[1261] where a question gets asked
[1263] and and an answer gets produced both in
[1266] a natural language interaction
[1267] perspective you know we understand what
[1271] part of the uh the business the concepts
[1273] that are being referenced in the
[1275] question actually are referenced in the
[1277] actual knowledge graph and then we're
[1280] able to generate a query a structured
[1282] query for that and then look to your
[1285] enterprise data sources in a federated
[1287] manner to get the answers and present
[1289] those answers or summarize those answers
[1291] back to the user or do further analysis
[1294] on the data or generate more charts
[1296] describe the entity itself or in our
[1300] scenario we're also leveraging the power
[1302] of external LM so that there is an
[1304] element of tapping into what is good out
[1307] there sometimes which is this broad
[1309] general knowledge that still can be
[1311] leveraged uh perhaps in order to help
[1314] the user do their job. Ultimately, it's
[1317] about helping uh specific users in these
[1320] industries uh with their jobs to be done
[1323] and um and giving them ultimate access
[1326] and power to information whether it's
[1328] tap tapping into your knowledge sources
[1331] inside the enterprise or general
[1332] knowledge that's available is part of
[1334] the the the value that we can bring with
[1336] this sort of multi- aent orchestration.
[1341] So, what does it all look like? Well,
[1343] let's dive right into it. Um I will give
[1345] you a quick demonstration um to kind of
[1348] have some of these concepts uh bring
[1350] some of these concepts to life. Uh I
[1353] will also take a moment to see if there
[1355] are any questions
[1358] from anyone here that I can answer.
[1364] Okay. Uh let's see. We have a few
[1366] questions. What are the most common
[1367] scenarios where hallucinations occur in
[1369] AI systems and how how can Stardog
[1372] mitigate these risks? Hopefully, Lynn um
[1374] with the the slide where I see you
[1377] decided to ask that question the
[1379] beginning of my presentation
[1381] uh hopefully uh it's been made clear
[1384] through the end of my presentation uh so
[1386] far uh in terms of how Stardog takes a
[1389] unique approach.
[1391] Um what does the conceptual architecture
[1393] look like Robert? Uh hopefully you saw
[1396] that in the last few slides. I'm happy
[1398] to uh speak to it a little more broadly
[1400] if you have more specific questions.
[1402] Ultimately like I said we sit between
[1404] your source systems and your consuming
[1406] applications uh and providing a sort of
[1410] a semantic data layer. Um whether it's
[1413] an implementation of data mesh or data
[1415] fabric um many approaches have been or
[1418] data products. Um those are typical ways
[1420] that companies start to build this
[1422] foundation with Stardog's knowledge
[1425] graph approach.
[1426] Um question from Shrian. Do you have
[1429] financial like banking system ontology
[1431] mapped? The answer is yes. We can not
[1433] only take we've mapped a lot of
[1435] different ontologies across different
[1437] industries. Certainly a good great way
[1439] to jump start like I said your genai use
[1441] cases uh and prove out uh those use
[1444] cases uh quickly. Um
[1449] uh I will talk about uh our approaches
[1452] and that might come across uh clearer
[1454] when I start to demonstrate as well. Uh,
[1457] how do you stop LLMs from hallucinating
[1460] when it comes to generating the proper
[1461] query? That's a good question as well,
[1463] Harry. Harry, we use a combination of um
[1467] fine-tuning approaches for the large
[1469] language model that we do utilize for
[1471] our purposes for from a query generation
[1474] perspective, but we also have uh the
[1476] ability to do selfcorrection.
[1478] So it's a bit of an autonomous
[1481] um interaction that happens between our
[1484] query engine and and the large language
[1487] model. When we see a response of a
[1490] specific query that has errors, we have
[1492] validation we have validation steps in
[1494] there and then we ask a specific we send
[1497] a specific response back asking for
[1500] corrections to those validation errors
[1501] and so that interaction happens behind
[1503] the scenes.
[1506] All right. Um, if using enterprise
[1508] sources instead of the LLM to generate
[1510] the answer, what is the enterprise?
[1514] What if the enterprise is not in a
[1516] user-friendly format? Uh, see loads of
[1519] nested structured data when they expect
[1522] a neat natural language sentence. Yeah.
[1524] So, I mean, look, this some of this is
[1526] some some good UI magic. other is just
[1529] the way you want to break down the
[1531] specific uh ontology or the data model
[1534] that reflects information in those
[1536] sources. There's multitude of ways to do
[1539] that. Um uh and again I'll I'll showcase
[1542] and highlight some of those as well for
[1544] you here as we go through the
[1546] demonstration. Um what differentiates
[1549] you from Neo Forj and others Robert? I
[1551] mean the big key difference here is that
[1553] as I mentioned we're not taking a rag
[1557] based approach which is first of all
[1559] focused on documents second of all is uh
[1563] leaving the ultimate LLM as the arbiter
[1565] of the final answer um in the in our
[1569] case you know we can operate not only
[1571] our Dota documents but databases
[1572] structured databases semiructured
[1574] databases and then we ultimately rely on
[1577] the enterprise sources as the source of
[1579] truth for the answers that we present
[1580] back to the user. And then more
[1582] importantly, our federation approach
[1584] allows us to leave data at source. So
[1586] we're actually accessing real-time
[1588] dynamic data versus neo forj which is a
[1590] graph database where you actually have
[1592] to physically copy move data before you
[1593] can do any take any action. Hopefully
[1596] that answers some of the questions
[1598] specific to that. Um and then are you
[1600] using multiple ontologies
[1603] based on a general business or does they
[1604] need to be specific to the business and
[1606] thus bespoke? Yes and yes. Right. So we
[1610] we certainly can leverage industry
[1612] ontologies that are relevant from a
[1614] general business perspective. Um every
[1617] industry every use case is very
[1619] specific. And so the idea here is that
[1622] we're trying to um make this as focused
[1626] from a from a benefit to the user
[1630] perspective. And sometimes that might
[1631] require some changes to the ontology or
[1634] to be very specific. Sometimes re adding
[1636] reasoning logic that is specific to a
[1639] user or user use case that can also be
[1642] um annotated on top of the semantic
[1644] model. I'll talk about that as well. So
[1647] lots of good questions. I'm going to
[1648] take a quick break here and get into the
[1650] demonstration. I'll come back to the
[1652] questions after the demonstration. Let
[1654] me go ahead and share my desktop again.
[1657] And
[1661] there it is. Sorry.
[1666] All right, let's move to the
[1667] demonstration part of this.
[1669] So, um
[1672] I will open up our uh voicebox
[1676] application here. So, we can go into a
[1679] new chat.
[1681] Um I'm taking a context of a healthcare
[1683] scenario. This can be a supply chain.
[1685] This could be um a financial use case as
[1689] I mentioned some of those uh examples I
[1691] shared earlier. In this case I have
[1692] healthcare patient data where I'm
[1695] looking at medical conditions uh
[1697] performed during encounters with
[1699] providers uh with prescriptions and
[1701] diagnosis and the treatments that have
[1703] been administered.
[1705] And as a uh you know healthc care
[1708] professional I'm trying to uh better
[1711] understand the implications of and
[1713] effects of certain medications. Perhaps
[1714] I'm in pre-clinical clinical R&D uh and
[1717] I need to better understand all of this.
[1719] U you can imagine a lot of this data
[1720] sits across silos. Uh and so the
[1723] interaction here this is sort of from a
[1725] context of our user interface. Obviously
[1728] there's an API behind this if you want
[1729] to embed this within your own
[1730] applications. So maybe as a user I can
[1734] start off with some you know preset
[1736] questions that are important to me.
[1738] Things like list the years of how many
[1740] procedures were performed in that year
[1742] in decreasing order. And you can see
[1745] immediately we come back with a
[1746] response. There's 35 years of recording
[1749] procedures. Uh you see the listing of
[1751] the year and the procedures. I can
[1753] review this data in a sort of um
[1755] tablelike structure if I wanted to do
[1757] that. Um what's also interesting is when
[1760] I came back with the answer I have uh
[1763] the ability to kind of see move this
[1766] here
[1770] um explain the response. I can see that
[1773] procedure was performed and I can see
[1775] the structured query behind it that was
[1777] generated and this allows me to then see
[1779] the source of the information from which
[1781] I I was able to pull this data from. Um,
[1784] so that that's part of the the query
[1786] generation piece that it runs behind the
[1788] scenes. Uh, I may want to turn this into
[1790] a
[1792] chart, bar chart. Um, and again, the
[1796] idea here is that I can not only look at
[1797] table data, but I can look at sort of
[1799] more uh visual information presented to
[1802] me. Now, of course, there's a lot of
[1803] data here. So, if I wanted to analyze
[1807] um trends, I can kind of look at those
[1810] as well and say, okay, what is the data
[1812] really telling me? help me with the
[1813] analysis based on this data set. I can
[1816] see that there's general trends around
[1819] data either significantly increasing the
[1822] number of procedures performed.
[1823] Obviously, that's visually
[1826] uh evident in the chart here, but you
[1828] can kind of see this is sorted in the
[1830] order of the year of a number of
[1832] procedures. Uh and so that analysis is
[1835] now presented back to me here. Um
[1839] uh and then of course I can also utilize
[1841] multiple agents that sit behind this to
[1844] run um computation more complex
[1846] computations to compute the total
[1849] procedures
[1852] performed
[1855] and its standard
[1858] deviation.
[1860] And again here I'm leveraging the power
[1862] of uh certain uh language models that
[1866] are better at mathematical statistical
[1869] operations. You can kind of see I I've
[1871] been able to come back with a response
[1872] from the total procedures and the
[1874] specific standard deviation. Now from
[1876] here I may want to ask questions like
[1878] you know uh which
[1881] was the most
[1884] prescribed
[1887] or which medication was prescribed the
[1889] most. Right? I mean so there's multiple
[1890] ways. Uh the idea here is I want to
[1892] understand you know which which
[1893] medication was prescribed the most so I
[1895] can kind of ask that question.
[1898] Um and
[1900] when I do that
[1902] I'm also looking at the dynamic uh gen
[1907] prompts that get generated that I may
[1909] want to ask more questions. Uh but you
[1912] can also see the interpretation. I just
[1914] said which medication prescribed the
[1915] most. it kind of came back and
[1917] interpreted it to be which medication
[1918] was prescribed the most from 1971 to
[1920] 2019. So it has that multi-turn
[1923] conversational context from my previous
[1925] set of questions to understand what
[1928] needs to be applied in order to answer
[1929] the question. You can kind of see that
[1931] it actually came back with uh the
[1933] specific information about the
[1935] medication uh with total 219
[1938] subscriptions and the these hyperlinks
[1939] represent information that I'm actually
[1941] pulling back from my enterprise data
[1943] sources and I can kind of look at that
[1946] you know in sort of a graph-based view
[1947] here and I can see everything associated
[1950] with that particular uh medication in
[1953] terms of diagnosis prescriptions
[1955] encounters conditions etc. Um, in that
[1959] information I can see more details about
[1961] the specific treatments and when they
[1963] were highlighted and I can see uh what
[1966] else it tells me about the predictions.
[1968] So if I have ML models that are attached
[1970] to uh the specific medication, I can
[1974] kind of look at what those predictions
[1976] are telling me uh for the types of
[1978] conditions that are associated with that
[1980] medication as well. That's part of my uh
[1983] you know larger knowledge graph. uh I
[1985] can also continue the conversation from
[1988] that full page experience but I'll kind
[1990] of go back to the full page experience
[1991] for now and I and here I can kind of
[1994] also leverage um some of this external
[1996] knowledge base as well right so if I say
[1999] what are
[2001] the side effects
[2005] of Smith's and I can type so I'm just
[2008] going to copy this here
[2011] um medication here
[2015] uh one of the important elements of this
[2017] for us is you know when when do we know
[2021] not to answer a question right this is
[2023] the part of the no hallucination so you
[2025] know we came back with cannot find an
[2026] answer partly not partly 100% because
[2031] this information was not grounded in the
[2035] semantic model and it was not mapped to
[2039] an enterprise data source uh and so We
[2042] will always on the side of we cannot
[2044] find an answer to this question. But if
[2046] we wanted to leverage the external
[2048] knowledge base of a given large language
[2053] model that you know the organization is
[2055] using or you want to leverage a third
[2057] party or a llama 31 doesn't really
[2059] matter. We have the ability to configure
[2061] access to this um external knowledge
[2065] base. So again from a user perspective
[2068] they get the information they want with
[2071] the caveat that you know we remind them
[2073] that this is unverifiable data. It can
[2076] still contain hallucinations but at
[2078] least they have information that they
[2079] can use some judgment to say yes I can
[2082] understand the side effects of that
[2085] medication. uh in this particular
[2087] context I can say who are the patients
[2093] that were prescribed
[2097] that medication.
[2100] Um and and again from here
[2104] I can generate you know perhaps a very
[2107] specific say again I can't answer the
[2109] question but if I wanted to look and say
[2110] okay what you know what show me the
[2112] specific employees or people uh that
[2115] were diagnosed with this particular
[2117] medication maybe I want to look at very
[2118] specific individual and see if that
[2121] answers the question that I'm seeking
[2124] all of that all of that is prompted by
[2127] really what sits behind this is the
[2129] semantic model the semantic model here
[2131] and I'll open the healthcare one
[2134] is you could kind of see the patient
[2136] data provider data specialty data
[2138] organizational data diagnosis data
[2140] encounter data prescriptions procedures
[2142] we have built a semantic model and then
[2145] this information is mapped back to the
[2147] source of the information so when I pull
[2148] patient data in like I did with ebony I
[2151] can kind of pull back and see that this
[2152] data actually is being pre pulled from
[2155] my delta lake table in data bricks uh
[2158] this could also be attached to um you
[2161] know a whole variety of sources um uh
[2164] from Snowflake to Synapse to Salesforce
[2167] Postgress all of that can be mapped here
[2169] and the the information is federated at
[2172] query time we push compute down to that
[2175] system to in order to answer the
[2176] question now certain sources don't lend
[2178] themselves for real-time querying we
[2180] have the ability to materialize
[2182] information as well either in our
[2183] caching layer or in our in our storage
[2186] layer if that needs to happen as well
[2188] and so in this hybrid approach. You can
[2190] access data that's fast changing
[2192] directly at the source. You can pull say
[2194] move static data information into the
[2197] into um into our storage layer uh for
[2201] materialization and this can be across
[2204] multiple domains, right? This is one
[2205] context around supply chain. We can kind
[2208] of see that we have supply chain data
[2210] about distributors and trucks and
[2212] sensors, selling points, finished
[2215] products, production outputs, and we've
[2217] mapped that data to different
[2218] environments, Snowflake, the data
[2220] bricks, you know, we have customer
[2222] information in this case coming from
[2223] Snowflake.
[2225] Uh, and then we have uh sensor data that
[2227] we're pulling in from data bricks
[2229] because that's fast changing perhaps.
[2231] Uh, we have data mapped to some file
[2233] system. Uh so this is again a variety of
[2236] ways you can uh encapsulate domain
[2239] knowledge as part of your grounding of
[2242] the large language model and when a
[2244] question comes in we identify parts of
[2245] the semantic model we need and those
[2248] relationships within those entities that
[2250] we need to understand to generate the
[2252] query for us and then we push the
[2255] compute down from the federated data
[2256] access against your source systems and
[2258] then summarize that answers back. Now
[2260] what's also important in the value of
[2262] the knowledge graph on top of the
[2264] semantic model is the fact that you can
[2266] reason over your enterprise data and and
[2269] that could be applied based on your
[2271] business logic. Right? So one of the
[2273] things I talk about when I talk about
[2275] anomalies is that anomaly is not a
[2277] concept that exists inside of your
[2278] enterprise data but a business logic can
[2281] be applied and and the data and the
[2283] information can be reasoned over the
[2284] data. So when a sensor has an output uh
[2289] in as part of a temperature reading
[2291] that's being monitored on a truck with a
[2294] value of greater than 45° Fahrenheit,
[2296] then you can infer that truck has an
[2298] anomaly and that sensor output can be
[2300] classified as anomaly. So you can add
[2303] business logic that's relevant to your
[2305] user use cases and this can vary by
[2308] user. the definition of supplier might
[2310] change perhaps uh you want to add those
[2313] and again these can be annotated on top
[2314] of the semantic model and executed at
[2317] the time I'm asking those questions that
[2318] I was showing you earlier
[2321] all right um I'm sure that has generated
[2324] lots of questions uh so let's take a
[2326] quick look
[2328] at where we are
[2331] lots of questions okay I will try my
[2334] best to answer these questions and these
[2336] are
[2338] this is actually coming in the chat
[2339] interface. Let me stop sharing here.
[2342] Um or maybe there in the Q&A as well.
[2347] Uh and the possible returning personal
[2349] information is it possible limit the
[2351] data that can be returned based on the
[2352] user? That is absolutely correct. Uh we
[2355] follow fullback Aback um controls. Uh
[2359] data can be obuscated at from at a finer
[2362] grain level. Um so like a social
[2365] security number can be hashed out or
[2366] phone number can be hashed out and that
[2368] can be based on groups or roles of
[2370] people uh that are uh that are either
[2372] part of the startup system. We can also
[2374] take your roles as you've described them
[2376] in your own identity providers like uh
[2379] entry ID from Azure. Um
[2385] hopefully that answers your question
[2386] Jonathan Robert uh only a SAS solution
[2388] available or is there no on-prem option?
[2390] Yes, there is both a SAS and an on-prem
[2392] option for customers. Um, please reach
[2396] out. Happy to to talk through that for
[2398] you with you as well. Our fully managed
[2400] solution is sits on AWS. Uh, but we have
[2404] a uh VPC option that's available on all
[2407] cloud our major cloud providers. We're a
[2409] dockerized Kubernetesbased system. Um,
[2413] so you can deploy in any of those
[2415] environments.
[2416] Um
[2419] let's see coming back to the previous
[2421] question string procedures uh was there
[2423] hardcoded in NLG output template for
[2426] each attribute hopefully some of this
[2428] was answered through the demonstration
[2432] but if I only have one data source why
[2434] would acknowledge graph be better than
[2436] my own prompt describing my data model
[2439] Harry that's a good question I would say
[2441] this is where I would say if you have
[2443] only one data source and your types of
[2445] questions don't really require complex
[2448] joins at the back end, you're probably
[2451] good with what you have, right? But if
[2453] you're if you're types of questions that
[2454] you're generating or your user is
[2456] generating require complex joins across
[2459] tables even within a single data source,
[2464] um then knowledge graphs are pertinent.
[2466] More importantly, what it's also does is
[2468] it enables you to encapsulate enterprise
[2472] knowledge at the semantic layer or
[2474] knowledge graph level. And so tomorrow,
[2476] if you wanted to switch sources, you
[2479] don't have to necessarily retrain,
[2481] recreate, reprompt data based on uh on
[2484] that source and the way that data is
[2486] structured or how you model information
[2488] there. Because remember the idea of the
[2490] semantic model is you're adding new
[2492] meaning attached to that data. you're
[2495] you're enriching through semantics
[2497] creating uh uh inferring new knowledge
[2501] uh and so those semantic concepts may
[2503] not necessarily exist in your data
[2505] model. So as an example, you know, I
[2507] would say that I'm part of I'm a member
[2509] of the royal family and I have I have a
[2513] parent child relationship to uh you know
[2516] to the prince and the prince has the
[2518] relationship to the king and a parent
[2519] child relationship and that's evident in
[2521] my data model that's evident in my data.
[2524] But what's not evident is the cousin
[2525] relationship, the sibling relationship,
[2527] the aunt and the uncle and the
[2530] grandparent relationship. That's
[2532] something you can semantic semantically
[2534] enrich within your semantic model
[2536] without having to uh rewire your your
[2539] data model uh which was you know again
[2542] designed for fast coefficient querying
[2543] perhaps or or or modeling and and
[2546] structuring data for fast and querying
[2548] not necessarily capturing that complex
[2550] knowledge that is uh is needed.
[2553] Hopefully Harry that answers your
[2554] question.
[2556] Um
[2558] I see the questions have moved over to
[2559] the chat. Uh
[2563] how can I learn about Stardog? Um
[2565] there's lots of information. In fact,
[2567] that's a let let me transition to that
[2569] here and I'll come back to more
[2570] questions
[2572] uh for this group.
[2575] Uh
[2577] back to my webinar slides share mode.
[2581] Okay. Um, how do I get more information
[2584] about Stardog? Which was the question
[2586] that was asked. Um, first, uh, for those
[2590] that are interested in, um, figuring out
[2594] ways to bring rapid value around Genai
[2597] and Genai use cases, we have a very
[2599] methodical approach to enabling this for
[2602] you. We call a zero to 8 week
[2604] engagement. Um we offer both fully
[2607] hosted and a managed service on AWS or
[2609] on prem that can be implemented in eight
[2611] weeks. Um and we typically connect up to
[2614] five enterprise data sources. So
[2616] everything from knowledge engineering
[2618] that requires discovery of data
[2620] connecting mapping data to building out
[2622] the data model or leveraging an existing
[2624] model and making sure that it fits your
[2627] needs uh with a uh which is part of the
[2630] refinement of the model. Uh and then
[2633] there's a test period by your users um
[2636] in order to ensure that the the
[2639] information the answers that are coming
[2641] back are accurate and good and then we
[2643] can roll this out to a larger set of
[2645] user community within your organization.
[2648] Um but if you do want to get started uh
[2650] there is an experience for you for free.
[2652] Uh go to uh stardog.com/cloud
[2656] and you will see that journey for you uh
[2658] through a free endpoint. you can
[2660] experience the same demonstration that I
[2662] just gave you uh within that free
[2664] endpoint um across multiple
[2668] uh industries and then of course uh
[2670] whenever you're ready for us to engage
[2672] with you just give us a call um or reach
[2674] out uh and connect um and just on that
[2677] topic of getting started um this is
[2680] where you kind of go and we have these
[2682] industry knowledge packs
[2684] uh with various industry models that you
[2687] can utilize to kind of experience um
[2690] some of this uh based on the specific
[2692] industry that you have.
[2695] All right, I think uh that is the end of
[2699] the session. I will see if there are
[2702] more questions that got generated. Uh in
[2705] the meantime,
[2708] uh I see that there was
[2711] are you using embeddings for semantic
[2713] search? We are as a part of semantic
[2715] search. we are um using it to identify
[2718] the key parts of the ontology. So the
[2719] semantic search is against the question
[2722] interpretation against the specific
[2724] ontological concepts in the the data
[2727] model itself and that's all wired and
[2730] built and integrated within the product.
[2732] Um
[2734] we should be announcing a a gift as well
[2736] if I'm not mistaken.
[2739] Uh
[2744] the winner is yes, Cindy from Cityroup.
[2747] Thank you, Jazz. Uh it's a $100 Amazon
[2750] gift card on your on its way to you,
[2752] Cindy. Uh we appreciate you attending
[2754] and we do appreciate everyone attending
[2756] the session. I will take a few more
[2758] minutes to answer questions if you want
[2760] to hang around here for a little bit.
[2764] Um
[2766] and we see if there's anything I missed.
[2769] Have you encountered misinformation
[2772] risk in your implementations? None. None
[2774] so far. Vijay, again the idea here is to
[2777] eliminate hallucinations by grounding
[2779] everything against the ontology. So when
[2781] I ask the question, show me the uh side
[2783] effects. It it does not have that
[2785] information and hence it will not give
[2786] you an answer rel versus a large
[2789] language model by design is is expected
[2791] to give you an answer always and
[2793] sometimes in ways that sounds very
[2795] authoritative when it's clearly not.
[2798] Um
[2800] what kind of star LLM's uh so we look we
[2803] we continuously fine-tune uh uh large
[2807] language models we leverage open source
[2810] um we've leveraged open llama 31 and we
[2813] continue to look at others out there in
[2814] the industry um and and
[2818] continue to evaluate on your behalf the
[2821] best model to generate the best accurate
[2824] responses
[2825] um what ontology do you have for
[2828] healthcare? Again, I shared an example
[2830] of that. Um, if you check out our um
[2834] startup.cloud free endpoint, you'll see
[2836] access to some of those models for
[2838] healthcare as well. And that can be
[2841] explored in your sandbox.
[2843] Um,
[2845] the startup provide functionality with
[2846] vector DB. Like I said, we do have an
[2848] embedded vector DB or vector search
[2851] approach um as part of the initial
[2855] identification of specific ontology
[2857] concepts to your questions.
[2859] Um
[2861] let's see what else uh is Stardog
[2864] product. Uh if one has RDF ontology
[2866] model, yes, you guys can use an existing
[2870] ontology model from an RDF construct and
[2873] bring that into Stardog. Stardog is
[2875] itself a RDFbased system um and and it's
[2880] our own proprietary developed um
[2883] standardsbased uh graph technology based
[2885] on RDF.
[2887] Um are you using single or multiple
[2889] ontologies? I think I spoke about that
[2891] earlier. So I think I'm caught up on the
[2892] question and answering. Um again if I
[2895] missed answering any questions
[2897] um do we work with DoD or other cleared
[2900] environments? Absolutely we do. uh
[2903] please reach out to us uh and we can
[2905] share with you a lot more details about
[2907] our footprint in the DoD space. Um again
[2912] thank you very much. Is your health
[2914] related demo on your startup website? It
[2916] absolutely is
[2918] uh data fabric data mesh which is good
[2920] in data virtualization.
[2923] Um honestly data mesh more so than data
[2927] fabric but both have fundamentally
[2929] benefits of utilizing the the power of
[2931] virtualization. So uh again thank you
[2935] for your uh attention and I will let you
[2938] guys be on your way and go about your
[2941] day and and appreciate everyone
[2942] listening and attending uh intently. So
[2945] thank you again.
