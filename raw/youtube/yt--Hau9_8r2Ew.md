---
schema_version: 1
id: yt--Hau9_8r2Ew
type: youtube
title: Martin Schrimpf; Advancing Integrative Models of Human Intelligence with Brain-Score;
  AI@MIT 3/7/23
url: https://www.youtube.com/watch?v=-Hau9_8r2Ew
authors:
- MIT Siegel Family Quest for Intelligence
ingested_at: '2026-06-01T19:24:29Z'
content_hash: sha256:ca5ae896388cf004a5156ce0715689645106ef3286adb74725038505cd5b8665
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: MIT Siegel Family Quest for Intelligence
  channel_url: https://www.youtube.com/@mitquestforintelligence2398
  duration_seconds: 650
  caption_track: fetched
  snippet_count: 279
filter:
  score: 0.7
---
[0] ZACK ANKNER: Hey, everyone.
[1] I'm Zack.
[1] I'm one of the heads for AI@MIT.
[5] JIMIN LEE: And I'm Jimin,
one of the other co-pres.
[7] ZACK ANKNER: Yep.
[8] And we're super excited
about this event today
[10] to be working with MIT Quest.
[12] We have a lot of awesome
speakers lined up for you guys.
[16] And yeah, just before
we get started,
[18] we just want to let you know
that after the speakers go,
[22] we'll have a panel discussion.
[25] So please, hold your questions
till after the speakers
[27] have finished speaking.
[29] And after this, there
will be a reception
[32] in the atrium after this event.
[36] So first up, the first
speaker is Martin Schrimpf.
[38] He is currently a research
scientist at MIT Quest.
[42] And he will be starting
over at EPFL next year.
[47] MARTIN SCHRIMPF: Well, thank
you very much for having me.
[49] Thank you for
organizing this event.
[53] Yeah, I will say, since
I'm starting my own lab,
[55] if you find what I'm going to
talk about interesting, then
[57] please consider applying.
[60] I should also say
everything I'm going
[61] to talk about is not just me.
[63] This has really been a
fantastic collaboration
[65] with many, many
people over the years.
[69] Many of them are present
on these slides .
[73] So a core goal of our field--
and our field here is loosely
[77] computational neuroscience--
[79] is to model human
intelligence, as well
[81] as the neural mechanisms
that underlie it.
[83] We think this is exciting
because it might provide us
[86] with a computational
understanding of intelligence.
[89] It might lead to the
next generation of AI.
[92] And perhaps in the
future, it could
[93] help with things
like neural disorders
[95] and help cure those
brain disorders.
[99] But one core question that
I think we're just not
[102] really sure how to
engage is how can we even
[104] tell we're making progress.
[106] And so in this talk,
what I'm going to propose
[109] is, and also show
what we have done
[111] is an integrative
model testing approach
[113] that we've now applied
to vision and language,
[115] and that I think has really
boosted our efficiency making
[118] progress quite a bit.
[121] So if you think of modeling
primate vision, then the way
[124] we think to engage with that
is that we should develop
[126] the model alignment to all the
tests in the field, basically.
[129] All the experiments that
anyone has ever done,
[131] ideally, we would test the
models in all of those.
[133] Of course, in practice,
when we can't do everything,
[135] but we should at least
not just do one and do
[138] as many as we can, I think.
[139] In a more empirical
form, this plot here
[143] is showing the number
of neural benchmarks,
[145] so it's testing how
well models are aligned
[148] to the neural mechanisms and
the neural representations
[150] in the visual cortex.
[152] And on the y-axis,
it's showing how well
[155] the best model out
of those benchmarks
[156] is aligned with
neural benchmarks.
[158] So basically, it's saying the
more neural benchmarks we have,
[160] the better I can predict on
an unseen behavioral benchmark
[163] how well your model
is going to do.
[165] So this is just one
characterization
[166] of how more benchmarks
are going to help,
[168] but it's really to
motivate that we
[170] should test on all experiments.
[173] I said this.
[174] And then there's
two primary forms
[176] of testing what
we've done so far.
[177] One is to test the
behavioral element.
[179] So here we show the
same images to the model
[181] that were shown to humans.
[182] And I'm going to show an
example of that in a second.
[184] And then we test how
similar the outputs are.
[187] But also, we test
the neural alignment.
[188] And we do this at the level of
spike rates, which previously
[190] have been shown to
predict behavior.
[192] And we're also going to
include macaque visual cortex
[195] because that has
previously been shown
[196] to be very similar to our
own visual cortex in humans.
[200] And yeah, we do all
of this on a platform
[202] called Brain-Score that I'm
going to talk a little bit.
[205] And also, Katherine is going
to have more details for you.
[207] So I want to run one
video trial with you.
[210] So imagine you're the subject.
[211] Maybe for extra motivation,
imagine you're being paid.
[214] Your job is to fixate on
the dot in the middle,
[216] and then I'm going
to flash an image.
[218] And you should
raise your left hand
[219] if you think the image on
the left is the most similar,
[222] or your hand on the right if you
think the right one is similar.
[224] Ready?
[228] You all got this.
[229] So if you were a subject,
you would now be paid.
[231] This was very easy.
[232] If the images have changes
in the viewpoint parameters,
[236] at some point, you're probably
going to start making mistakes.
[238] For instance, the next
one that's coming up,
[240] like bear versus rhino.
[241] For some of these, you might
not be so sure at some point.
[245] So when you show these to
tons of subjects on MTurk,
[247] you can build what is
called a confusion matrix.
[249] So here the different
rows in the matrix
[251] are effectively the
different images.
[253] And the different columns
are different risk factors.
[256] So one element in
the matrix tells you,
[258] for instance, how difficult
is it to categorize
[261] a dog versus a fork,
which is pretty
[263] easy in green color, or
maybe rhino versus elephant,
[266] which is more
difficult in red color.
[270] So when we run this
as a benchmark,
[271] then this is our data.
[272] To test models on this, we run
the same experimental paradigm.
[275] So we show the same exact
images to the models.
[277] We have them perform a
similar task where they also
[280] do a sample task.
[281] And then they make a
similar prediction.
[282] So we can also compute
the confusion matrix
[284] for the models.
[285] And then there's different
ways to compare them.
[286] You can just correlate
whether the models
[288] make the same mistakes.
[289] And that is going
to give you a score.
[291] And I want to stress
that this is not just
[293] a test of ground
truth performance.
[294] It's really alignment to human
behavior on an image level.
[299] So really, we want the
model to make mistakes
[301] if the humans make
mistakes because we
[303] want a model of humans.
[306] One last thing about
this behavioral setup
[308] is that we can also run the
same task and the same images
[312] on macaque monkeys.
[313] So here's a video of a monkey
performing the same task.
[317] At the bottom we can
see the very same images
[319] that you just saw.
[319] And they get rewarded with
juice and get a green screen
[322] if they get it right.
[323] If they don't get it right,
they get a timeout, and black.
[325] And usually, they're
pretty eager to keep going.
[330] What this then
enables us is we can--
[332] as we show images, we
can implant electrodes,
[335] and we can record the neural
activity in their brains.
[337] So these are going to
be electrical signals.
[339] I don't have enough time
to detail everything here,
[342] but we can convert this
into spike rates, which
[345] tell us how active a particular
neuron is at a given time.
[348] So the way I like to think
about that is per image,
[350] it's going to give you a vector
of activations or of activity.
[353] So at the end,
you're going to get
[354] a matrix of images
times neuron where
[356] each element of the
matrix tells you
[357] how active a particular neuron
is for a particular image.
[361] And again, we can run
this on models as well.
[363] So we can show, again,
the same images.
[365] In the model, we can now
record from different areas.
[368] Again, there's different
ways to do this.
[369] Just imagine there is a
particular layer in the model
[372] that we like.
[373] And that is going to be the
prediction from the model.
[375] So these are now internal layer
activations from the model.
[378] And we're going to
compare those to the data.
[380] There's many different
ways to do this.
[381] I like one that is called
neural predictivity where
[383] we try to predict the
activity for unseen images.
[386] And then, again, we
get a similarity score.
[390] So putting this
all together now,
[392] I'm going to show you model
scores on different benchmarks.
[396] I should say, in
visual cortex, there
[398] is roughly four cortical
areas called V1.
[400] So that's early visual
cortex going up all
[402] the way up to IT, that's
high-level visual cortex.
[404] That's basically what is
involved in human object
[406] recognition.
[408] And I'm going to show you the
scores of one particular model.
[410] So this is a classic
neuroscience model
[412] that people developed in the
2000s, which was considered
[414] to be really state of the art.
[416] It's doing OK on maybe
the early benchmarks,
[418] but especially as we get to
high levels of cortex behavior,
[420] it really doesn't do well.
[422] Here's all the models that
computer vision has developed.
[425] You can see they're
doing a lot better.
[427] And in fact, the current state
of the art models are of neural
[430] and behavioral
alignment are models
[433] that are deep neural
networks trained
[435] on a computational task.
[438] We also show all of this on our
website called brain-score.org.
[441] So I encourage you to check
that out after the talk.
[443] And then it always lists
the current best models
[446] on basically all the different
benchmarks that we have.
[448] And I want to point
out what previously
[450] was a PhD project where you
test some models or maybe one
[454] benchmark, you can now
just run in a couple
[456] of hours on this website.
[457] So I really think this
makes it much more efficient
[459] for our field to make progress.
[462] And it also enables us to
compare all these models
[465] in a unified manner
on all the benchmarks,
[467] and to make sure that the
models really are correct,
[470] and to also show where
the weaknesses are.
[472] Our community is adding more
and more of these benchmarks.
[474] Currently, we are at over 50.
[476] And of course, we
want to add many more.
[480] So what this also
enables is when
[482] we average across all
the different scores,
[484] one dot here is going
to be one model.
[486] So across all the
different models,
[488] we're going to get
a range of scores.
[490] But now you might
wonder, is there
[492] something that explains why some
models are better than others?
[494] And from Peter's work,
what has been suggested
[497] is that perhaps
optimization for a task,
[499] such as object categorization,
might be a predictor.
[503] And indeed, we found that models
that are better at ImageNet--
[506] so this is a large scale
computer vision database.
[510] Models that are better
classifying images
[511] in this ImageNet competition
are the models that
[515] are more aligned to behavior.
[518] But still, they're not perfect.
[520] And also, the latest ones
are actually not much better.
[523] So machine learning is
optimizing on the x-axis.
[525] They're building better
and better models,
[527] but after some point,
the best models actually
[529] start to be not aligned to
predict behavior anymore.
[532] So there's really
still a bit of mystery.
[533] But at least from the
low performance regime,
[537] you can improve your
models by just optimizing
[539] on this computation task.
[544] So this was vision.
[545] In my remaining 10 seconds,
I want to briefly tell you
[548] about language, because
one part of this approach
[550] is that it's very easy to
generalize across new domains.
[553] So here the question
is, as we use models
[555] from the natural language
processing community,
[557] can they be any
similar or can they
[559] predict what processing
in the human brain
[561] or the human language
system is going to be like?
[563] Here the data is going to
be mostly fMRI data, as well
[567] as ECoG recordings.
[568] Roughly, these are
non-invasive methods.
[570] ECoG is invasive, but fMRI,
you can just go in a scanner.
[573] Maybe some of you
have done those.
[575] So the y-axis here
is going to be
[577] how well the models are
aligned to neural measures
[579] in the human language system.
[580] And again, across
multiple brain data sets.
[582] I think that is
important, because then we
[584] can have some confidence
that the results are general.
[587] And it turns out
some of the models
[588] are actually really good
models of the human language
[591] system, especially
gpt2-xl, which many of you
[594] have probably heard about is
coming quite close to what
[598] we've measured in the brain.
[600] And again, we find that there is
a normative task that tells us
[603] what models are better.
[604] In this case,
predicting the next word
[605] seems to be a powerful
predictor of which models
[609] are going to be best
aligned to the human brain.
[612] I've definitely run out of time.
[614] But I hope you can
take away from this
[615] is that as we add more and
more benchmarks together,
[618] I think that is going to enable
us to make meaningful progress.
[622] And Brain-Score is
one implementation
[624] of this approach.
[624] It's currently the largest scale
version in vision and language.
[628] It allows us to identify
the most brain-like models,
[630] provide empirical
constraints for new models,
[632] and we can also discover these
relationships, for instance,
[635] between object
categorization and brain
[638] alignment, or a next-word
prediction alignment.
[641] Everything is open source.
[643] And we could really
use your help.
[644] And I think Katherine is
going to say more about this.
[646] Thank you.
[648] [APPLAUSE]
