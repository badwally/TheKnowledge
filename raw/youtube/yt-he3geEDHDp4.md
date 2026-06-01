---
schema_version: 1
id: yt-he3geEDHDp4
type: youtube
title: Day 2 Session 6, Martin Schrimpf, Brain-Score Vision/Language
url: https://www.youtube.com/watch?v=he3geEDHDp4
authors:
- DANDI
ingested_at: '2026-06-01T19:55:44Z'
content_hash: sha256:15bd3f059169c2ca0ae8cf71fbb23f964fd503ee3e43ccaa47db22861bd46091
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: DANDI
  channel_url: https://www.youtube.com/@dandiarchive
  duration_seconds: 1165
  caption_track: fetched
  snippet_count: 571
filter:
  score: 0.75
---
[0] uh yeah thanks very much for the intro
[2] thank you so much to the organizers this
[3] has been great already uh I want to
[6] start off by saying that everything I'm
[8] going to talk about is really not just
[9] me uh our community I think is is
[12] growing in a in a very good direction
[14] and really all of this is the result of
[16] some fantastic collaborations including
[18] some people that are here like Jim and
[20] Catherine as well
[22] yeah uh I think yesterday a lot of the
[24] the discussions were about we're getting
[27] to a point now where we have a lot of
[28] large scale data now now what do we do
[29] with it and what kind of data should we
[31] collect uh I'll try to assume that for
[35] all of this talk or I'll just declare
[37] that our goal is to build an acurate
[39] model of the brain and how it supports
[41] intelligent Behavior Uh we can may
[43] discuss after if you you think that is
[45] not the goal but I I do think that is
[46] going to enable some things uh for
[48] instance I think that is a good
[51] description of how human intelligence
[53] might be implemented in computational
[55] terms uh it might lead to Next
[57] Generation I and it might also have some
[59] applications in in clinical settings and
[62] I think especially with regards to
[64] yesterday having this competation
[66] understanding that is one way to
[67] integrate all of these data together
[69] like you can have one model that ideally
[71] is gued and constrained by all the data
[73] that we have collected and will
[75] collect so the the two main things I
[77] want to convey today uh are first I
[81] think just the data alone is often not
[83] enough when we want to model the brain
[85] then really we need experimental
[86] benchmarks at scale and I'll talk to you
[89] what what that means and I think those
[91] make the research more efficient and
[92] also accessible to newcomers and I have
[94] an example of what that can look like
[96] and also want to say that the models
[97] that we have today in vision and
[99] language I think are actually pretty
[100] decent already and we can start using
[102] them for guiding experiments and uh also
[105] for some some cool other
[107] things uh so most of the field I think
[111] operates sort of in this isolated
[113] fashion uh right now I mean I know this
[115] room is a very good example of where I
[117] think we we could be heading but I would
[118] say by and large many people are still
[121] sticking in some is some electrodes
[122] collecting some isol data then we build
[124] a model and then maybe there's another
[125] lab that stick electrod somewhere else
[127] and they also build a model and then
[128] eventually we're left with this
[130] conglomerate of data that doesn't really
[132] talk to each other and also models that
[133] maybe each model one individual data set
[136] but we don't even know if that's going
[137] to be general for other data uh I was I
[139] was worried when Bing before showed this
[141] example where you you don't see the full
[142] picture because I thought it was going
[144] to be an elephant uh like the analogy
[146] I'm going to use is you only see parts
[147] of the elephant with this approach you
[149] you don't really know what the full
[150] picture is all of this is necessary but
[153] if we're serious about building a UniFi
[155] model of things like Vision or language
[157] or the whole brain then this I think is
[159] insufficient so instead what I think we
[162] should be doing is to build models that
[164] explain all the data uh all past present
[167] and future data that we can never
[168] collect and I think one just in tun way
[170] to get there is what we call integrative
[172] benchmarking which really just means
[173] let's put all the data together and use
[175] it collectively to constrain the
[178] models and the platform we veloping for
[180] this it's called brain score the made I
[181] heard about and the the idea is that
[183] this will get us to a yeah a full
[185] picture of the entire elephant and in uh
[188] in satus terms I I want to point out
[190] here that level zero data where there's
[192] no metadata is just completely useless
[194] here we need metadata in order to run
[195] the models like we do uh the monkeys and
[198] and
[199] humans uh I know we pass the lunch break
[201] so uh I'm going to try and help you
[203] stretch a little bit so let's say you're
[206] you're a subject in this experiment and
[208] your task is to fix it on the DOT and
[210] I'm going to flash an image and
[211] afterwards it's going to be two two
[213] sample images and this is to to show you
[214] one sample data set that we're we're
[215] considering here uh one of the two
[217] sample images is going to be closer to
[218] the image that we saw before the other
[219] one is not so raise your left hand if
[221] you think it's the one on the left and
[222] your right hand if you think it's the
[223] one on the right
[226] ready okay cool you're being paid uh so
[229] you can keep doing this if you want to
[230] if you want to stretch it but these are
[232] going to get harder uh eventually so
[235] we're wearing the Viewpoint parameters
[236] here for some of them oh yeah okay
[237] you're already you're already
[238] disagreeing with each other
[241] uh turns out yeah other humans also
[243] disagree and there you can keep going if
[246] you really feel like stretching it uh
[248] and so we can compute how much people
[250] disagree with each other and how how
[252] difficult it is to uh to do these
[255] categorization tasks because we have
[256] ground Toth information so we we B this
[258] confusion Matrix each row is basically
[260] an image each column is the choices you
[263] can make and then there are things that
[265] are easier like Fork versus dog is maybe
[267] easy but like you said it like you saw
[269] rhino versus elephant more difficult so
[272] when we test models on this then in this
[274] benchmarking Paradigm this is our data
[276] like I said this not the only thing the
[277] other thing is also how exactly did we
[278] run the experiment what images did we
[280] run and what visual degrees did we run
[281] them what order and then we use those to
[284] or we run those on the model so we just
[286] have to model look at the stimuli we
[287] have to perform the same task there's
[289] some detail on how to do that I'm going
[290] to skip that in rest of time but
[291] eventually the model makes a prediction
[293] of what the behavior should look like
[295] and then we can just compare with
[297] different metrics how similar are are
[300] the data the B data to the model
[302] predictions and here for instance this
[303] is not just ground truth accuracy this
[305] is really Image level alignment right
[307] like if the humans make mistakes you
[309] also want the models to make
[311] mistakes one nice point about this kind
[315] of experimental or this kind of task
[316] setup is that Mak monkeys can do them as
[318] well so their whle cortex is extremely
[321] similar to ours this is a monkey run in
[323] gy
[324] slab and that allows us to then implant
[327] electrodes that we can record from in
[330] order to figure out what is going on as
[331] they look at these images so I usually
[333] think of this as one vector per image
[335] with time average so at the end you left
[337] of this Matrix of neurons images where
[340] each element in the Matrix tells you how
[341] active is one particular neuron for one
[344] particular image and so then again
[346] turning this into a benchmark that is
[348] the data we also have an experimental
[350] Paradigm where again we show those
[351] images and can run this on the model so
[355] usually the models we work with are deep
[356] no networks when we record from these
[358] models then that tou means retrieving
[360] the internal layer activations so there
[363] there's many layers in the network
[364] there's one that we declare to be V1 and
[366] one that we declare to be it and then
[368] that the activations of that of that
[371] layer are the predictions of the model
[372] in response to this particular
[374] experiment we can again compare those
[376] there's many different metrics I like
[378] this one it's going to give us a
[380] score and that that is sort of the the
[383] overall setup so we can now do this
[385] across the entire hierarchy of the
[387] virual system or the the virual vental
[389] stream more specifically
[390] ranging from V1 through it to behavior
[394] and when we test a bunch of models we we
[395] can start with something like with h Max
[398] who still knows
[400] hmax know it yeah who who knows okay not
[404] many okay hmax is a I guess a model from
[407] I think the 1999 so early on uh it was
[411] pretty good for a while I think like
[413] right now it's not considered as good
[414] anymore so but but this is sort of
[415] classic Neuroscience um we can now also
[417] run the kitchen sync of computer vision
[419] model mod so these These are models that
[422] people build not for a purpose of brain
[425] alignment or anything about the brain
[426] really it's it's models that are built
[427] for classification mainly uh if we test
[430] those models they some of them actually
[432] do quite well uh specifically they do
[434] better than the the classic Neuroscience
[436] we had before and I think it's fair to
[439] say that some of those models are at
[441] least today state-of-the-art for these
[442] neural and behavioral L tests that we
[444] have en vision and what emphasize again
[446] none of these were trained on biological
[448] data like these are task of models uh so
[451] they they also might give us some some
[452] insight of how the system got to where
[454] it is all of this is hosted up to date
[458] on the braincare website so I encourage
[460] you to to check that out after the talk
[462] and I think the the strength here really
[464] is we can compare all models in a
[466] unified manner so we can very very
[468] clearly say which model is better than
[470] others because they've all been treated
[471] exactly the same uh they also scale to
[474] many benchmarks so it's easy for the
[475] community to add more and more of those
[477] benchmarks and each new Benchmark can be
[479] run on any existing model or new model
[481] and any new model can be run on any of
[483] the benchmarks so this uh is set up in a
[486] way that it scales together and to to
[488] show you that our community is making
[490] true on adding more benchmarks here uh I
[493] like to just show the slide this is
[495] where we are today this is around 50
[497] benchmarks these are not just uh
[499] regression based they're also
[501] distributional tests of like centers
[502] around in V1 different generalization
[505] and and Behavior Uh and I I still think
[508] this is far from where we want to be
[509] like this is the state today but really
[511] this to me is more of a beginning like
[513] this is still if you want to constrain
[515] million parameter models this is way too
[517] little uh and we get we get around one
[520] model submission per day at the moment
[522] so really what I think we should be
[523] doing and I I hope the the NH agrees to
[526] with us and funds us is that we want to
[527] funnel something like Dandy into this
[528] directly so that we can really use any
[531] new data that is being collected and use
[533] it to constrain
[534] models now one thing this enables is uh
[537] you can ask some some why questions
[539] about the the models for instance you
[541] can collapse over the score so we're
[542] going to take an aggregate sort of the
[544] the mean of all the scores so one dot
[546] now is going to be one model and uh
[549] across many models we we might wonder
[551] what explains the model differences uh
[553] so Guided by early work by by denans we
[556] we looked at imag net top one
[557] performance imet is this uh yeah big
[559] data set in computer vision that I think
[560] everyone knows by now it's a object
[562] classification and turns out models that
[564] do better at classifying objects are
[567] also more more brain like at least to
[569] some extent if you look at the latest
[570] models and keep optimizing eventually
[572] this actually falls off U and there's
[575] still a big gap so we're far from done
[577] but I think this is some some first
[578] success and this is one example of where
[580] I think lots of data can be useful to
[582] track these relationships I'm just going
[584] to flash through these in the list of
[585] time but uh there are many other
[588] relationships we can discover for
[589] instance does improving the model on
[590] neural lament improve its behavioral
[592] lament or is robustness anything that
[595] tracks with different bra elment like
[597] for instance we found that models that
[598] are more like V one also tend to be more
[600] bu but but again I'm going to skip that
[603] in the rest of time and just say this I
[606] think this part is is really what draft
[608] the point Tom so the the x-axis here is
[610] the number of neural benchmarks that we
[611] use to uh to find the best model of the
[616] brain under those those benchmarks and
[618] the yaxis is a held out Benchmark of
[620] behavior so this basically says as you
[622] add more neural benchmarks you also
[623] align better to
[625] behavior so if we were to do many many
[628] more of these I think then the lik that
[629] will do well on Benchmark M plus1 uh
[631] just
[632] increases okay uh I want to also mention
[636] some some words about language because I
[638] I
[639] think really this approach started
[642] Envision but it's very broadly
[643] applicable so the problem is very
[645] similar but we ask is the human language
[647] system similar to models and now the
[648] data is not monkey recordings but rather
[651] mainly fmri as well as Eco data and we
[655] also found here that as we test model
[657] alignment to the human language system
[659] and again over many or three three data
[662] sets that's what we had access to at the
[663] time we hope that's going to be more uh
[665] we actually found some models especially
[666] gpd2 that really did exceptionally well
[669] and again similar to to Vision we found
[672] that models that are better at some task
[673] in this case it was next rep prodution
[675] so prct in the next word in a sequence
[677] uh those models also tend to be better
[679] models of the brain uh this may a quick
[682] plug for an alpha version of uh brain
[684] score language that we're we're starting
[685] to roll out this is yeah really taking
[688] brain SC from vision language uh we hope
[690] there will be many many benchmarks we
[692] already have all of those up we have a
[693] lot of the models up so if you work on
[695] this then I hope this will be useful to
[698] you uh the nice thing about this is uh
[701] students that maybe don't really know uh
[705] what fmri is or how all of the data were
[707] collected they can also make very quick
[709] use of this so we've had one master
[711] student work with us this summer this uh
[713] a three-month summer project uh that the
[715] DPL funds and the question he asked was
[719] really
[720] if you you take these large language
[722] models and you optimize them on on World
[724] Knowledge and people do this mainly with
[726] instruction tuning so what that means is
[727] you you give the model some some kind of
[730] context you give it some options and
[731] then you ask like which of those options
[732] would you choose and then you you
[734] optimize it on that and by doing so you
[736] make it more human-like and uh and also
[738] increase its World Knowledge as has been
[739] shown so then he just used those models
[742] he plugged them into brain score and and
[743] try to see does that improve the
[746] alignment to brain data and turns out it
[747] does and he he did a lot more that I'm
[749] I'm not going to talk about but I think
[751] this really shows like in in one
[753] summer a cool paper came out of this and
[756] you you didn't have to know everything
[758] about about data analysis just with open
[760] source tools that student was able to to
[762] make a lot of quick progress the student
[763] was also exceptional but uh really think
[765] the tools have
[767] to the the last thing uh I want to say
[770] is that the models I think are also at a
[772] stage where we can start to use them for
[774] experiments like this came up a bit
[775] yesterday as well and maybe also
[777] today right now the way we collect data
[779] is somewhat random like we we sample and
[782] we we hope that we get the the right
[784] data at least for model purposes I think
[786] we can start to move towards uh some
[788] more more targeted correction paradigms
[791] and I'll give you one example of that so
[793] I told you before we have some models
[795] that are doing pretty well on alignment
[797] to the human language system so we took
[799] one of those models and by we really
[800] mean
[801] gr so you took gpd2 and then over
[806] aligned it to brain data from from new
[808] subjects so is really just making the
[810] model predict different voxel in in
[812] different subjects that she recorded and
[814] then she had a big text corpora that she
[816] ran through the model and chose the
[819] sentences that the model predicts to
[822] drive or suppress the language system so
[824] basically make activity really high or
[826] really low so you can rank order the
[828] sentences and you choose sort of the the
[830] highest predicted ones and the lowest
[831] predicted ones and we divide those into
[833] drive and suppress sentences and then we
[836] go back and sort of similar to what
[837] Andreas was talking about before we we
[839] validate that those Productions of the
[840] model are actually correct so we we show
[842] those two subjects in the FMI scanner
[844] and uh see if that works out PR the end
[847] product of all of this is the model
[848] gives us sentence predictions that
[850] should drive or suppress the Langer
[852] system uh to give you some examples of
[854] of the drive ones uh we can we can read
[856] them read them here uh I think that the
[859] drive ones people typically say they're
[860] a bit more surprising maybe they're
[862] they're not quite as smooth if you read
[865] them whereas the the suppress sentences
[866] are perhaps a bit more moreor in there
[869] so things that you would expect in the
[871] real world and turns out this this
[873] approach actually works so as you as you
[876] run the drive press sentences in humans
[879] you can control the N activity in the
[881] language system and you you can make it
[883] go higher and lower and then gr develop
[885] more analysis on what the the underlying
[887] factors of all of this are but I think
[889] really the the power here is that we can
[891] use the models to to search a large
[893] space that otherwise we would have no
[895] control over and here we can make the
[897] the brain the experiments much more
[898] efficient
[900] okay I'm going to wrap up there uh bring
[903] it back to the the two things I I think
[904] used to take away from this one is yeah
[906] data loone is really not enough I think
[908] converting it with Rich metadata into
[910] benchmarks that you can use to run
[912] models on it and to make the data
[914] accessible to modelers who might not
[915] know everything about Neuroscience is is
[917] really a key in making our field more
[919] efficient uh and also make it accessible
[921] to
[922] newcomers and then second I think we are
[924] at a point where the models are pretty
[925] decent at least in some fields and we
[927] can start to use them for experiments
[928] and we can we can ask questions between
[930] models like which ones are really better
[932] and which ones make very different
[933] predictions and uh then actually verify
[935] that all of that in biological subjects
[938] cool with that I'm happy to take your
[940] questions
[941] [Applause]
[946] thanks uh thank you for the talk so in
[949] the beginning world the overarching goal
[951] you mentioned was moving to clinical
[953] application so I was wondering how do
[955] you envision the transition from what we
[957] have now board people submitting and
[960] trying to improve the models to clinical
[964] applications and how do you enion this
[966] process and what do we need in order to
[969] move yeah I'll try to give one example
[970] that uh I think like cannot be done this
[973] year or next year but I hope is
[975] something we can work towards so uh
[978] there is some success now in people that
[980] are blind and uh Labs like pet rol
[983] sumers implant electrodes in V1 so they
[987] do monkeys but other labs like BOS King
[989] to to humans and then they sort of paint
[992] on V1 so they they form a letter like l
[994] or s or so and there's R topic mapping
[996] so you can very easily do this and then
[998] subjects that otherwise do not see can
[999] actually with a limited set of number of
[1001] letters can recognize those letters I
[1003] think that's really cool uh but also
[1006] they have a lot of trouble to scale this
[1007] up to object level like basically their
[1009] approach is we're just going to do the
[1010] edges uh but we're we don't have enough
[1013] electrode coverage or resolution to
[1015] stimulate all all those edges in like
[1017] the rich visual world we live in so if
[1019] we were to be able to take those
[1021] electrodes to higher visal areas and
[1024] stimulate there where like let's say in
[1026] it where we think objects are
[1027] represented then maybe there that way we
[1030] can actually list at object level Vision
[1031] but in that here of course we we we
[1032] can't just paint on cortex we we don't
[1034] know how to stimulate but I think the
[1036] models can tell us how so if we had a
[1038] good model of how neur activity is
[1039] supposed to look like then perhaps they
[1041] can tell us what the right stimulation
[1042] patterns would be for any visual
[1045] input I think that that's one way this
[1047] could go there's probably also uh there
[1049] also examples where you don't have to
[1050] necessarily stick electrodes onto people
[1052] there's probably like stimulus to
[1054] behavioral uh applications too but yeah
[1057] this is one that I like ofri how would
[1059] you for the discrep between the number
[1062] ofam a layer that
[1067] represents yeah me ideally you would
[1069] want like what Andress calls a digital
[1071] twin rate something that actually looks
[1073] like the brain and then you you run the
[1075] experiment on the digital twin and then
[1077] before running it in the real subject
[1080] like I'm not saying the current bottles
[1081] are good enough for this but I think we
[1082] can get
[1088] there sure yeah thanks Mar for the great
[1092] talk and really cool stuff so as a
[1094] someone who's worked on engineering
[1096] these benchmarks I'd like to hear about
[1097] the quality control for the data coming
[1099] in because I I do have a little bit of a
[1101] concern if like we can just you know
[1104] everyone knows I love Dandy here I've
[1105] said it like 10 times but like if we
[1107] just can dump everything on D without
[1109] any quality control and then it
[1110] automatically goes to benchmarks we
[1112] could I mean you could see a potential
[1114] problem with this right so I'm just
[1115] wondering what your thoughts are on this
[1116] having done it really successfully yeah
[1119] I mean I don't think we have done that
[1120] successfully you put on the web
[1122] successfully so far we've we've taken
[1124] data from people that we trust to have
[1126] good data I think but there's one
[1128] control which is I think also what Alex
[1130] is going to talk about more uh to try
[1131] and estimate the the noise ceiling of
[1134] the data so if you have crappy data
[1136] presumably uh that number will be very
[1138] very low and then that perhaps might be
[1140] one criteria to exclude it I'm not sure
[1143] maybe we just need some manual checks
[1145] before actually inserting this but uh I
[1148] I know right now when we put benchmarks
[1150] on brain score the packaging of data is
[1152] by far the most painful process because
[1154] there's so many different data sources
[1155] everyone has their own favorite format
[1157] and if we can automate that and like
[1159] even if there's more manual work on top
[1161] I think that would already go a long way
