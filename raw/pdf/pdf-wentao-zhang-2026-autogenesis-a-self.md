---
id: pdf-wentao-zhang-2026-autogenesis-a-self
type: pdf
title: 'Autogenesis: A Self-Evolving Agent Protocol'
url: ''
authors:
- Wentao Zhang
ingested_at: '2026-04-29T16:19:51Z'
content_hash: sha256:d695101d4d7f6d117803254d43d2cd9499282da1e8cd72faefd3b61d1cb219e5
source_path: raw/pdf/pdf-wentao-zhang-2026-autogenesis-a-self.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 24
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__f6167676.pdf
published_at: '2026'
---
Autogenesis: A Self-Evolving Agent Protocol
WentaoZhang1
Abstract real-worldenvironments. Toovercomethislimitation,en-
dowing agents with self-evolution capabilities—enabling
Recent advances in LLM based agent systems
themtoautomaticallyadjuststrategies,refineinstructions,
have shown promise in tackling complex, long
and update tools based on environmental feedback—has
horizontasks. However,existingagentprotocols
emerged as a critical avenue for achieving robust auton-
(e.g.,A2AandMCP)underspecifycrossentity
omy. Thistransitionfrompredefinedexecutiontodynamic
lifecycleandcontextmanagement,versiontrack-
adaptationrepresentsafundamentalshiftinagenticsystem
ing,andevolutionsafeupdateinterfaces,which
design.
encouragesmonolithiccompositionsandbrittle
gluecode. Weintroduce AUTOGENESIS PRO- Despitethegrowinginterestinself-evolvingagents,imple-
TOCOL(AGP),aselfevolutionprotocolthatde- mentationsremainlargelyfragmentedandadhoc. Existing
coupleswhatevolvesfromhowevolutionoccurs. systemsoftenlacksharedstandards,renderingtheevolution
Its Resource Substrate Protocol Layer (RSPL) processneithercomposablenorauditable. Developersare
modelsprompts,agents,tools,environments,and frequently forced to rely on brittle glue code, leading to
memory as protocol registered resources1 with monolithicarchitecturesthataredifficulttomaintain. Fur-
explicitstate,lifecycle,andversionedinterfaces. thermore,withoutexplicitlifecyclemanagementandsafe
ItsSelfEvolutionProtocolLayer(SEPL)speci- updateinterfaces,self-modificationintroducessignificant
fiesaclosedloopoperatorinterfaceforpropos- risks of runtime instability. To address these issues, it is
ing, assessing, and committing improvements necessarytoelevatedevelopmentfromadhocengineering
with auditable lineage and rollback. Building practicestotheprotocollevel,decoupling“whatevolves”
on AGP, we present AUTOGENESIS SYSTEM from“howevolutionoccurs”viaastandardizedframework
(AGS),aself-evolvingmulti-agentsystemthat toensuremodular,traceable,andsafeevolution.
dynamically instantiates, retrieves, and refines
While protocols such as Anthropic’s Model Context Pro-
protocol-registered resources during execution.
tocol (MCP) (Anthropic, 2025b) and Google’s Agent-to-
WeevaluateAGSonmultiplechallengingbench-
Agent(A2A)havestandardizedconnectivity,applyingthem
marksthatrequirelonghorizonplanningandtool
directly to self-evolution scenarios presents a conceptual
useacrossheterogeneousresources. Theresults
mismatch.Theseprotocolsareprimarilydesignedtoresolve
demonstrateconsistentimprovementsoverstrong
connectivity challenges—specifically, model-tool invoca-
baselines, supporting the effectiveness of agent
tion(MCP)orinter-agentcommunication(A2A).However,
resourcemanagementandclosedloopselfevolu-
thecoreofself-evolutionliesnotininvocation,butinstate
tion.
mutationandmanagement.
Existingconnectivityprotocolslacknativesupportforen-
1.Introduction tityLifecycleandVersionLineage. Inaclosed-loopevolu-
tionarysystem,ifthecreation,update,anddestructionof
RecentadvancesinLLM-basedagentsystemshavedemon- componentsarenotpreciselydefined,theoptimizercannot
strated significant potential in tackling complex, long- safelyapplymodifications. Moreover,theabsenceofver-
horizon tasks. However, static agent designs often prove siontrackingandrollbackmechanismsmeansthaterroneous
insufficientwhenfacingthediversityandstochasticityof updatescanleadtoirrecoverableerrors. Consequently,re-
lyingsolelyoncommunicationprotocolsisinsufficient;a
1Nanyang Technological University, Singapore. Correspon-
denceto:WentaoZhang<zhangwent963@gmail.com>. novelprotocolcapableofmanagingthedynamicsofmuta-
tionisrequired.
1Unlessotherwisespecified,resourcesrefertoinstancesofthe Tobridgethegapfromconnectivitytoevolution,aspecial-
fiveRSPLentitytypes:prompt,agent,tool,environment,memory izedprotocolmustaddressthreeessentialproblems:
withagentoutputs.
1
6202
rpA
61
]IA.sc[
1v43051.4062:viXra

Autogenesis:ASelf-EvolvingAgentProtocol
• Decoupling: Resourcessuchasprompts,tools,andmem- 2.RelatedWork
orymustbeabstractedfromtheagent’scorelogic,trans-
2.1.LLM-basedAgentSystemsandToolUse
formingthemintopassive,independentlymanagedenti-
tiesratherthantightlycoupledcodeblocks. Recentprogressinlargelanguagemodel(LLM)basedagent
• Safety & Auditability: Strict version control and roll- systemshasdemonstratedtheirabilitytoaddresscomplex,
backmechanismsmustbeintroducedtoensurethatevery long-horizon tasks that require multi-step reasoning and
evolutionarystepistraceableandreversible. external tool interaction (Rein et al., 2024; Mialon et al.,
• Formalism: Asetofstandardizedoperators(e.g.,reflect, 2023). Inthesesystems,LLMstypicallyserveascentral-
propose,verify)needstobedefinedtostrictlygovernthe izeddecision-makingmodulesthatinterpretobservations,
evolutionprocess,convertingheuristictextmodifications decomposetasks,andinvoketoolstoaffecttheenvironment.
intoarigorouscontrolloop. BenchmarkssuchasGAIA(Mialonetal.,2023)havefur-
therhighlightedtheimportanceofstructuredtooluseand
Toaddressthesechallenges,weintroduceAUTOGENESIS.
planningcapabilitiesinagentdesign.
Farfrombeingmerelyautilitylibrary,AUTOGENESISisa
two-layerprotocolarchitecturedesignedtostrictlydecouple Most existing agent frameworks adopt architectures in
theevolutionarysubstratefromtheevolutionarylogic. Our whichprompts,tools,andmemoryareembeddedastightly
coremotivationistostandardizeunderlyingresourcerepre- coupledinternalcomponents. Toolsarecommonlytreated
sentations,enablingthesameoptimizationalgorithms(Yuk- asfixedfunctionalmodulesthataremanuallycuratedandin-
sekgonuletal.,2025;Shaoetal.,2024;Hu,2025b)tobe tegratedintotheagentpipeline.Whileeffectiveforbounded
seamlesslyappliedacrossdiverseagentcomponents. tasks, this design limits systematic reuse and controlled
adaptation of tools as task requirements evolve. In con-
• Layer1: ResourceSubstrateProtocolLayer(RSPL).
trast,ourapproachmodelstools(includingnativescripts,
This layer defines the substrate of evolution, modeling
MCPtools(Anthropic,2025a),andagentskills(Anthropic,
Prompts,Agents,Tools,Environments,andMemoryas
2025b))asprotocol-registeredresourceswithexplicitinter-
Protocol-registered Resources. RSPL endows these re-
facesandstaterepresentations,enablingdynamicinstantia-
sourceswithexplicitstate,lifecycle,andversionedinter-
tionandcontrolledrefinementduringexecution.
faces,renderingthemstandardizedobjectsamenableto
observationandmanipulation.
• Layer 2: Self-Evolution Protocol Layer (SEPL). 2.2.ConnectivityandInteroperabilityProtocols
This layer establishes a closed-loop operator interface
As agent-based systems grow in scale and complexity,
grounded in control theory. It defines atomic opera-
severalprotocol-leveleffortshaveemergedtostandardize
tions—Reflect, Select, Improve, Evaluate, and Com-
model–toolinteractionandinter-agentcommunication. An-
mit—to formally execute the evolution cycle, ensuring
thropic’sModelContextProtocol(MCP)(Anthropic,2025a)
thateveryself-modificationisdocumentedandadheresto
providesaunifiedinterfaceforconnectinglanguagemod-
strictsafetyconstraints.
elstoexternaltoolsanddatasources. Similarly,Google’s
Building on this protocol, we present AUTOGENESIS- Agent-to-Agent(A2A)protocolaimstostandardizecommu-
AGENT,areasoning-and-actingtool-callingagent. Instead nicationprimitivesthatsupportcollaborationamongmulti-
ofrelyingonhard-codedcomponents,itdynamicallyinstan- pleagents.
tiates,retrieves,andrefinesresourcesviaprotocolinterfaces
These protocols primarily address interoperability at the
duringexecution.Weevaluatedthissystemonmultiplechal-
levelofinvocationandmessagepassing. Theyspecifyhow
lengingbenchmarks,includingGPQA(Reinetal.,2024),
agentsandtoolsinteract,butlargelyleavetheinternalstate
AIME, GAIA (Mialon et al., 2023), and LeetCode (Leet-
ofagentsandresourcesopaque. Inparticular,theydonot
Code). The results demonstrate that by leveraging stan-
definemechanismsformanagingresourcelifecycles,track-
dardizedresourcemanagementandclosed-loopevolution,
ing version lineage, or constraining state mutations over
AUTOGENESIS-AGENT consistently achieves significant
time. Asaresult,whileconnectivityprotocolssimplifyin-
improvementsoverstrongbaselines.
tegration, theydonotdirectlysupportthepersistentstate
Thesignificanceofthisworkextendsbeyondperformance evolutionrequiredbyself-modifyingagentsystems.
gains;itillustratesapotentialshiftfrommanualprompten-
gineeringtoautomatedprotocolengineering. Byequipping 2.3.Self-CorrectionandOptimizationMechanisms
agentswithstandardizedself-repairandevolutioncapabili-
Aparallellineofworkinvestigatesmechanismsthatenable
ties,AUTOGENESISprovidesafoundationalparadigmfor
agentstoimprovetheirperformancethroughself-correction
buildingnext-generationagentsystemscapableofsustained
andoptimization. MethodssuchasTextGrad(Yuksekgonul
autonomousadaptationincomplexenvironments.
etal.,2025)interpretnaturallanguagefeedbackasasignal
2

Autogenesis:ASelf-EvolvingAgentProtocol
analogoustogradients,enablingiterativeupdatestostring- 3.1.Layer1: ResourceSubstrateProtocolLayer
valuedcomponentssuchasprompts. Reinforcementlearn-
TheResourceSubstrateProtocolLayer(RSPL)definesthe
ingbasedapproacheshavealsobeenappliedtoagentim-
evolvablesubstrateasasetofprotocol-registeredresources2
provement. TechniquesincludingReinforce++(Hu,2025a)
withexplicitstate,lifecycle,andversionlineage. Inthispa-
and GRPO (Shao et al., 2024) frame agent components
per,theseresourcescomprise(i)instructions(Prompt),(ii)
aspoliciesanduseevaluationsignalsasrewardstoguide
decisionpolicies(Agent),(iii)actuationinterfaces(Tool),
optimization.
whichencompassnativetoolscripts,MCPtools(Anthropic,
Whilethesemethodsdemonstratethatagentbehaviorscan 2025a),andagentskills(Anthropic,2025b),(iv)task/world
be iteratively improved, they are typically applied within dynamics(Environment),and(v)persistentstate(Memory).
narrowlyscopedsettingsandlackasharedabstractionfor Crucially,resourcesinRSPLarepassive: theyencapsulate
managingheterogeneousagentcomponents. Updatesare nooptimizationlogicandcannotself-modify;allobserva-
often applied directly to prompts or policies without ex- tions and state transitions occur only through controlled,
plicitlifecyclecontrol,versiontracking,orrollbacksupport. interface-mediatedoperationsinvokedbyhigherlayers.
AUTOGENESIS provides a protocol-level abstraction that
accommodates these optimization strategies by exposing 3.1.1.COREENTITIES
agentcomponentsasstandardized,evolvableresourcesand
We focus on these five entity types as a minimal yet ex-
definingoperator-levelinterfacesthroughwhichdifferent
pressivesubstrateforagenticsystems. Thischoiceisnot
optimizationmethodscanbeappliedinacontrolledmanner.
intendedtobeexhaustive,butrathertoidentifyacommon
denominatoracrossmodernagentstacksandprovideauni-
2.4.Summary
formtargetspaceonwhichSEPLcanoperate.
Existingworkonagentsystems,interoperabilityprotocols,
Definition3.1(ResourceEntity). Aresourceentityoftype
and self-optimization has laid important foundations for ω anditstype-levelcollectioncanberepresentedas:
autonomousbehavior. However, theseeffortsdonotpro-
vide a unified protocol for managing the persistent state e =(n , d ,ε , g , m ),
ω,i ω,i ω,i ω,i ω,i ω,i
(1)
evolution of agent-internal resources. In particular, cur-
= e i ,
ω ω,i ω
rent connectivity protocols emphasize interaction but do E { | →I }
notaddresslifecyclemanagementorversionedstatemuta- where = PROMPT,AGENT,TOOL,ENV,MEM de-
T { }
tion. AUTOGENESIS addresses this gap by introducing a notesthesetofRSPLentitytypes,ω indexestheentity
→T
two-layerprotocolarchitecturethatseparatesthedefinition type, istheindexsetofresourceinstancesoftypeω,and
ω
I
of evolvable resources from the mechanisms that govern i indexesanindividualinstance. Heren isaunique
ω ω,i
→I
theirevolution,enablingmodular,traceable,andauditable resourcename,d isashortdescription,ε :
ω,i ω,i ω ω
X ↑Y
self-evolutioninmulti-agentsystems. isaninput-to-outputmapping,g 0,1 isthetrainable
ω,i
→{ }
markerthatindicateswhethertheresourceisevolvable,and
3.Autogenesis m ω,i isanauxiliarymetadatadictionary.
Despitegrowinginterestinself-evolvingagents,mostsys- A key motivation for making prompt, tool, and memory
tems remain engineered in an ad hoc manner and lack a explicitRSPLresourcesisdecoupling. Manyagentsystems
sharedprotocolstandardthatmakesevolutioncomposable, package prompts, tools, and memory as internal compo-
auditable, and interoperable. We introduce AGP, a two- nents of an agent, which entangles agent logic with task-
layerself-evolutionprotocol. TheResourceSubstrateProto- specificinstructionsandcapabilitybundles,increasingmain-
colLayer(RSPL)specifiestheevolvablesubstrate,namely tenanceandlimitingtransfer. Byexternalizingthemasfirst-
whichresourcesmaychangeandhowtheyarerepresented, class,versionedresourceswithstandardizedinterfaces,the
versioned,andaccessed. TheSelf-EvolutionProtocolLayer sametool-callingagentpolicycanbepairedwithdifferent
(SEPL)specifiestheevolutionlogic,namelyhowupdates promptsandtoolsets,anddeployedunchangedacrosstasks
areproposed,assessed,andcommittedthroughasafeoper- andenvironments.
atorinterface. Inspiredbyinterfacestandardizationefforts
Tosupportresourceregistration,unifiedmanagement,and
in agent tooling (e.g., the Model Context Protocol), this
instantiation,RSPLstoresaserializableregistrationrecord
separationcleanlydecoupleswhatevolvesfromhowevo-
foreachresourceinstance.
lutionoccurs,enablingmodularity,traceability,andsafety-
preservingevolutionacrosscomponents. Definition3.2(ResourceRegistrationRecord). Aresource
2Unlessotherwisespecified,weuseresourcestorefertoin-
stancesofthefiveRSPLentitytypes:prompt,agent,tool,environ-
ment,andmemory.
3

Autogenesis:ASelf-EvolvingAgentProtocol
Layer 1: Resource Substrate Protocol Layer (RSPL) Layer 2: Self-Evolution Protocol Layer (SEPL) Multi-agent System
Core Resources Evolvable Variables (Vevo)
ReporterAgent Browser Use Agent
Co A n d t d ent R E e xp p o o r r t t A D c e t c io id n e s B A r c o t w io s n e s r R R e e s c u o l r t d s
V1.0.1 V1.0.0 V1.0.3 V1.0.6 V1.0.0 V1.0.1
Prompt Agent Tool Environment Memory
(εPrompt) (εAgent) (εTool) (εEnv) (εMen) PlanningAgent
Operator Algebra & Evolutionary Loop Tools
Server Interface & Context Manager Planning Interprete Decompose Assign Registration 1 An . s G we e r n In e iti r a a liz t a e tion user tasks i s n u t b o - m ta a s n ks ageable t s o u b sp -a e g c e ia n l t i s zed
Lifecycle Control
5.Commit 2.Reflect
State Access Improvement Commit Multi-Agent Proposal Generation DeepResearcherAgent Deep AnalyzerAgent ToolGeneratorAgent
Optimization
Cycle O Q p u t e im ri i e z s e S T e o a o r l c s h I R n e s f ig in h e t Dive O rs rg e a F n o iz r e mats R S e u a m s m on a r a iz n e d Re T tr o ie o v l al Cr T e o a o ti l on R T e o u o s l e
Infrastructure Services
4.Evaluate 3.Improve
Answer Evaluation Variables Improvement
Version Model Dynamic Tracer
Manager Manager Manager Module
sevitcejbO resU Create a new plan Delete the plan Update the plan Mark step as completed sub-agent A sub-agent B toolC Feedback …… snoitcA
Protocol Application
Planning Tool
u c p re d a a t t e e d m e a le r t k e for C T co r r a e m c a p k te le e , x x u e t p a c d u s a k ti t s o e n , s a i s m n ta u d t l e t m a s n a e n o a u g s e l y plans
Objective Shifts(Update & Unexpected Errors Plans)
Version Lineage
Game Math Problem
Playing Solving Computer Use Trading Brower Use
Figure1.TheAutogenesisarchitecture.
registrationrecordanditstype-levelcollectioncanberepre- historyforrestoration. ItsexportedAPIcanbeviewedasa
sentedas: smallsetoffunctionallygroupedoperatorsforlifecycleand
registration(e.g.,init,build),retrievalandinspection
c =(e , v ,ϑ ,ϖ , ),
ω,i ω,i ω,i ω,i ω,i ω,i
F (2) (e.g.,list,get state),evolutionandversioning(e.g.,
= c i ,
C ω { ω,i | →I ω } update, restore), execution and contract (e.g., run,
whereω indexestheentitytypeandi indexesan load contract), and serialization and deserialization
ω
individua → l T instance. Here e is the resou → rc I e entity tuple (e.g.,save to json,load from json). Themanager
ω,i
definedinTheorem3.1,v
ω,i
Visaversionstring,ϑ
ω,i
is explicitlysupportscontractgeneration,producingaconsoli-
→
animplementationdescriptor(e.g.,importpath,classdefini- datedcapabilityandconstraintspecificationforthemanaged
tion,orsource-codestring),ϖ areinstantiationparameters entities,whichprovidesstable,up-to-datedescriptionsthat
ω,i
(e.g.,constructorarguments),and isasetofexported improvereliabilityandreducepromptbloat,enablingsys-
ω,i
F
representationsusedbyLLMstointeractwiththeresource tematiccontextengineeringviacontrolledpromptinjection.
(e.g., function-callingschema, natural-languagetext, and Forinstance,fortools(whichmaybenativescripts,MCP
structuredargumentschema). tools,oragentskills)thecontractcantakeaskills.md-
styleform(Anthropic,2025b)thatenumeratestoolactions,
Definition 3.3 (Protocol-registered resource). For each
arguments,preconditions,andusageconstraints. Concrete
entity type ω, let denote the type-specific registry of
ω
R interfaceinstantiationscanbefoundinSectionC.1.2.
protocol-registeredresources,andlet = denote
R ωR ω
theglobalregistry. RSPLbindseachentitytypeω toadedi- Serverinterface. Theserverisintroducedtoencapsulate
!
catedcontextmanager ω andaserver-exposedinterface the context manager’s internal complexity and present a
M
ω . Werepresentthetype-levelregisteredresourceas stable,simplifiedinterfaceforexternalcallers. Itpackages
A
heterogeneousmanagementroutinesbehindauniformsetof
r =( , , ), (3)
ω C ω M ω A ω endpointswithconsistentrequest/responsesemantics,while
whereeachc isaregistrationrecordinTheorem3.2. delegatingtheimplementationdetailstothecontextman-
ω,i ω
→C
Thecontextmanager maintainsthecollection ,the ager. Thisseparationisolatesclientsfrominternaldesign
ω ω
M C
version lineage for type ω, and implements lifecycle and changes, reduces coupling, and provides a single control
update operations over these records; the server-exposed plane through which the protocol mediates safe, version-
interface encapsulates andexposesaunifiedexter- awareinteractionswithRSPLresources.
ω ω
A M
nal interface by delegating requests to the corresponding
context-managerroutines. 3.1.2.INFRASTRUCTURESERVICES
Contextmanager. Thecontextmanagerimplementsthe RSPLfurtherincludescross-cuttingservicesthatsupportre-
managementplaneforeachresourcetype. Beyondlifecycle liableevolution,includingreproducibility,safedeployment,
controlanddependencyconstraints,itmaintains(i)anac- andversionedrecovery:
tiveregistryofmaterializedresourcesand(ii)aversioned
4

Autogenesis:ASelf-EvolvingAgentProtocol
Modelmanager. Aunifiedmodel-APIlayerthatstandard- Definition3.4(EvolvableVariableSet). Wedefinetheuni-
izescallsacrossproviders(e.g.,OpenAI,Anthropic,Google, versal set of evolvable variables, , as the union of all
evo
V
andOpenRouter,etc.),whilesupportingrouting,fallback, managedresourceentitiesandexecutionartifacts:
andcost-awareselectiontokeepmodelaccessconsistentas
componentsevolve.
= y , (4)
evo ω
Versionmanager. Maintainsversionlineageforeachre- V " ω E $↓{ }
#→T
source,enablingrollback,branching,anddiffing. Versions
where denotes the set of resource entities of type ω
areauto-incrementedidentifiers(e.g.,semanticversions)as- E ω
governedbytheRSPL.Theelementyencapsulatesexecu-
signedonregisterorupdate,eachreferencinganimmutable
tionartifacts,specificallyfinaloutputsandreasoningtraces,
snapshotoftheconfigurationrecordandassociatedartifacts
which constitute the observational basis for retrospective
forauditabilityandreproducibility.
optimization. Furthermore, each variable v is as-
evo
→V
Dynamicmanager. Handlesserializationordeserialization sociatedwithabinarylearnabilityconstraintg 0,1 ,
v
→{ }
ofresourceconfigurationsforpersistenceandtransfer,en- therebystrictlydefiningthetrainableparametersubspace
ablingsafehot-swappingofresourcesatruntimewithout != v g =1 .
evo v
{ →V | }
restartingtheagentsystem.
TracerModule. Amodulethatcapturesfine-grainedexe-
3.2.2.OPERATORALGEBRA
cutiontraces(inputs,outputs,intermediatedecisions,tool Toformalizetheevolutionarytrajectoryasarigorouscon-
interactions, etc.) forinterpretabilityanddebugging, and trol process, we decompose the state transition function
as training signals for dataset synthesis and retrospective into atomic operations that correspond to the canonical
improvement. phases of iterative optimization: observation, attribution,
proposal, verification, andcommit. Consequently, wees-
3.2.Layer2: Self-EvolutionProtocolLayer(SEPL) tablishfivenecessaryauxiliaryspacestoensuretheprocess
ismathematicallywell-defined. Thetracespace guaran-
The Self-Evolution Protocol Layer (SEPL) establishes a Z
teessystemobservability;thehypothesisspace provides
control-theoreticformalismforagenticsystemevolution. It H
the basis for semantic error attribution; the modification
conceptualizesthecontinuousimprovementofanagentic
space formalizesthemodificationprimitives;theobjec-
systemasageneralizedoptimizationproblemdefinedover D
tivespecification definestheoptimizationlandscape;and
aheterogeneousstatespace. Formally,SEPLmodelsevolu- G
theevaluationspace encapsulatesperformancemetrics
tionarydynamicsasastatetransitionfunctiongovernedby S
andsafetystatus. Thesecomponentsconstitutetheminimal
astrictlytypedoperatoralgebra.
sufficiencyrequiredtoclosetheself-evolutionloop.
BymediatingallstatemutationsthroughstandardizedRSPL
Reflect(ϱ). Definedasϱ: ς( ),thisoperator
interfaces, theprotocolguaranteesthatevolutionistrace- Z↔V evo ↑ H
bridgesthegapbetweenrawobservationandoptimization
able,reversible,andsafe-by-construction. Whilethispaper
direction. Itapproximatesthe“semantic gradient”ofthe
focuses on the reflection-driven optimizer as the primary
system by mapping high-dimensional execution traces to
instantiation,ourimplementationalsosupportsotheropti-
specific,causalfailurehypotheseswithinthevariablespace.
mizationstrategies,includingTextGrad(Yuksekgonuletal.,
2025), GRPO (Shao et al., 2024), and Reinforce++ (Hu, Select(φ).Formulatedasφ : ς( ) ς( ),thisop-
evo
V ↔ H ↑ D
2025b), utilizing the same state manipulation primitives. eratoractsasthegenerativepolicy. Ittranslatesdiagnostic
Furtherdetailsonthesealternativeimplementationsarepro- hypothesesintoconcreteupdateproposals,samplingcan-
videdinSectionC.2. didatemodifications designedtominimizetheidentified
D
errorsignalsubjecttostructuralconstraints.
3.2.1.EVOLVABLEVARIABLES
Improve(↼).Themutationoperator,↼:
V
evo
↔
ς(
D
)
↑Ve↑vo
,
Totransitionfromheuristicadaptationtoasystematicevo- executes the physical state transition. It applies discrete
lutionprotocol,weintroducetheconceptofvariablelifting. updates viastandardizedRSPLinterfacestoyieldapro-
D
Thisabstractionprojectsdiscrete,heterogeneousRSPLre- visionalcandidatestate.
sources (e.g., tool code, system prompts) onto a unified
representationofevolvablevariables. Thisformalismoffers
Evaluate(↽). Specifiedas↽:
Ve↑vo↔G↑S
,thisoperator
servesastheobjectivefunction. Itmapsthecandidatestate
significanttheoreticaladvantagesbyhomogenizingthein-
andgoalspecificationtotheevaluationspace (comprising
teractionsurfaceforevolutionaryoperatorsandrigorously S
quantitativescoresandstrictsafetyinvariants).
delineatingthetrainablesubspaceviaanexplicitlearnability
mask. Commit(⇀). Operatingas⇀:
Ve↑vo↔S↑V evo
,thisfunc-
tionactsasaconditionalgatingmechanism. Itutilizesthe
5

Autogenesis:ASelf-EvolvingAgentProtocol
Algorithm1SEPLEvolutionaryLoop 4. AGS andOptimizationStrategies
Input: AgenticSystemA,Objective ,BudgetT
G ThissectionpresentstheconcreteinstantiationoftheAGP
Output: Optimizedstate Ve↓vo protocol, demonstrating its practical usability as a self-
1: Initialization:
evolvingagentsystem.
2: e ( v 0 o ) VariableLifting(A) ↭Projectresourcesto
V ↗
optimizationmanifold
4.1.AGSArchitecture
3: (0) Execute(A, e ( v 0 o )) ↭Obtaininitial
Z ↗ V
observationaltrace Building on AGP, we instantiate the two-layer protocol
into AGS, a self-evolving multi-agent system organized
4: OptimizationCycle:
aroundanAgentBusarchitecture. Ratherthanrelyingon
5: fort=0,1,...,T 1do
↘ a monolithic controller or a rigid pipeline, AGS uses a
6: //Phase1: Diagnosis&Proposal
7: H (t) ↗ ϱ( Z (t), V e ( v t o )) ↭Reflect: Computesemantic s a h ll a a re g d en m ts es c s o a m ge m b u u n s ic a a s te th e e xc c l e u n s t i r v a e l l c y o t o h r r d o i u n g a h tio s n ta b n a d c a k rd b i o z n e e d :
gradients
busmessages,enablingloosecoupling,transparentobserv-
8: D (t) ↗ φ( V e ( v t o ), H (t)) ↭Select: Generate ability, and concurrent sub-agent execution. Throughout
modificationprimitives
allconfigurations,prompts,tools(includingnativescripts,
9: //Phase2: Mutation&Verification MCP tools, and agent skills), and memory are treated as
10: e ( v t o +1) ↼( e ( v t o ), (t)) ↭Improve: Applyupdates first-classRSPLresourceswithexplicitlifecycleandver-
V ↗ V D
tocandidate sionlineage,ratherthanhard-codedinternalcomponents.
11: %(t+1) ↽( e ( v t o +1), ) ↭Evaluate: Mapto Thesystemoperatesthroughthreeinterleavedmechanisms:
S ↗ V G
evaluationspace
12: //Phase3: G%ating&Transition Orchestration via Plan Generation. Upon receiving a
task fromthe AgentBus, theOrchestrator isresponsible
13: V e ( v t o +1) ↗ ⇀( V e ( v t o +1), S (t+1)) ↭Commit: solely for planning and coordination; it does not execute
Conditionalstatetransition
subtasksdirectly. Concretely,theOrchestratorproducesa
14: //Phase4: Ne%xtIteration structured plan.md artifact that records the overall task
15: (t+1) Execute(A, e ( v t o +1)) decomposition: ahuman-readableflowchartoftheexecu-
Z ↗ V
16: ifConverged( (t+1))then tiongraph,anorderedlistofsubtasksteps,andtheassign-
S
17: break mentofeachsubtasktoadesignatedsub-agent(e.g.,deep
18: endif researcher, browser-use agent, tool-calling agent, or tool
19: endfor generator). ThisplanisregisteredasaversionedRSPLre-
(t)
20: return evo source,makingthecoordinationstructureitselfinspectable
V
andevolvable. TheOrchestratorthenbroadcastseachsub-
task together with its specification to the corresponding
evaluationsignalsin togovernstatetransition,rigorously
sub-agentsviathebus.
S
enforcingsafetyinvariantsandperformancemonotonicity
byacceptingthecandidate onlywhenspecificsuccess Concurrent Sub-Agent Execution and Iterative Re-
criteriaaremet.
Ve↑vo
planning. Uponreceivingabroadcastsubtask, eachsub-
agentindependentlyretrievestherelevantpromptandtool
3.2.3.THEEVOLUTIONARYLOOP resourcesfromtheRSPLregistryviasemanticsearch,exe-
cutestoolcallstointeractwiththeenvironment,andwrites
Theatomicoperatorsdefinedaboveareorchestratedintoa intermediateresultsandreasoningtracestosharedmemory
rigorousclosed-loopprocess,summarizedinAlgorithm1. aspersistent,queryablestate. Sub-agentsoperateconcur-
(0)
Startingfromaninitialstate evo ,SEPLiterativelyexecutes rently:thebusdecouplestaskdispatchfromtaskcompletion,
V
the system to generate observational traces ( ), derives somultiplesub-agentsmayexecuteinparallelwithoutsyn-
Z
causalfailurehypotheses( ),andsynthesizesmodification chronizationoverhead. Onceallsub-agentsinthecurrent
H
primitives( ). roundhavecompleted,theOrchestratorcollectstheirout-
D
putsviathebus,summarizestheaggregatedresults,andup-
Crucially, the loop is closed via the evaluation space
S datesplan.mdwiththecurrentexecutionstate. Basedon
andthecommitoperator⇀. Thisdesignensuresthatself-
thisglobalview,theOrchestratordecideswhetherthetaskis
evolutionisnotarandomwalk,butadirectedtrajectorythat
completeorwhetherafurtherroundofsubtaskdecomposi-
isgroundedinexecutiondata,traceablethroughversioned
tionandbroadcastisrequired. Thiscollect-and-replanloop
updates,andmonotonicallyimprovingunderstrictlydefined
repeatsuntiltheterminationconditionissatisfied,enabling
safetyinvariants.
thesystemtohandletasksofarbitrarydepthandbranching
complexity. Asacomplementarypattern, AGS alsosup-
6

Autogenesis:ASelf-EvolvingAgentProtocol
ports agent-as-tool composition, in which a sub-agent is AlternativeStrategies. Beyondreflection,ourimplemen-
wrappedbehindastandardRSPLtoolschemaanddirectly tationsupportsadditionaloptimizationstrategiesthatmap
invokedbyatool-callingagentalongsideconventionaltools, naturallyontothesameSEPLoperatorinterface:
MCPservices,andskills,enablinglightweightmulti-agent
TextGrad (Yuksekgonul et al., 2025) treats the natural-
collaborationwithoutbus-levelorchestration.
language feedback produced by ϱ as a “textual gradient”
Self-Evolution. Interleavedwiththebuscoordinationloop, andappliesgradient-descent-likeupdatestostring-valued
AGS triggers the SEPL evolutionary loop (Algorithm 1) variables(prompts,code). WithinAGP,TextGradinstanti-
wheneverobservationaltracessignalcorrectablefailuresor atesφasagradient-informedproposalgeneratorand↼asa
suboptimalperformance. Concretely,theagent(i)reflects string-leveleditoperator,whilereusingthestandard↽and
onexecutiontraces (tooloutputs,errors,latencies,reward ⇀forevaluationandgating.
Z
signals,andtaskprogress)toderivecausalfailurehypothe-
Reinforce++/GRPO(Hu,2025b;Shaoetal.,2024)adopt
ses ,(ii)selectstargetedmodificationproposals over
H D a reinforcement-learning perspective, treating the evolv-
evolvablevariables(e.g.,prompttext,toolsourcecodefor
able variables as a policy and the evaluation signal as a
nativescripts,MCPtoolconfigurations,skilldefinitions,or
reward. Here, ϱ samples multiple candidate trajectories,
theplanstructureitself),(iii)appliescandidateupdatesto
φ ranks them by reward, ↼ updates the policy parameters
produceaprovisionalstate ,(iv)evaluatesthecandidate
V evo (e.g.,promptweightsorLoRAadapters)viapolicy-gradient
againsttheobjective ,and(v)commitsacceptedmodifi-
G estimates,and⇀commitsonlyiftheupdatedpolicyexceeds
cationsasversionedtransit%ionswithauditablelineageand
abaselinereturnthreshold. Thesestrategiesdemonstrate
rollback. Failed evolution attempts are rolled back with-
that the SEPL operator algebra is sufficiently general to
outsideeffects,andsuccessfulonesbecomeimmediately
accommodate both inference-time text optimization and
availabletoallsub-agentsinsubsequentbusrounds. This
gradient-basedparameterupdateswithinaunifiedprotocol.
tightintegrationensuresthatevolutionisalwayssafe,trace-
able,andcomposableacrossthefulllifetimeoftheagent
network. 5.EmpiricalStudies
In this section, we present empirical results of deploying
4.2.InstantiatingtheOptimizer
AGS across various challenging benchmarks with AGP
TheAGPprotocolisagnostictothespecificoptimization protocoltodemonstrateitscomprehensivecapabilities.
strategy: anyprocedurethatconformstothefive-operator
BenchmarkInstruction. ForGPQA-Diamond(198ques-
SEPL interface (ϱ, φ, ↼, ↽, ⇀) can serve as the evolution-
tions),weadoptaclosed-book,non-retrievalevaluationpro-
aryengine. Wedescribetheprimaryinstantiationusedin
tocol. Theagentispresentedwithagraduate-levelSTEM
our experiments and briefly outline alternative strategies
multiple-choicequestion(coveringbiology,chemistry,and
supportedbyourimplementation.
physics)andmustoutputexactlyoneoptionasthefinalan-
ReflectionOptimizer. Thedefaultoptimizerinourexperi- swer.GPQA-DiamondisdesignedtobeGoogle-proof,such
mentsimplementstheSEPLloopthroughnatural-language thatsimplewebsearchisinsufficientandsuccesstypically
reflection. Given an execution trace (t) and the current requiresdifficult,multi-stepscientificreasoningbeyondfac-
evolvablestate (t) ,theReflectoperato Z rϱpromptstheback- tualrecall. Overall, thisbenchmarkmeasurestheagent’s
evo
V
bone LLM to analyze failures and generate structured di- deep scientific understanding and closed-book reasoning
agnostic hypotheses (t) in natural language (e.g., “the ability.ForAIME,weuseproblemsfromthe2024and2025
H
prompt lacks explicit instruction for edge-case handling” AmericanInvitationalMathematicsExamination(AIME24
or“thesortingalgorithmhasO(n2)complexityonthecrit- andAIME25),eachconsisting30problems. Eachinstance
ical path”). The Select operator φ then translates these requirestheagenttosolveacompetition-levelproblemand
hypothesesintoconcretemodificationproposals (t),such outputasingleintegeranswer. Weevaluateperformanceby
D
as appending constraint clauses to the system prompt or exact-matchaccuracy,whichprimarilymeasurestheagent’s
rewritingafunctionbody. TheImproveoperator↼applies long-horizonsymbolicreasoningandarithmeticprecision.
theseproposalsthroughtheRSPLset variablesinter- ForGAIA,weevaluateontheGAIATestsplit(300tasks).
facetoproduceacandidatestate. TheEvaluateoperator↽ Eachtaskspecifiesareal-world,multi-stepobjectivethat
re-executesthetaskunderthecandidatestateandcompares typicallyrequiresplanningandtooluse(e.g.,webbrowsing
performanceagainsttheobjective . Finally,theCommit and document/file operations). Wemeasure performance
G
operator⇀acceptstheupdateonlyifperformanceimproves bytasksuccess(completion),whichprimarilyreflectsthe
orsafetyinvariantsarepreserved,otherwiserollingbackto agent’slong-horizonplanningandreliabletool-useexecu-
thepreviousversion. Thisreflection-drivenloopisrepeated tion. ForLeetCode,weconstructanin-house,LeetCode
forafixedbudgetofT rounds. multi-language programming benchmark to evaluate ex-
7

Autogenesis:ASelf-EvolvingAgentProtocol
ecutable code generation under reduced data contamina- Table1.ResultsonGPQA-Diamond,AIME24andAIME25.
tion. Tomitigatepotentialtraining-datacontaminationfrom
Approach GPQA-Diamond AIME24 AIME25
widelycirculatedlegacyproblems,weintentionallyselect
gpt-4o
recentlyreleasedproblemsacrossdiversecategories(e.g.,
vanilla 47.98 13.34 6.67
arrays,trees,linkedlists,etc.) andsplittheminto200train- evolveprompt 53.81 13.34 13.34
evolvesolution 53.53 16.67 13.34
ingproblemsand100testproblems. Theagentsolveseach
evolveprompt+solution 58.08 16.67 13.34
probleminoneofmultiplelanguages(Python,C++,Java,
Improvement(%) 21.05 24.97 100
Go,etc.),andwereportmultiplemetricsincludingoverall → → →
gpt-4.1
score(acceptance),test-casepassrate,andruntime,which
vanilla 65.15 23.34 20.00
together measure algorithmic reasoning, implementation evolveprompt 68.68 33.33 23.33
correctness,andefficiency. evolvesolution 68.68 36.67 30.00
evolveprompt+solution 67.67 40.00 33.33
Improvement(%) 3.87 71.38 66.65
5.1.ExperimentsonScientificandMathematical → → →
grok-4.1-fast
Benchmarks
vanilla 83.33 96.67 90.00
evolveprompt 83.84 96.67 93.33
5.1.1.EXPERIMENTSETTING
evolvesolution 87.81 96.67 90.00
evolveprompt+solution 89.34 96.67 96.67
To validate our self-evolving agent AGS based on the
Improvement(%) 7.21 0.00 7.41
AGP protocol, we conduct experiments across GPQA- → →
claude-sonnet-4.5
Diamond, AIME24, and AIME25, focusing on evolv-
vanilla 78.28 76.67 73.33
ing prompts and agent outputs. These benchmarks rep- evolveprompt 79.79 86.67 90.00
resent standard reasoning tasks where evolution of agent evolvesolution 80.30 80.00 90.00
evolveprompt+solution 81.44 86.67 90.00
architecture,memorysystems,environments,andtoolsis
Improvement(%) 4.04 13.04 22.73
relativelylesscriticalcomparedtoinstructionrefinement → → →
and solution quality. To isolate the self-evolution capa- gemini-3-flash-preview
vanilla 88.38 83.33 83.33
bility on prompts and solutions, we deliberately do not evolveprompt 88.89 93.33 86.67
equipAGSwithanyexternaltoolsinthissetting,andcom- evolvesolution 87.88 93.33 90.00
evolveprompt+solution 90.40 93.33 93.33
parethreeevolutionstrategies: evolvepromptonly,evolve
solution only, and the combined evolve prompt+solution. Improvement(%) 2.28 12.00 12.00
→ → →
To ensure comprehensive coverage across model capa-
bilities, we evaluate using multiple backbone models:
corrects errors exposed during reflection; weaker models
lower-performingmodels(gpt-4o,gpt-4.1),amedium-
make more correctable mistakes, whereas stronger mod-
performing model (claude-sonnet-4.5), and a
elsalreadyoperatenearceiling. claude-sonnet-4.5
high-performingmodel(gemini-3-flash-preview,
occupies a middle tier (76–78% vanilla) and improves
grok-4.1-fast). Ourself-evolutionalgorithmprimar-
by 4.0%, 13.0%, and 22.7% on GPQA, AIME24, and
ilyemploysthereflectionoptimizerwithamaximumof3
AIME25,respectively,confirmingthatheadroomcorrelates
optimizationrounds,afterwhichtheagentoutputistaken
withevolutionbenefit. (2)Combinedevolutiondominates
asthefinalsolution.
prompt-onlyandsolution-only. Acrossallmodels,evolve
Metrics. Wemeasureperformance byexact-matchaccu- prompt+solution consistently yields the best scores. For
racy: for GPQA-Diamond, the agent’s selected option gpt-4.1onAIME24,evolvepromptreaches33.3%and
must match the ground-truth multiple-choice answer; for evolve solution 36.7%, whereas the combined approach
AIME24andAIME25,theagent’snumericaloutputmust reaches40.0%;onAIME25,therespectivescoresare23.3%,
exactlymatchthereferenceintegeranswer. 30.0%,and33.3%.claude-sonnet-4.5showssimilar
patterns: evolveprompt+solutionoutperformseithersingle
5.1.2.RESULTSANDANALYSIS strategyonallthreebenchmarks. Thissuggeststhatinstruc-
tion refinement and solution refinement address comple-
TheresultsinTable1revealfourkeyobservationsacross
mentaryfailuremodes;combiningbothclosesmoreerrors
models and evolution strategies. (1) Weak models
thaneitheralone. (3)Mathbenchmarksrespondmore
gain more; strong models gain less. gpt-4.1, with
stronglythanscienceQA.AIME24andAIME25exhibit
lower vanilla baselines (23.3% on AIME24, 20.0% on
largerrelativegainsthanGPQA-Diamond. Forgpt-4.1,
AIME25), improves by 71.4% on AIME24 and 66.7%
GPQA improves by 3.9% while AIME24 improves by
on AIME25 under evolve prompt+solution. In contrast,
71.4%; for gemini-3-flash-preview, GPQA im-
gemini-3-flash-previewstartsat83–88%andim-
provesby2.3%whilebothAIMEbenchmarksimproveby
proves by 2.3% on GPQA-Diamond and 12.0% on both
12.0%.Long-horizonsymbolicreasoning(multi-stepderiva-
AIMEbenchmarks.Thereasonisstraightforward:evolution
8

Autogenesis:ASelf-EvolvingAgentProtocol
tions,arithmeticchains)exposesmoreintermediatefailure Table2.PerformanceresultsforagentsonGAIATestbenchmark.
pointsthatreflectioncantarget;closed-bookscienceQA,by
Agent Level1 Level2 Level3 Average
contrast,reliesmoreonfactualrecallwhereprompt/solution
refinement offers fewer levers. (4) Ceiling effects cap o4-mini-DR 67.59 59.10 44.28 59.30
JoyAgent 77.42 67.30 46.94 67.11
evolutiononsaturatedbenchmarks. grok-4.1-fast
o3-DR 79.42 68.97 47.48 68.70
reaches96.7%onAIME24withvanilla,leavingminimal
Langfun 84.95 73.58 48.98 73.09
headroom;evolutionyieldsnogainthere. Itstillimproves Alita 92.47 71.70 55.10 75.42
GPQAandAIME25by7.2%and7.4%,respectively,where DeSearch 91.40 75.47 61.22 78.07
baselines are lower. This reinforces that self-evolution is h2oGPTe-Agent 89.25 79.87 61.22 79.73
Su-Zero-Ultra 93.55 77.36 65.31 80.40
mosteffectivewhenbothmodelcapabilityandbenchmark
AWorld 95.70 81.13 57.14 81.73
difficultyleaveroomforimprovement.
HALO 94.62 84.91 69.39 85.38
ToolOrchestra 95.70 82.39 87.76 87.38
Insummary,AGSdeliversconsistentgainsacrossdiverse
modelcapabilitiesandbenchmarksthroughoutourexper- vanilla 91.40 77.36 61.22 79.07
evolvetool 98.92 85.53 81.63 89.04
iments. Stronger models improve modestly but reliably;
weakermodelsimprovesubstantiallywhensufficienthead- Improvement(%) 8.23 10.56 33.34 12.61
→ → → →
roomexists. Thecombinedprompt+solutionevolutionstrat-
egyconsistentlyoutperformssingle-strategyevolution,and
mathbenchmarksbenefit morestronglythanscience QA taskcomplexityishighest. Ontheeasiertiers,thegapnar-
fromiterativerefinement. rowsbutremainsconsistent: Level1reaches98.92%(vs.
95.70%forToolOrchestra)andLevel2reaches85.53%(vs.
84.91%forHALO),indicatingthattoolevolutionprovides
5.2.ExperimentsonGeneralAgentBenchmark
broad-spectrumimprovementratherthanbeinglimitedto
5.2.1.EXPERIMENTSETTING asingledifficultyregime. (2)Toolevolutionyieldslarge
gains on hard tasks. Compared to the vanilla baseline
ForGAIA,wefocusonevolvingtools,asGAIAtaskspri-
(79.07%avg.),evolvetoolimprovesperformanceby12.6%
marily depend on tool capabilities rather than pure rea-
overall. Theimprovementisstronglyskewedtowarddiffi-
soning. Our system architecture consists of a top-level
culty:Level1gains8.2%,Level2gains10.6%,andLevel3
planner agent (m = 50) and multiple specialized sub-
gains33.3%. Thispatternmirrorstheheadroomeffectob-
agents: a deep researcher (m = 3), a browser-use agent
servedinthemathbenchmarks: hardertasksexposemore
(m = 3), a report agent, a tool generator (m = 3),
correctablefailuremodes,whichthereflection-driventool
and a deep analyzer agent (m = 3). All agents utilize
evolutioncantarget. Notably, the33.3%gainonLevel3
gemini-3-flash-preview as the backbone model,
represents the single largest relative improvement across
wheremdenotesthemaximumnumberofreasoningsteps
allbenchmarksinourstudy,underscoringthattoolevolu-
peragent. Theself-evolutionoftoolsisprimarilydrivenby
tionisparticularlyeffectivewhentasksdemandcomplex
thetoolgeneratoragent: givenasubtask,itfirstretrieves
multi-steptoolchainsthatstatictoolkitscannotadequately
candidatetoolsfromthemanagedtoolregistryviaseman-
cover. (3)Hierarchicalresourcemanagementmitigates
ticsearch;ifasuitabletoolisfound,theagentattemptsto
planningcomplexity. GAIA’smulti-domaintasksrequire
executeit,anduponencounteringerrors,iterativelyrefines
temporalandcross-modalstatecoherence,andmanybase-
thetool’ssourcecodethroughreflection;ifnosuitabletool
linesdegradeduringdomaintransitions(e.g.,frombrowser
exists, the agent synthesizes a new tool from scratch and
retrievaltolocalfileanalysis). Bytreatingprompts,tools,
registersitasaversionedRSPLresourceforfuturereuse.
and environments as first-class RSPL resources with ex-
Metrics.WeadoptthePass@1scoreontheGAIATestsplit plicitlifecyclemanagement,AGSpreservessession-critical
andreporttask-completionaccuracyateachdifficultytier stateacrossagentboundaries,reducingcontextualforgetting
(Level1,Level2,Level3)aswellastheoverallaverage. andenablingcompositionalgeneralizationonLevel2and
Level3scenarios. Furthermore,whentheplanningagent
The results in Table 2 reveal three key observations.
encountersnovelsubtasks,itinvokesthetoolgeneratorto
(1) AGS achieves state-of-the-art performance. With
synthesizecontext-specificfunctionalitiesonthefly,bypass-
an average score of 89.04%, AGS surpasses all public
ingthefixed-capabilitybottleneckofstaticagenttoolkits.
leaderboard entries, outperforming the next-best agent
Thisdynamictoolcreationandrefinementloop,mediated
ToolOrchestra (87.38%) by 1.66 percentage points. This
entirelythroughtheSEPLoperatorinterface,ensuresthat
advantage is especially pronounced on the hardest tier:
new capabilities are version-tracked and reusable across
AGS scores 81.63% on Level 3, compared to 69.39%
subsequenttasks.
for HALO and 57.14% for AWorld, demonstrating that
evolution-drivenadaptationprovidesthelargestgainswhere Insummary,GAIAconfirmsthatAGP’sself-evolutionpro-
9

Autogenesis:ASelf-EvolvingAgentProtocol
tocolextendsbeyondpurereasoningtaskstocomplex,tool- Table4.Evaluationmetricsforthealgorithmiccodingbenchmark.
intensiveagentscenarios. Thelargestgainsemergeonthe
Metric Description
hardesttasktiers,whereiterativetoolrefinementandhierar-
Capabilitymetrics
chicalresourcemanagementprovidethemostleverage. PR Numberofproblemspassingalltestcaseswithin
timeandmemorylimits.
TLE Numberofproblemsexceedingtheallowedexe-
5.3.ExperimentsonAlgorithmicCodingBenchmark
cutiontimelimit.
MLE Number of problems exceeding the allowed
5.3.1.EXPERIMENTSETTING
memoryusage.
CE Number of problems where generated code
Benchmarkdesignrationale.Ourbenchmarkconstruction
failedtocompile.
isdrivenbythreemotivations: (i)evaluatinginference-time RE Numberofproblemsencounteringaruntimeer-
self-evolutiononexecutablecode,(ii)calibratingagentper- rorduringexecution.
WA Numberofproblemsproducingincorrectoutput.
formance against the distribution of human submissions, TO Numberofproblemswherethemodelfailedto
and(iii)assessingcross-languagerobustnessunderlong-tail respondwithinthetimeout.
RpE Numberofproblemswherethemodelreturned
language usage. We build on top of theLeetCode online
aninvalidorunparseableresponse.
judge,whichprovidesanexecution-basedevaluationinter-
Efficiencymetrics
face and rich feedback signals. Specifically, acceptance
AR Meanruntime(ms)ofacceptedsolutions.
status and per-test-case pass rates enable fine-grained as- AM Meanmemory(MB)ofacceptedsolutions.
APC Meantestcasespassedbeforefailure.
sessmentoffunctionalcorrectnessbeyondbinarysuccess.
Foracceptedsubmissions,theplatformreportsruntimeand Human-referencedmetrics
ARB Percentageofacceptedsolutionswhoseruntime
memoryusagealongwithpercentile-basedruntimebeats outperformshumansubmissions.
andmemorybeatsstatisticscomputedagainstthedistribu- AMB Percentageofacceptedsolutionswhosememory
usageoutperformshumansubmissions.
tionofhumansubmissions,whichdirectlysupportshuman-
referenced evaluation. Finally, LeetCode provides stan-
dardizedstartercodeacrossmanyprogramminglanguages,
Metrics. As shown in Table 4, we report three groups
enablingconsistentandreproduciblemulti-languageevalua-
of metrics that capture complementary aspects of coding
tionunderaunifiedprotocol.
performance. First,capabilitymetricsmeasurefunctional
Datacollection. Wecollectthefullsetof3,822program- correctnessandfailuremodesunderthejudgeconstraints.
mingproblemsavailableonLeetCodeatthetimeofcrawl- Second, efficiency metrics summarize runtime and mem-
ing. For each problem, we extract the natural-language orycostforacceptedsubmissions. Third,humanmetrics
statement, official input–output examples, and language- quantify how often accepted submissions outperform the
specificstartercodetemplates. Eachproblemisannotated distributionofhumansolutionsinruntimeandmemory.
withitsplatform-provideddifficultylabel(Easy,Medium,
TheresultsinTable3andFigure2revealfourkeyfindings
Hard)andtopicaltagsdescribingrequiredalgorithmiccon-
acrosscodingcapability,efficiency,andhuman-referenced
cepts(e.g.,arrays,trees,dynamicprogramming). Weper-
dimensions. (1)Self-evolutionconsistentlyimprovespass
formqualitychecksincludingfilteringmalformedrecords,
rate across all languages. The evolve solution agent
removingduplicates,andvalidatingsuccessfulparsingof
achieves relative pass-rate improvements ranging from
statements, examples, and templates. From the full pool,
10.1% (Python3) to 26.7% (Kotlin), with compiled lan-
weselect100recentlyreleasedtestproblemsacrossdiverse
guagesbenefitingmost: C++reaches99andJava98outof
categoriestomitigatetraining-datacontamination.
100problems. Thesegainsareaccompaniedbybroadreduc-
Evaluationprotocol.Wecompareavanillabaselineagainst tionsinexecution-blockingerrors;compileerror,runtime
AGS with evolve solution enabled. For the vanilla base- error,timeout,andresponseerrorfrequentlydroptozero,
line,theagentpresentsafixedinputrepresentationtothe indicatingthatiterativerefinementeffectivelyrepairsformat
model, deterministically extracts executable source code, andtoolingissuesthatcauseoutrightfailures. Figure2(first
andsubmitsittotheexecution-basedjudgeinasinglepass. row)corroboratesthisfinding,showingconsistentlyhigher
ForAGS,theagentiterativelyrefinessolutionsthroughthe pass-ratetrajectoriesfortheevolvingagentasproblemsac-
SEPLreflectionoptimizerwithinafixedrevisionbudgetof cumulate. (2)Evolutionimprovesruntimeefficiencybut
3rounds,whilekeepingthetaskspecificationandevaluation showsmixedmemoryeffects. Averageruntimedecreases
interfaceunchanged. Thiscontrolledsetupenablesdirect ineverylanguage,withreductionsof7.8%inPython3and
comparisonbetweenone-shotgenerationandinference-time 19.8–46.4%incompiledlanguages. Figure2(secondrow)
self-evolutiononsolutionquality. Weevaluateacrossfive confirms this trend: the evolving agent accumulates sub-
languages(Python3,C++,Java,Go,Kotlin)usingmultiple stantiallylowercumulativeruntime,andthegapwidensas
backbonemodelsandreportmulti-dimensionalmetrics. tasksaccumulate.ThispatternalignswithreductionsinTLE
errors,suggestingthatreflectionhelpsreplacesuboptimalal-
10

Autogenesis:ASelf-EvolvingAgentProtocol
Table3.Resultsbasedongemini-3-flash-preview.Vanillaandevolvesolutionarereported;Improvement(%)denotesrelative
change. indicatesgain; indicatesdegradation.
→ ↑
Agent Capabilitymetrics Efficiencymetrics Humanmetrics
PR TLE MLE CE RE WA TO RpE AR(ms) AM(MB) APC ARB(%) AMB(%)
Python3
vanilla 79 4 0 0 2 14 1 0 1376.19 56.59 750.89 73.28 36.62
evolvesolution 87 3 0 0 1 9 0 0 1269.39 59.08 750.98 70.29 42.15
Improvement(%) 10.1 25.0 0 0 50 35.7 100 0 7.8 4.4 0.0 4.1 15.1
→ → → → → → ↑ ↑ ↑ →
C++
vanilla 84 2 0 2 1 10 0 1 266.04 168.93 743.31 68.02 59.24
evolvesolution 99 0 0 0 0 1 0 0 142.60 148.43 749.86 88.99 73.14
Improvement(%) 17.9 100 0 100 100 90 0 100 46.4 12.1 0.9 30.8 23.5
→ → → → → → → → ↑ → →
Java
vanilla 84 0 0 2 2 9 1 2 125.04 126.09 752.86 71.03 59.18
evolvesolution 98 1 0 0 0 1 0 0 96.30 120.00 751.09 88.33 72.38
Improvement(%) 16.7 0 0 100 100 88.9 100 100 23.0 4.8 0.2 24.4 22.3
→ → → → → → → → → → →
Go
vanilla 82 1 0 9 0 7 0 1 139.22 22.01 739.46 76.22 63.48
evolvesolution 95 0 0 0 0 5 0 0 111.64 18.35 754.17 81.52 67.94
Improvement(%) 15.9 100 0 100 0 28.6 0 100 19.8 16.6 2.0 7.0 7.0
→ → → → → → → ↑ → →
Kotlin
vanilla 75 2 0 8 1 10 2 2 171.99 72.80 760.43 83.49 79.07
evolvesolution 95 1 0 0 0 4 0 0 122.83 77.88 749.38 83.58 67.21
Improvement(%) 26.7 50 0 100 100 60 100 100 28.6 7.0 1.5 0.1 15.0
→ → → → → → → → ↑ ↑ → ↑
gorithmswithmoreefficientones. Memoryusage,however,
showsamixedtrend: itdecreasesinC++,Java,andGobut
increasesmodestlyinPython3andKotlin,plausiblybecause
the evolving agent introduces auxiliary data structures to
ensurecorrectnessorimprovespeed. (3)Evolvedsolutions
becomemorecompetitiveagainsthumansubmissions.
Runtime beats (ARB) increase strongly in compiled lan-
guages,withgainsof30.8%inC++and24.4%inJava,and
smaller gains in Go (7.0%) and Kotlin (0.1%). Memory
beats(AMB)increaseinPython3,C++,Java,andGo,but
decrease in Kotlin (15.0% ). Figure 2 (third row) shows
≃
thattheevolvingagentsustainshigherARBandAMBtra-
jectoriesthanthevanillaagentinmostsettings,indicating Figure2.Performancecomparisonofevolvingandvanillaagents
within-inference.
thatcompetitivenessagainsthumansubmissionsimproves
consistentlyovertheinferencetrajectory. TheKotlindiver-
gencemirrorstheabsolutememorytrendandsuggeststhat
systemandcompilerfeedbackproviderichersignalsforre-
inlong-taillanguagestheevolvingagentmaytradememory
flection. Human-referencedmetricsconfirmthatthesegains
forcorrectnessorspeed. (4)Within-inferencetrajectories translate into solutions that are increasingly competitive
reveal compounding improvement dynamics. Beyond withhumansubmissions. Thewithin-inferencetrajectory
endpoint metrics, Figure 2 enables trajectory-level analy-
analysisfurtherdemonstratesthatAGPnotonlyimproves
sis of self-evolution. Across all three metric groups, the
endpointscoresbutalsoenablesfine-grainedvisibilityinto
gap between evolving and vanilla agents widens as prob-
when and how self-evolution provides the most leverage
lemsaccumulateratherthanplateauing,suggestingthatthe
duringasingleinferenceepisode.
reflection-drivenoptimizercontinuestofindcorrectablefail-
uremodesthroughouttheevaluation. Thiscompounding
6.Conclusion
behaviorismostpronouncedintheruntimepanel,where
cumulativeefficiencygainsaccelerateinlaterproblems.
WepresentedAGP,atwo-layerself-evolutionprotocolthat
Insummary,self-evolutiononthealgorithmiccodingbench- decouples what evolves from how evolution occurs. The
mark delivers consistent improvements in functional cor- ResourceSubstrateProtocolLayer(RSPL)modelsprompts,
rectness and runtime efficiency across all five languages, agents,tools,environments,andmemoryasfirst-class,ver-
withthelargestgainsincompiledlanguageswherethetype sionedresourceswithexplicitlifecycleandinterfacecon-
11

Autogenesis:ASelf-EvolvingAgentProtocol
tracts. TheSelf-EvolutionProtocolLayer(SEPL)specifies
a closed-loop operator algebra for proposing, evaluating,
andcommittingimprovementswithauditablelineageand
rollback. Buildingonthisprotocol,weinstantiatedAGS,a
thinking-and-actionagentthatdynamicallyretrieves,refines,
andevolvesheterogeneousresourcesduringexecution. We
believethisprotocol-levelapproachtoself-evolutionpro-
videsaprincipledfoundationforbuildingmodular,trace-
able,andsafelyimprovableagenticsystems.
12

Autogenesis:ASelf-EvolvingAgentProtocol
References
Anthropic. Equipping agents for the real
world with agent skills. https://
www.anthropic.com/engineering/
equipping-agents-for-the-real-world-with-agent-skills,
2025a. AccessedOctober2025.
Anthropic. Introduction to agent skills.
https://anthropic.skilljar.com/
introduction-to-agent-skills, October
2025b.
Hu, J. Reinforce++: A simple and efficient approach
for aligning large language models. arXiv preprint
arXiv:2501.03262,2025a.
Hu, J. Reinforce++: A simple and efficient approach
for aligning large language models. arXiv preprint
arXiv:2501.03262,2025b.
LeetCode. Leetcodeonlinejudge. https://leetcode.
com. Accessed2025.
Mialon,G.,Fourrier,C.,Wolf,T.,LeCun,Y.,andScialom,
T. Gaia: abenchmarkforgeneralaiassistants. InThe
TwelfthInternationalConferenceonLearningRepresen-
tations,2023.
Rein,D.,Hou,B.L.,Stickland,A.C.,Petty,J.,Pang,R.Y.,
Dirani, J., Michael, J., and Bowman, S. R. Gpqa: A
graduate-level google-proof q&a benchmark. In First
ConferenceonLanguageModeling,2024.
Shao,Z.,Wang,P.,Zhu,Q.,Xu,R.,Song,J.,Bi,X.,Zhang,
H.,Zhang,M.,Li,Y.,Wu,Y.,etal. Deepseekmath: Push-
ingthelimitsofmathematicalreasoninginopenlanguage
models. arXivpreprintarXiv:2402.03300,2024.
Yuksekgonul, M., Bianchi, F., Boen, J., Liu, S., Lu, P.,
Huang,Z.,Guestrin,C.,andZou,J. Optimizinggener-
ative ai by backpropagating language model feedback.
Nature,639(8055):609–616,2025.
13

Autogenesis:ASelf-EvolvingAgentProtocol
A.Notation
WesummarizethemainmathematicalsymbolsandtheirmeaningsinTable5. Forreadability,thenotationisgroupedby
functionalcategories(greyrows),coveringtheRSPLsubstrate(resourceentities,registrationrecords,andregistries)andthe
SEPLlayer(evolvablevariables,auxiliaryspaces,andoperatordefinitionsusedintheoptimizationloop).
Table5.Notationusedinthepaper.Greyrowsindicatecategories.
Symbol Description
IndexingandSets
SetofRSPLentitytypes, PROMPT,AGENT,TOOL,ENV,MEM .
T { }
ω Entitytypeindex,ω .
↓T
ω
Indexsetofresourceinstancesoftypeω.
I
i Instanceindex,i ω.
↓I
V Spaceofversionstrings.
ε() Powersetoperator.
·
RSPLResourceEntity(Def.C.1)
e
ω,i
Resourceentitytuple(n
ω,i
,d
ω,i
,ϑ
ω,i
,g
ω,i
,m
ω,i
).
n ω,i Uniqueresourcename.
d ω,i Shortdescription.
ϑ ω,i : ω ω Input-to-outputmappingoftheresource.
X ↔Y
g ω,i Trainablemarkerindicatingwhethertheresourceisevolvable.
m ω,i Auxiliarymetadatadictionary.
ω
Setofresourceentitiesoftypeω.
E
RSPLRegistrationRecord(Def.C.2)
c
ω,i
Registrationrecord(e
ω,i
,v
ω,i
,ϖ
ω,i
,ϱ
ω,i
,
ω,i
).
F
ω
Setofregistrationrecordsfortypeω.
C
v ω,i Versionstringoftheresourceinstance.
ϖ ω,i Implementationdescriptor(e.g.,importpath,class,orsource).
ϱ ω,i Instantiationparameters(e.g.,constructorarguments).
ω,i ExportedrepresentationsforLLMinteraction(schemas/text/structuredargs).
F
Protocol-registeredResource(Def.C.3)
ω Type-specificregistryofprotocol-registeredresources.
R
R
Globalregistry,
ωR
ω.
ω Contextmanagerfortypeω (maintainsregistryandversionlineage).
M ω Server-exposedi!nterfacefortypeω (delegatesto ω).
A M
r
ω
Type-levelregisteredresourcetriple(
ω
,
ω
,
ω
).
C M A
SEPLVariables,Spaces,andOperators
Universalsetofevolvablevariables(allmanagedentitiesplusexecutionartifacts).
Vevo
v Avariablein .
Vevo
g
v
Learnabilityconstraintforvariablev(binary).
! Trainablesubspace, { v ↓Vevo | g v =1 } .
y Executionartifacts(e.g.,outputsandreasoningtraces).
Tracespace.
Z
Hypothesisspace.
H
Modificationspace.
D
Objectivespecification.
G
Evaluationspace(metricsandsafetystatus).
S
ς,φ,↼,↽,⇀ Reflect,Select,Improve,Evaluate,andCommitoperators.
OptimizationLoop(Alg.1)
A Agenticsystem.
T Optimizationbudget(numberofiterations).
t Iterationindex.
(t) Evolvablestateatiterationt.
Vevo
(t) Observationaltraceatiterationt.
Z
(t) Hypothesesatiterationt.
H
(t) Proposedmodificationsatiterationt.
D
(t+1) Candidatestateafterapplyingmodifications.
Vevo
(t+1) Evaluationresultforthecandidatestate.
S
"
14

Autogenesis:ASelf-EvolvingAgentProtocol
B.ComparisonwithOtherProtocols
We provide a structured comparison between Autogenesis, Google A2A, and Anthropic MCP in Table 6. The goal
of this comparison is to position Autogenesis relative to widely used protocol abstractions in agent tooling, and to
clarify which protocol-levelprimitives are required to make self-evolution composable, auditable, and safe inpractice.
Accordingly,thecomparisonisorganizedintofourhigh-leveldimensions(greyrows): BasicInformation,AgentandSystem
Capabilities,EvolvableResourceManagement,andSelf-EvolutionMechanism. Blue-highlightedentriesemphasizethe
specificcapabilitiesthatenableclosed-loopimprovement(e.g.,lifecyclecontrol,versionlineage,contractgeneration,and
operatorizedupdates),whicharenotdirectlyaddressedbycommunication-orinvocation-centricprotocols.
Table6.Protocol-levelcomparison:Autogenesisvs.GoogleA2Avs.AnthropicMCPacrosskeydimensionsforagenticsystemsandself-
evolution.Symbols:↫=Supported, =Partial, =Notsupported.Highlightedrows(bluebackground)emphasizeevolution-enabling
↗ ↘
capabilities.
Dimension Autogenesis A2A MCP
BasicInformation
Proposer Ourwork Google Anthropic
ProtocolFocus Self-evolutionAgenticSystem Multi-agentSystemCollaboration Tool
EntityScope Prompt/Agent/Tool/Env/Memory Agent/Tool Tool
AgentandSystemCapabilities
AgentFirst-Class ↫ ↫
↘
Multi-Agent ↫ ↫
↘
Tracer ↫
↗ ↘
MemoryasResource ↫
↘ ↘
EvolvableResourceManagement
LifecycleOps ↫
↗ ↘
VersioningandRollback ↫
↘ ↘
RegistryandRetrieval ↫
↗ ↗
ContractGeneration ↫
↗ ↘
Self-EvolutionMechanism
Closed-LoopEvolution ↫
↘ ↘
OperatorizedUpdates ↫
↘ ↘
Auditability ↫
↗ ↗
GeneralandEcosystem
Model-Agnostic ↫ ↫ ↫
Scalability O(logn) O(n2) O(n)
OpenEcosystem ↫
↗ ↗
B.1.BasicInformation
Proposer: Thisdimensionidentifiestheoriginatingorganizationanddesigncontextofeachprotocol. Google’sA2Ais
introduced as part of an agent communication framework, focusing on enabling agents to collaborate via standardized
interactionprimitives. Anthropic’sMCP(ModelContextProtocol)isdesignedtostandardizehowLLMsconnecttoexternal
toolsandresources. Autogenesisisproposedinthisworkasaprotocolforsystematicself-evolution,targetingcomposable,
auditable,andupdateableagenticsystems.
ProtocolFocus: Thisdimensiondescribestheprimaryinteractionpatternsandcontrolplaneeachprotocolstandardizes.
Autogenesisfocusesonenablingclosed-loopimprovementofagenticsystemsbyorganizingresourcesandupdatesthrough
protocoloperatorsandversionedstate. A2Afocusesonmulti-agentcollaborationandcommunication. MCPfocuseson
standardizingmodel-to-tool(andresource)invocationinterfaces.
EntityScope: Thisdimensiondefineswhatistreatedasfirst-class,protocol-governedcomponents. Autogenesisexplicitly
managesheterogeneousentities(e.g.,prompts,agents,tools,environments,andmemory)asprotocol-registeredresources
withexplicitstateandlineage,whichisnecessaryforcomponent-levelevolution(e.g.,promptrefinement,tool/codeupdates).
A2Acentersaroundagents(andtheirinteractions),andtypicallydoesnotestablishtools/environments/memoryasunified
15

Autogenesis:ASelf-EvolvingAgentProtocol
managedentities. MCPtreatstools/resourcesascallableinterfacesforLLMs,butdoesnotnativelymodelthemasevolvable
componentswithlifecycleandversionlineage.
B.2.AgentandSystemCapabilities
AgentFirst-Class: First-classsupportmeansagentsaremodeledasmanagedprotocolcomponentswithexplicitschemas,
metadata,andlifecyclehooks(enablingregistration,discovery,orchestration,andcontrolledupdates). Autogenesissupports
agentsasfirst-classresources. A2Aprovidesagent-centriccollaborationbutoftentreatsagentsasserviceendpointswithout
unifiedlifecycle/versionlineage. MCPdoesnotdefineagentsasprotocolcomponents,focusinginsteadonmodel-to-tool
connectivity.
Multi-Agent: Thisdimensioncaptureswhethertheprotocolnativelysupportsmulti-agentcompositionbeyondad-hoc
applicationlogic.Autogenesissupportsmulti-agentconfigurationsaspartofabroadersystemsubstrate,enablingcoordinated
executionwithtraceabilityandevolution-readystate. A2Aprovidesdirectsupportforagent-to-agentcollaboration. MCP
doesnotaddressmulti-agentorchestrationasaprotocolconcern.
Tracer/Observability: Observability refers to whether the protocol provides native mechanisms to record execution
traces(inputs/outputs,intermediatedecisions,toolcalls,statetransitions)fordebugging,evaluation,andlearningsignals.
Autogenesis includes protocol-level tracing to support auditable evolution. A2A and MCP typically leave tracing to
application-levelimplementations,whichcanleadtoinconsistentobservability.
MemoryasResource: Thisdimensionreflectswhethermemoryisexplicitlymodeledandmanagedasaprotocol-levelcom-
ponent. Autogenesistreatsmemoryasafirst-classresource(e.g.,readable/writablestatewithexplicitinterfaces),enabling
persistentimprovementandreproducibleevolution. A2AandMCPgenerallydonotprescribeamemorymanagement
protocol,leavingmemorytoexternalsystems.
B.3.EvolvableResourceManagement
LifecycleOps: Lifecycleoperationsrefertostandardizedproceduresforinitializing,registering,constructing,anddecom-
missioningprotocol-managedcomponents. Autogenesisprovidesexplicitlifecycleoperatorssothatupdatescanbeapplied
safelytowell-definedtargets. A2AandMCPdonotprovidecomprehensivelifecyclemanagementacrossheterogeneous
componenttypes.
VersioningandRollback: Versionlineageandrollbackprovidethefoundationforsafeevolution: everyupdateyields
an auditable snapshot, supports comparison, and enables restoration when regressions occur. Autogenesis integrates
versionmanagementasaprotocolcapability. A2AandMCPdonotnativelysupportversionlineageforprotocol-managed
components,makingsystematicevolutiondifficult.
RegistryandRetrieval: Thisdimensioncaptureswhethertheprotocolsupportsunifiedregistration,listing,andretrievalof
components(optionallyviasemanticsearch)toenablereuseandscalablecoordination. Autogenesismaintainsaregistryof
protocol-registeredcomponentsandsupportsretrievaltoreduceduplicationandimprovecomposability. A2AandMCP
providepartialdiscoverymechanismsbutdonotdefineaunifiedmanagementplaneoverheterogeneouscomponents.
ContractGeneration: Contractgenerationreferstoproducingconsolidated,up-to-datecapabilityandconstraintspecifica-
tions(e.g.,toolactions,arguments,preconditions,usageconstraints)forreliableorchestrationandreducedpromptbloat.
Autogenesissupportscontractgenerationasasystematicformofcontextengineering. A2AandMCPgenerallyrelyon
staticdescriptionsorapplication-layerdocumentationwithoutprotocol-levelcontractaggregation.
B.4.Self-EvolutionMechanism
Closed-LoopEvolution: Closed-loopevolutionmeanstheprotocolsupportsaniterativeimprovementloop(execute
↑
diagnose propose verify commit)ratherthanone-offadaptation. Autogenesisisexplicitlydesignedaroundthis
↑ ↑ ↑
looptoenablesustainedimprovement. A2AandMCPdonotprovideanativeself-evolutionloop.
OperatorizedUpdates: Thisdimensioncaptureswhethersystemupdatesareexpressedasatyped,composableoperator
interface(ratherthanad-hocscripts),enablingcontrolledstatetransitionsandrepeatableevolution. Autogenesisdefines
self-evolutionasoperator-mediatedtransitionsoverprotocol-managedresources. A2AandMCPdonotdefineanoperator
algebraforevolution.
16

Autogenesis:ASelf-EvolvingAgentProtocol
Auditability: Auditabilitymeansthatsystemchangesaretraceableandreviewable: whatchanged,whyitchanged,under
whatevidence,andwithwhatevaluationoutcome. Autogenesisemphasizesauditabilitythroughversionedlineageand
trace-basedevaluationsignals. A2AandMCPprovideonlypartialaudittrailsviaexternaltoolingratherthanprotocol-level
guarantees.
B.5.GeneralandEcosystem
Model-Agnostic: ThisdimensioncaptureswhethertheprotocolcanworkacrossdifferentLLMbackendsandproviders.
Autogenesisismodel-agnosticbydesignviaaunifiedmodelinterfacelayer. A2AandMCParealsobroadlymodel-agnostic
astheydefineinteractionstandardsratherthanbindingtoaspecificmodel.
Scalability: Scalabilityreflectshowcoordinationanddiscoverybehaveasthenumberofcomponentsgrows. Autogenesis
supportsscalablemanagementbytreatingheterogeneouscomponentsasregistry-governedresourceswithretrievalmecha-
nisms,enablingefficientlookupandcontrolledorchestration. A2Amayfacecoordinationoverheadasinteractionsdensify
inlargemulti-agentsettings. MCPstandardizestoolinterfacesbutmaystillrelyonapplication-levelorchestrationforlarge
tool/resourcesets.
OpenEcosystem: Openecosystemsupportreferstowhethertheprotocolcanenableareusableecosystemofinteroperable
components. Autogenesis provides a full protocol stack for managing, evolving, and auditing agentic components,
whichsupportscomponentsharingandsafeintegration. A2AandMCPofferpartialecosystemenablementfocusedon
interoperabilityortoolinterfaces,typicallyrequiringadditionallayersforevolution-readymanagement.
C.DetailsofSelf-EvolutionProtocol
C.1.Layer1: ResourceSubstrateProtocolLayer
TheResourceSubstrateProtocolLayer(RSPL)definestheevolvablesubstrateasasetofprotocol-registeredresourceswith
explicitstate,lifecycle,andversionlineage. Inthispaper,theseresourcescomprise(i)instructions(Prompt),(ii)decision
policies(Agent),(iii)actuationinterfaces(Tool),whichencompassnativetoolscripts,MCPtools(Anthropic,2025a),and
agentskills(Anthropic,2025b), (iv)task/worlddynamics(Environment), and(v)persistentstate(Memory). Crucially,
resourcesinRSPLarepassive: theyencapsulatenooptimizationlogicandcannotself-modify;allobservationsandstate
transitionsoccuronlythroughcontrolled,interface-mediatedoperationsinvokedbyhigherlayers.
C.1.1.COREENTITIES
Wefocusonthesefiveentitytypesasaminimalyetexpressivesubstrateforagenticsystems. Thischoiceisnotintendedto
beexhaustive,butrathertoidentifyacommondenominatoracrossmodernagentstacksandprovideauniformtargetspace
onwhichSEPLcanoperate.
DefinitionC.1(ResourceEntity). Aresourceentityoftypeω anditstype-levelcollectioncanberepresentedas:
e =(n , d ,ε , g , m ),
ω,i ω,i ω,i ω,i ω,i ω,i
(5)
= e i ,
ω ω,i ω
E { | →I }
where = PROMPT,AGENT,TOOL,ENV,MEM denotesthesetofRSPLentitytypes,ω indexestheentitytype,
T { } →T
istheindexsetofresourceinstancesoftypeω,andi indexesanindividualinstance. Heren isauniqueresource
ω ω ω,i
I →I
name,d isashortdescription,ε : isaninput-to-outputmapping,g 0,1 isthetrainablemarkerthat
ω,i ω,i ω ω ω,i
X ↑Y →{ }
indicateswhethertheresourceisevolvable,andm isanauxiliarymetadatadictionary.
ω,i
A key motivation for making prompt, tool, and memory explicit RSPL resources is decoupling. Many agent systems
packageprompts,tools,andmemoryasinternalcomponentsofanagent,whichentanglesagentlogicwithtask-specific
instructions and capability bundles, increasing maintenance and limiting transfer. By externalizing them as first-class,
versionedresourceswithstandardizedinterfaces,thesametool-callingagentpolicycanbepairedwithdifferentprompts
andtoolsets,anddeployedunchangedacrosstasksandenvironments.
Tosupportresourceregistration,unifiedmanagement,andinstantiation,RSPLstoresaserializableregistrationrecordfor
eachresourceinstance.
DefinitionC.2(ResourceRegistrationRecord). Aresourceregistrationrecordanditstype-levelcollectioncanberepresented
17

Autogenesis:ASelf-EvolvingAgentProtocol
as:
c =(e , v ,ϑ ,ϖ , ),
ω,i ω,i ω,i ω,i ω,i ω,i
F (6)
= c i ,
ω ω,i ω
C { | →I }
whereω indexestheentitytypeandi indexesanindividualinstance. Heree istheresourceentitytupledefined
ω ω,i
→T →I
inTheoremC.1,v
ω,i
Visaversionstring,ϑ
ω,i
isanimplementationdescriptor(e.g.,importpath,classdefinition,orsource-
→
codestring),ϖ areinstantiationparameters(e.g.,constructorarguments),and isasetofexportedrepresentations
ω,i ω,i
F
usedbyLLMstointeractwiththeresource(e.g.,function-callingschema,natural-languagetext,andstructuredargument
schema).
DefinitionC.3(Protocol-registeredresource). Foreachentitytypeω,let
ω
denotethetype-specificregistryofprotocol-
R
registeredresources,andlet = denotetheglobalregistry. RSPLbindseachentitytypeω toadedicatedcontext
R ωR ω
manager andaserver-exposedinterface . Werepresentthetype-levelregisteredresourceas
ω ω
M ! A
r =( , , ), (7)
ω ω ω ω
C M A
whereeachc isaregistrationrecordinTheoremC.2. Thecontextmanager maintainsthecollection ,the
ω,i ω ω ω
→C M C
versionlineagefortypeω,andimplementslifecycleandupdateoperationsovertheserecords;theserver-exposedinterface
encapsulates andexposesaunifiedexternalinterfacebydelegatingrequeststothecorrespondingcontext-manager
ω ω
A M
routines.
C.1.2.CONTEXTMANAGER
Thecontextmanagerimplementsthemanagementplaneforeachresourcetype. Beyondlifecyclecontrolanddependency
constraints,itmaintains(i)anactiveregistryofmaterializedresourcesand(ii)aversionedhistoryforrestoration.Itsexported
APIcanbeviewedasasmallsetoffunctionallygroupedoperatorsforlifecycleandregistration(e.g., init, build),
retrievalandinspection(e.g.,list,get state),evolutionandversioning(e.g.,update,restore),executionand
contract(e.g.,run,load contract),andserializationanddeserialization(e.g.,save to json,load from json).
Themanagerexplicitlysupportscontractgeneration,producingaconsolidatedcapabilityandconstraintspecificationforthe
managedentities,whichprovidesstable,up-to-datedescriptionsthatimprovereliabilityandreducepromptbloat,enabling
systematiccontextengineeringviacontrolledpromptinjection. Forinstance,fortools(whichmaybenativetoolscripts,
MCP-connected tools (Anthropic, 2025a), or agent skills) the contract can take a skills.md-style form (Anthropic,
2025b)thatenumeratestoolactions,arguments,preconditions,andusageconstraints. Theexportedmanagementinterface
implementedby andexposedby areasfollows:
ω ω
M A
C.1.3.SERVERINTERFACE
Theserverisintroducedtoencapsulatethecontextmanager’sinternalcomplexityandpresentastable,simplifiedinterface
forexternalcallers. Itpackagesheterogeneousmanagementroutinesbehindauniformsetofendpointswithconsistent
request/responsesemantics,whiledelegatingtheimplementationdetailstothecontextmanager. Thisseparationisolates
clientsfrominternaldesignchanges,reducescoupling,andprovidesasinglecontrolplanethroughwhichtheprotocol
mediatessafe,version-awareinteractionswithRSPLresources.
C.1.4.INFRASTRUCTURESERVICES
RSPLfurtherincludescross-cuttingservicesthatsupportreliableevolution,includingreproducibility,safedeployment,and
versionedrecovery:
Modelmanager. Aunifiedmodel-APIlayerthatstandardizescallsacrossproviders(e.g.,OpenAI,Anthropic,Google,
andOpenRouter, etc.), whilesupportingrouting, fallback, andcost-awareselectiontokeepmodelaccessconsistentas
componentsevolve.
Versionmanager. Maintainsversionlineageforeachresource,enablingrollback,branching,anddiffing. Versionsare
auto-incrementedidentifiers(e.g.,semanticversions)assignedonregisterorupdate,eachreferencinganimmutablesnapshot
oftheconfigurationrecordandassociatedartifactsforauditabilityandreproducibility.
Dynamicmanager. Handlesserializationordeserializationofresourceconfigurationsforpersistenceandtransfer,enabling
safehot-swappingofresourcesatruntimewithoutrestartingtheagentsystem.
18

Autogenesis:ASelf-EvolvingAgentProtocol
Table7.OperatorsetofContextManagerandServerInterface.
Operator Description
Lifecycle&Registration
init Autodiscoverresourcesandregistertheresourceconfigurationtotheregistry.
build Buildaresourceinstancefromcodeandconfiguration.
register Registeranewresourceinstancewithauniquenameandversion.
unregister Unregisteraresourceinstancefromtheactiveregistryandversionhistory.
Retrieval&Inspection
get Retrievearesourceinstancebynamefromtheactiveregistry.
get info Retrievearesourceconfigurationbynamefromtheactiveregistry.
list Listallregisteredresourcenames.
retrieve Retrievesimilarresourcesviasemanticsearchwhensupported.
get state Getthecurrentstateofaresourceinstancewhensupported.
Evolution&Versioning
update Updatearesourceimplementationandgenerateanewversion.
copy Duplicatearesourcewithanoptionalnewnameandversion.
restore Restoreaspecifichistoricalversionbynameandversionstring.
get variables Exposeresourcecode/configurationasevolvablevariables.
set variables Updateresourcevariablesandgenerateanewversion.
Execution&Contract
run Runaresourceinstancewithstructuredinput.
save contract Savethecontractofaresourceinstancetoafile.
load contract Loadthecontractofaresourceinstancefromafile.
Serialization&Deserialization
save to json SerializeconfigurationsandversionhistorytoaJSONfile.
load from json DeserializeconfigurationsandversionhistoryfromaJSONfile.
Tracer Module. A module that captures fine-grained execution traces (inputs, outputs, intermediate decisions, tool
interactions, etc.) for interpretability and debugging, and as training signals for dataset synthesis and retrospective
improvement.
C.2.Layer2: Self-EvolutionProtocolLayer
TheSelf-EvolutionProtocolLayer(SEPL)specifieshowanagenticsystemcanimproveitselfthroughaprincipledclosed-
loopoperatorinterface. SEPLframesself-improvementasiterativestatetransitionsoveraheterogeneousevolvablestate,
whileroutingallmodificationsthroughstandardizedRSPLinterfacessothatupdatesremainauditable(versioned),reversible
(restorable),andsafebyconstruction.
C.2.1.OVERVIEW
SEPLconceptualizescontinuousimprovementasageneralizedoptimizationproblemoverastructuredevolvablestatespace.
Formally,SEPLtreatsevolutionarydynamicsasstatetransitionsgovernedbyastrictlytypedoperatoralgebra,enabling
differentoptimizationstrategiestosharethesamemutationsurfaceandsafety/verificationgates. Inoursystem, SEPL
admitsmultipleinstantiations—includingreflection-drivenoptimization(ourdefault),TextGrad(Yuksekgonuletal.,2025),
GRPO(Shaoetal.,2024),andReinforce++(Hu,2025b). Wedonotexpandtheirfullmechanicsinthisoverview;instead,
wesummarizetheirvariables,operators,andloopproceduresindedicatedsubsectionsbelow.
C.2.2.EVOLVABLEVARIABLES
SEPLreliesonvariableliftingtoprojectheterogeneousRSPLresources(e.g.,prompts,toolimplementations(nativescripts,
MCPtools, oragentskills), andmemorymodules)intoaunifiedevolvablevariablespace. Thisabstractionprovidesa
commoninterfaceforallevolutionoperatorsandmakesthelearnablesubspaceexplicitviaabinarylearnabilitymask. We
referreaderstothemaintext(SEPL,EvolvableVariables,Definition“EvolvableVariableSet”)fortheformaldefinitionof
andtheassociatedlearnabilityconstraint.
evo
V
19

Autogenesis:ASelf-EvolvingAgentProtocol
C.2.3.OPERATORALGEBRA
SEPL formalizes evolution as a composition of typed operators over auxiliary spaces, aligning with the canonical
phases of iterative optimization (observation, attribution, proposal, verification, and commit). We adopt the reflection-
driven instantiation in the main text as the canonical example: it specifies a minimal operator suite ϱ,φ,↼,↽,⇀ (Re-
{ }
flect/Select/Improve/Evaluate/Commit)operatingoverthetrace,hypothesis,modification,objective,andevaluationspaces
( , , , , ). Wereferreaderstothemaintext(OperatorAlgebra)fortheformaloperatorsignaturesandtheirsemantics;
Z H D G S
belowweprovidemethod-specificoperatorizationsforTextGrad,GRPO,andReinforce++inadditiontoreflection.
C.2.4.REFLECTIONOPTIMIZER
Evolvable Variables. In the reflection-driven instantiation, the evolvable state is given by the lifted variable set
evo
V
introducedinthemaintext(SEPL,EvolvableVariables). Concretely, includesRSPL-managedresources(e.g.,prompts,
evo
V
tools,memories,andagentcomponents)togetherwithexecutionartifacts(e.g.,theproducedanswerandreasoningtrace).
Abinarylearnabilitymaskspecifieswhichvariablesmaybemodified,allowingtheoptimizertotargetonlyauthorized
componentswhilekeepingnon-learnableresourcesfixed.
OperatorAlgebra. WeinstantiateSEPLwiththecanonicalreflection-drivenoperatorsuiteinthemaintext(Operator
Algebra). Forcompleteness,werestatetheoperatorsignaturesandtheirintendedrolesbelow.
• Reflect(ϱ). Definedasϱ: ς( ),thisoperatorbridgesthegapbetweenrawobservationandoptimization
evo
Z↔V ↑ H
direction. Itapproximatesthe“semanticgradient”ofthesystembymappinghigh-dimensionalexecutiontracestospecific,
causalfailurehypotheseswithinthevariablespace.
• Select(φ). Formulatedasφ : ς( ) ς( ),thisoperatoractsasthegenerativepolicy. Ittranslatesdiagnostic
evo
V ↔ H ↑ D
hypothesesintoconcreteupdateproposals,samplingcandidatemodifications designedtominimizetheidentifiederror
D
signalsubjecttostructuralconstraints.
• Improve(↼). Themutationoperator,↼:
V
evo
↔
ς(
D
)
↑Ve↑vo
,executesthephysicalstatetransition. Itappliesdiscrete
updates viastandardizedRSPLinterfacestoyieldaprovisionalcandidatestate.
D
• Evaluate(↽). Specifiedas↽:
Ve↑vo↔G↑S
,thisoperatorservesastheobjectivefunction. Itmapsthecandidatestate
andgoalspecificationtotheevaluationspace (comprisingquantitativescoresandstrictsafetyinvariants).
S
• Commit(⇀). Operatingas⇀ :
Ve↑vo↔S↑V evo
,thisfunctionactsasaconditionalgatingmechanism. Itutilizesthe
evaluationsignalsin togovernstatetransition,rigorouslyenforcingsafetyinvariantsandperformancemonotonicityby
S
acceptingthecandidate onlywhenspecificsuccesscriteriaaremet.
Ve↑vo
The Evolutionary Loop. These operators are composed into the reflection-driven closed-loop procedure shown in
(0)
Algorithm 2. Starting from an initial lifted state , the agent first executes to collect an observational trace (tool
evo
V Z
outputs,intermediatedecisions,failures,andprogresssignals). Thereflectoperatorϱmaps toasetofcausalhypotheses
Z
,whicharethentranslatedbyφintoconcretemodificationprimitives (e.g.,promptedits,tooladjustments,ormemory
H D
updates)overthelearnablesubsetof . Theimproveoperator↼applies viaRSPLinterfacestoobtainacandidate
evo
V D
state,whichisevaluatedby↽toproduce capturingbothperformancemetricsandsafetyconstraints. Finally,thecommit
S
operator⇀gatesthetransitionbyacceptingonlycandidatesthatsatisfythepredefinedcriteria,recordingeachaccepted
changeasaversionedresourceupdatewithauditablelineageandenablingrollbackwhennecessary.
C.2.5.TEXTGRADOPTIMIZER
EvolvableVariables. IntheTextGradinstantiation,theevolvablevariablesarerestrictedtoasubsetofpromptvariables
marked as optimizable and lifted into TextGrad variables with explicit role descriptions. In our implementation, each
optimizablepromptmoduleisrepresentedasaTextGradvariablewhosevalueisthecurrentprompttextandwhoserole
descriptionspecifiestheprompt’sfunction,enablingtheoptimizertoconditionupdatesonitsintendedsemantics.
Operator Algebra. TextGrad instantiates SEPL with a prompt-level operatorization in which “gradients” are natural-
languagecritiquesproducedbyanLLMevaluatorandupdatesareimplementedasconstrainedpromptrewrites. Following
thestandardTextGradview,weexpressthemethodwithfivecoreoperators,namelyExecute,Loss,Backward,Improve,and
Commit,wherethe“gradient”isapieceoftext(acritique)ratherthananumericvector:
• Execute(⇁ tg). ⇁ tg :(A, evo ,x,f) runstheagentunderthecurrentpromptvariablesandproducesanexecution
V ↑Z
trace/outcome.
• Loss(λ tg). λ tg : tg ,where tg isaspaceofnatural-languagecritiques(textualgradients). Inourimplementation,
Z↑G G
20

Autogenesis:ASelf-EvolvingAgentProtocol
Algorithm2ReflectionOptimizerEvolutionaryLoop
Input: AgenticSystemA,Objective ,BudgetT
G
Output: Optimizedstate Ve↓vo
1: Initialization:
2: e ( v 0 o ) VariableLifting(A) ↭Projectresourcestooptimizationmanifold
V ↗
3: (0) Execute(A, e ( v 0 o )) ↭Trace:toolI/O,failures,latencies,progress
Z ↗ V
4: OptimizationCycle:
5: fort=0,1,...,T 1do
↘
6: //Phase1: Diagnosis&Proposal
7: (t) ϱ( (t), e ( v t o )) ↭Reflect:attributefailures/inefficiencies
H ↗ Z V
8: (t) φ( e ( v t o ), (t)) ↭Select:proposeeditsoverlearnablevariables
D ↗ V H
9: //Phase2: Mutation&Verification
10: e ( v t o +1) ↼( e ( v t o ), (t)) ↭Improve:applyproposedupdates(candidate)
V ↗ V D
11: (t+1) ↽( e ( v t o +1), ) ↭Evaluate:metrics+safetyinvariants
S ↗ V G
%
12: //Phase3: Gating&Transition
13: ifAccept( (t%+1))then
S
14: //Accept: safe&non-degrading
15: e ( v t o +1) ⇀( e ( v t o +1), (t+1)) ↭Commit:versionedupdate
V ↗ V S
16: else
17: //Reject: roll%back/keeppreviousstate
(t+1) (t)
18: evo evo
V ↗V
19: endif
20: //Phase4: NextIteration
21: (t+1) Execute(A, e ( v t o +1)) ↭Re-rununderupdatedresources
Z ↗ V
22: ifConverged( (t+1))then
S
23: break
24: endif
25: endfor
(t)
26: return evo
V
λ isrealizedbyTextLoss,whichqueriesanevaluatorLLMandreturnscritiquefeedback.
tg
• Backward(β tg). β tg : evo tg evo assignstextualgradientstooptimizablepromptvariablesbystoringthecritique
V ↔G ↑V
(optionallywithcontext)inaper-variablegradientbuffer. Inourcurrentimplementation,wedistributethesamecritique
toeachoptimizablepromptvariableforstability.
• Improve(↼ tg). ↼ tg :
V
evo ↑Ve↑vo rewritespromptvariablesviaatextual-gradient-descentstep: itconstructsanupdate
instruction from each variable’s role description, current value, and accumulated textual gradients, then queries an
optimizerLLMandextractstheimprovedvariabletextfromaconstrainedoutputformat.
• Commit(⇀ tg). ⇀ tg : Ve↑vo
↑V
evo synchronizestheupdatedpromptvariablesbackintotherunningagentandclears
caches,completingthestatetransition.
TheEvolutionaryLoop. Algorithm3presentsthefullTextGradoptimizationcycleinoperatorform. Ateachiteration,
theagentisexecutedunderthecurrentpromptvariablestoobtainatrace via⇁ ,anLLM-basedevaluatorproducesa
tg
Z
natural-languagecritiqueg viaλ ,thecritiqueisassignedasatextualgradienttotheoptimizablepromptvariables
tg tg
→G
viaβ ,thepromptvariablesareimprovedvia↼ usingtextual-gradient-descent,andthecandidatestateiscommittedvia
tg tg
⇀ tosynchronizetheupdatedpromptsbackintotherunningagent(andclearcaches)beforethenextiteration.
tg
C.2.6.REINFORCE++OPTIMIZER
EvolvableVariables. Reinforce++optimizesatrainablesubsetofRSPLresources,focusingonpromptvariablesandtool
implementations(nativescripts,MCPtools(Anthropic,2025a),andagentskills(Anthropic,2025b)),andoptionallyrefining
theproducedsolutiontext. Ourimplementationfollowsatwostagestructure: (i)updatetrainablevariablesthatgovern
behavior(e.g.,promptsandtools),and(ii)updatethesolutionitselfwhenenabled.
21

Autogenesis:ASelf-EvolvingAgentProtocol
Algorithm3TextGradPromptOptimizationLoop
Input: AgenticSystemA,taskx,attachmentsf (optional),BudgetK,evaluator/optimizerLLMsM ,M
eval opt
Output: Updatedstate Ve↓vo (promptvariablesupdatedviaTextGrad)
1: //Phase0: Setup
2: SetbackwardenginetoM eval ↭EvaluatorusedbyTextLoss
3: e ( v 0 o ) VariableLifting(A) ↭LiftoptimizablepromptstoTextGradvariables
V ↗
4: InitializetextualoptimizerwithM opt ↭TextualGradientDescentoverpromptvars
5: //OptimizationCycle
6: fork =0,1,...,K 1do
↘
7: //Phase1: Execute(Forward)
8: (k) ⇁ tg (A, e ( v k o ),x,f) ↭Runagentwithcurrentprompts
Z ↗ V
9: //Phase2: Loss(TextualGradient)
10: Buildevaluationinstructionfrom (k) ↭Conditiononsuccess/error
Z
11: g(k) λ tg ( (k)) ↭TextLossproducescritiquestring
↗ Z
12: //Phase3: Backward(AssignGradients)
13: e ( v k o ) β tg ( e ( v k o ),g(k)) ↭Assigncritiquetogradientbuffers
V ↗ V
14: //Phase4: Improve(TextualGradientDescent)
15: e ( v k o +1) ↼ tg ( e ( v k o )) ↭RewritepromptsviatextualGD
V ↗ V
16: //Phase5: Commit&NextIteration
17: % e ( v k o +1) ⇀ tg ( e ( v k o +1)) ↭Syncback;clearcaches
V ↗ V
18: ifConverged(g(k))then
19: break %
20: endif
21: endfor
(k)
22: return evo
V
OperatorAlgebra. Reinforce++ischaracterizedbyaclippedobjectivewithanexplicitpenaltytoareferencesolution,
whileusingreflectiontotranslateRLsignalsintoconcreteedits. Wegroupthemethodintoasmallsetofcoreoperators:
• Sample(⇁ rpp). ⇁ rpp :(A, evo ,x,f) samplesarolloutunderthecurrentresourcesandyieldsanexecutiontrace
V ↑Z
containingtheproducedanswer.
• Reward (↽ rpp). ↽ rpp : (y(t),y(t ↔ 1),y ↓ ,y sft ) (r(t),A(t),J(t),ϱ(t)) computes the RLsignal tuple from the current
↑
solutiony(t). Herer(t)isataskrewardcomparingy(t)withy ,andϱ(t)isaratiosurrogatedefinedbyatextsimilarity
↓
ϑ(, )asϱ(t) ↬ϑ(y(t
↔
1),y(t)). Wedefineapenaltytoareferencesolutiony
sft
aspen(t) ↬β logmax(ϑ(y
sft
,y(t)),▷
0
)
· ·
andsetA(t) ↬r(t)
↘
pen(t). TheclippedReinforce++objectiveis
& &
& &
J(t) ↬min ϱ(t)A(t), ϱ¯(t)A(t) , ϱ¯(t) ↬clip(ϱ(t),1 ▷,1+▷).
↘
• Reflection (ϱ rpp). ϱ rpp : ( , train ,r’(t),A(t),J(t),ϱ(t))( produces an edit oriented diagnosis that is explicitly
Z V ↑H
conditionedontheRLmetricsandtheexecutiontrace.
• Improve(↼ rpp). ↼ rpp :(
V
,
H
) ↑Ve↑vo appliesRLinformededitstoeither(i)thetrainableresources
V
train suchasprompts
andtools,or(ii)thesolutionvariableitselfwhensolutionrefinementisenabled,yieldingacandidatestate.
• Commit(⇀ rpp). ⇀ rpp : Ve↑vo
↑V
evo appliesacceptedupdatesbacktoRSPLresources,completingthestatetransition.
TheEvolutionaryLoop. Algorithm4summarizestheReinforce++loopinaphasedform. Eachiteration(i)computes
Reinforce++signalsviatheclippedobjectiveandthepenaltytothereferencesolution,(ii)improvestrainableresources
throughRLconditionedreflectionandedits,(iii)optionallyimprovesthesolutiontext,and(iv)appliesanearlystopping
evaluation.
C.2.7.GRPOOPTIMIZER
Evolvable Variables. GRPO optimizes a trainable subset of RSPL resources, focusing on prompt variables and tool
implementations(nativescripts,MCPtools(Anthropic,2025a),andagentskills(Anthropic,2025b)),andoptionallyrefining
theproducedsolutiontext. SimilartoReinforce++,ourimplementationfollowsatwostagestructure: (i)updatetrainable
22

Autogenesis:ASelf-EvolvingAgentProtocol
Algorithm4Reinforce++OptimizationLoop
Input: AgenticSystemA,taskx,groundtruthy ↓ ,referencesolutiony sft ,BudgetT
Output: Finalsolutiony(t)andupdatedtrainableresources
train
V
1: //Initialization
2: e ( v 0 o ) VariableLifting(A) ↭Lifttrainableresources
V ↗
3: (0) ⇁ rpp (A, e ( v 0 o ),x,f) ↭Sampleonce
Z ↗ V
4: Extractsolutiony(0)from (0)
Z
5: y( ↔ 1) y(0) ↭Initializeprevioussolution
↗
6: fort=0,1,...,T 1do
↘
7: //Phase1: Reinforce++rewardandobjective
8: (r(t),A(t),J(t),ϱ(t)) ↽ rpp (y(t),y(t ↔ 1),y ↓ ,y sft ) ↭Reward,penalty,clippedobjective
↗
9: //Phase2: Improvetrainableresources(promptandtool)
10: Vt ( r t a ) in ↗ GetTrainables( V e ( v t o ))
11: Ht ( r t a ) in ↗ ϱ rpp ( Z (t), Vt ( r t a ) in ,r(t),A(t),J(t),ϱ(t)) ↭ReflectionconditionedonRLsignals
12: Vt ( r t a + in 1) ↗ ↼ rpp ( Vt ( r t a ) in , Ht ( r t a ) in ) ↭Applyeditstotrainables(candidate)
13: Vt ( r t a + in 1) ↗ ⇀ rpp ( Vt ( r t a + in 1)) ↭Commitupdates
%
14: //Phase3: Rerununderupdatedresources
15: Z (t+1) ↗ ⇁ rpp (%A, V e ( v t o ) ↓Vt ( r t a + in 1),x,f)
16: Extractsolutiony(t+1)from (t+1)
Z
17: //Phase4: Optionalsolutionrefinement
18: Hs ( o t l ) ↗ ϱ rpp ( Z (t+1), { y(t+1) } ,r(t),A(t),J(t),ϱ(t)) ↭Reflectonsolutionquality
19: y(t+1) ↗ ↼ rpp (y(t+1), Hs ( o t l )) ↭Editsolutiontext(candidate)
20: y(t+1) ⇀ rpp (y(t+1)) ↭Commitsolutionupdate
↗
21: /%/Phase5: Earlystopping
22: ifSatisfied( (t+ % 1))then
Z
23: break
24: endif
25: y(t) y(t+1) ↭Advancecurrentsolution
↗
26: endfor
27: returny(t)
variablesthatgovernbehavior(e.g.,promptsandtools),and(ii)updatethesolutionitselfwhenenabled.
OperatorAlgebra. GRPOischaracterizedbysamplingmultiplecandidatesolutionsperstepandusinggroupnormalized
advantageswithaclippedobjective. Weformalizethemethodwiththefollowingcoreoperators:
• Sample (⇁ grpo). ⇁ grpo : (A, V evo ,x,f,K) ↑ {Z i } K i=1 samples K independent rollouts under the current resources,
yieldingK executiontraceseachcontainingacandidatesolutiony .
i
• Reward (↽ grpo). ↽ grpo : ( { y i } K i=1 ,y ↓ ,y(t ↔ 1)) ↑ ( { r i } K i=1 , { A i } K i=1 , { J i } K i=1 , { ϱ i } K i=1 ) computes RL signals for all
K candidates. For each candidate y , we compute a task reward r comparing y with y , a policy ratio surrogate
i i i ↓
ϱ
i
↬ϑ(y(t
↔
1),y
i
)usingtextsimilarityϑ(, ),andagroupnormalizedadvantageA
i
bynormalizingrewardsacrossthe
· ·
candidateset: A = (r r¯)/φ wherer¯andφ arethemeanandstandarddeviationof r K . TheGRPOclipped
i i ↘ r r { i }i=1
objectiveforeachcandidateis
min(ϱ ,1+▷) ifA 0
i i
J i ↬min ϱ i A i , ϱ¯ i A i , ϱ¯ i ↬ ⇐ .
)max(ϱ
i
,1 ▷) ifA
i
<0
↘
’ (
• Reflection(ϱ grpo).ϱ
grpo
:(
{Z i }
K
i=1
,
V train
,
{
r
i
,A
i
,J
i
,ϱ
i }
K
i=1
)
↑H
producesaneditorienteddiagnosisthatisexplicitly
conditionedonthemultiplecandidatesolutionsandtheirRLmetrics,enablingtheoptimizertoidentifypatternsacross
candidates.
• Improve (↼ grpo). ↼ grpo : (
V
,
H
)
↑V
e↑vo applies RL informed edits to either (i) the trainable resources
V
train such as
promptsandtools,or(ii)thesolutionvariableitselfwhensolutionrefinementisenabled,yieldingacandidatestate.
23

Autogenesis:ASelf-EvolvingAgentProtocol
Algorithm5GRPOOptimizationLoop
Input: AgenticSystemA,taskx,groundtruthy ↓ ,BudgetT,numberofcandidatesK
Output: Finalsolutiony(t)andupdatedtrainableresources
train
V
1: //Initialization
2: e ( v 0 o ) VariableLifting(A) ↭Lifttrainableresources
V ↗
3: (0) ⇁ grpo (A, e ( v 0 o ),x,f,1) ↭Sampleinitialsolution
Z ↗ V
4: Extractsolutiony(0)from (0)
Z
5: y( ↔ 1) y(0) ↭Initializeprevioussolution
↗
6: fort=0,1,...,T 1do
↘
7: //Phase1: Samplemultiplecandidates
8: {Zi (t) } K i=1 ↗ ⇁ grpo (A, V e ( v t o ),x,f,K) ↭SampleKrollouts
9: Extractcandidatesolutions y(t) K from (t) K
{ i }i=1 {Zi }i=1
10: //Phase2: GRPOrewardandobjective
11: ( { r i (t) } K i=1 , { A( i t) } K i=1 , { J i (t) } K i=1 , { ϱ( i t) } K i=1 ) ↗ ↽ grpo ( { y i (t) } K i=1 ,y ↓ ,y(t ↔ 1)) ↭Groupnormalizedadvantages,clippedobjectives
12: //Phase3: Improvetrainableresources(promptandtool)
13: Vt ( r t a ) in ↗ GetTrainables( V e ( v t o ))
14: Ht ( r t a ) in ↗ ϱ grpo ( {Zi (t) } K i=1 , Vt ( r t a ) in , { r i (t),A( i t),J i (t),ϱ( i t) } K i=1 ) ↭ReflectionconditionedonmulticandidateRLsignals
15: Vt ( r t a + in 1) ↗ ↼ grpo ( Vt ( r t a ) in , Ht ( r t a ) in ) ↭Applyeditstotrainables(candidate)
16: Vt ( r t a + in 1) ↗ ⇀ grpo ( Vt ( r t a + in 1)) ↭Commitupdates
%
17: //Phase4: Rerununderupdatedresources
18: Z (t+1) ↗ ⇁ grpo (%A, V e ( v t o ) ↓Vt ( r t a + in 1),x,f,1)
19: Extractsolutiony(t+1)from (t+1)
Z
20: //Phase5: Optionalsolutionrefinement
21: Hs ( o t l ) ↗ ϱ grpo ( {Zi (t) } K i=1 , { y(t+1) } , { r i (t),A( i t),J i (t),ϱ( i t) } K i=1 ) ↭Reflectonsolutionqualityusingmulticandidatecontext
22: y(t+1) ↗ ↼ grpo (y(t+1), Hs ( o t l )) ↭Editsolutiontext(candidate)
23: y(t+1) ⇀ grpo (y(t+1)) ↭Commitsolutionupdate
↗
24: /%/Phase6: Earlystopping
25: ifSatisfied( (t+ % 1))then
Z
26: break
27: endif
28: y(t) y(t+1) ↭Advancecurrentsolution
↗
29: endfor
30: returny(t)
• Commit(⇀ grpo). ⇀ grpo : Ve↑vo
↑V
evo appliesacceptedupdatesbacktoRSPLresources,completingthestatetransition.
TheEvolutionaryLoop. Algorithm5summarizestheGRPOloopinaphasedform. Eachiteration(i)samplesK candidate
solutions,(ii)computesGRPOsignalsviagroupnormalizedadvantagesandclippedobjectives,(iii)improvestrainable
resourcesthroughmulticandidateconditionedreflectionandedits,(iv)optionallyimprovesthesolutiontext,and(v)applies
anearlystoppingevaluation.
24
