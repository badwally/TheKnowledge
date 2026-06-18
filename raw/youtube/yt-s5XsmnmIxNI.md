---
schema_version: 1
id: yt-s5XsmnmIxNI
type: youtube
title: Predicting brain activity using Transformers - Hossein Adeli
url: https://www.youtube.com/watch?v=s5XsmnmIxNI
authors:
- Hossein Adeli
ingested_at: '2026-05-30T21:59:47Z'
content_hash: sha256:126cfc7215c344fa4a42d02f5be7463e56e25e228a18e81be7523d79d36891da
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: Hossein Adeli
  channel_url: https://www.youtube.com/@HosseinAdeli
  duration_seconds: 960
  caption_track: fetched
  snippet_count: 393
filter:
  score: 0.7
---
[0] Thank you for the introduction.
[4] So [clears throat] I want to first start
[5] by talking a little about why we
[7] participated in the challenge. So a
[10] belief that is shared by a lot of people
[12] in this room is that and and we really
[15] strongly believe in that is that deep
[17] neural networks provide us a
[20] computational uh language to form these
[23] hypotheses about different brain
[24] mechanisms. Um these hypotheses could
[28] differ in their architecture, in their
[30] uh diet of the data that they get, in
[32] their learning objectives. But in order
[34] to really extract insights from these
[37] models, we need robust ways to compare
[40] them with brain activity with behavioral
[43] data in order to really adjudicate among
[46] them. Now, Algonaut provides this
[49] opportunity to take out a really strong
[51] bias out of our modeling practice, which
[53] is accessing the test data. By by
[56] withholding that test data, you really
[59] um prevent this bias to to creep into
[62] your analysis. Um, also the reason we
[66] participate is that because the
[67] development kit, the tutorials, the uh
[70] uh different videos that they were made
[72] were very well put together like it
[74] really made us very easy. So I recommend
[77] to people to really check out the
[79] tutorials even if you're not interested
[80] in the challenge itself. Um yeah for
[83] these reasons we participated and we
[84] think this is an important initiative.
[88] So to our approach there is a recipe for
[91] predicting neural activity which is well
[94] you have an image or other sensory
[96] modality you you convert that you encode
[98] that in certain features then you take
[101] those features and you map them to fMRI
[103] or other neural activity. Now it stands
[107] to reason that what you use to encode
[109] would be the best performing computer
[111] science model. It would be CNN's or uh
[114] transformers or an ensemble of models.
[117] However, these are large dimensions.
[121] So a lot of people would use PCA or
[123] other approaches to reduce the
[125] dimensionality. Then you would read uh
[128] uh train a regression on top of that and
[129] get noral activity.
[132] We are using also a transformer encoder
[135] for encoding the features. But the area
[138] that is a little underexplored
[141] is this mapping between features and
[143] noral activity. Right? Instead of
[145] regression, can we explore other ways to
[147] do this and can we actually learn that
[149] mapping? This seems to be the right time
[152] to do it because of the availability of
[154] larger scale data including NSC data set
[158] uh which Agonaut is is based on.
[162] So first with the encoder we used a
[164] vision transformer a vit and just to
[167] refresh your memories shown on the right
[169] an image is uh divided into patches
[172] different patches are uh encoded with v
[174] fe feature representation and over
[177] multiple layers of encoding each patch
[180] is uh contextualized in it response by
[183] attending to all the other patches that
[185] it finds relevant and that's what's
[186] called self attention. You could train
[189] such a model for classification but you
[191] could also train such a model with uh
[193] self-supervised for reconstruction for
[195] distillation for other purposes. And
[197] what we use is a model called u dino
[200] which is distillation with no labels.
[203] And in this model you basically have
[204] different variations of the same image
[206] and you want to make sure they have the
[207] same uh representation. So that allows
[210] the model kind of forces the model to
[212] capture the essence of the image. So
[214] it's self-supervised. The reason we
[216] selected this backbone is because in
[218] earlier work we were modeling the uh
[221] dynamics of object grouping and we
[223] created this construct called affinity
[225] maps which basically looks at the
[228] activity the representation of one patch
[230] and compares it with the all the all the
[232] other patches and we wanted to say okay
[234] a good representation should be object
[235] ccentric meaning that if meaning that
[239] patches that have similar representation
[241] should be on the same object and we dis
[244] we basically compared a lot of models
[245] models. What we found was that uh Dino
[248] version two which is a variation on Dino
[251] with a VIT base model uh which is a 12
[254] layer encoder and patch size of 14 works
[256] best. So that is our back one
[260] on the decoder side right mapping these
[263] representations to fMRI activity we are
[267] we are taking inspiration from a model
[268] called DER and in this model basically
[272] it's trained for object detection. So on
[274] the decoder side, you basically have
[277] different queries. In this case, they
[279] represent different objects. So, and
[281] they're learnable embeddings. They could
[283] specialize in detecting maybe large
[285] objects or objects that are in a corner
[287] or specific things. And they attend to
[292] different parts of the through this key
[294] querying mechanism, they attend to
[296] different parts parts of the encoder in
[298] order to basically detect a certain
[300] object. Putting all of this together, we
[303] could get a model like this where we
[306] basically have an image. We divide it
[308] into patches and if you need, you have
[310] to pad it a little bit so it fits the
[312] patch sizes. We feed these image
[314] patches. We go through many layers or
[316] multiple layers of the encoder. In this
[318] case is 12. We could get the visual
[321] input from one of these encoder layers
[324] which is say about 31 by 31. These are
[327] the number of patches and the the
[329] feature dimension of each patch is
[330] around 768 in this case. You feed that
[333] to the decoder. On the decoder side, you
[336] use queries that correspond to different
[339] brain areas, the different regions of
[341] interest that you're interested to
[342] predict. And that query basically
[345] attends to the visual features that find
[348] relevant. Then that is linearly mapped
[351] onto the visual representation of that
[353] specific area. Here
[357] we we decided to have models taking
[359] input from different layers of the
[361] encoder. But why would we want that?
[364] Theoretically we would have expected
[366] that if the input comes from earlier
[369] layers of the encoder, it would be
[371] better for the decoder to be able to
[372] predict early visual areas because we we
[375] expected this hierarchy of
[376] representation kind of map. And this is
[378] exactly what we found. Here I'm showing
[381] the best model performance like uh where
[384] the which encoder layer was used the
[388] representation in order to predict each
[390] of them and you could see these are the
[391] view posterior view of the brain and you
[393] could see there is this gradedness that
[395] the decoder can predict the voxil better
[399] if it's looking in the early visual
[401] areas if it's looking at the early
[403] layers of the encoder. So we see this
[405] graded abstraction of representation in
[407] our encoder.
[410] So we basically combine responses from
[413] these different models. We also have a
[415] post-processing step where we try to
[417] reduce the dimensionality and try to
[419] basically take advantage of um
[422] dependencies among the voxels. Um and we
[425] add a little behavioral responses here.
[427] These aren't core to our model. We just
[428] added it at the end to get a little bit
[430] boost. Um but look at the code if you're
[432] interested.
[435] Now putting it all together and this is
[437] the cordy of the organizers actually
[439] generating this uh we get a score of
[441] around 63.5 and this is the view um
[445] based on the performance we didn't use
[447] any sorts of dependencies in terms of
[448] time and and whatnot but but it would be
[451] interesting to also look at those
[453] factors if we look at them would we be
[455] able to improve our performance or not
[458] now having told you this story so
[461] I want to tell you what do we gain when
[463] We go from regression to these sorts of
[466] transformerbased mapping from
[468] representation to the visual to the fMRI
[471] activity and what we can get actually
[474] are attention maps right just just to
[478] refresh your memory this is the multi
[480] head attention basically is attending
[484] each query basically each regions of
[486] interest you have a query and it's
[488] attending to different parts of the
[490] visual encoder in order to predict the
[492] response
[493] So now we could actually plot those
[495] attention maps. This shows the attention
[498] weights from a query on uh that was
[502] predicting the v1v on the left
[504] hemisphere. So what would it attend to?
[507] Well, in this case it's attending to
[509] this quadrant of the visual input. This
[512] is remarkable. We did not do any
[513] receptive field mapping in this model.
[515] This is all data driven. The fact that
[517] this query eventually has to predict the
[520] brain activity of this area
[523] makes it basically attend to this part
[526] of the visual input.
[530] Let's look at some face selective
[532] regions. Similarly, we see that when
[536] when queries are basically trained to
[538] only predict certain uh face selective
[540] areas, the attention emerges looking at
[544] the face in the image. Again, no, we're
[547] not doing any perceptive mapping or
[549] anything. Um, we could look at body
[552] selective areas and see what the
[554] attention signal is there. Or we could
[556] look at the place selective areas and we
[558] see attention is more distributed that
[560] way.
[561] Um,
[562] we could look at other face examples and
[564] you could see it even works for animal
[566] faces or or person face above. Even
[569] though there are much more salient stuff
[571] in these scenes, you could see that um a
[574] query that is supposed to predict the
[576] FFA one or FFA um two is attending to
[581] this specific region of the uh image
[584] which we find remarkable because again
[587] no mapping like it it gives us the idea
[590] that maybe you could do this in a
[592] datadriven way. If you define an
[593] anatomical area and then train this
[596] model, you could see which area this
[598] this query attended to and find the
[600] selectivity of that anatomical area.
[605] So transformers in this work help us in
[607] three ways. Um one encoding we believe
[611] that transformers that are trained with
[613] self-supervised objectives uh deserve
[616] consideration as models of visual
[618] representation in the brain. Um and and
[621] we approached this both in this case
[623] with the noral data but in prior work in
[625] terms of grouping and attention
[628] mapping to brain activity. I think we
[630] think transformers aside from working
[632] better, they could give us a more
[635] elegant way of going from normal
[636] activity from features to neural
[639] activity.
[640] And and as I showed, they really
[643] increase the interpretability and and in
[645] a way they allow us to discover
[647] selectivity in a datadriven manner. in a
[651] way that well if I have an anatomical
[653] area then I could potentially find out
[656] what concepts are maximally activating
[659] this area.
[662] Now for future direction I think we need
[665] more data. I think NSD is a great
[668] starting point, but I think it would be
[669] nice to have 10 or 50 folds more data in
[672] order to train these models and have
[674] many more layers and and in a way if if
[676] we really want to take advantage of the
[678] datadriven approach. I think we should
[681] we should have more data. Um we should
[684] try different backpss. I think we we
[687] tried self-supervised one but we could
[689] also try uh vision language aligned
[691] ones. I think those are also strong
[693] backbones. we should better quantify the
[696] segmentation uh using segmentation maps
[699] quantify this attention and see what the
[701] selectivity is. Um and I'll leave you
[704] with one last thought. Maybe the way we
[706] think about areas of the brain
[708] communicating we could update that to
[709] think about maybe an area has this gated
[712] way of communicating with other cell in
[714] a way that the encoder and decoder are
[716] communicating here. But but that's just
[718] a thought and and very forwardlooking
[720] but but I think it's an interesting
[721] thought to have with that. I thank you
[724] and my collaborators.
[737] >> Great. Thank you. Uh any questions?
[740] >> Yeah.
[741] >> Yep.
[741] >> Hello. So do you think uh which of the
[746] uh parts of the vit for example the is
[749] the architecture more important or is
[751] the uh cell virus losses that is trying
[754] to predict uh obs obscure patches uh
[759] color coloring and that is more
[760] important for for it to learn more uh
[763] important representations. So is the
[765] loss function more important or the have
[767] you tried and or the architecture more
[769] salient and
[770] >> so we we tried this with different so if
[773] if you let's say use change the
[774] objective instead of in this case being
[777] distillation with with reconstruction
[780] we would get similar input I I think as
[782] long as long as it's a self-supervised
[784] thing in supervision as we know kind of
[787] abstracts over a lot of representation
[790] but when you use self-supervised or
[792] unsupervised methods whatever you want
[793] to call But they they maintain a lot of
[796] more of the information. If you if you
[798] need to reconstruct the object then you
[800] would have to maintain the information.
[802] Architecture is very important. I think
[804] um what we saw in prior work um the
[809] transformerbased architecture works a
[811] lot better with say self-supervised
[814] methods than a convolution does. So it's
[817] just it's just all sorts of thing have
[818] to come together for it to give you this
[820] nice objectentric representation that
[822] could eventually give you better
[823] prediction power.
[827] >> Thanks great talk. Um do you have a
[830] sense of what scale of data you need for
[832] the transformer mapping to be
[834] successful? Like with a run-of-the-mill
[836] cognitive neuroscience experiment would
[838] that work?
[840] >> Probably not. I mean so we are training
[842] these models per subject. So in this
[845] case we have around 9,000 images for
[848] each subject and we have the data for
[850] them I would say and again we had to
[853] simplify our model a lot in terms of
[855] even for that data set. So I would say
[857] you probably need that scale of images
[860] but with the other like with the other
[863] project that I was talking about earlier
[865] there we're not training beyond the
[867] initial point. So I think if you start
[869] from a pre-trained transformer, it gives
[872] you enough features that you could come
[874] up with a creative way of using it
[876] without retraining. In this case, we
[878] train the decoder on the data. So
[880] >> but in that case, would you still be
[882] able to get those attention maps?
[884] >> U probably not. Yeah. So in that case,
[887] you probably would want because the
[888] decoder so you have to train a decoder
[890] in order to attend the right way. Yeah.
[892] >> Okay. Very cool work. Thank you.
[894] >> Thanks.
[897] Sorry, I have one more question. So if I
[900] understand correctly, your you have um
[902] your model has one branch for each ROI
[905] and they do not overlap. What do you
[907] think will happen will happen if you had
[910] um if your linear layer were to uh
[913] predict um vertices that overlap between
[916] our eyes?
[917] >> So uh there are different ways of
[920] defining the queries. If we do uh for
[923] example streams so you could have for
[926] different streams and stuff they would
[927] overlap a little bit but but we haven't
[931] tried really over overlappinging the
[933] stuff but I know what you so that's an
[935] interesting point I we haven't tried
[937] that
[937] >> because you would end up with some sort
[939] of like ensemble model in the sense that
[940] you would have several predictions maybe
[942] for villes which overlap between and I
[945] was just surprised like I would I was
[946] just wondering what happens at the
[948] intersection of our maybe
[949] >> that's interesting we haven't looked at
[955] Great. Let's give uh one last round of
[957] applause for
