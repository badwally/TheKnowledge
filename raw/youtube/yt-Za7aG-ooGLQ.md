---
schema_version: 1
id: yt-Za7aG-ooGLQ
type: youtube
title: 'GraphRAG Explained: AI Retrieval with Knowledge Graphs & Cypher'
url: https://www.youtube.com/watch?v=Za7aG-ooGLQ
authors:
- IBM Technology
ingested_at: '2026-06-17T20:57:44Z'
content_hash: sha256:45432c48ad5b2b0dae5612aa9a20c16d8f54151b65e04658e8a41e94dccb8520
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: IBM Technology
  channel_url: https://www.youtube.com/@IBMTechnology
  duration_seconds: 859
  caption_track: fetched
  snippet_count: 219
filter:
  score: 0.8
---
[1] Today I'm going to show you how to populate a 
knowledge graph and query it using an LLM.
[6] Graph retrieval augmented generation.
[9] or GraphRAG
[10] is emerging as a powerful alternative to vector search methods.
[14] Instead of using a vector database,
[16] GraphRAG systems store data in the format of a knowledge graph
[20] using a graph database.
[22] In a knowledge graph, the relationships 
between data points, called edges,
[26] are as meaningful as the connections between data points,
[30] called vertices, or sometimes nodes.
[33] A GraphRAG approach leverages the structured nature of graph databases
[37] to give greater depth and context of retrieved information
[41] about networks or complex relationships.
[46] The first step in setting up our system is creating 
and populating the knowledge graph.
[52] We'll be using an LLM to assist in creating the knowledge graph.
[56] Given unstructured text data,
[59] the LLM will extract entities and relationships from the data,
[64] transforming the data into structured data,
[67] which can then be inserted into the knowledge graph.
[72] After the knowledge graph is created,
[74] we'll be using the LLM to query data from the knowledge graph
[78] and return the response in natural language.
[81] Cypher is the query language for a graph database.
[85] When a user asks a question in natural language,
[88] the LLM will generate the Cypher query
[90] to extract that information from the knowledge graph.
[94] The Cypher query then gets executed on the database and the results are returned to the LLM.
[100] The last step is for the LLM to interpret the results of the Cypher query
[105] in the context of the natural language question
[108] and return a natural language response.
[112] For this example, we'll need an API key and project ID.
[116] The link to this notebook is in the description below.
[119] In the notebook, you'll find instructions for retrieving these credentials.
[125] We'll be using Neo4j, an open-source graph database.
[129] But any graph database can be used to create the knowledge graph.
[133] We'll create a local instance of the database
 using a containerization tool.
[138] I'll be using Podman,
[139] but you can use any containerization tool.
[142] For example, Docker,
[143] as long as it allows you to create a Neo4j instance.
[147] If you don't have a containerization tool already,
[149] take a moment to install one.
[154] After installing, initialize and start a machine.
[159] My machine's already initialized, so I'm just starting it here.
[170] Once you have this running,
[172] you can start a database instance
[175] with this configuration.
[177] We need credentials to access the database.
[180] So, I'm setting a name and password here.
[182] We also need to include the APOC library as a plugin
[186] in order to enable additional functionality 
for working with data and graphs.
[192] It looks like our graph database is up and running now.
[198] It's a good practice to create a fresh 
virtual environment for this project.
[202] I'm using Python 3.11.3 here.
[206] In the Python environment for your notebook,
 install the following Python libraries.
[213] We'll be using the OS and getpass modules to set up credentials.
[217] We'll use LangChain's document class 
to store the text for input into our graph database
[223] and the LLM graph transformer to create a graph from our text input.
[229] To interact with and query the graph database, 
we'll use the LangChain Neo4j module
[235] and it's accompanying
[236] GraphCypherQAChain class.
[239] To craft our prompts for the LLM,
[241] we'll use LangChain's prompt template
[244] and FewShotPromptTemplate.
[247] We'll use the LangChain IBM and IBM watsonx.ai
[252] modules
[252] to interact with the LLM and to set the parameters for our models.
[260] We'll need to set up our credentials using the API key 
and project ID that we retrieved earlier.
[266] We'll also need to set the URL from which we'll access these services.
[271] Now that our environment is set up, 
we can create the knowledge graph.
[275] First, we need to create a connection to the
 local database instance that we started earlier.
[281] Next, we define our data for input into the knowledge graph.
[285] In this case,
[286] the text describes employees at a company,
[289] groups they work in
[290] and their job titles.
[292] We'll use this set of relationships to test the graph generating capabilities of the LLM.
[298] But you don't have to limit your data to straightforward examples of relationship data.
[303] GraphRAG systems have been shown to be successful
[305] in retrieval and summarization tasks 
for far more complex narrative and connected data.
[315] Now we'll configure our LLM,
[318] which will generate text describing the graph.
[320] The LLM temperature should be fairly low
[323] and the number of tokens high
[325] to encourage the model to generate as much detail as possible.
[329] without hallucinating entities or relationships that aren't present.
[336] One of the most powerful LLM use cases is transforming unstructured text data into structured data.
[343] The LLM will transform our text input string
[346] into a structure of nodes and relationships that we can use to populate the knowledge graph.
[353] The LLM graph transformer
[356] allows you to set the kinds of nodes and relationships you'd like the LLM to generate.
[361] Restricting the LLM
[363] to just those entities
[364] makes it more likely that you'll get a good representation of the knowledge in a graph.
[370] Given our text input,
[371] we set the allowed nodes to person, title and group.
[376] We also set the allowed relationships to
[379] title,
[380] collaborates and group.
[382] We use the document class to prepare 
our text to be added to the graph documents.
[388] The call to convert to graph documents
[391] generates text in a format that represents the entities in the graph.
[398] We can inspect this graph documents object
[401] to see how the LLM generated nodes and relationships from the text,
[405] representing the relevant context and relevant entities.
[414] Now that we have the data in the correct format,
[416] we can insert these nodes and edges into the graph database
[420] using the addGraphDocuments method.
[427] Once the graph data is created,
[429] we can visualize it using our browser.
[434] In order to query our graph database,
[437] we'll use Cypher queries.
[445] Cypher is, for a graph database, what SQL is for a relational database.
[449] Instead of operating on tables,
[451] Cypher queries operate on the nodes, relationships and paths in the graph database.
[458] To visualize the graph in the browser,
[460] I ran this query which shows us all 
the nodes and relationships in the graph.
[465] On a larger knowledge graph, this visualization might be too complex.
[469] But for our example, it works to verify the structure of the graph.
[474] It looks like the relationships in our input text have been correctly represented here in the knowledge graph.
[484] We can also examine the schema and data types in the database
[488] using the get schema property of the graph.
[492] Without the LLM,
[494] creating the knowledge graph might be a manual process to diagram entities and relationships from unstructured text.
[501] Now that we have our knowledge graph,
[503] we can query it,
[504] taking advantage of the graph structure 
and graph database retrieval capabilities
[509] to derive valuable information
[511] over the data
[512] in a more holistic way than semantic search can perform on a vector database.
[518] Now we'll use natural language to query the knowledge graph.
[522] The natural language query will be passed to the LLM,
[526] which is going to translate the query into Cypher syntax.
[530] This Cypher query will be executed on the database
[533] and the result will be returned to the LLM using natural language.
[537] Prompting the LLM correctly requires some prompt engineering.
[541] We'll think of the prompting step in two parts, 
so we'll need to set up two different prompts.
[546] The first prompt gives the LLM instructions 
for generating a correct Cypher query
[551] from the user's natural language query.
[554] LangChain provides a FewShotPromptTemplate
[558] that can be used to give examples to the LLM and the prompt,
[561] encouraging the LLM to write correct and succinct Cypher syntax.
[566] This code block gives several examples
[569] of questions and corresponding Cypher 
queries that the LLM should use as a guide.
[574] It also constrains the output of the model to only the query.
[578] An overly chatty LLM might add in extra information
[582] that would lead to invalid Cypher queries.
[586] Using a prefix with a specified task and instructions
[590] also helps to constrain the model behavior
[592] and makes it more likely that the LLM will output correct Cypher syntax.
[601] The second prompt provides the LLM instructions for translating the result of the Cypher query
[606] into natural language
[608] given the original natural language question from the user.
[611] We employ a few-shot prompting strategy here, too,
[615] providing examples to the LLM for how to do this.
[619] We call this prompt the QA prompt.
[621] Essentially,
[622] it describes how the LLM should answer the question with the information returned from the graph database.
[632] Now we'll bundle together our Cypher prompt, our QA prompt,
[636] our knowledge graph
[637] and an LLM to create the question answering chain,
[640] using the graph Cypher QA chain class.
[644] We're implementing a simple retrieval procedure here.
[647] But there are ways to improve on this strategy 
by providing additional context to the LLM
[652] about groupings and summaries 
of like nodes within the knowledge graph.
[658] Using a temperature of zero and a length penalty
[661] encourages the LLM to keep the Cypher prompt short and straightforward.
[665] If you're wondering why we're configuring a different LLM here,
[669] it's because we're setting different parameters for retrieval of information from the graph
[674] than we used earlier for constructing the graph.
[676] Now we can query the data by invoking the chain with a natural language question.
[681] If you try this out, your responses may be slightly different than what we're seeing here
[686] because LLMs are not strictly deterministic.
[689] Here's our first question.
[692] What is John's title?
[694] We can see the Cypher query generated by this LLM
[697] to retrieve the information,
[699] the result of the Cypher query
[701] and the natural language response from the LLM
[704] as Director of the Digital Marketing Group.
[707] Looks good.
[709] Let's try a slightly more complex question.
[712] Who does John collaborate with?
[715] Again, the LLM generates a Cypher query to retrieve the correct information from the graph database
[721] and returns the correct response.
[724] John collaborates with Jane.
[726] This looks good.
[728] Let's ask the chain about a group relationship.
[731] What group is Jane in?
[734] Jane is in the executive group. Okay.
[737] Let's try one more that requires the LLM to give us two outputs.
[742] Who does Jane collaborate with?
[745] Jane collaborates with Sharon and John.
[748] Even for this more difficult query,
[750] we can see the chain correctly identifies both of the collaborators.
[754] Beyond retrieving the simple titles and relationships from our input string in this example,
[760] GraphRAG can summarize and retrieve contextual information
[764] over the whole structure of the knowledge graph.
[766] So, how is this different from a VectorRAG system?
[770] Firstly, instead of calculating embeddings and storing the resulting embedded information in a vector database,
[777] a GraphRAG system transforms unstructured text data
[781] into structured data
[782] using an LLM.
[784] And a knowledge graph is populated with this data.
[788] The second difference is in the retrieval step.
[790] Instead of performing semantic search 
and returning results with semantic similarity,
[796] the LLM generates a Cypher query 
in response to the user's natural language query,
[801] which gets executed on the graph database 
containing the knowledge graph.
[806] The GraphRAG system avoids one of the limitations of VectorRAG.
[810] If you think about the way VectorRAG returns top semantic search results to a query,
[815] you can recognize that VectorRAG can't provide the LLM with knowledge over the whole text corpus in response to one query.
[823] It's limited to the top semantic search results.
[827] GraphRAG can leverage graph indexes,
[830] which store summaries about groupings of like nodes
[833] to provide summarization over the whole 
corpus of text within one query result.
[839] In practice, you may want both the capabilities of retrieval from a semantic search on a vector database
[845] and a graph search over a knowledge graph.
[848] It's possible to build these sort of HybridRAG systems 
using both vector databases and graph databases.
[855] Check out the GitHub link in the 
description below to try out GraphRAG for yourself.
