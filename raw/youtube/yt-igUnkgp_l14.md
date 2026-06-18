---
schema_version: 1
id: yt-igUnkgp_l14
type: youtube
title: The Semantics of a Semantic Layer by Dave Mariani
url: https://www.youtube.com/watch?v=igUnkgp_l14
authors:
- AtScale
ingested_at: '2026-06-18T01:38:20Z'
content_hash: sha256:0db8f175103bf352615bd1c29a736e35fdfcd8a4ad977fe29d40153686b08f0b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: AtScale
  channel_url: https://www.youtube.com/@AtScale
  duration_seconds: 1235
  caption_track: cached
  snippet_count: 496
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:20Z'
  user_correction: null
---
[0] foreign
[4] s today where we're going to obviously
[6] be talking about the semantic layer but
[8] we got to start with some definitions
[10] so let's dig into it
[13] you know what one of the best
[14] definitions of a semantic layer comes
[17] right from Wikipedia you do a Google
[19] Search and this is on for semantic layer
[21] and this is what's going to pop up and I
[23] really like this definition because it
[25] has some key words that we should really
[27] be aware of so first of all
[30] a semantic layer is a business
[32] representation of corporate data so
[36] business being sort of the key word in
[39] that sentence
[40] the second path of the second sentence
[42] is it helps users access data
[44] autonomously
[46] autonomously means self-service so a
[49] semantic layer is a business
[50] representation of data that promotes
[53] self-service
[54] and then finally
[56] common business terms so that means
[59] everybody's speaking the same language
[62] so really that really sums up what a
[64] semantic layer is is doesn't it it's
[67] about speaking the same language about
[70] promoting self-service and to make sure
[73] that uh the physical data in the
[76] Enterprise is represented as a logical
[78] and business friendly analytics ready
[81] data store
[82] so let's talk about what a semantic
[85] layer means when it comes to value for
[87] the business
[88] well first a semantic layer provides
[92] control consistency and Agility to
[96] deliver data products to the business
[98] now if you look at this chart over here
[101] to the right what you're going to see is
[103] basically in the before picture you're
[105] going to see what my infrastructure
[108] looked like when I was running analytics
[110] for Yahoo
[111] you can see that there's a bunch of
[113] different data consumers all with their
[116] own built-in semantic layers you can see
[118] that there's a bunch of data stores from
[121] data warehouses to a proliferation of
[124] data Marts to the data Lake we invented
[127] Hadoop at Yahoo
[128] and you know what I had to make big data
[131] small every day and you know what we
[134] couldn't decide as a company what the
[136] definition was of an impression or a ad
[140] click
[141] everybody had their own terminology
[143] everybody had their own definition and
[146] obviously their own reports and
[147] dashboards so ultimately there was a
[151] real lack of trust in the data and the
[153] analytics that we were using to run the
[155] business
[157] so what I wanted was a single source of
[161] truth I wanted the semantic layer not to
[164] live in the applications themselves not
[166] to live in the visualization
[168] visualization tools I wanted them not to
[171] live in the data platforms because we
[173] know we have many consumers and we have
[176] many data sources
[178] so with the semantic layer we can take
[181] out that business logic have it live by
[184] itself
[185] um and that way we can plug and play
[187] when it comes to how you consume data
[189] and also where that data comes from
[192] we also have the added benefit of
[194] abstracting away all that complexity
[198] so the business user or that data
[200] scientist or that application developer
[202] can use data without having to
[204] understand where it came from or how to
[206] actually write code to get access to it
[210] so where does a semantic layer fit in
[215] the Enterprise data stack
[217] well you can see it's going to sit in
[219] between your data consumptions and your
[223] data layers your data platforms your
[226] data stores
[227] so let's just start with the consumption
[229] side at the top here
[231] you can see that we have obviously we
[233] have business analysts who are using bi
[237] tools like Tableau and power bi and
[241] Excel and looker and they need those to
[244] look at data to make decisions to do
[247] historical or descriptive type of
[251] analysis diagnostic analysis using their
[254] tools and they need to speak protocols
[256] like SQL but not just SQL but MDX and
[260] Dax as well so it's not good enough just
[263] to have SQL because tools like Excel and
[266] power bi want to speak xmla to be have a
[271] live direct connection
[273] now what about data scientists
[275] well they need a different interface
[277] don't they they need python for their
[279] Jupiter notebooks and their automl
[281] platforms and you know what they're not
[283] just reading from data not just reading
[286] the semantic layer they're now
[287] generating new predictions so now
[290] they're doing predictive and
[291] prescriptive analysis and they need to
[294] write that back so that the rest of
[296] their Community as well as their
[298] Partners in the on the business side can
[301] use those predictions to make decisions
[303] well the semantic layer is that
[306] connective tissue it's that glue to
[309] bring together those teams so now the
[312] business analysts don't have to just do
[314] descriptive and diagnostic analysis now
[317] they can combine that analysis with
[319] predictive and prescriptive on behalf of
[322] their Partners the data scientists who
[324] are generating and writing back these
[326] new predictions
[327] and then finally we can't forget about
[329] the application developers because
[331] they're going to embed those analytics
[333] into their business systems
[335] um and into their applications and that
[338] means that they need to have a whole
[339] nother set of protocols they need to
[341] access that semantic layer with rest and
[344] with odbc and with jdbc
[346] so as you can see on the consumption
[348] layer it's not one size fits all for a
[352] semantic layer to really work for the
[354] Enterprise it needs to be Universal and
[357] not just Universal from a data
[359] perspective but Universal from a
[361] protocol perspective
[362] so a SQL access is not good enough
[366] now what about on the back end well on
[369] the back end it needs to plug into all
[371] your Enterprise data whether that lives
[373] in a data warehouse whether it's on-prem
[375] like an oracle or a teradata or it's in
[378] the cloud like a snowflake or a bigquery
[380] or a redshift it needs to access your
[383] data Lake whether it be data bricks or
[386] whether it be spark it needs to get
[388] access to that data that's raw and in
[390] the data Lake and it needs to surface
[391] the data in the in the SAS applications
[394] like a sales force or a servicenow
[398] that's a really complex environment and
[400] the semantic layer can tap into that
[402] present a logical mashed up view of all
[406] those individual data sets so that the
[408] data consumers can consume that logical
[411] business data without worrying where it
[413] came from
[414] and it's not good enough just to just to
[416] do all that we also need a data catalog
[418] to help make the semantic layer findable
[421] and searchable and accessible by a wider
[425] range of users and so it's really
[426] important for the semantic layer to
[428] communicate with the Enterprise data
[430] catalogs so that metadata can be shared
[432] in a data fabric style
[435] so what is then the value of that
[438] semantic layer well it all starts with
[440] the data model
[442] and then this data model this is where
[444] we're actually going to create that
[445] logical view of data and it's really
[448] important for the data model to be
[450] dimensional it's got to have measures
[454] and dimensions and calculations for time
[456] and it needs to have hierarchies so you
[458] can drill down from uh from a summary to
[462] a detail and so it needs to be
[464] expressive enough that you can
[467] embed the logic of the business into
[471] this semantic model
[472] so once you have that semantic model
[474] created now it can be consumed in a very
[478] easy way without having to force your
[480] Tableau users to import data or create
[483] data extracts they don't need to
[486] understand the physical data they don't
[488] need to remodel the data in tableau
[491] and the Excel users it hates Excel users
[495] but that's that doesn't need to be so
[497] because if you have a live connection to
[499] the semantic layer we're not talking
[501] about spread marks or dumping data into
[504] Excel we're talking about using live
[506] pivot table connections we're talking
[508] about creating cells that map back to
[511] the semantic layer that that that are
[513] embedded in the Excel worksheets and in
[515] those models so there's no need to to
[519] kick the Excel users down the road
[522] and what about the power bi users well
[524] power bi is a very popular visualization
[527] platform and it needs to access data
[530] live to be really really powerful and it
[532] needs to do that with Dax so with a
[535] semantic layer no more creating more
[537] models in power bi those power bi users
[540] can instantly connect and build their
[543] dashboards and do their analysis and
[546] what about looker you know looker Works
[548] off of look ml well that semantic layer
[551] needs to also be compatible with other
[553] metric languages like lookaml and with
[556] that we can have one semantic layer and
[559] one semantic model to feed them all
[562] this just covers the bi Persona imagine
[565] the data science and application
[567] personas as well doing their same things
[569] with their own tool sets that's really
[571] the power and the value of that semantic
[573] layer
[575] so what are we going to use a semantic
[578] layer for well there's really sort of
[581] the way I think about it there's like
[583] four different sort of use cases
[585] the first and most popular use case
[587] today probably is just uh Cloud
[590] analytics it's it's really migration to
[593] the cloud data platforms a lot of
[596] companies have either moved or in the
[597] process of moving from on-prem to the
[600] cloud for their data pipelines and for
[602] their data and analytics Stacks what
[604] that means in that new environment you
[606] got much many more users who can drive
[609] more costs and also create some
[612] Performance challenges a semantic layer
[615] can be an excellent solution to managing
[617] those costs and also managing those
[620] performance across all your applications
[622] and all your consumers
[625] another great uh use case is an
[628] Enterprise metric store
[629] so uh being able again to house and
[634] centralize the definitions of the
[636] business in one location so no matter
[639] how it gets consumed revenue is revenue
[642] gross margins gross margin regardless of
[644] of of of where you you access it or
[648] where you embed it into a dashboard
[650] report or into a machine learning model
[654] another great use case is bridging Ai
[656] and bi so we talked about the power of
[660] combining descriptive and Diagnostic and
[663] prescriptive and predictive analysis all
[666] in one platform
[667] well the semantic layer can be that glue
[670] there's no need to have silos of data
[673] science they're separate from your
[676] business analysts they can share and
[678] collaborate and the semantic layer is
[681] that collaboration point
[683] and then finally
[686] olap has never really gone away I know a
[689] lot of people would like to see it go
[690] away but the business demands that ease
[693] of use and that speed of access for
[695] analytics so if you got applications
[698] like SQL Server analysis services or
[700] cognos or business objects you don't
[703] have to throw the baby out with the bath
[705] water you can allow your users to have
[707] that functionality but to do it in a
[709] modern safe and secure environment in
[713] the cloud and a semantic layer is an
[715] excellent choice for for bringing those
[718] users into the Modern Age
[722] okay so let's talk about data mesh and
[725] we're going to be talking a lot about
[727] data mesh today in some sessions so I
[729] encourage you to to dive deeper here
[732] um but in a traditional data mesh type
[735] of of architecture
[738] um what you see is that uh a goal and
[741] data mesh is not a technology first of
[743] all it is a it is a an organizational
[746] principle
[748] and you know in in in in the historical
[751] uh terms we've you know we've tended to
[754] think about delivering analytics to the
[757] business as a monolithic sort of our
[759] process where you have a centralized
[762] data team or a bi team who are Doling
[765] out uh data sets and Analysis to the
[768] different business users and business
[769] groups and in this example I'm using
[772] sales finance and marketing
[775] so the problems with that traditional
[777] approach is that it's just not fast
[779] enough for business and it's also really
[782] difficult for a data team to understand
[784] all the nuances of finance of marketing
[788] and sales they can't be business experts
[791] in every business domain that's what the
[793] business users are for that's what
[795] they're good at they understand their
[797] own business and they should be able to
[800] author their own data products
[802] well that's where data mesh comes in
[805] data mesh really allows the business
[807] users the domain owners the data
[809] stewards in their own domain to control
[812] and create those data products
[814] but there's one problem with that
[817] you can see that it leaves out the data
[819] team the data team can focus on maybe uh
[823] the the platforms and the standards and
[826] the technology but they're really not in
[828] control or able to manage uh that that
[832] interaction between the different data
[835] domains so what can that result in well
[838] it can result in the same chaos that
[840] we've been dealing with over the past
[842] couple decades with the self-service bi
[844] Revolution where it's a free-for-all and
[847] everybody does their own thing
[850] well that doesn't need to be the case
[851] and this is where the semantic layer
[854] really can help in a data mesh style
[857] architecture and it really comes down to
[860] the semantic layer repository because
[863] that means that the repository means
[866] it's an area where we can share business
[869] definitions in the form of a semantic
[872] model
[873] so what do I mean by that
[875] well first of all you can see that the
[878] the data team or the centralized team
[880] gets back into play here
[883] and they may for example create a
[885] conformed Dimension like the time
[887] dimension and that's important because
[889] now if we have a common calendar now we
[892] regardless of what the data is or how we
[895] roll it up everybody is using the same
[897] definition of time I know that may seem
[900] trivial it's not
[903] um and uh believe me I had so many
[904] problems about rolling up data in
[906] different time periods and with with a a
[909] data mesh and a semantic layer you can
[911] have a conformed Dimension that then
[913] gets used by the data domains so now
[917] marketing is can create their own
[919] campaign Dimension because they can own
[921] that because they understand campaigns
[923] and they can combine that campaign
[926] Dimension and that time Dimension to
[928] create a campaign model
[930] so now marketing puts into into play
[934] their knowledge about what a marketing
[936] campaign is and they can control and
[938] create their own campaign models to
[941] create their own marketing products
[944] but with consistency over time
[946] the sales team can create a sales Ops
[948] model and that sales Ops model can also
[951] take advantage of those conformed
[953] Dimensions okay now Finance Finance gets
[956] into the into the game here and finance
[958] of course controls everything with
[960] Finance when it comes to costs so now
[962] you can see we have our different
[963] domains who are owning their different
[965] data models they're sharing common
[968] Dimensions so that everybody's speaking
[970] the same language when it comes to
[971] Roll-Ups and how you look at the data
[973] and now we can do something
[975] extraordinary because we have a common
[978] language for how we're expressing our
[980] business rules we can now combine models
[983] to create all new composite analysis so
[986] Watch What Happens here the marketing
[988] team can create a campaign Roi model
[992] that combines their campaign model that
[995] they created with the cost model that
[997] Finance created
[999] so now you can see that we can create
[1001] new mashups without having the campaign
[1004] and the managers and the marketing teams
[1006] having to understand how Finance works
[1009] and finance doesn't need to understand
[1011] how marketing works so now we've
[1014] empowered the business to create their
[1016] own data products but with consistency
[1018] and control and the ability to share
[1021] their analysis with all other business
[1024] units and business domains in the
[1026] company that's a game changer
[1029] so let's all wrap this up here
[1033] what did we learn here and you're going
[1035] to be hearing a lot more about this
[1036] today
[1038] but a semantic layer means that everyone
[1042] is going to speak the same business
[1044] language
[1045] everybody is talking the same language
[1047] because we're dealing with a logical
[1048] view of the business we're not dealing
[1051] with tables and columns and bits and
[1053] bytes we're dealing with true logical
[1056] business Concepts so semantic layer
[1059] makes that consistent across the
[1062] organization
[1063] now we have everyone being able to get
[1066] involved and make business decisions
[1068] make data driven decisions using
[1072] analytics because now we've opened the
[1074] the semantic layer to everyone not just
[1078] the bi users not just the data
[1080] scientists but anybody with Excel on
[1082] their desktop
[1083] with the right semantic layer you can
[1086] make data available for everyone in your
[1088] organization and not just the people who
[1091] know how to write SQL
[1093] a semantic layer also promotes as we
[1097] just discussed a manageable data mesh
[1100] type of architecture
[1102] so rather than a free-for-all going back
[1105] to the you know the business
[1107] um making up their own terms and and
[1110] making up their own pipelines you can
[1112] now standardize on a single way of being
[1115] able to Define your business logic and
[1118] you can make that all work seamlessly
[1120] and make it shareable across all your
[1122] data domains in your organization
[1126] when it comes to data governance we now
[1128] have a single control plane for every
[1131] single query so whether that be Road
[1134] level security whether that be column
[1136] level security whether that mean data
[1138] masking whether that mean role-based
[1141] access and control
[1142] a semantic layer is that control plane
[1145] meaning every single query crosses its
[1148] threshold that means we can apply that
[1150] governance in one place there's no need
[1153] for a separate governance platform or
[1155] governance tool and a good semantic
[1158] layer should be able to inherit the the
[1161] uh the controls and the security that
[1165] come with the base data platforms so it
[1168] shouldn't be competing it should be a
[1170] layer on top which means it needs to
[1172] integrate with the data platform
[1174] security protocols
[1176] and then finally
[1178] a semantic layer is an abstraction layer
[1181] isn't it and that means that it's going
[1184] to Future proof your decisions from how
[1187] you access and consume data to what data
[1190] gets accessed by having that firewall
[1194] and having that single control plane
[1196] separate your consumption as well as
[1198] your data platforms you can plug and
[1201] play and switch data around you can you
[1203] can retire platforms you can migrate
[1205] platforms you can introduce new tools
[1208] you can consolidate tools you can expand
[1210] your tool access without having to worry
[1212] about
[1214] retooling your entire stack
[1216] so with that I hope that did a good job
[1220] at sort of setting setting the stage for
[1222] what we're going to be talking about
[1223] today
[1225] um and we're going to be really diving
[1226] deeper in a lot more detail on some of
[1229] the stuff I just talked about
[1231] so uh hold on to your seats and uh enjoy
[1235] the show
