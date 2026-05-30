---
schema_version: 1
id: yt-46vht4LAqGk
type: youtube
title: Part-2 of our IJCAI tutorial on deep learning for Brain Encoding and Decoding
url: https://www.youtube.com/watch?v=46vht4LAqGk
authors:
- Data Science Gems
ingested_at: '2026-05-30T20:41:02Z'
content_hash: sha256:6766d2044c871ba373236bab2e2a5f644c215462afbc5a236027f73124639b6e
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Data Science Gems
  channel_url: https://www.youtube.com/@dlByManish
  duration_seconds: 5484
  caption_track: fetched
  snippet_count: 1901
filter:
  score: 0.7
---
[1] um I'll basically quickly try to wrap up
[3] with the stimulus representations part
[4] and then have Professor puppy take over
[6] and talk about the brain decoding part
[9] so uh before the break I talked about
[12] tech stimulus representations uh now I'm
[15] going to talk about visual stimulus
[17] representations so the earlier pieces of
[19] work uh used methods which were popular
[22] in computer vision community in those
[24] days so visual filter Banks uh Gabor
[27] wavelet pyramids and then as deep
[29] learning progressed people actually
[31] started taking in those that progress
[34] into the neurosense community as well so
[36] hmax is more like a primitive CNN um so
[40] folks we use that and then of course I
[42] mean most of the recent models basically
[44] use cnns when it comes to visual stimuli
[46] uh
[48] so um so visual stimuli now
[51] um earlier data sets in fact were not
[54] even naturalistic images so in 2008 when
[58] folks experimented Neuroscience
[60] experiments with visual stimuli they
[62] were done using uh using some of those
[65] images were just binary were just some
[68] patterns while in some other cases yes
[70] there were some naturalistic images
[71] which were used so uh in either way uh
[76] what the features that were used so
[78] basically Gabor wavelet pyramids which
[80] would look for certain kinds of patterns
[82] with respect to special frequency right
[85] so and and orientation so as you see
[87] these kinds of patterns people would
[88] apply those filters try to extract those
[90] kinds of frequency patterns and spatial
[93] patterns and orientation based patterns
[95] and then come up with representations
[97] for an image
[99] this is what computer vision used to do
[100] uh before cnns came in right
[103] but post that over time CNN ish kind of
[106] model started coming up like hmax model
[109] so this model is like a CNN which is
[111] very close to uh the way neurologists
[114] think that the visual cortex system
[116] works so there are simple cells and
[118] there are complex cells and there are
[120] several layers of them so therefore you
[122] know at the base you would basically
[125] have some Edge detectors and then you
[127] would have
[128] um you know some some some more complex
[130] cells essentially they also had Max
[133] pooling in them but then the simple
[135] cells basically uh would not be the
[137] convolution operation as we know of
[138] right now yeah there would be Edge
[140] detectors or some sort of other
[142] operations like gaussian with mean and
[145] it's some gaussian you know smoothing
[147] being applied and so on right so that
[149] was the hmax model but then uh more
[153] recently convolution neural networks are
[154] being used and as we know about them
[156] today yes of course there are
[157] convolutionary conversation layers
[159] pooling layers activation and so on okay
[163] um now for word stimuli in fact some
[166] people also used these convolutional
[168] neural networks to represent word
[169] stimuli so the way you would do this is
[171] to essentially uh of course one way of
[173] doing this for uh sentences is to
[176] basically come up with a word embedding
[177] uh representation for every word in the
[179] sentence and then run a one-dimensional
[182] filter but the other way to just come up
[184] with a good visual representation for a
[186] word is to take the word and then gather
[188] most relevant images by doing some
[191] search using a search engine and then
[193] taking those images and Computing CNN
[195] representations on top of them
[197] that gives you a visual representation
[199] for example or a CNN based
[201] representation for the word car right
[203] and then yeah people have experimented
[205] with various kinds of models LX net
[207] which is generate Inception resonate
[209] densenet and so on
[211] um
[212] you could do you could also by the way
[214] use the objects as features so if you
[216] basically have visual represent and a
[218] visual stimuli you could take this
[221] particular visual stimuli and come up
[223] with objects now clearly several object
[226] detection methods are very popular today
[228] so you could either do those object
[230] detection methods uh directly you
[232] basically do object detection figure out
[234] objects their names and then those names
[237] begin you can actually do semantic
[239] encoding so either you could uh you know
[242] use some sort of fastest embeddings some
[246] sort of fastest embedding so as to get
[247] semantic embeddings uh so as to get
[249] representations for those words or you
[251] could use topic models and so on
[254] now in some cases yes these features uh
[257] were too many so therefore in some cases
[259] people actually also resorted to doing a
[262] PCA and then just using a smaller
[264] dimensional representation of these
[266] objects coming in uh or of the of the
[269] world embeddings corresponding to the
[270] objects which were detected by object
[272] detectors in the images
[275] um people have also used semi-supervised
[277] cnns so the problem is scarce data so
[281] and this was very popular as a method
[283] way back when the when the existing
[285] pre-trained models were not that great
[287] so if you were basically uh trying to do
[289] a brain encoding decoding in a
[291] particular domain where there was not
[293] enough data then you would essentially
[296] use Auto encoders so as to essentially
[298] come up with really good visual
[300] representations uh again these Auto
[301] encoders were CNN based right and then
[304] you would essentially uh have a good
[307] pre-trained uh you know encoder
[309] convolution encoder and then you would
[311] basically use that with the kind of
[313] images that you would have in that
[314] domain so as to come up with the
[315] representations that can be passed on
[317] for brain decoding or brain encoding
[319] purposes
[322] um uh in fact this is another paper from
[325] our group where we essentially tried to
[326] combine lstms with convolution neural
[328] networks so here the idea was that maybe
[332] we can do predictions of these brain
[333] activations slice by slice so fmri
[336] voxels are uh you know this kind of
[339] information of course is available for
[341] the entire volume but then it is also
[343] available slice by slice so can you take
[346] the image so in this architecture the
[348] way we do this is that is as follows we
[349] take the image and then we run an
[352] exception model in some ways some CNN
[354] model in that senses right we have that
[357] representation the CNN embedding right
[359] we pass it to an LST
[361] the first uh you know in the first part
[363] the lstm tries to predict the first
[365] slice and then in the you know it uses
[367] this information to predict the second
[368] slice uh along with of course the CNN
[371] embedding of the image that is
[373] essentially given uh to every input okay
[376] so basically we make slice by slice
[378] predictions uh using a CNN lstm kind of
[380] framework as you see here
[383] uh the stimuli here Still Remains
[385] essentially uh captured uh using a CRM
[389] kind of a model but then the nice point
[391] is that here for decoding for for
[393] encoding purpose for encoding purpose to
[395] guess the brain activations we are sort
[397] of encoding uh by doing slice by slice
[400] predictions
[402] more recently of course latent diffusion
[404] models have become popular so
[406] essentially
[408] um you might have heard about diffusion
[410] models and diffusion models essentially
[412] uh try to take a take an image and the
[416] diffusion process tries to essentially
[419] um you know get to the latent Vector
[422] corresponding to that image in fact the
[425] little diffusion models these days are
[426] super efficient they first take the
[428] image try to use the auto encoder setup
[430] so as to get latent representations and
[433] then they apply diffusion process on
[434] those latent representations
[436] in fact in in in this in this kind of
[439] setup there are two processes one of
[442] them is a diffusion process which takes
[444] an image from the training data and
[446] tries to obtain
[448] um a noisy vector or in fact the idea is
[451] to basically get complete noise Vector
[453] at the end uh on the way learning the
[455] parameters of the diffusion process
[457] however on the other hand you start with
[460] the noise vector and this is what in
[461] fact you do at generation time you start
[462] with the noise vector and then you have
[464] a denoising unit which basically tries
[467] to get you a latent Vector which can be
[469] decoded back to a real image to an image
[471] of this guy to an image of this guy okay
[474] later diffusion models are super popular
[476] these days because of models like clip
[478] or models like a stable diffusion dally
[481] two and so on which enable you to
[483] generate images almost realistic images
[485] uh now these latent diffusion models can
[488] also be made conditional in nature which
[490] basically means that you can actually
[491] Supply conditioning information and
[494] thereby generate images which correspond
[496] to those conditioning information and
[498] what these models in Neuroscience do is
[500] to have conditioning information
[502] provided using fmri so you can basically
[504] say here are familiar brain activations
[506] can I basically generate images based on
[508] them right and therefore these
[510] representations essentially
[512] um are are quite popular because now uh
[515] you know people have been able to come
[517] up with uh with representations that
[520] look pretty similar to the ones that the
[523] participant was shown when the fmri
[524] recording was done so in the first row
[527] what you see here are the images that
[529] were shown to the participant and then
[530] you recorded fmri brain recordings and
[532] using those fmris without knowing the
[535] original image people who are able to
[537] reconstruct what is shown at the bottom
[538] now isn't that magic I mean that's
[540] that's like saying that yes I mean you
[542] know I can actually just just try to see
[545] just try to see these guys brain
[546] recordings and then I can imagine I can
[548] actually see what this guy has seen
[550] right so it's like you know there are
[553] also some papers which sort of are like
[555] hey maybe this is a good way of of
[557] decoding um what dreams the person is uh
[560] is is is having you know while sleeping
[563] okay so that's that
[565] so that's about visual stimuli now audio
[567] stimuli there is not too much of work in
[569] the audio domain but recently more and
[571] more data sets are coming up
[573] older stimulus presentations use the
[576] typical features that one can obtain
[577] using pi audio or librosa libraries so
[581] like World rate phoneme rate presence of
[583] phonemes Mel frequency capsum
[585] coefficient features Mill spectrogram
[586] features and then you know even features
[589] based on Mel's spectrogram itself zero
[591] Crossing and so on right but more
[593] recently people have been using uh deep
[595] learning and deep neural networks for
[597] doing uh audio stimuli representations
[599] as well for example soundnet is one of
[602] those popular uh you know audio stimulus
[605] representation architectures where you
[607] could essentially take I mean well you
[610] can take unlabeled video so if you just
[612] have audio you can just take audio as
[614] well but you can take the unlabeled uh
[616] video and then you can actually pass the
[618] raw waveform uh through the CNN
[621] architecture which essentially outputs
[624] um outputs and audio representation but
[626] if you also have the visual frames you
[627] can actually try to come up with a
[630] representation where try to come up with
[632] the representation such that
[633] representation and video and the and the
[635] visual representation are in sync with
[637] each other right so that's that now of
[641] course more recently there have been
[642] many many uh other uh audio kind of
[645] models which have been proposed but it
[647] has to be seen you know how these kinds
[649] of models become popular uh in the uh in
[652] the Neuroscience Community very recently
[654] in fact we have had a paper in Winter
[656] speech where we have experimented with
[658] several kinds of Audio models in
[661] including vf2net uh and we have to net
[663] uh 2.0 uh and many other models
[667] um which are popular uh in the speech
[669] community in fact we've also
[671] experimented uh so just like in natural
[673] language processing there's this
[674] Benchmark called glue and I talked about
[676] textum representations which can be
[678] obtained using fine-tuned models on glue
[681] Benchmark data sets similarly in the
[682] speech world you have a you have a
[684] benchmark called a superb and we have
[687] also recently experimented uh with the
[689] trying to use uh these sound based
[692] models fine-tuned on various tasks uh in
[695] the super Benchmark and then see which
[697] of them gives you better encoding
[700] accuracies right so these tasks could
[702] include you know
[703] automatic speech recognition speech
[705] speaker recognition uh emotion
[707] recognition from speech and so on so
[709] several tasks and then there again we
[711] have observed that automatic speech
[712] recognition gives you really good
[714] results in terms of brain encoding
[716] okay so now let me quickly talk about
[719] multimodal stimulus representation so uh
[722] these representations are super
[723] important when your stimulus actually
[725] contains two or more than two kinds of
[728] modalities so for example processing
[731] videos requires Audio Plus image
[733] representation right so essentially and
[735] therefore some people have essentially
[737] just did that I mean you know if there
[739] is audio sure let me use soundnet if
[741] there is image let me use vgg and then
[743] combine the representations at the end
[744] so those are called as late Fusion
[746] models you fuse the representations but
[748] towards the end right uh similarly there
[751] have been image plus text kind of
[752] combinations as well so people have
[753] taken uh you know data sets which have
[756] image stimulus along with say sentence
[759] about the image and so on and then again
[760] people have just done the same thing for
[762] text basically you use glove or Elmore
[764] bird and so on but for images you
[766] basically use vgg uh or or any of the
[769] other popular image processing image
[770] stimulus based deep deep learning
[773] representations okay
[775] um however more recently in fact we
[777] worked on multimodal stimuli using
[780] multimodal deep learning models okay so
[781] this is again um you know work from a
[784] group where we basically uh took a
[787] multimodal stimuli so um you know there
[789] is a text part and there is an image
[791] part right uh and then uh we uh used uh
[796] various multimodal Transformers of
[798] course you know because this was the
[799] first paper trying to apply multimodal
[801] uh multimodal Transformer
[803] representations on this multimodal
[805] stimuli we also compared with several
[807] other uh uni model as well as simpler
[810] multimodal architectures for example we
[812] experimented with the pre-trained cnns
[815] we also experimented with pre-trained
[816] text Transformers separately just using
[818] the text modality and just using the
[820] speech modality right and then we also
[823] leveraged image Transformers so
[824] essentially uh you know just to
[827] basically capture the image modality uh
[829] we have uh you know we basically not
[832] just used the pretend cnns more recently
[835] image Transformers have also become
[836] popular so we also experimented with the
[838] beat architecture bi-directional encoder
[840] representation from Ace Transformers or
[842] or others like Vision Transformer and
[845] then as I mentioned we also experiment
[846] with late Fusion models because that's
[848] the obvious that's that has been the
[850] obvious ways of combining the image
[851] modality and the text modality together
[853] which in it combined with Roberta or
[856] resonate combined with Roberta and so on
[858] and then lastly we also experimented
[861] with multi-modal Transformers
[863] you know um so so leveraging the state
[866] of the art so essentially clip models LX
[868] smart models visual bird models and so
[870] on we found that visual word visual word
[873] performs the best in fact you know we
[875] have done more and more kinds of
[876] analysis like trying to figure out uh
[878] you know which layers of the visual
[880] model uh give you the best performance
[882] in terms of brain encoding accuracies
[884] we've also done some really fancy uh you
[886] know uh tasks so for example it's a very
[890] interesting question uh if I'm looking
[892] at an image and I'm as a human if I'm
[894] trying to describe it using a sentence
[896] which parts of my brain are involved
[897] right it's like technically called as
[900] image capturing task and the question
[902] that I'm asking here is that if am I
[904] looking at an image and then I'm trying
[905] to sort of you know come up with a
[907] caption you know so which parts of my
[909] brain are actually doing image
[910] captioning so those kinds of questions
[912] now can be answered very nicely using
[914] these multimodal Transformer based
[916] representations over multimodal stimuli
[918] especially if you have fmri
[920] representations uh with such multimodal
[922] stimuli right so that's that now that
[926] was the uh that was the initial
[928] um you know first part of this uh
[930] tutorial uh and we sort of wrap it up
[933] here uh in summary we have already
[935] talked about the basic introduction to
[938] brain encoding and decoding where
[939] Professor babiraju introduced what is
[941] brain encoding what is brain decoding
[943] what do cognitive Neuroscience uh people
[946] do right
[948] um what are interesting questions uh
[950] then we talked about popular data sets
[953] um audio video multimodal you know
[955] speech based text-based data sets and in
[959] this session and and of course before
[961] the coffee break I also talked about
[962] various kinds of stimulus
[964] representations text-based
[966] representation speech based
[967] representations uh multi-modal
[968] representations and so on right now
[971] Professor bafi Raju will take over and
[973] he will sort of talk about uh deep
[975] learning representations for brain
[976] decoding uh post that will have lunch
[979] break and then Maria will join in where
[981] she will basically start talking about
[982] deep learning brain encoding
[985] okay so any questions before we move
[988] over to Professor babiraju's Part
[995] if you think of it you know cognitive
[997] Neuroscience is a very awesome field uh
[1000] to be studying at this point uh thanks
[1002] to super awesome advancements in deep
[1004] learning uh what I find very exciting is
[1007] to be able to you know the cognitive
[1008] Neuroscience sort of gives you this
[1010] satisfaction and this interesting
[1012] insight into how your brain works right
[1014] and with all the advancements that are
[1016] happening both in the Deep learning
[1018] field also in the field where you know
[1021] in in the in the hardware field so the
[1023] way you take these measurements the
[1025] scale at which these data sets are
[1026] becoming available cognitive
[1028] Neuroscience has become like a green
[1029] area for several students to uh to do a
[1033] whole bunch of research work on so I
[1035] mean you know as of now we are working
[1037] on several papers yeah in in various
[1040] areas
[1041] um so if you if you basically are like a
[1043] student interested in this area looking
[1045] to join please feel free to you know
[1047] also connect with us for research
[1048] collaborations later
[1050] but that's that
[1052] uh and take it over from here unless
[1054] there are any questions yeah
[1057] yeah small questions
[1060] okay
[1062] yes thank you just a
[1067] um
[1069] tourism from a neuroscience point if you
[1071] can implement or simulate uh and the
[1074] gate and okay
[1078] sorry the question was somewhat audible
[1080] but not clearly so uh someone cannot
[1083] repeat it
[1084] so from a neuroscience point of view is
[1089] there and uh what is the mechanism or
[1091] what is there a mechanism to simulate
[1094] and the gate like a logical and logic
[1097] all
[1098] well from a neuroscience perspective
[1100] yeah I mean I think
[1102] those Gates
[1104] you can simulate those Gates but why
[1107] would you want to do that is the
[1108] question right I mean in the sense
[1112] I see uh yeah I mean I think uh
[1118] I mean I'm not very sure why would you
[1121] want to simulate it using natural
[1123] mechanisms right see cognitive neuros
[1125] has just built on deep learning and if
[1128] you ask me that hey are there neural
[1130] models artificial neural models which
[1131] can simulate candidates to solve the
[1133] problems
[1134] exactly right yeah yeah now uh now the
[1138] question is
[1141] yeah if your question is that if natural
[1144] um you know neurons inside us are they
[1146] acting as like and Gates or or Gates
[1149] um you know uh I don't think people have
[1151] tried to look at it at that level I mean
[1153] I think people have tried to look at it
[1154] at a more broader level where uh where
[1158] you can take a stimuli and try to
[1160] understand I mean at a much more
[1161] abstract level rather than really
[1163] talking about the basic unit of
[1165] processing in the sense that is it and
[1167] gate or or gate I mean of course people
[1169] have tried to do experiments with a
[1171] single neuron and that is how in fact
[1172] people designed various activation
[1174] functions saying that I mean in fact
[1176] there are very old YouTube videos about
[1178] neurologists trying to do experiments uh
[1181] with uh with all those electrodes and
[1183] then trying to figure out that yes if
[1184] there is a edge moving in you know if
[1186] there's an edge coming in there's an
[1188] edge detector which can be trained using
[1189] neurons and so on
[1191] um but
[1193] um you know beyond that I think more so
[1194] in the recent recent times people have
[1197] been experimenting with more abstract
[1198] representations rather than deep detail
[1203] please feel free to add I mean that was
[1205] my answer that was my thoughts yeah
[1207] thank you yeah I guess uh if we go back
[1211] to 1940s uh McCulloch and Pitts were one
[1215] of the early uh my colleague was a
[1219] neuroscientist who tried to look at how
[1222] the uh all our non model of spiking
[1227] patterns of neurons how these could
[1231] support logic gates and he had he along
[1234] with a logician Pitt have written in a
[1238] book uh detailing all the kinds of logic
[1242] circuits that are possible where the
[1246] essential neural processing is retained
[1249] but an abstract mathematical model and
[1252] this sort of forms the basis for later
[1255] models like perceptrons and multi-layer
[1258] perceptrons this is a whole uh
[1261] so the basis uh and the excitement uh
[1265] from I would say 1940s has been the
[1269] ability of these uh neuron like uh
[1273] elements implementing basic uh you know
[1277] logic gates in fact I would uh just go
[1279] on to add for Neumann uh was inspired by
[1283] these kind of models and what took a
[1286] different direction of uh proposing a
[1289] digital architecture based on these uh
[1291] these on off elements right I mean of
[1294] course the rest is history as we could
[1297] say so uh I think the basic logical
[1301] operations are somewhat I think is the
[1305] basis for most of the modern
[1307] developments and neural network service
[1310] okay so yeah let me share my screen
[1315] there are no other questions we'll
[1320] next uh one hour or so before the lunch
[1323] break we'll look at a couple of examples
[1327] of brain decoding models uh details of a
[1333] couple of them
[1335] and this is to sort of supplement and
[1339] extend
[1340] the detailed presentation on stimulus
[1343] representations from different
[1344] modalities that Manish took us through a
[1348] very exhaustive manner right so what uh
[1356] yeah so I will basically uh this is the
[1359] sort of agenda for next 50 minutes or
[1363] one hour I'll start with the re sort of
[1367] asserting the difference between
[1369] encoding and decoding then we look at
[1372] basic strategies of a non-linear or
[1376] linear models for building these
[1379] decoding engines and today we look at
[1383] language decoding using uh three or four
[1388] uh papers that we have chosen from a
[1392] whole collection and there is a recent
[1394] survey which lists about uh
[1397] more than 30 studies in the last five to
[1401] six years
[1402] that have built either decoding or
[1404] encoding models and so it's a very uh
[1409] sort of
[1410] emerging and happening area within
[1414] computational
[1416] Neuroscience or
[1418] applications of AI in cognitive
[1421] neuroscience
[1422] so you look at couple of those examples
[1424] uh including our own
[1426] um one
[1428] so uh as we discussed
[1433] encoding uh
[1435] it takes you from stimulus
[1437] representation to brain activity and in
[1441] this case the brain activity is
[1445] the functional MRI it could be easy it
[1448] could be energy or any kind of activity
[1450] that you have Nars then Optical
[1453] recording nirs recording that any of
[1457] those activations so going from learning
[1459] a model to predict brain activity is the
[1462] encoding process uh it tells us
[1465] basically encoding models allow us to
[1469] these are process models that
[1473] they can be interpreted as process
[1475] models and constraining computational
[1480] theories of the brain right on the other
[1483] hand decoding takes brain activity and
[1487] tries to
[1488] predict the stimulus representation or
[1491] stimulus category or representation or
[1494] actually reconstruct the stimulus in
[1497] some sense it is what Manisha has tried
[1500] to
[1501] convey the excitement is like reading
[1504] the mind I give you the brain activity
[1506] and can you predict uh what kind of
[1509] stimulus the person might have been
[1512] experiencing to give race to this kind
[1515] of brain activity
[1517] of course this problem is much more
[1519] complex difficult and in some sense
[1523] ill posed in the sense that there are
[1526] many uh representations that are
[1529] compatible with the same brain activity
[1532] right and the Brain also being complex
[1534] uh dynamical system that its activation
[1538] may not be related to a a
[1542] single sort of stimulus representation
[1546] so
[1547] um decoding in general
[1549] uh is very relevant for cognitive
[1553] neuroscientists interested in how
[1555] semantic information is represented in
[1558] the brain how brain represents uh uh the
[1562] meaning in in the cortical activation as
[1565] well as to computational linguistic
[1568] linguists who are interested in the uh
[1573] cognitive plausibility of the
[1575] distributional models like but starting
[1578] from early word embedding models like
[1581] word to work glove work and the recent
[1585] large language models what is the their
[1588] cognitive possibility uh can also be
[1592] assessed by their ability to buy their
[1596] you know their concordance will take
[1598] away brain represents linguistic
[1600] information
[1601] so these are some of the possibilities
[1604] but let's go into the details
[1607] so in brain decoding the idea is can we
[1611] reconstruct the stimulus given the brain
[1613] response the features of the stimulus
[1615] either in a categorical setting like
[1617] this I show image of a shoe and is the
[1621] recorded brain activity use that
[1623] activity to predict whether it is a shoe
[1626] or a cat right for example which
[1629] category that this is this activation
[1633] belongs to and given a test stimulus of
[1637] a different image shoe image is it
[1641] possible to still predict the category
[1643] of the stimulus
[1644] okay so the other uh more
[1649] nuanced linguistic decoding is where you
[1653] acquire the functional MRI and the Brain
[1656] activation uh represented as uh walk
[1660] cells which are selected uh I'll talk
[1664] about this in next slides more detail
[1667] these activity in the selected regions
[1671] and voxels uh they are the corresponding
[1674] activation Vector can we use this to
[1677] through a model decoder can we predict
[1680] the representation of the word that has
[1685] actually excited this activity that has
[1688] caused this activity the stimulus
[1690] representation in the form of word
[1692] embedding instead of simple category
[1695] information this is also a part of
[1697] decoding and in the next stage actually
[1701] reconstruct the word that corresponds to
[1704] this embedding right so in this case a
[1707] dog is the word that the decoder
[1710] predicts given this brain activity of
[1713] course uh
[1716] this linguistic decoding can utilize
[1718] features uh from
[1722] Models like birth uh fuse this feature
[1726] Vector from the functional MRI in order
[1729] to actually let the the language encoder
[1733] predict the corresponding
[1737] um
[1738] uh the uh lexical item that corresponds
[1742] to this input right this the linguistic
[1745] decoding
[1747] so there are two broad approaches
[1751] just to kind of group them the linear
[1756] models and non-linear models in the
[1758] linear models you take an object an
[1762] image this is from this horikawa
[1766] kamintani
[1767] data 2018 where participants were shown
[1771] objects and then or a label is given and
[1777] they are supposed to imagine the
[1779] properties of the object that
[1781] corresponds to this label the functional
[1784] MRI activity brain activity is used to
[1787] build a decoder to predict the feature
[1791] pattern
[1794] features of the stimulus pattern that
[1798] might have caused this brain activity
[1799] and these features could be used to
[1802] either predict the label one among the
[1806] various labels uh jet or turtle or
[1809] leopard or skyscraper and so on
[1813] and you could use a rich regression
[1816] model to actually predict the stimulus
[1819] representation as an output or a
[1822] logistic regression to actually predict
[1825] the classification the given this
[1828] activity the person might be thinking
[1831] class 1 object versus class 3 object
[1834] right so it's a classification that you
[1837] actually learn to predict
[1839] so of course this stimulus
[1841] representation prediction is much harder
[1843] in general
[1845] and the people also have used instead of
[1849] just selecting uh voxels through some
[1853] schema uh a selection schema or for
[1857] example one of the schema that is used
[1859] is uh how predictive are these
[1863] activations which of the uh you know one
[1867] lakh voxels that are active are more
[1870] highly related to the Target Concepts or
[1873] words uh you select a subset of them as
[1877] a as a feature Vector like in this case
[1880] this feature
[1882] activity brain activity Vector
[1885] consisting of activations of voxels that
[1889] you can identify or you can model this
[1891] in a more uh uh
[1894] complex way is the 3D brain image scan
[1898] is fed to a 3D CNN for example
[1901] and then come up with a feature Vector
[1904] that represents the brain activity and
[1907] use this feature Vector to do the
[1910] decoding task either classification or
[1913] stimulus representation prediction or
[1915] reconstruction
[1917] right so this uh deep cnns are used to
[1920] actually process the the vein Imaging
[1923] activation vector
[1926] so the next task for us uh uh is given
[1930] we have some broad understanding of how
[1932] these models and what kind of models are
[1935] used to to build this uh decoding models
[1940] uh how do we evaluate the performance of
[1943] these models there are two metrics that
[1946] I talk about actually three things that
[1948] I talk about payroll is accuracy is one
[1951] common metric that is used where if this
[1955] is the stimulus
[1956] this is the concept word that I am
[1959] showing a sentence of uh the concept
[1962] here is apartment in the sentence that
[1965] uses this concept is presented and there
[1969] is another concept jth concept that is
[1973] that uses
[1975] another sentence that uses a different
[1978] concept eighth concept which is here
[1980] building of course apartment building
[1983] are related but there are different uh
[1985] the one is more specific one is more
[1988] General right so those concept words and
[1992] the corresponding
[1994] so uh you actually predict the
[1999] representation semantic Vector
[2002] representation
[2003] coming from this uh decoding model right
[2007] the model that we have uh built build uh
[2012] it predicts this semantic Vector uh this
[2016] is the original Vector the ground truth
[2019] and Y I hat is the corresponding decoded
[2022] semantic Vector similarly for this jth
[2026] concept this is the actual this could be
[2030] for example uh 300 dimensional glove
[2034] vector or birth representation vector or
[2037] a word to have type of representation of
[2041] the uh of the word building for example
[2046] um this is the ground truth y j is the
[2049] ground Truth for building and YJ hat is
[2053] the decoded semantic Vector from a model
[2057] that you have built for example a
[2058] regression model that you have built
[2061] this is the decoded these are
[2063] predictions these are predictions from
[2067] the decoder and this pairwise accuracy
[2071] says that you mash
[2073] the decoded Vector of y i hat with y i
[2077] and look at the correlation similarly YJ
[2081] hat with its ground truth correlation
[2084] and also do the all the opposite
[2089] right the decoded semantic Vector with y
[2093] i hat how similar it is to another
[2095] concept Vector similarly YJ hat the
[2099] prediction for the jth concept how
[2102] similar it is to this
[2104] so both within concept similarities and
[2109] across concept similarities are are
[2112] computed and the pairwise accuracy is
[2115] computed if
[2117] the within pair some of these
[2120] correlations for example one of the ways
[2122] of computing similarity is a Pearson
[2125] correlation the Pearson or cosine
[2128] similarity between these two vectors so
[2131] any of these are used and the similarity
[2135] score of within I to I and J to J the
[2139] sum of this should be greater than the
[2142] cross correlation then we say that the
[2144] decoder is able to distinguish these
[2147] Concepts uh and these vectors are
[2150] further away
[2152] these cross representations are farther
[2156] away compared to the the within concept
[2159] predictions
[2162] okay so this average over all the test
[2165] instances for a participant is given as
[2168] a pairwise accuracy scope right so this
[2171] is what is written if this correlation
[2173] of y i to y i hat and Y J to y j hat the
[2177] sum of this is greater than the other
[2180] cross pairs then we give a score of 1
[2183] otherwise zero and we score like this
[2186] for every pair and average pairwise
[2190] accuracy is computed uh for all the test
[2193] stimuli for each participant separately
[2195] and this is what is reported as the
[2198] decoding models performance one
[2201] performance measure of the decoder
[2205] the other metric is rank accuracy how
[2209] well the decoded Vector right so this is
[2212] the decoded semantic Vector for this
[2215] uh what kind of rank does it enjoy
[2218] across all the other semantic vectors
[2222] the ground rules of all the other
[2223] semantic vectors
[2225] so we we hope that I concept apartment
[2230] uh decoded semantic Vector is more more
[2234] highly related to apartment Tech
[2236] semantic Vector ground truth compared to
[2238] all the others so we rank order then
[2241] these correlations you compute the
[2243] correlation and you rank order these and
[2248] we look at the rank that this decoded
[2251] semantic Vector has compared to all the
[2254] other test instances within in the all
[2257] the other scientific vectors within your
[2260] concept base
[2262] and the lower the rank I mean the rank
[2265] one is better than rank two and so on
[2267] and we look at the average rank that the
[2271] decoder has for across all the uh the
[2275] decoded semantic Vector instances for
[2278] participant so this average rank score
[2282] or accuracy is another metric that is
[2284] also reported for decoder evaluation
[2289] okay so the rank characteristics is
[2290] computed uh as you know based on these
[2293] statistics from this sort of estimation
[2296] ah the evaluation process
[2300] the other uh metric that is also used
[2303] sometimes is what is called
[2305] representational similarity Matrix and
[2308] the concept is like this and suppose the
[2310] person is experiencing different scene
[2312] scene one to scene 20 the brain
[2315] activation is recorded the pairwise
[2319] similarity across
[2321] this is a representational similarity
[2324] from the visual cortex of the of the
[2327] participant the brain activation
[2329] corresponding to scene one how well it
[2332] is correlated with brain activations
[2334] with the other scenes when they are
[2336] seeing the other scenes right obviously
[2338] the diagonal is very high close to one I
[2342] mean actually equal to one because you
[2344] want to see that this the scene one is
[2348] correlated and these cross correlation
[2350] tell how similar the brain activations
[2353] are when they are seeing scenes of
[2357] different types
[2358] so this Matrix this 20 by 20 Matrix in
[2362] this case represents is called the
[2366] representational similarity Matrix of
[2368] brain activations associated with
[2371] participants viewing of this 20 scenes
[2376] so uh each The Matrix elements here of
[2380] the correlations of each pair of scenes
[2384] that they are looking at this
[2386] correlation obtained from brain
[2388] activation
[2390] right it is also possible I can
[2394] get here so this is what is uh you can
[2397] actually talk about either similarity or
[2400] dissimilarity dissimilarity is just one
[2403] minus similarity and this kind of Matrix
[2407] sometimes is also used is called a a
[2410] representational dissimilarity matrix
[2413] and
[2415] the analysis the one of the interesting
[2418] things about this RSA analysis is that
[2422] it is possible to compare model
[2424] representations and brain
[2426] representations without actually
[2428] directly comparing them uh it's a
[2432] powerful approach where the model is
[2435] given right scene 1 to scene 20 for
[2439] example this is a decoder uh in this
[2442] case this model is actually decoding uh
[2446] type of object cat dog ball and so on
[2451] what are the uh representations learned
[2454] in the hidden layer corresponding to
[2456] each of these and then Suppose there are
[2459] 20 Concepts and what is the
[2462] pairwise correlation or similarity or
[2465] dissimilarity
[2467] across all pairs of these Concepts so
[2471] here what you are comparing is what is
[2474] the representation that this model
[2476] learns and how similar or
[2480] representations across pairs of Concepts
[2483] in this case uh you know objects and so
[2488] on and if you have a brain activity
[2490] associated with this you can also come
[2493] up with a brain DSM which compares the
[2497] activation Vector associated with pairs
[2501] of these objects how similar they are
[2503] and and summarize them in this kind of
[2507] dissimilarity Matrix and look at how
[2510] similar these two matrices are through
[2512] some sort of a metric for example
[2515] represent representation similarity
[2517] metric how correlated these are that
[2521] gives you whether the model and the
[2523] Brain have a similar
[2526] a representational Dynamics when they
[2531] are encountering these different
[2532] concepts so this is uh one uh kind of uh
[2537] representational I mean uh evaluation
[2540] metric for uh uh the decoder models
[2544] right so
[2547] so uh in the next part uh another uh 40
[2552] 45 minutes I'm planning to discuss uh
[2557] few examples of decoders that are
[2560] presented
[2562] uh in the recent times as you can see
[2564] these are in the happening in the last
[2566] four or five years
[2568] this is a paper from uh
[2573] Pereira at all 2018 nature communication
[2576] looks at Word level Universal brain
[2580] decoder
[2582] let's go into the details classical
[2584] decoding solution so
[2586] brain decoding was introduced by Tom
[2591] Mitchell uh in 20 2008 there's a series
[2595] of papers from Tom Mitchell from CMU
[2600] group who has looked at decoding
[2603] Solutions extracting linguistic meaning
[2605] from
[2607] Imaging data related to concrete nouns
[2610] so these are drawings of different
[2613] objects
[2614] uh and uh participants are viewing them
[2619] along with this uh label
[2621] and uh some of these are concrete nouns
[2626] like hammer and some and all of these uh
[2630] concrete uh objects uh
[2633] they uh use similar stimuli for training
[2637] and testing and the semantic categories
[2641] are smaller in number you know given the
[2644] the time of this work 2008 the
[2647] categories they use for Animals body
[2650] parts vegetables vehicles and there are
[2653] several few exemplars of each of this
[2656] category participants viewed this and
[2659] they built
[2662] a decoding model associated with the
[2666] these
[2667] these Concepts and
[2672] they have built successfully uh decoding
[2676] models from brain activity where the
[2679] brain activity is used to predict which
[2682] category of stimulus the participant is
[2685] experiencing currently
[2688] and uh
[2690] this paper published by parallel
[2693] Builds on this work this uh
[2697] on this earlier work
[2699] uh is presented a new approach for uh
[2703] brain decoding where
[2705] a large semantic space is explored 180
[2709] different concepts both uh abstract and
[2714] concrete topics are used
[2718] these are clean from
[2721] a a large corpora from various corpora
[2726] and words and sentences are represented
[2729] as and so this representation schemes uh
[2734] Manish went through in this case they
[2737] use
[2738] a global Vector for word representation
[2741] of glove Vector 300 dimensional block
[2744] Vector is the representation for all
[2746] these Concepts in this case
[2749] these vary across several Dimensions
[2752] concrete abstract
[2754] and subjects read these uh
[2757] linguistic stimuli
[2760] on uh topics That Vary as I as I said
[2765] both in concrete topics as well as
[2768] abstract abstract such as pleasure
[2771] Justice law Etc
[2773] uh and this is the glove representation
[2776] introduced by Pennington at all 2014
[2779] that is what is used to represent these
[2782] words
[2783] and the going to the details of the
[2787] experiment they have uh
[2790] are subjects to look at three different
[2794] views right let me start with the
[2798] SE uh these three views where
[2803] the first experiment
[2806] includes uh concept plus picture view
[2810] where they are shown a picture of a in
[2813] this case the concept is birth a picture
[2816] of a bird and uh in one case and in the
[2821] other case they are shown a concept and
[2826] related words in the sort of a word
[2830] cloud format this is what the the
[2833] participants see for example for the
[2836] bird concept they see this this workload
[2841] view on the screen in another scenario
[2844] they have
[2847] the sentences that represent uh use this
[2852] idea of bird right so they look at this
[2855] sentence
[2856] so the concept word in all these cases
[2858] is bird similarly wash unaware so some
[2862] are quite abstract some are very
[2864] concrete and these three uh views
[2869] correspond to uh the three recordings
[2874] associated with a word cloud view
[2876] picture view sentence View
[2879] all these uh recordings are done in
[2882] experiment one and there were 180
[2885] Concepts that were used that had 128
[2887] nouns both nouns verbs adjectives
[2890] function words the 16 participants this
[2893] is one of the largest data sets that is
[2897] available publicly for experimentation
[2900] and they have nicely given the labeled
[2904] regions brain regions this is an atlas
[2907] of the brain that labels what is the
[2910] name of each region and so they have
[2913] looked at both
[2917] a diverse areas 333 regions or a smaller
[2922] number corresponding to an Al Atlas
[2925] automated anatomical labeling atlas of
[2929] 180 regions
[2930] so the brain activity and the stimulus
[2934] representations are provided
[2936] in experiment two and three they did
[2938] three experiments in the reported they
[2941] show sentences
[2943] uh either in this format where there is
[2947] a topic and uh musical instrument is the
[2951] topic and different kinds of instruments
[2954] clarinet accordion piano sentences that
[2958] use these are shown
[2960] and in another experiment the passage is
[2963] the on the same topic gambling there are
[2967] different passages that are shown to the
[2969] participants
[2971] so and the love representation for all
[2975] of this is is also
[2978] provided is arrived at by averaging all
[2982] the content words the glove
[2984] representations of the content words if
[2986] it is a sentence all the content words
[2988] and the corresponding love
[2990] representation are taken average and
[2993] that constitutes the the embedding or
[2997] sentence representation for that the
[3000] representation for that sentence
[3002] similarly for passage and so on
[3006] so uh they have
[3009] the overall pipeline looks like this a
[3012] stimulus is given to the participant the
[3015] brain activity associated with that is
[3018] recorded
[3019] and uh based on this 3D brain activation
[3024] informative voxels are selected and I'll
[3029] talk about that in a second on the other
[3031] side you have this
[3033] the apartment
[3036] is represented as a
[3039] in the as a as a glove Vector 300
[3043] dimensional Club Vector this is the
[3045] semantic Vector associated with the
[3048] stimulus now what you are learning is to
[3052] predict this Vector from the brain
[3056] activation in its typical decoding task
[3059] this Brain image is taken as the input
[3063] uh in this case a voxel and all the
[3068] Neighbors in the 3D neighborhood are
[3071] taken as
[3072] and as input and reach regression tries
[3076] to predict this semantic Vector for uh
[3080] apartment one small detail here is that
[3082] in this particular implementation each
[3085] Dimension is predicted separately so
[3088] there are 300 models that are built and
[3091] that try to predict each of the
[3093] dimensions of this semantic vector
[3096] and now if given X is the input W is the
[3100] model Y is the output from the model we
[3103] compare with the ground truth if
[3107] right so ground truth is this and what
[3109] is the correlation between the ground
[3111] truth and the prediction W of X is the
[3115] prediction y hat and the correlation
[3118] between that is used to
[3121] to evaluate the decoding accuracy so one
[3126] other detail here the informative work
[3129] cells are selected which
[3132] um for from different regions which are
[3135] associated with which uh that uh are
[3141] have predictive capacity for predicting
[3145] the Training Concepts uh from the brain
[3148] activity those voxels those activities
[3152] which are highly associated with the uh
[3156] the target concept are selected and in
[3160] this particular uh study 5000 about 10
[3166] percent of the total work cells are
[3168] selected based on their relatedness
[3171] their predictive capacity for these
[3174] semantic vectors and the whole
[3176] experiment is done in a 18-fold cross
[3179] validation setting there are 180
[3181] Concepts 170 concepts are used for
[3184] meaning 10 are held out and this is
[3187] repeated 18 times and what is reported
[3190] is the average over all these
[3194] 18-fold experiments
[3197] right so these voxels are selected based
[3200] on their correlation with the um with
[3204] this semantic Vector that corresponds to
[3207] the stimulus
[3209] so the pairwise and rankwise results the
[3214] first one experiment one you remember
[3216] there is a a sentence view there was a
[3220] picture view and there was a word cloud
[3222] view the three brain activations that
[3225] were recorded when participants were
[3228] looking at only the picture the concept
[3231] word and the picture or a sentence that
[3235] uses that concept word or in the word
[3239] cloud format where the cons the target
[3242] word is in the middle and the related
[3245] words are on the peripheral
[3247] so what you see here are four bars that
[3251] represent each of these dots is each
[3254] participant
[3255] uh there are 18 participants that 16
[3259] participants that participated in this
[3262] experiment one
[3264] these are 16 dots and what you see is
[3266] the average pairwise accuracy remember
[3269] this pairwise accuracy is the
[3273] uh the predicted semantic vector
[3277] how it is related to the Target uh
[3281] semantic vector
[3283] and uh you know if it is if the
[3286] correlation of that is
[3288] higher than cross correlations with
[3291] other Concepts right and uh and average
[3295] of that so the 75 percent accuracy on
[3298] average
[3299] uh across all these tasks individual
[3302] tasks are shown separately and what you
[3305] see is picture view has a higher uh
[3309] decoding performance in terms of
[3311] pairwise accuracy uh right so a picture
[3315] I guess is worth
[3318] a thousand words right to the popular
[3321] adage and I guess these brain results
[3324] also seem to bear that out so these are
[3329] participant numbers the colors represent
[3331] these 18 participants experiment two and
[3335] three uh remember where the sentences
[3339] are presented uh either from different
[3342] topics or same topic or sentences from
[3345] the same passage and as you can imagine
[3348] sentences from the same passage are more
[3352] difficult to decode compared to
[3354] distinguishing sentences from different
[3356] topics so consequently the pair was
[3359] accuracy for a different topic
[3362] decodability is a topic decodability is
[3365] much higher
[3368] similarly in Experiment three where
[3371] there are passages that are taken from
[3374] the same uh the topic or same words
[3378] within the same Passage
[3380] the right hand side is rank accuracy
[3383] from the three experiments remember rank
[3386] accuracy is the predicted the semantic
[3390] vector what is its rank compared to all
[3394] the other semantic vectors and the lower
[3398] right the the
[3401] rank accuracy the better experiment one
[3404] what you see is all these uh three it is
[3409] possible to the decoder performance is
[3412] quite uh
[3414] good in all three cases it's Superior in
[3417] the case of experiment one
[3419] remember the lower the rank the better
[3422] right first rank is better than second
[3425] rank is better than third Rank and so on
[3427] so this uh rank accuracy uh is superior
[3432] for experiment one uh on an average
[3436] so decoder wait from experiment one
[3439] could distinguish so this decoder that
[3442] is built based on the concepts from the
[3445] first experiment that are used reused in
[3448] for sentence uh topic prediction from
[3451] sentences and uh passaged you know
[3455] sentences discrimination of sentences
[3458] from same or different passages
[3460] uh so this decoder that's built seem to
[3465] have much generalized performance that's
[3468] why this is called a universal decoder
[3470] right so decoder built from experiment
[3473] one it could distinguish sentences at
[3476] different levels of granularity coming
[3479] from different topics or same topic for
[3483] for different passages or within the
[3485] same Passage the same the decoder is
[3488] actually built from experiment one but
[3491] used to test uh stimuli from decoding
[3495] performance from two and three so that's
[3498] why this paper uh is labeled and it goes
[3502] beyond the 2008 Mitchell's paper which
[3506] actually is a pioneering uh contribution
[3509] in the brain decoding literature but uh
[3513] recently yeah taking advantage of the
[3517] advances in the
[3520] uh deep learning models and machine
[3524] learning literature so this
[3528] Universal decoder has and let's look at
[3532] how uh these activation of these
[3536] informative boxes that is that are
[3537] extracted where do they reside
[3540] and what is shown here is uh the uh
[3545] different networks brain networks that
[3549] these work cells belong to and for
[3552] various participants remember that for
[3555] each participant the set of work cells
[3557] would be different and but this view
[3561] graph shows that on average there are uh
[3565] quite a few uh fraction of out of 5000 a
[3571] significant fraction around more than 20
[3574] percent come from uh boxes that are in
[3578] the language area of the brain
[3580] and similarly task related and there are
[3584] some work cells from Visual and what is
[3586] called default mode network uh these
[3590] voxel distribution this is 5000
[3593] informative work cells are roughly
[3596] distributed among the four networks
[3598] which are relevant for a linguistic task
[3602] and uh and overall the language Network
[3605] seems to have possess a higher
[3609] proportion of voxels
[3612] and another fact is that visual tasks
[3616] and default mode these are large
[3619] networks the brain areas associated with
[3622] them are large even though language
[3624] Network byte size is small its
[3627] contribution to this linguistic decoding
[3629] is High I mean as can be expected and
[3634] also on the right hand side what you see
[3636] is this is brain activation across all
[3639] the 16 participants who there seems to
[3642] be a large activity average activity in
[3647] the language areas and the temporal and
[3650] temporal parietal area and the frontal
[3653] and inferior frontal regions which are
[3655] known for language related activity
[3659] and so it seems to be consistent pattern
[3662] across all these
[3664] uh these participants so the insights
[3668] gathered from this first study which I
[3671] have selected for this tutorial that it
[3674] presents a viable approach for what is
[3678] labeled as a universal uh decoder of uh
[3683] these Concepts capable of extracting a
[3687] representation of the mental content
[3689] from the linguistic material
[3692] right so this semantic resolution of
[3696] this brain based decoding
[3698] of course will continue to improve given
[3703] you know there are a lot of advances uh
[3708] there are models which I'm not covering
[3710] here but that use recent advances in you
[3715] know using large language models
[3717] representations derived from those or
[3719] brain activation that predict those
[3721] representations all these Studies have
[3725] progressed this field since 2018 when
[3729] the spark paper was published in the
[3731] last four years there's a huge number of
[3734] studies a significant number of studies
[3737] that use latest advances in language
[3740] models
[3742] so the next one that I'm going to talk
[3747] about is uh one that was talked about
[3752] this Gap year at all to 2019 from the
[3756] French group
[3757] uh that links that looks at uh uh
[3763] artificial and neural representations of
[3766] language some interesting results this
[3768] has already been alluded to by uh you
[3772] know The Scrambled model that Manish
[3774] talked about so I will briefly talk
[3778] about it and not go into uh re-emphasize
[3782] because this has already been discussed
[3784] this is a task where participants this
[3789] is a parallel data set that they use you
[3792] already know that functional MRI brain
[3794] recording was done
[3796] when participants were shown pictures or
[3800] of Concepts
[3803] or sentences that use a concept or a
[3806] word cloud that uses
[3808] that has the the target Concept in the
[3811] center
[3813] and a neural network model that uses the
[3817] that uh derives the sentence
[3820] representation and in this case what
[3823] Gauthier and
[3825] colleagues have done is to extract uh
[3830] task-based representations instead of
[3833] using only the uh
[3836] sentence vectors you their idea was to
[3840] evaluate the link between human brain
[3842] activity and the act the representation
[3845] or the neural network model
[3849] and
[3851] and look at this as the models are this
[3855] model neural network models are
[3857] optimized for different tasks right so
[3861] task specific uh representations are
[3864] used to uh are used for prediction for
[3869] decoding task
[3871] right so
[3873] and look at why these mappings are
[3875] successful and what are the shared
[3879] representations across models and and
[3882] human brain so what they have done is
[3886] look at two kinds of representation one
[3889] is from pre-trained bird models uh and
[3894] also fine-tuned bird models these models
[3897] that are fine-tuned on different natural
[3900] language understanding tasks where the
[3902] paraphrasing or sentiment analysis or Q
[3906] and A or nli these kind of different
[3910] kinds of national language tasks this
[3913] representations that are used to train
[3917] the models and also to predict
[3920] uh the representations uh coming out of
[3924] these task-based models pre pre-trained
[3929] of fine-tuned pre-trained but but
[3933] fine-tuned on different tasks
[3937] uh apart from this they also designed a
[3941] few custom tasks one of them is this
[3944] scramble language model where a sentence
[3948] inputs uh where the words are shuffled
[3951] fingers are used for grasping writing
[3954] this is the original sentence and they
[3955] Shuffle the words within a sentence this
[3958] model is called and then they fine-tune
[3961] this language model
[3963] on this scrambled inputs right so it's a
[3966] pre-trained bird but uh fine-tuned on
[3969] these scrambled uh words the other is a
[3973] scrambled paragraph
[3975] where uh they take the words are
[3979] scrambled within a paragraph not within
[3981] a sentence but across the sentences
[3986] within a paragraph
[3988] all right so and this is called uh
[3990] language model it's scrambled para and
[3993] there is a baseline model which is
[3995] random uh sort of scrambling uh
[4000] and they have looked at the decoding
[4003] performance of of several of these
[4007] models
[4008] uh these task based models how well they
[4015] decoder predicts the representations
[4017] from these from the brain activity brain
[4020] activity is the input and
[4022] representations corresponding to
[4024] semantic task or natural language
[4027] understanding tasks or this
[4031] The Scrambled para or scrambled
[4034] models they and there's also they have
[4038] done other models where the the POS tax
[4042] the parts of speech tags are scrambled
[4045] uh right so
[4047] what you see here is the performance the
[4050] mean squared error right here mean
[4052] squared error is the metric that
[4057] strictly evaluates the ability of human
[4060] brain activations
[4062] to exactly match the representational
[4065] geometry of this model activations right
[4068] so what is brain activations are
[4071] predicting this model uh
[4073] uh you know predictive model
[4076] representations and you're correlating
[4078] with them in this case we are looking at
[4080] a metric that looks at the difference
[4083] squared or average squared error between
[4086] these two
[4087] what you see is this surprisingly The
[4091] Scrambled para and scrambled models seem
[4096] to have higher accuracy both on mean
[4099] squared error as well as on the average
[4101] rank remember the rank accuracy metric
[4104] for decoder where you the decoded
[4110] representation is compared across all
[4113] the other
[4114] candidates and look at
[4117] how well
[4119] uh these predictions rank among all the
[4124] other ground truth factors right so
[4128] again the average the lower this average
[4131] rank the better right so the para and
[4135] scramble seem to perform much better
[4137] compared to
[4138] the other
[4140] models that use that that try to predict
[4144] representations from other tasks
[4147] scrammer language models uh so I've sort
[4151] of shortlisted this for its uh uh
[4155] interesting observation uh so this is uh
[4160] the at different stages of fine tuning
[4164] what is the difference between the rank
[4167] accuracy and the squared error what you
[4170] see here is that this uh these models uh
[4175] scrambled and these have higher rank I
[4178] mean they have better rank accuracy
[4181] at different stages of fine tuning
[4187] I mean the steps fine tuning steps even
[4190] after 50 steps already you will see
[4193] Superior performance both uh in their
[4197] lower mean squared error higher a good
[4201] rank accuracy for these
[4205] uh so what we understand from this the
[4209] set of scrambled language modeling tasks
[4211] which best match the structure of brain
[4213] activation
[4214] uh these models optimized for uh
[4219] fine-tuned based on Scrambled inputs uh
[4223] seem to improve the decoding performance
[4227] uh so uh it's one observation from this
[4232] uh interesting study where the
[4234] dependencies of these
[4238] um
[4239] do not seem to matter for their decoding
[4242] model the decoding model is quite uh
[4244] robust
[4249] so uh the last but one study in the next
[4253] 15 minutes we'll talk about two more one
[4255] is
[4256] this uh this is a recent study 2023
[4261] study from Alexander Hoots group
[4263] University of UT Austin
[4266] this is a recent paper initial
[4268] Neuroscience paper very interesting
[4270] decoding exercise this is a continuous
[4273] language decode what we have seen so far
[4275] is where you uh generate either a word
[4281] embedding right isolated word related to
[4285] that concept word
[4287] or a sentence that you
[4290] so here is an attempt where you decode a
[4295] linguistic
[4296] items continuously
[4299] so here this decoder is built uh when
[4305] participants three subjects are
[4308] listening to 100 narrative stories this
[4311] is a again a very good nice data set 16
[4315] hours of listening
[4318] uh this data recorded over several days
[4322] and months from three participants
[4324] listening to thousand narrative stories
[4327] and encoding model so what you see here
[4330] is an encoding model and combined with a
[4333] decoder that tries to generate
[4337] decode what the participants are hearing
[4341] as a continuous stream of linguistic
[4345] labels that are predicted
[4348] so let me take you through this
[4350] interesting architecture
[4352] this encoding model is built by
[4355] extracting features from
[4358] so this is a narrative that's heard
[4360] through the earphones right headphones
[4363] so this is a a speech uh waveform
[4368] corresponding to the narrative features
[4370] are extracted and this feature
[4373] an encoding model is learned to predict
[4378] the brain response corresponding to this
[4381] narrative when they are listening to
[4384] this narrative what are the activations
[4386] in the brain can I
[4389] predict this through an encoding model
[4392] a detailed uh account of how these
[4396] encoding models are built will come
[4398] after lunch when Maria will take you
[4401] into encoding model modeling literature
[4405] but here is an example that uses an
[4408] encoding model in order
[4411] profitably to improve decoder
[4414] performance right so this part is clear
[4416] where you have
[4418] the stimulus features generate bold
[4422] response
[4423] okay and what is shown here this
[4426] encoding model is used in this scheme
[4430] where this decoder brain decoder
[4433] it maintains us a a set of candidates
[4438] that to reconstruct the language from
[4442] the novel brain recording right the
[4444] decoding is given brain recording can
[4447] you reconstruct the stimuli that they
[4450] are listening to
[4452] so in order to reconstruct uh the
[4455] decoder maintains a set of candidate
[4458] word sequences that I started off with I
[4462] saw a big dog I saw a dog and so on
[4464] these are the various candidates that
[4467] are maintained
[4468] and then these candidates are when new
[4473] words are detected a language model
[4476] right as it is language model tries to
[4481] predict this is a language model that
[4484] tries to predict based on this candidate
[4487] what are the continuations proposed
[4489] continuations of this so I saw a dog
[4492] could be continued with I saw a dog with
[4495] or I saw a dog and and so on
[4499] now these are continuations potential
[4501] continuations for this
[4503] now these uh word sequences are the
[4510] features extracted from these are
[4511] multiplied or Asus you know they are uh
[4518] they are used to generate uh brain
[4522] activity remember encoding model that
[4525] you have trained you can use it in order
[4527] to predict what is the possible brain
[4530] activation if this is the continuation
[4532] what is the brain activation
[4534] so these are the predictions and the
[4538] decoder predicts uh what what is done is
[4542] these are rank ordered this this uh the
[4546] encoding model scores the likelihood of
[4549] the recorded brain responses under each
[4552] continuation so the encoding model gives
[4556] a rank and the one the most likely
[4560] continuations are retained and so this
[4563] sort of process where an encoding model
[4568] it uh ranks the possible brain
[4573] activations and those and the associated
[4577] continuations are the decoding solutions
[4580] for uh that are associated with a given
[4584] brain activation
[4585] so this kind of a encoder decoder model
[4588] seem to have done very well this uh
[4593] these are some of the results these are
[4596] actual stimulus
[4599] sequences and these are decoded stimuli
[4601] what is shown this color code is these
[4604] are exact predictions some of them
[4607] are exact prediction some of them have
[4611] just for example uh I got up from the
[4615] air mattress air mattress and pressed my
[4617] face against the glass of the bedroom
[4620] window what is it I just continue to
[4622] walk up to the window and open the glass
[4625] and so some words are of course errors
[4628] there is
[4630] these are erroneous words there's a few
[4633] of them are errors so this is a view of
[4637] a different decoding solutions for
[4641] different sentences these are
[4643] continuously generated uh linguistic uh
[4649] items into as a form of continuous
[4652] sentences
[4654] and what this particular graph shows is
[4659] how well this decoder performs what is
[4663] the story similarity
[4666] uh across different metrics the bird
[4669] score is one of the recent uh
[4672] scoring systems which newer method which
[4676] uses machine learning ideas to quantify
[4679] whether two sequences share a meaning or
[4682] not
[4683] right so on all of these what is shown
[4686] here for the three participants
[4689] the decoding the story similarity that
[4693] is the based on the decoder they are
[4697] well above chance level and the star
[4701] tells you if it is statistically
[4704] significant there is a
[4707] false Discovery rate metric that is
[4710] computed estimated so all these decoder
[4713] performances are much about chance level
[4716] and across word error rate blow rating
[4720] uh different ways to measure the story
[4724] that is decoded and the original story
[4726] how similar they are
[4728] and this this continuous decoder seems
[4732] to perform very well
[4734] to summarize what this particular paper
[4739] 2013 23 Paper talks about a continuous
[4745] language representations that can be
[4748] decoded or reconstructed from
[4751] uh function MRI recordings
[4754] which are non-invasive so we have a way
[4758] to measure brain activity from that you
[4761] can actually construct reconstruct what
[4764] this brain activity corresponds to in
[4767] terms of a continuous language
[4768] representation
[4770] so given novel brain recordings this
[4773] decoder generates the stories which are
[4776] word sequences that form story which are
[4779] intelligible based on variety of metrics
[4782] we saw about score and various other
[4785] blow and other spores
[4788] that recover meaning of this this
[4793] experienced speech perceived and
[4798] so there's other tasks that are done I
[4801] am not going through those uh in the
[4803] interest of time but but leave you with
[4806] this idea of exciting possibility
[4809] enabling uh
[4811] uh decoding one of the important things
[4814] for Technologies the decoder building is
[4818] a gateway into building better brain
[4821] computer interfaces especially for
[4823] people who have challenges because of a
[4829] disease or accident or whatever that
[4832] compromises their linguistic function
[4835] their ability to express
[4840] commands or Converse in national
[4843] language is compromise now
[4847] these results begin to show promise in
[4850] terms of their ability to uh
[4854] one day
[4856] for us to build a brand you know more
[4859] efficient brain computer interface
[4862] models
[4863] in the last few minutes I will talk
[4865] about some of uh the work that we have
[4868] done on multi-view on Cross View
[4869] decoding this is based on pereira's data
[4873] set
[4874] we asked this question can we use the
[4877] information that is available within the
[4881] brain activation to go from one view to
[4885] the other
[4886] suppose I show you a concept
[4889] right these different views of the
[4891] concept bird it's a sentence that uses
[4895] this or the picture that uses that
[4899] concept or the word cloud that
[4902] depicts the meaning in this sort of uh
[4906] related words surrounding it can we use
[4911] these to go from one viewer to the other
[4913] view for this concept right earlier
[4916] Works have explored uh
[4919] uh which of these views for example we
[4922] looked at the IRS results which of these
[4925] views provides richer information to
[4928] understand the concept
[4929] and we saw that pairwise decoding
[4932] accuracy rank accuracy for picture view
[4935] was better so what we are asking is a
[4938] different question can we use train a
[4941] model with word cloud View
[4943] and test it with other views sentence
[4947] view or picture view or how General this
[4952] decoding uh the model that you build how
[4956] generally is it to generate
[4958] representations that
[4960] correspond to sentence view picture view
[4963] what cloud right so itself and similarly
[4967] picture view and look at other views and
[4972] sentence view brain data used to decode
[4976] uh representations of the other views
[4979] this we label this as multi-view
[4982] decoding this is presented in calling
[4985] last year
[4988] so this uh
[4991] I am straight away going to the results
[4993] these are uh picture view pairwise
[4997] accuracy we use birth and uh the
[5000] baselines but random attuned with
[5004] I mean this is uh
[5008] random uh intenses this uh these are
[5013] three uh uh built based on brain
[5016] activation
[5019] uh decoding word a picture decoder
[5023] this is sentence decoder word cloud I am
[5027] training with picture view obviously
[5029] picture will have higher accuracy but
[5032] what You observe here is the accuracy
[5034] for decoding other views sentence View
[5038] and word cloud view is not too bad of
[5041] course it is inferior to the original
[5044] trained scenario but the same model is
[5049] able to to decode uh Concepts from the
[5055] sentence View and
[5059] um a word cloud view right this is a
[5061] shuffled trained on
[5064] shuffled Target Concepts right so this
[5067] is
[5068] uh this is rank accuracy also paints a
[5072] similar picture higher accuracy for
[5076] uh train but not bad not too bad for uh
[5080] other
[5082] uh decoding other views right ranks and
[5085] similar story for sentence View
[5089] and word cloud view right so uh
[5094] uh
[5096] interesting then that you see a model
[5100] that is trained on sentence view has
[5103] similar performance on all the other
[5105] views whereas a model trend on word
[5108] cloud View
[5109] has good performance in the other
[5112] picture and sentence
[5115] um
[5117] yeah so but not in its own
[5121] so pictures seems to be best accuracy
[5125] sentences
[5126] for these seems to be best accuracy in
[5131] this multi-view decoding concept so the
[5134] main idea here that uh
[5136] uh is being explored is how General are
[5140] these decoding models that we built
[5143] based uh and their generalizability
[5146] across different views uh and these are
[5150] the distribution of informative work
[5152] cells uh across different brain regions
[5155] language regions like left language
[5158] right hemisphere language regions vision
[5162] uh and what you see here is uh the
[5166] proportion of uh
[5168] informative work cells in left language
[5171] regions for sentences is higher in the
[5174] left hemisphere and it is well known in
[5177] cognitive Neuroscience
[5180] left hemisphere
[5182] specialization for language
[5184] representation is based out and vision a
[5188] region for example has uh much more many
[5193] work cells that correspond to word and
[5195] picture view again not very surprising
[5199] because the task here the stimulus has a
[5203] rich visual information so the vision
[5205] areas have a lot more contribution to
[5209] this decoder model
[5212] so the other uh in the last couple of
[5215] minutes I will take you through this
[5218] cross view decoding this is another task
[5220] that we
[5221] so can we decode from one view you know
[5225] what we looked at is going from a model
[5228] built from one view can you generalize
[5230] to other people
[5232] so the other question that we asked is
[5235] can we train with picture view
[5237] but uh
[5239] generate captions
[5242] for the images that you are seeing right
[5245] the image captioning sort of task the
[5248] other is image tagging task I train with
[5250] picture view
[5252] and can you come up with the image tags
[5256] so decode image Stacks visual words in
[5260] this case caption and the last one is
[5262] can you actually generate a sentence
[5266] sentence formation process so I have a
[5270] decoder that is trained on
[5272] brain activation given brain activation
[5275] it it predicts word cloud View and take
[5278] this decoder but use it to
[5282] so to generate a sentence from that
[5286] right sentence formation
[5288] and the last one is keyword extraction
[5290] which is again published recently in
[5293] calling from our group uh that these uh
[5297] cross view decoding is also feasible
[5300] these decoders that we can build are
[5303] quite generic uh we can
[5306] uh quite a good performance pairwise and
[5310] rank accuracy for all these tasks of
[5314] course sentence formation is a very
[5315] complex task the accuracy is lower but
[5318] it's still feasible much better than
[5321] this shuffled models so image captioning
[5325] keyword extraction all these are
[5327] feasible from this is the average over
[5330] all these experiments these uh so these
[5334] different tasks uh image captioning
[5337] decoding performance average accuracy
[5341] and so on so these are these are
[5344] shuffled concept this but
[5347] fine-tuned with shuffled Concepts and
[5352] the summary is that the cross view and
[5357] multi-view decoding tasks tasks
[5359] established
[5360] uh that so the uh information that is
[5365] there in the brain responses
[5367] is actually rich
[5369] uh
[5370] this is what the hypothesis for us was
[5373] that the brain activation is much richer
[5375] and it is possible to utilize this to
[5380] put this into service for variety of
[5382] tasks although this activation was seen
[5385] for a particular task and you know that
[5388] the brain has these distributed
[5390] activation and it is possible are
[5395] results indicate that is possible to use
[5398] this to multiple Downstream tasks right
[5402] so
[5403] uh to summarize what I have discussed in
[5407] this session in the last one hour is
[5410] present you with three different themes
[5415] one is this Universal brain decoder
[5417] which has actually set off
[5419] uh a series of Investigations by variety
[5424] by various investigators this Universal
[5428] brain decoder that has put this language
[5431] decoding again on the uh in the radar
[5436] and we looked at how the artificial and
[5440] human neural representations can be
[5443] utilized one exciting example that I
[5446] presented is this continuous language
[5449] decoder
[5450] that seems to now generate continuous
[5454] sentences uh linguistic sequences word
[5457] sequences associated with brain
[5460] activation
[5461] and the multiview and cross view
[5463] decoding give you an idea that these
[5466] decoders have lot more uh
[5470] um or representation than that can be
[5474] used to
[5476] actually use them for multiple
[5478] Downstream tasks
[5480] okay so uh this is a good time
