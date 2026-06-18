---
schema_version: 1
id: yt-4j78w__YudU
type: youtube
title: 'Bruno Olshausen: Robust and efficient, probabilistic inference in sparse coding
  networks'
url: https://www.youtube.com/watch?v=4j78w__YudU
authors:
- Hirak Jyoti Kashyap
ingested_at: '2026-05-30T20:02:08Z'
content_hash: sha256:cc25f117cd183a2977b371604eefbd872dd647b900cdc29ecfeffee27fb703ba
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: Hirak Jyoti Kashyap
  channel_url: https://www.youtube.com/@hirakjyotikashyap6920
  duration_seconds: 2283
  caption_track: fetched
  snippet_count: 1199
filter:
  score: 0.78
---
[0] sir alsacin from uc berkeley and
[4] he will talk about robust and efficient
[6] probabilistic influence in sparse coding
[8] networks
[9] so bruno you can take it from here
[12] okay thanks a lot and you can hear me
[13] okay
[14] yes great
[16] uh well thanks iraq and others for uh
[19] organizing and putting this together
[21] uh and also for having me um i got a lot
[25] of the talks this morning and um i
[27] apologize for not being able to
[29] participate in the discussion a lot of
[30] interesting points came up i was tuning
[32] in uh but this being father's day uh i
[35] was driving my father to church uh
[38] and uh but tuning in and so uh anyways
[40] maybe we can revisit some of those um
[42] things later uh this after the
[44] discussion later too
[46] um
[47] but yeah so i'd like to tell you about
[48] some of our recent work on uh sparse
[51] coding which is a model of how visual
[53] information is encoded
[55] in the primary visual cortex
[57] and specifically these properties of
[59] robustness
[61] and how to do probabilistic inference
[64] efficiently and this is something i
[65] think we've made some recent
[67] inroads on
[68] and it's mainly the work of my students
[70] dylan payton who worked on the work i'll
[72] be telling you about on robustness uh to
[74] adversarial perturbations and michael
[77] fang
[78] who's a student who developed this
[80] model for doing a probabilistic sampling
[82] um in the model
[84] so
[85] um since uh
[87] uh
[88] hold on
[91] okay uh one of the advantages of uh
[94] going later in the program is that you
[96] can sort of uh in the context of other
[99] things that preceded you so there was a
[100] lot of talk in the morning about
[102] feedback and recurrent uh recurrent
[104] networks in the brain and so forth and
[106] so i want to begin by just kind of
[109] giving you a feel for why
[112] uh why feedback is probably so important
[114] the cortex
[116] and i think this is a property that's
[117] just not really been captured yet in any
[119] any artificial neural network out there
[122] um yet
[123] um and so so this is one example of that
[125] uh it's a it's a it's a what's called a
[127] puzzle picture due to dahlenbach from
[129] the 1950s
[131] and there's a figure in here there's a
[132] figure in this picture if you haven't
[134] seen it before most people don't see it
[135] initially
[136] uh there's a figure in here and you
[139] can't see it because it's kind of you
[140] know sort of taken in a somewhat uh
[142] ambiguous
[144] way
[144] uh and so one way of interrogating
[147] people what they see is to ask them to
[148] draw
[149] uh what they see um
[151] and uh in this particular example so for
[153] one per person who was asked to draw
[155] what they see this is what they what
[157] they drew in the lower right and so it's
[159] basically just kind of a veritable
[161] representation
[162] of the black and white contours um in in
[165] the scene
[167] okay so now i'll give you some hints
[168] about what's here uh it's uh it's an
[170] animal
[172] and specifically it's a cow
[176] and uh so
[177] maybe for a lot of you that's already
[178] enough to get it um and i'll just point
[180] with my mouse hopefully you can see my
[182] mouse but just uh so this is the head of
[184] the cow
[185] uh in this region here and there's an
[187] eye here there's another eye here and
[189] the snout down here
[191] um so so for most people that's usually
[194] enough for it to kick in
[195] and once it does it's a very strong
[197] three-dimensional perceptible cow and
[199] lots of detail emerges that wasn't sort
[202] of obvious before what was going on
[204] okay so now for this subject if you ask
[206] them to draw uh what they see is you can
[208] imagine the answer is going to be quite
[210] quite a bit different
[212] so now this is what they draw the image
[213] is exactly the same so the only thing
[216] that changed is something inside your
[218] head
[219] and i think what this importantly
[221] demonstrates is that
[223] a vision and all of perception really uh
[226] is a generative process okay so we're
[229] constantly with our brains this is what
[230] evolution designed us to do uh we're
[232] constantly building models of the world
[235] and we're explaining the incoming
[236] sensory data in terms of these models uh
[239] that we are that we're creating in our
[241] heads and in fact you know the data
[243] coming in is what supports those models
[245] and our ability to explain
[247] the data in terms of the model is what
[249] supports our belief in in in these
[251] models of what's happening in the world
[252] okay so this is really sort of uh
[254] somewhat of a different way of thinking
[256] about the vision problem rather than
[258] just you know casting it in terms of
[259] non-linear regression training inputs to
[261] outputs and doing and learning and all
[263] this stuff
[264] that you know trying to think of it as a
[266] process of model building and inference
[269] okay so that's the context of what maybe
[271] the work i'm going to be telling you
[272] here
[273] and uh
[275] so so this is one you know this is kind
[277] of where we can schematize the problem
[279] and by the way i just want to
[281] go back and illustrate and mention one
[283] thing that i think this also illustrates
[285] is the process of explaining away right
[287] and so so what that means is that for
[289] example some of these details before
[291] before you saw the 3d figure in here you
[293] probably just saw it as a loose
[294] collection of you know black and white
[296] contours right and you didn't really
[297] know what the difference between this
[298] and this is right but now that you know
[300] what's here you would probably attribute
[301] this boundary here to being a difference
[303] in reflectives and this boundary to
[305] being um due to three-dimensional uh the
[308] shape and the way that the shading is
[310] being generated by the light as it's
[312] cast upon this three-dimensional object
[314] okay and so when you say this is due to
[316] three-dimensional shading then you're
[317] also saying it's not or you don't need
[319] to explain it anymore in terms of
[320] reflectance and vice versa here if you
[323] explain that in terms of reflectance
[325] then there's no need to explain it in
[326] terms of three-dimensional shading and
[328] this is also a huge part of the kind of
[330] inference inferential processes
[332] going on in our brain any given time
[334] there's multiple explanations for what
[335] could be happening and you're trying to
[337] sort of rule in and rule out um these
[339] different possibilities okay and that's
[341] a process what's called explaining away
[342] in probabilistic models okay so we're
[344] gonna be saying more about that in a
[345] minute okay so this is one way of
[346] schematizing what's happening is we have
[348] the world on the left side uh uh you
[350] know electromagnetic waves that are
[353] being focused by the lens onto the back
[354] of the eye creating this image in the
[356] back of the retina which we just heard
[358] about in the previous talk
[359] uh and a whole array of photoreceptors
[361] sampling this so much
[363] and so the job of the brain then is to
[364] try to interpret all this all these
[366] pixel values coming in essentially from
[368] the retina and and to try to build some
[370] kind of internal model what it thinks is
[372] going on in the world
[374] uh so um how do we do that how do we
[376] approach this mathematically okay so the
[378] answer for many of us is using the
[380] framework of bayesian inference okay
[382] this is not my idea this is kind of a
[383] model idea that's been
[385] uh um you know sort of propagated in the
[387] field now for many many decades actually
[390] um and it since since hemholtz actually
[393] described as inference not bayesian
[394] inference but the bayesian inference
[396] sort of idea is a little more recent
[398] okay but so the idea is we can sort of
[400] think that what's going on the brain the
[402] brain basically has a model for how
[404] images are generated from
[405] three-dimensional causes in the world
[407] from lighting from reflectance from how
[409] light reflects off of objects and so
[410] forth that we have sort of somehow we
[412] have implicitly of a model some kind of
[414] a model in our brain of how
[416] how these things are happening and how
[418] this light might might be cast upon the
[419] retina at the same time we have a prior
[422] that tells us uh the relative
[423] probability of these different things
[425] being out there in the world so for
[426] example cows are more probable perhaps
[429] than other kinds of things that could
[430] explain
[431] that that grainy image
[433] okay so the job of inference then is to
[435] go backwards and to say okay given the
[437] image data given the image data what's
[439] what's going on in the world that's our
[440] hypothesis h about what's going on the
[442] role this is the posterior distribution
[444] the posterior probability that we're
[446] trying to develop inside our heads this
[447] is mathematically how you would frame
[449] the problem in terms of bayesian
[450] inference and what's interesting about
[452] this inferential process in terms of
[453] these graphical models is that when you
[455] formulate even when you formulate the
[456] model as a generative model going from
[458] right to left so the model is generating
[460] the data
[461] okay the inferential process
[463] inevitably involves this these this
[466] bi-directional flow of information where
[468] you have information propagating within
[470] layers of representation and between
[471] levels of representation this is just
[473] something that an unavoidably emerges
[476] from the process of inference in these
[477] bayesian models in the causal causal
[479] generative models okay and so of course
[482] you know the hypothesis is that uh maybe
[484] these these bi-directional flows of
[486] activity are what recurrent connections
[488] are doing in the brain horizontal
[490] recording connections within levels of
[492] representative areas and and and
[494] bi-directional
[496] connections between between levels of
[498] representation in the brain okay so
[500] that's the overall kind of thesis i'm
[501] going to push here
[503] and
[504] so how do we uh how do we sort of drill
[506] down on that and make it more specific
[507] in terms of uh in terms of the visual
[509] cortex well this is an insight that
[512] horace barlow had uh many years ago um
[515] and from a combination of just looking
[517] at the activity and cortex and what you
[519] see activity is fairly fairly silent
[521] only a small fraction of neurons seem to
[523] be
[523] firing
[524] in any given instance
[526] and also just looking at the
[527] dimensionality of the representation so
[529] this is an important anatomical fact
[531] of the input layer of cortex so layer
[533] four is the input layer you could sort
[534] of think of that as like the first layer
[536] of your neural network um here that's
[538] being or indicated by this bar here
[540] and you can just see from this diagram
[542] that the number of neurons in the input
[544] layer in in cortex receiving information
[546] from the lgn which is in turn relaying
[548] information from the retina
[550] um is vastly greater so you have many
[552] more neurons here in the input layer of
[553] cortex than you do
[555] uh you know wires coming in these are
[557] you could sort of again like these are
[558] pixels coming in or wires coming in from
[560] the lgm this is the grain of that
[562] representation okay
[563] so it's not doing dimensionality
[565] reduction by any by any means right
[567] that's what the retina is very good at
[568] doing it has in the retina by contrast
[570] we have a bottleneck we're trying to
[571] take the information from many cones
[574] and funnel it into many fewer retinal
[576] ganglion cells here's the exact opposite
[578] we're taking relatively few retinal
[580] ganglion cell fibers and we're
[582] vastly expanding that into a higher
[584] dimensional space okay so barlow reason
[587] that maybe what we're doing then is
[588] taking the input data and carving it up
[591] into a feature space and we're making it
[593] very sparse so these neurons here are
[595] very choosy
[596] and only a small handful are going to be
[598] firing depending on whether the patterns
[601] coming in from the input in any given
[603] moment in time match uh what that neuron
[606] is selected for
[607] okay so that's the idea that barlow
[609] proposed many years ago uh and uh
[612] together with david field in the in the
[613] 90s uh we developed this model the
[616] sparse coding model which is basically a
[618] linear jar to model this process how
[620] what sort of hypothesis for how v1 might
[622] be processing images um so the idea is
[625] that you know so what maybe v1 is trying
[627] to do is form a very simple generative
[630] model it doesn't have sort of models of
[631] cows and faces and 3d shapes and stuff
[634] it's just modeling images in terms of a
[636] simple dictionary of
[638] of shape features two-dimensional shape
[640] features the so-called gabor functions
[642] right
[643] uh and
[644] so that's what it's trying to do is fit
[645] this model to the incoming data at a
[647] given point in time
[648] uh
[650] and so so the so that again so then how
[653] if you just sort of work out how
[654] inference happens that model so we can
[656] impose sparsity through a prior over
[658] these coefficients a sub i uh that that
[661] makes them sparse this is just the
[662] linear generative model of the images
[664] and so when we work all that out and
[667] compute a posterior posterior
[668] distribution over these coefficients uh
[671] we that leads you to this following
[672] minimization problem down here and when
[675] you flush that as a neural circuit it
[677] leads you to this bi-directional flow of
[678] activity among these units so in other
[680] words it's saying it's not enough to
[682] simply
[683] for each of these units compute the
[684] inner product of its feature with the
[686] image and then send it to a threshold
[688] that's not enough you must necessarily
[690] talk to it there it has to be this
[692] communication between units to form the
[694] the right representation
[696] um of the image in terms of this model
[698] so that's illustrated here in terms of
[699] this neural circuit this is something we
[701] call lca or lateral i'm sorry uh the
[704] locally competitive algorithm that
[706] developed with chris chris rozelle
[708] a while back and uh
[710] and so this is a recurrent neural
[712] circuit it's recurrent inhibition so
[714] each of these units
[715] is computing the inner product between
[718] its dictionary element this phi sub i
[720] and the image
[721] and then that's fed into a threshold
[724] and then it's also getting inhibited by
[726] the outputs of all these other units
[728] and it feeds that basically the result
[730] of that process the inner product here
[732] plus the inhibition from its neighbors
[734] to that threshold and that's the uh
[736] that's the best resulting activity that
[738] coefficient and so basically what you're
[740] doing this is the dynamics over here
[741] it's exactly the same as a hopfield net
[743] by the way and uh it's very simple
[746] dynamics linear leaky integrator being
[748] driven by
[749] uh the the feed forward projection uh
[751] and getting inhibition from its
[753] neighbors and then going through a
[754] thresholding function g this little g is
[756] the thresholding function so these
[758] dynamics solve this minimization problem
[760] okay for doing bayesian inference
[763] on the image again in terms of a very
[764] simple dictionary of um
[768] features okay so that's the proposal is
[770] you have this very large population of
[772] neurons this is showing a learned
[774] population of features a dictionary for
[778] a 16 by 16 pixel image patch
[780] uh so each neuron is a different patch
[782] here what it's selected to the pattern
[784] that it's trying to uh find in the in
[786] the image or
[787] it's trying to explain the image in
[789] terms of these patterns
[790] uh and now if you take if if you if you
[793] give it a 16 by 16 image patch over here
[795] as input
[796] and just compute linear projections in
[798] other words if you just compute the
[799] inner product between the image and each
[801] of those dictionary elements i just
[803] showed you this is what you get so each
[805] each pixel here is just showing the
[806] resulting inner product for each of
[808] those patches we just looked at okay so
[810] you can see it's that that's not
[812] particularly sparse actually um so so
[814] there's a lot of sort of highly
[815] distributed activity and the result of
[817] this minimization problem trying to
[820] trying to solve that that problem to
[822] compute the the optimal coefficients
[824] just the ones that are needed results in
[826] this very much pruned set of activities
[828] which then allows you to reconstruct the
[830] image okay
[832] uh and so if we go back now and look at
[833] that dictionary which elements did it
[835] use to reconstruct this image you can
[837] see it has sort of something vertical
[838] here something horizontal here something
[839] horizontal here these are the features
[841] that it used so it zeroed out everything
[843] else everything else here just said look
[845] i don't need that and what told it that
[847] it doesn't need these things is that it
[849] could explain the image in terms of
[851] these other features so this was able to
[853] explain
[854] uh much of the pixel variants and so it
[856] didn't need the other ones and that's
[857] the purpose of these lateral and lateral
[859] interactions okay so this is the process
[861] of explaining away the result is that it
[864] gives you a much more interpretable
[866] representation rather than just
[867] delivering you the inner product which
[869] is actually very vague and ambiguous now
[872] it's making a much more meaningful
[873] statement it's saying look this feature
[875] here is contained in the image this
[877] feature here is contained in the image
[879] and these other things are not okay this
[880] is this is what i think the world is
[882] composed of okay so that's basically so
[884] it gives you a more meaningful
[885] representation so it's so it's actually
[887] a very sort of important um thing that
[890] we think is going to be an important
[891] ingredient a kind of important uh
[893] primitive possibly to incorporate into
[896] deep component models
[898] okay so so so west is good for um so i
[901] just sort of gave you some kind of hand
[903] wavy verbal explain sort of arguments
[905] there but but so dylan uh so was able to
[908] show that what this selectivity actually
[910] does is it helps protect against
[911] adversarial perturbations so as we know
[914] this is a big problem that that plagues
[916] deep deep confidence is that can be
[918] easily fooled by small perturbations in
[920] the image
[921] uh and and to to miscategorize things
[924] and this is something the field has been
[925] working a lot to on to understand and to
[927] figure out how to
[929] um how to make it go away
[931] and so we would argue this is this is
[933] happening because you basically you're
[935] these these networks are designed in a
[937] very ad hoc way okay by just computing
[939] linear projection so let's just look at
[941] that right if you just think about think
[943] of these arrows here as weight vectors
[945] so this arrow here
[947] corresponds to the weight vector of one
[948] neuron and this arrow here corresponds
[950] to the weight vector of another neuron
[952] in the space so this is just showing you
[953] the input space the in the space of
[954] possible
[956] input stimuli let's say for again for a
[958] 16 by 16 image patch so we're in a 256
[961] dimensional space okay so this is the
[963] weight vector of one neuron that's the
[964] weight vector of another on okay so now
[966] if we want to look at the set of stimuli
[968] that activate this neuron with this
[970] weight vector here
[972] then
[973] then
[974] that would correspond to these these
[976] colored lines and so what these colored
[978] lines are showing you the iso response
[979] contour that is the set of stimuli that
[982] are going to give the exact same
[983] response from that neuron okay so if you
[985] go to any point along this line that
[987] gives the same linear projection onto
[989] that weight vector that's going to give
[991] you us the same response from that
[993] neuron okay
[995] um so as you can see it's not very
[996] selective right a linear neuron is not a
[998] very selective mechanism it's going to
[999] respond to a lot of things that are not
[1001] even aligned to the to the direction of
[1003] that weight vector so when we look at a
[1005] receptive field of a neuron we see this
[1007] gabor function looks oriented we sort of
[1009] think oh wow that's how the neuron gets
[1011] orientation selectivity it turns out
[1013] that's not how it does it right that's
[1014] not good enough and i'll show example of
[1016] that in a second okay
[1018] and uh so so so if you wanted to fool
[1021] this this kind of system and by the way
[1022] just thresholding is not going to help
[1024] you here if you just take linear
[1025] projection and threshold
[1026] like through a relu or something that's
[1028] not going to solve this problem okay so
[1030] if you wanted to fool this system you
[1032] could very easily do it let's say if i
[1033] give a stimulus here
[1034] and i want to make this neuron respond
[1036] more but then i just push out this
[1037] direction so i'm pushing out into a part
[1039] of the space that has nothing to do with
[1040] this neuron selectivity
[1042] what this what this neuron appears to be
[1044] selected for and that's going to
[1046] increase the the response to that neuron
[1047] okay by contrast when you do this
[1050] process of explaining away through the
[1052] sparse coding model when you actually
[1053] solve this inference problem when you
[1055] cast vision perception as an inference
[1057] problem even in the in the context of v1
[1060] i'm thinking about these these these
[1061] neurons with these dictionaries
[1064] this is what it does it basically curves
[1065] these iso response contours why is it
[1067] doing this well if again let's just
[1069] consider these two neurons right by the
[1072] time the stimulus moves over here so
[1074] that it's aligned with this neuron's
[1075] weight factor well then this neuron
[1077] doesn't need to respond anymore it's
[1078] basically been explained away because
[1080] that's going to turn this neuron on so
[1082] anything over here is going to get
[1084] inhibited by uh
[1086] by uh by this neuron here on on this
[1089] neuron's response okay so so what that's
[1092] going to end up doing for this neuron
[1093] here with this weight vector is just
[1095] going to make it much more selective
[1097] than these kind of iso-response
[1098] contoured spurs it could basically curve
[1100] these iso-response contours to make it
[1102] more selective to things that are
[1103] aligned with this
[1105] with this weight vector
[1106] and and so here's what would happen and
[1108] sort of an example of uh sort of an
[1110] adversarial attack
[1112] um let's say uh you are uh you know
[1115] you're you start with the stimulus which
[1116] is a one here uh the digit one and this
[1119] is and they what they did here is a
[1120] simple simulation where you use sparse
[1122] coding on the first layer and a simple
[1124] uh classifier in in the second layer to
[1127] do mnist recognition and so if you give
[1129] it a digit one here for example this
[1131] point in the space and now you try to
[1133] fool it into thinking it's a three
[1136] well it turns out really the only way
[1139] you can do that is you have to sort of
[1140] make that digit look more like a three
[1143] right it's hard to find in a relevant
[1144] part of the space to push out into just
[1147] following these iso response contours so
[1148] these curved iso response contours end
[1151] up moving you along director directions
[1154] that are more consistent with the thing
[1156] you're trying to fool and so it's harder
[1157] to fool okay so in order to fool to
[1159] think as a three you kind of have to
[1160] make it look more like a three
[1162] um so this is kind of a neat
[1164] result they got and it was uh published
[1166] in journal of vision in in 2020 which i
[1169] can refer you to for
[1170] uh more details
[1172] and here's just maybe an another simple
[1174] example to give some intuition why
[1177] when i say a linear mechanism something
[1178] that just simply computes inner product
[1180] is a very weak mechanism here's an
[1182] example of that right so these two
[1184] stimuli these two bars here versus these
[1186] two dots are going to give the exact
[1188] same response from this gabor function
[1190] the reason why is because here they're
[1191] relatively low contrast you have four
[1193] pixels in a row which are in the
[1194] excitatory flank and four pixels around
[1196] the inhibitory flank versus just one
[1198] pixel here and one pixel here that are
[1200] brighter right
[1202] uh but so here's the stimulus this
[1203] completely you know it doesn't really
[1204] have anything to do with anything we
[1206] would call this oriented right but it's
[1208] going to exhibit the exact same response
[1210] from this neuron okay and so again so if
[1213] you're just computing projection it's
[1214] going to be easy to be fooled by that
[1216] but in the context of doing inference
[1218] and explaining away then these these
[1220] representations become more meaningful
[1222] and so we would argue this kind of
[1224] recurrent lateral inhibition
[1226] is uh it's a it's an important primitive
[1228] of neural computation it's there in v1
[1230] we know i'm not saying it's doing my
[1232] model but we know that right there in
[1234] layer four v1 there's a huge inhibitory
[1236] uh into a neuron in a network
[1239] and uh so this is potentially one thing
[1241] i would offer that this is my hypothesis
[1243] of what that network is doing at least
[1245] right and so this is something we find
[1248] all over the brain and uh maybe this is
[1250] sort of a useful primitive we can start
[1252] putting in our networks and and to make
[1253] them more uh robust
[1255] okay and uh there's more to say about
[1257] that recurrent computation echoing some
[1259] of the uh comments of time
[1262] kreitzman this morning but um
[1265] but maybe i'll save that till later but
[1267] um okay
[1269] so there's another question here i want
[1270] to address which is how to do all this
[1272] efficiently and so this is another thing
[1274] i think we have to wrap our heads around
[1276] if we're going to
[1277] uh design systems that you know even
[1280] remotely approach the ability of
[1281] biological systems to do vision is how
[1284] do they do this with such low energy and
[1286] such small form factors
[1288] okay so i think maybe the thinking
[1289] that's going on a lot of people's heads
[1291] is that well i don't need to worry about
[1293] that now i'm just going to use my gpu
[1295] it's going to consume lots of power i'll
[1296] just get my simulation working and then
[1298] when i finally get everything working
[1300] then i can worry about making it like
[1301] low energy and small form factor
[1303] and uh well probably doesn't work like
[1305] that
[1306] right you probably have to sort of think
[1307] about those at the same time
[1309] and uh and so this is what biology had
[1312] to do in designing the system so this is
[1313] just i'm just contrasting two things
[1315] together you know the jumping spider on
[1317] the right this is one millimeter you
[1319] know it has very low energy consumption
[1321] uh and it has does remarkable piece of
[1324] vision it can do 3d vision it can
[1325] navigate in the world it can hunt prey
[1327] with his eyes it moves his eyes back and
[1329] forth it does active vision i mean it's
[1331] truly remarkable if we could simulate
[1333] the jumping spider on a supercomputer i
[1335] think we would all be very happy we'd be
[1337] thrilled right but we can't we don't
[1339] know how to do this this really
[1340] still lies beyond our ability to do this
[1343] okay here's the super computer on the
[1345] left right in berkeley just up the hill
[1347] we have the lawrence berkeley lab uh a
[1349] five megawatt supercomputer okay and i i
[1352] would challenge anybody to simulate a
[1354] jumping spider on this computer i don't
[1355] think it's gonna work
[1357] uh and so you know this just kind of
[1359] to me is a huge explanatory gap in our
[1361] understanding of biology but it also
[1363] points the way to opportunity
[1365] uh that as engineers we should be
[1367] thinking maybe differently about how to
[1369] design these systems that if you need
[1371] lots of gpus that are power hungry maybe
[1373] you're on the wrong path
[1375] we should be thinking about designs and
[1376] algorithms that can work at this this
[1378] kind of form factor and this kind of
[1380] energy consumption and if you don't see
[1382] a road map
[1383] from your algorithm to that then
[1385] probably you're barking at the wrong
[1386] tree
[1387] um and so so some hints for that what
[1390] you know how to design these systems i
[1392] is trying in terms of you know these
[1394] biological principles there's this
[1396] beautiful book that came out recently
[1397] from peter sterling and simon laflin i'd
[1399] like to point everybody too
[1401] uh this is really sort of like an
[1403] engineering engineering engineer's
[1404] handbook for how to design things at low
[1407] energy and form factor uh
[1409] in terms of the brain is doing so
[1410] they're really unraveling and revealing
[1412] a lot of these principles that the brain
[1413] is using very specifically this is this
[1415] looks like i figured like a very general
[1416] list but what they do in this book is
[1417] they go into very specific examples and
[1420] retinal circuits in the cerebellum you
[1421] name it all over the brain and sort of
[1423] revealing how
[1425] how neural circuits are trading off snr
[1428] signal to noise ratio with volume with
[1430] speed with power um and so forth uh
[1433] requirements um in in the brain so it's
[1435] really i think an eye-opening
[1437] eye-opening read
[1438] and so so going back to this thing you
[1440] know we're so i'm sort of proposing that
[1442] that the brain is doing a probabilistic
[1443] inference well how are we going to do
[1445] that efficiently um
[1447] and and again i think one of the
[1448] important parts that one of the
[1449] important things to remember here is
[1451] that we actually want to represent a
[1452] posterior distribution so in what i just
[1454] showed you with the sparse coding model
[1456] it's actually not representing the whole
[1457] distribution it's just finding one point
[1459] of that distribution it's going to the
[1460] maximum just finding the most probable
[1462] explanation but that's rarely what we
[1464] really want to do in these probabilistic
[1466] models usually what we want to be able
[1467] to do is sample or somehow represent
[1469] these multimodal distributions okay
[1472] multiple hypotheses and their different
[1473] probabilities simultaneously
[1475] and so uh so over the past you know
[1478] looks like you know maybe almost two
[1479] decades
[1480] uh there's a there's been this kind of
[1482] uh you know sort of uh body of work
[1483] emerging uh starting with uh this work
[1486] by patrick hoyer and apple hooverinin
[1488] uh where um we're proposing this idea
[1491] that maybe
[1492] maybe this neural variability this what
[1494] appears to be noise in the brain these
[1496] apparent stochasticity responses in the
[1498] brain
[1499] maybe that's part of a strategy for
[1501] sampling from probability distributions
[1503] okay so see these are you know a lot of
[1505] papers so this is not my novel idea but
[1507] we just sort of advanced this idea more
[1509] recently in in terms of this the model
[1511] of sparse coding
[1513] and so and so uh i'm running out of time
[1516] so i think i'm gonna probably just zip
[1517] ahead and give you the about this not
[1520] head but i'm just gonna maybe end with
[1521] this point here this is really the key
[1523] idea
[1524] is that
[1525] that if you represent a probability
[1527] distribution as a boltzmann distribution
[1529] for example if you have some like these
[1530] posterior i'm talking about over the
[1532] coefficient values if you can represent
[1534] that
[1534] as the as e to some energy function um
[1538] then what you want to do what we're
[1540] doing right now in sparse coding is
[1541] we're finding the minimum energy state
[1543] okay we're just going to this point here
[1545] but what we really want to do is sample
[1547] here
[1548] and what's kind of remarkable so there's
[1549] this thing called logibond dynamics and
[1550] what it says is that
[1552] if you want to sample from this
[1554] distribution
[1555] then what you should do
[1557] is not just grade into sense so the way
[1559] we're doing it now is not unlike this
[1560] it's very close to doing gradient
[1562] descent that lca okay it's not exactly
[1564] great intercept but it's very close to
[1565] this okay
[1566] so we could design analog hardware not
[1569] you know other people have actually we
[1570] could design efficient analog hardware
[1572] that computes this
[1573] very efficiently people have implemented
[1575] on luigi as well that's not analog but
[1577] but people have implemented this on wii
[1578] okay so we can design hardware that does
[1580] this
[1582] uh very well
[1583] but but this is what's really remarkable
[1585] it says well you look if you want to
[1586] actually sample from that distribution
[1588] then just do what you've already do do
[1590] what you're already doing
[1591] and just add noise
[1593] okay
[1594] so this is just just amazing right it's
[1596] mine kind of mind-blowing
[1598] so when i sort of learned about this
[1599] stuff and and uh and so it's saying look
[1601] just build circuits that do this if you
[1603] already have a circuit that does this
[1604] then just simply inject noise into it
[1606] gaussian iid noise okay
[1609] and you will be sampling from this
[1610] distribution this is actually what you
[1612] want to do you don't actually want to go
[1613] to the bottom and stay here you actually
[1615] want to sample from that distribution
[1617] okay
[1618] and so so this recent paper we have from
[1620] our group and that that i just i just uh
[1623] gave the reference earlier so if it's
[1624] the work by mike michael fang i just
[1625] it's going to be coming out neural
[1627] computation shortly um i'm sorry i don't
[1629] have time to go
[1630] and put too much detail in here
[1632] obviously but but what this allows us to
[1635] do now for the first time
[1636] is learn parameters of the prior in the
[1638] sparse coding model that we weren't able
[1640] to do before okay so like that parameter
[1642] lambda that goes in front of the cost
[1644] function uh usually that's a that's a
[1646] parameter we sort of uh we specify in
[1649] advance we just hold it there now we can
[1651] learn that parameter we can learn the
[1652] size of the dictionary so usually the
[1654] size of the dictionary is something we
[1655] have to specify a priori and we just go
[1657] with that so here's what's being shown
[1659] is you can learn the size of the
[1660] dictionary so if you give it a large
[1661] dictionary and it doesn't want to use
[1662] all those elements then they just go to
[1664] zero okay so this what happens if you
[1666] can actually sample from the posterior
[1668] then it allows you to fit all these
[1670] other aspects of the model that normally
[1672] we've had to help to fix because all
[1674] we're doing is computing the posterior
[1676] maximum
[1677] okay and and the big you know goal that
[1679] i would have
[1680] i think looking forward now is to trying
[1682] to think about how to build these
[1683] hierarchical
[1684] bayesian models so sparse coding is a
[1686] one layer bayesian model latent variable
[1688] model but what do we want to have
[1689] multiple layers of representation this
[1691] is
[1692] tai simulator and david mumford's
[1694] idea that basically we can think of the
[1697] visual cortex the hierarchical model and
[1699] and they propose that it's doing
[1700] particle filtering to represent these
[1702] posteriors at each level
[1703] okay but potentially now i think uh in
[1706] my view we have kind of a road map for
[1708] how to to move forward forward with this
[1710] model
[1711] to to learn the parameters of such
[1712] hierarchical models this is some recent
[1714] work from mate leno's group a recent
[1717] paper that came out in nature
[1718] neuroscience also proposing this idea
[1720] not for sparse coding but for a
[1721] different kind of model which is showing
[1722] that it actually does a good job
[1725] accounting for a lot of the variability
[1726] you see in actual cortical responses
[1729] okay
[1730] so um so i think the points i want to
[1732] leave you with are that
[1734] um
[1735] uh these recurrent inhibitory circuits
[1738] uh maybe they're doing sparse coding
[1740] okay
[1741] and i think there's a lot of evidence
[1743] accumulating for that
[1744] and uh and then one of the advantages
[1747] this could confer is selectivity which
[1749] is going to help protect against
[1750] adversarial robustness so maybe this is
[1752] something we want to adopt
[1754] in our artificial neural network designs
[1756] and finally that uh that this neural
[1759] sampling hypothesis i think is it seems
[1762] to be coming a viable hypothesis for how
[1764] you could represent posteriors how you
[1766] could adapt parameters of these models
[1768] and make them more complex and deep um
[1771] so
[1772] anyways that's what i'll leave you with
[1774] and
[1776] take questions now or
[1778] later in the discussion
[1785] hi okay i think i got a question um
[1788] oh uh yeah there are a lot of claps
[1791] sorry
[1792] maybe you didn't hear it
[1795] thank you very much for
[1797] really uh
[1799] enlightening talk so if there is any
[1801] question for professor olson please uh
[1805] please this is the time
[1816] yeah i think i got a question um
[1820] so have you thought about using this um
[1824] sparse coding or like lateral inhibitory
[1827] approach for maybe like sub-policy
[1830] networks and reinforcement learning
[1833] was the first name sub-policy network
[1836] yeah like um
[1838] like
[1839] maybe like a sub-policy network oh boy
[1842] uh
[1843] i'm not a i'm not familiar with enough
[1845] with that to say
[1846] uh but it sounds like uh it sounds like
[1848] an interesting idea i'm sorry i don't
[1851] um
[1854] yeah i hadn't thought about that
[1856] okay
[1859] okay
[1862] this is uh really interesting work
[1863] though cool i guess i'm gonna go get
[1866] that book
[1867] what what's your what's your thinking
[1868] about how that might be useful
[1871] yeah i'm thinking about how that might
[1872] be useful for um
[1876] i guess ex
[1877] i guess applying this idea to like
[1879] creating a generator of model for
[1881] um pieces of an image to
[1884] kind of extending that to like pieces of
[1886] um
[1889] like motion or
[1891] things like that
[1894] absolutely i mean i think you could
[1896] everything i presented here was for
[1897] static images were very much thinking
[1899] about uh dynamic image sequences
[1901] learning motion this way
[1903] um and
[1905] those kinds of things as well now
[1912] i have a quick question uh thank you for
[1914] the talk uh i'm curious so if you're uh
[1917] doing posterior inference with lantern
[1919] dynamics on sparse codes are your
[1922] samples still sparse like you could have
[1924] with
[1926] hard thresholding functions so if there
[1928] are no longer sparks because you're
[1930] adding these gaussian noise
[1932] are you able to learn these successful
[1934] uh gabor filters um so so the neat thing
[1937] what comes out from this uh dynamics
[1939] this is in all in the paper um i'm sorry
[1941] uh uh
[1942] where are we okay so so
[1945] uh so we can actually now
[1947] use l0 prior so this is something that
[1949] was harder to do before so usually in
[1951] sparse coding people use an l1 cost
[1953] function and
[1954] what you really want to express varsity
[1956] is l0 something that just counts the
[1957] number of
[1960] non-zero coefficients but that's
[1962] impossible to optimize over right and
[1964] some people use l1 as a proxy and it's
[1966] not for but l1 is not a very first prior
[1968] so so now we can actually use these like
[1970] priors that are so called uh spike and
[1972] slab
[1973] priors and do inference in them and what
[1975] that gives you is the following dynamics
[1977] down here there's questions so basically
[1979] it's just like a leaky integrator with
[1981] noise okay so you so just that alone
[1983] you're right you're thinking is exactly
[1984] right if you inject noise it's gonna
[1985] kind of take whatever sparse and make it
[1987] denser right
[1988] but importantly you end up thresholding
[1990] that so this is not just sort of some ad
[1991] hoc thing that we put in this just
[1993] emerges as you know if you just think
[1995] about look at look at that the launch of
[1997] on dynamics in this setting you need to
[1999] threshold it okay so you can derive this
[2002] as the optimal launch development
[2003] dynamic strategy so this these variables
[2005] s
[2006] now end up
[2008] being uh being very sparse and they're
[2010] sampling from the posterior of the using
[2012] this l0 prior
[2013] um
[2015] but yes you're injecting gaussian noise
[2017] here which is very non-sparse
[2019] but what's making it sparse is the
[2020] threshold
[2021] yeah
[2023] thank you
[2028] i have a question
[2030] sorry
[2031] sorry uh
[2033] you mentioned extending the sparse
[2035] coding model into a hierarchical one by
[2038] stacking these layers
[2040] my understanding is that
[2042] the dictionary begin overcomplete means
[2044] that your output now is somewhere larger
[2047] than i mentioned before
[2049] how do you manage this uh ah good
[2051] question plug them inside
[2053] good question yes that's that's the
[2055] question
[2056] i mean because if you just if you just
[2058] sort of make it over complete on
[2059] overcomplete and overcomplete you know
[2061] then your brain is going to explode um
[2063] so so you can't just keep on doing that
[2065] so
[2066] so we have some other work uh called the
[2067] sparse manifold transform which i think
[2069] gives one possible answer to that and
[2071] other people have been talking about
[2072] this too
[2074] which is that some kind of combination
[2075] of expansion and contraction so so you
[2078] do the sparse expansion
[2080] uh but then you need to somehow contract
[2082] again before expanding again
[2084] uh you don't just want to take the
[2086] linear sparse code i mean the yeah the
[2089] first layer sparse code and then feed
[2090] that to v2 for example
[2092] uh
[2093] so so i think that's an important part
[2095] of it uh also an important ingredient in
[2097] there is going to be
[2098] modeling transformations
[2100] so this is uh
[2102] again something people have been using
[2104] either manifold models for we've been
[2106] approaching that using lead groups and
[2108] that's another way to sort of condense
[2110] the representation uh so to to learn the
[2113] variability so this is as opposed to
[2114] simply doing passive pooling
[2116] to sort of more model an active process
[2118] where you're modeling these
[2119] transformations and that's another way
[2121] of
[2122] condensing it but but but you're right i
[2124] mean that's not
[2125] your your question goes to the heart of
[2126] the problem which is why
[2129] you know there's nobody's really built a
[2131] stacked sparse coding network that
[2132] really kind of illustrates the advantage
[2134] of hierarchy
[2136] um actually there's some very nice work
[2137] out of laurent perry nays lab lauren
[2140] perrine and victor boutin they had a
[2142] nice paper that came out and i think
[2143] both plos and neural computation
[2146] pair papers uh
[2148] looking what they call predictive sparse
[2150] coding so they built a hierarchical
[2151] model
[2152] but
[2153] they don't really address the problem is
[2155] just you know that you're posing as well
[2156] right which is how do you how do you how
[2158] do you avoid just keep on making it over
[2160] completely more often complete
[2162] oh my god
[2164] i think there's an answer to that but no
[2165] one's done it yet
[2167] what do you think of the idea of
[2168] discarding some information at each
[2170] layer as you go forward
[2173] yeah well that's okay so i wouldn't call
[2175] it discarding okay
[2176] in in so let's go back to this uh uh uh
[2180] uh you know the um i'm sorry the tai
[2182] singh lee and david mumford diagram
[2185] uh still like in in in the con in this
[2186] sort of in this hierarchical
[2188] probabilistic model
[2190] the idea is that
[2193] what you would send to
[2195] higher layers just doesn't have all the
[2196] detail okay so so there's there's things
[2199] that you that stay behind in v1 okay so
[2202] that doesn't mean they're discarded
[2203] altogether but maybe the details
[2206] the details remain in v1 and it's more
[2208] the abstract properties have been
[2210] carried forward to e2 so in that sense
[2212] these representations are complementary
[2214] right if you want to know something
[2215] about the 3d shape
[2217] or whose face this is or something then
[2219] you would interrogate these higher level
[2220] areas but if you need to know detailed
[2223] shape parameters like if you're trying
[2224] to take some tweezers and manipulate
[2226] something like a thread
[2228] then you need to interrogate v1 right
[2230] because that just you know it's not
[2231] curious that information is not
[2232] discarded
[2233] it's kept around
[2235] uh but it stays in b1 right and so
[2238] that's the idea so and that you would
[2239] sort of see i think with this kind of
[2242] idea where this the sort of condensation
[2244] that i'm talking about you expand
[2246] condense the condensation dot or the
[2248] contraction doesn't keep all the
[2249] information
[2250] but
[2251] uh that information those details staple
[2253] stay stay stay around in the lower level
[2255] area
[2257] but now the question becomes like uh how
[2259] do you know what to leave behind and
[2262] well yeah okay yeah so thanks a lot
[2266] yeah that's great i mean that's great
[2268] question and that that that's why i'm
[2270] you know i think but that's kind of like
[2271] the rough
[2273] sketch of how
[2275] we could we could we could talk more
[2276] about it
[2277] the details of that but that's but
[2279] that's kind of like the question you
[2280] have to think about that's right that's
[2281] great thank
