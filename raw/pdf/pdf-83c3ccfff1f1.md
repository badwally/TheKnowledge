---
id: pdf-83c3ccfff1f1
type: pdf
title: 'Agentic AI: Autonomous Intelligence for Complex Goals&#x2014;A Comprehensive
  Survey'
url: ''
authors: []
ingested_at: '2026-04-29T16:16:14Z'
content_hash: sha256:dda99bfb7b3784d5c96e3313b637140a28d69e07ad7a35d374033c1596592868
source_path: raw/pdf/pdf-83c3ccfff1f1.pdf
domains:
- ai-and-agents
nlm_corpus_ids:
- 7eac1296-b611-422e-85bb-6c36f5c8872b
wiki_pages:
- wiki/concepts/agentic-ai.md
- wiki/concepts/autonomous-ai-systems.md
- wiki/concepts/goal-directed-ai.md
- wiki/concepts/agentic-ai-vs-traditional-ai.md
- wiki/concepts/reinforcement-learning.md
- wiki/concepts/adaptive-control-mechanisms.md
- wiki/concepts/agentic-ai-applications.md
- wiki/concepts/agentic-ai-ethical-challenges.md
- wiki/entities/deepak-bhaskaracharya.md
- wiki/entities/karthigeyan-kuppan.md
- wiki/entities/b-divya.md
meta:
  page_count: 25
  extraction_tool: pdfplumber
  pdf_metadata_subject: IEEE Access;2025;13; ;10.1109/ACCESS.2025.3532853
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__83c3ccff.pdf
published_at: '2025'
---
Received1January2025,accepted19January2025,dateofpublication22January2025,dateofcurrentversion29January2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3532853
Agentic AI: Autonomous Intelligence for Complex
Goals—A Comprehensive Survey
DEEPAKBHASKARACHARYA 1,(SeniorMember,IEEE),
KARTHIGEYANKUPPAN 2,(SeniorMember,IEEE),ANDB.DIVYA 3
1DepartmentofComputerScience,TheUniversityofAlabamainHuntsville,Huntsville,AL35806,USA
2JPMorganChase,Houston,TX77082,USA
3DepartmentofElectronicsandCommunicationEngineering,ManipalInstituteofTechnology,ManipalAcademyofHigherEducation,
Manipal,Karnataka576104,India
Correspondingauthor:B.Divya(divya.ashwin@manipal.edu)
ABSTRACT Agentic AI, an emerging paradigm in artificial intelligence, refers to autonomous systems
designedtopursuecomplexgoalswithminimalhumanintervention.UnliketraditionalAI,whichdependson
structuredinstructionsandcloseoversight,AgenticAIdemonstratesadaptability,advanceddecision-making
capabilitiesandself-sufficiency,enablingittooperatedynamicallyinevolvingenvironments.Thissurvey
thoroughly explores the foundational concepts, unique characteristics, and core methodologies driving
the development of Agentic AI. We examine its current and potential applications across various fields,
including healthcare, finance, and adaptive software systems, emphasizing the advantages of deploying
agenticsystemsinreal-worldscenarios.ThepaperalsoaddressestheethicalchallengesposedbyAgentic
AI,proposingsolutionsforgoalalignment,resourceconstraints,andenvironmentaladaptability.Weoutline
a framework for safely and effectively integrating Agentic AI into society, highlighting the need for
further research on ethical considerations to ensure beneficial societal impacts. This survey serves as a
comprehensiveintroductiontoAgenticAI,guidingresearchers,developers,andpolicymakersinengaging
withitstransformativepotentialresponsiblyandcreatively.
INDEX TERMS Agentic AI, autonomous systems, human-AI collaboration, adaptability, governance
frameworks,ethicalAI.
I. INTRODUCTION i.e., goal-directed, even in situations where there are drastic
A. MOTIVATIONANDBACKGROUND changesandmultiplesuchgoalstotogglebetween.
AgenticAIsconstituteaqualitativeleapinthedevelopment OneofthefactorsthatmotivatedthedesignofAgenticAIs
of artificial intelligence, defined by their capability to set isthenecessityfortoolsdesignedtobeabletooperateinbet-
complex goals in a changing and uncontrolled situation teryetcomplexreal-worldconditionswithsignificantroom
and to pursue them through autonomously managing their forflexibility.Forexample,indisasterrelief,healthcare,and
resources.MostAIsystems,however,werebuiltandoperated cyber security, where proper decisions are needed and the
as tools under supervision with restrictions and definitions chaosisconsiderable,theabilitytocontrolasituationinde-
provided.Thesesystemsaregoodatdoingwell-definedtasks pendently is critical. Agentic AIs don’t just assist in human
withincertainboundariesbutprominentlyfailwheneverthe action; they enhance it while taking on tasks that demand
attempted tasks have no end-state or specific parameters to highinvolvementandmulti-taskingwithoutconstanthuman
manipulate.WhereasAgenticAIscanbelow-leveloperative, intervention. Such a paradigm shift promises to expand the
targetareaofAIfrombeingpassiveandreactivetofocusing
onstrategicplanning,informationprocessing,andproblem-
The associate editor coordinating the review of this manuscript and solving, enabling a new era once the rights conditions
approvingitforpublicationwasFilbertJuwono . aremet.
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
18912 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TheimpactofAgenticAI[1],[2],[3]onsocietyislikelyto Asystematicreviewofthemainelementsthatcomprise
•
beconsiderable.AsAIbecomesembeddedinmoreandmore Agentic AI systems with an emphasis on how these
core systems and industries, agentic AI systems would be systemsdifferfromothercommonsenseandgenerative
abletoworksidebysidewithhumansandtakeontasksthat AIsystems.
canreallocatehumaneffort,increaseproductivity,andengage Acomprehensivestudyofthetechniquesandconcepts
•
in situations where human presence may be undesirable or usedinconstructingandassessingAgenticAI,including
dangerous. This change could transform job structures in the architectures, learning approaches, and training
sectors,allowingforworkinginconcertwhereAIsperform methods.
operational tasks and people deal with more complex and The current and potential uses in different areas,
•
strategicroles. including practical examples of the effectiveness of
AgenticAIapplicationsinpractice.
Highlighting engineering problems but not limited to
B. DEFINITIONANDSCOPE •
these:goaldesignandconvergence,contextadaptation,
Inthissense,AgenticAIincludestheclassofautonomousAI
andlimitedresources.
systems[4]thatundertaketofinishasetofcomplextasksthat
A considers the ethical, societal, and regulatory issues
span over long periods of time without human supervision. •
with adopting Agentic AI, including relevant concerns
It learns context and makes decisions. Such systems are
ofresponsibility,equity,andtransparency.
designedtooperatewithacertainlevelofautonomy,allowing
Recommendations towards future research, advancing
them to traverse changing settings, deal with unexpected •
suggestions on how the issues of scale, context, and
situations,andoptimizeperformanceovertime.Tyingthem
ethics are best integrated into the implementation of
together are the features of autonomy and adaptiveness to
AgenticAI.
cope with task-oriented processes. Unlike classic AI [5],
Thispaper’sexpectedcontributionsaremorethansimplya
whichisrule-basedandrequiresinstructionstobeperformed,
literaturereview;rather,theyshouldofferausefulandwell-
and generative AI, which patterns and generates an image,
organized background to develop the issues and particulars
AgenticAIfeaturesthebestofbothworlds.
ofAgenticAI.Thispaperaimstoprovideimportantinsights
It is valuable to place agentic AI alongside current AI
into managing operational practices and technological solu-
paradigmstoputitsboundariesintoperspective.Forexample,
tions that promote and sustain the development of ethical
classical AI was never focused on image recognition or
agenticAIsystems.
languagetranslations[6],[7]butinsteadaimedatachieving
verynarrowgoals.
D. PAPERORGANIZATION
The first is how Generative AI [8] works. In reverse
Theremainderofthispaperisorganizedasfollows
operations,itcombinespiecesofinformationlearnedthrough :
SectionIIIntroducesthebasicconceptsanddefinitions
numbers and creates content, such as words or images. •
that help understand Agentic AI as a specific entity in
On the other hand, Agentic AI surpasses the former two
thebroadercontextofartificialintelligence.
approaches with goal-oriented, input-formed, and adaptable
Section III Deals with the typical structure of Agentic
characteristicsthatallowittoaccomplishintricateandmulti- •
AI, including independence, flexibility, and the ability
layeredtasksinaperiodwithoutneedingasetofinstructions
tochoosewhattodo.
eachtime.
SectionIVIdentifiesanddescribesmethodsofAgentic
At this point of the survey, the focus is on why someone •
AIconstruction–thestructuraldesigns,typesoflearn-
should be interested in Agentic AI. From its structural
ing,andformsofassessmentandefficiencymeasures.
and operational characteristics, why is it based on goals,
SectionVDiscussesdifferentsectorswhereagenticAI
and how can that advanced type of AI be applied in •
hasfoundapplicationsconcentratingonapplicationsin
various fields where its application is unique? In addition,
industriesandcasesofjointworkwithhumans.
this article also looks into the various practical and moral
Section VI Presents a comparative analysis of various
issues that arise from using systems based on such AI and •
systems that exemplify Agentic AI with a focus on
discussesapproachesthatdealwithsafety,transparency,and
the different performance measures and indicators
accountability.TheprovideddefinitionofAgenticAIallows
employedinevaluatingthesesystems.
the authors of this survey to discuss precisely what features
SectionVIIExplainsthetechnicalaspectsanddifficul-
ofthistypeofAIsystemdistinguishitfromothersandaidin •
tiesofAgenticAIaboutaimssettingandinteractionwith
itseffectiveandintegratedanalysis.
theenvironmentaspects.
SectionVIIIRaisesthesocial,ethical,andgovernance
•
C. OBJECTIVESANDCONTRIBUTIONS issues, as concerns responsibility, equity, and compli-
Thissurveypaperaimstoprovideanextensivecollectionof ancewiththelaw.
AgenticAIknowledgeandsetitsboundariesforeasierunder- SectionIXLooksatexistingsystemsthatfacilitatethe
•
standingbyawideraudienceofresearchers,developers,and constructiveandresponsibleimplementationofAgentic
policy-makers.Keycontributionsofthissurveyinclude: AI,includingoversightandregulationcomponents.
VOLUME13,2025 18913

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
SectionXDescribesgapsinknowledgeandprospected learningapproachesonreallybigdatasetswherebehavioris
•
ResearchandDevelopmentworkalongsidetheconsid- determined by the input and instructions given to them by
erationofrefreshingAgenticAIideas. people. Thus, traditional AIs are best applied in controlled
Section XI recommends the paper’s final remarks, environmentswithlimitedabilitytomicromanagesituations
•
includingaconclusionofthefindingsandaremarkthat andrathermoresignificantoutcomes.
cross-disciplinary connections are needed to move the On the other hand, Agentic AI systems can be described
fieldforwardinaresponsiblemanner. as possessing the characteristic of open-endedness where
This comprehensive survey will provide valuable insights there is no prescription of how the task should be achieved.
into Agentic AI’s current state, future potential, and the They work with and adapt to rapidly changing conditions.
challenges that must be addressed to ensure its safe and On the other hand, while conventional AI systems might
effectivedeployment. be accurate, they do not have the situational awareness
and goal-directed dynamics inherent in Agentic AI. A case
II. FOUNDATIONALCONCEPTSANDDEFINITIONS examplemayincludeafactory’sAImodelthatisdeveloped
A. AGENTICAIANDITSROLEINTHEAIECOSYSTEM topredictequipmentfailure.Asmuchasthepremiseisgood,
Within the AI field, Agentic AI serves as a different form AIwillnotincorporateadaptiveshiftsinthewayitpredicts
ofintelligencethatcantakemoreautonomouslyfunctioning failuresduetofactorssuchaschangesinthemanufacturing
agenticbehaviorsthatarenotlimitedtoperformingspecific scheduleorchangesinwearpatternsacrossmachines.Onthe
tasks or following content-generating algorithms. When other hand, Agentic AI could change its metrics estimation
viewed in an ecosystem context, Agentic AI stands out processes depending on the context and adapt both its short
because of its purpose, flexibility, and behavior, which andlong-termstrategies,whichisimpossiblewithtraditional
enables such AIs to operate almost independently. Rather models.
than following strict guidelines like other robotic AIs, As shown in Table 1, Agentic AI systems not only adapt
Agentic AI systems are promoted to have rationalism in based on real-time context but also maintain the flexibility
them, which enables each system [9] to reason and adapt tooptimizeforcomplex,long-termgoals.Thesedistinctions
todifferentscenariosandsuchcircumstancesinasufficient illustrateAgenticAI’svalueinscenarioswhereconventional,
waytoaccomplishgoals.Duetoitstendenciestoenhanceits rule-bound AI falls short, emphasizing its transformative
functions to prepare for any obstacles, Agentic AI has been roleinaddressingthedemandsofunpredictable,high-stakes
seen as a potential point of anchor for tasks and goals that environments.
requirehighlevelsofinteractions,forexample,autonomous
devices,collaborativerobots,andinteractivedecisionsupport C. EXPANDEDCOMPARISONWITHCLASSICALAGENTS
systemsintheareasoffinanceandhealthcare. While classical AI systems are primarily rule-based or
The increasing demand for systems capable of supervised-learning models designed for specific tasks,
autonomously handling intricate and dynamic processes Agentic AI integrates autonomy and adaptability, enabling
has led to growing interest in Agentic AI, particularly in broader functionality. The differences between these
sectors with a scope for AI automation. Though built on paradigmsarebestillustratedwithexamples.
basic AI principles, Agentic AI increases the scope of AI
achievement by adding the elements of dependence and 1) CLASSICALAGENTS
adaptiveindependentaction.TheecosystemofAIoccupiesa Theseagentsexcelincontrolledenvironments.Forexample,
space between purely reactive and narrowly rule-based AI rule-based financial trading algorithms function effectively
technologies and broader ideas about AGI, performing an when predefined parameters remain constant. However,
essential function of enabling autonomous decision-making they struggle with volatile market changes or unpredictable
withindefinedboundariesorstructures.Thisuniqueposition disruptions.
accentuates the ability of Agentic AI to fit in scenarios
where the ability to make rapid decisions, manage over- 2) AGENTICAI
timeobjectives,andlearnonthegoarefundamentalstothe Incontrast,AgenticAI-poweredtradingsystemsdynamically
problemathand. adjuststrategiesbasedonreal-timedata,historicaltrends,and
unexpected market shifts, making them more resilient and
B. COMPARISONWITHTRADITIONALAI adaptive.
AI, which can be described as ‘Agentic’ has its core
differences when compared to the other advanced types 3) REINFORCEMENTLEARNINGVERSUS
of AIs in terms of autonomy, function, and scope, among LANGUAGE-MODEL-BASEDAGENTS
others. Such AI systems are integrated into specific tasks Whilereinforcementlearningfocusesonoptimizingcumula-
like image analysis [10], translation of languages [11], and tiverewardsinaspecifictaskenvironment,language-model-
recommendationengines[12],makingthemabletoperform based agents extend this by interpreting complex natural
designatedtasksinahighlyfocusedbutcharacteristicnarrow language inputs and interacting with humans seamlessly.
manner and scope. They are mostly based on supervised For example, an RL agent excels at optimizing gameplay
18914 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE1. ComparisonoftraditionalAIandagenticAI.
TABLE2. Comparisonofclassicalagents,reinforcementlearningagents,andagenticAI.
strategies, whereas a language-model-based agent can gen- where agents learn to adapt based on prior experiences,
erate dialogue, interpret rules, and adapt strategies during a enable greater resilience and flexibility. As shown in the
livegame.Table2highlightsthekeydifferences. flowchart, adaptive control mechanisms provide ‘‘Environ-
mental adaptation,’’ allowing agents to maintain optimal
D. TECHNICALFOUNDATIONS performanceevenunderchangingconditions.
The development of Agentic AI systems relies on core Figure 1 provides a visual representation of these
algorithmsandframeworksthatenablegoal-directedbehav- core frameworks, illustrating how they interact to enable
ior,contextualadaptation,andautonomousdecision-making. autonomous,adaptable,andgoal-drivenbehaviorinAgentic
These technical foundations incorporate advances in rein- AI systems. Together, these technical foundations equip
forcementlearning,goal-orientedarchitectures,andadaptive Agentic AI with the structural and functional capabilities
controlmechanisms. necessarytomanagecomplex,evolvingtasksindependently,
Reinforcement Learning (RL) [13] is central to many settingitapartfromtraditionalAIsystemsthatrelyonrigidly
agentic systems, as it equips AI models with the ability definedparametersandinstructions.
to learn through trial and error. In RL, agents are trained Bycombiningreinforcementlearning,goal-orientedarchi-
to maximize cumulative rewards by interacting with an tectures, and adaptive control, Agentic AI systems achieve
environment,adaptingtheiractionstoachievespecificgoals a level of autonomy and resilience that allows them to
over time. This learning paradigm is particularly useful operate effectively in diverse environments. This section
for Agentic AI because it enables systems to continuously establishesthetechnicalbasisforunderstandingtheadvanced
refine their strategies based on feedback. As illustrated capabilities of Agentic AI, providing a foundation for the
in Figure 1, reinforcement learning supports ‘‘Learning methodologies and applications discussed in the following
throughinteraction’’andinvolvesatrial-and-errorapproach sections.
tooptimizedecisionsovertime.
Goal-Oriented Architectures [14] provide a structural III. CORECHARACTERISTICSOFAGENTICAI
frameworkformanagingcomplexobjectiveswithinAgentic A. AUTONOMYANDGOALCOMPLEXITY
AI systems. Unlike traditional architectures, which often Autonomy is one of the most sought-after qualities that
focus on single tasks, goal-oriented architectures enable Agentic AI can possess. This is especially needed where
agents to prioritize and pursue multiple objectives simul- complex multi-goal scenarios are involved. Most tradi-
taneously. These architectures support a modular structure, tional AI systems focus on completing one task and
where larger goals are broken into manageable sub-goals. are programmed with non-complicated input and output
In the context of Figure 1, goal-oriented architectures requirementstoachievethatsinglegoal.Incontrast,systems
facilitate ‘‘Managing complex objectives,’’ allowing agents powered by agentic AI can move through multiple needed
toapproachtasksinstructuredsteps. tasks and shift from one basic one to multiple complex
AdaptiveControlMechanisms[15]ensurethatAgentic end goals. Such systems come with a certain amount of
AI systems can adjust to changing environments. By incor- self-governance where continual supervision of a human
poratingadaptivecontrol,agentsrecalibratetheirparameters being is not mandatory, though at times preferred, and
in response to external variations, such as data shifts AI agents function independently upon a predetermined or
or unexpected disruptions. Techniques like meta-learning, evolvinggoalstructure.Oneextrastepdoes,however,require
VOLUME13,2025 18915

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
FIGURE1. TechnicalfoundationsofagenticAI,illustratingkeycomponents:ReinforcementLearning,Goal-Orientedarchitectures,andadaptivecontrol
mechanisms.
acknowledgment; for Agentic AI, Autonomy is not just of other drivers would be before deciding how to act in a
limited to the completion of a single aim–instead, lesser particularsituationwhentheneedariseswithinaveryshort
goals,aswellasindividualstrategies,aresubstitutedtomeet period.
larger goals that are long-term in nature. An example can To do this, Agentic AI systems, as a general rule, are
be drawn from autonomous robotics [16], where such an equipped with means for environmental interaction, on-the-
agentic system would demand the complete traversal from spotdataprocessing,andsituationalcontextcomprehension.
pointAtopointB,withtheadditionalallowanceofmaking These capabilities allow the system to keep track of and
diversionsaroundtheroute,movingconstraintssuchastask actively participate in the operational parameters that are
hierarchy,timeframes,energyexpendableratios,andsafety prone to alterations even at the last minute. For instance,
standards.Suchanunderstandingdeepensthecomprehension change control [18] in Agentic AI systems is typically
of goal complexity, where high-order decision models are embedded within the Agent as reinforcement learning or
used wherein goals guide analysis, planning, and action. adaptive algorithms so that the Agent can work optimally
Quite clearly, then, as this enables Agentic AI systems to regardless of the changing conditions. These characteristic
carry out intricate objectives that had been deconstructed features make Agentic AI fit for use in environments with
intosub-tasksthatcouldfitautonomouslyintoanoperational many dynamics where reactions must be rapid, such as in
strategycoupledwithadjustments. Disastermanagement,healthcare,finance,etc.
B. ENVIRONMENTALANDOPERATIONALCOMPLEXITY C. INDEPENDENTDECISION-MAKINGANDADAPTABILITY
Moreover,AgenticAI’scapacitytooperatewithinvariedand Autonomy and flexibility are core requirements for the
changing circumstances is yet another characteristic of this AgenticAItoworkindependentlyforlonghours.Incontrast
AI. Unlike past AI, built for the mostoptimum functions in to rule-based systems, which merely do what they are told,
a constant and easily predictable environment [17], Agentic Agentic AI has to situate itself in its current context and
AIs integrate all the variability in the real world. This make decisions as it is working, so it has to learn over time
involvesadjustingquicklytoenvironmentalconditions,data and improve on its behavior. This type of decision-making
orpatternchanges,andeventime-wornornewlyconstituted is commonly done through reinforcement learning or meta-
userdemands.InthecaseofAIagentsforself-drivingcars, learning when the AI agent gets feedback repeatedly and
theidealAgentDidnotPhotoshoptocomplywithartificial improvesitsbehavior.
boundaries contained in traffic laws alone but would learn Flexibility allows Agentic AI to act differently in the
new road designs and try to understand how the behavior same scenario and pursue the relevant goals. For instance,
18916 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
in a customer service situation, an agentic AI could change execute them. This approach is effective for managing
its communication strategies to those that work best with taskswithmultiplelevelsofcomplexity.
customers’ moods to achieve customer satisfaction. This Goal-Oriented Modular Architectures: These archi-
•
requiresprioritizinggoalsandassessingpossiblecoursesof tectures [22] organize agent functions into modular
actionandtheiroutcomeswithrespecttothesystem’sgoals. components,whereeachmodulespecializesinspecific
Becauseofflexibilityandautonomyindecision-making[19], aspectsof thetask.Such modularityenablesflexibility
AgenticAIcanreconceptualizeitsstrategiesandadapttonew and scalability, allowing the agent to handle different
information adopted in the model to operate in a changing tasksbyreconfiguringmodulesasneeded.
environment.
To further illustrate the integration process of Agentic B. LEARNINGPARADIGMS
AI into society, Figure 2 outlines the key stages. This AgenticAIreliesonseverallearningparadigms,eachsuited
includesdatacollectionandpreprocessing,thecoreAgentic to different types of tasks and goals. The main paradigms
AIsystem’sfunctionality,anditsdeploymentacrossvarious used in agentic systems are supervised, unsupervised, and
industries such as healthcare, finance, manufacturing, and reinforcementlearning.Table4providesacomparison.
customer support. The flowchart visually represents the
adaptability and independence of Agentic AI in dynamic C. ADVANCEMENTSINMETHODOLOGIES
environments. Recent advancements in Agentic AI methodologies have
focusedonkeycapabilitiesessentialtomodernagentdesign.
D. COMPARATIVEANALYSIS These include reasoning and planning, tool use, memory
Comparedtolinearsystemsofregulation,AgenticAIstands mechanisms, Retrieval-Augmented Generation (RAG), and
out because of its improved ability to remain autonomous, instructionfine-tuning[23].
function within an ever-changing context, and cope with
multiple goals. In most cases, operative agents are created 1) REASONINGANDPLANNING
where the functional area is characterized within rigid These frameworks enable agents to anticipate outcomes,
boundaries,withunfailingandstraightforwardpreconditions prioritize tasks, and adapt strategies dynamically. They
for successful performance. On the other hand, Agentic AI are critical for managing complex, multi-objective tasks
systemsaredesignedtoworkoncomplexgoalsthathaveyet in evolving environments like disaster management and
tobestructuredandcanbedefinedinabroadcontext. autonomousnavigation.
AsshowninTable3,traditionalagentsexcelinstructured
tasks but lack the flexibility required for adaptive, goal- 2) TOOLUSEANDINTEGRATION
orientedtasksincomplexenvironments.AgenticAIadvances Agents equipped with the ability to interact with external
these systems by introducing a high degree of autonomy tools and APIs can perform computations, retrieve real-
and adaptability, enabling the agent to interact with and time data, and simulate scenarios, significantly enhancing
respond to its environment in ways that extend beyond decision-makingprocesses.
simple rule-following. This comparative analysis highlights
thedistinctivecapabilitiesofAgenticAI,positioningitasa 3) MEMORYMECHANISMS
transformative approach in fields where independent, goal- Episodic and semantic memory models allow Agentic AI
driven,andcontext-awarebehaviorisessential. systems to retain contextual information, improving their
abilitytorecallpastinteractionsandoptimizeongoingtasks.
IV. METHODOLOGIESINAGENTICAIDEVELOPMENT
A. ARCHITECTURALAPPROACHES 4) RETRIEVAL-AUGMENTEDGENERATION(RAG)
Architectural approaches in Agentic AI typically involve RAG empowers agents to retrieve external knowledge
modular and hierarchical designs that enable the system to dynamically, enhancing the relevance and context of their
managecomplexgoalsandadapttodynamicenvironments. outputs.Thiscapabilityisparticularlysignificantinconver-
Common architectures include multi-agent systems (MAS), sationalagentsandreal-timedecision-makingsystems.
hierarchicalreinforcementlearning(HRL),andgoal-oriented
modulararchitectures. 5) INSTRUCTIONFINE-TUNING
Multi-AgentSystems(MAS):MAS[20]dividestasks This process ensures that agents understand and execute
•
among multiple autonomous agents that collaborate or nuanceddirectives,enablingthemtoperformmulti-steptasks
competetoachieveacommongoal.Thisarchitectureis withhighprecisionandadaptability.
particularlyusefulinscenarioswherecomplexgoalscan
bedecomposedintosmallertasksthatindividualagents D. TRAININGANDEVALUATIONTECHNIQUES
canhandle. Training Agentic AI systems requires techniques that allow
Hierarchical Reinforcement Learning (HRL): HRL agentstolearnfrominteractionswithcomplexenvironments.
•
[21] structures decision-making hierarchically, where Commontrainingtechniquesincludesimulation-basedtrain-
high-levelagentsdefinesub-goals,andlow-levelagents ing,curriculumlearning,andmulti-tasklearning.
VOLUME13,2025 18917

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
FIGURE2. IntegrationprocessofagenticAIintosociety.
TABLE3. ComparisonoftraditionalagentsandagenticAI.
TABLE4. ComparisonoflearningparadigmsforagenticAI.
Simulation-BasedTraining:Simulationsgivestudents E. TOOLSANDFRAMEWORKS
•
asafecontexttoinvestigatenumeroussituationswithout Developing Agentic AI requires specialized tools and
real-world consequences [24]. This is very effective in frameworks that support reinforcement learning, simula-
reinforcementlearning[25]asitallowsagentstodesign tion, and multi-agent system development. Tools such
policiesthataretransferabletotherealtask. as OpenAI Gym, Unity ML-Agents, TensorFlow Agents,
Curriculum Learning: Structure tasks in increasing and Rasa offer platforms for developing, training, and
•
orderofcomplexitysothatanagentdevelopsbasicskills evaluating Agentic AI systems across various applications.
thatcanbebuiltuponinnew,morecomplextasks[26]. Each tool provides unique capabilities, from reinforcement
Suchastructureofprogressivelymorecomplextasksis learning environments to multi-agent simulations, enabling
fundamentalinamulti-goal-orientedenvironment. researchers and developers to experiment with different
Multi-Task Learning: In multi-task learning [27], architectures and training techniques. Figure 3 overviews
•
agents acquire the capabilities to perform several tasks populartoolsandframeworksofthedifferentmethodologies
at once, which expands their generalization abilities of Agentic AI Development Methodologies, which are
over multiple goals, tasks, and scenarios. The problem employed in the development and enhancement of such
is of utmost interest in designing agentic AI systems autonomous AI systems that can work towards achieving
that are supposed to tackle multiple objectives in somehigher-ordergoals.Theapproachesarefurthersimpli-
parallel. fiedintofourcategories:
EvaluationtechniquesforAgenticAIoftenincludemetrics 1) ArchitecturalApproaches:Thisbranchdealswiththe
such as task success rate, adaptability, resource efficiency, different architectures that autonomous agents use to
and long-term goal achievement. Table 5 provides an accomplishtheiraims.AmongkeymethodsareMulti-
overviewofthesetrainingandevaluationtechniques. Agent Systems, which consist of agents working in
18918 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE5. TrainingandevaluationtechniquesforagenticAI.
collaboration and competition with others; Hierarchi- for understanding the core techniques driving Agentic AI
calReinforcementLearning,whichfocusesondividing development.
tasksintoahierarchytohelpwiththelearningprocess;
andGoal-OrientedModularArchitectureswhichentail V. APPLICATIONSOFAGENTICAI
theconfigurationofthesystembasedongoalormodule A. INDUSTRIALAPPLICATIONS
specification. AgenticAIcanpotentiallyrevolutionizemultipleindustries,
2) LearningParadigms:Thispartemphasizestherelated includinghealthcare,finance,education,andmanufacturing.
study of autonomous agents derived from different In healthcare, for example, Agentic AI can be used to
machinelearningsources.TheseconsistofSupervised analyze incoming patient data, identify abnormal patterns,
Learning, which is based on the use of labeled and alert corresponding medical personnel to damage. AI-
data; Unsupervised Learning, in which the model based devices could, for example, prevent the delay of
seeks relations in unlabeled data; and Reinforce- vitaldiagnosesbymonitoringpatients’keyhealthindicators
ment Learning, which is trial and error, wherein and notifying them when the situation worsens. In finance,
the agent is being trained to carry out temporal for instance, Agentic AI algorithms can assist in making
decision-making. investment transactions, detecting fraudulent activities, and
3) TechniquesofTrainingandEvaluation:Inthiscase, providing tailored investment solutions. They are capable
the focus is on methods that are designed for the of evaluating the situation on the exchange, independently
training and performance assessment of agentic AI. makingdecisionsregardingthepurchaseorsaleofsecurities,
Techniques include Simulation-Based Training which and adjusting their strategies to changing conditions in
allows for controlled environments to train a number real time, which significantly improves the quality of
of agents, Curriculum Learning in which agents can managerial performance and reduces the participation of
perform a series of simple tasks and more difficult humanbeings[1].
onesafterward;andMulti-TaskLearningwhichallows In education, intelligent tutoring systems utilizing Agen-
agentstocarryoutmultipletasksatatime.Trainingor tic AI technology assist learners by tailoring educational
evaluatingagentsinthesimulatedenvironmentisdone content [31] to their needs and addressing their progress
usingOpenAIGym[28]andUnityML-Agents[29]. andrequests.Suchanapproachleadstoenhancedacademic
4) Computational Tools and Frameworks: The last performance and decreased pressure on teachers because
subsection discusses more tools or computational repetitive tasks such as grading and finding appropriate
frameworks pertinent to the building process of materialsaredoneautomatically.Inmanufacturing,Agentic
autonomous AI systems. Tools such as Reinforce- AI is applied to predictive maintenance where the state of
ment Learning (RL) algorithms can be implemented themachinesisassessed,futurebreakdownsareanticipated
usingTensorFlowAgents,PyMARL,amulti-agentRL and maintenance is carried out when necessary without the
library,andRasa[30],aframeworkforconversational involvementofpeoplesothatproductionrunssmoothlywith
agents. minimal delay. It is clear that once implemented, Agentic
Thestructuralbreakdownoutlinedintheparagraphsabove AI enables industries to operate with greater effectiveness,
portraystherangeofmethodologiesandtoolsthatcanbeused flexibility,andscalability.
tocreateagenticAIsystemsandhowtheycanalsoenhance
theadaptability,efficiency,andfunctionalityofautonomous B. HUMAN-AICOLLABORATION
systemsincomplexenvironments. Agentic AI extends the range of human productivity in
The methodologies discussed in this section encompass collaborativeandcognitivedomains[32].Insuchknowledge-
diverse applications and ethical considerations. Table 6 intensive ventures as legal or research, it can support pro-
summarizeskeymethodologiesinAgenticAI,theirpractical fessionals by automatically condensing documents, pulling
applications across domains, and the associated ethical up relevant papers, or performing professional background
challenges. This summary provides a concise reference investigationssotheuserscanconcentrateonmorecomplex
VOLUME13,2025 18919

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
FIGURE3. OverviewofAgenticAIDevelopmentMethodologies,includingArchitecturalApproaches,Learning
Paradigms,TrainingTechniques,andTools.
18920 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE6. Summaryofkeymethodologies,applications,andethicalchallenges.
aspects of the work. For example, in legal practice [33], medicine [36], where an Agentic AI system could manage
Agentic AI can examine a corpus of legal text, remember chronic patients by overseeing their patient history, sending
essential documents and help lawyers retrieve cases with medication intake reminders [37], and changing treatment
similarlaws. recommendations based on other health indicators. Such
Inthecreativeindustries,AgenticAIcandrafttext,develop systems would provide individualistic care-management
designconcepts,ormakecreativealterationsbasedonearlier protocol and even monitor for early indicators of other
editsorclientinput.AgenticAItoolsareexpectedtobeable progressing health conditions, especially for aged people
toreducesuchneedlesstasksandimprovetheproductivityof likelytorequiremaximumattention.
content development. Also, in customer services, Agent AI For literature creation, Agentic AI is expected to acquire
cantakecareofsimplequestions,offerassistance,androute new roles in generating content automatically, targeting
complicatedproblemstohumanagents,enhancingresponse wider audiences and meeting precise parameters in content
time and client satisfaction. This seamless integration of creation. For instance, in marketing, Agentic AI systems
human-AI collaboration enables workers to spend their would send customized emails and adverts based on user
time in a more strategic and creative workspace. At the activity and generate content for the adverts in the first
same time, Agentic AI takes care of the operational place.Furthermore,inthecontextofself-regulatoryresearch,
aspects. ScientistsusingAgenticAIcanaccomplishtheobjectivesof
aliteraturesearch,developingnewlinesofthought,andeven
creating research designs. Faster research periods could be
C. ADAPTIVESOFTWARESYSTEMS
witnessed in the fields of drug development [38] research
There is a gradual move towards Agentic AI in adaptive
or climate change research. Through expansion in these
or ‘‘living’’ software systems [34], which can change their
new directions, Agentic AI shows more ability to penetrate
featureswithouttypicallimitationsanddynamicallymodify
high-valuemarketsrequiringcustomized,dynamicandself-
theirfunctionalitiesdependingonenvironmentalevolvement.
servicingapplications.
Thesevariablesmakethesystemreconfigureitselfrapidlyor
Table 7 provides an overview of Agentic AI applications
automaticallytoensurethatself-learningimproveseverytime
acrossvariousdomains,illustratingthediverserangeoftasks
aroundusage.Theseincludereal-timeupdatesofsuggestions
and contexts where autonomous, goal-directed systems can
bypeopleasafunctionoftherecommendationsandupdates
enhance operations and create value. From healthcare to
ofsuggestionsbasedonchangesintheevolutionoftheuser
personalized marketing, the versatility and adaptability of
recommendationsdynamically.
AgenticAIopenpossibilitiesforinnovativesolutionsacross
Othercasesincludeautomatedactivitiesinthesmarthouse
industries.
where, because of the powered agentic AI, boarders can
change the lighting, temperatures and security protocols for
inbuilt AI to note the behavior of the users. In project E. SCENARIOSDEMONSTRATINGADAPTABILITY
development processes, for instance, Agentic AI project 1) DISASTERMANAGEMENT
management bots can focus on task sequencing, workload An Agentic AI system deployed in disaster management
distribution, and task timeline complexity to dynamically autonomouslyanalyzesreal-timeenvironmentaldataduring
altertimelines[35]wherenecessary,whichenablestheusers a flood. It reallocates resources, such as rescue teams and
to suit the various changes in the project quite effectively. medicalsupplies,toareasmostinneed,adjustingstrategies
Such adaptive software applications reduce human-in-the- dynamically based on changing weather conditions and
looprequirementsandenhancetheusabilityandfunctionality incomingdata.
ofthesystem.
2) CUSTOMERSUPPORT
D. EMERGINGAPPLICATIONAREAS In an e-commerce setting, an Agentic AI chatbot adapts
With dynamic patient needs demanding continuous respon- its tone and problem-solving strategies based on real-time
siveness, there are new targeted use cases for applying sentiment analysis of customer interactions, improving user
Agentic AI in specific spheres. Such include personalized satisfaction.
VOLUME13,2025 18921

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE7. Overviewofagenticaiapplicationsacrossdomains.
3) HEALTHCAREMONITORING such as unexpected scenarios well deepened in the
A hospital-based Agentic AI system detects patterns in healthcareandautonomousdrivingsectors.
patient vital signs, predicts potential complications, and Scalability: It refers to the system’s qualities, which
•
autonomouslynotifieshealthcareproviders,enablingtimely must not change as the range or complexity of tasks
interventionswithouthumaninput. changes. This is an important characteristic in indus-
These scenarios highlight the dynamic and goal-directed tries with significant volumes of data or operational
capabilitiesofAgenticAIinreal-worldapplications. processes,suchasthecasewithfinanceormanufactur-
ing[44].
UserSatisfactionandHuman-AICollaborationEffi-
VI. COMPARATIVEANALYSISOFAGENTICAI •
ciency: User satisfaction with Agentic AI systems
IMPLEMENTATIONS
dependent on human interaction [45], [46] is a key
A. COMPARISONMETRICS
performance indicator. This metric examines how lan-
To comprehensively assess and triangulate Agentic AI
guage, particularly AI’s involvement, translates into
deployments, it is necessary to identify metrics commensu-
productivity, usability, and support quality for human
ratewiththeiroutput,flexibilityandleverage.Thefollowing
doers.
metricsareprevailinginthefield:
Table 8 summarizes these metrics, providing a basis
Adaptability: This metric considers the AI system’s for evaluating Agentic AI implementations across various
•
propensity or capability to react to environmental applications.
modificationsthatarepromptorabruptactively.Ahigh
adaptability[39]scoremeanstheAIsystemcanundergo B. CASESTUDIES
performance losses due to novel conditions like shifts The case studies presented in this subsection illustrate the
instatisticalmeasures,butnottotheextentofincurring practical uses and performance of agentic AI systems in
significantlosses. several scenarios. These examples highlight the capabilities
Goal Achievement Efficiency: This metric reflects on ofAgenticAIinaccomplishingcomplexgoalsinachanging
•
theAI’sinclinationorabilitytoachieveitsgoalswhile environment.
usingminimalresourcessuchastimeandperson-hours. HealthcareMonitoringandDiagnostics:Ahealthcare
•
This metric becomes critical in applications where the monitoring system based on Agentic AI developed
provision of the AI model’s determinism has strong for healthcare monitoring can independently identify a
consequencesonthefeasibilityoftheapplication. patient’sstatetobedeterioratingthroughsteadytracking
Learning Rate and Convergence: Measures the time of patients’ vital signs. This system has been tested in
•
theAItakestolearnandattachtoaspecifictask.Quick a hospital to enhance the timeliness of patient health
learningrateandquickconvergencearealwayspreferred intervention [47]. It is becoming critical as it improves
as they enable the AI to work effectively in dynamic the time taken to respond to various health issues.
environmentsrequiringcontinuallearning[40],[41]. Thanks to the system’s versatility, it can operate under
Robustness and Resilience: This measure determines different patient conditions and problems, presenting
•
the system’s performance level when its parameters highrobustnessandreliability.
change or during disturbances. Robustness [42], [43]is FinancialMarketAnalysisandAlgorithmicTrading:
•
oneattributethatenablestheeffectivedesignofAgentic In the finance industry [48], [49], an agentic AI
AI,whichcanoperateinseveralvitiatingcircumstances, system was used for trading strategies and real-time
18922 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE8. ComparisonmetricsforagenticAIimplementations.
marketoptimizationwithminimumhumaninteraction. benchmarking datasets and environments have been devel-
To minimize strategies, the AI adjusts them based on opedandarenowusedtocarryoutAgenticAI:
past and current data to improve trading outcomes Healthcare Datasets (e.g., MIMIC-III, PhysioNet):
in times of great market volatility. This case study • Healthcaredatasets[53],[54]areappliedinthetraining
showcases the efficacy and flexibility of agentic AI in and evaluating systems for AI designs for patient
fast-pacedandhigh-risksettingsasminorenhancements monitoring, clinical diagnostic prediction, and clinical
in speed and accuracy in decision-making lead to decisionsupport.TheclaimthatanAgenticAIsystemis
significantfinancialreturns. doinganexcellentjobinHealthcarebenchmarksshows
AutonomousCustomerSupportinE-Commerce:On thatitispossibletomakeAIsystemsthatcanprecisely
•
an e-commerce platform, a customer service e-agent workwithsuchsensitiveandlife-criticalinformation.
madepossiblebyAgenticAItechnologybegsunassisted
Financial Data (e.g., Yahoo Finance, NASDAQ his-
attention [50], knowing full well the needs of the • toricaldata):Fundamentaldatasetsofrespondentswith
individualuserowingtotheirpastbehaviorandknown salesrecords[55]suchasthehistoricalstockpricesare
preferences. Over time, the AI agent adapts to past very useful for an Agentic AI, capable of predictive
interactions and input to the system to improve its analytics and algorithmic trading. These datasets can
responses to questions; this is a classic illustration of alsobeusedtoratetheperformanceregardingprediction
a good human-AI relationship [51]. Customers have ability, robustness in fluctuating volatile markets, and
generally been more satisfied with the individualized profitabilityoftrades.
and context-responsive adaptive support, and the case AutonomousDrivingSimulators(e.g.,CARLA,Ope-
demonstratesthemeritsofincorporatingAgenticAIin • nAIGym):Theenvironmentsallowfordrivingtesting
customer-facinginitiatives. forautonomousnavigationtasksandforAIinvehicles.
Smart Manufacturing and Predictive Maintenance: AI systems’ rate of learning, as well as their adaptive
•
Onaplantfloor,agenticAIcomputesthepredictedtime capability,arealsotestedundersuchenvironments[56],
to failure of the machine and the remaining useful life
[57]. Simulators are especially helpful in tests that
andwhentoperformmaintenance[52]activitiessoasto demand systems to perform similar tasks of safety and
maximizeoperationalavailability.Thissystemleverages decision-makingundervariousconditions.
data from a cluster of machines to proactively predict
Customer Service Datasets (e.g., MultiWOZ, Ama-
futurefailuresandoptimizethedistributionofresources, • zon Customer Reviews): Efficient and personalized
which, in turn, drives the production process. From AI-augmentedcustomerinteractionsareevaluatedinthe
exampledeployments,therobustnessandscalabilityof dimensionofUserandSystemsorSupportcollaboration
theAgenticAIsystemhaveshownitsabilitytofunction where this set of data assists in the estimation of
efficientlyinlarge-scaleanddata-drivenoperations. such measures. The ability to perform well on these
ThesecasestudiesemphasizetheapplicabilityofAgentic benchmarksisadirectindicatoroftheagent’sabilityto
AI technologies in various industries, from healthcare to attend to user concerns as well as hold up to complex
financial and manufacturing. They all demonstrate various inquiries.
aspects of these technologies in practical use that can be Manufacturing and IoT Datasets (e.g., NASA Prog-
scalablefordifferentlevelsofcomplexityissues. • nosticsDataRepository):Thisdatasourceconsistsof
sensordatafromindustrialequipmentthatisutilizedto
C. BENCHMARKING traintheAIapplicationforpredictivemaintenance[58],
Benchmarking is one of the most important procedures [59].Evaluationofperformanceonthesedatasetsseeks
for assessing Agentic AI performance and its standard toassessthepredictionoffailures,resourceallocation,
model.Thisstepisimportantasitallowsmodelresearchers and how effectively operations respond to different
and developers to model. Some several standardized conditions.
VOLUME13,2025 18923

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
of highly complex goals, and these goals may evolve over
Table 9 summarizes these benchmarks, highlighting the time.Thereisastraightforwarddesignproblemherebecause
diverse application areas and the specific focus of each people’s goals do not always lead to intended outcomes,
datasetorenvironment. which could, for example, call for developing inappropriate
ThiscomprehensivebenchmarkingapproachallowsAgen- goals,techniques,orstrategies.
tic AI systems to be evaluated and refined based on However,thequestionofgoalmisalignmentissometimes
performanceinkeyapplicationareas,ensuringthattheymeet more easily addressed than when the central goals of the
industrystandardsforefficiency,accuracy,andadaptabilityin projectsaremulti-dimensionalandcontingentontheproject
real-worldscenarios. context. For example, in the case of medical ethics, an AI
agentoperatingforamaximumrecoveryrateofthepatients
D. CRITICALEVALUATIONOFEXISTING might be focusing on those strategies that work fast and
IMPLEMENTATIONS give results even in the short term but may not be the
Existing Agentic AI implementations highlight its trans- best thing in the long term. Furthermore, these issues are
formative potential and the challenges associated with its intertwined with ethical goals and values structures, which
deployment. aredifficulttoarticulateandintegratewithinthegoalsystem
Successes due to cross-cultural or industry particularities. Addressing
In healthcare, Agentic AI systems have successfully this problem is a requirement because other researchers are
•
monitored patients, identified early warning signs, investigating aligned frameworks like value alignment and
and suggested interventions in real time. These sys- inversereinforcementlearning,whereintheeticsystemsare
tems enhance healthcare delivery, particularly in high- congruent with the emic reward systems. However, these
demandscenarios. explanations are still at the very basic understanding and
In finance, algorithmic trading powered by Agentic AI need a lot of work to cope with complex changes in human
•
has demonstrated superior performance during volatile goals.
market conditions by dynamically adjusting trading
strategies. B. ENVIRONMENTALANDSITUATIONALADAPTABILITY
Inmanufacturing,predictivemaintenancesystemshave As mentioned earlier, agentic AIs tend to be used in
•
reduced downtime by proactively anticipating equip- dynamicandhighlycomplexenvironments.Thisadaptability
mentfailuresandschedulingmaintenance. challengerelatestoadaptingtoreal-worldconditions,which
Limitations may change within a narrow time frame without human
Healthcaresystemsoftenrequireextensivedataprepro- intervention. In practical terms, it is quite challenging to
•
cessingandstrugglewithdataheterogeneity. be highly adaptive, as many dynamics in the real world
Financial AI models may overfit historical trends, are highly unpredictable such as market trends in financial
•
limitingadaptabilitytonovelevents. investment, epidemiological trends in health care, or even
Manufacturing systems face integration issues with journeyeventsinautonomouscars.
•
legacyequipmentandscalabilityconstraints. For most agentic AI systems, technological or contextual
LessonsLearned barriers require action even when there is incomplete infor-
Effective Agentic AI implementations require robust mation, increasing performance reliability ambiguities. For
•
datapipelinesandhigh-qualitytrainingdatasets. instance, in the case of autonomous driving, the agentic AI
Incorporating feedback mechanisms and human over- maynotbefamiliarwiththesurroundingtrafficconditionsor
•
sightimprovesperformanceandensuresethicalcompli- weatherpatternssuchassnoworheavyrainfall,necessitating
ance. the need to adapt in a safe manner to maintain efficiency.
Hybrid models combining classical and agentic While meta-learning and reinforcement learning can help
•
paradigms often yield superior results, as seen in increasetheadaptabilityofagentsbyallowingthemtolearn
complex,multi-stakeholderenvironments. from their past, the limitations lie within the approaches
Addressingtheselimitationswhileleveraginglessonslearned as well, as adaptation and robustness are difficult goals
will be critical for advancing Agentic AI across diverse to achieve. Furthermore, implementing machine learning
domains. models based on generalized processes in such complex
environmentsusuallyrequiresahighcomputingtime,which
VII. TECHNICALCHALLENGESANDLIMITATIONS isonlysometimespractical.
A. GOALALIGNMENTANDCOMPLEXITY
Acriticalconsiderationinthedesignofanysystemishowthe C. RESOURCECONSTRAINTS
autonomouslysetgoalsoftheAIwillagreewiththediverse Agentic AIs are complex systems that require lots of
perspectives of social morals and human users’ objectives. computation and energy resources for their training and
In more simplified terms, it is not like how AI generally deploymentphasesinnavigablespaces.Oneisreinforcement
operates today, where there are set commands to follow. learning, which greatly relies on simulation and data
In contrast, agentic AI benefits from possessing a number processing and consequently increases the cost and time of
18924 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE9. BenchmarksanddatasetsforevaluatingagenticAIimplementations.
trainingwhenused.Millingouttimeforresourcedemandsin Table 10 provides a summary of the primary technical
real-time decision-making circumstances is a big challenge challenges and limitations faced in the development and
inapplicationssuchasthefinanceindustryandautonomous deployment of Agentic AI. Addressing these challenges is
vehicles. essential to advancing the field and ensuring that Agentic
In addition, hardware is another resource for Agentic AI, AIsystemscanfunctioneffectivelyandresponsiblyinreal-
as these systems usually require specialized facilities when worldscenarios.
deployed in real-world environments. For instance, if an
autonomous drone or robot is to be used, it would require
VIII. ETHICAL,SOCIALANDGOVERNANCE
high-performing GPUs, low-latency sensors, and a vital
IMPLICATIONS
energysourcetoenablepromptdecision-making.Inaddition,
A. ACCOUNTABILITYANDRESPONSIBILITY
the proliferation of agentic systems, especially those based
In light of the decision-making independence such systems
oncentralizedcontrolandmonitoring,canputanincreasing
display, understanding accountability and responsibility in
strain on data storage, processing and network bandwidth
Agentic AI systems is a complex challenge. With the more
resources. Coupled with these challenges are the hardware
traditionalAIsystems,toolsfallunderthepurviewofpeople
optimization methods and energy-efficient algorithms that
–thedeveloper,theoperator,ortheuserandtheresponsibility
willberequiredtoimplementAgenticAIsystemslargelyand
rests with the person who uses the tool. With Agentic AI,
cost-effectivelyefficiently.
the question of accountability is more contentious due to
the nature of an independent-acting AI. In situations where
autonomous AI makes a decision that results in a negative
D. SCALABILITY
outcome, the question of responsibility is often misplaced;
With the complexity of design increasing, scaling improves
isitthedeveloper,theserviceproviderwhodeploystheAI,
the system’s performance. Some applications of Agent AI,
ortheAIsystem.
whether in smart cities, healthcare, or financial services,
This particular issue comes out clearly in areas such as
are massive in scale, requiring a higher AI-to-agent ratio,
finance and healthcare, where such systems deal with high-
multifaceted tasks, or huge amounts of data to be handled.
stakesdecision-makingwithhighrepercussions.Thereneeds
However, it is nontrivial to ensure that such systems can
to be a more significant gap between the responsibility and
be scaled up to a higher level without losing some key
liabilityattributionframeworksandthebehavioralintricacies
performance metrics, as it usually involves a multitude of
present in Agentic AI systems. Therefore, Regulations and
concurrenttasksanddatasources.
possibly new legal structures must be invoked to delineate
Multipleagentsorcomponentsdesignandtheirinteraction
responsibility or accountability, especially in environments
presentsamajorchallengeregardingscalability.Forexample,
wheremultiplestakeholdersareparticipatingintheexecution
in a smart city, there may be an AI that manages traffic,
ofthesystem,whichismostofthetime.
energy, and waste collection. Different architectures must
be capable of getting required subsystems to work together
andperformcomplextaskssimultaneously.Besides,asmost B. BIAS,FAIRNESS,ANDTRANSPARENCY
architectsunderstand,thescalingofAgentAIalsomagnifies It is also known that agentic AI systems may replicate and
problems like goal dependency, resource usage, and the exacerbatebiasesinthetrainingdataavailabletothem.The
ability to act in plenty of scenarios. Today, decentralized notion of bias is especially concerning regarding the use of
control, federated learning, and hierarchical structures are Agentic AI in hiring, policing, and lending practices. Not
being used or researched to improve scalability. However, onlymustthesebiasesbeacknowledged,buttheymustalso
the problem remains as scaling out seamless techniques is be addressed through appropriate data management, careful
atechnologicallimitationrelatedtoAIoperatingatalarger algorithm deployment, and active bias reduction programs.
scale. Still,itisessentialtonotethataddressingbiasandmitigating
VOLUME13,2025 18925

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE10. TechnicalchallengesandlimitationsinagenticAI.
itinautonomoussystemsisamuchmoredifficulttaskthan D. REGULATORYANDLEGALPERSPECTIVES
in traditional AI because of the nature of the tasking such The regulatory and legal perspective on Agentic AI is
systemsaredesignedtoperform. still a work in progress as regulators try to streamline
Anotherimportantaspectthatalsohelpsenhancefairness the unique challenges that autonomous systems present.
and trust in Agentic AI [60] systems is transparency. The AI regulations as they stand today mainly address
These systems’ operations must be explained through privacy, transparency, and accountability issues but may
XAI approaches, and there must be an effort to make not necessarily tackle the challenges posed by Agentic
transparent decision-making processes for end users and AI’s autonomy. For instance, the like of the EU’s General
relevant stakeholders. This exposure can help effectively Data Protection Regulation (GDPR) [61] imposes stringent
check an AI’s actions and create a framework for tackling obligations with respect to data and user consent, but these
biasorinjustice.However,explainabilityisquitechallenging requirements may not be adequate when managing AI
to attain fundamentally, and a more significant deal of systemsthatoperateinreal-timewithautonomousdecisions.
it is supposed to be achieved in cases of agentic AI Policymakers[62]arealsoinvestigatingotherframeworks,
systems, which tend to use deep reinforcement learning particularly for high-risk AI systems. Some approaches
models. This area of concern has always been find- call for an ‘‘AI responsibility chain,’’ which can help
ing the right balance between structural complexity and stakeholders determine the accountability of each party of
transparency. theAIsystems.Incontrast,othersrecommendamandatory
explainability forsome AIapplications. Legal standardsfor
Agentic AI are likely to include risk management plans
C. PRIVACYANDSECURITYISSUES
that contain requirements for conducting risk assessments,
Theagentscanperformtheirfunctionseffectivelyindifferent
periodic audits, and certifications for systems operating in
environments by relying on relevant information, often
susceptiblesectorssuchashealth,finance,andsecurity.Itis,
private in domains like healthcare and finance, that are
however,expectedthatasAgenticAIprogresses,developing
alreadysensitiveareas.Suchrelianceonpersonalinformation
legal frameworks that enable innovation while enhancing
invitesprivacyconcernsasdatacanbemishandledandeven
safetyandaccountabilitywillbecrucial.
accessed illegally, leading to a large breach of user privacy.
Table 11 summarizes the primary ethical and governance
Additionally, in this context, the autonomous ability of the
considerationsforAgenticAI,highlightingthecomplexities
Agentic AI can pose a challenge as the data usage can be
thatariseasthesesystemsbecomeincreasinglyautonomous.
difficult to track, thus increasing the likelihood of privacy
abuse.
Thereisalsoasecuritychallengeinthatcyber-attackscan IX. CURRENTFRAMEWORKSFORSAFEAND
threaten these systems, undermining their intended purpose ACCOUNTABLEAGENTICAI
andexposingweaknessesinthesysteminplace.IfagenticAI A. SAFETYPROTOCOLS
systemsarehacked,theycouldbringforthalotofdestruction, Several safety measures and frameworks have been created
primarily when the systems govern critical infrastructure or as a requirement to prevent the autonomous risks involved
sensitive tasks that need to be decided within that context. with decision-making. One of the most basic methods is
There is a great need to maintain a robust and holistic goal safety protocols, being objective-oriented procedures
approach towards cybersecurity, as it is required to secure to suggest to the AI which goals are acceptable to pursue
the information that such systems depend on and their and which actions are harmful. These protocols prevent
functionality. While techniques such as differential privacy harm by ensuring that AI endeavors to achieve legal, safe,
and secure multi-party computation may seem promising, and ethical goals. Also, to prevent AI from going out of
privacy and security threats still exist, so implementation boundsorreachingunanticipateddangeroussituations,fail-
should be done carefully to retain the required functional safemechanisms[63]aredeployed,whichcanadjustoreven
privacy. terminateAIactivitiesaltogether.
18926 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE11. EthicalandgovernanceconsiderationsforagenticAI.
One such framework primarily employed is the risk agenticartificialintelligencedoesnotexceedcontrolledand
evaluation and management protocol [64], which leads supervised settings, with all sorts of human intervention
to the review of the risks posed by the actions of the AI, proceduresfirmlyinplace.
and subsequently, the control measures are put in place.
This is especially important in healthcare and autonomous
C. TRANSPARENCYMECHANISMS
drivingscenarios,whereAItakesactionsthatimpacthuman
Trustandaccountabilityarefoundationaltothedeployment
lives.Additionally,someAgenticAIsystemsutilizeethical
of Agentic AI, and both can be eroded owing to lack of
guardrails[65],whichrestraintheAIfrommakingdecisions
transparency. Explainable AI (XAI) [70], [71] techniques
that raise ethical concerns and promote the AI to perform
have been proposed to offer a more transparent view of
according to social norms and ethics. The illustrated safety
the inner workings of these multi-layered decision-making
protocolsworkasasystemoflayers,offeringagoodlevelof
AI models. As a result, XAI enriches the accountability of
protectionfortheabuseofAgenticAIinanethicalmanner.
the processes involved in reaching decisions as leaders in a
particularfield,suchasthatoffinanceandhealthcare,where
decisions have profound consequences, are informed about
B. MONITORINGANDCONTROLMECHANISMS
thepremisesonwhichspecificactionsweretaken.
The autonomous action of agentic AI systems requires
Beyond just the transparent nature, audit trails can also
monitoring and control mechanisms to govern such actions
be added as an extra layer within Agentic AI systems
andallowforhumaninterventionwherenecessary.Real-time
to document every logic and decision so that the actions
monitoringsystems[66],[67]overseetheAI’sactivitiesand
taken by the AI can be examined afterward. These logs are
decisions and allow humans to intervene if necessary. For
perfectforcompliancebecausetheycanassistorganizations
example, in the case of financial trading systems, AI can
in ensuring that past choices were compliant with the
be employed to identify unusual trade patterns in real-time
law. Self-documenting algorithms [72] also help promote
trading by alerting the relevant authorities and allowing for
self-explainable AI by automatically preparing reports and
theconductofsuchactivitiestobeatacceptablerisklevels.
explanations about the system’s decisions while it is in
Such frameworks as Human-in-the-loop (HITL) [68]
operation. Such mechanisms not only foster transparency
and human-on-the-loop (HOTL) [69] have been designed
but also facilitate feedback mechanisms, as they enable
with the idea of maintaining an equilibrium between the
developers and stakeholders to improve and understand the
extentofautonomyexperiencedandthenecessityofhuman
decision-makingprocessoftheAIovertime.
control. When HITL configurations are deployed, human
operatorstendtoapprovesomeactionsanddirectlyinteract
with the AI while making certain decisions. On the other D. CASESTUDIESOFGOVERNANCEAPPROACHES
hand,inHOTLsystems,thehumansupervisormonitorsthe Several industry and academic efforts have created gover-
AIwithoutdecidingoneveryactionbutcanintervenewhen nance frameworks to guarantee the safe, responsible and
necessary.Thesemechanismsareessentialforhealthcareand ethical use of AI. Here are several examples that are worth
other serious decisions involving AI, where the presence of mentioning[73]:
humanintelligenceisstillrequired. Microsoft’s AI Principles and Responsible AI Stan-
•
Override protocols also exist in Agentic AI systems to dard:Theseincludefairness,reliability,privacy,inclu-
stoporchangeactionsundertakenbytheAIifasituationis siveness, and transparency, which govern the shaping
classifiedasunforeseenorfallsoutsidethereasonablerange ofAIsystemsaccordingtoMicrosoft’sResponsibleAI
of expected behavior. Last-line systems provide another Standard.ItalsocontainstheAetherCommittee,which
level of defense by making it possible for the AI to fairly addresses the ethical and social issues brought
be overpowered by a human if its autonomous conduct aboutbyAI.Therehavebeenotherproductsthroughout
becomes damaging. Combined with the aforementioned, thebusinessforwhichthisframeworkhasbeenusedto
these monitoring and control measures are designed to build robust AI risk processes throughout Microsoft’s
deliver a multitude of defense in depth to ensure that the offerings.
VOLUME13,2025 18927

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE12. GovernanceframeworksforsafeandaccountableagenticAI.
Google’s AI Principles and Model Cards for Trans- theenvironmentsorchangesignificantlywithoutretraining.
•
parency: Google defines AI principles for developing Thus, future work might involve solving meta-learning
and deploying AI while ensuring privacy, security, and transfer-learning problems specifically for Agentic AI
and accountability across its platforms. The company systems, allowing them to rapidly adapt to new situations
alsoemploysModelCards,whichcontaininformation based on their previous experiences. Moreover, it would be
on a model’s performance, limitations, and intended interesting to research on platforms that enable real-time
application, allowing users to appreciate the strengths learning whereby agents learn and modify in response to
andweaknessesofAIsystems. changes but their primary functions are not affected. This
OpenAI’s Charter and Safety Standards: OpenAI wouldimprovebothresilienceandadaptabilitytremendously.
•
undertook to adopt a charter that contains ethical and
safety standards to be observed in developing general- B. IMPROVINGGOALALIGNMENTWITHHUMANVALUES
purpose AI. OpenAI takes a human-focused approach Integrating ethical and value-based human approaches into
andisvalue-orientedtowardalignmentwiththesegoals, AgenticAIsystemsisoneoftheopenbranchesofresearch
safety research, and open development of AI. This thatshouldbeadvancedinthefuture.Giventheautonomous
organization’s safety research is directed at developing natureofoperatingthesesystems,thereexiststhepossibility
models meant to interact and operate in unpredictable of a goal misalignment problem whereby the AI is driven
environments, allowing for the responsible future of to do the right thing. Still, the action is contrary to human
AgenticAI. interests. This work can explore value alignment strategies
TheIEEEGlobalInitiativeonEthicsofAutonomous suchasinversereinforcementlearning(IRL)andcooperative
•
and Intelligent Systems: IEEE’s initiative has for- inversereinforcementlearning(CIRL),inwhichtheAIgoes
mulated standards [74] with corresponding guidelines through experience and exposure to human social context
on ethical AI and addressed areas such as matters of to learn human preferences and values. In addition, such
transparency, accountability, as well as data integrity. frameworks should be created that would permit real-time
They are aimed at assisting developers in setting the adjustmentstothelevelofalignmentbetweenAgenticAIand
standard for the UK AI systems that they develop so humanobjectivesdependingonchangingsocialbehavioror
thatthesesystemswillnotonlyworkbutmustbeethical thetargetedaudience’scues.
and social, ensuring trust and safety in autonomous AI
technologies.
C. INTEGRATIONINTOLIVINGSOFTWAREAND
These case studies illustrate diverse governance CYBER-PHYSICALSYSTEMS
approachesthatbalanceinnovationwithsafety,accountabil- When Agentic AI is widespread, developing robust ethical
ity,andtransparency.Table12summarizestheseframeworks, and global guidelines for this technology application and
comparingkeyprinciplesandfocusareas. developmentwillbeessential.Autonomousdecision-making
in the systems complicates ethical issues like bias, privacy,
X. OPENRESEARCHCHALLENGESANDFUTURE accountability, and transparency. Areas of future research
DIRECTIONS can be directed at how to build a universal ethical frame-
The development and deployment of Agentic AI systems work for Agentic AI, which may include mechanisms of
presentseveralopenresearchchallengesthatrequireattention multidimensional ethical audit, oversight, and certification.
to ensure safe, effective, and ethically aligned AI. This This includes initiatives involving policymakers, ethicists,
sectionexploresthesechallengesandoutlinespotentialfuture and AI practitioners to embed supervisory mechanisms that
directionsforadvancingAgenticAI. foster advancements without undermining other societal
interests[75].
A. ENHANCEDADAPTABILITYANDRESILIENCE
Indynamicanduncertaincontexts,AgenticAIsystemsmust D. ETHICALFRAMEWORKSANDGLOBALSTANDARDS
demonstrateadaptabilityandresilienceastheyoperateinthe ThedefinitionofAIagencyisstillinthemakingstage,and
environment.Mostexistingmodelsdonotgeneralizeacross howadvanceddecision-making,planning,andreasoning[76]
18928 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
willbeembracedwithinAgenticAIisstillbeingdetermined. decorated with efficient elements of decentralized control,
Theoretical advances in multi-agent systems such as coor- the quicker the optimized directional tasks and networks as
dination,decentralizeddecision-making,orstructured‘goal’ awholesystemwillbe,whereoptimizationprocessesoccur
managementcouldhelpincreasetheautonomyofAIsystems in bulks of intelligent agents. As it has become apparent in
withoutlosingcontrol.Also,abetterunderstandingofagents’ recentyears,thesetaskshavebecomepossiblewithsystems
cognitive functions, such as curiosity, intrinsic motivation, based on swarm intelligence and decentralized [79] control
and moral reasoning, could contribute to developing more ofstructuresandprocesses.
robust and responsible Agentic AI systems. Formulating Another area of interest is the hierarchical models,
scripts for AI agencies will be vital for ensuring that these which break down decision-making processes into different
systems can operate in a deterministic and dependable layers[80],wherethesystemcanonlyfocusongeneralgoals
mannerindiverseandcomplexenvironments[77]. and distribute particular actions to subordinate agents. For
instance, in the smart city context, a hierarchical Agentic
AI could oversee the movement of cars throughout the
E. THEORETICALADVANCESINAIAGENCY
city. At the same time, local agents manage the traffic
The concept of agency in AI is still evolving, and there
at a particular intersection. This configuration diminishes
is much to be explored regarding how Agentic AI can
the computation each agent has to perform and enables
developadvanceddecision-making,planning,andreasoning
bettersystemscalability.Thehierarchicalmodelshavefound
abilities.Theoreticalresearchintotopicssuchasmulti-agent
much application in the coordinated control of multiple,
coordination, decentralized decision-making, and long-term
interdependent processes in a system since they allow for
goalmanagementcouldprovidenewinsightsintoenhancing
agnostictaskschedulingasthestateofthesystemchanges.
AI autonomy while maintaining control [78]. Additionally,
Balancedloadingoftasksamongprocessorsisanother
advancing our understanding of cognitive functions like
factor that improves scalability since it allows distribut-
curiosity, intrinsic motivation, and moral reasoning in arti-
ing computations over several devices or servers. Within
ficial agents could help design more robust and ethically
distributed processing frameworks, large scale Agentic AI
aligned Agentic AI systems. Developing formal models of
systems could make the most of cloud or edge computing
AI agency will be essential for ensuring these systems
resourcestocarryoutcomputationinmultipleprocessesand
can act responsibly and predictably in diverse and complex
lower the time taken to respond. Such a situation proves
environments.
helpfulinoperatinginremoteapplicationsorintime-critical
Table13providesasummaryoftheprimaryopenresearch
situations such as autonomous vehicles or smart grid sys-
challenges and future directions in Agentic AI. Each area
tems where real-time data processing and decision-making
highlightscriticalaspectsofadvancingthefieldresponsibly
are critical. There is ongoing advancement in deploying
andsustainably.
distributed AI frameworks, such as federated learning [81]
and edge AI [82], that enhance the maneuverability of
F. SCALABILITYANDEFFICIENCY AgenticAIsystemsinawideroperationalareawithdispersed
The deployment of Agentic AI systems in large-scale and installations[83].
complexenvironmentsimposesnewconstraints,resultingin ApartfromtheAIsystemsintegration,improvementofthe
vast requirements for scalability and efficiency. There are Agentic AI systems embodies energy-efficient algorithms
scenarioswhensuchsystemsneedtomanageresourcesand and hardware optimizations [84]. This is vital when
informationatlarge,interactwithnumerousagents,andmake the applications must run endlessly and provide real-time
decisions within a short period. For both scalability and responses.SeveralAgenticAImodelsarebuiltusingopera-
efficiency to be achieved, new advancements in algorithms, tionallyexpensivealgorithmslikedeepreinforcementlearn-
architectures, and hardware have to be made. This research ing, requiring enormous power resources. Further progress
areaischaracterizedbytheuseofcenterlessandhierarchical is made in energy-efficient machine learning approaches,
frameworks and distributed processing or energy-efficient such as sparse neural networks and quantized models that
hardware. address the computation requirements at lower levels while
Aside from its numerous advantages, a well-known retaining the quality of the end products. Furthermore,
limitation that stems from the emergence of decentralized neuromorphicprocessorsandAIacceleratorsaresomeofthe
architectures is their integration into large-scale systems. emerginghardwaretechnologiesthataremeanttoenablethe
Sincethecontrolprocesscanbehandledbynumerousnodes performance of AI tasks with minimal power requirements.
in a fully distributed way, there is no need for a single These hardware improvements are critical in expanding the
centralizedcontroller.Thus,theresponsibilityandloadofthis AgenticAIsystemstoedgedevicesandIoTapplicationswith
nodedonotaffectthesystem’sscalability.Animprovement limitedornopowerresources.
ofspecificprocessesinthis-stylearchitecturemightinclude Although progress has been achieved, they only partially
certain structural, behavioral rules that regularize agents’ solve the problem of scalability and efficiency, which con-
actions regarding network interactions. The more structures tinuetobeactiveresearchissuesasreal-worldenvironments
VOLUME13,2025 18929

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE13. SummaryofopenresearchchallengesandfuturedirectionsinagenticAI.
becomeincreasinglycomplex.Futuredirectionsinthisarea enablingthesystemtoleverageitspreviouslessonsinsteadof
include the development of adaptive resource allocation acquiringnewones.Transferlearningisknowntobeeffective
techniques [85] that dynamically allocate computational during these scenarios since it allows the AI to adjust to
resources based on task importance, as well as self- different patient profiles or drive in different environments,
optimizing algorithms [86] that adjust their complexity suchasautonomousdriving.
dynamically depending on the requirements. Moreover, Resilience in the case of Agentic AI systems is crucial
thankstocollaborativeintelligence[87]conception,agents as it allows them to deliver consistent outcomes despite
will be able to solve issues without complicated integration upsets being caused by compromised sensors, intermittent
processes as they will be able to handle sophisticated networks or external factors that were not anticipated.
operationscollectively,thusenhancingsystemscalability. To increase resilience, there are ongoing investigations on
robust reinforcement learning techniques that enable the
reliable functioning of agents in the presence of consistent
G. ENHANCEDADAPTABILITYANDRESILIENCE uncertaintyorunknownnoise.Robustreinforcementlearning
AgenticAIsystems,particularlythoseemployedbyahuman methods rely on dual dynamics, allowing the learner to
worker or soldier, are built to endure persistence under seek performance maximization and impact minimization
demanding, unpredictable conditions. Therefore, achieving of stochastic events. This dual objective ensures the agent
persistentoperationalsuccesswouldrequirethesesystemsto can effectively implement its functionalities even when the
modifytheiractionsautonomouslyandgainfurtherlearning normalconditionsvary.
resilience constantly. How can one reach such a high level Self-recovery mechanisms are being explored as sup-
oflearningresilience?Onepossibleanswerliesintheuseof plementary to everyday learning strategies. Self-recovery
AgenticAItechnologiesthatcangeneralizeacrossdifferent mechanisms allow Agentic AI systems to auto-flag and
environments and concepts, deal with high uncertainty, and rectify their duplicates without help. For example, self-
copewithunforeseeninterruptions. recovery strategies in autonomous robotics may include
One exciting way of achieving such resilience is through obstacle avoidance strategies where the robot uses an
meta-learning, or what children call ‘‘learning to learn.’’ alternativeapproachorsiteconfigurationstrategies.System
Suchmeta-learningalgorithmsenableanAItolearninforma- self-recoverymechanismsallowseamlesssystemrestoration
tionthatmayapplytodifferentassignmentsorenvironments, after a range of disruptions, which is particularly beneficial
allowing the AI to be flexible with virtually no retraining. tomission-criticalareaslikedisastermanagementandspace
For example, in robotic tasks [88], a meta-learning agent exploration,wherehumaninterventionisnotalwaysfeasible.
raisedinoneenvironment(let’ssay,inthehouse)canmove Thestand-outareasofresearchthatarehelpfulinboththe
to an alternative environment (the outside) and assume the modificationandrobustnessofAgenticAIincludereal-time
knowledge of moving within the outside environment. This learning. AI self-recovery mechanisms [92], on the other
is because AI can now learn like humans [89] and use hand, include real-time learning. This mechanism allows
its past experiences in the environment to approach new AI systems to receive and integrate new information into
situations[90]. relevantmodelswithoutceasingoperationalactivities.Thisis
Anothersignificantapproachforenhancingadaptabilityis excellent,forexample,inthefinanceorcyberwarfarezones
calledtransferlearning[91].Ithasprovedthatunlikestatic models,whichrequireswiftAIalterationsonmarketchanges
models trained for a particular purpose, a learning model orthreats.However,withthiscapability,newchallengesalso
trained for one task can perform a similar or even related, ariserelatedtothereal-timeprocessingofdata,theabilityto
yetdistinct,task.Thismethodisparticularlyconvenientfor conductcomputation,modelmaintenance,andstability,and
Agentic AIs acting in many different operational spheres, theseneedtobeaddressedinfuturestudies.
18930 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
Looking to the future, progress in improving adaptability acts. Provisions for processes that would enable tracing
andsurvivabilitywilllikelyincludethecreationofcontext- responsibility in a wide range of stakeholders, including
awarelearningalgorithms[93],whichevaluatethesetting farmers, custodians, and machines, must be in place. Some
and act by it. In other words, some form of contextual approaches suggest an AI responsibility chain, which
AI could switch its unitary decision-making style depend- separates the roles and responsibilities of each stakeholder
ing on uncertainty or resource availability. Furthermore, during the development and deployment process to prevent
investigation of multi-modal learning [94], [95], which over-relianceononeindividual[97].
fuses information from multiple sources and types to better Privacy and Security Standards are especially critical
understand different situations, may assist in improving the when addressing Agentic AI, which generally requires
versatility of Agentic AI systems in the operative context. operating on susceptible data. There should be guidelines
Withvisual,auditory,andotherkindsofinformation,multi- prescribing how data is managed, secured or anonymized
modallearningcanbeparticularlyeffectiveforautonomous to meet user privacy. This includes baseline restrictions on
vehiclestryingtofunctionincomplexsituations. processing,suchastheuseofdifferentialprivacyandsecure
access to databases, which allow for reducing possibilities
for breaches or abuse of the data. Furthermore, appropriate
H. ETHICALFRAMEWORKSANDGLOBALSTANDARDS measures should be employed to safeguard the security
The increasing capabilities of Autonomous Agentic AI of Agentic AI, especially in smart cities and autonomous
systems operating in significant sectors have intensified vehicles where such AI systems are exposed to potential
the call for appropriate ethical considerations and global cyberthreatsandcanbeadangertothepublic.
standards to be put in place. These considerations and To concretize these principles, several regulating author-
standardsarepivotalinregulatinghowAgenticAIinteracts ities and industry associations have suggested using ethical
with stakeholders and the environment to minimize adverse guidelines and frameworks aimed at the responsible use of
impacts,biases,andthreatstosafetyandprivacy.Inaddition, artificialintelligence.Inparticular,someofthecorematerial
appropriate and well-thought-out ethical considerations and forthelegalissuesofprivacyandotheruserrightsarecon-
global standards also seek to define the scope and areas of tainedintheEthicsGuidelinesforTrustworthyAIdeveloped
transparency,equity,accountability,anduserprivacy,which by the European Union and the General Data Protection
needtobeemphasizedinthedesignanduseofAI. Regulation. Similarly, the IEEE and the Partnership on AI
One of the critical barriers to establishing these frame- organizationshavealsoformulatedsomebehavioralartificial
works is the existence of ethical and legal variety in intelligence ethics addressing responsibility, fairness, and
different societies. Ethical issues, including data protection, opennessissues.Althoughtheseguidelineshavenouniversal
transparency in who took the decision, and reliance on application,effectiveinternationalgovernmentauthorityhas
autonomousdecisions,mayrangefromonesocietytoanother been advocated to coordinate the interaction between AI
depending on legal order, customs, traditions, or politics. policiesandstandardsfromdifferentcountries.
For these differences to be addressed while promoting Afurtherdevelopmentconcerningtheissueisestablishing
synergies among regions, a global set of ethical standards an internationally operating AI coordinating entity or a
for AI governance is fundamental. Establishing universal consortium like in Europe that could promote the estab-
ethicalprinciplescanprovidethebasisforthisalignmentby lishment of AI standards and global adherence to ethical
developing common approaches to equity, non-maleficence principles. This organization would create an objective to
andbeneficencethatwouldoverridelocaldifferences. standardize AI regulations so that ethical norms and safety
Transparency and Explainability are undoubtedly the requirementswillinvariablybeprovidedacrosscountriesand
components of an ethical algorithm since they allow third industries. Moreover, it necessitates research on adaptive
partiestocomprehendthedecision-makingprocessofartifi- regulatoryregimes[98]thatareresponsivetotechnological
cialintelligence.InAgenticAI,suchattributesarenecessary developments.
for users’ trust, especially in crucial sectors like healthcare Table 14 summarizes the primary components of ethical
and finance, where the rationale behind the decision needs frameworks and global standards for Agentic AI, outlining
to be accountable. These include XAI techniques that essentialareasforresponsibleandsafeAIgovernance.
allow stakeholders to explain the interpretation process.
Therefore, given the erosion of these fundamental rights,
theseframeworksshouldemphasizetheneedtoincorporate I. THEORETICALADVANCESINAIAGENCY
stakeholders’responsibilitiesandauthorities’mechanismsto AIsystemswiththepotentialforintelligentactionstillneed
scrutinizeAI-generateddecisions[96]. theoretical development regarding number and complexity
Moreimportantandunwaveringlyrelatedtothedevelop- in understanding agency, self-organization, and decision-
mentofethicalframeworksistheissueofanAccountability making processes. For now, embodiments of Agentic AI
andResponsibility.Withthegrowingautonomyofagentsin exhibit their expected performance in structured tasks and
society,therehavebeensignificantdifficultiesindetermining environments, yet transferring such capabilities into higher-
whoshouldbeheldresponsiblefortheresultsofAI-enhanced order, poly-context environments will necessitate a sensible
VOLUME13,2025 18931

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
TABLE14. KeyComponentsofethicalframeworksandglobalstandardsforagenticAI.
underlying framework. In a larger perspective, however, developmentinthetheoryofself-rewardingwillenhanceAI
some theoretical extensions of the issues, like multi-agent agents’abilitiestobegoal-orientedanddirectedbyaflexible
coordination,meta-goalachievement,activepersistence,and strategy while dealing with complex problems caused by a
planner controlling with ethical consideration, assist the AI lackofstructure.
modelsinbehavingappropriatelyindifferentenvironments. Moralreasoningandethicaldecision-makingaregain-
Multi-agent coordination is an example of such a class ing acceptance in the field of advanced AI agency [99],
of theories, and it is concerned with allowing AI agents particularlynowthatAIisincreasinglyusedforsensitiveand
to engage, communicate, and collaborate in environments high-risktasks.Researchonmoralreasoningseekstooffera
that contain multiple autonomous entities. In particular, basisforethicaldeliberationsinautonomoussystemssothat
practicalapplicationsmulti-agentcoordinationiscrucialfor AgenticAIcanpurposefullychooseactionswiththoughtof
applicationsincollaborativerobotics,decentralizedsystems, their effects and values. In this context, integrating ethics,
and smart city architecture. This domain examines how philosophy, and psychology into AI is an overarching aim
agents learn to pursue their separate aims while achieving if ethical AI systems should be created. Codifying moral
mutual goals or seeking to work cooperatively, utilizing reasoning in AI will be necessary for health, law and order,
materials from game theory, reinforcement learning, and and autonomous automobiles, the decision of which can be
communication theory. Developments in this domain will influentialtosociety.
allowAgenticAItocarryoutinterdependentcomplextasks A few of the areas of theoretical research that need a
whereagentsmustcooperateandcompete. mention are self-awareness and meta-cognition [100] in
Long-term goal management is decisive and is char- AI which include building systems that understand their
acterized as having advanced agentic capabilities. There actions,abilities,orlimitationsasself-referentialknowledge.
are deeply ingrained limitations concerning timelines with All the AI that are self-aware will be able to self-evaluate
currentAIsystems.CurrentAIstendtooptimizeforshorter whethertheyhaveperformedtheirtasksoptimally,whatcan
timelines, thus losing the capacity to strategize, forecast beimproved,andwhatactionstotakewhentherearefailures
trends, and distinguish between sub-objectives. Theoretical orpoorperformance.Self-agencyabilitieswillalsoallowAI
work addresses the practical challenges of enabling AIs to toassessitsstrategiesandlearningprocessesinthehopesthat
set and pursue long-range goals as conditions change and its agents will be able to enhance their decision-making in
constraintsemerge.Hierarchicalreinforcementlearningand thefuture.Progressintheself-awarenessandmeta-cognition
temporal reasoning are two measures that have promise as areas might allow for the emergence of more sophisticated
they allow AI systems to decompose high-level goals into and flexible Agentic AI systems that enhance and improve
sub-tasks,whichtakethesystemtowardtheoverallendstate theirperformanceandrobustnessinmultipleenvironments.
throughpredeterminedobjectives. Inthisregard,thefuturepossibilitiesoftheworksincluded
Agents’ ability to wait for a reward and workers’ pursuit the possibility of creating formal models of AI agency,
on their own define two self-rewarding procedures that which would include the discussed dimensions and form
emergetowardsthecreationofagenticAI;bothproceduresin a theoretical framework that could be used for the design
dominationwithzerohitorstandaloneprovideenoughbasis and evaluation of agentic behavior. The models could also
to move forward without external incentives or directives. serve the great purpose of setting metrics and benchmarks
Anemergingfieldofresearchinself-directedstrategyrelies for agencies that would, in turn, facilitate ascertaining
on developing agents that can explore, learn, and adapt the efficacy of AI systems in performing complex and
basedsolelyontheircuriosityabouttheirenvironment.This nonsupervised tasks. Further, studies on adaptive moral
would be important in cases where the information space is frameworks and contextual decision-making [101] might
uncertainorwherethegoalisnotdefinedandothervariables enableAgenticAItotakesituationalethicsandchangehow
are likely to change within the domain of the goal. Further itmakesdecisionsinvariouscontexts.
18932 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
J. ROADMAPFORFUTURERESEARCH and human-AI collaboration. As these systems evolve,
The future of Agentic AI depends on addressing current they are poised to tackle complex tasks autonomously,
limitations and expanding its applicability. Key areas for significantlyexpandingthescopeofAIapplicationsinboth
researchinclude structured and unstructured environments. By combining
:
Goal Alignment with Human Values: Developing adaptive learning, robust reinforcement mechanisms, and
•
frameworks for inverse reinforcement learning (IRL) real-time responsiveness, Agentic AI systems can deliver
and cooperative IRL to ensure Agentic AI objectives dynamic solutions that enhance productivity and efficiency.
alignwithsocietalvalues. However,withincreasedautonomycomestheresponsibility
Scalability: Exploring decentralized architectures and to address ethical considerations and ensure accountability,
•
federatedlearningtoenableAgenticAItohandlelarge- transparency, and fairness. As Agentic AI continues to
scale,distributedsystemseffectively. evolve, it is essential that these systems are developed with
AdaptabilityandResilience:Advancingmeta-learning a clear focus on ethical alignment, resilience, and regula-
•
andtransfer-learningtechniquestoallowAgenticAIto tory compliance to prevent potential misuse or unintended
adapttonovelsituationswithoutretraining. consequences.
Energy Efficiency: Innovating energy-efficient hard-
•
ware and algorithms to reduce the computational REFERENCES
cost of deploying Agentic AI in resource-constrained
[1] A.Chanetal.,‘‘Harmsfromincreasinglyagenticalgorithmicsystems,’’
environments. inProc.ACMConf.Fairness,Accountability,Transparency,Jun.2023,
Ethical and Governance Frameworks: Establishing pp.651–666.
• [2] A.Paul,C.LokYu,E.A.Susanto,N.W.L.Lau,andG.I.Meadows,
universal ethical standards, transparency mechanisms,
‘‘AgentPeerTalk: Empowering students through agentic-AI-driven dis-
and regulatory guidelines to ensure responsible AI cernmentofbullyingandjokinginpeerinteractionsinschools,’’2024,
deployment. arXiv:2408.01459.
[3] Y.Shavit,S.Agarwal,M.Brundage,S.Adler,C.O’Keefe,R.Campbell,
Real-Time Learning Systems: Designing systems
• T. Lee, P. Mishkin, T. Eloundou, A. Hickey, K. Slama, L. Ahmad,
capable of learning and adapting in real-time without P.McMillan,A.Beutel,A.Passos,andD.G.Robinson,‘‘Practicesfor
disruptingongoingoperations. governingagenticaisystems,’’inProc.Res.Paper,OpenAI,Dec.2023,
By addressing these areas, future research can enable pp.1–25.
[4] S.Guenatetal.,‘‘Meetingsustainabledevelopmentgoalsviarobotics
AgenticAItoachieveitsfullpotentialacrossindustrieswhile
and autonomous systems,’’ Nature Commun., vol. 13, no. 1, p.3559,
mitigatingrisks. Jun.2022.
[5] E. H. B. Maia, L. C. Assis, T. A. de Oliveira, A. M. da Silva,
and A.G.Taranto, ‘‘Structure-based virtual screening: From clas-
XI. CONCLUSION
sical to artificial intelligence,’’ Frontiers Chem., vol. 8, p.343,
A. SUMMARYOFKEYFINDINGS Apr.2020.
This survey has explored the foundational characteristics, [6] S.Yao,J.Zhao,D.Yu,N.Du,I.Shafran,K.Narasimhan,andY.Cao,
‘‘ReAct:Synergizingreasoningandactinginlanguagemodels,’’2022,
methodologies, applications, challenges, and future direc-
arXiv:2210.03629.
tions of Agentic AI. Key findings highlight that Agentic AI
[7] R.Yang,S.Lin,Y.Li,S.Zhao,Y.Ge,X.Li,andY.Shan,‘‘GPT4Tools:
representsasignificantadvancementinartificialintelligence, Teachinglargelanguagemodeltousetoolsviaself-instruction,’’inProc.
characterized by autonomy, goal-oriented behavior, and Adv.NeuralInf.Process.Syst.,Jan.2023,pp.1–13.
[8] S.Feuerriegel,J.Hartmann,C.Janiesch,andP.Zschech,‘‘Generative
adaptabilityacrossdiverseenvironments.Wehaveidentified
AI,’’Bus.Inf.Syst.Eng.,vol.66,no.1,pp.111–126,Sep.2023.
core applications in industries such as healthcare, finance, [9] T.Chong,T.Yu,D.I.Keeling,andK.deRuyter,‘‘AI-chatbotsonthe
and manufacturing, where Agentic AI’s ability to make servicesfrontlineaddressingthechallengesandopportunitiesofagency,’’
J.RetailingConsum.Services,vol.63,Nov.2021,Art.no.102735.
context-aware, autonomous decisions offers transformative
[10] L. Chen, S. Li, Q. Bai, J. Yang, S. Jiang, and Y. Miao, ‘‘Review of
benefits. However, deploying these systems in real-world
imageclassificationalgorithmsbasedonconvolutionalneuralnetworks,’’
scenariosintroduceschallengessuchasscalability,resource RemoteSens.,vol.13,no.22,p.4712,Nov.2021.
constraints, and ethical concerns, all of which require [11] A.Brisset,R.Gill,andR.Gannon,‘‘Thesearchforanativelanguage:
Translation and cultural identity,’’ in The Translation Studies Reader.
robustsolutionstoensuresafeandeffectiveAIdeployment.
Evanston,IL,USA:Routledge,2021,pp.289–319.
Through a comparative analysis, we examined various [12] H. Ko, S. Lee, Y. Park, and A. Choi, ‘‘A survey of recommendation
implementation frameworks, tools, and methodologies that systems:Recommendationmodels,techniques,andapplicationfields,’’
Electronics,vol.11,no.1,p.141,Jan.2022.
contribute to the development and evaluation of Agentic
[13] Y.Matsuo,Y.LeCun,M.Sahani,D.Precup,D.Silver,M.Sugiyama,
AI. We also identified open research challenges, including
E. Uchibe, and J. Morimoto, ‘‘Deep learning, reinforcement learn-
goal alignment, multi-agent coordination, and regulatory ing, and world models,’’ Neural Netw., vol. 152, pp.267–275,
adaptation, which must be addressed to fully realize the Apr.2022.
[14] F. Binucci, P. Banelli, P. Di Lorenzo, and S. Barbarossa, ‘‘Dynamic
potentialofAgenticAI.
resourceallocationformulti-usergoal-orientedcommunicationsatthe
wirelessedge,’’inProc.30thEur.SignalProcess.Conf.(EUSIPCO),
B. FINALINSIGHTSONAGENTICAI Aug.2022,pp.697–701.
[15] L.Zhao,H.Cheng,J.Zhang,andY.Xia,‘‘Adaptivecontrolforamotion
Agentic AI holds transformative potential across numerous
mechanism with pneumatic artificial muscles subject to dead-zones,’’
sectors,promisingadvancesinautomation,decision-making, Mech.Syst.SignalProcess.,vol.148,Feb.2021,Art.no.107155.
VOLUME13,2025 18933

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
[16] C. A. Aubin, B. Gorissen, E. Milana, P. R. Buskohl, N. Lazarus, [38] S.Gao,A.Fang,Y.Huang,V.Giunchiglia,A.Noori,J.R.Schwarz,
G.A.Slipher, C. Keplinger, J. Bongard, F. Iida, J. A. Lewis, and Y.Ektefaie,J.Kondic,andM.Zitnik,‘‘Empoweringbiomedicaldiscov-
R.F.Shepherd, ‘‘Towards enduring autonomous robots via embodied erywithAIagents,’’Cell,vol.187,no.22,pp.6125–6151,Oct.2024.
energy,’’Nature,vol.602,no.7897,pp.393–402,Feb.2022. [39] M. Murtaza, Y. Ahmed, J. A. Shamsi, F. Sherwani, and M. Usman,
[17] P. Dhamija and S. Bag, ‘‘Role of artificial intelligence in operations ‘‘AI-based personalized E-learning systems: Issues, challenges, and
environment:Areviewandbibliometricanalysis,’’TQMJ.,vol.32,no.4, solutions,’’IEEEAccess,vol.10,pp.81323–81342,2022.
pp.869–896,Jul.2020. [40] N. Loizou, S. Vaswani, I. Laradji, and S. Lacoste-Julien, ‘‘Stochastic
[18] S.Kapoor,B.Stroebl,Z.S.Siegel,N.Nadgir,andA.Narayanan,‘‘AI polyak step-size for SGD: An adaptive learning rate for fast conver-
agentsthatmatter,’’2024,arXiv:2407.01502. gence,’’inProc.Int.Conf.Artif.Intell.Statist.,Feb.2020,pp.1306–1314.
[19] N.J.FastandJ.Schroeder,‘‘Poweranddecisionmaking:Newdirections [41] M. Chen, H. V. Poor, W. Saad, and S. Cui, ‘‘Convergence time
for research in the age of artificial intelligence,’’ Current Opinion optimizationforfederatedlearningoverwirelessnetworks,’’IEEETrans.
Psychol.,vol.33,pp.172–176,Jun.2020. WirelessCommun.,vol.20,no.4,pp.2457–2471,Apr.2021.
[20] R.C.CardosoandA.Ferrando,‘‘Areviewofagent-basedprogramming [42] R. Hamon, H. Junklewitz, and S. M. J. Ignacio, ‘‘Robustness and
formulti-agentsystems,’’Computers,vol.10,no.2,p.16,Jan.2021. explainabilityofartificialintelligence,’’PublicationsOfficeEur.Union,
[21] P.Putta,E.Mills,N.Garg,S.Motwani,C.Finn,D.Garg,andR.Rafailov, vol.207,pp.1–40,Jan.2020.
‘‘AgentQ:AdvancedreasoningandlearningforautonomousAIagents,’’ [43] U. Mittal and D. Panchal, ‘‘AI-based evaluation system for supply
2024,arXiv:2408.07199. chainvulnerabilitiesandresilienceamidstexternalshocks:Anempirical
[22] T.M.Getu,G.Kaddoum,andM.Bennis,‘‘Asurveyongoal-oriented approach,’’Rep.Mech.Eng.,vol.4,no.1,pp.276–289,Nov.2023.
semanticcommunication:Techniques,challenges,andfuturedirections,’’ [44] S. Tatineni and V. R. Boppana, ‘‘Ai-powered devops and mlops
IEEEAccess,vol.12,pp.51223–51274,2024. frameworks: Enhancing collaboration, automation, and scalability in
[23] A. Zeng, M. Liu, R. Lu, B. Wang, X. Liu, Y. Dong, and J. Tang, machine learning pipelines,’’ J. Artif. Intell. Res. Appl., vol. 1, no. 2,
‘‘AgentTuning:EnablinggeneralizedagentabilitiesforLLMs,’’2023, pp.58–88,2021.
arXiv:2310.12823. [45] P. Hemmer, M. Westphal, M. Schemmer, S. Vetter, M. Vössing, and
[24] C.-P.DaiandF.Ke,‘‘Educationalapplicationsofartificialintelligence G.Satzger, ‘‘Human-AI collaboration: The effect of AI delegation on
insimulation-basedlearning:Asystematicmappingreview,’’Comput. humantaskperformanceandtasksatisfaction,’’inProc.28thInt.Conf.
Educ.,Artif.Intell.,vol.3,Jan.2022,Art.no.100087. Intell.UserInterface,Mar.2023,pp.453–463.
[25] N.Shinn,B.Labash,andA.Gopinath,‘‘Reflexion:Languageagentswith [46] M.Fan,X.Yang,T.Yu,Q.V.Liao,andJ.Zhao,‘‘Human-AIcollaboration
verbalreinforcementlearning,’’inProc.Adv.NeuralInf.Process.Syst., forUXevaluation:Effectsofexplanationandsynchronization,’’Proc.
Jan.2023,pp.1–18. ACMHum.–Comput.Interact.,vol.6,pp.1–32,Mar.2022.
[26] X. Wang, Y. Chen, and W. Zhu, ‘‘A survey on curriculum learning,’’ [47] S. P. Pattyam, ‘‘Artificial intelligence for healthcare diagnostics:
IEEETrans.PatternAnal.Mach.Intell.,vol.44,no.9,pp.4555–4576, Techniques for disease prediction, personalized treatment, and patient
Sep.2022. monitoring,’’J.Bioinf.Artif.Intell.,vol.1,no.1,pp.309–343,2021.
[27] R.M.Samant,M.R.Bachute,S.Gite,andK.Kotecha,‘‘Framework [48] G.Cohen,‘‘Algorithmictradingandfinancialforecastingusingadvanced
for deep learning-based language models using multi-task learning in artificial intelligence methodologies,’’ Mathematics, vol. 10, no. 18,
naturallanguageunderstanding:Asystematicliteraturereviewandfuture p.3302,Sep.2022.
directions,’’IEEEAccess,vol.10,pp.17078–17097,2022. [49] S.P.Pattyam,‘‘Ai-drivenfinancialmarketanalysis:Advancedtechniques
[28] J. Arroyo, C. Manna, F. Spiessens, and L. Helsen, ‘‘An open-AI forstockpriceprediction,riskmanagement,andautomatedtrading,’’Afr.
gym environment for the building optimization testing (BOPTEST) J.Artif.Intell.Sustain.Develop.,vol.1,no.1,pp.100–135,2021.
framework,’’inProc.BuildingSimul.Conf.,Sep.2021,pp.175–182. [50] L.T.Khrais,‘‘Roleofartificialintelligenceinshapingconsumerdemand
[29] Y.Song,A.Wojcicki,T.Lukasiewicz,J.Wang,A.Aryan,Z.Xu,M.Xu, inE-commerce,’’FutureInternet,vol.12,no.12,p.226,Dec.2020.
Z.Ding,andL.Wu,‘‘Arena:Ageneralevaluationplatformandbuilding [51] R.Fedorko,!.Král,andR.Ba"ík,‘‘ArtificialintelligenceinE-commerce:
toolkitformulti-agentintelligence,’’inProc.AAAIConf.Artif.Intell., Aliteraturereview,’’inProc.Congr.Intell.Systems(CIS),vol.2.Cham,
Apr.2020,vol.34,no.5,pp.7253–7260. Switzerland:Springer,Jan.2022,pp.677–689.
[30] X.Kong,G.Wang,andA.Nichol,ConversationalAIWithRasa:Build, [52] Z. M. Çınar, A. A. Nuhu, Q. Zeeshan, O. Korhan, M. Asmael,
Test,andDeployAI-powered,Enterprise-gradeVirtualAssistantsand and B. Safaei, ‘‘Machine learning in predictive maintenance towards
Chatbots.Birmingham,U.K.:PacktPublishingLtd,2021. sustainablesmartmanufacturinginindustry4.0,’’Sustainability,vol.12,
[31] V. Heilala, P. Jääskelä, M. Saarela, and T. Kärkkäinen, ‘‘Adapting no.19,p.8211,Oct.2020.
teaching and learning in higher education using explainable Student [53] A. Johnson, L. Bulgarelli, T. Pollard, S. Horng, L. A. Celi, and
agencyanalytics,’’inPrinciplesandApplicationsofAdaptiveArtificial R.Mark.(2020).Mimic-iv.Accessed:Aug.23,2021.[Online].Available:
Intelligence.Hershey,PA,USA:IGIGlobal,2023,pp.20–51. PhysioNet.:https://physionet.org/content/mimiciv/1.0/
[32] B.Abedin,C.Meske,I.Junglas,F.Rabhi,andH.R.Motahari-Nezhad, [54] M. Hammad, A. A. A. El-Latif, A. Hussain, F. E. A. El-Samie,
‘‘Designingandmanaginghuman-AIinteractions,’’Inf.Syst.Frontiers, B. B. Gupta, H. Ugail, and A. Sedik, ‘‘Deep learning models for
vol.24,no.3,pp.691–697,Jun.2022. arrhythmia detection in IoT healthcare applications,’’ Comput. Electr.
[33] C.Fang,J.N.Wilkenfeld,N.Navick,andJ.L.Gibbs,‘‘‘Aiamhere Eng.,vol.100,May2022,Art.no.108011.
torepresentyou’:Understandinghowinstitutionallogicsshapeattitudes [55] M.J.Awan,M.S.M.Rahim,H.Nobanee,A.Munawar,A.Yasin,and
toward,’’Manage.Commun.Quart.,vol.37,no.4,pp.941–970,2023. A.M.Z.Azlanmz,‘‘Socialmediaandstockmarketprediction:Abig
[34] S.Hu,C.Lu,andJ.Clune,‘‘Automateddesignofagenticsystems,’’2024, dataapproach,’’Comput.,Mater.Continua,vol.67,no.2,pp.2569–2583,
arXiv:2408.08435. 2021.
[35] A.BairdandL.M.Maruping,‘‘ThenextgenerationofresearchonISuse: [56] P.Li,A.Kusari,andD.J.LeBlanc,‘‘Anoveltrafficsimulationframework
AtheoreticalframeworkofdelegationtoandfromagenticISartifacts,’’ for testing autonomous vehicles using SUMO and CARLA,’’ 2021,
MISQuart.,vol.45,no.1,pp.315–341,2021. arXiv:2110.07111.
[36] J. J. Woo, A. J. Yang, R. J. Olsen, S. S. Hasan, D. H. Nawabi, [57] I. Han, D.-H. Park, and K.-J. Kim, ‘‘A new open-source off-road
B. U. Nwachukwu, R. J. Williams, and P. N. Ramkumar, ‘‘Custom environmentforbenchmarkgeneralizationofautonomousdriving,’’IEEE
largelanguagemodelsimproveaccuracy:Comparingretrievalaugmented Access,vol.9,pp.136071–136082,2021.
generation and artificial intelligence agents to noncustom models for [58] F.Mauthe,S.Hagmeyer,andP.Zeiler,‘‘Creationofpubliclyavailable
evidence-based medicine,’’ Arthroscopy, J. Arthroscopic Rel. Surg., datasetsforprognosticsanddiagnostics(Don’tshort)addressingdata
Nov.2024. scenariosrelevanttoindustrialapplications,’’Int.J.PrognosticsHealth
[37] E.Yang,T.Garcia,H.Williams,B.Kumar,M.Ramé,E.Rivera,Y.Ma, Manage.,vol.12,no.2,pp.1–6,Nov.2021.
J.Amar,C.Catalani,andY.Jia,‘‘Frombarrierstotactics:Abehavioral [59] Y.A.Yucesan,A.Dourado,andF.A.C.Viana,‘‘Asurveyofmodeling
science-informedagenticworkflowforpersonalizednutritioncoaching,’’ forprognosisandhealthmanagementofindustrialequipment,’’Adv.Eng.
2024,arXiv:2410.14041. Informat.,vol.50,Oct.2021,Art.no.101404.
18934 VOLUME13,2025

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
[60] G.Wang,Y.Xie,Y.Jiang,A.Mandlekar,C.Xiao,Y.Zhu,L.Fan,and [80] S.Saha,Z.Gan,L.Cheng,J.Gao,O.L.Kafka,X.Xie,H.Li,M.Tajdari,
A.Anandkumar,‘‘Voyager:Anopen-endedembodiedagentwithlarge H.A.Kim,andW.K.Liu,‘‘Hierarchicaldeeplearningneuralnetwork
languagemodels,’’2023,arXiv:2305.16291. (HiDeNN):Anartificialintelligence(AI)frameworkforcomputational
[61] G.SartorandF.Lagioiaetal.,‘‘Theimpactofthegeneraldataprotection scienceandengineering,’’Comput.MethodsAppl.Mech.Eng.,vol.373,
regulation(GDPR)onartificialintelligence,’’Tech.Rep.,2020. Jan.2021,Art.no.113452.
[62] F. Miao, W. Holmes, R. Huang, and H. Zhang, AI and Education: A [81] A.Z.Tan,H.Yu,L.Cui,andQ.Yang,‘‘Towardspersonalizedfederated
GuidanceforPolicymakers.Paris,France:UnescoPublishing,2021. learning,’’ IEEE Trans. Neural Netw. Learn. Syst., vol. 34, no. 12,
[63] A.V.S.Neto,J.B.Camargo,J.R.Almeida,andP.S.Cugnasca,‘‘Safety pp.9587–9603,Dec.2022.
assuranceofartificialintelligence-basedsystems:Asystematicliterature [82] Y.Shi,K.Yang,T.Jiang,J.Zhang,andK.B.Letaief,‘‘Communication-
review on the state of the art and guidelines for future work,’’ IEEE efficient edge AI: Algorithms and systems,’’ IEEE Commun. Surveys
Access,vol.10,pp.130733–130770,2022. Tuts.,vol.22,no.4,pp.2167–2191,4thQuart.,2020.
[64] G. S. Collins, P. Dhiman, C. L. Andaur Navarro, J. Ma, L. Hooft, [83] F.Saeik,M.Avgeris,D.Spatharakis,N.Santi,D.Dechouniotis,J.Violos,
J. B. Reitsma, P. Logullo, A. L. Beam, L. Peng, B. Van Calster, A.Leivadeas,N.Athanasopoulos,N.Mitton,andS.Papavassiliou,‘‘Task
M.vanSmeden, R. D. Riley, and K. G. Moons, ‘‘Protocol for devel- offloading in edge and cloud computing: A survey on mathematical,
opment of a reporting guideline (TRIPOD-AI) and risk of bias tool artificial intelligence and control theory solutions,’’ Comput. Netw.,
(PROBAST-AI)fordiagnosticandprognosticpredictionmodelstudies vol.195,Aug.2021,Art.no.108177.
basedonartificialintelligence,’’BMJOpen,vol.11,no.7,Jul.2021, [84] M. Capra, B. Bussolino, A. Marchisio, G. Masera, M. Martina, and
Art.no.e048008. M. Shafique, ‘‘Hardware and software optimizations for accelerating
[65] A. Biswas and W. Talukdar, ‘‘Guardrails for trust, safety, and ethical deepneuralnetworks:Surveyofcurrenttrends,challenges,andtheroad
developmentanddeploymentoflargelanguagemodels(LLM),’’J.Sci. ahead,’’IEEEAccess,vol.8,pp.225134–225180,2020.
Technol.,vol.4,no.6,pp.55–82,Nov.2023. [85] A. Abid, M. F. Manzoor, M. S. Farooq, U. Farooq, and M.Hussain,
[66] W.Cai,J.Wang,P.Jiang,L.Cao,G.Mi,andQ.Zhou,‘‘Application ‘‘Challenges and issues of resource allocation techniques in cloud
ofsensingtechniquesandartificialintelligence-basedmethodstolaser computing,’’ KSII Trans. Internet Inf. Syst. (TIIS), vol. 14, no. 7,
welding real-time monitoring: A critical review of recent literature,’’ pp.2815–2839,2020.
J.Manuf.Syst.,vol.57,pp.1–18,Oct.2020. [86] R. Ranjan, N. Vemuri, and K. Venigandla, ‘‘Autonomous devops:
[67] S.Saponara,A.Elhanashi,andA.Gagliardi,‘‘Implementingareal-time, IntegratingRPA,AI,andMLforself-optimizingdevelopmentpipelines,’’
AI-based,peopledetectionandsocialdistancingmeasuringsystemfor Asian J. Multidisciplinary Res. Rev., vol. 3, no. 2, pp.214–231,
covid-19,’’J.Real-TimeImageProcess.,vol.18,no.6,pp.1937–1947, 2022.
Dec.2021. [87] J.Paschen,M.Wilson,andJ.J.Ferreira,‘‘Collaborativeintelligence:
[68] E. Mosqueira-Rey, E. Hernández-Pereira, D. Alonso-Ríos, HowhumanandartificialintelligencecreatevaluealongtheB2Bsales
J.Bobes-Bascarán, and Á. Fernández-Leal, ‘‘Human-in-the-loop funnel,’’Bus.Horizons,vol.63,no.3,pp.403–414,May2020.
machinelearning:Astateoftheart,’’Artif.Intell.Rev.,vol.56,no.4, [88] A.Brohanetal.,‘‘RT-2:Vision-Language-actionmodelstransferWeb
pp.3005–3054,Apr.2023. knowledgetoroboticcontrol,’’2023,arXiv:2307.15818.
[69] K.Kuru,‘‘Conceptualisationofhuman-on-the-loophapticteleoperation [89] S.HuandJ.Clune,‘‘Thoughtcloning:Learningtothinkwhileacting
with fully autonomous self-driving vehicles in the urban environ- byimitatinghumanthinking,’’inProc.Adv.NeuralInf.Process.Syst.,
ment,’’ IEEE Open J. Intell. Transp. Syst., vol. 2, pp.448–469, Jan.2023,pp.1–18.
2021. [90] J.X.Wang,‘‘Meta-learninginnaturalandartificialintelligence,’’Current
[70] D. Gunning, M. Stefik, J. Choi, T. Miller, S. Stumpf, and G. Yang, OpinionBehav.Sci.,vol.38,pp.90–95,Apr.2021.
‘‘XAI—Explainableartificialintelligence,’’Sci.Robot.,vol.4,no.37, [91] R. Mehrotra, M. A. Ansari, R. Agrawal, and R. S. Anand, ‘‘A
p.7120,Dec.2019. transferlearningapproachforAI-basedclassificationofbraintumors,’’
[71] D. B. Acharya, B. Divya, and K. Kuppan, ‘‘Explainable and fair Mach.Learn.Appl.,vol.2,Dec.2020,Art.no.100003.
AI: Balancing performance in financial and real estate machine [92] H. Lee, J. Kim, J. Park, and S. Kang, ‘‘STRAIT: Self-test and self-
learning models,’’ IEEE Access, vol. 12, pp.154022–154034, recoveryforAIaccelerator,’’IEEETrans.Comput.-AidedDesignIntegr.
2024. CircuitsSyst.,vol.42,no.9,pp.3092–3104,2023.
[72] T. Weise and Z. Wu, ‘‘Replicable self-documenting experiments with [93] A. K. Y. Yanamala and S. Suryadevara, ‘‘Adaptive middleware
arbitrary search spaces and algorithms,’’ in Proc. Companion Conf. framework for context-aware pervasive computing environments,’’
GeneticEvol.Comput.,Jul.2023,pp.1891–1899. Int. J. Mach. Learn. Res. Cybersecurity Artif. Intell., vol. 13, no. 1,
[73] P.B.deLaat,‘‘CompaniescommittedtoresponsibleAI:Fromprinciples pp.35–57,2022.
towardsimplementationandregulation?’’PhilosophyTechnol.,vol.34, [94] D.Driessetal.,‘‘PaLM-E:Anembodiedmultimodallanguagemodel,’’
no.4,pp.1135–1193,Dec.2021. 2023,arXiv:2303.03378.
[74] K.Michael,R.Abbas,G.Roussos,E.Scornavacca,andS.Fosso-Wamba, [95] Y.Huang,C.Du,Z.Xue,X.Chen,H.Zhao,andL.Huang,‘‘Whatmakes
‘‘EthicsinAIandautonomoussystemapplicationsdesign,’’IEEETrans. multi-modallearningbetterthansingle(Provably),’’inProc.Adv.Neural
Technol.Soc.,vol.1,no.3,pp.114–127,Sep.2020. Inf.Process.Syst.,Jan.2021,pp.10944–10956.
[75] M.Metta,S.Ciliberti,C.Obi,F.Bartolini,L.Klerkx,andG.Brunori,‘‘An [96] N.Balasubramaniam,M.Kauppinen,A.Rannisto,K.Hiekkanen,and
integratedsocio-cyber-physicalsystemframeworktoassessresponsible S.Kujala,‘‘TransparencyandexplainabilityofAIsystems:Fromethical
digitalisation in agriculture: A first application with living labs in guidelines to requirements,’’ Inf. Softw. Technol., vol. 159, Jul. 2023,
Europe,’’Agricult.Syst.,vol.203,Dec.2022,Art.no.103533. Art.no.107197.
[76] E. Zelikman, Y. Wu, and N. D. Goodman, ‘‘STaR: Bootstrapping [97] F. Santoni De Sio and G. Mecacci, ‘‘Four responsibility gaps with
reasoning with reasoning,’’ in Proc. Adv. Neural Inf. Process. Syst., artificial intelligence: Why they matter and how to address them,’’
Jan.2022,pp.15476–15488. PhilosophyTechnol.,vol.34,no.4,pp.1057–1084,Dec.2021.
[77] E.Emanuel,G.Persad,A.L.Kern,A.Buchanan,C.Fabre,D.Halliday, [98] N.A.Smuha,‘‘Froma‘racetoAI’toa‘racetoAIregulation’:Regulatory
J.Heath,L.Herzog,R.J.Leland,E.T.Lemango,F.Luna,M.S.McCoy, competitionforartificialintelligence,’’SSRNElectron.J.,vol.13,no.1,
O. F. Norheim, T. Ottersen, G. O. Schaefer, K. Tan, C. H. Wellman, pp.57–84,2021.
J. Wolff, and H. S. Richardson, ‘‘An ethical framework for global [99] C.SmallandC.Lew,‘‘Mindfulness,moralreasoningandresponsibility:
vaccine allocation,’’ Science, vol. 369, no. 6509, pp.1309–1312, Towardsvirtueinethicaldecision-making,’’J.Bus.Ethics,vol.169,no.1,
Sep.2020. pp.103–117,Feb.2021.
[78] S.S.Sundar,‘‘Riseofmachineagency:Aframeworkforstudyingthe [100] A.Langdon,M.Botvinick,H.Nakahara,K.Tanaka,M.Matsumoto,and
psychology of Human–AI interaction (HAII),’’ J. Computer-Mediated R.Kanai,‘‘Meta-learning,socialcognitionandconsciousnessinbrains
Commun.,vol.25,no.1,pp.74–88,Mar.2020. andmachines,’’NeuralNetw.,vol.145,pp.80–89,Jan.2022.
[79] L. Cao, ‘‘Decentralized AI: Edge intelligence and smart blockchain, [101] V.Lai,C.Chen,Q.V.Liao,A.Smith-Renner,andC.Tan,‘‘Towardsa
metaverse,Web3,andDeSci,’’IEEEIntell.Syst.,vol.37,no.3,pp.6–19, scienceofhuman-AIdecisionmaking:Asurveyofempiricalstudies,’’
May2022. 2021,arXiv:2112.11471.
VOLUME13,2025 18935

D.B.Acharyaetal.:AgenticAI:AutonomousIntelligenceforComplexGoals—AComprehensiveSurvey
DEEPAKBHASKARACHARYA(SeniorMember, B. DIVYA receivedtheBachelorofEngineering
IEEE) received the Master of Science degree in (B.E.) degree in electronics and communica-
computerscienceandthePh.D.degreefromThe tionengineeringfromVisvesvarayaTechnological
UniversityofAlabamainHuntsville(UAH). University (VTU), Belagavi, and the Master of
He is currently a Scholar and a Teacher Technology(M.Tech.)degreeinsignalprocessing
with distinguished research experience in the from the Siddaganga Institute of Technology,
field of machine learning, deep learning, and Tumakuru. She is currently pursuing the Ph.D.
computer science applications. He is a Principal degree in biomedical image processing with
ResearchScientistwiththeInformationTechnol- NITK,Surathkal.
ogy and Systems Center, UAH. He has applied SheholdsthepositionofanAssistantProfessor
advancedmachinelearningtechniques,especiallyinNASA-fundedprojects, with the Department of Electronics and Communication Engineering,
todevelopsuper-resolutiontoolsforprecipitationdataandEarthobservation Manipal Institute of Technology, Manipal. This specific knowledge of
systemstoaddresspublichealthissuesinSub-SaharanAfrica.Hehasused electronicsandsignalprocessingandherqualificationsmadehersuccessful
his proficiency in ML models to solve many novel domain problems in intheacademicandresearchareas.Herteachingcareerspansover14years,
patternrecognition,predictiveanalytics,anddata-drivendecision-making. whichisoneofthefactorsthathasearnedherareputationfordedication
HeunderstandsthetheoreticalaspectsofMLalgorithmsandthepractical and passion toward her profession. She helps students hone their critical
challengesofimplementingtheminreal-worldproblems.Healsoteaches and analytical skills and ensures that the latest technology is included in
part-time with the UAH’s Computer Science Department. He mentors thesyllabusasneeded.Herexpertiseincludesappliedtechnologysubparts,
graduateandundergraduatestudentsandservesonacademicreviewboards suchasmachinelearning(ML),deeplearning(DL),andsignalprocessing,
forseveraltop-notchjournals,helpingtofurtherthefieldofAIandcomputer to which she also actively contributes research and development. She
science.Withadvancedtechnicalskillsinengineeringlanguages,including has taken part in a number of projects, which implement ML and DL
Python, C++, and Java, as well as in frameworks, such as React JS, technologies for enhancing image analysis, data analysis, and prediction.
hesitsonthecuspoftheoreticalresearchandpracticaldevelopment.His Alltheseeffortsaimtobuildmoreefficientandprecisesystemsthatcanbe
multidisciplinaryapproachmakeshimuniquelyplacedtoadvanceindustrial usedinpractice,particularlyinthebiomedicalfield.Sheisverypassionate
applicationsofAIaswellasacademicresearch,withhisworkattheleading aboutapplyingmachinelearningtosolvereal-worldproblemsinhealthcare.
edgeofinnovation.Heworkstoempowertalent,developAIbreakthroughs, She is actively participating in the academic community undertaking the
andfosterresponsibleAIinseveralsectors.Hisareasofresearchinterests responsibilitiesofamentor,conductingresearch,andactivelylearningthe
include machine learning (ML) and deep learning (DL), including graph newtoolsandtheoriesintheareaofmachinelearninganddeeplearning
neuralnetworks,clusteringtechniques,andGumbel-Softmaxdistribution. technologies. Her research interests include machine learning and efforts
relatedtosignalprocessingandbiomedicalimageprocessing.
KARTHIGEYAN KUPPAN (Senior Member,
IEEE) received the Master of Computer Appli-
cations (M.C.A.) degree from Anna University,
while perfecting his computer science and
softwareengineeringskills.
He is currently the Vice President and the
Senior Manager of software engineering with
more than 17 years of experience in designing,
developing, and integrating complex software
systems in multiple industries. Understanding
multipletechnologies,suchasJava,Python,machinelearning,andcloud,
hecanproducenewsystemstomeettoday’sneedswhileaddressingfuture
scalability and efficiency. He is a Team Leader with multiple years of
experience managing cross-functional teams to deliver projects meeting
technicalrequirementsandbusinessgoals.Throughouthiscareer,heand
histeamhaveachievedthehigheststandardsinthedeliveryofITservices,
achievingseverallargegovernmentprojects.Theyretainedtheirleadership
positioninthedevelopmentofnewITsolutionsduetothetendencytofollow
orpredictthedevelopmentofnewtechnologicalsolutions.Thegoalisto
buildthesesolutionsinsuchawaythattheyarehighlyreliable,secureas
wellasconfigurabletocatertofutureincreaseddemand.Heisalife-long
learner,aself-starter,andatruehigh-potentialprofessionalwithapenchant
forcontinuouslearningandgrowth.Hispassionfornewopportunitieshasled
himtoparticipateinmultipleopen-sourcesoftwareprojectsandfurtherhis
knowledgeinthefieldofknowledgemanagementthroughthecompletionof
hismaster’sdegree.Moreover,hehasservedasamentorwiththeguidance
ofpersistenceanddedicationthathasinfluencedmanyinternstudents.His
visionary approach to problem-solving and passion for innovation have
garneredhimindustryinfluence.
18936 VOLUME13,2025
