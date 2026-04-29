---
id: pdf-vaishak-belle-2026-the-future-is
type: pdf
title: 'The Future Is Neuro-Symbolic: Where Has It Been, and Where Is It Going?'
url: ''
authors:
- Vaishak Belle
- Gary Marcus
ingested_at: '2026-04-29T16:18:34Z'
content_hash: sha256:fd5a53d1ee64003cc36fb5acced44f31c205f50b0d72250717e6dd9ded2ea981
source_path: raw/pdf/pdf-vaishak-belle-2026-the-future-is.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 8
  extraction_tool: pdfplumber
  pdf_metadata_subject: The Fortieth AAAI Conference on Artificial Intelligence (AAAI-26)
  pdf_metadata_keywords: 'ETA: Neuro-symbolic AI, ETA: Third Wave Of AI, ETA: Connectionism
    And Symbolism, ETA: Symbol Emergence'
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__be6c6b08.pdf
published_at: '2026'
---
TheFortiethAAAIConferenceonArtificialIntelligence(AAAI-26)
The Future Is Neuro-Symbolic: Where Has It Been, and Where Is It Going?
VaishakBelle1,GaryMarcus2
1UniversityofEdinburgh
2NewYorkUniversity(Emeritus)
Abstract Todealwithpossiblyfalsefacts,anduncertaintyingen-
eral, probabilistic logics emerged (Bacchus 1990; Halpern
Thisreportexplorestheevolutionandcurrentstateofneuro-
2003),thatallowedforamixtureofprobabilisticandlogical
symbolic artificial intelligence, an approach that integrates
assertions. However, because they inherited the expressive
neural network capabilities with symbolic reasoning. We
powerof(oftenfirst-order)logicbutthenfurtherextendedit
trace the historical context from early AI aspirations to
modern implementations and successes, highlighting key forprobabilisticknowledge,theytoosufferedfromscalabil-
paradigms,andotherlogicalandsemanticalconsiderations. ityissues.Andtheylargelyglossedoverthepointofwhere
We argue against the “scaling is all you need” hypothesis, the probabilities came from. Presumably, these need to be
andpointtopersistentchallengesinreliablesymbolicreason- drawn from data, but integrating the learning of statistical
ingwithdeepandlargemodels.Weconcludebysuggesting information and ensuring its consistency with prior logical
thatdespitenumerousimplementationchoicesandthe“broad knowledgeisanon-trivialmatter(Valiant1999).
church”natureofneuro-symbolicAI,theseapproachesoffer
When limited to graphs, however, Bayesian (and later
the most promising path towards AI systems that combine
causal)networksofferedareasonablecompromisebetween
patternrecognitionwithrobustreasoning,particularlyforap-
expert knowledge together with probabilistic and statisti-
plicationsrequiringstructuredknowledge,explainability,and
calinformation(Pearl1998),andwereamenabletocertain
trustworthiness.
types of learning from data (Koller and Friedman 2009).
Building on this success, the field of statistical relational
Introduction
learning (SRL) aimed to unify logical and probabilistic
In its original inception, the field of artificial intelligence frameworks by controlling the expressiveness (Raedt et al.
(AI) was deeply concerned with how human cognition 2016), such as by investigating finite-domain relational ex-
could be automated on a computer (Turing 1950). John tensions to Bayesian networks (Koller and Pfeffer 1997;
McCarthy, for example, argued for the development of so- Getooretal.2001).Bethatasitmay,apurelyexpert-driven
calledcommon-senseprogramsthatcouldreasonandprob- paradigmfordealingwithhigh-dimensionaldataisunlikely
lem solve, using the mathematical apparatus of logic for tosucceed–unlesstheyoutsourcedata-heavycomputation
formalising the application domain. The idea was arguably toneuralnetworks.
radicalatthattime(althoughLeibnizhadalreadywondered
aboutthinkingasanalgebraicprocess(Levesque2012)). FromNeuraltoNeuro-Symbolic
Despite continuing extensions of logical formalisms to In the areas of vision and speech, in the last two decades,
deal with actions, plans and agents (Levesque 1996; Kelly neural network-based learning began demonstrated out-
and Pearce 2008), three representational aspects severely standing performance in pattern recognition across com-
challengethisprogram:(a)thelackofcompleteknowledge putervision(Krizhevsky,Sutskever,andHinton2012),natu-
(that is, an exhaustive formalisation) in almost all applica- rallanguageprocessing,andrecommendationsystems.This
tions,(b)thedifficultyinassertingthatlogicalassertionsare is owing to a cascade of improvements. Classically, neural
categorically true, and (c) the need to leverage sensorimo- networkswerebuiltconsistingofinput,hidden,andoutput
tordataandrelevantstatisticalpatternsfromthatdata.Sen- layers with limited depth, but then “deep” learning archi-
sorimotor data, including visual and auditory information, tectures introduced multiple hidden layers, likely enabling
moreover,issampledfromhigh-dimensionalspaces,which thelearningofdeeperhierarchicalrepresentations(although
leadtotheproblemofscalabilitywithpurelylogicalframe- these internal constructions are largely opaque to humans).
works.Forexample,a16!16blackandwhiteimagewould Therewerealso:
require,say,adatastructurewith216 16propositionstocap-
× 1. Architecturalimprovements:Thedevelopmentofcon-
ture the pixel values, and for a dataset of 100,000 images
volutionalneuralnetworks(CNNs)forcomputervision,
wouldrequireasmanyinstancesofsuchdatastructures.
recurrent neural networks (RNNs) (Goodfellow et al.
Copyright©2026,AssociationfortheAdvancementofArtificial 2016)andtransformers(Vaswanietal.2017)forsequen-
Intelligence(www.aaai.org).Allrightsreserved. tial data, and graph neural networks for structured data
40954

(Barcelo´ et al. 2020) dramatically expanded the repre- worlds distinct from the controlled settings where the
sentationalcapabilitiesofneuralapproaches. data was collected in the first place. All of this leads to
2. Training regimes: Although not always well under- degraded performance or complete failure, some catas-
stood, techniques such as dropout and batch normalisa- trophic.Onemayresortto(oftenexpensive)continuous
tion(Goodfellowetal.2016)targetedissuesincomput- retrainingoradaptationmechanisms,butageneralsolu-
inggradients. tionislacking(Luetal.2018;Mallicketal.2022).
3. Computational advances: The development of GPU The development of neuro-symbolic AI can be under-
computing provided the necessary computational power stood as a response to the limitations of purely neural ap-
totraincomplexmodelswiththousandsofhiddenlayers proaches(Sun2002;GarcezandLamb2023;Marcus2001).
onmassivedatasets. Interestingly,toalargeextent,itcanremainagnosticabout
4. Data availability: Partly driven by the ability to now howdeeplearningmaymatureinthefuture.Oneofthemo-
harness such datasets, continued efforts in data collec- tivations of neuro-symbolic AI is to also better understand
tion, including from the internet, provided the training how symbols emerge (Garcez and Lamb 2023), which, yet
resourcesneededforsuchmodelstolearn. again,fitsnicelywiththedeeplearningparadigmwherethe
hypothesisisentirelyimplicit,informedbythehyperparam-
Despitethesestrides,purelyneuralmodelsstillhaveim- eters.Suchsymbolswouldthenempowerthereasoningpro-
portant,andperhapsfundamentallyirreparable,limitations. cessesofthesystem,andpossiblyaidintransparency,guar-
Ontheonehand,thesemodelsrequirelargeamountsofdata antees,correctnessandbeyond.
to achieve robust predictions, making them unsuitable for
From a practical viewpoint, neuro-symbolic AI seeks to
many applications where extensive datasets are simply not
combine the pattern recognition capabilities of neural net-
available.Butontheother,doesscalingthesemodelstotrain
works with the explicit reasoning mechanisms of symbolic
overlargerandlargerdatasetsleadtogeneral-purposeintel-
systems.Inthissense,neuro-symbolicAIisnotbutasingle
ligence(Chollet2019)?Thatis,wouldit“hitawall”interms
approach,butafamilyofframeworksthatconsiderthecou-
ofitsabilities(Marcus2018,2022;Chollet2017)?
pling of symbols and reasoning, on the one hand, and con-
From a technical viewpoint, purely neural models have nectionism,probabilitiesandlearning,ontheother(Hitzler
been noted to exhibit several critical limitations (Marcus andSarker2022;Sarkeretal.2021).Fromalogicalpointof
2018;Besoldetal.2021): view, there is further debate on whether a fuzzy semantics
1. Structuredreasoning:Neuralnetworksarepowerfulat for the representations is better suited (van Krieken, Acar,
patternrecognitionbutstrugglewithhierarchicalorcom- and van Harmelen 2022) or a probabilistic (De Smet and
positereasoning(LakeandBaroni2018)andcannotef- DeRaedt2025)one,thelattercloselyborrowingandextend-
fectivelydifferentiatebetweencausalityandcorrelation. ingearlierworkonstatisticalrelationallearning(DeRaedt
Thecommunityhasoftenaddressedthatbyexplicitpro- etal.2020).
grammatic bias, which is essentially a neuro-symbolic As noted in (Garcez and Lamb 2023), precisely because
endeavor (Ellis et al. 2022; Lake, Salakhutdinov, and of this broad remit, it relates to debates and discussions on
Tenenbaum2015),aswediscussbelow. howtointegratealgebraicprocessingwithneuralnetworks
(MarcusandDavis2019;Marcus2001),aswellasKahne-
2. Data requirements: As mentioned above, neural net-
man’sSystem1vsSystem2thinking(Kahneman2011).
works demand large amounts of data to achieve robust
This sub-field has gained increasing prominence, with
predictions, making them unsuitable for many applica-
dedicated workshops (e.g., hosted by Samsung and IBM),
tions where extensive datasets are simply not available
interest groups at major research institutions (e.g., at the
(Marcus2018),andwherethereisexistingexpertknowl-
Alan Turing Institute), and the recent establishment of
edgethatisnoteasilyreflectedinthecollecteddata.
a specialized journal. Google DeepMind’s Olympiad-level
3. Knowledgeintegration:Onthelatterpoint,neuralnet-
AI solvers are neuro-symbolic (Google DeepMind 2024b).
works do not easily support the integration of expert or
Likewise, the increasing use of symbolic systems such
commonsenseknowledge(Maldonadoetal.2018).
as code interpreters within LLM-based systems represents
4. Explainability: Neural networks function as black-box another neuro-symbolic approach; however, as argued by
systems,makingitdifficulttounderstandhowtheyreach (Marcus2025b),thistrainingregimeisnotalwaysacknowl-
specificpredictionsforgiveninputs(Rudin2019). edged, leading the wider community to believe LLM sys-
5. Guarantees: Neural networks compute probability dis- tems have powerful reasoning capabilities despite not hav-
tributions over possible outcomes, potentially predict-
inganyinbuiltsymbolicmanipulationengines.1
ing outcomes that violate constraints, a serious concern Indeed, as studied by efforts such as (Valmeekam et al.
in safety-critical applications (Gajowniczek et al. 2020; 2022),LLMs’abilitytoreasonaboutmathematicalandsym-
InnesandRamamoorthy2020). bolictruthsisbrittleandunreliable.Outsideofthis,thein-
6. Distributiondrift:Neuralnetworks,andalmostallother
1Anuancedpointofdebatehereiswhetherintegrating,say,a
statistical models that predict by learning a distribution
pythoninterpretercountsasneuro-symbolicinjustthesameway
forthetrainingdata,struggleinenvironmentsthatdiffer as integrating a SAT solver does. We gloss over the point here,
from their training data (Marcus 1998). This is because andonlynotethatsymbolmanipulation,emergence,reasoningand
theydonotincludeanyinherentmechanismstodealwith relatedfacetsareallmajorconsiderationsinneuro-symbolicAI.
40955

ability of stochastic learners to understand causal relation- real-valued)truthofthelabels.Inboththeseformalisms,
shipsaswellasthetendencyoflargemodelstohallucinate theneuraltrainingisinfluencedbythelogicalstructure.
(or more accurately, confabulate) certainly suggests back-
3. Differential program induction. Program induction is
groundexpert-ledknowledgeiscrucialfortrustworthiness.
amajorareaincomputerscience(Gulwani2010).Ano-
table example is work from Google DeepMind (Evans
Directions and Grefenstette 2018) on learning explanatory logic
rules from noisy data, which upgrades inductive logic
Taking a pragmatic view on neuro-symbolic AI as for-
programming to model neural predicates learned from
malisms and frameworks that combine, enhance or other-
noisydata.Arelatedbutsomewhatorthogonalparadigm
wise support neural networks with reasoning mechanisms
usesprogramstoenforcestructureinneuralpredictions,
leads, not surprisingly, to distinct and numerous strategies
asseenintheworkofconceptlearning(Lake,Salakhut-
(Feldstein et al. 2024). For example, an important branch
dinov,andTenenbaum2015).Forworkonhowprogram
of neuro-symbolic AI builds on SRL by combining proba-
inductionmightaffecthumancomprehension,see(Rule
bilisticlogicalmodelswithneuraltraining(DeRaedtetal.
etal.2024).
2020), and this leads a well-defined and scoped view of
neuro-symbolic AI as the neural extension to weighted
4. TrainingNeuralNetworkswithLogicFormulas.The
ideaofconstrainingthelossfunctionofneuralnetworks
model counting (Belle 2017; Chavira and Darwiche 2008;
with symbolic knowledge is useful in a wide range of
Sang,Beame,andKautz2005;VandenBroeck,Meert,and
applications from physics (Stewart and Ermon 2017) to
Darwiche2014).Thereare,however,otherdesignpatterns:
robotics (Innes and Ramamoorthy 2020). There are a
integratingsymbolsintothelearningregimeisnottheonly
number of developments here, such as the work of se-
player in town. One could, for example, let the high-level
manticloss(Gajowniczeketal.2020)andMultiplexNet
controllayerbebasedonlogicthatworkslargelyindepen-
(Hoernle et al. 2022), the former based on a probabilis-
dentlyoftheneural/probabilisticlayers(Silveretal.2023),
ticinterpretationoftheoutputlabels,andthelatterona
commonly seen in robotics applications. In fact, if we are
fuzzy(orreal-valued)truthofthelabels.Thereisaclose
toleveragelargelanguagemodels(Vaswanietal.2017),we
relation between loss function constraints versus high-
wouldundoubtedlyhavemoreinstancesofsuchdecoupling
level knowledge representation, and incidentally the se-
of neural and symbolic functions (Athalye et al. 2024). In
manticlossandDeepProblogperformessentiallysimilar
(Wangetal.2024),forexample,itisshownthataugmenting
functionswhencomputinggradients.
LLMswithexternalworkingmemoryviaaneuro-symbolic
pipelinehelpswithmulti-stepdeductivereasoning. 5. Semantics. As hinted above, some neuro-symbolic for-
Assuggestedin(LenatandMarcus2023),therearesev- malisms use a probabilistic interpretation, and others a
eralinterestingideasfromearlierattemptsofbuildinglarge- fuzzy(orreal-valued)interpretationfortheirlogicalvari-
scaleexpert-drivenlogicalknowledgesources,suchasCYC ables.Thiscanimpactthelearnedhypothesis,andgradi-
(LenatandGuha1989),thatcouldplayapivotalroleinen- ent computation (van Krieken, Acar, and van Harmelen
suringthatgenerativemodelsbecometrustworthyinthefu- 2022). There is also the issue of what sort of semantics
ture. bestdescribesneuro-symboliclearning;e.g.,seediscus-
Keepingthisbreadthinmind,weoutlinesomekeyrepre- sionsin(Tsamoura,Hospedales,andMichael2021)that
sentativeareasofinquiryinthefield.(Wecannotofcourse
itisatypeofabduction.2
coverordojusticetoall,givenscopeandlengthlimits.) 6. Static vs Dynamics. Not surprisingly, adding temporal
or dynamic aspects can change the semantics and lan-
1. Knowledge Graphs and Expert Knowledge Integra-
guage, and there are a number of symbolic solutions to
tion. Knowledge graphs represent a fundamental area
dealing with actions. For example, reward machines fo-
in neuro-symbolic AI, with applications ranging from
cuses on training (reinforcement learning) agents with
proteindatabasesandsocialnetworkstocommonsense
(temporal) logical formulas (Icarte et al. 2022). Differ-
knowledge bases in advanced language models (Demir
ential program induction can be extended to a dynamic
and Ngomo 2023; Hossain, Saghapour, and Chen 2025;
setting(e.g.,reinforcementlearning)too(BelleandBu-
Lavin2021).Researchinthisareafocusesonbothlearn-
eff2023;BueffandBelle2024).
ing such graphs from neural techniques and reasoning
abouttheknowledgetheycontain. 7. Leveraging LLMs. Exploiting and augmenting LLMs
forsymbolicreasoningtasksconstitutesanentirelynew
2. Neuro-Symbolic Programs. Generally, this line of re-
classofapproaches.Whenusedasblackboxhelperfunc-
searchcanbeseenasextendingknowledgegraphswith
tions, systems like Logic-LM (Pan et al. 2023) employ
non-trivial axioms specified in logic programs. Rep-
LLMs to translate natural language into logical formu-
resentative examples include DeepProbLog (Manhaeve
las,afterwhichsymbolicexecutorscomputesolutionsdi-
etal.2018),whichinterfacesneuralpredicatesasexter-
rectly.Thisservesasaneffectivecountermeasureagainst
nal artefacts in probabilistic logic programs, and Logic
TensorNetworks(Badreddineetal.2022),whichallows 2Wehaveglossedoverthetopicofcausality(PearlandMacken-
neural outputs as artefacts in first-order theories. Inter- zie).Whileneuro-symbolicintegrationitselfdoesnotdirectlyad-
estingly, the former is based on a probabilistic interpre- dresscausality,causalknowledgeexpressedusingsymbolicstruc-
tation of the output labels, and the latter on a fuzzy (or tures(HalpernandPearl2005;Halpern2016)might.
40956

LLMconfabulations,particularlyformathematicaltasks Despitethesechallenges(ofmaturity,onemightadd),un-
and puzzles. A pre-ChatGPT solution making a similar less one accepts the “scaling is all you need” argument, it
argumentcanbefoundin(Driesetal.2017),wherecom- is difficult to envision approaches that rigorously and cate-
binatorial problems formulated in natural language are gorically address issues of knowledge integration and cor-
convertedtosymbolicconstructssolvedusinglogicpro- rectnessotherthanneuro-symbolicones!Interestedreaders
gramming.Notably,WolframAlphaimplementedacom- mayalsoreferto(Marcus2022)onwhyoneshouldnotbe
parablepipelinejustasChatGPTwasreleased(Wolfram acceptingthescalingargumentinthefirstplace.As(Marcus
2023). These symbolic executor pipelines demonstrate 2025a)putsit,itisproblematicscientifically,economically,
considerable power; they can correctly handle modal andpolitically.
reasoning problems such as theory of mind (Tang and Still,neurosymbolicAIshouldnotbeenseenasamagic
Belle 2024). Similarly, (Athalye et al. 2024) build sym- bulletforsolvinggeneral-purposeAI,noramagicsolution
bolic world models from language models. Importantly, for trustworthiness. For example, formal approaches may
such symbolic guardrails may be essential, as LLMs not capture various non-quantifiable harms in the resposi-
consistently struggle with reasoning and planning tasks bleandtrustworthydeploymentoftechnology(Belle2023).
(Valmeekametal.2022). Neuro-symbolicAIislikelynecessaryforprogress–primar-
ily because reliable answers about objects in the world re-
Considerations quire world models, which neuro-symbolic approaches can
provide–butitisnotsufficientonitsown(Marcus2020).
Thedesigning,buildinganddeploymentofneuro-symbolic
approachesundoubtedlybringssomeaddedcomplexity,es-
Discussion,DevelopmentsandCaseStudies
peciallyowingtothelackofaunified“framework”orpro-
grammingregime.Butthiswasperhapstruetooduringthe AlphaGeometryandAlphaProof Wediscussedanearly
early days of deep learning. It is worth factoring in a few exampleofneuro-symbolicintegrationinWolframAlpha’s
considerations: ChatGPT extension (Wolfram 2023). For example, asking
ChatGPT about the distance between Chicago and Tokyo
1. Diversity of Approaches. The “broad church” nature
couldleadtoerrors,notleastowingtoitsstochasticity.But
of neuro-symbolic AI (Belle et al. 2023) raises ques-
theextensionparsesthenaturallanguagequestiontoasym-
tions about whether a uniform approach is necessary or
boliclookupinWolframAlpha,plausiblyleadingtothecor-
whetherdiversityinparadigmsbenefitsthefield.Thisin-
rectresponse.Inthisway,itsnotdifferentfromthesymbolic
cludesconsideringifweneedaunifiedmathematicallan-
executorapproachof(Panetal.2023)and(TangandBelle
guagetobridgevarioussystem-buildingmethodologies.
2024),discussedearlier.
Evidence from robotics applications suggests the latter
A significant large-scale development in neuro-symbolic
(Athalye et al. 2024; Silver et al. 2023) given the com-
AI is arguably Google DeepMind’s work on mathematical
plexityofmixinghardwareandsoftwareinteractions.
problem-solving.TheyintroducedsystemsAlphaGeometry
2. Balancing Reasoning and Learning. A fundamen- anditssuccessor,AlphaGeometry2,aswellasanewersys-
tal question concerns the appropriate balance between temcalledAlphaProof,allofwhichachievedimpressivere-
expert-providedknowledgeanddata-derivedknowledge. sultsintacklingInternationalMathematicalOlympiadprob-
This includes considerations about how high-level con- lems (Google DeepMind 2024a). AlphaGeometry (Google
cepts provided by humans might be mapped onto low- DeepMind2024b),forexample,isexplicitlydescribedas“a
level features, and whether these high-level concepts neuro-symbolicsystemmadeupofaneurallanguagemodel
themselvescouldbepartiallyorfullylearned.Theremay and a symbolic deduction engine, which work together to
alsobedomain-specificconsiderationsaboutthebalance find proofs for complex geometry theorems”. This system
betweenneuralandsymboliccomponents,withsomeap- exemplifies the “thinking, fast and slow” paradigm (as re-
plicationareaspotentiallyrequiringmoreofonethanthe ported by Google DeepMind), where one system provides
other. Coupled with this point is the question of what fast,intuitiveideas,andtheotheroffersmoredeliberate,ra-
kindoflogicisneededinneuro-symbolicsystems,e.g., tional decision-making. Likewise, the newer AlphaGeome-
we already noted differences between a probabilistic vs try2systemmaintainsthisneuro-symbolicstructurebutin-
fuzzyinterpretation.Also,propositionallogicandfinite- corporatesalanguagemodel,trainedfromscratchonsignif-
domain relational logic have been common in neuro- icantlymoresyntheticdatathanitspredecessor.AlphaProof
symbolicAI,butonemayneedtofurtherconsidertem- tooappearstohaveananalogousstructure,withalanguage
poral and dynamic logic, particularly for agents operat- model feeding into a search through formal proofs verified
inginphysicalenvironments,andperhapsevenepistemic and formulated in Lean, a symbolic proof assistant system
logic(TangandBelle2024). (Ying et al. 2024). See (Wang et al. 2025; Xin et al. 2024)
3. Knowledge vs Correctness. High-level knowledge forothersuchefforts.Onarelatednote,GoogleDeepMind’s
specifiedforlossfunctionsmaynotbeobeyedaftertrain- AlphaFoldwascitedinarecentNobelPrizeaward(Google
ing (Gajowniczek et al. 2020). There is even evidence DeepMind 2024c), which is a differentiable approach but
that networks could learn properties that are different involves numerous geometry and domain constraints along
fromwhatwasintended(Marconatoetal.2023).Wemay withstructuralpriorsinitsdesign,whichisverymuchinthe
hope that future neuro-symbolic solutions robustly han- spiritofneuro-symbolicmodelling(e.g.,lossfunctionsand
dlesuchproblems,buttheyarecertainlyaconcerntoday. backgroundknowledge)discussedearlier.
40957

LLMs and Reasoning Recent work has highlighted sig- andmorealignable.
nificant limitations in the reasoning capabilities of LLMs
that further motivate the neuro-symbolic approach. For ex- References
ample, studies from both Apple (Shojaee et al. 2025) and
Athalye, A.; Kumar, N.; Silver, T.; Liang, Y.; Wang, J.;
Salesforce (Huang et al. 2025) have demonstrated that
Lozano-Pe´rez, T.; and Kaelbling, L. P. 2024. From
LLMs struggle with algorithmic reasoning and multi-turn
Pixels to Predicates: Learning Symbolic World Models
tasks that require precise execution of procedures. These
via Pretrained Vision-Language Models. arXiv preprint
findings suggest that current LLM technology is likely not
arXiv:2501.00296.
reliableforcomplexreasoningtasks.Andasdiscussedear-
lier, efforts such as (Valmeekam et al. 2022) demonstrated Bacchus,F.1990. RepresentingandReasoningwithProba-
muchearlieraboutthelimitationsofLLMsforplanning. bilisticKnowledge. MITPress.
It is plausible that LLMs might excel at tasks they have Badreddine,S.;Garcez,A.d.;Serafini,L.;andSpranger,M.
encounteredintrainingbutstrugglewithnovelsituationsor 2022. Logic tensor networks. Artificial Intelligence, 303:
slightvariationsoffamiliarproblems.Butvariableandsym- 103649.
bol substitutions, symmetry and transitivity, among other
Barcelo´, P.; Kostylev, E. V.; Monet, M.; Pe´rez, J.; Reutter,
things, are hallmarks of logical reasoning, which suggests
J.;andSilva,J.-P.2020. Thelogicalexpressivenessofgraph
thatalogicaloracleorsolverthatisdistinctfromtheLLM
neuralnetworks. In8thInternationalConferenceonLearn-
machineryisunavoidable.
ingRepresentations(ICLR2020).
Tools Integration Along with Wolfram Alpha’s integra- Belle, V. 2017. Weighted Model Counting With Function
tion with ChatGPT, OpenAI has released plug-ins like Symbols. InUAI.
“Code Interpreter” to enable the model to perform mathe-
Belle, V. 2023. Knowledge representation and acquisition
matical calculations or correctness checking using external
forethicalAI:challengesandopportunities. EthicsandIn-
software.
formationTechnology,25(1):22.
While these integrations improve performance on
straightforward mathematical tasks, they still face chal- Belle, V.; and Bueff, A. 2023. Deep Inductive Logic Pro-
lengesinreliablysolvingwordproblemsthatinvolveacom- gramming meets Reinforcement Learning. In The 39th In-
binationofscienceandmathematics.Asarguedin(Marcus ternationalConferenceon LogicProgramming.Open Pub-
andDavis2023),thedifficultiesarisefromtwomaingaps: lishingAssociation.
LLMsusuallylackthecommonsenseknowledgeneededto Belle, V.; Fisher, M.; Russo, A.; Komendantskaya, E.; and
translatewordproblemsintomathematicalcalculations,and Nottle,A.2023. Neuro-symbolicAI+agentsystems:afirst
theydonotseemtoreliablyunderstandhowtousethetools. reflectionontrends,opportunitiesandchallenges. InInter-
Testing of these tool-augmented systems seems to show nationalConferenceonAutonomousAgentsandMultiagent
mixedresults;see(MarcusandDavis2023)fordiscussions. Systems,180–200.Springer.
This inconsistency suggests the need for more robust inte-
Besold, T. R.; Bader, S.; Bowman, H.; Domingos, P.; Hit-
grationbetweenneuralandsymbolicsystems.
zler, P.; Ku¨hnberger, K.-U.; Lamb, L. C.; Lima, P. M. V.;
de Penning, L.; Pinkas, G.; et al. 2021. Neural-symbolic
Conclusion
learning and reasoning: A survey and interpretation 1. In
Neuro-symbolic AI represents a promising (and perhaps Neuro-symbolic artificial intelligence: The state of the art,
only) approach to addressing the limitations of purely neu- 1–51.IOSpress.
ral or purely symbolic systems. By combining the pattern Bueff, A.; and Belle, V. 2024. Learning explanatory logi-
recognitioncapabilitiesofneuralnetworkswiththereason- calrulesinnon-lineardomains:aneuro-symbolicapproach.
ingpowerofsymbolicsystems,neuro-symbolicapproaches MachineLearning,1–36.
offerpotentialsolutionstochallengesinareassuchasstruc-
Chavira, M.; and Darwiche, A. 2008. On probabilistic in-
tured reasoning, knowledge integration, explainability, and
ferencebyweightedmodelcounting.Artif.Intell.,172(6-7):
reliability.
772–799.
Recent developments, particularly in mathematical
problem-solving systems like AlphaGeometry and Al- Chollet, F. 2017. The limitations of deep learning. Deep
phaProof, demonstrate the viability and effectiveness learningwithPython.
of neuro-symbolic approaches. Given the current ex- Chollet, F. 2019. On the measure of intelligence. arXiv
citement about LLM technology, we pointed to studies preprintarXiv:1911.01547.
that underscore the necessity of moving beyond purely
De Raedt, L.; Dumancˇic´, S.; Manhaeve, R.; and Marra, G.
neural approaches, and assuming scaling will lead to
2020. Fromstatisticalrelationaltoneuro-symbolicartificial
general-purposeAIonitsown.
intelligence. arXivpreprintarXiv:2003.08316.
Fundamentally,determiningtheoptimalbalancebetween
De Smet, L.; and De Raedt, L. 2025. Defining neurosym-
neuralandsymboliccomponents,andunderstandingthefor-
bolicAI. arXivpreprintarXiv:2507.11127.
mal linguistic and semantic requirements, might be a valu-
ableplacetostarttowardsthedevelopmentoffutureAIsys- Demir, C.; and Ngomo, A.-C. N. 2023. Neuro-Symbolic
temsthataremorecapable,morereliable,moreinterpretable ClassExpressionLearning. InIJCAI,3624–3632.
40958

Dries,A.;Kimmig,A.;Davis,J.;Belle,V.;andDeRaedt,L. Hossain, D.; Saghapour, E.; and Chen, J. Y. 2025.
2017. Solving Probability Problems in Natural Language. NeSyDPP4-QSAR: A Neuro-Symbolic AI Approach for
InIJCAI. Potent DPP-4-Inhibitor Discovery in Diabetes Treatment.
Ellis,K.;Albright,A.;Solar-Lezama,A.;Tenenbaum,J.B.;
bioRxiv,2025–03.
andO’Donnell,T.J.2022. Synthesizingtheoriesofhuman Huang, K.-H.; Prabhakar, A.; Thorat, O.; Agarwal, D.;
languagewithBayesianprograminduction. Naturecommu- Choubey, P. K.; Mao, Y.; Savarese, S.; Xiong, C.; and Wu,
nications,13(1):5024. C.-S. 2025. Crmarena-pro: Holistic assessment of LLM
Evans,R.;andGrefenstette,E.2018. Learningexplanatory agents across diverse business scenarios and interactions.
rulesfromnoisydata. JournalofArtificialIntelligenceRe- arXivpreprintarXiv:2505.18878.
search,61:1–64. Icarte, R. T.; Klassen, T. Q.; Valenzano, R.; and McIlraith,
Feldstein, J.; Dilkas, P.; Belle, V.; and Tsamoura, E. 2024. S. A. 2022. Reward machines: Exploiting reward function
Mappingtheneuro-symbolicAIlandscapebyarchitectures: structureinreinforcementlearning. JournalofArtificialIn-
Ahandbookonaugmentingdeeplearningthroughsymbolic telligenceResearch,73:173–208.
reasoning. arXivpreprintarXiv:2410.22077. Innes, C.; and Ramamoorthy, S. 2020. Elaborating on
Gajowniczek, K.; Liang, Y.; Friedman, T.; Zabkowski, T.; learned demonstrations with temporal logic specifications.
andVandenBroeck,G.2020.Semanticandgeneralizeden- arXivpreprintarXiv:2002.00784.
tropylossfunctionsforsemi-superviseddeeplearning. En- Kahneman,D.2011. Thinking,fastandslow. Macmillan.
tropy,22(3):334.
Kelly, R. F.; and Pearce, A. R. 2008. Complex Epistemic
Garcez, A. d.; and Lamb, L. C. 2023. Neurosymbolic AI:
ModalitiesintheSituationCalculus. InKR.
The3rdwave.ArtificialIntelligenceReview,56(11):12387–
Koller,D.;andFriedman,N.2009. ProbabilisticGraphical
12406.
Models-PrinciplesandTechniques. MITPress. ISBN978-
Getoor, L.; Friedman, N.; Koller, D.; and Taskar, B. 2001.
0-262-01319-2.
Learning Probabilistic Models of Relational Structure. In
Koller, D.; and Pfeffer, A. 1997. Object-oriented Bayesian
ICML,170–177.
networks. InProc.UAI,302–313.
Goodfellow, I.; Bengio, Y.; Courville, A.; and Bengio, Y.
2016. Deeplearning,volume1. MITpressCambridge. Krizhevsky, A.; Sutskever, I.; and Hinton, G. E. 2012. Im-
agenet classification with deep convolutional neural net-
Google DeepMind. 2024a. AI achieves silver-medal stan-
works. Advancesinneuralinformationprocessingsystems,
dard solving International Mathematical Olympiad prob-
25.
lems. https://deepmind.google/discover/blog/ai-solves-imo-
problems-at-silver-medal-level/. Vaishak Belle: Accessed: Lake, B.; and Baroni, M. 2018. Generalization without
2025-09-01VaishakBelle:Accessed:2025-09-01. systematicity: On the compositional skills of sequence-to-
sequence recurrent networks. In International conference
Google DeepMind. 2024b. AlphaGeometry:
onmachinelearning,2873–2882.PMLR.
An Olympiad-level AI system for geometry.
https://deepmind.google/discover/blog/alphageometry- Lake,B.M.;Salakhutdinov,R.;andTenenbaum,J.B.2015.
an-olympiad-level-ai-system-for-geometry/. Accessed: Human-level concept learning through probabilistic pro-
2025-09-01. graminduction. Science,350(6266):1332–1338.
Google DeepMind. 2024c. Demis Hassabis & Lavin, A. 2021. Neuro-symbolic neurodegenerative dis-
John Jumper awarded Nobel Prize in Chemistry. ease modeling as probabilistic programmed deep kernels.
https://deepmind.google/discover/blog/demis-hassabis- In International Workshop on Health Intelligence, 49–64.
john-jumper-awarded-nobel-prize-in-chemistry/. Accessed: Springer.
2025-09-01.
Lenat, D.; and Marcus, G. 2023. Getting from generative
Gulwani, S. 2010. Dimensions in program synthesis. In AI to trustworthy AI: What LLMs might learn from CYC.
PPDP,13–24.ACM. arXivpreprintarXiv:2308.04445.
Halpern, J. Y. 2003. Reasoning about Uncertainty. MIT Lenat, D. B.; and Guha, R. V. 1989. Building large
Press. ISBN0262083205. knowledge-based systems; representation and inference in
Halpern,J.Y.2016. Actualcausality. MiTPress. theCycproject. Addison-WesleyLongmanPublishingCo.,
Inc.
Halpern,J.Y.;andPearl,J.2005. Causesandexplanations:
A structural-model approach. Part I: Causes. The British Levesque,H.J.1996. WhatIsPlanninginthePresenceof
JournalforthePhilosophyofScience,56(4):843–887. Sensing? InProc.AAAI/IAAI,1139–1146.
Hitzler,P.;andSarker,M.K.2022. Neuro-SymbolicArtifi- Levesque, H. J. 2012. Thinking as computation: A first
cialIntelligence:TheStateoftheArt. course. MitPress.
Hoernle, N.; Karampatsis, R. M.; Belle, V.; and Gal, K. Lu, J.; Liu, A.; Dong, F.; Gu, F.; Gama, J.; and Zhang, G.
2022. Multiplexnet: Towards fully satisfied logical con- 2018. Learningunderconceptdrift:Areview. IEEEtrans-
straintsinneuralnetworks.InProceedingsoftheAAAICon- actionsonknowledgeanddataengineering,31(12):2346–
ferenceonArtificialIntelligence,5700–5709. 2363.
40959

Maldonado, R.; Goodwin, T. R.; Skinner, M. A.; and Rule,J.S.;Piantadosi,S.T.;Cropper,A.;Ellis,K.;Nye,M.;
Harabagiu, S. M. 2018. Deep learning meets biomedical andTenenbaum,J.B.2024. Symbolicmetaprogramsearch
ontologies: knowledge embeddings for epilepsy. In AMIA improves learning efficiency and explains rule learning in
AnnualSymposiumProceedings,volume2017,1233. humans. NatureCommunications,15(1):6847.
Mallick, A.; Hsieh, K.; Arzani, B.; and Joshi, G. 2022. Sang, T.; Beame, P.; and Kautz, H. A. 2005. Performing
Matchmaker: Data drift mitigation in machine learning for BayesianInferencebyWeightedModelCounting. InAAAI,
large-scalesystems. ProceedingsofMachineLearningand 475–482.
Systems,4:77–94. Sarker,M.K.;Zhou,L.;Eberhart,A.;andHitzler,P.2021.
Manhaeve, R.; Dumancic, S.; Kimmig, A.; Demeester, T.; Neuro-symbolicartificialintelligence. AICommunications,
and De Raedt, L. 2018. Deepproblog: Neural probabilistic (Preprint):1–13.
logic programming. Advances in Neural Information Pro- Shojaee, P.; Mirzadeh, I.; Alizadeh, K.; Horton, M.; Ben-
cessingSystems,31. gio, S.; and Farajtabar, M. 2025. The illusion of thinking:
Marconato,E.;Teso,S.;Vergari,A.;andPasserini,A.2023. Understanding the strengths and limitations of reasoning
Notallneuro-symbolicconceptsarecreatedequal:Analysis models via the lens of problem complexity. arXiv preprint
and mitigation of reasoning shortcuts. Advances in Neural arXiv:2506.06941.
InformationProcessingSystems,36:72507–72539. Silver, T.; Chitnis, R.; Kumar, N.; McClinton, W.; Lozano-
Marcus,G.2018. Deeplearning:Acriticalappraisal. arXiv Pe´rez,T.;Kaelbling,L.;andTenenbaum,J.B.2023. Pred-
preprintarXiv:1801.00631. icate invention for bilevel planning. In Proceedings of
the AAAI Conference on Artificial Intelligence, volume 37,
Marcus, G. 2020. The Next Decade in AI: Four Steps To-
12120–12129.
wardsRobustArtificialIntelligence. arXiv:2002.06177.
Stewart,R.;andErmon,S.2017. Label-freesupervisionof
Marcus,G.2022. Deeplearningishittingawall. Nautilus,
neural networks with physics and domain knowledge. In
10:2022.
Proceedings of the AAAI Conference on Artificial Intelli-
Marcus, G. 2025a. The Fever Dream of Im-
gence,volume31.
minent Superintelligence Is Finally Breaking.
Sun, R. 2002. From the Unconscious to the Conscious: A
https://www.nytimes.com/2025/09/03/opinion/ai-gpt5-
Connectionist-Symbolic Approach. In From Synapses to
rethinking.html. Accessed:2025-09-01.
Rules: Discovering Symbolic Rules from Neural Processed
Marcus, G. 2025b. How o3 and Grok 4
Data,293–313.Springer.
Accidentally Vindicated Neurosymbolic AI.
Tang, W.; and Belle, V. 2024. ToM-LM: Delegating The-
https://garymarcus.substack.com/p/how-o3-and-grok-4-
oryOfMindReasoningtoExternalSymbolicExecutorsin
accidentally-vindicated?r=8tdk6. Accessed:2025-09-01.
LargeLanguageModels. NeSy.
Marcus, G.; and Davis, E. 2019. Rebooting AI: Building
Tsamoura, E.; Hospedales, T.; and Michael, L. 2021.
artificialintelligencewecantrust. Vintage.
Neural-symbolic integration: A compositional perspective.
Marcus, G.; and Davis, E. 2023. Getting GPT to InProceedingsoftheAAAIConferenceonArtificialIntelli-
work with external tools is harder than you think. gence,volume35,5051–5060.
https://garymarcus.substack.com/p/getting-gpt-to-work-
Turing,A.M.1950.ComputingMachineryandIntelligence.
with-external. Accessed:2025-09-01.
Mind,59(236):433–460.
Marcus,G.F.1998. Rethinkingeliminativeconnectionism.
Valiant, L. G. 1999. Robust logics. In Proceedings of the
Cognitivepsychology,37(3):243–282.
thirty-first annual ACM symposium on Theory of Comput-
Marcus, G. F. 2001. The algebraic mind: Integrating con- ing,642–651.
nectionismandcognitivescience. MITpress.
Valmeekam, K.; Olmo, A.; Sreedharan, S.; and Kambham-
Pan, L.; Albalak, A.; Wang, X.; and Wang, W. Y. 2023. pati, S. 2022. Large Language Models Still Can’t Plan
Logic-lm: Empowering large language models with sym- (ABenchmarkforLLMsonPlanningandReasoningabout
bolic solvers for faithful logical reasoning. arXiv preprint Change). arXivpreprintarXiv:2206.10498.
arXiv:2305.12295.
Van den Broeck, G.; Meert, W.; and Darwiche, A. 2014.
Pearl,J.1998.Graphicalmodelsforprobabilisticandcausal SkolemizationforWeightedFirst-OrderModelCounting.In
reasoning. InQuantifiedRepresentationofUncertaintyand KR.
Imprecision,367–389.Springer.
vanKrieken,E.;Acar,E.;andvanHarmelen,F.2022. Ana-
Pearl,J.;andMackenzie,D.???? TheBookofWhy. lyzingdifferentiablefuzzylogicoperators. ArtificialIntelli-
Raedt,L.D.;Kersting,K.;Natarajan,S.;andPoole,D.2016. gence,302:103602.
Statistical relational artificial intelligence: Logic, probabil- Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones,
ity,andcomputation. SynthesisLecturesonArtificialIntel- L.;Gomez,A.N.;Kaiser,Ł.;andPolosukhin,I.2017. At-
ligenceandMachineLearning,10(2):1–189. tentionisallyouneed. Advancesinneuralinformationpro-
Rudin,C.2019.Stopexplainingblackboxmachinelearning cessingsystems,30.
modelsforhighstakesdecisionsanduseinterpretablemod- Wang, H.; Unsal, M.; Lin, X.; Baksys, M.; Liu, J.; San-
elsinstead. NatureMachineIntelligence,1(5):206–215. tos, M. D.; Sung, F.; Vinyes, M.; Ying, Z.; Zhu, Z.; et al.
40960

2025. Kimina-prover preview: Towards large formal rea-
soningmodelswithreinforcementlearning. arXivpreprint
arXiv:2504.11354.
Wang, S.; Wei, Z.; Choi, Y.; and Ren, X. 2024. Symbolic
working memory enhances language models for complex
ruleapplication. arXivpreprintarXiv:2408.13654.
Wolfram,S.2023. Wolframalphaasthewaytobringcom-
putational knowledge superpowers to ChatGPT. Stephen
WolframWritingsRSS,StephenWolfram,LLC,9.
Xin, H.; Guo, D.; Shao, Z.; Ren, Z.; Zhu, Q.; Liu, B.;
Ruan, C.; Li, W.; and Liang, X. 2024. Advancing theo-
remprovinginLLMsthroughlarge-scalesyntheticdata. In
The 4th Workshop on Mathematical Reasoning and AI at
NeurIPS’24.
Ying,H.;Wu,Z.;Geng,Y.;Wang,J.;Lin,D.;andChen,K.
2024. Lean workbook: A large-scale lean problem set for-
malized from natural language math problems. Advances
in Neural Information Processing Systems, 37: 105848–
105863.
40961
