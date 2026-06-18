---
schema_version: 1
id: yt-qGp_Mort9Dg
type: youtube
title: Ontology-based Data Access made Practical, by Diego Calvanese
url: https://www.youtube.com/watch?v=qGp_Mort9Dg
authors:
- EDBT-INTENDED Summer School 2022
ingested_at: '2026-06-18T01:38:27Z'
content_hash: sha256:c6300071d1bd86e50e98f99de21291f858c949805234df3632d8e308c75d3799
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: EDBT-INTENDED Summer School 2022
  channel_url: https://www.youtube.com/@edbt-intendedsummerschool2888
  duration_seconds: 9562
  caption_track: cached
  snippet_count: 1506
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:27Z'
  user_correction: null
---
[4] yeah so i was mentioning on top israel which is a spin off we founded three years ago uh which tries to bring to industry uh
[12] some of the ideas that i will be talking about today related to managing data
[18] using ontologies and the main practical means as we're saying before to mcginn that my
[24] presentation will be less theoretical than the very nice talks that we we had today uh today in the past days
[31] uh i hope it will not be too basic again compared to the to the previous
[37] presentations so in that sense it this is more practical but i will not be talking about what we do in the company
[43] so what i will be talking about is essentially the result of the work in my research group and not
[51] only in my research group but also in other groups working on on this topic of data management using ontologies
[59] and we have been working on this topic since theoretically since 15 years
[65] practically in the sense of developing tools and technologies since 10 years
[70] so that the tools that we have developed are now quite well engineered and i hope i will give you some ideas about this in
[76] my presentation uh umeo is also an affiliation where i'm
[81] part-time so i'm part-time in rumeo in northern part of sweden and where i'm also building up a
[88] research group and some of the phd students uh are also here role models and livia are here they come from romeo
[96] okay i think you've seen this variation of this picture hundreds of times in different colors in different sizes and
[102] whatever just talking about data management where several issues become important
[108] typically volume is considered important but volume is not the only aspect in fact we are dealing here more than with
[115] volume with variety of the data which is related to the fact that data has a complex structure and we need to take
[121] this into account uh when we want to manage data then there are also the other aspects where acidic plays also an
[128] important role in the context of ontologies because ontology logical theories that deal with somehow the
[134] quality of the data one of the qualities of the data is related to whether data is consistent is
[140] true in some sense so this is also an important aspect although i will not say too much about that point i will not say
[147] anything about velocity which is also an important dimension uh namely related to the fact that data
[153] changes and there is a lot of work and there will be a lot to say about dynamic data so data changing over time
[159] because in fact this is what data always does i mean no data is static in reality data evolves and you need to take this
[166] into account but okay
[172] so one point that i wanted to make is that and this is also uh has been assessed in industrial settings is that
[179] the volume is not the key aspect in general a key aspect is the fact that data has a complex structure so the
[185] variety is the key aspect this is relates to some survey that has been done now quite some
[190] years ago but this is still valid so when companies and large corporations or
[196] large organizations who have to deal with with data look at the challenges the biggest
[202] challenge comes from variety of the data and what i want to say today and the
[208] technology you've been developing try to address this point
[215] now let me uh provide a brief motivating example for
[220] what what i will be saying so for ontology based data management and this is related to the fact that uh in large
[227] corporations in large organization uh a key aspect is that of uh
[233] of getting to the right data so bringing the right data to the right people and then also uh establishing the quality of
[240] this data and the example i want to make is from the oil and gas domain where we had some years ago uh quite
[247] large european projects with the big industrial partners one of these industrial partners was equinor at that time it was called
[254] statoil which is the biggest uh norwegian oil company i mean it's
[259] they they are the the leaders in uh drilling oil on on sea worldwide and
[265] they have large teams of data engineers they have also large teams of geologists
[270] who have to analyze the data and in that setting uh the engineers and these are
[275] geologists so and geophysicists so these are not computer engineers they spend a large amount of their time
[282] on the problem of forgetting the access to the right data so that they can
[288] study and analyze this data and get the information the useful information they need in order for example the
[294] predictions about drillings they need to make and the example i want to make is precisely
[300] about the department of state oil exploration so equinor exploration now
[306] where geologists need to access uh before drilling new wellbores they need
[312] to understand where they should do the next drillings and for that they need to get relevant information about previous
[318] drillings and analyze this data so that they can then give suggestions where it is more likely that they will find the
[324] oil and for that statoil or equinox maintains a large
[329] relational database it's called zleg which is not so large in terms of size
[335] if we compare it to the big data now maintained for example by social networks and so on but it's still large
[341] in terms of size it's terabyte of relational data but what is uh challenging is the complexity of this
[346] data so this database is constituted consists of more than 1 500 relational
[352] tables each with thousands of or hundreds of attributes and more than thousands 700 views that
[358] are built over these tables and on this database were in in equinox
[363] work 900 geologists so they need to access this data and
[368] for example here we have a simple extract of an information request that
[374] such geologists might have so they would like in some geographical area of interest that they characterize they
[380] want to return get all the pressure data tagged with some stratigraphy information
[387] with some control attributes that they are aware of and they know
[392] and also they need to apply further filtering on it now a geologist poses the question roughly
[398] in these terms so in essentially natural language but then to obtain the answer to this is a question they need to
[404] access this lega database and this which means they need to translate their request into sql which is the language
[412] with which you access such a relational database now in order to get the answer to this
[417] query they need to access a main table for elbows which has 38 columns and if you
[423] try to look at this table and the names of these columns you will not understand anything so this this database uses
[429] cryptic names both for the tables and for the attributes in this table then uh to obtain the pressure data
[436] which is also part of this request they need to join with four additional tables and apply some filtering conditions and
[443] then to obtain the stratigraphy information they need to join uh the the
[449] the table so far with five more tables okay so if you if you put things together you
[454] get a quite complex sql query that is written here and uh that makes use of these these
[462] tables with their attributes now obviously the engineers so the geologists are not able to write the sql
[469] query it's not their business they're not computer scientists so they would not never be able to write this query so
[474] what they do in general they go to a data management expert so satellite has several uh data
[481] management so data uh specialists so these are people who are computer scientists and know well the
[488] database know well how to access it but also have have gained experience in this
[494] domain in the oil and gas domain because they need to understand what their geologists are talking about so the journalists come with their request the
[500] one that we saw in the previous slide and then these data management experts they translate this request
[507] after several iterations with the geologists into the sql query that you hear that you see here and this whole
[513] process can take up to several days so it's not something that they do on the spot i mean it's complicated you have to
[519] deal with uh three thousand uh so this is a costly process
[525] and then this process tp is iterated because the geologists get the answer then to the query this is being executed
[531] they analyze the look at the data and then they see that they need additional apply additional filters maybe
[536] additional conditions so this whole process iterates so this is a quite costly effort
[543] and that requires the interaction between costly experts the geologists they are highly paid engineers also data
[550] management experts and they need to have a deep knowledge about uh this data
[556] and also about the domain and this whole thing is quite costly as was saying this costs uh equinor roughly 50 million
[563] euros per year just this problem so just dealing with the data access problem in
[568] this department with 900 geologists and at that time so we looked at this
[574] several years ago this was a motivation for starting this european project in which statoil was
[580] one of the industry partners and in which we were trying to push the technologies based on ontologies for
[587] solving precisely this issue so how do we address uh the challenges
[593] that come from for example this use case but this similar problem occurs in many
[598] other settings think of large banks of public administrations so this is very
[604] very special in other european countries but i guess it's the same in italy there's a huge effort was the
[609] digitalization of the public administration and also there are huge problems related to also integrating
[616] data coming from different departments different ministries
[622] is is is a challenging problem now the idea that was proposed at that
[627] time that we proposed in that project but that has been pursued also in other
[632] settings is to address the problem by using domain
[638] knowledge specifically encoded in ontology so the idea is to use a global schema but this global
[644] scheme is represented in terms of an ontology because this ontology exposes
[651] the information the relevant information the data in terms of a graph what we call now a knowledge graph
[657] so this information is exposed through the ontology to the users but then this
[663] ontology is mapped to the actual data sources so we use this global schema in terms of an intelligent map this global
[669] schema to the actual data sources and the ontology expose it as a graph which
[674] is a flexible data model so the approach that we took there is not to use traditional data integration technology
[680] which exposes relational data in general so traditional data integration this
[685] global schema is a relational scheme instead the idea is to use a graph model so a knowledge graph because it gives
[692] more flexibility integration and then a further point that was pushed in this work and we are pushing is to
[699] do this integration in a virtual way so we don't materialize the integrated data
[704] into whatever into a data warehouse which would be relational or a knowledge graph
[710] a materialized knowledge graph but we keep this integrated information virtual so it's not materialized and
[718] if you put together these ideas you get to this virtual knowledge graph approach to data access integration which we now
[726] call in this way so we call this technology virtual knowledge graphs but for a long time and
[732] still it's been known as ontology-based data access and integration for the obvious reason that this knowledge graph
[738] is presented through an ontology to the user and the underlying data sources are
[744] connected with ontology so that's how we also call it and you find a lot of papers a lot of workers our own work and
[751] uh this keyword of obda or obdi if the integration aspect has to be emphasized
[760] so if we just put together these ideas we get to the architecture concept of
[766] architecture this is depicted here where we have uh here the the bottom level the
[771] data sources and now the setting that we assume is one where we present uh at this level a relational
[779] view of these data sources so these data sources in general can be quite heterogeneous so can be relational databases but also csv files json
[786] documents uh xml or excel files csv files so various
[793] kinds of data and even web services but still what i'm saying today and
[800] the the setting that i'm addressing now i assume that we have a layer a lower
[805] low level layer somehow that exposes this data in terms of relational relational schema
[812] and there are several uh federation tools also commercial ones they know dodramio paid just a few of them but
[818] there are dozens of such federation tools that provide such a relational view of the underlying data which is
[826] quite conceptually quite simple in the sense that uh all the data sources are put together
[832] and each one is just exposed relationally okay in a quite natural way then these uh sources are mapped to an
[840] ontario to the virtual knowledge graph that you see depicted there which is constituted by component is the ontology
[846] itself the ontology defines essentially the vocabulary that is shown to the user which is
[853] typically a vocabulary in a language this we in which the users are familiar so for example you use
[859] terms that are familiar to all these geologists so terms coming from the oil and gas domain if you're integrating
[866] data sources from that domain so the ontology is the component is exposed but then uh the mappings that uh
[873] the intermediate layer between the ontology and data sources they essentially expose the data and the
[878] sources in terms of knowledge graph that is formulated using the terms of this ontology and then users which could be
[885] either human users but also applications that uh leverage uh the integrated data they issue
[892] queries to this vertical knowledge graph system and the idea is that these queries which come from various
[898] applications or users they get translated by the system into queries down to the data sources and the
[904] answers are provided to the users okay so that's that's the idea
[909] and i want to discuss the various components of this general architecture but before i do so and i mean i will do
[916] so today let me briefly motivate some of these points i already said something but let me hear
[922] summarize it again so why ontology so why do you use an ontology for the global scheme i mentioned this already
[928] an ontology in general is a structured formal representation of certain concepts that are relevant for domain of
[935] interest and the relationships between these concepts and in this setting the ontology has
[941] essentially a twofold purpose it defines this vocabulary of terms that are relevant for the domain of interest and
[946] that are the terms known to the users and these terms are essentially classes and properties uh that i exposed to the
[954] user uh cast and this morning talked about concepts in description logics and roles
[961] in description logics is just nothing else than classes are concepts and properties also for draws depending on
[967] whether you take a more somehow theoretical approach in terms of descriptionology or you go more to the semantic web but terminology where
[975] ontologies are and the elements of an ontology are called in this way then the second purpose of the ontology
[983] is uh to extend the information in the data sources with domain knowledge so
[989] the intelligent codes relevant domain knowledge so the data is enriched with this knowledge and this knowledge can be
[995] used at query answering time at queer processing time in order to provide
[1000] additional answers and karsten was talking about this extensively this morning or the
[1006] reasoning that we do with ontologies is this kind of enrichment of the answers
[1016] sorry yes obviously this is an issue
[1022] this ontology requires expertise about the domain in order to encode the correctly and in a possibly
[1030] complete way the domain knowledge this is in general not an easy task so because these ontologies can become
[1036] quite complex so they can have themselves hundreds of classes and properties
[1042] when they have to encode a complex domain okay so but this we see this is not the only aspect the second aspect will be the
[1048] mapping component which i talked about but we shall talk in a second
[1054] but the advantage of this setting is that in fact one can also rely on a lot of work that has already been done so
[1059] there are many uh available standard ontologies over various domains that one can use and one
[1066] can leverage in this setting and the ontology is also at various levels so so-called i mean domain ontologies
[1074] of the type that was mentioned before but also so-called apa level ontologies which are somehow more abstract
[1079] ontologies that define more general abstract properties of the of
[1085] classes and properties are present in antarctica and can be used in order to assess the quality of
[1091] the other components of the ontology so there are many uh ontologies available and can be used for for this activity
[1098] but this doesn't mean that in general can just rely on such available ontologies so this requires as we're saying also in general quite some
[1106] commitment to uh to build the custom customized ontology for specific domains
[1113] and this is one of the challenges in this in this setting so it doesn't come for free it
[1118] requires somehow a commitment to develop or to invest in the development of this
[1124] ontology this is an offer not an effort that you do in one day i mean developing such comprehensive can require several
[1130] months of work of domain experts in general who have to interact also with
[1136] ontology experts because one group of people knows the domain and know what knowledge they want to encode
[1142] but they might not know how this ontology should be built so this is a challenge in general
[1150] now the second aspect i want to mention is why do we use a knowledge graph as was mentioned before the traditional
[1156] approach is to adopt a relational global schema but knowledge graphs gives more
[1161] flexibility so it doesn't require to commit to a certain structure a priori
[1166] because committing to relational structure can be quite binding if you have a long-running project
[1173] also a graph is is able to better deal with heterogeneity which is an important
[1178] aspect in this setting also with missing information in complete information
[1184] and when new information comes this is also an important aspect in general having a graph that's
[1190] not required to do complex restructuring operations that you would have to undergo if you have if you commit to
[1195] certain relational structures so it has some advantages the other aspect are the mappings
[1202] now what are these mappings i will talk extensively about the mappings in the in this
[1208] tutorial today but essentially these mappings are declarative specifications and
[1214] again in the traditional approach to data integration the connection between the apa schema
[1219] the tpa the global relational schema and the data source is often done in a procedural way through code that
[1227] extracts the information from the sources and expose it in in terms of the global relational scheme instead
[1233] mappings are not called they are declarative and this has several advantages uh first of all they are easier to
[1240] understand and tends to design and to maintain they support an incremental approach to
[1246] integration as we will comment and see and also being declarative they are machine processable so one can reason
[1252] over such mappings and can use them in order to automate certain processes and this is heavily exploited in this set
[1270] yes so take it as a synonym of uh somehow the t-box of yellow ontology
[1276] but then together with the t-box and i will talk about this you have the the a-box that is however not uh
[1284] materialized a-box but is a an a-box that is virtual in the sense that it is constructed from the data
[1290] using the mappings okay so this idea of knowledge graph combines both the t-box
[1295] plus this data that this a-box that is presented in a virtual way
[1303] now this is more i mean i must admit it clearly so the fact of talking about
[1308] knowledge graphs and dirty knowledge graphs is a marketing issue because the term knowledge graph is nowadays popular
[1314] i mean there's the google knowledge graph facebook has a knowledge graph and so on so if you talk to industry people
[1321] mentioning knowledge graphs they become immediately interested if you talk to them saying you do intelligence based
[1326] data access they they don't know what this is about and probably are not interested so it's it's a marketing move
[1333] that helps to communicate to people that we hope to convince to adopt this
[1338] technology
[1344] now the last point that i want to briefly discuss is this virtualization aspect
[1350] so in general again in traditional data integration mostly uh
[1356] data integration is done through what is called the etl approach the extract transform load approach in which data is
[1362] extracted materialized extracted in a material way from the sources
[1368] it's a process transformed and then is loaded in a materialized global schema typically a data warehouse but also in
[1375] the setting where you want to use knowledge graphs it could be also a materialized knowledge graph
[1380] okay instead in the virtual approach we don't do this so we keep the data at the sources
[1388] so data stays in the sources and is only accessed at query time when requests are issued to the integration system these
[1394] requests are translated down to the sources and the data is extracted at the moment on the fly
[1400] and provided as an answer to the user so this avoids to construct potentially quite large and costly to maintain a
[1409] knowledge graph of data store and to keep it updated because that's a key issue in general when data evolves if
[1414] you materialize integrated data and the source is evolved then you need to
[1420] uh re materialize the incremental way but this is a costly process in general having a
[1426] virtual approach avoids this okay so somehow the data is always fresh also uh one can use since the data is in
[1434] the sources one can use existing data infrastructure and expertise to maintain these uh sources that often are already
[1440] available and in fact often the data sources need to stay in large organizations why because
[1447] there are many applications running over these sources already and you cannot just simply throw away that because
[1454] there is a complex infrastructure it runs on them so they have to be maintained anyway
[1461] and the virtual approach also is better suited to deal with incrementality
[1468] in the sense that if you want to add additional data sources you can just add them to your architecture you define the
[1474] mappings in a declarative way and they are automatically incorporated in your integration system so the next query
[1479] that you issue will take into account these new sources the same when sources change when when they get offline so
[1485] this automatically accounts for that now let me make also a disclaimer this
[1492] is ideally an ideal world in which you can always access the sources in a virtual way in
[1498] reality we have seen that it's not always the case it doesn't work always for various reasons one is performance
[1504] issues clearly accessing sources in a virtual way has a cost in terms of
[1510] performance because this data needs to be processed on the fly and sometimes this processing might be complex and
[1517] there are also other issues related to uh quality of the data so often the data sources are not of of high quality data
[1524] is dirty as we say so it needs to be cleaned and there are many operations that you can do about cleaning the data
[1530] that can be done on the fly so in the virtual setting but this is not always possible sometimes these cleaning
[1536] operations are costly and you want to do them once and then maybe
[1541] store the clean data so in general the the real setting that one has to consider is one in which you have a
[1548] hybrid architecture which possibly part of the data is materialized maybe the
[1553] one that is very static it doesn't change very often or that requires heavy cleaning operation so you materialize that data
[1560] and store it maybe in an additional source then data that is uh very dynamic that one you keep virtual
[1567] so in general you have to combine these two aspects and this is in general a challenge also
[1572] in terms of deciding taking decisions about which data to materialize which data to virtualize and how to get
[1580] combined architecture but in part this is also supported by this uh data federation tools that i was
[1586] mentioning before which provides some partial support for materialization so in part you can also
[1592] deal with it at that level okay i will not talk about this anymore today so
[1598] i assume that we are dealing with purely virtual architecture for simplicity here
[1606] okay so this was a brief motivation for what i'm going to talk about
[1611] and so discovered the essentially the first ballot here the challenges that we have in data access and
[1618] how we what is the plan for addressing them and now i want to go a bit more into detail about the various points so
[1625] i will talk about the various elements of this virtual knowledge graph architecture
[1632] and then i want to spend some time on two points one is
[1638] how to uh process queries and how to optimize the query processing okay so this is a
[1645] complex engineering activity to some degree but there are some interesting aspects on that side as well and i want
[1651] to give you some ideas about that the second point that i want to mention is related to what you were asking before
[1657] you were saying the ontology how do we get that ontology that's one problem but i would say the bigger problem is how to
[1663] get the mappings because ontology available mappings tp are not available they depend on the specific sources and
[1668] they can also be highly complex if you have tables with thousands uh so if you have
[1674] a database with thousands of tables and hundreds of attributes and you need to map your ontology to these tables you
[1680] can imagine that the mapping itself will be quite complex so coming up with uh these mappings is a challenging
[1687] task and requires effort so it was investment that you guys also supporting technology
[1693] so i will give you some ideas of what we are doing uh in this respect
[1698] regarding this problem here any questions
[1703] yes
[1723] some degree database is actually quite dynamic database in terms it's a database that is growing what is the idea of this database it works i mean
[1730] why does it have so many tables essentially the way satellite operates is whenever they have a new drilling
[1735] they set up a new set of tables related to that specific drilling where they saw all the information regarding that
[1742] drilling often these tables are very similar i mean but they're not always the same it's not exactly the same table
[1747] as before because maybe they have they are using new drilling equipment they they drill in different kind of
[1754] stratigraphic zones that require to keep different parameters so they essentially their choice is to create a new set of
[1761] tables whenever they have a new new drilling that they do and then these poor data management experts they need
[1768] to look into this and take this into account when they receive these requests and try to understand whether now these
[1774] new tables need to be incorporated or not uh in in the answers that they give to the engineers
[1780] now in a setting where we are using this approach a declarative approach the idea
[1786] is that whenever these new tables are added essentially we understand the structure also relying on similar tables
[1793] that were already mapped in that database to the ontology ontology typically doesn't change much because
[1799] the domain is always the same and we define new mappings to these uh these new tables they take into account
[1805] the expertise or the experience that has already been done with previous tables
[1817] the mappings i mean i will say something about this so we are working on automatic map
[1822] injuries and there is there is some form of automation in that in that process but it will not work to do it completely
[1829] automatically in general in general it requires manual intervention and manual expertise
[1835] although there is a lot one can do automatically and that's one of the direction which we are working not only
[1840] we but there's a community also working on this uh automatic mapping extraction and generation
[1848] but it's a challenging problem a lot of questions
[1856] okay then let me say something about uh the general approach to virtual knowledge
[1862] graphs and i want to say a few words because i'm not sure who is familiar with the various technologies so i want
[1868] to say a few words about the data model that we use for the knowledge which is rdf and the corresponding schema
[1875] formalism which is rdfs then the ontology language which is uh uh autoql
[1881] carson this morning mentioned alto el uh he said that r2l is one of these sub
[1888] languages of an expressive ontology language the owl 2 language
[1893] auto ql is another sub language technically they are called profiles in the w3c jargon but the profile is
[1900] essentially a syntactic restriction of a more expressive language autoql is
[1907] such a profile that is suited to the setting of ontology-based data management i will say some words about
[1913] sparkuel the query language which is somehow connected to conjunctive queries that were
[1918] extensively discussed today by carson but also in other talks in the previous days
[1924] and then i will uh spend a bit more time on the mappings and i will give then how
[1930] this framework can be formalized and we'll say something about queer answering in in general
[1936] and then come back to this in the the further parts okay
[1942] so who of you is familiar with the rdf
[1947] and knows about semantic web but just to understand okay
[1953] right a few may one third know something about this okay
[1958] if you're bored tell me i will not go
[1964] and we will not say deep things about this just to fix the terminology uh one point that i want to make before i start
[1970] with this is that we are clearly in a setting of incomplete information so we are not in a pure database setting here we are
[1976] setting an ontology setting why because the incompleteness comes on the on one
[1982] hand because we are dealing with data integration data integration is inherently a problem where we you have
[1987] incompleteness because in general you cannot assume that your sources are complete with respect to the information that you want to see at the global
[1993] schema okay that's one source of incompleteness and this is essentially encoded in the semantics of the mappings
[1999] so these mappings are typically what are called sound mapping so they correspond logically to implications which means
[2005] you could have at the global level additional data with respect to the one that is retrieved from the sources
[2011] precisely because the source is assumed to be incomplete and then another form of incompleteness comes from the ontology itself it's a logical tear and
[2018] ontology so it introduces incompleteness uh however
[2023] since it is an illogical theory an ontology it's suited it's designed to deal with incompleteness so that's
[2029] inherent in the approach to deal with incompleteness that's the plus
[2035] the minus is that dealing with incompleteness is in general something costly we don't have a model one
[2040] database or which we answer queries we have a set of models in general it's an infinite set of models
[2046] each of these models could be infinite okay so we have the issues that also passed and was mentioned this morning
[2051] also in this setting and we need to do in general logical inference so the challenge is how can we get rid of
[2057] larger inference and go back to a setting which we can use commercial
[2062] technology for database and that's exactly what we do in this setting
[2068] now i want to talk about these various components of this vkg framework and now
[2074] these have been essentially the corresponding standards have been defined now since many years you see that the dates it's quite old it's
[2080] ancient times in terms of computer science but these are the reference standards of
[2086] the technology that you're using that's semantic web technology specifically rdf is a recommendation in in w3c terms a
[2093] recommendation is a standard what is a recommendation is essentially a standard document which
[2099] people are here and tools are here so rdf was defined in the current version in 2014 the ontology language is this
[2106] altouch language which was defined the uh mid second edition i mean r2 is a
[2112] successful language of the old language which was called owl now we call it one but you know it's now also 10 years old
[2119] uh the mapping language the standard one is artworml and in fact the technology and the tools adhere to this mapping
[2126] language i will not really present that where ml i will present why because arturo is unreadable by humans it's not
[2132] meant to be right by humans so it's meant to be read by machines so we i will not introduce it i will just talk
[2138] about a simple to read language that is essentially equivalent as far as we are
[2143] concerned to argue rml and then i will say some words about sparkvue l which is the query language used in this setting
[2150] let me also again here make a disclaimer uh sparkuel is and this technology is the
[2156] one of the semantic web now not all uh let's say industries organizations who
[2164] are facing these problems that we are talking about really embrace the semantic web approach and semantic web
[2169] technologies so in fact it now becomes also important to uh rephrase that and we somehow develop
[2179] some of these technologies and tools in a more quote traditional setting but still i think the flexibility given
[2187] by graphs is important so we don't want to at least in the general general setting to go to a relational approach
[2194] although in some cases relational approach is also needed so one direction which to go is to use property graphs
[2201] and then also rely on some graph database technology at various levels in this setting one way is for
[2207] example to provide the vision of such a system in terms of a
[2213] graph database instead of a knowledge graph okay so to present uh the data that is uh extracted directly from the
[2220] ontology in terms of property graph for example that's one approach in which one can go another possibility is also to
[2226] consider that the lower lab graph databases as data sources and possibly then exploit also the
[2232] additional features and capabilities that these graph databases have with respect to more traditional relational
[2238] technology for example processing path queries in an efficient way which is something important so these are all
[2243] directions in which this kind of technology is also being explored and developed
[2249] but i will not really talk about this today there's no time to talk about this
[2256] okay uh let me just say a few words about rdf or this rdf rdf is a language
[2262] that is essentially a graph a way to represent graphs it's a graph based data
[2268] model uh where we have labeled nodes that are connected by labeled edges and
[2274] the nodes have three different forms they are either liters which denote constant values that belong to some data
[2280] type and they have not yet we have the standard data type strings integers real numbers and so on those
[2286] that you can imagine then we have nodes that are essentially identifiers they denote a resource they
[2291] are called iris for internationalized resource identify and these are just global identifiers on the web okay an
[2298] irie is think of an is similar to a url but it's not for a website it's in general for a
[2304] resource that is available on the web and so they act as global identifiers and
[2310] then we have also blank nodes which represent anonymous objects you can think of them as existentially
[2316] quantified individuals as essentially quantified objects
[2322] the properties which are the binary edges they're also themselves denoted by by an iris so an item might also denote
[2329] the property an edge between two nodes okay between two iris themselves
[2336] okay so this is just the general rdf model now uh rdf
[2341] is a graph so you represent the graphs in rdf and how do you represent graphs as sets of strippers and you can just
[2347] imagine each of these triples has two nodes with the connecting edge so and the three elements of such a
[2354] triple are called subject predicate object so the subject and the object are two the two nodes and the predicate is
[2360] the edge that connects them and here you see an example where you have a node that represents a certain
[2365] person that probably lives in bolzano the name of this person is meant to be
[2371] john in fact there is a property which is defined by the way by standard
[2376] ontology the friend of a friend of told you which you can find on the web that defines this name property and here we
[2383] are stating to this triple that that uh individual uh has name has the name
[2388] john and that's the on the right you see this is the notation for a string how to denote how to set a data type to a
[2396] literary okay john is a string letter and we are saying it's of data type string that's
[2401] the syntax of rdf strippers yeah and here we have the three elements
[2407] i was saying uh there's some uh there's the standard allows you to to
[2413] write these items in a more compact way by introducing uh abbreviations you can introduce so-called prefixes for example
[2419] you could say that a friend of a friend you want to introduce a friend of a friend prefix so
[2425] that when you want to denote this property name you don't need to write the long ira but you just use the
[2430] abbreviation that you have introduced this prefix and then this is becomes part of the rdf document
[2437] that maintains the information and so you can write your triples in a more compact way you can also have other
[2443] prefixes for example here or you can also define a base according to which then you
[2449] represent all the all your triples in in your graph okay but it's not really important i mean
[2457] let me just give you a few examples i was saying that the triple in general represents uh an edge between two objects but there
[2463] are also triples that in fact represent the membership of an object to a class and these are the triples who have a
[2469] special the special predicate rdf type so for example you're saying that
[2474] this uh id here this person 25 belongs to the class professor that's the way in
[2480] which it is written now i also use uh the more classical logical notation
[2485] which this is just a unary fact okay a fact of a unary predicate the class professor and you're saying that p25 is
[2492] an instance of this class okay this is what you're more familiar with probably
[2501] now let me just say that there is also an abbreviation since that vf type is so common the typical abbreviation is a so
[2507] s stands for rdf type then we have a triple in the sense that
[2513] it was saying before as an edge in this case it's an edge connecting an ire an object to a literal a string the string
[2520] artillery so i'm saying that the last name of this person is abdale again i can write this as a binary predicate
[2526] last name which in this case would be a predicate that represents a so-called the data property so it connects an
[2532] object to a data value and finally we have an edge that
[2538] connects two objects for example uh here we are saying that this person p25
[2544] teaches the course c7 okay and where teaches now is a so-called
[2550] object property which connects two objects we have an object for a person an object for
[2556] a course again we can write this in more abstract notation as a fact as a binary effect where teaches a binary predicate
[2566] now we can represent this set of triples as a graph so here you see this
[2571] representation of the triples of some of these triples as this graph so each of these
[2576] edges represents one of these strippers that put a few of the triples here i mean these are not all and for example
[2583] we are saying here that p25 is of type professor so you see here in this graph we have nodes that represent
[2590] both both objects so that iris they denote
[2595] proper objects but also the classes themselves here professor is meant to be a class but this also
[2600] becomes an object in this graph okay it has its own iv
[2606] and i'm saying that p25 is a professor whose last name is a tale
[2612] and teaches this course here who's tied this kr and so on okay
[2618] so we can represent uh such a set of triplets graphically uh as
[2624] uh the way you see here and that's convenient when we will be talking about uh query answering because query
[2629] answering is based you know for sparql is based on graph matching and so we need to have this graph representation
[2635] of our data now in rdf there are also other elements
[2640] i mentioned data types i could show you a list of the various data types there are these blank nodes that i mentioned
[2645] before and also there is a mechanism to essentially group parts of a graph
[2651] together they are called name graphs which lead to what are called quadruples so the thing is uh more complicated than
[2657] i've shown here but it's we don't need to to be concerned about this
[2663] this was the first part i wanted to say now something about this how to ql anthology language
[2670] now just a few slides to keep it light that show you
[2676] what is an ontology an ontology is a collection of classes so a key element of ontology is to group
[2684] information in terms of classes that are organized in a hierarchy okay here you have a nice hierarchy of ice creams
[2691] because this heat you can enjoy it but in general in ontologies as we have seen
[2698] also today in carson presentation we have not only the classes but we also have the properties so the hierarchical
[2705] structure is not not only the asp it's not the only aspect we have the properties that can then be graphically
[2711] represented the whole ontology typically as a graph so it's convenient to represent ontologies in the form of a
[2716] graph but for other ontologies are not really graphs they are logical theories so i
[2722] could write an ontology in terms of a first order logic theory that's what you see here i will use this as a running
[2728] example for when we talk also about the mapping so i have here the domain of actors and movies okay so here you see
[2735] an anthology that encodes the fact that uh infrastructure logic every actor is a
[2740] staff member a serious actor is an actor movie actors and actors and actors and movie actors are disjoint and so on so i
[2747] can write the first logic actions that encode some knowledge okay
[2752] now in general ontologies are not we don't express arbitrary first order
[2759] axioms in an ontology we restrict the language because of computational aspects because we want the setability
[2765] of inference disability of queer answering and not only disability we want to do this also efficiently so
[2771] in particular we consider ontologies encoded in description logics and what you see here is the same ontology that
[2777] was encoded as first order logic actions now in the form of
[2784] actions in a description logic and specific these actions in a description logic that corresponds to this output ql
[2790] language that i would be talking about so these axons in this dna light
[2796] description logic actually it's not really even precisely artificial because we can also assert functionality in the
[2803] logic so this goes beyond this articular language but it's something that this has also been
[2808] considered in description login that is to some degree uh harmless although one has to pay
[2815] attention and how this these elements interact obviously uh as carson has shown today quite much more
[2822] detail than i'm doing now but essentially these actions that you see here express the same information
[2827] that was before expressed as first of the logic statements i will talk about this language in a second okay
[2836] sure usually
[2844] yeah okay so it depends what you're doing so now this setting is one in which we intend
[2851] to capture conceptual models so and you will see uh this r2ql language is has
[2856] been designed and was meant to capture conceptual models why because that's what people use when they design
[2862] information systems and that's some formulas they're familiar with and they can understand now in conceptual
[2868] modeling functionality is an important feature because it's used to characterize better your domain so
[2882] so it was not there because because it was meant to be an r2l ontology the version that we are using and how to
[2887] clear it doesn't support functionality i will say something about this now the question is what do you do with this
[2892] functionality functionality becomes important when you want to check consistency of your data without the ontology at least in the setting of this
[2899] the light framework so functionality instead does not play a role in query answering so once you have assessed that
[2906] your data is consistent and that for example no person has two social security numbers or no wellbore has two
[2913] different depths or whatever which could be expressed through functionality once you once you've assessed that your data
[2918] is consistent you can forget about functionality for queries
[2931] sure sure obviously and not only functionality i mean in general you need so people if you give them the power
[2938] to use second order logic they will use second order a lot you provided they understand it so this is always the case
[2944] but then it's an engineering task to agree between the ontology engineer who
[2950] knows the formalisms and who knows the somehow the pros and cons of adding more knowledge and the domain expert would
[2957] have the who would like to have the maximum expressivity to agree on something that
[2962] is manageable okay so in the end it's an engineering task the anthology that you produce and that you use then in your
[2970] integration system for example
[2976] so as i was saying before this our tutorial language is one of the three profiles there's also a third one alto
[2982] rl but in addition to r2l mentioned by carsten
[2988] and our two ql is derived from this the from this the light description logic
[2994] family so the light r specifies the logic that corresponds to how to ql and
[2999] this belongs to this family of lightweight description logics why lightweight because they have a
[3006] controlled expressive power in the sense that you control exactly what you can express in
[3012] this logic it has been tuned towards capturing conceptual modeling formalisms
[3018] but uh keeping inference efficient and when we talk about efficiency the key
[3025] aspect was efficiency in data complexity and in particular in this setting uh the
[3031] data complexity is ac 0 which is the complexity of evaluating first order queries and in fact we have this first
[3037] order rewritability property which means that queries over such an ontology
[3042] conjunctive queries or union of conjunctive queries can be rewritten into uh first order queries
[3049] variants in general we rewrite them into union of conjunctive queries and then these queries can just be evaluated providing
[3055] the implied answers okay and this gives these ac 0 data complexity because the
[3061] rewriting does not require to access the data it's just the pure
[3066] writing that uses only the ontology and the query so it's uh it's not affected by the data itself
[3073] and then once one has the rewriting one can just evaluate it over the data source and this gives
[3079] uh this is done with the complexity of first of all queer evaluation which is ac0 and in fact also consistency can be
[3086] checked in the same way so the problem of for example checking consistency with respect to functional
[3092] functional functionality that you might want to have in your ontology can also be reduced to a problem of queer
[3098] evaluation so in that sense although our although r2l does not have
[3103] functionality it can in fact be added to this framework and for the purpose of checking consistency
[3110] of the data with respect to the functionality constraints
[3116] questions okay very i mean let me just keep this i
[3123] was mentioning that ontology has classes data properties and object properties i was giving some examples in this
[3130] running example that i will use uh also i will use a graphical notation uh that i'm introducing just one example
[3138] now in an ontology in general we have two parts this was also mentioned before we
[3144] have uh what we call the ontargeo tea box now there's also ambiguity now in
[3150] the terms here sorry for the confusion uh also because the terminology that i'm
[3156] using here is not the owl 2 or the our terminology so in our an ontology comprises as you are saying the t-box
[3164] plus the a-box so the intentional part plus the extension part instead i use
[3169] for this the term knowledge base so for me a knowledge base uh contains
[3175] the what i call the ontology which is the schema level information so the axioms
[3180] plus the extension part that for us is an rdf graph okay so i call it rdf graph and
[3187] not a box because we are in the semantic website okay so i use the term knowledge base
[3192] for the combination of these two parts why because when we talk about ontology in the
[3198] ontology based data access setting what we mean is just the intentional part so the schema level information
[3205] which is made up of the vocabulary that is relevant for the domain plus the axioms that capture the domain
[3212] knowledge okay and the rdf graph is just a set of triples as we see
[3218] as we have seen before so we have triple that radiator belongs to a class with
[3223] this rdf type and then triples that assert that an object has a certain data property or that an object is connected
[3230] to another to another object via an object property that we have appear okay
[3238] now what are the actions that we have in this r2l language they are listed here on this slide so this slide that tells
[3244] you what our ql is and we can explain how to ql uh quite well in in terms of database terms okay
[3252] for those where is floris flores you don't like description logics right and you never
[3258] so you can read the light not as a description logic but just using your
[3264] deep knowledge about databases okay so what you have here you have a class you can declare a class what is a class it's
[3270] a unary predicate you can declare a property which is a binary predicate we have only union binary predicates and in
[3276] fact we have object and data properties so that they are distinguished there but
[3281] semantically they are just binary predicates okay and uh in uh in our file you have these
[3288] declarations you need to declare these terms that you want to use then you can
[3293] assert that the class is a subclass of another one that's just an inclusion between unity relations in database
[3299] terms okay because the class is a unit relation so you say that the unit relation movie actor is included in the actor relation
[3307] you can also say disjointness you can assert disjointly between two classes that's a disjointness constraint
[3313] which could be a deny can be written as a denial constraint involving unary predicates
[3319] you can say that a certain class is the domain of a property that's again it's the inclusion
[3325] of a unit relation so of the first component of a binary relation in a unit
[3331] relation okay that's what you say when the domain of a of a binary relation is a certain class you say that
[3338] the first component of the acts in relation is a movie actor okay
[3343] and you can say that a certain class is the range of a binary relation and this
[3350] is written in this way but this just can be read by saying the second component of the xen relation is included in the
[3356] movie relation okay it's just an inclusion dependency between unitary relations
[3362] you can also express something a bit slightly more complex i'll skip this uh
[3368] i skip the let's say i skip the our notation here you saw the r notation because
[3374] our is in is written in such a way that this requires a few lines to write i don't it's not very elegant in that sense but
[3381] that's how all is made uh instead we can easily write it in this uh abstract delight notation by
[3388] just saying that the class movie actor so the unit relation is included in the first component of the binary relation
[3395] okay so that's again an inclusion dependency and since you you have here a binary relation on the right hand side
[3402] this implies an existential quantification so you need to extensively quantify the second component of the relation
[3408] which you also have you should just include the unit relation in a binary one okay this can all be understood in database terms
[3415] you have also directly inclusion between binary relations so axin is a binary
[3420] it's a property so it's a binary relation place in it's also binary relation so action is a is a sub-relation of uh
[3427] place in that's a binary inclusion dependency and we can also uh
[3433] we have also inverse properties so we can say that uh the binary relation is
[3438] included in the inverse of another binary relation which just means in terms of independence you swap the two
[3443] components you should write it as an improvement dependence so this allows this logic to not give a
[3450] preference to any of the two directions of a binary relation because you have the inverse operator and you can always
[3455] invert the relation and treat those components in a symmetric way okay
[3462] any questions about this so this is essentially what you can express in this dna light logic so it's
[3468] a pretty simple logic and okay here i have also some examples and i give the semantics so that's the
[3474] semantics give me first order logic but it's just what i told you in words okay
[3483] okay let me skip this for a moment this is related to what i was saying before about the impact of this jointness of
[3489] functionality and also this joint has a similar role as i was saying before this joint test is not used for query
[3494] answering it's just used for consistency checking of the data with respect to the ontology okay
[3500] the the only uh actions that are used for query answering are the somehow the positive ones those that do not involve
[3506] this negation here these jointness okay i don't i haven't put here uh these joints of properties
[3512] which can also be asserted so we have only this joint with your classes but
[3517] this will not play a role in query answering now
[3523] i was saying that this logic is tightly related to conceptual models and this is essentially
[3528] shown here on this example which uh and for which i'm using here
[3533] and a top notation for the ontology but this resembles in fact the uml class diagrams and i could also
[3540] have drawn here an entity relationship diagram if you prefer from that point of view if you take this
[3545] concept or view they are all these formalisms are essentially equivalent and what i can express in this deal
[3553] light logic or how to ql if you want is essentially what i can express in such
[3560] uml class diagrams about the domain okay i can say that you see it here i can say
[3565] that classes are subclasses of other classes i can say this jointness in such a hierarchy
[3571] i can talk about domain and range of binary relations i can say that plays in has as domain act and as range play
[3578] i can assert not only subclasses but also sub properties so
[3584] the binary relation action is a subrelation of the place in relation and i can then do similar things for the
[3590] data properties which are just attributes in uml class diagrams so for example title is an attribute of display
[3597] class that has his range a string so the title of a play is a string
[3602] and that's it and i'm sorry sorry and there also if you had a mandatory participation so i say that every movie
[3608] actor must act in some movie at least one movie okay so this is the kind of knowledge that we can express in this
[3614] output qr language and in fact it's convenient to visualize our tutorial ontologies as
[3620] uml class diagrams for example or if you prefer using such a graphical notation but there's not much of a difference as
[3626] you can see okay and these are exactly the constructs that are common in conceptual modeling
[3632] and that's why somehow this logic has been tailored towards capturing conceptual models
[3642] a few words about spark2l now
[3647] we are in a setting of incomplete information so a priori we have to think well about what language you want to use
[3653] now in principle in we could use we could go towards two extremes something
[3659] quite expressive sql okay the language used in databases or something
[3665] much less expressive so an ontology language use the ontology language as a query language now
[3671] the first approach is the one that has been pursued in uh in knowledge representation quite a lot
[3676] so in order to presentation before queer answering became popular people were considering the ontology
[3682] language also as the way to query their knowledge okay this is not very very
[3688] uh a good approach because ontology language are good for representing knowledge but they are not good for
[3694] querying knowledge they are way too weak to query knowledge because they don't have joint capabilities in this ontology
[3700] language you have a very limited way to express joints which make them unsuitable as on as query languages on
[3707] the other hand if you use sql which is first order logic at least first order then we have
[3713] aggregation and so on if you sql then in a setting of incomplete information pre-answering
[3718] becomes undecidable so that's also not a suitable language the negation is a problem so the idea is the approach to follow
[3725] here is to go towards something in the middle which is a conjunctive queries and in fact uh conjunctive priests have
[3731] been initially studying this setting and then uh moving the whole approach to the semantic web framework
[3739] uh spark2l was considered has been studied as the queer language but the course part ql is very similar to
[3746] conjunctive grid and parquel has some differences i will discuss them briefly but essentially that's the form of queer
[3752] language and also then we can use not only conjunctive periods but also unions clearly
[3758] and in fact one can use sparkle just as a syntax for conjunctive queries but in the end there are differences and
[3765] i'll just point this out in a second now what is particular as a query language sparql
[3770] it's the standard query language for querying rdf data now sparkyl is based on graph matching so
[3777] esparcuel the the the basic form of a sparkle query is
[3783] such a a graph pattern so you have triple
[3788] patterns and uh that are composed together into a graph pattern so you can represent such as particle query
[3796] such a basics particular query as a graph and you see here the representation of this particular query
[3801] is a graph where you introduce nodes for the variables and also nodes for the constants which in
[3808] this case are both proper consoles but also class names are viewed as elements in this graph as as
[3814] nodes in this graph with an id so this somehow they play the role of a constant but
[3819] since it's the project type but this actually represents a unary predicate so you're
[3825] saying that the object that will be instantiated by p is an instance of the class professor
[3831] and similarly the object which sees instantiated will be an instance of
[3836] the class course and then you say that the professor teaches a course and the course has a title that is represented
[3842] by t okay so this is just the graph that represents the query structure
[3847] in addition so this is just the basic form in addition we have several than other operators that make sparkle
[3854] actually a more powerful language there is union uh there is an operator optionally we
[3860] say some words about this then there are complex filter conditions which can be
[3866] considered similar to selection conditions in uh in a conjunctive query and then we have
[3872] also aggregation operators there is also forms of negation and then in fact in spark ul 1.1 which is the the current
[3880] version we have also a regular expression so called property paths that allow to
[3885] express navigation using transitive closure so spark l has also has these features
[3890] as well now let me just say a few words about uh okay this is the simple form these basic
[3897] graph patterns they already mentioned it's a bit slow
[3904] and we can now evaluate such a query with a basic graph pattern over an rdf graph by
[3911] just using graph matching so we match the graph of the query with the graph of the rdf data
[3918] and the nodes that which we match the variables that appear in the query head
[3923] in the select clause of our query those represent the answer that we
[3929] provide so the answer is a list it's necessary not a list it's a set of instantiations of the answer variables
[3937] for example here we see that these four answer very very instantiated can be interested in two ways by
[3943] matching this uh basic graph pattern in two different ways over the graph that you see here and this gives us two
[3949] answer uh quadruples in this case because we have four answer verbs okay
[3957] uh okay this i don't think it's so important it's just i think i'm using this somewhere on the
[3963] when i use a when i have a basic graph pattern made up of several trippers they are all
[3969] terminated by a adopter i can also group them together and write
[3974] them in a bit more compact way by avoiding to repeat the first component of the triple effect puts here a semicolon instead of a dot this is just
[3981] syntax it's just syntactic sugar
[3988] [Music] what is more important is that i can obviously do also projection in sparky
[3995] so i do not need to put all the variables that appear in the graph pattern
[4001] in the select clause and those verbs that do not appear they are projected out in this case i want only to return
[4008] the last name and the title the last name of the person who teaches some course together with the title of the
[4014] course i'm not interested in the id of the course itself and
[4021] so this is just projection and why i'm mentioning this because uh
[4026] regarding this there's a difference between conjunctive readings particular quiz in their semantics that becomes
[4032] relevant when we deal with ontologies now uh
[4038] we have here just a very simple correspondence between the star ql query and the corresponding conjunctive query
[4043] but just viewing each triple if the triple is rdf type this becomes a unary predicate i don't have one here but if
[4050] the triple is another one that uses just uh a data object property this just becomes a binary predicate so we have here three
[4057] triples that corresponds to three atoms in the body of my conjunctive query and
[4062] the variables that are in the select clause are the answer variables of my query okay so it's an immediate correspondence
[4069] you don't need to say what the conjunctive if i have a projection then i will have in the head of the query
[4075] only subset of the variables okay so again i have this correspondence between sparkier and
[4081] and conjunctive queries now there's have a difference when we come
[4087] uh to the semantics of sparkuel and conjunctive chris in the presence of an
[4092] ontology why because in spiritual all the variables that
[4097] appear in the body all the verbs that appear in the body
[4103] they require to be instantiated on nodes of my rdf graph okay also those that are
[4109] projected out so here for example i'm projecting out the p variable still in order to find a
[4117] match for this query on the graph i need to match this p variable on some node of
[4123] the graph now if i just have an rdf graph there is no difference between
[4128] the conjunctive query and the spark different comes if i have an ontology because if i have an ontology this
[4134] ontology might imply existentially certain nodes so certain nodes might not
[4139] be present in the graph but they are existentially implied now if i have such nodes that are existentially implied and i evaluate
[4146] this conjunctive query over my graph then the existentially quantified verb
[4152] in the conjunctive query in this case this one can also match these existentially implied objects so
[4159] whereas in particular this is not the case so all the variables including those that are appear just in the body
[4165] and not in the head need to match some node in the graph okay so this creates a difference
[4170] uh in the evaluation of spectral queries and conjunctive queries in the presence of ontology and this is
[4176] quite relevant because uh practically this means that the evaluation of spark2l queries is
[4182] simpler than the evaluation of conjunctive quiz over knowledge graphs or rdf graphs in the
[4189] presence of an ontology okay yes
[4201] yes but so if yes i will say something about this later
[4206] uh but if you now reformulate sparky l queries according to the our so-called
[4211] altitude entailment regime which means taking into account the reasoning that is done over the
[4217] altitude ontology you need to take into account this difference so the existentially quantified verbs in this
[4223] particular so the the verbs that appear just in the body of the of the specular query
[4229] they need to match nodes that you have explicitly in your graph in the rdf graph and
[4241] so if you use the if you use a formulation algorithm for conjunctive queries you will get the answer
[4247] according to the semantics of conjunctive quiz which is not the same semantics as part 2 l so this means you need to adapt the
[4253] reformulation algorithm to take into account the sparkvue semantics it's not the same reformulation as you have for
[4259] conjunctivitis in fact it's simpler because you don't need to do this form of existential reasoning essentially
[4270] and if you talk to uh more applied people
[4275] in fact they say this extension reason is useless okay and uh
[4281] they are advocating to actually switch it off because it just causes additional overhead
[4288] and they say that anyway users don't really understand this existential reason they
[4294] don't count on it and one should just switch it off this is the practical attitude i always have
[4299] discussions with benjamin with the see the cto of uh on topic about this aspect
[4306] but the experience is that in practice people don't want this
[4316] sorry no it's not exactly no no the ontology so the the the part of the ontology that causes
[4323] existentially quantified objects to to be considered that part is uh is not needed according to
[4330] what counts in the ontario is the whole is the reason with respect to the hierarchies but that as we see later can be done so
[4338] reason results hierarchies can be done in a more efficient way by uh in the context of mappings we'll
[4344] talk about this by the so-called mapping saturation process that we mentioned later so this can be dealt with in a
[4351] more efficient way and then if one switches off for this reason with respect to axons that have
[4357] an existential quantifier
[4365] yeah yes and no but the data log is is not is not ac 0 i mean if you have a
[4370] data it depends what you want to use of data yes
[4382] yeah ok this was illustrating this difference okay but i think uh uh
[4388] when you you can look it up late on the slides it's it's what i just explained here on the in
[4395] terms it's just uh working with the models of of the ontology
[4400] where you have here an existential accent that implies an object that allows you to answer this specul
[4407] query using existential reasoning so it's a simple example that shows the difference between the smart parking
[4413] semantics
[4419] you may lose
[4438] it depends i mean you don't so you saturate the mapping so you you you take into account all the reasoning with
[4444] respect no yeah but yes yes i agree with you but that's that's the discussion i have i mean i agree with you
[4450] but the so the argument by the practitioners is that this
[4456] information that you lose these answers that you lose are not really relevant because users anyway don't count on that that's uh
[4464] but i mean i i i take your view i mean if you switch it off you lose so your answers are incomplete with respect to
[4471] the semantics of uh of conjunctivity but be careful because partial has a different semantic so in fact in spark2l
[4478] this is what you want to have unless you write your queries using anonymous variables which you also can do i mean
[4484] one one has to pay attention i mean in this particular you can also have anonymous variables which means you
[4489] don't mention the verb explicitly although you have there an existential implied variable but that
[4495] one cannot appear in a cycle so it's only a three-shaped query that you can express and that one
[4501] that that's why it makes a difference right but the argument is that this is
[4506] practically not significant what you lose there
[4529] yes but yes but this aspect this aspect i will talk about this how at least we
[4535] propose to manage this because this is tightly connected with how mappings are managed and this is this exponential
[4541] blow up in general can be avoided by using uh queer optimizations that take into
[4547] account the mappings and by using other techniques which which i wanted to talk about actually i don't know where i will
[4552] be able because i'm very slow i see i started no i mean okay
[4558] so you know it's ready for yes okay i have started i still have some times
[4564] i i will come to this but i agree with you and with andreas that by switching it off we might lose some
[4571] answers i'm not saying that that switching it off
[4578] gives you the same results
[4583] uh the other point i want to mention uh i will not have time to go into the details about optional but option is
[4588] another construct that is present in spark ql that causes significant complications in this
[4595] case sparkle is more complicated than conjunctive quiz because we don't really have optional in conjunctivitis now what
[4601] is optional option allows you to match a part of the so to obtain enhance
[4606] answer instantiation for a variable if there is a match but if there is no match you still obtain the instantiation
[4612] for the other parts of the variable for for example in this case we want to return uh the per person together with the last
[4620] name and also the first name if the first name is present in the graph now for example here we have that
[4627] for uh anna anna rossi we have the first name and the last name so ana ross is
[4634] is here it's that object okay p38 who has a last name but also first name so
[4640] we'll return a match for all three variables instead for art we only have
[4645] the last name but we don't have a first name still since we require so since in
[4650] the query the first name the instantiation for the first name is within an optional clause
[4656] uh we still return a match for the other variables that are out of the option okay so you can return partial matches
[4663] so you see in sparquill you don't really always return
[4668] tuples that have the same arity as the number of answer variables but in the case of optional you might have some of
[4674] the answer verb is not instantiated that's why in fact technically the answer to a sparkly query is a set of uh
[4681] instantiations of the answer variables not a set of status
[4687] so this optional uh intuitively corresponds to an outer join in in sequel that you would have in a sql
[4693] query okay because also in an outer join you might have an l value in sparky you don't return an algorithm you just miss
[4700] a match for one of the answer variables
[4705] and i will not say anything more about optional but optional uh complicates query answering
[4713] substantially and it it requires and if you want to optimize
[4719] queries you need to to take this into account experience so there's work on optimizing also specific areas
[4726] respect to the presence of options also because it has the way it's defined
[4731] semantic is defined you have some form of negation due to the presence of option
[4746] ok so i just talked briefly about basic graph patterns and briefly about optional i
[4752] mentioned the other constructs that we have in sparc ql uh i will not use this so i didn't even introduce them
[4759] but obviously if you want to consider uh sparkle properly in this setting you
[4765] need to deal with uh with all these constructs uh and in particular for example the
[4770] technology that we are developing the on top system that is developed in bulgarno these with all these constructs except
[4776] currently for path expressions which uh outside of of the fragment that we support at the
[4782] moment but an important aspect is for example aggregations goodbye operators and
[4787] aggregation functions which is a key aspect if you want to use this language in practical settings
[4797] okay now let me come instead to a key point which is the mapping language so how to map an ontology to a
[4804] relational database now the mapping is the is the component
[4809] of this architecture that encodes how the data and the sources should be used to create the objects and the values
[4816] that are present in this virtual knowledge graph that the user then virtually queries okay so
[4823] it tells us how to construct this virtual knowledge graph formulated in terms of the vocabulary of the ontology
[4830] now as i as we were saying here's just a summary of what i was already saying the
[4836] queries are formulated over the virtual knowledge graph so the quiz answered with respect to the ontology and the
[4842] data of this virtual knowledge graph but this is not materialized it stays virtuous and
[4848] intuitively the mapping is then used to translate the queries over the ontology into queries over the data sources
[4854] that's how we use the mapping we don't use too popular we don't use it effectively to populate the knowledge
[4860] graph use it to translate the queries okay we define the semantics of the whole system in terms of
[4865] the knowledge graph that is being generated through the mapping but then the actual pre-answering process
[4871] translates the queries
[4876] now one aspect that is also dealt with by this mapping is to deal with this so-called
[4883] impedance mismatch the fact that at the lower level we have a database that stores values so strings numbers
[4889] integers whereas at the upper level we have an ontology that stores objects so abstract objects that have an identifier
[4896] so we need to create these objects from the data and the sources and that's what the mapping also does so it
[4903] is a way to specify how the object should be created the level of the ontology from the values obtained
[4909] through from the sources so this specification is embedded in the mapping now how does this mapping look
[4916] like the mapping is uh consists of a set of so-called mapping assertions each of these mapping
[4923] assertions has a sql query on the left hand side this is what we call the source part of the mapping the source
[4929] query which is the sql query and it has a target part and the target part is a
[4934] set of so-called triple patterns i would say in the second world disease so these triple patterns are essentially
[4940] atoms and these atoms have as predicates the classes and properties of the
[4945] ontology and they make use of the answer variables of the sql query that's why
[4950] here i use these x x are the answer variables of the sql query they appear in these triple patterns and
[4957] uh the triple patterns contain also this third the steed that stands for
[4962] for terms that technically are called iri templates uh we say a second on the next section
[4968] about i will say something about this on the next slide but intuitively it's these iri templates that tell us how to
[4976] construct valid iris for rdf from the
[4981] values in the database essentially by concatenating the values coming from the database with among them and possibly also with string
[4988] constants okay so we construct an identifier through string concatenation intuitively
[4995] and uh yes so when i use
[5000] a variable of the source query this is meant to be the answer variable of of the sql query and the mechanism with
[5008] which we construct these objects is the following so the idea is that the answers that are
[5015] returned by the sql query each tuple that is an answer of the sql query is used so the values that are
[5022] returned is used in this item place to construct the object identifiers
[5027] and specifically what we have in these triple patterns we have a set of
[5032] triple patterns that have this form they are either rdf type assertions so asserting that
[5038] an ira that refers to some answer verbs of the sql query is of a certain class
[5044] it belongs to a certain class so c is a class of the ontology or that two iris that are constructed using the
[5052] answer variables of the sql query are connected by a certain property so prop
[5057] here is a data or object property of the ontology and the idea is that each answer
[5064] template is returned by source query when it is evaluated over the database for each such answer variable so so for
[5071] each such answer tapper the id template generates either an object or a value depending on
[5078] the form of this id template and this object value populates the virtual knowledge graph and specifically
[5083] populates the classes and properties according to what is specified in these templates
[5089] so this is a way to provide this solution to this impedance mismatch the fact that we have values in the database
[5095] and we have objects in the ontology
[5102] um
[5125] no this is all related to how you do this transformation and this is related to what i will be talking about about
[5130] how to design these mappings and there are specific patterns and they will talk specifically about mapping patterns that occur frequently when you
[5138] do these mappings okay so there are specific forms that are related essentially to the keys that you have in
[5143] your database and the foreign keys that you have in the database that tell you which are the values that you should use to generate these object identifiers
[5150] let me just give you a simple example here so i use now the the i don't use the i told
[5158] you don't use the hardware ml language because it's unreadable i use a much simpler language which is equivalent in
[5165] expressive power to r2ml but it's much easier to read it's the one that we have in our system
[5170] uh i was saying when we have a mapping we have the source part which is a sql query
[5176] so here i'm assuming to have a sql query over a movie table i will introduce this example in a second
[5183] where this movie table has some attributes movie called a movie type movie type and attribute type so here
[5190] simple sql query and then there is this target part which is made up of these
[5195] triple patterns for example these are two triple patterns that could appear in the target part of this mapping
[5201] and i have a second mapping that has a different source query and a different target part in this case i have only one
[5207] triple pattern okay now let me discuss this example okay
[5212] so assume let's assume we have this ontology a very simple ontology the one that we saw before about our movies and
[5219] actors and i'm always actually only using a part of this ontology i'm only using the part that is actually referred
[5225] to in the mapping in the right in the target part of the mapping because i'm constructing
[5230] instances of the class movie of the class let's see the mapping of the class
[5238] uh sorry of the class movie of the title data property under acts in object
[5245] property so the title is a data property or an attribute if you want of the of a play xen connects movie actors
[5253] to movie okay so i want to populate the part of this ontology using these mappings and where
[5260] do i get the data to populate this ontology i get it from two database tables so i suppose assume i have a
[5267] movie table that stores that has four columns possibly additional ones
[5272] but here i'm interested only in this four it has a movie called a movie title a year and the type of a movie actually
[5280] here i'm assuming the view that our kids have for them and movies movies and series they are somehow in
[5286] the same category so i have here actually both movies and series so for example the matrix the movie that was
[5292] produced in 1999 altered cardboard is a series in 2018 okay and in this movie table i have both
[5299] movies and series and distinguish them by this type attribute plus then every every movie has its code
[5305] instead in the actor code i store the information about the name of the actors a code i said to the actor but i also
[5312] store in which play the actor plays okay here there is a code that tells me that can you read
[5319] the plays in this this movie and carrion moss plays in this other
[5324] movie and which is this movie actually is the matrix and harrison ford the plays in blade runner okay that's the
[5330] intuition behind this table now you might say this is not a very good table because it's not normal life you're right it's not normalized but
[5336] i don't have the control over this table right so this is a table that someone has given me i have to deal with it
[5342] that's where the information is that i want to access i might not be able to modify this table i can only query okay
[5349] that's the typical setting in which we are when we access legacy data sources okay and
[5356] they're often badly designed so for example here they are not normalized now
[5361] what do i do here i want to populate this ontology from this table so i can define two mappings the first one
[5369] queries the movie table just the movie table okay and in fact here i'm interested in populating the movie uh
[5375] class just with proper movies so i want a a query here
[5380] uh the movie table filtering according to the types i only want those movies that have type and not the series okay
[5387] and i returned the movie code and the movie title and now what do i do with this i use the movie code to create an
[5393] object that is a movie object and to create this object i obtain i put a
[5399] prefix as a string the string colon m slash followed by the code of the movie and
[5406] now intuitively it seems reasonable why because intuitively i could imagine although nobody is telling me this that this
[5412] movie code is a key in the movie table so it's a reasonable way to create a movie object using the code okay and in
[5419] fact that's what i'm doing and they put a prefix to distinguish the movies for example from the actors
[5425] and what i do i say that this movie belongs to the movie class and i also say that this movie has a title that is
[5433] the title obtained as an answer to this query okay the movie title is here string this creates a literal which is a
[5440] string value that is obtained as the year as the title here okay
[5447] so if i apply this mapping sorry
[5453] if i if i apply this mapping intuitively i use this mapping to apply it to this
[5459] table and i issue the query and was creating the knowledge graph materialized i would get the following
[5466] uh triples in my knowledge graph i would get that
[5471] m5118 is an object in the class movie also m2281 is an object in the class
[5479] movie why because this is what is returned by this query and this triple pattern asserts that these two objects
[5485] belong to the class movie and the first one has the title the matrix the second one is the title blade runner okay so
[5492] this creates this mapping applied to this table creates these four triples
[5497] that constitute part of my knowledge graph if i was materializing this data okay
[5502] this is just to understand the semantics of this mapping and similarly here i have here a query
[5508] that is likely more complicated why because here again i want just the movies so i want uh what do i want i
[5515] want to understand which actor acts in which movie but since the information about whether this is a proper movie is
[5521] contained in this table and it will join between these two tables on the uh on the code so i join p code of actor
[5529] with encode of movie that's what they do here and then i select only those movies that
[5534] have type m and those i return i return this triple
[5541] put in the actor so creating an actor object with which now has a prefix a and
[5547] connecting it to the movie object through the axing property okay and now if i apply this mapping to these two
[5553] tables what i get i get these three triples okay i get that
[5558] the act of 438 which is this one acts in the movie
[5564] five one one eight five seven two which intuitive is carrion moss acts
[5569] in the matrix and the harrison ford intuitively acts in blade runner
[5575] so yes
[5587] do we have an implementation for source to target tgds
[5592] so the point is uh this is a so the this mapping language is essentially the artworm mapping
[5600] language right which has been defined in the w3c community now what we have been doing we are implementing realizing this
[5607] technology in the context of the semantic web technology stack right so in that
[5614] technology stack people expect to use ontologies in our 2ql they expect to use rqrml mappings
[5621] and they expect to obtain rdf data
[5635] yes
[5648] okay but essentially these are the definitions of the mappings i've already told you about the definitions
[5662] okay i would be curious to see this because i mean we are developing tools to do mapping
[5669] design and we have looked at the commercial technology but there is nothing that is really usable in a
[5674] commercial setting as far as i am aware but maybe we have missed something so i would be interested to talk about this
[5692] no no but we don't have just conjunctive queries i mean in the source we have sql queries right
[5701] yes yeah sorry maybe i should have said this yes sorry i forgot i mean in fact in the source we don't want to i mean
[5707] this is not realistic to restrict to conjunctive sorry yeah i was
[5713] i was not very uh aware sorry
[5720] okay in general you you need especially for the data cleaning operations which are very frequent in the setting so one
[5728] of the key aspects of mappings is to clean the data and there you need the way beyond the conjunctive pairs
[5736] then i mean how much power you put in the target queries affects how much you can
[5742] optimize your query processing because the expressive power or sorry of the
[5748] the construct that you use in in the source part of your mappings heavily affects the kind of optimization that you can apply in inquiry answering
[5759] so this is a crucial aspect in general and one has to pay attention to this so in principle
[5765] from a point of view of implementation our tools allow you to write arbitrary sql queries but if you write arbitrary
[5771] sql queries for example with complex aggregation operations or complexly nested queries
[5777] uh the opportunities for optimizations are drastically reduced and then
[5783] you see this immediately because performance goes down if you if you if your queries fall in
[5790] fragments that we are able somehow to parse and for which we can apply optimization techniques
[5795] we are able to uh drastically simplify the generated queries and this is crucial for
[5801] practical applicability of the techniques yeah but in general
[5808] one has to go beyond the conjunct decrease on on the on the source part of the mapping okay
[5816] but also from a point of view of defining semantics this is not really an issue i mean because
[5822] you can have in principle an arbitrary computable query there in principle
[5836] yes let me if i manage okay yes it's a good moment because my machine is against stuck and
[5841] i cannot advance so it's necessarily a good moment in the meantime i try to wake up
[5849] okay we stopped here showing how these mappings work i mean conceptually it's very simple there's
[5855] nothing fancy about this it's just a simple mechanism to extract data
[5862] virtually and construct objects in the knowledge graph i will say something late about mapping
[5868] patterns that tell you how you choose what should be the uh attributes that you use to create your
[5874] object identifiers to use uh in uh your iris to identify the objects so
[5881] there are some common structures and i want to say a few words about this later
[5887] i notice if you look at the number of slides there for you you realize
[5892] as carson also was realizing with his lights but i realizing even more
[5898] dramatically that he will never finish the slide so i will have to cut but i had already foreseen to cut slides it's
[5903] not unforeseen and i know roughly where to cut now this is just about the standard mapping
[5909] language that told you about arturo ml there's not much more to say uh also i don't want to spend too much time
[5916] on formalizing all of this obviously we can give a semantics to all of this in terms of first order of ontologies and
[5923] the semantics is the one that you would expect so uh we provide the
[5928] formalization of such a system in terms of a triple the ontology the mapping and the database schema if we add the
[5934] database we get an instance and then we can define the semantics in terms of the models of the corresponding ontology and
[5942] the mods are defined intuitively by saying what are the objects that you have in your domain
[5949] uh the domain of the knowledge graph that you are constructing
[5956] that you're obtaining from the data through the mappings as if you were materializing it this gives you uh
[5962] an a box in terms of description of the ontology so the the knowledge graph
[5968] on and together with the ontology which means the intentional component
[5973] uh you have then an ontology based setting and you answer queries over these ontology based settings that's
[5979] that's the semantics okay and that's what uh sorry i'm going back that's what
[5985] we are saying here and you compute then certain answers which are just the logical implied answers in line with what carson was
[5991] saying this morning so there's nothing special about this we have this notion of first order writability so the ontology language uh
[6001] this the light family and specific the light r or p2l has been designed in such a way that
[6006] conjunctive queries and universe conjunctive queries are first order rewritable which means if you can rewrite a query
[6015] uh over the ontology in a new query that for example can be a union of
[6020] conjunctive query such that evaluating this rewritten query over
[6025] the data gives you the certain answers to your original query over the ontology
[6030] together with the data and this gives you as complexity ac 0 and data complexity and then one can
[6037] show that this logic is for example log space in in the complexity
[6043] in terms of the ontology and the mappings and mp complete if we take combined complexity but it's
[6048] not surprising because already conjunctive creates a database and be complete
[6053] although here the mp com i mean there's a practically there's a further component that
[6059] contributes to the complexity which is the exponential blow up that you get if you naively apply this rewriting and
[6068] the technique to unfold your mappings that we will talk about in a moment
[6073] so i want you said to spend i would say half an hour on this optimization and
[6078] half an hour on the last part which is this designing the mappings and they give you some ideas about how you choose
[6088] what other attributes you use for example to identify the objects based on a pattern-based approach that
[6095] that helps practically in this technique first a few words about optimization now
[6102] conceptually the query answering process is simple you apply you have a query
[6107] over the ontology you apply rewriting with rest of the ontology actions you get a rewritten query which will be for
[6113] example for a query that is a union of conjunctive query or as particular query you get the union of conjunctive quiz
[6119] over the ontology then you consider the mappings and you unfold your query is related to
[6126] the mappings you get the sql query now this unfolding is not just view unfolding i'll show
[6131] uh some ideas behind this because you have to take into account these iri templates so which are essentially uh
[6138] scrolling symbols that appear in the in the that you have to deal with in doing the unfolding so the unfolding is in in
[6145] practice a partial evaluation of logic programs if you want but you get from that the sql query that
[6151] you evaluate over your database you get your answers then you have to take into account
[6157] the mapping again to translate this relational answer into a set of
[6163] of of instantiations of the answer variables
[6168] of your original spark to help pray if we start from sparky l period that is the answer that you provide to the user
[6174] so conceptually it works like this in practice it doesn't really work like this so if you if you do this in
[6179] practice and you don't apply optimizations the system will just not work i mean our first implementations of
[6186] the system 10 years ago was implementing this from a simple query and not a two complex ontology and simple mappings
[6193] we got the query a sql query that had hundred thousand unions literally hundred thousands and obviously this
[6198] doesn't work uh and why doesn't it work because there are exponential blow steps that
[6204] blow up exponentially what you get is intermediate results and if you don't apply optimizations in that
[6210] setting it doesn't work in practice so
[6215] let me just briefly talk about how first illustrate the simple approach
[6222] behind the query answering and then i will discuss a few optimizations that one can do here
[6230] so the steps are those that i was mentioning before plus there is an optimization step but also this one is not really how it works in practice
[6238] now the first aspect is the rewriting step that i was mentioning so you're writing
[6243] your query with respect to the ontology and now there are two aspects that one has to consider one is the hierarchies of
[6251] classes and properties so essentially the implications that do not involve
[6256] existential quantifies you just have subclass and sub property assertions
[6261] that have to be taken into account and then there is also the part that involves instead the
[6267] actions that have an existential on the right hand side which correspond to this
[6273] participation constraints if you want in a conceptual model or an
[6279] inclusion dependency where on the left hand side you have a unit relation on the right hand side you have a binary relation that implies an extension okay
[6285] so they are considered separately and they have somehow they play a different role in the whole rewriting process
[6292] now very simple if you have uh your action that says that every graduate student is a student and you ask for
[6299] uh and you know that john is a graduate student and your query asked for a student
[6304] in sparc yeah it's written like this obviously you should return his answer john because of the action that tells
[6310] you that graduate student is also a student and now how do you get this very simply by
[6316] rewriting your query sorry no no we don't have the rewriting
[6322] okay this was just to illustrate the idea i will show the writing in a second now this is
[6327] dealing with a hierarchy okay instead if you have an action that says that every student is supervised by a professor and
[6334] you know that john is a student and your query is asking for give me all those objects that are supervised by some
[6341] professor which is particular you could write in this way using an anonymous variable which i didn't explain
[6348] uh then again in this case you would like john to be written as an answer why
[6354] because your ontology actions implies that john is supervised by some professor okay
[6361] being a student so this involves existential reasoning because in order to answer this query
[6367] somehow you need to know that there is a professor although you don't know who the
[6372] professor is clearly there will be some professor who supervises john
[6377] and this is what we mean by existential reasoning the query writing algorithm takes this
[6384] into account and for example if you start from your query that uh
[6391] asks for give me all those x's are supervised by some professor you can use the two axioms that you have here
[6398] that's student the super professor and the graduate students are students to rewrite this query into first of all
[6404] take into account the first action into a query that returns students
[6409] and then once we return student we also want to return graduate students because of this action intuitively very simply
[6416] we apply the inclusions from left to right or if you want to chase the queries related to the inclusions and
[6422] this chase terminates because you cannot generate
[6427] an infinite number of different queries so the query writing algorithm does this it traces the query writes your query
[6434] and this rewriting is finite intuitively because at least for this logic every writing
[6440] step does not increase the length of the right hand side of your query and you have only a finite number of
[6446] uh of different right hand sides or different queries that you can generate
[6453] and this is what the rewriting algorithm does now let me skip this aspect this is related
[6459] to the semantics i mean one can show this logic has a canonical model
[6465] property so we know that there is one uh model that is the
[6470] representative of all the uh models over which you would like to answer your queries in such a way so is
[6477] the representative it means that uh if you have a if your query maps
[6483] to the this canonical model then it maps all to all the other models why because
[6488] there's a homophysics from the canonical model to all the other models okay and so in principle you can answer your query
[6494] just over the canonical model this canadian model in general is infinite
[6499] but the rewriting algorithm essentially uh rewrites your query in such a way that
[6504] there is a match of the original query over the canonical model if and only if there is a match of the rewriting over
[6511] the uh explicitly asserted part of your knowledge is over the a-box okay
[6517] that's the idea behind this and the rewriting algorithm just implements
[6522] this technique let me skip this let me also skip these steps this was just illustrating the
[6528] writing algorithm i just want to show one slide where it's summarized which is the one i wanted actually to
[6534] use it's this one that shows which other writing steps do you apply
[6540] so into very intuitively if you have an atom in your query uh you apply
[6546] the inclusion axioms the inclusion assertions in your ontology
[6551] uh from right to left so for just for example if you have a c2 atom in your
[6557] one of the conjuncts in your unit conjunctive query and you have these inclusion actions you can rewrite
[6563] this conjunct by just replacing the axon the the atom corresponding to a class in the
[6570] right hand side of the axon with the same atom but where you have replaced the class with the one in the
[6576] left-hand side and similarly for the axioms that don't have existentials for
[6582] the actions that have existential in the right you need to pay attention on when you can apply this rewrite instead but
[6587] the idea is very simple you apply chase step of your query or writing step of your query until
[6593] you saturate and you this is the rewriting algorithm that
[6601] saturates your query and when you have obtained uh when you're finished saturating your
[6606] rewriting that's the query that gives you the certain answers now
[6612] okay let me skip all of this sorry i should have just removed these lights
[6618] now simple observation shows that this in general leads to an exponential blow up you can just
[6624] show this by taking a query that has n atoms you want to see n and you have for
[6630] each of this atom you have an axon in the ontology sorry this doesn't react very well
[6638] i don't know what the machine has it's very slow okay so for each of the atoms in your query
[6644] you have an axiom in the ontology where that atom is in the right hand side then you can choose for each of the
[6650] atoms whether to rewrite it or not and for each of these choices you have one union in the conjunctive query which
[6657] means that in the end you have two to the n unions in the union of conjunctive query
[6664] so this means that in practice uh this blows up exponentially and sorry in
[6671] theory blows up exponentially the problem is that this applies in practice as well because it's not very uncommon to have similar situations okay so this
[6678] is not just a theoretical blow up this is related to the 100 000 queries that we got in our first implementations
[6686] uh a similar situation occurs with the mappings now let me just uh
[6695] say a few words about this uh i said when when i was describing the
[6700] mappings i said that we have in the source part the sql query in the target part we have
[6706] a set of triple patterns now practically it's difficult to deal with
[6712] this set of triple patterns so what we are doing at least in our implementation is we split this up
[6718] so we split up each mapping assertion that has a set of paper patterns into a set of mapping assertions that have all
[6723] the same query on the left hand side the same sql query but a single atom in the right hand side because it's simply to
[6729] deal with such mappings that have a single triple pattern on the right hand side
[6735] and this is what we call here the splitting so for example if you have here a mapping
[6741] that populates four triple use has four triple parts in the right hand side we get four mappings all with the same sql
[6747] query okay but we don't forget that these mappings come from the same sql query
[6753] sorry that these formattings come from the same mapping and have therefore the same sql query in the right hand side
[6760] okay let me skip this because this that's not what we are doing we are not materializing that's just conceptually
[6766] to understand what is going on uh instead uh what the algorithm does it uses the
[6773] mappings to unfold the query so it essentially views the mappings
[6779] as a kind of view definition and unfolds the query with respect to this view definition
[6790] okay so technically what we do we we introduce
[6799] we introduce a view symbol for each uh mapping assertion where we have before splitting
[6806] so for each query that we have on the left for each sql query that we have on the left hand side we introduce an auxiliary view symbol and we introduce
[6812] such a view definition where we define this auxiliary view symbol in terms of the sql query
[6818] then we look at the split version of the mapping assertions and we introduce clauses that
[6824] correspond to the split versions where we view simply each mapping that
[6829] you can read as an implication as if it was a corresponding clause where the right hand side the target part of the
[6834] map is just the head of the clause and the que the auxiliary symbol corresponding to the sql query on the
[6840] left is just the body of the clause and then we have we can just view this as a set of
[6846] of clauses and our query contains
[6851] the atoms in its body that appear here in the head and then we just then we just have to find the most
[6857] general unifier between the the query and the heads of these clauses and apply
[6863] the most general unifier to obtain a new query formulated in terms of the auxiliary symbols
[6870] let me just show this on an example here we have these two mappings two sql
[6876] queries on four atoms on oh sorry here four and here three atoms
[6882] here triple patterns on the right hand side this gives rise to seven split mapping
[6888] assertions that refer to two auxiliary symbols corresponding to the two sql queries the first one and the second one
[6893] here we have augs one and out two and uh notice that what we have here in
[6900] the heads of these mappings are the triple uh the iri templates that i have here written as if they were uh
[6906] scholarly functions okay because mathematically they are calling functions so just use this notation
[6912] because it's more compact instead of writing and i write templates okay but this read this is an i template that has
[6917] this as a kind of prefix and then has here the answer variable of the sql query because p called this one of the
[6924] answer verbs of the sql query and so on for the other ones okay so we have here these addition plates
[6930] or column terms in the head of our clauses and now we need to and if we now have a
[6938] conjunctive query that refers to these ontology predicates actor is a class
[6945] name name is a data property and so on and we have here our here are the
[6951] relevant uh clauses that we have obtained from the mappings we can now find the most general unifier between
[6960] the body of our query and the heads of the various clauses that we have introduced
[6966] and this is that you see here is the most such a most general unifier for example the a variable is unified with
[6973] act a code because it uses the same predicate symbol and you can unify it and so on
[6979] so this is most general unifier we can apply it to our
[6984] query and we obtain a new query now that which we have now unified so in
[6991] which now all the atoms in the body now unify with the heads of the clauses
[6998] and we we now substitute each atom with the corresponding body of the clause
[7007] if this advanced will be better we get a new query in which now we make use of the
[7013] auxiliary symbols in the body and remember these actually symbols represent the sql queries that we had in
[7019] our mappings now one thing that we see immediately here i don't want to go into details but we see here that
[7025] the same symbol is repeated multiple times okay so these are self joints and they're introduced by the
[7031] by the mechanism of mapping and folding okay so we see here that we had only two mappings
[7037] but we had seven atoms here so the aux one uh symbol is repeated three times and the
[7044] house two symbol is repeated two times and we also see that for example the first uh argument here
[7051] is the same okay the the play code here aux two is over the same play code okay and this is
[7057] relevant or here aux 1 has the same the same a code in the second component
[7064] for example and this is an issue because this query is not the
[7071] the best that one could produce if one has additional information for example if we know that
[7077] uh in our in our query the the play code that is returned by this
[7083] query is somehow a key of the tuples that are returned by this query then we know that these two atoms can be
[7092] replaced can be unified by a single atom so this query becomes equivalent to the one in which we place the two atoms by a
[7099] single atom okay and in which these underscores which are anonymous variables for example the last one is
[7104] unified with the matrix okay so we can optimize this query uh exploiting the fact that
[7111] the first component here is a key of this of the returned relation if we have this information obviously
[7118] but this is one opportunity for optimization
[7124] this one just shows that also in this step we have an exponential go up it's again a simple example analogous to the
[7130] one of the rewriting now just worked out with mappings where for each atom in my
[7136] query i have now two mappings that essentially uh can be um can be used to unfold these
[7142] atoms and again here choosing one or the other i get an exponential number of different unfoldings okay so we have an
[7148] exponential blow up in the rewriting a potential exponential blow up in the mappings again this is not just
[7154] theoretical this occurs in practice because it's very common that for the same symbols in your ontology you have
[7161] multiple mappings that define the symbols as soon as you have two sources that contain the same information these two
[7167] sources will be mapped to the same symbols so this gives rise to two different
[7172] ways to unfold your queer that contains that symbol okay and in practice this occurs
[7178] okay so again we have this exponential blow up [Music]
[7184] now to take this into account there are many ways to
[7189] exploit this unfolding and do this unfolding in practice so the one that i've shown you is just the one in which
[7195] you simply unfold each atom separately and so what you generate from a single
[7201] conjunctive query if you unfold the each of the atoms in your the body of your query with respect to the various
[7207] mappings and for each of these unfolding you generate a new conjunctive query in
[7212] a big union you get this exponential blow up but in practice you might do it also differently you might instead of
[7220] unfolding each atom separately you could unfold an atom with a union another atom with the other union and then
[7226] construct your query as a join of unions okay now what is better than what is which is
[7233] the best which is the battery uh unfolding and reformulation that you can produce
[7239] you could say obviously the beta one is the one that computes a join of unions
[7244] because instead of being exponential this joint of union is just has the same size as the query
[7250] the problem is that this joint of union if you look at how this is generated will be a query that requires to do
[7257] joints over uh terms that are constructing applying the desired templates so in
[7264] practice the query that you get is a query that will contain joins over string concatenation operations
[7270] and the database engine is not able to do any optimization on this query and is not able to apply any to use any
[7277] indexes that it has in order to compute this query in practice although this prism much smaller when you go and
[7283] execute this query it might take much much longer to execute so it's by no means clear that it's better to compute
[7291] a join of unions as opposed to a potentially exponential union of joints so this is a clear optimization problem
[7299] you can and in fact that's what what we have done david uh was a phd who is now an
[7304] assistant professor in bolzano as part of his phd thesis implemented a
[7309] cost-based optimization algorithm that was exactly evaluating the trade-off between these two approaches and what
[7315] came out on several experiments that he was running is that in practice there is no solution that is better this depends
[7321] i mean this cost model gives you cases in which it's better one for the union or it's better to to
[7328] keep the unions and make a joints of unions and in general it's a combination of these two approaches
[7335] so there's no simple solution to this aspect on how how to optimize this
[7341] obvious depends on than having an accurate cost model so this is a typical database optimization problem but one
[7347] that comes up in the setting and is not the typical optimization problem that you
[7352] you can just give to your database engine so database engines are not able to uh compute the optimal
[7359] uh optimizations for this kind of queries to optimize these queries in in a suitable way because these are not
[7365] typical queries that the database engine is fed okay so they are not able to do this
[7371] optimizations now
[7377] a few words about this aspect because in fact an approach that is
[7383] helps in getting more efficient queries is the one based on mapping saturation so the
[7389] idea is that when we want to compute the unfolding of a query
[7397] this is an operation that is done at runtime so when we
[7402] issue the query over our uh of our ontology based integration system
[7407] this query is processed this rewritten is then unfolded with related to the mappings now if you do this operation at runtime
[7415] this has some some cost that you pay at runtime in practice however
[7422] i mean there's some uh computation that you can anticipate and pre-compute that makes
[7428] them the computation of your rewritings more efficient in terms of processing time and this is
[7435] this aspect of a mapping saturation that i want to mention
[7440] and this related to these two kinds of uh ontology actions that we have those that i mentioned before sorry
[7447] that are related to the hierarchies these are simple axioms that don't involve existential on the right hand side and
[7454] those instead that are related to the existentials and this can be treated differently as a was mentioned before
[7460] namely we use for those actions that involve existentials
[7465] uh a rewriting algorithm that is not the one that i was illustrating before that
[7471] is a trivial one this is a more sophisticated one called the tree witness rewriting that was developed
[7477] by people in birdback some years ago and we use this together
[7483] with a mapping saturation technique that uses the mapping in order so uses
[7489] the mappings in order to so sorry use the ontology actions in order to enrich the mappings so instead
[7496] of working with the original mappings that have been designed by the user we use the
[7501] axioms that appear in hierarchies so the simple ones in order to enrich the
[7506] mappings and get a larger set of mappings very simple again it's nothing smart not
[7513] nothing fancy it's very it's very simple approach if you have a mapping that maps
[7518] a sql query to a term that has a concept a class
[7523] and this class appears in the left hand side of an inclusion then you simply enrich the mapping with the same mapping
[7528] that has the same sql query but now on the right hand side it has the class that appears in the right-hand side of
[7533] the tools this is simply a chase of the mappings with respect to the inclusion
[7539] assertions in your t-box okay and the same you do for uh inclusion assertions domain and range
[7545] assertions and for property inclusions okay so you saturate your mappings with respect to the axioms in your t-box and
[7552] in this way you get a richer set of mappings
[7558] now you get a richer set of mappings it will
[7563] still be uh polynomial i mean at most you get a number of mappings that is equal to the
[7568] size of the ontology times the number of original markets that you have
[7574] now why is this good you might say yes okay you have traded one for the other uh and
[7579] in this way you have gained much to some degree this is true but uh the
[7585] point is that working with saturated mappings gives you additional opportunities for optimizing the mapping
[7590] itself and pruning the mapping itself let's look at the simple exercise okay
[7595] this is just an example of a mapping saturation so suppose we have here
[7600] these few axioms in the ontology student is a person post office faculty and so on we have here these mappings
[7608] and you see these mappings access just a few tables tuned academic
[7614] teaching an academic table and they populate uh these classes the
[7621] idea here is for example that in the database we have an academic table where
[7626] the code nine in the position type indicates postdocs whereas code 2 in the
[7632] position type the position attribute of the academic table indicates for professors the typical
[7638] situation right you have a table and there is some attribute that encodes some information that
[7643] ontologically is relevant because in your ontology you distinguish between postdocs and professors in the table
[7649] this is a low-level encoding done through a specific code okay this is a very common situation
[7656] now if we saturate our mapping by applying for example
[7663] the fact that the student is a person to the first mapping we obtain the the
[7669] mapping the number six here this is analogous to this one where we just replace the student class with the
[7675] person class and so on for the other ones okay so it's easy to see that if you unfold the
[7680] set of mappings with respect to these axioms this hierarchy of classes
[7686] we and also domain a domain assertion that we have here we obtain a larger set of mappings that should then be added to
[7693] the original ones that we have okay so we obtain a larger set of mappings here
[7700] now the idea what is the idea behind this mapping saturation
[7706] the idea behind this mapping saturation is that we can then use it in fact we can first of all we can use the
[7713] saturated mappings together with the existential actions only and get rid of
[7719] the axioms that are the hierarchy actions in the ontology so
[7725] we enlarge a set of mappings but we reduce the actions of the ontology that we have to consider
[7731] the effect is that this rewriting step would be simplified but the mapping and folding step would be more complicated
[7737] because we have more mappings okay so in principle this might not give you might not gain you much because you trade one
[7744] for the other okay but there's one observation that we can do namely that the saturation you can do it once and
[7750] for all you don't need to do it for every query whereas uh the t-box action
[7755] they are considered for every query that you answer instead the mapping saturation you do it and then you can
[7760] answer many queries exploiting the saturated mapping so you factorize some
[7765] common operations that you get when you do query answer okay this is the advantage one of the practical
[7770] advantages that you have but we'll see other advantages
[7776] namely the fact that this set of saturated mappings can then be
[7784] optimized and pruned by exploiting information that you have about your database
[7789] and information about the queries that appear in the left-hand side of your mappings for
[7795] example the query we have here in the mappings
[7800] queries that are specific for uh academics with position called nine that populate faculty in this position called
[7807] two they've got the top that populate uh so yeah i think there is an error yeah
[7812] maybe i'm not sure but you know faculty sorry faculties is uh
[7818] is a the class high in the hierarchy yeah that so exactly you know that's exactly the point for optimization so we have here
[7825] due to the saturated mappings we obtain the population of the same class both for position nine and for position
[7832] two memory faculty on the other hand we have here another mapping that is mapping number five that populates
[7838] faculty without any selection condition on the position now clearly uh this query here is just a more
[7845] specific query it's contained in the query that we have here okay this conjunctive query with a selection condition is a sub is a is contained in
[7854] this one so this means that if we just use query containment to optimize our
[7859] mappings we can actually get rid of this mapping because it populates the same class of the ontology but just with a
[7866] more specific condition so by using query containment
[7871] of the queries that appear in the left hand side of the mappings in those cases where we can because we can do this if
[7877] these are for example conjunctive phrases in this simple case we can in fact prune the set of saturated mappings
[7886] and we might also have more additional constraints for example might have a foreign key over my data over the
[7892] database for example the one that says that if x is a course that is is being
[7899] taught by someone then uh x appears in the first position of the
[7905] academic table okay so this might be a foreign key that you
[7911] know holds over your database and now the information about containment between the left-hand side queries and
[7917] the information that comes from constraints that you have on your database can be used to actually
[7923] optimize the set of saturated mappings in this case
[7928] as i was saying we can get rid of for example mappings number 7 8 9
[7934] and 10 and also 12 and 13 by using a query containment simple query
[7940] containment and also the foreign key i think let me see why we get rid of
[7946] yeah okay exactly teaching is since we have a foreign key from teaching to academic this mapping here
[7953] which populates the faculty class is actually subsumed by the mapping number five that also populates the faculty
[7959] using uh the a code that appears in the first position which is also
[7965] the same code that pc in the second position of teaching so using this foreign key this mapping is redundant
[7972] considering the first mapping so we can prune it so the effect of these optimizations is that you saturate your
[7978] mappings but then you have opportunity to optimize the set of saturated mappings and get as much smaller set of
[7985] mappings so you trade the size of the hierarchies in your t-box
[7992] which would be which would affect the rewriting for a larger set of mappings that then gets pruned down so overall you get
[7999] a simple ontology and in the end a simple set of mappings
[8004] so these are techniques that in practice make the whole process of
[8011] rewriting and query unfolding with the rest of two mappings more efficient and
[8017] together with other optimization techniques in the end this leads to rewriting queries that
[8024] so to rewriting techniques that produce queries that are similar to those that
[8031] users would produce manually if they were implementing
[8036] the rewriting over the database directly instead of using the
[8042] ontologies and intermediate steps
[8048] so we are now to the point where when there are these opportunities for optimization
[8054] and opportunities for optimization are given by the presence of constraints in the database
[8060] like keys and foreign key constraints i mean the other aspect that i hadn't mentioned and i think i don't have time
[8067] to do it i have some have some slides is uh using the keys to uh
[8074] to prune the to prune the unfoldings because you can eliminate uh
[8080] many of these joints that would be produced by these unfoldings okay due to
[8085] the presence of key constraints and also of incompatible iris templates
[8090] so this leads in the end to uh techniques that produce
[8096] queries that are comparable in size those that would produce manually
[8102] okay let me skip this instead let me say something about
[8110] this process of designing mappings
[8118] now the form of the mappings is something crucial in the performance of the
[8123] resulting system i mean it's crucial in terms of performance but
[8129] it's also crucial in terms of semantics of the overall system so the mappings clearly need to reflect the semantics of
[8137] the data in your data sources and of the domain knowledge that you have in
[8142] your ontology so we required these mappings somehow
[8148] on the one hand allow for efficient processing on the other hand capture correctly the
[8154] semantics of your system now first of all we can make some simple observations about the form of such
[8160] mappings uh and you see them here so one is that
[8165] when we whenever we write a mapping we should try to have uh in the uh source query so the sql query
[8173] that is part of the mapping it should be you should have the simplest form that is possible
[8179] and uh this leads to the fact that we should try to write mappings when mappings are
[8186] being designed one should not try to put a lot of triple patterns on the right hand side together
[8193] and populate them with the same sql query because this might lead for some of these triple patterns in the right to
[8198] a query that is more complex than what is needed to populate that mapping okay this is one observation so it's better
[8204] to split the mappings into many small mappings rather than having few larger mappings
[8210] because the few larger mappings are more likely to contain redundancy and unnecessary complexity in
[8215] the query on the left in particular this is related to joints in this query so one should as much as
[8221] possible avoid unnecessary joints in the source period
[8228] and yeah this is what greater water was saying before so these atoms should be combined a single single mapping
[8233] assertions only they really require the same query and
[8238] yeah also another important aspect is the form of desired templates
[8246] one needs to pay attention across a set of mappings to have a consistent set of error templates so
[8252] when the same so somehow the same into the same objects should be retrieved through different
[8258] queries and populate the same classes or related classes one is to pay attention
[8264] to make use of the same iri template so that really these objects that we construct are compatible
[8270] in the way they populate the different classes now these are some simple observations
[8276] that one can apply but these in general are not sufficient to ensure a good design of the over set of mappings
[8282] especially in complex scenarios so how can we proceed there
[8290] so the idea is to exploit somehow common patterns that appear in data sources
[8298] so why because in general we have in the data sources pattern that occur
[8305] frequently and that are common because data sources in general follow
[8310] common design principles that are being applied when the data sources have been developed and the corresponding database
[8316] have been developed so this is related to uh
[8323] to the presence of typical forms of constraints that occur in relational databases the consequence
[8330] of the database design process and this is related when we are talking about the tpl form of constraints we are talking
[8336] about key and foreign key constraints which are the most commonly used in relational databases
[8343] and in general when we have certain occurrences of such combinations of keys and foreign keys in
[8350] the data sources certain currencies are an indication that in ontology you want to populate
[8357] classes according to certain patterns and we try to identify
[8363] such common patterns that you find data sources and how they give rise
[8368] to common structures at the level of deontology and tends to structure that you want to see reflected
[8375] in your mappings now one observation that one should do here is that the constraints that we are
[8382] talking about of our data sources might either be constraints that are explicitly specified because
[8388] data sources relational databases have constraints are specified but very often
[8394] such constraints are not even explicitly specified why i mean there are many reasons why database designers or
[8399] database administrators in fact remove constraints that are present in the database
[8405] for performance optimization or because the data is not clean enough to respect
[8410] the the constraints although it should respect them because there are constraints that value and domain
[8415] there's some dirty data that will dilate the constraints and therefore database administrators in fact remove
[8421] the constraints from from the database engine or they're not present because the other mechanism by which actually
[8427] these constraints are enforced over the data for example because the database is accessed through
[8432] specific applications that ensure themselves that the constraints are satisfied so there is no reason to
[8438] enforce additional reconstraint in the database because this would be a payment you paint
[8444] so this has a penalty in terms of performance of the database engine so
[8449] however these constraints semantically hold over the data and therefore it's important that
[8455] in such mapping design process they are actually taking into account so one should not just look at the
[8461] explicitly declared constraint but also a constraint that for example could be mined from the data using data profiling
[8468] techniques which analyze the data sources relations data source and try to extract the various
[8473] kinds of dependencies keys foreign functional dependencies that hold over the data and they can be taken into
[8479] account in the mapping design process and also actually in pre-optimization for
[8484] the query writing so yeah this is related to the fact that
[8490] uh when databases are designed one follows some conceptual modeling principles that
[8497] are applied in the database design process and this means that the database schema that
[8503] one actually has available actually reflects conditions at holding the application
[8509] domain and often the design process is done using
[8514] some semantically rich models for example entity relationship diagrams that are often used in database
[8521] design now one problem in this setting is that these models are used during the design
[8527] phase of your data sources but then they get lost when the actual database is uh
[8532] deployed so often the whole information that had been acquired and
[8537] was present about the domain gets lost when the database is deployed however this information is not it's lost in the
[8544] sense that it's not it might not be present anymore but it's still reflected in some form or another
[8551] either explicitly in some database constraints or possibly in the structure of the data that
[8556] respects certain design principles because for example your database is normalized
[8566] so this is this observation so we have in our database often uh
[8571] footprints of the design process that led to the
[8576] development of a specific database and the idea is to exploit this information so to make use of this information in
[8583] order to support the mapping design process
[8589] so which means that we should take into account various kinds of information first of all the relational schema with
[8596] all the constraints if they are present also somehow the conceptual schema that is at
[8603] the basis of the relational schema that we are working with data that is stored in the database when
[8609] we have access to the data this is not always the case there are situations where one has direct access to the data in the
[8616] process of design some other situations you might not have access but if you have data stored in database and you can
[8623] access it then you can for example profile this data this might give you additional useful information
[8630] and also uh possibly domain knowledge that might be present in the whole sort
[8636] might be present in the heads of the people who carry out the design or it might be already present in some
[8641] ontology axioms that are available because we might work already with a domain ontology that
[8647] is available when designing the market okay so all this kind of information can be taken into
[8652] account and i want just to give you an idea of how this is done by describing an approach
[8658] based on mapping patterns and what is the idea of such patterns these patterns take into account these various forms of
[8664] information that's what is listed here okay so they rely on the database schema the ontology when
[8671] present and the mapping that we might have between the two so this is part of the
[8677] pattern specification and also the conceptual information about the
[8683] domain of interest so
[8690] i have 10 minutes i can show you one or two patterns now one observation is that i was meant
[8696] as i was mentioned before these patterns might just rely on schema level information that is available
[8702] or they might also rely on data level information when that might supplement the schema like information
[8709] and in fact the patterns that we specify have a schema version that assumes that the specific
[8717] constraints keys and foreign keys are explicitly present but also a data version where these constraints might
[8725] not be explicitly present but might be derived or available from the underlying
[8730] data that might be accessible there are also some patterns that just rely on the data that requires somehow
[8736] data access i will show you one of those yeah okay i think this is not needed i
[8744] am going to use primary key constraints key constraints and foreign keys the foreign keys the primary keys are
[8749] represented in the usual way using underlining attributes foreign keys are represented
[8754] in this way this means that t1 of a is included in t2 k
[8761] yeah also notice that when i when i draw this when i write this information keys
[8767] and foreign keys the bold phase attributes are not a single attribute necessary this could be combinations of attributes in general
[8775] okay i will not show everything let me just show a few simple patterns we have here several ones but
[8782] i mean i start with a very simple one because this is almost trivial but
[8789] that's one that occurs frequently so the idea is that you have a simple table in your database that has some primary key
[8796] attributes and some additional attributes now often this information corresponds to what it corresponds to
[8805] the conceptual model that was at the basis of this table that was uh specif that contained some entity
[8813] in which these attributes that make up the primary key of the table were identifiers for that entity and there
[8819] are some additional attributes that contributed to this entity as well now this is a very simple situation
[8826] that leads to a situation in which in your ontology you have a class that corresponds to this
[8832] entity okay you have uh some data properties for this class and these data properties
[8839] correspond to all the attributes of the class including the primary key so for each of the attributes that make up for
[8845] the both the primary key and additional attributes you have a data property in your ontology and you assert that the domain
[8852] of this data property is specifically the class that corresponds to this entity and now what is the mapping the
[8857] mapping is very simple it just queries this table okay and creates for each table in this
[8864] table an object in the class and how it is object identified it's identified through the primary key attributes okay
[8871] so and this is the mapping says this okay extract from the table the query is
[8876] just the one that extracts the whole table construct use the key attributes
[8881] which are the answer verbs of which are part of the answer variable of the query that queries the whole table
[8887] use them to construct instances of this of this class and
[8893] assert them to be instances of this class and in addition assert that the instance of this class have
[8899] the values of the various attributes that make up both the primary key and the additional attributes
[8904] as data properties for the corresponding data properties okay so it's very intuitive
[8912] what is written there is what i was just saying just a very simple example suppose you have a client table with social security number name date of
[8918] birth and hobbies in your database you can map this to a client you can
[8924] assume that you have a client class okay so the target contains the client class you have
[8930] for each of the attributes you define a data property so you will have the social security number the name
[8936] uh the date of birth and okay the hobbies i don't have them yeah okay because you might not in your domain not
[8942] all the information might be relevant okay in the ontology you might not be interested in the hobbies of these
[8947] persons although you have a table with many additional attributes some might not be relevant for your domain for
[8953] example here the hobbies are not relevant so they are not mapped okay so we have here mapping that just queries
[8959] this table and populates the class and the corresponding data properties very simple okay
[8965] the key point is we use the primary key to create the object identifier and to use
[8972] here there's also something common use here a prefix this becomes part of the
[8977] name of this ira that is somehow related to the class so i use here for the client class a user
[8984] prefix that reminds me of the fact that here these objects are client objects
[8991] okay now this was a the simplest pattern that
[8997] you can imagine here you have a slightly more involved pattern these are a common situation you have three tables
[9002] where one table has its primary key that is split into two parts so that our foreign keys was the
[9009] primary keys of two other tables now this is a typical situation that would result if you start it from
[9016] an er model where you have a relation that connects two entities the primary
[9022] keys of the two tables that i've called your ttf correspond to the identifiers of these two entities the two tables have
[9029] additional attributes that correspond to additional attributes of the two entities and here this schema would be
[9036] would lead to a relational design that that is made up of these three tables okay
[9041] so we can have a pattern that reflects sorry no
[9047] click on the wrong button so we have a pattern that reflects exactly
[9053] this situation okay so we assume that we have already used the previous pattern to map these two
[9060] entities okay and that map the two tables t and tf according to these two entities so now i
[9066] just specify the additional part that corresponds to this relationship okay so for this relationship
[9072] i have just a source query that queries this table and i create i use since this
[9078] is a binary relationship i use an object property that is inspired by
[9085] this relation that connects that is used to connect the two classes so i have here an object property that
[9090] has the first class as domain c and the second class as range and their service and here i populate this object property
[9097] with the objects that result from the objects
[9102] obtained from the two tables entf okay and here you see the coherence between this pattern and the previous one
[9108] because if i mapped before this table t two objects where i use ke as
[9115] to construct the id of that object now i need to use the same
[9120] primary key to construct the object that i use here in the data prop in the object property okay so this mapping
[9126] must be in aligned with the previous one otherwise i would get something wrong in my ontology
[9132] okay let me just show another one
[9139] [Music] yeah okay this is an example but you can easily here we had the
[9146] client table of before suppose we have also a location table and now we have a
[9151] table address that says that the client has is in a certain location okay and
[9159] yeah and here we have this situation where we
[9164] have the foreign keys right so we have the foreign key from this the address table towards the client and
[9170] location table it's exactly a situation that we had before and we can use this mapping here to populate
[9177] in this case an address property okay with the client and the location in this case the
[9182] location is constructed using the two attributes that make up the primary key of the location the city and the street
[9188] okay and here i use the prefix that is this one
[9194] let me just show a slight variation of this and then i'm finished it's the one where
[9200] so this is related to the fact that we need to pay attention that we align the patterns that come from
[9206] different components of our relational schema so now suppose that i had the
[9212] table t and tf as before and now i had tf with the primary key
[9217] key f and now i have a relation similar to before that has two foreign keys but now this
[9222] foreign key is not was the primary key of this table but it's towards towards an additional key of this table okay
[9228] this is also a common situation so i suppose here i have an additional
[9234] key and for some reason the primary key sorry the foreign key goes to the secondary key not the primary one
[9241] now when i define this pattern i need to pay attention to this you see this is a situation where in
[9247] order to get the so since when i was mapping this table i
[9252] was using this the primary key to construct the objects in the class cf
[9258] okay and now you need to be coherent and if i want to connect objects so i want
[9264] to connect objects of of the class c or coming from this table with object of the class
[9270] cf coming from this table i need to get access i need to obtain to retrieve the primary key that
[9277] was used to construct the objects for the class cf and that's why in this case i need a join between the table tr and
[9282] the table tf in order to obtain the attributes of the primary ttf
[9289] and then i can use this primary key to construct the object that i use here in
[9294] the object property if i didn't use i didn't use a join here
[9299] i would construct an incoherent ontology this is an example that shows that in this case i need a join so i need a join
[9305] between these two tables whereas in the previous case the join was not needed here the previous case i don't need a
[9312] join because the primary key the foreign key is towards the primary key okay so this is
[9318] a typical example that if one doesn't uh have knowledge of how things work uh one
[9324] gets wrong and we see this with uh designs of of of
[9330] mappings that are for example that user join in this case where the join is not necessary clearly using a join is just
[9336] a more complicated equation is more complicated than necessary okay that's what i wanted to say
[9345] let me just go to the end i have one brief summary slides i mean
[9350] there are more complicated patterns that occur
[9357] it's a bit slow in advance
[9365] obviously no i mean i did not it was not my intention to present all this pattern this is it's not that i was
[9375] i hope to show you one more but uh
[9382] okay i think this is also additional considerations now we have
[9388] conceived diverse scenarios of designing such systems where this pattern can be useful depending on what is the
[9394] information that you already have and what is what you want to produce i think we can keep this as well
[9401] we are working on automating the design process and this is using the patterns is
[9407] is a way to support the design process he doesn't want to advance
[9419] yeah i think i've given you a slight brief impression of this approach to
[9425] ontology access and scientology based access integration of
[9430] data sources and there is a mature it's mature in the
[9436] sense that it has been studied the foundations have been well investigated there are mature systems
[9442] that are being deployed in a commercial setting it's not yet mature in the sense that it's widely adopted i should admit
[9447] this this is an effort that we and other people in the community are
[9452] trying to do who are working with this kind of technology so this is not yet a technology that is recognized
[9458] as in the general data integration scenario although it has a lot of potential for
[9464] specific situations we're not saying that this is the solution that fits all problems in that
[9469] setting but uh there are many scenarios in which this is a good approach
[9475] uh yeah also i mean one other work that one that
[9481] we and other groups are doing is tailoring this technology towards specific scenarios the finance domain
[9487] the medical domain and so on i mean by using exploiting relying standard ontologies and
[9492] extensive domain knowledge that are available in these domains this is also so developing verticals in the various
[9498] domains uh the performance issue is still something that is being worked on also
[9505] because it becomes more and more important to support not only relational data but different kinds of data graph
[9511] data tree structure data temporal data is an important aspect there's a lot to say about this
[9517] yeah thank you [Applause]
[9523] many people with homeland work in various places and with some for example with australia
[9532] with avigdor and troy were working on the mapping pattern and roman
[9538] is involved actively in the development of the on top system i didn't show a slide about on top i mean i should have shown
[9544] but i don't have it and yeah i mean the foundations that we developed with the group in rome
[9550] led by maurizio and in bolzano
[9556] several people went through still some of their some have moved and are continuing to work
[9562] some doing other things but yeah thank you
