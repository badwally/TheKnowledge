---
schema_version: 1
id: yt-RQBgEx__B0M
type: youtube
title: Jim DiCarlo - VSS 2014 Symposium
url: https://www.youtube.com/watch?v=RQBgEx__B0M
authors:
- Kendrick Kay
ingested_at: '2026-05-30T21:59:37Z'
content_hash: sha256:ec01218d886b676e25ad2c1037dea59b70e1c9f81cef06cc3564c1df4fd8374e
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Kendrick Kay
  channel_url: https://www.youtube.com/@kendrickkay
  duration_seconds: 1330
  caption_track: fetched
  snippet_count: 693
filter:
  score: 0.7
---
[3] okay um I I want to start by thanking
[5] the organizers for giving me a chance to
[7] reflect some of the work going on in my
[9] lab here I'm speaking on behalf of many
[11] of us listed on the slide here um I want
[14] to start by echoing some of the points
[16] you heard earlier uh that really if you
[18] think about any science the point of a
[20] good science is to take uh measurements
[22] in some domain one and make accurate
[24] General predictions across this
[26] accurately into some domain too for many
[28] of us here that first domain is the
[31] domain of images and our goal originally
[34] was to try to predict things about
[35] behavior and perception this is why
[37] we're at vsss um so the accuracy of this
[40] predictive mapping is a measure of the
[41] strength of any scientific field I think
[43] you heard that implied in the other
[45] talks and this accurate predictivity we
[47] think ultimately is what the reason
[49] we're doing science the ability to build
[50] fix or augment systems in our case the
[52] visual system so um it it it there's
[56] been this is of course possibly the
[57] domain of psychophysics and there's been
[59] some great success stor here but um
[62] things um became challenging when you
[64] get to complex tasks things that that we
[66] like to work on things like object
[67] recognition that this mapping is very
[69] hard to do and for that reason and for
[71] other reasons of of want we went inside
[73] the system and there was a big rush in
[75] the field to start going inside the box
[77] so to speak and measuring neural
[78] activity so here each of these dots
[80] might refer to say the spiking pattern
[82] of all neurons in a particular area and
[84] I think that's what people are here
[85] Loosely referring to as quote neural
[88] representation um and with this movement
[90] as you saw in all those talks certainly
[93] most of what you've seen already is a
[94] focus on mapping between images of
[97] neural activity and trying to build good
[99] predictive models there and while we
[101] think that's important work and we do
[102] that kind of work ourselves as I'll show
[104] you those are called encoding algorithms
[106] we think that this um sort of History
[108] has caused us as a field to essentially
[110] been neglecting this link between neural
[113] activity and complex behavior and
[115] perception um behavior and perception is
[117] not image reconstruction it's doing much
[119] more than that and and I think you heard
[121] that in many of the questions so this
[123] link has been neglected and it's been
[125] dominated by weekly predictive word
[127] models in my field those go something
[129] like it does object recognition let's go
[132] home face neurons do face tasks let's go
[135] home and um my personal favorite
[138] attention solves that so um we we now
[142] have to try to work in what what many of
[144] us want to do is to actually build
[146] accurate decoding algorithms that go
[148] from neural activity to behavior and
[149] perception so we don't think of this as
[151] just extracting activity from the brain
[152] we're trying to build mechanisms that go
[154] from this to these things that we can
[155] measure
[156] behaviorally okay and this is important
[159] these accurate decoding link is
[160] important because remember behavior is
[162] the reason that we're here it's the
[164] reason the public pays us to be doing
[166] this kind of work this is why they're
[167] interested in this and why we're
[168] studying neurons and not liver cells
[171] this this is why um say we focus it
[173] needs us gets us focused on encoding
[175] algorithm efforts that that on the
[177] aspects of activity that actually matter
[179] that are relevant to behavior and it
[181] prevents any work on encoding algorithms
[183] from devolving into just trying to
[185] produce fits in limited domains say for
[186] instance image for instance White Noise
[189] images okay so my lab works on a
[191] particular subdomain of vision object
[193] recognition and by that I include faces
[196] um and U when we do recognition of
[197] course primates don't absorb a whole
[199] scene like this we digest the central 10
[201] degrees we do this by making um rapid
[203] eye movements across the scene sampling
[205] the scene and 200 millisecond fixation
[208] intervals and what that does is bring to
[209] our V stream engine something that looks
[211] like this a series of snapshots you can
[214] notice that you can recognize one or
[215] more objects in each and every one of
[217] those images this ability we call Core
[219] recognition as described here i' like to
[222] illustrate how good we are at this by
[224] always showing this RSVP video this is
[226] shown by folks like Molly and Potter in
[227] the 70s that we can do this quite well
[229] quickly mapped one or more objects in
[232] images like this so This ability core
[234] recognition is not all of object
[235] recognition but we think it's core to
[237] the process and so that's everything I
[239] tell you today is focused on on this
[240] behavioral ability what we call Core
[242] recognition the reason core object
[244] recognition is hard one reason is that
[246] there are many possible objects tens of
[248] thousands of possible objects and also
[250] that each object can produce an
[251] essential infinite number of images on
[253] the retina due to changes in things like
[255] position size pose illumination okay so
[258] the way then we study this is we
[259] actually just take 3D models we have
[261] lots of them we can control their Lane
[263] parameters we can then render them and
[265] we can place them on backgrounds we tend
[266] to place them on uncorrelated
[268] backgrounds to remove confounds that
[269] computer algorithms like to cheat on so
[272] we we end up with um a bunch of images
[274] that look like this this might seem
[275] strange to you that you have cars
[277] floating and heads floating um but this
[278] is turns out to be a very powerful space
[281] that you can challenging for computer
[282] vision yet very doable by humans and we
[284] think it's tapping something that
[286] fundamentally our visual system is doing
[287] quite well and it's a very generative
[289] space of parameterized images okay so
[292] just to give you a feel for it you know
[294] we show images like this 8 degrees
[295] Center of gaze 100 or 200 milliseconds
[297] that doesn't much matter you get similar
[299] results you can sort of do this yourself
[301] that's a car that was a plane that's a
[303] face um car car car okay you get the
[307] idea goes pretty quickly it's very easy
[309] even with those funny looking images
[311] okay I want to point out that what we'd
[313] really like to do is characterize fully
[314] core object recognition we haven't done
[316] that yet but we've been working to
[318] characterize what we call Basic level um
[320] core object recognition among all basic
[322] level objects and I'll point you to a a
[325] talk um by haung a graduate student in
[327] the lab on Tuesday where we
[329] characterized we think we can contain
[330] all essentially 10,000 objects in a
[333] compact space of somewhere between 20
[335] and 50 dimensions and H we tell you the
[337] data to support that idea and we think
[339] that's quite cool so please go to that
[340] talk what I'm going to tell you about is
[342] a sample of core object recognition
[344] space that we've done in the past we
[346] sampled tasks like these of these kind
[348] of objects shown here so it's not again
[350] a full characterization but just a
[352] sample so that we can measure some
[353] Behavior within this domain that we have
[355] a Target to ask about the link between
[357] neural activity and behavior here are
[359] the kind of daa you get out when you
[360] measure hum's ability to do these kind
[362] of tasks for instance discriminate
[364] animals from other basic level objects
[366] or astras from other cars or face one
[368] from a bunch of other faces here's
[370] showing the amount of variation that we
[371] put in it how how much view pose and so
[374] forth variation we have in the objects
[376] and you can see from the D Prime values
[377] that as you add more variation it
[379] generally gets harder and this isn't
[381] surprising um you you should you should
[383] notice that humans aren't perfect at
[384] everything there's a wide range of D
[386] primes um and uh the some tasks are
[389] harder than others this is not something
[392] that um that is noise this is a pattern
[395] of performance is reliably explained
[397] reliably produced across different human
[399] observers and you might int it that this
[401] of course we should get data that looks
[403] like this but again you're doing
[404] intuitive psychophysics when you make
[406] those estimates of saying oh these are
[407] harder than that this pattern is not
[409] easily explained by low-level visual
[411] features as we'll tell you in a moment
[413] of course your brain sort of perceives
[414] that this is hard and this is easy but
[416] this is not easily explained by
[417] low-level visual features and that's
[419] what we're after
[420] okay so we study would like to study
[422] this brain the human brain we study this
[424] brain the non-human primate you might
[426] say well monkeys can't do recognition
[428] well that's not true I refer you to a
[429] poster here um by um Rishi rajalingham
[432] in the lab these show confusion matrices
[434] that he's collected on humans and
[436] monkeys you see how very similar they
[437] are in basic level recognition tasks so
[439] once you train monkeys to do these kind
[441] of tasks they make essentially the same
[442] patterns of errors as humans make so
[444] this is a very good behavioral model as
[446] we suspected and here he's showing it
[448] directly so now because are monkeys we
[450] know a whole lot about their vental
[451] stream as you've already heard about we
[453] study this area it especially in its
[455] precursor area V4 to remind you it
[458] projects to Regions involved in decision
[460] and action and to Regions involved in
[461] memory we can study these
[463] representations because they're monkeys
[464] and not humans at the level of neuronal
[466] spiking activity and that's what we do
[468] okay so we lay out the representations
[470] shown here as series of population
[472] representations each is a retinotopic
[474] map as you know well know in this
[475] audience in this Symposium I think we're
[477] all thinking of each area as conveying a
[479] new popul representation so when you
[481] watch that RSVP video there are neurons
[483] in your various visual areas clicking
[485] along leing something schematically like
[487] this remember our goal is to understand
[489] the link between neural activity and
[490] behavioral report that is what aspects
[493] of this neural activity explain
[495] behavioral report and exactly how does
[497] it do so this was one of our goals this
[499] again is what we call a predictive
[501] decoding algorithm this is work done by
[503] n maaz when he was a post talk in the
[505] lab haung a current graduate student
[506] Ethan Solomon an undergraduate we did
[509] this work by recing from multiple areas
[511] along the vental stream using chronic
[512] recording arrays so we can record
[514] hundreds of neural sites simultaneously
[516] and we pull this across various monkeys
[518] I won't have time to tell you about the
[519] details of our data but just for those
[521] of you who haven't seen it data these
[523] are spiking data from it each tick mark
[525] is an action potential these are
[526] different sites to a set of very
[528] simplistic images shown here just to
[529] give you a sense of it and um you can
[531] see that different sites like respond to
[534] different images um and um you can also
[536] notice that there's this sort of
[537] response window that it runs tend to
[539] resp respond we've narrowed down the key
[541] response window as I'll show you in a
[542] moment that seems very relevant to
[544] behavior as highlighted here in yellow
[546] and you can also notice trial to trial
[547] variability that any decoding algorithm
[549] has to deal with okay so what I want to
[552] tell you the top line on this part of
[553] the story is that we can now use a
[556] predictive population decoding methods
[558] we can now using those methods we can
[559] now report a decoding algorithm that
[562] accurately predicts behavior and so let
[564] me tell you in outline what that
[566] algorithm is the algorithm samples from
[569] proximately 150 arbitrary sites
[572] spatially distributed over all of it it
[575] measures each site average spiking
[577] response average over 100 milliseconds
[579] in that sort of in that window I showed
[581] you a moment ago for each object that
[583] you want to um be able to discriminate
[585] it learns an appropriate weighted sum of
[587] those 100 measurements if you want to
[590] pull this B into a phrase It's a learned
[592] weighted sum of approximately 150
[594] distributed average average over 100
[596] millisecond responses in it that's still
[598] too long for me so I boil it down into
[601] this little acronym laws of dark it
[604] algorithm okay so I'll refer to all of
[606] this as laws of dark it algorithm so
[609] here is my evidence that this this is
[611] some of the evidence that this algorithm
[613] is actually a predictive and decoding
[615] model here's actual behavioral
[617] performance measurements that I showed
[618] you earlier with some tasks indicated
[620] here so here's D primes ranging from 0
[622] to 6 here's the predicted behavioral
[624] performance of this algorithm um again
[626] reading it data to make these
[628] predictions again 64 tasks you can see
[631] this is very close to the unity line
[632] predicting both the pattern of
[634] difficulty of the task and the absolute
[636] magnitude of performance of these tasks
[639] I want to say as a sidelight last um in
[641] cosign this year it's not just category
[643] that can be predicted you can also
[645] predict very accurately other variables
[647] and we think to human level the ability
[648] to estimate position with this exact
[650] same algorithm can estimate position of
[652] an object in an image like this and
[654] that's work that we presented um in
[655] cosign so for those of the
[657] neuroscientists in the room this may
[659] sound again like a computer algorithm
[661] still a little too disconnected from the
[662] brain the way to think about this is
[664] that you have it cortex think about
[666] Downstream neurons in areas like
[668] prefrontal cortex or perinal cortex they
[670] need to sample from this and at the end
[673] after all this is done what they're
[674] really doing is we estimate um waiting
[677] approximately 5,000 single unit inputs
[680] to a neuron and if you want the simple
[682] model to then produce say a face or
[684] responding to say I see a face I see a
[686] car so there's a mechanistic
[687] implementation of this if you're
[689] interested in to why this is 5,000 and
[690] not 150 I'm happy to answer that in
[693] questions okay the the result that I've
[696] pointed out here is non- Trivial most
[698] alternative algorithms cannot predict
[699] the behavior I showed you nearly at all
[702] here's the L of dark it algorithm that I
[704] described here's its accuracy of
[706] prediction now Quantified here it's
[708] within the human to human consistency
[710] similar to Nico's talk you're in this
[711] gray bar that means we cannot
[713] distinguish the output of this algorithm
[714] from another human being um other part
[717] ways of reading it or other visual
[719] repres presentations like V4 or
[720] simulated V1 or some computer vision
[722] algorithms don't come close to this that
[724] does not mean that these areas are not
[726] somehow involved in recognition it just
[728] means that we don't have a predictive
[729] decoding algorithm that goes from them
[731] to these kind of behaviors okay it also
[734] can predict reasonably well the patterns
[736] of confusion matrices um shown here
[738] again the different confusing one object
[740] for another not just performance here's
[742] a noise corrected correlation although
[744] this is not quite as accurate currently
[746] at these higher levels of variation and
[747] that's something that we're still trying
[748] to understand
[750] okay so we have a very good though still
[752] not perfect decoding algorithm that goes
[754] from it into producing the behavioral
[757] report again quite accurately why should
[759] we care why how can this kind of
[761] algorithm actually help the field well
[764] um I want to say that first of all it
[766] predicts that changes in behavioral
[768] report resulting from manipulations of
[770] neural activity can be predicted from
[772] this kind of algorithm so for instance
[773] it tells us if we manipulate it neurons
[775] Say by turning them on and off with
[777] light optogenetics they might have value
[779] for brain machine interfaces it would
[780] tell us what should happen in Behavior
[782] so it gives us prediction and if we bend
[784] them with learning it tells us what
[785] should happen if you're interested in
[787] our optogenetics work and it I refer you
[788] to this talk here on Sunday by arasha
[791] Fraz also it tells us what aspects of it
[794] activity must actually be explained by
[796] these bottomup encoding algorithms it
[797] grounds these kind of algorithms and we
[799] think that's important in some sense it
[801] helps Define what the it Neal
[803] representation is at least with respect
[805] to tasks like core object recognition
[807] Okay so where I've taken you so far is
[809] I've built you I've given you a
[811] predictive model that goes we think
[813] reasonably well and I'm showing these as
[814] dotted lines because it's not perfect
[816] yet but it's very very good between it
[818] neural activity and behavior and
[820] perceptual report and it's a predictive
[821] model over this entire domain now what I
[824] want to tell you about in the last few
[825] minutes I have left and Kendrick please
[827] interrupt me when I run out of time is
[829] the encoding algorithm again I mentioned
[831] we're not just interested in this we're
[832] using this partly as a constraint on
[834] this the encoding algorithms that takes
[836] us from images to it responses similar
[838] as you heard in many of of the other
[839] talks so I'll briefly tell you about our
[842] work on that line here we've been using
[844] a large class of of these kind of
[846] convolutional networks um these are
[848] similar to things you've already heard
[849] about um the things I want to highlight
[851] for those you aren't used to these kinds
[852] of algorithms is that they have elements
[854] that are we would call neurons that have
[855] large fan in they're filters they have
[857] simple nonlinearities that are um
[860] similar to the to the known visual
[861] system each layer uh is convolutional as
[865] I mentioned that if you don't know what
[866] that means just think of it as emulating
[868] retina Toopy um it has many types of
[870] tuning functions so for instance at the
[872] first layer you could have many
[873] different orientations of Gabor that's
[875] what the stack indicates and there's a
[877] deep stack of layers here's shown three
[879] layers in the model I'll tell you about
[880] we have four layers okay so what's good
[883] about these algorithms is that they're
[884] General and predictive as you heard from
[886] many other of the speakers to any image
[888] it will predict what neurons should be
[889] doing in each of these different layers
[891] so these aren't word models they're real
[892] algorithms but the problem is this is a
[894] very broad class there are many many
[896] many thousands of unknown parameters
[898] that are not directly determined by the
[899] neurobiology so how do we set those
[901] parameters to actually choose an
[902] algorithm well this is worked on by Dan
[904] Yan's post talk in the lab and again
[906] hung a graduate student and what they
[908] wanted to do was to better mine this
[910] large class of algorithms for ones that
[912] might be better explaining of the vental
[914] stream be a good in coding algorithm of
[915] the ventral street so um to do this we
[918] thought we'd use optimization methods to
[920] find specific algorithms find parameter
[922] methods and what we were going to
[923] optimize was not fitting neural data but
[926] to optimize the kind of visual tasks
[928] that the laws of dark it had suggested
[930] the ventral stream was actually built to
[932] solve the kind of tasks I showed you a
[934] moment ago we think of this optimization
[936] as being a kind of perhaps an evolution
[938] or developmental process and we're
[939] agnostic about which aspect that is this
[942] is the big picture of what they did
[943] here's the kind of tasks again that they
[945] were optimizing towards they're very
[946] similar to what I showed you earlier you
[948] have 3D objects you have a large number
[950] of them they have semantic breadth
[952] you're going to render them with large
[953] amounts of variation and these are just
[954] some example images again background
[956] correlations making backgrounds
[958] completely uncorrelated
[960] to show you when we optimize this way
[961] here's the first algorithm that came out
[963] this is 2012 this is the called we
[965] called it the HMO algorithm which is
[966] stands for the type of optimization
[968] procedure that's a detail that doesn't
[970] much matter to us but if you care about
[972] the details of this I refer you to the
[973] paper that's just been published so um
[976] that's the it shows that the algorithm
[977] performs well on these kind of tasks
[979] that other algorithms hadn't been
[981] performing well on so that said it was
[982] kind of in the game and then what we did
[984] is take the model so here's the model
[986] laid out it's a four- layer model of
[988] that class showed you it have specific
[990] parameters now all set we'd optimized it
[992] to do these kind of tasks up here and
[994] now what we did was to ask how well is
[996] it going to explain it neurons or V4
[998] neurons so first we did to fit it we
[1001] took the top layers of this model and
[1003] just did linear regression and so this
[1004] is analogous to to what Nico had just
[1007] told you that we need to now is we need
[1008] to map this on it so what we do is we
[1011] take some of the data to fit the linear
[1013] mapping and we test how well it fits on
[1015] the remaining part of the data so we're
[1016] asking if this linear basis if this is a
[1018] linear this this is like a rotation of
[1020] that and there are RDM ways of doing
[1021] this that we've done as well and I'd be
[1023] happy to talk about that but here's a
[1025] single unit data for those of you who
[1026] like single units um the um black line
[1028] is the response to hundreds of images
[1030] this isn't time these are images and
[1032] they're just happen to be grouped by
[1033] categories here there's images of the
[1035] type I showed you earlier the one seen
[1037] here the red line overlay is the
[1039] prediction of the HMO algorithm for this
[1041] particular neural site I want to remind
[1043] you that all of these images the
[1044] predictions this is predictive none of
[1046] these images were previously seen by
[1048] this hm model in making these
[1050] predictions here you can see it does a
[1051] pretty good job r s of
[1053] 0.48 um that is really really good for
[1056] it here's another site just to flip
[1058] through it you might have called this a
[1059] face neuron in a simple way you can see
[1061] there's still structure within the
[1062] category of faces and it seems to
[1064] capture that somehow okay so it also
[1067] fits other neurons that you can't easily
[1069] call as category selective in some
[1071] simple way it seems to capture their
[1072] responses as well and so on average what
[1075] you get out of the top layer of this
[1076] algorithm is about half of the respon
[1078] response variance on average is
[1080] explained half of the explainable
[1081] response variance and that's much better
[1083] than all these previous other models as
[1085] I'm as compared to down here and um this
[1088] again a dramatic improvement over
[1090] previous algorithms so um we also then
[1093] went on and went to the next step and
[1094] said well we're fitting it pretty well
[1095] what happens at these intermediate
[1097] levels remember these algorithms had
[1098] never been optimized to do any kind of
[1100] neural fitting they were optimized to do
[1102] this kind of task but they had a
[1103] structure like the vental stream so then
[1105] we go in and look at the middle layers
[1107] and this is B4 now looking at good a fit
[1109] of V4 neurons that's on the Y AIS here's
[1112] the model predictions or the fits of the
[1114] model um done in exactly the same way as
[1116] we did for it and what you see is the
[1118] intermediate levels of this model
[1119] predict about half of the response
[1121] variance in V4 and um again we find that
[1124] quite remarkable because all that we
[1126] really done here is we took a
[1127] bioinspired algorithm class plus set of
[1130] tasks that we thought we' chosen in the
[1131] right way and just an optimization
[1133] method and It produced neural likee
[1135] encoding functions It produced what
[1136] appears to be a very good encoding
[1139] algorithm and I want to just sort of
[1140] give you a big picture of what this
[1142] means or how we think about this so one
[1144] thing that we noticed is that any time
[1147] these little dots indicate individual
[1148] encoding algorithm those are a set of
[1150] all those parameters in any one of those
[1152] models so you see lots of dots there and
[1153] these black dots are specific models
[1155] that are in the literature so what's on
[1157] this axis here is performance of those
[1159] algorithms on those kind of recognition
[1160] tasks I've been showing you high
[1162] variance core object recognition task
[1164] and this on the y- axis is the ability
[1166] to predict it responses as I described
[1168] last few slides so what we did was we
[1171] saw this plot and we said look there's a
[1172] correlation here so if we can optimize
[1174] for this that means that we might get a
[1176] good high performing model which we did
[1178] and then it turned out that it's just
[1179] continued to follow this trend that it
[1181] actually still is explaining the it
[1183] responses even better so there's a you
[1184] don't have to be a rocket scientist to
[1186] say well keep doing more of that and you
[1187] might be getting more of that and that's
[1189] that's essentially where we're headed so
[1191] what what I've told you now is that we
[1193] we've now built predicted models that go
[1195] from this domain and it to this domain I
[1197] called it the laws of it decoding
[1199] algorithm there's still work to be done
[1201] as I mentioned it's not perfect I
[1202] haven't shown you predictions for each
[1203] image and we think that will be
[1204] interesting to pursue that line and
[1206] further refine these decoding algorithms
[1208] this is not the end of the game it's the
[1209] beginning I also haven't I told you
[1212] about the HMO and coding algorithm that
[1214] as you saw is half the variant explained
[1215] but still work to be done and so we're
[1217] working on that as well and we'd really
[1219] like to see if we can make that
[1221] unsupervised and that's the kind of
[1222] active work that's going on in the lab
[1224] so just for my end here I want to give
[1226] you my answers to the questions that the
[1228] the uh uh organizers asked me to put up
[1231] here what is the most critical open
[1233] question about visual representation
[1235] well I hope you heard in my talk here
[1236] that what we need to do is to have
[1239] accurate predictive maps from neural
[1240] activity to behavior and perception call
[1242] those decoding algorithms that doesn't
[1244] mean we don't need encoding algorithms
[1245] but this has been relatively neglected
[1247] and I think really sets context for
[1248] those encoding algorithms again they
[1250] tell us what aspects of neural activity
[1252] must be accurately predicted from visual
[1254] images and also which details if you
[1256] will about neural responses are not
[1258] actually Critical with respect to the
[1259] behaviors that we defined to be
[1261] interesting and it focuses those
[1263] encoding efforts also on the full domain
[1265] of task relevant images again rather
[1266] than going into a subdomain of images
[1268] and as a bonus we think this is also
[1270] itself deeply interesting and has direct
[1272] applications for instance brain machine
[1274] interface manipulating those neurons
[1275] directly to induce perception so to
[1278] achieve this goal what is the most
[1279] important thing we need more of well we
[1280] just need efforts to build these kind of
[1282] gorithms we need to go away from word
[1284] models and these predictive algorithms
[1286] need to accurately link neural activity
[1288] to behavior perception to do that I
[1290] think hopefully many of you in the room
[1291] will like to hear this that means we
[1293] need Rich characterization of domains of
[1295] visual behavior and perception that
[1296] means we need more good psychophysics in
[1299] these domains that's the Target that we
[1300] should be aiming for these kind of
[1302] models need those kind of data and that
[1303] characterization in both humans and
[1305] animals and so that's the thing I would
[1307] say we need the most of at the moment I
[1309] want to thank these folks who did all
[1310] the work here especially Dan yans and ha
[1312] Hong who I mentioned throughout the talk
[1314] and also my funding agencies and thank
[1316] all of you for your time and putting up
[1317] with my H presentation thank
[1328] you
