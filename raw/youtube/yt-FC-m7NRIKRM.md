---
schema_version: 1
id: yt-FC-m7NRIKRM
type: youtube
title: 1.8 billion regressions to fMRI | Journal Club
url: https://www.youtube.com/watch?v=FC-m7NRIKRM
authors:
- Paul Scotti
ingested_at: '2026-06-02T00:37:04Z'
content_hash: sha256:2d0f8744c291f1a7e9dcef4aed28214a0b1b41e10d742d1c6f6e647f59e70f1d
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: Paul Scotti
  channel_url: https://www.youtube.com/@humanscotti
  duration_seconds: 5098
  caption_track: fetched
  snippet_count: 1860
filter:
  score: 0.7
---
[3] okay yeah however you want to start
[6] all right
[8] um
[9] okay so I think you guys can see the
[11] paper Okay cool so uh yeah thank you so
[15] much for uh coming on for this uh paper
[17] discussion I really wanted to uh
[20] understand what uh these authors have
[23] come up with and uh so there you go
[25] that's why I was like they're fair
[28] enough I'll just post this so uh this
[32] paper what uh
[34] what it does it's like given we have a
[38] lot of computer vision models like based
[42] on Transformers uh convolution units and
[46] it's just and the authors just wanted to
[48] see how well these uh you know computer
[52] vision models which there are a lot of
[53] them now uh compare and predict in uh
[58] predicting the brain activity uh using
[61] the NSG data sets so they used around
[65] 224 different models and uh they tested
[69] different aspects of it basically uh
[72] they describe an inductive bias which
[75] means that you know just having one
[77] thing different from each other and
[78] keeping all the things same so I'm just
[81] gonna uh you know dive in deep into what
[84] were the things that actually tested on
[87] um so testing out 160 pre-trained models
[92] and 60 uh untrained models so they
[96] tested 224 models on the NSD data set
[98] and
[100] that came across around 1.8 billion
[103] regressions just interesting and that's
[106] uh what this 1.8 billion regression
[108] scene on the title actually means so in
[111] the testing they actually uh did around
[114] 1.8 200 questions that's uh kind of
[116] crazy but
[117] yeah so they tested out how uh so first
[122] of all it does not uh predict fmri uh
[126] Walks Like The FMI boxes I wish it did
[129] uh but what these authors did was uh you
[132] know get a pre-trained model or an
[134] untrained model uh pass an image through
[137] it uh onto a Higher Dimension latents
[140] right and pass the fmri
[143] uh in a similar encoder uh to get it
[146] onto the same uh Dimensions you know get
[150] the vectors of the same dimensions and
[152] then compare those two embeddings uh and
[156] get a PSN score which you know defines
[158] how well two embeddings are correlated
[161] with each other so by changing different
[164] parts either it might be a model or uh
[168] different you know different models
[170] which are pretend or different tasks and
[173] a whole a whole lot of things and
[176] actually uh the authors uh came up with
[180] what kind of uh parameter should we
[183] change uh in order to achieve the
[186] highest uh you know highest brain
[189] activity
[190] so uh
[193] okay so uh that's what the paper is all
[196] about so
[198] first of all uh here we see
[203] yeah so um before that
[206] um you know uh getting into detail about
[208] what were the things that would actually
[211] uh you know what the authors actually
[214] discussed uh they used two types of
[218] linking methods which were used to
[220] compare the
[223] two embeddings so here they've used uh
[226] uh classic
[228] RSA or uh represented representational
[232] similarity uh
[235] what is it analysis and uh v e r s m i
[240] mean if we go more in into detail about
[243] it these two are all are also the
[246] factors in data binding how well the
[250] model you know model embeddings
[251] correspond to the brain activity
[253] so
[255] so the classic CR uh RSA is just it
[259] assumes that each uh layer of the model
[264] uh contributes equally to predicting the
[267] voxel level brain predictivity which
[270] basically means that each part of the
[273] model is contributing equally whereas uh
[276] voxel level and uh voxel encoding RSA it
[280] resumes that some parts of the image uh
[283] lead to different parts of uh brain
[287] which are being activated so it's not
[289] equally divided in the sense that given
[292] an image uh
[294] it's not necessary that each part of an
[297] image will equally activate that part of
[300] uh you know that part of OTC which is
[304] like uh human positive temporal cortex
[307] so voxel uh encoding artists assumes
[311] that it is reweight so the weights of
[314] the encoders are rebated
[317] and not every part of the image
[320] corresponds equally so if you want uh so
[323] if you want to deep deep dive into like
[325] how exactly they calculated it's
[327] mentioned uh right here
[331] uh but in a chest uh what exactly
[335] so I've just explained what's the gist
[338] of these classical RSA and voxel
[341] encoding rsas and it really and this is
[344] also actually a factor in determining
[346] how close are we uh to predict the brain
[350] uh predictability
[353] so uh yeah
[356] okay I I actually would like to
[359] understand better the specifics of what
[362] is the what are they actually doing with
[364] this RSA so they have all these models
[366] for every given model they fit they they
[370] do say classical RSA between the
[373] occipital temporal cortex voxels
[377] um
[378] correlated to for every layer of the
[382] model
[383] the projections from that layer and then
[385] they pick the best fitting layer as
[387] exactly what they pick and for the the
[391] the
[393] v-e-rsa it's the same thing except they
[396] allow the rebating yeah
[401] um so how do you how do you get from
[402] like a model layer of an arbitrary
[405] number of features to the same
[407] dimensionality as the voxels
[411] correlation
[415] because the RFA is like a correlation
[417] Matrix right so yeah getting the voxels
[420] to the features of a given layer of the
[423] model but the number of features in a
[425] model might not or it's usually not
[427] going to equal the number of voxels
[430] so how do you do the dimensionality
[434] changing to do correlation for it
[438] uh they actually uh even before they get
[441] into that they actually reduce the
[443] dimensionality so
[445] um
[446] uh this is uh this is where they
[449] mentioned here so they reduce the
[452] dimensionality uh uh using the sparse
[456] random projection see now this is the
[458] power of uh machine learning that I'm
[461] not very familiar with so I was uh so
[464] I'm not really good with the details so
[466] uh they did uh reduce the dimensionality
[469] Mostly because if we are looking at
[472] models which is like BGG
[475] in their deepest of the deepest layer it
[478] could have like a 3.2 million Dimensions
[481] per image and that's like too many for
[483] them to handle so they reduce it down to
[486] a Target dimensions and after that they
[489] start uh you know Computing this past
[491] random projections for each uh layers of
[494] the deep learning model so uh so so
[498] reducing the dimensionality plays it's
[501] like the first thing they do I think
[503] that's what they used to equalize the
[505] dimensions between uh the brain boxes
[508] and the image
[510] like as an example then let's say that a
[513] model layer has
[516] um a hundred thousand features and
[518] occipital temporal cortex has I don't
[521] know 5000 voxel I don't know how many
[523] boxes but you have to basically make it
[528] so you take the 100 000 features you
[530] have to make it five thousand random
[533] projection without the weight means that
[536] you're basically selecting 5 000 of
[539] those 100 000
[541] and not altering them at all
[544] for classical RSA yeah I think so
[548] although this is something I need to
[550] read more about
[552] uh because
[554] um
[555] although it does play a part in
[556] explaining what other
[558] uh features do to a network uh we should
[562] really understand this so yeah this is
[564] something I should really uh
[566] yeah right they have to somehow
[568] determine how they're gonna pick those
[571] five thousand
[576] yeah
[578] uh
[579] yeah it's actually interesting how they
[581] actually uh do it
[583] I need to I actually did not read in
[586] detail about how they actually
[587] calculated although they do use uh so so
[592] most of the models if we look at it once
[594] we go ahead it's like the classical RSA
[596] score the PSN uh coefficient of
[599] classical RSA is generally at a lower
[601] rate
[603] um than compared to the voxel encoding
[605] RSA so it just suggests that rebating
[608] those uh uh you know
[611] applying the rebating over those layers
[613] is actually uh it's yeah so there's this
[617] metric that rebating actually explains
[619] 79 of the variance of the NS of the
[624] voxels of the NSD data set while the
[626] classical RSA just explains like around
[628] 31 which means that
[631] uh like there is a lot of variation
[633] across plus you know in the classical
[636] RSA that we just cannot explain
[638] uh so it's like
[641] reweighting really helps us explain uh
[644] you know it helps us realign those uh
[646] image vectors with the brain boxes and
[649] yeah so I should really just get into
[651] how they actually do it I've actually
[653] wasn't even familiar with uh obviously
[656] before this so you really need to do
[658] something about it yeah yeah just one
[662] more
[663] um question then do they do the random
[665] Sports projection both for classical and
[668] for the voxel-wise
[671] they re-weight the outputs of the random
[674] projection or they re-weight before the
[679] so they they do random projection for
[682] both and it's the only difference is
[684] they also re-weighed afterwards for
[687] Knoxville encoding in computer
[691] say the say the thing is I'm not
[693] familiar with what's representational
[695] similarity in Matrix with uh so it's a
[699] complicated way of seeing it correlate a
[701] pairwise correlation Matrix I believe
[704] like
[706] um oh is it that
[709] um not too familiar with it although I I
[712] will definitely get back into this this
[714] is something that they need to uh dive
[716] deep around into the math effect
[719] yeah
[722] sorry this is not the outcome I actually
[724] expected I will actually get deeper into
[726] it but uh yeah the weeds a bit but yeah
[731] it's like these two uh metrics out of it
[735] are constantly being used to measure how
[738] good of a brain mappings we have but
[741] even in the paper they mentioned we
[742] don't uh the authors don't actually know
[744] which one actually is better than the
[746] other although we see the classical rsas
[749] person score is not actually that good
[751] across all of the factors across all of
[753] the models as compared to voxel encoding
[755] but it does not actually mean that uh
[758] voxel and Co like the Vox encoding
[760] artist says uh statistically more
[763] significant than classical RSN so uh all
[767] they should just think about it uh it
[770] can't be true that each part of an image
[772] constitutes equally to the activations
[775] in your brain it has to be like some
[777] parts of the brain will contribute more
[779] anyway just uh talk just some thinking
[782] top of my head so uh as for as far the
[786] mathematics goes into it I'll have to
[788] look deeper because even I wasn't
[790] familiar with the
[795] is yeah
[797] the RSA is pretty simple it's pretty
[799] much just what Paul said where
[802] you extract the features for in this
[804] case a thousand images you construct The
[805] Matrix thousand by the feature Dimension
[808] say feature Dimensions like five
[809] thousand you know a thousand by five
[811] thousand and you just compute the
[812] correlation Matrix
[814] Within like separately for the model and
[817] for the brain data and so you get a
[820] thousand by a thousand correlation
[821] Matrix for each case
[823] then you just correlate those two
[825] correlation matrices and it basically
[828] just measures whether like the
[830] the geometry of the features is similar
[834] in the two
[837] model and brain and uh in this way you
[840] don't have to worry about the difference
[841] in feature Dimension because you only
[843] correlate within the two
[845] like you correlate within the model and
[847] then within the brain
[849] the feature separately and then just
[851] compare the correlation matrices which
[853] are the same shape
[855] right
[856] also essentially just correlates
[860] okay
[864] uh yeah that makes sense
[870] at this point is like
[873] you talked earlier about a little bit
[875] about how you wish they were doing
[877] how you wish they were predicting brain
[880] activity instead of doing this RSA I
[883] kind of looked at the voxel encoding RSA
[885] as
[887] effectively just another way to to
[889] measure
[890] brain activity prediction performance
[893] because the the weights
[896] are given by
[899] just a like a trained linear encoding
[902] model
[904] I just said that in the hopes that it
[907] might it would be helpful for us for the
[909] arguments Challenge and that's all yeah
[911] identical coordination of the fmri
[914] activation so
[918] that's all
[920] right
[921] um yeah so
[924] um
[927] okay okay so
[930] yeah
[932] so to test out if these brain uh you
[935] know uh this brain activations are
[938] actually correlated with the uh you know
[941] the high level latency of the image uh
[944] what the first authors wanted to do was
[946] to test out whether there's a difference
[949] between using a CNN based models uh or
[954] versus the Transformer based because uh
[958] because the cnns have like this
[960] convolutional bias are using you know
[963] convolutions the mathematical Concepts
[966] and convolutions to extract the features
[968] of the image which is actually similar
[972] to how uh we humans correlate uh visual
[976] you know we perceive visuals so
[980] uh so whether to test out if this
[983] convolutional bias will actually affect
[985] the brain activity another predictive
[988] brain activity and well the results was
[992] like uh not so much
[995] in a sense uh both Transformers and uh
[1000] wait give me a sec yeah so both
[1001] Transformers and uh CNN based
[1005] architecture were equally uh were
[1008] predicting equally well you know the OTC
[1010] structures so
[1013] both had like a PSN score of around 0.67
[1016] and 0.66 for Transformer so this is 0.01
[1021] increase so there is no actually so
[1026] statistically speaking both models were
[1028] good at predicting these brain
[1031] activations but uh vits
[1035] but when comparing the accuracies of
[1038] these to vits were less predictive than
[1042] cnns on average when compared to uh you
[1046] know when comparing the boards crsn V
[1049] ersmetrics so the reason might be
[1053] because of this inductive wise that the
[1056] convolution uh uh the the mathematical
[1060] operation of convolution is similar to
[1064] uh how cnns extract the features of the
[1067] image and perceive those image
[1069] so that might be it
[1072] but but both models you know
[1075] with such a huge difference in the
[1078] architecture you know Transformers using
[1080] these multi-head retention uh and it you
[1083] know first we break down the images and
[1085] then we pass it on uh as compared to
[1087] convolutions where we use the filters
[1090] and the kernels to extract features you
[1092] know even if they have this whole
[1095] different architectures they are
[1097] essentially uh predicting similar
[1100] responses in the high level cortex
[1103] so the models are actually converging at
[1106] the same representation format which
[1109] means the the high level latents are
[1112] actually pretty similar even though the
[1115] models are very very different
[1118] uh here uh as you can see the uh
[1125] uh yeah yeah so so yeah so these are the
[1129] scores that I mentioned 0.66 uh PS4 the
[1133] Transformer and 0.67 for convolutional
[1136] models so it actually does not really
[1140] depend it actually does not differ if we
[1143] use a convolution based Network as
[1146] compared to a Transformer based Network
[1149] so uh as compared if we look into other
[1153] architecture it does not really vary
[1156] so the next uh these authors examined
[1160] was the task variation uh what so the
[1164] currently these uh yeah sorry I was just
[1169] hoping I'd like to pause on this result
[1171] for a little bit because I think it's
[1172] kind of yeah go ahead it's interesting
[1174] yeah
[1175] um
[1176] one thing that I saw got brought up in
[1180] connection to this result I wonder if we
[1182] could talk about is like
[1185] something to do with the fact that all
[1187] of these networks that have been that
[1189] are being evaluated here are
[1193] have been kind of like selected for good
[1195] performance on imagenet like these
[1199] aren't these aren't like 20 random
[1201] models these are like 20 of the best
[1203] models
[1204] that have been produced over the past
[1206] decade plus out of thousands and
[1208] thousands of models that have failed
[1210] so I wonder what your thoughts are on
[1213] how that should affect our
[1215] interpretation of these results that
[1217] these are models taken from
[1220] uh these are like good pre-train models
[1222] taken from the internet not random
[1224] models
[1225] okay so that was actually intentional on
[1228] their part because they wanted to uh
[1230] make sure that so every each of the
[1233] models that were tested they were tested
[1235] on image net 1K so all all of the models
[1238] have the same data set with similar
[1240] accuracies uh so uh coming up there is
[1244] actually a section where they test out
[1246] uh different models which don't have
[1249] which actually some of which actually do
[1251] have the you know the top scores for
[1254] imagenet and some of them actually don't
[1256] so uh you know once we get into that
[1261] um the the authors find that there's
[1263] actually no correlation at all between
[1266] the top performance or the all the
[1268] models which are not as good of a
[1270] performers here just to make sure that
[1273] with just to ensure that the only reason
[1276] of uh you know observing change is the
[1280] fact that we're using a CNN is the
[1284] convolutional bias is the reason why
[1286] they've used uh these models which have
[1288] been trained on imagenet data central
[1290] like just one data set uh and have
[1293] similar accuracies so there is actually
[1296] a section where they uh where they you
[1299] know test models which don't have
[1301] similar accuracies and well it does not
[1304] really affect it so yeah
[1309] cool
[1311] um one other quick question is uh did
[1314] you like notice any patterns in The
[1318] Ordering of the models
[1321] I tried to look a little bit I didn't
[1323] really notice any patterns
[1325] in terms of like
[1328] uh
[1331] recent models the y-axis like they just
[1334] sorted it yeah yeah they're like sorted
[1338] by brain prediction score
[1341] RSA
[1344] I mean yeah
[1347] um if you look at this squeeze Knight
[1349] 1.0
[1351] uh it has like a score of around
[1354] 0.63 yeah so I guess they're just sorted
[1357] on the basis of their uh PSL coefficient
[1360] but then again it's not even a Delta of
[1363] 0.1 and that's actually one of the
[1365] results of the paper is like uh
[1368] comparing these models across
[1370] convolution neural networks to
[1372] Transformers most of their peers and
[1374] correlation score is less the Delta is
[1378] like 0.1 it's not even that much
[1381] uh
[1382] yeah so it's just um
[1385] it's like nothing now like point one is
[1388] uh noticeable it's uh not in the sense
[1391] if we okay so if we change a lot of
[1394] these metrics right if we change whether
[1397] we use CNN versus Transformers whether
[1399] we use uh like the models with the top
[1403] accuracies like if we change a lot of
[1405] these uh
[1407] uh you know a lot of these things with
[1410] the models which affect the accuracy of
[1412] the image on the imagenet but in terms
[1416] of predicting the brain activations
[1419] uh the Delta of 0.1 is all they differ
[1423] at and that's it like a lot of this
[1425] paper actually like the conclusion of
[1428] this paper is like even if we have some
[1430] features that can actually improve
[1432] features of the of any deep learning
[1434] model which can actually increase the uh
[1436] accuracy of let's say uh detecting you
[1440] know in the object class of an object
[1442] classification it does not really
[1444] translate into predicting uh the brain
[1447] activations so yeah
[1452] this paper is kind of like
[1456] um it's like saying even if you have a
[1458] lot of things to improve a model it
[1461] might not necessarily improve the brain
[1463] activations that's that's one of the
[1466] things
[1469] do you remember what are the error bars
[1473] uh what
[1475] you see how those little air bars on
[1477] each of the
[1478] to the individual plot I mean should the
[1480] individual markers
[1482] [Music]
[1485] it's like each one is a little rectangle
[1487] with the height
[1490] yeah
[1491] bars over something
[1495] yeah in general I think like yeah the
[1498] differences are small
[1500] but
[1501] the error bars are also pretty small
[1504] some of the differences look reliable
[1506] like say like the best Transformer
[1509] versus the middle Transformers
[1512] excite versus whatever these other ones
[1516] are
[1523] differences are reliable for shares
[1526] since they're counting numerically small
[1529] yeah like and I I mean I'm curious about
[1532] the order still because let's say that
[1535] they sorted it based on yeah the
[1536] performance of the Pearson right but
[1539] yeah looking at the labels it kind of
[1541] goes in the order that you would expect
[1543] of like squeeze net resnet 18 at the
[1546] very bottom and then NF resonant 50 at
[1549] the top like
[1550] it kind of follows right and I think
[1553] yeah the kind of the order they were
[1555] they were released
[1557] yeah I mean like the performance of the
[1559] model going up can correlate with the
[1562] Pearson going up
[1564] yeah on next L was released off like
[1570] before like after resonance is it that
[1573] it's true confidence is one exception
[1575] that I noticed also yeah they're both in
[1578] the middle so the difference is not huge
[1579] but it was interesting to me that
[1581] complex is in the middle in it
[1584] Punk next is also a pretty different
[1587] architecture
[1590] within the CNN family it's pretty
[1592] different
[1595] and it's yeah it's a pretty new model so
[1597] like I don't think they'll just place it
[1600] right over here
[1603] yeah I I just think it's just uh on the
[1606] basis of their PSN so that's yeah that's
[1609] something that was sorted
[1611] but then yeah it's just similar for
[1612] Transformers as far
[1615] but then like looking at the models
[1617] based on that sorting trying to read tea
[1620] leaves in terms of Which models predict
[1622] better
[1623] in the Transformers for example you see
[1625] mostly like vanilla Transformers at the
[1627] bottom and some more
[1630] specialized like hierarchical
[1633] Transformers like the swing at the top
[1641] yeah
[1642] it's interesting but I think the two
[1644] leads are hard
[1648] [Music]
[1655] I think this is uh these results are
[1658] just for uh you know just explaining
[1661] the convolution advice uh if the
[1663] presence or absence of them actually
[1665] affects
[1666] uh you know the prediction of brain
[1668] activation so uh
[1672] uh yeah so should I move on or do you
[1675] have any more questions or thoughts
[1679] about this
[1680] yeah I think we did this one pretty well
[1682] you go ahead
[1683] okay
[1684] so uh yeah that was just about uh
[1688] whether or not having a convolution
[1690] about it but the next one was uh
[1695] whether
[1696] what if we use the models which have
[1699] different tasks so not all of them have
[1703] you know the object classification so
[1705] they use different con uh you know
[1708] computer vision models and some of them
[1711] were actually self-supervised algorithms
[1714] as well
[1715] and they also tested out whether the
[1719] representation of images and aligning it
[1722] with their captions actually help uh in
[1725] brain productivity or not
[1728] so uh
[1730] this is uh
[1732] if it just moved down to the result so
[1734] they used uh so let's first talk about
[1738] the taxonomy models so basically using
[1741] models which have different uh you know
[1744] in a different
[1747] uh they wanted to see if the models with
[1749] different uh tasks can actually uh
[1752] affect the brain productivity so they uh
[1757] so they used
[1758] from autoencoder to you know detecting
[1762] depth so that's a perception to semantic
[1765] segmentation an object classification
[1767] and this actually gave a pretty strong
[1770] indication that you know the tasks
[1773] actually matter yeah even the thing uh
[1777] the surprising thing was the auto
[1778] encoding I mean not really surprising
[1781] but the auto encoding uh
[1783] lisco like of uh PSN score over 0.077
[1789] and vrs is four of 0.103 so one of the
[1792] lowest scores uh and the object
[1795] classification
[1797] relatively had the highest score of
[1800] 0.436 which is not uh you know which is
[1805] not as equal to the one previously as I
[1809] mentioned uh and these authors just
[1811] mentioned that the object classification
[1813] in this uh the data set was not as
[1816] varied as compared to mhnet 1K so that
[1820] was their reasoning for because at this
[1823] point uh my thought was if object
[1827] classification has the highest score why
[1828] is it not equal to the
[1831] you know the emissioner because it also
[1834] uh
[1835] classifies images but in this object
[1838] classification they used uh
[1841] I think the I think the classification
[1843] and the number of classes was like
[1845] around 100 uh whereas in image rate was
[1848] like image here one case was like a
[1850] thousand so since it was like a 10 times
[1853] I guess the classes were like 10 times
[1856] uh larger it led to a higher correlation
[1859] scope
[1861] uh when comparing these models with
[1864] different Arts so uh that I think was
[1868] kind of given but yeah that's kind of
[1870] interesting
[1872] so uh yeah that was like taxonomy or
[1876] object classification doing the best for
[1878] the task onomy like they're using all
[1881] the same input diet right
[1883] but yeah they use a different so tasks
[1886] do like the task of the model does make
[1889] a noticeable differences like the yeah
[1892] yeah
[1894] so like you can't really use some model
[1896] which details like let's say semantic
[1898] segmentation unexpected to you know
[1901] predict those brain uh selectivity so
[1904] even like uh even like it mentions here
[1907] clearly that uh in spite of taxonomy's
[1910] larger training threat of around 4.5
[1912] images uh nearly Thrice that off uh
[1916] imagenet 1K it still has a lower uh PS
[1920] info that's just because uh you know the
[1924] classes are less and the data set is uh
[1927] you know is
[1929] not that uh diverse so um that's kind of
[1934] interesting because you know just going
[1936] off of the author's interpretation on
[1940] Twitter and I think most people's take
[1941] away from the paper itself is that
[1943] image.it is the by far most important
[1946] thing but like exactly that doesn't mean
[1949] that the task doesn't matter like it
[1952] still matters to some degree
[1954] yeah I don't know if uh if image diet is
[1958] like the most important like the task
[1960] matters I guess that's not the second
[1963] because uh clearly there is a lot of uh
[1967] variation between image classification
[1969] and just say Auto encoder
[1972] so uh yeah
[1976] I guess we can also think of it in a
[1978] sense that
[1980] um
[1981] an object classifier will have a better
[1985] understanding of an image as compared to
[1989] you know let's just say depth prediction
[1993] like a depth perception a model so or a
[1998] semantic segmentation model you know so
[2000] so an object classification model will
[2004] have a will have a better understanding
[2006] of an image So that obviously relates in
[2010] terms of uh you know predicting the
[2012] brain uh activations yeah so but also
[2016] maybe it's only pronounced here because
[2018] it's using such an impoverished image
[2021] diet like maybe if it was using imagenet
[2025] or a better input diet then the role of
[2029] task doesn't matter much at all
[2032] yeah but all of these uh data sets are
[2036] using the same data set uh so the data
[2039] sets are same even though even in the
[2042] architecture they use resonance 50 as an
[2043] architecture each of the moments no but
[2046] the the input diet for the object
[2049] classification is the indoor scenes
[2051] right but if it was instead imagenet and
[2055] maybe
[2056] the difference between
[2058] the model then it becomes the same model
[2061] as the one that was yeah yeah so uh if
[2064] if we use the imagenet then it'll
[2067] predict more classes which means it's uh
[2071] using
[2072] a different data set having a diverse
[2074] data set but in this sense that each and
[2077] every model that was trained on is on
[2079] the same data set so we can so it really
[2082] comes down to the tasks that were uh you
[2086] know you know that you know the task of
[2087] the model instead of uh the data set so
[2091] each each of them are just using the
[2093] same data set this uh yfccim uh data set
[2097] so
[2098] yeah I'm talking about like the takeaway
[2101] should the takeaway be that input diet
[2103] matters the most followed by task
[2106] based on the orange plot here or should
[2110] it be like if you have an impoverished
[2112] image diet then task matters a
[2114] noticeable amount is number two but if
[2116] you have a very nice image diet then
[2119] maybe the test doesn't matter that much
[2123] uh yeah so actually data set matters a
[2126] lot because uh that is the most I would
[2128] say because if we uh go down into this
[2131] study it's like they test out between
[2134] image that 1K versus 21k so uh and when
[2139] comparing those you would assume that
[2141] since 21k has like a lot more variations
[2144] and it's like a lot more so it's a large
[2147] state of that
[2149] um it should lead to a higher score but
[2151] that but there is actually no
[2155] significant increase between 1K and 21k
[2158] so uh that's just and obviously uh so
[2162] they've also compared I think they also
[2165] say that the image net 21k isn't
[2167] actually that much more diverse than
[2170] image that 1K right yeah is this larger
[2173] it's not diverse yeah yeah so it does
[2175] not actually uh so the so the quantity
[2178] actually is not reflecting off to the uh
[2180] you know the increase in score that one
[2183] might expect even in you know when they
[2187] compare language alignment which I'm
[2188] going to talk about so
[2191] yeah in comparing all the models with
[2193] meta Ai and they actually compared it
[2196] with the open airs clip the clip
[2199] performed the best
[2201] uh which obviously has the language
[2203] alignment uh but when compared to the
[2206] language alignment of uh you know this
[2208] the clip model of meta which was
[2211] released by meta it it is not actually
[2214] uh so so one interesting observation
[2217] over here is like if we uh if they
[2219] actually
[2221] if we actually see the click model of uh
[2224] meta uh who which has a language
[2226] alignment
[2228] it has a slight negative correlation
[2231] between the brain activity just a very
[2234] slight uh between the brain activity and
[2236] uh you know the language alignment but
[2239] open ai's clip performs the best and
[2243] that's the the author's claim that
[2245] that's not because the the because the
[2248] clip is language line it's because the
[2250] clip was trained on a data set which was
[2253] not released to the public like uh it
[2255] was first trained on like 400 billion
[2258] images which uh you know this highly
[2261] curated and propriety data sets of 400
[2263] million uh image Tech space so it's not
[2266] actually because they are language
[2267] aligned it's because uh they've changed
[2270] in such a good data set so it's so the
[2273] data sets that uh diversity and uh
[2277] actually matters a lot in like in the
[2279] conclusion they actually uh say that
[2282] there's actually no cleared metrics to
[2285] determine how do we have the best text
[2288] like the band's best diversity uh in a
[2291] model obviously we talk about ssim
[2294] scores and everything but that has not
[2296] been implemented into the model but
[2299] since uh into the data sets so seeing
[2302] the data set being such a high uh you
[2305] know indicator of how
[2308] predict how the trade predictivity can
[2310] be uh you know can be determined so that
[2314] is something what these authors are you
[2316] know suggesting people to work on is to
[2319] you know have more diverse data science
[2321] so a data set is clearly the biggest uh
[2325] you know biggest factor in data mining
[2327] the predictivity yeah
[2333] it makes it makes me think that like
[2335] maybe this is the way to
[2337] Quantified image diversity how diverse
[2341] was your uh input images for training
[2344] your model let's compare it to the brain
[2351] oh yeah yeah actually yeah
[2357] but then again for that we need a much
[2359] diverse data set to actually train the
[2363] model first
[2364] because these are models have trained on
[2367] imagenet and then they use the NSG data
[2369] set to actually pass on uh the images
[2372] and the voxels
[2374] uh so yeah it's it's all about the data
[2378] that it seems
[2379] so uh they're also used so it starts I
[2383] mean what were you saying there would
[2385] that work or not you think like the fact
[2387] that it's NSD yes that means that we're
[2390] using specific images but these plots
[2394] like the models were not trained on coco
[2396] or NSD
[2397] so they are like is it still a perfectly
[2400] fine proxy for quantifying the diversity
[2404] of the models in terms of the image
[2408] diet
[2410] I mean it should be the only the the
[2414] only reason uh they haven't trained
[2416] they're using NSD because we have image
[2419] and fmri pairs with NSD but they are not
[2422] essentially trained on all right so
[2425] that's the imagenet have the same cocoa
[2427] images because NHD just uses Coco images
[2430] right they don't okay so
[2434] I I mean
[2436] uh for inference
[2438] I I think for inference they are using
[2442] the images which the models haven't seen
[2444] which means that using a different data
[2447] set to test out whether the model has it
[2450] if has this uh image embeddings means
[2453] that yeah yeah so it's a good indicator
[2456] of how or if the image models are trying
[2461] their best to you know or if a model can
[2464] actually understand those uh or have has
[2467] you know can actually produce the image
[2471] latents which actually relates to an
[2473] image
[2474] like these images which are being used
[2476] to calculate the PSN score they're
[2478] actually not part of their training data
[2480] set so it's so I think yeah
[2484] it should work
[2485] if the model is working well which
[2488] the whole argument around this paper is
[2490] that we have good functioning uh
[2493] computer vision models
[2495] so yeah
[2498] yeah I'm just kind of curious about that
[2500] because it's like
[2502] you wouldn't think
[2504] in order to
[2506] quantify how good the input image
[2508] variation of all these different models
[2511] is would be to basically
[2514] take brain data from a separate National
[2517] scenes data set of cocoa images and then
[2520] somehow that boils everything down to
[2523] specifically the input image diet as
[2526] being the prime factor of like what's
[2529] causing the difference in Pearson scores
[2535] uh yeah
[2537] yeah
[2539] maybe there's like a more
[2540] straightforward way to measure image
[2543] diversity right I imagine there would be
[2545] but if there isn't then this would be a
[2547] kind of wacky way to determine who has
[2550] the best image variation of across
[2553] models
[2556] um yeah yeah I've never heard of a good
[2558] way to measure today
[2560] yeah definitely heard people talk about
[2563] it before
[2564] but this this paper mentions that there
[2568] is actually not a good way of like not
[2570] yet there is not a lot of uh people who
[2574] are actually talking about diversity
[2576] amongst the data side and there's
[2578] actually not
[2579] a way to actually calculate it so I'm
[2582] not actually sure
[2583] this is the first time I'm actually
[2585] hearing about
[2587] diversity within the data set yeah so
[2590] it's like yeah and one data set might be
[2592] bigger but maybe it's not better but
[2594] also a lot of these companies do not
[2597] open source their models so like you
[2599] have open AIS models you have anthropic
[2602] model I don't know all any sort of
[2604] closed model that you want to evaluate
[2606] who has actually the best data for
[2608] training like I guess this would be one
[2611] way to to do that
[2614] without having access to the actual
[2617] training images
[2620] and maybe maybe that's why Urban Air has
[2623] a piece that hit us that on which they
[2625] trained glimp
[2627] because it's so good
[2630] like it like it just because of their
[2635] training on that data it's like uh it's
[2638] better than all the models that that
[2640] were just trained
[2641] uh you know all the meta models that
[2644] were just trained on uh these other data
[2647] sets so
[2648] uh yeah
[2651] so like in in a language alignment it
[2654] basically doesn't matter if the images
[2656] are aligned with their uh you know their
[2659] captions
[2660] or just their captions so uh but before
[2664] that let me just get into the
[2666] self-supervised algorithms
[2668] which I kind of think is interesting so
[2672] they did they start with some uh
[2675] self-supervised algorithms which uh
[2679] so it's like simpler and bother twins
[2683] uh
[2684] to see how they compare with each other
[2688] um
[2689] so simpler was like pure self
[2692] supervision which uh and clip was like
[2697] pure language alignment and then there's
[2701] another model called slip which is
[2703] partly language alignment and partly
[2705] self-supervation so you know across all
[2709] three there were no substantial
[2712] differences between the Pearson scores
[2714] of all three uh models although there
[2718] was a slight decline a decrease in the
[2721] pure language trained uh you know the
[2724] clip
[2725] so there was just a slight decrease in
[2729] here not sure if that's uh significant I
[2733] don't think so you can see there is a
[2736] like a slight decline over here but all
[2739] in all these uh self-supervised models
[2743] they achieve the same person scores for
[2746] brain productivity
[2749] and so yeah so because of that the
[2754] authors you know came up with the
[2755] conclusion that the superior performance
[2757] of open ai's clipped is actually not
[2760] because of the language alignment
[2763] and it is mostly because of the private
[2765] data set that they were trained on
[2768] so I mean another yet again you know
[2770] indicator that the data set actually
[2772] plays a major role uh
[2776] and uh you know getting the screen
[2778] predictivity to work
[2781] yeah I think the result is super
[2784] interesting
[2786] and also kind of challenging for the
[2790] previous talk we heard uh
[2794] Arya
[2795] Arya Wang right yeah
[2797] work out in the paper
[2800] yeah that was pretty cool didn't like
[2802] that
[2804] but uh
[2806] I think there's another possible
[2807] explanation here which is the yscc
[2810] they did have to
[2813] right I guess but also the yfcc data set
[2816] might have bad captions like
[2819] foreign
[2823] if you start with a data set yeah sure
[2825] it's the data said where all three
[2827] models have been trained but if the
[2829] captions are not sufficient to train a
[2831] good clip model then it's not really
[2833] fair honestly I think
[2835] if you want to do
[2838] this is part of a larger point
[2842] but I think
[2844] this paper and also Aria's paper and
[2846] lots of these papers have a challenge to
[2849] deal with the fact that they're they're
[2850] all taking models off the internet and
[2852] not training their own models and so
[2854] they're all doing
[2856] they're all forced to do kind of
[2858] difficult confounded comparisons that
[2861] are not very clean like ideally you
[2863] would train every single model online to
[2864] be
[2865] or something like that some
[2868] recent data set and then do it and train
[2870] them all
[2871] with exactly the same compute budget
[2873] exactly the same team training them all
[2876] and do a really fair comparison but that
[2878] would cost a billion dollars
[2881] uh yeah they used around like 164 166
[2886] diff I mean actually they use 224 but
[2890] out of them six like 60 were on train so
[2893] they used around 160 models in the you
[2897] know pytots Imaging library to actually
[2900] get these results so in just getting
[2903] these results it it was around 1.8
[2906] billion regressions just imagine how
[2909] much if they actually had to train each
[2910] and every one of them
[2913] like even even in the footnotes they
[2915] mentioned to just to uh replicate all of
[2918] the results that we just mentioned it'll
[2920] take like uh weeks uh it'll take weeks
[2924] of training time on like eight RX 30 90
[2926] I'm like I can't even get my answer one
[2929] they need eight and then they're running
[2931] it for weeks and this is just to get
[2933] these results not to account for
[2935] training which for some of the models
[2937] take days so I think that was most
[2941] possible
[2943] yeah totally so I just think compounds
[2946] are part of the part of the game here
[2948] and no one is uh insulated against
[2952] compounds when they're using these
[2954] off-the-shelf models
[2956] yeah
[2959] what were you saying though about the
[2961] the
[2963] because the the reason why they talk
[2967] about the arya's paper
[2970] um specifically calling it out is
[2973] because I think in in arya's paper right
[2975] they talk about how like
[2978] you know the resnet 50 was where Alex
[2982] net uh whatever model that was was like
[2985] better at early visual areas and then
[2987] clip was way better at the higher level
[2989] visual areas and
[2992] um
[2993] like so like the but the comp well what
[2997] was it exactly that they call out for
[2999] that paper I'm
[3002] yeah so the issue as I understood it uh
[3006] is that it when doing comparisons with
[3009] openai clip there's a two possible
[3012] explanations one is that clip the model
[3015] framework is better or two the clip data
[3018] set is better you don't know which it is
[3021] since we cannot access the quilt data
[3023] set
[3025] I see so basically Arias was talking
[3028] about like using clip with language
[3031] image
[3033] it can be a better model but maybe it's
[3036] because of actually because of the image
[3038] data set and that's the difference the
[3039] images are richer
[3041] yeah yeah okay
[3044] but but in this case you have yfcc
[3049] honestly don't know if the captions are
[3052] good enough
[3056] and uh
[3059] if you have good captions which I'm sure
[3061] open I collected good captions I'm
[3063] probably lying to be has good captions
[3066] or whichever the you know the
[3067] state-of-the-art open clip model data
[3070] set trend on that you would ideally
[3073] take a data set that's good for clip and
[3075] then train a vision only model on that
[3077] data set and see what happens
[3085] yeah
[3086] [Music]
[3088] um yeah so basically it's like we don't
[3091] really know if these if they if these
[3095] models have have a good alignment
[3097] between image and
[3098] the text right
[3104] okay yeah yeah that's that's a fair
[3108] thing
[3110] um but yeah so all of this you know just
[3113] points so next they tested out uh
[3117] uh how does the input died or you know
[3121] the data sets differ with the brain
[3124] productivity and this is where the most
[3127] of their conclusions come from it's like
[3130] so they tested out imagenet uh
[3134] one K versus 21k and when they observed
[3139] no as I mentioned they observed no real
[3141] real effect uh on both crsa and V ersa
[3145] for uh when comparing these two data
[3149] sets even though you know 21k has like
[3153] uh a lot more images but it's not as uh
[3157] diverse as 1K or it's not more diverse
[3161] than 1K so they have very similar scores
[3165] so even if they have like
[3168] more classes and more images it is not
[3171] reflecting off to a better increase you
[3174] know better increase in this course
[3178] so uh yeah so the so it really just
[3182] means that the raw quantity of training
[3184] data does not necessarily lead to an
[3187] increase in productivity
[3190] um
[3190] and I mean yeah but even the 21k data
[3194] set is not as uh diverse as 1K so that
[3199] really that means that that that
[3201] probably explains why there was not an
[3203] increase uh in the scope
[3207] and apart from that they actually also
[3210] use the data sets which uh were focused
[3214] on object detection
[3217] um
[3218] so open images data set or uh you know
[3222] the you know the data sets which are
[3224] focused on scene so they use Place 365
[3227] for that and uh data sets which were all
[3231] based on the face
[3233] um
[3234] so there's vgg phase two and well the
[3238] results were pretty much as you would
[3240] expect there was a decrease in the
[3242] scores of uh in pain predictivity when
[3247] we are using data sets which are
[3248] specialized and for vgd phase two it was
[3252] even worse so
[3254] at least for this architecture which was
[3257] just a resnet 50 and these objectives
[3260] the visual diet is a substantial uh
[3263] indicator uh indicator and a substantial
[3268] variator in for brain productivity and
[3271] the diversity is one of the most
[3274] important thing in it so
[3278] uh later diversity in a data set uh
[3281] obviously proves that it is one of the
[3283] most important factor in determining the
[3285] brain productivity uh as confirmed
[3288] because they use these data sets and the
[3291] results for the universe uh and also a
[3294] thing to mention uh that these data sets
[3297] so like these open images and place 365
[3300] they are much larger data sets than
[3303] imagenet so
[3306] this again you know really proves that
[3308] the quantity of the images does not
[3310] really matter if they if the images are
[3313] not diverse uh like the data set is not
[3315] diverse so as you can see it's like 2.75
[3318] times 1.5 times they mentioned it but
[3320] this is still has a lower score than
[3323] than
[3325] yeah importantly though I this is all on
[3328] occipital temporal cortex which is like
[3330] a big swath of the brain
[3334] and I know that that includes regions of
[3337] the brain that are specific to objects
[3339] places faces
[3341] but it's not like they specifically
[3344] looked at rois of like specific brain
[3347] regions like
[3348] if you use a form face area para
[3350] hippocampal Place area mod healer kind
[3353] of areas of the brain that are known to
[3355] specialize in a specific kind of image
[3358] processing
[3359] I wonder if that would change things
[3365] okay so these V1 V2 V3 V4 which are the
[3370] visuals okay so they lie inside this
[3374] occipital temporal cortex right
[3377] OTC yeah it's all I think OTC is what
[3380] it's like in the figure you can see it's
[3383] basically visual cortex and yeah ventral
[3386] temporal so like the the very back of
[3390] the brain is going to be the early
[3392] visual cortex stuff but there's modular
[3394] high-level reasons of the brain like
[3396] visa from face area that are more you
[3399] know lateral underneath the brain
[3401] farther away from early visual cortex
[3403] that are very specific for processing
[3405] faces in that case
[3408] so if you isolated Justified brain
[3410] reasons and maybe having a model that is
[3413] specific to phases would actually be
[3416] more helpful
[3418] yeah it'll be interesting to see how
[3420] activations in each of the visual you
[3423] know leave on V3 V4
[3425] uh vary across different uh
[3429] you know different factors
[3431] right now I think they're just averaging
[3433] out just mentioning OTC
[3435] but they're averaging out across and
[3437] they're doing this kind of like weird
[3439] random projection thing which I don't
[3441] know if that's gonna kind of preserve
[3443] these modular representational things
[3447] that are known to be the case in the
[3450] brain
[3452] yeah
[3453] yeah we don't actually know which parts
[3454] of the ODC are actually being activated
[3459] um it's just averaging it out well to be
[3462] yeah
[3463] yeah it's establishing and out so
[3467] yeah it'll be interesting to see how
[3468] this varies across uh different rois
[3473] uh yeah
[3476] like imagine but that would be pretty
[3479] incredible to
[3481] see like okay this specific region of
[3484] the brain known to only process faces if
[3487] you use an image diet that it doesn't
[3489] really have that many faces in it but
[3491] it's very diverse what if that actually
[3493] has the better Pearson scores than the
[3497] yeah exactly yeah yeah right like that
[3500] would be kind of crazy maybe if you just
[3502] yeah maybe if we just use this place 365
[3505] degrees that maybe it just activates
[3507] some different parts of uh uh in a
[3511] different Roi which is not which you
[3514] know differs from let's say face and so
[3518] we yeah it can help us map out these
[3520] different rois which I think they're
[3522] already mapped out there's actually no
[3524] different parts of the brain uh activate
[3527] for different phases but this is like we
[3530] can track changes over time in terms of
[3532] data sets and different uh different
[3536] factors so yeah that is one of the
[3537] things we could actually look at I I
[3540] don't I'm not sure why they've just used
[3542] the whole OTC
[3544] what will they do in 1.8 billion
[3547] regressions maybe that's uh it's enough
[3549] to pick one swath of the brain
[3556] there's got to have been a paper or like
[3558] at least a poster
[3560] that uh compared models trained on face
[3563] only data sets versus General data sets
[3566] in terms of brand prediction performance
[3568] they must have done that I'm sure they
[3570] did that you think so like I don't know
[3572] if other papers have been this
[3574] scientific in restraining those models
[3577] that they're using in terms of like all
[3580] these parameters that they do a great
[3581] job in this paper of isolating like
[3584] image guide versus
[3587] um task versus
[3589] you know architecture
[3593] yeah I think
[3595] um
[3597] it is conspicuously missing I think
[3599] maybe they're like holding it out for a
[3602] separate
[3603] paper or something to do like a more
[3606] yeah I suppose
[3609] sorry boy it would be as simple enough
[3611] second paper for them to do they've
[3612] already got all the code in place to do
[3614] this on OTC right yeah which is kind of
[3617] uh
[3618] split it out by Roi
[3621] um yeah I'll look around see if see if
[3623] folks have done that I would expect
[3625] somebody in the Nancy camera store but
[3628] to have done that
[3630] it would make sense yeah
[3634] right so in the NSD data sets uh I know
[3638] we have these voxels available so do we
[3640] have can we make out which part
[3644] relates to which Roi is
[3650] like uh right now right now when I was
[3653] like looking for alcohol so we have like
[3656] three by
[3657] 39K uh size of boxes so are they
[3661] actually flat like are they actually
[3663] flattened or this is
[3665] how they are they have to be flattered
[3668] right for the sorry for the NSD data set
[3671] or the voxels flattened is that what
[3673] you're asking
[3674] yeah yeah
[3676] not initially no we have the the third
[3678] full 3d
[3680] Okay so
[3682] uh okay so after flattening it was like
[3686] three by 39K you know dimensions of
[3689] Matrix
[3690] okay so okay so when we have that 3D
[3694] thing you know when we have those in 3D
[3698] we can actually map out which part of
[3700] the boxes out of which rois right yeah
[3703] you can do it either way like they give
[3705] you for the natural scenes data set they
[3706] give you the rois so you can flatten the
[3708] rois the same way that you flattened the
[3711] brain and then just like do the indices
[3713] comparison to see which Vertex or which
[3717] Troxel corresponds to each and also in
[3719] the algonauts themselves they give you
[3721] files I think in the challenge space
[3723] where you're able to match the rois
[3726] accordingly
[3728] oh yeah I did see it I know
[3731] I mean yeah so if if they're already
[3733] doing this for OTC I think they can uh
[3736] get the similar results for each Roi
[3740] is assuming that we have we can we have
[3744] the data which correlates to each other
[3746] so I guess we have that
[3748] so
[3749] um but it's like that's sort of big
[3751] picture Point here is that they're sort
[3754] of saying that these models are not
[3757] really that important like all the
[3760] differences between these models of
[3762] architecture you know CNN versus
[3764] Transformer uh the specifics of the task
[3766] these don't really matter as much when
[3769] it comes to understanding brain like in
[3772] terms of being able to better predict
[3773] with an architecture that seems to fit
[3775] better with how the brain actually works
[3777] like a priority you might think cnns
[3779] would do better because that's more
[3781] similar to how brain hierarchical uh
[3784] like how the actual brain works but
[3787] that's not the case so it's sort of like
[3789] okay is there anything
[3793] usable with all of these models for
[3796] better understanding how the brain works
[3798] they find that the major thing is just
[3801] the image diet can
[3803] delineate which of the models is going
[3805] to predict better but that's not really
[3807] uh theoretically
[3809] exciting I suppose for us to better
[3812] understand the brain
[3815] you know but yeah but they came at that
[3819] conclusion that you know all it's only
[3821] that uh data said that matters because
[3825] they take the whole of this ODC and uh
[3829] they get they get its high
[3832] representation latents which it averages
[3834] out uh
[3836] the differences between each of the rois
[3839] so
[3840] just because vgg fail just because using
[3843] a vgd phase data set means uh you know
[3847] the correlations code actually decreases
[3850] doesn't actually make that doesn't tell
[3853] us that if uh it doesn't actually tell
[3856] us that you know the activations in the
[3859] regions of interest you know which uh
[3861] which have been known to correlate when
[3864] humans see the face are actually being
[3866] correlated are actually being activated
[3868] so they're just averaging out all of the
[3872] uh they're just averaging out
[3875] to get and generating these these
[3878] latents yeah
[3881] we they're doing this random projection
[3883] thing so it's not exactly averaging it's
[3886] not exactly our vision but how do we
[3889] know the variations within the OTC uh
[3893] when we have uh you know for getting
[3895] input variations like like the the
[3898] initial take from this paper is sort of
[3900] a pessimistic you know we're not really
[3902] learning that much about the brain from
[3904] oh yeah it's it's comparing the
[3906] different architectures of models but
[3907] maybe the reason for that is because of
[3910] what you're saying of like this is a
[3912] very broad analysis they haven't tried
[3914] looking at hierarchically like different
[3917] brain regions maybe you're you know your
[3920] this random projection thing or the fact
[3922] that you're doing it across a single
[3924] brain region is Maybe
[3927] muddling the results to give you that
[3929] cynical kind of take but oh yeah maybe
[3933] did more subtle kinds of probing of
[3935] specifics across the hierarchy of the
[3938] brain maybe then it turns out
[3940] you get a different result
[3943] yeah yeah yeah that's a good point it's
[3946] maybe because we're looking at the whole
[3949] holy seeds yeah because it's a very
[3951] pessimistic paper it's just uh
[3955] I like there is no relation between cnns
[3958] and Transformers uh just just a data set
[3962] and yeah uh maybe it's because we it's
[3966] just such a generalized study and not on
[3969] the basis of actual rois which I'm
[3972] really interesting to see if there are
[3973] actually papers which describe how
[3977] uh you know brain productivity in
[3979] certain Roi change in respect to
[3981] different
[3983] uh different data sets or different
[3985] images
[3986] uh yeah
[3988] I guess that's one of the main problem
[3990] the main
[3992] uh problems in Neuroscience to
[3994] understand which part of the brain gets
[3996] activated in response to which images
[3998] although I have read about some rois
[4001] which you know get activated when there
[4005] is a image and there's a different Roi
[4007] when there is the face in front of us
[4010] but we don't actually really know which
[4013] part of the brains get activated so
[4016] uh yeah I'm really interested to see if
[4018] there are other papers for you know
[4020] delving deep into this
[4025] um
[4026] yeah uh so
[4029] uh yes uh next up they actually tried
[4034] out a training if training actually
[4037] leads to a higher PSL score and I mean
[4040] obviously it does
[4042] um so out of out of you know like four
[4046] model is retested they also tested out a
[4048] model which is not being trained and
[4050] just randomly initialized and obviously
[4053] it has a uh the one which is not which
[4055] was not trained had a very low score
[4060] um there's a graph okay so it's actually
[4064] this is one of the one of the crafts I
[4067] wanted to focus on it's like all the 126
[4071] models that were just tested they had
[4075] this is what I mentioned earlier they
[4076] had a they had a Delta of PS of around
[4078] 0.1
[4081] this drop that you mentioned is mostly
[4083] because of the data set because uh and
[4089] it drops down to an area where the
[4091] models were untrained
[4094] so
[4095] at most it just it just seems to me it's
[4098] like most of the time it's the data set
[4100] uh that's the significant
[4103] you know character in determining the
[4106] brain productivity
[4107] uh right so challenge up real quick
[4111] yeah I'm going to kind of challenge us
[4113] looking at this figure I get that their
[4115] messages that the data set is the main
[4117] factor but this is not obvious from the
[4119] figure
[4120] I think like
[4122] all these black uh markers are from the
[4125] imagenet right
[4128] yeah and then then you got like two
[4130] markers from places and bases and then
[4132] you've got a bunch of like uh these
[4136] whatever tan markers from tusconomy
[4139] um
[4141] and so the the claim comes down to this
[4144] steep drop that we see around the
[4146] tesconomy models
[4148] is showing
[4150] is supporting the data set is important
[4152] claim
[4155] these these plus economy models Edge is
[4158] not very well trained
[4160] and the task is not very good
[4164] or audit absolutely
[4167] you know correlates that the task
[4169] actually does matter uh when data mining
[4172] bring productivity so if there is
[4175] another if there is a semantic
[4176] segmentation that if if a model has been
[4179] trained on semantic segmentation it
[4180] those learnings does not turn so very
[4184] well into predicting the brain
[4185] productivity so although that's also a
[4188] factor that these models that that the
[4191] tasks of these models actually does
[4193] matter
[4195] um it's also the diet so yeah uh you you
[4199] cannot arbitrarily say from this graph
[4201] that it's just the model it's because
[4204] there are different models
[4206] as well
[4208] um yeah especially for data sets used
[4212] there's like countless models and
[4215] architectures and tasks and only four
[4216] data sets I would like to see one model
[4221] trained on different fractions of
[4223] imagenet
[4225] although their argument for only using
[4228] image net to compare all of this is just
[4230] like they wanted to keep everything same
[4233] and just have one thing different you
[4236] know as an inductive bias so at least so
[4240] since they're comparing all of these
[4242] only on image that data set
[4246] they're hoping that whatever the reason
[4248] and changes in the PSN score is
[4250] attributed to actually is attributed to
[4253] the
[4254] types of models and their diet and the
[4258] types of their tasks and not actually
[4260] the data set but
[4263] although we've seen in the autograph it
[4265] means that the data set actually uh also
[4268] matters
[4269] so yeah
[4272] to conclude the data set point when
[4274] there's only four four
[4277] data sets
[4279] uh well to be fair these data sets
[4283] they're not very diverse
[4285] so you can't even compare these data
[4288] sets to image which has like a lot of
[4290] images they're like very focused data
[4293] sets focusing on scenes of faces
[4297] so
[4299] what about open images
[4303] uh no it's just is this based focused on
[4307] the objects so I it's just it's based
[4311] focused on object it's not as diverse as
[4314] image now although it is much larger but
[4317] not as diverse so you can't really even
[4320] compare with image
[4322] I don't know I think open images was
[4324] supposed to be a good data set from
[4325] Google with like a lot of
[4328] good stuff about it
[4332] is
[4339] because this paper mentions that it's an
[4342] object focused
[4343] uh data set and not uh not like a
[4353] by itself like the golden divers
[4359] you know there's plenty of problems with
[4362] image that too and also they do have a
[4364] focus I think on objects in English that
[4367] like maybe not to the same degree but
[4369] usually there's a focal object in images
[4373] and image now right it's not usually a
[4375] cluttered scene of several different
[4377] objects
[4379] yeah very true
[4381] like plot the heat map with the bounding
[4383] boxes
[4389] so is there a data set which is like
[4391] actually balanced with everything
[4394] and that's a better data system image
[4396] now
[4398] no I mean if you want real like
[4401] diversity
[4402] it kind of like depends like I don't
[4406] know does it please rely on 2B is that
[4408] diverse because they're basically just
[4410] scraping everything
[4412] right
[4414] yeah I think that one's good
[4416] is lion to be just is yeah I guess one
[4422] of the things about lion to me is just
[4424] because it's like
[4425] it's the sheer size of it I don't know
[4427] if it is
[4430] yeah it's like they have like two
[4432] billion images but are these are they
[4434] diverse enough again this paper actually
[4437] says there is actually no way of uh
[4440] calculating how diverse a data set is
[4443] that is something uh that people need to
[4446] work on
[4447] and I think that yeah
[4450] do you know V2 paper does a good job
[4453] like trying to address this issue they
[4456] construct a new data set they take care
[4458] to try to make it like quote diverse in
[4461] some way
[4462] um
[4463] they come out with a data set with like
[4465] 140 million images so not the biggest
[4468] data set
[4470] but well curated and the chart they're
[4473] aiming for diversity and did they use
[4476] Dino in this paper
[4479] um but it isn't a deep dive GitHub which
[4484] the author made
[4486] so
[4487] um
[4488] I'm not read a single incidence of Dino
[4493] why didn't they report Dino if it's in
[4495] the GitHub for the you know they have
[4498] their own Deep dive GitHub that
[4500] automates using all these models and I
[4502] looked and and Dino was in it
[4504] as well as a few other models that I
[4506] think are not in the paper
[4509] it could be a difference of the guy now
[4512] B1 versus B2 V2 is pretty recent
[4517] ly different
[4522] yeah yeah
[4524] [Music]
[4527] they also tested out if
[4532] the representations so like if a model
[4536] so they also texted out if the effective
[4541] dimensionality plays a part in uh
[4544] getting the brain predictivity uh
[4545] getting a higher PSN score on brain
[4547] predictivity basically meaning if uh
[4551] these model representations you know if
[4555] they have a file if if these
[4559] uh so okay so the models latents does
[4563] this have to does the complexity of a
[4564] model have to do with uh you know how
[4568] accurately it predicts the brain
[4569] predictivity so they did test out
[4573] uh the you know to test out this
[4577] relationship between Ed and uh brain
[4580] predictivity
[4582] although uh yeah so
[4586] um so there was no among the trained
[4589] models you know which were which were
[4591] already trained there was no real
[4593] correlation
[4594] and
[4596] and Unchained models which uh you know
[4599] they don't have highest scores anyway
[4601] there was actually a slight negative
[4603] correlation but it's not statistically
[4605] significant
[4607] so
[4609] although it does mean that having a more
[4612] complex uh embeddings lead to a higher
[4616] crsa and we ersa score as mentioned in
[4620] these graph but it's mostly because of
[4624] uh it's not because they're more complex
[4626] it's because uh the models that are
[4630] being used to compare that thing uh they
[4634] are either trained or untrained so if
[4635] there are trained models they have a
[4637] higher RSS code than uh the models which
[4640] are on train so it's actually not
[4641] related to having a much you know a more
[4644] complex or a higher latent space so uh
[4649] if this so there is no actually real
[4651] correlation on effective dimensionality
[4653] as well
[4655] so I mean as as you just go down there's
[4658] no
[4659] correlation and most of the
[4663] things
[4665] so yeah it's right here on the graph
[4669] so I mean uh moving on next they also
[4672] tested out classification accuracy and
[4675] this is also something I mentioned
[4676] before
[4678] um so this time they tried the models
[4680] which have a higher accuracy scope
[4684] so so like the previous work suggested
[4687] that there will be a higher correlation
[4690] if these models have a higher accuracy
[4692] scores but the newer study said that
[4694] there is actually no correlation and
[4697] even even with this uh even when these
[4700] authors tested it out using comparing
[4703] the models which have scored like in the
[4705] top one percent of image net 1K uh
[4709] had little to no correlation uh between
[4712] the classification accuracy versus the
[4714] brain productivity
[4716] um
[4717] so yeah
[4719] even with you know testing out with the
[4721] models which had a wide range of
[4722] accuracies there was a limited range of
[4726] brain productivity so even though some
[4729] of the models might have more from let's
[4732] say 70 to 80 percent accuracy even if
[4735] the range of accuracies have you know
[4737] there have a broad range uh
[4741] the the brain predictivity scores were
[4744] not differing that much so it's so even
[4748] the classification accuracy at some
[4750] point is not a very good indicator of
[4753] predicting you know the brink uh
[4756] predictivity source
[4759] they also tested out uh the number of uh
[4763] images uh the number of trainable
[4765] parameters so if there are if there's a
[4770] regular state of increase in the
[4772] parameters if that's going to be
[4775] you know factor for brain productivity
[4777] but they uh for they got of various
[4782] amounts of irregular set of patterns so
[4785] if there was this increase in trainable
[4787] parameters there was a decrease in crsa
[4790] score but a non-significant increase in
[4793] V erss score so there's not a
[4796] consistency in the number of trainable
[4799] parameters so it was like I don't so I
[4804] the number of trainable parameters also
[4805] does not really uh matter in terms of
[4808] getting the brain productivity scores
[4811] so yeah
[4815] um
[4817] then uh
[4819] they you know After figuring it out like
[4823] after getting all of this
[4826] uh wait let me see here so they also did
[4828] model to model comparisons uh which was
[4831] basically
[4833] a study of
[4835] comparing different models If he if they
[4837] can actually
[4838] uh identify you know okay give me a sec
[4843] um
[4845] wait where was that uh
[4851] yeah uh so comparing more to model
[4854] comparison was mostly about uh comparing
[4857] if a particular model uh if like the two
[4860] particular models have the same
[4862] understanding or a similar understanding
[4864] of uh the images
[4867] basically when they compare you know the
[4870] most brain aligned layers of the top 124
[4874] uh brain predictive models
[4876] there was a vast variety of similarity
[4879] between these models uh even though
[4882] these models were like let's say from
[4884] cnns to uh
[4887] Transformers they were getting at the
[4890] same representation space even though
[4892] they had a very different architecture
[4898] um and yeah so and these authors also
[4901] mentioned here that
[4902] although these you know what we've
[4906] talked about number of trainable
[4907] parameters the types of models also
[4909] matter what also matters is you know the
[4912] metrics that we are using so crsa versus
[4915] voxel encoding RSA
[4918] uh because as I mentioned before it's
[4921] like 31 of the variation across the
[4923] voxels in the NSD data set are being ex
[4926] is being explained by uh crsa but over
[4930] 79 is being explained by the ersa so
[4933] it's definitely the re-weighting of uh I
[4937] need to get more deeper into like what
[4939] rebating actually works and how it
[4941] actually works but this is definitely
[4943] you know playing a major part in uh
[4946] explaining the variance across uh in
[4949] this NSC data set and yeah that's what
[4952] the whole paper is all about
[4953] uh in the chest and this is like uh
[4958] there are parameters which we use to you
[4961] know improve the accuracy of a deep
[4962] learning model and we would think that
[4965] these parameters would also improve the
[4967] brain productivity scores but most of it
[4970] actually does it it's mostly about uh
[4973] the data set
[4974] in this case so yeah that that was the
[4977] whole paper
[4981] yeah thank you so much for watching us
[4982] through the paper me here great um
[4984] overview of everything yeah
[4987] I mean yeah even I I wanted to Deep dive
[4990] into this paper anyways I was like I'll
[4992] do it and still have to you know learn
[4995] more about how they rebate those
[4998] so yeah there's they stop
[5001] yeah and I I think we there are
[5003] definitely some open questions here
[5005] where I don't think we should be totally
[5008] pessimistic about the possibilities of
[5012] you know they're being actually
[5014] interesting connections between
[5016] different kinds of models and mapping
[5018] them to the brain
[5020] oh yeah definitely we should actually
[5022] Explore More how it uh varies across
[5025] region uh you know regions of interest
[5027] if anything
[5029] yeah yeah
[5032] they're really really interesting paper
[5035] wow
[5037] yeah I agree this was a really high
[5039] quality paper I'm glad that uh you know
[5042] they were able to tackle this and it's
[5043] not an easy effort to get all of these
[5046] memories working
[5048] it's pretty crazy actually that they got
[5051] this to work
[5053] yeah
[5055] you just read uh replicated it will take
[5058] like weeks to you know just get it done
[5061] so yeah oh yeah totally
[5066] all right any any last thoughts from you
[5070] or Connor
[5075] all right I'm good and thank you thank
[5077] you so much for walking us through the
[5078] paper it's really fun to go through it
[5080] yeah no worries it was mostly for uh I
[5085] wanted to understand this paper so might
[5087] as well
[5089] so that's all
[5091] right yeah thanks so much
[5093] see you guys around
[5095] yeah see ya see you Monday
