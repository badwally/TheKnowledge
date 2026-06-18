---
schema_version: 1
id: yt-4SaY4uQEewU
type: youtube
title: Deep Learning and the Brain 2019 – Prof. Kalanit Grill-Spector
url: https://www.youtube.com/watch?v=4SaY4uQEewU
authors:
- ELSC Video
ingested_at: '2026-05-30T20:02:09Z'
content_hash: sha256:513af20279a30ccf9f89318d2c3f555ff5024d5cdfd262968142f673824e8697
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: ELSC Video
  channel_url: https://www.youtube.com/@elscvideo
  duration_seconds: 2155
  caption_track: fetched
  snippet_count: 829
filter:
  score: 0.7
---
[22] okay so first of all I'd like to send to
[25] the organizers for inviting me and as I
[28] was preparing for this conference I was
[31] reminded of a conference that I've been
[34] here as a graduate student more than 20
[36] years ago in Jerusalem and it was a very
[39] inspiring conference because it was a
[42] stimulating time about new algorithms
[44] about learning and today I feel that
[47] it's also a very exciting time in the
[49] field and the interface between
[51] neuroscience and deep learning and what
[54] I hope today is to convey my enthusiasm
[56] to this as well as maybe seed some new
[60] ideas so my ultimate goal is to
[65] understand the brain computations that
[68] enable face a perception so the question
[72] in my mind is whether we can leverage
[74] advances both in neuroscience as well as
[76] in deep neural networks to produce a
[80] nearly accurate model of face perception
[83] so in order to do such thing we need to
[86] do a couple of things first we have to
[89] understand how the human brain works and
[92] understand implementation properties of
[94] the brain
[95] second of all we need to implement these
[98] properties into hierarchical deep neural
[101] networks or hdn ends and then what we
[104] could do is use these HTT and ends to
[107] test the computational utility of
[109] specific implementation features of the
[112] brain and the reason that this is an
[115] exciting time in the field is because of
[118] work like the waa worked by Danny Amin's
[120] and colleagues have shown that by taking
[122] a newly inspired brain network and
[126] training it to do an object recognition
[128] task and a network like this cannot only
[131] predict human performance but it
[134] generates neurons or units in the
[136] network that resembles a proposal in
[139] responses of neurons in the macaque
[142] brain and one of the reasons that and
[147] this so not only this hierarchy
[151] this neural network is inspired by the
[152] brain but it also has several useful
[155] computational features first of all it
[158] can map any function between input and
[160] output second of all it is trainable and
[163] third of all once it's trained it's very
[165] fast because of the feed-forward
[167] processing so what happens in the human
[171] brain so imagine that you're looking at
[174] the space life gets reflected from the
[178] face to your eyes and image is formed on
[180] the retina then through the optic nerve
[182] it's it reaches the LGN and from the LGN
[185] it reaches primary visual cortex or v1
[188] and then through a series of visual
[191] areas that we think of them as
[193] processing stages information area Rives
[196] - what i'm going to call as ventral
[197] temporal cortex or vtc and then you may
[200] be a percept emerges now in the domain
[204] of face recognition we might need to
[206] think about which regions might be
[208] specifically involved in face processing
[210] and in the ventral streams there are
[213] three clusters of face selective areas
[215] in the human brain and the way that we
[219] identify these regions in people's brain
[221] we put them in an fMRI scanner and shows
[223] them a multitude of images and then
[226] search for voxels in the brain that
[227] respond more strongly to faces compared
[229] to other stimuli including body parts
[232] common objects places and building as
[234] well as characters and dipp'd lee you'll
[237] find three clusters of face selectivity
[239] one cluster in the inferior occipital
[241] gyrus that I'm gonna call iog faces
[244] another cluster in the posterior part of
[247] the fusiform gyrus that I'm going to
[248] call P few spaces and the third clusters
[251] that's about a centimeter two centimeter
[253] and a half more anteriorly I'm gonna
[256] call em fuse faces and a characteristic
[259] of these areas is that they respond more
[262] strongly to faces than to any other
[264] stimulus and this response and the
[267] selectivity is maintained across formats
[269] for example if you show silhouettes of
[271] faces is there also produce higher
[274] responses and silhouettes of shapes or
[276] scrambled light so it's quite an
[278] abstract response we can also use
[282] electrical brain stimulation
[283] to test involvement of these regions and
[286] perception and occasionally we'll have
[288] patients like epilepsy patients that
[290] have electrodes implanted in their brain
[292] to test for the onset of epileptic
[294] seizures and we had such a patient that
[296] we had electrodes implanted by chance
[299] over P fuse and amp fuse and you can use
[301] the electrical stimulation to see what
[303] happens when you disrupt normal activity
[305] in the brain regions and we did a series
[308] of trials and I'm going to show you one
[310] of these trials all right ready 1 2 3
[325] yeah in metamorphosed again and you look
[329] like someone I've seen before but maybe
[333] a different person in my memory almost
[336] like your your nose kind of shifted to
[340] the left a little bit and your look just
[343] changed
[345] did ya don't tell me one well I mean I
[351] don't have a photographic memory but it
[353] just you could turn into someone else
[356] you started leave you looked like
[357] someone else did I keep my gender yeah
[359] oh yeah
[361] how did you know I'm not the female
[362] those are still wearing a suit and tie
[364] oh you could see the suit and tie a
[366] bully your face changed everything else
[368] was the same yeah
[371] did this skin color remain the same yes
[374] yeah the position of my lips and nose
[379] and eyes stay the same when they got
[382] worse they shifted let's say they
[386] shifted to a side and maybe stretched
[389] but they didn't get larger or smaller
[394] okay
[396] there was it was more of a perception
[399] how I perceived your face interesting
[402] tell me more that's about all I can say
[412] really shows cause an involvement of
[416] these regions in face perception because
[418] when you stimulate them you get a
[419] specific deficit in the perception of
[421] faces so now that we have a really good
[425] model system in the human brain to study
[427] a face perception how are we going to
[429] implement this in a neural network so
[433] the networks that Dan described before
[435] it was inspired by a macaque brain and
[438] usually it involves a hierarchy like
[440] this that goes from V 2 V 1 to V 2 to V
[443] 4 to I T however in the human brain you
[449] might notice that these three is as big
[452] as V 2 and in fact bigger than V 4 so
[455] one thing that when you want to model
[456] the human brain perhaps you need to
[458] update the hierarchy for example include
[460] v3 another thing that you might want to
[463] consider is that ventral temporal cortex
[464] is not a homogeneous piece of cortex as
[468] it includes three stages of face
[470] processing so you might also want to
[472] include these regions in your network
[476] and finally I do want to point out
[478] another difference between the humans
[480] and the macaques humans have an extra
[483] gyrus in the temporal lobe and actually
[487] the gyrus the fusiform gyrus were face
[490] selective region s is a human specific
[493] and it doesn't exist in lower monkeys so
[496] one thing that we might want to do is a
[498] model to generate them nearly
[501] accurate monoface perception is
[502] including hierarchy that includes v1 v2
[505] v3 v4 IGP fuse and M few spaces so not
[511] only that we need to update our
[512] hierarchy to generate a nearly accurate
[515] and model of face recognition but we
[517] might also want to consider how to
[519] compare stages and processing in the
[520] brain to stages in an artificial neural
[523] network so one of the common approaches
[526] that people have used in the field is
[528] using something called representational
[530] similarity analysis that you look at how
[532] representational spaces in the brain and
[534] in the deep neural networks might
[537] resemble each other so typically what
[539] you do in a human experiment you might
[541] put people in the scanner and show them
[543] different images for example an image of
[545] a hand and an image of the face and
[547] measure the distributed response to
[550] these different stimuli across ventral
[551] temporal cortex and then determine how
[553] similar these responses are and
[555] typically the metric is a correlation
[557] metric and basically each bin in this
[560] representational similarity matrix
[561] defines how similar to brain responses
[564] to different stimuli might look like and
[566] then you might want to do the same thing
[571] in a human in an artificial neural
[573] network and see if these and if these
[578] are our sm's resemble each other one of
[581] the things that came out of a large body
[584] of research actually in human
[585] neuroscience is that images of the same
[588] category tend to generate it's very
[590] similar brain responses so you can see
[591] here this dark square root means that
[594] the correlation between patterns
[595] responds to different phase images is
[597] very high however if you look at the
[600] correlation between images of faces to
[602] let's say inanimate objects they they
[604] generate very different responses so in
[608] this particular picture I took from a
[610] study by Niko Kriegers Corte and what he
[613] did in the study he generated our SMS in
[615] different stages of an artificial neural
[618] network and examined which square
[621] processing stage resembles that of
[623] ventral temporal cortex in human and
[626] what he found was that the higher stages
[629] of the network kind of like Dan's work
[630] and basically the highest stage of the
[632] network
[633] generated the most similar
[635] representational structure as the human
[637] brain and moreover actually a linear
[639] combination again kind of like did Nan's
[641] work generates the best correlation so
[645] this is kind of interesting because of
[648] two things first of all if there is a
[649] tool for us to compare hdn ends to human
[652] brains but it also suggests that if you
[654] have a network that in the highest
[656] stages has some sort of categorical
[657] responses this might be a good network
[660] for the process of object recognition so
[664] so far I've shown you a lot of
[666] similarities between the brain and hdn
[669] ends but there are also some differences
[670] that I'd like to illustrate so first of
[673] all this representation similarity
[676] analysis is really interesting but it's
[677] very abstracted from the way information
[679] is laid out in the brain and if you're a
[682] person like me who stares at people's
[684] brain on a regular basis you'll notice
[686] that the brain is actually organized in
[688] a very consistent manner across people
[691] for example if you look at maps of faces
[693] versus places or animate versus
[695] inanimate objects they generated a very
[698] consistent apology or topography Icaza
[701] ventral temporal cortex in which there
[704] is this lateral medial gradient so it's
[706] like a representational axis of animus
[709] II is actually laid on a physical access
[712] on somebody's brain and furthermore a
[715] large body of research from other labs
[718] as well illustrates that there are
[720] multiple maps not only maps of category
[722] in ventral temporal cortex but also maps
[724] of eccentricity bias and will world
[727] object sites that also have this lateral
[730] medial gradient and the gradient is so
[732] consistent across people that if you
[734] understand identify a small sulcus in
[738] the fusiform gyrus that bisect it it's
[740] called the M FS you'll find that the m
[743] FS predicts the lateral medial
[745] transition in all of these formats so
[748] this is kind of interesting because it
[750] suggests that there's not only a
[751] functional structure coupling between
[753] the brain and macro anatomy but it also
[756] generates a regular a relationship
[758] across multiple maps for example lateral
[761] to zoom FS you'll find face
[763] representation annum
[765] representation mobile representation and
[768] small objects and medial to ZFS you'll
[770] find place representation inanimate
[773] objects periphery and large a objects
[777] and this is this means that there is
[782] this regularity among multiple
[784] representation laid out on the cortical
[787] surface and another thing to note is
[789] that these representations might have
[791] different spatial skills for example the
[793] map of animus II spends several
[795] centimeters encompassing the entire
[797] ventral temporal cortex and you can see
[800] that within the animate compartment
[802] you'll see more finer scale
[804] representation at the scale of
[805] centimeters of clusters that are
[808] preferring faces or bodies and this is a
[811] second cluster of faces and a lot of
[813] work from electrophysiology suggested
[816] that they're in even finer scale maybe
[818] at the scale of a cortical column and
[819] that this car a cortical column of maybe
[822] a hundred microns you'll find clustering
[824] of neurons that might represent face
[827] parts or face a viewpoint so looking at
[831] the structure we proposed the hypothesis
[833] that there might be a relationship
[834] between the levels abstraction of
[837] representation and the spatial scale
[839] that's represented at the brain were by
[841] more abstract information such as
[843] distinction between animate and
[845] inanimate objects at the scale of
[847] several centimeters information about
[850] ecologically relevant categories such as
[852] bodies and faces might be at the scale
[854] of a centimeter and at the level of make
[858] up a cortical column you might represent
[860] very fine-grained details such as
[862] features and one so this is might be
[866] interesting but it also might be good
[868] for something computationally in that it
[870] gives you a flexible a level of
[872] information or hierarchical information
[874] structure within ventral temporal cortex
[876] and depending on task demands you might
[879] read out different kinds of information
[880] by reading out information from rental
[883] temporal cortex across different spatial
[885] scales now this is not a difference
[889] between the brain and deep neural
[892] networks because the performance of the
[894] deep neural arch work doesn't really
[896] depend on how the neurons organized
[899] within a layer but this also gives an
[902] opportunity to test some hypotheses for
[906] example I've given a hypothesis that
[908] this spatial structure might give us
[911] some flexible readout of category
[913] information and by comparing between
[915] different networks one that has a
[917] spatial structure and one that does not
[919] have a spatial structure it might give
[921] us an opportunity to test this kind of
[923] hypothesis and as was mentioned before
[929] as the basic processing in the visual
[932] system is done by receptive fields so
[937] one of the receptive field a receptive
[939] field is a region and visual space that
[942] is processed by a neuron and one
[945] features of receptive fields in the
[947] human brain is that the receptive fields
[949] that code similar location in the visual
[951] field are physically clustered and this
[953] clustering is in the order of a
[955] millimeter in the human brain
[957] which gives us an opportunity was fMRI
[960] since we cannot access single neurons we
[962] can measure the visual field represented
[965] by the population of neurons in a voxel
[968] and we call that a population receptive
[970] field or P Refs
[972] and the P reps and I'm going to describe
[974] today involve a very simple mathematical
[977] model and they include a two dimensional
[979] Gaussian a followed by a compressive
[983] non-linearity and again this is a
[987] similarity between the architecture of
[989] hdn ends in the brain because the basic
[991] operation that's performed today in
[994] these deep neural networks is the
[995] convolution operation was a filter a
[998] spatial filter that operates on the
[1000] image and the hypothesized computational
[1003] value of this kind of architecture is
[1006] that it breaks out a difficult problem
[1008] to a lot of local computations and
[1010] therefore it enables parallel processing
[1012] of the image and increasing the speed of
[1015] processing a feature of the hierarchy of
[1020] the ventral stream is that the receptive
[1024] field size and consequently the
[1025] population receptive field size
[1027] increases
[1029] as us ends if the ventral stream
[1031] processing hierarchy so for example by
[1034] the time that you're in face-selective
[1035] regions the mean PRF size is about four
[1039] times as big as a PRF size in v1 and the
[1044] same is true of the architecture of H
[1047] DNN because the pooling operation from a
[1049] lower layer to an upper layer generates
[1052] a unit in the higher stages of the
[1054] network that see bigger and bigger
[1056] portions of the image so to give you
[1061] some intuitive anchoring about how these
[1063] population receptive field size might
[1065] relate to your vision so suppose you're
[1067] looking at somebody standing in front of
[1069] you maybe he's there about a meter away
[1071] and you're looking at their face what
[1073] would be what would appear up in v1 see
[1076] if it maybe it's two degrees of the
[1079] center and you'll see that this PRF
[1080] really looks at really local information
[1082] maybe something like the corner of your
[1085] eye by the time we sent you before so a
[1090] paraffin before might be a facial
[1094] feature maybe it will see the eye the
[1096] eyebrow and the corner of your nose and
[1099] by the time you reach to face selective
[1103] regions face a PR Epson face-selective
[1105] regions might include several facial
[1108] features or maybe even the whole face so
[1111] this suggests that they're kind of
[1112] optimized to integrate across
[1114] information across facial features and
[1117] that seems to be maybe the space the
[1119] spatial basis for something like
[1121] holistic processing and face recognition
[1125] so the idea is that this increase in the
[1128] receptive field size across the
[1129] processing hierarchy might generate more
[1132] task relevant receptive fields that they
[1135] are more useful for a recognition in
[1139] higher stages as a network yeah
[1148] so the receptive field doesn't change
[1150] you saccade your fixation point changes
[1153] with your saccade so in this particular
[1154] example I showed an example where you're
[1158] gonna be fixating in the center of the
[1159] face shown here by the crosshair and
[1161] I'll show you a bit what happens under
[1162] different tasks okay so um however um
[1171] [Music]
[1173] okay so this is what happens so so far
[1177] I've shown you this hierarchy that's
[1179] happening both in the neural networks
[1181] and in the rain but there are also some
[1186] differences for example the basic
[1189] architecture of HCM that was in a layer
[1192] you have the same filter that is
[1194] kebabbed across entire image meaning
[1197] that the filter is fixed across a layer
[1201] now this is not true in the brain so
[1205] what happens in the brain in each a
[1206] processing stage P refs are actually a
[1209] differing in size depending on
[1212] eccentricity so close to your center of
[1214] gaze in your fixation the puris are
[1216] small and as you go from the center to
[1218] the periphery the P refs or receptive
[1221] field size changes and this is true in
[1224] every visual area even as the average
[1226] receptive field size increases across
[1229] the processing hierarchy now this is an
[1231] example of a difference again between
[1233] the brain and then HGN and the question
[1235] is is it good for something or maybe
[1237] this is a biological constraint so what
[1240] we think is happening in the brain that
[1241] the brain has a trade-off between
[1243] resolution and and limited like hardware
[1248] and the compromise that the brain has
[1251] done is to reduce resolution but reduce
[1254] resolutions specifically in the
[1255] periphery while keeping the resolution
[1258] high at the center of gaze so again
[1260] these differences between the brain
[1264] implementation and deep neural networks
[1266] that might not have the same kind of
[1267] physical limitation also can give rise
[1270] for us to understand what might be
[1272] constraints in biological systems
[1276] another thing that might be interesting
[1278] to
[1279] is how do these PRF style the visual
[1282] field so in this example I took all the
[1285] pure Epson v1 in the left hemisphere and
[1288] see how they cover up the visual field
[1291] and this is what we call the visual
[1293] field coverage of a region and as you
[1297] can see the left hemisphere covers
[1299] pretty uniformly the right visual field
[1301] so in each hemisphere we have a Hemi
[1304] field representation of the world and
[1305] this is typical of early and
[1307] intermediate retinotopic areas however
[1309] this is not true in face-selective
[1311] regions so now I'm showing you say again
[1315] left hemisphere data that prfs in the
[1318] face selective regions and while they we
[1322] still have the center's being in the
[1324] contralateral visual field you see that
[1326] the receptive fields are big they and
[1328] always cover as a phobia and extend to
[1330] the epsilon visual field and the
[1332] consequence is that is that if we look
[1334] at the visual field coverage it's not
[1336] uniform but in fact we have much higher
[1339] coverage of the fovea than the periphery
[1342] of the visual field and recall that the
[1344] fovea bias and work like raah work by
[1348] Raffaella has suggested that this
[1351] popular bias might be related to the way
[1354] that we look at faces so you ask what
[1357] happens when we do normal viewing of
[1360] faces so when people in our case we
[1362] measured by movements when people were
[1364] asked to recognize the face they're
[1366] shown an image that they may or may not
[1368] seen several minutes before and they
[1370] have to say do you recognize it or not
[1371] and we let people really view the face
[1374] if you measure the density of fixations
[1377] you'll find out that many of the
[1378] fixation in fact most of them are close
[1381] to the center of the face this is
[1383] illustrated in this plot and the reason
[1386] that we think that people are doing this
[1388] kind of behavior because it puts their
[1390] receptive field in these face selective
[1392] areas in the region where they're
[1394] informative faces for face recognition
[1395] and these are ours internal features of
[1399] the face so this also just suggests
[1402] another idea that maybe these prfs in
[1404] higher order areas might be
[1408] tasks relevant so to test this
[1411] hypothesis we measured prfs across the
[1413] ventral a processing hierarchy across
[1416] two different tasks so in this test we
[1419] put people in an fMRI a machine asked
[1421] them to fixate on the stream of rapidly
[1423] presented digits shown centrally and
[1426] then we showed faces in 25 random
[1429] locations and as they're looking at
[1432] these streams before each trials are
[1434] giving a cue to what to attend so
[1437] they're asked to either attend to the
[1438] centrally presented digits and report if
[1441] two consecutive digits are identical or
[1444] they're asked to attend to the face
[1446] without moving their eyes and report if
[1448] two consecutive faces are the same
[1451] person and we ensure that they keep
[1453] their eyes on fixation by measuring
[1455] their eyes movements during that from
[1457] rice scanner and then we could test if
[1459] prfs are fixed across these two tasks or
[1461] maybe the task might affect the PRF
[1465] properties so if we look at
[1470] face-selective regions i/o GPUs and M
[1472] fuse and measure their prfs in under the
[1475] two tasks we see that attention affects
[1477] p refs first of all during the face test
[1481] you can see that the perhaps are more
[1482] eccentric or more further from the
[1484] center of gaze as compared to the digit
[1487] task so this suggests that attending two
[1489] faces peripherally shifts the processing
[1492] units towards the attendant location and
[1496] notably this property is specific to
[1498] face selective regions because if we
[1500] look at P ref eccentricity in early
[1503] visual areas such as v1 v2 or v3 we
[1506] really don't see a significant
[1507] difference in their PRF location across
[1510] desk another interesting feature is not
[1513] only that the PRF location changes but
[1516] also their chat size changes so when
[1518] people are asked to attempt to face
[1522] compared to digit you can see it here
[1524] and the PRF size actually doubles so
[1527] basically there's a doubling in the PRF
[1529] size during the face task compared to
[1532] the digit task in all three face
[1533] selective regions but again in v1 or v2
[1537] re suite we don't see
[1539] and I changing the PRF size so this is
[1543] just that higher order eras seem to be
[1545] modulated the PRF seem to be modulated
[1547] by Testaments whereas earlier visual
[1550] areas are not so what are the
[1552] consequences of this change in the PRF
[1555] location across the BAS desk one can
[1558] think about understanding this by
[1560] looking at the visual field coverage
[1562] under two tasks so this is a leftie few
[1564] spaces these are all the pure ups in
[1566] this regions under the digit tasks and
[1568] these are the same pure FS under the
[1571] faith desk and you can see that you're
[1573] in the face task the receptive fields
[1575] are bigger and more scattered and
[1577] consequently extend much more to the
[1579] periphery so that means that if you have
[1581] a face in the periphery it's covered by
[1584] more PFT's during the face task compared
[1587] to the digit task and this might have
[1589] some computational a consequences for
[1592] example maybe because of the difference
[1594] in visual field coverage you can better
[1596] detect the face in the periphery
[1598] compared in the face tasks compared to
[1601] as they did a task and in order to test
[1604] this hypothesis we did what's called a
[1606] model-based decoding we took the
[1608] responses of the pure FS under the digit
[1610] task and then under the face task and
[1613] estimated how well they can dissociate
[1616] the location in the faces in different
[1618] parts of the visual field so this
[1620] example shows the spatial error in
[1622] identifying the location of faces in the
[1624] rapper right upper quadrant and you can
[1627] see that there's a lot of error during
[1629] the digit tasks but much reduced error
[1631] during the face desk and in fact we can
[1634] quantity really measures that and
[1636] there's a four-fold reduction in the
[1638] spatial error during the face task than
[1641] the digit task so this again suggests
[1644] that we have a pair up in the human
[1646] visual systems that might be modulated
[1647] by tasks and give us tasks optimized
[1650] processing and again this is a big
[1654] difference between the brain and maybe
[1656] the brain can use these kind of top-down
[1658] connections like Denon mentioned in the
[1660] brain to provide for tasks optimized
[1663] processing and sometimes insights
[1668] actually come from the computational
[1671] literature rather than the neuroscience
[1674] and I think that one of the most
[1676] profound insight from the computational
[1678] work was that learning is key for
[1681] generating good filters for object
[1685] recognition for example this is a slide
[1687] from a Khrushchev ski and Hinton seminal
[1689] work in 2012 and which they trained a
[1693] network to categorize all the images and
[1696] imagenet and then they looked at the
[1698] features and different layers of the
[1699] network and they found that in their
[1702] artificial neural network the features
[1704] in the first layer resembled that of v1
[1708] and the idea is that this may be filters
[1711] might be optimized for extracting the
[1713] natural image statistics across a broad
[1716] range of object categories so this of
[1720] course also leads to an obvious
[1723] questions whether prfs
[1725] in the human visual system are also
[1727] amenable to experience and maybe the
[1730] experience during human development so
[1734] what we did in our experiments we wanted
[1737] to test if perhaps are changing across a
[1740] childhood and adulthood so I'm gonna
[1743] describe two experiments that we did in
[1744] 25 children and 25 adults we use
[1748] children between the ages of 5 and 12
[1750] before age of 5 we cannot really K get
[1753] children to be still and attentive in
[1756] our scanner so it's gonna be very
[1758] difficult to do these experiments in
[1760] infants as then would like us to do and
[1763] nonetheless and this is an age of a lot
[1766] of a development in the child brain as
[1769] there's a lot of improvement and face
[1770] recognition and reading that involves
[1772] these higher-order areas so what we do
[1775] in this experiment we have participants
[1777] line in from our eye scanner we have
[1779] them stare at a central stimulus that's
[1782] a little bit more child friendly and
[1784] when the stimulus changes color the
[1786] participants press a button and as are
[1789] attending to the center we have a high
[1791] contrast bar with checkerboards sweeping
[1794] across the visual field and again we
[1797] make sure that the participants fixate
[1799] and our children can either
[1801] fixate across this target and what we
[1804] did is we measured PRF properties across
[1806] a ventral visual processing stream
[1808] between children and adults so this is
[1812] the average PRF size from across the
[1815] ventral visual hierarchy in children and
[1818] light colors and adults in dark color so
[1821] you can see that children like adults
[1823] have increasing receptive field size as
[1825] you ascend the visual hierarchy and in
[1827] fact there is no difference a
[1829] quantitative difference in the PRF size
[1832] across children and adults if you look
[1836] at the visual field coverage across
[1838] again retinotopic region and the ventral
[1841] stream in both children and adults you
[1843] see this really nice hemifield
[1845] representation and there seems to be no
[1847] significant difference between children
[1849] and adults at least in retinotopic
[1850] regions in the way that the receptive
[1852] fields die as a visual field so at least
[1855] by the age of five the early retinotopic
[1857] areas seem to be fully developed so what
[1862] happens in higher-order areas so this is
[1866] official fill coverage in the child
[1868] right P few spaces and you can see that
[1873] is in the right hemisphere now it covers
[1876] the left side of the visual field and
[1877] you can see this phobia bias as you can
[1879] see there's a higher coverage in the
[1882] center of gaze but you can also see that
[1885] a lot of the coverage is actually on the
[1887] lower left visual a quadrant but this is
[1893] a different visual field coverage than
[1894] what we see in adults as you can see
[1897] that there are two changes that are
[1898] happening first of all is a phobia bias
[1901] seems to be increasing from childhood to
[1903] adulthood that you can see there's a
[1905] higher density of Fogel coverage in
[1907] adults and we can quantify this by
[1909] measuring the center of mass of a visual
[1911] field coverage across a children and
[1913] adults and you can see that in the right
[1915] hemisphere specifically is this for real
[1917] bias increases from childhood to
[1920] adulthood another thing that you might
[1922] notice is that the area of a visual
[1924] field that is covered by the adults pee
[1927] reps is bigger than the children's fear
[1929] F because it extends into the upper
[1931] visual field as well as the ipsilateral
[1934] she'll field so and in fact if we
[1936] measure this this is about double the
[1938] visual fill coverage in adults as
[1940] compared to children so we see in these
[1943] higher-order face-selective regions a
[1944] profound development of P Refs
[1947] after the age of five yes five minutes
[1952] okay and so what does this mean in terms
[1958] of your behavior so if you're a child
[1960] and you're presented with the following
[1962] stimulus let's see where your visual
[1964] field coverage happens in your face
[1966] selective regions so I'm just plopping
[1967] it the right peepees faces visual field
[1970] coverage and you can see that most of
[1972] the the places where you have the
[1974] highest coverage is actually outside the
[1976] region where you have interesting
[1977] features for face recognition so what
[1980] you should do as a child is you should
[1982] move your gaze upwards and rightwards
[1984] because that would put your visual field
[1987] coverage on the place was informative
[1989] features and we could testify processes
[1992] by looking at where children adults look
[1994] at faces when they're asked to do a face
[1996] recognition task so on this example
[1998] stimulus this is the adults a fixation
[2001] and this is a child fixation and
[2003] consistent was our prediction you can
[2005] see that this child fixation has shifted
[2007] right words and upwards whereas adults
[2009] fixation is on the center of the face
[2011] and we can do this from many images and
[2013] we can see the bias in the child's
[2015] fixation compared to adults using a
[2017] vector and you can see that there is a
[2019] significant bias a child's fixate
[2021] upwards and right words and compared to
[2025] adults and basically they never fixate
[2027] downwards and leftwards because that
[2029] would push their visual field field
[2031] coverage actually even more outside of
[2033] the faces this is kind of interesting
[2035] because it shows that experience still
[2038] modes or prfs even through our childhood
[2040] development and it also suggests that
[2042] this is related to understanding where
[2044] our informative features in interfaces
[2050] so again the idea that in the brain as
[2053] well in the hdn ends the filters are
[2055] learned is probably useful because it
[2057] lets us adapt to our natural images
[2059] statistics and also adapt our a
[2062] processors for particular tasks that are
[2064] important for us on a daily basis
[2067] so to wrap up I hope I've convinced you
[2072] that this is an exciting point in the
[2073] field that we can combine advances in
[2076] both hdn ends and neuroscience to build
[2079] what I call new early accurate models of
[2081] the human ventral stream but in order to
[2084] make hdn ends nearly accurate sui also
[2087] have to make changes to the present if
[2092] architectures that are prevalent in
[2094] computer science specifically we might
[2097] want to consider how to implement HD NN
[2099] that actually have spatial topologies we
[2103] need to think about what's gonna change
[2105] in the HD NN if we are going to have
[2106] filters that change with eccentricities
[2109] we might need to think about how
[2111] implementing filters that are test
[2112] suggestible and not only during the
[2115] learning stage and I haven't talked
[2117] about it but there's also a lot of
[2118] temporal properties disease filters and
[2120] as dan has indicated right now most of
[2124] the architecture is a static and I my
[2129] great hope is that this a computational
[2130] understanding will not only lead to
[2132] generative models of the brain letting
[2135] us to better be able to predict brain
[2138] responses but also provide important
[2141] insights about the computational utility
[2143] of specific implementation features in
[2145] the human brain so thank you for your
[2149] attention
[2151] [Applause]
[2154] you
