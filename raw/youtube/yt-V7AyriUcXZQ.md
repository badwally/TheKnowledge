---
schema_version: 1
id: yt-V7AyriUcXZQ
type: youtube
title: The Platonic Representation Hypothesis
url: https://www.youtube.com/watch?v=V7AyriUcXZQ
authors:
- MITCBMM
ingested_at: '2026-05-30T20:02:00Z'
content_hash: sha256:88245b23b04b7408597b7561b8843f7d2fba6773be1d6e2fd3b065eaa6c3ede9
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: MITCBMM
  channel_url: https://www.youtube.com/@MITCBMM
  duration_seconds: 4149
  caption_track: fetched
  snippet_count: 1670
filter:
  score: 0.75
---
[0] PHILIP ISOLA: So I'll talk
about this position paper
[4] that we put out at ICML
and this general argument
[7] that we call the platonic
representation hypothesis.
[9] And this is work that's with
Minyoung and Brian and Tongzhou.
[14] Brian is over here and was
your moderator last night.
[17] So you can ask him the
hard questions as well.
[21] OK.
[25] So I want to start with this
paper that I really like.
[29] This is a little bit older,
2015 paper on object detectors
[34] and how they seem to emerge
when you train a network to do
[36] scene classification.
[39] So what this paper did is
they trained a neural network
[41] to recognize different scenes
and label them with kitchen
[45] or bathroom or whatever.
[47] And then you can do what
Jacob was talking about.
[50] You can do linear probes on
different layers of the network.
[53] You can try to look at
what signals in the input--
[57] that's not really a linear
probe, but it's related.
[59] What signals in the input
most activate neuron A?
[63] And what images most
activate neuron B?
[66] So you can kind of
imagine what it might be.
[68] It should have something
to do with scenes.
[70] And what it turned out
is that it's objects.
[73] So there exist object detector
neurons that fire selectively
[78] whenever they see an object.
[79] Like this neuron A--
[81] sorry.
[82] That neuron A fires
whenever it sees a dog face.
[85] And this neuron B fires
whenever it sees a robin.
[88] And this was really
cool because this
[90] is like a very concrete
version of what I might
[93] be willing to call emergence.
[94] And it was one of the first that
really convinced me at the time
[97] that deep nets are learning
some interpretable internal
[100] structure.
[100] They're not just like a
black box mystery thing.
[103] It's actually learning something
structured that makes sense.
[105] To recognize this scene,
you need to parse it
[108] into the object content.
[109] OK, so a lot of
other researchers
[111] went forward with that.
[113] We had this paper
a little bit later
[115] in which we trained a network
to colorize photos-- so
[117] take a black and white image
and predict the missing colors.
[121] And we did the same experiment.
[123] So let's take neurons and see
what input images most activate
[127] those neurons.
[128] And so you can try to guess.
[130] What are going to be these
units, these detectors
[133] in a colorization network?
[134] Anybody have a guess?
[135] What do you think it might be?
[137] It was dog faces and robins
for scene classifiers.
[142] But what was it going
to be for colorization?
[145] AUDIENCE: Leaves maybe.
[146] PHILIP ISOLA: Leaves?
[146] Yeah.
[147] Anything else?
[147] Maybe something about low
level photometric statistics
[150] of the world.
[150] OK.
[151] No, it's dog faces.
[153] It's robins.
[153] It's flowers.
[154] It's the same thing.
[156] It doesn't matter if you train
it to do scene classification
[158] or you train it to do image
colorization, two things that
[160] seem very, very different.
[162] The network learns
internal structure, which
[165] is what's surprisingly similar.
[168] And this is a story that we've
seen over and over again.
[172] It's probably not that
new to many of you.
[174] This is really
textbook knowledge.
[176] These are figures from a
textbook that we just published.
[178] So this is textbook knowledge.
[180] This is well-known.
[183] So over the years, we've seen
that different neural networks
[187] trained in different ways
often learn the same types
[190] of internal units.
[191] And we're just stating that as
a more provocative hypothesis
[195] of let's see how
general that is.
[198] Different neural networks with
different architectures trained
[200] on different data sets
with different optimizers,
[203] to what degree do they converge
on the same way of representing
[205] the world?
[207] And our hypothesis is they
converge to some degree.
[210] OK.
[213] OK.
[213] So I know what
you're all thinking.
[215] You're all thinking, well,
of course they converge.
[217] They're all trained
on the same data.
[219] It's all about the data, right?
[220] Machine learning, deep learning,
it's all about the data set.
[223] All our models are trained,
in the previous examples
[226] I showed, on ImageNet
and data sets like that.
[229] They're all trained on
the same set of photos,
[231] so of course they learn
the same representation.
[233] Or now all our models are
trained on the internet.
[235] Of course they're going to
just learn an internet model.
[238] It's going to be the same
because all the companies train
[240] their models in the same
way on the same data set.
[243] OK, so that's one possibility.
[245] Another possibility is,
no, it's not just the data,
[248] it's the architecture.
[249] We're all using transformers.
[251] So of course we're going to
get some kind of convergence.
[254] Another possibility is,
let's see, the optimizer.
[257] OK?
[258] We're all using ADAM and SGD.
[260] Maybe it's the people.
[261] Maybe it's because we
talk to each other.
[263] It's a sociological thing.
[264] We converge because we all
go to the same conferences,
[266] we meet here, and I
recommend that you
[268] use the same methods as I use.
[271] It could be all of those things.
[273] But I'm going to say something
maybe a little stronger,
[277] which is actually, the data
differs between different models
[280] and the architectures differ
between different models,
[283] but we still see some degree
of representational similarity.
[286] What is the same between all
these models most fundamentally?
[290] The world.
[291] So this is the gist of the
whole argument I'll make.
[293] I'll come back to this.
[294] It's all about the world.
[296] Any model that you
train in this universe
[298] should learn structure
related to the physics
[302] and the statistics
of this universe.
[304] That's the basic argument
at the highest level.
[308] OK.
[311] So the outline of the talk
is going to be-- first,
[313] I'll present evidence
of convergence.
[315] Then I'll talk about some
forces in machine learning
[318] that could be driving
this kind of convergence.
[321] Then I'll speculate
a bit and have
[323] a kind of toy
mathematical model of what
[325] we might be converging to.
[327] If models are converging
to similar representations,
[329] what is that endpoint
to that convergence?
[332] And then I'll talk about
implications and limitations
[334] of this analysis.
[336] And there should
be plenty of time
[338] for questions and interruptions
and people saying,
[341] this is all wrong.
[342] So feel free to do that
throughout the talk.
[344] It doesn't have to
just be at the end.
[347] OK.
[347] So let's first look at
evidence of convergence.
[352] OK, so I already showed you some
with training neural networks
[355] and computer vision
to do different tasks.
[358] We always get the dog face
detector or the human face
[360] detector.
[361] We always seem to
get neurons that
[363] detect those types of patterns,
regardless of the objective.
[366] And I think the most
classical and striking version
[369] of this still today
is the emergence
[372] of these Gabor-like
edge filters in the cat
[375] cortex in AlexNet on the right.
[379] So this is a biological system.
[381] If you look at v1, it will have
these Gabor-like detectors.
[385] Maybe that's not all there
is, but that's part of it.
[387] In AlexNet, this
is literally all
[389] it is because we
can characterize
[391] all the filters in the first
layer of that neural network.
[393] And these are the
receptive fields
[395] or these are the filters
themselves, in fact.
[398] And they look quite similar.
[400] So that's the classical
result. But that's
[401] some kind of convergence.
[402] The first layer of processing
in convolutional neural networks
[406] looks like it converges on
the same set of filters.
[409] And there's kind of proofs
for when that might happen,
[412] going back to things
like Olshausen and Field
[414] and sparse coding and so forth.
[416] But people have carried that
story a lot further forward
[419] to the point where it's
no longer provable,
[421] but it's just an
empirical observation.
[423] And here's one recent
paper that I like.
[425] This is a paper that
identified these things
[427] that they call Rosetta neurons.
[429] And so Rosetta neurons are,
like the Rosetta Stone,
[432] neurons that are paired between
different neural networks, that
[437] can be used to
bridge or translate
[439] between different
neural networks.
[440] So in all of these
networks, in the columns,
[445] there exist these four
different neurons.
[448] These are kind of
convolutional response maps.
[451] So it's saying
where in the image
[453] does the neuron fire, that's
what the heat map is showing.
[456] And there exists a
neuron in StyleGAN,
[460] which is a generative
model, and in ResNet,
[462] that's a classifier,
that will fire whenever
[466] it sees a red Santa hat.
[469] OK, this is a redness or
maybe a Santa hat detector.
[473] And there exists a neuron
that's a cat eye detector.
[476] And they found that
there were about 20 or so
[478] of these Rosetta
neurons that were just
[480] the same receptive
field, the same response
[483] pattern across all the different
models that they tried.
[486] So our conjecture is actually
it's much more than 20.
[489] That we'll just go
in and all of them
[491] will be the same in the end.
[492] But they didn't
go quite that far.
[494] So that's one more
piece of evidence.
[497] I'm only going to be selecting
a few different papers
[499] to highlight here before I get
to some of our new results,
[502] because there's
really a lot of people
[503] that have studied this question
and I can't cover all of it.
[508] So here's another one.
[510] This is a paper that
popularized this approach called
[514] model stitching.
[516] And what they do is they take
a computer vision system, so
[520] a convolutional network, and
they break it into two halves.
[525] They train the first
half with data set A
[528] and they train the
second half with data
[530] set B, or even changing the
objective in some cases.
[533] Like train the first
with a cross entropy
[535] objective, the second with
a regression objective
[539] or like a least
squares objective.
[541] And then they stitch them
together with a linear layer.
[545] And the question is whether
this network can correctly
[550] operate, correctly classify
the input photos you give it,
[554] when it's only learning
this linear transformation
[559] between the output
representation of this network
[561] and the input representation
of that network.
[564] So if this representation
is incompatible
[568] with that representation,
then a linear mapping
[570] wouldn't be able to align
them and operate correctly.
[572] But if they're actually
learning fundamentally
[574] the same information just up
to a linear transformation,
[577] then this should work.
[579] And what they found
is that this works.
[581] OK, so here is-- if I stitch,
this is a random baseline
[586] and this is the penalty I get.
[588] So the decrease in
performance due to stitching
[591] versus just training the
whole thing end to end.
[593] If I stitch, this
is the fraction
[597] of the layers where
I'm cutting off
[601] my bottom half of the
network and then stitching
[603] on the top half of the network.
[605] And you can see
there's a big stitching
[606] penalty for random networks.
[610] But for these
pre-trained networks
[612] trained on self-supervised
tasks, on supervised tasks,
[616] on all different types
of tasks, there's
[617] really barely any
stitching penalty.
[619] So these flat lines are saying
that if I train network half
[624] A on one task and network
half B on a different task
[627] and I put a linear
layer in between them,
[629] then it just works.
[630] It works just as well
as end-to-end training
[632] the whole thing.
[633] That's more or less
what this is saying.
[637] OK.
[641] So that's another line of
prior evidence for this.
[646] Somehow these different
vision systems
[648] trained in different ways
on different data sets
[650] are learning representations
that are compatible
[654] up to a linear transformation.
[657] Another very popular way of
characterizing representations
[661] is to look at how they measure
distance between different data
[665] points.
[665] And so this is going to be
the main one that we look
[667] at for the rest of the talk.
[668] And I'll tell you the technical
details of how this works now.
[674] So this is sometimes called
representational similarity
[677] analysis or kernel methods.
[679] So what you do is we will
first restrict our attention
[682] to representations which
are vector embeddings.
[685] So mapping from some data to
a vector in RD, let's say.
[693] Yeah, I should move so
that you can actually
[694] see the equations here.
[696] So we're going to characterize
such a representation
[698] in terms of its kernel.
[700] So what is the kernel?
[701] The kernel is the
function that specifies
[703] how does that neural
network, that embedding,
[706] measure distance between
different data points?
[709] So it's the inner product
between the embedding for data
[713] point i and the embedding
for data point j.
[715] So if these are images, it'd be
like I embed the two vectors,
[718] I take the inner product, and
maybe I take their dot product,
[721] and this creates the kernel,
the similarity function.
[725] OK, so visually it
looks like this.
[728] Here again with
an image example,
[730] but you could do this
on any type of data.
[732] We will create the kernel
for a vision system
[735] as what is the similarity of the
embeddings, the representations
[739] for the apple with the orange?
[740] So the apple with the orange
are quite similar to each other,
[743] according to this
particular model.
[745] And so the kernel will say that
these have high similarity.
[748] However, the apple
and the elephant
[750] are going to be
lower similarity.
[752] So the apple and the elephant
or the orange and the elephant
[754] will be darker.
[756] So this is what the
kernel tells us.
[757] How does the neural network
represent the similarity
[762] or difference in representation
space between different inputs?
[765] OK, so this is a
really important object
[767] for understanding
and representation.
[769] How does it measure distance?
[771] It shows up all over in machine
learning, kernel methods,
[774] and so forth.
[774] I mean, I know these are
a little out of fashion,
[776] but they're still important.
[778] And in neuroscience,
the name for this
[780] is representational
dissimilarity analysis.
[783] OK, so a lot of fields have
come up with the same thing.
[786] Now, in order to characterize
whether the representation
[790] of one neural network is
similar to the representation
[793] of another neural
network, we're going
[795] to measure the similarity
between the kernels induced
[799] by those two neural networks.
[801] So it's a similarity
of similarities.
[803] OK, so this is one
neural network.
[805] This is the DINO neural network.
[808] It's a computer vision system.
[809] Here's another one called CLIP.
[811] It's another computer
vision system.
[812] I can create the DINO kernel
evaluated over these emojis.
[817] I can create the CLIP kernel
evaluated over these emojis.
[820] These are maybe
slightly different.
[822] But if these two vision
systems represent
[825] the data in the same way
up to similarity analysis,
[829] then these two kernels
should be similar.
[831] And our kernel alignment metric
or our kernel similarity metric
[834] will just be some distance
between the kernel
[837] matrices for two
different neural networks.
[840] Any questions?
[841] That's going to be the
technical object that we look
[843] at for the rest of the talk.
[848] Cool.
[848] OK.
[849] Yeah, one.
[849] AUDIENCE: I do have a question
about the stitching part.
[852] When you are saying
stitching, are you
[853] referring to the
same architecture
[855] or different architectures?
[856] PHILIP ISOLA: Yeah.
[857] So in the stitching
work, I believe
[859] you need to have two
architectures where
[862] you can take the output
of one architecture
[866] and put a linear
mapping to the input
[868] to the second half
of the other network.
[870] So it doesn't have to be that
they're identical architectures.
[872] And I think probably some
of the stitching work
[875] did not use the same
architecture for the A
[877] and the B half of the network.
[881] But they have to be compatible
up to a linear transformation.
[884] So it has to be the first
one outputs an N dimensional
[886] vector and the second one
outputs an M dimensional
[888] vector that would satisfy--
[889] takes as input an M
dimensional vector,
[891] and then we'd have a
linear map from N to M.
[893] So they don't have to be
the same architecture.
[896] I don't remember what they did
in that paper that I showed.
[899] They might have just used
the same architecture.
[901] Yeah.
[902] AUDIENCE: What is the rationale
for doing this kernel similarity
[904] as opposed to something
else like a transferability
[907] [INAUDIBLE] resolutions?
[909] How do you think the orientation
or [INAUDIBLE] for example?
[913] PHILIP ISOLA: Yeah so
an alternative to this
[915] would be to try to embed
the images with DINO
[920] and then learn a
mapping that tries
[924] to predict what would the
equivalent representation be.
[926] And if it's a linear
mapping, that's
[927] again like linear probes and
things Jacob was talking about.
[930] So I think that's
perfectly fine to do
[933] and that would be complementary.
[934] The main reason we didn't
do that here is it's
[937] costly because you have
to train those models.
[940] And yeah, I would just say
this is another choice that's
[946] cheap to analyze.
[950] But I actually do think
we should do this.
[952] So yeah.
[954] OK, good?
[955] So moving on.
[958] Yeah, one more question.
[960] AUDIENCE: [INAUDIBLE]
Like, this doesn't
[964] account any dimensionality,
number of nodes,
[967] like [INAUDIBLE], right?
[972] Is there any way that
[INAUDIBLE] number
[976] of dimensions,
number of activation
[978] nodes that we use to
calculate [INAUDIBLE].
[984] PHILIP ISOLA: So
we're really trying
[985] to characterize
representation in a way that's
[989] invariant to some
of those details.
[991] So maybe those details matter.
[992] Like, what is the
dimensionality of the embedding?
[994] Maybe that matters
for certain reasons.
[996] And that actually might
matter with the metric trying
[999] to predict the embedding
from one net given
[1000] the embedding from another net.
[1002] But this factors that away.
[1003] So this reduces all--
[1006] it's a characteristic of
a representation, which
[1009] is the same dimensionality,
the same format,
[1012] regardless of what is the
original architecture that you
[1016] used.
[1016] So regardless of what
the dimensionality N
[1018] is of the embedding, the
kernel will be the same size.
[1022] So we consider that
to be a positive.
[1025] This means that we can
analyze things that
[1027] differ in their dimensionality.
[1030] You might also be
familiar with work
[1031] that talks about how SGD
finds similar parameter
[1037] vectors that
minimize the function
[1038] or that all live in some
basin, in some sense.
[1042] And that's looking at
convergence of parameters.
[1044] And this is completely
invariant to parameters.
[1046] This is like a function space
representation-- function space
[1050] characteristic of the network,
as opposed to a parameter space
[1053] representation.
[1053] So we're getting away
from the number of units,
[1055] the number of parameters.
[1056] And we think that's a positive.
[1058] It abstracts things
a little bit.
[1060] Yeah.
[1061] AUDIENCE: So do you
use the embeddings
[1065] from a particular layer or
is it all of the layers?
[1067] PHILIP ISOLA: Yeah, so
that's another good question.
[1069] So for most of the
computer vision systems,
[1072] there's kind of a
canonical layer that
[1074] is used as the representation.
[1076] It's often right
before the logits,
[1078] or sometimes in
models like SimCLR,
[1080] there's a projection
head on top.
[1081] But there's often a canonical
representation that people use.
[1085] And that's the one that we use.
[1086] For other models,
like language models--
[1088] which we'll get
to later-- there's
[1090] not a canonical embedding layer
of like GPT-3 or whatever.
[1093] And for those models, we
just kind of concatenate
[1097] a bunch of layers together.
[1098] It's a bit ad hoc, but we
didn't have a principled way
[1101] of deciding which layer to use.
[1103] OK, so how do you measure the
similarity between two matrices?
[1108] There's a lot of choices.
[1109] You could just take the
distance between them.
[1115] However, the one that
we found that actually
[1117] shows the trends
the most cleanly
[1120] is this one, which is kind of a
nearest neighbor based metric.
[1125] So what we do is we take
a set of data points,
[1129] we embed them with neural net f.
[1130] We take that same
set of data points.
[1132] We embed them with neural net g.
[1134] And we ask, what percent
of the nearest neighbors
[1137] of a given data point are
shared between f and g?
[1142] So here we have the nearest
neighbors to the blue point
[1146] are red and yellow, and here
they're also red and yellow.
[1150] But this one differs in
the purple data point.
[1154] So this means that two out of
three of the nearest neighbors
[1157] are shared between the
embeddings for f and g.
[1160] OK, so this is one way of
measuring the similarity
[1163] between two kernels.
[1164] Because the kernel tells you
what the nearest neighbors are.
[1166] Essentially, it tells
you the distance
[1168] to all of the data points
in embedding space.
[1170] And this is saying,
do the kernels
[1172] induce the same set of nearest
neighbors between network f
[1175] and network g?
[1176] Or how many of the
neighbors are the same?
[1178] So that's our particular metric
that we use in our experiments.
[1181] But in the literature,
there's a few other metrics.
[1183] One is called CKA,
Center Kernel Alignment.
[1186] So there's a few other ones.
[1187] And they all kind of roughly
tell a similar story.
[1191] I'll mention some point
about CKA a bit later.
[1193] Yeah.
[1194] AUDIENCE: Yes.
[1195] I was just going
to ask, have you
[1198] tried other ones
that work less well?
[1201] If so, do you have
any explanations
[1203] on what works better?
[1204] PHILIP ISOLA: Let me say that.
[1206] So CKA works less well.
[1207] Some of the trends are the
same, but some of them differ.
[1210] And I'll bring that up in
the limitations section.
[1212] So we'll come back to that.
[1213] Did I see one more question?
[1215] Yeah.
[1216] AUDIENCE: When you say in this
comparison that one of them
[1219] works less well than the other,
how are you comparing that to?
[1221] What's the ground truth?
[1222] PHILIP ISOLA: Yeah.
[1225] So what I mean by that
will become clearer
[1227] on the subsequent
slides, but basically I'm
[1230] going to show some trends,
and these trends show up
[1233] when we use this metric.
[1234] They don't show up
as cleanly when we
[1236] use some of the other metrics.
[1237] So the type of convergence
that we will observe
[1241] is convergence in the
nearest neighbor structure
[1243] of two representations.
[1244] It's not convergence in certain
other types of structures
[1246] of two representations.
[1248] AUDIENCE: But how do
you know that that's
[1250] an actual proof, like a trend
that's actually [INAUDIBLE]
[1254] something serious.
[1255] PHILIP ISOLA: We could have
kind of hacked the metric
[1257] to find the one.
[1259] I think that's a good
question to keep in mind.
[1261] That maybe is a
limitation that--
[1264] yeah, maybe we found
the one metric that
[1265] shows what we wanted to see.
[1267] But keep thinking about that.
[1268] I would say it the
other way around.
[1269] I would say we found a sense
in which representations
[1272] are converging, and that
sense is the nearest neighbor
[1274] structure.
[1276] OK.
[1280] So of course, there's a lot of
research on this same question
[1284] in neuroscience.
[1285] So I want to go over
this a little bit
[1287] before getting to
our new experiments.
[1290] So this is the representational
dissimilarity analysis
[1294] line of work.
[1296] And what they do there is
the same type of thing.
[1298] They take two images.
[1299] They show it to a monkey
or a human or some animal.
[1302] And they measure the
activations inside the brain.
[1309] OK, so we get a embedding in the
brain, some activation vector.
[1313] And we can look
at the similarity
[1315] between the activation
vector for face and face,
[1318] and it's high.
[1319] Or this is dissimilarity,
so the dissimilarity is low.
[1321] And the dissimilarity between
face and house is higher.
[1326] These are not considered
similar by the animal's brain.
[1329] So that's how you extract
kernels for the brain.
[1332] You can use neural
recordings for that.
[1334] And the interesting
thing there is
[1337] that people have found that the
kernel between a computer vision
[1343] system, an artificial
network, and the kernel
[1346] for the macaque brain
are to some degree
[1349] quite similar looking.
[1350] So we could measure--
[1351] this is the kernel for the--
[1355] OK, sorry.
[1355] This is the kernel for IT
and the macaque, I believe.
[1360] And this is the kernel in a
deep net from a few years ago.
[1363] And they look quite similar.
[1364] You could measure the
alignment in different ways.
[1366] You could use the
nearest neighbor metric.
[1367] They were using something
else at the time.
[1369] But just visually you can
tell they're quite similar.
[1371] So there's a cluster
of things which
[1373] is like faces and a cluster
of things which is houses.
[1375] And that same cluster
appears in the monkey.
[1380] OK.
[1381] So deep nets and the
primate visual cortex
[1384] seem to organize data in
somewhat similar ways.
[1387] That's this other
line of research.
[1388] And I'm not going to get too
much into the neuroscience.
[1393] There's a lot of
controversies about exactly
[1394] how to measure that.
[1395] But we thought, we'll just
look at artificial networks
[1398] and we'll do the
same analysis there.
[1401] OK.
[1404] So you can also do this
with behavioral studies.
[1407] And this is actually
some work that we
[1409] have done in my
group some years ago,
[1412] or I was involved in
some of this work.
[1414] So instead of measuring
probes in the brain,
[1418] I can just ask a
human, how similar
[1420] are these two images and how
similar are those two images?
[1424] So we're going to do that
test with you right now.
[1426] We'll just do a little game.
[1428] This is work that we
did a few years ago.
[1432] It led to this metric
called LPIPS, which
[1435] you might have used before.
[1437] So the question is, how
similar does a human think
[1441] this image is to that image?
[1443] And we'll make a
neural net model
[1444] that will output the same
similarity as a human would
[1448] output if you just asked them.
[1451] So there's behavioral
data behind this.
[1453] We didn't just ask them how
similar are these two images.
[1456] But we had various just
noticeable difference type test,
[1459] and two alternative
forced choice type tests.
[1463] But those are just details.
[1464] Somehow, we asked humans, how
similar are these two images?
[1467] So I'm going to
ask you that now.
[1468] So here is the reference image.
[1470] And I'm going to
ask you how similar
[1471] is this image to the left
image and then the right image.
[1474] So here's the left image
and here's the right image.
[1477] And what I want
you to do is clap
[1480] if you think the left image is
more similar to the middle image
[1486] than the middle image
is to the right image.
[1488] So clap if you think that.
[1490] [SPARSE CLAPS]
[1491] OK, a few people.
[1493] Sorry, there we go.
[1494] You did that.
[1495] OK, now clap if you
think the right image is
[1497] more similar to the middle
image than the middle image is
[1499] to the left image.
[1500] [CLAPS]
[1501] A lot more people.
[1502] OK, so that's what you said.
[1504] You're all human.
[1505] And this is what our
participants say too.
[1507] OK, but why is that?
[1508] Interestingly enough,
it's not trivial.
[1510] If you look at the Euclidean
distance between this image
[1514] and that image in pixel space,
they're actually quite similar.
[1518] And this image and this image
have a higher Euclidean distance
[1521] because it's warped.
[1522] The pixels are all a
little bit misaligned.
[1525] And this is the most
standard classical way
[1527] of measuring how
similar are two images.
[1530] It's sometimes called PSNR.
[1534] There's other metrics you
might have heard of, like SSIM.
[1537] Same thing.
[1538] They think this image and
that image are similar.
[1540] So classic image
processing people
[1543] didn't know how to
measure similarity.
[1544] It looked like the brain is
doing something dramatically
[1546] different.
[1547] But what about
just the deep nets?
[1549] Do they learn a
notion of similarity
[1551] that is the same
as humans or not?
[1555] OK.
[1558] So the way we can do that is,
again, construct the entries
[1565] in the kernel matrix for
a computer vision system.
[1567] So we pass an image and another
image through the neural net.
[1572] And we do a little bit
of processing to average.
[1575] And we basically subtract the
activations at all layers.
[1579] So here, we're not using
just the final embedding,
[1581] but all deep layers of the
network, do some normalization
[1584] and so forth.
[1585] And then finally,
you get a scalar out,
[1586] which is just saying, what is
the distance between this image
[1589] and that image, according to the
activations of this neural net?
[1593] So this is building one
entry in the kernel matrix.
[1597] OK, so here were the
empirical results.
[1601] On the y-axis, it's going
to be how often does--
[1607] I'll show a bunch of networks.
[1609] And we're going to be measuring
how often those networks agree
[1612] with humans as to
which of the two
[1614] possible images
in these triplets
[1616] is more similar to the
reference in the middle.
[1619] So if the network says that
image A is more similar to image
[1624] B than it is to image
C, and humans also
[1627] say that image A is
more similar to image B
[1628] than it is to
image C, then we'll
[1630] get a high agreement
with humans.
[1633] So I already told you that
just the Euclidean distance
[1639] between the pixels
doesn't work very well.
[1641] Well, 70%.
[1642] OK, SSIM and these classic
metrics don't work too well.
[1648] And yeah, question?
[1651] AUDIENCE: The last one, human
one, is just human versus human?
[1653] PHILIP ISOLA: This last
part is human versus human.
[1655] It's a noise ceiling.
[1657] How often do two humans agree?
[1660] And these are AlexNet and VGG,
some old neural networks, right?
[1664] I mean, this is a little
bit of older work.
[1666] And these aren't trained
to fit human data.
[1671] This is a classifier.
[1673] This is an image
classifier, again.
[1675] And yet they're
better predictors
[1677] of human similarity judgments.
[1679] They have more
similar kernels to
[1680] the human behavioral
psychophysical
[1682] kernel than all the kind of
classic similarity metrics.
[1686] And it doesn't really matter
what architecture you use
[1689] or if you train these with
supervised data or these
[1692] are self-supervised methods.
[1694] It's all kind of the same.
[1695] Well, not quite the
same, but close enough.
[1699] So there's some details.
[1700] I'm not going to talk
about each of these methods
[1702] and the differences.
[1703] The main effect is just that if
I train a neural network, a deep
[1705] neural network, it learns a
notion of similarity which
[1708] is related to the human
notion of similarity
[1711] by behavioral response.
[1719] So we did another paper
on this just last year.
[1722] So this is a little
bit more up to date.
[1724] And in this paper,
we wanted to--
[1729] in the LPIPS paper, the
last one I showed you,
[1731] we were looking at the kind of
low-level notions of similarity.
[1733] Like if I blur an
image, do I consider
[1735] that to be less similar
than a distorted image?
[1738] And here we're just saying,
take two random photos,
[1740] and they can differ in
a lot of different ways.
[1742] The background can
differ and so forth.
[1743] How similar does a neural
net think those two are
[1746] and how similar do humans
think those two are?
[1748] And do these trends
still hold up in 2023?
[1751] OK, so let's play
the game again,
[1753] just because it's kind of fun.
[1755] So we're going to
do the same thing.
[1756] So you're going to
first clap if you
[1758] think this image is more
similar to this image
[1760] than this image
is to that image.
[1762] OK, clap if you think the left
one is the more similar image.
[1765] OK?
[1766] No?
[1768] Right one.
[1769] [CLAPS]
[1770] OK.
[1770] So, good.
[1773] This is actually
what that model--
[1775] the previous one
I talked about--
[1776] decided.
[1777] Because it was really only able
to model low-level similarity
[1780] very well.
[1781] And AlexNet and
VGG, they kind of
[1783] agreed with humans
on blur and so forth,
[1785] but they didn't agree on these
types of more complicated data.
[1787] OK, another one.
[1789] OK, clap if you
think it's the left.
[1793] Right.
[1793] [CLAPS]
[1794] You see that you have
a lot of agreement.
[1796] And again, LPIPS disagreed.
[1798] So it wasn't sufficient.
[1799] It actually didn't model
humans as well as we thought.
[1802] OK, this is a little bit harder.
[1804] Think about it.
[1805] Left.
[1806] [CLAPS]
[1807] Right.
[1810] I think there might be some
weird bias going on, because
[1813] in this case, actually--
[1815] oh, wait.
[1816] Oh no, I got it wrong.
[1817] No, you're right.
[1818] Because I chose all these--
[1820] these examples are
all examples where
[1822] humans disagree with LPIPS.
[1823] So actually, humans did
think that this one is it.
[1827] I might be mixing left and right
up because I think I'm rotated.
[1830] OK.
[1831] This is pretty easy.
[1833] OK, this image?
[1835] This image.
[1835] [CLAPS]
[1836] Yeah.
[1836] OK.
[1837] So I gave it an easy
one, and actually, LPIPS
[1839] agreed with humans on that one.
[1841] So LPIPS is not terrible.
[1844] But now the question
is, OK, fine.
[1845] So AlexNet actually only
captured low-level similarity
[1848] that agrees with humans.
[1850] What about the newest networks?
[1852] What about CLIP and DINO
and these foundation models,
[1854] the newest generation of
computer vision systems?
[1857] Do they agree with humans on
these more complicated images?
[1861] And it turns out they do.
[1863] So again, this trend
is just holding.
[1865] As time passes, these bigger,
better computer vision systems
[1869] are agreeing with humans
on more types of data.
[1875] So again, the same graph.
[1877] Agreement with human judgments,
some different models.
[1880] You can see the
LPIPS one I showed
[1881] you has a medium agreement with
humans on these complicated
[1884] images.
[1885] But the latest computer
vision systems,
[1888] which are using
architectures which
[1889] are five or six
years after LPIPS,
[1891] are agreeing with
humans much better.
[1894] So just by waiting for better
computer vision systems
[1896] to come out, we get
better agreement
[1898] with human psychophysics.
[1900] You might be asking
yourself, wait,
[1903] but does DINO also agree
on those low level blur
[1905] and so forth?
[1906] And yes, it does, but only
about as well as LPIPS.
[1908] It seemed like LPIPS already
kind of saturated that.
[1911] Yeah, question.
[1912] AUDIENCE: These models were not
trained on the same data, right?
[1917] They have vastly different data.
[1919] PHILIP ISOLA: Yeah.
[1920] AUDIENCE: So it's not
about the architecture.
[1922] They just see more
statistics about the world.
[1925] PHILIP ISOLA: Yeah.
[1927] That's the rough
hypothesis we'll
[1928] get to, that they're
converging to something which
[1931] is like the statistics of the
world, natural image statistics,
[1934] rational analysis
kind of argument.
[1936] Yeah.
[1937] AUDIENCE: Like the transformer
training, medium images
[1940] and the image that [INAUDIBLE].
[1944] PHILIP ISOLA: Yeah.
[1944] So these are trained
on much more data
[1946] than these were trained on.
[1947] And when you train
on more data, you
[1949] get a model which better
matches human perception.
[1952] But they're not trained
to match human perception.
[1954] That's the point.
[1956] OK, yeah.
[1957] AUDIENCE: Just want to
make sure I understand.
[1959] So how do you teach
these models to output
[1961] the pair of similarity, like
A versus B and A versus C?
[1965] What do you do with that?
[1966] PHILIP ISOLA: Yeah.
[1967] So you measure the
distance according
[1971] to the model between
A and B and you
[1973] measure the distance
between A and C,
[1975] and you compare those two.
[1976] And whichever one is bigger
is the model's choice.
[1979] AUDIENCE: Yeah,
but the distance is
[1980] decided by you or by the model?
[1981] PHILIP ISOLA: The model.
[1982] The model outputs a distance.
[1984] Given a pair of images, the
model gives you a distance.
[1990] So I'll just quickly
show-- well, maybe I've
[1993] gone back too many slides.
[1996] AUDIENCE: It's just
the Euclidean distance
[1998] between the embeddings.
[2000] AUDIENCE: Well, why Euclidean?
[2001] This is [INAUDIBLE].
[2002] What are they?
[2003] PHILIP ISOLA: You can
choose other metrics.
[2005] They're all going to be
in pretty high agreement
[2007] with each other.
[2008] But yeah, I believe in fact
we're using cosine similarity.
[2014] OK, yeah.
[2014] Sorry, here it was.
[2016] OK.
[2017] In this paper, it
was the L2 distance.
[2019] But anyway, it's
kind of a detail.
[2021] I don't think it matters.
[2024] OK, so let's get to some
new 2024 experiments
[2029] from this platonic paper.
[2031] OK, so this was all
history and prior work,
[2033] which I think argues
for this hypothesis.
[2037] And we wanted to test
it more directly.
[2040] OK, so we have some similarity
between different computer
[2043] vision systems.
[2046] What we want to look at
next is, is this similarity
[2051] increasing over time?
[2054] And if it is
increasing over time,
[2056] then that suggests there's some
kind of convergence going on.
[2059] Over time, as we train
bigger and better models
[2061] on more and more data, if
they agree more and more
[2064] with each other and potentially
with humans as well,
[2068] then it's like we're all
converging to something.
[2070] And what is that and
how far will that go?
[2072] And the hypothesis is an
investigation of that question.
[2077] OK, so we're going to now run
a study with all of the 2024
[2084] models looking at the kernel
alignment between each
[2088] of these models with
each of the other models.
[2090] We're asking, is one vision
system becoming more alike
[2095] to other vision systems
as a function of time?
[2098] So hypothesis one is
that, no, not necessarily.
[2103] Actually, there are different
ways you can fundamentally
[2106] represent the visual world.
[2108] You could represent it in terms
of edges and textures or objects
[2111] and events.
[2112] There's many different
possible ways
[2114] of being visually intelligent.
[2116] That's hypothesis one.
[2118] OK, maybe Tommy thinks
this is the case.
[2120] And I don't like putting
forth a hypothesis.
[2124] What I'm saying is meant
to be thought provoking,
[2127] but not necessarily something
I strictly believe is true.
[2130] OK, so there's probably
some truth to this.
[2132] But the other possibility
is no, all strong visual
[2135] representations are alike.
[2136] There's only one
way to do vision.
[2138] There's only one way
in this physical world,
[2140] to do computer vision or human
vision or whatever it is.
[2142] There's just one way to do it.
[2144] So here's the first new study.
[2148] So what we did is we took a
bunch of different computer
[2151] vision systems.
[2153] They're all trained-- some
are VITs, vision transformers,
[2156] some are CNNs.
[2158] None are RNNs.
[2159] But anyway, a few
different architectures.
[2161] They're trained on
different data sets.
[2163] Some are even trained on
synthetic data as opposed
[2167] to real data.
[2168] And in this plot here,
I'm going to measure--
[2174] I'm going to sort the
models by their performance
[2177] on this general competency
called the VTAB task.
[2181] So VTAB is just
measuring a vision system
[2184] by how well it does at a
bunch of different things--
[2186] classification, bounding box
prediction, counting objects,
[2189] and so forth.
[2191] And I'm going to
group the models
[2192] into five bins of
competency according
[2194] to the VTAB performance.
[2195] And then we're
going to ask, what
[2197] is the variability within
each bin between the kernels?
[2201] And so on the y-axis
is within the bin,
[2207] how similar are the
representations learned
[2209] by those different models?
[2211] OK, so here's the result.
Well-performing models
[2215] have very similar
representations
[2216] on their embedding layers,
not in their outputs.
[2220] Poorly performing models
are all different.
[2223] So you may recall that this
sounds like the first line
[2227] of Anna Karenina now, right?
[2228] All happy models are alike.
[2230] All unhappy models or all poorly
performing models are different.
[2234] They're poor in their own way.
[2236] Yeah.
[2237] AUDIENCE: But when
you do kernel,
[2240] you have this 1 over
n, this representation.
[2243] So the fluctuation
in the kernel is
[2245] order of 1 over
square root of n.
[2247] So when you have models
with wider layers,
[2255] you have the
fluctuation is smaller.
[2257] PHILIP ISOLA: Yeah, you mean the
dimensionality of the embedding
[2260] is kind of creating a bias.
[2261] Yeah, that's a good question.
[2262] We should systematically
look at that.
[2264] I don't think that's going
to explain much of it
[2266] because most of these
models have similar--
[2269] I don't know.
[2269] Brian, do did we fix the--
[2272] AUDIENCE: [INAUDIBLE]
[2273] PHILIP ISOLA: Oh yeah,
it's also the nearest--
[2275] well, we should think
about it a little bit more.
[2277] AUDIENCE: What happens
when you try to do it
[2279] with the Gaussian process?
[2282] PHILIP ISOLA: So I'm not
sure if we've tried that.
[2286] But we have tried doing
this with just randomly
[2288] initialized networks,
which will vary
[2290] in their embedding
dimensionality.
[2292] And those don't align
with any of these models.
[2296] So if it were just about as
dimensionality goes to infinity,
[2300] you approach some limit
which is convergent,
[2302] then you would expect a
random network would also
[2304] have that property.
[2305] And that doesn't happen.
[2306] We can talk a little bit
more in detail about it.
[2308] I think it's something we should
look at more systematically.
[2310] But I don't think that's
explaining the data.
[2312] So here's just another way of
looking at that same result.
[2316] OK, I'll come back
in just a second.
[2317] This is a UMAP.
[2319] So if you know t-SNE,
it's similar to t-SNE.
[2321] It's just an embedding
where two models
[2323] with similar representations
are near each other.
[2326] In this scatter plot, each
point in the scatter plot
[2328] is a different model.
[2329] And you can see that
the kind of main thing
[2331] that controls how models
cluster, which models have
[2335] similar representations,
is not their architecture,
[2337] it's not their training
data, it's their performance.
[2339] So competent models are all
alike in their representations.
[2342] OK, maybe not too surprising,
but this is the data.
[2345] Yeah.
[2347] AUDIENCE: What's
the set of images
[2348] over which you're
computing the distribution
[2350] of [INAUDIBLE] similarly?
[2353] Like, how sensitive is this?
[2355] AUDIENCE: Yeah,
that's [INAUDIBLE].
[2356] AUDIENCE: [INAUDIBLE] versus
all of our lines versus
[2359] your physically
impossible scenes versus--
[2362] PHILIP ISOLA: Yeah.
[2363] So the kernels are evaluated
in general over this Wikipedia
[2367] image captioning data set.
[2370] Brian, is that true
for this experiment?
[2372] This is Wikipedia data?
[2373] Yeah.
[2373] So it's images
found on Wikipedia.
[2375] I don't know that we've really
looked at the sensitivity
[2378] to different data
distributions for evaluation.
[2380] They're all trained
on different data.
[2381] But for evaluating the kernels,
yeah, it was always Wikipedia.
[2384] That's a good thing.
[2385] We should check that.
[2386] OK.
[2388] Yeah.
[2389] One more.
[2390] AUDIENCE: Does this sort
of dissolve the [INAUDIBLE]
[2394] distract us from those
thoughts [INAUDIBLE]?
[2398] PHILIP ISOLA: We'll get to
that in the implications.
[2401] But you would think, well, OK,
if all good models are somehow
[2403] converging, then just take
them all and ensemble them.
[2407] It should work well.
[2408] They should already be kind
of aligned and ensemble-able.
[2411] So I think that is
an interesting thing
[2413] that you could try.
[2415] But you will have to--
[2417] in order to ensemble,
you'll have to somehow--
[2420] there's a symmetry, which is
that you can get the same kernel
[2423] with differently rotated data.
[2424] Any isometric
transformation of the data
[2426] will have the same kernel.
[2427] So you have to get rid
of that symmetry somehow.
[2432] So that's something that
I think is interesting.
[2434] But a lot of you
might be saying, OK,
[2436] that's kind of obvious.
[2438] Like, two different
computer vision systems
[2440] that perform well in
the same set of tasks
[2442] have similar representations.
[2444] Maybe it has to be that.
[2446] We're not proving this at the
level of the neural collapse
[2448] in the previous talk,
where we are really
[2450] showing that it has to be that.
[2451] But I think intuitively
it kind of-- yeah,
[2453] if my representation is good
for the same set of things,
[2456] then it's going to be a
similar representation.
[2458] But maybe it could
have been otherwise.
[2461] It could have been that
there are equivalently
[2463] good representations for
the same set of things.
[2465] But it's not unreasonable.
[2466] But this is, I think, going
to be the more surprising--
[2468] at least to me, this was a
more surprising experiment.
[2470] Are language models learning the
same kernel as vision models?
[2477] So hypothesis one,
well, no, of course not.
[2480] Language models model language.
[2482] They're going to learn about
syntax and next word prediction.
[2485] They're not going to really
have anything to do with vision.
[2487] And the better the
language model, the more it
[2489] will be a specialist in just
the superficial characteristics
[2491] of language.
[2493] Hypothesis two, no.
[2495] Actually, it's what
Jacob was saying.
[2496] Language models are world models
and they learn general knowledge
[2499] about the world.
[2500] And so the best
language model will
[2502] be the best model of the world,
which will also be a good vision
[2505] model.
[2506] And maybe there's a strong
form, which is like yeah,
[2509] the best language model is
literally the best vision model.
[2511] They actually converge to
exactly the same thing.
[2514] So here, we're going to measure
the similarity between two
[2519] kernels, but now it's a vision
kernel and a language kernel.
[2522] So how do we measure between
two different modalities?
[2525] What we do is we
use paired data.
[2527] So we take the image of an
apple and the image of an orange
[2531] to create the vision kernel.
[2532] And we take the word
apple and the word orange
[2534] to make the corresponding
paired matched language kernel.
[2539] So importantly, the language
models we'll look at
[2542] are trained only on
language data, no vision.
[2543] The vision models we'll
look at are trained only
[2545] on images, no language.
[2547] But in order to evaluate the
similarity of how they represent
[2550] the world, we'll use
paired data to align
[2552] the two kernels in this way.
[2555] So here's the Wikipedia
data that we ran this on.
[2559] And we take a bunch
of images online.
[2561] We take their captions, so
it's an entire sentence.
[2564] We embed the images
with the vision system.
[2567] We embed the captions
with a language system.
[2569] We extract some layer of
the language representation.
[2572] There's technical details there.
[2575] We get these embeddings.
[2577] And then we will measure--
[2579] sorry, we will measure,
is the distance
[2583] between the embedding for
Half Dome and Yosemite
[2587] the same as the distance between
the embedding for the word Half
[2591] Dome and the word
Yosemite Valley,
[2593] or the sentence
Half Dome at sunset
[2595] and the sentence
Yosemite Valley?
[2598] OK.
[2599] So on the x-axis is going to be
the competency of the language
[2605] model.
[2606] So that's going to be measured
as just how good are you
[2608] at next character prediction,
next word prediction.
[2610] It's using a metric
called bits per byte,
[2614] but that's the details.
[2615] Basically, the log likelihood
of the next character
[2618] that you're predicting.
[2619] On the y-axis is going to be the
kernel alignment between each
[2624] of the language models that
we look at versus DINO, which
[2628] is a vision model.
[2630] OK, so what's the
trend going to be?
[2632] OK, we made it into a line
by choosing the right metric.
[2636] Different metrics will
be not quite as linear,
[2638] but they go up and to the right.
[2641] So these are a bunch of
different language models.
[2644] We looked at different sizes--
[2646] bloom, 560 million parameters,
llama, 65 billion parameters.
[2651] Each point is a
different language model.
[2653] And so llama has a
similar kernel to DINO.
[2657] It aligns in the sense
that I gave you to DINO.
[2660] And the worst language
models align worse.
[2663] So better language models learn
representations that measure
[2667] distance in ways that are more
alike to a given vision model.
[2671] And it also goes the other way.
[2672] The better the vision
model, the stronger
[2674] the alignment to
the language model.
[2676] So DINO Giant is a better
vision model than DINO Small.
[2680] And Dino Giant has
higher alignment to llama
[2683] than DINO Small.
[2686] OK.
[2689] So you might wonder, what
about other vision models?
[2691] What about not DINO?
[2693] Well, basically-- oh, sorry.
[2696] What's going to
happen in the future?
[2698] We really don't know.
[2699] OK.
[2699] I think this trend
will keep increasing.
[2702] But maybe we're going to overfit
to language soon and just fall
[2705] off a cliff.
[2705] So it might not hold
up into the future.
[2708] But the same story is true for
a bunch of different vision
[2711] models.
[2712] This is Masked Autoencoder.
[2714] This is CLIP.
[2716] CLIP is interesting
because CLIP is
[2718] trained to align vision
representations to text
[2721] representations.
[2722] So you might have expected that
the CLIP kernel will be really
[2726] well aligned to a llama kernel.
[2728] But it's only a little more
aligned to the llama kernel
[2732] than is DINO.
[2735] OK, MAE is a bit worse.
[2737] It's point one on our metric
and CLIP is point two.
[2740] But the trend is
the same between all
[2741] of these different systems.
[2742] They're all going
up and to the right.
[2745] OK.
[2748] Another interesting
thing is, this is true
[2750] not just for log likelihood
of the next character.
[2753] But now I'm switching the axis.
[2756] I'm going to have on the x-axis
the alignment of a language
[2758] model to vision
and on the y-axis
[2761] is the downstream performance
of the language model.
[2764] So the more similar
a language model
[2767] is to a vision model in terms
of this kernel, the higher
[2772] performance that
language model ends up
[2773] getting on this common
sense reasoning benchmark.
[2779] And the trends are
all kind of aligned.
[2780] So bigger models are
more aligned to vision.
[2783] Stronger models are
more aligned to vision.
[2786] And more recent models are
more aligned to vision,
[2788] because those three
things are all correlated.
[2791] So this does suggest
something we haven't done,
[2794] but we really want to do, which
is, what if I fine tune llama
[2797] to be more aligned with DINO?
[2799] Will performance of llama go up?
[2801] If I fine tune a language model
to be more like a vision model,
[2805] will I do better at
language modeling?
[2807] This is a correlation.
[2808] We haven't done that
causal experiment,
[2810] but hopefully we'll have
something to say on that soon.
[2812] Yeah.
[2814] AUDIENCE: Can you read the
actual numbers on the axis?
[2816] Because I'm having
trouble seeing
[2818] whether 0.2 is
like a large score
[2821] or I guess a
reasonable score, or is
[2824] it just like we're hitting
noise with correlation,
[2828] where you kind of understand.
[2829] PHILIP ISOLA: Right.
[2830] 0.2, is that good
alignment or bad alignment?
[2833] It's definitely
not-- the highest
[2834] you can get on this metric is 1.
[2836] This means that 20% of the
nearest neighbors of model A
[2840] are the same as the nearest
neighbors in model B's
[2843] embedding.
[2845] But that depends on
your dictionary size,
[2847] how many possible candidate
neighbors are there.
[2849] I think it was 1,000.
[2851] Dictionary has 1,000 I think.
[2853] So of the top five
nearest neighbor,
[2858] when there's 1,000 possible
candidates, 20% are shared.
[2862] So that's technically
what it means.
[2864] But I think it's
easier to say, well,
[2867] CLIP, a model trained to
align vision to language,
[2872] learns embeddings which are
not that much more aligned
[2876] to a language model than
these pure vision models.
[2878] So I think that gives
you a calibration.
[2881] AUDIENCE: If I recall correctly,
somehow llama is like 0.8.
[2884] But here you show it's 0.2.
[2886] Isn't that too low?
[2888] PHILIP ISOLA: Sorry, which one?
[2889] AUDIENCE: Somewhere
back in the slides,
[2891] you have this human alignment.
[2892] The score is around 0.8.
[2896] PHILIP ISOLA: Oh, I think--
[2897] oh, in the vision
modalities, it was 0.8?
[2899] Yeah, so there's
technical differences
[2902] between the experiments and
the metrics aren't maybe
[2904] not directly comparable.
[2905] But a vision system is more
aligned to another vision system
[2908] than it is to a language system.
[2910] So the numbers here
are going to be lower.
[2914] AUDIENCE: As a reference point,
the model that you do not train,
[2916] [INAUDIBLE] untrained
is like 0.035.
[2919] PHILIP ISOLA: Yeah.
[2920] So chance is like
0.03 if you just
[2921] randomly initialize a network.
[2924] AUDIENCE: Do you know if
you use the text to confirm
[2926] what that would be?
[2928] PHILIP ISOLA: The text embedding
from clip will be much higher.
[2930] Yeah, this is the
vision embedding
[2931] from CLIP against llama.
[2932] The text embedding from
CLIP against llama,
[2936] I think it's higher,
but I remember.
[2938] Brian, do you know?
[2939] OK, we never ran it.
[2940] So I just assume it's higher.
[2942] AUDIENCE: Yes, the
vision embedding
[2942] from CLIP, which presumably is
like super, super, [INAUDIBLE].
[2945] PHILIP ISOLA: Yeah, I think
it should be pretty high.
[2947] Yeah.
[2948] OK.
[2951] OK.
[2952] So yeah, there's a lot of
other work in this space.
[2956] So I guess this is
just a slide saying,
[2960] read the paper if you want
to get more references.
[2962] There's a whole field around
representational alignment.
[2964] There's workshops.
[2965] At NeurIPS, there's going to
be a representational alignment
[2967] workshop on these questions.
[2969] But I want to move
on now to some
[2971] of our hypotheses
and explanations
[2973] for why this might happen.
[2976] OK.
[2978] So first, I'm going to go over a
few kind of basic ML 101 reasons
[2983] why you would expect
convergence to happen in theory.
[2986] And then I'll go into an
idea for what it might all be
[2991] converging to, if this is true.
[2993] So the first effect from
ML 101 is that if I train,
[2999] here's my hypothesis
space I'm searching over.
[3002] I'm training a model
to solve a task.
[3003] So here's a set of
hypotheses that solve a task.
[3006] If I train a model
to solve one task,
[3008] then it will arrive at
something in this space.
[3010] If I train a model
to solve two tasks,
[3013] it will arrive at something in
this space, or solve task 2,
[3017] it will arrive in
something in this space.
[3019] If I train a model to multitask,
to solve task A and task B,
[3022] or equivalently to do well
on data set A and data set B,
[3026] then we'll be at the
intersection of these two.
[3029] So the more constraints you put
on your machine learning system,
[3034] the more objectives
it has to satisfy,
[3035] the more data points
it has to fit.
[3037] You get a strictly
smaller subspace
[3040] of the hypothesis space,
which is going to fit
[3043] all of those constraints.
[3044] So this is one effect that
could lead to convergence,
[3047] training on more
tasks, on more data--
[3049] and that's what
we're doing now--
[3051] should result in fewer and fewer
valid functions that satisfy
[3054] all of those constraints.
[3056] OK.
[3057] This has also been called
the contravariance principle.
[3062] It's roughly the same idea.
[3063] And also, again, others
have referred to this
[3067] as kind of an Anna Karenina.
[3069] Happy families,
happy representations
[3070] have to satisfy a lot of things.
[3072] Any one thing that goes
wrong, and they'll be unhappy.
[3074] But if you have to
solve a lot of things,
[3075] then it will force
this convergence.
[3077] OK, so this observation has
been out there for a while.
[3080] But I think that
this is part of it.
[3083] OK, here's another, I think,
important condition for us
[3087] to get convergence.
[3088] So we need to have
big enough models.
[3090] Because if you think about
it, if I have two models that
[3093] are kind of small-- so
here's the possible space
[3095] of all functions.
[3096] And here's neural net
A hypothesis space.
[3099] It only parametrizes
some functions.
[3101] Neural net B hypothesis space,
it parametrizes other functions.
[3105] And this ambient space,
actually the minimum
[3107] in the ambient space of the
machine learning problem
[3110] is over here.
[3110] It's not within either of
these hypothesis spaces.
[3113] Then they won't converge
because this guy
[3115] will learn that point and this
guy will learn that point.
[3118] But if I simply
scale up the models,
[3119] I have a greater chance of
finding a solution, which
[3124] I have a greater chance
that the two models
[3126] will overlap on the optimum
in the ambient space.
[3130] So if I scale up two
hypothesis spaces,
[3132] they're going to overlap more.
[3134] And therefore, there will be the
chance that they can actually
[3137] arrive at the same solution.
[3140] So I think that
this is part of it
[3142] too, that we are making
bigger and bigger models.
[3144] And that should have
the effect that there
[3145] is the possibility
of convergence,
[3148] if I also have other constraints
that force me to find solutions
[3151] in a small subspace.
[3154] OK.
[3155] And then another hypothesis
is that, well, here's
[3159] the set of functions
that solve all the tasks,
[3161] but it might still have
a lot of symmetries.
[3163] It might be that
this is a huge space,
[3165] there's a million
functions that fit any--
[3167] n data points can be fit with a
million different curves, right?
[3170] So I need to have
some regularizer that
[3173] chooses which of those
curves I'm actually going
[3177] to pick within this space.
[3179] These are the points that fit
the data, the parameters that
[3181] fit the data.
[3182] But which one am
I going to choose?
[3183] So we know that in deep nets
and all of machine learning,
[3187] you always have some
regularizers, implicit or
[3189] explicit.
[3190] And these are some bias
towards simple functions.
[3192] And so we'll converge.
[3193] And maybe that bias
will be smooth,
[3196] and so it will just prefer us
to push to simpler functions
[3199] and arrive at some
corner of this space.
[3201] So that could be
affecting convergence too.
[3203] And there's a lot of work.
[3204] I think we had some
talks on it earlier,
[3208] that deep nets do have these
types of biases toward low norm,
[3212] low rank solutions,
and so forth.
[3215] So these are kind of machine
learning 101 type explanations
[3218] for why this might happen.
[3220] But I think that they
could be part of it.
[3225] So next, I want
to talk about what
[3227] is the endpoint of all of this.
[3230] This is the most speculative
part of the talk.
[3232] This is all just position talk.
[3233] It is all speculation,
but with some results.
[3237] But the most
speculation is here.
[3239] So here is why we came
up with this name,
[3243] the platonic hypothesis.
[3244] So it goes back to the
idea of Plato's cave.
[3247] So you might have
heard of that story.
[3249] Plato imagined
prisoners in a cave
[3251] whose only experience
of the outside world
[3253] is the shadows projected
on the cave wall.
[3256] And the prisoner's task
is to somehow infer
[3259] what is going on outside
in the real world.
[3262] And it's meant as an
allegory because Plato
[3264] is saying that's how it is
for all of us in real life.
[3267] We don't see reality.
[3269] We just see photons
and waveforms.
[3271] And these are projections,
partial shadows
[3274] of the true platonic ideal.
[3277] And so he had some
ideas around what
[3279] that platonic ideal might be.
[3281] It's cones and squares
and mathematical objects.
[3284] We're not making any
specific claim there,
[3286] but just saying that all of the
data we see is some projection
[3289] or sampling from an
underlying world.
[3292] And that world is common
between all the different ways
[3294] of sampling the data.
[3295] So here we have our real world
out there, our platonic ideal.
[3299] And we can take a
photo of it or we
[3302] can talk about it with language
or we can listen to it.
[3305] And all of the
different modalities
[3307] are projections somehow,
directly or indirectly,
[3310] of that world.
[3311] So here's an
indirect projection.
[3312] I go take a photo and
then I caption the photo.
[3315] But the information
comes from that world.
[3317] And if I train
representations unimodal
[3320] on language and on
vision, well, they
[3323] become similar
because ultimately
[3325] that data is just a function
of that underlying world.
[3328] That's the rough idea.
[3329] Not an incredibly
novel idea, but that's
[3331] the rough idea we're promoting.
[3333] OK.
[3336] So we have a kind of
toy mathematical model
[3339] for starting to work
with this and make
[3342] more precise statements.
[3344] So we're going to imagine a
world which works as follows.
[3347] The world consists of a
discrete set of events, z.
[3351] z is that causal variable that
generates our observations.
[3355] We observe data mediated--
[3358] OK, there's a
distribution over z.
[3360] We observe data and
that data is mediated
[3362] through observation functions.
[3364] We put a huge constraint
on these functions.
[3367] We're going to assume
that they are bijective,
[3370] so meaning the image
contains all the information
[3374] in the world.
[3375] Which is not true,
but that's going
[3377] to be our toy model for now.
[3379] In this world, we're going
to model co-occurrences
[3383] over observations.
[3384] So how often do I see red cone
next to blue cone, for example?
[3391] And this modeling
co-occurrences over observations
[3395] is super common.
[3397] So in computer
vision, we do a lot
[3399] of this contrastive learning.
[3400] We sample two patches,
two co-occurring patches
[3403] in an image.
[3403] And we try to align the two
co-occurring patches and move
[3406] apart two patches from
two different images.
[3409] In language, there are
similar contrastive learners,
[3413] which try to say that car and
street are similar because they
[3416] co-occur together.
[3417] This is like
distributional semantics,
[3420] like meaning is
use kind of ideas.
[3422] So this modeling co-occurrences
and learning representations
[3425] from it is one of the standard
things that people do.
[3429] OK.
[3430] So You can show and
people have shown
[3432] that contrastive learning
with the NCE objective
[3437] converges to the pointwise
mutual information
[3440] between your observations.
[3443] So what is contrastive
learning doing?
[3445] Contrastive learning is
learning an embedding
[3448] f such that the inner product
between image A and image
[3456] B will be related to this
probability ratio, which
[3461] is how often A and
B co-occur divided
[3463] by how often you would expect
them to co-occur by chance.
[3468] This is saying, if I have two
image patches that co-occur,
[3471] I'm going to bring
them together,
[3473] make them have high
similarity to image patches
[3474] that don't co-occur.
[3475] I'll try to push them apart,
make them have low similarity.
[3478] And so that objective
is equivalent
[3482] to the pointwise mutual
information between these two
[3484] objects.
[3486] OK, so contrastive learning
of this particular form
[3489] in this particular
world boils down
[3491] to learning an embedding
in which similarity
[3495] in the embedding space, the
kernel of that embedding,
[3497] is equal to the pointwise
mutual information
[3499] between these observations.
[3504] So that's just saying that if
apples and oranges co-occur
[3506] in the kitchen
together, then they
[3508] will embed close to each other
under this learning objective.
[3511] And elephants will embed
far away because they don't
[3513] co-occur with these two things.
[3517] OK.
[3518] Now, the really
interesting thing
[3520] is that if my observation
functions are bijective
[3523] and my world is discrete, then
these projections don't end up
[3531] changing these probabilities.
[3532] So what this ends up
meaning is that the PMI
[3534] over the observations
x is equal to the PMI
[3538] over the underlying events z.
[3539] So this is a really toy world.
[3543] But in this toy
world, you will expect
[3545] that you'll get exactly the same
kernel if you learn from images
[3551] versus if you learn from text.
[3554] OK, so this is one
toy construction
[3556] in which you will get
convergence, theoretically.
[3560] It matches roughly what we
do in contrastive learning,
[3564] except that we don't
model data which is
[3567] sampled in a bijective fashion.
[3568] And so that's the big
kind of assumption
[3570] that's wrong in this model.
[3573] But I hope it's
a starting point.
[3576] And this does kind
of actually hold
[3579] to some degree in real data.
[3580] So here's a simple
experiment where we are--
[3583] I think, actually, Jacob showed
some results on this line
[3587] as well.
[3588] So you can measure the
co-occurrence of color values
[3593] within images and measure the
PMI between red and green.
[3600] Green and blue have high
pointwise mutual information.
[3602] They co-occur a lot.
[3603] Red and green have lower.
[3604] They co-occur less.
[3605] And you'll recover an embedding
in which blue and green are
[3609] near each other because
they co-occur a lot,
[3611] and blue and red are far from
each other because they co-occur
[3614] less.
[3614] So that's roughly similar
to how you see color.
[3618] You think green and blue are
more similar than red and green.
[3621] It's roughly similar
to the LAB color
[3624] space, which is kind of
how humans see color.
[3626] And if you do the same on
words, the word red and the word
[3629] blue and the word green
and the word yellow,
[3632] you'll get roughly the same
kernel, which gives you
[3636] roughly the same embeddings.
[3639] OK, so this is replication
of some prior work
[3644] from Abdou et al.
[3645] But we ran this on
a few newer models.
[3649] These are a contrastive language
learner, a predictive language
[3652] learner, and they do in fact
learn similar color kernels
[3656] as you get from co-occurrence
over pixel values.
[3661] So just to make that a little
more intuitive, all I'm saying
[3665] is that if you sampled
pixels from an image,
[3669] then you'll be likely to see
two shades of blue co-occurring.
[3673] And that will tell
you if you train
[3675] a contrastive learner, that
will make the two shades of blue
[3678] have a high similarity.
[3679] If you sample color
words from sentences,
[3683] then you'll also probably
have the two shades
[3685] of blue co-occurring, because
people will describe the scene
[3688] and they might
describe the colors.
[3690] And if they describe
blue, they're
[3691] likely to describe turquoise.
[3693] OK, so you'll get a similar
kernel in both of those cases,
[3696] because both of these are
descriptions or observations
[3699] of the same underlying world.
[3700] And as long as those
observations satisfy
[3703] some properties,
in the strictest
[3704] sense being bijective
and so forth,
[3706] then you'll get this result.
But in the more relaxed,
[3710] real setting, I think you might
get a more relaxed version
[3712] of that result. OK.
[3716] OK.
[3717] So finally, I'll
talk a little bit
[3719] about implications
and limitations,
[3721] because you're probably all
thinking, OK, this is cool,
[3723] but you're way overstating it.
[3724] There's a lot of
details that are wrong.
[3726] And it's true, there are a
lot of details that are wrong.
[3728] OK, so let's look
at some limitations.
[3732] So one is that,
hold on, we can't
[3734] get perfect convergence
between language and vision,
[3737] because there are some images--
[3740] some visual experiences
that are just ineffable.
[3742] You can't describe
them in language.
[3744] And there are some
verbal concepts
[3746] which can't be visualized.
[3748] OK, so for example,
how would I talk
[3754] about the experience of
seeing a total solar eclipse?
[3757] Can you raise your hand
if you've seen one?
[3759] Did you see the one
a few months ago?
[3761] Yeah, OK.
[3762] Can you describe that in words?
[3763] You can't tell a friend.
[3765] It was so magical.
[3766] It's ineffable.
[3768] OK, so clearly, your
visual experience
[3770] and your sensory response was
just fundamentally different
[3773] than just talking about it.
[3776] What about this?
[3778] I believe in the
freedom of speech.
[3779] What is the visual
equivalent of that?
[3782] It's an abstract concept.
[3783] Vision is not good at
showing abstract concepts.
[3787] I mean, I could take
a photo of the text,
[3789] but that's a little
bit of a cheat.
[3793] OK, so these are
all cases where you
[3795] don't have this bijection
between the world
[3797] and the observation.
[3799] The text is some abstraction.
[3801] It's like information
is lost, you abstract.
[3804] In the vision case,
maybe people never
[3806] talk about solar eclipses
with a level of detail
[3809] necessary to really
feel that experience.
[3811] So you don't capture
that information in text.
[3814] Nobody talks about it.
[3817] OK.
[3819] Yeah.
[3819] The kind of weird thing
about this is, yeah,
[3821] maybe vision and
language are different.
[3823] But our best vision
systems are trained to be
[3825] aligned with language.
[3826] So we're kind of training
our computer vision systems
[3829] to reduce the world to the
same information as a sentence,
[3832] as a caption.
[3833] And that's working the
best on a lot of tasks.
[3836] So OK, maybe there are some
narrow edge case differences,
[3840] but there's a lot of
shared information too.
[3844] And that might be
the majority of it.
[3847] OK.
[3850] Oh yeah, here's just
an experiment kind
[3851] of investigating that in
a little bit more detail.
[3854] Certainly the word
orange can't capture
[3858] the same representational
complexity
[3860] as a picture of an orange.
[3861] But what about a paragraph
talking about that picture
[3863] of the orange?
[3864] Maybe that is going to
have enough information
[3867] to actually capture the
same kind of representation.
[3870] And in fact, we do
see evidence of this.
[3872] So if we look at alignment
between sentences and images,
[3877] the longer the sentence is,
the higher the alignment.
[3879] So if I look at the
alignment between embeddings
[3883] of five-word
sentences and images,
[3887] the alignment is mediocre.
[3888] And if I look at the embeddings
of 30-word sentences and images,
[3892] it's higher.
[3892] And if I had the embedding of
an entire Shakespearean play
[3896] and an image of a rose,
maybe then Shakespeare
[3901] has described it
in so much detail
[3902] that you'll have
very good alignment.
[3904] So an image is worth a thousand
words, is the idea here.
[3909] OK.
[3911] I think for the sake
of time, I'll say--
[3915] yeah, we can talk
about that offline.
[3917] The alignment's not perfect.
[3918] There's different
ways of measuring it.
[3919] These are technical details.
[3921] But this one comes to
mind for a lot of people.
[3923] OK, maybe I buy the
story about convergence,
[3925] but I don't think you're
converging to reality.
[3927] I don't buy the
platonic part of it.
[3929] You're converging to whatever
the internet reflects
[3932] about the world, which
might be biased and not
[3936] actually about the physical
truth, but just some kind
[3938] of weird misinformation online.
[3942] So maybe all these
models are converging
[3944] and the alignment is
increasing, but that's
[3946] because they're converging to
something superficial or not
[3950] factual or just these kind
of BS machines, these just
[3954] bad language models.
[3956] And that could be
because we're training
[3958] on data, which doesn't
really represent everything
[3960] we care about.
[3961] It's limited in its own way.
[3962] Or maybe our paradigm,
our transformers,
[3965] they're incapable of
doing certain things.
[3968] And so all these models are
incapable of the same things,
[3971] so it looks like convergence,
but not to something good.
[3976] And there also could be
sociotechnical reasons for this,
[3978] because again, we
share all of our ideas
[3980] and everybody wants to do well
on ImageNet classification.
[3983] So we converge to a
visual representation,
[3985] which is good at that,
but not at other things.
[3989] OK.
[3991] But there are a lot of
interesting implications.
[3993] I think one was
pointed out before
[3994] that if these models learn
similar representations,
[3997] you should be able to share data
and knowledge between models.
[3999] You should be able to ensemble
them, distill one to the other.
[4003] So in particular, it should
help if you train your language
[4007] models on images.
[4008] And it should help if you train
your image models on language.
[4011] People are doing this, in fact.
[4012] So unfortunately,
we're not going
[4014] to be able to give much advice
because people are already
[4016] doing it.
[4017] But we're confirming that
that was a good thing to do.
[4022] It should be possible to
translate between modalities
[4024] with minimal paired data
because the kernel should
[4027] be kind of a bridge which
is invariant between the two
[4029] modalities.
[4030] And all you have to do
is map to the kernel
[4033] and then directly map
to the other modality.
[4036] And there's some
interesting papers
[4039] that have used minimal
paired data and kernel type
[4043] methods in order to do these
cross-modal translation tasks.
[4049] There's this old problem
of Molyneux's problem.
[4053] And he wrote this letter to John
Locke a few hundred years ago
[4056] and asked if a person who was
born blind was given sight,
[4062] would they immediately be
able to recognize a cone apart
[4068] from a cube, just
from sight alone,
[4072] having only had
experience with touching
[4074] these objects in the past?
[4076] So do you get this
knowledge transfer
[4078] from one modality to the other?
[4079] And there's recently
some interesting work
[4081] from Pawan Sinha
and others at MIT,
[4083] where they did find, in fact,
that if you give children
[4087] sight who were born blind--
[4089] you do surgery, you correct
their cataracts-- then
[4093] after only a little
bit of learning,
[4095] they are able to
associate images
[4097] with their previous concepts.
[4099] And so it says that you can't
do it with no learning at all,
[4102] but you can do a
little adaptation.
[4103] And I think that's consistent
with this hypothesis.
[4105] If I already have this kind
of platonic representation
[4108] of the world from touch,
then to learn the mapping
[4111] to that representation from a
new modality, all I have to do
[4114] is learn how to map to
that representation.
[4115] I don't have to learn
the representation
[4117] in the first place, so it should
be a lot more data efficient.
[4120] But the main implication is
just that if there really
[4122] is some kind of thing
we're converging to,
[4124] then we should understand it.
[4125] We should characterize it.
[4126] We should know what that is.
[4127] It's an important object.
[4128] So if the hypothesis is
true, at least in part,
[4131] then I think this is an
important thing to study.
[4134] OK.
[4135] Oh.
[4135] So I'll end there.
[4137] I had a set of slides in case
there was extra time, but yeah.
[4140] So it's for a world model.
[4142] OK, we already heard about
world models in language.
[4144] We'll skip that.
[4145] We can talk about that offline.
[4146] OK, so thank you.
[4148] [APPLAUSE]
