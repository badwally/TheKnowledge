---
schema_version: 1
id: yt-dyw0VgSrs2A
type: youtube
title: STLab Seminar - Extraction of common conceptual components from multiple ontologies
url: https://www.youtube.com/watch?v=dyw0VgSrs2A
authors:
- Semantic Technology Laboratory
ingested_at: '2026-06-17T19:26:33Z'
content_hash: sha256:b52c35f70887655f9e837d046501b80eb2d7451a740394884a033ba4c88fa4b7
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Semantic Technology Laboratory
  channel_url: https://www.youtube.com/@semantictechnologylaborato3277
  duration_seconds: 4139
  caption_track: fetched
  snippet_count: 1691
filter:
  score: 0.74
---
[10] so welcome everybody
[13] so again today we have our um estee
[16] lauder seminar
[17] today is the seminar is given by
[19] valentina
[21] carriero she's a phd student
[25] in computer science and engineering at
[27] the university of bologna
[30] and she's going to present some results
[33] from her phd work
[35] she's at the second year of phd
[38] this presentation addresses a work that
[42] has been
[42] submitted to a conference under a double
[45] blind review so
[47] um yeah just to tell you that
[50] this is not to be like circulated
[53] until we get the notifications which
[57] which is expected by the 23rd of june
[61] so also the recording will be published
[63] after that date
[65] um and so she's working on
[68] extracting patterns from um from
[71] ontologist
[73] and you will see today some of the
[75] results that she
[77] has got so far and of course she will
[81] explain the the hypothesis and the
[83] method she
[84] she's developed so far
[87] there are certainly lots of
[91] points that can raise discussion so i
[93] hope that
[94] after her presentation we will have a
[97] live discussion of course
[100] as for all seminars but especially for
[103] phd students all comments
[105] critics and suggestions are very welcome
[108] for valentina
[111] so valentina you have 30 minutes i'm
[113] going to
[114] set the timer just in case i'll tell you
[117] when you have
[118] five minutes left yeah i will set my own
[120] timer
[122] okay very close so please
[125] this stage is yours okay thank you
[128] valentina
[129] so in this seminar as valentina said i
[132] will
[133] uh present the initial results of my phd
[135] project
[137] and this is a joint work with of of
[139] course
[140] my supervisor valentino tia and luigi
[142] sprino
[146] this first slide was meant to introduce
[149] some basic concepts and terminology but
[151] considering today's audience i think i
[153] can skip this
[155] and uh so um existing no don't
[159] skip it don't skip it there are some
[161] some
[162] okay so i i maybe i will take like uh
[165] two minutes because i was thirty without
[168] but
[168] you go um okay in this context by
[171] knowledge graph we mean
[173] a knowledge base that encodes knowledge
[175] using a graph based structure
[178] um where the nodes of this graph are
[181] real word entities
[182] and the edges between the nodes are uh
[185] relations between these entities
[188] in knowledge graphs uh the knowledge can
[190] be formally represented by
[192] schemas for example ontologies that
[194] define concepts
[196] that are called classes and relation
[198] between
[199] these concepts uh that are called
[202] properties
[203] so for example we can have uh the the
[206] node dos
[207] yes key and moscow uh and relation was
[210] born in so the cfsk was born
[212] in uh moscow and dostoyevsky is
[215] a person in an ontology
[218] and moscow can be defined as place
[223] okay so uh existing knowledge graphs uh
[226] use many different and heterogeneous
[229] schemas for example ontologies
[231] that correspond to uh different uh
[234] modeling choices
[235] and these ontologies can diverge in
[238] expressiveness
[239] a level of granularity or axiomatization
[243] coverage names and naming conventions
[246] and all these is part of the so-called
[249] in a work by altogether
[252] knowledge problem where the semantic web
[255] is
[255] seen as a knowledge soup because of the
[258] heterogeneous semantics of these
[260] data sets and in this context
[263] understanding
[264] large ontologies and large knowledge
[265] graphs is still an issue
[267] and it is actually a crucial preliminary
[270] step for many
[271] ontology engineering tasks such as
[273] reusing
[274] existing ontologies for modeling data
[277] creating correspondences between
[280] concepts and relations from different
[282] ontologies
[283] evaluating ontologies and querying uh
[286] different
[287] knowledge graphs at the same time
[290] um so ontology summarization
[293] um aims at making these ontologies more
[296] understandable by returning an ontology
[300] summary
[300] so for example starting from an ontology
[304] on cultural heritage
[305] that can define concepts such as
[308] location cultural property
[309] technique subject we will have a subset
[312] or a sub
[314] sub graph containing the only the most
[316] important concepts
[317] based on some measures such as
[319] centrality
[320] the centrality of the nodes um
[324] but in most cases uh for example when
[327] you need to reuse some ontologies for
[329] your data
[331] uh you need to compare different
[333] ontologies and this is not supported
[336] and in order to have an overall
[338] comprehension of one ontology
[340] even one ontology you need to um
[344] uh know all the facts that that ontology
[347] can represent not only the key concepts
[350] uh these facts can be represented by
[352] complex structures
[354] that often express a relational meaning
[357] like membership or locating
[359] and this we call uh these complex
[361] structures conceptual components
[364] a conceptual component is an intentional
[367] counterpart
[368] of an ontology design pattern an odp
[373] defines a set of classes properties
[376] actions
[377] that are needed in order to answer to
[379] certain competency questions
[381] a conceptual component is at a more
[384] abstract
[384] level and it is independent of the
[387] specific
[388] implementation formalization so for
[391] example here we have
[393] the membership conceptual component
[395] which represents
[396] in general the fact of being a member of
[398] a collection
[399] and it is implemented in two different
[402] ontologies with two different ontology
[404] design patterns
[405] the first one is able to answer to a
[408] question for example such as
[411] which are the members of a collection
[413] with the binary relationship
[415] as member between a collection and an
[417] object
[418] the second one is able to answer also to
[420] questions such as
[422] which are the members of a collection
[423] during a specific time interval
[426] with an array relationship membership
[429] with the three arguments including time
[433] so we can imagine ontologies as
[435] compositions of ontology
[437] design patterns that implement concept
[440] of components
[441] and starting from a corpus of ontologies
[445] we can have them classified based on the
[448] conceptual components
[449] implement with different ontology design
[452] patterns
[453] so i think it's already clear how this
[455] can impact on ontology understanding
[457] and comparison of different ontologies
[460] for performing many ontology engineering
[463] tasks
[465] going deeper into our approach we start
[468] from the intuition that
[470] an ontology is developed either
[472] intentionally or unintentionally as a
[474] composition of ontology design patterns
[477] as modeling solutions to modelling
[479] problems
[480] regardless their quality and we
[483] formulate
[484] two hypotheses the first one
[487] is that the density of the of the
[490] connections
[491] between the entities of the same
[493] ontology design patterns
[494] so the density of the connections
[496] between these entities of the
[498] address control design pattern and these
[501] entities of the
[502] odp event is higher than the density of
[505] the connections between entities from
[507] different ontology design patterns and
[510] the second
[511] hypothesis is that the combination of
[513] the words that are used to describe
[516] an ontology design pattern
[519] because ontologies of course are not
[521] only about topology but also
[523] names uh vocabulary is semantically
[526] coherent
[526] with the relation that that pattern
[529] represents
[530] so for example for a pattern about
[531] membership we can have
[534] words such as member and collection
[538] this is our pipeline and in particular
[542] we use community detection
[544] for uh identifying um topological
[547] phenomena such as the one in
[550] our first hypothesis and we use text
[552] clustering
[553] uh for grouping the detected ontology
[556] design patterns
[558] based on their terminology
[561] we apply this method on a corpus of
[563] ontology so
[564] the first step is to build a corpus and
[566] i want to uh
[567] introduce you to uh the two corpora we
[570] used in our experiments
[572] um we built a corpus of
[576] ontologies on cultural heritage it
[578] contains 43 ontologies four of them
[581] are ontology networks that are treated
[584] like a hollow ontology
[586] we exclude ontologies on related domains
[589] such as chemistry
[591] and also top-level ontologies for
[594] building this corpus we use
[596] the linked open vocabularies repository
[599] and
[600] we disseminated an online survey and
[603] we include uh in the inferred versions
[606] when possible that is here for uh 33
[609] ontologies out of 43
[611] uh otherwise we include the asserted
[613] versions
[615] the second corpus is actually the data
[617] set that
[618] was was used in 2020 for the conference
[621] track
[622] of the ontology alignment evaluation
[623] initiative it contains 16 ontologies
[627] uh on the conference domain which is of
[629] course less vast and
[631] cultural heritage but still has
[635] many sub domains like price or travel
[638] and we were able to generate the
[639] inferred versions for
[641] all ontologies um so after being
[645] building our corpus um we need to
[648] transform
[649] our input ontologies in uh graph
[652] structures that a community detection
[655] algorithm can
[657] work on this mean that these ontologies
[660] need to become
[660] graphs that are undirected and unlabeled
[665] we call intestinal ontology graph a
[668] graph that is derived from an ontology
[671] that encodes its intentional level
[673] and that is built by following these
[675] rules
[677] the first rule generates an edge p
[680] between a node d and the node are when
[683] the property p in the original ontology
[686] has
[687] d as domain and r as range
[691] the second rule starts from a property
[694] restriction on a class that can be
[697] existential or universal or cardinality
[701] and generates an edge p that is the
[704] property in the restriction
[705] between the class uh local to the
[708] restrictions c1
[710] and the class that is in the class
[712] expression c2
[714] so we still have a directed and
[718] um labeled graph so we need a
[722] third rule uh if we are starting from
[725] any
[725] uh edge p in our first version of the
[729] intentional graph
[730] between a node n1 and the node n2
[733] we generate an undirected and unlabeled
[735] edge
[736] between n1 and the new node n1 pn2
[740] and another edge between n1p and 2
[743] and the node n2 this new node
[747] captures the context of use of the
[749] property p
[750] that is p was used for connecting the
[754] node n1 and the node n2 and this is
[757] needed because
[758] uh community detection returns not
[761] overlapping communities
[762] so if we have just the the
[765] node p for p this will end up only in
[769] one community well we know that
[772] the same properties and the same classes
[775] can be
[776] uh relevant to many different ontology
[778] design patterns
[780] so in this way we enables overlapping
[782] communities
[783] as you can see we do not consider in
[785] these rules the
[786] hierarchy of classes and properties
[790] so here's an example starting from
[793] this ontology fragment here for example
[796] we have a domain
[798] action on the properties recorded by and
[801] in the ontology we have also the range
[803] action
[804] so event is recorded by location in our
[807] intentional
[808] graph we have a node for the class event
[811] uh the intermediate node for the
[813] contextualized property event is
[816] recorded by location
[817] and the node for location all with
[820] undirected and unlabeled edges
[823] and the same happens for any kind of
[826] property restrictions such as here max
[829] cardinality
[830] involving a data type property with a
[835] with a data type as um
[838] as range some additional notes
[842] when a property has no domain or range
[845] we assume
[846] it has our thing as domain range so we
[849] still keep this property in our
[850] intentional graph
[852] while we do not consider domain range
[855] declarations that involve blank
[857] nodes or uh class expressions in
[860] property list
[860] restrictions like these uh however we
[864] empirically observed that
[865] this has no great impact and at least in
[868] our two
[869] corporate there are a few cases like
[871] this
[873] so now that we have our intentional
[876] ontology graphs for our
[878] input ontologies we need to apply
[882] community detection to each of them
[885] and community detection aims at
[888] gathering together the nodes of a
[890] network
[890] into groups such that there is a higher
[894] density of edges within groups
[896] than between them so it's what we need
[899] we use the uh state-of-the-art closer
[901] newman more algoli
[903] algorithm but after running some
[905] experiments we found that there were
[908] many big and uh with a low density
[912] communities that could be a split from
[916] that could be split in more meaningful
[919] communities
[920] so we found that by running this
[922] algorithm
[923] recursively on communities with a
[925] density lower than the average
[927] density of all communities detected at
[930] the previous step would improve the
[932] results
[936] community detection returns communities
[938] as sets of nodes so
[940] this will this is an example of a
[943] community
[944] after splitting our property
[947] contextualized property nodes
[949] in the original even original
[952] classes and uh property involved
[955] we apply an additional step that is
[958] retrieving the
[959] original the ontology fragment in the
[962] original ontology
[963] uh with with those nodes that represent
[966] um the ontology design pattern that we
[970] have observed uh and we
[973] do this we define a boundary um by using
[976] some heuristics so we
[978] get the triples asserting the type um
[981] of the node domain and range axioms for
[985] the properties
[986] inverse super equivalent properties and
[988] classes
[989] or restrictions on classes that involve
[992] at least one
[993] property that is in the community and
[995] also the annotations so for example for
[998] the node
[999] reduction in one of our communities we
[1002] get all these free rules like also the
[1005] super classes or the comment
[1008] um now that we have our communities
[1012] uh we are ready to um for the clustering
[1015] step
[1016] and uh since we are working on a corpus
[1020] of ontologies um if we cluster
[1024] all the communities from all ontologies
[1026] according to their vocabularies
[1028] we may identify the conceptual
[1031] components
[1032] that are shared potentially by all of
[1035] them
[1036] in order to do so we build a virtual
[1039] document for each community
[1042] by concatenating all english labels
[1045] from the entities of the community when
[1048] there is no label we use the local id
[1050] and
[1051] we split it if needed and we also remove
[1054] the repetitions
[1055] so starting from a community like this
[1058] using the the labels or the local ids
[1061] we get a virtual document like this one
[1067] then we disambiguate these virtual
[1069] documents
[1070] uh by using a ukb that is based on
[1073] wordnet
[1074] and we also include a frame knit frames
[1077] that have a close match with
[1079] the scene sets that in the virtual
[1081] documents
[1083] by using frame server and we add also
[1086] more general
[1087] frames um by exploiting the hierarchy of
[1090] frames
[1091] so starting from this first version of
[1093] virtual document
[1094] we um we get this new version that
[1099] uh has all the scene sets uh possible
[1102] frames with a close match and also
[1104] possible more general frames
[1107] and we use this virtual document for uh
[1109] the clustering step
[1111] um so we use the uh
[1115] k-means which is a state-of-the-art
[1116] unsupervised clustering algorithm
[1119] uh for clustering our virtual documents
[1122] and each cluster uh potentially
[1125] represents
[1126] a conceptual component by um
[1130] putting together all the ontology design
[1132] patterns that
[1134] implement that conceptor component
[1137] the clusters that we detect we
[1141] are put in a hierarchical network where
[1144] two clusters are hierarchically related
[1147] if
[1147] there is at least one frame in one
[1150] cluster that inherits from at least
[1152] one frame in another cluster
[1155] and these relations relationships
[1158] between fray or between clusters
[1160] are weighted based on the number of
[1163] frames that have
[1164] these uh inheritance relations
[1168] uh we assign a meaningful name to each
[1171] conceptual component
[1173] that is the most frequent frames or
[1177] these synthetic frame sources that have
[1179] the highest
[1181] frequency within all the virtual
[1182] documents of the communities of that
[1185] cluster
[1186] and uh we also add a description that is
[1189] just the concatenation of
[1190] all the terms that represent the
[1193] observed ontology design pattern of that
[1195] component
[1197] so for example here we have two uh
[1199] virtual documents that represent two
[1201] communities that is
[1202] two observed ontology design patterns
[1205] and they
[1206] end up in the same cluster that
[1209] represents the conceptor component event
[1213] because the most frequent frame is
[1216] the event frame that occurs 41 times
[1220] in the 21 communities
[1223] of the cluster that come from 13
[1226] different ontologies
[1228] and from the description here we can
[1230] already see that
[1232] we are talking about different types of
[1234] events such as
[1235] reproduction or cultural
[1241] the last step of our method is the
[1243] generation of a catalog
[1245] of conceptual components and observed
[1247] ontology design
[1248] patterns where ontologies are classified
[1252] based on the concept or components
[1254] they implement and where each conceptual
[1257] component is
[1257] linked to its ontology design patterns
[1261] within the ontologies that implement
[1263] that concept of component
[1265] we also provide an html rendering and
[1268] all credits for the catalog go to
[1270] luigiosprino
[1271] uh here for example we have again the
[1273] event concept or component with the
[1276] description
[1276] and we can access to
[1280] all the ontology design patterns that
[1283] implement the event component
[1285] you know for example here one from
[1287] acidox crm with
[1289] also the rdf our implementation of the
[1292] the pattern so the ontology fragment
[1294] and the uh the whole ontology
[1299] um so we run these methods on both
[1302] corpora and as for the intentional
[1305] graphs these are the
[1307] average number of nodes and that is um
[1310] of the intentional graphs and in the
[1313] duration
[1313] transformation from the original
[1315] ontology to the intentional
[1317] graph we keep about 90
[1321] of the original properties and
[1324] uh 50 percent of the classes so
[1327] this number may seem very very low but
[1330] actually this is because of ontologies
[1332] that
[1333] have a poor axiomatization and since
[1337] we do not consider the class hierarchy
[1339] and property hierarchy
[1340] these ontologies are mostly affected by
[1344] these rules so for example imagine an
[1346] ontology that has no domain range
[1348] restrictions
[1349] no no property restrictions on classes
[1352] so classes are not used anywhere
[1354] so they are basically taxonomies and
[1356] there are many
[1357] um they do not really uh
[1360] implement odps and in its
[1364] relational meaning so it's not a big
[1366] deal
[1368] um we've found uh more than one thousand
[1371] communities
[1372] in the cultural heritage corpus and more
[1375] than 400 in the conference one
[1377] with an average of 30 and 26
[1381] respectively community spare ontology
[1385] by a manual random inspections of these
[1388] communities we found that there are
[1390] patterns that are common to many
[1391] communities
[1392] and that um actually correlate with
[1395] modeling practices
[1397] that have been adopted for a specific
[1399] ontology
[1400] or for a specific ontology fragment so
[1403] for example we will have
[1405] some communities that are like these uh
[1408] two communities
[1409] uh they don't they are bad in the sense
[1411] that they don't have a conceptual unity
[1414] they mix
[1414] many um properties with different
[1418] hero generous meanings um and this is
[1421] again
[1421] because of a poor axiomatization for
[1424] example here we have
[1425] properties that have non-domain and
[1427] range that are
[1428] not used in the ontology or uh here
[1432] we have dominion range but again um
[1435] that's it
[1436] so in these cases the topology couldn't
[1438] support the identification of
[1440] significant communities um
[1444] actually these bad communities could um
[1447] support ontology evaluation tasks for
[1450] example by suggesting
[1451] uh in the insertion of new axioms in a
[1455] specific ontology fragment
[1458] and in other cases community detection
[1461] just splits too much
[1462] so here for example we have two inverse
[1464] properties
[1465] that are in two different communities
[1468] with the same classes
[1471] so we have duplicates that's not great
[1474] but
[1474] i want to say that when we retrieve the
[1477] the rdf our implementation
[1479] of these ontology design patterns we
[1482] include also inverse property axiom
[1484] so at least we complete these um
[1487] these patterns and also these two
[1489] communities end up
[1491] in the same class
[1494] anyway the majority of the detected
[1497] community
[1498] has a good level of semantic coherence
[1500] here for example
[1501] um three communities from sydok crm
[1505] about transfer of custody um destruction
[1508] and joining of an actor in a group and
[1511] um
[1512] what i want to highlight is that uh the
[1515] properties that
[1516] um are clearly inverse property
[1519] like joined as what was joined by or
[1522] destroyed was destroyed by
[1524] um none of them have been explicitly
[1528] asserted as
[1529] immersed in the original mythology still
[1531] we have them in the same community
[1534] um we know that arco implements many
[1537] ontology design patterns
[1539] and here are some some of the the
[1542] patterns that we were able to detect
[1544] uh these four patterns are actually
[1547] specializations
[1548] of the more general situation pattern
[1551] that we
[1552] also could uh detect in arco
[1556] uh as for clustering we use the elbow
[1560] method to determine the
[1561] uh optimal number of clusters
[1564] uh that is 100 for the cultural heritage
[1567] corpus and
[1568] 81 for the conference um
[1572] with an average of 13 and five
[1575] communities per cluster respectively
[1578] um and these communities uh come from an
[1581] average of
[1582] uh 4.5 and 2.6 ontologies
[1586] uh per cluster the overlap coefficient
[1591] tells us that our clusters have a good
[1593] quality because they are very dissimilar
[1596] and we also perform an evaluation
[1599] our results against the ontology
[1601] matching task even if
[1602] we do not produce ontology alignments
[1605] but we start from the hypothesis that
[1608] given a pair of similar entities to a
[1610] line
[1611] because there is a data set for example
[1615] of alignments or a tool
[1617] ontology matching tool they should
[1619] belong to either the same cluster or to
[1622] to related clusters and our results
[1625] uh our this experiment shows that our
[1628] clusters and their relations may be used
[1631] to improve
[1632] the performance of ontology matching
[1634] algorithms
[1637] so our clusters identify a wide range of
[1641] different conceptual components with
[1642] different levels of abstraction
[1645] there are general components that as
[1647] expected emerge from both corpora like
[1650] event or membership
[1652] but there are also components that are
[1653] specific to the domain like
[1655] performing arts and attribution for
[1657] cultural heritage
[1658] and submitting documents and respond to
[1661] proposals
[1661] for conference
[1665] here's an example from the cultural
[1666] heritage corpus
[1668] it's the categorization conceptual
[1671] component
[1672] and we can see here some general
[1675] patterns
[1676] from some ontologies like concept
[1678] classified skin
[1679] or classification it's classification of
[1682] thinking or classification in time
[1684] and then there are a different um
[1687] specialization like musical
[1689] instrument classification or
[1692] photographic
[1693] heritage classification um
[1696] acquisition uh here we have three
[1699] communities
[1700] and this is from seduck
[1703] this is from arco and um actually
[1707] this class from marco is actually
[1709] aligned to
[1710] this class from sido and
[1714] um we also have a more sim
[1718] simpler um pattern like the binary
[1720] relationship between an item and
[1722] an immediate acquisition from bib frame
[1727] for the conference we have for example
[1730] the submitting document
[1732] conceptual component again we have
[1736] the general concept of submission with
[1737] some content
[1739] an author that submits a paper and
[1743] for example deadline abstract submission
[1745] and here it is related to an abstract
[1748] here instead the submission deadline
[1750] that is actually a date time
[1752] is related to a call so many different
[1754] uh
[1755] implementations of the same general
[1757] component submitting documents
[1761] so i showed you i mean the
[1765] good conceptual components but not all
[1767] clusters are good conceptual components
[1770] so for example there are clusters that
[1772] clearly need to be split
[1774] like this one that has 111 communities
[1778] from the cultural heritage corpus
[1780] where there is no frame or synthetic
[1782] really emerges so
[1783] there is this one the synthetic agent
[1786] that
[1787] occurs only 14 times in 111 communities
[1790] on it so it's not really
[1791] representative um and also communities
[1794] that
[1795] maybe should be merged like these two uh
[1798] that have the same
[1799] uh the same name we have also some
[1803] problems with names
[1804] um mostly because of disambiguation here
[1807] for example
[1808] a community that is named being employed
[1812] but if we look at the communities so we
[1816] have
[1816] all this work um
[1819] [Music]
[1820] i mean occurrences and it's because
[1824] um frbr um
[1827] i mean for frbr work is an intellectual
[1830] or artistic creation so it's not
[1831] really uh talking about being employed
[1835] so in general we need to improve
[1837] conceptual components uh extraction
[1840] um also it is uh interesting
[1844] um to study how to identify and exploit
[1847] communities features for for example
[1850] ontology evaluation
[1851] like how to recognize bad communities
[1854] and how to suggest for example
[1856] improvements for
[1858] refactoring deontology we also need to
[1862] do a user-based evaluation of this
[1865] method
[1867] and it's not that simple because we
[1869] would need
[1871] experts in on in pattern-based ontology
[1874] engineering
[1874] so we are thinking about evaluating
[1877] these
[1878] this method uh in an indirect way
[1882] like by evaluating a pattern-based
[1884] visualization tool that
[1886] christian colonia is developing um
[1888] [Music]
[1889] using um that we'll use in this case our
[1892] method
[1893] and or for example using our method for
[1896] ontology selection or ontology reduce
[1899] tasks
[1900] uh we will also need to include class
[1903] expressions in the intentional graphs
[1905] and it's something i'm doing
[1907] right now in these days and of course
[1910] it's important to find an automatic
[1912] um an automatic way to link catalogs and
[1915] foundational
[1917] ontologies ontologies design patterns um
[1921] to our observed ontology time patterns
[1923] in order to understand
[1924] how and how much state-of-the-art
[1927] patterns are
[1928] used in practice and of course an
[1931] annotation
[1932] language of conceptual components and
[1935] ontology design patterns
[1937] uh within the ontologies so
[1940] there are probably many other things we
[1942] we can do but
[1944] i think i'm done for now so thank you so
[1947] much
[1951] okay wow perfect timing valentina
[1956] i forgot something probably yeah but
[1959] anyway so
[1960] i i hope there will be uh there will be
[1964] questions or
[1964] uh requests for clarification comments
[1968] so you will have
[1969] the the chance to to integrate
[1973] um okay so we have already one hand
[1976] raised
[1976] and by the way nice talk
[1980] missile
[1986] okay thank you very very interesting
[1989] talk
[1991] i was wondering if you have
[1994] or if you thought about evaluating
[1998] quantitatively the the
[2001] results i mean you you
[2006] might annotate manually and ontology
[2009] with the
[2011] implementation of the same patterns and
[2013] see
[2014] how many of these design pattern are
[2018] found
[2018] by your method
[2021] and also how many that you found
[2025] are not correct okay so if you have some
[2028] precision recall of
[2033] measurement of your method
[2036] also i wanted to ask you which
[2041] community detection algorithm you
[2044] you use and
[2047] if you have tried to
[2050] to use another similar
[2054] similarity measure for
[2057] for the clustering like uh
[2061] based on embedding or like bad
[2065] something like that maybe too many
[2068] questions
[2069] yeah one question at the time by the way
[2071] uh valid you do
[2073] so thanks so much for the suggestions
[2075] and uh yeah
[2076] for the first one we were just
[2080] talking about doing what you suggested
[2082] so
[2083] uh yes we need and then
[2086] i mean we did just a manual evaluation
[2089] so for example
[2090] looking at the results and i know some
[2092] patterns from arco
[2094] and i but it's just manual so yes
[2097] uh we were thinking about annotating
[2100] some ontologies starting for sure from
[2103] marco
[2104] with the implemented ontology design
[2106] patterns in order to
[2108] see what you would have said so
[2111] precision and recall so yes totally
[2114] and for the second one yes also with
[2117] um so the community detection we use the
[2120] closet newman more algorithm i
[2123] can there was the reference in the slide
[2126] but
[2127] i i can also point you to the algorithm
[2130] it's actually very
[2132] kind of old and uh state-of-the-art um
[2136] okay with in the it is implementing the
[2139] net network's
[2141] python library and i also tried
[2144] um the another the label propagation
[2148] algorithm but i mean didn't seem to
[2151] produce
[2152] better results and for the clustering
[2155] um yes we thought about try to use also
[2159] embeddings like
[2160] bert or something but we didn't
[2163] do that um but yes it's something that
[2167] we should consider because um
[2170] maybe it produces uh better results so
[2174] okay thank you okay yeah we were talking
[2178] miser about
[2180] thinking on how we can exploit these
[2182] language models so to improve
[2183] for example the explanation of the
[2186] cluster
[2187] but but it's uh still we thought about
[2190] it today so it's a good suggestion
[2192] but yeah it's something that definitely
[2194] will be considered
[2195] thanks yeah yeah the language model uh
[2198] works very very well compared with
[2202] previous techniques
[2205] so certainly
[2208] it's what to try yeah
[2212] um aldo
[2216] [Music]
[2227] okay that's it uh so thanks valentina
[2230] very clear nice work uh actually you're
[2233] on the
[2235] uh you're going to to solve the
[2237] modularization automatic modularization
[2239] problem in ontologies
[2241] in the next fusion um okay so the
[2245] my observation is about the role of data
[2248] about that
[2249] um i guess you have not yet introduced
[2251] it within the
[2253] method but for example if you go to
[2256] slide
[2256] 34
[2260] i like actually
[2265] yeah i did it but i can't hear a moment
[2270] [Music]
[2283] i can hear you yeah um
[2286] so you see that should be that one
[2290] yeah but you say that to actually verify
[2293] that no probably is the next one 35
[2296] sorry i missed nope
[2299] nope definitely i was okay forget about
[2301] it so
[2303] you notice that ontology is that okay
[2305] this one 34.
[2307] it is i didn't realize it was there okay
[2309] so the poor externalization
[2311] is something that would preclude the
[2313] possibility
[2314] to link to them to
[2319] extract a design pattern from an
[2321] anthology
[2322] however now imagine this situation you
[2325] don't have a pure taxonomy
[2327] because this could be ontology that's
[2329] just classes and properties
[2331] and you don't have any action that links
[2334] classes and properties okay
[2336] yet you might have a lot of data that
[2339] use these ontologies and actually
[2341] assert property
[2344] declarations now so in that way you can
[2347] factor in the ability to infer
[2350] axioms based on the usage that you've
[2353] made of this authority this actually
[2354] is a pretty known work we made something
[2357] uh
[2357] many years ago about extracting
[2359] ontologies from data
[2361] based on these loose vocabularies um
[2364] still you can not discover patterns
[2366] there and uh
[2367] and this is the case of quite a few
[2370] ontologies actually that are used
[2372] especially
[2373] in linked data and knowledge graphs that
[2375] don't actually
[2376] match um this would be interesting to
[2379] uh to to add in your media as well no
[2382] of course considering the fact that by
[2384] using these
[2386] data-driven approaches not necessarily
[2388] you are
[2389] you are catching the real intended
[2391] semantics
[2392] intended conceptualization but
[2395] on the other hand is even more precise
[2397] because sometimes you have authorities
[2398] that are accidentized
[2400] but they are used only partly
[2403] or with this special way in a special
[2407] way in the data
[2409] so considering these aspects might be
[2410] very interesting to
[2412] to reinforce your uh to improve your
[2414] your meat or not that
[2416] becomes even broader you can discover
[2418] patterns even when
[2419] people do not know anything about uh
[2421] relating decently uh
[2424] index traumatizing vocabulary okay
[2429] yeah yeah thanks so much we uh also
[2432] talked about
[2433] um i mean including in the approach
[2436] about the topology the vocabulary and
[2439] the data
[2441] so yes this was something we wanted to
[2443] do but um
[2445] i didn't think about the fact that it
[2447] would improve
[2449] i mean it would um yeah improve the
[2452] results
[2452] um mostly in these cases so
[2455] there is a proximitization so i think
[2457] that this is
[2459] something that uh it's very interesting
[2461] that yeah
[2462] we will do it thank you
[2468] okay thanks
[2472] um yeah in fact we we actually
[2474] considered at the very beginning that we
[2476] wanted to go
[2477] you know to analyze these three
[2479] dimensions and then
[2481] so far we valentina didn't yet
[2486] worked on the data because also besides
[2489] discovering
[2490] other patterns that maybe come from the
[2493] data unless from the
[2495] even if they are not expressed in the
[2497] scheme and the ontologies
[2498] you can also reinforce the result uh
[2502] the patterns to discover from the schema
[2504] so if the data actually
[2505] show that also for um we also thought
[2508] that
[2509] data can tell us better how to uh draw
[2512] the boundaries you know
[2513] uh for uh for extractive for uh
[2517] um yeah for extracting the
[2519] implementations the the actual uh
[2522] implementations in the ontology it's
[2524] just that she's not yet
[2526] there but um but it's something that
[2529] definitely
[2530] must be considered um there is a
[2533] and hand raised by andrea of course
[2536] invite all the others to raise their end
[2537] and
[2539] if they have questions or comments
[2540] andrea please go ahead yeah my
[2543] my question is somehow very related to
[2546] what you're saying
[2548] so what is here the notion of context or
[2553] boundaries so how we can detect the
[2555] clear boundaries in order to
[2557] uh identify precisely what what the
[2560] pattern is
[2561] so typically so just also to rehearse
[2564] what you mentioned about
[2565] the knowledge soup another key point or
[2568] for
[2568] for a pattern is the
[2571] you know the relevance with respect to
[2573] specific context and also it's available
[2575] it's
[2577] capability to uh you know to
[2580] identify clear boundaries either around
[2583] data or
[2584] in a specific domain uh so this is uh
[2588] somehow the first question then i don't
[2591] know if it is just for
[2592] for you know for the example or for sake
[2595] of
[2595] uh you know shortness uh in the examples
[2599] you provided
[2600] uh for the results and and experiments i
[2603] see only
[2604] uh you know two uh tired structures
[2608] in in terms of buttons so you you have
[2610] only two layers for your patterns
[2613] uh it is always the the the case or
[2617] uh it is also it is only by by chance
[2620] that you have this kind of structure for
[2622] your patents
[2625] guys for the boundary yeah
[2628] i mean that's a problem by now as i said
[2631] we used
[2631] just some basic heuristics or the
[2635] domain range for properties and for
[2638] example for the
[2640] property restrictions on on classes we
[2643] decided to include only those property
[2645] restrictions where
[2646] there were properties in the community
[2648] not other
[2649] not any of course property restrictions
[2651] on on one class
[2654] but yes um we we can improve i mean the
[2657] boundary for example by using data
[2659] and we of course didn't still uh
[2662] solve this uh this problem um
[2666] there's a second question i didn't
[2667] really understand you mean you know
[2669] yeah the the second question is is about
[2672] the structure i see in your examples uh
[2676] if you open the last slides there are a
[2679] couple of results and in those results
[2681] you i think you are presenting uh
[2684] example
[2685] uh of patterns you
[2689] you were able to gather from your
[2691] analysis and
[2693] this pattern seems to be uh
[2697] structured they say you know
[2700] you mean these slides no the previous
[2703] one of yeah
[2704] the the previous one yeah okay
[2711] and okay
[2716] yeah there are more structure yes now i
[2718] i
[2719] thought that the structure was based
[2721] only or
[2722] on you know two uh layer uh connected
[2725] each other but this is not the case you
[2727] have also more complex uh
[2729] structures then uh yeah if i can
[2733] um i have a different kind of questions
[2736] which
[2737] uh is more about the method
[2741] you said that
[2745] you generate a sort of
[2748] textual document from the uh
[2752] the ontology basically or representation
[2754] of the
[2755] uh structure of the ontology
[2758] uh that that is used for
[2762] uh linking your terminology to
[2765] uh dwarnet framesters or to lexical
[2769] resources uh so you have scene sets
[2772] instead of
[2774] upwards yes but
[2777] then you lose the the structure
[2780] so you have a document without any
[2782] structure or any relation or any
[2784] topology or
[2785] any logical representation of
[2788] the document so is there any solution
[2792] you are thinking about of it first this
[2794] is relevant what
[2795] i'm saying or i'm focusing on the wrong
[2798] problem
[2799] uh and the second point is then okay how
[2802] to
[2803] to cope with this uh problem
[2807] yeah actually we lose this structure
[2809] since the beginning because
[2811] even here uh we just concatenate
[2814] words and regardless if they are
[2818] from a property or a class and we also
[2821] remove repetitions for example and so
[2824] yeah we lose the structure and
[2826] we we don't know if reduction agent is
[2829] together or not
[2830] and this is something actually we
[2833] thought about
[2834] so how to preserve the fact that
[2837] they are like that i don't know the
[2840] identities
[2841] together and it's not separated and
[2844] um i mean i keep track of the provenance
[2848] of the parts of the virtual documents
[2851] but then
[2852] the clustering and the disambiguation
[2856] i don't um so i think
[2859] it may be irrelevant because uh actually
[2863] uh if i understood well yes if here
[2866] we have an event narration and not
[2868] narration
[2870] separated for example i don't know so
[2874] uh no i i don't have any idea on how to
[2878] to consider the structure you know here
[2880] for for
[2881] clustering or for using the terminology
[2885] um i would like to comment
[2887] uh if i may uh on both of the the
[2890] comments from andrea so one is about the
[2892] boundary
[2893] uh the first one so the boundary uh so
[2896] you asked
[2896] how do you know what the pattern is when
[2898] it's relevant well
[2900] as valentina said and also
[2903] explained in this in the presentation we
[2905] have some heuristics
[2906] to retrieve the the actual
[2909] implementation in the
[2911] um in the ontology for this conceptual
[2914] component
[2915] and these uh these heuristics basically
[2918] are
[2919] designed so that uh so we we of course
[2922] risk to
[2923] to miss some pieces but we are sure that
[2926] we don't go too broad
[2928] so that we actually draw a boundary
[2930] which may be too constraining but
[2932] we prefer this then um also because
[2936] at the in this work we are not
[2937] interested in defining
[2940] precisely what what the pattern is or
[2943] or having a definition on how to design
[2945] the boundary but we want
[2947] to make sure that we can retrieve
[2951] an approx a good approximation of the
[2953] implementation of the pattern
[2956] so the idea is that if you if you look
[2958] at the implementation of a certain
[2959] component
[2960] we point you to um a block
[2964] let's say an implementation and then
[2967] you as an ontology engineer can
[2970] recognize whether
[2971] for example you want to add another
[2973] property or another class
[2975] so we are not aiming at identifying
[2979] you know automatically a definite a
[2981] formal definition or
[2982] complete precise definition of what a
[2984] pattern is even because i think that
[2986] even a human cannot do this
[2988] so we are interested in uh in
[2992] having a good modularization of the
[2994] ontology
[2995] which of course it's approximate as it's
[2997] an empirical
[2999] approach um and as for the structure in
[3003] the text
[3003] so i wanted to remark that on one end as
[3007] valentina said because i didn't think
[3009] about it but
[3010] actually we so we don't need the
[3012] structure in the text
[3014] because we need we use the text so we
[3015] extracted it so we built the virtual
[3017] documents because we want to use them as
[3019] a basis for clustering
[3021] so we we don't care about the structure
[3024] while we do the clustering
[3026] however we may experiment on
[3030] using some knowledge about the relations
[3032] between these terms
[3033] um to improve the clustering so this can
[3037] be a way
[3038] to use them yeah now just to try
[3041] something
[3042] about my questions but the the structure
[3044] is that
[3045] uh i don't know if it is relevant the
[3047] structure of the original ontology
[3049] uh per person but uh as you are able to
[3053] together or to retrieve possible scene
[3056] sets or
[3057] you know frames from frame net and then
[3060] you have the relations among frames and
[3062] among other
[3063] uh you know rows and whatever
[3066] and frames are patterned somehow okay
[3070] our patterns uh so my intuition my
[3074] my suggestion is there is is there any
[3076] any way
[3077] uh to combine
[3081] somehow the knowledge you have from a
[3083] lexical knowledge basis
[3086] that contains frames and other kind of
[3088] patterns in order to gather
[3090] patterns from anthologies so
[3093] i don't know i mean it is just a comment
[3096] um
[3097] we thought so initially when we looked
[3098] at the the data determine a lot
[3101] the terminology we thought okay how do
[3103] we
[3105] identify the frame the you know the most
[3108] representative frame so i don't know if
[3110] valentina you want to answer this or you
[3112] you want me to continue but but if you
[3114] have something to add i will go
[3116] after you now you can
[3119] okay sorry no no really i mean
[3122] of course but so we we thought uh so we
[3125] had this um
[3127] basically bag of words and initially we
[3129] didn't even
[3130] remove the repetitions so we removed the
[3132] repetitions later because we noticed
[3134] that
[3135] the results were noisy and we tried and
[3138] actually they improved
[3140] um and so we had these big awards and we
[3144] thought okay now that we have this
[3146] so i had so we had actually initially
[3149] this uh the same intuition that you have
[3152] can we
[3153] like match uh frames and their roles so
[3156] can we
[3156] identify that here there is a frame so
[3160] so can we match what is here with the
[3162] possible
[3164] like if if we are recognizing frame
[3166] occurrences basically
[3168] and uh and so
[3172] and this is uh certainly any
[3175] you know a post you know an hypothesis
[3178] that
[3178] you you may be able to do it at least
[3181] manually like you look at it
[3183] and you can try um but
[3186] um so we but then we said okay
[3189] no i mean how can you do this because
[3191] it's not a text
[3193] with the sense now that you can try and
[3195] do frame recognition
[3196] uh and um frame detection and
[3200] uh and at least to to our
[3203] uh knowledge i didn't i i so we didn't
[3207] identify any way to do this easily or
[3211] or without you know focusing on that
[3213] specific problem instead of what we had
[3215] to achieve and so clustering actually
[3218] was
[3218] clearly a good way to go at least to
[3222] put these things together and then we
[3224] the disambiguation
[3226] and the the frame the
[3229] you know the relation between the scene
[3232] certain frames that framester
[3234] gives us where at least so far enough
[3237] to have a good um a good result in terms
[3241] of approximating again
[3243] what's the most representative frame so
[3245] we use basically
[3246] mainly frequency and
[3249] by removing it by removing the
[3251] duplicates this was even more
[3252] representative
[3253] of course this can be improved but more
[3255] than trying to recognize the frames
[3258] because the frames are very generally
[3260] defined so it's really
[3261] so how can you detect these are anyway
[3265] there's not a sentence where you can run
[3268] i don't know thread or
[3269] or reframe the frame detection
[3272] uh tool so i think that instead
[3275] of trying with the with the language
[3277] model to see if we can improve
[3279] the way to summarize or um you know
[3282] adding a meaning to describe the cluster
[3285] is probably
[3286] a better way to go but uh yeah
[3289] so this is okay
[3292] yeah i don't know if there is also uh
[3296] um a future work that same sex including
[3299] also
[3300] uh ontology design patterns as a
[3303] you know a repository of patterns for
[3305] aligning for
[3306] for alignment or you know
[3309] as a background knowledge for the
[3313] recognition of existing or
[3314] you know off of patterns
[3318] because it could be also another
[3321] strategy
[3322] or a possible direction that can be uh
[3326] you know follow it
[3330] yeah we thought about including in
[3333] our corpus in our corpora
[3337] for example foundational ontologies such
[3339] as dolce
[3340] and in order to see where the the
[3344] how dolce is split by community
[3346] detection and where
[3348] dolce patterns end up in which clusters
[3352] uh in order to see what we can
[3355] kind of align uh so yes uh also this is
[3359] something i will do probably
[3360] tomorrow so um
[3362] [Music]
[3363] something interesting i think
[3367] actually this thing is i think it's a
[3369] really
[3371] you know i don't know what valentina
[3373] would be able to get from this but
[3376] putting the dolce other one from no we
[3379] we want to put torture because we know
[3380] that there are
[3381] many of the general patterns that are
[3384] used or
[3386] um so if we if we end up actually having
[3389] the deutsche battens distributed
[3392] coherently with
[3393] their you know with their
[3395] specializations i think this would be
[3398] a powerful result because
[3402] i think many of us know that uh
[3406] understanding what's the general pattern
[3408] that you can reuse
[3409] when you have a local or a specif you
[3412] know a domain specific vocabulary
[3415] um automatically of course i mean this
[3418] is the problem of matching
[3420] your competency questions your
[3422] vocabulary with the general pattern that
[3424] you
[3424] that you can specialize so if
[3428] this valentina's method with probably
[3431] some
[3431] adjustment and improvement uh is able to
[3435] to do this at least at a certain extent
[3438] uh with it with good results then i
[3441] think this would be a very powerful
[3443] result also for uh you know reusing
[3447] the method in another context such as
[3450] um you know identifying you know having
[3454] the competency questions and
[3455] now tell me what's the pattern i need to
[3459] reuse
[3463] there's no question i have another
[3465] comment which
[3467] is which is nice to to discuss
[3470] here i don't i don't think it is very
[3473] related to what valentina
[3475] did so far but i think it closes somehow
[3478] the loop
[3479] uh once we have the patterns and the
[3481] models and we want to
[3483] create a new ontology by relying by
[3486] using pattern and using patterns
[3488] a common issue i have is that when i
[3492] import
[3493] an ontology with protege for instance or
[3495] a single pattern
[3498] i am provided with the whole pattern or
[3501] ontology
[3503] and this is a bit annoying because
[3506] in many cases i am really interested in
[3508] few concepts or
[3510] in a small part which is really that the
[3513] real pattern i want to use but
[3516] there is no working to the best of my
[3519] knowledge there is no working
[3520] extension of owl or uh protege
[3525] that allows us to use a
[3528] pattern or any possible
[3533] solution like opla that allows to
[3538] annotate ontology modules
[3541] and i just did a work uh
[3546] oven on patterns and i had to reuse
[3549] parts of uh ontology networks in another
[3554] you know view of the same ontology
[3557] network
[3558] and uh i was forced to redefine
[3562] uh you know concepts and and and
[3565] relations uh instead of importing the
[3569] uh whole ontology or uh whole modules
[3572] and this is you know something that goes
[3575] in the direction of identifying patterns
[3577] reusing patterns and reusing pattern in
[3580] a feasible way
[3581] that means i want to use patterns not
[3584] whole ontologies or whole modules
[3591] and sorry for the big uh to redefine
[3595] uh outlet uh at first and then uh
[3598] because uh the the semantics of the
[3600] import is to
[3602] uh import all the uh axioms from the
[3606] the imported ontology so you first you
[3608] first need to
[3609] redefine the semantics of a new
[3612] import and then uh also you need um
[3617] a vocabulary for uh it's fine
[3621] i i understand that the semantics of
[3623] import is to
[3625] import the id the whole ontology or the
[3628] whole artifact you are pointed out
[3630] you are pointing out the problem is
[3632] probably about how
[3634] visualized
[3637] so if i import your ontology this is
[3640] a logic a logical fact
[3644] but as a designer or user i want to
[3648] be displayed only with the part i am
[3650] interested in
[3652] and i think that you the two
[3655] things should be taken
[3659] uh in two different
[3662] ways the naturalization part and the
[3665] design
[3665] part of the ontology from the logical
[3668] meaning
[3669] of the axioms of the imports
[3673] that's true just for reasoning
[3676] the input then you actually
[3679] you are right if you want to do
[3681] something that allows to import
[3683] only logically the part you want to use
[3686] then we have to redefine our or to
[3689] define a new axiom
[3691] but i think that the problem can be
[3693] taken from different perspective
[3695] but i i don't want to spend
[3699] other words on this topic because i
[3701] think that we are going out from
[3703] the original scope valentina wanted to
[3707] comment
[3708] vale you wanted to comment uh no i just
[3711] wanted to say
[3712] so that would be uh
[3715] i mean the import of a of a module so
[3718] uh of a specific pattern you want to
[3721] reuse
[3721] um so so yes i mean i think it
[3725] would be very useful and so maybe a a
[3728] tool that is
[3729] specific for this use i don't know so
[3732] that splits an ontology
[3734] and then you can but yes i don't know
[3738] if you need some specific
[3742] i mean not not owl not power imports
[3745] of course i don't think it's a problem
[3747] of the language well of course you can
[3749] have
[3750] a primitive in the language that allows
[3754] you to do but i think this is more a
[3755] problem of implementing
[3756] a way to do this so this is a problem we
[3761] it's not a new problem clearly because
[3764] when you
[3765] when you study modularization or
[3769] ontology is important
[3771] so this is the first thing you you end
[3773] up having as an issue
[3775] so when we we developed the the catalog
[3778] of patterns in neon
[3780] so it that was the first um
[3783] the you know when we started working on
[3786] on the concrete implementations of
[3788] patents
[3790] and so we're talking about 2006 maybe it
[3794] was
[3795] like something like that um anyway
[3798] so in that project especially there was
[3802] also a lot of work about modularization
[3804] taken mainly from a logical perspective
[3807] you know like
[3808] andrea was saying um and in fact
[3811] valentina's work i think that what you
[3812] andre are saying
[3814] indeed it's related to valentina's work
[3816] it's not out of scope
[3818] so what valentina's method they said
[3821] it takes a designer perspective so we
[3823] want to know
[3824] what the ontology talks about and we
[3826] want to identify those parts of the
[3828] ontologies where
[3829] this is a assertive so we are not caring
[3831] about
[3832] if i use that part what happens
[3836] in terms of consistency if i take it out
[3839] from the whole ontology because usually
[3842] this was the perspective
[3845] applied to ontology modularization like
[3848] making sure that you can control
[3851] consistency the whole consistency while
[3854] you were
[3855] modularizing or extracting a module
[3859] we i remember that we also did
[3862] some work actually we did an
[3864] implementation that now it's not
[3866] available so there was a tool
[3868] but it was developed for the neon
[3869] toolkit so it's it's now
[3872] like other things uh so we actually did
[3875] develop some of these
[3876] supporting tools that then went into
[3880] you know we couldn't we didn't have the
[3883] the resources to implement the same
[3886] tools for protege for example
[3888] so we did them as a west plugins for
[3890] this
[3891] this toolkit that then was dismissed
[3895] and and so they got lost but there was a
[3897] tool
[3898] that we did which was actually an xd
[3900] plan xd plugin
[3902] for uh for uh the neon toolkit where you
[3905] could
[3906] um copy basically a pattern
[3909] from the ontology uh and uh and reuse it
[3913] you know use only the part that that you
[3916] wanted to reuse
[3916] so you would clone it so we i remember
[3919] that we defined
[3920] two operations so one was cloning which
[3923] would mean
[3924] i copy so i use this pattern from this
[3927] ontology as a template and they create a
[3929] new one so
[3929] we had this supporting tool that would
[3932] basically copy
[3933] the the the structure and the other one
[3937] was
[3937] um there was another one like the
[3940] extraction i think
[3942] uh that i don't remember anyway because
[3944] now it's
[3946] it's it's long ago but but we had this
[3949] uh
[3950] this idea that you could you would want
[3953] to use only part of the ontology
[3955] uh and you wanted to have some tool that
[3958] would implement
[3958] this like while you are editing your
[3961] ontology instead of importing they all
[3963] think you just
[3963] copy the parts that you want so in
[3966] principle
[3967] you could have also a a primitive in
[3970] in all a new let's imagine an extension
[3973] with the like partial input
[3975] the problem is that that is that if you
[3977] do this then you have to face
[3979] all the logical consequences and
[3981] properties
[3982] so i think this is more um adequate for
[3986] a pragmatic approach
[3988] and um and i think that so one of the uh
[3991] the the possible
[3994] um evolutions of that that valentina is
[3997] thinking for her work is also to
[4000] um to annotate automatically the
[4002] patterns that she discovers
[4004] because we we can go always from the
[4006] conceptor components to the actual
[4009] uh classes and properties and actions
[4011] that are involved
[4012] so that you can basically for example if
[4014] you have a tool that understands these
[4016] annotations
[4017] you can say okay let's copy or clone
[4020] this
[4022] this pattern and in my ontology so i
[4024] think
[4025] that actually the valentina's work can
[4027] can also have
[4030] an application in this kind of of
[4033] very pragmatic ontology engineering task
[4040] and okay so is there any other
[4043] comment or questions or curiosity
[4046] or even other suggestions so we had very
[4049] nice suggestions
[4050] some of them we already thought about
[4052] them but it's very good
[4053] to hear that you know uh
[4056] it it means it makes sense if also
[4058] others have the same ideas
[4061] is there any other question or comment
[4064] okay so i think we can uh thank valentin
[4068] again
[4068] for the very nice talk um
[4072] good luck to all of us for the
[4073] notifications but anyway this is a cool
[4075] work so we will publish it anyway
[4078] regardless iswc and i'm saying this in
[4082] the recording
[4083] so after the notification they can hear
[4086] that we don't really care
[4088] because we know it's it's really good i
[4090] i i honestly think it's
[4092] it's really okay i'm i'm biased but
[4096] um but this is something it's it's there
[4099] since very long and this is the first
[4101] time i see
[4102] a result that can have an impact on a
[4106] pragmatic modularization of anthologies
[4110] so thank you very much everyone martina
[4114] will
[4116] circulate the details of the next
[4119] seminar
[4120] who will talk next week martina
[4123] margarita margarita okay so margherita
[4126] will be the next so i hope to see you
[4129] all there
[4131] i expect to see you all there and
[4135] have a good day thank you very much
