---
schema_version: 1
id: yt-cnYdCVi-MjM
type: youtube
title: 'Text-to-SQL is dead: The next generation of querying is Agentic'
url: https://www.youtube.com/watch?v=cnYdCVi-MjM
authors:
- Weaviate vector database
ingested_at: '2026-06-17T20:57:39Z'
content_hash: sha256:e07c5b790c047eb1b304cd6b44538ad3e3000ff173e3d58f606446b8d502dc5b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Weaviate vector database
  channel_url: https://www.youtube.com/@Weaviate
  duration_seconds: 214
  caption_track: fetched
  snippet_count: 108
filter:
  score: 0.7
---
[0] the true power of large language models
[2] is starting to be discovered their
[4] ability to take natural language inputs
[6] and make decisions on how to interact
[8] with external tools like databases to
[10] perform tasks but which models work best
[13] as agents the researchers in this paper
[15] are exploring how a type of agenta
[17] querying function calling is moving
[19] beyond traditional methods they done a
[21] comprehensive analysis of loads of
[23] different models and even created a new
[24] data set to test them we'll get to the
[26] results in a second but first let's talk
[28] about something else they proposed to
[30] even the playing fields traditionally if
[31] you wanted Advanced database querying
[33] with an AI model you'd probably try text
[35] tosql the model takes a natural language
[37] question and translates it into a SQL
[39] query but this approach has a couple of
[41] problems SQL dialects can vary across
[43] databases and the models can also
[45] struggle with real world complexities
[47] like filtering and aggregation and
[48] search this paper proposes a different
[50] approach function calling instead of
[52] generating raw SQL the llm structures
[55] its queries using predefined function
[56] calls in adjacent format with optional
[59] Arguments for search filter aggregation
[61] and grouping in a full system it would
[62] look something like this a query comes
[64] in from the user and is passed to our
[66] llm based on the user's input the LM
[68] outputs Json that can be used to query
[70] the database everything from what text
[72] to use whether it's aggregation or
[73] search query and additional arguments
[75] like filters or grouping the llm passes
[77] that to the search system which then
[79] performs the search and Returns the
[80] results so let's take a look at example
[82] a user asks how many menu items are
[84] priced under $20 in a function calling
[86] setup the model would generate something
[88] like this this method solves a major ISS
[90] issue in text to sequel adaptability
[92] with this Json structure there's no need
[94] for the model to understand sequel
[95] syntax or specific database structures
[98] and it can be translated to any other
[100] query language the same logic applies to
[102] more complex queries like irations or
[104] filtering across multiple properties but
[106] can models even create Advanced queries
[108] like this for example the query what is
[110] the average price of seasonal specialty
[112] menu items under $20 grouped by whether
[114] they are vegetarian or not requires a
[116] compination of a search query for
[118] seasonal Specialties a price filter
[120] agregation to compute the average price
[123] and a group by operation to categorize
[125] results by vegetarian status so to
[127] evaluate whether models could handle
[129] these types of advanced queries the
[130] researchers created DB gorilla this data
[133] set includes five distinct use cases
[135] each with three collections like
[136] restaurants menus and reservations 315
[139] test queries covering different
[141] combinations of filters search
[142] aggregation and grouping and a synthetic
[145] database schema designed to test real
[146] world use cases using this data set the
[148] study tested eight different l stems
[150] from five different families the best
[152] performing models were claw 3.5 Sonic
[154] GPT 40 mini GPT 40 and Gemini 1.5 Pro
[158] these models successfully created and
[159] formatted structured queries with high
[161] accuracy lower performing models like
[163] Gemini 2.0 Flash and llama 3.18 billion
[166] struggled a lot more with getting all
[167] parts of the query correct another key
[169] finding was schema adaptability GPT 40
[172] demonstrated the most consistent
[173] performance across different database
[175] schemas while smaller models showed
[177] significant variance one major issue
[179] observed was that some models completely
[181] skip function calls when they shouldn't
[183] have Gemini 2.0 flash for example failed
[185] to issue queries 54% of the time which
[188] significantly lowered the performance
[189] knowing the best models and having a
[191] language agnostic way of quaring
[193] databases is going to allow us to kick
[195] off a lot more advanced agentic apps we
[197] still have a ways to go until they can
[199] be completely autonomous assistance
[201] however these sorts of purpose build
[202] agents are going to be the next big bang
[204] of AI applications and I'm so excited to
[207] see what will happen next till the next
[209] one and as always all the resources are
[211] linked in the description
