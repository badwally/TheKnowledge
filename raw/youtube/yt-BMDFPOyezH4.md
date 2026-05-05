---
id: yt-BMDFPOyezH4
type: youtube
title: 'A2A vs MCP: AI Agent Communication Explained'
url: https://www.youtube.com/watch?v=BMDFPOyezH4
authors:
- IBM Technology
ingested_at: '2026-04-30T17:28:29Z'
content_hash: sha256:f8779c658e1f1781fb726b53a4f85eb99e4037c6ef24acfb3cb344a041f519f9
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: IBM Technology
  channel_url: https://www.youtube.com/@IBMTechnology
  duration_seconds: 693
  caption_track: fetched
  snippet_count: 94
---
[0] By themselves, AI agents are kind of isolated. 
Yeah. Right. They can reason by themselves. They
[9] can generate stuff by themselves. But how does 
one agent talk to another agent or talk to your
[18] existing infrastructure? That's where it can get 
messy. Lots of custom integrations to things like
[25] data stores or code bases. Yeah. Yeah. And look, 
the the industry knows this is a problem. So,
[33] naturally, we got protocols. A2A, MCP. Maybe 
you've seen these acronyms floating around.
[42] And maybe you're wondering how they can be used 
to help agents and which one you're supposed to
[47] use. Well, look, I'm a bit of an advocate for 
MCP, so I'll take that one. But first, Anna,
[54] convince me why I need A2A in my life. If you're 
doing anything with multi-agent orchestration,
[60] you should absolutely consider A2A Martin. 
A2A is short for agent to agent protocol. So
[67] essentially siloed agents can communicate and 
work together regardless of differing vendors
[73] or frameworks. Okay. So whether you or 
I or somebody else built the agents,
[79] does that mean they can they can still work 
together? Exactly. It's an open protocol
[84] that defines how AI agents can exchange messages 
and task requests between each other. And these
[93] messages can be requests, responses, and even 
negotiation or coordination steps. All right,
[99] fair enough. But but how do these agents know how 
to collaborate with the other agents here? Like,
[107] do they have a digital name tag or something? 
Actually, yeah, kind of. With A2A, agents use
[114] something called an agent card. Essentially, a 
standardized descriptor to advertise what they can
[120] do. Okay. An agent card. That's a a fancy name for 
a resume. Yeah, exactly. Other agents can discover
[130] these cards dynamically and figure out what 
skills or services are offered and decide, hey,
[136] you do that, I'll do this. and pass tasks back and 
forth. Okay, that's that's pretty elegant, but but
[143] my agent here, it still needs to talk to my to my 
database. So, is A2A .. A2A going to do that for me?
[150] It's not really what A2A is for. All right. Noted. 
We'll we'll come back to you, Mr. Database. Um,
[157] but another question for you. So, if I've got a 
variety of different agents and they use different
[163] modalities. So let's say this agent here, this is 
primarily a text modality agent. Maybe this one
[171] primarily works with images. Can they understand 
each other or would it be like us trying to
[179] speak two different languages? So that's actually 
another plus of using A2A. Once discovered, agents
[186] can send structured messages or task requests to 
each other. And these exchanges in in information
[192] are modality agnostic, meaning agents can swap 
images, files, structured data, not just text. And
[201] if you have one agent generate a design mockup, 
another agent can review it, and another can uh
[208] be a client approval agent. All part of the same 
flow. All right. And then how do these two agents,
[214] you got this arrow here, how do they communicate? 
What's the the transport layer? It's just plain
[218] old HTTP. So any existing web server, API gateway, 
or infrastructure that speaks HTTP can host an A2A
[228] agent just like a normal web service. But 
the magic is really in the data format and
[234] communication style. And whenever I hear the word 
magic in text, it's usually followed by a bunch of
[240] acronyms. Indeed, it is. And here's one for you. 
A2A uses JSON RPC 2.0 for request and response
[250] payloads. That means agent to agent communication 
happens via structured JSON which is language
[257] agnostic and widely supported. Nice. So you're 
getting the benefits of web infrastructure like
[262] I guess routing, security layers, load balancing, 
logging, that sort of stuff. And because A2A is
[268] building on standard HTTP and the magic of JSON 
RPC, it integrates easily with existing backend
[277] stacks. I'll admit the transport layer story is 
pretty clean. Starting to come around. I mean, I'm
[285] listening. I'm listening. Well, how about this? 
A2A isn't just for quick call and response tasks.
[292] You'll like this one, Martin. For long running jobs 
or workflows where agents need to send progressive
[298] updates, A2A supports streaming updates via 
server sent events. That means one agent can
[305] push status updates and partial results to another 
in near real time. Meaning that remote agents can
[312] send back intermediary progress while they work. 
This live streamed progress updates, which seems
[320] useful. Just useful, Martin. very useful. But but 
that still leaves the question of how a single
[327] agent gets context which conveniently is what MCP 
handles. Convenient indeed. All right, convince
[335] me. It'll be my pleasure. So A2A handles agent to 
agent communication. But what happens when we've
[344] just got a standalone individual agent that needs 
access to external data or tools? Well, MCP is
[356] what happens at least if you want to provide a way 
that access is done in a standardized way. And MCP
[364] is model context protocol? Model context protocol. 
Giving a single agent the context it needs to
[371] actually do useful work. And that might be work 
like pulling a file out of a file system. It might
[380] be work like interacting with an existing code 
repository. It might be something like writing
[388] to a database. Well, Martin, couldn't I just 
write code to do all these things? Yeah, you sure
[394] could. And you'd be writing it again and again 
because you'd have to write it every time you
[400] swap models or every time you swap tools. Okay, I 
I'm listening. All right. So, look, MCP creates a
[407] layer and that layer is where the AI agent doesn't 
need to know the specifics about how to interact
[413] with any of these resources here. There's a a 
really simple infrastructure around this. Ah,
[419] I sense some boxes and lines are incoming. Yeah, 
you do. Okay. So, we've got uh first box is an
[426] MCP host. Uh this is the AI application where the 
agent actually runs. And then below that we've got
[435] the actual MCP server. And the MCP server knows 
how to communicate to these resources like the
[444] file system or the code repo or the database. But 
it does so while presenting a uniform interface to
[450] the agent. A uniform interface how exactly? Like 
if my agent wants to retrieve a file from the
[457] file system or wants to edit a line of code in the 
repo, what does it do? Yeah, it it uses primitives
[464] that are exposed by this guy, the MCP server. 
So there's a bunch. You've got tools. Now, these
[471] functions are things that the model can invoke. 
So it could be a tool to, for example, search the
[477] database or commit something to the code repo. 
Uh there are also resources and these are things
[484] that the model can read like files or database 
records or maybe maybe live application state.
[492] And then the third primitive are prompts. So these 
are basically pre-built templates that help the
[499] model interact and that serve more efficiency. 
Okay. So the agent doesn't need to know how the
[505] database is implemented or which API works best 
with the local file system. It just kind of passes
[512] the request to the primitives exposed by the MCP 
server and it handles translation. That makes a
[519] lot of sense. Well, thank you. Well, in theory 
at least. But in practice, how does the MCP host
[526] communicate with the MCP server? Yeah. Okay. So 
like A2A the message format is JSON RPC but
[536] the transport actually that depends it depends 
on where the server lives. So for local servers
[542] that are running on the the same machine let's 
say like maybe a an IDE plugin that's accessing
[550] your local file system. Well it uses just standard 
input output for that. But if we are talking about
[556] something that is you know not on your machine a 
remote server that is a different kettle of fish
[563] instead that uses HTTP with its streaming support. 
Okay. So you write an MCP server once let's say
[572] for a CRM system and any MCP compatible host 
can use it. And what happens when you bring in
[579] a new model or a new application? Yeah it doesn't 
doesn't matter. you're you're not rebuilding the
[585] integration every time. Just reuse the same MCP 
server. And because it's open, there are a ton
[593] of pre-made MCP servers. There's an MCP server for 
all sorts of file systems, for Slack, for GitHub,
[599] for databases, and so on. So, I think we've both 
made our case for why A2A and MCP can be useful.
[607] So how about we consider a scenario where both A2A 
and MCP can be used together. Right? So perhaps
[619] let's do an example of a a retail store. So we 
have got our own inventory agent here and that
[628] inventory agent is going to use MCP to interact 
with some databases. So, it's going to use that
[638] to store and retrieve information about perhaps 
products, uh, about stock levels as well. And
[644] if the inventory agent detects products low in 
stock, it notifies an internal order agent, which
[653] then communicates with external supplier agents. 
So, maybe you have one or maybe you have two or
[662] even more. So that's a pretty nice solution. 
So you're saying I really do need MCP. Yeah,
[670] you do need MCP, but like you're showing here, 
you do also need A2A. So A2A for agents talking
[677] to agents and MCP for agents talking to tools and 
data. Yeah, it turns out we weren't competing.
[686] We were complementing. Wow. Did you just make 
interoperability sound heartwarming? Hey, maybe I did.
