---
schema_version: 1
id: yt-mjSAghcxJK4
type: youtube
title: Meghyn Bienvenu. Ontologies in Computer Science and Description Logics (2/2)
url: https://www.youtube.com/watch?v=mjSAghcxJK4
authors:
- VIKTOR GORBATOV
ingested_at: '2026-06-17T18:26:15Z'
content_hash: sha256:ddfc798576486301c6627a5160ceb04d38a8b3099f62b2243cdd611a8648d1be
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: VIKTOR GORBATOV
  channel_url: https://www.youtube.com/@VVGorbatov76
  duration_seconds: 1710
  caption_track: fetched
  snippet_count: 761
filter:
  score: 0.71
---
[5] okay so that's satisfiability that's a
[6] first Bas very basic uh reasoning task
[9] we need next one subsumption so here we
[14] want to check whether in every model
[17] some concept is a subset of another
[19] concept
[21] okay and why do we want to do this well
[23] first of all we really want to
[26] understand the relationships between the
[28] different concepts that we've expressed
[30] uh so some things might not be put there
[34] explicitly in the antology but in fact
[35] by chaining together uh doing some
[38] reasoning we're actually able to infer
[40] new relationships okay um in fact one
[43] particular if we uh a more specific task
[46] then subsumption is something called
[48] classification so here what we do is we
[49] take all of the atomic Concepts that
[52] appear in our onology and we do all the
[55] subsumption checks to see which ones are
[58] more General more specific than each
[59] other and we organize our antology our
[62] Atomic Concepts into basically a
[64] hierarchy okay and this is very useful
[67] uh for navigating the antology for
[69] seeing what's in it and and also yeah so
[73] both for understanding it and also for
[75] debugging it
[76] because uh satisfiability okay we
[79] definitely want our knowledge base to be
[80] satisfiable but that's a pretty minimal
[84] uh guarantee on the quality right the
[86] fact that there's no contradictions
[88] doesn't mean that it that it gives us
[90] the information we want and so if we for
[93] instance compute all the uh inclusions
[95] between the atomic Concepts and then we
[97] see that there's either an atomic
[100] subsumption like there's an inclusion
[103] that is missing or there's an inclusion
[105] that is there that we don't think should
[107] be there this gives us some other
[108] additional information uh about what
[111] might be wrong with our ontology okay so
[114] this is another uh useful tool for
[117] checking for errors and and just
[118] checking that the modeling that we've
[119] done is is is correct or as as far far
[123] as we can tell so let's take another
[124] example here so here I have something a
[128] little bit more complicated okay so this
[129] is a bit as before giraffes are animals
[131] that only eat leaves trees are plants
[134] okay leaves are parts of trees and now I
[138] have a bit more complex definition I
[139] decid to write it in another way so now
[141] I say that herbivores are
[143] animals that only eat things that are
[146] not animals okay maybe this is not the
[148] right way to do it but someone might
[149] write it might think to write it in this
[151] way and they only eat things that are
[154] not parts of animals okay okay so this
[157] is one way you might think of writing it
[159] and then we have this last statement
[161] here which maybe looks a bit complicated
[162] but it's really not very hard it just
[163] says that if I'm an animal or if I'm a
[166] part of an animal then I can't be a
[168] plant and I can't be a part of a plant
[170] okay so it just states that this is
[172] destroyed with that this is destroyed
[173] with that it's just so I don't run off
[175] the slide I put them all together in one
[177] but that's all that it
[178] says okay and so my question is is it
[182] the case that my uh my knowledge base
[187] implies this subsumption do I have that
[190] this axium is
[194] entailed because is an animal and that
[198] the animal who it's uh Le it is the
[201] animal who who it's not animal and who
[205] it's
[207] not okay so you think it's good
[211] well no I mean giraff is not equivalent
[213] to
[214] Herbivore but I mean
[217] uh something who it'ss Le yeah and
[221] something who it'ss not animal and not
[224] AAL okay so they're not equivalent but
[227] there is a subsumption so indeed if I
[230] only eat leaves it means that I only eat
[233] things that are not animal and I only
[235] think that are not parts of animal so
[236] they're not equivalent these Expressions
[238] don't mean the same thing but but indeed
[240] this is stronger this implies this and
[242] this implies this when you put it
[243] together with these you need these three
[245] other axioms you have to chain the
[246] reasoning together and then you're able
[248] to infer indeed that uh that we satisfy
[252] these conditions and so giraffe are
[255] herbivores okay
[259] good okay so another important thing is
[263] that we'd also like to do some reasoning
[265] with our aox right so we have some data
[267] we want to be able to do some reasoning
[268] on it as well um um so for instance a
[271] very simple uh task is to find uh all
[274] those individuals that belong to a given
[276] concept C so I have some class
[277] description I want to identify those
[279] individuals that satisfy this class or
[281] that belong to this class
[283] okay um or you could do advice so you
[286] could pick an individual and you want to
[287] find out which classes it belongs to
[290] okay and this is a very simple way of
[294] querying our ax okay our set of
[298] facts and then
[300] another way of doing some querying which
[303] is a lot more complex and it's become
[306] popular in recent years is conjunctive
[308] query answering so I won't go through
[310] all the definitions because it would be
[312] long and it's it's really not necessary
[314] but the idea is that we're going to have
[315] some sort of we're going to have a
[317] conjunctive query and I'll give an
[319] example in the next slide um and we want
[322] to find those tuples of individuals that
[325] always satisfy this query they're
[326] basically answers to it and the idea is
[328] that these conjunctive queries are
[331] correspond to a very standard class of
[333] queries in databases and so the the
[335] thing is is that if we want to um take
[339] basically a database but which gives an
[340] incomplete description of the world okay
[342] so I have a bunch of facts but maybe
[344] it's really big so it's kind of like a
[345] database nowadays um and then I want to
[348] add on top of it an ontology because I
[350] want to be able to infer an additional
[351] information using some background
[353] knowledge okay then people are going to
[356] be pretty unsatisfied if they can only
[358] ask these simple queries because maybe
[360] they before they were querying their
[363] data with database engines using
[365] database languages and they could make
[367] very complex queries they didn't have
[369] any sort of reasoning or knowledge but
[371] they could have complex queries and so
[372] these people are going to be very
[373] unhappy if we take away their query
[375] language okay they want to be able to
[376] say say the same types express the same
[379] types of questions as before and so that
[381] means that in description Logics we've
[384] now move to considering more complex
[386] queries that we can pose over our
[388] knowledge basis okay and what makes
[390] difficult is that they are complex
[392] queries from databases but now we have a
[394] more complex setting because we also
[396] have knowledge we have models instead of
[398] a single interpretation so very simple
[400] example here is suppose that I have in a
[405] very really simple ontology here just
[408] inclusions okay so mountain gorillas are
[410] gorillas gorillas are primates mountain
[412] gorillas are critically endangered and
[414] then I have some facts probably have a
[416] lot more but here are three so I know
[418] that Molly is a mountain gorilla who is
[420] kept at the burden zoo and the B zoo is
[422] a zoo okay um then a conjunctive query I
[425] might ask is something like this so they
[427] they consist of a bunch of atoms with
[429] variables and conjunctions between them
[431] okay so I might want to find all those
[433] pairs X and Y such that X is a primate
[436] and X is critically endangered part of a
[439] critically endangered species and X is
[441] kept at Y and Y is a zoo for instance
[444] okay and using the information here
[447] together so this is the just the facts
[450] together with the information in our T
[451] box we would be able to get back uh
[454] Molly Berlin Zoo okay but if you just
[458] have the bare facts you wouldn't be able
[459] to do this okay you need to have
[461] admittedly some very simple knowledge
[463] here is really nothing more than just a
[465] hierarchy of classes but in many
[467] realistic cases already adding this
[469] allows you to do a lot more when you're
[471] doing queries
[473] okay so those are the main reasoning
[476] tasks so now that we've defined our
[477] reasoning tasks we can talk a little bit
[479] about how how hard it is to perform them
[482] so if I want to make an algorithm and
[484] get a computer to do one of these tasks
[485] for me how hard is it going to be so
[488] there have been really very extensive
[491] investigations into the computational
[493] complexity of reasoning um people have
[496] considered a huge variety of different
[499] description Logics ranging from very
[501] very simple things that aren't much more
[503] than taxonomies uh all the way up to
[505] incredibly expressive things still of
[508] course not all the first order logic
[509] because we want to remain decidable but
[511] you can really say quite a lot of things
[513] and they've considered various reasoning
[515] tasks so for instance if we look at
[517] things like satisfiability subsumption
[520] instance checking these turn out to
[521] basically always have the same
[522] complexity they're inter reducible but
[525] once we move to conjunctive queries this
[527] actually requires completely new
[529] algorithms and often has like a
[530] different complexity okay and there's
[532] actually a variety I will discussed on
[534] the last slide that there are also a lot
[537] of newer reasoning tasks that are very
[539] relevant
[540] and for those also people have studied
[542] the complexity of them okay so nowadays
[546] we have quite a good understanding so
[548] here what I pictured and unfortunately
[550] it comes out uh a bit fuzzy is there is
[553] a website with a compl the description
[556] logic complexity Navigator and you can
[558] click some different boxes to say which
[560] things you want to put in your
[561] description logic and once you do that
[565] and you click go then it's going to
[566] display the complexity for you and also
[569] the references to where this was proven
[571] okay it only handles the so-called
[573] expressive description Logics there are
[575] some more restricted ones we consider
[577] nowadays that aren't there but it's
[578] still uh a useful resource and here's
[581] just a picture which has uh among the
[583] expressive description of Logics all the
[585] different relationships and so on so you
[586] can see and this is just some of the
[588] Logics that people consider there's
[589] really a whole whole SLE of them okay
[592] now what uh what is the takeaway message
[594] from all this work on the complexity of
[597] reasoning well the first thing is that
[600] that it's pretty bad okay if we look at
[603] the computational complexity so I don't
[605] know how many of you have seen this
[606] before so are people for instance if
[608] some of you seen like MP complete is
[610] this something you've seen okay so MP
[612] complete is a class um that we don't
[616] know for sure that it can't be done in
[617] polinomial time but we strongly suspect
[620] that it can't be done in polinomial time
[622] so for a long time people said oh our
[623] problems NP complete ooh we're not going
[625] to be able to handle it okay the cas
[629] what what we know with description
[630] Logics is that for most of the
[631] description Logics that have been
[632] considered in the literature uh
[634] reasoning by which I mean satisfiability
[636] subsumption and so on is X time hard or
[640] worse so X time is the class of things
[642] basically that take exponential time
[644] that's basically the definition of it
[645] okay and so for these it's not just that
[648] we excuse me suspect that it's
[651] intractable we know that it's
[653] intractable of course the good news is
[656] is that this is a worst case complexity
[659] result it means that can find some
[661] ontologies and you have to craft really
[663] nasty things in them okay uh for we and
[666] some uh data sets for which I can get
[670] this result uh it doesn't mean that
[672] necessarily the things that we uh
[674] encounter and practice will necessarily
[676] be as bad as this and this was why
[677] there's still hope even for the Logics
[679] that have this bad complexity result
[682] nonetheless it does mean that we have
[684] some challenges if we want to implement
[686] fast reasoners for these Logics but
[690] yeah does have to do with the fact that
[692] say classical
[695] logic if I I'm correct we have to it
[698] doesn't have anything like computable
[700] model right so it's yes so that sort of
[704] logic somehow it's very different from
[706] what you have algorithmically and that's
[709] why it just goes well I guess what you
[712] can see it as is that okay for us in
[714] some of our description Logics okay I
[716] mean first of all a difference with
[718] first logic is we are decidable for most
[720] of the ones we consider um the big
[722] difference is that um we in some cases
[726] we do have finite models even we can
[728] show that if it's satisfiable it's
[729] always satisfiable in a finite model
[731] however the size of these models can be
[733] very large and so basically the the size
[735] of the model that you need to look at
[736] could be exponential size and that is
[738] what kind of gives you this here yeah um
[741] so there's a variety of things that come
[743] together to make it hard actually
[745] different combinations of our
[746] Constructors will move you to this x
[748] time um but a main idea is that even if
[752] we can either actually come up with a
[755] model like because it's finite or we can
[757] come up with a finite representation of
[759] a model these typically are very large
[760] and this is what causes problems yeah
[764] okay so another thing that came out of
[765] all this work is that people identified
[767] useful tractable description Logics but
[770] by which I mean description Logics for
[772] which we can do reasoning in polinomial
[773] time and the thing is that in the very
[776] beginning actually of description Logics
[777] people because they found out that some
[779] things were NP complete and they were
[780] very worried so they tried to restrict
[782] things but what they came up with were
[783] Logics that were unusable nobody in the
[786] right mind would Express knowledge using
[787] these Logics the interesting thing is
[789] that more recently like starting from
[791] like the 2000s
[793] people played with different ways of
[796] restricting it and they came up with
[797] ones that are actually very relevant in
[799] Practical applications and are possible
[803] uh polinomial time reasoning so that's a
[804] very nice development and nowaday people
[807] work really on both because the idea is
[808] that now that we have an idea of the
[811] complexity when you need to do some
[813] modeling you choose the weakest logic
[816] that will meet your modeling needs okay
[818] so you have these complexity results to
[820] guide you and you can see oh well maybe
[822] I should try to avoid adding this
[824] because it will take me from being
[825] polinomial uh to something much worse of
[827] course in the end if you really need
[829] very complex modeling then maybe that is
[832] more important than being able to go
[834] fast okay just to uh and I'm I'm fairly
[837] close to the end so don't worry uh just
[839] to illustrate a little bit this
[841] complexity versus expressivity tradeoff
[843] so this is a very standard description
[845] logic this is actually the one that is
[847] pictured here it says base description
[849] logic ALC so this is a really standard
[851] one um and it basically had the Bon
[854] things and the existential universals
[856] okay so it's really natural it's kind of
[857] naturally comes up if you take like the
[858] basic modor Logics and you kind of try
[860] to find the coronary description Logics
[862] okay so it's very natural and for this
[865] one you can show is X time complete okay
[867] I already told you this is often the
[869] case
[870] um and then you can add many things to
[872] it actually and stay X time complete so
[874] not increase the worst case complexity
[876] so for instance if you add these
[877] inverses which is a very natural
[879] construct to have then you stay X time
[881] complete okay now let's consider what
[884] happens with e so e is a very
[887] interesting description logic it's very
[889] simple as you can see here yeah
[891] basically we have conjunction
[892] existential and that's just about it
[894] okay why is it interesting well earlier
[897] on I discussed this big Medical and bi
[900] uh biology ontologies turns out that for
[903] most of them this is what you need what
[906] about no they don't really use that so
[909] much no why
[911] biolog I'm just saying that this does
[914] most what you need there's actually some
[916] weak forms of negation you can add to
[917] this to do disjoint classes that you can
[919] add without so simple forms of negation
[921] the form of D joyness you can add and it
[923] doesn't change to complexi this is okay
[925] so you need to often go slightly Beyond
[926] this logic to express those ontologies
[929] but still we are polinomial time so this
[932] is very good because those really huge
[934] ontologies um they're they're really big
[936] right so if we used a very complex logic
[938] it would be very hard to do okay so what
[941] happens now if I take well it was
[944] natural to add inverse roles here what
[946] happens if I had inverse roles to this
[947] very weak thing boom we're at X time
[951] complete I mean that's really surprising
[954] right it doesn't look particularly
[956] dangerous I don't have negation I don't
[959] have disjunction I mean and nonetheless
[962] I move up to X complete which shows you
[963] that I mean this work of mapping the
[965] landscape is actually it's non-trivial I
[969] mean the results are not always obvious
[971] and it's important for practitioners to
[973] know that when they move from this to
[975] that they have this huge jump in
[977] complexity and so what they can expect
[979] in terms of times for computing for
[981] instance the hierarchy of classes is
[983] completely different and that's
[985] important to
[986] know okay so uh this is my second to
[990] last slide so just to give you a really
[993] high level idea of what these reasoning
[995] algorithms look like okay so first up if
[999] we look at these expressive DLS so
[1001] things like ALC or Beyond
[1005] okay then the idea would be say if we
[1008] want to determine whether this
[1009] subsumption holds we're going to try to
[1013] build a counter model by which I mean a
[1016] model that satisfies everything in t in
[1018] the T box
[1020] and such that I have an individual which
[1022] is C and it's not D so what I'm going to
[1025] do is I'm basically going to say okay
[1027] suppose I have this guy here who's C and
[1029] not D and then I'm going to say well
[1031] because the tbox says that well C
[1033] implies blah so I'm going to have to add
[1035] that and the tbox says that well I'm uh
[1038] either an e or an F so I'll add e or F
[1041] and I will try out that's a bit of the
[1043] what makes it difficult I will actually
[1044] have to do case based reasoning I'll
[1046] have to say well if I were an e then
[1048] blah blah blah blah BL blah if I were an
[1050] F then blah blah blah blah blah and I
[1052] have to see whether in the end I'm able
[1054] to build a counter model or
[1056] representation of a counter model is
[1059] it yes exactly here yeah yeah so this is
[1062] a very classical technique which is used
[1064] for many Logics and this is the
[1066] underpinnings of
[1068] most uh most of the reasoners for
[1070] expressive DLS now if you just take the
[1072] standard Tau method and you implement it
[1074] doesn't work so people spend a lot of
[1077] time working on very clever
[1078] optimizations
[1080] that allow them to actually make this
[1081] work on reasonably size ontology so
[1084] hundreds or a couple thousand axum okay
[1088] um and this is kind of the the the state
[1091] of the art and it it allows people
[1092] already to do useful reasoning okay now
[1096] another method that's very uh become
[1098] very popular this is kind of a very CL
[1102] the basic idea is very similar to
[1104] classical rule-based reasoning so the
[1106] idea is that if we're in a logic that
[1108] doesn't have any disjunctions then we're
[1111] going to apply our AXS as rules
[1113] essentially and just kind of see all the
[1114] things that we can deduce okay we're
[1116] just going to deduce more and more
[1118] things and then we're going to check
[1121] whether the thing we were looking for we
[1122] derive it
[1125] okay um what makes this slightly more
[1128] complicated is that we have this
[1130] existential quantifier so if I apply a
[1132] rule say if I say that an animal has a
[1135] parent who's an animal and if I keep
[1137] applying this I could get kind of Cycles
[1138] so you have be a little bit careful to
[1140] make sure that this forward chaining
[1142] halts but in the end you are able
[1144] because there's no disjunction here to
[1146] kind of just build a larger and larger
[1149] set of consequences okay and then to
[1151] check whether the thing you want is
[1152] there and this is very helpful because
[1155] we could take for instance that huge
[1157] medical antology snow Med so that had
[1159] like 400,000 terms in it and even more
[1161] axioms and you can classify it so find
[1164] all the relationships between the atomic
[1165] Concepts in a few seconds okay by using
[1168] this type of idea
[1169] okay so the idea is fairly simple
[1171] although you do have to do more than
[1173] just what is done with uh with
[1176] traditional algorithms for for for rules
[1179] to deal with this type of
[1180] quantifications there are still some
[1181] things that have to be done to make it
[1183] work it's not completely trivial but the
[1185] underlying idea is fairly
[1186] straightforward okay and then a last one
[1189] that is actually quite important and
[1190] unfortunately I didn't have a lot of
[1192] time to cover it today is that um okay
[1195] so I said that nowadays people are
[1197] really interested in these more Advan
[1199] forms of querying like with these
[1200] conjunctive queries okay and the problem
[1204] is is that they're actually quite
[1205] difficult to answer and so if we want to
[1207] have you know kind of database level
[1209] performance we need to work with simple
[1213] very simple uh ontologies and we also as
[1216] much as possible we like to exploit
[1218] existing database tools okay and so
[1221] people came up with this uh another
[1223] family of lightweight description Logics
[1225] called
[1226] dlite and what was nice about this
[1229] Logics is that we can take our
[1230] conjunctive query and we can kind of and
[1233] then we look at our T box to the axioms
[1235] and we think about well how are what are
[1237] all the ways that I could satisfy this
[1240] query um given what I know about the
[1244] axioms okay um and then what I get in
[1247] the end is a new query which typically
[1249] is actually much larger that's a bit of
[1251] an issue in practice and this new query
[1253] it incorporates all of the relevant
[1255] information from the antology but it's a
[1258] database query and now I can just give
[1259] the database query to the database that
[1261] executes it on my a boox as if it were a
[1264] database and it gives me back my answers
[1266] so in a way I manage to reduce the
[1268] reasoning task of query answering where
[1270] I have to consider what happens in many
[1271] different models to the evaluation
[1274] problem of checking whether something
[1275] holds in the particular interpretation
[1278] corresponding to my set of facts and a
[1280] very simple example unfortunately I
[1282] didn't have space to put something a
[1284] little bit more interesting is that if I
[1287] have for instance I want to find all the
[1288] prime a
[1289] okay all the primates and in my antology
[1292] I'm going to have things like well a
[1294] gorilla is a primate and a chimpanzee is
[1296] a primate and so on then what I can do
[1299] is I can kind of make a disjunction of
[1301] all the ways of being a primate and then
[1303] I send that to the database and it looks
[1306] and sees well is this thing a gorilla is
[1309] it a treny and so on and it checks and
[1311] the answers to this database query will
[1313] be exactly the answers that I want with
[1315] my semantics when I take the ontology
[1317] and this query okay so it's a way that
[1320] we kind of can uh compile out uh the
[1324] reasoning
[1325] okay okay so to I promised uh that I
[1330] would conclude with some kind of current
[1332] topics in description logic research so
[1335] where is the field going and I think
[1336] this will also answer some of your
[1338] questions um so I mean the first thing
[1340] and here I'll be very quick because it's
[1341] kind of obvious we want things to go
[1343] fast we want this to be usable in
[1345] Practical applications there's really no
[1347] limits to how fast we would like like
[1349] this to go and especially since now we
[1351] want to deal with larger and larger T
[1353] boxes so ontologies larger and larger
[1355] data sets there's a real problem
[1357] scalability so there's a lot of work to
[1359] be done uh of building really efficient
[1362] reasoners Okay so we've come a long way
[1363] but there's certainly a lot more to be
[1365] done
[1367] okay um the other thing is that as I
[1370] mentioned on more than one occasion
[1371] during the talk coming up with these
[1373] ontologies is actually really difficult
[1376] and so we already saw that
[1379] satisfiability testing or this
[1381] classification subsumption these already
[1383] give us some tools to help us figure out
[1386] with what we're building is what we want
[1388] okay but that's not the only thing we
[1390] would like there's actually a lot of new
[1392] reasoning tasks people have come up with
[1395] specifically for the purpose of helping
[1396] people to construct and maintain
[1398] ontologies so the first thing is okay
[1402] your ontology it's
[1404] unsatisfiable it's got hundreds
[1407] thousands hundreds of thousands of
[1409] axioms what do you do right you have no
[1412] idea you have no idea what to fix right
[1414] so some people come up with Services
[1417] where they will find where what are the
[1420] ains that are responsible for causing
[1423] that contradiction or which things are
[1425] causing that unwanted inference so if I
[1427] find that in the class hierarchy things
[1429] are not organized as I want why okay
[1432] that's very important because otherwise
[1433] it's practically impossible for someone
[1434] to know what to face U modularity so the
[1437] idea is that that people SP a lot of
[1439] time say building snow Med what happens
[1441] if in my application I don't need snow
[1444] Med but I need a little piece of snow
[1445] meded okay so I want to reuse parts of
[1448] existing ontologies how do I do it so
[1450] how do I automatically pick out the
[1453] relevant portion of an ontology for my
[1455] application so the idea is say I want to
[1457] I want to say well these are the terms
[1459] in this ontology that are interesting to
[1460] me and then I want to press go and it
[1463] gives me the subset that I need okay so
[1465] there's a lot of work on this and there
[1466] are tools to to do it there are variety
[1468] of ways of expressing what is a module
[1470] what is a yeah oh okay I thought you had
[1473] a question okay so I mean there's of
[1475] course a lot of issues in just defining
[1476] what is a module what makes a good
[1478] module why and so on and then afterwards
[1481] actually Computing it is also very
[1483] difficult
[1485] um a third thing I'm going along I'm
[1488] modifying there's several of us maybe
[1490] working on this big onology I'm making
[1492] some changes and now I want to see what
[1494] are the differences between different
[1495] versions of my ontology just as people
[1498] who write code use versioning tools to
[1500] check what
[1502] changed we would like to have that for
[1504] ontologies the difference is is that
[1506] saying just that we change this is not
[1508] necessarily very useful what you'd like
[1511] to understand is what are the
[1512] differences in the semantics of the two
[1514] what are the difference and the
[1515] inferences between the two so you want
[1516] to give kind of have a semantic
[1518] difference between them two ontologies
[1520] what do they say about the world that is
[1522] different okay and that also requires
[1525] some effort both to Define what you mean
[1527] by that and to computer
[1530] okay and the last thing is that as was
[1534] realized during the talk there are a lot
[1536] of types of knowledge that don't so
[1538] nicely fit into the framework that we've
[1540] outlined here and okay I will mention a
[1544] couple of them but there's really many
[1546] uh many of them and so of course people
[1548] want to know can we extend description
[1551] Logics or can we come up with different
[1553] types of description Logics that will
[1555] allow us to capture these other types of
[1557] knowledge which in some applications
[1559] might be of crucial importance so for
[1562] instance people have introduced fuzzy
[1565] description Logics just like fuzzy logic
[1568] um to cope with Badness because
[1570] sometimes people are not in a class or
[1572] not in a class they're in a class to a
[1574] certain degree okay you can be kind of
[1577] tall you can be very tall okay
[1580] contextual information well what does
[1583] tall even mean even if we agree this to
[1585] a degree am I tall as an elephant or I
[1588] tall as a building so some people try to
[1591] come up with things where I can kind of
[1592] Reason about context within the
[1595] description logic defeasible reasoning
[1598] so I mean obviously both at some point
[1601] in philosophy and also in computer
[1603] science knowledge representation certain
[1604] forms of non-monotonic reasoning have
[1607] generated a huge amount of work because
[1608] lots of Common Sense knowledge that we'
[1610] like to represent doesn't really obey
[1614] the normal rules of logic so Birds
[1616] usually fly but Penguins don't and so
[1619] we'd like that if we have something that
[1620] is a bird we can conclude it at flies
[1622] now we learn as a penguin we don't want
[1624] to conclude it anymore okay so these
[1626] require alternative semantics they've
[1628] been studied a lot for classical logic
[1630] but now how do we put these into uh
[1634] description Logics and of course since
[1636] now we're really concerned about
[1637] actually doing it so a lot of work on
[1639] non monotronic reasoning uh it was yeah
[1643] what can we do with this one what we can
[1644] do with that one but it was not so much
[1646] concerned with computation here we
[1647] actually want to have a syst the Dozen
[1649] so this really gives us kind of new uh
[1651] problems to deal with and uh also
[1654] inconsistency
[1656] tolerance okay so I've given you a lot
[1658] of discussions about debugging
[1660] ontologies and so on but if nowadays uh
[1664] we're going to have data and data can be
[1665] very big data can be very dirty we can't
[1668] necessarily expect that at every time
[1670] point the set of facts is coherent with
[1672] the ontology but does it mean that we
[1674] have to just give up throw up our hands
[1676] and say I can't answer anything no
[1678] because a lot of the information there
[1679] is okay and so you can adopt alternative
[1681] semantics there to be able to give back
[1683] meaningful answers despite the fact that
[1685] you do have some contradictions okay so
[1689] that gives you just a little bit of idea
[1690] of where the field is going and as you
[1691] can see that it brings out a lot of
[1695] classical issues in logics in knowledge
[1697] representation and also in computation
[1699] because we really have a lot of problems
[1701] to develop really good algorithms uh to
[1703] do this okay there you go
[1707] [Applause]
