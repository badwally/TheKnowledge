---
schema_version: 1
id: yt-zrLulOXryVA
type: youtube
title: Successes and Failures of Neural Network Models of Hearing
url: https://www.youtube.com/watch?v=zrLulOXryVA
authors:
- MITCBMM
ingested_at: '2026-06-01T19:55:48Z'
content_hash: sha256:d5d676d282c76441ded914225eeb1e6b833ad572500085d46027be8069a316d2
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: MITCBMM
  channel_url: https://www.youtube.com/@MITCBMM
  duration_seconds: 3494
  caption_track: fetched
  snippet_count: 1432
filter:
  score: 0.75
---
[0] HECTOR PENAGOS: It is my
pleasure to have Josh here.
[3] And as many of you know, he's
taken a really cool approach
[6] to studying human hearing from
a computational perspective,
[10] building on neural
network models
[13] to try to infer mechanisms
that can give rise
[16] to different hearing phenomena.
[19] Today, he's going to
tell us about successes
[21] with this approach
and some challenges
[23] that he continues to
work on in his lab.
[27] Let's try to keep
this interactive.
[29] This is a Zoom meeting format.
[31] So you can unmute yourself
and ask a question
[34] as Josh is presenting.
[36] There will also be a
Q&A session at the end
[39] so that we allow
Josh time to finish
[41] what he's prepared to
present, and we don't
[43] get stuck at any given point.
[44] But feel free to ask questions.
[46] And, Josh, by all means,
you tell us when to stop
[50] and when to continue.
[52] So I'm going to turn
it over to Josh now.
[55] Thanks.
[56] JOSH MCDERMOTT: All right,
thanks a lot, Hector.
[58] Thanks, everybody, for coming.
[60] So I'm going to
tell you about some
[62] of our recent progress
and roadblocks
[66] in using neural networks
to build models of hearing.
[70] So the problem that
we're interested in
[73] is deriving
information from sound.
[76] And so I usually start by
playing people some sounds,
[78] so just listen to
this audio signal.
[82] [AUDIO PLAYBACK]
[82] - Much nicer because it
doesn't know when [INAUDIBLE]
[86] - Yeah, it's great.
[87] - It's-- everyone [INAUDIBLE]
had a place to go [INAUDIBLE]
[90] And so many people--
[90] I used to hang out
with a friend of mine--
[92] - Are you using the app that
determines what [INAUDIBLE]
[97] [END PLAYBACK]
[97] JOSH MCDERMOTT: OK, so that's
just some everyday audio,
[99] just something I
recorded on my phone.
[101] And the point of
playing you that
[102] is that, just by
listening, you're
[104] able to tell that that
was a recording that
[105] was made in a cafe.
[107] You could hear the
voices of people talking,
[109] tell that a couple
of them are women.
[111] You can hear a man.
[111] You could distinguish
their accents.
[113] You can hear the music
in the background,
[115] the dishes clattering,
all that stuff, right?
[117] And so what was happening is
that there was a waveform that
[120] made its way to your ears.
[121] It caused a particular pattern
of pressure displacements
[123] inside your eardrum
like that shown here.
[126] And just from that pattern of
the way that your eardrum was
[129] wiggling back and
forth, you were
[130] able to tell all
those things that
[132] were going on in the world.
[133] So it's a pretty remarkable
computational feat.
[137] But on the other hand, human
hearing is quite fragile.
[140] So it's probably, like, the
most common sensory deficit,
[143] which is that as people--
[144] typically, as they age,
also with noise exposure,
[147] you lose your hearing.
[148] So this is a graph that kind
of shows the average audiogram
[151] as a function of age group.
[153] And you can see that if you're
in your 20s and 30s, like,
[157] things are pretty good.
[158] But then after that, on average,
your hearing steadily degrades.
[162] And so this is a plot of
your detection threshold
[165] as a function of frequency.
[166] And so especially
at high frequencies,
[168] hearing loss becomes extremely
common by the time you're
[171] in your 70s, 80s, or 90s.
[174] We have treatments for hearing
loss, which is hearing aids.
[176] They help people in quiet, but
less so in noisy environments.
[181] So typically, if people have to
go into a restaurant or a bar,
[184] they'll have a
hard time hearing.
[185] And even those of us like
myself who are middle-aged
[190] will have a harder time than
we did when we were in college.
[193] And our inability to
develop the treatments
[196] for hearing impairment is really
limited by an understanding
[199] of how we hear.
[199] Like, we don't really
understand how our brain takes
[202] the input it gets from the ear
and does the interesting things
[205] that we do with sound.
[206] And so it's a little hard
to know how to fix it.
[208] So our research group
is called the Lab
[210] for Computational Audition.
[211] And really, our number
one kind of long-term goal
[213] is to build good predictive
models of human hearing.
[216] So we'd like to end up with
a computer program that
[218] will take audio as
input and then make
[221] good predictions
about what a person is
[223] going to hear when they get
that audio into their ears.
[226] And we think if we were
successful in that goal,
[228] it would transform our ability
to make people hear better.
[233] So from where I sit, the
peripheral auditory system,
[236] by which I mean the ear
which includes the cochlea,
[239] is fairly well characterized.
[240] So sound comes in through
the outer ear, gets
[247] funneled through the ear canal.
[248] It causes your eardrum to
vibrate back and forth.
[250] Those vibrations are transmitted
through these three tiny bones,
[253] through this thing that
looks like a snail.
[255] That's the cochlea.
[256] It's the sensory organ does
the transduction in hearing.
[259] And we've got pretty
standard and widely accepted
[261] models of that part of
the auditory system.
[265] So typically, there's
a sound signal.
[267] And then that gets
passed through a bank
[269] of bandpass filters,
because one of the signature
[271] properties of
cochlear transduction
[272] is that it's frequency tuned.
[274] There's typically
nonlinear operations.
[277] And that culminates in a
representation we'll often
[280] refer to as a cochleagram.
[282] And we commonly will look at
that representation as an image
[288] where you have frequency on the
y-axis and time on the x-axis.
[291] And then the gray level
here represents the energy
[294] at that point in time,
or the firing rate that
[296] would be coming out of
that particular channel
[298] in your auditory nerve.
[299] So this is a cochleagram that
we made for recording somebody
[302] drumming.
[303] [DRUMMING]
[305] And we kind of think
of this picture as,
[307] like, what your ear is
sending to your brain.
[310] So as I said, the models of
the peripheral auditory system
[313] are pretty widely accepted.
[315] There's lots of different
variants of them.
[317] And you work with
different variants
[318] depending on your purposes.
[320] But that's a pretty
well-understood part
[321] of the system.
[322] So mostly what we worry about
is what happens downstream.
[326] And so over the past five
years or so, my group
[328] has spent a lot of
time asking whether we
[332] can obtain better models
of the auditory system
[335] by training systems
to perform tasks.
[337] That has been
enabled in large part
[339] by the revolution that's
happened in engineering
[341] that everybody here knows
about, which is that we can now
[344] get pretty good performance on a
variety of classification tasks
[348] with artificial neural networks.
[350] So these systems have
repeated applications
[352] of pretty simple operations.
[354] And the parameters can
be optimized to classify
[357] input signals pretty well.
[359] So the approach that
we generally take
[361] is to hardwire a
model of the cochlea
[364] to be faithful to
biology, on the grounds
[366] that we have a fair
amount of knowledge
[368] of what that stage of the system
is doing and how to model it.
[372] And then we generally learn
all the subsequent stages
[374] with a neural network.
[375] We consider the result
as a candidate model
[378] of the auditory system.
[380] So everybody knows
that similar approaches
[382] have been fruitful
in the visual system,
[384] in particular in predicting
responses in the visual cortex
[387] and predicting
aspects of behavior.
[389] We thought that they
would be particularly
[391] useful in the auditory system
where, by contrast, the cortex
[395] was not very well understood.
[396] And we didn't really have
any previous good models
[399] of behavior.
[401] So there are lots of widely
discussed limitations
[403] to this approach that everybody
here, I think, has heard about,
[406] so I won't dwell on them.
[408] But the fact is that
for now, if you really
[410] want to approach aspects
of human behavior and brain
[413] responses, it's
pretty hard to avoid
[415] dealing with neural networks.
[417] And so it's important to
understand and appreciate
[421] and think about the limitations.
[422] And we certainly spend a
lot of time doing that.
[424] And then we will
spend the second half
[426] of the talk talking about
some of the limitations
[428] that we have hit upon.
[430] But it's been an
exciting approach
[432] that we've tried to mine.
[436] So the plan for what I was going
to talk about today to kind of
[439] have two parts of the talk--
[440] I mean, the first
part, I was going
[442] to give you a summary of
some of the recent successes
[445] of our neural network
models of hearing,
[447] mostly in terms of their
ability to account for a pretty
[450] broad range of human behaviors.
[453] And then in the second part,
I was going to talk about some
[455] of the shortcomings
that we have come across
[458] and some of the exploratory work
we've been doing in that domain
[461] to try to understand
those shortcomings,
[463] figure out how to fix them.
[465] So just in case I don't
get through everything,
[467] these are the take-home
messages from the first part.
[470] Overall, after you train neural
networks on natural auditory
[475] tasks using natural
sounds, across the board,
[477] we find pretty good matches to
human behavioral experiments.
[480] And this is now evident in a
bunch of different domains.
[484] The recognition of speech and
noise, sound localization,
[487] pitch perception.
[488] We've also done some
experiments on music recognition
[490] I will talk about.
[492] And one of the things
that we've done with this
[494] is we've manipulated
the training conditions.
[496] And doing this shows that the
similarity that you observe
[499] between the model
on human behavior
[501] is really a function of
optimization for natural tasks
[504] and natural sounds in
a biological cochlea.
[507] And so if you alter those
tasks or sounds or cochlea,
[510] you tend to no longer see
the behavioral similarity
[513] to the same extent.
[514] And this can be useful in
that it provides insight
[516] into the origins of
human behavioral traits.
[518] So that's kind of one
application of that.
[522] The other thing I'm going to--
[523] I'll show you is that
degrading simulated cochlear
[526] input in order to simulate the
effects of hearing impairment
[530] on the ear.
[531] If you degrade the input
to the neural network,
[533] it tends to reproduce
the characteristics
[535] of human hearing impairment, OK?
[536] And so we have really
the first models
[539] of human hearing impairment that
can actually perform behaviors.
[543] So we think those will be useful
in a bunch of different ways.
[545] So this is what I'm going to do
in the first part of the talk.
[549] So the question that we
initially started to ask
[553] was whether trained neural
networks can replicate human
[555] behavior.
[557] We were naturally drawn
to speech recognition
[559] because it's an
important human behavior.
[561] And it's one where there
were lots of labeled corpora.
[564] So we've trained
a lot of networks
[566] to recognize speech
and background noise.
[569] We'll take excerpts of
speech, superimpose that
[571] on different kinds
of background noise.
[573] And the task that
we have mostly used
[576] is to report the
word that occurs
[578] in the middle of the clip.
[579] And there are a lot of reasons
why we chose that task.
[582] One is that it's a task that
you can ask a person to do.
[586] And this is what
one of the stimuli
[587] is like-- so
there's some speech,
[589] and you have to say
the word that occurs
[591] in the middle of the clip.
[592] In this example, the person
will say gross domestic product
[594] group.
[595] And the answer will be domestic.
[596] [AUDIO PLAYBACK]
[597] - --gross domestic
product grew one--
[599] [END PLAYBACK]
[599] JOSH MCDERMOTT: All right, and
in different variants of this,
[602] there have been different
numbers of words,
[603] but there's always a lot.
[604] You know, in this
case, it was 600.
[606] In more recent versions, it
was more like 800 or 1,000.
[610] The methodology that we
used to build these models
[612] is pretty standard.
[613] So the weights are learned
with backpropagation.
[616] We typically do some
kind of optimization
[618] over the architectural
hyperparameters.
[620] I mean, one of the
big things that we
[622] impose on these models which
is not entirely uncontroversial
[626] is convolution in both
time and frequency.
[628] And so nobody really
has too much difficulty
[631] with convolution in time.
[632] But convolution in
frequency is not obviously
[634] a very natural
choice for sounds.
[637] And it turns out that that
is actually pretty useful
[639] to do if you're trying
to build models.
[641] And in fact, I'm
going to come back
[642] to that towards the
end of the talk.
[644] And so our initial
work in this domain
[646] was led by Alex
Kell and Dan Yamins.
[650] And these behavioral
experience were
[651] run by Erica Shook,
who was an undergrad
[653] in the lab at the time
through the CBMM MSRP program.
[657] So I'm going to show
you what happens
[659] with humans when they have to
recognize speech and background
[661] noise.
[662] There'll be a bunch of
different conditions, which
[663] are different
types of background
[664] noise and different
signal-to-noise levels.
[667] And here's what the graph
is going to look like.
[670] So this is going to
plotted in proportion
[672] correct as a function of
signal-to-noise ratio.
[674] So as you go from left
to right, the speech
[678] is essentially getting
louder relative to the noise.
[680] And you'd expect that it
should get easier to recognize.
[683] And indeed, that's
true, but there's
[684] different lines here for
different types of background
[686] noise.
[686] And you can see that it's a
lot easier to recognize speech
[689] when it's superimposed
on music than if it's
[691] superimposed on babble, which
is kind of like crowd noise.
[693] All right, so this is
just what humans do, OK?
[696] And so we then ran the model
on the exact same experiment.
[699] And the results of
that are shown here.
[701] And there's really two points
to take away from this.
[703] One is that the model is overall
matching human performance
[707] in this domain.
[708] In fact, it's doing
a little bit better.
[709] But the other thing is that
the relative performance
[711] of the different conditions
is pretty similar.
[713] So the model also does
a lot better with music
[715] than it does with
speech babble, OK?
[717] And the key point to make here--
and this is true for everything
[720] that I will show you--
[721] is that there's no fitting of
the model to human behavior,
[725] right?
[725] What happens here is you train
the model to perform a task.
[728] In this case, the
model was trained
[730] to recognize speech and noise.
[732] And then it is tested.
[734] And this is just
what it does, OK?
[736] And the results look
fairly similar to humans.
[739] And in fact, if you plot the
proportion correct of humans
[743] on the task versus the model
proportion correct on the task
[745] for all the different
conditions--
[747] each dot's a different
condition here--
[748] they're pretty
strongly correlated.
[751] OK, so this was one
of the first examples
[753] that we found in this
domain that was published
[756] a couple of years ago.
[758] We've since moved on to
other auditory behaviors.
[760] One of the other really cool
things that we do with sounds
[763] is localize them.
[764] So localization with sound
is pretty interesting
[767] because, unlike in
vision, a sound's location
[770] is not made explicit on the
sensory receptor epithelium.
[774] So you get this map of
frequency in your cochlea.
[778] And if a sound comes from
a different location,
[780] that's not really laid
out on the cochlea
[782] in a straightforward way.
[784] But it's something that has
been studied scientifically
[786] over a very long time.
[787] It's in all the textbooks.
[788] And the classical story is
that there are three main types
[791] of cues to a sound's location.
[793] So if the sound is coming
from the right, in general,
[796] it will arrive first
at the right ear
[798] compared to the left ear.
[800] And that produces
a time difference
[802] between the left
and the right ear,
[803] here shown in red and blue.
[805] There will also be
level differences,
[807] and that's because your head
casts an acoustic shadow, such
[810] that the intensity of the
sound at the right ear
[812] will generally be higher than
the sound at the left ear.
[815] And then your ears
have this funny shape.
[817] And the thing on the outside of
your ear is called the pinna.
[820] And the funny shape
of the ear filters
[822] sound in particular ways.
[824] And that filtering is
different depending
[826] on where the sound comes from.
[827] So if it comes
from above, you'll
[829] get a particular kind
of transfer function.
[831] If it comes from below,
you get a different kind
[832] of transfer function, OK?
[834] And so we believe that
people have learned
[836] to recognize that
filtering and use that
[839] in order to localize sounds
in the vertical range, OK?
[843] All right, so that's
the textbook story.
[846] But in real-world
environments, there's noise.
[848] There's reflections.
[849] Reflections pose a particularly
interesting problem
[851] because if you think about
it, if there's a sound coming
[854] from a particular
place, if the sound that
[857] comes from that
source reflects off
[859] a surface in the
environment, that reflection
[861] will arrive from the wrong
direction, all right?
[863] So reflections actually
really provide erroneous cues.
[867] So in general, localization
in real-world conditions
[869] is a hard problem.
[870] And we've never really had
models that can actually
[872] localize sounds, OK?
[875] So Andrew Francl, who is
a grad student in the lab,
[879] he has been trying to build
models of sound localization
[882] using neural networks.
[884] And to get around the
necessity of needing
[888] lots of labeled data,
he's trained the model
[890] in a virtual environment.
[891] So this is a schematic
of how that works.
[894] So you have natural
sound sources--
[896] that's shown in red--
[897] noise sources which
are shown in black.
[899] And then those are rendered
in an acoustic simulation
[902] of a room.
[904] So there's a virtual person
with two ears, who's positioned
[907] at a particular location.
[909] And the source is at
a particular location.
[911] And then we simulate what
the room does to the sound.
[914] So you simulate all the
reflections and stuff.
[916] And what that gives you
are two audio signals that
[920] should replicate
what the audio would
[923] be in the ears of a person
that was in that room listening
[926] to those sounds.
[928] So you get left-ear
and right-ear signals.
[930] You pass those through
model of the cochlea.
[932] And then that's the input
to a neural network that
[935] has to report the azimuth--
[937] that's the location in
the horizontal plane--
[939] and the elevation
of the sound, OK?
[942] So Andrew set this whole
thing up, and he trained it,
[945] and the model trains.
[946] And then one of the
kind of cool things
[947] is that even though it's trained
in the virtual environment,
[949] it generalizes to the
real world, by which we
[951] mean building 46.
[953] So this is a mannequin
that's relaxing
[955] in a chair in our lab space.
[957] And it's a very
special mannequin
[958] that has microphones
inside its mannequin ears.
[962] And so you can make
recordings of what
[964] sounds sound like coming
from particular locations
[967] in this particular room, OK?
[970] So Andrew created a test set
from the mannequin recordings
[975] and then provided those
as input to the model.
[977] And you can see that the
model does pretty well.
[979] So the judgments here are
largely along the diagonal, OK?
[983] All right, so
that's kind of cool.
[985] We have a model of
sound localization
[986] that actually works in
real-world conditions.
[989] But then what he did is
he went and reproduced
[993] a lot of experiments from
the literature on the model.
[996] So people been studying
sound localization
[998] for a really, really long time.
[999] And there's a very rich panoply
of experimental results.
[1003] And overall, the findings
are that the model generally
[1006] reproduces human results
across a pretty wide range
[1009] of experiments.
[1010] And I'll just give you a
couple of the highlights here.
[1013] So one of the classic things
that you find in textbooks
[1016] is that the use
of time and level
[1020] differences between the two
ears is frequency dependent.
[1023] And this is classically
referred to as duplex theory.
[1025] So the classical
story is that humans
[1028] rely on interaural time
differences at low frequencies
[1032] and interaural level differences
or intensity differences
[1034] at high frequencies.
[1036] And so this is an e--
[1037] one of many, many,
many experiments
[1039] that provided evidence for this.
[1041] And so in this
experiment, people
[1043] were presented with noise
that was either low pass--
[1046] so this is, like, a schematic
spectrogram of the noise.
[1049] So this one's got low
frequencies here--
[1050] or high pass, all right?
[1052] And then the noises
are rendered spatially.
[1055] And then the
experimenter secretly
[1058] adds an additional level
difference or time difference
[1061] to the stimulus, OK?
[1063] And then what you ask
the participant to do
[1065] is to localize the sound.
[1067] And the question is whether
the added time or level
[1070] difference will change their
perceived location, OK?
[1074] And so you get these
graphs that plot
[1076] the imposed bias for
either the ITD or the ILD
[1081] versus the response, OK?
[1084] And so what you find
here is that in humans,
[1086] for high frequency stimuli, the
level differences that you add
[1090] have a big effect on
their localization,
[1094] whereas the time
differences don't.
[1095] And the reverse is true for
low frequencies stimuli.
[1098] So the time difference
really has a big effect,
[1100] and the level
difference doesn't, OK?
[1102] And there is a classical
story that that's
[1104] because that's usually
the places where
[1108] these cues are useful.
[1110] And the model largely
reproduces that.
[1112] So it is strongly affected
by added level differences
[1115] for high-frequency
stimuli and strongly
[1117] affected by time differences
for low-frequency stimuli, OK?
[1121] Another kind of
classical finding
[1123] is that people really
rely on their outer ears
[1126] if they are localizing
in the vertical plane,
[1129] but not in the horizontal plane.
[1131] So this is a really
beautiful study from 1998
[1135] from the group of
John Van Opstal, where
[1138] they brought people in the lab,
and they measured their ability
[1141] to localize.
[1142] And then they put these
plastic ear molds in their ear.
[1145] And the purpose of
the plastic ear molds
[1147] is to alter the way that
the ear filters sound.
[1150] So this was an attempt to test
whether people are actually
[1153] using the filtering
in their ears.
[1156] And so what you
can see in panel B
[1158] is human localization
before you put the molds in.
[1161] And so these dashed lines are
a grid of locations in space.
[1165] And then the solid lines
depict human localization.
[1169] And the point is that the
solid lines are kind of
[1171] on top of the black lines, which
means that people are accurate,
[1173] right?
[1173] People can accurately
localize sounds.
[1176] Panel C is showing
what happens when
[1178] you put these plastic
molds in people's ears.
[1180] And what's cool is that people
retain the ability to localize
[1184] in the horizontal plane,
but they completely
[1186] lose the ability to
localize in elevation, OK?
[1190] And so this is an
indication that these people
[1193] have learned to use the
particular filters that
[1195] are in their ears.
[1196] And so Andrew was able to
reproduce this experiment
[1198] with the model
because the model was
[1200] trained on a particular set
of ear filters, all right?
[1205] But then he can take
another set of ear filters
[1207] and swap that in and
test the model on that.
[1209] And so this is what happened.
[1211] And you see more or
less the same thing
[1212] that you see with humans, which
is that the model localizes
[1215] accurately when you test
it with the set of ears
[1217] that it was trained on.
[1220] But then when you swap in
a different set of ears,
[1222] it retains the ability
to localize in azimuth--
[1224] so that's the horizontal plane--
[1226] but it loses the ability
to localize in elevation.
[1230] So, one other final example
that I'll leave you with
[1233] is this thing called
the precedence effect.
[1235] So this is a well-known effect
in sound localization, whereby
[1240] the very first part
of the sound tends
[1242] to dominate your
perception of the location.
[1245] And the classical
example of this
[1247] was discovered by Hans Wallach,
who was a great Gestalt
[1250] psychologist who also
did a lot of work
[1251] on human motion perception
and many other great things.
[1255] But he's also known for
the precedence effect.
[1258] And the setup here is that you
have two speakers, like one
[1261] to the left, and
one to the right.
[1262] And the speakers
just play clicks.
[1264] And one of them is leading--
[1266] that means that the click comes
out of this speaker first,
[1268] and the other one is lagging.
[1270] So there's a slight time
delay between the clicks.
[1273] All right, and the
phenomenon here
[1275] is that when the delay between
the two clicks is short,
[1278] so less than 10 milliseconds
or so, in general, people
[1282] were report hearing
a single sound.
[1284] And the location that they hear
is that of the first click,
[1288] all right?
[1288] So that's why it's called
the precedence effect.
[1290] The click that
precedes is the one
[1293] that dominates your
localization, OK?
[1294] So if you ask them to tell you
the location they perceive,
[1298] they'll report 45 degrees,
which in this case,
[1300] is the location of
the leading click.
[1302] And then at some point,
that breaks down.
[1304] OK, all right, now,
this has been widely
[1307] hypothesized to
be something that
[1309] is an adaptation for dealing
with reflections, the idea
[1312] being that when sound is
reflecting off of surfaces
[1315] in the environment,
well, the sound that
[1316] comes direct from the
source is generally
[1318] going to get there first because
that's the shortest path.
[1321] And so if you get delayed
copies of the sound,
[1323] those might be reflections.
[1324] And so your brain
might have learned
[1326] to suppress them in some way.
[1329] So it's a well-known effect
in human sound localization.
[1331] And the model
replicates that too.
[1333] So this is the graph
that shows that.
[1335] So the judged location here is
dominated by the leading click
[1339] when the delays are short.
[1341] And then the effect
kind of goes away.
[1343] OK, so we've also got
kind of analogous results
[1346] in pitch perception.
[1347] In this case, these
are models that
[1348] are trained to report
the fundamental frequency
[1351] of natural sounds superimposed
on noise, where you can take
[1354] a whole panoply of classical
psychophysical experiments,
[1357] replicate them on the model.
[1359] And in general, it
tends to qualitatively
[1361] and, in many cases,
quantitatively reproduce
[1363] how humans hear.
[1365] All right, so from
my perspective,
[1368] this is a big advance over
previous models, in that we're
[1371] getting human-like behavior
out of our auditory models
[1373] for the first time.
[1374] And this occurs in realistic
conditions, in many cases,
[1377] with comparable accuracy.
[1379] They exhibit similar
psychophysics, which
[1380] suggests similar use of cues.
[1383] And one of the
interesting things
[1385] that we've done
with this is to use
[1387] this phenomenon, the fact that
we get these behavioral matches
[1390] between the model and
humans, to investigate
[1393] the conditions that give
rise to human-like behavior.
[1396] So in particular, we've asked
whether this similarity that we
[1399] often observe depends on the
statistics of the environment
[1402] or on the properties of the ear.
[1405] And the way that
you do this is you
[1406] can train the model in
alternative conditions, right?
[1409] So for instance, with these
pitch perception phenomena,
[1411] we instead trained our models
on unnatural synthetic tones
[1415] instead of--
[1416] in this case, it was
clips of speech and music.
[1419] And again, you're not
going to understand
[1420] the details of
these experiments,
[1422] and it doesn't really matter.
[1423] [INAUDIBLE] It's just a
bunch of effects which,
[1424] if you were into
pitch perception,
[1426] you would understand and love.
[1429] But the key point
here is to just notice
[1431] that when I flip between
these two slides--
[1433] so this one is the
result of the model that
[1435] was trained on natural sounds.
[1437] And this is the model that's
trained on the synthetic tones.
[1440] You can get really
different results.
[1443] So the model is solving the
same problem in this case.
[1446] But it seems to be doing it
in a very different way that's
[1448] really unlike the way
that humans solve it,
[1451] presumably because humans are
optimized for natural sounds
[1454] in some sense.
[1456] And so these kinds of
models give us a way
[1457] to actually evaluate that.
[1459] And we've got somewhat
similar kinds of results
[1461] for sound localization.
[1463] So what Andrew did is he
took his virtual training
[1466] environment and altered
it in various ways.
[1468] And he did three
different things.
[1470] One is that he got
rid of reverberations,
[1472] so he removed echoes.
[1473] So that's anechoic training.
[1474] So that's like if
you lived in a world
[1476] where every surface
would completely absorb
[1479] the sound that impinged on it.
[1482] He also removed
background noise.
[1484] So you can keep all
of the reverberation,
[1485] get rid of the
background noise, or you
[1487] can make the sounds unnatural.
[1488] So bandpass noise in
this particular case.
[1491] And so these are models
that are trained up
[1493] in these alternative worlds.
[1495] And you think of this as,
like, simulating evolution
[1497] and development in some
alternative universe.
[1500] You can then bring
the model into the lab
[1502] and run it on this same
set of experiments.
[1505] And so this is a summary graph
that shows the human model
[1509] dissimilarity across a big
set of experiments, OK?
[1512] So lower means you have a
better fit to the human data.
[1516] And the light blue bars is
training in normal conditions.
[1520] And then the other three bars
are these three alternative
[1523] virtual worlds.
[1524] And you can see that in
each of these three cases,
[1526] you get a worse fit
to the human data.
[1529] And in many cases, these
divergences are interpretable.
[1532] And so I'm just
going to show you
[1533] the one that is our favorite.
[1536] So this is the results of
that precedence effect.
[1538] So again, this is where
localization is really
[1540] dominated by the leading sound.
[1544] And the blue curve is the
one that I showed you before.
[1548] And then the other three
curves are these three
[1550] alternative environments.
[1551] And so you can see
that two of them
[1553] largely reproduce the effect.
[1556] And one of those is the
thing that has no noise.
[1558] And the other one is the
thing with unnatural sounds.
[1560] And then the one that looks
really, really different
[1563] is the anechoic training.
[1564] So if you train a
system in conditions
[1567] that do not have
reflections, you actually
[1569] lose the precedence
effect, which
[1571] provides pretty nice evidence
that this particular perceptual
[1575] effect is, in fact, some
kind of adaptation to deal
[1578] with the presence
of reflections when
[1580] you have to localize sounds.
[1582] All right, I'm going to
just pause for one minute
[1584] and ask if anybody
has any questions.
[1587] PRESENTER: It's from
[INAUDIBLE] He's
[1589] asking, is it possible that the
sound volume confuses the model
[1592] when detecting the
sound source distance?
[1594] JOSH MCDERMOTT:
Not sure under what
[1596] conditions you are
referring to that.
[1598] I mean, in the virtual training
environment, of course the--
[1602] I mean, the sound volume is sort
of appropriate for the distance
[1605] at some level.
[1605] I mean, all that
stuff is kind of
[1607] rendered correctly insofar
as the simulation is correct.
[1613] And so the model should
be learning some of that.
[1615] I mean, like, in
this version of this,
[1618] we didn't use a big
range of distances.
[1622] But in principle,
that's just something
[1624] that-- that's another thing
that it should learn to use.
[1628] And in the-- I mean, in the
psychophysical experiments,
[1630] you don't really see any signs
that that's causing problems.
[1635] And one of the things,
I guess, that is--
[1637] that's kind of interesting about
these results is that you're
[1644] getting human-like
behavior with some pretty
[1647] weird psychophysical
stimuli that were dreamed up
[1651] by an experimentalist
at some point
[1652] because they thought they'd
test at some kind of hypothesis,
[1655] you know?
[1657] So the model is trained
on natural sounds,
[1659] but it does exhibit
generalizations
[1661] to certain kinds of sounds
that are not obviously
[1665] in the training distribution.
[1669] So that's kind of mostly what
I've got to say about that.
[1672] OK.
[1672] AUDIENCE: I have a question
about the cochleagram.
[1675] So is it-- have you
tried to train this model
[1679] without using the cochleagram?
[1680] And were the results worse?
[1683] JOSH MCDERMOTT: Yeah,
it's a good question.
[1685] We have done-- we've done lots
of variants of that where--
[1694] you know, we've certainly
altered our cochlear model
[1696] in lots of ways.
[1697] So for instance, if you--
[1701] in these models that
are trained to estimate
[1703] fundamental frequency that
we use to account for pitch
[1705] perception, if you degrade
the timing information
[1710] in the cochlear model,
you tend to get abnormal,
[1714] like inhuman results,
from that, which
[1716] is some evidence that human
pitch perception really
[1720] depends on the fine
timing information that's
[1722] coming out of the cochlea.
[1724] So there's lots of things
that are kind of like that.
[1730] But I think you might
have been asking, well,
[1732] have you just gotten rid
of the cochlear model
[1734] entirely and tried to
learn from the waveform?
[1737] Is that what you're
asking about?
[1739] AUDIENCE: Yes.
[1740] JOSH MCDERMOTT: Yeah, so we've
done a little bit of that.
[1742] And yeah, in
general, things tend
[1746] to be worse, although
you can often
[1749] do fine on the training set.
[1751] But the generalization is
often funny in various ways.
[1755] You know, we haven't explored
that in great detail,
[1759] in part because, again, it's--
[1760] I mean, it's an
interesting question,
[1762] but from the standpoint
of building models
[1764] of the auditory
system, we think we
[1765] have a pretty good idea of
what should go in for the ear,
[1768] you know?
[1768] And so it's not
obvious that that's
[1773] the greatest idea from
the standpoint of building
[1775] a model of the auditory system.
[1777] But I agree.
[1777] It's interesting question.
[1780] AUDIENCE: Thank you.
[1782] JOSH MCDERMOTT: OK.
[1783] All right, so I mentioned
that hearing is fragile.
[1790] And the most common complaints
are that-- so we often
[1793] measure hearing impairment by
measuring the audiogram, right,
[1796] and find that the
thresholds are elevated.
[1799] But the most common complaint
of hearing-impaired listeners
[1801] is actually difficulty
hearing in noisy conditions.
[1804] You know, you go to a restaurant
with your grandchildren,
[1806] and you can't hear what
they're saying, or whatever.
[1810] And one of the frustrating
things about that is that we
[1813] don't really understand how
the peripheral impairments that
[1816] we're beginning to understand--
so the changes that happen
[1819] in the ear when people
lose their hearing--
[1821] we don't understand how
those impairments give rise
[1823] to behavioral impairments.
[1824] And that's in part
because we've never really
[1826] had working models that
can actually instantiate
[1829] auditory behavior, all right?
[1830] So we've been attempting to
try to build those models
[1833] in the hopes that we
might be able to use
[1835] them to develop better
treatments for hearing
[1836] impairment.
[1838] And there's a couple
behavioral signatures
[1841] that are measured in people
with hearing impairment.
[1844] And the first is
just what I said,
[1846] which is to say that speech
recognition is usually
[1849] pretty good when the
signal-to-noise ratio is high.
[1853] So that's what's shown
here, where you don't
[1855] have a lot of background noise.
[1857] But there are big deficits
in noisy conditions, OK?
[1861] So this is proportion correct
versus signal-to-noise ratio.
[1863] The solid symbols here are
normal hearing listeners.
[1866] The open symbols are people
with hearing impairment.
[1869] So you can see there's a bigger
gap here at the lower SNRs,
[1872] all right?
[1873] So that's kind of
one common finding.
[1875] And then another is that
normal hearing listeners
[1879] have a much easier
time hearing a noise
[1881] if the noise is modulated.
[1882] So this is the temporal-- the
time waveform of the noise.
[1886] And so you can see these are
amplitude fluctuations that
[1889] are imposed on the noise,
whereas this is just
[1891] stationary noise that has
a pretty flat envelope.
[1894] And so again, this is
the same kind of thing.
[1896] This is percent correct
in a speech recognition
[1898] task as a function of
signal-to-noise ratio.
[1901] But for the dashed line,
the modulated noise,
[1903] normal hearing listeners
do a lot better
[1905] for the equivalent
signal-to-noise ratio compared
[1907] to stationary noise.
[1909] Whereas for
hearing-impaired listeners,
[1911] that advantage pretty
much goes away, OK?
[1915] So again, not really
well understood
[1916] why this happens,
although there are
[1918] various theoretical
explanations.
[1920] So what we've done is
we tried to simulate
[1922] the loss of outer
hair cells, which
[1924] is one type of hearing loss.
[1926] Again, the details here
don't really matter.
[1928] There's a handful
of common traits
[1930] that we associate with the
loss of outer hair cells.
[1933] They include broader
frequency tuning,
[1935] reduced response
to quiet sounds,
[1936] and a narrow dynamic range.
[1937] And we have a way of
instantiating that
[1939] in our models of
the cochlea, OK?
[1942] And then we then swap those
into the neural network model.
[1946] So this is the results
of the normal hearing
[1948] model with a normal hearing
cochlea on that speech
[1950] recognition task.
[1952] So this is proportion correct
versus signal-to-noise ratio.
[1954] The lines are different
types of background noise.
[1957] And then when you swap in
the hearing-impaired cochlea,
[1960] you can see that
things get worse,
[1961] but particularly in the very
noisy conditions, right?
[1964] So the model is almost as good
at what we call clean speech.
[1968] So that's without
any background noise.
[1972] So similarly, we can
reproduce that benefit
[1975] that normal hearing listeners
get for modulated noise--
[1978] so the human graph is
shown here at the bottom,
[1981] and the model graph
is shown at the top--
[1983] if we have a normal
cochlea there, right?
[1985] So the dashed line is pretty
far above the solid line.
[1989] But if we swap in this model
of impaired cochlear function,
[1993] that advantage pretty
much goes away, OK?
[1996] So when we alter the cochlea
to simulate hearing impairment,
[1999] it qualitatively
reproduces the signatures
[2001] of hearing impairment in humans.
[2003] Now one other kind
of interesting thing
[2005] here is that the way
that we did this is we
[2008] trained the neural network
on the normal cochlea.
[2012] And we freeze the
network, and then swap
[2014] in a model of impaired hearing.
[2016] And it's natural
to wonder, well,
[2017] what happens if instead the
neural network is trained
[2021] on the impaired cochlea?
[2023] And what's interesting is
that, at least for this type
[2025] of hearing impairment, when
you do that--0 we call that
[2028] the plastic model of
hearing impairment--
[2030] the deficits
basically go away, OK?
[2033] So you can see that
the relationship
[2036] between the impaired hearing
model and the normal hearing
[2038] model is right on
the diagonal here.
[2042] And the same is true for this
benefit for modulated masking
[2046] noise.
[2047] And so when the neural network
is allowed to adapt itself
[2050] to the altered
ear, it's actually
[2053] able to get pretty
normal behavior.
[2056] And so that is-- it's sort of
intriguing to speculate that,
[2058] well, maybe that is
consistent with the idea
[2060] that aspects of human
hearing impairment
[2063] are due to a lack of plasticity.
[2066] So, you know, your brain is kind
of fixed once you get older.
[2069] And then your ear
changes, and the system
[2071] doesn't have the
ability to change
[2073] to optimize, to reoptimize
itself for the new operating
[2077] conditions.
[2077] But maybe if there was
some way to imbue it
[2079] with sufficient plasticity, you
could fix things a little bit.
[2082] That's total speculation,
but kind of interesting.
[2086] OK, so, and I think-- so we've
also done a whole bunch of work
[2089] to try to use these
kinds of models
[2091] to predict brain responses.
[2093] I've talked about
this lots of times.
[2094] So I'm going to just skip over
that in the interest of time.
[2098] But they do better
than normal models.
[2100] All right, so those are
the take-home messages
[2102] from the first part, which is
to say that, in general, when
[2106] you take neural networks,
and you train them
[2108] on natural auditory tasks
with natural sounds,
[2110] you get pretty good
matches to human behavior.
[2113] And this is in all of the
domains that we've looked,
[2115] so speech recognition and
noise, sound localization,
[2118] pitch perception,
music recognition.
[2120] You can also manipulate
the training conditions.
[2123] And that seems to suggest that
the similarity that you observe
[2126] between these models and humans
is a function of optimization
[2130] for natural sounds and
tasks in the cochlea, right?
[2133] So when you make the
optimization conditions
[2135] unnatural, you tend to
deviate in various ways.
[2138] And that can give you
insight into the origins
[2140] of human behavioral traits.
[2142] And then finally,
I showed you how
[2143] degrading of simulated cochlear
input to the neural network
[2147] can reproduce some of
the characteristics
[2149] of human hearing impairment,
which we think is
[2151] an interesting new direction.
[2153] All right, so what I
want to turn to now
[2155] is a discussion of some
of the model shortcomings.
[2158] And these are the-- this
is the take-home messages
[2160] from the second part, because I
don't get through all of them.
[2163] So I'm going to tell you
about a method called metamer.
[2166] We're going to generate
metamers of neural networks
[2169] and argue that these
provide a way to reveal
[2171] model invariances.
[2173] One of the key findings
from doing this
[2175] is that metamers
of the deep layers
[2177] of standard neural
network models
[2178] are not metameric for humans.
[2180] They're not even recognizable
to humans, which seems
[2183] like a pretty huge discrepancy.
[2185] And this is true for both
vision and auditory networks.
[2188] We have found that
model metamers can
[2190] be made more human-recognizable
with some architectural
[2193] modifications, in this
case, by reducing aliasing,
[2197] and by making models more
robust to adversarial examples,
[2200] for reasons that we
don't fully understand.
[2202] But neither of these
things is sufficient,
[2204] and the divergences
kind of still remain.
[2206] And that is a challenge for now.
[2210] OK, so let's talk
about metamers.
[2213] So metamers are a really old
idea in perceptual science.
[2216] I teach them every year in my
undergraduate perception class.
[2218] They're defined as
physically distinct stimuli
[2221] that are indistinguishable
to the observer.
[2222] The classic example
comes from color vision.
[2225] So these are two spectra
of visible light.
[2227] So wavelength is on the x-axis,
and power's on the y-axis.
[2231] So the one on the left is the
spectrum from a tungsten bulb.
[2234] The one on the right
is a metameric match
[2235] from a color monitor.
[2237] So you can see that
physically, those two spectra
[2239] are completely different.
[2240] But to a human with normal color
vision, they'll look the same
[2243] and, in fact, will
be indistinguishable.
[2245] And the reason for this
is very well understood.
[2247] It's because you have
three types of cones.
[2249] And so you take that
high-dimensional spectrum
[2252] and project that onto
your three photopigments.
[2256] And that projection down
onto the subspace inevitably
[2258] is going to map many different
things onto the same point.
[2262] And in fact, metamers were used
long before we had the ability
[2266] to go poking around
in the eye to infer
[2268] the trichromatic nature
of human [INAUDIBLE]
[2270] So it's a kind of a classical
story in perception research.
[2273] And the idea of metamers has
been revived multiple times.
[2276] Since then, it's often also
been a big part of human texture
[2279] perception, and
then most recently,
[2282] was important in the
understanding of crowding,
[2285] including by our own Ruth
Rosenholtz as well as
[2288] others, Eero Simoncelli
most notably.
[2292] OK, so we got
interested in the idea
[2294] that metamers might
be a useful way
[2296] to try to understand these
neural network models.
[2300] And so the-- you
know, we normally
[2301] think of these-- the recognition
tasks that these kind of models
[2304] are solving as confronting the
challenge of becoming invariant
[2310] in the right ways to all
of the different ways
[2312] in which natural stimuli vary.
[2315] So you learn to
recognize the word "dog,"
[2318] and the difficulty is
that I can say the word
[2321] dog in lots of different ways.
[2322] And you say it in a way
that sounds different.
[2324] Everybody's voice is different.
[2326] Instead of recognize
the word "dog,"
[2327] you have to be invariant to all
of those factors of variation,
[2330] right?
[2331] And it's natural to
suppose that when
[2333] you train the network,
what you're doing
[2335] is imbuing it with
invariances that
[2337] allow it to perform its task.
[2340] And you would expect that
if the network ends up
[2343] being a good model of
human recognition, well,
[2346] the variances
should be the same.
[2348] And so we thought that metamers
generating stimuli that
[2352] would produce the same
responses in the model
[2354] might reveal the
learned transformations
[2356] and could provide another test
of whether the model captures
[2359] human perception.
[2360] So this is work that was led
in lab by Jenelle Feather.
[2364] And the idea is really simple.
[2366] So you have a stimulus that
gets passed through the model.
[2369] And then you have
some activations
[2372] that are induced at
some stage of the model.
[2374] And the goal is to generate a
stimulus that produces nearly
[2379] the same activations, OK?
[2381] So we want to have
a synthetic stimulus
[2382] that, when passed
through the model,
[2384] will give you the
same activations
[2386] at some particular
point within the model.
[2388] And so that is
pretty easy to do.
[2389] You just do gradient
descent on the input signal
[2392] in order to minimize
a loss function
[2395] that you set up between the
activations to the two signals.
[2399] All right, so when
you do this, you
[2401] end up with the synthetic
signal for which
[2404] the model's response in a
particular layer is matched.
[2410] Now, the kinds of
models that we work with
[2412] are feed forward
and deterministic.
[2414] And so if the responses
are matched in one layer,
[2416] they will be matched in
all subsequent layers.
[2418] And then the decision about
the stimulus will be the same.
[2421] So if the model thinks that
this particular speech utterance
[2424] contains a particular
word in the middle,
[2427] it will, by definition, think
that this synthetic signal also
[2430] contains that same
word in the middle, OK?
[2434] And so this is just graphs
that kind of quantify that.
[2437] So if you match on an
early layer, by definition,
[2442] the late layer also
has to be a matched.
[2444] And so these are the
correlation coefficients
[2447] between the activations
of the original signal
[2450] and the metamer.
[2451] But critically, the
same thing is not true
[2454] if you match on a late layer.
[2455] So if you match on a
late layer, in general,
[2458] the response is that the early
layer will not be matched.
[2460] And that's because the
network involves pooling
[2463] and is building up
these invariances.
[2466] And so it's just
the case that you
[2469] can have multiple
distinct stimuli
[2471] will produce the same
responses deep in the network.
[2475] OK, so that's the
central idea, right?
[2477] We're going to be
generating metamers
[2479] from different layers of
these networks, in our case,
[2482] from speech.
[2483] And we're going
to listen to them
[2484] and see what they sound like.
[2485] And so some examples
of that are shown here.
[2488] So these are metamers
that were generated
[2490] from a neural network that's
trained to recognize speech.
[2494] So we take this
original speech signal.
[2496] We measure its activations.
[2497] And then we're going
to synthesize signals
[2499] matching the activations at
each stage of the network
[2503] from very early up
to very late OK?
[2506] And to visualize
the signals, we are
[2509] going to represent them as
their cochleagram, right?
[2511] So this is a spectrogram-like
representation--
[2513] frequency on the
x-axis, time on the--
[2516] I'm sorry, frequency on the
y-axis, time on the x-axis, OK?
[2519] And just from eyeballing
it, you can kind of
[2521] see that as you move
through the network,
[2524] these particular
examples of metamers
[2527] start to look less and less
like the original signal.
[2530] And so that's
consistent with the idea
[2531] that the network is
building up invariances.
[2535] And if you know
anything about audio,
[2536] you will probably intuit that
these signals might-- don't
[2539] look a whole lot like speech.
[2541] And indeed, they don't
sound much like speech.
[2543] And that's kind of the key find.
[2545] So I'm just going to play
you some examples here.
[2548] [AUDIO PLAYBACK]
[2548] - The job security
program that prevents la--
[2550] [END PLAYBACK]
[2550] JOSH MCDERMOTT: All
right, so that's
[2551] from a very early
layer that essentially
[2553] sounds like the original.
[2554] And you can keep going.
[2556] [AUDIO PLAYBACK]
[2556] - The job security program
that prevents like la--
[2559] the job security program
that prevents la--
[2561] [END PLAYBACK]
[2562] JOSH MCDERMOTT: All right,
starts to sound more different.
[2563] [AUDIO PLAYBACK]
[2564] - The job security
program that prevents la--
[2567] the job security program
that prevents la--
[2570] the job security program
that prevents la--
[2572] [END PLAYBACK]
[2572] JOSH MCDERMOTT: And
by the end, it's
[2574] very hard to hear anything.
[2575] [AUDIO PLAYBACK]
[2576] - The job security
program that prevents la--
[2578] [END PLAYBACK]
[2579] JOSH MCDERMOTT: OK, so I should
just emphasize these are--
[2582] each of these is a
signal, an audio signal,
[2585] that produced nearly identical
activations to the clean speech
[2589] signal at the corresponding
layer of the network, OK?
[2592] And so the
consequence of that is
[2593] that they are fully recognizable
to the network by design.
[2596] But what we find is that
they become progressively
[2599] unintelligible to humans.
[2601] So the way that we
evaluate this is actually
[2603] with a recognition task.
[2605] So this is actually
not a test of metamers,
[2607] and it's more
conservative than that.
[2609] We're just asking whether the
human can recognize the speech
[2613] utterance, or the word
in the middle that
[2616] was used to generate it, OK?
[2619] And these are the results and
we verified that the network
[2622] can recognize its own metamers.
[2623] It's supposed to.
[2624] And indeed, it does, right?
[2625] So that's the gray line.
[2627] It's a ceiling.
[2628] So the graph here is
plotting the proportion
[2630] correct versus the
layer of the network
[2633] from which the
metamer was generated.
[2635] And so the green line
here is human performance.
[2637] And so we can see that
from the early layers,
[2640] human listeners can
recognize the speech.
[2641] But then it gets
harder and harder.
[2643] And then by the late
layers, they really
[2644] can't hear anything.
[2646] So this result is not
specific to audio.
[2649] You get qualitatively
similar results
[2650] if you do the same kind of
exercise for vision networks.
[2653] These are three common visual
neural network architectures.
[2657] And these are metamers generated
from this particular image
[2660] from successive layers.
[2661] And by the time you
get to the deep layers,
[2663] you can't recognize them.
[2664] And so I think this
is-- this is not new.
[2666] And indeed, the
synthesis method here
[2668] has been around for a long time.
[2669] There's an early neural
network visualization paper
[2673] that did essentially this.
[2674] But I think the
significance of this
[2677] for the relevance
of these models,
[2680] the perception has really not
been very widely appreciated.
[2684] And it certainly
had been measured.
[2685] So Jenelle went did the
recognition experiment
[2687] on these vision models and found
more or less the same thing.
[2691] So by the time you get
to the deep layers,
[2693] you generate metamers for those.
[2694] And those are not recognizable.
[2698] OK, so it's kind of an
interesting contrast to what I
[2701] was telling you about in the
first part of the talk, where
[2704] I gave you all
these examples where
[2706] we find similar behavior
between the models and humans.
[2710] But those are all
with natural sounds,
[2712] or at least not with incredibly
unnatural sounds, OK?
[2716] So here, we're generating
these signals using the model,
[2719] and we get very
divergent behavior.
[2721] So it seems like a pretty
substantial inconsistency
[2723] with biological
perceptual systems.
[2727] So we've since been using this
to try to evaluate models,
[2730] and also trying
to understand what
[2731] is responsible for this
kind of curious behavior.
[2735] One kind of interesting
finding actually
[2737] relates to biologically
inspired constraints,
[2741] or what some people might argue
are biologically inspired.
[2743] So I mentioned at the start
of the talk that typically,
[2746] when we are building
these models,
[2747] we always impose convolutions
in both dimensions of the input,
[2751] time and frequency.
[2753] And we've found
empirically that that
[2755] tends to make the
models easier to train,
[2757] tends to make
performance better.
[2760] And what Jenelle did with
Christina Trexler, who
[2762] is an undergrad
who was in the lab
[2764] last summer with
the MSRP program,
[2768] is to actually
evaluate the role of
[2770] this particular architectural
constraint in the metamer
[2773] phenomenon.
[2774] So what you're seeing
here in the top row
[2776] are metamers that are
generated from the kind
[2779] of standard models
that we normally
[2780] use that have convolution in
both time and frequency, OK?
[2782] And so that kind of looks
more or less like the thing
[2785] I just showed you.
[2786] And the thing at the
bottom is a model
[2787] that only has 1D
convolutions, so in time only,
[2790] and it's fully
connected in frequency.
[2793] And particularly, so I was
drawing attention to the fact
[2795] that the deep layers
of our standard models
[2798] generate metamers that are
not recognizable to humans,
[2800] and that's true.
[2801] But the early layer is generally
things that are pretty normal.
[2804] But you can see here that
with 1D convolutions, even
[2806] at these very early layers,
the metamers are pretty crazy.
[2809] So I'll just play you a
couple to give you a flavor.
[2812] [AUDIO PLAYBACK]
[2813] - The job security
program that prevents la--
[2815] [END PLAYBACK]
[2815] JOSH MCDERMOTT: That's very
intelligible compared to this.
[2817] [AUDIO PLAYBACK]
[2817] - The job security
program that prevents la--
[2819] [END PLAYBACK]
[2820] JOSH MCDERMOTT: OK?
[2821] All right, so this is at least
some indication that if you're
[2823] in the business of building
models of the auditory system,
[2826] imposing convolution
in frequency
[2828] is, at minimum, a useful
thing to do, in the sense
[2832] that when you have these
fully connected models,
[2834] though in principle,
in some conditions,
[2836] they might be able to
learn the same thing,
[2838] they have a pretty
hard time doing that.
[2840] And one of the other kind
of interesting observations
[2842] that Jenelle and Christina made
with this particular finding
[2846] is that although the
metamers of these models
[2848] were very different,
their behavioral phenotype
[2852] on natural speech was
actually really similar.
[2855] So this is the result of
that same speech recognition
[2857] experiment I've shown
you a few times now.
[2859] So we've got proportion
correct on the y-axis,
[2861] and signal-to-noise
ratio on the x-axis.
[2864] And the different lines
are different types
[2866] of background noise.
[2867] And you can see that
the two types of models
[2868] do pretty much the
same on this, right?
[2870] So you really only are
seeing this difference
[2872] when you look at metamers.
[2874] OK, so some reason
for optimism is
[2878] that we have had a little bit
of success improving metamers
[2881] by making sensible
architectural modifications.
[2884] So one kind of scandal
of the deep learning area
[2890] is that the models typically
violate a lot of signal
[2893] processing principles.
[2895] So in particular,
it's pretty common
[2897] to get significant aliasing.
[2899] And so we made some
architectural modifications
[2901] that remove aliasing.
[2903] We found that when you do that,
the metamers get a bit better.
[2906] So it doesn't get
rid of the problem,
[2907] but they become
more recognizable.
[2911] So that's consistent with
classical signal processing
[2913] intuitions about
what you might expect
[2915] biological sensory
systems to do.
[2917] But the last thing that
I want to leave you with
[2919] is another thing that we
have found that kind of helps
[2923] to improve this to some extent.
[2924] And that has to
do with addressing
[2927] another kind of commonly
talked about divergence
[2929] between neural networks
and human perception,
[2931] which is adversarial examples.
[2932] This is an extremely
well-known phenomenon
[2934] at this point, which is that
most neural networks can
[2937] be fooled by small things that
are imperceptible to humans,
[2942] adversarial perturbations.
[2943] So you take a particular
training example--
[2945] could be an image, could be
a speech utterance that has
[2948] a particular label--
[2949] and you can derive, using the
model, a very small change
[2953] to the stimulus that will cause
the model to misclassify it.
[2957] And one of our neighbors across
the street, Aleksander Madry,
[2961] has developed a method
for making models
[2964] robust to adversarial examples.
[2965] And this essentially involves
generating adversarial examples
[2969] during training and then
training at-- simply adding
[2971] those to the training
set, training the model
[2973] to correctly classify them.
[2975] And this is sort
of a picture that
[2977] is intended to give a little
bit of an intuition of this,
[2980] which is that there's some class
boundary that the model learns.
[2983] And maybe it's not
sufficiently complex, such
[2986] that you can get these
really small changes
[2988] that end up on the wrong
side of the class boundary.
[2990] And with the
adversarial training,
[2992] you kind of get
something that maybe
[2993] is a little bit more correct.
[2996] And Aleksander had noted
that when he actually
[2997] visualized representations
from these networks,
[2999] they tended to look better.
[3001] And so we thought that we could
measure this and relate this
[3005] to this metamer phenomenon
that we've been looking at.
[3008] And indeed, Jenelle found, in
collaboration with Guillaume
[3011] Leclerc and Aleksander, that
the robust models in the vision
[3015] domain have metamers that are
more recognizable to humans.
[3018] So you can just kind of see
this when you generate them.
[3021] She did a behavioral
experiment showing
[3024] that, particularly for the deep
layers, the robustly trained
[3027] models give you more
recognizable metamers
[3030] for humans than do the
standard trained models.
[3033] What Jenelle then
did is she went
[3035] and trained robust
audio models and found
[3038] a similar kind of phenomenon.
[3040] So you get a pretty
big improvement
[3042] in the recognizability
of the metamers
[3044] for the robust networks.
[3048] Now the big question here is,
like, why is this happening?
[3052] It's also worth noting that the
issue is far from completely
[3054] fixed, right?
[3055] So you still get a pretty
big recognition gap here.
[3057] But it does it does
make things better.
[3060] And I think we
still don't totally
[3061] know why this is
making a difference.
[3064] And it's interesting
to think a little bit
[3066] about the relationship
between metamers
[3068] and adversarial examples.
[3069] And sometimes, metamers
are like the congress
[3071] of adversarial examples.
[3072] So these are cases where the
model is judging two signals
[3075] to be the same, but that
they-- where they look
[3078] or sound different to humans.
[3081] But it's more
complicated than that.
[3083] I mean, metamers,
in some sense--
[3084] they're very different
from adversarial examples
[3086] in the sense that they're
independent of a classifier.
[3088] So you can generate metamers
for any kind of representation,
[3091] like the classifier is
not really part of it.
[3093] So it's just as relevant
for models that are
[3095] trained without supervision.
[3096] So indeed, one of the
things we're working on now
[3098] is looking at this
kind of phenomena
[3100] in models that are trained
with unsupervised learning.
[3104] So this is really still
kind of an open question.
[3106] It's mostly an empirical
finding at this point.
[3108] But it is something that
really makes a big difference.
[3111] And so the last thing that
I'll just leave you with
[3114] is that this phenomenon of
metamers is useful in the sense
[3118] that it reveals
differences that are not
[3120] evident with our
usual metrics, OK?
[3121] So in the paper by Alex
Kell from a couple of years
[3125] ago, we made two
primary comparisons.
[3127] One is behavioral comparisons
with natural sounds.
[3130] And the other is
fMRI predictions.
[3132] And Jenelle did this
nice demonstration
[3134] that both of those
kinds of metrics
[3137] really don't show differences
between the standardly
[3139] trained neural networks and the
robust trained neural networks.
[3142] So the correlation between
human speech recognition
[3147] across different
background conditions
[3149] is pretty much the same for
the two types of models.
[3151] It's very high in both cases.
[3152] And the fMRI predictions
are really equally
[3155] good in the two cases right?
[3156] So it's really only when
you do the metamers test
[3159] or if you evaluated
adversarial examples
[3161] in this particular
case that you would
[3163] see these differences, OK?
[3164] OK, so those are just the
take-home messages from part 2.
[3168] We've been using metamers
of neural networks
[3171] to reveal model invariances.
[3173] The general finding
is that the metamers
[3175] of the deep layers
of neural networks
[3176] are not metameric for humans.
[3178] They're usually not even
recognizable to humans.
[3180] So they're very
far from metameric.
[3182] This is true across modalities
for both vision and auditory
[3185] networks.
[3186] We've had some success
improving the models.
[3190] Metamers can be made
more human-recognizable
[3192] with certain kinds of
architectural modifications
[3194] that seem sensible
and by making models
[3196] more robust to
adversarial examples,
[3198] though we don't totally
understand that yet.
[3200] But this definitely doesn't
fix the problem completely.
[3202] These divergences remain.
[3205] And so just a top-level
summary here-- we've
[3207] been working on building
new models of audition
[3210] via deep learning
of audio tasks.
[3213] We have lots of examples
now of compelling
[3214] matches to human behavior with
real-world sounds and tasks
[3217] that we didn't have before.
[3219] We've replicated lots of
classical psychophysical
[3221] results that give us
insight into the origins
[3224] of behavioral traits.
[3225] We've got better models
of the auditory cortex
[3227] than we did before.
[3228] Evidence for hierarchical
organization--
[3229] I skipped over that.
[3231] But there are significant
remaining discrepancies
[3233] that we see with model metamers.
[3236] But I just want to conclude by
acknowledging all the folks who
[3239] did this work.
[3240] Alex Kell, Andrew Francl,
Mark Saddler, Jenelle Feather,
[3243] Erica Shook, Ray Gonzalez,
Dan Yamins, Yang Zhang,
[3246] Kaizhi Qian, their
collaborators at IBM,
[3248] and Guillaume and Aleksander
across the street.
[3252] And I'd like to thank you.
[3253] And I'm happy to take questions.
[3255] PRESENTER: Josh,
there's a question
[3256] from [INAUDIBLE] in the chat.
[3258] He asks, can you
please elaborate more
[3260] on what aliasing is
and how you reduced it
[3264] with architectural choices?
[3267] JOSH MCDERMOTT: Yeah, I
went through that really,
[3269] really quickly.
[3271] So aliasing is A
phenomenon happens
[3273] when you downsample a signal
without low-pass filtering
[3279] first.
[3281] And it causes information
that is in high frequencies
[3286] to get kind of moved
into low frequencies.
[3288] And so it's something
that you always
[3291] try to avoid when you're
doing signal processing.
[3294] So if you downsample, you
apply a low-pass filter, OK?
[3298] And neural networks
often end up aliasing
[3301] because, of course, as you know,
the downsampling operations
[3305] are kind of a big
part of what they do.
[3308] And the filtering
that precedes that
[3310] is usually not constrained
to be low-pass in any way.
[3314] And so you can just--
you can do that
[3316] by essentially building
in low-pass filters
[3319] prior to the pooling operations.
[3321] And that can largely
eliminate the phenomena.
[3324] And that has the effect of
making the metamers more
[3326] recognizable, which is
consistent with the idea
[3329] that, in accord with what
we were taught in DSP,
[3337] the brain might be set up so
as to try to minimize aliasing.
[3342] I mean, you can think of
it as like, when you alias,
[3344] you kind of--
[3345] you're mixing things
up, right, that maybe
[3347] should not be mixed
up, which is to say
[3350] the different frequencies.
[3353] AUDIENCE: Can I ask
a follow-up question?
[3355] JOSH MCDERMOTT: Definitely.
[3357] AUDIENCE: So another
question I wanted to ask was,
[3360] have you tried synthesizing
with putting some
[3363] of these constraints--
like, not allowing
[3366] any high-frequency sound to
be in your synthetic stimuli,
[3370] and see what the effect
of that would be?
[3373] The reason I'm asking for
this is to kind of try
[3376] to isolate whether how
much of the problem
[3379] is coming from having
high-frequency components
[3383] in any kind of stimuli.
[3387] JOSH MCDERMOTT: So
to be clear, the--
[3391] well, when we're talking
about high frequencies here,
[3396] we're not talking about high
audio frequencies, necessarily.
[3399] I mean, the aliasing phenomenon
this kind of internal
[3402] to the network, right?
[3403] So it's sort of high frequencies
inside the neural network
[3407] representation.
[3409] So if you've got a
spatial array of x and y,
[3413] it's frequencies in
that domain, right?
[3418] And I mean, we--
[3421] I'm not sure if we've
actually tried to--
[3425] we've probably done some
experiments along these lines.
[3427] But I think what you
might be getting at,
[3430] or what your question
is related to,
[3433] is the tendency of a lot of
people who do neural network
[3438] visualizations to actually
employ smoothness priors,
[3442] so that's a pretty
common thing to do.
[3446] And I think people
who have tried
[3449] to do visualizations,
they realize
[3451] that if you don't
impose smoothing priors,
[3453] things don't look very
good, which is essentially
[3454] the phenomenon that
we're talking about.
[3456] You can definitely make things
better by imposing priors.
[3462] But it kind of defeats
the purpose, right,
[3464] because the question here
is whether the model has
[3467] got the same invariances
as the human.
[3470] And so if you really want
to ask that, you don't
[3472] want to actually be imposing
priors onto the solution,
[3475] you know?
[3477] So, I mean, I
think it's possible
[3478] that it might give
you some clues.
[3482] But in this case,
we sort of already
[3484] got the clue from the aliasing
architectural manipulation.
[3487] So I'm not sure that that
particular prior is itself
[3492] going to be all
that informative.
