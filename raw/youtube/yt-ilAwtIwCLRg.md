---
schema_version: 1
id: yt-ilAwtIwCLRg
type: youtube
title: 'Similarity Alignment: A Missing Link Between Structure, Function and Algorithms'
url: https://www.youtube.com/watch?v=ilAwtIwCLRg
authors:
- Simons Institute for the Theory of Computing
ingested_at: '2026-05-30T20:41:01Z'
content_hash: sha256:2212c97fc044cfbc90cd45ebe1ae5e9cb12ecc6399ae993697b7a1af6e0d73e7
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Simons Institute for the Theory of Computing
  channel_url: https://www.youtube.com/@SimonsInstitute
  duration_seconds: 5654
  caption_track: fetched
  snippet_count: 2035
filter:
  score: 0.7
---
[0] [AUDIENCE MEMBER] Okay.
[173] [MODERATOR] So it's a pleasure
to introduce the next speaker,
[176] and actually, the only speaker
for the afternoon, after that we
[179] will just be having discussion.
[182] Uh Mikhail Chokhlovski,
he comes from the Flatiron
[188] Institute near here,
and he will talk about
[191] similarity alignment,
the missing link between
[193] structure, function,
and algorithms.
[195] All
[196] [MISHA CHKLOVSKII] Right.
[198] Thank you very much
for having me here.
[201] It's always a pleasure.
[203] So,
[206] I think there were enough
talks this workshop already
[211] to convince you that with all
the explosion in neuroscience
[218] data acquisition from neuronal
population activity to
[225] connectomics, there is an
urgent need for a theory
[229] that would explain or account
for all these observations,
[235] but also relate them to
the computation that
[241] the brain carries out.
[244] Right?
[245] So, what kind of theory
could fit this niche?
[249] That's what I would like
to address in this talk.
[253] Now
[255] these days can't
give a talk without
[258] mentioning deep learning.
[260] So here is a slide
comparing what deep
[265] learning networks do and the
biological neural networks.
[271] So one difference is that in
most cases the deep learning
[278] networks are used in
supervised setting.
[282] They're trained on
huge labeled datasets.
[286] Yet in biology labeled
examples are rare.
[292] And most of the learning
I think happens in an
[295] unsupervised setting with
just very few labels involved.
[300] So, more like maybe
a semi-supervised if
[302] you want to push it or
reinforcement learning,
[305] but not a supervised setting.
[308] So, that's one major difference.
[309] And the other major difference
is that in constructing those
[314] networks computer scientists
typically don't care whether
[318] they're biologically
plausible in a sense
[321] that they use learning
rules that are non-local.
[326] Meaning that the synaptic
weight is adjusted based
[330] on the activity of a lot of
other neurons in the system,
[334] not just the two neurons that
the synapse connects, which is,
[337] of course, the only thing that
biology would allow in a real
[341] brain just because physically,
a synapse has access only to the
[345] activity of those two neurons.
[347] [AUDIENCE MEMBER] So,
I can't resist pointing
[349] out that you're right about
back prop, but the Boltzmann
[352] machine-- That's right.
[352] --which also has a
version is heavier.
[356] So, it's not a, That's right.
[358] [MISHA CHKLOVSKII] Yeah,
I'm referring, yes.
[360] [AUDIENCE MEMBER] It's not that,
it's a important comment about
[362] the current generation that
is The very efficiently
[366] being put to use, but it,
it's not a restriction on
[370] being able to do deep learning.
[372] [MISHA CHKLOVSKII] Right.
[373] Um, and also both machine is,
can be used in unsupervised
[376] mode, so that's not
what I'm comparing.
[379] Right, thanks.
[380] Yeah, that's an important point.
[383] Um, well, so that's why I'm not
that enthusiastic about using
[389] deep convolutional network as
the theory that connects
[395] experiment to computation.
[398] Even though there is a
similarity between the two.
[401] Um, okay, I made the slide
before Tally's talk, okay?
[405] So now I would say less poorly
understood than I thought.
[414] Nevertheless, my mathematician
colleagues tell me that this
[417] kind of similarity is not
a good reason to use this
[422] as a model of that.
[425] So we would like to come up with
an alternative kind of framework
[434] that would be built by
what we call a normative
[437] algorithmic approach.
[439] Okay?
[439] So we would like to start with
some sort of computational
[442] objective that is motivated
by the computational task
[447] that the brain performs,
so that's the link to
[449] computation, right?
[451] So we will focus on object
categorization, which is what
[456] convolutional networks also do,
but in unsupervised settings.
[459] So it would be clustering
in the first part of the
[461] talk and manifold learning
or disentangling in the
[464] second part of the talk.
[466] Once formulating this objective
mathematically, we would like
[469] to derive an online algorithm
that optimizes this objective.
[475] What do you mean by
an online algorithm?
[477] Well, that's an algorithm
which operates in a
[480] biological setting,
biologically plausible
[482] setting, where data is
not available all at once.
[485] It is streamed to the
brain by sensor organs
[488] one sample at a time,
and the brain cannot
[490] wait too much before
computing the output.
[494] So the output has to be
produced on the fly in real
[497] time and without requiring large
memory storage capacity, right?
[502] So you cannot, like,
it's done in classical
[506] machine learning or
statistics algorithm.
[508] You cannot load all the data
into RAM and crunch it there.
[511] That's not a biologically
plausible mode, at least
[514] not on the level,
mechanistic level
[516] of individual neurons
and microcircuits.
[518] Okay?
[518] That's the level
we are addressing.
[520] So the goal is to derive
an online algorithm and
[523] then to map that algorithm
onto a neural network.
[526] In some sense,
to derive a neural
[528] network architecture
whose dynamics, both
[531] neural activity dynamics
and synaptic plasticity,
[535] will carry out the steps
of the online algorithm.
[539] And what's crucial, we will
want to ensure that we are
[544] not violating the biological
requirement on the locality of
[549] learning rules, that they're
Hebbian or anti-Hebbian only.
[553] Okay?
[553] So that's kind of our program,
and I have to admit that
[556] it's not entirely new.
[558] You know, even in the '90s
people have used this
[563] kind of approach.
[564] You know one famous
example is of course,
[567] Bruner's sparse dictionary
learning, where starting with
[572] the objective minimizing L1
regularized reconstruction
[576] error they derived an online
algorithm which actually does
[579] map onto neural network,
which in some architectures
[583] gives local learning rules.
[584] Okay?
[585] So this program has been also
followed by other people.
[590] But what we did differently
is we started with a different
[595] computational objective,
and that allowed us to
[599] resolve some problems that
existed with reconstruction
[602] error minimization approach,
but also gave some interesting
[606] results that I think is valuable
not just to understand how the
[612] brain works, but in general
for machine learning.
[617] So before I tell you
what our approach is,
[623] I want to motivate it by
showing you an experimental
[629] result that was obtained by
functional MRI in a human
[635] inferior temporal cortex.
[636] This is a higher visual area.
[639] And what they did,
they basically showed
[643] their subject 100 different
objects and recorded neural
[649] activity vectors, okay?
[651] Where each component vector
is activation of a voxel in
[656] fMRI image, and then they
computed inner products or
[660] correlations between all
pairs of such vectors,
[663] between pairs of such
vectors corresponding to
[667] all pairs of the objects,
and they filled up this
[671] similarity matrix.
[673] Okay?
[675] So if the two objects produce
similar activity patterns in
[680] IT, they're shown by blue pixel.
[683] Dissimilar activity patterns,
they're shown by red pixel.
[686] And immediately you can see this
log diagonal structure which
[690] seems to align with animate
and inanimate categories,
[694] suggesting that the activity
patterns corresponding to
[698] animate objects are more
similar to each other than
[700] animate to inanimate.
[702] Okay?
[703] [AUDIENCE MEMBER] What's the
scale of the --I mean, is like
[706] both dark blue mean like perfect
100% correlation or is this like
[710] maximum at 30% correlation?
[713] [MISHA CHKLOVSKII] That's
a good question.
[714] I don't actually remember.
[715] This data is taken from series
of papers by Kriegeskorte.
[721] You know, I would say it's
probably --Well, okay, here's
[726] the way to answer this question.
[727] The diagonal, right,
shows perfect correlation.
[732] So that's the color
corresponding to
[735] [AUDIENCE MEMBER] One.
[735] Well, it shows, I mean,
does it show--Do you show
[739] the same thing twice?
I mean, that's the diagram.
[741] [MISHA CHKLOVSKII] Yeah.
[742] So there is a little bit
of a spread there too.
[744] I don't remember exactly
how much spread there was
[748] But you know, it's pretty high.
[750] Okay.
[754] Anyhow, so this is the
similarity matrix that
[757] was measured in one--Oh,
[759] You have question?
[761] [AUDIENCE MEMBER] So how do they
figure out to order the rows
[763] and columns in this particular
way to see the structure?
[765] [MISHA CHKLOVSKII] Oh,
so these are animate objects.
[767] [AUDIENCE MEMBER] Yeah.
[768] But how do you figure
out that you should group
[770] objects by animate and body,
face and that sort of stuff?
[772] It's a pretty non-trivial
[774] [MISHA CHKLOVSKII] --well,
there have been there has
[776] been prior knowledge that the
way those objects are presented
[780] may have some separation.
[782] Oh.
[782] [AUDIENCE MEMBER] So this is
purely on prior knowledge,
[784] there's no training of,
there's no algorithm that you're
[786] [MISHA CHKLOVSKII] No,
no, no, no.
[787] They just
[787] Oh, wow.
[788] Yeah, they just ordered it
basically animate this way
[791] and inanimate that way.
[793] [AUDIENCE MEMBER] They just
decided to do it like that.
[793] Okay.
[794] [MISHA CHKLOVSKII] Yeah.
[795] Yeah.
[795] There's no training.
[796] [AUDIENCE MEMBER]
Follow-up question.
[798] How do you measure the
similarity of two activities?
[801] [MISHA CHKLOVSKII] So
this is just correlation.
[803] So this is just
the inner product,
[804] normalized inner product.
[806] You can also compute distances.
[809] But yeah.
[812] Okay.
[814] So this is the observation.
[816] You know, some people find it
more surprising than others,
[819] but what I think is really
amazing is that if you compute
[825] the similarity matrix for
different individuals,
[830] you will get a very
similar similarity matrix,
[833] even though individual activity
patterns in the brains of those
[838] individuals that correspond
to the same stimulus could
[841] be very different, right?
[843] Because the neurons
between the individuals
[846] are not identifiable.
[847] There could be even a
different number, okay?
[849] Yet the similarity matrix
is invariant, and it's so
[853] invariant it's scary, okay?
[855] Because this is a similarity
matrix from a monkey IT, okay?
[861] And it's obtained not by fMRI,
if anyone doesn't take this
[867] fMRI evidence seriously, but by
single unit electrophysiology.
[873] Okay?
[873] So this is similarity computed
on activity vectors where each
[877] component is a fire rate of an
individual neuron in IT of a
[881] monkey, and you get pretty
much similar structure.
[885] [AUDIENCE MEMBER] And it's
a human face for the monkey
[887] and not a monkey face?
[889] [MISHA CHKLOVSKII] Well,
there are both monkey
[890] faces and human faces.
[892] I, I mean, I'm sure when you
zoom into the details, you
[895] will see differences here,
but on the animate and
[897] inanimate, I think it's,
it's all pretty similar.
[902] Okay?
[904] So I think this is amazing
that similarity matrices,
[910] but not activity patterns
are the invariants between
[915] different neural representations
of different individuals.
[920] Since that data come out there
are some more indication that
[925] this is indeed the case.
[926] The latest ones are still
unpublished works in the
[931] olfactory system, both in
mammals and invertebrates
[935] which show very well that,
again, even though activity
[940] patterns in piriform cortex
or mushroom body may be very
[946] different from individual
to individual, similarity
[949] matrices computed for each
individuals are invariant.
[953] [TALIS] The dimensionality here
is different as supposed to be
[955] [MISHA CHKLOVSKII] --no,
the dimensionality is
[957] determined by the dataset, but--
[960] [TALIS] Is measured on
some vector of --Ah,
[963] [MISHA CHKLOVSKII] The
internal dimensionality is
[965] of course very different.
[966] [TALIS] How different
do you mean?
[969] [MISHA CHKLOVSKII] I don't know.
[970] I think it's probably
higher here because they
[974] recorded from many neurons
because they just, you know,
[977] maybe dozens of neurons.
[980] And here, these are single
unit electrode recordings.
[985] In the human?
[985] In the human fMRI.
[986] So these are voxels
[987] --i'll try a different
[987] --but
[988] It is not that big.
[989] I don't know how many
voxels there are.
[991] Okay.
[991] But I suspect that here
the folded dimensionality
[995] is slightly bigger.
[996] [TALIS] It's a little bit
too good to be true, maybe.
[999] [MISHA CHKLOVSKII] Maybe, maybe.
[1000] But the olfactory-- So you can
argue because this is not--
[1003] This is fMRI, okay?
[1005] You don't know what
happens in those voxels.
[1007] These are single unit
recordings so you combine
[1009] from different trials,
but the olfactory data
[1011] that is still unpublished
is, comes from calcium imaging.
[1015] So it's a population activity,
and it's very hard
[1018] to argue with it.
[1021] Okay.
[1022] So this kind of observation
makes you understand why
[1028] thinking about neural
representation as
[1030] a representation
of similarities,
[1032] as was pointed out
in a long paper by
[1034] Shimon Edelman in
'98, is a good idea.
[1037] Okay?
[1038] If something is
invariant, right?
[1040] That may be something that
biology really cares about.
[1046] So that's kind of the
starting point for us.
[1051] But the question we
addressed is, okay,
[1054] so we're going to
use similarity as the
[1057] neural representation,
but the big question is,
[1060] how do you get that
similarity matrix, right?
[1064] Because the similarity
matrix is not the same in
[1068] every visual area, right?
[1070] This is similarity
matrix in IT, right?
[1073] And if you record activity
in V1 in response to the same
[1078] set of objects, you of course
don't see the structure because
[1081] V1 does not care whether the
object is animate or inanimate.
[1085] It cares about edges, and if the
edge statistics is normalized
[1089] between animate and inanimate,
you won't see much structure.
[1093] So that's exactly what happened.
[1094] So how does the brain
get from this kind of
[1098] similarity matrix to that
kind of similarity matrix.
[1102] And what I would like to do is
to say, okay, if we view neural
[1107] computation as a transformation
of similarity matrix we can
[1112] actually make progress.
[1114] And the zeroth order
way to think about it,
[1118] which might seem a little
bit counterintuitive given
[1120] the previous slide, is what
we call similarity alignment.
[1124] Basically, what you want
to do between the inputs
[1126] and the outputs of a single
layer of a neural network
[1129] is to match similar output
similar input activity to
[1135] similar output activity.
[1137] Okay?
[1138] So it's like multidimensional
scaling or manifold learning.
[1143] You're trying to
preserve distances
[1146] between nearby stimuli.
[1148] Of course,
what this
[1149] doesn't tell you,
what you do with
[1151] remote stimuli,
and that's where
[1154] the whole game
is played, okay?
[1156] And that's why by applying this
transformation multiple times,
[1159] we think you can get from
this similarity matrix to
[1163] that similarity matrix.
[1166] [AUDIENCE MEMBER] Would it be,
you know, a friendly amendment,
[1170] would it be a little
more meaningful to
[1174] think of, you know,
that the computation is
[1179] transforming you know,
achieving similarity between
[1182] stimuli that are evolutionary
useful to be considered similar?
[1187] You see what I'm saying?
[1188] That, that, um
[1191] [MISHA CHKLOVSKII] --yeah.
[1191] So how this came about--
[1194] [AUDIENCE MEMBER] Right, right.
[1194] Yeah.
[1195] No, no.
[1195] But what I'm saying
so, you know, is that,
[1196] is that is that like I
understand similar in
[1200] animate and inanimate.
[1200] Right.
[1201] Because this is a
incredible because that's
[1207] a fantastic dichotomy.
[1208] Okay?
[1209] That has a lot of prey and
predator, is another thing.
[1214] [MISHA CHKLOVSKII] Right.
[1215] Right.
[1215] Right.
[1216] [AUDIENCE MEMBER] But I
mean, sort of, I don't
[1219] know boring animals and,
you know, so may not be a.
[1228] [MISHA CHKLOVSKII] I agree,
but I think that if I really
[1230] follow this line of questioning,
we run into the limitations of
[1233] unsupervised setting, right?
[1235] We have to say, "Well,
you can't just, like,
[1237] analyze images and get
all this stuff out.
[1239] You have to think about
behavioral goals and-"
[1242] It was
[1243] [AUDIENCE MEMBER]
Supervised, though.
[1243] [MISHA CHKLOVSKII] Right.
[1244] So, but we are not
going that far.
[1246] Okay.
[1246] For this talk only,
we're staying in
[1248] the supervised--
unsupervised setting,
[1251] and which is probably
okay to deal with the
[1253] first few layers because
those representations will be
[1257] used for all different tasks.
[1261] [AUDIENCE MEMBER] I wonder if,
so for the figure on the left--
[1265] [MISHA CHKLOVSKII] Yeah.
[1265] [AUDIENCE MEMBER] It
seems very messy.
[1266] Yeah.
[1267] You're using the categories
and clusters of high-level
[1269] objects they're using for
the figure on the right.
[1271] [MISHA CHKLOVSKII] Yeah.
[1272] [AUDIENCE MEMBER] So I wonder
if you use something like
[1274] similarities between edges and--
[1275] Oh, yeah.
[1276] --ratings and stuff,
you'll get a very nice.
[1277] [MISHA CHKLOVSKII] Yeah.
[1278] And in fact, I have a plot.
[1279] I'm sorry, I don't have it in
this PowerPoint, but I have a
[1282] slide showing that if you plot
edge orientation similarity,
[1287] then you get a beautiful
two-banded structure just
[1290] as you would expect.
[1291] Yes.
[1293] [AUDIENCE MEMBER] So maybe that,
I think that, what I'm trying
[1295] to clarify then is that your,
your previous slide said
[1297] that you're trying, you,
you wanna map the input,
[1299] similarity in the input
space into similarity
[1302] in the neural space.
[1303] But here,
we're seeing
[1304] similarity in a
psychological space.
[1305] So is--
[1306] [MISHA CHKLOVSKII] Right.
[1306] So what I want to--
[1309] Yeah, that's confusing.
[1310] I'm sorry.
[1310] I know this problem exists.
[1313] What I want to talk about is a
transformation taking place in
[1316] each layer, in one layer only.
[1318] Okay?
[1321] I don't have a full answer to
how stacking those layers will
[1325] get you from there to here, to
the psychological similarities.
[1329] But I think that for a single
layer, you can think in zeroth
[1333] order that you just preserve
the distances between
[1336] nearby objects.
[1338] Okay?
[1338] But we will see why we think
it's likely that this can give
[1341] you a psychological similarity
towards the end of the talk,
[1345] but it may not be clear.
[1347] Yes.
[1351] [AUDIENCE MEMBER] All right.
[1352] [MISHA CHKLOVSKII] Okay.
[1355] So let's set up some simple
computational problem, right?
[1358] Since we're talking
about categorization,
[1361] which deep learning,
of course, does extremely well,
[1363] we're going to do it in
an unsupervised setting.
[1366] So in the pixel intensity space,
the difference between animate
[1369] and inanimate objects in the
simplest case would be just
[1372] like this kind of two clouds
of data that may perhaps
[1377] be linearly separable.
[1379] Okay?
[1379] This doesn't have
to be the case.
[1381] The manifolds can be entangled.
[1382] That's what we deal, we'll
deal with part, in part two.
[1385] But in part one,
we will just do
[1387] unsupervised clustering of
this linearly separable dataset.
[1392] [AUDIENCE MEMBER] Okay?
[1393] [MISHA CHKLOVSKII] Well,
you may think, "Well,
[1394] what's the big deal?"
[1395] Right?
[1396] There are tons of clustering
algorithms and networks, and I
[1400] would argue that actually none
of those existing algorithms,
[1405] at least the ones that I know
of, pass our requirements for
[1411] biological plausibility.
[1412] Right?
[1413] So these algorithms are mainstay
of statistics, of course,
[1417] but they're all offline.
[1419] Okay?
[1420] Even if you have online
K-means algorithm for example,
[1426] like the implementations by this
neural networks, you may have
[1431] something that works online,
but when you look at the
[1436] specifics of the winner take
all dynamics in those networks,
[1439] they don't really respect the
locality of the learning rules.
[1444] At least that's my understanding
from reading those papers.
[1447] So that's why we figured we
had to build this from scratch.
[1453] [TALIS] But whether
clustering works online or
[1456] not depends on algorithm.
[1458] Depends on?
[1459] Essentially, the,
the online version of
[1462] K-means for generations.
[1463] [MISHA CHKLOVSKII] I agree.
[1464] [TALIS] And, you know,
some sort of algorithm.
[1466] It just looks--
and they work
[1468] perfectly as--
when we have
[1470] well-separated clusters.
[1471] [MISHA CHKLOVSKII] Yes.
[1471] [TALIS] And they fail
miserably the, the--
[1473] but K-means also
fail miserably.
[1474] Any, all of those algorithms
essentially are hard,
[1477] MP-hard in the worst case.
[1479] So, it's not really clear,
I mean, what do you require.
[1483] [MISHA CHKLOVSKII] Right.
[1483] So the, their algorithm has
passed the online requirements,
[1487] but there isn't a neural network
with local learning rules so
[1493] that synapses are only habit
and anti-habit derived from
[1497] a principled objective.
[1499] That doesn't exi--
that did not exist.
[1502] In fact, you are correct,
and I'll go, I will show
[1505] you a network that
implements K-means online in
[1508] a biologically plausible way.
[1510] But we have to work for that,
[1512] [AUDIENCE MEMBER] Okay?
[1514] [MISHA CHKLOVSKII] So right.
[1516] So okay.
[1518] So that's why I will ask you
to bear with me a little bit.
[1522] There is a little bit
of an unusual thinking
[1524] about clustering,
okay that we had to do
[1528] so that we generate an
objective function that
[1531] then can lead to an online
algorithm and a neural network
[1534] that has local learning rules.
[1536] So it may look a little
bit weird in the beginning,
[1539] but it basically is very
close to K-means.
[1542] Okay, so what we have is
these two clouds of points.
[1545] We would like to ge--
in the X1, X2 input space,
[1550] and we would like to generate an
output which is this assignment
[1555] indices that is one zero for
red cluster and zero one for
[1560] the blue cluster, okay?
[1563] And we can do it very
easily if we think not in
[1567] a centroid-based way like
you usually do in K-means,
[1571] but in similarity-based way,
sort of like is done in
[1575] hierarchical clustering
maybe, right?
[1577] So if the two points are
sufficiently similar, right,
[1581] you want to assign them to
the same output vector.
[1586] If the two points
are dissimilar,
[1590] you want to assign
them to different
[1593] assignment indices,
which happen to
[1595] be orthogonal.
[1597] This can be easily accomplished
by simply thresholding the
[1601] input similarity, right?
[1603] If you think of input similarity
as just an inner product of the
[1608] stimuli T and tau, then if you
thresholded it we threshold
[1613] at alpha so that the output
is one here and zero here,
[1618] you will get the desired result.
[1620] Of course,
you would have
[1621] to choose alpha in
a way that you know,
[1624] these points are more
similar than alpha and
[1627] these points are less
similar than alpha.
[1629] But basically,
that will achieve
[1631] this goal, right?
[1631] Because what does one mean for
output similarity since the norm
[1636] of this factor has to be one,
it would have to be one of
[1642] those two and they would have
to be aligned, that means you
[1647] assign them to the same cluster,
and zero means you end up in
[1652] different clusters because
the assignment indices are,
[1655] assignment vectors
are orthogonal.
[1656] Is there a question?
[1657] [AUDIENCE MEMBER] Yeah,
just a basic question.
[1658] So are you assuming that
somehow the similarity function,
[1662] the business function is kind of
known to say this underlying
[1667] neural circuit that is
performed this operation or?
[1670] [MISHA CHKLOVSKII] Here,
it's just an inner product.
[1672] [AUDIENCE MEMBER] Right.
[1673] But are you assuming that
talking about the brain, right,
[1676] but somehow that similarity
function is built in?
[1679] Um--
[1680] [MISHA CHKLOVSKII] Right.
[1680] So the goal of,
the reason why I had
[1682] to redo the clustering
from bottom up is that
[1685] we want to do it in a way
that a neural network could
[1689] do with local learning rules.
[1691] So we can do this kind of
similarity, we cannot do a
[1696] Gaussian kernel, for example.
[1698] I don't know how to
do a Gaussian kernel.
[1702] [AUDIENCE MEMBER] This so
I mean, your clustering
[1705] needs just one input,
but your similarity
[1708] function needs two inputs.
[1710] So is the one input in the
similarity function a prototype
[1714] [MISHA CHKLOVSKII] Or?
[1714] No, no.
[1715] Eh, this is applied to
a pair of inputs, okay?
[1718] Yeah.
[1718] Oh, sorry.
[1719] Okay.
[1719] So what I should have said is,
let's forget about the online
[1722] requirement for a second.
[1723] We will just derive the
objective function and
[1725] then we'll do it online,
and surprising as it is,
[1729] even though the objective is
derived in the offline setting,
[1733] we will be able to come up with
an online algorithm, okay?
[1737] So-- I,
[1738] [AUDIENCE MEMBER] I
guess I'm confused that--
[1739] Yes, for classification,
I just need one in the end once
[1742] the system has been trained--
[1743] Yeah, I need just one
point in input space,
[1745] and then I can tell is
it this or that class?
[1747] Right.
[1747] But if I refer to similarity,
I need two points in order to
[1750] calculate the similarity.
[1751] [MISHA CHKLOVSKII] You
are correct.
[1752] [AUDIENCE MEMBER] So I
can say these two points
[1754] are close to each other
or these are far apart,
[1756] but it doesn't there's something
[1758] [MISHA CHKLOVSKII] Missing that
[1758] [AUDIENCE MEMBER] Allows
me clustering.
[1759] [MISHA CHKLOVSKII] You're
absolutely correct,
[1760] and that's why similarity
things it seems like a very
[1765] counterintuitive concept to
use for online clustering
[1767] because you would need to
compare with every other
[1771] stimulus, in fact, right?
[1773] Just a century.
[1773] So, huh?
[1775] [TALIS] Just with a century.
[1776] [MISHA CHKLOVSKII] Exactly.
[1777] So, what we're doing now
is we're just deriving the
[1780] objective, not worrying about
the online for a second, okay?
[1783] So imagine that all
the data is up there--
[1785] [AUDIENCE MEMBER] But the second
X, is that then a representative
[1788] prototype or central-- Yes.
[1790] [MISHA CHKLOVSKII] Imagine
Okay.--imagine that
[1791] you have all the data
points, right? So here,
[1795] we're just looking at two, but
we'll have all the data points,
[1797] and I just want to derive an
offline objective that will
[1800] give you a clustering solution.
[1801] [AUDIENCE MEMBER] Okay.
[1802] So essentially,
you are making
[1803] the point that
basically used in
[1805] manifold learning
that, you know,
[1807] Euclidean space only,
or Euclidian space the
[1810] Euclidian distance globally
doesn't make sense, but locally,
[1813] it makes a lot of sense.
[1814] So this is like the zeroth,
like other approximation
[1818] towards geodesic?
[1819] Yes.
[1819] Distance.
[1820] Yeah.
[1821] If there are three or
more clusters and then
[1823] if they're dissimilar,
it doesn't tell you very
[1824] much about where they
should be put, right?
[1827] [MISHA CHKLOVSKII] That's true.
[1828] In hard clustering,
they're just orthogonal
[1830] assignment factors, so it
doesn't tell you much, yes.
[1835] So anyway,
so we want
[1836] to threshold,
so what kind of
[1837] objective would
give me this kind of
[1839] thresholding operation?
[1840] Well, this is one, okay?
[1842] So we're going to maximize
with respect to this assignment
[1847] indices whose norm is limited
to 1 and the components would
[1852] have to be non-negative,
this kind of expression.
[1855] Okay?
[1856] It's easy to verify that
this indeed does what we
[1858] want to do if the similarity
is greater than alpha,
[1861] the parenthesis is positive,
and that means to maximize this,
[1866] we choose the maximum value
of the inner product of y's,
[1869] which is 1 of course
because their norm is 1,
[1872] but that means that the y's
are aligned, that means they
[1874] belong to the same cluster.
[1876] Okay?
[1876] So that's this part.
[1878] If similarity is
less than alpha,
[1880] the parenthesis
is negative,
[1882] we want to choose
inner product of y's as
[1886] low as possible because the
components are now negative.
[1890] The best way to do it would be
to set them orthogonal, that is
[1893] assigned to different clusters.
[1895] [AUDIENCE MEMBER] I see.
[1895] So this is summed over
T and tau basically?
[1898] [MISHA CHKLOVSKII] Okay.
[1899] So this point,
these are just
[1900] two points.
[1901] I see.
[1902] And for two points,
it will give you what we want.
[1905] The question is,
will it work for
[1907] the whole dataset?
[1909] Can we just sum over T and tau?
[1912] That's not a easy question
to answer because you see
[1916] the same YT is used in
different pairs, of course.
[1920] So the different inner products
are actually not independent,
[1925] and that's why it's not clear
whether it will work or not.
[1929] But it turns out that it's
pretty easy to prove a theorem
[1933] that if it so happens that
the similarity between all
[1941] the pairs within the same
clusters are greater than
[1944] alpha and similarities of
any two points from different
[1947] clusters are less than alpha,
then indeed this
[1950] solution will work.
[1952] So you just set the positive
elements of the input
[1956] similarity to the max,
the negative elements to the
[1961] min, which is orthogonal, and
out comes the cluster picture.
[1965] Okay?
[1965] Of course,
you would have
[1966] to choose alpha,
such alpha doesn't always
[1968] exist, of course, right?
[1970] But if we assume that our
data has well segregated
[1973] clouds so that distances
between points from different
[1977] clouds are greater than
distance between any pair
[1980] of points within the same
cloud, then such alpha exists,
[1983] and we can cluster by just
solving this objective.
[1988] Okay?
[1989] So then we can go from this
you know cartoon of that
[1995] fMRI of IT with animate and
inanimate objects and cluster
[2001] them have these two blocks of
ones and zeros, meaning that
[2004] we assigned all these stimuli
to pets, these are to plants,
[2008] and this could be represented
by just two neurons because
[2011] they're two categories.
[2012] Okay?
[2014] So that's
pretty straightforward.
[2016] Um, wha-- wh-- but, but, you
know, K-means would do that too,
[2020] So why did we do all that?
[2022] Well, we did all that
because with this kind
[2027] of objective function,
we can actually solve this
[2031] problem in an online setting.
[2034] Even though,
as Lawrence
[2036] point out you need
two examples to compare,
[2043] to compute similarities,
and they are not available at
[2046] any given time step, you only
go given, are given one, okay?
[2051] You can still
solve this problem.
[2053] And the answer,
as Talis suggested,
[2055] has to do with appear--
appearance of the centroids.
[2058] The way the centroids appear
is-- Oh, by the way I,
[2062] I forgot to say one more thing,
that this constraint on the
[2065] amplitude on the norm of Y
is just here implemented by
[2070] Lagrange multiplier Z to make
this biologically plausible.
[2075] But it's basically
the same problem.
[2076] Okay, so how does this happen
that we can just use centroids?
[2080] This is the central line.
[2082] Okay?
[2082] So if you understand this, you
understand similarity alignment.
[2086] Basically the tricky term here
is this quadratic term that has
[2091] these different two different
axes and two different y's,
[2095] and we can transform it by
bringing the sum over tau
[2099] inside, into this parenthesis,
and calling that sum WYX.
[2109] This immediately allows
you to perform optimization
[2112] online because this is such
a big sum over many samples
[2118] that you have seen,
it doesn't really change much
[2122] from time step to time step.
[2125] And whenever you
get a new stimulus,
[2127] you can use WYX from
the previous step.
[2131] You don't really need to
know the current Y tau.
[2137] So all you have to do is then
to optimize a quadratic function
[2143] with respect to YT, which is
now the current stimulus
[2148] that is available to you.
[2150] There is a non-negativity
constraint and there is also
[2155] this other term coming from
alpha and from Z, that's why
[2161] the actual iteration looks a
little bit more complicated,
[2165] but basically what is happening
here is you can solve this
[2171] optimization at every time step
for a given XT by dynamics of
[2177] neural activity in a reasonably
looking, biologically
[2180] looking neural network.
[2182] Okay?
[2183] Because so this
quadratic-- Uh, sorry,
[2186] this is not even quadratic term.
[2188] This is linear term--
[2190] [TALIS] Bilinear.
[2191] [MISHA CHKLOVSKII] Bilinear
term, sorry.
[2194] Results in just simply matrix
vector multiplication that is
[2199] naturally implemented if the
activity vector is carrying
[2204] the components of X and then
the matrix W consists of
[2211] synaptic weights in this
feedforward connections.
[2215] So that would compute
W times X, okay?
[2219] Now this term arises from
a cross-term between Y and
[2224] Z through the same kind of
trick and it has to do with
[2228] the normalization of the
assignment indices and it can
[2234] be implemented by representing
Z by the activity of one other
[2238] neuron which is naturally
viewed as inter-neuron,
[2242] inhibitor inter-neuron
because of the minus here, okay?
[2246] And then the synaptic weights
from that inter-neuron to the
[2251] principle neurons will be
WYZs, okay, which are also
[2255] this correlations between
YZ so it's He-- Hebbian.
[2259] And the threshold here has
to do with the summed past
[2265] activity B and parameter
alpha which sets the
[2270] threshold on similarity, okay?
[2272] So then whenever a new
stimulus arrives it
[2278] goes into this network.
[2281] Each neuron prod--
computes a summed a
[2284] produce computes a
weighted sum of the
[2287] feedforward inputs
and feedback from the
[2290] inhibitor inter-neurons,
thresholds it, which is neur--
[2293] what neurons love to do, right?
[2296] And then produces the output
which also goes into the
[2301] inter-neuron which does
very similar thing and that
[2305] whole activity iterates, okay?
[2307] [AUDIENCE MEMBER] What
is Z here?
[2308] [MISHA CHKLOVSKII] So Z is the
activity of this inter-neuron.
[2312] [AUDIENCE MEMBER] But
how do you compute it?
[2313] I mean--
[2313] [MISHA CHKLOVSKII] Oh, okay.
[2314] Sorry, I didn't write
it down but Z would be
[2321] just, so what you do,
you just take a derivative
[2328] of that with respect to Z
and you would get something
[2336] like ZT is ZT plus gamma
WYZY YT minus theta.
[2344] I think there is a threshold
which comes from the,
[2348] which comes from this term.
[2353] [AUDIENCE MEMBER] And
WZY comes from another?
[2355] [MISHA CHKLOVSKII] And
WZY is the same kind of
[2358] correlation that we had for YX.
[2364] [TALIS] So what determines
the number of clusters?
[2369] [MISHA CHKLOVSKII] Just the
architecture of the network.
[2372] How many neuron,
principle neurons
[2374] were assigned.
[2375] So it also turns out
that you don't really
[2377] have to be very accurate.
[2380] You can produce
an overabundance.
[2383] You can build a network with
an overabundant number of
[2387] neurons and then they will
get activated when needed, okay?
[2391] So you don't really have to
be very concerned about that.
[2394] There are all kinds of
regularizations that you can do
[2396] to have that done automatically.
[2398] [AUDIENCE MEMBER] Uh, s--
so you draw this, like,
[2400] Z's an inhibitory
population but are you
[2402] saying that WYZ and WXY are,
are all positive or negative?
[2407] Or like-- Right.
[2408] [MISHA CHKLOVSKII] So because Ys
and Zs have to be non-negative,
[2412] any correlation of Y and Z
would be positive, okay?
[2418] So then these vectors,
this synapses have positive
[2421] weights and the reverse synapses
which are just the transpose
[2424] of that matrix come in with
the minus in the dynamics,
[2428] so this will be all negative.
[2432] The feedforward ones depend
on what you assume about X.
[2437] If X is also non-negative,
then they're all non-negative.
[2442] So
[2442] [AUDIENCE MEMBER] If you're
concerned about local learning
[2445] and things such as this,
does it concern you that,
[2449] for example, you have the
transpose of the weights
[2452] being in some other place?
[2455] In other words, you have
[2458] [MISHA CHKLOVSKII] --right.
[2458] Yeah.
[2459] So that, no, that is not a major
concern because actually the
[2464] rule is still Hebbian so you
don't have to you, you don't
[2469] have to worry about it.
[2471] You just run it.
[2471] Yeah, you just run it
[2473] And it all comes out fine.
[2475] In reality,
they may not
[2476] be exactly the
same numerically
[2479] But yeah.
[2482] [AUDIENCE MEMBER] Okay?
[2484] [MISHA CHKLOVSKII] And of
course, okay, after the
[2487] activity dynamic settles
for each stimulus presentation,
[2491] you have to update the synaptic
weights because there is a new
[2497] term in this the covariance
has to be updated by
[2502] the additional term.
[2504] Okay?
[2505] And this learning rule was
of course local so, you know,
[2509] biologically plausible Hebbian
or a-- anti-Hebbian synapses.
[2517] So that's basically the main
idea of similarity alignment.
[2519] So if, for a certain family of
objective functions that are
[2523] rated in terms of similarity,
this trick works like a charm
[2528] and churns out various
biologically plausible Hebbian
[2532] and anti-Hebbian networks and
when you require non-negativity,
[2538] that also corresponds to
rectification in neurons.
[2542] Now I probably,
for this audience,
[2544] I don't have to defend
Hebbian synapses,
[2547] but let me just
show, you know,
[2548] one paper that very
clearly demonstrates
[2551] this is the case.
[2553] You know,
this is the correlation
[2554] between the activity of
two neurons in the cortex
[2556] and this is the synaptic
weight between them, okay?
[2559] So that's of course
as expected-- now the
[2563] next question, okay,
now that we built this
[2566] network does it really
do what we want it to do?
[2570] Does it really cluster?
[2571] So let's throw this
easily clusterable data
[2574] set on that network.
[2575] Of course, you have to realize
that the network has not
[2579] been pre-trained, okay?
[2581] So you start with some kind of
virgin network with, you know,
[2584] initialized randomly, whatever,
and you just keep throwing
[2586] those data points in at,
in an arbitrary order.
[2589] And it just clusters the
whole data set, okay?
[2593] [TALIS] So again,
the number of clusters
[2594] is determined by the
size of the layers?
[2596] [MISHA CHKLOVSKII] Yeah,
so here we just took the same.
[2598] But we do have regularizations
that automatically choose
[2600] the number of clusters.
[2601] [AUDIENCE MEMBER] Yeah.
[2602] [TALIS] It's
[2603] [AUDIENCE MEMBER] Not--
[2603] So if you choose --If you start
with more hidden units-- Yeah.
[2607] --in clusters,
the regularization
[2608] will set some to zero.
[2610] Well, suppose you start with
fewer-- Some zero there.
[2612] It will pick it.
[2615] [MISHA CHKLOVSKII] There
are both possibilities, yes.
[2618] Yeah, they start with
fewer than they will
[2620] merge certain clusters.
[2625] [TALIS] So the split
of the cluster, this
[2627] is the interesting part,
where a new cluster is born.
[2629] [MISHA CHKLOVSKII] That's right.
[2630] [TALIS] What happens then?
[2631] There's a first
solution in the layer.
[2638] [MISHA CHKLOVSKII] So,
because it's online,
[2640] the only thing that we
see is that, you know,
[2643] initially when you show
the first data point,
[2646] first neuron is activated.
[2648] Then when you show the second
one, if the second data point's
[2651] sufficiently close to the first,
then that first neuron
[2653] represents it.
[2654] If it's not sufficiently close,
then another neuron gets
[2657] activated and this
process gets repeated.
[2662] [AUDIENCE MEMBER] Is alpha
an external parameter?
[2664] [MISHA CHKLOVSKII] Yes.
[2664] Alpha has to be set.
[2667] [EWA] Yeah, I guess a related
question to that which is,
[2669] that what is setting the
scale of the clusters if
[2671] you have more cells than
[2672] [MISHA CHKLOVSKII] Clusters--
You would have --That's alpha.
[2674] In the data and it would be--
[2674] That's alpha.
[2675] [EWA] It's alpha, right?
[2676] Yeah,
[2676] Yeah.
[2677] So that's kind of
like a fixed scale?
[2677] [MISHA CHKLOVSKII] Yeah,
you have to set--
[2678] Okay, so if
[2679] [TALIS] You have clusters
in clusters, in some sort
[2680] of hierarchical data,
you're not going to find --
[2683] [MISHA CHKLOVSKII] Um,
not with this simple--
[2686] Not with this, not with this
simple network, that's true.
[2689] Do
[2691] [AUDIENCE MEMBER] You think
that it's absolutely necessary
[2693] for this to work, that there
is some feedback perhaps from
[2696] the next hierarchical stage?
[2699] A signal that will basically
tell you, "No, no, no, you
[2702] didn't cluster this correctly."
[2703] Yeah.
[2704] "you thought it is a cat,
but it's not a cat, it's a,
[2706] it's a panther."
[2707] Yeah.
[2707] And you know?
[2708] [MISHA CHKLOVSKII] Yeah.
[2710] And, in my opinion,
this is what feedback is for.
[2714] Oh.
[2714] Yeah, I don't think
I'm very original about
[2716] that, but yes, exactly.
[2718] [AUDIENCE MEMBER] And if
I may, one more question.
[2719] So as I synthesize,
I think about cortical
[2724] columns and whether this
circuit that you're describing
[2727] here is essentially what
happens in layer four,
[2730] like the inputs exist
there-- --the cortical
[2733] inputs exist there.
[2734] Have you thought about
this possibility, that
[2737] essentially clustering
happens in a cortical
[2739] column of layer four?
[2740] [MISHA CHKLOVSKII] Well it may,
but I have to warn you because
[2744] this is an oversimplified
cartoon of the cortical network.
[2749] In a minute,
I will show you what
[2750] we think is the most
reasonable biological
[2755] implementation of this,
which is the insect mushroom
[2758] body which I think is actually
suits this very well.
[2762] But I think cortex is a
little bit more complicated
[2765] so ready to go on a limb.
[2768] [MODERATOR] How
strictly is your output
[2770] orthogonalized after this?
[2773] I mean, the Y vectors.
[2775] [MISHA CHKLOVSKII] Y
vectors, how strictly?
[2777] So in this case,
this is hard clustering.
[2780] So only one neuron is non-zero
in response to-- Right.
[2784] --any stimulus.
[2785] [MODERATOR] So always giving
you this kind of So it's
[2787] [MISHA CHKLOVSKII] Always
orthogonal, okay?
[2790] [MODERATOR] So there is no
residual structure -- There
[2791] [MISHA CHKLOVSKII] Is
no structure.
[2793] Now, it is possible to
actually do soft clustering
[2798] with it, and it's very easy.
[2799] You just,
you add a L2
[2802] regularizer in Y to
the objective function,
[2804] and then you have multiple
neurons respond to each
[2808] stimulus, and then the
orthogonality is lost.
[2812] And that's what you can use
to represent a hierarchical
[2815] structures or manifolds.
[2816] We'll get to that
in the second part.
[2819] [AUDIENCE MEMBER] Two questions.
[2820] So in the original equations,
so in the early equations,
[2822] it appeared to me that the Y
vectors are sort of just chosen
[2827] appropriately for the X vectors.
[2829] And then this network structure,
someone suggested the Y vectors
[2832] are actually computed
from the X vectors.
[2835] Yeah.
[2835] So are the Y vectors
now just chosen, No, no.
[2839] [MISHA CHKLOVSKII] So
when I tried to motivate--
[2840] Or is there a computation
[2841] [AUDIENCE MEMBER] Going
on from When I tried
[2842] [MISHA CHKLOVSKII] To motivate
the objective function, I said,
[2844] "What Y do we want?"
[2845] Yes.
[2845] But the network has, of course,
to compute Y on the fly
[2848] for each stimulus.
[2849] [AUDIENCE MEMBER] Yeah, okay.
[2850] Second question, so this W, Y,
X that contains, in principle,
[2854] all the data that the
network had seen--
[2856] Yes.
[2856] So if you've been changing
statistics then you have
[2859] to Well, that's right.
[2860] [MISHA CHKLOVSKII] That's right.
[2861] This is a sufficient
statistics for this, right?
[2863] But if there's non-stationarity
then, you know--
[2866] [AUDIENCE MEMBER] If
you have --whatever.
[2868] [MISHA CHKLOVSKII] Right?
[2869] I mean, this is not online--
[2872] I mean,
because in
[2872] [AUDIENCE MEMBER] Clustering--
[2873] Yeah.
[2874] --clustering very often,
the clustering in the
[2875] beginning is somewhat
wrong and that gets corrected.
[2878] Yeah.
[2878] And if you don't get rid of the
first examples, you keep this
[2883] [MISHA CHKLOVSKII] So
[2884] Yeah,
[2884] So it's very easy to--
Irritating information.
[2885] Yeah, it's very easy to build
in forgetting into this.
[2888] Yeah.
[2888] So we have learning
rules with forgetting
[2890] And then they can track
the changing statistics.
[2893] So that's fine.
[2896] As long as your setting
is statistical rather
[2898] than adversarial,
this works just fine.
[2901] Mm-hmm.
[2901] And in practice,
it works all the time.
[2904] [AUDIENCE MEMBER] Does
this recurrent network
[2905] have to iterate over time
or let it converge or?
[2909] [MISHA CHKLOVSKII] Yes.
[2909] Yes.
[2910] So for each stimulus
presentation the network
[2913] has to iterate to compute Ys
[2916] And I realized that this feature
is somewhat unbiological,
[2920] so now we have derived networks
that do not have to iterate.
[2925] So that is actually possible,
at least for linear networks.
[2930] But I'm not talking about
this in, in the talk.
[2935] [AUDIENCE MEMBER] It feels
like maximum likelihood to me.
[2938] If you had sort of
exemplars that where
[2942] the distributions overlap,
then you're gonna cut 'em along
[2947] the equal probability boundary.
[2949] [MISHA CHKLOVSKII] Yep, yep.
[2949] You will.
[2950] In fact, the reason this
clusters is because it's
[2953] not that different from K
means, which in turn can
[2957] be thought of, what is it?
[2959] Gaussian model expectation
maximization, right?
[2962] So it is related
to what you said.
[2966] But let me just show so everyone
recognizes this as a K Mean
[2971] subjective function, okay?
[2973] But just by some algebra,
I can get rid of the Ws, right?
[2978] Because they're just centroids
of corresponding clusters,
[2981] and I can get this expression
where the constraint again is
[2985] this Lagrange multiplier term.
[2987] And instead of this,
I have this thing which,
[2991] look, this is the cross
term from the similarity
[2995] in Y to similarity in X.
[2998] The only difference from
what I was just telling you
[3000] before is this normalization
by the sum of Y, okay?
[3005] So, it is possible to
derive a K Means objective
[3008] function in terms of this,
in this similarity looking form,
[3013] and then you have a network with
biological learning rules that
[3019] actually performs clustering.
[3021] So, it's not really that
surprising that this does
[3024] as well as K means, okay?
[3028] [AUDIENCE MEMBER] But I th--
we seemed to took a right
[3031] angle turn from my
question which was--
[3033] Oh, then I didn't
[3034] [MISHA CHKLOVSKII] Understand.
[3035] [AUDIENCE MEMBER] --so that,
whether there's a big faction
[3037] of people that think Bayesian
representations are, are-- Yeah.
[3042] --the way the w-- brain works.
[3043] Yeah.
[3043] And so in that,
I'm, I'm, I'm s--
[3046] stumbling and to see
how these, the complete,
[3049] the overlapping distributions--
[3050] Yeah.
[3051] --get represented--
[3051] Right.
[3052] --in your clustering algorithm.
[3053] [MISHA CHKLOVSKII] Right.
[3054] So I don't have a slide on that.
[3056] But basically if you
do the following,
[3059] you just add to this
the term which is plus
[3062] trace of Y transposed Y
in the matrix notation.
[3066] Oh, okay.
[3066] Okay?
[3067] That kind of L2 regularization
on top of K means will turn
[3071] it into soft clustering.
[3073] [AUDIENCE MEMBER] Okay.
[3074] [MISHA CHKLOVSKII] And
then for each data point,
[3076] you can activate multiple
neurons to a different rate.
[3080] You can associate that or
interpret this as probabilities
[3084] of assigning that data point
to a particular cluster.
[3087] And that's actually
important, right?
[3088] So, that I think
makes a lot of sense.
[3091] I just didn't want
to talk about it.
[3093] Okay.
[3094] Yeah.
[3096] Okay?
[3097] So we can do soft K Means, and
because we could do clustering,
[3101] we looked for a biological
network that you actual,
[3104] you know network that could
implement something like this.
[3107] And what we found we
think is the best option
[3110] that could be modeled by
clustering is operation of
[3116] the mushroom body in an insect.
[3118] So just a brief review
of olfactory system.
[3122] So most of animals,
the way they smell is
[3126] that they have dedicated
neurons whose receptors are
[3131] tuned to particular compounds.
[3134] And so there are many of them,
like we have maybe 200 different
[3139] ones and the fly has 50 and
you know, mouse has 1,000.
[3144] So, so there's,
here I'm just
[3146] showing just two.
[3147] So there's a different
kind of dimensions of
[3150] the olfactory space.
[3151] And after the preliminary
processing in the insect,
[3155] it's called antennal lobe,
which would be olfactory
[3158] bulb in the mammal.
[3159] It's going to information is
transmitted to the part called
[3163] the mushroom body which has
several characteristic that
[3166] makes us think that our model
would work just great there.
[3171] There is a huge divergence
from say 50 channels to 5,000.
[3175] Um, there is only one
inhibitory interneuron
[3180] for the whole set of 5,000
mushroom body Kenyon cells.
[3187] This is surprising by itself,
but this is also has been
[3190] one of the problems with
the existing model of
[3192] processing there because
if you apply, for example,
[3194] sparse dictionary learning
here it's very hard to do it
[3198] with a single interneuron.
[3200] But for clustering, of course,
you want just a single
[3202] interneuron, because what
that interneuron does,
[3206] it just makes sure that the norm
of the assignment index vector
[3209] isn't, doesn't exceed one.
[3211] That's the only job,
the only constraint,
[3213] which is a scaler constraint,
that it has to implement
[3216] and that's why it's a
single interneuron.
[3218] So that's what we are proposing.
[3220] And of course we can explain
then a lot of features, right?
[3225] So it makes sense that
neurons are rectifiers, right?
[3230] Because the assignment indexes
are non-negative, right?
[3234] There's no sense of having
negative to belong to
[3240] some cluster with a
negative weight, right?
[3242] Even if you have probabilistic
assignment, okay, probabilities
[3246] are non-negative.
[3247] So actually that's why we
think neurons are rectifiers
[3252] in general because they
represent assignment indices
[3256] to different clusters.
[3258] As I mentioned,
we can account for
[3260] single giant interneurons.
[3262] You get sparse over complete
representation of course,
[3266] because you want to have
many different clusters
[3269] in the olfactory space
that correspond to
[3272] different stimuli.
[3274] Sparsity arises from
the competition, and
[3276] if you have competition
plus non-negativity,
[3279] a lot of the components
have to be zeros.
[3282] And of course,
this predicts
[3284] non-random connectivity
which went against initial
[3288] experimental measurements
in that system, but are now
[3291] confirmed by connectomics.
[3292] [AUDIENCE MEMBER] What happens
if that giant interneuron dies?
[3295] Seems very unstable.
[3298] [MISHA CHKLOVSKII] Yeah.
[3298] I think there is an experiment
where they ablated or shut
[3301] down that interneuron and
they showed that recognition
[3305] of odors became worse.
[3308] I, I don't remem--
I think this is uh, Mi--
[3311] Mis-- Mezenbaugh, maybe?
[3315] [AUDIENCE MEMBER] What
do you mean by odors?
[3317] [MISHA CHKLOVSKII] Orders?
[3318] [AUDIENCE MEMBER] Oh, odors.
[3319] Yeah, sorry.
[3320] I meant odors, yes.
[3320] Accent.
[3322] [MODERATOR] Is there
actually some so
[3323] What--
[3324] Is there evidence that
actually some clustering
[3326] goes on in this system?
[3328] I mean, there's these
other models where they're
[3329] actually just this kind
of, you know, they--
[3332] Yes.
[3332] They spread out--
[3333] Yeah.
[3334] --and alone.
[3335] Right.
[3335] I mean, is there really
an unsupervised
[3337] clustering going on?
[3337] [MISHA CHKLOVSKII] Yeah,
so the experiment that suggests
[3340] that it's more clustering
than compressive sensing--
[3344] Yeah.
[3345] --is the fact that
there are neurons,
[3347] there are Kenyon
cell neurons that
[3350] do not respond to
pure components
[3354] of the mixture,
but respond to
[3356] the mixture.
[3359] [AUDIENCE MEMBER] Right.
[3360] [MISHA CHKLOVSKII] That
wouldn't be the case in a
[3361] compressive sensing view.
[3363] So, and that has been
reported before by
[3366] Gilles Luran and others.
[3367] [MODERATOR] But they
also mix, right?
[3368] I
[3368] [MISHA CHKLOVSKII] Mean--
No, no.
[3369] But, but-- so what I'm saying
is that this neuron will
[3371] not respond to odor A,
will not respond to odor B,
[3375] but it will respond to A plus B.
[3377] And that looks to me
more like clustering than
[3379] like compressive sensing.
[3386] [AUDIENCE MEMBER] My question's
about the mushroom body.
[3388] Is that only interneuron
out there or are there
[3390] also local interneurons?
[3392] [MISHA CHKLOVSKII] This is
the only interneuron there.
[3395] [AUDIENCE MEMBER] What?
[3397] [MISHA CHKLOVSKII] It's
called giant interneuron.
[3398] [AUDIENCE MEMBER] All the
other are secondary cells?
[3401] [MISHA CHKLOVSKII] Yes.
[3403] So this circuit is
actually somewhat of
[3405] an oversimplification,
but this one, um-- Well,
[3409] this part of the circuit
is actually pretty accurate.
[3412] There's more complication going
on with the output when actions
[3415] are decided and so on, and,
you know learning takes place.
[3419] But the input is like that.
[3421] It is really true,
as confirmed by connectomics.
[3423] [AUDIENCE MEMBER] And be
careful when you think
[3424] about insects and,
and invertebrate
[3427] neurons because, you know,
you might have-- Like, a lot
[3430] of the neurons are monopolar
and there's a cell body.
[3432] Right.
[3433] But then there's this very
elaborate dendritic tree,
[3436] and it's not necessarily true
that this dendritic tree isn't,
[3439] necessarily in-- You know,
it could be like multiple
[3443] little inhibitory--
[3444] It's not iso-potential.
[3445] It's not
necessarily iso-potential.
[3445] Right.
[3446] So,
[3446] [MISHA CHKLOVSKII] This
is a very good point,
[3448] and that possibility has
been considered and there has
[3452] been a debate in the community
whether this interneuron
[3455] acts as one or there's a
localized computations.
[3458] The latest data that I've
heard about is that it has
[3462] been proven that it acts as one.
[3464] Hm.
[3465] Okay?
[3465] But that's an
experimental finding.
[3467] Of course,
I cannot claim
[3468] that theoretically.
[3469] Ewa?
[3470] So
[3470] [EWA] Back to the
question of scale and
[3472] the clustered geometries.
[3473] Yeah.
[3473] Is there reason to think
that different odorants and
[3476] odor mixtures have similar
size scaled clusters or
[3480] the clustered geometries
are the compact blobs,
[3483] or could they be manifolds or,
[3486] [MISHA CHKLOVSKII] They
are probably manifolds,
[3489] but that's why this
talk has part two,
[3491] although we don't have
that much time left.
[3495] Okay?
[3497] All right.
[3498] Okay.
[3498] So now that's all I had to
say about simple clustering.
[3505] Is there anyone who have
not seen the solution?
[3510] Okay, so you're supposed
to see young woman or old
[3514] woman even though the--
[3515] You know,
this is the
[3517] same image, right?
[3518] The same vector in the
pixel intensity space.
[3522] This, of course,
a visual illusion,
[3523] but it is here to emphasize
the point that two objects
[3528] that very similar in the pixel
space could actually belong to
[3531] completely different classes
and live in different manifolds
[3535] in this high dimensional space,
like animate and inanimate.
[3538] And, you know,
going back to this
[3540] illustration from
DeCarlo and Cox, right?
[3544] Then the way to view the visual
system is that layer after layer
[3551] of visual processing is trying
to disentangle these manifolds
[3555] without destroying their
internal structure so that
[3559] you can learn very easily
from very few examples by
[3563] linear classification.
[3565] And because you did not destroy
the structure of the manifolds,
[3567] you can generalize, right?
[3570] So that's one way to think
about object categorization
[3574] and visual processing, right?
[3576] And this is,
of course what
[3579] we really need
to do, right?
[3580] Clusters, you know,
belonging to animate and
[3583] inanimate in the pixel space,
they are not well segregated.
[3587] They're probably more like this.
[3588] Of course,
the manifolds
[3589] don't really intersect.
[3590] They look intersecting
here because the projection
[3593] onto low dimensional space.
[3594] Still, they're highly entangled,
you have to pull them apart.
[3598] Well, if you want to pull
apart those manifolds,
[3600] perhaps some kind of manifold
learning technique will work
[3603] which preserves neighborhood
relationships between nearby
[3606] points, but tries to pull
the manifolds apart.
[3610] And there are many respectable
methods in you know,
[3615] manifold learning that
work reasonably well.
[3619] But in my view,
all of them lack
[3622] biological plausibility.
[3624] And the biggest problem
here is that they--
[3626] It's very difficult to
formulate them in the
[3629] online setting because
most of these methods
[3631] work in the following way.
[3633] You take the whole dataset,
you compute the affinity
[3636] matrix between all the
stimuli into a graph,
[3640] and then you perform a
spectral analysis of that graph.
[3644] And so when the new point
comes about you have to
[3648] recompute the whole graph.
[3650] That doesn't work in
the online setting.
[3652] So what can we do?
[3655] Well, we thought, well,
since we built our network
[3659] to preserve neighborhood
relationships, maybe it can
[3662] do this manifold disentangling.
[3665] We took our network and
through this cartoon of
[3669] entangled manifolds, right?
[3671] So now there's two clusters.
[3673] They're of course not
labeled, it's unsupervised.
[3676] But they cannot be
linearly classified, right?
[3679] So what's going to happen?
[3683] Well, first of all nothing good
is going to happen if you use
[3685] this original objective function
that I showed you because this
[3689] describes similarity in terms
of just in a product.
[3693] And if you put an origin here,
then this points on the same
[3698] axis will be indistinguishable
even though they belong to
[3701] different manifolds because
they inner products just depend
[3704] on the angle between the points.
[3706] So you have to rewrite
it in terms of the
[3708] Euclidean distances.
[3710] May seem like a major problem
for neurally biologically
[3716] plausible networks, but
actually we know how to
[3719] build a neural networks
that process distances
[3723] not just similarities.
[3724] So that's not a big deal.
[3726] So we built a neural
network that optimizes
[3730] this objective and out come
this not very nice result
[3735] because what the network did,
they're just two neurons in the
[3740] output and they just tear up the
dataset depending on the value
[3746] of alpha you can, you know,
get more points assigned
[3750] to different clusters
but that's all they do.
[3754] They're not learning manifolds.
[3756] [AUDIENCE MEMBER] So,
we're invited to pretend we've
[3759] never heard of support vector
machines or anything like that.
[3763] [MISHA CHKLOVSKII] Well,
we want something to be
[3764] neurally plausible, right?
[3765] [TALIS] But,
everything is
[3767] linear here.
I mean
[3768] [MISHA CHKLOVSKII] --no.
[3769] There is a rectification.
[3770] Okay.
[3771] A rectifier.
[3771] [TALIS] Yeah.
[3772] But there's no,
high dimension. Well,
[3777] [MISHA CHKLOVSKII] So the high
dimension part is right on.
[3779] If we add more neurons, if you
don't just use two neurons for
[3784] two clusters, but we'd learn,
I think in this case we
[3787] have to use 40 neurons or
so, then miracle occurs.
[3791] So those neurons actually
learn receptive fields that
[3796] tile the two manifolds, okay?
[3801] And each neuron represents
only data points from one
[3806] or the other manifold.
[3809] So this network can in
fact learn manifolds, okay?
[3815] And because the neurons
are either representing
[3818] one manifold or the other,
in the next layer you could
[3823] just linearly classify it
with some supervision, okay?
[3827] Just to put this data
in the format a little
[3832] bit more familiar to
neuroscientists here is,
[3835] I just colored the data
points here by the neuron
[3840] that represents that data
point, that activates in
[3844] response to that data point.
[3846] I didn't have as many colors
as there are neurons, okay?
[3850] So you see the same
color repeating,
[3852] but that's just
an artifact, okay?
[3853] They do tile the manifold with
contiguous receptive fields.
[3858] Of course, if you show this to
neuroscientists you immediately
[3861] think of place cells, right?
[3865] [MODERATOR] And so if you,
if you turn your giant
[3867] interneuron a little
bit down so that you get
[3869] actually a distributed--
What happens then? Right.
[3873] [MISHA CHKLOVSKII] So
this doesn't have to be
[3876] hard clustering, okay?
[3877] So depending on that L2 norm
regularizer that I talked about,
[3881] you can change the degree of
sparsity and you can make
[3884] this clustering soft and you
can make receptive fields of
[3888] different neurons overlap.
[3890] In fact,
they do in
[3890] this realization.
[3891] You can see that
[3894] Oh, where is it?
[3895] Like, look here, okay?
[3897] They're clearly overlapping.
[3899] [TALIS] But you still don't get
the disconnected components.
[3901] [MISHA CHKLOVSKII] No.
[3902] You don't, okay?
[3904] But I will get to it in
a couple more slides.
[3907] Okay.
[3908] So what similarity alignment
seems to be able to do is
[3912] not just to cluster but
to learn manifolds, okay?
[3916] So then we went on a a
theoretical soul search in
[3920] trying to understand what's
going on and what helped me
[3923] a lot is knowing about the
paper that was published
[3928] by Cho and Soul in 2010
where what they suggested
[3933] is that neural networks can,
can be built to compute kernels,
[3941] local kernels just like
radial basis functions,
[3944] except that they showed
by just performing exact
[3950] mathematical calculation
that a single layer network and
[3955] okay, they use F instead of Y,
but it's a single layer network
[3958] like ours except that the number
of units is infinite, the number
[3962] of output units is infinite, and
the weights are randomly chosen
[3966] from a Gaussian distribution.
[3968] They're not learned.
[3969] They're randomly chosen from
a Gaussian distribution.
[3971] So this is like random
projections, okay?
[3974] And the neurons are
rectifiers with any of those
[3978] activation functions, okay?
[3979] Linear rectifiers
or other rectifiers.
[3982] So if you have a network
like this and you present
[3986] stimuli after stimuli,
the output the network
[3989] gives can be thought of
as a kernel computation,
[3993] meaning that the inner product
of the output activities for
[3999] two stimuli, T and T prime,
depends on the angle between
[4004] those input vectors T and
T prime once they've been
[4007] normalized theta, in this way.
[4011] So it's non-negative and it goes
to zero for orthogonal vectors.
[4016] Okay?
[4017] So you get a significant kernel
only if the two vectors are
[4021] close to each other.
[4023] So just like for Gauss
in RBF kernel-- except
[4027] they called it arc cosine
kernel because they exact,
[4029] they could compute this
integral exactly and show
[4032] that it's given by a closed
form arc cosine expression.
[4037] [AUDIENCE MEMBER] --yeah.
[4038] [MISHA CHKLOVSKII] Okay?
[4039] And different shapes of a kernel
are produced by different kinds
[4043] of nonlinearities.
[4045] [AUDIENCE MEMBER] Okay?
[4046] [MISHA CHKLOVSKII] So where
does this kernel come from?
[4048] Okay, it's very easy to
understand because to have
[4051] a non-zero inner product,
you have to have components
[4054] of F that is neuron, that
is active with response
[4058] to different stimuli.
[4059] Okay?
[4060] Which Ws respond to a
given stimuli because of
[4063] rectification to respond
to stimulus XT, this W has
[4068] to sit in this half circle.
[4071] Okay?
[4072] And to have a non-zero
activation in response to a
[4076] stimulus T prime this W has to
sit in the green half circle.
[4082] So the number of Ws that
respond is given by the
[4086] area of the intersection.
[4089] And that area, of course,
decays on the angle.
[4092] So, that's the basic idea of
how rectification leads to the
[4096] locality in the kernel sense.
[4100] Okay?
[4103] So what we did in this
context is we got rid of
[4109] the requirement that you
need infinite number of neurons
[4113] and randomly generated synaptic
weights by learning synaptic
[4117] weights through the data.
[4121] So our kernel is not
preset from the beginning.
[4124] The kernel is being learned
from the data as the data
[4128] arrives in the online way,
but the idea of what's
[4131] going on is, is ne--
exactly like Cho and
[4134] Sol described for
random projections.
[4136] Because we can learn from
the data, we don't need
[4139] infinitely many neurons.
[4141] We don't need to spend the
whole space, ambient space,
[4144] of stimuli with centroids.
[4147] We can only put the
centroids, the Ws,
[4150] only where the data lives.
[4152] So the centroids will span
the same manifold, the same
[4155] low-dimensional manifold,
on which the data lives.
[4158] That's why when Clay talked
about computing uh, im-- im--
[4163] embedding for Ws, they form a
low-dimensional space because
[4166] they live in the low-dimensional
manifold where data lives.
[4174] Okay all right.
[4176] So just one more
theoretical results.
[4178] Of course, you know,
words are good and I appeal
[4180] to this random projection uh,
r-- result of Cho and Sol,
[4184] but can we actually prove that
our network will really do that?
[4187] And in fact, we can.
[4189] We have to take
advantage of symmetry.
[4191] So for a dataset which uniformly
spans a circle, for example,
[4195] as a function of theta,
we can solve our optimization
[4199] function exactly and show that
the receptive fields are bump,
[4206] the bumps, the localized bumps
like you saw numerically.
[4209] This is possible because
you can write the problem
[4213] in as convex optimization
using compositive matrices.
[4216] I'm not going to go into that.
[4218] But some of you will
recognize the solution.
[4221] The solution is that
activation of each neuron for
[4225] the continuous representation is
simply a threshold cosine, okay?
[4230] So this would be the place
fields of individual neurons
[4236] indexed by their centroid phi.
[4239] And we can show that
these are exactly cosines.
[4243] Amazingly, this is the same
math as for the ring attractor.
[4249] It's exactly the same math,
but the interpretation is
[4252] completely different.
[4253] In the ring attractor,
there's individual neurons
[4257] that interact with each other.
[4261] Here, these are data points
that interact with each
[4265] other in the data space
through this computation.
[4269] Okay?
[4270] [TALIS] Well,
you do dot products,
[4271] so it's not really
surprising that
[4272] it'll be a cosine.
[4274] [MISHA CHKLOVSKII] Okay.
[4274] Uh, it took, it took some to,
it's actually uh, Anirban
[4279] Sengupto derived this.
[4280] So it took work.
[4282] But there is now an exact
solution that shows that
[4284] this is what our network does.
[4286] It does learn these
kernels, cosine kernels,
[4288] in a data dependent
way just as promised.
[4292] And just to throw
some eye candy,
[4295] we can learn not
just the place fields.
[4298] We can start with place
fields and based on
[4300] correlations for this
synthetically moving animal,
[4303] we can actually get grid cells.
[4305] Um, I mean,
that may not be
[4307] that surprising,
but we are doing
[4308] it with a network
just with Hebbian
[4311] learning rules.
[4312] [AUDIENCE MEMBER] Can you
elaborate a little bit more
[4313] why you get place cells?
[4320] Or grade cells?
[4320] Uh, I'm sorry.
[4321] [MISHA CHKLOVSKII] No.
[4322] So grade cells I cannot
say much more other think
[4326] about, you know, there was
no non-negativity constraint.
[4330] This would be simply PCA, like
linear multidimensional scaling.
[4335] So you would get
Fourier harmonics.
[4338] Once you get non-negativity,
you get something slightly
[4341] different, but you keep
the periodicity.
[4342] So that's all I can
say at the moment.
[4345] [TALIS] It's a clustering
of a uniform sphere.
[4347] [MISHA CHKLOVSKII] Yeah.
[4348] Yeah.
[4349] [TALIS] And you
don't have a choice
[4351] [MISHA CHKLOVSKII] Okay.
[4352] All right.
[4352] And of course, you know, we,
we passed the Holshausen
[4356] and Field test.
[4357] We can learn Gabor patches
from natural images.
[4361] But the big, of course,
the big prize is can we
[4364] really stack those layers
to get from here to there?
[4369] We don't know yet.
[4370] We think we can.
[4372] I want to show one
example where we have been
[4375] successful with stacking,
and that's an example of
[4378] this cartoon of entangled
manifolds using the spirals.
[4382] Again, the network is
completely unsupervised,
[4384] so it doesn't see the
red/blue color.
[4386] It just gets those data points.
[4388] And this is the similarity
matrix of the input.
[4390] Once you pass it
through the first layer,
[4392] it unfolds the manifolds, okay?
[4396] And it sees the two
separate manifolds.
[4399] If you keep stacking our network
on top, after the sixth layer,
[4403] the two clusters actually
get pulled apart.
[4408] [AUDIENCE MEMBER] Okay?
[4409] [MISHA CHKLOVSKII] Of course,
what you need to do for that is
[4411] you need to reduce the number of
neurons in the representation
[4415] as you go along, right?
[4416] You have to have this
funnel that leads to just
[4419] two clustered neurons.
[4420] Remember, when we tried to
apply a network with just two
[4423] neurons to the original data,
nothing good happened-- --okay?
[4428] But when we did it
gradually, layer after layer,
[4430] reducing the number of neurons,
then this clustering did happen.
[4435] Of course, we have to go to
such lengths only because
[4438] we require this to be
completely unsupervised.
[4440] If you allow just a little
bit of supervision, you could
[4443] cluster after the first layer
because there is already one
[4449] dimension along which red
and blue are separated.
[4452] It's just not in one
of the top eigenvalues,
[4455] so you wouldn't get it
from spectral clustering.
[4457] But if you knew if you had some
supervised input, you could.
[4462] Okay?
[4462] [TALIS] Spectral clustering
solves this spiral problem.
[4466] [MISHA CHKLOVSKII] It does
solve this, but you have to
[4468] first compute an affinity
graph with the Gaussian kernel.
[4471] Okay.
[4472] And I don't know how
to do this neurally.
[4475] Okay?
[4476] So this is our way,
this is our workaround
[4482] to do manifold learning
or kernel analysis in an
[4487] online biologically plausible
way with Hebbian networks.
[4494] Okay?
[4496] Initially, we thought of just
way to make things biological.
[4499] Now, I'm starting to think
that there is maybe something
[4501] fundamentally useful to that
kind of approach where you
[4505] compute the kernel
on the fly-- --and
[4507] The graph is being recomputed
in an online fashion rather
[4511] than doing it a priori as
is done conventionally.
[4514] But I would be happy
to talk about it.
[4516] [AUDIENCE MEMBER] Question.
[4516] [MISHA CHKLOVSKII] Yeah.
[4517] [AUDIENCE MEMBER] So this is
an empirical thing, right?
[4519] [MISHA CHKLOVSKII] Yeah.
[4519] [AUDIENCE MEMBER] Or it's
an empirical or is it--
[4522] Yeah.
[4522] --you just ran it and it--
[4523] [MISHA CHKLOVSKII] Yeah.
[4524] [AUDIENCE MEMBER] Oh, I see.
[4524] [MISHA CHKLOVSKII] Yeah.
[4525] [AUDIENCE MEMBER] But you,
you didn't show that this
[4526] actually will always,
you know, like theoretic--
[4531] I mean, what I'm saying is
instead of just running it,
[4534] why don't you show that it--
[4537] [MISHA CHKLOVSKII] I
think we could do that.
[4538] I mean, this result that,
you know, our first
[4542] theoretical result that
actually shows that we get
[4544] this kernel is relatively new.
[4547] Ah, okay.
[4548] So I think we should be
able perhaps to extend it
[4551] to that case, but yeah,
it's a good question.
[4555] [AUDIENCE MEMBER] So to
do something hard if you
[4559] take six layers to do
something that's easy,
[4562] do you think you'll have
to get very deep to do image
[4566] categorization or something?
[4567] Maybe not.
[4568] [MISHA CHKLOVSKII] No,
I don't think so.
[4570] I mean, in, in-- Well, okay,
I don't know what it takes to
[4574] do image categorization because
I don't think that the visual
[4578] system just repeats this one
operation that I just described,
[4582] which is similarity alignment.
[4584] I think there is
something else, right?
[4586] Because you have to
learn invariances--
[4589] Yeah.
[4589] --and stuff like that.
[4590] So there are other things
that need to be done which
[4593] we don't know how to do,
at least not in a biologically
[4595] plausible way, right?
[4597] So then I don't know how
many layers you need,
[4600] but I want to point out, I mean,
this may be a little bit of a
[4604] red herring because, you know,
the real computation is
[4607] kind of done here, okay?
[4608] The manifolds are learned here.
[4610] Right.
[4610] All the other layers are doing--
Have to be pretty versed in
[4614] that, to keep it that way, yeah.
[4615] Are pulling those manifolds
apart in a very inefficient way.
[4618] If you get just a little
bit of feedback, a little
[4621] bit of a supervised signal,
you could just do it in a
[4623] two-layer network very easily.
[4626] Okay?
[4626] Where you just, you know,
the first layer computes these
[4629] features and the second layer is
just a perceptron, you're done.
[4634] Okay?
[4635] But for completely unsupervised,
this is what you have to do.
[4637] So I'm not sure it's a
really very, very good
[4641] model of stacking in
the visual system.
[4644] But that's as far
as we got, so--
[4646] [TALIS] Oh, but again,
this dimension reduction
[4647] in the unsupervised case,
it's not clear that this
[4649] is what we actually need.
[4651] I mean, in this case,
it's really just the
[4654] geometrical disconnected
components, but I may want
[4657] something completely different.
[4658] [MISHA CHKLOVSKII] Exactly.
[4659] Exactly.
[4659] So,
[4660] [TALIS] And,
[4661] [MISHA CHKLOVSKII] Exactly.
[4661] So, so you would--
so if I'm talking about
[4664] a model of the brain,
I would stop here, right?
[4666] And then I would do
something else at this stage
[4669] and maybe then stack again.
[4673] [AUDIENCE MEMBER] So just
as a discussion point,
[4675] so Dan Yamins and Jen Carlo,
they train these big feedforward
[4678] networks with back prop and
then compare the internals
[4682] of those feedforward networks
to areas like before, right?
[4686] And can explain variance.
[4688] And so in conversation with
Dan he pointed out that if
[4693] the object recognition
portion of that task,
[4697] in order to make those
correspondences with data
[4699] is actually critical.
[4700] And if you do the same analysis,
but instead use a feedforward
[4706] network that was trained
as an autoencoder,
[4709] that the autoencoding
network does a significantly
[4712] worse job of explaining the
variation in neural data.
[4717] [MISHA CHKLOVSKII] Well,
but I don't find that
[4720] surprising, right?
[4721] Because, Okay,
so you have two
[4723] networks, right?
[4725] One does natural
object categorization,
[4728] the other one does artificial
object categorization.
[4731] But where do the categories
come for the artificial network?
[4735] These are the same categories
that we perceive that are
[4738] presumably represented in IT.
[4741] So then you have two
networks where both the
[4744] inputs are the same and
the targets are the same.
[4749] [AUDIENCE MEMBER] So I
brought it up because it
[4750] struck me that you were,
maybe I misunderstood--
[4752] Yeah.
[4752] --that you were motivating--
--a sort of stacked
[4755] unsupervised structure,
at least in some analogy to--
[4759] [MISHA CHKLOVSKII] No, no,
no, no, no, not at all.
[4761] That's what, why I was saying.
[4762] Th-- This is just a way to show
that we can do this clustering.
[4766] We can pull the manifolds apart.
[4768] But the biologically relevant
part, I think, ends here.
[4776] [AUDIENCE MEMBER] Okay.
[4778] In the title you said
that you would sort of
[4781] link structure, function,
and what was the third?
[4784] Models or something?
[4785] [MISHA CHKLOVSKII] Computation.
[4786] [AUDIENCE MEMBER] Computation.
[4787] So can you elaborate
a little bit on that?
[4789] Because, I mean,
so I was somehow, I mean,
[4791] when I went into this
talk, I was somehow--
[4793] Right.
[4793] --thinking, okay,
looking at you,
[4794] look at it for
connectomics and
[4797] models and, I mean,
also your introduction
[4799] sounded like that.
[4800] And now it's more like
a self-contained model.
[4802] So where's the linkage to--
[4803] Oh, okay.
[4804] [MISHA CHKLOVSKII] Yeah.
[4805] So, so so all these
predictions of, you know, Ws,
[4810] I don't know what, what's good.
[4812] You know, the predicted Ws
that they're, you know, this,
[4815] that we can compute the Ws by
actually analyzing this dataset.
[4820] That's something that
is, can be tested.
[4822] And, in fact,
we are testing
[4825] this in the olfactory
system where we have
[4828] the full connectome,
but the problem is that we
[4832] don't have the true natural
image dataset in olfaction.
[4837] Mm-hmm.
[4837] Right?
[4838] So we're trying to do it
with the data we have.
[4840] And we have some preliminary
indication of success,
[4844] but it was too premature to
actually talk about it, I felt.
[4851] But that's what we are doing.
[4853] [AUDIENCE MEMBER] So,
you always said that W
[4854] relates to a connectome?
[4856] [MISHA CHKLOVSKII] That's right.
[4856] So W can be measured
by connectomics,
[4859] but it can also be
predicted by measuring
[4862] activity in that circuit.
[4866] [AUDIENCE MEMBER] Okay?
[4867] [MISHA CHKLOVSKII] And
then activity can also be
[4869] predicted the same way from W.
[4870] So this theory allows you--
I don't know which --Ah, maybe
[4875] this slide would be the best.
[4878] Sorry for flashing
this so quickly.
[4882] Yeah.
[4883] So this is a computational
objective that ties you to
[4886] what you want to do, like
cluster and manifold learning.
[4889] The Ws are expressed in terms
of activities, so they can
[4895] be related to activities.
[4896] They can also be measured
through connectomics.
[4899] And of course, Ys and Xs
are activities of neurons
[4902] that can be measured by
large-scale neuronal
[4905] population recordings like with
calcium imaging, for example.
[4909] So this ties together.
[4911] That's what I--
Thanks for the
[4912] question, actually.
[4913] Yeah.
[4913] This ties together all
these three different
[4916] levels of analysis,
two experimental and
[4918] one theoretical.
[4919] [AUDIENCE MEMBER] So another
place to look would be the
[4922] inputs to the cerebellum,
the mossy fibers, they go to
[4925] this globarioli and then from
there to the parallel fibers,
[4928] and it's thought that there is
some kind of feature extraction.
[4931] Yep.
[4932] And, since this is feet
forward with inhibition
[4935] just like you get--
[4936] Yep.
[4937] In that structure you might
be able to have another-- Yep.
[4940] --place to, um--
[4941] Yeah.
[4942] --you know, look at it.
[4943] But the other thing is
how well does it scale in,
[4946] in terms of the numbers, right?
[4948] If give, giving it the
others it said that there's
[4953] 10 billion neurons in the brain.
[4955] Of course,
100 billion
[4956] are in the cerebellum.
[4957] [MISHA CHKLOVSKII] Right.
[4959] [AUDIENCE MEMBER] Right?
[4959] And most of those
are granule cells.
[4960] Right.
[4960] So it, can this scale up to
100 billion, do you think?
[4963] [MISHA CHKLOVSKII] Oh,
we don't know.
[4966] On a laptop,
we can run up
[4968] to, you know,
a few thousands
[4971] But I don't see
why not, all right?
[4973] I mean, the only thing that I
find a little bit problematic
[4979] for such scaling is this
iterative settling of activity.
[4984] So we are trying
to get rid of it.
[4986] Well--
[4986] But--
[4987] [AUDIENCE MEMBER] But
it's also, you're not
[4988] gonna have one inhibitory
neuron for the whole brain.
[4990] Yeah.
[4990] [MISHA CHKLOVSKII] Right.
[4991] So I, in this talk,
just for simplicity,
[4994] I only talked about the
similarity alignment with
[4996] the single inter-neuron,
but we also have other
[5000] mathematical expressions that
give multiple inter-neurons.
[5004] And those multiple inter-neurons
may be disconnected from each
[5007] other or may mutually inhibit
each other as also happens.
[5011] So actually,
that's my final slide,
[5015] [AUDIENCE MEMBER] I think.
[5016] So Misha, do you think you
can incorporate this balance
[5019] exhibition-inhibition into
your, your model?
[5022] Yeah.
[5024] [MISHA CHKLOVSKII] Ohp, sorry.
[5025] So, sorry.
[5025] Just to answer.
[5026] So these are different
biological features that
[5030] we can capture in this by
changing terms and writing
[5033] down a slightly different
computational objective.
[5037] So, you know,
the giant inter-neurons,
[5040] what I talked about today,
but we can also do it's not--
[5047] Yeah, so we can also do
multiple inter-neurons
[5051] with anti-Hebbian rules.
[5053] So it's all possible and yeah,
other kinds of inter-neurons
[5059] with other learning rules.
[5061] Um--
[5062] Okay.
[5062] --sorry.
[5063] So the question was?
[5064] [AUDIENCE MEMBER] About
balance exhibition-inhibition.
[5066] [MISHA CHKLOVSKII] I
mean, it is, it does
[5067] have to be all balanced.
[5068] I'm not sure it will pass the,
the exact definition of a
[5072] balanced network in the sense
of Sompolinsky and company,
[5077] but keep in mind that this is
not like a recurrent network
[5082] that we are working with here.
[5083] It's mostly a feed-forward
network where recurrency is
[5087] only a feedback inhibition.
[5091] So it's not really the
kind of network for
[5096] which balance excitation
inhibition was shown, right?
[5101] [AUDIENCE MEMBER] Yeah.
[5102] Yeah.
[5103] Uh Misha, the uh,
the comment about not
[5106] having to kernelize to relate
to manifold embedding schemes,
[5111] in, in your updating rule,
you have a W that appears
[5114] in both terms.
[5115] So, so you,
you update the
[5117] Ys and you update the
Ws and then, then those
[5120] Ws go back into the Ys.
[5122] So you get this W squared.
[5124] And in the manifold learning
world, there's a quadratic
[5129] form of that sort on distances.
[5132] And so, it may be the case
that your scheme is working
[5138] there because you're implicitly
forming that nonlinear aspect,
[5142] the relevant nonlinear aspect
of the kernel by the two
[5147] steps in your updating.
[5151] [MISHA CHKLOVSKII] We
have to think about this.
[5153] It's not immediately
obvious to me.
[5156] Maybe.
[5157] Maybe.
[5158] Okay.
[5159] So this is the most
important slide.
[5160] There's are people who were
involved in this work in
[5163] different, at different stages.
[5166] Thank you very much.
[5167] (applause)
[5171] I'm actually missing
Yang Shi Chen who is
[5174] also should be on that
slide and it's my oversight.
[5180] [AUDIENCE MEMBER] Can you
go back to the first time
[5182] you showed the spirals?
[5183] Okay.
[5185] [MISHA CHKLOVSKII] Go ahead.
[5191] First time.
[5192] Is this the first time?
[5194] [AUDIENCE MEMBER] Or yeah,
when you have like a bunch of
[5195] them, like all of the, Yeah.
[5198] Um, so I'm wondering, like,
what happens if you, like,
[5201] put a data point that's not
on one of the spirals or like
[5204] if you just, you know, sample
the whole two-dimensional space.
[5208] I mean, would you just have
like a tile with the neurons,
[5211] just tile this whole space?
[5212] [MISHA CHKLOVSKII] Yeah.
[5213] So, it depends where you put it.
[5214] If you introduce small amount of
noise, it will just work anyhow.
[5218] But if you put it
very far from it,
[5220] then you may get a
neuron that will represent
[5223] just that data point.
[5224] [AUDIENCE MEMBER] Or like
after it's learned, you know,
[5226] you train it with this--
[5227] Oh,
[5228] [MISHA CHKLOVSKII] After
it's learned?
[5228] Oh, then it's simple.
[5230] It's just the projection.
[5231] You will try the, to find
the nearest centroids and
[5237] you will distribute activity
among those centroids.
[5242] [AUDIENCE MEMBER] Right.
[5242] So like this For
a noisy solution.
[5244] So every neuron here is really--
In hard clustering, it's just
[5246] [MISHA CHKLOVSKII] For annoying,
in soft clustering it would be
[5248] just like maximum likelihood.
[5250] So,
[5250] [AUDIENCE MEMBER] There's this,
like a circle at every neuron?
[5253] Yeah.
[5257] A question about the
image coding example.
[5260] So how do you code
the image then?
[5262] Is it winner take all?
[5263] I mean, is it just one
unit that gets to respond
[5265] to the whole image patch or
do you somehow soften it so
[5268] that multiple units come?
[5269] Oh, we
[5269] [MISHA CHKLOVSKII] Just,
You mean when we learn
[5271] Gabor patches?
[5271] Yeah.
[5272] Oh, just like you did,
you know, just patches.
[5273] It's 12 by 12 patches.
[5275] Right, I know-- From the image.
[5276] But
[5276] [AUDIENCE MEMBER] Now
you have a population
[5277] of neurons coding that.
[5278] [MISHA CHKLOVSKII] Yeah.
[5279] [AUDIENCE MEMBER] Is
can only one neuron?
[5281] [MISHA CHKLOVSKII] No, no.
[5281] This was, okay.
[5283] Actually, to be honest,
this is soft clustering
[5286] but not just that.
[5288] It was a network which
we originally called
[5290] similarity matching which
had multiple interneurons.
[5294] So it's a--
[5295] Or, maybe even-- No,
maybe even direct connections.
[5298] [AUDIENCE MEMBER] I see.
[5299] [MISHA CHKLOVSKII] Yeah.
[5299] [AUDIENCE MEMBER] So that
leads me to another question.
[5300] Yeah.
[5301] There seems to be a strong,
at least qualitative similarity
[5303] between this learning
rule and FoldiX. Yes.
[5305] Which is like a mixture
of heavy and anti-heavy.
[5307] Yes.
[5307] What do you sort of--
[5308] How-- Is there some way to, uh--
[5310] [MISHA CHKLOVSKII] Oh, yeah. I--
[5311] Well, it's, it's the same.
[5313] So if you didn't have a
non-linearity, you know,
[5316] for the linear one you
could just uh-- We could,
[5322] can also derive a network
like this and the learning
[5325] rules are very close to FoldiX.
I think for feed-forward,
[5329] they're exactly the same because
those are just Oya's rules.
[5333] For the--
He didn't
[5334] have an interneuron,
he had lateral connections.
[5336] So for the lateral connections,
we get slightly different
[5339] learning rules.
[5340] Our normalization
term is different.
[5343] But remember that he did not
derive his learning rules.
[5346] From this class.
[5347] He just postulated them.
[5348] This was heuristic.
[5350] And so it's nice that it
worked, but, you know,
[5353] it's very hard to analyze
the nature of the solutions.
[5355] Ours are derived from
a principled objective,
[5359] so we can actually see
what the solution will be.
[5362] So that I think
is the advantage.
[5366] [AUDIENCE MEMBER] So this
in some ways resembles
[5369] the self-organizing map.
[5371] Yeah.
[5372] And with a lot more,
I think rigor and
[5376] theory behind it.
[5377] But I think the spirit
is similar though.
[5379] [MISHA CHKLOVSKII] Yeah, yeah,
[5380] Yeah.
[5380] I think I even,
[5381] [AUDIENCE MEMBER] You had
it on the first slide.
[5382] Yeah.
[5384] [MISHA CHKLOVSKII] Yeah.
[5384] I think it's a more
principled and biologically
[5390] plausible instantiation of
self-organization map.
[5398] [AUDIENCE MEMBER] So the
key thing that came out
[5400] was that your update rule
A has to be online and B
[5403] has to be rectified linear.
[5405] So that would just
automatically imply that
[5407] the objective function,
if this came out from just doing
[5410] gradient descent on the logic,
the function of the logic
[5414] function has to be quadratic
with some positivity constraint.
[5417] So if you recall,
so if you always
[5420] think that neurons
have to be attached
[5423] to an anti-neuralgia,
then that means the only
[5427] class of objective function
you can solve is this class.
[5431] [MISHA CHKLOVSKII] Right.
[5431] But it's a very big class.
[5432] We now have a huge
family of networks.
[5435] I mean,
even for
[5436] clustering, right?
[5437] I mean, we have this kind
of objective and we have--
[5444] [AUDIENCE MEMBER] So I
don't disagree that--
[5446] This kind
[5446] [MISHA CHKLOVSKII] Of
objective, right?
[5448] And this is just like
for clustering with a
[5450] single interneuron.
[5451] There are many,
many more that we have.
[5453] Sure.
[5453] Right.
[5454] So it's a rich class.
[5455] [AUDIENCE MEMBER] Sure,
it's rich, but you're
[5457] saying you don't think
that's a big constraint.
[5459] Say now if I want to
optimize some, you know,
[5462] E to the minus X or whatever,
then you know, probably--
[5468] So you're saying that
biologically it's not
[5470] necessary to consider
those sort of objects.
[5472] Okay.
[5472] [MISHA CHKLOVSKII] Okay.
[5473] So
[5475] probably not necessary,
but at this point in time,
[5480] these are the only ones for
which we can make a connection
[5483] from the objective to the online
algorithm, to the neural network
[5488] with local learning rules.
[5489] [AUDIENCE MEMBER] Okay.
[5490] [MISHA CHKLOVSKII] Once
you write down a log or
[5491] an exponential, which I,
I would love to write them
[5494] down, it becomes much trickier.
[5496] I'm not sure how to
do this at the moment.
[5500] So that's the reason, right?
[5502] So, you know,
that's why we
[5504] use Euclidean
divergence rather
[5506] than something else.
[5507] [AUDIENCE MEMBER] So you
mentioned this briefly
[5508] about your variances.
[5509] Let's take an MNIST
digit, like one.
[5512] If you shift it just a
little bit the similarity
[5515] is zero, right?
[5517] And so how would you
think about that?
[5518] So in the
[5519] [MISHA CHKLOVSKII] --right.
[5520] So you know,
it depends how
[5523] much data you have.
[5525] If the data is sufficiently
dense to, you know, trace out a
[5528] manifold in the pixel intensity
space then we will do just fine.
[5534] [AUDIENCE MEMBER] But
in your first layer
[5535] [MISHA CHKLOVSKII] We
[5536] [AUDIENCE MEMBER] Get
zero, Oh, I see.
[5538] There are different ones there.
[5539] [MISHA CHKLOVSKII] Well,
they're sufficiently closed ones
[5541] that whose overlap is non-zero
and the network will learn that.
[5545] Now whether this is biologically
plausible, well, you need
[5549] to invoke some other ideas
like temporal correlations,
[5553] slow feature analysis, or
[5558] whatever.
[5559] I don't know.
[5560] But certainly for very
high density of data,
[5563] we can learn those manifolds.
[5569] [MODERATOR] So okay,
so we will have a break.
[5571] After the break,
I think we will have a
[5573] discussion and it will
be the most energetic
[5575] discussion that we'll
have at the entire workshop
[5578] because it was just one talk.
[5580] We are, you know,
we are near 5 o'clock.
[5583] So please think a little bit
what are the points, also the
[5587] bigger picture points we want
to discuss and figure out.
[5591] You have heard now almost three
quarters of the talks and so I
[5595] think it's now time to really
think a little bit bigger
[5598] picture and then of course
dive into all the details
[5601] where we disagree and,
but so enjoy the coffee
[5604] and think a little bit
about discussion points too.
[5607] We have some
[5608] [AUDIENCE MEMBER] --yeah.
[5609] You know, the,
and so we have lots
[5611] of data now, right?
[5613] Every talk is a data
point in the space of
[5616] all possible theories.
[5617] Mm-hmm.
[5618] And the question is,
you know, how does that,
[5619] how do we relate that to
a theory for say the
[5622] cortex or the cerebellum.
[5625] It has been, you know,
the theory has been
[5629] very thin in biology
and in neuroscience on
[5633] the whole, right?
[5634] There, there's,
there are a few
[5635] that we have.
[5636] But it would be nice to try
to integrate across all of
[5641] the different approaches
that we've heard, you know.
[5646] Is it the case that there
is a theory emerging
[5648] or more than one?
[5650] For, from all of the,
all the data that's
[5652] coming in, that will
come in that we can t--
