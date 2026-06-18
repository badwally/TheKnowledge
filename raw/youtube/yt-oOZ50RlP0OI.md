---
schema_version: 1
id: yt-oOZ50RlP0OI
type: youtube
title: The FoodKG Reimagined KGC 2024
url: https://www.youtube.com/watch?v=oOZ50RlP0OI
authors:
- 'The Knowledge Graph Conference '
ingested_at: '2026-06-17T20:57:30Z'
content_hash: sha256:cc1132c69ebee9062f3b9f715d123ae61cab89ef4b7b1793eea337405acca33a
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: 'The Knowledge Graph Conference '
  channel_url: https://www.youtube.com/@theknowledgegraphconference
  duration_seconds: 1894
  caption_track: fetched
  snippet_count: 744
filter:
  score: 0.7
---
[0] uh streamline basically it's automatic
[3] process. It's just like conversion of
[4] the units and some you know dual
[6] location from level one to level uh
[9] level two uh depends on what you're
[12] deriving from those you know level one
[14] products I mean it doesn't necessarily
[16] have to have NASA sometimes you know
[17] other people you know a proposed project
[20] like that uh but uh I guess you know
[23] that depends on a level two product but
[25] level zero to one is more streamlining
[27] Jennifer do you have any comments on
[29] that
[31] can you hear All
[35] right. So, so I think um there is more
[37] than that but uh within the NASA open
[40] science policy and we're trying to sort
[44] of all
[59] the email is there. Yeah, you can email
[62] us the questions you have. Thank you.
[64] We're right on time.
[68] Thank you so much. Thank you, Jennifer.
[70] And thank you,
[80] Excuse
[92] me. Can you please take this talking?
[95] Um,
[102] thank you. Uh, can we please have some
[104] silence? And, uh, we'd like to start
[106] with the next speaker as soon as
[108] possible. Are you ready?
[115] Senator.
[135] All right.
[138] I'm very happy to uh um introduce Oshani
[142] Venatne. I hope I said it correctly and
[145] it's the food knowledge graph reimagined
[148] reimagined. Um Osani please go ahead.
[152] All right, welcome everybody. Um so from
[155] games to climate change to food and
[157] right before lunch I guess uh right on
[160] you. Um okay so you know by
[164] participating in this session I have
[165] listed several talk objectives. So first
[168] I will talk about the motivation of this
[171] work. uh so there's a lot of complexity
[173] in you know constructing a knowledge
[175] graph of food items and then I will talk
[179] about the the stuff we did to actually
[180] construct the knowledge graph and then
[183] I'll talk about bunch of applications
[185] and uh you know unsurprisingly you know
[187] the application is food recommendation
[189] food substitutions things like that and
[192] um you know really the the point of this
[193] talk is like you know how we can extend
[195] this food kg and applications and uh
[199] just like you know previous talks like
[200] you know we are exploring things like
[202] you know retrieval augmented generation
[204] I'll talk about that with respect to
[207] both the inference and also in um extend
[210] the food k uh and then I'll also talk
[213] about quality assurance of um the
[217] various food items we have uh with
[219] instant mechanisms
[221] so I want to you know give a big shout
[223] out to the collaborators behind this
[225] project uh so this work actually started
[228] uh with this IBM RPI collaborative
[230] project called health empowerment
[231] through analytics, learning and
[232] semantics. If you want to find more
[235] information about this project, you can
[236] go to that website which has like you
[238] know more information other than the
[240] food kg. Uh and like Deborah McGinness
[243] was a co-pi on that project. uh she's
[246] here in the audience and more recently
[248] we have started a collaboration with UCI
[252] they have future um health institute and
[256] they have this open framework called
[258] open computational health agents or open
[261] sha and we have some collaborations from
[264] uh that organization as well
[267] okay so the motivation I guess it's you
[269] know uh kind of a no noer uh so there's
[273] this huge you know problem of uh chronic
[275] health conditions and if you see the you
[279] know woman there just like me you know
[281] she's leaning towards unhealthy food it
[282] d items and you know she has you know
[285] fruits on the other side uh and you know
[288] basically evidence-based nutrition
[290] recommendations are not easily
[292] integrated into the diet you know
[293] applications that use uh and more
[296] importantly they're not personalized uh
[299] to our you know specific you know health
[301] conditions our preferences things like
[303] that
[305] so uh and another motivation is that you
[307] know let's say you open your fridge and
[309] have uh you know chicken you have onion
[311] and garlic and you're in the mood for
[313] some Indian dishes uh so you have these
[316] you know constraints and if you Google
[318] you know what can I what Indian dish can
[320] I make with chicken onion and garlic you
[323] will be presented with you know bunch of
[325] these options and uh if you look at
[329] these options like you know maybe some
[331] of them are the same recipe It's not
[333] that easy to like you know figure out
[336] these other you know same recipe. You
[338] have to like you know do a little bit of
[339] research and maybe you know this hungry
[342] Jennifer is on this specific low-fat low
[344] carb diet and is also lactose intolerant
[347] and if these recipes are suitable for
[349] her like she has to again like you know
[351] do a lot of reading to figure that out.
[353] So knowledge graphs could actually help
[355] that problem because you can you know
[357] have all this you know integrated uh you
[359] know view into the data.
[362] Um so but you know it's all good uh
[366] knowledge labs are good but you know
[368] there's some challenges in um you know
[370] kind of combining all these things
[372] together because so at the very high
[374] level you have recipes and uh recipes
[377] have ingredients and each of these
[379] ingredients have different nutrients and
[381] we also have dietary guidelines and then
[384] on top of that we have these personal
[386] like in human factors like you know
[387] personal preferences allergies and
[388] things of that nature and Um so we we
[394] want to like you know integrate all
[395] these things uh so that eventual users
[398] do not have to you know spend a lot of
[400] time um to figure out what they can eat
[403] and at the same time we want to maintain
[405] the provenence of uh the recipes that
[408] they are looking at right so that's the
[410] biggest problem with you know recent
[411] LLMs right so you can get the same
[414] information but you don't know where
[415] this recipe is coming from so in our
[418] food knowledge graph we are maintaining
[421] the founders information,
[424] right? So, we have worked to, you know,
[427] build this cohesive food knowledge graph
[429] and it brings together recipes,
[430] nutrients and other food vocabularies.
[433] Uh, it links to existing ontologies and
[435] vocabularies. Uh, it's straightforward
[438] to use. It's modular so anybody can
[440] extend this resource and in fact so we
[443] published this paper in 2019. uh so far
[446] like you know I personally know of at
[448] least 20 different projects that are
[450] using uh the food kg and we have over
[453] 200 publications so this is a a very
[456] good resource and people are using that
[458] and I encourage everybody in the
[459] audience to you know u use this uh uh
[463] resource and more importantly we
[465] maintain provenence for every assertion
[467] so we are combining different data
[470] sources so when we combine these
[473] different data sources it's very easy to
[475] lose who's like you know where things
[476] are coming from but in in our knowledge
[478] graph we actually maintain that power so
[480] that's a very important goal of our work
[485] so let me talk about the data sources u
[487] so we have u at the last count we had
[490] you know close to 1 billion triples and
[493] this includes all the like you know
[495] prominence information things that uh
[497] but if you look at it the recipe the
[500] number of recipes is a little over 1
[502] million um and each uh uh the recipes
[505] actually came from this data source
[507] called recipe 1m and we also augmented
[510] that with the cooks theorus and it has a
[513] very large catalog of ingredients and on
[515] top of that like if you look at like you
[517] know food.com recipe will have bunch of
[520] ingredients but it's very uh rarely or
[523] it's not actually uniform to find
[524] nutrient information related to a
[526] recipe. Some recipe site will have
[528] nutrient information some won't. So we
[530] had we wanted to harmonize you know have
[532] a kind of a you know standard interface
[534] for our food recipes. So what we did was
[537] we uh tapped into the USDA's uh nutrient
[540] database and that has over 8,000 natural
[543] food products like you know apple and
[546] also 400,000 branded food items. So it's
[548] like you know bag of like you know lace
[549] chips packet and each of these food
[552] items have over 46 measured nutrients.
[556] These are macro and micro ingredients or
[558] sorry nutrients.
[561] And then of course we deliberate good
[563] ontology. Uh maybe some of you audience
[565] have used it. It's a field to poke
[568] ontology and uh it's a very you know
[571] thoroughly like you know uh it's a very
[573] thorough uh you know vocabulary for uh
[575] food stuffs. Uh so we leverage uh the
[578] food on as well. So what are some
[582] challenges? Again like you know I don't
[583] I'm preaching to the choir here. Uh so
[586] there are problems in consistency you
[587] know some recipes have kilograms some
[589] have you know pounds and non-standard
[592] use of measure to taste as needed a few
[595] shakes how do we like actually capture
[596] the you know amount complicated units so
[600] it's like you know fraction of something
[602] and different ambiguous names the same
[604] concept like pancake cupcake hot cake
[606] they're all the same thing and it's very
[608] hard to like you know all those things
[610] and accuracy so we were like you know
[612] harmonizing different recipe you know
[614] sources And you know we we could find
[616] like you know same uh recipe in multiple
[619] sources and you know we found these
[621] alignment problems. So that was also a
[623] problem. Spellings spelling errors
[625] incomplete data. So missing units was a
[627] big problem. Uh because most sites like
[630] you know they have you know stuff
[631] without like numbers without any uh
[634] unit. Uh so we had to do some guess work
[636] and then unnecessary information. So we
[638] do the entity extraction and we find
[640] this like you know ingredient called
[642] black black beans from the stove as well
[644] as black beans or beans. So figuring out
[647] like you know what that means uh was you
[649] know problematic and then completeness.
[652] So food knowledge you know continues to
[654] evolve and that's uh the stage we at
[657] right now because they're trying to like
[658] you know build the next version of uh
[660] the food.
[662] Then another you know challenge this is
[665] both a challenge and a blessing. So food
[667] on if you have you know uh worked with
[670] it it's very you know dense and like you
[672] know it has a lot of information. So
[674] navigating the food on specificity was a
[677] problem. For example if you wanted to
[679] look up the egg like as a product. Uh so
[681] there's like you know egg food product
[683] and you have to go down like figure out
[685] like the hen product and then there's
[687] like you know part of animal and egg in
[689] another category right so which u you
[692] know uh categorization is uh is the
[695] right one uh was you know it's not a big
[698] challenge but you know it has way too
[701] much information than our food knowledge
[702] graph requires. So sometimes it's
[705] actually a better thing because yeah
[706] more information is actually better than
[708] lack of information.
[710] All right. So let me briefly talk about
[712] the construction. So we intentionally
[714] decided to keep the con conceptual
[716] ontology model kind of flat so that we
[719] can integrate things you know uh quite
[721] easily. So this is the the full you know
[724] ontological view of our food k like you
[728] know each of these you know classes have
[729] like you know millions of instances.
[733] Uh so just to give an example like you
[735] know we have uh something like a recipe
[738] uh it has has ingredient and
[739] ingredients. So this is like the most
[741] queried uh you know triple in our
[744] knowledge graph as you can imagine. Uh
[746] and then we have other you know various
[748] data type attributes. Uh if you take
[751] something like food characteristic
[752] because we are trying to recommend
[753] certain food items. So people might have
[755] certain preferences for foods. We have
[757] those like you know characteristics
[758] encoded as well and we those
[765] fell down. It's funny.
[768] Okay. All right. So yeah. So food
[771] characteristics are there and then user
[773] preferences again like you know uh maybe
[775] like you know somebody has u uh an
[778] allergic reaction they don't dislike
[779] something right. Uh so we we try to
[782] capture all those things in the ontology
[783] as well. And then food on import. So I
[786] mentioned like you know food on is
[787] massive. So we decided to just extract
[790] food product by organism category and
[793] this you know has
[797] maybe I'll just hold it if you can hear
[800] me. Okay. Um right so we we extracted
[803] this very uh you know food product by
[805] organism uh you know and then we have
[807] mappings to those concepts input on.
[811] Right. So uh with respect to
[813] constructing the uh knowledge graph uh
[815] the first like you know big step was uh
[818] you know mapping the nutrients and for
[820] that we leverage systematic data
[822] dictionary approach. So I'm looking at
[824] so but like know Sabir was the main
[826] person so looks exactly like him. So and
[830] Deborah like you know uh this uh project
[834] came from Deborah's group. So we
[835] leverage a semantic data dictionary
[837] because um the USDA ingredients are in a
[841] relational format and it's uh quite uh
[844] you know uh easy to uh convert those uh
[847] you know relational information into
[849] triple format and we uh again like you
[851] know we uh kept like you know where
[853] things are coming from. I mentioned
[855] provenance is a very important thing and
[857] of course we use tools like onto Fox as
[859] well. Uh and then yeah so uh for keeping
[863] provenance we used the nano publication
[865] uh you know standard. Um so if you're
[868] not familiar with the nanop publication
[870] standard so basically there's something
[871] called an assertion graph and a
[873] prominence graph and a publication
[874] infograph. These are subgraphs. So the
[877] assertion graph will have uh an
[879] ingredient
[881] has you know this particular ingredient
[883] and uh then like the ingredient will
[886] have these nutrients. So we are doing
[888] you know those kinds of like you know
[890] merging of various information and then
[892] the brownness information will have
[894] where is this recipe coming from we
[896] record the URL of that and then uh also
[899] the nutrient information from USDA and
[901] for the publication information who did
[904] what. So in uh our knowledge of
[907] construction you know case we have this
[909] linker which is u you know an automated
[912] process. So the nano publication uh
[914] publication information will contain uh
[916] this assertion was made by this linker
[919] but it's quite possible that uh this is
[922] done by a human. So uh I'll talk about
[924] this when I go to the incentive part. So
[926] it's quite possible that a human will
[928] come and say okay here's a new recipe
[930] you know I'm making this assertion um
[933] the prominence is basically I found this
[934] information from such and such source
[936] and the publication information contains
[938] the humans you know contact information
[940] and name and whatnot attribution and
[943] other you know kinds of uh information
[946] or like of provenence related
[948] information.
[950] Okay. So now uh let me talk about the
[953] applications. Uh so you know we created
[957] this food bot. Uh so in this food bot
[960] and there's a demo if you want to take a
[962] look. Uh you can ask a question and then
[965] it'll provide some answers. Um so uh
[970] that person earlier like you know
[971] Jennifer like you know maybe you know
[973] she wants to find a good uh breakfast
[976] with eggs. Uh and the bot will provide
[979] this information. uh now one uh big
[981] thing we do behind the scenes is that we
[983] personalize the knowledge. So the
[986] person's personal health knowledge graph
[988] Jennifer's PHKG will contain that she's
[991] 35 years old and he's a female. uh but
[994] if another person uh with a different
[996] PHKG uh ask the same question uh so in
[1000] this case like you know this is a 65
[1001] year old male who's diabetic uh it you
[1004] know our heels uh food bot will provide
[1008] food options with uh lower glycemic
[1010] index so that they can be um you know
[1014] you know it's more health conscious
[1018] so we provide this personalization
[1020] behind the scenes
[1022] uh yeah so this is what happens um you
[1025] know uh behind the food uh uh heels uh
[1030] food board of the heels project. So when
[1032] a user asks a question we have uh this
[1035] expansion query expansion. So in
[1038] addition to the question so this is like
[1039] you know similar to u you know providing
[1042] context uh in you know the kg or like
[1044] LLM based applications um but we do this
[1048] in a semistructured way. So uh not only
[1051] are we putting in the users you know
[1053] question we also provide like you know
[1055] users u uh preferences you know their
[1058] health conditions and then we uh have
[1061] this knowledge based Q&A which is
[1063] powered by this method called
[1064] birectional attention networks or bamnet
[1068] uh so this is kind of like an LSTM
[1070] method u you know I've listed the paper
[1072] here so we are leveraging uh that uh
[1075] method to do the Q&A and uh then we
[1079] query from the food kg and provide the
[1081] answer. And in terms of the dialogue
[1083] generation, so this was done prior to
[1085] LLM. So we leveraged the IBM Watson
[1089] dialogue flow. So there you have to
[1091] identify intents uh and entities and
[1093] then we have this dialogue flow and in
[1095] the dialogue flow you can have these
[1097] hooks to like you know additional
[1099] knowledge graph uh or like you know
[1100] knowledge endpoints and that's how we
[1103] you know kind of construct the the
[1105] answer and provide back to the user and
[1107] it's able to you know maintain a
[1110] dialogue flow but not um you know as as
[1114] good as like you know the current LLMs
[1118] and then another application that we
[1120] have uh is this ingredient
[1122] substitutions. So we um uh what we
[1125] wanted to do is you know so if we have
[1129] um a particular
[1131] recipe let's say rice like you know you
[1133] are being health conscious and you want
[1134] to find a you know substitute for rice
[1136] so maybe you want the you know the food
[1139] bot to provide cauliflower rice as uh as
[1142] a substitution.
[1144] So um for this we leverage implicit
[1146] semantics and explicit semantics. So for
[1149] implicit semantics we you know leverage
[1151] like embedding based like you know um
[1153] word toe kind of model and see like you
[1155] know which kind of recipes are in the
[1157] similar you know similar to that
[1159] particular recipe. Um and uh for
[1163] expressive semantics we leverage the put
[1165] on hierarchical information and there's
[1169] a huristic. So the huristic the dish
[1171] huristic diet improvement ingredient
[1173] substitution heristic leverages both the
[1175] implicit and explicit semantics and then
[1178] ranks the you know results and provides
[1180] to the user. So if you want more details
[1183] about that uh particular work I you know
[1185] I have the paper listed as well.
[1189] All right. So
[1191] in terms of extending the food kg and
[1193] the applications
[1195] um if there are any questions feel free
[1197] to ask. I think I'm going a little bit
[1198] faster but uh that's okay. I guess we
[1201] can go to food. Uh all right. So the
[1205] types of questions that the food kg can
[1207] answer. Uh so there are these factoid
[1209] type of questions. So we can ask uh you
[1211] know how much a certain nutrient is in a
[1214] particular uh food item. So here like
[1217] you know we asking how much fat sat in
[1219] butter salted and the food recommener
[1221] gives 51 whatever grams of fat. Now this
[1225] number might seem you know very high.
[1228] This is actually 100 grams. So this is
[1229] what u the uh USDA you know um provides.
[1234] So USDA all the food items they're
[1237] giving nutrients by 100 grams. Um if you
[1240] take like you know maybe uh you know
[1241] spoonful of butter which is what uh
[1244] chapd gives it gives like you know seven
[1246] grams or something. So uh that is you
[1249] know uh a spoon is like know 14 grams
[1251] and then you know it's half of that. So
[1253] it kind of uh you know is aligned with
[1256] what chajipity gives. And then we have
[1259] comparison questions. So uh we can
[1261] compare two different um uh food items
[1266] uh against like you know one uh nutrient
[1268] type.
[1270] And then constraint questions is is the
[1272] most like you know uh prominent type of
[1274] questions that we have. uh so the
[1276] previous example that we had like you
[1278] know which Indian dish has chicken onion
[1280] garlic and then we have a bunch of these
[1282] recipes and more importantly we have the
[1284] link which is derived from the proess
[1286] information.
[1288] So some of the limitations of the food
[1291] kg uh uh or the heels foodb powered by
[1295] the food kg is that the range of
[1297] questions in natural language is very
[1299] constrained because what we did was we
[1302] um had uh like our uh retrieval engine
[1306] is actually powered by sparkle. Uh so we
[1308] had you know in the previous examples
[1310] you probably saw like you know you know
[1312] the how you know we are trying to like
[1314] you know match with fat sat which is the
[1317] label for that in the food knowledge
[1319] graph. Uh if you ask like you know
[1321] saturated fat sometimes it might not
[1323] work uh perfectly right so you know
[1326] there were you know certain quirks uh if
[1328] you ask if you change u uh the the way
[1331] you ask a question. So similar to that
[1334] problem is the lexical gap right? So the
[1336] same question can be asked in multiple
[1337] ways. And then the other you know uh
[1340] problem is like you know the answers
[1342] retrieved from the sparkle endpoint uh
[1344] they are heavily templated. So if you
[1345] are a repeated user you'll get the same
[1347] kind of you know boring answer all the
[1349] time. So uh so so that was also
[1352] something that we want to improve.
[1355] So uh if you are wondering like you know
[1357] how do these you know types of questions
[1359] uh compare with chajp current version of
[1361] chajpd
[1363] uh you know if you ask like you know
[1365] which Indian dish has chicken onion
[1367] garlic it'll give bunch of uh you know
[1370] recipe suggestions like this if you want
[1372] to ask the same question from our food k
[1375] without the personalization uh because
[1377] like you know the chachi video prompt
[1379] did not have any personalization or you
[1381] know a few short u uh examples
[1384] Um so we have uh you know I think there
[1388] there are some similarities but you know
[1390] what you can notice is like you know we
[1392] have uh direct names because we have the
[1395] entities directly there in the food kg
[1397] and we have the link which have all the
[1400] like you know aggregated nutrient
[1401] information everything uh connected.
[1406] So uh what we are currently doing is we
[1408] are improving the food kg inference with
[1410] retrieval augmented generation. Uh so
[1413] luckily we have so many sparkle queries.
[1415] So I I mentioned three three different
[1418] kinds of questions. So we have factoid
[1420] type questions. We have comparison
[1422] questions and constraint questions. So
[1425] for each type we have hundreds of uh
[1428] sparkle query templates. And so what
[1430] we've been doing is like you know we are
[1431] using those uh you know query templates
[1434] as you know few short examples to uh
[1438] augment the retriever. And then we are
[1442] uh retrieving some answers and then of
[1443] course like the generator has to uh kind
[1446] of put that in a nice way so that the
[1447] users can uh see the answers in natural
[1450] language. So uh we are you know of
[1452] course like you know there are questions
[1454] with like the the token you know sizes
[1456] and whatnot. So this is uh something
[1457] that we actively working on but uh we
[1460] are off to a good start because we have
[1462] that uh you know u base of uh uh several
[1466] hundreds of like you know sparkle
[1468] queries related to food retrieval. One
[1470] minute left.
[1473] So this is eight minutes. That's why I
[1476] thought like you had more time but any
[1479] all right. Okay. So um next up I want to
[1483] talk about like uh the incentivization
[1485] aspect. Um so um this is a project that
[1489] uh uh some of my students did. Uh so
[1492] they wanted to ext extend the food kg
[1494] with the baked goods. So their idea was
[1497] uh people could submit food recipes and
[1499] then uh if they are novel so we want to
[1502] find something that's not currently in
[1504] the uh food kg um they get a reward uh
[1510] for submitting that particular uh recipe
[1512] and so they have this blockchain based
[1514] implementation it's actually you know
[1516] there's working code there so you can uh
[1518] test it out if you have a MetaMask
[1521] wallet
[1522] um and uh And then like you know this
[1526] has this NFT kind of thing like you know
[1528] so you submit a recipe if it's there
[1530] other people have the rights to purchase
[1533] your recipe. Uh so this could be a way
[1536] to like incentivize good quality data
[1538] entry to the food kg or any kg for that
[1540] matter. Uh we also have this like you
[1543] know uh mechanism to deposit some money
[1545] before submitting the recipe because you
[1547] know it's uh easy to like you know have
[1549] very random you know uh recipes
[1551] submitted right uh so that it's
[1553] completely novel right like you know
[1555] something with like you know uh you have
[1557] a question or yeah so um other users can
[1561] buy the rights to publish the recipe so
[1564] is it like the recipe is unique it has
[1567] to be unique so like you know we check
[1569] if uh the submitted recipe is not there
[1572] in the knowledge graph. So it says other
[1575] users, but can one user buy the rights
[1578] for that specific recipe? Yeah. And then
[1580] can they resell it? Yes. So they have
[1584] the ownership.
[1586] Yeah. It's like any NFD. Nothing nothing
[1588] new in terms of the uh the buying and
[1591] selling aspect. Uh all right. So I think
[1593] I'm right on time. So this is a summary
[1595] of uh you know my presentation. uh the
[1598] project website is available if you want
[1601] to uh contribute if you want like you
[1603] know collaborate with with us uh you
[1605] know please contact and with that I'll
[1607] conclude my presentation and uh happy to
[1610] take any questions at the back
[1614] are you are you taking oh sorry
[1619] thank you Osani that was a great
[1621] presentation except you mentioned food
[1623] and it's almost lunch time are you
[1625] taking any metrics about either like how
[1628] users rate recipes or some other way of
[1631] tracking like how good they are
[1633] currently no but we could certainly
[1634] extend that. Yes. So we had um you know
[1637] another you know group of people uh were
[1640] looking at recipe reviews um but that uh
[1644] part of the project were never
[1646] incorporated into the uh food kit
[1650] include that. Yeah.
[1658] Um, excuse me. Sorry, we're taking a
[1660] question here. Yeah. Out of curiosity,
[1664] what food or food group was like the
[1665] most difficult to model or had the most
[1667] edge cases? Like just what was the most
[1669] difficult part of modeling all this
[1671] data? I can give so many examples. So,
[1673] one big problem we had was uh remember
[1676] USDA has these like no branded product
[1678] items. So the natural food items are
[1682] 8,000, branded uh products are 400,000.
[1686] So if I were to search for something
[1687] like apple juice, we get like know baby
[1690] food, apple juice, baby food something.
[1693] So there are so many um you know
[1695] varieties of food. So uh for edge cases,
[1698] yeah, I think yeah not not many people
[1700] would you know use the food ketrie
[1704] too many baby food items unfortunately.
[1710] Are you doing any kind of modeling for
[1711] the preparation of the recipe? Not just
[1713] the ingredients but how is it prepared?
[1716] Yeah. So actually the recipe 1 M data
[1719] set has the uh the the steps and in fact
[1722] I believe Solar had the flow graph uh
[1724] work. So another you know one of
[1726] Deborah's students who actually
[1727] graduated uh he he modeled the flow
[1731] graph um for how actually I'm not sure
[1734] about the details but in the food kg we
[1737] don't have uh recipe steps but you know
[1740] there's some concurrent work that we
[1742] could easily incorporate.
[1745] Any other questions?
[1750] So um food kg seems like u an
[1754] application for wellfed people right
[1756] there's NSF has a track in the
[1759] convergence accelerator on food and
[1761] nutrition security. I was curious if you
[1764] knew about that and the projects that
[1766] are looking uh at various sort of food
[1769] related issues that are on the nutrition
[1771] security side. I haven't personally
[1774] looked at it but I'm more than happy to
[1776] take a look and you know collaborate if
[1778] there are opportunities in that case uh
[1780] I'm from NSF so we will certainly want
[1782] to connect you uh to those projects okay
[1785] we should talk
[1789] any other questions
[1797] hi I'm just curious about uh the
[1799] provenence information you mentioned so
[1801] did you see or have you encounter any um
[1806] applications or implementation using the
[1808] provenence maybe like tracking I don't
[1811] know confidence score when answering you
[1814] know the question something like that
[1816] have you right um so
[1820] um well we in the like no recommendation
[1822] engine we weren't using the prominence
[1824] information but you know it could be
[1827] possible that a human curated one to
[1829] have a higher importance than the linker
[1832] right? Because it's vetted by an actual
[1834] human. Um, so it's something that we can
[1836] incorporate. We currently don't use
[1838] prominence information in the ranking.
[1840] It's only like the similarity, the
[1842] semantic similarity to the user's
[1843] question. But we provide the prominence
[1845] information so that the user can vet,
[1847] you know, this is, you know, from a good
[1849] source.
[1852] Any other questions?
[1854] I'd really like to thank all of the
[1856] speakers. I apologize. I I I wasn't told
[1858] that I was going to be the moderator for
[1860] this session uh for this uh track, but
[1863] uh thank you Osani. Thank you Armen
[1866] Talanka. Thank you very much. I
[1868] apologize again. And we had a great
[1871] great we had two great presentations
[1872] that I caught and I know I missed that
[1874] first one which I really wanted to
[1875] attend. Was that you? I'm sorry. You
[1878] know what? I I really wanted to attend
[1879] that and I came running up and and then
[1881] they dragged me back. But anyway, um I
[1885] any any questions? It's lunchtime. I
[1887] know. Uh, you know, so grab the
[1889] speakers, talk to them. Thank you again
[1891] to the audience.
