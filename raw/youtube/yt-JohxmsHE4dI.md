---
schema_version: 1
id: yt-JohxmsHE4dI
type: youtube
title: Designing and Building Enterprise Knowledge Graphs from Relational Databases
  in the Real World
url: https://www.youtube.com/watch?v=JohxmsHE4dI
authors:
- Columbia SPS
ingested_at: '2026-06-18T01:38:22Z'
content_hash: sha256:dea43190451f2b6a58d04a8621f4a27a9340d8907366e3495570024f58e4441b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Columbia SPS
  channel_url: https://www.youtube.com/@ColumbiaSPS
  duration_seconds: 1160
  caption_track: cached
  snippet_count: 573
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:22Z'
  user_correction: null
---
[2] an enterprise database so if you opened
[5] this up what do you see well it's
[7] supposed to see a very ugly relational
[9] schema right
[10] thousands of tables tens of thousands of
[12] an attribute so you have too many tables
[14] into many attributes it's impossible to
[16] understand the names so this is an
[19] ecommerce database you have you're
[20] talking about orders
[21] there's not one table called orders it's
[23] probably 10 or 15 complex relationships
[26] people just want to know I want to know
[27] the orders are the customers and the
[29] products very simple relationships that
[31] involves a very complicated sequel query
[33] with a bunch of joins the data elements
[35] do not correspond to the way the
[37] business people think about things right
[39] even if you like you're an sa p the
[41] names are in German then the data
[43] experts are not available
[44] master data sometimes off limits you get
[47] a spreadsheet and CSV file people are
[49] starting to use these data prep tools
[51] they're great but they start generating
[53] these silos of quote unquote clean data
[55] and then everybody starts to finding
[57] what a large order is somebody said it
[59] was 15 order somebody said was 20 orders
[61] and we start getting this difference and
[63] then databases have a bunch of quality
[66] issues of Knolls of duplicates how do we
[68] fix this stuff so what if you could see
[68] Knowledge Graph
[71] again this doesn't look as beautiful as
[73] I wanted me but if you could just
[74] visualize your data and this very
[76] beautiful way of how the business users
[79] think about it which is what we draw on
[81] the whiteboard bubbles and lines between
[83] them and that really is what we're
[84] calling the knowledge graph it's just
[86] this way of modeling data as a graph and
[88] we want to be able to connect us to that
[89] inscrutable data sources that we have
[91] and that's what I'm gonna be talking
[92] about for the next 18 minutes here how
[95] do we do this in the real world so who
[97] are we cap sentences span out from the
[99] University of Texas at Austin that's
[101] where I did my PhD I've been over for a
[102] decade trying to understand the
[103] relationship between relational
[105] databases and Semantic Web graph
[107] technologies understand how do we put
[109] these two things together and when we've
[110] developed this our mapping technology
[113] our real-time virtualization semantic
[116] data virtualization technology which was
[118] spun out into camps until like five
[119] years ago so we've been really working
[122] on this problem for over a decade so in
[125] case you have to leave in the next
[126] minute this is what I want you to take
[127] away
[128] you got domain experts who want to be
[130] able to ask business questions and you
[132] want to generate reports and go get beta
[133] and do
[134] ai machine-learning whatever but you
[136] have all this bunch of different data
[137] sources and there's this gigantic
[139] conceptualization camp and the question
[142] is or my of course is how do we bridge
[145] this conceptualization gap because if we
[147] don't it's garbage in and garbage out
[148] which people have already mentioned so
[150] how do we bridge this conceptualization
[151] gap so as you can imagine the answer
[153] would I my answer is oh we use a
[154] knowledge graph but the longer answer is
[157] that there's three things only to take
[158] away
[159] we need a knowledge engineer we need
[161] methodologies and we need tools where we
[163] need to understand the relationship
[165] between humans and machines in the loop
[167] so now you can leave if you leave but
[170] but knowledge graph is this big thing
[170] Let's put Historyin Today's Context
[172] and I'm really happy I saw peers talk
[174] about the history and I'm a big fan of
[175] history we talk about knowledge and data
[178] and things have been going on for
[180] decades and decades knowledge graph is a
[182] term that Google posted in a marketing
[185] blog seven years ago but the history
[188] goes all the way back to semantic
[190] networks and network databases go figure
[192] graphs back in the sand back in the 60s
[194] and there's been all this bunch of
[196] events that have occurred over the last
[198] 60 years raise your hand if you ever
[200] heard about the Japanese fifth
[201] generation project okay
[203] those who have it go look at the
[204] Wikipedia page you're gonna see that
[206] we're kind of reinventing the wheel in
[208] the new context and the new systems that
[210] we have today I mean this is just a
[211] quick laundry list of things that are
[213] going on if you're interested take a
[215] look at this knowledge graph today we're
[217] organizing a tutorial on the history of
[219] knowledge graphs it goes back for 50
[221] years so we've been also hearing a lot
[224] about right
[225] we had the goal is to be able to create
[227] this knowledge graph and extract the
[229] knowledge graph from different data
[230] sources and we have data coming from
[232] unstructured all the way to structure
[233] we've been hearing a lot today about the
[235] unstructured stuff not everybody is a
[238] Google Airbnb in the world in the world
[241] and our focus is the structured part so
[244] really well if I start from with just
[246] one relational database understanding
[248] one relational database is already a
[249] hard problem so I admire people who are
[252] working things on text and stuff that's
[253] a really complicated problem I want to
[255] focus on something that's even but I
[257] think it's still simpler to do but it's
[259] still very hard so we're focusing on the
[261] structured part and if we look at the
[264] chasm stuff we're really very early on
[266] we're still in the innovators face
[267] and we've been working out this from a
[269] research perspective for over ten years
[271] and now the last four or five years
[273] trying to commercialize this as I said I
[274] carry two hats
[275] I carry my academic scientific hat but
[277] also my engineering business head on and
[280] I've been looking to this chasm for the
[282] last almost a decade I want to share
[283] with you what I've been observing in
[284] this castle observation number one
[284] Ad-Hoc
[287] there's a lot of ad hoc things that
[289] people are doing
[289] people say oh here's a database and I
[292] can just ad hoc write code and generate
[294] a graph and stick in a graph database
[296] okay what's really in here do you how
[299] many times you like actual people are
[301] thinking like what's my schema have no
[302] idea how do i Cris why is this slow what
[305] if the person who wrote that scripts got
[307] run by a bus god forbid
[309] who's gonna maintain that stuff this
[311] happens right now all the time then if
[314] you go look at the look at the semantics
[316] aware folks right people who've been
[318] doing the RDF stuff in ontology and
[318] Semantic Aware
[320] things you have it on toad is creating
[322] creating ontology and then there's a
[325] bunch of stuff that occurs that
[327] traditional IT folks who know sequel
[330] databases have no freaking idea what's
[332] going on who's gonna put this engine in
[334] production and and and think the
[337] complaint is that you need to hire
[338] people with PhDs as Semantic Web to
[340] maintain this this is not a scalable
[341] solution it's observation number three
[345] we're boiling the ocean
[345] Boiling the Ocean
[347] people are going on and thinking we need
[348] a go and engineer the ontology of
[350] everything and we're to spend six months
[352] and I know the dollars typical typically
[354] how you do your enterprise data
[355] warehouses right you go higher and
[357] Accenture forgive I know they're here
[358] but you go six months in a million
[360] dollars to create a bridge to their
[361] warehouse what and then you say there's
[364] all these techniques about how to create
[365] ontology and then we say well I've
[366] created my ontology I got my database
[368] schemas let's go map them we can use
[370] machine learning to put these two things
[372] together that stuff doesn't work in real
[373] life in theory and the academia looks
[377] nice because we're matching this one
[378] thing to one thing over here but in
[380] reality and enterprise complex systems
[383] they don't because these database
[386] schemas are so hard how many people in
[386] Real World Schemas are Hard
[390] an organization understand these
[391] database schemas Oracle EBS has 25,000
[396] tables which attributes called segments
[398] one segment two segments
[400] so when you're trying to say that we
[402] want to automate these things it's
[403] incredibly hard
[404] why because not even the humans will
[406] agree so let's assume I have this really
[408] short schema here let's make the big
[411] assumption that there's a table called
[413] order and every single instance of that
[414] table order represents what a concept
[417] order is and let's assume that there's a
[419] table called date and the table called
[421] an oxygen called date and currency
[422] these are simple one-to-one mappings
[424] okay but you have to know that four and
[427] five mean four and five means inactive
[430] and one two three means active that's
[433] written down somewhere right maybe it's
[435] in the database maybe it sends out
[436] documentation but in let's talk about
[439] the e-commerce pace the concept or the
[442] attribute of a net sales financially
[444] where's the net sales it's a gross - the
[446] taxes - the discounts you think in your
[449] source database is it attribute called
[450] net sales or something as simple as the
[453] gross in the Texas no you got to go
[455] figure this out you have to know that in
[457] this company our customer type a always
[459] gets a 5% discount and the shipping cost
[461] in Canada and the u.s. always have taxes
[463] and other you got to put this in so I
[466] was the capital one folks we're talking
[468] about the mappings this is our day to
[470] day I have no idea how we're ever gonna
[473] automate this stuff and what we really
[474] need to do is to have methodologies
[476] we'll talk about in a second how are we
[478] gonna do with moles and duplicates
[478] Chasm Observation 5: Real World Mappings are Hard
[480] sometimes you see that there's Knowles
[482] oh the null means one but there's a one
[486] value - why is there a No I don't know
[487] it's just the way the system was
[489] designed so if you don't make those
[491] changes and you do some aggregation that
[493] you're missing a bunch of data or why
[495] for some reason does a customer have
[496] multiple birth dates it's and and the
[499] relational database is consistent with
[501] respect to its constraints it's just how
[502] things are modelled right social problem
[507] knowledge hoarding the capital our
[507] Knowledge Hoarding
[510] ladies were saying this morning people
[511] don't want to share their knowledge
[513] right people have popular knowledge is
[515] power control job security and makes
[517] them feel very important everybody comes
[519] to them right and you come in here say
[521] how we're going to democratize our human
[523] and humanize your data well they feel
[526] threatened so how do we overcome this
[528] and how do we create the schemas I know
[532] graphs are all about
[534] laughs we can go do this quickly but
[534] How to design Graph Schemas?
[535] once you get into getting into
[537] enterprise data you realize that we need
[538] schemas and there are no good graph
[540] modeling schema tools out there so how
[540] How do we bridge the Chasm?
[544] do we bridge this chasm two aspects the
[548] social one is what I'm calling the
[550] knowledge engineer and we need
[552] methodologies and from the technical
[554] point of view we need modeling and
[555] mapping tools and there is this balance
[557] that we need to understand which i think
[559] is an open question from a scientific
[561] perspective and also in the industry is
[562] that we need to understand the balance
[564] between humans and machines we are in
[566] this expectation now the machine
[568] learning AI world that we want to
[569] automate everything but I think we have
[571] to be very careful and I don't know if
[572] we can't automate everything or do we
[574] even want to automate everything and
[576] make sure how much it control is a human
[578] is a human in control
[579] so let's resurrect the knowledge
[582] engineer I already seems a couple of
[582] The Resurrection of the knowledge Engineer!
[583] slides with the term who is the
[585] knowledge engineer it's somebody in the
[587] middle between the business user and the
[588] IT somebody from a hard skill
[590] perspective knows how to an Alexis de
[593] daño Seco no scripting and they know how
[595] business modeling they have to know how
[596] to draw a conceptual graphs and so forth
[599] from a soft skill perspective they're
[601] geeks with geeks and they're people
[602] person with with the business users so
[604] they're really people who work with both
[606] sides of their brain and actually when
[608] organization people we find the best
[610] knowledge engineers or people who have a
[612] background in computer science and have
[615] dual degrees in English and philosophy
[617] or musicians again this is not a term
[620] I'm inventing right this goes back to
[621] the early days in the 70s I mean the
[625] Donald Michie form Edinboro I think is
[627] the first time I see the terminology
[628] engineering going around
[629] history sorry so and I'm not here alone
[633] this is a bunch of this is a Google job
[635] post this is I think this was Thomson
[637] Reuters this is MasterCard this is
[639] Amazon this is done in Bradstreet but if
[642] you look at what they're looking for and
[643] these are kind of experts from their
[645] from their job postings you can see
[647] they're looking people who can analyze
[648] graph structures who know ontology so no
[650] spark or no data massaging but they can
[653] work with linguists they can work the
[654] win the fight they know have knowledge
[655] of the financial industry they can
[657] translate to business use of
[659] requirements they have communication
[660] skills so this is the new type of role
[663] that we're seeing and you may be asking
[665] is
[666] how is this different from the data
[666] Knowledge Engineer vs Data Scientist
[668] scientist and I saw in some slides
[670] knowledge engineer slash data scientist
[672] they are not the same person you always
[674] hear this complaint that 80% of the time
[676] that they decide to spend on on
[677] organizing clean the data that is true
[679] and this is not what the data scientists
[681] should do and I'm not talking about
[683] cleaning the data oh there's a space or
[685] an apostrophe here no it's really
[687] understanding the semantic relationship
[689] between this concept that the business
[691] users are talking about and the where
[693] the data is and then once you have that
[694] understanding go give the data to the
[696] data scientist it's clean beautiful day
[698] let them run with it to methodologies
[703] this is something that was never in my
[706] life by tamas networking methodologies
[708] I'm a core computer scientist I do
[711] theory I do systems never I thought is
[713] gonna methodologies but I realized going
[715] off into the real world trying to figure
[716] out what people and trying to address
[717] this knowledge hoarding problem is that
[719] we have to have a process to do this
[722] so nothing methodology if you go back to
[726] the 80s and why expert systems kind of
[727] failed is because there was a lack of
[728] methodologies it's a little big work in
[730] the 90s so we're building upon this work
[732] so to avoid boil in the ocean what we
[735] want to do is to focus on building on
[737] the business questions so traditionally
[740] what we always see is that people say oh
[742] we need to integrate data here's all my
[744] databases go into great data and we
[745] bring in an Accenture or or whatever
[748] right and go build an enterprise data
[750] warehouse but in reality built
[752] integrating your data as a means to an
[753] end because your goal is to answer
[755] business questions so tom was presenting
[757] this morning again how they were
[758] focusing on business questions so we
[761] have two processes steps the knowledge
[762] capture phase the first thing is you
[764] want to understand the business question
[764] (2) Methodology for the knowledge Engineer
[765] and we want to be able to really
[769] understand where this where the context
[771] of where things come from so really go
[773] through a very basic who what where when
[775] why type of thing understand what these
[776] questions are and we really tried to
[778] prioritize the physics questions and
[780] literally start from question number one
[782] and at this point is when you understand
[783] oh there is three there's three
[786] different words that mean the same thing
[788] or we use the same word that means three
[790] different things and we're trying this
[792] is at the business level talking about
[793] we're not even looking at the data after
[795] that we start saying okay where is it in
[797] the data we start collecting a
[800] of existing procedures of scripts so I
[804] see this all the time
[805] 1015 pages of one sequel query that runs
[808] a report do you know what goes on in
[811] that sequel query how many people
[813] understand it it runs it runs in ten
[815] minutes and it generates the reports
[817] that people are making billion dollar
[818] decisions on so there's a lot of
[822] interesting knowledge that you can
[823] extract so let's extract all the
[823] Knowledge Capture
[825] existing documentation out there and
[827] then we want to be able to see where
[829] this is in the data and we realize look
[831] I don't need five databases to model
[833] this question I only need one database I
[835] need a thousand tables I need two tables
[837] and we start trying to organize these
[840] mappings that we've really defined
[842] almost like a spreadsheet of how did how
[844] to represent all this information in
[845] there once we have that we can go in and
[848] say okay now we understand this we can't
[850] we have basically meetings to make sure
[852] that we are on the same page and let's
[853] go implement this and now you can go
[853] Knowledge Implementation and Tools
[855] implement your your-your-your schema and
[858] in when the RDF graph worlds you have
[861] all the schemas property graph schemas
[863] that we're working on
[864] there's declarative mapping language out
[866] there for the in the RDF world then you
[869] want to be able to generate your data
[870] you know the virtual way and you know in
[873] a material way and then you now have
[875] data to answer that question next
[877] question comes along can I answer it
[879] with the same data that I have with the
[881] model that I have all right you're done
[883] I can't what's missing okay maybe it's
[886] one concept maybe there's one attribute
[887] and you extend it in an iterative way
[889] you extend that one thing you go look
[890] for the mapping there's a very small
[892] thing and you keep iterating as in
[894] little by little pay-as-you-go model to
[896] this and the great thing is that you are
[898] really compartmentalize in the concepts
[900] and were the connections to the
[901] different data sources and you are not
[903] boiling the ocean 3 we need better tools
[907] and what we did at Cap centa a couple
[907] Tools for the knowledge Engineer
[910] years ago as I said you know what we
[912] there's fantastic academic really strong
[916] tools to create ontology
[918] there's nothing out there for just
[919] general purpose graphs things I can't
[921] put from the business users so we took
[923] like a half a dozen of our engineers and
[925] for two and a half years we spent and we
[928] designed graphing so you can check it
[930] out
[930] GRA dot fo imagine it's a it's a graph
[933] tool combined with the Google Docs it's
[936] a visual collaborative real-time
[937] ontology knowledge graph tool and
[941] actually this week we announce that
[943] we're supporting now neo4j for their
[945] Morpheus project for which is a cipher
[947] of Apache spark we're supporting Tiger
[949] graph we're supporting Jenni's graph we
[952] have now we can export documentation
[954] coming soon we'll have an API a bunch of
[957] other stuff so I'd love to show you
[958] demos I'm gonna be here today and
[959] tomorrow so graph oh so we really want
[962] to have a tool where business users can
[964] go in eliminate the whiteboarding aspect
[968] so where do we put how do we bridge this
[968] Bridging the Chasm
[972] chasm I believe that two bridges chasm
[974] we need the knowledge engineer and we
[976] need to empower the knowledge engineer
[977] with tools and methodologies before I
[980] wrap up this has been work for over a
[983] decade of my academic side on the
[985] business engineering side so many people
[988] I can't think but now to wrap up I
[990] started with this question 20 minutes
[990] Takeaway Message How do we bridge the conceptualization gap between the domain
[992] ago how do we bridge the
[993] conceptualization gap between the domain
[995] experts in the data we need knowledge
[998] graphs we need knowledge engineers the
[1001] knowledge engineers need to be empowered
[1002] with methodologies we need to focus on
[1004] the business question so we do not boil
[1006] the ocean and we need to empower the
[1009] knowledge engineers with tools and we
[1011] need to understand this balance between
[1013] the human and the machine in the loop
[1015] with that thank you very much
[1025] I got three minutes for questions thank
[1029] you yeah I see I see well how come did
[1033] you switch to the dark side of the
[1035] property graph force this is a great
[1039] question and I think so I'm I'm of
[1042] course I'm moderating the vendor panel
[1044] tomorrow and and I think right I I had
[1047] some quick you that question because I
[1049] had a question about someone telling me
[1051] well one is running the the vendor round
[1053] table but is not impartial they're
[1056] decided right no this is here's that
[1059] here's the thing this is a great
[1061] community and the community out to now
[1064] there's been some sort of division and
[1066] this sort of division between RDF and
[1068] property graph it doesn't serve anybody
[1069] I think we need a unite right so still
[1079] one or two questions
[1089] thanks a lot for great presentations
[1091] just picking up on the conversation we
[1094] began at the break any quick version of
[1097] you can share with us on testing
[1100] methodology so posed design yes so one
[1105] of the things that we want that we that
[1107] were working in is at least in the RDF
[1109] space there's a standard called shackle
[1111] which is a shape constraint language
[1113] it's a constraint language so what you
[1115] really want to be able to do is when
[1116] you're defining your your-your-your
[1118] schema you can define these constraints
[1120] which in reality will receive people are
[1122] really interested on cardinalities and
[1124] then you can when you're when you're
[1126] when you're through your pipeline of
[1128] your data let it be an ETL or a
[1129] virtually no ETL you can run these
[1131] checks and then you can see how things
[1133] are going
[1133] in the in the virtual aspect what's
[1136] really interesting is that I do my
[1137] mapping
[1138] everything looks great six months later
[1140] somebody complains data is coming out
[1142] wrong so what did the software
[1144] breakthrough the mapping break I don't
[1146] think so the way you realize is that
[1147] there was a problem in the data that
[1149] some that there was an update on the
[1150] software that fields and data so what
[1152] we've really had we started to identify
[1153] is a bunch of data quality issues all
[1155] the way back to the systems that are
[1157] writing into the original source
[1159] databases that's an example but we can
[1160] talk more about this offline
