---
schema_version: 1
id: yt-Q1aji4uJJgc
type: youtube
title: KGC 2023 Talk — Using Knowledge Graphs for Navigating Data Assets by RelationalAI's
  Márton Búr
url: https://www.youtube.com/watch?v=Q1aji4uJJgc
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-18T01:38:25Z'
content_hash: sha256:f4ea3354a7e1e99f8d95b66dc8b979cfb2405eb089682c0d11dfd49466ca7e1e
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 1375
  caption_track: cached
  snippet_count: 548
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:25Z'
  user_correction: null
---
[0] and I will discuss our feature that is
[4] called the semantic search which helps
[7] users of the semantic layer explore
[9] parts of the ontology that is of
[11] Interest
[12] these ontologies can grow pretty big
[15] especially for uh for large Enterprises
[18] so it's useful to have this thing and
[21] then I'll go on and discuss how to weave
[24] the data into the ontology and
[28] the problem I will focus on is
[32] how to verify the trustworthiness of a
[34] semantic layer which is that how to know
[37] that the results that we are getting
[39] back from such a layer is actually
[40] accurate and this containing the data
[42] that we want and the solution we provide
[45] is some sort of a Geodon capability from
[48] a conceptual level to to the physical
[50] level so um I'll try to I will
[53] demonstrate it in a live demo if I have
[55] I have enough time for that
[57] okay so uh
[61] um somatically is essentially a set of
[63] hierarchical views that present the data
[66] in uh in in some form to the user and
[69] such a layer allows the user to express
[73] queries in terms of business Concepts
[76] relationships that are familiar to
[79] domain experts rather than referring to
[82] explicitly referring to physical layer
[85] names such as table or column names
[89] and the semantic layer is also allowing
[93] some sort of flexibility in terms of
[95] defining defining the views that that we
[99] that we can use to look at look at our
[101] data
[104] there has there has been a lot of ideas
[107] and approaches developed for uh for
[110] creating semantics and model creative
[113] models for the domain and this category
[115] we can categorize these as such as you
[117] can see in the slides so there are
[119] proposals which are which we which we
[122] call the SQL first
[124] DBT and Malloy for example there is also
[129] Knowledge Graph based the data catalogs
[131] and the data Fabrics there are also
[134] industry proposals legend or more field
[137] Legend is by Golden Sex Morpheus by
[139] Morgan Stanley and then we can also talk
[142] about a standard standards so um
[146] semantic web is one big standard and
[150] sbvr is by OMG
[153] and today I'm going to
[157] call out this this note here that
[160] relational AI is actually powering any
[162] of these approaches so it's it's it's up
[164] to you which one you want to go with
[167] um this uh this knowledge graph
[168] management system we have is actually
[170] able to support you so um in this talk
[173] I'm going to be using a modeling
[177] approach that is very close to the sbvr1
[179] in fact many of the people who are on
[182] the board of the sbvr committee have
[186] created this modeling language this is a
[189] visual modeling language called
[192] um
[193] objects or modeling
[194] it is basically
[197] giving us a visual set visual tool set
[199] for representing ontologies domain
[202] Concepts and relationships there is a
[204] good to support for creating these
[207] models in my opinion Norma is is really
[211] following this principle of do one thing
[213] but do it well and gives us a good tool
[216] to create these domain ontologies
[219] um it also has very good support for
[221] normalization which is especially useful
[223] when creating models and working with
[226] the business users and there is some
[228] adaptation in the industry one big user
[232] of form is um is the European Space
[234] Agency
[236] foreign
[238] so let me just briefly walk you through
[241] this example ontology that I will use in
[243] my presentation and this is basically
[246] presenting a domain where we want to
[249] keep track of some customer data but
[252] when they are build what they are built
[255] for what kind of products they have
[256] purchased what kind of subscriptions
[258] they have and inform we can represent
[261] concepts by using these rounded
[262] rectangles such as Bill or a line item
[265] as you can see it here on the slide and
[267] you can have relationships between them
[269] in which
[271] these Concepts can play or play a roles
[273] in so for example if you look at line
[275] item and build between these two
[277] concepts there is a relationship called
[279] is part of and you can easily verbalize
[281] this relationship as if you read it in
[283] the direction of
[285] of the Roll order line item is part of a
[288] build so
[289] um and and in addition to that I'm not
[292] going to cover but gives you form gives
[295] you a very good set of um of constraints
[298] that you can that you can use to to
[300] supply to your to your domain models
[303] on the other hand we have our data
[305] living in the model data stack uh in
[308] some some physical form and what we want
[311] our
[312] our semantic layer to do for us is to
[315] make this connection between the domain
[317] Concepts and the physical presentation
[320] of the data so that we don't have to
[322] find out how exactly we should be
[325] referring to the data we can use the
[327] concepts that are coming coming from the
[329] from the domain
[331] however like I said it is still it still
[335] can be a it is often very tricky to find
[338] out uh what parts of the domain are
[340] interesting for us so there should be
[342] some tool that allows us to explore the
[344] ontology that we that we are working
[346] with and for that we have come up with
[350] what we call a semantic search which is
[352] exactly doing this is a tool to explore
[354] the ontology of the business domain and
[357] um
[358] it provides the vocabulary for for the
[360] search queries for the semantic search
[362] queries
[364] um and the output of this search is
[365] basically a list of precise names
[366] Concepts uh relationships of Interest
[369] which are familiar to two domain experts
[374] so how does this how does the semantic
[376] search query look like so sticking with
[378] this example we can just say that I am
[381] interested in
[382] exploring the ontology the part of the
[385] ontology that has
[387] some parts related to to build to build
[389] a concept and then we get a result where
[393] the ontology is expanded in a way that
[395] we are presented with all the
[397] relationships that build as a concept is
[399] playing roller
[401] and um now we have uh two uh two uh
[406] relationships presented for us so we can
[408] go on and further expand this part of
[411] the ontology and use line item is part
[414] or B relationship to navigate uh further
[417] and see more of the ontology without
[419] actually having to understand in detail
[422] uh all the rest of the rest of it
[428] um the semantic search work has been
[430] already published last year at the
[432] models conference so I'm not going to go
[434] into details for that if you're
[435] interested in this kind of work uh
[437] please take a look at the paper
[441] but it was a good feedback and
[443] validation for actually a need need for
[445] this kind of tool and we were happy to
[448] happy to present that
[450] okay so uh in in addition to having uh
[454] this tool that can help us explore the
[457] ontology of course we need to somehow
[459] make sure that we uh also weave the data
[463] into the into the semantic layer not
[466] just have the the concepts the
[468] conceptual model uh in the in the
[470] knowledge graph so um
[472] again what's the motivation for having
[474] this um having such semantic layers one
[477] of the major motivation is as it was
[479] called out in the in the keynote just a
[481] few minutes ago there is a there are
[484] many data silos at the large
[486] International companies
[488] um manage myself managed by several
[490] teams using several different approaches
[492] so synchronization change propagation
[494] and duplication is is always a problem
[496] so um
[498] we would like to have uh all the data in
[501] a semantic layer that can provide that
[505] can provide views and manages all these
[508] or solve these these synchronization and
[510] and other kind of problems
[514] so uh how we can view this Source data
[517] into our ontology and
[520] for that we have these declarative rules
[522] that are in addition to being
[524] declarative they are also executable so
[527] this is one nice thing about using a
[530] relational Knowledge Graph management
[531] system is that we can adhere to this
[534] principle where we say model is the code
[536] and if we follow some number of some
[540] small number of weaving patterns then we
[542] can ensure that um when we write these
[545] rules we can analyze these rules and
[547] figure out to what degree we have both
[548] in our data sources into the semantic
[550] layer and what how much work is still
[553] still to be done
[555] so let me give you an example for such a
[558] weaving Rule and um here on this slide I
[561] call out a small fragment of the
[563] ontology
[564] that I presented earlier so here we have
[566] a line item that charges some amount and
[570] here in this piece of rail code you can
[573] see that we Define the value type amount
[577] we also defined a set of line item
[580] entities and then we describe the
[582] definition of how this line item charges
[585] amount relationship should look like and
[588] how we weave Source data into uh into
[591] this um this relationship
[594] and it's not very uh
[597] it's not very difficult to see that
[600] the definitions definitions on top
[602] correspond to the concepts in the
[605] ontology and this definition
[607] here in the middle is actually a
[610] definition for the relationship and now
[612] here in this simple case we can we can
[615] easily see the source columns that we
[617] used to create this create this
[620] relationship
[621] and that's exactly what we are
[623] interested in is to make this connection
[625] between
[627] um the conceptual level and the physical
[629] physical layer and if we write these
[632] kind of rules and we support this with
[635] um an analysis tools that can read these
[639] read these rules that we have defined
[641] and give us a report what
[643] um
[645] sources were were evolving into what
[648] concepts and what relationships
[650] so
[652] we have this weaving approach but the
[655] problem is that still these might
[658] contain errors so maybe someone made a
[661] mistake wrong information was used when
[664] creating the relationship so in order to
[667] be able to gain trust in the semantic
[669] layer we need to have the ability to
[671] explore the ontology which is the
[673] provided by the semantic search so the
[676] semantic search queries and also drill
[678] down so that we are able to understand
[680] that a certain concept or relationship
[682] is populated from what data sources so
[685] the added value of this approach is that
[687] we can rapidly explore the domain and
[690] increase trust in some in our semantic
[693] layer
[694] and I would like to briefly uh switch to
[697] the
[698] switch to this live environment
[700] and give you a quick
[703] demo how this works but before I jump
[706] into it I would like to go back to the
[708] uh
[709] ontology so this is this is the um
[713] this is our domain model some small
[715] domain model and
[718] what you see here is the actual console
[721] that uh
[722] that with which you can easily interact
[724] with the relational and Knowledge Graph
[726] management system so I loaded the
[728] ontology already into this knowledge
[729] graph and I have the data also available
[734] so the data is also loaded
[737] and have defined I have defined a couple
[740] of a couple of these mentioned weaving
[742] rules
[743] following these patterns that I
[745] mentioned for weaving
[747] um to populate the the the the semantic
[750] layer so
[752] again here I have the line item here I
[754] have the build concept there is this
[756] relationship line item is part of build
[758] and then if I go here line item I can
[762] see that yes here is this line item
[765] entity
[766] which is basically a concept and here I
[769] have this definition of line item is
[771] part of this part of a build and then
[775] this weaving rule I have the uh
[779] the actual names of the sources so the
[783] layer is populated from these two
[784] columns
[787] um
[788] and then if I go back to my query window
[793] I can run this first query which is
[798] about starting from the concept line
[801] item and I can expand one step at a time
[803] by the ontology that we have so
[807] we can see here that line atom is
[809] playing or playing a role in these four
[811] relationships and if I want to navigate
[814] towards uh the the build concept I can
[818] add one more parameter
[821] and then drill down
[824] in the
[826] in the ontology and then you can see
[828] here
[829] that it's further unfolded and we could
[833] continue this navigation and explore the
[835] parts of the ontology and then on top of
[836] this
[837] what we also have is these drill down
[840] queries so now that we actually
[842] discovered the concepts and
[843] relationships that we would like to use
[845] we can now go ahead and get information
[847] about where where are these uh
[851] relationships populated from and here in
[853] the tooltip I'm sorry it's a little uh a
[855] little too small font size
[857] um you can see that um
[859] this relationship is actually coming
[861] from the sales table bill ID column and
[864] the sales table line item id columns so
[867] if you want to verify that this is
[870] actually populated from the right right
[873] sources then you can do it with this
[875] with this help and again these um this
[878] information is synthesized by reading
[881] the rules that we have written once and
[883] then this this query this drill down
[886] query will actually understand and
[887] presents us
[889] the data lineage for for that particular
[892] relationship so what I mean by that is
[895] that now I can go ahead and
[898] can be sure that I'm getting back here
[900] navigating through this this
[902] relationships I'm actually getting
[906] the data I am looking for so I can list
[908] now for example all the bills the
[911] building dates and what line items
[913] belong to that without that that
[914] particular build
[920] um so yeah uh that's um that's
[922] about it that's what I wanted to show
[925] you uh today so as a summary
[928] um relational knowledge graphs uh By
[931] Nature have S with it for implemented
[933] semantic layers
[935] um semantic search makes it easy to
[937] scope down through the part of the
[939] ontology that we are actually interested
[941] in and the ability to link the
[943] conceptual level to physical uh level uh
[946] it helps
[947] verifying that the semantic layer is is
[951] correctly productively populated
[953] so uh thank you so much
[965] so I'm not sure so it flips to me like
[969] essentially
[970] you've mathematology to a relational
[973] database and you use the the
[975] relationships in anthology
[978] to understand Semitic relationships
[981] lately I guess what I'm trying to
[982] understand is how is this different from
[984] what we often do we map for relational
[986] database to an apology what what's the
[988] what's the semantics of the semantic
[991] search or is there so here what we are
[995] doing is writing this mapping but this
[997] mapping is also executable so you load
[999] it into your semantic layer and it
[1001] doesn't need then the data source
[1002] doesn't need to be a relational table it
[1006] can be a Json it can be any kind of data
[1008] source that you store in that you store
[1010] in the modern data stack so in this
[1012] example I was using the tabular format
[1014] data but in principle you can use it
[1016] uses drill down queries to identify
[1019] whatever data whatever data sources you
[1021] have
[1023] the key thing that you're doing here is
[1025] you're saying here's an ontology I'm
[1027] mapping it to the relations that are in
[1029] my in my
[1031] structured data and as a result we get
[1034] the ability right but but the mapping
[1036] but the mapping is executable
[1039] so it's all it's actually populating
[1041] your your semantic layer so when you run
[1044] the queries that's not running directly
[1046] in your database it's running in the
[1048] knowledge graph management system
[1051] I mean this should be a surprise to this
[1053] community's community this is a lot this
[1056] is just another way of
[1058] accomplishing it and uh sort of uh
[1061] giving the not you know we didn't get
[1064] into it today with the knowledge graph
[1065] engine has the ability to run a variety
[1068] of queries that are easy to run in SQL
[1070] you know for example graph queries or
[1073] recursive queries or other queries that
[1075] would be harder to do in a sequel only
[1078] implementation
[1079] right thank you so you get kind of a
[1081] virtualization of the graph
[1084] the graph shows up as a set of
[1085] materialized views uh inside of a system
[1088] that's not
[1090] like so
[1092] um
[1095] processor and you get uh
[1097] the the graph is reference
[1100] relational database in a highly
[1103] normalized environment called graphical
[1105] form
[1106] and you can
[1109] do these transformations in SQL if you
[1111] like or you can do them in a
[1115] reasoning language rule language
[1122] right
[1123] there's a question behind me as well so
[1125] you're kind of building on that one of
[1127] the things that
[1129] I believe
[1131] generating relational databases is
[1133] always harder than one would think it
[1136] ought to be just
[1137] is is that kind of handled by the
[1140] creation of this semantic layer so that
[1142] if you're if you are essentially pinging
[1145] to the different relational databases
[1147] it's all
[1148] handled by the
[1151] National AI platform
[1153] so yeah you you have full control in
[1156] your weaving rules what you're giving it
[1158] with what concept and you can have
[1159] multiple data sources for for one single
[1162] relation and then you will you can
[1164] report out that what are those sources
[1167] so it doesn't necessarily need to be one
[1169] unique so it can be can be multitude of
[1172] data sources
[1173] I can also add so this is a federation
[1176] model where the data States and
[1178] databases and you Federate a password we
[1181] we don't see that as much in Industry
[1183] now I think it's sort of a new mode
[1185] of working where because you have these
[1187] super scalable Cloud databases like
[1189] Snowflake and bigquery and so on where
[1191] people we see people doing is just
[1193] taking data from a thousand or ten
[1195] thousand different SQL databases and
[1196] pouring it all into uh
[1198] into Snowflake and so there is no
[1200] Federation anymore they're using as a
[1203] first cut SQL and tools like DBT to
[1207] transform and clean
[1209] the data in place so that they can serve
[1213] you know bi tools and spreadsheets and
[1215] dashboards and data apps all from like a
[1218] progressively more refined model the
[1220] issue is SQL has its limits in
[1222] expressivity as I tried to hand out
[1224] earlier and so can you use more
[1227] sophisticated relational languages to
[1230] express more sophisticated semantics
[1232] right like if you had the you wanted to
[1234] express transitive closure or you want
[1236] to express some uh you know connected
[1238] components analysis or between the
[1240] centrality or if you wanted to do what
[1243] you saw earlier uh talk about simulation
[1246] or maybe doing prescriptive analytics
[1249] all of these things are just not native
[1251] to SQL engines like uh stuff like in
[1253] bigquery and so
[1255] by plugging into them and extending them
[1257] with a stored relational language now
[1259] you can express these semantics directly
[1262] there as opposed to having to leave and
[1264] go somewhere else or Federate and you
[1267] know Federation obviously has its
[1268] advantages but for um you know it has
[1271] its also its limitations right because
[1273] you gotta
[1274] you know sometimes you have scalability
[1277] issues
[1278] okay
[1280] [Music]
[1285] have a quick break or please stick
[1287] around and Mom will be here to answer
[1288] questions
[1290] about the paper
[1303] I think the theme for this afternoon is
[1305] different approaches of this idea of a
[1308] cement declare so it's great to have PPT
[1309] on board I think they've brought this
[1311] idea to the mainstream and are starting
[1315] to think Beyond just the sequel being
[1317] the language right so they've announced
[1318] SQL plus python support for expressing
[1321] semantics but obviously when you go to
[1323] python you're now back in procedural
[1325] programming land and so uh uh maybe SQL
[1328] plus python plus a language like this
[1330] and then I think Steve is going to be
[1332] giving talking about more fair which is
[1334] a yet another cut
[1336] on this idea so really interesting space
[1340] and I think a key to adoption of a lot
[1342] of the ideas of this community in the
[1344] mainstream because so many people have
[1346] so much data in systems like stuff like
[1348] they've got to create an ontology or a
[1351] data model of some kind to sit above it
[1353] to make it coherent people it's just too
[1355] much too much complexity to have every
[1358] bi user go navigate 10 000 data months
[1361] true
[1363] this is very true
[1366] okay so you know we've got to get it one
[1368] way or another so get the ideas
[1375] all right all right we have five minutes
