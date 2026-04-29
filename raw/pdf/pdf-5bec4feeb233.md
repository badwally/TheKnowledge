---
id: pdf-5bec4feeb233
type: pdf
title: State of Foundation Models - 2025 (Innovation Endeavors)
url: ''
authors: []
ingested_at: '2026-04-29T16:15:19Z'
content_hash: sha256:e43d2aed2e73fbc677af4083da097027959369890a57f937a0f6ab4c67470d21
source_path: raw/pdf/pdf-5bec4feeb233.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 126
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__5bec4fee.pdf
published_at: '2025'
---
INNOVATION
ENDEAVORS
State of Foundation Models, 2025 | Davis Treybig | June 2025
1
1

STATE OF FOUNDATION MODELS, 2025
Video presentation here >
Edited with Capsule >
2

TABLE OF CONTENTS
01 Setting the Stage
02 Models
03 Use Cases & Applications
04 Building Foundation Model Products
05 Market Structure & Dynamics
06 What’s Next?
07 What We’re Excited to See Built
3

TLDR;
(cid:0) Generative AI has gone mainstream – 1 in 8 workers worldwide now uses AI every month, with 90% of that growth
happening in just the last 6 months. AI-native applications are now well into the billions of annual run rate.
(cid:0) Scaling continues across all dimensions – All technical metrics for models continue to improve >10x year-over-year,
including cost, intelligence, context windows, and more. The average duration of human task a model can reliably do is
doubling every 7 months.
(cid:0) The economics of foundation models are…confusing – OpenAI & Anthropic are showing truly unprecedented growth,
accelerating at $B+ of annual revenue. But, end-to-end training costs for frontier models near $500M, and the typical
model become obsolete within 3 weeks of launch thanks to competition & open source convergence.
(cid:0) Just like the smartest humans, the smartest AI will “thinks before it speaks” – Reasoning models trained to think
before responding likely represent a new scaling law — but training them requires significant advances in post-training,
including reinforcement learning & reward models. Post-training may become more important than pre-training.
(cid:0) AI has now infiltrated almost all specialist professions – From engineers and accountants to designers and lawyers, AI
copilots and agents are now tackling high-value tasks in virtually all knowledge worker domains
(cid:0) Agents finally work, but we are early in understanding how to build AI products – Agents have finally hit the
mainstream, but design patterns & system architectures for AI products are still extremely early.
(cid:0) “AI-native” organizations will look very different – Flatter teams of capable generalists will become the norm as
generative AI lessens the value of specialized skills. Many roles will blur - such as product, design, & engineering.
4

01 Setting the stage
5

Two key insights unlocked this technology wave
01 Self Supervised Learning to scale data
“John went to the mall and Input “John went to the mall and bought…”
bought a hamburger from
Johnny Rockets” Output (label) “...a hamburger from Johnny Rockets”
02 Attention Architecture (“Transformer”) to scale compute
⊙ Compute efficient (parallelizable)
⊙ Accurate (understands full context)
The dog went to the pound
6

Scaling models leads to “emergent” behavior
Google Research 2022 7

So we pushed for exponential growth in modal size…
Coatue AI 2022 8

As a result, we got the fastest rate of adoption of new technology of all time
ChatGPT’s Explosive Growth ChatGPT reached 100M users in 60 days
Weekly Active Users (in millions)
The Information 9

As well as some of the fastest revenue ramps of all time
Model Revenue Active Users Timeframe Employees
GitHub Copilot ~400M ARR 1,500,000 3 years NA
Midjourney ~200M ARR 20,000,000 2 years ~40
Cursor ~100M ARR 360,000 1 year ~20
10

All technical metrics are following exponential curves
January 2023 Spring 2025 Delta
Context window (frontier) 2 – 8k tokens ~1M tokens ~100 – 500x increase
Cost/token (GPT4-level) $100 million $.1 million >1000x reduction
Compute to train (FLOP) ~10^24 ~10^28 >1000x increase
11

LLMs quickly surpass almost all new benchmarks as they are released
Science reasoning
Advanced Math
Professional reasoning
(biology, law, philosophy…)
Complex language reasoning
General reasoning Grade-school math
Graduate physics
“AGI”
Software Engineering
12

The task span LLMs can handle has jumped from 1 second to 1 hour
— in just 5 years
Measuring AI Ability to Complete Long Tasks 13

LLMs reasoning capabilities now exceed humans in various domains
01 LLMs now outperform doctors 02 LLMs now solve geometry problems
in aggregate on numerous more accurately than 99.999% of
diagnostic tasks people on Earth
AlphaGeometry, Towards Conversational Diagnostic AI 14

Diffusion has seen a similarly exponential rate of improvement
Imagen – Google Deepmind (~2022) Visual Electric (2024)
15

02 Models
16

Training costs for frontier models continue to balloon
Leading models now cost >$300M
Model Release Date Estimated Training Cost (millions)
$4.50
GPT-3 2020
PaLM 540B 2022 $10.00
Claude 2 2023 $25.00
GPT-4 2023 $100.00
Gemini Ultra 2023 $190.00
LLaMA 3.1 (405b) 2024 $120.00
Llama 4 2025 $300.00+
Extreme Cost of Training AI Models, Sam Altman on GPT4, Llama 3.1, Llama4 17

But, frontier models also depreciate on a 6–12 month timescale
GPT-4
⊙ $100M+ to train
⊙ Closed source
⊙ Released March 2023
DeepSeek-VL
⊙ <$10M to train
⊙ Open Source
⊙ Released March 2024
18

Open source continues to converge with closed source
Artificial Analysis - Q4 2024 Report, see also Maxime Labonne 19

Most models only last 3 weeks
Data from The Intelligence Consolidation (Re-Visualized) 20

Data budgets are also insane, though data budgets and
compute budgets are blurring
⊙ Deepmind spending $1B a year on data
annotation
Illustrative breakdown of spend for leading model
⊙ OpenAI spending ~3B a year on training
and data
Pre-training 150-300M
⊙ Meta spent $125M on post-training data
for LLaMA 3
Post-training (incl RL) 50-150M
⊙ OpenAI paying $2–3k per individual
reasoning trace
Data 50-150M
OpenAI Expenses
21

Zeitgeist shifting away from purely scaling parameters & pre-training
Smaller models are more efficient to serve - in cost, memory, and latency - and advances in inference-time compute are
reducing the need to max out pre-training
Epoch AI 22

Smaller models more saturated on large datasets are less “training
efficient”, but are much better to serve
For a given loss, smaller models requires far
more training tokens, but:
1. Smaller models are easier and
cheaper to run inference
2. Smaller models are lower latency
We don’t train LLMs Enough, Llama 3 8B is 75x Chinchilla 23

What’s Next?
⊙ Synthetic data
⊙ Agents (systems
engineering)
⊙ Inference time scaling
⊙ ?
Ilya Sutsekevar 24

Inference time compute (“reasoning”) is a new frontier
What’s the implication of the new
Internal Monologue
User Prompt Canadian prime minister on foreign
exchange rates?
To answer this question, I first need
to consider:
1. The economic drivers of
exchange rates
Reasoning *Thought for 5 minutes*
2. Canada’s current exchange
rates
Below is a holistic overview of the 3. The differences in policy
between Canada’s new and
impact the new Canadian prime
Output former prime minister
minister may have on FX rates,
broken down by…. To start….
25

…and represents a new scaling law for models
Learning to reason with LLMs 26

Interestingly, test-time compute is not a particularly new concept
Cicero 27

Small reasoning models can outperform models 10–20x larger
given enough time to think
3B reasoning model
beats 70B model given
enough thinking
Scaling Test Time Compute 28

There are multiple ways to develop reasoning models
⊙ Pay for or create labeled reasoning traces
Post-train on ⊙ Synthetically generated reasoning traces in verifiable
domains (e.g. Math problems)
reasoning traces
⊙ Train process reward models (PRM) or outcome reard
models (ORM) to guide sampled generations
Use “search” techniques
⊙ Model and secondary system (verifier/validator)
at inference time
go back and forth to guide “thinking”
29

There are multiple ways to develop reasoning models
Post-train on
Model “thinks with itself” for a long time – single,
reasoning traces
continuous, long stream of output tokens
Use “search” techniques
Control flow mediates interaction between model and
at inference time
secondary systems guiding thinking
30

o1-pro is likely “best of n o1”
o1 response 1
o1 response 2
Verifier picks
User Prompt
“Best of N”
o1 response 3
o1 response 4
31

Common versions of inference-time search techniques
Huggingface 32

Challenges and open questions with reasoning models
How well do easily constructed synthetic data sets generalize?
Does synthetic math & coding data translate well to other domains?
What is the optimal reinforcement learning algorithm/approach?
⊙ Sampling strategy
⊙ Process vs outcome rewards
⊙ Noisy & sparse reward signals in complex tasks
⊙ Computational cost/complexity
Data generation & acquisition
High end reasoning traces worth $3k…
Scaling RL Compute 33

The post-training algorithm landscape continues to evolve
“Write a short story about a dog”
Response Response Mechanism
“The dog jumped over a tree…” Reward = 3.7 Reinforcement learning
Proximal Policy
Optimization (PPO)
“The dog jumped over a tree…” Preferred Supervised training w/
Direct Preference
preference pairs
Optimization (DPO)
“The dog killed a cat…” Dispreferred
“The dog jumped over a tree…” Preferred Train reward model +
Guided Reinforcement
reinforcement learning
Preference Optimization
“The dog killed a cat…” Dispreferred
(GRPO)
34

Verifiers & reward models are becoming essential for AI development
Procedural verifiers Learned verifiers
Domain Verifier
Process reward model
Code generation
Compile + unit tests
tasks
Outcome reward models
Math problems Theorem provers
Learned domain specific verifiers
Domains with
“precise” answers Majority voting
In theory generalize better,
More accurate, but don’t generalize well
but are they accurate enough?
See also: DeepSeek - Generalist Reward Modeling, Scaling RL Compute 35

Generalist reward models are the “holy grail”, but are difficult to build
DeepSeek - Generalist Reward Modeling 36

Specialized fine tuning may look increasingly autonomous
and self-supervised
1. Take sample inputs
2. Generate sample
responses via test-time
compute
3. Use reward model to
score responses
4. Run RL loop to fine tune
Tao 37

Mixture-of-experts models are becoming increasingly commonplace
A router dynamically activates different parts of the model based on the input - with each sub-component acting as
an 'expert' in a specific domain
Notable MoE models
● DeepSeek v2 & v3
● Mixtral
● GPT4
(rumored 8x220B models)
DeepSeek MoE 38

Context windows growing dramatically, though beware of false advertising
Llama 4 Scout is both
pre-trained and post-trained with a
“
256k context length
We present compelling results in
tasks such as retrieval with
“retrieval needle in haystack”...
– Llama 4 Paper
Andriy Burkov
39

Tokenization remains a stubbornly “hacky” aspect of foundation models
Tokenizing the word “Egg”
Building Tokenizer from Scrarch (Andrej Karpathy), Byte Latent Transformer 40

Training directly over bytes vs. tokens may be one potential solve
Byte Latent Transformer: Patches Scale Better Than Tokens 41

Mechanistic interpretability is maturing rapidly. Will steering become more
common outside of research?
Mapping the Mind of Large Language Model (Anthropic) 42

Multimodality continues to advance, but omni-modality is early
VLMs have gained steam over Omni-modal models are still early and in the
the last few years research phase
[Text, Image, Video, Aud io] Text
PaliGemma, Chamelon 43

Other interesting architectural trends gaining steam
Attention variant that works well in very long
State Space Models
context situations (e.g. audio)
Generalization of diffusion which may allow
Flow Matching Models
for more efficient learning
Diffusion alternative that makes better use of
Inductive Moment Matching
pre-trained parameters via “jumps”
Language modeling via diffusion, vs.
Discrete Diffusion Models
auto-regression
44

Image models are not just higher quality, but much more precise - now
capable of in-context learning, typography, and native style transfer
“Ghiblify” this Precise text control without control nets
ChatGPT, Reve Image 45

Video models are hitting their “ChatGPT Moment”
Veo 46

Generalized robotics models are showing real promise
Robots can now perform novel tasks in never-before-seen environments - which was unheard of just a few years ago
Physical Intelligence 47

World models simulate actions in environments
Key initial use case is training data for robotics. Although, longer-term this may form the basis of “dynamic” media
experiences (e.g. a ‘choose your own’ adventure TV show)
Genie 2 48

Audio, voice, & speech models continue to mature
Example Maturity
Music Mainstream
Audio & Voice Cloning Mainstream
Voice-to-Voice Very early
Suno Example, Eleven Labs Example 49

Evo 2: A “DNA foundation model” trained in self-supervised way on
genomic sequences
A G C T A T C T T A G C G C A T T T A T T C G C
Input sequence Output “label”
Evo 2 50

Potential use cases of DNA Foundation Model
These models are nascent and do not have broad industry adoption
Mutation Effect Prediction
Change sequence & analyze sequence
“I went to the store and bought an elephant”
likelihood to identify “damaging” mutations
Biological feature discovery
Use interpretability techniques to train SAE that
identify biologically-relevant concepts
Guided genome design
Combine w/ biological function prediction
A G C T A T C T T A G C > A Score = X
models like Enformer to design sequences
SAE on Evo2 (Goodfire), Enformer 51

Beyond DNA, foundation model concepts are being applied to many
areas of the sciences. But market maturity in these domains is early.
The biggest barrier to real adoption is data availability: high-quality data in these domains is scarce
Given function, predict protein design Given small molecule, predict human pharmacokinetics
Given protein structure, predict geometry Given past weather, predict future weather
Given cell perturbation, predict expression Given material structure, predict properties
scBERT
Chroma, Iambic, AlphaFold, GenCast, scBERT, Orbital Materials 52

03 Use Cases & Applications
53

Search & information synthesis remains the marquee LLM use case
Likely >1000 startups with product-market-fit that are vertical-specific versions of this use case
“General Purpose” Domain Specific
Investing
Legal
Construction
Healthcare
People search
54
Glean, Perplexity, Bench, AlphaSense, Tetrix, Harvey, Trunk Tools, OpenEvidence, Happenstance

AI is fundamentally disrupting software engineering
⊙ SWE Copilots are a ~$2B a year
market in the span of ~2–3 years
⊙ Cursor is fastest growth SaaS ever -
now at ~1B ARR
swyx 55

It’s difficult to overstate the impact of AI code generation products
Many of the best engineers I know think this has changed their workflow more than anything in the past 20+ years
Garry Tan 56

LLMs are beginning to touch the entire software development lifecycle
Likely that all developer tool products are rethought in a world of AI code gen
Code Review Site Reliability Engineer
Documentation Observability
Migration Autonomous SWE
Prototyping Spec & Dependencies
Testing & QA And a lot more…
Graphite, Greptile, Dosu, Mintlify, Mechanical Orchard, Lovable, Bolt, Ranger, QA Tech, Cleric, Resolve, AllHands, Replit, Tessl 57

AI copilots and agents will transform all specialized, high-skilled
knowledge work
PCB Engineers Animation
Game
3D Designers
developers
Electrical Mechanical
engineers engineers
Video
Accountants
editors
Quilter, Bezi, Cadstrom, Basis, Cartwheel, Odyssey, Leo, Sequence 58

Creative expression of all forms is being re-invented
Video & Animation Brand Design 3D Design
Lonely Little Flame (Runway), Visual Electric, Meshy 59

Other interesting AI startup categories
Verticalized writing Verticalized “Translation”
Education, coaching, Semi-structured
& companionship Systems of Record
Second order effects
Voice Agents
of AI
“Tier 1” Labor
“Synthetic” data
Automation
Gale, Speak, Ferry Health, Dropzone, LightTable, Clarify, Profound, Evidenza
60

Therapy, life organization, and learning rank among top overall AI use cases
HBR survey of online posts, articles, and
blogs touching on how people use AI
HBR - Top Gen AI Use Cases 61

04 Building foundation model products:
Patterns, challenges, ecosystem, & infrastructure
62

From model, to RAG, to agents - LLM-based apps are maturing significantly
Notion AI Github Copilot Deep Research
model model + data model + data + tools
63

Agents are models using tools in a loop
Common Tools
⊙ Search files/data
Action/Tool
⊙ Write code
⊙ Call API
Human LLM Call Environment
⊙ Search web
⊙ Use browser
Feedback
STOP
64
Visual inspiration from Hannah Moran (Anthropic)

Leading agent startups will recurse 50+ times, using a range of tools
30-60 chained LLM calls,
which include:
⊙ Planning
⊙ Retrieving & analyzing
“Help me reconcile this month’s
internal data
collections with revenue” ⊙ Writing & running code
⊙ Browsing the internet
⊙ Manipulating spreadsheet
⊙ Calling APIs of accounting
systems/tools
Basis 65

Generalist agents are not here yet, but a number of constrained agent
startups have strong product market fit in purpose-built use cases
General agent startups But, “specialized” agents are doing
have struggled extremely well
Alex Gravely 66

Agent success is often a function of expectation-setting
Learning to use agents is a skill - the SWEs I know who make the best use of remote agents spent time learning how to do it
“When it worked, it was impressive.
Does Devin suck?
But that’s the problem - it rarely worked”
“An AI is now the most productive
Or is it amazing? engineer at our company (measured by
PRs merged)”
Thoughts on a month with Devin, Sahil Lavingia, Swyx 67

Key traits of successful agent products
● Automated vs. supervised ● Expectation setting - where and
Finding the right human
● Review & management workflows - e.g. when to use? Where NOT to
vs. machine balance
“Agent inbox” use?
● High existing failure / mistake rate
● Status quo = nothing - e.g. bug
● “First pass” workflows - use AI to catch
Use case selection report no one will get to
things earlier/sooner
● Low risk of mistakes
● Coverage more critical than correctness
● How does the AI “show its work”? ● Minimizing cognitive overhead
Product & Design ● Built-in correction mechanisms (e.g. edit of management
action, rewind, restart from here, etc) ● Workflow specificity
68

Good teams often think more in terms of “systems” than models
"What are the best arguments for and against the claim that social media is
harmful to democracy?"
Query LLM Response
Generate arguments
LLM LLM
for $query
(Generator) (Critic)
Rank top 3
Synthesize LLM
Response
conclusion
(Judge)
Generate arguments
LLM LLM
against $query
(Generator) (Critic)
Rank top 3
69

We use ensembles of models much more internally than people
might think…
“
If we have 10 different problems, we might solve them using 20
different model calls, some of which are using specialized
fine-tuned models.
They're using models of different sizes because maybe you have
different latency requirements or cost requirements for different
questions. They are probably using custom prompts for each one.
Basically you want to break the problem down into more specific
tasks versus some broader set of high level tasks.
– Kevin Weil, CPO, OpenAI
X post
70

Common systems paradigms in foundation model apps
● Repeated sampling
● Best of N
● Multi-hop planning
● Verification & voting
● Fan out, fan in
Large language monkeys 71

There will likely emerge higher level frameworks that remove the need to
manually tune AI systems
Ember
Ember, DSPy, Christopher Potts Talk, Compound AI Systems 72

Apple Intelligence – bad product but illustrative system architecture
Base models + LoRA adapters, client + server hybrid architecture
On-device Server-side
Platform Tools
Router Tools
Models
Search Index Orchestrator LoRA Adapters
Model
Large server-side LLM
LoRA Adapters
Language Diffusion
Base Model Base Model
Apple Intelligence 73

While context windows continue to increase, retrieval is here to stay
RAG beats long context models by order of magnitude on quality, cost, and latency for most non-trivial use cases
Quality Cost
Latency
Time to first token w/ Gwen 2.5 Turbo
68 seconds
1M context
p99 search latency over 1M
677 ms
documents
Yurts benchmark, Gwen 2.5 Turbo 74

Advanced retrieval pipelines can be incredibly complex
Information retrieval remains one of the most underrated skills in most applied AI startups
● Pre-filtering
● Neural + lexical hybrid
search
● Multi stage reranking
● Advanced embedding
techniques (e.g.
Matryoshka)
● Cross-encoders
● And a lot more…
Quadrant Hybrid Search 75

What do the best applied AI startups obsess over?
Solve research problems w/
Evaluations Data curation
UX
You are your evaluations
Solve a research grade
technical problem, or scope
down the workflow?
Search & Retrieval Model layer as “last resort” Systems thinking
“We spend 10x the Prompt >
engineering effort on Systems engineering >
retrieval as we do models” Post train > Pre-train
What we’ve learned from a year of building with LLMs 76

Context engineering is the new prompt engineering
For even simple queries, it is not uncommon to have 10x+ the relevant context than can be effectively utilized by the
model. Context management thus becomes a constrained optimization & recommendation systems problem - what
information should be prioritized given constraints?
A simple code copilot query
Relevant context categories Description Approx. Size
might have ~1M of relevant (tokens)
context, but:
PR diff + related new code The actual PR files (e.g. 6 files modified, 2 added) 30,000
1. Your model caps out at Immediate file neighbors Files in the same module or directory (5–10 files) 50,000
128k context
User permission subsystem Historical core code for auth/user perms 120,000
2. Exceeding 50% of the
Relevant documentation API usage guides, internal security practices, auth system design docs 100,000
“theoretical” capacity may
confuse model in complex Recent user interaction history Copilot memory of user's past 10 PRs, preferred patterns, prior comments 50,000
query
System prompt Role instructions, formatting rules, security checklist reminders 100,000
3. At least 10-20% must be Test coverage context Nearby test files, known test gaps for affected areas 100,000
reserved for output tokens
Stack traces or bug reports Linked recent runtime errors or audit trail data 80,000
Company-wide code patterns High-level embeddings or prompts representing org-wide secure coding style 100,000
How do you map ~1M
General project structure Core architecture scaffolding (entry points, service graph, data flow) 150,000
of addressable context
to ~60k of space? Total 880,000
77

Key questions in context engineering
Coverage vs. specificity Pre-processing context at inference time
What % of context window should you fill per query? At what Assuming you have more context than can be fed to the
point does distracting the model more outweigh providing model, do you simply “cut” some data, or do you apply
more relevant data? more sophisticated techniques like:
1. Semantic deduplication
Ranking & Relevance 2. Summarization
3. Information compression
What content should be prioritized? For a given query, what
is the most relevant content? This maps to traditional Such techniques can, in theory, reduce the # of tokens of
recommendation systems context without compressing information as much
Bin-Packing & Ordering Context “Planning”
The order in which context appears in context Assuming you can retrieve context from many
windows affects models’ ability to reason over it. How different sources per query but don’t have the latency
do you optimally order and interleave context? budget to retrieve from them all - which do you
prioritize given the query?
Note that more “traditional” prompt engineering is a lot less relavent as models get bigger - e.g. see ProSA, Tobi Lutke on the rise of Context Engineering 78

As AI systems become more complex, the way we evaluate them will
need to change as well
Pseudocode for classic RAG retrieval test - define golden retrieval outputs for given user
query & database state, and compute precision/recall/RR
function test_retrieval(query, database, retriever, golden_outputs):
Early generative AI systems had fixed control flows with
retrieved_docs = retriever(query, database)
often <5 steps (e.g. typical RAG system).
matched_docs = 0
This means manual debugging is not hard, and you can For doc in retrieved_docs:
write tests for each sub-step of the pipeline (e.g. lexical If doc in golden_outputs, matched_docs +=1
search step, semantic search step, LLM step, etc)
Precision = matched_docs/ len(retrieved_docs)
Percival - debugging agents to analyze your agents
Agents often have semi-unbounded control flows, and
extremely complex reasoning traces involving 100+
steps.
Manual debugging becomes almost impossible, and you
can’t write tests for each sub-step because the
permutational complexity of paths is too large. We likely
need to move to agents evaluating agents or other more
automated forms of simulation/testing.
Trail Paper 79

For those training or post-training models, high quality data curation is
massively under-appreciated
Consider models trained on two comparable datasets:
RedPajama-V1
Model 1 (well known, “high quality” training Baseline
set that was basis of LLama)
Vs. baseline, you can achieve….
Highly curated derivation of ● Same accuracy for ~13% of the compute and 7.7x
RedPajama-V1 (e.g. removing the training speed
Model 2
redundant data, creating better
● 8.5% more absolute accuracy for the same training
data distribution)
cost
● 48% the inference cost for the same training cost
via smaller mode
Dataology Example 80

There is a lot room for differentiation in product & design - few AI
startups are truly reinventing workflows
Granola entered seemingly saturated market, and won via completely rethinking the UX patterns of AI note taking. There are
huge opportunities for design-led companies and designer founders right now
And 50+ more
81

UX design patterns for foundation model apps still feel…early
82

Great AI startups must balance building around model deficits today
vs. waiting to ride model advances
100+ AI image products built In-context learning w/ images obviates
around fine-tuning the entire flow
Lensa 83

We realized that with the new GPT4o model,
our system design from 9 months ago was no
“
longer relevant.
We have entered a totally new paradigm and
are completely redesigning our system to
reflect it.
- AI startup founder
84

Model Context Protocol is emerging as the ecosystem standard for tools
OpenAI, Anthropic, Deepmind, & Microsoft have now all publicly supported MCP
Gmail Endpoint 1
MCP Server 1: Gmail
Gmail Endpoint N
Figma Endpoint 1
MCP Client
MCP Server 2: Figma
(Claude)
Figma Endpoint N
Blender Endpoint 1
MCP Server 3: Blendr
Blender Endpoint N
85

Example – using Model Context Protocol to design 3D shapes
in Blender from Claude
Siddharth Ahuja 86

The interface for agentic tool use is extremely important
Consider a coding agent that can:
1. Edit files
2. Search files
3. View files
4. Manage context
Subtle changes in agent interface massively impact quality!
Building coding agents 87

In this vein, many leading startups build first-class integrations to optimize
the tool-use interface rather than use MCP
Our agent literally became 10x better when we
“
stopped using standard MCP servers and built
extremely deep, specialized integrations into the
SaaS tools it needed to use
- CEO of Series A agent startup
88

Personality is an underrated aspect of differentiation for foundation model
products
“General consumer” AI products heavily
oriented towards instruction-following,
research-assistant workflows
But, different personality traits desired in
other categories, e.g.
1. Design – Creativity & Randomness
2. Education – Authority vs. sycophancy
3. Therapy – Question asking vs. answer
giving
Base Models Beat Aligned Models at Randomness and Creativity 89

The infrastructure ecosystem around foundation models apps
has matured considerably
Inference Data Evals & Frameworks
management Observability & libraries
Embeddings Search Agent Tools Domain Specific
& Retrieval
Web Search
Document Proce ssing Infra
Browser use
AI Video Infra
Code environments
90

Foundation models are also driving a renaissance in semiconductors
New wave of transformer-focused chip
Three key trends
startups being founded
⊙ Rapid proliferation of transformer-oriented chip
Founded in 2022,
startups (see left)
raised $125M
⊙ For the first time ever, AI compute costs >>>> AI
labor costs. So, rewriting AI software for new
Founded in 2022, chips is now worth it
raised $120M
⊙ Consolidation of AI models driving
semiconductor companies to inference business
models (e.g. Groq)
Founded in 2019,
raised $160M
91

05 Market Structure & Dynamics
92

~10% of all venture dollars in 2024 went to foundation model companies
VC Invested in FM Labs Total Global Venture % of Global VC to FM
Year
(Primary Rounds) Funding Labs
2020 <$0.1 B $294 B ~0.03%
2021 $2.3 B $643 B ~0.36%
2022 $1.3 B $462 B ~0.28%
2023 $15 B $285 B ~5.3%
2024 $33 B $314 B ~10.5%
Crunchbase 93

And >50% of all venture dollars in 2025 has gone to AI
Coatue 2025 Report 94

Foundation model startups are also accelerating at 1B+ revenue
Annualized revenue reached $2
billion in the first quarter, the
company confirmed, more than
doubling from a $1 billion rate
in the prior period
The Information, CNBC 95

OpenAI is becoming a consumer app company,
and Anthropic an API company
Tanay’s Newsletter 96

Leading model companies will likely have to become application layer
companies to survive
97

Google was slow out of the gates, but seems increasingly unstoppable
Google “owns” pareto frontier of speed vs. quality as of April 2025. Reflective of how this is an economies of scale business
Latent Space 98

Memory is emerging as the key potential stickiness driver for
consumer AI chat apps like ChatGPT
Whoever owns general consumer AI memory will own “Sign in with X” for all AI applications - allowing users to “bring their
own memory”. But, memory is very difficult to get right.
Sample memory architecture from Mem0 - key question is what to remember and how to
distill it, as well as how to blend memory with other context especially in longer sessions
Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory, Memory for ChatGPT 99

Will foundation model companies in physical domains like robotics
be able to “defy gravity” like we have seen in images & text?
Operational complexity of these domains are much higher than pure software. But, pricing is similar to software
Company Description Funding Key Investors
Building foundation models for robotic control and Thrive Capital, NEA, Khosla, etc.
Skild AI 350M+
manipulation
1X (formerly Halodi) Humanoid robotics with AI training systems $100M+ OpenAI Startup Fund, Tiger Global, EQT
LLM-native robot training and cobot manipulation
Cobot AI 150M+ Possibly early-stage VCs (unconfirmed)
stack
Focused on training AI agents for general physical
Physical Intelligence (Pi) 500M+ Likely stealth or early-stage funding
tasks
Figure AI Humanoid robots powered by advanced AI models ~$675M Microsoft, OpenAI, Nvidia, Jeff Bezos
Sanctuary AI General-purpose humanoid AI systems $100M+ Bell, Export Dev. Canada, others
Agility Robotics Humanoid warehouse and logistics robots $180M+ DCVC, Playground, Amazon Industrial
100

High valuations at the application layer, but also unprecedented
revenue growth
⊙ Bolt - $0 to $20M in 60 days
Series B & C AI Companies - Valuation &
⊙ HeyGen - $0 to $35M in a year
Growth Premium (2H’23 - ‘24 YTD)
⊙ Harvey - $1M to $15M in a year
⊙ Hebbia - $500k to $10M in a year
88x
⊙ Glean - $10 to $40M in a year 464%
⊙ Together - $1 to $10M in a year
29x
197%
⊙ Github CoPilot drives 40% percent of
GitHub revenue growth
⊙ OpenAI - >$2B Annual Run Rate
Avg. Revenue Avg. Growth
Multiple Rate
Redpoint 2024 AGM 101

AI-native applications are now in the multi-billion dollar run rate
Tanay Japiura X post 102

AI applications are fundamentally resetting expectations for what people
will pay for software
It is not unreasonable to suspect most
professionals will be paying
5–10k+/month in next few years
“Amp is unconstrained in token usage
(and therefore cost). Our sole incentive is to
make it valuable, not match the cost of a
subscription”
Tibor Blahor X, Amp 103

Even in categories where the incumbent has every conceivable
advantage, startups win
False narrative that AI is a ‘sustaining innovation’. Building successful AI products looks too different.
vs.
vs.
104

Huge risk of novelty effect revenue in AI startups – numerous examples of
“rise and fall” revenue curves
AI Photo Apps (TechCrunch) 105

Overall, the AI market feels very “bubbly” across many dimensions
Many companies burning $50M+ a year on training without established product-market-fit
Sifted article 106

Market structure of the GPU ecosystem looks profoundly different than the
CPU ecosystem, driving rise of new “GPU Cloud” vendors
Two drivers
CPU Clouds GPU Clouds
Gen AI (GPU) workloads exhibit scaling
● Bundle hardware w. cloud ● Offer zero software laws, meaning that incremental compute
always has marginal advantage.
services beyond access to the GPU
itself
● Sell “low level” software So, given fixed budget, you care more about
services (e.g. EC2) at very ● Do not focus on additional GPU-time vs. paying margin for
low margin, and higher incremental services “value add” software”. CPU workloads do
level services at not benefit from more compute beyond
incrementally higher ● Extreme focus on fixed what is needed.
margins duration, longer term
contracts
● Primarily pay-as-you-go Dollar cost of GPU workloads tends to be
model >>> CPU workloads. As such, labor
relationship flips - better to pay
someone $1M a year to write custom
software than eat 10% margin increase
for bundled software.
Very good discussion of this here w/ SF Compute 107

NVIDIA & the GPU ecosystem remain the “guaranteed” winners
“AI Inference token generation has surged tenfold in just one year…” - NVIDIA Q1 Report
NVIDIA Q1 Report 108

06 What’s next?
109

Operating as an “AI-native” company looks fundamentally different
The best companies are increasingly adopting a mantra of: “Learn how to use AI, or leave.”
Shopify Memo 110

Small, capital efficient teams are the new normal
“Its last funding round was a modest $12 million Series A from Accel last year.
Back then, it had 16 people; today it employs just 30.”
Upstarts Media 111

And the composition of teams is rapidly changing
“I increasingly don’t see a difference between
“
designers & product managers in our company”
–
VP Product, Growth-stage startup
“AI has completely changed how I think about hiring
“ as a CMO. I don’t hire specialists anymore. I hire
generalists who can use AI tools”
–
CMO, Publicly-listed company
112

Learning to “manage” fleets of AI workers will become a new skill,
not dissimilar from managing people
“Agent Inbox” Design Pattern Emerging
I haven’t written a new line of
code myself in 3 months.
“
I spend all my time managing
and reviewing agents
–
CTO, leading CodeGen startup
See also LangGraph Agent Inbox 113

Products are being designed for AI as the primary “consumer”, not humans
.cursorrules files are the new 80% of Neon database instances
d ocs? created by AI agents, not humans
Cloudflare Worker, Nikita Shamgunov X 114

Where will the most value be destroyed?
Outsource to In-house Incumbents in “line of fire” of AI
Functions that were traditionally outsourced to For example - unstructured data businesses (e.g.
agencies & consultancies will be moved in-house CRM), creative tool businesses (e.g. Figma),
(e.g. video production) developer tool businesses (e.g. Github)
Specialist to Generalist Companies unwilling to go through cultural &
organizational pain
People in extremely specialized jobs, and tools
oriented towards specialists, will be at risk as Adapt to AI, or lose
generalists + AI can achieve similar results
Middle management will be eroded
Jobs primarily oriented around communication and
information transfer will be deleted (e.g. project
manager, middle manager)
115

Is AGI close? The smartest AI researchers seem to think so…
These models are just advanced
statistical prediction devices
There will be AGI There will be AGI
in 3 years in 3 years
116

07 What We’re Excited to See Built
117

The downstream impact of AI code generation
The proliferation of AI code generation will have far reaching impacts on the rest of the
software development lifecycle
What this might look like:
Reinvention of the SLDC The AI first software organization
How might CICD, deployment, observability, git, and similar The divide between engineering, product, and design is
change in a world where AI is writing more code than blurring. Task management tools will manage tasks for
humans? agents just as much as they manage humans. As
organizational structures change in these ways, what new
Software engineering “shifting right” needs emerge?
Many designers / PMs are already prototyping and submitting
PRs thanks to AI code gen. Is there room for “IDEs” or Validation, Testing, & Guardrails
similar products for such personas? How will traditional The importance of testing, validation, and guardrails on
design & product tools change? software is going up dramatically. Will traditionally niche
approaches become mainstream (e.g. load testing, fuzz
testing, formal proofs, etc)? Will “review” workloads like
code review need to be rethought?
We may also need better ways to automate “product”
feedback as well – e.g. using LLMs to run synthetic
See also - Agent First Developer Toolchain, The Visual IDE experiments, synthetic UXR studies 118

Modern data-as-a-service businesses
LLMs have fundamentally altered our ability to collect, create, structure, understand, and
transform data. We predict there will be a renaissance of “Data-as-a-Service” companies
What this might look like:
Collect previously inaccessible data Use LLMs at the “last-mile” in data delivery
Use voice agents to call people or interview people. Use Allow users to get “custom” data on demand vs. being forced
email agents to solicit data at a novel scale. Use LLMs into a predefined schema/structure. Build rich query &
conversational ability to extract deeper, more flexible insights analysis workflows into the data business.
from people (e.g. Listen Labs)
Synthetic + Real
Structure previously unstructure-able data LLMs are very good at mimicking users/people. Use LLMs to
E.g. turn personal websites into metadata-rich people create synthetic data, and blend that synthetic data with real
profiles. data in an intelligent way (e.g. Evidenza)
Novel business models
If AI lowers the cost/effort/time required to collect certain data by 1000x via synthetic results, AI interviews, or similar, can
you re-invent the business model of a data/research category? E.g. could you build a proactive expert interview platform
that reaches out to you with relevant, personalized interviews
Good examples include Happenstance & Juicebox (people data), Exa (Web Data), and Ferry Health (Provider Data). 119

Next-generation creative tools
There’s an obvious opportunity to disrupt creative expression of all forms
What this might look like:
Defensibility via something besides AI Mixing traditional editing w/ AI
Mechanisms worth exploring: Immense opportunity to innovate on how to combine
traditional editing modalities with generative AI, allowing for
Networks – New forms of social networks built around
both rapid experimentation & precise control.
AI-based democratization of creation. Allow users to “fork”
or “remix” content generated by others, or create new forms
E.g. generative 3D + mesh editing + point cloud editing + 3D
of marketplaces for AI-native creators
style transfer. Subframe is a good example of this in UX design
(combining “vibe prototyping” w/ classical layer editing)
Runtimes – Lower level infrastructure innovations in
computer graphics or similar that become more valuable as
You need VSCode in order to build the copilot
AI makes it easier to produce content
Unlike in software engineering, most other professional design
Workflow Specificity – Not enough companies have focused domains lack an open source editor with a rich plugin
on specific types of creators. ecosystem.
E.g. what might an AI image gen company built purely for
So, how do you sequence building the editor, then the copilot?
brand design, or purely for photographers, look like?
E.g. see Sequence in video editing
120

Data for AI
Data is likely to remain the largest bottleneck for advancing AI systems. What are novel and
clever ways of producing more, high-fidelity data?
What this might look like:
Data as a by-product Community & Network Based Evals
Products or applications which are offered for “free” but LMArena is a good, early example of tapping into the
generate high-quality data for ML systems as an implicit “wisdom of the crowd” to produce evaluation criteria for
byproduct (more here) models.
Simulation & RL Environments What are other mechanisms for creating marketplaces or
What might an “Ansys for RL” look like? Can we come up with networks for people to evaluate AI systems?
high-quality environments to train, evaluate, and improve
agents? What might these look like and could a startup help Verifiers, Checkers, & Reward Models
create, manage, and run them? Generalist reward models and verifier models are likely to
become a standard model class, analogous to embedding
Data management for AI models, which assist in generating reward data for AI.
Better ways to structure, manage, query, cluster, curate &
clean data for AI (e.g. Datology) “Vertical” Annotation companies
Companies offering extremely high quality annotation data in
specialized domains that are outside the scope of
“mainstream” labeling labs (e.g. DavidAI in audio12) 1

AI & Science
Generative models will have a profound impact across the sciences - from chemistry,
biology, materials, mathematics, climate, and more
What this might look like:
Data for the sciences AI & Math
Data is, by far, the limiting factor for foundation model utility
Autonomous theorem proving
in many science categories such as biology & chemistry.
We often need to “prove” traits of mission critical systems -
e.g. proving that aircraft will behave correctly, or that a
We think there are opportunities around novel forms of data
distributed system has no consensus bugs.
capture (e.g. sensing/screening), as well Mercor/Scale style
businesses that identify more scalable forms of data
Can you combine LLMs w/ formal mathematical languages
annotation. E.g. Elio Labs building a novel microscope
like Lean to build autonomous verifiers, reducing the
designed specifically for AI.
cost/effort/complexity to prove traits of systems by multiple
order of magnitude?
Closed-Loop Generate + Verify (e.g. “AI Scientist”)
Combine advances in generative models with improvements
Auto-formalization & Optimization
in traditional computational modeling (e.g. CFD) and wet lab
Mathematical optimization (e.g. Gurobi, Mathworks) has
automation to form closed-loop, generator + verifier style
traditionally been limited by the knowledge of how to
systems in areas like materials, biology, chemistry, etc.
formalize business problems into math. LLMs are good at
this. Does this allow for novel startups?
E.g. Orbital Materials does this in materials 122

Infrastructure for AI
AI systems & workloads are creating many new infrastructure requirements, as well as
altering that way we need to think about traditional infrastructure categories
What this might look like:
Multi-Modal Data Management Infrastructure primitives for AI
Generative models mean most companies will increasingly Web search for AI systems, browsers for AI systems,
need to manage & process complex multi-modal data, computing sandboxes for AI, wallet & payments infra for AI,
including audio, video, images, text. The tooling to do this etc. Most “web primitives” will need to be redesigned for AI
is still early (e.g. see Aperture, Lance as good examples)
Infra problems that get 100x worse with agents
AI-provisioned infrastructure For example, authorization and fine grained access control
Many traditional infrastructure categories (e.g. databases, for internal services will get 100x worse when a bunch of AI
VMs, APIs) are transitioning to being used more by AI agents have access to do many things in your environment.
agents than humans.
GPU Ecosystem
This greatly increases the importance of serverless Dealing with GPUs is still immensely complicated. Lots of
architectures, scale-to-zero, multi-tenancy w/ strong continued opportunity for GPU abstraction, multi-tenant
isolation, treating everything-as-code, & support for GPUs, abstracting GPU vs. CPU, and novel compute
ephemeral and volatile workload patterns (e.g. see why marketplaces for GPU (e.g. SF Compute)
Replit uses Neon as a backend*)
123
*See also how Bauplan is interesting in terms of exposing data pipelines to agents since everything is sandboxed and git-versioned by default, a rarity in data infrastructure

Foundation Model Systems
How do infrastructure & tooling needs change as we begin to view foundation model
applications more like systems?
What this might look like:
Optimization of FM Systems Reinforcement Learning & Verifiers
Along the lines of DSPy & Ember - how do we make it There is likely a startup opportunity to offer best in class
easier to build, test, and evaluate complex foundation generalist reward models and verifiers as an API, similar to
model systems which make heavy use of more complex what we saw with embedding models (e.g. see GR)
systems paradigms such as repeated sampling, fan out +
fan in, verifiers, and similar? Beyond this - it is becoming clear that most AI application
companies will benefit from doing domain-specific RL
I think over time this will more like “simulation” - ala against end-to-end task success in their apps. The tooling &
Applied Intuition in autonomous vehicles. Given infra to do this is very complex. How do we make it easier?
sophisticated FM applications can likely be treated as
complex systems, you will likely want optimize them end Generator + Verifier Systems
to end. I am extremely interested in any founders combining
foundation models as “generators” with secondary verifier
systems - e.g. see KernelBench and this blog
124

INNOVATION ENDEAVORS
About the Author
Davis Treybig is a Partner at Innovation Endeavors, an early-stage
venture fund that backs founders solving complex technical and
engineering challenges to rethink large industries.
Artificial intelligence is a core focus area of the fund. We have
invested broadly in AI across areas like biotechnology (e.g. Eikon),
robotics (e.g. Gatik), computer vision (e.g. Planet), financial research
(AlphaSense), healthcare (Viz), the built environment (e.g. Trunk
Tools), & more.
Davis primarily invests in computing infrastructure, machine
intelligence, and next-generation tools for builders - including
developers, designers, and engineers. Recent investments include
Augment, Bauplan, Capsule, Dosu, Extend and Responsive.
davis@innovationendeavors.com • Substack • Twitter • LinkedIn
125

INNOVATION ENDEAVORS
davis@innovationendeavors.com
126
