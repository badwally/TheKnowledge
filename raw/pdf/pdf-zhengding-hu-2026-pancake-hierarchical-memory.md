---
id: pdf-zhengding-hu-2026-pancake-hierarchical-memory
type: pdf
title: 'Pancake: Hierarchical Memory System for Multi-Agent LLM Serving'
url: ''
authors:
- Zhengding Hu
- Zaifeng Pan
- Prabhleen Kaur
- Vibha Murthy
- Zhongkai Yu
- Yue Guan
- Zhen Wang
- Steven Swanson
- Yufei Ding
ingested_at: '2026-04-29T16:19:07Z'
content_hash: sha256:edf7510dbfd04aca8db4e14c3a60a62e609fd8b604f9561bc35c7d57c974e7f4
source_path: raw/pdf/pdf-zhengding-hu-2026-pancake-hierarchical-memory.pdf
domains:
- ai-and-agents
nlm_corpus_ids:
- 7eac1296-b611-422e-85bb-6c36f5c8872b
wiki_pages:
- wiki/entities/pancake-system.md
- wiki/entities/zhengding-hu.md
- wiki/entities/yufei-ding.md
- wiki/entities/steven-swanson.md
- wiki/entities/uc-san-diego.md
- wiki/entities/mem-gpt.md
- wiki/entities/a-mem.md
- wiki/concepts/agentic-memory.md
- wiki/concepts/approximate-nearest-neighbor-search.md
- wiki/concepts/multi-tier-memory-system.md
- wiki/concepts/intra-agent-locality.md
- wiki/concepts/step-wise-memory-locality.md
- wiki/concepts/scattered-cluster-problem.md
meta:
  page_count: 17
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__e939804a.pdf
published_at: '2026'
---
Pancake: Hierarchical Memory System for Multi-Agent LLM Serving
ZhengdingHu,ZaifengPan,PrabhleenKaur,VibhaMurthy,ZhongkaiYu,YueGuan,
ZhenWang,StevenSwanson,YufeiDing
Hitory Knowledge Recall
ComputerScienceandEngineering,UniversityofCalifornia,SanDiego
Hitory Knowledge Recall
Hitory Knowledge Recall Uer Query
Abstract
Inthiswork,weidentifyandaddressthecorechallengesof
agenticmemorymanagementinLLMserving,wherelarge-
scalestorage,frequentupdates,andmultiplecoexistingagents
jointlyintroducecomplexandhigh-costapproximatenearest
neighbor(ANN)searchingproblems.WepresentPancake,a
Memory
multi-tieragenticmemorysystemthatunifiesthreekeytech-
niques:(i)multi-levelindexcachingforsingleagents,(ii)co-
ordinatedindexmanagementacrossmultipleagents,and(iii) Tak Planning Knowledge
Code Generation Action Hitory
collaborativeGPU–CPUacceleration.Pancakeexposeseasy-
Scientific Reearch Uer profile
to-use interface that can be integrated into memory-based LLM Agent Memory Database
agentslikeMem-GPT,andiscompatiblewithagenticframe-
Figure1:Memory-basedworkflowofagenticLLMs.
workssuchasLangChainandLlamaIndex.Experimentson
realisticagentworkloadsshowthatPancakesubstantiallyout-
performs existing frameworks,achieving more than 4.29!
generationthroughoutLLMinference,whilealsodynamically
end-to-endthroughputimprovement.
insertingnewlygenerateditemsforfuturereference.
AgentMemoryenablesreliable,consistent,andprogres-
1 Introduction sively refined agent outputs over complex tasks. Yet,such
a continuous memory mechanism also introduces a highly
Agentshaveemergedasoneofthedefiningparadigmsofthe dynamic database environment that demands frequent ap-
LLMera,enablingcomplextaskscenariosincludingtaskplan- proximatenearest-neighbor(ANN)operations[40],typically
ning[25,58],knowledgeorganization[5,18],tool-augmented implementedthroughembeddingvectorindexes[23].Such
generation [57,76] and even scientific researches [47,64]. operationsintroduceanewandsubstantialsourceofoverhead
Thesecomplextasks,oftencarriedoutthroughmulti-turnen- inagentservingwhentheindexscalebecomeslarge.
vironmentinteraction[77],self-reflection[59],ormulti-agent Existing agentic memory implementations largely focus
collaboration[39],hasintroducedsubstantialinformationinto on functional support while lacking performance-oriented
thegenerationprocessandposessignificantchallengesfor optimization. As shown in Figure 1, for popular memory-
contextlengthandattentionfidelity[45]. basedworkflows[53,73],thememoryoperationalcostgrows
Inresponsetothistrend,AgentMemory[82]hasemerged sharplywithmemorysize,reachingmorethan82%oftheto-
asakeymechanismtomanagecomplexcontextsandenhance talexecutiontime.Meanwhile,mostexistingvectordatabase
generationquality.UnlikepriorRetrieval-AugmentedGener- systemsfallshortinsupportingagenticmemory:theyeither
ation(RAG)methods[5,29,30,37,38,71],whichrelyona optimizeonlyastaticindex[9,17,26,72,81],orrelyonbatch-
staticknowledgedatabaseandlacktheabilitytocapturean orientedupdates[49,50,60,74]designedforperiodicmain-
agent’sruntimestate,results,andotherdynamicinformation, tenanceintraditionaldatabases[63],makingthemill-suited
agent memory maintains an external database that records forhighlydynamicandfine-grainedmemoryoperations.
essentialinformation,includingexternalknowledge[30,53], Inthiswork,wepresentPancake,amulti-tiermemoryman-
actionhistory[73,88],userprofile[21,67],andmore.The agementsystem designed to address the key challenges of
agentmustretrievethemostrelevantmemoryitemstoguide implementinganagenticmemorysystem:
1
6202
beF
52
]AM.sc[
1v77412.2062:viXra

Agent 1: Information Query Index 1 throughasinglegraphtraversal.Pancakealsorecordsagent-
D = mm.Search(1 ) Wiki Knowledge specificaccesspatternsforeachcluster,toreducecross-agent
# RAG with D (Fully Shared) searchoverheadcausedbyinconsistentaccesspatterns.
Title: Program Guide
Content: How to write Forprogrammabilityinmulti-agentapplications,Pancake
Agent 2: Task Planner Python code…
providesasimplePythoninterfacethatsupportsoperations
M1 = mm.Search([1 ,2 ,3 ])
# P = Plan with Mem overarbitrarymemoryscopes,includingdifferentsharedand
Index 2
mm.Insert(P, 3 ) localmemoryparts,whichexistingframeworksdonotoffer.
Code Snippets
(Partially Shared) Figure2showsamulti-agentcode-generationsetup,where
Agent 3: Coding Code: def A(x, y): differentagentsflexiblyoperateoverknowledge,code,and
M2 = mm.Search([1 ,2 ]) return x + y
# C = Code with M2 Execute Result: {0.4} historymemorieswithPancakeinterface.
mm.Update(C,2) Third, modern LLM serving systems are typically de-
Index 3 ployedatGPU-CPU platforms [36,86],whichcreates an
Agent 4: Validator Action History
(Partially Shared) opportunitytoacceleratememoryoperations.Existingvector
# R = Improvement with P
History: Value ={0.4} databases can only reside entirely on the GPU [32,33],or
mm.Delete(P,2 ) New Plan:
mm.Insert(R,3 ) New funcshould be … GPU caching mechanism for static indexes [61,84]. How-
ever,in agenticservingscenarios,thecoexistence oflarge-
Figure2:Anexampleofmulti-agentmemoryinPancake. scalememorybases[53]andLLMinferenceengineseverely
restrictsavailableGPUmemory.Moreimportantly,thefre-
quentmemoryupdatesmakesstaticcachingtechniquesin-
First,forasingleagent,akeylimitationofexistingvec- feasibletoapply.Tofullyutilizeresources,Pancakeimple-
tor search systems is their inability to efficiently handle ments CPU–GPU coordinatedindexmanagementto accel-
thefrequent,fine-grainedupdatescharacteristicofmemory erate hotspot cluster computation,with an insertion buffer
workloads [53,73]. Existing incremental indexing meth- designandasynchronoustransfersforlow-latencyonlineup-
ods [49,74] are designed for large-batch insertions in tra- dates.
ditionaldatabases[34,63]andrelyondirectin-placeinserts Insummary,thecontributionofthispaperisasfollows:
withperiodic rebalancing. Underthe small-batchinsertion
patternsandinterleavedsearchofagentworkloads,inserted • WeintroducePancake,thefirstmulti-tiermemoryman-
vectorsareoftenscatteredacrossvariousclustersduetohigh- agement system tailored for multi-agent applications.
dimensionaldistanceconcentration[20]despitestrongseman- Pancakeexploitsagentworkloadcharacteristicstoop-
ticcoherence,degradingbothsearchefficiencyandrecall. timizeupdatestrategyforsingle-agentmemory,cluster
Toaddressthisinefficiency,weexplicitlyincorporateagent- constructionformulti-agentcoordination,anddynamic
specificaccessbehaviorsintoindexconstructionandmain- CPU–GPUcollaborativeexecution.
tenance.Specifically,Pancakeexploitsbothintra-agentand
• Pancakecanbedirectlyintegratedintoagentworkflows
inter-requestlocalitythroughamulti-levelcacheindexthat
likeMem-GPT[53]andpluggedintomainstreamagen-
progressively promotes related vectors to upperlevels,im-
ticframeworkslikeLangChain[1]andLlamaIndex[44].
provingsearchorderingandenablingearlytermination.To
ItprovidesaconciseAPIthroughwhichagentscanper-
guidecachingbehavior,Pancakemodelseachagent’smemory
formmemoryoperationsacrossflexiblememoryscopes.
accesspatternasfinite-statemachine(FSMs)withcontinuous
updating and merging,enabling index cluster construction • Extensive experiments across diverse agent datasets
closelyalignedwiththeagent’sworkload. showthatPancakedeliversover4.29 averageend-to-
→
Second,supportingmulti-agentworkloadsischallenging, endperformancespeedupcomparedwithexistingmem-
astheyfrequentlyinvokedifferentsetsofagentstoperform ory libraries,and reduces the memory-operation time
memorysearchesatruntime[54]. Usingconventionaltwo- sharetoanaverageof3.2%underlarge-scaledatabase.
levelindexstructures[17]whilemaintainingseparateindexes
foreachagentisinefficient. Attheupperlevel,thisdesign
2 BackgroundandRelatedWork
must traverse the coarse index of every agent, even when
onlyasubsetisinvolvedinthequery,leadingtoexcessive
2.1 Memory-basedAgentandANN
coarse-searchoverhead.Atthelowerlevel,itusesuniform
clustersforthesharedmemorypart,ignoringtheinconsistent A memory-basedagenttypically perform three operations:
accesspatternsacrossagents,thuscausingmisalignedcluster LLMGeneration;MemorySearch,whichretrievesitemsrele-
organizationandinefficientfine-grainedsearch. vanttothecurrentcontext;andMemoryUpdate,whichinserts,
Pancake addresses these challenges witha hybridgraph deletes,ormodifiesitemsinthememorystore.Asshownin
that connects multiple agents’ indexes into a unified struc- Figure3,differentagentrolesinducedifferentoperationpat-
ture,enablingtheupper-levelcoarsesearchtobeperformed terns. For instance, multi-turn dialogue agents search and
2

nprobeatunableaccuracy–efficiencytrade-off[56].Were-
LLM generation Memory operation
fer to cluster selection as coarse search,and to the search
withintheselectedclustersasfinesearch.Coarsesearchtyp-
Plan Refine
icallyreliesonaFlatindexorgraph-basedindexessuchas
Multi-Turn Search Update Search Update HNSW[48]orVamana[26]inlarge-scalesettings.
Dialogue Interleaved search / update However,existingframeworksareprimarilydesignedfor
Step 1 Step 2 … Step N read-onlyscenarioslikeRAG,andthereforeassumeastatic
vectordatabasewithone-shot,full-indexconstruction.Such
Search Search Update
Long-Context designs are incompatible with agentic memory workloads,
Summarization Multiple search with one update
where frequent updates make reconstruction prohibitively
Action 1 Action 2 … expensive.Tosupportonlineupdates,severaldynamicvector-
Search Update Update databasetechniqueshavebeenproposed[49,50,60,70,74].
Personalized
Generation Single search with multiple update Forexample,SPFresh[74]avoidsglobalrebuildingthrough
in-place inserts and lightweight local rebalancing, while
Gen 1 Gen2 …
Quake [50] uses a hierarchical cluster structure and adap-
Search Search Search tively splits clusters based on access frequency. However,
Knowledge
Retriever Search only thesedesignstypicallyassumeperiodic,batch-orientedup-
datesconsistentwithtraditionaldatabaseworkloads[35,63].
Figure3:Memory-basedagentsandtheirworkflows. Incontrast,agenticmemoryservinginvolveshighlyfrequent
updatesthatinterleavecloselywithsearchoperations,leading
todegradedefficiencyandaccuracyinsuchsystems.
updatememoryateverysteptoremainconsistentwiththe
interactionhistory[53,78],whereascontext-summarization
3 Motivation
agentssearchandgenerateforseveralroundsandtheninsert
acompressedmemoryitem[10,52,79].
3.1 Inefficient Update Strategy for Single-
These search and update memory operations inherently
introduce requirements for approximate nearest neighbor AgentMemoryAccess
(ANN)queries.ANNistypicallyimplementedthroughvector
Inthissection,weanalyzesingle-agentmemoryaccesspat-
databases,wheretextualinformationisencodedintovector
ternsandshowthatexistingvectordatabasemaintenanceal-
embeddings [14,66] and relevance is quantized based on
gorithmsstruggletoefficientlyhandlefrequent-updatework-
vectorsimilarities[11].SuchANNqueriesoccurrepeatedly
loads.Intypicalagent-servingsystems,anagentprocesses
throughoutanagent’sstep-wisegeneration,theirlatencyand
manyindependentrequests,eachinvolvingmulti-stepLLM
accuracythereforebecomeincreasinglycriticaltotheoverall
generationandfrequentinterleavedsearch–insertoperations.
performanceofmodernLLMservingsystems.
Examplesincludecodingagentsreceivingcontinuoususer
To support memory operations, existing memory-based
tasks [75] and scientific agents analyzing large batches of
agents such as Mem-GPT [53] and A-Mem [73] provide
experimentaldata[80].
theirownmemoryimplementations,andopen-sourcedagent
Forvectorinsertionduringmemoryupdates,existingdy-
frameworks like LlamaIndex [44] and LangChain [1] also
namicvectordatabases[49,50,74]typicallyadoptin-placein-
offerbuilt-instorageinterfaces.However,thesemodulesem-
sertswithperiodicupdates,asshowninFigure4.Newvectors
phasize functionality and rely on suboptimal indexing and
areinserteddirectlyintothenearestclusters,withdistances
searchingimplementations.Asthememorysizegrows,their
calculatedbetweentheclustercentroids. Reconstructionis
querylatencyincreasessharply,reachingmorethan99%of
triggeredonlywhenthesizeorthesemanticshift[49]ofthe
theend-to-endruntimeatscale.Thistrendhighlightstheneed
clusterreachesathreshold.Thisstrategyiseffectiveforlarge-
forascalableandefficientagenticmemoryframework.
batchscenarios,whilebecomessuboptimalwithinterleaved
small-batchsearchandinsertoperations.
2.2 DynamicVectorDatabase Scattered ClusterProblem of In-Place Insertion. A key
issue of in-place insertion is that new vectors inserted
Numerousvector-databaseframeworks[9,17,22,26,65]have into a large pre-clustered index often get scattered across
exploredtechniquesforefficientsearchbyorganizingvectors many clusters,even when they are semantically close. As
into structuredstorage formats,known as indexes. Among showninFigure4(a),across100requestsfromseveralagent
them,the Inverted File (IVF) index [27] is widely used: it datasets[13,15,46],memoryitemsfromthesameagentare
partitionvectorsintoclustersandranktheseclustersbythe dispersedintoupto175clusters,with38%–100%ofthese
distancebetweentheircentroidsandthequery.Onlythetop- clusters being accessed with frequency less than 5%. This
nprobeclustersareselectedforvector-wisesearch,making behaviorstemsfromthehigh-dimensionalshelleffect[3,6],
3

R1 R2 Requests Cluster Centroid R1 R2 Requests Cluster Centroid
Memory Access ReasoningChain Memory Access ReasoningSteps
Scattered Cluster
Assignment
R1
R1 R2 Cluster 3
Cluster 1 R2 Cluster 2 Cluster 1
Fail to represent
Naïve Sol: Agent Dedicated Cluster Cluster 2 complex workflows
Figure4:Directin-placeupdatesscatterthenewvectorsinto
Figure5:Formorecomplexworkloads,localityacrossmul-
a large numberof existing clusters,leading to degradation
tiple reasoning steps ofdifferentrequests can be observed.
inefficiencyandrecall.Anaivesolutionistoleverageintra-
Thismakesnaivededicatedclustersfortheagentinefficient,
agentlocalityandmaintaindedicatedclustersforaagent.
asitfailstocapturestep-wiseclustering.
wherepointsconcentratenearthesurfaceofahypersphere, different requests tend to cluster together. For example,in
causingsmallsemanticvariationstotranslateintolargedif- tool-augmentedagents[57],theplanning,tool-calling,and
ferencesincentroiddistancecalculations.Thus,evenhighly reflectionstepsacrossdifferentrequeststendtoaccesssimilar
relatedmemoryitemsmaybeinsertedtodifferentclusters. regionsofmemory.AsshowninFigure5(a),memoryitems
Such scattered cluster assignments bring challenges for belongingtothesamereasoningstepacrossdifferentrequests
both efficiency and accuracy. First, this forces scanning a demonstratehighersimilarity,comparedtotheintra-request
larger number of clusters to retrieve semantically related andintra-agentsimilarity.Figure5(b)furtherillustratesthe
items,incurringextracomputationovermostlyirrelevantvec- clusteringpatternsofmemoryitemsthrough2-dimensional
tors.Second,itemsinsuchscatteredclustersbecomeharder PCAvisualizationinthetool-callingdataset[46]with100
tolocatebycentroiddistances,andtheirclustersmaybeelim- requests,wherethreeclustersemerge,eachcorrespondingto
inatedduringthecoarsesearchstage,leadingtodropinrecall. anindividualstepoftheworkflow.
Totacklethisproblem,wefirststudytwolocalitycharac- This step-wise organization induces frequent transitions
teristicsofagentmemory,whichprovidecriticalguidancefor acrossmultipleclusters.Therefore,althoughmaintaininga
designingeffectiveclusteringstrategies. singlededicatedclusterforeachagentworksforsimplework-
Intra-AgentLocality.AsshowninFigure4(b),requestsin flows in Figure 4,itis insufficientto capture the step-wise
agenticworkflowsinsertmemoryitemsthatremain highly structures in more complicatedscenarios,as shown in Fig-
coherentacrossstepsandacrossrequestsofthesameagent. ure5.Thegreencentroidbecomessemanticallyunrepresen-
Thedistancesbetweeneachitemand(i)thecentroidofthe tative,ultimatelydegradingaccuracyandsearchefficiency.
memoryitemsintherequestand(ii)theaggregatedcentroid Inthiswork,weaimtooptimizetheagentmemoryman-
ofalltheagent’smemoryitemsarebothsubstantiallysmaller agementconsideringbothintra-agentandstep-wiselocality.
thanthedistancestoexistinglargeclustersinthedatabase. Comparedtoexistingapproaches[49,74],Pancakeintroduces
Thisphenomenonisparticularlypronouncedintask-focused moreefficientclusterassignmentandconstructionstrategies
workflows(e.g.,mathematicalreasoning[12]).Astraightfor- thatalignwiththeagent’scomplexmemoryaccesspatterns.
wardstrategyisthereforetoassignadedicatedclustertoeach
agent’sinsertionrequests.However,thisapproachisinsuffi-
3.2 ChallengesforMulti-AgentMemoryIndex
cientinmorecomplexworkflows,wheremulti-stepreasoning
Management
introducescross-steptransitionsthatcannotbecapturedbya
singlecluster(wewilldetailthisinthenextparagraph). Beyondthememoryinefficiencyforasingleagent,weiden-
Inter-Request Step-wise Locality. Beyond intra-agent lo- tify the challenges of effectively managing and searching
cality,morecomplexworkflowsrevealanadditionallayerof acrossmultipleagentmemories,whichisaclearneedforto-
structure:memoryitemsfromthesamereasoningstepacross day’sagenticworkloads.Inatypicalmulti-agentsetting,each
4

(b) Graph-based Coarse Index
(Cost: 7 entroids)
Coarse Index
(HNSW)
12 entroids
Query: Sear h in Stati + Agent 1 + Agent 2 memory Computation
Costs
Agent 1 Stati Multiple Graph Hybrid-Graph
Memory Traversal Traversal
Centroid
Agent 2
Top-1 Cluster
(a) Flat Coarse Index (b) HNSWCoarseIndex (c)   Coarse Index
(Cost: 12 omputations) (Cost: 7 omputations) (Cost: 4 omputations)
Figure6:Coarsesearchcostswithdifferentindexmethods.
Figure8:ComparisonofoperationcostsonGPUandCPU,
including(a)searchtimeand(b)datatransferandallocation.
TheresultsaresampledontAhgeenMt 2SMARCO[51]dataset.
Memory
12 entroids
As shown in Figure 6,when querying two agents and the
staticmemory:(a)usingaFlatindexrequirescomputingthe
distancestoallcentroids,and(b)usingHNSW[48]requires
Sear h Query afulltraversalofthecoarse-indexgraphofeveryagent.
Weobservethatsuchmulti-indexsearchpatternscausea
Figure7:CoarseandFineSearchChallengesinMulti-Agent
significantamplificationofcoarsesearchcostwhenthenum-
Memory. (a) Coarse search overhead grows rapidly as the
berof agents increases. As shown in Figure 7(a),with the
numberofagentsincreases.(b)Whentwoagentsaccessthe
twocommonlyrecommendedFaissindexesforlarge-scale
sameclusterinthestaticmemory,theiraccesspatternsexhibit
settings[17],thecostofcoarse-grainedsearchrisessharply
non-uniform distributiFoinnes; circles denote accessedvectors,
and exceeds 80% of the total latency when the number of
andstarsdenotetheceInndtreoxidsformedbythosevectors.
agentsreaches20.Therefore,itbecomesnecessarytoreor- Ex essive Coarse Sear h Integrated Coarse Index
ganizecoarseindexesacrossagents,therebyreducingsearch
costsduringsearchacrossdifferentagentmemories. Shared Coarse 0
agentcontinuouslyupdatesitslocalmemory,yetmaysearch
Coarse 0
onthememoriesofotheragents.Forexample,ingenerative- Non-Uniform Fine Search Patterns across Agents. We
agentsimulationslikeAITown[54],eachagentrecordsits furtherobservefinesearchinefficiencyduetothedifferent Coarse 1 Coarse 2 Coarse 1 Coarse 2
ownactionandobservationhistories,butreliesoninformation agentmemoryaccesspatterns.AsshowninFigure7(b),when
originatingfromotheragents’memoriestoplanbehaviors multiple agents query the same clusterin a memory index
andcoordinategroupactivities.Becausedifferentagentsbe- (constructedwithstaticmemorybase[53]),thevectorsthey Index 0
comeactiveorinteractatdifferentmoments,thesetofagent accessdiffermarkedlyindistributionandclusteringbehavior. Index 0
Distribution
memoriestosearchalsovariesovertime. Thisdivergencecausestheeffectivecentroidforeachagent
Alignment
This brings a clear demand for memory frameworks to toshiftintheembeddingspace.Thisdivergencecausesthe Index 1 Index 2
support flexible specification of the memory search scope. centroidsformedbyeachagent’saccessedvectorswithinthe
However,existingANNlibraries[9,17,26]onlyprovidein- sameclustertoshiftnoticeablyintheembeddingspace. Index 1 Index 2
terfacesformaintainingandqueryingonasingleindexfora
Thisfindingindicatesthattheoptimalfine-indexorganiza-
givenvectordatabase,whileoffernonativesupportforsearch (a)Individual ( )   : Multi-Index
tionishighlyscope-dependent:forexample,anindexlayout
operationsacrossdifferentvectordatabases.
optimizedforAgent1’saccesspatternmaybepoorlyaligned Management
Astraightforwardapproachistomaintainindependentin-
withAgent2’spattern.Asaresult,Agent1’sclusterorgani-
dexesforeachagent’smemory.Whenqueryingthememories
zationmayforceAgent2tocomputeovermanyirrelevant
of different scopes,the system searches the corresponding
vectorsandpotentiallysufferdegradedrecall.Suchdisalign-
indexesandthenmergestheresults.Althoughthisapproach
mentmakesitnecessaryforcoordinatedorganizationoffine
canbeimplementeddirectlyusingexistinglibraryinterfaces,
indexesacrossmultipleagents.
itsuffersfromsearchefficiencyissues,describedasfollows.
ExcessiveCoarseSearchCost.Large-scalevectorindexes Toaddresstheaboveissues,Pancakeintroducesahybrid
typicallyadoptatwo-stepsearch:acoarsesearchfirstselects graphforefficientcoarsesearchwithinonlyonegraphtraver-
the nearestclusters basedon centroiddistances,anda fine sal,asillustratedinFigure6.Pancakealsoalignsfine-index
searchisthenperformedwithintheselectedclusters.When accessbyassociatingeachclusterwiththepatternrecogni-
independentindexesaremaintainedforeachagent,awide- tionofotheragents,enablingoptimizedcross-agentsearch
scope query must traverse the coarse index of every agent. performance.
5

3.3 DifficultiesforGPU-CPUCollaboration
L0 index
In this section, we explore how to fully utilize the hard- Pattern 1 F P S a M tt e T r a n b 2 le Pattern 3 C 1 C 3
wareresourcesoftheGPU-CPUplatform,whichiswidely
adoptedin LLMinference[36,86]. Vectorsearchinvolves
C1 C1 C2 C1
high-dimensionalfloating-pointcomputationandtherefore
C3 C3 C
2
Similarity-based Pattern Matching
benefitssubstantiallyfromGPUacceleration.Asshownin
L1 index
Figure8(a),wecharacterizetheperformanceadvantagesof C1 C3 C1
CPUandGPUexecution.Whenthenumberofvectorsper …
Pattern-aware
cluster is small (< 256), CPU-based computation exhibits Prefetching
C1 C2 C3 L2 index
lower latency. In contrast, once the cluster size reaches a
…
moderaterange( 512),GPU-basedvectorsearchachieves
↑ New request
aclearspeedupofmorethan 3 . TheGPUsearchlatency
→
remainslargelystableastheclustergrows,sincethedominant
Figure9:Three-levelmemoryindexcachetooptimizesearch
overheadarisesfromkernellaunchratherthancomputation.
efficiency,withFSM-basedmodelingforaccesspatterns.
PriorworkhasextensivelyexploredfullyGPU-residentin-
dexes[32]andsearchframeworks[84].
However, large-scale vector databases (often over 100
havior;(ii)Multi-layermemorystoragethatsupportsefficient
GB[19])placeheavydemandsonGPUmemoryandmakeit
sharing,reuse,andmigrationofmemoryacrossagents;and
impracticalfortheGPUtostoretheentireindex.Thelarge
(iii)Multi-deviceefficientexecution withdynamichotspot
modelweightsandKVcachefurtherexacerbatethispressure.
detectionandcross-deviceconsistencymanagementtofully
Thisnecessitatesanon-demanddatatransfermechanismbe-
leverageheterogeneousCPU–GPUresources.
tweentheCPUandGPU.However,suchtransferintroduces
significantoverhead,typicallyfarexceedingtheactualcompu-
tationtime,asshowninFigure8(b).Toaddressthischallenge, 4.2 Pattern-DrivenMulti-LevelIndexCache
existinghybridCPU–GPUdesignsemployhotspotcaching
ExistingdynamicANNmethodseitherrelyonstreamingin-
andoffloading[24,33,43,61]forlarge-scaleindexes.
sertionandlocalrebalancing[49,50,74],oroncoarse-grained
The highly dynamic nature ofagentmemory introduces
bufferingandperiodicmerging[60,87].Bothapproacheslack
anadditionaldimensionofcomplexityformaintainingcon-
awarenessofagent-levelworkloadpatterns,includingintra-
sistencyinCPU–GPUco-managedindexes.Hotspotclusters
requestlocalityandinter-requeststep-wiselocality.
in agent memory are not only frequently queried but also
Three-LevelClusterCaching.Weemploypartialcachingto
frequentlyupdated.However,becauseCUDAlacksefficient
resolvethemismatchbetweenlocalizedaccessoperationsand
mechanismsforconcurrentdynamiclistexpansion,clusters
thecoarse-grainedclusterstructureoftheunderlyingANN
cachedontheGPUcannotflexiblysupportfrequentinsertions.
index.AsshowninFigure9,eachupperlevelindexforms
Priorworkprimarilysupportscachemanagementforstatic
asubsetofthelevelbelow,butisorganizedtomoreclosely
indexes, while performing updates on the CPU index and
reflecttheagent’sintrinsicmemory-accesspatterns.
retransferringthemodifiedclustersbacktotheGPUincurs
Searchandupdateovertheindexalwaysbeginatthetop
prohibitiveevictionandtransfercosts.
level.L0maintainsatableSthattracksthemostfrequently
To address the above challenge, Pancake implements a
accessedN tinyclusters,whichcontainsthemostrecently
GPU–CPUcoordinateddynamicindexmanagementscheme p
accessed vectors to preserve the agent’s temporal locality.
basedoninsertionbuffersandasynchronoustransfers.This
When an L0 cluster overflows,evicted vectors are written
designenablesdynamicallyextensiblehotspotclusterstobe
backinto the L1 index. L1 also maintains N intermediate
acceleratedduringbothsearchandupdateoperations. p
clusters. Itcachesthetop-k neighborsforeachsearchand
↓
update,where k is slightly larger than the actual retrieval
↓
4 Pancake:MethodsandSystemDesign parameterk,allowingL1tostorethebroaderneighborhood
aroundfrequentlyaccessedvectors.Finally,onceanL1clus-
terexceedsapredefinedsizethreshold,itismergedwiththe
4.1 Overview
L2clusters,formingastableandcoarse-grainedstructure.
In this work,we present Pancake,a multi-tier ANN-based Weleveragetheearlyterminationmechanism[4]invector
system designed to meet the demands of dynamic agentic searchtoacceleratecomputationusingcacheddata.During
memoryworkloads.Pancakefollowsacoordinatedmulti-tier search,wheneveralltop-kcandidatesatthecurrentlevelhave
designthatconsistsof:(i)Multi-level,cache-inspiredindex distancessmallerthan! d ,weskipcomputationatthe
et agent
·
orchestrationinformedbytrajectory-basedagentworkload next level. Here,d denotes the average top-k distance
agent
embeddings,enablinglocality-awaresearchandupdatebe- acrossrecentqueriesofthesameagent.Inpractice,setting
6

! et =0.6 0.8providesastrongtrade-offbetweenefficiency StaticCoarse Index
↔
andaccuracy.Wefurtherintroduceaverificationmodeinthe
Agent 1 Agent 2
system:afteranearlyreturn,thesystemoptionallyperforms Coarse Index Coarse Index
thecompletesearchinthebackground.Thisenablesdynamic
adjustmentof! withoutincurringadditionallatency,while Connection with
et Hybrid Graph
maintainingcompatibilitywithLLM-coordinatedspeculative-
generationworkflows[24,31,83].
FSM-basedPatternModeling.Theagentmemoryaccess
AgentCluster 1 Profile1 StaticCluster Profile2 AgentCluster 2
patternscanbemodeledasaFinite-State-Machine(FSM): v11v12v13 1 3 5 v1v2v3v4v5v6 2 4 6 v21v22v23
P=(S,T), (c i c j ) T, c i ,c j S, Figure10:Multi-agentindexmanagementwithhybridgraph
↗ ↘ ↘
andagent-specificpatternprofilingonsharedclusters.
where S is the set of semantic cluster states. Each cluster
(c,∀) S storesitsclustercentroidcandtheaverageintra-
↘
clustervectordeviation∀fromthecentroid.Thetransitionset accessintherequestsequencebecomesanindependentstate,
T capturesthedirectedmovementofmemoryaccessesacross andstates are subsequently mergedaccording to the maxi-
clusterstates.SuchFSMabstractionpreservesbothsemantic mumnumberofstatesN andtheminimummergingdistance
S
groupingandstep-wisetransitionbehavior. d .IfthenumberofFSMentriesexceedsN ,thesystem
merge p
TheL0indexmaintainsapatterntablewithN p FSMen- merges two FSMs with the highest similarity,producing a
tries.Givenanewrequestwithmemoryembeddingsequence compactandcontinuouslyupdatedFSMtable.
(v ,v ,...,v),wecomputeitssimilaritytopatternP based
1 2 t i
onprefix-statealignmentandtransitionconsistency:
4.3 Multi-AgentIndexingwithHybridGraph
t ∀ We propose a multi-agent–friendly index mechanism that
sim(P,v )= #I (c c ) T k ,
i 1:t k=1 ! k ≃ 1 ↗ k ↘ i " ·1+ | c k ≃ v k | i s n h c o o w rp n o i r n at F e i s g c u o re or 1 d 0 in , a o t u e r d d c e o s a ig rs n e u s n e i a fi r e c s h t a h n e d m a u li l g ti n p m le e c n o t. ar A se s
whereI[]istheindicatorfunction.Usingthissimilarity,each indexesintoahybridgraphstructure,enablingefficientcoarse
·
request identifies the best-matching pattern and infers the search through graph traversal. Meanwhile,by associating
expectedtargetclusterforsubsequentmemoryaccesses. eachclusterwithagent-specificmemoryaccesspatterns,re-
Pattern-basedReorderingandPrefetching.Modelingthe ferredtoasagentprofiles,wefurtherreduceoverheadand
accesspatternenablesworkload-awaresearchreordering.For improverecallforthecross-indexoperations.
eachsearchoperation,thecachemanagermatchesitsrecent HybridGraphConstruction.Weintroduceagraphstruc-
accesssequencetoapatternintheFSMtableandpredictsthe turethatconnectsthestaticmemoryandeachagent’slocal
mostprobableL0andL1cluster.Thesearchprocessthenpri- memory.Forthefineindex,vectorsineachstaticandagent
oritizesthepredictedcluster,enablingamoreefficientsearch localmemoryarestoredonlyonce,eliminatingredundantstor-
orderandincreasingthelikelihoodofearlytermination. age.Forthecoarseindex,eachmemoryscopemaintainsits
FSM-basedmodelingalsoenablesprefetch-likebehavior owncoarseindex,organizedasamulti-levelgraphstructure
in theindexcache. Aftereachcompletedsearchorupdate, similartoHNSW[48].Eachlayerformsabounded-degree
thesystempredictstheclusterslikelytobeaccessednext.If graphwithuptoM neighborspernode.Queriesperforma
theseclustershavebeenevictedorwrittenback,background greedydescentthroughtheupperlayers,followedbyabest-
prefetchingistriggeredtoproactivelyrefreshthecacheahead firstsearchatthebottomlayerusingafrontierofsizeef search
of time. Prefetching is carried out through an independent toapproximatethenearestneighbors.
search,itcanruninparallelwiththeagent’sLLM-generation Amongmultiplecoarseindexes,wefurtherintroduceinter-
steps,creatingadditionalopportunitiestoreduceoverhead. graphconnectionstoenablenavigationacrossdifferentmem-
FSMConstruction.ConstructingsuchFSMsonlineischal- ory scopes. Specifically, when maintaining each agent’s
lenging, as agent memory accesses arrive in the form of coarseindex,eachnodeinthegraphisadditionallyconnected
embedding vectors rather than pre-labeled semantic clus- into the static coarse index with probability of 1/ef connect ,
ters.Classicalpattern-recognitionapproaches(e.g.,PCA[2], thereby creating a controlled numberof cross-agent portal
HMMs[55])areprohibitivelyexpensiveforhigh-dimensional nodesthatsupportcollaborativemulti-agentsearch.
andfine-grainedonlineagentworkloads.Wethereforeadopta Across-scopememoryoperationbeginsinthestaticcoarse
lightweightheuristicFSMconstructionandmergingstrategy. index entry and performs a BFS-like traversal. When the
Whenanagentrequestcompletes,thecachesystemfirst traversalencountersanodewithaninter-connectiontothe
attemptstomatchitagainstanexistingFSMinthetable.Ifno targetscope,thesearchaddsthecorrespondinggraphtothe
matchisfound,anewFSMiscreated.Duringcreation,each searchfrontier,andsettheinter-connectednodeastheentry.
7

GPU
memory
Thisenablesseamlesstransitionacrossmemoryscopeswhile
LLM On-GPU Splitting
avoidingunnecessarysearchingoverirrelevantregions. Storage GPU Custer X
Todetermineasuitablevalueforef ,wecomparethe custer Hotspot-aware
connect Mode Weight Caching
density of the static coarse index with that of each agent-
Custer 1 Custer 2
KV Cache
specific index. We measure the average centroid spacing
New custer
withintheprivateindex(d agent )andthestaticindex(d static ), Adaptors G O P n U l o S a e d a e rc d h Me G m PU ory
andsettheinter-connectionprobabilityas Asynchronized
GPU-CPU update
CPU
ef =min ! d static , 1 . custer Search Custer 1 Custer 2 Custer 3 Insert
connect ic
CPU # ·d agent $ Insert buffer
Insert Buffer 1 Buffer 2 CPU
Query memory Theintuition is asfollows: when thestaticindexcovers buffer Memory
abroaderspace,onlysparseconnectionsareneeded;when
thetwospaceshavesimilardensity,denserconnectionshelp Figure11:GPU-CPUcoordinatedindexmanagementtoen-
avoidcross-graphlocalminima.Empirically,wechoose! ic ablehotspotclustercomputationacceleration.
between4and8tobalanceefficiencyandrecall.
SearchOptimizationwithAgentProfile.Duetohighlynon-
uniformaccesspatterns,clustersinthestaticmemoryexhibit memorybudget.Wheneverthehotspotsetchanges,thesys-
different usage patterns across agents. However,the static tem performs cluster eviction and reallocation to keep the
memoryindexcannotadapttothesedifferences,leadingto GPUcachealignedwiththecurrentworkload.Datamigra-
unnecessarysearchoverheadandpreventingtheindexfrom tionisthroughasynchronousCPU–GPUtransferstoavoid
aligningwithagent-specificaccesspatterns. highlatency.However,insertionsintheagenticmemorymay
Toaddressthis,Pancakeintroducesanagentprofilemecha- causefrequentstalenessofthecachedclusters.
GPU memory
nismforeachstaticcluster.Specifically,everystaticclusteris
CPUInsertionBuffer.Asshowninthesamplingresultsof
associatedwithanagent-specifictablethatrecordsthelocal
§3.3,theCPUcomputationtimeofasmallsetofvectorsis
IDsofrCece1ntlyaccesseCd2vectorswithinthatcluster.Suchlist
lowerthantheGPU’sclusterprocessinglatency.Therefore,
ismaintainedasafixed-sizesortedlist.Wheneverthetop-k
wemaintainaper-clusterinsertionbuffer:onceaclusteris
results of a query fall inside the current cluster, the corre-
residentontheGPU,subsequentinsertionstargetingthatclus-
spondinCguvesctteorr I1Dsarepromotedtothefrontofthelist.For
terarefirstaccumulatedinitsCPU-sidebufferofsizeB .
insert
subsequentaccesses,whentheagentrevisitsthecluster,itfirst
Forallthesearchestargetingthatcluster,computationisper-
retrievesCth2evectorsreferencedinitsprofilebytheirstored
formedcollaborativelyusingboththeGPU-cachedportion
localIDs,enablingabettersearchordCer2andincreasingthe
oftheclusterandthevectorsnewlyinsertedtheCPUbuffer.
likelihooCd3ofearlytermination.Becausetheprofilemaintains
Thepartialresultsfromthetwodevicesarethenmergedto
onlyvectorIDsandalightweightliststructure,theadditional
produce the finalresults. Because the additionalCPU-side
storageandmanagementoverheadisnegligiblecomparingto
searchrunsinparallelwiththeGPUcomputationandcon-
thehigh-dimensionalembeddingcomputations.
tributesonlyasmallfractionoftheoverallprocessingtime,
the end-to-end request latency effectively matches that of
asingle-GPUexecution. Basedonthisobservation,weset
4.4 DynamicGPU-CPUIndexCoordination
B tothelargestclustersizewhereCPU-sidesearchcost
insert
Tofurtherleverageheterogeneoushardwareresources,wein- islowerthanGPU-sidesearch,whichis128onourplatform.
troduceaGPU–CPUcoordinateddynamicindexmanagement Asynchronized Consistency Management. When the in-
mechanism,asillustratedin Figure11. Ourheterogeneous sertionbufferbecomesfull,thecorrespondingGPU-cached
design consists ofa CPU-side insertion bufferanda GPU- clusterisresized,andthebufferedvectorsaremigratedfrom
side manager for hotspot-aware caching, onloaded search, theCPUtotheGPU.Toavoidthesubstantiallatencycaused
andconsistentclustermaintenance. Suchasystemenables byon-demanddatatransfers,weadoptafullyasynchronous
memory-efficienthotspotaccelerationanddynamiccluster cluster-expansionmechanism.TheGPU-sideindexmanager
organization across devices. This is particularly critical in proactivelyallocatesnewspaceforclusterstoexpandandper-
theco-locatedservingscenariowithLLMs[24],wherethe formsdatatransfersinparallelwithonlineserving.Already
inferenceengineoccupystensofgigabytesofGPUmemory. cacheddataaremigratedusinglow-costGPU–GPUcopies,
Hotspot-awareCaching.Inourhybridindexmanager,GPU while newly inserted buffer data are transferred through
memory dynamically caches hotspot clusters to accelerate GPU–CPU copies. Once the new data transfer completes,
criticalcomputation.ForeachCPU-residentcluster,thesys- the old GPU cluster is released, enabling seamless online
tem tracks its access frequency and selects the most fre- cluster switching. This design eliminates both the waiting
quently accessed clusters according to a predefined GPU overheadassociatedwithsynchronous data movementand
8

thememorywasteincurredbyover-allocatingGPUspace. integrating their memory backends with LLM generation
On-GPUClusterSplitting.TheGPUcacheintroducesan- workloads.Thebaselinesinclude:A-Mem[73]:backendfor
other optimization opportunity: accelerating the computa- semanticallyevolvingmemoryinlong-termconversational
tionforclustersplitting.ClusteringalgorithmslikeK-means- retrieval.MemGPT [53]:backendforOS-stylememorythat
based methods [16,85] typically incurs a vector similarity swapsinformationbetweenmaincontextandexternalstorage.
costthatismultipletimeshigherthanthatofregularsearch. LlamaIndex[44],vector-storebackendintheRAG-oriented
Thus,weimplementalightweightkernelbasedonGPU-based framework. LangMem: vector-storebackendintheagentic
K-meansalgorithms[7,41]toonloadclustersplitting,avoid- frameworkLangChain[1].
ing the high computational load and latency on the CPU.
For evaluating the performance of standalone vector
Importantly,duetothelocalityofmemoryaccess,clusters
databases, we compare our system against state-of-the-art
thatrequiresplittingareusuallycachedontheGPU,sothis
dynamicallyupdatablevector-indexlibraries.Weusethevec-
techniquecanreducethemajorityofsplittingoverhead.
tors generated from the memory operations in our end-to-
end agent workloads as input to these systems. The base-
5 Implementation linesinclude:Quake[50],structuredandinsert-friendlyin-
dex library with dynamic hot-region–aware optimization.
User Interface. Pancake provides a user-friendly Python SpFresh [74],a large-scale vectorsearchframeworkbased
interface that exposes simple primitives foragent-memory onstreaminginsertionandlocalized,balancing-awarerecon-
operations,includingsearch,insert,update,anddelete,with struction.DiskANN[26,60],openANNlibrarythatcombines
explicitspecificationofthetargetmemoryscope.Ourinitial- anupper-layergraphwithalower-layerclusterindex.
izationinterfacealsosupportsloadingfromexistingindexes,
Forablationstudy,wealsoimplementtwodynamicmain-
suchasFaiss[17],enablingreconstructionthatisfriendlyto
tenancestrategieswithinourframework,including:Pancake-
IVF-basedindexes.Operationssubmittedthroughtheinter-
IVF-Static,whichinitializesanIVFindexonceandsimply
face are batched,andadjacentoperations ofthe same type
appendsnewvectorstothenearestcentroidwithoutanyfur-
arefurthergroupedintoasinglebatchtoimproveresource
thermaintenance.Pancake-IVF-Split,whichperformscluster
utilization.
splittingwhenthesizereachesathreshold,consistentwith
Multi-threadedIndexConstruction.InPancake,clusters
streaming-updateandlazy-reconstructionstrategies[49].
areimplementedasmultithread-shareddatastructures,pro-
tectedbyshared-readandexclusive-writelocks.Eachcluster Dataset. We evaluate our system across diverse forms of
is associated with metadata, including its index identifier, agent dataset, including multi-turn human–agent dialogue
multi-agentprofiles,anditsresidencystatusacrossthemulti- datasets(UltraChat[15],UltraFeedback[13]),longchain-of-
levelcacheandtheGPUcache.Wemaintainamultithreaded thoughtmathematicalreasoning(Prm800k[42],Gsm8k[12]),
executionpoolthatincludesdedicatedsearchthreads,update and task-oriented agent datasets covering function calling
threads,cache-managementthreads,andGPU-management (APIGen[46])andenvironmentinteraction(AgentGym[69]).
threads.Insertanddeleteoperationsarealsohandledwithin
Workload.Weevaluateseveralrepresentativememoryaccess
the search threads, where items are updated based on the
patterns,whichcanbeobservedindifferenttypesofagents:
search results. Pancake adopts asynchronous invocation to
ensureconcurrencywithLLMcallsandtomaintaincompati- –One-Search-One-Insert: Each generation step search the
bilitywithexistingRAG-stylesystems[24,28,31]. memoryandupdatesitwiththenewoutput,typicalformulti-
turnconversationalagents[53,78].
6 Evaluation –Step-Search-Then-Insert:Eachstepsearchthememory,but
updatesoccuronlyattheend,typicalforsummarizationor
6.1 ExperimentalSetup long-contextcompressionagents[10,52,79].
Hardware.WeconductallexperimentsonaCPU–GPUhy- –Search-Then-Step-Insert:Onlythefirststepperformsmem-
bridserver.Eachnodeisequippedwithone64-coreAMD orysearch,whiletheupdateoccursineachstep,typicalfor
EPYC9534processorandeightNVIDIAH100GPUswith personalizedagentsdrivenbyuserprofiles[21,67].
80GBofmemory.Themaincontrol,scheduling,andcom-
–Search-Only: Theagentonlyqueriesmemorywithoutup-
putation logicofPancakerun on theCPU,whiletheLLM
dates,typicalforRAG-styleagents[5,8,71].
generation and GPU caching are performed on the H100
GPUs. Static Knowledge Database. We initialize the vector
Baseline. Foragentserving,we compare fourmemory de- databasesimilartotheMem-GPT[53]setup,usingtheMS
sign algorithms and their system implementations. These MARCO corpus [51], 8M passages in total, as the initial
systemsprovidedefaultANN-basedinterfacesformemory knowledgebase.AllembeddingsareencodedusingtheE5
managementandretrieval.Weevaluatethemend-to-endby model[66]with1024dimension.
9

Figure12:End-to-endthroughputcomparisonbetweenPancakeandotheragenticframeworks,inasingleagentscenarioacross
fourdifferentaccesspatterns.TheexperimentsareconductedwithvLLM[36]forLlamamodels[62]andAPIcallsforGPT-5.
Figure14:Scalingbehaviorofend-to-endthroughputwith
anincreasingagentnumber.Theexperimentsareconducted
withLlama3.1-8B.
Figure13:End-to-endthroughputcomparisonintwo-agent localinferenceservers[36]andremoteAPIexecution,Pan-
mixedworkload,conductedwithLlama3.1-8B. cakeconsistentlysustainsstablesingle-agentrequestthrough-
put,achievingend-to-endperformanceimprovementsranging
from1.12 to26.18 .Onaverage,thespeedupoverexisting
→ →
6.2 OverallPerformance librariesismorethan4.29 .
→
For the memory operations only, Pancake achieves
Inthissection,weevaluatetheend-to-endimprovementson speedups of more than 6.81 . The average memory oper-
→
memory-basedagentsperformancewhenusingPancake. ationtimeofPancakeaccountsforlessthan17.9%,andon
Single-AgentThroughput.Wecomparedifferentmemory average3.2%ofthetotalexecutiontime.Thisdemonstrates
managementlibrariesinsingle-agentsettingsacrossmulti- the effectiveness of Pancake in mitigating memory-related
plemodelsanddatasets,asshowninFigure12.Acrossboth bottlenecks.
10

Figure 16: Tradeoffbetween recallandquery latency over
differentindexingstrategies.
asAgentGymandAPIGen,exhibitlargerperformancedrops.
Figure15:QuerythroughputofPancakeandexistingvector Thisisbecausebroaderdatasetcoverageincreasesthenum-
databaseimplementations,withthebatchsizesetas8. berofnodestraversedduringthecoarse-levelgraphsearch,
resultinginproportionallyhighersearchoverhead.
Inaddition,weobservethatworkloadsdominatedbysearch
6.3 ComparisonwithExistingVectorDatabase
operations,includingOne-Search-One-InsertandSearch-only,
exertapronouncedperformanceimpactonbaselinesystems. Query Throughput Improvement. We compare Pancake
This is because existing systems rely on suboptimal index withexistingvectordatabasesandindexingstrategiesunder
constructionsandmaintenancestrategies,whichallowlow- onlineservingworkloads.AsshowninFigure15,Pancake
costinsertionsbutincurexcessivesearchoverhead. consistentlyimprovesthroughputacrossmemory-intensive
Mixed-Workload Throughput. We evaluate the impact agent-serving scenarios, achieving 1.9 to 4.2 average
→ →
oftwo-agentmixedworkloadsonend-to-endperformance, speedupsoverthebaselines.Thesespeedupsstemfromcache
whereeachagentperformsinsertsonitsprivatememoryand andindexdesignstailoredtoagentmemory-accesspatterns,
searches on bothsharedandprivate memory. As shown in which is overlooked in priorwork. When leveraging GPU
Figure 13,existing memory frameworks exhibitadditional acceleration,Pancakefurtherachievesanadditional2.2!per-
performancedegradation,droppingby29.9% 55.9%.This formancegain,resultinginmorethan3.9!speedupoverother
↔
degradation arises from separate memory instance mainte- baselines.Thisdemonstratestheeffectivenessofdynamically
nanceandthelackofcoordinatedmanagementacrossshared coordinatingGPUresourcesthroughourmanagementmech-
andprivatememoryregions,whichleadstointerferencebe- anisms.
tweenagentsandamplifiesoperationoverhead.Incontrast, TradeoffbetweenEfficiencyandRecall. Wecomparere-
Pancakeleveragesitshybrid-graphdesigntoenableefficient call–latencytrade-offsunderbothmixedsearch–updateand
cross-agentsearchandindexalignment,therebypreserving search-onlyworkloads.AsshowninFigure16,directlyapply-
searchlocalityandreducingredundantscans,Pancakelimits ingIVFindexyieldsrelativelylowrecall:inthesearch-only
the performance drop to no more than 9.8% under mixed setting,IVFmustscanupto128clusterstoreachrecallabove
workloads. 0.9.Underthesearch–updateworkload,IVFsuffersaneven
Multi-AgentScalability.Weconstructvaryingnumbersof larger recall drop because newly inserted vectors are scat-
memory-basedagentsandexecutedistinctrequestsoverthe teredacrossdifferentclusters,leadingtoreducedlocalityand
samedataset,thenmeasureoverallthroughputwithoperations suboptimalindexorganization.
acrosssharedandprivatememoryregions.AsshowninFig- Byexploitingagentlocalityandmemory-accesspatterns,
ure14,Pancakeachievesnear-linearscalabilityinmulti-agent Pancakeeffectivelyleveragesitscachingmechanismtore-
settings.Withupto20concurrentagents(thetypicalscale ducelatencywhilemaintaininghighrecall.Moreover,with
ofcommonmulti-agentframeworks[39,68]),theend-to-end coordinated GPU processing,Pancake can scan additional
performancedegradationremainsbelow10.2%. clusterswhilesimultaneouslyservingcachehits,achieving
Wealsoobservethatmorecomplexdatasetsequences,such lowerlatencytogetherwithaslightimprovementinrecall.
11

Figure18:Efficiencyimprovementsfrommulti-levelindex
management on (a) coarse index search cost and (b) total
Figure17:Numberofscannedvectorstoachievefullyrecall
computationcost.
oftop-5memoryitems.Theinsertion-to-searchratiois1:1.
6.4 AblationStudy
Inthissection,weconductdetailedcomparativeexperiments
ontheoptimizationtechniquesandprovideanin-depthanal-
ysisoftheireffectsandtherootcausesoftheimprovements.
OptimizedIndexwithMulti-levelCache.Wecomparehow
different dynamic maintenance strategies affect the search
costs with dynamism. A lower number of scanned vectors
Figure 19: (a) GPU speedups under varying pre-allocated
indicates that the index has evolved into a structure better
GPUcachesizes.(b)Computationlatencyofeachqueryover
alignedwiththecurrentagent’saccesspatternandprovides
theinputworkloadwithAgentGymdatasetand10GBGPU
strongerearly-terminationopportunities,therebyimproving
memorycachesize.Theinsertion-to-searchratiois1:1.
performance.AsshowninFigure17,performingIVF-Static
updates leads to significantly higher scan counts, because
newlyinsertedmemoryitemsaredistributedacrossmanyclus-
ofPancakeinmulti-agentindexmanagement.
tersratherthanbeinglocalized.IVF-Spliteventuallyreduces
SpeedupswithGPUCaching.WeevaluatehowGPUcache
thenumberofscannedvectorswithsufficientinsertionsand
sizeaffectsperformance.AsshowninFigure19(a),theGPU-
thestableclustersformed.However,thelongpre-convergence
acceleratedversionachievesupto1.92 speedupoverthe
phasecanbeobservedsincetheindexcannotrebalanceuntil →
CPUbaselineandreachesaperformanceplateauwithonly
thesplittingthresholdisreached.Incontrast,ourmulti-level
5 15 GB of GPU memory. The effectiveness of GPU ac-
indexcacheeffientlyexploitsagent-specificspatialandtem- ↔
celerationdependsontheworkload:conversationaldatasets
porallocality,allowingittostabilizeatalowscancostmuch
distribute query-relevant clusters more widely,requiring a
earlier. This early adaptation leads to up to 2.23 latency
→ largerGPUcachetofullyexploitacceleration.
reductionoverlong-servingworkloads.
We also examine latency over time under a mixed
SearchEfficiencywithMulti-AgentIndex.Wefirstcom-
search–insertworkload.AsshowninFigure19(b),theGPU
pare the reduction in coarse indexsearchcostundermulti-
versionwarmsupquicklybycachinghotclustersandmain-
agentindexmanagement. AsshowninFigure18(a),main-
tainslow,stablelatency.Occasionalspikesarisewhenstream-
tainingseparateindexesforeachagentleadstoanear-linear
inginsertionstriggerclustersplits,temporarilyintroducing
increaseincoarsesearchoverheadasthenumberofagents
additional computation. In our GPU-enabled design,most
grows.Incontrast,ourmulti-indexmanagementemploysahy-
clusteroperationsareperformedontheGPU,reducingthe
bridgraphthatinterconnectsagents’coarseindexes,enabling
costofthesespliteventsandkeepingtheirimpactminimal.
efficientnavigationoftheglobalsearchspaceandachieving
morethana20!reductionincoarsesearchcost.
We furthercompare the totalsearchcostunderdifferent 7 Conclusion
optimizationstrategies.AsshowninFigure18(b),thehybrid-
graphconstructionreducesthenumberofvectorsimilarity WepresentedPancake,amulti-tiermemorymanagementsys-
computations by up to 11.6% compared to independently temthatbridgesthegapbetweendynamicagenticmemory
constructed indexes. Moreover, when incorporating agent andANN-basedvectorindexing.Pancakeleveragessemantic
profiles,wecantrackeachagent’saccesspreferenceswithin localityforsingle-agentworkloads,hybridindexingformulti-
thestaticclusters,achievinganadditional21.8%reduction agent memory management, and CPU–GPU collaborative
in average computation cost without modifying the global indexingforacceleration.WithasimplePythoninterfaceand
indexlayout.Theseresultshighlighttheuniqueadvantages supportforflexiblemulti-scopememoryoperations,Pancake
12

integrateseasilyintoexistingagentframeworks.Experiments [10] PrateekChhikara,DevKhant,SaketAryan,Taranjeet
acrossdiverseagentdatasetsshowthatPancakesignificantly Singh,andDeshrajYadav. Mem0:Buildingproduction-
reducesmemoryoperationoverheadanddeliversmorethan readyaiagentswithscalablelong-termmemory. arXiv
4.29 averageend-to-endspeedupoverexistingimplementa- preprintarXiv:2504.19413,2025.
→
tions.
[11] GobindaGChowdhury. Introductiontomoderninfor-
mationretrieval. Facetpublishing,2010.
References
[12] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
MarkChen,HeewooJun,LukaszKaiser,MatthiasPlap-
[1] langChain. https://github.com/langchain-ai/ pert,JerryTworek,JacobHilton,ReiichiroNakano,etal.
langchain,2022.
Trainingverifierstosolvemathwordproblems. arXiv
preprintarXiv:2110.14168,2021.
[2] HervéAbdiandLynneJWilliams. Principalcomponent
analysis. Wileyinterdisciplinaryreviews:computational [13] Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao,
statistics,2(4):433–459,2010. BingxiangHe,WeiZhu,YuanNi,GuotongXie,Ruob-
ingXie,YankaiLin,etal. Ultrafeedback:Boostinglan-
[3] CharuCAggarwal,AlexanderHinneburg,andDanielA guagemodelswithscaledaifeedback. arXivpreprint
Keim. Onthesurprisingbehaviorofdistancemetricsin arXiv:2310.01377,2023.
highdimensionalspace. InInternationalconferenceon
[14] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
databasetheory,pages420–434.Springer,2001.
Kristina Toutanova. Bert: Pre-training of deep bidi-
rectionaltransformersforlanguageunderstanding. In
[4] Vo Ngoc Anh,Owen de Kretser,and Alistair Moffat.
Proceedingsofthe2019conferenceoftheNorthAmer-
Vector-spacerankingwitheffectiveearlytermination.
ican chapteroftheassociation forcomputationallin-
InProceedingsofthe24thannualinternationalACM
guistics:humanlanguagetechnologies,volume1(long
SIGIRconferenceonResearchanddevelopmentinin-
andshortpapers),pages4171–4186,2019.
formationretrieval,pages35–42,2001.
[15] NingDing,YulinChen,BokaiXu,YujiaQin,Shengding
[5] AkariAsai,ZeqiuWu,YizhongWang,AvirupSil,and Hu,ZhiyuanLiu,MaosongSun,andBowenZhou. En-
Hannaneh Hajishirzi. Self-rag: Learning to retrieve, hancingchatlanguagemodelsbyscalinghigh-quality
generate,andcritiquethroughself-reflection. 2024. instructionalconversations. InProceedingsofthe2023
ConferenceonEmpiricalMethodsinNaturalLanguage
[6] KevinBeyer,JonathanGoldstein,RaghuRamakrishnan, Processing,pages3029–3051,2023.
andUriShaft. Whenis“nearestneighbor”meaningful?
[16] YufeiDing,YueZhao,XipengShen,MadanlalMusu-
InInternationalconferenceondatabasetheory,pages
vathi,andToddMytkowicz. Yinyangk-means:Adrop-
217–235.Springer,1999.
inreplacementoftheclassick-meanswithconsistent
speedup. InInternationalconferenceonmachinelearn-
[7] JankiBhimani,MiriamLeeser,andNingfangMi. Ac-
ing,pages579–587.PMLR,2015.
celeratingk-meansclusteringwithparallelimplemen-
tationsandgpucomputing. In2015IEEEhighperfor-
[17] MatthijsDouze,AlexandrGuzhva,ChengqiDeng,Jeff
manceextremecomputingconference(HPEC),pages
Johnson,GergelySzilvasy,Pierre-EmmanuelMazaré,
1–6.IEEE,2015.
MariaLomeli,LucasHosseini,andHervéJégou. The
faisslibrary. IEEETransactionsonBigData,2025.
[8] SebastianBorgeaud,ArthurMensch,JordanHoffmann,
TrevorCai,ElizaRutherford,KatieMillican,GeorgeBm [18] Darren Edge, Ha Trinh, Newman Cheng, Joshua
Van Den Driessche, Jean-Baptiste Lespiau, Bogdan Bradley,AlexChao,ApurvaMody,StevenTruitt,Dasha
Damoc,AidanClark,etal. Improvinglanguagemod- Metropolitansky,RobertOsazuwaNess,andJonathan
els by retrieving from trillions of tokens. In Interna- Larson. From local to global: A graph rag ap-
tional conference on machine learning, pages 2206– proachtoquery-focusedsummarization. arXivpreprint
2240.PMLR,2022. arXiv:2404.16130,2024.
[19] WikimediaFoundation. Wikimediadownloads.
[9] Qi Chen, Bing Zhao, Haidong Wang, Mingqin Li,
ChuanjieLiu,ZengzhongLi,MaoYang,andJingdong [20] DamienFrançois,VincentWertz,andMichelVerleysen.
Wang. Spann: Highly-efficient billion-scale approxi- Theconcentrationoffractionaldistances.IEEETransac-
matenearestneighborhoodsearch. AdvancesinNeural tionsonKnowledgeandDataEngineering,19(7):873–
InformationProcessingSystems,34:5199–5212,2021. 886,2007.
13

[21] Tao Ge,Xin Chan,Xiaoyang Wang,Dian Yu,Haitao [31] ChaoJin,ZiliZhang,XuanlinJiang,FangyueLiu,Shu-
Mi, and Dong Yu. Scaling synthetic data cre- fanLiu,XuanzheLiu,andXinJin. Ragcache:Efficient
ation with 1,000,000,000 personas. arXiv preprint knowledgecachingforretrieval-augmentedgeneration.
arXiv:2406.20094,2024. ACMTransactionsonComputerSystems,44(1):1–27,
2025.
[22] Ruiqi Guo, Philip Sun, Erik Lindgren, Quan Geng,
David Simcha, Felix Chern, and Sanjiv Kumar. Ac- [32] JeffJohnson,MatthijsDouze,andHervéJégou. Billion-
celeratinglarge-scaleinferencewithanisotropicvector scalesimilaritysearchwithGPUs. IEEETransactions
quantization. InInternationalConferenceonMachine onBigData,7(3):535–547,2019.
Learning,pages3887–3896.PMLR,2020.
[33] VKarthik,SaimKhan,SomeshSingh,HarshaVardhan
[23] Yikun Han, Chunjiang Liu, and Pengfei Wang. A Simhadri, and Jyothi Vedurada. Bang: Billion-scale
comprehensive survey on vector database: Storage approximate nearest neighbour search using a single
and retrieval technique, challenge. arXiv preprint gpu. IEEETransactionsonBigData,2025.
arXiv:2310.11703,2023.
[34] RalphKimballandJoeCaserta. Thedatawarehouse
[24] ZhengdingHu,VibhaMurthy,ZaifengPan,WanluLi, ETLtoolkit. JohnWiley&Sons,2004.
XiaoyiFang,YufeiDing,andYukeWang.Hedrarag:Co-
[35] RalphKimballandMargyRoss. Thedatawarehouse
optimizinggenerationandretrievalforheterogeneous
toolkit: Thedefinitiveguidetodimensionalmodeling.
rag workflows. In Proceedings of the ACM SIGOPS
JohnWiley&Sons,2013.
31stSymposiumonOperatingSystemsPrinciples,pages
623–638,2025. [36] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
Sheng,LianminZheng,CodyHaoYu,JosephGonzalez,
[25] WenlongHuang,PieterAbbeel,DeepakPathak,andIgor
HaoZhang,andIonStoica. Efficientmemorymanage-
Mordatch. Languagemodelsaszero-shotplanners:Ex-
mentforlargelanguagemodelservingwithpagedatten-
tractingactionableknowledgeforembodiedagents. In
tion.InProceedingsofthe29thsymposiumonoperating
International conference on machine learning,pages
systemsprinciples,pages611–626,2023.
9118–9147.PMLR,2022.
[37] PatrickLewis,EthanPerez,AleksandraPiktus,Fabio
[26] SuhasJayaramSubramanya,FnuDevvrit,HarshaVard- Petroni,VladimirKarpukhin,NamanGoyal,Heinrich
hanSimhadri,RavishankarKrishnawamy,andRohan Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel,
Kadekodi. Diskann:Fastaccuratebillion-pointnearest etal. Retrieval-augmentedgenerationforknowledge-
neighborsearchonasinglenode. Advancesinneural intensive nlp tasks. Advances in neural information
informationprocessingSystems,32,2019. processingsystems,33:9459–9474,2020.
[27] Herve Jegou, Matthijs Douze, and Cordelia Schmid. [38] PatrickLewis,EthanPerez,AleksandraPiktus,Fabio
Productquantizationfornearestneighborsearch. IEEE Petroni,VladimirKarpukhin,NamanGoyal,Heinrich
transactions on pattern analysis and machine intelli- Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel,
gence,33(1):117–128,2010. etal. Retrieval-augmentedgenerationforknowledge-
intensive nlp tasks. Advances in neural information
[28] Wenqi Jiang, Shuai Zhang, Boran Han, Jie Wang,
processingsystems,33:9459–9474,2020.
BernieWang,andTimKraska. Piperag:Fastretrieval-
augmentedgenerationviaalgorithm-systemco-design. [39] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii
arXivpreprintarXiv:2403.05676,2024. Khizbullin,andBernardGhanem. Camel:Communica-
tive agents for" mind" exploration of large language
[29] ZhengbaoJiang,FrankFXu,LuyuGao,ZhiqingSun,
modelsociety. AdvancesinNeuralInformationProcess-
QianLiu,JaneDwivedi-Yu,YimingYang,JamieCallan,
ingSystems,36:51991–52008,2023.
andGrahamNeubig. Activeretrievalaugmentedgen-
eration. In Proceedings of the 2023 Conference on [40] WenLi,YingZhang,YifangSun,WeiWang,MingjieLi,
Empirical Methods in Natural Language Processing, WenjieZhang,andXueminLin. Approximatenearest
pages7969–7992,2023. neighborsearchonhighdimensionaldata—experiments,
analyses, and improvement. IEEE Transactions on
[30] ZhengbaoJiang,FrankFXu,LuyuGao,ZhiqingSun,
Knowledge and Data Engineering,32(8):1475–1488,
QianLiu,JaneDwivedi-Yu,YimingYang,JamieCallan,
2019.
andGrahamNeubig. Activeretrievalaugmentedgen-
eration. In Proceedings of the 2023 Conference on [41] YouLi,KaiyongZhao,XiaowenChu,andJimingLiu.
Empirical Methods in Natural Language Processing, Speeding up k-means algorithm by gpus. Journal of
pages7969–7992,2023. ComputerandSystemSciences,79(2):216–229,2013.
14

[42] HunterLightman,VineetKosaraju,YuriBurda,Harrison [52] Siru Ouyang,Jun Yan,I Hsu,Yanfei Chen,Ke Jiang,
Edwards, Bowen Baker, Teddy Lee, Jan Leike, John ZifengWang,RujunHan,LongTLe,SamiraDaruki,
Schulman,IlyaSutskever,andKarlCobbe. Let’sverify Xiangru Tang, et al. Reasoningbank: Scaling agent
stepbystep. InTheTwelfthInternationalConference self-evolvingwithreasoningmemory. arXivpreprint
onLearningRepresentations,2023. arXiv:2509.25140,2025.
[43] Chien-Yu Lin, Keisuke Kamahori, Yiyu Liu, Xiaoxi- [53] CharlesPacker,VivianFang,Shishir_GPatil,KevinLin,
angShi,MadhavKashyap,YileGu,RulinShao,Zihao SarahWooders,andJoseph_EGonzalez. Memgpt:To-
Ye,KanZhu,StephanieWang,etal. Telerag:Efficient wardsllmsasoperatingsystems. 2023.
retrieval-augmented generation inference with looka-
[54] JoonSungPark,JosephO’Brien,CarrieJunCai,Mered-
headretrieval. arXivpreprintarXiv:2502.20969,2025.
ithRingelMorris,PercyLiang,andMichaelSBernstein.
[44] Jerry Liu. LlamaIndex. https://github.com/ Generativeagents:Interactivesimulacraofhumanbe-
jerryjliu/llama_index,112022. havior. InProceedingsofthe36thannualacmsympo-
siumonuserinterfacesoftwareandtechnology,pages
[45] NelsonFLiu,KevinLin,JohnHewitt,AshwinParan- 1–22,2023.
jape, Michele Bevilacqua, Fabio Petroni, and Percy
[55] LawrenceRRabiner. Atutorialonhiddenmarkovmod-
Liang. Lostinthemiddle:Howlanguagemodelsuse
elsandselectedapplicationsinspeechrecognition. Pro-
longcontexts. TransactionsoftheAssociationforCom-
ceedingsoftheIEEE,77(2):257–286,2002.
putationalLinguistics,12:157–173,2024.
[56] SiddhantRay,RuiPan,ZhuohanGu,KuntaiDu,Shaot-
[46] ZuxinLiu,ThaiHoang,JianguoZhang,MingZhu,Tian
ing Feng,Ganesh Ananthanarayanan,Ravi Netravali,
Lan,JuntaoTan,WeiranYao,ZhiweiLiu,YihaoFeng,
andJunchenJiang. Metis:Fastquality-awareragsys-
RitheshRN,etal. Apigen:Automatedpipelineforgen-
temswithconfigurationadaptation. InProceedingsof
eratingverifiableanddiversefunction-callingdatasets.
theACMSIGOPS31stSymposiumonOperatingSys-
Advances in Neural Information Processing Systems,
temsPrinciples,pages606–622,2025.
37:54463–54482,2024.
[57] TimoSchick,JaneDwivedi-Yu,RobertoDessì,Roberta
[47] ChrisLu,CongLu,RobertTjarkoLange,JakobFoerster,
Raileanu, Maria Lomeli, Eric Hambro, Luke Zettle-
Jeff Clune,and David Ha. The ai scientist: Towards
moyer,NicolaCancedda,andThomasScialom. Tool-
fullyautomatedopen-endedscientificdiscovery. arXiv
former:Languagemodelscanteachthemselvestouse
preprintarXiv:2408.06292,2024.
tools. AdvancesinNeuralInformationProcessingSys-
tems,36:68539–68551,2023.
[48] Yu A Malkov andDmitry A Yashunin. Efficientand
robustapproximatenearestneighborsearchusinghierar-
[58] Noah Shinn, Federico Cassano, Ashwin Gopinath,
chicalnavigablesmallworldgraphs. IEEEtransactions
Karthik Narasimhan, and Shunyu Yao. Reflexion:
onpatternanalysisandmachineintelligence,42(4):824–
Language agents with verbal reinforcement learning.
836,2018.
Advances in Neural Information Processing Systems,
36:8634–8652,2023.
[49] JasonMohoney,AnilPacaci,ShihaburRahmanChowd-
hury,UmarFarooqMinhas,JefferyPound,CedricReng- [59] Noah Shinn, Federico Cassano, Ashwin Gopinath,
gli,NimaReyhani,IhabFIlyas,TheodorosRekatsinas, Karthik Narasimhan, and Shunyu Yao. Reflexion:
and Shivaram Venkataraman. Incremental ivf index Language agents with verbal reinforcement learning.
maintenanceforstreamingvectorsearch. arXivpreprint Advances in Neural Information Processing Systems,
arXiv:2411.00970,2024. 36:8634–8652,2023.
[50] Jason Mohoney, Devesh Sarda, Mengze Tang, Shi- [60] Aditi Singh, Suhas Jayaram Subramanya, Ravis-
haburRahman Chowdhury,AnilPacaci,IhabFIlyas, hankarKrishnaswamy,andHarshaVardhanSimhadri.
Theodoros Rekatsinas, and Shivaram Venkataraman. Freshdiskann:Afastandaccurategraph-basedannin-
Quake: Adaptive indexing for vector search. arXiv dex for streaming similarity search. arXiv preprint
preprintarXiv:2506.03437,2025. arXiv:2105.09613,2021.
[51] TriNguyen,MirRosenberg,XiaSong,JianfengGao, [61] BingTian,HaikunLiu,YuhangTang,ShihaiXiao,Zhuo-
SaurabhTiwary,RanganMajumder,andLiDeng. Ms huiDuan,XiaofeiLiao,HaiJin,XuecangZhang,Jun-
marco: A human-generatedmachine reading compre- huaZhu,andYuZhang. Towardshigh-throughputand
hensiondataset. 2016. low-latencybillion-scalevectorsearchvia CPU/GPU
{ }
15

collaborativefilteringandre-ranking. In23rdUSENIX InternationalConferenceonLearningRepresentations,
ConferenceonFileandStorageTechnologies(FAST25), 2024.
pages171–185,2025.
[72] Qian Xu, Juan Yang, Feng Zhang, Junda Pan, Kang
[62] HugoTouvron,ThibautLavril,GautierIzacard,Xavier Chen,YourenShen,AmelieChiZhou,andXiaoyong
Martinet,Marie-AnneLachaux,TimothéeLacroix,Bap- Du. Tribase: A vector data query engine for reliable
tisteRozière,NamanGoyal,EricHambro,FaisalAzhar, andlosslesspruningcompressionusingtriangleinequal-
etal. Llama:Openandefficientfoundationlanguage ities. ProceedingsoftheACMonManagementofData,
models. arXivpreprintarXiv:2302.13971,2023. 3(1):1–28,2025.
[63] Denny Vrandecˇic´ andMarkus Krötzsch. Wikidata: a [73] WujiangXu,ZujieLiang,KaiMei,HangGao,Juntao
freecollaborativeknowledgebase. Communicationsof Tan,andYongfengZhang. A-mem:Agenticmemory
theACM,57(10):78–85,2014. forllmagents. arXivpreprintarXiv:2502.12110,2025.
[64] HanchenWang,TianfanFu,YuanqiDu,WenhaoGao, [74] YumingXu,HengyuLiang,JinLi,ShuotaoXu,QiChen,
KexinHuang,ZimingLiu,PayalChandak,Shengchao QianxiZhang,ChengLi,ZiyueYang,FanYang,Yuqing
Liu,PeterVanKatwyk,AndreeaDeac,etal. Scientific Yang,et al. Spfresh: Incremental in-place update for
discoveryin the age ofartificialintelligence. Nature, billion-scalevectorsearch. InProceedingsofthe29th
620(7972):47–60,2023. SymposiumonOperatingSystemsPrinciples,pages545–
561,2023.
[65] Jianguo Wang, Xiaomeng Yi, Rentong Guo, Hai Jin,
PengXu,ShengjunLi,XiangyuWang,XiangzhouGuo, [75] John Yang,Carlos E Jimenez,AlexanderWettig,Kil-
ChengmingLi,XiaohaiXu,etal. Milvus:Apurpose- ianLieret,ShunyuYao,KarthikNarasimhan,andOfir
builtvectordatamanagementsystem. InProceedings Press. Swe-agent: Agent-computer interfaces enable
ofthe2021internationalconferenceonmanagementof automatedsoftwareengineering. AdvancesinNeuralIn-
data,pages2614–2627,2021. formationProcessingSystems,37:50528–50652,2024.
[66] LiangWang,NanYang,XiaolongHuang,BinxingJiao, [76] ShunyuYao,NoahShinn,PedramRazavi,andKarthik
LinjunYang,DaxinJiang,RanganMajumder,andFuru Narasimhan. ∃-bench:Abenchmarkfortool-agent-user
Wei.Textembeddingsbyweakly-supervisedcontrastive interactioninreal-worlddomains,2024.
pre-training. arXivpreprintarXiv:2212.03533,2022.
[77] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
[67] ZhenWang,YufanZhou,ZhongyanLuo,Lyumanshan Shafran,KarthikRNarasimhan,andYuanCao. React:
Ye,AdamWood,ManYao,andLuoshangPan. Deep- Synergizingreasoningandactinginlanguagemodels.
persona:Agenerativeengineforscalingdeepsynthetic In The eleventh international conference on learning
personas. arXivpreprintarXiv:2511.07338,2025. representations,2022.
[68] Qingyun Wu,Gagan Bansal,Jieyu Zhang,Yiran Wu, [78] Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie
Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Chen,WeinanDai,QiyingYu,Ya-QinZhang,Wei-Ying
Shaokun Zhang, Jiale Liu,et al. Autogen: Enabling Ma,Jingjing Liu,Mingxuan Wang,et al. Memagent:
next-genllmapplicationsviamulti-agentconversations. Reshaping long-context llm with multi-conv rl-based
InFirstConferenceonLanguageModeling,2024. memoryagent. arXivpreprintarXiv:2507.02259,2025.
[69] Zhiheng Xi, Yiwen Ding, Wenxiang Chen, Boyang [79] GuibinZhang,MuxinFu,GuanchengWan,MiaoYu,
Hong, Honglin Guo, Junzhe Wang, Dingwen Yang, Kun Wang,andShuicheng Yan. G-memory: Tracing
Chenyang Liao,Xin Guo,Wei He,et al. Agentgym: hierarchical memory for multi-agent systems. arXiv
Evolvinglargelanguagemodel-basedagentsacrossdi- preprintarXiv:2506.07398,2025.
verseenvironments. arXivpreprintarXiv:2406.04151,
[80] Huan Zhang, Yu Song, Ziyu Hou, Santiago Miret,
2024.
and Bang Liu. Honeycomb: A flexible llm-based
[70] WentaoXiao,YueyangZhan,RuiXi,MengshuHou,and agent system for materials science. arXiv preprint
JianmingLiao. Enhancinghnswindexforreal-timeup- arXiv:2409.00135,2024.
dates:Addressingunreachablepointsandperformance
[81] Qianxi Zhang,Shuotao Xu,Qi Chen,Guoxin Sui,Ji-
degradation. arXivpreprintarXiv:2407.07871,2024.
adong Xie, Zhizhen Cai, Yaoqi Chen, Yinxuan He,
[71] FangyuanXu,WeijiaShi,andEunsolChoi. Recomp: Yuqing Yang, Fan Yang, et al. VBASE : Unifying
{ }
Improvingretrieval-augmentedlmswithcontextcom- onlinevectorsimilaritysearchandrelationalqueriesvia
pression and selective augmentation. In The Twelfth relaxedmonotonicity. In17thUSENIXSymposiumon
16

OperatingSystemsDesignandImplementation(OSDI
23),pages377–395,2023.
[82] Zeyu Zhang,Xiaohe Bo,Chen Ma,Rui Li,Xu Chen,
QuanyuDai,JiemingZhu,ZhenhuaDong,andJi-Rong
Wen. A survey on the memory mechanism of large
languagemodelbasedagents,2024. URLhttps://arxiv.
org/abs/2404.13501.
[83] ZhihaoZhang,AlanZhu,LijieYang,YihuaXu,Lanting
Li,PhitchayaMangpoPhothilimthana,andZhihaoJia.
Acceleratingretrieval-augmentedlanguagemodelserv-
ingwithspeculation. arXivpreprintarXiv:2401.14021,
2024.
[84] Zili Zhang,Fangyue Liu,Gang Huang,Xuanzhe Liu,
and Xin Jin. Fast vector query processing for large
datasetsbeyond GPU memorywithreorderedpipelin-
{ }
ing. In21stUSENIXSymposiumonNetworkedSystems
Design and Implementation (NSDI 24),pages 23–40,
2024.
[85] WeijieZhao,ShulongTan,andPingLi. Song:Approxi-
matenearestneighborsearchongpu.In2020IEEE36th
InternationalConferenceonDataEngineering(ICDE),
pages1033–1044.IEEE,2020.
[86] Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie,
Chuyue Livia Sun, Jeff Huang, Cody Hao Yu, Shiyi
Cao,ChristosKozyrakis,IonStoica,JosephEGonzalez,
etal. Sglang:Efficientexecutionofstructuredlanguage
modelprograms. Advancesinneuralinformationpro-
cessingsystems,37:62557–62583,2024.
[87] ShuruiZhong,DinghengMo,andSiqiangLuo. Lsm-
vec:Alarge-scaledisk-basedsystemfordynamicvector
search. arXivpreprintarXiv:2505.17152,2025.
[88] WanjunZhong,LianghongGuo,QiqiGao,HeYe,and
YanlinWang. Memorybank:Enhancinglargelanguage
modelswithlong-termmemory. InProceedingsofthe
AAAIConferenceonArtificialIntelligence,volume38,
pages19724–19731,2024.
17
