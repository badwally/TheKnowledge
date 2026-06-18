---
schema_version: 1
id: yt-hILYM9oBI0M
type: youtube
title: 'KGC 2023 Keynote: Knowledge Graphs in Today’s Evolving Landscape & Beyond
  — Deborah McGuinness, RPI'
url: https://www.youtube.com/watch?v=hILYM9oBI0M
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:37:57Z'
content_hash: sha256:ec03aa9af3d58b88026fc78b91ee7897bad5028e43c3d47d5f702bf79f347fe2
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 1777
  caption_track: cached
  snippet_count: 699
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:37:57Z'
  user_correction: null
---
[2] hey hello good morning everyone welcome
[6] to the knowledge graph conference for
[8] those who were not here yesterday and
[10] the day before
[12] and we now have uh the honor to welcome
[17] Deborah McGinnis that will give us a
[21] keynote Deborah was the recipient of the
[24] KGC award last year and
[29] Deborah is a long time practitioner
[32] researcher in the field of semantic web
[35] ontologies knowledge Engineering in
[37] general and uh she will bring us a New
[42] Direction for the field today
[46] the recipient of this year's award will
[50] be announced tomorrow morning so uh be
[53] here
[54] Deborah
[55] great thanks very much for that uh
[58] gracious introduction and I'm really
[61] thrilled to be here talking to the
[63] knowledge graph Community I have been in
[65] the knowledge graph Community since way
[66] before we used the phrase Knowledge
[68] Graph and the ontology Community for
[69] many decades and one of the benefits
[72] from being in the field for a long time
[73] and being asked to give the opening
[75] keynote is that you might get to think
[79] back and think forward and bring up a
[82] few topics that might be worthy of
[84] discussion and that might set some
[86] directions uh for the field
[88] so knowledge graphs the title is
[90] knowledge grass in today's evolving
[92] landscape and Beyond
[94] so you can't be anywhere close to this
[97] field without realizing that the AI
[99] landscape is changing you know I did a
[102] few searches for some topic from some
[105] titles like uh how llms could transform
[109] the world uh they're changing the game
[112] for X I happen to choose tax filing but
[114] for everything uh and then the title for
[117] one of them chat GPT changes everything
[119] which I think is true you know one of
[123] the take-home messages that you should
[124] get from this is we are at an inflection
[127] point that this community this broad
[130] Community knowledge graphs ontologies
[132] web 3 provenance that we can really jump
[136] on and I think the time is now so that's
[138] one of the take-home messages that I
[141] will remind us at the end
[143] you know there's surprising speed and
[146] surprising accomplishments you know you
[148] can't ignore the uh the impact that they
[153] have with passing these tests that
[155] experts
[156] um sometimes have trouble passing so one
[159] of the I'm gonna collect some messages
[161] uh throughout this talk one of the
[163] messages is the accomplishments of llms
[168] we really need to acknowledge them and
[170] we really need to leverage them
[172] um and so I'm gonna hopefully give some
[175] topics that we can discuss on how and
[177] when we might leverage them
[180] but what does it really mean to pass a
[183] test
[184] um so CNET had this great quote uh so it
[187] can pass the bar exam but does it matter
[190] uh and I really like this exams or
[193] performances they don't test how
[195] knowledgeable students are they test how
[197] much students can cram into their brain
[199] and regurgitate for a few hours much of
[202] the information is subsequently
[203] forgotten often with Glee they're closer
[206] to tests of dedication than they are of
[208] knowledge and actually over the last
[210] couple of days here I've had a lot of
[212] conversations about what knowledge is
[214] anyway and given that my PhD is a
[217] knowledge representation that's like a
[219] topic of major interest but
[222] um but do they have knowledge or can we
[225] use what they've got whatever we're
[227] going to call it
[229] so do they understand
[232] you know some of the important questions
[234] I think are when can and should we trust
[238] the results of gender to the eye and can
[241] they help us figure that out so can they
[244] tell us how they came to an answer you
[246] know they might be able to tell us what
[248] question they're trying to answer
[249] whether that's the question that we put
[251] in or whether that's a question that
[254] somehow they've decided that if they
[257] could answer that question then they
[259] could answer the bigger question and
[261] that's a step in the right direction but
[263] that I don't think is enough in many
[265] settings and can they provide the
[268] context in which their recommendations
[270] are reliable I think the answer is no
[273] but I think our field or our Fields can
[277] help there
[278] so there are many opportunities and I
[281] think the opportunities kind of scream
[283] semantics and they scream knowledge
[286] graphs and I think I'm going to convince
[289] you or you can ask me if I haven't
[291] convinced you
[292] um that uh this field has a unique
[295] opportunity now
[298] so in homework for this talk I was using
[300] uh chat GPT quite a bit I asked them I
[305] asked it what are knowledge graphs and
[307] why are they important for a generative
[309] Ai and actually
[311] consistent with I think what a lot of us
[313] are finding they actually gave pretty
[315] decent I got some pretty decent answers
[317] and I did it a few times and I got
[319] consistently some pretty good answers
[322] um they they gave this this answer gave
[324] three main topics
[327] um they provide more efficient
[328] organization and retrieval of
[329] information you know that might be a
[331] little bit debatable but the knowledge
[334] in a structured format that is
[336] definitely something that we do better
[338] than
[339] um generative AI currently does not that
[342] it can't be asked to do that and not
[343] that it can't provide syntactically
[346] correct structure for some things but is
[350] that syntactically correct structure
[352] containing the semantic content that we
[355] want it to be we want to be in there
[359] um secondly knowledge graphs are more
[361] powerful and and accurate processing of
[363] information
[365] um I don't think we're going to compete
[367] with the generative AIS for powerful
[369] processing of information but accurate
[372] processing of information and what is
[375] accuracy and how are we going to
[376] evaluate it
[378] um and uh knowledge gaps can provide
[381] foundations for sophisticated querying
[383] and reasoning capabilities I went to an
[386] interesting master class yesterday by
[388] relational AI where they gave some
[392] um thought-provoking examples of what
[395] appeared to be reasoning
[397] um and you know at a certain level it
[400] did uh it did do some reasoning so
[404] um Vijay asked it uh to assume the
[407] closed World assumption and then answer
[409] some questions which you know was maybe
[412] a shiny object maybe kind of a cute
[414] parlor trick but but there was some
[416] content there so you know they got to
[419] start at some reasoning functionality
[422] I'm not really sure that I'm going to
[423] use capability
[425] um but this is a place that knowledge
[427] graphs can play and uh they also said
[431] knowledge graphs can extract insights
[433] and answer complex questions can be good
[435] for search engines recommendation
[437] systems and virtual assistants
[439] uh and third they can provide Knowledge
[442] Management and collaboration and they
[444] can help bridge communication gaps so
[447] this collaboration and bridging of
[450] communication gaps is one of the other
[452] big points that I think our field is
[454] well poised to address
[457] um so two messages from this they can
[459] help communicate and interoperate uh in
[462] ways that at least we can see with a
[465] declarative representation of the
[466] meaning and provide that interoperation
[470] and maybe not so debatably they can help
[473] move up this pyramid the d-i-kw period
[477] the data to information to knowledge to
[480] actionable wisdom
[482] um so I think this is another
[484] opportunity for this field
[488] and then you know one of the things that
[490] I've struck by
[492] um I took my first AI class in the late
[495] 70s and I still love AI but we are we've
[499] never been in the news like we are today
[501] you know I've been through AI Winters
[503] I've been through AI Summers one of my
[505] colleagues calls this the AI scorcher
[509] um you because now we are having
[512] emerging discussions and pending
[514] legislation so like the blue print for
[517] the AI Bill of Rights you know I don't
[520] really know how we're going to make this
[522] effective and enforceable but these
[525] topics are going to come out whether
[527] they're coming out from government or
[528] whether they're coming out from
[530] technological bodies that try to create
[533] safe and effective systems try to
[536] minimize discrimination try to provide
[539] data privacy
[541] um provide notice and explanation for
[542] those of you who know me my thesis was
[545] on explanation in the 90s
[548] explanation is near and dear to my heart
[550] you know I I'm not happy with the
[553] explanation capabilities today of
[556] generative Ai and there's tremendous
[558] opportunities there
[560] and then these human Alternatives and
[563] consideration so an opportunity to say
[566] hey this is wrong and hey I need some
[568] recourse option you know it's I'm not
[572] seeing that today in generative AI so
[574] one of the things that knowledge graphs
[577] may be poised to help with is to address
[580] these policy needs and requirements and
[583] potentially at least expose
[585] accountability issues maybe not solve
[587] them but you know this is something that
[589] we need to address
[592] again if you ask open AI what are
[594] generative AI limitations and actually
[597] when I post this I've got links for
[600] everything that I pulled from and all
[601] the questions that I pose to open AI
[603] because I try to be a transparency
[605] researcher
[606] um so one challenge for generative AI is
[609] to ensure that the generated data is
[611] coherent consistent and semantically
[613] meaningful and this is where knowledge
[616] graphs can come in handy so again we're
[619] very well aligned with the knowledge
[622] graph strengths of semantics provenance
[625] relationships and potentially logical
[627] relationships that are well well exposed
[630] and well defended
[633] so if we just look at some challenges
[637] and strengths of large language models
[641] and knowledge graphs they kind of align
[644] pretty interestingly so if you ask open
[648] AI
[649] um it's got challenges around coherence
[651] provenance semantics and explainability
[654] if you actually I did ask open AI what
[657] the challenges were for knowledge graphs
[659] and this is a paraphrase of what it said
[662] the time required to build them at least
[664] required to build good ones the people
[667] and the skill sets required to build
[669] them uh the scalability and the
[672] integration across multiple knowledge
[674] graphs you know these in my mind align
[677] quite well and so
[679] debatably and maybe not so debatably
[682] knowledge graphs and large language
[684] models they might be a marriage made in
[687] heaven or wherever your happy place is
[689] but they can at least be a complementary
[691] marriage and
[694] um one take-home message is this and the
[697] other take-home message that goes along
[699] with this is we've got a time now that
[702] we could really jump on and I think if
[705] we don't jump as a community we're going
[707] to be left behind so I'm hoping that
[710] this helps create some discussions where
[713] we get motivated to work as a group and
[717] work collaboratively with these people
[719] who some people claim are putting us out
[722] of business
[724] so I just was at Ted technology
[726] entertainment and design a couple weeks
[727] ago
[728] um AI was a giant theme at Ted and the
[732] discussion kept coming up from the stage
[734] from Chris Anderson among others is AI a
[737] threat or an opportunity well
[740] um I think most reasonable thoughtful
[742] people say both uh you know I pulled
[745] this from Gizmodo here are the jobs our
[748] new AI overlords plan to kill and this
[751] is its list but the list goes on and you
[755] know there's some justification for all
[758] these fields as well as other fields
[760] that large language models can do
[762] significant portions of some of these
[765] job specifications
[767] so
[769] I also went to Austin last week to the
[773] Web Conference to uh provenance week and
[777] to a web science conference and the
[781] first day was a health science day where
[783] the new Dean of the medical school the
[787] Dell medical school at UT Austin she was
[790] speaking to health professionals and she
[792] sent a version of this she said
[794] generative AI will not replace
[796] clinicians but clinicians who do not
[799] collaborate with generative AI will be
[801] replaced
[803] and I believe that and actually my
[805] generalization of it is this that
[808] generative AI will not replace most
[810] knowledge professionals thus most of us
[812] in this room but many knowledge
[815] professionals who do not collaborate
[816] with AI will be replaced or at least
[819] their jobs are going to be modified and
[821] I I'm telling my students this I'm
[824] telling the world this because again I
[827] think we we need to really learn about
[830] what these systems can do and how we can
[833] help them and how they can help us so
[835] that we can be more than the sum of our
[836] parts so my message five is collaborate
[841] and now the rest of the talk is going to
[844] be just discussing some potential
[847] collaboration areas again I asked chat
[851] CPT uh what collaboration areas might
[854] make some sense and it suggested
[857] transparency in Providence wow we're
[859] really well suited there we've got a
[861] worldwide web recommendation for
[863] provenance on the web we've got a lot of
[865] work in transparency accuracy
[868] um we've got a lot of at least
[870] declarative representations for what it
[871] means to be accurate and then we've got
[873] ways to Define accuracy
[876] privacy uh nobody's really solved this
[879] uh at least on the llm side
[882] um but we at least have stabs at it in
[885] knowledge graphs and in web3 uh fairness
[889] and
[890] um you know at least we can say who's
[893] getting this who isn't getting this what
[895] it's been trained on and the
[897] accountability I think this is an
[899] enormous uh opportunity that we're only
[902] scratching the surface on you know and
[905] actually these are just some
[906] collaboration areas I think there's more
[908] that we can look at so message seven is
[912] explore many opportunities and create
[915] exploration sandboxes I'm going to show
[918] you a little bit about an exploration
[920] sandbox that I and a number of
[923] colleagues at RPI are creating and I'm
[925] not saying that this is the be all and
[927] end-all we're not going to spin out a
[929] startup company on this at least I don't
[931] think we are but something like these
[934] sandboxes I think we all should be doing
[935] this
[938] so this is our chat BS I didn't name
[941] this actually I don't know whether you
[943] named this uh Jamie mccusker is one of
[946] the contributors one of the primary
[947] contributors to this project along with
[949] John Erickson uh Enrique Santos Sola
[952] sharaya myself Jim hendler and pretty
[955] much everybody at the tetherless world
[956] constellation which is within RPI has
[960] been chatting about this so uh you know
[963] how can we start to think about whether
[966] the answers that we're getting make
[968] sense
[969] so this fact Checker it uses the open AI
[973] completion API service it constructs an
[976] entity relation graph in the form of
[978] entity one relationship entity two so
[981] you know the motto for knowledge graphs
[984] is started by or the blog that Amit
[988] sungal wrote Things Not strings you know
[991] so this is a thing relationship and then
[994] it uses entity looking entity linking to
[997] look up both the entities and the
[998] relationships against your choice of
[1002] resource we chose actually Jamie chose
[1005] wikidata or the group chose wikidata and
[1009] then it constructs a Json LD graph as it
[1011] proceeds so you can ask a question
[1013] unless we're asking what's the oldest
[1017] University Technical university in the
[1019] United States if you ask by the way RPI
[1021] is but if you ask it it'll get a few
[1024] different answers you can ask it a
[1027] number of times and then you can link to
[1030] the wikidata entity for that and then
[1033] you can see the the wikidata page
[1036] related to that you can see the
[1038] groundings you know groundings are are
[1041] special one of our special sauces and
[1043] one of the things that generative AI
[1045] does not do for us and then you know we
[1049] can highlight things that look like they
[1051] need additional uh discussion you can
[1054] download Jason LD uh
[1058] and then you know you can ask things
[1060] like who is Deborah you know it did a
[1062] decent job but there's a number of
[1064] things that are true and there's some
[1066] things that are false like uh I didn't
[1069] found the Rensselaer Institute for data
[1072] exploration and application but a lot of
[1074] the rest of it is actually accurate but
[1076] then you could go ask questions so this
[1079] right now is made for a Hume to support
[1081] human exploration we saw I don't know
[1084] whether yawns oh yeah yon's already left
[1086] but yons was in the room uh in an
[1089] earlier uh session where he gave a nice
[1091] little demo where he then turned around
[1094] and asked structured queries to web chat
[1097] to say
[1098] um you know can you find evidence for
[1100] one of these statements so we could do
[1102] that as well
[1104] and this is one of the ones that I
[1106] really like it says Deborah McGinnis won
[1109] the 2021 Turing award
[1112] and uh and but then you know I didn't uh
[1116] somebody else did his pictures there and
[1118] then like I we did this question right
[1120] before I was going to the um the Web
[1123] Conference where I got to hear the
[1124] Turing award lecture from Bob who's in
[1126] the audience and I told him hey you know
[1129] chat GPT says I won the touring award
[1131] and then he said oh it said I did it too
[1134] but a little while ago
[1136] and then he actually did and then I said
[1138] it from a panel at website and then one
[1140] of the panelists said you know it's just
[1142] predictive so I'm waiting
[1148] um but you know you you need to be able
[1150] to explore these kinds of findings
[1153] and you could ask then follow-ups you
[1156] know it knows that I didn't win the
[1158] Turing award if you ask it that but uh
[1160] but you know it didn't figure that out
[1162] to begin with and here's uh the picture
[1165] of how our fact Checker went together
[1167] I'm not claiming that this is the right
[1170] architecture or one that other people
[1172] should pick up but you know we all
[1174] should be exploring these kinds of
[1176] architectures finding places that large
[1179] language models help knowledge graphs
[1181] that knowledge graphs help large
[1182] language models and ultimately that
[1185] we're more than the sum of our parts and
[1188] we're transparent and we have at least a
[1191] shot at being accountable
[1195] an assessment I think is an enormous
[1198] opportunity so that was kind of one
[1201] sandbox for assessment this is another
[1204] sandbox for assessment I and a number of
[1207] colleagues oh and I need their names on
[1210] this
[1210] um well actually we've got some papers
[1212] on this I'm part of the DARPA the
[1214] defense Advanced research projects
[1216] agency machine Common Sense program
[1218] which I was super excited to get in uh
[1221] it was started by one of my favorite
[1222] DARPA program managers he went to the
[1224] kickoff meeting set up a bunch of
[1226] metrics for four-year program and then
[1228] retired the next day
[1230] um but those metrics and I came in as a
[1233] knowledge representation person my team
[1234] was going to build this co-build this
[1236] Common Sense Knowledge Graph and it was
[1239] going to help Common Sense uh on the web
[1241] and then all these language programs
[1243] started beating these metrics and they
[1245] beat your four metrics in year one so
[1248] you know the writing was on the wall but
[1250] the writing for me was I'm not going to
[1253] write that Common Sense Knowledge Graph
[1255] because they don't really need them but
[1257] what we really need is better metrics
[1259] the metrics that my one of my favorite
[1262] program managers in all time set up were
[1264] not adequate in my opinion and in the
[1267] whole program's opinion for evaluating
[1270] whether these systems really had common
[1272] sense so we were doing some context
[1275] aware exploration of ways to evaluate
[1278] common sense and again at Ted if you
[1281] listen to yaejing Chao from the Allen
[1283] Institute who's also on that program she
[1285] gave a nice talk at Ted where she was
[1288] saying we really need common sense to
[1292] help figure out I think it was Lena
[1295] somebody asked the question the other
[1297] day how can I see uh the Eiffel Tower
[1300] from Rome and one of the answers was
[1302] move the Eiffel Tower to Rome well you
[1304] need some common sense to realize that's
[1306] a bad plan it's better for you to go to
[1309] Paris or go to a museum and to see
[1311] pictures of it but uh but that that plan
[1316] to move the Eiffel Tower to Rome just
[1318] makes zero sense so we need assessment
[1322] opportunities and tools to really
[1325] provide ways to evaluate these systems
[1328] and I think common sense as part of that
[1330] is is one key component that's despite
[1334] darpa's investment is still understudied
[1337] so assessment tools I think are an
[1340] enormous opportunity
[1342] uh my third to last message is
[1346] harmonized data portals are going to be
[1349] around they're still needed I've got a
[1351] picture here of the initial Institute of
[1353] environmental health science uh funded
[1355] project human health exposure analysis
[1358] repository my team I lead the data
[1361] science resource of that which is my job
[1363] is to create an ontology enabled system
[1367] and an ontology to cover all of exposure
[1369] everything you breathe everything you've
[1371] been exposed to and all of your
[1373] potential Health outcomes
[1374] I got a lot of job security
[1377] um and uh but to really provide
[1380] meta-analysis capabilities we're trying
[1383] to pull together all these studies and
[1385] you need precise alignment
[1388] I know that these tools can start to do
[1391] alignment but the Precision of the
[1393] alignment is not there and not adequate
[1395] for making life and death kind of
[1397] decisions on medical interventions that
[1400] might save somebody or that might
[1402] accelerate their death so these
[1405] harmonized data portals they're still
[1407] needed and knowledge graphs and
[1409] semantics are a component of that and
[1413] you know we do things like expose things
[1416] by the different kind of chemical
[1417] Studies by the different kinds of
[1420] conditions
[1421] um lots of counting I know that with Sal
[1425] Khan's advising to chat GPT it just got
[1428] much better at math but it's not perfect
[1430] in that but it's improving but I don't
[1433] think it's going to get you know it
[1435] doesn't have the foundation despite what
[1438] some people are saying that give it
[1440] enough data and these properties emerge
[1442] I'm not ready to buy that I'm I'm not
[1445] disputing that they're getting good
[1447] results but I'm still not ready to buy
[1449] that it's going to be the be all and end
[1451] all of that
[1452] so message 10 hybrid AI Solutions and
[1457] pipelines you know the whole how
[1459] everything fits together provide an
[1461] opportunity here's an image from an IBM
[1464] AI Horizons Network funded project that
[1467] we're working on uh that uh basically
[1470] does precision medicine with a lot of
[1472] different components of AI
[1475] so
[1476] second to last slide I've got a
[1479] collection of the messages
[1481] we shouldn't ignore the accomplishments
[1484] and of large language models and we
[1487] really need to leverage them and more
[1489] than that we really need to jump on them
[1491] and show them and the world how our kind
[1495] of Technology can make a difference
[1497] knowledge graphs can help with
[1499] communication and interoperation they
[1502] can help large language models move up
[1504] the diki pyramid they can provide some
[1508] foundation not enough not all of the
[1510] foundation but some foundation for
[1512] addressing policy and accountability
[1514] needs
[1515] I believe that they can be this marriage
[1518] kind of made in heaven but I think the
[1521] time is now and mostly my potentially my
[1525] biggest take-home message is we need to
[1527] collaborate and create these
[1529] Partnerships or you know there's a lot
[1531] of language like copilot or a virtual
[1534] assistant I think we're in a really good
[1536] place to do that
[1537] and creating these exploration sandboxes
[1540] I think is part of our future assessment
[1543] tools I think are one of the biggest
[1545] opportunities and we need to be hybrid
[1548] so my final messages are collaboration
[1553] is key
[1555] um I want not to be replaced I want to
[1558] partner with AI so that I don't become
[1562] one of those many knowledge
[1563] professionals who is replaced
[1565] and I'm using uh Wendy Hall's phrase of
[1569] the AI scorcher the generative AI
[1572] explosion or in her opinion the AI
[1574] scorcher and I actually subscribed to
[1576] that I think it provides the knowledge
[1578] graph community and I'm including
[1580] knowledge or ontologies Providence web3
[1583] with a unique opportunity to shine and
[1585] then more than that I actually believe
[1588] that if we don't jump on this
[1589] opportunity
[1590] we're going to be left behind
[1593] so with that I'll take questions
[1595] [Applause]
[1602] see Aura ICD and ic1
[1608] thank you for this uh I have a comment
[1611] and I have a question so uh you said we
[1614] could be left behind if we don't cease
[1615] this opportunity I sort of
[1617] when I look at the long span of AI I
[1620] sort of see another kind of opportunity
[1623] here which is that we could truly mess
[1624] things up now uh and I lived through the
[1628] AI winter I've been doing this for a
[1629] long time I lived through the AI winter
[1631] I don't want to do that again
[1634] um so that's my comment my question to
[1637] you is about
[1639] these language models and handling
[1641] derivative work so scenario could be I
[1646] ask uh uh a language model to write a
[1650] song let's say in the style of The Who
[1653] and a song comes back uh
[1657] what are the legal implications of that
[1659] because obviously it has to draw from
[1662] existing work of this uh
[1665] this band uh
[1667] any thoughts on that I love this uh
[1670] actually at the decentralized knowledge
[1672] graph Workshop that was yesterday this
[1673] is one of the discussion points that we
[1675] had
[1676] um where we could pose the a partial
[1679] solution we get it out on a blockchain
[1682] or some kind of decentralized annotated
[1684] uh resource and then we start to add the
[1688] metadata so Aura said this it used this
[1692] resource I really want that in my
[1694] provenance you know I'm going to encode
[1696] it in Bravo but get it encoded in some
[1698] kind of provenance chain so that and get
[1701] it in some kind of blockchainey
[1703] infrastructure so that the world can see
[1706] somebody posted this somebody you
[1709] expanded on this somebody built on top
[1712] of it and somebody used these resources
[1713] so we can get credit and blame
[1718] okay who's next
[1719] unfortunately we're at time I see 255.
[1723] it's 9 30 okay
[1725] [Laughter]
[1730] thank you but it's one Juan wanted to
[1733] ask a question and okay you guys all
[1735] right uh knowledge engineering and
[1738] prompt engineering how do they
[1740] collaborate
[1741] perfect opportunity
[1744] um you know prompt engineering is
[1745] incredibly hot what they're making 300
[1747] 000 According to some headline that I
[1749] saw the other day uh so I I think
[1753] um encoding a smart prompt can be uh
[1757] informed by knowledge graphs and
[1759] semantics and then uh we can get maybe a
[1763] little bit more structure and we can
[1764] start to understand where prompts are
[1766] better and worse so I think there's
[1768] great opportunity there but I don't know
[1770] that prompt engineering is going to be
[1772] enormous in five years I think it's
[1774] going to go away
[1777] thank you very much again Deborah thanks
