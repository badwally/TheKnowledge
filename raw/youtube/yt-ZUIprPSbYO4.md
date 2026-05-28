---
schema_version: 1
id: yt-ZUIprPSbYO4
type: youtube
title: Automate Your HubSpot CRM with Claude Code 🤖
url: https://www.youtube.com/watch?v=ZUIprPSbYO4
authors:
- SyntaxGTM (Tom Granot)
ingested_at: '2026-05-28T04:05:19Z'
content_hash: sha256:85084aa36063ffd8e5950136d95acf206d686468c752c04e3bacd704d2588296
domains:
- orita-cmo
nlm_corpus_ids:
- adc34eb9-c798-4530-8b0d-4b166a0bc38a
wiki_pages:
- wiki/entities/hubspot.md
- wiki/entities/claude-code.md
- wiki/concepts/hubspot-data-hygiene.md
- wiki/entities/breeze.md
- wiki/entities/tom-granot.md
- wiki/entities/hubspot-admin-skills.md
- wiki/concepts/plan-before-execute-after.md
- wiki/concepts/icp-tiering.md
meta:
  channel: SyntaxGTM (Tom Granot)
  channel_url: https://www.youtube.com/@SyntaxGTM
  duration_seconds: 902
  caption_track: fetched
  snippet_count: 459
filter:
  score: 0.75
---
[0] So, this video is a bit different than
[1] the things I usually do. This is about
[3] HubSpot. So, uh
[4] you know, it's not really PMM work to do
[6] HubSpot.
[7] I have, however, worked for startups for
[9] so long that HubSpot became second
[11] nature, and as a developer, I was always
[12] trying to find, you know, scripts and
[14] tricks and various ways, you know, to
[15] make my work easier. Specifically now
[17] with Cloud Code, we came to a point
[19] where we can actually work with the API
[20] directly from within Cloud Code. Also,
[22] at the same time,
[23] HubSpot released like two or three
[25] different things which we will review
[27] today that help you work with AI inside
[29] of HubSpot. However, they all have their
[31] limitations. At the end of the day, the
[32] best way to work within HubSpot right
[34] now using AI is using an external tool
[37] that creates either API calls or CLIs
[40] for you for various use cases. And that
[43] is what we're going to focus on today. I
[44] actually built a very, very large
[46] repository of HubSpot admin tools, and
[48] we're also going to focus generally on
[50] the process. So, when you work with
[51] customer or your own CRM data, you have
[54] to be very meticulous. This is very
[55] expensive, very hard to get data. We
[58] don't want to mess anything up. So,
[59] that's what we're going to focus on
[60] today. Uh let's get started. So, the
[62] immediate thing you're going to get when
[64] you're looking for HubSpot AI is Breeze.
[65] Breeze is the new um HubSpot AI
[68] incarnation. Um what Breeze actually has
[71] is this little AI assistant on the side,
[74] which enables you to get
[76] uh you know, ask it specific things and
[78] get back specific answers. It also has
[80] growth I'm sorry, it also has agents,
[82] which are essentially um workflows that
[85] you can use with like with Breeze inside
[88] of HubSpot. Um if you ever worked with
[90] the Operations Hub inside of HubSpot,
[92] you have a bunch of these manual things
[94] that you can do, like automatically
[96] trigger them, sorry, manually trigger on
[98] automations using uh Operations Hub.
[101] This is similar, except they're ongoing
[103] agents that continuously do the work. Of
[105] course, they are priced to the teeth,
[107] and most companies don't need them going
[109] on a constant basis, just
[111] once in a while.
[113] Um also, HubSpot now has this credits
[115] system. Um I don't know if they even
[117] mention it in the website, but there is
[119] now in this new credit system, which you
[122] probably somewhere here. Uh
[125] I don't even know where where they show
[127] it, but they actually have credits now,
[129] which you use when you use various
[131] aspects of the platform with AI. So, for
[135] me, Breeze was great, and there's things
[137] you can do with it, especially querying
[139] information. But anything that required
[140] write, so actually changing up
[142] information, was difficult to do, plan,
[145] and audit in advance. So, of course, I
[146] went to the HubSpot MCP server and
[148] thought, "Well, the HubSpot MCP server
[150] must have capabilities to write
[152] properly." Well,
[156] no.
[157] Uh MCP server only supports read only
[159] access. So, you know,
[161] no. Okay, fine. So, there must be a CLI
[164] or something that I can use for that.
[165] There is. It's only for developers and
[167] things that, you know, require
[169] development around the CMS and pages and
[171] stuff like that. So, that's irrelevant.
[172] So, I went back to the trusted API
[175] reference review overview and started
[177] building scripts. Uh this ended up with
[180] this mega repo of HubSpot admin skills
[183] for Cloud Code, which we will go over
[184] today. First and foremost, I want to
[186] talk to you a little bit about the the
[188] way I actually do my work. So, I do it
[191] in four stages. First and foremost, I
[194] plan it out. And the way it works is I
[196] have like a specific planning skill that
[198] will tell me, "Okay, what do you want to
[199] do? All right, here are the API
[201] reference endpoints that we want to do.
[202] Here are the scripts. Here's the retry
[204] logic. Here's everything that I need to
[205] do to make sure that and whenever I do
[208] like an atomic operation, whenever I
[209] actually do something with HubSpot, I
[211] can revert it back, or at the very
[214] least, I can know what happened, so I
[215] can do a manual
[217] uh
[217] action in the platform to roll it back.
[219] So, you plan, then you make a before
[221] script, which essentially queries the
[223] data. I could have used HubSpot MCP
[225] here. However, I chose to stay
[227] completely with script generation,
[229] mostly to make sure that even if it
[231] takes more time initially to generate
[234] the script per the customer's response,
[236] we are not bound by the tools that the
[237] MCP supports. We can instead create our
[240] own API API calls very specifically, by
[243] the way, with things that are not
[245] necessarily inside of the MCP. Like
[247] sometimes I would like to go and have
[249] the script go to an external resource,
[251] fetch something, and come back. The MCP
[253] will only work with the HubSpot instance
[254] that you have in front of you. So, the
[257] before script essentially checks, "Hey,
[259] what's the situation? Tell me what the
[261] current properties, contacts, companies
[263] that I'm working with, how they look
[264] like." And then uh
[266] to to to kind of understand the before
[267] state, and then the execute actually
[269] executes the scripts and runs it and
[271] fixes everything along the way that
[272] breaks. Then the after part verifies the
[274] fix, and I think that's the most
[276] important part. Sometimes, the system at
[278] the end of the process doesn't
[279] immediately adhere to the state that we
[281] want it to be. For example, a lot of
[283] times when you do stuff that involves
[284] scoring or that involves uh updating a
[287] lot of different contacts, you want to
[289] do it via a workflow. Uh my stuff will
[292] help you build the workflow, but the run
[295] of the workflow is on HubSpot systems.
[297] It can take 4 hours for a workflow to
[299] propagate through 100,000 contacts,
[301] right? So, the after script is actually
[305] meant for checking,
[306] "Are we expecting this to be completed
[308] immediately? If not, what's the expected
[310] completion time?" And like I mentioned,
[312] to come back. In practice, what I did
[314] was I used the task management software,
[316] and I built um for every skill, I built
[318] a ticket. And then every time that I
[319] planned, I added a comment. And I be the
[321] before, I added a comment with the
[323] status. I executed, I added a comment. I
[324] after, I added a comment. And I only
[325] completed when the after part of it
[327] succeeded. Um now,
[329] in addition to that, I also have these
[331] routines which I added to the system,
[333] which are a cleanup routine every week
[335] that you want to run manually, not
[336] automatically, and a quarterly database
[338] cleanup, which is a more involved, let's
[340] say it takes an hour or two to actually
[341] get through once a quarter. Let's talk a
[344] little bit about the skills that I have.
[345] First and foremost, there's a HubSpot
[346] audit that looks at the portal, checks
[348] the situation, and makes
[349] recommendations. This is a very
[351] important process because it might come
[354] up with stuff that are not covered from
[356] with the skills inside of this repo.
[358] This is actually excellent because at
[359] the end of the day, I gave them
[361] a way I gave everyone a way to add their
[364] own skills based on what they made
[366] internally in HubSpot
[368] to the repo, so everyone can enjoy it.
[370] Everything is, of course, anonymized,
[371] cleaned up. We're not getting any
[373] private information in. But it would be
[376] a very interesting case to get people
[378] who have, you know, HubSpot instances
[379] running for years and having very
[381] specific problems, it would be cool if
[383] once the app the audit explores them and
[385] understands them, we will basically
[387] create a skill based on that. That would
[389] be awesome and like super community
[391] driven. Uh I'm not sure that's actually
[393] going to happen. People are afraid of
[394] the, you know, working with their
[395] instances, but I do, you know, want to
[397] help. Anyways, once I finish the audit,
[399] I actually create a HubSpot
[400] implementation plan based on the audit
[402] to actually make it work. By the way,
[404] this has a presentation add-on that I
[406] have internally based on the customer
[408] that I work with, where I actually
[410] generate a PowerPoint that I can show in
[412] the meeting telling them, "Hey, this is
[414] the audit results. This is the
[415] implementation plan. Let's get to it."
[417] Um so, that's the initial stuff.
[419] Database hygiene. There are a few things
[421] that you need to do that are just,
[426] you know,
[427] just easy. You probably should not have
[429] any contact with that email to them. You
[430] should probably not send me messages to
[432] anybody who had a hard bounce. And then
[434] there are more complicated things that I
[436] do. For example, ghost contacts. So,
[439] imagine you have a contact that had no
[441] activity since the since it was added 5
[443] years ago to the CRM.
[445] In practice, I don't want to talk to
[447] that contact. I want don't want to hold
[448] it as a marketing contact. It's not
[449] relevant to me anymore. But if it was
[451] set before as a marketing contact, it's
[452] probably
[454] going to stay there. Uh so, this
[455] suppresses them. Uh we also I also have
[457] like stuff with owners, yada yada. A lot
[459] of data enrichment stuff, which
[461] essentially cross-references company and
[463] contact data and makes enrichments from
[465] them. Then I have my proud and joy,
[467] which are the ICP tiers. Essentially, it
[470] will ask this skill will ask the user
[472] questions on what the ICP is, then look
[474] at the property list inside of HubSpot
[476] and make a decision on what's the best
[477] way to actually uh create the ICP tiers,
[481] then build the lead scoring mechanism
[482] using the actual uh HubSpot's
[485] uh new score feature with like fit and
[487] engagement and combine, and then
[489] actually build smart lists that I can go
[490] into the platform and look at uh
[493] based on those ICP tiers. There's also a
[495] lot of like automation workflows,
[496] hygiene, yada yada. And then [snorts]
[498] the ongoing maintenance, which just
[499] makes sure that all the properties
[501] inside of your
[502] uh inside of your system actually work.
[504] Uh I think I want to go into one of
[506] those skills just to give you a sense of
[507] how it looks like. Uh and the skill I
[509] wanted to, you know, go into is to
[511] creating ICP tiers. And I want to walk
[513] you through a little bit of what the
[514] skill and the scripts look like, just to
[516] make sure you understand the logical
[517] flow. So, in the skill,
[520] what I'm actually doing is I'm saying,
[522] uh I will create this ICP classification
[525] flow. There are prerequisites. The nice
[527] thing about the prerequisite section,
[528] which every skill has, is that before in
[531] the before section, where it will try to
[533] actually, sorry, in the plan section,
[534] where it will when it will try to
[536] actually plan for this, it will look at
[538] the prerequisites and say, "Hmm, do I
[541] have the prerequisites or not?" Because
[543] not all of the time you are the super
[545] admin of the instance that you're a part
[547] of. So, it will basically check whether
[549] you can have all of these access, which
[550] is very cool. And then it will gather
[552] requirements across
[554] uh across multiple different
[556] uh nuances. Uh for example, it will
[558] check whether
[560] people match or don't match your ICP,
[562] what employee count ranges define define
[564] your tiers. And these will be questions,
[566] again, that will be proactively asked
[568] with the user with the ask user
[569] interview feature inside of Cloud Code.
[571] Um now, before you do that, you look at
[575] the definition of the ICPs, you audit
[577] the current state with the actual
[578] scripts that allow enable you to to
[580] audit them, you create the ICP tier
[582] property inside of HubSpot, and then you
[584] build them classification workflows. And
[586] here comes another interesting bit that
[588] I encountered when I worked with these
[590] things. So,
[591] in practice, building a workflow using a
[594] workflows API is hella unstable. It's
[596] very, very hard to reliably ask HubSpot
[599] to create a workflow using the API and
[600] have it created. This is for a good
[602] reason.
[603] I think that API is relatively new and
[606] also unstable on purpose because it
[608] benefits the company to make the
[611] the workflow API unstable
[613] because they want you to work inside the
[615] platform to create workflows. If you
[616] never have to go into the platform
[618] again, why would you? And I think they
[619] understood that. Also, Breeze the AI
[622] doesn't know how to create complicated
[625] workflows or to edit existing workflows.
[627] I know this because I tried to do many
[629] different things that for example,
[631] looking for unknowns and stuff like
[632] that. Their immediate comment inside of
[634] Breeze is they're saying stuff like it's
[636] not supposed because it can cause
[638] infinite loops and stuff like that.
[639] Also, there's no edit functionality. So,
[641] you can only create new workflows from
[643] scratch, which is problematic if you
[644] have existing workflows that you want to
[646] edit. Anyways, at the end of the day, I
[649] decided that I will build this manual UI
[652] build instructions and then I will put
[654] them inside of my Anthropic
[657] extension.
[658] And I'm just going to let Claude do it.
[660] Or sometimes, because we now have Chrome
[663] usage inside of Claude Code, I let the
[665] browser use features inside of Claude
[667] Code to do it. In any case, it will
[669] check out all the different
[671] possibilities and it will based on the
[673] actual it might ask you to go put it
[676] into Breeze and see the answer back. But
[678] in any case, it does know of all the
[680] different options that you can have to
[681] make workflows happen. Then there's a
[683] bunch of specifications here and then
[685] there's the after state, which is us
[686] checking, "Hmm, can we actually say that
[689] this has been implemented?" Cool,
[691] there's a checklist which it needs to
[692] definitely check that everything
[694] happened. And then a lot of different
[696] learnings that we had based on this.
[698] Now,
[699] I want to talk about the learnings a
[700] little bit. Um one of the interesting
[703] things that I learned via
[706] via the process is
[709] I taught
[710] essentially, I taught the HubSpot
[713] workflow how
[717] to learn
[719] what to look for. I guess that's not the
[720] best way to put it. But I taught the
[722] HubSpot the HubSpot workflow the HubSpot
[725] sorry, skill
[726] what is
[728] technically possible and not technically
[730] possible actually running it over and
[732] over and over and over again until I
[733] reach something that, you know, made a
[735] lot of sense. I feel like to me, a
[738] concrete issue is whether
[744] Cut this. Before I let you go, one final
[746] thing. I want to give you an example of
[747] an actual before script. This is a
[749] Python script I use I use UV, which is
[751] like a new Python runner thingy that
[753] enables you to actually run and like
[755] scaffold a project properly. It's a
[757] replacement displacement of it replaces
[759] pip, I think. And like virtual end and a
[762] bunch of other, you know, more older
[763] Python tooling. It's very fast and it
[765] just makes things very very quick. So, I
[768] I use Python mainly because of that. So,
[770] essentially what the script does it
[772] configures itself and then it defines
[773] some helpers and then what it it does in
[775] practice is and you'll note a lot of the
[777] printing here. It runs and it prints a
[779] lot of information which then Claude
[781] Claude Code can use to summarize in the
[783] actual end result. The reason why I do
[786] why I have so many prints is because
[788] this is running inside of Claude Code.
[790] So, I never actually look at all of
[792] those prints, but I need the I need
[794] Claude Code to know what happened in
[796] each stage of the way and the prints are
[797] a deterministic, you know, one and done
[800] thing telling me, "Hey, this is the
[801] status. This has happened." And then
[803] Claude reads through the whole thing and
[805] then ends up coming back with a great
[808] notion of what happened. Um
[810] So, this is kind of how the the the
[812] actual scripts look like. I think this
[814] is it. I don't have a lot more I want to
[815] go into.
[817] Um
[818] yeah, let's summarize. I think maybe the
[819] most interesting thing about this video
[821] doesn't have anything to do with the
[822] HubSpot at all. It's about the way these
[824] skills were built. So, I work a lot on
[826] many different things at any given point
[828] in time. We all do. And when I want to
[830] improve on something, usually what I do
[831] is I just I do it again. I learn from
[833] resources. I go and update process that
[836] I work in my own like personal, you
[837] know, standard standard operating
[839] procedure in my mind. I think one of the
[841] core things that I learned from this
[843] experience is the most interesting
[845] things for skills are the things you
[846] never write down. It's the things that
[848] you have kept in your mind that are the
[850] little technical limitations because
[852] you've hit an API endpoint that you can
[853] access
[854] a specific use case and stuff like that.
[857] It's all like super hard to to work on.
[860] I think one of the best things for you
[861] to do and there's many different types
[863] of processes that do that for you. And
[866] we'll talk about some of them like
[867] entire and other, you know, intent-based
[869] workflows later on. But try and keep a
[871] running log of the limitations you've
[873] hit. I think the limitations you've hit
[875] are the really interesting bits that
[876] create great skills because it will
[878] allow a skill once already, you know,
[882] created once, it will allow it to update
[885] itself with new information as you
[887] personally as a human do the work
[889] yourself. And I haven't quite cracked
[891] how to do that yet for all of my skills,
[892] but it's slowly improving. Um
[895] So, yeah. Thank you so much.
[897] Uh and I hope you enjoyed it. And let me
[899] know if there's other skills you want to
[900] learn.
