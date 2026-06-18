---
schema_version: 1
id: yt-fB2JQXEH_94
type: youtube
title: 'RAG vs Agentic AI: How LLMs Connect Data for Smarter AI'
url: https://www.youtube.com/watch?v=fB2JQXEH_94
authors:
- IBM Technology
ingested_at: '2026-06-17T20:57:42Z'
content_hash: sha256:e2b7c635d8e875c7efea45a9c2ce4406167efd73aaa905e74e27748f65afdb71
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: IBM Technology
  channel_url: https://www.youtube.com/@IBMTechnology
  duration_seconds: 588
  caption_track: fetched
  snippet_count: 94
filter:
  score: 0.7
---
[0] I think it's fair to say that some of the most used AI buzzwords in recent times have
[7] been, well, one of them is certainly agentic AI, and... let me
[14] guess another one, right? Probably RAG. Yeah. Retrieval augmented generation. And with those
[21] buzzwords has come plenty of hype and preconceived notions. Preconceived notions like
[27] how the primary use case for agentic AI today is coding. Exactly. Or that RAG is always the best
[34] way to incorporate specific, up-to-date information into a model's context window. Wait, so
[40] are we saying that these things are not the case? Oh, Cedric. You know, this is where we wheel out
[47] the consultant's default answer, right? Well, I guess I do. Is RAG always the best
[54] option? Well, here it comes. It depends. It depends. There you go. You know, I spent seven
[61] years as a technical consultant, and no matter what the question, a good old "it depends," that
[66] always seems to work. Well, I have an idea. How about we explain what it depends on. Right. So,
[72] let's start off by explaining what these terms agentic AI and RAG really mean. And then you can
[78] get your practitioner viewpoint out where these buzzy technologies are actually going to be put
[83] into action. Now, AI multi-agent workflows, they perceive their environment, they make
[89] decisions and they execute actions towards achieving a goal. And all of this happens with
[95] minimal human intervention. Now, architecturally, these components, they kind of form a loop. So, the
[101] first thing on the loop might be to perceive. And once they've perceived their
[108] environment, they can consult memory, they can
[114] reason, they can act along a particular path,
[121] and then they can go through the final stage, which is to observe what happened, and kind of
[127] round and round we go in a loop. the key here is that each agent operates at the application
[134] level. They're making decisions, they're using tools and they can communicate with each other.
[139] Now Martin, that's great. But if I had to pick the most common use case for agentic AI, I think it has
[145] to be coding agents, right? Uh, yeah. You mean like, uh, like code assistants and copilots? Precisely.
[150] And these are examples of agents that can help plan and architect new ideas that can
[157] help write code straight to our repository, and even help review the code that we've generated—with
[164] minimal human guidance and by using LLMs that have larger context windows with reasoning
[170] capabilities. This, this kind of looks like a, like a mini developer team, like where you have maybe a,
[175] an architect agent that kind of plans out the feature. And then we've got the
[182] implementer that's going to come along and actually write the code. And then we've got the
[186] reviewer that checks out that code, and then maybe send some feedback in a loop like this.
[193] Exactly. And this agentic pattern still needs human intervention. But our job is to be more of a
[199] conductor of an orchestra, right, than play a single instrument. Now, let's also think about
[205] another use case for agentic AI. Think about enterprises with the need to handle support
[210] tickets or HR requests. Or, for example, customers who have some particular query where specialized
[217] agents can autonomously filter and query this to the right agent that's able
[224] to then use tool calling in order to use services or an API, using some type of
[231] protocol like model context protocol, which standardizes the interaction between our LLMs and
[237] the tools that we use every day. Cool. So instead of using a chat window with an LLM to kick off an
[244] action, agents can be responsive in their own environment. Exactly. But, but there is a
[251] challenge, right? Because without reliable access to external information, these agents, they can
[257] quickly hallucinate, or they can make misinformed decisions. And one way we can limit
[264] those misinformed decisions is with retrieval augmented generation or
[270] RAG. Right. And RAG is essentially a two-phase system because you've got a offline phase where
[276] you ingest and index your knowledge, and an online phase where you retrieve and generate on demand.
[282] And the offline part, it's pretty straightforward. So, we start off with, well, let's start it over
[288] here. We're going to start with some documents. So, these are your documents. That could be Word files, it
[293] could be PDFs, whatever. And we're going to break them into chunks and create vector
[298] embeddings for each chunk using something called an embedding model. Now,
[305] these embeddings, they get stored into a special type of database called
[312] a vector database. So, now you have a searchable index of your knowledge. And when a query
[318] hits the system—so we've got perhaps here a prompt from the user—that's where the
[325] online face kicks in. So, the prompt goes to a RAG retriever, and that takes
[332] the user question and it turns it into vector embeddings using the same embedding model. And
[339] then it performs a similarity search in your vector database. Now, that's going to return back
[346] to you the top K most relevant document chunks, perhaps 3 to 5 passages that are most likely to
[352] contain the answer. And that is what is going to be received by the large language
[359] model at the end of this. Wow, Martin! And this is really powerful. But when we start to scale things
[366] up with more data, right, from our organization, or perhaps allow more users to start using
[372] this RAG application, this is where it gets really tricky. Because the more documents or tokens that
[379] our large language model is going to retrieve, well, the harder it is for the LLM to recall that
[384] information, in addition to increased cost for our AI bill and wait times. And if we actually plot
[391] this out roughly, when we talk about accuracy and the amount of tokens retrieved by our RAG
[396] application, well, the more we add sometimes can have a marginal increase in performance or
[401] accuracy, but afterwards can in ... result in degraded performance because of noise or redundancy.
[408] So, maybe not everything should be dumped into the context of an LLM with RAG. But going back to
[414] Martin's point about the two phases of RAG, let's start to talk about ingestion. Because we need to
[419] be really intentional about our data curation, using perhaps open-source tools like Docling
[425] that can help us do document confersion ... conversion to get it ready for our RAG
[430] application. That means starting from, for example, PDF types to m-machine-readable and LLM-readable
[436] types like Markdown, with their associated metadata. And this means not just the text from
[442] our PDFs and documents or spreadsheets, but also tables, graphs, images, pages that are
[449] truncated and much, much more. So here we can enrich your data before we write it to that
[454] vector database or a similar storage. But after ingestion, the next step is retrieval or also
[461] known as context engineering. So, context engineering, as the name implies, allows us to
[468] form our context for the LLM for RAG applications into a compressed and
[474] prioritized uh,result. So, this starts with hybrid recall from databases, right? So, if the user is
[481] asking, "Hey, what is agentic AI?" what we're going to do is use both the semantic meaning of
[488] our question, but also do keyword search, specifically in this example, for agentic AI. Now,
[495] when we do the recall to get that information from our database, what we're also going to do
[500] when we get those top K chunks, as Martin mentioned, is re-rank them for relevance,right, to
[506] prioritize them for our LLM. When we get this back, well we can also do combination of
[513] chunks. So if these two chunks are related, well, we'll put them together and piece this, so at the
[518] end of the day, when we provide the context and the question for our LLM, we have one single
[524] coherent source of truth. This results in higher accuracy, faster inference and cheaper AI cost. Now
[530] that sounds great. And speaking of costs, I hear that local models can power
[537] RAG and agentic AI. Is that, is that the case? Yes, the rumors are true because instead of paying for
[543] an LLM, lots of developers have already been using open-source models, using open-source tools
[550] like vLLM or Llama C++. And this allows us to maintain the same API as
[557] a proprietary model but have the added benefit of data sovereignty—so, keeping everything on premise—and
[563] tweaking our model runtime for KV cache in order to have big uh, improvements that could
[570] speed up our RAG or agentic AI applications. Yeah, so that is AI agents with the
[577] help of RAG, a winning combination. Always, right? Well, maybe not
[584] always, but, you know, of course, it depends.
