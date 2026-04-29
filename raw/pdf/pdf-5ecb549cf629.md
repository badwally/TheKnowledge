---
id: pdf-5ecb549cf629
type: pdf
title: BBS1200047 181..254
url: ''
authors: []
ingested_at: '2026-04-29T16:15:30Z'
content_hash: sha256:dece4c6c7f1f8acf38e7813e0226cffded2b9b265b56613f8e468303e32b0291
source_path: raw/pdf/pdf-5ecb549cf629.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 73
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__5ecb549c.pdf
published_at: '2026'
---
BEHAVIORAL AND BRAIN SCIENCES (2013) 36,181–253
doi:10.1017/S0140525X12000477
EDITOR’S NOTE
Aexceptionallylargenumberofexcellentcommentaryproposalsinspiredaspecialresearchtopicforfurtherdiscussionof
thistargetarticle’ssubjectmatter,editedbyAxelCleeremansandShimonEdelmaninFrontiersinTheoreticalandPhilo-
sophicalPsychology.ThisdiscussionhasaprefacebyCleeremansandEdelmanand25commentaries andincludesasep-
arate rejoinder from Andy Clark. See:
http://www.frontiersin.org/Theoretical_and_Philosophical_Psychology/researchtopics/Forethought_as_an_evolutionary/1031
Whatever next? Predictive brains,
situated agents, and the future of
cognitive science
Andy Clark
SchoolofPhilosophy,Psychology,andLanguageSciences,
UniversityofEdinburgh,EH89ADScotland,UnitedKingdom
andy.clark@ed.ac.uk
http://www.philosophy.ed.ac.uk/people/full-academic/andy-clark.html
Abstract:Brains,ithasrecentlybeenargued,areessentiallypredictionmachines.Theyarebundlesofcellsthatsupportperceptionand
actionbyconstantlyattemptingtomatchincomingsensoryinputswithtop-downexpectationsorpredictions.Thisisachievedusinga
hierarchical generative model that aims to minimize prediction error within a bidirectional cascade of cortical processing. Such
accounts offer a unifying model of perception and action, illuminate the functional role of attention, and may neatly capture the
special contribution of cortical processing to adaptive success. This target article critically examines this “hierarchical prediction
machine”approach,concludingthat itoffers the bestclueyetto theshape ofaunifiedscienceof mindandaction.Sections1and2
lay out the key elements and implications of the approach. Section 3 explores a variety of pitfalls and challenges, spanning the
evidential,themethodological,andthemoreproperlyconceptual.Thepaperends(sections4and5)byaskinghowsuchapproaches
mightimpactourmoregeneralvisionofmind,experience,andagency.
Keywords: action; attention; Bayesian brain; expectation; generative model; hierarchy; perception; precision; predictive coding;
prediction;predictionerror;top-downprocessing
1. Introduction: Predictionmachines
correct, and that it captures something crucial about the
way that spending metabolic money to build complex
1.1. FromHelmholtztoaction-orientedpredictive
brains pays dividends in the search for adaptive success.
processing
In particular, one of the brain’s key tricks, it now seems,
“The whole function of the brain is summed up in: error is to implement dumb processes that correct a certain
correction.” So wrote W. Ross Ashby, the British psychia- kind of error: error in the multi-layered prediction of
trist and cyberneticist, some half a century ago.1 Compu- input. In mammalian brains, such errors look to be cor-
tational neuroscience has come a very long way since rected within a cascade of cortical processing events in
then. There is now increasing reason to believe that which higher-level systems attempt to predict the inputs
Ashby’s (admittedly somewhat vague) statement is to lower-level ones on the basis of their own emerging
©CambridgeUniversityPress2013 0140-525X/13$40.00 181
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
modelsofthecausalstructureoftheworld(i.e.,thesignal to create the sensory patterns for itself (in “fantasy,” as it
source). Errors in predicting lower level inputs cause the was sometimes said).3 (For a useful review of this crucial
higher-level models to adapt so as to reduce the discre- innovationandasurveyofmanysubsequentdevelopments,
pancy. Such a process, operating over multiple linked seeHinton 2007a).
higher-level models, yields a brain that encodes a rich A generative model, in this quite specific sense, aims to
body of information about the source of the signals that capture the statistical structure of some set of observed
regularly perturb it. inputsbytracking(onemightsay,byschematicallyrecapi-
Such models follow Helmholtz (1860) in depicting per- tulating) the causal matrix responsible for that very struc-
ception as a process of probabilistic, knowledge-driven ture. A good generative model for vision would thus seek
inference. From Helmholz comes the key idea that to capture the ways in which observed lower-level visual
sensory systems are in the tricky business of inferring responsesaregeneratedbyaninteractingwebofcauses–
sensory causes from their bodily effects. This in turn for example, the various aspects of a visually presented
involves computing multiple probability distributions, scene. In practice, this means that top-down connections
since a single such effect will be consistent with many within a multilevel (hierarchical and bidirectional) system
different sets ofcausesdistinguished only by their relative come to encode a probabilistic model of the activities of
(and context dependent) probabilityof occurrence. unitsandgroupsofunitswithinlowerlevels,thustracking
Helmholz’sinsightinformedinfluentialworkbyMacKay (asweshallshortlyseeinmoredetail)interactingcausesin
(1956), Neisser (1967), and Gregory (1980), as part of the thesignalsource,whichmightbethebodyortheexternal
cognitive psychological tradition that became known as world–see,forexample,Kawatoetal.(1993),Hintonand
“analysis-by-synthesis” (for a review, see Yuille & Kersten Zemel (1994), Mumford (1994), Hinton et al. (1995),
2006). In this paradigm, the brain does not build its Dayan et al. (1995), Olshausen and Field (1996), Dayan
current model of distal causes (its model of how the (1997), and Hinton and Ghahramani (1997).
world is) simply by accumulating, from the bottom-up, a It is this twist–the strategy of using top-down connec-
mass of low-level cues such as edge-maps and so forth. tions to try to generate, using high-level knowledge, a
Instead (see Hohwy 2007), the brain tries to predict the kind of “virtual version” of the sensory data via a deep
current suite of cues from its best models of the possible multilevel cascade–that lies at the heart of “hierarchical
causes. In this way: predictive coding” approaches to perception; for
example, Rao and Ballard (1999), Lee and Mumford
Themappingfromlow-tohigh-levelrepresentation(e.g.from
(2003), Friston (2005). Such approaches, along with
acoustictoword-level)iscomputedusingthereversemapping, their recent extensions to action–as exemplified in
from high- to low-level representation. (Chater & Manning
Friston and Stephan (2007), Friston et al. (2009),
2006,p.340,theiremphasis)
Friston (2010), Brown et al. (2011)–form the main
Helmholz’s insight was also pursued in an important focus of the present treatment. These approaches
body of computational and neuroscientific work. Crucial combine the use of top-down probabilistic generative
to this lineage were seminal advances in machine learning models with a specific vision of one way such downward
that began with pioneering connectionist work on back- influence might operate. That way (borrowing from
propagation learning (McClelland et al. 1986; Rumelhart work in linear predictive coding–see below) depicts the
et al. 1986) and continued with work on the aptly named top-down flow as attempting to predict and fully
“Helmholz Machine” (Dayan et al. 1995; Dayan & “explain away” the driving sensory signal, leaving only
Hinton1996;seealsoHinton&Zemel1994).2TheHelm- any residual “prediction errors” to propagate information
holtz Machine sought to learn new representations in a forward within the system–see Rao and Ballard (1999),
multilevel system (thus capturing increasingly deep regu- Lee and Mumford (2003), Friston (2005), Hohwy et al.
larities within a domain) without requiring the provision (2008), Jehee and Ballard (2009), Friston (2010), Brown
of copious pre-classified samples of the desired input- et al. (2011); and, for a recent review, see Huang and
output mapping. In this respect, it aimed to improve (see Rao (2011).
Hinton 2010) upon standard back-propagation driven Predictivecodingitselfwasfirstdevelopedasadatacom-
learning.Itdidthisbyusingitsowntop-downconnections pressionstrategyinsignalprocessing(forahistory,seeShi
to provide the desired states for the hidden units, thus (in & Sun 1999). Thus, consider a basic task such as image
effect) self-supervising the development of its perceptual transmission: In most images, the value of one pixel regu-
“recognition model” using a generative model that tried larlypredictsthevalueofitsnearestneighbors,withdiffer-
ences marking important features such as the boundaries
between objects. That means that the code for a rich
image can be compressed (for a properly informed recei-
ANDY CLARK isProfessorofLogicandMetaphysicsin ver) by encoding only the “unexpected” variation: the
the School of Philosophy, Psychology, and Language cases where the actual value departs from the predicted
Sciences at the University of Edinburgh in Scotland. one. What needs to be transmitted is therefore just the
He is the author of six monographs, including Being difference (a.k.a. the “prediction error”) between the
There:PuttingBrain,BodyandWorldTogetherAgain actual current signal and the predicted one. This affords
(MIT Press, 1997), Mindware (Oxford University
major savings on bandwidth, an economy that was the
Press, 2001), Natural-Born Cyborgs: Minds, Technol-
driving force behind the development of the techniques
ogies and the Future of Human Intelligence (Oxford
by James Flanagan and others at Bell Labs during the
University Press, 2003), and Supersizing the Mind:
1950s (for a review, see Musmann 1979). Descendents of
Embodiment,Action, andCognitiveExtension(Oxford
University Press, 2008). In 2006 he was elected this kind of compression technique are currently used in
FellowoftheRoyalSocietyofEdinburgh. JPEGs, in various forms of lossless audio compression,
182 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
and in motion-compressed coding for video. The infor- Various forms of gradient descent learning can progress-
mation that needs to be communicated “upward” under ivelyimproveyourfirstguesses.Appliedwithinahierarch-
alltheseregimesisjustthepredictionerror:thedivergence icalpredictive processing5regime,thiswill–ifyou survive
fromtheexpectedsignal.Transposed(inwaysweareabout longenough–tendtoyieldusefulgenerativemodelsofthe
to explore) to the neural domain, this makes prediction signal source (ultimately, theworld).
error into a kind of proxy (Feldman & Friston 2010) for The beauty of the bidirectional hierarchical structure is
sensoryinformationitself.Later,whenweconsiderpredic- that it allows the system to infer its own priors (the prior
tive processing in the larger setting of information theory beliefs essential to the guessing routines) as it goes along.
and entropy, we will see that prediction error reports the It does this by using its best current model–at one
“surprise” induced by a mismatch between the sensory level–asthesourceofthepriorsforthelevelbelow,enga-
signals encountered and those predicted. More formally– ging in a process of “iterative estimation” (see Dempster
andtodistinguishitfromsurpriseinthenormal,experien- et al. 1977; Neal & Hinton 1998) that allows priors and
tiallyloadedsense–thisisknownassurprisal(Tribus1961). modelstoco-evolveacrossmultiplelinkedlayersofproces-
Hierarchical predictive processing combines the use, singsoastoaccountforthesensorydata.Thepresenceof
withinamultilevelbidirectionalcascade,of“top-down”prob- bidirectionalhierarchicalstructurethusinduces“empirical
abilistic generative models with the core predictive coding priors”6intheformoftheconstraintsthatonelevelinthe
strategy of efficient encoding and transmission. Such hierarchy places on the level below, and these constraints
approaches, originally developed in the domain of percep- are progressively tuned by the sensory input itself. This
tion, have been extended (by Friston and others–see sect. kindofprocedure(whichimplementsaversionof“empiri-
1.5)toencompassaction,andtoofferanattractive,unifying cal Bayes”; Robbins 1956) has an appealing mapping to
perspective on the brain’s capacities for learning, inference, known facts about the hierarchical and reciprocally con-
and the control of plasticity. Perception and action, if these nected structure and wiring of cortex (Friston 2005; Lee
unifying models are correct, are intimately related and &Mumford2003).7
work together to reduce prediction error by sculpting and Aclassicearlyexample,combiningthiskindofhierarch-
selecting sensory inputs. In the remainder of this section, I ical learning with the basic predictive coding strategy
rehearse some of the main features of these models before described in section 1.1, is Rao and Ballard’s (1999)
highlighting(insects.2–5following)someoftheirmostcon- model of predictive coding in the visual cortex. At the
ceptuallyimportantandchallengingaspects. lowest level, there is some pattern of energetic stimu-
lation, transduced (let’s suppose) by sensory receptors
from ambient light patterns produced by the current
1.2. Escapingtheblackbox
visual scene. These signals are then processed via a multi-
A good place to start (following Rieke 1999) is with what level cascade in which each level attempts to predict the
might be thought of as the “view from inside the black activity at the level below it via backward8 connections.
box.” For, the task of the brain, when viewed from a The backward connections allow the activity at one stage
certain distance, can seem impossible: it must discover of the processing to return as another input at the pre-
information about the likely causes of impinging signals vious stage. So long as this successfully predicts the
without any form of direct access to their source. Thus, lower level activity, all is well, and no further action
considerablackboxtakinginputsfromacomplexexternal needs to ensue. But where there is a mismatch, “predic-
world.Theboxhasinputandoutputchannelsalongwhich tion error” occurs and the ensuing (error-indicating)
signalsflow.Butallthatit“knows”,inanydirectsense,are activityispropagatedtothehigherlevel.Thisautomatically
thewaysitsownstates(e.g.,spiketrains)flowandalter.In adjusts probabilistic representations at the higher level so
that(restricted)sense,allthesystemhasdirectaccesstois that top-down predictions cancel prediction errors at the
itsownstates.Theworlditselfisthusoff-limits(thoughthe lower level (yielding rapid perceptual inference). At the
box can, importantly, issue motor commands and await same time, prediction error is used to adjust the structure
developments). The brain is one such black box. How, of the model so as to reduce any discrepancy next time
simplyonthebasisofpatternsofchangesinitsowninternal around (yielding slower timescale perceptual learning).
states,isittoalterandadaptitsresponsessoastotuneitself Forward connections between levels thus carry the
to act as a useful node (one that merits its relatively huge “residual errors” (Rao & Ballard 1999, p. 79) separating
metabolic expense) for the origination of adaptive the predictions from the actual lower level activity, while
responses? Notice how different this conception is to backward connections (which do most of the “heavy
ones in which the problem is posed as one of establishing lifting” in these models) carry the predictions themselves.
a mapping relation between environmental and inner Changing predictions corresponds to changing or tuning
states. The task is not to find such a mapping but to infer your hypothesis about the hidden causes of the lower
the nature of the signal source (the world) from just the level activity. The concurrent running of this kind of pre-
varying inputsignalitself. dictionerrorcalculationwithinaloosebidirectionalhierar-
Hierarchical approaches in which top-down generative chy of cortical areas allows information pertaining to
models are trying to predict the flow of sensory data regularities at different spatial and temporal scales to
provide a powerful means for making progress under settle into a mutually consistent whole in which each
suchapparentlyunpromisingconditions.Onekeytaskper- “hypothesis” is used to help tune the rest. As the authors
formed by the brain, according to these models, is that of put it:
guessing the next states of its own neural economy. Such
guessing improves when you use a good model of the Prediction and error-correction cycles occur concurrently
signal source. Cast in the Bayesian mode, good guesses throughoutthehierarchy,sotop-downinformationinfluences
thus increase the posterior probability4 of your model. lower-level estimates, and bottom-up information influences
BEHAVIORALANDBRAINSCIENCES(2013)36:3 183
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
higher-levelestimatesoftheinputsignal.(Rao&Ballard1999, what is (to use Hosoya et al.’s own phrase) most “news-
p.80) worthy” in theincoming signal.10
In the visual cortex, such a scheme suggests that back- These computations of predicted salience might be
ward connections from V2 to V1 would carry a prediction made solely on the basis of average image statistics. Such
of expected activity in V1, while forward connections anapproachwould,however,leadtotroubleinmanyeco-
fromV1toV2wouldcarryforwardtheerrorsignal9indicat- logicallyrealisticsituations.Totakesomeofthemoredra-
ingresidual(unpredicted) activity. matic examples, consider an animal that frequently moves
To test these ideas, Rao and Ballard implemented a between a watery environment and dry land, or between
simple bidirectional hierarchical network of such “predic- a desert landscape and a verdant oasis. The spatial scales
tive estimators” and trained it on image patches derived at which nearby points in space and time are typically
from five natural scenes. Using learning algorithms that similar in image intensity vary markedly between such
progressively reduce prediction error across the linked cases, because the statistical properties of the different
cascade and after exposure to thousands of image types of scene vary. This is true in less dramatic cases
patches, the system learnt to use responses in the first too, such as when we move from inside a building to a
level network to extract features such as oriented edges garden or lake. Hosoya et al. thus predicted that, in the
and bars, while the second level network came to interests of efficient, adaptively potent, encoding, the be-
capture combinations of such features corresponding to
havioroftheretinalganglioncells(specifically,theirrecep-
patterns involving larger spatial configurations. The tivefieldproperties)shouldvaryasaresultofadaptationto
model also displayed (see sect. 3.1) a number of interest- the current scene or context, exhibiting what they term
ing “extra-classical receptive field” effects, suggesting that “dynamic predictivecoding.”
such non-classical surround effects (and, as we’ll later Putting salamanders and rabbits into varying environ-
see, context effects more generally) may be a rather ments, and recording from their retinal ganglion cells,
direct consequence of the use of hierarchical predictive Hosoya et al. confirmed their hypothesis: Within a space
coding. of several seconds, about 50% of the ganglion cells
For immediate purposes, however, what matters is that altered their behaviors to keep step with the changing
the predictive coding approach, given only the statistical imagestatisticsofthevaryingenvironments.Amechanism
properties of the signals derived from the natural images, was then proposed and tested using a simple feedforward
wasabletoinduceakindofgenerativemodelofthestruc- neuralnetworkthatperformsaformofanti-Hebbianlearn-
ture of the input data: It learned about the presence and ing. Anti-Hebbian feedforward learning, in which corre-
importance of features such as lines, edges, and bars, and lated activity across units leads toinhibition rather thanto
about combinations of such features, in ways that enable activation (see, e.g., Kohonen 1989), enables the creation
better predictions concerning what to expect next, in of “novelty filters” that learn to become insensitive to the
space or in time. The cascade of processing induced by most highly correlated (hence most “familiar”) features of
theprogressivereductionofpredictionerrorinthehierar- the input. This, of course, is exactly what is required in
chy reveals the world outside the black box. It maximizes ordertolearntodiscountthemoststatisticallypredictable
the posterior probability of generating the observed states elementsoftheinputsignalinthewaydynamicpredictive
(the sensory inputs), and, in so doing, induces a kind of coding suggests. Better yet, there are neuronally plausible
internal model of the source of the signals: the world ways to implement such a mechanism using amacrine cell
hidden behindthe veil ofperception. synapses to mediate plastic inhibitory connections that in
turn alter the receptive fields of retinal ganglion cells (for
details, see Hosoya et al. 2005, p. 74) so as to suppress
the most correlated components of the stimulus. In sum,
1.3. Dynamicpredictivecodingbytheretina retinal ganglion cells seem to be engaging in a computa-
Asanexampleofthepower(andpotentialubiquity)ofthe tionally and neurobiologically explicable process of
basic predictive coding strategy itself, and one that now dynamic predictive recoding of raw image inputs, whose
moves context center stage, consider Hosoya et al.’s effect is to “strip from the visual stream predictable and
(2005) account of dynamic predictive coding by the therefore less newsworthy signals” (Hosoya et al. 2005,
retina. The starting point of this account isthe well-estab- p.76).
lished sense in which retinal ganglion cells take part in
some form of predictive coding, insofar as their receptive
fields display center-surround spatial antagonism, as well 1.4. Anotherillustration:Binocularrivalry
as a kind of temporal antagonism. What this means, in Sofar,ourexampleshavebeenrestrictedtorelativelylow-
each case, is that neural circuits predict, on the basis of level visual phenomena. As a final illustration, however,
local image characteristics, the likely image characteristics consider Hohwy et al.’s (2008) hierarchical predictive
of nearby spots in space and time (basically, assuming coding model of binocular rivalry. Binocular rivalry (see,
that nearby spots will display similar image intensities) e.g., essays in Alais & Blake 2005, and the review article
and subtract this predicted value from the actual value. by Leopold & Logothetis 1999) is a striking form of
Whatgetsencodedisthusnottherawvaluebutthediffer- visual experience that occurs when, using a special exper-
encesbetweenrawvaluesandpredictedvalues.Inthisway, imental set-up, each eye is presented (simultaneously)
“Ganglion cells signal not the raw visual image but the with a different visual stimulus. Thus, the right eye might
departures from the predictable structure, under the be presented with an image of a house, while the left
assumption of spatial and temporal uniformity” (Hosoya receives an image of a face. Under these (extremely–and
et al.2005, p. 71). Thissaves on bandwidth, and also flags importantly–artificial) conditions, subjective experience
184 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
unfolds in a surprising, “bi-stable” manner. Instead of alternative hypothesis is not suppressed; it is now propa-
seeing (visually experiencing) a confusing all-points gated up the hierarchy. To suppress those prediction
merger of house and face information, subjects report a errors, the system needs to find another hypothesis. But
kind of perceptual alternation between seeing the house having done so (and hence, having flipped the dominant
and seeing the face. The transitions themselves are not hypothesis to the other interpretation), there will again
always sharp, and subjects often report a gradual breaking emerge a large prediction error signal, this time deriving
through (see, e.g., Lee et al. 2005) of elements of the from those elements of the driving signal not accounted
other image before it dominates the previous one, after for by the flipped interpretation. In Bayesian terms, this is
which thecycle repeats. a scenario in which no unique and stable hypothesis com-
Such“binocularrivalry,”asHohwyetal.remindus,has bines high prior and high likelihood. No single hypothesis
been a powerful tool for studying the neural correlates of accounts for all the data, so the system alternates between
conscious visual experience, since the incoming signals thetwo semi-stable states. Itbehaves as a bi-stable system,
remain constant while the percept switches to and fro minimizing prediction error in what Hohwy et al. describe
(Frith et al. 1999). Despite this attention, however, the asanenergylandscapecontainingadoublewell.
precise mechanisms at play here are not well understood. Whatmakesthisaccountdifferentfromitsrivals(suchas
Hohwy et al.’s strategy is to take a step back, and to thatofLeeetal.2005)isthatwhereastheypositakindof
attempt to explain the phenomenon from first principles direct, attention-mediated but essentially feedforward,
in a way that makes sense of many apparently disparate competition betweentheinputs,thepredictiveprocessing
findings.Inparticular,theypursuewhattheyduban“epis- accountposits“top-down”competitionbetweenlinkedsets
temological”approach:onewhosegoalistorevealbinocu- of hypotheses. The effect of this competition is to selec-
larrivalryasareasonable(knowledge-oriented)responseto tively suppress the prediction errors associated with the
an ecologicallyunusual stimulus condition. elements of the driving (sensory) signals suggesting the
Thestartingpointfortheirstoryis,onceagain,theemer- currentwinninghypothesis.Butthistop-downsuppression
ging unifying vision of the brain as an organ of prediction leavesuntouchedthepredictionerrorsassociatedwiththe
using a hierarchical generative model. Recall that, on remainingelements ofthedriving signal. Theseerrors are
these models, the task of the perceiving brain is to then propagated up the system. To explain them away
account for (to “explain away”) the incoming or “driving” the overall interpretation must switch. This pattern
sensorysignalbymeansofamatchingtop-downprediction. repeats, yielding the distinctive alternations experienced
Thebetterthematch,thelesspredictionerrorthenpropa- duringdichopticviewingofinconsistentstimuli.11
gates up the hierarchy. The higher-level guesses are thus Why,undersuchcircumstances,dowenotsimplyexperi-
acting as priors for the lower-level processing, in the enceacombinedorinterwovenimage:akindofhouse/face
fashion of so-called “empirical Bayes” (such methods use mash-up for example? Although such partially combined
theirowntargetdatasetstoestimatethepriordistribution: percepts do apparently occur, for brief periods of time,
akindofbootstrappingthatexploitsthestatisticalindepen- they are not sufficiently stable, as they do not constitute a
dencies that characterize hierarchical models). viable hypothesis given our more general knowledge about
Withinsuchamultilevelsetting,avisualperceptisdeter- the visual world. For it is part of that general knowledge
minedbyaprocessofpredictionoperatingacrossmanylevels that, for example, houses and faces are not present in the
ofa(bidirectional)processinghierarchy,eachconcernedwith same place, at the same scale, at the same time. This kind
different types and scales of perceptual detail. All the com- of general knowledge may itself be treated as a systemic
municatingareasarelockedintoamutuallycoherentpredic- prior, albeit one pitched at a relatively high degree of
tive coding regime, and their interactive equilibrium abstraction(suchpriorsaresometimesreferredtoas“hyper-
ultimately selects a best overall (multiscale) hypothesis con- priors”).Inthecaseathand,whatiscapturedisthefactthat
cerning the state of the visually presented world. This is “thepriorprobabilityofbothahouseandfacebeingco-loca-
the hypothesis that “makes the best predictions and that, lized in time and space is extremely small” (Hohwy et al.
taking priors into consideration, is consequently assigned 2008, p. 691). This, indeed, is the deep explanation of the
the highest posterior probability” (Hohwy et al. 2008, existence of competition between certain higher-level
p. 690). Other overall hypotheses, at that moment, are hypotheses in the first place. They compete because the
simply crowded out: they are effectively inhibited, having system has learnt that “only one object can exist in the
lostthecompetitiontobestaccountforthedrivingsignal. same place at the same time” (Hohwy et al. 2008, p. 691).
Notice, though, what this means in the context of the (This obviously needs careful handling, since a single state
predictive coding cascade. Top-down signals will explain of the world may be consistently captured by multiple
away (by predicting) only those elements of the driving high-level stories that ought not to compete in the same
signal that conform to (and hence are predicted by) the way: for example, seeing the painting as valuable, as a
current winning hypothesis. In the binocular rivalry case, Rembrandt,asanimageofacow,etc.)
however, the driving (bottom-up) signals contain infor-
mation that suggests two distinct, and incompatible,
1.5. Action-orientedpredictiveprocessing
states of the visually presented world–for example, face
at location X/house at location X. When one of these is Recent work by Friston (2003; 2010; and with colleagues:
selected as the best overall hypothesis, it will account for Brown et al. 2011; Friston et al. 2009) generalizes this
all and only those elements of the driving input that the basic “hierarchical predictive processing” model to
hypothesis predicts. As a result, prediction error for that include action. According to what I shall now dub
hypothesis decreases. But prediction error associated with “action-oriented predictive processing,”12 perception and
the elements of the driving signal suggestive of the action both follow the same deep “logic” and are even
BEHAVIORALANDBRAINSCIENCES(2013)36:3 185
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
implemented using the same computational strategies. A brains)expect(see Friston2009;Fristonetal.2010).Per-
fundamental attraction of these accounts thus lies in their ception,cognition,andaction–ifthisunifyingperspective
ability to offer a deeply unified account of perception, provescorrect–workcloselytogethertominimizesensory
cognition, and action. prediction errors by selectively sampling, and actively
Perception,aswesaw,isheredepictedasaprocessthat sculpting, the stimulus array. They thus conspire to move
attemptstomatchincoming“driving”signalswithacascade a creature through time and space in ways that fulfil an
of top-down predictions (spanning multiple spatial and ever-changing and deeply inter-animating set of (sub-per-
temporal scales) that aim to cancel it out. Motor action sonal) expectations. According tothese accounts, then:
exhibits a surprisingly similar profile,exceptthat:
Perceptual learning and inference is necessary to induce prior
Inmotorsystemserrorsignalsself-suppress,notthroughneuron- expectations about how the sensorium unfolds. Action is
ally mediated effects, but by eliciting movements that change
engagedtoresampletheworldtofulfiltheseexpectations.This
bottom-upproprioceptiveandsensoryinput.Thisunifyingper- places perception and action in intimate relation and accounts
spectiveonperceptionandactionsuggeststhatactionisbothper- forbothwiththesameprinciple.(Fristonetal.2009,p.12)
ceivedandcausedbyitsperception.(Friston2003,p.1349)
Insome(I’llcallthemthe“desertlandscape”)versionsof
This whole scenario is wonderfully captured by Hawkins thisstory(seeespeciallyFriston2011b;Fristonetal.2010)
and Blakeslee, whowrite that: proprioceptive prediction errors act directly as motor com-
mands.Onthesemodelsitisourexpectationsaboutthepro-
Asstrangeasitsounds,whenyourownbehaviourisinvolved, prioceptiveconsequencesofmovingandactingthatdirectly
your predictions not only precede sensation, they determine bring the moving and acting about.13 I return briefly to
sensation.Thinkingofgoingtothenextpatterninasequence these“desertlandscape”scenariosinsection5.1furtheron.
causes a cascading prediction of what you should experience
next. As the cascading prediction unfolds, it generates the
motor commands necessary to fulfil the prediction. Thinking,
1.6. Thefreeenergyformulation
predicting, and doing are all part of the same unfolding of
sequences moving down the cortical hierarchy. (Hawkins & Thatlarge-scalepicture(ofcreaturesenslavedtosenseand
Blakeslee2004,p.158) to act in ways that make most of their sensory predictions
come true) finds fullest expression in the so-called free-
Acloselyrelatedbodyofworkinso-calledoptimalfeed-
energy minimization framework (Friston 2003; 2009;
backcontroltheory(e.g.,Todorov2009;Todorov&Jordan
2010; Friston & Stephan 2007). Free-energy formulations
2002) displays the motor control problem as mathemat-
originate in statistical physics and were introduced into
ically equivalent to Bayesian inference. Very roughly–see
the machine-learning literature in treatments that include
Todorov (2009) for a detailed account–you treat the
Neal and Hinton (1998), Hinton and von Camp (1993),
desired (goal) state as observed and perform Bayesian
inference to find the actions that get you there. This Hinton and Zemel (1994), and MacKay (1995). Such for-
mulations can arguably be used (e.g., Friston 2010) to
mapping between perception and action emerges also in
display the prediction error minimization strategy as itself
some recent work on planning (e.g., Toussaint 2009). The
a consequence of a more fundamental mandate to mini-
idea, closely related to these approaches to simple move-
mizeaninformation-theoreticisomorphofthermodynamic
ment control, is that in planning we imagine a future goal
state as actual, then use Bayesian inference to find the set free-energyinasystem’sexchangeswiththeenvironment.
Thermodynamic free energy is a measure of the energy
of intermediate states (which can now themselves be
availabletodousefulwork.Transposedtothecognitive/infor-
whole actions) that get us there. There is thus emerging a
fundamentally unified set of computational models which, mational domain, it emerges as the difference between the
waytheworldisrepresentedasbeing,andthewayitactually
asToussaint(2009,p.29)comments,“doesnotdistinguish
is.Thebetterthefit,thelowertheinformation-theoreticfree
betweentheproblemsofsensorprocessing,motorcontrol,
or planning.” Toussaint’s bold claim is modified, however, energy(thisisintuitive,sincemoreofthesystem’sresources
arebeingputto“effectivework”inrepresentingtheworld).
by the important caveat (op. cit., p. 29) that we must, in
Prediction error reports this information-theoretic free
practice, deploy approximations and representations that
energy, which is mathematically constructed so as always to
are specialized for different tasks. But at the very least, it
begreaterthan“surprisal”(wherethisnamesthesub-person-
now seems likely that perception and action are in some
ally computed implausibility of some sensory state given a
deepsensecomputational siblings and that:
model of the world–see Tribus (1961) and sect. 4.1 in the
Thebestwaysofinterpretingincominginformationviapercep- presentarticle).Entropy,inthisinformation-theoreticrendi-
tion, are deeply the same as the best ways of controlling out-
tion,isthelong-termaverageofsurprisal,andreducinginfor-
going information via motor action … so the notion that
mation-theoretic free energy amounts to improving the
thereareafewspecifiablecomputationalprinciplesgoverning
world model so as to reduce prediction errors, hence redu-
neuralfunctionseemsplausible.(Eliasmith2007,p.380)
cing surprisal14 (since better models make better predic-
Action-oriented predictive processing goes further, tions). The overarching rationale (Friston 2010) is that
however, in suggesting that motor intentions actively goodmodelshelpustomaintainourstructureandorganiz-
elicit, via their unfolding into detailed motor actions, the ation, hence (over extended but finite timescales) to appear
ongoing streams of sensory (especially proprioceptive) toresistincreasesinentropyandthesecondlawofthermo-
results that our brains predict. This deep unity between dynamics. They do so by rendering us good predictors of
perception and actionemergesmost clearlyin the context sensory unfoldings, hence better poised to avoid damaging
of so-called active inference, where the agent moves its exchangeswiththeenvironment.
sensorsinwaysthatamounttoactivelyseekingorgenerat- The“free-energyprinciple” itself then statesthat“allthe
ing the sensory consequences that they (or rather, their quantities that can change; i.e. that are part of the system,
186 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
will change to minimize free-energy” (Friston & Stephan interacting set of distal causes that predict, accommodate,
2007, p. 427). Notice that, thus formulated, this is a claim and (thus) “explain away”the driving sensory signal.
aboutallelementsofsystemicorganization(fromgrossmor- This appeal to “explaining away” is important and
phologytotheentireorganizationofthebrain)andnotjust central, but it needs very careful handling. It is important
about cortical information processing. Using a series of asitreflectsthekeypropertyofhierarchicalpredictivepro-
elegant mathematical formulations, Friston (2009; 2010) cessingmodels,whichisthatthebrainisinthebusinessof
suggeststhatthisprinciple,whenappliedtovariouselements active,ongoing,inputpredictionanddoesnot(eveninthe
of neural functioning, leads to the generation of efficient early sensory case) merely react to external stimuli. It is
internal representational schemes and reveals the deeper important also insofar as it is the root of the attractive
rationale behind the links between perception, inference, coding efficiencies that these models exhibit, since all
memory, attention, and action scouted in the previous sec- that needs to bepassed forward through thesystem is the
tions. Morphology, action tendencies (including the active error signal, which is what remains once predictions and
structuringofenvironmentalniches),andgrossneuralarchi- driving signals have been matched.16 In these models it is
tectureareallexpressions,ifthisstoryiscorrect,ofthissingle therefore the backward (recurrent) connectivity that
principleoperatingatvaryingtime-scales. carries the main information processing load. We should
Thefree-energyaccountisofgreatindependentinterest.It not, however, overplay this difference. In particular, it is
representsakindof“maximalversion”oftheclaimsscouted potentially misleading tosay that:
insection1.5concerningthecomputationalintimacyofper-
Activation in early sensory areas no longer represents sensory
ceptionandaction,anditissuggestiveofageneralframework information per se, but only that part of the input that has
that might accommodate the growing interest (see, e.g., notbeensuccessfully predictedby higher-level areas. (de-Wit
Thompson 2007) in understanding the relations between etal.2010,p.8702)
lifeandmind.Essentially,thehopeistoilluminatethevery Itispotentiallymisleadingbecausethisstressesonlyone
possibilityofself-organizationinbiologicalsystems(see,e.g., aspect of what is (at least in context of the rather specific
Friston 2009, p. 293). A full assessment of the free energy models we have been considering17) actually depicted as
principle is, however, far beyond the scope of the present a kind of duplex architecture: one that at each level com-
treatment.15 In the remainder of this article, I turn instead bines quite traditional representations of inputs with rep-
toanumberofissuesandimplicationsarisingmoredirectly resentations of error. According to the duplex proposal,
from hierarchical predictive processing accounts of percep- what gets “explained away” or cancelled out is the error
tionandtheirpossibleextensionstoaction. signal, which (in these models) is depicted as computed
bydedicated“errorunits.”Thesearelinkedto,butdistinct
from, the so-called representation units meant to encode
2. Representation,inference, and the continuity of
thecausesofsensory inputs. By cancelling outthe activity
perception, cognition, and action
oftheerrorunits,activityinsomeofthelaterallyinteract-
ing “representation” units (which then feed predictions
The hierarchical predictive processing account, along with
downwardandareinthebusinessofencodingtheputative
themorerecentgeneralizationstoactionrepresents,orsoI
sensory causes) can actually end up being selected and
shallnowargue,agenuinedeparturefrommanyofourpre-
sharpened. The hierarchical predictive processing account
viouswaysofthinkingaboutperception,cognition,andthe thus avoids any direct conflict with accounts (e.g., biased-
humancognitivearchitecture.Itoffersadistinctiveaccount
competition models such as that of Desimone & Duncan
ofneuralrepresentation,neuralcomputation,andtherep-
1995) that posit top-down enhancements of selected
resentationrelationitself.Itdepictsperception,cognition,
aspects ofthe sensory signal, because:
andactionasprofoundlyunifiedand,inimportantrespects,
continuous.Anditoffersaneurallyplausibleandcomputa- High-level predictions explain away prediction error and tell
the error units to “shut up” [while] units encoding the causes
tionallytractableglossontheclaimthatthebrainperforms
of sensory input are selected by lateral interactions, with the
some form ofBayesian inference.
errorunits,thatmediateempiricalpriors.Thisselectionstops
thegossiping[henceactuallysharpensresponsesamongthelat-
erallycompetingrepresentations].(Friston2005,p.829)
2.1. Explainingaway
Thedrivetowards“explainingaway”isthusconsistent,in
Tosuccessfully representtheworldinperception, ifthese thisspecificarchitecturalsetting,withboththesharpening
models are correct, depends crucially upon cancelling out and the dampening of (different aspects of) early cortical
sensorypredictionerror.Perceptionthusinvolves“explain- response.18 Thus Spratling, in a recent formal treatment
ingaway”thedriving(incoming)sensorysignalbymatching of this issue,19 suggests that any apparent contrast here
itwithacascadeofpredictionspitchedatavarietyofspatial reflects:
and temporal scales. These predictions reflect what the
system already knows about the world (including the Amisinterpretationofthemodelthatmayhaveresultedfrom
body)andtheuncertaintiesassociatedwithitsownproces- the strong emphasis the predictive coding hypothesis places
sing. Perception here becomes “theory-laden” in at least on the error-detecting nodes and the corresponding under-
one (rather specific) sense: What we perceive depends emphasis on the role of the prediction nodes in maintaining
an active representation of the stimulus. (Spratling 2008a,
heavilyuponthesetofpriors(includinganyrelevanthyper-
p.8,myemphasis)
priors) that the brain brings to bear in its best attempt to
predict thecurrent sensory signal.On this model,percep- What is most distinctive about this duplex architectural
tion demands the success of some mutually supportive proposal (and where much of the break from tradition
stack of states of a generative model (recall sect. 1.1 really occurs) is that it depicts the forward flow of infor-
above) at minimizing prediction error by hypothesizing an mation as solely conveying error, and the backward flow
BEHAVIORALANDBRAINSCIENCES(2013)36:3 187
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
as solely conveying predictions. The duplex architecture higher-level states and features. Instead of simply repre-
thusachievesaratherdelicatebalancebetweenthefamiliar senting “CAT ON MAT,” the probabilistic Bayesian brain
(there isstilla cascade offeature-detection, withpotential will encode a conditional probability density function,
for selective enhancement, and with increasingly complex reflecting the relative probability of this state of affairs
features represented by neural populations that are more (andanysomewhat-supportedalternatives)giventheavail-
distant from the sensory peripheries) and the novel (the able information. This information-base will include both
forward flow of sensory information is now entirely the bottom-up driving influences from multiple sensory
replaced by a forward flow ofpredictionerror). channels and top-down context-fixing information of
This balancing act between cancelling out and selective various kinds. At first, the system may avoid committing
enhancement is made possible, it should be stressed, only itself to any single interpretation, while confronting an
by positing the existence of “two functionally distinct sub- initialflurry of error signals (which are said to constitute a
populations, encoding the conditional expectations of per- major component of early evoked responses; see, e.g.,
ceptual causes and the prediction error respectively” Friston 2005, p. 829) as competing “beliefs” propagate up
(Friston 2005, p. 829). Functional distinctness need not, and down the system. This is typically followed by rapid
of course, imply gross physical separation. But a common convergence upon a dominant theme (CAT, MAT), with
conjecture in this literature depicts superficial pyramidal further details (STRIPEY MAT, TABBY CAT) sub-
cells(aprimesourceofforwardneuro-anatomicalconnec- sequently negotiated. The set-up thus favors a kind of
tions) as playing the role of error units, passing prediction recurrently negotiated “gist-at-a-glance” model, where we
error forward, while deep pyramidal cells play the role of first identify the general scene (perhaps including general
representation units, passing predictions (made on the affective elements too–for a fascinating discussion, see
basis of a complex generative model) downward (see, Barrett & Bar 2009) followed by the details. This affords
e.g., Friston 2005; 2009; Mumford 1992). However it a kind of “forest first, trees second” approach (Friston
may(ormaynot)berealized,someformoffunctionalsep- 2005,p. 825; Hochstein & Ahissar 2002).
aration is required. Such separation constitutes a central This does not mean, however, that context effects will
feature of the proposed architecture, and one without always take time to emerge and propagate downward.21
whichitwouldbeunabletocombinetheradicalelements In many (indeed, most) real-life cases, substantial context
drawn from predictive coding with simultaneous support information is already in place when new information is
for the more traditional structure of increasingly complex encountered. An apt set of priors is thus often already
feature detection and top-down signal enhancement. But active, poised to impact the processing of new sensory
essentialasitis,thisisademandingandpotentiallyproble- inputs without further delay. This is important. The
matic requirement,which we will return toin section 3.1. brain,inecologicallynormalcircumstances,isnotjustsud-
denly “turned on” and some random or unexpected input
delivered for processing. So there is plenty of room for
top-downinfluencetooccurevenbeforeastimulusispre-
2.2. Encoding,inference,andthe“BayesianBrain”
sented. This is especially important in the crucial range of
Neural representations, should the hierarchical predictive cases where we, by our own actions, help to bring the
processing account prove correct, encode probability new stimulus about. In the event that we already know
densitydistributions20intheformofaprobabilisticgenera-
we are in a forest (perhaps we have been hiking for
tive model, and the flow of inference respects Bayesian hours), there has still been prior settling into a higher
principles that balance prior expectations against new level representational state. But such settling need not
sensory evidence. This (Eliasmith 2007) is a departure occur within the temporal span following each new
fromtraditionalunderstandingsofinternalrepresentation, sensory input.22 Over whatever time-scale, though, the
andonewhosefullimplicationshaveyettobeunderstood. endpoint (assuming we form a rich visual percept) is the
Itmeansthatthenervoussystemisfundamentallyadapted same. The system will have settled into a set of states that
to deal with uncertainty, noise, and ambiguity, and that it make mutually consistent bets concerning many aspects
requiressome(perhapsseveral)concretemeansofintern- of the scene (from the general theme all the way down to
ally representing uncertainty. (Non-exclusive options here more spatio-temporally precise information about parts,
includetheuseofdistinctpopulationsofneurons,varieties colors, orientations, etc.). At each level, the underlying
of“probabilisticpopulationcodes”(Pougetetal.2003),and mode of representation will remain thoroughly probabilis-
relative timing effects (Deneve 2008)–for a very useful tic, encoding a series of intertwined bets concerning all
review,seeVilares&Körding2011).Predictiveprocessing the elements (at the various spatio-temporal scales) that
accounts thus share what Knill and Pouget (2004, p. 713) makeup theperceived scene.
describe as the“basicpremise on which Bayesian theories In what sense are such systemstruly Bayesian? Accord-
ofcortical processing will succeedorfail,” namely,that: ingtoKnilland Pouget:
The brain represents information probabilistically, by coding
The real test of the Bayesian coding hypothesis is in whether
and computing with probability density functions, or approxi-
the neural computations that result in perceptual judgments
mationstoprobabilitydensityfunctions(op.cit.,p.713)
ormotorbehaviourtakeintoaccounttheuncertaintyavailable
Suchamodeofrepresentationimpliesthatwhenwerep-
ateachstageoftheprocessing.(Knill&Pouget2004,p.713)
resentastateorfeatureoftheworld,suchasthedepthofa
visible object, we do so not using a single computed value That is to say, reasonable tests will concern how well a
but using a conditional probability density function that system deals with the uncertainties that characterize the
encodes“therelativeprobabilitythattheobjectisatdiffer- information it actually manages to encode and process,
ent depths Z, given the available sensory information” and (I would add) the general shape of the strategies it
(Knill & Pouget 2004, p. 712). The same story applies to usestodoso.Thereisincreasing(thoughmostlyindirect–
188 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
seesect.3.1)evidencethatbiologicalsystemsapproximate, at the world from “inside” the black box. That procedure
inmultipledomains,theBayesianprofilethusunderstood. (which will work in all worlds where there is organism-
To take just one example (for others, see sect. 3.1) Weiss detectable regularity in space or time; see Hosoya et al.
etal.(2002)–inapaperrevealinglytitled“Motionillusions 2005; Schwartz et al. 2007) allows a learner reliably to
as optimal percepts”–used an optimal Bayesian estimator match its internal generative model to the statistical prop-
(the “Bayesian ideal observer”) to show that a wide erties of the signal source (the world) yielding contents
variety of psychophysical results, including many motion that are, I submit, as “grounded” (Harnad 1990) and
“illusions,” fall naturally out of the assumption that “intrinsic” (Adams & Aizawa 2001) as any philosopher
humanmotionperceptionimplementsjustsuchanestima- couldwishfor.Suchmodelsthusdeliveranovelframework
tor mechanism.23Theyconcludethat: for thinking about neural representation and processing,
and a compelling take on the representation relation
Many motion “illusions” are not the result of sloppy compu-
itself: one that can be directly linked (via the Bayesian
tation by various components in the visual system, but rather
apparatus) to rational processes of learning and belief
a result of a coherent computational strategy that is optimal fixation.
underreasonableassumptions.(Weissetal.2002,p.603)
Examplescouldbemultiplied(seeKnill&Pouget[2004]
forabalancedreview).24Atleastintherealmsoflow-level, 2.3. Thedelicatedancebetweentop-downandbottom-up
basic,andadaptivelycrucial,perceptual,andmotoriccom- Inthecontextofbidirectionalhierarchicalmodelsofbrain
putations, biological processing may quite closely approxi- function,action-orientedpredictiveprocessingyieldsanew
mate Bayes’ optimality. But what researchers find account of the complex interplay between top-down and
ingeneralisnotthatwehumansare–ratherastoundingly– bottom-up influences on perception and action, and
“Bayes’ optimal” in some absolute sense (i.e., responding perhaps ultimately of the relations between perception,
correctlyrelativetotheabsoluteuncertaintiesinthestimu- action, and cognition.
lus),butrather,thatweareoftenoptimal,ornearoptimal, AsnotedbyHohwy(2007,p.320)thegenerativemodel
at taking into account the uncertainties that characterize providingthe“top-down”predictionsisheredoingmuchof
theinformationthatweactuallycommand:theinformation themoretraditionally“perceptual”work,withthebottom-
that is made available by the forms of sensing and proces- up driving signals really providing a kind of ongoing feed-
sing that we actually deploy (see Knill & Pouget 2004, back on their activity (by fitting, or failing to fit, the
p. 713). That means taking into account the uncertainty cascadeofdownward-flowingpredictions).Thisprocedure
inourownsensoryandmotorsignalsandadjustingtherela- combines “top-down” and “bottom–up” influences in an
tiveweightofdifferentcuesaccordingto(oftenverysubtle) especially delicate and potent fashion, and it leads to the
contextual clues. Recent work confirms and extends this development of neurons that exhibit a “selectivity that is
assessment,suggestingthathumansactasrationalBayesian not intrinsic to the area but depends on interactions
estimators, in perception and in action, across a wide across levels of a processing hierarchy” (Friston 2003,
variety of domains (Berniker & Körding 2008; Körding p. 1349). Hierarchical predictive coding delivers, that is
et al.2007;Yu 2007). to say, a processing regime in which context-sensitivity is
Ofcourse,themerefactthatasystem’sresponseprofiles fundamentaland pervasive.
take a certain shape does not itself demonstrate that that To see this, we need only reflect that the neuronal
system is implementing some form of Bayesian reasoning. responses that follow an input (the “evoked responses”)
In a limited domain, a look-up table could (Maloney & may be expected to change quite profoundly according to
Mamassian 2009) yield the same behavioral repertoire as the contextualizing information provided by a current
a “Bayes’ optimal” system. Nonetheless, the hierarchical winning top-down prediction. The key effect here (itself
and bidirectional predictive processing story, if correct, familiar enough from earlier connectionist work using the
would rather directly underwrite the claim that the “interactive activation” paradigm–see, e.g., McClelland
nervous system approximates, using tractable compu- & Rumelhart 1981; Rumelhart et al. 1986) is that, “when
tationalstrategies,agenuineversionofBayesianinference. a neuron or population is predicted by top-down inputs it
The computational framework of hierarchical predictive will be much easier to drive than when it is not” (Friston
processing realizes, using the signature mix of top-down 2002, p. 240). This is because the best overall fit between
and bottom-up processing, a robustly Bayesian inferential driving signal and expectations will often be found by (in
strategy, and there is mounting neural and behavioral evi- effect)inferringnoiseinthedrivingsignalandthusrecog-
dence (again, see sect. 3.1) that such a mechanism is nizing a stimulus as, for example, the letter m (say, in the
somehow implemented in the brain. Experimental tests context of the word “mother”) even though the same bare
have also recently been proposed (Maloney & Mamassian stimulus,presentedoutofcontextorinmostothercontexts,
2009; Maloney & Zhang 2010) which aim to “operationa- wouldhavebeenabetterfitwiththelettern.25Aunitnor-
lize”theclaimthatatargetsystemis(genuinely)computing mallyresponsivetothelettermmight,undersuchcircum-
its outputs using a Bayesian scheme, rather than merely stances,besuccessfullydrivenbyann-likestimulus.
behaving“asif”itdidso.This,however,isanareathatwar- Sucheffectsarepervasiveinhierarchicalpredictivepro-
rants a great deal offurther thought and investigation. cessing, and have far-reaching implications for various
Hierarchical predictive processing models also suggest forms of neuroimaging. It becomes essential, for
something about the nature of the representation relation example, to control as much as possible for expectations
itself. To see this, recall (sect. 1.2 above) that hierarchical when seeking to identify the response selectivity of
predictive coding, in common with other approaches neurons or patterns of neural activity. Strong effects of
deploying a cascade of top-down processing to generate top-down expectation have also recently been demon-
low-level states from high-level causes, offers a way to get strated for conscious recognition, raising important
BEHAVIORALANDBRAINSCIENCES(2013)36:3 189
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
questions about the very idea of any simple (i.e., context Instead, the weight given to sensory prediction error is
independent) “neural correlates of consciousness.” Thus, varied according to how reliable (how noisy, certain, or
Melloni et al. (2011) show that the onset time required to uncertain) the signal is taken to be. This is (usually) good
form a reportable conscious percept varies substantially news,asitmeanswearenot(notquite)slavestoourexpec-
(by around 100 msec) according to the presence or tations. Successful perception requires the brain to mini-
absence of apt expectations, and that the neural (here, mize surprisal. But the agent is able to see very (agent-)
EEG)signaturesofconsciousperceptionvaryaccordingly– surprising things, at least in conditions where the brain
a result these authors go on to interpret using the appar- assigns high reliability to the driving signal. Importantly,
atusofhierarchicalpredictiveprocessing.Finally,inapar- that requires that other high-level theories, though of an
ticularly striking demonstration of the power of top-down initiallyagent-unexpectedkind,winoutsoastoreducesur-
expectations, Egner et al. (2010) show that neurons in prisal by explaining away the highly weighted sensory evi-
thefusiformfacearea(FFA)respondeverybitasstrongly dence. In extreme and persistent cases (more on this in
to non-face (in this experiment, house) stimuli under high sect.4.2),thismayrequiregraduallyalteringtheunderlying
expectationoffacesastheydotoface-stimuli.Inthisstudy: generative model itself, in what Fletcher and Frith (2009,
p. 53) nicely describe as a “reciprocal interaction between
FFA activity displayed an interaction of stimulus feature and
perception and learning.”
expectation factors, where the differentiation between FFA
responses to face and house stimuli decreased linearly with Allthismakesthelinesbetweenperceptionandcognition
increasing levels of face expectation, with face and house fuzzy,perhapsevenvanishing.Inplaceofanyrealdistinction
evoked signals being indistinguishable under high face expec- between perception and belief we now get variable differ-
tation.(Egneretal.2010,p.16607) ences in the mixture of top-down and bottom-up influence,
Onlyunderconditionsoflowface expectation wasFFA and differences of temporal andspatial scale in the internal
response maximally different for the face and house models that are making the predictions. Top-level (more
probes, suggesting that “[FFA] responses appear to be “cognitive”) models26 intuitively correspond to increasingly
determined by feature expectation and surprise rather abstract conceptions of the world, and these tend to
than by stimulus features per se” (Egner et al. 2010, capture or depend upon regularities at larger temporal and
p. 16601). The suggestion, in short, is that FFA (in many spatialscales.Lower-level(more“perceptual”)onescapture
ways the paradigm case of a region performing complex or depend upon the kinds of scale and detail most strongly
featuredetection)mightbebettertreatedasaface-expec- associated with specific kinds of perceptual contact. But it
tationregionratherthanasaface-detectionregion:aresult is the precision-modulated, constant, content-rich inter-
thattheauthorsinterpretasfavoringahierarchicalpredic- actions between these levels, often mediated by ongoing
tive processing model. The growing body of such results motor action of one kind or another, that now emerges as
leads Muckli to comment that: theheartofintelligent,adaptiveresponse.
Theseaccountsthusappeartodissolve,atthelevelofthe
Sensory stimulation might be the minor task of the cortex, implementingneuralmachinery,thesuperficiallycleandis-
whereas its major task is to … predict upcoming stimulation
tinctionbetweenperceptionandknowledge/belief.Toper-
aspreciselyaspossible.(Muckli2010,p.137)
ceivetheworldjustistousewhatyouknowtoexplainaway
Inasimilarvein,Raussetal.(2011)suggestthatonsuch
the sensory signal across multiple spatial and temporal
accounts:
scales. The process of perception is thus inseparable from
neural signals are related less to a stimulus per se than to its rational (broadly Bayesian) processes of belief fixation,
congruence with internal goals and predictions, calculated on andcontext(top-down)effectsarefeltateveryintermedi-
the basis of previous input to the system. (Rauss et al. 2011, atelevelofprocessing.Asthought,sensing,andmovement
p.1249) here unfold, we discover no stable or well-specified inter-
Attention fits very neatly into this emerging unified face or interfaces between cognition and perception.
picture, as a means of variably balancing the potent inter- Believing and perceiving, although conceptually distinct,
actionsbetweentop-downandbottom-upinfluencesbyfac- emergeasdeeplymechanicallyintertwined.Theyarecon-
toring in their precision (degree of uncertainty). This is structed using the same computational resources, and (as
achieved by altering the gain (the “volume,” to use a we shall see in sect. 4.2) are mutually, reciprocally,
common analogy) on the error-units accordingly. The entrenching.
upshot of this is to “control the relative influence of prior
expectations at different levels” (Friston 2009, p. 299). In
2.4. Summarysofar
recent work, effects of the neurotransmitter dopamine are
presented as one possible neural mechanism for encoding Action-oriented(hierarchical)predictiveprocessingmodels
precision (see Fletcher & Frith [2009, pp. 53–54] who promise to bring cognition, perception, action, and atten-
referthereadertoworkonpredictionerrorandthemesolim- tiontogetherwithinacommonframework.Thisframework
bicdopaminergicsystemsuchasHolleman&Schultz1998; suggests probability-density distributions induced by hier-
Waelti et al. 2001). Greater precision (however encoded) archicalgenerativemodelsasourbasicmeansofrepresent-
means less uncertainty, and is reflected in a higher gain on ing the world, and prediction-error minimization as the
the relevant error units (see Friston 2005; 2010; Friston drivingforcebehindlearning,action-selection,recognition,
et al. 2009). Attention, if this is correct, is simply one andinference.Suchaframeworkoffersnewinsightsintoa
means by which certain error-unit responses are given wide range of specific phenomena including non-classical
increasedweight,hencebecomingmoreapttodrivelearning receptive field effects, bi-stable perception, cue inte-
andplasticity,andtoengagecompensatoryaction. gration, and the pervasive context-sensitivity of neuronal
More generally, this means that the precise mix of top- response. It makes rich and illuminating contact with
down and bottom-up influence is not static or fixed. work in cognitive neuroscience while boasting a firm
190 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
foundation in computational modeling and Bayesian and clearly suggestive, cannot establish strong conclusions
theory. It thus offers what is arguably the first truly sys- about the shape of the mechanisms generating those
tematic bridge27linking three ofour most promisingtools behaviors.
for understanding mind and reason: cognitive neuro- Morepromisinginthisregardareotherformsofindirect
science, computational modelling, and probabilistic Baye- evidence, such as the ability of computational simulations
sian approaches to dealing withevidenceand uncertainty. of predictive coding strategies to reproduce and explain a
variety of observed effects. These include non-classical
receptive field effects, repetition suppression effects, and
3. Fromaction-orientedpredictiveprocessingtoan thebi-phasicresponseprofilesofcertainneuronsinvolved
architecture ofmind in low-level visual processing.
Thusconsidernon-classicalreceptivefieldeffects(Rao&
Despite that truly impressive list of virtues, both the hier- Sejnowski 2002). In one such effect, an oriented stimulus
archical predictive processing family of models and their yields a strong response from a cortical cell, but that
recentgeneralizationstoactionfaceanumberofimportant response is suppressed when the surrounding region is
challenges,rangingfromtheevidential(whataretheexper- filled with a stimulus of identical orientation, and it is
imental and neuroanatomical implications, and to what enhanced when the orientation of the central stimulus
extentaretheyborneoutbycurrentknowledgeandinvesti- is orthogonal to those of the surrounding region. This is a
gations?) to the conceptual (can we really explain so much surprising set of features. A powerful explanation of this
aboutperceptionandactionbydirectappealtoafundamen- result, Rao and Sejnowski (2002) suggest, is that the
talstrategyofminimizingerrorsinthepredictionofsensory observed neural response here signals error rather than
input?) to the more methodological (to what extent can some fixed content. It is thus smallest when the central
these accounts hope to illuminate the full shape of the stimulus is highly predictable from the surrounding ones,
human cognitive architecture?) In this section I address andlargestwhenitisactivelycounter-predictedbythesur-
each challenge in turn, before asking (sect. 4) how such roundings. A related account (Rao & Ballard 1999, based
modelsrelatetoourconsciousmentallife. on the simulation study sketched in sect. 1.2) explains
“end-stopping” effects, in which a lively neural response
to a preferred stimulus such as an oriented line segment
3.1. Theneuralevidence
ceases or becomes reduced when the stimulus extends
Directneuroscientifictestingofthehierarchicalpredictive farther than the neuron’s standard receptive field. Here,
codingmodel,andofitsaction-orientedextension,remains too, computational simulations using the predictive
initsinfancy.Thebestcurrentevidencetendstobeindir- coding strategy displayed the same effect. This is because
ect, and it comes in two main forms. The first (which is the natural images used to train the network contained
highly indirect) consists in demonstrations of precisely many more instances of these longer line segments, facili-
the kinds of optimal sensing and motor control that the tating prediction in (and only in) such cases. Extended
“Bayesian brain hypothesis” (sect. 2.2) suggests. Good linesegmentsarethusmorepredictable,soerror-signaling
examples here include compelling bodies of work on cue responsesarereducedoreliminated.Inshort,theeffectis
integration (see also sects. 2.2 above and 4.3 following) explained once more by the assumption that activity in
showing that human subjects are able optimally to weight these units is signaling error/mismatch. Similarly, Jehee
thevariouscuesarrivingthroughdistinctsensemodalities, and Ballard (2009) offer a predictive processing account
doingsoinwaysthatdelicatelyandresponsivelyreflectthe of “biphasic response dynamics” in which the optimal
current (context-dependent) levels of uncertainty associ- stimulus for driving a neuron (such as certain neurons in
ated with the information from different channels (Ernst LGN–lateral geniculate nucleus) can reverse (e.g., from
& Banks 2002; Knill & Pouget 2004–and for further dis- preferring bright to preferring dark) in a short (20 msec)
cussion, see Mamassian et al. 2002; Rescorla, in press). space of time. Once again the switch is neatly explained
This isbeautifully demonstrated, in thecase ofcombining asareflectionofaunit’sfunctionalroleasanerrorordiffer-
cues from vision and touch, by Bayesian models such as ence detector rather than a feature detector as such. In
that of Helbig and Ernst (2007). Similar results have such cases, the predictive coding strategy (sect. 1.1) is in
been obtained for motion perception, neatly accounting full evidencebecause:
forvariousillusionsofmotionperceptionbyinvokingstat-
Low-levelvisualinput[is]replacedbythedifferencebetween
istically valid priors that favor slower and smoother the input and a prediction from higher-level structures….
motions–see Weiss et al. (2002) and Ernst (2010). higher-level receptive fields … represent the predictions of
AnotherexampleistheBayesiantreatmentofcolorpercep- the visual world while lower-level areas … signal the error
tion (see Brainard 2009), which again accounts for various between predictions and the actual visual input. (Jehee &
knowneffects(here,colorconstanciesandsomecolorillu- Ballard2009,p.1)
sions) in terms ofoptimal cue combination. Finally, consider the case of “repetition suppression.”
ThesuccessoftheBayesianprograminthesearenas(for Multiple studies (for a recent review, see Grill-Spector
somemoreexamples,seeRescorla[inpress]andsect.4.4) etal.2006)haveshownthatstimulus-evokedneuralactivity
isimpossibletodoubt.Itisthusamajorvirtueofthehier- is reduced by stimulus repetition.28 Summerfield et al.
archical predictive coding account that it effectively (2008) manipulated the local likelihood of stimulus rep-
implements a computationally tractable version of the so- etitions, showing that the repetition-suppression effect is
called Bayesian Brain Hypothesis (Doya et al. 2007; Knill itself reduced when the repetition is improbable/unex-
&Pouget2004;seealsoFriston2003;2005;andcomments pected. The favored explanation is (again) that repetition
insects.1.2and2.2above).Butbehavioraldemonstrations normallyreducesresponsebecauseitincreasespredictabil-
of Bayesian performance, though intrinsically interesting ity(thesecondinstancewasmadelikelierbythefirst)and
BEHAVIORALANDBRAINSCIENCES(2013)36:3 191
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
thusreducespredictionerror.Repetitionsuppressionthus are now widely reported in the literature (see, e.g., Born
also emerges as a direct effect of predictive processing in etal. 2009;Pack &Born 2001).
the brain, and as such its severity may be expected to One extremely important and as yet not well-tested
vary (just as Summerfield et al. found) according to our implication of the general architectural form of these
local perceptual expectations. In general then, the predic- models is (recall sect. 2.1) that each level of processing
tive coding story offers a very neat and unifying expla- should contain two functionally distinct sub-populations
nation, of a wide variety ofsuch contextual effects. of units. One sub-population, recall, is doing the “real”
Can we find more direct forms of evidence as well? work of representing the current sensory cause: These
Functional imaging plays an increasing role here. For units (“representational neurons” or “state units”) encode
example, an fMRI study by Murray et al. (2002) revealed the area’s best guess, in context as processed so far, at
justthekindsofrelationshipspositedbythepredictivepro- the current stimulus. They thus encode what Friston
cessing (hierarchical predictive coding) story. As higher (2005, p. 829) describes as the area’s “conditional expec-
level areas settled into an interpretation of visual shape, tations of perceptual causes.” The other sub-population is
activityinV1wasdampened,consistentwiththesuccessful in the business of encoding precision-weighted prediction
higher-levelpredictionsbeingusedtoexplainaway(cancel errors: These units (so-called error units) fire when there
out) the sensory data. More recently, Alink et al. (2010) isamismatchbetweenwhatispredictedandwhatisappar-
found decreased responses for predictable stimuli using entlybeingobserved.Thetwosetsofunitsareassumedto
variants on an apparent motion illusion, while den Ouden interact in the manner prescribed by the hierarchical pre-
etal.(2010)reportsimilarresultsusingarbitrarycontingen- dictive coding model. That is to say, the error units
cies that were manipulated rapidly during the course of process signals from the representation units both at their
their experiments.29 Finally, the study by Egner et al. own level and at the level above, and the representation
(2010; described in sect. 2.3 above) went on to compare, units send signals to the error units both at their own
in simulation, several possible models that might be used level and at the level below. Forward connections thus
toaccountfortheirresults.Theauthorsfoundapredictive conveyerror,whilebackwardconnectionsare freetocon-
processing regime involving the co-presence of represen- struct(inapotentiallymuchmorecomplex,andhighlynon-
tation and error units (see sect. 2.1 earlier) to offer by far linearfashion)predictionsthataimtocancelouttheerror.
the best fit for their data. In that best-fit simulation, error Unfortunately, direct, unambiguous neural evidence for
(“face-surprise”) units are modeled as contributing twice these crucial functionally distinct sub-populations is still
asmuchtothefMRIsignalasrepresentation(“face-expec- missing. Hence:
tation”) units, leading the authors tocomment that: One limitation of these models–and of predictive coding in
Thecurrentstudyistoourknowledgethefirstinvestigationto general–is that to date no single neuron study has systemati-
callypursuedthesearchforsensorypredictionerrorresponses.
formally and explicitly demonstrate that population responses
(Summerfield&Egner2009,p.408)
in visual cortex are in fact better characterized as a sum of
featureexpectationandsurpriseresponsesthanbybottom-up Thegoodnewsisthatthereis,aswesaw,mountingand
featuredetection.(Egneretal.(2010,p.16607) converging indirect evidence for such a cortical architec-
ture in the form (largely) of increased cortical responses
The predictive processing model also suggests testable
to sensory surprise (surprisal). Crucially, there also exists
hypotheses concerning the ways in which interfering
(sect. 2.1) a plausible neuronal implementation for such a
(e.g., using TMS–transcranial magnetic stimulation–or
scheme involving superficial and deep pyramidal cells.
other methods) with the message-passing routines linking
Nonetheless, much more evidence is clearly needed for
higher to lower cortical areas should impact performance.
To take one specific example, the model of binocular the existence of the clean functional separation (between
the activity of different neuronal features or sub-popu-
rivalry rehearsedin section 1.4 predicts that:
lations) required by these models.30
LGN and blind spot representation activity measured with
fMRIwillnotsuggestthatrivalry isresolvedbeforebinocular
convergence, if deprived of backwards signals from areas
abovebinocularconvergence.(Hohwyetal.2008,p.699)
3.2. Scopeandlimits
In general, if the predictive processing story is correct,
we expect to see powerful context effects propagating According toMumford:
quite low down the processing hierarchy. The key prin- In the ultimate stable state, the deep pyramidals [conveying
ciple–and one that also explains many of the observed predictionsdownwards]wouldsendasignalthatperfectlypre-
dynamics of evoked responses–is that (subject to the dictswhateachlowerareaissensing,uptoexpectedlevelsof
caveatsmentionedearlierconcerningalreadyactiveexpec- noise, and the superficial pyramidals [conveying prediction
tations) “representations at higher levels must emerge
errorsupwards]wouldn’tfireatall.(Mumford1992,p.247)
before backward afferents can reshape the response In an intriguing footnote, Mumford then adds:
profile of neurons in lower areas” (Friston 2003, p. 1348). In some sense, this is the state that the cortex is trying to
In the case of evoked responses, the suggestion (Friston achieve: perfect prediction of the world, like the oriental
2005, sect. 6) is that an early component often tracks an Nirvana, as Tai-Sing Lee suggested to me, whennothing sur-
initialflurryofpredictionerror:onethatissoonsuppressed prisesyouandnewstimulicausethemerestrippleinyourcon-
(assuming the stimulus is not novel or encountered out of sciousness.(op.cit.,p.247,Note5)
itsnormal context) by successful predictionsflowing back- Thisremarkhighlightsaverygeneralworrythatissome-
wards from higher areas. Such temporal delays, which are times raised in connection with the large-scale claim that
exactly what one would expect if perception involves corticalprocessingfundamentallyaimstominimizepredic-
recruiting top-level models to explain away sensory data, tion error, thus quashing the forward flow of information
192 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
and achieving what Mumford evocatively describes as the offerare,wesaw,constrainedtobeprobabilistic(andgen-
“ultimate stable state.” It can beput likethis: erative model based) through and through. But that is
compatible with the use of the probabilistic-generative
How can a neural imperative to minimize prediction error by
modetoencodeinformationusingawidevarietyofdiffer-
enslaving perception, action, and attention accommodate the
obvious fact that animals don’t simply seek a nice dark room ent schemes and surface forms. Consider the well-docu-
and stay in it? Surely staying still inside a darkened room mented differences in the way the dorsal and ventral
would afford easy and nigh-perfect prediction of our own visual streams code for attributes of the visual scene.
unfolding neural states? Doesn’t the story thus leave out The dorsal stream (Milner & Goodale 2006) looks to
much that really matters for adaptive success: things like deploy modes of representation and processing that are
boredom, curiosity, play, exploration, foraging, and the thrill at some level of interest quite distinct from those coded
ofthehunt?
and computed in the ventral stream. And this will be
The simple response (correct, as far as it goes) is that true even if there is indeed, at some more fundamental
animals like us live and forage in a changing and challen- level,acommoncomputationalstrategyatworkthrough-
ging world, and hence “expect” to deploy quite complex out the visual and the motor cortex.
“itinerant” strategies (Friston 2010; Friston et al. 2009) to Discoveringthenatureofvariousinnerrepresentational
stay within our species-specific window of viability. formatsisthusrepresentativeofthelargerprojectofunco-
Change, motion, exploration, and search are themselves veringthefullshapeofthehumancognitivearchitecture.It
valuable for creatures living in worlds where resources seemslikelythat,asarguedbyEliasmith(2007),thislarger
are unevenly spread and new threats and opportunities project will demand a complex combination of insights,
continuously arise. This means that change, motion, some coming “top-down” from theoretical (mathematical,
exploration, and search themselves become predicted– statistical, and computational) models, and others coming
and poised to enslave action and perception accordingly. “bottom-up” from neuroscientific work that uncovers the
Onewaytounpack this ideawouldbetolookattheposs- brain’s actual resources as sculpted by our unique evol-
ibleroleofpriorsthatinducemotionthroughastatespace utionary (and–as we’llnext see–sociocultural) trajectory.
until an acceptable, though possibly temporary or other-
wiseunstable,stoppingpoint(anattractor)isfound.Inpre-
3.3. Neatsversusscruffies(twenty-firstcenturyreplay)
cisely this vein Friston (2011a, p. 113) comments that
“some species are equipped with prior expectations that Backinthelate1970sandearly1980s(theheydayofclas-
they will engage in exploratoryor social play.” sical Artificial Intelligence [AI]) there was a widely held
The whole shape of this space of prior expectations is viewthattwopersonalitytypeswerereflectedintheorizing
specific to different species and may also vary as a result about the human mind. These types were dubbed, by
of learning and experience. Hence, nothing in the large- Roger Schank and Robert Abelson, the “neats” versus the
scale story about prediction error minimization dictates “scruffies.”31 Neats believed in a few very general, truth-
any general or fixed balance between what is sometimes conducive principles underlying intelligence. Scruffies
glossed as “exploration” versus “exploitation” (for some saw intelligence as arising from a varied bag of tricks: a
further discussion of this issue, see Friston & Stephan rickety tower of rough-and-ready solutions to problems,
2007, pp. 435–36). Instead, different organisms amount often assembled using various quick patches and local
(Friston 2011a) to different “embodied models” of their ploys, and greedily scavenging the scraps and remnants of
specific needs and environmental niches, and their expec- solutions to other, historically prior, problems and needs.
tations and predictions are formed, encoded, weighted, Famously,thiscanleadtoscruffy,unreliable,orsometimes
and computed against such backdrops. This is both good merely unnecessarily complex solutions to ecologically
news and bad news. It’s good because it means the novel problems such as planning economies, building
stories on offer can indeed accommodate all the forms of railway networks, and maintaining the Internet. Such his-
behavior (exploration, thrill-seeking, etc.) we see. But it’s torically path-dependent solutions were sometimes called
bad(oratleast,limiting)becauseitmeansthattheaccounts “kluges”–see, for example, Clark (1987) and Marcus
don’tinthemselvestellusmuchatallaboutthesekeyfea- (2008).Neatsfavoredlogicandprovablycorrectsolutions,
tures: features which nonetheless condition and constrain while scruffies favored whatever worked reasonably well,
an organism’s responses in a variety of quite fundamental fast enough, in the usual ecological setting, for some
ways. given problem. The same kind of division emerged in
Inoneway,ofcourse,thisisclearlyunproblematic.The early debates between connectionist and classical AI (see,
briefestglance atthestaggeringvariety ofbiological(even e.g., Sloman 1990), with connectionists often accused of
mammalian) life forms tells us that whatever fundamental developingsystemswhoseoperatingprinciples(aftertrain-
principlesaresculptinglifeandmind,theyareindeedcom- ingonsomecomplexsetofinput-outputpairs)wasopaque
patible with an amazing swathe of morphological, neuro- and“messy.”Theconflictreappearsinmorerecentdebates
logical, and ethological outcomes. But in another way it (Griffiths et al. 2010; McClelland et al. 2010) between
canstillseemdisappointing.Ifwhatwewanttounderstand those favoring “structured probabilistic approaches” and
is the specific functional architecture of the human mind, those favoring “emergentist” approaches (where these are
the distance between these very general principles of pre- essentiallyconnectionistapproachesoftheparalleldistrib-
diction-error minimization and the specific solutions to uted processing variety).32
adaptive needs that we humans have embraced remains Myownsympathies(Clark1989;1997)havealwayslain
daunting. As a simple example, notice that the predictive more on the side of the scruffies. Evolved intelligence, it
processingaccountleaveswideopenavarietyofdeepand seemed to me (Clark 1987), was bound to involve a kind
importantquestionsconcerningthe natureandformat of of unruly motley of tricks and ploys, with significant path-
human neural representation. The representations on dependence, no premium set on internal consistency, and
BEHAVIORALANDBRAINSCIENCES(2013)36:3 193
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
fast effective situated response usually favored at the that of understanding the full human cognitive architec-
expense ofslower,more effortful, even ifmore truth-con- ture) that will be done by direct appeal to action-oriented
ducive modes of thought and reasoning. Seen through predictive processing and the amount that will still need
this lens, the “Bayesian brain” seems, at first glance, to tobedonebyuncoveringevolutionaryanddevelopmental
offer an unlikely model for evolved biological intelligence. trajectory-reflectingtricksandploys:thescruffyklugesthat
Implemented by hierarchical predictive processing, it gradually enabled brains like ours to tackle the complex
posits a single, fundamental kind of learning algorithm problems of themodern world.
(based on generative models, predictive coding, and pre-
diction-error minimization) that approximates the rational
ideal of Bayesian belief update. Suppose such a model
proves correct. Would this amount to the final triumph of 3.4. Situatedagents
the neats over the scruffies? I suspect it would not, and Wemayalsoaskwhat,ifanything,thehierarchicalpredic-
for reasons that shed additional light upon the questions tive processing perspective suggests concerning situated,
about scope and limits raised in theprevious section. world-exploiting agency (Clark 1997; 2008; Clark & Chal-
Favoring the “neats,” we have encountered a growing mers 1998; Haugeland 1998; Hurley 1998; Hutchins
body of evidence (sects. 2.2 and 2.3) showing that for 1995; Menary 2007; Noë 2004; 2009; Rowlands 1999;
many basic problems involving perception and motor 2006; Thelen & Smith 1994; Wheeler 2005; Wilson 1994;
control, human agents (as well as other animals) do 2004). At least on the face of it, the predictive processing
indeed manage to approximate the responses and choices story seems to pursue a rather narrowly neurocentric
of optimal Bayesian observers and actors. Nonetheless, a focus,albeitonethatreveals(sect.1.5)sometrulyintimate
considerable distance still separates such models from the linksbetweenperceptionandaction.Butdigalittledeeper
details of their implementation in humans or other and what we discover is a model of key aspects of neural
animals. It is here that the apparent triumph of the neats functioning that makes structuring our worlds genuinely
over the scruffies may be called into question. For the continuous with structuring our brains and sculpting our
Bayesian brain story tells us, at most, what the brain (or actions. Cashing out all the implications of this larger
better, the brain in action) manages to compute. It also picture is a future project, but a brief sketch may help set
suggests a good deal about the forms of representation thescene.
and computation that the brain must deploy: For Recall(sects.1.5and1.6)thatthesemodelsdisplayper-
example, it suggests (sect. 2.2) that the brain must deploy ceptionandactionworkinginproductivetandemtoreduce
a probabilistic representation of sensory information; that surprisal (where this measures the implausibility of some
it must take into account uncertainty in its own sensory sensory state given a model of the world). Perception
signals, estimate the “volatility” (frequency of change) of reduces surprisal by matching inputs with prior expec-
the environment itself (Yu 2007), and so on. But that still tations. Action reduces surprisal by altering the world
leaves plenty of room for debate and discovery as regards (including moving the body) so that inputs conform with
the precise shape of the large-scale cognitive architecture expectations. Working together, perception and action
within which allthis occurs. servetoselectivelysampleandactivelysculptthestimulus
Thehierarchicalpredictiveprocessingaccounttakesus array. These direct links to active sculpting and selective
afewimportantstepsfurther.Itoffersacomputationally sampling suggest deep synergies between the hierarchical
tractable approximation to true Bayesian inference. It predictive processing framework and work in embodied
says something about the basic shape of the cortical and situated cognition. For example, work in mobile
micro-circuitry. And, at least in the formulations I have robotics already demonstrates a variety of concrete ways
been considering, it predicts the presence of distinct in which perception and behavior productively interact
neural encodings for representation and error. But even via loops through action and the environment: loops that
taken together, the mathematical model (the Bayesian maynowbeconsidered asaffordingextra-neuralopportu-
brain) and the hierarchical, action-oriented, predictive nitiesfortheminimizationofpredictionerror.Inprecisely
processing implementation fail to specify the overall this vein, Verschure et al. (2003), in work combining
form of a cognitive architecture. They fail to specify, for robotics and statistical learning, note that “behavioural
example, how the brain (or better, the brain in the feedback modifies stimulus sampling and so provides an
context of embodied action) divides its cognitive labors additionalextra-neuronalpathforthereductionofpredic-
between multiple cortical and subcortical areas, what tion errors” (Verschure etal. 2003,p. 623).
aspects of the actual world get sensorially coded in the Moregenerally,considerrecentworkonthe“self-struc-
first place, or how best to navigate the exploit–explore turing of information flows.” This work, as the name
continuum (the grain of truth in the “darkened room” suggests, stresses the importance of our own action-based
worry discussed in sect. 3.2 above). It also leaves unan- structuring of sensory input (e.g., the linked unfolding
swered a wide range of genuine questions concerning across multiple sensory modalities that occurs when we
the representational formats used by different brain see,touch,andhearanobjectthatweareactivelymanipu-
areas or for different kinds of problems. This problem is lating). Such information self-structuring has been shown
only compounded once we reflect (Anderson 2007; also to promote learning and inference (see, e.g., Pfeifer et al.
see sect. 3.4 following) that the brain may well tackle 2007, and discussion in Clark 2008). Zahedi et al. (2010)
many problems arising later in its evolutionary trajectory translatethesethemesdirectlyintothepresentframework
bycannilyredeployingresourcesthatwereonceusedfor usingroboticsimulationsinwhichthelearningofcomplex
other purposes. coordination dynamics is achieved by maximizing the
In the most general terms, then, important questions amount of predictive information present in sensorimotor
remain concerning the amount of work (where the goal is loops.
194 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Extensions into the realm of social action and multi- environments” for thinking such as mathematics,
agentcoordinationarethenclosetohand.For,akeyprox- reading,34writing, structured discussion, and schooling,in
imal goal of information self-structuring, considered from a process that Sterelny (2003) nicely describes as “incre-
the action-oriented predictive-processing perspective, is mental downstream epistemic engineering.” The upshot
thereductionofmutualpredictionerroraswecollectively is that the human-built environment becomes a potent
negotiate new and challenging domains (see, e.g., recent source of new intergenerationally transmissible structure
work on synchronization and shared musical experience: that surrounds our biological brains (see, e.g., Griffiths &
Overy & Molnar-Szakacs 2009; and the “culture as pat- Gray 2001; Iriki & Taoka 2012; Oyama 1999; Sterelny
terned practices” approach suggested by Roepstorff et al. 2007;Stotz 2010;Wheeler&Clark 2009).
2010).Suchaperspective,byhighlightingsituatedpractice, Whatarethepotentialeffectsofsuchstackedandtrans-
very naturally encompasses various forms of longer-term missible designer environments upon prediction-driven
material and social environmental structuring. Using a learning in cortical hierarchies? Such learning routines
variety of tricks, tools, notations, practices, and media, we make human minds permeable, at multiple spatial and
structure our physical and social worlds so as to make temporal scales, to the statistical structure of the world
them friendlier for brains like ours. We color-code consu- as reflected in the training signals. But those training
mer products, we drive on the right (or left), paint white signals are now delivered as part of a complex develop-
linesonroads,andpostpricesinsupermarkets.Atmultiple mental web that gradually comes to include all the
time-scales, and using a wide variety of means (including complex regularities embodied in the web of statistical
words, equations, graphs, other agents, pictures, and all relations amongthesymbols andother forms ofsocio-cul-
the tools of modern consumer electronics) we thus stack tural scaffolding in which we are immersed. We thus self-
thedicesothatwecanmoreeasilyminimizecostlypredic- constructakindofrolling“cognitiveniche”abletoinduce
tionerrorsinanendlesslyempoweringcascadeofcontexts the acquisition of generative models whose reach and
from shopping and socializing, to astronomy, philosophy, depth far exceeds their apparent base in simple forms of
and logic. sensory contact with the world. The combination of “iter-
Consider, from this perspective, our many symbol- ated cognitive niche construction” and profound neural
mediatedloopsintomaterialculturevianotebooks,sketch- permeability by the statistical structures of the training
pads,smartphones,and,asPickering&Garrod(2007)have environment is both potent and self-fueling. When these
observed,conversationswithotheragents.(Forsomeintri- two forces interact, repeatedly reconfigured agents are
guing speculations concerning the initial emergence of all enabled to operate in repeatedly reconfigured worlds,
thosediscretesymbolsinpredictive,probabilisticcontexts, and the human mind becomes a constantly moving
see König & Krüger 2006.) Such loops are effectively target. The full potential of the prediction-error minimiz-
enabling new forms of reentrant processing: They take a ation model of how cortical processing fundamentally
highly processed cognitive product (such as an idea about operates will emerge only (I submit) when that model is
the world), clothe it in public symbols, and launch it out paired with an appreciation of what immersion in all
into the world so that it can re-enter our own system as a those socio-cultural designer environments can do (for
concrete perceptible (Clark 2006a; 2008), and one now some early steps in this direction, see Roepstorff et al.
bearing highly informative statistical relations to other 2010). Such a combined approach would implement a
such linguaform perceptibles.33 It is courtesy of all that version of so-called neuroconstructivism (Mareschal et al.
concretepublicvehiclinginspokenwords,writtentext,dia- 2007) which asserts that:
grams, andpictures that our bestmodels ofreality (unlike
those of other creatures) are stable, re-inspectable objects Thearchitectureofthebrain…andthestatisticsoftheenviron-
apt for public critique and refinement. Our best models ment,[are]notfixed.Rather,brain-connectivityissubjecttoa
broadspectrumofinput-,experience-,andactivity-dependent
oftheworldarethusthebasisforcumulative,communally
processes which shape and structure its patterning and
distributedreasoning,ratherthanjustthemeansbywhich
strengths…These changes, in turn, result in altered inter-
individual thoughts occur. The same potent processing actions with the environment, exerting causal influences on
regimes, now targeting these brand new types of statisti-
what is experienced and sensed in the future. (Sporns 2007,
cally pregnant “designer inputs,” are then enabled to dis- p.179)
cover and refine new generative models, latching onto
(andattimesactivelycreating)evermoreabstractstructure Allthissuggestsapossibletwistupontheworries(sects.
in theworld.Action andperception thus worktogether to 3.2and3.3)concerningtheabilityofthepredictiveproces-
reduce prediction error against the more slowly evolving sing framework to specify a full-blown cognitive architec-
backdrop of a culturally distributed process that spawns a ture. Perhaps that lack is not a vice but a kind of virtue?
succession of designer environments whose impact on the For what is really on offer, or so it seems to me, is best
development (e.g., Smith & Gasser 2005) and unfolding seen as a framework whose primary virtue is to display
ofhumanthoughtandreasoncanhardlybeoverestimated. some deep unifying principles covering perception,
Suchculturallymediatedprocessesmayincurcosts(sect. action, and learning. That framework in turn reveals us as
3.3) in the form of various kinds of path-dependence highlyresponsivetothestatisticalstructuresofourenviron-
(Arthur 1994) in which later solutions build on earlier ments, including the cascade of self-engineered “designer
ones. In the case at hand, path-based idiosyncrasies may environments.” It thus offers a standing invitation to evol-
become locked in as material artifacts, institutions, nota- utionary, situated, embodied, and distributed approaches
tions, measuring tools, and cultural practices. But it is tohelp“fillintheexplanatorygaps”whiledeliveringasche-
that very same trajectory-sensitive process that delivers maticbutfundamentalaccount ofthecomplexandcomp-
thevastcognitiveprofitsthatflowfromtheslow,multi-gen- lementary roles of perception, action, attention, and
erational development of stacked, complex “designer environmentalstructuring.
BEHAVIORALANDBRAINSCIENCES(2013)36:3 195
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
4. Content andconsciousness alive. It would do the evolved creature no good at all to
keep experiencing the scene as to some degree uncertain
How, finally, do the accounts on offer relate to a human if the current task requires a firm decision, and if its
mentallife?This,ofcourse,isthehardest–thoughpoten- neural processing has already settled on a good, strongly
tiallythemostimportant–questionofall.Icannothopeto supported bet as towhat’s (most probably) out there.
adequately address it in the present treatment, but a few Onewaytobegintocashthatoutistorecallthatbiologi-
preliminaryremarksmayhelptostructureaspaceforsub- cal systems will be informed by a variety of learned or
sequent discussion. innate “hyperpriors” concerning the general nature of the
world.Onesuchhyperprior,asremarkedduringthediscus-
sionofbinocularrivalryinsection1.4,mightbethatthereis
4.1. Agencyandexperience
onlyoneobject(onecauseofsensoryinput)inoneplace,at
To what extent, if any, do these stories capture or explain
agivenscale,atagivenmoment.35Another,moregermane
facts about what we might think of as personal (or agent- tothepresentdiscussion,mightbethattheworldisusually
level) cognition–the flow of thoughts, reasons, and ideas inonedeterminatestateoranother.Toimplementthis,the
that characterize daily conscious thought and reason? A brain might36 simply use a form of probabilistic represen-
first (but fortunately merely superficial) impression is that tation in which each distribution has a single peak
theyfallfarshortofilluminatingpersonal-levelexperience. (meaning that each overall sensory state has a single best
Forexample,thereseemstobealargedisconnectbetween explanation).Thiswouldruleouttrueperceptualambiguity
surprisal (the implausibility of some sensory state given a whileleavingplentyofroomforthekindofpercept-switch-
modeloftheworld–seesect.1.6)andagent-levelsurprise. ing seen in the binocular rivalry cases. The use of such a
This is evident from the simple fact that the percept that, representational form would amount to the deployment
overall, best minimizes surprisal (hence minimizes predic- of an implicit formal hyperprior (formal, because it con-
tion errors) “for” the brain may well be, for me the agent, cerns the form of the probabilistic representation itself)
some highly surprising and unexpected state of affairs– to the effect that our uncertainty can be described using
imagine, for example, the sudden unveiling of a large and such a unimodal probability distribution. Such a prior
doleful elephant elegantly smuggled onto the stage by a makes adaptive sense, given the kinds of brute fact about
professional magician. action mentioned above (e.g., we can only perform one
The two perspectives are, however, easily reconciled. action at a time, choosing the left turn or the right but
The large and doleful elephant is best understood as never both atonce).
improbable but not (at least not in the relevant sense– Such appeals to powerful (and often quite abstract)
recall sect. 3.2) surprising. Instead, that percept is the hyperpriors will clearly form an essential part of any
one that best respects what the system knows and expects larger, broadly Bayesian, story about the shape of human
about the world, given the current combination of driving experience. Despite this, no special story needs to be told
inputs and assigned precision (reflecting the brain’s about either the very presence or the mode of action of
degree of confidence in the sensory signal). Given the such hyperpriors. Instead, they arise quite naturally
right driving signal and a high enough assignment of pre- within bidirectional hierarchical models of the kind we
cision, top-level theories of an initially agent-unexpected have been considering where they may be innate (giving
kind can still win out so as to explain away that highly- them an almost Kantian feel) or acquired in the manner
weighted tide of incoming sensory evidence. The sight of of empirical (hierarchical) Bayes.37 Nonetheless, the sheer
thedolefulelephantmaythenemergeastheleastsurpris- potency of these highly abstract forms of “systemic expec-
ing (least “surprisal-ing”!) percept available, given the tation” again raises questions about the eventual spread of
inputs, the priors, and the current weighting on sensory explanatory weight: this time, between the framework on
prediction error. Nonetheless, systemic priors did not offerandwhatever additionalconsiderationsandmodesof
render that percept very likely in advance, hence
investigationmayberequiredtofixandrevealthecontents
(perhaps) thevalue tothe agent of thefeeling ofsurprise.
ofthehyperpriorsthemselves.38
The broadly Bayesian framework can also seem at odds
with the facts about conscious perceptual experience for
4.2. Illuminatingexperience:Thecaseofdelusions
a different reason. The world, it might be said, does not
look as if it is encoded as an intertwined set of probability It might be suggested that merely accommodating the
density distributions! It looks unitary and, on a clear day, range of human personal-level experiences is one thing,
unambiguous. But this phenomenology again poses no while truly illuminating them is another. Such positive
real challenge. What is on offer, after all, is a story about impact is, however, at least on the horizon. We glimpse
the brain’s way of encoding information about the world. the potential in an impressive body of recent work con-
It is not directly a story about how things seem to agents ducted within the predictive processing (hierarchical pre-
deploying that means of encoding information. There is dictive coding) framework addressing delusions and
clearly no inconsistency in thinking that the brain’s perva- hallucination in schizophrenia (Corlett et al. 2009a;
sive use of probabilistic encoding might yield conscious Fletcher & Frith 2009).
experiences that depict a single, unified, and quite unam- Recalltheunexpectedsightingoftheelephantdescribed
biguous scene. Moreover, in the context of an active in the previous section. Here, the system already com-
world-engaging system, such an outcome makes adaptive mandedanaptmodelableto“explainaway”theparticular
sense. For, the only point of all that probabilistic betting combination of driving inputs, expectations, and precision
is to drive action and decision, and action and decision (weighting on prediction error) that specified the doleful,
lacktheluxuryofbeingabletokeepalloptionsindefinitely graypresence.Butsuchisnotalwaysthecase.Sometimes,
196 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
dealing with ongoing, highly-weighted sensory prediction learning,andaffect intoasingleoverarchingeconomy:one
error may require brand new generative models gradually within which dopamine and other neurotransmitters
to be formed (just as in normal learning). This might hold control the “precision” (the weighting, hence the impact
the key, as Fletcher and Frith (2009) suggest, to a better on inference and on learning) of prediction error itself.
understandingoftheoriginsofhallucinationsanddelusion But when things go wrong, false inferences spiral and feed
(thetwo“positivesymptoms”)inschizophrenia.Thesetwo back upon themselves. Delusion and hallucination then
symptoms are often thought to involve two mechanisms become entrenched, being both co-determined and co-
and hence two breakdowns, one in “perception” (leading determining.
to the hallucinations) and one in “belief” (allowing these The same broadly Bayesian framework can be used
abnormal perceptions toimpact top-level belief). It seems (Corlett et al. 2009a) to help make sense of the ways in
correct(see,e.g.,Coltheart2007)tostressthatperceptual which different drugs, when given to healthy volunteers,
anomolies alone will not typically lead to the strange and can temporarily mimic various forms of psychosis. Here,
exotic belief complexes found in delusional subjects. But too, the key feature is the ability of the predictive coding
must we therefore think of the perceptual and doxastic framework to account for complex alterations in both
components aseffectively independent? learning and experience contingent upon the (pharmaco-
A possible link emerges if perception and belief-for- logically modifiable) way driving sensory signals are
mation, as the present story suggests, both involve the meshed, courtesy of precision-weighted prediction
attempt to match unfolding sensory signals with top-down errors, with prior expectancies and (hence) ongoing pre-
predictions. Importantly, the impact of such attempted diction. The psychotomimetic effects of ketamine, for
matching is precision-mediated in that the systemic example,aresaidtobeexplicableintermsofadisturbance
effects of residual prediction error vary according to the to the prediction error signal (perhaps caused by AMPA
brain’s confidence in the signal (sect. 2.3). With this in upregulation) and the flow of prediction (perhaps via
mind, Fletcher and Frith (2009) canvass the possible con- NMDAinterference).Thisleadstoapersistentprediction
sequences of disturbances to a hierarchical Bayesian error and–crucially–an inflated sense of the importance
systemsuchthatpredictionerrorsignalsarefalsely gener- or salience of the associated events, which in turn drives
ated and–more important–highly weighted (hence the formation of short-lived delusion-like beliefs (see
accorded unduesaliencefor driving learning). Corlett et al. 2009a, pp. 6–7; also, discussion in Gerrans
There are a number of potential mechanisms whose 2007). The authors go on to offer accounts of the varying
complex interactions, once treated within the overarching psychotomimetic effects of other drugs (such as LSD and
framework of prediction error minimization, might con- other serotonergic hallucinogens, cannabis, and dopamine
spiretoproducesuchdisturbances.Prominentcontenders agonists such as amphetamine) as reflecting other possible
include the action of slow neuromodulators such as dopa- varietiesofdisturbancewithinahierarchicalpredictivepro-
mine, serotonin, and acetylcholine (Corlett et al. 2009a; cessing framework.41
Corlett et al. 2010). In addition, Friston (2010, p. 132) Thisfluidspanningoflevelsconstitutes,itseemstome,
speculates that fast, synchronized activity between neural one of the key attractions of the present framework. We
areasmayalsoplayaroleinincreasingthegainonpredic- here move from considerations of normal and altered
tion error within the synchronized populations.39 The key states of human experience, via computational models
idea,howeverimplemented,isthatunderstandingtheposi- (highlighting prediction-error based processing and the
tivesymptomsofschizophreniarequiresunderstandingdis- top-downdeploymentofgenerativemodels),totheimple-
turbances in the generation and weighting of prediction mentingnetworksofsynapticcurrents,neuralsynchronies,
error.Thesuggestion(Corlettetal.2009a;2009b;Fletcher andchemicalbalancesinthebrain.Thehopeisthatbythus
& Frith 2009) is that malfunctions within that complex offeringanew,multilevelaccountofthecomplex,systema-
economy(perhapsfundamentallyrootedinabnormaldopa- tic interactions between inference, expectation, learning,
minergic functioning) yield wave upon wave of persistent and experience, these models may one day deliver a
and highly weighted “false errors” that then propagate all better understanding even of our own agent-level experi-
the way up the hierarchy forcing, in severe cases (via the encethanthataffordedbythebasicframeworkof“folkpsy-
ensuingwavesofneuralplasticity)extremelydeeprevisions chology.” Such an outcome would constitute a vindication
inourmodeloftheworld.Theimprobable(telepathy,con- oftheclaim(Churchland1989;2012)thatadoptinga“neu-
spiracy, persecution, etc.) then becomes the least surpris- rocomputational perspective” might one day lead us to a
ing, and–because perception is itself conditioned by the deeper understanding ofour ownlived experience.
top-downflowofpriorexpectations–thecascadeofmisin-
formation reaches back down, allowing false perceptions
4.3. Perception,imagery,andthesenses
andbizarrebeliefstosolidifyintoacoherentandmutually
supportive cycle. Anotherareainwhichthesemodelsaresuggestiveofdeep
Such a process is self-entrenching. As new generative facts about the nature and construction of human experi-
models take hold, their influence flows back down so that enceconcernsthecharacterofperceptionandtherelations
incomingdataissculptedbythenew(butnowbadlymisin- between perception and imagery/visual imagination. Pre-
formed)priorssoasto“conformtoexpectancies”(Fletcher diction-driven processing schemes, operating within hier-
&Frith2009,p.348).Falseperceptionsandbizarrebeliefs archical regimes of the kind described above, learn
thusformanepistemicallyinsulatedself-confirmingcycle.40 probabilisticgenerativemodelsinwhicheachneuralpopu-
This, then, is the dark side of the seamless story (sect. 2) lation targets the activity patterns displayed by the neural
about perception and cognition. The predictive processing population below. What is crucial here–what makes such
model merges–usually productively–perception, belief, models generative as we saw in section 1.1–is that they
BEHAVIORALANDBRAINSCIENCES(2013)36:3 197
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
canbeused“top-down”topredictactivationpatternsinthe a flexible combination of top-down predictions and
level below. The practical upshot is that such systems, driving sensory signal.
simply as part and parcel of learning to perceive, develop But then why, given this unifying model in which the
the ability to self-generate42 perception-like states from senses work together to provide ongoing “feedback” on
thetopdown,bydrivingthelowerpopulationsintothepre- top-down predictions that aim to track causal structure in
dicted patterns. the world, do we experience sight as different from
There thus emerges a rather deep connection between sound, touch as different from smell, and so on? Why,
perception and the potential for self-generated forms of that is, do we not simply experience the overall best-esti-
mental imagery (Kosslyn et al. 1995; Reddy et al. 2010). mated external states of affairs without any sense of the
Probabilistic generative model based systems that can structure of distinct modalities in operation as we do so?
learn to visually perceive a cat (say) are, ipso facto, This is a surprisingly difficult question, and any answer
systems that can deploy a top-down cascade to bring must remain tentative in advance of a mature scientific
about many of the activity patterns that would ensue in story about conscious experience itself. A place to start,
the visual presence of an actual cat. Such systems thus though, is by noticing that despite the use of a single
display (formorediscussion ofthis issue, seeClark (forth- general processing strategy (the use of top-down predic-
coming) a deep duality of perception and imagination.43 tions to attempt to explain away sensory prediction error),
The same duality is highlighted by Grush (2004) in the there remain important differences between what is
“emulator theory of representation,” a rich and detailed being “explained away” within the different modalities.
treatment that shares a number of key features with the Thisisprobablybestappreciatedfromtheoverarchingper-
predictive processing story.44 spective of Bayesian perceptual inference. Thus, vision,
Hierarchicalpredictiveprocessingalsoprovidesamech- haptics, taste, and audition each trade in sensory signals
anismthatexplainsavarietyofimportantphenomenathat captured by distinct transducers and routed via distinct
characterize sensory perception, such as cross- and multi- early processing pathways. The different sensory systems
modal context effects on early sensory processing. Murray then combine priors and driving signals in ways that may
et al. (2002) displayed (as noted in sect.3.1) the influence yield differing estimates even of the very same distal
of high-level shape information on the responses of cells state. It is true that the overall job of the perceptual
in early visual area V1. Smith and Muckli (2010) show system is to combine these multiple estimates into a
similar effects (using as input partially occluded natural single unified model of the distal scene. But different
scenes) even on wholly non-stimulated (i.e., not directly sensory systems specialize (unless one is pressed into
stimulated via the driving sensory signal) visual areas. unusualservice,asintheinterestingcaseofsensory-substi-
Murray et al. (2006) showed that activation in V1 is influ- tution technologies45) in estimating different environ-
enced by a top-down size illusion, while Muckli et al. mental features, and even where they estimate the same
(2005) and Muckli (2010) report activity relating to an feature, their estimates, and the reliability (in context) of
apparent motion illusion in V1. Even apparently “unimo- those estimates will vary. In a thick fog, for example,
dal” early responses are influenced (Kriegstein & Giraud vision is unreliable (delivering shape information with
2006) by information derived from other modalities, and high uncertainty) while touch is less affected, whereas
hence commonly reflect a variety of multimodal associ- when wearing thick gloves the reverse may be true. That
ations. Even the expectation that a relevant input will means that even where two senses are reporting on the
turn out to be in one modality (e.g., auditory) rather than very same environmental state (e.g., shape by sight, and
another(e.g.,visual)turnsouttoimpactperformance,pre- shape by touch) they may deliver different “guesses”
sumably by enhancing “the weight of bottom-up input for about what is out there: guesses that reflect inferences
perceptual inference on a given sensory channel” made on the basis of distinct priors, different sensory
(Langner et al.2011,p. 10). signals, and the differing uncertainties associated with
This whole avalanche of context effects emerges natu- those signals.
rally given the hierarchical predictive processing model. Such differences, it seems to me, should be enough to
Ifso-calledvisual,tactile,orauditorysensorycortexisactu- ground the obvious experiential differences between the
ally exploiting a cascade of downward influence from various modalities. At the same time, the operation of a
higherlevelswhosegoalisactivelytopredicttheunfolding common underlying processing strategy (Bayesian infer-
sensory signals (the ones originally transduced using the ence, here implemented using hierarchical predictive
various dedicated receptor banks of vision, sound, touch, coding)accountsfortheeasewithwhichmultipleconflict-
etc.) extensive downward-reaching multimodal and cross- ingestimatesareusuallyreconciledintoaunifiedpercept.
modal effects (including various kinds of “filling-in”) will Inthiswaytheframeworkonofferprovidesapowerfulset
follow. For any statistically valid correlations, registered of “fundamental cognitive particles” (generative models
within the increasingly information-integrating (or “meta- and precision-weighted prediction-error-driven proces-
modal”–Pascual-Leone & Hamilton 2001; Reich et al. sing) whose varying manifestations may yet capture both
2011) areas towards the top of the processing hierarchy, the variety and the hidden common structure of our
can inform the predictions that cascade down, through mental lives.
what were previously thought of as much more unimodal Difficult questions also remain concerning the best way
areas,allthewaytoareasclosertothesensoryperipheries. to connect an understanding of such “fundamental par-
Such effects appear inconsistent with the idea of V1 as a ticles”andthegrossstructureofourdaily(andbynowmas-
site for simple, stimulus-driven, bottom-up feature-detec- sively culturally underwritten) conception of our own
tion using cells with fixed (context-inflexible) receptive mental lives. In this daily or “folk” conception, we rather
fields. But they are fully accommodated by models that firmly distinguish between perceptions, thoughts,
depict V1 activity as constantly negotiated on the basis of emotions, and reasons, populating our minds with distinct
198 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
constructs such as memories, beliefs, hopes, fears, and representation or hypothesis but (precisely) the world.
(agent-level) expectations. We thus depict minds and We do so courtesy ofthe brain’sability to latch on to how
selves in ways that are likely to make at best indirect the world is by means of a complex flow of sub-personal
contact (see, e.g., Barrett 2009; Clark 1989; Dennett processes.Thatflow,ifthesestoriesareontrack,fullywar-
1978; 1987) with the emerging scientific vision. Yet brid- rantsthe“Helmholtzian”descriptionofperceptionasinfer-
gingbetweenthesevisions(themanifestandthescientific ence. But it is precisely by such means that biological
image; Sellars 1962) remains essential if we are to gain beings are able to establish a truly tight mind-world
maximal benefits from a better understanding of the linkage. Brains like these are statistical spongesstructured
inner (and outer) machinery itself. It is essential if, for (sect. 1.2) by individual learning and evolutionary inheri-
example, we aspire to deploy our new understandings to tance so as to reflect and register relevant aspects of the
improve socialrelations and education, to increase human causal structure ofthe world itself.47
happiness, or to inform our responses to social problems. Oneplacewherethisbecomesespeciallyevidentisinthe
Tobridgethisgapwillplausiblyrequireeffort andcompro- treatment (sect. 2.2) of visual illusions as Bayes-optimal
mise from both sides (Humphrey 2000), as the folk percepts. The idea, recall, is that the percept–even in
conception alters under the influence of a scientific under- thecaseofvariouseffectsandillusions–isanaccurateesti-
standing that must itself recognize the causal potency of mation of the most likely real-world source or property,
the folk-psychological constructs: constructs which we givennoisysensoryevidenceandthestatisticaldistribution,
encounter and model just as surely as we encounter and within some relevant sample, of real-world causes. This is
modelotherconstructssuchasmarriage,divorce,andtaxes. an important finding that has now been repeated in many
domains, including the sound-induced flash illusion
(Shams et al. 2005), ventriloquism effects (Alais & Burr
4.4. Sensingandworld 2004) and the impact of figure-ground convexity cues in
depth perception (Burge et al. 2010). Additionally, Weiss
What, then, of the mind–world relation itself? Hohwy
etal.’s(2002)Bayes-optimalaccountofaclassofstatic(fix-
(2007) suggeststhat:
ation-dependent) motion illusions has now been extended
One important and, probably, unfashionable thing that this toaccount foramuchwidersetofmotionillusionsgener-
theorytellsusaboutthemindisthatperceptionisindirect… ated in the presence of active eye movements during
what we perceive is the brain’s best hypothesis, as embodied smooth pursuit (see Freeman et al. 2010, and discussion
in a high-level generative model, about the causes in the inErnst2010).Perceptualexperience,evenintheseillusory
outerworld.(Hohwy2007,p.322)
cases,thuslookstobeveridicallytrackingstatisticalrelations
Thereissomethingrightaboutthis.Thebulkofourdaily betweenthesensory dataanditsmost probablereal-world
perceptualcontactwiththeworld,ifthesemodelsareonthe sources. The intervening mechanisms thus introduce no
mark,isdeterminedasmuchbyourexpectationsconcerning worrisome barrier between mind and world. Rather, it is
thesensedsceneasbythedrivingsignalsthemselves.Even only because of such sub-personal complexities that agents
morestrikingly,theforwardflowofsensoryinformationcon- likeuscanbeperceptuallyopentotheworlditself.48
sistsonlyinthepropagationoferrorsignals,whilerichlycon-
tentful predictions flow downward, interacting in complex
5. Taking stock
non-linear fashions via the web of reciprocal connections.
Oneresultofthispatternofinfluenceisagreaterefficiency
5.1. Comparisonwithstandardcomputationalism
intheuseofneuralencodings,since:
Just how radical is the story we have been asked to con-
anexpectedeventdoesnotneedtobeexplicitlyrepresentedor sider? Isitbestseen asanalternativetomainstreamcom-
communicatedtohighercorticalareaswhichhaveprocessedall
putational accounts that posit a cascade of increasingly
of its relevant features prior to its occurrence. (Bubic et al.
complex feature detection (perhaps with some top-down
2010,p.10)
biasing), or is it merely a supplement to them: one whose
If this is indeed the case, then the role of perceptual main virtue lies in its ability to highlight the crucial role
contact with the world is only to check and, when necess- of prediction error in driving learning and response? I do
ary, correct the brain’s best guessing concerning what is not think we are yet in a position to answer this question
out there. This is a challenging vision, as it suggests that withanyauthority.ButthepictureIhavepaintedsuggests
our expectations are in some important sense the primary anintermediateverdict,atleastwithrespecttothecentral
source ofall the contents of our perceptions, even though issues concerning representation andprocessing.
such contents are constantly being checked, nuanced, and Concerning representation, the stories on offer are
selected by the prediction error signals consequent upon potentially radical in at least two respects. First, they
the driving sensory input.46 Perhaps surprisingly, the suggest that probabilistic generative models underlie both
immediate role of the impinging world is thus most sensory classification and motor response. And second,
marked when error signals, in a well-functioning brain, they suggest that the forward flow of sensory data is
drivethekindsofplasticitythatresultinperceptuallearn- replaced by the forward flow of prediction error. This
ing, rather than in the cases where we are simply success- latter aspect can, however, make the models seem even
fully engaging a well-understood domain. more radical than they actually are: Recall that the
Nonetheless,wemaystillrejectthebaldclaimthat“what forward flow of prediction error is here combined with a
weperceiveisthebrain’sbesthypothesis.”Evenifourown downwardflowofpredictions,andateverystageofproces-
predictionisindeed (atleast infamiliar,highly learntcon- singthemodelsposit(aswesawinsomedetailinsect.2.1)
texts)doingmuchoftheheavylifting,itremainscorrectto functionally distinct “error units” and “representation
say that what we perceive is not some internal units.” The representation units that communicate
BEHAVIORALANDBRAINSCIENCES(2013)36:3 199
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
predictions downward do indeed encode increasingly personal, affective, and hedonic significance. This folding-
complex and more abstract features (capturing context in is probably especially marked in frontolimbic cortex
and regularities at ever-larger spatial and temporal scales) (Merker 2004). But the potent web of backward connec-
in the processing levels furthest removed from the raw tions ensures that such folding-in, once it has occurred, is
sensoryinput.Inaveryrealsensethen,muchofthestan- able (as noted by Barrett & Bar 2009; see also sect. 2.2)
dardarchitectureofincreasinglycomplexfeaturedetection to impact processing and representation at every lower
is here retained. What differs is the shape of the flow of stage of the complex processing hierarchy. If this proves
information, and (relatedly) the pivotal role assigned to correct, then it is prediction error calculated relative to
thecomputation andpropagation ofprediction error. these affectively rich and personal-history–laden expec-
Arelatedissueconcernstheextenttowhichthenewfra- tations that drives learningand response.
mework reproduces traditional insights concerning the Thusconstrued,anaction-orientedpredictiveprocessing
specialization of different cortical areas. This is a large frameworkisnotsomuchrevolutionaryasitisreassuringly
question whose full resolution remains beyond the scope integrative.Itsgreatestvalueliesinsuggestingasetofdeep
of the present discussion. But in general, the hierarchical unifying principles for understanding multiple aspects of
form of these models suggests a delicate combination of neuralfunctionandorganization.Itdoesthisbydescribing
specialization and integration. Different levels learn and anarchitecturecapableofcombininghigh-levelknowledge
deploy different sets of predictions, corresponding to andlow-level(sensory)informationinwaysthatsystemati-
different bodies of knowledge, aimed at the level below cally deal with uncertainty, ambiguity, and noise. In so
(specialization)butthesystemsettlesinawaylargelydeter- doing it reveals perception, action, learning, and attention
minedbytheoverallflowandweightingofpredictionerror, as different but complementary means to the reduction
wherethisflowisitselfvariedaccordingtocurrentcontext of (potentially affect-laden and goal-reflecting) prediction
andthereliabilityandrelevanceofdifferenttypesofinfor- error in our exchanges with the world. It also, and simul-
mation (integration).49 taneously,displayshumanlearningassensitivelyresponsive
Asecondsourceofpotentialradicalismlieswiththesug- tothedeepstatisticalstructurespresentinbothournatural
gestion(sect.1.5)that,inextendingthemodelstoinclude and human-built environments. Thus understood, action-
action (“action-oriented predictive processing”), we might oriented predictive processing leaves much unspecified,
simultaneously do away with the need to appeal to goals including (1) the initial variety of neural and bodily struc-
and rewards, replacing them with the more austere con- tures (and perhaps internal representational forms) man-
struct ofpredictions. In this vein, we read that: dated by our unique evolutionary trajectory, and (2) the
Crucially,activeinferencedoesnotinvokeany“desiredconse- acquiredvarietyof“virtual”neuralstructuresandrepresen-
quences.” It rests only on experience-dependent learning and tational forms installed by our massive immersion in
inference: Experience induces prior expectations, which “designerenvironments”duringlearninganddevelopment.
guide perceptual inference and action. (Friston et al. 2011, To fill in these details requires, or so I have argued, a
p.157) deep(butsatisfyinglynatural)engagementwithevolution-
Inthis desert landscape vision,there areneither goals nor ary, embodied, and situated approaches. Within that
rewardsignalsassuch.Instead,thereareonly(bothlearnt context,seeinghowperception,action,learning,andatten-
and species-specific) expectations, across many spatial and tionmightallbeconstructedoutofthesamebasematerials
temporal scales, which directly enslave both perception (prediction andpredictionerrorminimization)ispowerful
and action. Cost functions, in other words, are replaced and illuminating. It is there that Friston’s ambitious syn-
by expectations concerning actions and their sensory thesis is at its most suggestive, and it is there that we
(especially proprioceptive) consequences. Here, I remain locate the most substantial empirical commitments of the
unconvinced. For even if such an austere description is account. Those commitments are to the computation (by
indeedpossible(andforsomecriticalconcerns,seeGersh- dedicated error units or some functionally equivalent
man&Daw2012),thatwouldnotimmediatelyjustifyour means) and widespread use by the nervous system of pre-
claiming that it thereby constitutes the better tool for cision-weighted prediction error, and its use as proxy for
understanding the rich organization of the cognitive the forward flow of sensory information. The more wide-
economy. To see this, we need only reflect that it’s all spread this is, the greater the empirical bite of the story.
“just” atoms, molecules, and the laws of physics too, but If it doesn’t occur, or occurs only in a few special circum-
that doesn’t mean those provide the best constructs and stances, the story fails as a distinctive empirical account.50
components for the systemic descriptions attempted by
cognitive science. The desert landscape theorist thus
5.2. Conclusions:Towardsagrandunifiedtheoryofthe
needstodomore,itseemstome,todemonstratetheexpla-
mind?
natory advantages of abandoning more traditional appeals
to value, reward, and cost (or perhaps to show that those Action-oriented predictive processing models come tanta-
appeals make unrealistic demands on processing or lizingly close to overcoming some of the major obstacles
implementation–seeFriston2011b). blocking previous attempts to ground a unified science of
Whatmaywellberightaboutthedesertlandscapestory, mind, brain,and action. They take familiar elements from
itseemstome,isthesuggestion thatutility (ormoregen- existing, well-understood, computational approaches
erally, personal and hedonic value) is not simply a kind of (suchasunsupervisedandself-supervisedformsoflearning
add-on, implemented by what Gershman and Daw (2011, using recurrent neural network architectures, and the use
p. 296) describe as a “segregated representation of prob- of probabilistic generative models for perception and
ability and utility in the brain.” Instead, it seems likely action) and relate them, on the one hand, to a priori con-
that we represent the very eventsoverwhich probabilities straints on rational response (the Bayesian dimension),
become defined in ways that ultimately fold in their and, on the other hand, to plausible and (increasingly)
200 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
testableaccountsofneuralimplementation.Itisthispotent hierarchical predictive coding regime? How confident are
positioning between the rational, the computational, and we of the basic Bayesian gloss on our actual processing?
the neural that is their most attractive feature. In some (Do we, for example, have a firm enough grip on when a
ways, they provide the germ of an answer to Marr’s system is computing its outputs using a “genuine approxi-
dream: a systematic approach that addresses the levels of mation” to a true Bayesian scheme, rather than merely
(in the vocabulary of Marr 1982) the computation, the behaving “as if” itdid so?)
algorithm, and the implementation. Thechallenges(empirical,conceptual,andmethodologi-
The sheer breadth of application is striking. Essentially cal) are many and profound. But the potential payoff is
thesamemodelshereaccountforavarietyofsuperficially huge. What is on offer is a multilevel account of some of
disparate effects spanning perception, action, and atten- the deepest natural principles underlying learning and
tion. Indeed, one way to think about the primary “added inference,andonethatmaybecapableofbringingpercep-
value” of these models is that they bring perception, tion, action, and attention under a single umbrella. The
action, and attention into a single unifying framework. ensuing exchanges between neuroscience, computational
They thus constitute the perfect explanatory partner, I theorizing, psychology, philosophy, rational decision
have argued, for recent approaches that stress the embo- theory, and embodied cognitive science promise to be
died, environmentally embedded, dimensions of mind among the major intellectual events of the early twenty-
and reason.51 Perception, action, and attention, if these first century.
views are correct, are all in the same family business: that
of reducing sensory prediction error resulting from our ACKNOWLEDGMENTS
exchanges with the environment. Once this basic family Thistargetarticlehasbenefittedenormouslyfromcommentsand
business is revealed, longer-term environmental structur- reactions from a wide variety of readers and audiences. Special
ing (both material and socio-cultural) falls neatly into thanks are due to the BBS referees, who provided an especially
place. We structure our worlds and actions so that most rich and challenging set of comments and suggestions. The
of our sensory predictions come true. present incarnation of this article owes a great deal to their
patient and extensive help and probing. Thanks also to Karl
But this neatness hides important complexity. For,
Friston, Jakob Hohwy, Tim Bayne, Andreas Roepstorff, Chris
another effect of all that material and socio-cultural scaf-
Thornton, Liz Irvine, Matteo Colombo, and all the participants
foldingistoinducesubstantialpath-dependenceaswecon-
at the Predictive Coding Workshop (School of Informatics,
front new problems using pre-existing material tools and
University of Edinburgh, January 2010); to Phil Gerrans, Nick
inherited social structures. The upshot, or so I have Shea, Mark Sprevak, Aaron Sloman, and the participants at the
argued, is that a full account of human cognition cannot first meeting of the UK Mind Network held at the Faculty of
hopeto“jump”directlyfromthebasicorganizingprinciples Philosophy, Oxford University, March 2010; to Markus
of action-oriented predictive processing to an account of Werning, and the organizers and participants of the 2010
the full (and in some ways idiosyncratic) shape of human meeting of the European Society for Philosophy and
thought andreason. Psychology, held at Ruhr-Universität Bochum, August 2010; to
Nihat Ay, Ray Guillery, Bruno Olshausen, Murray Sherman,
What emerges instead is a kind of natural alliance. The
Fritz Sommer, and the participants at the Perception & Action
basic organizing principles highlighted by action-oriented
Workshop, Santa Fe Institute, New Mexico, September 2010;
predictive processing make us superbly sensitive to the
to Daniel Dennett, Rosa Cao, Justin Junge, and Amber Ross
structure and statistics of the training environment. But
(captain and crew of the hurricane-Irene-blocked 2011
our human training environments are now so thoroughly CognitiveCruise);toMiguelEckstein,MikeGazzaniga,Michael
artificial, and our explicit forms of reasoning so deeply Rescorla, and the faculty and students at the Sage Center for
infected by various forms of external symbolic scaffolding, the Study of Mind, University of California, Santa Barbara,
that understanding distinctively human cognition where,asaVisiting Fellowin September2011,Iwasprivileged
demands a multiply hybrid approach. Such an approach toroad-testmuchofthismaterial;andtoPeterKönig,JonBird,
would combine the deep computational insights coming Lee de-Wit, Suzanna Siegel, Matt Nudds, Mike Anderson,
Robert Rupert, Bill Phillips, and Rae Langton. A much earlier
from probabilistic generative approaches (among which
figure action-oriented predictive processing) with solid version of some of this material was prepared thanks to support
neuroscientific conjecture and with a full appreciation of from the AHRC, under the ESF Eurocores CONTACT
(ConsciousnessinInteraction)project,AH/E511139/1.
the way our many self-structured environments alter and
transform the problem spaces of human reason. The
NOTES
most pressing practical questions thus concern what
1. This remark is simply described as a “scribbled, undated,
might be thought of as the “distribution of explanatory aphorism” in the online digital archive of the scientist’s journal:
weight” between the accounts on offer, and approaches Seehttp://www.rossashby.info/index.html.
that explore or uncover these more idiosyncratic or evol- 2. I am greatly indebted to an anonymous BBS referee for
utionary path-dependent features of the human mind, encouraging me to bring these key developments into clearer
andthecomplextransformativeeffectsofthesocio-cultural (bothhistoricalandconceptual)focus.
cocoonin which itdevelops. 3. The obvious problem was that this generative model itself
Questions also remain concerning the proper scope of neededtobelearnt:somethingthatwouldinturnbepossibleif
a good recognition model was already in place, since that could
the basic predictive processing account itself. Can that
provide the right targets for learning the generative model. The
account really illuminate reason, imagination, and action-
solution (Hinton et al. 1995) was to use each to gradually boot-
selection in all its diversity? What do the local approxi-
strap the other, using the so-called “wake-sleep algorithm”–a
mations to Bayesian reasoning look like as we depart
computationallytractableapproximationto“maximumlikelihood
furtherandfurtherfromthesafeshoresofbasicperception learning”asseenintheexpectation-maximization(EM)algorithm
andmotor control? Whatnewformsofrepresentation are ofDempsteretal.(1977).Despitethis,theHelmholtzMachine
thenrequired,andhowdotheybehaveinthecontextofthe remained slow and unwieldy when confronted with complex
BEHAVIORALANDBRAINSCIENCES(2013)36:3 201
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
problemsrequiringmultiplelayersofprocessing.Butitrepresents impact of the driving sensory signal is effectively altered so that
animportantearlyversionofanunsupervisedmultilayerlearning the best interpretation flips. Attention thus engages the same
device,or“deeparchitecture”(Hinton2002;2007b;2010;Hinton (broadlyBayesian)mechanism,butviaadifferent(andpotentially
&Salakhutdinov2006;Hintonetal.2006;forreviews,seeBengio lessautomatic)route.Thisalsoexplains,withinthepresentframe-
2009;Hinton2007a). work,whywehavemuchmorecontroloverthealternationratein
4. This names the probability of an event (here, a worldly thecaseofambiguousfigures(asdemonstratedbyMeng&Tong
cause), given some set of prior beliefs and the evidence (here, 2004).
the currentpattern of sensorystimulation). For our purposes,it 12. Thisisalsoknown(see,e.g.,Fristonetal.2009)as“active
thus names the probability of a worldly (or bodily) cause, con- inference.” I coin “action-oriented predictive processing” as it
ditionedonthesensoryconsequences. makesclearthatthisisanaction-encompassinggeneralizationof
5. In speaking of “predictive processing” rather than resting the (hierarchical) predictive coding story about perception. It
withthemorecommonusage“predictivecoding,”Imeantohigh- also suggests (rightly) that action becomes conceptually primary
lightthefactthatwhatdistinguishesthetargetapproachesisnot in these accounts, since it provides the only way (once a good
simplytheuseofthedatacompressionstrategyknownaspredic- world model is in place and aptly activated) to actually alter the
tive coding. Rather, it is the use of that strategy in the special sensory signal so as to reduce sensory prediction error–see
contextofhierarchicalsystemsdeployingprobabilisticgenerative Friston (2009, p. 295). In addition, Friston’s most recent work
models.Suchsystemsexhibitpowerfulformsoflearningandare on active inference looks to involve a strong commitment (see
ableflexiblytocombinetop-downandbottom-upflowsofinfor- especially Friston 2011a) to the wholesale replacement of value
mationwithinamultilayercascade. functions,consideredasdeterminantsofaction,withexpectations
6. In what follows, the notions of prior, empirical prior, and (“priorbeliefs,”thoughnotethat“belief”hereisverybroadlycon-
priorbeliefareusedinterchangeably,giventheassumedcontext strued)aboutaction.Thisisaninterestingandchallengingsugges-
ofahierarchicalmodel. tionthatgoesbeyondclaimsconcerningformalequivalenceand
7. Because these proposals involve the deployment of top- even beyond the observations concerning deep conceptual
downprobabilisticgenerativemodelswithinamultilayerarchitec- relations linking action and perception. “Action-oriented predic-
ture,itistheorganizationalstructureoftheneocortexthatmost tive processing,” as I shall use the term, remains deliberately
plausibly provides the requisite implementation. This is not to agnosticonthisimportantmatter(seealsosect.5.1).
rule out related modes of processing using other structures, for 13. Inoteinpassingthatthisradicalviewresonateswithsome
example, in nonhuman animals, but simply to isolate the “best influential philosophical work concerning high level (reflective)
fit.” Nor is it to rule out the possibility that, moment-to- intentionsandactions:specifically,Velleman’s(1989)accountof
moment, details of the large-scale routing of information flow practical reasoning in which intentions to act are depicted as
within the brain might depend on gating effects that, although self-fulfillingexpectationsaboutone’sownactions(see,e.g.,Vel-
cortically mediated, implicate additional structures and areas. leman1989,p.98).
For some work on such gating effects among cortical structures 14. Themostfundamentalaspectoftheappealtofreeenergy,
themselves,seedenOudenetal.(2010). Friston claims, is that it provides an organismically computable
8. Ihaveadoptedtheneuroanatomistpracticeoflabelingcon- window on surprise (i.e., surprisal) itself, since “…surprise
nections simply as “backward” and “forward” so as to avoid the cannot be quantified by an agent, whereas free energy can”
functional implications of the labels “feedback” and “feedfor- (Friston 2010, p. 55). I read this as meaning, in the present
ward.” This is important in the context of predictive processing context, that prediction error is organismically computable,
models,sinceitisnowtheforwardconnectionsthatarereallypro- sinceitrepresents(aswesawinsect.1.2)aninternallycalculable
viding(byconveyingpredictionerror)feedbackonthedownward- quantity.This,however,isnotafeatureIwillattempttoexplorein
flowingpredictions–seeFriston(2005),Hohwy(2007),anddis- thepresenttreatment.
cussion in section 2.5 of the present article. Thanks to one of 15. Foraninterestingcritiqueofthemostambitiousversionof
theBBSreviewersforthishelpfulterminologicalsuggestion. the free energy story, see section 5.1 in Gershman and Daw
9. Noticethatanerrorsignalthusconstruedishighlyinforma- (2012).
tive, and in this respect it differs from the kinds of error signal 16. Thiskindofefficiency,asoneoftheBBSrefereesnicely
familiarfromcontroltheoryandsystemsengineering.Thelatter noted, is something of a double-edged sword. For, the obvious
aremostlysimplesignalsthatrepresenttheamountoferror/mis- efficiencies in forwardprocessing areherebought at the cost of
match. The former (“prediction error signals”) are much richer the multilevel generative machinery itself: machinery whose
and carry information not just about the quantity of error but implementationandoperationrequiresawholesetofadditional
(in effect) about the mismatched content itself. It is in this connections to realize the downward swoop of the bidirectional
sense that the residual errors are able, as it is sometimes said hierarchy.Thecasefor predictiveprocessing isthusnotconvin-
(Feldman & Friston 2010) to stand in for the forward flow of cingly made on the basis of “communicative frugality” so much
sensory information itself. Prediction errors are as structured asuponthesheerpowerandscopeofthesystemsthatresult.
and nuanced in their implications as the predictions relative to 17. In personal correspondence, Lee de-Wit notes that his
which they are computed. (Thanks to an anonymous BBS usage follows that of, for example, Murray et al. (2004) and
refereeforsuggestingthisimportantclarification). Dumoulin and Hess (2006), both of whom contrast “predictive
10. Hosoyaetal.herebuildonearlierworkbySrinivasanetal. coding” with “efficient coding,” where the former uses top-
(1982).Seealsoinformation-theoretictreatmentsofmutualinfor- down influence to subtract out predicted elements of lower-
mation,suchasLinsker(1989).Foralargerperspective,seeClif- level activity, and the latter uses top-down influence to enhance
fordetal.(2007). or sharpen it. This can certainly make it look as if the two
11. What about more common forms of perceptual alterna- stories (subtraction and sharpening) offer competing accounts
tion, such as those induced by ambiguous figures like the of,forexample,fMRIdatasuchasMurrayetal.(2002)showing
Necker cube or the duck-rabbit? In these instances, the gross a dampening of response in early visual areas as higher areas
driving sensory input is exactly the same for the two percepts, settled into an interpretation of a shape stimulus. The accounts
soswitchingcannotbeinducedsimplybytheongoinginfluence would be alternatives, since the dampening might then reflect
of the unexplained portions of bottom-up input. Instead, such eitherthesubtractionofwell-predictedpartsoftheearlyresponse
casesarebestexplainedbyasimilarprocessinvolvingattentional (“predictivecoding”)orthequashingoftherestoftheearlysignal
modulations(whichmay,butneednot,bedeliberate).Attention and the attendant sharpening of the consistent elements. The
(see sect. 2.3) serves to increase the gain on select error units. models I am considering, however, accommodate both subtrac-
By altering the gain on some error units and not others, the tionandsharpening(seemaintextfordetails).Thisistherefore
202 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
aninstance(seesect.5.1)inwhichmoreradicalelementsofthe 29. Foranexcellentdiscussionofthisrecentwork,seede-Wit
target proposals (here, the subtracting away of predicted signal etal.(2010).
elements) turn out, on closer examination, to beconsistent with 30. Leede-Wit(personalcommunication)raisestheintriguing
morefamiliareffects(suchastop-downenhancement). possibilitythatthedistinctionbetweenencodingerrorandencod-
18. The consistency between selective sharpening and the ing representational content might be realized in alternate
dampening effects of “explaining away” also makes it harder– dynamics of the very same neuronal substrate, with early
thoughnotimpossible–toteaseaparttheempiricalimplications responsesencodingerrorandlateronessettlingintoarepresen-
ofpredictivecodingand“evidenceaccumulation”accountssuch tation of something like “agreed content.” In a related vein,
as Gold and Shadlen’s (2001)–for a review, see Smith and Rat- Engeletal.(2001)discussthepotentialroleofneuralsynchrony
cliff (2004). For an attempt to do so, see Hesselmann et al. as a means of implementing top-down influence on early
(2010). processing.
19. Inthis(2008a)treatmentSpratlingfurtherarguesthatthe 31. These terms, according to a memoir by Wendy Lehnert
formsofhierarchicalpredictivecodingaccountwehavebeencon- (2007), were introduced by Bob Abelson as part of a keynote
sideringaremathematicallyequivalenttosomeformsof“biased address to the 3rd Annual Meeting of the Cognitive Science
competition” model, but that they nonetheless suggest different Societyin1981.
claims concerning neural implementation. I take no position on 32. The hierarchical predictive coding family of models that
theseinterestingclaimshere. (along with their extensions to action) form the main focus of
20. Foranearlyoccurrenceofthisproposalintheliteratureof the present treatment are not, in my view, happily assimilated
cognitiveneuroscience,seeAndersonandVanEssen(1994).That toeitherofthesecamps.TheyclearlyshareBayesianfoundations
treatmentalsoanticipates(althoughitdoesnotattempttomodel) withthe“pure”structuredprobabilisticapproacheshighlightedby
the crucial role of top-down expectations and dynamic forms of Griffithsetal.,buttheircomputationalrootslie(aswesawinsect.
Bayesianinference. 1.1)inworkonmachinelearningusingartificialneuralnetworks.
21. Thanks to one of the BBS reviewers for suggesting this Importantly, however, hierarchical predictive processing models
importantnuancetothetemporalstory. now bring “bottom-up” insights from cognitive neuroscience
22. Thismeansthatweneedtobeverycarefulwhengeneral- intoincreasinglyproductivecontactwiththosepowerfulcompu-
izing from ecologically strange laboratory conditions that effec- tationalmechanismsoflearningandinference,inaunifyingfra-
tively deprive us of such ongoing context. For some recent meworkable(asGriffithsetal.correctlystress)toaccommodate
discussion, see Kveraga et al. (2007), Bar (2007), Barrett and averywidevarietyofsurfacerepresentationalforms.Moreover,
Bar(2009),andFabre-Thorpe(2011). suchapproachesarecomputationallytractablebecauselocal(pre-
23. An interesting alternative to the inference-rich Bayesian diction-errorminimizing)routinesarebeingusedtoapproximate
account is suggested by Purves and Lotto (2003), who offer a Bayesian inference. For some excellent antidotes to the appear-
more direct account in terms of the bare statistics of image- ance of deep and irreconcilable conflict hereabouts, see
sourcerelationships.ForacomparisonwithBayesianapproaches, Feldman(2010)andLee(2010).
seeHoweetal.(2006). 33. We glimpse the power of the complex internal statistical
24. Some of the earliest work depicting perception and per- relationshipsenshrinedinhumanlanguagesinLandauerandcol-
ceptualillusionsasinvolvingBayesian inferenceis thatof Hans- leagues’fascinatingworkon“latentsemanticanalysis”(Landauer
Georg Geissler, working in the 1970s in East Germany. This &Dumais1997;Landaueretal.1998).Thisworkrevealsthevast
work, unfortunately, was not widely known outside the DDR amountofinformationnowembodiedinstatistical(butdeep,not
(DeutscheDemokratischeRepublik)butsee,forexample,Geiss- firstorder)relationsbetweenwordsandthelargercontexts(sen-
ler(1983;1991). tences and texts) in which they occur. The symbolic world we
25. I here adapt, merely for brevity of exposition, a similar humansnowimmerseourselvesinisdemonstrablychock-fullof
examplefromFriston(2002,p.237). information about meaning-relations in itself, even before we
26. Technically,thereisalwaysasinglehierarchicalgenerative (orourbrains)attempttohookanyofittopracticalactionsand
model in play. In speaking here of multiple internal models, I thesensoryworld.
mean only to flag that the hierarchical structure supports many 34. For example, Stanislas Dehaene’s (2009) “neural re-
levelsofprocessingwhichdistributethecognitivelaborbybuild- cycling”accountofthecomplexinterplaybetweenneuralprecur-
ingdistinct“knowledgestructures”thatspecializeindealingwith sors, cultural developments, and neural effects within the key
differentfeaturesandproperties(soastopredicteventsandregu- cognitivedomainsofreadingandwriting.
laritiesobtainingatdifferingtemporalandspatialscales). 35. Such hyperpriors could, for example, be “built-in” by
27. Theclearlineagehereiswithworkinconnectionismand “winner-takes-all” forms of lateral (within layer) cortical inhi-
recurrent artificial neural networks (see, e.g., Rumelhart et al. bition–seeHohwyetal.(2008,p.691).
1986, and early discussions such as Churchland 1989; Clark 36. AshelpfullypointedoutbyoneoftheBBSreferees.
1989). What is most exciting about the new proposals, it seems 37. Theintroductionofhyperpriorsintotheseaccountsisjust
to me, is that they retain many of the insights from this lineage aconvenientwayofgesturingattheincreasinglevelsofabstrac-
(which goes on to embrace work on Helmholz machines and tion at which prior expectations may be pitched. Some expec-
ongoing work on “deep architectures”– see sect. 1.1) while tations, for example, may concern the reliability or shape of the
making explicit contact with both Bayesian theorizing and con- space of expectations itself. In that sense, hyperpriors, although
temporaryneuroscientificresearchandconjecture. they can sound quite exotic, are in no way ad hoc additions to
28. Sucheffectshavelongbeenknownintheliterature,where the account. Rather, they are just priors in good standing (but
they emerged in work on sensory habituation, and most promi- maintaining the distinction makes it a bit easier to express and
nently in Eugene Sokolov’s pioneering studies of the orienting compute some things). Like all priors, they then impact system
reflex. Sokolov concluded that the nervous system must learn dynamicsinvariousways,accordingtotheirspecificcontents.
anddeploya“neuronalmodel”thatisconstantlymatchedtothe 38. This worry (concerning the appeal to hyperpriors) was
incoming stimulus, since even a reduction in the magnitude of first drawn to my attention by Mark Sprevak (personal
some habituated stimulus could engage “dishabituation” and communication).
prompt a renewed response. See Sokolov (1960). See also 39. Amuchbetterunderstandingofsuchmultipleinteracting
Bindra(1959),Pribram(1980),andSachs(1967).Hereandelse- mechanisms (various slow neuromodulators perhaps acting in
whereIamextremelygratefultooneoftheBBSreferees,whose complex concert with neural synchronization) is now needed,
extensive knowledge of the history of these ideas has greatly along with a thorough examination of the various ways and
enrichedthepresenttreatment. levelsatwhichtheflowofpredictionandthemodulatingeffects
BEHAVIORALANDBRAINSCIENCES(2013)36:3 203
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
oftheweightingofpredictionerror(precision)maybemanifest 50. Theempiricalbetisthus,asEgnerandcolleaguesrecently
(for some early forays, see Corlett et al. 2010; see also Friston putit,that“theencodingofpredictions(basedoninternalforward
& Kiebel 2009). Understanding more about the ways and levels models)andpredictionerrorsmaybeaubiquitousfeatureofcog-
atwhichtheflowandimpactofpredictionerrormaybemanipu- nitioninthebrain…ratherthanacuriosityofrewardlearning…
latedisvitallyimportantifwearetoachieveabetterunderstand- ormotorplanning”(Egneretal.2010,p.16607).
ingofthemultiplewaysinwhich“attention”(hereunderstood– 51. When brought under the even-more-encompassing
seesect.2.3–asvariouswaysofmodifyingthegainonprediction umbrellaofthe“freeenergyprinciple”(sect.1.6),thecombined
error)mayoperatesoastobiasprocessingbyflexiblycontrolling ambition is formidable. If these accounts were indeed to mesh
thebalancebetweentop-downandbottom-upinfluence. in the way Friston (2010) suggests, that would reveal the very
40. There are probably milder versions of this everywhere, deepestoflinksbetweenlifeandmind,confirmingandextending
both in science (Maher 1988) and in everyday life. We tend to theperspectiveknownas“enactivist”cognitivescience(see,e.g.,
see what we expect, and we use that to confirm the model that DiPaolo2009;Thompson2007;Varelaetal.1991).
is both generating our expectations and sculpting and filtering
ourobservations.
41. Intriguingly,theauthorsarealsoabletoapplythemodelto
onenon-pharmacologicalintervention:sensorydeprivation.
42. This need not imply an ability deliberately to engage in
Open Peer Commentary
such a process of self-generation. Suchrich, deliberate forms of
imagining may well require additional resources, such as the
language-driven forms of cognitive “self-stimulation” described
inDennett(1991),Chapter8.
43. Itisperhapsworthremarkingthat,deepdualitynotwith-
standing, nothing in the present view requires that the system,
The problem with brain GUTs: Conflation of
when engaged in imagery-based processing, will typically
support the very same kinds of stability and richness of experi- different senses of “prediction” threatens
enced detail that daily sensory engagements offer. In the metaphysical disaster
absence of the driving sensory signal, no stable ongoing infor-
mation about low-level perceptual details is there to constrain doi:10.1017/S0140525X1200221X
theprocessing.Asaresult,thereisnoobviouspressuretomain-
tainorperhapseventogenerate(seeReddyetal.2010)astable MichaelL.AndersonaandTonyChemeroa,b
hypothesisatthelowerlevels:thereissimplywhatevertask-deter- aDepartmentofPsychology,Franklin&MarshallCollege,Lancaster,PA
mineddownwardpressuretheactivehigher-levelencodingexerts. 17604-3003;bDepartmentsofPhilosophyandPsychology,Universityof
44. Common features include the appeal to forward models Cincinnati,Cincinnati,OH45221.
and the provision of mechanisms (such as Kalman filtering–see michael.anderson@fandm.edu http://www.agcognition.org
Friston 2002; Grush 2004; Rao & Ballard 1999) for estimating tony.chemero@fandm.edu http://edisk.fandm.edu/tony.chemero
uncertainty and (thus) flexibly balancing the influence of prior
expectations and driving sensory inputs. Indeed, Grush (2004, Abstract:Clarkappearstobemovingtowardepistemicinternalism,which
heoncerightlyrejected.Thisresultsfromadoubleover-interpretationof
p. 393) cites the seminal predictive coding work by Rao and
predictivecoding’ssignificance.First,Clarkarguesthatpredictivecoding
Ballard (1999) as an account of visual processing compatible offersaGrandUnifiedTheory(GUT)ofbrainfunction.Second,heover-
with the broader emulator framework. In addition, Grush’s readsitsepistemicimport,perhapsevenconflatingcausalandepistemic
accountofperceptionas“environmentalemulation”(seesection
mediators.Weargueinsteadforapluralityofneurofunctionalprinciples.
5.2 of Grush 2004) looks highly congruent with the depiction
(Friston 2003 and elsewhere) of perception as reconstructing Thepredictivecodingmodelofbrainfunctionisadeeplyimpor-
the hidden causes structuring the sensory signal. Where the tant development for neuroscience, and Andy Clark does the
accounts seem to differ is in the emphasis placed on prediction field a service with this careful, thorough, and accessible
error as (essentially) a replacement for the sensory signal itself, review. We are concerned, however, that Clark’s account of
the prominence of a strong Bayesian interpretation (using the the broad implications of model–and in particular his attempt
resourcesof“empiricalBayes”appliedacrossahierarchyofpro- toturnitintoaGrandUnifiedTheory(GUT)ofbrainfunction–
cessing stages), and the attempted replacement of motor com- may be at least four dogmas of empiricism out-of-date (Ander-
mands by top-down proprioceptive predictions alone (for a nice son 2006; Chemero 2009; Davidson 1974; Quine 1951). Clark’s
treatment of this rather challenging speculation, see Friston adoption of a thoroughgoing inferential model of perception,
2011a). It would be interesting (although beyond the scope of his neo-neo-Kantian view of the relationship between mind
thepresenttreatment)toattemptamoredetailedcomparison. and world, and his insistence that every sensory modality oper-
45. An account of such transformed uses might be possible ates according to the same underlying causal-epistemic logic–
within the action-oriented predictive coding framework. The all (individually and severally) threaten to return us to the bad
key to such an account would, I conjecture, be to consider the old days of epistemic internalism (e.g., Rorty 1979) that the
potential of the substituting technologies to deliver patterns of field, including the author of Being There (Clark 1997), rightly
sensorystimulationthatturnouttobebestpredictedbytheuse left behind.
of the very same intermediate-level generative models that HerewesuggestthatClark(althoughnothealone)hasmadean
characterizethesubstitutedmodality.SeealsoPrinz(2005). errorinconflatingdifferentsensesof“prediction”thatoughttobe
46. Thanks to Susanna Siegel for useful discussion of this kept separate. The first sense of “prediction” (henceforth
point. prediction ) is closely allied with the notion of correlation, as
1
47. Forsomefurtherdiscussion,seeFriston(2005,p.822). whenwecommonlysaythatthevalueofonevariable“predicts”
48. This way of describing things was suggested by my col- another (height predicts weight; education predicts income;
leagueMattNudds(personalcommunication). etc.).Prediction isessentiallymodel-free,anditcomesdownto
1
49. For the general story about combining specialization and simplerelationshipsbetweennumbers.Thesecondsenseof“pre-
integration, see Friston (2002) and discussion in Hohwy (2007). diction”(prediction ),incontrast,isalliedinsteadwithabductive
2
Foramorerecentaccount,includingsomeexperimentalevidence inferenceandhypothesistesting.Prediction involvessuchcogni-
2
concerning the possible role of prediction error in modulating tivelysophisticatedmovesasinferringthe(hidden)causesofour
inter-areacoupling,seedenOudenetal.(2010). currentobservations,andusingthathypothesistopredictfuture
204 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
observations,bothaswepassivelymonitorandactivelyintervene if the world that we experience and think about is a projection
intheworld.Itistheoryladenandmodel-rich. of our minds. Western philosophy has been down this lonely
We have no trouble believing that a fundamental part of our and unproductive road many times. It would be a shame if the
exquisite attunement to environmental contingencies involves spotlight that Clark helpfully shines on this innovative work in
sensitivity to (and the ability to make use of) inter- and cross- neuroscienceweretoleadusbackthere.
modalcorrelationsinsensorysignals.Sensitivitytotemporaland
spatial (e.g., across the retina) correlations could underwrite
manyfunctionaladvantages,includingtheonesClarkhighlights,
such as reducing sensory bandwidth and drawing attention to
salient departures from expectations. In this sense we share Attention and perceptual adaptation
Clark’s belief that predictive coding is likely to be a ubiquitous
1
and fundamental principle of brain operation; neural nets are doi:10.1017/S0140525X12002245
especiallygoodatcomputingcorrelations.
However, we don’t think that evidence for predictive coding
NedBlockaandSusannaSiegelb
1
warrants a belief in predictive coding. And it is only from aDepartmentofPhilosophy,NewYorkUniversity,NewYork,NY10003;
2
predictive codingthatmanyofClark’slargerimplicationsfollow. bDepartmentofPhilosophy,HarvardUniversity,Cambridge,MA02138.
2
Clark makes the move from predictive coding to predictive ned.block@nyu.edu ssiegel@fas.harvard.edu
1 2
coding largely by relying on an innovative account of binocular http://www.nyu.edu/gsas/dept/philo/faculty/block/
rivalryofferedbyHohwyetal.(2008).InClark’ssomewhatsim- http://www.people.fas.harvard.edu/∼ssiegel/
plified version of their proposal, the experienced alternation
Abstract: Clark advertises the predictive coding (PC) framework as
between seeing the face stimulus presented to one eye and the
applyingto a widerange of phenomena, includingattention.We argue
house stimulus presented to the other is explained by a knowl-
that for many attentional phenomena, the predictive coding picture
edge-drivenalternationbetweenrivalhypotheses(faceatlocation
eithermakesfalsepredictions,orelseitoffersnodistinctiveexplanation
x,houseatlocationx)neitherofwhichcanaccountforallofthe ofthosephenomena,therebyreducingitsexplanatorypower.
observations.AccordingtoClark,thereasontheimagesdon’tfuse
andleadtoavisualsteady-stateisbecauseweknowthatfacesand According to the predictive coding view, at every level of the
housescan’tcoexistthatway.Ifthisknowledge-drivenaccountis visual/corticalhierarchy,therearetwokindsofunits:errorunits
thecorrectwaytounderstandsomethingasperceptuallybasicas and representation units. Representations propagate downward
binocularrivalry,thenpredictive codingcanbegintolooklikea in the visual hierarchy whereas error signals propagate upward.
2
plausible, multilevel and unifying explanation of perception, Errorinthissensemightbebettercalled“discrepancy,”sinceit
actionandcognition:perceptioniscognitiveandinferential;infer- is the discrepancy betweenwhat the visual systempredicts (at a
enceperceptual;andallofitisactive. givenlevel)andwhatisrepresentedatthatlevel.Clarkadvertises
Butwhilethepredictive codingmodelofbinocularrivalrymay thepredictivecoding(PC)frameworkasapplyingtoawiderange
2
beconsistentwithmuchofthedata,itisfarfromtheonlypossible ofphenomena,includingattention,whichClarksays“isachieved
explanationofthephenomenon.Hereisanoutlineofareasonable byalteringthegain(the‘volume,’touseacommonanalogy)on
predictive coding account: Given the generally high-level of theerror-units”(sect.2.3,para.6).Wearguethatformanyatten-
1
cross-correlation in the inputs of our two eyes, the left eye tional phenomena, the predictive coding picture either makes
signal wouldpredict greater correlationwith the righteye than false predictions, or else it offers no distinctive explanation of
1
iscurrentlyinevidence;thiswouldweakentheinputsassociated thosephenomena,therebyreducingitsexplanatorypower.
withthelefteye,unmaskingtheinputsassociatedwiththeright Considerabasicresultinthisarea(Carrascoetal.2004),which
eye, which would predict cross-correlated left eye signals . . . is that attention increases perceived contrast by enhancing “the
1
and so on. However far this particular proposal could be taken, representationofastimulusinamannerakintoboostingitsphys-
the point is one can account for the phenomenon with low- ical contrast” (Ling & Carrasco 2006, p. 1243). A cross-modal
level, knowledge-free, redundancy-reducing inhibitory inter- study using auditory attention-attractors (Störmer et al. 2009)
actions between the eyes (see, e.g., Tong et al. 2006). After all, showedthatthecontrast-boostingeffectcorrelatedwithincreased
binocularrivalryalsooccurswithorthogonaldiffractiongratings, activity in early stages of visual processing that are sensitive to
indicating that high-level knowledge of what is visually possible differences in contrast among stimuli. The larger the cortical
needn’t be the driver of the visual oscillation; humans don’t effect,thelargertheeffectonperceivers’judgments.Increasing
havehigh-levelknowledgeabouttheinconsistencyoforthogonal thecontrastofastimulushasaneffectonthemagnitudeofper-
gratings.Ingeneral,althoughnoteverypairofstimuliinducebis- ceptualadaptationtothatstimulus,causinggreaterthresholdacti-
tableperceptions,thedistinctionbetweenthosethatdoandthose vationin thetiltafter-effectand longerrecoverytime.Lingand
thatdon’tappearstohavelittletodowithknowledge(seeBlake Carrasco(2006)showedthatattendingtoastimuluswhileadapt-
[2001] for a review). Adopting a predictive coding account is a ingtothatstimulushasthesameeffectasincreasingthecontrast
2
theoretical choice not necessitated by the evidence. It is hardly oftheadaptingstimulus.Afterattendingtotheadaptor(70%con-
aninconsequentialchoice. trast),thecontrastsensitivityofallobserverswasequivalenttothe
Usingpredictive codingasaGUTofbrainfunction,asClark effectofadaptingtoa81–84%contrastadaptor.
2
proposes,isproblematicforseveralreasons.Thefirstproblemis HowdotheseresultslookfromaPCperspective?Supposethat
with the very idea of a grand unified theory of brain function. attimet ,theperceiverisnotattendingtotheleftsideofspace
1
There is every reason to think that there can be no grand butnonethelessseesastripedgridontheleftwithapparentcon-
unifiedtheoryofbrainfunctionbecausethereiseveryreasonto trastof70%.Becausethereisnomovementorotherchange,at
think that an organ as complex as the brain functions according timet ,thevisualsystempredictsthatthepatchwillcontinueat
2
to diverse principles. It is easy to imagine knowledge-rich 70%. But at t the perceiver attends to the patch, raising the
2
predictive codingprocessesemployedingeneratingexpectations apparentcontrastto,say,82%.Nowatt thereisanerror,adis-
2 2
thatwewillconfrontajarofmustarduponopeningtherefriger- crepancybetweenwhatispredictedandwhatis“observed.”Since
atordoor,whileknowledge-freepredictive codingprocesseswill thePCviewsaysattentionisturningupthevolumeontheerror
1
be used to alleviate the redundancy of sensory information. We representations, it predicts that at t the signal (the represented
3
should be skeptical of any GUT of brain function. There is also contrast) should rise even higher than 82%. But that does
a problem more specific to predictive coding as a brain GUT. nothappen.
2
Taking all of our experience and cognition to be the result of Therearetwoimportantlessons.First,theinitialchangesdue
high-level, knowledge-rich predictive coding makes it seem as toattendingcomebeforethereisanerror(att intheexample),
2 2
BEHAVIORALANDBRAINSCIENCES(2013)36:3 205
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Figure1(Block&Siegel). Adisplayofoneofthetexturedfigures(thesquareontheright)usedbyYeshurunandCarrasco(1998).The
square appeared at varying degrees of eccentricity. With low resolution in peripheral locations, attention improved detection of the
square;butwithhighresolutionincentrallocations,attentionimpaireddetection.
so the PC viewpoint cannot explain them. Second, the PC view pattern as occupying a larger area. Here too, predictive coding
makes the false prediction that the changes due to attending offersnodistinctiveexplanation.
willbemagnified. The facts of attention and adaptation do not fit well with the
SometimesPCtheoristsassumetheerrorsignalisequaltothe predictive coding view or any picture based on how “sensory
input.Perhapsthisidentificationmakessomesenseifthepercei- neuronsshouldbehave”(Lochmannetal.2012)ratherthanthe
ver’s visual system has no “expectations,” say because the eyes facts of how they do behave. Without a distinctive explanation
have just opened. But once the eyes have opened and things in of these facts,the explanatory promises of predictivecoding are
the environment are seen, it makes no sense to take the error overdrawn.
signaltobethesensoryinput.
ThePCpicturealsoseemsto lackadistinctiveexplanationof
why attention increases spatial acuity. Yeshurun and Carrasco
(1998)showedthatincreasedattentioncanbedetrimentaltoper- Attention is more than prediction precision
formancewhenresolutionwasalreadyontheborderoftoohigh
forthescaleof thetexture,increasingacuitytothepointwhere doi:10.1017/S0140525X12002324
thesubjectdoesnotseetheforestforthetrees.Toolittleatten-
tioncanalsobedetrimental,makingithardertoseethetrees.Yes- HowardBowman,aMarcoFiletti,aBradWyble,band
hurunandCarrascovariedresolutionofperceptionbypresenting ChristianOliversc
texturedsquares(suchastheoneinFig.1)atdifferenteccentri- aCentreforCognitiveNeuroscienceandCognitiveSystems,andtheSchoolof
cities (the more foveal, the better the resolution). But they also Computing,UniversityofKentatCanterbury,KentCT27NF,UnitedKingdom;
varied resolution by manipulating the focus of spatial attention: bDepartmentofPsychology,SyracuseUniversity,Syracuse,NY13244;
With the eyes focused at the center, they attracted attention to cDepartmentofCognitivePsychology,FacultyofPsychologyandEducation,
the left or to the right. Combining contributions to resolution VUUniversityAmsterdam,1081BTAmsterdam,TheNetherlands.
from eccentricity and attention, they found that there was an H.Bowman@kent.ac.uk M.Filetti@kent.ac.uk
optimallevelofresolutionfordetectingthesquare,withdetection bwyble@gmail.com c.n.l.olivers@vu.nl
falling off on both ends. Single cell recordings in monkey visual http://www.cs.kent.ac.uk/people/staff/hb5/
cortex reveal shrinking receptive fields (the area of space that a http://www.cs.kent.ac.uk/people/rpg/mf266/
neuron responds to) in mid-to-high level vision, specifically in www.bradwyble.com http://olivers.cogpsy.nl
V4,MT,andLIP,andthisshrinkageinreceptivefieldsisacontri-
butortoexplainingtheincreaseinacuity(Carrasco2011). Abstract:Acornerstoneofthetargetarticleisthat,inapredictivecoding
framework,attentioncanbemodelledbyweightingpredictionerrorwitha
DoesthePCframeworkhaveadistinctiveexplanationofatten-
measureofprecision.Wearguethatthisisnotacompleteexplanation,
tionaleffectsonspatialacuity,intermsof“gaininerror-units”?If,
especially in the light of ERP (event-related potentials) data showing
duetothelevelofacuity,onedoesnotseethesquare,thenthe
large evoked responses for frequently presented target stimuli, which
predictionofnosquarewillbeconfirmed,andtherewillbenodis-
thusarepredicted.
crepancy(“error”)tobemagnified.Sincethegaininerrorunitsis
theonlydistinctiveresourceofthePCviewforexplainingatten- ThetargetarticlebyAndyClarkchampionspredictivecodingas
tional phenomena, the view seems to have no distinctive expla- a theory of brain function. Perception is the domain in which
nation of this result either. Can the predictive coding point of many of the strongest claims for predictive coding have been
view simply borrow Carrasco’s explanation? That explanation is made, and we focus on that faculty. It is important to note
a matter of shrinkage in receptive fields of neurons in the rep- that there are other unifying explanations of perception, one
resentation nodes, not anything to do with prediction error, so beingthatthebrainisasaliencedetector,withsaliencereferring
the predictive coding point of view would have to concede that broadlytorelevancetoanorganism’sgoals.Thesegoalsreflecta
attention can act directly on representation nodes without a short-termtaskset(e.g.,searchingacrowdforafriend’sface),or
detourthrougherrornodes. moreingrained,perhapsinnatemotivations(e.g.,avoidingphys-
Finally, attention to certain items–for example, random dot icalthreat).Aprominentperspectiveis,exactly,thatoneroleof
patterns–makes them appear larger. Anton-Erxleben et al. attention is to locate and direct perception towards, salient
(2007) showed that the size of the effect is inversely related to stimuli.
thesizeofthestimulus,explainingtheresultintermsofreceptive The target article emphasises the importance of evoked
fieldshift(suchshiftsarealsoobservedfromsinglecellrecordings responses, particularly EEG event-related potentials (ERPs), in
inmonkeyvisualareas;Womelsdorfetal.2006).Thisexplanation adjudicating between theories of perception. The core idea is
depends on the retinotopic and therefore roughly spatiotopic thatthelargerthedifferencebetweenanincomingstimulusand
organization common to many visual areas–not on error units. the prediction, the larger the prediction error and thus the
Neurons whose receptive fields lie on the periphery of the larger the evoked response. There are indeed ERPs that are
pattern shift their receptive fields so as to include the pattern, clearlymodulatedbypredictionerror,forexample,theMismatch
moving the portion of the spatiotopically represented space to Negativity(evokedbydeviationfromarepeatingpatternofstimu-
include the pattern, resulting in the representation of the luspresentation),theN400(evokedbysemanticanomalies),and
206 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
P3 responses to oddball stimuli. In addition, stimuli that violate obtain classically predictive or anti-predictive (i.e., salience
our expectations do often capture attention (Horstmann 2002), sensitive) patterns, and both patterns are found experimentally.
consistent with predictive coding. However, such surprise- Thus, the theory really requires a computational explanation of
driven orienting is justone aspect of attention, and we question howthemodulatoryeffectofprecisionvariesacrossexperimental
whether prediction error provides an adequate explanation for contexts, otherwise there is a risk that it becomes effectively
attentionalfunctioningasawhole. unfalsifiable.
A central aspect of attention, which makes perception highly Second,predictionerrorispassedbackupthesensorypathway
adaptive, is that it can purposefully select and enhance expected so that parameters can be adjusted to improve predictions (i.e.,
stimuli. This arises when an arrow cues where a target will learning), and the amount parameters change is a function of
appear,oraverbalinstructionindicatesitwillbered.However, the size of the precision-weighted prediction error. This,
in this context, ERPs are largest to the target stimuli (P1, N1, however, raisesafurther problemwitha big precision-weighted
N2pc,P3;Luck2006),inlinewithasaliencyaccount.Suchheigh- predictionerrorbeinggeneratedthroughalarge(attention-gov-
tenedresponsestopredictedstimulidonotseemtositcomforta- erned) precision, when observed and predicted are similar.
blywithpredictivecoding.AsClarkhighlights,resolutionofthis Specifically, in this case, the parameters should not change and
conundrum has, in analogy with statistical tests, focused on pre- certainly not a lot, even though precision-weighted prediction
cision (Feldman & Friston 2010). The two-sample t-test, say, is errormightmandateit.
aratioofthedifferenceoftwomeans,andvariabilityintheesti- Third, directing attention, and thus improving precision, at a
mate of that difference. Precision-weighted prediction error is pre-determined location is one thing. But what makes attention
such a test: The difference between prediction and observation soadaptiveisthatitcanguidetowardsanobjectatanunpredict-
is weighted by the precision or confidence in that difference– able location–simply on the basis of features. For example, we
that is, the inverse of variability, or, in other words, the signal could ask the reader to find the nearest word printed in bold.
fedbackupthesensorypathway,theevokedresponse,isapre- Attention will typically shift to one of the headers, and indeed
cision-weighted prediction error. Importantly, attention is pro- momentarily increase precision there, improving reading. But
posed to increase precision; that is, the brain has greater this makes precision weighting a consequence of attending. At
confidence in its estimate of disparity between predicted and leastasinterestingisthemechanismenablingstimulusselection
observed when that observation is being spot-lit by attention, inthefirstplace.Thebrainhastofirstdeployattentionbeforea
and,indeed,perceptiondoesseemmoreaccurateinthepresence precisionadvantagecanberealisedforthatdeployment.Salience
of attention (Chennu et al. 2009). This then enables predictive theory proposes that stimuli carrying a target feature become
coding to generate big bottom-up responses to expected, in the more salient and thus draw attention. But which predictive
sense of attended stimuli, as simulated for spatial attention in coding mechanism is sensitive to the match between a stimulus
(Feldman2010). featureandthetargetdescription?Intypicalvisualsearchexper-
Although predictive coding is an elegant and intriguing iments,observersarelookingfor,andfinding,thesametargetin
approach,obstaclesremaintoits beingfullyreconciledwith the trialaftertrial.Forexample,inourrapidserialvisualpresentation
saliency perspective. First, precision-weighting has a multiplica- experiments,eachspecificdistractorappearsveryrarely(onceor
tiveeffect.Hence,therehastobeadifferencebetweenobserved twice), while pre-described targets appear very frequently. We
and predicted in the first place for precision to work on. If obtained effectively no evoked response for distractors but a
observedisexactlyasexpected,howeverbigprecisionmightbe, largedeflectionforthetarget(seeFig.1).Itseemsthatpredictive
the precision-weighted prediction error will be zero. Yet classic coding mandates little if any response for this scenario. If any-
EEG experiments show that attentional enhancement of ERP thing, should the distractors not have generated the greatest
components(e.g.,P1andN1)isgreatestwhentargetsappearin response, since they were (a) rare, and (b) not matching
the same location for many trials (Van Voorhis & Hillyard predictions?
1977). One could of course argue that there is always some Evenifonecoulddeviseapredictivecodingframeworkthatallo-
error,andthattheeffectsofattentiononprecisionareextremely catedahigherprecisiontothetargetrepresentation(whichisastep
largerelativetothaterror.However,dependingupontheextent beyonditsspatialallocationinFeldman2010),itisunclearhowit
to which precision modulates the prediction error, one could could generate a massive precision-weighted prediction error
Figure1(Bowmanetal.). Ananti-predictiveERPpattern.
BEHAVIORALANDBRAINSCIENCES(2013)36:3 207
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
specificallyfortargets,wherepredictedandobservedmatchexactly. 10p.m.wefoundacellwithahuge,verticallyorientedreceptive
Itisalsounclearwhysuchanerrorisneeded. field. Perhaps it was an artifact, the bursting discharges of an
injured cell as the mapping stimulus swept vertically across our
screen.Sowechangedtoahorizontalscan.Thefieldremained,
fivetimesbiggerthananyorientedreceptivefieldeverrecorded
Applications of predictive control in from a cat. Our jaws dropped as we looked at each other, a
momentofdiscovery–thiswasn’tanormalcortex,butsomething
neuroscience
completelydifferent.Itwasthemagicalmomentinsciencewhen
you know something about nature that no one else knows. We
doi:10.1017/S0140525X12002282 coveredoneeye,thentheother;thereceptivefielddisappeared
and reappeared. Later that night we recorded several other
BruceBridgeman
similar fields, all vertical or horizontal, all monocular, and all
DepartmentofPsychology,UniversityofCalifornia–SantaCruz,SantaCruz, huge. It turned out later that the receptive field orientations
CA95064.
matched the mask orientations for the corresponding eye
bruceb@ucsc.edu http://people.ucsc.edu/∼bruceb/
(Hirsch & Spinelli 1970). Plasticity in this cat’s cortex extended
beyondanymereselectionofnormalreceptivefields,beyondany-
Abstract:Thesensorycortexhasbeeninterpretedascodinginformation
ratherthanstimuluspropertiessinceSokolovin1960showedincreased thing that anyone had suspected. The cat had reorganized its
responsetoanunexpectedstimulusdecrement.Themotorcortexisalso cortex from visual experience alone. Clearly the cortex, by the
organizedaroundexpectation,codingthegoalofanactratherthanaset structureofitsreceptivefields,waspredictingfutureinput.
ofmusclemovements.Expectationdrivesnotonlyimmediateresponses Thiswouldbeaninterestingcuriosityifnotforitsunder-appreci-
but also the very structure of the cortex, as demonstrated by atedimplicationthatthesameprocessmustbeoccurringinnormal
development of receptive fields that mirror the structure of the visual cats,and,byextension,inhumansaswell.Sensoryreceptivefields
world.
aretunedtothestructureoftheworldthattheanimalencounters
initsearlyexperience.Thereceptivefieldsofnormalanimalshavea
Predictionisapowerfulprincipleinneuroscience,anditisnotanew
1/fstatisticalstructure,asdoesthenaturalworld.
one.Ithasbeencentraltointerpretationofbrainfunctionsincethe
influentialworkofE.N.Sokolov(1960)(seetargetarticle,Note28). Itisevenpossiblethatthedominanceofthefovealprojection
onto V1, a quarter of the entire surface in humans, is a conse-
Hefoundthatcorticalresponsesdependnotontheamplitudeofan
quence of the huge number of projections coming up from the
incomingsignal,butonitsinformationvalue.Anexpectedstimulus
periphery.ThesmallsizeofV1receptivefieldsrepresentingthe
caused hardly a ripple, while an unexpected one triggered what
foveamightoriginatefromthebetteropticsandsmallerconver-
Sokolovtermedanorientingresponse.Thekeyexperimentwasto
gence of the foveal anatomy. The distribution of receptive field
repeatastimulusuntilitscorticalsignalnearlydisappeared(habitu-
ationoftheorientingresponse,orClark’s“repetitionsuppression”).
orientationsandspatialfrequenciesreflectsthepropertiesofthe
normalvisualenvironment(Switkesetal.1978);thecortexispre-
Then Sokolov decreased the stimulus amplitude or its duration.
dictingitsowninputbyitsverystructure.Thisispreciselywhat
Sokolovreasonedthatifthecortexweremerelyechoingstimulus
Clark realizes when he concludes, “dig a little deeper and what
properties the response should have decreased, but instead it
we discover is a model of key aspects of neural functioning that
increased.Withaqualitativechange,noamountoffussingwithnon-
makesstructuringourworldsgenuinelycontinuouswithstructur-
linearitiesandthresholdscouldexplaintheresult.Thecortexwas
ingourbrains”(sect.3.4,para.1).Buttheevidencehasbeenthere
codingnotstimuluspropertiesbutstimulusinformation,thediffer-
allalong.
encebetweensignalandexpectation.Inthiscontextitisnowonder
thatweignoreandfailtoremember mostofthevaststreams of
signals emanating from our millions of sensory receptors. So
Clark’spredictionthesishasbeenthedominantinterpretationof
corticalsensorycodingformorethanahalf-century. When the predictive brain gets it really wrong
Another insight that shaped neuroscience is that the brain is
not about representing the stimulus; it is about organizing doi:10.1017/S0140525X12002233
action. The evidence begins with an anatomical paradox that
the precentral “motor” cortex is innervated by the dorsal thala- GavinBuckinghamandMelvynA.Goodale
mus, a region homologous to the dorsal spinal cord that pro- TheBrainandMindInstitute,NaturalSciencesCentre,TheUniversityof
cesses sensory information (Pribram 1971, p. 241). Pribram WesternOntario,LondonONN6A5B7,Canada.
askswhythemotorcortexshouldbecloselytiedtoanotherwise gbucking@uwo.ca mgoodale@uwo.ca
sensorystructure.Hisansweristhat themotorcortexisreallya http://publish.uwo.ca/∼gbucking/
sensory cortex for an image of achievement, analogous to the http://psychology.uwo.ca/faculty/goodale/
images in sensory regions and organized similarly. Motor cortex
Abstract:Clarkexaminesthenotionofthe“predictivebrain”asaunifying
codes environmental contingencies, not literal muscle move-
modelforcognitiveneuroscience,fromthelevelofbasicneuralprocesses
ments, and continuously compares progress in execution of an
tosensorimotorcontrol.Althoughweareingeneralagreementwiththis
act with its goal. notion,wefeelthattherearemanydetailsthatstillneedtobefleshed
Similarly,ithaslongbeenknownthatreceptivefieldsinsensory
outfromthestandpointofperceptionandaction.
cortex are shaped not onlyby anatomybut alsoby experience, so
thattheyencodebestwhatispredictedtobepresentintheenviron- Inhistargetarticle,Clarkpaintsadiversepictureofhowpredic-
ment. I was privileged to witness the first evidence that sensory tion is a ubiquitous part of brain and behaviour interactions.
experience could tune the receptive field properties of the Taking heavy cues from Friston’s “free energy principle,” his
primaryvisualcortex(V1).HelmutHirsch,thenaStanfordgraduate target article summarises ideas at the neural level, suggesting
student, was studying kittens that he raised wearing masks that that the critical variable for sensory coding and motor control is
exposed one eye to vertical stripes and the other to horizontal the deviation from the expected signal, rather than the sensory
stripes. Together with Nico Spinelli and Robert Phelps we began ormotorprocessingperse.Inthefieldofsensorimotorcontrol,
recordingfromsinglecellsinV1ofthemask-rearedkittens,using this Bayesian approach is a popular one (e.g., Körding &
thefirstautomatedreceptive-fieldmappingapparatus.Weprepared Wolpert 2004). Many researchers have built their careers
ourfirstkittenanddippedourmicroelectrodeintoitscortex. showingthat,inawiderangeofcontexts,anindividual’smotorbe-
Thefirstcellswerecordedhadlarge,poorlydefinedreceptive haviour can be modeled as the approximately optimal combi-
fieldsofthesorttoexpectinavisuallydeprivedcat.Thenaround nationofthe“undiluted”sensoryinputandthepriorprobability
208 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
ofthatsensoryeventoccurring,thusbiasingtheresponseoneway thatthenexttimeafreshbottleofwaterisgrasped,thesensori-
or the other. Similarly, a wide range of psychophysical exper- motor prediction will have a good chance of being accurate).
iments have demonstrated that our conscious perception of Thus, when lifting SWI-inducing cubes for the first time, lifters
events in the world represents not veridical sensory input, but will apply excess force to the large cube and apply insufficient
theintegrationofmultiplesourcesofevidencefromoursensory force to the small cube the first time they lift them, but will lift
system and our prior experience, rather than the veridical (and thesetwoidentically-weightedcubeswithappropriatelyidentical
noisy)sensoryinputitself(Gregory1998).Anespeciallycompel- forcesafteronlyafewexperienceswiththem(Flanagan&Beltz-
ling case for this Bayesian standpoint can be made from the ner2000).Clearly,thisadaptivebehaviourisaconsequenceofa
study of perceptual illusions, and several classic visual illusions complex interaction between short-term and long-term priors
can be explained with this optimal integration strategy (Geisler (Flanagan et al. 2008)–a process that looks far more like the
& Kersten 2002; Weiss et al. 2002). In these contexts, this inte- BayesianprocessesoutlinedbyClarkinhistargetarticle(Braya-
gration is thought to overcome the noise in the system of our nov&Smith2010).Itistemptingtoascribeacausalrelationship
sensory organs, maximising the likelihood of perceptual or between the force errors and the perceptual ones. Remarkably,
motor“success.” however,thetwokindsoferrorsappeartobecompletelyisolated
Despitetheapparentdescriptivepowerofoptimallycombining from one another: The magnitude of the SWI remains constant
sensory prediction with sensory input, there are common situ- from one trial to the next, even in the face of the rapid trial-to-
ationswhereconsciousperceptionisclearlynotaproductofBaye- trialadaptationofthegrippingandliftingforces.Thiscomplicates
sian-styleoptimalintegration.Infact,whenweliftanobjectand thesituationevenfurtherbysuggestingthattheremustbeinde-
experience its weight, our conscious perception of how heavy it pendentsetsofpriorsformotorcontrolandperceptual/cognitive
feelsisalmostexactlytheoppositeofwhatmightbeexpectedif judgements,whichultimatelyservequitedifferentfunctions.
a perceiver integrates perpetual priors with sensory input. This In conclusion, we have outlined how the deceptively simple
incongruence is easily demonstrated with the famous size– SWIparadigmcanuncovertheoperationofmultiplepriorsoper-
weight illusion(SWI),firstdescribedin 1891byAugustinChar- ating simultaneously, with different weightings and different
pentier (translation by Murray et al. 1999). The SWI occurs goals. It is worth noting, however, that while the predictive
when small and large objects, that otherwise look similar to one brainmakessenseinapost-hocway,providingacomputationally
another,areadjustedtohaveidenticalweights.Whenindividuals plausible parameter for both the perceptual and lifting effects
lifttheseobjects,thesmallonefeelssubstantiallyheavierthanthe (Brayanov&Smith2010),itisstillverymuchablack-boxexpla-
(equally-weighted) larger one–an effect that is persistent and nation–and, to date, the term “prior” seems to serve only as a
apparentlycognitivelyimpenetrable.Themechanismthatunder- convenient placeholder in lieu of any tangible mechanism
pinsthisillusionisstillsomethingofamystery.Ithaslongbeen linking expectations to the perceptual or motor effects they
contended (in a rather vague way) that the illusion is caused by appeartoentail.
the violation of an individual’s expectations about how heavy
each object will be–namely, the expectation that the large
objectswilloutweighthesmallobjects(Ross1969).Itisnotdiffi-
culttoimaginehowthispriorisbuiltup,giventheconsistencyof
Expecting ourselves to expect: The Bayesian
therelationshipbetweensizeandweightoutsideofthelaboratory
brain as a projector
setting. It is repeatedly encountering this positive size/weight
relationship throughout our entire lives that presumably serves
toestablishaverypowerfulpriorforourperceptionsofheaviness doi:10.1017/S0140525X12002208
(Flanagan et al. 2008). Crucially, however, this prior is not inte-
grated into the lifter’s percept of how heavy the objects feel, as DanielC.Dennett
onemightpredictfromaBayesianoptimalintegrationstandpoint. CenterforCognitiveStudies,TuftsUniversity,Medford,MA02155.
Instead, the lifter’s conscious perception of heaviness contrasts ddennett@tufts.edu
thepriorexpectation,leadingsomeauthorstolabeltheeffectas ase.tufts.edu/cogstud/incbios/dennettd/dennettd.htm
“anti-Bayesian” (Brayanov & Smith 2010). Variants of the SWI
Abstract:Clark’sessaylaysthefoundationforaBayesianaccountofthe
can even manifest in a single, unchanging, object, which can be
“projection” of consciously perceived properties: The expectations that
madetofeeldifferentweightsbysimplymanipulatinganindivid-
our brains test against inputs concern the particular affordances that
ual’s expectations of what they are about to lift (Buckingham &
evolutionhasdesignedustocareabout,includingespeciallyexpectations
Goodale2010). ofourownexpectations.
The functional significance of this contrastive effect has been
the source of great (and largely unresolved) debate–why would The“Bayesian”brainasa“hierarchicalpredictionmachine”isan
ourperceptualsystembesostrickenwitherrors?Extendingthe enticing new perspective on old problems, for all the reasons
conclusions of a recent study by Baugh and colleagues (Baugh Clark articulates, ranging over fields as disparate as neuroanat-
etal.2012),itcouldbeproposedthattheSWIisaproductofa omy, artificial intelligence, psychiatry, and philosophy; but he
perceptual system specialised for the detection and subsequent also catalogues some large questions that need good answers.
flaggingofoutliersinthestatisticsoftheenvironment.Thus,con- Whilewaitingforthedetailstocomein,Iwanttosuggestsome
scious weight perception can be framed as an example of a task other benefits that this perspective promises. If it turns out not
whereitisimportanttoemphasisetheunexpectednatureofthe to be sound, in spite of all the converging evidence Clark
stimuli, in a system which presumably favours more efficient describes,wewillhaveallthemorereasonforregret.
codingofinformation. Itiseverybody’sjob–butparticularlythephilosophers’job–to
Asliftingbehaviourisalargelypredictiveprocess,ourfingertip negotiatethechasmbetweenwhatWilfridSellars(1962)calledthe
forces are driven by our expectations of how heavy something manifestimageandthescientificimage.Themanifestimageisthe
looks.And,inamoreconventionalBayesianfashion,theweight- everydayworldoffolkpsychology,furnishedwithpeopleandtheir
ingofthesepriorsisrapidlyadjusted(orrapidlyignored)bythe experiencesofallthemiddle-sizedthingsthatmatter.Thescienti-
presenceofliftingerrors.Thisprovidesthesensorimotorsystem ficimageistheworldofquarks,atoms,andmolecules,butalso(in
with the best of both worlds–lifting behaviour that is flexible thiscontextparticularly)sub-personalneuralstructureswithpar-
enough to rapidly adapt to constantly changing environments ticular roles to play in guiding a living body safely through life.
(e.g., a bottle of water which is being emptied by a thirsty Thetwoimagesdonotreadilyfallintoregistration,aseverybody
drinker), but will automatically “snap back” to the (generally knows, leaving lots of room for confusion and compensatory
correct) lifting forces when the context of the lift is altered (so adjustment(nicelyexemplifiedbythesurprise/surprisalpair).
BEHAVIORALANDBRAINSCIENCES(2013)36:3 209
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
ConsiderwhatIwillcallHume’sStrangeInversion(cf.Dennett prediction error signals is interpreted as confirmation that,
2009).Oneofthethingsinourworldiscausation,andwethinkwe indeed, the thing in the world we are interacting with has the
seecausationbecausethecausationintheworlddirectlycausesus propertiesweexpectedittohave.Cutenessasapropertypasses
toseeit–thesamewayroundthingsindaylightcauseustosee the Bayesian test for being an objective structural part of the
round things, and tigers in moonlight cause us to see tigers. world we live in, and that is all that needs to happen. Any
When we see the thrown ball causing the window to break, the further “projection” process would be redundant. What is
causationitselfissomehowperceptible“outthere.”Notso,says specialaboutpropertieslikesweetnessandcutenessisthattheir
Hume. This is a special case of the mind’s “great propensity to perception depends on particularities of the nervous systems
spread itself on external objects” (Treatise of Human Nature, thathaveevolvedtomakemuchofthem.Thesameisofcourse
Hume 1739/1888/1964, I, p. xiv). In fact, he insisted, what we alsotrueofcolors.ThisiswhatisleftofLocke’s(andBoyle’s)dis-
doismisinterpretaninner“feeling,”ananticipation,asanexternal tinctionbetweenprimaryandsecondaryqualities.
property.The“customarytransition”inourmindsisthesourceof
oursenseofcausation,aqualityof“perceptions,notofobjects,”
butwemis-attributeittotheobjects,asortofbenignuser-illusion,
tospeakanachronistically.AsHumenotes,“thecontrarynotionis
sorivetedinthemind”(p.167)thatitishardtodislodge.Itsur- Grounding predictive coding models in
vives to this day in the typically unexamined assumption that all empirical neuroscience research
perceptualrepresentationsmustbeflowinginboundfromoutside.
HereareafewotherfolkconvictionsthatneedStrangeInver- doi:10.1017/S0140525X1200218X
sions: sweetness is an “intrinsic” property of sugar and honey,
whichcausesus tolikethem;observed intrinsicsexinessiswhat TobiasEgneraandChristopherSummerfieldb
causes our lust; it was the funniness out there in the joke that aDepartmentofPsychology&Neuroscience,andCenterforCognitive
causedustolaugh(Hurleyetal.2011).Thereisnomorefamiliar Neuroscience,DukeUniversity,Durham,NC27708;bDepartmentof
and appealing verb than “project” to describe this effect, but of ExperimentalPsychology,UniversityofOxford,OxfordOX13UD,United
courseeverybodyknowsitisonlymetaphorical;colorsaren’tlit- Kingdom.
erally projected (as if from a slide projector) out onto the front tobias.egner@duke.edu
surfacesof(colorless)objects,anymorethantheideaofcausation http://sites.google.com/site/egnerlab/
issomehowbeamedoutontothepointofimpactbetweenthebil- christopher.summerfield@psy.ox.ac.uk
liardballs.Ifweusetheshorthandterm“projection”totrytotalk, https://sites.google.com/site/summerfieldlab/home
metaphorically,aboutthemismatchbetweenmanifestandscien-
tificimagehere,whatisthetruelongstory?Whatisliterallygoing Abstract:Clarkmakesaconvincingcaseforthemeritsofconceptualizing
oninthescientificimage?Alargepartoftheansweremerges,I brains as hierarchical prediction machines. This perspective has the
potential to provide an elegant and powerful general theory of brain
propose,fromthepredictivecodingperspective.
function, but it will ultimately stand or fall with evidence from basic
Every organism, whether a bacterium or a member of Homo
neuroscience research. Here, we characterize the status quo of that
sapiens, has a set of things in the world that matter to it and evidenceandhighlightimportantavenuesforfutureinvestigations.
whichit (therefore) needs to discriminate and anticipateas best
it can. Call this the ontology of the organism, or the organism’s Theintuitionthatourbrainsharborapredictive(forward)model
Umwelt(vonUexküll1934/1957).Thisdoesnotyethaveanything linking visual percepts to their probable external causes (Helm-
todowithconsciousnessbutisratheran“engineering”concept, holtz1876)hasbeenfleshedoutoverrecentdecadesbysophisti-
like the ontology of a bank of elevators in a skyscraper: all the catedmodels(Friston2005;Mumford1992;Rao&Ballard1999),
kinds of things and situations the elevators need to distinguish inspiringtheviewthatClarkputsforwardinthetargetarticle,that
and deal with. An animal’s Umwelt consists in the first place of predictive coding is a cardinal principle of neural systems (cf.
affordances (Gibson 1979), things to eat or mate with, openings Friston2010;Hawkins&Blakeslee2004).Whilethisperspective
to walk through or look out of, holes to hide in, things to stand offerselegantpost-hocexplanationsforawidearrayofbehavioral
on, and so forth. We may suppose that the Umwelt of a starfish andneuralphenomena,empiricalstudiesdirectlytestingthebasic
or worm or daisy is more like the ontology of the elevator than biologicalassumptionsofpredictivecodingremainscarce.Specifi-
like our manifest image. What’s the difference? What makes cally, the core empirical hypotheses derived from the predictive
ourmanifestimagemanifest(tous)? coding scheme are the presence of separable and hierarchically
HereiswhereBayesianexpectationscouldplayaniteratedrole: organized visual expectation and surprise computations (and
Ourontology(intheelevatorsense)doesaclose-to-optimaljobof associated neural units/signals) in the posterior brain (Friston
representingthethingsintheworldthatmattertothebehaviorour 2005). These predictions are provocative, because they differ
brains have to control. Hierarchical Bayesian predictions accom- drastically from traditional views of visual neurons as mere
plishthis,generating affordancesgalore:Weexpectsolidobjects bottom-upfeaturedetectors(Hubel&Wiesel1965;Riesenhuber
to have backs that willcome into view as we walkaround them, &Poggio2000).Butwhatistheempiricalevidencedirectlysup-
doors to open, stairs to afford climbing, cups to hold liquid, and portingtheseclaims?Wefirstaddressresultsfrommacroscopic,
soforth.ButamongthethingsinourUmweltthatmattertoour human neuroimaging studies, followed by microscopic data
well-beingareourselves!WeoughttohavegoodBayesianexpec- frominvasiveanimalexperiments.
tations about what we will do next, what we willthink next, and At the macroscopic level of inquiry provided by whole-brain
whatwewillexpectnext!Andwedo.Here’sanexample: functionalneuroimaging,thereareatpresentmodestbutpromis-
Thinkofthecutenessofbabies.Itisnot,ofcourse,an“intrin- ing lines of empirical support for predictive coding’s core prop-
sic”propertyofbabies,thoughitseemstobe.Whatyou“project” ositions.Mostfirmlyestablishedisthefindingofrobustoccipital
outontothebabyisinfactyourmanifoldof“felt”dispositionsto responses evoked by the surprising presence or absence of
cuddle,protect,nurture,kiss,cooover,...thatlittlecutie-pie.It’s visualstimuli,presumablyattributabletothecomputationofpre-
not just that when your cuteness detector (based on facial pro- dictionerror(e.g.,Alinketal.2010;denOudenetal.2009;Egner
portions, etc.) fires, you have urges to nurture and protect; you et al. 2010). Similarly, “repetition suppression,” the attenuated
expecttohavethoseveryurges,andthatmanifoldofexpectations neuralresponsetoarepeatedstimulusthatpredictivecodingattri-
justisthe“projection”ontothebabyofthepropertyofcuteness. butestoadecreaseinpredictionerror(Friston2005),hasrepeat-
Whenweexpecttoseeababyinthecrib,wealsoexpectto“findit edly been shown to be modulated by expectations, including in
cute”–thatis,weexpecttoexpecttofeeltheurgetocuddleitand humanfunctionalmagneticresonanceimaging(fMRI)(Summer-
so forth. When our expectations are fulfilled, the absence of field et al. 2008), electroencephalographic (EEG) (Summerfield
210 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
et al. 2011), and magnetoencephalographic (MEG) (Todorovic hypothesis are few but generally supportive. Looking to the
etal.2011)recordings.However,althoughevidenceforvisualsur- future, additional demonstrations of simultaneous prediction and
prisesignalsattheneuralpopulationlevelisfairlyabundant,the surprisecomputationswithinasingleprocessingstage(inparticular
attributionofthesesignalstolocalpredictionerrorcomputations fromsingle-neuronelectrophysiology),aswellasevidenceforhier-
isnotunequivocal,inthattheycouldinsteadbearguedtoreflect archical interactions with adjacent stages, are required. We hope
attentionalhighlightingofunexpectedstimuli(cf.Pearce&Hall that over coming years, neuroscientists will be inspired to collect
1980)drivenbypredictiveprocessingelsewhereinthebrain.In thesedata.
fact, the precise role that attention plays in the predictive
codingmachineryiscurrentlyunderdebate(Feldman&Friston
2010; Summerfield & Egner 2009) and represents an important
lineofrecent(Koketal.2011;Wyartetal.2012)andfutureinves-
Prediction, explanation, and the role of
tigationsintothepredictivebrainhypothesis.
Incontrasttothissupportfortheexistencevisualsurprisesignals, generative models in language processing
thepropositionthattherearesimultaneouscomputationsofpredic-
tionandpredictionerrorsignalscarriedoutbydistinctneuralpopu- doi:10.1017/S0140525X12002312
lations in visual cortex is presently only poorly substantiated. One
recentfMRIstudyshowedthatneuralpopulationresponsesinthe
ThomasA.Farmer,a,bMeredithBrown,aand
ventralvisualstreamcanbesuccessfullymodeledasreflectingthe MichaelK.Tanenhausa
summedactivityofputativepredictionandpredictionerrorsignals aDepartmentofBrainandCognitiveSciencesandbCenterforLanguage
(Egneretal.2010;Jiangetal.2012).Similarly,arecentcomputational Sciences,UniversityofRochester,Rochester,NY14627-0268.
modelcanaccountforawidearrayofauditoryEEGresponsesby tfarmer@bcs.rochester.edu mbrown@bcs.rochester.edu
supposing co-existing prediction and prediction error neurons mtan@bcs.rochester.edu
(Wacongneetal.2012).However,neitherofthesestudiesdemon-
stratesunambiguouslythesimultaneousoperationofdistinctneural Abstract:Wepropose,followingClark,thatgenerativemodelsalsoplaya
sub-populationscodingforexpectationsandsurprise,afindingthat centralroleintheperceptionandinterpretationoflinguisticsignals.The
dataexplanationapproachprovidesarationalefortheroleofpredictionin
would greatlybolster the biological feasibility of predictive coding language processing and unifies a number of phenomena, including
models.Finally,thepurportedhierarchicalnatureoftheinterplay
multiple-cue integration, adaptation effects, and cortical responses to
between expectation and surprise signals has garnered indirect violationsoflinguisticexpectations.
supportfromahandfuloffMRIstudies.Forinstance,Murrayand
colleaguesdemonstratedthe“explainingaway”ofactivityinlower- Traditional models of language comprehension assume that
level visual regions by activity in higher-level visual cortex when language processing involves recognizing patterns, for example,
presentingacoherentvisualobjectcomparedtoitsdissembledcon- words, by mapping the signal onto existing representations,
stituentparts(Murrayetal.2002).Otherinvestigatorshaveemployed retrieving information associated with these stored represen-
effectiveconnectivityanalysisoffMRIdatatoprobehowdynamic tations, and then using rules based on abstract categories (e.g.,
interactionsbetweendifferentbrainregionsmaymediateprediction syntacticrules)tobuildstructuredrepresentations.Fouraspects
andsurprisesignals(denOudenetal.2009;2010;Koketal.2011; oftheliteratureareinconsistentwiththisframework.First,listen-
Summerfield&Koechlin2008;Summerfieldetal.2006).Neverthe- ersareexquisitelysensitivetofine-grained,sub-categoricalprop-
less,acomprehensivedemonstrationofpredictivecoding“message erties of the signal, making use of this information rather than
passing”acrossseveraladjacentlevelsofthevisualprocessinghierar- discarding it (McMurray et al. 2009). Second, comprehenders
chyremainslackingfromtheliterature. rapidlyintegrateconstraintsatmultiplegrains.Third,theygener-
Perhaps most importantly, microscopic or cellular level data ateexpectationsaboutlikelyinputatmultiplelevelsofrepresen-
addressing the core tenets of the predictive coding hypothesis tation. Finally, adaptation is ubiquitous in language processing.
havebeenparticularlyscarce.Inpart,thismaybeformethodo- These results can be unified if we assume that comprehenders
logicalreasons:Forexample,neuronswithproposed“predictive useinternally generated predictionsat multiplelevels to explain
fields”mightbeexcludedfromrecordingstudieswherecellsare the source of the input, and that prediction error is used to
screened according to their bottom-up sensitivity. Moreover, updatethegenerativemodelsinordertofacilitatemoreaccurate
the dynamics of the reciprocal interaction within the hierarchy predictionsinthefuture.
mightgiverisetocomplexneuralresponses,makingithardtoseg- Extendedtothedomainoflanguageprocessing,Clark’sframe-
regatepredictionanderrorsignals.Nevertheless,recentworkhas workpredictsthatexpectationsathigherlevelsofrepresentation
supplied some promising data. First, Meyer and Olson (2011) (e.g., syntactic expectations) should constrain interpretation at
haverecentlydescribedsingleneuronsinmonkeyinferotemporal lowerlevelsof representation(e.g.,speechperception).Accord-
cortexthatexhibitsurpriseresponsestounexpectedstimulustran- ingtothisview,listenersdevelopfine-grainedprobabilisticexpec-
sitions,thuspossiblydocumentingvisualpredictionerrorneurons tations about how lexical alternatives are likely to be realized in
in the ventral visual stream. Two other recent studies, one in context (e.g., net vs. neck) that propagate from top to bottom
monkeys (Eliades & Wang 2008) and one in mice (Keller et al. throughthelevelsofahierarchicallyorganizedsystemrepresent-
2012), assessed neuronal activity in the context of sensorimotor ingprogressivelymorefine-grainedperceptualinformation.Pro-
feedback (e.g., the integration of movement with predicted visional hypotheses compete to explain the data at each level,
changes in visual stimulation), observing putative prediction with the predicted acoustic realization of each alternative being
errorsignalsinprimarysensorycortices(foralternativeinterpret- evaluated against the actual form of the input, resulting in a
ations, see Eliades & Wang 2008). Importantly, in Keller et al. residual feed-forward error signal propagated up the hierarchy.
(2012),thesesurprisesignalsco-occurredwithbothpuremotor- As the signal unfolds, then, the activation of a particular lexical
relatedandsensory-drivensignals,thusprovidinginitialevidence candidate should be inversely proportional to the joint error
for the possibility of co-habiting prediction and prediction error signalatalllevelsofthehierarchy(i.e.,thedegreeofdivergence
neuronsinearlyvisualcortex.Moreover,theputativeprediction betweenthepredictedacousticrealizationofthatcandidateand
error neurons were found in supra-granular layers 2/3, which theactualincomingsignal),suchthatcandidatewordswhosepre-
house precisely the superficial pyramidal cells that have been dictedrealizationsaremostcongruentwiththeacousticsignalare
posited to support prediction error signaling by theoretical favored.
modelsofpredictivecoding(Friston2008;Mumford1992). Hierarchicalpredictiveprocessingthereforeprovidesapoten-
Inconclusion, we submitthatthe extantdata from studies that tial explanatory framework for understanding a wide variety of
directly aimed at testing core tenets of the predictive coding context effects and cue integration phenomena in spoken word
BEHAVIORALANDBRAINSCIENCES(2013)36:3 211
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
recognition. Converging evidence suggests that the initial Active inference and free energy
moments of competition between lexical alternatives are con-
strainedbymultiplesourcesofinformationfromdifferentdimen- doi:10.1017/S0140525X12002142
sions of the linguistic input (e.g., Dahan & Tanenhaus 2004;
Kukonaetal.2011),includinginformationexternaltothelinguis- KarlFriston
tic system, such as visually conveyed social information (Hay & TheWellcomeTrustCentreforNeuroimaging,InstituteofNeurology,University
Drager2010;StaumCasasanto2008)andhigh-levelinformation CollegeLondon,QueenSquare,LondonWC1N3BG,UnitedKingdom.
aboutaspeaker’slinguisticability(Arnoldetal.2007).Crucially, k.friston@ucl.ac.uk
lexical processing is influenced by information preceding the
target word by several syllables or clauses (Dilley & McAuley Abstract: Why do brains have so many connections? The principles
2008; Dilley & Pitt 2010) and this information affects listeners’ exposed by Andy Clark provide answers to questions like this by
appealing to the notion that brains distil causal regularities in the
expectations(Brownetal.2011;2012).Theintegrationofthese
sensorium and embody them in models of their world. For example,
various constraints, despite their diversity, is consistent with the
connections embody the fact that causes have particular consequences.
hypothesis that disparate sources of constraint are integrated Thiscommentaryconsiderstheimperativesforthisformofembodiment.
withingenerativemodelsinthelanguageprocessingsystem.
Clark’sframeworkalsohelpsexplainarecentsetofresultson 1. Introduction. It is a pleasure to comment upon Andy Clark’s
contexteffectsinreadingthataresurprisingfromtheviewpoint exposition of the Bayesian brain, predictive coding, and the
of more traditional theories that emphasize the bottom-up, free-energy principle. Clark describes modern thinking about
feed-forward flow of information. Farmer et al. (2006) demon- thebrainasaconstructiveandpredictivemachineinacompelling
strated that when a sentential context conferred a strong expec- andaccessibleway.Furthermore,hedevelopsthefundamentsof
tation for a word of a given grammatical category (as in The this approach from basic questions about the nature of life and
childsavedthe…,whereanounisstronglyexpected),participants consciousness–remarkably, without recourse to mathematical
wereslowertoreadtheincomingnounwhentheformofit(i.e.,its equations.
phonological/orthographicproperties)wasatypicalwithrespectto Clark’s synthesis is impressive–it highlights the consistency
other words in the expected category. In a subsequent MEG (and convergence) of the underlying ideas from many perspec-
experiment,Dikkeretal.(2010)showedthatatabout100msec tives, ranging from the psychophysics of perceptual inference
post-stimulus onset–timing that is unambiguously associated through to motor control and embodiment. The key thing that
withperceptualprocessing–astrongneuralresponsewaselicited emergesfromhistreatmentisthatminimisingsurpriseorsurpri-
when there was a mismatch between form and syntactic expec- sal (Tribus 1961) accommodates many intuitions and theories
tation.Moreover,thesourceoftheeffectwaslocalizedtotheocci- aboutbrainfunctionthathaveemergedoverthepastcenturyor
pitallobe,suggestingthatthevisualsystemhadaccesstosyntactic so. Had space allowed, other ideas could have been celebrated
representations.TheseresultsprovidesupportforClark’shypoth- (developed)withinthisframework;forexample,theprincipleof
esisthat“ifthepredictiveprocessingstoryiscorrect,weexpectto efficient coding (Barlow 1961); the notion of perception as
seepowerfulcontexteffectspropagatingquitelowdownthepro- hypothesis testing (Gregory 1980), and the action-perception
cessinghierarchy”(sect.3.1,para.8).Linguisticcontextisusedto cycle(Fuster2001)–allrestonthepremisethatwebuildparsi-
generate expectations about form-based properties of upcoming moniousmodelstoexplainourworld(Dayanetal.1995).
words,andtheseexpectationsarepropagatedtoperceptualcor- In what follows, I revisit three challenges–highlighted by
tices(Tanenhaus&Hare2007). Clark–tothefree-energyprinciple,anditsincarnationslikepre-
Thisframeworkalsoservestospecifythefunctionalityofthepre- dictivecodingandtheBayesianbrain.Specifically,theseare:(1)
dictionerrorthatariseswhensomedegreeofmismatchbetweena the relationship between free-energy minimisation and predic-
prediction and the incoming signal occurs. In behavioral and tive coding, (2) the dark room problem, and (3) explanatory
Event-RelatedPotential(ERP)experiments,prediction-inputmis- power.
matchfrequentlyresultsinincreasedprocessingdifficulty,typically 2. Free-energy and predictive coding. Clark frames surprise
interpretedasevidencethatpredictionisbeingmade.But,under minimisation in terms of predictive coding in the Bayesian brain
Clark’sframework,theerrorsignalassumesfunctionality;inpart, (Mumford 1992; Rao & Ballard 1999; Yuille & Kersten 2006).
itservestoadjusthigher-levelmodelssuchthattheybetterapproxi- This works extremely well and is a useful way to introduce the
matefutureinput.Theexplanatorypowerofthishypothesiscan ideas. However, it may detract from a simple but important
best be seen when considering the large amount of relatively point:Predictivecodingisaconsequenceofsurpriseminimisation,
recent literature on adaptation within linguistic domains. not its cause. Free-energy is a mathematical bound on surprise,
Whether in the domain of speech perception (Kleinschmidt & wherepredictionerrorisameasureoffree-energythatiseasyto
Jaeger 2011; Kraljic et al. 2008), syntactic processing (Farmer compute (neurobiologically). Free-energy minimisation is an
etal.2011;Fineetal.underreview;Wellsetal.2009),prosody instance of the celebrated principle of least action–because the
(Kurumadaetal.2012),orpragmatics(Grodner&Sedivy2011), average energy over time is also called action. Furthermore, it
ithasbecomeincreasinglyapparentthatreadersandlistenerscon- entails the maximum entropy principle (Jaynes 1957)–because
tinuallyupdatetheirexpectationsaboutthelikelihoodofencoun- free-energy is expected energy minus the entropy of predictions.
tering some stimulus based on their exposure to the statistical These principles willbe familiarto anyonein physics orstatistics
regularitiesofaspecificexperimentalcontext.Adaptationofexpec- because they govern the behaviour of known physical systems.
tationsispredictedbyClark’sframework,anditmaybetakenas The important thing–for self-organising systems–is that the
evidencethatprediction-inputmismatchproducesanerrorsignal long-term average of surprise is (almost surely) equal to the
thatisfedforwardtoupdatetherelevantgenerativemodels. entropy of sensations. This means that minimising free-energy
In sum, Clark’s hierarchical prediction machine hypothesis minimises sensory entropy. As articulated nicely by Clarke, we
providesaframeworkthatwebelievewillunifytheliteratureon can minimise free-energy (prediction errors) by either changing
predictioninlanguageprocessing.Thisunificationwillnecessarily our predictions (perception) or changing the things that we
involvesystematicexaminationofwhataspectsofthestimulusare predict (action). The key thing that the free-energy principle
predicted,wheninthechainofprocessingthesepredictionsare bringstothetableisthatbothperceptionandactionminimisepre-
generatedandassessed,andthepreciseformofthesegenerative dictionerrorbutonlyactionminimisessurprise(becausesurpriseis
models.Thistaskwillbechallengingbecauseitislikelythatgen- anattributeofsensationsactivelysampled).Thisisactiveinference
erativemodelsusesignal-relevantpropertiesthatdonotmapto (Friston 2010). The imperative to minimise surprise rests on the
thestandardlevelsoflinguisticrepresentationthatareincorpor- need to resist a natural tendency to disorder–to minimise
atedintomostmodelsoflanguageprocessing. sensoryentropy(Ashby1947).TheBayesianbrainandpredictive
212 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
codingarethenseenasaconsequenceof,orrequirementfor,this Nevertheless,weremainunconvincedthattheHPMoffersthebestclue
fundamental imperative–not asa causal explanation for how our yettotheshapeof aunifiedscienceofmindandaction.Theapparent
brainswork.Thisisimportant,becauseanyevidencethatsuggests convergence of researchinterests is offset by a profounddivergence of
weareBayes-optimalcanbetakenasevidenceforactiveinference. theoreticalstartingpointsandidealgoals.
3.Thedarkroomproblem.Clarkintroducesandthen(almost)
WesharewithClarkacommitmenttoexploringthedeepconti-
dismissesthedarkroomproblembyappealtoitinerant(explora-
nuities of life, mind, and sociality (Froese & Di Paolo 2011).
tory)behavioursthatminimisesurpriseoverlongperiodsoftime
Similar to the enactive notion of “sense-making,” Clark’s “hier-
(that is, minimise sensory entropy). I think that his discussion is
archical prediction machine” (HPM) entails that perceiving
exactly right; however, the “grain of truth” in the dark room
cannot be separated from acting and cognizing. Nevertheless,
problem can be dismissed in an even simpler way–by noting
thatpredicationerrorsareonlydefinedinrelationtopredictions. we disagree with Clark’s theoretical premises and their ideal
consequences.
Forexample,whenweenteradarkroom,thefirstthingwedois
Clark begins with the assumption that the task of the brain is
switchonalight.Thisisbecauseweexpecttheroomtobebrightly
analogous to establishing a “view from inside the blackbox.” On
lit(ormoreexactly,weexpectourbodilymovementstobringthis
this view,the mind is locked insidethe head and it follows that,
about).Inotherwords,thestateofaroombeingdarkissurprising
as Clark puts it, “the world itself is thus off-limits” (sect. 1.2,
because we do not expect to occupy dark rooms. This surprise
para. 1). This is the premise of internalism, from which another
depends upon (prior) expectations, but where do these prior
assumption can be derived, namely that knowledge about the
beliefs come from? They come from evolution and experience,
worldmustbeindirect.Accordingly,thereisaneedtocreatean
in the sense that if we did not have these prior beliefs, we
internal model of the external source of the sensory signals, or,
would be drawn to dark rooms and die there. In short, a
inClark’sterms,of“theworldhiddenbehindtheveilofpercep-
dynamic world can only support a generative model of that
tion”(sect.1.2,para.6).Thisisthepremiseofrepresentationalism.
world (prior beliefs) that predicts the dynamics it encounters–
Itisimportanttorealizethatthesetwopremisessetupthebasic
predictionsthatactionfulfils.
problemspace,whichtheHPMisdesignedtosolve.Withoutthem,
4. Evidence and explanatory power. Clark questions the evi- the HPM makes little sense as a scientific theory. To be sure,
dence for surprise minimisation and its explanatory power. I am
internalism may seem to be biologically plausible. As Clark
morecomplacentaboutthisissue,becausethefree-energyformu-
observes,allthebrain“knows”about,inanydirectsense,arethe
lationexplainssomuchalready.Potentexamplesrestonappreciat- ways its own states (e.g., spike trains) flow and alter. However,
ingthatanagentdoesnothaveamodelofitsworld–itisamodel.
theenactiveapproachpreferstointerpretthiskindofautonomous
In other words, the form, structure, and states of our embodied
organizationnotasablack-boxprisonofthemind,butratherasa
brains do not contain a model of the sensorium–they are that
self-organizedperspectivalreferencepointthatservestoenactaset
model. This allows one to equate the long-term minimisation of
of meaningful relations with its milieu (Di Paolo 2009). On this
surprise with the entropy of our physical (sensory) states–and
view,mindandactionarecomplexphenomenathatemergefrom
explainsourcurious(biological)abilitytoresistthesecondlawof
the nonlinearinteractions of brain, body, andenvironment (Beer
thermodynamics (Ashby 1947). But what does this mean practi-
2000). Such a dynamical perspective supports a relational, direct
cally? It means that every aspect of our brain can be predicted
realistaccountofperception(Noë2004;2009).
fromourenvironment.Thisseemsapowerfulexplanationforneu-
An enactive approach to neuroscience exhibits many of the
roanatomyandneurophysiology.Aniceexampleistheanatomical
virtuesoftheHPMapproach.Followingthepioneeringworkof
divisionintowhatandwherepathwaysinvisualcortex(Ungerlei-
Varela (1999), it is also formalizable (in dynamical systems
der & Mishkin 1982). Could this have been predicted from the
theory);ithasexplanatorypower(includingbuilt-incontext-sensi-
free-energy principle? Yes–if anatomical structure in the brain
tivity);anditcanberelatedtothefundamentalstructuresoflived
recapitulates causal structure in the environment, then one
experience (including multistable perceptions). Indeed, it
would expect independent causes to be encoded in functionally accounts for much of the same neuroscientific evidence, since
segregatedneuronalstructures.Giventhatobjectscanbeindiffer-
globalself-organizationofbrainactivity–forexample,vianeural
entplaces,theypossessseparableattributesof“what”and“where.”
synchrony–requires extensive usage of what Clark refers to as
This translates into separate neuronal representations in segre-
“backwardconnections”inordertoimposetop-downconstraints
gated visual pathways. In summary, the evidence for the free-
(Varelaetal.2001).
energyprinciplemaynotnecessarilybeinnextmonth’sscientific
Advantageously, the enactive approach avoids the HPM’s
journalsbutmaylieintheaccumulatedwealthofempiricalneuro-
essential requirement of a clean functional separation between
biologicalknowledgethatAndyClarkhasunpackedforus.
“errorunits”and“representationunits,”anditexhibitsadifferent
kind of neural efficiency. Properties of the environment do not
needtobeencodedandtransmittedtohighercorticalareas,but
not because they are already expected by an internal model of
the world, but rather because the world is its own best model.
Thebrainisnotanisolated “blackbox,”noris
The environment itself, as a constitutive part of the whole
its goal to become one brain-body-environment system, replaces the HPM’s essential
requirement of a multilevel generative modeling machinery (cf.
doi:10.1017/S0140525X12002348 Note16inthetargetarticle).
Theenactiveapproachalsoavoidsabsurdconsequencesofthe
TomFroesea,bandTakashiIkegamib
HPM, which follow its generalization into an all-encompassing
aDepartamentodeCienciasdelaComputación,InstitutodeInvestigaciones “free-energyprinciple”(FEP).TheFEPstatesthat“allthequan-
enMatemáticasAplicadasyenSistemas,UniversidadNacionalAutónomade titiesthatcanchange;i.e.thatarepartofthesystem,willchange
México,CiudadUniversitaria,A.P.20-726,01000MéxicoD.F.,México; to minimize free-energy” (Friston & Stephan 2007, p. 427).
bIkegamiLaboratory,DepartmentofGeneralSystemsStudies,Graduate
AccordingtoClark,thecentralideaisthatperception,cognition,
SchoolofArtsandSciences,UniversityofTokyo,Meguro-ku,Tokyo153-8902,
and action workclosely togetherto minimize sensoryprediction
Japan.
errorsbyselectivelysampling,andactivelysculpting,thestimulus
t.froese@gmail.com http://froese.wordpress.com
array. But given that there are no constraints on this process
ikeg@sacral.c.u-tokyo.ac.jp http://sacral.c.u-tokyo.ac.jp/
(according to the FEP, everything is enslaved as long as it is
Abstract: In important ways, Clark’s “hierarchical prediction machine” partofthesystem),thereareabnormalyeteffectivewaysofredu-
(HPM) approachparallelstheresearchagendawehave been pursuing. cingpredictionerror,forexamplebystereotypicself-stimulation,
BEHAVIORALANDBRAINSCIENCES(2013)36:3 213
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
catatonicwithdrawalfromtheworld,andautisticwithdrawalfrom “the attributionof agencyto another is a genuine result ofwhat
others.Theideathatthebrainisanisolatedblackbox,therefore, is truly experienced” (Gallagher 2004, p. 17, my italics). Some
formsnotonlythefundamentalstartingpointfortheHPM,but experiments suggest that this experience is the result of a prior
alsoitsidealendpoint.Ironically,raisingtheHPMtothestatus belief about the external origin of movement. This would be a
of a universal principle has the opposite effect: namely, making nicevindicationoftheseamlessstory.Ithink,however,thatthe
it most suitable as an account of patently pathological mental mindisnotquitesoseamlessandthatthereisanotherexplanation
conditions. consistentwiththepredictivecodingframework.
SimilarconcernsabouttheovergeneralizationoftheFEPhave How could someone experience his or her own movements as
beenraisedbyothers(Gershman&Daw2012),andareacknowl- alienated actions? The short answer is that right inferior parietal
edgedbyClarkinhis“desertlandscape”and“darkroom”scenarios. activationrepresents“surprisal”forintendedmovements.Surprisal
The general worry is that an agent’s values need to be partially isminimisedforintendedmovementsbecausethemotorcommand
decoupled from prediction optimization, since reducing surprise from the supplementary motor area (SMA) attenuates activity in
for its own sake is not always in the organism’s best interest. In the right interior parietal cortex. On the seamless story, unpre-
thisregardtheenactiveapproachmaybeofhelp.LikeFriston,it dicted/unattenuated parietal activation (surprisal) arising in the
rejects the need for specialized value systems, as values are context of action observation is experienced as alienation: “The
deemed to be inherent in autonomous dynamics (Di Paolo et al. patientsreallyhadnocues(asinferredfromthechangeinactivity
2010). But it avoids the FEP’s problems by grounding values in intheparietallobe)aboutwhethertheysawtheirownmovements
theviabilityconstraintsoftheorganism.Arguably,itistheorgan- orthoseofanalienagent”(Jeannerod2006,myitalics).Thus,they
ism’sprecariousexistenceasathermodynamicallyopensystemin experiencetheirownmovementsasalienated.
non-equilibrium conditions which constitutes the meaning of its InanimportantexperimentDapratiandcollaboratorshadsub-
interactionswiththeenvironment(Froese&Ziemke2009). jects tracea path from theirbody midline to a targetdirectly in
However, this enactive account forces the HPM approach to front of them. The subjects’ view of their moving hands was
make more realistic assumptions about the conditions of the occluded until the final 30% of the movement. For the first
agent. Notably, itis no longeracceptablethat the FEPrequires 70%,patientssawacomputer-generatedtraceofthemovement
a “system that is at equilibrium with its environment” (Friston path. On some trials the experimenters introduced a deviation
2010, p. 127). This assumption may appear plausible at a suffi- of15%intothemovementpathsothatifuncorrectedthetrace
ciently abstract level (Ashby 1940), but only at the cost of wouldveerofftotheright.Bothschizophrenicandneurotypical
obscuring crucial differences between living and non-living subjects were able to compensate for the perturbation, during
systems (Froese & Stewart 2010). Organisms are essentially the occluded section of the movement, with the result that
non-equilibrium systems, and thermodynamic equilibration when the hand came into view, the hand was to the left of the
with the environment is identical with disintegration and midline. Danckert et al. (2004) express the consensus in a large
death, rather than optimal adaptiveness. However, contra to literaturewhentheysaythatsuchcasesshowthat“on-linemoni-
the motivations for the FEP (Friston 2009, p. 293), this does toring and adjustment of action is unaffected in patients with
not mean that organisms aim to ideally get rid of disorder schizophrenia”(p.253).
altogether, either. Living beings are precariously situated InDaprati’sexperiment,thelast30%ofthemovementisnot
between randomness and stasis by means of self-organized cri- occluded.Whenthesubjectseesthehanditis15degreestothe
ticality, and this inherent chaos has implications for perception leftofastraightlinetothetarget.Neurotypicalsubjectsattributed
(Ikegami 2007). Following Bateson, we propose that it is more thisdiscrepancytothecomputer,indicatingthattheywereableto
important to be open to perceiving differences that make a becomeawarethattheyhadintendedadifferentmovementthan
difference, rather than to eliminate differences that could sur- the one they actually made. Schizophrenics with positive symp-
prise you. toms did not, leading to the conclusion that “online control can
coexist with a tendency to misattribute the source of error”
(Dapratietal.1997,p.253,emphasistheirs).
This tendency arises for schizophrenics when they visually
attend to the movement. In this case they seem lose access to
Unraveling the mind information about self-initiation. (Note: this is a problem of
degreenotkind.Thedominanceofvisualattentionoverproprio-
doi:10.1017/S0140525X1200235X ceptive/motor information generates similar misattributions in
manyconditions).
PhilipGerrans Blakemoreetal.(2003)hypnotizedsubjectswhosearmswere
DepartmentofPhilosophy,UniversityofAdelaide,NorthTerraceCampus,SA attached to a pulley apparatus and gave them two instructions.
5005,Australia. In the first they were told to raise their arms and in the second
philip.gerrans@adelaide.edu.au http://philipgerrans.com thatthepulleywouldraisetheirarms.Thepulleydidnotactually
exertanyforce.Highlyhypnotizablesubjectsmovedtheirarmsin
Abstract: A radical interpretation of the predictive coding approach responsetobothinstructionsbutinthesecondcasetheyreported
suggests that the mind is “seamless”–that is, that cancellation of error nofeelingofagency,attributingthemovementtothepulley.In
signals can propagate smoothly from highest to lowest levels of the
effect,hypnosisinducedtheexperienceoffailedactionmonitor-
controlhierarchy,dissolvingadistinctionbetweenbeliefandperception.
ing characteristic of delusions of alien control. The authors
Delusions of alien control provide a test case. Close examination
explain:“Thepredictionmadebytheparietalcortexisconcerned
suggests that while they are evidence of predictive coding within the
cortex,theyarenotevidencefortheseamlessinterpretation. more with high level prediction such as strategic planning
actions.” Furthermore, they suggest, “Perhaps the predictions
Andy Clark describes delusions as the dark side of the seamless madeby theparietal cortexcan bemade available toconscious-
storyforpredictivecodinginwhich,“Inplaceofanyrealdistinc- ness”(Blakemoreetal.2003,p.243,myitalics).Inotherwords
tion between perception and belief we now get variable differ- we can experience ourselves as authors of our actions in virtue
ences in the mixture of top-down and bottom-up influence, and of attenuated parietal activity. Because schizophrenics cannot
differences of temporal and spatial scale in the internal models attenuate this activity, they cannot become aware of themselves
thataremakingthepredictions”(sect.2.3,para.8). asauthorsoftheiractionsinsomeconditions.
Theorists who endorse the predictive coding model have Doesitfollowthatunattenuatedparietalactivityrepresentsthat
arguedthatindelusionsofaliencontrol,patientsactuallyexperi- someoneelseistheauthoroftheaction?Fromwhatwehaveseen
encebeingcontrolledbyanexternalagent.AsGallagherputsit, so far, the modulation of parietal activity only tells the subject
214 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
whetheramovementisproducedbytheSMA.Thatisaverylow andreproducing–areonacontinuumofconnectedultimateand
levelofcognitiveprocessingfromwhichinformationaboutagency proximatecausesandperhapsfueltheorganizationofperception
isabsent. andaction?DoBayesiananimalspredictthefuturefromasetof
Evolution has not posed us with the problem of determining constantly updated priors to produce predictions of most impor-
which movements are ours rather than someone else’s. It has tance:findingamate,findingabettermate,ordying?
posed us with the problem of determining which aspects of a Fitnessisarelativeconceptanddemography-dependent.Here,
movement are consequences of motor intentions in order to we direct readers to a theoretical scenario (Figure 1) with its
computeandresolveerror.Therefore,thereseemsnoreasonto mathematical analytical solutions for the evolution of human
thinkthatwewouldneedtousepredictivecodingtodisambiguate and nonhuman Bayesian individuals who perceive their real
theagentofanactionratherthantosimplycontrolourownaction. time alternatives, predict the fitness that would accrue or not
This is true both at the level of automatic and of controlled from those alternatives and modify their behavior accordingly.
processing. One of our main assumptions is that individuals are able to
Ingeneral,then,Iconcludethatparietalactivationisnotspecial- predict(unconsciouslyorconsciously)theirowndemographiccir-
isedfordeterminingwhointendedtheaction.Rather,itdetermines cumstances (how they are doing/will do relative to others). To
foranymovementwhetheritisaconsequenceofamotorinstruc- someofourreaders,ourassumptionshaveseemedotherworldly.
tion. It evolved to control movement, not to identify the agent. Clark’sarticlesuggeststhatourassumptionsarenotsooddinthe
Becauseschizophrenicscannotattenuatethisactivitywhenvisually humancognitivesciencesandtheysignalnewempiricalresearch
monitoringactions,theycannotexperiencethemselvesasauthors aboutthemeaningsofanimalbehaviorintheunifiedcontextsof
of those actions. In both experiments, however, the context pro- linkedproximateandultimatecauses.
videsadefaultinterpretationofalienation. FromaDarwinianevolutionaryperspective(Darwin1871),who
If the fabric of the mind is stitched together seamlessly with among potential mates to accept and/or reject is one of the most
predictivecodingthreadsweshouldbeabletounravelitentirely importantofreproductivedecisions.Tobefitnessenhancingincon-
from the top down. But the fact that online control in schizo- temporarytime,reproductivedecisionsmustbeflexibleandmade
phreniaisintactsuggeststhattheseamlinkingautomaticandvisu- against the unavoidable context of demography (Gowaty &
ally guided motor control, while flexible, has been robustly Hubbell2005).Demographyisnotstatic:thingschange;stochastic
tailoredbyevolution. effectsareinevitable.Potentialmatesenterandleavepopulations;
some individuals may die and never appear again; and predators,
parasites,andpathogenscomeandgo,sothatthesurvivallikelihoods
ofdecision-makersalsochange.Theminimalsetofparameterscon-
tributing to stochastic demography (Hubbell & Johnson 1987) are
Bayesiananimalssenseecologicalconstraints thoseprovidingsensoryinformationabouttheavailabilityofpoten-
to predict fitness and organize individually tial mates (encounter probability, e), the likelihood of continued
flexible reproductive decisions l w if i e th o in fd t e h c e isi p o o n p -m ul a a k ti e o r n s( o su f rv fi i t v n a e l s p s ro th b a a t bil w it o y, ul s d ),a b n e d c t o h n e fe d r i r s e tr d ibu fr t o io m n
mating with this or that potential mate (w-distribution). The
doi:10.1017/S0140525X12002385 minimalsetofinformationnecessaryformakingreal-time,fitness-
enhancingreproductivedecisionsise,sandthew-distribution.
PatriciaAdairGowatyandStephenP.Hubbell
GowatyandHubbell(2005)hypothesizedthatindividuals,not
DepartmentofEcologyandEvolutionaryBiology,andInstituteofEnvironment sexes, are under selection to flexibly modify their reproductive
andSustainability,LosAngeles,CA90095;andSmithsonianTropical
decisions moment-to-moment as their ecological and social cir-
ResearchInstitute,Unit9100,BOX0948,DPOAA34002-9998.
cumstanceschangetoenhancetheirinstantaneouscontributions
gowaty@eeb.ucla.edu shubbell@eeb.ucla.edu tolifetimemeanfitness(Fig.1).Stochasticvariationine,s,andl
http://www.eeb.ucla.edu/indivfaculty.php?FacultyKey=8418
(latency from the end of one mating, to onset, to receptivity, to
http://www.eeb.ucla.edu/indivfaculty.php?FacultyKey=8416
the next mating) results in mean lifetime number of mates
Abstract: A quantitative theory of reproductive decisions (Gowaty & (MLNM).VariationinMLNMfavorstheevolutionofsensitivity
Hubbell 2009) says that individuals use updated priors from constantly to e, s, and l, while variation in the w-distribution favors assess-
changing demographic circumstances to predict their futures to adjust ment of fitness that would be conferred through mating with
actions flexibly and adaptively. Our ecological/evolutionary models of this or that potential mate. Once sensitivity and assessment
ultimate causes seem consistent with Clark’s ideas and thus suggest an evolve,thestageissetforflexibleindividualstomodifytheirbe-
opportunity for a unified proximate and ultimate theory of Bayesian havior in ways which their sensitivities and assessments predict
animalbrains,senses,andactions. are fitness enhancing. The analytical solution to this model is
the Switch Point Theorem (SPT). An SPT graph shows the
Reading Clark suggests possible connections between proximate
causes of animal–not just human–perception, mind, and action rule for acceptance and rejection of each potential mate,
rankedfrombestat1toworstatn,byasingleuniqueindividual
andtheirultimatecauses.Wesuggestthatitisworthconsidering
in the population, given variation in e, s, l, n and the w-
that nonhuman animals, not just humans, are Bayesian too, and
distribution.
thatthe world alsoappearstothem as a setofintertwined prob-
The assumptions of the analytical solution as to how many
ability density distributions. We think of all animals as Bayesian
and we define (Gowaty & Hubbell 2005; 2009) animals as adap- potential mates in a population will be acceptable or not to a
tively flexible individuals who “predict” (“visualize,” “imagine”) givenindividual(Gowaty&Hubbell2009)areasfollows:
alternativesandmakechoicesamongthem“controllingplasticity”
to serve fitness. We have argued previously that animals predict 1. Beforetherewasnaturalselectiontoacceptorrejectpoten-
their futures and act as though they are indeed perceiving and tialmates,therewasstochasticvariationinencounterswithpoten-
responding to “intertwined set[s] of probability density distri- tialmatesandwithdecision-makers’likelihoodofsurvival.
butions” (see target article, sect. 4.1, para. 3). We say explicitly 2. The encounter probability and survival probability deter-
that animals behave as if playing the odds of fitness against the minethemeanlifetimenumberofmatesandthevarianceinlife-
oddsoftime.Thus,wearguethatanimalsareflexibleindividuals timenumberofmates.
who act behaviorally and physiologically in real ecological time, 3. Potentialmatescomeinn-qualities,wheren=thenumber
not just evolutionary time, to enhance their real-time fitness. ofpotentialmatesinthepopulation.
Could it be that the intertwined set of probability density distri- 4. Mateassessmentisself-referentialanddependsuponinfor-
butionsassociatedwiththemainproblemsofindividuals–surviving mationlearnedduringdevelopmentaboutselfrelativetoothers.
BEHAVIORALANDBRAINSCIENCES(2013)36:3 215
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Figure 1(Gowaty& Hubbell). The hypothesisfor the evolution of adaptivelyflexiblebehavior (modified fromfigures in Gowaty&
Hubbell2005;2009).
5. Individuals update their information to predict adaptive Abstract:Wesuggestthatthehierarchicalpredictiveprocessingaccount
acceptance and rejection of potential mates thereby maximizing detailedbyClarkcanbeusefullyintegratedwithnarrativepsychologyby
instantaneouscontributionstolifetimefitness. situating personal narratives at the top of an individual’s knowledge
Theanalyticalsolutionofwhomtoacceptandrejectformatingis hierarchy. Narrative representations function as high-level generative
models that direct our attention and structure our expectations about
theswitchpointtheorem(SPTinFig.1). unfolding events. Implications for integrating scientific and humanistic
viewsofhumanexperiencearediscussed.
Resistance to our assumptions from behavioral ecologists is
perhaps not surprising, for we begin with individuals, rather Clark’s article presents the hierarchical predictive processing
than sexes, to predict sex differences. What surprises us, accountofhumancognitionasaunifyingmodelforunderstanding
however, is that there are critics who resist our assumption that mind and action. He also highlights the importance of bridging
animals use probabilistic information as instantaneous clues to thisperspectivewithourdaily“folk”or“humanistic”conceptions
predict their next move, which the SPT proved theoretically is ofselfandworld.Weproposethatsuchabridgeisprovidedbythe
adaptive.TheBayesianupdatingthatClarkdescribesasafunda- fieldofnarrativepsychology,withnarrativemodelsoftheworld
mentalaspectofneuralprocessingofwhattheworldis,suggests occupying the highest levels of an individual’s predictive
tousthathisandourideasareconceptuallylinked.Ouruseofthe hierarchy.
Bayesian metaphor suggests that there is something self-similar Agrowingbodyoftheoryandresearchindicatesthatthebroad-
linking proximate and ultimate causes. But, what if animals too estandmostintegrativelevelsofanindividual’sknowledgesystem
areBayesianswithlinkagesbetweenhowandwhybrainsinterpret can be characterized as narrative descriptions of reality (Bruner
theworld? 1986;1991;McAdams1997;Peterson1999;Ricoeuretal.1990;
We agree with Clark. What is on offer is a unified science of Sarbin 1986). Although narratives can take many different
perception, attention, prediction, and flexibility of action. The forms, they are distinguished by their ability to compress and
SPTsuggeststhatfitnessdrivesall.
encode a great deal of information about the world, including
the causal relations between events over time (Graesser et al.
1997), the planning and sequencing of goal-directed actions
(Schank & Abelson 1977), the emotional significance of an
event within a temporal context (Oatley 1992), the unfolding
Personal narratives as the highest level of nature of personal identity (McAdams 1997), and the dynamic
cognitive integration intentions of multiple social agents (Mar & Oatley 2008). It is
the integrative ability of narrative representations to coordinate
vastdomainsofknowledgeandbehaviorthathasledsometheor-
doi:10.1017/S0140525X12002269
ists to propose narrative as an organizing framework for under-
JacobB.Hirsh,aRaymondA.Mar,bandJordanB.Petersonc standing human psychology (Sarbin 1986). Narrative
aRotmanSchoolofManagement,UniversityofToronto,Toronto,ONM5S3E6, representations thus appear to function as high-level generative
Canada;bDepartmentofPsychology,YorkUniversity,Toronto,ONM3J1P3, models of the sort that Clark describes, structuring our expec-
Canada;cDepartmentofPsychology,UniversityofToronto,Toronto,ONM5S tationsaboutdailyexperiencesandprovidinganorganizingframe-
3G3,Canada. workforinterpretingincomingsensoryinformation(Bruner1986;
jacob.hirsh@utoronto.ca www.jacobhirsh.com Mandler 1984). Such representations are particularly crucial for
mar@yorku.ca www.yorku.ca/mar anticipatingthesequentialunfoldingofeventsovertime,allowing
peterson@psych.utoronto.ca www.psych.utoronto.ca/users/ forthepredictionofactionsandoutcomeswithinachainofevents
peterson (Abelson 1981). Integrating narratives into predictive modeling
216 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
means that information consistent with an individual’s currently high-level generative models (instantiated as narrative represen-
active narrative schema will be “explained away” in the fashion tations) is thus one of the core requirements for mental health
that Clark describes; events that were not predicted by the and well-being. Insomuch as the humanities help to provide us
schema,ontheotherhand,willrequiremoredetailedprocessing withnarrativerepresentationsthatcapturetheemotionalvicissi-
andaccommodation. tudesofdailylifeinagivenculturalenvironment(Oatley1999),
Incorporating narrative psychology into the hierarchical pre- they help to orient and constrain our predictive modeling and
dictive processing account brings with it an important advan- provide critical components of our adaptive functioning in the
tage. In particular, narratives provide a point of contact world. Integrating narrative psychology with the predictive pro-
between the predictive processing account and the socio-cul- cessing account thus highlights the importance of humanistic
tural context in which individual minds develop. Narrative rep- approaches for arriving at a complete understanding of human
resentations are fundamentally social in nature, as children are cognitivescience.
socialized to adopt particular modes of narrative thought
during development (Nelson & Fivush 2004). An individual’s
personal narrative representations of the world are selectively
constructed from the many social and public narratives that
Whenever next: Hierarchical timing of
are available within the broader cultural context (Nelson
2003). Inplacingthesenarrativestructuresatthetopofthepre- perception and action
dictive hierarchy, an individual’s cultural context is afforded a
powerfulinfluenceonthetop-downregulationofdomain-specific doi:10.1017/S0140525X12002336
knowledge structures and behavioral patterns (Kitayama &
Cohen 2010). LinusHolmandGuyMadison
More broadly, this hybrid narrative predictive processing DepartmentofPsychology,UniversityofUmeå,90187Umeå,Sweden.
accounthighlightstherelevanceofthehumanitiesforthecogni- linus.holm@psy.umu.se guy.madison@psy.umu.se
tivesciences,suggestingaunifiedframeworkfortheirintegration.
http://www.psy.umu.se/om-institutionen/personal/guy-madison
A primary function of the humanities is elaborating upon the
“manifest”imageoftheworldasitisdirectlyexperiencedbyus, Abstract:Thetargetarticlefocusesonthepredictivecodingof“what”and
incontrasttothe“scientific”imagethatprovidesadepersonalized “where” something happened and the “where” and “what” response to
make. We extend that scope by addressing the “when” aspect of
view of the world (Sellars 1963). Narrative psychology acknowl-
perception and action. Successful interaction with the environment
edges the importance of these “manifest” images, as they guide
requires predictions of everything from millisecond-accurate motor
an individual’s expectations and shape the cascade of cognitive
timing to far future events. The hierarchical framework seems
operations that give rise to subjectiveexperience. Within such a appropriatefortiming.
framework, a full appreciation of an individual’s subjectivity is
thuscrucialtoadequatelymodelingherconstrualofandreactions Timingintrinsicallyinvolvesprediction.Determiningwhentoact
totheworld. uponafutureeventrequirestheabilitytopredictit.Forinstance,
Althoughhigher-ordernarrativesinfluencecognitiveprocesses, ensemble music performance requires precise estimation of the
the coherence of these narrative representations varies from passage of time in order to synchronize and coordinate sounds
person to person, with some having more clearly articulated tore-producethemusicalstructure.
stories for situating their experiences than others (McAdams Acentralideainthepredictivecodingaccountofcognitionis
2006). A crucial consequence of this variation is that those with that prior knowledge is used to guide sensory interpretations
onlyvaguenarrativerepresentationsoftheworldwillhavemore and action decisions. Identifying the periodicity of an event in
difficulty selectively focusing attention on the most relevant the world is typically an ill-posed problem: How does the
aspects of the environment. From a predictive processing per- agent know beforehand what constitutes the signals that indi-
spective, a lack of narrative coherence will produce an inability cate a period? To infer the beat in a complex musical piece,
togenerateanadequatepredictivemodeloftheworld,hindering or when a quail will reappear from behind a bush, are under-
the ability to “explain away” the majority of the sensory infor- specified problems in the sensory signal. In both cases, prior
mation being received and producing a burdensome processing experience appears necessary to play to the beat or to catch
load. When no high-level generative model is available to ade- the quail.
quatelyanticipatetheongoingunfoldingofevents,thecognitive Anotherkey ideain thepredictivecoding frameworkisinfor-
system can very easily be overwhelmed by the large volume of mation compression. Representing music or other temporally
“error”informationbeingcarrieduptheneuralhierarchy(Hirsh structuredeventsascyclesreducestheentropyinthesignaland
etal.2012).Thishasdownstreamconsequencesfortheindividual, allowsformoreefficientstorage.Actioncanservetofurtherboot-
as a lack of personal narrative integration is associated with straptiming.Forinstance,humansspontaneouslytapalongwith
reduced well-being (Baerger & McAdams 1999). In contrast, theirhandsorfeettomusic(Brown2003)andentraintheirmove-
developingclearlyarticulated narrativeaccountsofone’sexperi- mentstootherpeople’smovements(Demosetal.2012;Merker
encesisassociatedwithanumberofpositivehealthbenefits(Pen- et al. 2009). Just like active interactions with an object improve
nebaker&Seagal1999). perception (Harman et al. 1999), timed activities have been
Althoughtheaffectivesignificanceofpredictionerrorswasnot shown to improve the reliability of temporal perception (Grahn
highlightedinClark’sarticle,thenarrativeaccountanditsbaseof & McAuley 2009; Phillips-Silver & Trainor 2007). A benefit of
subjectivitymakesthisclear,aspredictionerrorscanreflectviola- having induced the rhythm is that violations of rhythm are
tionsofbasiclifeassumptions.Sucherrorsareoftenexperienced easiertodetect(Ladinigetal.2009).
asaversiveandthreatening(Hajcak&Foti2008)andcantriggera Bayesianinferenceoftimingrequirestemporaluncertaintiesto
variety of attempts to minimize or suppress error information berepresented.Thenatureofthetimingsignalremainsopento
(Proulxetal.2012),someofwhichveertowardthepathological debate. One candidate is trace strength that decays with time
(Peterson 1999). The emotional impact of expectancy violations (Buhusi & Meck 2005). A function of decay, trace strength
alsoappearstovarydependingontheleveloftheneuralhierarchy conveys information about the time since it occurred. Another
at which they occur, such that relatively low-level errors are time signal candidate is populations of oscillating neurons.
experiencedasfairlybenignwhileviolationsofone’scorenarra- Timing could then be established by coincidence detection in
tives about the world are often associated with severe forms of the oscillating network (Matell & Meck 2004; Miall 1989).
emotional trauma (Janoff-Bulman 1992). Within the narrative Regardless of the signal format, its representation is noisy and
framework, the ability to flexibly maintain the integrity of one’s its uncertainty should reasonably increase with timing over long
BEHAVIORALANDBRAINSCIENCES(2013)36:3 217
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
durations.Indeed,humantemporalperceptionandproductiondo Two kinds of theory-laden cognitive
deterioratemonotonicallywithtimescale(Buhusi&Meck2005). processes: Distinguishing intransigence
Exactlyhowthehumansystemdealswithtemporalsignaluncer-
from dogmatism
taintyremainsanopenquestion.
Akeynotioninthetargetarticleisthehierarchicaldivisionof
doi:10.1017/S0140525X12002403
labor from bottom sensory to top associative cortical control.
For timing, the scaling of time appears as a likely attribute to EliasL.Khalil
stretch across such a hierarchical structure. Millisecond control
DepartmentofEconomics,MonashUniversity,Clayton,Victoria3800,
ofmotortimingcannotfeasiblybecarriedoutdirectlybythepre-
Australia.
frontalcorticalregionsinvolvedinworkingmemory,duetotrans-
elias.khalil@monash.edu www.eliaskhalil.com
ferspeed,andtheaccumulatedsignalerrorthatsuchanextensive
chainoftransmissionwouldinvolve.Instead,millisecondcontrol Abstract:Thebrainisinvolvedintheory-ladencognitiveprocesses.But
might be represented closer to the action output (e.g., cortical there are two different theory-laden processes. In cases where the
effector representation and the cerebellum) and involve a more theory is based on facts, more facts can either falsify or confirm a
directpathwaybetweensensoryinputandmotoroutput.Incon- theory.Incaseswherethetheoryisaboutthechoiceofabenchmarkor
trast, when observation and action become more detached in a standard, more facts can only make a theory either more or less
time,thewindowofopportunityforplanningopensup,involving warranted.
moreprefrontalprocessing.
Consistently,manystudiessupporttheviewthatthereisadis- Clarkoffersareviewofaviewofthebrainwherethebrainpro-
tinction in neural representation, for example, above and below cessesinputinformationinawaythatconfirmsitspriorsoritspre-
about one second (Gooch et al. 2001; Lewis & Miall 2003; dictions.Thisdoesnotmeanthatthebraincreatesitsownreality.
Madison 2001). Furthermore, time representation for sub- Thebrain,rather,processesinputdata,butitdoessoinlightofits
second intervals appears at least to some extent to be sensory own priors. The brain is a bidirectional hierarchical structure.
specific(Morroneetal.2005; Nagarajanetal.1998), andunder While the top layers generate priors, the lower layers process
some conditions even limited to spatial locations (Burr et al. input data. The brain amounts to the dynamics of image-
2007; Johnston 2006). Additionally, there appear to be break- making, where the top-down process generates unified images,
pointsinintervaldiscriminationsuchthattherearescalarproper- while the bottom-up process, which takes data, corrects the
tiesintimingperformanceforintervalsaboveaboutonesecond, images.
but nonlinear relationships between time and perception below Suchaniterativecognitiveprocessisnotsimple.Thetop-layer
one second (Karmarkar & Buonomano 2007; Rammsayer generatedpriorsgreatlydeterminetheassimilatedinputs.Butthe
1999)–further supporting the notion that longer time intervals input data are not fully manipulated by the priors. As such, it is
are controlled by different brain regions from those involved in best to characterize the brain as a medium that tries to balance
sub-secondtiming.Also,withlongertimeperiodsunderconsider- betweentwocompetingneeds:First,thebrainneedstogenerate
ation,alargerpartoftheprefrontalcortexgetsactivated(Lewis& a unified, that is, meaningful, image of the real world. The top
Miall2006; Simonsetal.2006).This timing-relatedfrontal lobe layers, which generate the priors or the predictions, function to
network is also largely overlapping with those employed by fulfilltheneedforunity.Second,thebrainneedstoaccommodate
working memory and executive control processes (Jahanshahi raw input data to stay as truthful as possible to the given real
etal.2000;Owenetal.2005),suggestingthattimingconstitutes world.Ifthebrainperformsonlythefirstfunction,thatis,preser-
a general cognitive control problem at longer time durations. vingtheunityoftheimage,thebrainwouldgenerateimagesthat,
The hierarchical organization from accurate and dedicated although unified, are disconnected from reality. On the other
timing devices at sensory levels and less accurate but flexible hand, if the brain performs only the second function, that is,
timing at longer time frames in the prefrontal cortex might be preserving the details of the world, the brain would generate
accounted for by signal averaging in the time domain from images that, although detailed, are tremendously messy and
sensorytofrontalcorticalregions(Harrisonetal.2011).Harrison meaningless.
and colleagues suggested that decay rate is faster close to the As a result of trying to meet these two competing needs, the
sensoryinputlevelandsloweratlaterstagesinthevisualhierar- images that cognitive processes generate are theory-laden. This
chy, thus allowing for a differentiation across time scale and has long been understood by the emerging new philosophy of
brain region. Taken together, there is abundant support for the science, most epitomized by the contribution of Thomas Kuhn,
differentiation of brain regions involved in timing at different andcanevenbetracedtoImmanuelKant.Thisisnottheplace
timescales. toreviewthehistoryofphilosophyofscience,characterizedulti-
Communication of temporal information across the levels of mately as a conflict between rationalism (demanding unity of
the outlined timing hierarchy is currently rather unclear. Intui- image) and empiricism (demanding detailed images) (see Khalil
tively,themoretemporallyextendedcontrolprocessesassociated 1989).WhatisgermanehereisthatClarkfailstonotetwodiffer-
with prefrontal working memory processes might still influence entkindsoftheory-ladencognitiveprocesses:thefirst,whichcan
control at shorter time frames without interfering in direct becalled“perception-laden”processes,whereone’stheorycanbe
control, such as in initiation of a drumming exercise, without ultimatelycorrected by sensory input; the second, whichcan be
employingmomenttomomentvolitionalcontroloftheindividual called “conception-laden” processes, where one’s theory cannot
beats. Recent findings from our research group suggest that beultimatelycorrectedbysensoryinput.
executive functions are indirectly related to motor timing via, Perception-laden beliefs, for example, let one predict stormy
forexample,effectorcoordination(Holmetal.,inpress).Further- weather or that the Earth is flat. In light of sensory input, and
more,thereisawell-establishedyetpoorlyspecifiedrelationship using Bayes’ rule, one may adjust such a prediction and reach
between intelligence and simple motor timing (Galton 1883; the conclusion that the weather will be stable and the Earth is
Madisonetal.2009).Moreresearchisclearlyneededtoidentify round.Manypeoplemaynotadjustquicklyandinsiston“explain-
howhigh-leveltemporalexpectationsmightinfluencebriefinter- ing away” the data to justify their priors. But such manipulation
valtiming.Anotherimportantquestionishowthebrainidentifies can be delineated from the normal course of belief adjustment.
the time scales from noisy input and learns how to treat those When perception-laden processes are at issue, priors must ulti-
signals. The predictive account of cognition seems like a useful mately adjust to correspond to the mounting evidence. The
theoreticalframeworkforunderstandingtiming,andtheBayesian legal system, and everyday science, cannot function without the
formalism is a promising tool to investigate and explain its adherencetothepossibilityofbelief-freegroundsthatcanallow
operation. sensorydata,inthefinalanalysis,todominatetop-downpriors.
218 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Conception-laden beliefs, for example, let one view a picture theories of cognition. For illustration we consider the visual
such as the famous Rubin Vase, where the brain switches neurosciences, a paradigmatic field for the investigation of
between perceiving the vase and perceiving the two profiles. sensory processes. A discourse given by standard textbooks
The image depends on what the brain judges to be the back- depictsaworldexternaltotheagent,withasetofpre-established
ground. If the background is judged to be white, the brain sees attributesandobjects.Sensoryprocessingstartswithtransmitting
the two profiles. If the background is judged to be black, the theseattributesbylow-levelneuronstosubsequentstages.There,
brainseesthevase.Noamountofdatacancompelthetoplevel moreelaboratecomputationsextractpatternsofstimulusfeatures
hierarchy of the brain to abandon its prior. The prior here andobjects.Uptothispoint,processingfocusesonaveridicalrep-
cannot be confirmed or refuted by evidence because it is not resentation of the external world,serving for later decisionsand
based on evidence as with perception-laden processes. The actions.Weargueinfavorofaradicalchangeofthisview,assign-
choice of background, the basis of conception, is similar to the ingacentralroletopredictionsofsensoryconsequencesofone’s
choiceofabenchmark,whereonecanjudgeaglasstobeeither own actions and thereby eliminating the strict separation of
half-fullorhalf-empty.Likewise,onejudgesone’sincomeassat- sensoryandmotorprocessing.
isfactoryornon-satisfactorydependingonone’sbenchmark.Hap- In the target article, Andy Clark beautifully describes the
piness seems to depend, at least partially, on the choice of an central role of predictions in sensory processing. We endorse
arbitraryincomeasthebenchmarkincome. thisview–yettwocomplementaryaspectsareneeded.First,pre-
The conflation of the perception- and conception-laden pro- dictability of sensory signals serves as a normative principle
cesses leads to the commitment of a Bayesian fallacy. The guiding sensory processing and as a boundary constraint in the
fallacy arises from the supposition that all beliefs are percep- selectionofinformationtoprocess.Second,predictionsareper-
tion-laden and, hence, can be corrected by further empirical formed only in the context of the agents’ action repertoire
investigation (Khalil 2010). It is imperative to distinguish con- (König & Krüger 2006). These two specifications have crucial
ceptionsfromperceptions.Asidefromallowingustounderstand implications.
happiness, the distinction sheds light on two kinds of stubborn- Theinformationcontentoftheprimarysensorysignalisenor-
ness:intransigence,relatedtoperception-ladenbeliefs,anddog- mous,andextractionofinformationwithoutfurtherconstraintis
matism, related to conception-laden beliefs. Belief in a flat an ill-posed problem. However, it is not the task of the sensory
Earthandinconspiracytheoriesillustratesintransigence.Incon- systems to process all possible details, and a reduction of infor-
trast,toinsistonabackground,despitetherisingevidencetothe mationisparamount.Eveninsimplemodelsystems,takinginto
contrary,illustratesdogmatism.TousetheRubinVaseexample,if account a limited behavioral repertoire converts demanding
a person chooses the black as the background and, hence, the sensory processing into a tractable problem (Wyss et al. 2004).
imageisthevase,butcontinuestochoosetheblackdespitecon- Applying the normative principle of predictability generalizes
trary added evidence–such as added eyes and moustache–the this idea and serves as a selection criterion for features to
personwouldbedogmatic.Whilethedogmaticbeliefcannotbe processandvariabilitytoignore.Indeed,withinthehierarchyof
judgedastrue orfalse,itcanbejudged aswarrantedorunwar- the visual system, neuronal response properties are invariant to
rantedgiventhedetailsoftheprofiles.Thechoiceofbackground, more and more parametric changes of the sensory input
to remind ourselves, is non-empirical and, hence, cannot be (Tanaka 1996). Even category learning at higher levels of the
characterizedastrueorfalse. visualsystemcanbeinterpretedwithinthisframework.Thecom-
monalitiesbetweendifferentinstancesofthesamecategoryrelate
tosimilarsensorimotorpatternsgeneratedbytheinteractionwith
these“objects.”Finally,actionsaredirectlyrelatedtotheagent’s
survivalandtherebyprocessingfeaturesthatchangepredictably,
Predictions in the light of your own action given chosen actions, are more relevant than those that do not.
repertoireasageneralcomputationalprinciple Hence, processing of sensory signals is guided by the relevance
forbehavior,andrelevanceisexpressedbytheabilitytopredict
doi:10.1017/S0140525X12002294 sensorychangescontingentontheownactionrepertoire.
A paradigm is based on the active interpretation of incoming
PeterKönig,a,bNiklasWilming,aKaiKaspar,a sensory information such that it makes sense for the agent.
SaskiaK.Nagel,aandSelimOnatc Hence, it is intended to replace a passive representationalist
aInstituteofCognitiveScience,UniversityOsnabrück,49076Osnabrück, view. In such a paradigm, the predicted future state of the
Germany;bDepartmentofNeurophysiologyandPathophysiology,University worldisimportantinsofarasitinteractswithownactionsandvari-
MedicalCenterHamburg-Eppendorf,20251Hamburg,Germany; ablesofimportanceareco-determinedbytheactionrepertoire.A
cDepartmentofSystemsNeuroscience,UniversityMedicalCenterHamburg- demonstration of the integration of new sensory information
Eppendorf,20251Hamburg,Germany. (magnetic north) that is co-determined by own movements
koenig@uni-osnabrueck.de nwilming@uni-osnabrueck.de (yaw-turns) is given by the feelSpace project (Kärcher et al.
kkaspar@uni-osnabrueck.de snagel@uni-osnabrueck.de 2012; Nagel et al. 2005). Comparing different species, for
sonat@uos.de example, cat and human, with similar visual input (Betsch et al.
http://cogsci.uni-osnabrueck.de/∼NBP/ 2004; Einhäuser et al. 2009), the remarkable differences in the
http://cogsci.uni-osnabrueck.de/∼nwilming/ sensoryhierarchyappeartobeatoddswithapassiverepresenta-
http://kai-kaspar.jimdo.com/ tionalist view and await an explanation. Here, differences in be-
http://cogsci.uni-osnabrueck.de/en/changingbrains/people/saskia havioral repertoire offer themselves. Pointedly, we speculate
www.selimonat.com that the huge action repertoire of humans, due to, for example,
opposablethumbs,mightfostertheillusionofaveridicalpercep-
Abstract: We argue that brains generate predictions only within the tionoftheworld.Ithasbeenemphasizedearlyonthatcognitive
constraints of the action repertoire. This makes the computational
andmotorcapabilitiesdevelopinparallelandmutualdependence
c se o n m so p r le y x a it n y d tr m ac o t t a o b r le sy a s n te d m f s o . s H te e rs nc a e, st i e t p is -b m y- o st r e e p of pa a ra b l e le n l e d fi e t v t e h l a o n pm a e li n t t er o a f l (Piaget 1952). To grow up means to harden specific action rou-
tines,ontheonehand,buttolosethebulkofalternativeaction
constraint and may serve as a universal normative principle to
understandsensorimotorcouplingandinteractionswiththeworld. capabilitiesand cognitiveflexibility,onthe otherhand. Further-
more, a large variability of perceptual interpretation of identical
Presentcognitivescienceischaracterizedbyadichotomysepar- physical stimuli is found between humans of the same culture
ating sensory and motor domains. This results in a perceived area aswell asbetween differentcultures (Segallet al. 1963). A
gap between perception and action and is mirrored in leading critical view of our own culture reveals many aspects that serve
BEHAVIORALANDBRAINSCIENCES(2013)36:3 219
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
toincreasethereliabilityofpredictions.Insummary,agentswith predicting sensory inputs becomes trivial and precise. In
identical sensory organs but different action repertoires might response, Clark suggests that “animals like us live and forage
haveverydifferentviewsoftheworld. in a changing and challenging world, and hence ‘expect’ to
Istheconceptofnormativeprinciplesplausibleinviewofour deploy quite complex ‘itinerant’ strategies” (sect. 3.2, para. 2).
knowledgeofcorticalnetworks?Neuronalcomputationsarecon- At first, this response seems tautological: We act so that we
strained by properties of the brain in the form of number of can predict the outcome of our actions; we predict that our
neurons and synapses, and space and energy consumption. The actions will be complex and interesting; and therefore we act
latter has served as an argument for sparse coding–that is, low in complex and interesting ways. The tautology is broken by
meanactivityatconstantvarianceofactivity(Barlow1961).The invoking a prior expectation on action, one presumably hard-
insight that receptive fields of simple cells in primary visual wired and selected for by evolutionary pressures. But, such an
cortex form such an optimally sparse representation of natural assumption would seem to remove the explanatory power of
imagesdrasticallyincreasedinterestinnormativemodels(Olshau- the MPE principle in describing complex behaviors. Further-
sen & Field 1996; Simoncelli & Olshausen 2001). Properties of more, it goes against the common view that the evolutionary
the second major neuron type in primary visual cortex, complex advantageofthebrainliesin theabilitytobeadaptiveandalle-
cells, can be understood along similar lines as optimizing stable viate much of the need for hardwired pre-programming (pre-
representations (Berkes & Wiskott 2005; Körding et al. 2004). expectations) of behavior. A more satisfying solution to the
Importantly, both optimization principles can be easily “Dark Room Dilemma” may potentially be found in a different
implementedbyrecurrentconnectivitywithinacorticalarea(Ein- information theoretic interpretation of the interaction between
häuseretal.2002).Hence,existingnormativemodelsoftheearly action and perception.
visualsystemareplausibleinviewofanatomicalandphysiological Clark turns to the free-energy formulation for an information
data. theoretic interpretation of the MPE principle (Friston &
Acriticaltestoftheconceptwillbetheapplicationwellbeyond Stephan 2007). Within this framework, average prediction error
processingintheprimaryvisualcortex.Thestepfromsparseness is captured by the information theoretic measure entropy,
andstabilitytopredictabilityasanoptimizationprinciplerequires which quantifies an agent’s informational cost for representing
criticalextensions.Phillipsetal.(1995)putforwardaveryprom- the sensory input by its internal model. An alternative quantifi-
isingproposal:Coherentinfomaxselectsandcoordinatesactivities cation of the predictive accuracy of an internal model would be
as a function of their predictive relationships and current rel- toconsiderits mutualinformation(MI)withthesensoryinputs.
evance. The relation of this approach (see Phillips’ commentary MIquantifiestheinformationsharedbetweentwodistributions–
in this issue) to the free energy principle (Friston 2010) and in this case, the informational content the internal states of the
optimal predictability (König & Krüger 2006) has to be investi- brain hold regarding its future sensory inputs. MI and entropy
gated. These developments hold the promise to apply to areinasenseconversesofoneanother.Entropyistheinforma-
“higher” cognitive functions as well as giving rise to a true tionalcostofa(bad)internalmodel,whileMIistheinformational
theoryofcognitivescience. gainsofa(good)internalmodel.Whenselectingamodel,mini-
mizingentropyandmaximizingMIbothyieldminimalprediction
error.Whenselectingactions,however,thesetwoprinciplesyield
verydifferentresults.
Actions allow an agent, through the sensor-motor loop, to
Maximal mutual information, not minimal
change the statistics of its sensory inputs. It is in response to
entropy, for escaping the “Dark Room” suchchangesthattheprinciplesofmaximizingMIandminimizing
entropydiffer.Thisdifferencecanbehighlightedbyahypotheti-
doi:10.1017/S0140525X12002415 calextreme,inwhichanagentacts toremoveallvariationin its
sensory inputs–that is, it dwells in a “Dark Room.” Here, a
DanielYing-JehLittleandFriedrichTobiasSommer trivial model can perfectly predict sensory inputs without any
RedwoodCenterforTheoreticalNeuroscience,UniversityofCalifornia– informationcost.Entropythusgoestozerosatisfyingtheprinciple
Berkeley,Berkeley,CA94720-3198. of minimal entropy. Similarly, MI also goes to zero in a Dark
dylittle@berkeley.edu fsommer@berkeley.edu Room.Withoutvariationinsensoryinputsthereisnoinformation
http://redwood.berkeley.edu/wiki/Daniel_Little fortheinternalmodeltotrytocapture.Thisviolatesthemaximal
http://redwood.berkeley.edu/wiki/Fritz_Sommer MIprinciple. Instead,of entering a“DarkRoom,”an agentfol-
lowing a principle of maximal MI would seek out conditions in
Abstract:Abehavioraldrivedirectedsolelyatminimizingpredictionerror which its sensory inputs vary in a complex, but still predictable,
would cause an agent to seek out states of unchanging, and thus easily
fashion. This is because MI is bounded below by the variability
predictable, sensory inputs (such as a dark room). The default to an
in sensory input and bounded above by its ability to predict.
evolutionarily encoded prior to avoid such untenable behaviors is
Thus,MIbalancespredictabilitywithcomplexity.Passively,max-
unsatisfying. We suggest an alternate information theoretic
interpretationtoaddressthisdilemma. imizing MI accomplishes the same objective as minimizing
entropy,namelythereductionofpredictionerror,butactivelyit
We would like to compliment Clark for his comprehensive and encouragesanescapefromtheDarkRoom.
insightful review of the strengths and limitations of hierarchical Theprediction–complexitydualityofMIanditsimportanceto
predictive processing and its application to modeling actions as learninghasbeenarecurringfindingincomputationalmethods.
well as perception. We agree that the search for fundamental Important early implementations of a maximal MI principle in
theoretical principles will be key in explaining and uniting the modelingpassivelearningincludetheComputationalMechanics
myriad functions of the brain. Here, we hope to contribute to approach for dynamical systems of Crutchfield and Young
the discussion by reconsidering a particular challenge to the (1989) and the Information Bottleneck Method of Tishby et al.
minimum prediction error (MPE) principle identified by Clark, (1999)foranalyzingtimeseries.Recently,theInformationBottle-
which we dub the “Dark Room Dilemma,” and by offering an neckmethodhasbeenextendedtoactionselectionbyStill(2009).
alternate solution that captures both the drive to reduce errors Further,thePredictiveInformationModelofAyetal.(2008)has
andthedrivetoseekoutcomplexandinterestingsituations. shownthatcomplexbehaviorscanemergefromsimplemanipula-
As described by Clark, a common challenge to extending the tions of action controllers towards maximizing the mutual infor-
principleofminimumpredictionerror(MPE)toactionselection mation between states. And our own work utilizes MI to drive
is that it would drive an animal to seek out a dark room where exploratorybehaviors(Little&Sommer2011).
220 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
The principle of minimum prediction error and the related forpredictivebrainprocessingbeforestimulusonsetandimpor-
hierarchical prediction models offer important insights that tant information about cortico-cortical communication would
should not be discounted. Our aim is not to suggest otherwise. remainconcealed.Motivatingthesearchforpredictivesignalsin
Indeed, we favor the view that hierarchical prediction models thesystemisthereforeanotherimportantcontributionofthecon-
could explain the motor implementation of intended actions. ceptualframework.
But we also believe its explanatory value is limited. Specifically, Concrete level description. On the concrete conceptual level,
it would be desirable for a theoretical principle of the brain hierarchical cortical prediction provides a scaffold on which we
to address and not spare the intriguing question of what can constrain variants of predictive coding models. Predictions
makesanimals,eventhesimplestones,ventureoutoftheirdark are proposed to explain away the incoming signal or filter away
rooms. the unexpected noise (Grossberg 2013). Rao and Ballard (1999)
proposed a model in which forward connections convey predic-
tionerrorsonly,andinternalmodelsareupdatedonthebasisof
the prediction error (Rao & Ballard 1999). Grossberg on the
otherhandproposesAdaptive ResonanceTheory(ART)models
Backwards is the way forward: Feedback in
that update internal models based on recognition error. It
the cortical hierarchy predicts the expected remains an empirical question which combination of these
future models suffices to explain the rich and diverse cortical response
properties. A recent brain imaging study shows that under con-
doi:10.1017/S0140525X12002361 ditionsoffacerepetition,somevoxelsshowrepetitionsuppression
consistent with the concept that the prediction error is reduced
LarsMuckli,LucyS.Petro,andFraserW.Smith with every repetition of the identical image, while others (30%)
CentreforCognitiveNeuroimaging,InstituteofNeuroscienceandPsychology, show repetition enhancement (De Gardelle et al. 2012). Rep-
UniversityofGlasgow,GlasgowG128QB,UnitedKingdom. etition enhancement in a subpopulation of fusiform face area
Lars.Muckli@glasgow.ac.uk lucyp@psy.gla.ac.uk (FFA)voxelscouldreinforcetheinternalmodelofthefaceiden-
Fraser.Smith@glasgow.ac.uk http://muckli.psy.gla.ac.uk/ tity and be used to stabilize the prediction. The claim that the
brain is a prediction machine might be true regardless of the
Abstract:Clarkoffersapowerfuldescriptionofthebrainasaprediction preciseimplementationofpredictivecodingmechanism.Internal
machine,whichoffersprogressontwodistinctlevels.First,onanabstract modelsmightupdateonerror,stabilizeonconfirmationorscruti-
conceptuallevel,itprovidesaunifyingframeworkforperception,action, nize on attention (Hohwy 2012). A recent brain imaging study
andcognition(includingsubdivisionssuchasattention,expectation,and
investigated whether expectation induced signal suppression
imagination). Second, hierarchical prediction offers progress on a
coincideswithsharpeningoftheunderlyingneuronalcode(Kok
concrete descriptive level for testing and constraining conceptual
et al. 2012). Consistent with the predictive coding framework,
elements and mechanisms of predictive coding models (estimation of
predictions,predictionerrors,andinternalmodels). auditory-cuedstimuliledtoreducedV1fMRIactivity.Although
the overall activity was reduced, the activation profile was more
Abstractleveldescription.Understanding the brain as a predic- distinct, “sharpened,” for the expected conditions as measured
tion machine offers a compelling framework for perception, using multivariate decoding analysis. The study concludes that
action, and cognition. Irrespective of the neuronal implemen- expectationhelpstoexplainawaythesignalwhileattentionampli-
tation,theframeworkascribesafunctiontointernalmodelsand fies the remaining prediction error (Hohwy 2012; Spratling
neuronalprocessestobestpreparefortheanticipatedfuture.At 2008b).
an abstract level, the predictive coding framework also draws Another concrete level aspect of predictive coding relates to
attentiontotwoblindspotsinneuroscience:(1)internalcortical the question of spatial precision. Are the back-projected predic-
communication (i.e., maintaining internal models) and (2) the tions at the precision level of the “sending” brain area (i.e.,
brain processes prior to stimulation onset (i.e., predictive coarse), or at the precision level of the “receiving” brain area
processing). (i.e., spatially precise)? We have evidence in favor of both; V5
Astartingpointtoexploreinternalcommunicationisbyinves- feedback signals spread out to a large region in primary visual
tigatingcorticalfeedback(VanEssen2005;Muckli&Petro2013). cortex (de-Wit et al. 2012; Muckli et al. 2005) but spatio-tem-
Conventional paradigms struggle, however, to isolate cortical poral predictions in V1 which have been relayed by V5 can
feedbackduringsensoryprocessing(whichincludesbothfeedfor- also be spatially precise (Alink et al. 2010). The optimal way to
ward and feedback information). We have demonstrated such account for this discrepancy is by assuming an architecture that
separationbyblockingfeedforwardstimulationusingvisualocclu- combinescoarsefeedbackwiththelateralspreadoffeedforward
sion and reading out rich information content (multivariate pat- signals (Erlhagen 2003). If this principle holds true, it helps to
terns) from within non-stimulated regions of the retinotopic explain why the architecture of cortical feedback as described
cortex (which receive cortical feedback activation; Muckli & by Angelucci et al. (2002) contributes to precise predictions
Petro2013;Smith&Muckli2010).Bydecodingcorticalfeedback, even though it is divergent.
we begin to shed light on internal processing. With regard to The examples above show that on an abstract level important
investigating brain processes prior to stimulationonset, we have new research is motivated by the hierarchical predictive coding
shownthatmotionpredictionsarecarriedovertonewretinalpos- framework and on a concrete conceptual level, the many inter-
itions after saccadic eye-movements (Vetter et al. 2012), which actions of cortical feedback of predictions, processing of predic-
confirms that saccadic updating incorporates predictions gener- tion errors, and different accounts of feedforward connections
ated during pre-saccadic perception. This is an important proof (some stabilizing the internal model, others explaining away
of concept of predictive coding in saccadic viewing conditions. signal discrepancies) await further empirical scrutiny. However,
Moreover, Hesselmann et al. (2010), have shown that variations the developing narrative of predictive coding becomes increas-
in baseline activity influence subsequent perception, and a inglycompellingwithattentionfromsophisticatedhumanneuroi-
causal role of V5 in generating predictions sent to V1 can be maging and animal neurophysiological studies (Muckli & Petro
demonstrated using transcranial magnetic stimulation (TMS). 2013).Notonlyisextendingourknowledgeofcorticalfeedback
Pilot data show that TMS interferes with predictive codes anditsencapsulatedpredictionsessentialforunderstandingcorti-
during the baseline prior to stimulation onset (Vetter et al., calfunction,butimportantopportunitieswillarisetoinvestigate
under revision). If the brain would be seen as a “representation deviationsofpredictivecodinginagingandneuropsychiatricdis-
machine”insteadofa“predictionmachine,”onewouldnotlook easessuchasschizophrenia(Sandersetal.2012).
BEHAVIORALANDBRAINSCIENCES(2013)36:3 221
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Skull-bound perception and precision there and then to ensure optimal encoding. Precisely because
optimization through culture the mind is destined to be behind the veil of sensory input,
itthenmakessenseforittodevisewaysofoptimizingtheinfor-
doi:10.1017/S0140525X12002191 mation channel from the world to the senses. Thus, through
activeinferencepredictionerrorisminimized,notonlybyselec-
BryanPaton,aJoshSkewes,bChrisFrith,candJakobHohwya tive sampling, but also by optimizing its precision: removing
aPhilosophyandCognitionLaboratory,PhilosophyDepartment,Monash sourcesofnoiseintheenvironmentandamplifyingsensoryinput.
University,Clayton,VIC3800,Australia;bDepartmentofCultureandSociety, Manyofthetechnical,socialandculturalwaysweinteractwith
AarhusUniversity,DK8000AarhusC,Denmark,andInteractingMindsCentre, the world can be characterized as attempts to make the link
AarhusUniversityHospital,DK8000AarhusC,Denmark;cInstituteof betweensensoryinputandenvironmentalcauseslessvolatile.We
Neurology,UniversityCollegeLondon,London,WC1E6BT,andAllSouls see this in the benefits of the built environment (letting us
College,OxfordUniversity,OxfordOX14AL,UnitedKingdom. engageinactivitiesunperturbedbywindandweather),intechnical
Bryan.Paton@monash.edu filjcs@hum.au.dk c.frith@ucl.ac.uk andelectronicdevices(radioletsushearthingsdirectlyratherthan
Jakob.Hohwy@monash.edu through hearsay), and in language (communicating propositional
https://sites.google.com/site/bryanpaton/home content). This picture relies on the internal nature of the neural
http://www.cfin.au.dk/menu538-en
mechanism that minimizes prediction error, relative to which all
https://sites.google.com/site/chrisdfrith/Home ourculturalandtechnologicaltrappingsareexternal.Cultureand
https://sites.google.com/site/jakobhohwy/ technologysituatethemindclosertotheworldthroughimproving
the reliability of its sensory input. But perception remains an
Abstract:Clarkacknowledgesbutresiststheindirectmind–worldrelation
inferredfantasyaboutwhatliesbehindtheveilofinput.
inherentinpredictionerrorminimization(PEM).Butdirectnessshouldalso
Bymaintainingfocusontheinternalnatureofperceptualpro-
beresisted.Thiscreatesapuzzle,whichcallsforreconceptualizationofthe
cesses,inthiscausalsetting,wecanappreciateanotherperspec-
relation.Wesuggestthatacausalconceptioncapturesbothaspects.With
this conception, aspects of situated cognition, social interaction and tive on social interaction and culture than the “mutual
culturecanbeunderstoodasemergingthroughprecisionoptimization. predictionerrorreduction”thatClarkrightlypointsto.
AsLockeinsisted,communicationisthesharingofeachother’s
AndyClarkacknowledgesthe“challengingvision”ofpredictionerror hiddenideas.Ideasarewell-hiddencauses,soPEMisthetoolfor
minimization(PEM),accordingtowhichrepresentationisinnerand inferring them through a mix of prediction (“after saying A, he
skull-bound such that perception is a fantasy that coincides with tendstosayB”)andactiveinference (askingsomethingtoelicita
reality (Frith 2007). This view does not require homunculi and predictedanswer).Anoverlookedaspecthereishowthisisfacili-
sense-databutdoesconveyasomehowindirectmind–worldrelation. tatednotjustbyrepresentingtheother’smentalstatesbutalsoby
Clarkresistsindirectness.HestatesthatPEM“makesstructur- aligningourmentalstateswitheachotherinaprocessofneuralher-
ing our worlds genuinely continuous with structuring our brains meneutics–a fusion of expectation horizons. We do this, not to
andsculptingouractions”(sect.3.4,para.1),andthat“whatwe change thesensoryinputitself,buttoenhance theprecisionwith
perceive is not some internal representation or hypothesis but whichwecanprobeeachother’scurrentmentalstates,perhapsto
(precisely)theworld”(sect.4.4,para.3,emphasisClark’s). such an extent that the receiver in a social interaction ends up
Thesentimentisright,butcautionaboutdirectnessisneeded. having more precise information about the sender’s mental states
Withoutindirectnessweignorehowthemindisalwaysprecariously thanthesenderhim-orherself(Frith&Wentzer,inpress).
hostagetotheurgetoriditselfofpredictionerror.Thisurgeforces Perhapsculturetoo,inaverywidesense,canbeseenas,atleast
veryimprobableandfantasticalperceptionsuponuswhentheworld partly, a tool for precision optimization through shared context.
doesnotcollaborateinitsusual,uniformway.Forexample,inthe Ritual,convention,andsharedpracticesenhancemutualpredict-
contemporary swathe of rubber-hand and full-body illusions, we ability between people’s hidden mental states. This wouldmake
easilyandcompellinglyexperiencehavingarubberhand(ortwo), sense of cultural diversity because this process is concerned
occupyinganother’sbodyoralittledoll’sbody,orhavingmagnetic with signal reliability rather than with what the signals are
forces or spectral guns operating on our skin (Hohwy & Paton about, and there are many different ways of using cultural tools
2010;Lenggenhageretal.2007;Petkova&Ehrsson2008).More- to align our mental states. Furthermore, when precision has
over, more stable and fundamental aspects of mind, such as our been optimized, alignment enables simple, information rich sig-
senseofagency,privilegedaccesstoself,andmentalizing,allseem nalingandtherebycommunicationefficiency.
tomakesenseonlyintermsofperceptualfantasizing(Frith2007). Ifalignmentofmentalstatesisanintegralpartofhowculture
Thisleavesapuzzle.OnPEM,theperceptualrelationcannotbe optimizes precision and communication efficiency, then culture
direct. But neither is it wholly indirect. The challenge is then to shouldbeseenasprovidingasetofframeworksforinterpretation,
reconceive the mind–world relation to encompass both aspects. ratherthanmerelyforscaffoldinginterpretation.Ifthebrainisa
Wesuggestacausalconception,anduseitsinternalaspecttolever- hierarchical Bayesian network providing a perceptual fantasy of
ageanunderstandingofsituatedandsocialcognition. theworld,thenculturedeterminesandconstrainsthehyperpriors
Theimplicitinversionofagenerativemodelhappenswhenpredic- neededbysuchaneuralsystem.
tionerrorisminimizedbetweenthemodelmaintainedinthebrain
andthesensoryinput(howtheworldimpingesonthesenses).This
yieldscausalinferenceonthehiddencauses(thestatesofaffairsin
theworld)ofthesensoryinput.Thisisadistinctlycausalconception
ofhowthebrainrecapitulates–providesamultilayeredmirrorimage Neuronal inference must be local, selective,
of–thecausalstructureoftheworld.Thisrepresentationalrelationis and coordinated
direct in the sense that causation is direct: There is an invariant
relation between the model and world, such that, given how the doi:10.1017/S0140525X12002257
model is, it changes in certain ways when the world changes in
certainways.But,seenfromtheinside,thereisindirectnessinthe WilliamA.Phillips
sensethatcausalrelataaredistinctexistences,givingrisetoaneed PsychologyDepartment,UniversityofStirling,FK94LAStirling,Scotland,
forcausalinferenceonhidden,environmentalcauses. UnitedKingdom,andFrankfurtInstituteofAdvancedStudies,60438Frankfurt
Though the brain can optimize precisions on its prediction amMain,Germany.
error, it is hostage to the causal link from environmental causes wap1@stir.ac.uk
to sensory input. If the variance in the signal from the world to http://www.psychology.stir.ac.uk/staff/staff-profiles/honorary-staff/bill-
the senses is large, then there is only so much the brain can do phillips
222 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Abstract: Life is preserved and enhanced by coordinated selectivity in relevance. This is emphasized by the theory of Coherent
local neural circuits. Narrow receptive-field selectivity is necessary to Infomax (Kay et al. 1998; Kay & Phillips 2010; Phillips et al.
avoid the curse-of-dimensionality, but local activities can be made 1995), which synthesizes evidence from neuroanatomy, neuro-
coherent and relevant by guiding learning and processing using broad physiology, macroscopic neuroimaging, and psychophysics (Phil-
coordinating contextual gain-controlling interactions. Better
lips & Singer 1997; von der Malsburg et al. 2010). That theory
understanding ofthe functionsand mechanisms of thoseinteractions is
is further strengthened by evidence from psychopathology as
thereforecrucialtotheissuesClarkexamines.
reviewed by Phillips and Silverstein (2003), and extended by
MuchinClark’sreviewisoffundamentalimportance.Probabilistic manysubsequentstudies.KördingandKönig(2000)arguefora
inferenceiscrucialtolifeingeneralandneuralsystemsinparticular, closelyrelatedtheory.
butdoesithaveasinglecoherentlogic?Jaynes(2003)arguedthatit Free-energy theory (Friston 2010) and Coherent Infomax
does,butforthatlogictoberelevanttobraintheory,itmustbe assumethatgoodpredictionsarevital,andformalizethatassump-
shown how systems built from local neural processors can tionasaninformationtheoreticobjective.Thoughthesetheories
performessentialfunctionsthatareassumedtobetheresponsibility
havesuperficialdifferences,withCoherentInfomaxbeingformu-
ofthescientistinJaynes’theory(Fiorillo2012;Phillips2012). latedattheneuronalratherthanthesystemlevel,itmaybeposs-
Mostcrucialofthosefunctionsareselectionoftheinformation ible to unify their objectives as that of maximizing prediction
relevanttotheroleofeachlocalcellormicrocircuitandcoordi- success,which,underplausibleassumptions,isequivalenttomini-
nation of their multiple concurrent activities. The information mizingpredictionerror(Phillips&Friston,inpreparation).For-
available to neural systems is so rich that it cannot be used for mulatingtheobjectiveasmaximizingtheamountofinformation
inference if taken as a single, multi-dimensional whole because correctly predicted directly solves the “dark-room” problem dis-
the number of locations in multi-dimensional space increases cussed by Clark. That objective, however, does not necessarily
exponentially with dimensionality. Most events that actually implythatpredictionerrorsarethefundamentalcurrencyoffeed-
occurinhigh-dimensionalspacesarethereforenovelanddistant forwardcommunication.Inferencescouldbecomputedbyredu-
frompreviousevents,precludinglearningbasedonsampleprob- cing prediction errors locally, and communicating inferences
abilities. This constraint, well-known to the machine-learning more widely (Spratling 2008a). That version of PC is supported
community as the curse-of-dimensionality, has major conse- by much neurobiological evidence, though it remains possible
quences for psychology and neuroscience. It implies that for thatneuralsystemsusebothversions.
learning and inference to be possible large data-bases must be Anotherimportantissueconcernstheobviousdiversityofbrains
dividedintosmallsubsets,asamplyconfirmedbytheclearselec- andcognition.Howcouldanyunifyingtheorycastlightonthat?
tivityobservedwithinandbetweenbrainregionsatallhierarchical Though possible in principle, detailed answers to this question
levels.Creationofthesubsetsinvolvesbothprespecifiedmechan- arelargelyahopeforthefuture.CoherentInfomaxhypothesizes
isms,asinreceptivefieldselectivity,anddynamicgroupingaspro- a local building-block from which endlessly many architectures
posedbyGestaltpsychology(Phillipsetal.2010).Thecriteriafor couldbebuilt,butuseofthattoenlightentheobviousdiversity
selection must be use-dependentbecause information crucial to is a task hardly yet begun. Similarly, though major transitionsin
one use would be fatal to another, as in the contrast between the evolution of inferential capabilities seem plausible, study of
dorsal and ventral visual pathways. Contextual modulation is what they may be remains a task for the future (Phillips 2012).
also crucial because interpretations with low probability overall By deriving algorithms for learning, Coherent Infomax shows in
may have high probability in certain contexts. Therefore, the principlehowendlessdiversitycanarisefromdiverselives,andit
activity of local processors must be guided by the broader hasbeenshownthattheeffectivenessofcontextual-coordination
context,andtheirmultipleconcurrentdecisionsmustbecoordi- varies greatly across people of different ages (Doherty et al.
nated if they are to create coherent percepts, thoughts, and 2010), sex (Phillips et al. 2004), and culture (Doherty et al.
actions. 2008).Useofthispossiblesourceofvariabilitytoenlightendiver-
Mostmodelsofpredictivecoding(PC)andBayesianinference sityacrossandwithinspeciesstillhasfartogo,however.
(BI)assumethattheinformationtobecodedandusedforinfer- Overall, Iexpect theories such as those examined by Clark to
enceisagiven.Inthosemodels,itis–bythemodelers.Modelers have far-reaching consequences for philosophy, and human
mayassumethatintherealworldthisinformationisgivenbythe thought in general, so I fully endorse the journey on which he
externalinput,butthatprovidesmoreinformationthancouldbe hasembarked.
usedforinferenceiftakenasawhole.Self-organizedselectionof
the information relevant to particular uses is therefore crucial.
Efficientcodingstrategies,suchasPC,areconcernedwithways
oftransmittinginformationthroughahierarchy,notwithdeciding
God,thedevil,andthedetails:Fleshingoutthe
what information to transmit. They assume lossless transmission
predictive processing framework
ofallinputinformationtobethegoal,andsoprovidenowayof
extracting different information for different uses. Models using
BI show how to combine information from different sources doi:10.1017/S0140525X12002154
when computing a single posterior decision; but they do not
DanielRasmussenandChrisEliasmith
show how local neural processors can select the relevant infor-
mation, nor do they show how multiple streams of processing CentreforTheoreticalNeuroscience,UniversityofWaterloo,Waterloo,ONN2L
can coordinate their activities. Thus, local selectivity, dynamic- 3G1,Canada.
grouping, contextual-disambiguation, and coordinating inter- drasmuss@uwaterloo.ca celiasmith@uwaterloo.ca
actions are all necessary within cognitive systems, but are not
Abstract: The predictive processing framework lacks many of the
adequatelyexplainedbytheessentialprinciplesofeitherPCorBI.
architecturalandimplementationaldetailsneededtofullyinvestigateor
Clark’s review, however, does contain the essence of an idea evaluatetheideasitpresents.Onewaytobegintofillinthesedetailsis
that could help resolve the mysteries of selectivity and coordi- by turning to standard control-theoretic descriptions of these types of
nation,thatis,context-sensitivegain-control,forwhichthereare systems (e.g., Kalman filters), and by building complex, unified
severalwidely-distributedneuralmechanisms.Acrucialstrength computationalmodelsinbiologicallyrealisticneuralsimulations.
of the free-energy theory is that it uses gain-controlling inter-
actions to implement attention (Feldman & Friston 2010), but Godisinthedetails
such mechanisms can do far more than that. For example, they —MiesvanderRohe
can selectand coordinateactivities by amplifyingorsuppressing Thedevilisinthedetails
them as a function of their predictive relationships and current —Anonymous
BEHAVIORALANDBRAINSCIENCES(2013)36:3 223
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Despite their theologically contradictory nature, both of these processingframework uses the prediction error signal to update
statementsaretrue:thefirstisnotingthatdetailsareimportant, its representations). Clark claims that the predictive processing
and the second that getting the details right is difficult. It is for framework differs from these structures in that it contains a
exactlythispairofreasonsthatwebelievethepredictiveproces- richer error signal (see Note 9 in the target article). However,
singframeworkislimitedinitsabilitytocontribute,inadeepway, the Kalman filter is often employed in a multidimensional form
toourunderstandingofbrainfunction. (Villalon-Turrubiates et al. 2004; Wu 1985), allowing the error
This is not to deny that the brain does prediction. This is a signal to encode rich and complex information about the world.
view that has been beautifully articulated by Clark, and lies in Makinguseoftheseparallelsprovidesmanypotentialadvantages.
a great tradition. For instance, in his 1943 book, Kenneth For example, Clark describes the need to adjust the relative
Craik devotes several chapters to his central hypothesis that: weight of the model’s predictions versus the incoming infor-
“One of the most fundamental properties of thought is its mation, but he does not indicate how that balance is to be
power of predicting events” (Craik 1943, p. 50). The evidence achieved. This is a well-studied problem in Kalman filters,
for prediction-related signals is strong, and the high-level where there are specific mechanisms to adjust these weights
models are often tantalizing. However, we (and, in our experi- depending on the measurement or estimate error (Brown &
ence, most neuroscientists) want more: We want specific Hwang1992).Thus,itmaybepossibletoreplacethepoorlyspeci-
neural mechanismsthat areemployed in specific circumstances, fiednotionof“attention”usedtocontroltheseweightsinthepre-
and we want to know how such models can be arranged to dictive processing framework (sect. 2.3) with well-defined
explain complex behavior (i.e., we want an architectural mechanisms, providing a more grounded and concrete
specification). description.
Unfortunately,asClarkhimselfpointsout,thepredictivepro- Thisisawayofprovidingcomputationaldetailstotheapproach,
cessingframework“fail[s]tospecifytheoverallformofacogni- but we advocate going further–providing implementational
tive architecture” and “leaves unanswered a wide range of details as well. For instance, there is more than one way to
genuine questions concerning the representational formats implementaKalmanfilterinaspikingneuralnetwork(Eliasmith
used by different brain areas” (sect. 3.3, para. 4). The extent of &Anderson2003,Ch.9),eachofwhichhasdifferentimplications
the predictive processing framework’s architectural claims is for the neurophysiological behavior of those networks. Once a
that the brain is organized in a hierarchical manner, with error neural implementation has been specified, detailed comparisons
signals passing up the hierarchy and predictions of world state betweencomputationalmodelsandempiricaldatacanbemade.
passing down. However, this description seems to miss all the Morecritically,forthegrandersuggestionthatthepredictivepro-
interesting details: What is the specific form and function of cessingframeworkisunifying,theimplementationofsomesmall
the connections between levels of this hierarchy? In the setofmechanismsshouldexplainawideswathofempiricaldata
human brain, along what neuroanatomical pathways should we (see, e.g., Eliasmith et al. [2012] or Eliasmith [in press] for one
expect to see this information flowing? And, more generally, suchattempt).
how do different hierarchies interact? How does information TheideaspresentedbyClarkarecompelling,compatiblewith
pass between them? Is there a unifying representational empiricaldata,andattempttounifyseveralinterestingaspectsof
format? The predictive processing framework leaves all of cognition. However, given the current lack of implementational
these details unspecified, but it strikes us that the filling-in of detailorfirmarchitecturalcommitments,itisimpossibletodeter-
thesedetailsiswheretheframeworkwouldgaindeep,empirical mine whether the predictive processing framework is largely
content. correct or empirically vacuous. The real test of these ideas will
It may seem as if some of these questions are answered. For comewhentheyareusedtobuildamodelthatunifiesperception,
instance,theprimarymethodofrepresentationinthebrainissup- cognition,andactioninasinglesystem.Suchaneffortwillrequire
posedtobethroughprobabilitydensityfunctionsacrosstheposs- adeeperinvestigationofthedetails,andeitherfilltheminwith
ible states/concepts. However, as Clark mentions, these answers, or if answers are not to be found, require a reworking
representations could be implemented with a “wide variety of of the theory. Either way, the predictive processing framework
different schemes and surface forms” (sect. 3.2, para. 4). For willbenefitenormouslyfromtheexercise.
example,aprobabilitydensityp(x)couldberepresentedasahis-
togram (whichexplicitly stores howmany times each statex has NOTE
occurred) or as a summary model (e.g., storing just the mean 1. We have in mind here all the varieties of Kalman filters (e.g.,
extended,unscented,etc.).
and variance of a normal distribution). These different schemes
have enormously different resource implications for a physical
implementation.Aslongasthecharacterizationofrepresentation
isleftatthelevelofspecifyingageneral,abstractform,itisdiffi-
culttoempiricallyevaluate. Interactively human: Sharing time,
Evenwhatseemstobethemostspecificclaimofthepredictive constructing materiality
processing framework–that there exist functionally distinct
“error” and “representation” units in the brain–is ambiguous. doi:10.1017/S0140525X12002427
Given multidimensional neuron tuning (Townsend et al. 2006;
Tudusciuc& Nieder2009),unitscouldbesimultaneouslysensi- AndreasRoepstorff
tive to both error and representation, and still perform the rel- InteractingMindsCentre,andCentreforFunctionallyIntegrative
evant computations (Eliasmith & Anderson 2003). This would Neuroscience,InstituteofCultureandSociety,AarhusUniversity,DK-8000
be compatible with the neurophysiological evidence showing AarhusC,Denmark.
neurons responsive to prediction error, without requiring that andreas.roepstorff@hum.au.dk
there be a sharp division in the brain into these two different
sub-populations.Again,thedetailsmatter. Abstract: Predictive processing models of cognition are promising an
Onewaytobegintofillinthemissingdetailsinthepredictive elegant way to unite action, perception, and learning. However, in the
processingframeworkisbybeingmorespecificastowhatfunc- current formulations, they are species-unspecific and have very little
tions are computed. For example, Kalman filters1 (Kalman particularly human about them. I propose to examine how, in this
framework, humans can be able to massively interact and to build
1960) are standard control-theoretic structures that maintain an sharedworldsthatarebothmaterialandsymbolic.
internal representation of the state of the world, and then use
thedifferencebetweenthepredictionsofthatinternalstateand AndyClarkhaswrittenanimpressivepiece.Predictiveprocessing
incoming data to update the internal model (as the predictive ideas have been the hype in the neurocognitive community for
224 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
some years, for all the reasons that the target article’s review and that the dimensions of materiality “we” can spin ourselves
identifies. They propose to unify models of perception, action, into seem to be constantly changing. Humans appear to live
andlearningwithinaframework–whichiselegant,alignedwith liveswherebothpriorsand possibilitiesforaction–andperhaps
neuroanatomical and functional findings, computationally plaus- also, increasingly, the world–are shaped by actions of others
ible, and able to generate empirical research with relatively and constrained, stabilised, and afforded by those structures
clearhypotheses. built in the process. But if “being human” in general is about
Sofartheideashavebeenawell-keptsecretwithinthecommu- livinginunfoldedpractices,what,then,isitaboutourcognition
nity.ThisBBSarticleislikelytochangethat.Asoneofthefirst, that allows us to do that? We don’t know. But something about
Clark brings the predictive processing framework in touch with howhumanscanbridgethematerialandthesymbolic,andsome-
more general views in cognition and philosophy of mind in a thingabouthowtheyinandthroughinteractionscanshareboth
formatavailabletoawideraudience.Strippingitofthemathemat- externalandinternaltime,maybecritical.
ical formality without losing out on the conceptual stringency, The predictive framework, in “linking action, perception, and
opens for a wider discussion of potential implications for how learning,” is highly relevant also to researchers outside of the
wethinkofthebrainandofourselves.Keytermslikeanticipation, neurosciences. But at this stage, there is much to fillin for itto
expectancy, models of reality, attention, agency, and surprise functionasageneralmodelofhumancognitionandaction.Cer-
appeartomoveseamlesslybetweentheneuronal,themathemat- tainly,thefreeenergyprinciple,thepredictivehierarchicalstuff,
ical,thephenomenological,andthebehavioral.Theambitionto theputativelinksbetweenaction,perception,andlearningseem
extendthistoageneralmodelofhumancognitionisimpressive, tobegoodcandidatesforthenew“roughguide”tobrainfunction.
butthisisalsowheretheproposalbecomesveryopen-ended.For, However,theseguidingprinciplesappeartoworkequallywellin
ultimately, how human-specific is this predictive framework? In rats,inmacaques,andinhumans.Forthoseofuswhoareparticu-
the current formulation, hardly at all. The underlying neural larlyinterestedinwhathumansdotothemselves,toeachother,
models are basically species-unspecific, and the empirical cases and to their world, there seem to be a lot of lacunae to be
move back and forth between many different model systems. explored, and a lot of gaps to be filled. Getting these right may
This is not a weakness of the framework; on the contrary, the perhapsalsoteachsomethingaboutwhathumans,asinteractive
ambitionistolayoutageneraltheoryofbrainfunction,cortical agents, embedded in sociocultural worlds, may do to their
responses, predictive coding, free energy, and so forth. brains. Will this throw new light on neuroscience too? Perhaps.
However, it leaves a lot of work open when gauging how this There is certainly much work to be done by researchers from
relatestoaspecificunderstandingofhumanactionandcognition. manydisciplines.
To begin this, one may need to ask what is characteristic of
humans as a life form? We don’t knowfor sure, but there are a
few candidates. One is an unusual ability for interaction–
people coordinate, couple, take turns–at many different levels
(Levinson 2006). Through interactions, they come to share a Action-oriented predictive processing and the
structuringofactivitiesintime,and,perhaps,bringbraininternal neuroeconomics of sub-cognitive reward
processes in sync too. Another, probably not unrelated, is an
amazingabilitytoco-constructartefactsandbuildsharedworlds doi:10.1017/S0140525X12002166
that are at the same time material and symbolic (Clark 2006b;
Roepstorff2008):worldsthatexistoutsidetheindividual,andin DonRoss
time-windows,whichextendsbeyondthehere-and-nowofinter- SchoolofEconomics,UniversityofCapeTown,Rondebosch7701,Cape
action;worldsthat,somehow,getinternalized.Arethesetwoprin- Town,SouthAfrica.
ciples uniquely human? Probably not: Other species also don.ross@uct.ac.za http://uct.academia.edu/DonRoss
coordinateactions,andotherspeciesalsomodifytheirsurround-
ings,buildingnichesthatarebothmaterialandcognitive,butthe Abstract: Clark expresses reservations about Friston’s reductive
degreetowhichpeopledoitisamazing,andwestillneedtofigure interpretation of action-oriented predictive processing (AOPP) models
of cognition, but he doesn’t link these reservations to specific
outhowthiscancomeabout,alsoatacognitivelevel.
Insociologyandanthropology,oneinfluentialattempttorelate alternatives. Neuroeconomic models of sub-cognitive reward valuation,
which, like AOPP, integrate attention with action based on prediction
interactions and the co-constructed shared worlds has been a
error, are such an alternative. They interpret reward valuation as an
focus on human practices (Bourdieu 1977; Roepstorff et al. inputtoneocorticalprocessinginsteadofreducingit.
2010) as particular unfoldings of temporality set within specific
materialities.Translatedintopredictivecodinglingo,theseprac- Clark impressively surveys the prospects, based on current evi-
ticesmayhelpestablishpriorsorevenhyperpriors,setsofexpec- dence and speculations tethered to clearly specified models,
tationsthatshapeperceptionandguideaction(Roepstoff&Frith that action-oriented predictive processing (AOPP) accounts of
2012).Followingfromthis,humanpriorsmaynotonlybedriven cortical activity offer the basis for a deeply unified account of
bystatisticalpropertiesintheenvironment,pickedupbyindivid- perception, cognition, and action. It is indeed clear that such
ualexperience,orhardwiredintothedevelopingcognitivesystem. accountsprovide,attheveryleast,afreshandstimulatingframe-
They are also a result of shared expectations that are communi- work for explaining the apparently expectation-driven nature of
cated in interactions, mediated by representations, solidified perception. And once one gets this far, it would be a strangely
through materiality, and extended into an action space, going timidmodelerwhodidnotseevalueinexploringthehypothesis
way beyond the physical body and into proximal and distal that such perception was closely linked to preparation of action
formsoftechnology. and to monitoring of its consequences. However, Clark struc-
This means that both the “predictive” and the “situated” in tures his critical discussion around the most ambitious efforts
Clark’s title may get a radical twist. It is not so much a matter to use AOPP as the basis for a reductive unification of “all
of living inside a “socio-cultural cocoon,” as Clark puts it (sect. elements of systemic organization” in the brain (sect. 1.6, para.
5.2, para. 4). This metaphor suggest that we will at some point 3), efforts mainly associated with the work of Karl Friston and
grow up and come out of the cocoon into the real world. It is his co-authors. Clark expresses some reservations about this
alsonotjustamatterof“man”as“ananimalsuspendedinwebs strong, over-arching hypothesis. My commentary amplifies
ofsignificancehehimselfhasspun,”asCliffordGeertz(1966),fol- some of these reservations, based on neglect of the role of
lowing Max Weber, famously suggested. This formulation over- specialized subsystems that may integrate valuation, attention,
emphasizes the symbolic and the individualistic, and it fails to and motor preparation semi-independently of general cortical
see that the webs“we”have spun areindeedalso verymaterial, processing.
BEHAVIORALANDBRAINSCIENCES(2013)36:3 225
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Clark’s survey is notable for the absence of any discussion of generalcognition,allowsustostraightforwardlymodelthediscon-
relative reward-value computation. Studies of such valuation nect Clark identifies between surprise to the brain (“surprisal”)
based on single-cell recordings in rat striatum were the original andsurprisetotheagent.Clark’sexampleisofasurprise-minimiz-
locus of models of neural learning as adjustment of synaptic ingperceptualinferencethatsurprisestheagent.Butdisconnects
weights and connections through prediction-error correction intheotherdirectionarealsoimportant.Gamblingaddictionmay
(Schultz et al. 1997). The temporal difference (TD) learning resultfromthefactthatthemidbrainrewardcircuitisincapable
that has been progressively generalized in descendents of of learning that there is nothing to learn from repeatedly
Schultzetal.’smodelisaformofRescorla-Wagnerconditioning, playingaslotmachine,evenafterthemechanism’svictim/owner
notBayesianequilibration,andsocouldnotplausiblybeexpected hasbecomesadlyawareofthistruth(Rossetal.2008).
toprovideageneralaccountofmammaliancognition.However, Thesuggestionhereisthatneuroeconomicsisoneresource–of
neuroeconomists have subsequently embedded TD learning in course we should expect there to be others–for addressing
modelsof widerscopethat exploit driftdiffusionand meta-con- Clark’s concern that “even taken together, the mathematical
ditioning to track such complex targets as stochastic dominance model(theBayesianbrain)andthehierarchical,action-oriented,
of strategies in games with shifting mixed-strategy equilibria predictive processing implementation fail to specify the overall
(Glimcher2010;Lee&Wang2009).Suchmodelscaneffectively form of a cognitive architecture. They fail to specify, for
approximateBayesianlearning.However,asClarkreports,Fris- example, how the brain … divides its cognitive labors between
ton’s most recent work “looks to involve a strong commitment multiple cortical and subcortical areas” (sect. 3.3, para. 4). But
… to the wholesale replacement of value functions, considered in that case it seems most natural to join the neuroeconomists
as determinants of action, with expectations … about action” inunderstandingsub-cognitivevaluationasaninputtocognition,
(seeNote12inthetargetarticle). ratherthanassomethingthatamodelofcognitiveactivityshould
Onetheorist’seliminationisfrequentlyanothertheorist’scon- reduceaway.
struct implementation. Neuroeconomic models of the striatal
dopamine circuit do away with the need to posit learned or
innaterewardvaluehierarchiesthatprovidetargetsforthelearn-
ingofactionandthetrainingofattention.LikeAOPPtheory,such
Affect and non-uniform characteristics of
models effectively fuse attentional capture and entrenchment
withreward,explainingbothasfunctionalproductsofthepredic- predictive processing in musical behaviour
tion error learning encoded by dopamine signals. Extensions of
neuroeconomic models to account for pathologies of attention doi:10.1017/S0140525X12002373
andvaluation,suchasaddiction,haveincorporatedevidencefor
direct dopaminergic/striatal signaling to motor preparation RebeccaS.Schaefer,KatieOvery,andPeterNelson
areas. For example, Everitt et al. (2001) suggest that direct InstituteforMusicinHumanandSocialDevelopment(IMHSD),ReidSchoolof
signals to motor systems to prepare to consume addictive Music,UniversityofEdinburgh,EdinburghEH89DF,UnitedKingdom.
targetswhenattentionisdrawntopredictorsoftheiravailability r.schaefer@ed.ac.uk k.overy@ed.ac.uk p.nelson@ed.ac.uk
arethebasisforthevisceralcravingsthat,inturn,causeaddictive http://www.ed.ac.uk/schools-departments/edinburgh-college-art/music/
preoccupation. More basically, Glimcher’s (2003) proposal to research/imhsd/imhsd-home
model some neural response using economics was originally
motivatedbyobservationsofactivityincellsthatcontroleyesac- Abstract:Theimportantrolesofpredictionandpriorexperiencearewell
establishedinmusicresearchandfitwellwithClark’sconceptofunified
cades when monkeys implement incentivized choices through
perception,cognition,andactionarisingfromhierarchical,bidirectional
gazedirection(Platt&Glimcher1999).
predictive processing. However, in order to fully account for human
Thisintegrationofattentionandneurallearningwithactionis
musical intelligence, Clark needs to further consider the powerful and
crucial in the present context, because, like the prediction variableroleofaffectinrelationtopredictionerror.
errorsmodeledinAOPP,thisallowsthemto“carryinformation
notjustaboutthequantityoferrorbut…aboutthemismatched The roles of prediction, expectation, and prior experience in
contentitself,”asClarksays(Note9ofthetargetarticle). musical processing are well established (Huron 2006; Large
So far, we might seem to have only a semantic difference et al. 2002; Meyer 1956; Narmour 1990; Phillips-Silver &
between neuroeconomics and Friston’s radical interpretation of Trainor 2008; Vuust & Frith 2008), and indeed have led to the
AOPP: Neuroeconomists take themselves to be furnishing a proposal that music has the capacity to create an environment
theoryofneuralvaluefunctions,whileFristonproposestoelimin- of minimized prediction error within individuals and within
atethem.Butthisinfactrepresentssubstantivedivergences,allof groups(e.g.,viaasteadypulse)(Overy&Molnar-Szakacs2009).
which reflect worries that Clark notes but doesn’t connect with Bayesian models have been shown to account for a range of
particularalternativeaccounts. phenomena in music perception (Temperley 2007) and have
First, consider the problem of why, if AOPP is the general been used to bring together apparently diverging datasets from
account of cognitive dynamics, animals do not just sit still in rhythm perception and production tasks (Sadakata et al. 2006).
dark rooms to maintain error-minimizing equilibria. Clark cites Moreover, it has been shown that the motor system is engaged
Friston’ssuggestioninresponsethat“somespeciesareequipped during auditory rhythm perception (e.g., Grahn & Brett 2007),
with prior expectations that they will engage in exploratory or andthatmusicalimageryevokessimilarneuralresponsesasper-
social play” (Friston 2011a; see sect. 3.2, para. 2, in the target ception(Schaeferetal.2011a;2011b).Clark’sunifiedframework
article). However, good biological methodology recommends of perception, action, and cognition is thus well supported by
against positing speculative innate knowledge as inferences to recentmusicresearch.
bestexplanationsconditionalonone’shypothesis.Theneuroeco- However,thecurrentaccountdoesnotattempttodealwiththe
nomicmodelofstriatalvaluationmakesthispositunnecessary– rangeofwaysinwhichpredictionerrorinducesarousalandaffect.
or,onanotherphilosophicalinterpretation,replacesthedubious Theextenttowhichourpredictionsaremetorviolated,histori-
IBEbyevidenceforamechanism–bysuggestingthatdiscovery cally theorized to lead to an arousal response (Berlyne 1970),
of mismatches between expectations and consequences of can make a piece of music more or less coherent, interesting,
action is the basis of phasic dopamine release, and such release and satisfying. Aesthetically, this leads to the concept of an
isthefoundationofreward,attention,andfurtheraction. optimallevelofsurprisal,which(althoughinitiallyformulatedto
Second, allowing for a relatively encapsulated and cognitively describe liking or hedonic value for differing levels of musical
impenetrable pre-frontal mechanism in striatum that integrates complexity;e.g.,North&Hargreaves1995)canbedescribedas
attention and action in a way that is partly independent of an inverted U-shaped function in which, on the x-axis of
226 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
predictionerror,thereisapreferredlevelofsurprisalthatleadsto and communication, from simple group clapping, a uniquely
a maximally affective response, plotted on the y-axis. However, human behaviour requiring constant automatic adjustments of
this optimal surprisal level is not uniform over musical features probabilistic representation (Molnar-Szakacs & Overy 2006;
(e.g., expressive timing, harmonic structure), but rather is Overy & Molnar-Szakacs 2009), to more sophisticated rhythmic
closely coupled to the specific characteristics of that musical organizationandself-expression(Nelson2012)withanemphasis
featureorbehaviour.AsClarkstates,contextsensitivityisfunda- on“error”aspositive,meaningfulinformation.
mental,andinthecaseofmusic,differentlevelsofconstraintwill
exist simultaneously across different systems of pitch space and
time. For example: Singing often has high constraints in terms
of pitch, tuning, and scale, while timing constraints may be
more flexible; but drumming usually involves strict timing con-
straints, with more flexibility in terms of pitch. Our perceptual Extending predictive processing to the body:
systems are finely attuned to these constraints, to the point that Emotion as interoceptive inference
rhythmic deviations that fit with certain aspects of perceived
musical structure are less well detected (Repp 1999), and doi:10.1017/S0140525X12002270
humanlyproduceddeviationsfromasteadyrhythmarepreferred
overrandomlyaddednoise(Hennigetal.2011). AnilK.Setha,bandHugoD.Critchleya,c
This tuning of our perceptual system to specific deviations aSacklerCentreforConsciousnessScience,UniversityofSussex,Brighton
from an internal model is seen not only in performance aspects BN19QJ,UnitedKingdom;bDepartmentofInformatics,UniversityofSussex,
of music (such as expressive microtiming), but also in compo- BrightonBN19QJ,UnitedKingdom;cDepartmentofPsychiatry,Brightonand
sitional aspects found in the score (such as syncopation). Most SussexMedicalSchool,BrightonBN19QJ,UnitedKingdom.
musical styles require and indeed “play” with levels of surprisal a.k.seth@sussex.ac.uk H.Critchley@bsms.ac.uk
in the temporal domain, from the musical rubato of Romantic www.anilseth.com www.sussex.ac.uk/sackler/
piano performance, to the syncopated off-beat rhythms of jazz,
to the complex polyrhythms of African percussion. Proficient Abstract:TheBayesianbrainhypothesisprovidesanattractiveunifying
musicians and composers are implicitly aware of these effects, framework for perception, cognition, and action. We argue that the
framework can also usefully integrate interoception, the sense of
and tailor their efforts to interact with the surprisal responses
the internal physiological condition of the body. Our model of
ofthelistener.Thisleadstowhathasbeencoined“communica-
“interoceptive predictive coding” entails a new view of emotion as
tive pressure” in creating music (Temperley 2004): an implicit
interoceptive inference and may account for a range of psychiatric
knowledgeof themusicaldimensionin whichpredictioncan be disordersofselfhood.
manipulated stylistically, without leading to a lack of clarity of
the musical ideas. While this complexity corresponds closely to In his compelling survey, Clark powerfully motivates predictive
what Clark refers to as a designed environment, it is important processing as a framework for neuroscience by considering the
to note that different musical environments have different “viewfrominsidetheblackbox,”thenotionthatthebrainmust
rules, that different listeners (due to their different exposure discover information about the world without any direct access
backgrounds,suchascultureandtraining)seekdifferentenviron- to its source. The ensuing discussion, and the large majority of
ments, and that the desired outcome is a complex affective the literature surveyed, is focused on just these relations
response. Indeed, exposure has been shown to influence liking between brain and (external) world. Perhaps underemphasized
for a completely new musical system after only 30 minutes of in this view is the question of how perceptions of the body and
exposure (Loui et al. 2010). This finding supports the idea of a selfarise.However,thebrain’saccesstothefactsofitsembodi-
strong personalized configuration of one’s own preference for ment and of its physiological milieu is arguably just as indirect
unpredictability, reflected in musical likes and dislikes, as well as its access to the surrounding world. Here, we extend Clark’s
as one’s own prediction abilities, shown to be quite stable over integrative analysis by proposing that interoception–the sense
time per individual, affecting interpersonal coordination ofthephysiologicalconditionofthebody(seeCraig2003)–can
(Pecenka & Keller 2011). An individual personality might be alsobeusefullyconsideredfromtheperspectiveofpredictivepro-
thrill-seeking and seek out highly unpredictable new musical cessing.Ourmodelof“interoceptivepredictivecoding”(Critchley
experiences,or,morecommonly,mightseekouthighlypredict- &Seth2012;Sethetal.2011)suggestsanewviewofemotional
ablefamiliar,favoritemusicalexperiences. feelingsasinteroceptiveinference,andshedsnewlightondisso-
Thus, different kinds of musical experience, different musical ciativedisordersofself-consciousness.
styles,andpersonalmusicalpreferencesleadtodifferentpredic- Interoceptive concepts of emotion were crystallized by James
tions,errorresponses,arousal,andaffectresponsesacrossarange (1890) and Lange (1885/1912), who argued that emotions arise
ofmusicaldimensionsandhierarchicallevels.Theupshotisthat fromperceptionofchangesinthebody.Thisbasicidearemains
thesurprisalresponseisnon-uniformformusic:Thepositioning influential more than a century later, underpinning frameworks
ofacurvedescribing“optimalsurprisal”foraffectiveoraesthetic forunderstandingemotionanditsneuralsubstrates,suchasthe
reward will be determined by culture, training, or musical style, “somatic marker hypothesis” (Damasio 2000) and the “sentient
and its precise shape (e.g., kurtosis) may be specific to the type self”model(Craig2009),bothlinkedtothenotionof“interocep-
andlevelofthepredictionormentalmodel.Andwhilethecharac- tive awareness” or “interoceptive sensitivity” (Critchley et al.
teristicsoftheoptimalsurprisalforeachaspectofmusicdiffers, 2004).Despitetheneurobiologicalinsightsemergingfromthese
the commonality remains affect, which, we propose, plays a frameworks, interoception has remained generally understood
major part in what makes prediction error in music (large or along “feedforward” lines, similar to classical feature-detection
small)meaningful,andindeeddeterminesitsvalue. or evidence-accumulation theories of visual perception as sum-
Totheextentthatpredictionisestablishedasapowerfulmech- marizedbyClark.However,ithaslongbeenrecognisedthatexpli-
anisminconveyingmusicalmeaning,itseemsclearthenthatitis citcognitionsandbeliefsaboutthecausesofphysiologicalchanges
theaffectiveresponsetothepredictionerrorthatgivestheinitial influencesubjectivefeelingstatesandemotionalbehaviour.Fifty
predictionsuchpower.Wethusproposethat thevalenceof the years ago, Schachter and Singer (1962) famously demonstrated
prediction error, leading to a range of affective responses, is a thatinjectionsofadrenaline,proximallycausingastateofphysio-
necessarycomponentofthedescriptionofhowpredictiveproces- logicalarousal,wouldgiverisetoeitherangerorelationdepend-
singcanexplainmusicalbehaviour.Thefunctionofsuchaffective ingontheconcurrentcontext(anirritatedorelatedconfederate).
predictabilitywillrequirediscussionelsewhere,butwepostulate This observation was formalized in their “two factor” theory, in
thatthiswillincludedeepconnectionswithsocialunderstanding which emotional experience is determined by the combination
BEHAVIORALANDBRAINSCIENCES(2013)36:3 227
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Figure1(Seth&Crichley). Amodelofinteroceptivepredictivecodingaccordingtowhichsubjectivefeelingstatesareconstitutedby
continuallyupdatedpredictionsofthecausesofinteroceptiveinput.Predictionsareshapedbygenerativemodelsinformedby“efference
copies” of visceral, autonomic, and motor control signals. These are generated, compared, and updated within a salience network
anchoredontheanteriorinsularandanteriorcingulatecorticesthatengagebrainstemregionsastargetsforvisceromotorcontroland
relaysofafferentinteroceptivesignals.AdaptedfromSethetal.(2011).
ofphysiologicalchangeandcognitiveappraisal,thatis,emotionas potentialroleofVENsinthisprocessandinconsciousawareness
interpretedbodilyarousal. moregenerally(Critchley&Seth2012).
Thoughtheyinvolveexpectations,two-factortheoriesfallcon- Disruptedinteroceptivepredictivecodingmaycausallyaccount
siderablyshortofafullpredictiveprocessingmodelofemotion. for a range of psychiatric disorders. Chronic anxiety has been
Byanalogywithcorrespondingmodelsofvisualperception,pre- suggested to result from heightened interoceptive prediction
dictive interoception involves hierarchically cascading top-down errorsignals(Paulus&Stein2006).Byanalogywithcomparator
interoceptivepredictionsthatcounterflowwithbottom-upintero- models of schizophrenia (Frith 2012; Synofzik et al. 2010), we
ceptive prediction errors. Subjective feeling states are then alsosuggestthatdissociativesymptoms,notablydepersonalization
determined by the integrated content of these predictive rep- andderealizationarisefromimprecise(asopposedtoinaccurate)
resentations across multiple levels (Seth et al. 2011). In other interoceptivepredictionerrorsignals.Bythesametoken,thesub-
words, the model argues that emotional content is determined jectivesenseofrealitycharacteristicofnormalconsciousexperi-
by a suite of hierarchically organized generative models that ence (i.e., “conscious presence”) may depend on the successful
predict interoceptive responses to both external stimuli and the suppressionbytop-downpredictionsofinformativeinteroceptive
internalsignalscontrollingbodilyphysiology(Fig.1). signals(Sethetal.2011).
Insummary,subjectiveemotionsandevenconsciouspresence
Itisimportanttodistinguishinteroceptivepredictivecodingor maybeusefullyconceptualizedintermsofinteroceptivepredic-
processing from more generic interactions between prediction tive coding. A key test of our model will be to identify specific
andemotion(e.g.,Gilbert&Wilson2009;Ploghausetal.1999). interoceptivepredictionerrorresponsesintheAICorelsewhere.
Crucially, predictive coding involves prediction at synchronic, This challenge is also yet to be met for predictive processing
fasttime-scales,suchthatpredictions(andpredictionerrors)are models of perception in general, and the relevant evidence
constitutive of content. For example, while Paulus and Stein wouldgoalongwaytowardsexperimentallyvalidatingtheBaye-
(2006) hypothesize the existence of interoceptive prediction sianbrainhypothesis.
errorswithininsularcortexinthegenerationofanxiety,theydo
notcontend,inthefullpredictivecodingsense,thatinteroceptive
predictions are the constitutive basis of emotions. Similarly,
althoughBarrettandBar(2009)proposethataffective(interocep-
tive) predictions within orbitofrontal cortex shape visual object Perception versus action: The computations
recognitionatfasttime-scales,theyagaindonotdescribeintero- may be the same but the direction of fit differs
ceptivepredictivecodingperse.
Severalstrandsofevidencelendsupporttoourmodelandpoint doi:10.1017/S0140525X12002397
to its implications for dissociative psychiatric symptoms such as
depersonalizationandchronicanxiety(Sethetal.2011).Anterior NicholasShea
insularcortex(AIC)inparticularprovidesanaturallocusforcom- DepartmentofPhilosophy,King’sCollegeLondon,Strand,LondonWC2R
parator mechanisms underlying interoceptive predictive coding, 2LS,UnitedKingdom.
throughitsdemonstratedimportanceforinteroceptiverepresen- nicholas.shea@kcl.ac.uk
tation (Craig, 2009; Critchley et al. 2004) and by the expression http://www.kcl.ac.uk/artshums/depts/philosophy/people/staff/academic/
within AIC of prediction error signals across a variety of affect- shea/index.aspx
ladencontexts(Paulus&Stein2006;Singeretal.2009;Palaniyap-
pan & Liddle 2011). Human AIC is also rich in Von Economo Abstract:Althoughpredictivecodingmayofferacomputationalprinciple
neurons(VENs),largeprojectionneuronswhicharecircumstan-
thatunifiesperceptionandaction,stateswithdifferentdirectionsoffitare
involved(withindicativeandimperativecontents,respectively).Predictive
tially associated with self-consciousness and complex social
statesareadjustedtofittheworldinthecourseofperception,butinthe
emotions(Craig2009).Inourmodel,fastVEN-mediatedconnec- caseofaction,thecorrespondingstatesactasafixedtargettowardswhich
tionsmayenabletherapidregistrationofvisceromotorandviscer-
theagentadjuststheworld.Thiswell-recogniseddistinctionhelpsside-
osensory signals needed for efficient updating of generative stepsomeproblemsdiscussedinthetargetarticle.
models underlying interoceptive predictive coding. The recent
discovery of VENs in the macaque monkey (Evrard et al. 2012) One of the central insights motivating Clark’s interest in the
opens important new avenues for experimental tests of the potential for predictive coding to provide a unifying
228 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
computational principle is the finding that it can be the basis of in a darkened room will be entirely ineffective in reducing such
effective algorithms in both the perceptual and motor domains errorsignals.Forexample,ifthereisoneofthesegoalstaterep-
(Eliasmith 2007, p. 380). That is surprising because perceptual resentationsforthelevelofsugarintheblood,whensensoryfeed-
inference in natural settings is based on a rich series of sensory backfailstomatchthetargettheagentdoesnothavetheoptionof
inputsatalltimes,whereasanaturalmotorcontroltaskonlyspe- reducingtheerrorsignalbychangingitsexpectation;instead,the
cifiesafinaloutcome.Manyvariationsinthetrajectoryareirrele- agent must act so as to change the sensory feedback (i.e., to
vant to achieving the final goal (Todorov & Jordan 2002), a increase the level of sugar in the blood). This answer is comp-
redundancy that is absent from the perceptual inference lementarytoClark’sobservationthatsomeformsofpriorexpec-
problem. Despite this disanalogy, the two tasks are instances of tationcouldleadagentstoengageinexploratoryactionsorsocial
thesamegeneralmathematicalproblem(Todorov2006). play. It is orthogonal to the distinction between exploratory and
Clark emphasises the “deep unity” between the two tasks, exploitativeactions(whichcan,inanyevent,onlybedrawnrela-
whichisjustifiedbutmightservetoobscureanimportantdiffer- tivetosomesetofgoalstates).
ence.Intheperceptualtask,apredictionerrorisusedtochange Afinalobservationconcernsthequestionofwhethertheexpec-
expectationssoastomatchtheinput,whereas,asClarknotes,in tations involved in predictive coding calculations refer to the
themotortaskthepredictionerrorisusedtodrivemotorbehav- externalworld.Itissometimessuggestedthatpredictionsandpre-
iour that changes the input. In perception, prediction error is diction errors only concern the states of other computational
minimised by changing something internal (expectations), elements in the system. Goal states are perhaps the most
whereasinactionpredictionerrorisminimisedbychangingsome- obvious candidate for representations that refer to the external
thing external (acting on the world so as to alter sensory input). world. Since the feedback to which they are compared is
Although itistruein onesense thatthere isacommoncompu- changedbyactionontheworld,itisplausiblethattheycometo
tational principle that does not distinguish between perceptual represent the external world affairs that must be changed if the
andmotortasks(sect.1.5),weshouldnotoverlookthefactthat predictionerroristobecancelled.
those computations are deployed quite differently in the two Toconclude,Clark’spersuasivecasefortheimportanceofpre-
cases. In the two cases state representations have what philoso- dictivecodingasaunifyingcomputationalprinciple,likeanyfruit-
phershavecalleddifferent“directionsoffit.”Amotortasktakes ful research agenda, brings new issues into focus. An important
as input a goal state, which is held fixed; a motor program to one is the question of what makes that computational principle
attain that goal state is then calculated (Todorov 2004). These operateinindicative(perceptual)modeinsomesubsystemsand
goal states have a world-to-mind direction of fit and imperative inimperative(action)modeinothers.
content. By contrast, the state descriptions in the perceptual
task (expectations fed back from higher levels in the processing
hierarchy) are continually adjusted so as to match the current
sensory input more closely. They display a world-to-mind direc-
tionoffitandhaveindicativecontent.Thedifferenceisapparent Schizophrenia-related phenomena that
initsconsequencesforthebehaviouroftheorganism:Prediction challenge prediction error as the basis of
errors in respect of indicative representations can be fully can- cognitive functioning
celled without the agent having to perform any action, whereas
prediction errors in respect of imperative representations doi:10.1017/S0140525X12002221
cannotbecancelledunlesstheagentmovesinsomeway.
Iftheseaccountsareright,thenthedeepunityconsistsinthefact StevenM.Silverstein
thatbothperceptionandactioninvolvethereductionofprediction UniversityBehavioralHealthCareandDepartmentofPsychiatry,RobertWood
error.However,sincetheydosobyquitedifferentmeans,adeep JohnsonMedicalSchool,UniversityofMedicineandDentistryofNewJersey,
differencebetweenperceptionandactionremains.Somesensori- Piscataway,NJ08854.
motoraccountsofourinteractionswiththeworlddoindeedserve silvers1@umdnj.edu
todissolve theboundarybetweenperceptionandaction(Hurley
1998),butthepredictivecodingframeworkonitsowndoesnot. Abstract: There are aspects of schizophrenia that pose challenges for
(Itdoes,however,undermineaclearboundarybetweenperception Clark’s model. These include: (1) evidence for excitatory activity
underlying self-organizing neural ensembles that support coordinating
andcognition.)Thisgivesrisetoanimportantquestionforthepre-
functions,andtheirimpairmentinschizophrenia;(2)evidenceregarding
dictivecodingprogramme:Whatdetermineswhetheragivenpre-
hallucinations that suggest they are not due to excessive prediction
diction/expectation is given a mind-to-world functional role,
error;and(3)thecriticalroleofemotionalfactorsas settingconditions
allowing it to be adjusted in the light of prediction errors, and fordelusionformation.
what gives other expectations a world-to-mind functional role,
such that prediction errors cause bodily movements/action? As Clark’smodelemphasizestheprocessingofpredictionerror,and,
theevidenceforacommoncomputationalprincipleinperception insection4.2,thisisappliedtoanunderstandingofhallucinations,
andactionmounts,theneedbecomespressingtospecifyhowthis delusions,andschizophrenia.Thiscommentaryemphasizesthree
fundamentaldifferencebetweenitstwomodesofoperationarises. points related to these themes, with the overall goal of demon-
Clark goes on to consider whether an austere “desert land- stratingthatClark’sview,atpresent,doesnotprovideafullyade-
scape” description of the computational processing is possible quateheuristicforunderstandingpsychoticphenomena.
that does away with goals and reward entirely (sect. 5.1), in the Clark’s theory emphasizes anti-Hebbian feedforward proces-
sense that neither are represented in the model. If action gui- sing, in which correlated activity across neurons is suppressed,
dance requires states with a world-to-mind direction of fit, then presumably because no deviation from what is expected is
stateswhichfunctionasgoalshavenotbeeneliminated.Evenif present, therefore allowing any signals related to deviation from
the difference is a matter of degree, with many cases in the what is expected (i.e., prediction error) to become relatively
middle, we are still operating with a continuum marked by the more salient. While this would appear to be a useful data-com-
extent to which a state operates as a goal state at one end or as pressionstrategyforcodinginvariantbackgroundinformation,it
anindicativestateattheother. doesnotaccountforcasesinwhichitispreciselythecorrelation
Thedistinctionbetweenindicativeandimperativecontentsalso between stimulus elements that codes their object properties,
throws light on the darkened room problem: Why don’t agents thereby signaling stimulus significance. Numerous demon-
minimise prediction error by just sitting still in a darkened strationsexist(e.g.,Kinoshitaet al.2009; Silversteinetal.2009;
room?Ifsomesubsystemsareconstrainedtominimiseprediction Singer 1995) wherein increasing the correlation between an
errornotbychangingexpectationsbutbyacting,thensittingstill aspect of elements (e.g., stimulus orientation in contour
BEHAVIORALANDBRAINSCIENCES(2013)36:3 229
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
integration paradigms) leads to increased signal strength. Of models. It also must be noted that the delusions that patients
course,itispossibletoargue,asClarkdoes,thatthisisduetoa develop are not about random events, but typically are framed
cancellationoftheactivityinerrorunitsandsubsequentenhance- inreferencetotheself,withappreciationofthestatisticalstruc-
mentofthesignalcodingthecontourorshape.However,itisnot tureoftherestoftheworldbeingintact.Similarly,auditoryhal-
clear how these competing hypotheses could be pitted against lucinations often involve negative comments about the self, and
eachotherinadefinitivestudy. ithasbeensuggested,duetothehighprevalenceofhistoriesof
ConsistentwithClark’sview,evidenceexiststhat,forexample, childhoodphysicalandsexualabuseinpeoplewithschizophrenia
asrandomorientationaljitterisappliedtodisconnectedcontour (Readetal.2005),thatvoicesareaspectsofmemorytracesassoci-
elements, increases in fMRI BOLD signal are observed (Silver- ated with the abuse experience that have been separated from
stein et al. 2009). Clark’s view is also consistent with Weber’s other aspects of the memory trace due to hippocampal impair-
(2002) view that much of our direct understanding of visual ment secondary to chronic cortisol production (Read et al.
forms results from perception of “metamorphoses of geometry” 2001) (as opposed to being due to top-down expectancy driven
ortopological(isotopic)alterationsofbasicforms,aviewconsist- processing). A purely computational theory of hallucinations
entwithevidencethattopologicalinvariantsaretheprimitivesto and/or delusions is like a mathematical theory of music–it can
which our visual system responds most strongly (Chen 2005). explain aspects of it, but not why one piece of music creates a
However, it is also the case that compared to a non-informative strongemotionalresponseinonepersonyetnotinanother.Psy-
background of randomly oriented Gabors, perception of a choticsymptomformationmustbeunderstoodwithinthecontext
contour is associated with increased activity (Silverstein et al. ofpersonalvulnerabilityandemotionalfactors,andthesearenot
2009). Clarifying the extent to which these two forms of signal wellaccountedforbyaBayesianviewatpresent.
increaserepresentfunctioningofdifferentcircuitsisanimportant
taskforfutureresearch.Untilthisisclarified,Clark’sviewappears
to be most appropriate for understanding signaling of objects in
theenvironment,asopposedtobrainactivityinvolvedincreating
representations of those objects. This is relevant for schizo- What else can brains do?
phrenia,asitischaracterizedbyabreakdownincoordinatingpro-
cesses in perception and cognition (Phillips & Silverstein 2003; doi:10.1017/S0140525X12002439
Silverstein & Keane 2011). A challenge for Clark’s view is to
accountforthesephenomena,whichhavebeenpreviouslyunder- AaronSloman
stood as reflecting a breakdown in Hebbian processing, and SchoolofComputerScience,UniversityofBirmingham,BirminghamB152TT
reduced self-organization at the local circuit level, involving UnitedKingdom.
reducedlateral(andre-entrant)excitation. a.sloman@cs.bham.ac.uk http://www.cs.bham.ac.uk/∼axs
Clarknotesthatwhileperceptualanomaliesalonewillnottypi-
cally lead to delusions, the perceptual and doxastic components Abstract: The approach Clark labels “action-oriented predictive
should not be seen as independent. However, there are several processing” treats all cognition as part of a system of on-line control.
This ignores other important aspects of animal, human, and robot
syndromes (e.g., Charles Bonnet Syndrome, Dementia with
intelligence.Hecontrastsitwithanalleged“mainstream”approachthat
LewyBodies,Parkinson’sDiseaseDementia)wherevisualhallu-
alsoignoresthedepthandvarietyofAI/Roboticresearch.Idon’tthink
cinationsareprominentanddelusionsaretypicallyabsent(Sant-
thetheorypresentedisworthtakingseriouslyasacompletemodel,even
house et al. 2000). Moreover, it would appear to be difficult to ifthereismuchthatitexplains.
explainthewell-formedhallucinationscharacteristicofthesesyn-
dromes as being due to prediction error, given their sometimes Clark’spaperdeservesfarmorethan1,000words,butIhaveto
improbablecontent(e.g.,verysmallpeopledressed in Victorian be brief and dogmatic. Characterizing brains as predicting
era attire), and apparent errors in size constancy (ffytche & machinesignoresmanyabilitiesproducedbyevolutionanddevel-
Howard 1999; Geldmacher 2003) that argue against Bayes- opment,1includingmathematicaldiscoveryandreasoning,using
optimal perception in these cases. There are also many cases of evolved mechanisms (perhaps) shared by several species
schizophreniawheredelusionsarepresentwithouthallucinations. capableofthe“representationalredescription”postulatedinKar-
Finally,whileevidenceofreducedbinoculardepthinversionillu- miloff-Smith (1992) and the meta-configured competences
sionsinschizophrenia(Keaneetal.,inpress;Koetheetal.2009) suggestedinChappell&Sloman(2007),including(largelyunstu-
providesevidence,ontheonehand,foraweakenedinfluenceof died) discoveries of “toddler theorems” (Sloman 2010). The
priors(orofthelikelihoodfunction)(Phillips2012)onperception, “action-oriented predictive processing” approach treats every-
this evidence also indicates more veridical perception of the thing as on-line control (Powers 1973), like “enactivist” theorists
environment.Therefore,thesedatasuggestthat,ratherthanpre- who usually ignore competences required to make predictions
dictionerrorsignalsbeingfalselygeneratedandhighlyweighted true and processes generating and choosing (sometimes uncon-
(asClarksuggests),suchsignalsappearnottobegeneratedtoa sciously) between goals, plans, designs (for houses, machines,
sufficient degree, resulting in a lack of top-down modulation, etc.), preferences, explanations, theories, arguments, story plots,
and bottom-up (but not error) signals being strengthened. formsofrepresentation,ontologies,grammars,andproofs.Predic-
Indeed, this is exactly what was demonstrated in recent studies tive processing doesn’t explain termite cathedral building.
using dynamic causal modeling of ERP and fMRI data from a (CompareChittka&Skorupski2011).
hollow-mask perception task in people with schizophrenia Simultaneous localisation and mapping (SLAM) robotic tech-
(Dima et al. 2009; 2010). A developing impairment such as this niques,partlyinspiredbythingsanimalsdo,createuseful(topolo-
would lead to subjective changes in the meaning of objects and gical, metrical, and possibly logical) representations of enduring
theenvironmentasawhole,andoftheself–which,inturn,can extended environments. That’s not learning about mappings
spawndelusions(Mattusek1987;Sass1992;Uhlhaas&Mishara between inputs and outputs. It’s a special case of using actions,
2007),eventhoughthedelusionalthoughtsareunrelatedtothe percepts, and implicit theories to derive useful information
likelihoodfunctionsandbeliefsthatexistedpriortotheonsetof abouttheenvironment.Anotherisproducingatheoryofchemical
thedelusion. valency.
Finally,Clark’sviewofhallucinationsissimilartomanymodels Systematically varying how things are squeezed, stroked,
of schizophrenia, in that it is based on computational consider- sucked, lifted, rotated, and so forth, supports learning about
ationsonly.But,asnoted,delusionsoftengrowoutofphenomen- kinds of matter, and different spatial configurations and pro-
ologicalchangesandemotionalreactionstothese(seealsoConrad cesses involving matter (Gibson 1966). Predicting sensory
1958), and this cascade is typically ignored in computational signals is only one application. Others include creating future
230 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
structuresandprocessesintheenvironment,andunderstanding experienceofstrugglingtobuildworkingsystems,whenusedto
processes. Choosing future actions often ignores sensory and guideresearchratherthanreplaceit.)Thisprojectrequiresstudy-
motor details, since a different ontology is used (e.g., choosing ingmanytypesofenvironment,includingnotonlyenvironments
between a holiday spent practising French and a music- with increasingly complex and varied physical challenges and
making holiday, or choosing insulation for a new house). For opportunities, but also increasingly rich and varied interactions
more on “off-line” aspects of intelligence ignored by many with other information processing systems: predators, prey, and
“enactivist” and “embodied cognition” enthusiasts, see Sloman conspecifics (young and old). Generalizing Turing (1952), I call
(1996; 2006; 2009). Even for on-line control, the use of servo- thisthe“Meta-morphogenesisproject”(Sloman2013).
control with qualitative modifications of behavior responding Clarkcomparestheprediction“story”with“mainstreamcom-
to changing percepts reduces the need for probabilistic predic- putational accounts that posit a cascade of increasingly complex
tion: Head for the center of the gap, then as you get close feature detection (perhaps with some top-down biasing)” (sect.
use vision or touch to control your heading. Choosing a 5.1).ThisfitssomeAIresearch,butlabellingitas“mainstream”
heading may, but need not, involve prediction: it could be a and treating it as the only alternative, ignores the diversity of
reflex action. approaches and techniques including constraint-processing,
PredictingenvironmentalchangesneednotuseBayesianinfer- SLAM, theorem proving, planning, case-based reasoning,
ence, for example when you predict that two more chairs will naturallanguageprocessing,andmanymore.Muchhumanmotiv-
ensureseatsforeveryone,orthatthegearwheelrotatingclock- ation, especially in young children, seems to be concerned with
wisewillmaketheonemeshedwithitrotatecounter-clockwise. extensionsofcompetences,asopposedtopredictingandacting,
And some predictions refer to what cannot be sensed, for andsimilarlearningbyexplorationandexperimentisbeinginves-
example most deep scientific predictions, or a prediction that a tigatedinrobotics.
particularwayoftryingtoproveFermat’slasttheoremwillfail. Aminorpoint:Binocularrivalrydoesn’talwaysleadtoalternat-
Manythingshumansusebrainsfordonotinvolveon-lineintel- ing percepts. For example look at an object with one eye, with
ligence,forexamplemullingoveraconversationyouhadaweek something moving slowly up and down blocking the view from
ago,lyingsupinewitheyesshutcomposingapianopiece,tryingto the other eye.The remote object can appear as if behind a tex-
understand the flaw in a philosophical argument, or just day- turedwindowmovingupanddown.
dreamingaboutaninter-planetaryjourney. Clark claims (in his abstract) that the “hierarchical prediction
Idon’tdenythatmanycognitiveprocessesinvolvemixturesof machine” approach “offers the best clue yet to the shape of a
top-down, bottom-up, middle-out (etc.) influence: I helped unified science of mind and action”. But it unifies only the
produce a simple model of such visual processing decades ago, phenomenaitsproponentsattendto.
Popeye(Sloman1978,Ch.9),andcriticizedover-simpletheories
ofvisionthatignoredrequirementsforprocessperceptionandon-
linecontrol(Sloman1982;1989).DavidHogg,thenmystudent, NOTE
used3-Dpredictiontoreducevisualsearchintrackingahuman 1. For more details, see http://www.cs.bham.ac.uk/research/projects/
cogaff/12.html#1203.
walker(Hogg1983).Sloman(2008)suggeststhatrapidperception
ofcomplexvisualscenesrequiresrapidactivationandinstantiation
of many normally dormant, previously learnt model fragment
types and relationships, using constraint propagation to rapidly
assemble and instantiate multi-layered percepts of structures Distinguishing theory from implementation in
and processes: a process of interpretation, not prediction predictive coding accounts of brain function
(compare parsing). Building working models to test the ideas
will be difficult, but not impossible. Constraint propagation doi:10.1017/S0140525X12002178
neednotuseBayesianinference.
“Thusconsiderablackboxtakinginputsfromacomplexexter- MichaelW.Spratling
nal world. The box has input and output channels along which DepartmentofInformatics,King’sCollegeLondon,UniversityofLondon,
signalsflow.Butallit‘knows’about,inanydirectsense,arethe
LondonWC2R2LS,UnitedKingdom.
waysitsownstates(e.g.,spiketrains)flowandalter….Thebrain
michael.spratling@kcl.ac.uk
is one such black box” (sect. 1.2). This sounds like a variant of
concept empiricism, defeated long ago by Kant (1781) and Abstract: It is often helpful to distinguish between a theory (Marr’s
buriedbyphilosophersofscience. computational level) and a specific implementation of that theory
(Marr’s physical level). However, in the target article, a single
Many things brains and minds do, including constructing
implementation of predictive coding is presented as if this were the
interpretationsandextendingtheirownmeta-cognitivemechan-
theory of predictive coding itself. Other implementations of predictive
isms, are not concerned merely with predicting and controlling
coding have been formulated which can explain additional
sensoryandmotorsignals. neurobiologicalphenomena.
Evolutionary“trails”,fromverysimpletomuchmorecomplex
systems,mayprovidecluesforadeeptheoryofanimalcognition Predictivecoding(PC)istypicallyimplementedusingahierarchy
explainingthemanylayersofmechanisminmorecomplexorgan- of neural populations, alternating between populations of error-
isms.Weneedtodistinguishdiverserequirementsforinformation detectingneuronsandpopulationsofpredictionneurons.Inthe
processing of various sorts, and also the different behaviors and standard implementation of PC (Friston 2005; Rao & Ballard
mechanisms. A notable contribution is Karmiloff-Smith (1992). 1999), each population of prediction neurons sends excitatory
Other relevant work includes McCarthy (2008) and Trehub connections forward to the subsequent population of error-
(1991), and research by biologists on the diversity of cognition, detecting neurons, and also sends inhibitory connections back-
eveninverysimpleorganisms.Ihavebeentryingtodothisthis wards to the preceding population of error-detecting neurons.
sortofexplorationof“designspace”and“nichespace”formany Similarly, each population of error-detecting neurons also sends
years(Sloman1971;1978;1979;1987;1993;1996;2002;2011a; informationinbothdirections;viaexcitatoryconnectiontothefol-
2011b). lowing populationof predictionneurons, and via inhibitory con-
Wherenointermediateevolutionarystepshavebeenfound,it nections to the preceding population of prediction neurons.
may be possible to learn from alternative designs on branches (See, for example, Figure 2 in Friston [2005], or Figure 2b in
derived from those missing cases. We can adopt the designer Spratling [2008b]). It is therefore inaccurate for Clark to state
stance(McCarthy2008)tospeculateabouttestablemechanisms. (seesects.1.1and2.1)thatinPCthefeedforwardflowofinfor-
(It is a mistake to disparage “just so” stories based on deep mation solely conveys prediction error, while feedback only
BEHAVIORALANDBRAINSCIENCES(2013)36:3 231
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Commentary/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
conveys predictions. Presumably what Clark really means to say implementation(PC/BC)ismathematicallysimplerwhileexplain-
is that the standard implementation of PC proposes that ingmoreoftheneurophysiologicaldata:ComparetherangeofV1
inter-regional feedforward connections carry error, whereas response properties accounted for by PC/BC (Spratling 2010;
inter-regionalfeedbackconnectionscarrypredictions(whileinfor- 2011; 2012a; 2012b) with that simulated by the standard
mationflowinthereversedirectionstakesplacewithineachcor- implementationofPC(Rao&Ballard1999);ortherangeofatten-
ticalarea).However,thisissimplyonehypothesisabouthowPC tionaldataaccountedforbythePC/BCimplementation(Spratling
shouldbeimplementedincorticalcircuitry.Itisalsopossibleto 2008a) compared to the standard implementation (Feldman &
group neural populations differently so that inter-regional feed- Friston 2010). Compared to the standard implementation, PC/
forward connections carry predictions, not errors (Spratling BC is also more biologically plausible; for example, it does not
2008b). employ negative firing rates. However, PC/BC is still defined at
As alternative implementations of the same computational anintermediate-levelofabstraction,andtherefore,likethestan-
theory,thesetwowaysofgroupingneuralpopulationsarecompa- dard implementation, provides integrative and functional expla-
tiblewiththesamepsychophysical,brainimaging,andneurophy- nations of empirical data (Spratling 2011). It can also be
siological data reviewed in section 3.1 of the target article. interpreted as a form of hierarchical Bayesian inference (Loch-
However, they do suggest that different cortical circuitry may mann & Deneve 2011). However, it goes beyond the standard
underlie these outward behaviours. This means that claims implementation of PC by identifying computational principles
(repeated by Clark in sect. 2.1) that prediction neurons corre- that are shared with algorithms used in machine learning, such
spond to pyramidal cells in the deep layers of the cortex, while as generative models, matrix factorization methods, and deep
error-detecting neurons correspond to pyramidal cells in super- learning architectures (Spratling 2012b), as well as linking to
ficialcorticallayers,arenotpredictionsofPCingeneral,butpre- alternativetheoriesofbrainfunction,suchasdivisivenormalisa-
dictions of one specific implementation of PC. These claims, tion and biased competition (Spratling 2008a; 2008b). Other
therefore, do not constitute falsifiable predictions of PC (if they implementations of PC may in future prove to be even better
didthentheideathatPCoperatesintheretina–asdiscussedin models of brain function, which is even more reason not to
sect.1.3–couldberejected,duetothelackofcorticalpyramidal confuse one particular implementation of a theory with the
cellsinretinalcircuitry!).Indeed,itishighlydoubtfulthatthese theoryitself.
claims even constitute falsifiable predictions of the standard
implementation of PC. The standard implementation is defined
at a level of abstraction above that of cortical biophysics: it con-
tains many biologically implausible features, like neurons that
can generate both positive and negative firing rates. The Sparse coding and challenges for Bayesian
mapping between elements of the standard implementation of models of the brain
PC and elements of cortical circuitry may, therefore, be far less
direct than is suggested by the claim about deep and superficial doi:10.1017/S0140525X12002300
layer pyramidal cells. For example, the role of prediction
neurons and/or error-detecting neurons in the model might be ThomasTrappenbergandPaulHollensen
performed by more complex cortical circuitry made up of FacultyofComputerScience,DalhousieUniversity,Halifax,NSB3H4R2,
diverse populations of neurons, none of which behave like the Canada.
model neurons but whose combined action results in the same tt@cs.dal.ca paulhollensen@gmail.com
computationbeingperformed. www.cs.dal.ca/∼tt
ThefactthatPCistypicallyimplementedatalevelofabstrac-
Abstract: While the target article provides a glowing account for the
tion that is intermediate between that of low-level, biophysical,
excitementinthefield,westressthathierarchicalpredictivelearningin
circuits and that of high-level, psychological, behaviours is a
the brain requires sparseness of the representation. We also question
virtue.Suchintermediate-levelmodelscanidentifycommoncom-
the relation between Bayesian cognitive processes and hierarchical
putationalprinciplesthatoperateacrossdifferentstructuresofthe generativemodelsasdiscussedbythetargetarticle.
nervoussystemandacrossdifferentspecies(Carandini2012;Phil-
lips & Singer 1997); they seek integrative explanations that are Clark’s target article captures well our excitement about predic-
consistentbetweenlevelsofdescription(Bechtel2006;Mareschal tive coding and the ability of humans to include uncertainty in
et al. 2007), and they provide functional explanations of the making cognitive decisions. One additional factor for represen-
empiricaldatathatarearguablythemostrelevanttoneuroscience tational learning to match biological findings that has not been
(Carandini et al. 2005; Olshausen & Field 2005). For PC, the stressedmuchinthetargetarticleistheimportanceofsparseness
pursuitofconsistencyacrosslevelsmayprovetobeaparticularly constraints. We discuss this here, together with some critical
important contribution to the modelling of Bayesian inference. remarks on Bayesian models and some remaining challenges
Bayes’ theorem states that the posterior is proportional to the quantifyingthegeneralapproach.
productofthelikelihoodandtheprior.However,itplacesnocon- There are many unsupervised generative models that can be
straints on how these probabilities are calculated. Hence, any usedtolearnrepresentationstoreconstructinputdata.Consider,
model that involves multiplying two numbers together, where forexample,photographsofnaturalimages.Acommonmethod
those numbers can be plausibly claimed to represent the likeli- for dimensionality reduction is principle component analysis
hoodandposterior,canbepassedoffasaBayesianmodel.This thatrepresentsdataalongorthogonalfeaturevectorsofdecreas-
has led to numerous computational models which lay claim to ing variance. However, as nicely pointed out by Olshausen and
probabilistic respectability while employing mechanisms to Field(1996),thecorrespondingfiltersdonotresemblereceptive
derive “probabilities” that are as ad-hoc and unprincipled as the fields in the brain. In contrast, if a generative model has the
non-Bayesian models they claim superiority over. It can be additional constraint to minimize not only the reconstruction
hopedthatPCwillprovideaframeworkwithsufficientconstraints error but also the number of basis functions that are used for
to allow principled models of hierarchical Bayesian inference to any specific image, then filters emerge that resemble receptive
bederived. fieldsofsimplecellsintheprimaryvisualcortex.
A final point about different implementations is that they are Sparserepresentationintheneuroscientificcontextactuallyhas
notnecessarilyallequal.AswellasimplementingthePCtheory alongandimportanthistory.HoraceBarlowpointedoutforyears
usingdifferentwaysofgroupingneuralpopulations,wecanalso that the visual system seems to be remarkably set up for sparse
implement the theory using different mathematical operations. representations (Barlow 1961), and probably the first systematic
ComparedtothestandardimplementationofPC,onealternative model in this direction was proposed by his student Peter
232 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Földiák(1990).Itseemsthatnearlyeverygenerativemodelwitha implement a general learning machine. While all these models
sparseness constraint can reproduce receptive fields resembling are Bayesian in the sense that they represent causal models
simple cells (Saxe et al. 2011), and Ng and colleagues have withprobabilisticnodes,thenatureofthemodelsareverydiffer-
shown that sparse hierarchical Restricted Boltzmann Machines ent. It is fascinating to think about how such specific Bayesian
(RBMs) resembles features of receptive fields in V1 and V2 models as the ideal observer can emerge from general learning
(Lee et al. 2008). In our own work, we have shown how lateral machines such as the RBM. Indeed, such a demonstration
inhibition can implement sparseness constrains in a biological would be necessary to underpin the story that hierarchical gen-
waywhilealsopromotingtopographicrepresentations(Hollensen erative models supportthe Bayesian cognitive processingasdis-
&Trappenberg2011). cussed in the target article.
Sparse representation has great advantages. By definition, it
meansthatonlyasmallnumberofcellshavetobeactivetorepro-
duceinputsingreatdetail.Thisnotonlyhasadvantagesenergeti-
cally,italsorepresentsalargecompressionofthedata.Ofcourse,
theextremecaseofmaximalsparsenesscorrespondingtogrand- Authors’ Response
mothercellsisnotdesirable,asthiswouldhinderanygeneraliz-
ationabilityofamodel.Experimentalevidenceofsparsecoding
has been found in V1 (Vinje & Gallant 2000) and hippocampus
(Waydoetal.2006).
Therelationoftheefficientcodingprincipletofreeenergyis
Are we predictive engines? Perils, prospects,
discussed by Friston (2010), who provides a derivation of free and the puzzle of the porous perceiver
energyasthedifferencebetweencomplexityandaccuracy.That
is, minimizingfree energy maximizes the probabilityof the data
doi:10.1017/S0140525X12002440
(accuracy), while also minimizing the difference (cross-entropy)
between the causes we infer from the data and our prior on AndyClark
causes.Thefact thatthelatteristermedcomplexityreflectsour
SchoolofPhilosophy,Psychology,andLanguageSciences,Universityof
intuition that causes in the world lie in a smaller space than
Edinburgh,EdinburghEH125AY,Scotland,UnitedKingdom.
their sensory projections. Thus, our internal representation
andy.clark@ed.ac.uk
shouldmirrorthesparsestructureoftheworld. http://www.philosophy.ed.ac.uk/people/full-academic/andy-clark.html
While Friston shows the equivalence of Infomax and free
energy minimization given a sparse prior, a fully Bayesian Abstract:Thetargetarticlesketchedandexploredamechanism
implementationwouldtreattheprioritselfasarandomvariable (action-oriented predictive processing) most plausibly associated
to be optimized through learning. Indeed, Friston goes on to with core forms of cortical processing. In assessing the
saythatthecriticismofwherethesepriorscomefrom“dissolves attractions and pitfalls of the proposal we should keep that
with hierarchical generative models, in which the priors them- element distinct from larger, though interlocking, issues
selves are optimized” (Friston 2010, p. 129). This is precisely concerningthenatureofadaptiveorganizationingeneral.
whathasnotyetbeenachieved:amodelwhichlearnsasparserep-
resentation of sensory messages due to the world’s sparseness,
ratherthanduetoitsarchitectureorstaticpriors.Ofcourse,we R1. Introduction:Combiningchallengeanddelight
arelikelyendowedwitharangeofpriorsbuilt-intoourevolved
corticalarchitectureinordertobootstraporguidedevelopment. Thetargetarticle(“Whatevernext?Predictivebrains,situ-
Whatthesenativepriorsareandtheformtheytakeisaninterest- ated agents, and the future of cognitive science”–hence-
ingandopenquestion. forth WN for short) drew a large and varied set of
There are two alternatives to innate priors for explaining the responses from commentators. This has been a source of
receptive fields we observe. First, there has been a strong ten- bothchallengeanddelight.Challenge,becausethevariety
dencytolearnhierarchicalmodelslayer-by-layer,witheachlayer
anddepthofthecommentariesreallydemands(atleast)a
learningtoreconstructtheoutputofthepreviouswithoutbeing
book-length reply, not to mention far more expertise than
influencedbytop-downexpectations.Suchtop-downmodulation
istheprimecandidateforexpressingempiricalpriorsandinfluen- I possess. Delight, because the wonderfully constructive
and expansive nature of those responses already paints a
cinglearningtoincorporatehigh-leveltendencies.Implementing
amodelthatbalancesconformingtobothitsinputandtop-down far richer picture of both the perils and the prospects of
expectationswhileofferingefficientinferenceandrobustnessisa the emerging approach to cortical computation that I
largely open question (Jaeger 2011). Second, the data typically dubbed“action-orientedpredictiveprocessing”(henceforth
used to train our models on differs substantially from what we PPforshort).InwhatfollowsIrespond,atleastinoutline,to
areexposedto.Thevisualcortexexperiencesastreamofimages threemaintypesofchallenge(the“perils”referredtointhe
withsubstantialtemporalcoherenceandcorrelationwithinternal title)thatthecommentarieshaveraised.Ithenoffersome
signals such as eye movements, limiting the conclusions we can
remarksonthemanyexcitingsuggestionsconcerningcomp-
draw from comparing its representation to models trained on
lementary perspectives and further applications (the pro-
staticimages(see,e.g.,Rustetal.2005).
The final comment we would like to make here concerns the spects).Iendbyaddressingakindofconceptualpuzzle(I
call it “the puzzle of the porous perceiver”) that surfaced
discussion of Bayesian processes. Bayesian models such as the
ideal observer have received considerable attention in neuro- in different ways and that helps focus some fundamental
science since they seem to nicely capture human abilities to questions concerning the nature (and plausibility) of the
combine new evidence with prior knowledge in the “correct” impliedrelationbetweenthought,agent,andworld.
probabilistic sense. However, it is important to realize that
these Bayesian models are very specific to limited experimental
tasks, often with only a few possible relevant states, and such
models do not generalize well to changing experimental con- R2. Perils ofprediction
ditions. In contrast, the Bayesian model of a Boltzmann
machine represents general mechanistic implementations of The key perils highlighted by the commentaries concern
information processing in the brain that we believe can (1) the proper “pitch” of the target proposal (is it about
BEHAVIORALANDBRAINSCIENCES(2013)36:3 233
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/AndyClark: Predictivebrains,situated agents,and thefutureof cognitive science
implementation, algorithm, or something more abstract?); level model”: one that still leaves unspecified a great
(2) the relation between PP and various other strategies many important details concerning implementation.
and mechanisms plausibly implicated in human cognitive Unlike Rasmussen & Eliasmith, however, Spratling
success;and(3)thenatureandadequacyofthetreatment notes that: “Such intermediate-level models can identify
ofattentionasamechanismfor“precision-weighting”pre- common computational principles that operate across
diction error. different structures of the nervous system … and they
provide functional explanations of the empirical data that
arearguablythemostrelevanttoneuroscience”(emphasis
R2.1 Questioningpitch
Spratling’s). WN aimed to present just such an intermedi-
Rasmussen & Eliasmith raise some important worries ate-levelmodel.Insodoing,itnecessarilyfellshortofpro-
concerning content and pitch. They agree with the target viding a detailed architectural specification of the kind
article on the importance and potency of action-oriented Rasmussen & Eliasmith seek. It does, however, aim to
predictive processing(PP),anddescribe theideasascom- pick out a space of models that share some deep assump-
pelling,compatiblewiththeempiricaldata,andpotentially tions: assumptions that already have (or so I argued–see
unifyingaswell.Butthecompatibility,theyfear,comesata WN, sect. 2) many distinctive conceptual and empirical
price. For, the architectural commitments of PP as I consequences.
defineditare,theyargue,tooskimpyasyettodeliverates- Spratling then worries (in a kind of inversion of the
table model unifying perception, action, and cognition. I doubts raised by Rasmussen & Eliasmith) that in one
agree. Indeed (as they themselves note) much of the respect, at least, the presentation in WN is rather too
target article argues that PP does not serve to specify the specific, too close to one possible (but not compulsory)
detailed form of a cognitive architecture. I cannot agree implementation. The issue here concerns the depiction of
with them, however, that the commitments PP does errorasflowingforwards(i.e.,betweenregionsinthehier-
make therefore run the risk of being “empirically archy) and predictions as flowing backwards. WN depicts
vacuous.” Those commitments include the top-down use thisasadirectconsequenceofthepredictivecodingcom-
of a hierarchical probabilistic generative model for both pressiontechnique.Butitisbetterseen,Spratlingconvin-
perceptionandaction,thepresenceoffunctionallydistinct cingly argues, as a feature of one (albeit, as he himself
neural populations coding for representation (prediction) accepts, the standard) implementation of predictive
and for prediction-error, and the suggestion that predic- coding. Spratling is right to insist upon the distinction
tions flow backwards through the neural hierarchy while betweentheoryandimplementation.Itisonlybyconsider-
only information concerning prediction error flows for- ing the space of alternative implementations that we can
wards. The first of these (the widespread, top-down use start to ask truly pointed experimental questions, (of the
of probabilistic generative models for perception and kind highlighted by Rasmussen & Eliasmith) of the brain:
action) constitutes a very substantial, but admittedly quite questions that may one day favour one implementation of
abstract, proposal: namely, that perception and (by a the key principles, or even none at all. One problem, I
clever variant–see WN, sect. 1.5) action both depend suspect, will be that resolving the “what actually flows
upon a form of “analysis by synthesis” in which observed forward?” issue looks crucial to adjudicating between
sensory data is explained by finding the set of hidden various close alternatives. But that depends (as Spratling’s
causes that are the best candidates for having generated work shows) upon how we carved the system into levels
that sensory data in the firstplace. in the first place, since that determines what counts as
Mechanistically, PP depicts the top-down use of (hier- flow within a level versus flow between levels. This is not
archical)probabilisticgenerativemodelsasthefundamen- goingtobeaseasyasitsounds,sinceitisnotgrosscortical
tal form of cortical processing, accommodating central layers but something much more functional (cortical
cases of both perception and action, and makes a further columns, something else?) that is at issue. Experimenters
suggestion concerning the way this is achieved. That sug- and theorists will thus need to work together to build
gestion brings on board the data compression strategy detailed, testable models whose assumptions (especially
known as “predictive coding” (WN, sect. 1.1) from which concerning what counts as a region or level) are agreed in
it inherits–or so I argued, but see below–a distinctive advance.
imageoftheflowofinformation:oneinwhichpredictions Egner&Summerfielddescribeanumberofempirical
(from the generative model) flow downwards (between studies that support the existence both of (visual) surprise
regions of the neural hierarchy) and only deviations from signals and of the hierarchical interplay between expec-
what is predicted (in the form of residual errors) flow for- tation and surprise. Some of this evidence (e.g., the work
wardsbetweensuchregions.Thegeneralformofthispro- byEgneretal.2010andbyMurrayetal.2002)isdiscussed
posal(asBridgemanproperlystresses)isnotnew.Ithasa inthetext, butnew evidence (see, e.g.,Wyart et al.2011)
long history in mainstream work in neuroscience and psy- continues toemerge.In their commentary Egner & Sum-
chology that depicts cortex as coding not for properties of merfield stress, however, that complex questions remain
the stimulus but for the differences (hence the “news”) concerning the origins of such surprise. Is it locally com-
between theincoming signal and theexpected signal. puted or due to predictions issuing from elsewhere in the
PP goes further, however, by positing a specific proces- brain? My own guess is that both kinds of computation
sing regime that seems to require functionally distinct occur, and that complex routing strategies (see Phillips
encodings for prediction and prediction error. Spratling et al. 2010 and essays in von der Marlsberg et al. 2010)
notes, helpfully, that the two key elements of this determine, on a moment-to-moment basis, the bodies of
complex (the use of a hierarchical probabilistic generative knowledge and evidence relative to which salient (i.e.,
model, and the predictive coding data compression precise, highly weighted) prediction error is calculated. It
device) constitute what he describes as an “intermediate- is even possible that these routing effects are themselves
234 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
drivenbypredictionerrorsofvariouskinds,perhapsinthe further defended in his revealing commentary. PP is,
manner sketched by den Ouden et al. (2010). Egner & however, deliberately pitched between these two
Summerfieldgoontonote(seeWN,sect.3.1)thecontin- extremes. It is committed to a general cortical processing
ued absence of firm cellular-level evidence for the exist- strategy that minimizes surprisal using sensorimotor loops
ence of functionally distinct neural encodings for that sample the environment while deploying multilevel
expectation and surprise. More positively, they highlight generative models to predict the ongoing flow of
some recent studies (Eliades & Wang 2008; Keller et al. sensation.
2012; Meyer & Olson 2011) that offer tantalizing hints of Friston’sfocusisonapresumedbiologicalimperativeto
such evidence. Especially striking here is the work by reduce surprisal: an imperative obeyed by reducing the
Kelleretal.(2012)offeringearlyevidencefortheexistence organism-computablequantityfreeenergy.Bothpredictive
of prediction-error neurons in supra-granular layers 2/3, codingandtheBayesianbrainare,Fristonargues,resultsof
which fits nicely with the classic proposals (implicating this surprise minimization mandate. The kinds of proces-
superficial pyramidal cells) by Friston (2005), Mumford sing regime PP describes are thus, Friston claims, the
(1992), and others. Such work represents some early results of surprisal minimization rather than its cause.
steps along the long and complex journey that cognitive Friston may be right to stress that, assuming the free
science must undertake if it is deliver evidence of the energy story as he describes it is correct, predictive
kind demandedby Rasmussen & Eliasmith. coding and the Bayesian brain emerge as direct conse-
Muckli, Petro, & Smith (Muckli et al.) continue this quences of that story. But I do not think the target article
positive trend,describingarange ofintriguingandimpor- displays confusion on this matter. Instead, the issue turns
tant experimental results that address PP at both abstract on where we want to place our immediate bets, and
and more concrete levels of description. At the abstract perhaps on the Aristotelian distinction between proximate
level, they present ongoing experiments that aim to and ultimate causation. Thus, the proximal cause (the
isolate the contributions of cortical feedback (downward- mechanism) of large amounts of surprisal reduction may
flowing prediction) from other processing effects. Such well be the operation of a cortical predictive processing
experiments lend considerable support to the most basic regime, even if the ultimate cause (the explanation of the
tenets of the PP model. Moving on to the more concrete presence of that very mechanism) is a larger biological
level they suggest, however, that the standard implemen- imperative for surprisalminimization itself. Thisseems no
tation of predictive coding may not do justice to the full stranger than saying that the reproductive advantages of
swathe of emerging empirical data, some of which (Kok distal sensing (an ultimate cause) explain the presence of
et al. 2012) shows both sharpening of some elements of various specific mechanisms (proximal causes) for distal
theneuronalsignal,aswellasthekindofdampeningman- sensing,suchasvisionandaudition.WN,however,deliber-
dated by successful “explaining away” of sensory data. ately took no firm position on the full free energy story
However, as mentioned in WN sect. 2.1 (see also com- itself.
ments on Bowman, Filetti, Wyble, & Olivers Friston also notes,importantly, that other ideas that fit
[Bowman et al.] below), this combination is actually withinthisgeneralframeworkincludeideasaboutefficient
fully compatible with the standard model (see, e.g., coding. This is correct, and I regard it as a shortfall of my
remarks in Friston 2005), since explaining away releases treatment that space precluded discussion of this issue.
intra-level inhibition, resulting in the correlative sharpen- For, as Trappenberg & Hollensen nicely point out,
ing of some parts of the activation profile. I agree, dimensionality reduction using generative models will
however, that more needs to be done to disambiguate only yield neurally plausible encodings (filters that
and test various nearby empirical possibilities, including resemble actual receptive fields in the brain) if there is
theimportantquestionsaboutspatialprecisionmentioned pressure to minimize both prediction error and the com-
laterinMucklietal’sinterestingcommentary.Suchexper- plexity of the encoding itself. The upshot of this is
iments wouldgosomewaytowardsaddressingtherelated pressure towards various forms of “sparse coding”
issues raised bySilverstein,who worries that PP (by sup- running alongside the need to reduce prediction error at
pressing well-predicted signal elements) might not grace- multiple spatialandtemporalscales,andin someaccepta-
fully accommodate cases in which correlations between bly generalizable fashion. Trappenberg & Hollensen
stimulus elements are crucial (e.g., when coding for suggest that we still lack any concrete model capable of
objects) and need to be highlighted by increasing (rather learning to form such sparse representations “due to the
than suppressing) activity. It is worth noting, however, world’s sparseness” rather than due to the pre-installation
thatsuchcorrelationsformtheveryheartofthegenerative of some form of pressure (e.g., an innate hyperprior)
models that are used to predict the incoming sensory pat- towards sparse encodings. But this may be asking too
terns. This fact, combined with the co-emergence of both much, given the quite general utility of complexity
sharpening and dampening, makes the PP class of models reduction. Reflecting on the sheer metabolic costs of
well-suitedtocapturingthefullgamutofobservedeffects. creating and maintaining internal representations, such a
I turn now to the relation between key elements of PP bias seems like a very acceptable ingredient of any
and the depiction of the brain as performing Bayesian “minimal nativism” (Clark 1993).
inference. Trappenberg & Hollensen note that the
space of Bayesian models is large, and they distinguish
between demonstrations of Bayesian response profiles in R2.2. Othermechanisms
limited experimental tasks and the much grander claim I move nowtoasecondsetofperils, or challenges. These
that that such specifics flow from something much more challenges concern the relation between PP and various
general and fundamental. The latter position is most other strategies and mechanisms plausibly implicated in
strongly associated with the work of Karl Friston, and is human cognitive success. Ross draws our attention to a
BEHAVIORALANDBRAINSCIENCES(2013)36:3 235
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/AndyClark: Predictivebrains,situated agents,and thefutureof cognitive science
large and important body of work on “neuroeconomic generative models in cognitive science (e.g., Dayan
models of sub-cognitive reward valuation.” Such models et al.’s [1995] work on the Helmholz machine, leading to
(e.g., Lee & Wang 2009; Glimcher 2010) posit pre-com- all the work on “deep learning”–see Bengio 2009) I was
puted reward valuations (outputs from specialized subsys- careful to highlight their role in dealing with cases where
tems performing “striatal valuation”) as the inputs to successful learning required deriving new representations
more flexible forms of cortical processing. But despite my tracking hidden variables. As the story progressed, the
intended emphasis on cortical processing, nothing in the role of complex multilevel models learnt and deployed
PP story was meant to stand in the way of such modes of using bidirectional hierarchies (as most clearly
influence.Tobesure,Friston’sown(“desert landscape”– implemented by the cortex) was constantly center stage.
seeWN,sects.1.5and5.1)attempttoreplacerewardand The larger free energy story, to be sure, covers both the
valuesignalswithmultilevelexpectationsmayatfirstsight knowledge-rich and knowledge-sparse cases. From the
seem inimical to such approaches. But Friston’s account free energy minimization perspective we might even
ends up accommodating such modes of influence (see, e. choosetoconsider(asdoesFriston)thewholeembodied,
g., Friston 2011b), albeit with an importantly different embedded agent as “themodel” relative towhich surprise
functional and terminological spin. Here (see WN, sect. is (long-term) minimized. But that story, in turn, does not
3.2, and the commentary by Friston), it is important to conflate the two senses of prediction either, since it
recognize that predictions and expectations, in Friston’s fluidly covers both. Anderson & Chemero suggest that
large-scale free energy treatments, are determined by the Isomehowrelyonthe(veryspeculative)modelofbinocu-
shapeandnatureofthewholeagent(morphology,reflexes, larrivalrytomakeanillegitimatemovefromaknowledge-
and subcortical organization included) and are not merely free to a knowledge-rich understanding of prediction.
the products of probabilistic models commanded by Here, the exposition in WN must be at fault. It may be
sensory and motor cortex. Insights concerning the impor- that they think the account of rivalry plays this role
tance of the mid-brain circuitry are compatible both with becauseIprecededitwithsomeremarksondynamicpre-
PPandwiththefull“desertlandscape”versionofFriston’s dictivecodingbytheretina.Buttheretinalcase,whichmay
ownaccount.Thismeans,incidentally,thatthekindofnon- indeed beunderstoodasessentiallyknowledge-sparseand
cortical route to a (partial) resolution of the Darkened internal-model-freeprediction,wasmeanttoillustrateonly
Room problem suggested by Ross (and hinted at also by thepredictivecodingdatacompressiontechnique,andnot
Shea) is in fact equally available to Friston. It is also con- the full PP apparatus. Nor did I intend anything much to
sistentwith(thoughitisnotimpliedby)themorerestricted turn on the binocular rivalry story itself, which was meant
perspectiveofferedbyPP,understoodasanaccountofcor- merely as a helpful illustration of how the hypothesis-
tical processing. testing brain might deploy a multi-layered model. It is
Ross’sconcernthatPPmaybelosingsightofthecrucial clear that much more needs to be done to defend and
role played by non-cortical (e.g., environmental, morpho- flesh out that account of binocular rivalry (as also pointed
logical, and subcortical) organization is amplified by out by Sloman).
Anderson&Chemero,whofearthatPPputsusonaslip- Anderson & Chemero believe that an account might
pery slope back to full-blown epistemic internalism of the be given that delivers the rivalry response by appealing
kind I am supposed to have roundly and convincingly solely to “low-level, knowledge-free, redundancy-reducing
(Clark1997;2008)rejected.That slopeisgreased, Ander- interactions between the eyes.” This might turn out to be
son & Chemero suggest, by the conflation of two very true, thus revealing the case as closer to that of the
differentsensesofprediction.Inthefirstsense,prediction retinalganglioncellsthantoanycaseinvolvinghierarchical
amounts to nothing more than correlation (as in “height predictive processing as I defined it. There are, however,
predictsweight”),sowemightfind“predictiveprocessing” very many cases that simply cry out for an inner model–
whereverwefindprocessingthatextractsandexploitscor- invokingapproach.Thus,considerthecaseofhandwritten
relations.ThissenseAnderson&Chemeroregardasinno- digit recognition. This is a benchmark task in machine
cent because (involving merely “simple relationships learning,andonethatHintonandNair(2006)convincingly
between numbers”) it can be deployed without reliance treat usinga complex acquired generativemodel that per-
upon inner models, in what they call a model-free or forms recognition using acquired knowledge about pro-
even “knowledge-free” (I would prefer to say “knowl- duction. The solution is knowledge-rich because the
edge-sparse”) fashion so as to make the most of, for domainitselfishighlystructured,exhibiting(liketheexter-
example, reliable cross-modal relationships among sensed nalworldingeneral)manystackedandnestedregularities
information. The second sense is more loaded and “allied that are best tracked by learning that unearths multiple
with abductive inference and hypothesis testing.” It interacting hidden variables. I do not think that such
involves the generation of predictions using internal cases can be dealt with (at least in any remotely neurally
models that posit hidden variables tracking complex plausible fashion) using resources that remain knowledge-
causalstructureinthebodyandworld.Predictionthuscon- free in the sense that Anderson & Chemero suggest.
strued is, let us agree, knowledge-rich. Evidence for the Whatseemstrue(Clark1989;1997;2008)isthattowhat-
utility and ubiquity of prediction in the knowledge-free ever extent a system can avoid the effort and expense of
(or knowledge-sparse) sense provides, just as Anderson & learning about such hidden causes, and rely instead on
Chemeroinsist,noevidencefortheubiquityandoperation surface statistics and clever tricks, it will most likely do
(norevenforthebiologicalpossibility)ofpredictiveproces- so. Much of the structure we impose (this relates also to
sing inthe second (knowledge-rich)sense. the comments by Sloman) upon the designed world is, I
This is undeniably true and important. But nowhere in suspect, a device for thus reducing elements of the pro-
the target article did I make or mean to imply such a blems we confront to simpler forms (Clark & Thornton
claim. In displaying the origins of this kind of use of 1997). Thus, I fully agree that not all human cognition
236 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
depends upon the deployment of what Anderson & whatlooksfromoneperspectivetobeamultiple,fragmen-
Chemero call “high-level, knowledge-rich predictive ted, and disconnected cognitive economy may, on deeper
coding.” examination, turn out to be a well-integrated (though by
What kind of overall cognitive organization, it might be nomeanshomogeneous)mechanismrespondingtoorgan-
asked, does the embodied, embedded agent then display? ism-relevant statistical structurein the environment.
Is that organization multiply and impenetrably fractured Gerrans continues the theme of fragmentation, resist-
and firewalled, comprising a motley within which a few ing the claim that prediction error minimization proceeds
principled, knowledge-rich responses bed down with seamlessly throughout the cortical hierarchy. His test
unwashed legions of just-good-enough ploys and strata- cases are delusions of alien control. I agree with Gerrans
gems? Surely such a motley is incompatible with the that nothing in the simple story about prediction error
hope for any kind of unifying treatment? This issue (let’s minimization explains why it seems that someone else is
call it the Motley Challenge) is among the deepest unre- incontrol,ratherthansimply(asintheothercaseshemen-
solved questions in cognitive science. Buckingham & tions)thattheactionisnotunderourowncontrol.Itisnot
Goodale join Ross and Anderson & Chemero, and (as cleartome,however,whythatshortfallshouldbethought
Idiscusslater)SlomanandFroese &Ikegami,inpress- to cast doubt on the more general (“seamlessness”) claim
ing the case for the cognitive motley. Following a crisp that perception phases gently into cognition, and that the
description of the many successes of Bayesian (i.e., differences concern scale and content rather than under-
optimal cue integration, given prior probabilities) models lying mechanism.
in the field of motor control and psychophysics, Bucking- Silversteinraisessomeimportantchallengesbothtothe
ham & Goodale turn to some problem cases–cases suggestionthatPPprovidesanadequatelygeneralaccount
where Bayesian style optimal integration seems to fail– oftheemergenceofdelusionsandhallucinationsinschizo-
usingthesetoargueforafracturedandfirewalledcognitive phrenia, and (especially) to any attempt to extend that
economy displaying “independent sets of priors for motor account tocover other cases (such asCharles Bonnet syn-
control and perceptual/cognitive judgments, which ulti- drome) in which hallucinations regularly emerge without
mately serve quite different functions.” Poster-child for delusions. Importantly, however, I did not mean to
this dislocation is the size-weight illusion in which similar- suggest that the integrated perceptuo-doxastic account
looking objects appear weight-adjusted so that we judge that helps explain the co-emergence of the two positive
the smaller one to feel heavier than the larger despite symptoms in schizophrenia will apply across the board.
their identical objective weights (a pound of lead feels What might very reasonably be expected, however, is that
heavier, indeed, than a pound of feathers). Buckingham other syndromes and patterns (as highlighted by
& Goodale survey some intriguing recent work on the Gerrans)shouldbeexplicableusingthesamebroadappar-
size-weight illusion, noting that although Bayesian treat- atus,thatis,asaresultofdifferentformsofcompromiseto
ments do manage to get a grip on lifting behavior itself, the very same kind of prediction-error–sensitive cognitive
they fail to explain the subjective comparison effect economy. In Charles Bonnet syndrome (CBS), gross
which some describe as “anti-Bayesian” since prior expec- damage to the visual system input stream (e.g., by lesions
tancies and sensory information there seem contrasted to the pathway connecting the eye to the visual cortex, or
rather than integrated (Brayanov &Smith 2010). by macular degeneration) leads to complex hallucinations
Isthisacaseofmultiple,independentlyoperatingpriors without delusion. But this pattern begins to makes sense
governing various forms of response under various con- if we reflect that the gross damage yields what are effec-
ditions?Perhaps.ThefirstpointIwouldmakeinresponse tively localized random inputs that are then subjected to
isthatnothingeitherinPPorinthefullfree-energyformu- the full apparatus of learnt top-down expectation (see
lation rules this out. For the underlying architecture, by Stephan et al. 2009, p. 515). Recent computational work
dint of evolution, lifetime learning, or both, may come to by Reichert et al. (2010) displays a fully implemented
include “soft modules” partially insulating some response model in which hallucinations emerge in just this broad
systems from others. To the extent that this is so, that fashion,reflectingtheoperationofahierarchicalgenerative
may betraceable,asFristonsuggests,to therelative stat- (predictive) model of sensory inputs in which inputs are
isticalindependenceofvariouskeytrackedvariables.Infor- compared with expectations and mismatches drive further
mation about what an object is, for example, tells us little processing. The detailed architecture used by Reichert
about where it is, and vice versa, a fact that might explain et al. was, however, a so-called Deep Boltzmann Machine
the emergence of distinct (though not fully mutually insu- architecture (Salakhutdinov & Hinton 2009), a key com-
lated–see Schenk & McIntosh 2010) “what” and “where” ponent of which was a form of homeostatic regulation in
pathways in the visual brain. Returning to the size-weight whichprocessingelementslearnapreferredactivationlevel
illusion itself,ZhuandBingham(2011)showthattheper- towhichtheytend,unlessfurtherconstrained,toreturn.
ceptionofrelativeheavinessmarchesdelicatelyinstepwith Phillips draws attention to the important question of
theaffordanceofmaximum-distancethrowability.Perhaps, how a PP-style system selects the right sub-sets of infor-
then, what we have simply labeled as the experience of mation upon which to base some current response. Infor-
“heaviness”is,insomedeeperecologicalsense,theexperi- mation that is critical for one task may be uninformative
ence of optimal weight-for-size to afford long-distance or counter-productive for another. Appeals to predictive
throwability? If that were true, then the experiences that coding or Bayesian inference alone, he argues, cannot
Buckingham & Goodale describe re-emerge as optimal provide this. One way in which we might cast this issue, I
perceptsforthrowability,albeitonesthatweroutinelymis- suggest, is by considering how to select what, at any given
conceive as simple but erroneous perceptions of relative moment, to try to predict. Thus, suppose we have an
objectweight.TheZhuandBinghamaccountisintriguing incomingsensorysignalandanassociatedsetofprediction
butremainsquitespeculative.Itremindsus,however,that errors.Foralmostanygivenpurpose,itwillbebestnotto
BEHAVIORALANDBRAINSCIENCES(2013)36:3 237
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/AndyClark: Predictivebrains,situated agents,and thefutureof cognitive science
botheraboutsomeelementsofthesensorysignal(ineffect, model in which precision-modulated prediction error is
totreatpredictionfailuresthereasnoiseratherthansignal). usedtooptimizeperceptualinferenceinawaythatrepro-
Other aspects, however, ones crucial to the task at hand, duces the ERP and psychophysical responses elicited by
will have to be got exactly right (think of trying to spot thePosner spatial cueing paradigm (see Posner 1980).
the four-leaf clover among all the others in a field). To do Bowmanetal.goontopressanimportantfurtherques-
this, the system must treat even small prediction errors, tion concerning feature-based attention. For, feature-
in respect of such crucial features, as signal and use them based attention seems to allow us to enhance response to
to select and nuance the winning top-down model. a given feature even when it appears at an unpredicted
WithinthePPframework,theprimarytoolforthisis,Phil- location.Intheirexample,thecommandtofindaninstance
lips notes, the use of context-sensitive gain control. This of bold type may result in attention being captured by a
amplifies the effects of specific prediction error signals nearby spatial location. If the result of that is to increase
while allowing other prediction errors to self-cancel (e.g., the precision-weighting upon prediction error from that
byhavingthaterrorunitself-inhibit).Thesamemechanism spatial location (as PP suggests) that seems to depict the
allows estimates of the relative reliability of different precision weighting as a consequence of attending rather
aspects of the sensory signal to be factored in, and it may thanacauseorimplementationofattending.Theresolution
underpin the recruitment of problem-specific temporary ofthispuzzlelies,Isuggest,inthepotentialassignmentof
ensembles of neural resources, effectively gating infor- precision-weighting atmanydifferentlevelsoftheproces-
mation flow between areas of the brain (see den Ouden singhierarchy.Feature-basedattentioncorresponds,intui-
et al. [2009] and essays in von der Marlsburg et al. tively, to increasing the gain on the prediction error units
[2010]). On-the-hoof information selection and infor- associated with the identity or configuration of a stimulus
mation coordination of these kinds is, Phillips then (e.g.,increasingthegainonunitsrespondingtothedistinc-
argues, a primary achievement of the neurocomputational tive geometric pattern of a four-leaf clover). Boosting that
theory known as “Coherent Infomax” (Kay & Phillips response (by giving added weight to the relevant kind of
2010; Phillips et al. 1995). Both Coherent Infomax and sensory prediction error) should enhance detection of
PP emphasize the role of prediction in learning and that featural cue. Once the cue is provisionally detected,
response,anditremainstobedeterminedwhetherCoher- the subject can fixate the right spatial region, now under
entInfomaxisbestseenasanalternativeor(morelikely)a conditionsof“four-leaf-clover-there”expectation.Residual
complementtothePPmodel,amountingperhapstoamore erroristhenamplifiedforthatfeatureatthatlocation,and
detaileddescriptionofacorticalmicrocircuitabletoactasa highconfidenceinthepresenceofthefour-leafclovercan
repeated component in the construction of a PP (if you are lucky!) be obtained. Note that attending to the
architecture. wrong spatial region (e.g., due to incongruent spatial
cueing) will actually be counter-productive in such cases.
Precision-weighted prediction error, as I understand it, is
R2.3. Attentionandprecision
thus able to encompass both mere-spatial and feature-
Thisbringsustoourthirdsetofperils:perilsrelatingtothe based signal enhancement.
treatment of attention as a device for upping the gain on Block & Siegel claim that predictive processing (they
(hence the estimated “precision” of) selected prediction speak simply of predictive coding, but they mean to
errors. Bowman et al. raise several important issues con- target the full hierarchical, precision-modulated, genera-
cerning the scope and adequacy of this proposal. Some tive-model based account) is unable to offer any plausible
ERP (event-related potential) components (such as P1 ordistinctiveaccountofverybasicresultssuchastheatten-
and N1), Bowman et al. note, are increased when a target tional enhancement of perceived contrast (Carrasco et al.
appears repeatedly in the same location. Moreover, there 2004). In particular, they claim that the PP model fails to
are visual search experiments in which visual distractors, capture changes due to attending that precede the calcu-
despite their rarity, yield little evoked response, yet pre- lation of error, and that it falsely predicts a magnification
described, frequently appearing, targets deliver large of the changes that follow from attending (consequent
ones. Can such effects be explained directly by the atten- upon upping the gain on some of the prediction error).
tion-modulated precision weighting of residual error? A However,IfindBlock&Siegel’sattemptedreconstruction
recent fMRI study by Kok et al. (2012) lends elegant of the PP treatment of such cases unclear or else impor-
support to the PP model of such effects by showing that tantly incomplete. In the cases they cite, subjects fixate a
these are just the kinds of interaction between prediction central spot with contrast gratings to the left and right.
andattentionthatthemodelofprecision-weightedpredic- The gratings differ in absolute (actual) contrast. But
tionerrorsuggests.Inparticular,Koketal.showthatpre- when subjects are cued to attend (even covertly) to the
dictedstimulithatareunattendedandtask-irrelevantresult lower contrast grating, their perception of the contrast
inreducedactivityinearlyvisualcortex(the“silencing”of there is increased, yielding the (false) judgment that, for
the predicted, as mandated by simple predictive coding) example, an attended 70% (actual value) contrast grating
but that “this pattern reversed when the stimuli were isthe same as an unattended 82% grating. Block & Siegel
attended and task-relevant” (Kok et al. 2012, p. 2198). suggest that the PP account cannot explain the initial
The study manipulated spatial attention and prediction by effect here (the false perception of an 82% contrast for
using independent prediction and spatial cues (for the the covertly attended 70% contrast grating) as the only
details, see the original paper by Kok et al.) and found error signal–but this is where they misconstrue the
that attention reversed the silencing effect of prediction story–is the difference between the stable pre-attentive
upon the sensory signal, in just the way the precision- 70% registration and the post-attentive 82% one. But this
weighting account would specify. In addition, Feldman difference,theyworry,wasn’tavailableuntilafterattention
and Friston (2010) present a detailed, simulation-based had done its work! Worse still, once that difference is
238 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
available, shouldn’t it be amplified once more, as the PP which reach out to the larger organizational forms of
account says that gain on the relevant error units is now music, culture, and group behaviors.
increased?
This is an ingenious challenge, but it is based on a mis-
construal oftheprecision-weighting proposal. It isnot the R3.1. Newdimensions
case that PP posits an error signal calculated on the basis
Shea usefully points out that perception and action, even
of a difference between the unattended contrast (regis-
assumingtheyindeedsharedeepcomputationalcommon-
tered as 70%) and the subsequently attended contrast alities,wouldstilldifferinrespectoftheir“directionoffit.”
(now apparently of 82%). Rather, what attention alters is
In(rich,world-revealing)perception,wereduceprediction
the expectation of precise sensory information from the
error by selecting a model that explains away the sensory
attended spatial location. Precision is the inverse of the
signal. In world-engaging action, we reduce prediction
variance, and it is our “precision expectations” that atten-
errorbyalteringbodyandworldtoconformtoourexpec-
tion here alters. What seems to be happening, in the case
tations.Thisiscorrect,andithelpsshowhowthePPframe-
athand,isthattheveryfactthatwecovertlyattendtothe
work, despite offering a single fundamental model of
grating on the left (say) increases our expectations of a
cortical processing, comports with the evident multiplicity
precise sensory signal. Under such conditions, the expec-
tationofpreciseinformationinducesaninflatedweighting and variety offorms ofcognitive contact with theworld.
Farmer, Brown, & Tanenhaus (Farmer et al.)
for sensory error and our subjective estimate of the con-
suggest (this was music to my ears) that the hierarchical
trast is distorted as a result. The important point is that
prediction machine perspective provides a framework
the error is not computed, as Block & Siegel seem to
that might one day “unify the literature on prediction in
suggest, as a difference between some prior (in this case
language processing.” They describe, in compelling detail,
unattended) percept and some current (in this case
the many applications of prediction-and-generative-
attended) one. Instead, it is computed directly for the
model-basedaccountstolinguisticphenomena.Language,
present sensory signal itself, but weighted in the light of
indeed, is a paradigm case of an environmental cause that
our expectation of precise sensory information from that
exhibitsacomplex,multilevelstructureaptforengagement
location. Expectations of precision are what, according to
using hierarchical, generative models. Farmer et al. stress
PP, is being manipulated by the contrast grating exper-
several aspects of language comprehension that are hard
iment, and PP thus offers a satisfying and distinctive
to explain using traditional models. All these aspects
accountoftheeffectitself.Thissamemechanismexplains
revolve(itseemstome)aroundthefactthatlanguagecom-
the general effect of attention on spatial acuity, especially
in cases where we alter fixation and where more precise prehension involves not “throwing away” information as
processing proceeds, so much as using all the information
information is indeed then available. Block & Siegel are
available (in the signal, in the generative model, and in
right to demand that the PP framework confront the full
the context) to get a multi-scale, multi-dimensional grip
spectrum of established empirical results in this area.
ontheevolving acousticandsemanticcontent.Allmanner
But they underestimate the range of apparatus (and the
of probabilistic expectation (including speaker-specific
distinctiveness of the accounts) that PP can bring to
lexical expectations formed “on-the-hoof” as conversation
bear. This is not surprising, since these are early days
proceeds)arethusbroughttobear,andimpactnotjustrec-
and much further work is needed. For an excellent
ognition but production (e.g., your own choice of words),
taste, however, of the kind of detailed, probing treatment
too. Context effects, rampant on-the-hoof probability
of classic experimental results that is already possible, see
updating,andcross-cueingareallgristtothePPmill.
Hohwy’s (2012) exploration of conscious perception,
The PP framework, Holm & Madison convincingly
attention, change blindness, and inattentional blindness
argue,alsolendsitselfextremelynaturallytothetreatment
from the perspective of precision-modulated predictive
of timing and of temporal phenomena. In this regard,
processing.
Holm&Madisondrawourattentiontolargeandimportant
bodiesofworkthatdisplaythecomplexdistributionoftem-
poralcontrolwithinthebrain,andthatsuggestatendency
R3. Prospects of later processing stages and higher areas to specialize in
more flexible and longer time-scale (but correlatively less
I have chosen to devote the bulk of this Response to dedicated, and less accurate) forms of time-sensitive
addressing the various perils and pitfalls described above control. Such distributions, as they suggest, emerge natu-
and to some even grander ones to be addressed in rally within the PP framework. They emerge from both
section 4 further on. A reassuringly large number of com- thehierarchicalformofthegenerativemodelandthedyna-
mentators,however,haveofferedilluminatingandwonder- mical and multi-scale nature of key phenomena. More
fully constructive suggestions concerningways in which to specifically, the brain must learn a generative model of
improve, augment, and extend the general picture. I’m coupled dynamical processes spanning multiple temporal
extremely grateful for these suggestions, and plan to scales(aniceexampleisFristonandKiebel’s[2009]simu-
pursue several of them at greater length in future work. lationofbirdsongrecognition).Holm&Madison(andsee
For present purposes, we can divide the suggestions into comments by Schaefer, Overy, & Nelson [Schaefer
two main (though non-exclusive) camps: those which add et al.]) also make the excellent point that action (e.g.,
detail or further dimensions to the core PP account, tapping with hands and feet) can be used to bootstrap
extending it to embrace additional mental phenomena, timing, and to increase the reliability of temporal percep-
such as timing, emotion, language, personal narrative, tion. This provides an interesting instance of the so-called
and high-level forms of “self-expectation”; and those “self-structuring of information” (Pfeifer et al. 2007), a
BEHAVIORALANDBRAINSCIENCES(2013)36:3 239
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/AndyClark: Predictivebrains,situated agents,and thefutureof cognitive science
key cognitive mechanism discussed in Clark (2008) and in cuteness of the baby, if I read Dennett correctly, is
thetarget article(see WN,sect.3.4). nothing over and above our expectations concerning our
Gowaty & Hubbell suggest that all animals are Baye- probable reactions (themselves rooted, if the PP story is
siansengagedinpredictingthefuture onthebasisofflex- correct, in a bunch of probabilistic expectations) to immi-
ibly updated priors, and that they “imagine” (the scare nentbaby-exposure.Weexpecttofeellikecooingandnur-
quotes are theirs) alternatives and make choices among turing, and when those expectations (which can, in the
them. This is an intriguing hypothesis, but it is one that manner of action-oriented predictive processing, be par-
remains poised (thanks in part to those scare quotes) tially self-fulfilling) are met, we deem the baby itself cute.
between two alternative interpretations. On the one This is what Dennett (2009) describes as a “strange inver-
hand,thereisthe(plausible)claimthatelementsinthesys- sion,” in which we seem to project our own reactive com-
temic organization of all animals respond sensitively, at plexes outward, populating our world with cuteness,
various timescales, to environmental contingencies so as sweetness, blueness, and more. I think there is something
to minimize free energy and allow the animals to remain exactlyright,andsomethingthatremainsunclear,inDen-
within their envelope of viability. On the other hand, nett’ssketch.Whatseemsexactlyrightisthatweourselves
there is the (to me less plausible) claim that all animals turnupasonecrucialitemamongthemanyitemsthatwe
ground flexible behavioral response in the top-down humans model when we model our world. For, we our-
deployment of rich, internally represented generative selves (not just as organisms but as individuals with
modelsdevelopedandtunedusingprediction-drivenlearn- unique histories, tendencies, and features) are among the
ing routines of the kind described by PP. I return to this manythingsweneedtogetagripuponifwearetonavigate
issue in section 4. the complex social world, predicting our own and others’
Seth&Critchleysketchapowerfulandpotentiallyvery responses tonew situations, threats, andopportunities.
importantbridgebetweenPP-styleworkandnewcognitive To that extent (see also Friston 2011a), Dennett is
scientific treatments of emotion and affect. The proposed surely right: We must develop a grip (what Dennett
bridge to emotion relies on the idea that interoception describes as a set of “Bayesian expectations”) upon how
(the“senseofthephysiologicalconditionofthebody”)pro- we ourselves are likely to react, and upon how others
videsasourceofsignalsequallyaptforpredictionusingthe modelus.OurUmwelt, asDennettsays,isthuspopulated
kinds of hierarchical generative models described in the not just with simple affordances but with complex expec-
target article The step to emotion is then accomplished tations concerning our own nature and reactions. What
(according to their “interoceptive predictive coding” remains unclear, I think, is just how this complex of ideas
account–see Seth et al. 2011) by treating emotional feel- hooks up the question with which Dennett precedes it,
ings as determined by a complex exchange between namely, “what makes our manifest image manifest (to
drivingsensory(especiallyinteroceptive)signalsandmulti- us)?” For this, on the face of it, is a question about the
level downwards predictions. Of special interest here are origins of consciously perceived properties: the origins of
signals and predictions concerning visceral, autonomic, awareness, or of something like it–something specialthat
andmotorstates.Attentiontopredictions(andpathologies we have and that the elevator (in Dennett’s example)
of prediction) concerning these states provides, Seth & rather plausibly lacks. It does not strike me as impossible
Critchley plausibly suggest, a major clue to the nature that there might be a link here, perhaps even a close one.
and genesis of many psychiatric syndromes. Dissociative But how does it go? Is the thought that any system that
syndromes, for example, may arise from mistaken assign- models itself and has expectations about its own reactive
mentsofprecision(toolittle,inthesecases)tokeyintero- dispositions, belongs to the class of the consciously
ceptivesignals.Butareemotionalfeelingshereconstructed aware?Thatconditionseemsbothtooweak(tooeasilysat-
by successful predictions (by analogy to the exteroceptive isfiedbyasimpleartificialsystem)andtoostrong(asthere
case)? Or are feelings of emotion more closely tied (see maybeconsciousagentswhofailtomeetit).Isitthatany
alsothecommentsbySchaeferetal.regardingprediction system that models itself in that way will at least judge
error in music) to the prediction errors themselves, pre- (perhaps self-fulfillingly) that it is consciously aware of
senting a world that is an essentially moving target, certainthings,suchasthecutenessofbabies?That’stempt-
defined more by what it is not than by what it is? Or ing,butweneedtohearmore.Oristhisreallyjustastory–
might (this is my own favorite) the division between albeit a neat and important one–about how, assuming a
emotionalandnon-emotionalcomponentsitselfproveillu- system is somehow conscious of some of the things in its
sory,atleastinthecontextofamulti-dimensional,genera- world, those things might (if you are a sufficiently bright
tivemodel–nearlyeveryaspectofwhichcanbepermeated and complex social organism under pressure to include
(Barrett&Bar2009)bygoalandaffect-ladenexpectations yourself in your own generative model) come to include
that are constantly checked against the full interoceptive suchotherwiseelusiveitemsascuteness,sweetness,funni-
and exteroceptive array? ness, and soon?
Dennett’s fascinating and challenging contribution fits Hirsh,Mar,&Peterson(Hirshetal.)suggestthatan
naturally, it seems to me, with the suggestions concerning importantfeatureofthepredictivemosaic,whenaccount-
interoceptive self-monitoring by Seth & Critchley. Just ing for distinctively human forms of understanding, might
how could some story about neural prediction illuminate, be provided by the incorporation of personal narratives as
in a deep manner, our ability to experience the baby as high-levelgenerativemodelsthatstructureourpredictions
cute, the sky as blue, the honey as sweet, or the joke as inagoal-andaffect-ladenway.Thisproposalsitswellwith
funny? How, in these cases, does the way things seem to thecomplexofideassketchedbyDennettandbySeth&
us (the daily “manifest image”) hook up with the way Critchley, and it provides, as they note, a hook into the
things actually work? The key, Dennett suggests, may lie important larger sociocultural circuits (see also comments
in our expectations about our own expectations. The by Roepstorff, and section 4 further on) that also sculpt
240 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
and inform human behavior. Personal narratives are often mutual prediction error, in the group case–is reduced.
co-constructed with others, and can feed the structures But this simple idea, they argue, needs augmenting with
andexpectationsofsocietybackinaselementsofthegen- considerations of arousal, affect, and the scaffolding
erativemodelthatanindividualusestomakesenseoftheir effects of cultural, training, and musical style. There is,
own acts and choices. Hirsh et al., like Dennett, are thus Schaeferetal.suggest,anoptimalorpreferredlevelofsur-
concerned with bridging the apparent gap between the prisal at which musical experience leads to maximal (posi-
manifest and scientific image, and accounts that integrate tive) affective response. That level is not uniform across
culturally inflected personal narratives into the general musical types, musical features, or even individuals, some
picture of prediction-and generative-model based cogni- of whom may be more “thrill-seeking” than others. The
tionseemideallyplacedtoplaythisimportantrole.Narra- commentary provides many promising tools for thinking
tivestructures,iftheyarecorrect,lietowardstheverytop about these variations, but makes one claim that I want
ofthepredictivehierarchy,andtheyinfluenceandcanhelp to question (or at any rate probe a little), namely, that
coordinate processing at every level beneath. It is not affectiswhat“makespredictionerrorinmusic…meaning-
obvious to me, however, that personal narrative needs to ful,andindeeddeterminesitsvalue.”Thisistrickyground,
be the concern of a clearly demarcated higher level. butIsuspectitismisleading(seealsocommentsonSeth&
Instead, a narrative may be defined across many levels of Critchley)todepictpredictionerroras,ifyoulike,some-
the processing hierarchy, and supported (in a graded thingthatisgiveninexperience,andthatitselfgeneratesan
rather than all-or-none fashion) by multiple interacting affective response, rather than as that which (sub-person-
bodies ofself-expectation. ally) determines the (thoroughly affect-laden) experience
itself. I am not convinced, that is to say, that I experience
my own prediction errors (though I do, of course, some-
R3.2. Largerorganizationalforms
times experience surprise).
This brings us to some comments that directly target the
larger organizational forms of music, culture, and group
R4. Darkened rooms andthe puzzle ofthe porous
behaviors. Many aspects of our self-constructed sociocul-
perceiver
tural world, Paton, Skewes, Frith, & Hohwy (Paton
et al.) argue, can be usefully conceptualized as devices
R4.1. Darkenedrooms
that increase the reliability of the sensory input, yielding
a better signal for learning and for online response. A Severalcommentators(Anderson&Chemero,Froese&
simple example might be the use of windscreen wipers in Ikegami, Sloman, and to a lesser extent Little &
the rain. But especially illuminating, in this regard, are Sommer) have questioned the idea of surprisal minimiz-
their comments on conversation, ritual, convention, and ationastheunderlyingimperativedrivingallformsofcog-
shared practices. In conversation, speakers and listeners nitionandadaptiveresponse.Arecurrentthreadhereisthe
often align their uses (e.g., lexical and grammatical worry that surprisal minimization alone would incline the
choices–see Pickering & Garrod 2007). This makes good error-minimizing agent to find a nice “darkened room”
senseunderaregimeofmutualpredictionerrorreduction. and just stay there until they are dead. Despite explicitly
But conversants may also, as Paton et al. intriguingly add, bracketing the full free-energy story, WN did attempt (in
aligntheirmentalstatesinakindof“fusionofexpectation sects. 3.2–3.4) to address this worry, with apparently
horizons.”Whensuchalignmentisachieved,theotherwise mixed results. Little & Sommer argue that the solution
bluntandimprecisetoolsofnaturallanguage(seeChurch- proffereddependsunwholesomelyuponinnateknowledge,
land 1989; 2012) can be better trusted to provide reliable or at least upon pre-programmed expectations concerning
information about another’s ideas and mental states. Such the shape (itinerant, exploratory) of our own behavior.
a perspective (“neural hermeneutics”; Frith & Wentzer, Froese & Ikegami contend (contrary to thepicture briefly
in press) extends naturally to larger cultural forms, such explored in WN, sect. 3.2) that good ways of minimizing
as ritual and shared practice, which (by virtue of being surprisalwillinclude“stereotypicself-stimulation,catatonic
shared) enhance and ensure the underlying alignment withdrawal from the world, and autistic withdrawal from
that improves interpersonal precision. Culture, in this others.”
sense, emerges as a prime source of shared hyperpriors Hintsofasimilarworrycanbefoundinthecommentsby
(high-level shared expectations that condition the lower- Schaefer et al., who suggest that musical appreciation
level expectations that each agent brings to bear) that involves not the simple quashing of prediction error
helpmakeinterpersonalexchange bothpossibleandfruit- (perhaps that might be achieved by a repeated pulse?)
ful. Under such conditions (also highlighted by Roep- but attraction towards a kind of sweet spot between pre-
storff) we reliably discern each other’s mental states, dictability and surprise: an “optimal level of surprisal,”
inferringthemasfurtherhiddencausesintheinterpersonal albeit one that varies from case to case and between indi-
world. Natural hermeneutics may thus contribute to the viduals and musical traditions. As a positive suggestion,
growing alignment between the humanities and the Little & Sommer then suggest we shift our attention
sciences of mind (Hirsh et al.). At the very least, this fromtheminimizationofpredictionerrortothemaximiza-
offers an encompassing vision that adds significant dimen- tion of mutual information. That is to say, why not depict
sions to the simple idea of mutual prediction error the goal as maximizing the mutual information (on this,
reduction. see also Phillips) between an internal modelof estimated
Schaefer et al. combine the themes of mutual predic- causesandthesensoryinputs?Minimizingentropy(predic-
tion error reduction, culture, and affect. Their starting tionerror)andmaximizingmutualinformation(hencepre-
point is the idea that music (both in perception and pro- diction success), Little & Sommer argue, each deliver
duction) creates a context within which prediction error– minimal prediction error but differ in how they select
BEHAVIORALANDBRAINSCIENCES(2013)36:3 241
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/AndyClark: Predictivebrains,situated agents,and thefutureof cognitive science
actions. A system that seeks to maximize mutual infor- information. This also means that the suggestion (Froese
mation won’t, they suggest, fall into the dark room trap. &Ikegami)thatenactivismoffersanalternativeapproach,
For,itisdriveninsteadtowardsasweetspotbetweenpre- withadistinctiveresolutionofthedarkroomissue,ismis-
dictability and complexity and will “seek out conditions in guided. Indeed, the “two” approaches are, with respect to
whichitssensoryinputsvaryinacomplex,butstillpredict- the darkened room issue at least, essentially identical.
able, fashion.” Each stresses the autonomous dynamics of the agent.
Manyinterestingissuesariseatthispoint.Forexample, Each depicts agents as moving through space and time in
wemightalsowanttominimizemutualinformation(redun- waysdeterminedby“theviabilityconstraintsoftheorgan-
dancy) among outputs (as opposed to between inputs and ism.”Eachgroundsvalue,ultimately,inthoseviabilitycon-
model)soastoachievesparse,efficientcoding(Olshausen straints (which are the essential backdrop to any richer
&Field1996).Butforpresentpurposes,themainpointto forms of lifetime learning).
make is that any improvement afforded by the move to Froese & Ikegami also take PP (though they dub it
mutual information is, as far as I can determine, merely HPM: the “Hierarchical Prediction Machine” story) to
cosmetic. Thus, consider a random system driven towards taskforitscommitmenttosomeformofrepresentational-
some sweet spot between predictability and complexity. ism.Thiscommitmentleads,theyfear,toanunacceptable
For that system, there will be some complex set of inputs internalism (recall also the comments from Anderson &
(imagine, to be concrete, a delicate, constantly changing Chemero) and to the unwelcome erection of a veil
stream of music) such that the set of inputs affords, for between mind and world. This issue arises also (although
that agent, the perfect balance between predictability and fromessentiallytheoppositedirection)inthecommentary
complexity. The musical stream can be as complex as you by Paton et al. Thus, Froese & Ikegami fear that the
like. Perhaps it must be so complex as never quite to depictionofthecerebralcortexascommandingprobabilis-
repeat itself. Surely the agent must now enter the ticinternalmodelsoftheworldputstheworld“off-limits,”
“musical room” and stay there until it is dead? The whilePatonetal.suggestthatmypreferredinterpretation
musical room, I contend, is as real (and, more important, ofthePPmodelmakesthemind–worldrelationtoodirect
as unreal) a danger as the darkened room. Notice that and obscures the genuine sense in which “perception
you can ramp up the complexity at will. Perhaps the remains an inferred fantasy about what lies behind the
sweet spot involves complex shifts between musical types. veilofinput.”Ifindthisstrangelycheering,asthesediame-
Perhapsthelocationofthesweetspotvariessystematically trically opposed reactions suggest that the account is, as
with the different types. Make the scenario as complex as intended, walking a delicate but important line. On the
you wish. For that complexity, there is some musical onehand,Iwanttosaythatperception–rich,world-reveal-
roomthatnowlookssettoactasadeathtrapforthatagent. ingperceptionofthekindthatwehumansenjoy–involves
Thereis,ofcourse,aperfectlygoodwayoutofthis.Itis the top-down deployment of generative models that have
tonotice,withFriston,thatallthekeyinformation-theor- come, courtesy of prediction-driven learning within the
eticquantitiesaredefinedandcomputedrelativetoatype bidirectionalcorticalhierarchy,toembodyrich,probabilis-
of agent–a specific kind of creature whose morphology, ticknowledgeconcerningthehiddencausesofoursensory
nervous system, and neural economy already render it inputs.Ontheotherhand,Iwanttostressthatthosesame
(but only in the specific sense stressed by Friston; more learningroutinesmakeusextremelyporoustothestatisti-
on this shortly) a complex model of its own adaptive calstructureoftheactualenvironment,andputuspercep-
niche.Assuch,thecreature,simply becauseitisthecrea- tually in touch, in as direct a fashion as is mechanistically
ture that it is, already embodies a complex set of “expec- possible,withthecomplex,multilayered,worldaroundus.
tations” concerning moving, eating, playing, exploring,
and so forth. It is because surprisal at the very largest
R4.2. Thepuzzleoftheporousperceiver
scale is minimized against the backdrop of this complex
set of creature-defining “expectations” that we need fear This, then, is the promised “puzzle of the porous percei-
neither darkened nor musical (nor meta-musical, nor ver”: Can we both experience the world via a top-down
meta-meta-musical) rooms. The free-energy principle generative-model based cascade and be in touch not with
thus subsumes the mutual information approach (for a a realm of internal fantasy but, precisely, with the world?
niceworkedexample,seeFristonetal.2012).Theessential One superficially tempting way to try to secure a more
creature-defining backdrop then sets the scene for the direct mind–world relation is to follow Froese &
deployment(sometimes,insomeanimals)ofPP-stylestrat- Ikegami in rejecting the appeal to internally represented
egies of cortical learning in which hierarchical message models altogether (we saw hints of this in the comments
passing, by implementing a version of “empirical Bayes,” by Anderson & Chemero too). Thus, they argue that
allows effective learning that is barely, if at all, hostage to “Properties of the environment do not need to be
initial priors. That learning requires ongoing exposure to encoded and transmitted to higher cortical areas, but not
rich input streams. It is the backdrop “expectations,” because they are already expected by an internal model
deeply built-in to the structure of the organism (manifest- of the world, but rather because the world is its own best
ing as, for example, play, curiosity, hunger, and thirst) model.” But I do not believe (nor have I ever believed:
that keep the organism alive and the input stream rich, see, e.g., Clark 1997, Ch. 8) that this strategy can cover
andthatpromotevariousbeneficialformsof“self-structur- all the cases, or that, working alone, it can deliver rich,
ing” of theinformation flow–seePfeifer et al.(2007). world-revealing perception of the kind we humans
This means that the general solution to the darkened enjoy–conscious perception of a world populated by
room worry that was briefly scouted in WN, section 3.2, (among other things) elections, annual rainfall statistics,
is mandatory, and that we must embrace it whatever our prayers, paradoxes, and poker hands. To experience a
cosmetic preferences concerning entropy versus mutual world rich in such multifarious hidden causes we must do
242 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

Response/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
some pretty fancy things, at various time-scales, with the PP thus functions primarily as an intermediate-level
incoming energetic flux: things at the heart of which lie, I (see Spratling) descriptionofthe underlying formofcor-
claim, the prediction-driven acquisition and top-down tical processing. This is the case even though the larger
deployment of probabilistic generative models. I do not story about free energy minimization (a story I briefly
believe that prayers, paradoxes, or even poker hands can sketched in WN, sect. 1.6, but tried to bracket as
be their own best model, if that means they can be raising issues far beyond the scope of the article) aims
known without the use of internal representations or to encompass far more. As a theory of cortical processing,
inner models of external hidden causes. Worse still, in PP suggests we learn to represent linked sets of prob-
the cases where we might indeed allow the world, and ability density distributions, and that they provide the
directly elicited actions upon the world, to do most of the form of hierarchical generative models underlying both
heavy lifting (the termite mound-building strategies men- perception (of the rich, world-presenting variety) and
tioned by Sloman are a case in point) it is not obvious many forms of world-engaging action. Importantly, this
that there will–simply by virtue of deploying such strat- leaves plenty of space for other ploys and strategies to
egies alone–be any world-presenting experience at all. coexist with the core PP mechanism. I tried to celebrate
What seems exactly right, however, is that brains like that space by making a virtue (WN, sects. 3.2–3.4) out
ours are masters of what I once heard Sloman describe as of the free-energy story’s failure to specify the full form
“productive laziness.” Hence, we will probably not rely on of a cognitive architecture, envisaging a cooperative
a rich internal model when the canny use of body or project requiring many further insights from evolutionary,
world will serve as well, and many of the internal models situated, embodied, and distributed approaches to under-
that we do use will be partial at best, building in all kinds standing mind and adaptive response. Was it then false
ofcalls(seeClark2008)toembodied,problem-simplifying advertising to offer PP itself as a unifying account? Not,
action.TheupshotisthatIdidnotintend(despitethefears I fondly hope, if PP reveals common computational prin-
of Anderson & Chemero) to depict all of cognition and ciples governing knowledge-rich forms of cortical proces-
adaptive response as grounded in the top-down deploy- sing (in both the sensory and motor realms), delivers a
ment of knowledge-rich internal models. But I do think novel account of attention (as optimizing precision), and
such models are among the most crucial achievements of reveals prediction error minimization as the common
cortical processing, and that they condition both online goal of many forms of action, social engagement, and
and offline forms of human experience. environmental structuring.
NordidIintend,asSlomaninakindofreversalofthe There is thus an important difference of emphasis
worryraisedbyAnderson&Chemerofears,toreduceall between my treatment and the many seminal treatments
cognition to something like online control. Where Ander- by Karl Friston. For as the comments by Friston made
son & Chemero subtly mislocate the PP account as an clear, he himself sets little store by the difference
attempt to depict all cognition as rooted in procedures between what I (like Anderson & Chemero) might
apt only for high-level knowledge-rich response, Sloman describe as knowledge- and inner-model-rich versus
subtly mislocates it as an over-ambitious attempt to knowledge-sparse ways of minimizing free energy and
depict all cognition as rooted in procedures apt only for reducing surprisal. Viewed from the loftier perspective
low-level sensorimotor processing. Sloman thus contrasts of free-energy minimization, the effect is indeed the
predictionwithinterpretation,andstressestheimportance same. Free-energy reduction can be promoted by the
to human (and animal) reasoning of multiple meta-cogni- “fit” between morphology and niche, by quick-and-dirty
tivemechanismsthat(heargues)gofarbeyondthepredic- internal-representation-sparse ploys, and by the costlier
tion and control of gross sensory and motor signals. In a (but potent) use of prediction-driven learning to infer
related vein, Khalil interestingly notes that human cogni- internally represented probabilistic generative models.
tion includes many “conception-laden processes” (such as But it is, I suspect, only that costlier class of approaches,
choosing our own benchmark for a satisfactory income) capable of on-the-hoof learning about complex interani-
that cannot be corrected simply by adjustments that mated webs of hidden causes, that delivers a certain “cog-
bettertrack gross sensory input. nitive package deal.” The package deal bundles together
Fortunately, there are no deep conflicts here. PP aims what I have been calling “rich, world-presenting percep-
onlytodescribeacorecorticalprocessingstrategy:astrat- tion,” offline imagination, and understanding (not just
egy that can deliver probabilistic generative models apt apt response) and has a natural extension to intentional,
bothforbasicsensorimotorcontrolandformoreadvanced world-directed action (see Clark, forthcoming). Such a
tasks.Thesamecorestrategycandrivethedevelopmentof package may well be operative, as Gowaty & Hubbell
generativemodelsthattrackstructurewithinhighlyabstract suggested, in the generation of many instances of animal
domains, and assertions concerning such domains can response. It need not implicate solely the neocortex
indeedresistsimpleperceptualcorrection.Tosaythatthe (though that seems to be its natural home). But potent
mechanismsof(rich,world-presenting)perceptionarecon- though the package is, it is not the only strategy at work,
tinuous with the mechanisms of (rich, world-presenting) even in humans, and there may be some animals that do
cognitionisnottodenythis.Itmaybe,however,thatlearn- not deploy the strategy at all.
ingaboutsomehighlyabstractdomainsrequiresdelivering Thus, consider the humble earthworm. The worm is
structured symbolic inputs; for example, using theformal- doubtless a wonderful minimizer of free energy, and we
ismsoflanguage,scienceandmathematics.Understanding might even describe the whole worm (as the comments
how prediction-driven learning interacts with the active by Friston suggest) as a kind of free-energy minimizing
productionanduptakeofexternalsymbolicrepresentations model of its world. But does the worm command a
andwithvariousformsofdesignerlearningenvironmentsis model of its world parsed into distal causes courtesy of
thusacrucialchallenge,asRoepstorffalsonotes. top-down expectations applied in a multilevel manner?
BEHAVIORALANDBRAINSCIENCES(2013)36:3 243
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
This is far from obvious. The worm is capable of sensing, ofcomplex,interactingdistalcausesandtheabilitytogen-
but perhaps it does not thereby experience a perceptual erate perception-like states from the top down. It delivers
world. If that is right, then not all ways of minimizing understanding because to perceive the world of distal
freeenergyareequal,andonlysomeputyouinperceptual causes in this way is not just to react appropriately to it. It
touch (as opposed to mere causal contact) with a distal istoknowhowthatworldwillevolveandalteracrossmul-
worldcharacterizedbymultipleinteractinghiddencauses. tipletimescales.This,inturn,involveslearningtogenerate
Thisbringsusback,finally,tothevexedquestionofthe perception-likestatesfromthetop-down.Thisdouble-inno-
mind–worldrelationitself.WhereFroese&Ikegamifear vation, carefully modulated by the precision-weighting of
thatthePPstrategycutsusofffromtheworld,insertingan attention,lies(PPclaims)attheveryheartofmanydistinc-
internal model between us and the distal environment, I tivelyhumanformsofcognition.Tobesure(recallGowaty
believe that it is only courtesy of such models that we &Hubbell)thesamestrategyisatworkinmanynonhuman
(perhaps unlike the earthworm) can experience a distal animals,deliveringtheretooaquitedeepunderstandingof
environment at all! Does that mean that perception pre- a world of distal causes. What, then, is special about the
sents us (as Paton et al. suggest) with only a fantasy humancase?
about the world? I continue to resist this way of casting Roepstorff points to a potent complex of features of
things. Consider (recall the comments by Farmer et al.) humanlife,especiallyourabilitiesoftemporallyco-coordi-
theperceptionofsentencestructureduringspeechproces- natedsocialinteraction(seealsocommentariesbyHolm&
sing. It is plausibly only due to the deployment of a rich Madison, Paton et al., and Schaefer et al.) and our
generative model that a hearer can recover semantic and (surely deeply related) abilities to construct artifacts and
syntactic constituents from the impinging sound stream. designer environments. Versions of all of this occur in
Does that mean that the perception of sentence structure other species. But in the human case, the mosaic comes
is “an inferred fantasy about what lies behind the veil of togetherundertheinfluenceofflexiblestructuredsymbolic
input”? Surely it does not. In recovering the right set of languageandanalmostobsessivedrivetoengageinshared
interacting distal causes (subjects, objects, meanings, culturalpractices.Wearethusenabledrepeatedlytorede-
verb-clauses, etc.) we see through the sound stream to ploy our core cognitive skills in the transformative context
themultilayeredstructureandcomplexpurposesofthelin- of exposure to patterned sociocultural practices, including
guistic environment itself. This is possible because brains the use of symbolic codes (encountered as “material
like ours are sensitive statistical sponges open to deep symbols”; Clark 2006a) and complex social routines
restructuring by the barrage of inputs coming from the (Hutchins 1995; Roepstorff et al. 2010). If, as PP claims,
world.Moreover,evenapparently low-levelstructuralfea- oneofthemostpotentinnertoolsavailableisdeep,predic-
turesofcortex(receptivefieldorientationsandspatialfre- tion-driven learning that locks on to interacting distal
quencies), as Bridgeman very eloquently reminds us, hidden causes, we may dimly imagine (WN, sect. 3.4;
come toreflecttheactual statisticalprofileoftheenviron- Clark 2006; 2008) a virtuous spiral in which our achieved
ment,anddosoinways thataresurprisingly open tovari- understandings are given concrete and communicable
ation by early experience. form,andthensharedandfedbackusingstructuredprac-
Does this commit me to the implausible idea that per- tices that present us with newpatterns.
ception presents us with the world “as it is in itself”? Such pattern-presenting practices should, as Roepstorff
Here, the helpful commentary by König, Wilming, suggests, enable us to develop hierarchical generative
Kaspar, Nagel, & Onat (König et al.) seems to me to models that track ever more rarefied causes spanning the
get the issue exactly right. Predictions are made, they bruteandthemanufacturedenvironment.Bytrackingsuch
stress (see also the comments by Bridgeman), in the causestheymayalso,ininnocentways,helpcreateandpro-
light of our own action repertoire. This simple (but pro- pagatethem(thinkofpatterned practicessuch asmarriage
found)factresultsinreductionsofcomputationalcomplex- andmusic).Itisthispotentiallyrichandmultilayeredinter-
ity by helping to select what features to process, and what action between knowledge-rich prediction-driven learning
things to try to predict. From the huge space of possible and enculturated, situated cognition that most attracts me
ways of parsing the world, given the impinging energetic tothecorePPproposal.Theseareearlydays,butIbelieve
flux, we select the ways that serve our needs by fitting PP has the potential to help bridge the gap between
our action repertoires. Such selection will extend, as simplerforms ofembodiedandsituated response,the self-
Paton et al. have noted (see also Dennett), to ways of structuring of information flows, and the full spectrum of
parsing and understanding our own bodies and minds. sociallyandtechnologicallyinflectedhumanunderstanding.
Such parsing enables us to act on the world, imposing
furtherstructureontheflowofinformation,andeventually
reshaping the environment itself tosuit our needs.
Roepstorff’s engaging commentary brings several of
References
these issues into clearer focus by asking in what ways, if
any, the PP framework illuminates specifically human
forms of cognition. This is a crucial question. The larger
[Theletters“a”and“r”beforeauthor’sinitialsstandfortargetarticleand
free-energy story targets nothing that is specifically responsereferences,respectively]
human, though (of course) it aims to encompass human
Abelson,R.P.(1981)Psychologicalstatusofthescriptconcept.AmericanPsychol-
cognition. The PP framework seeks to highlight a cortical ogist36(7):715–29. [JBH]
processing strategy that, though not uniquely human, is Adams,F.&Aizawa,K.(2001)Theboundsofcognition.PhilosophicalPsychology
plausiblyessentialtohumanintelligenceandthatprovides, 14(1):43–64. [aAC]
Alais,D.&Blake,R.,eds.(2005)Binocularrivalry.MITPress. [aAC]
asmentionedabove,acompelling“cognitivepackagedeal.”
Alais,D.&Burr,D.(2004)Theventriloquisteffectresultsfromnear-optimal
Thatpackagedealdelivers,atasinglestroke,understanding bimodalintegration.CurrentBiology14:257–62. [aAC]
244 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Alink,A.,Schwiedrzik,C.M.,Kohler,A.,Singer,W.&Muckli,L.(2010)Stimulus Brown,M.,Dilley,L.C.&Tanenhaus,M.K.(2012)Real-timeexpectations
predictabilityreducesresponsesinprimaryvisualcortex.JournalofNeuro- basedoncontextspeechratecancausewordstoappearordisappear.In:Pro-
science30:2960–66. [aAC,TE,LM] ceedingsofthe34thAnnualConferenceoftheCognitiveScienceSociety,ed.N.
Anderson,C.H.&VanEssen,D.C.(1994)Neurobiologicalcomputationalsystems. Miyake,D.Peebles,&R.P.Cooper,pp.1374–79.CognitiveScienceSociety.
In:Computationalintelligence:Imitatinglife,ed.J.M.Zurada,R.J.Marks&C. [TAF]
J.Robinson,pp.213–22.IEEEPress. [aAC] Brown,M.,Salverda,A.P.,Dilley,L.C.&Tanenhaus,M.K.(2011)Expectations
Anderson,M.L.(2006)Cognitiveepistemicopenness.Phenomenologyandthe fromprecedingprosodyinfluencesegmentationinonlinesentenceprocessing.
CognitiveSciences5(2):125–54. [MLA] PsychonomicBulletinandReview18:1189–96. [TAF]
Anderson,M.L.(2007)Themassiveredeploymenthypothesisandthefunctional Brown,R.G.&Hwang,P.Y.C.(1992)Introductiontorandomsignalsandapplied
topographyofthebrain.PhilosophicalPsychology20(2):143–74. [aAC] Kalmanfiltering,2ndedition.Wiley. [DRa]
Angelucci,A.,Levitt,J.B.,Walton,E.J.S.,Hupe,J.M.,Bullier,J.&Lund,J.S. Brown,S.(2003)Biomusicologyandthethreeparadoxesaboutmusic.Bulletinof
(2002)Circuitsforlocalandglobalsignalintegrationinprimaryvisualcortex. PsychologyandtheArts4:14–17. [LH]
JournalofNeuroscience22:8633–864. [LM] Bruner,J.(1986)Actualminds,possibleworlds.HarvardUniversityPress. [JBH]
Anton-Erxleben,K.,Henrich,C.&Treue,S.(2007)Attentionchangesperceived Bruner,J.(1991)Thenarrativeconstructionofreality.CriticalInquiry18(1):1–
sizeofmovingvisualpatterns.JournalofVision7(11):1–9. [NB] 21. [JBH]
Arnold,J.E.,Hudson,C.L.&Tanenhaus,M.K.(2007)Ifyousaytheeuhyouare Bubic,A.,vonCramon,D.Y.&Schubotz,R.I.(2010)Prediction,cognitionandthe
describingsomethinghard:Theon-lineattributionofdisfluencyduringrefer- brain.FrontiersinHumanNeuroscience4(25):1–15. [aAC]
encecomprehension.JournalofExperimentalPsychology:Learning,Memory, Buckingham,G.&Goodale,M.A.(2010)Liftingwithoutseeing:Theroleofvision
andCognition33:914–30. [TAF] inperceivingandactinguponthesizeweightillusion.PLoSONE5(3):e9709.
Arthur,B.(1994)Increasingreturnsandpathdependenceintheeconomy.Univer- doi:10.1371/journal.pone.0009709. [GB]
sityofMichiganPress. [aAC] Buhusi,C.V.&Meck,W.H.(2005)Whatmakesustick?Functionalandneural
Ashby,W.R.(1940)Adaptivenessandequilibrium.TheBritishJournalofPsychiatry mechanismsofintervaltiming.NatureReviews:Neuroscience6:755–65.
86:478–83. [TF] [LH]
Ashby,W.R.(1947)Principlesoftheself-organizingdynamicsystem.Journalof Burge,J.,Fowlkes,C.&Banks,M.(2010)Natural-scenestatisticspredicthowthe
GeneralPsychology37:125–28. [KF] figure–groundcueofconvexityaffectshumandepthperception.Journalof
Ay,N.,Bertschinger,N.,Der,R.,Güttler,F.&Olbrich,E.(2008)Predictiveinfor- Neuroscience30(21):7269–80. [aAC]
mationandexplorativebehaviorofautonomousrobots.TheEuropeanPhysical Burr,D.,Tozzi,A.&Morrone,C.(2007)Neuralmechanismsfortimingvisual
JournalB–CondensedMatterandComplexSystems63(3):32939. [DYL] eventsarespatiallyselectiveinreal-worldcoordinates.NatureNeuroscience
Baerger,D.&McAdams,D.(1999)Lifestorycoherenceanditsrelationto 10:423–25. [LH]
psychologicalwell-being.NarrativeInquiry9:69–96. [JBH] Carandini,M.(2012)Fromcircuitstobehavior:Abridgetoofar?NatureNeuro-
Bar,M.(2007)Theproactivebrain:Usinganalogiesandassociationstogenerate science15(4):507–509. [MWS]
predictions.TrendsinCognitiveSciences11(7):280–89. [aAC] Carandini,M.,Demb,J.B.,Mante,V.,Tolhurst,D.J.,Dan,Y.,Olshausen,B.A.,
Barlow,H.B.(1961)Possibleprinciplesunderlyingthetransformationsofsensory Gallant,J.L.&Rust,N.C.(2005)Doweknowwhattheearlyvisualsystem
messages.In:Sensorycommunication,ed.W.Rosenblith,pp.217–34.(Chapter does?JournalofNeuroscience25(46):10577–97. [MWS]
13).MITPress. [KF,PK,TT] Carrasco,M.(2011)Visualattention:Thepast25years.VisionResearch51:1484–
Barrett,L.F.(2009)Thefutureofpsychology:Connectingmindtobrain.Per- 525. [NB]
spectivesinPsychologicalScience4:326–39. [aAC] Carrasco,M.,Ling,S.&Read,S.(2004)Attentionaltersappearance.Nature
Barrett,L.F.&Bar,M.(2009)Seeitwithfeeling:Affectivepredictionsduring Neuroscience7:308–13. [NB,rAC]
objectperception.PhilosophicalTransactionsoftheRoyalSocietyofLondonB: Chappell,J.&Sloman,A.(2007)Naturalandartificialmeta-configuredaltricial
BiologicalSciences364(1521):1325–34. [arAC,AKS] information-processingsystems.InternationalJournalofUnconventional
Baugh,L.A.,Kao,M.,Johansson,R.S.&Flanagan,J.R.(2012)Materialevidence: Computing3(3):211–39.Availableat:http://www.cs.bham.ac.uk/research/pro-
Interactionofwell-learnedpriorsandsensorimotormemorywhenlifting jects/cosy/papers/#tr0609. [AS]
objects.JournalofNeurophysiology108(5):1262–69.doi:10.1152/ Chater,N.&Manning,C.(2006)Probabilisticmodelsoflanguageprocessingand
jn.00263.2012. [GB] acquisition.TrendsinCognitiveSciences10(7):335–44. [aAC]
Bechtel,W.(2006)Reducingpsychologywhilemaintainingitsautonomyvia Chemero,A.(2009)Radicalembodiedcognitivescience.MITPress. [MLA]
mechanisticexplanation.In:Thematterofthemind:Philosophicalessayson Chen,L.(2005)Thetopologicalapproachtoperceptualorganization.VisualCog-
psychology,neuroscienceandreduction,ed.M.Schouten&H.L.deJong,Ch. nition12:553–637. [SMS]
8.Blackwell. [MWS] Chennu,S.,Craston,P.,Wyble,B.&Bowman,H.(2009)Attentionincreasesthe
Beer,R.D.(2000)Dynamicalapproachestocognitivescience.TrendsinCognitive temporalprecisionofconsciousperception:VerifyingtheneuralST2model.
Sciences4(3):91–99. [TF] PLOSComputationalBiology5(11):1–13. [HB]
Bengio,Y.(2009)LearningdeeparchitecturesforAI.FoundationsandTrendsin Chittka,L.&Skorupski,P.(2011)Informationprocessinginminiaturebrains.
MachineLearning2(1):1–127. [rAC] ProceedingsoftheRoyalSocietyofLondon,B:BiologicalSciences278
Berkes,P.&Wiskott,L.(2005)Slowfeatureanalysisyieldsarichrepertoireof (1707):885–88.doi:10.1098/rspb.2010.2699. [AS]
complexcellproperties.JournalofVision5(6):579–602. [PK] Churchland,P.M.(1989)Theneurocomputationalperspective.MIT/Bradford
Berlyne,D.E.(1970)Novelty,complexityandhedonicvalue.PerceptionandPsy- Books. [arAC]
chophysics8:279–86. [RSS] Churchland,P.M.(2012)Plato’scamera:Howthephysicalbraincapturesaland-
Berniker,M.&Körding,K.P.(2008)Estimatingthesourcesofmotorerrorsfor scapeofabstractuniversals.MITPress. [arAC]
adaptationandgeneralizationNatureNeuroscience11:1454–61. [aAC] Clark,A.(1987)Thekludgeinthemachine.MindandLanguage2(4):277–300.
Betsch,B.Y.,Einhäuser,W.,Körding,K.P.&König,P.(2004)Theworldfromacat’s [aAC]
perspective–statisticsofnaturalvideos.BiologicalCybernetics90:41–50. [PK] Clark,A.(1989)Microcognition:Philosophy,cognitivescienceandparalleldistrib-
Bindra,D.(1959)Stimuluschange,reactionstonovelty,andresponsedecrement. utedprocessing.MITPress/BradfordBooks. [arAC]
PsychologicalReview66:96–103. [aAC] Clark,A.(1993)Minimalrationalism.Mind102(408):587–610. [rAC]
Blake,R.(2001)Aprimeronbinocularrivalry,includingcurrentcontroversies.Brain Clark,A.(1997)Beingthere:Puttingbrain,bodyandworldtogetheragain.MIT
andMind2:5–38. [MLA] Press. [MLA,aAC]
Blakemore,S.,Oakley,D.&Frith,C.D.(2003)Delusionsofaliencontrolinthe Clark,A.(2006a)Language,embodimentandthecognitiveniche.TrendsinCog-
normalbrain.Neuropsychologia41(8):1058–67. [PG] nitiveSciences10(8):370–74. [arAC]
Born,R.T.,Tsui,J.M.&Pack,C.C.(2009)Temporaldynamicsofmotioninte- Clark,A.(2006b)Materialsymbols.PhilosophicalPsychology19(3):291–307. [AR]
gration,In:Dynamicsofvisualmotionprocessing,ed.U.Ilg&G.Masson.pp. Clark,A(2008)Supersizingthemind:Action,embodiment,andcognitiveextension.
37–54.Springer. [aAC] OxfordUniversityPress. [arAC]
Bourdieu,P.(1977)Outlineofatheoryofpractice,trans.R.Nice.Cambridge Clark,A.(2012)Dreamingthewholecat:Generativemodels,predictiveprocessing,
UniversityPress. [AR] andtheenactivistconceptionofperceptualexperience.Mind121(483):753–
Brainard,D.(2009)Bayesianapproachestocolorvision.In:Thevisualneuro- 71. [rAC]
sciences,4thedition,ed.M.Gazzaniga,pp.395–408.MITPress. [aAC] Clark,A.(forthcoming)Perceivingaspredicting,In:Perceptionanditsmodalities,
Brayanov,J.B.&Smith,M.A.(2010)Bayesianand“anti-Bayesian”biasesinsensory ed.M.Mohan,S.Biggs&D.Stokes.OxfordUniversityPress. [arAC]
integrationforactionandperceptioninthesize–weightillusion.Journalof Clark,A.&Chalmers,D.(1998)Theextendedmind.Analysis58(1):7–19. [aAC]
Neurophysiology103(3):1518–31. [GB,rAC] Clark,A.&Thornton,C.(1997)Tradingspaces:Computation,representation,
Brown,H.,Friston,K.&Bestamnn,S.(2011)Activeinference,attentionandmotor andthelimitsofuninformedlearning.BehavioralandBrainSciences20(1):57–66.
preparation.FrontiersinPsychology2:218.doi:10.3389/fpsyg.2011.00218. [aAC] [rAC]
BEHAVIORALANDBRAINSCIENCES(2013)36:3 245
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Clifford,C.W.G.,Webster,M.A.,Stanley,G.B.,Stocker,A.A.,Kohn,A.,Sharpee, de-Wit,L.H.,KubiliusJ.,WagemansJ.&OpdeBeeck,H.P.(2012)Bistable
T.O.&Schwartz,O.(2007)Visualadaptation:Neural,psychologicaland GestaltsreduceactivityinthewholeofV1,notjusttheretinotopicallypredicted
computationalaspects.VisionResearch47:3125–31. [aAC] parts.JournalofVision12:1–14. [LM]
Coltheart,M.(2007)Cognitiveneuropsychiatryanddelusionalbelief(The33rdSir de-Wit,L.,Machilsen,B.&Putzeys,T.(2010)Predictivecodingandtheneural
FrederickBartlettLecture).TheQuarterlyJournalofExperimentalPsychology responsetopredictablestimuli.JournalofNeuroscience30:8702–703. [aAC]
60(8):1041–62. [aAC] Dikker,S.,Rabagliati,H.,Farmer,T.A.&Pylkkanen,L.(2010)Earlyoccipital
Conrad,K.(1958)DiebeginnendeSchizophrenie.ThiemeVerlag. [SMS] sensitivitytosyntacticcategoryisbasedonformtypicality.PsychologicalScience
Corlett,P.R.,Frith,C.D.&Fletcher,P.C.(2009a)Fromdrugstodeprivation:A 21:629–34. [TAF]
Bayesianframeworkforunderstandingmodelsofpsychosis.Psychopharma- Dilley,L.C.&McAuley,J.D.(2008)Distalprosodiccontextaffectswordseg-
cology(Berlin)206(4):515–30. [aAC] mentationandlexicalprocessing.JournalofMemoryandLanguage59:294–
Corlett,P.R.,Krystal,J.K.,Taylor,J.R.&Fletcher,P.C.(2009b)Whydodelusions 311. [TAF]
persist?FrontiersinHumanNeuroscience3:12.doi:10.3389/ Dilley,L.C.&Pitt,M.(2010)Alteringcontextspeechratecancausewordsto
neuro.09.012.2009. [aAC] appearordisappear.PsychologicalScience21:1664–70. [TAF]
Corlett,P.R.,Taylor,J.R.,Wang,X.J.,Fletcher,P.C.&Krystal,J.H.(2010)Toward Dima,D.,Dietrich,D.E.,Dillo,W.&Emrich,H.M.(2010)Impairedtop-down
aneurobiologyofdelusions.ProgressinNeurobiology92(3):345–69. [aAC] processesinschizophrenia:ADCMstudyofERPs.NeuroImage52:824–32.
Craig,A.D.(2003)Interoception:Thesenseofthephysiologicalconditionofthe [SMS]
body.CurrentOpinioninNeurobiology13(4):500–505. [AKS] Dima,D.,Roiser,J.P.,Dietrich,D.E.,Bonnemann,C.,Lanfermann,H.,Emrich,
Craig,A.D.(2009)Howdoyoufeel–now?Theanteriorinsulaandhumanaware- H.M.&Dillo,W.(2009)Understandingwhypatientswithschizophreniado
ness.NatureReviewsNeuroscience10(1):59–70. [AKS] notperceivethehollow-maskillusionusingdynamiccausalmodeling.Neuro-
Craik,K.(1943)Thenatureofexplanation.CambridgeUniversityPress. [DRa] Image46:1180–86. [SMS]
Critchley,H.D.&Seth,A.K.(2012)Willstudiesofmacaqueinsularevealtheneural DiPaolo,E.A.(2009)Extendedlife.Topoi28(1):9–21. [aAC,TF]
mechanismsofself-awareness?Neuron74(3):423–26. [AKS] DiPaolo,E.A.,Rohde,M.&DeJaegher,H.(2010)Horizonsfortheenactivemind:
Critchley,H.D.,Wiens,S.,Rotshtein,P.,Ohman,A.&Dolan,R.J.(2004)Neural Values,socialinteraction,andplay.In:Enaction:Towardanewparadigmfor
systemssupportinginteroceptiveawareness.NatureNeuroscience7(2):189– cognitivescience,ed.J.Stewart,O.Gapenne&E.A.DiPaolo,pp.33–87.MIT
95. [AKS] Press. [TF]
Crutchfield,J.P.&Young,K.(1989)Inferringstatisticalcomplexity.PhysicalReview Doherty,M.J.,Campbell,N.M.,Tsuji,H.&Phillips,W.A.(2010)TheEbbinghaus
Letters63:105–108. [DYL] illusiondeceivesadultsbutnotyoungchildren.DevelopmentalScience13:714–
Dahan,D.&Tanenhaus,M.K.(2004)Continuousmappingfromsoundtomeaning 21.doi:10.1111/j.1467-7687.2009.00931.x. [WAP]
inspoken-languagecomprehension:Evidencefromimmediateeffectsofverb- Doherty,M.J.,Tsuji,H.&Phillips,W.A.(2008)Thecontext-sensitivityofvisualsize
basedconstraints.JournalofExperimentalPsychology:Learning,Memory,and perceptionvariesacrosscultures.Perception37:1426–33. [WAP]
Cognition30:498–513. [TAF] Doya,K.,Ishii,S.,Pouget,A.&Rao,R.eds.(2007)Bayesianbrain:Probabilistic
Damasio,A.(2000)Thefeelingofwhathappens:Bodyandemotioninthemakingof approachestoneuralcoding.MITPress. [aAC]
consciousness.HarvestBooks. [AKS] Dumoulin,S.O.&Hess,R.F.(2006)ModulationofV1activitybyshape:image-
Danckert,J.,Saoud,M.&Maruff,P.(2004)Attention,motorcontrolandmotor statisticsorshape-basedperception?JournalofNeurophysiology95:3654–
imageryinschizophrenia:implicationsfortheroleoftheparietalcortex. 64. [aAC]
SchizophreniaResearch70(2–3):241–61. [PG] Egner,T.,Monti,J.M.&Summerfield,C.(2010)Expectationandsurprisedeter-
Daprati,E.,Franck,N.,Georgieff,N.,Proust,J.,Pacherie,E.,Dalery,J.&Jeanerod,M. mineneuralpopulationresponsesintheventralvisualstream.Journalof
(1997)Lookingfortheagent:Aninvestigationintoconsciousnessofactionand Neuroscience30(49):16601–608. [arAC,TE]
self-consciousnessinschizophrenizpatients.Cognition65:71–86. [PG] Einhäuser,W.,Kayser,C.,König,P.&Körding,K.P.(2002)Learningtheinvariance
Darwin,C.(1871)Thedescentofmanandselectioninrelationtosex.JohnMurray. propertiesofcomplexcellsfromtheirresponsestonaturalstimuli.European
[PAG] JournalofNeuroscience15:475–86. [PK]
Davidson,D.(1974)Ontheveryideaofaconceptualscheme.Proceedingsand Einhäuser,W.,Moeller,G.U.,Schumann,F.,Conradt,J.,Vockeroth,J.,Bartl,K.,
AddressesoftheAmericanPhilosophicalAssociation47:5–20. [MLA] Schneider,E.&König,P.(2009)Eye-headcoordinationduringfreeexplorationin
Dayan,P.(1997)Recognitioninhierarchicalmodels.In:Foundationsofcompu- humanandcat.AnnalsoftheNewYorkAcademyofSciences1164:353–66. [PK]
tationalmathematics,ed.F.Cucker&M.Shub,pp.43–57.Springer. [aAC] Eliades,S.J.&Wang,X.(2008)Neuralsubstratesofvocalizationfeedbackmoni-
Dayan,P.&Hinton,G.(1996)VarietiesofHelmholtzmachine.NeuralNetworks toringinprimateauditorycortex.Nature453:1102–106. [rAC,TE]
9:1385–403. [aAC] Eliasmith,C.(2007)Howtobuildabrain:Fromfunctiontoimplementation.
Dayan,P.,Hinton,G.E.&Neal,R.M.(1995)TheHelmholtzmachine.Neural Synthese159(3):373–88. [aAC,NS]
Computation7:889–904. [arAC,KF] Eliasmith,C.(inpress)Howtobuildabrain:Aneuralarchitectureforbiological
deGardelle,V.,Waszczuk,M.,Egner,T.&Summerfield,C.(2012)Concurrent cognition.OxfordUniversityPress. [DRa]
repetitionenhancementandsuppressionresponsesinextrastriatevisualcortex. Eliasmith,C.&Anderson,C.(2003)Neuralengineering:Computation,represen-
CerebralCortex.[Epubaheadofprint:July18,2012].doi:10.1093/cercor/ tation,anddynamicsinneurobiologicalsystems.MITPress. [DRa]
bhs211. [LM] Eliasmith,C.,Stewart,T.C.,Choo,X.,Bekolay,T.,DeWolf,T.,Tang,Y.&Ras-
Dehaene,S.(2009)Readinginthebrain.Penguin. [aAC] mussen,D.(2012)Alarge-scalemodelofthefunctioningbrain.Science338
Demos,A.P.,Chaffin,R.,Begosh,K.T.,Daniels,J.R.&Marsh,K.L.(2012) (6111):1202–205. [DRa]
Rockingtothebeat:Effectsofmusicandpartner’smovementsonspontaneous Engel,A.K.,Fries,P.&Singer,W.(2001)Dynamicpredictions:Oscillationsand
interpersonalcoordination.JournalofExperimentalPsychology:General synchronyintop–downprocessing.NatureReviews:Neuroscience2:704–16.
141:49–53. [LH] [aAC]
Dempster,A.P.,Laird,N.M.&Rubin,D.B.(1977)Maximumlikelihoodfrom Erlhagen,W.(2003)Internalmodelsforvisualperception.BiologicalCybernetics
incompletedataviatheEMalgorithm.JournaloftheRoyalStatisticalSociety, 88:409–17. [LM]
SeriesB39:1–38. [aAC] Ernst,M.O.(2010)Eyemovements:Illusionsinslowmotion.CurrentBiology20
Deneve,S.(2008)BayesianspikingneuronsI:Inference.NeuralComputation (8):R357–59. [aAC]
20:91–117. [aAC] Ernst,M.O.&Banks,M.S.(2002)Humansintegratevisualandhapticinformation
Dennett,D.(1978)Brainstorms:Philosophicalessaysonmindandpsychology. inastatisticallyoptimalfashion.Nature415:429–33. [aAC]
BradfordBooks/MITPress. [aAC] Everitt,B.,Dickinson,A.&Robbins,T.(2001)Theneuropsychologicalbasisof
Dennett,D.C.(1987)Theintentionalstance.MITPress. [aAC] addictivebehavior.BrainResearchReviews36:129–38. [DRo]
Dennett,D.C.(1991)Consciousnessexplained.Little,Brown. [aAC] Evrard,H.C.,Forro,T.&Logothetis,N.K.(2012)VonEconomoneuronsinthe
Dennett,D.C.(2009)Darwin’s“StrangeInversionofReasoning”.Proceedingsofthe anteriorinsulaofthemacaquemonkey.Neuron74(3):482–89. [AKS]
NationalAcademyofSciencesUSA106(Suppl.1):10061–65. [rAC,DCD] Fabre-Thorpe,M.(2011)Thecharacteristicsandlimitsofrapidvisualcategorization.
denOuden,H.E.M.,Daunizeau,J.,Roiser,J.,Friston,K.J.&Stephan,K.E.(2010) FrontiersinPsychology2:243.doi:10.3389/fpsyg.2011.00243. [aAC]
Striatalpredictionerrormodulatescorticalcoupling.JournalofNeuroscience Farmer,T.A.,Christiansen,M.H.&Monaghan,P.(2006)Phonologicaltypicality
30:3210–19. [arAC,TE] influenceson-linesentencecomprehension.ProceedingsoftheNational
denOuden,H.E.M,Friston,K.J.,Daw,N.D.,McIntosh,A.R.&Stephan,K.E. AcademyofSciencesUSA103:12203–208. [TAF]
(2009)Adualroleforpredictionerrorinassociativelearning.CerebralCortex Farmer,T.A.,Monaghan,P.,Misyak,J.B.&Christiansen,M.H.(2011)Phonolo-
19:1175–85. [rAC,TE] gicaltypicalityinfluencessentenceprocessinginpredictivecontexts:Areplyto
Desimone,R.&Duncan,J.(1995)Neuralmechanismsofselectivevisualattention. Staubetal.(2009)JournalofExperimentalPsychology:Learning,Memory,and
AnnualReviewofNeuroscience18:193–222. [aAC] Cognition37:1318–25. [TAF]
246 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Feldman,H.&Friston,K.J.(2010)Attention,uncertainty,andfree-energy.Fron- Galton,F.(1883)Inquiresintohumanfacultyanditsdevelopment.MacMillan. [LH]
tiersinHumanNeuroscience4:215.doi:10.3389/fnmuh.2010.00215. [HB, Geertz,C.(1966)Religionasaculturalsystem.In:Theinterpretationofcultures,pp.
arAC,TE,WAP,MWS] 87–125.BasicBooks. [AR]
Feldman,J.(2010)Cognitivescienceshouldbeunified:CommentonGriffithsetal. Geisler,W.S.&Kersten,D.(2002)Illusions,perceptionandBayes.Nature
andMcClellandetal.TrendsinCognitiveSciences14(8):341. [aAC] Neuroscience5(6):508–10.doi:10.1038/nn0602-508. [GB]
ffytche,D.H.&Howard,R.J.(1999)Theperceptualconsequencesofvisualloss: Geissler,H.-G.(1983)Theinferentialbasisofclassification:Fromperceptualto
“Positive”pathologiesofvision.Brain122:1247–60. [SMS] memorycodesystems.Part1:Theory.In:Modernissuesinperception,ed.
Fine,A.B.,Jaeger,T.F.,Farmer,T.A.&Qian,T.(underreview)Rapidexpectation H.-G.Geissler,H.Buffart,E.Leeuwenberg&V.Sarris,pp.87–105.North-
adaptationduringsyntacticcomprehension. [TAF] Holland. [aAC]
Fiorillo,C.D.(2012)BeyondBayes:OntheneedforaunifiedandJaynesiandefi- Geissler,H.-G.(1991)Constraintsofmentalself-organization:Theindirectvali-
nitionofprobabilityandinformationwithinneuroscience.Information3 dationapproachtowardperception.EstrattodaComunicazioniScientifichedi
(2):175–203.doi:10.3390/info3020175. [WAP] PsicologiaGenerale5:47–69. [aAC]
Flanagan,J.R.&Beltzner,M.A.(2000)Independenceofperceptualandsensori- Geldmacher,D.S.(2003)Visuospatialdysfunctionintheneurodegenerativedis-
motorpredictionsinthesize-weightillusion.NatureNeuroscience3(7):737–41. eases.FrontiersinBioscience8:e428–36. [SMS]
doi:10.1038/76701. [GB] Gerrans,P.(2007)Mechanismsofmadness.Evolutionarypsychiatrywithoutevol-
Flanagan,J.R.,Bittner,J.P.&Johansson,R.S.(2008)Experiencecanchange utionarypsychology.BiologyandPhilosophy22:35–56. [aAC]
distinctsize-weightpriorsengagedinliftingobjectsandjudgingtheirweights. Gershman,S.J.&Daw,N.D.(2012)Perception,actionandutility:Thetangled
CurrentBiology:CB18(22):1742–47.doi:10.1016/j.cub.2008.09.042. [GB] skein.In:Principlesofbraindynamics:Globalstateinteractions,ed.M.I.
Fletcher,P.&Frith,C.(2009)Perceivingisbelieving:ABayesianapproachto Rabinovich,K.J.Friston&P.Varona,pp.293–312.MITPress. [aAC,TF]
explainingthepositivesymptomsofschizophrenia.NatureReviews:Neuro- Gibson,J.J.(1966)Thesensesconsideredasperceptualsystems.Houghton
science10:48–58. [aAC] Mifflin. [AS]
Földiák,P.(1990)Formingsparserepresentationsbylocalanti-Hebbianlearning. Gibson,J.J.(1979)Theecologicalapproachtovisualperception.Houghton
BiologicalCybernetics64:165–70. [TT] Mifflin. [DCD]
Freeman,T.C.A.,Champion,R.A.&Warren,P.A.(2010)ABayesianmodelof Gilbert,D.T.&Wilson,T.D.(2009)Whythebraintalkstoitself:Sourcesoferrorin
perceivedhead-centredvelocityduringsmoothpursuiteyemovement.Current emotionalprediction.PhilosophicalTransactionsoftheRoyalSocietyofLondon
Biology20:757–62. [aAC] BBiologicalScience364(1521):1335–41. [AKS]
FristonK.(2002)Beyondphrenology:Whatcanneuroimagingtellusaboutdis- Glimcher,P.(2003)Decisions,uncertaintyandthebrain.MITPress. [DRo]
tributedcircuitry?AnnualReviewofNeuroscience25:221–50. [aAC] Glimcher,P.(2010)Foundationsofneuroeconomicanalysis.OxfordUniversity
Friston,K.(2003)Learningandinferenceinthebrain.NeuralNetworks16(9):1325– Press. [rAC,DRo]
52. [aAC] Gold, J. N. & Shadlen, M. N. (2001) Neural computations that underlie
Friston,K.(2005)Atheoryofcorticalresponses.PhilosophicalTransactionsofthe decisions about sensory stimuli. Trends in Cognitive Sciences 5(10):16
RoyalSocietyofLondonB:BiologicalSciences360(1456):815–36. [arAC, 238–55. [aAC]
TE,MWS] Gooch,C.M.,Wiener,M.,Hamilton,C.A.&Coslett,B.H.(2001)Temporaldis-
Friston,K.(2008)Hierarchicalmodelsinthebrain.PLoSComputationalBiology4: criminationofsub-andsuprasecondtimeintervals:Avoxel-basedlesion
e1000211. [TE] mappinganalysis.FrontiersinIntegrativeNeuroscience5:1–10. [LH]
Friston,K.(2009)Thefree-energyprinciple:Aroughguidetothebrain?Trendsin Gowaty,P.A.&Hubbell,S.P.(2009)Reproductivedecisionsunderecological
CognitiveSciences13(7):293–301. [aAC,TF,AR] constraints:It’sabouttime.ProceedingsoftheNationalAcademyofSciences
Friston,K.J.(2010)Thefree-energyprinciple:Aunifiedbraintheory?Nature USA106:10017–24. [PAG]
ReviewsNeuroscience11(2):127–38. [aAC,TE,KF,TF,PK,WAP,TT] Gowaty,P.A.&Hubbell,S.P.(2005)Chance,timeallocation,andtheevolutionof
Friston,K.(2011a)Embodiedinference:OrIthinkthereforeIam,ifIamwhatI adaptivelyflexiblesexrolebehavior.IntegrativeandComparativeBiology45
think.In:Theimplicationsofembodiment(CognitionandCommunication),ed. (5):931–44. [PAG]
W.Tschacher&C.Bergomi,pp.89–125.ImprintAcademic. [arAC,DRo] Graesser,A.C.,Millis,K.K.&Zwaan,R.A.(1997)Discoursecomprehension.
Friston,K.(2011b)Whatisoptimalaboutmotorcontrol?Neuron72:488–98. AnnualReviewofPsychology48(1):163–89. [JBH]
[arAC] GrahnJ.A.&Brett,M.(2007)Rhythmandbeatperceptioninmotorareasofthe
Friston,K.,Adams,R.A.,Perrinet,L.&Breakspear,M.(2012)Perceptionsas brain.JournalofCognitiveNeuroscience19(5):893–906. [RSS]
hypotheses:Saccadesasexperiments.FrontiersinPsychology3:151.doi: Grahn,J.A.&McAuley,J.D.(2009)Neuralbasesofindividualdifferencesinbeat
10.3389/fpsyg.2012.00151. [rAC] perception.NeuroImage47:1894–1903. [LH]
Friston,K.J.,Daunizeau,J.&Kiebel,S.J.(2009)Reinforcementlearningoractive Gregory,R.(1998)Brainymind.BritishMedicalJournal317(7174):1693–95.
inference?PLoS(PublicLibraryofScience)One4(7):e6421. [aAC] [GB]
Friston,K.J.,Daunizeau,J.,Kilner,J.&Kiebel,S.J.(2010)Actionandbehavior:A Gregory,R.L.(1980)Perceptionsashypotheses.PhilosophicalTransactionsofthe
free-energyformulation.BiologicalCybernetics102(3):227–60. [aAC] RoyalSocietyofLondonB290(1038):181–97. [aAC,KF]
Friston,K.&Kiebel,S.(2009)Corticalcircuitsforperceptualinference.Neural Griffiths,T.,Chater,N.,Kemp,C.,Perfors,A.&Tenenbaum,J.B.(2010)Prob-
Networks22:1093–104. [arAC] abilisticmodelsofcognition:Exploringrepresentationsandinductivebiases.
Friston,K.,Mattout,J.&Kilner,J.(2011)Actionunderstandingandactiveinfer- TrendsinCognitiveSciences14(8):357–64. [aAC]
ence.BiologicalCybernetics104:137–60. [aAC] Griffiths,P.E.&Gray,R.D.(2001)Darwinismanddevelopmentalsystems.In:
Friston,K.&Stephan,K.(2007)Freeenergyandthebrain.Synthese159(3):417– Cyclesofcontingency:Developmentalsystemsandevolution,eds.S.Oyama,P.
58. [aAC,TF,DYL] E.Griffiths&R.D.Gray,pp.195–218.MITPress. [aAC]
Frith,C.D.(2007)Makingupthemind:Howthebraincreatesourmentalworld. Grill-Spector,K.,Henson,R.&Martin,A.(2006)Repetitionandthebrain:Neural
Blackwell. [BP] modelsofstimulus-specificeffects.TrendsinCognitiveSciences10(1):14–23.
Frith,C.D.(2012)Explainingdelusionsofcontrol:Thecomparatormodel20years [aAC]
on.ConsciousnessandCognition21(1):52–54. [AKS] Grodner,D.&Sedivy,J.(2011)Theeffectofspeaker-specificinformationon
Frith,C.D.&Wentzer,T.S.(inpress)Neuralhermeneutics.In:Encyclopediaof pragmaticinferences.In:Theprocessingandacquisitionofreference,vol.2327,
philosophyandthesocialsciences,vol.1,ed.B.Kaldis.Sage. [rAC,BP] eds.E.Gibson&N.Pearlmutter,pp.239–72.MITPress. [TAF]
Frith,C.,Perry,R.&Lumer,E.(1999)Theneuralcorrelatesofconsciousexperi- Grossberg,S.(2013)AdaptiveResonanceTheory:Howabrainlearnstoconsciously
ence:Anexperimentalframework.TrendsinCognitiveSciences3(3):105. attend,learn,andrecognizeachangingworld.NeuralNetworks37:1–47. [LM]
[aAC] Grush,R.(2004)Theemulationtheoryofrepresentation:Motorcontrol,imagery,
Froese,T.&DiPaolo,E.A.(2011)Theenactiveapproach:Theoreticalsketches andperception.BehavioralandBrainSciences27:377–442. [aAC]
fromcelltosociety.PragmaticsandCognition19(1):1–36. [TF] Hajcak,G.&Foti,D.(2008)Errorsareaversive.PsychologicalScience19(2):103–
Froese,T.&Stewart,J.(2010)LifeafterAshby:Ultrastabilityandtheautopoietic 108. [JBH]
foundationsofbiologicalindividuality.CyberneticsandHumanKnowing17 Harman,K.,HumphreyK.G.&Goodale,M.A.(1999)Activemanualcontrolof
(4):83–106. [TF] objectviewsfacilitatesvisualrecognition.CurrentBiology9:1315–18. [LH]
Froese,T.&Ziemke,T.(2009)Enactiveartificialintelligence:Investigatingthe Harnad,S.(1990)Thesymbolgroundingproblem.PhysicaD42:335–46. [aAC]
systemicorganizationoflifeandmind.ArtificialIntelligence173(3–4):366– Harrison,L.M.,Bestmann,S.,Rosa,M.J.,Penny,W.&Green,G.G.R.(2011)
500. [TF] Timescalesofrepresentationinthehumanbrain:Weighingpastinformationto
Fuster,J.M.(2001)Theprefrontalcortex–anupdate:timeisoftheessence.Neuron predictfutureevents.FrontiersinHumanNeuroscience5:1–8. [LH]
30:319–33. [KF] Haugeland,J.(1998)Mindembodiedandembedded.In:Havingthought:Essaysin
Gallagher,S.(2004)Neurocognitivemodelsofschizophrenia:aneurophenomeno- themetaphysicsofmind,ed.J.Haugeland,pp.207–40.HarvardUniversity
logicalcritique.Psychopathology37(1):8–19. [PG] Press. [aAC]
BEHAVIORALANDBRAINSCIENCES(2013)36:3 247
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Hawkins,J.&Blakeslee,S.(2004)Onintelligence.OwlBooks/TimesBooks. [aAC, Horstmann,G.(2002)Evidenceforattentionalcapturebyasurprisingcolorsin-
TE] gletoninvisualsearch.PsychologicalScience13(6):499–505. [HB]
Hay,J.&Drager,K.(2010)Stuffedtoysandspeechperception.Linguistics48:865– Hosoya,T.,Baccus,S.A.&Meister,M.(2005)Dynamicpredictivecodingbythe
92. [TAF] retina.Nature436(7):71–77. [aAC]
Helbig,H.&Ernst,M.(2007)Optimalintegrationofshapeinformationfromvision Howe,C.Q.,Lotto,R.B.&Purves,D.(2006)Comparisonofbayesianandempirical
andtouch.ExperimentalBrainResearch179:595–605. [aAC] rankingapproachestovisualperception.JournalofTheoreticalBiology
Helmholtz,H.von(1860/1962)Handbuchderphysiologischenoptik,vol.3,ed.& 241:866–75. [aAC]
trans.J.P.C.Southall.Dover.(Originalworkpublishedin1860;DoverEnglish Huang,Y.&Rao,R.(2011)Predictivecoding.WileyInterdisciplinaryReviews:
editionin1962). [aAC] CognitiveScience2:580–93. [aAC]
Helmholtz,H.von(1876)HandbuchderphysiologischenOptik.LeopoldVoss. Hubbell,S.P.&Johnson,L.K.(1987)Environmentalvarianceinlifetimemating
[TE] success,matechoice,andsexualselection.AmericanNaturalist130(1):91–
Hennig,H.,Fleischmann,R.,Fredebohm,A.,Hagmayer,Y.,Nagler,J.,Witt,A., 112. [PAG]
Theis,F.J.&Geisel,T.(2011)Thenatureandperceptionoffluctuationsin Hubel,D.H.&Wiesel,T.N.(1965)Receptivefieldsandfunctionalarchitecturein
humanmusicalrhythms.PLoSONE6(10):e26457. [RSS] twononstriatevisualareas(18and19)ofthecat.JournalofNeurophysiology
Hesselmann,G.,Kell,C.A.&Kleinschmidt,A.(2010)Predictivecodingorevidence 28:229–89. [TE]
accumulation?FalseinferenceandneuronalfluctuationsPloSOne5(3):9926 Hume,D.(1739/1888/1964)Treatiseofhumannature,ed.L.A.Selby-Biggs.Oxford
[LM] UniversityPress.(Originalworkpublishedin1739;OUPedition1888;reprint
Hesselmann,G.,Sadaghiani,S.,Friston,K.J.&Kleinschmidt,A.(2010)Predictive 1964sourcecited.) [DCD]
codingorevidenceaccumulation?Falseinferenceandneuronalfluctuations. Humphrey,N.(2000)Howtosolvethemind-bodyproblem.JournalofConscious-
PloS(PublicLibraryofScience)One5(3):e9926. [aAC] nessStudies7:5–20. [aAC]
Hinton,G.E.(2002)Trainingproductsofexpertsbyminimizingcontrastivediver- Hurley,M.,Dennett,D.C.&Adams,R.B.,Jr.(2011)Insidejokes:Usinghumorto
gence.NeuralComputation14(8):1711–800. [aAC] reverse-engineerthemind.MITPress. [DCD]
Hinton,G.E.(2007a)Learningmultiplelayersofrepresentation.TrendsinCog- Hurley,S.(1998)Consciousnessinaction.HarvardUniversityPress. [aAC,NS]
nitiveSciences11:428–34. [aAC] Huron,D.(2006)Sweetanticipation:Musicandthepsychologyofexpectation.MIT
Hinton,G.E.(2007b)Torecognizeshapes,firstlearntogenerateimages.In: Press. [RSS]
Computationalneuroscience:Theoreticalinsightsintobrainfunction,eds.P. Hutchins,E.(1995)Cognitioninthewild.MITPress. [arAC]
Cisek,T.Drew&J.Kalaska.Elsevier. [aAC] Ikegami,T.(2007)Simulatingactiveperceptionandmentalimagerywithembodied
Hinton,G.E.(2010)Learningtorepresentvisualinput.PhilosophicalTransactions chaoticitinerancy.JournalofConsciousnessStudies14(7):111–25. [TF]
oftheRoyalSociety,B.365:177–84. [aAC] Iriki,A.&Taoka,M.(2012)Triadic(ecological,neural,cognitive)nicheconstruc-
Hinton,G.E.,Dayan,P.,Frey,B.J.&Neal,R.M.(1995)Thewake-sleepalgorithm tion:Ascenarioofhumanbrainevolutionextrapolatingtooluseandlanguage
forunsupervisedneuralnetworks.Science268:1158–60. [aAC] fromthecontrolofreachingactions.PhilosophicalTransactionsoftheRoyal
Hinton,G.E.&Ghahramani,Z.(1997)Generativemodelsfordiscoveringsparse SocietyB367:10–23. [aAC]
distributedrepresentations.PhilosophicalTransactionsoftheRoyalSocietyB Jaeger,H.(2011)Neuralhierarchies:Singin’theblues.Oralpresentationat
352:1177–90. [aAC] OsnabrückComputationalCognitionAllianceMeeting(OCCAM2011),Uni-
Hinton,G.E.&Nair,V.(2006)Inferringmotorprogramsfromimagesofhand- versityofOsnabrück,Germany,June22–24,2011.Availableat:http://video.
writtendigits.In:Advancesinneuralinformationprocessingsystems18:Pro- virtuos.uni-osnabrueck.de:8080/engage/ui/watch.html?id=10bc55e8-8d98-
ceedingsofthe2005NIPSConference,ed.Y.Weiss,B.Scholkopf&J.Platt,pp. 40d3-bb11-17780b70c052&play=true. [TT]
515–22.MITPress. [rAC] Jahanshahi,M.,Dirnberger,G.,Fuller,R.&Frith,C.D.(2000)Theroleofthe
Hinton,G.E.,Osindero,S.&Teh,Y.(2006)Afastlearningalgorithmfordeepbelief dorsolateralprefrontalcortexinrandomnumbergeneration:Astudywith
nets.NeuralComputation18:1527–54. [aAC] positronemissiontomography.NeuroImage12:713–25. [LH]
Hinton,G.E.&Salakhutdinov,R.R.(2006)Reducingthedimensionalityofdata James,W.(1890)Theprinciplesofpsychology.HenryHolt. [AKS]
withneuralnetworks.Science313(5786):504–507. [aAC] Janoff-Bulman,R.(1992)Shatteredassumptions:Towardsanewpsychologyof
Hinton,G.E.&vanCamp,D.(1993)Keepingneuralnetworkssimplebymini- trauma.FreePress. [JBH]
mizingthedescriptionlengthofweights.In:ProceedingsofCOLT-93(Sixth Jaynes,E.T.(1957)Informationtheoryandstatisticalmechanics.PhysicalReview
AnnualConferenceonComputationalLearningTheory,SantaCruz,CA,July (SeriesII)106(4):620–30. [KF]
26–28,1993),ed.L.Pitt,pp.5–13.ACMDigitalLibrary. [aAC] Jaynes,E.T.(2003)Probabilitytheory:Thelogicofscience.CambridgeUniversity
Hinton,G.E.&Zemel,R.S.(1994)Autoencoders,minimumdescriptionlengthand Press. [WAP]
Helmholtzfreeenergy.In:Advancesinneuralinformationprocessingsystems Jeannerod,M.(2006)Motorcognition:Whatactionstelltheself.OxfordUniversity
6,eds.J.Cowan,G.Tesauro&J.Alspector.MorganKaufmann. [aAC] Press. [PG]
Hirsch,H.V.B.&Spinelli,D.(1970)Visualexperiencemodifiesdistributionof Jeannerod,M.,Farrer,C.,Franck,N.,Fourneret,P.,Posada,A.,Daprati,E.&
horizontallyandverticallyorientedreceptivefieldsincats.Science168:869– Georgieff,N.(2003)Actionrecognitioninnormalandschizophrenicsubjects.
71. [BB] In:Theselfinneuroscienceandpsychiatry,ed.N.Kirchner&A.David,pp.
Hirsh,J.B.,Mar,R.A.&Peterson,J.B.(2012)Psychologicalentropy:Aframework 380–406.CambridgeUniversityPress. [PG]
forunderstandinguncertainty-relatedanxiety.PsychologicalReview119 Jehee,J.F.M.&Ballard,D.H.(2009)Predictivefeedbackcanaccountforbiphasic
(2):304–20. [JBH] responsesinthelateralgeniculatenucleus.PLoS(PublicLibraryofScience)
Hochstein,S.&Ahissar,M.(2002)Viewfromthetop:Hierarchiesandreverse ComputationalBiology5(5):e1000373. [aAC]
hierarchiesinthevisualsystem.Neuron36(5):791–804. [aAC] Jiang,J.,Schmajuk,N.&Egner,T.(2012)Explainingneuralsignalsinhumanvisual
Hogg,D.(1983)Model-basedvision:Aprogramtoseeawalkingperson.Imageand cortexwithanassociativelearningmodel.BehavioralNeuroscience126(4):575–
VisionComputing1(1):5–20. [AS] 81. [TE]
Hohwy,J.(2007)FunctionalIntegrationandthemind.Synthese159(3):315–28. Johnston,A.,Arnold,D.H.&Nishida,S.(2006)Spatiallylocalizeddistortionsof
[aAC] time.CurrentBiology16:472–79. [LH]
Hohwy,J.(2012)Attentionandconsciousperceptioninthehypothesistestingbrain. Kalman,R.E.(1960)Anewapproachtolinearfilteringandpredictionproblems.
FrontiersinPsychology3:96,1–14.doi:10.3389/fpsyg.2012.00096. [rAC,LM] TransactionsoftheASME–JournalofBasicEngineering(SeriesD)82:35–
Hohwy,J.&Paton,B.(2010)Explainingawaythebody:Experiencesofsuperna- 45. [DRa]
turallycausedtouchandtouchonnon-handobjectswithintherubberhand Kant,I.(1781/1929)Critiqueofpurereason,trans.N.KempSmith.Macmillan.
illusion.PLoSONE5(2):e9416. [BP] (Originalworkpublishedin1781;KempSmithtranslation1929). [AS]
Hohwy,J.,Roepstorff,A.&Friston,K.(2008)Predictivecodingexplainsbinocular Kärcher,S.M.,Fenzlaff,S.,Hartmann,D.,Nagel,S.K.&König,P.(2012)Sensory
rivalry:Anepistemologicalreview.Cognition108(3):687–701. [aAC,MLA] augmentationfortheblind.FrontiersinHumanNeuroscience6:37. [PK]
Hollensen,P.&Trappenberg,T.(2011)Learningsparserepresentationsthrough Karmarkar,U.R&Buonomano,D.V.(2007)Timingintheabsenceofclocks:
learnedinhibition.PosterpresentedattheCOSYNE(Computationaland Encodingtimeinneuralnetworkstates.Neuron53:427–38. [LH]
SystemsNeuroscienceConference)AnnualMeeting,SaltLakeCity,Utah, Karmiloff-Smith,A.(1992)Beyondmodularity:Adevelopmentalperspectiveon
February24,2011. [TT] cognitivescience.MITPress. [AS]
Holleman,J.R.&Schultz,W.(1998)Dopamineneuronsreportanerrorinthe Kawato,M.,Hayakama,H.&Inui,T.(1993)Aforward-inverseopticsmodelof
temporalpredictionofrewardduringlearning.NatureReviews:Neuroscience reciprocalconnectionsbetweenvisualcorticalareas.Network4:415–22.
1:304–309. [aAC] [aAC]
Holm,L.,Ullén,F.&Madison,G.(inpress)Motorandexecutivecontrolin Kay,J.,Floreano,D.&Phillips,W.A.(1998)Contextuallyguidedunsupervised
repetitivetimingofbriefintervals.JournalofExperimentalPsychology:Human learningusinglocalmultivariatebinaryprocessors.NeuralNetworks11:117–
PerceptionandPerformance.doi10.1037/a0029142. [LH] 40. [WAP]
248 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Kay,J.&Phillips,W.A.(2010)CoherentInfomaxasacomputationalgoalforneural activityinauditory,somatosensory,andvisualcortices.CerebralCortex21
systems.BulletinofMathematicalBiology73:344–72.doi:10.1007/s11538-010- (12):2850–62. [aAC]
9564-x. [rAC,WAP] Large,E.W.,Fink,P.&Kelso,J.A.S.(2002)Trackingsimpleandcomplex
Keane,B.P.,Silverstein,S.M.,Wang,Y.,Zalakostas,A.,Vlajnic,V.,Mikkilineni,D. sequences.PsychologicalResearch66:3–17. [RSS]
&Papathomas,T.V.(inpress)Reduceddepthinversionillusionsinschizo- Lee,D.&Wang,X.-J.(2009)Mechanismsforstochasticdecisionmakinginthe
phreniaarestate-specificandoccurformultipleobjecttypesandviewing primatefrontalcortex:Single-neuronrecordingandcircuitmodeling.In:
conditions.JournalofAbnormalPsychology. [SMS] Neuroeconomics:Decisionmakingandthebrain,ed.P.Glimcher,C.Camerer,
Keller,G.B.,Bonhoeffer,T.&Hubener,M.(2012)Sensorimotormismatchsignals E.Fehr&R.Poldrack,pp.481–501.Elsevier. [rAC,DRo]
inprimaryvisualcortexofthebehavingmouse.Neuron74:809–15. [rAC,TE] Lee,H.,Ekanadham,C.&Ng,A.(2008)Sparsedeepbeliefnetmodelforvisualarea
Khalil,E.L.(1989)AdamSmithandAlbertEinstein:Theaestheticprincipleof V2.In:AdvancesinNeuralInformationProcessingSystems20(NIPS’07),ed.J.
truth.HistoryofEconomicsSocietyBulletin11(2):222–37. [ELK] Platt,D.Koller,Y.Singer,&S.Roweis,pp.873–80.MITPress. [TT]
Khalil,E.L.(2010)TheBayesianfallacy:Distinguishinginternalmotivationsand Lee,M.(2010)EmergentandstructuredcognitioninBayesianmodels:Comment
religiousbeliefsfromotherbeliefs.JournalofEconomicBehaviorandOrgan- onGriffithsetal.andMcClellandetal.TrendsinCognitiveSciences14
ization75(2):268–80.doi:10.1016/j.jebo.2010.04.004. [ELK] (8):345–46. [aAC]
Kinoshita,M.,Gilbert,C.D.&Das,A.(2009)Opticalimagingofcontextualinter- Lee,S.H.,Blake,R.&Heeger,D.J.(2005)Travelingwavesofactivityin
actionsinV1ofthebehavingmonkey.JournalofNeurophysiology102:1930– primaryvisualcortexduringbinocularrivalry.NatureNeuroscience8
44. [SMS] (1):22–23. [aAC]
Kitayama,S.&Cohen,D.(2010)Handbookofculturalpsychology.TheGuilford Lee,T.S.&Mumford,D.(2003)HierarchicalBayesianinferenceinthevisual
Press. [JBH] cortex.JournalofOpticalSocietyofAmerica,A20(7):1434–48. [aAC]
Kleinschmidt,D.&Jaeger,T.F.(2011)ABayesianbeliefupdatingmodelofphonetic Lehnert,W.(2007)Cognition,computers,andcarbombs:HowYalepreparedme
recalibrationandselectiveadaptation.AssociationforComputationalLinguistics forthe90’s.In:Beliefs,reasoning,anddecisionmaking:Psycho-logicinhonorof
–ComputationalModelingandComputationalLinguistics. [TAF] BobAbelson,ed.R.Schank&E.Langer,pp.143–73.Erlbaum. [aAC]
Knill,D.&Pouget,A.(2004)TheBayesianbrain:Theroleofuncertaintyinneural Lenggenhager,B.,Tadi,T.,Metzinger,T.&Blanke,O.(2007)Videoergosum:
codingandcomputation.TrendsinNeuroscience27(12):712–19. [aAC] Manipulatingbodilyself-consciousness.Science317(5841):1096. [BP]
Koethe,D.,Kranaster,L.,Hoyer,C.,Gross,S.,Neatby,M.A.,Schultze-Lutter,F., Leopold,D.&Logothetis,N.(1999)Multistablephenomena:Changingviewsin
Ruhrmann,S.,Klosterkötter,J.,Hellmich,M.&Leweke,F.M.(2009)Bin- perception.TrendsinCognitiveSciences3:254–64. [aAC]
oculardepthinversionasaparadigmofreducedvisualinformationprocessingin Levinson,S.C.(2006)Onthehuman“InteractionEngine.”In:Rootsofhuman
prodromalstate,antipsychotic-naiveandtreatedschizophrenia.European sociality,ed.N.J.Enfield&S.C.Levinson,pp.39–69.Berg. [AR]
ArchivesofPsychiatryandClinicalNeuroscience259:195–202. [SMS] Lewis,P.A.&Miall,R.C.(2003)Distinctsystemsforautomaticandcognitively
Kohonen,T.(1989)Self-organizationandassociativememory.Springer-Verlag. controlledtimemeasurement:Evidencefromneuroimaging.CurrentOpinion
[aAC] inNeurobiology13:250–55. [LH]
Kok,P.,Jehee,J.F.&deLange,F.P.(2012)Lessismore:Expectationsharpens Lewis,P.A.&Miall,R.C.(2006)Arighthemisphericprefrontalsystemforcognitive
representationsintheprimaryvisualcortex.Neuron75(2):265–70. [LM] timemeasurement.BehaviouralProcesses71:226–234. [LH]
Kok,P.,Rahnev,D.,Jehee,J.F.,Lau,H.C.&deLange,F.P.(2011)Attention Ling,S.&Carrasco,M.(2006)Whensustainedattentionimpairsperception.Nature
reversestheeffectofpredictioninsilencingsensorysignals.CerebralCortex Neuroscience9(10):1243–45. [NB]
22:2197–206. [rAC,TE] Linsker,R.(1989)Anapplicationoftheprincipleofmaximuminformationpreser-
König,P.&Krüger,N.(2006)Symbolsasself-emergententitiesinanoptimization vationtolinearsystems.In:Advancesinneuralinformationprocessingsystems,
processoffeatureextractionandpredictions.BiologicalCybernetics94(4):325– vol.1,ed.D.S.Touretzky,pp.86–194.Springer. [aAC]
34. [aAC,PK] Little,D.Y.&Sommer,F.T.(2011)Learninginembodiedaction-perceptionloops
Körding,K.P.,Kayser,C.,Einhäuser,W.&König,P.(2004)Howarecomplexcell throughexploration.OnlinePublicationarXive:1112.1125. [DYL]
propertiesadaptedtothestatisticsofnaturalstimuli?JournalofNeurophy- Lochmann,T.&DeneveS.(2011)Neuralprocessingascausalinference.Current
siology91(1):206–12. [PK] OpinioninNeurobiology21(5):774–78. [MWS]
Körding,K.P.&König,P.(2000)Learningwithtwositesofsynapticintegration. Lochmann,T.,Ernst,U.A.&Denève,S.(2012)Perceptualinferencepredicts
Network:ComputationinNeuralSystems11:1–15. [WAP] contextualmodulationsofsensoryresponses.TheJournalofNeuroscience32
Körding,K.P.,Tenenbaum,J.B.&Shadmehr,R.(2007)Thedynamicsofmemory (12):4179–95. [NB]
asaconsequenceofoptimaladaptationtoachangingbody.NatureNeuro- Loui,P.,Wessel,D.&HudsonKam,C.L.(2010)Humansrapidlylearngrammatical
science10:779–86. [aAC] structureinanewmusicalscale.MusicPerception27:377–88. [RSS]
Körding,K.P.&Wolpert,D.M.(2004)Bayesianintegrationinsensorimotor Luck,S.J.(2006)Theoperationofattention–millisecondbymillisecond–overthe
learning.Nature427(6971):244–47.doi:10.1038/nature02169. [GB] firsthalfsecond.In:Thefirsthalfsecond:Themicrogenesisandtemporal
Kosslyn,S.M.,Thompson,W.L.,Kim,I.J.&Alpert,N.M.(1995)Topographical dynamicsofunconsciousandconsciousvisualprocessing,ed.H.Ö.B.G.
representationsofmentalimagesinprimaryvisualcortex.Nature378:496– Breitmeyer,pp.187–206.MITPress. [HB]
98. [aAC] MacKay,D.J.C.(1995)Free-energyminimizationalgorithmfordecodingand
Kraljic,T.,Samuel,A.G.&Brennan,S.E.(2008)Firstimpressionsandlastresorts: cryptoanalysis.ElectronLetters31:445–47. [aAC]
Howlistenersadjusttospeakervariability.PsychologicalScience19:332–38. MacKay,D.M.(1956)Theepistemologicalproblemforautomata.In:Automatastudies,
[TAF] ed.C.E.Shannon&J.McCarthy,pp.235–51.PrincetonUniversityPress. [aAC]
Kriegstein,K.&Giraud,A.(2006)Implicitmultisensoryassociationsinfluencevoice Madison,G.(2001)Variabilityinisochronoustapping:Higher-orderdependencies
recognition.PLoS(PublicLibraryofScience)Biology4(10):e326. [aAC] asafunctionofintertapinterval.JournalofExperimentalPsychology:Human
Kukona,A.,Fang,S.,Aicher,K.A.,Chen,H.&Magnuson,J.S.(2011)Thetime PerceptionandPerformance27:411–22. [LH]
courseofanticipatoryconstraintintegration.Cognition119:23–42. [TAF] Madison,G.,Forsman,L.,Blom,Ö.,Karabanov,A.&Ullén,F.(2009)Correlations
Kurumada,C.,Brown,M.&Tanenhaus,M.K.(2012)Pragmaticinterpretationof betweengeneralintelligenceandcomponentsofserialtimingvariability.
contrastiveprosody:Itlookslikeadaptation.In:Proceedingsofthe34thAnnual Intelligence37:68–75. [LH]
ConferenceoftheCognitiveScienceSociety,ed.N.Miyake,D.Peebles,&R.P. Maher,B.(1988)Anomalousexperienceanddelusionalthinking:Thelogicof
Cooper,pp.647–52.CognitiveScienceSociety. [TAF] explanations.In:Delusionalbeliefs,ed.T.F.Oltmanns&B.A.Maher,pp.15–
Kveraga,K.,Ghuman,A.&Bar,M.(2007)Top-downpredictionsinthecognitive 33.Wiley. [aAC]
brain.BrainandCognition65:145–68. [aAC] Maloney,L.T.&Mamassian,P.(2009)Bayesiandecisiontheoryasamodelofvisual
Ladinig,O.,Honing,H.,Haden,G.&Winkler,I.(2009)Probingattentiveand perception:TestingBayesiantransfer.VisualNeuroscience26:147–55. [aAC]
preattentiveemergentmeterinadultlistenerswithoutextensivemusictraining. Maloney,L.T.&Zhang,H.(2010)Decision-theoreticmodelsofvisualperception
MusicPerception26:377–86. [LH] andaction.VisionResearch50:2362–74. [aAC]
Landauer,T.K.&Dumais,S.T.(1997)AsolutiontoPlato’sproblem:TheLatent Mamassian,P.,Landy,M.&Maloney,L.(2002)Bayesianmodelingofvisualper-
SemanticAnalysistheoryoftheacquisition,induction,andrepresentationof ception.In:Probabilisticmodelsofthebrain,ed.R.Rao,B.Olshausen&M.
knowledge.PsychologicalReview104:211–40. [aAC] Lewicki,pp.13–36.MITPress. [aAC]
Landauer,T.K.,Foltz,P.W.&Laham,D.(1998)IntroductiontoLatentSemantic Mandler,J.M.(1984)Stories,scripts,andscenes:Aspectsofschematheory.
Analysis.DiscourseProcesses25:259–84. [aAC] Erlbaum. [JBH]
Lange,C.G.(1885/1912).Themechanismsoftheemotions.In:TheClassicalPsy- Mar,R.A.&Oatley,K.(2008)Thefunctionoffictionistheabstractionandsimulation
chologists,ed.B.Rand.pp.672–684.HoughtonMifflin. [AKS] ofsocialexperience.PerspectivesonPsychologicalScience3(3):173–92. [JBH]
Langner,R.,Kellermann,T.,Boers,F.,Sturm,W.,Willmes,K.&Eickhoff,S.B. Marcus,G.(2008)Kluge:Thehaphazardconstructionofthehumanmind.
(2011)Modality-specificperceptualexpectationsselectivelymodulatebaseline Houghton-Mifflin. [aAC]
BEHAVIORALANDBRAINSCIENCES(2013)36:3 249
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Mareschal,D.,Johnson,M.H.,Siros,S.,Spratling,M.W.,Thomas,M.S.C.& Murray,S.O.,Schrater,P.&Kersten,D.(2004)Perceptualgroupingandthe
Westermann,G.(2007)Neuroconstructivism–I.:Howthebrainconstructs interactionsbetweenvisualcorticalareas.NeuralNetworks17(5–6):695–705.
cognition.OxfordUniversityPress. [aAC,MWS] [aAC]
Marr,D.(1982).Vision:Acomputationalapproach.Freeman. [aAC] Musmann,H.(1979)Predictiveimagecoding.In:Imagetransmissiontechniques,
Matell,M.S.&Meck,W.H.(2004)Cortico-striatalcircuitsandintervaltiming: ed.W.K,Pratt,AdvancesinElectronicsandElectronPhysics,Supplement
Coincidencedetectionofoscillatoryprocesses.CognitiveBrainResearch 12:73–112,AcademicPress,Orlando,FL. [aAC]
21:139–70. [LH] Nagarajan,S.S.,Blake,D.T.,Wright,B.A.,Byl,N.&Merzenich,M.M.(1998)
Mattusek,P.(1987)Studiesindelusionalperception(translatedandcondensed).In: Practice-relatedimprovementsaretemporallyspecificbutgeneralizeacross
Clinicalrootsoftheschizophreniaconcept.TranslationsofseminalEuropean skinlocation,hemisphereandmodality.JournalofNeuroscience18:1559–70.
contributionsonSchizophrenia,ed.JCutting&M.Sheppard,pp.87–103. [LH]
CambridgeUniversityPress.(Originallypublishedin1952.) [SMS] Nagel,S.K.,Carl,C.,Kringe,T.,Märtin,R.&König,P.(2005)Beyondsensory
McAdams,D.P.(1997)Thestoriesweliveby:Personalmythsandthemakingofthe substitution–learningthesixthsense.JournalofNeuralEngineering2(4):R13–
self.TheGuilfordPress. [JBH] R26.doi:10.1088/1741-2560/2/4/R02. [PK]
McAdams,D.P.(2006)Theproblemofnarrativecoherence.JournalofConstruc- Narmour,E.(1990)Theanalysisandcognitionofbasicmelodicstructures:The
tivistPsychology19(2):109–25. [JBH] implication-realizationmodel.UniversityofChicagoPress. [RSS]
McCarthy,J.(2008)Thewell-designedchild.ArtificialIntelligence172(18):2003– Neal,R.M.&Hinton,G.(1998)AviewoftheEMalgorithmthatjustifiesincre-
14. [AS] mental,sparse,andothervariants.In:Learningingraphicalmodels,ed.M.I.
McClelland,J.,Botvinick,M.,Noelle,D.,Plaut,D.,Rogers,T.,Seidenberg,M.& Jordan,pp.355–68.Kluwer. [aAC]
Smith,L.(2010)Lettingstructureemerge:Connectionistanddynamical Neisser,U.(1967)Cognitivepsychology.Appleton-Century-Crofts. [aAC]
systemsapproachestocognition.TrendsinCognitiveSciences14(8):348–56. Nelson,K.(2003)Selfandsocialfunctions:Individualautobiographicalmemoryand
[aAC] collectivenarrative.Memory11(2):125–36. [JBH]
McClelland,J.&Rumelhart,D.(1981)Aninteractiveactivationmodelofcontext Nelson,K.&Fivush,R.(2004)Theemergenceofautobiographicalmemory:Asocial
effectsinletterperception:Part1.Anaccountofbasicfindings.Psychological culturaldevelopmentaltheory.PsychologicalReview111(2):486–511. [JBH]
Review88:375–407. [aAC] Nelson,P.(2012)Towardsasocialtheoryofrhythm.In:Topicsinmusicaluniversals/
McClelland,J.,Rumelhart,D.&thePDPResearchGroup(1986)Paralleldistrib- ActualitésdesUniversauxMusicaux,ed.J.-L.Leroy.EditionsdesArchives
utedprocessing,vol.2.MITPress. [aAC] Contemporaines. [RSS]
McMurray,B.,Tanenhaus,M.K.&Aslin,R.N.(2009)Within-categoryVOTaffects Noë,A.(2004)Actioninperception.MITPress. [aAC,TF]
recoveryfrom“lexical”gardenpaths:Evidenceagainstphoneme-levelinhi- Noë,A.(2009)Outofourheads:Whyyouarenotyourbrain,andotherlessonsfromthe
bition.JournalofMemoryandLanguage60:65–91. [TAF] biologyofconsciousness.Farrar,StrausandGiroux/HillandWang. [aAC,TF]
Melloni,L.,Schwiedrzik,C.M.,Muller,N.,Rodriguez,E.&Singer,W.(2011) North,A.C.&Hargreaves,D.J.(1995)Subjectivecomplexity,familiarity,andliking
Expectationschangethesignaturesandtimingofelectrophysiologicalcorrelates forpopularmusic.Psychomusicology14:77–93. [RSS]
ofperceptualawareness.JournalofNeuroscience31(4):1386–96. [aAC] Oatley,K.(1992)Bestlaidschemes:Thepsychologyofemotions.CambridgeUni-
Menary,R.(2007)Cognitiveintegration:Attackingtheboundsofcognition.Palgrave versityPress. [JBH]
Macmillan. [aAC] Oatley,K.(1999)Whyfictionmaybetwiceastrueasfact:Fictionascognitiveand
Meng,M.&Tong,F.(2004)Canattentionselectivelybiasbistableperception? emotionalsimulation.ReviewofGeneralPsychology3(2):101–17. [JBH]
differencesbetweenbinocularrivalryandambiguousfigures.JournalofVision Olshausen,B.A.&Field,D.J.(1996)Emergenceofsimple-cellreceptivefield
4:539–51. [aAC] propertiesbylearningasparsecodefornaturalimages.Nature381(6583):607–
Merker,B.(2004)Cortex,countercurrentcontext,anddimensionalintegrationof 609. [arAC,PK,TT]
lifetimememory.Cortex40:559–76. [aAC] Olshausen,B.A.&Field,D.J.(2005)HowclosearewetounderstandingV1?
Merker,B.H.,MadisonG.S.&Eckerdal,P.(2009)Ontheroleandoriginofiso- NeuralComputation17:1665–99. [MWS]
chronyinhumanrhythmicentrainment.Cortex45:4–17. [LH] Overy,K.&Molnar-Szakacs,I.(2009)Beingtogetherintime:Musicalexperience
Meyer,T.&Olson,C.R.(2011)Statisticallearningofvisualtransitionsinmonkey andthemirrorneuronsystem.MusicPerception26(5):489–504. [aAC,RSS]
inferotemporalcortex.ProceedingsoftheNationalAcademyofSciencesUSA Owen,A.M.,McMillan,K.M.,Laird,A.R.&Bullmore,E.(2005)N-backworking
108:19401–406. [rAC,TE] memoryparadigm:Ameta-analysisofnormativefunctionalneuroimaging
Meyer.L.B.(1956)Emotionandmeaninginmusic.UniversityofChicagoPress. studies.HumanBrainMapping25:46–59. [LH]
[RSS] Oyama,S.(1999)Evolution’seye:Biology,cultureanddevelopmentalsystems.Duke
Miall,R.C.(1989)Thestorageoftimeintervalsusingoscillatingneurons.Neural UniversityPress. [aAC]
Computation1:359–71. [LH] Pack,C.C.&Born,R.T.(2001)Temporaldynamicsofaneuralsolutiontothe
Milner,D.&Goodale,M.(2006)Thevisualbraininaction,2ndedition.Oxford apertureprobleminvisualareaMTofmacaquebrain.Nature409:1040–42.
UniversityPress. [aAC] [aAC]
Molnar-Szakacs,I.&Overy,K.(2006)Musicandmirrorneurons:Frommotionto‘e’ Palaniyappan,L.&Liddle,P.F.(2012)Doesthesaliencenetworkplayacardinal
motion.SocialCognitionandAffectiveNeuroscience1:235–41. [RSS] roleinpsychosis?Anemerginghypothesisofinsulardysfunction.Journalof
Morrone,C.M.,Ross,J.&Burr,D.(2005)Saccadiceyemovementscausecom- PsychiatryandNeuroscience37(1):17–27. [AKS]
pressionoftimeaswellasspace.NatureNeuroscience8:950–54. [LH] Pascual-Leone,A.&Hamilton,R.(2001)Themetamodalorganizationofthebrain.
Muckli,L.(2010)Whatarewemissinghere?Brainimagingevidenceforhigher ProgressinBrainResearch134:427–45. [aAC]
cognitivefunctionsinprimaryvisualcortexV1.InternationalJournalofImaging Paulus,M.P.&Stein,M.B.(2006)Aninsularviewofanxiety. [Review].Biological
SystemsTechnology(IJIST)20:131–39. [aAC] Psychiatry60(4):383–87. [AKS]
Muckli,L.,Kohler,A.,Kriegeskorte,N.&Singer,W.(2005)Primaryvisualcortex Pearce,J.M.&Hall,G.(1980)AmodelforPavlovianlearning:Variationsinthe
activityalongtheapparent-motiontracereflectsillusoryperception.PLoS effectivenessofconditionedbutnotofunconditionedstimuli.Psychological
(PublicLibraryofScience)Biologyl3:e265. [aAC,LM] Review87:532–52. [TE]
Muckli,L.&Petro,L.S.(2013)Networkinteractions:Non-geniculateinputtoV1. Pecenka,N.&Keller,P.E.(2011)Theroleoftemporalpredictionabilitiesin
CurrentOpinioninNeurobiology23(2):195–201. [LM] interpersonalsensorimotorsynchronization.ExperimentalBrainResearch211:
Mumford,D.(1992)Onthecomputationalarchitectureoftheneocortex.II.The 505–15. [RSS]
roleofcortico-corticalloops.BiologicalCybernetics66(3):241–51. [arAC, Pennebaker,J.W.&Seagal,J.D.(1999)Formingastory:Thehealthbenefitsof
TE,KF] narrative.JournalofClinicalPsychology55(10):1243–54. [JBH]
Mumford,D.(1994)Neuronalarchitecturesforpattern-theoreticproblems.In: Peterson,J.B.(1999)Mapsofmeaning:Thearchitectureofbelief.Routledge.
Large-scaletheoriesofthecortex,ed.C.Koch&J.Davis,pp.125–52.MIT [JBH]
Press. [aAC] Petkova,V.I.&Ehrsson,H.H.(2008)IfIwereyou:Perceptualillusionofbody
Murray,D.J.,Ellis,R.R.,Bandomir,C.A.&Ross,H.E.(1999)Charpentier(1891) swapping.PLoSONE3(12):e3832. [BP]
onthesize-weightillusion.PerceptionandPsychophysics61(8):1681–85. Pfeifer,R.,Lungarella,M.,Sporns,O.&Kuniyoshi,Y.(2007)Ontheinformation
[GB] theoreticimplicationsofembodiment–principlesandmethods.LectureNotes
Murray,S.O.,Boyaci,H.&Kersten,D.(2006)Therepresentationofperceived inComputerScience(LNCS),vol.4850.Springer. [arAC]
angularsizeinhumanprimaryvisualcortex.NatureReviews:Neuroscience Phillips,W.A.(2012)Self-organizedcomplexityandcoherentInfomaxfromthe
9:429–34. [aAC] viewpointofJaynes’sprobabilitytheory.Information3(1):1–15.doi:10.3390/
Murray,S.O.,Kersten,D.,Olshausen,B.A.,Schrater,P.&Woods,D.L.(2002) info3010001. [WAP,SMS]
Shapeperceptionreducesactivityinhumanprimaryvisualcortex.Proceedings Phillips,W.A.,Chapman,K.L.S.&Berry,P.D.(2004)Sizeperceptionisless
oftheNationalAcademyofSciencesUSA99(23):15164–69. [arAC,TE] context-sensitiveinmales.Perception33:79–86. [WAP]
250 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Phillips,W.A.,Kay,J.&Smyth,D.(1995)Thediscoveryofstructurebymultistream Ricoeur,P.,Blamey,K.&Pellauer,D.(1990)Timeandnarrative,vol.3.University
networksoflocalprocessorswithcontextualguidance.Network:Computation ofChicagoPress. [JBH]
inNeuralSystems6:225–46. [rAC,PK,WAP] Rieke,F.(1999)Spikes:Exploringtheneuralcode,MITPress. [aAC]
Phillips,W.A.&Silverstein,S.M.(2003)Convergenceofbiologicalandpsycho- Riesenhuber,M.&Poggio,T(2000)Modelsofobjectrecognition.NatureNeuro-
logicalperspectivesoncognitivecoordinationinschizophrenia.Behavioraland science3(Suppl.):1199–204. [TE]
BrainSciences26:65–82;discussion82–137. [WAP,SMS] Robbins,H.(1956)AnempiricalBayesapproachtostatistics.In:Proceedingsofthe
Phillips,W.A.&Singer,W.(1997)Insearchofcommonfoundationsforcortical ThirdBerkeleySymposiumonMathematicalStatisticsandProbability,vol.1:
computation.BehavioralandBrainSciences20:657–722. [WAP,MWS] ContributionstotheTheoryofStatistics,pp.157–63.UniversityofCalifornia
Phillips,W.A.,vonderMalsburg,C.&Singer,W.(2010)Dynamiccoordinationin Press. [aAC]
brainandmind.In:StrüngmannForumReport,vol.5:Dynamiccoordinationin Roepstorff,A.(2008)Thingstothinkwith:Wordsandobjectsasmaterialsymbols.
thebrain:Fromneuronstomind,ed.C.vonderMalsburg,W.A.Phillips& PhilosophicalTransactionsoftheRoyalSociety,B363(1499):2049–54. [AR]
W.Singer,Chapter1,pp.1–24.MITPress. [rAC,WAP] Roepstoff,A.&Frith,C.(2012)Neuroanthropologyorsimplyanthropology?Going
Phillips-SilverJ.&Trainor,L.J.(2007)Hearingwhatthebodyfeels:Auditory experimentalasmethod,asobjectofstudy,andasresearchaesthetic.Anthro-
encodingofrhythmicmovement.Cognition105:533–46. [LH] pologicalTheory12(1):101–11. [AR]
Phillips-Silver,J.&Trainor,L.J.(2008)Vestibularinfluenceonauditorymetrical Roepstorff,A.,Niewohner,J.&Beck,S.(2010)Enculturingbrainsthroughpat-
interpretation.BrainandCognition67:94–102. [RSS] ternedpractices.NeuralNetworks23(8–9):1051–59. [arAC,AR]
Piaget,J.(1952)Theoriginsofintelligenceinchildren.InternationalUniversity Rorty,R.(1979)Philosophyandthemirrorofnature.PrincetonUniversityPress.
Press. [PK] [MLA]
Pickering,M.J.&Garrod,S.(2007)Dopeopleuselanguageproductiontomake Ross,D.,Sharp,C.,Vuchinich,R.&Spurrett,D.(2008)Midbrainmutiny:The
predictionsduringcomprehension?TrendsinCognitiveSciences(11):105– picoeconomicsandneuroeconomicsofdisorderedgambling.MITPress.
110. [arAC] [DRo]
Platt,M.&Glimcher,P.(1999)Neuralcorrelatesofdecisionvariablesinparietal Ross,H.E.(1969)Whenisaweightnotillusory?TheQuarterlyJournalofExper-
cortex.Nature400:233–38. [DRo] imentalPsychology21(4):346–55.doi:10.1080/14640746908400230. [GB]
Ploghaus,A.,Tracey,I.,Gati,J.S.,Clare,S.,Menon,R.S.,Matthews,P.M.& Rowlands,M.(1999)Thebodyinmind:Understandingcognitiveprocesses.Cam-
Rawlins,J.N.(1999)Dissociatingpainfromitsanticipationinthehumanbrain. bridgeUniversityPress. [aAC]
Science284(5422):1979–81. [AKS] Rowlands,M(2006)Bodylanguage:Representinginaction.MITPress. [aAC]
Posner,M.(1980)Orientingofattention.QuarterlyJournalofExperimentalPsy- Rumelhart,D.E.,McClelland,J.L.&thePDPResearchGroup(1986)Parallel
chology32:33. [rAC] distributedprocessing,vol.I:Explorationsinthemicrostructureofcognition.
Pouget,A.,Dayan,P.&Zemel,R.(2003)Inferenceandcomputationwithpopu- Foundations.MITPress. [aAC]
lationcodes.AnnualReviewofNeuroscience26:381–410. [aAC] Rust,N.C.,Schwartz,O.,Movshon,J.A.&Simoncelli,E.P.(2005)Spatiotemporal
Powers,W.T.(1973)Behavior,thecontrolofperception.AldinedeGruyter. [AS] elementsofMacaqueV1receptivefields.Neuron46:945–56. [TT]
Pribram,K.H.(1971)Languagesofthebrain.Prentice-Hall. [BB] Sachs,E.(1967)Dissociationoflearninginratsanditssimilaritiestodissociative
Pribram,K.H.(1980)Theorientingreaction:Keytobrainrepresentationalmech- statesinman.In:Comparativepsychopathology:Animalandhuman,ed.J.
anisms.In:Theorientingreflexinhumans,ed.H.D.Kimmel,pp.3–20. Zubin&H.Hunt,pp.249–304.GruneandStratton. [aAC]
Erlbaum. [aAC] Sadakata,M.,Desain,P.&Honing,H.(2006)TheBayesianwaytorelaterhythm
Prinz,J.J.(2005)Aneurofunctionaltheoryofconsciousness.In:Cognitionandthe perceptionandproduction.MusicPerception23:269–88. [RSS]
brain:Philosophyandneurosciencemovement,ed.A.Brook&K.Akins,pp. Salakhutdinov,R.&Hinton,G.E.(2009)DeepBoltzmannmachines.Proceedingsof
381–96.CambridgeUniversityPress. [aAC] the12thInternationalConferenceonArtificialIntelligenceandStatistics
Proulx,T.,Inzlicht,M.&Harmon-Jones,E.(2012)Understandingallinconsistency (AISTATS),vol.5,ed.D.vanDyk&M.Welling,pp.448–55.TheJournalof
compensationasapalliativeresponsetoviolatedexpectations.TrendsinCog- MachineLearningResearch,publishedonline,athttp://jmlr.csail.mit.edu/
nitiveSciences16(5):285–91. [JBH] proceedings/papers/v5/ [rAC]
Purves,D.&Lotto,R.B.(2003)Whyweseewhatwedo:Anempiricaltheoryof Sanders,L.L.,Muckli,L.,deMillas,W.,Lautenschlager,M.,Heinz,A.,Kathmann,
vision.Sinauer. [aAC] N.&Sterzer,P.(2012)Detectionofvisualeventsalongtheapparentmotion
Quine,W.V.O.(1951)Twodogmasofempiricism.ThePhilosophicalReview60:20– traceinpatientswithparanoidschizophrenia.PsychiatryResearch.[Epub
43. [MLA] aheadofprint:April28,2012].Availableat:http://dx.doi.org/10.1016/
Rammsayer,T.(1999)Neuropharmacologicalevidencefordifferenttimingmech- j.psychres.2012.03.006. [LM]
anismsinhumans.TheQuarterlyJournalofExperimentalPsychology,Section Santhouse,A.M.,Howard,R.J.&ffytche,D.H.(2000)Visualhallucinatorysyn-
B:ComparativeandPhysiologicalPsychology52:273–86. [LH] dromesandtheanatomyofthevisualbrain.Brain123:2055–64. [SMS]
Rao,R.P.N.&Ballard,D.H.(1999)Predictivecodinginthevisualcortex:A Sarbin,T.R.(1986)Narrativepsychology:Thestoriednatureofhumanconduct.
functionalinterpretationofsomeextra-classicalreceptive-fieldeffects.Nature Praeger/Greenwood. [JBH]
Neuroscience2(1):79–87. [aAC,TE,KF,LM,MWS] Sass,L.(1992)Madnessandmodernism.Insanityinthelightofmodernart,lit-
Rao,R.P.N.&Sejnowski,T.J.(2002)Predictivecoding,corticalfeedback,and eratureandthought.BasicBooks. [SMS]
spike-timingdependentplasticity.In:Probabilisticmodelsofthebrain:Per- Saxe,A.,Bhand,M.,Mudur,R.,Suresh,B.&Ng,A.(2011)Modelingcortical
ceptionandneuralfunction,ed.R.P.N.Rao,B.A.Olshausen&M.S.Lewicki, representationalplasticitywithunsupervisedfeaturelearning.Posterpresented
pp.297–315.MITPress. [aAC] atCOSYNE2011,SaltLakeCity,Utah,February24–27,2011.Availableat:
Rauss,K.,Schwartz,S.&Pourtois,G.(2011)Top-downeffectsonearlyvisual http://www.stanford.edu/~asaxe/papers. [TT]
processinginhumans:Apredictivecodingframework.NeuroscienceandBio- Schachter,S.&Singer,J.E.(1962)Cognitive,social,andphysiologicaldeterminants
behavioralReviews35(5):1237–53. [aAC] ofemotionalstate.PsychologicalReview69:379–99. [AKS]
Read,J.,Perry,B.D.,Moskowitz,A.&Connolly,J.(2001)Thecontributionofearly Schaefer,R.S.,Vlek,R.J.&Desain,P.(2011a)Decomposingrhythmprocessing:
traumaticeventstoschizophreniainsomepatients:Atraumagenicneurode- Electroencephalographyofperceivedandself-imposedrhythmicpatterns.
velopmentalmodel.Psychiatry64:319–45. [SMS] PsychologicalResearch75(2):95–106. [RSS]
Read,J.,vanOs,J.,Morrison,A.P.&Ross,C.A.(2005)Childhoodtrauma,psy- Schaefer,R.S.,Vlek,R.J.&Desain,P.(2011b)Musicperceptionandimageryin
chosisandschizophrenia:Aliteraturereviewwiththeoreticalandclinical EEG:Alphabandeffectsoftaskandstimulus.InternationalJournalforPsy-
implications.ActaPsychiatricaScandinavica112:330–50. [SMS] chophysiology82(3):254–59. [RSS]
Reddy,L.,Tsuchiya,N.&Serre,T.(2010)Readingthemind’seye:decoding Schank,R.&Abelson,R.(1977)Scripts,plans,goalsandunderstanding:Aninquiry
categoryinformationduringmentalimagery.NeuroImage50(2):818–25. intohumanknowledgestructures.Erlbaum. [JBH]
[aAC] Schenk,T.&McIntosh,R.(2010)Dowehaveindependentvisualstreamsfor
Reich,L.,Szwed,M.,Cohen,L.&Amedi,A.(2011)Aventralstreamreadingcenter perceptionandaction?CognitiveNeuroscience1:52–78. [rAC]
independentofvisualexperience.CurrentBiology21:363–68. [aAC] Schultz,W.,Dayan,P.&Montague,P.R.(1997)Aneuralsubstrateofprediction
Reichert,D.,Seriès,P.&Storkey,A.(2010)HallucinationsinCharlesBonnet andreward.Science275:1593–99. [DRo]
Syndromeinducedbyhomeostasis:ADeepBoltzmannMachinemodel. Schwartz,O.,Hsu,A.&Dayan,P.(2007)SpaceandtimeinvisualcontextNature
AdvancesinNeuralInformationProcessingSystems23:2020–28. [rAC] ReviewsNeuroscience8:522–35. [aAC]
Repp,B.(1999)Detectingdeviationsfrommetronomictiminginmusic:Effectsof Segall,M.H.,Campbell,D.T.&Herskovits,M.J.(1963)Culturaldifferencesinthe
perceptualstructureonthementaltimekeeper.PerceptionandPsychophysics perceptionofgeometricillusions.Science139(3556):769–71. [PK]
61(3):529–48. [RSS] Sellars,W.(1962)Philosophyandthescientificimageofman.In:Frontiersof
Rescorla,M.(inpress)Bayesianperceptualpsychologytoappear.In:Oxford ScienceandPhilosophy,ed.R.G.Colodny,pp.35–78.UniversityofPittsburgh
handbookofthephilosophyofperception,ed.M.Matthen.OxfordUniversity Press. [Reprintedin:Science,PerceptionandRealitybyW.Sellars(1963,
Press. [aAC] Routledge&KeganPaul)]. [aAC,DCD]
BEHAVIORALANDBRAINSCIENCES(2013)36:3 251
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictivebrains,situated agents,and thefutureof cognitive science
Sellars,W.(1963)Science,perception,andreality.Routledge&KeganPaul. Sloman,A.(2011b)What’svisionfor,andhowdoesitwork?FromMarr(andearlier)
[JBH] toGibsonandbeyond.(Onlinetutorialpresentation,September2011.Available
Seth,A.K.,Suzuki,K.&Critchley,H.D.(2011)Aninteroceptivepredictivecoding at:http://www.slideshare.net/asloman/). [AS]
modelofconsciouspresence.FrontiersinPsychology2:395. [rAC,AKS] Sloman,A.(2012)Paper4:Virtualmachineryandevolutionofmind(Part3).Meta-
Shams,L.,Ma,W.J.&Beierholm,U.(2005)Sound-inducedflashillusionasan morphogenesis:Evolutionofinformation-processingmachinery.In:Alan
optimalpercept.NeuroReport16(10):1107–10. [aAC] Turing–hisworkandimpact,ed.S.B.Cooper&J.vanLeeuwen.Elsevier.
Shi,YunQ.&Sun,H.(1999)Imageandvideocompressionformultimediaengin- [AS]
eering:Fundamentals,algorithms,andstandards.CRCPress. [aAC] Smith,F.W.&Muckli,L.(2010)Nonstimulatedearlyvisualareascarryinformation
Silverstein,S.M.,Berten,S.,Essex,B.,Kovács,I.,Susmaras,T.&Little,D.M. aboutsurroundingcontext.ProceedingsoftheNationalAcademyofSciences
(2009)AnfMRIexaminationofvisualintegrationinschizophrenia.Journalof USA16:20099–103. [aAC,LM]
IntegrativeNeuroscience8:175–202. [SMS] Smith,L.&Gasser,M.(2005)Thedevelopmentofembodiedcognition:Sixlessons
Silverstein,S.M.&Keane,B.P.(2011)Perceptualorganizationimpairmentin frombabies.ArtificialLife11(1):13–30. [aAC]
schizophreniaandassociatedbrainmechanisms:Reviewofresearchfrom2005 Smith,P.L.&Ratcliff,R.(2004)Psychologyandneurobiologyofsimpledecisions.
to2010.SchizophreniaBulletin37:690–99. [SMS] TrendsinNeuroscience27:161–68. [aAC]
Simoncelli,E.P.&Olshausen,B.A.(2001)Naturalimagestatisticsandneural Sokolov,E.N.(1960)Neuronalmodelsandtheorientingreflex.In:Thecentral
representation.AnnualReviewofNeuroscience24:1193–216. [PK] nervoussystemandbehavior,ed.M.Brazier,pp.187–276.JosiahMacyJr.
Simons,J.S.,Schölvinck,M.L.,Gilbert,S.J.,Frith,C.D.,&Burgess,P.W.(2006) Foundation. [BB,aAC]
Differentialcomponentsofprospectivememory?EvidencefromfMRI. Sporns,O.(2007)Whatneuro-roboticmodelscanteachusaboutneuralandcog-
Neuropsychologia4:1388–97. [LH] nitivedevelopment.In:Neuroconstructivism:Perspectivesandprospects,Vol.
Singer,T.,Critchley,H.D.&Preuschoff,K.(2009)Acommonroleofinsulainfeelings, 2,ed.D.Mareschal,S.Sirois,G.Westermann&M.H.Johnson,pp.179–204.
empathyanduncertainty.TrendsinCognitionScience13(8):334–40. [AKS] OxfordUniversityPress. [aAC]
Singer,W.(1995)Developmentandplasticityofcorticalprocessingarchitectures. Spratling,M.W.(2008a)Predictivecodingasamodelofbiasedcompetitioninvisual
Science270:758–64. [SMS] attention.VisionResearch48(12):1391–408. [aAC,WAP,MWS]
Sloman,A.(1971)InteractionsbetweenphilosophyandAI:Theroleofintuitionand Spratling,M.W.(2008b)Reconcilingpredictivecodingandbiasedcompetition
non-logicalreasoninginintelligence.In:Proceedingsofthe2ndIJCAI[Inter- modelsofcorticalfunction.FrontiersinComputationalNeuroscience
nationalJointConferenceonArtificialIntelligence],ed.D.C.Cooper,pp.209– 2(4):1–8. [LM,MWS]
26.WilliamKaufmann.Availableat:http://www.cs.bham.ac.uk/research/cogaff/ Spratling,M.W.(2010)Predictivecodingasamodelofresponsepropertiesin
04.html#200407. [AS] corticalareaV1.JournalofNeuroscience30(9):3531–543. [MWS]
Sloman,A.(1978)Thecomputerrevolutioninphilosophy.HarvesterPress/Huma- Spratling,M.W.(2011)Asinglefunctionalmodelaccountsforthedistinctproperties
nitiesPress. [AS] ofsuppressionincorticalareaV1.VisionResearch51(6):563–76. [MWS]
Sloman,A.(1979)Theprimacyofnon-communicativelanguage.In:Theanalysisof Spratling,M.W.(2012a)PredictivecodingaccountsforV1responseproperties
meaning:Informatics5,ProceedingsASLIB/BCSConference,Oxford,March recordedusingreversecorrelation.BiologicalCybernetics106(1):37–49.
1979,ed.M.MacCafferty&K.Gray,pp.1–15.Aslib.Availableat:http://www. [MWS]
cs.bham.ac.uk/research/projects/cogaff/81-95.html#43. [AS] Spratling,M.W.(2012b)Unsupervisedlearningofgenerativeanddiscriminative
Sloman,A.(1982)Imageinterpretation:Thewayahead?In:Physicalandbiological weightsencodingelementaryimagecomponentsinapredictivecodingmodel
processingofimages(ProceedingsofanInternationalSymposiumorganisedby ofcorticalfunction.NeuralComputation24(1):60–103. [MWS]
TheRankPrizeFunds,London,1982),ed.O.Braddick&A.Sleigh,pp.380– Srinivasan,M.V.,Laughlin,S.B.&DubsA.(1982)Predictivecoding:Afreshview
401.Springer-Verlag.Availableat:http://www.cs.bham.ac.uk/research/projects/ ofinhibitionintheretina.ProceedingsoftheRoyalSocietyofLondon,B
cogaff/06.html#0604. [AS] 216:427–59. [aAC]
Sloman,A.(1987)Referencewithoutcausallinks.In:Advancesinartificialintelli- StaumCasasanto,L.(2008)Doessocialinformationinfluencesentenceprocessing?
gence,vol.2,ed.J.B.H.duBoulay,D.Hogg,&L.Steels,pp.369–81.North- In:Proceedingsofthe30thAnnualConferenceoftheCognitiveScienceSociety,
Holland.Availableat:http://www.cs.bham.ac.uk/research/projects/cogaff/81-95. ed.B.C.Love,K.McRae,&V.M.Sloutsky,pp.799–804.CognitiveScience
html#5. [AS] Society. [TAF]
Sloman,A.(1989)Ondesigningavisualsystem(towardsaGibsoniancomputational Stephan,K.,Friston,K.&Frith,C.(2009)Dysconnectioninschizophrenia:From
modelofvision).JournalofExperimentalandTheoreticalAI1(4):289–37. abnormalsynapticplasticitytofailuresofself-monitoring.SchizophreniaBul-
Availableat:http://www.cs.bham.ac.uk/research/projects/cogaff/81-95. letin35(3):509–27. [rAC]
html#7. [AS] Sterelny,K.(2003)Thoughtinahostileworld:Theevolutionofhumancognition,
Sloman,A.(1990)Mustintelligentsystemsbescruffy?In:Evolvingknowledgein Blackwell. [aAC]
naturalscienceandartificialintelligence,ed.J.E.Tiles,G.T.McKee&G.C. Sterelny,K.(2007)Socialintelligence,humanintelligenceandnicheconstruction.
Dean.Pitman. [aAC] PhilosophicalTransactionsoftheRoyalSocietyofLondon,SeriesB:Biological
Sloman,A.(1993)Themindasacontrolsystem.In:Philosophyandthecognitive Sciences362(1480):719–30. [aAC]
sciences,ed.C.Hookway&D.Peterson,pp.69–110.CambridgeUniversity Still,S.(2009)Information-theoreticapproachtointeractivelearning.Europhysics
Press.Availableat:http://www.cs.bham.ac.uk/research/projects/cogaff/81-95. Letters85:28005. [DYL]
html#18. [AS] Störmer,V.,McDonald,J.&Hillyard,S.A.(2009)Cross-modalcueingofattention
Sloman,A.(1996)Actualpossibilities.In:Principlesofknowledgerepresentationand altersappearanceandearlycorticalprocessingofvisualstimuli.Proceedingsof
reasoning:Proceedingsofthe5thInternationalConference(KR’96),ed.L. theNationalAcademyofSciencesUSA106(52):22456–61. [NB]
Aiello&S.Shapiro,pp.627–38.MorganKaufmann. [AS] Stotz,K.(2010)Humannatureandcognitive–developmentalnicheconstruction.
Sloman,A.(2002)Diagramsinthemind.In:Diagrammaticrepresentationand PhenomenologyandtheCognitiveSciences9(4):483–501. [aAC]
reasoning,ed.M.Anderson,B.Meyer&P.Olivier,pp.7–28.Springer- Summerfield,C.&Egner,T(2009)Expectation(andattention)invisualcognition.
Verlag. [AS] TrendsinCognitionScience13:403–409. [aAC,TE]
Sloman,A.(2006)Requirementsforafullydeliberativearchitecture(orcomponent Summerfield,C.,Egner,T.,Greene,M.,Koechlin,E.,Mangels,J.&Hirsch,J
ofanarchitecture).ResearchNoteNo.COSY-DP-0604,May2006.Schoolof (2006)Predictivecodesforforthcomingperceptioninthefrontalcortex.
ComputerScience,UniversityofBirmingham,UK. [AS] Science314:1311–14. [TE]
Sloman,A.(2008)Amulti-picturechallengefortheoriesofvision.ResearchNote Summerfield,C.&Koechlin,E.(2008)Aneuralrepresentationofpriorinformation
No.COSY-PR-0801.SchoolofComputerScience,UniversityofBirmingham, duringperceptualinference.Neuron59:336–47. [TE]
UK. [AS] Summerfield,C.,Trittschuh,E.H.,Monti,J.M.,Mesulam,M.M.&Egner,T.
Sloman,A.(2009)Somerequirementsforhuman-likerobots:Whytherecentover- (2008)Neuralrepetitionsuppressionreflectsfulfilledperceptualexpectations.
emphasisonembodimenthasheldupprogress.In:Creatingbrain-like NatureNeuroscience11(9):1004–1006. [aAC,TE]
intelligence,ed.B.Sendhoff,E.Koerner,O.Sporns,H.Ritter&K.Doya, Summerfield,C.,Wyart,V.,Johnen,V.M.&DeGardelle,V(2011)Humanscalp
pp.248–77.Springer-Verlag. [AS] electroencephalographyrevealsthatrepetitionsuppressionvariedwithexpec-
Sloman,A.(2010)Iflearningmathsrequiresateacher,wheredidthefirstteachers tation.FrontiersinHumanNeuroscience5:67.(Onlinepublication).
comefrom?In:ProceedingsoftheInternationalSymposiumonMathematical doi:10.3389/fnhum.2011.00067. [TE]
PracticeandCognition,AISB2010Convention,DeMontfortUniversity,Lei- Switkes,E.,Mayer,M.J.&Sloan,J.A.(1978)Spatialfrequencyanalysisofthevisual
cester,ed.A.Pease,M.Guhe&A.Smaill,pp.30–39.AISB(Societyforthe environment:Anisotropyandthecarpenteredenvironmenthypothesis.Vision
StudyofArtificialIntelliegenceandSimulationofBehaviour). [AS] Research18:1393–99. [BB]
Sloman,A.(2011a)Varietiesofmeta-cognitioninnaturalandartificialsystems.In: Synofzik,M.,Thier,P.,Leube,D.T.,Schlotterbeck,P.&Lindner,A.(2010)Mis-
Metareasoning:Thinkingaboutthinking,ed.M.T.Cox&A.Raja,pp.307–23. attributionsofagencyinschizophreniaarebasedonimprecisepredictionsabout
MITPress. [AS] thesensoryconsequencesofone’sactions.Brain133(Pt.1):262–71. [AKS]
252 BEHAVIORALANDBRAINSCIENCES(2013)36:3
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::

References/Andy Clark: Predictive brains, situated agents, and thefuture ofcognitivescience
Tanaka,K.(1996)Inferotemporalcortexandobjectvision.AnnualReviewof Vilares,I.&Körding,K.(2011)Bayesianmodels:Thestructureoftheworld,
Neuroscience19:109–39. [PK] uncertainty,behavior,andthebrain.AnnalsoftheNewYorkAcademyof
Tanenhaus,M.K.&Hare,M.(2007)Phonologicaltypicalityandsentenceproces- Science1224:22–39. [aAC]
sing.TrendsinCognitiveScience11:93–95. [TAF] Villalon-Turrubiates,I.E.,Andrade-Lucio,J.A.&Ibarra-Manzano,O.G.(2004)
Temperley,D.(2004)Communicativepressureandtheevolutionofmusicalstyles. MultidimensionaldigitalsignalestimationusingKalman’stheoryforcomputer-
MusicPerception21:313–37. [RSS] aidedapplications.In:ProceedingsoftheInternationalConferenceonCom-
Temperley,D.(2007)Musicandprobability.TheMITPress. [RSS] puting,Communications,andControlTechnologies,Austin,Texas,August
Thelen,E.&Smith,L.(1994)Adynamicsystemsapproachtothedevelopmentof 14–17,2004(CCCTProceedings,Vol.7),ed.H.-W.Chu,pp.48–53.University
cognitionandaction.MITPress. [aAC] ofTexasPress. [DRa]
Thompson,E.(2007)Mindinlife:Biology,phenomenology,andthesciencesof Vinje,W.E.&GallantJ.L.(2000)Sparsecodinganddecorrelationinprimaryvisual
mind.HarvardUniversityPress. [aAC] cortexduringnaturalvision.Science287:1273–76. [TT]
Tishby,N.,Pereira,F.C.&Bialek,W.(1999)Theinformationbottleneckmethod. vonderMalsburg,C.,Phillips,W.A.&Singer,W.,eds.(2010)StrungmannForum
In:Proceedingsofthe37thAllertonConferenceonCommunication,Control, Report,Vol.5.Dynamiccoordinationinthebrain:Fromneuronstomind.MIT
andComputing,ed.B.Hajek&R.S.Sreenivas,pp.368–77.Universityof Press. [rAC,WAP]
IllinoisPress. [DYL] vonUexküll,J.(1934/1957)Astrollthroughtheworldsofanimalsandmen:Apicture
Todorov,E.(2004)Optimalityprinciplesinsensorimotorcontrol.NatureNeuro- bookofinvisibleworlds.In:Instinctivebehavior:Thedevelopmentofamodern
science7(9):907–15. [NS] concept,ed.&trans.C.H.Schiller.InternationalUniversitiesPress(1957).
Todorov,E.(2006)Optimalcontroltheory.In:Bayesianbrain,ed.K.Doya,pp. [DCD]
269–98.MITPress. [NS] VuustP.&Frith,C.D.(2008)Anticipationisthekeytounderstandingmusicandthe
Todorov,E.(2009)Parallelsbetweensensoryandmotorinformationprocessing.In: effectsofmusiconemotion.BehavioralandBrainSciences31:599–600.
Thecognitiveneurosciences,4thedition,ed.M.Gazzaniga,pp.613–24.MIT [RSS]
Press. [aAC] Wacongne,C.,Changeux,J.P.&Dehaene,S.(2012)Aneuronalmodelofpredictive
Todorov,E.&Jordan,M.I.(2002)Optimalfeedbackcontrolasatheoryofmotor codingaccountingforthemismatchnegativity.JournalofNeuroscience
coordination.NatureNeuroscience5(11):1226–35. [aAC,NS] 32:3665–78. [TE]
Todorovic,A.,vanEde,F.,Maris,E.&deLange,F.P.(2011)Priorexpectation Waelti,P.,Dickinson,A.&Schultz,W.(2001)Dopamineresponsescomplywith
mediatesneuraladaptationtorepeatedsoundsintheauditorycortex:AnMEG basicassumptionsofformallearningtheory.Nature412:43–48. [aAC]
study.JournalofNeuroscience31:9118–23. [TE] Waydo,S.,Kraskov,A.,Quiroga,R.Q.,Fried,I.&Koch,C.(2006)Sparserep-
Tong,F.,Meng,M.&Blake,R.(2006)Neuralbasesofbinocularrivalry.Trendsin resentationinthehumanmedialtemporallobe.JournalofNeuroscience
CognitiveSciences10:502–11. [MLA] 26:10232–34. [TT]
Toussaint,M.(2009)Probabilisticinferenceasamodelofplannedbehavior.Küns- WeberJ.(2002)Thejudgementoftheeye.Themetamorphosesofgeometry–oneof
tlicheIntelligenz3:23–29. [aAC] thesourcesofvisualperceptionandconsciousness(afurtherdevelopmentof
Townsend,B.R.,Paninski,L.&Lemon,R.N.(2006)Linearencodingofmuscle Gestaltpsychology).Springer. [SMS]
activityinprimarymotorcortexandcerebellum.JournalofNeurophysiology96 Weiss,Y.,Simoncelli,E.P.&Adelson,E.H.(2002)Motionillusionsasoptimal
(5):2578–92. [DRa] percepts.NatureNeuroscience5(6):598–604.doi:10.1038/nn858. [aAC,GB]
Trehub,A.(1991)Thecognitivebrain.MITPress.Availableat:http://www.people. Wells, J. B., Christiansen, M. H., Race, D. S., Acheson, D. J. & MacDonald,
umass.edu/trehub/. [AS] M. C. (2009) Experience and sentence comprehension: Statistical learning
Tribus,M.(1961)Thermodynamicsandthermostatics:Anintroductiontoenergy, and relative clause comprehension. Cognitive Psychology 58:250–71.
informationandstatesofmatter,withengineeringapplications.D.VanNos- [TAF]
trand. [aAC,KF] Wheeler,M.(2005)Reconstructingthecognitiveworld.MITPress. [aAC]
Tudusciuc,O.&Nieder,A.(2009)Contributionsofprimateprefrontalandposterior Wheeler,M.&Clark,A.(2009)Culture,embodimentandgenes:Unravellingthe
parietalcorticestolengthandnumerosityrepresentation.JournalofNeuro- triplehelix.PhilosophicalTransactionsoftheRoyalSocietyofLondon,B363
physiology101(6):2984–94. [DRa] (1509):3563–75. [aAC]
Turing,A.M.(1952)Thechemicalbasisofmorphogenesis.PhilosophicalTrans- Wilson,R.A.(1994)Widecomputationalism.Mind103:351–72. [aAC]
actionsofRoyalSocietyofLondonB237:37–72. [AS] Wilson,R.A.(2004)Boundariesofthemind:Theindividualinthefragilesciences–
Uhlhaas,P.J.&Mishara,A.L.(2007)Perceptualanomaliesinschizophrenia: cognition.CambridgeUniversityPress. [aAC]
Integratingphenomenologyandcognitiveneuroscience.SchizophreniaBulletin Womelsdorf,T.,Anton-Erxleben,K.,Pieper,F.&Treue,S.(2006)Dynamicshifts
33:142–56. [SMS] ofvisualreceptivefieldsincorticalareaMTbyspatialattention.Nature
Ungerleider,L.G.&Mishkin,M.(1982)Twocorticalvisualsystems.In:Analysisof Neuroscience9:1156–60. [NB]
visualbehavior,ed.D.Ingle,M.A.Goodale&R.J.Mansfield,pp.549–86. Wu,Z.(1985)MultidimensionalstatespacemodelKalmanfilteringwithapplications
MITPress. [KF] toimagerestoration.IEEETransactionsonAcoustics,Speech,andSignal
VanEssen,D.C.(2005)Corticocorticalandthalamocorticalinformationflowinthe Processing33:1576–92. [DRa]
primatevisualsystem.ProgressinBrainResearch149:173–85. [LM] Wyart,V.,Nobre.A.C.&Summerfield,C.(2012)Dissociablepriorinfluencesof
VanVoorhis,S.&Hillyard,S.A.(1977)Visualevokedpotentialsandselective signalprobabilityandrelevanceonvisualcontrastsensitivity.Proceedingsofthe
attentiontopointsinspace.PerceptionandPsychophysics22(1):54–62. [HB] NationalAcademyofSciencesUSA109:3593–98. [rAC,TE]
Varela,F.J.(1999)Thespeciouspresent:Aneurophenomenologyoftimecon- Wyss,R.,König,P.&Verschure,P.F.M.J.(2004)Involvingthemotorsystemin
sciousness.In:Naturalizingphenomenology:Issuesincontemporaryphenom- decisionmaking.ProceedingsoftheRoyalSocietyofLondon,B:Biological
enologyandcognitivescience,ed.J.Petitot,F.J.Varela,B.Pachoud&J.-M. Sciences271(Suppl.3):S50–52. [PK]
Roy,pp.266–317.StanfordUniversityPress. [TF] Yeshurun,Y.&Carrasco,M.(1998)Attentionimprovesorimpairsvisualperform-
Varela,F.J.,Lachaux,J.-P.,Rodriguez,E.&Martinerie,J.(2001)Thebrainweb: ancebyenhancingspatialresolution.Nature396:72–75. [NB]
Phasesynchronizationandlarge-scaleintegration.NatureReviewsNeuro- Yu,A.J.(2007)Adaptivebehavior:HumansactasBayesianlearners.Current
science2:229–39. [TF] Biology17:R977–80. [aAC]
Varela,F.J.,Thompson,E.&Rosch,E.(1991)Theembodiedmind.MITPress. [aAC] Yuille,A.&Kersten,D.(2006)VisionasBayesianinference:Analysisbysynthesis?
Velleman,J.D.(1989)Practicalreflection.PrincetonUniversityPress. [aAC] TrendsinCognitiveScience10(7):301–308. [aAC,KF]
Verschure,P.,Voegtlin,T.&Douglas,R.(2003)Environmentallymediatedsynergy Zahedi,K.,Ay,N.&Der,R.(2010)Highercoordinationwithlesscontrol–a
betweenperceptionandbehaviourinmobilerobots.Nature425:620–24. [aAC] resultofinformationmaximizationinthesensorimotorloop.AdaptiveBehavior
Vetter,P.,Edwards,G.&Muckli,L.(2012)Transferofpredictivesignalsacross 18(3–4):338–55. [aAC]
saccades.FrontiersinPsychology3(176):1–10. [LM] Zhu,Q.&Bingham,G.P.(2011)Humanreadinesstothrow:Thesize-weightillusion
Vetter,P.,Grosbras,M.H.&Muckli,L.(underrevision)TMSoverV5disrupts isnotanillusionwhenpickingthebestobjectstothrow.EvolutionandHuman
motionpredictability. [LM] Behavior32(4):288–93. [rAC]
BEHAVIORALANDBRAINSCIENCES(2013)36:3 253
2(cid:30)(cid:30)(cid:27):(cid:10) /7(cid:22)(cid:2)7(cid:28)1 (cid:5)(cid:4)(cid:2)(cid:5)(cid:4)(cid:5)(cid:9) (cid:13)(cid:4)(cid:5)(cid:7)(cid:4)(cid:8)(cid:6)(cid:8)(cid:15)(cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:7)(cid:9)(cid:9)(cid:1)(cid:12)(cid:31).4(cid:22):20/(cid:1)7(cid:25)4(cid:22)(cid:25)0(cid:1).(cid:33)(cid:1)(cid:11)(cid:16)5.(cid:28)(cid:22)/10(cid:1)(cid:14)(cid:25)(cid:22)(cid:32)0(cid:28):(cid:22)(cid:30)(cid:33)(cid:1)(cid:12)(cid:28)0::
