---
schema_version: 1
id: yt-joC4NZgLtqA
type: youtube
title: Building Ontologies with Basic Formal Ontology
url: https://www.youtube.com/watch?v=joC4NZgLtqA
authors:
- Barry Smith
ingested_at: '2026-06-17T19:27:50Z'
content_hash: sha256:13819ba49a9b4794ddd722fbdcf103520b2fbbb9e0d0d12bd49eb9a072714c96
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Barry Smith
  channel_url: https://www.youtube.com/@BarrySmithOntology
  duration_seconds: 4678
  caption_track: fetched
  snippet_count: 1571
filter:
  score: 0.7
---
[0] what we're going to be talking about
[1] today is basic formal ontology I'm
[3] assuming that not everyone in the room
[6] is an expert on basic formal ontology so
[9] I will start more or less from the
[10] beginning there is a book which is a
[15] guidebook to basic formal ontology which
[18] I will send around along with some and
[24] that the book is designed as a guidebook
[27] so it tells you why you need an ontology
[30] and it tells you how to build an
[31] ontology and it explains how to build an
[34] ontology specifically using BFO as your
[37] starting point and then it gives some
[39] examples of ontology which have used BFO
[42] as their starting point and it's going
[44] to appear in Chinese it's it started in
[50] the wake of the gene ontology
[52] so the Balaji was created in 1998 and
[58] originally the gene ontology was created
[64] as a collection of terms organized in a
[68] hierarchy and each of those terms had a
[70] definition but the definitions were not
[73] always very good and I became involved
[76] with the gene ontology community trying
[79] to help them to formulate better
[81] definitions and what the gene ontology
[86] is is a collection of terms which you
[90] would use to tag or annotate gene
[94] sequence data or protein sequence data
[97] so if you find a gene you want to know
[100] for instance what biological processes
[102] that gene is involved in and so you need
[105] a term for biological processes such as
[108] cell division or perception or walking
[113] was completed many other genome projects
[117] were completed and it was very quickly
[121] realized that if the gene ontology was
[123] to be a success then it has to be
[125] species neutral that is to say it should
[129] not be an ontology of human biological
[132] processes
[134] of mouse biological processes but it
[137] should be an ontology of biological
[139] processes of any organism now this idea
[145] that you need to build your ontology in
[150] such a way that it will be workable it
[153] will be useful even when new organisms
[156] on you biological processes or new cell
[161] part entities are discovered this idea
[166] is quite generalizable that is to say
[169] you will build a better ontology if you
[172] try and to tag the data that you have
[175] from your specific project at this
[177] specific time your ontology will very
[180] quickly not work the way to ensure that
[183] your ontology works over a long period
[186] and the gene ontology has been
[187] remarkably successful over now almost
[191] twenty years
[192] you move to a higher level of generality
[194] you anticipate what data you might
[197] discover by building your ontology at a
[201] higher level of generality than the data
[203] that you have when you start but then
[206] there is a problem what happens when you
[210] reach the top what happens when you
[213] can't go to any further level of
[216] generality and this question was
[220] addressed already by philosophers so
[223] Aristotle put forward a theory of what
[226] the most general terms are that you
[228] might use to describe for instance
[230] biological reality and at the very best
[233] already by philosophers so Aristotle put
[236] forward a theory of what the most
[239] general terms are that you might use to
[241] describe for instance biological reality
[244] and at the very top you have what
[246] Aristotle called substance by which he
[248] means something like an object or a
[250] thing and some substances are material
[252] and they are called bodies and some
[255] bodies are animate and they are called
[259] living bodies and some living bodies are
[261] sensitive and they're called animals and
[263] some animals
[265] rationale and they are called humans now
[270] BFO is a the maximally general ontology
[274] it's a top-level ontology you can't get
[277] more general so it's working at the same
[279] level as substance material immaterial
[282] in Aristotle's terms now the top level
[287] of the gene ontology consists of three
[289] terms cellular component malaria logical
[293] process so all the terms in the gene
[296] ontology fall under one of these three
[299] headings and then we have subtype
[302] relations so by binding is a kind of
[306] molecular function binding is a subtype
[308] of molecular function and metabolic
[315] process is a kind of biological process
[318] so metabolic metabolic process is a
[320] subtype of biological process and what
[323] we're interested now is what is cellular
[326] component a subtype of or what is
[330] molecular function a subtype of and it
[333] was in answering those questions that
[335] BFO was born so BF o is the gene
[338] ontology taken to the maximal level of
[341] generality there are the three top level
[344] terms of BFO correspond to the three top
[347] level terms of BFO namely independents
[352] are things like things objects tables
[355] billiard balls people dependent
[360] continuance are attributes qualities
[362] height weight color and so on also
[366] functions such as binding which is a
[370] molecular function according to the gene
[372] ontology and then occurrence are just
[374] processes and beginnings and endings of
[377] processes things that occur continuance
[380] continue occurrence occur and everything
[383] in the universe according to BFO is
[386] either one or the other
[389] and we can think about that claim later
[393] on befo however does not claim to be
[396] complete befo is offered as a an assay
[401] of what exists but if we discover other
[404] things which exist and BFO will have to
[406] be changed in order to cope with those
[409] other things this is so examples of
[413] mature independent continued include
[415] material entities examples of dependent
[418] continuing includes qualities and roles
[421] and we've already seen an example of a
[423] current which is processed and this is
[426] how BFO works so we've already seen that
[429] the gene ontology extends BFO and this
[433] is the mental functioning otology
[435] similarly the mental functioning
[437] ontology extends BFO so anatomical
[441] structures are independent continuance
[443] according to BFO thinking is a cognitive
[446] process which is a process according to
[448] BFO and so whatever ontology you have
[452] you you are challenged to create it as
[458] an extension of BFO and if you can't do
[460] that then that's a problem for BFO it's
[462] not a problem for you all right now BFO
[467] is very small and you will see that most
[470] of the there we have various temple
[472] regions and the basic structure of BFO
[476] is not much more than this and it
[481] evolves very slowly so we've been
[483] through three versions in 16 years we're
[486] just about to release a fourth version
[488] which I will be announcing publicly for
[491] the first time in about an hour its
[496] domain neutral so being absolutely
[498] general means that you can apply to
[500] absolutely everything so you can apply
[502] it to cosmology and falafels at early
[505] and informed consent and yoghurt
[509] manufacturing it and government and
[512] military and administration and it's
[515] being applied to all of those things it
[518] has a very active user forum which keeps
[521] me awake at night
[523] it has a large user base and it has a
[526] lot of people who know how to use it so
[529] you'll find that that link its domain
[533] neutral so being absolutely general
[536] means that you can apply to absolutely
[538] everything so you can apply it to
[540] cosmology and filler
[541] philately and informed consent and
[545] yogurt manufacturing it and government
[549] and military and administration and it's
[552] being applied to all of those things it
[556] has a very active user forum which keeps
[558] me awake at night it has a large user
[562] base and it has a lot of people who know
[564] how to use it so you'll find that that
[567] link a list of the 300 or so ontology
[570] groups who are using BFO and the this is
[575] a positive feature of BFO if a lot of
[578] people use it then a lot more people
[580] will be finding it beneficial to use it
[584] because there are Tala G's will then be
[586] associate ball with the ontology is
[588] already created by other people using
[590] BFO so this is a network effect and so
[597] the I want to argue that there are four
[600] keys to ontology success the gene
[602] ontology is clearly a successful
[604] ontology BFO seems to be a successful on
[606] solji the first key to success is that
[609] you distinguish two kinds of ontology x'
[611] on the one hand you have what are called
[614] reference ontology x' which are designed
[617] to be reused over and over again and
[620] this is true both of BFO and of the gene
[624] ontology and of the other ontology is in
[626] the elbow foundry and then you have
[628] application ontology x' which descends
[630] from the reference ontology but which
[633] are built for a specific local purpose
[636] for some project or for some group and
[638] [Music]
[639] they're tied to local data the second
[643] key is MoDOT modularity that is to say
[648] you should build your ontology
[650] oh that that division of labor if you
[653] build a protein ontology you're going to
[656] act people interested in proteins both
[658] as users and as builders of the ontology
[661] if you call it the protein ontology
[664] people will know that that's a good
[666] place to look to find ontology terms for
[670] annotating data about proteins so this
[673] means that you have discoverability you
[675] have motivation also modularity means
[680] that you can you don't have to build
[681] everything at once you can start with
[684] just part of the domain of your ontology
[685] and then try and build out the details
[688] to that part and then go back to other
[691] parts later but in all of this you
[694] should remember that you want a future
[696] proof your ontology so that you should
[698] make sure that you leave room for the
[699] other parts all right and you should not
[704] believe in mappings mappings never work
[707] you should try and get the ontology
[709] right hope that you'll be able to map
[711] your terms to other ontology x' as time
[714] goes by and the way that you organize
[719] all of this is in terms of hub and
[722] spokes so you have a hub which is a very
[726] general ontology like BFO and then you
[729] generalize by building outwards by
[733] defining more general reference ontology
[736] x' and then more specific reference
[738] ontology x' until at the very end you
[740] get to your local application ontology
[742] so that you might need for your specific
[744] project the reference ontology x' will
[746] contain terms like Mouse and the
[749] application ontology will contain terms
[751] like subject in Mouse experiment number
[754] 467 and then the fourth key is choose
[760] the right hub and of course you should
[763] choose BFO but i have to prove that by
[765] showing you why BFO is better than the
[768] alternatives which is choose the right
[770] hub and of course you should choose BFO
[773] but i have to prove that by showing you
[776] why BFO is better than the alternatives
[779] which have been put forward all right
[781] now there are some examples of hub and
[784] spokes sweets which have been advanced
[787] in which are being built these are three
[790] which are not part of biology while it's
[792] called the common core ontology which
[794] was built as part of a natural language
[797] processing experiment and which has now
[799] been used in many ontology projects
[802] primarily in military domains another is
[806] the industrial ontology foundry which is
[808] being built under the direction of the
[812] National Institute of Standards and
[814] Technology by people in different areas
[816] of Industry and then there is something
[818] called the model-based systems
[819] engineering ontology which is a very
[822] large ontology suite which we're just
[823] starting at the moment and the common
[827] core ontology
[828] currency unit information entity agent
[831] quality event artifact ontology and then
[834] a series of extension ontology is
[836] covering various domains and this these
[838] extension ontology zuv being built over
[841] and over by different for different
[843] projects which want to use this common
[845] core framework but they need to extend
[847] to a new area and as I say the common
[852] core ontology ZAR freely available and
[854] you can find them very easily just by
[856] well that the link is actually down
[858] there in the bottom I will put these
[859] slides on my website almost immediately
[863] after the talk but these are the biology
[868] ones or the biology related ones and the
[871] oboe foundry ontologies are at the top
[873] then we have the infectious disease
[875] ontology suite at the bottom planty Oman
[877] Tala geez and some of these have hubs so
[880] top-level ontology hub these are the
[883] ones with hubs and in each case the hub
[886] is BFO so there are no seat was
[890] successful in its day but it didn't have
[893] a hub and the so the the performance
[899] simulation initiative ontology suite
[901] died a long time ago it had a different
[904] hub but it died so it's not successful
[907] the oboe foundry was a an idea for
[913] developing a suite of ontology is on the
[915] basis of a set of common principles
[918] and modularity which we called
[920] orthogonality is one example of a common
[923] principle and it was sketched here in
[928] 2007 but we'd already started working on
[931] the Ober foundry and basic formal
[935] ontology as the ontology underlying as
[939] it were the gene ontology is the hub and
[941] then we have various domain level
[944] ontology such as the protein ontology
[946] that the bio little level ontology is
[949] between them and the organization of the
[952] gene ontology is along two dimensions
[955] along the top on the horizontal axis we
[960] have BFO basically independent
[962] continuous dependent continuous and
[964] occurrence and then on the vertical axis
[967] we have granularity which means very
[969] small things bigger things even bigger
[972] things and we added then population
[976] ontology x' up here we added an
[980] environment ontology which covers all
[982] levels of granularity we added OB which
[986] is the ontology for biomedical
[988] investigations which covers experiments
[991] so the OB the domain of OB is
[994] experimental processes and everything
[996] which belongs to experimental processes
[998] including things like publications
[1001] funding agencies equipment and so forth
[1005] samples samples and then we added the
[1012] information artifact ontology because we
[1014] realized we didn't have a place for
[1015] publications or for data or for
[1018] footnotes or for ontology and so the
[1021] information artifact ontology includes
[1023] all of those things things like images
[1025] and so forth and that's an extra
[1028] ontology within this framework so this
[1034] is the framework again this is BFO the
[1037] basic structure and this is the color
[1041] scheme so green is process orange is
[1045] attributes and then yellow it's things
[1047] like cells or molecules or people and I
[1050] don't use the
[1051] color scheme systematically from this
[1054] point onwards so we want all right now
[1058] BFO is based upon a view of ontology
[1062] which is opposed to what used to be the
[1066] standard view in on 2fo is based upon a
[1069] view of ontology which is opposed to
[1073] what used to be the standard view in
[1075] ontology circles particularly in
[1077] medicine but also in other fields this
[1079] standard view was called the concept
[1081] orientation and on this view an ontology
[1084] is a representation of concepts and you
[1088] will still sometimes hear the word
[1090] concept in ontology circles so I worked
[1093] I used to be much more irritating than I
[1096] am now and I used to humiliate people
[1099] when they used the word concept by
[1102] asking them to define it and they
[1104] couldn't and I could show very easily
[1107] that if they try to define it then it
[1109] wouldn't work for what they were doing
[1111] now an example of the concept
[1112] orientation is this is sno-med which is
[1115] a very successful ontology like
[1118] initiative they say that for at the top
[1122] level to the topmost term in sno-med is
[1125] the term concept
[1126] Pikul object for sno-med which is sort
[1128] of better but then when they have virus
[1131] test kit they get that risk test kit
[1134] they get that right but when they talk
[1136] about the sickle cell test cake they
[1138] make it they make a mistake and call
[1140] that the substance whipped by substance
[1141] they mean a thing like oxygen or water
[1144] sno-med didn't necessarily make this
[1147] mistake because they were confused by
[1150] the term concept but they did publish a
[1152] warning saying the term concept when we
[1156] use it means actually three different
[1158] things so in other words the very term
[1162] which is the most important term in the
[1163] whole ontology is itself not a term with
[1167] a unitary meaning and what we say
[1170] instead is that an ontology represents
[1173] the types of things in reality some
[1177] things are independent continuance some
[1180] things are animals some things are frogs
[1183] some things are
[1184] and so they are and in each case we have
[1188] a different type of entity and the job
[1190] of the ontology is to represent those
[1192] independent continuance some things are
[1194] animals some things are frogs some
[1197] things are movements of the arm and in
[1201] each case we have a different type of
[1203] entity and the job of the ontology is to
[1205] represent those types of entities and
[1209] the same entity might be represented
[1212] under different perspectives so if we
[1214] talk about a warehouse for instance
[1217] there are two ways of viewing a
[1218] warehouse you can either view it from
[1220] the point of view of the goods inside it
[1222] the stock or you can view it from the
[1225] point of view of things going in and out
[1227] the flows and BFO tries to accommodate
[1234] both kinds of perspectives both are
[1236] equally realistic perspectives on
[1239] reality and both are needed not just for
[1242] dealing with what happens in a warehouse
[1243] but also for dealing with what happens
[1245] in an organism and similarly we can cope
[1249] as we've already seen with different
[1251] granularities effectives on reality and
[1254] both are needed not just for dealing
[1256] with what happens in a warehouse but
[1257] also for dealing with what happens in an
[1260] organism and similarly we can cope as
[1263] we've already seen with different
[1265] granularities we can cope with molecules
[1267] or we can cope with galaxies so BFO is
[1272] meant to be a very general framework for
[1274] representing the types of entities in
[1276] all domains of reality it's absolutely
[1279] domain neutral so that just repeats what
[1283] I just said so we have universals or
[1287] types or categories and then we have the
[1289] instances of those things so I am an
[1293] instance of the type independent
[1295] continuant I'm also an instance of the
[1297] type organism which is a subtype of the
[1301] type of independent continued
[1304] here we have an inventory of instances
[1308] and a catalog of types Oh ontology zaur
[1311] catalogs are very often in inventories
[1315] so these are instances up here you you
[1319] can only photograph an instance you
[1321] can't photograph a universal universals
[1326] have extensions which are the
[1327] collections of all their instances so
[1335] when we're doing science we are not
[1339] interested in instances we're interested
[1342] in universals we're not interested in
[1345] Bill Clinton for instance we're
[1348] interested in organisms or in behavior
[1350] or in qualities of organism or functions
[1355] of organism parts but to do experiments
[1359] we have to concern ourselves with
[1361] instances because we can't do
[1363] experiments without processing specific
[1367] samples or representatives of the
[1370] instances of the universals that were
[1371] interests then what we want the ontology
[1373] to do is to enable us to reason about
[1376] both the instances and the universals
[1379] and it does that by asserting various
[1382] relations between universals for
[1385] instance the is our relation so every
[1387] cat is a mammal every mammal is an
[1390] organism every organism is an object all
[1394] of those are assertions about universals
[1397] and then everything which is true of the
[1401] universal frog is true of all instances
[1403] of the universal frog so every frog is a
[1408] mammal for instance so this is not a
[1411] very good diagram I don't trust me when
[1414] I do biology because I might say things
[1417] like every frog is an animal when I
[1419] should say every frog is well anyway
[1423] so I'm going to say a little bit about
[1426] relations relate ontology terms should
[1430] have definitions by using two part
[1432] definitions so a human being is an
[1435] animal which is rational that's not
[1436] necessarily a good definition a good
[1438] definition for biological purposes but
[1441] it's a good definition for purposes of
[1444] illustrating how to write definitions if
[1446] you want to define a term say B one you
[1450] look in your ontology at what its parent
[1452] term is and then you say well what is it
[1456] about the A's the parent term which all
[1459] the B ones have in common but which the
[1461] b-2s don't have what it what is the
[1463] specific difference separating B ones
[1465] from B to S
[1466] that's the definition it's the species
[1469] plus the specific difference this is the
[1473] jet this sorry this is it's the genus
[1475] plus a specific difference this is the
[1477] species human being a human being is an
[1480] animal which is rational the species is
[1482] the genus with the specific difference
[1485] which picks out the instances of the
[1487] species from the totality of instances
[1490] of the gem in your ontology but then you
[1493] can't define the top term in your
[1495] ontology anyway not in your ontology by
[1498] definition it's the top term alright so
[1503] and you find more rules for definitions
[1505] in Chapter four of the book which you've
[1509] seen so people have trouble with
[1512] definitions it turns out that that rule
[1514] the two part definition rule makes
[1516] definition writing much simpler than it
[1519] would be without that rule and we have
[1522] something like 20 rules for definitions
[1524] with not all of which are quite so
[1528] simple but all of them are helpful for
[1530] writing definitions in a consistent way
[1533] now another traffic rule is that all the
[1537] terms in your ontology should be
[1538] singular nouns and again many people
[1543] mess up their ontology by mixing plurals
[1547] and singulars and the rationale for this
[1550] Ram's in your ontology should be
[1552] singular
[1553] nouns and again many people mess up
[1558] their ontology by mixing plurals and
[1560] singulars and the rationale for this
[1564] rule is that ontology terms represent
[1566] universals and you there is no universal
[1569] cats or dogs there is a universal cat
[1572] and the universal dog and the universal
[1575] headache and so forth so I said already
[1580] you can't take a photograph of a
[1582] universal but you can create cartoons
[1584] and diagrams and this is an example of a
[1587] diagram of universals and of relations
[1589] between universals and this is a kind of
[1593] ontology now it's the the the question
[1603] arises at this point how do we know
[1605] we're dealing with universal so it's
[1608] clear that it cell is a universe now
[1613] it's the the the question arises at this
[1617] point how do we know we're dealing with
[1618] universal so it's clear that it cell is
[1623] a universal it's clear that there
[1625] brother of an Elvis fan
[1626] that's not a universal that's an almost
[1629] random collection a chemical whose name
[1633] begins with B is not a universal and so
[1637] we have clear cases where we are dealing
[1640] with universals clear cases where we're
[1642] not dealing with universal then we have
[1644] some problem cases which are problematic
[1645] in different ways so Higgs boson was a
[1648] problem case until quite recently and by
[1653] a response to people who think that this
[1657] makes ontology building very difficult
[1660] is to say you shouldn't worry there is
[1664] always going to be a penumbra of problem
[1668] cases whether you're dealing with truth
[1670] and in with good and bad or whether
[1672] you're dealing with bald and non bald
[1674] practically all interesting words have a
[1679] penumbra
[1680] in the middle where the black and white
[1684] has a penumbra called gray the fact that
[1687] we have this penumbra doesn't mean that
[1689] nothing is black and nothing is white
[1690] and the fact that we have this penumbra
[1693] doesn't mean that nothing is a universal
[1694] and nothing is not a universal the
[1697] penumbra never causes problems if you
[1701] put dark matter into your ontology that
[1703] will not cause problems and it's true
[1706] for any other problem case putting Higgs
[1708] boson in your ontology as it happened
[1713] wouldn't have caused any problems
[1714] because we now know that there are Higgs
[1716] bosons even if we then discover that
[1719] there are no Higgs bosons you would just
[1721] have to delete Higgs boson from your
[1723] ontology in just the same way that you
[1726] would delete it from your scientific
[1727] theory because ontology so you have to
[1730] change your ontology in light of new
[1732] scientific discoveries this is not a
[1734] problem it's just the way science works
[1736] all right so now I will sketch BFO 1.0
[1740] this was the first released version and
[1743] you've seen this already so at that time
[1746] it was developed in the in Germany and
[1750] as part of a medical ontology project
[1753] and this was the problem that we started
[1756] with this is what motivated the
[1759] development of BFO in the way that it
[1763] was motivated initially and gradually we
[1767] started working with a gene ontology and
[1769] realized that the coherent way of
[1771] thinking of it was in terms of the gene
[1774] ontology division into three kinds of
[1776] entities so we have a tumor and we say
[1781] truthfully that it developed over 25
[1783] years
[1784] but what developed what was it at the
[1787] beginning nothing the tumor developed in
[1790] the lung over 25 years this is a very
[1793] tricky public problem which has led
[1795] philosophers to some very strange views
[1799] so for instance some philosophers do not
[1803] believe that tumors or lungs exist there
[1806] are only humor rating processes and
[1810] longish processes bill clinton doesn't
[1812] exist there is only
[1814] bill clinton izing processes i find this
[1818] view nonsense and it certainly is not a
[1820] help of you if you want to deal with the
[1822] ontology of medicine because it would
[1824] mean that there are no patients or
[1825] doctors so we needed to find a way of
[1830] saving the objects in a world in which
[1834] objects change quite radically and the
[1840] way we look first of all we divided
[1843] everything into objects and processes
[1845] and then we said that let's change quite
[1851] radically and the way we look first of
[1856] all we divided everything into objects
[1858] and processes and then we said that we
[1863] just need to create an inventory of
[1865] reality which will cope with both kinds
[1868] of entities and we'll do so in such a
[1871] way that we can deal with the fact that
[1872] some entities engage in processes which
[1876] involve the beginning to exist of those
[1878] entities or the ceasing to exist of
[1880] those entities and so we took from
[1883] philosophy the distinction between
[1885] continuance and occurrence continuance
[1887] continue to exist from nothing to what
[1891] may be a very large mass and occurrence
[1894] occur they begin that they have a middle
[1897] and then they have an end and these are
[1898] just two very different ways of existing
[1900] in time one is to continue the other is
[1903] to occur so we've seen stocks and flows
[1906] there are products and processes and
[1908] nashit and they are truly very different
[1913] kinds of entities continuance continue
[1917] they can gain and lose parts and still
[1920] be the same you all gained and lost many
[1923] parts in the course of your existence
[1925] but you are the same and again there are
[1929] some philosophers who would deny that
[1931] who would say no there is nothing about
[1934] me which is identical with me twenty or
[1936] forty years ago and to those
[1938] philosophers I say lend me a hundred
[1941] dollars and I promise to pay it back to
[1943] you in ten years I'll pay
[1946] back with 100 percent a year interest
[1948] and then they have to say either that
[1952] they will accept the loan and then of
[1955] course I don't pay it back because they
[1956] don't exist
[1957] well they don't accept the loan and then
[1960] they are revealing that they have a very
[1962] peculiar ontology another feature of
[1965] continuance is that they exist as a
[1967] whole if they exist at all occurrence
[1969] have temporal parts I do not have any
[1972] temporal parts my youth is not a
[1974] temporal part of me it's a temporal part
[1977] of my life which is an ax current and
[1981] occurrence unfold themselves in phases
[1984] people don't have unfold themselves in
[1986] phases occurrence exists only in their
[1990] faces but continuance exists at every
[1994] time at which they exist at all so these
[1997] are two radically different kinds of
[1998] entities so you are a continuant and
[2002] your life is an ax current you are three
[2004] dimensional your life is
[2005] four-dimensional all right so we have
[2010] relations can there are two kinds of
[2013] continuance there are independent
[2014] continuance and there are dependent
[2016] continuance and an example of equalities
[2019] like temperature now processes depend on
[2024] their participants so there is a
[2026] participation relation participation
[2029] relation qualities depend upon their
[2033] bearers and the the continuance which
[2041] participate in process is stand in
[2043] participates in relation and we're
[2048] talking about dependence now this is
[2049] more precisely specific dependence what
[2052] this means is that a specific entity
[2055] specifically depends on another specific
[2058] entity and that means that the first
[2061] entity can't exist unless the second
[2063] entity exists an example is your
[2065] headache if you have a headache and you
[2068] cease to exist and your headache ceases
[2070] to exist your headache is dependent on
[2073] you you are not dependent on your
[2075] headache you can continue to exist
[2077] perfectly well without the headache
[2079] but we have dependence also on the type
[2083] level so a the type specifically depends
[2087] on B that we have dependence also on the
[2090] type level so a the type specifically
[2094] depends on B that's the kind of
[2096] assertion you would find in an ontology
[2098] means that every instance of a depends
[2101] on in the instance level sense some
[2103] instance of B so headache is dependent
[2107] upon organism in the universal sense
[2110] because every instance of headache is
[2112] the headache of some instance of
[2115] organism all right so we're talking
[2119] about specific dependence and there are
[2123] three types of specifically dependent
[2125] continuance we will understand why I say
[2127] specific very soon there is also a
[2129] nonspecific kind of dependence which
[2132] were coming to so qualities roles and
[2135] dispositions qualities are just their
[2138] roles are exercised and they exist
[2143] because we ascribe them to people so
[2146] employers tendencies or powers that
[2150] entities have so tomatoes have a
[2152] disposition to ripen all of these are
[2155] specifically dependent continuance in
[2157] BFF so let's suppose we have a fly we're
[2163] observing the fly we want to annotate
[2165] the phenotypes then we look at the
[2170] phenotype ontology and we see things
[2173] like the particular case of redness that
[2176] we see in this particular fly eye
[2179] instantiates the universal red just as
[2182] the eye that we see before us in this
[2185] fly instantiates the universal eye and
[2189] red is a universal which is a subtype of
[2192] the universal color just as AI is a
[2195] subtype of the universal anatomical
[2198] structure so this is an instance of that
[2201] and that is a subtype of that therefore
[2203] this is also an instance of of that the
[2207] instance of reddest positions are what
[2209] we call realizable dependent kin
[2211] that means they get realized manifested
[2215] executed expressed in certain
[2218] corresponding processes so the pathogen
[2222] roll gets realized in the pathogen
[2226] attacking some host the fragility
[2231] disposition gets realized when the glass
[2233] breaks now a special kind of disposition
[2238] is is function for instance to come or
[2241] to unlock or to steer the state function
[2248] of the steering wheel is to steer the
[2249] car and so on and we'll talk about
[2251] functions and their relations and
[2252] dispositions in a minute so all of these
[2256] things are realizations of realizable
[2260] dependent continuance so the application
[2262] of a therapy the course of a disease the
[2263] projection of a film the exercise of a
[2266] role and realizable these are just three
[2269] subtypes that we have documented so far
[2272] but there's nothing to prevent other
[2275] kinds of realizable or indeed other
[2277] kinds of qualities or non realizable z--
[2280] being identified in them we would just
[2282] change BFO to suit and remember
[2286] everything I'm talking about has
[2288] instances so one way of viewing the
[2291] universe of BFO is to say that it's the
[2293] universe of all of those things which
[2295] have instances there are no numbers in
[2298] BFO because no numbers do not have
[2301] instances and because we rely on
[2304] mathematics we don't want to reinvent
[2306] the wheel
[2308] alright so roles are externally grounded
[2311] they exist because some authority
[2314] ascribes them to the relevant entity
[2321] so they exist because someone is in some
[2323] special physical or social circumstances
[2327] all right so roles are externally
[2330] grounded they exist because some
[2332] Authority ascribes them to the relevant
[2336] entity so they exist because someone is
[2342] in some special physical or social
[2344] circumstances and they that means
[2346] they're optional they can always be lost
[2353] without the bear is suffering any
[2355] physical change so if you get fired you
[2359] don't change physically you may be a bit
[2362] sad neurologically there may be
[2364] consequences but just the act of being
[2367] fired just takes away a role it doesn't
[2369] change you physically so this is how
[2374] they the roles works so nurse is not a
[2377] role because you we define what it is to
[2382] be an instance of nurse to say that you
[2383] are an instance of a human being and
[2386] fire just takes away a role it doesn't
[2388] change you physically so this is how
[2392] they the roles works so nurse is not a
[2396] role because you we define what it is to
[2400] be an instance of nurse to say that you
[2402] are an instance of a human being and you
[2406] have a nurse role so the nurse role in
[2409] here is in you so this the word nurse is
[2413] called a defined class it doesn't it's
[2415] not a term which represents a universal
[2417] it's a term which we can define in terms
[2420] of other terms namely human being and
[2423] nurse role which do represent universal
[2426] [Music]
[2428] now dispositions are realizable which
[2432] are such that the bearer will be
[2436] physically changed if they lose them so
[2440] if you succeed in creating a tomato
[2443] which does not ripen in other words if
[2445] you succeed not on the external
[2447] ascription as in the case of roles but
[2451] on the physic
[2452] of the bearer and dispositions are the
[2457] realm of the possible in BFO so they
[2460] have to do with what can be what what
[2463] tends to be what has the potential to be
[2465] and so on and this is the core of the
[2476] treatment of causality in BFO terms now
[2482] functions you can think of as good
[2484] designed dispositions where they're
[2486] designed either by processes of
[2489] evolution or by an actual human designer
[2492] who is building a car or some other kind
[2495] of machine so functions are like
[2499] dispositions they in fact they are a
[2501] special kind of disposition the physical
[2505] make in order to realize processes of
[2507] that kind so the heart evolved because
[2512] something was needed to pump and the
[2515] heat pump in this particular pump was
[2520] created because someone designed the
[2522] pump to do that and that's why is its
[2524] function to pump so a function is a
[2528] disposition which is such that the
[2531] bearer exists because something was
[2533] needed the rationale for the existence
[2536] of the Bearer is such that something was
[2538] needed to do this thing to pump to steer
[2541] to ripen or whatever it might be to
[2545] treat to kill to save whatever it is if
[2551] the thing exists in order to do that
[2554] thing then doing that thing is the
[2556] function of the thing that exists and at
[2561] this point I'll give you the opportunity
[2563] to ask questions or raise object that
[2565] thing then doing that thing is the
[2568] function of the thing that exists
[2571] and at this point I'll give you the
[2574] opportunity to ask questions or raise
[2576] objections so on throw things at me
[2578] [Music]
[2587] yep yes but you agree that there is this
[2598] seemingly quite evident distinction
[2601] between those things which are ascribed
[2604] and ascribing can have very big
[2607] consequences but it's different from
[2609] those things which exists because of the
[2611] way an entity is structured physically
[2614] [Music]
[2621] know every universal both continuant
[2624] universals instantiate that universal so
[2628] the instance of the universal rabbit is
[2630] the rabbit here on in this area of time
[2634] and space so instances are always
[2636] particulars in time and space universals
[2639] are in principle unendingly repeated in
[2644] all of those instances if you had such a
[2656] magic instrument that you could stop a
[2660] tomato from ripening so it's the
[2661] disposition of the tomato to ripen if
[2663] you want to take that away from the
[2666] tomato you would have to change it
[2667] physically if I if if it's the role of
[2671] John to be a nurse I can take that role
[2674] away from him without changing him
[2676] physically that's quite simple point oh
[2678] yeah absolutely yeah you would yes it's
[2682] still of tomato or even the tomato so
[2687] that the heart can realize its function
[2690] either well when you are healthy or not
[2692] so well and then you're sick this
[2694] wouldn't be important for some of the
[2696] things we serve later on so we have
[2699] realizable dependent continuance
[2701] including dispositions a sub kind of
[2703] disposition its function and functions
[2705] go hand-in-hand with a sub kind of
[2707] process which are functionings so that's
[2710] not a term in BFO but it's the term in
[2712] English so functions are realized in
[2715] functionings
[2715] and another confusion in biological
[2718] ontology is between
[2720] functions and functioning so people very
[2723] often don't realize that there are two
[2725] different things and one could even say
[2727] that the gene gene ontology is not
[2729] absolutely clear about the distinction
[2730] between functions and functioning but I
[2733] don't want to say anything bad about the
[2734] gene ontology all right and then we have
[2737] disease which is also not a term in BFO
[2740] but you can think of diseases as being
[2742] bad functions diseases on which where
[2746] something goes wrong with the
[2747] functioning of the organism because
[2751] there is some disorder in the organism
[2753] so that the function of the heart for
[2755] instance is now malfunctioning now we
[2762] have a few more bits and pieces so sites
[2764] are this is a term in BFO for dealing
[2768] with places for dealing with the
[2769] habitats the niches where organisms live
[2772] for instance so this is a site this is
[2774] Manhattan Canyon and the term Manhattan
[2779] is ambiguous on the one hand Manhattan
[2782] is a collection of bricks and rock and
[2783] wiring and plumbing and so forth in
[2785] which you can see you can we could in
[2788] principle way Manhattan but on the other
[2790] hand you can't live in Rock and wires
[2792] you have to live in the gaps between the
[2796] rock and the concrete and the plumbing
[2798] and so forth and that's a complex site
[2802] so we have two things we have the
[2804] Manhattan you can't live in Rock and
[2806] wires you have to live in the gaps
[2809] between the rock and the concrete and
[2812] the plumbing and so forth and that's a
[2814] complex site so we have two things we
[2818] have the Manhattan the physical
[2819] structure the retainer and then we have
[2821] the gaps where people live and we call
[2823] both of those things Manhattan BFO
[2826] doesn't allow that kind of mistake and
[2829] so we we have the word Manhattan the
[2834] site for this thing and then we have
[2837] Manhattan the material entity for this
[2838] thing and of course very often we talk
[2841] about the extended Manhattan which is
[2843] the some of the material thing plus the
[2845] site and and it just the same applies to
[2849] all the other sites your mouse for
[2852] instance
[2853] sometimes we mean the the lips and the
[2855] the jaw and so forth and sometimes we
[2858] mean the hole with an H that's a site
[2861] and similarly with nostril with your car
[2864] your sites your mouth for instance
[2866] sometimes we mean the the lips and the
[2869] the jaw and so forth and sometimes we
[2872] mean the hole with an H that's a site
[2875] and certainly with nostril with your car
[2878] your fridge your bed or all of these
[2882] have this ambiguity between site and
[2884] material and retainer for the site so
[2889] why do we need well we have mbf Oh both
[2891] sites and 3d regions and the reason why
[2895] we need both is because sites move
[2897] around they go through distinct 3d
[2900] regions where 3d regions can't move
[2903] they're tied to the relevant frame of
[2906] reference so this is why we need both
[2910] and and we've used the the BFO ontology
[2915] of sites to create the protein site
[2918] ontology for the protein ontology so
[2921] PTMs teen molecule and so we we can
[2929] distinguish various different kinds of
[2931] sites and amino acid change site the
[2933] site of an amino acid residue in a
[2936] protein the cited post translationally
[2938] modified amino acid residue within a
[2940] protein and so forth and we get this
[2942] kind of hierarchy then and
[2946] [Music]
[2951] each instance of Mao's histone h3
[2953] point-three site is part of some amino
[2956] acid chain and is the location of some
[2958] amino acid residue and this is the this
[2962] is part of the protein site ontology as
[2965] a hierarchy alright now we move on to
[2968] BFO 1.1 this is where we add generically
[2973] dependent continuance and generically
[2976] dependent continuance our continuance
[2978] that can get our patterns that can get
[2981] copied which means all the intimate if I
[2985] have a headache you cannot have my
[2986] headache but if I have a PDF file you
[2989] can have my PDF file and similarly we
[2992] know that G sequences and protein
[2994] sequences and so forth can be copied so
[2996] they too are generically dependent
[2999] continuance they are like qualities
[3001] complex qualities which can be copied
[3004] from one bearer to another and all of
[3007] these things are examples of information
[3011] artifacts which are generically
[3012] dependent continuance and also things
[3015] like plans and laws are examples of
[3018] generically dependent continuance so you
[3021] write a plan on a piece of paper and you
[3023] you can instruct someone else in the
[3026] plan and then the plan has been moved
[3028] from one bearer to another Bearer and we
[3033] can concretize plans so with the
[3037] Beethoven's Ninth Symphony is concretize
[3039] in a certain pattern of ink ink marks on
[3041] a score that score at score is a set of
[3045] instructions to create a certain process
[3049] called the performance and we know that
[3054] scores can be copied they can be copied
[3057] by writing out another copy or they
[3059] could be copied by scanning or by
[3061] sending to a publisher and telling the
[3063] publisher to print a thousand copies the
[3065] thing which gets copied that which is
[3068] the same across all of these
[3070] concretization x' is a generically
[3073] dependent continuant it's a pattern
[3074] which can exist in many different
[3077] bearers you need patterns to deal with
[3080] information entities and deal with gene
[3083] sequences
[3084] [Music]
[3085] yeah yeah and of course the same pattern
[3091] can be concretize in different kinds of
[3093] media in ink or in pixels or in other
[3097] kinds of medias so when we pixels or in
[3105] other kinds of media so when we when we
[3112] fill in a form we create a pattern which
[3117] is based on the empty form the we fill
[3121] in the gaps in the empty form that
[3123] pattern can then be scanned we can use
[3126] optical character recognition in order
[3128] to create a PDF version of that pattern
[3130] it's the same pattern but it exists in
[3133] different concretization and BFO has
[3136] room for both the concretization and for
[3139] the information content entities which
[3141] are the same in the different
[3143] concretization and that can be very
[3145] important when you're keeping track of
[3146] how data was entered in a hospital for
[3148] instance all right so we've said all of
[3154] that and this is how it looks so we have
[3156] specifically dependent continuance which
[3158] equalities and realizable we have
[3160] generically dependent continuous which
[3162] are information up topmost term of the
[3164] information artifact ontology and that's
[3167] the topmost term of the sequence
[3168] ontology alright these are some
[3173] information entities in science these
[3175] are other information entities that
[3176] people use in labeling and demographics
[3179] and so forth you see that the realm of
[3181] the information artifact ontology is
[3183] very broad but now what is
[3186] characteristic of information artifacts
[3188] is not merely that they are patterns
[3190] copyable patterns but also that they're
[3193] about something that's how we define
[3196] information artifacts they are there is
[3199] something which they are about alright
[3203] BFO 2.0
[3205] [Music]
[3208] so this has been the the release version
[3215] of BFO for several years now and you can
[3219] find the specification in the user guide
[3222] it's debated still that there are a lot
[3224] of people using it and it's really
[3231] changed very little compared to BFO 1.1
[3235] so it's changed in various
[3237] terminological ways we have a slightly
[3239] more detailed treatment of space and
[3241] time we changed our view of spatial
[3244] boundaries so that all boundary all
[3247] spatial boundaries are now Fiat
[3249] boundaries and what that means is that
[3250] they are either a product of human
[3253] discrimination as when we draw the line
[3256] between France and Germany for instance
[3258] or they are like a product of human
[3262] discrimination in other words they are
[3263] not discontinuities in the physical
[3266] world and the reason for this is that
[3270] whatever you choose as a candidate for
[3275] being a real physical discontinuity
[3277] turns out to be not a physical
[3280] discontinuity when you examine it at a
[3282] sufficiently mark when we shake hands
[3283] with somebody we want there to be two
[3286] people involved and that means there has
[3288] to be a boundary between the one person
[3290] and the other person but that boundary
[3292] is a Fiat boundary we say and then we we
[3302] link the various different kinds of
[3305] spatial boundary with corresponding
[3308] kinds of spatial regions so there are
[3310] zero dimensional spatial regions which
[3312] are points for instance the north pole
[3314] or the South Pole
[3315] the only two good examples at least on
[3319] this planet and then there are one
[3322] dimensional spatial regions which are
[3323] all the lines of latitude and longitude
[3325] and then there are two dimensional
[3327] spatial regions which are the quasi
[3329] rectangles formed by those lines and log
[3332] of latitude and longitude and then there
[3334] are three dimensional spatial regions
[3335] which are the surface of the earth as
[3337] represented in the lines of latitude and
[3340] longitude
[3340] and they correspond the latitude and
[3342] longitude and they correspond to zero
[3346] dimensional contains ero dimensional
[3348] Fiat boundaries one-dimensional Fiat
[3350] boundaries and so on these are
[3352] boundaries in the things these are
[3354] boundaries or regions in the space which
[3359] the things occupy so we have things and
[3361] we have the spatial regions which are
[3364] occupied by those things and sites are
[3368] like objects they too are occupying
[3371] three-dimensional spatial regions so
[3373] Manhattan the site really does occupy a
[3376] certain spatial region at any given time
[3378] and so similarly for processes so we
[3383] have process boundaries which occupy
[3386] time points and processes which occupy
[3390] time intervals and we in in BFO two we
[3396] distinguish two families of independent
[3400] continuant material and processes which
[3404] occupy time intervals and we in in BFO
[3410] two we distinguish two families of
[3415] independent continuant material entities
[3417] and immaterial entities and sites are
[3419] examples of immaterial entities because
[3422] sites are not made of anything they are
[3424] the gaps between the material entities
[3426] and we distinguish between three kinds
[3432] of immaterial entities namely sites
[3434] boundaries and spatial regions and we
[3437] distinguish three kinds of material
[3440] entity and this is a very very partial
[3447] partition since we don't rule out that
[3451] there could be other kinds of material
[3452] entities in addition to objects which
[3455] are self-contained like organisms fiat
[3459] object parts which are part since we
[3463] don't rule out that there could be other
[3464] kinds of material entities in addition
[3467] to objects which are self-contained like
[3470] organisms
[3471] via object paths which are parts of
[3475] self-contained objects which are not
[3476] detached for instance my arm or my nose
[3478] and object aggregates which are the
[3483] Beatles or the Rolling Stones if you
[3487] prefer so these are different kinds of
[3492] material entity and the objects are the
[3497] natural units they are causally
[3499] relatively isolated so that organisms
[3501] portions have solid matters such as
[3503] rocks and engineered artifacts such as
[3506] watches and cars these are the three
[3508] families of objects which are currently
[3513] documented in the literature on BFO but
[3516] which are certainly not exhausted so we
[3518] need to deal with for instance ice cubes
[3521] don't know where to put them yet we will
[3523] know where to put them we will need to
[3524] have a force and maybe even a fifth for
[3528] plasma but we're working on that know
[3531] where do we claim that BFO is complete
[3533] yes oh not so I think that it's almost
[3547] certainly the case that there are
[3548] examples of entities with an inherent
[3551] shape under all three headings but there
[3553] are certainly examples under object but
[3556] I don't think it's a criterion for being
[3558] an object yet though that might be a
[3564] reason for having liquid as being a
[3566] separate category we need to find a
[3569] place for liquids there's no portions of
[3571] liquid there's no question about that of
[3572] course we can always put them under
[3574] material entity so the rule is that if
[3577] you don't know where to put them on a
[3579] lower level then just move why is it not
[3584] there because we know that we can put
[3589] them on the material entity and people
[3591] were satisfied with that but we we are
[3593] not satisfied ourselves any more so in
[3596] fact there is already a version with
[3598] liquid and plasma there which I can give
[3603] you
[3604] if you wish oh that's a sight no problem
[3609] put your finger in it society you can't
[3614] eat the whole or by itself your way you
[3620] mean that the the all right so these are
[3628] fiat object parts and this is an object
[3632] aggregate it's it's something like a set
[3635] but it's treated as material it's a
[3637] certain part of material reality picked
[3639] out by a certain kind of granular parts
[3641] of the study picked out by a certain
[3643] kind of granular partition so the
[3644] Beatles or the Rolling Stones would be
[3646] another example three apples is an
[3649] example of an object aggregate in the
[3650] BFO sense and then finally in BFO 2.0 we
[3655] added the term history a history is a
[3658] very special kind of process it's a
[3661] process which consists of the sum of all
[3665] the constituent processes taking place
[3667] in the spatial temporal region occupied
[3670] by a material entity so it's your life
[3673] if you like it's the time worm which
[3676] consists of all the processes in which
[3678] you engage yeah
[3684] [Music]
[3690] yep a piece of lasagna is an object a
[3705] portion of lasagna a lasagna if you wish
[3709] in the pan that's an object so as I said
[3716] earlier there there can be partitions of
[3719] reality on different levels of
[3721] granularity so certainly there are
[3724] objects inside the lasagna so it's it's
[3727] it contains objects as part that doesn't
[3730] mean that it's an object aggregate
[3732] necessarily the object aggregate
[3734] contains nothing else but the lasagna
[3737] contains liquid for instance a lasagna
[3741] can't contain air pockets so it's not an
[3746] object aggregate it has objects as part
[3749] you have objects as parts but you're not
[3751] an object aggregate for exactly the same
[3752] reason absolutely but thereby you've
[3757] introduced other things like air pockets
[3759] say it's nothing but those members which
[3763] are material we're aggregating when you
[3768] you might aggregate and then boil or
[3771] puree and I'm hoping that a puree of
[3774] lasagna is not an object in your
[3776] ontology all right
[3778] so history we've dealt with so now I
[3784] said the fourth key to ontology success
[3787] was choosing the right hub so now I'm
[3790] going to consider what how BFO
[3792] distinguishes itself in the competition
[3795] between the existing top-level ontology
[3798] is because there are several top-level
[3800] ontology which exist now BFO has a very
[3807] large user base I don't think that by at
[3810] least one order of magnitude there are
[3812] people who use the other ontology s but
[3815] they they they tend to be where they are
[3817] use tied to single projects and has a
[3820] very large user base
[3821] I don't think that but by at least one
[3824] order of magnitude there are people who
[3826] use the other ontology s but they they
[3829] they tend to be where they are used tied
[3831] to single projects and then there is no
[3834] follow-through where many of the people
[3836] using BFO have been using B fo for some
[3839] years and they they create sub projects
[3843] so in other words there is a life to the
[3845] uses of B fo but there are many many
[3847] more of them than there are with regard
[3850] to the other projects also there's a
[3852] much wider variety of projects using B
[3855] fo also b fo is much smaller than some
[3859] of the other competitor top-level
[3861] ontology and if there's if they're large
[3864] and I'm talking thousands of terms now
[3867] then that harder to learn and BFO it is
[3872] so there that you there are people who
[3874] know how to apply B fo and you can apply
[3877] it over and over again to different
[3879] cases they're large and I'm talking
[3882] thousands of terms now and that harder
[3883] to learn and BFO it is so there that you
[3889] there are people who know how to apply B
[3891] fo and you can apply it over and over
[3894] again in different cases and there there
[3896] is a lot of experience which has been
[3898] accumulating and most of it is
[3899] documented in one way or another in the
[3902] user forum alright so the three main
[3905] candidates are BF o Dolce and sumo so BF
[3912] o is small and it's strictly domain
[3914] neutral so it doesn't contain any domain
[3916] specific terms at all Dolce is pretty
[3921] close to BF o it's roughly the same size
[3923] it has the same goals and structures it
[3925] has some domain specific terms such as
[3928] society achievement accomplishment so it
[3931] it tends to be interested in human
[3934] things and b fo b fo is interested in
[3936] nothing except the most boring and then
[3940] sumo is much larger than either BF o or
[3942] dolce and it incorporates many
[3944] domain-specific terms such as body
[3946] covering or fruit or vegetable now there
[3952] are others so there's upper psyche but
[3955] that's that has three thousand terms
[3957] it's not a true upper ontology at all
[3959] and there is a website which has several
[3963] others but they are hardly used if they
[3966] are used at all or there are things
[3970] which claim to be top-level anthologies
[3972] but they're not so there's something
[3973] called marine TLO that is not a thiele
[3976] at ELO is absolutely general so we'll
[3981] talk just about dolce sumo and upper
[3987] psyche very briefly so b fo and dolce
[3991] grew out of the same motivations in fact
[3993] the I was working with the Dolce people
[3997] when Dolce was born so they they look
[4000] very similar and they both the rest on
[4005] this basic distinction we continued sin
[4007] occurrence they both rests on a
[4009] distinction independent independent
[4011] entities the latter Dolce just calls
[4013] qualities and they both rest on a
[4016] distinction instances and universal so
[4018] they don't have any further levels just
[4021] those two so that means that they are
[4023] very close so these are so BFO as in
[4029] addition to having more users it has
[4030] better documentation to be honest so
[4033] it's not always good to live in Italy it
[4040] has more rigorous definitions in
[4042] available in more forms so there's
[4044] nothing like the the BFF book for Dolce
[4047] and it has a much larger cadre of people
[4050] who know how to use it so BFO has taken
[4054] care of its users much more than Dolce
[4057] so there are instances and there a
[4061] universal so I am an instance of the
[4064] universal man and this headache in my
[4067] head is an instance of the universal
[4069] headache we need entities in all four of
[4072] these realms in order to do justice to
[4074] reality in fact BFO has six categories
[4077] because it has process universals and
[4080] process instances in addition to
[4083] qualities in
[4084] object instances object universals and
[4087] quality universals of quality instances
[4093] your headache process instance my arm
[4096] movement and this is another instance
[4099] this is another instance the same type
[4102] of album which is a certain move in an
[4106] Irish dance that's the process of
[4114] cooking the recipe tells you because
[4118] that's the technical term so you realize
[4120] a plan by going through the steps which
[4124] the plan instructs you to follow so you
[4126] realize a recipe by going through the
[4128] steps which the recipe instructs you to
[4130] follow and then going through those
[4131] steps is a series of processes which
[4134] makes one long process which is the
[4136] realization of the recipe I can see
[4140] there's a certain interest in food over
[4141] this corner all right so you'll see why
[4148] I mentioned this ontological square in a
[4149] minute so both BFO and dulce have an
[4154] ontological Asafa chol sauce I started
[4157] out being a philosopher and I stopped
[4159] being a philosopher I became an
[4161] oncologist Nicola Moreno started out
[4164] being an engineer and he says in his in
[4168] his memoirs that he stopped being an
[4172] engineer because of me so we've changed
[4176] places as it were Eno started out being
[4179] an engineer and he says in his in his
[4182] memoirs that he he stopped being an
[4186] engineer because of me
[4188] so we've changed places as it were
[4191] alright so what so for BFO universals
[4196] that they are in reality they're the
[4198] kinds of things that scientists study we
[4200] study the universal electron we study
[4203] the universal cell we study the
[4204] universal tuberculosis for Dolce
[4210] universals are what they call conceptual
[4213] containers so they belong to the realm
[4217] of our concept
[4218] they don't belong to the realm of what
[4219] is in reality so earlier on I said you
[4228] shouldn't worry about dark matter if you
[4230] want to put dark matter into your
[4231] ontology go right ahead I say the same
[4233] thing to lasagna
[4234] [Music]
[4236] Versalles and then a penumbra of problem
[4239] cases in the middle I agree that lasagna
[4241] is a problem case but you can put it
[4243] under universals when you're doing a
[4245] food ontology you would have to do that
[4246] it's fine yeah it relaxed put lasagna in
[4250] your ontology portion of lasagna so you
[4255] never create lasagna you create a
[4257] portion of lism so I believe that a key
[4279] to creating a good ontology is to write
[4282] good definitions for all the terms and
[4284] all the relations the reason I believe
[4288] that is because you're never going to
[4291] teach anybody to use it properly unless
[4293] they can check the definitions however
[4296] there are certain issues however there
[4298] are certain areas where definitions are
[4302] not so important presumably everyone
[4304] who's using your ontology will know what
[4306] lasagna is anyway and writing a
[4309] definition would really in part just be
[4314] reproducing the recipe so you probably
[4317] don't need a definition of lasagna but
[4319] that doesn't mean that lasagna is not a
[4320] universal
[4325] so being a universal does not
[4327] necessitate that we are able to write a
[4329] definition we knew that there was
[4332] something called SARS before we knew how
[4336] to define it so there are very many
[4339] cases where we know that there is a
[4340] disease and we know it's the universal
[4342] because there are lots of patients
[4343] coming with the same symptoms we don't
[4345] know how to define that disease now you
[4348] do know how to define la santé but you
[4349] don't need to define it in order for us
[4351] to know that there is a universal with
[4353] lots of subtypes there is vegan lasagna
[4355] since we don't know how to define that
[4358] disease now you do know how to define
[4361] Lausanne you but you don't need to
[4362] define it in order for us to know that
[4364] there is a universal with lots of
[4366] subtypes there is vegan lasagna for
[4369] instance for all I know
[4370] [Music]
[4372] all right so so for da da Jie is much
[4379] more social and culturally focused not
[4381] merely in the sense that they contain
[4383] terms such as organization in the
[4386] ontology but also in the sense that they
[4388] see universals as being cultural
[4390] creations and so they don't draw a clear
[4393] line between reality and fiction or
[4395] between reality and myth and that goes
[4399] hand-in-hand with the fact that Dolce
[4401] tends to be interested in linguistics so
[4411] the many of the people who've been
[4413] working with Dolce have been you like
[4419] linguistics so the many of the people
[4422] who've been working with Dolce have been
[4424] using Dolce for various kinds of
[4427] supporting various kinds of linguistics
[4430] related activities and language relates
[4433] across a domain much larger than the
[4435] domain of real entities which is what
[4438] BFO is interested in language goes on
[4441] holiday scientists never go on holiday
[4447] alright so this is the ontological
[4450] square the problem with sumo is that
[4454] it's not based on the ontological square
[4457] so it tsumo in fact incorporates a small
[4460] piece of BFO it was put together by
[4462] combining various ontological components
[4465] from different circles the first problem
[4468] is sumo is that it's not a true formal
[4469] ontology it contains words like monkey
[4471] for instance but the main problem is
[4474] that it doesn't have it only has
[4476] universals corresponding to predicates
[4478] to the extent that it has universals at
[4481] all all its individuals are material
[4485] entities so the ontology is much thinner
[4489] from a the point of view represented by
[4494] this diagram at least than either BFO or
[4497] dolce so they have no room for headache
[4499] headaches so headaches are accidental
[4503] they are caught they are things which
[4505] come and go but there's no place in sumo
[4510] for headaches and I confronted the the
[4514] although maintainer of sumo and he said
[4517] no there are no headaches of course
[4519] there are no headaches there are just
[4520] people and then we predicate of those
[4523] people that they have a headache but
[4526] that's like predicating that they are a
[4528] person or they are hungry think that for
[4530] medical purposes you have to have
[4532] headaches in your ontology and you have
[4535] to have other diseases too and sumo has
[4537] no room for those things all right so
[4540] psyche psyches is a common-sense
[4543] ontology it's short for encyclopedia and
[4545] it was designed to create a
[4547] representation of the entirety of human
[4549] common sense and it's inconsistent
[4551] deliberately it's full of micro theories
[4554] which are not consistent with each other
[4556] and the the reason the rationale put
[4559] forward by psych is that common sense is
[4561] not consistent so why should an ontology
[4563] of common sense be not consistent now
[4565] BFO and dulce both think that an
[4568] ontology must be consistent and and so
[4573] common sense includes things like the
[4575] virgin mary and so the Virgin Mary is in
[4579] psyche the so the virgin birth actually
[4584] that's even better so the virgin birth
[4586] in psyche is the conceiving something by
[4589] a logic
[4591] actually no anyway this is not very
[4594] important
[4596] so John sower who is a kind of Jeremiah
[4603] who participates in lots of ontology
[4607] fora and argues that no good ontology
[4610] can be created and one line of argument
[4614] that he takes is that philosophers argue
[4616] all the time and said I'll never be a
[4619] good good
[4620] single ontology and the the and that's
[4624] why psych is so wonderful because psych
[4626] is full of inconsistencies because
[4627] that's the way all ontology will have to
[4631] be so he says that that there is no
[4637] scientific knowledge that is not just
[4639] what he calls knowledge soup and we
[4644] should stop attempting to achieve
[4645] consistency and develop instead a
[4647] structure of micro series to accommodate
[4649] an open-ended possibly inconsistent
[4650] knowledge soup rich enough to include
[4653] any possible language game now I think
[4657] this is this is the the gene ontology
[4660] proves that we can do ontology not in a
[4665] form of knowledge soup and if you're
[4668] interested you can hear a debate between
[4670] him and me which is very funny so
