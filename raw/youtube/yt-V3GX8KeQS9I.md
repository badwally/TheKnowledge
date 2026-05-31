---
schema_version: 1
id: yt-V3GX8KeQS9I
type: youtube
title: Part-1 of our IJCAI tutorial on deep learning for Brain Encoding and Decoding
url: https://www.youtube.com/watch?v=V3GX8KeQS9I
authors:
- Data Science Gems
ingested_at: '2026-05-30T21:59:38Z'
content_hash: sha256:0f0e659498b22cd54ec315d7312179553a9a4a9ebff3fd6a9ef3c21b005093ea
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Data Science Gems
  channel_url: https://www.youtube.com/@dlByManish
  duration_seconds: 5277
  caption_track: fetched
  snippet_count: 2145
filter:
  score: 0.75
---
[2] foreign
[11] welcome to this tutorial on deep neural
[15] networks and brain alignment brain
[18] encoding and decoding uh first off
[23] let me on behalf of all the pr all my
[27] co-speakers on this tutorial I apologize
[29] for not being able to come there
[31] physically
[33] various logistic issues and we should
[35] have planned better but here we are
[39] uh with the help of a bunch of
[43] volunteers including pritam who is there
[45] as a host and later
[48] Professor Pacific ball and uh ankan
[53] Malik who are going to help us post this
[56] and hope we'll have as near to physical
[62] tutorial as we can make it given the
[65] scenario
[67] so without much further Ado let me start
[71] the proceedings the agenda for today is
[77] this
[80] uh we have a
[84] the session is organized in four
[87] different sort of segments the first
[90] segment one and a half hours before
[92] coffee break we I'll start with the
[95] basic idea of what uh functional MRI
[98] what brain recordings are encoding
[101] decoding what the problem that we are
[105] planning to give solutions for and
[109] followed by Manish Dr Manish Gupta from
[112] Microsoft
[114] India who is going to present
[117] um stimulus representations
[119] uh and that might spill over after
[122] coffee break then I'll pick up again for
[126] discussing uh brain decoding Solutions
[130] is a typo here uh we'll start with brain
[133] decoding today for uh an hour before
[136] lunch break then we'll break for lunch
[138] we come back and then Dr Maria toneva
[142] from Max Planck Institute she is going
[145] to talk about brain encoding so again
[148] this is a type of one and a half hours
[151] before coffee break afternoon coffee
[153] break followed by the last session where
[156] we'll discuss Advanced methods and
[159] summarize the session
[161] and uh yeah let me start with the basic
[165] introduction
[167] and ideas related to brain encoding
[171] decoding techniques and what are the
[174] research goals that uh
[176] we are going to address
[179] uh in the field of Neuroscience so what
[182] we are looking at today is an
[184] interdisciplinary sort of approach to uh
[189] combine brain deep learning models in
[193] the service of Neuroscience
[195] so field of Neuroscience looking at
[198] brain function and structure and how
[202] they are related and looking at various
[204] questions
[206] related to how brain learns during both
[210] during childhood adolescence and how
[213] this learning and memory deteriorate our
[216] aging all of these is interesting to see
[220] what areas are included how the
[222] structure declines how the function uh
[225] is most of the function is intact but
[228] some of it declines with age all these
[232] questions are of Interest along with
[234] various cognitive functions memory
[236] attention decision making how speech and
[240] language are processed in the brain what
[243] areas and how what is the representation
[247] brain uses for uh representing language
[252] speech and various other perceptual
[254] dimensions and how they are process to
[259] do uh you know higher order cognitive
[262] functions like reasoning and so on
[265] planning
[266] and so neuroscientists are interested in
[269] these diverse topics I understand the
[272] structure and function uh that subserves
[275] these functions and we would also like
[278] to see if uh any insights that
[282] understanding how brain represents could
[284] inform deep learning models and AI in
[288] general
[290] so
[291] um so let me then look at the
[295] workshop is centered around two main
[300] Concepts brain encoding and decoding and
[304] these are very important problems how
[308] does brain import information
[310] and how is it possible for us to decode
[314] the information from brain responses so
[318] the first bullet here is encoding
[321] process the process of learning a
[323] mapping E from the stimulus side as
[328] stimuli to the brain response so this is
[332] the mapping that we are learning from
[335] stimulus representation to predicting
[338] brain response a model that takes in
[341] input as stimulus representation either
[344] in the form of uh
[347] uh a categorical information features
[350] uh derived from traditional feature
[354] engineering machine learning approaches
[356] or from Deep neural networks you uh
[360] derive representation and map that and
[363] see how that match to predicting brain
[366] function right so this is one task
[369] encoding learning this mapping e that
[373] goes from stimulus to brain Activation
[375] so the other major task that we are
[377] interested is decoding
[379] so given the brain response F can we
[385] predict the stimulus representation
[388] and in uh some cases actually
[392] reconstruct the stimulus the brain is
[395] experiencing right so this is the other
[397] way around given the brain response can
[400] be
[402] predict the stimulus features or predict
[407] reconstruct the stimulus itself that is
[409] the decoding task and the other is mixed
[414] uh sort of other forms of encoding
[417] decoding where you are doing this
[420] encoding decoding using responses from
[423] the participants map participants
[426] Behavior to behavior to the brain
[428] response or from the brain response
[430] predict the participant Behavior it
[433] could be for example a perceptual
[435] stimulus that is given and they are
[438] asked to look at whether they can
[440] see what is being shown in a rapid
[443] presentation or they cannot distinguish
[446] all they are unsure they can see what
[449] they are I'm sure suppose this is a
[451] perceptual decision making task from
[453] which the behavior is mapped to brain
[456] response and from the brain response you
[458] are predicting these outcomes you can
[461] also do this among multiple brain active
[464] activity regions
[467] right so as uh so to summarize uh the
[472] encoding uh is learning a representation
[475] from brain resp from the stimulus
[478] representation to brain response and we
[481] do this typically uh for example using a
[485] regression function you learn the
[487] mapping between stimulus representation
[490] and the brain response and in this case
[493] in the decoding case you are learning
[496] this function D that Maps brain responds
[500] to stimulus representation as these
[504] functions e and D can be used to once
[507] you learn them you can use them to
[510] predict uh either brains activations in
[515] the case of encoding or stimulus
[518] features or representation in the case
[520] of decoding for new
[523] stimuli that were not used during
[525] training
[527] now uh in the next couple of slides I
[530] will take you to how these brain
[534] responses are actually recorded
[539] there are what you show here is a graph
[542] the horizontal axis is temporal
[545] resolution low temp you know very high
[549] temporal resolution or low numbers here
[552] and which goes into milliseconds or sub
[555] millisecond level to a course temporal
[559] resolution which is of the order of
[561] seconds on the vertical axis you have
[564] again a force a very high spatial
[568] resolution to course spatial resolution
[570] measured in terms of millimeters of the
[573] cortex from which you can record so what
[577] you see in the yellow are invasive
[580] recording approaches for example where
[582] an electrode is inserted into the uh
[586] into the cortex in order to look at
[590] brain responses the blue ones are
[593] non-invasive responses for the most part
[596] of this tutorial we are interested in
[598] these kind of recordings
[601] or either looking at the electrical or
[604] magnetic field from the scalp EEG or Meg
[608] electroencephalography or
[611] magnetoencephalography and the other is
[613] looking at blood flow features from the
[616] blood flow and how they change when
[620] participants are engaged in a task the
[623] most popular one is the functional
[626] magnetic resonance imaging MRI I hope
[629] most of you are familiar with uh is a
[633] procedure that is done to look at the
[636] structure of your body parts including
[640] brain but here the small F here refers
[643] to functional MRN and one of the recent
[646] uh
[647] non-invasive techniques is infrared
[649] spectroscopy based functional cortical
[653] function
[655] recording called nears or avenirs
[659] uh so these are some of the techniques
[662] and uh so function MRI
[665] and EEG Meg and FNS are the ones that we
[670] will look at as I told you already
[672] functional MRI has
[675] um uh as per this graph there's a high
[678] is a lower temporal resolution but very
[681] high spatial resolution
[683] um uh and compared to EEG and F nurse is
[689] some sort of a compromise option
[693] and the actual recording device looks
[698] something like this this is a typical
[699] MRI Scanner with a large magnet into
[703] which participants are wheeled in and in
[707] our case the object of interest is the
[710] brain so uh the uh when you wheel in and
[715] there are head coils inside that allow
[717] you to record brain activation
[720] uh while participants are engaged in
[722] task and what is shown below is a
[725] functional MRIs
[726] processed functional MRI scan which look
[730] which shows you activation the posterior
[732] part of the brain this is the front part
[735] in the back part posterior part where uh
[739] significant activations are indicated by
[741] these uh yellow and red blocks
[745] so uh the function MRI is very
[748] attractive for cognitive Neuroscience
[750] investigation because it does not
[752] involve any invasive procedure the
[756] inherent uh blood oxygen level dependent
[761] contrast which is inherent within the
[764] brain that is what is math used to get
[768] an estimate of the function of the brain
[772] right so and uh and hemodynamic response
[777] function so the couple of features that
[778] we need to be mindful of that since this
[782] procedure looks at blood response uh
[786] constituents of the blood and how they
[789] respond to to brain function there is a
[793] delay that is
[795] in the uh in the recording so what you
[800] see is activation is actually uh what
[803] happened five seconds ago so these are
[805] not sort of instantaneous measurements
[808] this is something to keep track of or
[810] keep in mind while designing
[813] computational models so the next issue
[817] that we want to look at is what is the
[819] goal in this right given these kind of
[822] measurements that are available when
[824] participants are engaged in tasks so the
[828] cognitive science uh especially the
[833] computational modeling that is applied
[835] in cognitive science research looks at
[837] primarily three uh aspects one is
[840] predictive accuracy can we build models
[843] that accurate models that aim to uh
[849] that are useful for understanding how
[852] brain Imports information
[854] and the feature deportability from the
[858] neural data so how accurate these models
[862] are and how can we increase the accuracy
[865] of these models predictive accuracy so
[868] this is the one dimension the other
[871] dimension is interpretability of the
[874] models thus designed and can we look at
[880] uh
[881] What uh convolutional neural network for
[885] example that models the brain function
[887] what kind of representations that are
[890] learned in the layers of these cnns
[894] versus what happens in the actual brain
[897] in the visual area for example a CNN
[900] that is learning visual representation
[903] and what kind of deep learning features
[907] that are learned versus uh what is the
[910] representation hierarchical
[912] representation the visual system in the
[914] brain
[915] and uh so uh this uh interpretability
[921] allows us to map the what happens in the
[926] models to theories of brain function
[929] right so uh this is very important sort
[933] of Dimension when we are
[937] making these models the third dimension
[940] obviously is biological possibility of
[943] course is there a concordance between
[946] what you are seeing in your deep
[948] learning model and what actually is
[951] happening in the brain and
[954] incorporate measurement can be
[956] incorporate biologically realistic
[959] measurement related considerations when
[962] we are such as for example uh
[964] hemodynamic response function it is
[967] possible that this response varies
[969] across the cortex uh you know from
[973] sensory to motor to association areas
[976] the hemodynamic response function may be
[978] different can we incorporate this
[981] biological fact into the models this is
[984] one concern the other is that but if we
[987] build these linear readout models
[992] can we look at what additional
[994] computations of uh are Incorporated in
[1000] order for the downstream functions to
[1003] work right so this biological
[1005] possibility
[1007] predictive accuracy and interpretability
[1011] all these Dimensions which are important
[1013] for us
[1014] in the next few minutes five or ten
[1018] minutes I am going to take you into some
[1021] of the popular data sets and what is the
[1026] playground for building these models
[1028] what is the
[1030] current availability of variety of data
[1033] sets and variety of cognitive functions
[1037] that these data sets correspond to so
[1040] that we can now start going into
[1042] stimulus representations how do we
[1044] estimate them how do we use them to
[1046] build models so
[1049] um let me then move on to the different
[1054] types of stimuli and popular data sets
[1057] this is a slide that tells you each
[1059] bullet corresponds to one more more
[1063] modality text textual data visual
[1068] auditory video and multi-modal stimulus
[1071] data
[1072] so here are some data sets popular data
[1076] set names Harry Potter story data set
[1079] Zuko EG data set these are data sets
[1082] that look at textual stimuli and how
[1086] brain responds in participants
[1088] uh either toward word stimuli sentence
[1092] stimuli or paragraph stamina and the
[1095] other ones are visual stimuli is a basic
[1098] visual patterns either binary or much
[1103] more nuanced or
[1105] visual patterns natural images there's a
[1109] natural images vim1 data set board 5000
[1112] is a data set name and so on and the
[1115] auditory stimuli when people are
[1117] listening to stories for example through
[1120] their auditory system so we give
[1122] headphones and they are listening to the
[1124] story for example
[1127] a narrative State asset or a math radio
[1130] or is a a big data set that's available
[1133] for us where the auditory stimulus as
[1137] well as the brain response from the
[1139] participants is made available through
[1141] these repositories and video data set
[1144] where people are watching videos either
[1148] this famous Doctor Who BBC's show or
[1152] Japanese ads data set this is a video or
[1155] data set where the stimulus is a video
[1157] and you are continuously recording brain
[1160] activity as participants are engaged in
[1164] this passive viewing task for example
[1167] so the last one is multi-modal stimuli
[1170] in which there are both the linguistic
[1173] the textual representation and a line
[1175] drawing of the concept that this word
[1178] represents for example Pereira data set
[1181] which we will discuss in more detail
[1183] when we talk about decoding models and
[1186] so on
[1188] okay so in the uh the other dimension is
[1192] the types of uh recording either a
[1197] functional MRI all these are
[1199] non-invasive recordings fmri EG Meg F
[1203] nurse is also there's one data set
[1206] that's available uh few data sets in the
[1209] infrared spectroscopy emission all these
[1212] non-invasive and the sampling rate is
[1216] another feature which is important and
[1219] uh uh the in some cases the eye
[1223] movements when participants are engaged
[1226] in looking at stimuli those are also
[1229] available
[1230] and uh and we this point we covered uh
[1234] uh the the stimulus modality could be
[1238] any of these and in some of these uh
[1241] cases where the participants are engaged
[1244] in a a memory task for example recognize
[1249] if you have seen this object before
[1250] typically called one back task or a
[1254] question answering task or a property
[1256] generation task or a national language
[1259] understanding task uh so these data sets
[1264] can vary along these task dimension
[1267] the other is time given to participants
[1269] and the types of participants
[1272] gender wise or in one of the data sets
[1277] we have both the cited and visually
[1280] challenged that are actually processing
[1283] auditory stimuli and we look at
[1286] comparative analysis of how the brain
[1289] representations are different or similar
[1292] and how many repetitions of the stimuli
[1296] that were recorded and the the last one
[1300] is the language uh are these which
[1303] language are they stimuliant are these
[1306] in English or Italian French Chinese
[1309] Japanese and so on the language
[1313] so here is a whole list I am not going
[1315] to go through all of them but highlight
[1317] one or two of them uh this is a data set
[1321] uh
[1323] by our standards an older one 2016 data
[1327] set where uh the task given to
[1330] participants is a property generation
[1332] task and the second Anderson data of
[1336] 2017 where participants are imagining a
[1340] situation and not only is given and they
[1342] imagine a situation and while they are
[1345] doing this imagery task or their brain
[1350] response is recorded or in another case
[1353] movie quality is rated they view a movie
[1356] clip and they do they give a rating on
[1360] that so this is the first data set this
[1362] uh of
[1366] um
[1366] where participants are given a stimulus
[1371] either in the visual form or in the
[1374] pictorial form or in the auditory form
[1378] and they have to
[1381] given this stimulus they have to
[1385] uh
[1388] uh they have to uh mentally
[1392] go through what kind of properties that
[1395] come to their mind right a pineapple is
[1398] a fruit and it is sweet and so on and
[1401] several participants both cited as well
[1405] as visually challenged congenitally
[1407] blind or given these recordings are
[1410] available in this data set as put out in
[1413] 20 uh
[1416] 16.
[1417] so the next data set is uh Italian word
[1420] stimulus data set and the functional MRI
[1423] recorded and these words come from two
[1426] domains law and music both abstract as
[1430] well as more concrete uh uh
[1433] words that come from either law domain
[1436] or music domain and participants have to
[1440] uh uh passively look at these experience
[1444] these stimuli
[1446] right so the other is a language
[1448] processing cognitive language processing
[1451] Zuko data set where participants are
[1454] given material uh from Wikipedia uh uh
[1459] where there is a normal reading but you
[1462] manipulate the sentiment of the or
[1466] relations or uh they are asked questions
[1469] about relationships that exist within
[1472] the stimulus or the comment about the
[1476] sentiment of the of the particular
[1479] stimulus sentence that is given to them
[1482] right so this uh reading speeds all of
[1486] this this is a easy data set that is
[1488] available
[1490] PG as well as eye tracking data set that
[1493] is
[1494] made available publicly for us Zuko
[1499] so the next Dimension is visual stimulus
[1502] data again this is a whole host of them
[1505] some of them are highlighted here
[1508] passive viewing data set is an old 2006
[1512] data set where people are viewing uh
[1517] Visual Basic visual patterns and then in
[1520] the other case they are looking at
[1522] object images and they either do a
[1526] one-pack task or a passive viewing of
[1528] natural images or object images
[1532] right so I'll uh skip this this kind of
[1536] data set we are not interested currently
[1538] and this is a basic visual patterns that
[1541] are given and participants are asked to
[1543] remember which pattern they have seen
[1545] before
[1547] and in another task I want this
[1553] in 20
[1555] 17
[1556] please recorded this data set and made
[1559] available where participants are either
[1563] asked to do in one condition
[1565] one back task have you seen uh the
[1569] current image that you are seeing is it
[1571] repeated from previous uh right so they
[1575] have to keep monitoring the other case
[1579] where they give a queue and a word is
[1581] highlighted and during the evaluation
[1584] period they need to
[1586] think of all the properties that that
[1590] correspond to the highlighted word and
[1593] then they need to give how confident
[1595] they are with the sort of imagination
[1598] they have
[1600] exercised on that particular stimulus
[1603] that's a board 5000 data looking at uh a
[1608] huge collection of is a 20 hour
[1610] functional MRI scans from each
[1613] participant it's a really a big effort
[1617] looking at variety of images from Coco
[1620] database image net scene image database
[1623] around 5000 Unique Images are given
[1627] and participants data brain passive
[1631] viewing data set is collected
[1634] Argonauts is actually a challenge that
[1636] is running uh almost every year this is
[1641] from one of the years where brain
[1643] encoding challenge where you have to
[1646] look at how to predict the brain
[1649] response when people are viewing uh
[1651] images of objects
[1654] its auditory stimulus data set where uh
[1657] participants are either passively
[1660] listening to a narrative since the
[1663] narrative large data set
[1666] 345 second stimulus 27 diverse stimuli
[1671] to 345 participants data massive data
[1675] set that has been recorded at Princeton
[1678] from the Princeton group passively
[1680] listening to a narrative spoken
[1684] narrative right so I'll skip this in
[1687] this case that uh data set where you are
[1691] imagining scenarios there are 26
[1693] participant common scenarios from
[1696] reading resting writing bathing cooking
[1699] housework these scenarios are given and
[1702] you are supposed to visualize what
[1705] happens in those and what are the
[1707] attributes of the particular
[1710] imagination scenario that people have to
[1714] rate the kind of attributes they
[1716] experienced the experiential attributes
[1719] are rated by the participants
[1722] so this is the narrative data set uh so
[1725] the
[1726] um the finally the video stimulus data
[1730] set this is again a rich data set where
[1733] participants are viewing uh ads
[1736] passively viewing either short clips or
[1740] Japanese ads these are taken from either
[1743] entity uh I mean web uh or TV ads and
[1749] people four types of labels that are
[1752] associated see in descriptions uh
[1755] Effectiveness indices preference votes
[1758] uh these are the diverse categories from
[1761] which these ad advertisement movies are
[1765] video clips are taken
[1768] all right so this is uh algonauts uh
[1770] 2021 challenge data set where short
[1773] video clips are given and uh we have to
[1777] build models their brain response
[1779] corresponding to when subjects are
[1781] looking at a video like this are
[1784] provided and you can now use this data
[1787] set to uh to constitute encoding and
[1791] decoding tasks okay so the last one is
[1794] multimodal data set there is a question
[1796] answering passive viewing I'll talk
[1800] about this more detail when I discuss
[1803] decoding models so uh let me skip this
[1808] this is the uh uh 2012 data set from uh
[1813] Tom Mitchell's group who was a Pioneer
[1816] in this uh in this domain of encoding
[1819] and decoding this is the parayra data
[1821] set where a picture and uh
[1824] representation uh representative
[1827] sentences that describe this concept or
[1832] a word cloud that looks at this uh
[1834] different uh concept and the related
[1837] words
[1838] right so brain activity associated with
[1841] all these stimulus modalities are
[1843] present or recorded the last one for
[1847] completeness I am also showing this
[1850] data set where these Optical recordings
[1854] are done when participants are engaged
[1857] in audio visual stimulus processing
[1860] right so given that we discussed briefly
[1865] and rapidly various types of data sets
[1869] now I hand over to manage to go into
[1874] details of how the stimuli could be
[1877] represented yeah Manish
[1885] thank you Professor Papi yeah I think
[1887] that was a quick and uh uh like uh yeah
[1892] I mean a quick and exhaustive
[1894] description of various kinds of uh data
[1897] sets and the way uh been encoding and
[1900] decoding field has evolved over years
[1903] right uh I'll basically get started uh
[1907] let me start by sharing my screen hope
[1909] all is good
[1910] so uh just to sort of uh give a brief
[1914] recap of what Professor puppy sort of
[1916] covered we talked about already about an
[1919] introduction to brain encoding and
[1921] decoding so he talked about encoding
[1923] which is a process of taking the stimuli
[1926] and being able to predict your brain
[1928] activations right on the other hand
[1930] decoding is a process where you actually
[1932] take those brain activations and in some
[1935] ways try to magically identify what this
[1938] guy would have seen or what this guy is
[1940] thinking or what this guy has just read
[1942] and so on right so in some ways it's
[1944] sort of nothing short of Magic the brain
[1946] decoding process
[1948] and then we talked about various data
[1951] sets in fact we looked at five different
[1955] types of data sets based on modalities
[1957] text visual audio video and other
[1960] multimodal stimuli and we also saw how
[1964] these data sets are obtained in
[1966] different kinds of settings so there are
[1968] fmri EG Meg settings and they varied
[1971] based on how frequently you sample the
[1974] next brain response uh fixation points
[1977] so as to actually record them more
[1979] accurately
[1980] forms of different stimuli what is the
[1983] active task that the participant is
[1986] doing so as to sort of unders so as to
[1988] make sure that there is less noise in
[1990] those recordings so the participant is
[1992] actively the noise is lesser right then
[1995] how much time is given to participants
[1997] uh what are the kind of participants uh
[2000] number of times the response to stimuli
[2001] was recorded what is the language in
[2003] which the stimuli is presented if it's
[2005] text based right so we looked at these
[2008] various text stimuli data sets
[2010] um and and and and and so on right so
[2013] essentially Professor Papi also went
[2014] into details about some of these text
[2017] visual uh audio uh video and multimodal
[2021] kind of stimulus data sets right so uh
[2024] so while this might have been like you
[2026] know you might have thought that this
[2027] was sort of a little rushed but remember
[2029] that this is just the basis of each of
[2031] these data sets each of these kinds of
[2033] stimuli we are going to talk a little
[2036] bit in more detail uh over the next few
[2038] sessions right so essentially for
[2040] example uh in this session I am going to
[2043] talk about stimulus representations so
[2046] you have those data sets uh with
[2048] different kinds of stimuli whether it is
[2050] text images or audio or video how do you
[2054] replay present them because once you
[2056] represent them you can actually build a
[2059] very simple small little adapter modules
[2061] for example just a let's say a bridge
[2064] regression and then use them for brain
[2066] encoding similarly the stimulus
[2069] representations are also very important
[2071] when you are trying to decode things so
[2073] if you are doing brain decoding uh
[2075] earlier pieces of work specifically did
[2078] not really decode it to the actual
[2080] stimuli so by looking at brain
[2082] activations it's not like you'll be able
[2084] to exactly guess what was the actual
[2087] text that this guy saw right or what was
[2090] the actual image that this person that
[2092] this participant actually saw but what
[2094] you would be able to guess is a good
[2096] representation of that image that the
[2098] participant visualized
[2100] so therefore these stimulus
[2103] representations play an important role
[2104] so in this hour you know I will talk
[2106] about these stimulus representations and
[2109] then later uh you know after the coffee
[2112] break
[2113] professor babiraju in fact will come
[2115] back again uh you know a little bit
[2117] after the copy of a break I mean I'm
[2119] assuming uh we will still spill over a
[2122] little after the coffee break and then
[2123] Professor Babi Raju will come back again
[2125] and he will talk about print decoding so
[2128] we will get into deep details about each
[2131] of those methods which have been used to
[2133] take these stimulus presentations uh and
[2136] uh to take the brain recordings and be
[2139] able to decode them some of them just
[2141] decode back to stimulus presentations
[2143] while more recent methods have tried to
[2145] decode back to the original text or
[2148] images right then we'll have a lunch
[2151] break and we'll then carry forward with
[2153] other things like encoding and advanced
[2155] methods
[2156] okay so let's start with stimulus
[2159] representations and in this hour I am
[2162] going to talk about uh you know text
[2164] based stimulus representations visual
[2166] stimulus representations audio stimulus
[2169] representations and multimodal stimulus
[2171] representations now hki is in general a
[2175] very very broad audience right so if you
[2177] are if you belong to the Neuroscience
[2179] Community uh you're specifically to the
[2181] Neuroscience Community uh you would
[2184] basically really like the Deep details
[2186] of these stimulus representations but if
[2189] you are in the traditional deep Learning
[2192] Community right so essentially deep
[2194] learning and the Machine learning
[2195] community and you know and you have
[2198] basically already experimented with a
[2200] whole bunch of these representations
[2202] then you might be like okay this is a
[2204] good revision of things okay so either
[2206] way uh what I have tried to do is to
[2209] sort of make it comfortable for people
[2212] both from the deep Learning Community or
[2214] machine learning community and also so
[2216] from the Neuroscience Community to be
[2220] able to relate with both sides of the
[2222] world and therefore look at it from from
[2224] the two perspectives from the two
[2226] perspectives nicely
[2228] okay so let's get started so uh stimulus
[2231] representations
[2232] um
[2233] stimuli specifically so this is a key
[2236] slide where I'm going to talk about a
[2238] summary of these representations and of
[2241] course in the next few slides I'm going
[2243] to double click on each of them okay uh
[2245] so sticks text stimuli representation so
[2248] remember a lot of work in neuroscience
[2250] and cognitive Neuroscience has been
[2252] pretty old so some of the earlier Works
[2255] especially in the visual stimulus uh
[2258] date back to 2008 so more than like you
[2260] know around 15 years old now so some of
[2264] these earlier works are basically using
[2266] the text stimuli depended on basic NLP
[2269] representations so this included Corpus
[2272] coccurrence counts so you would just use
[2274] you know coherence counts of certain
[2276] words with some other words and so on
[2278] topic models uh linguistic features like
[2282] part of speech tags dependency features
[2284] coming from Stanford dependencies roles
[2287] based features so role role-based
[2289] semantic role labeling those kinds of
[2291] features right
[2293] discourse features so some of these text
[2296] data sets essentially are are our
[2300] stories for example in some of these
[2302] Tech stimuli data sets there's a Harry
[2304] Potter data set right right where you
[2307] have a Harry Potter story being being
[2310] represented using using sentences coming
[2313] up on the screen one by one so now can
[2316] we come up with interesting discourse
[2317] features out of that mentioned I will
[2319] talk in detail about how these discourse
[2322] features look like right uh semantic
[2325] data sets semantic features so in the
[2327] sense word embedding methods and this is
[2329] basically some things which started
[2332] um almost like 2015 2016 time period
[2334] right word embedding methods uh and then
[2338] you know more richer methods like
[2339] sentence presentation models the
[2341] recurrent neural networks uh Transformer
[2344] based methods and more recently yes
[2346] transform based generative methods as
[2348] well right
[2350] um then this was uh you know um of
[2353] course experiential attributes have been
[2355] used even before these deep learning
[2357] methods basically semantic text based
[2359] method started coming up so exponential
[2361] attributes essentially are manually
[2364] curated features uh which basically
[2367] involve human ratings which are provided
[2369] by by participants later after the
[2373] experiments after the print recording
[2375] experiments are done so these ones are
[2377] also called as behavioral attributes and
[2380] you know so the idea is that typically
[2382] when you show some stimuli to
[2384] participants yes I mean you know they
[2386] are in the scanner and you record their
[2388] brain recordings however after that
[2391] thing is done you basically also make
[2393] them sit through a bunch of questions
[2395] about what they visualized right and
[2398] those questions are the ones that are
[2399] recorded as exponential attributes and
[2401] can be used as really good
[2403] representations of stimulus because they
[2405] are the things uh that that the
[2407] participants themselves labeled about
[2408] the stimulus okay so that's that and
[2411] they can be either binary or they can
[2414] actually be also ratings on a leichard
[2416] scale as we'll talk about them in detail
[2418] later
[2420] okay
[2421] there are also other forms of stimuli
[2422] like visual stimuli and earlier methods
[2426] for visual stimuli representations of
[2428] course depend on filter Banks so visual
[2430] field filter Banks uh Gap or wavelet
[2433] pyramids so you know those were the
[2435] earlier representations in the computer
[2436] vision field as well these are 2008-2010
[2440] those kinds of time periods right
[2442] this was followed by something called as
[2445] hierarchical Max model hmax model which
[2447] I'll briefly talk about right later and
[2451] then of course you know more recent
[2453] works all use convolution neural
[2455] networks so almost starting from 2012
[2457] onwards so the for the past decade or so
[2459] all the visual stimuli has been
[2461] processed using convolution neural
[2463] networks
[2465] now the next one is audio stimuli so
[2468] audio stimuli of course the older method
[2471] is used standard features like phoneme
[2473] rate presence of phonemes male frequency
[2476] Capstone coefficients right well
[2478] spectrogram features so a whole bunch of
[2480] features which one can sort of in
[2482] today's world extract from awesome
[2484] libraries like Pi audio or librosa right
[2487] but then of course more recent methods
[2489] also depend on deep learning kind of
[2491] mechanisms like soundnet audio net and
[2493] so on
[2495] then there are multimodal stimuli as
[2497] well so in the sense that you basically
[2500] are shown an image but then hey you're
[2503] also shown text related to the image so
[2505] in that senses uh you have to come up
[2507] with some multimodal representations uh
[2510] and uh thanks to advancements in deep
[2512] learning you have a very awesome
[2514] multimodal models like visual bird
[2516] Wilbert LX smart you know clip model
[2520] very recently and so many other models
[2523] which have been coming up in the very
[2525] decent uh you know in in the very recent
[2527] times which have been explored so as to
[2529] come up with really awesome multi-modal
[2531] stimulated presentations
[2533] okay
[2534] so that's that now you know that was the
[2536] key slide I'll of course double click
[2538] into each of them and look at them in
[2540] detail also in the context of several
[2542] data sets that have been proposed okay
[2544] but this could be a very good time to
[2546] also take up any questions so
[2548] um I mean there is a mic in the room so
[2552] if you basically have any questions
[2553] please feel free to ask at this point
[2556] and then we can continue uh you know
[2559] with the remaining part right after that
[2567] oh
[2569] I don't see any hands at the moment
[2572] okay
[2573] thank you pritam thank you so if there
[2575] if there's no uh if there are no
[2577] questions we'll keep going
[2578] um and I'll talk about tech stimulus
[2580] representations
[2581] um
[2582] yeah so so as we discussed uh text
[2584] stimulus representations four different
[2586] types basic NLP representations uh the
[2589] older ones have been basic NLP
[2591] representations
[2592] um you know and exponential attributes
[2595] which are pretty common in that senses
[2598] um for specific kind of data sets which
[2600] are uh which are story based uh play
[2603] based uh you know those kinds of things
[2605] narratives right those kinds of things
[2607] they have discourse information as well
[2609] so therefore there are discourse based
[2611] features uh and then you know for for
[2613] more recent things more recent times
[2615] there have been deep learning based
[2617] representations right now double
[2619] clicking them a little more uh basic NLP
[2623] representations as I already mentioned
[2625] include Corpus cochrance counts and
[2627] topic models like LDA right but then
[2630] there are also linguistic features like
[2631] part of speech feature semantic row
[2633] labels or dependencies stand for
[2635] dependencies
[2636] now on the other hand there are also
[2638] disco space features specifically in
[2640] Harry Potter kind of data sets right so
[2643] these data sets these these features
[2644] basically include characters so the idea
[2647] is that if the participant in the uh in
[2652] the fmri uh you know scanner was reading
[2656] a sentence and there were mentions of
[2658] certain characters for example Harry
[2660] Harry Potter right so if you're a Harry
[2661] Potter fan you know who Harry is or this
[2664] month there was mention of other
[2665] characters like Voldemort that would
[2667] basically uh the the the hope is that
[2671] that basically leads to activation of
[2673] different parts of the brains uh or
[2675] intensities of different parts of brains
[2677] intensities of those activations are
[2679] different and that is why people
[2680] actually use leverage characters also as
[2683] features and discourse based features
[2685] right
[2686] so there are other discourse based
[2688] features which are important for example
[2689] motion so you know again these
[2692] particular disco space features have
[2693] been chosen from a perspective of
[2696] finding those kinds of things in the
[2698] discourse and those kinds of uh you know
[2700] signals in the in the discourse which
[2702] can uh lead to heavy brain activations
[2706] right so significant brain activations
[2707] remember although there has been
[2710] significant progress in the way brain
[2711] activations are measured when
[2713] activations are still very noisy and
[2715] therefore
[2716] um you know unless there is a
[2718] significant uh change in the activations
[2721] measuring it is complex and therefore
[2723] the features need to be you know strong
[2726] enough so as to be able to be predictive
[2728] of those activations which are measured
[2731] in a noisy map
[2733] so motion uh now motion verbs so this
[2736] includes verbs like you know eating or
[2739] sleeping or you know even uh you know
[2741] raising a band or things of that kind so
[2744] anything that denotes motion typically
[2747] leads to more thinking that is the that
[2749] is the basic hypothesis and therefore
[2752] people in also included motion related
[2753] words
[2754] now the Third Kind of things are speech
[2756] related words so these are basically
[2758] Words which are uh you know uh somebody
[2760] said something somebody yelled at
[2762] someone somebody uh you know uh was was
[2766] singing something and so on so anything
[2767] to do with speech right those kinds of
[2769] verbs uh emotions not motion verbs and
[2772] so on so several discourse based
[2774] features and I'll again double click
[2775] into them more later
[2778] deep learning based representations as
[2780] we discussed earlier as well these are
[2781] representations involving embeddings uh
[2784] slightly longer context in terms of RNs
[2786] lstms and transform based models
[2788] exponential attributes include ratings
[2790] on a scale of like art scale of zero to
[2792] six and also a binary exponential
[2794] attributes okay so let's look at them in
[2797] more detail now
[2798] so uh basic NLP representations for word
[2802] stimuli now in these representations the
[2806] idea is to actually come up with uh with
[2810] uh with the features which can actually
[2812] represent the text that was presented to
[2815] the to the participants now again in
[2818] various experiments text can be
[2819] represented in different forms so none
[2822] of the experiments actually have
[2824] presented let's say the whole paragraph
[2825] to the reader so of course you can
[2828] present full slides to the reader but
[2830] that's not typically what is done so the
[2833] way the equipment is typically you can
[2834] present uh one word at a time or you
[2838] could basically present maximum a
[2839] sentence at a time right
[2841] so those have been the typical modes of
[2843] presentation uh even when words have
[2846] been presented some of them some of the
[2849] presentations or even if centers have
[2851] been presented some of them basically
[2852] mandate the sentences presented for five
[2854] seconds and the participant looks at the
[2857] end sentence for the entire five seconds
[2858] While others basically uh by present the
[2862] sentence based on the reading speed of
[2863] the of the participant so you know the
[2867] participant reads the entire sentence
[2869] and then clicks a button saying I'm done
[2870] with reading the sentence okay so that's
[2873] the setting and under the setting let's
[2874] basically understand now these NLP
[2877] representations okay
[2880] so basically you know these kinds of
[2882] features essentially just try to note
[2884] down how many times any of these 25
[2887] verbs occurred so there are these 25
[2889] verbs that you can see and as you can
[2891] see this this basically data set was
[2892] created way old uh way back in time and
[2895] at that point people just realized that
[2897] hey maybe I could essentially just look
[2899] at important verbs and try to correlate
[2902] them with the activity in the brain
[2903] right so essentially therefore these are
[2905] features related to important verbs uh
[2908] that could activate a whole bunch of
[2910] brain areas okay so uh so that's that
[2913] and yes I mean at that time they did you
[2916] know ensure that they take sensory motor
[2918] activities
[2919] um your actions and so on actions
[2921] related to objects actions related to
[2923] people and special relationships and so
[2925] on okay so for each verb comma stimulus
[2928] w pair what they did was to compute the
[2931] feature based on some Corpus so for
[2933] example if this is Harry Potter kind of
[2935] stories you'd basically take the verb
[2938] and the stimulus word that was there
[2940] that was presented along with so if you
[2942] have a sentence you have several
[2944] stimulus Words which are presented and
[2945] you take the word so C right so C is a
[2948] verb you'd basically take the stimulus
[2950] word and then use its Corpus frequency
[2952] count so
[2954] um for example it could be C magic and
[2957] then therefore what you would do is to
[2958] basically go ahead and then look at the
[2960] word magic and the word c in the entire
[2963] Harry Potter story and based on the
[2965] number of times it occurs you are going
[2967] to use that as a as a as a feature right
[2969] so that's that
[2972] um so in fact other people extended this
[2974] data set to 985 common English words uh
[2977] and uh you know they basically try to
[2979] include more and more words uh which can
[2982] essentially relate to a sensory or motor
[2984] activities
[2985] okay people also build topic models so
[2989] the ideas I mean the idea is that yes
[2992] these are the words which are typically
[2993] presented to readers so house lever and
[2996] so on uh so in fact the initial
[3000] experiments focused on nouns more so so
[3002] readers uh especially when just words
[3005] were short rather than sentences uh
[3007] participants were shown nouns so house
[3009] was shown uh and then clearly uh if you
[3012] are just using 25 verbs in this data set
[3014] you would basically have like 25
[3015] features for the word house denoting how
[3018] many times the word house appears with
[3019] the word c with the word here with the
[3021] word listen uh in the data set from
[3024] which those those particular words were
[3026] chosen right on the other hand uh later
[3028] down the line people said maybe you can
[3030] come up with better representations
[3031] using topic models okay so for example
[3034] if the word airplane was shown maybe
[3036] what you could do is to basically get uh
[3039] you know uh essentially web pages that
[3042] relate with airplane from Wikipedia
[3044] let's take all web pages which relate
[3045] with the Wikipedia
[3047] airplane so for example it could be
[3049] fixed Wing aircraft aircraft aircraft
[3051] cabin airplane and so on and once you
[3054] have all of those web pages for all of
[3056] the words that you want to show let's
[3057] say you want you're basically showing
[3059] you know 100 words or maybe you know 500
[3062] Words as part of this experiment as part
[3064] of this data set you actually get all
[3066] different Wikipedia articles and then
[3068] you do topic modeling on top of them uh
[3070] topic modeling as you as some of you
[3072] mostly know you know there are several
[3074] different topic models starting from LDA
[3076] LSA digital processing individually kind
[3078] of model there's so many models which
[3080] have come up now but uh at that point
[3083] people basically used LDA and LSA latent
[3085] semantic modeling and latent digital
[3087] location right so those kinds of models
[3090] and then they try to group those words
[3092] and come up with a good topic
[3093] representation for every word now
[3096] remember before deep learning embeddings
[3098] came in those topic representations have
[3100] been treated as nice semantic
[3102] representations for Words even in
[3104] typical natural language processing
[3106] right so therefore people try to use
[3109] these topic models as features for word
[3111] stimuli
[3114] um further people looked at
[3117] NLP features that you could extract
[3119] about words and sentences so for example
[3122] word length so maybe you know so and the
[3125] idea here was to basically identify if
[3127] word length is at all related to the
[3130] activations in the brain that happen
[3131] right
[3132] um when when somebody sees a word so
[3134] word length could also be used as a
[3136] features just to be able to track those
[3138] activations more accurately or predict
[3140] those activations more accurately right
[3142] so is the word related to one of the 28
[3145] unique parts of speech tags and 17
[3147] unique dependency relationships so part
[3150] of speech tags are obvious you know
[3152] there are nouns and there are detailed
[3155] noun types like common noun proper noun
[3157] and so on there are verbs adjectives and
[3159] so on so and there's a standard list of
[3162] part of speech tags uh one can basically
[3164] just obtain the hosted by pentry Bank
[3167] often called as Pantry Bank part of
[3169] speech tax right the there's also
[3171] standard list of dependency
[3172] relationships so if you give a sentence
[3174] then it can basically contain uh you
[3176] know you can look at pairs of words and
[3177] and try to extract semantic relationship
[3181] between those pairs of words for example
[3183] noun subject relationship which
[3185] basically is a relationship between the
[3187] main verb of the sentence and the noun
[3189] and you can basically try to extract if
[3191] you know if if the particular word was
[3194] involved in one such relationship the
[3196] word that was shown okay uh position of
[3200] the word in the sentence so essentially
[3201] you could use uh you know the position
[3204] as a feature itself now again role-based
[3208] features could also be defined and then
[3209] from a role-based feature perspective
[3211] you could have several such features so
[3213] is the particular word that was shown
[3215] um at the particular time point right uh
[3218] is it a main verb of the sentence or is
[3220] it the agent right so basically the sub
[3223] subject of the sentence in some ways or
[3224] it is a patient or the recipient more
[3226] like an object of the sentence or is it
[3228] like the predicate or modifier or
[3230] complement so now note that you know
[3233] many of them have an overlap with the
[3235] dependency relationships and therefore
[3237] maybe not the same paper will use both
[3238] the roles and the dependency
[3240] relationships but then some cases you
[3242] know the roles are slightly different
[3243] from the dependency relationships and
[3245] therefore they could also be used in
[3247] complementary ways okay
[3249] so that's that
[3251] um now looking at discourse based
[3253] features uh I sort of alluded to them
[3255] already right but then there are other
[3257] discourse based features like character
[3259] names so and why Computing discussed
[3262] these features of course if you showed
[3263] sentences now sentences could also uh
[3266] include uh pronouns for the actual nouns
[3269] so he raised his rank now he basically
[3272] if it refers to Harry then you know they
[3274] also made efforts to ensure that the
[3276] co-reference resolved them so uh so that
[3279] and then counted the you know whether a
[3282] particular character was present or not
[3283] right motion related words as I
[3286] mentioned already it's like other kinds
[3287] of motion every kind of motion so fly
[3289] manipulate in fact this is a very large
[3291] list of motion related words that
[3293] delivers as features speech related
[3295] words so representing the dialogue you
[3297] know uh anything that represents direct
[3299] speech between characters
[3301] emotional related words so uh it said it
[3304] identifies a set of emotions that were
[3306] felt by the characters and clearly
[3308] emotions must be related to the way
[3309] people think especially if they are
[3311] tightly engrossed in the task right so
[3314] many of these data sets have been
[3316] collected by just passive viewing now
[3318] passive viewing uh you know typically
[3321] does not raise enough brain activations
[3323] in fact if people are just asked to lie
[3326] down in a chamber right and just you
[3328] know look at things uh highly likely
[3330] that they are in their own words you
[3332] know thinking about other random things
[3334] so therefore uh to make it much more uh
[3337] much more accurate and less noisy over
[3340] time people started
[3342] recording data sets with specific tasks
[3345] for example if you uh you know and this
[3347] happens even uh when I teach right so
[3350] students if you're basically telling
[3351] students that hey at the end of the
[3353] session there will be a quiz and based
[3355] on the quiz you'll be graded you know
[3357] people are much more attentive and they
[3358] basically just think about what you are
[3360] showing them right so the therefore you
[3362] know in many of these tasks in many of
[3365] these experiments the way the data sets
[3366] were collected is that at the end of the
[3368] data set you will actually or rather you
[3371] know several times while the data set is
[3374] being collected you involve the reader
[3376] into a particular task for example you
[3379] could ask that hey what you see is it a
[3381] noun or a verb right so that basically
[3383] the person is actually thinking about it
[3385] and the way the person communicates is
[3387] by choosing Things based on a button
[3389] press right so essentially they can
[3391] choose to press maybe you can do ABCD
[3393] kind of questions as well uh where you
[3395] know you can actually ask them to press
[3396] a particular button for something that
[3399] you want them to indicate as part of the
[3401] experiment that is going on right so
[3403] anyway so in this particular discourse
[3406] kind of features well you can actually
[3408] measure emotion you can also come up
[3410] with the emotions so does the word is
[3412] the word that was shown uh does it
[3414] indicate any emotion or not right or in
[3417] general other verbs so which don't
[3419] relate to any of the things here so you
[3422] identify a set of actions that just
[3423] occur frequently but were distinct from
[3425] motion right so for example here no C
[3428] Etc
[3430] now
[3434] using a deep learning representations
[3436] and these deep learning representations
[3440] started off with embeddings so just like
[3443] in natural language processing as well
[3444] 2013 word to it came in 2014
[3448] um uh glove came in and then in 2016
[3450] fast text came in
[3452] um so there and then of course 2018
[3454] elbow came in and after that of course
[3456] there have been like uh you know uh
[3459] sentence representation models and so on
[3461] so same kind of thing happened in the
[3463] Neuroscience Community as well so people
[3465] started off by saying that hey uh yes
[3468] I'm showing these stimuli
[3469] representations and I do not want to
[3471] just capture typical NLP based features
[3474] uh you know because the new embedding
[3477] based features that have come up are now
[3479] much more accurate so therefore let's
[3481] basically use uh embedding based
[3483] features right so here what you see are
[3485] some embedding based features and then
[3487] later as a Maria and Professor Bobby
[3489] will talk about these features were sort
[3491] of then mapped basically using encoding
[3494] and encoding and decoding models to
[3496] brainstem to brain brain activations
[3498] okay but then the kind of features that
[3501] were used yes depending on the time
[3502] period when the data set was collected
[3504] and experiments were done
[3506] sort of caught up with the advancements
[3509] in uh in in the text-based Deep Learning
[3511] Community
[3512] um and uh you know people used 300
[3515] dimensional glove features or in an sc
[3518] so non-negatives sparse embeddings
[3520] thousand Dimension base
[3522] um or even using skip gram models so a
[3524] script program word to make models uh in
[3526] fact people specifically trained uh you
[3529] know Italian models as well because some
[3531] of these data
[3533] also mentioned uh were non-english also
[3536] so not everything is just English
[3537] although most of these data sets are in
[3539] English some of them
[3540] um are in Japanese some of them in
[3542] Italian uh so they also came up with uh
[3545] word to wake embeddings specifically
[3546] scriptgram embeddings in this particular
[3548] case uh for uh for such data sets right
[3552] fast text embeddings
[3554] and then you know people also try to
[3557] compare across embeddings which
[3559] particular stimulus representation works
[3560] well
[3561] and uh of course most of the experiments
[3564] most of these data sets actually contain
[3565] nouns but some of these data sets also
[3567] can you know and many of them also
[3569] contain verbs some of them also contain
[3571] adjectives okay so what was observed is
[3574] that typically uh most of these uh word
[3577] to wake word embedded kind of
[3578] representations work really well for
[3580] nouns but not that well for for verbs
[3583] and therefore people actually used still
[3586] used concepted for verbs but then they
[3588] ended up using a whole bunch of these
[3590] word and based embedding methods for
[3591] nouns right and then over time we will
[3593] see a whole you know almost everyone
[3596] moving uh to latest deep learning based
[3598] methods okay
[3601] um so over time yes in 2000 uh you know
[3604] 15 16 time period lstms and RNs became
[3607] very popular especially in the machine
[3609] translation field uh and then over time
[3611] uh Neuroscience Community also started
[3614] leveraging lstm-based features this was
[3617] also the time when people stopped just
[3619] looking just showing word stimuli to
[3621] people to participants but actually
[3623] started showing full sentences uh so if
[3627] you show full sentences then it was sort
[3628] of obvious that you would use uh some
[3630] sort of a sentence presentation but even
[3633] if you were showing word stimuli right
[3634] so and showing sentences as word
[3637] stimulac so many times sentence was
[3639] shown just as word stimuli so you'll
[3641] show a word and then you know maybe
[3643] pause for let's say 500 milliseconds
[3645] show the next word and then show the
[3647] next word and so on right so that is how
[3650] sentences were shown to people now uh
[3652] whether you show them one word at a time
[3654] or you show them in one go using lstms
[3657] or RNs became obvious uh and then people
[3660] actually uh also uh tried out other
[3663] kinds of setting I mean of course you
[3665] could basically just give the entire
[3666] sentence to an lstm and then come up
[3668] with a representation uh using some sort
[3671] of an lstm model it could be an Elmo
[3673] model so this is specifically an Elmo
[3675] model with two layers of Wireless teams
[3677] right
[3679] um but you could also do uh some sort of
[3682] multitask lstms so this is of course
[3684] multitask elastium predict next word and
[3687] predict the part of speech of the next
[3689] word so in a typical elbow model of
[3691] course you predict the next word and
[3692] predict the previous word by using two
[3695] uh unidirectional lstms one in the
[3697] forward Direction one in the backward
[3698] Direction but there are other ways of
[3700] doing multitasking with ls teams as well
[3702] and in this particular paper you know
[3704] what they did was to try to predict the
[3706] next word and try to also predict the
[3707] part of speech tag of the next word and
[3709] what I was talking about is this elbow
[3711] model where people were trying to also
[3713] to uh you know use lstms but from a
[3716] forward Direction and backward Direction
[3718] both of them
[3719] uh so while these multi-tasker streams
[3722] on the left side were not pre-trained so
[3724] uh remember pre-training was not so
[3726] popular at that time so people were
[3728] trying to build up pre-turning so the
[3729] left side part is not pre-trained people
[3731] who are training get uh you know as as
[3733] we go uh on the right side What You
[3735] observe is that this one was of course
[3738] Elmo is a pre-trained model and then you
[3740] would use Elmo with the current data
[3742] sets as to essentially uh predict uh the
[3745] context sensitive representation for
[3747] every word in the sentence okay
[3750] so that's that now um and then people
[3752] observe that yes depending on the
[3755] context length that you have uh usually
[3757] using a context length of up to 10 words
[3760] was beneficial and then usually using
[3762] let's say in a two layer Elmore you know
[3765] using the higher layer gave better
[3766] results from a brain decoding
[3768] perspective okay
[3771] um of course over time they they came in
[3774] several sentence embedding methods so
[3776] people started using uh not just
[3779] irelands and lstms from a non-preterent
[3781] perspective but people started using
[3783] pre-trained representations for sentence
[3785] embeddings so earlier methods basically
[3788] pre-trained sentence embedding methods
[3790] were simple pooling methods like if you
[3792] wanted to come up with a representation
[3793] for a sentence you just take all the
[3795] words in the sentence and you would
[3797] basically you know just do Max pooling
[3800] so you would take vertific embeddings
[3802] and then just uh you know take the max
[3804] for every element okay
[3806] um or you could do average mean pooling
[3808] or you could just concatenate all the
[3809] representations and then just do some
[3811] sort of pulling on top of them okay uh
[3814] now Advanced pulling methods came in uh
[3817] for sentence embeddings for example
[3818] facet Sif
[3821] um skip thought quick thought uh infor
[3823] sent Jensen uh you know in Universal
[3826] sentence encoder many of them over time
[3829] and this was this was permanently 2016
[3831] to 2018 because in 2018 birth came in
[3834] and then everything basically uh you
[3836] know people started believing more in
[3838] birth right uh rather Birds started
[3840] showing really awesome results okay this
[3842] was also the time you know essentially
[3844] 2016 2018 a time period and of course
[3847] papers published in 2019 based on those
[3849] research right this was also a time when
[3852] when participants were shown full
[3854] sentences in one go no word by word
[3856] stable people are shown full sentences
[3858] in one book this is specifically anyways
[3861] from the Pereira data set right so where
[3863] people were shown full sentences and
[3865] then you wanted to come up with a
[3867] representation for the full sentence
[3868] rather than just coming up with World
[3870] stimulus representations okay so so here
[3873] are you know sentences some kind of
[3875] sentence they were shown so piano is a
[3876] popular musical instrument pressing a
[3878] piano key uh causes uh you know and so
[3881] on so you can read the sentences right
[3882] so these sentences were chosen in a very
[3885] specific manner related to certain
[3886] interesting nouns or you know related to
[3890] certain categories like musical
[3891] instruments so
[3893] um but but regardless I mean you know uh
[3896] the idea is that the stimulus
[3897] representations started focusing on
[3899] sentence impedance right
[3901] uh and then you know of course in later
[3903] sessions you will see how various kinds
[3905] of encoding or decoding models were used
[3908] along with these sentence
[3909] representations and yeah I mean people
[3912] observed that of course you can do
[3914] simple pulling methods uh they will not
[3916] basically in general give you really
[3918] good accuracies what gives you very good
[3920] accuracies are more complex uh
[3922] structured embedding methods sentence
[3925] embedding methods for example infersent
[3927] which gave very good results right so um
[3931] as I basically sort of tried to organize
[3933] the sentence embedding methods were
[3935] completely unstructured models you know
[3937] which basically just involved
[3939] um some sort of simple pooling or
[3941] Advanced pooling methods but they're
[3943] still built upon word embeddings
[3944] themselves while structured models
[3947] essentially looked at sentences as a
[3951] whole trying to model them using
[3952] arguments and LS teams but pre-training
[3954] them as well based on some loss
[3956] functions for example next word loss
[3958] function
[3959] were prominently used in in building
[3962] these models some of them were just
[3963] built in an unsupervised manner but well
[3966] some of them actually had some
[3967] supervised data also right and then
[3969] clearly these structured models
[3970] specifically the supervised ones give a
[3972] really good results give really good
[3974] results
[3975] okay
[3976] um here is another comparison of the
[3979] results that you can obtain if you
[3981] basically just used Elmo if you used
[3982] Bird versus you use Transformer Excel
[3985] right so uh as time passed by of course
[3988] more interesting models like word have
[3991] started becoming popular okay so what
[3994] you observe is that I mean if if you
[3997] look at the right side picture in fact
[3999] if you look at this picture here is a
[4000] comparison across several models as you
[4002] see right so these are standard pooling
[4004] methods uh average pooling Max pooling
[4007] so these methods are effectively
[4009] um not very interesting because they
[4011] just work at the World level and then
[4013] they try to combine information at the
[4015] word level in an ad hoc manners just to
[4017] get sentency presentations right and
[4019] then towards the end what you see are
[4020] Transformer based methods robot gpd2 and
[4023] birth right in between you basically see
[4025] sentence embedding methods okay so
[4028] earlier experiments with these data sets
[4030] basically uh you know and then by the
[4032] way you see several bars there right so
[4034] those bars basically represent the
[4036] difficulty of the task let's put it this
[4038] way of course you know a professor Papi
[4040] and Maria will go into details of what
[4042] those tasks are and so on later but the
[4044] idea is that the green bar basically
[4045] shows you some task which was easy to do
[4048] right uh the the blue part is a little
[4050] more complex task and the orange piles
[4052] are more complex task y-axis basically
[4054] shows you the accuracy of predictions
[4056] and so on uh in terms of Pearson
[4058] correlation coefficient with the actual
[4060] plane activations okay
[4062] so what you observe from here you know
[4065] at least the initial experiments people
[4066] actually observed that information
[4068] embeddings were better than Roberta or
[4070] gpd2 or bird impedance okay so this is
[4073] very fancy you know again I mean 2019
[4076] 2020 is a time period Well when when
[4079] Transformers had just come in right
[4081] um and uh it was observed that inferson
[4084] was giving very good results especially
[4086] you know in in one of these papers
[4087] however over time of course uh people
[4090] have observed that well this data set
[4092] was small there are many other data sets
[4094] which can actually show you much better
[4095] results specifically uh a much better
[4098] results with Transformers specifically
[4099] if you tune these Transformer based
[4101] methods appropriately okay
[4103] what is also observed you know in the
[4105] Neuroscience Community widely across
[4107] several papers is that for Transformer
[4109] based methods uh for example you see in
[4112] in this bird picture here so um on the
[4114] y-axis you see context length uh on the
[4117] on the on the x-axis you see context
[4118] length on the y-axis you basically see
[4120] the mean voxel prediction accuracy so
[4122] what you observe is that typically uh
[4125] you know a context of 10 to 15 words
[4127] gives you really good results okay
[4129] really good results now the other thing
[4131] that is not shown in this particular
[4133] chart is that people observed people
[4136] have typically observed that the last
[4138] layer of bird does not give you the best
[4140] results in terms of predictions right so
[4142] what gives you really good results is
[4144] the middle layers so now and there is
[4147] more research being done in terms of
[4148] trying to correlate the way these
[4150] transform based models encode various
[4152] linguistic properties versus the way the
[4155] human uh you know system human
[4157] linguistic system actually encodes these
[4159] properties right but then you know of
[4162] course there will be
[4163] in the later part of the tutorial
[4166] okay so uh now people have experimented
[4171] after that with several other data sets
[4173] specifically birth so word became super
[4176] popular and
[4178] and people try to see if there can be
[4180] other kinds of loss functions uh so of
[4183] course you know birth and variance of
[4184] bird experimented with various loss
[4186] functions right so these loss functions
[4188] are different pre-turning strategies
[4189] also right uh like like there is MLM so
[4192] Mass language modeling and next sentence
[4194] prediction that of course the bird model
[4196] incorporates but then there have been so
[4199] many other uh other modeling techniques
[4202] uh like uh you know uh like like RTD so
[4205] essentially and several others right
[4207] which have come up uh what some folks
[4210] try to do is to basically build
[4212] something called a scrambled so the idea
[4214] in fact there are three different
[4216] variants that you see here so the idea
[4218] is scrambled LM is to basically it's a
[4220] language modeling technique of course so
[4221] unlike birth which does MLM uh or unlike
[4225] gbt which does the next word prediction
[4227] loss right what they did was scrambled
[4229] so the idea is that you randomly Shuffle
[4231] the words from the Corpus samples to
[4233] remove the first order cues to syntactic
[4235] structure so you completely destroy the
[4237] syntactic structure and you give it as
[4238] input right so in LM scramble and you
[4241] create this model called a scrambled or
[4243] LM scrambled the words are shuffled
[4245] within sentences so you still retain the
[4247] sentence structure and you scramble the
[4249] words within sentences and you give it
[4250] as input and of course the idea is to
[4253] predict the uh the the well-formatted
[4255] sentence without scrambling right in the
[4257] in the correct order now notice that in
[4259] fact if I think of it right scrambled LM
[4261] is a good technique it's an efficient
[4263] technique because compared to mass
[4265] language modeling which tries to compute
[4267] the loss just based on certain tokens
[4269] which are mass scrambled LM actually
[4270] computes loss for every token so from a
[4272] efficiency perspective it's pretty
[4273] efficient in that census okay they also
[4276] came up with another variant of
[4278] scrambled LML you know LM scrambled para
[4280] where the words are shuffled within
[4282] their containing paragraphs in the
[4284] Corpus so you don't really bother about
[4286] keeping the sentence order also the same
[4288] essentially just Shuffle the words
[4289] totally I mean you know across sentences
[4292] also in fact in this particular data set
[4295] uh stimuli was also shown as a short
[4297] paragraph like I mean this paragraph is
[4299] not a very long I mean like maybe like
[4300] four sentences on average four sentences
[4303] or so okay so that's that
[4306] um now of course while showing results
[4309] on uh on brain activations these papers
[4312] also contain some results on typical
[4314] standard NLP tasks and these tasks are
[4317] you know some of them are from the glue
[4318] Benchmark which is very popular in the
[4320] natural language processing Community uh
[4323] but they also found on brain tasks on on
[4326] Neuroscience tasks they found that is LM
[4329] pass model where you predict only the
[4331] part of speech of a must word rather
[4333] than the word itself is actually also
[4336] accurate so what they found is that you
[4338] know here is the typical LM so what you
[4341] see is uh in fact you know results being
[4344] shown on one of these data sets I think
[4347] the data set uh but two different matrix
[4350] mean squared error and average rank
[4352] metric
[4353] um and what you see is the results
[4354] coming from Models which have been
[4356] fine-tuned in different ways so LM
[4358] scrambled para is there LM scrambled is
[4360] there and then there is glove model
[4363] there is the standard language model
[4365] there is lmpos lmpos is basically a way
[4367] of predicting only the part of speech of
[4370] the master word rather than the actual
[4371] word itself and then there are other
[4372] models which are fine-tuned on these
[4374] tasks right what they observed is that
[4376] the mean average rank is basically the
[4378] smallest with LM scrambled I mean
[4380] smaller the better in this particular
[4382] case Okay so they found that scrambled
[4384] language models actually give them
[4385] better results okay so sample models are
[4388] actually work the best okay now again it
[4390] has evolved over time uh of course you
[4392] know the language models have also
[4394] evolved uh there are much better models
[4396] compared to birth today like Robert and
[4398] liberta with different loss functions
[4400] and also more robustly and now people
[4402] basically have figured out other models
[4405] which give better results but that point
[4407] people observed that rather than just
[4408] using the standard language modeling
[4410] losses if you basically use The
[4412] Scrambled parallel losses you would get
[4414] better results okay
[4416] uh more recently this is a paper that
[4419] our group has published more recently uh
[4421] we actually uh took a birth model uh but
[4425] then we basically you know fine-tuned it
[4427] across different tasks so you we took
[4430] the pert model which has been fine-tuned
[4432] on natural language inference tasks took
[4433] the part model fine-tuned on the
[4435] paraphrase detection task took the bird
[4437] model and fine-tuned it on sentiment
[4439] analysis star summarization task what's
[4441] a disadvocation task several such tasks
[4443] and then we tried to see that maybe you
[4447] know one of these tasks is more
[4448] correlated with the brain activations
[4449] compared to just using the standard
[4452] pre-trained bird to get word
[4453] representations or syntax presentations
[4455] right and what we found uh is that yes
[4458] that actually works so uh we we actually
[4461] found that some of these fine-tuned
[4463] representations give better results for
[4465] when we try to do brain decoding and
[4467] brain encoding so I mean again I mean
[4470] there'll be more discussions on which of
[4471] them work better and you know how they
[4473] compare later on but the idea is to tell
[4476] you that text based representations have
[4478] evolved all the way from using basic NLP
[4481] based features to using uh you know
[4483] world embeddings to using sentence
[4485] representations to using transform based
[4487] representations and not just pre-trains
[4489] also based Transformer based
[4491] representations but also appropriately
[4493] fine-tuned on various NLP tasks and
[4495] people have tried to find correlations
[4496] as to which NLP task basically leads to
[4499] uh the best encoding and decoding
[4501] accuracies
[4503] now people have also tried to use these
[4505] bird models with multitasking in in you
[4509] know multitasking kind of a setup now
[4511] again by multitasking I could mean
[4513] several things and in this particular
[4515] case I mean trying to use uh you know a
[4518] data set such that for the same stimulus
[4521] you have not just the fmri recordings
[4523] but you also have any G recordings okay
[4525] as Professor Papi Raju mentioned in his
[4528] first uh in his discussion right there
[4531] are several ways of doing recordings
[4532] there are if there are fmri sensors or
[4535] you know or fmri way of doing recordings
[4537] there is Meg there is eg and so on and
[4540] fortunately there is a data set where
[4541] you have both uh the ephemera recording
[4543] as well as the Meg recording and
[4545] therefore what you could do is to
[4547] basically build up what model such that
[4548] you can basically use uh the clsc
[4551] presentation so as to essentially just
[4552] record just just to try to create the
[4554] fmri while you can actually use the pool
[4557] Dem beddings for example so as to
[4559] predict the image right now uh you know
[4562] again while you're trying to come up
[4563] with these kinds of stimuli
[4565] representations they will come up with a
[4567] different different stimuli
[4568] representation for different subjects or
[4570] can you basically just use the same
[4572] stimuli representation across subjects
[4574] right so so therefore people have
[4575] basically used different kinds of
[4577] settings so in some of those cases they
[4579] basically fine tune but or not so
[4581] basically you could basically just use
[4583] the pre-trained part but maybe you could
[4586] fine tune based on a small part you know
[4588] maybe you know these fmri recordings are
[4590] there for one subject great you could
[4592] probably use small part of it and use it
[4594] for training right and then you find in
[4596] your birth model so that you can then do
[4597] testing on the remaining sentences for
[4599] this same subject right so that's one
[4601] way and again you don't you may not care
[4604] about subjects at all so you could
[4605] probably find it in a global model and
[4607] then you can basically just apply it on
[4609] the test subjects let's call it that way
[4611] right so all you could fine tune uh
[4613] based on one representative subject uh
[4615] you could find in a small part of you
[4617] know small part of the data of one
[4618] subject and so on and then of course you
[4621] can do multitask fine tuning as well so
[4622] fine tune using fmri as well as the Meg
[4625] data
[4627] here is the summary of the results
[4628] basically they found that fine tune
[4629] models predict fmri better than vanilla
[4632] part is sort of obvious some of these
[4633] results are obvious but the nice point
[4634] is that these basically all led to
[4637] advancements in the way uh you know
[4639] Neuroscience works so in the way people
[4641] do brain decoding and brain encoding
[4643] okay
[4644] so they also observe the relationships
[4646] between text and brain activity
[4647] generalized across experiment
[4649] participants so you could basically use
[4650] data from one participant fine tune on
[4653] that data and then leverage it for
[4655] predictions for other subjects now this
[4656] is super important because if you're
[4658] building devices
[4659] um you know
[4660] um for for understanding certain things
[4662] you could basically build devices based
[4664] on and build those training models based
[4667] on some subjects and then try to apply
[4669] it on other people uh you know without
[4672] having any training being done uh for
[4675] them right so in some ways this reminds
[4677] me of the way uh Speech to Text models
[4679] work so remember earlier speech to text
[4681] models if you were using speech to text
[4683] for dictation purpose let's say
[4685] Microsoft Word 10 years back a word will
[4688] tell you that hey let me train on your
[4689] speech right let me train on your voice
[4691] and then it will basically try to build
[4693] a personalized model which will be
[4694] stored locally on your machine but
[4696] today's models are so awesome right so
[4698] and and those were days by the way right
[4700] I mean this is something that we joke in
[4702] India a lot that hey man that guy is
[4704] trying to fake American accents so that
[4706] you know the American speech recognition
[4708] model can understand him but you know no
[4710] longer
[4711] longer of course and that is
[4714] that is models now can
[4716] I sort of work across subjects so you
[4718] can actually take train on some subjects
[4720] and then still it can generalize on
[4722] other participants right uh using energy
[4724] data can actually improve my prediction
[4726] so multitasking was a good thing to do
[4728] so multitask presentations typically
[4730] work better a single model can be used
[4732] to predict the fmri activity across
[4733] multiple experimental participants okay
[4735] so that's that now so you didn't really
[4738] need to train specific models for
[4740] different participants you could just
[4741] use the same model and globally apply it
[4744] so that's that now more recent work has
[4746] also gone into exploring these
[4748] Transformer models from a perspective of
[4750] what kind of syntactic and what kind of
[4753] semantic properties from text do various
[4756] layers of these Transformer models
[4758] capture okay and then can I basically uh
[4762] you know remove some of these properties
[4765] and then try to see if I can come up
[4767] with a better representation okay so the
[4769] idea is that let's say I have a bird
[4771] model I have a pre-trained bird model
[4772] and the way of course the pretend Bird
[4775] model has been trained on the Google
[4776] News data and Wikipedia data and
[4778] whatever right so it has probably
[4780] captured some properties for example
[4782] let's say it has captured
[4784] um uh let me just pick up some property
[4785] right so it has captured an ability to
[4789] be able to understand the occurrence of
[4792] nouns after verbs okay so in sentences
[4795] we are Joker afterwards some sentences
[4797] right it has captured it has nicely
[4799] learned that property but maybe that
[4801] property has to do nothing with the way
[4803] our brain works right so maybe that
[4805] property is completely uncorrelated uh
[4808] to uh to the way our brain works so then
[4811] can I remove that property and if I can
[4812] remove that property from the birth
[4814] model right then it is quite likely that
[4818] the stimulus representation that I'll
[4819] get after removing that property can
[4821] come up with better brain activation uh
[4824] you know better better brain encoding
[4825] and brain decoding okay so that is what
[4827] people did so people try to decompose
[4830] syntax and semantics and various
[4832] properties in this syntactic property
[4834] and semantic Properties by the way the
[4836] other reason why people also wanted to
[4837] do this right I mean removing some
[4839] properties uh and then coming up with
[4841] stimulus representations uh the other
[4843] reason was to also understand which
[4845] parts of the brain are activated by a
[4847] property for example if you have a
[4849] property uh like I mean the simplest
[4851] dumbest property length of the word
[4853] right let's say if you have a model
[4854] which basically or length of the
[4856] sentence for that matter when you have a
[4857] sentence based representation so which
[4859] part of the brain really corresponds to
[4861] length right length property if you want
[4863] to understand that what you could do is
[4865] to basically use a full pretend model
[4867] but model and just uh or even you can
[4870] fine tune it right and then you can use
[4871] it to figure out brain activations
[4873] across different voxels in the brain
[4875] okay now then what you could do is to
[4878] basically somehow try to remove that
[4879] length property from the word
[4881] representations and now how that removal
[4882] is done of course Maria will talk in
[4884] more details about that but there are
[4886] standard ways of removing Properties by
[4888] by you know looking at I mean actually
[4891] it sort of mentioned in briefly here as
[4894] well but the standard ways of removing
[4896] these properties from from from various
[4898] transform based models so if you remove
[4899] that property you can try to figure out
[4901] which parts of the brain were less
[4903] activated after you removed that
[4905] property and that tells you that yes
[4907] this part of the brain really has to do
[4909] with the length property because when
[4910] the length was there in the model
[4912] representation you could basically come
[4914] with a better better better uh your
[4916] prediction of the voxels there but when
[4919] the length was not there you come up
[4920] with a worse prediction of the voxels in
[4922] a particular part of the brain yeah so
[4925] so people have tried to therefore come
[4927] up with a stimulus representations which
[4929] lack syntax which lack semantics uh in a
[4933] very controlled manner in a very
[4934] controlled manner right and then this
[4936] was the time when people also realized
[4937] that yes you know
[4939] um
[4940] gpt2 models and of different layers of
[4943] gpd2 models and different layers of
[4945] these other models like XL net Roberta
[4947] Albert per digital GPD yeah all of them
[4950] capture uh you know these properties
[4952] nicely you know some of some part is
[4954] basically syntactic in nature some part
[4956] is semantic in nature and by looking at
[4958] the syntactic versus semantic part you
[4960] can actually figure out which parts of
[4962] the brain deal with the syntax in the
[4964] language versus which parts deal with
[4965] the semantics in the language okay so we
[4969] are almost close to taking a break but
[4971] then I will quickly basically also
[4973] discuss about exponential attributes now
[4975] these are essentially again you know not
[4978] deep learning oriented these are hand
[4980] curated features very similar to the
[4983] earlier features that I talked about but
[4985] these are not really some things that
[4986] are automatically computed so uh
[4988] remember in the first part of the
[4990] texting my representations I sort of
[4992] talked about Cochran's count Squad plus
[4993] coccurrence counts and so on those kinds
[4995] of statistical features which typically
[4996] people also use in the natural language
[4998] processing field but these features
[5000] exponential attributes are more like
[5002] behavioral attributes and they are
[5004] manually curated
[5005] so um uh when uh you know just after the
[5008] fmri experiment is done uh the
[5010] participant is basically asked to you
[5012] know uh sit down and look at those
[5014] things that were shown to them and rate
[5016] uh um or associate basically the the
[5020] images or text whatever they saw in this
[5022] particular case text that they saw uh
[5025] with a particular uh feature with a
[5027] particular exponential attribute okay so
[5029] for example a participant is asked
[5031] something like this on a scale of 0 to 6
[5033] to what degree do you think a banana of
[5035] a banana is having a characteristics
[5037] characteristic or defining color right
[5038] so essentially of course you know the
[5040] word banana was also shown uh you know
[5043] when when the print recordings were
[5045] being done so you take those words which
[5047] were shown when the print recordings
[5048] were being done and then you try to
[5050] associate them with any of these
[5051] experiential attributes right so can you
[5054] think about a color when you think about
[5057] the word water can you think about any
[5059] color right we can't right so or when
[5061] you think when you see the word honesty
[5063] can you think about color we can't right
[5065] so essentially the idea is that
[5067] um uh there are so many uh senses and uh
[5071] these words were chosen by the way these
[5073] exponential attributes are chosen in a
[5075] very very smart manner right so as you
[5077] see these are things that again can uh
[5080] you know uh are cognitive in nature so
[5082] essentially
[5083] um they relate to senses and they
[5086] require brain processing to be able to
[5087] understand them right so when you see
[5089] banana you of course see things your
[5091] your your
[5092] um you know uh visual cortex basically
[5095] is involved into doing those things so
[5097] therefore the idea was to basically ask
[5100] people whatever you know banana can it
[5102] be related to Vision can it be related
[5104] something that is bright or dark and not
[5106] just binary on a scale of zero to six so
[5109] that you can actually associate which
[5111] part of the brain regions might be
[5113] activated when somebody sees banana as a
[5115] stimuli okay so that's that now Anderson
[5118] at all actually started using this for
[5120] the first time uh and in fact most of
[5122] these data sets are from the same group
[5124] right so essentially
[5126] um 65 attributes to start with but then
[5128] later people used uh extended this to
[5131] other set of attributes also but then
[5133] you know uh what they found was that on
[5136] top of text models you know other kinds
[5138] of models these experiential information
[5140] uh give really significant benefits
[5143] especially when you are just using
[5144] typical stand typical uh you know
[5146] non-deep learning based
[5148] um non-deep learning based NLP features
[5150] right
[5152] so that's that uh and yeah I mean the
[5155] reason
[5158] very nice so it is
[5160] in the color of bananas because it is so
[5163] so what also happened is that uh on top
[5166] of text models
[5168] um a lot of experiential attributes go
[5170] unstated right and therefore these were
[5173] extra useful so in general when you're
[5175] talking about banana right you don't
[5177] typically talk about uh yeah its color
[5180] is yellow and so on so therefore when
[5182] you get these exponential features that
[5184] helped them that help them a lot but
[5186] then again with deep learning now with
[5187] deep learning the things the thing is
[5188] that deep learning embeddings basically
[5191] incorporate these kinds of exponential
[5194] attributes in them already so therefore
[5196] with deep learning method nobody uses
[5197] them but earlier they were super useful
[5199] right
[5200] so people extended these attributes not
[5203] just so the people collected not just
[5205] zero to six scale but we will also
[5207] collected binary attribute information
[5208] so for example behavioral data uh across
[5211] uh 42 different nearly possible semantic
[5214] features so these include features like
[5216] uh you know if the you know basically
[5219] social features mental action
[5221] communication knowledge and so on so
[5223] there are a whole bunch of these
[5225] dictionary and people collected uh human
[5228] in a manual way they collected this
[5230] Behavioral or experiential information
[5232] okay so that's the first part now uh
[5235] yeah um we are about time from a break
[5238] perspective uh and then you know after
[5241] the break I will probably spend like
[5243] about half an hour talking about visual
[5244] stimulus audio stimulus and multimodal
[5246] stimulus and then I'll hand it over to
[5248] Professor bappi Raju to talk about uh
[5251] deep learning for brain decoding
[5253] um and just to remind everyone after
[5255] that Maria will come in uh Professor
[5258] Maria from uh from MPI right she will
[5260] basically talk about brain encoding uh
[5263] and then uh you know again Maria will
[5265] continue uh after the coffee break in
[5267] the afternoon talking about Advanced
[5269] methods and then lastly uh Professor
[5272] will sort of summarize and talk about
[5274] future trends
