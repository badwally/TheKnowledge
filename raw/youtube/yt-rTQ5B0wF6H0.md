---
schema_version: 1
id: yt-rTQ5B0wF6H0
type: youtube
title: 'CCN 2021: Controversial stimuli: Optimizing experiments to adjudicate among
  computational hypotheses'
url: https://www.youtube.com/watch?v=rTQ5B0wF6H0
authors:
- Cognitive Computational Neuroscience
ingested_at: '2026-05-30T20:02:07Z'
content_hash: sha256:3f57ea2573539c13b7395de4af57ad2f8681a6476c39f448944b241ae3e7929f
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Cognitive Computational Neuroscience
  channel_url: https://www.youtube.com/@cogcompneuro
  duration_seconds: 10424
  caption_track: fetched
  snippet_count: 3953
filter:
  score: 0.75
---
[1] all right we can go ahead and get
[3] started um so hi everyone welcome to um
[6] the ccn virtual conference and to
[10] our second keynote and tutorial
[11] presentation so my name is leila ishik
[14] i'm a member of the program committee
[15] and i'm going to give a brief overview
[17] of ccn before i introduce the talking
[19] speakers
[23] so this is the ccn executive and
[26] communication committees thomas
[27] nasaleris enrique nunberg russ pauldrack
[30] and kendrick k
[32] as well as the program committee gunner
[34] bloom megan peters lena jones who's my
[37] co-host today
[38] ralph hefner gemma roy carlos ponce
[42] myself and jennifer lieberman
[45] and the program consists of three types
[48] of events that we really tried to
[50] optimize for the online format so the
[53] first was the algonauts challenge which
[56] and presentation which was the first
[58] kickoff event of the conference so if
[60] you missed it
[61] the recording is available on the ccn
[63] website
[64] we also have several genera generative
[67] adversarial collaborations um an
[69] innovative new style of event that began
[71] last year and has continued this year
[74] and this is our second keynote and
[76] tutorial
[78] so just to give you a brief rundown of
[80] the
[81] upcoming events that still happen we
[82] have the generative adversarial
[84] collaborations
[86] and so the idea behind these is that
[88] often in science you just have groups of
[91] like-minded people talking together and
[93] it's really hard
[94] to bring together people with
[96] alternating alternative
[98] ideas and philosophies and so that's
[100] really what the gac aims to do
[103] is to bring researchers with alternative
[105] theories together to help resolve their
[107] differences
[109] um so together they design an event that
[111] can
[112] help disambiguate between these
[114] different controversies
[116] um and the goal is really to foster
[119] healthy and collaborative scientific
[121] progress
[123] so we've had one gac so far which was
[127] extremely interesting on how visual the
[129] role of visual experience on
[132] ventral pathway representations
[135] and we have
[136] four more upcoming one is a progress
[138] report of all of the gacs from last year
[140] 2020 so you can see how these this
[143] process evolved over the last year
[145] and then three more on what constitutes
[147] understanding of the ventral pathway how
[150] does the brain combine generative models
[152] and direct discriminative computations
[154] and high level visions and then a final
[156] one on what makes a representation
[158] useful
[161] today we have our second keynote and
[163] tutorial
[165] and so the idea behind these was to move
[167] beyond a traditional keynote talk
[170] and so these will include an exciting
[172] keynote talk which i'm looking forward
[174] to hearing today but it will also
[176] include a following tutorial to give you
[178] a look under the hood to see the
[180] technicalities of how that's exciting
[182] science came about
[185] in addition it really
[187] will encourage open methods hands-on
[189] tutorials and help educate everyone on
[191] these cutting edge methodologies
[193] in order to enable
[195] new analyses and showcase the science
[199] and work behind the talks we often get
[200] to see
[204] and so the goal is for you to really
[206] learn the science and the tools so they
[208] will highlight the specific scientific
[210] assumptions their interpretations their
[212] analysis tricks etc
[216] and we really sought to increase
[217] community engagement so all of the
[220] keynote and tutorials were selected from
[222] community submissions that were open to
[224] the
[225] general ccn community
[228] and we've really prioritized
[232] quality of science but also quality of
[233] the tutorial diversity and what we
[236] thought everyone would get from the
[237] different topics
[240] um and so
[242] um yesterday we had our first tutorial
[244] on voxel wise modeling which if you
[245] missed it again a recording is available
[247] on the ccn website
[249] um and so today we are going to hear
[251] from nico cricuscorte talgolon
[256] on controversial stimuli optimizing
[259] experiments to adjudicate among
[260] computational hypotheses and then
[262] there's one following one on flexible
[264] identification of popular population
[266] dynamics from neural activity recordings
[270] um and so the goal of moving of this
[273] your ccn with everything online is to
[275] really make this
[277] a success we really need your
[278] participation so we encourage everyone
[280] to come participate in the tutorials
[282] learn all you can
[284] and enjoy it
[285] um and so
[287] with that i'm going to turn it over to
[289] nico cricuscorte who's going to give her
[291] deliver the keynote portion of this
[293] event
[294] so nico is a professor at colombia in
[297] both the departments of psychology and
[299] neuroscience and he is the director of
[303] cognitive imaging at the zuckerman mind
[305] brain behavior institute at columbia and
[308] many of us know nico from his pioneering
[311] methods in computational cognitive
[313] neuroscience and so we're excited to
[315] hear about
[317] his recent work and controversial
[318] stimuli
[340] what an amazing conference leila thank
[342] you so much this is uh super cool i'm
[345] really excited about what the the new
[347] program committee
[348] and executive committee has done here
[356] slide sharing working
[359] great
[361] okay so
[363] let's talk about controversial stimuli
[366] my title is controversial stimuli
[369] optimizing experiments to adjudicate
[371] among computational hypotheses
[374] in a sense what we're talking about here
[376] is nothing new at all it's something
[380] very very standard and something that um
[383] scientists always do scientists always
[386] want to design experiments to adjudicate
[388] among competing hypotheses and that's
[391] really all we're doing here just in a in
[393] a new context in a sense
[396] in perceptual neuroscience the
[398] experimental design involves a choice of
[400] stimuli
[403] and when our theories are implemented in
[405] complex brain computational models as is
[408] increasingly the case in cognitive
[409] computational neuroscience then we need
[412] optimization techniques to make stimuli
[415] that elicit distinct predictions from
[417] different models so this is just
[419] designing good
[421] experiments and this last phrase here
[423] stimuli that elicit distinct predictions
[426] from different models is the definition
[428] of controversial stimuli so the idea is
[430] that these stimuli are controversial
[434] between two models or among a set of
[437] models
[439] there's also
[440] a deeper and more complex issue behind
[443] this
[444] and it's the question whether we can
[446] make theoretical progress with these
[449] highly flexible models that we now have
[453] neural network models give us a language
[456] for expressing computational hypotheses
[459] and that's
[460] extremely useful for cognitive
[462] computational neuroscience and it's key
[464] to the field actually because it links
[467] cognition to its implementation in the
[469] brain it allows us to
[471] explore our theoretical ideas
[474] about how the information processing in
[476] the brain actually works
[479] however their high parametric complexity
[482] is both a blessing and a curse it's a
[484] blessing because it means that these
[487] models can capture intelligent behavior
[489] and the history of ai has shown that we
[492] need high parametric models to capture
[496] intelligent processes because
[498] intelligence requires a lot of knowledge
[500] and without that knowledge in the model
[502] the model cannot
[504] be intelligent and therefore it can also
[507] not capture higher level cognitive
[509] processes or even perceptual processes
[513] however this high parametric complexity
[516] is also a curse because it makes it hard
[518] to adjudicate between models so the
[520] people in our community who feel that
[522] these highly flexible models might be
[524] problematic
[526] they also have a point so because it's
[529] much more challenging both at the level
[531] of interpretation and at the level of
[534] statistical analysis to really um to
[537] really test and compare these models
[541] so on the one hand we need high
[543] parametric models to capture cognitive
[545] function but the question is how can we
[547] adjudicate among these highly flexible
[550] models
[552] i want to start with two examples from
[556] our lab's work that illustrate
[559] why we need controversial stimuli the
[561] first example is from camilla yotswick
[564] kate stores and jonathan o'keefe
[567] and it's about explaining
[569] human face dissimilarity judgments
[572] so what camilla and kate and john did
[574] was they generated faces with the basel
[578] face model a face graphics model where
[581] they sampled on this
[583] polar
[584] in these polar coordinates a set of
[587] experimental faces
[590] and then they use the large
[592] touchscreen to have uh subjects arrange
[595] many different pairs of faces along the
[597] vertical dimension to indicate how
[599] dissimilar these faces look to them
[603] so this was uh sort of dragging on the
[605] touchscreen you you put your finger on
[607] and you can drag these pairs around and
[610] it's only the vertical dimension that
[612] that counts here
[613] and enables you to communicate how
[616] distinct
[617] you you perceive
[620] every pair of faces
[624] so and then um we used a wide variety of
[627] different models in order to predict
[629] these face dissimilarity judgments so a
[633] set of models was obtained from the
[634] basel phase model so the internal
[637] parameters in the latent space of the
[638] basel face model as well as separate
[643] sets of components of this latent space
[646] the shape parameters of the texture
[647] parameters
[649] and a couple of other variations
[651] and they also tested deep neural network
[654] models different versions of the vgg
[656] architecture trained with either faces
[658] or objects and the alex net architecture
[661] and then also some older models the hmax
[664] model and the gist model which provides
[666] these summaries of
[668] gabors so it's a lower level
[671] older engineered feature model and then
[673] a couple of more high-level models about
[675] the configuration of faces and also
[678] about the
[679] the person attributes of the people
[685] so when they did a model comparison and
[687] here i'm showing you the model accuracy
[689] it's the pearson correlation of the
[691] representational
[693] dissimilarities predicted by each of
[695] these these models so these are
[696] distances in in the representational
[699] spaces of this model correlated with the
[702] dissimilarity judgments
[704] what they found was that
[707] some models could be rejected so we have
[710] some models here that are significantly
[712] below the noise ceiling so that's good
[714] we learned something but there's also
[716] this set here of models all of which are
[720] very close to the noise ceiling and
[722] they're not significantly different from
[724] each other and that included image
[726] computable models the deepnet models the
[728] gist model as well as this basel phase
[731] based
[733] latent latent models and sub-components
[735] of it
[737] so
[739] some good insights here and it's
[740] important to know that all these these
[742] models do pretty well but of course we
[744] would like to be able to distinguish
[746] these models because not all of them are
[749] likely to be correct simultaneously so
[752] why can't we distinguish these models
[754] here
[754] and the reason is the models are
[756] confounded they make similar predictions
[758] for natural and synthetic faces that are
[761] not chosen expressly to discriminate
[763] them so and if we wanted to take the
[766] next step and discriminate these models
[768] we'd have to design our our stimulus set
[771] in some way
[773] second example is from kate stores
[777] and
[777] she found that diverse deep nets all
[780] explain the human inferior temporal
[783] representational geometry similarly well
[786] after
[787] categorization task training and fitting
[790] to the it representational geometry so
[793] we use the the term training when we
[797] adapt the model to perform the task as
[799] well as possible and we use the term
[801] fitting when we adapt a model to explain
[805] brain or behavioral data as as well as
[808] possible
[810] so here kate did
[811] the both on a number of uh classical and
[816] well-known vision models
[818] and i'm showing you here the accuracy
[820] with which each of these models predicts
[822] the humanity representation of the
[824] similarity matrix for a set of little
[826] isolated natural object images
[832] so here in the different colors we have
[834] all combinations of trained and
[836] untrained and fitted and unfitted where
[839] trained as i've told you as refers to
[841] the categorization task training and
[843] fitting to the adaptation to make the
[846] model better capture the
[847] representational geometry which involve
[851] computing a pca for a separate set of
[853] images and then
[855] inferring some weights for these pca
[857] components
[861] so for lxnet it looks like this so both
[864] training and fitting helps somewhat but
[868] even the untrained and unfitted model
[870] with with
[871] random weights explained some variants
[873] already and then when we look at all the
[876] other models we see a strikingly
[879] similar picture with most of the models
[881] sort of
[883] approaching the lower bound of the noise
[886] ceiling but not quite reaching the noise
[888] ceiling
[889] and the models very similar to each
[892] other
[893] so all these models were trained and
[895] tested on natural images
[898] and we think that might be
[900] part of the problem here
[902] we think that it's the shared features
[905] of these models the deep hierarchy and
[907] the fact that all convolutional that
[909] explain the relative success of these
[911] models
[914] so why can't we distinguish the models
[916] well each model's parameter space is too
[919] expressive here it's a universal
[921] approximator for the distinct inductive
[924] biases that these models do have to be
[926] revealed when we're training and testing
[928] on natural images and then fitting to
[931] brain activity data so despite our
[934] use doing the statistics correctly here
[936] you know we're using cross validation
[938] we're using independent image sets
[941] you know there's nothing wrong with the
[942] statistics but
[944] the flexibility of the models means that
[948] for natural images they end up making
[950] all similar predictions
[954] so this brings us to controversial
[956] stimuli um
[958] and
[959] talgoland's
[961] motivation for uh pursuing this
[963] direction in our lab
[966] training and testing on different sets
[968] of natural images often does not reveal
[971] the differences between models
[974] so we need stronger tests of
[976] generalization performance this is i
[979] think a very very important point that
[982] tao keeps making in my lab
[986] first insight is that to elicit models
[990] distinct inductive biases we can test
[992] models on a population of stimuli that
[996] was not used in training so this is an
[998] out-of-distribution generalization
[1001] challenge and it's it provides a more
[1003] severe test of each of the models
[1006] to do this we could use natural stimuli
[1009] for example we could use stimuli drawn
[1011] from a different stimulus population or
[1014] we could use synthetic stimuli stimuli
[1017] optimize to elicit bolder predictions
[1019] from each of the models
[1023] the second important insight is that
[1025] since our goal is to adjudicate among
[1027] models because we want to make
[1029] theoretical progress we want to find
[1031] differences between models that provide
[1033] us some direction for changing
[1036] our theoretical positions
[1038] we can create synthetic stimuli that are
[1040] optimized to elicit distinct predictions
[1043] from different models
[1045] and stimuli that are controversial among
[1048] the models
[1050] so one way to create a synthetic stimuli
[1054] that elicit bolder predictions from each
[1056] of the models is to create maximally
[1059] exciting stimuli for particular layers
[1062] of a model of particular units and
[1064] models so you choose some portion of the
[1066] model for example a unit and then you
[1068] optimize the stimulus so as to drive
[1072] that unit as strongly as as possible and
[1075] possibly more strongly than natural
[1077] stimuli would and then
[1079] the model makes a strong prediction
[1081] which is that the corresponding neurons
[1083] in the brain also uh respond very
[1086] strongly to that very unnatural stimulus
[1089] and since that stimulus is very
[1091] different from any stimuli used in
[1094] training the model this provides a
[1095] strong test of generalization
[1097] performance
[1099] however our interest here is in
[1101] controversial stimuli because we're
[1103] interested in adjudicating among
[1106] different models
[1107] so in that case we need to define some
[1110] controversiality measure some
[1113] quantitative
[1114] objective that we can optimize
[1117] that compares the outputs of both models
[1120] so it could be that the models
[1122] categorize the given stimulus
[1124] differently or it could be something
[1126] about the representational geometry for
[1128] example that the rdms are not highly
[1131] correlated or something like that we
[1134] need to define the controversiality and
[1136] then we can use various optimization
[1139] techniques to change the stimuli to
[1143] optimize the stimuli usually iteratively
[1145] and make a set of stimuli that
[1149] achieves a high controversiality
[1152] score
[1155] tell first explored this using the mnist
[1158] data set so in a very small kind of toy
[1161] setting that's already interesting
[1163] because we have these these natural
[1166] little handwritten digits
[1169] and he tested a wide range of different
[1172] vision models and an important thing in
[1174] designing this was to
[1177] have the models
[1178] really sample interesting theoretical
[1181] dimensions so tell wanted to have feed
[1184] forward models as well as recurrent
[1186] models and he wanted to have generative
[1188] as well as discriminative models and
[1190] fill all these these four resulting
[1192] quadrants
[1194] so here are the the actual models some
[1197] of them were feed forward discernitive
[1199] that's the sort of standard deep neural
[1201] network categories some some of those
[1203] were adversarially trained
[1205] and then there were recurrent models
[1207] that were
[1208] discriminative in their
[1211] in their inference mode
[1213] and then there were generative models
[1215] where the inference was nevertheless
[1218] feed forward just one of them the
[1220] gaussian kernel density estimator model
[1223] and then there were recurrent models
[1224] that used some kind of generative
[1228] approach to
[1230] perceptual inference so that included
[1232] the catching that recon and a shot
[1234] analysis by synthesis or shot abs mode
[1240] the controversiality index in this case
[1243] was defined as follows controversiality
[1247] is
[1248] indexed by the digit pair and the model
[1250] pair so controversiality is defined for
[1252] a model pair in the digit pair and it's
[1254] a function of the image and it's this
[1258] function it's this minimum
[1260] across four probabilities and we're
[1262] maximizing the controversiality so we're
[1265] maximizing this minimum which means that
[1268] we're ensuring that all four of these
[1271] probabilities are high so what do these
[1273] probabilities mean this one means that
[1276] model a detects digit a this one means
[1279] that model a does not detect digit b
[1283] thinks that digit b is very unlikely to
[1285] be present
[1287] in the image
[1289] this one means that model b detects
[1291] digit b
[1293] and that
[1294] this one means that model b does not
[1296] detect digit a so it's a it's a full
[1299] double dissociation if you will uh model
[1302] a thinks it's a with high con
[1305] confidence and not b and model b thinks
[1307] it's b with high confidence not a so
[1310] that's a very strong
[1311] way to define controversiality
[1318] to get a better intuition on this uh tel
[1321] plotted the model output as a contrast
[1324] so here's you see the probability
[1327] that model a
[1329] um
[1332] it uh assigns to uh
[1335] the image containing a seven minus the
[1338] probability that model a assigns to the
[1340] image containing a three so that's a
[1343] contrast where at one end of the axis
[1347] model a detects a three but not a seven
[1349] that the other and it detects a seven
[1351] but not a three
[1353] we can do the same for for model b and
[1355] we get this two-dimensional
[1359] space so in these two quadrants the
[1362] models agree about a given stimulus
[1366] and in these two quadrants the models
[1368] disagree
[1369] when we look at the original mnist
[1371] images they they all
[1373] fall in these corners so deep into the
[1376] model agreement quadrants
[1378] and this illustrates how
[1380] it's going to be very difficult to
[1382] distinguish the model based models based
[1384] on their behavior because they've all
[1386] been over trained with this set of
[1389] natural little hand written digits and
[1391] their behavior is essentially going to
[1393] be
[1394] mostly correct for all of the models and
[1397] also identical to
[1399] human
[1400] categorizations of these images so if we
[1403] really want to say something about the
[1405] the computational mechanism we have to
[1407] probe the models of different stimuli
[1410] and we can use optimization to drive an
[1412] initial seed of a random image
[1415] into this model disagreement
[1418] quadrant here so here you have a
[1420] controversial stimulus
[1422] which uh to model a is a seven but not a
[1426] three and to model b it's a three but
[1429] not a seven
[1431] i see a seven there so i would say in
[1433] this case i i agree with with model a
[1436] but of course we need to ask uh subjects
[1440] in psychophysical experiments
[1443] so this is an example of a controversial
[1445] stimulus
[1447] for this amnesty
[1449] so in this way we can pit models against
[1452] each other so here um let's pit caps net
[1455] recon versus madri l2 when we do that we
[1459] can do that for all pairs of stimuli so
[1462] here for a given pair of models you see
[1464] all pairs of stimuli and for each of
[1467] these stimuli you can ask yourself
[1470] what does it look like to you
[1472] and does your label the label you would
[1475] put on that image agree with the label
[1478] provided by capturing that recon or
[1481] modery l2
[1482] so in this case there's a bit of
[1484] ambiguity here but most
[1487] most of us see
[1489] columns
[1490] of consistent digits here indicating
[1493] that their
[1494] their
[1495] perception of these images is more
[1497] consistent with the labeling provided by
[1500] captionnet nikon
[1502] so let's put capsulenet recon versus the
[1506] gaussian kernel density estimator
[1509] and in this case
[1511] even more clearly
[1513] most people see rows of consistent
[1515] digits indicating that the gaussian kde
[1518] better captures
[1520] human perception
[1522] so let's let's put gaussian kde against
[1525] short analysis by synthesis
[1528] in this case
[1529] most of us
[1531] clearly see columns of digits here
[1534] indicating that the short
[1537] analysis by synthesis model appears to
[1539] dominate the gaussian kde model
[1543] so tell generated these controversial
[1546] images for all pairs of digits and all
[1548] pairs of models creating this
[1551] this really large set of stimuli
[1556] and then he used these stimuli
[1559] in a psychophysical experiment
[1563] and in the experiment subjects were
[1565] presented with one of these stimuli at a
[1568] time and then they indicated the
[1571] probability that the image they're
[1573] looking at contained each of the digits
[1576] and these probabilities did not have to
[1579] add up to one so it was perfectly
[1583] reasonable to indicate that there is a
[1586] lot of evidence or high probability
[1589] for two of the digits at the same time
[1592] in the image
[1596] so when tal analyzed the data
[1599] the first thing we note is we can we can
[1602] compare all these models and they they
[1604] perform distinctly but um a prominent
[1607] feature of the set of results is that
[1609] none of the models reaches the noise
[1612] ceiling so we notice this large gap here
[1614] between the noise ceiling and
[1617] the best performing model
[1620] and
[1621] the second observation is that the best
[1623] performing model here is the shot
[1625] analysis by synthesis model and perhaps
[1628] consistent with what you could
[1629] experience by just looking at the
[1631] controversial stimuli
[1633] and this shot abs model was
[1635] significantly better than
[1638] all of the other models in this analysis
[1641] when we look at the the three relatively
[1644] best performing models here and look
[1646] back at our entire
[1649] scheme of of the different models we
[1651] note that all of the three best
[1653] performing models
[1655] involve some kind of generative
[1658] inference process
[1660] so we think that by
[1662] testing these multiple models we can get
[1665] some interesting theoretical insights as
[1667] well
[1670] i'll then scale this up to natural
[1672] images using these small images of the
[1675] sephora 10
[1676] image set
[1678] so now we're going to look at a pair of
[1681] categories rather than a pair of models
[1684] and at all of the different models
[1687] so let's start with with one example
[1690] here is a particular stimulus
[1693] stimulus that was optimized to look like
[1696] a horse to the graff wall joint energy
[1699] model which is a hybrid generative and
[1701] discriminative model
[1703] and at the same time the stimulus was
[1705] optimized to look like a cat to the one
[1708] pcn a6 model
[1712] to me this looks more like a horse so i
[1714] would say my perception agrees better
[1716] with the graphical joint energy model in
[1718] this case
[1720] but let's look at more of the stimuli
[1723] let's let's
[1724] start in the the upper left and look
[1727] at these three models um
[1730] um
[1731] at the top there
[1733] so for these models this the
[1736] controversial stimuli we get are these
[1738] rubbish images
[1739] and these meet the high standard for
[1742] controversiality so for each of these
[1744] one of the models is very sure that it's
[1746] a horse and not a cat and the other
[1748] model is very sure that it's a cat and
[1750] not a horse so this provides pretty
[1752] strong evidence against both of the
[1754] models and actually these stimuli are a
[1757] special case of controversial stimuli uh
[1760] which are adversarial stimuli and tal is
[1763] going to tell you much more about how
[1766] adversarial stimuli relate to
[1769] controversial stimuli but
[1771] the the short version is that
[1774] adversarial stimuli are a special case
[1776] of controversial stimuli where the
[1779] stimuli are controversial controversial
[1782] between
[1783] a model and some oracle that tells us
[1786] the ground truth label
[1790] when we look at the angstrom l infinity
[1793] model we see that these stimuli
[1795] perhaps look a little bit more cat-like
[1798] so that model i would say from just
[1800] eyeballing this seems to dominate the
[1803] first three models and when we look at
[1806] the ones
[1807] optimized to look like a horse to
[1809] angstrom they they also look more like
[1811] forces when the angstrom l infinity is
[1814] pitted against the first three three
[1816] models so this seems to be a somewhat
[1818] better model and then when we look at
[1820] the angstrom l2 model
[1822] that in turn seems to dominate not just
[1825] the first three models but also the l
[1828] infinity model again we're seeing sort
[1830] of cats along the vertical here and
[1834] perhaps forces i mean this is highly
[1836] subjective right don't believe me um
[1839] draw your own conclusions or wait for
[1841] the
[1842] psychophysical results which will be in
[1844] the next slide
[1846] and then
[1847] remember the calcium kde model performed
[1849] very well on the mnist data set and it's
[1852] a very simple
[1854] example of the generative model so when
[1856] we used it on this slightly in the
[1858] slightly more complex scenario here on
[1860] natural images and the gaussian kde
[1863] model failed really badly so
[1866] this does worse definitely than the
[1870] angstrom model
[1874] and
[1875] not even even better than the
[1878] not even clearly better than the
[1880] initial three models
[1882] and then when we looked at the graph
[1884] world joint energy model we found that
[1886] this one um
[1887] seemed to to dominate all the other
[1889] models and you can
[1891] intuitively um
[1893] appreciate that from looking just at
[1895] this one uh pair of categories horse and
[1899] cat here where along the the lower row
[1902] you see
[1904] most of us see see horses and along the
[1907] right column most of us see cats
[1912] so when tell did the psychophysical
[1914] experiment
[1915] these were the results again the most
[1917] striking feature is this big gap between
[1920] all of the models and the noise ceiling
[1922] so this indicates that all of the models
[1925] as usual are incorrect
[1928] but there are significant differences
[1930] between the models and the best model
[1933] was the graph wall joint energy model
[1935] the hybrid generative and discriminative
[1938] model which significantly dominated all
[1940] the other models you can also see the
[1942] failure of the gaussian kde model here
[1948] cal then scaled this up to natural
[1951] images larger natural image images from
[1954] the imagenet data set
[1957] and
[1958] here now since we're dealing with with
[1960] bigger images and bigger models and more
[1963] parameters we're limited to models that
[1966] are differentiable so we can't uh have
[1969] models where the optimization procedure
[1972] needs to be gradient free we need
[1974] gradients to do the optimization so
[1977] we're somewhat more limited in the
[1978] models that we can explore so far but
[1981] here are four
[1983] models to make a start on that
[1986] so when tal pitted the inception v3
[1988] model against the resnap 50
[1990] he got these kind of
[1992] interesting looking
[1995] rubbish images providing evidence
[1997] against both of these models
[2000] and then when he pitted these
[2001] adversarially trained
[2004] models
[2005] of two different architectures resnet
[2007] and wrn
[2009] against these first two models
[2012] and you got these results
[2014] so these results
[2016] are somewhat consistent with the
[2018] category
[2020] these images have been optimized to look
[2022] like to the adversarially trained models
[2024] the ymirana
[2026] dog category
[2028] so this seems to be looking
[2031] somewhat encouraging for the
[2032] adversarially trained models
[2035] and when we um
[2037] we then looked at
[2039] the
[2040] opposing quadrant where the stimuli were
[2042] optimized to look like persian cats the
[2045] adversarially
[2047] trained models and like why morana dogs
[2049] to the first two models and that you get
[2052] these textures um that perhaps are a
[2056] little more consistent in my subjective
[2058] perception with the fur of cats than
[2061] with
[2063] the shape and fur of by marana
[2066] dogs
[2067] so this would seem to provide some
[2069] evidence in favor of these adversarially
[2072] trained models over the first two models
[2074] at least
[2075] however when tell
[2077] contrasted the the two adversarially
[2080] trained models he got these monster
[2082] looking images that don't really have
[2085] any
[2086] any clear classification
[2088] and um this uh suggests to us that um
[2092] these adversarially trained models also
[2095] do not really account for um human
[2097] perception so we still have some way to
[2100] go but we have a little bit of a hint
[2102] which directions and model space might
[2105] be
[2106] good to move in
[2109] and more recently we took this to the
[2111] language domain so this is a
[2113] collaboration with christoph about
[2114] baldesano's lab tar worked together with
[2118] matthew siegelmann
[2120] a phd student in chris's lab to take
[2123] controversial stimuli to the language
[2126] domain and
[2127] tell and matt tested a variety of
[2130] language models
[2131] they fell into three categories n-gram
[2134] models two gram and three gram models
[2136] which use text corpus frequencies of
[2139] unique phrases of length n to make
[2142] predictions about the probability of the
[2144] upcoming word and this can then be
[2147] extended to making predictions about the
[2149] probability of entire sentences
[2152] they also use classical neural network
[2155] models so these are recurrent neural
[2156] nets
[2157] using fixed token embeddings
[2160] and they used
[2162] some of these more modern transformer
[2164] neural network models which are neural
[2166] nets that use context dependent
[2168] embeddings and multiple attention heads
[2170] and there were five different models in
[2172] this class including
[2174] bert and roberta and gpt2 and a couple
[2177] of others
[2181] so to get an intuition on how they made
[2184] these controversial sentences let's
[2186] imagine the space of all sentences which
[2189] of course is a discrete space as a
[2191] continuous space just to get some some
[2193] intuition
[2195] so each of the models
[2197] assigns a probability to each possible
[2201] sentence so here i'm drawing
[2203] one probability distribution over
[2205] sentence space
[2207] and i'm associating that with the bird
[2209] model
[2211] so here the high probability sentences
[2213] here are the low probability
[2214] sentences
[2217] if we look at another model let's say
[2219] gpt2 we get a different distribution
[2223] there is some region of agreement here
[2226] in the lower region here both models
[2229] agree that the sentence is likely in the
[2231] upper region there both models agree
[2233] that the sentence is unlikely
[2235] and in in the other regions here outside
[2238] this agreement region
[2240] we have the controversial sentences
[2242] right so these controversial regions of
[2245] sentence space are the regions that are
[2248] useful to us as scientists adjudicate
[2251] among them
[2255] the distribution of sentences that are
[2258] considered likely by humans tends to
[2260] fall somewhere here where um when
[2263] several models agree that the sentence
[2265] is likely then often humans also think
[2267] it's likely but there are some uh
[2269] sentences that are likely according to
[2272] humans that some of the models think are
[2274] very unlikely
[2277] so that's where the models fail to
[2279] capture
[2280] the
[2282] the likeliness of different sentences in
[2284] english
[2290] so
[2291] tell and matt and chris wanted to anchor
[2295] the generation of these controversial
[2297] stimuli in
[2299] the
[2300] high probability natural sentences so
[2302] they started with a natural sentence in
[2305] each case and calling that n here
[2307] and then they optimized that sentence by
[2311] changing one word at a time
[2314] according to
[2316] an objective function where they
[2318] minimize the probability of the sentence
[2320] according to gpd2 for example
[2323] under the constraint that the
[2325] probability according to birds stayed at
[2328] least the same
[2330] so
[2331] for bird we stay in this plateau of high
[2334] probability here the blue region
[2337] but for gpt2 we go down onto a low
[2340] probability region
[2342] and that's the optimized synthetic
[2345] sentence one
[2347] and then we can also make a synthetic
[2349] sentence two where we flip the two
[2352] models and we minimize the probability
[2355] of the sentence according to bird
[2358] while keeping the probability according
[2360] to gpg2 at least the same so now we're
[2363] staying on the green plateau associated
[2365] with the gt2 model
[2369] so here's some examples of these these
[2371] sentences it's really quite intriguing
[2373] so they started in this case with the
[2375] sentence this is the lie you have been
[2378] sold so that's a natural sentence that
[2381] they just found in corpus of sentences
[2384] and then they optimized it to be
[2387] unlikely
[2388] in the eyes of gpg2 and still
[2391] equally likely at least
[2394] in the eyes of birth and they got the
[2395] sentence this is the week you have been
[2398] dying
[2400] so not that this is a perfectly
[2402] grammatical sentence
[2404] however
[2406] it is an unlikely sentence because of
[2408] its meaning
[2411] and when they did the opposite and
[2414] minimized the probability according to
[2416] bert while maintaining the high
[2417] probability according to gpt 2 they got
[2420] this sentence
[2422] that is the narrative we have been
[2424] solved
[2425] so this is a perfectly grammatical
[2428] sentence and quite a likely sentence
[2430] it's probably been uttered
[2432] many times
[2435] so in this case
[2437] it looks as though the
[2440] probability distribution that determines
[2442] human
[2443] perception
[2445] of how likely different sentences are
[2448] at least in this one example appears to
[2450] be better aligned with gpg2 in fact when
[2454] subjects were asked whether
[2456] synthetic sentence 1 or synthetic
[2458] sentence 2 is more likely 10 out of 10
[2461] subjects
[2462] found synthetic sentence 2 more likely
[2466] so
[2467] these kinds of sentences were were
[2469] generated and many of them and we
[2472] performed an
[2473] experiment in 10 sets of uh
[2476] 10 subjects each so 100 subjects in
[2479] total with sort of the separate
[2481] replications of the experiment and
[2484] embedded in it
[2485] and the subjects were presented uh with
[2488] this question for each of the pairs of
[2491] sentences which sentence is more likely
[2493] to be encountered
[2495] so in this case it would be these two
[2498] synthetic sentences that is the
[2500] narrative we have been sold and this is
[2502] the week you have been dying and all 10
[2504] out of 10 subjects
[2506] pick the one on the left and we also got
[2509] some confidence information there but
[2512] i'm not gonna be showing you results
[2514] that use this information so it's at the
[2516] moment it's just about deciding which
[2518] one is relatively likely
[2522] so when analyzing the results here
[2525] when we look at random natural sentences
[2527] which are also included in the
[2529] experiment for comparison
[2531] we find that
[2533] all the models are relatively close to
[2536] noise ceiling and not significantly
[2538] below the noise ceiling so you could say
[2540] oh great news um we can completely
[2543] explain our data however um that's true
[2546] for all of the models and just reflects
[2548] the relatively low power here
[2553] so in these
[2555] results graphs that i'm showing you uh
[2558] this dashed line is chance performance
[2560] because it's about pairs of sentences so
[2562] it's about making a binary decision each
[2564] dot here is one replication of the
[2567] experiment there are 10 replications in
[2570] each replication there are 10 new
[2572] subjects and a totally new set of of
[2575] stimuli so different pairs of sentences
[2578] so when we treat this uh replication as
[2581] a random effect we can do inference that
[2584] generalizes the to the population of
[2586] subjects and also to the population
[2590] of sentence
[2591] pairs
[2592] and here in grey as as always is the
[2595] noise ceiling for comparison so in this
[2597] case none of the models were
[2599] significantly different from any other
[2601] models and none of the models were
[2604] could be rejected based on the data they
[2607] all
[2608] were
[2609] within the range of the the lower bound
[2611] of the noise here
[2613] we used controversial sentences we saw a
[2616] much more interesting picture where the
[2619] range of performance of the different
[2620] models is much wider so now we see that
[2623] several of the models can be rejected
[2625] they're significantly below the lower
[2627] bound of the noise ceiling indicated by
[2630] the black star here
[2633] and also when we did the pairwise model
[2635] comparisons we now saw that gtg2 for
[2638] example dominated all the models except
[2640] roberta in this example and there are
[2642] many other significant
[2645] model
[2646] comparison
[2647] results
[2649] so this particular
[2651] analysis is based on natural sentences
[2654] that were selected to be controversial
[2656] so this is not the synthetic sentences
[2659] that i illustrated for you before when
[2661] they used these synthetic sentences
[2664] results were even more uh striking with
[2666] a much stronger contrast between the
[2670] performance of the different models
[2672] some of the very simple models are
[2674] driven below chance performance here and
[2677] that's because they're pitted against
[2678] better models and these are binary
[2680] decisions and the better models so to
[2683] speak trick them into
[2686] making a performing below low chance
[2688] level and in this case we can reject
[2692] both most of the models on the basis of
[2694] the data and we also get
[2696] a lot of significant pairwise model
[2698] comparisons
[2700] you can also pull all the data together
[2702] so this gives kind of like an overall
[2705] summary of this experiment so it
[2706] includes all the trials that i've shown
[2708] you before
[2710] and additionally the trials where one of
[2712] the sentences was natural and the other
[2715] sentence was
[2717] synthetic and when we look at this we
[2720] have enough power to reject all of the
[2722] models
[2723] and we find many pairwise comparisons
[2726] significant giving some indication about
[2729] which
[2730] of these modeling developments might be
[2732] on the right track in one way or another
[2735] but the
[2737] gpt-2 model although it dominated most
[2740] of the other models did not
[2742] significantly dominate the roberto mall
[2745] so
[2746] conclusions on the controversial
[2749] sentences human behavioral experiments
[2752] with random natural sentences
[2754] render it difficult to distinguish
[2756] models and detect shortcomings of the
[2759] best models
[2761] controversial sentences whether natural
[2763] or synthetic reveal the shortcomings
[2767] of all of the models and provides
[2769] starker contrasts among the models
[2773] so um zooming out and moving toward the
[2777] conclusion
[2778] there's a historical
[2780] debate about whether to use artificial
[2783] stimuli or natural stimuli artificial
[2785] stimuli
[2786] are
[2788] controlled they're often designed to
[2790] adjudicate between models we have and
[2792] they're often
[2793] simpler historically natural stimuli are
[2796] less controlled they're more
[2797] ecologically valid they enable us to
[2800] test
[2801] models under the conditions
[2804] under which
[2805] our brains function in real life and
[2807] they're often more complex
[2809] there's a long-standing debate
[2813] between these two extremes we can think
[2815] of controversial stimuli as a kind of
[2818] synthesis
[2819] of these
[2820] these two extreme perspectives where you
[2822] get uh some of the benefits of each of
[2825] them so you can have a stimuli that are
[2828] complex that
[2830] have some
[2831] clearly
[2832] natural content in them as uh is
[2836] reflective of knowledge that the models
[2839] have learned about what things look like
[2841] in the world
[2842] but they are also designed to adjudicate
[2846] between models so they give us a lot of
[2848] power to make theoretical progress
[2852] despite our excitement about
[2853] controversial stimuli
[2855] i want to stress that model independent
[2858] natural stimuli
[2860] remain essential for
[2862] neuroscience and remain very important
[2864] also
[2865] in our lab so we're not about to just
[2868] stop using natural
[2870] stimuli we should always have them in
[2872] our experiments and we should
[2875] anchor our analyses in natural stimuli
[2878] but then also venture out into
[2880] controversial regions of stimulus space
[2883] in order to more strongly test on the
[2887] inductive biases of different models
[2890] so natural stimuli and provide a general
[2892] purpose tool for testing models with big
[2895] data sets
[2896] there's no need to know the models in
[2898] advance that's a big advantage of
[2901] natural stimuli
[2903] and they're ecologically
[2905] valid
[2907] i'm particularly excited about this
[2909] project
[2911] spearheaded by thomas marcellaris and
[2913] kendrick k where they acquired this
[2915] massive seven tesla data set with a big
[2918] set of natural stimuli and we're excited
[2921] about starting to to analyze this data
[2923] set
[2924] because it's really a very rich
[2927] resource very useful
[2931] so in conclusion a controversial stimuli
[2934] provide optimized probes for
[2937] adjudicating among computational
[2939] hypotheses
[2941] controversial stimuli reveal distinct
[2943] inductive biases of different deep map
[2946] models
[2947] human vision may rely on a computational
[2950] mechanism that combines elements of
[2952] discriminative and generative inference
[2955] and current language models differ in
[2958] their ability to recognize high
[2959] probability english sentences but none
[2962] of them can fully account for human
[2964] judgments of the relative likeliness of
[2967] different sentences
[2969] thank you very much
[2975] thank you nika that was a fantastic talk
[2978] um i we have some time for questions so
[2981] i think how the best way to do this is
[2983] to have people either chat their
[2985] questions if they prefer and i can read
[2986] them
[2987] or if you would like to raise your hand
[2989] and ask the question directly
[2992] i can unmute you
[2994] and so while we're waiting maybe i'll
[2996] ask my question first which was um
[2999] about how to interpret when you would
[3001] pick two models against each other and
[3002] the results look nonsensical
[3006] i think you were referring to those as
[3009] that as evidence of both models being
[3011] bad but i could also see a scenario
[3013] in which for example if you ask two
[3015] humans to come up with a controversial
[3017] stimulus it would probably look
[3019] like neither of the two categories right
[3021] so how can you distinguish between if
[3023] the models are equally good versus
[3025] equally bad
[3028] yeah that's a that's a great point um so
[3031] it could be that we can make
[3032] controversial stimuli also for pairs of
[3036] people right so it could be that it's
[3038] possible for example through very
[3039] extensive
[3041] psychophysics to make some weird
[3043] stimulus
[3044] where you show it to me and i say well
[3046] clearly that's a face and you wouldn't
[3049] have any idea you would see think it's
[3051] something completely different and that
[3053] would highlight differences between our
[3055] brains and i think it's an
[3057] incredibly exciting avenue to go in
[3061] in terms of
[3062] testing models
[3065] this is opening
[3067] a big can of worms and a and very
[3069] important challenge which is that our
[3073] models are also idiosyncratic like
[3075] individuals so every
[3077] every architecture when trained on a
[3079] given
[3080] training
[3081] data set
[3083] when it's trained from a different seed
[3085] and or it's trained with a different um
[3088] sample of stimuli from the same
[3090] distribution even gives you a totally
[3092] different uh trained neural net right
[3095] and so in subtle ways um different
[3097] instances of the same model behave
[3099] differently and it's very important to
[3102] check when you make
[3104] an adversarial stimulus or
[3107] a controversial stimulus whether that
[3109] stimulus generalizes to new samples from
[3112] the same distribution of models right
[3115] there's work from tim kitzman's lab that
[3118] has looked at
[3120] the individual differences among deep
[3122] neural networks and that's sort of
[3125] a step in that direction tell us also
[3127] thinking about this very deeply how we
[3129] can
[3130] integrate
[3132] distributions of instances of each of
[3136] the
[3136] models
[3137] into our inference framework um but
[3140] that's um yeah
[3142] quite a
[3143] quite a new direction that yeah we don't
[3146] have definitive results on yet
[3150] thanks elena did you want to ask your
[3152] question or do you want me to read it
[3155] i can read it um
[3157] yeah so my question is uh
[3160] could you speak more about the inductive
[3162] biases that these models have
[3165] so like uh in convolutional neural
[3168] networks one the big inductive bias that
[3171] everyone says it has is the translation
[3174] and variance bias
[3176] um is there some sort of like in what
[3179] we've you've seen in these models
[3182] using these controversial stimuli can
[3185] you
[3185] summarize
[3187] is it possible to summarize the
[3188] inductive biases in the same way
[3192] or yeah so they share the inductive
[3195] biases of deep convolutional
[3197] feed-forward networks so one of them is
[3200] translation invariants or translation
[3203] equivalents that the same features are
[3205] detected automatically all over the
[3207] image and that is is one very important
[3210] inductive bias
[3211] but some of them
[3213] have
[3214] an additional inductive bias which is
[3216] that it helps to form a complete
[3220] mental model of each of the classes that
[3223] you're you're trying to discriminate
[3225] right so the the winning model um in the
[3228] amnest example was the shot analysis by
[3231] synthesis model and this really learns a
[3233] generative model of digits so from this
[3235] model you can generate digits and they
[3237] look uh like natural digits and it uses
[3241] this generative
[3243] power in order to infer what a given
[3245] digit is right so this speaks to
[3249] this ongoing uh debate of perspectives
[3251] between um
[3253] the
[3254] feed-forward and discriminative approach
[3257] to vision which uh is very influential
[3260] in visual computational neuroscience and
[3262] also very influential in computer vision
[3264] and it's the approach that actually has
[3267] made it into our cell phones so in that
[3269] sense it's been much more practically
[3271] successful
[3273] and the the generative perspective on it
[3275] which is provides a very different
[3277] inductive bias
[3279] and
[3280] a more
[3281] normatively motivated approach to doing
[3284] vision
[3285] so the way the way you should do it from
[3287] from a bayesian perspective where you
[3290] make your prior knowledge explicit and
[3293] then you interpret the image as evidence
[3296] in the light of what you know about what
[3298] the whole distribution of
[3301] of images is for each of the the digit
[3303] classes of the categories right so this
[3306] is the biggest distinction between these
[3309] different models uh in terms of their
[3311] inductive biases and
[3314] a tentative result from this analysis is
[3316] that the generative inductive bias in
[3319] some form is important for explaining
[3322] human perception
[3326] thank you i i do have a another question
[3329] maybe not a follow-up but a different
[3331] one
[3333] so
[3334] it has to do with uh the idea of
[3336] confounding so
[3338] uh could you speak a bit more on like uh
[3342] how
[3343] uh
[3344] different models who perform very
[3346] similarly like what exactly is that
[3348] confounding
[3350] uh that
[3351] you were
[3352] using to explain
[3354] why they
[3356] perform so similarly
[3358] yeah um so i mean think of
[3362] cats and dogs right so let's say you
[3364] want to
[3365] learn to distinguish
[3367] cats and dogs they differ in many ways
[3370] right you could recognize them by the
[3372] ears or you could recognize them by the
[3374] mouths
[3375] and if you have two models and one uses
[3377] the ears and the other uses the mouths
[3380] and you only
[3381] test on natural images of cats and dogs
[3384] then both of these models are going to
[3385] be perfectly able to do this if they're
[3388] big enough you know to really be good at
[3390] recognizing dog mouths and cat mouths
[3393] and knowing the difference between them
[3395] and so then in the at the level of their
[3397] behavior these models wouldn't differ
[3399] but at the level of their mechanism they
[3402] do differ a lot right and when we when
[3405] we deal with other people let's say we
[3407] talk to our children or we we teach
[3410] students we make these inferences about
[3412] what is actually going on in their minds
[3414] right how are they making these
[3416] inferences and that would be different
[3418] in these these two models um despite the
[3420] fact that they perfectly well can
[3423] discriminate um cats and dogs so in this
[3426] case by making controversial stimuli
[3429] you'd end up making stimuli that that
[3432] changed the features of the mouths and
[3435] and ears and you could see from just
[3437] eyeballing the stimuli
[3440] which
[3441] set of features drives the responses in
[3443] each of these models and then you could
[3445] tell the difference between them and you
[3447] could also
[3449] compare them to humans and find out
[3450] whether humans rely more on the
[3453] ears or the mouths
[3458] thank you
[3462] i have more questions but
[3465] i want to i can take them offline
[3469] i mean we are running um
[3471] we are at 10 o'clock right so it's also
[3474] time for for tel's talk yep i think
[3476] we're right on time which is great so
[3478] thank you again nico for a fantastic
[3480] talk
[3480] thank you
[3481] i'm going to propose that before tell um
[3484] tell us talk we take a five-minute break
[3487] um and so we'll we'll meet back here at
[3489] let's say 1005
[3491] uh or every we'll
[3494] resume at 105.
[3797] um
[3798] so tall whenever you're ready we can
[3801] i'll stop sharing
[3803] and
[3805] i've changed it so that others can share
[3807] screen in case they have questions
[3808] during the tutorial um
[3812] during your talk portion would i was
[3814] going to keep everyone muted and monitor
[3817] the raised hands and chat does that
[3819] sound
[3820] good
[3823] okay so we're going to resume again with
[3825] um the tutorial portion from talgolan um
[3828] so i'm really looking forward to hearing
[3830] more about this exciting work from the
[3833] from a hands-on perspective um
[3837] i am going to
[3839] i think the best way to ask questions
[3841] during the the first portion of the
[3842] tutorial is to either type them in the
[3845] chat and i'll monitor that and ask tall
[3848] or
[3849] if you'd like to raise your hand i can
[3851] unmute you and you can ask it directly
[3868] okay
[3875] hi so this tutorial will have three
[3877] parts
[3878] in the first part i will give
[3881] an overview on both practical and
[3883] theoretical considerations
[3885] related to synthesizing controversial
[3887] stimuli
[3889] i will begin from the basic optimization
[3892] loop for creating controversial stimuli
[3894] then
[3895] i will compare controversial stimuli to
[3898] alternative approaches
[3900] next i will briefly discuss the results
[3903] from generalizing this method to
[3905] imagenet
[3906] and last we will discuss
[3910] ways of restricting the stimulus space
[3912] in which we search for controversial
[3914] stimuli
[3916] then we'll have time for some more
[3918] questions and discussion
[3920] and for those that will choose to stick
[3922] with us to the end we'll have about one
[3924] hour of hands-on high torch
[3928] implementation exercise
[3931] okay so let's begin with a basic
[3934] optimization loop
[3937] so we start from stimulus x
[3940] and i would strongly argue to use
[3943] a random noise image as the initial
[3946] image
[3947] so
[3948] any structure that will emerge
[3952] in that image in the stimulus will
[3954] emerge due to the models and not due to
[3956] our initialization
[3958] so now we take the stimulus and we feed
[3960] it into two neural networks model a and
[3963] model b
[3965] and we collect their outputs which we
[3967] interpret as predictions about human
[3970] responses
[3971] we calculate a controversiality score
[3974] which is a function that should be high
[3976] with the two models
[3978] disagree
[3979] for example if these are two
[3981] object classifiers if they see
[3984] distinct categories with high confidence
[3986] then the controversiality score should
[3988] be high and as nico mentioned in our you
[3992] know studies we use the heuristic
[3994] approach in which we chose
[3996] two categories at a time and calculated
[3999] this controversiality score within
[4001] respect to
[4002] these categories
[4004] so once we have this score we can use
[4008] an optimization algorithm to change
[4012] the pixels of the stimulus to increase
[4014] its controversiality
[4019] we run this loop
[4021] until we cannot make further
[4023] improvements
[4024] and then we have our controversial
[4026] stimulus
[4027] we produce many controversial stimuli
[4031] and then we
[4034] present this stimuli to human subjects
[4036] in a formal behavioral experiment in
[4039] which we compare between
[4042] the judgments of the subjects
[4044] and the predictions
[4046] of
[4046] the models and we are now guaranteed
[4050] that for a given stimulus in a given
[4052] subject the subject will not be able to
[4055] agree with both models as often happens
[4058] with natural images
[4062] if the models are
[4064] differentiable and this is usually the
[4065] case
[4066] then we can calculate the gradient of
[4069] the controversiality score with respect
[4072] to the pixels of the stimulus here this
[4076] is just the set of partial derivatives
[4080] of the score
[4081] with respect to each pixel
[4083] and if we have that we can feed this
[4086] gradient into a stochastic gradient
[4088] descent algorithm like adam and this is
[4090] a very fast and efficient way of
[4093] creating controversial stimuli it takes
[4096] less than a few minutes per image
[4103] i'm now going to make a couple of
[4105] practical technical points before we
[4108] shift gears and discuss
[4110] more theoretical considerations
[4113] so one practical point is about
[4116] stimulus preprocessing usually these
[4118] networks are trained not on raw images
[4122] but on images that were pre-processed so
[4125] this pre-processing usually includes
[4127] centering and scaling of the
[4130] rgb values
[4132] resizing the image to a certain size and
[4134] even sometimes changing the order of the
[4137] color channels
[4140] often
[4141] this pre-processing is not part of the
[4145] object that describes the model
[4148] it's somewhere in the training and
[4149] evaluation code
[4151] and
[4153] different models might be trained using
[4155] different conventions of pre-processing
[4158] so it's really important to get this
[4159] right to feed each model with the images
[4162] pre-processed as it was
[4165] trained
[4166] i found that the best way to ensure that
[4169] is to encapsulate
[4171] each model
[4172] along with its pre-processing in a
[4174] python class so we form for each model a
[4177] class that
[4179] receives raw images as inputs
[4183] and generates the outputs that we'd like
[4186] to test
[4187] if you're using pytorch then you can
[4189] [Music]
[4190] make this class a child
[4193] class of torch nm module sorry if you're
[4196] using pi torch
[4199] um
[4201] okay so
[4202] that's that and one more practical
[4205] consideration
[4207] images have
[4209] limited intensity range
[4212] so
[4213] if we are using floating point
[4214] representation
[4216] then
[4216] the pixels should have intensity values
[4219] between zero to one if we just run some
[4221] optimization algorithm they might run
[4223] beyond these limits
[4226] i found that the best way to ensure that
[4228] we respect this constraint is by
[4231] re-parameterizing the stimulus so
[4234] instead of optimizing directly the
[4236] stimulus we are optimizing a tensor z
[4238] which has the same shape as the stimulus
[4242] x but its values are allowed to run
[4245] between minus infinity and infinity and
[4248] we use the sigmoid function to compress
[4250] z
[4250] into
[4252] a valid image x and now we optimize z
[4255] and once we are done we are taking x as
[4258] our resulting image
[4260] and
[4261] we will see later that this concept of
[4264] reparameterizing this the stimulus is
[4267] useful for also
[4269] more sophisticated
[4271] tasks
[4274] okay so
[4275] how can i ask you a quick question sure
[4277] can you give an intuitive explanation
[4279] about why that reparameterization helps
[4285] so in this particular case
[4287] um
[4289] z can be can have any value that
[4292] it will get so
[4294] up to infinity
[4295] and once you apply the sigmoid
[4299] all of these values are mapped to this
[4301] zero to one
[4302] bond
[4304] so it makes the optimization easier to
[4307] have
[4308] so now you can run optimization without
[4311] any constraint you don't need to run
[4313] constraint optimization that has its
[4315] issues
[4317] thanks so much this is a common trick uh
[4320] common approach to
[4322] constraint optimization by ripa and try
[4324] re-parameterizing the variables so
[4327] the new problem is unconstrained
[4336] i i should say that i welcome questions
[4339] and you can also use the chat
[4342] when go graduate student in our lab is
[4344] monitoring that and she
[4346] will be able to answer even while i
[4348] speak
[4353] okay
[4355] so now once we
[4358] cleared
[4359] the table we can discuss some more some
[4362] more theoretical
[4364] considerations so i'm going to compare
[4366] controversial stimuli to alternative
[4369] approaches so one alternative approach
[4372] would be to have a human in the loop
[4375] so
[4376] in principle we can have the person here
[4379] inside the optimization group
[4381] and
[4382] optimize it stimuli that will cause
[4385] disagreement between
[4387] the model and the human observer
[4392] i think that this is a very attractive
[4394] idea but it's very inefficient it's very
[4397] difficult at the moment
[4399] our speed of evaluating human subjects
[4402] is several orders of magnitude slower
[4405] than
[4406] how we can evaluate
[4408] neural networks
[4409] and
[4411] we also don't have gradients from human
[4414] subjects
[4415] so this is attractive but inefficient
[4420] i'm quite sure that in the future this
[4421] will be done
[4425] a different approach which is
[4427] widely utilized and obviously predates
[4430] hours
[4431] is other cell examples
[4433] so when we create other cell examples we
[4436] are optimizing images or other stimuli
[4439] so they cause an incorrect
[4442] prediction in our targeted model
[4446] in an ideal setting we have access to
[4449] some kind of ground truth oracle
[4453] and
[4454] then we can if we have that we can
[4456] directly optimize
[4458] stimuli that are in that are guaranteed
[4461] to reduce an error in the model
[4466] this might apply for example if we have
[4468] some kind of simulated environment
[4472] in general settings we don't have
[4475] a ground truth oracle or it might be
[4477] expensive to evaluate
[4480] so we almost always use a ground truth
[4484] stand-in when we create other cell
[4487] examples some simple heuristic
[4489] that replace replaces
[4491] that ground truth
[4493] and the most common
[4496] branch of selling that we have
[4499] is the
[4501] epsilon robustness notion
[4504] so the idea is that we consider
[4506] a natural image along with its human
[4510] driven label
[4512] and we make the assumption that within a
[4515] certain wall of radius epsilon
[4518] a ball in image space
[4521] the
[4522] correct label
[4523] doesn't change
[4524] so if we apply perturbation whose
[4527] magnitude is
[4528] lesser or equal to epsilon the model
[4530] should keep its original classification
[4535] so
[4537] we use this um
[4539] we use this heuristic
[4541] and now we we don't know anything about
[4543] we don't make any assumption about
[4546] the responses the ground truth outside
[4548] the ball so we just search within the
[4550] ball
[4550] for images for which the model disagree
[4554] with this ground truth standing
[4557] if we cannot do that if we run this
[4560] optimization and we cannot find
[4562] images that cause this
[4565] kind of disagreement then we would say
[4567] that this model is epsilon robust
[4571] so that's not this is an informal
[4573] definition of epsilon robustness so an
[4575] epsilon robust model
[4578] will not change its classification often
[4580] clean image
[4582] for perturbations or less of magnitude
[4584] lesser or equal to epsilon and here you
[4587] can see a typical way of how this is
[4590] quantified so the x axis is the size the
[4594] magnitude of the perturbation and the
[4596] y-axis is the model's accuracy and if we
[4599] have a model which is more robust in
[4601] this epsilon robustness sense then its
[4603] accuracy curve will go down more slowly
[4607] and this model depicted here is actually
[4609] quite robust this is another acidic
[4611] trained model if you'll take a standard
[4614] discriminative
[4615] object classifier
[4617] its accuracy will drop to zero at the
[4619] moment that you will start introducing
[4621] other cell
[4622] adversarial perturbations even if these
[4625] adverse perturbations are
[4626] very small
[4629] from the perspective of
[4631] cognitive computational neuroscience
[4634] this is interesting but it it's not
[4636] exactly the thing that we are after
[4639] um because
[4641] absent robustness and model human
[4644] alignment
[4645] are not the same thing
[4647] these are related ideas so if you have a
[4650] model which is very non-robust in this
[4652] epson robustness sense if it completely
[4654] changes its predictions in response to
[4656] tiny perturbations that humans cannot
[4658] see then it cannot be
[4660] human aligned
[4661] but if we develop models that are more
[4664] and more
[4666] robust in the epson robustness sense
[4667] these models will not necessarily become
[4669] human aligned
[4671] and the reason for that is that
[4673] these perturbations that are
[4676] measured in image space so these
[4678] distances are
[4680] almost unrelated to perceptual distances
[4685] so
[4686] we can still use adversarial examples i
[4688] think that it's critical to
[4690] add
[4691] the behavioral
[4693] evaluation of the images if we want to
[4696] draw more scientific insights there are
[4698] already a couple of papers a couple of
[4701] studies that are starting to do that
[4703] but there's one more disadvantage to
[4705] using other cell examples which is that
[4708] this heuristic this ground truth
[4710] standing
[4711] is
[4712] quite
[4713] simplistic
[4716] if we use another
[4719] model in your network model as a branch
[4722] of setting
[4723] we might challenge
[4725] the first model in a more severe way
[4728] exposing new failure modes that we can't
[4731] see when we just use
[4733] the epsilon
[4735] epsilon ball assumption
[4737] and now we also can search over the
[4740] entire stimulus space we don't need to
[4742] limit ourselves to the vicinity of a
[4745] clean
[4747] image this is why we say that
[4750] other cell examples are a special case
[4753] of controversial stimuli
[4758] okay
[4759] the next point
[4760] will be about
[4762] our results from generalizing to
[4763] imagenet
[4764] so
[4765] you've already seen
[4767] this matrix but i'd like to make a
[4769] couple of more points
[4771] so
[4772] here we created
[4775] stimuli that
[4777] caused one model to detect a persian cat
[4780] and another model to detect one lame
[4782] runner dog so for example this image is
[4785] classified as a persian cat by residence
[4787] 50 and as a wave runner dog
[4790] by inception
[4793] once we
[4795] use
[4796] other 30 trained networks
[4798] and we pair them with standard networks
[4801] then we get something which is not
[4803] really persian cat-like but
[4806] we can identify some features and maybe
[4808] with forced choice behavioral evaluation
[4812] people will choose persian cat with high
[4814] probability
[4816] this is the converse example in which
[4819] the adversary trained model recognizes a
[4821] dog
[4822] the standard model recognizes a cat and
[4825] i can clearly see
[4827] this dog this dog's ear here and i
[4832] so
[4834] this phenomenology is not completely
[4836] surprising
[4838] these models come from the madrid lab
[4840] and they show in their studies that when
[4842] you run single model activation
[4843] maximization with adversaries trained
[4845] models you get images that are
[4849] human aligned to a certain degree
[4851] what's new and
[4853] is enabled by using controversial
[4855] stimuli is the direct comparison between
[4857] the two adversary trained models and
[4861] here we get these images that indicate
[4862] that none of these models are really
[4865] human aligned and you simply cannot see
[4868] that by just evaluating model through
[4870] the the lens of
[4872] epsilon robustness
[4875] we have some missing models here and
[4877] these models are
[4880] deep genitive
[4882] or hybrid discriminative generative
[4884] models
[4885] if we extrapolate from our mnist and
[4888] c410 results we expect that such models
[4892] deep generative or highly discriminative
[4894] genetic models
[4896] will dominate
[4897] this matrix in terms of model alignment
[4901] i i think that that's developing such
[4904] models that scale up to imagenet is an
[4906] important task
[4910] okay
[4912] we now got to the
[4914] last part of the overview
[4917] restricting is restricting the stimulus
[4919] space
[4921] so
[4922] ultimately we would like to predict
[4924] human responses for any images and for
[4927] that we need to develop stronger models
[4930] and essentially solve the problem
[4932] of other cell robustness in its
[4936] deeper sense of modern human alignment
[4939] but we can also make progress
[4942] even before we have these models
[4944] by
[4945] partitioning the similar space into
[4948] sub-regions
[4949] and working or comparing models within
[4952] these sub-regions
[4954] so we can think about
[4956] the
[4957] subspace or manifold of smooth images
[4961] 3d renderings
[4963] faces
[4965] natural images
[4966] and within each such manifold
[4970] we can search for controversial stimuli
[4972] and compare model with respect to how
[4974] well they predict human responses within
[4977] that manifold
[4981] there are very useful tools for
[4983] achieving this goal that we can borrow
[4985] from the literature of feature
[4987] visualization in which
[4990] researchers
[4991] intentionally want to create
[4993] interpretable
[4996] aesthetic images
[4997] that provide some kind of
[5001] insight about how this how the internal
[5004] representations of these models work
[5006] so
[5007] one mean is
[5009] high order stimulus parameterizations
[5011] and i will explain in a moment and the
[5013] other is expectation over noise
[5015] transformations
[5017] and both of these are implemented
[5019] in feature
[5020] visualization toolboxes
[5022] so we have the tensorflow package
[5025] lucid and there's a pi torch adaptation
[5028] for that called lucent and we will use
[5029] the pythagorean
[5031] in the hands-on tutorial
[5035] so let's begin with high-level stimulus
[5037] parameterizations
[5040] so we've previously seen that we can
[5041] optimize z instead of x and then
[5043] transform z
[5045] into an image
[5046] but this z doesn't have to be something
[5048] which is really image like it can be
[5051] some kind of
[5053] high level abstract representation
[5056] potentially a flow dimension
[5058] that we can
[5060] then convert
[5061] into an image
[5064] and if we have that then we can search
[5066] in that space of z
[5068] which
[5069] then spans
[5071] a smaller manifold or subspace
[5073] in image space
[5077] and doing this has two distinct effects
[5080] on
[5082] the search for stimuli
[5084] one obvious effect is imposing a prior
[5087] or a constraint
[5089] on the stimulus space
[5092] so a good example is using
[5094] again latent as a stimulus
[5096] parametrization so we take a trained cam
[5100] we throw the discriminator we don't need
[5102] it and now we use the input to the gan
[5105] as our stimulus parametrization
[5107] and the output of the
[5109] generator is
[5111] our st is our stimulus is our ex
[5115] and this approach was
[5117] utilized in a very powerful way for a
[5119] different aim finding
[5121] maximally exciting images
[5123] in this work from the livingston group
[5127] so let's see how this works in the
[5129] context of
[5131] controversial stimuli so now we see the
[5133] same
[5134] kind of procedure but with
[5137] this parameterization
[5139] and
[5140] we get some of different images
[5142] and now let's look at this image which
[5143] is
[5145] formed by contrasting the two standard
[5147] models which are not as aesthetic trends
[5149] and now this doesn't look like a noisy
[5151] image it requires psychophysical testing
[5153] but there are now some visible details
[5156] here
[5158] obviously this approach of using again
[5161] imposes a hard constraint on the
[5164] stimulus space and you can see that from
[5166] the dimensionality of the latent so if
[5169] the dimensionality of the latent is
[5170] smaller than the dimensionality of image
[5173] space then the gan can cannot
[5176] span the entire image space so we are
[5178] looking within a certain manifold
[5184] a second example
[5186] is the manifold of smooth images
[5188] and we can search within this manifold
[5191] using
[5192] comp
[5193] compositional pattern producing cp gains
[5197] so
[5197] these network these are neural networks
[5199] that convert transform
[5202] pixel coordinates
[5204] into color values
[5206] so they typically produce nice smooth
[5209] images and these images are controlled
[5212] by the weights of this network and we
[5214] can use the weights as our stimulus
[5216] primitization so
[5218] searching the space of weights that
[5220] produce
[5220] these synthetic images
[5223] and here you see the results for
[5226] the same controversial stimuli synthesis
[5228] procedure but now using this
[5230] parameterization
[5232] and
[5234] here although we eliminated
[5237] high frequency pattern
[5239] these two models are still somewhat
[5242] human misaligned for this image
[5245] here i actually recognize
[5248] the ear of of a wine runner this i would
[5251] choose wine runner if i was faced with
[5254] this image in a try
[5259] the other role that's using the stimulus
[5261] parameterization has
[5263] is to change the direction of the
[5264] gradients and since we are using local
[5266] search
[5268] that may change the local solution
[5270] solutions to which our optimization
[5272] procedure converges
[5275] so for example we can parameterize
[5279] the image by its complete complex
[5281] fourier coefficients
[5283] and scale these coefficients in inverse
[5285] proportion to their spatial frequency
[5288] this
[5289] method is taken from prisula's
[5292] paper in this steel
[5295] and by doing this we are slowing down
[5298] the gradient ascent in high frequencies
[5301] this is to me was a bit surprising but
[5304] gradient descent is not
[5307] invariant to linear
[5309] linear transformations of the optimized
[5312] variable
[5315] so let's see
[5316] what happens when we do this and i think
[5318] that this is the figure that nico had in
[5320] his presentation
[5323] and
[5324] now you can see that there's a certain
[5327] smoothness to these images which is
[5329] caused by
[5331] the optimization procedure
[5333] taking clogger making bloggers steps
[5336] in the low frequency range
[5339] sorry the low frequency range
[5344] and
[5346] yet
[5347] these are not really human
[5349] aligned this is
[5352] a weaker
[5353] way of regularizing
[5355] the similar space
[5357] because still at least in principle all
[5360] of the images are achievable we still
[5362] spend the entire image space but we bias
[5365] our research towards certain solutions
[5370] the other tool that we can use is adding
[5373] noise transformations
[5375] so
[5375] we generate our stimulus and then before
[5379] fitting it into the network
[5381] into the networks we
[5383] apply
[5384] some noise transformations like spatial
[5386] jitter which can be
[5388] thought as analogous to fixation jitter
[5393] slight rotation scaling
[5395] and we use
[5397] a differentiable implementation of these
[5399] transformations and then we can
[5402] optimize through these
[5404] noise transformations so in each
[5406] optimization iteration the noise
[5408] transformation is slightly different and
[5410] by doing that we achieve stimuli that
[5413] are
[5413] that the responses that they elicit in
[5415] the models are robust to these
[5417] transformations and this discourages the
[5419] optimization
[5421] from relying on high frequency
[5423] information that activate particular
[5425] pixels and through that particular units
[5428] in the network
[5430] and again this is implemented in the
[5432] feature visualization toolboxes
[5435] so we can think about
[5437] a continuum of ways of searching in
[5440] stimulus space that runs between less
[5443] restricted to more restricted
[5445] and pixel space would be the least
[5447] restricted
[5449] then we have regularized pixel space
[5451] like that fourier approach
[5454] and describe
[5456] cppns
[5457] gans and maybe the extremely the most
[5460] extreme
[5462] approach within this continuum in this
[5464] continuum is searching among
[5466] natural images so we can just consider a
[5469] large data set of natural images and use
[5471] some kind of discrete optimization
[5473] procedure in order to
[5475] find a set of natural images that will
[5477] discriminate between the models
[5480] and there are different tradeoffs to our
[5482] choices here
[5484] so when we use more restricted
[5487] stimulus search space choices we
[5491] introduce more high level content
[5494] by our procedure
[5496] and this adds some complexity for
[5498] example for u.s gans
[5500] they have their own biases about the
[5503] manifold of images that they model
[5506] so now this interacts with our test
[5508] models
[5511] on the other hand now it's easier to
[5513] divide and conquer stimulus domain
[5516] for example think about faces we can
[5518] have a parameterization that generates
[5520] just faces and now we can test phase
[5522] models
[5525] if we go towards the less restricted
[5529] side
[5530] then we must reject non-robust models
[5533] and
[5534] that might be either good or bad
[5536] depending on your research program and
[5539] the kind of problems that you want to
[5541] solve at the moment
[5544] and i think that ultimately if we take
[5546] our neural network models
[5548] seriously as mechanistic models they
[5550] should be able to predict human
[5552] responses
[5553] in
[5554] arbitrary settings so ultimately we
[5556] would like to be able to search over the
[5558] entire entire image space
[5562] now we have to say that there's another
[5564] choice that we need to make which can
[5566] interact with these bursters which is
[5568] the kind of optimization algorithm that
[5570] we use and here we have a continuum
[5573] between more local
[5574] and more global
[5576] search
[5577] optimization algorithms where hgd would
[5580] be on the local side and genetic
[5583] algorithms
[5584] will be
[5585] more global
[5589] okay so i i'm done with the overview uh
[5593] i'll be happy to
[5595] take questions
[5598] nico is also available to answer
[5606] thank you charl that was great and very
[5608] informative um
[5610] let's see
[5612] you can ask your questions either in the
[5614] chat or raise your hand
[5626] [Music]
[5634] uh yes
[5640] daniel go ahead
[5646] hi tall
[5649] thank you very much
[5650] hey
[5651] um
[5652] what a wonderful talk um and even a
[5655] luggard like me could at least pretend
[5657] like he was following along um i have a
[5659] very general and i suppose naive
[5661] question so i apologize in advance and
[5663] this this is to you and and nico i
[5664] suppose um
[5669] once one finds a controversial image
[5672] and i can see how
[5675] it can be useful for adjudicating
[5676] between different models that more
[5678] closely approximate
[5679] um
[5680] human vision or human perception very in
[5683] at that very course kind of in or out
[5686] level once you've identified that image
[5688] and you've identified this difference
[5690] between the two models one that aligns
[5691] more than not
[5692] can you provide an intuition how can we
[5694] then interrogate those models to learn
[5696] something more fundamental about the
[5698] visual perceptual system whether that's
[5701] the
[5702] functional
[5703] algorithmic approach at that sort of
[5705] level of description or whether that's
[5706] at the network architecture
[5708] approach and and just to give you a
[5710] sense of
[5711] the kind of form of answer i was
[5712] thinking about was niko had said earlier
[5714] that you could imagine two human
[5716] observers look at the same image and one
[5717] thing looks more cat like one more
[5719] dog-like and that may tell us something
[5721] fundamentally about the different
[5722] features that those two observers are
[5725] are using to to to make that perception
[5728] and i'm wondering if you can do that
[5729] there for with with two models and say
[5732] ah this model is closer to the on
[5734] average the human perception here are
[5736] the types of features that the therefore
[5738] that that human perception may be
[5740] attending to or here is the network
[5742] architecture the human brain may be
[5743] closer to can can you can you say
[5745] anything about those kinds of intuitions
[5750] okay so i think
[5752] the first
[5753] the immediate insight that we get is
[5755] from the relative performance of the
[5757] different models so that can provide us
[5760] with an arrow in model space
[5763] right
[5764] and but you are asking about
[5766] understanding
[5768] things that the model at the level of
[5770] the individual model
[5772] and i think that there
[5774] it might be attractive to do some kind
[5775] of
[5777] item analysis
[5779] looking more deeply into the particular
[5781] images
[5783] and the methods from the field of
[5785] interpretable ai
[5787] in which we can
[5790] filter the images
[5791] leave just particular features
[5794] to have a more in-depth
[5797] characterization of what drives these
[5799] models
[5800] we haven't done this
[5802] at this point
[5804] for example in the language study we are
[5806] thinking about
[5808] analyzing
[5809] why humans make the choices that they
[5811] made for different sentence pairs
[5814] whether there was a semantic valuation
[5817] violation
[5818] synthetic violation and so on
[5833] other questions
[5840] elena
[5843] uh yeah so um
[5844] [Music]
[5846] i was actually typing this up in an
[5847] email because it's kind of a
[5849] leftover question from before but i
[5851] think is
[5852] a good follow-up after daniel's question
[5855] um
[5856] do you think that and it's more general
[5859] do you think that uh
[5863] what could be the use of developing
[5866] um controversial images for humans
[5870] um
[5871] so
[5873] that being you know uh
[5875] i don't know if
[5877] uh
[5878] you'd be able to do this with uh
[5880] just a ns but uh
[5883] i'm just wondering if it could be used
[5885] as some form of tool
[5887] or these controversial images uh that
[5890] are being created by these ans that
[5891] you're comparing could it be used as a
[5894] tool to better understand something
[5896] about the individual system
[5898] cognition
[5899] uh this might sound like daniel's
[5901] question but i
[5903] wanted to follow up with it too
[5907] so you're asking about controversial
[5909] stimuli that target different human
[5911] individuals
[5912] is that right
[5915] so
[5916] first of all
[5918] right now we are just modeling the
[5919] average
[5920] human subject this is how
[5922] we are interpreting these models
[5925] and
[5926] it's a major task to
[5928] model the distribution of humans
[5932] we really still haven't done so
[5934] i think that once we'll be able to do
[5936] that and generate as you suggest
[5939] controversial stimuli that differentiate
[5941] between individuals
[5943] that might provide
[5947] new uh new phenomenology of
[5950] in inter-individual differences that we
[5953] don't have at the moment like we can
[5954] think about
[5956] rorschach
[5957] like uh ink
[5961] spots
[5962] and
[5963] maybe there are very interesting stimuli
[5965] that we can use
[5967] in order to spot
[5968] in the individual differences in how
[5972] people's
[5973] visual system is wired
[5976] but for that we must be able to model
[5979] the individual distribution
[5983] yeah maybe just to add to that yesterday
[5985] we watched this beautiful keynote and
[5988] tutorial on voxel-based modeling where
[5990] the focus is very much on
[5993] adjusting models to explain data and
[5995] individual subjects right so this is one
[5998] way of adjusting models fitting and
[6001] fitting linear and coding models and
[6003] then you have models that are really
[6005] models of individual subjects so it'd be
[6007] fascinating to use those models and then
[6010] create controversial stimuli for those
[6013] and that would be a way of
[6016] of testing to what extent these models
[6019] actually capture
[6020] idiosyncrasies and can be tested more
[6023] severely by making these bold
[6024] predictions about um synthetic stimuli
[6028] that
[6029] would be predicted to look like one
[6031] thing to one person and another thing to
[6032] another person so that's a fascinating
[6035] idea why not
[6038] thank you
[6042] any other questions
[6047] oh yeah sorry daniel yeah go ahead
[6056] you're muted
[6061] thank you yeah
[6063] um so one other question if i could um
[6066] one of the fascinating things about
[6068] human perception is our ability to not
[6070] just conclude some buying uh discrete
[6072] answer but also to rate our confidence
[6074] in this um
[6076] and it's somewhat debated i think in the
[6078] psychology literature if that process of
[6080] confidence is embedded in the process of
[6082] discrimination or if it's a separate one
[6084] that's reflected upon that output
[6087] and i'm wondering if since you you have
[6089] both these elements in your
[6090] psychophysics and in your ai modeling so
[6093] i'm wondering if there's an agreement
[6095] between the
[6097] psychophysical confidence that's rated
[6099] by participants and i suppose something
[6101] about the
[6103] posterior probability or the difference
[6106] between those posteriors that you find
[6108] between your models apologies in advance
[6110] for the background accompaniment
[6113] [Music]
[6116] so i would say that in large
[6119] this neural neo-network models are
[6122] very incalibrated
[6124] so
[6124] they tend to be very confident
[6128] when they shouldn't be
[6131] in our analysis in both projects the
[6134] amnesty cipher 10 project and the
[6136] language project we tried to move away
[6139] from evaluating
[6142] the con the model confidence
[6144] simply because
[6145] we still not we don't have the basics so
[6148] we want the first order choices of the
[6150] models to be human aligned
[6153] so we haven't showed that but
[6156] in the
[6157] anderson cipher 10 project we also
[6159] analyzed the data while
[6162] greetingly optimistically fitting
[6165] the
[6167] confidence ratings of the models to fit
[6170] the human ratings
[6172] so we gave the models their best chance
[6175] in terms of calibration and yet they uh
[6178] they are very human misaligned even when
[6180] we do that
[6181] i i agree that once we have
[6184] reasonable models of human choices
[6188] it seems very important to also have the
[6192] confidence ratings ratings right
[6195] and that might be related to the core
[6198] mechanistic
[6199] properties of these models
[6201] yeah precisely meaning it may be an
[6203] insight that they don't align and that
[6205] may not reflect the failure of the model
[6207] so much as the statement about the human
[6210] process being separated from the human
[6212] process of confidence separated from the
[6214] discriminative process
[6220] i agree
[6228] other questions
[6230] i think there's a question in the chat
[6232] oh yep okay
[6234] uh
[6235] so shahab asks would it make sense or be
[6237] possible to pit models against each
[6239] other based on their latent
[6241] representations rather than their
[6242] outputs
[6245] [Music]
[6246] we are working on that uh wait a couple
[6249] of months
[6251] good question
[6252] uh
[6254] and then t zhuang you want to go ahead
[6257] oh
[6258] yes and i have very specific questions
[6262] i'm sorry not very related to your
[6264] project but to
[6266] what um
[6268] my friend currently do
[6270] and that is about the
[6273] language model how much that language
[6275] model can reflect the human
[6278] judgement
[6279] we
[6280] what we did is that we asked the
[6282] participants to read the
[6285] semantic similarity between the
[6289] abstract words
[6291] and also we create
[6294] rdm based their readings
[6296] and
[6298] additionally we also use the
[6301] bird model
[6303] and work to act model to create rdm
[6306] models and we found that the correlation
[6309] between the computational models and the
[6312] human behaviors
[6313] are very low
[6315] and to that situation are
[6319] a bit tricky and we really don't know
[6321] how to treat situations could you give
[6324] me any suggestions on it
[6329] so i agree with we see similar findings
[6332] right
[6333] we test these models
[6335] that are
[6336] quite human misaligned when we test them
[6338] severely
[6339] uh i would be happy if you could post a
[6342] link to your study in the chat
[6345] and maybe we can take this offline once
[6347] i read it
[6348] um yeah actually that is not my project
[6351] my friend's project and she asked me to
[6354] ask you and probably that after the um
[6358] meetings
[6359] i will email you and we can make a group
[6362] and discuss together
[6364] thank you
[6365] oh yes thanks for help
[6371] other questions
[6375] all right let's take one more five
[6376] minute break then before the um
[6380] before the hands-on portion
[6383] and so we can meet back here at 10 55.
[6846] all right we can move on to the hands-on
[6850] portion
[6859] so there's a link to the tutorial in the
[6862] chat
[6865] if you don't see it
[6866] here i'll post it one more time
[6877] all right i'll take it away
[6881] okay so initially we wanted to have this
[6884] more similar to a lab section in which
[6886] you guys will
[6887] implement the entire thing
[6889] but we realize that there are certain
[6891] limitations to what can be done over
[6893] zoom in an hour so i'm going to walk you
[6895] through the code
[6897] that i
[6898] use in order to generate all of the
[6900] images that you've seen in my overview
[6904] so this uses pytorch and there's
[6908] you can open that
[6910] notebook
[6912] with google collab
[6914] and
[6917] you can message when if you have
[6920] problems you can also open
[6922] a breakout room and help you to
[6925] run things
[6927] so
[6929] please please do that
[6930] and i also invite you to to ask
[6932] questions the moment they arise
[6935] let me know if i miss anything on the
[6937] chance
[6941] okay
[6942] so
[6943] this is a very
[6944] detailed tutorial but i'm going to
[6947] highlight the most important parts
[6950] so
[6951] let's start
[6952] let's make sure that we have
[6956] a gpu
[6957] okay we have a gpu
[6960] i strongly encourage you if you would
[6962] like to
[6963] feel how this works run
[6966] this notebook on your own machine i'm
[6968] not sorry on your own uh google collab
[6972] session and not just watch me doing that
[6975] you can also introduce certain changes
[6977] and see how this works
[6980] tall can you zoom in and make your text
[6981] a little larger
[6987] great thank you okay
[6991] okay so let's
[6993] start with
[6995] the setup
[7008] i
[7009] import pytorch and port vision
[7014] a couple of helper libraries
[7016] and
[7018] as i presented in one of my first slides
[7021] the first step is to
[7025] create a common language for the neural
[7027] network models
[7028] by encapsulating the pre-processing
[7031] of the models
[7033] so here
[7035] there's
[7036] a class
[7037] that encapsulates torch vision
[7040] pre-trained models
[7042] so we can later subclass
[7045] this
[7048] this class to
[7050] define different pre-trained models so
[7052] let's look at the
[7053] important parts here
[7056] so we want we need to know what's the
[7058] input image size that the model expects
[7060] to
[7061] get
[7063] here we store
[7065] the
[7066] color normalization
[7069] on which these models were trained
[7071] and this is the same normalization for
[7073] all of the
[7075] torch vision models as far as i remember
[7077] and we also store
[7079] the mapping between
[7081] output units and classes
[7086] this might be especially useful if
[7089] you're going to compare one of the
[7090] storage vision models with a model from
[7092] other library in which the output units
[7095] were mapped in a different way
[7098] so next we load this
[7101] this model into
[7104] the gpu
[7106] often um we will use multiple gpus so
[7110] it's good to have this module aware of
[7113] which device is being used
[7116] and this is a very important
[7119] line here so this switches
[7121] the neural network to evaluation mode
[7124] turning off
[7125] stuff like batch normalization and drop
[7128] out
[7129] if you don't do that it might act in a
[7131] way that you didn't intended to act i
[7133] think that it is interesting to have
[7135] some stochasticity within the network
[7138] but don't do that by accident
[7140] so
[7141] remember this line
[7143] okay now we are looking at the forward
[7146] function
[7147] which takes us from raw images to
[7150] outputs
[7151] so
[7152] we
[7153] move the image to the device
[7155] of the model this allows us to work with
[7159] multiple gpus
[7162] we make sure the tensor has four
[7165] dimensions
[7166] and now we resize
[7169] the image
[7170] to
[7171] conform with the expected input size
[7174] on which the model was trained
[7177] and this is a differentiable
[7179] interpretation operation so we can later
[7182] back propagate
[7183] through that
[7187] here we apply the color normalization
[7192] and last we collect the outputs so
[7194] for torch video vision models the
[7196] outputs that we get are the logits
[7200] and we convert these to probabilities
[7204] and for these models
[7205] the conversion between logics to
[7207] probabilities is through the softmax
[7210] function
[7211] so
[7212] we return both the logics and the
[7215] probabilities
[7217] and here you can see how we subclass
[7219] this
[7220] torch vision pre-trained model class
[7222] to
[7223] define
[7224] particular pretend
[7226] models and we can have the details
[7229] on each model within its initialization
[7233] function
[7235] for example this is the input input
[7237] image size
[7242] again please ask questions if anything
[7245] is
[7245] unclear
[7247] okay i will evaluate this cell
[7250] and now let's create and load
[7254] these model classes
[7257] this downloads
[7259] the model weights
[7268] okay
[7270] and
[7273] we want to make sure before we do
[7274] anything
[7276] with stimulus optimization that we
[7279] are interfacing with the models
[7280] correctly
[7282] so this is a very basic sanity check
[7285] we are now
[7286] downloading a couple of
[7288] test images
[7290] and we are
[7291] testing the classifications of these
[7293] images in the models
[7299] so we can see that we can see that these
[7301] two models do very well
[7303] this is obviously an insufficient test
[7306] if you
[7307] interface with the model please try to
[7309] test its
[7310] known benchmarks for example imagenet
[7313] accuracy
[7316] often if you get the pre-processing
[7318] wrong the size wrong
[7320] then
[7321] you will see probabilities that are too
[7323] too low for easy images
[7325] or
[7326] misclassifications
[7330] okay
[7332] now we're going to define a
[7334] controversiality score
[7336] and we have here two versions of that
[7340] so
[7343] one version is aimed at
[7346] multi-label models models that can
[7349] assign a high probability to more than
[7350] one class
[7352] and this is consistent with our mnist
[7354] and cipher study
[7356] and the other kind is for soft max
[7359] models to multi-class models that they
[7361] can choose only a single class
[7363] so let's look at this function
[7365] we
[7367] supply this we provide this function
[7370] with an image
[7372] model one model two as objects
[7374] the names of the classes
[7379] alpha is a parameter that controls our
[7383] smooth
[7384] minimum how sharp is it if we choose a
[7387] high alpha then it will behave more like
[7390] the hard minimum
[7392] and
[7393] see if i can scroll this yeah
[7397] so
[7399] this is the distinction between
[7401] multi-class
[7402] and multi-label models this is for
[7404] multi-class
[7406] and
[7407] generating we would like to see outputs
[7411] okay
[7413] so let's look at the core part of this
[7416] so if we have
[7418] a multi-label model
[7421] then we are
[7424] looking at the logics
[7426] of
[7427] one model with respect to
[7429] one class
[7432] and
[7433] the other model with respect to the same
[7435] class with a minus sign
[7437] and vice versa and we're going to apply
[7439] smooth minimum over these
[7442] four terms and by maximizing this with
[7445] minimum we're going to push all of these
[7446] terms up
[7450] for simpler multi-class models
[7454] then we are going to look at the log
[7456] softmax
[7459] and looking at the log softmax is better
[7462] than looking at the probability itself
[7463] due to
[7464] the numerical precision of this quantity
[7469] so now we are taking
[7471] the
[7472] oh
[7473] let's try this again
[7485] okay
[7493] sorry about that so now we're taking the
[7496] log probabilities of
[7499] one model with respect to the first
[7501] class
[7502] and the other model with respect to the
[7504] second class and this is then
[7508] um
[7509] used as an input argument for the smooth
[7512] minimum operation
[7513] so
[7514] well i should switch to a
[7519] better better browser
[7523] let's use firefox instead of chrome
[7529] can you still see my screen
[7532] yes
[7534] okay
[7548] okay let's hope this will not happen
[7550] again
[7565] is the text sufficiently big also here
[7570] yes
[7572] okay
[7574] okay so we got back to
[7577] same place
[7578] and so this is our smooth
[7580] controversiality score
[7582] and we also
[7584] return what we call here hard
[7586] controversiality score which is the
[7589] minimum of the actual probabilities so
[7590] this is hard minimum and we are looking
[7593] at the probabilities another the logits
[7595] or log softmax and this is used for the
[7598] formal evaluation of the
[7600] controversiality of these images
[7602] and the amnesty cipher 10 project
[7605] we use this score in order to choose
[7609] which stimuli we're going to use
[7612] out of all of the stimuli that we
[7613] generated
[7616] so this is high if
[7618] the two models strongly disagree on the
[7620] image with respect to these two classes
[7626] okay
[7627] so now let's look at the image
[7629] optimization loop
[7631] so this function receives
[7633] model one and as object model two as an
[7636] object two classes the size of the image
[7639] and here we're going to
[7642] generate four controversial stimuli at
[7644] the same time and the way it is set up
[7647] is that there will be no interaction
[7649] between these different images so the
[7651] result will be the same
[7653] as if we
[7655] you ran this
[7657] code four times
[7658] we specify which optimizer
[7662] here we have
[7664] the parameters of the optimizer and
[7667] set the weight decay to zero
[7669] here weights would
[7671] translate to pixels and learning rate is
[7673] quite important so we'd like to adjust
[7675] the learning rate so we see
[7678] improvement in good pace but we don't
[7680] see sort of the optimization
[7682] overshooting and going up and down if we
[7684] see that we should reduce the learning
[7686] rate
[7687] this is the readout type we set it to
[7690] log softmax because we are going to use
[7691] multi-class models
[7693] random seed which is used for
[7696] creating the initial stimulus
[7699] and this controls when we should stops
[7702] so either after a
[7704] thousand steps
[7705] or
[7707] 10 steps without changing
[7709] the
[7710] pixel value in
[7712] to the extent of one
[7714] bit
[7717] okay so these are the main things
[7720] so now let's look at this
[7724] code so here we create
[7727] the initial image
[7728] which is a uniform uniformly distributed
[7731] random noise image between zero to one
[7735] it might also make sense to use pink
[7737] noise
[7738] instead
[7742] and
[7742] now we'd like to create our z right
[7746] we're not going to optimize
[7748] the image we're going to optimize
[7751] a version of that that's
[7753] whose value is run between minus
[7754] infinity and infinity
[7757] so in order to create the initial z
[7759] we are using the inverse sigma transform
[7762] and now we have a z
[7765] whose sigma transform is that initial
[7768] image that we created
[7774] this is important we tell pi torch that
[7777] we'd like
[7778] gradients with respect to z
[7782] and here we define
[7783] an optimizer
[7785] whose parameters are z
[7791] okay and now we get into the
[7793] optimization loop
[7795] so
[7796] in this line so
[7798] first this
[7800] we are
[7800] zeroing the gradient this is something
[7803] that we have to do
[7804] in pi torch unless we once gradient
[7806] accumulation
[7808] now we convert
[7810] we transform z
[7812] into
[7813] x
[7814] so unbounded image
[7816] into
[7817] a valid image between zero to one
[7820] and we feed
[7822] this x
[7823] into our function that evaluates the
[7825] models and returns
[7828] the controversiality score
[7831] here we define the loss
[7833] and this is minus the smooth
[7835] controversiality score and it's minus
[7838] because we want to
[7839] maximize the controversiality and this
[7842] optimizes minimize
[7845] this summates the loss across multiple
[7848] images
[7851] here we calculate the gradients
[7853] and adjust the image
[7857] so
[7858] that's the core part
[7861] here we test for
[7863] convergence
[7865] in this part
[7867] and finally we take the resulting x
[7871] here
[7872] i'm converting x to an 8-bit image and
[7875] back to floating point representation
[7877] because i want to eliminate
[7879] very fine
[7881] differences or fine
[7883] values in the in the image intensity
[7886] that cannot be represented on the screen
[7889] cannot be presented on screen
[7892] and i evaluate the hard control
[7894] controversiality score of that quantized
[7896] image
[7898] so this x is going to be our final
[7901] controversial stimulus that we might use
[7903] in
[7904] an actual experiment
[7906] so let's evaluate
[7910] these cells so we have this in memory
[7913] and we'll start by taking these two
[7916] standard neural networks
[7919] the resonant and inception
[7921] and we will create a controversial
[7923] stimulus with respect to the ram runner
[7927] and persian cat
[7929] classes uh if you are doing that you can
[7931] also change the classes there is
[7934] a list online you can see the link
[7936] within the model class of the names of
[7939] imagenet classes
[7942] here we specify that we are going to use
[7944] the multi-class formulation
[7948] so let's run this
[7955] and now you can see
[7957] these are the
[7958] predictions of the first model you can
[7959] see that
[7960] very quickly we convinced resin 50 that
[7963] it sees a wam runner
[7967] and inception
[7969] that it sees a persian cat
[7972] and this converge after
[7974] 51 steps
[7976] we have a perfect controversiality score
[7978] this is the hard controversiality score
[7981] for all of the four
[7983] images
[7985] meaning that
[7986] each model assigns
[7988] one to its target class one is
[7990] probability form
[7994] how does the convergence rate of each
[7997] model is that informative at all
[8000] um so you will see that
[8003] some models are
[8004] [Music]
[8005] slower to change
[8007] their response
[8009] i think that it is informative this is
[8011] not a measure that we
[8013] analyze
[8019] often
[8020] you will see if you there we now pair
[8022] two models that are really easy to
[8023] convince but
[8025] if you have a model which is
[8028] harder to convince then you might see a
[8030] dynamic in which the
[8033] model that is more easier to convince
[8036] is
[8038] changes its
[8039] classification first
[8041] and then the image starts to move
[8043] towards
[8044] the to
[8045] [Music]
[8046] convince the other model to drive its
[8048] specification
[8052] but since we are
[8053] using gradient
[8055] ascent if our learning rate is right
[8058] we we keep improve we keep improving the
[8061] controversiality scope in each step
[8066] so let's look at the resulting images
[8073] so you can see
[8075] these are these are not initial images
[8077] these are the optimized images
[8080] although to us they look the same like
[8082] noise images and
[8084] we see that the networks have very
[8086] strong disagreement about
[8089] their classification
[8092] okay
[8093] so
[8095] now let's consider
[8096] models
[8098] that are somewhat robust
[8100] so we're going to import models
[8102] from
[8103] the robustness toolbox this is a madrid
[8105] lab resource they open sourced both the
[8108] code for training such models and some
[8111] pre-trained models
[8114] this is their
[8115] reference
[8117] so we are now going to
[8119] install this package from
[8123] ipl
[8124] we also need wget to download
[8127] the network's weights
[8133] okay
[8136] and now we're going to define
[8138] another model class
[8140] for these
[8141] models and as you will see there are
[8143] certain differences between
[8145] these models
[8146] and the torch vision models with respect
[8149] to the interface and by encapsulating
[8151] these details
[8153] within this class we can later forget
[8158] about these way about these differences
[8161] and have a modal agnostic code
[8164] so
[8167] here this is our load function in which
[8169] we use wget
[8170] to download the model weights
[8173] if we call this for the first time
[8176] this is a robustness package specific
[8179] code
[8179] for
[8180] restoring the model from saved file
[8184] we move the model to its
[8187] designated gpu
[8189] again
[8190] we switch the models to evolve mode
[8194] turning off dropout and batterization
[8199] this is similar to what we what we had
[8202] in the torch vision class
[8204] so
[8205] we resize
[8207] the images
[8209] one difference here is that we do not
[8211] normalize the color channels because in
[8213] the robustness package
[8216] models
[8218] the normalization is done within
[8220] their model classes
[8223] okay so the rest is the same and here we
[8226] define
[8227] different particular pre-trained models
[8229] and
[8230] this is the architecture
[8232] this is the kind of
[8234] lp norm used for other cell training and
[8237] this is the
[8238] epsilon used for adversarial training so
[8241] greater epsilon
[8243] means more epsilon robust models
[8249] okay
[8251] so let's continue
[8252] we're now
[8253] loading this model
[8259] this takes a little bit
[8263] so let's let's continue and look at the
[8265] previous results while they they
[8267] download
[8268] so here we optimize the same thing we
[8270] take
[8271] but with different models we take resin
[8273] 50 and the version of resin 50 that was
[8276] adversely trained using l2 non-bounded
[8280] perturbation of the size 5.
[8283] and again we use
[8285] the weimaraner and persian cat
[8288] classes
[8291] these models are somewhat slower to
[8293] validate so i'm going to limit
[8297] the steps
[8300] and
[8302] let's see if
[8304] no still loads
[8305] so you can see that also here
[8308] we managed to
[8309] increase
[8311] the targeted classifications
[8313] we have here some sort of more
[8315] complicated dynamics
[8317] but eventually
[8319] we get to the point in which
[8323] we have
[8325] good controversiality scores so
[8329] each model detects
[8331] a wam runner this is average probability
[8333] across the
[8334] four images with high confidence
[8339] and
[8341] the persian cat
[8344] with high complements the other model
[8346] sorry
[8350] okay
[8351] so
[8353] let's see if the model is loaded and
[8354] loaded
[8356] sorry about
[8358] another
[8377] so while this runs
[8379] you can look at these
[8381] examples
[8382] you can see the model classifications
[8385] and the resulting images
[8387] which largely align with the
[8389] classifications of the robust model
[8399] okay
[8403] in the next step we are going to
[8405] create controversial stimulus
[8408] with the inverse
[8410] category designation
[8415] let's look at that
[8418] so now
[8419] the standard model c is a persian cat
[8422] and the robust model of the city
[8424] training model sees a waverunner
[8431] and the next step would be to
[8434] pit the robust models against each other
[8438] let's look at the results
[8440] so just let me show you then
[8443] we
[8444] use resin 50
[8445] trained
[8448] using visual research training
[8450] and a wide version frozen 50.
[8454] so it has
[8455] two times the channels
[8461] and now we get these images
[8463] that convince each of the
[8466] models
[8468] but are not
[8469] [Music]
[8471] either a cat or a dog
[8473] for us
[8476] so this is a direct comparison direct
[8478] contrast
[8479] of these two other static trained models
[8484] okay
[8486] and this is the
[8488] inverse
[8489] target assignment
[8494] and we get a slightly different result
[8497] we are now eyeballing all of these
[8499] images but to make any
[8500] concrete
[8502] inferences we must run psychophysical
[8505] testing using multiple subjects and also
[8508] multiple images we should think about
[8510] these images as
[8512] random factor that has to be evaluated
[8519] so
[8521] as a rule i wouldn't have the same
[8523] stimulus set for all of the subjects
[8526] it's good to have several different
[8528] stimulus groups
[8540] okay
[8541] so this is we already we've seen this
[8543] matrix
[8545] and now it's
[8549] you can go back to this but i want to
[8551] proceed to
[8552] the um to using non-trivial stimulus
[8555] parameterizations
[8557] so let's see how this is done
[8561] we are now going to use torch lucent
[8563] which is a pie torch adaptation of
[8565] tensorflow lucid
[8567] we'll install that
[8576] and now we need a slightly
[8578] more complicated stimulus optimization
[8580] loop
[8581] so here we provide this function
[8585] with a list of
[8586] random noise transforms these are
[8589] loosened objects
[8591] and
[8595] this is
[8597] paramf let's look at this
[8608] i should make a text smaller
[8611] so this is a function without no
[8613] arguments that returns two things it
[8616] returns
[8617] the representation the stimulus
[8618] parameterization that we are going to
[8620] optimize
[8621] and a function that
[8624] converts
[8626] this
[8627] z
[8628] into x into an image and that function
[8631] is dependent on the particular
[8632] parametrization that we are using for
[8633] example it might be a gang generator
[8636] uh i'm wondering if we want to
[8639] let people
[8641] try that
[8642] in their notebooks and
[8644] get some feedback or continue
[8657] try which part in the notebook the um so
[8659] they can start they can try uh the upper
[8662] the direct optimization parts
[8665] i'm not sure maybe some people are just
[8666] watching
[8671] i
[8672] think most people are probably going
[8673] along it's been very smooth so far on my
[8676] end okay
[8677] okay
[8678] please ask questions if anything is
[8680] unclear
[8682] you can also open
[8684] data issues later on
[8686] um
[8688] okay so i will continue
[8690] so installed
[8692] so that
[8695] and we described
[8698] these two
[8700] this parameter function
[8703] and the transform the list of transforms
[8707] so here we were borrowing
[8711] loosened
[8712] objects so
[8714] we don't need to code too much
[8716] to achieve this
[8718] so let's look at how we
[8721] create
[8723] the stimulus representation
[8726] so here
[8727] we create using this paramf
[8730] we create
[8732] the
[8733] okay create z
[8735] the stimulus parametrization this can be
[8737] actually more than one tensor
[8741] and we have image f which is a function
[8744] that takes params
[8746] and returns an actual image
[8750] this composes the list of random
[8752] transformations into a single transform
[8756] and now we
[8757] define the optimizer
[8759] with respect
[8761] to
[8763] this list of parameters
[8765] for example if we are going to use the
[8766] cppn
[8768] these parameters would be the weights of
[8770] the cppn network
[8776] so
[8778] here we create
[8780] the image from z
[8783] this is slightly less
[8785] explicit
[8787] and here we apply
[8788] the random transformation
[8792] i'm allowing
[8794] lucien to use a different gpu here
[8798] we now take
[8799] the transformed image or images if we
[8802] are
[8803] preparing more than one controversial
[8804] stimuli at the same time
[8806] and feed it
[8808] to the models
[8810] and collect the controversiality score
[8814] so next it's the same thing
[8816] and we take
[8819] the resulting image x
[8823] here
[8824] and that's our final symbols
[8827] so all of the magic is essentially done
[8829] within this
[8830] parameter f that gets us from z the
[8833] stimulus
[8835] parameterization to x the actual image
[8848] okay so let's try that and
[8852] first we still use the simple pixel
[8854] space
[8856] representation but we are adding
[8859] very strong jitter so
[8861] this is
[8862] about ten percent
[8864] of the image size 25 pixels
[8871] let's see
[8873] france
[8884] still works
[8888] now if any
[8890] if the response of the models was driven
[8892] by particular pixels in particular
[8894] locations that wouldn't work anymore so
[8896] we are searching
[8898] for features that are robust to to
[8901] jitter
[8910] so let's skip to the results
[8914] and you see that we see some emerging
[8916] structure
[8918] in these images this is somewhat similar
[8921] to
[8923] unsuccessful deep dream images this is
[8925] from where this method came from
[8928] let's look at the images that we created
[8930] now
[8934] same thing
[8937] so
[8938] this didn't fix
[8940] these models evaluation even within this
[8942] restricted similar space these
[8945] models are very human
[8947] misaligned
[8949] here you can see
[8950] the results of this procedure for all of
[8952] the
[8953] model pairs
[8955] and you can see that for the robust
[8956] models
[8957] these images are
[8959] smoother than what we've seen before
[8962] by the way when we
[8964] i'm not sure if i can explain that but
[8966] when we use larger jitter
[8968] we often see
[8970] misconfiguration
[8972] of the visual features
[8974] in these images
[8979] okay
[8981] and now let's look at less trivial
[8983] prioritizations
[8985] so here
[8986] we define a fourier parametrization
[8990] that downward down weights
[8992] the high frequency
[8995] components of the gradient
[8998] and
[8999] this part the correlate
[9001] also changes the color channels from rgb
[9005] representation which is highly
[9006] correlated
[9008] to
[9009] a decorated representation
[9011] in which
[9012] if you will evaluate these
[9014] channels with natural images
[9017] you will see that there is a zero
[9019] correlation
[9021] there's more information in the rational
[9023] for doing that in chris willa's paper
[9026] in
[9027] distill i recommend this
[9031] reading we also introduce cheater
[9036] so this runs
[9050] so here you can see the results for the
[9053] two
[9054] standard non-other acidic train models
[9059] maybe we can
[9062] zoom in
[9064] one of these images
[9075] okay and
[9076] here maybe we see some
[9078] pattern and again we are now playing
[9080] this eyeballing game but everything has
[9082] to be tested formally with multiple
[9085] subjects so it's not just my impressions
[9090] and here you see
[9092] the result of this analysis and this is
[9094] what you've seen in nico's talk
[9103] this is done for multiple categories we
[9106] skip that
[9110] and
[9111] i let's look at these examples for a
[9114] moment
[9116] so we see here an interesting failure
[9118] mode of both models both robust models
[9122] so each model sees is its targeted
[9126] category
[9127] and it doesn't see the other category
[9130] so here one model sees this duck and the
[9133] other models is this bridge
[9137] and not vice versa
[9139] and here the same dock is now
[9141] in the grocery store
[9143] and here we have this combination
[9145] between university straw and the screen
[9149] we see
[9150] two classes
[9152] and each model see only one class
[9156] so
[9157] there is a good question how we should
[9159] treat such images in which we have two
[9161] different interpretation when we test
[9163] human subjects
[9166] we might get very different results if
[9167] we have a false choice task versus a
[9170] more open-ended tasks like the one that
[9172] we use in the andersen cypher10 project
[9174] in which you could rate
[9177] each category independently
[9180] okay
[9181] so
[9182] next we have the cppn weights
[9185] so again we are adjusting the weights of
[9188] a compositional pattern producing
[9190] network and this creates
[9193] smooth images
[9194] we need
[9196] for this representation we need to slow
[9198] down
[9199] the learning rate
[9206] so there's certain trial and error which
[9208] should be guided
[9209] by the optimization dynamics not by the
[9212] results
[9215] so we'd like to see nice and steady
[9217] [Music]
[9218] cost decreasing optimization
[9225] so now we're adjusting the cpp and
[9226] weights
[9229] due to some implementation
[9230] limitation this is done only for
[9233] a single image
[9235] and we can see that this is a bit
[9236] jittery it might mean that
[9238] our learning rate
[9240] is still too high
[9249] although it does converge
[9254] now we are running this on the two again
[9256] naive
[9258] non-other silly trained models and we
[9260] get
[9262] a good controversiality
[9264] let's look this is the image that i
[9266] produced when i
[9268] ran this before let's look at the new
[9270] image
[9276] okay
[9280] and now
[9286] this is the figure that i showed
[9288] in the overview
[9290] using cppns for all of the model
[9292] pairings
[9294] we are approaching the end
[9296] here we see
[9297] classes the two robust models contrasted
[9301] for different classes
[9303] this is similar to the matrices that
[9304] niko showed in his talk
[9312] you also have code here i will not run
[9314] it it takes
[9316] many hours but you have code for
[9318] reproducing
[9319] these figures
[9321] using a batch of optimization
[9324] procedures to generate all of this
[9327] and i think that that would be the last
[9329] part now we are going to look at the
[9332] gun parameterization we need some custom
[9335] code here
[9336] and this is a special gun that we're
[9338] using
[9339] it is again that was trained
[9342] to invert
[9343] the
[9344] representations
[9346] of alexnet
[9348] so
[9350] they took alexnet
[9351] they presented natural images to alexnet
[9354] extracted
[9356] the latent representations
[9358] and then they
[9360] they trained again
[9362] to reproduce these latent presentations
[9364] so we have
[9366] four different
[9367] versions
[9368] of
[9370] this game
[9371] using different alex and features
[9376] so this is slightly technical won't get
[9379] into this
[9380] right now but we can run this code
[9386] we are downloading the gantt weights
[9397] here we're again using the two
[9399] standard models
[9406] and this is fc6
[9409] latency presentation
[9418] again the optimization here is slightly
[9420] jittery
[9422] this might be related to my
[9426] learning rate but it might also be
[9428] related to the random noise
[9429] transformations
[9431] so we are
[9432] evaluating slightly different slightly
[9435] jittered versions
[9436] of the image in each iteration
[9442] let's scroll down
[9448] so these are the results
[9450] from my
[9452] previous iteration
[9453] and again these are
[9456] non-autistic trained networks
[9459] and when when we use the gan
[9461] frequency requirementization
[9464] we don't get this
[9466] uniform noise images we get images in
[9468] which there are
[9469] certain
[9471] visual features that we might recognize
[9473] you can see that there's lots of
[9475] variability between the stimuli and this
[9477] is this is why it's very important to
[9479] think about this stimuli as a
[9482] random variable we'd like to have a
[9484] sample of this thing i would like to
[9485] test statistically that our
[9488] comparisons between human and models
[9490] generalized not only between
[9493] between subjects but also between items
[9497] in the
[9499] cipher 10 study i had some doubts so i
[9503] ran the entire procedure again and had
[9504] another batch of 30 subjects
[9507] luckily the results were almost the same
[9510] so we had a sufficiently large sample of
[9512] subjects
[9514] and no sufficiently large sample of
[9517] items
[9519] so
[9520] let's look at the new results
[9523] this worked very well as you can see
[9532] very spooky
[9542] as i said before i'm i'm
[9546] i'm a bit hesitant about the gun
[9548] approach it's very strong but
[9551] it also
[9552] complicates our interpretation of these
[9554] images because the gan has its own
[9556] biases that
[9558] might lead
[9559] to these images
[9566] so
[9566] to demonstrate that here i
[9571] create
[9572] uh controversial stimuli with a single
[9574] step which is not sufficient to achieve
[9576] controversiality so these are very very
[9579] close these images are very close to the
[9581] initial images
[9585] which is a random initialization and we
[9587] can still see lots of
[9592] visual detail
[9598] and here we see the effect of using
[9600] different versions of this gun
[9602] trained on inverting different alex net
[9604] layers
[9605] so that would be
[9606] pull 5
[9608] fc6
[9609] fc7 and fc8
[9611] and each version of this gun has its own
[9614] prior or
[9616] constraint
[9617] on
[9618] image space
[9622] this is especially evident for the pair
[9624] of the
[9626] non-robust models so we can compare this
[9630] with this
[9637] this to me really looks like a
[9639] blurred lime runner
[9641] and this is consistent with resin 50's
[9644] classification
[9647] okay so that's it finished in time
[9651] i would be happy to take more questions
[9654] if you have them
[9660] thank you paul that was great very
[9662] illuminating
[9668] any other questions
[9672] everyone i mean it just occurred to me
[9674] it should have been obvious before
[9675] probably but this could potentially also
[9677] be useful for evaluating different
[9680] training regimes and training data sets
[9683] like for example it seems like some
[9686] certainly the reconstructions are
[9687] affected by
[9689] statistical uh regularities of different
[9692] classes and the training set right like
[9694] the cat often seems centered whereas the
[9696] dog is not
[9701] yeah i agree so we have multiple
[9703] dimensions
[9704] in which we should compare models
[9707] so we have the training data
[9709] the training task
[9712] the algorithm used
[9715] to fit the model
[9719] and the architecture
[9722] so to cover model space systematically
[9724] we need to
[9726] evaluate lots of models
[9728] we are now generalizing this
[9729] controversiality score to
[9731] address multiple models with a single
[9734] image
[9735] so this way we won't suffer from
[9737] combinatorical explosion of the number
[9739] of model pairs that we need to evaluate
[9743] [Music]
[9745] okay
[9747] any remaining questions
[9752] uh hi again uh so
[9755] one thing that occurred to me as you
[9757] were going through this was
[9759] how in the general workflow you have all
[9763] these parts but one part that might slow
[9765] things down would be the human evaluator
[9768] that was the key part
[9770] um for determining how
[9772] uh like the quality of
[9775] these images so like what if
[9779] you were to replace the human evaluator
[9782] with some sort of
[9784] arbitrarily determined
[9787] reliable model
[9789] so
[9790] something that could be you know
[9792] could have been identified using this
[9794] work here uh as like like for example
[9797] gpt2
[9799] uh for the language models um did very
[9802] well and so did roberta
[9804] you know those could be one of the
[9806] models that could be used to
[9809] replace the human evaluator and then
[9813] judge
[9814] be used as a judge for all other models
[9816] do you think that that could be very
[9819] useful
[9820] scalable
[9821] and potentially even change
[9823] how models are evaluated in the deep
[9826] learning space
[9829] so i think that if we had a model that
[9831] we were willing to assume
[9834] that is correct we would certainly use
[9836] that and that would be much more
[9838] powerful than what we are doing and
[9840] running slow human experiments
[9842] but
[9844] i think that at this stage we can't
[9845] assume that any of these models
[9847] is a good approximation
[9849] of human judgments
[9851] so
[9853] this is why we don't have a special
[9855] status for one of the models
[9858] i have to say that in our
[9860] procedure
[9862] each model serves as a judge in a way
[9865] but it is that it is done in a symmetric
[9868] fashion
[9870] so each model serves as a judge for the
[9872] other model in a way or the counter
[9875] force
[9878] did this
[9880] answer your question
[9883] um i guess uh
[9885] you know when i used the word reliable
[9887] it's did a lot of work uh
[9889] i i
[9891] i do understand that um
[9893] you know no one model like all models
[9895] are wrong etc so
[9897] you know um
[9899] i was just thinking that
[9901] perhaps in addition to
[9904] beating benchmark performance levels and
[9906] accuracy
[9907] uh there could be a
[9909] you know give like whoever is the lead
[9913] in beating the benchmarks could then be
[9915] used to judge other models
[9918] um in addition
[9919] um
[9920] but uh
[9922] then there could always be some sort of
[9924] you know
[9927] side thing at the
[9930] like a parallel
[9933] evaluate human evaluation
[9935] aspect to evaluating all of these models
[9939] but in conjunction with judging
[9942] [Music]
[9944] models online you know with uh
[9948] you know whatever model is in the lead
[9950] um just to kind of add a bit of
[9954] you know
[9955] another dimension of
[9958] you know seeing how these models work
[9960] but i do understand what you mean by
[9962] uh
[9963] the
[9964] each model judging each other is
[9966] symmetrically is
[9968] an
[9969] agnostically uh
[9971] in using the human evaluator as
[9974] that is probably the best way
[9977] um
[9979] does that make sense
[9980] yeah so we essentially view each model
[9983] as a potential hypothesis
[9985] about how humans respond
[9988] we'd like to have an equal
[9990] status for all of the models in our post
[9993] optimization procedure and evaluation
[9994] procedure
[9996] i do see that once we go beyond pairs of
[9999] models when we optimize them
[10001] there are multiple games that can be
[10003] played you can think about consensus
[10005] consensus of models
[10007] some kinds of competitions it's a very
[10010] wide range of methods that can be
[10012] devised
[10014] maybe niko wants to add
[10018] yeah i think
[10019] it's a fascinating idea right so we're
[10022] looking here at two levels at which to
[10025] adapt models to our data the direct
[10028] level where we
[10029] adapt the parameters based on some data
[10032] that we've acquired by measuring human
[10034] brain activity or animal brain activity
[10036] or behavior insurance or animals and
[10039] that is very expensive data and usually
[10041] it's not enough data to set those
[10042] millions of
[10044] parameters right so um we need some some
[10047] alternatives to that and controversial
[10049] stimuli in a way give us uh another
[10053] level of analysis where we use these
[10056] directly
[10057] parametrically optimized models um and
[10061] pit them against each other and then
[10062] with very little brain or behavioral
[10064] data that is very
[10066] expensive we can get a sense of
[10069] direction a sense of which models from
[10072] which other models so we can improve
[10074] models of course it would be much more
[10077] efficient to be able to to use a model
[10079] as judged but then a question would be
[10082] if you already had the ground truth
[10084] model then why are you going on this
[10086] exploration in the first place to
[10088] compare all these other models you could
[10089] just say we already know the truth about
[10092] this perceptual process right we have
[10094] the judge model here
[10096] however i think
[10099] it's it's nevertheless an inspiring idea
[10101] because
[10102] then computer science we also want to
[10105] just understand the relationships
[10107] between different models right so it
[10108] could be that maybe we have a very good
[10111] model for computer vision for for some
[10114] application but now we want to compress
[10116] that down so that it fits on a
[10119] smartphone or something like that right
[10121] and so we want to explore radically
[10123] simpler architectures and so then
[10127] the approach that you're suggesting
[10129] could be super useful for
[10131] engineering for understanding sort of a
[10132] larger space of models and to what
[10135] extent they can
[10136] live up to the high standards of some
[10139] sort of reference model
[10141] that would be
[10142] that would be really cool
[10145] um yeah and i i'll i'll i'll stop soon
[10149] um i was just thinking that it would be
[10153] one of the aims of
[10155] the machine learning field the deep
[10156] running field is to create
[10159] more
[10159] higher highly performing models uh
[10162] that's one of the aims to be able to
[10164] solve problems very easily whereas uh
[10168] with
[10169] neuroscience
[10171] it's more so trying to better understand
[10174] the human brain or any brain or how the
[10178] brain solves these problems and i feel
[10181] like this method
[10183] can be used to kind of
[10186] hook
[10187] one aim to the other
[10189] so
[10190] what i mean is
[10193] you have the human evaluator that
[10195] determines the judging model which
[10198] determines which model is
[10201] which other models is as good or
[10204] as good or following the lead of the
[10206] judging model and that judging model is
[10210] determined to be the most human or
[10214] uh other brain like you know so
[10217] it's kind of like jerry rigging these
[10219] aims together to
[10221] pull things in the more brain-oriented
[10223] direction
[10226] that's kind of how i see it
[10228] but that's just more of a comment than a
[10230] follow-up question
[10233] i think that i now understand
[10236] what you suggested
[10237] so if we do this in a sequential manner
[10240] in which we don't have a single human
[10242] experiment
[10243] then indeed we can sort of gradually
[10245] focus on the right models
[10249] does this
[10251] is this is a line yeah
[10253] so this can be
[10254] this in principle this can be done
[10257] uh especially if we move from our
[10260] heuristic approach to a more principled
[10262] bayesian approach in which we can
[10265] quantify our
[10267] uncertainty about the models
[10268] as we proceed
[10270] and then if we see that a certain model
[10272] doesn't work very well we can stop
[10274] evaluating that model
[10276] not waste our human trials
[10280] yeah um
[10282] lana your
[10283] comment also makes me
[10286] think more in the the engineering
[10288] direction again that you know it might
[10291] actually be very useful when you have a
[10293] reference that is computable but very
[10296] expensive to compute right so then this
[10298] reference is very expensive much like
[10300] human or animal
[10302] data are very expensive
[10304] right and so you don't want to
[10307] directly
[10308] take the the normal
[10310] teacher student framework and deep
[10312] learning where you um
[10314] where you just train a student to to
[10317] emulate
[10318] the teacher and
[10320] as you're trying to compress the teacher
[10322] into a simpler model for example but you
[10324] want a method that needs much less
[10328] computation much less
[10331] data from the reference model right
[10333] and so at that level even though our
[10336] motivation with controversial stimuli is
[10339] primarily to
[10340] um
[10341] get evaluations of models of the human
[10344] brain and animal brains the primate
[10345] brain
[10346] i think it could also be useful
[10348] eventually in engineering to have this
[10351] this outer loop where you you can deal
[10353] with the situation where your empirical
[10356] constraints are extremely costly
[10364] yes
[10367] this is very cool uh
[10369] i'm going to step back because it kind
[10372] of dominated the conversation but thank
[10374] you so much for the
[10376] keynote and tutorial i've learned a lot
[10379] this is great
[10381] thanks for all the great questions
[10385] any remaining questions
[10389] all right well please join me again in
[10391] thanking um mikko tal and wen for a
[10393] fantastic series of talks and great
[10396] tutorials thank you all
[10398] thank you all
[10399] and
[10400] we have a few more ccn events coming up
[10404] you can see here so there's
[10406] um two more gacs
[10409] this week
[10410] um one more gac and a keynote next week
[10413] and then the final gac on useful
[10415] representations will be held october 1st
[10418] so thank you again and we hope to see
[10420] you all at future ccn events
