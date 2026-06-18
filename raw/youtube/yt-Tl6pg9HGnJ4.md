---
schema_version: 1
id: yt-Tl6pg9HGnJ4
type: youtube
title: 'Demo Day: LLM-Powered Stardog Voicebox and Knowledge Graphs'
url: https://www.youtube.com/watch?v=Tl6pg9HGnJ4
authors:
- Stardog
ingested_at: '2026-06-17T20:57:36Z'
content_hash: sha256:93d149cc0ad364ac8529bcf4527c1421cf15cbd98ddf83be6295515f69b36f89
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Stardog
  channel_url: https://www.youtube.com/@stardog-union
  duration_seconds: 2035
  caption_track: fetched
  snippet_count: 972
filter:
  score: 0.72
---
[0] Um
[2] Hi, and welcome to Stardog Demo Day.
[5] Uh today we're talking about LLM-powered
[8] Stardog Voice Box and our enterprise
[9] knowledge graph offering. Uh we run demo
[12] days so that you can see inside our
[13] platform, learn about new features, and
[15] ask questions.
[17] I'm Mandy Sedlak, I'm the VP of
[19] Marketing at Stardog.
[20] Um you know, as generative AI and large
[22] language models gain more mainstream
[24] traction, we've been fielding a lot of
[26] questions from customers and companies
[27] that we talk to about how Stardog uses
[30] AI and how AI uses Stardog.
[33] Um we have Mike Grove joining us today.
[35] Um Mike's a Stardog founder and LLM
[38] architect, and and he'll discuss the
[40] combined power of LLMs and knowledge
[42] graphs. Uh before I hand it over to
[44] Mike, I'm going to run quickly through a
[45] few slides, and I promise to be fast we
[48] can get to the good stuff, which is the
[49] live demos.
[50] Today, we're going to cover
[53] um what is a knowledge graph, why
[55] knowledge graphs and large language
[56] models and AI are better together. We'll
[59] introduce and demo uh Stardog Voice Box,
[62] as well as tell you about our Voice Box
[63] early access program, and we'll leave
[65] time at the end for question and answer.
[68] Really quick, just a reminder, please
[69] use the Q&A queue rather than chat.
[71] It'll be difficult to answer the
[73] questions in chat, put them in the
[74] question and answer queue and we'll get
[75] to as many as we can.
[78] All right. Um so, Stardog provides
[81] organizations with an enterprise
[83] knowledge graph.
[84] Um if you don't know what that is, it's
[86] a flexible semantic data layer that
[88] helps answer complex queries across data
[91] silos.
[92] So, by bringing your data together based
[94] on business meaning rather than where
[96] it's stored, more people in your
[97] organization get access to the answers
[99] they need
[100] when they need them.
[102] So, that's a really high-level overview.
[103] If you're already familiar with Stardog,
[104] you know that. Um
[108] if not, we can go deeper and there's
[109] plenty of other demo days that we um
[111] really dive deep into enterprise
[113] knowledge graphs.
[114] Um also, on the next slide, we just have
[116] a quick level set for everybody. Anybody
[118] who's new, we're going to talk today
[120] about LLMs and GenAI. Um give these
[123] definitions a read if if you need to as
[126] they are separate but related terms.
[128] Um and by the way, organizations are
[130] using these technologies. I just saw a
[133] recent article in VentureBeat where more
[134] than half of organizations, it was 54
[137] 55%, are experimenting with generative
[140] artificial intelligence. And um almost
[144] 20% are already implementing it in their
[146] operations. So, this isn't something
[148] that's far out in the future. Uh the
[151] wave will come at some point. It's here
[153] and I assume I'm guessing that a lot of
[154] you know that and that's why you're here
[156] today as well.
[158] All right. Um finally, just let's talk
[161] about knowledge graphs. You know, that
[163] that flexible semantic data layer. And
[165] LLMs go really well together. The old
[168] relational data structures of the past
[170] are outdated in the AI era. Um in fact,
[173] in a recent report, which is what this
[175] is quoted for is from, Gartner calls out
[177] how users expect answers to questions.
[180] So, LLMs and knowledge graphs together
[181] can help enterprises who have users in
[184] your organization that need answers to
[185] questions meet that demand.
[188] All right. I know I flew flew through
[190] that. That was fast. Um Mike, over to
[193] you
[194] to uh talk further about this and show
[196] some demos of Voicebox.
[198] Cool. Well, thank you Mandy for the
[201] intro uh both for me and uh about
[204] StarDog the platform. Uh
[206] as Mandy said, I'm Mike. I'm one of the
[207] founders here and the original architect
[209] of our platform. And I'm very excited to
[211] talk to everyone today about StarDog
[213] Voicebox. Uh it's my first chance to
[215] talk about it live. Um
[217] So,
[218] you know, Mandy talked a little bit
[219] about our platform. The The idea for our
[221] platform has always been to provide a
[225] capability for enterprises to create a
[227] comprehensive data layer. A lot of the
[228] challenges that enterprises face
[231] ultimately come down to data problems,
[233] not having accurate, timely data that
[236] they can base business decisions on.
[239] And generative AI is no different. It
[241] needs good data, too. But there are two
[244] particular challenges that generative AI
[246] introduces to the enterprise that
[249] have deeply affected our
[251] design for Voicebox and how we built it,
[254] how we think about it. So, I wanted to
[255] just mention those briefly.
[258] Then we will jump into a demo. We don't
[260] want to
[261] from that too long cuz that's that's the
[262] fun part. That's why everyone's here,
[263] I'm sure, to see Voicebox. But the two
[266] things that have greatly
[268] kind of affected how we think about
[269] Voicebox are
[271] the challenges that LLMs, these models,
[272] they're finite. They're trained and then
[274] there's no new information.
[276] You can't base business decisions that
[278] are critical on out-of-date information.
[281] Similarly,
[283] models can generate statistically
[285] probable,
[286] valid, often sensible, but incorrect
[289] answers. And the term for this is
[291] hallucination.
[293] These two unique challenges that
[294] generative AI presents will be stumbling
[297] blocks for the organizations as they try
[300] and introduce this technology into their
[302] enterprise. That's something that we've
[304] taken to heart in building Voicebox. So,
[307] what Voicebox is isn't necessarily a new
[310] LLM. We're not encoding your data in the
[314] language model, actually. Voicebox is a
[317] user of Start.
[319] So, our using these generative AI
[321] technology is to
[324] in a way, digitize me.
[327] Digitize all of Start, all the technical
[328] folks, all that expertise about how to
[330] create knowledge graphs, and that's what
[332] we're digitizing. That's what we're
[333] building into Voicebox. Voicebox is a
[335] user of the Start platform, just like I
[337] am, just like many of you maybe
[340] hopefully will be soon for those who
[343] those of you who are not. But that's the
[345] idea of Voicebox. It's not creating the
[347] answers. The answers are not coming from
[349] voicebox. The source of truth is your
[351] knowledge graph.
[353] So, your data is always up-to-date. It's
[355] always accurate. It's always complete
[356] because your knowledge graph has breadth
[359] of the entire enterprise can access all
[361] of its data. Similarly, it can't
[363] hallucinate. Voicebox is using that
[365] information that's coming from the
[366] knowledge graph, that source of truth.
[368] It's not making things up. So, it can uh
[372] directly confront these two challenges
[373] that generative AI um throws in front of
[376] us. So,
[378] that's kind of
[379] part of our guiding principles for
[380] voicebox. We'll talk more about how it
[382] works
[383] um and see some more demos, but I'm
[384] going to jump into our first look at
[387] voicebox.
[388] So, the first thing I'm going to do
[391] is jump over to Stardog Studio.
[396] Uh Stardog Studio is our environment,
[399] called our IDE, for the knowledge graph,
[401] for building knowledge graphs.
[403] So, one of the key
[405] um
[405] abilities of voicebox is to create
[408] queries. It's got to use that knowledge
[409] graph. So, primary way to use the
[411] knowledge graph is to get to is to write
[413] a query.
[415] So, my use case here is a customer 360
[417] kind of scenario. Uh this data is
[419] actually available on cloud right now.
[421] It's the training 360 kit, so you can go
[423] play with it if you wanted to take a
[424] look. Um and you see I asked a question,
[427] "How many customers have purchased
[428] orders for more than a thousand dollars
[430] and the product purchased was in the
[431] electronics department?" So, I got my
[434] answer. It was six.
[435] Um six isn't the most helpful.
[439] Uh it's just a number. So, I can work
[441] with voicebox and it can be my co-pilot.
[443] Again, it knows how to use Stardog. So,
[446] return
[448] only names and emails. So, I'm going to
[451] have it go ahead and evolve this query
[452] for me as my understanding of my
[454] requirements change and progress. So,
[456] you can see rather than getting six,
[459] the answer, but not necessarily helpful,
[461] I can get names and emails cuz maybe
[463] the these are obviously big spenders.
[466] Uh so maybe I want to send them a a
[467] thank you for spending over a thousand
[469] dollars on something that they bought at
[472] my company.
[473] Maybe I want to know what they bought at
[475] the company so I can go ahead and
[477] continue to work with Voicebox, continue
[478] to have it amend this query for me.
[482] Um so I can
[484] go ahead and ask it for that.
[489] And
[490] you probably see here the query's
[491] getting rewritten in the background. So
[492] Voicebox go ahead and writing that for
[494] me. I can see now that I've got the
[496] products that were purchased by each of
[498] those people. Um and maybe there's a
[500] particular set of products
[502] maybe I've got a new TV coming out and I
[504] want to send not only a thank you but a
[506] coupon for people buy another TV. Uh who
[509] doesn't need more TVs? So once again, I
[511] can work with Voicebox. I can further
[514] refine my request. It'll amend that
[516] query, give me precisely what I need. So
[518] I get down to the exact result set that
[520] I was looking for. The three people who
[522] bought TVs in the electronics department
[524] for more than ten thousand dollars.
[526] I didn't have to write any code. There
[527] was no
[528] expertise. I didn't even really have to
[529] know how the data was laid out in the
[531] knowledge graph. Voicebox takes care of
[533] all of that for me. These are things I
[535] would have done before.
[536] Uh manually look at the knowledge graph,
[538] understand the schema, try and figure it
[540] out, see where the data
[542] all handled by Voicebox. I can just ask
[544] what I need. If I didn't get it right
[545] the first time, I can continue to work
[547] with Voicebox in this kind of co-pilot
[549] manner, have it build exactly the right
[551] query for me to get the right data out
[553] of the knowledge graph.
[555] And back to what I was saying about, you
[556] know, this information is not coming
[557] from Voicebox. It's coming from the
[558] knowledge graph. Voicebox generated the
[560] query, not the answer. And I can see how
[563] did Voicebox come up with this answer?
[565] What's in it? It came up with the query.
[566] I can see exactly where this data came
[568] from all the way down to what tables it
[570] was read out of in the knowledge graph.
[573] So it's very exciting from an explain
[575] explainability point of view.
[577] So that's our first look at Voicebox,
[579] we'll be jumping back into Voicebox at a
[581] couple different points today.
[583] Um but I do want to jump back over to
[584] our slides and talk a bit more
[587] about Voicebox.
[588] So, how in the world did we build this
[590] thing in the first place?
[592] So, this is a kind of a very high-level
[594] architecture. So, a bit more
[595] mar-chitecture than architecture.
[598] Um but you can see here very clearly the
[599] knowledge graph called out as a key
[601] component. That's the source of truth.
[603] That's where all the information that
[604] actually comes from that you're working
[606] with.
[606] That Voicebox has access to. It's coming
[608] out of your knowledge graph. Not coming
[610] from Voicebox.
[611] There's a vector database. This This
[613] should look a lot like um
[616] I don't want to say the traditional, but
[617] the popularized LLM stack that
[619] Andreessen Horowitz has introduced. But
[622] they missed the critical key component
[624] piece of the knowledge graph.
[626] But it's vector database in there.
[627] That's the short and long-term working
[629] memory. Uh there's additional indexes
[631] that we keep in there that are
[633] beneficial to Voicebox for handling each
[635] of the different tasks. Um and that's
[638] actually another key uh
[640] thing to call out about Voicebox is that
[642] it's not a single LLM, a single thing.
[645] It's It's kind of an ensemble approach.
[647] Uh even a singular task like creating a
[650] query, which we just saw, has a couple
[652] different steps that go on. We don't
[654] want to send users incorrect queries. We
[655] don't want to send them out form
[657] queries.
[658] So, there's different linting and
[659] debugging steps that go on that use
[661] different models that have different um
[664] expertises or skill sets that we combine
[667] in various ways to produce the final
[669] product, which is the question the query
[671] to answer the question that you asked.
[676] So, now I'm going to jump back into our
[678] demo. We're going to try and stay up in
[679] the tools as much as we can. We're going
[681] to shift focus now though from studio.
[683] We're going to go into designer.
[685] Designer is our tool for creating
[687] knowledge graphs. So, we're going to
[689] show how Voicebox can be used to
[691] accelerate that process.
[693] So, we can see here I've got a designer
[695] project. I've got a couple data sources
[697] here at the bottom. These were all CSV
[700] files, um just cuz that was easier for
[702] me. Uh but I you can go ahead and use
[704] any enterprise data source, um which we
[707] we can show another time.
[709] And anything that StarDog supports, uh
[712] Voicebox can use. So, you can see here
[714] in my prompt, I tried to describe the
[716] use case we were actually just looking
[717] at. So,
[718] that use case in Studio I'm trying to
[720] recreate it here in Designer.
[722] I can tell you it took days to create
[725] that original data set. We're going to
[728] recreate it here in a matter of minutes.
[729] So, you can see my prompt where I'm
[731] describing my domain very clearly, very
[734] simply, plain English. Uh
[736] goes back to Voicebox. Voicebox kind of
[738] summarizes what it did. The ontology
[740] defines class
[741] tells me everything that I asked for, so
[743] I can go ahead and say, "Yeah, go ahead
[744] and add that to my canvas." We can see
[746] here this is my data model that it
[748] created. So, this is another one of
[749] Voicebox's services, model creation.
[752] Created a data model for me. I didn't
[754] have to do anything but describe my use
[756] case.
[758] There were some part of this I didn't
[759] like, I could change make changes, but
[761] this looks pretty good to me. It's
[762] exactly what I described, and I can go
[764] ahead and now use the Voicebox
[766] suggestion service to map all of this
[768] data.
[769] I'm going to sort by source.
[772] So, US customers, that's my customer
[774] information, and all of this will get
[776] automatically mapped for me. So, you get
[779] a confidence it was
[781] said for the label use the first name.
[783] Um that's not bad, um
[784] but I wasn't sure about it, so we can
[786] say no and actually use the full name.
[788] Uh but everyone else it looked like it
[790] got the answer, so I can just go ahead
[792] and accept those all. And I now I can
[794] just go source by source. So, we've got
[796] the product catalog. I'll go ahead and
[798] add a mapping there
[800] to all the product information.
[802] So, we can see again Voicebox suggests
[804] helps do most of the work for me, and I
[807] can see these last few things. I can
[810] just go ahead and Oops. Excuse me.
[813] Select that one and make that
[816] connection. Now, that's fully mapped.
[818] So, we're
[819] doing each of these things. It's only
[821] taking a moment
[823] to map these individual sources because
[825] I'm not actually having to do anything.
[826] I'm more or less just supervising what
[830] um
[831] Voicebox has done.
[834] And I'll now I'm mapping purchases.
[837] Products. So, we can see I'm able to do
[840] both relationships from one concept to
[842] another.
[843] So, this is product to uh
[846] a purchase and purchase back to a
[847] product uh from purchases to the
[849] customers that made them.
[852] And then all of the traditional kind of
[854] attributes that I've got.
[855] Go ahead.
[857] Of course, Zoom is in the way.
[859] That I don't
[861] I've mapped everything.
[863] Well, I guess I I've got this one more
[864] source we can do.
[866] Let's go ahead and do that very quickly.
[868] Product category.
[871] All right, that's great. And now I've
[872] mapped everything.
[874] I'm going to go ahead and publish.
[876] Apparently, I have a
[879] incomplete mapping.
[881] Of course, no live demo is You have
[883] rewards to your left there, Mike. What
[885] without a a mess up? Yeah, I didn't need
[887] that one.
[888] Um
[890] Oh.
[892] I forgot that last little bit.
[895] And then I'll just use all the defaults
[897] here and I'm going to go ahead and just
[899] create a new database, new knowledge
[900] graph for me for this source. And
[903] otherwise, accept all the defaults here.
[906] And now I've got a new knowledge graph.
[907] Just going to go ahead and publish that
[909] to my server and then I will jump over
[912] now to
[914] start our cloud and then we're going to
[915] go into Explorer so you can see Explorer
[917] quickly. Voicebox has not yet been
[919] integrated into Explorer, but that's
[922] coming soon. We'll be very excited about
[924] it, but it can take advantage of
[927] uh
[928] the capabilities of Voicebox by it's
[930] very easy to create a knowledge graph
[931] now. So, we can see we visualize, we can
[933] see that schema. This is created for us
[935] by Voicebox. We can go in and now see
[938] for any any of these things I can just
[940] pick out some
[942] in partic- some particular person in the
[944] knowledge graph and then just start
[945] exploring.
[947] And there's all this new data. This is
[948] all created with the help of Voicebox
[950] without me having to write any code or
[952] do anything in particular. I didn't need
[953] any special skill sets to do this. Uh I
[956] was able to do this very quickly and
[957] easily based on a simple description of
[960] my data.
[962] So, that's a very quick tour of Voicebox
[965] integrated in Designer.
[966] Um so, let me permit jumping back to the
[969] slides quickly here.
[975] We'll find them.
[978] Go.
[981] So, why did we integrate Voicebox with
[983] Designer? Well, we want to help people
[985] get started with Stardog more quickly.
[988] Reasonable business goal for us. Um but
[991] getting started with Stardog more
[992] quickly, building your knowledge graph
[993] more quickly is something that's very
[995] impactful for an organization.
[997] You get to take advantage of the network
[999] effect that comes from connecting more
[1001] data. The more sources of information
[1004] you connect, the more types of questions
[1006] you can
[1007] ask about that data, more variety,
[1010] more sophisticated questions, having
[1012] more facets that you can ask about in
[1014] these questions.
[1016] And organizations
[1018] benefit greatly from being able to
[1019] create knowledge graphs more quickly.
[1022] There's a 3x
[1024] increase in development time,
[1026] corresponding decrease in development
[1028] costs that Forrester saw when they did
[1030] their total economic
[1032] impact report about knowledge graphs.
[1034] So,
[1035] what we've done with Voicebox is just
[1037] make it even for people to get started.
[1039] They can get to taking advantage of
[1041] those cost savings, those time savings,
[1043] all the joys and benefits the knowledge
[1045] graph provides a more quickly, provide
[1047] more value to their organization faster.
[1053] Now, I want to
[1054] show one more demo.
[1056] But before we jump into the demo, I want
[1058] to talk a bit about the knowledge
[1060] catalog. The next demo centers around
[1063] Voicebox using the knowledge catalog,
[1065] something another new capability of the
[1067] platform we introduced this year that
[1069] I'm very excited about.
[1071] What's the knowledge catalog?
[1073] The knowledge catalog is an automated
[1076] uh
[1077] basically knowledge graph. We will reach
[1078] out to all of your catalogs and ingest
[1081] all of that data. All of the sources
[1082] that you connect to your knowledge graph
[1084] manually, all of that metadata will also
[1086] be pulled into the knowledge catalog.
[1088] It's unified under a single meta model.
[1091] So, you have a single way to see all of
[1093] your data's all of your organization's
[1095] metadata. All the tables and columns,
[1097] every everywhere that the organization
[1099] has put data across all of the different
[1101] catalogs that your organization uses.
[1104] It's bidirectionally synced.
[1106] So, the glossaries that you create in
[1108] Collibra will show up in StarDog.
[1111] You can take them, you could create a
[1112] data model out of them, you could push
[1113] them back to Collibra so the rest of the
[1114] organization can benefit.
[1117] This knowledge catalog, it's just a
[1118] special knowledge graph. And this
[1120] universal meta model we've taught
[1122] Voicebox how to use. So, Voicebox can
[1124] use the knowledge catalog just again,
[1126] like you or I would use it. So, let's
[1128] take a look at how that happens.
[1134] I'm going to go back over to studio.
[1140] Open up
[1142] new tab.
[1145] Instead of our training data, we're
[1147] going to connect to our knowledge
[1148] catalog.
[1151] Zoom.
[1153] And common question people say is
[1156] what data do we have in this database?
[1158] What's in here?
[1160] So, typically that's go to your data
[1163] catalog and hopefully it's in that
[1164] catalog and you look it up and now maybe
[1166] there's another catalog you can go look
[1167] it up in. Um
[1169] that's kind of passive metadata. This is
[1172] how you activate metadata. Voicebox is a
[1174] user of the Stardog knowledge catalog
[1176] and can answer those questions for you.
[1178] So, I'm going to ask Voicebox, what's in
[1180] this database C360 source?
[1184] There's there's theme theme here around
[1185] customer 360. Uh so, what Voicebox is
[1188] doing is using this knowledge catalog to
[1190] generate a query that will help me
[1193] answer this question. So, it's going to
[1195] use that metamodel. It's going to query
[1197] the catalog and say, "Hey, Mike, there's
[1199] credit card information in that
[1201] database."
[1202] So, this is really useful and this is
[1204] the live view. So, I'm querying my
[1205] knowledge graph, Voicebox is querying
[1207] the knowledge graph, querying knowledge
[1208] catalog, which is the knowledge graph
[1210] about the knowledge graph.
[1212] So, I can see this live up-to-date data
[1214] about how my knowledge graph has been
[1216] constructed. Oh, there's credit card
[1218] data in there.
[1220] Maybe that's going to help me take a
[1221] next step now understanding what
[1223] information I have available.
[1226] Another common question
[1228] is where is my data? Where where is my
[1231] customer data? Where is
[1233] you know, my patient data? Where is
[1235] whatever?
[1236] So, let's ask Voicebox and see if it can
[1239] help us answer that question too.
[1241] I'll open up a a new session with
[1243] Voicebox and I'm going to go ahead and
[1244] say, "What table contains the concept
[1246] credit card?" I'm going to give a little
[1248] extra prompting here. Uh
[1250] it's a tough query for Voicebox to come
[1253] up with. This is like
[1256] I said before, the collective expertise
[1257] of Stardog's technical uh
[1259] cadre of folks to create this query,
[1262] train
[1264] Voicebox how to create it. There's
[1266] credit card information that we found in
[1268] these two sources. So, these are two
[1270] tables in that Databricks data source
[1273] that we pinpointed say exactly that's
[1275] where those tables, that's where that
[1277] credit card information is.
[1279] The really amazing thing about this is
[1280] this query in the knowledge catalog and
[1282] then it queries every knowledge graph
[1283] that it has available on this endpoint
[1285] to find exactly what it's looking for.
[1288] It's a very sophisticated query that
[1289] Voicebox is able to do. It took days for
[1291] me to be able to figure this out.
[1293] Voicebox can do it now for everyone
[1295] immediately. Another great example of
[1297] how Voicebox can help kind of
[1299] supercharge
[1301] knowledge graph efforts at your
[1302] enterprise.
[1304] And then I can see where we're coming up
[1307] close to the Q&A session. I want to
[1310] just take like another minute to show
[1313] just a couple different queries, couple
[1316] um examples of
[1318] uh
[1318] Voicebox generating queries and getting
[1321] answers for me um just using a different
[1324] data set here. It's just
[1326] wasn't all hard coded. It's a couple
[1328] different cases. Um I'm going to pick a
[1330] different data set. This is the Carnegie
[1332] Hall Data Lab. It's open source data.
[1335] Um so, I picked this. Anyone know know
[1338] SPARQL, one thing you maybe notice is
[1341] pretty uniform these queries. There's
[1343] only
[1344] one data model here. There's only one
[1345] scheme that's used.
[1348] Open data sets are uh
[1350] not that nice.
[1352] So, they present an interesting
[1353] challenge for Voicebox having to deal
[1356] with the fact these vocabularies that
[1358] open source knowledge graphs and open
[1360] source data sets tend to use um So, it
[1362] says "Performers born in Vienna that
[1364] have played works by Schubert."
[1366] Uh so, we can see there's 29 uh
[1369] Voicebox was able to come up with that
[1370] quickly and easily. You can see there's
[1372] a number of different vocabularies used.
[1374] Uh it's even using Stardog's text max
[1377] text match functionality. So, it's using
[1380] fuzzy matching. I could have misspelled
[1382] Vienna or Schubert.
[1384] Humans do this all the time.
[1386] Um
[1387] so this is another example of Voice
[1388] boxes using StarDog. It's taking
[1390] advantage of the features of the
[1391] platform to help me get the answer to my
[1394] question. And this is a really cool
[1396] example of how Voice box can do that
[1399] dealing with a very varied data set and
[1401] using advanced capabilities like the
[1403] text match service to find the right
[1406] answer.
[1408] And then I think
[1410] with that I do want to jump over to QA
[1412] now um cuz I
[1415] can see there's a lot of stuff in the
[1416] queue. Uh I want to make sure we have
[1418] time to jump to uh as much of it as we
[1420] can. So maybe let's get back out to
[1423] slides to provide a backdrop here.
[1435] So uh
[1436] Mandy you know what
[1437] Hey what? Yeah. I'll I'll uh
[1439] I'll talk to this. You can take a look
[1441] at the QA real quick, Mike. Um
[1444] if anyone's interested in trying Voice
[1446] box themselves, we have an early access
[1448] program coming soon. Um we're going to
[1450] wait right now because the pro- program
[1453] is not yet live, but it will be very
[1454] shortly. If you're interested in that,
[1456] you can register for it. There's the
[1458] link here. We're also going to send this
[1460] link in the follow-up email. You will
[1462] have this um sent to you. You don't
[1465] really have to go hunting for it or
[1466] write it down on the screen right now.
[1468] Uh but there's an early access program.
[1470] So if you're interested, please uh sign
[1472] up and you can be among the first to try
[1474] out Voice box uh and give us feedback on
[1477] Voice box.
[1478] Um with that, I think we should go ahead
[1481] and and take questions. Uh just a
[1483] reminder to put them in the Q&A. I know
[1485] there were some in the chat. I think I
[1487] answered a couple of them there that
[1488] were um relatively simple, but the ones
[1491] that are more for Mike, um please let's
[1493] get them over to Q&A. And Mike, I'll let
[1495] you go ahead if you see a couple you
[1497] want to start with.
[1499] Sure. Um,
[1501] but yeah, there's a a lot here. Uh,
[1504] I don't know if we'll get to all of
[1504] them, but we will do our best. Uh, so
[1506] the first one is, "Voice box need to be
[1508] provided with any information about the
[1510] knowledge graph other than the knowledge
[1512] graph itself?"
[1514] Uh, no. Uh, that we have worked hard to
[1516] make it be that way. Uh, but Voice box
[1519] will do all of the discovery activities
[1521] that it needs to to be able to use the
[1523] knowledge graph. So, you just have to
[1524] say, "That's my knowledge graph over
[1526] there, Voice box. This is my question."
[1529] It will introspect the schema. It will
[1531] figure out how where the data is, what
[1533] it looks like, how to write the query.
[1535] So, you just need to give it a name and
[1537] what you need to know.
[1539] Um, so that
[1541] similar question.
[1544] Um,
[1545] Danny said this is very useful. How
[1546] sensitive is it to the class and
[1548] property names being clear?
[1551] Uh,
[1552] there is some sensitivity. So, if you
[1554] look at some of these public data sets
[1556] like WikiData that use effectively
[1559] nonsensical names,
[1561] you can't rely on simply the the
[1563] structure of the schema. So, this is
[1564] another thing that we've been working
[1566] on, how do you selectively grab
[1569] information out of the knowledge graph
[1570] to supplement the description of your
[1573] knowledge graph
[1575] for these cases where the data model is
[1577] is inscrutable. That typically isn't the
[1580] case in most of our customers, big
[1582] enterprises they're creating their
[1583] models from scratch in Designer. The
[1585] names are clear, the labels are clear,
[1588] and they're easily used by Designer.
[1589] But,
[1591] public data sets can be the wild west.
[1595] All right. So, moving on.
[1604] Considering that knowledge graphs are
[1606] built iteratively, they don't
[1608] immediately have answers to all the
[1609] questions. If this user doesn't know if
[1612] the answer is available, How will
[1613] Voicebox react to the user when it
[1615] doesn't know the answer?
[1618] It's a great question. I don't know that
[1619] I have a great answer for it, but I want
[1622] to attempt because it's really related
[1624] to kind of where we left off in the demo
[1627] and that knowledge catalog.
[1630] So yeah, and maybe you ask a question
[1631] and Voicebox generates a query and there
[1633] there are no results.
[1635] But Voicebox, I mean I showed this in
[1637] the first demo. Voicebox can work with
[1639] you. So maybe you work with it
[1641] iteratively and you refine the query and
[1643] you get down to something that does
[1644] return results. Or Voicebox can use that
[1647] knowledge catalog and say, "Hey, well
[1649] you know, it looked like you were asking
[1650] me about customer information. This
[1652] doesn't return any queries, but I can
[1653] see there's 17 data sources in your
[1655] organization that have customer
[1657] information. Maybe we should consider
[1659] some of those." So
[1660] maybe you should just have changed the
[1661] knowledge graph. So these these are
[1663] things that we're thinking about and
[1664] working on adding these capabilities to
[1666] Voicebox as development continues.
[1670] But I think that's a a key way to
[1671] activate the metadata. And this Voicebox
[1673] has a very nice role in the story of how
[1676] organizations actively
[1678] activate their metadata.
[1681] Okay.
[1690] Your question, does one have to use the
[1692] same terminology as in the KG?
[1695] For example, I'm using the term name
[1697] where
[1698] the property was name.
[1700] What if it was using some other
[1702] property?
[1703] Uh yes, so the No, you don't. The short
[1706] answer is no, you don't. Um so we call
[1707] this schema summarizations. I guess kind
[1710] of related to the
[1711] first two questions. We This is one of
[1714] the first things we did with Voicebox
[1715] was figure out how to communicate a
[1717] schema, including weird things about IDs
[1720] and non-standard ways people represent
[1723] bits of information so that Voicebox
[1725] can, again, do all the same things that
[1727] I do when I look at a new data set and
[1730] be able to get a lay of the land so it
[1731] knows how to write query just like I
[1732] would.
[1741] Will the knowledge catalog integrate
[1742] with the Informatica data catalog as
[1744] well? Not currently but that is on the
[1746] road map.
[1751] Can Voicebox create a data schema
[1753] consistent with BFO? No,
[1757] probably not.
[1758] BFO is not something that we've
[1759] considered. We don't use it for our
[1761] training data.
[1763] There's not a lot of information in the
[1765] public models about BFO. I don't think
[1767] we'd be able to do that.
[1770] Um
[1772] Is Voicebox using an LLM to generate the
[1774] SPARQL queries? Yes,
[1776] multiple but yes as I said it's an
[1779] ensemble approach. That kind of the
[1781] primary thing that I showed today was
[1783] Voicebox generating queries,
[1786] Voicebox generating a data model and
[1788] then Voicebox generating mappings to
[1790] connect the data model to the data.
[1793] And then I can use it to to run the make
[1796] queries that I can run and get answers.
[1799] And Mike, I'm I'm going to answer a
[1800] couple questions about the early access
[1801] program while you're looking at at the
[1803] questions. Yeah, great. A couple of
[1805] people have put questions in there about
[1806] the early access program. So it doesn't
[1808] cost to enter the program. No, there's
[1810] no cost to enter the program. You to be
[1813] part of the program you do need to be a
[1814] Stardog Cloud user or sign up for
[1816] Stardog Cloud. It's not a pre-req but it
[1819] one of the things in the process would
[1820] be to to create a Stardog Cloud account
[1822] so that you can try it.
[1824] Another person who signed up early,
[1825] thank you,
[1827] asked about the timing there.
[1829] We plan to get it out shortly. We're
[1831] we're working through it. We want to
[1832] make sure what we get out to you is
[1834] um
[1836] has all the proper documentation and
[1838] everything and it's run the right way.
[1839] So bear with us while we're getting
[1841] everything together to do it properly.
[1845] I think those are the only That That
[1847] summarizes a few of the questions on
[1848] early access. So, back to you.
[1850] I know we're at time, but there's one or
[1853] two questions maybe we can get to before
[1855] we let everyone go back to their days.
[1857] Um
[1859] The first question would Would Box work
[1861] if data was virtualized in Snowflake?
[1863] And then I guess also related, uh would
[1866] it work with unstructured files data
[1868] outside the knowledge graph?
[1870] Uh so data needs to be in the knowledge
[1872] graph?
[1873] That's number one, but the knowledge
[1875] graph StarDog can connect to both
[1877] Snowflake and unstructured
[1879] data. Um
[1881] And we can work with your NLP framework
[1883] of choice. We also have NLP stuff built
[1885] into the StarDog platform. So, Snowflake
[1888] and unstructured content can both be
[1889] brought into your knowledge graphs, and
[1891] then the answer is yes, VoiceBox will
[1892] absolutely work with either Snowflake or
[1895] unstructured data.
[1897] And then last here, can you briefly
[1900] expand on the knowledge catalog's role
[1902] answering a question like, "Where can I
[1904] find customer financial sales data for
[1906] last March?"
[1908] Is the expectation a person would create
[1910] the knowledge graph catalog or is raw
[1913] data parsed to generate the catalog? Uh
[1916] closer to the latter. So, we will
[1917] connect to your catalog. You just have
[1919] to tell us where they are and we will
[1920] pull in all the relevant data.
[1922] So, all of the information they have
[1924] about all the tables and columns, all
[1925] the different data sources, your
[1926] glossaries, all assets, asset types,
[1929] everything that's in Collibra and
[1931] Purview and Unity, Alation
[1934] slurped automatically into StarDog.
[1937] That's what's created this knowledge
[1938] catalog. We will overlay the metamodel
[1940] on top of it so you have a uniform
[1942] interface to all of that data. And then
[1945] at that point it's a knowledge graph
[1946] like any other, um just one that we've
[1948] specially trained VoiceBox to be able to
[1950] use. But it is this
[1953] automatic view of all of your metadata
[1956] within your organization. is a very
[1958] compelling way to start activating that
[1960] metadata, Voicebox or not.
[1971] Um
[1973] All right, and now Mike, you're getting
[1974] close. Any any others that you feel
[1976] compelled like, "Hey, let's make sure we
[1977] get this answered." I mean, there
[1979] there's an another 16 in the queue.
[1982] Uh-huh. Mhm. I think we could stay here
[1983] all afternoon. Um
[1986] So, maybe we'll have to take the rest of
[1988] them offline, but I'm too many good
[1990] questions by folks and
[1992] I think they just keep coming in. And
[1994] you know, we can create some some blogs
[1996] and other quick content on this. FAQs
[1997] from from this event might be excellent
[1999] for Voicebox. Mhm.
[2002] So, with that, I appreciate everyone
[2005] staying a little bit extra.
[2007] Uh I'm really excited to show everyone
[2008] Voicebox, get a chance to talk about the
[2009] knowledge catalog.
[2011] Um so, thank you for everyone's time
[2013] today. Look forward to more questions
[2016] and more time talking about Voicebox.
[2018] Absolutely. Thanks everybody for
[2020] following along. Expect an email from us
[2022] with today's recording, some additional
[2024] information, the link to that early
[2026] access program,
[2027] and don't hesitate to reach out to us
[2029] with further questions.
[2031] Have a nice day.
[2033] Bye.
