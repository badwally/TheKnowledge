---
schema_version: 1
id: yt-1_xH2mUFpZw
type: youtube
title: The Platonic Representation Hypothesis
url: https://www.youtube.com/watch?v=1_xH2mUFpZw
authors:
- Simons Institute for the Theory of Computing
ingested_at: '2026-05-30T20:02:01Z'
content_hash: sha256:b877eabcb1e3599882bb467d225dc5b3c3a149e5b99e3b2ab96a9a192eecceba
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Simons Institute for the Theory of Computing
  channel_url: https://www.youtube.com/@SimonsInstitute
  duration_seconds: 2667
  caption_track: fetched
  snippet_count: 1102
filter:
  score: 0.85
---
[0] PHILLIP ISOLA: Thank
you, [? Sherry, ?] yes.
[3] OK, so, yeah, thanks for
letting me take the time,
[6] despite the fact that I'm,
I guess, inviting myself.
[9] But I get to share a
little bit of my work, too.
[13] So this is work that we
are publishing at ICML.
[18] It's a position paper,
so it's a little
[19] different than some of the
talks I would normally give.
[22] It's a little bit
more opinionated.
[23] But I hope that this is
a good audience for that,
[25] to get some interesting
feedback and discussion going.
[28] This is work with Jacob,
or Minyoung, and Tongzhou,
[32] who are two of my students.
[33] They're actually both here.
[34] Is Jacob here somewhere?
[36] Yeah, in the back,
and Tongzhou is here.
[37] And then additionally,
Brian Cheung
[39] was another author on this work.
[41] And this is "The Platonic
Representation Hypothesis."
[45] So it actually is
teed up perfectly
[47] from [? Shimon's ?] last
question last night,
[50] which is, why are we seeing
different methods converge
[54] on similar representations?
[55] Why is it that
somebody born blind
[57] can learn a similar
representation of the world
[59] to somebody that is seeing?
[61] And here is going to be some of
my thoughts on that question.
[64] But we didn't plan that.
[66] I didn't coordinate with
[? Shimon ?] on this.
[68] So one of my favorite papers
from the last 10 years
[71] is this one.
[72] This is some work
from [? Agita ?]
[74] and Antonio and others.
[76] And what they found is that
if you train a deep net
[79] to classify a scene,
then what happens
[83] is you get intermediate
neurons, labeled A and B,
[87] that if you evaluate them
on a bunch of other images,
[90] it looks like these neurons
are acting as object detectors.
[94] So object detectors emerge as
a intermediate representation
[98] for solving the
scene recognition
[100] problem, which makes sense.
[101] This is such a cool
paper because it's
[102] one of the first times that I
think we saw that these are not
[105] just black boxes.
[106] They actually have some kind of
interpretable structure inside.
[109] So what you're seeing
on the right here
[111] are that there is a neuron on
some layer of a scene detection
[115] network, a scene classification
network that will fire whenever
[118] it sees a dog face.
[119] So it's like to decide
if this is outdoors,
[120] I might be looking
for dog faces.
[122] There's another
neuron that fires
[124] whenever it sees a robin hood.
[125] And of course, Antonio showed
you more of this the other day.
[128] There's more recent
results like that.
[131] OK, so we found this
really interesting.
[134] And did some work
a little bit later
[136] with Alyosha and
Richard Zhang, in which
[139] we were solving a completely
different problem, which
[141] is image colorization.
[142] So take a black-and-white photo
and try to predict the colors.
[145] And you can ask
the same question.
[146] What are the internal
units sensitive to?
[148] What do the neurons react to?
[151] And you can think for yourself.
[153] A lot of you all have seen
work like this before.
[155] But it should be some
features about color,
[157] some low-level texture stuff,
but what it's going to be.
[160] What is this neuron A
going to be sensitive to?
[163] Dog faces.
[164] OK, you learn a
detector for dog faces,
[167] whether you train it to do scene
recognition or colorization, two
[170] very different problems.
[171] And you also get
flower detectors.
[173] So you get a lot of
different units that
[175] detect different types of
things that we might-- might
[177] be nameable, might be semantic.
[180] So this is a story that it's--
[182] you've seen it before.
[183] I think many of you have.
[184] This is textbook
knowledge by now.
[186] These are figures
from our textbook.
[187] So I can-- I get to define,
what is textbook knowledge?
[190] OK, they really are.
[193] You can look at
page 300 something.
[196] But it's led me--
[198] and I think many people
have had similar--
[200] have stated similar hypotheses.
[201] But it's led me to
this basic hypothesis,
[204] that different
neural networks that
[207] are trained in very
different ways,
[208] with very different
architectures
[210] seem to be converging
to a similar or--
[213] the strong version
of the hypothesis
[214] is they're converging to
the same way of representing
[217] the world.
[219] Maybe that's a
hypothetical endpoint.
[221] It'll be the same, and
they're not quite there yet.
[225] So let's unpack
this a little bit.
[226] Oh, OK, so let's unpack
this a little bit.
[228] But I know what you're thinking.
[230] I know at least one
of you is thinking.
[231] Where's-- Alyosha is here?
[232] OK, maybe not.
[233] Well, I can use my
model of Alyosha.
[236] I know what he's thinking.
[237] Yeah, of course, they
converge to the same thing
[239] because it's all about the data.
[240] That scene recognition system
was trained on ImageNet.
[244] And-- that's actually not true.
[246] It was trained on a
different data set.
[247] But it's trained on a data set
with a lot of photos of dogs.
[249] And the colorization network
was trained on ImageNet, which
[251] is a lot of photos of dogs.
[253] Of course, they both
learned similar detectors.
[255] And that's not what
I'm going to say.
[257] That's not what
I'm going to argue.
[260] So it could be that there's
something else common
[262] between these different systems.
[263] It could be the architecture.
[265] Dan talked a little bit
about this a few days ago.
[268] It could be that it is
the optimization process.
[270] Andrew was talking about
some optimization properties
[273] that might lead to convergence.
[275] It could be the people.
[276] Maybe-- we're all talking.
[277] We're all sharing ideas.
[278] We're all going to
converge sociologically
[280] to the same types of ways
of representing the world.
[284] But what I'm going to
argue, essentially,
[288] is that it's none of these.
[290] So what's left?
[291] What is common between
all these systems?
[293] It's the world.
[294] These systems are all trained
on this same universe,
[297] this same reality,
this same Earth.
[298] And it's kind of similar
to it's all about the data.
[302] But it's that the data is an
intermediary to the world.
[304] And you could have data that's
superficially very different.
[307] But if it's still data that
samples from a similar world,
[311] then it will lead to
similar representations.
[313] So that's going to be
the rough argument.
[315] OK, so outline of
the talk will be,
[319] first, I will
share some evidence
[321] of convergence between
different models trained
[324] in different ways.
[325] Then I will talk a
little bit about what
[328] we might be converging to.
[330] Is there an endpoint to this?
[332] And finally, I'll talk about
limitations and implications
[335] of this idea.
[337] And again, there's a lot
of interesting implications
[340] and a lot of really
important limitations.
[342] So I hope that sparks debate.
[345] OK, so evidence of convergence.
[348] OK, I already showed you
that scene classifiers
[351] and colorization networks
learn some similar units.
[354] There's a lot more
papers along those lines.
[357] Maybe the first and
most famous examples
[359] are results like this
from Hubel and Wiesel
[362] found that there are Gabor-like
or oriented line detectors
[365] inside the cat cortex.
[367] And Bruno and others
have shown that there
[370] are simple statistical models
that also result in these Gabor
[374] filters being the natural way
of processing visual data.
[379] And of course, we also have
seen that in neural networks,
[382] the first layer, you always
get these edge detectors,
[385] these Gabor-like filters.
[386] These are the filters on
the first layer of AlexNet.
[388] So that's some kind
of commonality.
[391] These-- different systems,
brains, cats, and so forth,
[394] are converging to similar
first-layer representation.
[396] And over the years,
people have built that up
[398] and looked at second
layer and third layer
[400] and seen commonalities.
[402] Now, I'll jump forward to a very
recent version of that idea,
[405] which is work from Amil.
[407] Amil here?
[408] OK, Amil is over there--
[410] Amil and Alyosha on what
they called Rosetta neurons.
[413] And this is super cool.
[415] This is showing in each column
a different neural network,
[418] a different vision network
or graphics network.
[421] And the networks are processing
this image of the cat.
[424] And in each row,
they find-- they're
[427] highlighting a neuron,
which seems to be shared
[431] between all of these networks.
[432] So in StyleGAN,
there exists a neuron
[435] that fires for the Santa hat.
[438] And in ResNet50, there also
exists a neuron that selectively
[441] fires for the Santa hat.
[443] So it's a filter.
[444] So that's why we're
seeing a heat map.
[446] And that heat map is
high for the same region.
[450] And these networks are
not trained together.
[451] These were entirely
different neural networks
[453] trained on different data.
[454] So they called them
Rosetta neurons
[455] because it's like a common
language that's discovered
[458] across these different models.
[460] And they were a little more
conservative than we are.
[463] So they said they
found 20 or so,
[465] and it doesn't explain
all the variants.
[467] But I want to say that
this is like the start
[469] of some kind of convergence,
which may go further.
[474] So there's a lot more
evidence along these lines.
[479] But I want to get to
some of our new results
[482] and new experiments, where we
looked at this in a little bit
[484] more detail.
[485] So we have some
level of similarity
[488] between different
neural networks,
[490] different architectures,
different data sets.
[492] And I think that's something
that many people in the field
[495] have remarked on
over the last decade.
[496] But for this to be
actually converging
[499] to some optimal or
platonic representation,
[503] we've got to show that
the level of similarity
[505] is increasing over time or
increasing over performance
[509] or scale in some sense.
[511] So that's going to
be the next question.
[513] Is this increasing?
[514] And if so, that
suggests that there
[517] is a convergent trend going on.
[523] So I want to now set up
a little bit of notation
[528] to formalize what I
mean by representation
[531] and what I mean by
representational alignment
[533] and convergence to get
us on the same page.
[536] So I'm not saying
that all models
[538] are converging in all senses.
[539] I'm actually meaning it in
a fairly particular sense.
[542] So what I mean is we're going
to restrict our attention
[545] to representations that
are vector embeddings,
[548] so mappings from some data
like images to a vector.
[553] It's not everything, but
this is a very general class
[555] of representations.
[557] And we're going to characterize
a representation only
[561] in terms of its kernel.
[564] So this is actually
a very common way
[566] of characterizing
a representation.
[568] This tells me, how does the
representation measure distance
[572] between different data points?
[574] So the kernel of a
vision system evaluated
[579] over this set of images
will look like a matrix.
[582] It will be saying,
my representation
[584] of this person's face is
similar to my representation
[586] of that person's face
and very different
[588] from my representation
of this house.
[591] So the kernel is
an inner product
[593] between the embeddings between
one image and another image
[597] or one data point and another
data point, evaluated over all
[601] the pairs of data points.
[603] So kernels are really
important in understanding
[609] representations.
[610] Kernel methods, kernel machines
make use of this structure
[614] for learning.
[615] In neuroscience, there's
a lot of literature
[617] on representational
dissimilarity matrices.
[619] That's a kernel.
[620] This is from a
neuroscience paper.
[622] So kernels are a
fundamental structure
[625] for understanding the
properties of a representation.
[627] And that's all we're
going to talk about today.
[632] So in order to know if
two representations are
[635] the same in the way
that they represent
[636] distance, or they-- the same
in their kernel structure,
[639] we need a kernel
alignment metric.
[641] And that just means I'm going
to take the kernel for one
[644] representation and look at the
distance between that kernel
[648] and the kernel for
another representation.
[649] And that's my measure of how
similar the two representations
[652] are.
[653] There's a lot of kernel
alignment metrics.
[655] I'm not going to go into
the details of them.
[658] But just think of it as you
create this kernel matrix
[660] from one neural net.
[662] You create it for
another neural net,
[663] evaluate it on the
same data points,
[664] and you somehow
measure the distance.
[670] So let's do an experiment now.
[672] We're first going to look at
if different vision models,
[676] different vision neural networks
are increasing in their kernel
[679] alignment over time, or in
particular, over performance.
[682] As they get better,
which also as the years
[685] pass they get better, are
they becoming more similar
[688] in terms of their kernels,
how they represent the world
[690] in their internal activations?
[693] So two hypotheses
we can put out here.
[696] So one is that, no, they're not.
[698] There are many different
ways that you can represent
[700] the world that are all good.
[702] There's not just one way of
solving the problem of vision.
[705] That's one hypothesis.
[707] And two is, actually,
too bad, no.
[710] All strong models are like.
[711] This is the Anna
Karenina setting.
[714] That's a term that was
coined by Bansal, et al.,
[717] so it's not our own term.
[718] But I really like it.
[719] It's the idea that
it could be the case
[722] that all strong representations
are somehow alike.
[725] They have something in
common because it's all
[727] happy families are alike.
[729] It's the same idea
that there's a lot
[730] of ways you could go wrong.
[731] But if you are right
in all properties,
[733] then that's a set of constraints
that forces you to be alike.
[736] Dan Yamins and I
think Rosa have called
[739] this the contravariance
principle.
[741] So it's also quite
related to that.
[742] There's a lot of people in the
audience that have studied this.
[745] So it's just great to be here.
[746] So let's run our own
experiment on that.
[750] We're going to take
78 vision models.
[751] What I want to emphasize here
is that these models are all
[754] trained in different ways.
[756] So some are ResNets.
[757] Some are transformers.
[758] Some are trained on ImageNet.
[760] Some are
self-supervised systems.
[761] Some are trained
on other data sets.
[763] So different training
data, different objectives,
[765] different architectures.
[767] And I'm going to bucket
these different vision
[771] systems, these different
visual representations
[774] by their performance
on this benchmark
[777] of general visual competence.
[778] This is the VTAB benchmark.
[780] So this is our
proxy for, are you
[782] just a good general-purpose
visual representation?
[785] And so this is used as--
[788] to evaluate if I
have learned good
[789] features in computer vision.
[792] So on the x-axis is going to be
different bins of performance.
[796] So the first bin will be
visual representations that
[800] don't solve many VTAB tasks.
[802] And the last bin will be
visual representations that
[805] do solve a lot of VTAB tasks.
[807] And the y-axis is
going to be the kernel
[811] alignment, the average kernel
alignment between items
[814] in each bin.
[816] So here's the result.
So systems that
[820] are really good at a
lot of different tasks
[823] are all quite similar.
[824] And systems that are only good
at one task or not very good
[827] at all are all quite dissimilar.
[831] So it kind of makes sense.
[832] You might be thinking,
yeah, of course.
[834] If a system-- if two systems are
good at the same set of things,
[837] then of course, they must have
similar internal structures,
[839] similar representations.
[840] I don't think it
has to be the case,
[842] but it's reasonable
to suppose that.
[844] You can construct worlds in
which that wouldn't be true.
[846] But it's not too surprising.
[848] And it's the Anna
Karenina scenario.
[850] All strong representations in
these experiments are alike.
[853] So here's a t-SNE
plot or a UMAP.
[855] It's similar to a UMAP plot
of that result. Again, here
[858] are different vision networks.
[860] And notice that regardless
of whether you're contrastive
[862] or your CLIP or
your classification,
[864] different architectures,
different objectives, the--
[867] what's causing two
representations to be similar
[871] is their performance,
not their architecture.
[873] It could have been that all
of the contrastive methods
[876] cluster together
separately from all
[878] of the non-contrastive methods.
[880] But that wasn't the case.
[881] Performance is what is
dominating the clustering
[885] of these representations.
[890] So I think that a lot of people
would have expected that.
[894] As vision systems become more
general purpose, stronger
[897] at more tasks, they
become more aligned in how
[900] they represent the world.
[902] The next experiment
is going to be--
[903] well, to me, it was a
little more surprising.
[905] So now we're going to
ask, is the same happening
[908] between two modalities?
[909] So as language models
get bigger and better,
[912] do they become more and
more alike to vision models?
[916] This is a little
bit weird, right?
[919] So a few hypotheses.
[920] Hypothesis one is that, no.
[923] If you do better and better
at next-token prediction,
[925] next-word prediction,
you're going
[926] to become really good
at language, at syntax,
[928] at low-level, superficial
properties of language.
[932] And you're going to probably not
be something that's generally
[934] useful for other domains.
[936] It's just you're going to be a
super specialist on language.
[940] Hypothesis two, maybe not.
[943] Better language
models are just better
[945] intelligent representations
of the world.
[947] And they're also
better vision models.
[949] I'll tell you exactly
what-- how we measure that.
[952] And maybe the strong
form of hypothesis two
[954] is, the best vision model
is the best language model.
[957] This is going to be too strong.
[959] But we'll put that
there for, yeah, maybe.
[964] OK, so I have to tell you how
we can measure whether or not
[967] a vision model represents
the world in a similar way
[970] to a language model.
[971] Again, we're going to
use kernel alignment.
[973] But it's cross-modal
kernel alignment.
[976] So here are some images.
[979] And this box is
representation space.
[982] And I'm imagining
a neural network
[984] in which the apple and orange,
according to the vision system,
[987] have a similar representation.
[989] They're nearby in
representation space.
[991] And the apple and the
elephant are far apart.
[994] And we can also embed
the corresponding words
[998] for those items into
representation space
[1002] of a language model.
[1003] And what we're asking is whether
the similarity in the language
[1008] representation
matches the similarity
[1011] in the visual representation
for the corresponding image that
[1014] matches that text.
[1017] So if the representations
are converging,
[1019] we'd say that the similarity
according to a language model
[1022] of the word "apple" and
"orange" is roughly the same
[1025] as the similarity according
to a vision model of an image
[1028] of the apple and an
image of the orange.
[1033] So we have to have paired
data to evaluate this.
[1036] The models in this section are
all trained without paired data.
[1040] So they are vision models
trained only on images.
[1043] And we're going to measure their
similarity in representation
[1045] space to language models
trained only on language.
[1048] But we're going to evaluate
the kernel alignment using
[1051] paired data to be able to
ask, does the vision system
[1054] embed these two
photos of Yosemite
[1056] close to each other
in a way that-- and
[1059] does the language model also
embed these two sentences that
[1062] are captions about Yosemite
close to each other?
[1068] So here's the main result.
Here's the experiment.
[1072] We took 11 language models,
5 vision models, these vision
[1075] transformers.
[1076] We measure on the
x-axis the performance
[1079] of the language model
at language modeling,
[1082] so the performance
of the language
[1083] model at next-word prediction.
[1086] And we measure on the
y-axis the kernel alignment
[1089] between the language
model at each
[1093] of these points
and a vision model,
[1096] DINOv2, which is trained
self-supervised only on images,
[1100] no language used at all.
[1102] OK, so here's the result. So as
a language model, like Llama,
[1108] for example, up here
becomes better and better
[1112] at next-word prediction, its
kernel becomes more and more
[1116] alike to the DINO kernel.
[1119] And as DINO-- the
different colors
[1121] are different sizes of DINO.
[1123] So the biggest DINO model is the
most aligned with the language
[1126] models.
[1127] It goes both ways.
[1128] Bigger, better vision models
have more and more similar
[1131] kernels to bigger,
better language models.
[1137] So we have some metric
I didn't describe fully.
[1142] We only got up to
0.6 on that metric.
[1144] But the point is the trend.
[1145] The trend is going up.
[1146] It might [INAUDIBLE] off.
[1147] We'll see what happens.
[1148] We did this for a bunch
of different language
[1150] models, a bunch of
different vision models.
[1152] One thing I want to point out
is, OK, I actually lied to you.
[1155] I said that we were only looking
at pure language and pure vision
[1157] models.
[1158] We did look at one
VLM, one model clip
[1161] that's trained to
align images and text.
[1165] And you would expect
that a model trained
[1167] to align images and text will
end up with a similar kernel
[1169] because it's trained to have the
same kernel between the vision
[1172] encoder and the text encoder.
[1174] But CLIP is not actually--
it's only marginally more
[1178] aligned with Llama,
with a language model,
[1182] with language models in
general, than DINO is
[1185] aligned with language models.
[1187] So DINO has almost
the same alignment,
[1188] in this kernel-alignment
sense, with language models
[1191] as CLIP does,
despite that CLIP is
[1193] trained to be aligned with
language models, which
[1196] is interesting.
[1197] Was there a question or no?
[1199] AUDIENCE: [INAUDIBLE]
[1199] PHILLIP ISOLA: Yes, Bill.
[1201] AUDIENCE: Do you think this
would work for audition?
[1202] PHILLIP ISOLA: Yes.
[1203] [INAUDIBLE]
[1203] AUDIENCE: [INAUDIBLE] sound the
way as an apple sound the same?
[1206] PHILLIP ISOLA: Yes, maybe.
[1207] The hypothesis is that,
yes, it will work.
[1209] Me personally, I don't know.
[1210] But the hypothesis doesn't
represent my exact belief.
[1213] It's like we're
stating a hypothesis.
[1215] But, yes, the
hypothesis is it will.
[1217] And I'd love to hear Josh's
thoughts on that at some point.
[1219] Yeah, Dan.
[1220] AUDIENCE: [INAUDIBLE]
brief clarification.
[1221] The reason you're saying that
CLIP is only marginally better
[1223] is because it's at
0.2 versus the thing
[1225] from the previous slide?
[1226] Does that have [INAUDIBLE]?
[1228] PHILLIP ISOLA: Well, 0.6.
[1228] Yeah, that was the point, yeah?
[1230] AUDIENCE: OK.
[1231] PHILLIP ISOLA: Numbers
are still kind of low.
[1232] So who knows what will
happen as they go up to 1.
[1234] Blake.
[1235] AUDIENCE: But to push on
that a bit-- and I guess
[1237] this gets to what you
were saying, though.
[1239] Given what you said about weaker
models or more specialized
[1242] models, if you weren't training
on this very general next-token
[1246] prediction thing, but say you're
doing something really specific,
[1249] like you trained your language
model just to always highlight
[1251] the word "dog" for me, I
imagine this wouldn't hold.
[1254] PHILLIP ISOLA: I
think you're right.
[1256] AUDIENCE: [INAUDIBLE]
highlighting "dog"
[1257] would not correlate with
its match to visual models.
[1260] PHILLIP ISOLA: Yeah,
I think you're right.
[1262] I'm not going to talk
about that explanation.
[1264] That is something we
talk about in the paper.
[1266] We call it the
multitask hypothesis.
[1268] Train on more tasks,
get more convergence.
[1269] But it's also basically the same
as the contravariance principle.
[1273] So Dan and Rosa have already
articulated that idea.
[1276] But I think it's--
[1277] I think that's important.
[1279] OK, but let me go on.
[1282] We have a few reasons why we
think this might be happening.
[1284] I'm happy to discuss
more offline.
[1286] I want to talk about where
all of this might be heading.
[1290] And this is the most hypothesisy
part of this hypothesis,
[1294] I suppose, is this
is not proven.
[1297] But the picture that I have
in mind, that we have in mind
[1300] is something like Plato's cave.
[1302] So I think most of
you probably know
[1304] the allegory of
the cave, this idea
[1306] that there's prisoners
in the cave whose
[1308] only experience of
the outside world
[1309] is the shadows on the cave wall.
[1311] But they somehow infer that
there is a world out there.
[1314] And Plato made
that as an allegory
[1316] about our own experience.
[1318] We only experience data.
[1319] We don't actually have any
access to true physical state.
[1321] And he says, maybe
metaphysically, there isn't even
[1324] a true state.
[1325] There's just ideal
latent variables,
[1327] ideal forms behind it all.
[1329] I'm not going to make any
kind of metaphysical argument.
[1331] It's just an analogy.
[1333] But the picture
that we have in mind
[1335] is that, yeah, there
is a world out there.
[1336] There is some data-generating
process, some causal variable z.
[1339] And you can observe that
world in different ways,
[1344] multi-view learning.
[1345] You can look at
it through images.
[1346] You can caption the images.
[1348] You can potentially get
to that same sentence
[1351] via a different set
of sensors, maybe
[1353] via touch or a different
camera from a different angle.
[1357] So there's a lot of different
ways of viewing the world.
[1359] But if I learn a
representation of any
[1361] of these ways of
viewing the world,
[1363] well, because they're generated
by the same causal process
[1365] by the same world
behind it all, they
[1367] should somehow become alike.
[1369] That's the basic idea
for what we have,
[1372] for why we think ultimately
there is this convergence.
[1375] It's a very general
idea, an idea
[1378] that's been stated many
times in various ways.
[1380] But I think it's still a
powerful idea to investigate.
[1383] OK, so I want to--
[1385] so that's the general idea.
[1386] Now, I want to tell you
about one particular toy
[1389] mathematical model
in which you will
[1391] expect to get this
type of convergence.
[1393] But I'm going to
emphasize, this is just
[1395] one particular mathematical
formalization of this idea.
[1399] I think the idea could be
explored much more broadly.
[1402] So the mathematical
model that we
[1406] have that would exhibit
this type of convergence
[1410] between an image embedding
and a language embedding
[1412] goes as follows.
[1414] You have a world that
consists of discrete events
[1417] Z. They're sampled from some
unknown distribution P of Z.
[1423] All observations,
all learning signal
[1425] is mediated via observation
functions, which
[1428] we are going to assume
are bijective functions.
[1430] That's a huge simplification.
[1433] So they contain
all the information
[1435] in the observation
function that is contained
[1438] in the latent variable Z.
[1441] And in this world, we're
going to model co-occurrences.
[1445] We're going to use a
contrastive learning method that
[1448] will basically say, two
things that co-occur
[1452] are a positive pair.
[1454] Two things that don't
co-occur are a negative pair.
[1456] Align the positives.
[1458] Align two things that
are co-occurring.
[1459] Push apart two things
that are not co-occurring.
[1461] And this is the standard setup
for contrastive learning.
[1464] So this is not far
off from the types
[1466] of learners that are popular.
[1467] Like contrastive
language models might
[1471] try to align two
co-occurring words.
[1473] And contrastive
image models might
[1474] try to align two
co-occurring image patches.
[1479] So in that particular world,
with discrete random variables
[1482] and bijective
observation functions,
[1485] if you train a contrastive
learner with a noise contrastive
[1488] estimation objective,
you can prove--
[1491] and this is not a new result,
but you can show that the--
[1495] this will converge to the
pointwise mutual information
[1497] function.
[1499] So the intuition for that is
that what contrastive learners
[1502] are trying to do
is they're trying
[1503] to classify between
positives, co-occurring items,
[1507] and negatives,
non-co-occurring items,
[1509] and trying to learn an
embedding of the data in which
[1511] the inner product, or the
similarity between the embedding
[1514] vectors, is proportional
to that probability ratio.
[1518] And that probability ratio
is just how much more
[1522] often do the two items
co-occur together divided
[1524] by the product of the marginals.
[1527] How often would you expect,
by chance, them to co-occur?
[1530] And so basically, if
I learn an embedding
[1535] f, such that its inner
product with other items
[1537] is equal to this ratio, then the
kernel that it will arrive at,
[1541] the way that this representation
measures similarity
[1544] is going to be this
pointwise mutual information
[1547] function, the joint
probability divided
[1549] by the chance rate of
those things co-occurring.
[1552] This PMI function has
been a favorite of mine
[1554] for a long time.
[1555] So I'm just-- I'm always
trying to sneak it in.
[1557] But the rough picture is that
contrastive learning boils down
[1561] to finding an embedding
in which similarity equals
[1564] co-occurrence rate or pointwise
mutual information, which
[1567] is like normalized
co-occurrence rate.
[1569] So this is a little
bit-- maybe if you
[1571] don't like the Plato analogy,
this is the Wittgenstein.
[1574] And meaning is used--
meaning derives
[1578] from the rate of co-occurrence.
[1579] And so the reason why
the apple and the orange
[1583] are nearby in
representation space
[1585] is because those two things
co-occur in kitchens.
[1587] And elephants don't
tend to co-occur
[1589] with those items as much.
[1591] And one of the interesting
things about this model
[1593] is that if these observation
functions are bijective, then
[1598] not only do you converge
to the co-occurrence
[1600] of the observations,
you converge
[1602] to the co-occurrence of
the underlying events
[1604] because bijective
observation functions
[1607] on discrete random variables
preserve probability.
[1609] And so all these things
work out to be the same.
[1611] So what that boils
down to saying
[1613] is that the different views
that satisfy these properties
[1617] will converge to
the same kernel.
[1618] So the language representation
and the visual representation
[1621] will converge.
[1622] So a little bit of a mix
of Plato and Wittgenstein.
[1625] Maybe I should have chosen
more recent researchers.
[1628] But I went with those.
[1631] So that's just one
mathematical model
[1635] of what might be going on here.
[1640] I think I'll skip
that small example.
[1643] And I want to talk about
limitations and implications
[1646] because I think those
are maybe the most
[1648] interesting to get into.
[1652] So again, I think I know what
a lot of you might be thinking.
[1655] Hold on.
[1656] An image is not
equivalent to a sentence.
[1660] Again, if I go and see the
total solar eclipse a month ago,
[1666] that experience, I
just can't describe it.
[1668] It's ineffable, right?
[1668] There's no words to describe it.
[1671] Or if I am writing
an essay and I
[1675] talk about this
concept of free speech,
[1677] this is an abstract concept.
[1679] There's no image that
captures that concept.
[1681] So I think this is a
really valid criticism.
[1683] Different modalities
aren't actually
[1685] all bijective with some
underlying representation.
[1688] They might have different--
fundamentally different
[1690] information.
[1691] So I don't quite know how
to fully resolve this.
[1694] The empirical evidence
suggests we're
[1695] seeing some convergence,
despite that this might be true.
[1698] But this is a real limitation.
[1702] Mathematically,
in these cases, we
[1703] don't have that-- we don't
satisfy that mathematical model
[1706] I gave you.
[1707] The observation function is
lossy or abstract or partial.
[1712] It's not a complete
representation
[1714] of the underlying world.
[1717] But despite this, we do see
some interesting convergence.
[1720] I think one example
is that CLIP is
[1722] trained to reduce image
representations to just
[1726] being captions.
[1727] It's trained to align
visual representations
[1729] with language representations.
[1730] And yet we love it
in computer vision.
[1732] It works really, really
well, despite that it's
[1734] trained to throw away
everything about vision other
[1736] than language.
[1738] OK, so maybe
language is actually
[1739] closer to a complete
representation
[1741] of what we care about in
vision than we thought.
[1743] But it is a limitation.
[1747] Another limitation--
oh, actually,
[1750] probing that limitation
a little bit more,
[1752] so one implication is that
the more lossy and incomplete
[1757] is your observation
in language, the more
[1761] it might not match
what is in the image.
[1764] Because a single
word is not going
[1766] to fully describe an image.
[1767] And a caption might only
partially describe an image.
[1769] But we did an experiment,
which is, well,
[1770] what about 1,000 words?
[1772] So we varied the number
of words in captions
[1777] and measured the alignment
between the captions
[1780] and the visual data.
[1781] We only went up to 30
words, not 1,000 words.
[1783] But you can see
the trend goes up.
[1784] So the kernel alignment
between rich captions
[1787] with the corresponding
images is higher
[1789] than the kernel alignment
between just a single word
[1792] or a very partial caption.
[1793] So it kind of makes sense.
[1794] It's kind of consistent
with this idea
[1796] that as you get closer
and closer to complete
[1798] bijective observations, you will
get better and better alignment
[1803] with the vision modality.
[1808] Imperfect alignment-- so I
told you that on our metrics,
[1812] we haven't explained all
the variance by any means.
[1815] There's a lot more
variance left to explain.
[1817] So this is an open challenge.
[1819] And one other thing
for the people
[1821] who are deeper into this field
of representational alignment
[1824] is, technically, we're not
seeing global structure
[1827] alignment.
[1827] We're seeing local
structure alignment.
[1829] So if you're familiar
with the CKA metric--
[1832] this is for the people that are
really experts in this area--
[1835] we're actually not seeing
increasing CKA alignment.
[1838] This is a measure
of global structure.
[1840] We're seeing-- we only see this
alignment when we look at local
[1843] nearest neighbor structure.
[1844] So this is a detail
to the analysis.
[1846] But I'm happy to
talk more about that.
[1849] [INAUDIBLE], yeah.
[1850] AUDIENCE: Yeah,
Phillip, appreciate
[1851] the y-axis misalignment
[INAUDIBLE].
[1855] Can you say what it
is for a random model?
[1858] What's the floor?
[1859] What's the kernel of a
randomly initialized model?
[1861] [INAUDIBLE]
[1863] PHILLIP ISOLA: Right.
[1864] So for random model, I think
it's roughly 0 on this metric.
[1868] Tongzhou, is that right?
[1869] TONGZHOU WANG: For a
purely random process,
[1871] not the [INAUDIBLE] network.
[1872] PHILLIP ISOLA: No,
random network, though.
[1874] AUDIENCE: Random parameters,
but up the data points,
[1876] still encoding them as a kernel.
[1877] TONGZHOU WANG: I don't
have that number.
[1878] But that's a purely
random process.
[1880] Without network
[INAUDIBLE] bias.
[1882] It's much, much
lower [INAUDIBLE].
[1884] AUDIENCE: I think-- but--
[1885] PHILLIP ISOLA: Yeah,
that's a good baseline.
[1886] We should come back to that.
[1887] Yeah, I don't know
the exact number.
[1889] I think it's quite
a bit lower, though.
[1891] So another thing that
you might have in mind
[1893] is, OK, yeah, I buy
this convergence.
[1895] That's-- empirically, that
seems to be going on, but not
[1897] because they're converging
to some platonic reality.
[1899] These are [? BS ?] machines.
[1901] They're converging
to just dumb models.
[1904] OK, so valid.
[1905] It could be maybe all these
models are converging,
[1907] but not to a good representation
of the world, but to just
[1910] being these superficial,
stochastic parrots, maybe.
[1914] So it could be that there
are fundamental limitations.
[1916] We're all using transformers.
[1917] We're all doing next
token prediction.
[1919] And this is just flawed.
[1920] That's an option, too.
[1924] Maybe it's
socio-technical biases.
[1925] We all chat, and I tell you,
yeah, transformers are amazing.
[1928] They're converging.
[1928] Then you go and use them, and
it increases the convergence.
[1931] So maybe don't take that lesson.
[1934] OK, so there's a
lot of limitations.
[1936] There's some other ones
we discuss in the paper.
[1938] I think there's also really
interesting implications.
[1940] And I want to end
with the implications.
[1942] So one implication
is that there's
[1946] this complementarity between
all of these different sensory
[1949] modalities.
[1950] And we've seen this a lot.
[1950] We've talked a lot about this.
[1952] Again, [? Shimon ?] was
posing the question yesterday
[1955] that if I want to
train a vision model,
[1960] well, this implies
that I should be
[1962] able to use language data,
too, because the underlying
[1965] kernel, the
underlying structure,
[1966] if it's really
shared between them,
[1968] then I can get there
via multiple paths.
[1970] And I might as well use all
the paths available to me
[1972] to increase the rate at which
I get to that representation.
[1978] And I think an
interesting experiment
[1980] could be it should be the case
that to train a vision model,
[1984] there's value to
training it on a word.
[1985] A word should be worth n
pixels to a vision model.
[1989] And a pixel should be worth
m words to a language model.
[1992] If I train--
[1993] I'm going to train
a language model,
[1994] I should train it
on pixels, too.
[1995] That should help my performance.
[1998] And there's some evidence.
[1999] People are starting to do that.
[2000] There's some evidence of this.
[2001] But I think it's only--
[2002] in LLM land, it's only
a little bit explored.
[2005] Most LLMs are only
trained on language data.
[2007] But this implies you
should train them
[2009] on other types of data, too.
[2010] And they should get better
at language modeling.
[2012] And there's some evidence--
[2013] I mean, this is from
the GPT-4v blog post.
[2016] So it's not-- who knows
if it's replicable.
[2018] But they say that if you train
GPT-4 jointly with vision
[2024] model-- so GPT-4v has joint
vision and language model--
[2027] you do better at pure
language-reasoning tasks
[2030] than if you don't use vision.
[2032] So there's some transfer
between the modalities.
[2036] Another interesting implication
is that it should somehow
[2039] be relatively easy to
translate or convert
[2046] between different
representational formats
[2048] for different modalities
if they're all converging
[2050] to the same representation.
[2051] So, for example, it
should be relatively
[2053] easy to translate
between images and text
[2057] if their representations
are the same.
[2060] When you train a representation
of text and images
[2063] and they converge to
the same representation,
[2064] it will act like a bridge.
[2065] And maybe you'll only
need a little bit of data
[2067] to find the mapping from
the visual representation
[2070] to the text representation.
[2073] And this is something
I think that we also
[2075] see in practice to some degree.
[2076] There's a lot of success
of unpaired translation,
[2079] of translation
between modalities.
[2081] There's some interesting
work from Sompolinsky,
[2083] et al., or Sorscher,
et al., showing
[2086] that you can do unpaired
translation between images
[2089] and text to a certain degree.
[2091] And the idea is
basically the same,
[2092] that if the representations
that you get in each modality
[2095] are the same, then you just
have to align those two
[2097] representations up to some kind
of permutation or some rotation.
[2103] And this is just another
old philosophical question,
[2107] this Molyneux's problem
maybe you've heard about.
[2109] Imagine that a
child is born blind.
[2112] They only know how to
discriminate shapes by touch.
[2115] And then they are given sight.
[2117] Would they immediately be able
to discriminate shapes by sight?
[2122] And I think an implication of
this hypothesis, a postdiction
[2125] of this hypothesis would be
that, well, not immediately.
[2130] But it shouldn't-- it should
be relatively easy to take
[2133] your representation
learned from touch,
[2135] or maybe from
language in this case,
[2137] and use it as a target to learn
a representation for vision.
[2141] So you still have to
learn this arrow going
[2143] from the new modality, the
eyesight you've been given.
[2146] But you already have the kernel.
[2148] And half the battle, or
maybe a lot of the battle
[2150] was learning this
kernel structure.
[2151] So you already have it.
[2152] And you just have to learn how
to map the new modality into it.
[2154] And indeed, there's a
lot of interesting work.
[2156] I think we heard a bit about
it on one of the early--
[2158] the first days of this workshop,
that people have tried this now.
[2162] They've done things like
Pawan Sinha did this Project
[2164] Prakash, where he gave--
[2166] where they had surgeons
that would operate
[2167] on children who had cataracts.
[2169] They get sight for
the first time.
[2171] And it doesn't take them very
long to understand images.
[2174] Now, they don't
have it immediately.
[2176] But it's not very long.
[2180] OK, so I think there's
a lot more to discuss.
[2183] I'll end with the
final implication
[2184] being that if there is
some endpoint to all this,
[2186] if these things are
heading toward something,
[2189] we should work to
characterize it.
[2191] And think it's a
great challenge.
[2194] I hope that we can get a better
idea of what that model is.
[2198] Or if this is just
not true at all,
[2200] we should prove that
and show that, too.
[2202] So I will thank my co-authors
and funding agencies.
[2207] [APPLAUSE]
[2212] So I'm also moderating.
[2214] So I'll say five
minutes for questions.
[2215] OK, [? Shimon. ?]
[2217] AUDIENCE: So one thing is
an alternative or maybe
[2222] a similar view, if
the convergence may
[2225] be related to finding
the close-- the simplest
[2228] program that generates
[? beyond ?] the observation.
[2231] And this was-- it
would lead-- it
[2234] tends to find the latent
variables that actually
[2239] generated the observations.
[2241] And the exact observation,
different system
[2245] would get some different
observation of the same system.
[2247] They will end up with recovering
the same latent variables.
[2251] And it will not depend on the
computer that made it and so on.
[2255] So maybe there is a
direction of whatever
[2258] we do is we're
eventually recovering
[2260] the correct latent variables
and so on and so forth.
[2264] So anyway, this
general direction.
[2266] PHILLIP ISOLA: Yeah, I find
that really compelling.
[2268] So we had a section
I skipped, which
[2270] we called the Simplicity Bias
Hypothesis, which is roughly
[2274] that there are many ways of
fitting whatever data you have.
[2276] But under the pressure
to find the simplest,
[2279] you will get more
convergence than if you
[2281] don't have that pressure.
[2283] And, yeah, maybe
the simplest program
[2284] is somehow we're working
our way toward that simplest
[2288] program via regularization,
implicit and explicit.
[2291] I think it's speculation.
[2293] But it's interesting
to consider that.
[2295] AUDIENCE: [INAUDIBLE]
on some data,
[2296] some recent data or some
arguments that deep networks
[2302] actually have bias towards--
[2304] PHILLIP ISOLA: Yes.
[2304] AUDIENCE: --the lowest
complexity and so on,
[2306] in some way, and so on.
[2307] So maybe all of this--
[2308] PHILLIP ISOLA: I think
it all fits together.
[2310] And actually, Jacob, one of the
authors, had one of those papers
[2313] on deep nets have the bias
toward the simplest structure.
[2315] But I think there's still a lot
of open questions there, yeah.
[2319] [? Andrea. ?]
[2319] AUDIENCE: Just a comment.
[2320] It's on your
[? projecting ?] assumption.
[2324] Maybe you're winning a bit at
the moment because you're using
[2326] networks that have been
trained for recognition,
[2328] whereas if you had-- say you
had a network that had just been
[2331] trained to do reconstruction,
3D reconstruction,
[2333] maybe this wouldn't
work so well.
[2335] PHILLIP ISOLA: Yeah.
[2336] AUDIENCE: So it's just
possible you're seeing
[2338] something because of that.
[2339] PHILLIP ISOLA: It could be.
[2341] I think some-- are--
[2342] I don't know.
[2343] [INAUDIBLE], are
some of the models
[2345] that we have trained
for reconstruction
[2346] rather than recognition?
[2348] AUDIENCE: There are maybe
some that [INAUDIBLE].
[2350] PHILLIP ISOLA: OK, yeah,
so we have MAEs in there.
[2352] But they actually are
kind of an outlier.
[2354] So that's a little bit
of a violation, yeah.
[2357] AUDIENCE: [INAUDIBLE] can we
trained through 3D [? depth ?]
[2360] prediction?
[2360] So [INAUDIBLE] it's
not completely solid.
[2363] But it's just [INAUDIBLE] you're
seeing something like that,
[2366] maybe?
[2367] PHILLIP ISOLA: Yeah, I
think that's a good point.
[2369] And maybe, yeah,
contrastive-- it's
[2370] like instance discrimination
and classification,
[2373] these might all be more
alike than we really realize.
[2375] Even though I said they're
different objectives,
[2377] they're maybe not
that different, yeah.
[2379] Yeah, that's a good point.
[2381] Let's go to the back.
[2383] AUDIENCE: Yes, I guess this is
motivated by the possibility
[2386] that the representations
learned by these models don't
[2390] necessarily align with
representations that humans have
[2393] or of underlying true reality.
[2396] So I guess it seems like the
data that these models are
[2399] trained on is
curated in some way.
[2402] Like the statistics, the
text on the internet,
[2405] the images on the internet
don't think-- they selectively
[2409] pick out remarkable
things about the world.
[2411] It's not necessarily a random
sample over all possible data
[2415] that you could observe.
[2416] So I guess taking
that into account,
[2420] what is the implication of this
curation for representations
[2425] that come downstream of that?
[2428] PHILLIP ISOLA: I think
that's a great question.
[2430] So the data sets that we use
to train these models are
[2434] different in a lot of ways.
[2435] But they share one thing
in common, which is
[2437] they're all internet data sets.
[2439] They're all photos
and captions and texts
[2441] downloaded from the internet.
[2442] And that might be a very biased
and curated type of data.
[2446] If you just had a
robot on Mars, it
[2447] might come up with a very
different representation.
[2450] So I think that's
an open question.
[2453] I guess the strong
form of the hypothesis
[2455] is that, no, the
robot on Mars will
[2457] find the same
representation because it's
[2459] more about physics and the
underlying, like, you know,
[2462] F equals ma.
[2462] But I think I would believe
more in some data distribution
[2466] properties do really matter.
[2468] AUDIENCE: [INAUDIBLE] NASA would
upload the data to the internet.
[2470] PHILLIP ISOLA: NASA will upload
the data to the internet, yeah.
[2472] OK, Dan, here.
[2474] AUDIENCE: Yeah, so I guess
my very minor comment, which
[2477] is at some point you said
that maybe the strong form
[2481] of the hypothesis is that the
best vision model is the best
[2484] language model.
[2485] But maybe is what
you're saying that the--
[2489] some late layer of
the best vision model
[2491] has the same representation
as some [INAUDIBLE] layer?
[2495] Because it's not-- the
models are the same.
[2497] I mean, obviously
they're computing things.
[2499] PHILLIP ISOLA: Yeah,
just the kernels align
[2503] at some layer of
the models is maybe
[2504] what the statement would be.
[2506] AUDIENCE: But you could ask
whether like the intermediate or
[2508] early layers look similar.
[2510] And if they come to look
very similar in between,
[2514] that would be even
more surprising, right?
[2516] If an intermediate
layer came to look--
[2519] of a language model came to look
like an intermediate language
[2522] layer of a model, that
would be really unusual.
[2525] PHILLIP ISOLA: That
would be-- yeah,
[2526] so we a search over
multiple layers
[2529] and take the average
or the max, depending
[2531] on how we measure things.
[2533] So we don't really see this
layer-by-layer sequence being
[2535] matched between the two models.
[2537] But it's more like somewhere
in both of the networks
[2538] the kernels align.
[2539] AUDIENCE: Right.
[2540] So the hypothesis that they're
representing the same thing
[2542] is reasonable.
[2543] But it would be really
surprising if it turned out--
[2545] PHILLIP ISOLA: I agree.
[2546] AUDIENCE: Yeah.
[2546] PHILLIP ISOLA: That
would be even stronger.
[2547] AUDIENCE: [INAUDIBLE]
tracking it.
[2547] PHILLIP ISOLA: Yeah, we
haven't seen that yet.
[2549] Yeah, [? Leslie. ?]
[2550] AUDIENCE: [? I ?] [? guess ?]
another question is something
[2552] like, if you trained
on very different--
[2561] supposedly very different
data distribution,
[2563] not so much Mars because that's
the world's pictures [INAUDIBLE]
[2565] whatever, but just only
spatial transcriptomics data,
[2568] tons and tons of spatial
transcriptomics data,
[2572] would you expect it to
be the same asymptote?
[2575] Or would you expect it-- yeah,
maybe it goes up for a while.
[2578] And then it asymptotes lower.
[2580] PHILLIP ISOLA: I think every--
[2581] OK, so one of the
assumptions to this model,
[2584] the mathematical
version of the model,
[2586] is that you train on the
same distribution of events,
[2588] not the same data, but
the same distribution
[2590] over underlying events
that generate the data.
[2593] And the more you
violate that, the more
[2595] I think this might not be true.
[2596] But I expect that for
different problems and domains,
[2599] there'll be a percent-- a
degree to which this is true.
[2602] Yeah, so I don't know.
[2603] Leslie?
[2604] AUDIENCE: Suppose
this alignment,
[2605] should we think of it
as being marginally very
[2608] weak or very strong?
[2609] Or how do you think
of it quantitatively?
[2611] PHILLIP ISOLA: Right.
[2612] Is-- just on the scale of
0 to 1, like, it's point--
[2616] AUDIENCE: [INAUDIBLE]
[? extremely ?] strong?
[2618] PHILLIP ISOLA: I think
it's fairly strong.
[2620] So the meaning of that number is
the percent of nearest neighbors
[2624] that are in common between
the two kernels on average.
[2628] So if I take an item and I find
its nearest neighbors in one--
[2631] under one kernel, and I take
an item and I find its nearest
[2633] neighbors under another
kernel, it says,
[2634] about 1 out of 5 nearest
neighbors against a dictionary
[2637] of 1,000 possible
neighbors is shared.
[2641] OK, I think that we should
take the rest of the discussion
[2643] to the break.
[2644] So I'm happy to chat more.
[2645] But I also need to moderate
and move things forward.
[2647] So I'm going to say,
we'll come back at--
[2651] [? Sherry, ?] what time
are we coming back?
[2652] Is it 3:45.
[2657] 3:45.
[2658] Yeah, come back at 3:45.
[2660] Thank you.
[2661] [APPLAUSE]
[2665] [SIDE CONVERSATIONS]
