---
schema_version: 1
id: yt-5kq7M6pcQ5g
type: youtube
title: 'Jim DiCarlo, MIT: Reverse engineering visual intelligence'
url: https://www.youtube.com/watch?v=5kq7M6pcQ5g
authors:
- CCBM2018
ingested_at: '2026-05-30T21:59:36Z'
content_hash: sha256:1fbd6d5c6db04df8629f6df06ee267b90ccba9ff3f89e70a6c65e29dc4d5c8d2
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: CCBM2018
  channel_url: https://www.youtube.com/@CCBM-sb3cz
  duration_seconds: 2455
  caption_track: fetched
  snippet_count: 1291
filter:
  score: 0.8
---
[0] and so the next speaker is Jim DeCarlo
[3] who has thoughtfully given you all of
[5] his titles on his title slide so we know
[7] who he is
[8] Jim is chair of the department of brain
[10] and cognitive science at MIT and is well
[14] known for work that bridges the
[15] physiology and biology of object
[18] recognition and the use of deep neural
[19] networks to understand that biology so
[21] without further ado Jim okay good
[25] morning thank you for inviting me Tony
[28] and the organizers I remember this is a
[30] conference in neuroscience and AI and
[33] what they can say to each other so I'm
[35] going to try to give you an example of
[37] how that's worked for us and hopefully
[40] it either if you're not working in
[41] vision it will still inspire something
[43] that you like to think about beyond
[45] vision and again the story and vision is
[47] not yet complete but I'm going to tell
[48] you an overview of how we've put these
[51] things together so far and maybe how
[52] we're looking forward so I titled my
[54] talk reverse engineering human visual
[56] intelligence that's just a provocative
[59] title I'm not going to talk about all
[60] the visual intelligence but I do want to
[62] kind of talk about this term reverse
[64] engineering so what does that mean so
[66] for me what that means is we as a group
[68] having a goal really to account for each
[71] ability of the mind which I'll broadly
[73] call intelligence using components of
[76] the brain which for systems
[77] neuroscientists often means neurons and
[79] their connections and we want to do this
[82] in the language of engineering which
[83] means we're going to have math and
[84] computational models that can explain
[86] all this ok that's really a kind of a
[88] statement of the problem or which gets
[90] to an approach as my colleague Josh
[92] Tenenbaum likes to say is another way to
[93] put this as late let's do science like
[95] engineers or similarly let's do
[96] engineers like scientists right so this
[99] is how what we've tried to do in our own
[101] lab and um when I want to sort of give
[104] you the most important slide first
[105] everything I want to show you is from
[106] these folks in my lab and collaborators
[109] some of listed here and especially work
[111] of Dan yemen's that who's now at
[112] Stanford and I'll try to highlight folks
[114] along the way ok so reverse engineering
[117] I sort of gave you a set up of what that
[119] means but here's what it maybe means a
[121] little more concretely for us so if
[123] you're going to work on a problem some
[124] kind of visual problem you have to
[125] specify at first so define
[127] operationalize a domain of interest and
[129] usually this means something that brains
[130] do maybe better than us better could be
[133] in a perfect
[134] do better than machines in a performance
[135] sense it could mean a power sense could
[137] be an annus eyes all of those things are
[138] senses of better and then you want to go
[141] and measure something in the system so
[143] this is a natural science you go and
[145] make measurements of the system of
[146] biology and you want to choose those
[148] measurements wisely because there's lots
[149] of stuff you could measure in the brain
[150] right so you can measure behavior in
[152] spikes that's what I'm gonna show you
[153] but you could measure anatomy which is
[155] important as well you can measure blood
[157] flow neural perturbations subcellular
[159] genetics you could do all kinds of
[161] things within the brain it's a
[162] neuroscience there's a big tent so you
[164] need to choose wisely if you want to get
[165] constraints on these kind of on the
[167] thing that you've specified but then you
[169] can't stop there that's just measurement
[171] then you have to actually go and build
[173] models so you can think of this or I
[174] like to think of this as forward
[176] engineering under the constraints of
[178] those brain measurements so the model
[180] must can't just be a kind of conceptual
[183] model it has to actually capture all the
[185] measurements and it must predict
[187] held-out measurements as yan said it
[188] sort of if we the essence of
[190] intelligence you could call prediction
[191] and this is a meta version of that if we
[193] as scientists are going to say that we
[195] have an understanding we'd better be
[196] able to predict held-out measurements
[198] from the system of interest now in
[199] practice what this means for most
[201] systems neuroscience is that we're going
[203] to be working with artificial neural
[204] networks so because those have neurons
[206] you they may not be exactly like our
[208] neurons but they have neurons that can
[210] be mapped to the brain so that will
[211] allows us to make predictions in the
[213] brain and this often means because we're
[216] gonna predict and not just have
[217] conceptual ideas these models must often
[219] be built at scales that approach the
[220] scales of the problem the complexity of
[222] the task that we're engaged with so
[224] these are kind of components that you
[225] could call from ml machine learning AI
[227] broadly that are critical to advancing
[229] our understanding of how the brain and
[232] the mind work you don't just do this in
[233] a one way loop and then end of course
[235] then you end up with a family of models
[237] that need to be better called by more
[238] measurements build better models more
[241] measurements and them faster you can
[242] make this cycle go I I would posit that
[245] this leads to a model that will which we
[247] would call our kind of human
[249] understanding of the system that we set
[251] about to measure at least over the
[252] domain that we specified and you again
[255] this you can think of this is the domain
[256] of science which is its purview mostly
[258] lives here and this the domain currently
[260] of Engineering especially AI nml with
[262] respect to the this audience here so
[264] what our goal is to really as a field is
[266] to pull these things tighter
[267] together I think that's the point of
[268] this conference I want to point out that
[270] if you work in this framework the models
[272] you come up with are actually in the
[273] language of engineering so they're not
[275] that far away from various applications
[277] at which many of you are interested in
[279] and I don't just mean AI so um this is
[282] an MIT embodied by our Center for brains
[284] minds and machines and also an
[286] intelligence quest initiative launched
[288] at MIT this blending or merging of
[290] science and engineering so I'm going to
[292] tell you this sort of big picture idea
[294] of how we think about doing science
[295] today about our problem which we call
[298] human core visual object perception or
[300] more Moore's more precisely visual
[302] object recognition and I'll show you
[304] that next so many of you know our work
[306] we know we work on we want to understand
[308] visual scene comprehension or broadly
[310] visual intelligence um we started way
[312] back when and we've really been focused
[314] just on the problem of categorization
[315] much like the history of computer vision
[317] so just being able to be able to label
[319] the objects in the scene here we take
[321] advantage of our knowledge that we know
[322] something about the primate retina and
[324] the primate ventral visual stream that
[326] I'll show you in a minute it really
[327] processes the central part of the image
[329] say the central 10 degrees which is
[330] meant to be illustrated here and you
[332] don't take in the scene all at once and
[334] instantly understand it you make samples
[336] around this scene where you dwell for a
[338] few hundred milliseconds called
[339] fixations and you rapidly move your eyes
[342] to sample the scene so what that brings
[344] to your ventral stream engine that I'll
[346] talk about in a minute is a series of
[347] snapshots if you will of the world that
[350] looked like that now I hope that you
[352] could notice that you could still
[353] recognize one or more objects and each
[355] and every one of those images even
[356] though they're now kind of out of
[357] context and you didn't know what the
[358] sequence was yet you can still do that
[360] quite well and that problem is what
[362] we've been focused on that's called core
[364] object recognition central 10 degrees
[366] first 200 milliseconds of viewing tasks
[368] here report object category about say a
[370] central foreground object so essentially
[372] most all I'm going to tell you about
[373] today is about that problem but we don't
[375] think that's the end of the game that's
[376] just a way to get us a foothold on the
[378] problem of visual intelligence this
[380] problem is hard it was known to be hard
[382] from computer vision because objects
[384] like cars can produce an essentially
[386] infinite number of images like this car
[388] here and to do two things like pose size
[390] illumination background clutter and
[392] occlusion subordinate level variation
[393] but this is what makes the problem hard
[396] and so we like to engage that and the
[398] way we did this is by generating images
[400] where we often have a single
[401] rendered foreground object on a non
[403] related but naturalistic background and
[405] we can then generate a lot of images
[407] this way you can kind of like this and
[409] they might look like something out of a
[411] horror movie like this so um you can
[413] still quickly recognize that this is
[414] like a face or a head even though this
[416] is again something you'd be unlikely to
[418] typically see these kind of images
[420] brought computer vision systems to their
[422] knees yet you're easily able to do this
[424] this was in 2008 or so we could show we
[426] could crush all the computer vision
[427] systems just by that simple kind of
[429] image generation process and so we use
[432] this you here's an example of you just
[434] showing that you can do it yourself so
[435] okay there was an image in which ways
[436] you see I hope you noticed it was that
[438] not even telling you what's coming up I
[439] hope you notice you saw a bird and not
[441] an elephant okay so that's just a
[443] operationalized version of what I
[444] introduced and again around 2009 here's
[446] machine performance at high object
[449] uncertainty and here's human performance
[451] it shows a little bit of fall-off but
[452] humans are much better than machines in
[454] 2009 at doing this problem again this
[456] face is again what we call core
[458] recognition okay so back to reverse
[460] engineering
[461] so here's primates this is the one we
[462] don't understand the human primate we
[464] want to understand ourselves that's the
[466] mission here and um well but we want to
[468] go in now we got to measure I said I
[469] measure a bunch of internal stuff not
[471] just behavior but let's do this reverse
[473] engineering approach so here's where my
[474] lab takes advantage of the rhesus monkey
[476] system there's some rhesus monkey shown
[478] here one of the reasons we like to do
[480] this is that these organisms can easily
[483] do the same tasks that that you were
[485] just doing and here's an animal doing it
[486] in his home caged happily triggering a
[488] new image and then choosing which of the
[490] objects that saw in the image many many
[493] dozens of interleaved object recognition
[494] casts that are sort of randomly
[496] interleaved trial by trial you get lots
[498] of behavioral data this way and when you
[500] plot the behavioral data this is just
[501] that one grain of resolution this is for
[504] one primate species and the other and
[506] these are the difficulty patterns in
[508] d-prime units red means challenging so
[511] tanks are often confused with trucks and
[512] blue means it's sort of relatively easy
[514] to discriminate objects so look these
[516] patterns are not something that emerge
[517] out of pixel models or simple visual
[519] representations yet both of these
[521] primate species produce these patterns
[522] I'm not going to tell you which is which
[524] because the main point is that you we
[525] can't tell the difference here that
[526] monkeys and humans in terms of
[528] discriminating basic level objects are
[530] statistically indistinguishable and that
[533] means for us it gives us lice in
[535] to go in and start measuring the
[536] internal components to say how do you
[538] actually accomplish this task so now
[539] we're gonna measure the primate system
[541] components in a rhesus monkey and
[543] hopefully that gives us strong inference
[544] on human vision
[545] okay so decades of neuroscience has
[548] already provided us with lots of
[549] constraints on this problem we know
[551] about the ventral visual processing
[552] stream that's critically important for
[554] instance lesions in the top of the
[556] stream called in for temporal cortex
[557] produce deficits and recognition and
[560] then in the non-human primate and we
[562] like to lay this out as a series of kind
[564] of this is just a kind of conceptual
[566] space of neurons here millions of
[568] neurons in each area where we know
[570] something about the feed-forward anatomy
[571] the feedback Anatomy and the recurrent
[573] Anatomy they're just roughly illustrated
[575] just schematically with these arrows
[576] here um we also know a lot about the
[578] physiology and again this is all work
[580] well before my lab even started we know
[582] a lot about the physiology of the
[583] ventral visual stream we know for
[585] instance that there's a retinotopic map
[586] of course on the back of the retina here
[588] in the retinal ganglion cells and then
[589] continuing retinotopic maps all along
[592] here we know that there's local
[593] processing which is tiled across the
[595] visual field and much more that we know
[596] that I'll mention a bit more later ok so
[598] we know a lot about this system and but
[601] what you think's going on for a question
[602] like the one I showed you of being able
[604] to do core recognition is that when an
[605] image comes up like this when it your
[607] your brain just captures an image at the
[609] back of the retina it rapidly transforms
[611] this and I'll say an approximately first
[613] feed-forward pass just approximately
[616] again this is a schematic to a new
[617] population pattern of activity in i.t
[620] cortex here which is illustrated by
[622] these red dots so you this image evokes
[624] this pattern new image of Oaks a new
[626] pattern and these patterns in I T that
[628] are not photographs but some transformed
[630] versions of the input pattern the input
[632] pixel pattern can follow along in your
[634] ITU with a lag of about 150 milliseconds
[637] as you watch this video here and we
[639] think those that ability is what
[641] underlies these patterns under liability
[643] to do the thing I showed you at the
[644] beginning to say I saw a person I saw a
[646] sign I saw a Yoda okay so these are if
[649] you want to now get into the physiology
[651] we go in and record the spikes in a
[653] monkey and this is just it show those of
[655] you who are not used to neural data on
[657] what this looks like so each action each
[659] line here is an action potential
[661] recorded in an IT neuron in a monkey to
[663] in response to four different images and
[665] these these rows are different repeated
[667] trials and this is just to give you a
[668] feel for them
[669] elemental data that we are trying to
[671] measure and and try to predict so these
[673] are different IT sites respond as you
[675] can see the different images and I want
[677] to really draw here you to the point of
[678] the way we think about analyzing this
[680] data on first pass which is just to
[681] average over the trial reps an average
[683] often across a time window those
[685] parameters especially the timing
[687] perimeters are very interesting to us
[688] but for now I'll just going to tell you
[690] just think about this as averaging these
[691] little spiking times into one number so
[694] you're getting one number out of each of
[695] these images for this particular IT site
[698] and that's just an example neuron and
[700] it.4 for images one example neuron so
[703] i'm with work of my colleagues some of
[706] whom are in this room we scaled up our
[707] ability to record from the monkey with
[709] array recordings often now multiple
[713] arrays implanted simultaneously in the
[714] animal to record while they're doing
[716] awake behaving a performance of pass or
[718] just visual fixation and this allowed us
[720] to dramatically increase the amount of
[722] data both images and channels that we
[725] can get a per day and again this started
[727] almost 10 years ago now so when we take
[731] those data and analyze them in the way I
[732] just showed you a recount spikes again
[734] this is just a first pass of the data
[736] you can just think of now here's a bunch
[737] of recorded IT neurons and typically now
[740] our pools of neurons are hundreds in
[742] each animal and thousands if we pool
[743] monkeys together
[744] so these RIT neurons here and there's a
[746] response like I showed you earlier now
[748] we're looking at a population of neurons
[749] not one neuron in response to one image
[752] so you're seeing you know three spikes
[753] 12 spikes on the amount of response is
[756] just indicated here by color okay this
[758] is just again orient you to the data so
[760] notice this is just one image of course
[761] we collect many images here's eight
[763] images before I showed you four and
[764] these are now these complex images that
[766] I showed you at the beginning um so we
[769] don't just collect eight but these
[770] methods allow us to collect thousands of
[772] images so we end up with these very
[773] large data volumes that look like this
[775] that we can use to then constrain our
[777] modeling efforts so that's giving you a
[779] feel for the data we also for the
[781] aficionados point out that we measure
[782] these at very high resolution so 5050
[784] high signal-to-noise so 50 repetitions
[786] each to get a sense of what this neuron
[789] really responds to on average for each
[791] image okay so there's those kind of
[793] that's the kind of data that we get and
[795] then remember those behavioral data that
[797] I showed you that both primates have us
[799] and this primate that's shown here and
[801] one of the
[801] things that we showed over the last
[802] decade and we are these folks here at
[805] the most recent work is that you can
[806] take simple linear decoders train them
[809] up on a bit of data and accurately
[810] predict the performance on held out
[812] images and reduce these behavioral
[814] patterns so in this sense this is
[815] already one turn of that reverse
[817] engineering cycle that you can predict
[819] things you can build a model that
[820] predicts that the bottom line is this is
[822] a powerful set of features here just a
[824] linear transform needed to actually
[825] produce the behavioral performance that
[827] we see in both animals the specific
[829] parameters are that transform of course
[831] and interesting to neuroscience and
[832] they're important in lots of ways and if
[834] you think about things like BMI but I'm
[835] not going to talk about them today but
[837] those details matter more than just
[838] saying IT explains behavior so but I
[841] want to talk about now is that the AIT
[843] feature set you can think of it as the
[845] penultimate product of the brains
[846] algorithm for core recognition the
[848] ultimate product is of course the
[850] delivery of the behavior but so you can
[852] think of this as very close to being
[853] sufficient basically computationally to
[855] support the behavior so that's then a
[857] set up to ask for us the kind of harder
[860] questions in a way which is how are
[861] these features evolved developed learned
[863] to reach this powerful adult endpoint
[866] that relates to the talk you just heard
[867] from yawn do direct perturbations of
[870] these individual neurons cause
[871] perceptual changes that are predicted by
[873] these models that's these are ongoing
[875] lines of questions for us neither of
[877] which I'm gonna tell you about today
[878] what I will tell you about is this more
[880] important question which we've been
[881] working on for the last decade which is
[883] how do the IT features computed from the
[885] image similarly what are the
[887] intermediate features along the ventral
[889] stream these are essentially the same
[890] question okay and I'm gonna just give
[892] you a again an overview tour of that
[894] work so what we did is not just measure
[896] things about IT like that big block of
[898] data I just showed you but now let's
[900] build some models under those
[901] constraints okay so the models that I'm
[904] gonna show you they take as their input
[906] not this whole image and then try to do
[908] the task that's something that we and
[909] our collaborators are working on next
[911] for now just think of these models as
[913] taking an image like this one and
[915] processing it to something that's
[917] sufficient to support recognition so
[919] again forward by four degrees roughly
[921] central 10 degrees and these models they
[924] don't just come out of the blue they
[925] were inspired again by decades of
[927] neuroscience work that I alluded to
[929] already some of the key items that turn
[931] out to be important are listed here from
[934] neuroscience and again these is not our
[935] labs work this is decades of work prior
[937] to us this led to a series of models the
[940] first Fukushima in 1980 a first kind of
[943] kind of convolutional neural network
[945] that implemented some of these ideas in
[946] the context of doing visual recognition
[948] Tommy Poggio worked on this in the H max
[950] class of models my lab worked on this
[953] and sort of extended class doing GPU
[955] search through this model space and this
[957] was a Dave Cox and Nicolas Pinto and
[959] then I want to tell you about a model
[960] family that we worked on that was driven
[963] by Dan yemen's and a postdoc at a time
[965] in the lab at haha a graduate student we
[967] call this model HMO but it doesn't
[969] matter the specifics don't matter it's
[970] the general ideas that came from this
[972] that I hope that you will remember okay
[974] so um
[975] HMO was a model that was built by us to
[977] try to just say hey let's kind of use
[980] those constraints and we got these like
[982] layers within the visual system v1 v2 v4
[984] IT and those are already inspired by
[987] neuroscience so we were happy to be
[989] working with so-called deep networks
[990] because we were looking at a deep
[992] network and we knew from the work of
[995] many people again that there were
[996] different filter types in v1 which are
[998] illustrated here by these forward planes
[1000] those are these are supposed to be
[1001] sheets of simulated artificial neurons
[1003] now they don't show you the individual
[1005] neurons so think of these four types as
[1006] four types of filters like four types of
[1008] orientations and this these these
[1011] neurons in here they're not they're not
[1013] just kind of pulled out of the blue
[1014] again you they're doing linear
[1015] operations with some non-linearity and
[1017] often with some normalization gain
[1019] control and again these are ideas that
[1020] already existed again many of the folks
[1022] in this room but Matteo and David and
[1025] also I'm Tony mob ssin and others kind
[1027] of inspired these ideas and those are
[1028] implemented in here as well so really
[1030] we're just putting into the basket here
[1032] things that we roughly thought were true
[1034] based on the data that others had
[1036] already obtained um and then we applied
[1038] these kind of models to try to solve the
[1040] task I showed you which is to be able to
[1042] recognize objects across transformation
[1044] so we did this by generating objects
[1046] under transformations placing them on
[1048] random backgrounds as I showed you
[1049] earlier and try to sort of get a system
[1051] to solve that task now how do we get the
[1053] system to try to solve that task we have
[1055] architectural constraints here again
[1057] here only you'll essentially feed for
[1058] with a little bit of feedback
[1059] architectural constraints and then we
[1062] use something that I think is completely
[1063] um well maybe Yahshua's in the room so I
[1065] know if I just say too strong but this
[1066] is not what we thought of is biological
[1069] so on we just used applied math and
[1071] Peters science tricks to tune the
[1073] parameters for us they were hyper
[1074] parameter tuning now more recently
[1077] gradient descent which is the more
[1078] common way to train these so-called deep
[1080] networks I don't I don't want to dwell
[1082] on this other than say use engineering
[1084] to get this model family down to a
[1086] specific model that can perform this
[1087] task
[1088] we're not fitting any neurons when we do
[1090] this we're just optimizing within an
[1092] architectural space when you do this
[1094] what's really remarkable is that you can
[1095] then go ahead and compare these
[1096] artificial neurons to the actual neurons
[1098] we record in the brain and what we find
[1101] when we compare first of all I want to
[1102] say it's not like I expect an individual
[1104] IT neuron to pop out here that's gonna
[1107] match an IT neuron here we ask an
[1109] individual IT neurons fit in a set on a
[1111] basis set where there's a regression
[1113] from these artificial neurons on to this
[1115] neuron as if so that so that this just
[1118] lives in the spanning space of this here
[1119] and we can of course compare each of
[1122] these we can ask does v1 fit IT doesn't
[1124] be to fit IT and so forth of course we
[1126] do all that but so here's what you find
[1128] is that again you get this remarkable
[1130] ability to predict these complicated
[1132] responses and IT so here's one of these
[1134] IT neurons that we had previously
[1136] recorded this is its response now to
[1138] those thousands of images that I'm
[1140] showing you here and you grew them by
[1142] category this is not time I hope you can
[1144] see this at the bottom these are just
[1146] images of animals bows chairs and here's
[1148] some example images of chairs here so
[1150] this is the category chairs and you
[1152] could roughly call this a chair neuron
[1153] but the structure of the neuron is much
[1155] more interesting and it's response than
[1156] just saying it's a chair neuron but
[1158] what's remarkable is that here's the red
[1160] line prediction from that this is the
[1162] HMO model a regress to predict these
[1164] images it's never seen these images had
[1166] never even seen these objects yet it can
[1168] make this prediction of what this
[1169] neurons going to do for these images and
[1172] this was actually quite remarkable to us
[1173] that with this procedure we could get
[1176] things that could predict quite well
[1177] here's a so-called face neuron it kind
[1179] of responds on average more two faces
[1181] here's some face examples but you can
[1183] see it's more interesting than just
[1184] calling it a face neuron something else
[1186] is going on that's more subtle and you
[1188] could see it predicts it again
[1189] quite well okay so overall this was what
[1192] was impressive to us is that you just
[1194] kind of had these models that would
[1195] produce a very high explained variance
[1198] so of you know about 50% of the
[1199] explainable variance explained by these
[1201] models here's a v4 in
[1203] it looks even more complicated you can't
[1205] call it a chair or a face neuron it has
[1207] these crazy responses in response to
[1209] many images some examples shown here
[1210] remember V 4 is the input to I T and
[1213] here's the model predictions in red out
[1215] of different layers and I hope you can
[1217] kind of see that this middle layer 3
[1219] actually provides the best predictor of
[1220] this V 4 neuron again remember we did
[1223] not optimized for V 4 or I T we just
[1225] were trying to optimize within a space
[1226] to explain it to produce a task that we
[1230] had picked out again hi explain variance
[1233] of these kind of models these are all
[1234] predictions I want to stress a mid-level
[1236] neurons they're not data fits to these
[1238] neurons ok and also these networks I've
[1241] often heard people say that oh you have
[1242] this network it predicts stuff but it's
[1243] just a black box this is the furthest
[1245] thing from a black box I can imagine
[1247] because um we know everything about it
[1249] we built it we can map its internals I
[1251] understand the goal of trying to
[1252] appreciate it there's simpler versions
[1254] of this and I think error will probably
[1255] talk about that but it is certainly not
[1257] a black box I want also highlight here
[1259] that we're doing this an IT but others
[1261] have done this more recently and things
[1264] like fMRI especially Nico's previous
[1266] court date Olivia Jack gallant and
[1267] jitinder Malick Justin Gardner these are
[1270] just examples of people have used this
[1271] comparative approach between training
[1273] these networks and comparing them here
[1275] often at the level of fMRI there's a
[1277] meta lesson here that I think is them
[1278] one of the most important things that
[1280] you should take from this if you don't
[1281] remember anything about v4 and I T and
[1283] that and this is I think the most
[1284] important thing for this conference here
[1286] is that if you think about performance
[1287] of these models what we did here is we
[1290] noticed that as you had models that were
[1292] higher performing so this is performing
[1294] on a recognition task and this is our
[1296] ability to predict something
[1297] neuroscientists care about in this case
[1298] it's IT prediction explain variance but
[1301] you have this is a family of models
[1303] these are deep neural networks they're
[1304] sampled off the deep CNN family here
[1306] were some older examples and what we had
[1308] done the way we think about it is and
[1310] you know roughly when we did this work
[1311] in around 2012 and that model I showed
[1313] you we kind of were able to get a model
[1315] to do better we're using those
[1316] engineering tricks and so that moved us
[1319] and the performance axis it also moved
[1320] us and explained variants axis so
[1322] there's this correlation that was
[1323] continuing between performance of models
[1326] and the ability to explain the internals
[1328] the so-called hidden units of the brain
[1330] so again a computer vision goal sort of
[1332] driving a neuroscience goal and and I
[1335] think that's a very interesting
[1336] intersection of F
[1337] field it makes you wonder as a
[1338] neuroscientist can we just sort of sit
[1340] back and say okay now we have these
[1343] models we're developing you know we'll
[1344] just wait for computer vision they'll
[1346] just kind of give us better models and
[1347] we'll just wait and then they'll have
[1348] models of the brain and we don't have to
[1349] do anything else right so that's not
[1352] probably gonna work but let me give you
[1354] a sense of it kind of works a little bit
[1355] so Alec's net this model came out right
[1357] around the time we were doing this work
[1358] and it kind of took over computer vision
[1361] right so it is this assumed now this was
[1363] computer vision working in parallel they
[1365] weren't trying to explain the brain yet
[1367] they had a model that started winning
[1368] the image net competition and now deep
[1369] CNS took over computer vision as you've
[1371] heard from many others and then beyond
[1373] vision then deep networks took over and
[1375] with folks like Joshua neon and others
[1377] they comply these things for all kinds
[1379] of things and so there's this whole deep
[1381] learning revolution but just coming back
[1383] to these visual models so here's that
[1385] plot I showed you earlier this is
[1387] computer vision performance now image
[1390] net performance and and this is that
[1392] neuroscience goal fit IT that I showed
[1394] you earlier this is kind of like those
[1395] blue dots I showed you a minute ago here
[1397] was the model we had in 2012 don't worry
[1399] about the unit's here but that was the
[1401] level we were at these were models we
[1402] later developed in her lab but at 2012
[1404] actually this model was even better at
[1406] fitting IT than our own model was and
[1409] they had this model was better at
[1410] imagenet too so it kind of continued
[1412] that same kind of trend and you see that
[1413] trend continued here that doing better
[1415] here leads to better predictive power
[1417] here maybe not at ceiling yet that's an
[1419] interesting discussion point but then we
[1421] look forward keep watching what's going
[1423] on with these models and I'm like this
[1424] cannot continue forever and this is
[1426] actually what we're observing is sort of
[1427] as these models are getting deeper and
[1429] deeper and deeper they're doing better
[1431] and better and better but they're not
[1432] fitting IT necessarily better if
[1434] anything they maybe serve drifting away
[1435] from explaining what's going on in the
[1437] brain okay
[1439] that's again there's clues in these
[1440] models that are still helpful I don't
[1442] want to imply they're not useful but
[1443] that's kind of what you see if you look
[1444] at this at the first glimpse one of
[1447] these things these models did accomplish
[1448] is they not they were able to sort of
[1450] explain something that I showed you
[1452] before was hard for models to explain
[1453] which is the behavioral patterns and
[1455] performance at this grain of object
[1457] resolution that I showed you a minute
[1458] ago in fact here's the humans the
[1460] monkeys remember I said they were the
[1461] same here's the deep CN n this happens
[1463] to be Inception they're all they're all
[1464] except should be three they're all very
[1466] similar to each other so they had
[1467] achieved this kind of benchmark here um
[1470] interestingly you think about these
[1472] models and this is this is just very
[1473] recent work I'll just flash up but you
[1474] is it um you should be able to use these
[1476] models to actually drive the neurons
[1479] better you should be able to do stuff
[1480] with them beyond saying they fit things
[1481] and this is using synthesis tricks this
[1484] is related to things that you may hear
[1485] about from arrows so here we're
[1486] synthesizing best stimuli for these
[1490] different neurons here this happens to
[1492] be in v4 and these are the folks that
[1493] did the work and again this is ongoing
[1495] work it's kind of cool that you've seen
[1496] the synthesis procedures but you get
[1498] these kind of different things for
[1499] different neurons and if you kind of
[1501] repeat with new seeds you see these kind
[1502] of visually look very similar to that
[1503] remember our goal is to see can we
[1505] actually drive this neuron better than
[1507] we had ever seen a drive before and so
[1509] here was the response of this neuron for
[1510] a bunch of those images I showed you
[1512] remember I said the models are
[1513] predicting quite well and that's this
[1514] correlation here but what was kind of
[1516] cool is that way these these predicted
[1518] things that drive it were actually way
[1519] up near that sort of high end of the
[1521] response so at least the first-order
[1523] these kind of synthesize things are sort
[1525] of suggesting these models are really on
[1526] to something and that they can even
[1528] predict things that are driving around
[1529] stronger I want to point it this is just
[1531] one example neuron this is preliminary
[1533] work none of this is published yet this
[1535] is ongoing work in the lab okay so a
[1537] summary of what I always sort of told
[1538] you is that we now have many decent
[1540] maybe say sufficient models of the
[1543] ventral stream processing not the
[1545] learning you've heard about that from
[1546] others and one of the ventral streams
[1548] key supportive behavior core recognition
[1550] so what do we do now so I have I think
[1552] five minutes now so I'm going to tell
[1553] you what we've been doing the last
[1554] recently so um you go back get some more
[1557] data
[1558] here's Co heated car we're measuring
[1559] more and more images even computer
[1561] vision images and um we scale up our
[1563] behavioral testing so we're kind of an
[1565] adversarial node we view our job as like
[1567] we're gonna beat up on these models and
[1568] show how they differ from the brain and
[1569] that's gonna drive the next generation
[1571] of brain like models so we get a lot of
[1573] behavioral data we try to get a lot of
[1574] neural data here's just looking at the
[1576] behavioral data now at the image grain
[1578] resolution this is image by image I
[1580] don't worry about the details other than
[1582] to say look humans and monkeys still
[1583] look very very similar to eyeball you
[1585] can see here here's a deep CNN it starts
[1587] to even though I showed you was passing
[1589] our behavioral test it's starting to
[1590] fail on these kind of comparisons here
[1592] and that's quantified here that all of
[1594] these deep CNN's they're now failing at
[1596] this higher stringency comparisons of
[1598] primate so these circuits are doing
[1599] something the brain is doing something
[1601] that these models are not yet doing
[1603] bananas visual recognition tasks and
[1605] these break these brain circuits are
[1607] outperforming for many of these images
[1609] each dot is an image these out so each
[1612] dot is an image this is performance for
[1613] computer vision and and and primates and
[1616] these are images where the computer
[1618] vision image systems like alex net and
[1620] others they don't get this images right
[1622] yet the monkeys and humans get them
[1623] right and these are images where both
[1625] species get them right and so we can
[1627] compare these we can call these
[1629] discovered adversarial images these are
[1631] the examples of some of them there's
[1633] nothing obvious that separates one from
[1634] the other except that computer vision is
[1636] failing and primates get these all right
[1638] easily um so I'm one of the things that
[1641] I want to show you that we've done just
[1642] briefly is that when you go in and you
[1644] can go to look in the brain to say what
[1645] differs between how the brain processes
[1647] these computer vision yet unsolved
[1649] images and these computer vision let's
[1650] call them solved indicated by these two
[1652] colors here we go into our usual trick
[1654] and record in the ventral visual stream
[1656] go record a bunch of neurons record the
[1658] population and ask can we decode what's
[1660] going on out of IT it's not obvious that
[1663] the brain and the level of IT and the
[1664] monkey will actually solve these hard
[1666] images but when we go and measure the
[1668] decoders so here's what we see
[1669] the decoders come and they actually go
[1671] ok this is a decode as a function of
[1673] time this is monkey level accuracy this
[1675] image comes in and the decodes just fine
[1678] at this time point here and here comes
[1681] another one of these easy images ok just
[1683] fine ok computer vision is fine on these
[1685] no problem it fits what I told you
[1686] earlier brain decodes it in I T ok but
[1689] now here's one of these hard images you
[1690] get this quite right just as accurate as
[1692] others I just showed you you report this
[1694] is a car if you were to do this task and
[1695] the brain what does it do well it
[1698] decodes it but it takes it a little bit
[1699] longer on the order of 30 milliseconds
[1701] on average to dis decode this image but
[1703] it reaches the level of performance and
[1705] I T so your brain rattles around a
[1706] little bit longer
[1707] subconsciously yet you get this done
[1709] here's a foreshortened image of a dog
[1711] same thing you get it done a little bit
[1713] later
[1713] notice I T neurons are responding here
[1715] it's not as if things aren't responding
[1717] so the information hasn't kind of become
[1719] fully explicit with regard to the
[1720] category here's a bunch of these images
[1722] we tested thousands here's a few
[1724] examples I want you to see the blue and
[1726] the red and that they're shifted from
[1728] each other so these images are solved by
[1730] the ventral visual stream which makes
[1732] sense given the behavior but they take
[1734] about 30 milliseconds longer to solve
[1736] them
[1737] and similarly it's interesting that
[1738] those deep nets that I showed you
[1740] predicting IT neurons they predict best
[1742] at the front part of the response of IT
[1744] this is now a function of time and their
[1746] ability to predict I T neurons and they
[1748] predict worse and worse the further you
[1750] look in the response and I'm not talking
[1751] seconds later just 30 milliseconds later
[1753] okay so these are all consistent with
[1756] the idea that feedback and recurrent
[1757] circuits are needed not only they needed
[1759] to better explain the brain and its
[1761] dynamics but also their performance
[1763] critical as shown the examples I've
[1765] shown here so um let me just sort of
[1768] sort of end by saying of course we want
[1770] to go back and sort of model this better
[1771] we've only really modeled as I alluded
[1773] to earlier essentially the feed-forward
[1774] aspect of the brain of course somebody
[1777] mentioned the last question there's
[1778] feedback that's not often incorporate in
[1780] these models and I know many people are
[1781] interested in this we and our
[1783] collaborators are trying to build these
[1785] models guided by the kinds of data that
[1787] I just showed you as well as performance
[1788] data and we think if we incorporate
[1790] these kind of connections correctly
[1791] we'll get performance out of these
[1793] systems relative to even current
[1795] computer vision system but even if we
[1796] don't we're gonna better understand how
[1798] the brain works okay so I'm gonna just
[1801] sort of end with a big picture that you
[1802] know it's at MIT and I think broadly
[1804] with this coalition the way we're
[1805] thinking about this is that science and
[1807] engineering have something to offer as
[1809] we're building models that contain parts
[1812] of neural elements essentially neural
[1813] networks science can offer its
[1815] discoveries these are hypotheses for us
[1817] engineering is really good at doing this
[1819] and these are also alternative
[1821] intelligent systems for them so this is
[1823] an exciting time right now for both of
[1826] these fields and I think this is broadly
[1827] AI machine learning and engineering as
[1829] we described it earlier and remind you
[1831] you've heard from others I'm talking
[1832] about core recognition this is just
[1834] scratching the surface of what we might
[1835] call broadly human intelligence and
[1837] maybe my last slide if Tony will allow
[1839] me is that you know we're talking about
[1841] neuroscience the brain and how it's
[1843] going to relate into AI but remember a
[1846] science and engineering based approach
[1848] an engineering understanding of the
[1849] brain has opportunities to transform
[1851] human education ameliorate brain
[1853] disorders these are not things we talked
[1854] about this conference and relate to just
[1856] understand ourselves it's the greatest
[1857] question of humankind if we can do it in
[1860] engineering terms it would be a most
[1863] amazing journey for us to all beyond and
[1865] I hope you join thank you
[1873] thank you Jim let's see there are two
[1876] questions on the aisle over there if I
[1878] could get mics over there in front and
[1881] behind dick I saw you and two questions
[1887] so first yesterday we heard from
[1889] standing on here that the global Nirvana
[1893] workspace theory predicts that the
[1895] prefrontal cortex is crucial for
[1897] conscious awareness so from Jung Hyung
[1899] since that call base your object
[1901] recognition which is presumably
[1902] conscious can be solved by the ventral
[1905] stream alone so I was wondering if you
[1907] could comment on that and second
[1908] quickest question is that the deep
[1910] Network is fated to me raw data averaged
[1913] across 50 repetitions so presumably
[1915] there is a lot of trial to try our
[1917] ability in the mirror data is something
[1920] that that is worth considering yes so
[1923] there's two different questions there so
[1924] the trial by travelled and I average
[1926] that and it's a great question we
[1927] average it because we're trying to think
[1928] of these as sort of feature processors
[1930] and we want to know their average
[1931] encoding in the image space and that's
[1934] why we do it there are important
[1936] questions of when I how many neurons you
[1938] need given the variability to actually
[1940] complete the task and we've addressed
[1942] those in the papers you need you know on
[1944] the orders of 50,000 neurons for linear
[1946] decodes and I didn't those are details
[1948] that you'll find in the papers others
[1950] are using the variability to try to get
[1952] inference on the circuit so you looking
[1954] at the trial by travel and how the
[1956] animal will perform that's not something
[1957] we've been doing here I think they're
[1959] ultimately trying to get to the same
[1960] thing which is the relationship between
[1961] the neural activity and the perception
[1964] or at least the behavior those are just
[1965] different approaches to the same
[1967] question we'd prefer to do it in a sort
[1968] of high us and our regime because we
[1970] care about image space in the sense that
[1971] machine learning people care about image
[1973] space more than the sort of detailed
[1974] noise about the system although the
[1976] brain has to worry about the trial by
[1977] traveler but and it's not necessarily
[1979] noise that's another debate in the field
[1980] ok that was your first question the
[1982] other one about consciousness I I don't
[1983] even really know if I can touch that
[1985] question I'm an engineer so I serve
[1986] define what are the behavioral outputs
[1988] what can I measure can I build models to
[1990] link them so to the extent you will give
[1992] me behavioral measurements that you
[1993] would call awareness then models better
[1996] predict them and you know but they're
[1997] going to be behavioral reports of some
[1999] kind
[1999] and if the model if you we could talk
[2002] offline about what kind of reports you
[2004] think should be predicted to satisfy
[2006] that criteria and of course even
[2008] prefrontal I showed him I don't want to
[2009] say prefrontal is not involved I mean
[2010] that I say briefly flashed up the notion
[2013] of recurrence I don't mean the
[2014] recurrence has to be even in the ventral
[2016] stream it could be prefrontal to IT
[2017] recurrence to support that again I
[2020] wouldn't call that awareness but just in
[2021] the context of the task that I was
[2023] showing you those are the kind of things
[2025] that were after now if we cool
[2026] prefrontal does it affect these kind of
[2028] decodes that are laid on i.t those are
[2030] the ongoing experiments so I hope that
[2032] sort of gets you a question answer the
[2042] brain cortex reaches it's great
[2054] questions so does it if the IT takes
[2056] three milliseconds longer to produce it
[2058] if you believe the decoding model I
[2059] imply that by t-then supports the
[2061] behavior it should show up in the
[2063] latency of the reaction time right and I
[2065] one of that is that the quick answer is
[2067] yes that is true on average and then you
[2070] could you know we we I didn't show you
[2072] those slides but it is true so even
[2074] though I say humans saw those images you
[2075] could say well they don't sell them
[2076] quite as quickly just behaviorally
[2079] observe I want to also point out that
[2080] that's an on average statement that I'm
[2082] making the 30 milliseconds right there's
[2084] as you saw in the data there's a lot of
[2086] overlap some of those TV images are
[2087] still solved quickly by the brain and we
[2089] think those detailed data on which
[2091] images are solved fast which are soft
[2093] slow which are in our data that's
[2095] actually the value of constraining the
[2097] models not telling you the modeler that
[2099] you need feedback and you should solve
[2100] these images later because mother's
[2102] already know that I mean you heard
[2103] several of them come up and say that
[2104] right what we nourish scientists have to
[2106] provide is high dimensional constraint
[2108] data that's harder for them to fit and
[2110] so I didn't talk about there but I'm
[2112] sort of you've given me the opportunity
[2113] to say that now dig so let's try to
[2117] close the loop with Yuans talk and just
[2120] focus on that 30 millisecond delay it's
[2123] one thing to show that it takes 30
[2125] milliseconds longer it's another thing
[2127] to show why it takes 30 milliseconds
[2129] longer whether it's due to Rick
[2132] or not and the difference between the
[2134] models how do you do that in theoretical
[2136] space and how do you do that in actual
[2139] biological space right okay another
[2141] great questions so this is that's
[2143] actually a question that's a little
[2144] easier to address in the theory space so
[2146] what it means in the theory space for us
[2148] is you build models with various ideas
[2150] of recurrence and see if you might
[2152] explain the results and the way I was
[2154] just describing not just can you solve
[2156] those images but do you see the same
[2157] kind of delays per image that you
[2160] observe in the data so that's
[2161] essentially hunting in the hypothesis
[2163] space of various model types
[2164] hopefully inspired by some of the ideas
[2167] you're hearing from others and
[2168] engineering in ml to constrain that a
[2170] bit as well so that's sort of coming at
[2172] it from one but just because the AI
[2173] system catches up on the 30 milliseconds
[2176] doesn't mean that it's doing the same
[2178] way that the human brain does yes so I'm
[2181] not care about that you might be just
[2183] trying to build a better mousetrap No
[2185] well no I think not care about it I care
[2187] about I care about both but I think we
[2188] should you know admit in the few that's
[2190] why I said beginning neuroscience is a
[2191] big tent I care about the spikes at some
[2194] point you know I'm glad somebody cares
[2195] about the channels I probably go on to a
[2198] different problems so they're important
[2199] to certain things I mentioned brain
[2201] disorders at the end but what we each
[2203] care about is a little bit at what level
[2204] of predictive power are we gaining so if
[2206] I can't fake the spikes then I'll say
[2207] there's still a problem here for us at
[2209] the let and that's kind of what a monkey
[2210] tools best for measure but we are from
[2212] the biology point of view trying to
[2214] silence those feet we're trying to use
[2215] basically viral and dreds tricks to
[2218] silence the connections the feedback
[2219] connection specifically to see if we can
[2221] sort of gain traction on are those
[2222] feedback circuits critical in the
[2224] biology sense of the monkey but still
[2226] our measure will be are we predicting
[2227] the spikes and the behavior better as we
[2229] develop the models like those are units
[2231] of prediction that we aim for because we
[2233] can't touch things like the channels or
[2235] other lower things that you or others
[2236] might be interested in
[2237] does I care about the channels today and
[2239] I mean I'm talking about at the higher
[2241] level of systems organization of v12 IT
[2245] in which layer and which recurrence and
[2248] general principles nothing about forget
[2251] about the biophysics we don't care about
[2254] that today
[2255] yeah okay well some people care about it
[2258] I don't know they may not be in this
[2259] room but the notion of principles is a
[2262] very long discussion and I think I think
[2264] I don't think I could answer it right
[2265] now I hope for some principles but short
[2268] of principles I want a predictive model
[2269] and what I want to predict is the spikes
[2270] all along the ventral stream at all time
[2272] points and hopefully that can be done
[2274] with principles I think arrows talk will
[2276] kind of speak to that but there's just
[2278] to be clear there's no guarantee there
[2280] there is a guarantee that humans can
[2282] build a model of this system I think
[2284] that will happen weather will have human
[2285] digestible principles is still to be
[2287] determined
[2288] yeah back by the door thank you very
[2291] much for the talk is very impressive
[2293] work and very inspiring my question is
[2295] pretty related to the previous one I was
[2297] wondering whether you looked at or you
[2298] try to fit these models through predicts
[2301] oscillations local potentials sequences
[2304] of spikes as opposed to just spike rate
[2307] at a given instance given that we've
[2309] seen over the years that these may
[2311] constitute important codes we haven't
[2316] done much in terms of predicting things
[2318] like you know L fps and others I I know
[2321] there are other groups working on that
[2322] using these deep networks to do that and
[2324] are having similar success as you saw I
[2328] mean this is a very fast thing we don't
[2330] think it's time for slow frequency
[2331] oscillations to be mattering much in
[2333] this behavior but you know we so we're
[2336] just not really that's not what we've
[2337] been focused on but I think I hope you
[2339] take the general approaches of building
[2341] models to predict the things of interest
[2343] could be done again that's just not our
[2344] measurement of prime interest in the
[2346] moment so similar to the last question
[2348] yeah Tony you cut me off whenever hmm
[2352] you tell me when to end I don't know
[2354] people times will tell you in the end if
[2355] there are no more Esther one more here
[2364] one question is whether the recurrences
[2367] back to the hippocampus when you look at
[2369] these images have I seen this one before
[2371] have I seen this place before
[2374] and rather than refreshing the current
[2378] image you may be comparing that instant
[2381] with the previous one and maybe even
[2384] have your subjects put a name on what
[2387] they're seeing so maybe maybe not saying
[2391] it but if your subject in the experiment
[2394] might you not be labeling the badges
[2398] well our subjects are monkeys so they
[2401] can't really say but they get where
[2403] they're given iconic choices I as I
[2405] showed you at the beginning to just
[2406] point to the dog or the cat or whatever
[2408] they think they saw it's a transform
[2410] version so I can't get them to say
[2412] things but you know cool things could
[2413] could it be related to loops through the
[2415] hippocampus I certainly could be
[2416] subcortical right all we're saying is
[2418] that there's a time lag right so on that
[2420] decode out of I T so we have an
[2422] observation but we don't really know the
[2424] circuit details to explain it yeah and
[2426] that relates to the last question and
[2428] hippocampus probably more than I don't
[2429] think it's probably one place right it's
[2431] an observation we need to extend our
[2433] networks in multiple ways to try to fit
[2435] that observation and our job is to make
[2437] it hard for modelers to fit it and we're
[2439] some of those modelers but others are as
[2440] well that's on the experimental side so
[2443] it's a great suggestion I just wish I
[2445] could tell you more but maybe in a
[2446] couple years yeah Thank You Jimmy okay
[2450] [Applause]
