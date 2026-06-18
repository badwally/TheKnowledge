---
schema_version: 1
id: yt-TBjdvjdS2KM
type: youtube
title: Similarity of neural network representations revisited
url: https://www.youtube.com/watch?v=TBjdvjdS2KM
authors:
- LLMs Explained - Aggregate Intellect - AI.SCIENCE
ingested_at: '2026-06-02T03:03:06Z'
content_hash: sha256:6e5c01392223cf850e33880d8e67c9b289f4699ceb34f8c922b6c38407d4243a
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: LLMs Explained - Aggregate Intellect - AI.SCIENCE
  channel_url: https://www.youtube.com/@ai-science
  duration_seconds: 1286
  caption_track: fetched
  snippet_count: 512
filter:
  score: 0.75
---
[19] all right so my name is Simon Kornbluth
[22] I'm a research scientist at Google brain
[25] and today I'm going to present our paper
[27] similarity of neural network
[28] representations revisited this paper was
[32] previously presented at ICML this year
[35] and its joint work with Mohammed or Uzi
[38] Hong luckily and jeffing so the
[42] motivation behind this work is that it
[44] would really be great if we had a way to
[45] understand the representations of
[47] trained neural networks
[48] so why train neural networks why not
[51] just study learning algorithms well so
[54] the problem is when we train a neural
[55] network there's an interaction between
[57] the learning algorithm and some
[59] structured training data we don't know
[61] this structure of the training data so
[64] there's some limitation to what we can
[67] understand about how this trained in
[68] neural network is going to act based on
[71] our knowledge of the learning algorithm
[73] alone ultimately we need to study
[75] something that consists of both the
[77] learning algorithm and the data and so
[80] one way to do that is to try to look
[82] inside the trained neural network and so
[85] one approach to understanding a train
[86] neural network is to look at its
[88] representations and in particular we can
[90] think about ways to compare the
[92] representations of the trained neural
[93] network and this is an approach that has
[95] been very successful in neuroscience
[97] which is what my background was
[99] originally in so I want to start by
[102] introducing kind of what is a
[104] representation so for the purpose of
[107] this work when when I say representation
[109] what I really mean is a matrix and the
[112] columns of this matrix are some set of
[115] features so for example responses of
[118] neurons in some layer of some neural
[119] network and the rows of this matrix are
[122] examples so we passed some data set
[124] through the neural network we get the
[127] responses of all the neurons we stack
[129] them up into a matrix and this is our
[131] representation so I also want to say
[134] mathematically it's simpler to think
[136] about this when you Center these
[137] features so
[138] you subtract the mean across all the
[140] examples so that's something that we do
[141] and all the math throughout this talk so
[146] because we're comparing representations
[148] we really need two matrices X and y and
[151] these represent responses in layers may
[155] be of the same neural network may be a
[156] different neural networks but it's
[159] important that the examples here are
[161] aligned so the number of rows in these
[163] two matrices is the same and each row
[165] represents the same example but the
[168] number of features can be totally
[169] different there's no requirement for any
[171] kind of alignment between the neurons so
[175] next let's kind of think about what
[177] similarity means so the the simplest
[179] definition of similarity between vectors
[182] is just a dot product but we also extend
[187] this idea to other kinds of inner
[189] products so we can replace the dot
[192] product with positive semi definite
[194] kernels so now moving onto this idea of
[198] how to compare representations the the
[201] simplest way of comparing
[203] representations that we can think about
[204] is we just take every possible pairing
[208] of features between the two
[209] representations and we just measure
[211] similarity between them so we we take
[212] their dot product and if we do that we
[215] get this matrix X transpose Y there on
[217] the right but there's another way we
[220] could think kind of intuitively about
[222] comparing these representations which is
[224] for each each of these neural network
[226] layers we can take the dot product
[228] between all possible pairs of features
[230] so we can measure or put all possible
[233] pairs of examples so we measure
[235] similarity between the examples and not
[237] the features and this gives us this
[239] examples by examples matrix X X
[242] transpose it measures the inter example
[245] similarities according to this neural
[247] network layer so in machine learning
[249] sometimes people call this a gram matrix
[251] in neuroscience we would call this a
[253] representational similarity matrix so if
[256] we want to compare two of these
[257] representational similarity matrices
[258] then the easiest way to do that is just
[261] reshape the representational similarity
[264] matrix into a vector and then take its
[266] dot product with another reshaped
[268] representational similarity matrix yeah
[271] is there kind of like a nice
[272] interpretation of X s transpose because
[275] X transpose X is like the correlation
[278] between features right but this is
[279] coalition between individuals yeah so
[283] every element of this matrix is the dot
[286] product between one example and another
[287] example according to the neural network
[290] representation okay yeah I'm happy to
[299] return to it later okay so it turns out
[302] that actually these two ideas are kind
[304] of the same thing so comparing the
[306] features here if we do in a specific way
[308] if we take the dot products between all
[311] possible pairings of features we square
[313] them and then we sum them up that's the
[315] same as taking the dot product between
[317] these two reshaped in our example
[319] similarity matrices and to turn this
[322] into a similarity index we we want to
[324] normalize it and the normalization does
[326] two things first of all it makes this
[328] invariant isotropic scaling so we don't
[331] want it to be the case that the
[332] similarity changes if we just make one
[334] of the representations bigger and it
[337] also gives us a number between 0 and 1
[339] which is convenient to think about and
[343] it turns out we aren't the first people
[345] to come up with this idea and actually
[348] it's been rediscovered several times
[350] under several different names so in the
[352] psychology literature it's known as
[354] Tucker's congruence coefficient and more
[357] recently in the machine learning
[359] literature kind of a generalization
[361] involving kernels has been named
[363] centered kernel alignment and I want to
[365] talk a little bit more about how to get
[368] this generalization that uses a kernel
[370] in place of the dot product so the idea
[372] is very simple we have these these
[375] representational similarity matrices xx
[377] transpose and YY transpose and we just
[380] replace those with centered kernel
[381] matrices K tilde and L tilde so
[384] basically we take the kernel we compute
[387] the kernel between all possible pairs of
[389] examples that gives us a matrix and then
[391] we Center the rows and the columns of
[393] that matrix and that's kind of
[395] equivalent to centering the features in
[397] the linear case
[400] so having come up with this similarity
[402] index the next question is how do we
[405] know if it's any good and this is
[406] actually like a very difficult question
[408] to answer because there's not really any
[411] single definition of similarity that
[414] makes sense for all problems it's kind
[415] of like similarity can mean whatever you
[418] want it to mean and really what matters
[421] is what you're gonna use it for so one
[426] thing that we feel like is maybe the the
[428] minimal thing that you can ask for for a
[430] similarity index that you're using to
[431] compare neural network representations
[433] is if we have two neural networks that
[436] are architectural II identical but
[438] they're trained from different random
[439] initializations we want to take a layer
[442] from one network and measure its
[443] similarity with all the layers of the
[445] other network and we want it to be the
[446] case that the most similar layer is the
[448] layer that actually corresponds
[450] architectural II so in this example if
[452] we take the third convolutional layer of
[454] a neural network we want it to be more
[456] similar to the third convolutional layer
[458] of another neural network trained from a
[460] different ground of initialization than
[463] to any of the other layers of that
[464] network and so we can actually perform
[468] the sanity check and if we do this with
[470] the linear version of CK which is what I
[473] was showing you earlier we get a plot
[475] that looks like this so here the x and y
[478] axes are the layers of two different
[481] neural networks that are architectural
[483] II identical but trained from different
[484] random initializations and brighter
[486] colors here indicate greater similarity
[488] so you can see that the diagonal here is
[491] brighter than the off diagonals that
[492] indicates that the architectural
[494] corresponding layers are more similar
[496] than the non corresponding layers so
[498] beyond this plain CNN that's trained on
[501] C 410 we can also look at a resident
[503] trained on C 410 and a transformer
[506] that's trained to perform English to
[507] German translation and we can see that
[509] in each of these cases CK passes this
[513] sanity check the diagonals here are
[515] brighter than the off diagonals and we
[517] can recover the architectural
[518] correspondences based on similarity
[520] alone we can also compare CK to
[524] approaches that have previously been
[525] proposed to measure similarity between
[528] neural network representations so here I
[530] show representational of the
[533] that similarity between layers using
[536] canonical correlation analysis and
[538] singular vector canonical correlation
[539] analysis which are kind of ways of
[542] measuring similarity that have been used
[543] in previous work and you can see here
[548] that you don't see this bright diagonal
[550] and actually like a lot of the layers
[552] are very similar to either the first
[554] layer or the last layer of the network
[555] and that kind of indicates that there
[557] are problems with these methods and we
[560] can also take this sanity check and we
[562] can make it quantitative by saying okay
[565] we've got ten neural network strain from
[567] different random initializations if we
[569] take all of the pairs and we take a
[570] layer from one and measure its
[572] similarity with all the layers from the
[574] other how often is it that the layer
[576] with maximal similarity is the
[578] architectural corresponding layer the
[580] architectural corresponding layer and if
[582] we do that you can see with CKA we can
[585] recover the architectural
[587] correspondences with over 99% accuracy
[590] but with these other previously proposed
[592] methods the accuracy is much lower and
[594] so you might be wondering based on these
[598] results what is canonical correlation
[600] analysis and why have people proposed to
[604] use it previously to measure similarity
[606] between neural networks and why does CKD
[608] seem to work so much better and so
[611] mathematically actually there's a very
[613] nice relationship between canonical
[615] correlation analysis and CK so the idea
[618] behind canonical correlation analysis is
[621] that we compute this first CCA
[623] correlation by finding some linear
[626] combination of the features from X and
[627] linear combination of features from Y
[629] such that their correlation is maximized
[632] and the number that comes out of that is
[634] this first CCA correlation we can
[637] compute further CCA correlations by
[640] doing exactly the same thing with the
[642] restriction that these new linear
[644] combinations of features have to be
[646] orthogonal to the previous linear
[648] combinations of features so that's
[650] that's how CCA works it turns out to get
[655] a similarity index from CCA you can sum
[658] up the squared CCA correlations and
[660] divide by the total number of CCA
[662] correlations which is the number of
[663] features in the smaller representation
[667] and if you do that it's equivalent to
[671] taking the dot product between all
[674] possible pairings of principal
[676] components of X&Y with the principal
[678] components normalized to unit length and
[680] then again dividing by the number of
[681] features in the smaller representation
[684] so you can already see that this looks
[687] kind of like CK but we can also write CK
[691] in terms of the normalized principal
[693] components the eigenvectors of XX
[695] transpose and YY transpose and if we do
[699] that you can see that the main
[701] difference is that in ck a were waiting
[703] the dot products by the amount of
[705] variance explained by the principal
[707] components so CK is placing greater
[709] emphasis on similarity between these
[712] components that are responsible for more
[715] variance in the original representation
[718] so that's all the math for this talk but
[721] I have a few more kind of interesting
[722] empirical results to show you so the
[725] first thing is that we can use CK to
[727] measure similarity between architectures
[730] but between different architectures so
[732] here on the Left I have neural networks
[735] with different numbers of layers so a
[738] neural network with 8 convolutional
[740] layers 10 total layers and a neural
[742] network with 18 total layers or 16
[745] convolutional layers and you can see
[747] that if you measure similarity it's kind
[750] of like in the deeper network the new
[752] layers are inserted in between the old
[753] layers in terms of what the
[755] representations look like and you see
[757] there's still a diagonal in this plot
[760] even though the 18 layer network has
[762] twice as many layers on the right I'm
[764] measuring similarity between a 10 layer
[766] plain CNN and a 14 layer ResNet and
[770] again you can see that there's some
[772] architectural similarity between the two
[774] networks so finally we have this kind of
[778] serendipitous finding of that that kind
[781] of demonstrates what CK can tell us
[783] about what goes wrong when we train a
[786] neural network and it doesn't behave as
[788] we expected so we have this 10 layer CNN
[792] with 8 convolutional layers and it gets
[794] 94.1% on c for 10 if we make it twice as
[798] deep when it gets 95
[800] on C 410 so this is kind of the typical
[802] deep learning story you just make it
[804] deeper and the accuracy goes up but the
[807] problem is if you make it four times e
[808] power a times d for the accuracy
[810] actually goes down and so you could try
[813] to explain this in terms of like maybe
[815] there are vanish ingredients maybe
[817] there's something wrong with the
[818] training but you can also just directly
[820] look inside the training neural network
[821] and see what's gone wrong and so if we
[824] measure CK this time between layers of a
[827] single trained network in each of these
[829] plots so we no longer are using pairs
[832] trained with different random
[834] initializations now it's just one
[835] network you can kind of see what's gone
[837] wrong and this these really deep
[839] networks so if you look at the two
[841] layers that the two networks on the left
[843] you can see that the representations are
[845] kind of iteratively refined throughout
[847] the network and each layer is really
[849] only similar to the layers directly
[851] around it but these deeper networks
[853] which actually have lower accuracy you
[856] can see that there are entire chunks of
[858] the network that all have very similar
[859] representations and we can verify that
[862] CK actually gives us an accurate idea of
[865] how the neural network operates by
[867] training a logistic regression
[868] classifier on each of these layers
[870] individually to perform the original
[872] classification tasks and if you do that
[874] you really do see that in that very deep
[876] network on the right the accuracy
[878] plateaus less than halfway through the
[880] network suggesting that there really is
[882] no meaningful refinement of the
[884] representation happening in that second
[887] half of the network so that's all I have
[891] for today thanks for listening to the
[893] talk and if you're interested in code or
[895] in reading the paper you can go to our
[897] website CK similarity dot github that IO
[901] Thanks
[903] [Applause]
[904] [Music]
[913] um-hm
[914] which I write amiss at the beginning but
[916] I think you were motivated something as
[919] we won't find the correlation between
[921] examples in the training set as opposed
[924] to correlation between features yeah so
[928] so actually I think this is the the
[932] slide where you ask the question yeah so
[935] you can think about how do we measure
[937] the similarity between the
[938] representations of two examples and you
[940] can think about like maybe we can
[942] compare representations by measuring
[944] similarity of similarities between
[946] examples rather than doing something
[948] explicitly in feature space hmm and so
[951] that that's the idea behind this method
[953] but it ends up being the same thing as
[956] just measuring similarity in the
[957] original feature space at least if
[959] you're doing it with the dot product and
[962] this metric for your similarity they
[965] developed I guess like it is just one
[967] possible magic right yeah yeah so
[970] especially like people go back to the
[973] slide with a bunch of math so if you
[975] look at CKA there you can imagine like
[978] there are different possible weightings
[979] of the dot products between the
[981] principal components there and there's
[983] actually but one way to come up with the
[986] similarity index with different readings
[987] is to use regular eyes CCA instead of
[990] CCA or CK and we actually show that that
[993] kind of interpolates between the two in
[995] the paper disappear views resident the
[1008] residual layers yeah so we actually have
[1010] a
[1011] later ResNet in the paper and it doesn't
[1014] have this problem like it doesn't have
[1015] this issue of having entire
[1018] representation is we haven't tried
[1041] working with quantize networks and
[1043] everything here is just with
[1044] off-the-shelf standard real-valued cnn's
[1056] transformer versus very short diagonal
[1059] it's an interesting yeah the contrast is
[1064] very interesting do you have any
[1065] intuition as to why so resonant you seem
[1069] to have a I mean that maybe we can guess
[1071] you have a wider sort of diagonal I
[1073] maybe because it's propagating
[1075] information back I just wanted to know
[1076] if you have any especially for
[1078] transformer why is it more dispersed yes
[1081] so we have the so that's former and the
[1085] resonant have residual connections and
[1087] for a transformer you can also see that
[1089] there's kind of this funny pattern where
[1091] every other layer is similar and the
[1093] reason for that is that in the
[1095] transformer the the architecture
[1098] alternates between these like self
[1102] attention and feed-forward Network sub
[1104] layers and you can see that the self
[1106] attention layers are similar to other
[1108] self attention layers and the
[1110] feed-forward network layers are similar
[1112] to other feed-forward network layers but
[1115] there's less similarity even between
[1116] adjacent feed-forward network and self
[1119] attention sub layers walking through
[1125] depth
[1125] transport networks are more less
[1127] distinct from chat the layers are less
[1129] distinct from each other
[1131] in that sense yeah maybe I mean I think
[1134] that's true of all residual networks
[1136] like there at least if you measured them
[1138] with this similarity index you kind of
[1140] see that there's not as much refinement
[1144] if
[1144] you use the representation after the
[1146] residual connection
[1151] you showed accuracy for for the measures
[1155] but it isn't because a number of seats
[1157] always balance because a number of
[1159] features and examples are always
[1161] balanced which which so when you yes
[1164] this one this one yes
[1165] Syria to make sure usually with accuracy
[1168] in normal missionary task yes is that
[1170] fits in balance it doesn't really
[1171] reflect the performance yeah over here
[1174] everything seems to be balanced is it
[1176] because it what is that like yeah so
[1179] we're measuring accuracy of these two
[1181] different methods on the same set of
[1183] CNN's so we train 10 CNN's for different
[1187] random initializations and then we just
[1188] apply all of these methods to that set
[1190] of CNN's you back to the first one
[1202] don't miss the similarity between the
[1206] sub similarity between Mike Blair 7 I
[1207] think me and Larry 9 may seem like two
[1214] previous layers yeah but don't you like
[1217] norm everything so when you be the same
[1220] [Music]
[1222] so so I can kind of tell you the
[1225] explanation for why that is basically
[1228] when you have two different architecture
[1230] identical networks trained from
[1232] different random initializations
[1234] it kind of seems like as you go through
[1237] the network the representations become
[1239] more dissimilar and the reason for that
[1243] seems to be that like so I can tell you
[1246] one way to fix this which is if you make
[1248] the networks really wide then all of the
[1250] layers end up being very similar to each
[1252] other so it seems kind of like there are
[1255] differences between the different
[1256] initializations that accumulate over the
[1258] the layers deep network is expected of
[1265] like diverging similarity yeah
[1267] like shorten wide and colleague eight
[1268] yeah thanks for the question that's the
[1272] plan we do together
[1274] I've talked less thanks Simon thanks
[1283] [Music]
