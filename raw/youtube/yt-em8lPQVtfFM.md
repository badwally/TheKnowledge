---
schema_version: 1
id: yt-em8lPQVtfFM
type: youtube
title: 2018 Computational Neuroscience Workshop - Talk by Dr. James DiCarlo (MIT)
  and Open Discussion
url: https://www.youtube.com/watch?v=em8lPQVtfFM
authors:
- Rutgers Center for Cognitive Science (RuCCS)
ingested_at: '2026-06-01T19:24:38Z'
content_hash: sha256:9d0d6fd1ef755dbd95a8f2ee46fcb4c29e7a1b1567a9f5e272709a9b771bb94a
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: Rutgers Center for Cognitive Science (RuCCS)
  channel_url: https://www.youtube.com/@rutgerscenterforcognitives2635
  duration_seconds: 4944
  caption_track: fetched
  snippet_count: 1884
filter:
  score: 0.7
---
[0] presentation for this session so
[4] professor professor DeCarlo he was his
[10] own presentation basically all right so
[29] I'm gonna try to talk for three five
[31] minutes we have time for discussion so
[33] that makes every the most fun part
[35] I wouldn't think the organizer is a
[37] chance to talk and it's really been
[39] great that Jack gonna meet the set up a
[41] lot of what I would have covered so I'm
[44] going to go a little bigger through
[46] parts of that sorry you just define turn
[48] that back down that back up I like it
[74] [Applause]
[74] [Music]
[83] easier for people to all right so I've
[91] made this big blocking title where kursk
[95] I'm not going to solve that today I
[96] wanted to try to give a minute part of
[99] my octave which is to essentially
[100] introduce an approach to science that I
[103] think is a little different than our
[105] field of you have done but I think it's
[107] going to be a better way forward for
[109] sewing these harder problems and I call
[113] our hearse engineering and what I mean
[115] by that is we need to be able to account
[118] for each ability of the vine which I'm
[120] calling Broadway here intelligence using
[124] I would say components of the brain
[125] which for me means neurons other
[127] connections at least that's the relevant
[129] many of us
[131] we love that's what I'll talk about and
[134] in the language of engineering which
[136] means we need models that can be built
[138] and tested and distributed to others for
[140] building and testing to prepare that is
[143] what I'm calling a very centering
[144] approach another way of putting this is
[146] just through science like engineers and
[149] I'm going to try to show you how we've
[152] tried to do that on a problem that we
[155] work on Quora object recognition and
[157] when I said we I'm mostly an ambassador
[160] for these folks a lot of the names on
[162] the list I'm going to cover work and
[163] I'll try to acknowledge them as they go
[165] along and this is these are the folks
[166] that I'm currently in my lab and
[168] especially without getting game ends
[169] it's both highlights of his work he's
[171] now it's just a professor at Stanford
[174] okay so I'll try to have those folks as
[177] they come up so reverse engineering is a
[180] niche what is that so our version of the
[183] drivers of this goes like that so you
[184] you first have to just define or specify
[188] operational either performance domain of
[191] interest and I'll tell you how we do
[193] that so this is our approach is a bit
[195] more top-down when you look heard from
[197] Jack or Eva so we're starting with a
[199] behavioral goal and we are very much
[201] motivated by where our behaviors where
[204] the system is like humans to better and
[207] current engineered systems this could be
[209] better in the performance sense which
[211] I'll show you but also in the sense of
[212] power size of support so you're
[214] motivated by a phenomenon and it's NGH
[216] and in nature that you're trying to
[217] figure out how does this thing actually
[219] get that done in such a great way then
[222] you try to go inside the system and it's
[226] the measurements that are relevant to
[228] how that system might achieve that
[230] impressive performance and here is an
[234] arms really and choosing wisely what you
[236] try to measure because in the side of
[237] the head have lots of things you could
[239] measure and including things like you
[241] know behavior and as muscle movements in
[243] the head but let's say all the other
[244] things here is spiking read anatomy
[246] blood flow you're on probation you can
[249] do genetics you can think about synapses
[251] and RNA and all that stuff you can do
[253] all that but you have to choose wisely
[256] and I'll show you our choices then this
[258] is a critical step you
[260] to build something that will call models
[262] is what I'll call forward engineering
[264] under the constraints of all the
[266] measurements they've had at least the
[267] ones that you think are relevant to the
[269] system performance this is for loss
[272] means that you need to be able to
[274] capture those measurements and that's
[277] people call that fitting so you should
[279] at least capture but you must do more
[281] than that you must predict held out in
[283] it it's not just curvaceous predict
[285] things outside of what you use to
[287] constrain the building of that line now
[290] here's the neuroscience this means
[291] building models that are called
[293] artificial neural networks because again
[295] those are parts of the brain that were
[297] most interested in here and that's what
[300] that means I'm not happy about those
[302] have probabilities and we talked about
[303] that probably city beautiful building
[305] models but unless you have neurons in
[308] them I can't map them to the brain so
[310] they're not yet useful it often means
[313] that the models must be built at
[315] sufficient scale if they're going to
[316] actually predict things in the brain or
[318] behavior they often these are hard
[321] problems they often have to build scale
[323] vision is a great example
[324] there's a million sensors coming in I
[326] really in dimensional space coming in
[327] you need to be able to build things like
[329] these approximating that space okay then
[332] you just stop there this doesn't just go
[334] one way then you're done you have to go
[336] back again some more measurements use
[338] more modeling and really it's that loop
[340] between measurements colleges the faster
[342] you can make that go then eventually you
[345] get something that I'm going to posit we
[346] will understand me this is a point where
[349] we might debate but that really is
[351] understanding okay we can have that and
[353] I go the understanding of the whole
[354] brain or all of intelligence I mean only
[356] over the domain that I defined here and
[359] specified domain one now we can expand
[361] that going later but this is a recipe
[363] given a domain ok so this really science
[366] usually here measurements discoveries
[369] this is an engineering that is building
[371] but you really need to be doing both of
[372] these things together and MIT this was
[376] represented by and the sacrum brains
[377] minds of machines and more recently the
[379] intelligence quest effort which is
[381] essentially a linkage between science
[382] and you around these kind of issues and
[385] we're not here that you have these
[387] models they're just hoped for
[389] applications they're actually things
[390] that should be able to deliver
[393] form is similar to the one that you were
[395] trying model or understand
[397] here's your near the application okay so
[400] I'm going to show you how we've been
[401] doing this really 15 years around the
[403] problem of human core a visual object
[405] perception that's the domain so here's
[408] how our domain is started we really
[410] would like to understand this broader
[411] domain of visual intelligence
[413] let's take visual scene understanding
[415] that's a very big problem so we focused
[417] on a sub problem called court
[418] recognition which begins with the idea
[420] is you want to label the things out
[422] there as a need to point out other
[424] things you may want to do but for us we
[426] just want to be able to do category and
[427] identity so this is also a problem in
[429] computer vision it kind of looks like
[431] this we can say these are the objects of
[433] the bounding boxes because we're
[435] studying the brain and we know something
[436] about the brain we know it doesn't
[437] process that whole image at high acuity
[439] it processes the central region of high
[442] acuity and the part of the brain the
[443] ventral stream that I will talk about a
[446] focus was on the central 10 degrees
[448] which is kind of approximated here so
[450] we're going to think about 10 degree
[452] window as if you will we also know that
[454] primates that will just fix eight in one
[456] place but they sample that high acuity
[458] sensor they move it around the scene
[460] with saccade and fixations those
[462] fixations last on the order of 200 300
[465] milliseconds and primates and so if you
[468] look again it is the standpoint of the
[469] scene as these different points and that
[471] brings to that mental stream engine a
[475] series of images that look like these
[477] snapshots here I'll show you here in a
[478] minute okay so that's those are the
[481] sample thought of those as a kind of
[482] points will play for you and as you can
[484] see I hope that you can notice that you
[485] can recognize and identify one or more
[488] objects each and every one of those
[489] glimpses even though I kind of pulled it
[491] up a context now you're not trying to
[493] your eyes around you you can still do it
[494] and that ability to do that say 10
[497] degrees in a couple hundred milliseconds
[499] to say there's a what the main
[501] foreground object is that's what we
[503] refer to as core recognition and it's
[505] not the whole problem but we think it's
[506] the core of the bigger problem so that's
[509] why we call it core recognition here's
[510] the parameters I've just given you task
[512] is essentially to report object category
[514] there's other variants to that that
[516] we've done but this is the basic thing I
[518] want you to think about as the behavior
[519] of interest here so this is all the
[521] press
[522] by something why are we in specifying
[524] this but it's actually computationally
[526] very interesting because even though it
[527] seems very easy for you to do that and
[530] that's short amount of time it turns out
[532] to be quite challenging and that
[533] challenges do something that both you
[535] have to meet the mention but it's
[536] essentially the invariance problem the
[538] ability to recognize objects in the face
[540] of variations saying doing the objects
[542] pose relative to you the background or
[544] illumination and so forth so all of that
[546] I'm going to look together as
[547] naturalistic variation that the system
[550] naturally deals with in a very
[552] impressive way okay to test this we kind
[555] of take a middle ground which is instead
[557] of just showing the full national images
[558] we've been generating images that look
[560] like this we generated this because they
[562] were challenging for computer vision
[564] systems now we have control of many of
[566] the latent parameters so these are
[567] rendered objects placed on complex
[569] uncorrelated backgrounds which prevents
[571] cheating from the background yeah you
[573] guys think you can still tell oh that's
[575] a car you know that's a plane this might
[578] look like something from a movie you can
[580] still say that's a face or a head right
[582] and you can do this even in very short
[584] flynch times yeah machines again
[586] struggle with this I'll switch you admit
[587] it here's an example this is how a task
[589] might actually run for both that you in
[591] turn Bucky so you fix take this point
[593] and I'm gonna flash something up and
[594] then you haven't tell me you know which
[596] thing did you see that I don't left or
[598] right right right okay you can tell you
[601] what you're going to see next and then
[603] this is how many or list it will try
[604] what we're justified okay okay so was to
[607] the right now you're great look at that
[609] you're not perfect and we can
[610] parameterize that characterize how good
[612] you are and you've done all that but
[613] here's the big picture I want you to
[615] have a performance the impregnated so
[617] this is like 98% correct this but we're
[620] truly here is that uncertain you that
[622] invariance problem so this isn't they
[623] always told the object rates and a
[624] certain size front facing and so forth
[626] this is whenever you have hydration in
[629] those parameters you can see you're
[630] actually very tolerant invariant but
[633] you're hiding tolerance we're very used
[635] even in the center of ten degrees I'll
[637] get machines this is around 2009 they
[640] were really good in this kind of pattern
[642] recognition mode but hard that's so good
[644] at this generalization or they have to
[646] be able to do this in high variation
[647] conditions and so again here is the gap
[649] that we were especially excited about
[651] with regard
[652] or recognition they can see even in
[654] these clips images system shows its
[656] advantage that's what we wanted to
[658] understand so I'm talking about this
[660] system so that's why I titled my talk
[661] human visual intelligence because I'm
[663] just difficult tests on you I'd show you
[665] some human behavior we really like to
[666] understand our own system that's why we
[668] study animal models but these systems
[672] are hard to get that internal
[673] measurements for so we decided to in my
[677] lab work on this system which is the
[679] reason was monkey system that we can a
[681] state we can get more access to the
[683] internal components now the first
[684] question I asked in look I go here and
[686] I'm going to lose the behavioral
[687] performance and that's one of the
[689] advantages of these Cistus system is you
[690] do not lose lose the pang of performance
[692] this is a rhesus monkey doing the same
[695] casis of an it's home cage of her entire
[697] housing colony and you can see the
[700] animals triggering the screen kind of
[702] like you were when Kristin was a center
[704] to get some flesh targeted in she's
[705] choosing the hon the left and right
[707] targets on the object are all randomly
[709] interleaved so he's not just good to fix
[710] topics but he has a whole set of objects
[712] it has to be able to deal with and green
[714] means is getting it correctly it's a
[715] little juice reward and they love the
[717] new thousands of trials like this all
[719] day long and their commentator so we do
[721] that and here are the results of
[723] comparing humans and monkeys on these
[725] kind of tasks this is that the object
[727] green I'll show you the image green
[729] layer basically each of these colors
[730] indicates the difficulty of is
[732] discriminating so you can intuit that
[734] tanks are often more confused with
[736] trucks that says red dot here and you
[738] can see yellow and blue are sort of the
[740] easier conditions are easier to
[741] discriminate
[742] now the pointer way to say here is
[744] another eyeball you know how guns are
[746] gonna do the tables and so forth and so
[748] on
[748] but to just look at this and say you
[750] know which is the monkey which is the
[751] human and the point is you can't tell we
[754] can't statistically tell and at this
[756] level and even at finer grain these
[758] species are indistinguishable and their
[760] ability to do these contacts okay so we
[762] still have a behavior now we can go back
[764] to go inside and measure the system
[765] coupons okay these are the internals of
[768] the system jack i think they've already
[769] introduced if this is the ventral visual
[770] stream turkeys a bird have told us that
[774] this provides tells us
[776] the architecture of the system is a
[778] series of visual areas of the monkey of
[780] lesions in this part of the brain called
[782] in for temporal cortex that I mean to
[784] mentioned accrues deficits and
[785] recognition tasks we were especially
[787] interested in that when our class
[788] started what we're really interested in
[790] this whole process extreme and you can
[793] think of it as instead of a feed-forward
[794] interconnected important feedback system
[796] shop here we like to lay out these
[799] visual areas and the millions of neurons
[801] in each of them in these kind of
[802] schematic shown here which shows their
[804] forward connections the background
[805] connections in their recurrent
[806] connections in these schematic lines
[808] each dies over who then turned a single
[810] and their round of course to millions of
[812] neurons in each area and what we know a
[814] lot from neurophysiology indicative work
[817] some of which you've heard about already
[818] today but it's much much more than even
[820] Christie did that and tells us things
[822] like hey we have a map of the visual
[824] field at the back of the retina we have
[826] a max all the way up the system itv
[828] actually think of is about three areas
[830] also it's an even presented on so you
[832] can kind of think of this as three
[833] regions here and I'm just showing you
[835] for the purposes of today as one area
[837] but we also know lots about these
[840] neurons some of which I'll show you a
[841] bit later so this is kind of the router
[844] play on the land and then what the idea
[846] is you prevent an image like this one to
[847] the system it activates a photographic
[850] some isomorphic representation on the
[852] back of the retina and it's rapidly
[854] transformed to a new population pattern
[856] of neural activity this even ties here
[858] as in find this way through the system
[860] in about a hundred millisecond lab to
[862] reach IC cortex now I want you to say
[865] here that I'm showing us of a
[866] feed-forward view and I've learned it
[868] some people have decided that the kernel
[870] thinks the whole brain is before it and
[872] I want us to put it back on that say
[874] this is an approximation model to get us
[876] started as you'll see at the end of the
[878] talk where we're going now is kind of
[880] understanding Spivak connections but
[882] you've got to get started somewhere so
[883] we work on that P forward a framework
[885] for nearly a decade and that's the sort
[887] of idea than there you have a new image
[890] you get a new pattern of activities such
[892] as this one shot here and say this is
[894] rapid serial movie kind of like those
[895] snapshots I'll be showing you earlier
[896] but you can again recognize why don't
[898] you each every images your home along
[900] MIT quick so
[902] the new population had a vote at every
[904] image with a lag of about 100 or review
[906] 150 milliseconds and so though the
[909] patterns are not photographs but they're
[911] very very special and I'll show you that
[913] in a minute here's what it looks like
[915] when you record from these neurons of
[917] the month unites the cortex beautiful
[919] actual brain and this is our schematic
[920] these are actually green data this is
[922] just me give you a feel for things
[923] here's four different images shown to a
[925] monkey who's just passively fixating and
[928] then these are the different repetition
[929] shown that throws the Datsun became
[931] spikes this is one Milstein ninth cortex
[933] you see this leg you know whatever this
[935] image has an enterprise this stuff
[937] pretty well and not these cells well
[939] here's another side here's another site
[941] you can see they're all a little bit
[942] different kind of like you saw some
[944] jacket I mean duh and and what I want
[946] you to just take from this is we can
[948] take this data and we can quantify
[949] things and we do it in a very simple way
[951] again simple to get started
[953] and that simple way looks like this you
[955] just count spikes over windows save
[957] about 100 milliseconds adjusted for the
[959] lag of IQ cortex that I already
[960] mentioned and then gives you one an
[962] average number so each imminently for
[964] each ITT neuron we think of as producing
[967] one number to get started that whatever
[969] again here's an example computing those
[971] numbers and that's not all you want to
[973] do but is an addition to get started
[975] okay that's as Jeff mentioned you need a
[978] lot of data it's a constrained model so
[980] that was an example and we scaled up
[983] when you're tall raised I think we were
[984] the first day to plant Pisa Heinz cortex
[986] these are the triple arrays in the high
[987] D cortex so we could really scale up our
[990] data collection this wasn't even found
[993] about six years ago to get money many
[994] many more cells really more images per
[997] cell than we could before I'm using
[999] these kind of chronic methods and when
[1001] you when you think about those neural
[1003] data then we try to build a linking
[1005] model again back to the behavior of how
[1007] those neural data actually driving the
[1009] behavior and this is older work with the
[1011] basic idea is an image of Oaks a
[1013] population pattern that we can record
[1014] when cats pipes in a window like I
[1016] mentioned one and
[1019] in one number for each neuron thousands
[1020] of extra cross neurons which you can
[1023] think of as a point in a neural state
[1024] space it's just the way of representing
[1026] the data of course it must be true
[1028] because there are neurons are firing
[1029] this is a description of the data that
[1032] he deserves what's truism that it's a
[1034] population code this this is a point
[1038] here though the relationships of this
[1040] points to each other is irrelevant
[1041] please think about who's reading this
[1043] information so he's my images of
[1044] different faces and this is a schematic
[1047] here and images of non faces and what
[1049] you need is a downstream reader to say I
[1051] saw faces to be able to draw a
[1053] separating plane between those of those
[1055] high dimensional spaces to say have a
[1057] stand on face in your car or not car dog
[1060] or not hot dog so those are the kind of
[1063] decoders that we build up as girl data
[1064] and we think of them as approximation of
[1067] what neurons can do dot products
[1069] weighted sums with thresholds downstream
[1071] and simplify model goes a long way into
[1074] explaining what's going on here's the
[1076] actual data that we've seen on this in
[1078] real data
[1078] this is response to an image this is
[1081] typically we collect now somewhere
[1083] between a hundred to a thousand neurons
[1085] each green people are not against that
[1087] average response that I showed you
[1089] earlier let me forget here so the bunch
[1091] of numbers here is a population vector
[1093] your eight imagism and then should
[1095] earlier we collect thousands of images
[1096] so we get data sets that look like this
[1098] and I want to point out that these
[1100] images are collected at these data
[1102] within a very high repetition so we're
[1104] really interesting the average biting
[1106] response so we repeat this finger like
[1107] many times in a good estimate the
[1109] average response 50 repetitions for more
[1112] so then you have this big data volume
[1115] here and a lot of work we've done so far
[1117] so just ask how well this did explain
[1119] that what are the linking models between
[1121] that and that I've introduced that
[1122] population because what a minute ago and
[1125] I won't take you through a lot of work
[1127] over the last decade that essentially
[1128] shows simple linear models of the
[1131] decodes that I briefly showed can
[1133] accurately predict these performance
[1134] patterns in these private systems I'm
[1137] going from IT to this and you cannot do
[1139] that if you go to even its input area
[1141] beef or it's certainly not for all your
[1143] hair so this is a very powerful set of
[1145] features here in terms of this many
[1148] deportability to support is kind of it
[1150] okay
[1151] that's really my way a background of
[1152] this tension that the specific
[1154] parameters here are critical and
[1156] informative lots of applications but
[1158] things like brain machine interface and
[1161] so so forth but I'm not going to talk
[1163] about those here today those specific
[1165] parameters the big picture that I want
[1167] you to have though is that what would we
[1169] know from that previous work is that
[1170] this representation here is very
[1172] powerful for supporting the behavior and
[1174] we know how to think about it from kind
[1176] of looking at the spice of rate codes or
[1178] her tiny windows that we have in mind
[1180] here how many neurons approximately so
[1182] it gives us a grounding as to what we
[1184] should be trying to explain back from
[1186] the image so we don't just start up
[1188] trying to explain everything that we
[1190] might see how ways ITV teachers actually
[1193] evolved develop learn to reach this
[1197] powerful endpoint is one of the key key
[1199] set of open questions I'm not going to
[1201] talk about the work we've done on that
[1202] and are doing on that but that's wide
[1204] open question that's not answered by
[1206] what I showed you and you may wonder are
[1208] you really sure that if you push those
[1210] neurons around directly to stay up with
[1212] your dead expert use the law does it
[1214] cause changes in the animal's behavior
[1215] in the way you predict if you believe
[1217] this causal linking all that he put up
[1219] and we have evidence that that's true
[1221] I'm not going to review that for you
[1223] today it's not as complete as I would
[1225] like in terms of able to be able to do
[1227] full PMI like a matrix kind of thing but
[1230] we need to have evidence consistent with
[1232] that and if we might have to talk about
[1233] that the end I'll bring it up well I
[1235] want to spend the rest of my time
[1236] talking about is asking how are the IQ
[1238] features computed from the image it's
[1240] similarly what are the internal features
[1241] so this is going to connect us to what
[1243] amita and Ed talked about because
[1245] they've talked about this input area be
[1247] funded by table sorry then Jack sorry
[1250] you guys are basically the same I'm
[1255] sorry sorry
[1258] okay so everybody would be so far I'm
[1262] gonna list see how we're doing on time
[1263] let's see okay I've lost track level
[1268] we're okay but I'm gonna fly through
[1270] some more here so okay maybe two
[1272] computer models I don't have to say much
[1273] about this because I meet Ben and Jack
[1275] did which is you tend a model that wants
[1278] to take an image and
[1279] a bunch of feature sets or neural
[1281] approximations artificial neurons from
[1283] that the in models I'm going to tell you
[1285] about that you can think of in this
[1286] before you begin on the central part of
[1287] the field I scruffy 4x4 about a degree
[1290] image that's how how we map these models
[1293] so they don't really do the whole task
[1295] really process an image to a
[1296] representation that's one step away from
[1298] the task these models are motivated by a
[1302] lot of neural data they briefly review
[1304] decision are outlined here again I think
[1306] I mean the inject both outlines and this
[1309] is well this is just to remind you the
[1310] current deep convolutional nets actually
[1312] came up a lot of constraints from visual
[1314] thorough size fukushima missus i need to
[1317] mention this the hmx model that the
[1319] venture peas are palet second decade old
[1321] and Dave Cox who's now directing who is
[1325] my first graders commuted out of meeting
[1326] IBM's efforts at Cambridge in this area
[1331] and and they post Pinta who's an apple
[1333] though this class and models in the lab
[1336] this was in 2009 running GPUs to search
[1339] these model families there weren't have
[1341] time to tell you about that but we were
[1342] sort of knew there was going to be good
[1344] models in this space at the time but
[1346] then in 2012 I want to tell you about
[1348] this model because it was a breakthrough
[1349] from us it was the first convolutional
[1351] network that was able to start to
[1353] predict these things as well as you saw
[1355] from jackson tithi and it's we call that
[1357] mama HFO the mid model does not matter
[1360] anymore because agent all was already
[1362] minster past as i'll show you but it was
[1364] revealing for us at the time this was by
[1366] Danny Matteson haha postdoc and grad
[1370] student and here's the gist of this a
[1372] lot of what they did it's a deep
[1373] convolutional net why we build about the
[1376] net because the visual system looks like
[1378] it takes filters that applies the
[1380] different orientations in v1 it applies
[1382] them at different points in space that's
[1384] implemented as a convolution in these
[1385] models we don't think it's a convolution
[1387] in the brain but convolution
[1389] approximates the fact that you tweak
[1390] that a pair level the brain and then you
[1393] have some non-linearity and you do have
[1395] another set of features of the next
[1396] layer and another set of features and a
[1398] stack is a peeper but you're still doing
[1399] some conclusions over space your
[1401] graduate training features space for
[1403] features as you see here the features
[1405] are built as sort of a linear non linear
[1407] operators motivated off of things
[1409] that
[1410] they're feeding here option and others
[1412] have motivated especially replying so
[1415] they're least biologically inspired
[1416] enough and if not perfectly biologically
[1419] Matt but I'd like to say that
[1420] neuroscience putting why the constraints
[1422] on this model think that's why we're
[1424] building them because we're neuroscience
[1425] we're not computer vision people so then
[1428] you take those those models and you say
[1430] get them to do something this was the
[1432] main trick that dananddana
[1434] using to really get this work is that
[1436] instead of trying to fit two neural data
[1438] which is jacking up quite limited you
[1440] get a lot of data out of the task room
[1442] you get a lot of images and say if you
[1444] can guess at the task of what your
[1445] fitness system is doing it provides a
[1447] way to and all the parameters of the
[1449] model to do well on the task and again
[1451] we chose a task core recognition which
[1454] I've already introduced to you we can
[1455] synthesize images as shown here in it
[1457] Nuka recognition and then you use
[1459] basically a bunch of computer science
[1461] and math tricks to tune the parameters
[1463] of this plot optimize them to do well on
[1465] this path I don't play ever believe and
[1468] these are biological that's an
[1469] interesting debate for us they're just a
[1471] way to get this power into an end state
[1473] where it looks like this and then we can
[1475] take this thing which has never seen any
[1477] neural data and ask how well doesn't
[1480] look like the brain so there's no neural
[1481] opinion here you just have never have
[1483] devised do something well it kind of
[1486] looks like the brain are contextually
[1487] and now we can ask how functionally
[1489] doesn't look like the brain sir you can
[1491] take the quote neurons these are neurons
[1493] ethereal effect plays this single
[1496] neurons in here artificial neurons
[1497] compare them with different levels of
[1500] the brain and you already saw Ethan Jeff
[1502] doing this and and insert of a lot of
[1505] people doing this now but again in 2012
[1507] we did this this was kind of exciting
[1509] that we were able to take these things
[1511] and say take these neurons out of here
[1512] basically treat them as a link the
[1514] linear regression onto the neurons here
[1516] the goal was just to predict the
[1518] responses of the neurons and held out
[1519] images and see how well you can do that
[1521] as a measure a match between these
[1523] models and the actual ventral stream so
[1526] remember here's the neural data I showed
[1528] you boys are real neural data we have of
[1531] course the model doing the ballistic
[1533] generate the same kind of internal data
[1534] and then we can take these the model
[1537] that has how we're going to predict
[1538] these neural responses here's one of
[1540] these I
[1541] cause there's a bunch of those natural
[1542] images that I showed you earlier so
[1545] there's 1600 Evanier laid out here it's
[1547] not time these are just images plotted
[1549] here you might say this is a chair
[1550] neuron I don't to play around but you
[1552] can see it doesn't like all images of
[1554] chair there's some kind of structure the
[1556] image of that likes that's Harma
[1558] see-through when you can give it names
[1559] if you like and but so here's what the
[1562] model is able to do this is just the HMO
[1564] model taking its lair or and just
[1566] progressing it to predict these images
[1568] so they'll never see these images it's
[1570] never seen them in these objects of
[1572] these images you're going to see them in
[1574] connection generate a very good
[1575] prediction of the responsiveness appear
[1577] on these images so that was pretty
[1579] impressive to us and that we explained
[1582] on the order of about 50 percent of the
[1584] variance in these responses here on the
[1586] explainable variance which was way
[1587] better than any model at the time here's
[1590] a basement I've evolved you I heard you
[1591] guys in the introduction talk about
[1593] these you're on the snowboard you even
[1594] call it base you're on it it would
[1596] qualify the face grab by the standard
[1597] Craig theory or FaceTime but you can see
[1599] it's not really a face drives it doesn't
[1600] play all images of faces the structure
[1602] in here and you need a model that can
[1605] actually explain that but here you go
[1607] here's the model against assert explain
[1609] all that detailed structure you know
[1610] it's hard to put human name on it as
[1612] Jack said okay so again these models are
[1615] quite good there is think about half of
[1617] these playable variants at the time so
[1620] that was that was on T course Mel so
[1623] apply this to be for you see a lot of
[1626] between this now but everywhere applied
[1628] to be more this is actually B forcement
[1630] and it's Jack without these are really
[1632] hard to put labels on I mean can't
[1634] category label lines serve in no-man's
[1636] land as Jeff went out a number of years
[1638] ago I'm good here you go here's the file
[1640] and if you're some of the middle layer
[1642] of the model can actually predict quite
[1643] well I'm looking at these lines these
[1644] levels not so well this one not so well
[1646] well they did you want to need this
[1647] sentence to have a Goldilocks zone where
[1649] the bills of these models actually do
[1650] quite well in this case the model level
[1653] would layer three of each you know that
[1654] was just one person
[1655] well again in 2012 we were complaining
[1657] about half the variance which was a big
[1659] jump over previous models at the time
[1661] okay so these are predictions I already
[1664] said that he didn't see any of his
[1666] neural data so that's pretty impressive
[1668] white thing I also want to say people
[1670] sometimes call it model of black boxes
[1673] it's not a black box we can measure
[1675] everything from it in detail if we like
[1677] so it's just the thing that isn't easily
[1679] describable in human words but it's a
[1681] lot okay so I want to also highlight in
[1684] that it's nice and Jacqueline before me
[1686] that there's a lot of noise related with
[1687] my work eco review score today I've just
[1690] shown to work from him inside in Japan
[1692] and Malak partner Olivia others have
[1694] since taken this an especially applied a
[1696] lot of papers in human FM erotic that's
[1698] between these same kind of mappings to
[1700] the ventromedial stream
[1701] okay there's a summary in the data again
[1704] by lesson from his jacket on his paper
[1706] lesson is that you submit your paper to
[1708] nips then you submit your results later
[1710] to spice and they say you can't publish
[1712] in science because part and then publish
[1713] it didn't seem to quite explain and that
[1716] was a Western I wonder if there's a real
[1718] publication so you can't publish again
[1719] so so that that these are the results
[1722] shown here this is HFO should it fits a
[1725] layer beautiful this is a moment before
[1727] you see the middle layers to be quite
[1729] well that's one chuckle there and hm
[1731] open a nine see if I twelve a half
[1732] explainable variants explained here okay
[1735] they met a lesson from all of this that
[1738] I hope all of you will take from this I
[1739] think the most important things not
[1740] about HTML is about this slide here is
[1743] that performance on these models is
[1745] predicted performance of these most on
[1747] invariant recognition tasks predictive
[1749] of the ability to fit the brain event IT
[1752] features in this case you can see that
[1753] with a bunch of sample models here not
[1756] two parameters here is some sample files
[1758] per level education on earlier and what
[1761] we think we did with HMO is we optimized
[1763] performance forecast for the fall that
[1765] was better than these models on these
[1767] recognition computer vision tasks who
[1769] has actually been able to predict their
[1770] variance at a much higher level so you
[1772] just continue in this correlation here
[1773] so you use this and get that so this is
[1776] a computer vision goal this is a
[1778] neuroscience goal and then this leads to
[1780] a kind of natural ending sort of scary
[1781] of your hair scientists because you say
[1783] wait I don't even do any work here I
[1785] should just sit back and wait around for
[1787] computer vision to actually produce copy
[1789] in the brain that's some of the lemon
[1790] cakes argument here and that's what it
[1793] says here let's sit back and wait and
[1794] see what happens and it was right about
[1795] this time and who doesn't about that
[1797] balance net first anima seen is
[1799] something computer vision folks were
[1800] suddenly surprised that these models
[1802] that were neural networks
[1804] it works it doesn't make any sense that
[1805] vision works so well which I found
[1808] shocking because we respect the brain
[1810] the whole time and said because have to
[1812] work well but somebody finally got to
[1813] work really well
[1814] ouch then 2012 and that sounds gonna
[1818] need to show you Alex that here's the
[1819] performance whoa here's the performance
[1821] of computer vision on a computer vision
[1823] challenge called image that as a
[1824] function of years and models work they
[1827] went okay and then this model came to
[1829] beat up everyone in 2012 it was the
[1831] first commercial neural network to do so
[1833] well and then all the words are all
[1834] convolution perhaps from here on out so
[1836] they sort of took over computer vision
[1838] around 2013 and of course they're based
[1843] on the brain loosely as I described
[1845] earlier and now here we go again I'm
[1847] gonna practice again for you this is a
[1849] newer fly computer vision goal image net
[1851] performance neuroscience goal this is
[1853] kind of those blue dots I've just showed
[1855] you this the ability to fit IT here's a
[1857] bunch of models here's that ancient old
[1858] level detection with your earlier don't
[1860] worry these numbers aren't the same it
[1861] has to do with normal eyes I really just
[1863] want you to show you in a relative
[1864] comparison and here's Alex that that's
[1867] the model that there's mentioned and
[1868] meet the mention and and I remember
[1871] anything I were talking to Congress and
[1873] said even just use how's that that's
[1874] buddy hmm I don't use a phone just use
[1876] al instead it's already really millions
[1878] what would be available with this great
[1879] and she's using that because I
[1882] told her look we know that that's
[1883] actually kind of the best because here's
[1884] what happens in time so the team is
[1886] doing what they want but they're not
[1888] necessarily getting the brain anymore
[1890] right so there's a there's a bit of a
[1892] turnover here and so you can't just sit
[1894] back suppose maybe good news of your
[1895] inner side let's say don't this wait for
[1897] computer they're optimizing this they
[1899] don't care about that I'm mentoring this
[1901] but they're just doing that and so maybe
[1904] this is like we can't just wait around
[1905] anymore to let them do it all me next
[1908] they're just not putting the brain can
[1909] be better than Alex then at least on
[1911] this one measure I'm showing you here
[1913] but it's only one of the several
[1914] measures that we have but they didn't
[1916] meet some of our benchmarks so here's a
[1917] behavior I showed earlier humans and
[1919] monkeys here's the DCN end this was not
[1921] true for earlier vision models this is
[1924] was indistinguishable statistically for
[1925] us at that level of behavioral data
[1927] we've actually made a ling game out of
[1929] this this is our recent submission paper
[1931] so that's not out we don't may get me
[1933] out at some point this is
[1934] collaboration scores that we call brains
[1937] course includes IP fits before it fits
[1939] behavioral fit but you can see there is
[1941] this continuing trend you don't see a
[1943] stronger maturity is a little kid that
[1944] is flattening out here recently
[1946] Kevin fans even beyond Alex that kind of
[1948] macro sense if you talk behavior be
[1950] forfeit their their on average still
[1952] advancing and their ability to fit many
[1954] of the metrics that we are measuring so
[1956] we monitor it as closely while we're
[1958] also trying to sort of thin things that
[1959] are still broken and this is known as
[1961] illness emergency room who make this lot
[1964] here okay so summary here we're so we
[1967] have this model you know now several
[1969] models all those moms get a top of that
[1971] plot our ans that you could take as a
[1973] reasonable models of the ventral visual
[1975] stream processing not the learning as I
[1978] said earlier and just for one domain not
[1981] all the vision not even all of object
[1983] recognition just core optic reputation
[1985] that identify that's a lot of progress
[1987] anything but you can see one pointing to
[1989] really cold winters are what can we do
[1991] with this right so you say what's this
[1993] really understanding what can we do with
[1995] this time I knew at that time okay I
[2001] would do this cool part here because I
[2003] know era will like it and I'll skip the
[2005] stuff in the end so I don't maybe I can
[2008] take a vote I'll just do the whole part
[2011] a new part here because I think it
[2013] relates to the v4 stuff the Japanese is
[2014] your so this is something completely new
[2017] that we've been working on for a couple
[2019] you let us show you a bit of it why
[2021] don't you build me with these is to
[2022] actually control the dark neurons if you
[2024] actually have a bottle of that you
[2025] should be able to sort pick images and
[2027] try the neural population in any state
[2029] you want it maybe maybe not any state
[2032] but possible space this is related to
[2033] giving synthesis stuff you heard from
[2035] arrow in the past you're basically
[2037] taking the encoding model you build them
[2039] back to the brain then you invert the
[2041] process and even we'll talk about one
[2042] method of doing that there's lots of
[2043] ways to do that we did this closer to
[2046] what era knows another path we start
[2048] with the white boys division then you
[2049] just gray and optimize this to get them
[2051] things to drive them rounds to whatever
[2053] state you decide we want to put them and
[2055] call that controller image and then you
[2057] put this back in and close the loops
[2060] you're still recording from the neurons
[2061] back into lumpy because he can I Drive
[2063] he's not actually into the state of the
[2065] neurons that I'm recording can you
[2066] actually pushing on what you want them
[2068] to
[2068] and so here's whatever goal we call the
[2070] stretch which essentially tried the
[2072] neuron beyond any response that we saw
[2074] with an actual space images here's the
[2077] kind of an example of this attempt so
[2079] here's a predicted firing from the mo
[2081] here's a measure girl fire this is an
[2082] example in v4 see this magical relation
[2085] here this is the sunroom essentially
[2087] what I told you earlier like look how
[2088] could a smile as you can predict really
[2090] really well over space with naturalistic
[2092] images so that's kind of what a review
[2094] of what I showed you earlier one example
[2095] right here is the best image out of this
[2099] set of images here here's the receptive
[2101] field that we measure independently zoom
[2103] in on it tell me exactly what it is the
[2105] curve or the point thing in here it's
[2107] hard I've always heard this thing she
[2108] did you work it out but that's the image
[2111] just so you can look at it but then we
[2113] generate these control dimensions and
[2115] your evil womb they were supposed to
[2116] drive us something up here and they
[2118] really did driver beyond anything we
[2120] hadn't achieved across this large image
[2121] that here
[2123] it's kind of cool these are done from
[2124] additional different scenes you can see
[2126] they look for sexually similar but
[2127] they're not identical and so this is um
[2131] this is kind of a neat thing that the
[2134] bottling control them they're out of the
[2136] places by closing a prediction though so
[2138] I think that's a stronger test the model
[2140] in death or here's some examples of
[2142] these for other neurons you can see
[2144] they're perceptually different kind of
[2146] remind me of the texture stuff from
[2148] arrows groom but I think that's kind of
[2149] fun this is kind of raised at the moment
[2151] but here's the thing I'm actually even
[2153] more excited about is like trying I just
[2155] tried one neuron up to put the whole
[2157] population of the state so if you can
[2159] pull under and out and all the other
[2161] neurons to zero so here's what all the
[2162] other neurons we're doing what we try to
[2164] push that one neuron up with this image
[2166] that's the target neuron and you see
[2168] they're all being driven up a little bit
[2169] well they're above their baseline zero
[2172] here which isn't defined as a response
[2174] with noise an image but then we could
[2176] redo the optimization to find another
[2178] image that tries to control that neuron
[2180] to put the population to that so-called
[2182] one hot speed one neuron at least
[2184] recording they're not active and the
[2185] others not active trying to drive
[2187] another guy's gun we're not fully
[2189] successful at this
[2190] you can see by using the model we're
[2192] actually we're doing again we're clearly
[2193] making improvements these are really
[2194] spell early days on the Miss but this is
[2197] kind of I think a cool direction of
[2198] testing models mr. Levin Navy and crab
[2201] in control on the visual system in very
[2203] possibly you're dripping with okay what
[2206] else can we do with this well it's not
[2208] an urban model right it's one model we
[2211] can do it to do control tricks and
[2213] things like that we can try to do
[2214] commercial physiology on it does it need
[2216] to said but that's not the direction
[2218] we're taking right we want to make a
[2219] better model in a sense it's going to
[2221] pretty things even better I said we're
[2222] only about halfway there for IT we're
[2224] hiring before we got to make better
[2226] model so I'm really just going to kind
[2228] of show you the kind of things we're
[2230] doing just the interest of time we're
[2231] going to flick through we're testing
[2233] natural images we're getting a lot of
[2235] behavioral data from monkeys and humans
[2237] we can look at that data much higher
[2240] resolution I showed you earlier image by
[2242] image resolution TVs miles are not the
[2245] same value zoom in you can see a broken
[2247] here and it's not like one image is
[2249] broken is a pattern is broken and this
[2251] isn't I think we're trying to give you
[2253] that data as constraints to make the
[2255] models better this was a compare this is
[2257] now showing you the models are enough
[2258] clearly not brain like others and shows
[2260] two other ways they're not even as good
[2263] as the brain when you measure them
[2264] carefully image by image that's what's
[2266] up here and just for the kind of people
[2269] in the room that are really as rating
[2270] feedbacks I mentioned that earlier I'll
[2271] just give you this kind of tip in here
[2273] which is if you prepare because we not
[2276] work with a team in amount of Jack and
[2277] I'm dirty if you compare how well what
[2281] the brain does when it's actually trying
[2282] to solve how what it's doing when it's
[2284] dealing with these images where the
[2286] model here looks like the brain here in
[2289] terms of behavioral so these are we call
[2291] this computer vision solid images where
[2293] here's a bunch of images where the
[2294] system the monkey doesn't weigh better
[2296] and the model at least this model and so
[2299] we call this computer vision unsolved
[2301] images and we're really interested in
[2303] what is the brain doing to these images
[2304] that's not doing with these because
[2307] that's where the secret sauce is in some
[2309] sense relative to this existing the
[2311] neural network here and here's so these
[2313] images you can stare at while they long
[2315] to do regressions it's hard to find
[2317] anything that
[2317] wishes them and so forth it's a little
[2320] bit of weight on most things but not
[2321] anything obvious but we do find
[2324] something that clearly distinguishes
[2325] them in the rain so far that's where
[2327] coverage car shop here and the basic
[2329] idea is we're going to look at those
[2331] images now high-performing images only
[2333] here we're going to just show me what's
[2335] going on I'm gonna zoom in and show you
[2336] what the brain is doing in response to
[2338] these two types of image it's the ones
[2340] that leadership has effectively solved
[2342] and well as the brain and the ones
[2343] that's not us all as well and what we do
[2345] is we play our standard tricks go into
[2347] ITC what's the code looks like you plug
[2350] in a bunch of a radius down here you
[2351] record all the channels you can then
[2354] plug the decode as a function of time
[2356] what I'm going to show you in this
[2357] vector UW coder everything I've shown
[2359] here you go here's the decoder now we
[2362] got the decoder as a function of time
[2364] here's what image is that silence a face
[2366] and I'm going to show you how I deep
[2368] looks temporarily now soon it not just
[2370] what number but temporally zoomed in
[2372] because we have got a much higher
[2373] resolution now and what we see here is
[2376] the time up to the monkey neko here
[2378] comes more about our milliseconds looks
[2380] like gives the animals report similarly
[2382] I showed you I suggest earlier it's this
[2385] you know people it's just gonna get the
[2387] answer here zebra who comes up there's
[2389] the answer pops out of oven TV you can
[2391] decode it now here's a see if there's
[2394] the image with is a car looks like a
[2395] pretty easy cars a lot to the left
[2397] maybe I don't know what these pretty
[2398] quick mistakes a car that we selected
[2400] these images so you're really good be
[2402] really good saying this in the cars were
[2404] sending other ones of zebra and in here
[2406] you know
[2407] oh I'm team decoding it it was
[2409] successful but longer something happen
[2412] there maybe you talk look look I'm T's
[2414] responding that's what's up here it's
[2416] not like there's no activity it's just
[2417] not linearly available to support the
[2420] Pico here comes another when there's a
[2422] dog it's from a for short view a little
[2426] bit longer again that's for examples
[2428] just to give you a sense here's a dozen
[2431] examples and you can see that the red
[2434] dots which are the ones that are
[2435] computer vision not solved we say take a
[2437] little longer to get out of answer
[2439] and this is just one of them I'm getting
[2442] so many examples importantly these these
[2446] images are all solved than I'm T so
[2448] that's good even though they're not
[2450] solved by computer vision but just take
[2452] a little bit longer about 30
[2453] milliseconds longer still with the new
[2455] clinton still within a couple areas but
[2457] something is churning for another 30
[2459] milliseconds or so so i'll just suggest
[2461] some role for recurrence or feedback we
[2464] think this is not to be surprising to
[2466] all of you we just kind of cool that we
[2467] have evidence of rare time in point this
[2470] and what another piece of evidence here
[2472] if you take a deep neural network like
[2474] the helis one I've shown you here here's
[2475] its ability affinity response as a
[2477] function of time now snooping all the
[2479] time it fits well at the beginning and
[2482] then quickly falls off and doesn't fit
[2484] so well over here so all of this is
[2485] consistent with the idea these models
[2488] are missing some recurrence here that is
[2490] and that exists in the brain that's
[2493] giving it an extra boost especially for
[2495] these kind of read and challenged images
[2497] we call it here okay so how are you said
[2499] all that I'm gonna just have it end here
[2501] and say okay you have to build them not
[2504] just before Network we leave other
[2506] planners or triangle deference that are
[2507] recurrence that engage that in more
[2509] interesting ways that's kind of what
[2511] that says here and in the broader space
[2515] we're excited about the convergence
[2517] between measurements on the mind of the
[2519] frame and building things as models as I
[2522] started describing the reverse
[2523] engineering approach I think that's
[2524] broader than just vision it's extends to
[2527] other aspects of intelligence
[2530] there's my shameless advertising if
[2532] you're interested in coming to visit us
[2534] in the lab and I'm gonna just leave him
[2537] here with the organizer questions that
[2539] they asked it might weird answers
[2540] depending for discussion but then
[2542] they'll stop talking
[2548] [Applause]
[2585] [Music]
[2599] right so the question is essentially
[2601] kind of like a Heisenberg thing it's
[2603] like you gotta measure the system and
[2604] you're gonna push the system so even get
[2606] your measurements as moving the system
[2609] well so three things I can say about
[2613] that it's like if you take data from a
[2615] passive viewing animal which is still as
[2617] I'm seeing them 50 times I think we've
[2620] tried to zoom in on the first image
[2622] others have look at this I'm not going
[2624] to have no effect on this right there's
[2626] always adaptation within trials there's
[2629] there's slow adaptation over longer time
[2631] scale we're gonna section running with a
[2633] little bit roughshod over that because
[2634] we just average over lots of things so
[2636] we're giving you strip of that curve you
[2637] will be a philosopher many images so I'm
[2640] gonna I'm not going to deny that those
[2641] effects exist in data he doesn't believe
[2644] it is the past leaving monkey and that
[2646] versus it actively reading about the
[2647] early in its training versus an active
[2650] they knew might either late late
[2652] actually very monkey early in the data
[2653] collection versus very late months later
[2655] in the data collection
[2656] those three look very similar from the
[2658] metrics used here so we regarded the
[2661] ways I process the data here there's not
[2664] much of that then but again it doesn't
[2666] mean there's no effect it's also spikes
[2668] and we get lots of details in there then
[2669] he announces so I think I'm sort of
[2674] avoiding your question but telling you
[2676] from the measurement we do they don't
[2677] seem that dependent on that but learning
[2680] is a big open question I'd say less
[2682] about application but again how do you
[2684] give the neurons into that I mentioned
[2686] the headline learn the obvious termites
[2688] guess with a linear decoder
[2689] animal has to learn that he learns that
[2691] about two days I could show you slides
[2692] on that we don't think that learnings in
[2694] my team we think it's passed by T but
[2697] that's another question I can answer for
[2698] you here but we have some
[2700] the really depressions are you build a
[2703] bengal stream in the first place not
[2704] probably by that prophecy provides
[2706] training per million images which is
[2707] kind of have a certain air of adult this
[2713] is kind of a follow on David's question
[2716] what percentage of the variance is the
[2721] explainable variance so it depends how
[2724] you would measure the raw berries right
[2727] yeah so if we measure it on let's say
[2731] the account of the you know the count of
[2733] spikes in one in that 100 millisecond to
[2736] go in one trial yeah that's one number
[2739] right versus I can measure this all day
[2742] and that's going to be a different
[2743] number right so you're going to get any
[2745] number you want
[2746] so when for us but explain was
[2748] essentially to provide data we collected
[2750] like when we say we have 50 trials and
[2752] that is a sum amount of 50 RS give us
[2754] some other point where it's at 100 reps
[2755] I have more points
[2757] right so I'll just go up maybe what
[2759] you're asking is well I'm not sure how
[2761] to it's just an open question I mean
[2763] it's still gone Frederic is no reason
[2766] surgeon within your comp windows you can
[2769] easily compute the variance just over
[2772] the truck you've got 50 trials so you've
[2774] got that very handsome well so that's I
[2776] make an admission that because
[2777] everything we take the data and the 50
[2779] Travis women to the two halves correlate
[2781] them with each other
[2782] adjust efference but ask your ground
[2784] correct that tells us the ceiling limit
[2786] on what any model should be able to do
[2788] given that dataset but I can collect the
[2791] bigger dataset where that I will go up
[2800] yeah I know I understand but it really
[2806] no I'll tell you the really kind of
[2814] that's every question for us not scared
[2816] when we're trying to address it related
[2818] to this what's the explainable variance
[2819] across animals that's something that's
[2823] much harder to quantify in these
[2825] experiments and nervous lu small number
[2827] monkeys we need water bodies are
[2830] interviewing trees within and they're on
[2831] within an animal that's
[2832] Jackie and even all dude but it's up
[2835] cross monkeys is a harder one important
[2837] question and it's important to Aspen a
[2839] models bumping up to a limit like 50
[2841] percent wouldn't be the species limit we
[2844] don't really know these guys want to put
[2848] back on that that we're trying to figure
[2850] out what that number actually is not
[2851] fair the model just has to be a member
[2853] of the species it has to be like a
[2855] private doesn't have to be like that
[2857] particular private that's too hard us up
[2859] all over going that's a different kind
[2861] of yes I think have any more spend any
[2867] more subjects how much of the explain
[2876] your yeah I think that's a rephrasing
[2886] with the same interesting question right
[2888] and you can have models are happy to
[2890] share component which is what we're
[2892] mostly after at the moment but you'd
[2893] also like malls I could account for the
[2895] medial variability but that's in you're
[2897] able to in Gainey on that we're not so
[2898] much yet I wonder how the body but this
[2906] mother for example there there are data
[2908] from Bart's laboratory is that that the
[2911] low-frequency components can you form
[2915] much faster well yeah that's where I
[2922] kind of briefly breeze through here by
[2923] step luckily we I'm showing here some
[2926] kind of our this was kind of evidence
[2927] and convinced us that that kind of
[2929] timing lightly implies feedback dynamics
[2932] that are important to the animal's
[2934] behavior and we have who were the
[2936] crowing miles they take advantage of
[2937] that to connect the things that like
[2938] Chandler talked about that but now we
[2942] are asked how do we go from beyond this
[2943] model to these models which sort of
[2946] decide which of these connections we put
[2948] in and how do we put them right and to
[2950] the way we've been doing that so far is
[2953] the build models and half of its amount
[2955] of recurrent hours optimizing them in
[2957] the same way that these models are
[2958] optimized which is optimized on an image
[2960] categorization task as well
[2962] dude but I think we miss is hospitalized
[2964] but we're not getting this back right
[2966] now it's paying for it but also having
[2967] people just dive at MIT in a bit in my
[2969] group but that's the our current shofar
[2971] is to just change the architecture and
[2974] reoptimize and see if we get things that
[2977] do higher performance and fit but are
[2978] not better and so we're getting a little
[2980] hints to vote for those but it's nothing
[2982] on register really wow we made a huge
[2984] break you
[2984] we're not even sure it's a feedback or
[2986] just recurrence within area that might
[2988] get off well we're treating the data
[2990] like this drive us there so that that's
[2992] our personal part we have not solved
[2994] that problem it's one of them report old
[2997] impressions yes we're not the second
[3007] thing any good you mean what we're
[3012] asking them to do ya know once a week we
[3022] kind of giving the same task I gave you
[3023] which you ever been in it out of box
[3025] like here tell me what you see I didn't
[3027] say statements but we're building the
[3028] objects so they're one object place well
[3034] I don't know what it is all I know is
[3037] that's the I'll be a behavior is now
[3039] that's my definition of a words after
[3043] that or maybe or the people that do
[3049] segmentation point out that hey these
[3051] models are actually rival segmentation
[3053] right so so I think they're finishing
[3056] debate is about what architecture should
[3057] we put into this invitation you optimize
[3061] and then the deeper questions how does
[3063] the brain optimize s so that as time
[3065] evolution and some of that is going to
[3066] be unsupervised learning those are the
[3070] axes and Congress your entities here I
[3072] think those are be more active to be
[3074] searching over that's what we're trying
[3077] to search holder so this is a really
[3081] speculative question and I already know
[3084] the other speakers do think there's a
[3086] role for using lesions to try and build
[3090] better models so in other words could
[3092] you train a network
[3093] that makes mistakes in the same way that
[3097] monkeys with a v4 or ITV's in me or
[3102] humans for that yes so our approach to
[3107] that lesion I'd like to leave the
[3108] question because it's kind of gets tough
[3109] we call direct causality test and this
[3112] is their armor you know this here it's
[3114] like we have models that are decoding
[3116] models with a full encoder on the front
[3118] end and you need two different parts so
[3120] but you should be able to take that
[3120] model into its a like a similar lesion
[3122] on the model as it will to be animal and
[3124] I should see somewhere affection and the
[3126] end of the day all these aren't tests a
[3127] bottle the correctness to the end they
[3130] were conferred Android lots of XP
[3131] understanding think I said it but we've
[3133] done a bit of lesion work so that
[3136] optical that sir here and face patches
[3138] here but we've also been doing these
[3140] small V small injections people
[3142] mentioned this in some of the earlier
[3143] talks like oh it's hard to find effects
[3145] we end effects across tasks and so far
[3147] these effects are consistent with the
[3149] models I've got so far it's an important
[3151] stability that those model tinnitus
[3153] patients have ography but the horizontal
[3155] layout in the brain which is another
[3157] kind of cost constraint it's not a
[3158] performance constraint it's on fire in
[3160] cost context we put that in before you
[3162] actually lesion the model that's all
[3164] work that we have that I didn't have
[3166] time to tell you about the business like
[3168] some of our median data because they're
[3169] Micronesian enacted reversible you saw
[3172] b19 with like differential passage that
[3175] I think you're trying to get it you know
[3177] we have a great model the emanates all
[3179] about that's a discussion I'd like to
[3181] have me be special copier and like
[3183] because I think we're supposed to talk
[3184] together
[3185] I don't know maybe the three of us share
[3196] the same feeling like what other
[3197] standing is going to look like with the
[3198] model I don't know if you guys are on
[3200] the same page but yeah it's really cool
[3215] cool system we get a lot of model
[3218] elements that could be squeezing it out
[3220] of the model and then he basically two
[3222] different models in and out like you
[3224] need replication
[3230] [Music]
[3289] [Music]
[3314] there's a lot I said getting all the
[3318] series of all the renovation we've
[3319] actually regions there's a lot of
[3321] studies about no effects right and so
[3323] then you look at the stimuli and say oh
[3324] it was a red triangle versus the green
[3326] square it is retraining time so part of
[3330] it you know they're not if you're not
[3331] designing different routes right I mean
[3338] we think that to read out of the rest of
[3340] the monkey that is the Korres is the
[3341] balance great stuff can read out of
[3343] areas and beyond back here reading
[3345] probably me wanted it needs to so the
[3348] trick to doing is like try to keep the
[3350] m1 gauged in the system that you're you
[3352] know and not rerouted I know there's a
[3354] nice about Mike stuff here there was a
[3355] nice funny from his lab with optical
[3357] things like how
[3358] Oh in time way red so you know these
[3362] news of all things seem to work pretty
[3363] well we answered that monkey can right
[3366] around me so when we measure her these
[3368] kind of effects that we compare the size
[3370] of Levi's making relative to the number
[3372] of neurons we see that it's a map it's
[3374] this Billy would expect given the amount
[3376] of cotton ball and they have some
[3378] unpublished work on like silencing big
[3380] chunks of ITT that brought the animal
[3381] down your chance on kind of area so so
[3385] it's not a Queen's you have it's hard to
[3388] be careful with the behavior and then
[3390] use illusions and cause experiments like
[3391] that are really triggered for both of
[3393] these reasons just how you're doing the
[3395] mutation how you're controlling the
[3396] behavior both like white or others maybe
[3398] or didn't speak better to that I think
[3444] it's absolutely the way I think about
[3453] that you know I'm not very much trying
[3459] to come up with and I look at these
[3464] things and say can i adolescent and get
[3467] these things so I think they're
[3476] absolutely right and and another way to
[3478] be present is to keep making these
[3480] models fit because that's another
[3487] so you see models the predictions no I'm
[3497] not sayin well I haven't really heard
[3499] that everything you just said exactly
[3500] the best part about breaking that but I
[3503] know you made an important point that my
[3505] Kincaid this is just the entire family
[3507] of deep feed-forward networks that way
[3515] you can post by particular models so is
[3520] it Alec specific because of any long any
[3526] come back yeah so I can't I can show you
[3570] to your piece of data
[3571] I'm not helping you see forty from
[3574] before me but do find Iran's is before
[3578] that show to transient their response we
[3583] think we haven't done the vertical
[3586] experiment for this would we think the
[3588] second
[3589] transiently comes from feedback and why
[3593] do I think that we don't be exact same
[3595] experiment and the second transient even
[3599] before looks awfully long like like the
[3602] first one that the PLC neurons have only
[3606] one peak and it looks very similar in
[3610] response properties to
[3612] [Music]
[3615] like it could be but it's not I'm not
[3618] supporting selflessly I don't know that
[3620] these wrong subdued other boy which
[3630] which was that really visual system is
[3638] the boring part before you look in these
[3641] war or how much modulation there is due
[3645] to attention or any thoughts without
[3647] task effects it's about 15% of an animal
[3650] in a spatial attention task the
[3652] modulation of 15 teacher based attention
[3656] task modulation in tuning is about 15
[3659] percent so these are not enormous
[3660] effects you remember David shine burns
[3663] old study from like 20 years ago when he
[3666] had animals looking for really tiny
[3668] targets in very cluttered scene
[3669] somewhere swalot task he reported at the
[3671] interior pole that essentially attention
[3674] was attended to the target and saw the
[3681] terminals aware of it you have big
[3682] response this is the throwing you later
[3687] so I think there's a huge and a lot
[3691] there's a lot of data to show that these
[3694] effects increase in their magnitude from
[3699] where these models so I just want to
[3723] continue this this theme of the sort of
[3726] top-down aspects of this because there's
[3728] a you have these models running as
[3732] you're pointing out on on all cylinders
[3734] basically and the case has been made
[3736] that the reason we need to have
[3737] attention is that we came to handle this
[3740] basically it's too much of a cost on
[3745] on brain function so part of the
[3746] challenge here is that many of the tests
[3749] we do even in the human vision lab are
[3751] done with all cylinders and other it's
[3753] sparse environments as you presented two
[3756] simple judgments of objects and that's
[3758] not going to happen to the course of
[3760] natural behavior and we haven't really
[3762] harnessed this in terms of what is the
[3765] appropriate measure to use to capture
[3767] what we are getting from any image at
[3770] any time and we can't really test these
[3773] models of is addressing the questions
[3775] around the brain works until we leave
[3777] figure out what it is we want to measure
[3779] that so that's as much a problem on the
[3781] psychophysical end as it is a real
[3785] question on the neural the modeling
[3788] innovations expand the domain something
[3791] bigger than Y particularly why I showed
[3794] you I would like it to be arguing that
[3796] way rather than there must be feedback
[3798] it must be important there must be
[3799] attention must be pouring the argument
[3801] here's a new task that's the next task
[3804] up from core recognition okay now I need
[3806] to deal with eye movements right that's
[3808] sort of the natural thing you know what
[3809] are we going to ask that you've been
[3810] secure you have to do is add a search
[3811] basket you know things have been done
[3813] that go maybe but if we could formalize
[3814] things in that area and then build
[3817] models of X again this isn't some people
[3818] are doing this right now just we've
[3820] picked a problem again fine but I agree
[3822] with you motivated from subdued
[3823] psychophysical space doesn't really
[3827] exist in people no it's neat to raise
[3868] our single cells
[3869] I mean we're recording
[3894] rather a heretic question since I'm
[3898] talking to three people who have devoted
[3899] their lives in recording and analyzing
[3910] so the problem of how the brain works in
[3914] other words do you believe that euros
[3916] are only processing unit in the brain
[3921] those are two different questions
[3926] when you say cannon tell me doesn't mean
[3929] Anatomy or do you also mean physiology
[3932] oh yeah so in other words already
[3939] perhaps key player in the brain and I'm
[3943] referring 20 2008 silence paper were
[3948] fairly p1 astrocytes
[3950] were found to have narrower receptive
[3954] fields than neurons that's one of my
[3957] favorite images from just college that's
[3959] one of my favorite papers - so could for
[3963] example other types of brain cells such
[3966] as astrocytes contribute and oxygen as
[3970] Reds have higher tuning in neurons
[3972] orientation because they have a
[3975] threshold momentary an astrocyte
[3978] astrocytes in the primate enamels they
[3982] take up excess neurotransmitter they
[3985] essentially we package it as a side
[3989] effect they have little Philip voting on
[3991] the blood vessels and when an answer
[3993] site to text that it picked up some
[3995] neurotransmitter released its ability
[3997] are and more blood flow goes so after
[3999] essential the whole reason that ever I
[4000] works and it's basically just God's gift
[4003] to MRI that the tuning in answer site is
[4006] actually better than the
[4008] tuning in neurons those are the answers
[4013] well something we should exactly where
[4022] is very point is that NASA site
[4027] certainly plays some role in function
[4030] for example when more oxygen or sugar
[4032] fell to the bloodstream and actually
[4034] probably has but it's a very indirect
[4040] problem of that become closer
[4042] archaeologists think that those neurons
[4046] and astrocytes yourself and something
[4065] you don't ground your self which again
[4077] is is a choice
[4079] then there's reasonable guesses about
[4081] like one of the things that are most
[4083] likely to be relevance or the kind of
[4085] almond almond scale going to be in to
[4087] satisfactorily explain all vision I
[4089] think it's going to be minute but don't
[4102] you think that this constitutes booking
[4105] where the spikes are like the drug
[4107] looking where the light is is not a
[4110] question of neurons and spiking because
[4113] we have any suggestion what's in the
[4116] guts of the neuron may be a locus for
[4120] memory we have I don't know how many of
[4122] you folks were here a day ago when Dan
[4126] Margo Lee has presented the subtle
[4128] effects of changing ionic conductances
[4131] on
[4132] spike shape that lead to pattern changes
[4136] that underlie
[4138] behavioral changes and those conductance
[4141] is our conductances therefore they're
[4143] sensitive not only to the intracellular
[4144] state but the extracellular ionic state
[4147] which may be heavily as you suggest
[4149] conditioned by the glia so I wouldn't
[4152] laugh when we talk about adult
[4159] incurrence in 200 milliseconds so that
[4162] takes out a lot of these sort of thing
[4164] if I'm studying long term developments a
[4166] lot of these other things are relevant I
[4168] don't yet know but you think a problem
[4170] with a timescale that like links are
[4172] going to be needed to do that so you
[4174] have a better chance of making practice
[4176] of the 9 what you're saying is that
[4178] means relevant to some other questions
[4180] the exam to my question for my there
[4194] certainly you direct hormonal influences
[4196] their indirect neurotransmitters then
[4197] you know act as a general
[4200] neuromodulators the vast majority of
[4203] information transmission through the
[4205] system as far as we know this don't even
[4207] build a model of spikes that's it
[4223] symbols are relative I want to change
[4227] that very slightly to ask how our object
[4230] categories represent ask the three of
[4235] you see and direction that no reason to
[4247] answer oh this is how the ball symbols
[4251] or the ball representation so do you
[4255] envision that there could be concise
[4259] answer and usefully concise answer the
[4263] question small how our object categories
[4287] [Music]
[4291] that's right but your point is there's a
[4388] lot of detail how we have to represent
[4396] networks
[4399] very excited it seems to suggest that
[4403] there is no concise statement about how
[4408] the networks work that's a different
[4412] issue from there so in in this in visa
[4420] network you just got to cut the network
[4422] if you look at the police neck conveyors
[4424] right you're starting to see category of
[4427] those sorts of things so I showed you
[4428] some examples
[4430] feeding caps were many kinds of things
[4433] it doesn't matter precisely what color
[4436] it is or what shape it is but as long as
[4438] half with features that there was those
[4444] units are activated so the question
[4461] mention physiology spelling is record
[4463] everything all the time right now and
[4471] MRIs and in almost every way except you
[4475] if you look at this issue there are two
[4480] really interesting facts one well look
[4485] you there as Russ pointed out earlier
[4488] there's a bunch of semantically
[4489] selective caches of human cortex that's
[4493] surround the rabbit eye there is sort of
[4495] that you know you end up with these
[4496] concentric rings that talking with next
[4498] areas become increasingly meta tonic and
[4501] eventually you end up with a bunch of
[4503] patches that are fairly selective and
[4515] then that's the middle those patches
[4529] immediately anterior to those boxes are
[4532] hatches that are semantically selective
[4535] but not for visual stuff there's
[4536] definitely selectively the categories
[4538] that are brought up in territories and
[4540] if you look at semantic selectivity
[4544] patches behind this boy is usually
[4547] driven patches in visual lexical cortex
[4550] that is immediately anterior there that
[4553] are not by traditional categories by
[4554] stories of language there's selecting
[4557] for the same semantics so there's very
[4561] which pattern of sensitive a vision we
[4564] think because the brain generally thinks
[4566] are close together are usually wired
[4568] together we think that they're usually
[4570] selected categories feed into in humans
[4573] have language network for representing
[4575] semantic category that is a modal now
[4580] plug is our conversation alot of words
[4586] but they certainly can do category tasks
[4588] so they must have some internal semantic
[4590] representation it's our native language
[4593] but it's plates probably be mobile and
[4595] divorcement vision what happens with
[4598] these vision networks feed into high
[4600] water networks in prefrontal cortex
[4601] which are the ones that those will be
[4604] categories like and there's been a lot
[4606] of work from other people showing
[4608] categories to improve memory
[4611] this whole thing is called high
[4613] dimensional low dimensional so IP is
[4616] quite a few hundred dimensional you may
[4620] offer a fair amount of that like you see
[4624] I think of our cake shop it the
[4627] Colombians and privately draw when you
[4629] asked me to report because it's fun then
[4630] you step away from lots of reporters now
[4633] we're exactly how we do that we know
[4636] about sign me in Bethesda an open
[4638] residence bill but you could also occur
[4640] the patent dog stuff witness very well
[4642] learn things are going to come them in
[4644] the Bakker those are special dimensions
[4646] but it's probably going to be in my mind
[4648] some mixture it's not going to be like
[4650] here's just cats it's going to be a
[4652] buffering a lot of the things have been
[4654] a relatively low dimensional relative to
[4656] the sensor space that's available per
[4658] caste you could ask me even later what
[4660] do you think you saw that it
[4662] ahead of time I can report on that so
[4664] that's a servo that's how I think about
[4666] how it's gonna look at out of that
[4668] satisfying humid then the key questions
[4670] are like how many dimensions did you
[4671] buffer or were those dimensions and how
[4673] do they change with learning and history
[4675] and I'd only pull it on the ends of the
[4677] hints of the type rate of look we don't
[4679] have answers that's on the thing about
[4680] taxis on the encoding space or on the
[4682] memory buffer space those are hugely
[4715] isolated you know how that actually
[4734] works essentially statistical power
[4738] measurements really I won the best
[4747] Jimmer is anyone showing these
[4750] adversarial examples to here core up to
[4756] it as a way of driving a wedge between
[4759] the what the man is doing if your head
[4762] is like other people's nets it's being
[4764] blown away by the center observer
[4766] examples
[4767] what's happening in IT is if the not
[4769] cool we didn't show you back with
[4773] adversarial people don't know you create
[4775] thinking image you twist a few pixels
[4777] around human knowledge of the model and
[4778] then you say it's the looks like a cap
[4780] to a human but the bottle said that's a
[4782] given right so you don't even need to do
[4784] an experiment that you didn't did one
[4785] second physically to say there's
[4786] something's broke in with the model
[4788] right so
[4789] we took images that we found this kind
[4791] of a show you this computer vision
[4793] unsolved images then we're like just
[4794] they were tweets of Tribune they were
[4796] just discovered in a set of naturalistic
[4798] images and then we looked at ID and I
[4800] can handle them just fine
[4802] I didn't show this we can see and I'm T
[4895] not people that you can see a trial by
[4898] trial it's essentially one such probably
[4901] work at or school and see a trial by
[4902] trial then does unpublish so far so I
[4912] would not yet but it's just what you'd
[4916] expect
[4919] so I guess you heard all this mystery
[4923] there's a lot more to be done and they
[4925] were made about the skill and it's all
[4927] that really hopefully not but this is
[4934] wrong here
[4936] so let us be killed again
[4940] [Applause]
