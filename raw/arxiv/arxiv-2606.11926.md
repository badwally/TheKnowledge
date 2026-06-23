---
schema_version: 1
id: arxiv-2606.11926
type: arxiv
title: Toward Generalist Autonomous Research via Hypothesis-Tree Refinement
url: https://arxiv.org/abs/2606.11926
authors:
- Jiajie Jin
- Yuyang Hu
- Kai Qiu
- Qi Dai
- Chong Luo
- Guanting Dong
- Xiaoxi Li
- Tong Zhao
- Xiaolong Ma
- Gongrui Zhang
- Zhirong Wu
- Bei Liu
- Zhengyuan Yang
- Linjie Li
- Lijuan Wang
- Hongjin Qian
- Yutao Zhu
- Zhicheng Dou
ingested_at: '2026-06-22T17:49:32Z'
content_hash: sha256:3b958e29b63336e8c00f65bf254696fecf277ac6ffead77997b035de4e3b68ef
domains:
- ai-and-agents
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2606.11926'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: ''
  abstract_only: false
published_at: '2026-06-10'
source_path: raw/arxiv/arxiv-2606.11926.pdf
filter:
  score: 1.0
  policy_version: ai-and-agents-v0.1.0-auto
  rationale: Directly addresses agentic systems and long-horizon autonomous research
    through Arbor's hypothesis-tree coordinator-executor framework. Rigorous evaluation
    on six real research tasks with published code; strong empirical results (2.5×
    baseline gains). Published June 2026 by Renmin University + Microsoft Research,
    perfectly aligned with domain scope (autonomous agents, multi-agent coordination,
    strategic AI capabilities).
  decided_at: '2026-06-22T17:49:47Z'
  user_correction: null
---
Toward Generalist Autonomous Research via
Hypothesis-Tree Refinement
JiajieJin1,†,‡, YuyangHu1,†, KaiQiu2, QiDai2, ChongLuo2, GuantingDong1, XiaoxiLi1, TongZhao1,
XiaolongMa2, GongruiZhang2, ZhirongWu2, BeiLiu2, ZhengyuanYang2, LinjieLi2, LijuanWang2,
Hongjin
Qian1, YutaoZhu1, ZhichengDou1,∗
1GaolingSchoolofArtificialIntelligence,RenminUniversityofChina,2MicrosoftResearch
†Equalcontribution,‡WorkdoneduringaninternshipatMSRA,∗Correspondingauthor
Scientificprogressdependsonarepeatedloopofexploration,experimentation,andabstraction.Researchers
testcandidatedirections,interprettheevidence,andcarrytheresultinglessonsintolaterattempts.Westudy
howanAIagentcanrunthisloopautonomouslyoverlonghorizons.WeintroduceArbor,ageneralframework
forautonomousresearchthatcombinesalong-livedcoordinator,short-livedexecutors,andHypothesisTree
Refinement(HTR),apersistenttreethatlinkshypotheses,artifacts,evidence,anddistilledinsightsacross
time.Thecoordinatormanagesglobalresearchstrategyoverthetree,whileexecutorsimplementandtest
individualhypothesesinisolatedworktrees.Asresultsreturn,Arborupdatesthetree,propagatesreusable
lessons,refinesthesearchfrontier,andadmitsverifiedimprovements.Thisdesignturnsautonomousresearch
fromasequenceoflocalattemptsintoacumulativeprocessinwhichstrategy,execution,andevidenceare
carriedacrosstime.WeevaluateArborunderAutonomousOptimization(AO),anoperationalsettingwhere
anagentimprovesaninitialresearchartifactthroughiterativeexperimentationwithoutstep-levelhuman
supervision.Acrosssixrealresearchtasksinmodeltraining,harnessengineering,anddatasynthesis,Arbor
achievesthebestheld-outresultonallsixtasks,attainingmorethan2.5×theaveragerelativeheld-outgain
ofCodexandClaudeCodeunderthesametaskinterfaceandresourcebudget.OnMLE-BenchLite,Arbor
reaches86.36%AnyMedalwithGPT-5.5,thestrongestresultinourcomparison.
Note:Thisisalivingtechnicalreportforanongoingproject.Wewillcontinuetorefineandexpandthescopeof
evaluationastheprojectevolves,andwillupdatethisreportaccordingly.
#Contact: jinjiajie@ruc.edu.cn,dou@ruc.edu.cn
https://github.com/RUC-NLPIR/Arbor
Code:
aMath synthesis idea tree
AIME-style math
problem generation
Answer Problem Difficulty
verification structure calibration
1.1 1.2 2.1 2.2 3.1 3.2
code+prompt per-cand. AIME prompt hybrid solver gate 1-shot gate
10% 4% 6% 2% TO TO
1.3 1.4 2.3 2.4 3.3 3.4 factory try parametric 2-stage recalibrate restructure family fixes
fail 14% TO 18% fail 24%
merged evaluated pruned
Merged path: 1.1 -> 1.4 -> 2.4 -> 3.4
24 20
10
0
1 4 8 12
experiment cycle
)%(
erocs
ved
c Normalized held-out gains across tasks
Codex Claude Code Arbor
Model Training
Optimizer
Design Arbor 3237.5
init 3325 steps +2.70%
Architecture
Design Arbor 1.028
init 1.098 loss +6.32%
Harness Engineering
Terminal-
Bench Arbor 77.36 init 69.81 pass +7.55
BrowseComp Arbor 67.67
b Progress over experiment cycles init 45.33 acc. +22.34
difficulty t fa a m rg i e ly te f d ixes t 2 e 0 s . t 83% Data Synthesis recalibration Search-
parametric Agent Arbor 18
c v o e d ri e fi + ca p t r i o o m n pt factory init 5 gap +13.00
Claude Code 8.33 Math-
Reasoning Arbor 20.83
Codex 6.25 init 1.04 gap +19.79
merged not merged test
0 50% 100%
normalized gain from initial to Arbor
Figure1
Arborataglance.
(a)
Hypothesistreeand
(b)
developmentscorefromoneMath-ReasoningDataSynthesisrun.
(c)
Normalizedheld-outgainsacrossalltasks.
1
6202
nuJ
01
]LC.sc[
1v62911.6062:viXra

1 Introduction
Scientificresearchisacentralformoflong-horizonhumanintelligence(Chenetal.,2026a;Tieetal.,2025).Itsdifficulty
liesnotonlyinsolvingisolatedproblems,butinsustainingprogressacrossuncertainhypotheses,costlyexperiments,
failedattempts,anddelayedfeedback. Aresearchermustmaintainanevolvingunderstandingoftheproblemso
thateachattemptcanreshapewhatshouldbetriednext(Huetal.,2025). RecentLLMagentscannoweditcode,
calltools,retrieveinformation,andrunexperimentsforextendedperiods(Yaoetal.,2023b;Schicketal.,2023;Qin
etal.,2024),andsystemssuchasCodex(OpenAI,2025),ClaudeCode(Anthropic,2025),andOpenHands(Wangetal.,
2025)makesustainedprogressinrealcodebases,makingautonomousresearchanincreasinglyconcretesystems
problem.Yetlongerexecutionalonedoesnotguaranteeresearchprogress.Theopenchallengeishowanagentcan
maintainaresearchstatethatturnsmanylocalattemptsintocumulativehypothesisrefinementandverifiedartifact
improvement.
WeformalizethisproblemasAutonomousOptimization(AO),whichcapturesthecoreoperationalformofautonomous
research.InAO,anagentbeginswithaninitialartifactandaresearchobjective,thenimprovestheartifactthrough
experimentalfeedbackwithoutstep-levelhumansupervision.Thissettingisdifficultbecauseresearchfeedbackis
delayed,experimentscanbeexpensive,andfailedattemptsoftencontaininformationthatshouldguidelatersearch.
Asthehorizongrows,anagentthattreatseachtrialasanindependentlocalattemptlosesthestructureoftheresearch
process.EffectiveAOthereforerequiresapersistentresearchstatethatrecordswhathasbeentried,whatevidence
wasobtained,andhoweachresultchangesthespaceoffuturehypotheses.
Despiterecentprogress,currentagentsystemsstilldonotprovideageneralframeworkforrunningautonomous
researchoverlonghorizons(Leeetal.,2026;Louetal.,2026).Generalcodingagentscaneditcode,invoketools,and
runexperimentsformanyhours,buttheirautonomyismostlyexpressedaspersistenttaskexecution.Scientific-agent
systemsmoveclosertoresearchautomation,yetmanystillfollowpredefinedworkflowsorreviseasinglelineofwork
atatime(Luetal.,2024;Schmidgalletal.,2025;Zhangetal.,2025b).Theythereforelackthemechanismthatmakes
humanresearchcumulative:theabilitytomaintaincompetingdirections,testthemthroughconcreteexperiments(Yao
etal.,2023a;Zhouetal.,2023),interpretbothsuccessesandfailures(Huetal.,2025),andletthoselessonsreshapelater
exploration.ForAO,thekeychallengeistobuildthismechanismintotheagentsystemitself,sothatlong-running
experimentationbecomesaself-directedresearchprocessratherthananextendedsequenceoflocalattempts.
WearguethatageneralAOsystemshouldautomatethelong-horizonworkthatahumanresearchernormallyperforms
duringiterativeresearch. Startingfromanopenobjective, itshouldformresearchdirections, testthemthrough
concreteartifactchanges,andturntheresultingevidenceintomemorythatshapeslaterexploration.Progressshould
notdependonahumanrepeatedlychoosingthenextattemptorinterpretingwhatprevioustrialsmean.Instead,the
systemneedsaframeworkthatkeepsdirections,experiments,artifacts,results,andfailuresconnectedacrosstime,
turningautonomousresearchintoapersistentcycleofexplorationandverifiedimprovement.
Weintroduce
Arbor
,ageneralframeworkandopen-sourceresearchsystemforAO.Arborseparatesautonomous
researchintoalong-livedcoordinatorandshort-livedexecutors.Thecoordinatorownstheglobalresearchstateand
decideshowthesearchfrontiershouldevolve,whileeachexecutortestsonehypothesisinanisolatedworktreeand
returnsstructuredevidence.Arbormakesthistwo-levelprocesscumulativethroughHypothesisTreeRefinement
(HTR).HTRrepresentstheresearchprocessasapersistenttreeinwhicheachnodebindsahypothesis,theartifact
versionthatrealizesit,theexperimentalevidenceitproduces,andthedistilledinsightthatshouldshapelaterdecisions.
Whenexecutorresultsreturn,Arborwritesevidencebacktotheexecutednodes,abstractslocalfindingsupward,and
usestheupdatedtreetodecidewhichdirectionstoexpand,prune,ormerge,promotingacandidatetothecurrent
bestonlywhenitimprovesaheld-outevaluation. Thetreethereforeactsastheoperationalresearchstateofthe
system:itissimultaneouslythesearchfrontier,thememoryofpastattempts,andtheaudittrailforverifiedartifact
improvement.
ToevaluateArbor,weconstructsixAOtasksfromrealresearchsettingsacrossmodeltraining(Jordanandcontributors,
2025;Karpathy,2026),harnessengineering(Merrilletal.,2026;Weietal.,2025),anddatasynthesis.Eachtaskspecifies
aninitialartifact,anatural-languageobjective,atask-nativemetric,andadevelopment/testprotocolthatseparates
exploratoryfeedbackfromfinalscoring. Arborachievesthebestheld-outresultonallsixtasks,withmorethan
2.5×theaveragerelativegainofCodexandClaudeCodeunderthesametaskinterfaceandresourcebudget. On
MLE-BenchLite(Chanetal.,2024),Arborfurtherreaches86.36%AnyMedalwithGPT-5.5,thestrongestresultinour
comparison.Ablations,backbonestudies,transferexperiments,andcostanalysesshowthatthesegainscomefrom
2

Arbor’sevidence-structuredresearchprocess: hypothesesremaingroundedinexecutableartifacts,localfindings
becomereusableinsights,andlaterdecisionsaremadeoveranexplicitresearchstate.
Ourcontributionsaresummarizedasfollows:
• WeformulateAutonomousOptimization(AO)asaclassoflong-horizonresearchtasksinwhichanagentmust
iterativelyimproveanartifactunderafixedobjectiveandevaluatorwithoutstep-levelhumansupervision.
• Weintroduce ,ageneralframeworkforAOthatorganizesresearchthroughHypothesisTreeRefinement
Arbor
(HTR),pairingapersistentcoordinatorwithisolatedexecutorssothathypotheses,artifactversions,experimental
evidence,anddistilledinsightsaccumulateintoanauditableresearchstate;wereleaseitasanopen-source
researchsystem.
• WeconstructsixAOtasksfromrealresearchsettingsandshow,togetherwithMLE-BenchLite,thatArbor
deliversthestrongestheld-outgainsandthatpersistenthypothesismanagementandinsightpropagationare
thekeydriversofitsperformance.
2 RelatedWork
2.1 AutonomousResearchAgent
LLM-based automated research systems first appeared as end-to-end pipelines. The AI Scientist (Lu et al., 2024)
connectedideageneration,implementation,execution,resultinterpretationandpaperwritinginamostlyautomated
loop,whileAgentLaboratory(Schmidgalletal.,2025)organizedsimilarstagesasahuman-supervisedmulti-agent
research-assistantworkflow.Thenextwavemadethesearchprocessmoreexplicit:AIDE(Jiangetal.,2025)explored
MLengineeringasiterativecodesearch,AIScientist-v2(Yamadaetal.,2025)introducedagentictreesearchover
research plans and experiments, and multi-agent systems such as AI-Researcher, R&D-Agent (Yang et al., 2025)
and Loongflow (Wan et al., 2025) refined the literature-to-experiment loop through more specialized roles and
summarizationmechanisms.Inparallel,FunSearch(Romera-Paredesetal.,2024)andAlphaEvolve(Novikovetal.,
2025) treated LLMs as program mutation operators selected by executable fitness signals, and SciMaster (Chai
etal.,2025)broadenedautomatedresearchfromMLexperimentationtogeneral-purposescientificreasoningwith
tool-augmented,breadth-and-depthsearch.
Recentsystemsexpandtheobjectofsearchitself. MARS(Chenetal.,2026b)modularizesautomatedAIresearch
intoreflectivecomponents;AutoHarness(Louetal.,2026),Meta-Harness(Leeetal.,2026)andAHE(Linetal.,2026)
searchorevolvethecodeharnesssurroundinganagent;andDataMaster(Duetal.,2026)movesthesearchtargetto
data,usingDataTree,DataPoolandGlobalMemorytoorganizeautonomousdatadiscoveryandvalidation.Arbor
insteadstoresresearchstateinapersistenthypothesistree.Along-runningcoordinatorexpandsandupdatesthetree,
whileshort-livedexecutorsimplementindividualhypothesesinisolatedgitworktrees.Thisdesignmakeshypotheses,
failures,evidenceandmergedecisionsauditable. Italsoaddressesgapsnotedbyrecentsurveysandsandbagging
studies: weakevidencepreservation,loosedev/testdisciplineandsilentmetricchasing(Tieetal.,2025;Gasteiger
etal.,2025).
2.2 Long-HorizonAgent
Aslanguageagentshaveimproved,thekeyquestionhasshiftedfromwhethertheycancompleteisolatedtool-use
episodestohowlongtheycanremaincoherentonrealtasks(Liuetal.,2025a;Sinhaetal.,2025;Huetal.,2026a).
EarlysystemssuchasReflexion(Shinnetal.,2023)andGenerativeAgents(Parketal.,2023)extendedsingle-run
behaviorwithnatural-languagememoriesorreflectionsacrosstrials,makingexperienceaccumulationpartofthe
agentloop. Laterhuman-calibratedevaluationsmadethishorizonmeasurable: sometaskscompareagentswith
humantime-to-complete(Wijketal.,2024;Reinetal.,2025;Kwaetal.,2025),whileothers(Zhaoetal.,2025;Rank
etal.,2026)showthatagentsstillstruggletopreserveandreuseevidenceacrosslongoptimizationhistories,even
whentheenvironmentprovidesexecutablefeedback.
Recentapproachesthereforeincreasinglytreatlong-horizonagencyasaproblemofexternalizedstateorganization
rather than only prompt design. Some systems organize prior experience into persistent context, using curated
playbooks(Zhangetal.,2025c),state-adaptivetrajectoryretrieval(Huetal.,2026b),orcognitivecaches(Zhuetal.,
3

Coordinator 1 Observe 2 Ideate 3 Select 4 Dispatch Executors 5 Backpropagate 6 Decide
(long-lived) Read tree state Propose new Choose promising Send each selected Abstract insights Merge / prune /
Owns the tree and strategic search (frontier, insights, hypotheses under leaves to leaf to an isolated upward; update ancestor continue / pending
Maintains global research state constraints, priors) a chosen parent explore executor nodes and global priors
Hypothesis Tree (persistent research state)
A growing memory of ideas, evidence and insights
General Research Tasks Root Task Preserve Axis Statistics
Design efficient optimizer NS may discard useful row
M I h m y o p p d e ro e rp v l e a T r r t a a ra m in in e in i t n e g g rs recipes and 1 O Re b a s d e tr r e v e e state for LLM Training credit 6 Decide
(frontier, insights, Muon Geometry Diagnostics Merge / prune /
H En a h rn a e n s c s e E ev n a g lu in a e ti e o r n in a g nd test- constraints, priors) A m g a g tr r i e x g u a p te d a v t a e l s _ l f o a s il s hides which continue / pending Information Out
time infrastructure
Improved artifact
D G tra a e i t n n a e in S r g a y t o e n r t b h e e e v t s a te i lu s r a d t a io ta n for M L o a n L t e e P m p B o r o o d g t u t r l l e e e s n c s e l a c m s k a s L y o c c o a lla li p za se ti o in n (merged to trunk)
Accumulated insights
Model Architecture Search (priors for future search)
Design and refine model
architecture Pre-NS Conditioning
... Muon loses useful geometry Reusable constraints
before Newton-Schulz Axis-factorized Sign Update (avoid repeated failures)
Input Interface (AO) Separable updates may
preserve anisotropy
C In o it d ia e l b m a a s t e e r / i a R l e to p o improve R Ba o l w an /C ce o l a B n a is l o a t n ro c p e y M w L h P ile A (tr u e d e i t + a b d l e e c i t s r i a o c n e s)
E D a I R n d v e e s m a v s t l r e i f u s u o a s a c r r i t c o t g o i h n o u r s i n o d b a / j n e G c c o e ti a v , l e Test for 2 I P h a d y r c o p e h p o a o o th s t s e e e e n s n e p e s a w u re n n d t er D A e c v h i s e c v o e r c e u : r 3 r 2 e p 2 n r 5 e t ; s b e T e r e s v s i t n t ; g s M c f e u o r l r l g e N e : S d 3275 A C th c o e t o s i r v e d e i l n e f a a ro t v o e n r s t f i o e c r u (s se e s le b c u te d d g e le t a o v n es) L ❌ ❌ us o e c A R f a u x e l l i p I s f n u la s s ll t c - i a m g in t h i a g s t t t r i N c ix s e g w a e t lo o o n n m g -S e a t c r r h y e u n lz o d t e e s n t o ro u y g s h 5 B A u a p n b a d d s c a t g r t a k e lo c p b a t a r n in o l c s p e p ig r s i a h o to t r g s r s a n u o t p d e w e a s rd; B di e s t t t r e ib r u fu ti t o u n re search
4 Dispatch
Merged Running Failed but Pending 3 Select Executor Executor A Executor B Executor C Executor D Executors Structured Outputs
(in trunk) (selected) informative (not tried) Choose promising Short-lived executors (branch x.x) (branch x.x) (branch x.x) (branch x.x) Send each selected
V ye a t l id m a e te rg d e ( d n ) ot R (c u h n ild n in n g ode) P pr r o u m ne is d in ( g n ) ot leaves to explore r is u o n l a h t y e p d o e th n e v s ir e o s n m in ents l e e x a e f c t u o t o a r n isolated scores result insight branch
Figure2
Overallframeworkof Arbor.Apersistentcoordinatormaintainstheresearchstateasahypothesistree,iteratively
exploringideas,dispatchingexecutorstoimplementthem,andusingevaluationfeedbacktorefinethetreeandupdatethecurrent
bestartifact.
2026)sothatlaterdecisionscandrawonearlierfailuresandsuccesses.Otherspushthesameideaintothescaffold
aroundthemodel,coordinatingagentsthroughpersistentworkspaces(Chenetal.,2026a),recursivelymodifying
agentcode(Zhangetal.,2025a),orevolvingharnessesthatshapetooluseandexecutionconstraints(Louetal.,2026).
Arborfollowsthisstate-externalizationtrend,butitspersistentobjectisspecificallyaresearchtree:eachnodebindsa
hypothesis,implementationbranch,result,score,relatedworkandlearnedinsight,soprogressaccumulatesthrough
branchexpansion,insightbackpropagation,mergedecisionsandpruningratherthanthroughanever-growingcontext
window.
2.3 BenchmarkforAutonomousResearch
Research-agentbenchmarkshaveprogressedalongseveralcomplementarydirections.MLAgentBench(Huangetal.,
2024),MLE-bench(Chanetal.,2024)andMLE-Dojo(Qiangetal.,2025)evaluateagentsonexecutableML-engineering
workflowswithobjectivetaskmetrics.ScienceAgentBench(Chenetal.,2024),PaperBench(Staraceetal.,2025),and
FrontierScience(Wangetal.,2026)focusonprogrammaticdiscovery,orpaperreproductionunderexpert-designed
questionsandrubrics.RE-Bench(Wijketal.,2024),HCAST(Reinetal.,2025),AlgoTune(Pressetal.,2025),NanoGPT
speedrunning (Zhao et al., 2025), PostTrainBench (Rank et al., 2026) and Frontier-Eng (Chi et al., 2026) further
emphasizelong-horizonengineering,human-calibrateddifficulty,executablefeedbackanditerativeself-improvement.
Thesebenchmarksmeasureimportantoutcomes,butmanyevaluationsstilluseincompletesettings: somelacka
cleardev/testsplit,makingiterativesearchpronetooverfitting,whileothersrelyononeortwotasktypesandleave
generalityunder-tested. Arborthereforeevaluatesacrossmultipletasksandenforcesastricterprotocol:dataand
evaluationharnessesareimmutable,thedevsetsupportsiterativesearch,thetestsetisreservedformergeorfinal
validation,andeachexperimentistiedtobranch-levelartifactsandhypothesis-treerecords.
3 TaskFormulation
Wemodelauto-researchasaninstanceofAutonomousOptimization(AO),whichcanberepresentedasatuple
P =(M ,O,E ,E ).
0 dev test
4

ThematerialM isthemutableartifacttheagentmayinspectandmodify,typicallyacodebasetogetherwithits
0
associated data. The objective O specifies what it means for a modified material M′ to be better, for example a
metricdirectiondefinedovertheartifact’soutput. Thetwoevaluatorsinstantiatethesameobjectiveondifferent
evidence:E returnsfeedbacktheagentmayfreelyuseduringsearch,whiletheheld-outE measureswhether
dev test
thedev-drivenimprovementtransfersbeyondthefeedbackusedforexploration.LetS (M′)andS (M′)denote
dev test
thescalarscoresreturnedbythesetwoevaluatorsunderthemetricdirectionspecifiedbyO,sothatlargervaluesare
better;acandidatethatexploitsidiosyncrasiesofthedevsplitmayimproveS butisnotasuccessfulAOsolution
dev
unlessthegainalsotransferstoS .
test
Duringarun,theagentadaptivelygenerates,implements,andevaluatescandidatematerialsusingE .LetAbethe
dev
setofcandidatesproduced.Theartifact-levelgoalistoreturn
M⋆ =arg max S (M′),
test
M′∈A
subjecttotheconstraintthathypothesesandimplementationdecisionsaremadewithoutusingE asanexploration
test
oracle.
4 TheArborFramework
4.1 Overview
WeproposeArbor,ageneralframeworkforautonomousresearchundertheAOinterfacedefinedinSection3.AO
differsfromordinaryagentictooluseinthatthetargetisnotasingleresponseorcodepatch,butasustainedresearch
trajectory.Anagentmustproposehypotheses,materializethemasartifactchanges,interpretexperimentalfeedback,
anddecidewhichdirectionsshouldberefined,merged,orabandoned.Thecentraldesignproblemisthereforehowto
convertmanytransienttrialsintocumulativeresearchprogress.
Thisproblemimposesthreerequirementsonthesystemdesign:
• Researchexplorationmustbranchbecausemultiplecompetinghypothesesmaybe
Branchingwithcoherence.
plausibleatthesametime.However,unrestrictedbranchingcandegenerateintoanunstructuredlogofattempts.
Thesystemmustthereforemaintainafrontierinwhichcompetingdirectionscoexistwhileremainingorganized,
comparable,andactionable.
• Strategicdecisionsdependonevidenceaccumulatedacrossthewholerun,
Globalstrategywithlocalexecution.
whereasimplementingasinglehypothesisrequiresshort-horizoncodeediting,debugging,andevaluation.These
twolevelsshouldbeseparatedsothatlow-levelexecutiontracesdonotobscuretheglobalresearchstate, and
experimentaloutcomesremainattributabletothehypothesesthatproducedthem.
• Developmentfeedbackshouldguidehypothesissearch,butartifact-level
Explorationwithheld-outadmission.
progressshouldbeadmittedonlywhenittransfersbeyondthefeedbackusedduringexploration.Thesystemmust
thereforedistinguishexploratoryimprovementonE fromverifiedimprovementundertheheld-outevaluator
dev
E .
test
ArboraddressestheserequirementsthroughHypothesisTreeRefinement(HTR),asillustratedinFigure2.Itscentral
stateisapersistenthypothesistreewhosenodesbindtogetheraresearchhypothesis,theartifactversionthatrealizes
it,theevaluationevidenceitproduces,andthedistilledinsightthatshouldinfluencelaterdecisions. Along-lived
coordinatormaintainsthistreeastheglobalresearchstate: itobservesthecurrentfrontier,proposesrefinements,
selectspromisingleaves,integratesreturnedevidence,propagatesinsightsupward,anddecideswhethertocontinue,
prune,ormergeacandidatebranch.Short-livedexecutorstestselectedhypothesesinisolatedworktreesandreturn
compactreportscontainingscores,factualresults,distilledinsights,andartifactreferences.Aheld-outmergegate
promotes a candidate to the current best artifact only when its improvement transfers beyond the development
evaluator.Inthisway,ArbororganizesAOasevidence-structuredrefinementoveradurableresearchstaterather
thanrepeatedlocaltrial-and-error.Section4.2describesthehypothesis-treerepresentation,andSection4.3presents
thecoordinator–executorloopthatmaintainsit.
5

4.2 HypothesisTreeasResearchState
ThecenterofFigure2showsthehypothesistreethatservesasArbor’spersistentresearchstate.InAO,theintermediate
stateisnotonlythelatestartifactoritsevaluationscore,butalsothestructureofexploration:whichhypotheseshave
beenconsidered,howtheyrelatetooneanother,whatevidencetheyproduced,andwhatlessonsshouldconstrain
futuretrials. Atreeisanaturalrepresentationforthisstatebecauseitpreservesboththebranchingstructureof
researchexplorationandtheabstractionhierarchyfrombroaddirectionstoexecutableinterventions.
LetT =(V,E)denotearootedhypothesistreewithrootnoden .Eachnoden∈V isaresearchunit
0
n=⟨h ,ι ,µ ⟩,
n n n
wherethethreefieldsseparatethesemanticcontentofahypothesis,thereusableevidencederivedfromit,andthe
executablerecordthatgroundsit:
• Hypothesish n. Thehypothesisdescribesaverifiableorfalsifiableclaimabouthowthematerialshouldbe
changedtoimprovetheobjective.Itsgranularitydependsonthenodedepth:nodesclosetotherootdescribe
broadresearchdirections,whiledeepernodesspecifyconcreteinterventionsthatcanbeimplementedand
evaluatedbyanexecutor.ThisallowsArbortoorganizeexplorationasprogressiverefinementratherthanasa
flatsequenceofindependenttrials.
• Insightι n. The insight stores the reusable interpretation of evidence associated with the hypothesis. For
anexecutedleaf, itsummarizeswhatwastried, whathappened, andwhytheresultsupports, weakens, or
constrainsthehypothesis.Foraninternalnode,itabstractsovertheinsightsofitschildrenandsummarizes
thecurrentunderstandingofthatresearchdirection. Thus,ι isnotanexecutiontranscript,butacompact
n
semanticmemoryforlaterhypothesisgenerationandselection.
• Metadataµ n. Themetadataconnectsthesemantichypothesistoexecutableevidence. Itincludesthenode
status,developmentscorewhenavailable,factualresultrecord,implementationreferencesuchasagitbranch
orcommit,andoptionalbackgroundevidence. Thematerialitselfisnotduplicatedinthetree;instead,the
treestoresreferencestoexternalartifactstatesproducedinisolatedworktrees.Thiskeepstheresearchstate
compactwhileensuringthateachhypothesisremainsgroundedinaverifiableimplementation.
Thetreeseparatesinternaldirectionnodesfromexecutableleafnodes. Internalnodesmaintainabstractresearch
directionsandaccumulatedlessons, whereasleavesrepresentcandidateinterventionsthatcanbedispatchedfor
implementationandevaluation.Afteraleafisexecuted,itsscore,result,artifactreference,anddistilledinsightare
writtenbacktothecorrespondingnode.Theinsightisthenpropagatedupwardbyupdatingtheancestorsalongthe
pathtotheroot.Throughthisabstractionprocess,localexperimentaloutcomesbecomedirection-levellessonsand
eventuallycontributetoacompactglobalunderstandingoftherun.
Inthisway,thehypothesistreeservesthreerolessimultaneously.Itisasearchfrontierthatrecordswhichdirections
remainactive,validated,orpruned;along-termmemorythatstoresreusableevidencefrombothsuccessesandfailures;
andanauditableresearchrecordthatlinkseachartifactchangetothehypothesisandevidencethatmotivatedit.This
persistentstateprovidesthesubstrateonwhichthecoordinatorcanmakestrategicdecisionsacrosslong-horizon
autonomousoptimization.
4.3 HypothesisTreeRefinement
Tomaintainthetreeoveralong-horizonAOrun,Arborseparatesglobalfrontiercontrolfromlocalexperimental
execution.Apersistentcoordinator ownsthesharedtreeanddecideswheretoexpand,whichevidencetotrust,which
directionstoprune,andwhenacandidateshouldbemerged.Short-livedexecutorsareinvokedonlytotestindividual
hypotheses: eachexecutorreceivesonetreenode, materializesthecorrespondinginterventioninanisolatedgit
worktree,evaluatesit,andreturnsstructuredevidencetothecoordinator.
Duringtheresearchprocess,thecoordinatorseesthewholeresearchfrontierbutdoesnotdirectlyperformevery
low-levelimplementationstep;theexecutorperformsgroundedengineeringworkbutdoesnotmodifytheshared
treeorredirectthesearchobjective.Asaresult,exploratorycodechangesremainisolateduntiltheypassthemerge
gate,whilethetreerecordsonlydecision-relevantevidence:scores,factualoutcomes,artifactreferences,anddistilled
insights. This boundary allows Arbor to turn transient execution traces into a persistent research state without
reducingthetreetoarawlogoftoolcalls.
6

Algorithm1:
HypothesisTreeRefinement(HTR).CoordinatorownsTree;Executorownsoneworktree.
Input :P =(M0,O,E dev ,Etest),budgetB,branchingk
Output:bestartifactM⋆andhypothesistreeTree
1 initTree=({n0},∅),bn0 ←M0 ,M best ←M0
2
whileBleft∧pendingleavesexistdo
3 V ←Observe(Tree,M best ) // Observe: shape, root insight, pruned/validated lessons
4
p←chooseparentunderV; attachkpendingchildren{n(i):h(i)}←Ideate(p,V) // Ideate
5
L←pendingleavesunderSelect(V) // Select: frontier control
6 {(sn,rn,ιn,bn)}n∈L←parallelExecutor(hn,ι anc(n) ,M best ) // Dispatch
7
foreachn∈L,a∈path(n0→n)do
8 writeback(sn,rn,ιn,bn); ιa←Abstract({ιc} c∈ch(a) ) // Backpropagate
9 endforeach
10
n†←argmaxn∈Lsn // Decide: held-out merge gate, then prune
11 ifO(Etest(b n† ))>O(Etest(M best ))thenM best ←merge(b n† )
12
prunesubtreesfalsifiedby{ιn}n∈L ; persistTree
13 endwhile
14
returnM⋆←M
best
,Tree
15 ProcedureExecutor(hn,ι anc(n) ,M best ):
16
freshworktreeWn←M
best
17 repeat
18 ∆←Implement(hn,ι anc(n) ,Wn); (sn,rn)←E dev (apply(∆,Wn)) // repair ∆ only; hn is fixed
19
untilrunok∧hn -pathexercised,orcapreached
20
return(sn,rn,Distill(hn,∆,rn),commit(Wn))
4.3.1 Coordinator:Evidence-AwareFrontierControl
ThecoordinatorupdatesTreethrougharepeatedsix-stepprocedure: Observe,Ideate,Select,Dispatch,Back-
propagate,andDecide. Eachstepoperatesonthetreethroughanarrowinterfaceforaddingnodes,dispatching
executors,updatingnodeevidence,propagatinginsights,pruningsubtrees,andmergingverifiedbranches.Thekey
pointisthattheLLMpolicychooseshowtointerprettheresearchstate,whilealldurablestatechangesareexpressed
ascontrolledmutationsofthehypothesistree.
Atthebeginningofeachcycle,thecoordinatorre-groundsitselfinthecurrentresearchstatebyreadinga
Observe.
structuredprojectionofTree,includingactivefrontiernodes,recentlyreturnedevidence,ancestorinsights,andthe
currentbestartifactM .Thisstepmakesthetreetheauthoritativestateaftercontextcompressionandprevents
best
thecoordinatorfromrelyingonalossyconversationalhistory.
Thecoordinatorselectsaparentnodeandproposesasmallsetofchildhypothesesbeneathit. Eachchild
Ideate.
representsarefinement,alternative,orcorrectionoftheparenthypothesisandisinitializedasapendingnode.Unlike
free-formbrainstorming,ideationisconditionedonaccumulatedtreeevidence:validatedinsightsprovideassumptions
tobuildon,prunednodesprovidenegativeconstraints,andrecentexecutorreportssuggestwhichinterventionsare
feasibleorunder-tested.
Thecoordinatorchoosespendingnodestoexecutenext.Selectionbalancestheexpectedutilityofahypothesis
Select.
withtheevidencealreadyaccumulatedarounditsancestorsandsiblings.Adirectionmaybeselectedbecauseithas
strongpriorevidence,becauseitssiblingsexposeanunresolvedambiguity,orbecauseitsfailurewouldclarifyan
importantassumption.Thusselectionisnotmerelyscoremaximization;itisfrontiercontrolunderpartialanddelayed
feedback.
Selectedhypothesesaredispatchedtoindependentexecutors. Eachexecutormaterializesitsassigned
Dispatch.
hypothesisinafreshworktree,evaluatesthemodifiedartifactonE ,andreturnsacompactreportcontainingthe
dev
devscore,factualresult,distilledinsight,andbranchreference. Parallelexecutionofsiblinghypothesesprovides
comparativeevidencewithinthesameresearchdirection,whichisusefulforlaterpruningandabstraction.
Whenexecutorreportsreturn,thecoordinatorwritestheirevidenceintothecorrespondingleaf
Backpropagate.
nodes and updates insights along the path to the root. The propagated signal is not only a scalar score. It also
includescausalattributions,applicabilityconditions,andreusablelessonsextractedfromtheexperiment.Aleaf-level
observationsuchasadata-interfacemismatchcanthereforebecomeadirection-levelconstraint,andeventuallya
globalpriorthatshapesfutureideation.
7

Afterthetreeabsorbsthenewevidence,thecoordinatordecideswhethertocontinueexpandingadirection,
Decide.
pruneafalsifiedsubtree,stoptherun,orattempttomergeacandidatebranch.Promotionisguardedbyaheld-out
mergegate:thecandidateisevaluatedonE inafreshworktreeandismergedintoM onlyifitimprovesover
test best
thecurrentbestundertheobjectiveO.ThisgateseparatesexploratorysuccessonE fromverifiedartifact-level
dev
progress.
4.3.2 Executor:Hypothesis-BoundExperimentation
Anexecutorimplementsonelocalexperimentforoneassignedhypothesis.Givenanoden,itreceivesthehypothesis
h ,relevantancestorinsights,thecurrentbestartifact,andthedevelopmentevaluatorE .Itthencreatesanisolated
n dev
worktree,appliestheminimalinterventionneededtorealizeh ,runstheevaluator,inspectsfailuresorinactivecode
n
paths,andrepairsitsownimplementationwhennecessary.Thislocalloopmayinvolvemultipleeditsandreruns,but
itremainsboundtotheassignedhypothesis.
Theexecutorreturnsexactlytheevidenceconsumedbythecoordinator’streeinterface: acomparabledevscore
forselection,afactualresultforfutureideation,adistilledinsightforbackpropagation,andabranchreferencefor
held-outverification. Thiscontractisimportant. Ifanexecutorwereallowedtochangethehypothesiswhenthe
metricstalls,thereturnedscorewouldnolongerbeevidenceabouttheassignednode,andancestor-levelinsights
wouldbecomedifficulttointerpret.Bykeepingexecutorshypothesis-bound,Arborkeepslocalengineeringflexibility
whilepreservingthesemanticmeaningoftreeupdates.Algorithm1summarizesthefullHTRprocedure.
5 Experiments
5.1 AOTaskSuite
TotestwhetherArborcanimproverealresearchartifacts,wefirstconstructseveralAOtasksfromactualresearch
tasks. Each task consists of an initial material M , a natural language objective O, an executable development
0
evaluatorE ,aheld-outtestevaluatorE ,andatask-nativemetric.Table1givesacompactsummary;thetask
dev test
detailsaredescribedbelow.
Model training. The model-training tasks evaluate whether an agent can improve training algorithms under
expensiveexperimentalfeedback.In ,weuseNanoGPT-Bench(Jordanandcontributors,2025),a
OptimizerDesign
benchmarkforacceleratingNanoGPTtraining.TheinitialmaterialistheofficialtunedMuonoptimizerbaselinedis-
tributedwithNanoGPT-Bench,andtheobjectiveistoreachthetargetNanoGPTvalidationlossinasfewoptimization
stepsaspossible.ThedevelopmentevaluatorusesthestandardNanoGPT-Benchtaskduringsearch,whilethetest
evaluatorrerunstheselectedoptimizerwithtwoheld-outrandomseedsandreportstheaveragenumberofsteps.
In
ArchitectureDesign
,weusetheautoresearchbenchmark(Karpathy,2026). TheagentmodifiesagivenLLM
trainingcodebase,withthegoalofobtainingalowerfinallossunderafixedtimebudget.Thetestevaluatoragain
averagestwoheld-outrandom-seedruns.
Harnessengineering. Theharness-engineeringtasksevaluatewhetheranagentcanimprovethecontrollogic
aroundanotheragent. In ,theinitialmaterialisthestandardofficialterminal-agentcodebase
Terminal-Bench2.0
forTerminal-Bench2.0(Merrilletal.,2026),andtheobjectiveistoimprovepassrateonterminal-basedcodeand
shelltasks. Westratifythe89tasksbydifficultyinto36developmenttasksand53held-outtesttasks,ratherthan
optimizingonthefullbenchmark.In ,theinitialmaterialisourstandardminimalReAct-stylesearch
BrowseComp
harness(Yaoetal.,2023b;Weietal.,2025).Theobjectiveistoimproveansweraccuracyonbrowsingquestions;the
developmentandtestsetsare50and300non-overlappingBrowseCompquestions,respectively.
Datasynthesis. Thedata-synthesistasksevaluatewhetheranagentcanimproveagenerationpipelinewhose
outputisjudgedbydownstreammodelbehavior. In ,theinitialmaterialisahand-
Search-AgentDataSynthesis
designedpipelineforgeneratingsearch-agentquestionsfromseedknowledge.Developmentuses50seeditemsand
testuses100disjointseeditems.In ,theinitialmaterialisahand-designedpipeline
Math-ReasoningDataSynthesis
forgeneratingAIME-stylereasoningproblems;developmentgenerates50problemswith10seedandtestgenerates96
problemswith12seed.Bothtasksarescoredbythemeanpass@4−pass@1gapunderastrongGPT-5.5-basedReAct
evaluator.Thismetricrewardsproblemsthatarenotsolvedimmediatelybutcanbesolvedwithadditionalattempts.
8

CompactsummaryoftheAOtasks.DetailedtaskdefinitionsaregiveninSection5.1.
Table1
Type Task Initialmaterial Metricandsplit
ModelTraining OptimizerDesign NanoGPT-Bench;tunedMuonbaseline Stepstotargetloss(↓);
testaveragestwoseeds
ModelTraining ArchitectureDesign autoresearchLLMtrainingcodebase Finalloss(↓);test
averagestwoseeds
HarnessEngineering Terminal-Bench2.0 Officialterminal-agentcodebase Passrate(↑);36dev/53
testtasks
HarnessEngineering BrowseComp MinimalReAct-stylesearchharness Accuracy(↑);50dev/300
testquestions
DataSynthesis Search-AgentDataSynthesis Hand-designedsearch-datapipeline Meanpassgap(↑);50dev
/100testseeds
DataSynthesis Math-ReasoningData Hand-designedmath-datapipeline Meanpassgap(↑);50dev
Synthesis /96testproblems
5.2 ExperimentalSetup
Benchmarks. Ourevaluationusestwocomplementarytypesofbenchmarks. ThefirstistheAOTaskSuitein
Section5.1,whichconsistsofrealresearchtaskswithtask-specificmaterials,objectives,developmentevaluators,and
held-outtestevaluators.ThesecondisMLE-BenchLite,along-horizonmachinelearningengineeringbenchmark
derivedfromMLE-bench(Chanetal.,2024),whichallowscomparisonagainstestablishedbenchmarksystemsunder
theofficialtasksetupandreportingprotocol.
Baselines. Fortherealresearchtasks,wecompareagainsttwostrongcoding-agentbaselines: Codex(OpenAI,
2025)usingGPT-5.5andClaudeCode(Anthropic,2025)usingClaudeOpus4.6. Eachbaselinereceivesthesame
initialmaterial, objective, evaluator, andresourcebudgetasArbor, andisallowedtoinspectfiles, editcode, run
experiments,anditerateuntilthebudgetisexhausted.ForMLE-BenchLite,wecompareagainstreportedbenchmark
systems, including AIDE (Jiang et al., 2025), ML-Master (Liu et al., 2025b) and ML-Master 2.0 (Zhu et al., 2026),
AIRA-dojo(Toledoetal.,2025),InternAgent(Team,2026),R&D-Agent(Yangetal.,2025),Famou-Agent2.0(Lietal.,
2025),MARS(Chenetal.,2026b),Leeroo(Nadafianetal.,2026),AIBuildAI(Zhangetal.,2026),LoongFlow(Wanetal.,
2025),andAI-Scientist-stylesystems(Luetal.,2024;Chenetal.,2026a).ThebaselinenumbersinTable3areadopted
fromtheofficialMLE-BenchleaderboardandtheAI-ScientistpaperChenetal.(2026a).
Metrics. Wereportnativetaskmetricsinthemainresults,usingthedirectionindicatedinTable1.Forcross-task
averagesandablations,wealsoreportanormalizedheld-outimprovementovertheinitialmaterialafterorientingall
metricssolargerisbetter.For∆rows,percentage-valuedmetricsuseabsolutechanges;non-percentagemetricssuch
asstepsandlossusetherelativeimprovementbelow:
S˜ (M⋆)−S˜ (M )
∆ (M⋆)= test test 0 ,
test |S˜ (M )|+ϵ
test 0
whereS˜isthenativescoreforhigher-is-bettermetricsandthenegatednativescoreforlower-is-bettermetrics.To
measurereliability,weruneachstochasticmethodthreetimesandreportAvg@3withstandarddeviationunless
otherwisespecified.ForMLE-BenchLite,wereporttheofficialbenchmarkmetrics,includingvalid-submissionrate,
above-medianrate,any-medalrate,andmedalbreakdown.
Implementationdetails. Unlessotherwisenoted,boththecoordinatorandexecutorsuseClaudeOpus4.6asthe
backbonemodel.Allreal-research-taskruns,includingCodex(OpenAI,2025),ClaudeCode(Anthropic,2025),and
Arbor,usea48-hourwall-clocklimit.Tokeepthetwosingle-agentbaselinesrunningoverthislonghorizonwithout
manualintervention,welaunchCodexandClaudeCodethroughtheirofficial/goalmode,whichletseachagent
autonomouslysustainalong-runningtaskandavoidmid-trajectoryinterruptions;Arborislaunchedthroughitsown
coordinatorloop.ThedefaultArborbudgetis20coordinatorcycleswithmaximumtreedepth2.Executorparallelism
isboundedbytheavailableevaluatorresources,andallwall-clocktime,tokenusage,andevaluatorcallsarecounted
9

Mainresultsonrealresearchtasks.Eachtaskreportsnativedevelopmentandheld-outtestmetricsfortheinitialmaterial,
Table2
single-agentbaselines,andArbor;thetasklabelshowsthenativemetricdirection.Shaded∆rowsreportrelativeimprovements
overtheinitialmaterialforModelTrainingtasks,andabsolutechangesforallothertasks.
Initial Codex ClaudeCode Arbor(Ours)
Type Task
Dev Test Dev Test Dev Test Dev Test
Optimizer
Design 3325 3325 3325 3325 3275 3287.5
3225 3237.5
Model (steps↓)
Training ∆vs.init – – +0.00% +0.00% +1.50% +1.13% +3.01% +2.63%
Architecture
Design 1.096 1.098 1.089 1.083 1.033 1.033
1.029 1.028
(loss↓)
∆vs.init – – +0.64% +1.37% +5.75% +5.92% +6.11% +6.38%
Terminal-Bench2.0
58.33 69.81 63.89 73.59 71.70 72.22
(pass↑) 75.00 77.36
Harness
∆vs.init – – +5.56 +3.78 +16.67 +1.89 +13.89 +7.55
Engineering
BrowseComp
52.50 45.33 57.50 50.00 55.00 53.33
(acc.↑) 72.50 67.67
∆vs.init – – +5.00 +4.67 +2.50 +8.00 +20.00 +22.34
Search-Agent
4.00 5.00 12.00 9.00 12.00 12.00
(gap↑) 16.00 18.00
Data
∆vs.init – – +8.00 +4.00 +8.00 +7.00 +12.00 +13.00
Synthesis
Math-Reasoning
2.00 1.04 6.00 6.25 8.00 8.33
(gap↑) 24.00 20.83
∆vs.init – – +4.00 +5.21 +6.00 +7.29 +22.00 +19.79
whencomparingagainstbaselines.Thesameprompt-leveltaskdescriptionisusedacrossmethods;Arborreceivesno
task-specificsearchstrategybeyondtheadapterthatrunstheevaluatorandparsesscores.ForMLE-BenchLite,every
taskisoptimizedonasingleNVIDIAA100GPUundertheofficialbenchmarkresourcebudget.
5.3 MainResultsonRealResearchTasks
Table2comparesArborwithCodexandClaudeCodeonsixrealresearchtasks.Wefocusontwoobservations.
Arborgivesstrongerandmoregeneralheld-outgains. Arborobtainsthebestheld-outresultonallsixtasks,
coveringthreedifferenttypesofresearchartifacts:trainingalgorithms,agentharnesses,anddata-generationpipelines.
Thesamecontrollerandhypothesis-treedepthareusedacrossthesetasks;onlytheinitialmaterialandevaluatorare
changed.Thissuggeststhattheimprovementcomesfromthesearchprocedureitselfratherthanfromtask-specific
tuning. Thegainsarealsolargerthanthoseofsingle-trajectorycodingagents. OnBrowseComp,Arborimproves
held-outaccuracyfrom45.33to67.67,whileCodexandClaudeCodereach50.00and53.33.OnMath-Reasoning
DataSynthesis,Arborimprovestheheld-outpass-gapby19.79points,comparedwith5.21and7.29pointsforCodex
andClaudeCode.Thebaselinescanstillmakeprogress,buttheirgainsaresmallerandlessstableacrosstasktypes.
Thissupportsourmainhypothesis:inAO,thebottleneckisnotonlylocalcodeediting,butorganizingmanytrials
intoacoherentexplorationprocess. ThecostresultsinSection5.8furthershowthatArborachievesthesegains
withoutrelyingonsubstantiallylargertokenbudgets.
Thedev/testsplitexposesoverfittingduringautonomoussearch. Developmentfeedbackisusefulforguiding
exploration,butitisnotareliableadmissioncriterion.BecausetheagentrepeatedlyoptimizesagainstE ,itcan
dev
overfittothedevelopmentsplitorexploitevaluator-specificpatterns.ThisisespeciallyvisibleonTerminal-Bench:
ClaudeCodeachievesthehighestdevelopmentscore(75.00),butitsheld-outscoredropsto71.70;Arborhasalower
developmentscore(72.22),butreachesthebestheld-outscore(77.36).Thisgapmotivatestheheld-outmergegatein
Arbor.WeuseE toguidehypothesissearch,butpromoteacandidateartifactonlywhenitimprovesE .This
dev test
separatesexploratoryfeedbackfromverifiedprogress.Italsomakesdev/testdisagreementinformative:ahigh-dev,
10

MLE-BenchLiteresultsundertheofficialevaluationprotocol.Allentriesarepercentages.
Table3
Method Model Validsub. Abovemedian Bronze Silver Gold Anymedal
InternAgent DeepSeek-R1 100.00 78.79 10.61 16.67 34.85 62.12
ML-Master DeepSeek-R1 100.00 74.24 4.55 13.64 30.30 48.48
AIRA-dojo o3 100.00 70.45 7.95 12.73 34.32 55.00
ML-Master2.0 DeepSeekV3.2-Spe 100.00 84.85 13.64 31.82 30.30 75.76
R&D-Agent GPT-5 77.27 74.24 12.12 22.73 33.33 68.18
Famou-Agent2.0 Gemini-2.5-Pro 100.00 86.36 15.15 19.70 40.91 75.76
MARS Gemini-3-Pro 100.00 89.39 6.06 15.15 53.03 74.24
Leeroo Gemini-3-Pro 68.18 68.18 18.18 19.70 30.30 68.18
AIBuildAI Claude-Opus-4.6 100.00 81.82 13.64 25.76 37.88 77.27
AIDE Gemini-3-Flash 77.27 54.55 4.55 9.09 31.82 45.45
LoongFlow Gemini-3-Flash 77.27 77.27 12.12 25.76 39.39 77.27
Codex GPT-5.5(xhigh) 100.00 81.82 1.52 19.70 46.97 68.18
AI-Scientist Gemini-3-Flash 100.00 86.36 18.18 31.82 31.82 81.82
Arbor Gemini-3-Flash 100.00 86.36 13.64 27.27 40.90 81.82
Arbor GPT-5.5 100.00 95.45 0.00 9.09 77.27 86.36
low-testcandidateistreatednotasasuccess,butasevidencethatthecurrentdirectionmaybeexploitingthefeedback
signalratherthanproducingatransferableimprovement.
5.4 ResultsonMLE-BenchLite
WealsoevaluateArboronMLE-BenchLiteundertheofficialprotocol.UnlikeourAOtasksuite,thisbenchmarkfixes
thecompetition-styleMLtasks,scoringrules,andmedalthresholds,soittestswhetherthesamecontrollercanturn
repeatedexperimentsintostrongerrunnablesubmissions.Arborusesthesamecontrollerasbefore,addingonlyan
adapterforworkspacesetupandsubmissionformatting.Table3reportstheresults.
WithamatchedGemini-3-Flashbackbone,Arborreaches100%validsubmissions,86.36%above-medianrate,and
81.82% any-medal rate, tying the best same-backbone any-medal result while obtaining a higher gold rate than
AI-ScientistandLoongFlow.ReplacingthebackbonewithGPT-5.5,withoutchangingthecontroller,depth,scheduler,
oradapter,furtherraisesany-medalto86.36%andgoldto77.27%,thehighestvaluesinTable3.Theseresultssuggest
thatthehypothesis-treeorganizationtransfersbeyondourconstructedAOtaskstoestablishedlong-horizonML
engineeringbenchmarks.
5.5 BackboneGenerality
WenexttestwhetherArbor’sgainsaretiedtoaparticularbackbonemodel. Werepeatrepresentativerunswith
differentbackbones.AsshowninFigure3(a),Arborisnottiedtoasinglefrontiermodel:evenwithGemini-3-Flash,
a lighter backbone than the Claude and GPT variants, the same controller still improves both browsecomp and
MLE-BenchLite.ThissuggeststhatHTRprovidesamodel-agnosticstructureforexplorationandmemoryratherthan
dependingonaspecificmodel.
Wealsonoticethatbackboneeffectsaretask-dependent.AlthoughHTRprovidesacommonstructureforexploration
andmemory,finalperformanceismediatedbythecompatibilitybetweenamodel’scapabilitiesandthetaskrequire-
ments.ClaudeOpus4.6performsbestonBrowseComp,whereimprovingasearchharnessreliesheavilyonbroad
reasoninganderrordiagnosis.Incontrast,GPT-5.5performsbestonMLE-BenchLite,wheregainsaremoreclosely
tiedtoML-engineeringknowledge,includingdataprocessing,trainingrecipes,andleaderboard-orientedoptimization.
Thus,Arborismodel-agnosticattheframeworklevel,butitsempiricalceilingdependsontask–backbonefit.
11

100
75
50
25
0
BrowseComp BrowseComp MLE-Lite MLE-lite
dev test any-medal above-median
)%(
erocs
a Backbone sensitivity across tasks
Gemini 3 Flash Claude Opus 4.6 GPT-5.5 95.5
90.9 81.881.8 86.4 86.4 80
72.5 67.7
62.5 60
57.0
50.0 52.0
40
20
0
BrowseComp DeepSearch QA HLE
(used) (OOD) (OOD)
)%(
erocs
b Evolved-harness transfers
Δ +8.0 Init After run
Δ +22.3 69.0
67.7 61.0
45.3 Δ +6.0
31.5
25.5
Figure3
Backbonegeneralityandcross-tasktransfer. (a)Arborisrerunwithdifferentbackbonemodelswhilekeepingthe
controller,evaluatorbudget,andtaskadaptersfixed. ABrowseComp-evolvedsearchharnessisfrozenandevaluatedon
(b)
held-outsearch-agenttaskswithoutfurthertask-specificoptimization.
Table4
ComponentablationsonMLE-BenchLite(ClaudeOpus4.6
Table5
Arbor’snodestatistics.Dev+meansnodesthat
backbone).Entriesarepercentages. improveoverthebaselineonthedevset.
Valid Above Any Node Opt. Arch. Terminal Browse Search Math
Variant Bronze Silver Gold
sub. median medal num. Design Design Bench Comp Agent Reason.
FullArbor 100.00 90.91 4.55 27.27 50.00 81.82 All 26 150 17 26 15 15
w/otree 100.00 72.72 9.09 22.73 31.82 63.64 Dev+ 13 15 7 10 10 6
w/oinsightfeedback 100.00 77.27 4.55 13.64 36.36 54.54 Merged 2 9 3 3 4 4
5.6 Cross-TaskIdeaTransfer
Astrongertestofgeneralityiswhetheranoptimizedartifacttransfersbeyondthebenchmarkusedforsearch.Thisis
importantforauto-researchandauto-harnesssystems:anagentmayimproveonasourceevaluatorbyexploiting
benchmark-specificpatternsratherthandiscoveringgenerallyusefuldesignchanges.
Wethereforeevaluatetransferintheharness-engineeringsetting. ArborisfirstrunonBrowseComp,usingonly
BrowseCompdevelopmentfeedbacktopropose,implement,andmergesearch-harnesschanges.Aftertherun,we
freeze the resulting harness and evaluate it directly on two unseen search-agent tasks, HLE and DeepSearchQA,
withoutfurthertask-specificoptimization.
Figure3(b)showsthatthelearnedharnesstransfers.TheoptimizedharnessimprovesBrowseCompheld-outaccuracy
from45.33%to67.67%.Moreimportantly,thesamefrozencodebasealsoimprovesHLEfrom25.50%to31.50%and
DeepSearchQAfrom61.00±6.76%to69.00±6.41%. SincethesetwotasksareneverusedduringBrowseComp
optimization,thegainsindicatethatArborcandiscoverharness-levelchangesthatsurviveashiftintaskdistribution,
ratherthanonlyfittingthesourcebenchmark.
5.7 Ablations
WeablatethetwocomponentsmostcentraltoHTRonMLE-BenchLite:thehierarchicalhypothesistreeandinsight
feedback.Thew/otreevariantreducessearchtoaflatexperimentqueue,withallexperimentsattacheddirectlytothe
root.Thew/oinsightfeedbackvariantkeepsthetreestructurebutdisablesupwardpropagationofdistilledlessons.
Bothvariantsusethesametoolaccess,workspacebudget,evaluationprotocol,andClaudeOpus4.6backboneasthe
fullsystem.
HTRimprovesrefinementratherthanexecutability. Table4showsthatallvariantsobtain100%validsub-
missions,indicatingthattheablationgapisnotcausedbybasicexecutionfailure.Thedifferenceinsteadappearsin
outcomequality.FullArborreaches81.82%AnyMedal,comparedwith63.64%forw/otreeand54.54%forw/oinsight
feedback.ThesamepatternappearsinstrongercategoriessuchasAboveMedian,Silver,andGold.Thissuggeststhat
HTRmainlyimproveslater-stageresearchrefinement:oncearunnablesolutionexists,thetreehelpstheagentdecide
whichdirectionstoextend,revise,orabandon.
12

2000
1000
500
250
100
50
10
5
2
0
20 50 100 200 400
total tokens (M, log scale)
)%(
niag
tuo-dleh
evitaler
Token budget vs. relative held-out gain
Codex Claude Code Arbor
Tokenbudgetandrelativeheld-outgainacrosscompletedAOcostlogs.Tokentotalssuminputandoutputtokens;for
Figure4
Arbor,thetotalfurthersumscoordinatorandexecutorusage.They-axisreportspercentimprovementovereachtask’sinitial
held-outscore.
Thetreeisusefulonlywhenevidencecanaccumulateoverit. Removinginsightfeedbackwhilekeepingthe
treecausesalargerdropthanremovingthetreeentirely.Thisresultsuggeststhathierarchyaloneisnotsufficient.A
treewithoutpropagatedlessonscanstillorganizeexperimentssyntactically,butitdoesnotprovidethesemantic
memoryneededforlaterdecisions. Incontrast,fullArborusesthetreeasasubstrateforaccumulatingevidence:
leaf-levelresultsareabstractedintodirection-levellessons,whichthenconstrainfutureideationandselection.
Treestructureandinsightfeedbackarecomplementary. Thefullsystemoutperformsbothablations,indicating
thatthetwocomponentsaddressdifferentpartsofthesearchproblem.Thetreedefineswherecompetinghypotheses
arestoredandcompared,whileinsightfeedbackdetermineswhatreusableinformationiscarriedforward. Their
combinationallowsArbortoconvertlocalexperimentaloutcomesintopersistentconstraintsonfuturesearch,rather
thantreatingeachexperimentasanisolatedtrial.
5.8 TokenConsumptionandSearchCost
WefurtherexaminewhetherArbor’sgainsmainlycomefromincreasedmodelbudget.Figure4reportstotaltoken
consumptionandrelativeheld-outgain,whileTable5summarizesthecorrespondingtreetraces.
Structuredsearchratherthanlargersampling. Acrossthesixcompletedcostlogs,Arboruses20.12M–43.19M
tokens,acomparablescaletothesingle-trajectorybaselines.Withinthisbudget,Arborachieveslargerheld-outgains
onmosttasks.Thissuggeststhattheimprovementisnotsimplyduetospendingsubstantiallymoretokens,butto
howthebudgetisorganized:tokensareusedtomaintaincompetinghypotheses,runisolatedexecutions,compare
evidence,andupdatethesearchtree.
Dev improvements are filtered by held-out admission. Table 5 also shows that many nodes improve the
developmentscore,butonlyasmallersubsetaremerged.Thisgapisexpected.Adev-improvingnodemaystillbe
worsethanthecurrentbestartifact,ormayoverfitthedevelopmentevaluatorandfailtotransfertotheheld-outtest.
Themergegatethereforepreventslocaldevelopmentgainsfrombeingmistakenforartifact-levelprogress.Inthis
sense,thetreetracerecordsbroadexploration,whiletheheld-outgateadmitsonlyverifiedimprovementsintothe
finalartifact.
6 Discussion
WeanalyzeArbor’sinternalresearchtracestounderstandhowautonomousresearchprogressesoncetheagentstarts
runningexperiments. Wefocusonthreequestions: howhypotheseschangeovertime(Section6.1),whenuseful
13

Optimizer Design Architecture Design Terminal-Bench 2.0
3237.5 1.028
77.4 71.7 100%
1.033
3287.5
50%
0
BrowseComp Search-Agent Math-Reasoning
67.7 18.0 20.8
100%
12.0
50%
8.3
53.3
0
0 25 50 75 100 0 25 50 75 100 0 25 50 75 100
experiment progress (% of run elapsed)
)niag
ved
lanif
s'robrA
fo
%(
niag
ved
edon-rep
Arbor Claude Code admitted node rejected node held-out test best
(onepanelpertask).Curvesshowthebest-so-fardevelopmentgainoverthe
Figure5 ExplorationefficiencyonthesixAOtasks
run,normalizedtoArbor’sfinalgain,soArbor(solid)endsat100%andtheClaudeCodebaseline(dashed)atitsownrelative
ceiling.Starsmarkeachmethod’sheld-outtestmaximum,annotatedwiththetestscorefromTable2.
improvementsappear(Section6.2),andwhatkindsofideastheHypothesisTreeproduces(Section6.3).
6.1 HypothesisRefinementAnalysis
WeanalyzetheBrowseComphypothesistree,reportingthemainhypothesisshifts,thenodesthattriggeredthem,
andthefinaldesignselectedbythemergegate.Figure6tracesallthreecontractionsoftaskunderstandingalongside
theexperimentalnodesthatdroveeachtransition.Wefindthat:
Therunbeginsfromacoarsehypothesisandusesthefirst
Earlynodestestwhetherabroadmechanismholds.
experimentstoconfirmorrejectit.InBrowseComp,theinitialhypothesisisthatsearchagentsproducenear-miss
answersbymatchingsalientcueswhilemissingfine-grainedconstraints;constraint-decomposedverificationand
hostile-contradictioncheckingbothimprovedevelopmentaccuracy,confirmingthatfine-grainedanswercheckingis
avalidsourceofgain.
Onceamechanismisconfirmed,thetree
Laternodeslocalizethebottleneckbyprobingthemechanism’sboundary.
testswhereitstopsworkingratherthanpushingitfurther.InBrowseComp,theverifiernodescanjudgecandidates
producedbythesearchprocessbutrarelyrecovercandidatesthatwereneversurfaced,andpartofthehostile-verifier
gaincomesfromanswernormalizationratherthanreliableevidencediscovery. Thisshiftsthemaindesigntarget
fromstricterverificationtobroaderevidencecoverage.
The accumulated
Ancestor insights compress these results into the constraints that shape the final design.
positiveandnegativefindingsdefinewhatthesuccessfuldesignmustsatisfy.InBrowseComp,theevidence-dossier
aggregatorpreservescandidatesandsupportingevidenceacrossindependentrollouts,recoveringcorrectanswers
thatappearinonlyaminorityoftrajectories;follow-upnodesthenruleoutpersona-diverserollouts(whichonly
rerankwithinthesameretrievalfrontier),thesearch-augmentedjudge(whichoverfitsdevelopmentquestions),and
shareddecomposition(whichreducestrajectoryindependence).ArborthuslearnsthatBrowseCompbenefitsfrom
sharingevidencewhilekeepingsearchtrajectoriesindependent.
Takeaway. HypothesisrefinementinHTRisa deepeningoftaskunderstanding :earlynodestestbroadmechanisms,
laternodesidentifytheirlimits,andancestorinsightssummarizetheseresultsintoconstraintsforthenextroundof
proposals.Thisconstraintaccumulationisthecoreprocess-levelbenefitoverflattrial-and-error.
14

Task Understanding Evolution
Verification Problem Candidate Problem Evidence Sharing
Agents commit to near-miss Verification cannot fix what was Diversity Rollouts share retrieval failures;
answers matching salient cues but Verifier never retrieved diversity of prompts/personas
is not
missing fine-grained constraints confirms, reshuffles within same frontier
equal to
not
Fix attempted Fix attempted evidence What was ruled out
corrects
Decompose question into atomic K=5 independent ReAct rollouts + reach dianPersona diversity
constraints; run per-constraint dossier aggregator scoring by Search-augmented judge
verification passes constraints, not majority vote Shared decomposition
Key finding Key finding Fix adopted
Verifiers confirm existing wrong Correct answers appear in minority Two-round flow — round 1
candidates when search budget is rollouts; evidence dossiers are Independent, round 2 agents read
exhausted; part of the gain comes required to recover them Prior answers + dossiers
from answer normalization
Experiment Nodes
N1.1 N2.1 N3.1 N5.1 N7.1 N6.2 N8.1
Constraint Hostile Dossier Persona Decompose- Search- Two-round
Verifier Verifier aggregator rollouts execute aug. judge sharing
Earlier 60.0% 60.0% 65.0% 70.0% 60.0% 75.0% 72.5% Later
purned purned merged purned pruned purned merged
(informative) (informative) (drives shift) (informative) (uninformative) (informative) (drives shift)
EvolutionoftaskunderstandingacrosstheBrowseComprun.Eachupper-tierboxstatesthecurrentproblemframing,the
Figure6
fixattempted,andthemechanisticfindingthatdrovethenextshift.Thelowertiershowstheexperimentalnodesbehindeach
transition.
6.2 SearchEfficiencyAnalysis
Weanalyzewhenthebestcandidatesappearduringarun,usingeachnode’sexecutiontimeanddevelopmentgain.
Wefindthat:
Strongcandidatesoftenappearafterthesearchstatehasaccumulatedconstraints.
Acrosstasks,Arborfrequently
reachesitsbestcandidateinthemiddleorlaterpartoftherun.Theseimprovementsaresupportedbyearliernodes
thatidentifyusefulmechanisms,ruleoutweakvariants,andnarrowthedesignspace.
InBrowseComp,thefinalevidence-sharingdesignappears
Laterproposalsaremoretargetedthanearlyproposals.
onlyafterseveralfailedorpartiallysuccessfulverifiervariantsestablishthatfine-grainedcheckingmatters,that
candidatecoverageisthebottleneck,andthatjudge-sidesearchandshareddecompositionintroducenewfailure
modes.Thefinalproposalisthereforegeneratedfromamoreinformativeresearchstatethantheinitialproposals.
Thetreeimprovessearchbychangingtheproposaldistributionovertime.Arbordoesnotsimplyallocatebudget
uniformlyoverindependentattempts:itslaternodesareconditionedonaccumulatedevidencefromancestorsand
siblings.Successfulmechanismsbecomepriors,failedvariantsbecomenegativeconstraints,andpartialgainsbecome
startingpointsforrefinedhypotheses.
Takeaway. Earlierexperimentspersistentlyreducethearbitrarinessoflatersearch,placingmid-to-lateimprove-
Therelevantnotionofefficiencyiswhetherthesamebudgetproducesaless
mentsonahigherinformationbaseline.
repetitiveandmoreconstrainedevidencechain,ratherthanrunninglongenoughtostumbleontoaresultbychance.
6.3 IdeaQualityAnalysis
Weanalyzerepresentativeideasgeneratedacrossmodeltraining,harnessengineering,anddatasynthesistasks,classi-
fyingeachbyitsgranularity,implementationtarget,andrelationtopreviousevidence.Figure7showsrepresentative
examples.Wefindthat:
15

BrowseComp—harnessengineering Search-Agent—datasynthesis
➤RunindependentReActrollouts,thenselecttheanswerwhoseevidence ➤Stripentitysurfaceformsbeforegenerationsothemodelcannotcopy
dossiercoversthemostquestionconstraints,ratherthantakingamajority answertokensfromthequestion;re-injectobfuscatedaliasesonlyatretrieval
vote. time.
➤Inthesecondround,shareonlyanswercandidatesandtheirevidence ➤Aftergeneratingacandidatetask,haveaseparateagentattemptitadver-
dossiersacrossagents—neverplans,personas,ordecompositions. sariallyanddiscardanytasksolvedonthefirsttry.
Math-Reasoning—datasynthesis ArchitectureDesign—modeltraining
➤Instantiateeachproblemfamilyfromaparametrictemplatewithran- ➤Bracketwarmdownschedulelengthasanindependentknobandtest
domisedseeds,sodifficultyiscontrolledatthefamilylevelratherthanper threesettingsbeforevaryingotherhyperparameters.
instance. ➤Disableweighttyingbetweenembeddingandunembeddinglayersand
➤Identifyfamilieswherepass@4clustersnear0or1andapplytargeted measurewhetherthefreedcapacityisabsorbedbyattentionorthefeed-
re-samplingtoshiftthemintothetargetdifficultyband. forwardstack.
Figure7
RepresentativeideasgeneratedbyArboracrosstasks.Eachideaisproceduralratherthaninstance-specific,andeachwas
proposedonlyafterprecedingnodeshadruledoutbroaderdirections.
Inmodeltraining,ideasusuallymodifyaspecificoptimizercomponent,
Mostusefulideasarelocalandexecutable.
trainingrecipe,orarchitecturechoice. Inharnessengineering,theychangeconcretepartsoftheagentloop,such
asretrieval,aggregation,verification,orcontextmanagement. Indatasynthesis,theyrefinegeneration,filtering,
difficultycalibration,orverificationmodules.Thislocalitymakeseachideaeasytoimplement,evaluate,andattribute
toatreenode.
Manysuccessfulproposalsdirectlyrespondtoearlierobservations:the
Usefulideasareoftenevidence-conditioned.
BrowseCompevidence-dossierdesignfollowsfromthefailuremodeofverifier-onlyapproaches,andsimilarpatterns
appearindatasynthesis,wherelaternodesrepairspecificweaknessesindifficultycalibrationoranswerverification.
HTRthereforehelpsconvertlocalfailuresintonewdesignconstraints,andensuresthat“half-right”resultsbecome
thestartingpointforamoreprecisehypothesisratherthanareasontoabandonthedirection.
High-levelproblemformulationremainsimportant.Arborisstrongestwhentheobjectivecanbeimprovedthrough
asequenceofconcreterefinements,andlessreliablewhenprogressrequiresanewhigh-levelformulationweakly
connectedtotheexistingtree.TheArchitectureDesigntaskultimatelyacknowledgedthatsingle-knobtuninghad
reacheddiminishingreturnsandalargeralgorithmicmovewasneeded,butidentifyingthatmovestilldependedon
priorjudgmentratherthananythingthetreecouldautomaticallygenerate.Thishighlightstheroleofhuman-provided
taskdesign:theinitialartifact,evaluator,metric,andsearchinterfaceshapethekindsofideastheagentcandiscover.
Takeaway. As the tree grows, what has been ruled out, validated, and found to have boundary conditions all
becomepriorsconstrainingthenextroundofproposals. Arbor’sideasarethereforenotisolatedguessesbutlocal
advancesrelativetoaknowntaskunderstanding.Togetherwiththerefinementandtimingresultsabove,thispaints
thecompletepictureofHTRasaprocessmechanismthatmakesautonomousresearchcumulative:notmoreattempts,
butlessrepetitiveandmorememory-awaresearch.
7 Conclusion
WepresentedArborasaframeworkforAutonomousOptimization, wherearesearchagentmustimproveareal
artifactthroughlong-horizonexperimentalfeedbackratherthanexecuteasinglepredefinedtrajectory.Thecoreidea
istomaketheresearchstatepersistentandoperational:Arborrepresentscompetinghypotheses,artifactversions,
evaluationresults,failureattributions,andreusableinsightsinadurablehypothesistree. Acoordinatorusesthis
treetomanagestrategicsearch,whileshort-livedexecutorsgroundindividualhypothesesinisolatedworktreesand
returnstructuredevidence.Togetherwithinsightpropagationandaheld-outadmissiongate,thisdesignturnstrial
anderrorintoanauditableprocessofbranching,falsification,andevidence-constrainedimprovement.
AcrosstheAOsettingsstudiedhere,thisorganizationprovidesconsistentevidenceofvalue. Onsixreal-research
tasksspanningmodeltraining,harnessengineering,anddatasynthesis,Arborachievesthestrongestheld-outresults
amongthecompared methods; onMLE-BenchLite, thesame controllertransferstoan established long-horizon
16

ML-engineeringbenchmark.ThetransferstudyshowsthataBrowseComp-optimizedharnesscanimproveunseen
search-agenttasks,andtheablationsindicatethatthehypothesistreeandinsightfeedbackaremostusefulwhenthey
operatetogether.Theseresultssupporttheviewthatpersistenthypothesismanagementisausefulabstractionfor
autonomousresearch,whilethelimitationsofthecurrenttasksuite,scalarobjectives,modelcapabilities,andsearch
costleavesubstantialroomforbroaderandmorerigorousfutureevaluations.
References
Anthropic. ClaudeCode. https://github.com/anthropics/claude-code,2025. Agenticcodingtoolforterminal,IDE,andGitHub
workflows.Accessed:2026-06-02.
JingyiChai,ShuoTang,RuiYe,YuwenDu,XinyuZhu,MengchengZhou,YanfengWang,WeinanE,YuzhiZhang,LinfengZhang,
andSihengChen. Scimaster: Towardsgeneral-purposescientificAIagents,parti.x-masterasfoundation: Canweleadon
humanity’slastexam? CoRR,abs/2507.05241,2025. doi:10.48550/ARXIV.2507.05241. https://doi.org/10.48550/arXiv.2507.05241.
JunShernChan,NeilChowdhury,OliverJaffe,JamesAung,DaneSherburn,EvanMays,GiulioStarace,KevinLiu,LeonMaksin,
TejalPatwardhan,LilianWeng,andAleksanderMadry. Mle-bench:Evaluatingmachinelearningagentsonmachinelearning
engineering. CoRR,abs/2410.07095,2024. doi:10.48550/ARXIV.2410.07095. https://doi.org/10.48550/arXiv.2410.07095.
GuoxinChen,JieChen,LeiChen,JialeZhao,FanzheMeng,WayneXinZhao,RuihuaSong,ChengChen,Ji-RongWen,andKaiJia.
Towardautonomouslong-horizonengineeringforMLresearch. CoRR,abs/2604.13018,2026a. doi:10.48550/ARXIV.2604.13018.
https://doi.org/10.48550/arXiv.2604.13018.
JiefengChen,BhavanaDalviMishra,JaehyunNam,RuiMeng,TomasPfister,andJinsungYoon. MARS:modularagentwith
reflectivesearchforautomatedAIresearch. CoRR,abs/2602.02660,2026b. doi:10.48550/ARXIV.2602.02660. https://doi.org/10.
48550/arXiv.2602.02660.
ZiruChen,ShijieChen,YutingNing,QianhengZhang,BoshiWang,BotaoYu,YifeiLi,ZeyiLiao,ChenWei,ZitongLu,Vishal
Dey,MingyiXue,FrazierN.Baker,BenjaminBurns,DanielAdu-Ampratwum,XuhuiHuang,XiaNing,SongGao,YuSu,and
HuanSun. Scienceagentbench: Towardrigorousassessmentoflanguageagentsfordata-drivenscientificdiscovery. CoRR,
abs/2410.05080,2024. doi:10.48550/ARXIV.2410.05080. https://doi.org/10.48550/arXiv.2410.05080.
YizheChi,DeyaoHong,DapengJiang,TianweiLuo,KaisenYang,BoshiZhang,ZheCao,XiaoyanFan,BingxiangHe,HanHao,
WeiyangJin,DianqiaoLei,QingleLiu,HoudeQian,BowenWang,SituWang,YoujieZheng,YifanZhou,CalvinXiao,ErenCai,
andQinhuaiNa.Frontier-eng:Benchmarkingself-evolvingagentsonreal-worldengineeringtaskswithgenerativeoptimization.
CoRR,abs/2604.12290,2026. doi:10.48550/ARXIV.2604.12290. https://doi.org/10.48550/arXiv.2604.12290.
YaxinDu,XiyuanYang,ZhifanZhou,WanxuLiu,ZixingLei,ZimengChen,FenyiLiu,HaotianWu,YuzhuCai,ZexiLiu,Xinyu
Zhu,WenHaoWang,LinfengZhang,ChenQian,andSihengChen. Datamaster:Data-centricautonomousairesearch,2026.
https://arxiv.org/abs/2605.10906.
JohannesGasteiger,AkbirKhan,SamBowman,VladimirMikulik,EthanPerez,andFabienRoger. Automatedresearcherscan
subtlysandbag,March2025. https://alignment.anthropic.com/2025/automated-researchers-sandbag/.
YuyangHu,ShichunLiu,YanweiYue,GuibinZhang,BoyangLiu,FangyiZhu,JiahangLin,HonglinGuo,ShihanDou,ZhihengXi,
SenjieJin,JiejunTan,YanbinYin,JiongnanLiu,ZeyuZhang,ZhongxiangSun,YutaoZhu,HaoSun,BociPeng,ZhenrongCheng,
XuanboFan,JiaxinGuo,XinleiYu,ZhenhongZhou,ZewenHu,JiahaoHuo,JunhaoWang,YuweiNiu,YuWang,ZhenfeiYin,
XiaobinHu,YueLiao,QiankunLi,KunWang,WangchunshuZhou,YixinLiu,DaweiCheng,QiZhang,TaoGui,ShiruiPan,Yan
Zhang,PhilipTorr,ZhichengDou,Ji-RongWen,XuanjingHuang,Yu-GangJiang,andShuichengYan. MemoryintheageofAI
agents. CoRR,abs/2512.13564,2025. doi:10.48550/ARXIV.2512.13564. https://doi.org/10.48550/arXiv.2512.13564.
YuyangHu,HongjinQian,ShutingWang,JiongnanLiu,TongZhao,XiaoxiLi,ZhengLiu,andZhichengDou. Agentfugue:Agent
scalingforlong-horizontasksthroughcollectivereasoning,2026a. https://arxiv.org/abs/2605.24486.
YuyangHu,HongjinQian,ShutingWang,JiongnanLiu,ZiliangZhao,JiejunTan,ZhengLiu,andZhichengDou.Sam:State-adaptive
memoryforlong-horizonreasoningagent,2026b. https://arxiv.org/abs/2605.24468.
Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. Mlagentbench: Evaluating language agents on machine learning
experimentation. InRuslanSalakhutdinov,ZicoKolter,KatherineA.Heller,AdrianWeller,NuriaOliver,JonathanScarlett,and
FelixBerkenkamp,editors,Forty-firstInternationalConferenceonMachineLearning,ICML2024,Vienna,Austria,July21-27,2024,
ProceedingsofMachineLearningResearch,pages20271–20309.PMLR/OpenReview.net,2024. https://proceedings.mlr.press/
v235/huang24y.html.
17

ZhengyaoJiang,DominikSchmidt,DhruvSrikanth,DixingXu,IanKaplan,DenissJacenko,andYuxiangWu. AIDE:ai-driven
explorationinthespaceofcode. CoRR,abs/2502.13138,2025. doi:10.48550/ARXIV.2502.13138. https://doi.org/10.48550/arXiv.
2502.13138.
KellerJordanandcontributors. NanoGPT-Bench: NanoGPTtrainingspeedrunbenchmark. https://github.com/KellerJordan/
modded-nanogpt,2025.
AndrejKarpathy. autoresearch:AIagentsrunningresearchonsingle-GPUnanochattrainingautomatically. https://github.com/
karpathy/autoresearch,2026.
ThomasKwa,BenWest,JoelBecker,AmyDeng,KatharynGarcia,MaxHasin,SamiJawhar,MeganKinniment,NateRush,Sydney
vonArx,RyanBloom,ThomasBroadley,HaoxingDu,BrianGoodrich,NikolaJurkovic,LukeHaroldMiles,SeraphinaNix,
TaoLin,NeevParikh,DavidRein,LucasJunKobaSato,HjalmarWijk,DanielM.Ziegler,ElizabethBarnes,andLawrence
Chan. MeasuringAIabilitytocompletelongtasks. CoRR,abs/2503.14499, 2025. doi: 10.48550/ARXIV.2503.14499. https:
//doi.org/10.48550/arXiv.2503.14499.
YoonhoLee,RoshenNair,QizhengZhang,KangwookLee,OmarKhattab,andChelseaFinn.Meta-harness:End-to-endoptimization
ofmodelharnesses. CoRR,abs/2603.28052,2026. doi:10.48550/ARXIV.2603.28052. https://doi.org/10.48550/arXiv.2603.28052.
AnnanLi,ChufanWu,ZengleGe,YeeHinChong,ZhinanHou,LizheCao,ChengJu,JianminWu,HuaimingLi,HaoboZhang,
ShenghaoFeng,MoZhao,FengzhiQiu,RuiYang,MengmengZhang,WenyiZhu,YingyingSun,QuanSun,ShunhaoYan,
DanyuLiu,DaweiYin,andDouShen. TheFMagent. CoRR,abs/2510.26144,2025. doi: 10.48550/ARXIV.2510.26144. https:
//doi.org/10.48550/arXiv.2510.26144.
JiahangLin,ShichunLiu,ChengjunPan,LizhiLin,ShihanDou,XuanjingHuang,HangYan,ZhenhuaHan,andTaoGui. Agentic
harnessengineering:Observability-drivenautomaticevolutionofcoding-agentharnesses. CoRR,abs/2604.25850,2026. doi:
10.48550/ARXIV.2604.25850. https://doi.org/10.48550/arXiv.2604.25850.
JiahengLiu,DaweiZhu,ZhiqiBai,YanchengHe,HuanxuanLiao,HaoranQue,ZekunWang,ChenchenZhang,GeZhang,Jiebin
Zhang,YuanxingZhang,ZhuoChen,HangyuGuo,ShilongLi,ZiqiangLiu,YongShan,YifanSong,JiayiTian,WenhaoWu,
ZhejianZhou, RuijieZhu, JunlanFeng, YangGao, ShizhuHe, ZhoujunLi, TianyuLiu, FanyuMeng, WenboSu, Yingshui
Tan, Zili Wang, Jian Yang, Wei Ye, Bo Zheng, Wangchunshu Zhou, Wenhao Huang, Sujian Li, and Zhaoxiang Zhang. A
comprehensivesurveyonlongcontextlanguagemodeling. CoRR,abs/2503.17407,2025a. doi: 10.48550/ARXIV.2503.17407.
https://doi.org/10.48550/arXiv.2503.17407.
ZexiLiu,YuzhuCai,XinyuZhu,YujieZheng,RunkunChen,YingWen,YanfengWang,WeinanE,andSihengChen. Ml-master:
Towardsai-for-aiviaintegrationofexplorationandreasoning. CoRR,abs/2506.16499,2025b. doi:10.48550/ARXIV.2506.16499.
https://doi.org/10.48550/arXiv.2506.16499.
XinghuaLou,MiguelLázaro-Gredilla,AntoineDedieu,CarterWendelken,WolfgangLehrach,andKevinP.Murphy. Autoharness:
improvingLLMagentsbyautomaticallysynthesizingacodeharness.CoRR,abs/2603.03329,2026.doi:10.48550/ARXIV.2603.03329.
https://doi.org/10.48550/arXiv.2603.03329.
ChrisLu,CongLu,RobertTjarkoLange,JakobN.Foerster,JeffClune,andDavidHa. TheAIscientist:Towardsfullyautomated
open-endedscientificdiscovery. CoRR,abs/2408.06292,2024. doi:10.48550/ARXIV.2408.06292. https://doi.org/10.48550/arXiv.
2408.06292.
MikeA.Merrill,AlexanderGlennShaw,NicholasCarlini,BoxuanLi,HarshRaj,IvanBercovich,LinShi,JeongYeonShin,Thomas
Walshe,EstefanyKellyBuchanan,JunhongShen,GuanghaoYe,HaoweiLin,JasonPoulos,MaoyuWang,MariannaNezhurina,
JeniaJitsev,DiLu,OrfeasMenis-Mastromichalakis,ZhiweiXu,ZizhaoChen,YueLiu,RobertZhang,LeonLiangyuChen,Anurag
Kashyap,Jan-LucasUslu,JeffreyLi,JianboWu,MinghaoYan,SongBian,VedangSharma,KeSun,StevenDillmann,Akshay
Anand,AndrewLanpouthakoun,BardiaKoopah,ChangranHu,EtashKumarGuha,GabrielH.S.Dreiman,JiachengZhu,Karl
Krauth,LiZhong,NiklasMuennighoff,RobertAmanfu,ShangyinTan,ShreyasPimpalgaonkar,TusharAggarwal,Xiangning
Lin,XinLan,XuandongZhao,YiqingLiang,YuanliWang,ZilongWang,ChangzhiZhou,DavidHeineman,HangeLiu,Harsh
Trivedi,JohnYang,JunhongLin,ManishShetty,MichaelYang,NabilOmi,NeginRaoof,ShandaLi,TerryYueZhuo,Wuwei
Lin,YiweiDai,YuxinWang,WenhaoChai,ShangZhou,DariushWahdany,ZiyuShe,JiamingHu,ZhikangDong,Yuxuan
Zhu,SashaCui,AhsonSaiyed,ArinbjörnKolbeinsson,JesseHu,ChristopherMichaelRytting,RyanMarten,YixinWang,Alex
Dimakis,AndyKonwinski,andLudwigSchmidt. Terminal-bench:Benchmarkingagentsonhard,realistictasksincommand
lineinterfaces. CoRR,abs/2601.11868,2026. doi:10.48550/ARXIV.2601.11868. https://doi.org/10.48550/arXiv.2601.11868.
AlirezaNadafian,AlirezaMohammadshahi,andMajidYazdani. KAPSO:Aknowledge-groundedframeworkforautonomous
programsynthesisandoptimization. CoRR,abs/2601.21526,2026. doi:10.48550/ARXIV.2601.21526. https://doi.org/10.48550/
arXiv.2601.21526.
18

AlexanderNovikov,NgânVu,MarvinEisenberger,EmilienDupont,Po-SenHuang,AdamZsoltWagner,SergeyShirobokov,
BorislavKozlovskii,FranciscoJ.R.Ruiz,AbbasMehrabian,M.PawanKumar,AbigailSee,SwaratChaudhuri,GeorgeHolland,
AlexDavies,SebastianNowozin,PushmeetKohli,andMatejBalog. Alphaevolve:Acodingagentforscientificandalgorithmic
discovery. CoRR,abs/2506.13131,2025. doi:10.48550/ARXIV.2506.13131. https://doi.org/10.48550/arXiv.2506.13131.
OpenAI. CodexCLI. https://github.com/openai/codex,2025. Lightweightcodingagentthatrunslocallyonauser’scomputer.
Accessed:2026-06-02.
JoonSungPark,JosephC.O’Brien,CarrieJunCai,MeredithRingelMorris,PercyLiang,andMichaelS.Bernstein.Generativeagents:
Interactivesimulacraofhumanbehavior.InSeanFollmer,JeffHan,JürgenSteimle,andNathalieHenryRiche,editors,Proceedings
ofthe36thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology,UIST2023,SanFrancisco,CA,USA,29October
2023-1November2023,pages2:1–2:22.ACM,2023. doi:10.1145/3586183.3606763. https://doi.org/10.1145/3586183.3606763.
OriPress,BrandonAmos,HaoyuZhao,YikaiWu,SamuelK.Ainsworth,DominikKrupke,PatrickKidger,TouqirSajed,Bartolomeo
Stellato, Jisun Park, Nathanael Bosch, Eli Meril, Albert Steppi, Arman Zharmagambetov, Fangzhao Zhang, David Perez-
Pineiro,AlbertoMercurio,NiZhan,TalorAbramovich,KilianLieret,HanlinZhang,ShirleyHuang,MatthiasBethge,and
OfirPress. Algotune:Canlanguagemodelsspeedupgeneral-purposenumericalprograms? CoRR,abs/2507.15887,2025. doi:
10.48550/ARXIV.2507.15887. https://doi.org/10.48550/arXiv.2507.15887.
RushiQiang,YuchenZhuang,YinghaoLi,DinguSagarV.K,RongzhiZhang,ChanghaoLi,IanShu-HeiWong,SherryYang,
PercyLiang,ChaoZhang,andBoDai. Mle-dojo:InteractiveenvironmentsforempoweringLLMagentsinmachinelearning
engineering. CoRR,abs/2505.07782,2025. doi:10.48550/ARXIV.2505.07782. https://doi.org/10.48550/arXiv.2505.07782.
YujiaQin,ShihaoLiang,YiningYe,KunlunZhu,LanYan,YaxiLu,YankaiLin,XinCong,XiangruTang,BillQian,SihanZhao,
LaurenHong,RunchuTian,RuobingXie,JieZhou,MarkGerstein,DahaiLi,ZhiyuanLiu,andMaosongSun.Toolllm:Facilitating
largelanguagemodelstomaster16000+real-worldapis. InTheTwelfthInternationalConferenceonLearningRepresentations,
ICLR2024,Vienna,Austria,May7-11,2024.OpenReview.net,2024. https://openreview.net/forum?id=dHng2O0Jjr.
BenRank,HardikBhatnagar,AmeyaPrabhu,ShiraEisenberg,KarinaNguyen,MatthiasBethge,andMaksymAndriushchenko.
Posttrainbench:CanLLMagentsautomateLLMpost-training? CoRR,abs/2603.08640,2026. doi:10.48550/ARXIV.2603.08640.
https://doi.org/10.48550/arXiv.2603.08640.
DavidRein,JoelBecker,AmyDeng,SeraphinaNix,ChrisCanal,DanielO’Connel,PipArnott,RyanBloom,ThomasBroadley,
KatharynGarcia,BrianGoodrich,MaxHasin,SamiJawhar,MeganKinniment,ThomasKwa,AronLajko,NateRush,Lucas
JunKobaSato,SydneyvonArx,BenWest,LawrenceChan,andElizabethBarnes.HCAST:human-calibratedautonomysoftware
tasks. CoRR,abs/2503.17354,2025. doi:10.48550/ARXIV.2503.17354. https://doi.org/10.48550/arXiv.2503.17354.
BernardinoRomera-Paredes,MohammadaminBarekatain,AlexanderNovikov,MatejBalog,M.PawanKumar,EmilienDupont,
FranciscoJ.R.Ruiz,JordanS.Ellenberg,PengmingWang,OmarFawzi,PushmeetKohli,andAlhusseinFawzi. Mathematical
discoveriesfromprogramsearchwithlargelanguagemodels. Nat.,625(7995):468–475,2024. doi:10.1038/S41586-023-06924-6.
https://doi.org/10.1038/s41586-023-06924-6.
TimoSchick,JaneDwivedi-Yu,RobertoDessì,RobertaRaileanu,MariaLomeli,EricHambro,LukeZettlemoyer,NicolaCancedda,
andThomasScialom. Toolformer:Languagemodelscanteachthemselvestousetools. InAliceOh,TristanNaumann,Amir
Globerson,KateSaenko,MoritzHardt,andSergeyLevine,editors,AdvancesinNeuralInformationProcessingSystems36:Annual
ConferenceonNeuralInformationProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,2023.
http://papers.nips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html.
SamuelSchmidgall,YushengSu,ZeWang,XimengSun,JialianWu,XiaodongYu,JiangLiu,ZichengLiu,andEmadBarsoum.
Agentlaboratory: UsingLLMagentsasresearchassistants. CoRR,abs/2501.04227,2025. doi: 10.48550/ARXIV.2501.04227.
https://doi.org/10.48550/arXiv.2501.04227.
NoahShinn,FedericoCassano,AshwinGopinath,KarthikNarasimhan,andShunyuYao. Reflexion:languageagentswithverbal
reinforcement learning. In Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine,
editors,AdvancesinNeuralInformationProcessingSystems36: AnnualConferenceonNeuralInformationProcessingSystems
2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,2023. http://papers.nips.cc/paper_files/paper/2023/hash/
1b44b878bb782e6954cd888628510e90-Abstract-Conference.html.
AkshitSinha,ArvindhArun,ShashwatGoel,SteffenStaab,andJonasGeiping. Theillusionofdiminishingreturns:Measuringlong
horizonexecutioninllms.CoRR,abs/2509.09677,2025.doi:10.48550/ARXIV.2509.09677.https://doi.org/10.48550/arXiv.2509.09677.
GiulioStarace,OliverJaffe,DaneSherburn,JamesAung,JunShernChan,LeonMaksin,RachelDias,EvanMays,BenjaminKinsella,
WyattThompson,JohannesHeidecke,AmeliaGlaese,andTejalPatwardhan. Paperbench:Evaluatingai’sabilitytoreplicateAI
research. CoRR,abs/2504.01848,2025. doi:10.48550/ARXIV.2504.01848. https://doi.org/10.48550/arXiv.2504.01848.
19

InternScienceTeam. Internagent-1.5: Aunifiedagenticframeworkforlong-horizonautonomousscientificdiscovery. CoRR,
abs/2602.08990,2026. doi:10.48550/ARXIV.2602.08990. https://doi.org/10.48550/arXiv.2602.08990.
GuiyaoTie,PanZhou,andLichaoSun. AsurveyofAIscientists. CoRR,abs/2510.23045,2025. doi:10.48550/ARXIV.2510.23045.
https://doi.org/10.48550/arXiv.2510.23045.
EdanToledo,KarenHambardzumyan,MartinJosifoski,RishiHazra,NicolasMarioBaldwin,AlexisAudran-Reiss,MichaelKuchnik,
DespoinaMagka,MinqiJiang,AlisiaMariaLupidi,AndreiLupu,RobertaRaileanu,KelvinNiu,TatianaShavrina,Jean-Christophe
Gagnon-Audet,MichaelShvartsman,ShagunSodhani,AlexanderH.Miller,AbhishekCharnalia,DerekDunfield,Carole-Jean
Wu, Pontus Stenetorp, Nicola Cancedda, Jakob Nicolaus Foerster, and Yoram Bachrach. AI research agents for machine
learning:Search,exploration,andgeneralizationinmle-bench. CoRR,abs/2507.02554,2025. doi:10.48550/ARXIV.2507.02554.
https://doi.org/10.48550/arXiv.2507.02554.
ChunhuiWan,XunanDai,ZhuoWang,MingleiLi,YanpengWang,YinanMao,YuLan,andZhiwenXiao. Loongflow:Directed
evolutionarysearchviaacognitiveplan-execute-summarizeparadigm. CoRR,abs/2512.24077,2025. doi:10.48550/ARXIV.2512.
24077. https://doi.org/10.48550/arXiv.2512.24077.
MilesWang, RobiLin, KatHu, JoyJiao, NeilChowdhury, EthanChang, andTejalPatwardhan. Frontierscience: Evaluating
ai’s ability to perform expert-level scientific tasks. CoRR, abs/2601.21165, 2026. doi: 10.48550/ARXIV.2601.21165. https:
//doi.org/10.48550/arXiv.2601.21165.
XingyaoWang,BoxuanLi,YufanSong,FrankF.Xu,XiangruTang,MingchenZhuge,JiayiPan,YueqiSong,BowenLi,Jaskirat
Singh,HoangH.Tran,FuqiangLi,RenMa,MingzhangZheng,BillQian,YanjunShao,NiklasMuennighoff,YizheZhang,
BinyuanHui,JunyangLin,andetal. Openhands:AnopenplatformforAIsoftwaredevelopersasgeneralistagents. InThe
ThirteenthInternationalConferenceonLearningRepresentations,ICLR2025,Singapore,April24-28,2025.OpenReview.net,2025.
https://openreview.net/forum?id=OJd3ayDDoF.
JasonWei,ZhiqingSun,SpencerPapay,ScottMcKinney,JeffreyHan,IsaFulford,HyungWonChung,AlexTachardPassos,William
Fedus,andAmeliaGlaese. Browsecomp:Asimpleyetchallengingbenchmarkforbrowsingagents. CoRR,abs/2504.12516,2025.
doi:10.48550/ARXIV.2504.12516. https://doi.org/10.48550/arXiv.2504.12516.
HjalmarWijk,TaoLin,JoelBecker,SamiJawhar,NeevParikh,ThomasBroadley,LawrenceChan,MichaelChen,JoshuaClymer,
JaiDhyani, ElenaEricheva, KatharynGarcia, BrianGoodrich, NikolaJurkovic, MeganKinniment, AronLajko, Seraphina
Nix,LucasSato,WilliamSaunders,MaksymTaran,BenWest,andElizabethBarnes. Re-bench: EvaluatingfrontierAIr&d
capabilitiesoflanguagemodelagentsagainsthumanexperts. CoRR,abs/2411.15114,2024. doi:10.48550/ARXIV.2411.15114.
https://doi.org/10.48550/arXiv.2411.15114.
Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob N. Foerster, Jeff Clune, and David Ha. The
AI scientist-v2: Workshop-level automated scientific discovery via agentic tree search. CoRR, abs/2504.08066, 2025. doi:
10.48550/ARXIV.2504.08066. https://doi.org/10.48550/arXiv.2504.08066.
XuYang,XiaoYang,ShikaiFang,BowenXian,YuanteLi,JianWang,MinruiXu,HaoranPan,XinpengHong,WeiqingLiu,Yelong
Shen,WeizhuChen,andJiangBian. R&d-agent:Automatingdata-drivenAIsolutionbuildingthroughllm-poweredautomated
research,development,andevolution. CoRR,abs/2505.14738,2025. doi:10.48550/ARXIV.2505.14738. https://doi.org/10.48550/
arXiv.2505.14738.
ShunyuYao,DianYu,JeffreyZhao,IzhakShafran,ThomasL.Griffiths,YuanCao,andKarthikNarasimhan. Treeofthoughts:
Deliberate problem solving with large language models. CoRR, abs/2305.10601, 2023a. doi: 10.48550/ARXIV.2305.10601.
https://doi.org/10.48550/arXiv.2305.10601.
ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikR.Narasimhan,andYuanCao. React:Synergizingreasoning
andactinginlanguagemodels. InTheEleventhInternationalConferenceonLearningRepresentations,ICLR2023,Kigali,Rwanda,
May1-5,2023.OpenReview.net,2023b. https://openreview.net/forum?id=WE_vluYUL-X.
JennyZhang,ShengranHu,CongLu,RobertT.Lange,andJeffClune. Darwingodelmachine: Open-endedevolutionofself-
improvingagents. CoRR,abs/2505.22954,2025a. doi:10.48550/ARXIV.2505.22954. https://doi.org/10.48550/arXiv.2505.22954.
JiayiZhang,JinyuXiang,ZhaoyangYu,FengweiTeng,XionghuiChen,JiaqiChen,MingchenZhuge,XinCheng,SiruiHong,
JinlinWang,BingnanZheng,BangLiu,YuyuLuo,andChenglinWu. Aflow:Automatingagenticworkflowgeneration. InThe
ThirteenthInternationalConferenceonLearningRepresentations,ICLR2025,Singapore,April24-28,2025.OpenReview.net,2025b.
https://openreview.net/forum?id=z5uVAKwmjf.
QizhengZhang,ChangranHu,ShubhangiUpasani,BoyuanMa,FengluHong,VamsidharKamanuru,JayRainton,ChenWu,
MengmengJi,HanchenLi,UrmishThakker,JamesZou,andKunleOlukotun. Agenticcontextengineering:Evolvingcontexts
forself-improvinglanguagemodels. CoRR,abs/2510.04618,2025c. doi:10.48550/ARXIV.2510.04618. https://doi.org/10.48550/
arXiv.2510.04618.
20

RuiyiZhang,PeijiaQin,QiCao,LiZhang,andPengtaoXie. Aibuildai:AnAIagentforautomaticallybuildingAImodels. CoRR,
abs/2604.14455,2026. doi:10.48550/ARXIV.2604.14455. https://doi.org/10.48550/arXiv.2604.14455.
BingchenZhao,DespoinaMagka,MinqiJiang,XianLi,RobertaRaileanu,TatianaShavrina,Jean-ChristopheGagnon-Audet,Kelvin
Niu,ShagunSodhani,MichaelShvartsman,AndreiLupu,AlisiaMariaLupidi,EdanToledo,KarenHambardzumyan,Martin
Josifoski,ThomasFoster,LuciaCipolina-Kun,AbhishekCharnalia,DerekDunfield,AlexanderH.Miller,OisinMacAodha,
JakobN.Foerster,andYoramBachrach. TheautomatedLLMspeedrunningbenchmark:Reproducingnanogptimprovements.
CoRR,abs/2506.22419,2025. doi:10.48550/ARXIV.2506.22419. https://doi.org/10.48550/arXiv.2506.22419.
AndyZhou,KaiYan,MichalShlapentokh-Rothman,HaohanWang,andYu-XiongWang. Languageagenttreesearchunifies
reasoning actingandplanning inlanguage models. CoRR,abs/2310.04406, 2023. doi: 10.48550/ARXIV.2310.04406. https:
//doi.org/10.48550/arXiv.2310.04406.
XinyuZhu, YuzhuCai, ZexiLiu, BingyangZheng, ChengWang, RuiYe, JiaaoChen, HanruiWang, Wei-ChenWang, Yuzhi
Zhang, Linfeng Zhang, Weinan E, Di Jin, Siheng Chen, and Yanfeng Wang. Toward ultra-long-horizon agentic science:
Cognitiveaccumulationformachinelearningengineering. CoRR,abs/2601.10402, 2026. doi: 10.48550/ARXIV.2601.10402.
https://doi.org/10.48550/arXiv.2601.10402.
21

Appendix
A LimitationsandFutureWork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
B DetailsofArbor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
B.1 Prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
B.1.1 CoordinatorPrompt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
B.1.2 ExecutorPrompt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
B.2 AlgorithmWorkflow. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
B.3 KeyDesignof ArborFramework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
B.4 AgentToolsandHyperparameterSettings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
B.4.1 CoordinatorTools. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
B.4.2 ExecutorTools. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
B.4.3 EvaluationandMergeTools. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
B.5 IdeaTreeDataStructureandStorage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
C DetailsoftheAOTestSuite. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
C.1 OptimizerDesign. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
C.2 ArchitectureDesign . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
C.3 Terminal-Bench2.0. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
C.4 BrowseComp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
C.5 Search-AgentDataSynthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
C.6 Math-ReasoningDataSynthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
A LimitationsandFutureWork
Althoughtheempiricalresultsdemonstratethepromiseof Arborforautonomousresearch,thisstudyhasseveral
limitations.Wediscusstheselimitationsbelowandoutlinethecorrespondingdirectionsforfuturework.
Evaluationscope. Ourexperimentsareaninitialprobeofautonomousresearchratherthanacompletebenchmark
forscientificdiscovery.ThecurrentAOtasksuitecoversmodeltraining,harnessengineering,anddatasynthesis,
butitdoesnotyetspanthefulldiversityofresearchproblems.WithinAI,futuretasksshouldincludesettingssuch
aslow-levelkerneloptimization,pretrainingdata-mixturedesign,andmoreopen-endedsystemdesign.BeyondAI,
domainssuchasbiology,mathematics,andphysicsrequirebenchmarkswherevaluablehypothesesareharderto
specifyandvalidate.Abroadersuiteshouldthereforeevaluatenotonlymetricimprovement,butalsowhetherthe
generatedideasarescientificallymeaningful,reproducible,andtransferable.
Objectivedesign. ThepresentAOinterfacemainlyoptimizesafixedscalarobjectivedefinedbyatask-specific
evaluator.Thisisusefulforcontrolledexperiments,butitisasimplificationofrealresearch.Scientificobjectivesare
oftenmulti-dimensional:performance,resourceuse,robustness,interpretability,novelty,andsafetymayallmatter,
andimprovingonecanhurtanother.FutureAOsystemsshouldsupportmulti-objectivesearch,explicitconstraints,
Pareto-stylecomparison,andadaptiveschedulingbetweencompetingcriteria.Thiswouldalsoreducetheriskthatan
agentoverfitstoanarrowbenchmarkmetricwhilemissingthebroaderresearchgoal.
22

Ideageneration. Weobservethatagentscanreadevaluationfeedbackcarefullyandproposeusefullocalrefinements,
buttheirresearchabilityremainsfarfromthatofexperthumanresearchers.Indifficulttasks,theymayfailtoidentify
agenuinelynewmechanism,abandonapromisingdirectionafterearlyfailures,orreverse-engineersolutionsfrom
observedscoresinsteadofreasoningfromfirstprinciples.Amorefine-grainedstudyofagentideaformationistherefore
needed.Promisingdirectionsincludebetteruncertaintytracking,explicitreuseofnegativeevidence,mechanisms
forrevisitingsuspendedbranches,andtrainingorpromptingmethodsthatencouragecausalandfirst-principles
hypothesesratherthanonlyresult-drivenfixes.
Cost and infrastructure. Long-horizon autonomous research is limited not only by idea quality, but also by
systemsengineering.Inourruns,performanceandefficiencydependondetailssuchaspromptcaching,evaluator
scheduling,isolatedenvironmentstartup,parallelworktreeexecution,andthereliabilityofinter-agentcoordination.
Largenumbersofmodelcalls,evaluatorcalls,andartifacthandoffscanmakeasuccessfulsearchexpensiveevenwhen
eachindividualstepissimple. Futureworkshoulddevelopcost-awaretreepolicies,adaptiveevaluatorallocation,
strongercachingandcheckpointing,andmorerobustexecutioninfrastructuresothatAOsystemscanscalewithout
turningsearchbreadthintouncontrolledcomputecost.
Modelcapability. Finally,ArborinheritsthestrengthsandweaknessesoftheunderlyingLLMs.Currentmodelsare
oftencapableofcoding,summarizingresults,andmakingplausiblelocalhypotheses,buttheycanstillstrugglewith
deepdomainknowledge,longchainsofcausalreasoning,andgenuinelycreativeproblemreformulation.Stronger
foundationmodelswilllikelyimproveAOdirectly,butmodelscalingalonemaynotbesufficient. Futuresystems
shouldcombineLLMswithdomainknowledgebases,specializedtools,simulators,formalcheckers,andtraining
signalstargetedatscientifichypothesisgeneration.Inthissense,Arborprovidesastructureforaccumulatingand
testingideas,whilethequalityofthoseideasremainsanimportantfrontier.
B DetailsofArbor
Figure8summarizestheimplementation-levelagentinternalsusedbyArbor.
B.1 Prompts
B.1.1 CoordinatorPrompt
CoordinatorPrompt
Role.
YouarethepersistentcoordinatorinArbor.Yourjobistomaintainthehypothesistreeasthesharedresearchstate,
choosewhichhypothesesdeserveexecution,andconvertexperimentalfeedbackintoreusableevidence.Youdonoteditthe
targetartifactdirectly.Allimplementationworkisdelegatedtoshort-livedExecutors,whileyouownthetree,theresearch
frontier,andthemerge/prune/stopdecisions.
YouruninasinglepersistentReActloop.Whentheconversationapproachesthecontextlimit,
Runtimeanddurablestate.
olderturnsmaybecompressed;theon-diskhypothesistreeisthereforethesourceoftruth. Everycontrolledmutationis
savedasJSONfortoolsandregeneratedasMarkdownforhumaninspection.Operatormessagesprefixedwith[user note]
areinstructionsorquestionsthatmustbehandledatthenextsafepointbeforelaunchingnewExecutorsormergingbranches.
Researchcontract.
Atinitialization,inspectthetargetcodebaseandrecordtheAOcontractviaTreeSetMeta:theobjective,
metricdirection,developmentevaluatorE ,held-outevaluatorE ,datasetpaths,baselinescore,andevaluationcommands.
dev test
Commandsmustusethetemplatevariables{cwd}and{node_id}sothatthesamecontractcanbeinjectedsafelyintoisolated
executorworktrees.
Therootnoderepresentstheinitialartifact.Depth-1childrenarebroadresearchdirections;deepernodes
Hypothesistree.
aremorespecificrefinements,alternatives,orcorrectionsundertheirparent.Eachnodestoresalifecyclestatus(pending,
running,done,merged,orpruned),adevscore,afactualresult,astructuredinsight,andagitbranchreferencecode_ref.
Thetreeisnotatranscriptoftoolcalls:itisthecompactrecordofwhatwastried,whathappened,whyithappened,andhow
thatevidenceshouldshapefuturehypotheses.
Repeatthefollowingcycleuntilthebudgetisexhausted,nopromisingfrontierremains,ortheobjectivehas
Coordinatorloop.
beensatisfied.
1. Observe.
ReadthecurrenttreewithTreeView;inspectthecurrentbestartifact,recentexecutorreports,andexperiment
logswhenneeded.Reconstructtheliveresearchfrontierfromthepersistedtreeratherthanfrommemoryalone.
23

Runtime Configuration and Task Contract
AO Task Contract CLI + Preflight Plugin Policy LLM Provider EventBus
artifact, objective, E_dev, workspace, clean git state, eval contract, protected model calls, retries, logging, statistics,
E_test trunk branch paths, lifecycle hooks token accounting dashboard
Dispatch fixed
Persistent Coordinator Agent hypothesis Executor Agents
one long-running MetaAgentOrchestrator-owned core.Agent +Ancestor short-lived core.Agent instances, one isolated git worktree per hypothesis
insights +
Reason → Call too R ls e → A c O t b L s o er o v p e → Update strategy co E m _ m de a v nd Executor A — worktree W1 Executor Tool Surface
inspect → edit → smoke test → run
• 4-layer compression E_dev → report 1 2 3 4 5
Context Manager • Persistent conversation Inspect Modify ExecuteDelegate Report
• Inter-turn user notes
⌕ ✎ ♟
Tree ➤Executor ⌕Read-only Admission b I r s a o n la c t h e e d s Executor B — worktree W2 • Read • Edit • Bash • Nested • Score
• TreeV M ie a w nage • Run D Su i b s a p g a en tc t h • Ba I s n h spection • GitM a e n rg d e B S ra e n a c r h ch Wor a k n t d rees inspect → E e _ d d it e → v → sm re o p k o e r t test → run • • G G r lo e b p • Write • • T R M r u a e n i t n ri i c n s g • S w S u o a b r m k A t e r g e e e nt • • • R I B n r e s a s i n g u c h lt h t
• TreeAddNode • RunSubagent • Read • SearchIdeaContext on time context reference
• TreeUpdateNode Parallel • Grep • SearchIdeaContext
• TreePrune • Convergence • Glob Parallel
• TreeSetMeta Policy • LoadSkill • SearchStatus Executor C — worktree W3
• TreePropagate • Budget policy
Structured inspect → edit → smoke test → run local implementation only; no E_test access;
owns global search; never edits target code directly evidence: E_dev → report no shared-state mutation
Score, Result,
optional Insight,
background dispatch Code_ref
Background SearchAgent
isolated related-work context Verified Merge Gate
⊕ WebSearch ⌕ WebVisit Novelty the only path into the current best artifact
assessment
1 C ex a e n c d u id to a r te ◆ 2 F d ev r e e a ta s lu c h a h t e io d n 3 R p p r a u o t n h te E c _ te te d s - t + 4 M t o r n u e l n r y g k i e f to
branch worktree checks improved
Durable Workspace State
IdeaTree Experiment Git Refs Run ▤ Event
Artifacts Statistics Logs ✓ verified promotion → current × rejected branch → retained as
M J a S r O kd N o w + n Report, Metrics, Diff B T r r a u n n c k h + es Toke C n y s c , le T s urns, S G es it s , i C on o , n E te v x a t l, best trunk evidence
Figure8
Agent-levelimplementationdetailsof Arbor.
2. Constrain.
UseTreeView(format=“constraints”)toloadtreeshape,rootinsight,prunedlessons,andvalidatedfindings.
Treatprunedlessonsasnegativeconstraintsandvalidatedfindingsasassumptionstobuildon.
3. Ideate.
Selectaparentnodeandproposeasmallsetofexecutablechildhypotheses.EachcandidateaddedwithTreeAddNode
muststateitsmechanism,hypothesis,observablesuccesscondition,andknownconflictsorrisks.Donotaddcandidates
thatmerelyrepeataprunedfailuremode.
Choosependingleavesforthenextbatchusingaccumulatedevidence,expectedimpact,implementationcost,and
4. Select.
diversityacrossactivedirections.Preferhypothesesthatcanteachthetreesomethingusefulevenwhentheyfail.
5. Execute. Dispatch selected leaves with RunSubagent or RunSubagentParallel. Each Executor receives one fixed
hypothesis,theresearchcontract,andancestorinsights,thenworksinanisolatedgitworktreebranchedfromthecurrent
bestartifact.
6. Update.
Afterexecution,writebackthedevscore,factualresult,distilledinsight,andcode_ref. Propagateinsights
upwardsoleaf-leveloutcomesbecomedirection-levellessonsandeventuallyupdatetheglobalpriorattheroot.
7. Decide.
Continueadirection,pruneitwithTreePrunewhenitsassumptionsarefalsified,orpromoteacandidatethrough
GitMergeBranch.AbranchmayupdatethecurrentbestonlyafterthemergegateevaluatesitonE inafreshworktree
test
andconfirmsanimprovementoverthecurrentbest.
Executorsmaterializehypotheses;theydonotcontroltheglobalsearch.Theymayrepairimplementation
Executorboundary.
mistakesandrerunE ,buttheymustnotchangetheassignedhypothesis,inspectsiblingbranchesasshortcuts,oruse
dev
theheld-outevaluatorforroutineiteration.Theirreportsshouldbecompactenoughtobecometreeevidence:score,result,
insight,andbranchreference.
Mergeandterminationrules.
UseGitMergeBranchexclusivelyforpromotion;directgitmergesthroughBashareprohibited.
Beforeterminating,runtheheld-outevaluatoronboththefinalbestartifactandthebaselinewhenrequired,thenrecord
test_trunk_scoreandtest_baseline_scoreviaTreeSetMeta.Failed,pruned,andunmergedbranchesshouldremainin
thetreeasreusableevidenceratherthanbeingerasedfromtheresearchrecord.
24

B.1.2 ExecutorPrompt
ExecutorPrompt
YouareaResearchAgentthatimplementsresearchideasintocodebases,runsexperimentstoverifytheimplementation,
Identity.
andreportsresultshonestly. Youoperateautonomouslythroughatool-useloop. Thedirectionofeachideaisfixed. Your
engineeringjudgmentdetermineshowbesttoimplementitwithinthetargetcodebase.
Alltextoutputoutsideoftooluseisshowntotheuser. Toolresultsmaycontaindatafromexternalsources. If
System.
yoususpectatoolresultcontainsapromptinjectionattempt, flagitbeforecontinuing. Priormessagesarecompressed
automaticallyastheconversationapproachescontextlimits.
Readfilesbeforemodifyingthem.Donotcreatenewfilesunlessabsolutelynecessary.Diagnosefailurecauses
DoingTasks.
beforeswitchingtactics.Donotaddfeatures,refactors,docstrings,comments,ortypeannotationsbeyondwhattheassigned
idearequires.Verifythattheimplementationworksbeforereportingcompletion.
Evaluatethereversibilityofeachactionbeforeproceeding.Local,reversibleoperations(fileedits,
ExecutingActionswithCare.
runningtests)maybetakenfreely.Destructiveorhard-to-reverseoperations(deletingbranches,forcedresets,overwriting
uncommittedchanges)requirecarefulconsideration.Donotusedestructiveactionsasshortcutsorbypasssafetychecks.
YouareworkinginanisolatedgitworktreebranchedfromthecurrenttrunkHEAD.Allcodechanges
ExperimentWorkflow.
happenonthisexperimentbranch.Donotcommittomainormaster.BaselinescoresareprovidedintheEvaluationInfo
sectionofyourprompt.Runtheevaluationcommandontheunmodifiedcodebaseonlyifnobaselinescoresareprovided.
Saveexperimentresultstoresults/{node_id}-{description}/andcommitonlysmalldiagnosticfilesusinggit add -f.
UseRunTrainingforanytrainingorevaluationcommandthattakesmorethanfiveminutes.Donotusepollingloops.At
theend,provideaconcisereportwiththefollowingsections:Idea,Changes,ImplementationChoices,Baselinevs.Result,
Analysis,andInsights.
Theideadirectionisnon-negotiable.Youmaynotsubstituteafundamentallydifferentapproach.Implementation
CriticalRules.
choices(specificarchitecture,hyperparameters,codeplacement)areyours.Reportsignificantimplementationchoicesexplicitly.
Iftheideaunderperformsafteragood-faithimplementation,thatisthefindingtoreport.
B.2 AlgorithmWorkflow
Algorithm 2 expands the HTR pseudocode from the main paper (Algorithm 1) with implementation-level detail.
Notationfollowsthemainpaper:ι denotestheinsightrecordedatnoden,b thegitbranchreference,s theE
n n n dev
score,r thefactualresult,andι theconcatenatedinsightsonthepathfromn ton’sparent.
n anc(n) 0
B.3 KeyDesignofArborFramework
General-purposecodingagentssuchasCodexandClaudeCodearebuiltforgeneral-purposesoftwaretasks:they
chaintoolcallsonasingleworkingtreetoedit,test,andfixcodeagainstagoalthatisalreadywellspecified.Arbor
insteadtargetstheauto-researchsetting,andwemakeaseriesofengineeringchoicesthatspecializetheagentforit
sothatthesystemcanflexiblyadapttodifferentresearchneedsandmanagemanyexperimentsoveralonghorizon.
Wegroupitskeyengineeringdesignsintofourareas:(i)hypothesis-treemanagement,(ii)experimentmanagement,
(iii)long-horizonoperation,and(iv)functionalextensibilitythroughskillsandplugins.
Hypothesis-treemanagement. Unlikeacodeagentwhosememoryisthelinearchattranscript,Arborexter-
nalizes its research state into an explicit hypothesis tree (the idea tree), an in-memory object that is the single
authoritativerecordofarun.Eachnodeholdsahierarchicaldottedaddress(e.g.ROOT,1,1.1)thatencodesitspath
from the root, its parent_id and children_ids, a once-written hypothesis, a status field tracing the lifecycle
pending→running→done→{merged,pruned},adevelopmentscore,afactualresult,adistilledinsight,anda
code_refbranchpointertotheartifact.Depth-1nodesarebroaddirectionsanddeepernodesareconcreterefinements,
soedgesencodehypothesisrefinementratherthanchronologicalactions. Thecoordinatornevertouchestheraw
structure;itoperatesthetreeonlythroughasmallsetoftypedtools(TreeAddNode,TreeUpdateNode,TreePrune,
TreeSetMeta,TreePropagate)andreadprojections(TreeView).Storinganexperimentisthusacontrolledmutation:
theexecutor’sstructuredreportisparsedandwrittenintothenode’sscore/result/insight/code_reffields,and
thetreeisserializedtoJSON(andrenderedtoMarkdown)aftereverymutation.Crucially,whenanodefinishesArbor
backpropagatesitsinsight:propagate_insightswalksfromthenode’sparenttotherootand,ateachancestor,an
LLMsynthesizestheinsightsofthatancestor’schildrenintoaconcise(<200-word)summary.Leafinsightsdescribe
25

HypothesisTreeRefinement(HTR)withexpandedimplementationdetail.Thecoordinatorowns
Algorithm2:
Tree,andeachExecutorownsoneworktree.
Input :P =(M 0 ,O,E dev ,E test ),budgetB,branchingk,parallelismP
Output:
bestartifactM⋆,annotatedhypothesistreeTree,andrunsummaryreport
// Initialization
1
initTree=({n },∅),b ←M ,M ←M
2 0 n0 0 best 0
runE (M )andrecordbaselinescoreandevalcommandinTree.metaviaTreeSetMeta
3 dev 0
// Main coordinator loop
4
5
whileBleft∧pendingleavesexist∧nostopsignal
do
// Step 1: OBSERVE, build constraint view
6
V ←Observe(Tree,M ) // shape, root insight, pruned lessons, validated findings
7 best
// Step 2: IDEATE, skill-gated hypothesis proposal
8
V ←TreeView(format=constraints) // hard constraints: no re-tread of pruned directions
9 c
loadidea_draftingskillviaLoadSkill // mandatory gate: must precede any candidate proposal
10
p←Select (V)
11 parent
survivingcandidateafterFatal-FlawScan
12 foreach do
attachpendingchildn(i)withhypothesish(i)=(Mechanism,Hypothesis,Observable,Conflicts)
13
14
ι
anc(n(i))
←insightson path(n
0
→p) // injected into Executor prompt
pruneidea_draftingscratchfromcoordinatorcontext // elide skill body + reasoning post-TreeAddNode
15
16 endforeach
// Step 3: SELECT frontier for parallel dispatch
17
L←uptoP pendingleavesunderSelect (V)
18 frontier
// Step 4: DISPATCH, parallel Executor dispatch
19
20
{(s
n
,r
n
,ι
n
,b
n
)}
n∈L
←parallelExecutor(h
n
,ι
anc(n)
,M
best
)
// Step 5: UPDATE, write back and propagate
21
22
foreachn∈L,a∈path(n
0
→n)do
writeback(s ,r ,ι ,b )tonodeninTreeandsetn.status←done
23 n n n n
ι ←Abstract({ι } ) // propagate insights upward to root
24 a c c∈ch(a)
25 endforeach
checkconvergence:injectinterventionif≥wconsecutivenon-improvingexperiments
26
// Step 6: DECIDE, merge gate or prune
27
n† ←argmax s
28 n∈L n
29
ifs
n†
exceedsbestscoreby≥θthen
createdetachedworktreeatb andrunE withtemplatesubstitution
30 n† test
31
ifS
test
(b
n†
)>S
test
(M
best
)then M
best
←merge(b
n†
)andupdateTree.meta.trunk_score
32 endif
prunesubtreesfalsifiedby{ι } andpersistTreetoJSON+Markdown
33 n n∈L
34 endwhile
runE (M )andrecordtest_trunk_scoreandtest_baseline_score
35 test best
36
returnM⋆ ←M
best
,Tree,runsummary
37
ProcedureExecutor(h
n
, ι
anc(n)
, M
best
):
38
branchname←slug(node_id)+slug(h
n
)+SHA1(h
n
)
[:8]
createworktreeW in/tmp/fromcurrentbestbranchHEADonafreshbranch
39 n
injectevalcommand(with{cwd}→W ,{node_id}→n)andι intoprompt
40 n anc(n)
41 repeat
42
∆←Implement(h
n
,ι
anc(n)
,W
n
)
43
(s
n
,r
n
)←E
dev
(apply(∆,W
n
)) // repair ∆ only, direction h
n
is fixed
44 until
runok∧h
n
-pathexercised,orturncapreached
filter∆:commitimplementationfilesonly,skiplogs/checkpoints/caches
45
removeworktreedirectoryandretainbranchb forlatermergegate
46 n
47
return(s
n
, r
n
, Distill(h
n
,∆,r
n
), b
n
)
concreteimplementations,parentinsightssummarizefamiliesofinterventions,andtherootinsightmaintainsaglobal
understandingoftheproblem.Thislayerwiseabstractionletsthecoordinatorreasonattherightgranularitywithout
rereadingrawlogs.TheconcreteschemaandpersistenceformataredetailedinSectionB.5.
26

Experimentmanagement. EachpendingnodeisexecutedbyanexecutordispatchedthroughRunSubagentor
RunSubagentParallel. Ratherthaneditingthesharedworkingtreeinplace, Arborcreatesafreshgitworktree
branchedfromthecurrenttrunkHEADforeachcandidate,soeveryhypothesisgetsaclean,independentlyrecoverable
experimentalboundaryandseveralexecutorscaneditoverlappingfilesconcurrentlywithoutcorruptingthetrunkor
oneanother.Atlaunchtheexecutorisinjectedwiththeassignedhypothesis,theancestorinsightsalongitspath,and
thetaskobjective,developmentevaluatorE ,held-outevaluatorE ,metricdirection,datasplit,andbaselinescore
dev test
storedinthetreemetadataviaTreeSetMeta. Itspermissionboundaryisdeliberatelynarrow: theexecutor’stools
(Table8)actonlywithinitsownworktree.Itcannotreadthetrunk,inspectsiblingbranches,mutatethetree,orrun
E .Itmayrepairimplementationbugsandchoosereasonableengineeringdetails,butitmaynotswaptheassigned
test
hypothesisforadifferentresearchdirection,whichkeepsthereturnedevidenceattributabletothenodeactuallytested.
Theexecutorreportsbackfourseparatedfields: thedevelopmentscores ,afactualresultr (rawobservations
n n
suchaserrors,curves,andmetricbreakdowns),adistilledinsightι (thecausallesson),andthebranchreferenceb .
n n
Thecoordinatorauto-extractsthese,updatesthenode,anddecidesadmission:aresultcountsasausefulgainonly
whenitimprovesE overthetrunkbyatleastthemergethreshold,whichtriggerstheGitMergeBranchheld-out
dev
gatethatre-runsE inaseparatedetachedworktreeandpromotestheartifactonlyifitstrictlybeatsthecurrent
test
best.Everyotheroutcomeistreatedasfailureevidenceratherthannoise:thenode’sinsightand,ifthedirectionis
abandoned,itsTreePrunereasonareaggregatedintotheconstraintview(TreeView(format="constraints"))that
conditionsthenextIdeatestep,sonegativeresultsactivelynarrowthesearchspace.Tool-leveldetailsofdispatch,
scoreextraction,template-variablesubstitution({cwd},{node_id}),andartifactfilteringaregiveninSectionB.4.
Long-horizonoperation. Asingleauto-researchruncanspanhundredsofturnsandmanyhoursofevaluation,
farbeyondonecontextwindow,soArboraddsexplicitmechanismstokeepthesearchproductiveinsteadofstalling
onearlyfailuresorchasingnoisyevaluationswings.First,becausealldurablestatelivesinthepersistedideatree
ratherthanthetranscript,therunsurvivescrashes,agentrestarts,andcontextcompression;post-commitcontext
pruningfurtherelidesspentIdeatescratchworkandloadedskillbodiesonceacandidateiscommitted,bounding
contextgrowth.Second,longtrainingorevaluationcommandsareroutedthroughRunTraining,whichblocksuntil
completionortimeoutwhilecontinuouslycapturingpartialmetrics,progresslogs,andcheckpoints,soevenarun
thattimesoutat80%ofitsepochsreturnsactionableevidenceinsteadofasilentfailure.Third,aconvergencedetector
monitorsrecentscorevelocityoveraslidingwindowandcountsconsecutivenon-improvingexperiments,escalating
throughwarn,paradigm_shift,andstopsignals;italsoflagsparentexhaustionwhenaparent’srecentchildrenall
failtobeatthetrunk,promptingthecoordinatortosummarizethefailurepatternandopenafreshdepth-1direction
ratherthanover-exploringadeadbranch.Ameaningful-improvementthresholdpreventsasinglenoisyuptickfrom
resettingthissignal,balancingprematurestagnationagainstunboundedexploration.
Functionalextensibility(skillsandplugins). Toremainadaptableacrossresearchdomainswithoutchangingthe
coreloop,Arborexposestwoextensionsurfaces.SkillsaremarkdowndocumentswithYAMLfrontmatter,discovered
byaregistryfromboththebuilt-indirectoryandaproject-local.research_agent/skills/override,andloaded
on demand via LoadSkill. The Ideate protocol, for instance, loads idea_drafting, first_principles_probe,
andfatal_flaw_scanbeforeproposingcandidates,thenprunestheirbodiesfromcontextaftereachcommit,so
reasoningguidanceisinjectedjust-in-timeanddoesnotpermanentlyinflatecontext. Plugins areYAMLdomain
adaptersthatspecializethesystemdeclarativelyratherthanthroughcode:eachplugincaninjectdomainguidanceat
sixpromptpoints(coordinator/executorinit,ideate,decide,preamble,andworkflow),declareanevaluationcontract,
markprotected pathsand requiredoutputsfor themerge guard, overrideruntime configurationthrough named
profiles, andtuneconvergencethresholds. Forexample, themle_kagglepluginconfiguresaKaggle/MLE-bench
taskwithitsmetricdirection,evaluationcommand,protecteddatapaths,andtime-budgetprofilesentirelyinYAML.
Together,skillsandpluginsletArboradapttonewartifactsandevaluationregimeswhilekeepingthehypothesis-tree
machineryandagentcontractsunchanged.
B.4 AgentToolsandHyperparameterSettings
B.4.1 CoordinatorTools
Thecoordinator’stoolsetreflectsastrictdivisionoflabor: itmayreadanyfileintherepositoryandinspectthe
treeinanyprojection,butitmaynevereditcodedirectly. Allimplementationworkisdelegatedtoexecutorsvia
RunSubagent or RunSubagentParallel. This design is intentional. If the coordinator could edit code directly, it
27

wouldbetemptedtomakesmalllocalfixeswithoutcreatinganewtreenode,whichwouldbreaktheinvariantthat
everycodechangeistraceabletoahypothesis.Enforcingtheeditboundaryatthetoollevelmakesthisinvarianta
systempropertyratherthanabehavioralexpectation.
Table6liststhefulltoolset. Thetreetools(TreeView,TreeAddNode,TreeUpdateNode,TreePrune,TreeSetMeta,
TreePropagate)aretheprimaryinterfacethroughwhichthecoordinatormanagesthesharedresearchstate. The
dispatchtools(RunSubagent,RunSubagentParallel)aretheboundarythroughwhichthecoordinatorhandsoff
implementationtoexecutorsandreceivesstructuredevidenceback.Themergetool(GitMergeBranch)istheonlypath
throughwhichacandidatebranchcanbepromotedtothecurrentbest,enforcingtheheld-outgateatthetoollevel
ratherthanrelyingonthecoordinatortoremembertoverifybeforemerging.Table7reportsthekeyhyperparameters
usedacrossallexperiments.
Toolsavailabletothecoordinator.
Table6
Tool Description
TreeView Inspecttheideatreeinfiveformats:compact(statusoverview),full(Markdownrendering),node
(single-nodedetail),pending(pendingleaflist),andconstraints(aggregatedprunedlessonsandvalidated
findingsusedashardconstraintsintheIDEATEphase).
TreeAddNode Addachildnodetothetreewithafour-fieldhypothesisblock(Mechanism,Hypothesis,Observable,
Conflicts).TriggersIDEATEcontextpruningaftereachcommit.
TreeUpdateNode Updatemutablefieldsofanexistingnode(status,insight,score,result,code_ref,related_work).
TreePrune Markanodeanditssubtreeasprunedwithawrittenreason.Thereasonisaggregatedintotheconstraints
blockforfutureIDEATErounds.
TreeSetMeta Writeevaluationmetadatatothetreeroot:evaluationcommands(eval_cmd,eval_cmd_test),datasetpaths,
baselinescore,bestscore,andtestscores.AutomaticallyinjectedintoeveryExecutor’sprompt.
TreePropagate Re-propagateinsightsfromanodeupwardtotherootaftermanualcorrectionsviaTreeUpdateNode.
RunSubagent DispatchasingleExecutortoimplementandevaluateapendingtreenode.Createsanisolatedgitworktree
fromtrunkHEAD,injectsancestorinsightsandevaluationmetadata,auto-extractsresultsfromthestructured
report,andupdatesthetreenode.
RunSubagentParallel DispatchtwotofourExecutorsconcurrentlyonindependenttreenodes.EachExecutorrunsinitsown
isolatedworktree.
GitMergeBranch Validateandpromoteacandidatebranchtothecurrentbest.Createsatemporarydetachedworktreeatthe
sourcebranch,runsEtest withscoreextraction,andmergesonlyifthevalidatedtestscoreexceedsthe
currentbestscore.Protectedbranches(main,master)cannotbemergetargets.
Bash Executeshellcommandsforread-onlycodebaseinspectionandenvironmentqueries.Thecoordinatornever
usesBashtoeditcode.
FileRead Readthecontentsofafilewithinthetargetrepository.
Grep Searchforatextpatternacrossrepositoryfiles.
Glob Findfilesmatchingaglobpatternwithintherepository.
LoadSkill Loadaskilldocumentondemandfromtheregistry.IntheIDEATEprotocol,idea_drafting,
first_principles_probe,andfatal_flaw_scanareloadedbeforeproposingcandidates.Loadedcontent
isprunedfromcontextaftereachTreeAddNodecommit.
SearchIdeaContext DispatchaSearchAgentinthebackgroundtoannotateatreenodewithrelatedwork.Returnsimmediately.
TheSearchAgentrunsconcurrentlywithongoingIDEATEanddispatchworkandwritesastructured
annotation(summary,noveltyassessment,relatedpapers)tonode.related_workwhenfinished.
SearchIdeaContextParallel DispatchmultiplebackgroundSearchAgentsconcurrentlyforalistofnodeIDs.
SearchStatus Returnthecountofin-flightbackgroundSearchAgenttasks.
B.4.2 ExecutorTools
Theexecutor’stoolsetisdesignedaroundasingleconstraint:everyactionmustbelocaltoitsworktree.Theexecutor
hasnotoolsforreadingthecurrentbest,inspectingsiblingbranches,ormodifyingthesharedtree.Thisisolationisnot
merelyasafetymeasure.Itiswhatallowsmultipleexecutorstorunconcurrentlyonoverlappingcodebaseswithout
coordinationoverhead.Eachexecutoroperatesasifithasanexclusivecopyoftherepository,becauseitsworktree
isliterallyaseparatechecked-outdirectorythatsharesthegitobjectstorebutmaintainsitsownHEADandindex.
TheRunTrainingtooldeservesspecialmention:forexperimentsthatinvolvemulti-hourtrainingruns,usingBash
withatimeoutwouldeithercuttherunshortorblocktheexecutorforanunboundedduration.RunTraininginstead
blocksuntilthecommandterminatesortheconfiguredtimeoutisreached, continuouslycapturingintermediate
metrics,progresslogs,andcheckpointssothatevenatimed-outrunreturnsactionablepartialevidence.Thismatters
inpractice:atrainingrunthatcompletes80%ofitsepochsbeforetimingoutoftenrevealsenoughaboutadirection’s
trajectorytoinformaprincipledpruneorcontinuationdecision,whichismoreusefulthanasilenttimeoutthatleaves
thecoordinatorwithoutevidence.
28

Table7
KeyhyperparametersfortheArborcoordinatorandexecutors.
Parameter Default Description
Backbonemodel ClaudeOpus4.6 LLMforbothcoordinatorandexecutors(configurableperrole)
Maxcycles 20 Hardcapontotalcompletedexperiments
Maxcoordinatorturns 500 MaximumReActturnsforthepersistentcoordinatorloop
Executormaxturns 50 Maximumturnsperexecutor
Executortimeout 48h Wall-clocklimitperexecutor
Contextwindow 200Ktokens Coordinatorcontextlimit
Compressionthreshold 0.80 Compresscontextwhenitreaches80%ofthecontextwindow
Keptrecentturns 20 Numberofmostrecentturnspreservedaftereachcompression
Mergethreshold 5.0% MinimumE improvementrequiredtoinvokethemergegate
dev
E evaluationretries 1 Additionalheld-outevaluationattemptsafteratransientfailure
test
Convergencewindow 5 Slidingwindowsizeforscorevelocitycomputation
Convergencewarn/stop 3/8 Consecutivenon-improvingexperimentstotriggerwarning/stop
Toolsavailabletoeachexecutor.
Table8
Tool Description
Bash Executeshellcommandsintheworktreewithconfigurableper-calltimeouts(default600s,maximum
86,400s).
RunTraining Executealong-runningtrainingorevaluationcommandandblockuntilcompletionortimeout.
Automaticallycapturespartialmetrics,progresslogs,andcheckpoints.Supportsstagedbudgets(smoke,
pilot,full)withconfigurablewall-times.Maximumtimeoutis604,800s(sevendays).
FileRead Readthefullcontentsofafilewithintheworktree.
FileEdit Editafilebyreplacinganexactstringmatchwithnewcontent,enablingsurgicaleditsthatminimize
unintendedsideeffects.
FileWrite Writethecompletecontentsofafile,creatingoroverwritingit.
Grep Searchforatextorregexpatternacrossfilesintheworktree.
Glob Findfilesmatchingaglobpatternwithintheworktree.
SubAgent Spawnanestedexecutorwithacustompromptformodulardecompositionofcompleximplementation
tasks.Thenestedagentinheritsthesametoolsetandworktreecontext.
29

B.4.3 EvaluationandMergeTools
Arecurringchallengeinmulti-agentsystemsisensuringthatevaluationcommandsmeasuretherightcode.InArbor,
eachexecutorrunsinadifferentdirectory,onadifferentbranch,withpotentiallydifferentdatalocations.Anaively
hardcodedevaluationcommandwouldsilentlyevaluatethewrongartifact.Thetemplatevariablesystemaddresses
thisbyrequiringthecoordinatortospecifyevaluationcommandsusingtwoplaceholders:{cwd}issubstitutedwith
theexecutor’sworktreepathbeforethecommandreachestheexecutor’sprompt,and{node_id}issubstitutedwith
thetreenodeidentifiersothatresultsfromconcurrentexperimentsarewrittentodistinctoutputlocationsandnever
overwriteoneanother. Thecoordinatorisalsoexplicitlyprohibitedfromhardcodingabsolutepathsinevaluation
commands.Only{cwd}-relativepathsarepermitted.
Scoreextractionfromevaluatoroutputfollowsatwo-stagepipelinethathandlesthediversityofrealevaluation
scripts.ManyharnessesalreadyemitastructuredJSONblockwithascorekey.Thesystemattemptstoparsethis
first. IfnovalidJSONblockisfound,asiscommonwithtrainingscriptsthatreportlossoraccuracyinfree-form
loglines,asecondaryLLMcallreadsthefullcommandoutputandextractstheprimarymetricasapercentage.The
distinctionbetweenaprimarymetricandancillaryloggingistask-specific,sotheLLMcallusesaconcisesystem
promptthatinstructsittoreturnonlyasingleJSONobjectandtopickthemostprominentperformancefigureif
multiplemetricsappear.
Theheld-outevaluatorE isarchitecturallyseparatedfromthedevelopmentloop.Executorsareinstructednever
test
torunE .ItisaccessibleonlythroughtheGitMergeBranchtool,whichcreatesafreshdetachedworktreeatthe
test
candidatebranch’sHEAD,appliesthesametemplatesubstitution,andrunseval_cmd_testincompleteisolation
fromthemainrepository.Configurableretrylogicwithexponentialbackoffhandlestransientinfrastructurefailures
suchasgpuallocationtimeoutsorflakynetworkreads.Themergeisadmittedonlyiftheextractedtestscorestrictly
exceedsthecurrentbestscoreunderthemetricdirectionspecifiedinthetask.Thistwo-worktreedesignusesone
worktreefordevelopmentevaluationinsidetheexecutorandoneforheld-outevaluationinsidethemergegate.It
ensuresthatneithertheexecutornorthecoordinatoreverevaluatesthecandidateartifactinthesamedirectoryasthe
currentbest,eliminatinganyriskofresultleakagebetweenbranches.
Beforeaworktreebranchiscommitted,Arborappliesartifactfilteringtoseparateimplementationchangesfrom
generatedoutputs.Thesysteminspectsthefullworktreediffandclassifieschangedpathsaseitherimplementation
filesorartifacts.Rawlogs,modelcheckpoints,cachedirectories,generateddata,andlargebinaryfilesareexcluded
fromthecommit,keepingexperimentbranchescompactandensuringthatsubsequentthree-waymergesintothe
currentbestbranchinvolveonlymeaningfulcodedifferences.Thisfilteringisconservativebydesign:aborderline
fileisincludedratherthanexcluded,becauseamissingimplementationfilebreaksthemerge,whereasaspurious
largefileonlyaddsstorageoverhead.
B.5 IdeaTreeDataStructureandStorage
TheimplementationstoresArbor’shypothesistreeasanidea-treeobject. Thisobjectistheprimarydurabledata
structureofarun:itrecordstheresearchfrontier,completedexperiments,rejecteddirections,acceptedartifacts,and
reusableinsightsinoneinspectablestate.
Logical schema. The root node anchors the initial artifact and task contract. Depth-1 nodes represent broad
researchdirections,whiledeepernodesrepresentconcreterefinements,alternatives,orcorrectionsundertheirparent.
Edgesthereforeencodehypothesisrefinementratherthanchronologicalagentactions.Duringarun,pendingleaves
formtheexecutablefrontier;completed,merged,andprunednodesremaininthetreeasevidenceforfutureproposal
andselection.EachnodecarriesthefieldslistedinTable9.
Persistent storage. The idea tree is serialized to JSON after every controlled mutation and serves as the sole
authoritativerecordofresearchstateaccumulatedduringarun.Nohypothesis,score,artifactreference,orlesson
existsoutsidethisstructure.ThesamestateisalsorenderedtoMarkdownfordashboardsandhumaninspection.The
JSONrepresentationisconsumedbytools,whiletheMarkdownviewprovidesareadableaccountoftheresearch
process.Sinceeverymutationispersistedimmediately,theruncanrecoverfromcrashes,agentrestarts,andcontext-
windowcompressionwithoutrelyingonconversationalmemory.
30

Fieldsofasinglenodeintheideatree.Thefirstfourfieldsformthestructuralskeleton;theremainingfieldsarepopulated
Table9
progressivelyasthenodemovesthroughitsstatuslifecycle.
Field Type Description
id string Hierarchicaladdressencodingpositioninthetree(e.g."ROOT","1","1.1").The
dot-separatedprefixgivestheuniquepathfromroot.
parent_id string|null Identifieroftheparentnode.nullfortheroot.
children_ids list[string] Orderedidentifiersofchildnodes,appendedasthecoordinatorexpandsthetree
duringIdeate.
depth int Integerdepth:0=root,1=directionnode,2=branchnode.Themaximumdepth
isgovernedbymax_depth.
hypothesis string Researchhypothesisassignedbeforeexecution.Writtenoncebythecoordinator
duringIdeateandnevermodifiedthereafter.
status {pending,running, Statuslifecycle:pending→running→done,thendone→mergedifthemerge
done,merged, gatepasses,ordone→prunedotherwise.
pruned}
score float|null AbsolutescalarscoreonE asreportedbytheexecutor.Nulluntilthenodehas
dev
beenexecutedandscored.
result string Factualrecordoftheexperimentoutcome,writtenbytheexecutorasadirect
observationalreportbeforeanyinterpretationisapplied.
insight string StructuredlessonextractedbyDistillfromtheoutcome,thenbackpropagatedand
aggregatedateachancestoruptotheroot.
code_ref string|null Gitbranchnamepointingtotheimplementationartifactproducedbytheexecutor.
Nullifnoartifactwascommitted.
Agent-facingaccess. AgentsdonotedittherawJSONfiledirectly. Thecoordinatoraccessesthetreethrough
controlledreadviewsandmutationtools: compactfrontierviews,single-nodeviews,pending-leafviews,andthe
constraintviewusedbeforeideation;plusmutationsforaddingnodes,updatinglifecyclefields,pruningsubtrees,
settingmetadata,andpropagatinginsights.Executorsreceiveonlytheassignedhypothesis,theresearchcontract,and
ancestorinsights.Thisaccesspatternkeepsthetreeasasharedstateobjectratherthanalow-levellogoftooltraces.
C DetailsoftheAOTestSuite
C.1 OptimizerDesign
NanoGPT-Bench(Jordanandcontributors,2025)Track3isacollaborativebenchmarkfordiscoveringefficientneural
networkoptimizers.UnlikethemainNanoGPTspeedrun,whichminimizeswall-clocktimebyanymeans,Track3
targetsstepcount:methodsthatareslowinwall-clocktermsbutreachthetargetlossinfewerstepsarevalidand
desirable.Alloptimizerdesignsareevaluatedonthesamefixedarchitecture,dataset,andtrainingscript,sotheonly
leveravailableistheoptimizationalgorithmanditshyperparameters.
Baseline. WeinitializefromtheofficialtunedMuonoptimizersettingprovidedbythebenchmarkauthors.This
configurationappliesMuontotransformerblockweightsandAdamWtoembeddings,theoutputprojection,and
scalarparameters(biasesandgains).Withthesetunedhyperparameters,thebaselinereachesaFineWebvalidation
lossof≤3.28in3,325steps.Selectingawell-tunedofficialbaselineasthestartingmaterialisintentional:itplacesthe
agentinaregimewherenaivehyperparametersweepsareunlikelytoyieldlargegains,therebytestingtheagent’s
abilitytoidentifyandimplementgenuinelynoveloptimizerimprovementsratherthanharvestingeasywinsfroman
undertunedstartingpoint.
Developmentandtestsplit. Agentsiteratewiththedevelopmentevaluatorthroughoutthesearchloop.Afterthe
searchcompletes,theselectedoptimizerisre-evaluatedwithtwoheld-outrandomseeds,andthereportedtestscore
istheaveragestepcountacrossthoseruns.
31

Evaluator. Theevaluatorrunsthebenchmark’sofficialevaluationscriptrun_eval.py. Thescriptlaunchesthe
trainingjob,monitorsvalidationloss,andterminatesassoonasval_loss≤3.28isfirstreached.Thescoreisthe
stepcountattermination,withlowerbeingbetter.Ifthetargetisneverreached,apenaltyscoreexceeding7,000is
assigned.AllevaluationrunsareexecutedonfourNVIDIAA100-80GBGPUsusingtheofficialbenchmarkevaluation
code.
Agentinstruction. Theagentisinitializedwiththefollowingtaskdescription.
OptimizerDesignTaskInstruction
Improvethetraining-stepefficiencyoftheNanoGPToptimizeronFineWeb.Thetrainingscripttrain_gpt_simple.pytrains
a124M-parameterGPT-2onFineWebusingMuonfortransformerweightsandAdamWforembeddings,outputprojection,
andscalarparameters.
Goal.
Minimizethenumberoftrainingstepsrequiredtoreachval_loss≤3.28.Thecurrentbaselineachievesthistargetin
3,325steps.
Evaluation.
Runpython run_eval.pyfromtheprojectdirectory.Thescriptlaunchestraining,monitorsvalidationloss,and
terminatesatthefirststepwhereval_loss≤3.28.Thescoreisthestepcountattermination,withlowerbeingbetter.Ifthe
targetisneverreached,apenaltyscoreexceeding7,000isassigned.
Constraints.
Onlytrain_gpt_simple.pymaybemodified. Thedataset,batchsize,andmodelarchitecturemustremain
unchanged.Adjustingtrain_stepsinisolationisnotavalidimprovement.Multipleforwardpassespersteparenotpermitted.
C.2 ArchitectureDesign
ArchitectureDesignusestheautoresearchbenchmark(Karpathy,2026),acompactLLMpretrainingtaskdesigned
forclosed-loopresearchonarealtrainingcodebase. Theagentreceivesasingle-filetrainingimplementationand
mustimprovethefinalvalidationlossunderafixedwall-clocktrainingbudget.UnlikeOptimizerDesign,wherethe
modelarchitectureisfixedandonlytheoptimizerismodified,thistaskexposesthefulltrainingrecipe:modelshape,
attentionpattern,initialization,optimizerhyperparameters,learning-rateschedules,batchsizing,andtraining-loop
detailsmayallbechangedaslongasthebenchmarkevaluatoranddatapreparationremainfixed.
Baseline. Theinitialmaterialisthedefaultautoresearchrepository.Themainartifactistrain.py,asingle-GPU
decoder-only Transformer pretraining script derived from nanochat. Data preparation, tokenization, validation-
tokenselection,andevaluationhelpersliveoutsidetheeditableartifact,primarilyinprepare.py.Thedevelopment
evaluatorusesthefixedvalidationshardprovidedbythebenchmark.Thedefaultmodelisaroughly50M-parameter
Transformer,andthebaselinereportsthefinalvalidationbits-per-byteafterthefixedtrainingrun.
Developmentandtestsplit. Duringsearch,agentsoptimizeonlyagainstthedevelopmentevaluator,whichruns
thetrainingscriptonthebenchmark’sfixedprepareddataandreportsthefinalvalidationloss.Theheld-outscore
reportedinthemainexperimentsisobtainedbyrerunningtheselectedtrain.pywithtwoheld-outrandomseeds
andaveragingtheresultingfinallosses.Thisseparatesthefast,single-runfeedbackusedforhypothesisexploration
fromtheseed-averagedscoreusedforfinalcomparison.
Evaluator. Theevaluatorexecutesuv run train.pyfromthebenchmarkrepository.Attheendoftrainingthe
scriptprintsastructuredsummaryincludingval_bpb,peak_vram_mb,training_seconds,num_steps,andmfu_-
percent.Theprimaryscoreisthefinalval_bpb,withlowervaluesbetter.Thetrainingscriptenforcesa300-second
trainingbudget;runsthatcrash,timeout,failtofitinmemory,ordonotemitaparseablefinalval_bpbaretreated
asfailedexperiments.Theagentmayusesecondarydiagnosticssuchasstepcountandpeakmemorytointerpret
failures,butmergedecisionsarebasedonthelossmetric.
Agentinstruction. Theagentisinitializedwiththefollowingtaskdescription.
32

ArchitectureDesignTaskInstruction
Followprogram.mdastheauthoritativetaskspecificationfortheautoresearchrepository.
Goal. Minimizethevalidationbits-per-byte(val_bpb)reportedbyuv run train.py.Lowerisbetter.
Evaluation. Runuv run train.pyfromtheprojectdirectoryandextractthefinalval_bpb,togetherwithpeak_vram_mb,
training_seconds,num_steps,andmfu_percentfordiagnostics.Thescripthasafixed5-minutetrainingbudget.Ifarun
crashes,runsoutofmemory,exceedstheallowedwall-clockbudget,ordoesnotproduceaparseablefinalloss,treatitasa
failedexperimentunlessthereisanobviousimplementationbugthatcanbecorrectedquickly.
Constraints.
Onlytrain.pymaybemodified. Architecture,hyperparameters,optimizerbehavior,batchsize,modelsize,
attentionpattern,initialization,schedules,andtraining-loopdetailsareinscope. Donotmodifyprepare.py,especially
TIME_BUDGET,MAX_SEQ_LEN,EVAL_TOKENS,make_dataloader,orevaluate_bpb.Donotmodifydatafiles,tokenizerartifacts,
pyproject.toml,uv.lock,orinstallnewdependencies.
C.3 Terminal-Bench2.0
Terminal-Bench2.0(Merrilletal.,2026)isabenchmarkforevaluatingterminalagentsonrealisticcommand-line
tasksexecutedinsideisolatedDockercontainers.Tasksspan16categories,includingsoftwareengineering,security,
scientificcomputing,datascience,games,debugging,andothers,acrosseasy,medium,andharddifficultylevels.The
fulltaskpoolcontains89tasks.
Baseline. Priorharness-engineeringstudiesmaybeginfromcodebasevariantsthatdifferininterfaceextensibility,
toolset,orpromptstructure,creatingcomparisonconfounds.Toensureafairandreproduciblestartingpointweuse
theofficialterminal-agentcodebase(terminus-2)distributedwiththebenchmarkverbatim,withoutanymodifications
andwithoutintroducingadditionalinterfaces.ThebackbonemodelisGPT-5.5.TheagentoperatesasaReAct-style
loopthatissuestmuxkeystrokestoapersistentterminalsession.
Developmentandtestsplit. Westratifythe89tasksbydifficultyandsamplea36-taskdevelopmentsetanda
53-taskheld-outtestset. Thestratificationensuresthatbothsplitshavebalanceddifficultycoverage,preventing
a scenario where the agent is evaluated on an atypically easy or hard subset. Agents iterate exclusively on the
developmentsetduringtheresearchloop.Thetestsetisevaluatedonlyonceafterthesearchcompletes,toreport
held-outperformance.
Evaluator. The evaluator is the official Harbor evaluation harness distributed with Terminal-Bench 2.0. Both
developmentandtestevaluationsuse8concurrentworkers.Theevaluatorreportspassrateasthefractionoftasks
solvedcorrectly,withhigherbeingbetter.Thebaselineachieves58.33%onthedevelopmentset(21outof36tasks).
Agentinstruction. Theagentisinitializedwiththefollowingtaskdescription.
Terminal-Bench2.0TaskInstruction
Improve the pass rate of a terminal agent on Terminal-Bench 2.0. The current baseline achieves 58.33% on the 36-task
developmentsetusingGPT-5.5.
Maximizepassrateonthedevelopmentsplit.Iterateonthedevelopmentsplitexclusively.Evaluatetheheld-outtest
Goal.
splitonlyafterachievingameaningfulimprovementondevelopment.
Evaluation. Development: HARBOR_N_CONCURRENT=8 python3 run_eval.py –data data/dev.json. Test: HARBOR_N_-
CONCURRENT=8 python3 run_eval.py –data data/test.json. Thescoreisthefractionoftaskssolvedcorrectly,with
higherbeingbetter.
Modifiablecomponentsincludethesystemprompt,per-taskextrainstructions,theagentsubclass,thebaseagent
Constraints.
anditsReActloop,responseparsers,terminalsessionmanagement,andnewfilesundertheagentorpromptsdirectories.The
evaluationharness,taskdatafiles,APIconfiguration,andbaselinereferencerecordmustnotbemodified.
C.4 BrowseComp
BrowseComp(Weietal.,2025)isasearch-agentbenchmarkformulti-stepquestionanswering.Thematerialtobe
optimizedisnotthebenchmarkdataitself,butaminimalReAct-stylebrowsingharness(Yaoetal.,2023b)thatanswers
33

BrowseCompquestionsusingsearchandpage-readingtools.Thetaskmeasureswhetheranautonomousresearch
agentcanimprovethecontrollogicaroundasearchagentwhileleavingtheevaluatorandquestionsetsfixed.
Baseline. TheinitialmaterialisasimpleReAct-basedsearchharnesscenteredonsingle_agent_gpt.py.Foreach
question,aGPTAgentrunsasingleReActtrajectorywithasystemprompt,issuesweb-searchandpage-visittoolcalls,
andreturnsashortfinalanswer.TheonlineBrowseCompsettingusesSearchToolandVisitTool;thelocal-corpus
toolvariantsareavailableinthecodebasebutarenottheprimarypathforthisbenchmark. Thebaselineusesthe
simple-evalsBrowseCompquerytemplateandgradertemplate,withthesamemodelfamilyusedfortheanswering
agentandthegraderinthereportedruns.
Developmentandtestsplit. Thedevelopmentsplitcontains50BrowseCompquestionsandisusedforalliterative
optimization.Theheld-outtestsplitcontains300non-overlappingBrowseCompquestionsandisreservedforfinal
verification. In the released harness, these splits are exposed as data/bc_val.jsonl and data/bc_test.jsonl.
Agentsmayinspectandevaluateonthedevelopmentsplitduringthesearchloop,buttheymaynotediteitherdata
fileorusethetestsplitforiteration.
Evaluator. Thedevelopmentevaluatorisuv run python run_eval.py –data data/bc_val.jsonl –workers 8
–run-name {node_id}.Theheld-outevaluatorusesthesameentrypointwithdata/bc_test.jsonlandadistinct
runname.Theevaluatorsendseachquestiontotheharness,collectsthefinalanswer,normalizesitthroughthefixed
BrowseCompanswer-gradingpath,andreportsaccuracyascorrect/total.Itemswithrepeatedexecutionerrors
orunparsablefinalanswersarecountedaserrorsanddonotcontributetothecorrectcount.Theprimarymetricis
accuracy,withhighervaluesbetter.
Searchandtoolconfiguration. Theharnessexposestwobrowsingtoolstotheansweringagent. SearchTool
acceptsoneormoresearchqueriesandreturnscompactwebsearchresults,whileVisitToolfetchesandcleans
pagecontentforaselectedURL.Thetoolnamesandargumentschemasarefixedsothatalternativeharnessdesigns
remaincompatiblewiththesameReActagentinterface.Agentsmaychangethesystemprompt,rolloutorchestration,
responseparsing,candidateaggregation,andotherharnesscode,buttheevaluationscript,questionfiles,grader
template,andreferenceanswersarefixed.
Transfer-testprotocol. AfteroptimizationonBrowseComp,theresultingsearchharnessisfrozenandevaluated
directlyonunseensearch-agenttasks,includingHLEandDeepSearchQA,withoutadditionaltask-specificoptimization.
Thesamecodepath,search/visittoolinterface,andanswer-productionprotocolarereused.Thistransfertestchecks
whetherthediscoveredharnesschangesimprovegeneralbrowsingbehaviorratherthanmerelyfittingtheBrowseComp
developmentquestions.
Agentinstruction. Theagentisinitializedwiththefollowingtaskdescription.
BrowseCompTaskInstruction
OptimizeBrowseCompsearch-agentaccuracystartingfromthesimplebaselineonthecurrentmainbranch.Donotuseprior
optimizedbranches,cachedscores,oroldresultdirectoriesasthestartingpoint.
MaximizeansweraccuracyontheBrowseCompdevelopmentsplit.Usedevelopmentfeedbacktoproposeandevaluate
Goal.
harnesschanges,andreservetheheld-outtestsplitforfinalverification.
Evaluation. Development:uv run python run_eval.py –data data/bc_val.jsonl –workers 8 –run-name {node_id}.
Test:uv run python run_eval.py –data data/bc_test.jsonl –workers 8 –run-name {node_id}_test.Theevaluator
usesthefixedsimple-evalsBrowseComppromptandLLMgrader.Thescoreisaccuracy,withhighervaluesbetter.
Constraints.
The agent may modify the search harness, including single_agent_gpt.py, prompts, agent-control logic,
responseparsers,rolloutstrategies,andaggregationcode.Donotmodifyrun_eval.py,thedevelopmentortestdatafiles,
APIconfiguration,thegradertemplate,orcachedreferencerecords.
C.5 Search-AgentDataSynthesis
Search-Agent Data Synthesis is a pipeline-optimization benchmark that evaluates whether a research agent can
improveasyntheticquestion-answeringgenerationsystem.ThesystembeginsfromWikipedia-derivedtopicseeds
34

andproducesBrowseComp-styleinformation-retrievalquestions.Ahigh-qualitygenerateditemmustsatisfythree
properties simultaneously: structural well-formedness, answerability by a search-enabled model, and sufficient
difficulty that the solver does not answer it reliably in a single attempt. The task therefore measures not only
whethergeneratedquestionsareanswerable,butalsowhethertheyrequiremulti-stepevidencegatheringratherthan
surface-levellookup.
Baseline. Theinitialmaterialistheunmodifieddefaultdata-synthesispipelinedistributedwiththebenchmark.
Thebaselinepipelineconsistsoffivestages:extractingcandidatefactsfromatopicseed,ratingfactsbyinformation
value,constructingaquestionwhoseanswerisoneselectedfact,obfuscatingthetopicwithsupportingconstraints,
andapplyingstructuralverification. Thegenerator,solver,andjudgeuseGPT-5.5throughanOpenAI-compatible
interface.
Development and test split. The benchmark provides frozen seed snapshots for both evaluation splits. The
developmentsplitcontains50seedsandisusedexclusivelyforiterativeoptimization.Theheld-outtestsplitcontains
100 seeds and is reserved for final verification after the search loop completes. The pipeline generates at most
oneQAitemperseed. Fixingtheseedsnapshotsmakesthebenchmarkself-containedandensuresthatmeasured
improvementsreflectchangestothesynthesismechanismratherthanchangestothedatadistribution.
Evaluator. Theevaluatoristhebenchmark’sfixedrun_eval.pyentrypoint.Itloadstherequestedseedsplit,runs
thesynthesispipeline,solveseachgenerateditemfourtimeswithaweb-search-enabledReActmodel,andreportsa
JSONsummaryonthefinallineofstandardoutput.Theprimarymetricis:
N
1 (cid:88)(cid:0) (cid:1)
score = pass@4−pass@1 ,
N
i=1
wherepass@1is1ifthefirstattemptisjudgedcorrect,andpass@4is1ifatleastoneoffourattemptsiscorrect.
Higherscoresindicatequestionsthatremainsolvableinprinciplebutarenotansweredreliablyonthefirstattempt.
Agentinstruction. Theagentisinitializedwiththefollowingtaskdescription.
Search-AgentDataSynthesisTaskInstruction
Improvethequalityofgeneratedsearch-intensiveQAitemsbyoptimizingthedata-synthesispipeline.Thegoalmetricrewards
itemsthataresolvableunderrepeatedattemptsbutnotansweredreliablyonthefirstattempt:
score = mean(pass@4−pass@1).
Maximizethescoreonthedevelopmentsplit.Prefermechanism-levelimprovementsthatpreservewell-formednessand
Goal.
solvabilitywhileincreasingmulti-stepevidencegathering.
Evaluation. Development: python run_eval.py –split dev. Test: python run_eval.py –split test. Iterateonthe
developmentsplit.Runthetestsplitonlyafterameaningfulimprovement.
Constraints.
Onlythesynthesispipelineunderpipeline/maybemodified,includingpipelinesteps,theasyncrunner,the
stepregistry,pipelineconfiguration,andpromptfiles.Thescoringmodule,evaluationharness,benchmarkconfiguration,and
frozenseedsnapshotsmustnotbemodified.
C.6 Math-ReasoningDataSynthesis
Math-ReasoningDataSynthesisisapipeline-optimizationbenchmarkthatevaluateswhetheraresearchagentcanim-
proveasystemforgeneratingmathematicalcontestproblems.ThepipelinestartsfromfixedAIME/AIMO/NuminaMath-
styleseedsandproducesoriginalproblemswithexactintegeranswersintherange0–999.Theresearchtargetisthe
data-constructionmechanismitself:generatedproblemsmustbevalid,novel,diverse,mathematicallywellspecified,
andcalibratedsothatafixedreferencesolverdoesnotanswerthemtrivially.
35

Baseline. Theinitialmaterialistheunmodifieddefaultsynthesispipelinedistributedwiththebenchmark. The
pipelinetakeseachseed,generatesseveralcandidatecontestproblems,filterscandidatesforanswerformat,rationale
consistency,held-outoverlap,andnear-duplicateoverlap,andevaluatessurvivingcandidateswithafixedsolver.The
defaultgeneratorusesGPT-5.5-miniandthereferencesolverusesGPT-5.5.Theanswerpolicyisinteger_0_999.
Developmentandtestsplit. Thebenchmarkuseslockedseedfilesforbothevaluationsplits.Thedevelopment
splitcontains10seedswith5generatedcandidatesperseed,yieldingupto50candidatestotal. Theheld-outtest
splitcontains12seedswith8generatedcandidatesperseed,yieldingupto96candidatestotal.Eachseedspecifiesa
mathematicaltopic,technique,andtargetdifficulty.Agentsiterateexclusivelyonthedevelopmentsplitduringthe
researchloop.thetestsplitisreservedformilestoneandfinalverification.
Evaluator. Theevaluatoristhefixedrun_eval.pyentrypoint. Itloadstherequestedsplit, runsthesynthesis
pipeline,appliesvalidityandnoveltyfilters,evaluateseachsurvivingcandidatewiththefixedsolver,andprintsa
JSONmetricsobjectonthefinallineofstandardoutput.Theprimarymetricis:
N
1 (cid:88)(cid:0) (cid:1)
score = pass@4−pass@1 ,
N
i=1
whereN isthenumberofgeneratedcandidatesbeforefiltering,pass@1indicateswhetherthefirstsolversampleis
correct,andpass@4indicateswhetheratleastoneoffoursolversamplesiscorrect.Filteredcandidatesaretreatedas
zero.Thismetricrewardsproblemsthataresolvableunderrepeatedattemptsbutnotimmediatelysolvedonthefirst
sample.
Agentinstruction. Theagentisinitializedwiththefollowingtaskdescription.
Math-ReasoningDataSynthesisTaskInstruction
ImproveapipelinethatgeneratesAIME/NuminaMath-stylecontestproblemswithexactintegeranswersintherange0–999.
Generatedproblemsmustbevalid,novel,diverse,andcalibratedsothatthefixedreferencesolverfailsonthefirstsamplebut
succeedswithinfoursamples.Theprimarymetricismean(pass@4−pass@1)overallgeneratedcandidates.
Maximizetheprimarymetricreportedonthefinalstandard-outputlineoftheevaluator. Prefermechanism-level
Goal.
improvementssuchasstructuredorparametricgeneration,programmaticanswercomputation,anddifficultycalibration.
Evaluation. Development:uv run python run_eval.py –split dev.Test:uv run python run_eval.py –split test.
Iterateonthedevelopmentsplit.Runthetestsplitonlyformilestoneorfinalverification.
Constraints. Modifiable files include configs/pipeline.yaml, prompts/generate_problem.md, src/math_synth_-
bench/baseline.py, and new modules under src/math_synth_bench/. The benchmark harness, seed files, evaluation
references,metricsmodule,andverificationmodulemustnotbemodified.
36
