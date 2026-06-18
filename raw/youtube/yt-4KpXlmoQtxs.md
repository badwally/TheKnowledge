---
schema_version: 1
id: yt-4KpXlmoQtxs
type: youtube
title: 'Data Science Speaker Series: Sparse Coding - Prof. Mike DeWeese, UC Berkeley'
url: https://www.youtube.com/watch?v=4KpXlmoQtxs
authors:
- Fenrir LLC
ingested_at: '2026-05-30T20:41:04Z'
content_hash: sha256:52bf15198f5fd6b74917ca9ea7f62e19056f49ef956f5f45821ad10533f019c9
domains:
- convergent-ai-brain
nlm_corpus_ids:
- 0997b925-a7b2-47d2-8dcc-e11fcecf953e
wiki_pages: []
meta:
  channel: Fenrir LLC
  channel_url: https://www.youtube.com/@fenrirllc5923
  duration_seconds: 4923
  caption_track: fetched
  snippet_count: 944
filter:
  score: 0.7
---
[0] Okay! So, we are fortunate to have Mike DeWeese
with us here today to deliver the second in the
[8] Fenrir distinguished data scientist speaker 
series. Mike's a professor of physics and
[15] neuroscience at the University of California 
Berkeley. His theoretical interests include
[20] non-equilibrium statistical mechanics, information 
theory, and machine learning, and he has also done
[27] actual experimental neuroscience work as well 
as neuroscience theory. Today's talk is a bit
[34] machine learning, a bit neuroscience theory. 
So, Mike, why don't you take it away from there?
[41] All right. Thanks, Steve! Fun to 
talk. I appreciate the invitation.
[45] And that's right. What I'm going to focus on today 
is going to be, as as the title might suggest,
[51] something that involves machine learning and 
also involves neuroscience systems. Neuroscience,
[55] how the brain works. But we also are interested 
in non-equilibrium stat mech. So I made this
[62] very high-level, fancy graphic 
to sort of make this point.
[65] We're interested in the brain, we're interested 
in neural networks - or here's artificial neural
[68] networks down here. We're also interested in 
non-equilibrium stat mech. It turns out that,
[72] I think, most people are aware 
of the fact that there's,
[75] I think it's fair to say, a revolution going 
on with artificial neural networks right now.
[80] There's also a quiet revolution going on 
with non-equilibrium stat mech. There's
[85] there's a lot of exciting stuff that's been 
happening the last 20 years, I'd say. And
[90] it's actually gone largely sort of under the 
radar, I think, in American physics departments.
[94] So that's been something that we've been very 
excited to work on. And how does it relate to
[98] the brain. So I have arrows between every pair 
of things here. Why is that? Well, I think it's
[102] obvious, between the brain and artificial neural 
networks - these were inspired right by the brain.
[107] Turns out we can learn about the brain. I'll 
talk about that today. You can learn about the
[110] brain by studying artificial neural networks 
of the right type. I would say some of them
[116] are more accurate for describing their brains, 
some are less. I'll have more to say about that
[120] for non-equilibrium stat mech. It 
turns out that approach to equilibrium,
[124] which is what happens if you drive a 
system - some thermodynamic system -
[127] out of equilibrium by pushing it really hard, 
that actually in some ways (the mathematics
[135] involved and how you describe that return 
to equilibrium) looks a lot like learning.
[140] And so there are some mathematical tools 
we use from non-equilibrium stat mech
[144] to understand learning in the brain, and 
learning also in artificial neural networks.
[149] I just wanted to point that out to a big 
part of our group. But today, like I said,
[153] I'll focus on the section up here, just to 
keep it under 45 minutes. So here's my outline.
[159] I'm going to talk about, well, actually, here's 
another way to think about how physics can inform
[166] us when it comes to artificial neural networks 
in the brain. I'm going to sort of talk about a
[170] quote-unquote "principled way," I will say, about 
thinking about how to develop theories for how the
[176] brain works. As opposed to, you know, sort of the 
pejorative - this is a pejorative statement but,
[182] one way you might think about studying biology 
or even neural net artificial neural nets is
[188] sort of like a stamp collecting approach. There's 
all these facts and details to collect, all this
[191] information. It's hard to organize. But maybe if 
you know enough things and you put it together,
[196] you can figure out what's going on, or 
at least model it at some level. But our
[200] hope is that we can come up with a few basic 
ideas, sort of physics style - that will allow
[205] us through some optimization principle or some
sort of variational principle - that will tell
[210] us a lot of what's going on. And that's 
especially helpful when you've got models
[213] with gazillions of parameters. You're trying to 
understand something as complicated as the brain,
[217] and the brain is pretty impolite, right? Not 
only do you have enormous numbers of parts of it,
[223] but these aren't electrons where everyone's 
exactly the same. Each neuron's a little
[226] different in some way. So you have to come up 
with some, I would say, it's really helpful
[231] to come up with some principle to guide your your 
theory. Anyway, I'll talk about that a little bit.
[236] And then I will talk about, okay, if we
develop some algorithm that seems to predict
[245] the way ... Oh, what does V1 RFs mean? V1 is 
the primary visual cortex. The part of your
[251] brain - the first part that processes 
visual information in the cerebral cortex.
[256] And RFs is "receptive fields." So these 
are the visual features in the world that
[261] neurons care about, that they respond to.
So can this algorithm work in real brains?
[266] I'm going to argue that it could. And then, as 
a result, we can make predictions. And in fact,
[272] there's been a lot of really great work over 
the years. And in fact, Steve Strong and I sat
[276] together in a talk in 1996, when i first met Bruno 
- and I think Steve first met - Bruno Olshausen.
[281] And he did some really seminal work in this 
area. I'll talk about in a couple slides. Just
[287] coincidentally; I just remembered. And most of 
the work that's been done over the past couple
[292] decades has been about receptive field shapes. 
What are the features in the visual world that
[298] cells care about in our brain, right? And why they 
respond to them? But I'd like to go beyond that
[303] and ask questions about the connectivity 
structure in the brain, or the activity
[306] patterns you see. Make predictions beyond just 
what features matter. And then I'll talk about
[312] whitening. And by that I mean - well I'll describe 
the operation, but if you're familiar with it i'm
[317] just talking about essentially doing principal 
components analysis or sphering the data.
[323] It's traditional before you send in some visual 
input, or any kind of input for that matter,
[328] into some kind of a sparse coding model, first 
thing you do is you whiten your data. You sort
[333] of set it up so that the variance of the data 
in all directions is the same. And that has some
[339] some benefits, but it turns out it has a 
lot of benefits for a biologically plausible
[344] network. So I'm going to make an argument at the 
end that i've got a new idea for why - or my group
[348] does - for why our retinas do the preprocessing 
they do before you get to the cortex. Which i'm
[354] excited about in part because one argument 
against the ideas I want to present - the
[359] naysayers when it comes to sparse coding -
might say, well, if sparse coding is such a
[365] great idea, why has it taken until you get to your 
cortex before you start doing it? Why don't you do
[369] it in your retina? Why did you run into all this 
other stuff first? And there's a couple different
[373] answers to that question that sound plausible, 
but here's a new answer people didn't know
[377] about before. So it's another way to think about 
processing and why whitening might be a good idea.
[383] And I'll mention some ongoing projects 
that come from this story, and I'll give
[388] acknowledgements. All right. So the principle 
of sparse coding. What am I talking about?
[392] So the real world is structured. You heard it 
here first! You know, you look out your window.
[397] There's mountains and there's whatever this is. 
Some windows. If you have a home by the beach,
[401] this is what you get out the window. You don't 
see this in Chicago. You could see this out
[406] the window, but typically you don't see
unstructured stuff. And when I say it's
[411] structured, I mean I think we have an intuitive 
idea what's going on over here but mathematically
[415] how do we describe the structure here? And 
why do we care? The reason I care is that
[421] the fact that visual input and other types 
of natural sensory input is so structured
[425] might be that our brain is has evolved over time 
to do a good job of efficiently encoding this.
[432] Before I get into efficiency, let me just give you 
a laundry list of different ideas of principles,
[440] sort of like like physics principles, 
we might apply to understanding how
[443] the brain works. One is maximum information. 
You know, the visual system in fact there is an
[449] information bottleneck. You go from 100 million 
photoreceptors, roughly, in your two eyes,
[455] and then you go through a bunch of processing, 
and it goes to your optic nerve right? The
[460] information lines that go up to your brain. And 
there's only about a million of those. You have
[464] a hundred fold reduction in terms of numbers 
of cells. So maybe you want to maximize the
[470] information through that bottleneck, right? It 
might be a really good idea. Turns out that is a
[474] good idea. That explains a lot about various kinds 
of coding in different sensory systems in biology.
[481] How about reliable information? That's 
another kind of principle you might apply
[485] to to come up with a good theory. Like, in 
your motor periphery. controlling your hand,
[489] you don't necessarily want to send a lot of 
information to your hand. You just want to make
[492] sure that the information you send is understood 
properly and the hand works properly. So, reliable
[497] information is a good idea for a principle 
in some parts of the nervous system. Maximum
[501] entropy. In fact, we even studied minimum entropy 
in some cases, which nobody ever had done before.
[507] Max entropy is obviously is a very powerful idea 
in physics. It turns out it's also a very powerful
[512] idea in neuroscience. There's a cottage industry 
actually, using maximum entry models to fit
[520] with - you know, parameter free; once you maximize 
the entropy your parameters are all determined for
[524] your model and you can go and compare against the 
actual activity that's recorded in the brain. And
[530] there's a lot of success there. Minimum wiring 
length. The idea that one thing that limits the
[536] size of our brains is just the size of our heads 
getting through the birth canal. We're limited by
[542] ... Like, the reason humans are born so immature 
compared to many other animals has to do with
[547] how big the brain has to get for an adult human 
to function properly. So minimizing the wiring
[553] length by laying out your circuit in a smart way 
actually can save you a lot of volume. And it
[559] might be an important aspect of how the brain's 
set up. Slowness. Turns out that if I want to
[566] to look at a really complicated set of data, 
like a bunch of responses in my retinal
[573] neurons, it might be that slowness could tip 
me off as to where the important signals are.
[579] In other words, as I look around the room 
the retinal image is changing like crazy,
[584] right? Because the entire scene changes as i look 
around the room even though the objects in the
[588] room aren't going anywhere. Their identities are 
remaining the same for the most part, except for
[592] very slowly varying things - like maybe a friend 
of mine walks in the room and then walks out. So
[597] slowness done mathematically and with some 
creativity can actually be a really useful
[603] principle for figuring out coding schemes in the 
brain, to extract useful signals out of quickly
[609] varying inputs. Efficiencies. There's all kinds of 
efficiency. Obviously efficiency is a good idea,
[614] and in fact we're going to focus on sparseness 
and independence, which are related to efficiency
[619] in this talk. Sparseness, which i'll 
define a little bit more in a second, is
[624] a type of efficiency, if you like. And there's 
more than that, but that's just to give you a
[628] sort of a laundry list of things I've thought 
about. And that there's a lot of good ideas there.
[632] So, sparseness seems like a good candidate. What 
do I mean? It means minimal neural activity.
[638] There's lots of ways to describe that.
Without saying them all,
[643] you could talk about whether you have population 
sparseness, meaning you only have a few neurons
[649] that are active out of the population. You have 
lifetime sparseness, meaning that for any given
[653] neuron it's not very active over time, right? 
And these are related but not exactly the same.
[659] And there's different kinds of sparseness, too, 
in terms of how you measure activity. Do you mean
[663] that you have strictly zero activity for most of 
your neurons? Which would be L0 sparseness. Or do
[669] you mean that if you summed up the absolute value 
of the activity of all your neurons, it's small,
[674] which is like L1 sparseness. So there's different 
kinds of sparseness. It'll turn out that
[683] it's not going to matter too much for this talk 
which one we're talking about. I just wanted to
[687] throw that out. Identifies ... Oh yes, so the 
idea of sparseness actually will automatically,
[694] in a natural way, give us some idea about the 
causes underlying what produces a visual scene.
[701] Which is actually useful biologically, right? 
And in general it's probably a useful thing to
[705] be able to do, not just because it produces 
an efficient representation but because it
[710] gives you something meaningful about 
what's being conveyed and seen. And
[715] sparseness is efficient. If you only have a 
few active neurons, obviously you're going
[719] to use less energy, right? Because those 
neurons are the ones that are active,
[722] as opposed to everybody active all the time. 
And it's also related to independence. If you
[730] want to get as much information as possible 
from each of your very few active neurons, the
[735] more independent they are, sort of based on some 
simple ideas from information theory, the more
[740] information you can hope to get by looking at more 
of them. If you have very redundant information in
[744] a bunch of neurons, you have to look at a lot 
more of them before you get the same amount of
[747] information. So if you have just a few active 
neurons, it might make sense to make them as
[751] independent as possible, in terms of what they're 
conveying. It's related to overcompleteness. So,
[757] a lot of us, I think, learn about various 
representations in our math and physics
[763] and engineering courses. Fourier analysis is 
probably the best known example, right? That's
[768] an example of a complete basis, the way it's 
usually set up, meaning that you have a unique
[773] solution. There's a unique set of coefficients 
you'll put in front of each of your sine wave
[777] basis functions to represent any given signal 
or image or whatever you're trying to represent,
[783] right? But the brain actually has 
way more neurons than you would need
[788] for a complete representation. And that's partly 
because different parts of our brain are ... or,
[793] there's duplication in a sense, or higher 
order processing, where you have the same thing
[797] represented in many places. But even within one 
given area, like V1, the primary visual cortex,
[803] you have way more neurons - hundreds, thousands 
more neurons within even a single layer of that
[809] cortical area - to represent the visual input. 
Why is that? Well, maybe because you're trying
[813] to form a sparse representation with only a few 
active neurons. So you have lots of specialized
[818] neurons that could represent particular features 
that may or may not be present in the scene.
[823] And the more different over-complete neurons 
you've got, the better job you can do at being
[826] sparse and doing a really good job of representing 
the input without much error. So that's related to
[832] sparseness and overcompletenesses. You get 
simpler population codes. So if you have a
[838] representation that's not highly distributed, that 
just has a few active ... Well, it's distributed
[844] in that it involves a population, but it's not 
involving lots and lots of co-active neurons,
[850] it's a lot quicker to figure out what's going 
on and decode it for downstream neurons.
[857] And it works. That's the best reason that 
I'm bothering with this. And what do I mean
[862] by "it works" for vision? What I really mean is 
that it's been known now, since mid-'90s, that
[866] it does a good job, these sort of theories, these 
sparse coding models, for predicting the features
[872] that cells care about. And I'll talk about other 
predictions that we made beyond that in a few
[876] slides. Okay. So we're back to our picture, 
now, of the beach. And you know what features
[880] matter? So you know there's obviously a lot of 
structure here, compared just to white noise
[884] instantiations. When we look at this, if I'm to 
describe this to you, I'd say, "Well, there's
[890] objects in the scene, there's a mountain, and I 
can say which way the lighting is coming from,
[894] which is kind of tough here because it's a little 
bit of a hazy day. There's perspective. Maybe I
[899] can describe what's in the picture. But at a 
low level ... So that's a high level, right?
[904] At a low level, if I want to capture as 
much information as I can about the scene
[908] with as little activity in my neurons - or, if 
you like, as little time as possible - maybe
[913] I ask a cartoonist. Say, "Hey, you know you've 
got 30 seconds to make a drawing of this image."
[920] What is she going to do? Well, she's going to
look at edges. She's going to make a line drawing
[925] that goes around the edge of all the objects. 
Because that's the most informative thing you
[929] can do in a hurry, with just a few active places 
on the page. If you think of the pencil on the
[935] paper, that pencil lead on the paper, as like 
active neurons, with a sheet of neurons that
[939] are being active, right? You'd say, "Oh! Yeah, 
you'd make a line drawing." And then beyond that,
[945] well, you know, I just mentioned the idea of, you 
start off with the really salient edges. There's
[950] a really dark and light area with a hard edge 
between them. That's an obvious thing to draw to
[955] convey a lot of information about what's in the 
scene. But then there's a lot of subtle edges,
[958] too. And then there's a question of which are 
the most efficient or useful from a mathematical
[963] sense, if we're going to really do a careful 
job of this, right? And so, to get at that, what
[971] I've done is, I've got a black and white image 
now. This is all going to be about black and white
[975] images in this talk, although it doesn't really 
matter. But for the actual data that we we used,
[979] it was black and white, and it was whitened 
as well. And I'm not showing you a whitened
[983] example. I'll do that later. I'll get back to 
that whitening issue. But okay. So we have our
[988] our grayscale image. Here, we'd 
like to represent this little patch
[991] with some part of my visual system. How do I do 
it? Well, I'm going to represent it as a linear
[997] sum of features. And these features, you can think 
of as transparencies. You're probably all too
[1003] young to know what I mean by that. But these are 
pieces of acetate with dark ink printed on them,
[1011] and it's otherwise transparent. So if you stack 
these things on top of each other, you get a
[1016] linear summation of these different gray scale 
patterns if you do a good job of multiplying them
[1023] by the right coefficients. So with the certain 
coefficient, I turn up and down the darkness
[1028] of my dark spots with each of these numbers.
And these coefficients, you can think of as the
[1034] activity of neurons. So here I've drawn 
- here's a neuron whose voltage ... Uh,
[1038] so these are neurons in my brain, in 
my visual cortex. Here's a couple -
[1042] actually this isn't data from my brain, it's it's 
cartoon data - and here's a couple spikes that
[1047] are occurring. It turns out neurons in the brain 
don't talk to each other with graded signals, with
[1052] some exceptions. But by and large that's true. 
They talk to each other with these all-or-none
[1056] events that I'm going to call "spikes" or "action 
potentials." And in this case a1 might be the
[1060] number 2 because I count two spikes that occurred 
after this image was presented to my retina. And
[1065] then this guy doesn't fire at all. This guy didn't 
fire at all. These are just some sub-threshold
[1070] voltage fluctuations that don't count as 
activity because these don't reach other
[1075] neurons in the network. And so a2 would 
be zero, a3 would be zero, but a1 would be
[1079] non-zero. So you can see if you add the sub for 
all the neurons in my dictionary or my population
[1086] of neurons - different way of saying the same 
thing - then you'd wind up with a representation
[1093] of this input. And in fact, what Bruno Olshausen
figured out with David Field - his collaborator
[1099] and advisor back in those days, in the mid 90s - 
was that if you write down a cost function that
[1103] consists of the RMS error between the input - this 
green x here represents the actual pixel values
[1109] in this little square - and then here's your 
representation, the sum over all your neurons (m
[1116] indexes your neurons, right?) of your coefficients 
times your basis functions (these guys, right),
[1122] you take the RMS error of that - I guess it isn't 
even root mean square, it's just squared error,
[1126] pardon me. Anyway, take your error and then 
add to it a cost - there's another cost,
[1131] uh, a penalty in your cost function - that
is the l1 sparseness. That is just the sum
[1139] across all your neurons of how active each neuron 
is, with an absolute value. So this mathematical
[1146] formulation is an unconstrained optimization. And 
then you iterate. You go back and forth between
[1152] deciding what values you want 
for the coefficients, with fixed
[1160] features, right? And then you minimize 
that, and then you use that information
[1165] to ... You take those coefficients and 
say, well, how could I have improved my
[1169] representation by minimizing my cost function 
a little bit? By then changing the shape of
[1174] my features to do a better job. And if you 
iterate back and forth, eventually this thing,
[1178] the sparse coding algorithm, will converge and 
you'll have a dictionary of things that you say
[1184] your neurons ought to represent. What features in 
the world they represent in order to do a good job
[1189] of minimizing this cost function. Right? With 
this sort of a coding scheme. Oh yes, this is
[1195] what I just said. Reconstruction error is captured 
by this term, activity by this term. There's not a
[1199] huge amount of math in this talk. There's a couple 
slides. This is one of my math slides. Okay. So
[1204] this leaves representation of the data in terms 
of sparse activities, right? Only a few. Why?
[1209] Because of this guy, right? On average, you 
only get a few active neurons at a time.
[1214] This is unconstrained optimization, just to hit 
that point again. Okay. So here is what Olshausen
[1220] and Field found out in 1996. Turns out that each 
of these little squares is one of the features
[1225] that one neuron cares about in their network. And 
what you see is they have edge-like properties.
[1230] You tend to get things that are active - like 
they're gray, which means they don't really care
[1234] about most parts of the visual patch that they're 
trying to represent, but they care a lot about an
[1240] edge in a certain location. And these edges 
have - they go through one, two, three, or more
[1246] light or dark (which means large or small) 
fluctuations away from that sort of zero gray
[1253] background. These are Gabor patches. They look 
like sine waves that are windowed by - often
[1259] long and thin, but but windowed by some sort of a 
Gaussian function. Anyway, they're edge detectors.
[1265] So this is mathematically the kind of edge 
detector that this algorithm says is what you want
[1269] to do if you want to do a good job. These things 
are local, they're oriented, they have different
[1273] angles, right, they're band-passed - they're not 
perfectly sharp and they're not, they don't cover
[1278] the entire scene. They're edge detectors. That's 
what they are. And if you look at data from actual
[1286] mammals, like a Macaque monkey taken by 
Dario Ringach some time ago, turns out that
[1291] it's pretty good. These are the features 
that neurons in the visual cortex of
[1298] a monkey tend to care about. 
What they individually encode,
[1302] if you assume that the model that's being used 
is similar to the one that I just presented.
[1306] And you get a lot of things that look just like 
what they find in the model. That was a huge
[1309] theoretical triumph that started a whole line of 
research, when they said, wow, we can predict what
[1315] biology is doing just based on a principle 
and taking photographs - not his vacation,
[1319] it was actually his advisor's vacation - but 
take a bunch of photographs from a vacation,
[1323] chop it up into little segments, and then train 
the model on that with the right principle of
[1329] sparseness and with a cost function of minimizing 
your error, right? And out of it just pops this
[1336] biological result! Now it turns out there are some 
deviations here. You get point-like things instead
[1341] of just edge things entirely. And it turns 
out that that could be accounted for by ...
[1347] You get a little bit of a win by looking 
at L0 instead of L1 norm minimization. So
[1351] minimizing the number of non-zero coefficients 'a' 
rather than the sum of the absolute value. But the
[1357] real difference is looking at over-complete rather 
than a complete representation. That was a bigger
[1362] win. And then here's a more recent effort by ...
Again, Bruno Olshausen is a colleague of mine
[1369] at Berkeley. So is Fritz Sommer, it turns 
out. There's a lot of sparse coding going on
[1373] within our theoretical neuroscience group at 
Berkeley. But yeah. Martin Rehn, Fritz Sommer and
[1380] Bruno also has an algorithm akin to this, that's 
more sophisticated. That can handle L0 instead
[1385] of L1 minimization and that can handle other 
things too I'll talk about in a little bit.
[1390] And the upshot is that you 
wind up with a much better
[1393] fit to the data. So, great! Looks like sparse 
coding tells us something about what's going on
[1397] and the visual system is using that as well 
to understand the structure of natural scenes.
[1402] Can this work in real brains? Well, so here's 
again that picture I showed you a minute ago,
[1407] and here's my representation of this scene. So 
neuroscientists are the only - it's the only
[1414] culture in the history of the human race, I think, 
that actually uses backward arrowheads to indicate
[1420] flow of information from here to here. It's 
because the shape of the, of the structures on the
[1425] synapse between pairs of neurons has that shape. 
But anyway, so these are meant to be arrowheads
[1430] going in the other direction from left to right as 
we see it on the screen. And what's going on is,
[1435] here's my visual patch. I'm just taking a 
binarized, simplified version of it. And I'm
[1442] saying, okay, how is my network set up? I've got 
feed forward connections in blue that go from a
[1448] pixel in the image to a given neuron. There's more 
than one neuron in my in my world here, but I'm
[1455] just going to show one to start off with. And one 
way I can represent these connection strengths is
[1460] the way I did a minute ago, with these grayscale 
images that show the feature, the visual feature
[1466] in the world, that this neuron cares about. And 
you can think of this as the projection field,
[1471] if you like, or the receptive field. Turns out 
those are the same thing under some conditions
[1476] that are satisfied in the networks I'm going to 
talk about. So we can call it whatever you want.
[1480] We can call it a feature, a visual feature, 
a receptive field, or a projection field.
[1484] But essentially where does it come from? It's 
determined by the strengths of these connections
[1489] that say, yeah, if you have a light spot up in 
this pixel, I'm going to give a lot of activity
[1494] to this neuron. If it's dark down here, I'm 
going to give a lot of activity because ...
[1498] well, it depends on the shape of the receptor. 
Given this receptive field shape, if it's dark
[1502] down here then it's going to make this neuron 
more active. Whereas if it's light down here, it's
[1506] going to make it less active, right? So this is 
the feature that drives this neuron to be active.
[1511] And things that look different than that push it 
the other way, make it less active. And you have
[1516] a bunch of neurons in your network, and some of 
them are very similar for the things they code.
[1521] Why? Because it's an over-complete representation. 
You've got lots of similar receptive fields, lots
[1525] of similar shapes for your features, right? And so 
I have a little red ... So here again is an arrow,
[1531] this time with a circle on the end. Another weird 
nomenclature from neuroscience. This is an arrow
[1537] that goes from this neuron 1 to neuron 2. And 
the fact that I colored it red and put a circle
[1542] on the inside of a triangle reminds me to say that 
it's inhibitory. These guys look very similar. So
[1548] if this neuron shuts this neuron down, 
directly through a synaptic connection
[1553] based on how similar their current features are, 
that's a way that the network can use a local rule
[1560] at least during inference. What's inference? 
That's when you determine the values of your
[1564] coefficients, as opposed to learning. That's when 
you determine the shapes of your receptive fields.
[1570] So it's anyway more jargon. But the point 
is that when you're trying to figure out how
[1574] active each neuron should be in representing the 
scene, one way to do it that is local is to have
[1582] these inhibitory connections. And this is a small, 
a weaker, connection from neuron 1 to neuron 3.
[1588] Why? Because there's less overlap. There's less 
similarity in the features they represent. So
[1592] they don't need to really inhibit each other that 
much. They're going to be responding to different
[1595] images anyway - or different parts of the image -
and they're not going to interfere with each
[1600] other. So there are algorithms that take 
advantage of this local idea that could
[1604] be implemented in real brains, right? And "LCA," 
"SSC," this is algorithms by Bruno and by Fritz.
[1613] Bruno Olshausen and Fritz Sommer. And so that 
idea was already out there before we got in in
[1618] the game. But the thing that didn't exist was 
a way to learn these shapes in the first place
[1625] that's actually implemented - could be implemented 
in real variance. In other words, once you've got
[1630] these features figured out, people found ways 
that real brains could, using local rules,
[1636] figure out what the activities ought to be to 
represent the scene in front of the eyes. But what
[1640] didn't exist was, how do you figure out what these 
blue connections ought to be in the first place?
[1646] How do you determine what these receptive field 
shapes should be? And what's more, once you know
[1653] what they are and you want to go ahead and use 
these inhibitory connections that are strong for
[1657] similarly configured ... similar-looking features, 
and not so strong for non-similar - that requires
[1663] non-local information, right? To figure out how 
strong this connection ought to be right here,
[1667] this synapse right here would have to know all the 
connection strengths to this neuron from the input
[1674] and all the connection strengths 
from the input to this, you know.
[1678] And that's fine if you're simulating networks 
on a on a computer, but it's not fine if you're
[1682] building a robot or if you're trying to use your 
real brains, your biological system to try to
[1687] solve a problem. In other words we're trying 
to solve a global problem. You have a global
[1692] objective as far as coding: Minimize the error 
between your representation of the whole scene,
[1698] and do so with as few active neurons 
simultaneously as possible. Well,
[1702] that requires a lot of non-local information 
to do, but yet biology is constrained and real
[1707] hardware is constrained to use only local rules. 
So how do you do that? How do you learn these
[1711] things? So that's what i'm going to talk about 
next. That was our contribution with this stuff.
[1715] So here's a couple pictures of sailboats. 
This is work primarily of Joel Silverberg,
[1721] a past student the group who is now professor 
up at York University in Canada. So he likes to
[1731] sail. And so he used photographs of sailboats. He 
was not into equestrian sports, otherwise it would
[1736] have been "SADDLENet," because in fact that stands 
for "Sparse And Independent Learning," which is a
[1744] pretty good moniker, but really, strictly speaking 
it's really, "Sparse And Decorrelated Learning,"
[1750] because it's only paralyzed independence that 
he's imposing with his network. But he doesn't
[1756] like horses as much as he likes boats, so 
that's how that worked. Anyway, branding!
[1761] In the corporate world you know all about that. 
Okay. So here's Joel's network. Here's another
[1768] math-y slide. So in this, what we're going to 
do here is, I'm going to talk about individual
[1772] neurons. How do they work? Well, as I told you 
before, neurons in the brain that are talking to
[1777] each other in the cerebral cortex do so with 
these all-or-none events. They send spikes.
[1782] How does that work? Well, the neuron receives 
input from other neurons. This input can be
[1786] positive or negative. If you get enough positive 
input on a short enough time scale, so it doesn't
[1793] just all leak out (there's a time scale for 
how much you lose information in the past for a
[1797] neuron, right? You have a leaky integrate and
fire neurons, is we're talking about),
[1800] then if you if you reach threshold 
- represented here with green -
[1803] you'll produce one of these pink spikes. And 
so you're seeing spikes that are occurring
[1807] whenever you reach threshold. And 
then after a spike is produced,
[1810] there's some mechanism that sends the cell back 
down to some resting potential. Then you get more
[1814] positive and negative input and there's a lot of 
fluctuating stuff going on down here. These are
[1818] sub-threshold fluctuations. And the model 
includes, for each neuron, this internal
[1823] variable that's kind of like the voltage inside of 
a real neuron. It's a simplified version of that,
[1827] but has that character to it. And here again is 
our picture, you know, here's our visual scene.
[1833] Here's the patch we're trying to 
represent with a certain set of neurons.
[1836] Here's neuron 1 and neuron 2. There's connections. 
I'm gonna use 'q' to represent the feed-forward
[1840] connections from the various pixels in my 
patch to a given neuron, and they're indexed by
[1847] which pixel we're talking about and which 
neuron we're talking about. And then there's
[1851] our 'W's. These are our inhibitory connection 
strengths between pairs of neurons.
[1855] Every pair of neurons in the entire network is 
going to have an inhibitory connection between it.
[1861] And there's three learning rules. There's one that 
says how to change the threshold. And the idea is,
[1868] well, we want a sparse network where not many 
neurons are active. Okay? So what's our local
[1872] learning rule that's gonna achieve that? 
"n" is the count of how many spikes we got
[1877] in response to the last image we showed. And 'p' 
is our target value for probability of spiking.
[1883] So if p is ... actually, we would 
typically use numbers like 1 and 20. So
[1888] 0.05 is a good number for p. Actually 
biologists love the number p =  0.05,
[1892] but that's a coincidence. So 0.05 right here, and 
we'll see, all right, if you fire more often - if
[1898] you count more spikes than that - well, that 
minus that's going to be a positive number.
[1902] You better raise your threshold so you'll fire 
less. Right? If you do it less than this, well,
[1906] that's bad too. You don't want to be so sparse 
that nobody ever fires, ever. So, okay now you
[1910] better lower your threshold so you have a bigger 
chance of actually responding to some visual
[1914] stimulus. So you have a homeostatic mechanism 
for reaching a target level of sparseness, okay?
[1921] This is independent. Every neuron gets its own 
little learning rule to do this. They don't need
[1925] to know what the other neurons are doing to do 
that. Next thing is, I want decorrelation between
[1929] pairs of neurons. How do I achieve that? Joel 
says, Ah! I'm going to take the number of spikes
[1934] that occurred on one neuron times the number 
of spikes that occurred in the second neuron,
[1937] subtract my p squared target value - after 
all that's what you expect by chance.
[1942] If they're independent of one another - well, 
if they're decorrelated, right? - and then if
[1948] this is too big, then you're going to 
increase your inhibitory connection
[1951] and make them less corollary. If it's too 
small, you're going to decrease this value
[1956] so that they are a little more correlated, so that 
they go right to chance level. So you tend to fire
[1964] just as often as chance. And there's something 
I was going to say about that. What was that? So
[1970] this is the strength of the inhibitory connection. 
The minus sign comes later in case that's
[1974] a concern. There was something else I was going 
to say. Oh, I guess it was that this is also a
[1979] local learning rule. Yes. That's important. Why 
do I say that? It only depends on some internal
[1984] thing (my target value) and something that 
is known to the synapse. Any synapse between
[1991] any pair of neurons in the brain knows, if you 
like, whether or not the presynaptic cell (the
[1996] one that's coming into the synapse) is active and 
whether the postsynaptic cell is active. That's
[2002] allowed in my algorithm because that's local to 
the synapse. That's information that any little
[2008] synaptic connection between any pair of neurons 
will know. It's not going to know about these.
[2014] So this guy right here, W21 - it's going to know 
all about how active neuron 1 has been lately and
[2018] how active neuron 2 has been. But it's not going 
to know about the connection strengths over here,
[2023] you know, or about this. Actually this, yeah, it 
could know this. These things can know each other.
[2027] But about other inhibitory connections between 
neuron 1 and neuron 55 somewhere else? They can't
[2032] know that. But this learning rule only 
depends on the two neurons in question.
[2037] So that's really good, right? And then what's 
next? Oja-Hebb rule. So this is a Hebbian - oh,
[2046] I should say this is an anti-Hebbian rule. "This 
is a Hebbian rule" - who's Hebb? Hebb is a very
[2051] important psychologist - actually a Canadian 
psychologist, to bring up Canada again - and
[2055] in the '50s he came up with this maxim that 
turned out to be really prescient. He said look,
[2062] I think even though we don't really know 
much about what's going on the brain yet,
[2065] way back then, that there should be some causality 
involved in learning. And that if one neuron is
[2072] more likely to cause another neuron to fire, 
then the connection between the two should
[2076] be strengthened. That was his idea: That if one 
neuron causes another neuron to be more active,
[2082] that you should strengthen the connection between 
those two neurons. And it turned out that was a
[2087] really good idea. And all of modern machine 
learning and neuroscience benefits from this
[2094] idea. And there's lots of wrinkles on it. 
In this case, I'm showing an anti-Hebbian
[2101] sort of a rule that says, if you guys are are very 
co-active, you tend to increase the inhibitory
[2110] causal relationship between them. Right? In this 
case, though, we're doing the more typical thing,
[2114] which is ... So what are all these 
symbols here? 'x' represents the value
[2119] of my input. So that's the value of a pixel 
inside my little image to be represented,
[2125] right? That's the first time it's appeared, right? 
So far there's been no image at all. It's all been
[2129] about sparseness and independence. Now we get into 
representing the image. So I got my pixel value,
[2134] I subtract my representation based on my single 
neuron. So this says, how strong is my connection
[2142] right now between the input (that pixel) and 
my given neuron? Multiply it by how active the
[2148] neuron is ('n sub i') and that's my representation 
of the scene based on just one neuron at a time.
[2154] It's a local representation. It's impoverished 
representation. Nonetheless, take the difference
[2158] between those things. Now multiply by that 
activity again, and that's what we say we should
[2165] do to change the values of the synaptic strengths 
from the individual pixels to any given neuron in
[2171] our network. This is local. It only involves the 
activity of the neuron that's being talked to
[2178] (let's say neuron 2, for example) and the value of 
a single pixel, right? One of the pixels - not the
[2186] only one, but one of the pixels that that neuron 
represents. So this has a name on it other than
[2191] Zylberberg, the student who did the work in 
my group, and that's because this learning
[2196] rule had been thought of and used in the past. 
But never had this combination been considered
[2200] or understood. Joel's insight was that ... Similar 
to a network that Foldiak came up with way back in
[2207] 1990, that was similar to this but different in 
detail down here. This network works in a similar
[2212] way and produces a sparse representation. And 
Joel's network - Joel Zylberberg's network - has
[2217] the nice property that you can actually say what 
the objective function is that's being achieved
[2223] here. That was not the case with Foldiak's. 
Foldiak's network had some nice properties
[2228] and it produced sparse representations, and 
he was all about sparse coding. Was one of the
[2232] important early people thinking that sparseness 
was important for understanding how the brain
[2237] might work. But the math was a little trickier and 
it wasn't possible to write an objective function.
[2243] And another thing I want to say about it ... 
And just to make clear what I mean by objective
[2246] function (I'll do this real quick): These things 
right here are actually Lagrange multipliers.
[2252] They're not theta. It turns out they are related 
to theta and w, but I wrote them this way to make
[2257] the point that this is really, if you like, a 
constraint. And so is this. The way this network
[2263] works ... So what's the insight, right? How is it 
we're minimizing the RMS error across the entire
[2270] image - and it actually works! - this, is as we 
said earlier, a global objective, right? How are
[2274] we doing with local learning rules? Well, we're 
doing it by staying on a constraint surface on
[2279] a manifold in this huge dimensional, very high 
dimensional space of all the parameter values - so
[2285] every parameter value is one axis in this huge, 
high dimensional space - and what we're doing is,
[2289] we're maintaining sparseness and we're 
maintaining decorrelation between pairs
[2295] of neurons. And in that way, guaranteeing that 
individual neurons (the individual representing
[2300] actors, you know, in this population) aren't 
stepping on each other's toes. They're not all
[2305] representing the same part of the image. They're 
doing something different by maintaining ... So,
[2310] what do I mean by constraints and that 
it's being maintained? I mean that,
[2313] as Foldiak found empirically with his network back 
in 1990 (because his network was the same as far
[2320] as these two terms, but different for this term 
... Actually there was no term, there was nothing
[2325] on the left side for his. It was over here.). 
But these two things were the same for Foldiak,
[2329] essentially, and this was a little bit different. 
But he already noticed empirically that if he had
[2334] the learning rate set really high for the first 
guy, for this lambda, and really high for beta,
[2340] that the network worked a lot better than if 
he didn't have these guys set really high.
[2344] In other words, if he had this the learning 
rate for this term to go the same as these guys,
[2349] the network didn't work very well. And that's 
written in words down here at the bottom. And why
[2354] is that? It's because of this constraint thing 
that Joel figured out: That this is an example
[2359] of constrained optimization. And the reason it 
matters is that if you take the derivative with
[2365] respect to 'q' of my lower left-hand term here, 
you don't exactly get the term on the lower right.
[2370] You're missing one of the sums. The sum inside 
the inside the parentheses should still be here,
[2376] right? In other words, you should be summing over 
all the neurons in the network to figure out what
[2380] the representation of that pixel in the image 
is, but we just got rid of it. Why is that okay?
[2385] It's okay because these two terms are doing their 
job. They're making sure that different neurons
[2390] are not active very much, and they don't get 
active at the same time above chance. Well, if all
[2394] the neurons aren't active very much and if they 
don't act together more than chance, it hardly
[2399] ever happens that two neurons are simultaneously 
representing the same part of the image, just
[2404] because of that constraint. And that's how you can 
impose, through this set of constraints up here,
[2410] how we were able to learn a global objective with 
local learning rules. That was the basic insight.
[2415] And I was over the moon with this because I
said, okay! Finally I get to see what a
[2419] constrained optimization looks like! It's sort 
of obvious when somebody shows me - everything's
[2423] obvious when somebody shows me - but I
think this was a really new idea.
[2428] And why it is that even smart people like Foliak 
hadn't mentioned, seen empirically why is it
[2434] that you get these changes in - these divergences 
in - how fast your rates ought to be. Well,
[2438] here's the answer, I think. And it makes a lot of 
predictions. So, first of all it does as good as
[2444] any other sparse coding network for predicting 
... Um, here's a Rhesus monkey receptive field
[2450] shapes in in the primary visual cortex. We get the 
full range, we get the little point-like things.
[2454] We get the Gabor-like guys that are multi-modal 
with lots of wiggles. And we get the long thin
[2460] edge detector type things. Great. So it 
seems like it's getting the right features,
[2463] but that's all. That had already been done 
by other models, albeit not biologically
[2467] plausible ones. But then the next question is ...
Okay. So the answer is it's true in real brains.
[2472] Now we can ask, "What predictions can we 
ask about beyond receptive field shapes?"
[2476] And so, for the previous networks - 
even the really sophisticated ones -
[2481] the way they operated was, you put in by hand 
that you wanted the inhibitory strength between
[2486] between your pairs of neurons to be determined by 
the overlapping receptive field shape. You take a
[2491] dot product between the features they care about 
and use that to put in by hand what the what the
[2498] inhibitory strength ought to be. But our network 
learns this! And it's not just a diagonal line
[2502] between inhibitory connection strength and dot 
product between features. Right? You get this
[2507] spread of neurons. And sure enough, it does have 
the right quality! You have a lot of points in the
[2513] upper right, and you've got points in the lower 
left. But you've got a lot of other stuff too.
[2516] And what's nice about that is, it makes 
predictions for connection strengths. And in real
[2520] brains, this hasn't been this hasn't been tested, 
and that's because it's a hard measurement to
[2526] do [catches breath]. Excuse me. To do. I always 
choke up when I look at these data. But you know,
[2530] it's a hard measurement to make, but it's one 
that I can't wait to get clarity on, because it
[2537] will really be a good test of our model. Our model 
can be falsified, you know? ... And here's some
[2542] data I actually took with Tomas Hromadka back 
in my postdoc, before I was a professor. And
[2549] the data - actually, I shouldn't tell you 
this, but it was so well fit by a log normal
[2553] distribution that it - like, if we did a chi 
squared it would have been a bad fit because
[2557] it was too good of a fit! Which is a problem 
you don't usually face in biology. But anyway,
[2561] really good fit for log normal. 
What am I plotting? I'm plotting ...
[2567] Oh, am I getting ahead of myself? No, 
I think that's correct. I'm sorry.
[2570] My light is covering my axis. I think
this should be activity as a function
[2575] of ... oh yeah, spontaneous firing rate is the 
horizontal axis. I just wasn't paying attention.
[2581] And this is a histogram. So I'm saying, how many 
neurons have a certain basal level firing rate as
[2587] they're responding to whatever they're responding 
to? And it says A1, not V1. That's not a typo.
[2591] This was in the auditory cortex. So we recorded 
the auditory cortex in my lab. We need somebody
[2596] else to look at this in the visual cortex. 
Let me make sure I know what I'm looking at.
[2605] Number of cells. I'm trying to remind 
myself whether this is ... uh uh uh
[2612] yes, this is. So this is our model on the 
top, right? The SAILNet model. And what
[2618] it's showing is a nice log normal fit for the 
number of cells for a given amount of firing.
[2624] And the same thing on the right, but where we use 
different contrast stimuli. It turns out it looks
[2628] very exponential if you present very high contrast 
stimuli to the network, if it was trained on
[2634] lower contrast stimuli. So what's been seen in 
V1 experimentally looks more like the exponential
[2638] fit, but now we've got a prediction: If you use 
lower contrast stimuli, we expect a log normal
[2642] fit. And to my knowledge that still hasn't been 
presented in a way that ... So I need to go out
[2646] and hassle my visual cortex recording buddies 
and have that presented to me in a way that I
[2650] can make a direct comparison. Anyhow, log normal 
distributions of activity is what we predict.
[2655] We also predict log normal distribution for 
connection strengths across the network. It turns
[2661] out that if you ask, "Well, how strong are my 
inhibitory connections between pairs of neurons?"
[2666] It looks, you know, not a perfect fit. In fact, 
there are some telltale departures of log normal.
[2671] Maybe that's useful. In fact, if you take these 
seriously, hey it looks like a good ... Well,
[2675] okay, I want more data before I make a strong 
claim. But it does look like at least one of
[2680] the few places where somebody has looked, they 
do see a similar kind of distribution for the
[2688] connection strengths. However, once again it's 
not exactly the right data set. This is excitatory
[2693] connections, and i'm talking about inhibitory 
connections. It turns out to be a lot easier
[2696] to measure the strength of excitatory connections 
because you can stimulate the presynaptic neuron
[2700] and then record in the postsynaptic. It's hard to 
measure how much you shut down the transmission
[2705] that would have happened by stimulating the 
pre-synaptic neuron when it's an inhibitory
[2710] sort of a connection. When it tends to depress 
or prevent the activity. So anyway, it's a harder
[2715] measurement to do. I guess beautiful theories 
are ones that are hard to falsify, but I like
[2722] ones that are really falsifiable. So I'm looking 
forward to getting ... We've already seen some
[2726] corroboration, certainly with the receptive fields 
and with these almost-right data sets. But I'm
[2731] looking forward to actually getting the real data. 
This is an example. I'll just mention one slide.
[2739] The thing I showed you in the last page, I'm 
talking about SAILNet, biologically plausible
[2743] local learning rules. Got spiking neurons that 
produce these all-or-none events, as opposed to
[2748] graded outputs. Very realistic in that sense. It's 
not realistic, though, in the sense that I had
[2754] the same type of neuron representing excitatory 
and  inhibitory neurons. In your brain, in your
[2760] cerebral cortex, you have dedicated different 
population of neurons. Two separate populations,
[2765] one that's excitatory and one that's inhibitory, 
with rare exceptions. With biology there's always
[2770] some exceptions. But the vast majority of the 
neurons in your cerebral cortex either promote
[2776] the activity of downstream neurons or inhibit 
the activity of all the downstream neurons.
[2783] And so we've cooked up - and by "we," I mean 
Paul King and again Joel Zylberberg - cooked
[2787] up a network with separate populations. 
And then you need more learning rules,
[2791] right? Because you've got excitatory neurons 
and inhibitory neurons. You have to have
[2795] five different learning rules instead of 
just three. But without belaboring the point,
[2800] you can do this and it gives similar results. 
The receptive fields aren't quite as good,
[2805] at least in our hands, what we've fooled with so 
far. But it does work. And then it makes other
[2811] predictions about inhibitory versus excitatory 
connections. And there's a whole bunch of ...
[2816] I'll just give a quick laundry list 
of predictions you can make beyond
[2822] just receptive field shape. One is that ... Well, 
first of all, yeah. Accurate receptive field
[2826] shapes. That's the first thing we get. Next thing 
is there's ... Oh yeah, we talked about that,
[2833] that there's this correlation - and not just a 
correlation between the reciprocal overlap and the
[2838] inhibitory strength between the pairs of neurons, 
but that you get an interesting signature for
[2843] what that relationship is. That's not what people 
would have guessed or what you'd get from previous
[2848] models. Log normal distribution of firing rates. 
Log normal distribution of synaptic strengths.
[2853] We also can now say that this particular 
population of inhibitory neurons in our network,
[2860] that are actually called "FS" for "fast spiking," 
that are named so because of what they do when you
[2865] inject current in these neurons. They tend to 
fire quickly. And they have other properties as
[2869] well that distinguish them from other inhibitory 
neurons. Well, we can say what the computational
[2874] role is for those neurons! They are there to 
decorrelate pairs of excitatory neurons. And
[2881] the excitatory neurons are the ones that are 
actually representing the visual input. So
[2887] when I say "simple cells" in V1, a neuroscientist 
will say, "Oh yeah, you're referring to all the
[2892] neurons in the primary visual cortex that have 
certain receptive field properties." Well,
[2896] some of them are excitatory and some inhibitory. 
If you ask them, "Which ones are representing the
[2900] input?" [they'd say], "Well, I don't know!" 
In our case, we know that the inhibitory
[2904] neurons are not representing the input. They 
are providing the role of decorrelating pairs
[2909] of excitatory neurons. And that means that they 
have some different properties. One is that ...
[2914] Oh yeah, they have the role of decorrelating
excitatory neurons. ... One is that you don't
[2917] need that many inhibitory neurons because 
the excitatory neurons from an over-complete
[2921] representation. So you have lots of similar 
receptive field shapes. Similar features that are
[2927] represented by different excitatory neurons in the 
network. It turns out you can just have ... One
[2931] inhibitory neuron can service a group of 
five or so different excitatory neurons,
[2938] because they're similar enough in their shapes 
that if they all send excitatory inputs to the
[2944] inhibitory neuron, and then it sends back its 
inhibition to all the rest of them, they can
[2950] dis ... let me say this right way: Each of those 
excitatory neurons in that little sub-network can
[2955] effectively inhibit its neighbors (who are coding 
for similar things) without too much inhibiting
[2960] itself through that network, so that the mechanism 
still works. And so the network works fine if
[2965] you decrease the number of inhibitory neurons 
until you get down to a ratio of 1:4 or 1:5.
[2970] And that's the ratio that's in our brains. 
So as far as I know, it's the first theory
[2974] that actually makes a claim as to why - it 
makes a prediction, actually - for why it is
[2979] you've got more excitatory than inhibitory 
neurons. And what's more, it also says why
[2983] should it be that inhibitory neurons fire 
more. Well, the inhibitory neurons are not
[2988] forming a sparse representation of the input. 
They're there to decorrelate excitatory neurons.
[2992] So the excitatory neurons have these sparse 
responses. The inhibitory neurons are more active,
[2998] but that's okay because they're not part of the 
representation. They're there in small numbers but
[3002] with an important role of decorrelating pairs of 
excitatory neurons. So anyway, there's a laundry
[3009] list of things you get from this sort of thinking, 
this sort of principled approach to thinking about
[3014] what's going on. And also treating this ... 
I mean, in the first place this is a vision
[3019] model. Like, we're trying to understand the 
problem of vision. We're not just trying to
[3023] model the activity or connections of neurons. And 
there's a lot of important work that's done where
[3027] that's the only handle they've got on what's 
going on. But I really like to solve a problem
[3032] where I'm thinking about, like, "What is 
it the brain's trying to do?" [hesitates]
[3038] Anyway, it worked out for us, for this model. 
And sparseness can decrease during development.
[3044] So I'll briefly mention that one knock against 
sparse coding is that there is data from ferrets,
[3049] actually. When you look at their neurons during 
development, it turns out that the neurons get
[3054] more active with time, not less. You say, "Wait 
a minute. If during learning they're getting more
[3058] active, that sounds like sparseness is not the 
objective function." And indeed, if you were doing
[3064] some unconstrained optimization, maybe that's what 
you'd expect. But for a constrained optimization,
[3069] it's easy to see - and in fact we've cooked 
up examples where this is the case - if you
[3073] just happen to start out where you're a little too 
sparse, you're going to move up in your activity
[3078] until your sparseness is just right to hit your 
objective: your p-value is what you set it for.
[3084] Because you have a homeostatic mechanism, 
not just a just an unconstrained "make it
[3088] as sparse as possible" sort of mechanism. Anyway, 
so it turns out that we can address that concern
[3095] So, here I've given you an example of biology and 
physics inspired computing. In fact, we've come up
[3102] with a neural network that has nice properties, 
and we're actually using it to study statistics
[3107] of natural scenes and sounds. We're using it for 
things beyond just understanding the brain. And
[3111] here I've drawn a funny cartoon of a laptop 
that's thinking about this. And in fact,
[3117] I did that on purpose because you know,
machine learning ... Yeah, so here's the
[3123] opposite statement: Machine learning informs us 
about brains. But it also informs us all the stuff
[3128] about real artificial neural networks. In other 
words, if you want to really build a robot - I
[3133] think I've already mentioned this a couple 
times, but if you want to build a robot that
[3136] actually does what any neural network does, you 
have to face all the same problems - or many of
[3141] the same problems - that biology does. You need 
local learning rules, right? And you're probably
[3145] going to use an all-or-none ... Well, I shouldn't 
say that. You can use graded if you want. But
[3150] there's good reason to do the things that biology 
does. And in some cases it's unavoidable. I mean,
[3155] I would argue that there really is no way to 
build a network with ... I don't know. I mean, I
[3162] guess it depends. It's a threshold. Like, 
it depends on how many neurons. If I say,
[3165] you know, 10 to the 10 neurons, we can't 
build anything that big anyway right now,
[3169] so fine. But even a far smaller network, trying to 
have individual synapses aware of the connection
[3176] strengths of all the synapses in the network? 
You just can't get there from here, with physical
[3180] wires connecting those regions. And in fact, even 
though our goal with this project was really to
[3186] understand the brain, other groups have built 
physical devices that use these algorithms. So
[3192] there's dedicated hardware out there, in cameras, 
by a couple different engineering groups who
[3199] built this thing. Which tickled us 
because that wasn't our primary objective.
[3205] So I think it's an important thing to understand 
- even if you're interested in understanding
[3210] algorithms, understanding artificial thinking 
machines as opposed to just the brain - because
[3215] it's a problem we're going to have to face 
eventually, if you want to go beyond simulating
[3218] deep neural networks and stuff. Right. Okay So, 
how are we doing for time? I think we're over.
[3227] Oh! Well, how about this? 
I'll just say quickly that
[3234] one thing that comes out of this 
thinking is that there's pre ... I
[3239] think I mentioned at the very beginning 
that there's pre-processing that everyone
[3243] does - ever since Bruno Olshausen started doing 
this stuff in the mid-90s - which is, you whiten
[3250] your inputs. And for a visual image, this is 
what I mean, visually. So here's a photograph
[3254] at the beach. And then here's a whitened image. 
And you see it's kind of a ... It looks grayer,
[3260] but there's a lot of emphasis on the edges between 
things. You lose the DC, the slowly varying stuff
[3266] is taken away. The point is that natural images 
have a power law power spectrum. There's a lot
[3272] more power in the low frequencies than high 
frequencies. That's true of almost anything you
[3276] measure in nature. It turns out it's ubiquitous in 
nature to use power laws or things that are close
[3281] to power laws. You tend to get a lot more power 
in low frequencies. And so the first thing you do,
[3286] often, when you process signals, is you flatten 
the spectrum. And it goes by a lot of names. You
[3291] "whiten" it, or you "sphere" it, or use principal 
components analysis if that's the particular
[3295] whitening scheme you like. Whatever it is. In our 
network, it turns out that if you don't do that,
[3302] it fails. And so I'm now beating my chest 
about the fact that my network can't handle
[3307] things that previous networks could handle. Why 
is that? It's because that mechanism I told you
[3313] for for making local things work, local rules 
work, to produce a global objective - that thing
[3320] gets overpowered if you have too much variance in 
your data along some directions. Those directions
[3326] dominate every neuron. Your network learns 
those directions; they ignore the little stuff
[3330] and you get a really bad representation of the 
visual world. You get representations that don't
[3334] have any fine detail. Whereas the usual methods 
that people cooked up that aren't biologically
[3338] plausible - turns out that they they don't get 
fooled by that. You don't have to pre-whiten,
[3344] if you want. You get the same answer either way. 
And this just quantifies that step. So our network
[3348] is fragile. Oh yeah, there's a bunch of things 
we're doing now. I'll skip all that. I'm just
[3353] going to put up my thanks slide and just say: The 
upshot of the last thing I was saying is just that
[3361] it turns out that we have a new explanation for 
why your retina whitens images before it gets sent
[3367] to the cerebral cortex. Even though there are some 
really smart people in neuroscience and computer
[3372] science who say, "Well, I don't buy the sparse 
coding stuff because if that's such a good idea,
[3377] why don't you do it in the retina? Why do you 
wait till you get all the way to the cortex to do
[3381] whitening?" And there's a couple good answers to 
that question. But we have a new - qualitatively
[3384] new - answer to the question, which is: If 
you want to do it using biologically plausible
[3388] learning rules, you may be forced to do a separate 
pre-processing step of whitening before you can go
[3395] to the stage of using the sort of mechanisms 
we figured out. The only ones I know of for
[3400] doing sparse coding using local rules. Anyway, the 
people with the big names at the top in purple are
[3406] the ones who actually did the work of the things 
I showed you. Joel Zylberberg and Jason Murphy and
[3410] Paul King; Nicole Vivienne Ming, Eric Dodds, 
Jesse Livezey, Ji Hyun Bak. And then there's
[3418] many other people. I think here, like, it turns 
into microfiche at the bottom like an eye chart,
[3422] but I'm always loathe to cut people off of my 
appreciation slides. But thanks for our funding,
[3428] here in the middle. And if there are questions, 
I'll take them. But thanks for listening!
[3436] Well, thanks Mike! So, anybody that 
wants to, there's a question and answer
[3440] feature on Zoom. You're welcome to submit 
questions. I don't see them pouring in yet,
[3445] so i'm just going to grill Mike personally. 
People are dumbfounded by what they just saw.
[3451] But anyway, yeah, go ahead.
The pace was rapid.
[3455] Yet I still went over! That's my homework.
[3457] I don't think whitening can be 
done with local rules, right?
[3461] Because if you want to decorrelate 
pairwise, you've got to know about
[3464] pairs that are very far apart 
in the visual field, right?
[3472] That's a great question. When I say "local," 
I don't mean local in the visual world.
[3477] I mean local in the network. So
I'm allowed to decorrelate far away things in the
[3485] visual field as long as there's a pair of neurons 
... As long as the network is configured so that
[3491] the things I'm decorrelating are talking to each 
other. The place where they talk - that synapse
[3495] where they talk to each other? I'm allowed to 
use the activity of those two neurons if I like.
[3499] In principle. But in practice,
[3503] the way the retina is laid out, is whitening 
plausibly local with a realistic architecture?
[3512] So it turns out it's a subtle story of whitening 
in the retina and decorrelation in the retina.
[3517] It was long thought ... So a bunch of smart people
[3521] with beautiful data and good theories back in the 
- gosh, back in the very early 90s - You know, joe
[3530] attic and [thinking] ... Yang Dan, for example, 
and ... Gosh, I'm so slow to come up with names
[3540] in real time! Sorry? I said, "My thoughts were 
short; my hair was long." I remember those days.
[3549] Yeah, well, I think in my case it's a it's a 
natural phenomenon. But anyway, the bottom line
[3555] is that there's a bunch of good ideas,
and I think those ideas are true,
[3560] but they're not the whole story about how you 
achieve decorrelation and redundancy reduction
[3566] through receptive field shapes. There's a nice 
paper - from Marcus Meister's group from a few
[3573] years ago, actually, I think 15 years ago - that 
actually addresses that pretty specifically in the
[3579] retina. But they did a lot of careful measurements 
and they find that there's a large role for things
[3583] other than the receptive field shape, having to do 
with dynamics and other aspects of what's going on
[3587] in the retina. So nobody, I think, nobody would 
dispute that whitening is going on in the retina.
[3594] Or that it involves anything 
other than biologically plausible stuff. But it
[3599] turns out that the range of mechanisms involved in 
the retina for doing these sort of operations
[3604] is much bigger than you would have guessed based 
on the way people were thinking about it
[3610] over 10 years ago or 15 years ago. 
And actually, it's a good question
[3616] the extent that that's been assimilated by the entire 
community of theorists who are thinking about
[3620] visual models. But there's no 
issue with locality if you
[3628] have a neuron in the ...
You have, you know, ganglion cells,
[3634] for example, whose axons form the 
the optic nerve, right? Different ganglion cells are
[3641] responsible for, are hearing from, or seeing I should 
say, different sizes. Different receptive
[3647] fields out of the retina, right? And some 
are bigger than others. And how is that possible?
[3653] Well, it's because there's a bunch 
of photoreceptors in a big array, right? And a large
[3659] array might feed into ... And there's a bunch of other 
neurons, there's the bipolar cells and there's the
[3664] amacrine cells. Amacrines have long lateral 
connections to other amacrines ...
[3670] Actually, is that true? I don't know. Got to think 
about that, who's talking to whom exactly. Well,
[3674] I'll play it safe and say something I know 
is true, which is: Amacrine cells have lots of
[3678] long-distance connections. And it's through 
those - it's through the changing, the relative
[3683] importance of those long distance connections - that 
the retina can modify the spatial correlation of
[3689] the images that gets sent on  
to the thalamus and ultimately to the cortex.
[3695] And the thalamus is the sort of station halfway 
between the retina and the cortex.
[3703] It's apparently performing 
a sort of whitening operation, but in time.
[3708] It's doing temporal decorrelation, if you like. 
It's getting rid of the temporal
[3713] correlations. That's the way the story 
is usually presented and thought about: That
[3718] you get spatial whitening going on in the 
retina, and then in the thalamus, that's responsible
[3723] for temporal decoration. And then you get to the 
cortex. And then we would say, well, it looks like
[3727] sparse coding gives us a good idea of what we 
think is happening. And we would say, "Ah!
[3732] And that was sort of the way it had 
to be. You had to do some pre-whitening, if you
[3737] want, to use local rules in the cortex." I 
don't know if that addresses your question.
[3743] In many different ways. Yeah, so natural images, 
right? With power law correlations and structures.
[3752] How far down the chain do those power laws ... 
Does that all get taken out at the retina
[3759] with the retinal whitening, or do you 
find receptive fields that are
[3764] themselves power law? Because I see 
mountains and I see a little mouse on my desk ...
[3771] It's a good question, if you're asking how 
the spatial distribution ... So when you look
[3777] at the visual cortex in V1, right? 
Well, first of all, look at the retina! In the
[3782] retina, you've got different structures going on 
in the fovea and in the foveola, way inside the
[3788] fovea compared to the periphery. And the 
spatial ... the range of size of things that matters
[3794] changes depending on where you are in the retina. 
It also changes in the in primary visual cortex,
[3800] in V1. And so part of the way this is addressed 
is through a range of things that happen in a
[3806] given part of the visual field, which is the way 
I was presenting it in the talk. But part of it
[3812] is handled by looking - moving 
your eyes around, which we do constantly, right?
[3818] And then if there's a lot of high 
spatial frequency content somewhere in the
[3822] visual scene that you think might be important, 
or there's all kinds of objective functions
[3826] you might try to figure out where people tend 
to look where they look, you put your fovea
[3832] there. And by looking there, then you have 
access to stuff you didn't have access to when you
[3836] were looking away from it. So that 
complicates the story a little bit, and it would
[3841] change the way I would answer the question. But if 
we talk about a patch that's, you know,
[3845] 10 degrees eccentric or whatever - however you want 
to phrase that, but 10 degrees away from
[3851] the center of your vision - and ask: What's 
the distribution of ... That's a good question, "What's
[3858] the distribution of, say, receptive field sizes 
or spatial frequency?" And I don't
[3864] have a ready answer for you about what the 
distribution looks like for that. But I do
[3869] have a feeling that it's going to be limited. You 
know, you're not going to go
[3873] all the way down to the smallest scales 
unless you're in a representation that's
[3880] of the fovea, right? And it turns 
out there's other differences between the fovea
[3885] and elsewhere, which would complicate the story too. 
But in terms of what our network does, I
[3893] think to answer that question in a in a meaningful 
way we need to look at really big patches,
[3898] right? So that we can get a really big range 
of sizes. And you kind of got a feeling for how
[3902] big our patches were. It turns out we're 
limited by computer speed and size and all that.
[3910] Because you know, how big a patch can we handle? 
Well, we certainly go 16
[3917] by 16 size patches. But we're not doing 1,000
by 1,000 right? And so I think ...
[3925] It's a good question, though. There might be a 
way to answer that with pencil and paper, with
[3929] some good ideas to at least get a hint for 
it. I don't have a quick answer for you,
[3935] but I would guess that it's just going to 
reflect what you see in the input. Except if
[3942] you do a perfect job of whitening, right? Yeah, it's 
a good question. Once you do the whitening ... So then
[3947] it comes down to what about the structure 
of natural scenes beyond the power spectrum,
[3953] which is not well understood even though deep 
learning has done a good job of extracting some
[3959] pieces of information you thought would be hard 
to get. It's not clear exactly how it's getting
[3963] that information and it's not clear that it 
really reflects the full range of structure.
[3971] So, it's funny right? Like
[3976] this is so analogous to discussions - 
like we were talking about before we were recording -
[3982] about how you organize an economy of 
agents who have access to only to certain kinds
[3986] of local knowledge, right? And we were talking about 
how you have a natural inhibitory thing
[3991] because you have competition between firms, right? 
And then you're talking about this
[3995] Hebbian learning rule, right? If two things 
are firing at the same time you strengthen their
[3999] connection, right? One of the 
things that people talk about - and I don't
[4003] think there's a particularly clean answer, right? - 
is the existence of companies, right?
[4007] Firm formation. Like, why isn't everybody just 
doing their job and then contracting out
[4013] what they need to hire and being paid 
by people who need them? Why on earth do you have
[4019] people in a company, right? And 
of course we know it has something to
[4024] do with the frictions: The fact that information 
processing isn't free. So I can't find people
[4029] to be my customers and people to be my 
employers with zero cost.
[4034] But it really does sound so similar 
to sort of an agent-based economy and why
[4039] you would get firms, right? Like the sort of 
networks that are organizing to have a strong
[4045] connection are sort of the people 
who logically belong in a company.
[4049] And particularly if you want to go with sort 
of all-or-none penalties on weights, then
[4054] you're really like, these guys are in 
a company and these guys are not in a company.
[4058] And then, of course, then you have the "X" inhibitory stuff, which is this company
[4063] competing with that company. I wonder if 
you could do some really interesting things
[4068] with economics as well as vision, with sort 
of the whole "rules are locally learnable."
[4076] I like that setup. I'm sure there's 
something to be done there. As we discussed
[4082] before, and as you just mentioned again 
now, there's a natural inhibition, if you like,
[4088] in the form of competition.  
There's some customers out there who
[4092] want to buy whatever it is you're selling. 
Somebody else is selling the same thing. So it
[4097] comes at a cost if you and your competitor both 
try to solve this, sort of occupy the same niche
[4103] in a complex economy. And in this case,
[4106] Brand differentiation, blah, blah, that people...
[4110] Sure. Brand differentiation and 
beyond that, actual different delivery
[4116] of services, right? It's the different ... Or products, 
whatever it is, right?
[4120] Right.
[4121] The problem in the brain is that there 
isn't a natural competition. We had to impose one.
[4128] So, in a sense we're solving ... You know, 
in that way, I could take a strong
[4133] position and say: Well, we're solving a problem that 
is already solved in the case of
[4138] companies, or you know in the financial 
or whatever the business, the market, right?
[4143] But I mean, that's not exactly true. 
It's a different kind of competition. And
[4149] in neither case is it a total 
competition. There still is ...
[4155] Somebody who makes better ice cream can come 
in and out-compete somebody who's got ... even if
[4159] there's already somebody selling ice cream, right? 
And in fact that's kind of true in our network, too.
[4164] The mechanisms we have are where, depending on how 
active I am, I'm going to shut down the other guy,
[4171] right? And depending on how active he is, he's gonna 
shut me down. But if I'm a better fit to the data,
[4176] you know - which I guess the analogy is if I'm 
selling something that customers want more,
[4180] right? - then I'm more active. And then I'm shutting 
every guy down more than they're shutting me down.
[4185] So, in a sense the network is set up just like ... 
It's the story we hear from about bees, right?
[4190] You know, that when bees decide where they're gonna 
make their next hive, right, a
[4197] bunch of foragers go out and find spots. And they 
come back and they compete. And they're honest!
[4202] They wiggle as hard as they should based on 
the quality of the place they found. And they shut
[4206] up if somebody else is wiggling more, because 
they all ... You know. It turns out that the algorithm
[4210] is actually good for the whole hive to do that, not 
just for individuals to try. And the same thing's
[4214] true in our network. It's interesting, 
though, because in the marketplace,
[4221] in some sense you want the whole market to 
succeed, but it really is every firm for itself
[4230] in terms of what the firms are trying to do. 
You know, a firm doesn't try to design its
[4237] its practices or which niche it's going 
to go for because it thinks it's good for the
[4241] long-term economy. Probably they're saying, well, 
we're going to go out of business if you do this
[4244] and we're going to make a lot of money if we do 
that on a reasonable time scale.
[4249] That's a really interesting question. Like, suppose 
you had a complete command economy.
[4255] Would you wind up, because of the constraints of 
local information-sharing and finiteness, saying
[4260] that the politbureau has decreed 
there will be these small competing entities
[4265] called "companies" and the most efficient way to 
handle the costs of transmitting information and
[4271] local learning rules ... Like, yeah yeah! So 
you're saying in the brain you need to impose this,
[4276] well, you're saying it's for free 
in a market economy, but if you had a command
[4279] economy maybe you would actually be back to, "Well, 
now we have to impose this to get an efficient
[4284] representation of the economic state."
[4286] Sure. I think an open market system, that's essentially
[4289] what's happening. The controls that exist allow 
and encourage independent competitors.
[4297] Right. And is the result of people's choices about how to 
self-organize as a society and so on and so forth.
[4302] So it's possible that yeah, it's not 
that different than you imposing it.
[4308] In fact, right, isn't it the case that there are ... So I 
saw a talk on this recently that, I forget who
[4313] it was, but some CEO of a very successful company 
was saying, you know, if what you want to do is
[4319] avoid being taken over by the Young Turk company 
that comes in and is disruptive and changes your
[4325] business model - this is really dangerous for old 
companies, even (really, especially) the successful
[4330] ones, right? They got this business model that 
works; they don't have an effective way of
[4334] dealing with some new company that 
disrupts the market. But one way to deal with
[4340] it is to build a separate company within the big 
company, and to guarantee there's no communication
[4346] between that smaller company and the rest of the 
company. And he gave examples of ... I've already
[4352] talked about ice cream. I think it was an ice 
cream company, or maybe it was a computer company ...
[4355] where examples where it worked, and 
where it didn't work. And in fact, what made it work
[4361] and at least ... And you know, maybe he cherry- 
picked his data; you know more than I do
[4366] about about this sphere. But the companies in
these examples where it worked was where the
[4372] the bigger company did something that's 
really rare in big companies. They said, okay,
[4376] we're not going to manage this subset of 
the company. We're going to choose a few
[4379] good people to be in charge, and we're not 
even going to pay attention to what they're
[4382] doing. And they're going to act like our 
competitor. They're going to disrupt us.
[4387] And if they succeed at it, okay, then we're going 
to (in a in a way that benefits our company), we're
[4393] going to integrate that into the rest of our ... But 
we're not going to get taken over by, or you know,
[4398] thrown out to pasture, by some competitor. And 
he gave examples where that actually works.
[4403] So in some sense, there are cases where what 
you want to do is to spawn truly disconnected actors.
[4412] Because in some sense, right, 
an economy has actually a more dynamic issue
[4419] than ... You know. It's as though the sort 
of, "what you were going to see" - the statistics of
[4424] visual images, right - was completely changing over 
time, right? Because technology completely
[4430] changes what the business opportunities are, 
right? So there isn't kind of a 'right
[4434] answer' for the feature to recognize. As you point 
out, that can get disrupted by technologies.
[4439] There's another right answer for the feature. And 
so on. So it is like ... I think it has one more time
[4444] dimension, right? It's like machine learning 
in a continuously evolving ensemble rather than
[4450] with a static data set. It seems to like 
interesting connections.
[4456] So, I would make a stronger statement too, which is: 
Aside from thinking of it as a time scale, it's
[4462] possible ... We don't know how 
much of our brains are ... Based on the
[4469] length of the genome, we think it's really unlikely ...
Genome is like, what, it's a thumb drive from
[4473] 10 years ago. It's got, what, two gigabytes of data. 
And it's redundant on
[4480] top of that. And it encodes for everything in my 
entire body, including the parts that don't work
[4484] well and including the parts that have nothing to do 
with my brain. And so the idea that
[4489] we're encoding all this is ridiculous, right? 
Clearly we're learning from experience. We're
[4493] learning from visuals as I showed in this. You 
know, nothing's put in by hand here, except for
[4498] a couple learning rules and some initial wiring 
which is essentially all connected. Like,
[4503] there's not much structure there. You learn 
it from the statistics of the inputs. And so,
[4508] to what extent does our brain really work that way? 
There's a bunch of counter examples that suggest
[4512] that there's a lot, there's something else going 
on too, right? You know, a foal drops and within
[4517] you know, 20 minutes, it's walking around.  
Chances are it didn't learn that using these kind
[4522] of algorithms. Deep learning as well 
as our algorithm takes lots of - millions of -
[4526] iterations to learn. That's not realistic. 
If you calculate (back of the envelope)
[4532] how many images I've had to see before my brain 
trained up, it's way fewer than what you need for
[4537] any of these networks, right? So all I'm getting at 
is that there's probably a lot of hard or soft or
[4543] firm coding going on, or whatever you want to call 
it. It's not all learning.
[4550] I saw a pre-print that I'm not going to bother 
to read, because what would be the benefit to me?
[4554] But I did read the abstract, and as I understand 
it, it's one of these things where you can
[4559] show some amount of brain remodeling 
in people who've had COVID. And they're like,
[4563] "Oh my god, it's eating your brain!" And then 
there's this counterpoint which is actually:
[4569] The remodeling seems to be in the olfactory cortex. 
So it's entirely possible that you just lost your
[4575] sense of smell for three months, and your brain 
says, okay, well let's start adapting to this new
[4581] ensemble where we're not getting smell 
data. And that it'll probably rewire back
[4586] and you'll have, you know. But your recovery 
of your sense of smell may actually be delayed
[4591] as you learn to use the olfactory stuff again, 
as it comes back physically online. But that
[4596] does speak to the sort of, yeah, if the ensemble 
changes, maybe your brain is rewiring in real time.
[4601] And maybe there are non-trivial ensemble changes.
[4603] Well, and there are experiments where in
[4605] animal models they reroute visual and auditory 
information to different parts of the cerebral
[4614] cortex and it works better than you'd expect. 
The rules seem to be ridiculously robust. And
[4622] there are children with hemispherectomies - you 
take out half their brain because of severe
[4626] epilepsy or other problems. And if you're not 
an expert, you see the kid playing a few years
[4630] later on the playground, you can tell 
something's up, but the average person watching
[4636] wouldn't notice right away that that kid 
has half his brain or her brain missing from
[4641] a few years ago. Our brains 
are extraordinarily robust and plastic,
[4646] despite the fact that it seems like it's mostly 
just a few rules. Plus you look at how quickly
[4652] humans evolved from other creatures. I mean, 
with random mutations and natural selection
[4658] that's just not possible if it's too brittle and 
there's too many rules imposed and too much top
[4663] down control. I'm arguing for some aspects 
of market economy in evolution, I guess. But anyway,
[4670] it seems like learning is pretty powerful.
[4677] Is there literature on
[4678] the old style CS universality classes - 
'p' and 'np' - in a machine learning context?
[4685] Because you're sorta saying, 
"Hey, computations you can do with only local
[4690] learning rules." Maybe that's a class different from computation ...
[4695] Yeah, okay. That's a really good question and I've got two 
answers - two classes of answers, I mean. The first is,
[4701] so I gave you a one slide 
shout out to this result we've had more recently
[4706] about how the retina might be important 
for whitening because you have to do that.
[4711] But how do you make a claim like that? How do 
you tell people - and this is our problem.
[4716] It sits right now on the ariov, this paper, but 
cite it please! It's a beautiful paper, but it's
[4721] tough to get that into a journal. Why? So far 
it's because it's hard to argue to people that
[4727] any algorithm you think of that uses local 
learning rules, that whole class will have this
[4733] property. And I can't honestly claim that. I don't  
know what that class looks like. I don't even
[4738] know how to go about stating it. What I do know 
how to do is to say, well, any algorithm that uses
[4745] the same tricks that our algorithm does - because we 
have an intuition for why ours works -
[4751] then I can make an argument for why 
this is generally going to be true.
[4754] Why whitening is going to be useful. But there 
is no notion of the class of 'local learning rule
[4760] neural networks,' right? And maybe there will be 
down the road, but right now that doesn't exist.
[4765] I'd also say that there are different kinds 
of classes of algorithms people think about.
[4769] And in our group we've ... In the last year, we've 
been thinking a lot about ... There are these ...
[4774] So it turns out if you look at deep neural 
networks and you consider the infinite width limit,
[4781] it turns out that in that case there's 
a simple kernel description you can have
[4786] that describes the input-output relationship 
and the learnability in terms of a Gaussian
[4792] process. So it turns out there's a really simple 
model you can write down that characterizes
[4798] infinitely wide deep neural nets, and the way they 
learn, and what they can learn - all that kind of stuff.
[4804] And we have a bunch of results that we're just 
about to submit - and we just just submitted
[4809] one and are about to submit some some others - having to do with how 
universal this is. It turns out that
[4816] shallow networks are just as powerful as deep 
neural networks, and we can even figure out what
[4822] activation functions - what non-linearities - you 
need to impose on the shallow ones based on the
[4829] the deep net. Surprising result to 
me. And then other things too, like the fact that
[4836] if you look at really crazy 
networks, that are non-linear in ways that are
[4840] way outside of deep neural nets. So instead of 
just doing matrix multiplication and point-wise
[4845] nonlinearities, suppose you use really crazy 
non-linearities that mix things up in a more
[4849] complicated way. Turns out that if you go to this 
infinite width limit, that's a class of models you
[4854] can actually work with and calculate stuff. 
And I should say: This infinite width limit
[4860] existed before. That isn't new to us. What's 
new to us is using it to ask questions outside
[4865] the sort of standard deep neural nets, and start 
looking at stuff that's really weird, like
[4870] networks that only have one layer or networks that 
are non-linear in ways that are ... So
[4877] it turns out that you don't get that much more 
power, but they're just as trainable, pretty much.
[4880] So there's not a huge difference between the 
neural networks you read about
[4886] in all the literature and the and other 
things you might have considered that seem like
[4891] they'd be completely different.
[4895] I, and I'm sure our audience, 
are dying to hear more about that.
[4898] On the other hand, am double dying to have my 
lunch.
[4903] No doubt. No doubt.
[4903] It's 1:30 here and I held off until after your talk. So I think we're gonna have to wrap up there.
[4908] All right. Enjoy your lunch, Steve.
[4912] It's been great. And yeah! Send me your pre-print 
on the ultrawide net.
[4921] Thanks a lot!
[4922] Thanks, man. Ciao.
