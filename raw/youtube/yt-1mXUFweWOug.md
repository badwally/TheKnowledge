---
schema_version: 1
id: yt-1mXUFweWOug
type: youtube
title: '"Towards a Platonic Intelligence with Unified Factored Representations" by
  Akarsh Kumar'
url: https://www.youtube.com/watch?v=1mXUFweWOug
authors:
- Michael Levin's Academic Content
ingested_at: '2026-05-30T21:59:43Z'
content_hash: sha256:8a07878c93aa3c928cbf6f2515f3fcbc7aaa526597dc069bf4e078497e4df565
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Michael Levin's Academic Content
  channel_url: https://www.youtube.com/@drmichaellevin
  duration_seconds: 3825
  caption_track: fetched
  snippet_count: 1631
filter:
  score: 0.7
---
[0] Um this will be about like towards a
[2] platonic intelligence with a um unified
[6] factored representation.
[8] One second let me just move this.
[23] There we go.
[35] Okay.
[40] Okay. Amazing.
[42] Okay. So uh to start off with uh I want
[45] to state something obvious that you guys
[47] already know that the world is not
[49] random but rather it has a lot of
[51] structure as we know and this includes
[54] everything from like self similarity
[56] across like many spatial scales to like
[58] physics symmetries like symmetries in
[60] like translation rotation invariance of
[64] the world as in if you have like some
[66] laws of physics it's going to be true
[67] here and if you're like one mile away
[69] from here and um every I mean Everything
[73] has structure. I mean, even the fact
[74] that objects exist and they're basically
[77] persistent across time, that's a form of
[78] structure. And um the the fact that
[82] there's so many um common patterns
[85] across in this world, right, across many
[88] different objects, that's what leads
[90] some of us to believe in this like idea
[92] of like there's like this this um space
[95] of forms, this platonic space of forms
[98] where these properties, common
[99] properties across many objects are
[101] inherited from the space of forms.
[103] That's one way to think about um what's
[105] going on, right? And obviously this idea
[107] came from Plato and it was pretty
[109] influential and that's the main point of
[111] this um symposium is to talk about that.
[115] So um I claim that basically intelligent
[118] agents in order to solve their goals
[121] they need to really understand how the
[123] world works in order to control it right
[125] to uh achieve their goals. And in order
[128] to un uh understand this world, I argue
[131] that they must capture this structure of
[133] the world. All these different
[134] structures that the world has, they must
[136] capture it in some way. And more
[138] specifically, what I mean is that the
[140] internal representations
[142] of their minds and their brains must
[144] capture the structure of the world. So
[146] I'll talk about more concretely what
[148] this means next, but at a high level,
[150] basically you can't really control the
[152] world without understanding how it
[154] works. And you can't understand the
[155] world without really um understanding
[158] all the different structures that are in
[159] the world, right?
[162] So we face this problem in AI because in
[165] AI we're trying to create these
[166] intelligent agents, right? And we have
[169] this uh we face this problem. How do we
[171] capture the regularities of the world,
[173] right? So one of the things we've been
[176] uh think about thinking about in AI is
[179] like what if we just try to bake in some
[181] symmetries of the world through how we
[183] design the architectures of our agents
[186] right so this is also known as inductive
[188] biases and I'll give you an example of
[190] like two or three of these is like one
[192] is like translation invariance in images
[195] whenever you look at an image and you
[196] see like some object you know that the
[199] system should process the object very
[201] similarly if it's over here versus as if
[204] it's like shifted over 100 pixels to the
[206] right. And this is translation
[208] equariance or translation invariance.
[210] And we try to bake this into um ar an
[213] architecture based on the convolutional
[215] architecture. That's what it's made to
[216] do. Another example is like whenever we
[219] process sets of objects and we want we
[222] don't care about the ordering of the set
[223] like red green blue or blue green red.
[226] We don't care about if what the order is
[228] then we use an attention architecture uh
[230] in a transformer to do this kind of
[232] thing. Right? And in general, this field
[234] called symmetry learning or geometric
[236] deep learning has um is a really big
[239] field in deep learning. And basically
[240] the goal is how do we capture known
[243] regularities of the world into the
[245] architectures, right? And this is kind
[247] of like you're just baking in the
[249] structure of the world.
[251] But what about all the other um
[254] structures in our world, right? All the
[255] other regularities. And one example I
[258] really like is like lighting invariance.
[259] So you see this lion in the dark and
[262] during the day and you don't really know
[264] what architecture should capture this
[266] lighting invariance, right? And we don't
[268] know how to do this. So what's our
[271] solution?
[273] Well, okay. So, the solution is we just
[276] try to train on a lot of data with SGD
[278] and hope that the AI will learn this
[281] underlying regularity of the world um
[285] based on the patterns that it picks up
[287] from all of these data uh from all this
[289] data right that's this is the
[291] predominant paradigm in modern deep
[292] learning currently. So, the question is
[295] does this actually work right and
[297] there's a lot of evidence that's showing
[298] that it is somewhat working. I mean the
[300] AI systems nowadays if you use chat
[302] chieftd they can pick up on all sorts of
[304] patterns of the world and they seem to
[306] really understand the world and how it
[308] works and even self-driving systems they
[311] can like figure out uh what a stop sign
[314] looks like during the day at night and
[315] it seems like everything is just working
[317] but this brings us to our um position
[320] paper and our um which where we
[323] hypothesize that conventional SGD in
[327] deep learning um finds neural repres
[329] representations which are actually
[331] fractured and entangled um um in the
[335] sense that their actual internal
[337] representations are fractured and
[338] entangled. So uh over here we can see
[341] that I mean you find a network which has
[343] a certain output behavior but the output
[345] behavior we visualize it as like a skull
[347] which I'm going to get into detail how
[348] we're doing this but at a high level you
[350] visualize the output behavior and the
[352] internal representations don't really
[354] match what you would expect to see if
[357] it's really like understanding the skull
[359] in a subjective way right and more
[362] specifically what I mean is that it
[364] doesn't capture the underlying
[365] regularities of this world which is the
[367] skull
[369] So our position or our opinion is that a
[373] different kind of search algorithm which
[374] is not conventional SGD but a different
[377] kind of very exotic open-ended search
[379] may be the solution to learning what we
[382] call unified and factored neural
[385] representations. And as you can see over
[387] here the representations of the skull
[389] look a much better and much more like
[391] what we would want in how you would
[393] build up the skull. So let's get into um
[397] and so so you might be asking why does
[399] this matter at all right if the output
[401] behavior is the same and we basically
[403] believe that the internal representation
[405] of an agent really u affects its
[409] capability to generalize to new
[411] situations it's never seen before
[413] especially OOD its creativity in the
[416] sense that how and how it like sees the
[419] world and how it comes up with new
[420] solutions or new any artifact that it
[423] can create and especially continual
[425] learning and adaptation. And you can see
[428] over here on the top we see that the
[430] network with the nice representation if
[433] you perturb its weights it has really
[435] good adaptability behavior because the
[438] skull changes in like semantically
[440] meaningful ways versus the skull on the
[442] right the network on the right it has
[444] terrible adaptability and it basically
[446] just produces like a mess on the right.
[450] So let's get into the details of how
[452] we're uh doing this kind of experiment,
[454] right? So uh we're going to be using
[455] what we call like a compositional
[457] pattern producing network or CPN. And
[461] basically this is like a toy domain to
[463] study neural representations. And the
[465] goal is basically just to implicitly
[468] represent an image. And at a high level,
[470] it's inspired by the biological
[472] development process like morphogenesis.
[475] Um because it's about how do you reuse
[478] existing machinery to across different
[481] like uh points in space in order to
[483] achieve the same thing. That's where the
[484] inspiration comes from. So let's talk
[486] about how we would represent this
[487] specific image. Let's see this pixel uh
[490] that's highlighted over there. What
[491] we're going to do is we're going to
[493] basically mark its xy location and its d
[496] distance from the center. And we're
[498] going to take these three numbers and
[500] just plug them into a network that is
[502] the CPN. And after it's done processing,
[505] we're going to take its output and
[507] consider it as its HSV or you could
[510] think about it as just like a RGB value.
[512] And that's going to be the RGB pixel
[514] value for that um pixel. And if you
[517] sweep this across every pixel in the
[520] image, then you can basically visualize
[522] the entire output behavior of the CPN as
[525] a single image. And the reason that we
[529] construct the image like this rather
[530] than just modeling like the RGB pixels
[533] is because this makes it very very easy
[536] to uh visualize how the output behavior
[540] of this network is internally
[542] represented neuron by neuron. So in this
[544] case you can literally go to each neuron
[546] and see when does it activate at which
[549] XY locations does it activate and you
[551] can visualize that as an image also.
[555] And one thing I want to make clear, um,
[557] this is probably a really important
[558] slide, is that the CPN are an analogy.
[561] We're not really interested in just like
[562] how do you represent images, but rather
[565] these CPN serve as like a very useful
[567] visual analogy to think about what other
[570] AI systems like largecale LLMs might be
[573] doing, right?
[575] And basically the analogy is that its
[577] output behavior or the output image of
[580] the CPN is analogous to the LLM's entire
[583] output behavior over the entire its
[586] entire output space. Right? And the
[589] CPN's internal visualization is
[592] basically analogous to the LLM's
[593] internal representation of its entire
[596] output behavior. So basically just how
[597] it models and sees the world.
[600] And because we're using CPN, we can just
[602] visualize how these behaviors are
[605] constructed holistically, right? Not
[607] just like in a single neuron, but seeing
[609] how it's built up over many many
[611] neurons.
[613] And importantly, uh this brings us to
[615] the main point is that like two CPNs may
[617] have the exact same output behavior, but
[620] their inner encodings could be
[621] qualitatively different, right? And this
[624] means that two LLMs may have the same
[626] output behavior, as in you can't tell
[628] them apart from what they're doing on
[629] the outside, but their internal
[631] representation and how they see the
[633] world internally may be qualitatively
[635] different.
[638] Sweet. And with that, um, I will
[640] actually go on a slight tangent with
[642] Pigreeder, but it'll connect back into
[644] the main story very quickly. So, let's
[647] talk about Pigreeder. So, Pigreeder was
[649] basically an online website for humans
[652] to breed these CPN images to their
[655] desire. So, humans would just see these
[657] images and you'd pick like two or three
[658] of them you'd like and just mutate them
[661] and keep going. It's kind of like
[662] breeding horses, right? And what you're
[665] going to be doing is just evolving the
[667] underlying CPN that um generated these
[670] images.
[672] And importantly, one of the big uh
[674] things about the system is that there
[676] was no end goal. you can just do
[678] whatever you want. The humans weren't
[679] told like, oh, you should try to evolve
[681] a skull or you should try to evolve like
[683] a cat image or something. They just said
[685] just do whatever you want. Have fun. And
[688] uh one caveat here is that the actual
[690] CPN's used inside here were not like
[692] your conventional multi-layer
[694] perceptrons from um AI, but rather these
[697] things called neuro evolution of
[699] augmenting topologies need. And you can
[702] imagine this as like rather than having
[704] like a dense connected network, you have
[706] like a graph of neurons that you're
[708] growing in this arbitrary way. So it's
[711] much I guess in a way it's much more
[713] flexible, right?
[716] And so what would you expect to find
[718] from this pig reader system? Right? And
[720] I think most people would say that oh if
[722] people don't really have a objective
[723] goal in mind, then you kind of would
[726] just expect to find these um super
[728] rubbish images, right? This is what
[730] you'd expect to find. But here's what
[731] people actually found. These images with
[735] lots and lots of um structure and
[738] basically what humans prefer, right?
[740] It's like literally things from our
[742] world. So the question is like how did
[744] people um find these kinds of things?
[747] And if you want a deep dive into how um
[750] this kind of thing happened, you should
[751] really check out the book from my
[753] collaborators Ken and Joel on why
[755] greatness cannot be planned. And they
[757] really go into a lot of um insights into
[759] like the nature of search, deception,
[762] serendipity in search, which is um a
[764] really important topic I believe and
[766] open-endedness. And basically um they
[769] argue that this pigreeder system is like
[771] a um like a microcosm for like natural
[774] evolution or like scientific innovation.
[776] These open-ended process which keeps
[778] discovering stuff forever. So I do want
[780] to uh talk more about pig braider and
[782] then talk about that what properties it
[784] has that uh why I think you should
[787] consider it as like a very very
[788] interesting system. So first property it
[791] has is that it's open-ended. So if you
[793] think about natural evolution it's like
[794] this divergent evolutionary process
[796] which produces all these different
[798] diversity of animals right um and
[800] pigreeder is similarly like that.
[803] there's literally a pigreeder
[804] evolutionary tree where you just have
[807] images which are diverging and growing
[809] um open-endedly. So that's one thing
[811] that's really interesting about it.
[813] Other things that are interesting about
[815] it include this idea of serendipitous
[817] adaptation. So in evolution um a lot of
[820] the traits that we ended up with or all
[822] animals ended up with were traits that
[825] were evolved for one function but get
[827] repurposed later down the line for
[829] something else. So here's an example
[831] like feathers were originally evolved to
[834] keep like the animal warm but they later
[836] got repurposed for flight. So this is an
[839] example of like this huge task space
[841] where things are kind of just it's a
[843] more serendipitous rather than like
[844] planned ahead of time right and
[846] pigreeder displays this property also
[850] you can see that um the the stepping
[853] stones that they call it two let's say
[856] look at the teapot image someone was
[858] actually trying to evolve a egg in a hat
[862] before someone else took that image and
[865] started evolving a teapot so this is an
[867] example of like this machinery that was
[870] used to represent this egg got
[872] repurposed to represent this teapot. And
[875] this is like a common very common story
[877] in all the pig breeder discoveries.
[879] Basically, every image in pig breeder
[881] that was found is kind of it displays
[884] this idea that like there it's like
[886] almost seems like random, but it's what
[888] we'd call serendipitous and how it got
[890] to the end product. Right?
[893] And one final property that I want to
[895] outline is that um as we know that um
[898] natural evolution has developed very
[901] adaptable genotypes. And this is kind of
[904] like the emergence of evolvability,
[906] right? Because the way that our bodies
[909] and our um are structured is basically
[914] uh it contains certain axes of
[916] variation. Let's talk about the
[918] symmetries. The way our bodies are
[920] structured really has a lot of baked in
[922] symmetries. Like for example, there's
[924] like a bilateral symmetry and the way
[926] our organs are structured are modular.
[929] And it's just that there's a lot of um
[931] structure in the way our bodies are
[933] structured, right? And the reason it's
[934] like this is because certain axes of
[936] variation during search become much more
[939] likely while others become impossible.
[941] So for example, if you have a mutation
[943] in your genome and your right hand gets
[947] like uh longer, right? Your left hand
[950] would also get longer because evolution
[952] has kind of realized that encoding this
[954] axis of this symmetry into the genome is
[957] really important because there's no
[959] point in not doing it, right? So this
[960] axis of variation where both get uh
[962] longer becomes likely where whereas this
[965] axis where only one gets longer becomes
[967] impossible, right? So it's a way to kind
[969] of like speed up search in that way.
[975] And pigreeder has also shown um this
[978] form of evolvability emerging. There's
[980] examples in the pigreeder where certain
[982] images are structured in a very nice
[985] organized way such that their children
[989] have very fit descendants as in they're
[991] basically producing images that humans
[993] would like. And there are some images
[995] which don't have this property and but
[997] they quickly die out because humans
[999] don't select for their children. Right?
[1001] So there's this like implicit pressure
[1003] to be evolvable.
[1005] So great now that I talked about
[1006] pigreeder let's get into the actual
[1008] experiments that show this internal
[1010] representation that we've been talking
[1011] about. So let's look into just uh let's
[1014] pick this image of this skull right and
[1016] see what happens.
[1018] So let's take this skull image that we
[1020] found with pigreeder. And what we're
[1022] going to do is this. We're just going to
[1024] create a data set from it based on this
[1027] uh based on the mapping that we're
[1029] talking about where you have XYD to HSV
[1031] and you list out all the pixels, right?
[1033] And we have this big data set and then
[1035] what we can do is just train a
[1037] conventional network to recreate the
[1039] skulls using all the tools from AI,
[1041] right? And what we found what we find is
[1044] that the optimization works amazingly.
[1046] it perfectly reproduces this um skull
[1049] behavior, right? But then let's uh let's
[1053] talk about what happens when we start
[1054] looking at the internal representation
[1055] of how it represents the skull, right?
[1057] That's where we see some problems. But
[1059] before that, what we're going to do is
[1060] quickly talk about layerization, which
[1063] is not too important. So um but I will
[1065] quickly go over it just for the sake of
[1067] complete completeness. So basically, you
[1069] can imagine that our neat networks that
[1071] we found at Pigreeder, they're in this
[1073] arbitrary, they're like this arbitrary
[1075] graph of neurons. In order to make it
[1077] compatible with the space that we're
[1079] going to be doing SGD training with AI
[1081] on, we're going to convert everything
[1083] into a universal architecture which is
[1085] the MLP through this process of
[1087] layerization. And specifically uh this
[1090] will give us like an existence proof
[1092] that this pigreeder solution is in is a
[1095] solution that the SGD could have found
[1098] but it didn't. And more concretely, what
[1100] we're going to be doing is just taking
[1101] all the connections of this arbitrary
[1103] graph in neurons and stitching them
[1105] together to in the MLP to recreate the
[1107] same computational graph.
[1111] Okay, so this is what the internal
[1113] representations look like for the
[1115] pigreeder skull. This is the one found
[1118] with pigreeder. So you can see that the
[1120] four input neurons encode the four
[1122] inputs or X, Y, D, and we just have a
[1124] bias neuron for historical
[1126] compatibility. And over the layers as
[1129] you go up you can see that the neurons
[1131] encode different things and builds up
[1134] the pattern at which you see at the end
[1137] which is the skull. But you can see that
[1139] there's not really any redundancy. It's
[1142] very very uh modular in that way. It's
[1144] very sparse and it seems quite organized
[1147] in how it's doing it. Right? So let's
[1150] look at this SGD skull. Now to contrast,
[1153] this is what happens when you train SGD
[1155] when on the same network architecture to
[1157] get the skull.
[1159] It looks like a complete mess, right? It
[1161] looks like complete spaghetti. And you
[1163] can see everything ends up canceling out
[1165] the end and giving you the perfect
[1166] output behavior. But the internal
[1168] representations are like completely just
[1170] like what I'd call spaghetti, right?
[1171] They're just like a complete mess.
[1175] So, how does this actually impact um
[1178] downstream what we call like downstream
[1180] tasks or something? So, on the left over
[1183] here, what we're going to be doing is
[1184] just sweeping individual weights of this
[1187] network and seeing how the output
[1188] behavior changes. And you can see that
[1191] it really shows you that uh if you sweep
[1193] a weight, there's literally a weight
[1194] that corresponds to the mouth opening or
[1197] the left and eye winking or the distance
[1200] between the eyes right there. Right? or
[1202] like literally a weight controlling the
[1204] jaw width. And this kind of shows you
[1206] that the network kind of understands the
[1210] underlying um what we would call the
[1212] underlying regularities of the skull,
[1214] right? These are axes aligned with how a
[1218] human uh sees the skull. And if you
[1220] imagine that the skull is an analogy to
[1224] the real world and the behaviors uh that
[1226] you would want to employ, this basically
[1228] corresponds to nice changes in this
[1232] actual behavioral output of the network,
[1234] right? Versus if you have the network on
[1236] the left, you can see that the weights
[1238] kind of most almost all the weights look
[1240] like this. they kind of just correspond
[1242] to rubbish meaningless changes which
[1244] don't respect the underlying x x-axis
[1246] symmetry of the skull or any regularity
[1249] of the skull for that matter. Right?
[1253] So this pattern is true for all the
[1255] images that we've tried out like here's
[1257] this butterfly image for pigreeder and
[1259] here's this skull uh SGD image of this
[1262] uh butterfly.
[1264] You can see it's the same pattern and if
[1266] you look at the weight sweeps it's the
[1267] exact same thing. you capture the
[1269] regularities on the left and you don't
[1271] really do that on the right. Right? Over
[1273] here you can see that one of the weights
[1274] literally destroys the left wing while
[1276] leaving the right wing sort of intact
[1279] which is completely not respecting that
[1280] symmetry of the butterfly. Right? And
[1283] here's the apple image found at
[1285] Pigreeder and here's it with um SED
[1289] and it's the same pattern again um on
[1292] the left. U one of the my collaborers's
[1294] favorite is like the stem angle. There's
[1297] literally a weight in the apple network
[1298] that on the pig breeder side at least
[1300] that corresponds to if you sweep it, it
[1303] controls the angle at which the stem is
[1306] um controlled at. So this really shows
[1307] that the stem and the apple are like
[1309] modular are decomposed in like a modular
[1312] way in order to have this happen, right?
[1317] So the question is this is cool but this
[1319] is still like this toy domain. How does
[1320] this really apply to LLM and like real
[1322] intelligent systems, right? So there is
[1325] some uh evidence uh actually a lot of
[1328] evidence that um these LLMs also suffer
[1330] from fractured and entangled
[1332] representations that don't respect the
[1334] underlying regularities of the world. So
[1336] let's start off with a old example from
[1338] GPD3. So in GPT3 um we ran this
[1341] experiment where we had like um where
[1344] you just say like I have three pencils
[1346] and two pens and four erasers. How many
[1348] things do I have? And it gets it right.
[1351] You have nine things. But if you ask it
[1353] the same exact question, but change up
[1355] the um item names, like I have three
[1358] chickens, two ducks, and four geese. How
[1360] many things do I have? It gets it wrong.
[1362] It says you have 10 animals, right?
[1363] Instead of nine. And what this means is
[1367] that the machinery or the neural
[1369] circuitry that it's using to count up
[1372] the objects is entangled with the types
[1375] of the object that it's seeing. Right?
[1377] So this is an example of how it could be
[1379] the representation is entangled. Right?
[1381] So let's scale up to more modern
[1383] networks. Uh there's there's a lot of
[1385] papers that show that like um if you
[1388] change like if if a network can if a LLM
[1391] can be really good at doing like these
[1393] math problems, slightly changing the
[1394] numbers in the math problems causes them
[1397] to um decrease their performance on that
[1400] um on that data set, which is crazy
[1403] because you would expect them to be kind
[1405] of robust to changes in the numbers,
[1408] right? And uh sure if you scale them up
[1410] this has been going away which we're
[1412] going to talk about but let me go
[1413] through some other examples too. This
[1415] >> sorry can I can I ask a question uh in
[1418] the the previous slide the example about
[1421] the the counting
[1423] >> uh the the slide before this?
[1426] >> Yeah. So
[1428] does it say 10 because it includes the
[1431] me as well?
[1434] Uh because it says you have 10 animals
[1437] total. So, if it's actually including
[1439] the the person who's asking the
[1441] question, then it's actually not
[1442] incorrect, right? I mean, just out of
[1444] curiosity.
[1446] >> Oh, uh, the me is not in the prompt.
[1449] It's just the I have. And the fact that
[1451] it's asymmetric between the two shows
[1453] that's the difference, right? I don't
[1455] think that's what's going on because
[1456] whenever you say like how many things do
[1458] I have, you don't talk about yourself,
[1460] right?
[1462] >> Yeah. Yeah. I I I know. I know. But um I
[1465] was thinking maybe it's thinking in a
[1467] much clever way that uh that makes us
[1470] think that it's it's incorrect. I mean
[1472] in in a sense you could argue that it's
[1474] not incorrect but yeah I'm just saying
[1477] >> interesting.
[1479] Yeah. In that case it should at least be
[1481] symmetric on both sides. Right. I also
[1484] don't think it makes much sense to say
[1486] 10 in this case.
[1489] >> Yeah. Okay. Yeah that's that's fair.
[1493] um this paper from some of my friends at
[1495] MIT here um they basically showed that
[1498] these LLMs they're really really they're
[1500] trained on the internet right and the
[1501] internet has this the world that we
[1503] operate in which is like um the current
[1506] world but if you change their evaluation
[1508] to counterfactual worlds then the
[1511] performance goes down a lot and by
[1512] counterfactual world what I mean is like
[1514] instead of doing arithmetic in like base
[1516] 10 you do it in base 9 this is a way
[1519] less common um way to do things right or
[1521] in code execution you change it to be
[1524] base one indexing then the performance
[1526] goes down a lot. So in this way you
[1529] could argue that there's like it's not
[1531] respecting if you change one thing about
[1533] the world it's not respecting it's not
[1535] understanding the world where it's like
[1537] um it understands the regularities in a
[1540] deep way where it can be robust to these
[1542] counterfactual changes right
[1547] here's another example I really like um
[1549] this is from an anthropic mechan paper
[1552] from quite recently where they looked at
[1554] claude and they asked it what's 36 + 59
[1557] and it came out with the answer 95 which
[1560] is correct. But if you look at the um
[1564] actual arithmetic that goes behind this
[1566] answer right the actual neural circuitry
[1569] that's happening you can see it's using
[1572] like random heruristics that a human
[1574] would never even think about. It's like
[1576] saying like oh 36 is around 30 and if
[1579] you add and it's around 40 and if you
[1582] add around 40 plus around 50 it's like
[1585] around 92 and it's it's completely like
[1588] different than how a human would do this
[1590] arithmetic problem. Right? So it's
[1591] neural circuitry is kind of just like a
[1593] bag of huristics. And indeed there's
[1595] been a paper that's been written that
[1596] arithmetic um that language model solve
[1599] math with just a bag of heruristics
[1600] right while still getting the answer
[1603] right.
[1605] So I think it's uh I think there's a lot
[1607] of evidence that like these LLMs their
[1609] behaviors are amazing but the way they
[1611] actually represent these behaviors are
[1612] very um surprising and definitely
[1616] concerning
[1618] right and now let's talk about the
[1621] counterargument right like how does
[1623] scaling work because this is like the
[1624] predominant view in AI that if we keep
[1626] scaling these systems then um they
[1629] should just keep getting better right so
[1630] this is the scaling laws view and you
[1632] can see that the actual test loss or the
[1635] test performance and the downstream
[1636] performance and how you use use these
[1637] systems are getting better. But again,
[1640] this is a statement about um like the
[1642] actual behaviors, right? And if you if
[1645] we go on to the next slide, then we can
[1646] talk about the platonic representation
[1648] hypothesis from our lab. And this is
[1650] actually one of the coolest papers um
[1653] ever. So you guys should all definitely
[1654] check this out of basically what they
[1657] claim is that neural networks trained
[1659] with different objectives on different
[1660] modalities. So one could be trained on
[1662] images and one could be trained in
[1664] language. They show that these two
[1666] models trained on different modalities
[1668] and in different ways are actually
[1670] converging in some sense to like um uh
[1674] as you scale up the model sizes and
[1676] their performances. So over here in this
[1679] graph they're showing that um as you
[1681] increase the language model performance
[1683] its alignment with a vision model also
[1685] increases. And the reasoning behind this
[1687] is basically that as you force these
[1689] networks to do more and more tasks then
[1692] the number of representations which
[1694] solves all the tasks in either modality
[1697] kind of has to overlap more and more.
[1703] So this is all saying this is all very
[1705] very cool but I do want to point out
[1707] that these scaling laws and this
[1708] platonic uh representation hypothesis
[1711] are all very like statistical
[1712] observations of what's happening right
[1715] these are statistical observations of a
[1718] statistical uh behaviors right and it's
[1720] very unclear how this relates to
[1724] respecting regularities of the world and
[1726] I think we need a lot more um um
[1729] research trying to connect the two
[1732] because the examples we gave in our
[1734] paper where we did a survey on like all
[1736] these um studies that were showing that
[1738] language models struggle in this task in
[1741] this way or something they're more
[1742] talking about whether or not you respect
[1745] some regularity of the world and I think
[1747] this is a very different um way to see
[1750] the world than if you just look at this
[1752] as like a statistical um mechanism right
[1755] and one more thing I want to point out
[1757] is that the efficiency of this scaling
[1759] view right we don't have infinite data
[1761] in the world we only have the 10
[1763] trillion tokens of the internet and the
[1766] question is is that enough and if it's
[1768] not then this scaling view isn't really
[1771] a practical way forward right
[1774] and more practically we need to figure
[1776] out like even now u with with these
[1779] large scale um LLMs why do our LM still
[1783] have this notion of jagged intelligence
[1785] right as in they can do some really
[1787] really hard tasks like get IMO gold but
[1790] they can't reliably book a hotel or a
[1792] plane ticket for you. So why is it that
[1794] the task that we find so um hard like
[1798] the winning the IMO gold it can do
[1800] pretty nicely but it can't do something
[1802] what we seem as basic and um like book a
[1805] hotel
[1810] and I think the uh main point I want to
[1813] make is that deep learning is
[1815] fundamentally like a datadriven
[1817] statistical learning paradigm and I
[1819] think it's a very very fascinating
[1821] paradigm that that should be
[1822] investigated.
[1823] But I wonder if there exists like a more
[1826] efficient like regularitydriven learning
[1828] paradigm because obviously like human
[1831] intelligence and like animal
[1832] intelligence they don't just ingest like
[1835] billions of um examples in order to
[1837] learn right they do something much more
[1839] different and um something much more
[1842] akin to like understanding the
[1843] regularities of the world and building
[1845] on top of them. So what could this look
[1848] like? Right? And I think the things that
[1850] would matter the most is like something
[1851] like some process of complexification.
[1854] If you look at like the process like
[1855] morphogenesis,
[1857] it doesn't just encode every part of
[1859] your body at once. It grows it according
[1861] to something more fundamental, right?
[1864] And this is a very adaptive process
[1866] which adapts to the environment and it's
[1868] not just baked in. So and importantly I
[1870] think the cool thing is that if you do
[1872] this complexification in a learning
[1873] algorithm it should like try to build up
[1876] the regularities on top of other
[1877] regularities in the same way that like
[1879] if you go remember the skull internal
[1881] representations it's like building up
[1884] like x-axis symmetry and then on top of
[1887] that it builds in like the eyes from
[1890] that symmetry. So it's building up
[1891] symmetries on top of other symmetries in
[1893] a form of like a regularitydriven
[1895] learning that's like bottom up. And this
[1898] process of complexification should also
[1900] give you uh build on these ideas like
[1902] emergence and um I'm going to tie this
[1904] back into emergence in a bit.
[1908] Another thing that I think could be
[1909] really important is training for
[1911] adaptability. So rather than just
[1912] training for to solve the task, what we
[1914] really want is to train for adaptability
[1916] because I think it gives you a lot of
[1918] like regularization pressure to learn
[1921] like symmetries and regularities to be
[1924] robust to environmental changes, right?
[1927] And I think that a representation that
[1930] kind of has to be robust to
[1932] environmental changes is one that must
[1934] capture the axis of variation which like
[1937] as Plato would say like carve nature at
[1939] its joints, right?
[1942] And this is just personally what I think
[1943] is really important. It's like
[1944] serendipity.
[1946] And what I mean by serendipity is that
[1948] this the order in which you learn things
[1951] really matters. If you look at LLMs,
[1954] they learn uh calculus at the same time
[1956] as they're learning arithmetic. But
[1958] humans, they always learn arithmetic
[1960] before calculus because their internal
[1963] representation of calculus builds on top
[1964] of the regularities from arithmetic. But
[1968] LLMs, they kind of learn them at the
[1969] same time. So they must have different
[1972] circuitry if that's going to happen,
[1974] right? Different circuitry for
[1975] arithmetic and calculus. And that's why
[1977] I think this idea of serendipity or in
[1980] general curriculum learning is really it
[1982] should be important in terms of you're
[1984] doing this regularitydriven learning.
[1987] And I really think serendipity
[1988] specifically is important because it
[1990] gives you a much higher chance of
[1991] finding a useful learning curriculum to
[1994] actually employ. Right? And if you think
[1997] about it uh this these uh paradigms what
[2000] what paradigm captures all of these it's
[2002] like the field of open-endedness um I
[2004] think has a good uh not solution but
[2007] they've been thinking about this and I
[2008] think they have the toolkit to come up
[2009] with a solution that can handle all of
[2011] these.
[2013] >> Can I ask a question?
[2015] >> Yeah.
[2015] >> How do you think about the the the order
[2018] related to reinforcement learning?
[2020] Because uh uh you talk about uh uh
[2023] learning circulum and uh when you when
[2026] you train uh reinforced learning agents
[2028] they often start with some very simple
[2031] behaviors and by and by interacting with
[2035] the complex environment they they
[2036] complexify themselves. So, so I I was
[2040] just wondering uh if you if you can
[2043] train if you can convert this pattern
[2045] generation into some kind of reinforced
[2048] learning task, would it also have
[2051] similar meaningful and robust weight or
[2055] or not?
[2057] >> Uh that's a really interesting question.
[2058] I think the on policy nature of
[2061] reinforcement learning is a really um it
[2064] should be super useful it seems. But I
[2066] guess uh the fact that there's still
[2069] like a singular objective that you're
[2070] trying to solve is I think is a
[2072] downfall. I mean there's a lot of works
[2074] in the field of reinforcement learning
[2076] that show that like um you train the RL
[2080] agent to do one task and it masters it
[2082] but what it but if you perturb the
[2085] environment even even ever so slightly
[2087] like change like for example like change
[2089] like the placement of the objects even a
[2091] little bit or change the color of like
[2093] the how the objects are represented
[2095] everything breaks down. So I think the
[2097] way they represent their task solution
[2099] is still um very very um brittle. So I
[2103] think what you really need is uh either
[2105] take the scaling route and you just have
[2107] like a many many different tasks or the
[2108] more better route I think would be to
[2110] kind of have many different environments
[2113] that it's exposed to in like a sequence
[2117] and in kind of like a serendipitous way.
[2118] This is kind of what happened with
[2120] evolution, right? You're exposed to this
[2122] is what I'm going to talk about in the
[2123] next slide too is like you're exposed to
[2125] some environment but then you're forced
[2127] to adapt according to the environment to
[2129] some other environment and you're forced
[2131] to adapt again and this pressure to
[2133] adapt is what I think really creates
[2134] makes you robust because if you don't
[2136] adapt quickly then you will die and in
[2140] order to adapt I really think you need a
[2142] really strong representation. I think
[2144] they're um this is my hunch is that I
[2146] think a strong representation and
[2148] adaptable representation are like one
[2150] and the same.
[2151] >> Yeah. I also wondering how how does the
[2154] like models like AlphaG go looks like
[2156] because AlphaG go when you start the
[2158] reinforce learning they these start with
[2161] very poor uh players and the the there's
[2167] a similar a symmetry between player and
[2170] environment because you when you improve
[2172] yourself your environment also improved.
[2174] So there there's a nature there's a
[2177] nature course of learning uh maybe maybe
[2181] there are two kind of different
[2183] reinforce learning like offer I think
[2185] it's maybe a different one and maybe
[2187] they they have similar like complex
[2190] complexification process as you
[2192] mentioned
[2194] >> yeah it builds in a lot of these things
[2196] together but um I mean AlphaGo obviously
[2200] solved go so that was a huge impressive
[2201] result but I'm still not sure that it's
[2204] training to be adaptable. It's kind of
[2206] like its objective is to train to solve
[2208] the objective, right? The cool thing
[2209] about evolution is that it's like you
[2211] could say that it's optimizing to be a
[2213] good fit for the environment, but it's
[2215] implicitly optimizing for adaptability
[2218] because everything is always changing,
[2220] right? So, if someone shows that like
[2222] this if there is a pressure to like
[2224] adapt, then that would be um pretty
[2227] cool, I think. Yeah.
[2229] >> Thank you.
[2232] >> Yeah. So I guess zooming out a bit um
[2234] how does this relate to like the
[2235] platonic viewpoint and what you guys
[2238] have been thinking about for a while
[2239] right so I think this space of forms
[2241] that people have been thinking about
[2242] obviously um create like you could argue
[2245] that it's like this is where the real
[2247] world and all its patterns come from and
[2249] I think intelligent agents are fit or
[2252] like um trying to be intelligent to that
[2255] world so obviously indirectly the space
[2258] of forms is going to leak through but I
[2260] guess the cool thing is that uh that uh
[2262] uh I've been thinking about that I guess
[2264] maybe you guys can add something to the
[2266] conversation is that does this space of
[2268] forms directly does does the internal
[2271] representations of a good agent intern
[2273] like does this mind come directly from
[2275] the space of forms right so I guess uh
[2278] you could argue that like just as like
[2280] you have this like aspirational ideal of
[2282] like this platonic um shape and you have
[2285] the real instantiation of it in this
[2287] pyramid the same way that real
[2289] intelligent agents are kind of trying to
[2291] mimic this aspirational ideal of this
[2294] like perfect mind that can understand
[2296] the regularities of the real world. But
[2298] this is all just um speculation, right?
[2301] [laughter]
[2302] So cool. Yeah, this is something I'd
[2305] love to get your guys' thoughts on. And
[2307] just to wrap up, I'd like to thank my
[2308] collaborators Jeff, Joel, and Ken um for
[2311] making this work possible. And with
[2313] that, thank you.
[2320] >> Thank you. That was very interesting.
[2323] Uh
[2325] questions.
[2332] >> Yeah. Yeah.
[2333] >> Yeah. Hi. Um so as I understand this
[2338] you're the um the training process. So
[2341] first of all this is beautiful. um the
[2343] and you could sort of see where having
[2345] things modular like this now allows you
[2347] to do cognition rather than just like
[2350] randomly emitting motions and stuff. But
[2353] um it seemed to me that you're still
[2355] training on something. And so then the
[2359] question is is the difference between
[2362] this way and the old way of doing things
[2364] that instead of training to fulfill a
[2367] task, you're training towards some
[2370] criterion. In other words, somebody is
[2372] somewhere is saying, "Oh, gee, that
[2374] actually looks like something. I'll keep
[2375] that one." As opposed to to keeping the
[2378] spaghetti. Um, is is that a fair way to
[2381] look at it? So, or your evolutionary
[2383] adaptability, that's another criterion.
[2386] You survived. Maybe you did it this way,
[2387] maybe you did it that way. So, the tasks
[2390] are different, but the criterion is the
[2392] same.
[2394] >> Yeah. So I do want to say they they did
[2396] some experiments after pig breeder
[2398] happened where they asked people to
[2400] explicitly evolve the skull where
[2402] they're like your goal is to get to the
[2403] skull and get there as quickly as
[2405] possible and that did not work at all.
[2407] So I and even if it did I think that you
[2410] would end up with like kind of like a
[2411] brittle skull. I think the key important
[2413] thing is the fact that this environment
[2415] that people people are selecting images
[2417] right so this environment of selection
[2419] that's happening like the selection
[2420] pressure is extremely complex. It's this
[2423] it's as complex as a human brain because
[2425] they're the ones doing the selecting,
[2426] right? And more importantly, it's
[2428] changing after the skull gets
[2430] discovered. No one thinks that that's
[2432] interesting anymore. And you need to
[2434] figure out a different adaptation that's
[2435] more interesting than the skull, right?
[2437] So, I think this pressure to adapt again
[2439] is the thing that's creating these good
[2441] representations. That's
[2442] >> the Oh, go ahead.
[2443] >> Yeah. That's the reason that the skull
[2445] like there's a weight that corresponds
[2446] to the mouth opening because that's the
[2448] axis of variation that humans find the
[2451] most interesting. Right? So in the same
[2453] way in the real world there's some axis
[2455] of variation that are going to be like
[2458] um on earth that are going to be useful
[2460] and these are the ones that intelligent
[2462] agents need to capture right
[2464] >> but there's some point at which whoever
[2466] is doing it said okay I'm done you know
[2469] that's my picture.
[2472] So, that's the thing. Uh, when one
[2474] person gets it done and they upload
[2475] their picture, um, the next people, uh,
[2478] start evolving. It's like this
[2479] open-ended process. It never stops,
[2481] right?
[2484] >> Okay.
[2488] >> Chris,
[2490] okay. Yeah, Chris.
[2493] >> Yeah, thanks. This this was very nice.
[2496] Um I just wanted to comment on the
[2498] question in your last slide about the
[2501] effects of the the world of forms on um
[2506] the agent. Yeah, the one right after
[2508] that.
[2510] >> This one.
[2511] >> No, the one right after that.
[2514] No, I'm sorry. That one? Yes, that one.
[2517] [laughter]
[2518] >> I mean the the wonderful thing about
[2520] organisms is that we are part of the
[2523] real world. Mhm.
[2524] >> So, uh to the extent that uh this idea
[2529] of of forms informing our structure uh
[2534] or the structure of the real world, then
[2536] that applies to us too and in particular
[2540] to the way that our minds work.
[2545] So
[2546] in in thinking about this picture um we
[2550] have lots of intelligent agents that are
[2552] already part of the world
[2555] >> and so their interactions with the rest
[2559] of the world are just part of the way
[2561] the world works. Right? So
[2563] >> if the way the world works is driven by
[2566] some you know abstract principles
[2570] symmetry and so forth
[2572] >> then
[2573] um our behavior with respect to the
[2576] world is is driven by those same
[2579] symmetries.
[2581] Whereas with intelligent agents, we're
[2584] we're trying to use a an abstraction
[2589] from certain features of the real world
[2592] to design an intelligent agent when
[2595] we're coming up with with any machine
[2598] learning scheme.
[2600] >> Yeah.
[2603] And this suggests at least to me that
[2607] it's an interesting approach to think
[2609] about to design the simplest possible
[2611] agent can and just turn it loose
[2615] which I think is what you're describing
[2618] to some extent with pigreeder.
[2622] Um is that a fair assessment of the
[2624] proposal you're making?
[2627] So you're so the way I see it is that
[2630] like let's talk about like um a concrete
[2633] example of like planets right let's talk
[2635] about let's say that like the space of
[2637] forms in forms physics right and the way
[2640] that particles interact and these
[2642] particles you run them for a long time
[2645] according to like gravitational laws and
[2647] they form this uh imperfect planet right
[2650] with some bumps and things but this
[2652] planet is like emergent from the laws of
[2655] physics
[2656] But this planet, you could argue it's
[2659] kind of like trying to inherit the
[2661] property of being a perfect sphere,
[2663] right? So, not only were the laws of
[2665] physics inherited from the space of
[2667] forms, but also
[2670] um this emergent planet is trying to be
[2673] another idea from the space of forms.
[2675] Right. In the same way, I think that
[2677] intelligence in the sense that you said
[2679] they're just agents in the real world,
[2682] they're just complex systems. They're
[2683] just made off of small little tiny
[2685] particles following the laws of physics.
[2687] But as a global whole, the emergent
[2690] phenomenon of the brain could be
[2692] something like mimicking trying to mimic
[2694] some something more platonic in that
[2696] sense. Right. That's the way I've been
[2698] seeing it
[2699] >> if that makes sense.
[2700] >> Yeah. Okay. Thanks.
[2705] >> Thank you, Brian.
[2707] >> Hey, K. Uh, yeah. Yeah, I had a question
[2709] about u the framing around the way
[2714] the CPN and I guess open-endedness is
[2717] kind of this top- down signal where
[2718] you're having someone or something like
[2721] some maybe like God or something
[2723] choosing the things that actually are
[2726] desirable than less desirable and having
[2729] this top down view even for the SGD
[2731] model too to like match this target.
[2733] >> But is there a more bottomup view of the
[2735] open-endedness where like there isn't a
[2737] kind of
[2739] loss function that's given from top down
[2741] but like it's just kind of an emergent
[2743] property of the system. Maybe it's like
[2744] stability or persistence or something.
[2746] >> Yeah, I would actually classify the
[2748] Preeder stuff as bottom up. I would
[2751] classify the SGD ones as top down
[2753] because the SGD one kind of what it what
[2754] I feels like it's doing is that you have
[2756] this like block of marble and you're
[2758] chipping away at different places in
[2760] order to get the shape that you want,
[2762] right? But I see this pig breeder one as
[2764] in you're starting out with like like a
[2767] small no network which has like no
[2769] neurons and you're building up the first
[2771] neuron which encodes x-axis symmetry and
[2773] then you build up something else which
[2774] builds on top of that symmetry and
[2776] you're building this bottom up this uh
[2779] layers and layers
[2780] >> process is done by humans right and that
[2782] >> the selection process done by humans
[2784] that's the top down signal I'm kind of
[2785] describing is like
[2787] >> oh you're saying if you can replace
[2788] humans with some other signal
[2790] >> right like something that is more in the
[2792] nature of the system or the physics that
[2795] it would exist in a world rather than
[2796] having a human top down being like okay
[2798] this is something I like this is
[2799] something I like this is something I
[2800] don't like.
[2801] >> Yeah. So we're I don't think any like if
[2804] you do something like um any like if you
[2806] try to put an equation onto it I don't
[2808] think it's going to work because it's
[2809] not going to be nuanced or diverse
[2811] enough. We are doing some experiments
[2813] and trying to make like a automatic pig
[2816] breeder with VLMs using VLMs and even
[2820] that is like we're like struggling a
[2821] lot. So I think the I think the
[2823] environment that you're exposed to
[2824] really does have to be extremely rich
[2826] and complex in order
[2828] >> maybe that perspective maybe the human
[2830] itself is the environment that the
[2831] picture kind of lives in and it has to
[2833] survive or persist in and that's kind of
[2835] how you would
[2837] >> that's right that's I think that's the
[2838] right way to view it. So then the
[2840] question is if you want good um networks
[2843] and good um sorry um AI systems right
[2846] you need to subject them to the right
[2848] environmental pressures and the I think
[2850] the way that you subject them matters a
[2852] lot. So I'm a big fan of like you know
[2854] this pressure it to adapt. I think
[2856] that's the right way to think about it.
[2858] >> Cool. Thanks
[2860] >> Yanu.
[2864] Hey uh so I also have two question about
[2868] fairness. So, so the first one is uh uh
[2872] uh different architecture might suit
[2874] both for for different thing and that's
[2876] uh what you explained but uh I think uh
[2880] there are some example in in video games
[2882] like some people want to challenge
[2884] themselves so they they constrain
[2886] themsel like I only have one weapon to
[2889] win the game and when they decide to do
[2891] this the is the entire playing process
[2894] become very complex you can't play game
[2898] like a usual people and usually people
[2900] can play game in a quite a decomposible
[2903] way. They they have a clear clear
[2906] semantic meaning of doing this doing
[2908] that but when you apply this constraint
[2911] you you have lot of things that locally
[2913] looks nonsense. So just wondering first
[2916] the data is generated by CBPM
[2919] uh but uh you train it on MLP. So uh
[2924] this this kind of um I don't know if
[2926] it's a very fair to to compare this and
[2929] this lead to another question is uh CBPN
[2933] has a very uh carefully designed uh
[2936] architecture and training process and
[2938] some details but MLP uh I know that
[2942] there are some tricks or regularizations
[2946] on MLP. I just wondering have you tried
[2949] uh try to optimize MLP in order to make
[2953] it symmetric u because if you don't do
[2956] that then uh this comparison uh it's
[2959] also might feels unfair to compare.
[2963] Yeah.
[2964] >> Yeah. So in terms of the first of all in
[2966] terms of the fairness I mean uh in this
[2968] paper we're it's like a position paper
[2971] and we're not proposing pigreeder as an
[2973] algorithm that's supposed to compete
[2975] against and that everyone should use
[2977] right it's more like to inspire like
[2980] that fact that this algorithm has some
[2982] cool properties that were assoc even
[2984] though we cheated and we used humans in
[2986] the loop we used a different um neat
[2989] network it's supposed to inspire ideas
[2991] that maybe we can extract some insights
[2993] and turn this into an algorithm which
[2995] can compete against SGD and do better.
[2998] So, and we're not trying to be fair.
[3000] We're trying to cheat and come up with
[3001] an algorithm which in some way or shape
[3003] or form found something interesting,
[3006] right? Um yeah, I think that's the grand
[3009] goal of this kind of research. And your
[3011] second question was about uh what was
[3014] the second question?
[3015] >> Uh it's about how how many efforts you
[3018] applied you you put on optimizing MLP in
[3021] order to make it
[3022] >> Oh, yeah. Yeah. reasonable, right?
[3025] >> Yeah. So, obviously you can't bake in
[3027] any explicit symmetry into the network.
[3029] We did try a large set of experiments
[3031] using like um weight decay and we even
[3034] tried to make the target symmetric like
[3036] the target image perfectly symmetric to
[3038] see if if it was perfectly symmetric
[3040] would it pick up and the answer is it
[3042] almost never um picks it up. there are
[3045] like one or two seeds out of like 20
[3047] seeds in which you have if you have the
[3049] right weight decay with the right um
[3052] symmetry aspect with the right
[3054] architecture um because we tried out
[3055] different architectures also then it
[3057] ends up working but it almost never
[3060] actually works. Yeah.
[3063] >> Yeah. Okay. Yeah. There there was a
[3066] recent study that adding noise to the
[3069] weight of the the the model instead of
[3071] adding weight decay. I'm wondering, have
[3074] you tried that? Would it make the the
[3077] map become more symmetric?
[3079] >> No, I haven't tried that. I really doubt
[3082] that these things like this would
[3084] qualitatively change the learning
[3086] dynamics to make it capture regularities
[3089] versus not capture regularities. I don't
[3091] think any simple trick like that would
[3092] do it. Uh, one of the cool ideas that
[3095] I'm investigating with the undergrad
[3097] here is like basically trying to see if
[3100] um the network if we try to make the
[3103] weights predictable because
[3105] predictability is like a very specific
[3107] type of signal that could qualitatively
[3109] change what you learn, right? Because
[3110] weight decay is more like a simplicity
[3112] bias where you want to regularize it
[3114] towards like low weight norm. But I
[3116] think that if you try to make it
[3117] predictable, that's not the same thing.
[3119] It's not the same as simplicity. It's
[3121] the it's completely different. So I
[3122] think there are ideas in which it could
[3124] change, but honestly I don't even think
[3126] that's that would work that well. I
[3128] think what you really need to do is like
[3130] rethink what's going on and what the ad
[3133] what the pressures you are that you're
[3135] optimizing towards. And I think the
[3136] pressure to adapt is probably the
[3138] biggest thing that needs changing. I
[3139] think that would fix a lot of things.
[3142] >> Interesting. Yeah. Thank you.
[3144] >> Mhm. Excellent.
[3147] Um yeah, great paper. I really loved it.
[3151] Um I'm an experimental biologist so for
[3155] me this was really up my alley. You know
[3156] I really loved um
[3159] >> the idea and I think [clears throat] you
[3162] know objective functions are something
[3164] very fundamental and I think this really
[3166] this really sort of shows it. Um, and I
[3169] think one of the things you could you
[3172] could interpret from your paper is there
[3174] might be uh a trade-off between
[3177] complexity of the objective function and
[3179] how controllable uh the outcome is. As
[3183] you noted yourself with when you tell
[3186] people to select for a certain outcome,
[3187] pick breeder doesn't work anymore. How
[3190] fundamental do you think that trade-off
[3191] is?
[3193] the trade-off between um having a fixed
[3196] objective function and what else?
[3199] >> Yeah, sort of the richness of your
[3200] objective function and how uh how how
[3203] well you can determine the outcome of
[3205] your optimization process.
[3210] >> Yeah. So I think the fact that pig
[3213] breeder is not able to optimize directly
[3216] and that it has to take this like
[3217] serendipitous path through the search
[3219] space um I think there needs to be more
[3222] research like quantifying just how
[3223] important that is. That was like kind of
[3224] like the point of the paper that we
[3226] don't really know or understand what
[3227] caused these good representations and it
[3230] would be cool if like we could figure it
[3232] out, right? So um I think I it feels
[3235] that like the serendipitous search is
[3237] very very important. I can't exactly um
[3240] rigorously tell you why, but the reason
[3243] it feels that it's like important is
[3244] because it combines this pressure to
[3246] adapt while making optimization easier
[3250] because you're not just optimizing for a
[3251] single skull, right? Because that's like
[3253] really really hard to do. You're
[3255] optimizing for either a skull or a cat
[3258] or a dog or anything else that a human
[3260] would want, right? So I think that is
[3263] like the serendipitous search kind of
[3264] makes optimization easier and the
[3266] pressure to adapt is is something that's
[3268] obviously good and um that's hard to
[3271] satisfy. It's hard to optimize towards.
[3273] So then you need a serendipitous search
[3275] to optimize it if that makes sense.
[3281] >> Doug,
[3285] you're muted. Sorry.
[3289] >> Okay, great. Um so we find that natural
[3292] languages pervasively omit system
[3295] component relations which has to affect
[3298] whatever happens when you use written
[3301] stuff to train these machines. But um
[3305] then in that context that made me think
[3307] about your apple example. So does the
[3311] network know that the stem is a
[3314] component of the whole apple as opposed
[3317] to just something that's sitting next to
[3319] it? So that's this issue of not only so
[3323] engineers think in terms of systems and
[3325] components. So um not only do you have
[3328] two things sitting next to each other,
[3330] but there's is the stem a component of
[3332] the apple? Is the color red a component
[3334] of the apple? And that's different than
[3338] you know computer scientist is always
[3340] talking about overlapping sets and so
[3341] the system component thing is structural
[3343] completely different thing.
[3346] So how smart is this guy?
[3348] >> Yeah that's a good question. Um so over
[3351] here I mean you can see that there's
[3353] feature maps that correspond to just the
[3355] apple and there's a feature map that
[3356] corresponds to just the stem and at some
[3359] point in the network they get combined
[3361] in order to make the apple with the
[3362] stem. So I mean that's kind of like the
[3364] modular decomposition you would expect
[3367] in an ideal world if you wanted these
[3369] two things to be decomposed right
[3372] >> so I think the feature maps are they
[3374] basically show that it's like basically
[3375] perfect um in terms of what you would if
[3378] you want that but then the question is
[3380] um is that the right decomposition right
[3382] that's one of the things I've been
[3383] thinking about is like how do you know
[3385] this de so like basically if you imagine
[3386] the skull you can decompose it any
[3389] number of ways right you can decompose
[3392] it along this way which I like or
[3394] another way which you might like and
[3395] they're both we what we would call
[3397] unified and factored. So then that
[3399] really begs the question is like in a
[3400] ground truth manner what makes a good
[3402] representation and personally I feel
[3404] like that definition should be grounded
[3407] in the set of future tasks that you may
[3409] want to adapt to right I have this
[3412] thought experiment I like a lot which is
[3414] like if you evolve like a cat on Earth
[3417] right but you have the same identical
[3419] cat evolved on Mars and they're
[3421] identical in their behavior one may have
[3423] different axis of variation in its
[3425] genotype based on the past and future
[3428] environments it's going to be exposed
[3430] to, right? Because the future
[3431] environments in Mars are going to be
[3433] different than the ones on Earth. So, um
[3435] they might be very different in that.
[3438] Since you're thinking about that, um I
[3441] was debating whether to mention this,
[3442] but since you're at MIT, I don't know
[3443] whether they still teach uh what the
[3445] frog's eye um tells the frog's brain, an
[3448] ancient MIT paper that I think is one of
[3451] the more important papers in biology.
[3454] But basically, frog's eyes only see
[3457] things like uh edges, light, dark
[3460] contrast, and a couple other things. The
[3462] rest never gets through to the brain. So
[3465] if the fly is not moving, the frog
[3467] doesn't even see it. So they have a
[3469] basis set of universals like Kant would
[3473] talk about. Um you and I have a
[3476] different set more complex. On the other
[3478] hand, the frog could say, "Oh, that's a
[3480] needless overcomplexification of the
[3482] world."
[3483] >> Yeah.
[3483] >> And so there's some thought that goes
[3485] into what is your basis set.
[3487] >> Yeah. Exactly. And it should be grounded
[3489] in what you need to do now and what you
[3491] may need to do in the future, [laughter]
[3493] right? Well, good point. I guess
[3495] evolution decided that for the frog. So,
[3497] okay.
[3499] >> Yeah, that's very cool. What's that
[3501] paper called? What the frog eye
[3504] frog's eye. What the frog's eye tells
[3506] the frog's brain. Um, let me uh get you
[3510] the author so you can find it.
[3513] Um, everybody I think has passed away.
[3516] Um
[3518] >> uh
[3519] >> uh Jerry Lein, L T V I N and um Humberto
[3525] Machana who also passed away. Anyway, uh
[3529] it was an MIT thing. The biologist he
[3532] told me uh laughed at him uh when they
[3536] presented, but basically this stuff is
[3538] hardwired into your nervous system. Oh,
[3540] and he finally got it published in the
[3542] ILE E proceedings.
[3546] >> Very cool. I will check out that paper.
[3548] Thanks.
[3548] >> Yeah,
[3551] >> Santos.
[3553] >> Yeah. So, uh do you think that the
[3555] pressure to adapt is very different from
[3557] the pressure to generalize uh which is a
[3560] standard component of any MLP uh
[3564] optimization, right?
[3566] >> Yeah. I think uh honestly I don't think
[3568] we know the answer and I think that it
[3570] feels like it should be very very
[3571] different um in that sense because I
[3573] feel like the pressure to adapt if you
[3575] construct it in the right way I think it
[3578] should be like a much stronger pressure
[3579] that regularizes your neural network a
[3582] lot more um I don't have evidence for
[3584] this concretely yet but that's just a
[3586] feeling that I have. Yeah.
[3589] >> Okay.
[3592] >> Hey uh I want to ask another question.
[3596] uh I just realized that this uh study
[3598] might deeply related to computational
[3601] complexity theories because when you uh
[3604] gradually complexify your uh complify or
[3608] grow the the CPPM it's really like you
[3611] have a touring machine and you have a
[3613] sequence of program you and you add bits
[3616] to complicify
[3618] the the program and in computational uh
[3622] uh complexity theory this very
[3624] interesting a bias called uh Solomon of
[3628] induction or algorithm probability which
[3632] the theyentially
[3634] prefer shorter shorter programs and they
[3638] proven this uh this kind of distribution
[3642] this kind of bias has some very
[3644] beautiful and powerful uh universal
[3646] property. So so um and one of the reason
[3651] they have this two to the minus com
[3654] complexity is because they have some uh
[3658] they they are actually somehow growing
[3661] the the program. So so I want wondering
[3663] have you considered such connection
[3665] between them?
[3667] >> Yeah. So what I have been thinking about
[3669] a lot in terms of like is simplicity
[3672] like a um one is it a good um pressure
[3676] toward that you should strive towards
[3678] and two is it enough right and what for
[3681] one I do think that it's very
[3682] interesting obviously you want simpler
[3684] things rather than more complex things
[3686] but the question is that whether it's
[3687] enough is I'm not so sure about that is
[3690] because simplicity is basically supposed
[3692] to be a um um how do you call it like a
[3696] heruristic for what you really want
[3699] which is like generalization
[3701] adaptability etc etc right and I think
[3704] that if we can optimize for
[3706] generalization adaptability directly we
[3708] don't really need simplicity and in
[3710] often times I have I'm beginning to
[3712] think this more and more is that they
[3714] may not even be one uh that correlated
[3717] they're probably correlated up to a
[3718] point until they stray off so for
[3720] example in this skull example we have a
[3722] toy experiment obviously it's not that
[3724] conclusive because it's just a toy CPN
[3726] experiment
[3727] But we whenever we regularize it with
[3729] weight decay, we find solutions which
[3732] are way way lower weight norm than this
[3734] nice elegant modular solution. Way lower
[3737] weight norm. So in the traditional sense
[3739] of L2 regularization, you would say it's
[3741] a simpler representation, right? But it
[3744] turns out to be way less adaptable still
[3747] compared to this nice modular one. So um
[3750] maybe uh some sort of simplicity
[3752] mechanism or compression is not exactly
[3755] what you're looking for and it's
[3756] supposed to be just a heristic for
[3758] adaptability which is what you really
[3759] want.
[3760] >> Yeah. So, so what I exactly want to say
[3763] is I just uh intuitively feel that
[3767] evolution especially growing and
[3769] evolution putting together is is might
[3772] directly give you such bias of algorithm
[3776] probability and maybe that's why CBPN
[3779] and this kind of open-ended process give
[3782] you such clean result.
[3785] >> Oh, you're saying it's simple in like a
[3787] different way according to like
[3788] >> Yeah. Yeah. Like when you when you start
[3791] with some seed and you are add something
[3794] you are you are exponentially more
[3797] likely to have shorter evolution tree
[3800] that that shorter evolution tree like if
[3803] you in terms of something like assembly
[3805] theory they are more simple and
[3809] I feel that this architecture gives you
[3812] such bias.
[3814] >> Yes. Yes. Definitely I 100% agree with
[3816] that. Yeah, it it gives you a specific
[3819] kind of like um like graph bias towards
[3822] smaller graphs of neurons.
