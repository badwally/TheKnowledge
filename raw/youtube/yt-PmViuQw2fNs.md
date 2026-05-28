---
schema_version: 1
id: yt-PmViuQw2fNs
type: youtube
title: 'Automating MEDDIC: How to Flag Missing Decision Makers in HubSpot'
url: https://www.youtube.com/watch?v=PmViuQw2fNs
authors:
- HubSpot Excellence
ingested_at: '2026-05-28T14:04:49Z'
content_hash: sha256:0885119087104b06d78b0454df90dfb6e6fa72392ea95f4d2e6ed1d48550099d
domains:
- orita-cmo
nlm_corpus_ids:
- adc34eb9-c798-4530-8b0d-4b166a0bc38a
wiki_pages:
- wiki/concepts/meddic.md
- wiki/concepts/economic-buyer.md
- wiki/concepts/hubspot-association-labels.md
- wiki/concepts/hubspot-segments.md
- wiki/concepts/hubspot-deal-tags.md
- wiki/entities/hubspot-excellence.md
- wiki/entities/jasper.md
meta:
  channel: HubSpot Excellence
  channel_url: https://www.youtube.com/@HubSpotExcellence
  duration_seconds: 462
  caption_track: fetched
  snippet_count: 202
filter:
  score: 0.7
---
[0] We've all seen it happen. Reps will tell
[2] us that a deal is about to close and
[4] they haven't even spoken to the person
[6] who's actually signing the check. Today,
[9] I'm showing you how to implement Medic,
[11] the sales qualification framework into
[13] HubSpot to automatically flag any deals
[16] that are missing the economic buyer. My
[19] name is Jasper. I'm a certified HubSpot
[21] consultant and I help businesses with
[23] things like this. Let me share my screen
[25] and show you exactly how this works. So
[27] when we're in HubSpot, the first thing
[29] we want to do is we want to set up our
[32] association labels. To do this, it
[34] actually recently moved. We'll go to
[36] data management on the left hand side
[39] and then we'll go to data model. Here
[41] we'll click on edit data model in the
[43] top right and then we go to
[45] associations. We'll scroll down to deals
[48] and this will show us all of the deal
[50] associations we have. So all of the
[52] objects are linked to deals. Before we
[55] move any further, um, let me also
[57] clarify that this is when you have a
[60] professional or enterprise license for
[62] HubSpot. This does not work for starter
[65] licenses. So, what we're looking at
[67] specifically here is the association
[69] between deals and contacts. And when we
[71] click here, we can see that right now we
[73] do not have any labels implemented right
[76] there. So, we're going to create three
[78] different labels here. And the first one
[80] that I'm going to create, and by the
[82] way, we have like two options to do
[83] this. We have the single labels and a
[85] pair of labels. In this case, we're
[87] going to keep it simple and we're going
[89] to go for the single labels. So the
[91] first one is going to be the economic
[93] buyer.
[95] We're going to click on next. Then we do
[97] have the option to put limits on this.
[99] So by default it will say many contacts
[102] can have that label and many deals can
[103] have that label. If you want to limit
[105] that and say we only have one economic
[108] buyer for each deal, maybe that's part
[111] of the process at your organization. We
[113] can set it up here. Right now, I'm going
[115] to leave it on many. We're going to
[117] create this label. And we're going to do
[118] the same thing for our champion.
[122] And then we'll also do the same thing
[124] for blocker in this case.
[128] All right. So, this is the first part.
[130] We have our association labels. Now, the
[132] next thing we want to do is create some
[134] logic behind this. I do want to keep
[136] things simple. So what I want to do is
[139] create a tag that will automatically
[142] show on deals where the economic buyer
[144] is missing. So to do that the first
[147] thing we will do is we'll go to our CRM
[150] and then segments. And here we're going
[152] to create a segment for deals. And this
[156] is going to be any deals. And then we're
[159] going to look at associations. So we're
[161] associated contacts. And this is where
[164] we're just going to look at the record
[166] ID. So basically what I'm going to say
[167] here is that if the record ID is known,
[170] so this means that any deals who are
[172] associated to a contact will be part of
[174] this list. Now we're going to change
[176] this to economic buyer. And if
[178] everything is right, because we just
[180] created an association label, this list
[182] should come up empty. So here we'll just
[185] say admin deals with an economic buyer.
[194] We're going to save this list as an
[195] active list, so it automatically stays
[197] up to date. So, this list will have any
[200] deals that have an economic buyer
[202] attached to it. Now, before we turn this
[204] into a visual alert on our sales
[206] pipeline, if you want more architectural
[209] tips like this, make sure to like this
[211] video, subscribe to the channel for more
[214] HubSpot excellence. And if you would
[216] like a written SOP for this entire
[219] workflow, make sure to sign up for my
[221] brand new newsletter, HubSpot
[222] Excellence, down in the description, and
[225] I'll send the SOP to you for free. Now,
[227] let's get into the visual part. The next
[229] thing we're going to do is we're going
[230] to go to our deals pipeline. And what
[232] we'll see here is that it looks fairly
[235] normal. It doesn't have a lot of visual
[236] elements. It has the lead scoring on
[238] some of them, but that's about it. When
[240] we click on settings, if we do this from
[241] deals, we will land in the right place
[243] right away. But you need to go to data
[246] management objects and then deals. And
[248] then here we're going to go to
[250] pipelines. And then under pipelines,
[252] we're going to go to deal tags. So here
[254] we'll click on manage deal tags. If you
[257] want to do this for a specific pipeline,
[258] you can select that here. Otherwise,
[260] we're just going to go to create from
[263] scratch. And we need a name for this.
[266] So, let's give this deal tag a name at
[269] economic buyer. Um, so this way it
[272] becomes actionable. Um, the way that
[274] people will see this, this is a very
[276] important thing. So, we're going to make
[277] this red. We wanted this to show up in
[280] all pipelines. So, I'm going to leave
[282] that. And then for the description, this
[283] is also an important one. the
[285] description will actually show up
[287] whenever somebody hovers over that tag.
[290] So, we can say economic buyer is
[293] missing. Make sure to add one. Then for
[296] our filters, this is where the segment
[299] comes into play. We'll go for admin
[301] deals with an economic buyer and we'll
[304] say is not a member of this segment. So,
[307] we're going to review this tag. We'll
[309] see what it will look like. And this tag
[311] will show up for anyone who's not part
[313] of that list. So any deal that doesn't
[315] have an economic buyer. We're going to
[316] save this. And now we're going to go
[318] back to our deals pipeline. And I
[321] probably need to wait for a moment until
[323] this shows up everywhere. So as you can
[325] see, all of the deals now show that we
[327] do not have an economic buyer. So the
[330] next thing we want to do now is we want
[332] to check for one of these deals and add
[334] the economic buyer. So we'll go to this
[337] deal right here. And this is also how
[339] you apply those association labels in
[341] the process. So this will become part of
[343] the SOP at your organization. So when
[346] sales is working on a deal, they have
[348] some contact that they're working with
[349] for that specific deal. And you can see
[352] at association label here with that
[354] contact. And we're going to say that
[355] Logan Roy in this case is the economic
[358] buyer. So now when we go back to our
[360] deal pipeline and we wait for a moment
[363] and we refresh, now we can see that the
[366] label has disappeared from this deal.
[368] Now, of course, in an ideal world, most
[371] of these deals would not have this
[373] label, which makes sure that any deals
[375] that do have the label really stand out.
[378] So, the next time you're having a
[379] conversation with one of your sales
[381] reps, instead of going through every
[382] single deal and asking if we have
[385] everyone, you can basically point to any
[387] of these red tags that are on the deals
[390] and be like, why do we not have an
[392] economic buyer yet for this specific
[394] deal? This changes the conversation and
[397] makes it more clear in the system that
[399] the process is being followed and we
[401] actually do have our medic qualification
[405] before we move the deal forward. We can
[408] of course add some additional things
[409] here, but I'll leave those for another
[411] video. For example, we could also
[413] automatically check if the economic
[415] buyer has been identified at a certain
[417] stage. So for example, if a deal gets to
[420] presentation scheduled, but we do not
[422] know the economic buyer yet, we can send
[424] an alert to the sales rep, but for
[426] example, also send an alert to the sales
[430] manager as well, so that we can fix this
[432] before the deal moves forward. Now,
[434] setting up these labels is easy, but
[437] getting your team to actually use a
[439] methodology like medic can be quite
[442] hard. If your portal is technically
[444] messy or your sales team is ignoring
[447] your process, reach out to me. I help
[449] organizations reach HubSpot excellence
[452] and you can book a time with me in the
[454] description of the video down below. My
[456] name is Jasper, a certified HubSpot
[458] consultant, and I'll see you in the next
[459] video. White.
