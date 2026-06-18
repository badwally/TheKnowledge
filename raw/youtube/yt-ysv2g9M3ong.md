---
schema_version: 1
id: yt-ysv2g9M3ong
type: youtube
title: The quest to create engineer-quality models of the mechanisms of human visual
  object recognition Pt2
url: https://www.youtube.com/watch?v=ysv2g9M3ong
authors:
- MITCBMM
ingested_at: '2026-05-30T20:01:58Z'
content_hash: sha256:0a953151551e45c31634f81a044cb4d5d35db8e014529416d760d15056254370
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: MITCBMM
  channel_url: https://www.youtube.com/@MITCBMM
  duration_seconds: 3023
  caption_track: fetched
  snippet_count: 1334
filter:
  score: 0.75
---
[0] JIM DICARLO: This lecture I
give, I usually give before.
[2] But you've already
heard about kind
[3] of how certain deep
networks are aligned
[7] with the ventral stream.
[8] So that's what this
collaborative breakthrough
[9] is about.
[9] So I'm just going to
just breeze through that
[12] and give you kind of
my view on how I think
[14] about that and those results.
[16] This is what I mean by this
collaborative breakthrough.
[18] So remember, I set
this up by saying,
[20] we need encoding models that
could align with neurons.
[22] Whatever level of IT
they're recorded from,
[24] whether they're layer 2,
3, layer 4, or layer 6,
[27] as I just said, we'd
like models that
[29] could explain their responses
and they were not explained.
[32] This is sort of a
median explained
[34] level of response of neurons on
the x-axis or the y-axis here.
[38] So we'd like these
bars to be higher.
[40] And what the collaborative
breakthrough was about
[43] is that we found
models that started
[45] to be much higher than any of
these original models here.
[48] And the context for that is
when you think about the models
[51] that I showed you so far,
the way I think about it
[53] is that these are complicated
deep nonlinear models,
[57] and there's a lot of
parameters in them
[60] that you either pick by
intuition or some other way,
[63] that are not the neuroscience
experiments like the kinds I
[67] showed you.
[68] They don't tell you how to
set a synaptic weight, say,
[71] between V4 and IT, or
even between V1 and V2.
[74] Those are parameters
of these models that
[77] are not easy to tune based
on neuroscience experiments
[81] of the type that I've been--
[82] I showed you some of our
data, but similar experiments
[84] that I think you
had reviewed for you
[86] over the last couple of days.
[87] So that was the fundamental
lurking problem here,
[90] of these models, or at least
that's how I think about it.
[93] And the way that problem
was gotten around--
[95] I mean, it's not
fully gotten around,
[96] but the way progress has
been made on that problem--
[99] is to shift the
goal of the models
[102] to include another
problem, which
[104] is the problem of
actually solving the task.
[107] And then allow the optimization
of those models to tune
[110] some of those unknown parameters
in a way that just best does
[114] the task.
[115] And it then turns out that
that-- those models are better
[118] aligned with the neural
data than the prior models.
[122] That's a summary of
the breakthrough.
[123] So this is Dan
Yamins and Ha Hong,
[125] and they were people
who were very involved
[127] in this work in
my group when this
[129] was happening in 2013 and 14
or so, and these papers here.
[134] Dan is a professor at
Stanford, at the moment.
[139] And so here is kind of
the big picture again.
[141] You have a deep
convolutional neural network.
[145] This is not out of the blue.
[147] Remember Fukushima?
[148] HMAX?
[149] Those are also deep
convolutional neural networks.
[152] This was basically
textbook neurobiology
[154] of the ventral stream under
a feed forward assumption
[158] that this is what the
ventral stream does.
[160] So this was not a kind
of out of the blue idea.
[163] And so neuroscience,
in some sense,
[164] had already been framing this
as the right family models
[168] to be exploring,
as I showed you,
[170] others were already
exploring that theme.
[173] Then we'd already thought
the ventral streams involved
[175] in things like recognition.
[176] Like, you want to say this is
a pair of boots, regardless
[179] of its position or scale.
[181] And that's core
object recognition
[182] if you think of it as
a cognitive science
[184] kind of framing of what is
the brain solv-- what kind
[186] of behaviors is the brain doing?
[188] And I gave you outline
at the beginning.
[190] But what then happened is that
you needed ways to-- again,
[193] I just alluded to--
[194] to optimize a lot of the unknown
parameters of this network,
[199] the sort of micro scale
architecture, if you will--
[201] synaptic connections,
for example--
[204] in some way to
perform this task.
[206] And this is where various
engineering optimization
[208] tools came in to help us.
[210] And the most prominent
of those, of course,
[213] is called deep learning,
which you've heard about,
[216] which just propagates the
error backwards to tune
[218] the micro parameters
and synaptic weights
[220] within the architectural
family to do good at the task
[223] by a loss function that's
defined relative to the task.
[227] And that is one way to
tune the parameters.
[229] There are other ways
to tune the parameters,
[231] but are basically-- amount
to different optimization
[233] strategies to achieve the task
within some set of parameters
[236] here.
[237] And all of the
work that was done
[239] was essentially optimization
on the [INAUDIBLE] models
[242] for this kind of set of tasks.
[244] And the breakthrough
was essentially--
[246] the way I think about this--
[248] the way I think about this
from a kind of a science
[250] point of view is each time
you build one of these models,
[253] you complete an optimization.
[255] You just state, that is
a model of the system.
[257] You're not claiming
that that's a learning
[259] mechanism of the brain--
at least I'm not.
[261] You're stating it
as a hypothesis
[263] of the mechanisms that are
in play in the adult organism
[267] when it walks into the lab.
[268] And how you get there
is a separate issue.
[271] That's an issue where they
have to learn via development.
[273] But here we just think of
it as producing an emulation
[276] model of the
system, and checking
[278] the ability of that model to
align with the neural data.
[281] And so the way I
think about this
[282] is each choice of the parameters
at the end of a learning
[285] run or an optimization run, if
you will, for deep learning,
[288] is a statement, a hypothesis.
[292] It's locked in at
that point, so this
[293] is a hypothesis of how the
visual system processes
[296] visual images.
[297] No more learning.
[297] It's all just frozen and then
you check it against the data.
[300] So each choice of parameters
is an entirely new
[302] artificial ventral stream.
[304] And then the breakthrough if
you will, or the discovery,
[306] in science language, is
that the individual neurons,
[309] the artificial neurons
inside some of these models--
[312] not all of them,
but some of them--
[314] they behave, functionally
behave very much
[316] like the individual neurons
in the monkey brain.
[319] Behave both individually,
and certainly
[321] in linear combinations
like the neurons
[323] that I showed you earlier
recorded out of IT, or V4,
[326] or others later showed
some other areas as well.
[329] And so that's the big picture
that you've already heard.
[331] I hope that's sort of
my context on that.
[333] And what's to me, most exciting,
is that we're now in a regime
[337] which I mentioned way back
at the beginning of the talk,
[339] where people are building
detailed, engineered
[341] descriptions that are
scientific hypotheses.
[344] Their hypotheses, so
they're all wrong.
[346] They're all models.
[347] They're all wrong, but they're
all better than the models
[350] that we had before.
[351] And this is an example
of one at the top.
[354] And here's the brain that I've
been showing at the bottom.
[357] And we're now in
a world where we
[359] can start to compare at both
the individual neuron level,
[362] whether it's in IT,
or V4, or V2, or V1,
[365] and the behavioral
level simultaneously.
[368] Models are being asked
to explain all of this
[370] simultaneously.
[371] And so remember
back when I said,
[373] at the beginning of the
talk, multi-scale models that
[375] could explain, for instance,
what's going on in V1
[377] and also explain what's
happening in behavior.
[379] And we want models that
can do all of that,
[381] and that is now
what's being produced.
[383] And this is an example of a feed
forward only model at the top.
[387] I'm not saying that's
the right model,
[388] but it's an example of
a feed forward model.
[390] And the way-- I just
want to remind you--
[392] the way we make these
comparisons is first of all,
[394] it's not just hit IT,
it's all of the data.
[397] But the way we make a
comparison stay within IT
[400] is for any recorded
neuron in IT,
[403] we look for an in
silico artificial neuron
[405] or a linear combination
of neurons whose responses
[408] are similar to that IT neuron.
[410] And then we check
it on how well it
[413] predicts that IT neuron's
biological response
[416] on held out images.
[417] And that's the measure
that we use that we
[419] call explained variance.
[421] We do that for a bag of neurons,
then we get an average score,
[424] and that kind of gives
us a score for IT,
[426] give you that for V4 and V2.
[427] Those are the kind
of things you've
[429] been hearing from
others, and we've
[430] packaged that in
a platform called
[432] Brain Score, trying to be
a thing for the community.
[436] Because it's not just our
lab producing those data,
[439] it's many labs
producing data that
[440] need to be explained by
these kinds of models.
[443] And the upshot of all this, and
the breakthrough if you will,
[445] is that the models
suddenly started
[446] to predict the data much
better than they were before.
[448] Here you can see the
red line lining up
[450] much better with the black
line than the prior data I
[453] showed you.
[454] We don't have to call this
neuron and chair anymore.
[456] We can call it
neuron of type 12,
[460] or some number we can give it.
[461] But it's something that is much
better aligned with the data.
[464] Here it's not a
face neuron, it's
[466] something that can predict
the face neuron quite well.
[469] It aligns with-- the
artificial neuron is aligned
[471] with the biological neuron.
[474] And the one big picture
context to all of that--
[476] which I think you've heard that
before, so I'm going quickly--
[479] is that we had noticed--
[481] and this was sort of
backdrop to the work--
[483] that models, each dot here is
a full ventral stream model.
[486] So it's a full
ventral stream model
[487] and this is explained
variance on the y-axis.
[490] This is an accuracy.
[491] This is an accuracy on ImageNet
challenge and computer vision
[494] challenge on the x-axis.
[495] And we noticed that--
[498] actually, this is an image
that was a related challenge,
[501] but it's a core
recognition challenge.
[503] But we noticed that models
that were good at these tasks
[507] tended to align
better internally
[509] with the neural data, which
is, again, on the y-axis.
[512] So if you do good
on the x-axis, you
[514] tend to be good on the y-axis.
[515] And the breakthrough
was essentially
[517] that better optimization
tools created better models
[520] on these tasks, which resulted
in models like this one
[523] that we talked about 2013
or so, which was much better
[527] at explaining the
neuroscience data
[528] examples I just showed you.
[530] I'm giving you this
by way of context
[531] to say optimization within
architectural framework
[535] is a virtuous cycle that then
leads to models that are better
[538] explaining the mental data.
[539] Now that begs the--
and you've probably all
[541] heard this story before.
[542] I hope that you've heard
this, just my perspective.
[544] But I hope that you can also
realize you could say, well,
[547] couldn't we just keep
engineering better and better
[548] models, and will they naturally
explain the brain right?
[551] And if you think that,
at some point, you guys,
[553] it can't be true that you
can just do this forever.
[555] And in fact, we've already
seen that you can't just
[557] optimize for tasks and assume
that this will keep going up.
[560] It just so happened
that there was
[562] a time where we were
in a regime where
[563] it did work, to some degree.
[565] And now we need other changes
to make even better alignments
[567] with the brain.
[569] OK.
[570] So the big picture
summary of all of this
[571] is you kind of had
an, I think of it
[573] as an implicit collaboration
between scientists,
[576] labs like myself and
others, and engineers
[578] who are good at optimization
around specific assemblies
[582] of neural network mechanisms.
[584] And that then creates
hypotheses for brain science.
[588] Again, some of them are
more correct than others,
[590] and we can check their
goodness as well.
[592] And I've been telling
you this story in vision,
[594] but others have been taking
this same approach, not
[596] just in vision, but other areas
like audition, somatosensation,
[599] decision making, motor planning
and control, navigation.
[601] It's is the same general idea--
[603] optimize neural networks
within a task space
[605] and then check against
the neural data, and then
[607] [? flows ?] us through--
update the models
[609] based on the deviations from
the neural and behavioral data,
[612] and then update the models.
[613] And really, that's
just good science
[615] with engineering as a tool.
[617] OK.
[617] So then I want to
point out, though,
[619] for those of you who say, well,
look, what's the point of this?
[621] What's the point of
understanding the brain?
[623] It also has AI payoffs.
[624] And you might know that sort
of as deep learning kind of
[626] came on the scene right
around the ImageNet challenge,
[629] around 2012, it is
not a coincidence
[631] that they point out that
these models actually
[634] had their architecture based
in ventral stream architecture.
[637] But inspired by theories of how
the brain recognizes patterns
[640] as one of the sort
of founding building
[641] blocks of these models.
[643] And again, that again had been
already around for a while
[645] and then it kind of took
over a lot of so-called AI.
[648] Not just deep
inference, but deep
[650] learning, broadly, for
other application problems,
[653] as you know.
[654] So now I want to turn back
to the ongoing science.
[658] So this is not the
end of the road,
[660] it's an interesting
intersection,
[661] but what's going on next?
[663] So a big picture summary
that you should take--
[665] and again, this is
all background, now--
[667] is that particular ANNs--
not any ANN, but some ANNs--
[671] optimized in particular ways
can now reasonably, accurately
[674] explain and predict.
[677] It can explain the
detailed workings
[679] along the ventral stream
and predict the workings
[681] in the ventral stream
at the single neuron
[683] level, and the behavior level,
and the population of neuron
[685] level.
[686] Not perfectly, which
is why this glass is
[688] half full and not fully full.
[690] If it was perfect, I would
draw this as full full.
[693] But far better than
it could before,
[695] and we can quantify that,
and we have quantified that.
[698] But we can also see that no
way ANN, none of these models
[702] yet aces all the behavioral
and brain tests that we have.
[705] It doesn't fully predict the
explainable variance, even
[707] accounting for the cross monkey
thing that we talked earlier.
[710] It doesn't fully explain
the behavioral data as well.
[713] And I'm not showing you that.
[714] You'll have to take
it for granted.
[716] I could talk about
that, but we know
[718] it's true, to not be perfect.
[719] So you need to hold this in mind
that it's good, but not done.
[723] OK?
[723] So that's progress,
but not done.
[725] And to help the field
say that if we are done,
[729] or how far down we are, and
to keep people motivated
[732] on multi objectives-- not
just explaining V1, not
[734] just explaining V2,
not V2-- all of this,
[737] we've tried to build this
platform I referred to,
[739] Brain Score.
[739] And I think you'll
hear about this,
[741] you have already from
others, that many of you
[743] may want to use to submit your
own models to say how good did
[745] they fit the neural data
and the behavioral data
[749] across these different
levels in the ventral stream.
[751] And again, we think this is
just in service of good science
[754] which has to
explain all of that.
[755] So the summary of
this is that there's
[757] clear scientific
progress, but they're
[759] still incomplete, demonstrably
inaccurate in important ways.
[762] OK.
[763] This is where I want to put up
some frequently asked questions
[766] that maybe we have time
at the end to talk about.
[768] Why are you testing
explained variance?
[772] And are you just fitting
big models to the data?
[774] No.
[774] This is cross-validated.
[776] I hope these are things
that are obvious.
[778] And then one of the big lurking
questions of these models
[780] is some people
think they shouldn't
[782] count as an understanding, and
there's various forms of that.
[785] They're not intuitive.
[786] They're theoretically elegant.
[788] There's little-- if
you're a vision scientist,
[790] it doesn't give the information
about why the pixel--
[792] how the pixels matter.
[793] Or how do you improve
to make the next model?
[795] I think that's a
really good question.
[797] Or how do you generalize
to other problems
[799] with an AI [INAUDIBLE]?
[800] I'm going to put this up
as a thought experiment
[803] and we can put it
up again at the end,
[804] and we can sort of talk
about some of these things
[807] if we have to.
[808] But again, this is all by way a
review, of just trying to say,
[811] look, we have these models
that are pretty good.
[813] Better than before, but not
as good as we want them to be.
[816] OK.
[817] So are the best matching
in silico networks?
[819] Do they count as
an understanding?
[821] I referred to it, some
people disagree with that.
[823] But so, what I want to tell
you about next is not trying
[826] to take on that question
directly, but to ask,
[829] let's not have a debate about
what counts as understanding
[832] and what doesn't.
[833] Let's just ask, if
it's understanding,
[836] it should be useful.
[837] So let's say, what can
a brain scientist do
[839] with this quote,
"understanding,"
[841] or potential understanding?
[842] What can we do with these
models that we couldn't
[845] do before we had those models?
[846] In fact, this is
why scientists build
[848] models in the first place,
is to do something with them.
[851] Not just to report
to other scientists.
[853] So what can we do with them?
[855] Well, let me now turn you
back to Teuber again, and let
[859] you hear Teuber again, in 1974,
talk about what science does.
[863] So here we go.
[864] [VIDEO PLAYBACK]
[864] - You see, the [INAUDIBLE] view
is that science, any science,
[869] tries to explain, predict, and
control certain difficulties
[876] than to define astrophysics
as a science at this stage.
[881] You may explain and predict,
but control is still
[883] very difficult,
particularly where
[886] other galaxies are concerned.
[888] But who knows?
[892] By that token, you could say
we are far from being there
[896] because we cannot yet
explain, but we try.
[900] [PLAYBACK ENDED]
[900] JIM DICARLO: OK.
[901] So Teuber couldn't explain
things like perception in 1974,
[906] but I'm here offering you models
that offer the ability, I'm
[909] saying, to explain and predict,
and Teuber says that science
[912] should be able to control.
[914] So we took that
seriously, and we--
[916] Koh, you've already met
here, and Pouya Bashivan,
[919] they teamed up to do this
work that we published
[922] a couple of years ago, we
called Neural Population Control
[925] via Deep Image Synthesis.
[926] So this is now taking the models
and asking them to offer us
[931] the ability to control neurons.
[933] And I'm going to show you kind
of how we go through that,
[936] but I want you to see this
in the context of models.
[940] Even if they're not
always intuitive,
[941] they offer abilities
to do things
[944] that we couldn't do without
them once they can reasonably,
[946] accurately explain and predict.
[948] As I pointed out, these models
are only partially accurate.
[951] But we said, let's take
their partial accuracy
[953] and see what we're able to do in
the control sense of the word.
[957] So again, I'll just give
you this by way of review.
[960] The idea is that
here's an example
[962] model that's a pretty good
model of the ventral stream.
[964] It's got multi convolutional
layers, some fully connected
[967] layers, some categorization
at the backend.
[969] This is the level
of the model that we
[971] thought was a reasonably
good alignment with area V4.
[973] Remember, V4 is the
dominant input to IT.
[976] It's sort of midway
up the ventral stream.
[978] We started with V4
because we thought
[980] it would be easier
to get this to work
[981] in a mid-level area like
V4 rather than trying
[984] to go all the way to IT.
[986] So what we have is
a model of, this
[988] is a population of neurons.
[989] It's meant to be a linear map
to this population of neurons
[992] in V4.
[993] And so we claim that we have
models that are pretty good
[996] at doing this, and so now what
that offers is the ability
[1000] to say, well, let's turn
this around and say,
[1002] if our goal is to control the
neural activity in V4-- say,
[1006] of individual neurons or
populations of neurons--
[1009] call that a desired neural state
of, in this case, area V4--
[1012] that's a so-called control goal.
[1015] Then the model can give us ways.
[1018] What the model is doing
is specifying how pixels
[1020] ultimately drive neurons.
[1022] That's what the model's about.
[1023] It's an encoding model.
[1024] It goes from pixels
to neural activity.
[1026] So the model offers
the ability to specify
[1029] the pixel combinations to
design precise patterns
[1032] of light energy, i.e.
pixel patterns, that
[1035] are shown to the
eyes to try to set
[1037] the brain into different
neural states of our choosing.
[1040] That's why it's called control.
[1041] We, the experimenters,
decide what the state is.
[1044] We ask the model to give
us the control image,
[1046] and we are going to
go ahead and test,
[1048] did that control image drive
the neurons into the state
[1050] that we desire?
[1052] Here is the model.
[1053] So now this is done through
optimization through the model.
[1056] So given that you
have a model, you
[1057] can then ask the
model to optimize
[1060] the pixels to accurate--
to drive neurons
[1063] in a particular state.
[1064] And I'll show you examples of
the different ways we do that,
[1066] but this is just to show
you that typically, you
[1068] start with sort of a
random collection of pixels
[1070] and then you optimize
against some control goal
[1073] to achieve an image
that then, we then
[1074] show the image to the
animal, and we test how
[1078] good is that controllability.
[1079] So it's now an experiment
on how good the control is.
[1082] And we found in
this paper that we
[1084] could use these
model designed images
[1085] to reasonably, successfully set
the neural activity states here
[1089] in this mid-level, I'll
call it, deep in the brain.
[1091] It's multi cortical levels
in almost to the highest
[1094] level of the ventral stream.
[1096] So here is how this looks.
[1098] These are recordings of one
neural site in visual area V4.
[1102] This is the measured
neural firing
[1105] rate on the y-axis
in arbitrary units.
[1107] This is the model
predicted neural firing
[1109] rate of that neuron.
[1111] So remember what the model is,
it's got a linear basis of V4.
[1114] We built a linear map to
this individual V4 neuron
[1117] on some test data.
[1119] We then plotted on some
held out data, which
[1121] is what you're seeing here.
[1122] Each of these dots is an image.
[1124] This is one example image.
[1126] What you see is, this is the
model's predicted response
[1129] to these images, and this is
the measured actual neural
[1132] response to the images.
[1133] These are predictions
from the model.
[1135] And you see that the predictions
line up with the neural firing
[1138] rate quite well.
[1139] The dots are really like,
nicely along this line.
[1142] And first of all,
you should find
[1144] that pretty, cool except
to say this visual
[1147] is essentially the
breakthrough I already
[1149] told you, just plotted in
a more easier to see form.
[1151] This is what was
in these papers,
[1153] in effect, is that
models are pretty
[1155] good at predicting things,
and this is showing that here.
[1159] So it's not perfect.
[1160] This is glass half full.
[1161] It's pretty good,
especially for the V4 sites,
[1163] which are even better than
IT in terms of matching.
[1167] OK.
[1167] If you're with me so far, you
say, this is just the model.
[1170] This is the setup that
I gave you so far.
[1172] But now, an example
control goal is
[1175] if you think this
model is correct,
[1177] you should be able to do things
like drive this neuron up
[1180] here and find me an image
that the model predicts
[1183] would drive up here, that would
actually drive the neuron out
[1185] here.
[1186] So sort outside its normal
distribution, if you will.
[1188] This is a set of natural
images that we showed,
[1191] and this was the range
of responses we got out
[1193] of this V4 particular neuron.
[1196] And OK, so here you go.
[1198] We call this control goal 1--
[1199] super activate this neuron.
[1201] Drive any single neuron site
beyond the maximum response
[1204] observed so far.
[1205] That was the control.
[1206] This is not only
possible control,
[1207] but it's just one we
picked because it's
[1209] sort of a fun place to start.
[1212] And so we asked the model,
please find us images
[1214] that you think will
drive this neuron well.
[1216] That is, images that you
predict that are out here.
[1219] We do that optimization
procedure that I described,
[1221] and we did it within the
so-called receptive field
[1224] of this particular V4 neuron.
[1226] These are the images
it came up with,
[1228] with those optimization
procedures I showed you
[1230] earlier.
[1230] Now, we didn't ask the
model to make these images
[1232] look like cars, or
dogs, or anything.
[1234] We just put some constraints
on the optimization,
[1237] but we said, just
get this neuron
[1239] to fire, please, in
whatever way you can.
[1241] And these are the kind of
images it came up with.
[1243] These are five different
initializations of these runs,
[1246] and remember,
random start points.
[1248] But you can see they're
kind of similar,
[1250] and maybe you want to
interpret them in certain ways.
[1253] But regardless, these are
proposals, if you will,
[1255] of control images from the model
to activate this particular V4
[1259] neuron.
[1259] Then we go ahead and show those
back to the animal, and we see,
[1262] did we actually get the neuron
to drive up [INAUDIBLE]??
[1265] And here are the results of
this particular neural site.
[1268] These are the red dots.
[1269] These are these five images.
[1270] These are their neural
responses here on the y-axis.
[1273] And remember, the
model's predicting
[1275] them to be way out here,
at these units that
[1276] are in this regime here.
[1278] But, and they actually are high.
[1280] They're higher than
anything that we'd
[1282] seen out of the natural
distribution of images
[1284] so far, so that's
a success to me.
[1287] It's like wow, we
were able to drive
[1289] that neuron outside its regime
under the model direction,
[1292] so that's control success.
[1293] But it's not the
control we would desire,
[1296] because it should
be on a diagonal.
[1298] If everything was
perfect, these points
[1300] would be right on the diagonal.
[1301] The model would say it's at
unit 6, and it would be at 6.
[1305] It's not there.
[1307] So again, glass half
full gives us some power.
[1310] Glass half empty, probably
why we're not on the diagonal.
[1313] But you can see this
is on the road to like,
[1316] OK, models already
give us power,
[1318] even in this kind of
early stage of models.
[1321] And as we improve the
models, we think this control
[1323] will get even better.
[1325] Let me give you another example
that excites me even more
[1327] than that single neuron
example, the idea of setting
[1330] the V4 population into a state.
[1332] So not just one neuron being
high, but what if I want--
[1335] here's 40 V4, or 38
recorded V4 neurons.
[1339] This is called
population control goal,
[1341] like a neural
state, if you will.
[1343] Where you say, I'd
like, I don't know,
[1345] neural site 12, just to pick
a side out of a random set.
[1350] This is just one
example control goal.
[1351] I want this site to
activate very much,
[1353] and I want the other ones
to not activate at all.
[1356] So now I'm asking
the control goal
[1358] that's much more complicated.
[1359] It's a population control.
[1360] Give me this high,
give me all these low.
[1362] You can imagine, I'm like,
give me every other neuron
[1364] high and every other one low.
[1366] Or the even numbered neurons
high and the others low,
[1369] or some other random
pattern you could think of.
[1371] In principle, you could
do any of these things.
[1373] We only did this one thing
so far to just test it out,
[1376] like try this one.
[1377] Please, Mr. Model,
could you please
[1380] come up with some images
that do this control goal?
[1384] This is non-trivial
because these V4 neurons
[1387] were recording them.
[1388] These 38 neurons, they have
overlapping receptive fields.
[1391] So it's not as simple
as just putting energy
[1393] into one part of
the visual field.
[1395] All the energy is going
to go into this part
[1396] of the visual field, but
it has to somehow target
[1398] neuron 12 with some
clever pixel arrangements
[1400] that doesn't activate
the other neurons.
[1403] And if you just search through
image databases-- again,
[1406] we get we collected
about several--
[1407] I think it was a
couple hundred images,
[1409] Koh will remember exactly--
[1411] and you just looked through the
image database for the image
[1414] that best did this control
goal, this was the best image.
[1418] It happened to be an image of
this random floating chair.
[1421] It activated site
12 pretty well.
[1423] Unfortunately, it activated
a bunch of the other sites
[1425] as well.
[1427] So this is not a bad,
not terrible control,
[1430] but it's clearly not desired
and not looking exactly
[1433] like what's at the bottom.
[1434] And so we said,
could the model--
[1436] could it do better?
[1438] And of course, humans could
stare at this for a while
[1440] and say, well, I think we
should put some black lines,
[1443] and that'll be neuron 12.
[1444] We could kind of try
to do that, and then
[1445] how do we shut down neuron 38?
[1447] I don't know.
[1448] We could try to do
that with our minds
[1450] and we probably
wouldn't get very far.
[1452] But the model's like,
I know what to do.
[1454] I have access to all of this.
[1456] Well let the machine
optimize this.
[1458] And this is what
it came up with.
[1459] It said, this is my
proposal for what
[1462] you should show if you
really want this neural state
[1465] to happen.
[1466] It's not an image of a chair.
[1467] It's not an image of anything.
[1468] I don't know what it is, it's
just what the model proposes.
[1471] We call it a synthetic
controller image.
[1473] You see it has sort of remnants
of some of the structure you
[1476] see in this image?
[1476] That's sort of
interesting, but it's
[1478] whatever the model proposed
and we just take it at that.
[1482] It's the model's proposal.
[1483] Here's what it did when
we showed this image
[1486] to these same group of neurons.
[1488] It activated site 12-- great.
[1490] And it also tended to
have less activation
[1493] on all of these other sites.
[1494] But that's pretty good, so
progress relative to where
[1497] we were, but it's not perfect.
[1499] This red line should
be down lower,
[1501] and this red line should be
down, and these should be zero.
[1503] So again, glass half full--
[1506] progress.
[1506] But glass half empty,
not quite there yet.
[1510] But I hope you can see the
potential power of this
[1513] without needing to engage
on the word understanding.
[1516] The tools of the models
offer embedded knowledge
[1519] that can be used to do things
that are useful, like drive
[1521] neurons into certain states.
[1523] That then leads to sort of
possible behavioral control
[1525] goals, possible ways to
intervene in brain dysfunction
[1529] that the models
enable, even if we
[1531] don't have good intuition about
their nonlinear processes.
[1535] And so I want you to take that
from this presentation part
[1538] so far.
[1539] And Tiago, I see you asking--
you have your hand up.
[1541] Go ahead.
[1542] AUDIENCE: This failure
to completely know--
[1545] not activate the
other neurons, was
[1547] it something predicted
by the model in the sense
[1550] that the model could not,
when designing the stimulus,
[1556] synthesize an image
that you would silence?
[1558] Or it was something that
the model predicted,
[1559] that those neurons
would be silent,
[1561] but then the data
showed that there were?
[1562] JIM DICARLO: Yeah.
[1563] That's a great question, right?
[1564] Because one thing the
model could say, is
[1566] there is no way to achieve that
control state from [INAUDIBLE]..
[1570] And in some cases,
that was true.
[1572] And Koh will remember
better than I,
[1574] because he was the primary
author on this work with Prouya
[1577] Bashivan.
[1577] And in some cases, the
model would-- some setups,
[1580] the model would
fail to find these.
[1581] I think in this
example, the model
[1583] thought it could do better
than it actually did,
[1586] just like in the example I
showed with the single neuron.
[1589] So there's a little bit of
that, which is also interesting.
[1592] But I think the failures
that we see so far,
[1595] the non-perfect controls,
are mostly the models--
[1598] not because the model
said it would fail,
[1600] but we only
considered cases where
[1601] the model thought it would be
able to control, [INAUDIBLE]..
[1604] I just don't remember how we
quantified it in this example
[1607] here, and how to say,
was it that neuron 32 is
[1610] going to be low.
[1611] And I don't I'm not sure
we are going to be high.
[1613] I don't think we even looked
at it at that level of detail.
[1616] We had a sort of
global score on what
[1617] controllability it should have,
and that's how we quantify.
[1620] This is just a visual to
give you a sense of this,
[1622] but we actually quantify this
whole thing with a number.
[1625] And usually, the number ended
up being lower in the experiment
[1629] than the model
predicted it should
[1630] be able to get in terms of
an overall kind of SOFTMAX
[1633] score on this example here.
[1637] I don't that helps, Tiago,
but it's a great question.
[1641] And it's another area of
exploration in the models.
[1646] AUDIENCE: What does
negative activation mean?
[1649] JIM DICARLO: It's a good point.
[1650] So these are arbitrary units.
[1651] So I think we zeroed
this-- and again, Koh
[1653] may need to jump in and help
me with the average firing
[1656] rate or the background firing
rate to just the gray image.
[1661] So neurons, of course,
don't fire negatively,
[1662] but these data have
been transformed
[1665] to give us sort of a Z-score
in response out of each unit,
[1669] and that's why it
can go negative.
[1670] AUDIENCE: OK.
[1671] So I have another question.
[1672] So for this experiment
and the previous one,
[1675] I wonder if there's a
control, and maybe you guys
[1678] have already done it as
well, where you've searched
[1680] for the opposite condition?
[1681] So essentially, nullify
neuron, I think,
[1684] 12, and then amplify
all the other ones.
[1687] So I'm thinking, could you
do a negative control where--
[1690] and maybe you've done this
and I haven't seen it,
[1692] where even for the line
in the previous experiment
[1694] you map the response
to zero activation
[1698] or something like that.
[1699] I don't know what your
thoughts are on that, Jim.
[1702] JIM DICARLO: Yeah.
[1703] You mean like this, right?
[1704] AUDIENCE: Right.
[1705] Right.
[1705] Yeah.
[1705] Something like that.
[1706] Yeah.
[1706] JIM DICARLO: Yeah.
[1706] Yeah, that'd be cool.
[1707] Or I had just mentioned, like
could we do like this, right?
[1711] I mean, we have not tried
any of that stuff, at least
[1715] not-- unless Koh's done it
without telling me about it
[1717] yet, which maybe he might have.
[1718] But I don't think--
[1720] we've not tried that
yet, explicitly.
[1722] In principle, it
should work, but it's
[1724] like there's infinite space
of things to try there.
[1728] So this is all
we've done so far.
[1729] In fact, our next move was
to try to move this up to IT,
[1732] and things seem more
challenging at IT
[1734] for reasons we don't
yet understand.
[1735] So that's the edge
of where things are.
[1737] But we could go back to V4 and
try to play this game some more
[1740] there too, but we haven't yet.
[1744] So it's a great idea.
[1745] Although, if you think it
through, if these things fail,
[1749] then what do we do
with that knowledge?
[1751] There's always that
lurking in the background.
[1753] Like, if things don't work, then
it's just, what do we do next?
[1756] So it all comes back to
build a better models,
[1758] is the way we think
of it in the lab.
[1759] But we-- the answer
to your question is we
[1761] haven't tried it
yet, to my knowledge.
[1763] AUDIENCE: Does it
bother you at all
[1764] that these images
are not naturalistic?
[1767] Or in other words,
what would it look
[1769] like to try to find control
stimuli but from the manifold
[1772] of naturalistic images, and
is that even interesting?
[1776] JIM DICARLO: That's an
interesting question too.
[1778] It's like as I
mentioned, there are
[1780] sort of regularizers we put
on the images that give them
[1784] some structure.
[1786] You could try to make
them even stronger,
[1788] where you sort of search
within natural images.
[1790] But I kind of view
it the other way.
[1792] Like, I like to let the thing
go as far away as it could
[1796] to give it the best chance to
find something that we wouldn't
[1799] find on our own.
[1800] That's the way I was
thinking about it.
[1802] But the risk of that is,
of course, the models
[1804] are best in the regime
around the distribution
[1806] of the map of images.
[1808] So more space you give it,
the more it kind of basically
[1810] shows that it's an
incorrect model.
[1812] And that's the reality of
where things are at the moment.
[1815] So maybe these more
natural will probably
[1818] lead to better kind of
control in terms of matching,
[1822] because you're more within
the distribution of the test
[1824] images.
[1825] But it might not, for instance,
allow as much super activation
[1828] as we would achieve.
[1829] That would be my intuition.
[1830] It's like you wouldn't
be able to do things
[1832] that you could otherwise do.
[1834] But we haven't tried.
[1836] Again, that's a
great space of how
[1837] do you want to regularize
even more on the images
[1840] to do that, in effect?
[1842] But the question is,
does it bother me?
[1844] I'm like, no, I actually
find it most exciting
[1847] that it finds things that I
wouldn't find by just searching
[1850] natural databases.
[1850] That's how I think of
it, and that's the spirit
[1854] of model based control.
[1856] AUDIENCE: I wouldn't have
expected the V4 [INAUDIBLE]
[1859] to look anything
naturalistic either.
[1861] Because like, that's
way before areas
[1865] that we usually think are being
read out to execute behavior.
[1868] So my expectation is not
that, but if it comes out
[1871] of the model that way,
that will be good too.
[1873] So I kind of agree with Jim that
maybe we let the model speak.
[1876] And of course, as
he also mentioned,
[1878] that the models will be
biased towards, maybe
[1881] trivially towards, their own
training sets, so and so forth.
[1884] That's something that we
should keep an eye out on.
[1887] JIM DICARLO: But the
main point of all this
[1889] really was just to show--
[1891] it's really kind
of a foil to say,
[1893] those who want to
say these models
[1894] shouldn't count as
an understanding,
[1896] they have to reckon with these
kind of application goals.
[1900] Like that's, I think the--
[1902] there's going to be a trade-off
between the ability of models
[1905] to achieve applications like
this one and the intuition
[1910] about how models work.
[1911] And I think that tension
is in our field right now,
[1913] and this was a kind of
push in one direction
[1915] to say, hey, you
want applications?
[1918] Maybe you want to give
up a bit on intuition
[1920] and let the models have a
say on what should be done.
[1924] At least for me,
that's how I've been
[1926] motivated for this experiment.
[1928] AUDIENCE: I had a
follow-up question
[1929] to the glass half
full sort of thing.
[1934] So in the previous plot,
or even in this plot,
[1938] what the model is
essentially [INAUDIBLE] to do
[1942] is something that
could be considered out
[1944] of its distribution.
[1946] Like, it's
extrapolating what could
[1948] be images that would drive that
sort of neural firing grid that
[1953] has not been seen.
[1954] So how do we comment on whether
it's a shortcoming of the model
[1959] that it's not able to drive
those red points to the line,
[1964] or is it something else?
[1966] Maybe the model is good
enough, but because it's not
[1969] seen those samples, it couldn't
drive it to the x equal to y
[1976] line.
[1976] JIM DICARLO: Right.
[1977] Well, I think
that's a good point.
[1979] I share your
intuition that these--
[1981] we're asking the models
to go out of distribution,
[1983] as you say.
[1984] But I think this comes down
to how we use the word model--
[1986] how you and I use
the word model.
[1988] As I said earlier, once we
optimize and fix parameters,
[1992] that is the model.
[1993] So you're saying the
model might still be OK,
[1995] what you're imagining
is like, well,
[1997] the model if I taught
it on some more stimuli,
[1999] then it would be OK.
[2001] And to me, you're
creating a new model
[2002] because you're giving--
your micro tuning
[2004] the parameters then.
[2006] So right now this is evidence.
[2007] This model is-- this model,
as I construe the word model,
[2010] is wrong because these points
aren't on the diagonal.
[2014] But partly right, right?
[2015] So in that framing,
it's like no, the data
[2017] show the model is wrong,
but better than no model.
[2021] And your intuition
is like, maybe I
[2023] could make a better
model with more training,
[2025] and I can share
that, and that might
[2028] lead to a model that
would match better.
[2029] But we also get into like,
the more you have to do that,
[2032] the less the model is
able to actually offer any
[2034] generalization control , which
is kind of what you really want
[2038] from a perfect model.
[2039] So then again, this
tension of what
[2041] counts as generalization and
how far away it needs to be.
[2044] But I agree, you could
start to train models
[2046] on a bunch of other
stimuli that might lead
[2048] to better effective
control and even expanded
[2050] the domain in which
it could control.
[2055] I hope that makes sense.
[2056] Clearly, this is
a fail-- this is
[2058] both a success and a failure.
[2059] Again, half full and half
empty in our language
[2061] of what these models are.
[2064] Unless there's big
questions, I want
[2066] to kind of go on to any more--
[2068] I want to kind of just close
this section here a bit
[2070] and see if we can get to
some more fun discussion,
[2072] and maybe come back to this.
[2074] With the ability to control
patho-neuroactivity,
[2076] you have [INAUDIBLE]
images, which is something
[2078] that we think a lot about.
[2079] We think this is
something that I
[2080] think has long term potentiation
as one of the reasons
[2084] for these models.
[2088] Teuber, at the beginning,
was poo-pooing hypnosis,
[2091] but the history of psychology
has things like psychotherapy.
[2095] In principle, you
can influence brains.
[2098] I think I'm influencing
all your brains
[2099] right now, if you're listening
to me in some ways, just
[2102] by providing auditory
and visual input
[2105] to your brain, some of
which will be long lasting.
[2108] So there's no, in
principle, reason
[2111] that we couldn't intervene
in brains with a more
[2114] expansive space of interventions
guided by models that
[2118] might have health
benefits, that I think
[2120] we should think more
about, that would be
[2121] far better than giving drugs.
[2123] And classically, that's
called psychotherapy,
[2125] but we didn't have the
mechanisms to engage--
[2128] we don't have the knowledge
of what to say, how to say it,
[2131] how to provide it.
[2131] But these models might provide--
[2133] in the long run, are
going to provide new ways
[2135] to think about that idea of
intervening noninvasively,
[2140] hopefully to
improve [INAUDIBLE]..
[2142] So far, we've achieved these
in control up to this level V4,
[2145] and that's what I've showed you.
[2146] We've been trying to
get it to work in IT,
[2148] and that's still
been a challenge.
[2152] But, so what we think is as
we further improve our models,
[2154] a superpower will--
[2155] I call this a superpower--
will further improve.
[2157] And that's sort of
a motivating goal,
[2159] like back to make
a better model,
[2161] then we can come back to
control experiments again.
[2163] So this was sort of an
application detour, in a way.
[2166] OK.
[2167] Summary-- clear progress,
but still incomplete.
[2169] I want to turn to the last
part of the talk of like,
[2172] I think some of you have asked
these questions in the chat.
[2174] I said, what can
brain scientists
[2175] do with the current hypothesis?
[2176] I give you an example,
a control example.
[2178] This is just one
example of things
[2180] you can do with these
current best models.
[2182] But back to the glass
half empty, right?
[2184] OK.
[2184] What did I say?
[2185] The half full part can
help us do stuff already,
[2187] better than our old models,
but how can we improve this?
[2190] How do we fill up the glass?
[2192] How do we improve these models?
[2193] How do we improve the-- i.e.,
the mechanistic hypotheses?
[2196] And I think that is, of course,
the forward going research--
[2199] the central forward
going research
[2200] question, which will, of course,
have application payoffs.
[2203] OK.
[2204] And this question
is, of course--
[2207] to me, it's somewhat
obvious how you
[2209] do this, is how
you do any science.
[2211] You measure stuff,
you test stuff,
[2213] you see where it deviates
from the actual stuff, when
[2216] it deviates from the brain.
[2217] Then you build new models that
better match the deviations
[2221] that you see, then you use
those as the new hypotheses.
[2223] So the current best models,
they become the new hypotheses.
[2226] Then you measure stuff,
you try to compete
[2228] the models against each
other, measure more things.
[2231] Then you go ahead
and build new things
[2232] that close the gap
on the residuals.
[2234] This loop, that's science--
[2236] measure or build.
[2237] This is usually-- the thing
on the right is usually
[2239] called hypothesis building,
and the thing on the left
[2242] is called experiment.
[2244] And science should be
doing both of those things.
[2246] It's just that the hypotheses
are more complicated.
[2248] Those system level hypotheses,
they're complicated.
[2250] They're not hypotheses like,
IT does object recognition.
[2254] That's kind of not a fully
formed engineering hypothesis.
[2258] Or, the brain is a
collection of neurons,
[2261] and that's who you are, which
was the Astonishing hypothesis
[2263] that I showed at the beginning.
[2265] Those are not engineering
level quality hypotheses.
[2267] So the problem is engineering
level quality hypotheses are
[2270] complicated, are not intuitive.
[2271] But they can be built. They can
be managed by machines, just
[2274] like any engineered system.
[2275] So this loop is what
needs to run right now.
[2278] You've heard from
others, and you
[2280] will hear more about,
probably, about Brain Score
[2281] and benchmarking models.
[2283] And that's a big part
of what's on the left,
[2285] is that this is not just
one type of measurement,
[2287] but collections of measurement.
[2288] And the models,
many of you are--
[2289] those are also complicated.
[2291] Many of you there are
starting to play with them,
[2293] and the tools that
enable them, and those
[2295] will continue to be
interesting and good
[2297] forward hypothesis
building directions.
[2300] But let me just say, what
are major axes that we're
[2303] pushing on here?
[2304] Well, I'm just going to
highlight two major lines
[2306] of ongoing experimentally driven
work without actually showing
[2308] you this work, because I
think you've heard about it
[2310] or you will hear about it.
[2311] So for forward-going
model building,
[2313] there's two of the
important lines
[2314] for us in the lab right
now are study and improve
[2317] the early components of these
ventral stream hypotheses,
[2320] even the sort of
retina, LGN, V1 levels.
[2323] You've heard about some
of that from Tiago, who's
[2326] there in the audience, and a
grad student, Joel Dapello.
[2328] These are just two
of the students that
[2330] have happen to be working
with us, that are working
[2332] on these things right now.
[2334] This is already
having some pay-offs
[2335] in terms of improving models'
accuracy or robustness,
[2338] as Tiago told you.
[2339] But to me, it's just
building better models of V1
[2341] also needs the better models of
the whole ventral stream, even
[2343] measured at the
behavioral level.
[2345] And Tiago has told
you about that work
[2348] and can tell you
more about that.
[2349] And some of you may be
interested in projects
[2351] in this direction.
[2352] So think of that as sort of
one area model of the movement
[2354] that we're actively pushing on.
[2356] The other is to
study-- and some of you
[2358] asked about this-- the
recurrent feedback processes
[2360] in the ventral stream.
[2361] And this is work
in our lab that's
[2363] been mostly been led by
Koh, who's also there.
[2365] And try to measure the current
processes and the effects
[2369] of them, and also downstream
areas beyond the ventral stream
[2372] that interact with
the ventral stream,
[2374] because the ventral
stream does not
[2376] live in isolation in the brain.
[2377] So that also will lead
to new families of models
[2379] that we think will lead to
better alignment with even
[2382] areas like V1, V2, and
V4, which then, in turn,
[2385] will lead to things
like better control.
[2387] So those are ongoing
experiments a new model building
[2390] that also needs to be done.
[2391] But broadly, I want to
say the organizing--
[2393] and I have some backup slides,
if we have time at the end,
[2396] to tell you about both
of those lines of work.
[2398] But again, I don't want to steal
thunder from Koh and Tiago.
[2401] The organizing goal
of our field is
[2403] to discover ever more accurate
engineering level mechanistic
[2406] models of the human
visual system.
[2408] That's what I think.
[2409] The organizing goal of our
field is or should be--
[2411] and again, break,
measure current models
[2413] against myriad
measures which we're
[2416] cataloging in Brain Score.
[2417] Use those to build
better models.
[2419] These are examples of models.
[2420] Those models don't just
stand as models on their own,
[2422] they can be deployed
for AI applications
[2424] for us, mostly in
computer vision.
[2426] They can be deployed for
potential health applications,
[2428] and I alluded to the ones that
we think about longer term.
[2431] They can be deployed
to different ways
[2434] to allow you to learn faster,
like what images to show
[2436] you to learn objects faster.
[2438] Those are other things
that we're working on,
[2440] kind of broadly
connected to education.
[2442] And probably other things that
relate to vision, that we're
[2444] not even thinking about yet.
[2445] But these models stand as
our field's hypotheses,
[2448] at least of visual
intelligence, at the moment.
[2451] So I'm going to summarize
some take-home messages
[2453] that I've tried
to give you today,
[2455] and then I have some
motivating slides at the end
[2457] to kind of talk about
broader picture things,
[2460] and then have a lot of time
for discussion with all of you.
[2463] So summarize.
[2464] If you just fell asleep
for the whole lecture,
[2466] here this is the whole
lecture in a nutshell.
[2468] The background, the
ventral visual stream
[2470] produces an IT neural
population representation
[2473] that carries linearly
decodable image generalizable
[2476] solutions for all the tested
core object recognition tests
[2479] we've done so far.
[2481] We don't know if this is
yet a perfect description.
[2484] In fact, we know it's
not a perfect one,
[2486] but it's a very good description
of the animal's behavior
[2489] in core recognition regimes, is
linear reads out of IT cortex.
[2494] And we also found--
this was the sort
[2495] of collaborative
breakthrough-- that optimizing
[2498] some particular deep
artificial neural network
[2500] architectures for
core recognition tasks
[2503] leads to internal
neural representations,
[2505] neural patterns of firing in
artificial neurons in some
[2508] of those ANNs that turn
out to be remarkably
[2510] similar to the internal
representations
[2512] of the ventral stream.
[2513] Another way to put
that is they're
[2515] improved matches to the
internals of the brain
[2517] relative to prior models
that existed before,
[2520] but still only glass half full.
[2522] Still only half full.
[2524] This result-- if those of you
who are aficionados, somebody
[2527] mentioned faces may be
special-- this result includes
[2529] face neurons, by the way.
[2530] Often people think of
that as a separate system.
[2532] Those face neurons
naturally fall out
[2534] of these kind of optimizations.
[2536] You don't need to create
a separate system,
[2537] but it's interesting to think
about if you do do that.
[2541] And I want to also say, and this
audience I've mentioned this,
[2543] but I want to re-emphasize it.
[2544] This result is consistent
with but does not
[2547] imply that the brain learns
by classical backprop.
[2550] In fact, we don't think the
brain learns by backprop
[2553] with supervised examples.
[2555] We just view that as
an engineering trick
[2558] to get an optimization
that then aligns
[2560] with something that
evolution came up
[2561] with in a different direction.
[2563] And that's my preferred
interpretation
[2565] of these results,
the result that
[2566] an optimized neural
network by backprop
[2568] matches the brain does not mean
the brain is running backprop.
[2573] And so there is--
[2576] I think of this species A is
primate vision's optimized,
[2578] but evolution and
postnatal development
[2580] unsupervised mechanisms.
[2582] That's our most-- that's our
standard hypothesis of course,
[2585] in neuroscience and biology.
[2587] But species B, as I'll
calll it, deep ANNs.
[2590] They're optimized by
engineers in a different way,
[2592] but it's convergent in the
sense that the system functions,
[2596] the impinge information
representations
[2598] turn out to be
reasonably well aligned,
[2600] and that's why we
see those matches.
[2602] And that's important.
[2603] It provides a normative
framing on the ventral stream,
[2607] but it doesn't mean that this is
the way the brain is learning,
[2610] and I think that's
an important point.
[2613] These same ANN
models can be used
[2616] to guide the construction
of novel synthetic images
[2618] to super activate or control
populations of neurons.
[2620] This is the use--
[2621] that glass is half
full-- it's already
[2623] used for these control
senses, at least
[2625] I showed you in area V4.
[2627] Now turning to red, these
shortfalls, if you will.
[2629] These same ANNs, they're not
yet functionally identical.
[2632] The glass is half empty.
[2633] You can look at
some of these papers
[2635] and see that the
behavioral level,
[2636] we have other-- we see that
already at the neural level.
[2639] We know the glass
is still half empty.
[2640] There' still work to be done
on improving this model.
[2643] One difference that might
explain the glass half empty
[2645] is the lack of
recurrent circuits.
[2648] And some of Koh's
recent work shows
[2650] that fast acting automatically
above recurrent circuits
[2653] enable the ventral stream's
superior performance.
[2656] In other words, it enables
the IT representations
[2658] on many images.
[2660] We can see that they're
recurrently dependent.
[2662] And that's ongoing work
from Koh and others,
[2664] and so that's an area
of model improvement.
[2667] And we-- Koh included,
and Tiago included,
[2671] and many others at my lab
and other collaborators far
[2673] beyond-- are trying to
build new models that
[2675] incorporate more of these
biological constraints.
[2678] And thus far, these models
show that computer vision
[2680] gains in efficiency
and gains in robustness
[2683] to image perturbation.
[2684] And I didn't talk about
the depth efficiency that's
[2688] related to the
recurrence work, but I
[2690] did mention the
robustness in Tiago's work
[2692] that you can see when we make
things more biological as you
[2695] build those models.
[2696] So just stepping way back.
[2697] I've been talking about vision
as part of visual intelligence.
[2701] I've been talking about core
recognition, the first couple
[2703] hundred milliseconds.
[2705] There is far more, of course,
to human intelligence, even
[2708] visual intelligence.
[2709] Scene understanding requires
prediction over seconds--
[2713] where is it safe to walk?
[2714] Remember that first slide.
[2716] Requires things like what people
would call intuitive physics,
[2719] or intuitive psychology.
[2721] Those are frontier areas that
I'm not talking about today,
[2725] but I think the same
kind of approaches
[2727] are starting to find their
ways into those areas.
[2730] Broader language, social
interactions, and body
[2732] intelligence, of course,
is a very deep well
[2734] of human intelligence
that can be attacked
[2736] with the same kind of
approach, and actually
[2738] needs to be attacked if we say
we could really understand how
[2741] things like social abilities
are the result of the mechanisms
[2746] of the mind as [INAUDIBLE]
at the beginning.
[2749] So in the last one
last slide here,
[2751] I want to kind of-- if
you're an AI researcher
[2753] and you say, well,
OK, my goal is
[2756] to build computational
intelligence that
[2758] meets or exceeds
biological intelligence,
[2760] I want to just give you a
perspective on how I think
[2763] about if you're in that boat.
[2764] And I'd like to do
that too, although I'm
[2766] a neuroscience
researcher, primarily.
[2767] But I would love to see
silicon based things
[2770] that can compete with us.
[2772] What are your strategies?
[2773] You could say, well, let's
just forget about the brain.
[2776] We're just going to
build whatever we need to
[2778] and ignore brain sciences.
[2779] And that's not an
unreasonable goal.
[2782] You probably wouldn't be at the
CB&ampMM summer course if you
[2784] felt like that, so I'm already
speaking to a biased audience.
[2787] But so, let's say you're not
going to take that strategy.
[2789] You want to sort of pay
some attention to the brain,
[2792] but you still have
some strategies.
[2793] Like you could say,
well, I'm going
[2796] to talk like my brain
inspired, but I don't actually
[2800] want to care if the things
align much with my measurements.
[2803] As long as I can say
this is neuro-inspired,
[2805] it's really good for
my advertising and PR
[2808] to say I've got a neuro-inspired
system if it's just
[2811] loosely inspired.
[2812] And I guess you can do that.
[2814] I'm frankly not a
big fan of that.
[2815] In fact, I'd rather you
do number one and say,
[2817] I'm just doing good systems.
[2819] But you could also
say, well, I'm
[2821] going to use human
performance as a benchmark.
[2823] This is not yet up
to human performance,
[2824] but I'm going to
report relative that.
[2826] That's better, because
you're essentially
[2828] starting to use the biology
as measurement behavior,
[2831] as a marker of how you're doing.
[2834] But it's not going
to provide, maybe,
[2835] that strong of a constraint
that you just say, you know,
[2838] where 90% of humans
or something.
[2839] It just gives you a number.
[2841] It's good for
advertising and PR,
[2842] again, if you're a system
builder for AI systems.
[2845] Another way to go, which is
more of a neuroscience way,
[2848] is you say, look, I'm
not a AI researcher.
[2849] I'm going to study simple neural
systems, kind of like phages
[2853] were studied for DNA.
[2855] You figure out how DNA
works in a phage, a virus,
[2858] before you work on
eukaryotic cells.
[2861] The same idea in neural systems.
[2863] You work on some small system--
maybe it's a C. elegans,
[2866] or maybe it's a
fly, or maybe it's
[2867] a rodent-- something
that's smaller.
[2869] And you hope that you
can get some principles--
[2871] quote "principles--"
that somehow you're
[2873] going to scale up.
[2875] That's not an
unreasonable approach.
[2876] In fact, it's the
classic approach
[2878] in biology because of
histories like DNA.
[2881] I'm a little bit skeptical as
to whether that's going to work
[2883] to a great degree in these
very complicated systems,
[2886] but I don't--
[2886] I think it's a reasonable way
to go, and some of that work
[2890] should continue to be done.
[2891] The last approach
is the one I favor,
[2893] which is what I tried
to present to you today.
[2895] I'm calling this forward
engineering, which is basically
[2898] building scientific
hypotheses within, I'll say,
[2901] wisely chosen brain
science measurements.
[2903] Means you can't match
everything in the brain,
[2905] but you make some
guesses about the match.
[2908] You build systems, you
check their alignment up
[2910] at the behavior of
the neural level,
[2912] you look for tested deviations
for some measurements
[2914] as you build them, and
you adjust the system
[2916] building directions if
the deviations are growing
[2918] rather than shrinking.
[2919] So this is that loop
between science measurements
[2922] and engineering that
I was describing
[2923] where you're trying
to build sort
[2924] of an engineered copy of
the system, if you will.
[2927] That's a way to think
about it, an emulation
[2930] model of the system.
[2931] This is actually the
approach we're mostly taking.
[2934] It's engineering in the
service of science--
[2936] this is what I call
reverse engineering--
[2939] with the goal of
scientific hypothesis.
[2941] The advantage of this is--
[2943] its disadvantage is,
it doesn't always
[2945] have good intuitions
about like area number 4,
[2947] where you have intuitions
about principles.
[2950] But it has the ability
to actually make
[2952] advances in things like neural
control, which could then
[2954] lead to things like
human health, education,
[2956] and brain-machine interfaces.
[2958] So in some sense, it's
like the safe strategy
[2960] to build systems in this way.
[2962] The small bonus is, you
actually get this to work,
[2964] then you're helping to
solve one of the greatest
[2966] problems in the
history of our species,
[2968] which is Teuber and Crick's
Astonishing hypothesis-- how
[2973] do the transistors, how of
the mechanisms of neurons
[2975] give rise to our
intelligent abilities?
[2978] Not just that they
do, but how do they?
[2980] And that's really one
of the greatest problems
[2982] in the history of
the human species
[2984] to be solved as a science,
a great science question.
[2988] OK.
[2988] So that's some perspective,
again, coming out of it
[2990] from an AI point of view.
[2992] And I'm just going to
end there and leave you
[2996] guys with a lot of that
thought material to say,
[2998] like I'm happy to talk
about any of the things
[3000] that I've put up as more
teasers along the way,
[3002] including this one.
[3003] I'm also happy to
go on and talk more
[3006] about some of the recurrence
work or my ideas there.
[3008] But again, I think
you've heard some of that
[3010] from Koh and Tiago, so I don't
want to re-tell you things
[3013] that you've already heard about.
[3014] So let me just
pause there and see
[3016] where you guys want to go
with the next 15 or 20 minutes
[3018] we have left.
[3019] Thank you.
[3021] [APPLAUSE]
