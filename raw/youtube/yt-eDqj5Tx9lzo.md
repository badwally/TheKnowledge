---
schema_version: 1
id: yt-eDqj5Tx9lzo
type: youtube
title: NODES 2024 - Leveraging Semantic Networks for Data Integration at Deutsche
  Bahn
url: https://www.youtube.com/watch?v=eDqj5Tx9lzo
authors:
- Neo4j
ingested_at: '2026-06-17T20:57:10Z'
content_hash: sha256:822d3b1d2e51eb8446046df454626ed45f732ef5badba25bced111077756680f
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Neo4j
  channel_url: https://www.youtube.com/@neo4j
  duration_seconds: 1313
  caption_track: fetched
  snippet_count: 428
filter:
  score: 0.7
---
[9] well thanks a lot
[11] Damian yes Welcome to our little talk on
[14] leveraging semantic
[16] networks at deutche
[18] ban first you might ask what is deche
[23] Ban we are one of the world's leading
[26] mobility and logistic companies the
[29] people over here in Germany might know
[31] us as the train company even though we
[34] are active in different countries and
[36] outside Germany within deutan there is a
[40] company DB zusto and we are basically
[44] the driver of digitalization for all DB
[46] group companies you can think of us as
[50] the IT department of Deutsche bar and
[54] again within dbst you find the team
[58] infragraph Analytics we've been working
[62] on data
[63] integration since March of last year we
[66] are 10 members and I joined the team
[69] around March of last year before that I
[72] was a consultant and freelance
[76] freelancer working mostly in the
[78] internet and web field for about 25
[81] years and I've been working for about 10
[84] years with graph databases and that is
[86] one of the reasons why I came to the VIS
[89] sister so it's it's all about trains
[92] really let's have a very short look at
[95] the history of rail operations in
[98] Germany it all started basically about
[102] 200 years ago with a little train called
[104] adla going from nberg to fur this is
[108] pictured down here in the left and since
[111] then quite a lot has changed the trains
[114] have changed they have become more
[116] modern and up here you see something
[119] similar to the current design of our
[121] trains and not only have the trains and
[125] the infrastructure meaning the railroads
[128] and the network changed also the ways in
[131] which we manage those systems for our
[133] customers have
[135] changed with the introdu introduction of
[138] computers and databases of course lots
[140] of systems have been built within
[144] deutan which made things much more easy
[147] but it also brought one problem with
[150] with it we have many systems talking
[153] about the same
[156] things I just get the information that
[160] you actually can't see our presentation
[162] is that
[167] correct
[174] Damian that's
[178] unfortunate okay
[181] um thanks a lot um I got the um
[184] information from the audience
[189] um okay so sorry about that little
[192] glitch here now you see again the
[194] pictures and how things have changed and
[197] you probably also heard that
[200] um that computer system database systems
[204] um have been introduced within the last
[207] decades and that brought one problem
[211] with them that is that we have many
[213] systems talking about the same thing so
[216] think about a rail road Network we have
[219] signals we have train tracks we have
[222] switches which is like an intersection
[226] in the road where you can either go
[227] straight on or take a
[229] turn and while there is one
[232] object in reality a physical object like
[237] the signal the switch out there we have
[240] have many database systems talking about
[242] it and those database
[245] systems have different aspects of the
[249] information that would be relevant to
[251] that object for example the financial
[254] data or technical data there are many
[257] systems and you probably might know that
[261] from your um organization as well these
[264] are the things that happen over time but
[267] what do we want as a user as a a data
[272] analyst as a consumer of
[275] data we want to have one integrated data
[279] object which really contains all aspects
[282] of the object you don't really want to
[285] you don't really care where the data is
[288] from you're interested in the electronic
[291] equivalent of the one physical object
[293] out there that you're interested in at
[295] that point in time and for us within our
[299] team the key to achieve this is using an
[303] ontology that connects all the data
[305] objects in the
[307] databases and that
[310] translates the meaning and The Meta
[313] description of those objects which also
[316] translates the relations
[319] between those
[323] objects now let's have a slightly
[327] different look at that and I also notice
[329] that my my camera is not working anymore
[334] and here I am again hello for those um
[337] who haven't seen
[343] me so this is our approach that is
[346] basically what I've been talking on on
[348] the last slide imagine we have one
[350] object out there a railroad switch and
[353] there are many different aspects of
[356] information across in this picture six
[359] databases and those six databases can be
[361] connected in one way or the
[363] other what we end with once we have
[366] integrated things is the object on the
[370] right side there you'll find all the
[373] information that was scattered um around
[377] the databases connected to this one new
[382] integrated data object and you find that
[384] some pieces of information like B and C
[387] are there two times why because it was
[389] in
[390] they're in the databases two times for
[394] us that's a great thing because it means
[396] if the same property let's say the year
[399] in which a switch was built is the same
[402] in two databases it's quite a
[404] confirmation that that information is
[406] correct so if both say it was built in
[409] the year 2000 that's great so we have
[413] those in examples of confirmed
[416] information in there and that gives us a
[418] clean complete and Trust worthy object
[422] however the system can also or the
[424] situation can also be quite
[427] different in here you actually find that
[430] we have different versions for B let's
[433] say the year is 2000 in one database in
[436] 2001 in another database after
[439] integration we will find those
[442] Divergent values on the integrated
[445] object and that alerts us and we can
[448] pass on that information to experts that
[451] then in return can address the problem
[454] at the source and try to see where the
[458] problem originated
[460] from now this is all a little bit
[463] abstract let's get a bit risky and try
[467] something let's try a life
[470] demo this will tell you two things it
[474] will tell you a bit more about our
[476] integration approach and it also will
[479] show you our GUI that we have developed
[482] and this is pretty much work in progress
[484] so you get a glimp into a a glimpse into
[487] our workshop and the GUI is at at Alpha
[491] level however we are quite happy to
[494] already use it internally and you
[497] probably will will see why so let's go
[501] on with it but be please be patient
[503] things might go wrong because well it's
[505] a liveo what could possibly go wrong
[515] this is the user
[517] interface of our GUI we've connected to
[520] a local neo4j instance and we've
[523] selected a database that contains our
[526] sample
[527] data I can enter a cipher
[533] query and I get a result in the table
[537] now if you've been using other tools
[540] like the neo4j browser you already might
[542] notice a difference and that is that the
[546] objects Like A and B are here as a
[550] little link and if I hover over it I can
[554] get a
[555] preview into that object which happens
[557] to be a note here which has the ID 52
[562] which has a position middle I come to it
[565] what that means it has a name space and
[568] that holds true for all the object
[569] object might it be a
[572] note or might it be a
[578] relationship of course a table is not
[580] all and
[582] everything we
[584] might want to see those objects as a
[592] graph having a graph like that means
[595] usually at least for us that we start to
[598] drag objects around
[600] it is a bit easier if you use a false
[603] director graph you already get the idea
[606] hm that maybe those are two data setes
[610] of sorts that are separated but for us
[613] it still means lots of dragging around
[619] things and so we introduced a new
[622] feature which we
[626] call
[627] perspectives perspectives allows us to
[630] arrange notes store their positions
[633] store which relations are
[637] involved and restore them so that we
[640] then can start working on them and this
[642] is what we see
[644] here this is a very
[648] very um abstracted version of the German
[653] Railway Network we can go from Munich in
[656] the South to hurg in the north and as
[659] there's the switch we pass we could also
[661] turn and take a a ride and end up in
[667] Berlin we find two data sets we find a
[671] more Geographic oriented one on the left
[674] side and we find another one on the
[676] right side and I'll come to the one in
[678] the middle in a in a moment we can
[682] inform ourselves again about the notes
[686] we can move the notes around as usual of
[688] course
[690] and now one thing we can do is for
[692] example if we find the the property
[696] position of station
[698] name we can go there and get a
[700] description you find that in the last
[701] row this is the name of a train station
[704] or the position might tell us that it's
[708] the geoposition of something of course
[710] we used a string here not numbers to
[712] make it a bit more easy to understand
[715] and the same holds uh true for the
[717] switch we find that it has a label
[720] switch and we can inform ourselves what
[723] does switch mean and again at the bottom
[725] you find it's a onepoint
[729] switch okay let's have a look over to um
[733] at the data set that is located on the
[736] right there we have pretty much the same
[740] situation only the things are named
[743] differently here it is station number
[746] three the effectively the note that
[749] presents Munich because in that other
[751] data set in that other database they
[754] decided to use stage numbers we can
[757] again ask what is a station number the
[759] number of a station the same holds true
[761] for those other station now what
[765] about the switch in the middle here you
[767] see that we actually have three points
[770] describing a switch the point the
[772] starting point this is where you enter
[774] the switch and you can either go
[776] straight on which is called the chunk or
[778] you can take a turn and then you exit
[780] the switch on the branch taking you
[782] effectively to
[785] Berlin now what we want to end with
[789] that's what we've said is an
[791] integrated situation so this is what we
[794] get in the end when we integrate the
[796] data here we have the geop position and
[798] the station name from the left side we
[801] have the station number coming from the
[803] right
[804] side the same for Berlin and for hurg
[807] now what about the switch
[810] for the switch I change the styling I
[813] can do that up
[816] here and you see that this Noe has
[819] become more
[821] visible this is
[824] an a collection note which basically
[827] contains those three
[830] points and is an aggregation on a level
[833] that allows us to connect that switch
[836] and that switch or integrate it into
[838] this switch
[845] now how is that really possible or
[848] what's behind that let's and let's have
[851] a look at
[855] another perspective in here you again
[858] see that we have a data set on the left
[861] a data set on the right and the
[863] integrated data set on the middle let's
[865] have a
[866] quick peek at the left side I find the
[871] noes a little bit too big and I can also
[875] decrease the font size and I slightly
[878] rearrange things over here to make it a
[880] bit more
[882] visible for example you have down here
[885] Munich which is a main
[888] station it is a main station because it
[891] carries the label main station now
[894] within the same
[896] database we have notes that describe the
[899] label main station this is up here this
[902] is what we call a meta label a meta
[905] label contains information about the
[908] label that can be used in the actual
[910] data so the description that you see
[913] here in the last row main station and
[915] location is what is displayed down here
[920] if you wonder what's happening it's
[922] really showing the same
[925] node now the node down here also had
[928] properties position and station name you
[931] find position and station name here
[934] these are what we call Meta properties
[937] again it carries a
[940] description but it also shows way it can
[943] be used using those relationships so a
[945] position can be used in a switch as well
[947] as in a main station a station name can
[950] only be used in a main
[951] station and you see that those nodes are
[955] connected using a
[957] railroad um
[960] railroad as the relationship type and
[963] this is defined over here we have a meta
[967] relation and The Meta relation again
[969] describes the relationship type and in
[973] here we have a little helper called
[976] restriction which allows us to decide
[979] which labels can be connected to what
[981] other labels using that relationship
[987] Tye now we have the same thing on the
[990] right side it's slightly more
[994] complicated over here but you see that
[998] over here we have the computed switch
[1000] Which con contains those other labels or
[1004] meta
[1005] labels and you find that reflected as
[1008] we've seen before on the instance
[1011] level now the last thing that really is
[1014] missing I'll show you again in another
[1018] perspective this just chose the meta
[1020] level we've just
[1022] seen so you find the description of a
[1026] main station and a switch in the on the
[1029] left side you find the same on the right
[1033] side now we have also a model which
[1037] integrates and translate those
[1039] translates those two things and
[1043] again I can use a different styling and
[1046] here it becomes obvious what the secrets
[1049] are is we can draw connections and say
[1053] an integrated switch up here is the same
[1057] as the switch on the left side as well
[1061] as the computed switch on the right side
[1064] and this is how we know that things are
[1067] equivalent of course we need much more
[1070] technology and we have that technology
[1072] to really then on the actual data level
[1075] integrate things but this is the working
[1077] of the ontology and that's what's behind
[1080] it
[1084] now if you're interested in more details
[1087] about how this integration really works
[1090] and how that grammar Works
[1093] um we can tell you so we have the
[1096] description of the grammar in the
[1098] database itself but I think that's going
[1100] a little bit too far I'd rather show you
[1102] one or two more features um that we have
[1107] in our system one thing which I find
[1110] extremely
[1112] useful is that we can also
[1116] see the the information in in the notes
[1122] and we can edit
[1125] things we can edit the values we can add
[1129] properties we can edit the labels we can
[1132] change that but we cannot only work with
[1136] existing nodes we can also add
[1140] information for example imagine we have
[1144] cologne another city in Germany and we
[1147] want to connect that to that switch we
[1150] can just do it by using Dr and drop and
[1154] you
[1155] see in here that it now has a
[1158] relationship of the type fix me if you
[1161] don't like that we can again change that
[1165] and we get a selection of predefined
[1168] types that might make sense here so I
[1171] use the railroad type and now you see
[1175] how it has um switched over to
[1178] Railroad we can also add other
[1183] objects we can also choose let's say
[1186] that that really a new object should be
[1188] a main station and it has the same color
[1191] we can connect those or as you seen from
[1193] other
[1195] ideas we can easily create new objects
[1198] and their relations at the same
[1203] time one last feature that might be
[1206] interesting
[1208] is that we can change the sizes of
[1213] things which in itself is not incredibly
[1216] smart but it might be interesting for
[1219] you to know that we actually have
[1222] adopted
[1225] the the grass FS that you usually use
[1228] for styling and we've introduced the
[1230] possible to embed python to do those
[1234] kind calculations on the Fly um as we
[1239] please with that I want to come
[1243] to I want to finish the live demo and
[1246] would like to come to a last question
[1249] and that is open- sourcing the guy we
[1253] are already a contributor to open source
[1256] software and you find the GitHub
[1258] repository
[1260] on um up there on the
[1266] right now the big question is because we
[1270] contemplating open sourcing the GUI
[1272] would that go GUI be useful to
[1276] you in your organization could you work
[1279] with it is that something that's
[1280] interesting for you so our honest
[1283] question to you is or request maybe if
[1287] you're interested in this we please
[1289] write our team an email you find the
[1291] email here or contact us during the rest
[1295] of the conference or at any point later
[1297] in time send us an email and we get in
[1300] touch with that I'd like to thank you
[1304] for
[1305] listening and um if you have any
[1308] questions please ask them now thank you
