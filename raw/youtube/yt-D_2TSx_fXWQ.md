---
schema_version: 1
id: yt-D_2TSx_fXWQ
type: youtube
title: 'G-RAG: Knowledge Expansion in Material Science | Muslims in ML at NeurIPS''24'
url: https://www.youtube.com/watch?v=D_2TSx_fXWQ
authors:
- Muslims In ML
ingested_at: '2026-06-17T20:57:32Z'
content_hash: sha256:c2d9f08a890fd0c02f66c570992f3d92055301735d9b1e305f4a8552ea055b8b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Muslims In ML
  channel_url: https://www.youtube.com/@MuslimsInML
  duration_seconds: 532
  caption_track: fetched
  snippet_count: 176
filter:
  score: 0.7
---
[1] hello everyone it's an honor to be here
[4] at new 2024 Muslims and AML Workshop
[7] presenting our titled work J knowledge
[12] expansion in Material Science this work
[14] has been accepted to the third Muslims
[17] inal workshop collocated with new
[21] 2024 Material Science is a field that
[25] relies heavily on precise and upto-date
[27] information for Innovation however
[30] when we look at the tools available
[32] today particularly in llm field where we
[36] can integrate the uh retrieval or
[38] generation which also known as rag we
[42] see in uh we see significant limitations
[45] these models can retrieve outdated or
[47] irrelevant specially information
[50] struggled with hallucination and fail to
[53] provide sufficient interpretability
[55] especially in our
[58] domain our goal with this research was
[60] to overcome these challenges by
[63] leveraging the strength of graph
[65] databases and improving retrieval
[67] accuracy and contextual understanding
[70] and that's what to the Leed of to the
[73] development of
[76] G okay let's start by understanding the
[79] problem we uh set up to solve current
[82] Rec approaches while powerful rely
[85] heavily on unstructured knowledge pieces
[87] and simple retrieval Pipelines
[90] although there are many advancements
[92] right now happening in the rack uh field
[96] but still uh there is a lack of having a
[101] proper pipeline this limits their
[104] ability to provide reliable contextually
[107] relevant answers particularly when
[108] dealing with extensive specializ stents
[111] like uh we have right now in material
[114] size for example traditional systems May
[117] return a mix of relevant and marginally
[120] useful information diluting the quality
[123] of the response we identified this Gap
[126] and realized the potential integrating
[129] of graph based approaches to enhance
[131] both the retrieval and generation
[136] processes our proposed solution is a
[139] graph enhanced retrieve augmented
[141] generation system designed specifically
[144] to tackle these issues the core idea is
[148] simple instead of relying solely on text
[151] juns we employ a graph database to store
[155] entities um here we are uh making the
[159] term as mat IDs and their relationships
[163] these entities are extracted from
[165] Material s documents through advanced
[167] entity linking and relation extraction
[170] techniques the graph structure allows us
[173] to capture the reach semantic
[175] relationships between entities enabling
[178] more precise and context our retrieval
[181] our defining features of G is the
[184] integration of external knowledge
[186] space especially uh for this part we are
[190] using Wikipedia here's how it works
[193] after passing a document we identify key
[196] entities such as material properties
[198] compositions and experimental results
[201] using our span person Modio these
[203] entities are then used as queries to
[207] retrieve additional information from the
[209] wi knowledge
[212] Bas by tapping into the Wikipedia's fast
[215] and continuously updated repository we
[218] enreach the graph database with
[219] contextually relevant data these steps
[223] ensure that the system is not
[225] constrained by Static nature of internal
[229] uh data remains Dynamic and
[237] comprehensive our pipeline begins with
[240] PDF puring a critical step in Material
[242] Science where data comes in diverse
[245] formats including text figures and
[247] tables we utilized Advanced tools like
[251] uh visual instruct model for figures and
[254] Microsoft stable transformer for table
[257] data this ensures that all relevant
[259] information is pursed accurately for
[261] Downstream
[263] St we also introduced some agents to
[267] validate that our puring is happening
[270] very perfectly or
[277] sucessfully so here is the overall um
[281] methods of how we are passing all the
[284] PDF PowerPoint and all the text file and
[287] then also figures and tables and then
[290] all the chunking and then operating all
[295] using agents and then validating the
[298] process
[303] here the spam procor identifies key
[306] entities and the Bist processor
[308] integrates these entities into a
[310] coherent graph structure by connecting
[313] their entities with their semantic
[315] relationships supplementing them with
[317] Wikipedia derived knowledge the graph
[320] database forms a foundation for highly
[322] targeted information
[326] retrieval the span parser is the initial
[328] component of JX system designed to
[331] extract relevant entities and
[333] relationships by comparing semantic
[336] similarities it encores both the current
[338] knowledge base and external passage such
[341] as Wikipedia into high dimensional
[344] embeddings the similarity between the
[346] query and external passage is computed
[349] using a do prod
[350] embeds the module ranks and the
[353] retrieves the most relevant passages
[356] ensuring precise and Target de
[358] information retrieval for down
[360] stream
[367] T the passage processor processes the
[370] retrieved passages alongside the
[372] existing knowledge space combining them
[374] with structured input sequences it uses
[377] transform models to generate contextual
[379] embeding and identify relance SP within
[382] the combined data by calculating
[385] probabilities for start and end tokens
[388] of this pans the module accurate text
[392] segmentation this facilitates robust
[395] entity linking relationship extraction
[398] and integration of knowledge external
[400] knowledge into the
[407] system uh here is also the retrieval
[410] process from the graph database where we
[413] are using uh also the llm and here we
[417] are using the Lama in index for the all
[421] the
[428] processes what says Z AP is ability to
[432] balance the accuracy faithfulness and
[434] relevancy Al like traditional existem
[437] that struggle with limited context
[439] Windows J ensures the most critical
[441] notes and
[442] relationships Ur from the cph database
[446] this gives the information concise and
[448] relevant even with the token con of for
[453] instance when retrieving the yeld
[456] strength of material at specific
[458] temperatures G doesn't provide numbers
[461] it contextualize these values with the
[463] information about grain size thermal
[466] effects and
[467] compositions this is invaluable in
[470] material set where Precision is
[478] Paramount so G we designed a data set of
[482] 10 domain specific queries covering
[484] complex material science topics our
[486] experiments compared with NRE graph and
[489] G on mates like quietness faithfulness
[493] and relevancy the results Were Striking
[496] G improved quietness on scores by 60%
[500] compared to the knif Ron demonstrated
[502] Superior context Lancy for example in a
[505] query about the year strength of an aloy
[508] G provide create contextual responses
[511] that closely with the ground data this
[514] level of precision highlights the
[516] transformation potential of graph
[518] enhanced appoes particularly with the
[521] added dep of wikip
[525] integration so that's our presentation
[529] thank you all
