---
schema_version: 1
id: yt-GlYnYbQ77Us
type: youtube
title: Thirion Bertrand - Encoding models for brain imaging
url: https://www.youtube.com/watch?v=GlYnYbQ77Us
authors:
- HBP Education
ingested_at: '2026-05-30T21:59:49Z'
content_hash: sha256:cbd2fafc456296b31bd70452251a86b3151bb8cff831a4609ac7623361b27ec5
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: HBP Education
  channel_url: https://www.youtube.com/@HBPEducation
  duration_seconds: 3494
  caption_track: fetched
  snippet_count: 1110
filter:
  score: 0.7
---
[9] you
[21] you
[29] so I'm
[32] peuta scientists involved in brain
[34] imaging for 15 years or so so I'm going
[39] to tell you what we try to do with
[43] computational tools on frictional images
[47] functional brain images to study how
[50] stimuli for instance encoded in brain
[54] activity well there can be a culture
[59] clash where I use terms that are not
[61] familiar to you or concept that are not
[63] familiar to you so please raise the hand
[64] I'm not here to sell anything I'm just
[66] here for you so if you need some more
[69] explanations just try the hand and I'll
[71] be happy to provide more explanations
[73] and hopefully be clearer alright in this
[79] presentation so there will be three
[83] parts as in any good presentation the
[86] first one will be just definitions of
[89] what we I call an encoding models or
[91] what the community called encoding
[93] models so how we can the type of models
[96] that I used to analyze functional images
[99] of the brain and then I will go a bit
[103] more into detail I will give an overview
[107] of the main sensory representations that
[111] have been studied by the community in
[114] the recent years and the crucial
[116] question of model comparison and then I
[119] will focus on validation because to me
[124] new ideas new technologies should always
[127] come with good validation so that we
[130] make sure together that we are on the
[132] right track ok so this is my framework
[138] so I'll be talking mostly about
[140] functional magnetic resonance imaging
[142] and I will assume that you kind of know
[145] what fMRI is but well this will be your
[149] crash course and fMRI if you need it so
[152] typically in coding neuroscience you may
[155] want to assess some theory of how the
[158] brain works so some cognitive theories
[161] this doesn't work and so too
[166] to probe such a theory you will pick a
[169] certain set of stimuli of things that
[171] your task that you want to be performed
[174] by a subject during an experiment and
[177] you organize them in an so called
[179] experimental paradigm it's just a
[181] sequence of tasks performed by the
[184] subjects during an acquisition so you
[186] take the fresh brain of a 20 year
[188] student and you put him or her in the
[191] scanner and you get these brain scans
[194] while the subject is performing the
[196] tasks and then at the time of that
[199] analysis you can try to try to relate
[202] the fMRI data that relate to the stimuli
[206] and encoding models go from stimuli to
[209] brain images it's a model that estimates
[212] the effect of a certain cognitive task
[216] on brain activity and decoding in the
[220] converse operation in which you input a
[223] brain image and will try to predict what
[225] task was performed what stimulus was
[228] presented okay so actually today I would
[232] have time only to cover mostly anchoring
[235] but we can talk about decoding later by
[239] the way I'll be leaving tomorrow at noon
[242] before brexit so so if you have any
[247] question of want to discuss we can
[249] discuss to night of course or tomorrow
[251] morning maybe before we go further you
[257] you may know are not bald functional
[260] magnetic resonance imaging board means
[262] blood oxygen level dependent so it's
[265] just a modality that we physically used
[267] to physically measure the brain response
[270] to the stimuli so the neural response to
[273] stimuli it's an indirect measures that
[275] actually does not measure neural
[277] activity but the blood response the
[279] blood oxygenation changes that follow a
[282] neural activity
[283] we believe it's a relatively good marker
[285] of neural activity but it's imperfect
[288] of course so we could use other
[292] modalities like eg and M eg if we work
[294] on humans or direct electric recordings
[297] if we work on animals
[299] so I'll be focusing on both for for
[303] simplicity here because I think it's
[306] quite advantageous overall to study what
[309] what I call brain encoding so the
[312] advantages of bold imaging is that a
[314] full brain coverage so you can map the
[318] responses in all brain regions and these
[321] with a decent spatial resolution about
[323] two millimeters isotropic which is which
[326] is okay to understand what brain regions
[329] are doing of course it's not sufficient
[332] to map cortical columns for instance so
[336] we don't have an excellent resolution we
[340] cannot truly map the detail of
[342] fractional architecture just we are
[344] getting close to it but not to that
[346] level may be the big disadvantage of the
[350] bald imaging is a temporal resolution
[353] because we are sampling blood response
[357] that takes five time five seconds to
[359] occur after neural activity and also
[363] induces a blurring of the response in
[365] time so we have a poor time resolution
[368] in in the data you can only have of the
[371] order of two seconds and I think I will
[376] discuss it more later but we don't have
[379] a real access to neural mechanisms we
[381] just kind of see the increase of
[383] decrease of local activity of the sets
[387] of neurons but of this is very far four
[390] mechanisms because we don't have the
[392] resolution because the measurement is
[394] too indirect okay so let's go a bit
[401] further now so remember we put the
[404] subject in the scanner and we say we
[407] presented some images to the participant
[409] and so the images were processed by the
[413] participant so you can think of
[415] different kinds of mathematical
[418] operations that are implemented by the
[420] neurons in the in the cortex and so the
[425] neurons activated depending on their
[427] properties and we observe through a
[430] complex metabolic pathway the
[433] response if we formalize this we start
[438] with the stimulus X so X is the vector
[442] of value that represents your input
[443] could be a natural image that you
[446] present it to the participant then from
[449] that will create a stimulus
[451] representation Phi of X this is really
[454] the core concept today so the the pixel
[458] values of an image may not be very
[459] interesting xi to understand brain
[461] activity will rather want to extract
[463] some features could be a color histogram
[466] could be a measure of the contrast in
[471] different parts of the image etc and
[474] then in a given brain locations so far
[480] sorry Phi of X is high dimensional
[481] typically because you cannot represent
[484] an actual image with just a few numbers
[487] you typically need relatively large a
[489] collection of numbers to represent a
[491] complex stimulus so Phi of X is high
[494] dimensional but in a given brand
[497] location you will have some coefficients
[500] beta that tell you how strongly the
[502] neurons are sensitive to the different
[503] dimensions of the representation so you
[506] will measure Phi of X dot beta and
[510] actually not measure that what you
[512] observe is a family activity Y which is
[517] this thing the neural activity but
[520] convolved in time with mo dynamic filter
[524] which is just due to the blood response
[527] the blood oxygenation changes which are
[530] represented by the temporal filter H so
[533] think of this as events occurring in
[535] time you need to convert their time
[537] occurrence with this mo dynamic dynamic
[540] filter then on top of it you've got some
[543] recent parameters like respiratory
[546] effect motion of the head etc plus plus
[549] some noise and this is the first model
[552] of the ball signal that you observed
[555] there's nothing new here this is very
[557] classical thing now you've got X and
[560] you've got Y okay you've got the
[562] stimulus represented and you've got to
[563] the ball signal you measured so how are
[566] you going to
[566] analyze this well first of all you will
[570] create the representation Phi of X that
[572] you fancy that you want it's your choice
[575] either as a modeler so to decide which
[578] features of the input may be relevant to
[581] explain brain activity and then the most
[586] common way once you have created this
[587] Phi of X the most common way to proceed
[590] is to take the ball signal Y and from it
[595] to essentially deconvolve the signal so
[600] you will essentially extract the
[602] response to the presentation of stimulus
[605] X so an estimate of the neural response
[609] for this given trial ok and then so this
[613] is the first step and then second step
[615] from this you will compute beta which is
[619] actually you parameter of interest so
[622] beta will mean in exit on brain
[625] locations the neurons are more sensitive
[629] to say the color information in the
[632] image or whether in the image there was
[634] a face represented or not etc so this
[638] information of the feature selectivity
[642] of the neurons is the beta vector does
[646] that make sense yeah and then one
[651] possibility one other possibility is
[653] also to estimate all the parameters
[655] jointly in a big minimization problem I
[658] will just now make this a bit less
[660] abstract by showing how it works in
[663] practice so you've got your fMRI data
[668] which I called Y in my previous slide
[671] and you create typically a model a
[674] temple model of your experiment this is
[678] called a design matrix so you know when
[681] across time when you present it the
[684] different stimuli and in typical fMRI
[689] experiments you would say in that case
[691] show images of famous faces scrambled
[695] faces or unknown faces so three types of
[698] stimulus stimuli which are
[701] different events in time and in most
[704] fMRI experiment you you take all the
[708] events of one type and you make one
[711] regressor - to capture the response to
[715] this condition okay and plus some some
[719] regressors of no interest which which
[721] are here and so typically in traditional
[724] fMRI analysis you would get the
[727] activation for famous versus unknown
[730] faces for instance and compare computer
[733] difference in response to these two
[735] conditions or scrambled versus unknown
[738] face typically but when we do an
[742] encoding analysis we do things a bit
[743] differently we develop the design into
[747] this kind of matrix in which now each
[750] column is for one single event so this
[753] is what I call previously the
[755] convolution step okay I told you that
[758] what you observed was a neuro response
[761] to each event convolved with the
[763] hemodynamic response well you've got it
[766] here there were some event in time and
[768] here you see the result of the
[770] convolution assuming that the human
[771] dynamic response is known you see the
[773] result of this the convolution and by by
[778] computing the correlation of this
[780] regressor with Y you will get what I
[783] could previously three V of x times beta
[787] okay and this is very classical it's a
[791] it's an standard ratably standard fMRI
[794] data analysis so more in detail for each
[797] of the columns of the design matrix it
[800] will obtain one brain image that shows
[804] you the amount of activity for each
[806] trial of your experiment okay each
[810] column being a trial here these images
[813] are ablaze are noisy because you've got
[816] very little signal to capture the effect
[819] so typically you will have a rather
[822] noisy noisy
[825] snapshot of brain activity and then so
[829] this was the deconvolution step and then
[832] in the encoding analysis proper you'd
[836] you take the stimuli that was presented
[838] for the first image which was like a
[840] face image a movie a famous face image
[842] okay and you say okay I create some
[845] representation of this stimulus which
[848] could be the contrast of the image of
[851] some global information about the face
[853] and you try to you will relate this Phi
[859] of X to the activity that was recorded
[862] for Phi or one a try all zero sorry
[865] trial 1 and so on trial 11 and probably
[868] you need many more trials to make a
[870] comprehensive analysis but that's the ID
[872] is that clear yeah okay so this is how
[880] people do in in reality well when they
[884] do this type of analysis
[888] I won't go much into details here
[891] there's also the possibility so in the
[895] in the previous slide I assume that the
[898] hemodynamic response age was known this
[901] may not be the case if it's not the case
[904] and you have a lot of fMRI data you can
[907] also try and estimate it from the data
[909] so we can estimate jointly the h and the
[912] beta this is a rather complex thing
[916] technically but then you obtain some
[918] estimates per voxel of the hemodynamic
[920] filter so yeah we on the data set we did
[924] that and we obtained a family of h
[926] filters one one per voxel so you see
[929] that essentially though there are some
[931] variations around a standard model that
[935] centrally Peaks in five seconds and then
[937] has an undershoot and when you have a
[942] lot of data it is advantageous to to
[945] learn the mo dynamic filter from the
[948] data rather than imposing predefined
[951] medomak filter you can see that it
[954] increases the performance of the
[956] and according model okay if you want to
[961] to get more details I'll give you the
[963] reference here but I just said that the
[967] performance of the encoding model is
[970] better so I need to define the
[971] performance of the encoding model
[975] remember that the encoding model it's
[977] interesting because it's a generative
[979] model it's a model that essentially is
[981] based on how the data are generated so
[984] once you have estimated the model on
[987] your data that is you have learnt a beta
[989] coefficient you can take then new
[992] stimuli and then simulate how the brain
[995] would respond to this new stimuli so you
[998] can essentially now guess the why that
[1000] would come if you put a new X into the
[1003] model okay because you know everything
[1006] to do that so this means that you can
[1010] use some validation measures like
[1012] cross-validation you take some data so
[1016] so stimulus fMRI images to train the
[1021] model to learn the data and then you
[1024] take another fold of the data to another
[1030] subset of the data to test the model so
[1033] based on X you simulate the Y and you
[1036] see how far you simulated Y is from the
[1039] true Y and this is measured by the R to
[1043] the coefficient of determination the R
[1045] to coefficient which measures the
[1047] difference between the true fMRI
[1050] activity observed in the test set versus
[1053] the one that you estimated from your
[1055] simulation compared to the simply the
[1059] violence of the of the Y in the test set
[1062] okay
[1063] and this number is smaller than one if
[1072] it's zero it means basically that you
[1074] have learnt nothing you are not doing
[1076] any better than just predicting the mean
[1079] of the test set so yeah you haven't
[1081] learned the variations in your in your
[1084] signal and if it gets if it's a very
[1088] good model it gets close to one because
[1090] if it's very good this goes to zero so
[1093] the r-square goes to one okay this R
[1097] square is measured in each voxel so for
[1100] each brain location you will be able to
[1103] say oh my my encoding model works or
[1106] doesn't work which is very important for
[1108] fMRI because we have good high
[1110] resolution so we will be able to say
[1113] that this brain region is well explained
[1115] by the encoding model while this other
[1118] brain region is not that also some other
[1123] possibilities but let's move forward
[1126] so to summarize a bit the Eid or
[1129] particular with a different picture
[1132] you've got some stimuli that are
[1134] presented in an experiment this is
[1137] called the input space and you can see
[1139] each of the stimuli as a certain vector
[1143] in a high dimensional space the space of
[1145] pixel values so the number of dimensions
[1148] will be the number of pixels in the
[1150] image but typically this X
[1153] representation where you just enumerate
[1155] the pixel values is not interesting it's
[1158] not meaningful okay probably you want to
[1160] extract some features from the image
[1162] like the presence of some objects the
[1165] the color information the amount of
[1168] contrast in the image and by doing this
[1171] you create a feature space and so you
[1173] encode your image in a certain feature
[1176] different feature dimensions this is Phi
[1179] of X and the mapping from X to Phi of X
[1182] can be nonlinear and then the final
[1188] thing is the
[1193] brain activation that you recorded with
[1195] fMRI which means that for each sample
[1197] you've got a vector of brain activity
[1200] and it's a vector in the voxel space
[1202] where each voxel is a brain location so
[1205] you can characterize each each sample by
[1209] the activity it elicited in in each
[1212] voxel so Phi of X is high dimensional Y
[1216] is high dimensional and Y is very noisy
[1221] obviously because measuring brain
[1224] activity is hard so we don't do anything
[1227] fancy here we just use a linear mapping
[1230] to relate the feature space to the brain
[1233] activity actually if you think of it
[1237] since you you need to fit the model for
[1240] each brain location and there are like
[1241] hundreds of thousands of voxel in your
[1243] brain and you are fitting a high
[1246] dimensional model because Phi of X is
[1248] high dimensional you need a very
[1250] efficient model to associate Phi of X
[1253] with Y so that's why I from the
[1258] beginning I implicitly assumed that it
[1260] was in there by saying essentially we
[1262] are going to learn a bit effector that
[1265] relates the feature space to the voxel
[1268] space okay and by the way decoding is
[1274] much is not much different when you do
[1276] brain activity decoding you just do the
[1279] same operations just you reverse that
[1282] arrow okay instead of mapping the
[1284] feature dimensions of the input to the
[1287] voxel voxel domain activation you just
[1291] predict the future characteristics from
[1294] the voxel from the brain activity so
[1297] from the values in the different voxels
[1299] and that's it okay so actually the
[1304] encoding and decoding are just you know
[1307] two two sides of the same coin okay and
[1315] well personally I can only learn by
[1318] doing things so if you if you've
[1324] would like to understand more and try we
[1326] provide some examples in the nylon
[1329] library it's an open source library that
[1332] you can just download now if you like
[1335] install and and play with the examples
[1338] as our examples in which we show you how
[1340] it works so you we take data from a real
[1343] experiment in which some visual things
[1347] were presented in a 10 by 10 screen so
[1351] 100 pixel screen and you've got brain
[1356] activity and you can so I will focus you
[1359] on the encoding information so for four
[1363] different voxels of the image domain you
[1367] can see here the four voxels are here
[1370] you can see the pixel in the image
[1374] domain that elicited activation in that
[1377] voxel so these are the beta coefficients
[1381] for each of the voxel in the in the
[1385] brain okay
[1386] and what you see in color here is a set
[1391] of a square value in each voxel how well
[1394] you can predict the activity of that
[1397] voxel in a given in unseen fMRI data
[1401] given your model and you see obviously
[1404] that you can predict brain activity only
[1408] in the visual cortex in the primary
[1410] visual cortex decoding is the converse
[1415] operation so essentially you can see our
[1421] well each pixel can be decoded from a
[1425] brain activity and for instance for this
[1431] pixel here
[1432] you can see the set the pattern of voxel
[1434] in the brain that predict the activity
[1437] the what happened in this pixel in terms
[1440] of stimuli so for nearby pixel you would
[1444] see some neighboring voxels involved in
[1447] the the prediction okay so play with it
[1454] okay let's go on I will go a bit deeper
[1459] now in sensor in to sensory
[1461] representations and the question of
[1463] model comparison I think there are two
[1468] key intuitions at least these are my
[1470] intuitions when I when I work on that
[1473] the intuition first is that for many
[1475] sensory systems there is a
[1478] correspondence between the physical
[1480] stimulus parameters and the brain
[1482] representations we can call that
[1486] functional gradients typically so the
[1490] best-known case is that of retinal tepee
[1493] okay you've got the visual field can be
[1497] a model at the two-dimensional structure
[1500] okay and it maps onto the
[1503] two-dimensional surface of the cortex
[1505] okay I will assume here that the cortex
[1508] is a surface which is not exactly the
[1511] case but forgetting the depths of the
[1514] cortex we we can consider it as a
[1520] surface and so the two-dimensional
[1522] visual field maps to the two-dimensional
[1526] cortical surface and it Maps smoothly so
[1530] it's a deformity creation ship in which
[1533] you sensory space
[1535] so here the locations in the visual
[1537] fields are mapped to here - actually -
[1540] the v1 regions or the retinotopic
[1542] regions okay so the general principle is
[1545] that you have a smooth invertible
[1549] actually relationship between what
[1552] happens in the sensory space and
[1553] cortical surface is also true if you
[1557] have very high resolution data for
[1559] visual orientation you see that the B in
[1565] the given location different
[1566] orientations are mapped in neighboring
[1570] neuron populations and this can to some
[1575] extent be seen with fMRI and there is
[1578] some continuity in this mapping this is
[1581] also the case for - not a P if you study
[1583] the auditory cortex you will see that
[1585] some voxels are more
[1588] responsive to some frequencies of the
[1591] audio content and there is a continuous
[1593] mapping between the frequencies and the
[1597] location of the voxels in the auditory
[1599] cortex it's actually I posit it-- that
[1602] it's also the case for the
[1604] representation of numbers with numerator
[1607] P where the one dimensional structures
[1609] number line that represents the
[1611] quantities organized in a topological
[1614] line this might correspond to a one
[1618] dimensional structure on the cortex this
[1624] was the first intuition the second one
[1626] is that for a complexity malucia you
[1631] will have different levels of
[1632] representations more or less abstract
[1634] you can always characterize an image by
[1638] relatively low level features like the
[1640] local contrast in the image color
[1642] istagram or by more high level features
[1645] like the semantics of the image oh
[1647] there's a face there's a landscape or
[1650] something like that and this corresponds
[1652] to different levels of abstraction and
[1655] these different levels probably
[1657] correspond to different brain areas okay
[1662] oh yeah normally this is a movie and it
[1666] moves the tire I put a PDF so you don't
[1669] see the the retinotopic stimuli moving
[1672] but the wedge stimulus should be
[1675] sweeping the the visual field and the
[1677] ring should be a ring that you see
[1680] expanding in the visual field so this
[1685] kind of stimuli are used to map
[1687] retinotopic information on the cortical
[1690] surface this means that for a population
[1694] of voxel in the early visual cortex when
[1697] you present the stimuli so system area
[1699] arpaio dick so you see that the voxel
[1702] will have the strong response at the
[1705] frequency of the stimuli and so this is
[1709] represented in that way so this is a
[1711] time post of activity in a given voxel
[1713] in the early visual areas when we show
[1715] the stimuli and so all the voxels
[1719] respond at the same frequency but the
[1721] Asthma phase
[1722] differences and the phase information
[1724] corresponds if one sums to the location
[1727] of the wedge in the visual field when
[1729] the vertical position is a certain phase
[1732] while the horizontal left position would
[1735] be a phase in quadrature and so on so
[1740] when we map the phase information with
[1743] the wedge stimulus we obtain this map on
[1746] the v1 visual cortex here we have drawn
[1749] v1 on the on the cortex and you see a
[1753] smooth mapping from the lower meridian
[1756] to the upper meridian so the where the
[1761] left part of the visual field is
[1763] represented on the right visual cortex
[1766] for the with the ring stimulus you would
[1771] map the retina to pick information
[1772] whether the voxel responds to more
[1775] central or peripheral visual information
[1778] and you see a continuous mapping from
[1780] Center to periphery with a much larger
[1784] representation of the central part of
[1787] the visual field okay this is super well
[1791] known it has been done hundreds of times
[1792] with fMRI it was actually the first big
[1795] experiment big encoding experiment of
[1799] fMRI was precisely a rich not a peep
[1802] historically and its support it's very
[1807] important actually because it's the
[1810] basic gradient to map the boundaries of
[1813] visual areas in the human cortex so we
[1817] can map visual areas in the dorsal
[1819] pathway so starting from the occipital
[1821] regions going up to the pilot also if we
[1824] expand it you go through v1 v2 dorsal v3
[1828] a B 3 B and then the entropy little
[1830] circus regions and you see here this is
[1834] the wedge information so the the polar
[1838] angle deformation of the visual field
[1840] you see how it is mapped along these
[1842] regions and same thing for the ventral
[1846] visual cortex going from the occipital
[1848] to the nipple regions
[1849] you've got different visual regions v1
[1853] v2 ventral v3 ventral beef
[1856] and then ventral occipital regions and
[1858] you see how the polar angle information
[1862] is mapped on these regions and similarly
[1865] how the eccentricity information is
[1869] mapped on these regions okay so this is
[1872] a key experiment in which we really see
[1874] as some functional structure on the
[1879] cortical surface through fMRI okay to go
[1886] a bit further then we need to introduce
[1889] the notion of model comparison because
[1897] typically what will happen is that you
[1899] will use some set of stimuli and then
[1902] you can generate different
[1903] representations so the so-called mapping
[1905] Phi that I called Phi from the beginning
[1909] actually there's no unique choice of Phi
[1911] you can make create different features
[1913] for instance from visual images you
[1916] could have feature that characterize
[1918] more the color content of the images or
[1921] the semantic content of the images or
[1923] the contrast in the spatial domain so
[1926] all these features could be extracted by
[1930] different models and so for the
[1933] different stimuli so different samples
[1935] of your experiments you generate these
[1937] different features which corresponds to
[1940] you encoding models of Phi and then you
[1945] will then see how well this Phi Phi one
[1950] representation explains brain activity
[1953] different locations using the R square
[1957] statistics which I introduced previously
[1959] you can do that for the few one and then
[1962] you can do that for free too and then
[1964] compare in which brain region c1
[1969] outperforms Phi 2 Phi 1 outperforms Phi
[1973] 2 so this is model comparison so model
[1976] comparison means in a given brain
[1978] location you see which model among few
[1982] Phi 1 and Phi 2 gets the best fit of the
[1986] data ok
[1991] and so now with this we can work on more
[1996] advanced computational models of vision
[2000] using the so called framework out 15
[2003] feet forward architectures in which a
[2006] given stimulus is processed in in
[2010] different steps in order to to achieve
[2013] some representations which can be which
[2017] are useful for instance for object
[2019] identification so this these
[2025] architectures have become very popular
[2027] in the last 10 years but they had been
[2029] there for 50 years I would say since
[2034] Hubal and visual discovery of complex
[2037] and simple cells in v1 and so the idea
[2041] the principles remains the same for an
[2044] hour 50 years which is that you can see
[2049] the processing of visual activity as a
[2054] sequence of layers in which neuron will
[2058] take some inputs combine them in early
[2061] and then will give the information to
[2064] will centrally apply some non-linearity
[2067] to this input and send it to the next
[2070] layer
[2071] so during many years the H max model was
[2076] the reference implementation for this
[2078] kind of processing so actually the model
[2081] was well well specified for the first
[2084] layer it was less clear how the next
[2086] players should be implemented so there
[2089] were some implementations of this that
[2091] were kind of working but we were still
[2095] lacking some principles to to get good
[2099] models for vision so Stefan mala has
[2103] introduced the scattering transform bit
[2106] more than five years ago now which was a
[2108] way using supervised learning to
[2112] generate some this kind of
[2114] representation so the idea was really to
[2115] cascade some kind of wavelet transforms
[2118] of the input
[2122] interleaved with nonlinearities but it
[2126] does not work that well what truly works
[2128] in vision problems is so-called
[2130] convolutional networks model so these
[2134] models are artificial models designed to
[2138] perform object recognition they are
[2141] exactly based on this principle but
[2144] simply the connections between the
[2148] neurons optimize to achieve the best
[2152] object identification so it's a
[2155] supervised learning okay so in the last
[2164] five years
[2165] many such convolutional networks have
[2168] become available and so we have used
[2171] them to see if they were a good
[2173] candidate model to explain brain
[2175] activity in humans so for a collection
[2179] of images that were presented to the
[2181] participants we have thrown the images
[2186] into three trained convolutional
[2189] networks and so we have creating the phi
[2192] of x where each Phi is the the the
[2198] activity in a given layer of the network
[2200] that comes when you present X so it's
[2206] the the artificial neural activity if
[2209] you like and so for each layer then you
[2211] try to see whether it can fit explain
[2215] the activity in each brain location
[2217] using the so called a square statistic
[2219] and so for each layer of the con that
[2223] you obtain an activation image that that
[2226] tells you how well each brain locations
[2229] is explained by the representation
[2232] generated by the layer 1 layer 2 etc
[2235] till the year 10 for instance if there
[2238] are 10 layers and what you see is that
[2240] actually the layer 1 will explain very
[2244] well activation in the major visual
[2246] cortex so in this part of the cortex so
[2249] in v1 and v2 while the the
[2253] the fifth layer typically will explain
[2256] less well v1 and v2 but a bit better the
[2259] surrounding visual regions and the final
[2262] layer of the artificial network will not
[2264] explain where the 1 and v2 will explain
[2267] well activation in the lateral visual
[2271] areas of the cortex actually it's it's a
[2279] very consistent and beautiful mapping in
[2282] which you can label each voxel by the
[2285] layer of the convolutional net work that
[2288] best explains it so for v1 and v2 it
[2290] will be the first layer and then the
[2293] surrounding regions like v3 it will be
[2294] the second layer etc and you've got this
[2297] onion structure of the visual cortex
[2300] that is recovered by the that
[2303] corresponds to the layers of the
[2305] commercial networks and we can we can do
[2311] that also with with by summarizing the
[2315] activity in different we want so we know
[2317] when we know the the borders of the
[2320] different written to pick regions we can
[2322] show that when some V one is best
[2324] explained by layer 1 and then quite well
[2326] by layer 2 and less well by the next
[2329] layers v2 is explained well by layer 2
[2333] and layer 1 and then less well v3 is the
[2338] best explained by layer 2 but not so
[2340] much by layer 1 and then decays and so
[2343] on so you really recover the visual
[2347] region hierarchy by comparing the board
[2351] activation to the to the representation
[2355] created by the convolutional network so
[2358] this has been observed and published by
[2361] many groups since 2014 yeah
[2368] so this has varied a lot and I think
[2371] it's still not fixed now you've got
[2375] pollard with more than other layers so
[2377] has net used for object recognition in
[2379] [Music]
[2381] artificial vision of course biologically
[2385] plausible model should have five six
[2389] layers something like that so yeah of
[2393] course there is remains a tension
[2395] between the optimization of the
[2399] artificial network for given tasks and
[2401] what the biology as has given us
[2404] certainly these commercial networks were
[2406] inspired by biological networks but now
[2411] I think they have at least most of these
[2414] networks they have become quite
[2416] different so there are some attempts
[2419] currently to create some networks that
[2422] are more primate like or human-like
[2426] so the Cornett Network has been designed
[2431] for that so it's a work by the DeCarlo
[2434] and colleagues so very similar things
[2442] has been done in the monkey context with
[2445] a physiology this is why what I'm
[2447] presenting today is not completely tied
[2449] to the board imaging actually the same
[2451] business can be done with electric
[2453] recordings the monkey
[2456] so they obtained for these types of
[2460] images the they analyze these images
[2462] through the convolutional network and
[2464] they tried with the convolutional
[2466] network to explain activity in different
[2470] locations of the info temporal cortex of
[2473] the monkey and what they found is that
[2477] well some of the neurons in IP were very
[2481] object specific points and some neurons
[2484] are chair neurons that respond when the
[2488] monkeys is a chair object or there are
[2492] some faces
[2493] neurons which responds selectively to
[2496] faces here is a one example for instance
[2499] and a bit as for humans we could not we
[2507] really need this complex multi-layer
[2510] conditional networks to explain the
[2512] activity
[2513] the info temple regions so the so-called
[2515] HMO layer in that case the old classical
[2520] models like H max which happened earlier
[2522] were not very good at D :
[2528] okay I'm going to skip that for the
[2531] interest of time but you can do them
[2532] same business for auditory cortex okay
[2536] I'll leave the slides available so if
[2538] you want to lock mine too that will be
[2541] fine so you can map you can have a
[2545] convolution Network for for sounds and
[2548] you will see some regions to the first
[2552] players of the red regions that respond
[2557] better that are better module by critic
[2568] of encoding models this is interesting I
[2571] think the value in these models but are
[2575] also some limitations maybe the first
[2579] one is a lack of interpretability
[2582] because typically I told you that we
[2585] estimate a beta in each voxel
[2587] which maps which says how strongly each
[2591] stimulus feature explains activity in
[2594] this foxhole but actually we don't look
[2596] at beta because beta is very
[2597] high-dimensional so how to look at that
[2599] so what we look at typically also called
[2602] a square statistics so we have very high
[2605] dimensional representations and we
[2607] summarized everything in a a square
[2609] statistic so this is not very easy to
[2613] interpret
[2613] I mean there remains a clearly some
[2617] ambiguity in the repetition of the model
[2619] I think partly related to your question
[2624] second model comparison is challenging
[2627] because the data of a limited SN now if
[2630] you just repeat the experiments twice
[2632] of course you hope Alagna second session
[2635] you hope to recover similar things but
[2637] well there are lots of noise in the data
[2639] which will not be reproduced like to
[2641] read the best a square that you can
[2644] achieve is probably something like point
[2646] 5
[2646] okay so the true scale of values that
[2649] you can achieve is between 0 and 0.5 and
[2653] so this max model model comprised in a
[2656] bit challenging so this means that you
[2659] need a lot of data to be able to go to
[2663] clear conclusion on whether encoding
[2667] model 1 is better than encoding model 2
[2669] you literally need to present thousands
[2672] of stimuli to your to your participants
[2680] no mechanistic insights yeah it has a
[2684] little danger here you could for
[2687] instance use as features of the images
[2691] the the color in a given location of the
[2696] visual space and just I could either as
[2699] RGB values okay you know playing and
[2702] coding of color information and maybe
[2704] this will explain activity in some given
[2706] voxel this doesn't mean that the neurons
[2710] in these voxels are encoding the RGB
[2713] channel information that is just mean
[2715] that they are sensitive to color but
[2717] maybe these neurons would be more
[2720] sensitive to the saturation of the color
[2724] and if they are sensitive to saturation
[2727] of course they will be explained a bit
[2729] by the RGB values but they will not be
[2732] neuron that encode RGB values so be very
[2735] cautious when interpreting this encoding
[2738] results and since with always have
[2743] limited stimuli because of time
[2745] constraints budget constraint that can
[2747] always be some confounding because
[2749] objects tend to co-occur together so
[2754] football ball will be always on a green
[2756] background like grass so if you can the
[2761] representation of the subject will be
[2763] correlated with other features of the
[2765] images so beware that the the
[2771] the images are the features of images of
[2774] a complex coalition structure and the
[2777] occurrence of object is may be related
[2779] to these features and so it's very hard
[2782] to to avoid this confounding because
[2785] it's present actually in the stimuli
[2787] that we use okay I have only have ten
[2792] minutes left I'm afraid I will need to
[2794] speed up a little bit I will leave you
[2803] slides
[2805] [Music]
[2811] see an experiment that we ran recently
[2814] on videos instead of working simply with
[2817] still images you could present a movie
[2821] to the participant and try to encode
[2823] this visual stream and see how well it
[2827] explains activity in the in the visual
[2830] cortex in the cortex and so we here we
[2833] took two such networks one that was
[2837] based on the optical flow so the
[2838] difference between successive frame and
[2840] one simply based on the RGB so the the
[2845] the color information across all pixels
[2848] so like like a static model but sampled
[2851] in time and we have different layers for
[2855] each of these networks and with this we
[2857] could see in several subjects
[2859] characterize the difference of the
[2861] response of different voxels in the in
[2865] the brain we actually acquire data on
[2868] the world brain but you see that the
[2870] responses are stronger only in the
[2874] occipital temporal Junction and although
[2878] all the occipital regions the the middle
[2881] path etc the the interesting thing is
[2885] that when we see which layer explains
[2889] well which voxels we obtain some
[2892] relatively clear boundaries some of them
[2895] are related to the different visual
[2898] areas some of them are not and it was a
[2901] bit of a strange result for instance
[2904] with so this is a contrast map that
[2908] shows the for each voxel whether it's
[2913] best explained by the RGB visual network
[2918] or the optical flow network so RGB is in
[2922] color or in a yellow red color and the
[2926] optical flow is in blue and this this
[2929] contrast does not correspond to
[2932] boundaries between visual areas it
[2934] actually corresponds to the
[2937] representation of eccentricity in this
[2940] subject so we also did a retinotopic
[2942] experiment in the same subject and you
[2945] see that the most peripheric regions in
[2948] terms of retina taupey are those that
[2950] respond to the optical flow in blue and
[2956] IC sorry I was wrong in my my my
[2961] explanation so the the peripheral
[2964] corresponds to the optical flow yeah
[2966] while the most Fourier regions that see
[2969] the central part of visual field are
[2972] best explained by the RGB Network and
[2975] actually there is a very good
[2977] correspondence between these two maps
[2978] which were acquired independently on the
[2981] same subject yeah it was tedious for
[2987] them the subjects hate this protocol I'm
[2994] putting that because this data will be
[2996] made available soon the next month in
[3000] the HVP a knowledge graph so they will
[3003] be accessible to to the community it's
[3007] part of the so-called individual branch
[3009] charting protocol so there's a web
[3011] interface so you can anybody can create
[3014] an account even if you're not part of
[3016] the HVP yourself you can create an
[3020] account to get access to the public data
[3022] and this data will be public and you can
[3025] query data across species protocols and
[3028] modalities so it's fMRI but you can get
[3033] its fMRI on humans on this video
[3036] watching your protocols
[3038] or written to big protocols but you
[3040] could query data from different species
[3042] and protocols and actually yeah HBP
[3049] human brain project has put a lot of
[3051] effort into the data integration in the
[3055] so called new informatics platform where
[3057] people can contribute data that are
[3060] curated and integrated into what the so
[3064] called knowledge graph that links the
[3067] data to metadata which is important to
[3069] be able to relate to them here I'm
[3071] referring only to the human fMRI staff
[3074] but there will be some data on different
[3078] animals etc and you can then create this
[3081] data by either some meta information or
[3085] the brain locations they relate to and
[3088] so on I think in that one we we
[3097] reproduce the one by Jack gallant from
[3099] back lay so it's a short video clips but
[3103] recently we've been doing Raiders of the
[3106] Lost Ark which was most much better for
[3108] the participants and we will be doing
[3111] the good the bad and evil assume so it's
[3120] an experiment in which we we have
[3121] selected a few subjects and we scan them
[3123] 50 times wearing as much as possible the
[3127] experimental conditions yeah this is
[3132] funny so you could stop with that one
[3136] way to validate and I'm obsessed by
[3138] validation okay it's it's good to tell
[3141] nice stories about the brain but it's
[3143] even much much more important to
[3145] validate them so how can we validate all
[3147] that business so one possibility is to
[3149] try and reconstruct the images that were
[3153] seen by the subject and this is the
[3155] converse a person it's decoding so you
[3157] give me the fMRI map and I try to
[3160] predict what was seen by the subject and
[3162] so the the thing works out that way you
[3166] have the training edges
[3167] you've the corresponding ephemeral
[3169] activity with a generator
[3172] you can try and reconstruct the training
[3174] image and you've got so the generator is
[3178] a deep network like a network that we
[3181] talked about and then you've got two
[3184] networks a discriminator that tries to
[3188] to predict if the image is real or fake
[3190] you want to reduce the gap between the
[3195] true images and the fake images or the
[3199] reconstructed images so as in a gun
[3203] Genet generative address our network and
[3207] your server comparator which tries to
[3209] make the reconstructed images as close
[3212] as possible to the training image and
[3214] then this is at training time so on a
[3218] bunch of images and then at test time
[3220] you take a test image and based only on
[3223] fMRI activity you generate the
[3225] corresponding reconstruction which is
[3227] not exceptionally nice in that case but
[3232] at least femoral activity has captured
[3235] something in terms of color or position
[3239] of the input image and so on so this is
[3247] this is demonstrated in this paper so as
[3252] you can see it's kind of successful I
[3255] mean it's not great obviously it does
[3258] not reconstruct the images so well it
[3260] usually captures the the visual layout
[3263] of the object in the image for sure
[3266] sometimes it captures a bit of color a
[3268] bit of texture of the images and of
[3272] course quite well in the central part of
[3275] the image while subjects fixates and not
[3277] so well in the periphery even more
[3284] challenging and it this has been done by
[3285] somebody from the HVP so the team of
[3289] Heiner Gerber it's about a mental
[3293] imagery where subjects were first
[3296] perceiving some letters displayed on the
[3299] screen and you can reconstruct the
[3303] the image of the letter based on fMRI
[3306] activity for the HTS C thing so it was
[3310] quite well in perception and it works to
[3313] some extent when the subject no longer
[3315] perceive the image but now try to to
[3318] visualize by mental imagery try to
[3322] recreate the image of the H the T the s
[3325] of the C actually finally the T works
[3328] quite well maybe because there is this
[3330] vertical bar in the middle which can be
[3333] captured actually by the model quite
[3335] well it works not so well for our
[3337] features of our letters actually I had
[3343] done an attempt at that a few years ago
[3345] and it's very challenging but it turns
[3348] out that we can to some extent and at
[3351] least better than chance generalize a
[3353] perceived images to mental imagery okay
[3362] it's time to conclude so the name of the
[3367] game was to compare complex
[3369] representations of cognitive content to
[3371] brain activity and I think that the key
[3373] concept is representations now with deep
[3376] learning solutions we have a great tool
[3378] to create good representations of
[3380] objects and benchmark them against
[3383] productivity and these representations
[3387] concept is very key in current deep
[3391] learning technology there's a big
[3394] bottleneck which is a limited SNR of the
[3397] data it's too far from arrive but it's
[3399] also true for M eg eg or any modality
[3402] that you would use and because we can
[3404] only acquire a limited number of samples
[3408] so there are lots of ongoing work I
[3411] think one of the interesting works
[3412] actually it relates to your question you
[3416] can design different architectures for
[3418] different tasks and how well these
[3420] different architectures will explain
[3422] brain activity I think it's a key
[3424] question and also working with language
[3427] for instance is a big challenge
[3429] because language is a complex content
[3432] before which now we start to have good
[3434] computer computational models
[3436] so we could compare these models to
[3437] brain activity lots of resources so of
[3441] course go to the a trippy knowledge
[3443] graph and you will see some some data
[3445] but there are also some public data so
[3448] you can look at them look at them
[3451] we provide open source software which
[3454] can be installed and you can run the
[3458] examples I can guarantee that all the
[3460] examples run so don't hesitate and I'd
[3465] be happy to to help on that and that's
[3469] it thank you for attention
[3471] [Applause]
[3477] [Music]
[3492] you
