---
schema_version: 1
id: yt-6-OdjYdEpeU
type: youtube
title: 'RDF Data Shape Use Statistics: SHACL use on GitHub'
url: https://www.youtube.com/watch?v=6-OdjYdEpeU
authors:
- IDLabResearch
ingested_at: '2026-06-18T01:38:12Z'
content_hash: sha256:db931519ad28bc8171ee502d9341a9941d75d60c0ad4e5abddec8c11bc5184eb
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: IDLabResearch
  channel_url: https://www.youtube.com/@IDLabResearch
  duration_seconds: 419
  caption_track: cached
  snippet_count: 212
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:12Z'
  user_correction: null
---
[0] Intro
[0] hello my name is sen lieber from gent
[2] university
[3] id lab in belgium let's have a small
[6] talk about constraints in rdf
[8] expressed using so-called data shapes
[11] but let me first ask you a question
[14] would you write such a bike think about
[18] it
[18] we go back to this example at the end of
[20] the presentation
[22] by the way this presentation we first
[25] gonna talk about
[26] what constraints are why we want to
[28] investigate the use of constraints
[31] what we did to analyze them and how we
[33] did it and
[34] what we actually found and what this
[37] means for you
[39] so what are constraints when you want to
[39] Represent restrictions in a knowledge model "A bicycle has two wheels"
[42] represent real-world concepts
[44] in a machine-understandable knowledge
[46] model you also have to deal with
[48] restrictions
[49] so you might say that a bicycle has two
[52] wheels
[53] now using a knowledge representation
[55] language following the open world
[57] ascension
[58] something like showing this image is
[61] totally valid
[62] because you defined your world that
[63] bicycle has two wheels
[65] and literally the second wheel is
[68] somewhere there in the world
[70] but is this enough because we also want
[70] Use a knowledge representation A bicycle needs to have two wheels
[73] to use
[74] this knowledge representation so if we
[77] slightly modify this restriction
[79] and say that a bicycle needs to have two
[81] wheels
[82] we basically create a constraint which
[84] we can validate
[85] so we basically close our world and only
[88] consider bikes of this particular image
[90] now
[91] and validate which bike has two wheels
[94] has a certain color
[95] or a certain size and other things
[100] okay these are constraints but why do we
[102] want to investigate the use of
[104] constraints
[105] well the thing is that different
[105] Why investigate the use of constraints?
[107] constraint types exist
[109] so thinking about a knowledge graph with
[111] notes and properties
[112] you might want to constrain the
[114] cardinality of properties
[116] or the data type of their values or
[119] other more detailed restrictions on the
[121] values
[123] but if you use now tool to create and
[126] edit such constraints
[128] we might run into a small problem there
[130] because we can only use
[132] what the tool supports but if a tool
[135] only supports
[136] what is commonly used we run into the
[138] self-fulfilling
[139] prophecy whereas we only use what's
[142] supported
[143] and nothing else which is a problem
[147] so what did we do to analyze it and how
[149] did we do it
[149] What did we analyze? Currently no large data shape repository
[152] the thing is that right now there is no
[154] large
[155] scale data shape repository like
[158] thinking of
[158] linked open vocabularies for ontologies
[161] something like that does not yet exist
[163] for
[163] data shapes so what we did is that we
[166] looked into
[167] the shackle specification which is the
[169] shapes constraint language
[171] recommended by w3c because it already
[174] lists
[174] a lot of different constraint types and
[177] then we used the github search
[180] and looked for the term shackle in
[182] github repositories
[183] and selected 19 repositories containing
[186] shackle shapes
[187] which do not appear as just simple
[189] examples
[189] How did we analyze? Montolo Knowledge Graph
[192] and what we did then is we defined for
[195] each constraint type of the shutter
[196] specification like a definition
[199] in rdf using our montelor knowledge
[201] graph
[203] then we used a lot stats extension to
[206] extract statistics from the input in
[208] this case
[209] our github shackle shapes
[212] to create statistics about constraint
[214] type use
[216] which are described using our mental
[218] knowledge graph
[219] and you can find the statistics online
[222] here under this url
[224] and they basically look like this they
[226] are data cube and prof compliance
[227] statistics
[229] where we describe different observations
[231] whereas one observation
[234] for instance here describes one specific
[237] constraint type
[239] then the actual measure which was taken
[241] in this case the occurrence so how often
[243] this restriction type occurs
[246] and then also many other dimensions such
[248] as when this measurement was taken
[250] from which input it was taken and so on
[252] and so forth
[254] so the most interesting part now what
[256] did we find
[257] and what does this mean for you so we
[257] More than 60% of repositories define constraints for the basic structure of a knowledge Graph
[260] found
[261] that more than 60 of the 19 repositories
[265] define constraints for the basic
[267] structure of your knowledge graph
[269] so the cardinalities of properties the
[272] data types and classes of their values
[275] or even like the logical disjunctions
[278] like
[278] it has to be either data type a or class
[282] b or whatever and
[282] More than 30% of repositories define constraints on specific values; even less for other literal-based constrain
[285] more than 30 of the repositories so much
[288] less
[289] use more specific constraints to really
[292] constrain specific values
[294] or something like regular expressions on
[297] literal values and even less than 30
[300] percent
[301] use other literal based constraints or
[304] constraints regarding
[306] languages like english or for the labels
[308] for example
[308] What does it mean? Class, cardinality, datatype, nodekind and disjunction constraints seem to be obvious choices
[311] so what does it mean now it means that
[313] right now
[314] these kind of basic constraints for the
[316] basic structure seem to be the obvious
[318] choice
[319] classes data types and so on however
[322] they are much more constraints possible
[325] and for example defined in the chakra
[327] specification
[328] for a reason so there's much more
[331] potentials to also
[332] use them which are right now not used a
[334] lot
[336] it also means that the tools we use
[339] right now to create and edit such
[341] constraints should maybe put a little
[343] bit more
[344] attention to these less used constraint
[347] types
[348] to avoid a self-fulfilling prophecy
[350] where they only provide us with class
[352] and data type constraints
[354] which we then use in the end
[357] so in this small talk we looked into
[359] what constraints are
[361] basically closed world restrictions for
[363] validation
[364] we investigated the use of constraints
[367] to understand
[368] the use of different constraint types
[371] and we analyzed shuttle shapes from
[373] github
[374] using our montla framework
[377] and we actually found that constraints
[379] for the basic structure
[380] are used a lot and there's lots of
[382] unused potential
[384] for more detailed constraints and
[387] going back to our initial question of if
[389] you would ride such a bike
[391] well you see it's possible to ride a
[393] bike like that but
[394] you don't have to if you just define
[397] your constraints to find really bikes
[399] with two wheels
[401] which improves the quality of your
[402] knowledge graph
[404] and also for developers don't make it
[406] hard for users
[407] you should support all constraint types
[409] it should not be
[411] as a user not be harder to define for
[414] example a regular expression on a
[416] literal
[416] than just defining or constraining its
[419] data type
