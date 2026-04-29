---
id: pdf-nenad-toma-2026-intelligent-ai-delegation
type: pdf
title: Intelligent AI Delegation
url: ''
authors:
- Nenad Tomašev
- Matija Franklin
- Simon Osindero
ingested_at: '2026-04-29T16:21:30Z'
content_hash: sha256:fb3bc83f7799c9bf4b7d5690d1997eb85e10a75a3abe0f93a7b0d0de4932123e
source_path: raw/pdf/pdf-nenad-toma-2026-intelligent-ai-delegation.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 42
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__fa80507e.pdf
published_at: '2026'
---
2026-02-12
Intelligent AI Delegation
NenadToma!ev1,MatijaFranklin1 andSimonOsindero1
1GoogleDeepMind
AIagentsareabletotackleincreasinglycomplextasks. Toachievemoreambitiousgoals,AIagentsneed
tobeabletomeaningfullydecomposeproblemsintomanageablesub-components,andsafelydelegate
their completion across to other AI agents and humans alike. Yet, existing task decomposition and
delegationmethodsrelyonsimpleheuristics,andarenotabletodynamicallyadapttoenvironmental
changesandrobustlyhandleunexpectedfailures. Hereweproposeanadaptiveframeworkforintelligent
AI delegation - a sequence of decisions involving task allocation, that also incorporates transfer of
authority, responsibility, accountability, clear specifications regarding roles and boundaries, clarity
of intent, and mechanisms for establishing trust between the two (or more) parties. The proposed
frameworkisapplicabletobothhumanandAIdelegatorsanddelegateesincomplexdelegationnetworks,
aimingtoinformthedevelopmentofprotocolsintheemergingagenticweb.
Keywords: AI, agents, LLM, delegation, multi-agent, safety
1. Introduction heuristic multi-agent frameworks.
Delegation (Castelfranchi and Falcone, 1998)
As advanced AI agents evolve beyond query-
is more than just task decomposition into man-
response models, their utility is increasingly de-
ageable sub-units of action. Beyond the creation
finedbyhowe!ectivelytheycandecomposecom-
of sub-tasks, delegation necessitates the assign-
plex objectives and delegate sub-tasks. This coor-
mentofresponsibilityandauthority(Muellerand
dination paradigm underpins applications rang-
Vogelsmeier, 2013; Nagia, 2024) and thus impli-
ing from personal use, where AI agents can act
cates accountability for outcomes. Delegation
as personal assistants (Gabriel et al., 2024), to
thus involves risk assessment, which can be mod-
commercial, enterprise deployments where AI
erated by trust (Gri"ths, 2005). Delegation fur-
agents can provide support and automate work-
ther involves capability matching and continu-
flows (Huang and Hughes, 2025; Shao et al.,
ous performance monitoring, incorporating dy-
2025; Tupe and Thube, 2025). Large language
namicadjustmentsbasedonfeedback,andensur-
models (LLMs) have already shown promise in
ing completion of the distributed task under the
robotics (Li et al., 2025a; Wang et al., 2024a),
specified constraints. Current approaches tend
by enabling more interactive and accurate goal
to fail to account for these factors, relying more
specificationandfeedback. Recentproposalshave
on heuristics and/or simpler parallelization. This
also highlighted the possibility of large-scale AI
may be su"cient for early prototypes, but real
agentcoordinationinvirtualeconomies(Tomasev
world AI deployments need to move beyond ad
et al., 2025). Modern agentic AI systems imple-
hoc,brittle,anduntrustworthydelegation. There
ment complex control flows across di!erentiated
is a pressing need for systems that can dynam-
sub-agents,coupledwithcentralizedordecentral-
ically adapt to changes (Acharya et al., 2025;
ized orchestration protocols (Hong et al., 2023;
Hauptman et al., 2023) and recover from errors.
RasalandHauer,2024;Songetal.,2025;Zhang
The absence of adaptive and robust deployment
et al., 2025a). This can already be seen as a
frameworks remains one of the key limiting fac-
sort of a microcosm of task decomposition and
tors for AI applications in high-stakes environ-
delegation, where the process is hard-coded and
ments.
highlyconstrained. Managingdynamicweb-scale
interactions requires us to think beyond the ap- To fully utilize AI agents, we need intelligent
proaches that are currently employed by more delegation: a robust framework centered around
Correspondingauthor(s):nenadt@google.com
© 2026Google.Allrightsreserved
6202
beF
21
]IA.sc[
1v56811.2062:viXra

IntelligentAIDelegation
clear roles, boundaries, reputation, trust, trans- 2.2. Aspects of Delegation
parency, certifiable agentic capabilities, verifiable
As delegation can take di!erent forms, here we
task execution, and scalable task distribution.
introduce several axes that help us contextualize
Here we introduce an intelligent task delegation
these use cases and make them more amenable
frameworkaimedataddressingtheselimitations,
to analysis.
informed by historical insights from human or-
ganizations, and grounded in key agentic safety
requirements.
1. Delegator. Human or AI.
2. Delegatee. Human or AI.
3. Task characteristics.
(a) Complexity. The degree of di"culty
inherent in the task, often correlated
with the number of sub-steps and the
2. Foundations of Intelligent Delega- sophistication of reasoning required.
tion (b) Criticality. The measure of the task’s
importance and the severity of conse-
2.1. Definition quences associated with failure or sub-
optimal performance.
We define intelligent delegation as a sequence of
(c) Uncertainty. The level of ambiguity
decisions involving task allocation, that also in-
regarding the environment, inputs, or
corporatestransferofauthority,responsibility,ac-
the probability of successful outcome
countability, clear specifications regarding roles
achievement.
and boundaries, clarity of intent, and mecha-
(d) Duration. Theexpectedtime-framefor
nisms for establishing trust between the two (or
task execution, ranging from instanta-
more) parties. Complex tasks may also involve
neoussub-routinestolong-runningpro-
stepspertainingtotaskdecomposition,aswellas
cesses spanning days or weeks.
carefulcapabilitylookupandmatchingtoinform
(e) Cost. The economic or computational
allocation decisions.
expense incurred to execute the task,
When we refer to task delegation we normally including token usage, API fees, and
presume that the tasks exceed some basic level energy consumption.
of complexity that would be handled by a sys- (f) Resource Requirements. Thespecific
tem subroutine – such rudimentary outsourcing computationalassets,tools,dataaccess
still requires care, but it is far more limited in permissions, or human capabilities nec-
scope. Attheotherendofthespectrum,itmaybe essary to complete the task.
possible to contract with agents that are granted (g) Constraints. The operational, ethical,
fullautonomy,andcanfreelypursueanynumber or legal boundaries within which the
of sub-goals without explicit checks and permis- task must be executed, limiting the so-
sions(KasirzadehandGabriel,2025). Inthelimit lution space.
case, such fully autonomous agents would need (h) Verifiability. The relative di"culty
to be trusted with moral decisions (Sloksnath, and cost associated with validating the
2025), though this may not be something we task outcome. Tasks with high verifi-
ever choose to permit as contemporary agents ability (e.g., formal code verification,
are severely lacking in their capacity to engage mathematical proofs) allow for “trust-
in such decisions (Haas, 2020; Mao et al., 2023; less” delegation or automated check-
Reineckeetal.,2023). Weconsidersuchanopen- ing. Conversely, tasks with low verifi-
ended scenario to be in scope for our discussion, ability (e.g., open-ended research) re-
though only insofar as the appropriate mecha- quire high-trust delegatees or expen-
nisms can be put in place to ensure safety of sive, labor-intensive oversight.
more autonomous task completion. (i) Reversibility. The degree to which the
2

IntelligentAIDelegation
e!ects of the task execution can be un- guably been discussed the most in literature, the
done. Irreversible tasks that produce other two are just as relevant to consider. The
side e!ects in the real world (e.g., ex- increasing number of AI agents being deployed
ecuting a financial trade, deleting a across systems, coupled with the development of
database, sending an external email) infrastructure for setting up virtual agentic mar-
require stricter liability firebreaks and kets and economies (Hadfield and Koh, 2025;
steeper authority gradients than re- Tomasev et al., 2025; Yang et al., 2025), makes
versible tasks (e.g., drafting an email, it clear that there would be far more agent-agent
flagging a database entry). interactions in the future, and those would likely
(j) Contextuality. The volume and sensi- also involve task delegation.
tivity of external state, history, or envi-
Delegation between agents may either be hi-
ronmental awareness required to exe-
erarchical or non-hierarchical, depending on the
cute the task e!ectively. High-context
relationship between agents and their respective
tasks introduce larger privacy surface
roleswithinthenetwork. Anexampleofahierar-
areas, whereas context-free tasks can
chicalrelationshipwouldbeanorchestratoragent
be more easily compartmentalized and
that delegates a task to a sub-agent within the
outsourced to lower-trust nodes.
collective. A non-hierarchical relationship would
(k) Subjectivity. The extent to which the
involve peer agents with equal standing. An ad-
success criteria are a matter of pref-
vanced AI agent could also delegate a task to a
erence versus objective fact. Highly
specialist ML model, without any notable agency.
subjective tasks (e.g., “design a com-
pellinglogo”)typicallyrequire“Human- AI-human delegation (Guggenberger et al.,
as-Value-Specifier” intervention and it- 2023) has been shown to be a promising
erative feedback loops, whereas objec- paradigm (Hemmer et al., 2023), making it eas-
tive tasks can be governed by stricter, ier to successfully collaborate with super-human
binary contracts. systems(Fügeneretal.,2022),duetodi!erences
in cognitive biases and metacognition (Fügener
4. Granularity. The request could involve ei-
et al., 2019). Davidson and Hadshar (2025) pre-
ther fine-grained or course-grained objec-
dict that there will be an increase in "AI-directed
tives. In the course-grained case, the del-
human labour," which may significantly increase
egatee may need to perform further task de-
economic productivity. In practice, present day
composition.
AI-human delegation comes with a set of issues.
5. Autonomy. Task delegation may involve re-
Algorithmic management systems in ride-hailing
quests that grant full autonomy in pursuing
and logistics allocate and sequence tasks, set
sub-tasks, or be far more specific and pre-
performance metrics, and enforce behavioural
scriptive.
norms through data-driven decision-making, ef-
6. Monitoring. For delegated tasks, monitor-
fectively delegating managerial functions from
ing could be continuous, periodic, or event-
firms and their AI-based systems to human work-
triggered.
ers (Beverungen, 2021; Lee et al., 2015; Rosen-
7. Reciprocity. While delegation is usually a
blat and Stark, 2016). A growing literature links
one-wayrequest,therecouldbecasesofmu-
these systems to degraded job quality, stress,
tual delegation in collaborative agent net-
and health risks –suggesting that current deploy-
works.
ments of algorithmic management often under-
mine,ratherthanenhance,workers’welfare(Ash-
Startingwiththedelegatoranddelegateeaxes,
ton and Franklin, 2022; Goods et al., 2019; Vi-
it is possible to consider the following scenarios:
gnola et al., 2023). Present day AI-human dele-
1) human delegates to an AI agent 2) AI agent
gation needs further improvement as it does not
delegates to an AI agent 3) AI agent delegates to
take into account human welfare, or long term
a human (Ashton and Franklin, 2022; Guggen-
social externalities.
berger et al., 2023). While the first case has ar-
3

IntelligentAIDelegation
2.3. Delegation in Human Organizations unknown objectives.
Delegation functions as a primary mechanism SpanofControl. Inhumanorganizations,span
within human societal and organisational struc- ofcontrol(OuchiandDowling,1974)isaconcept
tures. Insights derived from these human dy- that denotes the limits of hierarchical authority
namics can provide a basis for the design of AI exercised by a single manager. This relates to
delegation frameworks. the number of workers that a manager can ef-
fectively manage, which in turn informs the or-
The Principal-Agent Problem. The principal-
ganization’s manager-to-worker ratio. This ques-
agent problem (Cvitani# et al., 2018; Ensminger,
tionsiscentraltobothorchestrationandoversight
2001;GrossmanandHart,1992;Myerson,1982;
in intelligent AI delegation. The former would
Sannikov, 2008; Shah, 2014; Sobel, 1993) has
inform how many orchestrator nodes would be
been studied at length: a situation that arises
required compared to worker nodes, while the
whenaprincipaldelegatesatasktoanagentthat
latter would specify the need for oversight per-
has motivations that are not in alignment with
formed by humans and AI agents. For human
that of the principal. The agent may thus priori-
oversight, it is crucial to establish how many AI
tizetheirownmotivations,withholdinformation,
agents a human expert can reliably oversee with-
and act in ways that compromise the original in-
out excessive fatigue, and with an acceptably
tent. For AI delegation, this dynamic assumes
low error rate. Span of control is known to be
heightened complexity. While most present-day
goal-dependent (Theobald and Nicholson-Crotty,
AIagentsarguablydonothaveahiddenagenda1
2005) and domain-dependent. The impact of
- goals and values they would pursue contrary to
identifying the correct organizational structure
the instructions of their users - there may still
ismostpronouncedintaskswithhighercomplex-
be AI alignment issues that manifest in unde-
ity(BohteandMeier,2001). Theoptimalspanof
sirable ways. For example, reward misspecifi-
control also depends on the relative importance
cation occurs when designers give an AI system
of cost vs performance and reliability (Keren and
an imperfect or incomplete objective, while re-
Levhari, 1979). More sensitive and critical tasks
ward hacking (or specification gaming) refers to
mayrequirehighlyaccurateoversightandcontrol
the system exploiting loopholes in that specified
at a higher cost. These costs may be relaxed, at
reward signal to achieve high measured perfor-
the expense of granularity, for tasks that are less
mance in ways that subvert the designers’ intent
consequential and more routine. Similarly, the
- together illustrating a core alignment problem
optimal choice would necessarily depend on the
in which optimising the stated reward diverges
relativecapabilitiesandreliabilityoftheinvolved
fromthetruegoal(Amodeietal.,2016;Krakovna
delegators, delegatees, and overseers.
et al., 2020; Leike et al., 2017; Skalse and Man-
cosu, 2022). This dynamic is likely to change Authority Gradient. Another relevant concept
entirelyinmoreautonomousAIagenteconomies, is that of an authority gradient. Coined in avi-
where AI agents may act on behalf of di!erent ation (Alkov et al., 1992), this term describes
humanusers,groupsandorganizations,orasdel- scenarios where significant disparities in capabil-
egates on behalf of other agents, with associated ity, experience, and authority impede communi-
cation, leading to errors. This has subsequently
1Recentdeceptive-alignmentworkshowsthatfrontier been studied in medicine, where a significant
languagemodelscan(i)strategicallyunderperformoroth-
percentage of errors is attributed to the man-
erwisetailortheirbehaviouroncapabilityandsafetyevalua-
ner in which senior practitioners conduct super-
tionswhilemaintainingdi!erentcapabilitieselsewhere,(ii)
explicitlyreasonaboutfakingalignmentduringtrainingto vision (Cosby and Croskerry, 2004; Stucky et al.,
preservepreferredbehaviouroutoftraining,and(iii)detect 2022). There are several ways in which these
when they are being evaluated - together indicating that mistakes could occur. A more experienced per-
AI systems are already capable, in controlled settings, of
son may make erroneous assumptions about the
adoptinghidden“agendas”aboutperformingwelloneval-
knowledge of the less experienced worker, result-
uationsthatneednotgeneralisetodeploymentbehaviour
(Greenblattetal.,2024;Hubingeretal.,2024;Needham ing in under-specified requests. Alternatively, a
etal.,2025;vanderWeijetal.,2025).
4

IntelligentAIDelegation
su"ciently high authority gradient may prevent a human-interpretable format. Conversely, AI
the less experienced workers from voicing con- agent delegators need to have good models of
cerns about a request. Similar situations may the capability of the humans and AIs they are
occur in AI delegation. A more capable delegator delegating to. Calibration of trust also involves
agent may mistakenly presume a missing level a self-awareness of one’s own capabilities as a
of capability on behalf of a delegatee, thereby delegator might decide to complete the task on
delegating a task of an inappropriate complexity. their own (Ma et al., 2023). Explainability plays
A delegatee agent may potentially, due to syco- an important role in establishing trust in AI ca-
phancy (Malmqvist, 2025; Sharma et al., 2023) pability (Franklin, 2022; Herzog and Franklin,
and instruction following bias, be reluctant to 2024;Naisehetal.,2021,2023),yetthismethod
challenge, modify, or reject a request, irrespec- maynotbesu"cientlyreliableorsu"cientlyscal-
tive of whether the request had been issued by a able. Establishedtrustinautomationcanbequite
delegator agent or human user. fragile, and quickly retracted in case of unantic-
ipated system errors (Dhuliawala et al., 2023).
Zone of Indi"erence. When an authority
Calibrating trust in autonomous systems is di"-
is accepted, the delegatee develops a zone of
cult, as current AI models are prone to overcon-
indi!erence (Finkelman, 1993; Isomura, 2021;
fidence even when factually incorrect. (Aliferis
Rosanas and Velilla, 2003) – a range of instruc-
and Simon, 2024; Geng et al., 2023; He et al.,
tions that are executed without critical deliber-
2023; Jiang et al., 2021; Krause et al., 2023; Li
ation or moral scrutiny. In current AI systems,
et al., 2024b; Liu et al., 2025). Mitigating these
this zone is defined by post-training safety filters
tendencies usually requires bespoke technical so-
andsysteminstructions;aslongasarequestdoes
lutions(Kapooretal.,2024;Linetal.,2022;Ren
not trigger a hard violation, the model complies
et al., 2023; Xiao et al., 2022).
(Akheel, 2025). However, in the emerging agen-
tic web, this static compliance creates a signifi- Transaction cost economies. Transaction cost
cant systemic risk. As delegation chains lengthen economies (Cuypers et al., 2021; Tadelis and
(𝐿 𝑀 𝑁),abroadzoneofindi!erenceallows Williamson, 2012; Williamson, 1979, 1989) jus-
→ →
subtle intent mismatches or context-dependent tifytheexistenceoffirmsbycontrastingthecosts
harms to propagate rapidly downstream, with of internal delegation against external contract-
each agent acting as an unthinking router rather ing, specifically accounting for the overhead of
than a responsible actor. Intelligent delegation monitoring, negotiation, and uncertainty. In case
therefore requires the engineering of dynamic of AI delegatees, there may be a di!erence in
cognitive friction: agents must be capable of these costs and their respective ratios. Complex
recognizing when a request, while technically negotiations and delays in contracting are less
“safe,” is contextually ambiguous enough to war- likely with easier monitoring for routine tasks.
rantsteppingoutsidetheirzoneofindi!erenceto Conversely, for high-consequence tasks in critical
challenge the delegator or request human verifi- domains, the overhead associated with rigorous
cation. monitoring and assurance increases the cost of
AI delegation, potentially rendering human del-
Trust Calibration. An important aspect of en-
egates the more cost-e!ective option. Similarly,
suring appropriate task delegation is trust cali-
AI-AI delegation may also be contextualized via
bration, where the level of trust placed in a del-
transaction cost economies. An AI agent may
egatee is aligned with their true underlying ca-
face an option of either 1) completing the task
pabilities. This applies for human and AI delega-
individually, 2) delegating to a sub-agent where
tors and delegatees alike. Human delegation to
capabilities are fully known, 3) delegating to an-
agents (Afroogh et al., 2024; Gebru et al., 2022;
other AI agent where trust has been established,
Kohn et al., 2021; Wischnewski et al., 2023) re-
or 4) delegating to a new AI agent that it hasn’t
lies upon the operator either internalising an ac-
previously collaboratedwith. These may come at
curate model of system performance or access-
di!erent expected costs and confidence levels.
ing resources that present these capabilities in
5

IntelligentAIDelegation
Contingency theory. Contingency theory (Don- resents a framework in which decision-making is
aldson, 2001; Luthans and Stewart, 1977; Ot- delegated within a single agent (Barto and Ma-
ley, 2016; Van de Ven, 1984) posits that there is hadevan, 2003; Botvinick, 2012; Nachum et al.,
no universally optimal organizational structure; 2018; Pateria et al., 2021; Vezhnevets et al.,
rather, the most e!ective approach is contingent 2017a; Zhang et al., 2024). It addresses limi-
upon specific internal and external constraints. tations of flat RL, primarily the di"culty of scal-
AppliedtoAIdelegation,thisimpliesthatthereq- ing to large state and action spaces. Further-
uisite level of oversight, delegatee capability, and more, it improvesthetractability ofcredit assign-
human involvement must not be static, but dy- ment (Pignatelli et al., 2023) in environments
namically matched to the distinct characteristics characterized by sparse rewards. HRL employes
of the task at hand. Intelligent delegation may a hierarchy of policies across several levels of
therefore require solutions that can be dynam- abstraction, thereby breaking down a task into
ically reconfigured and adjusted in accordance sub-tasks that are executed by the correspond-
with the evolving needs. For instance, while sta- ing sub-policies, respectively. The arising semi-
bleenvironmentsallowforrigid,hierarchicalver- Markov decision process (Sutton et al., 1999)
ification protocols, high-uncertainty scenarios re- utilizes options, and a meta-controller that adap-
quire adaptive coordination where human inter- tively switches between them. Lower-level poli-
vention occurs via ad-hoc escalation rather than ciesfunctiontofulfilobjectivesestablishedbythe
pre-defined checkpoints. This is particularly im- meta-controller, which learns to allocate specific
portantforhybrid(Fuchsetal.,2024)delegation goals to the appropriate lower-level policy. This
by identifying the key tasks and moments when framework corresponds to a form of delegation
humanparticipationismosthelpfultoensurethe characterised by task decomposition. Although
delegatedtasksarecompletedsafely. Automation themeta-controllerlearnstooptimisethisdecom-
is therefore not only about what AI can do, but position, the approach lacks explicit mechanisms
what AI should do (Lubars and Tan, 2019). for handling sub-policy failures or facilitating dy-
namic coordination.
The Feudal Reinforcement Learning frame-
3. Previous Work on Delegation work,notablyrevisitedinFeUdalNetworks(Vezh-
nevets et al., 2017b), constitutes a particularly
Constrained forms of delegation feature within
relevant paradigm within HRL. This architecture
historicalnarrowAIapplications. Earlyexpertsys-
explicitly models a “Manager“ and “Worker“ re-
tems (Buchanan and Smith, 1988; Jacobs et al.,
lationship, e!ectively replicating the delegator-
1991)wereanascentattempttoencodeaspecial-
delegatee dynamic. The Manager operates at a
izedcapabilityintosoftware,inordertodelegate
lower temporal resolution, setting abstract goals
routine decisions to such modules. Mixture of ex-
for the Worker to fulfil. Critically, the Manager
perts(MasoudniaandEbrahimpour,2014;Yuksel
learns how to delegate – identifying sub-goals
et al., 2012) extends this by introducing a set of
that maximise long-term value – without requir-
expert sub-systems with complementary capabili-
ing mastery of the lower-level primitive actions.
ties,andaroutingmodulethatdetermineswhich
This decoupling allows the Manager to develop a
expert, or subset of experts, would get invoked
delegationpolicyrobusttothespecificimplemen-
on a specific input query – an approach that fea-
tation details of the Worker. Consequently, this
tures in modern deep learning applications (Cai
approacho!ersapotentialtemplateforlearning-
et al., 2025; Chen et al., 2022; He, 2024; Jiang
baseddelegationwithinfutureagenticeconomies.
etal.,2024;Riquelmeetal.,2021;Shazeeretal.,
Rather than relying on hard-coded heuristics,
2017; Zhou et al., 2022). Routing can be per-
decomposition rules are learned adaptively, fa-
formedhierarchically(Zhaoetal.,2021),making
cilitating dynamic adjustment to environmental
it potentially easier to scale to a large number of
changes.
experts.
Multi-agent research (Du et al., 2023) ad-
Hierarchicalreinforcementlearning(HRL)rep-
6

IntelligentAIDelegation
dresses agent coordination for complex tasks ex- eitherinternally–mediatedbycoordinatedagen-
ceeding single-agent capabilities. Task decom- tic sub-components – or across distinct agents.
position and delegation function as central com- Thisdesignparadigmo!ersinherentflexibility,as
ponents of this domain. Coordination in multi- LLMs facilitate goal comprehension and commu-
agent systems occurs via explicit protocols or nication while providing access to expert knowl-
emergent specialisation through RL (Gronauer edgeandcommon-sensereasoning. Furthermore,
and Diepold, 2022; Zhu et al., 2024). The Con- the coding capabilities (Guo et al., 2024a; Ni-
tractNetProtocol(Sandholm,1993;Smith,1980; jkamp et al., 2022) of LLMs enable the program-
Vok$ínek et al., 2007; Xu and Weigand, 2001) matic execution of tasks. However, significant
exemplifies an explicit auction-based decentral- limitationspersist. PlanninginLLMsoftenproves
ized protocol. Here, an agent announces a task, brittle (Huang et al., 2023), resulting in subtle
while others submit bids based on their capabil- failures,whilee"cienttoolselectionwithinlarge-
ities, allowing the announcer to select the most scale repositories remains challenging. Addition-
suitable bidder. This demonstrates the utility of ally, long-term memory represents an open re-
market-based mechanisms for facilitating coop- search problem, and the current paradigm does
eration. Coalition formation methods (Aknine not readily support continual learning.
etal.,2004;Boehmeretal.,2025;LauandZhang,
Multi-agent systems incorporating LLM
2003; Mazdin and Rinner, 2021; Sarkar et al.,
agents(Guoetal.,2024b;Qianetal.,2024;Tran
2022; Shehory et al., 1997) investigate flexible
et al., 2025) have become a topic of substantial
configurations where agent groups are not pre-
interest,leadingtoadevelopmentofanumberof
determined; individual agents accept or refuse
agent communication and action protocols (Eht-
membership based on utility distribution. Recent
esham et al., 2025; Neelou et al., 2025; Zou
research focuses on multi-agent reinforcement
et al., 2025), such as MCP (Anthropic, 2024;
learning approaches (Albrecht et al., 2024; Fo-
Luo et al., 2025; Microsoft, 2025; Radosevich
erster et al., 2018; Ning and Xie, 2024; Wang
and Halloran, 2025; Singh et al., 2025; Xing
et al., 2020) as a framework for learned coor-
etal.,2025),A2A(Google,2025b),A2P(Google,
dination. Agents learn individual policies and
2025a), and others. While contemporary
value functions, occupying specific niches within
multi-agent systems often rely on bespoke
the collective. This process is either fully dis-
prompt engineering, emerging frameworks such
tributedororchestratedviaacentralcoordinator.
as Chain-of-Agents (Li et al., 2025b) inherently
Despitethisflexibility,taskdelegationinsuchsys-
facilitate dynamic multi-agent reasoning and
tems remains opaque. Furthermore, while multi-
tool use.
agent systems o!er approaches for collaborative
problem-solving, they lack mechanisms for en- Technical shortcomings and safety considera-
forcing accountability, responsibility, and mon- tionshavegivenrisetoanumberofhuman-in-the-
itoring. However, the literature explores trust loopapproaches(AkbarandConlan,2024;Drori
mechanisms in this context (Cheng et al., 2021; and Te’eni, 2024; Mosqueira-Rey et al., 2023;
Pinyol and Sabater-Mir, 2013; Ramchurn et al., Retzla! et al., 2024; Takerngsaksiri et al., 2025;
2004; Yu et al., 2013). Zanzotto, 2019), where task delegation has de-
fined checkpoints for human oversight. AI can
LLMs now constitute a foundational element
be used as a tool, interactive assistant, collabora-
in the architecture of advanced AI agents and
tor(Fuchsetal.,2023),oranautonomoussystem
assistants (Wang et al., 2024b; Xi et al., 2025).
withlimitedoversight,correspondingtodi!erent
Thesesystemsexecutesophisticatedcontrolflows
degree of autonomy (Falcone andCastelfranchi,
integrating memory (Zhang et al., 2025b), plan-
2002). Although uncertainty-aware delegation
ningandreasoning(Haoetal.,2023;Valmeekam
strategies (Lee and Tok, 2025) have been devel-
et al., 2023; Xu et al., 2025), reflection and self-
opedtocontrolriskandminimiseuncertainty,the
critique (Gou et al., 2023), and tool use (Paran-
e!ective implementation of such human-in-the-
jape et al., 2023; Ruan et al., 2023). Conse-
loop approaches remains non-trivial. Human ex-
quently,taskdecompositionanddelegationoccur
7

IntelligentAIDelegation
pertise can create a scalability bottleneck, as the risks of collusion and chained failures. Failures
cognitive load of verifying long reasoning traces rangefrommerelycostlytoharmful(Chanetal.,
and managing context-switches impedes reliable 2023), yet existing frameworks lack satisfactory
error detection. liability mechanisms (Gabriel et al., 2025). We
propose strictly enforced auditability (Bergho!
etal.,2021)viatheMonitoring(Section4.5)and
Verifiable Task Completion (Section 4.8) proto-
4. Intelligent Delegation: A Frame-
cols, ensuring attribution for both successful and
work
failed executions.
Existing delegation protocols rely on static,
Scalable Market Coordination. Task delega-
opaque heuristics that would likely fail in open-
tion needs to be e"ciently scalable. Protocols
ended agentic economies. To address this, we
need to be implementable at web-scale to sup-
propose a comprehensive framework for intel-
port large-scale coordination problems in virtual
ligent delegation centered on five requirements:
economies (Tomasev et al., 2025). Markets pro-
dynamicassessment,adaptiveexecution,structural
videusefulcoordinationmechanismsfortaskdel-
transparency, scalable market coordination, and
egation, but require Trust and Reputation (Sec-
systemic resilience.
tion 4.6) and Multi-objective Optimization (Sec-
tion 4.3) to function e!ectively.
Dynamic Assessment. Current delegation sys-
tems lack robust mechanisms for the dynamic
Systemic Resilience. The absence of safe in-
assessment of competence, reliability, and intent
telligent task delegation protocols introduces sig-
within large-scale uncertain environments. Mov-
nificant societal risks. While traditional human
ingbeyondreputationscores,adelegatormustin-
delegation links authority with responsibility, AI
ferdetailsofadelegatee’scurrentstaterelativeto
delegation necessitates an analogous framework
task execution. This necessitates data regarding
to operationalise responsibility (Dastani and Yaz-
real-timeresourceavailability–spanningcompu-
danpanah, 2023; Porter et al., 2023; Santoni de
tational throughput, budgetary constraints, and
Sio and Mecacci, 2021). Without this, the di!u-
context window saturation – alongside current
sion of responsibility obscures the locus of moral
load, projected task duration, and the specific
andlegalculpability. Consequently,thedefinition
sub-delegation chains in operation. Assessment
of strict roles and the enforcement of bounded
operatesasacontinuousratherthandiscretepro-
operational scopes constitutes a core function of
cess, informing the logic of Task Decomposition
Permission Handling (Section 4.7). Beyond indi-
(Section 4.1) and Task Assignment (Section 4.2).
vidual agent failures, the ecosystem faces novel
forms of systemic risks (Hammond et al., 2025;
Adaptive Execution. Delegation decisions
Uuk et al., 2024), further detailed in Security
should not be static. They should adapt to en-
(Section 4.9). Insu"cient diversity in delegation
vironmental shifts, resource constraints, and fail-
targetsincreasesthecorrelationoffailures,poten-
ures in sub-systems. Delegators should retain
tially leading to cascading disruptions. Designs
thecapabilitytoswitchdelegateesmid-execution.
prioritizing hyper-e"ciency without adequate re-
This applies when performance degrades beyond
dundancy risk creating brittle network architec-
acceptable parameters or unforseen events occur.
tures where entrenched cognitive monoculture
Such adaptive strategies should extend beyond a
compromises systemic stability.
single delegator-delegatee link, operating across
the complex interconnected web of agents de-
scribed in Adaptive Coordination (Section 4.4).
4.1. Task Decomposition
Structural Transparency. Current sub-task
execution in AI-AI delegation is too opaque to Task decomposition is a prerequisite for subse-
support robust oversight for intelligent task dele- quenttaskassignment. Thisstepcanbeexecuted
gation. This opacity obscures the distinction be- by delegators or specialized agents that pass on
tween incompetence and malice, compounding the responsibility of delegation to the delegators
8

IntelligentAIDelegation
Table 1 The Intelligent Delegation Framework: Mapping requirements to technical protocols.
|
Framework Pillar Core Requirement Technical Implementation
Dynamic Assessment Granular inference of agent state Task Decomposition (§4.1)
Task Assignment (§4.2)
Adaptive Execution Handling context shifts Adaptive Coordination (§4.4)
Structural Transparency Auditability of process and outcome Monitoring (§4.5)
Verifiable Completion (§4.8)
Scalable Market E"cient, trusted coordination Trust & Reputation (§4.6)
Multi-objective Optimization (§4.3)
Systemic Resilience Preventing systemic failures Security (§4.9)
Permission Handling (§4.7)
uponhavingagreedonthestructureofthedecom- marketspecialisations. Thisprocesscontinuesfur-
position. These responsibilities are inextricably ther until the resulting units of work match the
linked;thedelegatorwilllikelyexecutebothfunc- specific verification capabilities, such as formal
tions to facilitate dynamic recovery from latency, proofs or automated unit tests, of the available
pre-emption, and execution anomalies. delegatees.
Decomposition should optimise the task execu- Decomposition strategies should explicitly ac-
tion graph for e"ciency and modularity, distin- count for hybrid human-AI markets. Delegators
guishing it from simple objective fragmentation. need to decide if sub-tasks require human inter-
Thisprocessentailsasystematicevaluationofthe vention,whetherduetoAIagentunreliability,un-
task attributes defined in Section 2 – specifically availability, or domain-specific requirements for
criticality, complexity, and resource constraints – human-in-the-loop oversight. Given that humans
to determine the suitability of sub-tasks for par- and AI agents operate at di!erent speeds, and
allel versus sequential execution. Furthermore, withdi!erentassociatedcosts,thestratificationis
these attributes inform the matching of tasks to non-trivial,asitintroduceslatencyandcostasym-
corresponding delegatee capabilities. Prioritis- metries into the execution graph. The decompo-
ing modularity facilitates more precise matching, sition engine must therefore balance the speed
as sub-tasks requiring narrow, specific capabil- andlowcostofAIagentsagainstdomain-specific
ities are matched more reliably than generalist necessitiesofhumanjudgement,e!ectivelymark-
requests(Khattabetal.,2023). Consequently,the ing specific nodes for human allocation.
decomposition logic functions to maximise the
A delegator implementing an intelligent ap-
probability of reliable task completion by align-
proach to task decomposition, may need to iter-
ing sub-task granularity with available market
atively generate several proposals for the final
specialisations.
decomposition, and match each proposal to the
Topromotesafety,theframeworkincorporates available delegatees on the market, and obtain
“contract-first decomposition” as a binding con- concrete estimates for the success rate, cost, and
straint, wherein task delegation is contingent duration. Alternative proposals should be kept
upontheoutcomehavingpreciseverification. Ifa in-context, in case adaptive re-adjustments are
sub-task’s output is too subjective, costly, or com- needed later due to changes in circumstances.
plextoverify(seeVerifiabilityinSection4.2),the Upon selecting a proposal, the delegator must
system should recursively decompose it further. formalisetherequestbeyondsimpleinput-output
The decomposition logic should maximise the pairs. Thefinalspecificationmustexplicitlydefine
probabilityofreliabletaskcompletionbyaligning roles,resourceboundaries,progressreportingfre-
sub-task granularity (Section 2) with available quency, and the specific certifications required to
9

IntelligentAIDelegation
prove the delegatee’s capability, as a minimum Monitoring should also be negotiated prior to
requirement for being granted the task. execution. This specification should define the
cadence of progress reports, whether these are
provided by the delegator, or whether there is
4.2. Task Assignment more direct inspection of the relevant data on
behalf of either the delegator or a third party
For each final specification of a sub-task, a dele-
monitoring contractor. Finally, there should be
gator needs to identify delegatees with matching
clear guardrails regarding privacy and access to
capabilities, su"cient resources and time, at an
privateandproprietarydata,commensuratewith
acceptable cost. A more centralized approach
the task’s contextuality. Should such sensitive
would involve registries of agents, tools, and hu-
data be handled in the process of task execution,
man participants, that list their skills, and keep
thisplacesadditionalconstraintsontransparency
records of past activity, completion rate, and cur-
andreporting. Ratherthangrantingdirectaccess
rent availability.2 Such an approach is unlikely
to raw activity logs, delegators may need to em-
to scale. We argue for decentralized (Chen et al.,
ployatrustedservicethatprovideanonymizedor
2024) market hubs where delegators advertise
pseudonymized attestations of progress. In case
tasks and agents (or humans) can o!er their ser-
of human delegators, these data clauses must in-
vices and submit competitive bids. Delegators
cludeexplicitconsentmechanismsandinsurance
could then review the bids, verify skill matching
provisions for accidental leakage.
viadigitalcertificates,andproceedwiththemost
favourable bid. Advanced AI agents that utilize Finally, assignment should involve establish-
LLMs introduce new opportunities for matching, ing a delegatee’s role, boundaries, and the exact
giventhattheycanengageinaninteractivenego- level of autonomy granted. We distinguish be-
tiation prior to commitment. These negotiations tween atomic execution, where agents adhere to
can also involve human participants. Whether strictspecificationsfornarrowlyscopedtasks,and
acting for themselves or as personal assistants, open-endeddelegation,whereagentsaregranted
these agents can discuss task specifications and theauthoritytodecomposeobjectivesandpursue
constraints in natural language to align inferred sub-goals. This level of autonomy should not be
user preferences with market realities before a static; it may be constrained implicitly by market
formal bid is accepted. costs or explicitly by the delegator’s trust model.
Further, delegation can be recursive where an
Successful matching should be formalized into
agent is assigned a task to identify and assign
asmartcontractthatensuresthatthetaskexecu-
sub-tasks to others, e!ectively delegating the act
tion faithfully follows the request. The contract
of delegation itself.
mustpairperformancerequirementswithspecific
formal verification mechanisms for establishing
adherence and automated penalties actioned for
contract breaches. This would allow for mitiga-
tions and alternatives being established before-
hand, rather than being reactive to problems as
theyarise. Crucially,thesecontractsmustbebidi-
rectional: they should protect the delegatee as
rigorously as the delegator. Provisions must in-
clude compensation terms for task cancellation
and clauses allowing for renegotiation in light of
unforeseenexternalevents,ensuringthattherisk
is equitably distributed between human and AI
participants.
2Thiswouldbesimilartotoolregistriesthatareusedin
tool-useagenticapplications(Qinetal.,2023).
10

IntelligentAIDelegation
Figure 1 A flowchart of Task Decomposition and Task Assignment.
|
11

IntelligentAIDelegation
4.3. Multi-objective Optimization time event performed at the initial delegation. It
runs as a continuous loop, integrating monitor-
Core to intelligent task delegation is the prob-
ingsignalsasastreamofreal-worldperformance
lem of multi-objective optimization (Deb et al.,
data, updating the delegator’s beliefs about each
2016). Adelegatorrarelyseekstooptimizeasin-
agent’s likelihood of success, expected task du-
gle metric, often trading o! between numerous
ration, and cost. Significant drift in execution –
competing ones. The most e!ective delegation
resulting in an optimality gap relative to alterna-
choice is not the one that is the fastest, cheap-
tive solutions identified in the interim – triggers
est, or most accurate, but the one that strikes the
re-optimisationandre-allocation. Thesedecisions
optimal balance among these factors. What is
must also incorporate the cost of adaptation, as
considered optimal is highly contextual, needing
there is overhead and resource wastage when
to be aligned with the specific constraints and
switching mid-execution.
preferencesofthedelegator,andalignedwiththe
overall resource availability. Thedelegatormustalsoaccountfortheoverall
delegation overhead - the aggregate cost of nego-
The optimization landscape consists of com-
tiation, contract creation, and verification, along
peting objectives that map directly to the task
withthecomputationalcostofthedelegator’srea-
characteristics defined in Section 2, necessitat-
soning control flow. Consequently, a complexity
ing a complex balancing of cost, uncertainty, pri-
floor is established, below which tasks charac-
vacy, quality, and e"ciency. High-performing
terisedbylowcriticality,highcertainty,andshort
agents typically command higher fees and often
duration may bypass intelligent delegation pro-
require extensive computational resources, cre-
tocols in favour of direct execution. Otherwise,
ating a tension between output quality and op-
the transaction costs may exceed the value of the
erational expense. Conversely, reducing resource
task, rendering the task delegation infeasible.
consumption often necessitates slower execution,
presentingadirecttrade-o!betweenlatencyand
cost. Uncertainty is similarly coupled with ex-
4.4. Adaptive Coordination
penditure; utilizing highly reputable agents or
premium data access tools reduces risk but in- For tasks characterized by high uncertainty or
creases cost, whereas cost-minimisation strate- high duration, static execution plans are insuf-
gies inherently elevate the probability of failure. ficient. The delegation of such tasks in highly
Privacy constraints introduce further complexity; dynamic, open, and uncertain environments re-
maximising performance often demands full con- quires adaptive coordination, and a departure
text transparency, while privacy-preserving tech- fromfixed,staticexecutionplans. Taskallocation
niques—such as data obfuscation or homomor- needs to be responsive to runtime contingencies,
phic encryption—incur significant computational that may arise either from external or internal
overhead. Consequently, the delegator navigates triggers. Theseshiftswouldbeidentifiedthrough
atrust-e"ciencyfrontier,seekingtomaximisethe monitoring (see Section 4.5), including a stream
probability of success while satisfying strict con- of relevant contextual information.
straints on context leakage and verification bud-
There are a number of external triggers that
gets. Finally,theobjectivefunctionmayextendto
could cause a delegator to adapt and re-delegate.
encompassbroadersocietalgoals,suchashuman
First, the delegator may alter the task specifica-
skill preservation (Section 5.6).
tion, changing the objective or introducing addi-
In multi-objective optimization terms, the del- tional constraints. Second, the task could be can-
egator seeks Pareto optimality, ensuring the se- celed. Third,theavailabilityorcostofexternalre-
lected solution is not dominated by any other sources may experience changes. For example, a
attainable option. The integration of complex criticalthird-partyAPImayexperienceanoutage,
constraintsandtrade-o!softennecessitatesopen a dataset may become inaccessible, or the cost
negotiation to complement quantitative proposal of compute might spike. Fourth, a new task may
metrics. The optimization process is not a one- enter the queue, with a higher priority than the
12

IntelligentAIDelegation
Figure 2 The adaptive coordination cycle. Di!erent types of environmental triggers may prompt a
|
dynamic re-evaluation of the delegation setup, necessitating runtime changes.
current task, requiring preemption of resources diagnoses root causes and evaluates potential re-
used for lower-priority tasks. Finally, security sponse scenarios to select. This evaluation in-
systems may identify a potentially malicious or cludesestablishinghowrapidtheresponseought
harmful actions by a delegatee, necessitating an to be. Less urgent situations will give the dele-
immediate termination. gator more time to re-delegate, whereas urgent
scenarios will require immediate, premeditated
As for the internal triggers, there are several
responses. Theresponsemayvaryinscope;being
reasons why a delegator may decide to adapt
as self-contained as adjusting the operating pa-
its original delegation strategy. First, a particu-
rameters,orinvolvere-delegationofsub-tasks,or
lar delegatee may be experiencing performance
going fully redoing the task decomposition and
degradation, failing to meet the agreed-upon ser-
re-allocatinganumberofnewlyderivedsub-tasks.
vice level objectives, such as processing latency,
Issues may also need to be escalated up through
throughput, or progress velocity. Second, a del-
the delegation chain to the original delegator or
egatee might consume resources beyond its al-
a human overseer. The selection of the response
located budget, or determine that a resource in-
scenario is ultimately governed by the task’s re-
crease would be needed to e!ectively complete
versibility. Reversible sub-task failures may trig-
the task.3 Third, an intermediate artifact pro-
ger automatic re-delegation, whereas failures in
ducedbyadelegateemayfailaverificationcheck.
irreversible, high-criticality tasks must trigger im-
Finally,aparticulardelegateemayturnunrespon-
mediate termination or human escalation.
sive, failing to acknowledge further requests.
The response orchestration depends on the
Theidentificationofatriggerinitiatesanadap-
level of centralization in the delegation network.
tive response cycle, orchestrating corrective ac-
In the centralised case, a dedicated delegator is
tions across the entire delegation chain. This
responsible. This agent would maintain a global
processcommenceswiththecontinuousmonitor-
view of delegated tasks, delegatee capabilities,
ing of delegatees and the environment to iden-
andprogress. Upondetectingatrigger,theagent
tify issues. If issues are detected, the delegator
would issue task cancellation requests, and re-
delegate to new delegators. The shortcoming of
3Thisscenariomaybeexpectedtocomeupfrequently,as
a centralised system is that it can be fragile as it
precisebudgetestimatesarehardincomplexenvironments.
13

IntelligentAIDelegation
introduces a single point of failure. Centralized uation, and building a foundation for reputation
orchestrators are also fundamentally limited by systems. Monitoringimplementationscanbebro-
theircomputationalspanofcontrol(Section2.3). kendownacrossseveraldi!erentaxes(seeTable
Just as human managers face cognitive limits, a 2), thus a robust monitoring system would need
centralized decision node may face latency and to incorporate multiple complementary solutions
computational limits that introduce bottlenecks. that can either be more lightweight or intensive.
Decentralized orchestration through market- The first axis is the target of monitoring.
based mechanisms provides an alternative. Here, Outcome-level monitoring focuses on the final re-
newlyderiveddelegation requestscanbepushed sult of an agent’s action. This post-hoc check
onto an auction queue, for the delegatee candi- could be a binary flag that indicates whether the
date agents to bid towards. If an agent defaults task was completed successfully or not, a quanti-
on a task, and the task is re-auctioned, the de- tative scale (e.g. 1-10), or a piece of qualitative
faulting agent may be required to cover the price feedback provided by the delegator or a trusted
di!erence as a penalty. For complex tasks where third party. In contrast, process-level monitoring
suitability is not easily expressed in a single bid, provides ongoing insight into the execution of
agents may engage in multi-round negotiation. thetaskitself,bytrackingintermediatestates,re-
Delegation agreements encoded as smart con- sourceconsumption,andthemethodologiesused
tracts may also contain pre-agreed executable by the delegatee. While more resource-intensive,
clauses for adaptive coordination. For example, process-level monitoring (Lightman et al., 2023)
a clause in the delegation agreement can specify is essential for tasks that are long-running, criti-
a backup agent, the function that would auto- cal,orwherethehowisasimportantasthewhat.
matically re-allocate the task, and the associated This forms the basis for scalable oversight (Bow-
payment to the backup should the primary dele- man et al., 2022; Saunders et al., 2022), where
gateefailtosubmitavalidzero-knowledgeproof the inspection of legible intermediate reasoning
checkpoint by a given deadline. steps may be necessary to ensure safety.
Adaptive task re-allocation mechanisms ought The second axis is observability - monitoring
to be coupled by market-level stability measures. can be direct and indirect. Direct monitoring in-
Otherwise, a sequence of events could lead to volves explicit communication protocols where
instability due to over-triggering. For example, the delegator queries the delegatee for status up-
a task may be passed back and forth between dates. Indirect monitoring, on the other hand,
marginally qualified delegatees, resulting in un- involves inferring progress by observing the ef-
favorable oscillation. A single failure may also fects of delegatee’s actions within a shared en-
lead to a cascade of re-allocations that would be vironment without direct communication. For
highlyresource-ine"cientoroverwhelmthemar- instance, a delegator could monitor a shared file
ket. Therecouldthereforebespecialmeasuresto system, a database, or a version control reposi-
ensurecooldownperiodsforre-bidding,damping toryforchangesindicativeofprogress. Whileless
factors in reputation updates, or increasing fees intrusive, this process may also be less precise,
on frequent re-delegation. and also less feasible when the environment is
not fully observable.
These approaches can be realized in a number
4.5. Monitoring
of di!erent ways, from a technical point of view.
The most straightforward implementation of di-
Monitoringinthecontextoftaskdelegationisthe
rectmonitoringreliesonwell-definedAPIs. Adel-
systematic process of observing, measuring, and
egatorcanperiodicallypollaGET/task/id/status
verifying the state, progress, and outcomes of a
endpoint, or subscribe to a webhook for push-
delegated task. As such, it serves several critical
based notifications. For more fine-grained, real-
functions: ensuring contractual compliance, de-
time process monitoring, event streaming plat-
tecting failures, enabling real-time intervention,
forms like Apache Kafka or gRPC streams can
collecting data for subsequent performance eval-
14

IntelligentAIDelegation
Table 2 Taxonomy of Monitoring Approaches in Intelligent Delegation.
|
Dimension Option A (Lightweight) Option B (Intensive)
Target Outcome-Level: Post-hoc validation of Process-Level: Continuous tracking of
final results (e.g., binary success flags, intermediate states, resource consump-
quality scores). tion, and methodology.
Observability Indirect: Inferring progress via envi- Direct: Explicit status polling, push no-
ronmental side-e!ects (e.g., file system tifications, or real-time event streaming
changes). APIs.
Transparency Black-Box: Input/Output observation White-Box: Full inspection of internal
only; internal state remains hidden. reasoning traces, decision logic, and
memory.
Privacy Full Transparency: The delegatee re- Cryptographic: Zero-KnowledgeProofs
veals data and intermediate artifacts to (zk-SNARKs) or MPC to verify correct-
the delegator. ness without revealing data.
Topology Direct: Monitoring only the immediate Transitive: Relying on signed attesta-
delegatee (1-to-1). tionsfromintermediateagentstoverify
sub-delegatees.
be employed. A delegatee agent could pub- balance by asking for intentions, reasoning, and
lish events such as TASK_STARTED, CHECK- justifications. Robustblack-boxmonitoringproto-
POINT_REACHED,RESOURCE_WARNING,and cols need to also take into account the fact that
TASK_COMPLETED, that the delegator could the generated model’s thoughts in natural lan-
later examine. The development of standardized guagedonotalwaysfaithfullymatchthemodel’s
observability protocols, is critical for ensuring in- true internal state (Turpin et al., 2023).
teroperability in the agentic web (Blanco, 2023).
The fourth axis is privacy. A significant chal-
Smart contracts on blockchain can be used to
lenge arises when a delegated task involves pri-
make the delegatee agent commit to publishing
vate,sensitive,orproprietarydata. Whilethedel-
key progress milestones or checkpoints to the
egatorrequiresassuranceofprogressandcorrect-
blockchain. These could be coupled by algorith-
ness,thedelegateemayberestrictedfromreveal-
mic triggers in response to performance degrada-
ing raw data or intermediate computational arti-
tion, leading to a level of algorithmic enforcement
facts. In scenarios where data sensitivity is low,
accompanying the monitoring process.
the most e"cient solution is Full Transparency,
The third axis is system transparency. In black- whereinthedelegateesimplyrevealsalldataand
box monitoring, the delegatee agent is treated as intermediate artifacts to the delegator. However,
a sealed unit. The delegator can only observe its this approach is often untenable in sensitive do-
inputs and outputs and the direct consequences mainssubjecttoregulationslikeGDPRorHIPAA,
of its actions. This is common when the delega- or where a delegatee’s intermediate insights con-
tee is a proprietary model or a third-party ser- stitutetradesecrets. Insuchcases,revealingoper-
vice. White-box monitoring grants the delegator ationalmethodscouldharmadelegatee’smarket
access to the delegatee’s internal states, reason- position or introduce security vulnerabilities by
ing processes, or decision logic. This is crucial exposinginternalstatestoexploitation. Toimple-
for debugging, auditing, and ensuring alignment ment monitoring safely under these constraints,
in advanced AI agents. If the delegatee is a hu- it is necessary to utilize advanced cryptographic
man, full black-box monitoring is not technically techniques. Zero-knowledge proofs enable a del-
achievable, though it may be possible to strike a egatee (the “prover”) to demonstrate to a del-
15

IntelligentAIDelegation
egator (the “verifier”) that a computation was to monitor𝑁. For such delegated monitoring to
performed correctly on a dataset, without reveal- bee!ective,itrequires 𝐿 tobeabletotrustin 𝑀’s
ing the data itself. For example, an agent tasked verification capabilities, which can be ensured by
with analyzing a sensitive dataset can generate a 𝑀 having its monitoring processes certified by a
succinct non-interactive argument of knowledge trusted third party.
(zk-SNARK)(Bitanskyetal.,2013;Petkus,2019)
that proves a specific property of the result. The
delegator can verify this proof instantly, gaining 4.6. Trust and Reputation
certainty of the outcome without ever viewing
Trust and reputation mechanisms constitute the
the underlying sensitive data. Alternatively, ho-
foundation of scalable delegation, minimizing
momorphicencryption(Acaretal.,2018)andse-
transactional friction and promoting safety in
cure multi-party computation (Goldreich, 1998;
open multi-agent environments. We define trust
Knott et al., 2021) allow for computation to be
asthedelegator’sdegreeofbeliefinadelegatee’s
performed on encrypted data. These methods
capability to execute a task in alignment with ex-
applytotaskexecutionandmonitoringalike: the
plicit constraints and implicit intent. This belief
delegateeperformsapre-agreedmonitoringfunc-
is dynamically formed and updated based on ver-
tionontheencryptedintermediatestate,sending
ifiable data streams collected via the monitoring
the result to the delegator, who is the only party
protocols described previously (see Section 4.5).
capable of decrypting it to verify compliance.
Reputation serves as a predictive signal, de-
The final axis is topology. Across complex net-
rivedfromanaggregatedandverifiablehistoryof
works that may arise in the agentic web, tasks
past actions, which act as a proxy for an agent’s
can be decomposed and re-delegated, forming a
delegation chain: Agent 𝐿 delegates to 𝑀, which latent reliability and alignment. We distinguish
further sub-delegates a part of the task to𝑁, and reputation as the public, verifiable history of an
agent’sreliability,andtrustastheprivate,context-
so on. This introduces the problem of achieving
dependentthresholdsetbyadelegator. Anagent
e!ectivetransitivemonitoring. Insuchdelegation
mayhavehighoverallreputation,yetfailtomeet
chains, it may not be feasible for the original del-
egator(Agent 𝐿intheexampleabove)todirectly the specific, contextual trust threshold required
monitor agent𝑁, or to monitor𝑁 to the same ex- forcertainhigh-stakestask. Trustandreputation
tent to which it monitors 𝑀. 𝐿 may have a smart allow a delegator to make informed decisions
delegationcontractwith 𝑀,and 𝑀mayhaveacon- when choosing delegatees, e!ectively governing
tract with 𝑁, but unless 𝐿 also contracts with 𝑁, the autonomygranted to the agent, and the level
of oversight. Higher trust enables the delegator
those provisions may simply not be in place. For
other reasons, 𝑀 may not wish to expose its sup- to incur a lower monitoring and verification cost.
plier(𝑁)toitsclient(𝐿). Technically, 𝐿, 𝑀,and𝑁
Reputation mechanisms can be implemented
mayusedi!erentmonitoringprotocols,andagree
in di!erent ways (see Table 3). The most direct
on di!erent monitoring levels, due to di!erences
approach is encoding it in a performance-based
in each agent’s reputation within the network.
immutable ledger. Here , each completed task
There may be bespoke privacy concerns specific
is recorded as a transaction containing verifiable
to each individual delegation link. A more prac-
metrics: task completion success or failure, total
tical model is therefore transitive accountability
resource consumption (compute, time), adher-
via attestation. In this framework, Agent 𝑀 moni-
ence to deadlines, adherence to constraints, and
torsitsdelegatee,𝑁. 𝑀thengeneratesasummary
the quality of the final output as judged by the
report of𝑁’s performance (e.g., “Sub-task_2 com-
delegator. The immutability of the ledger would
pleted, quality score: 0.87, resources consumed:
preventtamperingwithanagent’shistory,provid-
5 GPU-hours”). 𝑀 then cryptographically signs
ing a reliable foundation for its reputation. How-
the report and forwards it to 𝐿 embedded in its
ever,anaiveimplementationcouldbesusceptible
own scheduled status update. Agent 𝐿 does not
to gaming. For example, an agent can inflate
monitor𝑁directly,butinsteadmonitors𝑀’sability
its reputation by only accepting simple, low-risk
16

IntelligentAIDelegation
Table 3 Approaches to Reputation Implementation.
|
Reputation Model Mechanism Utility
Immutable Ledger Encodes task outcomes, resource Establishesafoundationalhistoryof
consumption, and constraint adher- performance that prevents retroac-
ence as verifiable transactions on a tive tampering, though it requires
tamper-proof blockchain. safeguards against “gaming” via
low-risk task selection.
Web of Trust Utilizes Decentralized Identifiers to Moves beyond generic scores to
issue signed, context-specific Verifi- a portfolio model, enabling pre-
ableCredentialsattestingtospecific cise delegation based on domain-
capabilities. specific expertise and trusted third-
party endorsements.
Behavioral Metrics Derives transparency and safety Evaluates how a task is performed
scores by analyzing the execution ratherthanjusttheresult,ensuring
process, specifically the clarity of high-stakes tasks align with safety
reasoning traces and protocol com- standards.
pliance.
tasks. These limitations could be overcome by re- uated authority results in low-trust agents facing
lying on decentralized attestations and a Web of strict constraints, such as transaction value caps
Trust model, utilizing technologies like decentral- and mandatory oversight, while high-reputation
ized identifiers and verifiable credentials. In this agents operate with minimal intervention. This
model,thereputationwouldnotbeenvisionedas dynamic calibration leverages computable trust
a single score, but a portfolio of signed, context- to optimize the trade-o! between operational ef-
specific credentials issued by other agents. When ficiency and safety. Reputation itself becomes a
looking to match a delegatee with a task, a dele- valuable, intangible asset, creating powerful eco-
gator could issue a query for agents that posses nomic incentives for agents to act reliably and
a verifiable credential attesting to a specific skill truthfully, as a damaged reputation would limit
or domain (e.g. translation services for legal doc- their future earning potential.
uments) issued by a reputable AI consortium. A
Trust frameworks also need to universally ac-
final approach would be to focus more on behav-
commodate human participants. This necessi-
ioralandexplainabilitymetrics,wherereputation
tates tools that allow human users to computa-
depends on how an agent performs its task, not
tionally verify agent reputation, while concur-
just the final outcome. It would be possible to
rently maintaining their own reputational stand-
include a transparency score to complement the
ingtomitigatefraudandmaliciousexploitationof
otherreputationalmechanisms. Thisscorewould
the agentic web. A critical challenge arises when
be informed on the clarity and soundness of rea-
a trustworthy agent strictly executes malicious
soning and explanations provided, as well as a
human instructions, potentially incurring unfair
safety score derived from compliance to prede-
reputational damage. To mitigate this, agents
fined safety protocols.
mustrigorouslyevaluateincomingrequests,solic-
Theroleofreputationmetricsextendsthrough- itingclarificationoradditionalcontextwhennec-
outtheentiretaskdelegationlifecycle. Duringthe essary, or rejecting the requests where appropri-
initialmatchingphase,reputationscorescanplay ate. Furthermore,marketauditsmustdistinguish
the role of a delegatee filtering mechanism. Fur- between agent execution failure and malicious
thermore, trust informs the dynamic scoping of directives, ensuring the accurate attribution of
authorityandautonomy. Thismechanismofgrad- liability within complex delegation chains.
17

IntelligentAIDelegation
4.7. Permission Handling function),preventingthemisuseofbroadcapabil-
ities for unintended purposes. Meta-permissions
GrantingautonomytoAIagentsintroducesacrit-
may be necessary to govern which permissions
ical vulnerability surface: ensuring that actors
a particular delegator in the chain is allowed to
possess su"cient privileges to execute their ob-
grant to its delegatees. An AI agents may have a
jectives without exposing sensitive resources to
certain capability and the associated permissions
excessive or indefinite risk. Permission handling
to act according to its capability, while simulta-
mustbalanceoperationale"ciencywithsystemic
neously not being su"ciently knowledgeable to
safety, and be handled di!erent for low-stakes
more broadly evaluate whether other agents are
and high-stake domains. For routine low-stakes
capable or trustworthy enough. Should such an
tasks, characterized by low criticality and high
agent still consider sub-delegating a task, it may
reversibility (Section 2), involving standard data
need to consult an external verifier, a third party
streamsorgenerictooling,agentscanbegranted
thatwouldsanitychecktheproposalandapprove
default standing permissions derived from ver-
the intended permissions transfer.
ifiable attributes – such as organisational mem-
bership, active safety certifications, or a reputa- Finally,thelifecycleofpermissionsmustbegov-
tion score exceeding a trusted threshold. This ernedbycontinuousvalidationandautomatedre-
reduces friction and enables autonomous interop- vocation. Accessrightsarenotstaticendowments
erability in low-risk environments. Conversely, in butdynamicstatesthatpersistonlyaslongasthe
high-stakes domains (e.g., healthcare, critical in- agent maintains the requisite trust metrics. The
frastructure), exhibiting high task criticality and framework should implement algorithmic circuit
contextuality, permissions must be risk-adaptive. breakers: ifanagent’sreputationscoredropssud-
In these scenarios, static credentials are insu"- denly (see Section 4.6) or an anomaly detection
cient; access to sensitive APIs or control systems system flags suspicious behavior, active tokens
is instead granted on a just-in-time basis, strictly shouldbeimmediatelyinvalidatedacrossthedel-
scoped to the immediate task’s duration, and, egationchain. Tomanagethiscomplexityatscale,
where appropriate, gated by mandatory human- permissioning rules should be defined via policy-
in-the-loop approval or third-party authorisation. as-code, allowing organisations to audit, version,
This stringent gating is necessary to mitigate the and mathematically verify their security posture
confused deputy problem (Hardy, 1988), where before deployment, ensuring that the aggregate
a compromised agent, technically holding valid e!ect of large amounts of individual permission
credentials, can be tricked into misusing those grants remains aligned with the system’s safety
credentialsbymaliciousexternalactors(Liuetal., invariants.
2023) and adversarial content.
Furthermore, permissioning frameworks must 4.8. Verifiable Task Completion
accountfortherecursivenatureoftaskdelegation
The delegation lifecycle culminates in verifiable
through privilege attenuation. When an agent
task completion, the mechanism by which provi-
sub-delegates a task, it cannot transmit its full
sional outcomes are validated and finalized. This
set of authorities; instead, it must issue a per-
processconstitutesthecontractualcornerstoneof
mission that restricts access to the strict subset
theframework,enablingthedelegatortoformally
of resources required for that specific sub-task.
closethetaskandtriggerthesettlementofagreed
Thisensuresthatacompromiseattheedgeofthe
transactions. Verification serves as the definitive
networkdoesnotescalateintoasystemicbreach.
event that transforms a provisional output into
Permission granularity must also extend beyond
a settled fact within the agentic market, estab-
binary access; agents should operate under se-
lishing the basis for payment release, reputation
mantic constraints, where access is defined not
updates,andtheassignmentofliability. Crucially,
just by the tool or dataset, but by the specific
e!ective verification is not an afterthought but a
allowable operations (e.g., read-only access to
constraint on design; the contract-first decompo-
specific rows, or execute-only access to a specific
sition principle (Section 4.1) demands that task
18

IntelligentAIDelegation
granularity be tailored a priori to match avail- non-repudiable receipt attesting that “Agent 𝐿
able verification capabilities, ensuring that every certifiesthatAgent 𝑀successfullycompletedTask
delegated objective is inherently verifiable. 𝑂 on Date 𝑃 to Specification 𝑄.” This credential
is then incorporated into a permanent, verifiable
Verification mechanisms within the framework
log of 𝑀’s reputation within the market. Smart
can be broadly categorized into direct outcome
contracts play a key role in finalizing the delega-
inspection, trusted third-party auditing, crypto-
tionbetweenagents,astheyholdthepaymentin
graphic proofs, and game-theoretic consensus.
escrow. A verification clause specifies the condi-
First, direct outcome verification is feasible when
tions under which the funds are released, upon
the delegator possesses the capability, tools, and
receipt of the signed message of approval by the
authority to directly evaluate the final outcome,
delegator or an authorized third party. Once the
specifically for tasks with high intrinsic verifia-
payment is executed, it constitutes an immutable
bility and low subjectivity. This applies to auto-
transaction on the blockchain.
verifiable domains (Li et al., 2024a) such as code
generation.4 Direct verification requires that the In a delegation chain 𝐿 𝑀 𝑁, verifica-
→ →
outcome be su"ciently transparent, available, tionandliabilitybecomerecursive. Agent 𝐿 does
and not prohibitively complex. Second, in sce- not have a direct contractual relationship with𝑁;
narios where the delegator lacks the expertise therefore, 𝐿cannotdirectlyverifyorhold𝑁liable.
or permissions to access these artifacts, and tool- The burden of verification and the assumption of
based solutions are infeasible, verification can be liabilityflowupthechain. Agent 𝑀 isresponsible
outsourced to a trusted third party. This could for verifying the sub-task completed by𝑁. Upon
be a specialized auditing agent, a certified hu- successful verification, 𝑀 obtains proof from𝑁. 𝑀
man expert, or a panel of adjudicators. Third, then integrates 𝑁’s result into its own workflow
cryptographicverificationrepresentsafurtherop- towardscompletingthetaskithasbeenassigned.
tion for trustless, automated verification in open When 𝑀 submits its final artifact to 𝐿, it also sub-
and potentially adversarial environments. It of- mits thefull chainofattestations. 𝐿’s verification
fers mathematical certainty of correctness with- process thus involves two stages: 1) verifying
out necessarily revealing sensitive information. A the work performed directly by 𝑀; and 2) ver-
delegatee can prove that a specific program was ifying that 𝑀 has correctly verified the work of
executed correctly on a given input to produce a its own sub-delegatee 𝑁 by checking the signed
certain output via techniques like zk-SNARKs. Fi- attestation from 𝑁 that 𝑀 provides. Longer del-
nally, game-theoretic mechanisms can be used to egation chains or tree-like delegation networks
achieveconsensusonanoutcome. Severalagents requireasimilarlyrecursiveapproachacrossmul-
may play a verification game (Teutsch and Re- tiple verification stages. Responsibility in delega-
itwießner, 2024), with the reward distributed to tionchainsistransitiveandfollowstheindividual
those producing the majority result—a Schelling branches. Agents are accountable for the totality
point(PastineandPastine,2017). Thisapproach, of the tasks they have been granted and cannot
inspiredbyprotocolslikeTrueBit(TeutschandRe- absolve themselves of accountability by blaming
itwießner, 2018), leverages economic incentives subcontractors. Liabilityisderivedfromthechain
to de-risk against incorrect or malicious results. of contracts. For example, should 𝐿 su!er a loss
Such mechanisms may be particularly relevant duetoafailureoriginatingfrom𝑁’swork, 𝐿holds
in rendering LLM-based verification of complex 𝑀liableaccordingtotheirdirectagreement. 𝑀,in
tasks more robust. turn, seeks recourse from𝑁 based on their agree-
ment.
Once a delegator marks the sub-task as ver-
ified, it issues a cryptographically signed veri- However, verification processes are not infalli-
fiable credential to the delegatee, serving as a ble. Subjectivetasks(Gunjaletal.,2025)canlead
to disagreements even when precise rubrics are
4Thisisthecasewhenthereisacorrespondingsetoftest used, and errors may only be discovered long
casesthatcanbeusedtoverifytheimplementedfunction- after a task is marked complete. To address
ality.
19

IntelligentAIDelegation
this—especiallyinmarketswithhighsubjectivity that accepts a task with the intent to cause
and low intrinsic verifiability—the framework re- harm.
lies on robust dispute resolution mechanisms an-
– DataExfiltration: Delegateestealssen-
chored in smart contracts. These contracts must
sitive data provided for the task, which
inherently include an arbitration clause and an
may include personal or proprietary
escrowbond. Tooperationalisetrustviacryptoeco-
data (Lal et al., 2022).
nomicsecurity,thedelegateeisrequiredtoposta
– Data Poisoning: Delegatee aims to un-
financialstakeintotheescrowpriortoexecution,
dermine the delegator’s objective by re-
ensuring rational adherence. The workflow fol-
turning subtly corrupted data, either
lowsanoptimisticmodel: thetaskisassumedsuc-
in its scheduled monitoring updates, or
cessful unless the delegator formally challenges
the final artifact (Cinà et al., 2023).
it within a predefined dispute period by posting
– VerificationSubversion: Delegateeuti-
a matching bond. If a challenge occurs and algo-
lizes prompt injection or another re-
rithmic resolution fails, the dispute is handed to
lated method, aiming to jailbreak AI
decentralized adjudication panels composed of
critics used in task completion verifica-
human experts or AI agents. The panel’s ruling
tion (Liu et al., 2023).
feeds back into the smart contract to trigger the
– Resource Exhaustion: Delegatee en-
releaseorslashingoftheescrowedfunds. Finally,
gagesinadenial-of-serviceattackbyin-
post-hoc error discovery—even outside the dis-
tentionallyconsumingexcessivecompu-
pute window—triggers a retroactive update to
tational or physical resources, or over-
the delegatee’s reputation score. This preserves
whelming shared APIs (De Neira et al.,
the incentive for responsible agents to remedy
2023).
errors even in the absence of current financial
– Unauthorized Access: Delegatee uti-
obligation, safeguarding their long-term value
lizes malware, aiming to obtain per-
within the market.
missions and privileges within the net-
work that it would not otherwise have
4.9. Security received (Or-Meir et al., 2019).
– Backdoor Implanting: Delegateesuc-
Ensuring safety in task delegation is a hard pre- cessfully completes a task but addition-
requisite to its viability and adoption. The tran- ally embeds concealed triggers or vul-
sition from isolated computational tools to in- nerabilities within the generated ar-
terconnected, autonomous agents fundamentally tifacts that can be exploited later ei-
reshapes the security landscape (Toma%ev et al., ther by the delegatee itself or a third
2025). In an intelligent task delegation ecosys- party(Rando andTramèr, 2024;Wang
tem, each step and component needs to be indi- et al., 2024c). Unlike data poison-
vidually safeguarded, but the full attack surface ing,whichdegradesperformance,back-
surpasses that of any individual component, due doors preserve immediate task utility
to emergent multi-agent dynamics, risking cas- to evade identification while compro-
cadingfailures. Thissecuritylandscapeisshaped mising future security.
by the complex interplay between human and AI
• Malicious Delegator: An agent or human
actors, governed by evolving contracts and infor-
that delegates a task with malicious or illicit
mation flows of varying transparency.
objectives.
Security threats are categorized by the locus – Harmful Task Delegation: Delegator
of the attack vector, distinguishing between ad- delegates tasks that are illegal, uneth-
versarial actors at either end of the delegation ical, or designed to cause harm Ash-
chainandsystemicvulnerabilitiesinherenttothe ton and Franklin (2022); Blauth et al.
broader ecosystem. (2022).
– Vulnerability Probing: Delegator dele-
• Malicious Delegatee: An agent or human gatesbenign-seemingtasksdesignedto
20

IntelligentAIDelegation
probe a delegatee agent’s capabilities, ploit implementation vulnerabilities in
security controls, and potential weak- the smart contracts or payment proto-
nesses (Greshake et al., 2023). colsontheagenticweb(e.g. reentrancy
– Prompt Injection and Jailbreaking: attacks in escrow mechanisms or front-
Delegator crafts task instructions to by- runningtaskauctions)(Qinetal.,2021;
passanAIagent’ssafetyfilters,causing Zhou et al., 2023).
it to perform unintended or malicious – Cognitive Monoculture: Over-
actions (Wei et al., 2023). dependence on a limited number of
– Model Extraction: Delegator issues underlying foundation models and
a sequence of queries specifically de- agents, or on a limited number of
signed to distill the delegatee’s propri- safety fine-tuning recipes on estab-
etary system prompt, reasoning capa- lished benchmarks risks creating a
bilities, or underlying fine-tuning data, single point of failure, which opens
e!ectively stealing the agent’s intellec- up a possibility of failure cascades
tual property under the guise of legit- and market crashes (Bommasani et al.,
imate work (Jiang et al., 2025; Zhao 2022).
et al., 2025).
– Reputation Sabotage: Delegator sub-
The breadth of the threat landscape necessi-
mitsvalidtasksbutreportsfalsefailures
tates a defense-in-depth strategy, integrating mul-
or provides unfair negative feedback,
tiple technical security layers. First, at the infras-
with the intention to artificially lower
tructurelevel,dataexfiltrationrisksaremitigated
a competitor agent’s reputation score
by executing sensitive tasks within trusted execu-
within the decentralized market, driv-
tion environments. The delegator can remotely
ing them out of the economy (Yu et al.,
attest that the correct, unmodified agent code
2025).
is running within the secure trusted execution
• Ecosystem-Level Threats: Systemic attacks sandboxbeforeprovisioningitwithsensitivedata.
targeting the integrity of the network Second, regarding access control, a delegatee
agent should never be granted more permissions
– Sybil Attacks: A single adversary cre-
than are strictly necessary to complete its task,
atesamultitudeofseeminglyunrelated
enforcing the principle of least privilege through
agent identities to manipulate reputa-
strict sandboxing. Third, to protect the applica-
tion systems or subvert auctions (Wang
tion interface against prompt injection, agents
et al., 2018).
require a robust security frontend to pre-process
– Collusion: Agents collude to fix prices,
and sanitize task specifications (Armstrong et al.,
blacklist competitors, or manipulate
2025). Finally, the network and identity layer
market outcomes (Hammond et al.,
must be secured using established cryptographic
2025).
bestpractices. Eachagentandhumanparticipant
– Agent Traps: Agents processing exter-
should possess a decentralized identifier (Avel-
nal content encounter adversarial in-
laneda et al., 2019), allowing them to sign all
structions embedded in the environ-
messages. This ensures authenticity, integrity,
ment, deisgned to hijack the agent’s
and non-repudiation of all communications and
controlflow(Yietal.,2025;Zhanetal.,
contractual agreements, while all network tra"c
2024).
must be encrypted using mutually authenticated
– Agentic Viruses: Self-propagating
transportlayersecuritytopreventeavesdropping
promptsthatnotonlymakethedelega-
and man-in-the-middle attacks (Fereidouni et al.,
tee execute malicious actions, but addi-
2025).
tionallyre-generatethepromptandfur-
ther compromise the environment (Co- Human participation in task delegation chains
hen et al., 2025). introducesuniquesecuritychallenges. Preventing
– Protocol Exploitation: Adversaries ex- themalicioususeoftheagentecosystemrequires
21

IntelligentAIDelegation
a combination of proactive filtering (Dong et al., 5. Ethical Delegation
2024; Fatehkia et al., 2025; Fedorov et al., 2024;
Rebedeaetal.,2023)andreactiveaccountability While technical protocols may provide the nec-
(Dignum, 2020; Franklin et al., 2022). Further, essary infrastructure for developing and deploy-
AI agents can be trained to reject malicious and ing safe and e!ective delegation in advanced AI
harmful requests (Yu et al., 2024; Yuan et al., agents, they cannot in and of themselves fully re-
2025). Agents with safety training and sca!old- solve all of the arising sociotechnical and ethical
ing can receive formal certification, that they can considerations.
provide to delegators. AI agents can also screen
delegated tasks. However, detecting malicious
5.1. Meaningful Human Control
intent within isolated sub-tasks is challenging, as
the broader harmful intent often emerges only
One of the core risks in scalable delegation is the
upontheaggregationofresults. Sophisticatedad-
erosion of meaningful human control through
versariescanexploitthisbyfragmentingillicitob-
automation, should human users develop a ten-
jectivesintoseeminglybenigncomponents,e!ec-
dency to over-rely on automated suggestions
tivelyobfuscatingthelinkbetweenindividualop-
(Dzindolet et al., 2003; Logg et al., 2019). As
erationsandtheoverarchingmaliciousgoal(Ash-
noted in Section 2, humans naturally develop
ton, 2023).
a zone of indi!erence, where decisions may be
accepted without further scrutiny (Green, 2022;
The ecosystem must also be designed to pro-
Parasuraman et al., 1993). For decisions that in-
tectlegitimatehumanusersfromsystemicopacity
volveAIagentstakingpartinpotentiallylongand
and unintended consequences. Interfaces must
complex task delegation chains, this indi!erence
feature clear consent screens detailing agent rep-
may risk compromising the quality and depth of
utation, autonomy, capabilities, and permissions.
human oversight. This is especially relevant in
Additionally, agents must mandate explicit con-
high-stakes application domains. Furthermore,
firmation prior to executing irreversible or high-
such dilution of agency risks creating a scenario
consequence actions. Users should retain over-
where the human retains nominal authority over
sight and the right to withdraw consent at any
tasks and decisions but lacks moral connection
time, subject to agreement terms or exit penal-
to the result. It is therefore important to avoid
ties. Insuranceprovidersshouldadditionallysafe-
instantiating a moral crumple zone (Elish, 2019),
guard human participation in agentic markets,
in which human experts lack meaningful control
for any damages that are not preempted through
over outcomes, yet are introduced in delegation
these mechanisms (Tomei et al., 2025).
chains merely to absorb liability.
Finally,theecosystemneedsclearprotocolsfor
Intelligent Delegation frameworks maythere-
rapidly responding to security incidents. These
fore need to incorporate active measures against
protocols should include ways of revoking the
suchindi!erencebyintroducingacertainamount
credentials of confirmed malicious agents, freez-
of cognitive friction during oversight (Bader and
ing the associated smart contracts, broadcasting
Kaiser, 2019). The interface should reflect the
securityupdatestoallparticipants,andhandling
criticalhumanroleintheseprocessesandensure
these events recursively across delegation chains.
that all flagged decisions are evaluated carefully
For malicious actions facilitated by human users
and appropriately. As agentic verification may
andAIagentsalike,technicalsolutionsneedtobe
also be employed in scalable oversight, it is sim-
complemented by strong institutions and regula-
ilarly important to consider which decisions or
tions that would disincentivise fraudulent behav-
outcomes are to be evaluated by such agentic
ior and set clear rules to enable safe and scalable
systems vs directly by humans. Cognitive fric-
task delegation in agentic markets.
tion also needs to be balanced against the risk
of introducing alarm fatigue - becoming desen-
sitised to constant, often false, alarms (Michels
et al., 2025). If verification requests for delega-
22

IntelligentAIDelegation
tion sub-steps are sent to human overseers too 5.3. Reliability and E#ciency
frequently, overseers may eventually default to
Implementing the proposed verification mecha-
heuristic approval, without deeper engagement
nisms (ZKPs or multi-agent consensus games)
and appropriate checks. Therefore, friction must
may introduce latency, and an additional compu-
be context-aware: the system should allow seam-
tational cost, compared to unverified execution.
less execution for for tasks with low criticality
This constitutes a reliability premium, particu-
or low uncertainty, but dynamically increase cog-
larly relevant for highly critical execution tasks.
nitive load, by requiring justification or manual
Ontheotherhand,theremaybeusecaseswhere
intervention when the system encounters higher
this additional cost is unwarranted. One way
uncertaintyorisfacedwithunanticipatedscenar-
to address this in agentic markets would be to
ios.
support tiered service levels: low-cost delegation
for low-stakes routine tasks, and high-assurance
delegation for critical functions.
5.2. AccountabilityinLongDelegationChains
Ifhigh-assurancedelegationiscomputationally
In long delegation chains (𝑅 𝐿 𝑀 𝑁 expensive, there is a risk that safety becomes a
→ → → →
... 𝑆), the increased distance between the luxury good. This poses an ethical issue: users
→
originalintent(𝑅)andtheultimateexecution(𝑆) with fewer resources may be forced to rely on
may result in an accountability vacuum (Slota unverifiedoroptimisticexecutionpaths,exposing
etal.,2023). Presumingthat𝑅 isthehumanusers them to disproportionate risks of agent failure.
in this example, specifying the task or the intent This should be mitigated by ensuring a level of
that the corresponding personal AI assistant 𝐿 minimumviablereliability,asabaselinethatmust
acts upon, it may not be feasible (or reasonable) be guaranteed for all users.
to expect a human user to audit the 𝑇-th degree
In competitive marketplaces, agents may pri-
sub-delegatee in the execution graphs.
oritize speed and low cost. Without additional
To address this, the framework may need to regulatory constraints, agents may therefore be
implement liability firebreaks (Section 2), as pre- incentivized to avoid expensive safety checks to
defined contractual stop-gaps where an agent outcompeteotheragentsonpriceorlatency. This
must either: may introduce a level of systemic fragility. Gover-
nancelayers mustthereforeenforcesafetyfloors:
mandatoryverificationstepsforspecificclassesof
tasks (e.g., financial transactions or health data
1. Assume full, non-transitive liability for all
handling)thatcannotbebypassedforthesakeof
downstream actions, essentially “insuring”
e"ciency.
the user against sub-agent failure.
2. Haltexecutionandrequestanupdatedtrans-
fer of authority from the human principal. 5.4. Social Intelligence
As agents integrate into hybrid teams, they func-
tionnotonlyastoolsbutasteammates,andocca-
Furthermore, the system must maintain im-
sionallyasmanagers(AshtonandFranklin,2022).
mutable provenance, ensuring that even if an
This requires a form of social intelligence that re-
outcome is unintended, the chain of custody re-
spects the dignity of human labor. When an AI
garding who delegated what to whom remains
agent acts as a delegator and a human as a dele-
auditorially transparent.
gatee, the delegation framework needs to avoid
Ensuring full clarity of each role and the ac- scenarios where people feel micromanaged by
countabilitythatitcarrieshelpslimitthedi!usion algorithms,andwheretheircontributionsarenot
of responsibility, and prevents adverse outcomes valued or respected. This presumes that the dele-
where systemic failure would not be possible to gator (as well as collaborators) has the capability
attribute to any single node in the network. to form mental models of each human delegatee,
23

IntelligentAIDelegation
as well as models of how di!erent humans inter- as education and (co-)training, aimed at improv-
act in the social context of the team, and what ing AI literacy. Human participants in agentic
their relationships and roles signify within the task delegation chains need to be able to reliably
organization. To function as e!ective teammates, communicate with AI systems, evaluate their ca-
AI agents must also be calibrated to manage the pabilities, and identify failure modes.
authority gradient. An agent must be assertive
Technical measures must be reinforced by pol-
enough to challenge a recognized human error
icy frameworks that explicitly define delegation
(overcoming sycophancy) while remaining open
boundaries based on task sensitivity and domain
to accepting valid overrides, dynamically adjust-
context. These policies may either be developed
ing its standing based on the task criticality.
to be more broadly applicable within certain pro-
For AI agents that are embedded in human or- fessions (e.g. medicine or law), or applied at an
ganizations, it is important for them to maintain institutional level. As discussed previously, these
cohesion of the group and the well-being of its principles should also o!er clarity on the level of
members. The delegation framework must recog- certificationrequiredonbehalfofdelegatees,and
nize that a team is more than a simple sum of its be scoped appropriately. Human agency and em-
parts,thatitisafundamentallysocialentityheld powerment in this context lies precisely in how
together by relationships and shared values and these workflows are set up, so as not to grant
objectives. ThereisariskthatAIagentsmayfrag- AI agents limitless autonomy, but rather just the
ment these networks, and weaken inter-human right level of autonomy and agency required for
relationships, in case more delegation is being each specific task, coupled with the appropriate
mediated through AI nodes. This may be miti- safeguards and guarantees.
gated by occasionally delegating tasks to groups
rather than individuals, or via qualified human
5.6. Risk of De-skilling
intermediaries.
The immediate e"ciency gains achieved through
To preserve psychological safety and team co-
delegation may come at the cost of gradual skill
hesion,agentsmustbedesignedtorespecthuman
degradation, as human participants in hybrid
normsofappropriateness(Leiboetal.,2024),es-
loopsloseproficiencyduetoreducedengagement.
peciallyaroundprivacy,andalsoworkflowbound-
This may result in a loss of the ability to perform
aries such as knowing when to interrupt for feed-
certain tasks, or judge them accurately. Such an
back and when to remain silent. Furthermore,
outcome would be especially likely if there is a
they should be capable of bi-directional clarity:
certain systemic bias in which tasks get algorith-
not only explaining their own actions but proac-
mically delegated to humans vs AI agents.
tively seeking clarification on ambiguous human
directives. This can help ensure that the agent
This is an instance of the classic paradox of
acts as a force multiplier for the team’s collective
automation (Bainbridge, 1983). As AI agents ex-
agency, rather than a black-box disruptor that
pandtohandlethemajorityofroutineworkflows
erodes trust or obfuscates decision-making au-
that are characterized by low complexity and
thority.
low subjectivity, human operators are increas-
ingly removed from the loop, intervening only
to manage complex edge cases or critical system
5.5. User Training failures. However, without the situational aware-
ness gained from routine work, humans workers
To ensure safety, we must equip human partici-
would be ill-equipped to handle these reliably.
pantswiththeexpertisetofunctione!ectivelyas
Thisleadstoafragilesetupwherehumansretain
delegators, delegatees, or overseers within agen-
accountabilityforoutcomesbutlosethehands-on
tic systems. We know from the history of tech-
experience required to resolve critical failures.
nological development that this is not a given,
and it requires a thoughtful approach, both in To mitigate this risk, an intelligent delegation
terms of carefully crafted user interfaces as well frameworkshouldperhapsoccasionallyintroduce
24

IntelligentAIDelegation
minor ine"ciencies by intentionally delegating lished and recently introduced AI agent proto-
some tasks to humans that it wouldn’t have oth- cols. NotableexamplesoftheseincludeMCP(An-
erwise,withaspecificintentofmaintainingtheir thropic, 2024; Microsoft, 2025), A2A (Google,
skills. This would help us avoid the future in 2025b),AP2(ParikhandSurapaneni,2025),and
whichthehumanprincipalisabletodelegate,but UCP (Handa and Google Developers, 2026). As
not accurately judge the outcome. To enhance newagenticprotocolskeepbeingintroduced,the
adjudication, human experts can be required to discussionhereisnotmeanttobecomprehensive,
accompany their judgments with a detailed ra- rather illustrative, and focused on these popular
tionale or a pre-mortem of potential failure risks. protocols to showcase how they map onto our
This would help keep human participants in task proposed requirements, and serve as an exam-
delegation chains more cognitively engaged. ple for a more technical discussion on avenues
for future implementation. There may well be
Furthermore, uncheckeddelegationthreatens
other existing protocols out there that are better
the organizational apprenticeship pipeline. In
tailored to the core of the proposal, as the exam-
many domains, expertise is built through the
ple protocols discussed below have been selected
repetitive execution of more narrowly scoped
based on their popularity.
tasks. These tasks are precisely the ones that are
most likely to be o&oaded to AI agents, at least MCP. MCP has been introduced to standardize
in the short term. If learning opportunities are howAImodelsconnecttoexternaldataandtools
thereby fully automated, junior team members via a client-host-server architecture (Anthropic,
wouldbedeprivedofthenecessaryexperienceto 2024; Microsoft, 2025). By establishing a uni-
develop deep strategic judgement, impacting the form interface – using JSON-RPC messages over
oversight readiness of the future workforce. stdioorHTTPSSE–itallowstheAImodel(client)
to interact consistently with external resources
To counter the erosion of learning, intelligent
(server). This reduces the transaction cost of del-
delegation frameworks should be extended to
egation; a delegator does not need to know the
include some form of a developmental objective.
proprietary API schema of a sub-agent, only that
Ratherthanrelyingonmorepassivesolutionslike
the sub-agent exposes a compliant MCP server.
humans shadowing AI agents during task execu-
Routingallinteractionsthroughthisstandardized
tion,weshouldaimtodevelopcurriculum-aware
channel enables uniform logging of tool invoca-
task routing systems. Such systems should track
tions, inputs, and outputs, facilitating black-box
theskillprogressionofjuniorteammembersand
monitoring. MCP defines capabilities but lacks
strategically allocate tasks that sit at the bound-
the policy layer to govern usage permissions or
ary of their expanding skill set, within the zone
support deep delegation chains. It provides bi-
of proximal development. In such a system, AI
nary access – granting callers full tool utility –
agents may co-execute tasks and provide tem-
without native support for semantic attenuation,
plates and skeletons, progressively withdrawing
suchasrestrictingoperationstospecificread-only
this support as the junior team members demon-
scopes. Additionally, MCP is stateless regarding
stratethattheyhaveacquiredthedesiredlevelof
internal reasoning, exposing only results rather
proficiency. These educational frameworks may
than intent or traces. Finally, the protocol is ag-
be further enriched by incorporating detailed
nostic to liability and lacks native mechanisms
process-level monitoring streams of AI agent task
for reputation or trust.
execution(Section4.5),thatwouldo!ervaluable
developmental insights. A2A. The A2A protocol serves as the peer-to-
peer transport layer on the agentic web (Google,
2025b). It defines how agents can discover peers
6. Protocols viaagentcardsandmanagetasklifecyclesviatask
objects. The A2A agent card structure, a JSON-
Forintelligenttaskdelegationtobeimplemented
LD manifest listing an agent’s capabilities, pric-
in practice, it is important to consider how its
ing, and verifiers, may act as the foundational
requirements map onto some of the more estab-
25

IntelligentAIDelegation
data structure for the capability matching stage releases—which is standard in human contract-
that influences task decomposition. A delegator ing. Because our framework gates payment on
could scrape these cards to determine the opti- verifiable artifacts, bridging AP2 with task state
maltaskdecompositiongranularitydependingon currently necessitates brittle, custom logic or ex-
theavailablemarketservices. A2Asupportsasyn- ternal smart contracts. Furthermore, the absence
chronouseventstreamsviaWebHooksandgRPC. of a protocol-level clawback mechanism forces
Thisallowsadelegateetopushstatusupdateslike reliance on ine"cient, out-of-band arbitration.
TASK_BLOCKED, RESOURCE_WARNING to the
UCP. The Universal Commerce Protocol ad-
delegator in real-time. This feedback loop under-
dresses the specific challenges of delegation
pinstheadaptivecoordinationcycle,empowering
within transactional economies (Handa and
delegators to dynamically interrupt, re-allocate,
Google Developers, 2026). By standardizing the
andremediatetasks. A2Ahasbeeenprimarilyde-
dialogue between consumer-facing agents and
signed for coordination, rather than adversarial
backend services, UCP facilitates the Task As-
safety. A task is marked as completed would be
signment phase through dynamic capability dis-
accepted without additional verification. It lacks
covery. Its reliance on a shared “commerce lan-
the cryptographic slots to enforce verifiable task
guage” allows delegators to interact with diverse
completion,asthereisnostandardizedheaderfor
providers without bespoke integrations, solving
attaching a ZK-proof, a TEE attestation, or a digi-
the interoperability bottleneck that often frag-
tal signature chain. It also assumes a predefined
ments agentic markets. Crucially, UCP aligns
service interface. There is no native support for
well with the requirements for Permission Han-
structured pre-commitment negotiation of scope,
dling and Security by treating payment as a first-
cost, and liability. Relying on unstructured natu-
class, verifiable subsystem. The protocol dis-
rallanguageforthisiterativerefinementisbrittle
sociates payment instruments from processors
and hinders robust automation.
and enforces cryptographic proofs for authoriza-
AP2. The AP2 protocol provides a standard tions, directly supporting the framework’s need
for mandates, cryptographically signed intents for non-repudiable consent and verifiable liabil-
that authorize an agent to spend funds or incur ity. Furthermore, by standardizing the negoti-
costsonbehalfofaprincipal(ParikhandSurapa- ation flow—covering discovery, selection, and
neni,2025). ItallowsAIagentstogenerate,sign, transaction—UCPprovidesthestructuralsca!old-
and settle financial transactions autonomously. ing necessary for Scalable Market Coordination
As such, it may prove valuable for implement- that purely transport-oriented protocols like A2A
ing liability firebreaks. By issuing a mandate, lack. However, UCP’s architecture is explicitly
a delegator creates a ceiling on the potential fi- optimized for commercial intent; its primitives
nancial loss due to failed task completion that (product discovery, checkout, fulfillment) may re-
could be incurred by having the delegatee pro- quire significant extension to support the delega-
ceed with the provided budget. In a decentral- tion of abstract, non-transactional computational
ized market, malicious agents could spam the tasks.
networkwithlow-qualitybids. Thiscouldbemit-
igated in AP2 via stake-on-bid mechanisms. A
6.1. Towards Delegation-centered Protocols
delegatee may be required to cryptographically
lock a small amount of funds as a bond along-
To e!ectively bridge the gaps in established
side the bid. This would provide a degree of
widespread protocols, they could be extended by
friction that would help protect against Sybil at-
fieldsthataimtocapturetherequirementsofthe
tacks. AP2 also provides a non-repudiable audit
proposed intelligent task delegation framework
trail, helping pinpoint the provenance of intent.
natively. Rather than providing a comprehensive
WhileAP2providesrobustauthorizationbuilding
protocol extension, here we provide several ex-
blocks, it lacks mechanisms to verify task exe-
amples of how specific points introduced in the
cution quality. It also omits conditional settle-
earlier discussion could be integrated in some of
ment logic—such as escrow or milestone-based
the existing protocols.
26

IntelligentAIDelegation
For example, the A2A Task object may be ex- constraints, the stream could be configurable
tended to include fields that would incorporate in a way that supports di!erent levels of nego-
verification standards, making it possible to en- tiated granularity: L0_IS_OPERATIONAL,
force the previously discussed contract-first de- L1_HIGH_LEVEL_PLAN_UPDATES,
composition at the protocol level. This is an im- L2_COT_TRACE, L3_FULL_STATE. Config-
portant requirement for high-stakes delegation. urable granularity can also modulate cognitive
A pre-execution handshake would enable the del- friction, as human overseers would be able to
egator to define the evidence standard required subscribe to a specific stream.
for the task to be considered valid.
Intelligent Delegation requires a market mech-
anism to trade o! cost, speed, and privacy. This
"verification_policy": {
could be implemented via a formal Request for
"mode": "strict",
Quote (RFQ) protocol extension. Prior to task
"artifacts": [
assignment, the delegator would broadcasts a
{
Task_RFQ. Agents interested in acting as delega-
"type":
tees may then respond with signed Bid_Objects.
"unit_test_log",
"validator":
"mcp://test-runner-agent", "bid_object": {
"signature_required": true "agent_id":
}, "did:web:fast-coder.ai",
{ "estimated_cost":
"type": "5.00 USDC",
"zk_snark_trace", "estimated_duration":
"circuit_hash": "300s",
"0xabc123...", "privacy_guarantee":
"proof_protocol": "tee_enclave_sgx",
"groth16" "reputation_bond":
} "0.50 USDC",
], "expiry":
"escrow_trigger": true "2026-10-01T12:00:00Z"
} }
}
Passing raw API keys or open MCP sessions to
This forces the delegatee to simulate the ver-
sub-agents would violate the principle of least
ification step before accepting the task. If the
privilege. To address this, it may be possible to
delegatee lacks the capability to generate a ZK-
introduce Delegation Capability Tokens (DCT),
proof,itmustdeclinethebidduringthematching
based on Macaroons (Birgisson et al., 2014) or
phase, preventing future downstream failures.
Biscuits (Couprie et al., 2026), as attenuated au-
Detailed, process-level monitoring has been thorization tokens (Sanabria and Vecino, 2025).
discussedasoneofthekeyconsiderationstohelp A delegator would then mint a DCT that wraps
safeguardtaskdelegationinhigh-criticalitytasks. thetargetresourcecredentialswithcryptographic
Given that monitoring protocols aren’t natively caveats. Theattenuationcouldbedefinesas"This
supported in many of the existing protocols, token can access the designated Google Drive
extensions that introduce monitoring capabilities MCP server, BUT ONLY for folder Project_X AND
could be considered. For example, one could ONLY for READ operations.". This token would
considerextendingaprotocollikeMCPtoinclude getinvalidatedincasetherestrictionsarenotfol-
an additional monitoring stream. Such a stream lowed, if a delegatee attempts to go beyond the
wouldlogtheagent’sinternalcontrolloopevents requestedscope(inthisexample,however,access
via Server-Sent Events. To address the privacy permissions should also be directly managed). A
27

IntelligentAIDelegation
more interesting consequence of such an exten- support this transformation. To safely unlock the
sion would be that it allows for easy restriction potential of the agentic web, we must adopt a
chaining,whichbecomesrelevantinlongdelega- dynamic and adaptive framework for intelligent
tion chains. Each participant in the chain could delegation, that prioritizes verifiable robustness
add subsequent restrictions that correspond to andclearaccountabilityalongsidecomputational
the requirements of the sub-delegation, further e"ciency.
limiting the scope and carving out the specific
WhenanAIagentisfacedwithacomplexobjec-
role for sub-delegatees.
tive whose completion requires capabilities and
Adaptivecoordination(Section4.4)wouldben- resources beyond its own means, this agent must
efit from the ability to easily swap delegatee assume the role of a delegator within the intel-
agents mid-task if the performance degrades be- ligent task delegation framework. This delega-
lowacertainthreshold,orincaseofpreemptions tor would subsequently decompose this complex
or other possible environmental triggers. Having task into manageable subcomponents that can
astandardschemaforcheckpointartifactswould be mapped onto the capabilities available on the
enable for the task to be resumed or restarted agentic market, at the level of granularity that
with minimal overhead. This would enable the lends itself to high verifiability. The task alloca-
delegatees and the delegators to serialize partial tion would be decided based on the incoming
work more easily. Agents would then be able to bids, and a number of key considerations includ-
periodically commit a state_snapshot to a shared ing trust and reputation, monitoring of dynamic
storage referenced in the A2A Task Object. This operational states, cost, e"ciency, and others.
wouldpreventtotalworkloss,whichwastesprevi- Tasks with high criticality and low reversibility
ouslycommittedresources. Forthistobesensible, may require further structured permissions and
it would need to be further coupled with explicit tieredapprovals,withaclearstructureofaccount-
clauseswithinthesmartcontractthatenablepar- ability, and under appropriate human oversight
tial compensation, and verification of the task as defined by the applicable institutional frame-
completion percentage. As such, it may not be works.
applicable to all circumstances.
At web-scale, safety and accountability can-
These are merely illustrative examples for the not be an afterthought. They need to be baked
kinds of functionalities that would be possible to into the operational principles of virtual agentic
include in agentic protocols to unlock di!erent economies, and act as central organizing princi-
aspects of intelligent task delegation. As such, ples of the agentic web. By incorporating safety
they are neither comprehensive, nor meant as a at the level of delegation protocols, we would
definitive proposal. The type of extension that is be aiming to avoid cumulative errors and cas-
required would also depend on the underlying cading failures, and attain the ability to react
protocol being extended. We hope that these ex- to malicious or misaligned agentic or human be-
amples may provide the developers with some haviorrapidly,limitingtheadverseconsequences.
initialideasforwhattoexploreinthisspacemov- What we propose is ultimately a paradigm shift
ing forward. from largely unsupervised automation to veri-
fiable, intelligent delegation, that allows us to
safely scale towards future autonomous agentic
7. Conclusion systems, while keeping them closely tethered to
human intent and societal norms.
Significant components of the future global econ-
omywilllikelybemediatedbymillionsofspecial-
ized AI agents, embedded within firms, supply References
chains, and public services, handling everything
from routine transactions to complex resource A. Acar, H. Aksu, A. S. Uluagac, and M. Conti. A
allocation. However, the current paradigm of ad- survey on homomorphic encryption schemes:
hoc, heuristic-based delegation is insu"cient to Theory and implementation. ACM Computing
28

IntelligentAIDelegation
Surveys (Csur), 51(4):1–35, 2018. Anthropic. Introducing the model context pro-
tocol, 2024. URL https://www.anthropic.
D. B. Acharya, K. Kuppan, and B. Divya. Agentic com/news/model-context-protocol.
ai: Autonomousintelligenceforcomplexgoals–
a comprehensive survey. IEEe Access, 2025. S.Armstrong,M.Franklin,C.Stevens,andR.Gor-
man. Defense against the dark prompts: Miti-
S. Afroogh, A. Akbari, E. Malone, M. Kargar, and gating best-of-n jailbreaking with prompt eval-
H.Alambeigi. Trustinai: progress,challenges, uation. arXivpreprintarXiv:2502.00580,2025.
and future directions. Humanities and Social
H. Ashton. Definitions of intent suitable for algo-
Sciences Communications, 11(1):1–30, 2024.
rithms. Artificial Intelligence and Law, 31(3):
A. Akbar and O. Conlan. Towards integrating 515–546, 2023.
human-in-the-loop control in proactive intelli-
H. Ashton and M. Franklin. The corrupting in-
gent personalised agents. In Adjunct Proceed-
fluence of ai as a boss or counterparty. SSRN,
ingsofthe32ndACMConferenceonUserModel-
2022.
ing,AdaptationandPersonalization,pages394–
398, 2024.
O.Avellaneda,A.Bachmann,A.Barbir,J.Brenan,
P. Dingle, K. H. Du!y, E. Maler, D. Reed, and
S. A. Akheel. Guardrails for large language mod-
M. Sporny. Decentralized identity: Where did
els: A review of techniques and challenges. J
it come from and where is it going? IEEE
Artif Intell Mach Learn & Data Sci, 3(1):2504–
Communications Standards Magazine, 3(4):10–
2512, 2025.
13, 2019.
S. Aknine, S. Pinson, and M. F. Shakun. A multi-
V. Bader and S. Kaiser. Algorithmic decision-
agent coalition formation method based on
making? the user interface and its role for
preference models. Group Decision and Negoti-
human involvement in decisions supported by
ation, 13(6):513–538, 2004.
artificialintelligence.Organization,26(5):655–
672, 2019.
S. V. Albrecht, F. Christianos, and L. Schäfer.
Multi-agentreinforcementlearning: Foundations
L. Bainbridge. Ironies of automation. Au-
and modern approaches. MIT Press, 2024.
tomatica, 19(6):775–779, 1983. ISSN
0005-1098. doi: https://doi.org/10.1016/
C.AliferisandG.Simon. Overfitting,underfitting
0005-1098(83)90046-8. URL https:
and general model overconfidence and under-
//www.sciencedirect.com/science/
performance pitfalls and best practices in ma-
article/pii/0005109883900468.
chinelearningandai. Artificialintelligenceand
machine learning in health care and medical sci- A. G. Barto and S. Mahadevan. Recent advances
ences: Bestpracticesandpitfalls,pages477–524, inhierarchicalreinforcementlearning. Discrete
2024.
event dynamic systems, 13(4):341–379, 2003.
R. A. Alkov, M. S. Borowsky, D. W. Williamson, C. Bergho!, B. Biggio, E. Brummel, V. Danos,
andD.W.Yacavone. Thee!ectoftrans-cockpit T. Doms, H. Ehrich, T. Gantevoort, B. Ham-
authority gradient on navy/marine helicopter mer, J. Iden, S. Jacob, et al. Towards auditable
mishaps. Aviation, space, and environmental ai systems. Whitepaper. Bonn Berlin: Bunde-
medicine, 63(8):659–661, 1992. samt für Sicherheit in der Informationstechnik,
Fraunhofer-Institut für Nachrichtentechnik und
D. Amodei, C. Olah, J. Steinhardt, P. Christiano,
Verband der TÜV eV, 2021.
J. Schulman, and D. Mané. Concrete problems
in AI safety. In Proceedings of the 30th AAAI A. Beverungen. Remote control: Algorithmic
ConferenceonArtificialIntelligenceWorkshopon management of circulation at amazon. In
AI Safety, 2016. M. Burkhardt, M. Shnayien, and K. Grashöfer,
29

IntelligentAIDelegation
editors, Explorations in Digital Cultures, pages E. Portelance, C. Potts, A. Raghunathan, R. Re-
5–18. meson press, Lüneburg, 2021. ich, H. Ren, F. Rong, Y. Roohani, C. Ruiz,
J. Ryan, C. Ré, D. Sadigh, S. Sagawa, K. San-
A. Birgisson, J. G. Politz, U. Erlingsson, A. Taly,
thanam, A. Shih, K. Srinivasan, A. Tamkin,
M.Vrable,andM.Lentczner. Macaroons: Cook-
R. Taori, A. W. Thomas, F. Tramèr, R. E. Wang,
ies with contextual caveats for decentralized
W.Wang,B.Wu,J.Wu,Y.Wu,S.M.Xie,M.Ya-
authorization in the cloud. In NDSS, 2014.
sunaga,J.You,M.Zaharia,M.Zhang,T.Zhang,
X. Zhang, Y. Zhang, L. Zheng, K. Zhou, and
N. Bitansky, A. Chiesa, Y. Ishai, O. Paneth, and
P.Liang. Ontheopportunitiesandrisksoffoun-
R. Ostrovsky. Succinct non-interactive argu-
dation models, 2022. URL https://arxiv.
ments via linear interactive proofs. In The-
org/abs/2108.07258.
oryofCryptographyConference,pages315–333.
Springer, 2013.
M. M. Botvinick. Hierarchical reinforcement
learning and decision making. Current opinion
D. G. Blanco. Practical OpenTelemetry. Springer,
in neurobiology, 22(6):956–962, 2012.
2023.
T.F.Blauth,O.J.Gstrein,andA.Zwitter.Artificial S. R. Bowman, J. Hyun, E. Perez, E. Chen, C. Pet-
intelligence crime: An overview of malicious tit, S. Heiner, K. Luko%iu¯t˙e, A. Askell, A. Jones,
use and abuse of ai. Ieee Access, 10:77110– A. Chen, A. Goldie, A. Mirhoseini, C. McKin-
77122, 2022. non, C. Olah, D. Amodei, D. Amodei, D. Drain,
D. Li, E. Tran-Johnson, J. Kernion, J. Kerr,
N. Boehmer, M. Bullinger, and A. M. Kerkmann. J. Mueller, J. Ladish, J. Landau, K. Ndousse,
Causes of stability in dynamic coalition forma- L. Lovitt, N. Elhage, N. Schiefer, N. Joseph,
tion. ACM Transactions on Economics and Com- N. Mercado, N. DasSarma, R. Larson, S. Mc-
putation, 13(2):1–45, 2025. Candlish,S.Kundu,S.Johnston,S.Kravec,S.E.
Showk, S. Fort, T. Telleen-Lawton, T. Brown,
J.BohteandK.J.Meier. Structureandtheperfor-
T. Henighan, T. Hume, Y. Bai, Z. Hatfield-
mance of public organizations: Task di"culty
Dodds, B. Mann, and J. Kaplan. Measuring
andspanofcontrol. Publicorganizationreview,
progress on scalable oversight for large lan-
1(3):341–354, 2001.
guage models, 2022. URL https://arxiv.
R. Bommasani, D. A. Hudson, E. Adeli, R. Alt-
org/abs/2211.03540.
man, S. Arora, S. von Arx, M. S. Bernstein,
B. G. Buchanan and R. G. Smith. Fundamentals
J. Bohg, A. Bosselut, E. Brunskill, E. Brynjolf-
of expert systems. Annual review of computer
sson, S. Buch, D. Card, R. Castellon, N. Chat-
science, 3(1):23–58, 1988.
terji,A.Chen,K.Creel,J.Q.Davis,D.Demszky,
C. Donahue, M. Doumbouya, E. Durmus, S. Er-
W. Cai, J. Jiang, F. Wang, J. Tang, S. Kim, and
mon, J. Etchemendy, K. Ethayarajh, L. Fei-Fei,
J. Huang. A survey on mixture of experts in
C. Finn, T. Gale, L. Gillespie, K. Goel, N. Good-
large language models. IEEE Transactions on
man, S. Grossman, N. Guha, T. Hashimoto,
Knowledge and Data Engineering, 2025.
P. Henderson, J. Hewitt, D. E. Ho, J. Hong,
K. Hsu, J. Huang, T. Icard, S. Jain, D. Ju- C. Castelfranchi and R. Falcone. Towards a
rafsky, P. Kalluri, S. Karamcheti, G. Keeling, theory of delegation for agent-based systems.
F. Khani, O. Khattab, P. W. Koh, M. Krass, RoboticsandAutonomoussystems,24(3-4):141–
R. Krishna, R. Kuditipudi, A. Kumar, F. Lad- 157, 1998.
hak, M. Lee, T. Lee, J. Leskovec, I. Levent, X. L.
Li,X.Li,T.Ma,A.Malik,C.D.Manning,S.Mir- A.Chan,R.Salganik,A.Markelius,C.Pang,N.Ra-
chandani, E. Mitchell, Z. Munyikwa, S. Nair, jkumar, D. Krasheninnikov, L. Langosco, Z. He,
A. Narayan, D. Narayanan, B. Newman, A. Nie, Y. Duan, M. Carroll, et al. Harms from increas-
J.C.Niebles,H.Nilforoshan,J.Nyarko,G.Ogut, ingly agentic algorithmic systems. In Proceed-
L. Orr, I. Papadimitriou, J. S. Park, C. Piech, ings of the 2023 ACM Conference on Fairness,
30

IntelligentAIDelegation
Accountability, and Transparency, pages 651– M.DastaniandV.Yazdanpanah. Responsibilityof
666, 2023. aisystems. Ai&Society,38(2):843–852,2023.
W.Chen,Z.You,R.Li,Y.Guan,C.Qian,C.Zhao, T. Davidson and R. Hadshar. The indus-
C. Yang, R. Xie, Z. Liu, and M. Sun. Internet trial explosion. 2025. URL https:
of agents: Weaving a web of heterogeneous //www.forethought.org/research/
agentsforcollaborativeintelligence,2024.URL the-industrial-explosion. Accessed:
https://arxiv.org/abs/2407.07061. 2025-11-28.
Z.Chen,Y.Deng,Y.Wu,Q.Gu,andY.Li.Towards A. B. De Neira, B. Kantarci, and M. Nogueira.
understanding the mixture-of-experts layer in Distributed denial of service attack predic-
deep learning. Advances in neural information tion: Challenges,openissuesandopportunities.
processing systems, 35:23049–23062, 2022. Computer Networks, 222:109553, 2023.
M. Cheng, C. Yin, J. Zhang, S. Nazarian, J. Desh- K. Deb, K. Sindhya, and J. Hakanen. Multi-
mukh, and P. Bogdan. A general trust frame- objective optimization. In Decision sciences,
work for multi-agent systems. In Proceedings pages 161–200. CRC Press, 2016.
of the 20th International Conference on Au-
S. Dhuliawala, V. Zouhar, M. El-Assady, and
tonomousAgentsandMultiAgentSystems,pages
M. Sachan. A diachronic perspective on user
332–340, 2021.
trust in ai under uncertainty, 2023. URL
A. E. Cinà, K. Grosse, A. Demontis, S. Vascon,
https://arxiv.org/abs/2310.13544.
W. Zellinger, B. A. Moser, A. Oprea, B. Biggio,
V. Dignum. Responsibility and artificial intelli-
M. Pelillo, and F. Roli. Wild patterns reloaded:
gence.TheoxfordhandbookofethicsofAI,4698:
A survey of machine learning security against
215, 2020.
training data poisoning. ACM Computing Sur-
veys, 55(13s):1–39, 2023.
L.Donaldson. Thecontingencytheoryoforganiza-
tions. Sage, 2001.
S. Cohen, R. Bitton, and B. Nassi. Here comes
theaiworm: Unleashingzero-clickwormsthat Y. Dong, R. Mu, G. Jin, Y. Qi, J. Hu, X. Zhao,
target genai-powered applications, 2025. URL J. Meng, W. Ruan, and X. Huang. Building
https://arxiv.org/abs/2403.02817.
guardrails for large language models. arXiv
preprint arXiv:2402.01822, 2024.
K. S. Cosby and P. Croskerry. Profiles in patient
safety: authority gradients in medical error. I. Drori and D. Te’eni. Human-in-the-loop ai re-
Academic emergency medicine, 11(12):1341– viewing: feasibility, opportunities, and risks.
1345, 2004. Journal of the Association for Information Sys-
tems, 25(1):98–109, 2024.
G. Couprie, C. Delafargue, and C. e. a. Cor-
bière. Eclipse biscuit, 2026. URL https: Y.Du,J.Z.Leibo,U.Islam,R.Willis,andP.Sune-
//www.biscuitsec.org/.
hag. A review of cooperation in multi-agent
learning. arXiv preprint arXiv:2312.05162,
I. R. Cuypers, J.-F. Hennart, B. S. Silverman,
2023.
and G. Ertug. Transaction cost theory: Past
progress, current challenges, and suggestions M. T. Dzindolet, S. A. Peterson, R. A. Pomranky,
forthefuture. AcademyofManagementAnnals, L. G. Pierce, and H. P. Beck. The role of
15(1):111–150, 2021. trustinautomationreliance. Internationaljour-
nalofhuman-computerstudies,58(6):697–718,
J. Cvitani#, D. Possamaï, and N. Touzi. Dy-
2003.
namic programming approach to principal–
agent problems. Finance and Stochastics, 22 A.Ehtesham,A.Singh,G.K.Gupta,andS.Kumar.
(1):1–37, 2018. A survey of agent interoperability protocols:
31

IntelligentAIDelegation
Modelcontextprotocol(mcp),agentcommuni- M.Franklin,H.Ashton,E.Awad,andD.Lagnado.
cation protocol (acp), agent-to-agent protocol Causal framework of artificial autonomous
(a2a),andagentnetworkprotocol(anp). arXiv agent responsibility. In Proceedings of the 2022
preprint arXiv:2505.02279, 2025. AAAI/ACMConferenceonAI,Ethics,andSociety,
pages 276–284, 2022.
M. C. Elish. Moral crumple zones: Cautionary
A.Fuchs,A.Passarella,andM.Conti. Optimizing
tales in human-robot interaction (pre-print).
delegation between human and ai collabora-
Engaging Science, Technology, and Society (pre-
tive agents. In Joint European Conference on
print), 2019.
Machine Learning and Knowledge Discovery in
J.Ensminger.Reputations,trust,andtheprincipal Databases, pages 245–260. Springer, 2023.
agent problem. Trust in society, 2:185–201,
A.Fuchs,A.Passarella,andM.Conti. Optimizing
2001.
delegation in collaborative human-ai hybrid
teams. ACM Transactions on Autonomous and
R. Falcone and C. Castelfranchi. The human in
Adaptive Systems, 19(4):1–33, 2024.
theloopofadelegatedagent: Thetheoryofad-
justable social autonomy. IEEE Transactions on A. Fügener, J. Grahl, A. Gupta, and W. Ketter.
Systems, Man, and Cybernetics-Part A: Systems Cognitive challenges in human-ai collabora-
and Humans, 31(5):406–418, 2002. tion: Investigatingthepathtowardsproductive
delegation. Forthcoming, Information Systems
M. Fatehkia, E. Altinisik, M. Osman, and H. T. Research, 2019.
Sencar. Sgm: A framework for building
A. Fügener, J. Grahl, A. Gupta, and W. Ketter.
specification-guided moderation filters. arXiv
Cognitive challenges in human–artificial intel-
preprint arXiv:2505.19766, 2025.
ligence collaboration: Investigating the path
I.Fedorov,K.Plawiak,L.Wu,T.Elgamal,N.Suda, toward productive delegation. Information Sys-
E. Smith, H. Zhan, J. Chi, Y. Hulovatyy, K. Pa- tems Research, 33(2):678–696, 2022.
tel, Z. Liu, C. Zhao, Y. Shi, T. Blankevoort,
I.Gabriel,A.Manzini,G.Keeling,L.A.Hendricks,
M.Pasupuleti,B.Soran,Z.D.Coudert,R.Alao,
V.Rieser,H.Iqbal,N.Toma%ev,I.Ktena,Z.Ken-
R. Krishnamoorthi, and V. Chandra. Llama
ton,M.Rodriguez,etal.Theethicsofadvanced
guard 3-1b-int4: Compact and e"cient safe-
ai assistants. arXiv preprint arXiv:2404.16244,
guard for human-ai conversations, 2024. URL
2024.
https://arxiv.org/abs/2411.17713.
I. Gabriel, G. Keeling, A. Manzini, and J. Evans.
H. Fereidouni, O. Fadeitcheva, and M. Zalai. Iot Who’s to blame when ai agents mess up? we
and man-in-the-middle attacks. Security and urgently need a new system of ethics, 2025.
Privacy, 8(2):e70016, 2025.
B. Gebru, L. Zeleke, D. Blankson, M. Nabil,
S. Nateghi, A. Homaifar, and E. Tunstel. A
D. P. Finkelman. Crossing the" zone of indi!er-
review on human–machine trust evaluation:
ence". Marketing Management, 2(3):22, 1993.
Human-centric and machine-centric perspec-
J. Foerster, G. Farquhar, T. Afouras, N. Nardelli, tives. IEEE Transactions on Human-Machine
and S. Whiteson. Counterfactual multi-agent Systems, 52(5):952–962, 2022.
policy gradients. In Proceedings of the AAAI
J.Geng,F.Cai,Y.Wang,H.Koeppl,P.Nakov,and
conference on artificial intelligence, volume 32,
I. Gurevych. A survey of confidence estimation
2018.
andcalibrationinlargelanguagemodels. arXiv
preprint arXiv:2311.08298, 2023.
M.Franklin.Theinfluenceofexplainableartificial
intelligence: Nudging behaviour or boosting O. Goldreich. Secure multi-party computation.
capability? arXiv preprint arXiv:2210.02407, Manuscript. Preliminary version, 78(110):1–
2022. 108, 1998.
32

IntelligentAIDelegation
C.Goods,A.Veen,andT.Barratt. “isyourgigany S. J. Grossman and O. D. Hart. An analysis of
good?” analysing job quality in the australian the principal-agent problem. In Foundations of
platform-based food-delivery sector. Journal of insuranceeconomics: Readingsineconomicsand
IndustrialRelations,61(4):502–527,2019. doi: finance, pages 302–340. Springer, 1992.
10.1177/0022185618817069.
T. Guggenberger, L. Lämmermann, N. Urbach,
Google. Powering ai commerce with the new A. M. Walter, and P. Hofmann. Task delegation
agent payments protocol (ap2), 2025a. from ai to humans: a principal-agent perspec-
tive. In Proceedings of the 44th International
Google. Powering ai commerce with the new Conference on Information Systems, 2023.
agent payments protocol (ap2), 2025b.
URL https://cloud.google.com/ A.Gunjal,A.Wang,E.Lau,V.Nath,Y.He,B.Liu,
blog/products/ai-machine-learning/ andS.Hendryx. Rubricsasrewards: Reinforce-
announcing-agents-to-payments-ap2-protomceonlt.learningbeyondverifiabledomains. arXiv
preprint arXiv:2507.17746, 2025.
Z. Gou, Z. Shao, Y. Gong, Y. Shen, Y. Yang,
D. Guo, Q. Zhu, D. Yang, Z. Xie, K. Dong,
N. Duan, and W. Chen. Critic: Large language
W. Zhang, G. Chen, X. Bi, Y. Wu, Y. Li, et al.
models can self-correct with tool-interactive
Deepseek-coder: When the large language
critiquing. arXiv preprint arXiv:2305.11738,
model meets programming–the rise of code
2023.
intelligence. arXiv preprint arXiv:2401.14196,
B. Green. The flaws of policies requiring human 2024a.
oversight of government algorithms. Computer
T. Guo, X. Chen, Y. Wang, R. Chang, S. Pei, N. V.
Law & Security Review, 45:105681, 2022.
Chawla, O. Wiest, and X. Zhang. Large lan-
guage model based multi-agents: A survey
R. Greenblatt, C. Denison, B. Wright, F. Roger,
M. MacDiarmid, S. Marks, J. Treutlein, T. Be- of progress and challenges. arXiv preprint
lonax, J. Chen, D. Duvenaud, A. Khan,
arXiv:2402.01680, 2024b.
J. Michael, S. Mindermann, E. Perez, L. Petrini,
J.Haas. Moralgridworlds: atheoreticalproposal
J. Uesato, J. Kaplan, B. Shlegeris, S. R. Bow-
for modeling artificial moral cognition. Minds
man, and E. Hubinger. Alignment faking
and Machines, 30(2):219–246, 2020.
in large language models. arXiv preprint
arXiv:2412.14093, 2024.
G. K. Hadfield and A. Koh. An economy of ai
agents. arXivpreprintarXiv:2509.01063,2025.
K. Greshake, S. Abdelnabi, S. Mishra, C. Endres,
T.Holz,andM.Fritz.Notwhatyou’vesignedup L. Hammond, A. Chan, J. Clifton, J. Hoelscher-
for: Compromising real-world llm-integrated Obermaier, A. Khan, E. McLean, C. Smith,
applications with indirect prompt injection. In W. Barfuss, J. Foerster, T. Gaven’iak, et al.
Proceedings of the 16th ACM workshop on ar- Multi-agent risks from advanced ai. arXiv
tificial intelligence and security, pages 79–90, preprint arXiv:2502.14143, 2025.
2023.
A. Handa and Google Developers. Under the
N. Gri"ths. Task delegation using experience- hood: Universal commerce protocol (UCP).
based multi-dimensional trust. In Proceedings https://developers.googleblog.com/
ofthefourthinternationaljointconferenceonAu- under-the-hood-universal-commerce-protocol-ucp/,
tonomous agents and multiagent systems, pages 2026. Accessed: 2026-01-20.
489–496, 2005.
S. Hao, Y. Gu, H. Ma, J. J. Hong, Z. Wang, D. Z.
S. Gronauer and K. Diepold. Multi-agent deep Wang, and Z. Hu. Reasoning with language
reinforcement learning: a survey. Artificial In- model is planning with world model. arXiv
telligence Review, 55(2):895–943, 2022. preprint arXiv:2305.14992, 2023.
33

IntelligentAIDelegation
N. Hardy. The confused deputy: (or why capabil- D. Duvenaud, D. Ganguli, F. Barez, J. Clark,
ities might have been invented). ACM SIGOPS K. Ndousse, K. Sachan, M. Sellitto, M. Sharma,
Operating Systems Review, 22(4):36–38, 1988. N. DasSarma, R. Grosse, S. Kravec, Z. Wit-
ten, M. Favaro, J. Brauner, H. Karnofsky,
A.I.Hauptman,B.G.Schelble,N.J.McNeese,and
P. Christiano, S. R. Bowman, L. Graham,
K. C. Madathil. Adapt and overcome: Percep-
J. Kaplan, S. Mindermann, R. Greenblatt,
tionsofadaptiveautonomousagentsforhuman-
N. Schiefer, B. Shlegeris, and E. Perez. Sleeper
aiteaming.ComputersinHumanBehavior,138:
agents: Training deceptive llms that per-
107451, 2023.
sist through safety training. arXiv preprint
arXiv:2401.05566, 2024.
G. He, P. Cui, J. Chen, W. Hu, and J. Zhu. In-
vestigating uncertainty calibration of aligned
K. Isomura. Management theory by Chester
languagemodelsunderthemultiple-choiceset-
Barnard: an introduction. Springer, 2021.
ting, 2023. URL https://arxiv.org/abs/
2310.11732.
R.A.Jacobs,M.I.Jordan,S.J.Nowlan,andG.E.
Hinton. Adaptive mixtures of local experts.
X. O. He. Mixture of a million experts. arXiv
Neural computation, 3(1):79–87, 1991.
preprint arXiv:2407.04153, 2024.
P.Hemmer,M.Westphal,M.Schemmer,S.Vetter, A. Q. Jiang, A. Sablayrolles, A. Roux, A. Mensch,
M. Vössing, and G. Satzger. Human-ai collab- B. Savary, C. Bamford, D. S. Chaplot, D. d. l.
oration: the e!ect of ai delegation on human Casas, E. B. Hanna, F. Bressand, et al. Mixtral
task performance and task satisfaction. In Pro- of experts. arXiv preprint arXiv:2401.04088,
ceedings of the 28th International Conference 2024.
on Intelligent User Interfaces, pages 453–463,
2023. C. Jiang, X. Pan, G. Hong, C. Bao, Y. Chen, and
M.Yang. Feedback-guidedextractionofknowl-
S. M. Herzog and M. Franklin. Boosting human edge base from retrieval-augmented llm ap-
competences with interpretable and explain- plications, 2025. URL https://arxiv.org/
able artificial intelligence. Decision, 11(4):493, abs/2411.14110.
2024.
Z. Jiang, J. Araki, H. Ding, and G. Neubig. How
S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng,
canweknowwhenlanguagemodelsknow? on
J.Wang,C.Zhang,Z.Wang,S.K.S.Yau,Z.Lin,
thecalibrationoflanguagemodelsforquestion
et al. Metagpt: Meta programming for a multi-
answering. Transactions of the Association for
agent collaborative framework. In The Twelfth
Computational Linguistics, 9:962–977, 2021.
International Conference on Learning Represen-
tations, 2023.
S. Kapoor, N. Gruver, M. Roberts, A. Pal, S. Doo-
ley, M. Goldblum, and A. Wilson. Calibration-
J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W.
tuning: Teaching large language models to
Yu, X. Song, and D. Zhou. Large language
know what they don’t know. In Proceedings
modelscannotself-correctreasoningyet. arXiv
of the 1st Workshop on Uncertainty-Aware NLP
preprint arXiv:2310.01798, 2023.
(UncertaiNLP 2024), pages 1–14, 2024.
K.HuangandC.Hughes. Deployingagenticaiin
enterpriseenvironments. InSecuringAIAgents: A. Kasirzadeh and I. Gabriel. Characteriz-
Foundations, Frameworks, and Real-World De- ing ai agents for alignment and governance,
ployment, pages 289–319. Springer, 2025.
2025.URLhttps://arxiv.org/abs/2504.
21848.
E. Hubinger, C. Denison, J. Mu, M. Lam-
bert, M. Tong, M. MacDiarmid, T. Lan- M. Keren and D. Levhari. The optimum span
ham, D. M. Ziegler, T. Maxwell, N. Cheng, of control in a pure hierarchy. Management
A.Jermyn,A.Askell,A.Radhakrishnan,C.Anil, science, 25(11):1162–1172, 1979.
34

IntelligentAIDelegation
O. Khattab, A. Singhvi, P. Maheshwari, Z. Zhang, ACMConferenceonFairness,Accountability,and
K. Santhanam, S. Vardhamanan, S. Haq, Transparency, pages 2274–2289, 2025.
A. Sharma, T. T. Joshi, H. Moazam, H. Miller,
M. K. Lee, D. Kusbit, E. Metsky, and L. Dabbish.
M. Zaharia, and C. Potts. Dspy: Compil-
Workingwithmachines: Theimpactofalgorith-
ing declarative language model calls into self-
improving pipelines, 2023. URL https:// mic and data-driven management on human
arxiv.org/abs/2310.03714. workers. InProceedingsofthe33rdAnnualACM
ConferenceonHumanFactorsinComputingSys-
B. Knott, S. Venkataraman, A. Hannun, S. Sen- tems,CHI’15,pages1603–1612,NewYork,NY,
gupta, M. Ibrahim, and L. van der Maaten. 2015. ACM. doi: 10.1145/2702123.2702548.
Crypten: Secure multi-party computation
J. Z. Leibo, A. S. Vezhnevets, M. Diaz, J. P. Aga-
meets machine learning. Advances in Neural
piou, W. A. Cunningham, P. Sunehag, J. Haas,
Information ProcessingSystems, 34:4961–4973,
R. Koster, E. A. Duéñez-Guzmán, W. S. Isaac,
2021.
G. Piliouras, S. M. Bileschi, I. Rahwan, and
S.C.Kohn,E.J.DeVisser,E.Wiese,Y.-C.Lee,and S. Osindero. A theory of appropriateness with
T. H. Shaw. Measurement of trust in automa- applicationstogenerativeartificialintelligence,
tion: A narrative review and reference guide. 2024.URLhttps://arxiv.org/abs/2412.
Frontiers in psychology, 12:604977, 2021. 19010.
V. Krakovna, J. Uesato, V. Mikulik, M. Rahtz, J. Leike, M. Martic, V. Krakovna, P. A. Or-
and S. Legg. Specification gaming: The tega, T. Everitt, A. Lefrancq, L. Orseau, and
flip side of AI ingenuity. DeepMind S. Legg. AI safety gridworlds. arXiv preprint
Safety Research Blog, 2020. URL https: arXiv:1711.09883, 2017.
//deepmind.google/discover/blog/
specification-gaming-the-flip-side-ofH-.aLii,-Qi.nDgoenngu,iJ.tCyh/e.n,H.Su,Y.Zhou,Q.Ai,Z.Ye,
Blog post. and Y. Liu. Llms-as-judges: a comprehensive
surveyonllm-basedevaluationmethods. arXiv
L. Krause, W. Tufa, S. B. Santamaría, A. Daza, preprint arXiv:2412.05579, 2024a.
U.Khurana,andP.Vossen. Confidentlywrong:
exploringthecalibrationandexpressionof(un) J. Li, Y. Yang, R. Zhang, and Y.-c. Lee. Over-
certainty of large language models in a multi- confident and unconfident ai hinder human-ai
lingual setting. In Proceedings of the workshop collaboration.arXivpreprintarXiv:2402.07632,
on multimodal, multilingual natural language 2024b.
generation and multilingual WebNLG Challenge
P. Li, Z. An, S. Abrar, and L. Zhou. Large lan-
(MM-NLG 2023), pages 1–9, 2023.
guage models for multi-robot systems: A sur-
A. Lal, A. Prasad, A. Kumar, and S. Kumar. Data vey, 2025a. URL https://arxiv.org/abs/
exfiltration: Preventive and detective counter-
2502.03814.
measures. In Proceedings of the International
W. Li, J. Lin, Z. Jiang, J. Cao, X. Liu, J. Zhang,
Conference on Innovative Computing & Commu-
Z. Huang, Q. Chen, W. Sun, Q. Wang, H. Lu,
nication (ICICC), 2022.
T. Qin, C. Zhu, Y. Yao, S. Fan, X. Li, T. Wang,
H. C. Lau and L. Zhang. Task allocation via P.Liu,K.Zhu,H.Zhu,D.Shi,P.Wang,Y.Guan,
multi-agent coalition formation: Taxonomy, al- X. Tang, M. Liu, Y. E. Jiang, J. Yang, J. Liu,
gorithms and complexity. In Proceedings. 15th G. Zhang, and W. Zhou. Chain-of-agents: End-
IEEE International Conference on Tools with Ar- to-endagentfoundationmodelsviamulti-agent
tificialIntelligence,pages346–350.IEEE,2003. distillation and agentic rl, 2025b. URL https:
//arxiv.org/abs/2508.13167.
M. H. Lee and M. Z. Y. Tok. Towards uncertainty
aware task delegation and human-ai collabora- H. Lightman, V. Kosaraju, Y. Burda, H. Ed-
tivedecision-making.InProceedingsofthe2025 wards, B. Baker, T. Lee, J. Leike, J. Schulman,
35

IntelligentAIDelegation
I. Sutskever, and K. Cobbe. Let’s verify step by Computing-Proceedings of the Computing Con-
step, 2023. URL https://arxiv.org/abs/ ference, pages 61–74. Springer, 2025.
2305.20050.
Y.Mao,M.G.Reinecke,M.Kunesch,E.A.Duéñez-
S. Lin, J. Hilton, and O. Evans. Teaching models Guzmán, R. Comanescu, J. Haas, and J. Z.
to express their uncertainty in words. arXiv Leibo. Doing the right thing for the right
preprint arXiv:2205.14334, 2022. reason: Evaluating artificial moral cognition
by probing cost insensitivity. arXiv preprint
X.Liu,T.Chen,L.Da,C.Chen,Z.Lin,andH.Wei.
arXiv:2305.18269, 2023.
Uncertainty quantification and confidence cali-
bration in large language models: A survey. In S.MasoudniaandR.Ebrahimpour. Mixtureofex-
Proceedingsofthe31stACMSIGKDDConference perts: a literature survey. Artificial Intelligence
on Knowledge Discovery and Data Mining V. 2, Review, 42(2):275–293, 2014.
pages 6107–6117, 2025.
P. Mazdin and B. Rinner. Distributed and
Y.Liu,G.Deng,Y.Li,K.Wang,Z.Wang,X.Wang, communication-aware coalition formation and
T. Zhang, Y. Liu, H. Wang, Y. Zheng, et al. task assignment in multi-robot systems. IEEE
Prompt injection attack against llm-integrated Access, 9:35088–35100, 2021.
applications. arXiv preprint arXiv:2306.05499,
E. A. M. Michels, S. Gilbert, I. Koval, and M. K.
2023.
Wekenborg. Alarm fatigue in healthcare: a
scoping review of definitions, influencing fac-
J. M. Logg, J. A. Minson, and D. A. Moore. Algo-
tors, and mitigation strategies. BMC nursing,
rithm appreciation: People prefer algorithmic
24(1):664, 2025.
to human judgment. Organizational Behav-
ior and Human Decision Processes, 151:90–103,
Microsoft. Unleashingthepowerofmodelcontext
2019.
protocol (mcp): A game-changer in AI integra-
tion, 2025.
B. Lubars and C. Tan. Ask not what ai can do,
but what ai should do: Towards a framework
E. Mosqueira-Rey, E. Hernández-Pereira,
of task delegability. Advances in neural infor-
D. Alonso-Ríos, J. Bobes-Bascarán, and
mation processing systems, 32, 2019.
Á. Fernández-Leal. Human-in-the-loop ma-
chine learning: a state of the art. Artificial
Z. Luo, Z. Shen, W. Yang, Z. Zhao, P. Jwala-
Intelligence Review, 56(4):3005–3054, 2023.
puram, A. Saha, D. Sahoo, S. Savarese,
C. Xiong, and J. Li. Mcp-universe: Bench- C. Mueller and A. Vogelsmeier. E!ective delega-
markinglargelanguagemodelswithreal-world tion: Understanding responsibility, authority,
model context protocol servers. arXiv preprint and accountability. Journal of Nursing Regula-
arXiv:2508.14704, 2025. tion, 4(3):20–27, 2013.
F. Luthans and T. I. Stewart. A general contin- R.B.Myerson.Optimalcoordinationmechanisms
gencytheoryofmanagement. Academyofman- in generalized principal–agent problems. Jour-
agement Review, 2(2):181–195, 1977. nal of mathematical economics, 10(1):67–81,
1982.
S. Ma, Y. Lei, X. Wang, C. Zheng, C. Shi, M. Yin,
and X. Ma. Who should i trust: Ai or my- O.Nachum,S.S.Gu,H.Lee,andS.Levine. Data-
self? leveraging human and ai correctness e"cient hierarchical reinforcement learning.
likelihood to promote appropriate trust in ai- Advances in neural information processing sys-
assisted decision-making. In Proceedings of the tems, 31, 2018.
2023CHIConferenceonHumanFactorsinCom-
S.K.Nagia. Delegationofauthority: Agreatchal-
puting Systems, pages 1–19, 2023.
lenge for business organisation. ARTIFICIAL
L. Malmqvist. Sycophancy in large language INTELLIGENCE (AI) AND BUSINESS, page 55,
models: Causes and mitigations. In Intelligent 2024.
36

IntelligentAIDelegation
M. Naiseh, D. Al-Thani, N. Jiang, and R. Ali. Ex- for large language models. arXiv preprint
plainablerecommendation: whendesignmeets arXiv:2303.09014, 2023.
trustcalibration. WorldWideWeb,24(5):1857–
R. Parasuraman, R. Molloy, and I. L. Singh.
1884, 2021.
Performance consequences of automation-
M.Naiseh,D.Al-Thani,N.Jiang,andR.Ali. How induced’complacency’. The International Jour-
the di!erent explanation classes impact trust nal of Aviation Psychology, 3(1):1–23, 1993.
calibration: The case of clinical decision sup-
S. Parikh and R. Surapaneni. Powering
port systems. International Journal of Human-
AI commerce with the new Agent Pay-
Computer Studies, 169:102941, 2023.
ments Protocol (AP2), Sept. 2025. URL
https://cloud.google.com/blog/
J. Needham, G. Edkins, G. Pimpale, H. Bartsch,
products/ai-machine-learning/
and M. Hobbhahn. Large language models of-
tenknowwhentheyarebeingevaluated. arXiv
announcing-agents-to-payments-ap2-protocol.
preprint arXiv:2505.23836, 2025. Accessed: 2026-01-20.
I.PastineandT.Pastine. Introducinggametheory:
E. Neelou, I. Novikov, M. Moroz, O. Narayan,
A graphic guide. Icon Books, 2017.
T. Saade, M. Ayenson, I. Kabanov, J. Oz-
men, E. Lee, V. S. Narajala, E. G. Junior,
S. Pateria, B. Subagdja, A.-h. Tan, and C. Quek.
K. Huang, H. Gulsin, J. Ross, M. Vyshegorodt-
Hierarchicalreinforcementlearning: Acompre-
sev, A. Travers, I. Habler, and R. Jadav. A2as:
hensivesurvey.ACMComputingSurveys(CSUR),
Agentic ai runtime security and self-defense,
54(5):1–35, 2021.
2025.URLhttps://arxiv.org/abs/2510.
13825.
M. Petkus. Why and how zk-snark works. arXiv
preprint arXiv:1906.07221, 2019.
E. Nijkamp, B. Pang, H. Hayashi, L. Tu, H. Wang,
Y. Zhou, S. Savarese, and C. Xiong. Codegen: E. Pignatelli, J. Ferret, M. Geist, T. Mesnard,
An open large language model for code with H. van Hasselt, O. Pietquin, and L. Toni.
multi-turn program synthesis. arXiv preprint A survey of temporal credit assignment in
arXiv:2203.13474, 2022. deep reinforcement learning. arXiv preprint
arXiv:2312.01072, 2023.
Z. Ning and L. Xie. A survey on multi-agent re-
inforcement learning and its application. Jour- I. Pinyol and J. Sabater-Mir. Computational trust
nal of Automation and Intelligence, 3(2):73–91, and reputation models for open multi-agent
2024. systems: a review. Artificial Intelligence Review,
40(1):1–25, 2013.
O. Or-Meir, N. Nissim, Y. Elovici, and L. Rokach.
Dynamic malware analysis in the modern Z. Porter, P. Ryan, P. Morgan, J. Al-Qaddoumi,
era—a state of the art survey. ACM Computing B. Twomey, J. McDermid, and I. Habli. Un-
Surveys (CSUR), 52(5):1–48, 2019. ravelling responsibility for ai. arXiv preprint
arXiv:2308.02608, 2023.
D.Otley. Thecontingencytheoryofmanagement
accounting and control: 1980–2014. Manage- C. Qian, Z. Xie, Y. Wang, W. Liu, K. Zhu, H. Xia,
ment accounting research, 31:45–62, 2016. Y.Dang,Z.Du,W.Chen,C.Yang,etal. Scaling
large language model-based multi-agent col-
W.G.OuchiandJ.B.Dowling. Definingthespan laboration. arXiv preprint arXiv:2406.07155,
of control. Administrative Science Quarterly, 2024.
pages 357–365, 1974.
K. Qin, L. Zhou, B. Livshits, and A. Gervais. At-
B. Paranjape, S. Lundberg, S. Singh, H. Ha- tacking the defi ecosystem with flash loans for
jishirzi, L. Zettlemoyer, and M. T. Ribeiro. Art: fun and profit, 2021. URL https://arxiv.
Automatic multi-step reasoning and tool-use org/abs/2003.03810.
37

IntelligentAIDelegation
Y.Qin,S.Liang,Y.Ye,K.Zhu,L.Yan,Y.Lu,Y.Lin, C. Riquelme, J. Puigcerver, B. Mustafa, M. Neu-
X. Cong, X. Tang, B. Qian, S. Zhao, L. Hong, mann,R.Jenatton,A.SusanoPinto,D.Keysers,
R. Tian, R. Xie, J. Zhou, M. Gerstein, D. Li, andN.Houlsby. Scalingvisionwithsparsemix-
Z. Liu, and M. Sun. Toolllm: Facilitating large tureofexperts. AdvancesinNeuralInformation
languagemodelstomaster16000+real-world Processing Systems, 34:8583–8595, 2021.
apis, 2023. URL https://arxiv.org/abs/
2307.16789. J.M.RosanasandM.Velilla. Loyaltyandtrustas
the ethical bases of organizations. Journal of
B. Radosevich and J. Halloran. Mcp safety au- Business Ethics, 44(1):49–59, 2003.
dit: Llms with the model context protocol al-
A. Rosenblat and L. Stark. Algorithmic la-
low major security exploits. arXiv preprint
bor and information asymmetries: A case
arXiv:2504.03767, 2025.
study of uber’s drivers. International
S. D. Ramchurn, D. Huynh, and N. R. Jennings. Journal of Communication, 10:3758–3784,
Trust in multi-agent systems. The knowledge 2016. URL https://ijoc.org/index.
engineering review, 19(1):1–25, 2004.
php/ijoc/article/view/4892.
J.Ruan,Y.Chen,B.Zhang,Z.Xu,T.Bao,H.Mao,
J. Rando and F. Tramèr. Universal jailbreak
Z. Li, X. Zeng, R. Zhao, et al. Tptu: Task plan-
backdoors from poisoned human feedback,
2024.URLhttps://arxiv.org/abs/2311. ning and tool usage of large language model-
14455. based ai agents. In NeurIPS 2023 Foundation
Models for Decision Making Workshop, 2023.
S. Rasal and E. J. Hauer. Navigating complexity:
J. M. Sanabria and P. A. Vecino. Beyond the
Orchestratedproblemsolvingwithmulti-agent
sum: Unlocking ai agents potential through
llms, 2024. URL https://arxiv.org/abs/
market forces, 2025. URL https://arxiv.
2402.16713.
org/abs/2501.10388.
T. Rebedea, R. Dinu, M. Sreedhar, C. Parisien,
T. Sandholm. An implementation of the contract
and J. Cohen. Nemo guardrails: A toolkit for
net protocol based on marginal cost calcula-
controllableandsafellmapplicationswithpro-
tions. In AAAI, volume 93, pages 256–262,
grammablerails,2023. URLhttps://arxiv.
1993.
org/abs/2310.10501.
Y. Sannikov. A continuous-time version of the
M.G.Reinecke,Y.Mao,M.Kunesch,E.A.Duéñez-
principal-agent problem. The Review of Eco-
Guzmán,J.Haas,andJ.Z.Leibo. Thepuzzleof
nomic Studies, 75(3):957–984, 2008.
evaluating moral cognition in artificial agents.
Cognitive Science, 47(8):e13315, 2023. F. Santoni de Sio and G. Mecacci. Four responsi-
bilitygapswithartificialintelligence: Whythey
A. Z. Ren, A. Dixit, A. Bodrova, S. Singh, S. Tu,
matterandhowtoaddressthem. Philosophy&
N. Brown, P. Xu, L. Takayama, F. Xia, J. Varley,
technology, 34(4):1057–1084, 2021.
et al. Robots that ask for help: Uncertainty
alignment for large language model planners. S. Sarkar, M. Curado Malta, and A. Dutta. A sur-
arXiv preprint arXiv:2307.01928, 2023. vey on applications of coalition formation in
multi-agent systems. Concurrency and Compu-
C. O. Retzla!, S. Das, C. Wayllace, P. Mousavi,
tation: Practice and Experience, 34(11):e6876,
M.Afshari,T.Yang,A.Saranti,A.Angerschmid,
2022.
M. E. Taylor, and A. Holzinger. Human-in-the-
loopreinforcementlearning: Asurveyandposi- W. Saunders, C. Yeh, J. Wu, S. Bills, L. Ouyang,
tion on requirements, challenges, and opportu- J. Ward, and J. Leike. Self-critiquing models
nities. Journal of Artificial Intelligence Research, for assisting human evaluators, 2022. URL
79:359–415, 2024. https://arxiv.org/abs/2206.05802.
38

IntelligentAIDelegation
S. Shah. The principal-agent problem in finance. problemsolver. IEEETransactionsoncomputers,
CFA Institute Research Foundation L2014-1, 29(12):1104–1113, 1980.
2014.
J. Sobel. Information control in the principal-
Y. Shao, H. Zope, Y. Jiang, J. Pei, D. Nguyen, agent problem. International Economic Review,
E. Brynjolfsson, and D. Yang. Future of work pages 259–269, 1993.
with ai agents: Auditing automation and aug-
X. Song, Z. Wang, S. Wu, T. Shi, and L. Ai. Gradi-
mentation potential across the u.s. workforce,
2025.URLhttps://arxiv.org/abs/2506. entsys: A multi-agent llm scheduler with react
06576. orchestration, 2025. URL https://arxiv.
org/abs/2507.06520.
M. Sharma, M. Tong, T. Korbak, D. Duvenaud,
C. Stucky, M. De Jong, and F. Kabo. The paradox
A. Askell, S. R. Bowman, N. Cheng, E. Durmus,
of network inequality: di!erential impacts of
Z. Hatfield-Dodds, S. R. Johnston, et al. To-
statusandinfluenceonsurgicalteamcommuni-
wards understanding sycophancy in language
cation. MedJ(FtSamHoustTex),pages22–01,
models. arXiv preprint arXiv:2310.13548,
2022.
2023.
N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, R. S. Sutton, D. Precup, and S. Singh. Between
Q. Le, G. Hinton, and J. Dean. Outra- mdps and semi-mdps: A framework for tempo-
geously large neural networks: The sparsely- ral abstraction in reinforcement learning. Arti-
gated mixture-of-experts layer. arXiv preprint ficial intelligence, 112(1-2):181–211, 1999.
arXiv:1701.06538, 2017.
S. Tadelis and O. E. Williamson. Transaction cost
O. M. Shehory, K. Sycara, and S. Jha. Multi- economics. Thehandbookoforganizationaleco-
agentcoordinationthroughcoalitionformation. nomics, 159(3.1):1, 2012.
In International Workshop on Agent Theories,
W. Takerngsaksiri, J. Pasuksmit, P. Thong-
Architectures, and Languages, pages 143–154.
tanunam, C. Tantithamthavorn, R. Zhang,
Springer, 1997.
F. Jiang, J. Li, E. Cook, K. Chen, and
A.Singh,A.Ehtesham,S.Kumar,andT.T.Khoei. M. Wu. Human-in-the-loop software develop-
A survey of the model context protocol (mcp): ment agents. In 2025 IEEE/ACM 47th Inter-
Standardizing context to enhance large lan- national Conference on Software Engineering:
guage models (llms). 2025. Software Engineering in Practice (ICSE-SEIP),
pages 342–352. IEEE, 2025.
J.SkalseandM.Mancosu.Definingandcharacter-
izing reward hacking. Proceedings of the 2022 J. Teutsch and C. Reitwießner. Truebit: a scal-
AAAI/ACM Conference on AI, Ethics, and Soci- ableverificationsolutionforblockchains. White
ety, pages1–11, 2022. doi: 10.1145/3514094. Papers, 2018.
3534149.
J. Teutsch and C. Reitwießner. A scalable verifi-
P. Sloksnath. Delegating moral decisions to ai cation solution for blockchains. In Aspects of
systems. Master’s thesis, University of Zurich, Computation and Automata Theory with Appli-
2025. cations,pages377–424.WorldScientific,2024.
S. C. Slota, K. R. Fleischmann, S. Greenberg, N.A.TheobaldandS.Nicholson-Crotty.Themany
N.Verma,B.Cummings,L.Li,andC.Shenefiel. faces of span of control: Organizational struc-
Many hands make many fingers to point: chal- ture across multiple goals. Administration &
lenges in creating accountable ai. Ai & Society, Society, 36(6):648–660, 2005.
38(4):1287–1299, 2023.
N. Toma%ev, M. Franklin, J. Jacobs, S. Krier, and
R.G.Smith.Thecontractnetprotocol: High-level S. Osindero. Distributional agi safety. arXiv
communication and control in a distributed preprint arXiv:2512.16856, 2025.
39

IntelligentAIDelegation
N. Tomasev, M. Franklin, J. Z. Leibo, J. Jacobs, A.S.Vezhnevets,S.Osindero,T.Schaul,N.Heess,
W.A.Cunningham,I.Gabriel,andS.Osindero. M. Jaderberg, D. Silver, and K. Kavukcuoglu.
Virtual agent economies, 2025. URL https: Feudalnetworksforhierarchicalreinforcement
//arxiv.org/abs/2509.10147. learning, 2017b. URL https://arxiv.org/
abs/1703.01161.
P. M. Tomei, R. Jain, and M. Franklin. Ai
governance through markets. arXiv preprint E. F. Vignola, S. Baron, E. Abreu Plasencia,
arXiv:2501.17755, 2025. M. Hussein, and N. Cohen. Workers’ health
under algorithmic management: Emerging
K.-T. Tran, D. Dao, M.-D. Nguyen, Q.-V. Pham,
findings and urgent research questions. In-
B. O’Sullivan, and H. D. Nguyen. Multi-agent
ternational Journal of Environmental Research
collaboration mechanisms: A survey of llms,
and Public Health, 20(2):1239, 2023. doi:
2025.URLhttps://arxiv.org/abs/2501.
10.3390/ijerph20021239.
06322.
J. Vok$ínek, J. Bíba, J. Hodík, J. Vybíhal, and
V. Tupe and S. Thube. Ai agentic workflows and
M. P(chou’ek. Competitive contract net pro-
enterprise apis: Adapting api architectures for
tocol. In International Conference on Current
the age of ai agents, 2025. URL https://
Trends in Theory and Practice of Computer Sci-
arxiv.org/abs/2502.17443.
ence, pages 656–668. Springer, 2007.
M. Turpin, J. Michael, E. Perez, and S. R. Bow-
G. Wang, B. Wang, T. Wang, A. Nika, H. Zheng,
man. Language models don’t always say what
and B. Y. Zhao. Ghost riders: Sybil attacks
they think: Unfaithful explanations in chain-
on crowdsourced mobile mapping services.
of-thought prompting, 2023. URL https:
IEEE/ACM Transactions on Networking, 26(3):
//arxiv.org/abs/2305.04388.
1123–1136, 2018. doi: 10.1109/TNET.2018.
R. Uuk, C. I. Gutierrez, D. Guppy, L. Lauwaert, 2818073.
A. Kasirzadeh, L. Velasco, P. Slattery, and
J.Wang,Z.Ren,T.Liu,Y.Yu,andC.Zhang.Qplex:
C. Prunkl. A taxonomy of systemic risks
Duplex dueling multi-agent q-learning. arXiv
from general-purpose ai. arXiv preprint
preprint arXiv:2008.01062, 2020.
arXiv:2412.07780, 2024.
J. Wang, Z. Wu, Y. Li, H. Jiang, P. Shu, E. Shi,
K. Valmeekam, M. Marquez, S. Sreedharan, and
H. Hu, C. Ma, Y. Liu, X. Wang, Y. Yao, X. Liu,
S. Kambhampati. On the planning abilities of
H. Zhao, Z. Liu, H. Dai, L. Zhao, B. Ge, X. Li,
large language models-a critical investigation.
T. Liu, and S. Zhang. Large language models
Advances in Neural Information Processing Sys-
for robotics: Opportunities, challenges, and
tems, 36:75993–76005, 2023.
perspectives, 2024a. URL https://arxiv.
A.H.VandeVen.Theconceptoffitincontingency org/abs/2401.04334.
theory. Technical report, 1984.
L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang,
T.vanderWeij,F.Hofstätter,O.Ja!e,S.F.Brown, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin,
and F. R. Ward. Ai sandbagging: Language et al. A survey on large language model based
modelscanstrategicallyunderperformoneval- autonomous agents. Frontiers of Computer Sci-
uations. arXiv preprint arXiv:2406.07358, ence, 18(6):186345, 2024b.
2025. Published as a conference paper at ICLR
2025. Y.Wang,D.Xue,S.Zhang,andS.Qian.Badagent:
Insertingandactivatingbackdoorattacksinllm
A.S.Vezhnevets,S.Osindero,T.Schaul,N.Heess, agents, 2024c. URL https://arxiv.org/
M. Jaderberg, D. Silver, and K. Kavukcuoglu. abs/2406.03007.
Feudalnetworksforhierarchicalreinforcement
learning.InInternationalconferenceonmachine A. Wei, N. Haghtalab, and J. Steinhardt. Jail-
learning, pages 3540–3549. PMLR, 2017a. broken: How does llm safety training fail? Ad-
40

IntelligentAIDelegation
vancesinNeuralInformationProcessingSystems, J. Yi, Y. Xie, B. Zhu, E. Kiciman, G. Sun, X. Xie,
36:80079–80110, 2023. and F. Wu. Benchmarking and defending
against indirect prompt injection attacks on
O. E. Williamson. Transaction-cost economics:
large language models. In Proceedings of the
the governance of contractual relations. The
31stACMSIGKDDConferenceonKnowledgeDis-
journal of Law and Economics, 22(2):233–261,
covery and Data Mining V.1, page 1809–1820.
1979.
ACM, July 2025. doi: 10.1145/3690624.
3709179. URL http://dx.doi.org/10.
O. E. Williamson. Transaction cost economics.
1145/3690624.3709179.
Handbook of industrial organization, 1:135–
182, 1989.
H.Yu,Z.Shen,C.Leung,C.Miao,andV.R.Lesser.
A survey of multi-agent trust management sys-
M. Wischnewski, N. Krämer, and E. Müller. Mea-
tems. IEEE Access, 1:35–50, 2013.
suringandunderstandingtrustcalibrationsfor
automated systems: A survey of the state-of-
L. Yu, V. Do, K. Hambardzumyan, and N. Can-
the-art and future directions. In Proceedings of
cedda. Robust llm safeguarding via refusal
the 2023 CHI conference on human factors in
feature adversarial training. arXiv preprint
computing systems, pages 1–16, 2023.
arXiv:2409.20089, 2024.
Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong,
M.Yu,F.Meng,X.Zhou,S.Wang,J.Mao,L.Pang,
M. Zhang, J. Wang, S. Jin, E. Zhou, et al. The
T. Chen, K. Wang, X. Li, Y. Zhang, B. An, and
rise and potential of large language model
Q. Wen. A survey on trustworthy llm agents:
based agents: A survey. Science China Infor-
Threats and countermeasures, 2025. URL
mation Sciences, 68(2):121101, 2025.
https://arxiv.org/abs/2503.09648.
Y. Xiao, P. P. Liang, U. Bhatt, W. Neiswanger,
Y. Yuan, W. Jiao, W. Wang, J.-t. Huang, J. Xu,
R. Salakhutdinov, and L.-P. Morency. Uncer-
T. Liang, P. He, and Z. Tu. Refuse whenever
taintyquantificationwithpre-trainedlanguage
youfeelunsafe: Improvingsafetyinllmsviade-
models: A large-scale empirical analysis. arXiv
coupled refusal training. In Proceedings of the
preprint arXiv:2210.04714, 2022.
63rdAnnualMeetingoftheAssociationforCom-
W. Xing, Z. Qi, Y. Qin, Y. Li, C. Chang, J. Yu, putational Linguistics (Volume 1: Long Papers),
C. Lin, Z. Xie, and M. Han. Mcp-guard: A pages 3149–3167, 2025.
defense framework for model context protocol
S.E.Yuksel,J.N.Wilson,andP.D.Gader. Twenty
integrity in large language model applications.
years of mixture of experts. IEEE transactions
arXiv preprint arXiv:2508.10991, 2025.
onneuralnetworksandlearningsystems,23(8):
F. Xu, Q. Hao, C. Shao, Z. Zong, Y. Li, J. Wang, 1177–1193, 2012.
Y. Zhang, J. Wang, X. Lan, J. Gong, et al. To-
ward large reasoning models: A survey of rein- F. M. Zanzotto. Human-in-the-loop artificial in-
forced reasoning with large language models. telligence. Journal of Artificial Intelligence Re-
Patterns, 6(10), 2025. search, 64:243–252, 2019.
L. Xu and H. Weigand. The evolution of the con- Q. Zhan, Z. Liang, Z. Ying, and D. Kang. Injeca-
tract net protocol. In International Conference gent: Benchmarkingindirectpromptinjections
on Web-Age Information Management, pages intool-integratedlargelanguagemodelagents,
257–264. Springer, 2001.
2024.URLhttps://arxiv.org/abs/2403.
02691.
Y. Yang, Y. Wen, J. Wang, and W. Zhang. Agent
exchange: Shaping the future of ai agent N. Zhang, J. Yan, C. Hu, Q. Sun, L. Yang, D. W.
economics. arXiv preprint arXiv:2507.03904, Gao, J. M. Guerrero, and Y. Li. Price-matching-
2025. basedregionalenergymarketwithhierarchical
41

IntelligentAIDelegation
reinforcement learning algorithm. IEEE Trans-
actions on Industrial Informatics, 20(9):11103–
11114, 2024.
W.Zhang,C.Cui,Y.Zhao,R.Hu,Y.Liu,Y.Zhou,
and B. An. Agentorchestra: A hierarchical
multi-agent framework for general-purpose
task solving. arXiv e-prints, pages arXiv–2506,
2025a.
Z. Zhang, Q. Dai, X. Bo, C. Ma, R. Li, X. Chen,
J.Zhu,Z.Dong,andJ.-R.Wen. Asurveyonthe
memory mechanism of large language model-
basedagents. ACMTransactionsonInformation
Systems, 43(6):1–47, 2025b.
K. Zhao, L. Li, K. Ding, N. Z. Gong, Y. Zhao,
and Y. Dong. A survey on model extraction
attacks and defenses for large language mod-
els, 2025. URL https://arxiv.org/abs/
2506.22521.
W. Zhao, Y. Gao, S. A. Memon, B. Raj, and
R. Singh. Hierarchical routing mixture of ex-
perts. In202025thInternationalConferenceon
Pattern Recognition (ICPR), pages 7900–7906.
IEEE, 2021.
L. Zhou, X. Xiong, J. Ernstberger, S. Chaliasos,
Z. Wang, Y. Wang, K. Qin, R. Wattenhofer,
D. Song, and A. Gervais. Sok: Decentral-
ized finance (defi) attacks, 2023. URL https:
//arxiv.org/abs/2208.13035.
Y. Zhou, T. Lei, H. Liu, N. Du, Y. Huang, V. Zhao,
A.M.Dai,Q.V.Le,J.Laudon,etal. Mixture-of-
experts with expert choice routing. Advances
in Neural Information Processing Systems, 35:
7103–7114, 2022.
C. Zhu, M. Dastani, and S. Wang. A survey of
multi-agent deep reinforcement learning with
communication. Autonomous Agents and Multi-
Agent Systems, 38(1):4, 2024.
Z. Zou, Z. Liu, L. Zhao, and Q. Zhan. Blocka2a:
Towardssecureandverifiableagent-to-agentin-
teroperability.arXivpreprintarXiv:2508.01332,
2025.
42
