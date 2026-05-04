---
id: yt-CQywdSdi5iA
type: youtube
title: The Model Context Protocol (MCP)
url: https://www.youtube.com/watch?v=CQywdSdi5iA
authors:
- Anthropic
ingested_at: '2026-04-30T17:28:31Z'
content_hash: sha256:4bbead1f8c16c2d2d8db4a92ecf15b38f31c6c65bd74d90e911ed50ff0e7ffd3
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Anthropic
  channel_url: https://www.youtube.com/@anthropic-ai
  duration_seconds: 1171
  caption_track: fetched
  snippet_count: 489
---
[0] - Around the time, like in September,
[1] we had like an internal hackathon,
[3] and everyone was free to build
[5] basically whatever we wanted to build.
[7] But it turns out everyone
just built an MCP,
[9] and it was-
- It was crazy.
[11] Like everyone's ideas were,
[13] "Oh, but what if we made
this an MCP server?"
[18] - Hey, I'm Alex.
[19] I lead Claude Relations here at Anthropic.
[22] - Hi, I'm Theo, I'm a
product manager on MCP.
[24] - Hey, I'm David, member of
technical staff at Anthropic
[27] and one of the co-creators of MCP.
[29] - Today we're gonna be talking
[30] about the Model Context Protocol
[31] and diving in deep into
what it is and what's next.
[35] Thank you both for coming on.
[37] Very excited to talk about MCP,
[38] but first there's a lot of talk about MCP
[43] and not a lot of maybe
real deep understanding
[46] of what it is.
[47] Can we dive into how you view MCP
[50] and like what it really means
[52] to be using MCP or building on it?
[55] - MCP is just a way for, you know,
[58] putting my workflow into
like an AI applications
[61] in a very simple way.
[62] I think that's how I really
wanted it to be initially,
[64] or that's how we want it to be,
[66] but it's just a way to give context
[68] to an application that uses an LLM.
[71] And that's just as simple as that.
[72] And that can be, you know, tools,
[75] it can be just raw context,
whatever you like it to be.
[78] - How is that different
than you calling an API
[81] or something like that?
[82] It's passing this
information from one place
[85] into the prompt basically of the model.
[87] What makes MCP special here?
[89] - I think the question is
what do models interact with?
[93] And they don't interact
directly with APIs.
[94] They interact with prompts
and tools and you know,
[99] whatever you're giving
the model to ingest.
[102] And so MCP standardizes how
you take that data from,
[107] whether it's an API or
some internal data source
[109] or whatever it is, how you take that data
[111] and then actually give it to the model.
[113] - So, this is a protocol then.
[114] So it's defining that sort
of interaction pattern.
[117] What are the main aspects of this protocol
[118] that like you have, that has to follow?
[122] - The main part is that it's a protocol
[124] between the AI application
that uses an LLM,
[126] and it exposes like
basically three main thing.
[129] It's tools, it's a set,
a thing called resources,
[133] which is just raw data
that you could like ingest
[135] into a RAG pipeline or
whatever you want it to do,
[138] and there's prompts.
[139] And that's the three main things
[140] that a server can expose for now, yeah.
[142] - So tools are like actions
[145] that the model can take out in the world.
[148] Resources could be files, texts.
[152] - Files, data, whatever kind of context
[156] you wanna give the model.
[158] - And then prompts are?
[160] - Just like what a user wants
to put into the context window
[165] by themself and just like
triggered by the user
[168] and just put into the context window,
[170] and then they can edit it as they want to.
[171] That's really what prompts are for,
[172] like prompt templates
at the end of the day.
[174] - Prompt templates, I see.
[175] So literally defining the prompt itself.
[177] - We typically see that being implemented
[179] as a slash command.
[180] - Oh, okay, I see.
[182] So if you're in the AI
application of your choice,
[185] you would do a slash command,
[186] and it pull in the prompt template.
[187] - Exactly.
- Save you time
[188] from having to write
that out, whatever it is.
[190] Okay, that's MCP at its most basic form.
[193] There's definitely a
lot of nuance in there.
[195] What was the origin of all this?
[196] Like how did this come about?
[197] - The origin I think is like,
[199] the most basic thing is that,
[201] that I worked on like
internal developer stuff,
[204] and I got very quickly frustrated
[206] about like having to copy things
[209] in and out of Claude desktop
[210] and then copying things back
and forth between my IDE,
[213] and that's just really what
I would thinking about,
[215] like how can I solve copy
and pasting the things
[218] I care about the most between
these two applications.
[221] And that's really the absolute
origin of where MCP started,
[225] at least in my mind.
[226] And then from there, I
explained that to Justin,
[229] who's the other co-creator,
[231] and he really took it and ran it.
[233] And then we together, just build it out
[236] and build into Claude desktop.
[237] And I think there was a pivotal
moment that you alluded to.
[239] Do you wanna talk about the hack week?
[242] - I feel like you should take the story.
[244] - Okay, yeah, hack week was fun.
[246] We weren't really sure,
is this gonna work?
[250] And, but at the round the time,
[252] like in September we had
like an internal hackathon,
[254] and everyone was free
[256] to build basically whatever
they wanted to build.
[259] But it turns out everyone
just built an MCP,
[261] and it was-
- It was crazy.
[262] Like everyone's ideas were,
[264] "Oh, but what if we made
this an MCP server?"
[267] - Yeah, yeah.
[268] - And we had everything
from people, you know,
[270] doing, you know, very standard
things like Slack integration
[274] or things you would think
of when you think MCP
[276] up to like people
[277] who like steered their
3D printer with MCP.
[281] And I love this like when
it got into the real world,
[285] when like Claude got into the real world
[287] because of an MCP server.
[289] - What was it?
[290] Because I remember that too
when we were doing these,
[293] all these hackathon projects,
[294] and there was no mandate
to force people to use MCP.
[297] This was just like an
entirely organic thing.
[300] Why did people gravitate towards
MCP for all their projects?
[303] - I think it really was
that standardization layer
[305] just made it so much easier
[307] to add context to the application,
[309] because the moment that
Claude is now integrated
[314] against MCP, that means
as the server builder
[317] you can build 1 to 10, 20,
however many servers you want,
[321] and you know that it
will automatically work
[322] with that application.
[323] And so I think that just
gives you the ability
[326] to only think about one side
[327] and not have to think
about the other side.
[328] - I think there's a bit of a magic moment
[330] when you teach Claude something new
[333] using an MCP server for the first time,
[336] and you see it takes action
about something you care about.
[340] And I feel that's a little
bit of moment of magic
[343] that I think MCP captures really well,
[345] which makes people so excited,
[347] because within five minutes
there's something going.
[350] - Right, right, yeah, I've seen it myself,
[353] and I mean even experienced it
[354] where it almost feels like you take Claude
[357] out of the the box, so to speak.
[359] And all of a sudden,
[361] instead of just being this thing
[362] that is just right there outputting text,
[365] it's doing other things,
[367] it's calling other applications,
fetching on their data,
[369] or even like operating a 3D printer,
[372] which is a really crazy thing.
[374] And that does feel really special.
[376] And I guess MCP allows that
[378] pretty seamlessly to some degree.
[380] So this was back in end
of summer, early fall,
[384] as we were doing these hack
week and these other things.
[388] When did we launch MCP, and
what did that look like?
[391] - We launched MCP around Thanksgiving.
[393] - Yeah, November.
- 2024.
[396] - And how was that launch?
[398] What was the reception?
[399] - Slow at first.
[400] I think everyone's response
is, as you can imagine,
[404] well, some people still have
this response is, what's MCP?
[406] - Right?
- Mm-hmm.
[407] - We, naming is hard.
[408] We definitely could have named it better.
[412] - It's arguable now, it's
kind of caught its storm.
[415] - I know.
- That's fair.
[417] But you still get the
like MPC instead of MCP,
[421] and then it makes me
think NPC, and you know?
[423] - Yeah, acronyms are hard.
[425] - But, yeah, acronyms are hard.
[426] But you had a lot of
people asking what is MCP,
[430] not just externally, but
I also think internally,
[433] because it was such a bottoms up movement.
[436] You know, initially people were like,
[437] oh, what is this thing?
[438] What does it mean to ask or
to give the model context?
[442] And then as people started
playing around with it
[444] and seeing it for themselves,
[445] I think that's where it
actually slowly caught steam.
[448] And the turning point was
[449] when more and more clients
kind of started adopting.
[454] So I think the IDEs were
the first to adopt.
[457] More recently we've seen a lot
[458] of adoption from model providers,
[459] and that's kind of created
a lot of kind of waves
[462] in the market to incentivize
a lot more server providers
[466] to actually build servers.
[467] - I think one of that part is like you see
[469] so many times on like social
media, like what is MCP?
[474] Why would I ever want this?
[475] And then like a month
later, a few days later,
[477] they're gonna be like, this
is the best thing ever,
[480] have so many of these
stories, and it's so funny.
[482] - Yeah, so it's now become,
I think it's fair to say
[486] like industry standard of
like integration protocol.
[490] I mean, there's nothing else in my mind
[491] that kind of rivals it,
[493] but I think like going back to the launch,
[495] a key decision here was to
actually make this open source.
[500] And that was pretty different
[503] in comparison to maybe previous efforts
[505] in this area that had been launched.
[508] Can you explain the reasoning
behind that decision
[509] and why did we open source it?
[512] - Yeah, if you have a closed
ecosystem for integrations
[517] and for a context to be
provided to AI applications,
[521] then a isn't clear to the,
you know, server builders
[527] or the integration builders, you know,
[530] is that AI application
gonna be around forever?
[531] Should they invest in that?
[533] Which ones should they invest in?
[536] And so by making it an open standard,
[538] you really kind of decrease the friction
[541] to even building those integrations.
[542] And we believe that the value
[546] of building an AI application
is not necessarily
[548] which integrations you have access to,
[550] but the model's intelligence
[552] and the workflow that you
build on top of the model.
[554] So we wanted to focus the
industry on those two things
[556] and not necessarily on
building integrations.
[558] - That makes sense.
[559] And there also seems potentially
like with open source,
[562] there's this kind of
cycle you can get into
[564] where somebody contributes to a server
[567] and then like somebody uses
it and they notice bugs in it
[570] and then they're like, oh,
I can just go fix it myself.
[572] And that maybe speeds it all up.
[574] - There's another part to that is Justin
[576] and I just like open source.
[578] - Hey, sometimes it's the simplest thing.
[580] - Yeah.
- Yeah.
[581] So now we have, you know,
[584] lots of companies adopting
MCP into their own products.
[586] We have lots of other developers
[589] and companies creating servers
to be able to use all these
[593] or to be plugged into all these clients.
[596] What does this look like
across the industry now?
[599] What's like the current state of MCP?
[601] - The current state is that
we have major players adopt it
[604] across like their products.
[606] We have a really big ecosystem
of MCP server builders.
[610] It's like 10,000-plus.
[612] And it's like at this
interesting intersection
[614] that initially was like
mostly focused on developers
[617] and a very local experience
[619] where the servers would run local
[620] and the software they
use it would run local.
[623] And I think we have this inflection point
[624] where we're starting to see
[628] these servers being
hosted like in the cloud,
[632] like as a web thing through
what we call remote MCP,
[636] and a Claude AI integrations is like
[638] really the first big entry to that
[640] that allows you to connect
just like a website,
[643] like that offers an MCP server
[645] into your day-to-day Claude AI workflow.
[647] And I feel this is like a pivotal moment
[649] where it can be like a
true standard for the web
[652] for how like LLMs interact with that.
[654] I think that's to see what
this is gonna work out.
[657] But yeah, I think that's
where we're currently at,
[659] and we do of course have
[662] a increasingly bigger community
being built around us,
[665] and this is like big companies,
[667] but it's also like sometimes
just open source people
[668] who just like working on MCP,
[671] and that's just becoming bigger.
[672] - The craziest thing is someone
fixed our docs this morning
[676] 'cause we had a image
that was out of date,
[678] and they just submitted the PR, we accept.
[679] - That's why you want
to do it open source.
[681] - Yeah, that's, I love that.
[682] - I love that the community gets behind it
[683] and they also feel ownership
[685] and wanting to maintain it as well.
[687] And it seems like, I mean,
[688] we were chatting about this
before we started filming,
[692] there's a lot of things
happening in the MCP world too
[695] outside of just like
working on the protocol.
[697] What's going on in your
world these days with MCP?
[701] - Yeah, it has a lot, right?
[702] There's conferences on MCP.
[706] There's just like a lot of conversation.
[708] There's like partnerships where
we work with like, you know,
[712] big companies on like
evolution of the specification
[715] and what their problems are.
[716] I learned a lot about like
enterprise deployments
[718] and the needs for identity
[720] and authorization in that
space over the last few months
[723] and had like help from
some of the best people
[726] in the world around this.
[727] And that's just like a
little bit of that world
[730] of MCP at the moment.
[731] - That's awesome.
[732] Yeah, I'm just like blown
away by like the response,
[736] and like I'm starting to
see now online of posts
[740] around like is this what it looks like
[742] to witness like the birth
of like a new protocol?
[744] Is this like what it was like to be around
[745] for HTTP or something like that?
[748] How would you guys
liken those comparisons?
[751] Like is this a new protocol of that sense,
[753] or how can we expect to
frame this in comparison
[756] to things we've seen in the past?
[758] - I mean, I would hope so.
[759] None of us can see the future.
[761] You know, knock on wood
[762] that we've landed on the right thing.
[763] But I think that's where the
community can help guide us.
[768] The hope is that we have
hit on the right problem
[772] of providing context to LLMs
[774] and that we have thought far enough ahead
[778] that all the right
building blocks are there,
[779] and the community can help
guide us as we're evolving it
[783] into kind of the next few steps.
[786] - I think from my perspective,
[788] we just need to build something
that people want to use
[791] and build this together with
people who care about this.
[794] And I think like you don't
need to compare it to HTP
[796] or anything else, it's just like,
[797] just make something
that people want to use,
[799] and that's in the end of the day.
[800] - So if I'm a developer,
[803] and I'm new to MCP, and
I wanna become involved,
[806] and I also wanna learn a little bit
[807] about how to work with MCP,
[809] do you have any tips for this person?
[812] - I think the first thing
that I would do is go look
[817] at an existing server that is online.
[821] Go play around with it, see
how it works with Claude AI,
[826] or Claude desktop if you wanna
play around with local MCPs.
[830] But just get a feel
[831] for what that interaction
pattern is first,
[833] and that will make it much easier
[835] for you to then build your own MCP.
[837] And start with the classic,
you know, hello world.
[839] Just do one tool, just
respond with, "Hello world."
[843] Do the same thing for you
know, prompts, resources.
[847] Just try the very basic thing for each
[849] before you go into anything more complex.
[851] And I think once people
get a feel for that,
[853] they realize how easy it is.
[854] - Yeah, I would certainly
just start local,
[856] just whip out Claude Code
[858] and just write code like an MCP server
[860] and just go from there.
[861] I think that works
actually surprisingly well,
[863] with like 10 minutes
you can have something,
[865] and then yes, what Theo said,
[866] just like look at great
servers and what they do
[869] and make the modification from there.
[871] - Yeah, it's funny you say that.
[872] I was experimenting the other day
[874] with just getting the docs
Model Context Protocol, the IO,
[878] pasting it into Claude Code,
and then like make me a server.
[883] And I didn't even have to like
[885] paste in the content or anything.
[886] Claude Code went, grabbed it, fetched it,
[888] brought it in, made the server.
[890] It was like a very easy
example right there
[893] of just how quickly you can get started
[895] with some of these things,
[896] especially when you've Claude
under the hood powering it.
[899] Any favorite MCP servers
[900] that you guys have seen
out in the world so far?
[904] - I really like those MCP servers
[905] that bridge the gap to
like the real world.
[908] Like I'm a person who likes music,
[910] and I have synthesizers at home,
[911] and there's an MCP server
that someone created
[914] to like create basically like,
[916] control their like synthesizer.
[919] And I just love that.
[920] It's just like,
[921] here's Claude interacting
with a physical device
[923] that later makes music, and
that's just so cool in my mind.
[926] I love those, and I
love the creative ones.
[928] I love the ones where people
play around with Blender.
[931] I love the quirky ones.
[932] Like one of our team members
has Claude control his door
[937] through like an MCP server
and like role-play a doorman,
[941] and it's just like I love that creativity.
[943] - I mean really with that,
[944] it's like the possibilities are endless.
[945] Anything that you could ping
through an API or anything,
[948] you could wrap in an MCP server
[950] and then control it with
Claude or another LLM.
[954] And the Blender one, explain that.
[958] So somebody was actually using Claude
[960] to control Blender just through MCP?
[963] - Yeah, basically is just like
[964] the MCP server just writes like
Blender scripts into Blender
[968] and you see in, you know,
there's lots of videos.
[970] You should check it out.
[971] It is like you just see
Claude calling these tools,
[974] and on the side Blender
just creates like a scene
[978] out of nowhere, and it's
actually just not the person.
[980] It's Claude creating it, and I love it.
[982] - That's awesome, I love that.
[984] Let's switch gears a little bit.
[986] So we just recently released Claude 4,
[989] so Opus and the new Sonnet.
[991] What does this enable for MCP,
[993] and how does this connect
into this broader theme
[996] we're seeing around agents and AIs
[999] that can kind of operate
on longer time horizons?
[1002] - As we get into models
with more intelligence,
[1005] it can do longer running tasks,
[1006] I think some of the primitives
that we've actually built
[1009] into MCP are going to become more used
[1011] that right now may not have
gotten as much adoption.
[1014] So, you know, things
related to statefulness,
[1019] things related to actually doing sampling,
[1022] but those are the primitives
that we thought about
[1024] in the beginning that actually
help in an agent's world,
[1027] but do require the models to
have the amount of intelligence
[1030] where they can kind of start
doing longer running tasks.
[1032] - That's interesting.
[1033] So some of these things that
maybe haven't been utilized
[1035] so much just yet will become
more and more important
[1039] because the models just get more capable,
[1041] and they're able to use 'em.
[1042] - It also just makes it probably easier
[1044] to like put more MCP
servers, like attach it,
[1047] and Claude is just gonna
get better and better
[1049] at like distinguishing which one it needs
[1052] to make to take action.
[1054] - How many MCP servers can
you throw at Claude at once?
[1059] How does it know how
to choose between them?
[1061] - Depends.
- Good question.
[1062] - It depends because it
depends on, you know,
[1065] how are the tools written,
are they overlapping?
[1067] If you put like three
issue tracker MCP servers
[1070] next to each other, of course
the model can get confused,
[1073] but if it's like, you know,
an issue tracker thing
[1075] and I don't know, something
completely different,
[1078] like I don't, you know, whatever,
[1080] and I think then it becomes,
you know, pretty easy,
[1083] then you can put a lot
of it next to each other.
[1085] Just a matter of like of your workflow
[1087] and how overlapping they
are on the end of the day.
[1089] - I see.
[1090] And I'm assuming as models get
more capable and intelligent,
[1094] it becomes like you can throw
more and more at them too.
[1096] So what's next for MCP?
[1099] - The protocol is now live.
[1100] There's good adoption,
but we can do a better job
[1103] of helping people understand what it is.
[1104] So we're definitely going to invest
[1106] in more examples, better documentation.
[1109] We're also investing in
key security primitives.
[1113] So the thing I think most people
are gonna be excited about
[1117] is agents and how we're
thinking about agents.
[1119] So for agents, one really big ship
[1123] that's coming is the registry API.
[1125] So that is going to allow models
[1127] to actually go and search
for additional servers
[1129] that they can then bring into the LLM.
[1134] That then allows kind of a little bit more
[1137] of an agentic loop
[1138] since the client doesn't
just get to decide, you know,
[1140] here are the 10 things that I am aware of
[1142] and that I want the
model to have context to.
[1144] The model can now go and search
for more things on demand.
[1147] The second is long running tasks.
[1149] So actually making it easy for you
[1152] to do longer running things with MCP.
[1155] And then the third one is elicitation.
[1157] So how do you as a server actually go back
[1161] and ask the user for more information
[1163] if you need more information.
[1165] - Exciting.
[1166] Well, I'm very excited to see
what the future holds for MCP.
[1169] And thank you both for coming on.
[1171] - Thank you.
