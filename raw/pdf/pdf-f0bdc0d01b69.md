---
id: pdf-f0bdc0d01b69
type: pdf
title: FallbackPDF__f0bdc0d0
url: ''
authors: []
ingested_at: '2026-04-29T16:19:46Z'
content_hash: sha256:90290b44e452a3783d7f863f565de8b5f4af322bc92b36f684a935cb5626e55c
source_path: raw/pdf/pdf-f0bdc0d01b69.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 12
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__f0bdc0d0.pdf
published_at: '2025'
---
A quantum semantic framework for natural language processing
Christopher Agostino→
NPC Worldwide, Bloomington, Indiana 47403, USA
Quan Le Thien
Department of Physics, Indiana University, Bloomington, Indiana 47405, USA and
Quantum Science and Engineering Center (QSEC),
Indiana University, Bloomington, Indiana 47405, USA
Molly Apsel
Cognitive Science Program, Indiana University, Bloomington, Indiana 47405, USA and
Department of Psychological and Brain Sciences,
Indiana University, Bloomington, Indiana 47405, USA
Denizhan Pak
Cognitive Science Program, Indiana University, Bloomington, Indiana 47405, USA and
Luddy School of Informatics, Computing, and Engineering,
Indiana University, Bloomington, Indiana 47405, USA
Elina Lesyk
Independent Consultant, Munich 81549, Germany†
Ashabari Majumdar
Department of Physics, University of Notre Dame, Notre Dame, IN 46556, USA and
NPC Worldwide, Bloomington, Indiana 47403, USA
(Spontaneity Collaboration)
Semanticdegeneracyrepresentsafundamentalpropertyofnaturallanguagethatextendsbeyond
simplepolysemytoencompassthecombinatorialexplosionofpotentialinterpretationsthatemerges
as semantic expressions increase in complexity. Large Language Models (LLMs) and other modern
NLPsystemsfaceinherentlimitationspreciselybecausetheyoperatewithinnaturallanguageitself,
making them subject to the same interpretive constraints imposed by semantic degeneracy. In
this work, we argue using Kolmogorov complexity that as an expression’s complexity grows, the
likelihood of any interpreting agent (human or LLM-powered AI) recovering the single intended
meaningvanishes. Thiscomputationalintractabilitysuggeststheclassicalviewthatlinguisticforms
possess meaning in and of themselves is flawed. We alternatively posit that meaning is instead
actualized through an observer-dependent interpretive act. To test this, we conducted a semantic
Bell inequality test using diverse LLM agents as “computational cognitive systems” to interpret
ambiguouswordpairsundervariedcontextualsettings. Acrossseveralindependentexperiments,we
found average CHSH expectation values ranging from 1.2 to 2.8, with several runs yielding values
(e.g., 2.3-2.4) that significantly violate the classical boundary (S 2). This demonstrates that
| |→
linguistic interpretation under ambiguity can exhibit non-classical contextuality, consistent with
resultsfromhumancognitionexperiments. Theseresultsinherentlyimplythatclassicalfrequentist-
based analytical approaches for natural language are necessarily lossy. Instead, we propose that
Bayesian-style repeated sampling approaches can provide more practically useful and appropriate
characterizations of linguistic meaning in context.
I. INTRODUCTION were unmet in the 1960s and 1970s—that computers on
their own would never be capable of producing any kind
Prior to the deep-learning revolution of the 2010s, ofgeneralintelligenceorsimulatingthephenomenonthat
there was a prolonged AI winter spanning from the mid- is described as natural language. AI researchers that
1980s to the early 2000s. During this period, most re- tried often found themselves drowning in heuristics that
searchersinnaturallanguageprocessingandartificialin- brokedownwithedgecases,usuallyabandoningthetasks
telligence contended—based on the promises of AI that for more readily-solvable problems. See Dreyfus’ What
Computers Still Can’t Do [1] to better understand the
logical and semantic limitations of artificial reason per-
ceived by researchers prior to the successes of tools mak-
→ info@npcworldwi.de;http://www.cjagostino.com ing extensive use of large neural networks like Google
† info@elinalesyk.com Translate and others that followed (e.g., transformers,
5202
nuJ
11
]LC.sc[
1v77001.6052:viXra

2
large language models). Such large neural networks that • the agent’s background knowledge, cultural milieu
have now become commonplace for consumer products [33–35],
areoftentermedDistributionalSemanticModels(DSMs)
• transient psychological states [36] 1
[2–6]. DSMs, in e!ect, infer relevance and meaning from
statistical co-occurrences, and they have enabled a vari-
• the specific language being used, as di!erent lan-
etyofhighlypracticalnaturallanguageprocessing(NLP)
guages carve up semantic space di!erently [37].
applications including topic models, sentiment classifica-
tion, and large language models [7–10]. By construction, This profound context dependence implies that meaning
DSMslikeBERT-styletopicmodelspresupposethatdoc- is not merely decoded from the specific words in and of
uments possess singular, intrinsic semantic compositions themselves independently but that meaning is actively
[e.g., early bag-of-words models; see 2, for contrast with constructed or realized by an interpretive agent within
dynamic views]. a specific situation—[38–40]. The same expression pre-
BecauseofthepracticalsuccessesofDSMsinmanydo- sented to di!erent agents—or to the same agent under
mains,someresearchershaveforgottenornotconsidered di!erent conditions—can yield di!erent interpretations
many of the initial criticisms of artificial reason that to [41,42]. Critically,thishighlightstheobserver-dependent
thisdayremainsound, insteadassumingthattheselimi- nature of the actualization of semantic meaning through
tationstoowillbesolvedbymorecomputeormoredata. direct interpretation, providing a quantum mechanical
However, consider the following salient problems in the analog to an observable acting upon a state which we
current field of Natural Language Processing: will explore the implications of more thoroughly in Sec-
tionIII.Thiskindofco-creativeprocesshasbeenposited
1. DSM-powered approaches still exhibit limitations
to be mediated by a process called Relevance Realiza-
particularly when dealing with complex, ambigu-
tion(RR)—acorecognitivecapacityenablingindividuals
ous, or context-rich texts [11, 12].
to e"ciently navigate vast semantic spaces by employ-
ing context-sensitive attentional mechanisms to identify
2. The apparent lack of much progress seen in the
relevant information and filter out the irrelevant [43–
latest generation of frontier large language models
45]. Crucially, RR is non-algorithmic in the standard
(LLMs)—comparedtotheleapsseeninpriormodel
computational sense [45], and as such is more adept at
releases—appears to have revealed a fundamental
handling challenges like problem framing and indefinite
barrier in the reliability of semantic problem solv-
search spaces that are intractable for purely formal sys-
ing that more compute/data have not alleviated
tems operating in “small worlds” [46]. This embodied,
(e.g., GPT-4.5, Llama 4, Gemini 2.5, Claude 3.7
observer-dependent, and contextually situated view of
Sonnet). Likewise, many frontier researchers have
meaning construction challenges any notion of seman-
shifted away from prioritizing progress in LLMs
tic expressions possessing intrinsic, context- or observer-
in favor of more dynamically capable models (e.g.
independent meaning, aligning with dynamic models of
JEPA [13], MAMBA [14], CTM [15], or modifi-
semantic memory [22, 27, 38, 41, 47–50].
cations to LLMs that allow them to self-improve
The inherent uncertainties and deep context-
[16, 17]).
dependencies of this dynamic process suggest that
These issues and the evolving research landscape sug- classical probabilistic and logical frameworks are in-
gest that the challenges faced by DSM-based approaches su"cient. Consequently, researchers have turned to
may stem from a more fundamental issue in linguistics: non-classical frameworks—such as those employing
the problem of semantic degeneracy. This concept, ex- principles from quantum theory—to find more suit-
tending beyond simple polysemy, refers to the inherent able mathematical tools. Such approaches have been
multiplicity of potential interpretations that arise when adopted to model a wide range of cognitive phenomena,
processing complex linguistic expressions [18–20]. including concept combinations, decision-making, and
Indeed, the concept intuitively makes sense: empirical memory [51–57]. The utility of these quantum-inspired
observationrevealstoanyobserverthatnaturallanguage models is not merely theoretical but is demonstrated
meaning is not fixed or absolute [2, 21] and interpreta-
tion itself is radically context-dependent [22–24]. Thus,
anysemanticmeaningrealizedbyanagentinterpretinga
natural language expression depends crucially on a com- 1 WhilemanyconsiderLLMssimplystatisticalmachinesthatare
binatorially explosive set of potential factors. These fac- completelydisconnectedfromthematerialrealityofthephysical
world,itiscertainlypossiblethatrealworldphysicalvariations
tors include but are not limited to:
intheenvironmentthattheyinhabitorotherrandomphenomena
likecosmicrayscouldinducetransientstates. Additionally,when
• the surrounding sentential and discourse context
a model like Claude from Anthropic possesses knowledge of the
[25, 26]
timeoftheyear,itshavingaFrenchnameandthetrainingand
systempromptingofClaudereinforceaFrenchmindsetontothe
• the agent’s current attentional focus and task de- modeltothepointthatitsresponsepatternsandwillingnessto
mands which can selectively highlight specific con- putine!ortvarydependingonwhetherthetimeofyearcoincides
ceptual features, [27–32] withFrenchholidays.

3
in empirical studies. For instance, Aerts et al. [58] conceptualizeK(M(S ))astheminimumnumberofbits
E
identified quantum-like contextuality e!ects when ana- required to unambiguously specify the intended meaning
lyzing concept co-occurrence statistics for the “Pet-Fish M(S )ofagivensemanticexpressionS . Thisspecifica-
E E
problem” on the World-Wide Web, showing that mean- tion must capture not only the identities of the concepts
ing construction at this scale deviates from classical involved but also their precise contextual nuances and
probabilistic assumptions. In a similar vein, other work the intricate web of relationships binding them into a
has applied Bell’s [59] theorem to human cognition, un- coherentwhole. Forinstance,theKCofspecifyingasin-
covering non-classical correlations that violate classical gle, coherent interpretation of ‘I just went to the animal
bounds in both information retrieval judgments [60] and shelter and I brought a dog home’ is low, whereas for a
cognitive decision-making tasks [61–63]. passage from a work as complicated and inter-connected
More recent work provides a crucial conceptual re- as James Joyce’s Finnegans Wake e.g.,
finement by distinguishing between two types of contex-
And what sensitive coin I’d be possessed of
tual influence. In experiments on facial trait judgments,
atLatouche’s,begor,I’dsinkitsumtotal,ev-
Bruza et al. [64] delineate between context-sensitivity, a
ery dolly farting, in vestments of subdomi-
standard causal influence of context, and true contextu-
nal poteen at prime cost and I bait you my
ality. The latter is defined as an acausal form of con-
chancey oldcoat against the whole ounce you
text dependence where a property may be genuinely in-
half on your backboard (if madamaud strips
determinate prior to measurement. They argue that if a
mesdamines may cold strafe illglandsl) that
cognitive phenomenon is found to be contextual, the un-
I’m the gogetter that’d make it pay like cash
derlyingcognitivepropertiesdonotpossesswell-defined,
registers as sure as there’s a pot on a pole.
pre-existing values. Instead, the property is actualized
And, what with one man’s fish and a dozen
in the moment of judgment—a phenomenon that non-
men’spoissons,sowingmywildplumstoreap
classical models are uniquely equipped to formalize.
ripe plentihorns mead, lashings of erbole and
Given the state of a!airs, we aim in this work to ac-
hydromel and bragget, I’d come out with my
complish two primary tasks: (1) identify the combina-
magic fluke in close time, fair, free and frol-
torial problems that have stalled the apparent progress
icky,zoomingtopholeonthemartasafactor.
of frontier LLMs and (2) provide a practical path for-
ward for understanding and studying natural language the KC would be extraordinarily high to the extent that
using a non-classical framework. To this end, in Sec- the amount of constraints from context needed to dis-
tion II, we provide an information-theoretic exploration ambiguate the ‘intended meaning’ of the passage might
of the role of semantic degeneracy in single-turn prob- requireaprogramthatisordersofmagnitudelongerthan
lem solving tasks. Then, in Section III, we formulate a the original expression, reflecting the vast amount of in-
quantum semantic theoretical framework for the act of formation needed to resolve its multifaceted ambiguities
interpretation. Following this, we detail our experimen- into one particular reading.
tal methodology in Section IV to test whether natural Thus,theinformationalburden,K(M(S )),necessary
E
language interpretation mayexhibitnon-classicalbehav- to constrain interpretations to those closely aligned with
ior, leveraging LLMs as interpretative stand-ins. Section an author’s original intention, scales dramatically with
V presents our findings, and Section VI discusses their the number and interconnectedness of the concepts and
broader implications for the future of computational lin- relationships within an expression S . While the con-
E
guistics and our understanding of cognitive science. stituent concepts c form the foundation, each requires a
i
number of bits for contextual instantiation. This linear
relationship might be tractable on its own, but it is the
relationshipsr betweenconceptsthatcontributetoac-
II. KOLMOGOROV COMPLEXITY, SEMANTIC i,j
DEGENERACY, AND THE CHALLENGE OF tualizingtheintendedmeaning, andspecifyingtheinter-
INTERPRETATION relationalconstraintsrequiresspecifyinganO(N2 )
Concepts
numberofbitstohaveashotatdisambiguatingpotential
interpretations and reproducing the intended one. Be-
The concept of Kolmogorov complexity (KC) [65] pro-
cause of this, the KC for an expression can be written as
vides a powerful lens through which to understand the
an inequality with a lower bound based on the number
fundamental limitations of natural language interpreta-
tion, particularly pertinent with respect to LLMs which
N N
are expected to reliably solve problems for users. Kol- K(M(S )) c + c2 (1)
mogorov Complexity, K(s), of a string s is formally de- E → i · i,j
i i,j
! !
fined as the length of the shortest computer program (in
afixeduniversaldescriptionlanguage)thatproducessas As can be seen, K(M(S )) increases at least superlin-
E
output. WhileKCstrictlyappliestofinitestrings,itsun- early as the complexity of an expression increases. Each
derlying principle—the quantity of information required of the K(M(S )) bits represents an informational speci-
E
for minimal description—can be extended to the domain ficity or a semantic choice point (e.g., deciding to inter-
of semantics. For some semantic expression S We can pret‘bat’asananimalinsteadofawoodenstickusedfor
E

4
baseball)thataninterpretingagentmustsuccessfullyre-
construct. Crucially,ateachsuchdecisionpoint,thereis
apotentialopportunityfordegeneratesolutionsasmany
words have multiple meanings, and so we specify some
degeneracy per bit d (Note that this essentially serves
b
asanerrorrate,butweemployitinthiswaytomaintan
the conceptual notion). Consequently, the probability of
aninterpretercorrectlyactualizingall K(M(S ))bitsto
E
arrive at the precise intended meaning is the product of
the probabilities of getting each bit right,
1
K(M(SE))
1
P(perfect interpretation)= ( ) (2)
N! d
k=1
"
If we assume an average degeneracy per bit,
d¯
b
1 1
P(perfect interpretation) ( )K(M(SE)) (3)
↑ N! d¯
b
arelationshipwhichweillustrategraphicallyinFigure1. FIG. 1. Probability of perfect semantic interpretation versus
As K(M(S E )) grows in Figure 1, the probability of a the number of core semantic concepts (N concepts) in an ex-
perfect (or otherwise similar enough) interpretation di- pression, illustrating the impact of superlinear growth in se-
minishes exponentially, rapidly approaching zero for ex- manticcomplexity. Thetotalsemanticbits(K,shownonthe
pressions of moderate complexity. This result provides topx-axis)aremodeledasthesumofinformationrequiredfor
a clear demonstration of semantic degeneracy in action: individual concepts and their pairwise relationships, here as-
the combinatorial explosion of alternative, plausible in- suming c concept =5 bits per concept and c relationship =1 bit
per relationship. Di!erent curves represent varying average
terpretations surrounding any expression S . At this
point, it is worth mentioning that this situ
E
ation bears
probabilitiesoferrorperbit(p e). Thesuperlinearincreasein
K with N concepts leads to a dramatically faster exponential
an analogy to concepts in statistical mechanics, wherein
decrease in the probability of flawless interpretation, under-
S is like an ensemble of micro-states. An error in infer-
E scoringtheprofoundchallengeposedbysemanticdegeneracy
ring even one bit (a constraint on a degree of freedom) as inter-concept dependencies proliferate.
leadstoadi!erentmicrostate,and,withthehighdimen-
sionality (K(M(S ))), it becomes overwhelmingly prob-
E
ablethataninterpreterwillrarely, ifever, reproducethe
pression,butratheranemergentphenomenonactualized
specific set of micro-states (which we will argue in Sec-
through the dynamic interaction between the expression
tion III are themselves unknowable a priori) that make
and an interpretive agent situated within a specific con-
up the ensemble, resulting in high ‘semantic entropy’.
text. As described, this framework naturally challenges
This KC-based analysis highlights a fundamental limita-
theassumptionofrealismwhichhistoricallyaroseinclas-
tionforNLPsystemsandexplainsthepersistentdi"cul-
sicalphysics. Toformallymodelthisobserver-dependent
ties in LLM-assisted tasks requiring deep, unambiguous
andcontextualnatureofmeaning,weproposeaquantum
understanding or translation of semantically degenerate
semanticframeworkwhichmirrorsthedi!erencebetween
expressions: the LLM generates a plausible meaning—
quantum and classical physics. Semantic expressions are
oneofmanyaccessiblemicrostates—butalmostneverthe
separatedfromsyntaxandinsteadtreatedasobservables,
singularlyintended one. Thisresultonitsownhighlights
mirroring how physical measurement outcomes in quan-
the need to move beyond training artificially intelligent
tum systems are detached from the system as opposed
systems that prioritize single-shot response success and
to the realism as assumed in classical system. We hope
toprioritize research on alternative models thatcan suc-
that the processes of interpretation and meaning actual-
cessfullysimulatenaturallanguageinthewaythatLLMs
ization are elucidated clearer under this quantum logical
have while also being able to dynamically update and
structure.
adapt itself accordingly. It is our hope that these lessons
here coupled with the quantum semantic approach can We begin by positing that a semantic expression, de-
provide a clearer fundamental basis upon which future notedS ,doesnotpossessapre-defined,inherentmean-
E
methods and models can be trained, tested, and evalu- ing. Instead, it functions as a symbol that a!ords a
ated. spectrumofpossibleinterpretationswhenengagedbyan
agent. To represent this capacity for interaction, S is
E
associatedwithastatevector ω inacomplexHilbert
|
SE↓
III. A THEORY OF QUANTUM SEMANTICS space , the semantic state space. This vector is a lin-
S
H
ear superposition of basis states, ω = c e . A
| SE↓ i i | i ↓
The foundational premise of this work is that mean- crucial aspect of this proposal is that the basis states
#
ing is not an intrinsic, static property of a semantic ex- e themselvesarenotassumedtobeknownorfixeda
i
{| ↓}

5
ˆ
priori, nor are they necessarily interpretable as a univer- terpretive observable ち(t) and the semantic expression
sal set of predefined semantic primitives. Instead, they ω (t) are generally not static. While ち ˆ (t) as an ob-
may represent abstract dimensions of potential semantic |
SE
↓
servable can vary explicitly in time, ω (t) ’s dynamics
di!erentiation that only become operationally relevant |
SE
↓
can, inanalogytoquantummechanics, begovernedbya
or partially discernible through specific interpretive acts
semantic Schrödinger equation:
(measurements), where e is the set of eigenbasis of
i
{| ↓}
ˆ
an observable ち—here denoted by a Japanese character
ε
w
fo
h
rm
ich
in
i
g
s
t
p
h
r
e
on
m
ou
ea
n
s
c
u
e
r
d
em
‘m
e
o
n
’
t
—
, i.
a
e
s
.
p
i
o
n
s
t
i
e
t
r
e
p
d
re
b
t
y
in
t
g
he
th
a
e
ge
s
n
y
t
n
p
ta
e
x
r-
.
i⊋sem
εt |
ω
SE
(t)
↓
=Hˆ
sem
(t)
|
ω
SE
(t)
↓
(5)
The Hilbert space is thus a formal construct whose
H S wherethesemanticHamiltonian,Hˆ (t),generatesthis
basis is defined by the set of all possible ways an expres- sem
evolution, encapsulating drivers such as shifts in context
sion can be distinctively engaged with, rather than by a
C (t), sequential information processing from S , and
pre-enumerated list of fundamental meanings. The co- A E
e"cients c
i
are complex numbers (c
i
C), determined the agent’s internal cognitive dynamics. The constant
by how the semantic expression S ca ↔ n be decomposed ⊋sem sets the scale for these semantic dynamics where
E
as a superposition of the semantic bases e i . While the quantum coherence between the bases | e ↓i is important.
squared moduli c 2 relate to probabiliti | es ↓ of outcomes This formalism allows for agents’ interpretive engage-
| i | ment evolution. The dependence of Hˆ (t) on t allows
upon measurement with respect to a chosen observable, sem
for modeling changes in this evolution as the agent nav-
the complex phase of these coe"cients holds additional
igates di!erent semantic loci. In this work, however, we
information with no direct analogue in classical proba-
setasidethetimeevolutioncomponentofourframework
bilistic models, and so it is impossible to derive any ana-
andfocusmoreoncertifyingthequantumstatenatureof
logical particular meaning from these coe"cients as one
thesemanticexpressionS throughsamplingexploration
might consider weights in a language model. Indeed, the E
by way of a Semantic Bell Test, thus adapting a logic
complexnatureisfundamentalformodelingpotentialin-
that has previously been employed in cognitive psycho-
terference and entanglement e!ects in semantic process-
ing. Thefullinterpretivesignificanceofc isonlyrealized logical experiments to reveal non-classical contextuality
i
through the associated interpretive axis e set by an in human judgements across diverse domains, including
i
| ↓ decision-making, information retrieval, and assessments
agent, i.e. there is no notion of pre-existing and isolated
of concepts [60–63].
probabilities of meaning.
An agent A engages S through an interpretive ob-
E
ˆ
servable, ち (t), which is dynamically constituted from
A IV. EXPERIMENTAL DESIGN
its semantic memory (comprising goals, persona, knowl-
edge, attentional state) as activated by the current con-
text C (t). The act of interpretation to ascertain a spe- This section outlines the experimental methodology
A
cific semantic aspect is represented by applying a Her- designed to test for non-classical correlations in seman-
ˆ ticinterpretation,analogoustoaCHSH-typeBelltestin
mitian operator, denoted ち (t) to ω . This operator
A | SE↓ quantum physics [59, 66]. In particular, this experiment
ˆ
ち (t) embodies the specific semantic probe. The eigen-
A focuses on how Large Language Model (LLM) agents
ˆ
values { m i } ofち A (t)encompassallpossibleoutcomesof interpret ambiguous word pairs within simple sentence
agentA’ssemanticmeasurement,specificallytheyrepre- structures,undervaryingcontextual(persona-based)set-
sentallpossibledistinctinterpretationsactualizedbythe tings.
agent,eventhoughtheycannotbeexplicitlyenumerated.
The probability of actualizing interpretation m is thus
i
given by A. LLMs as observers
P(m )= c ω 2 = ω Pˆ ω (4)
i |↗ i | SE↓| ↗ SE| i | SE↓ In this work, LLM agents serve as the “observers” in
this semantic Bell test. To mitigate potential model-
where Pˆ = e e is the projection operator onto the
i i i specificbiasesandenhancetherobustnessofourfindings,
| ↓↗ |
eigenspaceofm . Thisinteractionisanalogoustoaquan-
i eachagentinstantiationisrandomlyselectedfromapre-
tum measurement.
defined pool of diverse, state-of-the-art foundation mod-
Withsuchformulation,semanticmeasurementsbydif- elsandproviders. Thispoolincludesmodelssuchasvari-
ferentagentscannowpossessnon-commutativity,similar ants of Gemini (e.g., ‘gemini-1.5-flash’, ‘gemini-2.0-flash-
toquantumobservables. Iftwodistinctinterpretiveoper- lite’, ‘gemini-2.0-flash’ ), Anthropic’s Claude series (e.g.,
ˆ ˆ ˆ ˆ
ations, ち and ち , do not commute, i.e. [ち ,ち ]=0, ‘claude-3-5-sonnet-latest’, ‘claude-3-5-haiku-latest’, and
1 2 1 2 ↘
then the semantic aspects they probe cannot generally ‘claude-3-7-sonnet-latest’), DeepSeek’s ‘deepseek-chat’,
possess simultaneous, definite, pre-existing values. as well as various models from OpenAI (e.g., ‘gpt-
The dynamics of meaning actualization extends to the 4o‘,‘gpt-4o-mini’,‘gpt-4.1-mini’,‘gpt-4.1-nano’,‘gpt-4.1-
timeevolutionoftheinterpretiveprocess. Theagent’sin- nano’). This approach aligns with recommendations for

6
multi-model triangulation to ensure fairness and gener- agents. The agents are then tasked with choosing a sin-
alizability of results [67–70] and to ensure that any po- gular, unambiguous meanings for each of the words in
tential correlations we find are not restricted only to a the pair. Stimuli are constructed by embedding ambigu-
single model’s weights. For each experimental trial, two ous word pairs (e.g., “trunk” with meanings ‘A’ for stor-
primary base personas, “Alice” and “Bob” are generated. age/treevs. “bow” withmeanings‘A’forshipfront/knot)
These personas are characterized by randomly assigned intosimplesentencetemplates(e.g.,“Theword1wasset-
attributes such as age (e.g., 25-70 years) and location tled near the word2”). Four distinct interpretive settings
(e.g., Bloomington, IN; Detroit, MI), which implicitly aredefinedforagentsAlice(A,A’)andBob(B,B’),cre-
defines their primary language (English, in this setup). ated by providing their base personas with additional,
These attributes inform the agent’s base semantic mem- distinct short textual prompts designed to prime seman-
ory profile for the trial. tically orthogonal di!erent contextual perspectives (e.g.,
It should be noted here that, paradoxically, while “You are a surgeon...” vs. “You are a bus driver...”).
LLMs exhibit limitations on complex tasks because For each of these four settings, the corresponding LLM
of semantic degeneracy, their internal mechanisms—– agentprovidesasingularsimultaneousinterpretationfor
specifically their attention architectures—function as a both ambiguous words. Alice and Bob are not shown
kind of black box which—like the brain—collapses the the definitions under consideration so as to avoid bias-
state of potential interpretations into a specific one that ing them or limiting the semantic search space, and so a
they use when responding to user inquiries. Although separate LLM call is required to then determine if each
the underlying mechanism is of course distinct from the interpretation aligns with predefined meaning ‘ϑ’ or ‘ϖ’,
biological and cognitive underpinnings of human linguis- triggeringare-interpretationifthechoiceisunclear(e.g.
tic interpretation, the similarity of the two ‘observing’ a if the two options for meaning for the word ‘chair’ are
specific state suggests that LLMs do indeed e!ectively ‘leader of a group’ or ‘furniture to sit on’ and the in-
reproduce this function of language understanding and terpretation says ‘furniture or leader’) or outside these
cognition. Thus, these models can serve as experimen- options (e.g. for the chair example if it decides the sen-
tal interpretative probes in natural language tasks. In tence is referring to an execution by ‘electric chair’, it
addition, it has also been demonstrated that LLMs can wouldbeconsideredoutsideofthedefinitionalscopeand
generate responses that can to first order mimic human are-interpretationiscarriedout).3 Theseclassifiedinter-
linguisticbehaviorinvariouscontexts(e.g. examplesur- pretations are mapped to numerical values (A +1, B
≃
veys [71–73]2 Kitadai et al. [71] also note the power of 1),yieldinga2-elementoutcomevectorforeachset-
≃⇐
personasinimprovingtheverisimilitudeoftheresponses, ting. Finally,theoutcomevectors(ち ˆ ,ち ˆ ,ち ˆ ,ち ˆ )
an important facet that we make use of as well. Thus, are normalized, and expectation valu A es E( A X → Y) B are c B a → l-
we argue, that one can and should use LLMs to probe culatedastheaveragedotproductofcorrespondingpairs
the statistical patterns of semantic interpretations under of (ϑ, ϖ), which are then used to compute the CHSH S-
diverse conditions (e.g. persona and context variations). value S = E(A,B) E(A,B ↑ )+E(A ↑ ,B)+E(A ↑ ,B ↑ ).
By observing how LLMs grapple with semantic ambigu- However, a critical ⇐ assumption in this standard CHSH
ityandcontext-dependentmeaning,wecangaininsights formulation is that of marginal consistency, also known
into the mechanisms of interpretation and the types of as ‘no-signaling’ [76, 77], which posits that the marginal
computational strategies that are more or less success- probabilityforoneagent’soutcomeisindependentofthe
ful in navigating tasks with high semantic degeneracy measurement setting of the other agent. As Dzhafarov
[74, 75]. et al. [76] have extensively discussed, this assumption is
often violated in cognitive and behavioral experiments.
Such violations, termed ‘inconsistent connectedness’ can
B. Bell Test complicate the interpretation of Bell-type inequalities.
Therefore, while a result of S > 2 suggests a violation
| |
of local realism, it must be interpreted with caution, as
The core of our semantic Bell test involves present-
the excess correlation could potentially arise from these
ing sentences containing two ambiguous words to LLM
direct contextual influences rather than true contextual-
ity.
All agent definitions and LLM response handling are
carried out using the open-source npcpy package4.
2 Thelastofthesereferences,Tjuatjaetal.[73],actuallydescribes
the performance of LLMs in this regard as poor as they note
they are subject to perturbations that humans in a similar sur-
vey would not be as strongly a!ected. We note here that their
findings here fit neatly within the framework of this work and 3 Itispossibletoimaginethisexperimentcanbecarriedoutwith
that, if one additionally considers the role of relevance realiza- word choice sets with more than 2 meanings, and we plan to
tionforthehumansubject(context-richbywayofphysicalem- explore that in future work as this would allow us to further
beddedness)versustheLLM(context-pooranddisembodied),it explorethequbit-stylelogicwemightconsiderinmorepractical
appearsclearthatthemain‘problem’withtheLLMresponsesin applications,butthatisoutsideofthescopeofthiswork.
theirexperimentwasduetoadrasticcontextualdisadvantage. 4 https://github.com/NPC-Worldwide/npcpy

7
Experiment N Trials |S|
1 5 2.8
2 5 1.2
3 10 2.0
4 10 2.44
5 20 2.32
6 20 2.0
7 50 2.33
8 200 1.83
TABLEI.Calculated S valuesfortheCHSHinequalityfrom
| |
di!erent experimental runs, with slight variations between
thepersonaconfigurations(age,location)aswellasthetotal
numberoftrials(N)perexperiment. Values S >2indicate
| |
a violation of the classical Bell-CHSH inequality.
V. RESULTS
In this short section, we highlight and discuss the re-
sults of our Semantic Bell test.
In our experimentation, we conducted 8 experiments
where we varied the number of trials in the individual
experiments from 5-200 and instantiated di!erent per-
FIG. 2. Example evolution of the calculated CHSH S-value
sona combinations, and we show the various S values
as the trial number progressed for an experiment run with
| |
for the experiments in Table I. For illustrative purposes, a total of 50 trials, eventually settling at 2.327 (Experiment
weshowinFigure2theevolutionofthe|S|value’sevolu- #7 from Table I). The dashed red line at S = 2 indicate
±
tion across trial number for experiment #7 with N =50 the classical bounds of the CHSH inequality and the dashed
trials. Tobeclear,thereisnotanyparticularmeaningto greenlineindicatestheproposedquantumboundatS=2↑2.
be derived from the variation in S as it progresses with
| |
trial number as the S value itself ought to be derived
| |
fromaninfinitenumberoftrials. Thisillustrationsimply ing observer-dependent meaning actualization, engages
serves as a visual aid to show the stabilization of the S withand o!ersalternatives toclassicaltheoriesofmean-
| |
value for a non-negligible number of trials. ing and interpretation (Section VIB). We will then con-
Importantly in these results, we find a rich variety of necttheseideastospecificcognitivephenomenaandpsy-
correlation structure ranging from classical behavior to cholinguisticfindings(SectionVIC),andfinally,consider
non-classical quantum logical. Theoretically, the upper thebroaderimplicationsforNLPresearch(SectionVID)
bound for quantum systems in the Bell experiment is and practical industrial applications (Section VIE).
S 2⇑2. It is interesting then that one of our experi-
| |⇒
ments(albeitN =5),the S valuereached2.8,providing
| |
anempiricalupperboundfortheseexperimentsthatcan
A. Semantic Degeneracy: Implications for DSMs
be consistent with quantum computational frameworks. and LLMs
Distributional Semantic Models, including contempo-
VI. DISCUSSION rary Large Language Models (LLMs), have achieved re-
markable success by learning statistical co-occurrences
The arguments presented in this work, concerning the from vast text corpora [2, 6, 7, 9]. These models implic-
fundamental limitations imposed by semantic degener- itlyoperateundertheassumptionthatsu"cientstatisti-
acy and the potential of a quantum semantic frame- cal exposure can lead to robust representations of mean-
work, o!er a new lens through which to re-evaluate sev- ing. However, the principle of semantic degeneracy, par-
eral core debates and prevailing methodologies in natu- ticularly when analyzed through Kolmogorov complex-
ral language processing and cognitive science. This dis- ity (KC) as detailed in Section II, reveals a fundamental
cussion will first address how the information-theoretic challengetothisassumptionfortasksdemandingprecise,
challenge of semantic degeneracy, as quantified by Kol- contextually-specific interpretations, as we have shown
mogorov complexity, impacts the capabilities of distri- that as the complexity of a semantic expression and its
butional semantic models (DSMs) and Large Language required contextual disambiguation increases, the KC of
Models (LLMs) in tasks requiring deep contextual un- specifying the singularly intended meaning grows super-
derstanding (Section VIA). Subsequently, we will ex- linearly. This implies that any DSM or LLM—trained
plore how a quantum semantic framework, emphasiz- on finite sets of data and with fixed weights—will more

8
likelythannotprovidesolutionsandinterpretationsthat interpretation [38, 41, 42, 47, 48, 82] is naturally accom-
are not aligned with the ‘intended’ one on some critical modated if meaning is not fixed but realized in interac-
aspects that results in a complete breakdown in under- tion. This quantum concept of ‘measurement contextu-
standing. These information-theoretic limits stem from ality’ aligns with models of dynamic semantic memory
the combinatorial explosion of potential interpretations [27, 49, 50], accounts of attentional focus [28–30], the
andcanadequatelyexplaintheobservedplateausinLLM non-algorithmicnatureofRelevanceRealization[45],and
performance on complex reasoning tasks and the persis- evencross-linguisticvariationsinsemanticcategorization
tent di"culties DSMs face with ambiguous or context- [33, 34, 37].
richtexts[11,12]despiteincreasingmodelsizeanddata. Thisnotionofmeasurementcontextualityfindsstrong
Indeed it appears that the limitations of DSMs at nav- empirical parallels in human judgment research. For in-
igating tasks with high ambiguity likely precludes them stance, work by Bruza et al. [55, 64] on facial judgments
from ever achieving the status of ‘strong’ AI. It appears extendscontextualitybeyondlanguagetoperception,ar-
likely that alternative methods or ensemble approaches guing that such properties are indeterminate and con-
(e.g. where LLMs are used as reasoning engines along structed in the moment of judgment. This reinforces our
with an alternative, more dynamic model) will prevail. core premise: if concrete perceptual traits are indetermi-
nate, thenabstractsemanticmeaningisevenmorelikely
to require an interpretive act to become actualized. Our
B. Quantum Semantics versus Classical Theories of experimentalfindingsprovidedirectquantitativesupport
Meaning for this view. The violation of the CHSH inequality we
observediscomparableinmagnitudetoresultsfromcog-
The limitations highlighted by semantic degeneracy nitive experiments with humans, such as the work by
motivate the exploration of alternative frameworks for Aerts et al. [62] on conceptual entanglement. This par-
meaning. Our proposed quantum semantic framework allel suggests that LLMs tap into the same non-classical
(Section III), which posits that meaning is not an in- probabilistic structures inherent in human semantic pro-
trinsic property of text but is actualized through an cessing.
observer-dependent interpretive act, directly confronts This convergence of findings positions our LLM ex-
the classical assumptions of semantic realism and lo- periments as a novel methodology for investigating the
cality often implicit in DSMs and traditional linguistic fundamental nature of semantic contextuality itself. In
theories. Classical realism assumes pre-existing, definite this light, LLMs serve as sophisticated “computational
meanings, while locality assumes semantic components cognitive systems” capable of bridging the gap between
can be independently determined. A quantum semantic themacro-levelstatisticalphenomenafoundincollective
approach, by contrast, treats expressions as a!ording a human data and the micro-level interpretive acts of an
spectrum of potential interpretations (a superposition), individual agent. The contextuality we observe, there-
withaspecificmeaningbeing‘collapsed’oractualizedby fore,suggeststhisnon-classicalbehaviorisnotaquirkof
anagent’sinterpretive‘measurement’withinagivencon- human psychology or a specific LLM architecture, but a
text. Thisalignswithconstructivisttheoriesincognitive pervasive feature of how semantic meaning is structured
science that view understanding as an active, situated and processed in any complex, interconnected system.
process [22, 26, 78]. Philosophical critiques of essential-
istviewsofmeaning[e.g.,later79,80]alsoresonatewith
our results as meaning becomes tied to use and inter- D. Methodological Shifts: Bayesian Exploration
action rather than inhering statically in symbols. The and Quantum Cognition Analogies
non-commutativity of interpretive operations—a feature
of the quantum semantic model—implies that the order
The dual arguments—the limitations imposed by se-
of contextual probing can a!ect the realized meaning, a
mantic degeneracy on classical systems and the poten-
phenomenon di"cult to capture in purely classical addi-
tial of a quantum semantic framework—strongly suggest
tive models but observed in human cognition, e.g. order
a paradigm shift in NLP methodologies towards non-
e!ects in judgment [81] and quantum-like contextuality
classical, Bayesian-informed approaches. Instead of pur-
e!ects such as the ‘Pet-Fish’ problem [58].
suing a single, definitive interpretation, techniques in-
volving Monte Carlo sampling of interpretations under
diverse contextual conditions, combined with dynamic
C. Quantum Semantics: Connections to Cognitive explorations of semantic space (e.g., through Markovian
and Psycholinguistic Phenomena randomwalks),mayo!ermorepracticallyusefulandro-
bust characterizations of text. This is particularly rel-
Theobserver-dependentactualizationcentraltoquan- evant for tasks such as nuanced translation, novel dis-
tum semantics provides a compelling explanatory frame- covery, and complex single-turn completion where LLMs
work for a range of established cognitive and psycholin- currentlyfaceinherentdi"cultiesduetotheKolmogorov
guistic findings. The profound influence of an agent’s complexitychallenge;asystemdesignedtoexploreawide
current context, goals, and primed semantic memory on distribution of plausible actualizations, e!ectively navi-

9
gating many potential paths from problem to solution, tigate the fundamental, non-classical nature of semantic
whileslower,wouldlikelyprovemoree!ectiveatapprox- meaning. We have approached this analysis by identify-
imating an understanding of the requirements of the se- ing the information-theoretic limits inherent in any act
mantic expression. Adopting such a Bayesian-informed of linguistic interpretation and have provided the first
perspective allows systems to treat ambiguity not as an knowntestofcontextualityintheinterpretiveactsofdi-
error to be eliminated, but as an inherent and informa- verse LLM-powered AI agents. Our major conclusions
tive feature of the semantic landscape. This approach are the following:
directlyaddressesthecomputationalintractabilityposed
by semantic degeneracy, o!ering a practical path toward 1. Semantic degeneracy is a fundamental property
building more resilient and contextually-aware language of natural language that imposes an information-
technologies that better reflect the probabilistic nature theoreticlimitoninterpretation;ouranalysisusing
of meaning itself. Kolmogorovcomplexity(SectionII)formalizeshow
this makes the recovery of a single intended mean-
ing from a complex expression computationally in-
tractable for any system, thereby providing a clear
E. Practical Architectures and the Role of Human
Oversight explanation for the observed performance plateaus
in LLMs.
Translatingtheseconceptualshiftsintopracticalappli-
2. Linguistic interpretation under ambiguity exhibits
cations, especially for complex scenarios such as multi-
non-classicalcontextuality,asdemonstratedbyfre-
agent systems [83, 84], or large-scale enterprise envi-
quent and significant violations of the CHSH in-
ronments demanding dynamic document understanding equality (S >2) in our semantic Bell test experi-
[85,86],necessitatesthedevelopmentofnovelandadapt- | |
ments with LLM agents (Sections IV, V).
able system architectures for models attempting to ap-
proach intelligence. These architectures must be capable 3. Thecontextualitymeasuredintheinterpretiveacts
of managing and leveraging contextual variability rather of LLMs is consistent with a broader pattern of
than attempting to eliminate it. Crucially, the observer- non-classical findings across human cognitive sci-
dependent nature of meaning actualization, as posited ence, indicating that observer-dependence and in-
by the quantum semantic framework, underscores the determinacy are general principles of information
enduring and fundamental importance of Human-in-the- processing and not simply artifacts of human psy-
Loop(HITL)systems. Farfrombeingatemporarymea- chology.
sure until AI achieves perfect autonomy, HITL will re-
4. The observer-dependent nature of meaning, con-
main an integral component for navigating inherent se-
firmed by our experiment, reveals that there is
mantic ambiguity, validating interpretations, and ensur-
no absolute, fundamental meaning to be found,
ingthatsystemoutputsalignwithhumangoalsandethi-
only contextualized interpretations; consequently,
cal considerations, particularly in safety-critical domains
the only viable scientific methodology is to shift
[87–89]likehealthcare,defense,andfinance. Theexplicit
from seeking any single “correct” answer and in-
recognition of both the fundamental limits of purely au-
steaduserepeatedBayesian-stylesamplingtochar-
tomated interpretation in open contexts and the poten-
acterizehowtheseconditionalinterpretationsinter-
tial of alternative, context-aware frameworks can guide
connect within a possibility space.
thedevelopmentofmorerealistic,robust,andultimately
more capable language technologies.
5. The consistent emergence of non-classical contex-
tuality across a diverse pool of non-biological LLM
agents, when considered alongside similar findings
VII. CONCLUSIONS in human cognition, indicates that these statistical
propertiesarenotartifactsofanyspecificinterpre-
In this work, we have used a theoretical framework tivesystembutareobjective,structuralfeaturesof
basedonKolmogorovcomplexityandanovelexperimen- natural language itself.
tal design using Large Language Model agents to inves-
[1] H.L.Dreyfus,What Computers Still Can?T Do: A Cri- analysis,JournaloftheAmericanSocietyforInformation
tique of Artificial Reason (MIT Press, 1992). Science 41, 391 (1990).
[2] Z. S. Harris, Distributional Structure, WORD 10, 146 [4] T.K.LandauerandS.T.Dumais,ASolutiontoPlato’s
(1954). Problem: The Latent Semantic Analysis Theory of Ac-
[3] S.C.Deerwester,S.T.Dumais,G.W.Furnas,T.K.Lan- quisition, Induction, and Representation of Knowledge,
dauer,andR.A.Harshman,Indexingbylatentsemantic Psychological Review 104, 211 (1997).

10
[5] T.L.Gri"ths,M.Steyvers,andJ.B.Tenenbaum,Topics WordFrequencyE!ect: TheNeglectedRoleofDistribu-
in semantic representation, Psychological Review 114, tional Information in Lexical Processing, Language and
211 (2007). Speech 44, 295 (2001).
[6] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, [22] L. W. Barsalou, Situated simulation in the human con-
and J. Dean, Distributed Representations of Words ceptual system, Language and Cognitive Processes 18,
and Phrases and their Compositionality, arXiv preprint 513 (2003).
arXiv:1310.4546 (2013), arXiv:1310.4546 [cs.CL]. [23] W. Yeh and L. W. Barsalou, The Situated Nature of
[7] J.Devlin,M.-W.Chang,K.Lee,andK.Toutanova,Bert: Concepts,TheAmericanJournalofPsychology119,349
Pre-training of deep bidirectional transformers for lan- (2006).
guage understanding, arXiv Preprint arXiv:1810.04805 [24] E. T. Higgins, Knowledge activation: Accessibility, ap-
(2018), arXiv:1810.04805. plicability, and salience, in Social Psychology: Handbook
[8] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and of Basic Principles, edited by E. T. Higgins and A. W.
I. Sutskever, Language models are unsupervised multi- Kruglanski (Guilford Press, 1996) pp. 133–168.
task learners, OpenAI Blog (2019), openAI technical re- [25] K.Bicknell,J.L.Elman,M.Hare,K.McRae,andM.Ku-
port, Version 1. tas,E!ectsofeventknowledgeinprocessingverbalargu-
[9] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Ka- ments,JournalofMemoryandLanguage63,489(2010).
plan,P.Dhariwal,A.Neelakantan,P.Shyam,G.Sastry, [26] W. Kintsch, Predication, Cognitive Science 25, 173
A. Askell, et al., Language models are few-shot learners, (2001).
in Advances in Neural Information Processing Systems [27] L. A. M. Lebois, C. D. Wilson-Mendenhall, and L. W.
33(NeurIPS2020),editedbyH.Larochelle,M.Ranzato, Barsalou, Are Automatic Conceptual Cores the Gold
R.Hadsell,M.F.Balcan,andH.Lin(CurranAssociates, Standard of Semantic Processing? The Context-
Inc., 2020) pp. 1877–1901. DependenceofSpatialMeaninginGroundedCongruency
[10] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, E!ects, Cognitive Science 39, 1764 (2015).
L.Jones,A.N.Gomez,L.Kaiser,andI.Polosukhin,At- [28] E. Yee, S. Z. Ahmed, and S. L. Thompson-Schill, Color-
tentionIsAllYouNeed,arXivpreprintarXiv:1706.03762 less green ideas (can) prime furiously, Psychological Sci-
(2017), arXiv:1706.03762 [cs.CL]. ence 23, 364 (2012).
[11] M. N. Jones, When does abstraction occur in semantic [29] K. Hoenig, E.-J. Sim, V. Bochev, B. Herrnberger, and
memory: Insightsfromdistributionalmodels,Language, M. Kiefer, Conceptual Flexibility in the Human Brain:
Cognition and Neuroscience 34, 1338 (2018). Dynamic Recruitment of Semantic Maps from Visual,
[12] P.Ho!man,M.A.LambonRalph,andT.T.Rogers,Se- Motor, and Motion-related Areas, Journal of Cognitive
manticdiversity: Ameasureofsemanticambiguitybased Neuroscience 20, 1799 (2008).
onvariabilityinthecontextualusageofwords,Behavior [30] S. Van Dantzig, D. Pecher, R. Zeelenberg, and L. W.
Research Methods 45, 718 (2013). Barsalou,PerceptualProcessingA!ectsConceptualPro-
[13] M.Assran,Q.Duval,I.Misra,P.Bojanowski,P.Vincent, cessing, Cognitive Science 32, 579 (2008).
M. Rabbat, Y. LeCun, and N. Ballas, Self-supervised [31] C. Bermeitinger, D. Wentura, and C. Frings, How to
learning from images with a joint-embedding predic- switch on and switch o! semantic priming e!ects: Ac-
tive architecture, in Proceedings of the IEEE/CVF Con- tivation processes in category memory depend on focus-
ference on Computer Vision and Pattern Recognition ing specific feature dimensions, Psychonomic Bulletin &
(CVPR) (2023) pp. 15619–15629. Review 18, 579 (2011).
[14] A. Gu and T. Dao, Mamba: Linear-Time Sequence [32] N.S.Hsu,D.J.M.Kraemer,R.T.Oliver,M.L.Schlicht-
Modeling with Selective State Spaces, arXiv e-prints , ing,andS.L.Thompson-Schill,Color,Context,andCog-
arXiv:2312.00752 (2023), arXiv:2312.00752 [cs.LG]. nitive Style: Variations in Color Knowledge Retrieval as
[15] L. Darlow, C. Regan, S. Risi, J. Seely, and aFunctionofTaskandSubjectVariables,JournalofCog-
L. Jones, Continuous Thought Machines, arXiv e-prints nitive Neuroscience 23, 2544 (2011).
, arXiv:2505.05522 (2025), arXiv:2505.05522 [stat.ML]. [33] P.Athanasopoulos,Cognitiverepresentationofcolourin
[16] Q. Sun, E. Cetin, and Y. Tang, Transformer-Squared: bilinguals: The case of Greek blues, Bilingualism: Lan-
Self-adaptive LLMs, arXiv e-prints , arXiv:2501.06252 guage and Cognition 12, 83 (2009).
(2025), arXiv:2501.06252 [cs.LG]. [34] B. Thompson, S. G. Roberts, and G. Lupyan, Cultural
[17] T. Simonds and A. Yoshiyama, LADDER: Self- influencesonwordmeaningsrevealedthroughlarge-scale
Improving LLMs Through Recursive Problem Decom- semantic alignment, Nature Human Behaviour 4, 1029
position, arXiv e-prints , arXiv:2503.00735 (2025), (2020).
arXiv:2503.00735 [cs.LG]. [35] B. T. Johns, Distributional social semantics: Inferring
[18] P. Tabossi, L. Colombo, and R. Job, Accessing lexical word meanings from communication patterns, Cognitive
ambiguity: E!ects of context and dominance, Psycho- Psychology 131, 101441 (2021).
logical Research 49, 161 (1987). [36] J. Cesario, J. E. Plaks, N. Hagiwara, C. D. Navarrete,
[19] K. S. Binder and K. Rayner, Contextual strength does and E. T. Higgins, The Ecology of Automaticity: How
notmodulatethesubordinatebiase!ect: Evidencefrom Situational Contingencies Shape Action Semantics and
eye fixations and self-paced reading, Psychonomic Bul- Social Behavior, Psychological Science 21, 1311 (2010).
letin & Review 5, 271 (1998). [37] V. Marian and M. Kaushanskaya, Language context
[20] K. Rayner, A. E. Cook, B. J. Juhasz, and L. Frazier, guidesmemorycontent,PsychonomicBulletin&Review
Immediate disambiguation of lexically ambiguous words 14, 925 (2007).
during reading: Evidence from eye movements, British [38] L. W. Barsalou, Simulation, situated conceptualization,
Journal of Psychology 97, 467 (2006). and prediction, Philosophical Transactions of the Royal
[21] S. A. McDonald and R. C. Shillcock, Rethinking the Society B: Biological Sciences 364, 1281 (2009).

11
[39] D. Pecher, R. Zeelenberg, and J. G. W. Raaijmakers, Theory in Psychology and Beyond.
Does Pizza Prime Coin? Perceptual Priming in Lexi- [57] E. M. Pothos and J. R. Busemeyer, Quantum cognition,
cal Decision and Pronunciation, Journal of Memory and Annual Review of Psychology 73, 749 (2022).
Language 38, 401 (1998). [58] D.Aerts,M.Czachor,B.D’Hooghe,S.Sozzo,etal.,The
[40] A. M. Borghi, A. M. Glenberg, and M. P. Kaschak, pet-fish problem on the world-wide web., in AAAI Fall
Putting words in perspective, Memory & Cognition 32, Symposium: Quantum Informatics for Cognitive, Social,
863 (2004). and Semantic Processes (2010).
[41] L. Connell and D. Lynott, Principles of Representation: [59] J. S. Bell, On the einstein podolsky rosen paradox,
WhyYouCan’tRepresenttheSameConceptTwice,Top- Physics Physique Fizika 1, 195 (1964).
ics in Cognitive Science 6, 390 (2014). [60] S. Uprety, Investigation and modelling of quantum-like
[42] E.MuszandS.L.Thompson-Schill,Semanticvariability user cognitive behaviour in information access and re-
predicts neural variability of object concepts, Neuropsy- trieval (2020).
chologia 76, 41 (2015). [61] D.Aerts,S.Aerts,J.Broekaert,andL.Gabora,Thevio-
[43] J. Vervaeke and L. Ferraro, Relevance, meaning and the lationofbellinequalitiesinthemacroworld,Foundations
cognitive science of wisdom (2013). of Physics 30, 1387 (2000).
[44] B. P. Andersen, M. Miller, and J. Vervaeke, Predictive [62] D. Aerts, J. A. Arguëlles, L. Beltran, S. Geriente, M. S.
processing and relevance realization: Exploring conver- deBianchi,S.Sozzo,andT.Veloz,Spinandwinddirec-
gentsolutionstotheframeproblem,Phenomenologyand tionsi: Identifyingentanglementinnatureandcognition,
the Cognitive Sciences , 1 (forthcoming). Foundations of Science 23, 323 (2018).
[45] J. Jaeger, A. Riedl, A. Djedovic, J. Vervaeke, and [63] D.Aerts,J.A.Arguëlles,L.Beltran,S.Geriente,M.Sas-
D. Walsh, Naturalizing relevance realization: Why soli de Bianchi, S. Sozzo, and T. Veloz, Spin and wind
agency and cognition are fundamentally not computa- directions ii: A bell state quantum model, Foundations
tional (2023). of Science 23, 337 (2018).
[46] J.VervaekeandL.Ferraro,Relevancerealizationandthe [64] P. Bruza, L. Fell, P. Hoyte, S. Dehdashti, A. Obeid,
neurodynamics and neuroconnectivity of general intelli- A. Gibson, and C. Moreira, Contextuality and context-
gence,inSmartData,editedbyI.Harvey,A.Cavoukian, sensitivityinprobabilisticmodelsofcognition,Cognitive
G. Tomko, D. Borrett, H. Kwan, and D. Hatzinakos Psychology 140, 101529 (2023).
(Springer New York, New York, NY, 2013) pp. 57–68. [65] A. N. Kolmogorov, Three approaches to the quantita-
[47] D.L.Hintzman,MINERVA2: Asimulationmodelofhu- tive definition of information, Problems of Information
man memory, Behavior Research Methods, Instruments, Transmission 1, 1 (1965).
& Computers 16, 96 (1984). [66] J.F.Clauser,M.A.Horne,A.Shimony,andR.A.Holt,
[48] R. K. Jamieson, J. E. Avery, B. T. Johns, and M. N. Proposed experiment to test local hidden-variable theo-
Jones, An Instance Theory of Semantic Memory, Com- ries, Phys. Rev. Lett. 23, 880 (1969).
putational Brain & Behavior 1, 119 (2018). [67] W. Guo and A. Caliskan, Detecting Emergent Intersec-
[49] W. O. Van Dam, S.-A. Rueschemeyer, O. Lindemann, tionalBiases: ContextualizedWordEmbeddingsContain
andH.Bekkering,ContextE!ectsinEmbodiedLexical- aDistributionofHuman-likeBiases,inProceedingsofthe
Semantic Processing, Frontiers in Psychology 1, 150 2021AAAI/ACMConferenceonAI,Ethics,andSociety
(2010). (2021) pp. 122–133.
[50] W. O. Van Dam, M. Van Dijk, H. Bekkering, and S.-A. [68] B. K. Payne, H. A. Vuletich, and K. B. Lundberg, The
Rueschemeyer, Flexibility in embodied lexical-semantic Bias of Crowds: How Implicit Bias Bridges Personal
representations,HumanBrainMapping33,2322(2012). and Systemic Prejudice, Psychological Inquiry 28, 233
[51] D. Aerts, Quantum structure in cognition, Journal of (2017).
Mathematical Psychology 53, 314 (2009), special Issue: [69] Z. Siddique, I. Khalid, L. D. Turner, and L. Espinosa-
Quantum Cognition. Anke, Shifting perspectives: Steering vector ensem-
[52] P. Bruza, J. R. Busemeyer, and L. Gabora, Introduc- bles for robust bias mitigation in llms, arXiv preprint
tion to the special issue on quantum cognition, Journal arXiv:2503.05371 (2025).
of Mathematical Psychology 53, 303 (2009), special Is- [70] I. O. Gallegos, R. A. Rossi, J. Barrow, M. M. Tanjim,
sue: Quantum Cognition. S. Kim, F. Dernoncourt, T. Yu, R. Zhang, and N. K.
[53] L. Gabora and D. A. and, Contextualizing con- Ahmed, Bias and fairness in large language models: A
cepts using a mathematical generalization of the survey, arXiv preprint arXiv:2309.00770 (2023).
quantum formalism, Journal of Experimental & [71] A. Kitadai, K. Ogawa, and N. Nishino, Examining the
Theoretical Artificial Intelligence 14, 327 (2002), feasibility of large language models as survey respon-
https://doi.org/10.1080/09528130210162253. dents, in 2024 IEEE International Conference on Big
[54] P. Bruza, K. Kitto, B. Ramm, L. Sitbon, and D. Song, Data (BigData) (2024) pp. 3858–3864.
Quantum-like non-separability of concept combinations, [72] A. Salecha, M. E. Ireland, S. Subrahmanya, J. Sedoc,
emergent associates and abduction,Logic Journal of the L. H. Ungar, and J. C. Eichstaedt, Large language
IGPL 20, 445 (2012). models display human-like social desirability biases in
[55] P. Bruza, K. Kitto, B. Ramm, and L. Sitbon, A proba- big five personality surveys, PNAS Nexus 3, pgae533
bilistic framework for analysing the compositionality of (2024), https://academic.oup.com/pnasnexus/article-
conceptual combinations, Journal of Mathematical Psy- pdf/3/12/pgae533/61188312/pgae533.pdf.
chology 67, 26 (2015). [73] L. Tjuatja, V. Chen, T. Wu, A. Talwalkwar, and
[56] J.M.YearsleyandJ.R.Busemeyer,Quantumcognition G. Neubig, Do llms exhibit human-like response bi-
anddecisiontheories: Atutorial,JournalofMathemati- ases? a case study in survey design, Transactions
calPsychology 74,99(2016),foundationsofProbability of the Association for Computational Linguistics

12
12, 1011 (2024), https://direct.mit.edu/tacl/article- updating: The belief-adjustment model, Cognitive Psy-
pdf/doi/10.1162/tacl_a_00685/2468689/tacl_a_00685.pdf. chology 24, 1 (1992).
[74] S. T. Piantadosi and F. Hill, Meaning without [82] J. R. Anderson and R. Milson, Human memory: An
reference in large language models, arXiv preprint adaptive perspective, Psychological Review 96, 703
arXiv:2208.02957 (2022). (1989).
[75] A. Lampinen, I. Dasgupta, S. Chan, K. Mathewson, [83] Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu,
M. Tessler, A. Creswell, J. McClelland, J. Wang, and L. Jiang, X. Zhang, S. Zhang, J. Liu, A. H. Awadal-
F. Hill, Can language models learn from explanations lah, R. W. White, D. Burger, and C. Wang, Au-
incontext?,inFindings of the Association for Computa- toGen: Enabling next-gen large language model ap-
tionalLinguistics: EMNLP2022,editedbyY.Goldberg, plications via multi-agent conversation, arXiv preprint
Z. Kozareva, and Y. Zhang (Association for Computa- arXiv:2308.08155 (2023).
tional Linguistics, Abu Dhabi, United Arab Emirates, [84] LlamaIndex Contributors, Multi-Agent Workflows —
2022) pp. 537–563. LlamaIndex Documentation (2025).
[76] E. N. Dzhafarov, J. V. Kujala, and V. H. Cervantes, [85] P.Herzig,Sap’snewaiinnovationsandpartnershipsde-
Contextuality-by-default: a brief overview of ideas, con- liver real-world results (2024).
cepts, and terminology, inQuantum Interaction: 9th In- [86] J. Srivastava, J. Schuurmans, K. Ray, L. Mesnage,
ternational Conference, QI 2015, Filzbach, Switzerland, N. Butler, S. Dutta, T. Kubit, and T. Janner, Genai
July 15-17, 2015, Revised Selected Papers 9 (Springer, can revolutionize erp transformations, Boston Consult-
2016) pp. 12–23. ing Group Insight (2025).
[77] V. H. Cervantes and E. N. Dzhafarov, Advanced analy- [87] V. Quach, A. Fisch, T. Schuster, A. Yala, J. H. Sohn,
sisofquantumcontextualityinapsychophysicaldouble- T. S. Jaakkola, and R. Barzilay, Conformal language
detection experiment, Journal of Mathematical Psychol- modeling, arXiv preprint arXiv:2306.10193 (2023).
ogy 79, 77 (2017). [88] Z. Li, W. Wu, Y. Wang, Y. Xu, W. Hunt, and
[78] J. L. Elman, Finding Structure in Time, Cognitive Sci- S. Stein, HMCF: A human-in-the-loop multi-robot col-
ence 14, 179 (1990). laboration framework based on large language models,
[79] L. Wittgenstein, Philosophical Investigations (Basil arXiv preprint arXiv:2505.00820 (2025).
Blackwell, Oxford, 1953). [89] K. Naminas, Human in the loop machine learning: The
[80] W. V. O. Quine, Word & Object (MIT Press, 1960). key to better models (2025).
[81] R.M.HogarthandH.J.Einhorn,Ordere!ectsinbelief
