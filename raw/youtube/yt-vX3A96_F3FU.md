---
schema_version: 1
id: yt-vX3A96_F3FU
type: youtube
title: 'Graph RAG: Improving RAG with Knowledge Graphs'
url: https://www.youtube.com/watch?v=vX3A96_F3FU
authors:
- Prompt Engineering
ingested_at: '2026-06-17T20:57:07Z'
content_hash: sha256:ebacdadb39c603c2b44dcd1f3228621a3d264aaf507fc9618a5f377a381cbdd0
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Prompt Engineering
  channel_url: https://www.youtube.com/@engineerprompt
  duration_seconds: 956
  caption_track: fetched
  snippet_count: 262
filter:
  score: 0.72
---
[0] Graph RAG works great, but there was
one major issue and that is the cost.
[5] Microsoft just open sourced
GraphRAG, a system that they
[9] presented almost a year ago.
[10] This is a groundbreaking system
that combines knowledge graphs with
[14] Retrieval Augmented Generation or RAG.
[16] And the goal is to address some of the
limitations of the current RAG systems.
[20] The code is available on GitHub
and you can start using it in
[23] your own projects right now.
[24] You can use this with both
proprietary models like GPT 4
[29] and local models like Lama3.
[32] In this video, I'm going to show you
how graph RAG works and then guide you
[36] through setting it up on your local
machine to run some example tests.
[41] We will also take a look at
cost implications of a run.
[45] But before we dive into graph RAG, let's
first understand the motivation behind it
[49] by looking at traditional RAG approach.
[52] Traditional RAG is a method where
the language model retrieves
[56] relevant documents from a large
corpus to generate more accurate
[60] and contextually relevant responses.
[62] There are three steps
and here is how it works.
[65] In the first step we process the
documents and convert them into vectors.
[70] So we take our original documents,
we divide them into sub documents
[73] using a chunking strategy.
[75] We compute embeddings for each of the
chunks and then we store the chunks
[79] plus the embeddings in a vector store.
[81] That becomes our knowledge base.
[84] The next phase is query phase where
the user asks a question, we compute
[89] embeddings for that query, then do a
similarity search on all the vectors
[93] that are present in the vector database
and we retrieve the most relevant chunks
[98] or sub documents from our vector store.
[100] Then we combine the query plus
the retrieved context, give
[103] it to large language model
to generate a final response.
[107] As you can see, there are three
major limitations with this approach.
[110] The first one is limited
contextual understanding.
[113] So RAC can sometimes miss the nuances
in the data due to its reliance
[117] on retrieved documents alone.
[119] It doesn't have a holistic overview
of the document, so it doesn't really
[125] understand the overall picture.
[128] Now there are scalability issues.
[129] As the corpus grows, the retrieval
process can become less efficient.
[134] And there is associated complexity.
[137] So integrating external knowledge
sources in meaningful way can
[141] be complex and cumbersome.
[142] And with GraphRag, Microsoft is trying
to address some of these issues.
[147] Along with the code, Microsoft also
released a highly detailed technical
[152] report or paper titled from local
to global, a graph rag approach
[157] to query focused summarization.
[160] In this section, we are going to look at
the technical details of how this works.
[164] If you are just interested in using
the package, skip to the next section,
[170] but I highly recommend to stick around
for this section to understand how
[174] this whole thing actually works.
[175] So here's a quick representation of
the approach in the form of a flowchart
[179] that I created with the help of cloud 3.
[182] 5 sonnet.
[183] Now, just like rag there are
two different parts or phases.
[186] One is the indexing phase in the
other one is the query phase.
[190] During the indexing phase, we take
our original source documents.
[194] and convert them into sub documents
using a chunking strategy.
[198] This step is very similar to
traditional rag approaches, but
[202] then within each chunk, we try
to identify different entities.
[207] Now these entities can be
people places, companies, right?
[211] Depending on the context
that you're providing.
[214] And we also look for relationship
between these different entities
[218] across different chunks.
[220] So we.
[222] do two parallel things.
[223] One is entity extraction and
then relationship extraction.
[227] And we use that information
to create a knowledge graph.
[230] Knowledge graph is basically a
set of nodes that preserves the
[234] relationship between different entities.
[236] Now, based on the knowledge graph,
we create communities and I'll
[241] explain the step and a lot more
details in the subsequent section.
[245] But this is basically we detect
entities that are closer to each other.
[250] And then we describe the relationship
between these entities or
[254] communities using different levels.
[256] So in the paper they talk about three
different levels of communities,
[259] and I'll explain what those are.
[261] But for each one of those,
we create summaries.
[264] So think about it this way, that we
basically look at a set of chunks.
[269] Create summaries for those and then
combine it with Another set of chunks
[274] using reduced map approach create
summaries with those And so on and
[278] so forth until we have a holistic
overview of whatever is in this
[281] set of documents Now during the
query phase we take the user query.
[287] Then we select the community level
Basically, what level of information
[292] or what level of details we want, and
then think about this is again like
[297] a retrieval process that you're doing
on chunks, but rather than chunks,
[300] now you're doing it on communities.
[303] And we look at summaries of the
communities that will generate
[308] partial responses for us.
[310] If there are multiple communities
involved, then we combine those
[314] responses into a single response.
[316] And that is going to be the
final answer from the model.
[319] As we will learn in this video,
graph RAG is awesome, but there are
[323] still use cases for traditional RAG
systems, especially when it comes
[326] to the cost of running a graph RAG.
[328] If you want to learn about RAG beyond
basics, I have a course dedicated to
[333] the topic, in which we start with basic
techniques, and then we go into advanced
[337] techniques of building robust RAG systems.
[340] If that interests you, link
is in the video description.
[344] Now, back to the video.
[346] I hope this gives you a very good
understanding of how GraphRag works.
[350] Now let's set this up on our local machine
and we can start experimenting with it.
[355] They have provided very detailed
instructions on how to get started,
[358] so we're going to be using those.
[360] So first I'm going to create
a conda virtual environment.
[363] I'm going to call it GraphRag.
[365] And then we need to activate this
virtual environment, so we're going to
[368] just use conda activate GraphRag, and
our virtual environment is ready to go.
[374] Next, we need to install the package, so
we're going to use pip install graph rank.
[379] This is going to install the
graph rank python package for us.
[383] Okay, next we need to
run the indexing process.
[386] For that, we need our own dataset.
[389] But before copying the data set,
we're going to create another folder
[393] within the current working directory.
[395] If you can see the current working
directory is completely empty.
[398] They recommend to create a rack test and
then when that there's another folder
[402] called input, but you can essentially
provide any path that you want.
[406] So what I, what I did here was
I just created another package
[410] or sorry, another folder here.
[412] And it's basically rack test input, and
we're going to put our data in there.
[417] Next, we need a source document so
currently I think they only support
[420] plain text, and they have provided
a link to Charles Deacon's book, A
[426] Christmas Carol, so we're going to just
use that as a source of information.
[429] So if I run this command, this
will download the text of the book.
[434] So here's the project Gutenberg
ebook of a Christmas carol.
[439] I believe they currently support only
plain text, so you can potentially
[443] use something like Markdowns.
[446] And this is a pretty huge book.
[451] Okay, next we're going to set up our
workspace variables and for that we
[456] will be using this command python
dash m then Graph rag dot index.
[462] So basically we want to create an index
out of the Data that we have provided.
[468] However before that we need to initialize
our configurations for the variable
[475] to work And then we provide the root
directory where the data is stored.
[479] So when we run this, you're going to see
that it's going to create a whole bunch of
[483] different files in our current workspace.
[487] Okay, so we can see that here is the
input, but apart from that it also created
[493] an output where we can see a log, but it
hasn't really run the indexing process
[498] yet because we need to provide our LLM.
[501] It also created different prompts,
so these are the prompts that
[505] it's going to internally use to
create this knowledge graph for us.
[510] And these are basically the
prompts that they have set up.
[513] Now, there has been a lot of discussion
regarding these prompts these are
[517] very comprehensive prompts, so it
basically uses these prompts to
[521] not only extract different entities
from the provided corpus, but also
[526] creates the communities as well as
the summaries for each community.
[529] Next, we need to provide
our graph API key.
[532] This is basically the OpenAI API key.
[536] So you can select your OpenAI
model and provide that in here.
[540] Now you also have a settings.
[541] yml file.
[543] This is where you want to
set different configurations.
[546] For example, we set our graph API key.
[549] So it's going to get the
information from there.
[551] We want to use the GPT 4 O in this
case because that's faster and it's
[556] going to hopefully cost us less.
[559] You can also set the maximum number of
tokens that it's going to process, right?
[563] There are a whole bunch of
settings that you can do in here.
[566] And if you were to use a local
model such as the one that you
[569] are serving through OLAMA, You
can also change the base API path.
[576] So the URL so for example, if you were
to use grok that is serving lemma three.
[582] You will just provide that base URL here.
[584] Now for embeddings it also
is currently using the open
[587] AI embedding the small model.
[590] But you can change that if you want,
if you want to use another provider.
[594] Currently the chunk size
is limited to 300 tokens.
[598] We can play around with it, but we're
going to just go with the defaults.
[601] And there's going to be an
overlap of a hundred tokens.
[604] Thanks.
[606] Now as I was showing you different
prompts so for example, for entity
[609] extraction, here's the prompt
that it's going to be using.
[612] You can modify these prompts based
on your own needs which I highly
[617] recommend to do because that will
give you a lot more control compared
[620] to whatever is there by default.
[623] Okay, so with the previous command
it created the structure for us like
[627] how The different parameters are set
but now we need to Run this in order
[633] to actually start creating the index.
[636] So instead of initializing it.
[638] We'll just run the index creation
process this is going to basically Go
[645] through the whole document identify
different entities that are present
[649] in the documents or the corpus and
then Create relationship between
[653] those create a knowledge bank graph,
then create communities on top of it,
[658] and then it will create a
summarization of different
[661] communities at a different level.
[663] So this process can take some time.
[665] And I also want to see how much this
is going to cost us, because cost
[669] is definitely a factor because you
are not only running the embedding
[673] model, but you are also running this
entity recognition step as well as
[678] the community summarization step
that involves the use of an LLM.
[683] Now in this step it's actually currently
doing the summarization description.
[687] So the index creation process is complete
and then you can look at the output.
[691] So we're going to look at different
artifacts that it created.
[696] So these are just the database
files that it created.
[700] There is a JSON which keeps
track of different stats.
[703] So for example, total runtime,
that's the number of seconds it took.
[707] So about two minutes.
[709] There was a single document, right?
[711] So you will get a whole
bunch of information here.
[714] And then there is also another
indexing engine log that also
[719] describe different parameters.
[721] And now the next step is
going to be to run queries.
[724] Again, we're going to just use the
examples that they have provided.
[727] Now there are different set
of queries that you can run.
[729] So for example in order to run a
query, you're going to use Python M.
[733] That's basically referring to
the current Python environment.
[736] Then instead of indexing, you
are going to run the query.
[739] We will need to provide the
path where the data is stored.
[743] And the method is basically the
community level that you want to use.
[747] So basically, if you want to use the
root level, which is looking at all the
[751] information present in the document.
[753] Then you can use the global method.
[757] So something like this prompt, what are
the main themes in this story will need
[762] access to the global level information.
[765] So if you run this, this will just
use the global level or the top
[769] level community to generate answers.
[772] And here's the response that we got.
[774] So it says, success, global search
response, and top themes in the story.
[778] So it's transformation and redemption,
charity, and generosity, right?
[782] We are just looking at the examples
that they have provided in the
[785] subsequent videos, I'll show you a
lot more complex examples, working
[789] with different types of datasets.
[792] Now If you are looking for a specific
character within a story, then you
[796] probably want to use more local level or
lower level communities or information.
[801] So, in this case, we are using the method
as local because we are specifically
[805] looking for a single character.
[807] So In this case, it will just look
at as a community level or chunk
[811] level summaries and try to combine
multiple of them to generate an answer
[816] for this specific character for us.
[818] And then it was able to identify
a different relationships.
[822] Now you can see that a normal traditional
rag might be able to do something
[827] like this because it will simply look
at in different chunks where this
[832] specific characters is mentioned and
if they're it's describing like a
[836] relationship with another character.
[838] However, if you are looking for the
main theme of the document, that's where
[843] RAG is going to fail because RAG just
looks at the specific chunks that are
[849] retrieved during the retrieval process.
[851] It doesn't really have an
overall big picture of the
[855] corpus that you are providing.
[857] Also both for the global as well as
for the local level it will tell you
[861] where the information is coming from.
[863] So it actually cites its
sources, which is pretty neat.
[866] Graph RAG works great, but there was
one major issue and that is the cost.
[871] So for this specific example we send
a total of 570 requests through the
[878] API and we are talking about GPT 4 or
requests But for the embedding model,
[883] we only send about 25 requests, Now
in terms of the total number of tokens
[887] that were processed It's well over 1
million tokens, which comes out to be
[892] around 7 7 So we spend about 7 in total
to process this book and create a graph
[899] rack, which could be prohibitively
expensive for a large corpus of data.
[905] So this is definitely something you need
to consider if you're planning on using
[909] graph rack in your own application.
[911] I think this is substantially
more expensive if you were to
[914] build a traditional rack system.
[918] Anyways, I highly recommend
you check out graph rack.
[920] It's an innovative approach.
[923] Now, Microsoft is not the only company
that they have implemented a graph RAG.
[928] There are some other options.
[930] For example, Lama Index has their
own implementation of Knowledge
[934] Graph RAG query engine, and Neo4j
has their own graph RAG package that
[941] you can use to create graph RAGs.
[944] If there is interest, I will
create some content comparing these
[948] different implementations as well.
[949] Let me know in the comment section below.
[951] I hope you found this video useful.
[953] Thanks for watching and as
always, see you in the next one.
