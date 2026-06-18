---
schema_version: 1
id: yt-GWkk5AfRCpM
type: youtube
title: Basic Formal Ontology Tutorial (2025)
url: https://www.youtube.com/watch?v=GWkk5AfRCpM
authors:
- Barry Smith
ingested_at: '2026-06-17T19:26:34Z'
content_hash: sha256:7b0453ce0d42e208023829f8f5d7f7d49b194622eee4b4b3207319eadf5d6916
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Barry Smith
  channel_url: https://www.youtube.com/@BarrySmithOntology
  duration_seconds: 10477
  caption_track: fetched
  snippet_count: 2026
filter:
  score: 0.85
---
[7] I'll start with Dusan's questions, which are important because there have been lots of changes in BFO, but they're not changes in the content of BFO itself, which has remained very stable for twenty years, but rather in the surrounding support system that we've been building.
[28] Now we have a place where you can find what is current in BFO.
[36] That particular link contains links to what used to be current in BFO and to multiple other resources.
[44] We don't yet have the same resource for IOF, because IOF is still building the architecture for how it's going to document releases and so forth over time.
[56] But at some stage, there will be, we hope, a similar place where you can go to find out what is current in IOF.
[65] Now what's the difference?
[65] These are Dusan's questions, remember.
[67] What's the difference?
[69] So what's the difference between BFO and IOF?
[77] BFO is what we call a top-level ontology.
[77] That means it's an ontology which starts at the very top with very general terms like object, process, and so forth.
[79] Those terms then provide what you need to start writing definitions of more specific terms like factory or week or person.
[79] BFO is very small.
[80] It's used by hundreds of ontology project groups around the world.
[83] So what's the difference between BFO and IOF?
[87] So BFO is what we call a top level ontology.
[90] That means it's an ontology which starts at the very top with very general terms like object, process, and so forth.
[99] And those terms then yet then provide what you need to start writing definitions of more specific terms like factory or week or person.
[113] So BFO is very small.
[115] It's used by hundreds of, of ontology project groups around the world.
[122] Some 700 in the public domain that we've been able to track.
[126] Not all of those users use it properly.
[130] At some stage, we will find a way of correcting that by creating TikTok videos showing how BFO is to be used properly.
[141] That is not a joke, unfortunately.
[146] Then we have these people building domain ontologies.
[150] As we will see as we go along, it's a good idea if people build domain ontologies in suites of ontologies, which communicate with each other in such a way that you don't have one group building an ontology for sustainment of military materiel, for instance, and another group creating an ontology of military materiel, and they don't talk to each other.
[178] So the strategy that we developed is a strategy for creating suites of domain ontologies with BFO at the very top.
[188] Now what we've been doing for years is creating examples of how BFO is used in different domains, like the industry domain, which we're talking about at this meeting.
[202] It started around 2002, 2003 when I became involved with the groups of people around the world who were trying to make use of the new data which was unleashed by the Human Genome Project.
[218] People were building repositories of omics data, data in genomics, in proteomics, and all the dozens of other omics disciplines, and they were all collecting these data with different labels and different descriptions.
[234] As a lucky chance, I was involved with the leaders of the main ontology, which was trying to create some kind of harmony or consistency across all of these different repositories.
[251] They were, at the same time, attracting copycats who wanted to build their ontologies for their repository.
[262] These would be ontologies not of genomics or proteomics, but they would be ontologies of things like disease or population or pediatrics.
[275] So chaos was threatening.
[278] The chaos came about not because we had too many databases being built inconsistently across the world, but because we had too many ontologies being built inconsistently around the world, all trying to copy the success of the gene ontology, which is still the biggest and most successful ontology in the world.
[303] I decided that I would create a framework whereby we could understand what ontologies that were being built would indeed be consistent in their approach with the gene ontology so that you could use the ontologies together with the gene ontology, but have certain kinds of characteristics which would advance the possibility of having equal success in those other areas to the successes which have been achieved by the gene ontology.
[340] In working out from first principles what the best way to do those things would be, BFO was created.
[352] BFO is a reverse engineered version of the very top level of the gene ontology.
[360] It is a very general top level so the gene ontology consists of three ontologies.
[367] One ontology is the ontology of cell components where the gene is found.
[373] Another is the ontology of molecular functions, what the genes or the proteins do at that level.
[380] The third ontology was an ontology of biological processes, which includes everything from cell division to sexual mating behavior.
[389] I guess there is no other kind of mating behavior.
[393] So the BFO is based on three top-level terms measured by this standard: objects, cell components, functions, what molecules do, processes, what happens biologically when those molecules do their thing.
[411] This is illustrated in this picture here.
[414] You can see I'm only up to slide seven, and I've already spent seven minutes.
[418] With 200 slides, and that's because you keep interrupting me.
[426] So the three top levels of BFO are continuing, which means all of those things which continue, and occurrent, which means those things which happen, process it.
[437] Then there are two kinds of continuance, and this is the nearest we get to rocket science: dependent continuance, attributes in general, functions, qualities, dispositions, and so forth, and independent continuance, which means objects, planets, molecules, and everything in between.
[460] You can arrange the ontologies according to how they fit under these three categories, which are the basic categories of BFO, as we will see.
[470] Alright.
[471] We added further layers, further possibilities as new ontologies were not merely built, but received into what was now called the OBO Foundry, which was very much like the IO Foundry because the IO Foundry was built to be like the OBO Foundry.
[490] We added an ontology not for proteins or diseases, but for the experiments performed to identify the functions of proteins and so forth.
[502] That's OBI, which is the most of all the ontologies in the OBO Foundry. OBI is the most ambitious and the most logically coherent of the ontologies.
[513] It was built by people who cared a lot about logic.
[517] The very first work I did in the area of industrial manufacturing was on additive manufacturing, and I created, with people who know about additive manufacturing, an ontology of additive manufacturing based on OBI.
[534] I recommend that you look at OBI when you're thinking about manufacturing processes.
[540] Alright.
[541] We realized that we had nowhere in BFO to deal with information artifacts.
[548] So remember, we've been focusing on things like proteins and diseases.
[552] Information is a quite different thing, but that is the product of experiments.
[557] Experiments produce information, so we built the information artifact ontology.
[562] That was the only major change in BFO.
[565] We had to find a place for information, and we only had objects, attributes, and processes.
[573] Attributes meaning attributes of objects.
[576] We needed a place for information, and so that was BFO 1.1.
[582] Then we had BFO two, which was the new version which was created when OWL two appeared, so no changes in BFO.
[590] Now we have BFO twenty twenty, which apart from a few labeling changes and the dropping of one or two terms which had problems is the same as BFO two point zero.
[605] We have only had three versions in the course of twenty years' history.
[610] So.
[610] We became an ISO standard.
[613] That was something which was brought about by army intelligence, because they had been using ideas from the Oboe Foundry as the basis for a reorganization of the way they approach data.
[625] They realized that if they were going to be successful across the DOD, they needed to have an ISO standard, and so they made BFO into an ISO standard.
[637] Now we are recognized as a baseline standard for the DOD and the IC, and we are reaching a similar situation in the DHS where we have real successes.
[652] So.
[652] That is what it says here.
[655] This is BFO twenty twenty, which is what we have today.
[660] There is work going on behind the scenes to create BFO twenty twenty five or whatever we call it, but the official version is at the GitHub link that I gave to you earlier.
[675] Let us talk a little bit about the IOF.
[678] It was born in 2016.
[681] Hedi Khare was a postdoc working in Buffalo on ontologies.
[686] To my shame, I didn't talk to him very much.
[689] On almost the day he was leaving, he came to my office and said, Barry, why don't we start an industrial ontology founders group?
[698] I realized this man was a very important person, and he is now program manager for AI in the European Innovation Council, so other people recognize he's a very important person.
[713] He still plays in the background of IOF, but he's not an active member of our community, although who knows what might happen if we develop our European connections.
[725] So Europe is in some ways advanced beyond what we are aiming for here in the US.
[732] I can talk about that later if people are interested.
[735] So Hedi came to me.
[737] I said, This is a fantastic idea.
[738] What do we do next?
[740] And he said, Talk to Demetrius.
[742] Demetrius is a bourgeois de Lausanne, Greek.
[750] I won't say he's a very important visionary when it comes to ontology use within the modern industrial world, Industry 4.3 or whatever it is.
[765] Now he's connected with the university in Lausanne in Oslo, but he still has an Emeritus position in the EPFL, which is the French part of Switzerland engineering school.
[778] Then there is Serre, who played a very important role because he made this is why we're in this building.
[785] He made I f IOF somehow be under the umbrella of NIST, and he was responsible for other important things.
[798] In particular, this fight so the question when we founded IOS with BFO at the top, the question was, why should it be BFO?
[810] Some people said, We should work out which is better of the possible candidates.
[815] We had three candidates who came forward, and we spent months with all kinds of voting systems, and BFO won the vote.
[825] The reason why BFO won the vote, I believe, and I've written a paper about this, is because BFO is more than just an ontology.
[834] It's a support system.
[836] It's a product service system.
[838] It provides services, documentation, expert consultation, most of it free because we're crazy, constant updates to applications, recordings of applications of BFO and its related ontologies in different areas, including industry, and many other aspects that people find useful when it comes to ontology building.
[868] Dolce produces academic papers, but you don't really find any service support for your ontology work with Dolce.
[881] So now we have, as I say, more than 700 users of BFO, and one of, we have an increasing number of users.
[882] One of the main reasons for this is because of the idea of retrieval augmented generation, whereby many people are beginning to see that the retrieval the brag based procedures in AI work better when they are built on the basis of a well grounded ontology, and that means that we have more people interested in finding out what a well grounded ontology would look like, and that brings them to BFO.
[891] And this is why I gave you the handout.
[925] We have been, we, meaning, me and my collaborator who is an AI entrepreneur, biologist, MD, mathematician, philosopher, journalist, father of five children, and so forth.
[929] He is an extremely clever person, maybe too clever for his own good, who came to me in desperation having tried for fifteen years to build a chatbot for organizations like banks, and he had come to the conclusion that it's impossible.
[944] He wanted to find out.
[965] He came to me.
[967] I have no idea why.
[969] Well, apart from the fact that we knew each other, to find out why it is that it's so hard to build chatbots, and that's what the book is about.
[970] It's just been released in the second edition, and that's what the flyer is about.
[978] We now have several BFO based engineering ontologies that this is one of the first.
[982] It's a maintenance ontology, I believe, and you can see that Hedi is one of the authors here.
[988] We think we have made great progress in cleaning up the world of maintenance ontology over time.
[995] These are just some examples of other BFO based engineering ontologies.
[1003] I get about one a week from my Google alert.
[1008] I get about one a week from my Google alert.
[1013] This is BFO playing the role of top-level ontology.
[1017] It's serving as a starting point for people who want to build domain ontologies in their specific area.
[1024] Now it's not doing all the work.
[1026] It's not bringing these people together to form consistent suites of ontologies, which are linked to their neighbors within the suite.
[1036] That's why IOF is needed.
[1040] IOF creates that ingredient whereby the domain ontologies, if they do things properly, are well-structured because they're based on BFO. They also need to be future-proofed by being linked to the ontologies being built in the surrounding neighborhoods.
[1060] That's the only way you can have a chance of being useful in the next five, ten years if your ontology is being built in tandem with the ontologies being built by your neighbors.
[1073] This is the standard.
[1076] It costs 0 Swiss francs.
[1079] This screen is about the standard number two one eight three eight dash one, which is a statement of the requirements of being a top-level ontology.
[1089] BFO is two one eight three eight dash two.
[1092] It's also free.
[1095] It's free because it's used to build other standards.
[1100] ISO/IEC two one eight three eight dash two shows that BFO satisfies the requirements stated in dash one.
[1113] So what are the requirements for being a top-level ontology?
[1116] Well, there have to be textual definitions of all the terms.
[1120] There has to be an OWL2 axiomatization, and there has to be a first-order logic axiomatization.
[1128] This is quite difficult, and it's difficult not least because we require a consistency proof for what may be a set of three hundred first-order logic axioms.
[1141] The final requirement is the real killer.
[1145] It has to be maximally general.
[1148] In other words, it has to cover everything.
[1152] That's Rahad.
[1153] It's hard to work out how we would prove that you satisfy that requirement.
[1158] The way we decided was we gave a list of 12 domains, including things like processes, objects, activities of people, domains which are widespread, which cover many populations, many periods in human history.
[1187] We say that in order to prove that you satisfy the requirement of being maximally general, you have to show how you would handle data using your ontology belonging to that particular heading.
[1201] There are 12 headings.
[1204] Alright.
[1205] Now in all of this, we did not include mathematics under the heading.
[1211] We did not include physics under the heading.
[1214] That's because we were interested primarily in areas where people collect empirical data.
[1222] People do not collect empirical data when they're doing mathematics.
[1226] Now we have decided because we want to move out into the world of physics that we need to have some way of dealing with mathematical entities.
[1235] Not as part of BFO, because we're still constrained to areas where we have empirical data.
[1242] But in order to do physics, you need mathematics, and so we need a way of understanding ontologically the relationship between mathematics and BFO.
[1251] This is a very early approach to that particular set of problems, written by my AI colleague.
[1262] The second edition of the book contains a new chapter on physics, which is about physical systems.
[1268] It's a contribution to the ontology of systems engineering and systems physics.
[1276] Alright.
[1277] So Todd, who is Todd here?
[1281] In some virtual sense of here.
[1285] Okay.
[1285] Somebody ought to tell him that I'm beginning to talk about.
[1290] Todd raised some questions about what I called principles of realism.
[1295] BFO is well known to be an ontology which attempts to satisfy a realist approach.
[1305] Now there are two worlds in the ontology kingdom, one world is the US and the three worlds.
[1315] One world is the US, one world is Europe, which means Italy, and the third world, which we won't talk about, is England, which is really bad.
[1325] In America, people would turn, first of all, to BFO if they want to choose an ontology.
[1332] In Europe, they would turn to Italy and to Dolce because Dolce is Italian, and the Europeans don't like to use things which they think are tainted by America.
[1346] BFO is a realist ontology.
[1350] Dolce is a domain ontology for linguistic and conceptual engineering.
[1358] If you see an ontology with a name like that, you should run in the opposite direction because it means you're building an ontology of what goes on in people's heads or when they speak.
[1373] If you want an ontology about factories or about molecules or about chemical processes.
[1379] You don't want to know what goes on inside people's heads.
[1383] You want to know what goes on inside the world, and then you want to find good ways of describing it.
[1388] That's what BFO tries to do.
[1392] It turns out that when you move at this general level, then you can apply it it's so general.
[1398] You can apply it at multiple levels of granularity.
[1401] You can apply it to molecules, and you can apply it to planets and galaxies for all we know.
[1408] You can apply it on the basis of different perspectives.
[1411] You can look at the process in the world.
[1413] You can look at the objects in the world.
[1415] You can look at the time sequences in the world.
[1417] BFO can cater in this minimalistic, highly general way to all of these different perspectives.
[1426] Dolce can do that too.
[1428] But Dolce does it from a conceptualist direction, and BFO tries to do it from what we call a realist direction.
[1438] And so Dolce looks to the concepts in the world, and the problem is, of course, that people in Italy have concepts which are different from people in Peru or Tibet.
[1450] And that's why we don't look at concepts, we look at the molecules or at the people or at the buildings or the manufacturing processes.
[1460] And then we find that there are categories or types or universals in each of those areas.
[1465] There are types of people, there are types of buildings, there are types of processes, and these types have relations.
[1472] And BFO works at the level of very general types, which we call categories.
[1478] We try to work out the relations at that level, and then those relations are inherited at lower levels.
[1484] So this is the top level.
[1487] We have continuants, which are things which continue, and we define that in this very limited way.
[1493] When you're at this level, it's very hard to formulate definitions because to formulate definitions, you need to say what kind of thing you're defining, and then you need to know what the next kind up is.
[1505] And we here, we're at the very top.
[1509] So we have independent continuants like people, planets, tables, molecules, and we have what we here are calling specifically dependent continuants, which means things like shape, color, temperature, and so forth.
[1520] So qualities, in other words.
[1522] Also, roles will come to that.
[1524] And then we have processes.
[1527] And all of these are universals, and at the bottom, you can see instances.
[1532] One of those dots there on the very left is me because I'm an independent continuum.
[1538] I continue to exist and don't depend on anything else in contrast to my headache, which depends on me.
[1545] It's a specifically dependent continuum.
[1548] We'll see what specific is doing here in a minute.
[1553] Alright.
[1553] Now, of course, we might be wrong when we build an ontology.
[1559] Realism doesn't say that every ontology is somehow connected to its own reality.
[1564] What it says is that we should strive to have ontologies which reflect reality.
[1570] Now the question is, how do instances play a role?
[1579] We're not really interested in universals.
[1581] We're interested in universals because they have instances such as you and me.
[1586] We are both instances of a universal, namely the universal human being.
[1592] One of the issues is, do all universals have instances?
[1599] Dusan is in the room because Dusan is the vehicle for producing what I think is a good answer to this question.
[1609] When we are designing a new kind of gadget, there are no instances, but we want to talk about objects of that kind already in the design phase.
[1625] That's what design engineering design is all about.
[1628] How does BFO then manage to work with engineers who are involved in the design phase when there are no universals?
[1639] For Aristotle, every universal always has instances.
[1645] He doesn't leave any room for evolution or for production design processes.
[1652] But we have to allow the possibility that a design might bring into existence something like a universal even though there are no instances of that universal until a much later phase in the engineering process.
[1667] I am now canvassing for the idea that we introduce a new term or, anyway, a new definition of a term which we've been using sloppily for a long time, namely the term type.
[1681] Types are a special kind of universal.
[1683] They are universals which can exist proactively.
[1688] In other words, they can exist before there are any instances.
[1693] I'm going to put type into a little pocket I've created for my own purposes called BFO plus, which is where I'll put terms which are, for one reason or another, not going to be part of BFO, at least not yet.
[1711] Now we come to a second set of questions which come from Claude.
[1712] I haven't talked about general. I should've typed, read, or proofread the question.
[1717] We have specifically dependent continuance in BFO.
[1727] We also have generically dependent continuance, which I think is what Claude is getting at here.
[1731] A generically dependent continuance is an attribute which can migrate.
[1737] An example would be a PDF file.
[1744] A PDF file is a generically dependent continuum because you can send your PDF file to a friend by email and delete it from your computer.
[1748] The PDF file still exists because it's migrated to another bearer.
[1759] You can't do that with your headache.
[1765] You can't do it with your height or your weight or your shape, but you can do it with a generically dependent continuum.
[1768] Information entities are the main example of generically dependent continuance.
[1776] Now Claude wants to know, are there other kinds of dependent continuance?
[1783] He created this chart, which I'm using as a starting point now for understanding questions like this.
[1788] First of all, Claude distinguishes wants to know, I guess, this is the modality that we're speaking now.
[1797] So first of all, Claude distinguishes wants to know, I guess, this is the the the modality that we're speaking now.
[1806] Are there human-made entities which fall under the BFO, universal material entity, alongside natural entities?
[1817] In other words, are there two kinds of material entities?
[1820] We don't have that in BFO.
[1823] Someone might build an ontology, which is lower down, which makes that distinction.
[1828] That would be fine.
[1829] But I don't think the distinction is well grounded because some natural entities may be remade artificially.
[1842] So we may have a molecule which is a natural entity which cures cancer, which we find in a certain plant.
[1849] It's natural, but then we make many copies of this molecule in a factory.
[1855] It's the same molecule, and so there is no cut, no divide between man-made and natural entities in BFO or near BFO.
[1869] The next well, this is so Claude has cancer under natural material entities.
[1869] The problem with cancer and you have to remember that BFO was born because I and my colleagues were thinking about the questions like, what is, ontologically speaking, cancer or a cancer?
[1881] That's important.
[1897] That that's important.
[1899] So in one meaning, cancer means a tumor, which is an object.
[1904] And this is can this is cancer as a count noun where you can say two cancers or four cancers because what you mean is two tumors or four tumors.
[1913] And then cancer might mean disease, which is a disposition.
[1917] I'll come to what dispositions are later on, but roughly speaking, it means potentials, tendencies, real physical possibilities.
[1927] And this is also a count noun.
[1929] You can have two diseases or 17 diseases.
[1933] And then there is the cancer in your body, which is replicating itself very rapidly.
[1939] That is not a count noun.
[1942] It means the whole cancer in your body, and then it's a mass noun, sugar or luggage or information.
[1950] In France, you can talk about informations in French, but you can't talk about informations in English because it's a mass noun like water or any substance noun.
[1960] So how do we deal with mass nouns?
[1963] It turns out that when you try to deal ontologically with mass nouns, you make mistakes, or the people who use your ontology make mistakes.
[1973] Now I believe, and this is from more than twenty years of experience now, standing in podiums like this, that ontology, good ontology, ontology which is good for the world, has a legislative function.
[1991] In other words, we're going to force people to move in a certain direction.
[1996] They don't care.
[1998] Who cares about whether you use mass nouns or count nouns in a specific context?
[2003] But we care because we know things.
[2005] And so we should tell them in a loud voice, even with an English accent, a loud convinced voice.
[2014] You should never use mass nouns when building an ontology, and we'll you just make mistakes if you do that.
[2024] Alright.
[2025] Now water, the same kind of problem arises for water.
[2029] Water is in its main uses a mass noun.
[2031] So you could order six waters from the supermarket by means of which you mean six different kinds of water, but then you should say six kinds of water or bottles of six different kinds.
[2041] You shouldn't say six waters.
[2043] It sounds bad in English.
[2047] And then there are four meanings of the word water.
[2049] In ordinary English parlance, you could mean a kind of water.
[2053] You could mean some water.
[2055] You could mean all the water in the universe.
[2057] You could mean exactly one pint of water.
[2061] Here too, we see the problems that you get when you use a mass noun.
[2065] You should use "portion of water," which is a count noun.
[2071] Something similar arises for stone.
[2073] These are all Claude's examples.
[2076] When you say "use stone," you might mean this stone, or you might mean the substance stone, or you might mean all the stone in the universe.
[2083] But if you just say stone, you won't have clarity because it's a mass noun.
[2088] The same thing applies to air.
[2091] Here an air might mean the aggregate of air molecules.
[2095] That's probably not what it is, but that's what some people mean when they think they're thinking precise.
[2102] So, again, I've said it four times now.
[2103] When building an ontology, never use mass nouns.
[2105] If you find mass nouns in an ontology, you should run in the opposite direction.
[2107] Now this means that BFO made an architectural error, not because we used mass nouns, but because we ignored an issue that BFO faces when it tries to be applied toward the real physical world.
[2115] This is why physics becomes important.
[2133] We have objects, but when we're dealing with liquid, portions of liquid, or with portions of gas or with portions of plasma, none of those are going to be objects, at least not at ordinary room temperature.
[2136] So BFO needs to be extended with terms which will cover portions of material which are not objects.
[2150] So BFO needs to be extended with terms which will, cover portions of material which are not objects.
[2162] Now, interestingly, there is an ontology called the European Materials Modeling Ontology, EMMO, which was created by an Italian, mostly, as part of a European Union project of the European Materials Modeling Council, and it was really good.
[2190] It was based on BFO.
[2192] It added to BFO granularity layers to deal with gases, liquids, plasmas.
[2199] Very well architected.
[2201] I was really impressed.
[2204] Unfortunately, I didn't take a screenshot.
[2210] Now suddenly, behind our backs, because the funding from the European Commission ended, I imagine, they changed the name.
[2219] It's now called the European multi perspectival ontology.
[2233] I've forgotten what the other m means.
[2240] So the European multi perspectival ontology.
[2243] And now it's changed completely.
[2245] The layers, the granularity, the object, the plasma, it's all gone.
[2249] Now they want to build everything on the basis of quantum physics.
[2255] They have 11 axioms, which they think give an account of everything which exists because everything is made of quantum something.
[2265] So if we build our ontology based on quantum something, we will have everything.
[2269] We'll be a top level ontology from the bottom up.
[2273] It's very strange.
[2275] I won't talk anymore because I get angry.
[2278] Alright.
[2278] Now Claude says, where do philosophical concepts go?
[2286] I wish I had an hour for the next bit.
[2290] When I started working in ontology, I was working with medical people.
[2296] There is a very important medical ontology called SNOMED, the systematized nomenclature for medicine.
[2303] Still very important worldwide, lots of different language versions, very well defended by governments.
[2312] They changed it a bit to calm me down because I had a multiyear campaign.
[2319] It's crap, I said.
[2321] Mainly at the top.
[2322] At the bottom, there's just too much, but at the top, it's crap.
[2326] What is at the top?
[2327] The word concept.
[2330] Everything in the medical world is a concept, they said.
[2333] So did the influenza is a concept.
[2336] That's nonsense.
[2338] There is a concept influenza, but that's a concept.
[2342] But influenza is not the concept of influenza.
[2346] Influenza is something that goes on in reality, not in people's heads.
[2352] So what's the solution?
[2354] This applied in other areas in semantic web.
[2357] It's full of concept crap.
[2360] I said, never use the word concept.
[2365] If you use the word concept, you have to give me a dollar.
[2371] That was the idea.
[2372] If I use the word concept, I have to give you $100.
[2376] That was the deal.
[2377] I did not use the word concept then.
[2380] I mentioned it.
[2383] Alright.
[2384] That's the deal.
[2385] If Claude never used the word concept, you will be my friend.
[2389] You will save France.
[2392] Alright.
[2393] Then we have mathematical thingies, geometric shapes, numbers.
[2397] They were working on the mathematics ontology, and we're working on the physics ontology, on entropy.
[2404] One of the principal topics running through the whole book is entropy, thermodynamics.
[2412] That's the AI book, not the BFO book.
[2415] Alright.
[2415] I mentioned this already.
[2419] What other kinds of cases of generically dependent continuance do we have in addition to the two main examples in BFO papers at that time: gene sequences or ribonucleotide sequences, protein sequences, and so on.
[2440] On one hand, information entities on the other hand.
[2445] These are generically dependent continuance.
[2447] We know that gene sequences are patterns in your genome, which can be copied multiple times, which is the mark of a generically dependent continuum rather than a specifically dependent continuum.
[2461] So what other exact confusion is one of the confusions, which I believe we helped to eliminate from hype about the genome project.
[2476] One of the confusions is that to say that a gene, a DNA sequence is an information entity so that biology now becomes part of computer science.
[2488] People said that.
[2489] They say similar things about AI, similarly confused things.
[2496] Gene sequences are not information entities, but they are entities, molecular entities, which are such that we can create very, very reliable representations in information entities.
[2508] So we have a copying process.
[2511] We have a process of perfect representation in an information entity, but that doesn't the fact that we have a really good photograph of a person does not mean that a person is a photograph, which is the argument they made.
[2527] We created an ontology of information artifacts which made clear that information artifacts are not made of molecules.
[2536] We were working on OB, particularly, a group of people which included me, but which included other BFO creators.
[2548] Alan Ruttenberg is the most important person at this stage in the history.
[2553] Still today, very important.
[2555] We created clarity about the relation between gene sequences and information, and that's now built into the way the world of sequence biology functions.
[2569] Alright.
[2569] Now what other patterns are captured in addition to information and gene sequences?
[2577] That's Claude's question.
[2579] Well, my answer is games are generically dependent continuants.
[2584] Laws are generically dependent continuants.
[2587] So in other words, everything which goes on in Washington, it revolves or evolves around generically dependent continuants.
[2596] They're creating them all the time, and they're not just pieces of information.
[2600] They have powers.
[2603] Software is a mass noun.
[2608] There are no fines imposed for using software, but you shouldn't use the word software.
[2614] You should say piece of software or software tool.
[2619] Money is a dependent continuum.
[2624] The most important frontier areas of BFO research today relate to things like money, transactions, and things like that.
[2640] Laws also.
[2641] The state.
[2643] Alright.
[2644] These are features of BFO, and now comes Todd.
[2651] Now you could send Todd a message.
[2655] Then he can't defend.
[2656] Otherwise, he can't defend himself.
[2657] I hear you.
[2659] What follows if the realism principle is dropped?
[2662] You use BFO, you say all the nice things, but you don't care about reality.
[2669] We address this problem in a paper about realism.
[2677] One of the points we make in this paper is that we have people using BFO well who don't care about realism.
[2685] They don't care about reality.
[2687] They're like other computer scientists.
[2688] They like the software architecture that BFO makes possible.
[2693] You don't have to believe that you're replicating or representing reality to do good work with BFO.
[2700] BFO enables you to have clarity about distinctions on the side of reality, which other ontological processes are confused about.
[2712] For the purposes of this meeting, I tried to write down what some of those clarifying insights might be.
[2719] These are not new.
[2721] Aristotle was already here, but they are new to many circles of ontology application activity.
[2730] The first thing is Aristotle said every universal has instances.
[2751] We have now, after a long and bitter argument with Dusan, come to the conclusion that there are universals which have been created by people and which exist even though they don't have instances yet.
[2767] That is a useful clarification if you're interested in ontology, engineering design, musical composition, dance invention, and many other areas.
[2784] Most of the really interesting things in life are generically dependent continuants.
[2790] Money and laws, but music and poems.
[2795] All right.
[2795] The second is a very important test for whether you have a universal which you're dealing with.
[2805] A universal is such that if you instantiate it at any time.
[2814] A universal is such that if you're an instance of it, but then later cease to be an instance of it, then you will go out of existence.
[2826] I'm a human being.
[2828] If I cease to be a human being, I'm gone.
[2831] There isn't me anymore.
[2834] A cat, similarly, if it ceases to be a cat, it will no longer exist.
[2838] If you are thinking of things like factories which are open on Sunday, that is not a universal because it doesn't satisfy this test.
[2851] You can close the factory on Sundays.
[2855] It would still exist.
[2858] It wouldn't satisfy the label, but this just means that label is not the label for a universal.
[2866] This is the, well, more examples.
[2870] Dog is a universal by this test.
[2872] Child is not a universal.
[2874] When a child ceases to be a child, it doesn't go out of existence.
[2879] Every universal has to satisfy both of these conditions, and we think.
[2889] It might be that we need to work on that with regard to engineering design again because you could have a really good engineering design created by Ford or somewhere, and they invest millions.
[2902] The design is fantastic, but then there is a nuclear war, and they never build a single instance.
[2908] We still need to work on the details.
[2911] But generally speaking, we have this rule that every universal must at some time have an instance.
[2916] Yes?
[2933] You're not really allowed to speak at this point, but a lot of philosophical time has been wasted by questions like that.
[2947] Who cares?
[2950] You're hanging out with the wrong people if you worry about unicorns.
[2953] Well, no.
[2953] Of course.
[2954] Let's get a little more technical.
[2955] For example, there are technically designs done by Jules Verne or Da Vinci that would never become yeah.
[2964] I just said we need to think about designs which never become realized.
[2968] So I'm on the same side as you where it matters.
[2968] How technical does it have to be to be recognized as a design?
[2971] That's an edge problem.
[2974] We can never get perfect precision.
[2977] So we have this rule.
[2979] We put the word "prospectively" in here to keep you happy.
[2980] Other principles.
[2983] Number four.
[2988] So Plato has this phrase, there are when you try and cut up reality, we're trying to cut up reality now, there are joints.
[2988] There are places where we do have divisions.
[2991] We may learn later that there are no divisions, or we may learn that what we thought was a twofold division is in fact a threefold division.
[2993] So ontology is part of science in the sense that it's a fallibilistic activity.
[3003] We might make mistakes, but if we don't make any mistakes, then we can assume that where we find joints in reality, that means there are joints in reality, which means there are real distinctions between cats and dogs.
[3006] I better not say males and females, even between children and adults.
[3015] Even though we don't know where to draw the line, we still accept that there are real distinctions between children, or we should still accept that there are real distinctions between children and adults.
[3022] We're trying to capture those real distinctions.
[3037] I don't I better not say males and females, between children and adults even.
[3043] Even though we don't know where to draw the line, we still accept that there are real distinctions between children, or we should still accept that there are real distinctions between children and adults.
[3054] We're trying to capture those real distinctions.
[3056] The real key is that when we track down those real distinctions, we end up with hierarchies in the mathematical sense.
[3070] That means a tree is a hierarchy.
[3074] Every node in the tree has exactly one parent except the very top node, which has zero parents.
[3085] Aristotle influenced Linnaeus, who showed that this is true of the world of living things.
[3093] Problems arise at the level of bacteria, but for macroorganisms, the hierarchical principle applies.
[3115] In order to be successful, you have to build your ontology as part of a hub.
[3124] If you are not already part of a hub and you have already built some ontology, find the nearest relevant hub and make your ontology fit with that hub.
[3139] That is what IOF is for.
[3141] The second key to success is to choose a well-grounded top-level ontology, and BFO is the only game in town.
[3152] Another rule is very cheap to follow.
[3160] Every term in an ontology should be a singular noun or noun phrase, such as "drug administration" or "headache."
[3169] The main classification of medical information has a very nice axiom.
[3184] Socialism is our political system.
[3192] That is evidence of a mistake because nobody told them about singular nouns.
[3200] The reason singular nouns work is because terms in ontologies represent universals, and you want to have one term for each universal.
[3210] You need a noun or a noun phrase.
[3213] No verbs.
[3214] No sentences.
[3217] Here we have the qualities.
[3220] Qualities is a process, and processes is a temporal.
[3228] Temporal is a base ontology.
[3229] Something is going wrong here.
[3233] BFO doesn't have that kind of thing go wrong.
[3238] We know what continuants are.
[3239] We know what occurrences are.
[3241] You are a continuant.
[3243] Your life is an occurrence.
[3246] We have "depends on" specifically, and temperature depends on the bearer.
[3251] You can't get someone else's temperature.
[3254] Influenza may be a generically dependent continuant, although we need to think about infectious diseases very carefully when we're dealing with things like that.
[3268] We have a really good infectious disease ontology.
[3272] So now we come to government and law and things like that.
[3274] I have six minutes.
[3279] Qualities we know, they're easy to understand, and they are such that if they exist, they exist at all times.
[3282] There aren't two modes of existence in the way there are two modes of existence for something like lecturer.
[3292] I am a lecturer because I am now realizing my role as a lecturer, but I'm not always realizing my role as a lecturer, and sometimes I sleep, and I may never realize my role as a lecturer.
[3302] I may just be paid money to be a lecturer in a university or somewhere.
[3318] Roles are different from qualities.
[3325] Roles are not always realized.
[3327] Roles are not always realized.
[3330] Qualities are always realized.
[3332] Dispositions are roles.
[3337] They're not always realized.
[3338] We have two kinds of specifically dependent continuants.
[3342] I'm going to leave the next four minutes to John to go through some yellow slides.
[3353] I'll just say we have qualities and we have realizable dependent continuants.
[3358] Realizable dependent continuants are roles on the one hand, which are assigned by some social act typically, and dispositions, which are a matter of physics.
[3370] Hello.
[3373] I didn't realize I'd be up, so I'm here.
[3375] Yeah.
[3384] I'm happy to take as long as you'll give me.
[3384] I do like to talk, and I love a stage.
[3386] Processes and BFO.
[3388] This has taken up a lot of time and thought on people's parts.
[3390] Barry asked me to get up and say a bit about it because I've thought a lot about it myself.
[3392] You probably know or if you don't, I'll remind you.
[3396] Processes and BFO are not the sorts of things that change, so they don't have qualities.
[3402] They're not bearers of things like you and me.
[3406] So processes and BFO are not the sorts of things that change, so they don't have qualities.
[3412] They don't they're not bearers of things like you and me.
[3415] I bear a shape right now, a certain shape right now, a different shape right now, a different shape, stuff like that.
[3423] Gaining and losing these things over time is a very intuitive way of understanding, but philosophically and from a common sense perspective, what change amounts to is a gain or loss of properties of that sort.
[3435] Right?
[3435] So what is it for something to change? Extend it over time, gain or loss of properties.
[3441] So we're dealing with processes though.
[3444] We say they don't gain or lose properties in the same way that you or I might, because, roughly speaking, they have happened already.
[3458] So they're there.
[3459] The processes and BFO exist.
[3462] They're already there.
[3463] They have the dependent entities that they will always have once they've occurred.
[3469] So it's not proper.
[3470] It's incorrect to say that they might gain or lose properties the way I am when I move because they already have the properties.
[3479] So because of this, it's a consequence, an easy step to jump over and say, well, the processes, they aren't really changes or they aren't really changing, because they don't fall into this gain or loss.
[3493] Nevertheless, they are changes, we say.
[3496] So there's the extra, in a slogan form, processes don't change, but they are changes.
[3503] So the gain or loss of properties that happens with processes.
[3511] Now, of course, you can talk about different aspects of processes or different cuttings or slices of processes, as a way of describing differences from one slice of the process to another in a way that might look like change.
[3526] And we have to do this.
[3528] You say John is speaking slowly now, and in this process, he starts speaking more quickly.
[3535] And he's doing this thing with his mouth and all that good stuff, and it's up and down and up and down and all that.
[3541] But it's not the process that's changing.
[3543] It's John.
[3545] Does that make sense?
[3546] I'm changing.
[3547] I'm participating in the process and participating in something that's extended over time.
[3551] What you're doing is you're looking at slices of that process of speaking, and we're thinking about the changing, what might be inclined to say is the changing of the process is John's participation or the properties that he's bearing being gained or lost throughout that.
[3567] Putting this with a finer philosophical point, sometimes this is described in the literature as not real change.
[3578] It's more like difference.
[3580] So difference of one part of a process at one point versus difference of another.
[3585] So sometimes, as I said, that's not real change or processes because there's not gain or loss of properties, but it's just difference at different times.
[3593] Much like if you have a fire poker and it's cold on one side and hot on the other, there's just a difference.
[3601] There's no real change between the fire poker's ends.
[3603] You're just looking at one point and you're looking at another.
[3606] One has a hot property; the other has a cold property.
[3609] Does that make sense?
[3611] Whether you agree with it or not, I just want to make sure if that makes sense.
[3614] Yeah.
[3615] Fermentation.
[3617] Fermentation?
[3618] Describe fermentation.
[3621] Sounds like a process to me.
[3632] This is a good example.
[3634] Say more about the amount of fermentation change.
[3640] What are you counting?
[3642] Well, fermentation needs a kick start to begin with.
[3645] Does that make sense?
[3645] Yeah.
[3646] Just because it put the greens on the table doesn't mean fermentation will start.
[3649] Of course.
[3650] And fermentation will end when a number of things happen, either temperature or sugar.
[3656] Agreed.
[3658] Agreed.
[3659] But calling that thing a process of fermentation, which is how it's generally discussed by humans, does not fit into your model as clearly as I can see.
[3670] I feel it does.
[3670] So you have a process of fermentation that has lots of different accelerators or catalysts or whatnot ingredients.
[3677] And these are a lot of material things, portions of material things that bear various qualities at various times, they bear dispositions and whatnot.
[3684] They might even bear roles at certain parts if it's an accelerator.
[3689] Nevertheless, those are all qualities, properties borne by the material stuff or the independent continuants that are participating in a process of fermentation.
[3700] So, but I'll help you out.
[3701] Does that make sense?
[3701] If you think about the kind of thing that might be troubling when trying to fit in this model, you want to talk about the rate of change or something of the fermentation process.
[3713] You want to talk qualitatively about the process itself rather than the accelerator or the yeast or whatnot.
[3722] Right?
[3723] And I'm bringing this up on purpose.
[3725] It's unintuitive to some extent the way it's modeled.
[3730] All of that kind of rate change, all of those descriptions that you might be inclined to attribute to the process itself, they all have to be grounded in the material bearers, the independent bearers gaining or losing qualities or dispositions or roles or whatnot over time.
[3747] And so you always have to bear just fundamentally point there when you're describing the change rather than describe the process itself as bearing some kind of qualitative change.
[3760] If I put that even more simply, a flight can be turbulent.
[3764] We want to say a flight is turbulent.
[3766] Right?
[3767] It's the flight.
[3768] But on our characterization, it's the jostling and whatnot of the things participating in the flight.
[3775] That's where the turbulence is derived from.
[3778] And we can, loosely speaking, say the flight is turbulent, but really, it's me jostling in my seat, among other things.
[3787] Does that make sense?
[3789] I have a question, which was for Barry, but you can answer, John.
[3793] No problem.
[3794] That was my original question.
[3796] So in, I have meetings recently, we discussed process profile, process characteristic.
[3801] Am I reading you correctly that they don't exist because they are describing SDCs or participants in the process or being just shedding some light on that process profile, process characteristic?
[3816] Yeah.
[3816] Yeah.
[3816] What I'm saying should be compatible with process profile, process characteristic.
[3821] Although process characteristic, as I understand, doesn't have a formal characterization yet, although it's a work in progress.
[3828] And process profile was introduced to capture the commonalities that we see in processes, regular change cycles and stuff like that, without having to say anything about processes themselves, having qualities, or get into the issues that you might get into when you're dealing with AI and trying to talk about turn air or trying to get outside the scope of AI and talk about turn air properties.
[3855] Without these sorts of resources, process profiles enter the picture as a way to talk about these regularities of processes that we see.
[3864] Again, compatible with everything I've just said about the change.
[3868] I'll note that, to my mind, the best, at least correct me if I'm wrong, my best understanding of the utility of process profiles are as instead of the sort of temporal slices that you might take of processes at various times.
[3891] And process profiles are a way to cut horizontally out of processes that you take interest in.
[3897] So, the beating of my heart as part of the process.
[3900] I might take interest in the regularity of it existing over time, that kind of cycle.
[3905] And what I can do is I can take that slice and then take a slice horizontally and think about specific beat here or there or some subset of the beats.
[3913] And I find a lot of value myself modeling and being able to do that kind of cross stitching using process profiles versus processes.
[3921] Although I will say, to your point, the process profile characterization that Barry presented in the literature was initially pitched, and I think can do some of the work of capturing intuitions about process change here.
[3937] Although, again, it's not going to be, at the end of the day, different from what I've described insofar as the processes themselves don't have properties.
[3947] They're not gaining or losing properties nonetheless.
[3950] It's kind of like a refocusing of phase sessions, if I'm walking three miles per hour.
[3956] Is this process characteristic or my SDC, my quality at that point?
[3961] What is the process characteristic?
[3964] Process profile or I don't know.
[3965] We have that in IFN slash BFO.
[3969] Let me have a go.
[3970] We've been trying; this is a really hard problem.
[3973] I know.
[3973] I know.
[3975] Change.
[3975] We've been approached by many people who have begged to give us a vehicle for describing what intuitively are the qualities or properties of processes, and you're one of them, I imagine.
[3990] We've come up with the following solution of convenience.
[3998] Namely, if you want to build an ontology and you want to describe processes, then we give you an analog of quality for processes.
[4009] We use the term process characteristic.
[4012] So a process characteristic is on the page just like an object quality, and that means anything you can say about the process in principle can be recorded in your ontology as a process characteristic.
[4026] So if the process was interrupted, if the process was boring, if the process was repeated, then they're all process characteristics.
[4034] And you may define a process characteristic for your own purposes in your own ontology, and that will be all legal and BFO conforming.
[4043] There is no universal process characteristic.
[4046] It's merely an abbreviation for something which takes account of what John has just been saying.
[4054] We admit that we have come late to this particular circus for reasons which have to do with very powerful philosophical considerations, and we are now working very hard to document what I just said in a way which doesn't sound quite so fishy.
[4075] Then I need to talk about process profile.
[4077] Yeah.
[4078] Yeah.
[4078] So I question.
[4080] I want to add not easily done.
[4082] Yeah.
[4082] Yeah.
[4082] I want to add.
[4083] Barry's talking about us coming late to the game and whatnot.
[4087] I'm not so sure.
[4089] We're not linguists.
[4091] I'm not an ontology engineer because I'm interested in linking the way people talk.
[4097] I'm interested in modeling a structure on which I can derive the way people talk.
[4102] I totally understand how what I've just described might sound a little counterintuitive.
[4108] I don't care because I can derive all the intuitive stuff that you say.
[4113] That's what I care about.
[4114] I have a common structure that can do that.
[4116] You can call it what you want.
[4118] Process gets your heckles up.
[4120] Call it something else.
[4121] I don't care.
[4122] I'm not a linguist.
[4124] Some of this in these conversations I find, and I talk about this a lot.
[4129] A lot of intuitions get mongered.
[4131] People have an idea of what events are and processes or whatnot.
[4134] I don't care.
[4135] I care about the logic, and I can derive what you say.
[4139] I meet you.
[4140] Yeah.
[4141] That's right.
[4142] Let me ask a question.
[4144] One thing that's unclear to me is how if a process is change, how do you point out a particular, specifically dependent continuum, to say that is the thing that's changing, the color of the rose, for example?
[4159] Is that possible?
[4160] What relation would you recommend using?
[4165] Can you hear me?
[4168] So the way you just described, I guess, you have, we have, you can say this, but ultimately, I think what you're asking about, you want something deeper than a process profile.
[4181] You can give it a name.
[4182] You can give it a class name.
[4183] But if you're talking about the actual change, the thing Problem is that a process has a participant, but then it's just a vague you're pointing at the participants something about that changed.
[4194] Mhmm.
[4195] And if you're talking about running at six miles per hour, how do you point at a particular well, it's a bad example.
[4202] If you're talking about the color of the rose changing from red to brown
[4206] How do you point at the color of the rose to say that that is the thing that that changed in this process profile?
[4214] Yeah.
[4214] On the one hand, we have some resources to do this.
[4217] You can point to the specific instance of quality that is born by the rose.
[4222] 4. We do this in that case studies paper, BFO, that was in the applied ontology journal.
[4222] And we do this in that case studies paper, BFO, that was in, the applied ontology journal.
[4226] You can point to that specific quality and say it has this determinate determinable relationship.
[4232] You can talk about it having a specific instance of a specific shade and then shifting over to different shades.
[4239] You can talk at a higher level of green or red or whatever color it is and say the determinable level, there is still a constancy to the change, but you can also talk about the instance itself taking on different determinant qualities.
[4253] 10. It is just cycling through that.
[4254] We are changing through them.
[4255] Like, it's just kinda cycling through that.
[4257] That is what we do in the case study papers.
[4258] That is a specific instance of quality at the determinant level that goes from green to brown.
[4266] 15. A specific instance of brown can not be shared by other instances.
[4266] 17. The instance itself can take on different determinant colors.
[4269] Now, of course, it's specific, like, instance of brown can't be shared by other instances.
[4276] Right?
[4277] They're not migratable, but the instance itself can take on different determinant colors.
[4284] The question I have is, is the color changing from, let us say, red to brown, the name of a determinant universal, is it encoded in the name?
[4298] Is there some other way to connect that portion of a process, to say that the subject of the change is the color of the rose as opposed to the size of the rose?
[4309] I see what you are saying.
[4310] In the resources with BFO, we have participation.
[4314] We have the links between the change and process.
[4317] But there we leave open how you model the specifics of the change and how you point to the subjects and objects.
[4324] But in something like the common core, there's a whole hierarchy instead of relationships that characterize how you would pick out the subject that's changing or being gained or lost.
[4335] So I'm going to talk about process profile if I go back to the podium.
[4341] But I will say now that in the original paper about process profiles, we distinguish various kinds of process profiles, and one kind of process profile is what we call a polity process profile.
[4352] So you focus process profile means a sliver in the middle of a process that you focus on or measure or observe, and you focus on color.
[4363] So there is a process profile of the plant growth and decay process, which takes the plant from being red or green to being brown.
[4376] And that process is a process because every process profile is a process.
[4380] That process of changing color is a part of the larger process of the plant fermenting and rotting, and that's the general principle.
[4389] So process profiles are processes, but they are parts of larger processes.
[4398] So the process of his heart beating is a process profile within the much larger profile, which is his life or his history.
[4407] And the heartbeat process profile is cyclical for the moment, where his life is not cyclical.
[4417] So when we look at process profiles and we look at process profiles, we see different kinds of patterns which become combined together to make the whole full process, which is somebody's life.
[4430] And we have documented this.
[4432] It was part of BFO two point zero already.
[4435] It was removed from BFO twenty twenty because there are still questions.
[4443] So where do process profiles begin, and where do they end?
[4447] So he has not just a heartbeat cycle.
[4450] He also has a blood pressure cycle.
[4453] Is that one process profile if we take those two together, or is it two?
[4459] We don't really know where to draw the line of reality separating mere process profiles from full processes.
[4469] For that reason, we deprecated process profile from the official version of BFO, but it still has a BFO number because it was part of BFO two point zero, and it will now for the moment be part of BFO plus.
[4483] It's probably one of the most popular innovations in the BFO ontology world.
[4490] Of all the things that we've said, lots of people are using it. We, as you can tell, are not yet fully in control of how it should probably be used.
[4506] 100% agree.
[4507] So yeah.
[4509] Yeah.
[4509] Just real quick, and then I just want to check my understanding.
[4512] So a manufacturing process can be developed.
[4517] It can be constructed.
[4518] And so while it is being constructed, it is undergoing the process of construction and therefore is not yet a process because it's being changed by the process of making it?
[4532] Not quite.
[4534] Tell yeah.
[4535] Tell me more details. I'm being constructed.
[4539] Designing the process of building a car.
[4541] There's a process that needs to happen to the materials of the car.
[4546] Yeah.
[4546] But I need to make that process in the first place.
[4550] You mean design the process?
[4552] Yeah.
[4552] If you need to set up the process of designing a process.
[4557] Results in changes to the participant in that design process, the participant being the process that will be used to construct the car.
[4566] It sounds like you're saying.
[4568] I laid down a specification for the manufacturing of the vehicle that will prescribe the way materials will be arranged in certain ways in the future, but they haven't yet been arranged.
[4578] There is not a process until there is a process involved, but there's ambiguity here.
[4584] The one process you're talking about that is completed in this example is the creation of the blueprint.
[4591] Right?
[4591] Gone through the design phase.
[4593] Now what you're doing with the design phase and saying, hey.
[4595] Go forth on the conveyor line.
[4598] Right?
[4598] Put these things together in a certain way and follow this as a guide.
[4602] Then there's a different process that goes on.
[4604] Hopefully, if your company is gonna make a profit, a lot of processes that go on according to the specs and their processes that are subsequent to that, like sending these things to dealerships and selling them and whatnot that justify your original design.
[4618] Different processes going on, all of which can be explained according to what I've just described.
[4625] Yeah.
[4625] Okay.
[4625] That makes sense.
[4626] I would say that process is all along.
[4629] During the process of designing the process of creating the car, you have participants who are the designers, and they have various tests, mechanisms, and services that they draw on.
[4643] But it's all processes, and the participants are just who you would think they would be, namely the people involved and things around them that they use.
[4650] Once they've reached the point of having the design for the process of creating the car, then they have an output.
[4658] Processes have participants, and they have outputs.
[4661] In this case, the output is a process design.
[4664] That process design is an information content entity, but it's also an information content entity with an instruction or a request or a desirability or a requirement component.
[4682] So it's gonna make people do things like a musical score.
[4686] And so it's not any old information content.
[4689] It's not a description of something.
[4691] It's an information content entity with a what's the word?
[4696] Prescription role.
[4699] Not role.
[4699] No.
[4699] But yeah.
[4700] Role might That is where we agree because if you use only prescription, you cannot specify semantic relationships between this design process.
[4710] We never need to only.
[4713] I know.
[4713] But there is something else.
[4715] There is a process that you are designing.
[4716] Yeah.
[4717] There is a process, Jim says. Is it type or is it an ideal instance of a future process that you are designing?
[4724] So now you're slipping away again.
[4727] So let's go slowly.
[4728] And I know, but when you design a design process, so hang on.
[4737] Let’s get this right.
[4739] When you design a manufacturing process, tell me if I'm stating the example wrong.
[4746] When you design a manufacturing process, what you're doing is creating an information content entity.
[4753] That information content entity is going to serve the purposes of the people who then build the car.
[4762] Do we need to say anything more than that?
[4765] How do you represent relationships between participants in that process?
[4769] Between?
[4770] Between participants in this process that you are designing.
[4772] Which?
[4773] Processes you are designing when you pass the process, they are represented in the information content then.
[4778] But you don't represent participants in that future process.
[4781] There is no there.
[4782] There is no semantic.
[4783] You cannot ask who or what do I need to make that process?
[4786] So your agent in Provo.
[4788] Not engine, resources, machines, tools.
[4790] What is the output of that process?
[4792] Most of those things are universals that have instances all over the world.
[4797] Some of them don't have users.
[4798] What you're making doesn't have instances yet.
[4802] What you're making, you make that, so I'm not sure if it's true that designing the process for manufacturing a car of a certain type comes down in the end to creating that type in the sense that we both agree is possible to happen.
[4817] But if it is sufficient, then you have your type.
[4821] If the manufacturing process is ever unleashed, then you will have instances of that type.
[4828] But for the moment, you only have the type if you're lucky.
[4831] That's right.
[4832] I found another mic.
[4834] Yeah.
[4834] There's a straightforward way to model this.
[4837] If you're talking about blueprints and specs, stuff that is designing something that hasn't happened yet, much like in the case of fiction or simulations, there are no instances calling out to the arrangements of types you anticipate in the future.
[4850] You can handle this even within the scope of OWL, just like some basic restrictions.
[4855] You can create something like a blueprint specification as an information thing, and it's restricted to only types that otherwise would have instances, but a conjunction of them and the relationships that they might bear that exist already in the ontology.
[4871] So material entities, portions of this or that, all of which can recursively be defined even if you're referencing something that doesn't exist, all of which can recursively be defined in terms of information just on that recipe.
[4883] So you never have to talk about instances unless they come into existence as a consequence of the blueprints and types of roles.
[4890] Yeah.
[4891] Jim and I just finished writing a paper about this.
[4893] Jim and I just finished writing a paper about that.
[4896] Yeah.
[4901] Absolutely.
[4902] But we can do so at the level of types and intersect the intersection of types, which is an important distinction.
[4909] Unlike creating a specification for Honda SLS or something, unlike prescribing how I would like an instance to be a witness for the intersection of different types.
[4919] I'm not talking about any specific instance.
[4921] There is no instance.
[4922] But once there is, it's a witness for the intersection.
[4925] Just like when I'm talking about Harry Potter, a bunch of properties arranged in a certain way, nothing calls out to that.
[4931] If there is, I'll be suppressed in the future.
[4934] But right now, it's just a fictional thing.
[4936] Yeah.
[4936] Why not just consider design as a role for ICEs?
[4940] A role for ICEs?
[4942] Yeah.
[4942] I do not understand what you just said.
[4945] Say it again.
[4946] Well, consider design, an information content entity doesn't necessarily have to be a design until it's being realized as a blueprint or so on and so forth.
[4958] Why not consider it as a role?
[4960] I feel like the design itself.
[4962] I feel like you can have designs that aren't ever realized.
[4966] It seems like a plausible use.
[4967] People put together specifications that I'm just saying that in order to avoid what I was talking to telling Barry earlier, the fact that we just don't have to deal with the ambiguity of how technical a description of something that doesn't exist needs to be in order for it to be a design.
[4986] I can go on and write books about how biologically dragons get to exist, but I don't have a design of dragons.
[4992] I mean, I hear what you're saying, but I acknowledge there might be some value to avoiding the ambiguity or at least leaning into the ambiguity and getting by, but I am vehemently opposed to just allowing for that.
[5010] Because specifications, I will instead want a recipe for how to add the specification details as you need them, which is what we were doing.
[5017] I don't want to say here's a class and then fill it in as you want.
[5021] I want to provide guidance because I want the logical structure to be something that's repeated over and over again.
[5026] I think it goes away to answer the question you were raising.
[5030] How specific?
[5031] I don't tell you how specific.
[5032] I'll give you a recipe for creating the specificity, and then the stakeholders will tell me how specific it has to be.
[5038] I'm not a blueprint designer.
[5041] Not that blueprint.
[5042] I'm a recipe designer.
[5044] But this goes back to something I wanted to say when Barry was talking.
[5051] Oh, yeah.
[5051] I care about that.
[5054] I care about a recipe.
[5066] Of course you can.
[5069] I'm describing what they do.
[5075] I'm describing the life of engineers.
[5077] I'm not complicating it.
[5079] I don't wanna get in the way.
[5080] I'm not getting in the way.
[5081] That's what I'm doing.
[5082] I'm not gonna, for example, say that there's an instance calling out to some design specification that's not the spec itself.
[5090] That's some intersection of instances or the types that they have, that would be getting in a way because I'd be making them say something false, and they would agree.
[5098] I'm Alan.
[5101] I'm working for Boeing.
[5102] Boat leader.
[5103] I'm an engineer.
[5104] I'm also a cult leader in trying to socialize the value of ontology within Boeing.
[5110] We were talking yesterday about the church of ontology.
[5114] I feel like I'm walking into a minefield here, so bear with me as I start rambling my thoughts.
[5122] Right.
[5122] The notion of a design within manufacturing in aerospace of a design that may never come to be.
[5132] Right?
[5133] The process of a design, the act of engineering feels like that is a process.
[5144] In that act of engineering, there is an output which is a blueprint or a CAD drawing or something that feels like an information content entity that would then be used if we want to realize that product in reality.
[5163] I have a thought in my mind of about this thing that I'm gonna design.
[5172] Right?
[5172] I might put that thought on a piece of paper.
[5176] Right?
[5176] I've externalized that thought into reality for other people to see.
[5181] I might put that thought on a piece of paper.
[5184] I might put it into a CAD.
[5186] I might put it into a model.
[5187] I've externalized that thought.
[5190] When it comes to engineering design, all starts with a thought.
[5196] Right?
[5196] Can't find that thought in my brain.
[5199] Right?
[5200] Is that thought an instance?
[5203] Right?
[5204] Do I tie everything from the design?
[5208] Can I tie it to an instance of a thought?
[5210] Is that instance of a thought a thing?
[5213] Yes.
[5214] I don't know.
[5214] Oh, so yes.
[5215] We don't often go into the mental representations of consciousness or thoughts, but we certainly could.
[5223] There are mental qualities in hearing in your brain, the material thing in certain arrangements.
[5229] They can be the sorts of qualities that concretize information.
[5233] That's putatively about stuff in the world.
[5235] You have an idea, you have a blueprint.
[5237] It's a thought.
[5238] It's got that material thing, carrying information.
[5242] Some of that information you might want to convey to me.
[5244] You're talking into the microphone.
[5244] You convey it using your vocal cords as reverberation, all these particles with qualities, and they're transmitting this.
[5246] Ideally, I'll get it.
[5252] Yeah.
[5254] I want to put that instance of a thought of something that I had last night in the shower.
[5254] I want to put that into a database, an RDF.
[5261] I said, I had this thought yesterday, April 9 at some time.
[5265] Mhmm.
[5271] I thought about this new airplane design.
[5271] I have a temporal, a time stamp associated with that thought.
[5274] That thought then matures.
[5280] That thought then matures.
[5282] Right?
[5283] It's not the same thought.
[5284] It's matured over time.
[5285] Mhmm.
[5286] But I wanna capture that maturation of this thought that then became a piece of paper, that then became a CAD file.
[5293] That then became something I give to the manufacturer.
[5297] That then becomes something, material gets procured.
[5301] Yeah.
[5301] It then gets produced.
[5302] I want traceability of that there's all the way through.
[5307] That original thought that I had yesterday.
[5308] So, yeah, there's there's information that is common throughout.
[5312] There's information that has the same content.
[5314] Now that content can change in various ways, semantically.
[5318] Mhmm.
[5318] But assuming there's some kind of boundaries within a threshold within which it doesn't change outside of it.
[5325] It's a completely different thought.
[5327] You would judge it that way.
[5327] I would judge it that way.
[5329] But you can nevertheless maintain that there's a certain content, a specific content that might undergo this or that change as it matures through the workflow or through a brainstorming session or whatnot.
[5339] Sure.
[5340] What I want is that as that design matures from yesterday to tomorrow, next year, and the years following, a log of that change in information as it matures.
[5357] So that I can ask questions.
[5360] What happened?
[5361] I wanna do a difference.
[5362] Right?
[5362] I wanna do a difference.
[5364] Of design from two years in the future to what it is today.
[5368] Yeah.
[5369] Right?
[5369] Provenance of choice.
[5372] No physical entity.
[5373] And there's no this is what I was trying to get to.
[5375] Yeah.
[5375] There's a provenance of choices, am I gonna use Monte Carlo or Navier Stokes to analyze something?
[5382] There's a provenance of choice.
[5384] And those you wanna track those choices, and they may beget processes, like how I'm gonna analyze something, how I'm gonna test something.
[5393] Exactly right.
[5393] I know exactly what you're saying.
[5395] And I don't see that here because BFOs, as I learned reinforced today, may vary.
[5401] It's about physical things.
[5403] Things that don't realize.
[5404] It's because it's higher empirical data and it's also higher level than this.
[5412] Provenance is extension.
[5414] We like groundwork on which provenance would be tracked.
[5417] 7. 8.
[5417] Yeah.
[5418] Yeah.
[5418] You see this in common core or common annotations or Provo.
[5421] 11. And this stuff, now we have a mapping from Provo into BFO.
[5421] And this sort of stuff, and now we have a mapping from Provo into BFO.
[5425] This stuff you wouldn't properly put in BFO, but would be extended down through it.
[5430] Because what I found in workflow engineering workflows, there are activities without entities.
[5437] Agents have activities.
[5440] Yep.
[5441] And they may exist as a record, let's say, a record in a giant database that's not really a taggable entity by itself.
[5449] It doesn't stand alone or a thought in your head.
[5451] It's not an entity.
[5453] And yet when we're tracking provenance of decisions, I wanna do a reasoning.
[5460] Why did this guy's design methodology work better than this guy's methodology?
[5465] Correct.
[5466] That means every single decision, every attribute of the provenance is important.
[5471] That’s why I made that question about Provo.
[5474] I wanna stay in the BFO world.
[5476] Because ultimately, there are entities at a certain point.
[5480] Entities do get created and they fit into BFO.
[5484] But the process is what is interesting to me.
[5486] Yes.
[5487] Yeah.
[5487] Both.
[5488] Both the information and the processes, all of this can be tracked, and you can extend that from BFO.
[5494] There's a common framework.
[5495] It's a common framework, which many groups use.
[5497] There are several groups that extend it in different ways.
[5500] There are some people in DOD, and I see they use this comment annotation standard, which is not exactly the same as Provo, although inspired by folks outside in the open space often use Provo, which is why we have a mapping to it.
[5513] But all of this is on board, and we definitely want to recognize the needs for tracking both the information as it matures over time, also the processes involved, the processes that might be prescribed or described by that, all within scope.
[5526] Yeah.
[5527] I say all this having thought about it.
[5530] Mhmm.
[5532] From a practical standpoint, it's workable.
[5535] It's you're able to track that instance of a thought as it matures.
[5540] You can track it because you write it down.
[5543] Correct.
[5543] Right.
[5544] I can, if I want, I can say, "Hey."
[5547] I have an instance of this thing that I put as a named individual of an instance of something, that I can now query.
[5559] Right?
[5559] That's not an issue from a practical standpoint and putting it into a database.
[5567] Philosophically, I don't know.
[5570] I think we violently agree.
[5572] Yes.
[5574] There's a space.
[5575] Yeah.
[5576] Absolutely.
[5576] Yeah.
[5577] Can I add just one thing?
[5578] Because I think when we have a design and we have a model that has a different life, and I don't want to go to the configuration control, but when you go to the MSN, so there's a completely different life.
[5589] When you have the actual object and your model, they can be, there's the correlation on that, and you want you need to track that as well.
[5602] You're touching on that there's life cycle management of the information as it matures.
[5608] Right?
[5609] It is not just a physical product that we want to have a life cycle of.
[5613] We want to have a life cycle of information artifacts
[5619] I never said that this physical artifact exists during design.
[5623] No.
[5624] Put it in my mouth.
[5625] I never said that.
[5626] I said that we are designing something which may be a future artifact.
[5631] Uh-huh.
[5632] Simplifying the reasoning about that future artifact is simplified significantly if you make an instance of that in your model, and instantiating that future artifact would be ideal in an engine.
[5644] You can run simulations on that engine.
[5646] You can run Navios, talking patients, Monte Carlo simulation with properties, attributes, qualities of that artifact.
[5654] Answer questions.
[5655] What is the weight of that engine that you are designing?
[5661] Nonexistent.
[5662] But you are completely allowed to do that.
[5665] Yeah.
[5665] That it does instantiate once that thing.
[5670] That's what I'm saying.
[5671] So I'm not saying that this physical artifact exists today.
[5674] I'm saying you make a model of that artifact as an instance that you can reason in an engineering sense, whatever you need to make decisions that this is a performance and cost-effective solution.
[5687] You have many different alternatives to compare, design, and choose the best one to go forward.
[5694] That's what I'm saying.
[5695] I'm not saying this physical artifact exists today.
[5698] I understand I've been engineered for forty years.
[5702] Listen, I understand.
[5703] You are in scope of the paper.
[5707] We take your view into consideration.
[5709] We don't say we're speaking to this optimized query discussion you're bringing up, but I'll add it.
[5718] You're talking about the ease of reasoning using a dummy instance.
[5724] You don't need that.
[5726] You can do it at the type level, like we show.
[5728] You can write queries.
[5729] You can optimize your queries for this.
[5732] It's an information extraction question.
[5735] There are many ways to solve that.
[5736] You can introduce shackle shapes to modify your graph.
[5740] What I'm saying is, as a matter of the ontology, it is theoretically incorrect to say there's an instance, even a dummy instance, calling out to what the blueprint is supposed to be about.
[5756] All the practical motivation that might inform your judgment about whether to include such a thing can be done in different ways that don't put falsehoods in the mouths of engineers.
[5769] It's something that was worked out.
[5772] It's something we did in practice at APL.
[5774] When I worked there, we had the same problem.
[5776] We were often talking about stuff that didn't happen, simulations.
[5779] We're doing red teaming and cyber stuff.
[5781] Hope this doesn't happen.
[5783] We hope there's no instance calling after this simulation.
[5785] That's the plan.
[5786] That's the plan.
[5787] We had to figure out a way to do it.
[5789] I'm just saying, optimizing queries about this.
[5793] That's the easy part.
[5794] The hard part is making sure we don't put false words in the mouth of engineers.
[5795] They have the hard part to see.
[5798] The hard part is collecting the data.
[5800] Everybody has workflows to build things.
[5801] Everybody has workflows to build things, cars, planes, jets, whatever.
[5803] But very rarely do people write down their thoughts.
[5804] Everybody has workflows to build things.
[5807] You know?
[5807] Everybody has workflows to build things, cars, planes, jets, whatever.
[5811] But very rarely do people write down their thoughts.
[5814] Do they write down every process?
[5815] Do they have a grad student sitting next to them, entering into a chronological database?
[5820] The agent, the entity, the whatever.
[5824] We talk a lot about fit for purpose, and why I came to this meeting was I wanna be able to have that kind of information management querying.
[5835] Right?
[5835] I have software that does that in the workflow.
[5840] It logs and collects stuff.
[5842] But I need to instantiate it in a way through these ontologies that makes it kosher, that makes it able to be calculated on and those kinds of things, the history track.
[5853] So that I was looking at this as a gap until that paper came.
[5856] That paper just came out.
[5857] I sent that question to Barry, and it was great.
[5860] It was awesome.
[5861] You know?
[5861] So, anyway, that's real.
[5863] Hey.
[5863] I'll take compliments.
[5865] You guys want to give some more, I'll take them.
[5867] Hey.
[5868] I got a question.
[5870] I wanna rewind back to something that Alan said.
[5875] I'm sorry.
[5876] Is it the case that the thought you have and put to paper is a generically dependent continuant, and your mind is concretizing and the paper is concretizing?
[5889] So that thought is an information content entity.
[5893] The bearer of that thought is this brain matter happening.
[5893] I externalize that as sounds.
[5896] Things propagating through air.
[5900] It's transferable.
[5900] It's copyable.
[5900] I can put that on a piece of paper with ink.
[5906] That information is there.
[5910] The piece of paper is the bearer of that information.
[5911] There are various ways.
[5911] I could express the same content in different ways by architecting and crafting portions of information to convey meaning.
[5912] I can also put that on a piece of paper with ink.
[5915] That information is is there.
[5919] Right?
[5920] And and the piece of paper is the bearer of that information.
[5923] Right.
[5923] And there's various ways.
[5924] So different words you can use, sentences, modeling tools to express the same And I could express the same content in different ways by architecting and and crafting portions of information in different ways to convey some type of meaning.
[5940] Right?
[5940] So I can put it into sentences.
[5942] I can put it into a UML diagram.
[5945] I can use my words?
[5947] I'm architecting and using portions of information in a particular way to convey meaning to somebody else, whether it be a computer or another human.
[5959] It depends on how I architect it, depending on who the audience is, that I want that audience member to gain meaning.
[5967] Right?
[5968] That was a foundation for another question I wanted to ask.
[5971] Yep.
[5972] More to John or to Barry is, when a GDC changes, can a GDC change?
[5979] If it changes, does it produce a different GDC, or does the GDC change?
[5985] Yeah.
[5985] This is a fascinating question, I don't have fully characterized identity conditions for GDCs.
[5993] I want to respect the seemingly strong intuitions that folks have about there being some kind of identity conditions that allow for change the way an enduring thing might.
[6006] They are independent continuants.
[6007] I'm sorry.
[6008] They're not continuants or things that endure.
[6011] We should have criteria about which we allow material or whatnot changing, while persisting in their identity.
[6020] Where that threshold is is the tricky part.
[6023] If I make a change to a Word document, if I change the "to" to an "a" at the beginning of a sentence, is this new information?
[6032] That's a hard question.
[6034] Yeah.
[6034] Let me explain how this happened.
[6041] So there are various feeders into BFO.
[6043] One of them is Aristotle.
[6045] Another one is GIS treatment of space and time and so forth.
[6050] Another one is a Polish philosopher by the name of I see.
[6059] Another important influence was a Polish philosopher by the name of Roman Ingarden who wrote a book called The Literary Work of Art. It applies not just to literature, it applies also to newspaper articles or science texts or databases or any kind of information content entity.
[6078] So he started the life of information content entity ontology.
[6084] He had the idea that we have the text, which comes in instances, but it's a text of, let's say, a novel.
[6093] And the novel is the same.
[6094] It appears over and over again in printed books.
[6099] But a novel is more than just a text.
[6102] When you read a novel, you read about certain fictional characters.
[6106] Ali, you should leave the room for the next few minutes.
[6110] You read about fictional characters, and you read about their emotions and the places where they go and the wars they get involved in and so on.
[6117] But now we add, what is the literary work?
[6120] What is the literary work of art?
[6121] If we want to do justice to that, we need to take into account what happens when readers read a text because it's they who concretize the text.
[6131] Concretize is a technical term used by Palantir.
[6136] They haven't been reading Ingarden, but they may have been reading BFO.
[6141] The readers concretize this text, and now in the immediate post-publication phase, they'll concretize it in a sloppy way.
[6149] There won't be any patterns, but then gradually, people will learn how to read it properly.
[6154] What that means is that the concretization, which is generically dependent, dependent upon the brains of all the readers and on the text, over time, this concretization will have a life.
[6167] So GDCs can have a life.
[6169] If all the readers die and all the copies are destroyed, that GDC will cease to exist.
[6176] But so long as there are readers with brains who are concretizing the work, that concretization, which is the work for Ingarden.
[6185] We're not really interested in the text, we're interested in the text as a description of all of these going on, and it's that which has the aesthetic value.
[6194] If you read it badly, you lose the aesthetic value.
[6197] So that's my contribution.
[6198] Concretizations are things that can in principle have lives.
[6201] I think that works in the engineering case also.
[6206] The design will evolve.
[6210] It's the same design.
[6211] You still initiate it, but it's evolving nonetheless because it's then got to overcome the hurdles of physical realization.
[6212] Let me slip in another quick question that's on exactly this.
[6221] Can some GDCs be more generic than others?
[6224] The book of Harry Potter, it evolved in JK Rowling's mind, and as she told it to her children night after night, or until she wrote it down.
[6228] So is there a general Harry Potter story, a GDC that's somehow related to a more specific incarnation that is then concretized?
[6240] So is there a general Harry Potter story kind of a GDC that, that's somehow related to a more specific incarnation that is then concretized?
[6251] Check this out.
[6252] Alright.
[6252] You've got the information that's being conveyed by Rowling to her kids, and then ultimately is conveyed in books to millions of people worldwide.
[6259] So now if you're thinking about the genericness, what an interesting information content entity that you're using to measure the kind of count, as opposed to another.
[6273] So you can describe it that way.
[6274] You can describe it when the scope would be a foe in terms of genericness.
[6278] Now is it its own class up there on par with GDCs or constitutive of them?
[6284] No.
[6284] But you could construct it.
[6286] Right?
[6286] You can construct an instance that's about all of these instantiations.
[6291] You could create instances that are about other ins, information that's about information, as a descriptive matter.
[6296] That's within scope.
[6297] And we do this oftentimes with blueprints or processes.
[6301] We can describe the domain or the range of the information relation as it's sub.
[6309] Information content entity is a subclass of GDCs.
[6313] They're often in different extensions of a BFO.
[6316] The range is always entity to anything.
[6320] Yeah.
[6320] I think so the question of maturation of design.
[6324] Right?
[6325] I'm thinking that I could have an instance of just design of aircraft.
[6333] Right?
[6334] Then I could have an overarching one, and you're gonna have a conceptual design that I just thought about yesterday, and I have an instance of that.
[6344] Right?
[6345] Then I would have another instance today and another instance, another instance, another instance.
[6350] I think I need differences.
[6354] I think they each need to be an instance so that I can look at the past and see how it's changed.
[6361] But then the overall instance of a generalization of a design, I could say that this overall generalized design is about, or I don't know if it's vice versa, but this has a is about each of the instances that mature over time, I think.
[6383] I think we can extend this to the actual life cycle of aircraft production.
[6389] You build an aircraft of a certain mark.
[6393] I don't know what the technical terms are here.
[6395] Then you produce mark two.
[6397] It's the same underlying framework, then you produce mark three.
[6402] By mark five, you find that you need to make so many changes.
[6407] All of the aircraft produced so far are instances of aircraft type one, Mach one, but now you need an aircraft type two because you've made so many changes.
[6418] You're in a different world.
[6419] You start again as it were.
[6421] I don't know if that makes sense to say that you do that also prior to production where you have a design which goes through multiple phases, maybe in different shops which are more critical and focus on different aspects, you can still recognize that it's the design for the same aircraft, but it's going through phases which are demarcated in ways corresponding to what people now believe about what the production process will look like.
[6450] Just as a confirmation for what you said, would you treat, for example, an equation, a mathematical equation the same, but and its graph?
[6464] For example, the book series of tokens, Lord of the Rings versus the comic books, would you treat them in the same way that you just described?
[6474] Because, technically, they are about the same thing.
[6476] I know you would.
[6477] We have not trodden very far into these domains, but I think you're on I would.
[6488] I'm leaving the field entirely open.
[6493] So yes.
[6494] Yeah.
[6494] Okay.
[6495] Good.
[6496] He said yes.
[6499] Can I get to a comment with respect to Jim's question?
[6502] Can GDC if I see change in what's Yes.
[6505] Of course.
[6505] They can.
[6506] Yeah.
[6506] We have a good example.
[6508] Since GDC, I see is Kevin making multiple copies, as you said, in books.
[6514] So if you change one of them, if somebody goes and crosses out one word and says both of them exist.
[6521] Yeah.
[6522] So In practical well, let me finish.
[6523] In the practical world, for example, gentleman, I don't know your name.
[6527] Sorry.
[6528] If you give an example of an engineering design, I can decide that I don't want to take this design anymore.
[6534] I just delete all files about the design, and this design ceases to exist. I may create a new one.
[6542] The point is if changing or ceasing existence is related to how many other artifacts where it is realized exist.
[6554] If there is more than one, it doesn't.
[6557] If an orchestra is the only one, it disappears.
[6560] If an orchestra performs Beethoven's Seventh Symphony and makes one mistake, one trumpet sound, does that mean it's not a performance of Beethoven's Seventh Symphony?
[6575] The answer to this question is don't talk about philosophically interesting examples.
[6582] Talk about examples which are genuinely important for understanding things like engineering production.
[6589] I think that what we're missing in a discussion of engineering and simulation is it's a super duper multiscale thing.
[6600] We look at it as a workflow from start to end, either ending in something that's going to get built or something that's not going to get built.
[6611] There's a zillion things, wind tunnel tests, material tests, flight tests, cards, loads, all of that, and it's never deleted.
[6623] That's a company asset because somebody will come back ten years from now and say, did we have any Mach seven tests?
[6630] I used data from 1995 that was exactly what I needed for hypersonics.
[6635] This is the complexity of engineering, and there was a talk yesterday, or two days ago, that said simulation is not branching.
[6646] It's these parallel worlds.
[6648] That's untrue.
[6649] The simulated design is branching a zillion branches.
[6653] There are decisions made at every point.
[6656] Everybody wants to encapsulate that, and at least today, there is not one simulation of an aircraft.
[6663] I don't care if it's commercial or defense.
[6665] There's a zillion of them because they're role based, they're requirement based.
[6670] That reality is what we're trying to capture here.
[6674] The way that I'm looking at it is the existing system works.
[6680] How can we map it into ontology?
[6683] Like I said, that's where that paper created that bridge for me for provenance because it's really provenance with all the annotation, and we look at it as every node in that workflow has a graph hanging off it, which is the BFO based ontology.
[6701] But the steps that you go through because you make a decision.
[6704] Do I even have to go do loads for this?
[6707] There's a zillion it's vast when you look at a real design.
[6713] Yeah.
[6714] This is I just did a time check and I wanna ask, did we get through all the questions that people gave us?
[6720] No.
[6722] We had better spend some time on that.
[6725] Are there any final thoughts about this thread?
[6728] I do have some final thoughts.
[6729] I just wanna say that Iris, what you're saying is absolutely correct.
[6733] On the point of identity conditions for information, it's a very interesting philosophical topic, whether you change a word or whatnot or miss a note for sure.
[6743] What I think what Barry is pointing at is those really aren't the sorts of questions that we have to have firm conditions or constraints on when we're doing the high level modeling.
[6754] That doesn't mean there aren't firm constraints that come from requirements, solicitation, competency questions, and whatnot that come from the domain.
[6761] They're on the ground just as you're describing.
[6763] We take that and try to find what's common, whatever words we use.
[6769] The words don't matter.
[6770] We're not doing linguistics.
[6771] We're trying to provide a common structure across all those cases with general, and then provide you the resources under which you can fit your various characterizations, whether it's this company, this company, or not.
[6782] We're trying to solve interoperability problems and see what's common across them even if they have specific differences structurally on the ground.
[6789] That's why I came here.
[6790] It was great, all this trouble.
[6792] I love it.
[6792] No.
[6793] It's not trouble.
[6795] Yeah.
[6797] For a point, I think you made a very good point and that's what I was trying to say on Tuesday.
[6803] It's seven and a half years of development, so we need to have traceability, but when we address this problem and the example that I explained, the complexity is so big because we're trying to open that option to our engineers.
[6823] The key decisions, that's the thing that I want traceability from.
[6830] And that's the goal.
[6832] Yes.
[6832] We can use these tools.
[6834] Yes.
[6835] Yes.
[6835] This is the most important thing.
[6837] Yes.
[6837] In the last of these programs, let's spend more money there.
[6841] Yes.
[6843] Yeah.
[6844] Exactly.
[6844] Exactly.
[6845] Yeah.
[6845] I didn't make that decision.
[6846] Yes.
[6846] What was the rationale behind that decision?
[6849] Then I can start testing.
[6851] Supposed to go through some questions.
[6854] Is Milosz in the room?
[6856] Yes.
[6856] Hello, Milosz.
[6856] So Milosz is the only person whose questions I have answers to.
[6858] So we talked a lot about process profiles and process characteristics.
[6867] This is a summary in response to Milosz.
[6871] This is a summary in response to Milosz.
[6876] Process characteristic means any adjectival phrase treated as if it represented something in reality.
[6884] When you use an adjectival phrase in a true sentence about a process.
[6891] A process profile is a change within a process along a certain axis, for instance, temperature or color or whatever it might be.
[6902] With the relation between process characteristics and processes and process profiles themselves, we're working on it.
[6913] As you can see, we think we're making some progress, but it's difficult territory.
[6920] Where this all started was the following.
[6926] There is a very important area where we have many important process characteristics, which have a very important role in all kinds of engineering contexts.
[6939] They are process characteristics which involve the idea of rate or rate of change.
[6945] So they include things like velocity, acceleration, output rate, illness rate among the personnel, rate of fault detection in machines and so on.
[6959] Rates are everywhere in the world of processes, and it makes sense that we should find a way of treating rates ontologically, within a BFO consistent framework.
[6972] We do not have that yet.
[6973] I tried to convert this—this is the differential calculus, but it's a differential calculus generalized to include things like rate of hamburger production by this kitchen in October.
[6986] That's not really a mathematical question, but you need the differential calculus to understand any kind of rate, and I didn't succeed.
[6995] I have a degree in mathematics, but I did not succeed in getting something which looked like useful ontology content.
[7003] I've not forgotten about this, and the introduction of the phrase process characteristic is a first step toward having the possibility of describing rates in a BFO framework.
[7018] Now we have participation.
[7023] I'll read Maileth's question.
[7025] Is participation the appropriate relation to indicate dependency of process profile on a particular material entity?
[7032] The problem here goes back to the plant which goes from being green to being brown.
[7038] Is the color the thing which participates in that process profile, or is it the plant?
[7045] Our answer is part of BFO. It forces you to choose the answer.
[7051] The answer is the plant.
[7052] The plant is to participate in the process profile.
[7057] Plant is the participant in the process profile because the participant is the participant in the process as a whole.
[7065] If you say, let's suppose we just take this leaf and consider its color change process profile, then it would be the leaf which is the participant.
[7077] It's still a material entity.
[7078] It's still an object because that's what BFO says it has to be.
[7082] BFO forces you to say certain things, which is good because it means we're all forced along the same lines, so we don't fall in all directions.
[7092] But it's painful because that makes you think, which is painful for some people.
[7096] Alright.
[7098] Is participation even the right relation?
[7102] There are issues like processes of handover.
[7108] Can a process profile be such that there is a shift in participant along the way?
[7114] The example I came up with is when you have a production, a factory, there is an output of that production which can be described using process profile terms, and now the crew changes from the morning to the afternoon.
[7129] Can we then have a process profile which has the same process profile which has different participants at different times?
[7136] I don't see why not, and this is an example where it seems that that would be the case.
[7141] This is a really big question, and that means I don't have an answer.
[7150] I was still and I wrote one down.
[7155] John made this. John is on a phone call.
[7159] There are two worlds in which we live.
[7162] There's one world, which is the mathematically describable world where processes have a first instant, meaning a zero length time interval, a time interval which has zero length, and the last instant.
[7179] That's one world.
[7180] Then there is the common sense world where starting the race may take four seconds, but we don't know.
[7187] We don't measure it.
[7188] We know the race started.
[7189] We know the race ended, so we don't really care precisely when it started and precisely where it ended.
[7194] Same goes for death.
[7196] So when the surgeon calls the time of death, they're creating a time of death which is fake because no one knows exactly when the death occurred.
[7207] So there are two worlds, the instantaneous respecting world and the vague starting ending world.
[7214] BFO has to deal with both.
[7216] I don't think it does very well yet, but it provides all you need because it provides its time instant and time interval, which is what we're talking about here.
[7227] Most of what we know about is time intervals.
[7229] It's very rare that we really know about time instance, but it's very useful to have time instance for surgical cases where it may hinge on whether he died on Wednesday or Tuesday, who inherits his fortune.
[7244] I don't know.
[7247] Instant.
[7249] I've only been talking about instants in the last minute and a half.
[7254] Exactly.
[7256] Alright.
[7257] Now so what I say is all uses of first and last instant in the BFO sense are about zero length time regions.
[7275] But most use of time specifications in the real world is vague.
[7283] Alright.
[7283] Now another big problem, and I really haven't been following IOS treatment of plans.
[7289] So can someone tell me, does IOF treat the plan as being identical to the plan specification, or is the written version of the plan a GDC?
[7300] Or does it treat the plan as being something in the head of the manager?
[7306] Okay.
[7307] One of which is called plan specification.
[7319] Okay.
[7319] So a plan is a plan specification.
[7322] Good.
[7322] Alright.
[7323] Now we have the same problem between design and design specification.
[7330] So I don't know.
[7334] There are designers in the room, they should help me make this call.
[7340] So the same problem arose in the IOF core, and the decision was made not to care.
[7347] In other words, we call it plan, and we mean either plan in the head of the manager or the plan as specified on paper.
[7354] You should know about this because you have this idea in your head.
[7357] Notice that I did not use the word "concept," and neither did you, which is fantastic.
[7363] But now do you distinguish between the design and the design specification?
[7372] Yeah.
[7374] First thought in my mind was that to my mind, a design specification is something that is now actionable.
[7382] Right?
[7383] So somebody can now execute a design.
[7387] Right?
[7387] A design in general could be executable or not.
[7393] Right?
[7393] Is this a bit the difference between Tolstoy's manuscript and the published novel?
[7403] The original design may not be economically or viably or physically able to do today, and a new technique a month from now may make it viable to go back to the original design and come up with a different plan of how to implement it.
[7418] My guess is that we need to punt on this because we don't care.
[7426] In general, we don't care.
[7427] There'll be specific cases where we do care.
[7429] Do you want to say something about this?
[7431] Yeah.
[7431] I was gonna say the same thing, but also again because it comes up a lot, despite the fact that I just said this.
[7438] We're not linguists.
[7442] What does it mean?
[7442] You tell us.
[7443] We describe the common structure.
[7445] Design versus design specification.
[7447] Don't let your theoretical intuitions import into a general structure.
[7453] It's sometimes important to capture the designer's thought.
[7459] Yeah.
[7459] Because this may not be economically viable to him.
[7463] But we're to be exported.
[7466] Otherwise, the supplier is gone.
[7469] Correct.
[7472] In the software world, things are changing so fast that what's not viable today is definitely viable a month from now.
[7481] So I'd like to go to number four since we have very little time.
[7484] So we've been talking about roles of designs for if it's actionable then.
[7493] So that means that you are assigning a role to a GDC.
[7498] Now we don't have roles of GDCs in BFO, only objects can have roles.
[7505] But you're against roles of GDCs?
[7509] I'm in favor.
[7510] Okay.
[7511] So who is against?
[7513] I don't think anybody is against.
[7515] It's just, you can, the line is you no?
[7519] I said I'm in favor.
[7520] Yeah.
[7521] I said I'm in favor.
[7522] So the motivating case I see is, if I'm talking about arguments, so God exists, therefore God exists.
[7528] What's the difference between what's going on?
[7530] The same content and the premise and conclusion.
[7532] They occupy different roles in an argument context.
[7535] That's a good case to me.
[7537] The opponents, I think the only opposition I've seen is not opposition to GDCs having roles.
[7543] It's more that you can say that BFO without having GDCs bear roles.
[7548] I could everything I just said about that context, you could specify in terms of the inputs and outputs of processes of inferring or asserting.
[7557] You can spell out the different places that So in other words, you are against it because you think we don't need it.
[7564] No.
[7565] I'm not against it.
[7565] David is against it?
[7567] David Limbaugh.
[7567] Limbo.
[7568] What's his reason?
[7569] That's why.
[7570] He said you can reduce it away.
[7572] You can reduce it away and So some people criticize BFO because it moves slowly and officially we just didn't have this conversation.
[7590] Maybe we will change that, but we're at a stage where there are so many people involved with their peccadilloes and their urgent needs and their government mandates that we really have to work things through with different audiences until we reach the point where we find workable solutions, which will do justice to at least many of our stakeholders.
[7616] We need to wrap up because we're cutting into the break, and then we have to start another session at 11:20.
[7622] Okay.
[7622] Let's begin.
[7635] I'm going to continue where we left off.
[7638] Anyone who doesn't want to stay in the room can leave, but people shouldn't have conversations too loud while I'm trying to do this.
[7652] I'll pick up where John left off regarding the contents in the slides.
[7660] This just repeats what he says, but it gives it in a more visual way.
[7666] Arco should like it.
[7670] Arco still here?
[7673] Okay.
[7673] Never mind.
[7675] Let me continue.
[7681] Can you all hear me?
[7683] The idea is that when we're dealing with things like molecules or people, we know that they change qualities, so we need to have words or terms in our ontology to represent those qualities.
[7696] Processes do not change.
[7699] When we're dealing with objects, we can think of ourselves as being in a world where we are looking at objects.
[7705] They survive.
[7706] They endure through time.
[7708] When we're dealing with processes, we can't do that because we only ever see an instantaneous tiny slice of a process.
[7716] What we need to do is to become God, look down at the process world from a God's eye perspective, and then all processes are already there in their full extent.
[7729] We think that they're changing, but in fact, God knows that I was already going to do this with my hands from the very beginning of my beginning to talk.
[7741] From the God's eye perspective, the process is always there.
[7745] It doesn't change.
[7746] If I decide to do something else with my hands, nothing has changed because God knows that I would put my hands behind my back at this very moment.
[7755] That's the workable way of dealing with ontology with objects and processes in the same ontology.
[7766] We have to imagine two worldviews.
[7768] One is what we used to call the snap worldview because we take pictures, then the span worldview where we look at whole videos.
[7778] Alright.
[7778] That means we don't need any extra entities called qualities, but we need to talk about processes as speeding up or slowing down or being interrupted or being repeated.
[7790] We have introduced the facility to talk about processes in those terms by introducing the term characteristic, which is just an analog of quality in the process world, but which is merely an abbreviation for a more complicated story.
[7815] Then there are no instances of these process characteristics.
[7820] There are instances of qualities always, but it doesn't make sense to say that process characteristics exist because talk of process characteristics is merely an abbreviation for talking about processes and process profiles.
[7835] Alright.
[7836] Another way of putting this is characteristics are defined classes.
[7842] If there are many areas within an ontology like BFO where we need to introduce abbreviations.
[7850] An example would be the term pet, which is an abbreviation for either a dog or a cat or a fish or a cockatoo or a piece of stone or anything that you treat as a pet.
[7865] There is no universal pet.
[7868] It's an abbreviation of a long disjunctive list beginning with cat, dog, cockatoo, and so on.
[7878] But it's useful to have this abbreviation, and there are many other abbreviations that we need to use in tandem with BFO.
[7885] Because they're abbreviations, they're a matter of language.
[7888] They don't belong in the hierarchy.
[7890] They're neither continuants nor occurrents because they're not anything.
[7895] They're just ways of talking.
[7898] Alright.
[7899] Now we need to give people guidance when they're dealing with a real universal or whether they're dealing with a defined class.
[7908] I don't have that full guidance here.
[7912] Both defined classes and universals have definitions.
[7918] So the terminology of defined classes is somewhat confusing.
[7922] But people have got used to it.
[7924] We're not going to eliminate it now.
[7925] It's not an official part of BFO.
[7928] It's part of BFO implementation strategy, namely, use abbreviations when you need them.
[7937] Alright.
[7937] Now defined classes are different from universals, which are classes in the strict sense.
[7943] One subtype of universal we discussed this morning, they are the types which Dusan invents in his laboratory and hopes that he will have instances one day.
[7956] They are genuine universals already today, providing Dusan has a relevant power and so on and resources and everything.
[7966] Now every genuine class must be reachable from the root of the ontology by a process of single inheritance is our relations.
[7978] Pet is not reachable because there are several roots.
[7983] So there are fish which go through I don't know what's the next thing in the tree of life?
[7990] Swimming thing.
[7992] The fish and then there's cat.
[7994] Cat is a subtype of mammal.
[7996] Fish is not a subtype of mammal.
[7999] There is no single unique continuous path from pet to object, although all pets are objects.
[8011] Ali.
[8023] There are all kinds of ways of treating things.
[8026] It's not a problem.
[8027] It's nice to have the defined class pet, that people like pets.
[8032] There are pet shops.
[8037] I anyway.
[8041] We talked about this.
[8043] We'll call it the no sudden death criterion, although I'm not fixed on that terminology.
[8048] Dog is a universal child.
[8050] It's not a universal because something can cease to be a child without ceasing to exist.
[8055] The same goes for human versus manager and so forth.
[8059] One important stepping stone in the development of ontologies since the millennium is the idea, which was invented by Aristotle, that when you're building definitions of terms in an ontology, you should use what are called Aristotelian or two-part definitions.
[8080] An example would be a human is a rational animal.
[8085] Every human is an animal which is rational.
[8089] All your definitions of terms should look like that.
[8092] They have two parts.
[8093] The second part can be rather complicated.
[8095] It can have multiple constituent phrases, but the basic idea is you use b as a which sees.
[8105] If you do that, you guarantee single inheritance in the sense that if you do not have single inheritance, you will not know which route upwards to follow.
[8117] We may have a car, which is a blue car, which is also a Ford Pinto.
[8123] What is the parent that is relevant for car?
[8127] You might think that it is a blue car.
[8128] You do not even know that it is a Ford Pinto.
[8131] The only root of the tree which adheres to the no sudden death principle is the Ford Pinto car because you can repaint your car, then it becomes a red car, but it does not thereby cease to exist.
[8147] The no sudden death principle guides you in problematic cases.
[8152] Another case which is famous in the history of medical ontology is meningitis.
[8160] Meningitis is an infectious disease, and meningitis is a disease of the meninges.
[8167] Both of those are perfectly good terms in a medical ontology.
[8171] So which is the parent of meningitis?
[8174] How many people think that infectious disease is an appropriate parent?
[8180] How many people think that disease of the meninges is an appropriate parent?
[8185] You are all really unthinking louts.
[8192] I want volunteers at least.
[8195] John, you know everything.
[8197] What?
[8199] I will go with infection.
[8200] No.
[8200] You are both wrong.
[8204] There is a way of turning meningitis into a noninfectious disease.
[8210] The meningitis doesn't go away, but its infectious character doesn't go away.
[8215] You can't turn meningitis into a disease of the earlobe.
[8221] It's a disease of the meninges.
[8225] You get special points for being bereaved, and then I delete most of those points because you got the wrong answer.
[8238] No.
[8239] No.
[8239] I wanted a parent.
[8249] Yeah.
[8250] That's fine.
[8250] That's fine.
[8251] That wouldn't be its parent in the ontology.
[8253] Yeah.
[8253] Yeah.
[8253] That's it.
[8254] Yeah.
[8254] I get all.
[8258] I'll give you three quarters.
[8260] In a world where people are all immune to meningitis.
[8271] Would meningitis disease not be a disease in that world?
[8276] No.
[8277] In that world, meningitis is noninfectious.
[8283] There are many diseases that you can apply in some cases of meningitis, which remove the infectious character.
[8291] You still have the meningitis, but it's not long term.
[8294] Not a disease anymore in that world?
[8295] There are all kinds of other things wrong with meningitis other than its being infectious.
[8301] You don't want to have meningitis.
[8304] Oh, of course.
[8305] But what I'm saying is that you can also imagine a world in which every single human being is immune to it or every living being is immune to it.
[8312] So therefore, it's just not a disease at that point.
[8315] So that's an interesting sure.
[8317] Yeah.
[8319] No.
[8319] I know.
[8320] But at the same time, I'm saying you can question the fact that it's infectious.
[8324] I'm just saying you can also question the fact that it's a disease.
[8326] Okay.
[8327] Good.
[8327] So how much change do we want in order to change the definition?
[8331] We have the law that if you have one instance or had one instance or prospectively in Dusan's world will have an instance, then it's a universal, or rather every universe has had or prospectively will have an incident.
[8348] Meningitis, if meningitis existed in the world at any time, then it's a disease at every time because it's a universal and it's a child of the universal disease.
[8363] If it goes away because we have really strong AI that can cure cancer and make you immortal, which we will have before long, said David Chang.
[8373] You're saying that it's infectious only because we can pass it to one another.
[8373] No.
[8382] No.
[8382] Well, I'm also no.
[8383] What is it?
[8383] That's not right.
[8384] Certain pathogens are infectious because of their dispositions to be transmitted as part of their life cycle like a virus.
[8385] Yeah.
[8386] Yeah.
[8393] Yeah.
[8393] Yeah.
[8393] That's not about you.
[8393] You could be inoculated or whatnot or be vaccinated, but this is not about still an infectious disease.
[8393] Still infectious disease.
[8394] Well, it's yeah.
[8400] It's an infectious pathogen, and that may manifest an infectious disease if you have the appropriate abnormalities if it had been transmitted.
[8401] Well, it's yeah.
[8402] It's an infectious pathogen, and that may manifest an infectious disease if you have the appropriate, like, abnormalities if it had been transmitted.
[8410] But if it's not, the thing that that parasite, that pathogen itself is infectious, it just can't get through you.
[8419] So now how do we deal with defined classes when we're doing ontology building using Protege, for instance?
[8420] Well, the answer is that you don't in your asserted version of the ontology, the version that you keep close to your heart.
[8421] Protege gives you the two views.
[8427] On the one hand, there is the asserted version, the editor's version, the version that wears the trousers, and then you have the inferred version.
[8437] The inferred version is what you get when you add the definitions of your defined classes.
[8440] You suddenly have multiple parentage.
[8450] You have more spaghetti, probably bring down Arco's tramp plant thing, but that you can still find that useful.
[8454] People find multiple inheritance very often, for instance, when dealing with meningitis useful because you don't want to forget that it's an infectious disease.
[8456] So that's how you deal with this problem if you're using Protege.
[8465] You keep your asserted classes close to your heart, and you use the defined classes for the sake of convenience.
[8474] Now that I wrote this paper a long time ago on process profiles, and it was part of my effort to work out how to deal with rate data.
[8478] So I spent years trying to find a way of dealing with rate data in a world in which processes do not change.
[8489] So we have a process of running, which is p.
[8502] Now the first problem is that p is going to be an instance of multiple universes one way or another.
[8509] So it's going to be a running process.
[8514] It's going to be a fast running process.
[8523] It's going to be a running process with a certain duration.
[8526] It's going to be a fast running process.
[8528] It's going to be a running process with a certain duration.
[8531] It's going to be a running process, which involves motion.
[8536] It's going to involve displacement in space.
[8541] It's going to use up energy.
[8543] It's going to use up oxygen and so on.
[8545] Now all of those are facts about the running process.
[8550] And a good example of the kind of problem that we face now is the spinning top.
[8559] So there when you spin a spinning top, you initiate two processes.
[8563] One is a spinning process, but the spinning top gradually gets warmer.
[8568] It is a heating process.
[8570] So we have a process of increasing temperature, and we have a process of spinning, and they occupy exactly the same region of space time.
[8580] Exactly.
[8582] And so we need a way of dealing with that, and this was the birth of the idea of process profiles.
[8589] What we have here is a spinning process profile and a warming profile, and they both exist in the same space and the same time with the same participant.
[8601] And that's what we have here.
[8603] So we have measuring devices which tell us that this particular running process has these characteristics.
[8612] That's because there are these four process profiles and many more process profiles.
[8619] And so that's where we get some kind of relevance to engineering.
[8624] In an engineering context, we're dealing with multiple measurable process profiles.
[8632] And we just think we're dealing with processes, and that's true because every process profile is a process, but a process profile is usually measurable.
[8643] Sometimes it's not; the red, brown, plant process profile is not measurable so directly, but most of the process profiles that will matter in engineering are going to be measurable ones.
[8656] So what does a temperature chart represent?
[8657] It doesn't represent the molecules moving around in Ringo when he gets warmer.
[8660] It measures the temperature, which is a certain measurable feature.
[8666] The change in temperature is a process profile, a temperature process profile, or a quality process profile geared to the quality of temperature.
[8671] Then we get vibration level.
[8685] This is an engineering example.
[8687] The vibration level changes over time, and you can graph it.
[8690] The vibration level in an engine or a machine is a process profile candidate because we can measure it.
[8695] We can assign likelihoods to it and so forth.
[8706] The Dow Jones Industrial Average represents a process profile, so this diagram represents what happened here.
[8709] What happened here is much more complicated than what we would think if we just look here, but this is a very useful representation of a process profile, which captures what is important from some perspectives about what's going on in here.
[8717] There are other things going on here which would be important to some people, but for most people, it's that which is important.
[8733] Again, it's a measurable slice through a complex process.
[8740] Every time series graph is a representation of a process profile.
[8745] I had one question.
[8755] Yeah.
[8757] Would the environmental requirements be part of the process profile?
[8757] If there's no gravity, your spinning top doesn't work.
[8763] If there's no oxygen available for it to operate on, does that become part of the profile or outside of it?
[8766] There is a sense in which when we start doing process profile related work.
[8782] We are dislocating it ourselves from questions of causality, environment, finickiness of the relevant day, the weather.
[8792] We're only interested in this slice of reality, which is Ringo's temperature or the Dow Jones yesterday, or we're not interested in anything else.
[8803] Now if you start doing ontology about process profiles, then you might very well be interested in the environment.
[8810] So what happened at that time, which made the DAO crash by all those dollars, I suppose, and then you need to go out into the environment, but the process profile itself lives in process profile land, which is a very slim, deliberately a very slim impression created by the world when we impose measurement.
[8836] And this creates a whole series of philosophical questions.
[8843] And I hate philosophical questions, but I've got this far.
[8846] I will continue.
[8847] Plato talks about a slave boy, and he got a slave boy to prove Pythagoras' theorem by means of making lines in the sand with a stick.
[8859] So he drew a triangle.
[8861] And then Plato's question this is a philosophical question now.
[8865] Did the triangle, which the boy drew in the sand exist before he drew it, or did he create it?
[8875] That's a philosophical question.
[8876] There's no answer.
[8880] Now did we create the temperature process profile class?
[8887] The class these are classes.
[8888] They're universals.
[8889] When we invented temperature measurements, or were there corresponding changes in Ringo's temperature, which we can now represent in a graph before we created the unit of measure or the units of measure?
[8903] And it's a philosophical question.
[8906] There is no answer to it, but it's a good question to have in the back of your mind because it makes you think about the nature of units of measure and so forth.
[8914] Now, of course, with the Dow Jones Industrial Average, did that exist before Dow and Jones sat down and did some thinking?
[8925] In one sense, no, because they created this work of art.
[8931] But in another sense, yes, because the stock exchange existed, and it was doing all of those things.
[8935] And you can calculate retrospectively the Dow Jones average on every day that the stock exchange existed, I assume.
[8945] Well, anyway, I'm guessing.
[8948] Yes.
[8948] I do have a question.
[8949] So let's take the Dow Jones example.
[8952] Process is stock market trading.
[8955] Right?
[8956] Yeah.
[8956] And you have measurements of the chart that you showed.
[8959] Yeah.
[8960] And this is profit process profile of that trading process.
[8963] Yeah.
[8964] So are you talking about two processes since process profile is subclass of process?
[8968] Are we talking about two processes or one process?
[8971] So the Dow Jones Industrial Average process profile is one process within a much richer and complicated process, which includes lots of people buying and selling and reporting and gossiping and all the other things they do to influence the changes in the stock market.
[8993] The big fat, ugly, full process profile is measurement of some process.
[8998] Measurement focused views on complicated process.
[9001] So two processes exist?
[9003] At least the full process exists, and the process profile exists.
[9008] A lot of typing, a lot of sending signals wirelessly.
[9014] So earlier I said that the generically dependent continuant includes some of the most important things in reality, like poems and symphonies and works of literature and the Dow Jones Industrial Average and so forth.
[9015] The movements of the Dow Jones Industrial Average are a process profile, but the Dow Jones Industrial Average itself is a creation, and like writing a novel, creation on multiple levels.
[9032] All speech is like that.
[9044] If you measure what's going on when we speak, you have acoustic signals, you have neurological activities in people's brains, you have the signals themselves, which are measured acoustically.
[9047] All of these lines in these three, the two graphs, representations of process profiles.
[9061] If you add the speech itself, that is another process profile within this big, fat, ugly process, which is called a human being speaking, which involves me spitting, pushing air through my diaphragm, pushing air through my lungs, arms waving all the time.
[9068] Diaphragm pushing air through my lungs, arms waving all the time.
[9086] Speech is a process probe, and that's what it says here.
[9094] Conscious mental processes, so having ideas about aerospace manufacture, that is a process profile, which is dependent on all kinds of changes in your brain, primarily.
[9102] It's an intuitive definition.
[9119] We can do better than this, I believe, but we don't want to commit to anything better until we've worked out what we should commit to.
[9120] That takes a lot of arguing.
[9124] One of the reasons why BFO is the way that it is is because we have quite a number of argumentative philosophers who just like arguing, and so we have to find out how to keep them quiet.
[9131] You can look at that.
[9133] It's repeating what I just said.
[9150] Yes?
[9152] It's basically repeating what I just said.
[9154] Yes?
[9168] Yeah.
[9170] You can slice up the process profile into temporal bits.
[9173] That would be a proper current part.
[9176] If you want a proper continuing part, I guess we can do this.
[9184] I'll cheat for a minute.
[9185] All the parts of Ringo's temperature process profile when Ringo's temperature was greater than 30 degrees Celsius would give you a gappy process profile.
[9201] Is what?
[9203] Yeah.
[9203] Yeah.
[9203] I know.
[9204] But we could say that the gaps are part of the process profile as long as it's starting and ending point.
[9210] This is one of the areas where we have not. If every process profile is a process and a process must have parts, what are the parts of the process? We say processes must have temporal parts.
[9222] I don't believe that we say processes must have, what's the word?
[9229] I think it's proper or current part.
[9232] So a current part, temporal parts are slices in time.
[9236] Current parts are parts which can be extended in time.
[9241] Let's suppose we have the process profile. I think that we do not claim that every process must have a current proper path.
[9257] We say that every process has proper temporal parts because we want to distinguish between a process, which is extended, and a process boundary, which is the beginning or the ending of a process.
[9269] But I don't believe that we say that every process.
[9272] I'll double check.
[9272] I read it in Double Check.
[9274] Yeah.
[9275] For the meaning of difference in the right school.
[9277] Means I don't quite know if this is right or if this is this. I'm not perfect, so sometimes I wave my hands.
[9287] I never use sneer quotes, but Todd isn't here now.
[9289] So that's alright.
[9291] So now how does BFO deal with rate day data?
[9294] Now we come to Milosz's question.
[9296] Can answer real quick?
[9298] So I think I did this this morning, didn't I?
[9301] Yes.
[9301] I do have an answer.
[9302] I just looked it up.
[9304] Process, and I don't know if this is coming from BFO or from the core, but every process has a current part.
[9312] Oh, it's only.
[9314] Uh-huh.
[9314] It's an only.
[9315] Okay.
[9315] Alright.
[9316] Alright.
[9316] Good.
[9318] Say sorry.
[9319] Can you start again, Milos?
[9328] Yeah.
[9332] Yeah.
[9333] What Jim did is so quick.
[9339] So alright.
[9342] I need to do this more often so that I have the response more quickly in my mind.
[9349] So let me try again with the answer to Milosz 1.2.
[9357] Every process, every complicated process, every interesting process which we're likely to be measuring is going to have a process profile.
[9368] We very often want to talk about those processes.
[9372] One says that ringos tend to be increasing.
[9375] When we say that, what makes what we say true is the process profile, and also the process which the process profile is contained in, but that's redundant.
[9387] So the process profile is enough to make it true.
[9390] The ringo's temperature is increasing.
[9393] That is a characteristic, the increasingness.
[9397] That it is increasing.
[9399] The ringo temperature is increasing.
[9400] Our ringo temperature increased yesterday.
[9403] These are uses of the term process characteristic, which are convenient abbreviations for references to the corresponding process profile.
[9416] Many characteristics will be like that.
[9418] Not all, but many.
[9419] The zigzag process, interrupted process, repeated process, these all rely on something like yes.
[9441] No, I think they will have neuro numerical measurements.
[9445] For instance, we might want to say that John was running with a constant velocity of 11 feet per second.
[9455] He only has two feet, if he were a centipede.
[9462] I don't see any harm in having numbers in a person's characteristics.
[9468] When you say this is characterizing of the profile.
[9478] My speed profile is such that I can say I drove in a moderate speed of some.
[9488] The moderate speed numerically considered as 50 miles per hour.
[9497] Yeah.
[9497] I want to say I am driving in a moderate speed because my average speed is 60 miles per hour.
[9507] BAFO is there in order to create interoperability between different bodies of empirical data.
[9517] The police is following you when you're driving over the speed limit or when you're driving too slowly and thereby creating data.
[9528] We should concentrate on that starting point, not on I'm driving at a moderate speed because that's not empirical data.
[9540] Let me try this again.
[9542] The reason why it makes sense to talk about the God's eye view when dealing with processes is because when we're dealing with processes in a database, the data is always retrospective.
[9556] This is probably false empirically, but we don't have data about what's happening when we're collecting the data.
[9566] There's always some kind of temporal gap there.
[9573] Trying to find the relationship between the profile and the characteristics.
[9578] Yeah.
[9579] I average speed 60, but the average speed itself is a profile because that can change.
[9586] I can plot the average speed.
[9589] That can be as well.
[9590] You could have an average speed process profile.
[9593] You have to define it mathematically, but you could have. It's a hang on.
[9598] Yes.
[9598] It doesn't matter if the important thing is how labored the engine is, and that's the thing you're measuring, how many RPMs, the speed doesn't matter.
[9609] You're being efficient, you're gonna get as much distance out of it.
[9612] So measuring something as moderate or average speed when it doesn't matter doesn't mean anything.
[9621] What might be important is the RPM on the engine.
[9624] Oh, no.
[9624] Yes.
[9625] Yeah.
[9625] It's definitely something.
[9626] Yeah.
[9627] Yeah.
[9627] There's a lot of things that we don't measure because we don't consider them a profile.
[9632] We collect a lot of data that we don't understand whether it's gonna be a future profile.
[9638] At the end of the month in the future a useful profile.
[9644] It might be.
[9645] [No content to preserve]
[9645] That's why we should keep the data.
[9648] That's the discussion.
[9649] [No content to preserve]
[9649] [No content to preserve]
[9651] So as a clarification, would you consider the numerical aspects of process profiles?
[9658] Process characteristics, would that be part of the process characteristic itself, or would you consider it as a measurement information content entity?
[9669] [No content to preserve]
[9669] So you're pushing me down a road which I don't want to go down.
[9674] Come on, Barry.
[9675] That's why we are here.
[9676] So the road goes like this.
[9679] So we have a universal quality of being of length, which is measured in inches or centimeters or whatever.
[9691] It doesn't matter.
[9692] So we have a term in a length ontology or a measurement ontology which will be a term representing a child of length, and that would be a child of quality.
[9707] Do we now have a child of length which is called one inch length or 1.1 inch length or 1.11 inch length?
[9717] We don't want to go down that road, so you should not push me down that road because otherwise you will fall in. I would say that since at some point we want to consider things like relative qualities, we don't want to have it the way you described it. We want it to be measurements.
[9733] So these are real qualities which exist in reality and which could be, I mean, of course, the length exists, but there's also the measurement I see.
[9742] So as a matter of anecdotal interest, are you familiar with the catastrophe in the Airbus wiring which costs 6,000,000,000? I'm talking to you, Mr.
[9754] Boeing.
[9755] You are aware of that.
[9756] That was a case where millimeters of difference in the length of cables cost $6,000,000,000 to rectify.
[9765] These qualities, millimeter-size length differences are very important, and the confusion came about because of two distinct ontologies of "hole" in the French and the German engineering information bodies.
[9787] One of them thought that holes were two-D objects, holes that cables go through.
[9793] The other one thought that holes were three-D objects because they measured.
[9798] They saw the hole as being contained within a piece of metal or plastic, which would then have a length, and they miscalculated.
[9806] They couldn't put the two parts of the Airbus together when they brought them from Hamburg to Toulouse.
[9812] Anyway, these are important questions, but I don't want to go down that road.
[9819] I may say today.
[9822] I did address the shift in participant this morning.
[9824] I'm not happy with the crew handover.
[9828] Technically, they're not supposed to be in this room this Sunday for my daughter.
[9835] She said they're not supposed to be in.
[9839] Are you willing to give up?
[9842] Do you want to give up our new news?
[9845] We can't really hear you very clearly.
[9846] Another conversation.
[9849] We're So we can't really hear you very clearly.
[9855] Another conversation.
[9856] Okay.
[9858] Alright.
[9858] Let me move on.
[9873] Yeah.
[9878] Yeah.
[9878] Good.
[9881] Good.
[9882] Alright.
[9882] We have this hierarchy: quality, color, red.
[9888] Maybe dark red on the next level.
[9891] Maybe red RGB 93, 22, 41 on the next level down.
[9898] We're only interested in the first two or three levels for this purpose.
[9903] The plant is green, and we're dealing with green.
[9906] The plant is green at time t.
[9909] The plant is brown at time t prime.
[9915] The plant has a color, and the color quality is identical from t to t prime because it's identical through the whole existence of the plant.
[9927] It always has its color.
[9930] But this color is sometimes green, and then at later times, it's brown.
[9937] So even though it always has its color, it always has its quality, it can change the hue or the shade of color from one time to the next.
[9948] This means that when you say what is your temperature, what you mean is what is the measurement value of your temperature.
[9958] A correct answer to that question would be it's the same temperature as yesterday.
[9964] Even though it's higher today, it's still the same temperature because I only have one temperature, just as I only have one shape.
[9973] Even though my shape is changing, my size is changing, and so on.
[9976] This is the way BFO thinks about qualities and how do you.
[9992] Yeah.
[9996] Yep.
[10001] Could the speaker get a microphone?
[10010] Someone speaking?
[10011] Yeah.
[10011] That's here.
[10015] Alright.
[10015] I really don't understand this question because to me it seems obvious.
[10019] If we focus on the color of the plant, we are focusing on instances and we see we're interested in the color quality of the plant which exists as it exists at time t one and the color quality of the plant as it exists at time t two, and then conceivably we're interested in the continuous changes between those times.
[10040] We can see the instances before.
[10043] That's not part of the question.
[10044] The question is how do you tie the process profile that says this process profile is about that color?
[10053] No.
[10053] No.
[10053] The process profile is made up of those color qualities.
[10057] It's not about them.
[10058] It's a thing in the world.
[10060] Well.
[10061] A process profile has a participant, which is the rose.
[10065] Yep.
[10066] How do I get to how do I say the rose's color is during this process profile?
[10075] The rose's color was red.
[10078] Yeah.
[10078] I said earlier that when you start talking about process profiles, you are disengaging yourself from the messy world of what happens and is the case in causality.
[10088] You're just looking at this particular sliver of being, which is measurable or detectable.
[10094] In this case, the sliver is these colors.
[10096] You see them and you see over time how do I know that it's about the color and not the mass?
[10101] Because you're an intelligent human being.
[10104] We're interpreting it by the name of the process profile.
[10109] You're steeped in BFO.
[10112] You know how to recognize qualities.
[10114] You also know how to recognize colors because you're a human being.
[10117] You'd be dead if you didn't have that capacity.
[10120] You wouldn't know where to look for the milk and so forth.
[10123] I think what Jim is asking is whether we would have a specific process profile of the change of color.
[10130] Like.
[10131] That's what you wanted.
[10133] Mentioned this as an issue earlier.
[10134] How do you connect it to the color of this road?
[10137] Yeah.
[10137] Good.
[10138] I think I have a way for that.
[10139] I think that measurement units and measurement processes are cultural achievements of human beings.
[10147] We have had them for a long time.
[10152] Roughly about the time of Napoleon, we managed to have uniform ones over the whole planet.
[10157] We still have problems with comparing Celsius and Kelvin degrees and so on.
[10165] Even that is not quite sorted out by the metrology world, but we've seen the way forward to make those problems disappear.
[10174] Now we're back to Plato with his stick in the sand.
[10179] When those units of measure systems came into existence, did the world change, or did we just now have a way of grasping the features of the world which is more precise and communicable and so forth?
[10193] I lean towards the second answer.
[10197] And now you seem to be worried.
[10201] I think colors are out there and that we can see them and recognize them as colors.
[10206] And when we see something changing color, then we are recognizing a process profile.
[10212] So what's your issue?
[10216] So my issue is shouldn't there be some sort of a relation between a particular process profile and the particular color of the rose that is the participant in that process profile.
[10230] Yeah.
[10231] How do I point it to that particular color instead of the particular mass?
[10237] Yeah.
[10238] So when you say intelligent people, it seems like we're missing a relation.
[10243] Somebody tells you to measure the height of your brother, you don't worry about, do I need to measure the height or do I measure the length or the temperature?
[10254] You just know what height means.
[10257] I don't understand the question.
[10263] Does anyone else think he has a question here?
[10268] No?
[10272] So I've said that most process profiles are measurement process profiles, but there are also quality process profiles as regards, for instance, color.
[10282] I'm not sure. I don't think process profiles in the realm of measurement are the most useful ones, but there are process profiles in other realms.
[10290] And if I'm right, thinking is a process profile.
[10295] Conscious thinking is a series of events which make a process, and it's a process profile because part of your consciousness is not the circulation of blood through your brain, but your consciousness is somehow part of a system which involves circulation of blood in the brain.
[10320] Yeah.
[10320] So you can extend measurements to include things like color.
[10326] Yes.
[10326] We okay.
[10327] Let's try with this.
[10328] So yes, we as humans can understand surely from the label or in one way or another what is meant.
[10333] But if you have several thousand things in your database, how do you structurally what is your pattern?
[10341] You go to your catalog of devices and you look up color sensor and then you go to the color sensor and you put it in front of the flower and switch it on.
[10351] And then you get a very good measurement of a process profile.
[10357] Are you saying that through using the measurement instruments, we do not need a direct connection between a process profile and the quality it is related to?
[10367] It comes free with the label on the sensor.
[10374] I think that you are suggesting that we create a taxonomy of the different types of profile, just like we have a taxonomy of quality.
[10386] Right?
[10387] Yes.
[10387] Exactly.
[10387] Just like that.
[10388] Yeah.
[10388] Yeah.
[10389] So there will be a speed process profile.
[10392] There will be a color process profile.
[10394] The color process profile is different from the quality color, I think.
[10400] Yeah.
[10400] Absolutely.
[10401] Yeah.
[10402] That is correct.
[10405] So alright.
[10405] So let me try one more time.
[10407] Correspondence.
[10408] Right?
[10408] We cannot have any correspondence.
[10410] They are separate things and you understand it.
[10413] Oh, color means color of an object, and color process profile means color of a process profile.
[10420] That's all.
[10421] A body of gas can have a color.
[10423] Yeah.
[10424] Doesn't have to be an object.
[10428] So I really don't understand your problem.
[10431] So you lose.
[10432] You lose.
[10433] Talk tomorrow.
[10435] So I will say that the answer is IOF.
[10438] IOF needs to make classes or taxonomy.
[10444] So you have an IRI for color process profile, and all the companies need to use color process profile IOF color process profile whenever they are talking about color change.
[10456] Yeah.
[10456] That would probably be helpful because they would have consistency.
[10459] That's the correspondence that I was talking about.
[10460] Yeah.
[10461] Yeah.
[10462] Human beings have to be involved.
[10470] How much time do we have?
[10471] We have negative time now.
[10472] It's time for lunch.
[10475] Thank you all very much.
[10477] Thank you, Barry.
