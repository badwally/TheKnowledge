---
schema_version: 1
id: yt-NvbkfNxLVAA
type: youtube
title: Alex Huth - 2019 CCN Workshop at Dartmouth College
url: https://www.youtube.com/watch?v=NvbkfNxLVAA
authors:
- Dartmouth
ingested_at: '2026-05-30T20:02:04Z'
content_hash: sha256:8485fde36618b6592a8bd582c9ed1e6744a5c5f7676bb90786138b252a5ad5a1
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Dartmouth
  channel_url: https://www.youtube.com/@dartmouth
  duration_seconds: 3665
  caption_track: fetched
  snippet_count: 1469
filter:
  score: 0.8
---
[4] - Hey everyone, yeah,
[8] excited to talk to you about this stuff.
[9] So, I'm Alex Huth.
[10] I'm a professor at UT Austin.
[14] I feel like I'm having deja vu
[16] 'cause I gave a talk in this room
[17] from the same podium
almost exactly a year ago
[19] at the summer school here.
But this is not the same talk,
[22] so if any of you were here.
[24] Okay, so the title of my talk today is,
[26] Beyond Distributional Embeddings
[28] for Modeling Brain Responses to Language.
[30] So this is talking about a couple
[32] different ways that we can go further
[36] than just using distributional
word embeddings,
[39] which have kind of become
a pretty standard tool
[42] for trying to understand how the brain
[44] represents words in language.
[46] So, I'm going to start with
(laughs) a very high level thing
[49] that is really maybe not that
meaningful in any real way,
[53] but the question that we
want to address here is
[56] how do we understand language?
[58] How do we take these words
that are coming into our ears,
[63] our brain does something with them,
[65] something happens inside our heads,
[67] there's an idea maybe, a picture,
[70] something happens that is like
the byproduct of language.
[75] How does this process work?
[77] I don't know that I can
explain what understanding is,
[80] so I'll leave that for a later point.
[85] But I'm going to operationalize
this into a very specific
[88] sort of mathematical problem
[89] that is much easier to attack than trying
[91] to understand understanding.
[93] So I'm going to show you a bunch
of pictures of brains today,
[97] and I want to sort of orient you on how
[100] to read cortical flat maps which is
[102] what all these pictures are going to be.
[104] So let me start by doing that.
[106] So all the work I'm going
to show you is using fMRI
[109] to look at how the brain is
processing natural language,
[113] and to visualize this data,
[114] we're really only interested
[116] in cerebral cortex for the most part.
[118] I'm only going to show you
data from cerebral cortex,
[121] and cerebral cortex is of
course a sheet of neural tissue.
[124] So to visualize this we can take,
[126] from a high resolution 3-D MRI scan.
[130] We can reconstruct three-dimensional
version of the surface.
[134] We can make relaxation cuts
into the cortical surface
[137] after inflating it and then flatten it out
[138] so that we can see the
entire cortical surface
[140] all at once like so.
[144] So this is showing all of
the cortex for one subject.
[146] This is the left hemisphere
and the right hemisphere.
[149] This is the occipital cortex
is in the back of the brain
[152] is in the middle here,
[153] and then pre-frontal cortex
is out on either end.
[157] Areas that we know about in cortex,
[159] areas that we have good localizers for,
[162] we've outlined in white here.
[164] So we have like early visual cortex,
[166] this is V1 through V4.
[167] There's a lot of visual, sort
of category selective areas
[170] around visual cortex.
[171] This is auditory cortex,
this is my motor cortex,
[175] Broca's area and so on.
[177] But there's a lot of parts of cortex
[180] that aren't outlined here and
we don't have very good ideas
[182] or we don't easy ways to localize them,
[184] and yet, we'll find they
still respond to language.
[187] So, the kind of experiment that I do
[192] is a little different from a lot of,
[196] sort of neuroscience,
psychology experiments.
[198] Instead of having a controlled setting,
[201] where you might have people
[203] in a number of conditions,
[205] sort of look at very specific stimuli,
[208] I just have people lay in an MRI scanner
[210] and listen to stories.
[212] That's all.
[213] So they're going to lay there,
[215] and listen to somebody tell them a story.
[217] It's going to be an interesting story.
[218] We took stories from
The Moth, "Radio Hour,"
[220] which is wonderful storytelling podcast.
[223] If any of you are familiar
with it, or radio show.
[226] They're fun, so this actually a kind
[228] of fun experiment to be a subject for,
[230] unlike pretty much every
other fMRI experiment
[232] I've even been a subject for.
[234] They're awful.
[235] But this is just you lay there
[236] and listen to a podcast.
[237] This is like what we
do all the time anyway.
[239] I don't know.
[240] Some of this.
[242] So I want to show you a little bit
[244] of what this data looks like
[246] before I talk about how
we're going to analyze it.
[250] So it's going to be on
a flap map like this.
[252] Here we go.
[254] This is a different subject's brain.
[257] What I'm showing here is not the activity
[260] at each point in time
that we record with fMRI.
[263] It's not neural activity,
[264] anyone who calls it
neural is lying to you.
[267] fMRI is blood flow.
[268] It is a kind of crappy indicator
[271] of something that might be vaguely neural,
[273] but it's the best we can
get for whole human brains.
[277] Red spots are places that
have above average activity.
[280] Blue spots here have
below average activity,
[283] where average is just defined
[284] as like the average over this scan.
[288] It's going to play out slowly,
[289] because of course we're
reporting blood flow,
[291] which changes much more slowly
[292] than actual neural activity.
[295] And you're going to hear the story
[297] of the person's hearing
and see the brain activity.
[300] This is actually not one of the stories
[302] that we use in this main experiment.
[303] It's just for illustrative purposes.
[305] This is 15-second snippets
of a few different stories,
[308] stuck together.
[309] And the game that I want you guys
[311] to try to play, is to
listen and look at the words
[314] that are coming here,
[315] and try to figure out what the mapping is
[317] between these words
and the brain activity,
[320] and see if that means anything to you.
[322] So let's give this a shot.
[324] - [Narrator] What a crazy world
[326] we're bringing our children into.
[327] He thought it sounded
like the kind of statement
[330] that brings people closer together,
[332] pointing as it did to their common fate.
[334] But the sexy mom just glared at him
[337] and took the healthy living supplement too
[339] without asking.
[340] - [Narrator] He put Lily
in charge of the party
[341] while he was gone,
[342] and then he walked downstairs
[343] and there must have been
5000 people milling around,
[346] wrapped in furs or long overcoats,
[348] or ski parkas, leather jackets,
[350] high school, college kids,
[351] heavily champagned 60 year-olds,
[353] liking arms and singing.
[354] - [Narrator] Only the two front windows
[356] with white shades lowered
were not somehow blanketed.
[359] Your eye was constantly drawn
[361] to where the material
converged mid-ceiling,
[364] punctured by a dazzling, pink spotlight
[367] that looked like it might have
just vaporized a flamingo.
[369] She...
[372] - All right, so this is kind of tricky.
[373] I've stirred up this kind of thing a lot.
[375] It's very hard to do by eye,
[376] but it turns out we
have mathematical tools
[378] that can come to the rescue.
[379] Okay, so going back to
the original question,
[381] which I posed as this very broad like,
[383] how does the brain understand language?
[385] I'm going to operationalize
that question here,
[388] as a mathematical object,
[391] which is how well can we
predict, bring responses
[395] to natural language,
which is what this is,
[397] using some kind of model,
[399] some kind of mathematical
quantitative model.
[403] This doesn't tell us
exactly how the brain...
[406] It's very far from telling us
[407] how the brain actually
understands language,
[408] but it's something that
we can try to optimize.
[409] It's something that we
can try to improve on,
[411] and we can compare different models.
[413] So let me tell you how
this actually works.
[415] Okay, we use a technique
called Voxelwise modeling,
[419] that's been developed over
the past decade or more
[423] in Jack Gallant's lab.
[425] I'm going to run you
through the basic flow
[427] of how this goes.
[428] We take some natural stimuli.
[430] In this case, it was natural stories,
[431] we play them for our subject
and record fMRI data.
[436] Notice that this is sort
[438] of the experimental data collection part
[439] of this procedure,
[443] and there's actually
no hypothesis embedded
[445] in the experiment whatsoever.
[446] The experiment itself is hypothesis-free,
[448] which is actually very powerful,
[451] because that means that
we're not sort of constrained
[455] to testing specific hypotheses
[457] by our data collection procedure.
[459] But it also is a little bit difficult,
[463] because then we have to figure out
[463] how to actually instantiate hypotheses.
[465] That comes in this sort
of second stream here.
[468] So we take these same natural stimuli,
[471] we have some hypothesis
about some kind of feature
[473] that we think might be
represented in the brain.
[476] We extract that feature,
or that set of features,
[479] that feature space from the stimuli,
[482] and then in this first
stage of Voxelwise modeling,
[484] which we call the estimation stage,
[485] we're going to estimate these
Voxelwise regression models,
[489] which predict the response of each voxel,
[492] in the fMRI data, that's
each sort of point
[494] that we measure fMRI bold responses at,
[498] using the hypothesized
features, and the fMRI data.
[501] So these two come together
[502] to give us the Voxelwise
regression models,
[504] that I'll tell you more
detail about in a moment.
[507] Then in a second stage,
[509] we're going to take new natural stimuli,
[511] we're going to play them for our subjects,
[513] and get new fMRI data.
[514] So this is stimuli that the
model hasn't seen before,
[516] and the subject hasn't seen before.
[518] We're going to project those stimuli
[521] into our same hypothesized feature space,
[523] extract features from
them in the same way,
[526] and then use the regression models
[527] that we fit in the earlier stage
[528] to predict these new fMRI data.
[531] And we can measure how
good these predictions are.
[534] We can measure the correlation
[535] between our predicted and
actual response time courses
[538] for some voxel, and
that will give a score,
[540] a very quantitative score,
[541] of how well we're doing
at actually predicting
[544] this piece of brain.
[545] How well we're doing at
predicting what it does
[547] in response to natural language,
[548] which is very good benchmark
[549] for understanding what it
does in general, I think.
[553] Okay, so if this prediction works well,
[556] we can then try to understand what is it
[559] about the features that actually
[561] drives the responses in
something particular voxel.
[564] We can try to figure out which features
[566] maybe have high weights
in a regression model
[568] and use that to do some interpretation
[570] of what the different parts
of the brain are doing.
[572] That's fine, and I'll show
you an example of that later.
[576] But another thing we can
do which is very powerful,
[578] is that we can actually take our stimuli
[580] and project them into
different feature spaces.
[583] We're not constrained to
just one feature space here.
[585] We're not constrained to
testing one hypothesis,
[587] because our data didn't
have one hypothesis
[588] embedded in it when we
collected it in the first place.
[591] So we can extract these
different sets of features,
[594] go through this whole procedure
[595] with each set of features,
[597] and then see which one
explains the brain data better.
[600] Which one of these is a better fit
[601] to the actual brain data?
[604] And the sort of underlying
assumption here,
[606] is that the feature space that
best predicts brain activity,
[609] is the closest match to what the brain
[612] is actually computing.
[613] This has a lot of caveats in it,
[615] but this is sort of broadly the philosophy
[618] of the Voxelwise modeling procedure.
[621] Okay, so let's actually
talk about a specific model
[625] for this data.
[626] So this is a strong man model,
[629] but that's what makes it fun.
[631] So a very simple model might be
[634] that each voxel responds
some amount to each word.
[639] So here I have a voxel
response time course,
[642] this Ri of T, and my model
for that is going to be
[647] a weighted sum, of the w's are
going to indicator variables
[651] for different words.
[652] So the words are going to be
indexed, j equals one through n,
[657] and this is like, suppose
one of the words is penguin,
[660] then the indicator variable
for penguin is zero,
[664] whenever you hear a
word that's not penguin.
[666] Then it's one whenever
you hear the penguin.
[670] Now beta is going to be
the weight on that word.
[674] So this saying like how
much does this voxel
[677] respond to the word penguin?
[680] And we're saying that
the response time course
[682] of the voxel is a weighted
sum across all the words.
[685] So we're summing across all
of these different words.
[687] So this is like saying
that each part of the brain
[689] responds a little bit,
[691] maybe response goes up,
maybe the response goes down.
[694] Maybe it doesn't do anything at all,
[697] in response to every word you hear,
[699] which is very simplistic and
kind of crappy assumption,
[702] and that's why I'm calling
that the simplest model.
[705] Okay, so we know what the words are,
[709] because we know what the stories are
[710] that we played for our subject.
[711] We know what the responses are,
[713] because we recorded them, using fMRI.
[716] So the only thing we need is the betas.
[719] So how do we get that?
[721] We're going to do regularized regression,
[723] which I'm presenting here in
a sort of Bayesian framework,
[726] because that makes another
explanation easier later on.
[730] So the beta-hats, which
are estimated betas,
[733] these weights for each voxel,
[735] are the betas that maximize the product
[738] of a likelihood function,
[740] which is the probability
of observing this response,
[742] give the beta and the weights.
[743] This is just squared error, more or less,
[745] or e to the minus squared error.
[747] The product of this and prior,
[750] which is something that we think we know
[753] about beta already.
[755] We use ridge regression, which
is regularized regression,
[759] so to solve for beta,
[762] which means that we
have a prior that is...
[766] Essentially we assume
that these betas are,
[768] come from a normal distribution,
[769] that has zero mean and
identity covariance,
[772] which means that every word is unrelated
[774] to every other word.
[775] That's sort of the core
assumption in this model,
[778] is that all these words are
independent from each other.
[781] Okay, now we can fit this model,
[785] and we can test this model.
[786] So we fit it on a whole bunch of data.
[789] In the examples I'm going to show,
[790] we fit it on about two hours of data
[792] of subjects listening to stories,
[794] and then we have one
story that we held out,
[795] about 10 minutes long,
[796] and we can predict responses to that story
[799] given the models that we fit.
[802] And then we can compute the correlation
[804] between our predicted
and actual responses,
[807] and that's what this is.
[809] So here I've colored each voxel,
[810] according to its correlation
[812] between the predicted and actual response.
[813] So it's how well we're doing
[814] at predicting that piece of brain.
[817] The colors are gray for voxels
that are non-significant,
[820] red for voxels that are kind of crummy,
[822] and yellow for voxels
that are pretty good.
[823] You can see that this model,
[825] it does kind of okay in
some parts of the brain.
[828] So we have like this sort of
higher auditory cortex stuff,
[831] does reasonably well.
[833] This like, Broca's area
stuff does reasonably well.
[836] A little bit of other
junk in here, but it's...
[839] I don't know if you have
anything to compare this to,
[841] but this is not super good.
[842] Like we can do better.
[844] So how do we improve this model?
[845] How do we go further than just saying
[848] that we have some response to each word,
[851] then they're different,
and that's all we know.
[854] So one thing that I'm
interested in is semantics.
[859] I think that's why we're all here.
[862] So one thing that we can do
to try to improve this model,
[865] is to make a guess
before we fit the model,
[868] which is that we might
see similar responses
[871] to words that have similar meanings.
[876] So for instance, the words
month, week, and hour,
[879] all have related meanings.
[881] They all correspond to durations of time,
[882] so we might expect that we should see
[885] some part of the brain responds
a lot to the word month.
[889] It might also respond to the word week,
[891] and to the word hour.
[892] That would be a sort of
reasonable supposition
[895] that we can make.
[896] Similarly for other categories of words.
[899] How do we get these similarities,
[901] where do these come from?
[902] This is kind of the key question.
[903] So it turns out we get
this from word embeddings.
[908] So we get them from looking
at how words are used,
[911] across the the large corpus of text.
[913] This is now a very standard method.
[916] Goes back 30 years, I believe,
[918] to the earliest sort
of word embedding work,
[921] although the sort of
distributional hypothesis,
[923] this is based on, it
goes back even further.
[925] The exact embedding method
that we use doesn't matter,
[929] so in this case I used embeddings
[931] that are about 1000 dimensions
[932] for each word.
[934] The only thing that matters
is that the similarities
[936] between words are computed
as the dot-products
[938] between these embedding vectors.
[940] And this was actually...
[943] I'll come back to this.
[944] Okay, so this is how we estimate
[947] sort of which words are similar.
[949] It's based on how these
words are used in text.
[951] It's actually based on the similarity
[953] between the contexts, in
which these words appear.
[956] That's what we're using as our proxy
[957] for similarity of meaning,
[962] based on, of course, this
distributional hypothesis,
[964] "You shall know a word
by the company it keeps."
[966] Okay, so, now how do we
actually incorporate this
[971] into our model?
[971] How do we actually add in this information
[973] about which words mean similar things
[975] to this model that
predicts brain activity?
[979] So this was the model-fitting procedure
[983] that I told you about a moment ago,
[984] where we find the betas
that maximize the product
[987] of this likelihood function,
[988] which is just how well they fit the data,
[990] and a prior, which is what we think
[992] we know about them beforehand,
[994] and I told you that we use
this sort of dumb prior before,
[997] which is just that each
word is independent,
[998] but that the weights are small,
[999] but we can swap that out
for this better prior.
[1003] So let's, instead of assuming
[1006] that all the words are independent,
[1007] we can capture this intuition
[1009] that we should have similar responses
[1010] to words with similar meanings,
by changing our prior,
[1013] by replacing with now,
a normal distribution
[1016] where the covariance is given
[1018] by the similarity of words,
[1021] according to these word embeddings.
[1024] This, this explanation
of what we're doing,
[1027] this is not actually the explanation,
[1029] that when we wrote a paper about this,
[1031] that we used to describe this method.
[1034] We only realized later
[1035] that this is actually sort
of the underlying thing
[1038] that's happening here.
[1039] What we did originally,
was we actually fit models,
[1041] instead of fitting a weight per word,
[1043] we fit a weight per, sort
of word embedding dimension,
[1049] and to do that, we have to talk
[1050] about semantic features,
[1051] and then things get weird,
[1052] because these semantic
features that you get
[1054] out of word-embedding spaces,
[1055] they don't necessarily make sense.
[1056] They don't mean anything on their own.
[1060] But it turns out that sort of hiding
[1061] under this, was this really
nice mathematical fact
[1064] that what we were doing implicitly
[1066] was using the word embedding
[1068] as to kind of regularize the
models that we were fitting.
[1073] Anyway this is exciting.
[1073] We just had a paper come out recently
[1074] where we had sort of
described this new way
[1077] of looking at this problem.
[1079] And I want to point out here that,
[1082] this is not representational
similarity analysis.
[1083] It has a kind of flavor of that,
[1085] it looks like that, we
have a similarity space,
[1087] but this is not our say,
[1089] and in fact we have a paper
[1092] that is written but not submitted yet,
[1095] where we argue that there are like
[1096] sort of deep statistical problems
[1098] with RSA, especially when you use it
[1100] to compare models.
[1101] Stay tuned for that.
[1103] I don't know, someday.
[1105] All right, so fit this new model
[1107] that's like the improved model
[1109] that incorporates semantic similarity,
[1111] and then we test it as we did before.
[1115] And it turns out that it
works much better than before.
[1117] And to remind you, here's the...
[1120] This is what the map looked like
[1121] when we had the sort of
independent words model,
[1124] and this is what it looks like
[1125] when we incorporate word similarity,
[1126] when we allow the semantic similarity
[1129] of words according to this
distributional hypothesis
[1131] to influence the weights that we fit.
[1133] We do much, much, much better
[1135] at predicting brain responses.
[1138] All right, so we take
this as kind of evidence,
[1141] that, this is the same
correlation map shown in 3-D,
[1145] 'cause it's pretty.
[1147] We take this as evidence that
because these brain areas
[1151] are much better predicted by this model,
[1153] when we include semantic information,
[1156] when we include information
about word meaning
[1158] in that model, this is evidence
[1160] that these brain areas
actually represent something
[1163] about the meaning of these words.
[1165] Or, maybe more broadly,
[1167] that these brain area are
fulfilling some function
[1171] that's related to the
meanings of the words.
[1176] Okay, that's a specific
thing that we can get into
[1178] at some point, whatever.
[1179] So let's briefly go through this question
[1182] of model interpretation.
[1184] So now that we have models that fit well,
[1185] we can ask like, what are
they actually representing?
[1189] What do different voxels
represent in terms of words?
[1192] One thing we can do,
[1193] is we can just pick out one voxel
[1195] and look at the weights for that voxel,
[1196] like which words have high
weight for this voxel,
[1198] and which words have low weight?
[1199] So this is one voxel
from pre-frontal cortex.
[1203] It responds to words like
eight, mile, upwards,
[1206] maximum, nearly, meters.
[1207] It's the M & M voxel.
[1209] It really doesn't respond to words
[1210] like politics, religious,
political, appreciated,
[1212] response, culture, whatever.
[1214] This voxel probably has something
[1216] to do with processing like
spatial relationships, maybe,
[1221] numbers, something like that.
[1223] That seems to be what you can get
[1224] out of this list of numbers,
rather this list of words.
[1227] This is just one voxel out of thousands
[1229] of well-predicted voxels in one subject,
[1232] out of multiple subjects.
[1233] And I don't think I
mentioned that explicitly,
[1235] but we're doing all this
on individual subjects.
[1238] Everything I've shown you is
like is on individual people.
[1241] There's not combining of data so far.
[1244] Okay, so doing this is
laborious and kind of crummy,
[1249] so let's try to just
summarize this information
[1251] in a way that we can understand it easily.
[1254] I'm going to skip some steps here
[1255] and just show you the punchline.
[1258] We use principal components analysis
[1260] to reduce these models down
to just three dimensions.
[1263] We can turn those three
dimensions into a color,
[1265] by turning them into the red,
green, and blue components
[1268] of a color, and then we
can visualize each voxel
[1271] according to this color.
[1273] I was actually going to
take this out of this talk,
[1275] because whatever, I
didn't think I had time,
[1277] but then after Ray's talk this morning,
[1280] I thought it was really interesting.
[1281] So the first principle
component here, more or less,
[1284] it separates what I often call perceptual,
[1288] but what is really spatial
things from social things.
[1291] Like that is the largest
distinction in the brain,
[1293] in terms of like, which
brain areas respond
[1294] to which words.
[1296] It is perceptual or
spatial, versus social.
[1300] Voxels that are green here,
[1302] they really respond more to the like,
[1304] perceptual, spatial things,
[1305] and voxels that are red or pink
[1307] respond more to the social things.
[1309] Sort of crossing that axis, interestingly,
[1311] we have words that are both perceptual
[1313] and social, which is
like words for violence,
[1317] and words for body parts are often
[1319] like one corner of this space.
[1320] And the other corner is words
[1322] that are neither perceptual nor social,
[1324] and that's like time words,
[1327] time and sort of dynamics words,
[1329] which are interesting.
[1332] Anyway, okay, so I don't
want to go into detail here,
[1335] but we see that these brain areas
[1338] that were well-predicted by this model,
[1340] are representing or responding
[1343] to all different kinds of concepts.
[1344] We can use this as a sort of map
[1346] to try to understand what
these brain areas are doing,
[1348] and maybe even more excitingly,
[1350] these maps are really
consistent across subjects.
[1352] So this is three different
subjects, left hemispheres,
[1354] and their 3-D brains up top.
[1356] And we see very similar patterns
[1357] across these different brains.
[1359] Maybe unsurprising, but this
is showing us a lot of detail.
[1361] I'm trying to kind of impress upon you,
[1363] like the level of detail that we can get
[1364] out of these models.
[1366] Okay, but let's ignore sort of,
[1370] what these models are
telling us about selectivity,
[1373] and let's ask, can we do
better than this model?
[1375] Can we do better than this
word distribution model?
[1378] Yes, definitely.
[1379] Definitely we can.
[1380] So one thing that this
model completely ignored
[1384] was context, the context
in which words appear.
[1386] It assumes essentially
the response to each word
[1388] is independent of the other
words around that word.
[1392] And that's wrong.
[1393] That is not factually how language works.
[1398] So with my grad student, Shailee Jain,
[1400] we started working on a way
to try to solve this problem,
[1404] to try to introduce
context into these models.
[1406] And we were really
inspired by a set of papers
[1409] over the last few years,
[1410] where people have used
neural network models
[1415] as a way to try to get
at brain representations.
[1418] So one example that's very nice
[1421] is this paper form Michael Eikenberg.
[1423] They used a neural network
[1425] that was trained to
recognize objects and images.
[1429] This is a multi-layer
neural network model.
[1431] You can pull out
representations from each layer
[1434] of this neural network,
[1435] and then use these as features
[1437] in this Voxelwise and coding model,
[1439] and it turns out that
the lower level features
[1444] from the neural network
predict earlier visual cortex.
[1447] They predict like V1, V2.
[1448] The mid-levels predict like V3, V4,
[1452] and the higher levels
predict like a low V7,
[1455] higher level stuff.
[1457] So actually the hierarchy
of the neural network,
[1459] mapped on to the hierarchy
of visual cortex,
[1462] and we were like, "Ah, that's so cool.
[1463] "That's a cool result."
[1465] There's also this paper
from just last year,
[1468] from Alex Kell and Josh McDermott,
[1470] and a bunch of folks.
[1471] They took a really similar approach.
[1473] They used a neural
network that was trained
[1475] to recognize words in audio,
[1479] and also do a music thing,
which is not important for this,
[1482] but it was a multi-layer neural network,
[1484] and then they tried to
predict voxel responses
[1488] in auditory cortex from the activations
[1491] at different layers of this network,
[1493] and they found a similar kind of pattern.
[1494] So they have like early auditory cortex,
[1496] corresponds to low levels
in this neural network,
[1499] and high auditory cortex
responds to higher levels
[1502] in this neural network.
[1503] Okay, so we're kind of looking
for this kind of pattern.
[1507] But both of these things,
[1510] sort of they're going from
one kind of representation
[1512] to another.
[1513] In this case, you're going
from an image that has pixels
[1516] to like the name of a category.
[1519] In this case, 'we're going from,
[1521] they're going from like
a spectrogram of sound
[1524] to what word that sound corresponded to.
[1528] What is sort of, what
can we do with language,
[1532] with words that might correspond to this?
[1534] So one thing that's become really popular
[1536] in the NLP world in the
last year, two years,
[1540] is that idea of using language models
[1544] to sort of pre-train for
many different tasks.
[1547] So a language model is
just a neural network
[1551] that is trained to predict
the next from previous words.
[1556] You give it a set of words,
[1557] and it gives you a
probability distribution
[1558] over the next word in the sequence.
[1564] We trained a three-layer,
recurrent neural network model,
[1568] a long, short-term memory,
LSTM language model,
[1572] on a big corpus of text,
[1573] to predict the next word
from the previous words,
[1575] and then we used the internal states
[1578] of this language model,
to model the brain.
[1580] Okay, seems like
straightforwardly, vaguely similar
[1583] to what these other folks have done,
[1586] and I think you might hear
about similar things later
[1590] from Layla, and I know Maria
had a really cool paper
[1593] on this last year, and yeah, I don't know.
[1596] So this approach, it's
been getting attraction.
[1599] So one thing that we can vary here also,
[1603] is we can vary the number of words
[1606] that the neural network reads
before it makes a prediction.
[1610] So we can vary the context
length that it has access to
[1614] which gives a nice sort
of know that we can turn
[1617] to try to understand how
important is context,
[1620] 'cause that's sort of our theory here,
[1621] is that we want to add
context into this model,
[1624] so we can ask like how much does it help?
[1626] How much does context actually
affect these representations?
[1630] So that's what we're showing here.
[1631] So this is, now instead of showing you
[1633] a bunch of different flat maps
[1634] with model performance on them,
[1636] I'm just taking essentially the sum
[1638] across the flat map, to
just have one number,
[1641] which is the total variance explained
[1642] by each of these models,
[1643] and that's shown along the y axis here,
[1645] and along the x axis, we
have the context length.
[1648] So how many words the model reads
[1650] before it makes a prediction.
[1652] And well, we're actually
using the prediction,
[1654] but we're using its internal state,
[1656] like what is going on in
this neural network's brain,
[1658] and using it to try to
model our subjects' brains.
[1661] Okay, so the black, dotted line here,
[1664] is the embedding model.
[1665] That's the semantic model
that I showed you earlier,
[1669] and then these three colored lines
[1670] are the three different
layers of our neural network.
[1674] So the first layer, the green one here,
[1677] it doesn't show a really
strong context effect.
[1679] It's actually quite a bit better
[1681] than the embedding model,
[1683] and it improves a little bit with context,
[1685] but doesn't change too much.
[1686] The second layer is this pink line.
[1688] It actually starts off a little worse,
[1690] but then improves a lot more,
[1691] and it actually is our
best performing model here,
[1694] it does really well at
predicting the brain activity.
[1696] Then the third layer is this blue line,
[1698] and it starts off a lot worse,
[1699] and it improves,
[1700] but it doesn't reach the same
level as the other two here,
[1703] which is kind of surprising.
[1705] We're like, "What's going on here?"
[1706] Andrew?
[1707] - [Andrew] What are
the numbers in the box?
[1709] - Sir this is the total
variance explained.
[1711] So we essentially take the
r squared in each voxel,
[1715] and then sum that across the entire brain.
[1718] - [Andrew] The units?
[1719] - The units of essentially
number of voxels variance
[1724] that we've explained.
[1725] So 700 would mean that we've
explained the equivalent
[1729] of 700 voxels worth of variance.
[1732] Yeah, this is really equivalent,
[1734] taking like the mean correlation
across the whole brain.
[1737] They're going to be monotonically related.
[1741] Yeah, so this a control analysis,
[1743] so if we scramble the context,
[1744] if we reorder the words
before the current word,
[1748] then it turns out that that
makes these models worse,
[1750] which is good, 'cause that's
what we should expect.
[1754] Let me show you a comparison
to this on the brain.
[1757] So this is another flat map,
[1759] where the voxels are colored according
[1761] to their performance
with the semantic model
[1763] and the context model.
[1765] So voxels that are
white, are well-predicted
[1767] by both models.
[1768] Voxels that are blue are
much better predicted
[1770] by the semantic, like
word embedding models,
[1772] than the context model.
[1773] And voxels that are red
are much better predicted
[1775] by the context, than the semantic model.
[1777] You'll notice there are
very few blue voxels,
[1780] and quite a few red voxels,
[1781] which means this supports
the thing you saw
[1784] in the previous graph,
[1785] which is that this model
that incorporates context,
[1786] does a much better job at
explaining the brain activity,
[1789] does a much better job at predicting
[1791] how the brain is going
to respond to language,
[1793] than the model that did
not incorporate context.
[1798] We can also ask this question
[1799] about context length and how
that is affecting things.
[1804] So for each voxel, we can compute
[1806] a sort of context length preference index.
[1809] So here, voxels are colored blue
[1811] if they do better with short context,
[1814] if they're better
predicted by short context.
[1817] And you can see an example
of such a voxel here.
[1819] Interestingly, so these
voxels in auditory cortex,
[1823] tend to be much better predicted
[1826] by short context.
[1826] So if you don't include a lot of words,
[1828] that is actually a better model
[1830] for what's happening in this sort
[1832] of higher auditory context areas,
[1835] whereas voxels in a lot of these,
[1838] maybe higher order areas,
[1841] this one's in inferior temporal cortex,
[1843] are much better predicted by long context.
[1848] Okay, so this is kind of interesting.
[1850] This is kind of cool.
[1851] This corroborates other findings
[1853] that we've seen in the field.
[1855] Now let me show the weird finding
[1858] that came out of this that
we still don't really know
[1859] how to explain.
[1860] But let's look at layer preference.
[1862] So remember I told you this model
[1864] had three layers in it.
[1868] We expected to see something
like these other papers
[1870] that saw us for a progression
[1871] from low level to high
level across these layers.
[1874] This is what we see.
[1875] So here the voxels are colored according
[1878] to how well they're predicted
[1880] by these three different layers.
[1882] Voxels that are green,
they're much better predicted
[1884] by layer two than the others.
[1886] Red are much better
predicted by layer one,
[1888] and blue are much better
predicted by layer three.
[1891] And the pattern is, it's
subtle, and it's weird.
[1895] What we actually see is that
[1897] in the sort of higher level areas,
[1899] these areas that liked
the very long context,
[1902] they tend to actually be best predicted
[1904] by maybe layer two and layer one,
[1907] or somewhere in between those two,
[1909] whereas these voxels that are
in maybe lower level areas,
[1912] like auditory cortex,
[1913] are actually better predicted
by layers one and layer three.
[1917] So this doesn't match this thing
[1920] that people had seen in other studies.
[1923] So in these other studies,
they essentially found,
[1925] you take some input, you put it in.
[1926] You have this low-level representation.
[1928] The neural network learns to interpolate
[1930] between that and whatever
task you were training it on.
[1933] You get a high-level representation there,
[1935] and it pulls out these
intermediate representations
[1938] that are useful for explaining
intermediate processing
[1941] in the brain.
[1942] So sort of the neural
networks have learned
[1944] to interpolate between an input
[1946] and whatever the task output is,
[1949] which kind of makes sense.
[1950] It's nice, and it worked really well
[1951] in both of these cases.
[1953] But in our case, that
doesn't really map nicely
[1955] to what's going on.
[1956] So in our case, we have a language model
[1959] where we have an input, comes in.
[1961] It spreads through these different layers,
[1964] but then from the output
of this third layer,
[1968] it's actually trying to
predict the next input.
[1971] It's sort of loopy.
[1972] It's recurrent, but it's
also like the output
[1976] is actually in the same
space as the input.
[1978] You're not mapping from
one kind of representation
[1980] to a different one,
[1981] you're mapping from one representation,
[1983] like back to the same representation.
[1986] And that means that we don't
see this kind of hierarchy.
[1989] We don't see this low-level
to high-level hierarchy,
[1992] across this neural network.
[1993] And I know that Maria and
Layla reported the same thing
[1997] in their paper, and we're
like, "Ah that's great,
[1998] "that's cool that they're
corroborating this,"
[2001] but I don't know how to explain this.
[2002] I don't know like really what it means,
[2003] so if anybody has ideas,
I'd love to hear it.
[2007] This, that's what I just said.
[2009] Okay, so this one way that we've tried
[2013] to improve upon these word embedding,
[2016] through distributional
word embedding models.
[2019] Now let me tell you about a second way.
[2023] It's related to visual grounding.
[2025] So this is work done by my
grad student, Jerry Tang,
[2027] who's here and is giving a
poster on this this afternoon,
[2030] you should check out,
'cause he will tell you
[2032] in more detail, more precisely
what's he's done than I can.
[2035] Okay, so the basic idea...
[2038] Of course many of you are
familiar with the idea
[2040] of visual grounding of language.
[2044] When you hear the word dog,
[2046] you don't just dredge
up sort of associations
[2048] between the word dog and
other words that you've heard.
[2053] Of course this is related also to things
[2055] like pictures of dogs that you've seen.
[2056] This is my dog, she's very sweet.
[2060] So there are a lot of
concepts that we maybe
[2062] learn about visually, and
not just through language.
[2067] So how can we capture
that in these models?
[2069] How can we incorporate
that into these models?
[2072] So what Jerry did was,
[2077] he sort of took a page out
[2079] of this Eickenberg-style analysis.
[2083] What we can do, is we
can take lots of images,
[2086] images from Imagenet,
[2087] map them through some neural network
[2090] that was trained to
recognize objects and images,
[2093] pull out a representation
from that neural network,
[2095] that we think we know
actually from other studies,
[2100] is representative is how visual cortex,
[2103] at some intermediate to high level
[2106] represents these images,
[2108] and then look at similarities
of these representations,
[2112] rather than similarities of
sort of distribution properties
[2115] of the words.
[2117] So essentially each word gets mapped
[2120] to a collection of images.
[2121] Each collection of images gets pushed
[2123] through this neural network,
[2124] and then evaluate the similarity
[2126] between different words,
[2127] based on sort of how similar
the related images are.
[2131] So this gives us a measure of similarity
[2133] derived from visual properties
[2135] instead of from
word-distributional properties.
[2141] But of course this is only,
[2144] this is not really naturally a model
[2146] for how we learn about
things in their totality.
[2149] We do learn about things using both words,
[2152] and sort of visual input,
[2153] as well as other modalities.
[2156] So what we actually end up using
[2157] is a combination of these two.
[2159] So we will more or less
concatenate these two sets
[2162] of features, we get
distributional features
[2164] for each word, and these
visual features for each word,
[2166] and then combine them into
[2167] this visually grounded semantics base.
[2170] So let me show an example
of what this looks like
[2172] and maybe give you a little bit intuition.
[2174] So this is a bunch of words,
[2179] projected into just a
two-dimensional space.
[2183] This is, I've taken these embeddings
[2185] and mashed them down into two dimensions
[2187] using principle of components analysis,
[2189] and what we're showing here
is two different categories,
[2193] that I think have some kind
of intuitive relationship
[2195] to what's going on in these spaces,
[2197] so we can explain what's going on.
[2198] So, the sort of blue-green words here,
[2202] they're words for people.
[2203] And I'm sorry, I'm starting off here
[2205] with the distributional space.
[2206] So this is based on how
these words are used
[2209] in written text in general.
[2212] The green words, blue-green words here
[2214] are words for people.
[2216] So even though all these
people may be look very similar
[2220] to each other, they're pretty
far apart in this space,
[2223] because they occur in
quite different contexts.
[2225] You don't use the word boy and engineer
[2230] that often, like those are not replaceable
[2233] with each other in general.
[2236] So they are quite far apart in this space.
[2239] In pink is words for items of clothing.
[2244] And it turns out that these things,
[2247] we talk about them often pretty similarly.
[2249] They're used in similar ways,
[2252] even though they look very different.
[2255] In contrast, the people
who look pretty similar,
[2258] like a person is a person.
[2261] An engineer and a doctor probably look
[2264] much more similar to each other,
[2265] than like, I don't know,
a doctor and a shoe.
[2268] But yeah.
[2270] So all the clothing items
are kind of packed together
[2273] in this one little lump right here,
[2275] while the people are really spread out
[2276] in this distributional space.
[2279] But now if we interpolate from here
[2281] through the grounded
space where everything is
[2284] a little more complicated,
[2285] out to our purely visual space,
[2287] so now the similarities here
[2289] are just based on how visually similar
[2290] each pair of words are,
[2292] and now we have all these,
[2294] all the people are kind
of more packed together
[2296] in one corner of the space,
[2297] because people are people,
[2298] whereas the clothing items
[2300] are much more spread out.
[2302] So this is just to sort of illustrates
[2304] what the difference is
[2305] between our visually grounded space
[2307] and our distributional space.
[2310] Okay.
[2311] This is the same thing,
[2312] I'm just showing both at the same time.
[2315] Okay, so now we have two different priors.
[2317] We have visually grounded prior
[2321] that says that words should
have similar representations,
[2324] if they correspond to
things that look similar,
[2329] and we have the distributional prior,
[2330] which is that words should
have similar representations
[2333] in the brain if they correspond to things
[2335] that are, often occur in the
same context in language,
[2339] and we can compare these two.
[2340] Right, we can fit modes with each one,
[2342] and we can ask which model predicts better
[2345] in each part of the brain.
[2347] So this is showing a
flat map for one subject
[2350] with a similar kind of color map
[2352] to what I showed before.
[2354] Here black voxels are poorly
predicted by both models.
[2359] White voxels are well predicted by both.
[2361] Red voxels are better predicted
[2363] by the visually grounded model,
[2365] and blue voxels are better predicted
[2367] by the distributional model.
[2369] We can see that this is more mixed
[2371] than the other picture.
[2373] So it's not like the
visually grounded model
[2375] is better for everything.
[2378] But what we see is that
actually in the places
[2380] that are close to visual cortex,
[2382] so especially in these
areas that are near the edge
[2385] of visual cortex,
[2386] we have glomerations of these voxels
[2388] that are better predicted
[2389] by the visually grounded model,
[2391] than by the distributional model,
[2393] whereas in pre-frontal cortex,
[2395] we some of those as well,
[2396] and this actually lines up with places,
[2397] you know voxels that are selective,
[2399] for kind of visual concept,
[2400] but we see a lot of voxels here
[2402] that are better predicted by
the distributional features
[2405] than the visual features.
[2410] Right, and this especially true
[2411] close to these sort of known visual areas.
[2414] This is the parahippocampal place area,
[2415] extrastriate body area, and
retrosplenial complex, cortex.
[2420] This is just showing a bar graph
[2422] that is like average
across a couple subjects
[2425] of the model performance,
[2427] near each of these ROI's.
[2429] This is not in HRY, but this is for voxels
[2432] that are near each of these known ROI's.
[2434] So for the visual ROI's,
[2436] we tend to see improvement
[2437] of the visually grounded model
[2438] over the distributional model,
[2440] whereas in these other ROI's
[2442] that are language-selective things,
[2445] but not visual, this is SPMV's,
[2448] this is sort of frontal
language area and Broca's area,
[2450] is here.
[2452] We don't see that same distinction.
[2453] We see actually maybe a weak preference
[2456] for the distributional model.
[2458] Okay, so Jerry can tell
you more about this,
[2461] and there's more analysis
to be done with this,
[2463] which are pretty cool,
[2464] that like relating words
that are very concrete
[2469] to nearby, they're closest
neighbor who is abstract
[2475] in how those things are represented,
[2476] which is pretty exciting.
[2480] But yeah, so we're left
with some questions
[2483] from this too, especially this last thing,
[2485] so can we also do this
grounding other modalities,
[2490] can we ground in like tactile features?
[2492] What would that look like?
[2493] Can we extract tactile features
[2495] from words that seems tricker.
[2497] We don't have good
techniques for doing this.
[2498] But, they're things.
[2502] And also how can we combine this approach
[2506] with context models, 'cause I think
[2508] that would be a nice merger
of these two different streams
[2512] of research.
[2514] So that's it.
[2516] I want to end by thanking
all the people involved here,
[2519] especially Shailee and Jerry,
[2521] and Wendy de Heer and Anawar Nunez,
[2524] and Jack Gallant's lab.
[2525] Thank you.
[2526] (audience applauds)
[2527] - Thank you very much.
[2532] It looks like you have a
question, Jim, or a comment.
[2536] (laughs)
[2538] - So beautiful work.
[2540] I really liked the
context model, especially.
[2545] But the thing that always,
[2548] the question that I always come up with
[2549] when I see these kinds of models,
[2552] based on lexical units, words,
[2554] when they're listening to a story,
[2557] is what about the discourse level?
[2559] It's not, and the contextual model,
[2563] using the recurrent, is a
recurrent neural network,
[2567] still doesn't get at,
they're hearing a story,
[2571] and there are...
[2573] People come back, scenes come back.
[2576] Episodes are referred to again.
[2578] There's all this discourse information,
[2581] which is just what the
people are really listening,
[2584] representing, and I
suspect you're thinking
[2589] about this too, and trying to think
[2592] of how can you incorporate representation
[2594] of semantic information
[2598] that exists at the
discourse narrative level,
[2602] rather than at the single word level,
[2604] and what I just, what are
your thoughts about this?
[2606] - Well so, absolutely I
think this is of course,
[2611] what we're trying to work toward,
[2612] that's what we want to
understand in a way,
[2615] is how these higher level, larger concepts
[2619] that are communicated by sentences
[2620] or whole stories, are represented
[2623] and what's actually going on there.
[2626] For one, we just don't have
mathematical models of this,
[2629] like we don't have a
way to extract features
[2632] that capture sort of
discourse-level elements.
[2639] Maybe the best we can do right now,
[2640] is we can use these same
kinds of language models,
[2644] like the context model here,
[2646] but with very long context lengths.
[2648] So we've been experimenting
with this recently,
[2651] going out to more than 100 words,
[2654] which is not discourse,
whole discourse level,
[2657] but it's better than 20
words that we had here.
[2661] Interestingly what we found there,
[2663] is that this is super preliminary,
[2669] that the amount of data that
we're training the models on,
[2672] starts to really matter,
[2674] so the data that I
showed you, let's see...
[2680] Wait.
[2753] - You started us off talking
about the recapitulation
[2756] of stuff Ray was showing us
with space versus social words.
[2763] And then ended on the context
[2767] versus visual models, so I was wondering
[2770] if you have thought about
creating a similarity space prior,
[2776] based on sociality or
something of with the words.
[2782] - Yeah, that's interesting.
[2783] No, we haven't really thought about that.
[2787] Yeah, how would that work?
[2789] Yeah, we'd get like--
[2791] - You can do some polling.
[2797] Just get people to make judgements,
[2800] along different social
dimensions I suppose.
[2805] - [Alex] Yeah, that can
be really interesting.
[2808] - Some other kind of--
[2808] - Grounding and social
interaction like that would be--
[2811] - [Andy] Some like that.
[2812] - Yeah, interesting.
[2814] - Yes sir, one thing I like about this,
[2817] and there's and as a
comment and a questions, is,
[2819] that it's a way of comparing among
[2821] these word-embedding spaces,
[2823] is because you have
this external referent,
[2824] which is the brain, and you can say,
[2825] "Okay, which is, predicts
brain activity better?"
[2828] Essentially across the brain.
[2831] My question is when it
comes to the second part,
[2835] which is sort of interpreting
those dimensional spaces
[2837] and what goes with what,
[2838] aren't you getting out
kind of what you put in?
[2841] Because you're constraining the estimates
[2844] and the model to be similar,
[2846] based on these prior covariance matrices,
[2848] so you kind of have to see that
[2850] when you look at the
representations coming out, right?
[2853] - Yes, in a way, absolutely.
[2855] Like we are imposing semantic
smoothness on the word space
[2861] in the sense that...
[2862] If we go back to the early stages here,
[2868] yeah, so, when we fit this model,
[2872] the weights for month and week
[2874] actually cannot be that different.
[2876] They can't, one can't be
positive and the other negative.
[2878] Like, that's just
impossible under this model.
[2881] Of course this does sort of smooth things
[2884] and bring them down into essentially
[2886] some lower dimensional space
[2888] than the total dimensionality
of the set of words,
[2890] but so we tried, in doing this sort
[2894] of principal components analysis,
[2896] which, let me skip forward to that one.
[2901] In getting to this point,
[2904] we did do a test for exactly that issue,
[2907] which was we can ask about the...
[2912] We can do the same principal
components analysis
[2913] on the stimuli themselves,
so on the stories,
[2917] which should have all of that
same semantic smoothness,
[2919] all of that same built-in, sort of junk,
[2922] that is being pushed through
into the final models, here.
[2926] And then we compared how
much variance was explained
[2928] in the brain models,
[2929] from the principal components
of the stimuli themselves,
[2934] versus the principal
components of the brain data.
[2937] And it turns out that these
first three dimensions here,
[2939] explain significantly more variance
[2942] than the corresponding
pieces of the stimuli,
[2946] which we took as evidence that like,
[2947] these are dimension that are actually,
[2949] there is effect of the
feature space itself,
[2953] sort of buried in here,
[2955] but the fact that like this
is the first dimension,
[2958] is not something that you would get
[2959] from just the stimulus itself.
[2962] - [Tor] And just to quickly follow up,
[2963] but what about hand-coding
those categories,
[2965] like in some of your earlier papers?
[2967] Have you left that behind now,
[2968] or you think that's
still maybe even better.
[2972] - Hand-coding things is like the worst.
[2974] It really (all laugh)...
[2975] I spent, I don't know,
[2977] two months as a second-year grad student,
[2979] like hand-labeling images,
[2981] which was totally worth it.
[2982] It was great, but I just don't...
[2984] I like really don't want to do that again.
[2986] (audience laughs)
[2988] Yeah, so I mean, I really like to rely
[2991] on these sort of stimulus
computable models,
[2994] like something where we define a function
[2995] that you can apply to a stimulus,
[2997] and that gives you a set of numbers,
[3001] which also makes it practical to move
[3003] to these very large data
sets like we're doing now.
[3005] Like I hand coded two hours of video,
[3008] but I can't even imagine doing that
[3009] for like 20 hours of
video, which is whatever,
[3011] 20 hours of stimuli like we have now
[3013] for these subjects which
is, would be nightmarish.
[3016] So yeah.
[3017] - I had a couple of I guess,
semi-technical questions.
[3020] And maybe this is because
I don't know the full range
[3022] of your work as well as you do,
which is why I'm asking you.
[3025] Maybe it's laziness, but to what extent
[3027] does the choice of word embedding matter?
[3030] Okay, if you looked at a
bunch of different options,
[3033] and in sort of a similar vein,
[3035] if you just code words by their identity,
[3038] like have a one hot matrix of words,
[3041] how much do you get on top of that
[3042] from having, let's say GloVe embeddings
[3045] or even transformed or create embeddings.
[3048] - Yeah, so this is essentially
the identity model.
[3052] This is like a one hot word embedding,
[3054] where each word is just
an independent vector.
[3057] That was there when the old model
[3058] here that I'm comparing to.
[3059] So that is a lot worse than
these word embeddings, but--
[3063] - Well, is an embedding
the same as just one hot?
[3067] I think that they'll behave
completely differently,
[3070] if you have a vector embedding that's got
[3072] a bunch of real numbers versus something
[3072] that's just like, you know, small.
[3076] - I thought that, that was
your second question, though,
[3078] is like how does this compare
to an identity embedding,
[3080] or identity...
[3081] - [Adina] Okay, yes.
- Yeah.
[3083] Yeah, so I think this is exactly that.
[3086] This is the identity,
[3090] yeah, matrix, as a word embedding.
[3092] We've compared a bunch of
different word embeddings.
[3094] This was actually a road
that I started to go down
[3096] when I started my own lab, which was like,
[3098] "Ah, let's use this
method to actually like,
[3100] "compare embeddings,
[3101] "and we can do something cool with that."
[3103] It turns out, most things
work really similarly,
[3105] like really similarly.
[3107] In fact, even the dimensionality
doesn't matter too much.
[3110] You can squeeze things down
[3111] to in, maybe like 100 dimensions,
[3114] and it still works pretty
okay, with GloVe embeddings.
[3119] Yeah, and in terms of sort of
what the representations are,
[3122] that doesn't change too much either.
[3124] Like all of that is kind of the same.
[3126] That's true for like all these
modern embeddings actually,
[3129] so for Word2Vec, for GloVe,
[3134] for the embedding method that I use here,
[3136] which is some ad hoc thing,
[3140] which is actually very
similar to the embedding
[3142] that Marcel and Tom Mitchell used
[3145] in their 2008 paper,
[3147] which was a whatever,
small embedding as well,
[3154] these all seem to work pretty similarly,
[3156] and they work much better
[3157] than the sort of old-school embeddings,
[3159] so like LSA or HAL,
[3162] those don't work nearly as well.
[3164] So there is a big step from,
[3165] like the sort of simple embeddings
[3167] to these modern embeddings, I don't know.
[3170] I don't...
[3172] I could say more technical
things, but yeah.
[3175] Yeah, in general, like
they're pretty similar.
[3181] - Yeah I had one sort of
clarification question,
[3186] and another sort of speculative comment.
[3190] But the recurrent neural network model
[3193] that you used for context,
[3195] I just want to clarify the amount,
[3199] the kind of gear of how far
back in time it considers,
[3204] and the layers are two independent,
[3205] sort of like architectural choices,
[3207] like the fact that it has three layers,
[3210] but for example, does that middle layer
[3213] behave differently in any way,
[3216] depending on how far back...
[3219] - [Alex] Well let me pull that over here--
[3220] - I mean so what I'm wondering is,
[3222] it sort of strikes me as
almost each time point,
[3226] is almost like auto encoder,
[3228] but the next stage,
[3230] but it's not the input
word, it's the next word.
[3232] And so that's why it seems to me like
[3235] that middle layer would
be the important one
[3237] in the same way that it
is in the auto encoder,
[3239] because you're essentially going
[3240] from a word to an intermediate
representation to a word.
[3243] Is that sensible?
[3244] - So the middle layer,
[3248] the input to the middle layer
[3248] is already an intermediate representation.
[3250] So the word comes into the bottom layer.
[3253] The word actually there was an embedding,
[3254] and then the word goes
into the bottom layer,
[3255] and then the bottom layer
goes into the middle layer.
[3257] The middle layers goes into the top layer.
[3258] The top layer goes into like
an output embedding space,
[3260] and then outputs from there.
[3265] Honestly, this whole like issue,
[3267] made me so deeply question the idea
[3269] of like layers in
recurrent neural networks,
[3272] which when you think about it deeply,
[3273] it's like what, what?
[3275] Why is this a good idea?
[3277] It turns out with one layer
in recurrent neural network,
[3280] you can compute exactly the same things
[3282] that you can compute with multiple layers.
[3284] It's just a matter of like
[3285] how you connect the units together,
[3286] which we wrote a paper
about, that whatever.
[3289] We went down like a sort of
weird, diverted path there
[3292] of like what the hell do layers mean?
[3295] In like feed forward neural networks,
[3297] it's like very simple.
[3298] It's like this layer
feeds into that layer,
[3300] but in recurrent network,
[3301] each layer gets its own
inputs from the past,
[3304] and from the previous layer.
[3305] So it's...
- [Sam] So it's a little more.
[3307] - It's messier.
[3308] - Yeah, I only have worked
with recurrent neural nets
[3309] that have one layer, right,
[3311] and I don't know how to
interpret it otherwise,
[3313] but yeah okay.
[3314] - Yeah, I mean stacked recurrent nets
[3316] have become like really common in LP land.
[3321] It turns out it's just
a method of regularizing
[3325] what is essentially a
single-layer recurrent net,
[3329] but yeah, and so I don't
there's anything necessarily,
[3333] like that makes it architecturally obvious
[3335] that this middle layer should
be the best in some way.
[3339] The like vague idea I have in my head,
[3341] is something that like...
[3345] Come on.
[3347] That, you know, because the
output has to kind of be
[3352] aligned with the next input,
[3357] this layer is kind of the freest, in a way
[3359] to represent things in a way
[3361] that doesn't need to be
trivially mapped from the input,
[3364] and it doesn't need to be trivially mapped
[3365] to the word embeddings.
[3368] So it can have this, some kind of weird,
[3370] high-level representation.
[3371] That might be why it works so well.
[3374] But yeah.
[3375] - I'll save my second one for...
[3380] - So I just have a question about,
[3384] did I think is inherited
both with a semantic
[3387] and a context model to
mention how your building
[3392] two similarities in meanings of words,
[3395] and I'm just curious about what happens
[3397] with common errors and
similarities and meanings
[3400] and whether that's
something that is public,
[3403] the model is oblivious to it.
[3404] It can't discern, so it might be one
[3407] of just annoying philosophy questions,
[3409] to what extent is this
really semantic knowledge,
[3413] rather than just beliefs
about the meanings
[3416] that the agents actually have,
[3418] but if you take like those
common speaker errors,
[3421] that might be prevalent
across the community,
[3425] but are still not really
tracking the meaning,
[3427] how does that, is that
something that just gets...
[3431] The model is just going to be blind on?
[3434] - That's a good question.
[3435] I never looked at that.
[3437] That's really fun.
[3438] Like...
[3439] - Like for instance, factoid,
[3441] people oftentimes think that
doesn't have to be false--
[3444] - [Alex] But that is what factoid means.
[3446] - It's not fact, yeah.
[3446] - Yeah, or like using "begs the question"
[3450] - [Una] Exactly, yeah.
[3451] - to mean like raises the question.
[3452] - [Una] Right.
[3453] - I'm sure there are some subjects
[3454] where you just get like an anger response
[3455] somewhere in the brain where that happens.
[3458] Yeah, we haven't looked at this.
[3462] I suspect, so whatever these models
[3466] sort of say the representation is,
[3468] is kind of what...
[3472] It's based on how that
word is used on average
[3475] in the corpus that we put in.
[3476] So if factoid is used mostly
to mean like small fact.
[3481] - [Una] Right, that's
what I would guess, yes.
[3482] - False fact, which it
almost certainly is,
[3484] then that's what the model would...
[3486] - Right, and so you wouldn't get something
[3488] that's meaning, but something's that like
[3489] belief about meaning,
[3490] and you can also get this
with accidental correlations
[3493] in say phonological similarities.
[3496] Or words that sound the same,
[3497] you might assuming the same, but don't.
[3500] I say those would also be interesting to--
[3502] - Yeah so we have compared
[3503] to phonological similarity measures.
[3508] And that predicts a
very specific brain area
[3511] that is essentially just
the superior temporal gyrus
[3513] and that's it.
[3515] Yeah, so at least that...
[3518] It can be decorrelated to some extent.
[3521] - I wonder if you thought
about the ways in which,
[3526] your conclusions and your big picture
[3528] are dependent on the fact
that you're explaining
[3531] neural responses to Moth stories.
[3535] There is more to, there are
other kinds of concepts,
[3539] other kinds of discourse.
[3542] Imagine a political science lecture.
[3545] It's going to have much less, I think,
[3547] visual content.
[3552] And each kind of domain of discourse
[3555] of language, of conceptual space
[3558] has its own kind of characteristics,
[3562] and you're obviously exploring
the semantic characteristics
[3567] of this space.
[3569] And oh by the way, Jim's
very interesting suggestion
[3571] about event structure,
[3573] is an element of, a possibly
very important element
[3580] of story of Moth story of--
[3583] - Because they are narrative stories.
[3584] Right they have events,
[3585] whereas a lecture about
something does not.
[3588] So we've been exploring this lately,
[3591] so like I mentioned, we have data
[3592] for at least one subject now,
[3594] of up to 20 hours of stimuli
for that one subject.
[3598] This is not all Moth stories.
[3599] It's about half Moth stories,
[3601] but we're also, we trying to,
[3603] we build a little sort of factorial matrix
[3605] of the different kinds of stimuli
[3606] that we wanted to explore.
[3608] It's like narrative versus factual,
[3610] written versus sort of
spoken off the cuff,
[3613] and single speaker versus multi speaker.
[3616] So we're raising like
stories from the Atlantic,
[3619] as a sort of more factual version of this.
[3621] Turns out these models work extremely well
[3623] for those also.
[3625] - No new dimensions, no new elements.
[3627] - We haven't explored
that in enough detail yet,
[3629] so I definitely can't say that.
[3631] I don't know.
[3634] But that definitely
doesn't have the same kind
[3635] of event structure, and still,
[3636] at least like the basic
word embedding model
[3638] still works really well for that data.
[3640] And actually building
a model on like stories
[3643] from the Atlantic and then testing it
[3644] on Moth stories, still works very well.
[3647] So there's something that
is sort of core there,
[3650] to just like the meanings of these words
[3652] and the semantic
dimensions that they span.
[3654] - Do you think it would work
[3656] if you developed an embedding model
[3659] based on Atlantic stories?
[3661] - Haven't tried that yet.
[3663] That'd be interesting.
[3664] - [Man In Background] I
think I would let you--
