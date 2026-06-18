---
schema_version: 1
id: yt-t-GOSUnI2MI
type: youtube
title: 'LLMs + Knowledge Graphs: Enabling Trustworthy AI Agents'
url: https://www.youtube.com/watch?v=t-GOSUnI2MI
authors:
- Stardog
ingested_at: '2026-06-17T20:57:35Z'
content_hash: sha256:f85b12a2db20d2ebe8f6c2f8044c9e0e6f1d66a35d4e050afa63f7913e37f76c
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Stardog
  channel_url: https://www.youtube.com/@stardog-union
  duration_seconds: 2220
  caption_track: fetched
  snippet_count: 1086
filter:
  score: 0.7
---
[1] Hi everybody.
[2] Thank you for coming and taking time out
[3] of your mornings. Uh my name is Mike
[5] Grove.
[6] I'm one of the founders here at Stardog.
[8] Uh SVP engineering, other cool stuff in
[10] my title, uh but I guess founder is the
[12] one that matters the most. I'm really
[15] excited to be with everyone today to
[17] talk about trustworthy AI systems and
[20] what it takes to build them. Um
[22] surprise, surprise, it involves
[23] knowledge graphs.
[25] Uh I've been working in this space for
[27] 25 years. I got started in the late
[30] '90s. Uh I had the fortune of taking a
[32] class that exposed me to AI agents and
[36] what would eventually become called
[37] knowledge graphs. Uh I just needed
[39] credits. I did not know I was getting a
[40] career. Uh so I'm pretty excited to be
[43] here with you guys today to talk about
[45] some of those experiences,
[47] talk about Stardog, and talk about how
[50] we can use GenAI to build trustworthy AI
[53] solutions that solve problems in our
[54] enterprises.
[56] So, to a level set, let's do a quick
[58] agenda. Uh we're going to actually start
[59] off with a demo cuz
[61] demos are cool. People like seeing
[63] demos. That might be why a lot of people
[64] are joining us today to see something
[66] cool. Uh so we'll start off with that.
[68] Uh and then sadly we'll switch over to
[70] some slides. We'll go through some of
[72] the how and the what of what we saw, why
[74] knowledge graphs are particularly well
[76] fit for building these trustworthy AI
[78] systems. And then we're actually going
[80] to build one together. We're going to
[81] cap it off with another demo cuz again,
[84] demos are great. Uh we're going to build
[86] a knowledge graph together. It's not
[87] going to require code or programming or
[90] any technical skills whatsoever. We're
[92] going to push some buttons together. And
[93] we're going to make a knowledge graph.
[94] And then we're going to ask a pretty
[95] sophisticated question and uh get a
[98] pretty sophisticated answer. It's going
[99] to be very exciting.
[100] Uh I encourage people to ask questions
[102] along the way. Uh
[104] you can use the Zoom Q&A feature. I may
[107] break, depending on how many questions
[108] we have, in the middle, but we will
[110] certainly make sure there is time for
[112] questions at the end.
[115] Uh so, So further ado, uh let's jump
[117] over to a demo.
[119] I should get out of the slides here.
[122] And we're going to go right over to
[123] StarDog Designer, so we can see a
[126] knowledge graph kind of behind the
[127] scenes. So this is what this knowledge
[129] graph looks like. It's a tariff use case
[131] cuz
[132] tariffs are kind of relevant right now,
[133] so we can see our data model, also
[135] called an ontology,
[137] very popular thing people are talking a
[138] lot about. We'll talk more about
[140] ontologies later. We can see the
[142] different data sources that make up my
[143] knowledge graph. Data bricks, snowflake,
[145] postgres. This looks like something that
[147] exists in your enterprise.
[149] And I can jump right over to explorer. I
[151] can see that ontology, that data model
[154] front and center.
[156] And I can explore my knowledge graph
[157] this way, but for now we're going to
[159] look at Trustworthy AI through the lens
[161] of Voicebox.
[163] So we can see that same knowledge graph.
[165] Some of my colleagues have
[167] made some questions that were already
[169] relevant to me and my use case, so I'll
[170] go ahead and fire one of these off.
[172] Voicebox will quickly consider what
[174] information from that knowledge graph is
[176] relevant, go fetch it from the knowledge
[178] graph, and synthesize an answer. I get a
[180] short version of the answer here in the
[182] chat, and I get kind of a long-form
[184] version of the answer over here in the
[186] knowledge panel.
[187] Any text
[189] or any tables, excuse me, associated
[190] with the text are right here, easy for
[192] me to view and page through. Most
[194] importantly, front and center are the
[197] types of things that are involved in
[198] this answer here at the top, and the
[200] data sources involved, so I know where
[202] this data came from. Showing your work
[204] is a key component of Trustworthy AI.
[207] Then if I want to dig in
[209] and see how this came together, I can
[211] see the query that was issued in this
[212] case. One query was issued, and for
[215] those of us who are a little more
[216] technically minded, we can go ahead and
[217] even see the query code that was
[220] executed. We even have a nice little
[222] window where I can follow up what is my
[225] best option for non-US suppliers and
[229] what
[230] material am I have.
[234] So, it's further deep dive analysis on
[236] the answer itself.
[238] So, I don't have to context which I I
[240] don't have to go anywhere else. This is
[241] based on this exact data that was
[243] retrieved from the knowledge graph. So,
[245] very quick and easy for me to get an
[247] answer to my question.
[249] I'm going to jump over to one more
[251] example.
[252] Uh you see here is a different use case.
[255] This is a customer 360 e-commerce type
[258] scenario. This is a little more involved
[260] use case. So, the scenario here is I'm a
[263] I'm a product analyst or a business
[265] analyst, but I'm very much not a data
[267] scientist, but I need to perform some
[269] data science. I need to do some
[270] analytics on my data. So, we can ask
[272] Voicebox to go ahead and do that.
[279] Of course, I think I forgot to enable
[280] think mode.
[282] Oh, no, there it goes.
[283] Uh so, I can see what it's doing as it's
[286] doing it. So, I get full transparency
[288] into what Voicebox is doing. So, it's
[291] looking at my knowledge graph, trying to
[292] figure out what data it needs. It's
[294] issuing queries. This is data it's
[296] using.
[297] And now it's going to go ahead and write
[299] some code cuz it needs to do that
[300] analysis that I asked for.
[302] And remember, I can't write code. I'm
[303] not a data scientist.
[305] But, I'm going to let Voicebox do that
[306] for me, but I'm going to have the
[308] transparency and the traceability that
[309] Voicebox is going to show me the code
[311] that it wrote. So, I can understand
[314] what's going on. You can see some of the
[315] code just scrolled by here.
[317] Voicebox now is moving on to doing
[319] linear regression. So, it figured out
[320] what kind of statistical analysis to do
[322] on its own.
[324] And it can come up. It's compiling the
[325] final answer here, making its prediction
[328] for 2021.
[330] Uh and I should get a nice little answer
[331] here and a moment.
[333] Of course, this always takes longer when
[335] I am on live.
[337] Um uh you see my linear regression code
[339] just scrolled by. We'll get the nice
[340] overview.
[343] Here in a second. We'll just get that to
[345] redraw.
[347] So, we can see the analysis here.
[351] Get that prediction for 2021 and then
[353] again all those reasoning steps showing
[355] its work along the way, all the code
[357] that was written.
[359] That's transparency and traceability.
[361] This is what makes up these trustworthy
[362] AI systems. This is what you get for
[364] building on top of a knowledge graph.
[367] So let's go back over to our slides.
[371] And
[372] go ahead and talk about you
[375] As engineers and a lot of engineer my
[376] engineer friends are on today. Uh
[379] we're not building on trustworthy
[380] systems. We're not trying to at least,
[382] but I mean this is hard.
[384] Um I'm sure everyone here is using some
[386] sort of AI tools.
[388] Uh
[389] my engineering friends uh we're all
[390] probably using some sort of coding
[392] tools. They're all great.
[395] I don't trust them. You shouldn't trust
[396] them either. I eventually get to some
[398] very good code that I'm I'm confident
[400] in, uh but it takes a lot of my
[402] oversight because I don't trust that AI
[404] system. And these are as good as they
[407] get. These are hard systems to build.
[409] Hallucinations the thing that we talk
[411] about a lot, let's talk about a lot
[412] about in the world, uh obvious
[414] challenges to your business, brand
[416] damage, compliance risk of your chatbots
[418] going rogue. Uh but as engineers having
[421] a a system that almost works against us.
[423] It
[424] it could lie, it could confabulate, uh
[427] actively believe its own falsehoods,
[429] uh just
[431] start exhibiting different behaviors.
[432] They become the ultimate uh it worked
[434] for me machine.
[437] So these are very challenging systems to
[438] build and even if you get around
[441] the problems that hallucinations
[443] provide,
[444] the the physics of the situation are
[446] against you.
[447] Right? We're
[449] We're trying to build these systems. How
[450] do we tell an LLM what to do? How do we
[452] get it to follow our instructions? We
[454] give it a prompt.
[456] Well, every token we put in that prompt
[457] slows it down and it costs more money.
[460] So that's a double-edged That's a double
[461] whammy. You're you're driving up your
[463] cost to provide the service and you're
[465] providing a worse user experience.
[469] >> So, those tokens really matter. This is
[470] why context engineering is very hot
[472] right now.
[473] You have to put the right tokens into
[475] those contexts.
[477] But, because of cost and performance
[479] concerns, you want to put as few tokens
[481] in as you can.
[483] And it's not like you can get away with
[485] fewer tokens and bigger better models.
[487] The bigger better model bigger better
[489] models
[490] are not that much better.
[492] We've all been underwhelmed by the most
[494] recent big model release. And so, it's
[497] not much better than the last one.
[500] And Apple, you know, they famously had
[502] their paper that proved that those AI
[504] reasoning models didn't really reason.
[507] They don't
[507] think much harder.
[509] They don't do any better.
[511] So, the bigger models aren't going to
[512] bail you out.
[514] We have a ton of engineering pressure to
[516] use a small model with as few tokens as
[518] we can.
[520] But, somehow we have to get like 95%
[522] accuracy
[524] for a task.
[525] And it's still that's not very good.
[527] Like, what SaaS service does your
[528] enterprise subscribe to that's got one
[530] nine of reliability?
[532] Exactly zero, I promise you.
[535] And then the math is not you could be
[537] happy about 95% and 95% is fine for some
[539] use cases.
[541] Submitting PTO requests or figuring out
[543] how many days of leave. Sure, you can do
[545] that with 95% accuracy.
[548] But, not enterprise tasks. Not certainly
[550] five of these in a row. Five tasks at
[552] 95% success, you're looking at a C
[555] average. That's about 75% success rate.
[558] Add another five or 10, 20.
[562] You're you're looking at almost single
[563] digits.
[565] This is not enterprise reliability. And
[567] what enterprise workflows are shorter
[569] than five steps?
[571] Not many.
[574] So, this is a tremendously tough. As
[577] engineers, right? We got a system that
[578] may lie to us and we're being asked to
[581] use as small models possible with as few
[584] tokens as possible with the best
[585] performance as possible with as close to
[588] human level intelligence as possible.
[591] Build something that our enterprises can
[593] trust.
[594] It's hard.
[595] Very, very hard.
[599] And the tools that we've had have at
[601] hand haven't exactly given us the
[603] foundation for building these
[604] trustworthy systems that enterprises can
[607] take advantage of gen AI.
[609] Gartner and the like are talking about
[611] knowledge graphs. Obviously, I I
[612] mentioned knowledge graphs are the key.
[614] Um and we'll get to that in a second,
[615] but why not what we've got now? Why not
[618] fine-tuning? Originally, I I think a lot
[620] of people thought, "Well, we can just
[621] put our enterprise knowledge directly
[623] into these foundational models and
[625] that'll solve the problem."
[627] Well,
[628] you're still subject to the challenge of
[630] hallucinations and there's no
[631] sidestepping that with that approach.
[634] As a vendor like StartOr gets very
[636] difficult to get custom models through
[638] IT security. That could be a
[639] non-starter. And if you're on the other
[641] side and you don't have to worry about
[643] that, there's still
[644] pretty significant capital requirements,
[646] data requirements,
[648] hardware requirements that is not
[651] necessarily going to be a good fit.
[654] And then there's rag. Uh everyone's
[657] I'm surely familiar with rag. Uh rag is
[658] fantastic. It's led many successful
[662] first-generation generative AI projects
[664] into production.
[666] But we have to be real about what rag
[668] is. It's slightly better enterprise
[669] search.
[671] And we needed better enterprise search.
[673] We've needed it for a very long time.
[675] So, I'm very excited that rag has come
[677] along and provided this capability. But
[679] fundamentally, that's all it is.
[682] And we can see that by the fact that it
[684] only considers textual data.
[687] Go to Anthropic's website and you look
[689] at their Claude stack.
[691] Claude is as impressive as any
[692] generative AI technology at all. Their
[694] cloud stack
[696] text data only. They don't consider any
[698] structured sources.
[699] Everyone here works in a big enterprise.
[701] Your data teams, that's all structured
[703] data. All those dashboards, that's all
[705] structured data behind them.
[708] So, how are we going to build a
[708] trustworthy AI system that doesn't use
[710] any of the data that our enterprises
[711] trust?
[713] You're not going to.
[715] And graph rag doesn't change the
[716] situation.
[718] It's just rag with better marketing.
[721] Slightly better accuracy.
[723] But still the same challenges. Still
[725] doesn't consider most of the enterprise
[727] data. Certainly not the most important
[729] enterprise data.
[733] Then you have, not to mention relational
[734] solutions, but simple graph databases,
[738] simple RDF based systems, vector
[740] databases. No, they're not good enough.
[743] Even those RDF based systems and the
[745] simple graph databases that pretend like
[747] they do knowledge graphs with the
[748] knowledge part of knowledge graphs. You
[750] know, the ontologies.
[752] They all start with the same
[753] precondition. Step zero is
[757] go to your entire world of enterprise
[758] data.
[760] Take a subset of it. Make a copy and put
[762] it into our system.
[765] So, you're going to start out building
[767] an enterprise system
[769] that's going to power important decision
[770] making with out of date and incomplete
[772] data.
[773] No, you're not. No one's asking for
[775] that.
[777] So, it's not good enough.
[779] So, don't waste your time with
[782] kind of these old generation approaches.
[785] Knowledge graphs provide the appropriate
[787] foundation for powering generative AI in
[790] the enterprise
[791] for two reasons.
[795] They can deal with this through context
[796] and connectivity. We'll talk a bit more
[798] about what that means in a second.
[800] But this is what your enterprise looks
[801] like today, right? All these little
[803] circles, you can think of these are
[804] dashboards, right?
[806] And in those circles, that's a data team
[809] and infrastructure
[810] and
[812] those magnified we can get some insights
[814] for our enterprise in those circles.
[817] They're often aligned with different
[819] This is like the customer 360 use case
[820] we were going through before. They're
[822] aligned with different areas of business
[824] and we have some insight. We can get
[825] some trustworthy answers right smack dab
[828] in the bull's-eye of some of these
[830] areas.
[832] But holy cow, look how much is not
[833] covered.
[835] Look at how much insight we can't access
[838] because we have no visibility.
[841] The data's there, we just can't get to
[842] it.
[843] And look at how little overlap we have
[846] in the major areas of concern, the
[847] things that we care about the most that
[849] we've taken the time to make these
[851] little islands of
[853] insight.
[855] Practically no overlap.
[858] It's very hard for us to do what we need
[861] What enterprises are asking for us to do
[862] with this generative AI technology
[865] is in this mess.
[867] Go find that proverbial needle in the
[869] haystack.
[870] Find that root cause that's contributing
[872] to some problem or the one thing that
[875] unlocks value for the business or for
[877] our customers.
[879] Find that one thing.
[881] And then pull that thread all the way
[883] across the business.
[886] Across all the different relevant
[887] systems and processes and areas of
[890] concern.
[892] Collect all the relevant information.
[895] Put it in the hands of the right person
[896] at the right time.
[898] Or increasingly put it in the hands of
[899] the right AI system at the right time.
[904] But being able to have this complete
[906] picture
[907] This is what knowledge graphs enable.
[911] I said they enable that through context
[912] and connectivity.
[914] What does that mean and how does that
[915] work?
[917] This should be a little more hockey
[918] stick since it's exponential.
[920] Connectivity powers this. It's is the
[921] network effect
[923] of the connections.
[925] And it's easy to illustrate. We just
[926] think through this customer 360 case we
[928] had. So, we have just that product
[930] catalog.
[931] We cannot ask very sophisticated
[933] questions about our product catalog.
[935] What products do we have?
[937] How many do we have?
[939] Are any of them blue?
[942] As soon as we add a second,
[945] purchases of those products,
[947] it's a lot more interesting questions.
[950] What's the most popular product?
[953] The least popular?
[955] What's the trend for those products over
[957] the last 5 years?
[961] How about those products and the support
[963] request they receive?
[967] How about different versions those
[968] products we get from different suppliers
[970] located in different geographies subject
[972] to different concerns?
[974] You add that third, fourth, fifth, 10th,
[977] eventually you start considering the
[978] whole enterprise.
[981] The connectivity of those systems drives
[985] complexity of the questions you can
[986] answer.
[988] And that is directly correlated with the
[989] value provided by answering those
[991] questions.
[993] An enterprise is trying to live all the
[994] way out here on the right.
[997] We solved a lot of this stuff here on
[998] the left. That's what those little blue
[1000] circles were in that last diagram.
[1004] But now we need to move
[1006] out on the right. We need to get up that
[1007] hockey stick curve of value, and we can
[1009] only do that through connectivity.
[1013] Connectivity's hard, though.
[1015] All those different areas,
[1017] retail, shipping, logistics, they've all
[1019] got different ways they talk about their
[1021] data. So, you have to understand the
[1022] context. You have to understand how the
[1024] data's stored, what it means, what it
[1026] means to the business, what people mean
[1028] when they talk about it,
[1030] and what that data means as it exists in
[1033] the world. We started off with our
[1034] tariffs example.
[1036] There's a lot of world impact that are
[1038] outside of the walls of your enterprise
[1039] that needs to be taken into account.
[1040] That's a lot of context.
[1043] So, it's understanding that context that
[1046] unlocks that connectivity.
[1048] And it's moving up that connectivity
[1049] curve that moves us up the enterprise
[1051] value curve.
[1053] And knowledge graphs enable that by
[1054] providing that foundation of context and
[1057] connectivity and lets us create these
[1060] trustworthy systems.
[1063] So, at this point, if you came in
[1065] knowing about knowledge graphs,
[1067] I'm certain you've said this at some
[1069] point, if not a coworker said it to you.
[1071] Uh if you came in unfamiliar with
[1072] knowledge graphs, you're
[1074] almost certainly thinking this uh
[1075] because you weren't familiar with them.
[1077] I don't know how to build a knowledge
[1078] graph.
[1080] And if you're a little bit familiar,
[1081] you've probably heard I've mentioned it
[1083] a few times, the ontology word. The key
[1086] providing that context.
[1089] I don't know how to build an ontology.
[1090] We can't build ontologies. We're not
[1092] ontologists.
[1094] None of that's true.
[1096] You can build ontologies. You have
[1098] ontologists. It's you. It's your
[1099] coworkers. I promise you no one knows
[1101] your business better than the people who
[1103] work at your business.
[1106] Your on top Your ontology should reflect
[1108] your business. How you operate, how you
[1110] work, what you mean when you talk about
[1112] your business and your data. That's your
[1114] ontology.
[1118] So, the way to build knowledge graphs,
[1119] the power
[1121] these generative AI applications provide
[1123] trustworthy AI through knowledge graphs.
[1126] You institutionalize your knowledge in
[1128] these ontologies.
[1129] You do not write them down in arcane
[1131] syntax. You do not need any special
[1133] skills. You write user stories.
[1136] Now, anyone coming from engineering
[1137] product background, you certainly
[1138] written a user story. They're pretty
[1140] simple.
[1141] As an XYZ, you know, as a user of this
[1143] software,
[1144] I need XYZ
[1146] to ABC to unlock some value.
[1150] Right, and engineering teams groom that.
[1152] They take it apart. They figure out the
[1153] different parts and pieces, the who,
[1154] what, the where, the when, the why to
[1156] make that happen so they can provide XYZ
[1159] to unlock value ABC for their users.
[1162] It's the exact same thing here. We're
[1164] going to do that except I guarantee
[1166] you've already written down your
[1167] ontology.
[1169] You have these user stories. There isn't
[1171] a business in operation today that
[1172] doesn't have their goals written down,
[1174] doesn't have their most important
[1176] problems written down.
[1179] Listen,
[1180] business 101.
[1181] I guarantee this stuff's written down.
[1182] So, it's just a matter of bringing it
[1184] forward and promoting it and making it
[1187] the center of your knowledge graph.
[1190] That seemed a little abstract. Let's
[1191] walk through it in slides and then we're
[1193] just going to do this and we're going to
[1194] create a knowledge graph. We're going to
[1195] create it from five questions.
[1198] So, here's the user story BCBS 239.
[1202] I know there are some people from the
[1203] financial services domain here today. Um
[1207] this is probably very familiar to you uh
[1209] but for a lot of you it's not.
[1211] But I'm certain you see the ontology
[1213] here.
[1215] It's the data for the bank about their
[1217] liquidity positions, exposures,
[1219] counterparties, currencies,
[1221] jurisdictions. They care about risk data
[1222] aggregation. They want to manage
[1224] liquidity and risk.
[1225] So, I've got ideas of what the things
[1227] they care about and what they want to do
[1229] with them.
[1231] Well, that's half the battle. That's
[1232] what your ontology describes, the things
[1234] that you care about as a business, what
[1235] they mean and where they are.
[1239] We can groom this, we can take it apart
[1240] into some additional questions that
[1242] teases out more of the use case, more of
[1245] the things that we care about in our
[1247] world.
[1248] And you take one of these questions and
[1249] we break them up.
[1251] It's like just underlining the nouns.
[1252] The nouns become concepts in our world.
[1255] And we can very quickly scribble lines
[1257] between them.
[1258] Connect those all up.
[1262] We call it sketch ontology.
[1266] I know many of my engineering friends
[1268] here today, we start at whiteboards. I
[1270] think most people when they're starting
[1271] projects start by sketching out the
[1273] idea.
[1275] Knowledge graphs don't need to be any
[1276] different. So, we'll sketch out your
[1278] ontology from your user stories, from
[1280] your questions.
[1282] Already custom fit for you, for your use
[1284] case, for how you talk about your data.
[1287] So, you already know how to use it.
[1288] There's no training.
[1290] You've been talking about your business
[1291] for years.
[1294] If you want to make the knowledge graph
[1295] bigger, do you want to make it more
[1296] sophisticated, do you want to be able to
[1297] answer more questions? You add more
[1299] stories. You write more prop state
[1301] Excuse me, problem statements.
[1305] It doesn't have to be hard.
[1307] Like I said, we're already writing all
[1308] these things down. We write down our
[1309] goals. We write down our problems.
[1311] We make to-do lists.
[1313] And we just turn that into an ontology.
[1315] We turn it into a knowledge graph. And
[1316] we can change how our business is
[1317] operating.
[1319] So, let's go ahead and see how that's
[1320] done.
[1324] So, I'm going to jump over into Stardog
[1327] Designer here again.
[1329] And this is starting a project. Uh I am
[1333] on a webinar.
[1335] And
[1338] I am a
[1340] supply chain analyst.
[1343] I've done my preamble.
[1346] I'm going to get some questions here.
[1350] Go ahead.
[1352] One by one.
[1354] I thought about prepping this, but the
[1356] whole process usually goes so quickly
[1359] that I wouldn't have taken up all the
[1360] time of my demo.
[1362] So,
[1364] I apologize if this may be a little
[1365] tedious, but if for nothing else it
[1366] proves that this is no theater.
[1369] So, five questions, like I said, that
[1371] describe my area, supply chain.
[1374] I'm going to go ahead and start and
[1375] generate my bare-bones project here.
[1379] Open up the settings. I can see my
[1380] questions.
[1382] Move Zoom out of the way.
[1385] All right.
[1386] Now I need to add some data. So, all I
[1388] have to do
[1391] I'm going to go ahead. I'm going to use
[1392] MySQL here.
[1394] Oops.
[1395] And the Northwind data set, common test
[1397] and demo data set everyone may have
[1399] heard of before. Going to go ahead and
[1401] we're just going to
[1403] select the whole thing.
[1405] Every single table you can see is These
[1407] are live connections to that relational
[1408] source. I can see the data.
[1411] All right. I'm going to say create map.
[1412] Yes, please create me the knowledge
[1414] graph from all of that stuff.
[1417] So, it's going to go ahead and it's
[1418] going to think a little bit. What Voice
[1420] Box is doing is it's interrogating each
[1422] of those sources, sending it some SQL
[1423] queries, getting the schemas, looking at
[1426] the primary and foreign keys, trying to
[1428] understand how that data is related with
[1431] respect to those questions that I
[1432] entered.
[1434] So, boom.
[1437] Relay that to a relay out. So, we've got
[1439] a nice
[1441] I'm going to proto knowledge graph. It
[1442] created that data model for me,
[1444] associated it with all of my data.
[1448] But, let's see here. I can use Voice
[1450] Box.
[1451] They're not the best labels.
[1453] Order and order detail, you know.
[1456] Product is related to order detail by
[1458] the word product.
[1460] It's not very helpful. So, I'm going to
[1461] just go ahead and
[1463] ask Voice Box to do a better job on the
[1465] labeling.
[1467] So, it'll think about it. It'll look at
[1468] my model. It'll reconsider my questions
[1470] and try and make something that's a
[1471] little more human friendly.
[1476] Here we go. You can see updated all of
[1478] those labels. This look much better. As
[1481] a human reading them, I have a much
[1482] better idea.
[1484] So, I can go ahead and just accept all
[1486] those changes.
[1487] And I have basically just now got a
[1489] knowledge graph.
[1491] And I'm just going to go ahead and
[1492] publish.
[1494] Now, I've tried this a few times.
[1497] Oop.
[1503] Hopefully the fourth time is still the
[1504] charm. And we're going to enable voice
[1506] box.
[1507] Uh
[1508] I don't need to download anything when
[1509] I'm done.
[1511] We're going to use all the defaults here
[1513] and just we're going to go ahead and
[1513] publish.
[1515] So, this is actually going to take about
[1517] hopefully then about a minute, hopefully
[1519] not three. Um cuz I have to vamp for the
[1522] whole time while it's going.
[1524] What's happening right now is
[1526] it's taking what what are called
[1527] mappings. So, it I said, it looked at
[1529] those data sources, it figured out
[1530] primary and foreign keys, it created
[1533] that data model, and it kind of smooshed
[1535] those two things together, that model
[1537] and those mappings. So, that's how
[1540] the knowledge graph is able to access
[1542] all that structured information that's,
[1544] you know, logically part of the
[1546] knowledge graph, but not physically
[1547] stored in the knowledge graph.
[1549] It's indexing that schema that was built
[1552] so that when questions come in, it's
[1554] able to do relatively sophisticated
[1556] semantic parsing to understand the
[1558] intent of those questions. So, I said,
[1560] context is key.
[1561] It's got to be able to compile that
[1563] context and understand the questions as
[1565] it goes.
[1567] Um and then as an aside for everyone
[1570] here who's a practitioner who's hoping
[1571] to build stuff like this,
[1573] everything that you've seen,
[1575] first demo, second demo,
[1577] these are all available in all of our
[1578] APIs, MCP, LangChain, all that good
[1581] stuff.
[1582] Uh I mean, I love our interfaces. I'm
[1584] very proud of the engineering team that
[1586] has built them. I think they're great.
[1588] Uh but I can appreciate that you may
[1589] need to integrate into your enterprise
[1592] ecosystem
[1593] uh on your own.
[1595] Uh all this is available for easy
[1597] integration through APIs.
[1601] All right. Uh of course, this takes
[1602] longer than planned.
[1604] All right, here we go. I just had to I
[1606] just had to think about it for a second.
[1609] Go ahead, and we're going to fire this
[1610] back up. We'll go back into
[1614] Start log explorer.
[1617] It'll take a second and here's that data
[1618] model we just created together.
[1620] So I can see it all
[1622] nice and easy and Voicebox is right
[1624] here. I'm the president everywhere
[1627] can be to help me.
[1629] The question. So just level set.
[1632] We We pushed some buttons. We We asked
[1634] some questions and some data. There's no
[1636] fine training. There's no fine tuning.
[1638] There's nothing to set it up
[1640] for this question. What is the name of
[1642] the most used supplier for any shipper
[1645] who shipped orders placed by customers
[1647] in Brazil, but those orders were handled
[1649] by employees not in Brazil for products
[1652] in the produce category?
[1655] Such as every single thing in the schema
[1657] that we created over here.
[1659] Every single thing.
[1661] So what happening in Voicebox
[1663] is understanding the intent of this
[1664] question. It's figuring out which data
[1667] in that MySQL database is relevant. It
[1669] is writing one or more SQL queries to go
[1671] fetch that data from the source
[1674] and then bring it back and try and
[1676] figure out the answer for this question
[1679] based on the information that it
[1680] retrieved from the knowledge graph.
[1684] It's usually a lot faster.
[1686] I've said that several times today. Of
[1688] course when when I'm on the air
[1689] everything goes slowly, uh but it'll
[1691] come back here in a second and tell me
[1694] that a chippy distributor named Good Day
[1696] Mate
[1698] is our one supplier who's handling
[1701] orders in Brazil uh
[1703] with employees not in Brazil
[1706] Well,
[1707] while that's thinking here in Voicebox,
[1709] we'll just jump back over to the
[1711] Voicebox or in explorer, we'll jump over
[1713] to the Voicebox interface and we can see
[1719] uh
[1720] Sorry about that. Clicked the wrong
[1722] thing.
[1728] I'm just dropping here. All right.
[1732] So we can see our answer here.
[1734] We can see g'day, mate.
[1737] We can see all the different things that
[1738] were involved in this answer, all the
[1740] different data sources.
[1742] Oh, that took a little longer than
[1743] expected, but I think a lot of people
[1746] here write SQL queries. When was the
[1747] last time you wrote a SQL query over
[1749] eight tables?
[1751] Over a database you had never seen
[1752] before
[1753] in less than a minute.
[1759] We can see the visual explanation of
[1761] that query.
[1762] We can see the code of that query.
[1766] Full confidence and traceability in our
[1767] answer from start to finish.
[1770] So this is what knowledge graphs enable
[1772] and how we build these trustworthy AI
[1773] systems.
[1775] And we build them quickly and easily.
[1776] This is a really sophisticated question.
[1778] I know it took a few seconds to answer.
[1781] But that's the kind of questions our
[1782] business are trying to answer.
[1784] We can answer them with knowledge
[1785] graphs.
[1788] So
[1789] we are
[1791] I stuck the landing on time. I'm just
[1792] going to
[1793] jump here.
[1795] We'll skip the recap slide.
[1798] Uh cuz I'd like to make sure we have
[1799] plenty of time for questions uh cuz
[1801] there seems to be at least a lot in the
[1803] chat. Um
[1805] but I just before we get into the
[1807] question answering, I want to mention
[1809] that we're going to do a tutorial. It'll
[1811] be a more in-depth version of what you
[1812] just saw or we're going to do this
[1814] together.
[1815] Um so it'll be hands-on. Uh that's in
[1817] about 6 weeks.
[1819] Uh space is limited because it's a
[1820] hands-on activity. Uh so I encourage
[1823] everyone if what you saw here today was
[1825] interesting, you want to get started,
[1828] can absolutely start now at stardog.com.
[1831] Get started with Stardog Cloud. Uh but I
[1833] encourage you to sign up for our
[1834] following webinar so we can do this
[1836] together.
[1840] So at this point, um I'm going to
[1842] holy moly. All right.
[1848] There's a lot of chat and a lot of
[1849] questions.
[1851] All right, so first one is is this just
[1854] structured data? What about unstructured
[1856] and semi-structured forms?
[1858] So, that's a great question. I figured
[1860] someone would ask that cuz I I
[1862] I definitely was strongly talking about
[1864] structured data and the importance of
[1866] structured data. And then in our demo,
[1867] we saw just MySQL.
[1869] Uh, Stardog itself can handle both
[1871] structured and unstructured. We have a
[1875] system called what we call safety rag,
[1877] which isn't rag at all, but you know,
[1879] it's branding.
[1881] Um, and it's able to deal with
[1882] unstructured sources. It transforms them
[1884] into structured data.
[1886] So, it does information extraction and
[1887] entity recognition to pull that
[1889] information out and enrich your
[1890] knowledge graph.
[1893] Uh, and oh, and uh, for semi-structured,
[1896] things like um, Redis,
[1899] Elasticsearch, Stardog's back end can
[1902] already talk to those. It treats them as
[1903] structured data. Um, so from that point
[1905] of view, there's only two kinds,
[1906] structured and unstructured for us.
[1911] Uh, next one,
[1913] how much effort, time, money, and skills
[1915] goes into standing up a useful ontology
[1917] and maintaining it? Uh,
[1921] well, if you do it the old way, a lot
[1924] and it's not worth it.
[1926] Uh, if you go the route that I strongly
[1928] recommend, which is through just
[1930] documenting your business's problems
[1932] through user stories,
[1933] it is much easier to
[1935] both create and maintain the ontology
[1938] and have an ontology that actually fits
[1939] your use case.
[1941] What I see a lot with these ontology
[1944] creation efforts,
[1945] whether they're community efforts or
[1947] just internal efforts, is they're made,
[1950] um,
[1952] in theory.
[1953] They're not aligned to the real world.
[1955] They're not actually aligned to the
[1956] business. So, they become very difficult
[1958] for the business to use and the
[1959] businesses form the wrong idea about
[1961] ontologies and knowledge graphs
[1962] generally.
[1964] So,
[1965] the ontology exists, it's in your
[1967] organization, you just have to write it
[1969] down.
[1979] Next, is it possible to take the output
[1982] a step further to generate long-form
[1983] documents, slides, presentations
[1985] according to predefined templates?
[1988] Uh yeah, absolutely. I That was um part
[1991] of my point of trying to point out that
[1993] everything that you saw in Stardog is
[1995] available from API. So, yeah,
[1999] you will certainly see all of those
[2000] things coming into our product, but at
[2002] the same time, our product has been
[2004] built so we ourselves can build those
[2006] things so you could build them, too.
[2008] Uh particularly if you have
[2010] uh some technology that you're already
[2012] using for slide creation, it would be
[2013] very trivial to be able to hook up the
[2015] output from Voicebox, all that rich,
[2017] curated, trustworthy data, and pipe into
[2019] the slide so it actually uses the
[2021] correct uh up-to-date, accurate
[2024] information that you're pulling out of
[2025] the knowledge graph.
[2035] Um
[2036] then
[2039] there's a
[2040] lot in the chat. I don't know if we will
[2043] get to all of the chat, but any
[2045] questions that are in the chat, we'll do
[2046] one or two more here that are in the
[2048] Q&A. Uh but I promise everyone here if
[2051] we don't get to your question live, I
[2054] will make sure that we get to it
[2055] offline. You'll get an email from us. Uh
[2057] you'll also be getting the slides and
[2059] and link to the recording uh as a leave
[2062] behind.
[2063] Uh but just trying to be mindful of the
[2064] time here. We'll do two more questions.
[2068] Uh
[2069] one, how advanced is the ontology
[2071] editor?
[2072] So, asking about designer.
[2075] Uh
[2076] I will say not very advanced, and that's
[2079] by design.
[2082] These ontologies do not need to be
[2084] extremely sophisticated to actually
[2086] provide value to these organizations.
[2088] It's another pitfall that I see when
[2090] people try and build knowledge graphs.
[2092] They try to build
[2094] these very complex ontologies that that
[2096] again are not really tied to the
[2098] problems the business has or how the
[2099] business thinks or works. They're just
[2101] cool ontologies.
[2103] So, designer is
[2106] um
[2107] limited in that respect. Cuz we were
[2108] It's opinionated, I think is a better
[2110] way to put it. They are simple models
[2113] meant to let you get on with the
[2116] business of building knowledge graphs
[2117] and not get bogged down with what it
[2120] means to have a restriction on a
[2121] property cuz that almost never is
[2123] helpful.
[2128] All right. And then last one, what is
[2129] the best way to build RDF-based graph
[2132] rag applications?
[2135] How do we prove the accuracy of sparkle
[2137] generation, especially with a large
[2139] ontology?
[2140] Um
[2141] Well, first thing is to not use graph
[2144] rag. Uh that would be the
[2146] the best way you can improve your
[2148] accuracy cuz rag just isn't going to cut
[2151] it.
[2152] If for nothing else, it it doesn't have
[2154] most of the useful information that you
[2156] need.
[2157] But it also lacks that context and
[2159] connectivity really that you need to
[2161] effectively build queries, deal with
[2163] these large ontologies. Businesses are
[2165] big. There are a lot of things they care
[2167] about. And two parts of the business may
[2169] use different words to talk about the
[2171] exact same thing.
[2173] So, there's no one-size-fits-all
[2175] ontology even for a single organization.
[2179] Uh and with that, I think
[2182] we will wrap things up. Uh but I really
[2184] appreciate all the time consideration
[2187] from everyone today. Just a ton of good
[2189] questions. So many people were able to
[2191] join. I'm very excited. Uh as I said, we
[2194] will send slides and the leave behind.
[2197] So you have a link to the presentation.
[2199] You can try this all out on stardog.com
[2203] and we can do this together again in 6
[2205] weeks, build a knowledge graph
[2207] uh from scratch on a hands-on tutorial
[2210] that I'm really looking forward to. So
[2212] thank you everyone again for your time.
[2214] I'm Mike Grove from Stardog.
[2216] Good luck building your trustworthy AI
[2218] systems.
