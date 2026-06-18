---
schema_version: 1
id: yt-0jDIYzPqZ28
type: youtube
title: 'KGC 2022 Talk: ''How To Build A Customer 360 Knowledge Graph for FinTech!''
  — Gupta & Jere, Intuit'
url: https://www.youtube.com/watch?v=0jDIYzPqZ28
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:38:11Z'
content_hash: sha256:c3d864683ec5690d6d5b05e56074bd1e55bc3f4c068fb529419d74be87e4fcf8
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 1445
  caption_track: cached
  snippet_count: 640
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:11Z'
  user_correction: null
---
[0] Introduction
[0] good afternoon folks
[2] and uh first of all i would like to
[4] thank you and appreciate knowledge graph
[6] team for giving us this opportunity to
[8] present our journey and learning today
[11] uh my name is amit jeri and i'm the vice
[13] president of engineering at intuit and a
[15] lead into its customer identity access
[17] management and c360 platform
[20] capabilities which are part of the
[22] overall intuit platform uh gautam would
[24] you like to quickly introduce yourself
[28] sure uh
[28] Who are you
[31] uh myself like uh
[33] gazan gupta group manager at intuit
[35] primarily working in the knowledge graph
[38] and data engineering technologies for
[40] like uh more than like 20 years and this
[44] talk i'm trying to share like the
[46] learning that i have developed over the
[48] time so that's the thing and feel free
[50] to connect me on my linkedin yeah
[50] About Intuit
[53] okay so right on so uh next slide please
[56] uh
[56] so uh intuit's mission is uh it's pretty
[60] crisp we are a purpose driven and a
[62] value-driven global technology platform
[64] company a mission to power the
[67] prosperity around the world and what we
[68] mean by that is with the innovative
[70] products that we have like turbo tax
[72] quickbooks mint credit karma mailchimp
[75] we help millions of consumers small
[78] business and simply self-employed
[80] customers overcome their most financial
[83] important challenges which are kind of
[85] like pretty near and dear to them
[87] uh moving on to the next slides really
[89] the scale and then the gamut of
[90] customers and businesses that we serve
[93] across the globe is uh it's all about
[95] 150 million plus customers globally
[99] again segmented across small business
[101] simple employed and consumer space as i
[103] was saying earlier
[104] uh through the intuit platform that
[106] powers the multiple to multiple flagship
[109] products and then the it's really a
[112] world-class scale wherein the platform
[114] enables hundreds of billions of money
[116] movement
[117] with the highest possible accuracy
[119] payroll for about 16 million plus
[121] customers 50 plus million customers
[124] across north america actually use turbo
[127] tax to file their taxes uh 100 million
[130] customers with our latest acquisition
[132] with credit karma
[133] manage their financial life through
[135] intuit and credit karma offerings and
[137] then with the
[138] recent acquisition with mailchimp and
[140] then our flagship offering eight plus
[142] million small business owners across the
[144] globe trust with books to manage their
[147] accounting and finances so that's kind
[149] of like the scale uh we are actually
[152] looking at uh and moving to the next
[154] slide so a little bit of a context here
[154] What is Customer 360
[157] before i
[158] uh i touch on what is really c360 i
[160] think all of us probably would know it's
[161] a pretty standard industry technology
[163] term but
[165] primarily uh intuit used to be a product
[167] based company for last several years it
[170] almost like was a different brand per
[172] product but it has been transformed into
[174] a platform company where now we are
[176] delivering consistent and uniform
[177] ecosystem experiences across different
[180] products actually that are powered by
[182] one into platform which is a significant
[184] shift and as you can actually imagine in
[186] the platform world uh
[189] which coralize the customer identity
[191] access management and c360 that's almost
[193] like a keys to the kingdom
[195] so today we will focus on customer 360
[198] component of that so what's really is uh
[200] c360 it's a capability
[202] uh that thousands or with thousands of
[205] data points that define what the
[207] customer is and their relationships with
[209] intuit offerings and their customers
[211] that truly describe them and based on
[213] like what customers expect from us when
[216] they engage with us and then what we
[218] know about customers that really helps
[220] us enable intuit uh strategy uh through
[223] c360 so it's really enables us to
[225] provide experiences that demonstrate
[227] that we can actually demonstrate to our
[229] customers that we know them across all
[231] our touch points not necessarily just
[233] the in-product experiences but like
[235] end-to-end customer success marketing
[237] web properties name any channel and then
[240] that actually helps us like continuously
[242] improve the customer conversion
[243] retention and confidence in our uh our
[246] offering so really the
[248] uh pitch here in the moving to the next
[250] slide algorithm
[250] Financial Identity Network
[253] the uh the vision that actually we have
[256] which is a pretty bold vision
[257] provocation it's like to be that
[260] financial identity network powered by
[262] the knowledge graph for the fintech
[264] industry that's kind of like what we
[266] aspire to be and the graph essentially
[269] indeed is like intuits customers or even
[272] their customers by establishing the rich
[275] connections across customers and
[276] actually as you can think
[278] like beyond so to double click a little
[280] bit on the financial graph strategy next
[283] slide is
[284] there are really three main pillars
[286] the ownership the customers have like
[289] entitlements like their
[291] identity resolution which is very
[292] important like who they are what they
[294] actually say indeed they are and then
[296] their life cycle at every stage of
[298] engagement so ownership
[300] as you can see is really about the
[301] relationship with intuit in terms of
[304] products entitlement subscriptions they
[306] have access to and capabilities
[309] being like able to really verify
[311] customers digital identity against their
[314] real world identity and if you can
[315] actually really figure out uh on top of
[318] it like what stage of engagement they
[320] actually are at i mean you can pretty
[322] much imagine like knowing through the
[324] ml31 insights and learnings and what
[327] their intent is we can really try the
[329] highly personalized and engaging
[331] experiences and that actually we believe
[334] will lead to the network effects
[335] platform that will deliver the value
[337] through the relationships and
[338] collaboration so that's kind of like the
[340] overall uh strategy so how are we really
[345] working on it like next slide please and
[347] then how this is really shaping it up so
[349] in the interest of time uh
[351] i'll just double click on the very high
[352] level architecture i think this is just
[354] one slide but there is like a
[356] infrastructure
[357] people process technology product and
[359] even importantly mindset behind this
[362] we are in the very early stages of this
[364] journey but really on this diagrams if
[366] you start to think from the left the
[369] capability supports like synchronous and
[371] asynchronous modes streaming pipelines
[373] uh standard data lake integration at
[376] scale then we got like attribute and
[378] relationship stores with graphql apis
[381] and here really the bigger shift at
[384] intuitive like we have started to treat
[385] apis as really products and what i mean
[388] by that is like real self-service where
[391] there are like meaningless
[392] collaborations developers are able to
[394] actually discover apis first party
[396] second party third party they can adopt
[398] onboard to them at ease
[400] with like within a matter of minutes
[402] earlier you used to take like days and
[403] weeks so as our services journey we have
[406] matured a lot and then we have an
[408] asynchronous mechanism mechanism to also
[411] engage so uh
[412] customers uh actually for this
[415] infrastructure you can imagine is like
[416] the in product experiences customer
[418] success channels marketing properties
[421] and then the scale because of the 150
[423] million plus customers actually that we
[425] serve and even their customers customers
[427] partner enablement uh we are really
[430] looking at
[431] millions of customers visiting intuit
[433] properties api concurrency is already
[436] hitting like thousands of transactions
[437] per second and uh importantly also the
[441] intuit and then the external developers
[443] uh
[444] are able to actually adopt and bind to
[446] these apis with ease this actually in
[449] turn enables us to
[451] drive hundreds of experiments at scale
[453] to deliver the world-class personalized
[455] experiences something that actually we
[456] are not able to do this uh so with that
[458] overview let me hand it over to my peer
[461] gautam to walk us through the design
[463] patterns for building the customer 360
[465] knowledge graph thank you
[469] thank you amit
[472] i hope all of you can hear me so maybe
[474] like being an engineer at heart like
[477] this is a topic which is very close to
[480] like my heart and i have like you know
[482] worked through kind of my industry
[485] experience to capture these design
[487] patterns to solve for the common
[490] problems that we come across day-to-day
[493] like when we go for designing
[494] architecting for building a knowledge
[496] graph of this massive scale to solve for
[500] like you know our end customers right
[502] so
[503] typically like these are five design
[505] patterns
[506] and to start with
[508] first pattern is about the data movement
[510] whenever we build a graph at that time
[512] we have to feed data into that the data
[514] movement has to take place and in such a
[517] scenario our first reaction is to think
[520] in terms of a pipeline whereas from the
[522] pattern perspective what i've learned is
[524] that to think platform not pipelines so
[528] why platform because platform is a
[530] generic kind of a capability that can
[533] have reusable and configurable stages
[536] for each different kind of stage and we
[538] can plug and play we can build multiple
[541] kind of pipelines just by using those
[543] stages again and again right
[545] second thing is that in a platform we
[547] build a metadata repository that can be
[550] used by multiple like consumers of our
[553] platform to discover the data to
[556] attribute the data right and as well as
[558] to build the trust of our consumers that
[561] only the consented data is being
[563] provided to the end customers or the
[565] specific applications
[567] and
[568] another aspect of a platform is that we
[571] have operational excellence built into
[573] it that rather than like you know piece
[575] by piece adding into a specific pipeline
[578] we can make economies of scale by
[581] creating uh like dashboarding monitoring
[583] alerting those kind of things within the
[586] platform and that way we can have like
[588] very much efficiency while doing the
[591] data movement at this kind of a scale
[591] Data Structure
[595] all right so data has two states one is
[598] i mean data is either moving or it is at
[600] rest right so one pattern was for the
[603] data movement now other is when the data
[605] is addressed obviously a question comes
[607] where do we make the data rest where
[610] what is the data structure right
[612] so here again i have seen multiple times
[614] like through my career that discussion
[616] is happening which is the right storage
[619] uh technology for the data for knowledge
[623] graph what i have learned is that it's
[625] like
[626] no like you know one kind of a
[628] technology that can serve all kind of
[630] use cases so it's good to go for
[632] polyglot rather than a monolithic kind
[634] of a storage decision
[637] so by follicular time means like
[639] normally in programming we talk about
[641] polyglot like python java and all
[643] whereas in data storage polyglot i refer
[646] to that let's say you have a large
[648] amount of attribute data so
[651] for that like which is like a key value
[652] pair you can use a nosql database
[655] like dynamodb mongodb they are very good
[658] for like fast access to large amount of
[660] data for specific entities now then
[663] there is a need for searchable data
[665] which is only on specific fields so for
[668] that we can use something like apache
[669] solar elasticsearch there are plenty of
[671] data bases which serve this specific
[673] purpose right thirdly like if we have to
[677] have relationships which are like very
[679] specific to the large size graphs for
[682] that it's really good to have a graph
[684] database like title graph or like you
[686] know these are the good technologies
[688] that can be used for having multi-hop
[691] queries and getting insights from the
[693] graph perspective like running those
[695] graph queries specifically so this is
[698] like not a comprehensive list like there
[700] are more like technologies we can use
[702] but think in terms of polyglot so that
[705] we don't try to
[707] like you know put all of the features
[709] into one kind of a data storage right
[711] that's the pattern we i mean use it over
[714] the time and as amit mentioned in the
[716] architecture diagram there were three
[718] data like you know storage we are
[720] already using for these different uses
[722] but our end customer doesn't come to
[724] know that from where the data is coming
[726] like so for them it is like seamless
[726] Access Patterns
[730] so moving on once we have stored the
[732] data we have done the data movement now
[734] the purpose of the knowledge graph is to
[736] provide access of this data to a variety
[740] of consumers they can be developers data
[742] scientists data analysts like product
[743] managers so in such a scenario
[747] the pattern is like right for me not one
[749] size fits all
[750] so again here the immediate reaction for
[753] the data access like is that at times we
[756] go for a synchronous like a rest api on
[759] top of that data platform so that anyone
[761] can access it right whereas what we
[764] found is that there are other like
[766] access patterns that if we provide to
[768] the consumers then it can help us like a
[771] very quick adoption of the knowledge
[773] graph as well as like
[775] i mean scalability of the platform so
[778] that overall ecosystem can work like you
[780] know in a very efficient way rather than
[782] like
[783] one team like you know doing a bulk of
[785] work getting all the data from the api
[787] and then looking for some changes kind
[789] of pretty so i'll show you with some
[791] examples one is that
[793] for our
[794] knowledge graph we first built a pattern
[797] of graphql api so graphql api is a very
[800] generic most of you might have
[801] seen it where like let's say we have
[804] 6000 plus attributes and if they are
[806] exposed by a graphql api then any
[809] consumer of the api can specify the
[811] specific attributes and access them like
[813] on their need basis
[815] now
[816] some of our marketing partners they were
[819] interested more into like the changes to
[821] the data rather than like you know
[823] getting all the data i mean through the
[825] api or filtered data to the api they
[828] were more interested into let's say some
[830] celebrity who joins like you know one
[832] specific organization so when they join
[834] the graph of that organization now this
[836] is a new event that has happened so this
[839] event can be published to a specific
[842] topic where our consumers can start
[845] listening and that is the asynchronous
[847] pattern through which we start
[849] publishing uh these change data capture
[851] messages to our end users
[854] okay so that is a asynchronous pattern
[856] so after solving both these we came
[858] across another challenge where a lot of
[861] new consumers are like uh customers they
[864] come and they try to onboard our data
[867] platform for this knowledge graph here
[870] if they start listening to the real time
[872] before that they need kind of a backfill
[875] of the data like what was the historical
[876] thing right so for that backfill
[879] like the earlier options were to use
[881] some kind of a technology from the
[883] specific vendor for like backfill
[886] whereas we realize the pattern is to
[889] build like a reusable replay mechanism
[892] so that backfill can happen from an
[894] offline data store and
[897] cover consumers or like new clients they
[900] can access it by themselves through
[902] these historical bootstraps and then
[904] once they have done the historical
[905] bootstrap the past data they can start
[907] listening into the like they have come
[909] up to the speed and start listing the
[910] latest data also so that is like three
[913] different data access patterns and there
[915] are multiple more like you know which
[918] are still in the open kind of a thing
[920] and over the time like you know i can
[921] share but the key to remember is that
[924] data access is right for me not one size
[926] fits all like we can't just say that hey
[928] we just have an api use it no we have to
[930] solve for the multiple patterns for data
[932] access
[932] AI Integration
[934] all right moving forward like
[937] i hope all of you would agree that ai is
[940] like uh one thing uh which is uh seeping
[943] into every
[944] aspect of our technology right worldwide
[947] so there was a time when we were like uh
[950] working with the
[951] like more or less then microservices
[953] then like big data now is the time when
[957] the ai has to be part of every aspect of
[960] our knowledge graph now
[963] in this aspect
[965] how we think from the pattern
[966] perspective is that since ai is
[969] inevitable it has to be deeply
[971] integrated within the graph rather than
[973] like bolted on or like as a separate
[976] organization right so in this for
[978] example like we have feature store so
[981] like our features that are required for
[984] ai models that can be like created out
[986] of the knowledge graph using the
[988] attribute store using like the different
[991] technologies by which we can create like
[994] aggregation as well as like the
[998] like rich features that can be used
[1000] ready by the data scientists rather than
[1002] they're doing like all the feature
[1003] engineering right so that is one part
[1006] second is that since the knowledge graph
[1008] is being used for kind of a data
[1010] modeling there has to be a like feedback
[1012] loop so that any like ai model's results
[1016] should come back within the same
[1019] graph so that data scientists and our
[1022] business partners they can make a
[1024] decision how a model is performing and
[1026] based on that they can fine-tune the
[1028] model so that has to be deeply
[1029] integrated within that ai part
[1032] and finally like in the ai pipeline all
[1035] the aspects of ai like whether it's a
[1037] training optimization and like i mean
[1039] even training now the trend is more
[1041] towards auto ml so in in such a scenario
[1044] all of that
[1046] has to be we have to think about being
[1048] in the part of this whole platform and
[1050] as a various stages rather than like
[1052] something external which happens outside
[1054] the platform so then only like we can
[1056] let's say we have a graph store within
[1058] that graph store there are capabilities
[1061] to do the graph ammo based uh like
[1063] models so that insights can be taken and
[1066] the model can like start predicting in
[1068] the right way
[1070] all right so moving on like
[1073] this is like the last pattern i would
[1074] like to cover which is on the data
[1077] entities
[1079] here the pattern is like more from the
[1081] user perspective where like uh we treat
[1084] data as a product right so
[1087] whenever we come up with a platform and
[1089] start serving certain needs uh for our
[1092] uh like business partners there there
[1095] comes a long list of like feature
[1097] requests that they wanted like on a
[1100] roadmap
[1101] in this quarter or like in future kind
[1103] of a thing and using agile like their
[1105] favorite option is to take them to the
[1106] product backlog right and how many of
[1108] you agree that like product backlog is
[1110] something like which we look only like
[1113] once a quarter or like very few times
[1115] kind of a thing and it's always like you
[1117] know very difficult to prioritize things
[1119] uh rather than the current uh items
[1122] which are high priority we are working
[1123] on it right so in such a sense we can't
[1126] starve our uh and customers from this
[1128] perspective for that purpose the pattern
[1131] is that to introduce self-serve in this
[1134] whole ecosystem from the beginning
[1136] itself
[1138] so when we have self serve there it
[1140] means like no code or low code kind of
[1142] engineering where anyone like you know
[1144] even a product manager data analyst or
[1146] like your business person they can come
[1149] they can define like you know
[1151] relationships attributes within that
[1153] graph they can run their own like you
[1155] know models so all of that they can do
[1158] as a self-serve so there is no need to
[1160] develop specific features only for
[1162] serving uh like that specific kind of uh
[1166] customers needs so that is one part and
[1169] other part is that we introduce kind of
[1172] an inner source where our partner teams
[1174] they are welcome to contribute to the
[1177] platform if they need any new feature so
[1180] using that the whole development gets
[1182] scaled so that is how like the whole
[1184] platform gets adopted very fast as well
[1187] as it becomes like you know scaled up so
[1189] that multiple type of use cases
[1191] innovations can take place by like
[1194] different variety of personas
[1196] so i i find like myself successful when
[1199] any like you know business user with
[1201] like like no technical knowledge they
[1203] can also come and on board to our
[1206] knowledge graph to discover the data to
[1208] like you know run their use case as well
[1210] as like to propose like a new kind of uh
[1213] like experiments they are planning to do
[1215] for that in a self-serve form
[1218] so so these are the like top five
[1220] patterns uh that over the time we have
[1222] developed and that's what i wanted to
[1224] share with you yeah
[1224] Questions
[1226] i think with that like i think uh that's
[1228] all from our side and if you have any
[1231] questions feel free to like
[1233] put it in the chat and we'll be happy to
[1235] answer
[1249] yeah i have uh some question okay for
[1252] let me take some question from rashmi uh
[1255] can i have access to the presentation of
[1256] course like you know there is a link for
[1258] presentation please feel free to
[1259] download from there
[1261] then there's a question from ying uh on
[1264] how to efficiently query both the
[1266] document store and the graph stored
[1268] simultaneously in the run time yeah so
[1271] how
[1272] we are solving this problem is
[1274] that we have come up with a orchestrator
[1278] uh which is based on graphql
[1282] uh can you can you hear me
[1286] yeah okay so so we we have like an
[1288] orchestrator using that orchestrator it
[1291] can like you know redirect the queries
[1294] which are coming from the document store
[1295] as well as from the graph store so that
[1298] for the end customer it is like a
[1300] consumer of our api it is seamless that
[1302] orchestrator does all the work behind
[1304] the scenes to pick the data from the
[1306] document as well as the graph store and
[1308] to solve for that right
[1312] yes so i hope that answers the question
[1314] here
[1316] yeah so
[1317] my question is around
[1319] your low code environment for product
[1322] managers
[1323] i'm just wondering how those managers
[1325] edit or author the data
[1328] do you what use specific ui tools
[1331] frameworks is it
[1332] just editing data directly how exactly
[1335] do you do that
[1337] right so so for that like we have a
[1341] homegrown like ui and i mean within
[1343] intro like we have a big ecosystem uh
[1346] through that all the services are
[1348] through a specific common infrastructure
[1351] from where like we call it like dev
[1352] portal so using that anyone can access
[1355] any of these services and through that
[1357] we expose a ui where the metadata is
[1360] exposed to all the business users right
[1363] in the metadata business users can go
[1366] and they can like you know create like
[1367] experimental attributes they can make
[1370] changes in the attributes like but of
[1372] course we don't allow the editing of the
[1374] like the and data it's more about the
[1376] metadata that can be edited whereas the
[1378] end data comes keep coming from the real
[1380] time flows so but like that metadata is
[1383] fully like you know repository is a
[1384] self-serve kind of a thing that we have
[1386] developed right
[1388] and if i can just like add one point
[1390] at an uber level is
[1392] uh there has been a significant shift at
[1395] intuit in terms of the self-service
[1396] maturity model uh regardless of the type
[1399] of the assets it could be services
[1401] library mobile native libraries desktop
[1403] ecosystem or data models so as uh gautam
[1406] was saying the everything in terms of
[1409] self-service experiences through paved
[1411] roads uh is standardized on the dev
[1413] portal where the
[1415] developers actually are pretty much get
[1417] to do most of their stuff like on their
[1420] own and then the velocities are like top
[1421] of programs
[1424] all right well let's uh give an applause
[1426] hopefully you can hear us virtually uh
[1428] thank you very much um
[1430] gautama i i i thought you were going to
[1432] be here physically but in half an hour
[1434] have the panel so hopefully you can join
[1436] and you can join us virtually for the
[1437] panel
[1439] sure sure i'll be happy to join that
[1440] right thank you very much so our next
[1442] speakers we have them here so sarah and
[1445] thomas from enterprise knowledge
