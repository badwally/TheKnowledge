---
schema_version: 1
id: yt-p3TLEV3oIBY
type: youtube
title: How to use a Semantic Layer and Data Lakehouse
url: https://www.youtube.com/watch?v=p3TLEV3oIBY
authors:
- AtScale
ingested_at: '2026-06-18T01:38:24Z'
content_hash: sha256:c380eb9f288efddda45f77aff4eaea24f436f2267486cf0c2c6ee9a310355315
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: AtScale
  channel_url: https://www.youtube.com/@AtScale
  duration_seconds: 3048
  caption_track: cached
  snippet_count: 520
filter:
  score: 1.0
  policy_version: force-include
  rationale: Force-included by caller (--force-include); semantic filter bypassed.
  decided_at: '2026-06-18T01:38:24Z'
  user_correction: null
---
[2] hi everyone and welcome to an appskill live session and today we have two very special guests really good friends of
[8] mine from databricks so uh we have on the upper right is franco pitano franco is the lead product
[16] specialist um at uh at databricks and he specializes really
[22] i think now frank o'reilly and databricks sql which is the brand new product that uh that databricks um just
[29] shipped or just released i should say there's no shipping software because it's all a service and it's pretty
[34] amazing um and uh and sohambot is uh the lead solutions architect for databricks
[42] and sohom works on um on uh on on making sure
[47] people can migrate to the cloud so he's your man when it comes to uh charting a
[52] course to the cloud so hey guys welcome to welcome to the the session thanks for
[58] having us yeah yeah so um i just want to plug that this is just a little promo uh uh listeners
[58] Tech Session Announcement
[66] for our our tech session that we have coming up on april 21st uh it's april 21st
[72] which i think is a thursday um this thursday and uh it's at 2 p.m eastern
[78] and we're going to do some really fun stuff um we're going to do some real fun stuff with tech so today we're just going to chat about some some
[84] interesting topics i think and and and really talk about what we're going to what you're going to see
[90] um on the 21st um but uh so so this is just an uh an open session where we can
[96] uh talk about the lake house talk about the semantic layer and and really point you to some really awesome uh tech
[103] demonstrations that we have planned for you uh so franco um so uh
[108] what do you what do you plan on uh what do you plan on showing um on on thursday
[114] yeah that's a great question thanks again for having us here today uh here today dave i really appreciate it um
[114] Databricks
[121] essentially what a lot of people don't understand about data bricks and kind of what i consider it my goal this year
[128] is people don't really know that uh databricks can do low latency high concurrency serving of data out of the
[135] data lake they kind of know databricks as the big data data science ml company uh you know
[142] obviously the spark people uh is what we commonly get and uh what i'm out here is
[148] saying we're not just spark anymore uh spark is a big part of who we are where we came from but uh the world needs more
[156] than just spark we have then gone on to create uh delta lake which is one of the fastest growing
[163] uh globally used data lake table formats and also ml flow and then we acquired
[170] redash and we built this new product around it called databrick sql and essentially that's kind of what i'm
[176] i'm out here showing people the value of is essentially these sql endpoints and i
[181] know when we were first starting off on our at-scale journey so dave and i and soham
[187] we go we go way back we've been talking about this semantic layer on lake house i think since last year
[193] and uh you know at first dave was like i don't know if this is gonna work your your sql on points they're cool
[200] but you know we looked at the initial thing the initial readings and you're like we're going to need some more and
[205] it was great because we went back to engineering and they basically took a lot of that feedback and they built
[210] a pretty a pretty decent amount of features in a short period of time and then i think that's what we're going to go over right how how can you build a
[218] semantic layer on data bricks sql and how how performant is it so i'm really excited to kind of work with you uh on
[225] that and kind of see what the results are yeah i'm excited to show you know interactive uh queries now i say
[225] Interactive queries
[232] interactive i'm talking about sub second on databricks on databricks sql on a databricks cluster you know what i love
[238] about what i love about the lake house architecture is that you write data once um and you write it to the to delta lag
[245] and then you can apply and and put different engines on it depending on what your workload is you know you may
[250] use choose to use spark if you're a data scientist but you know you're going to use probably sql if you're a bi analyst
[256] so it's it's it's amazing it's really a real step forward to have
[262] a data platform where you can use the best engine for the job but you don't replicate or copy data so i just think
[268] that's again that's a real game changer and um i've been super happy with um with the product um and uh and it it's
[276] lightning fast you know so so so hum i mean what does data brick sql mean for
[281] you and for you know you taking uh customers um on that journey to the
[286] cloud yeah uh it's it's very satisfying for me
[291] to to see db sequel out and in ga now especially because i started my career
[298] as an etl developer and then a data warehouse architect so i come from the data warehousing world
[304] and then after 10 15 years of calling myself i was looking at my resume like etl developer etl architect database
[310] architect and so on and then on 2014-15 i made that switch i got hadoop
[316] certified and right so for a few years i was a big data architect right like like many of us here right we went from the
[323] uh relational rdbms world to big data because of the issues of uh data
[329] warehouses not being able to do streaming to do machine learning and so on and then
[335] i started doing spark because even on other big data platforms you use spark and then databricks is the creator
[342] original creator of apache spark and so i was lucky enough to then join databricks around three years ago
[349] and when i joined for the first year or two it was spark but with delta lake um
[354] it was a much better version of spark you can do asset compliance insert update deletes so it was an awesome
[361] engine for big data processing during my first year or so of data breaks and then
[366] ml flow came so machine learning became super easy on data breaks and then in the last year i'm super um
[372] delighted to see that now with db sql we are not just a good data
[378] warehousing product but we are actually the world's fastest data warehouse we just won the tpc-ds benchmark for data
[384] warehousing uh which anyone can go to tpc.org and check out and check out the results so it's funny how the world went
[392] from like data warehousing to big data and then back to data warehousing again but on big data right so that's what we
[398] call the lake house paradigm yeah you know it's like uh you're taking me back now because um you know since i
[398] Lakehouse Paradigm
[405] started since we started uh uh since we started at scale we started on hadoop
[412] and spark was our first sql engine that we used on on hadoop
[417] and uh you know when when databricks databricks was founded about almost the same time and uh and and what the big
[424] innovation was was to was to put hadoop or put spark in the cloud
[430] and i didn't really realize it at the time it's like okay well why wouldn't people want to manage it themselves but
[435] we clearly saw that companies and enterprises trying to manage clusters for themselves it's just
[442] they're not in the business to manage clusters they're in the business to sell their products you know they're not in
[447] the business to run a cloud um and so you know databricks and and and
[452] databricks um in the cloud and hosting spark and making it so easy really i
[458] think was uh uh the big impetus to making machine learning and sparks so ubiquitous today
[464] is that you sort of took all that all the hard stuff of having to stand up a cluster and then keep it running and you
[471] offloaded it to the cloud and so that's a huge innovation so databricks sql is just the next
[477] evolution of of really spanning out and handling more personas to be able to process data in the cloud on a lake on a
[484] lake house or on a data lake uh so uh so i'm it's very very excited so you guys should be obviously it
[491] should be very proud and and it's uh the future looks so bright um for what we can do for a whole new
[497] new set of personas yeah the interesting thing that uh i just learned was that uh you first
[497] Spark SQL
[504] dabbled with your uh kind of your semantic layer with spark sql is that
[509] about right that's right yeah we were we were writing uh on tickets for reynolds um
[515] i've i filed a bunch of jiras early on and and and uh complaining the reynold
[521] to get spark sql uh to to to work better so um yeah we've been an early proponent
[528] of running sql workloads um on on a um on a clustered environment using spark
[528] First Semantic Layer
[534] so your first kind of semantic layer wasn't donna warehouse then no
[539] um so you know it comes back down to where where my experience was so at yahoo we invented hadoop um and so i saw
[548] for right there that how difficult that hadoop was was not suitable at all for bi workloads back then and then i went
[555] to cloud and uh basically ran into the same thing again um and we happened to be uh one of
[562] cloudera's pilot customers and uh it was um it was actually when uh
[569] cloudera came and showed me impala uh that the light went on in my head just said that okay you know now there's at
[576] least a engine that we could run big data workloads on in a clustered
[581] environment and so that was really the impetus to start at scale was that i always wanted to have that semantic
[586] layer and franco i just chose hadoop because that's where the
[592] the pain was the most acute and so we started there um but obviously uh you
[597] know rode the wave to cloud data warehouses and cloud data platforms like data bricks um and made the platform
[604] work you know universally that's awesome so did i hear you right
[604] clout score
[609] you were at clout like the social media aggregator site that people were like comparing each
[616] other's social scores up so franco what was your clout score i remember really low back then
[622] no okay tell me tell me what low is okay tell me what says okay so the audience should know that your clout score which
[627] is a measure of your social media influence is was between zero and a hundred and um
[634] at the time justin bieber was uh the benchmark he was a hundred uh so so
[640] where did you compare to justin bieber franco oh really well like at that time i didn't have very much on my linkedin
[640] Storytime
[647] this was like 10 years ago right like it was a while ago uh it was it was back in 2000
[653] uh 2013 2014 yeah 2000 2012 2013. about
[658] 10 years ago yeah yeah i was no one back then i was still struggling with warehouses back then i didn't even know
[665] about hadoop uh actually funny story i bypassed hadoop i'm one of probably the
[670] only bricksters that had that went from data warehousing and bi straight into spark like i just that i remember when i
[678] was no no offense to yahoo or whoever created hadoop or anything but during the sales pitch they
[684] were like and then we're going to write intermediary steps out to disk and i was like no yeah i mean disk it's like the slowest
[690] thing in the stack like what do you mean we're going to write out temporary steps to disk no right we're not doing that
[696] how does this stuff process like but this was big data like they were processing petabytes so that was the
[702] only way that you could do it back then but i remember i was like there's no way i could get data warehousing and bi to work there's no like
[709] there's no layer here for me to operate with to actually get good experience for sql analysts and i was like i i can't
[715] make this hadoop stuff work i did however get a pitch from one of your early early
[722] sales people it wasn't you uh because i i remember you but uh i
[727] remember i'll never forget i was at the tableau conference in 2017
[732] and i was running around the the expo right and i was sent there on a
[738] mission they were like figure out what the modern modern data platform of the future is like go interview all the
[744] vendors and and is this hadoop thing going to work and i'll never forget i go by the
[749] atscale booth and you were making t-shirts literally you you had the the printer and uh yes you're there and you
[756] were making t-shirts and i was like this is awesome what is this company
[761] that's why you want to talk to us because we are making t-shirts that's why good luck with that
[767] what that was i didn't know anything about the tech so then i talked to one of your sales people and like it's the semantic layer for your for your uh
[772] hadoop and i was like what does that even mean like do you know what a semantic layer is like i knew what it was but i i kind of i uh whoever the
[780] sales rep was i apologize i kind of made your life horrible that day because the booth was dead at that time and and i
[786] was just struggling uh but i actually i i thought atscale was it's funny before we we kind of were
[793] prepping this and we were talking about like how long it took to really take off uh and i think you're an early innovator
[799] you were at clout i think clout was way too early for it for times you do that today
[805] everyone's going to want to know what their social media score is i mean yeah you know i mean what was interesting franco is that um you know
[805] Cloud Score
[812] the reason why i was attracted to cloud was that um i loved big data but i also liked the advertising model because you
[818] could use analytics against big data um to really turn it into true value um
[824] and that was sort of always of my draw into analytics was that analytics paired with the right kind of business model
[830] could really generate a whole lot of value and i'm a business guy at the end of the day i love business and um i love
[836] i love creating value not just creating tech um but uh you know so so when we know
[842] what was interesting was that the score was actually kind of evil honestly i mean my clout score i think
[848] was um was 27 so so look i was like and i hate social media um i really do um
[855] it's really hard for me to to to post stuff um uh because it's just uh it's
[860] almost like bragging and i it's just like it's like i was i was taught not to do that so in any case it's um so i had
[867] to actually get involved in social media for cloud because you couldn't have uh you couldn't have the um uh the vp of
[874] engineering for cloud have a pad cloud score um it was just not not good but
[880] the secret really was is that uh we um by people registering with clout and
[886] giving us their tokens so that we could start to collect all their their stream their fire hose
[892] that's how you basically got points and got a better score and then you were subject to clout perks which were free
[899] stuff from different manufacturers and businesses because you were a
[904] you were a clout you had clout in a particular topic so we had topics we had all the
[912] different sort of demographic and psychographic types of data coming from facebook we we scored half of facebook
[919] at the time uh of course then we had link we had linkedin uh we had uh uh instagram uh we
[926] had twitter so we had all the social media people and we were able to bring those profiles together and get a
[932] complete view of your social media presence across all of those those different social media systems and and
[939] platforms and that was unique there was nobody who had that data um and so as a data geek being able to apply machine
[946] learning to it that's why we had a hadoop is that we ran machine learning on it but it was really that last mile
[953] of being able to do the analytics on the clout uh audience that's where everything broke down so i
[960] needed that semantic layer that was that was going to handle all this different dimensionality because until i built a
[966] cube on top of hadoop for clout we had no way of seeing a entire view of our
[973] audience so all we knew at the time before that was that justin bieber was a hundred
[979] and we didn't know how many hundreds we had we didn't know if we had too many 20s too many 50s it was basically a big
[986] old guess and so once we had that view of being able to actually do analytics
[992] on a billion people you know and they're a billion people's on
[998] profile social profiles we were actually able to make that score um at least look
[1003] and behave like something that a data scientist would be proud of yeah and you know it's interesting
[1003] Hadoop Data Lake
[1010] around four or five years ago now when for one of my previous companies um
[1017] when we did create a petabyte scale hadoop data lake uh hue out of of uh cloudera i mean you
[1025] write you idiots i need to you remember that right you keep saying i remember you for the audience here hue
[1032] which was their which was their sequel console yes keep going
[1037] so we we evaluated the different vendors we i talked to at scale way back then
[1042] four or five years ago and and we we got you in so you were our semantic layer on
[1049] a big petabyte scale uh hadoop data lake and this was for uh probably a global fortune 5 company back
[1057] then and so we kind of i was i feel proud that at least we at least identified ah this is the key piece
[1064] missing in the hadoop early adopter earlier and the pain was exactly that right even
[1070] though we had spar thankfully mapreduce was who can do it except
[1075] five percent of the india companies right so thankfully there was spark thankfully because of rain ocean he created not just spark but
[1083] even data frame apis and so spark sql started gaining traction and then i remember
[1089] we got at scale work on spark sql to get the performance that that we needed
[1096] and uh so yeah tell me more about that this whole idea of semantic layer
[1101] on big data platforms right because some of our customers will do etl on data
[1107] bricks but they sometimes put the data out in the data warehouse and then the problem they face
[1113] is whatever the analytics they do it's kind of on a stale data because the etl from data lake to data warehouse is
[1119] happening nightly or something right yeah so um it's a common pattern and it
[1119] Why Data Lakehouse
[1125] makes me want to cry honestly because we spend as data engineers we spend all this time carefully curating this
[1132] awesome repository of data and then that last mile if you're a power bi customer or your tableau
[1138] customer you're shrinking it down to nothing you're summarizing all the value away and in tableau it's a tableau hyper
[1146] extract and in power bi it's a power bi premium which is basically analysis services
[1153] under the surface so you're taking big data and making it small and to me that's like a crime it's like
[1160] why did we go and do all this work and assembling this amazing data asset if
[1165] we're only going to look at one percent of it and and probably the most uninteresting one percent because somebody had to
[1172] decide what was worthy and what what wasn't worthy so you have somebody's opinion about what data is important i
[1178] think that's absolutely wrong so you know so that was really the impetus to say why don't we give users i mean business
[1184] users data scientists give the end consumers the choice of what they think
[1189] is interesting and what they want to explore and give them the the tools where they
[1195] can access that but access it with the kind of speed and sla
[1200] um that they've come to require um and and without having to make the
[1206] sacrifices of only dealing with the sliver of the data and that's what i love about atscale and the cement layer
[1212] on top of you know data bricks and the data bricks lake house is that you can have your cake and eat it too you don't
[1218] have to decide what data's worthy you don't have to do that early binding um where you're going to you know create
[1224] aggregate data and all the value away just to make it work in a bi tool or in a uh jupiter notebook yeah that's that's
[1224] SelfService Analytics
[1231] interesting so it's like enabling self-service analytics across your organization on all the data not just
[1238] the aggregated data but structured unstructured all the data and data scientists almost always will say you
[1245] know don't give me access to dev or qa give me access to your broad data right they can copy it
[1252] in a different place but they need access to all the data to gain that value and inside and even tie different data marts and
[1260] data warehouses together to what i call to do pan edw analytics right you could
[1266] have multiple data warehouses but like marketing data warehouse sales data warehouse and so on but only when you
[1272] put it together all your data marts your raw data iot data and then you do analytics on all of it
[1279] that's where you get your aha ideas aha moments and you gain value using machine learning
[1279] Semantic Layer
[1285] yeah yeah and so harm is like you know that's a good example because you have you have
[1290] your marketing domain experts they understand the marketing and marketing data and also the the what what it means
[1295] in terms of the dimensions and metrics around that shipping team understands the shipping data finance team
[1301] understands their finance data so we really like the fact that it's a semantic layer you can create these semantic models you can let the domain
[1308] experts define those models but then you can bring those models together and and
[1313] like lego blocks right and so you can see the full picture without having to know and know the full picture because
[1320] the person in shipping doesn't understand finance and the person in finance may not understand shipping but
[1325] if you can sort of put that knowledge together in that knowledge graph in that model and you don't sacrifice the
[1332] granularity of the data then you know sky's the limit in terms of understanding what's going on in your business
[1332] Data Warehouse
[1338] yeah i often refer to as data warehousing as
[1343] aggregating away the signal because as soon as you do aggregates you lose signal to noise right any signal that
[1349] was in that data is now gone because it's been aggregated away and so it's useless for machine learning engineers
[1355] give a machine learning engineer a warehouse they're gonna be like i can't do anything with this there's there's no signal here it's all
[1362] aggregated like i can't you can't learn on aggregate data and they always need access to the finer
[1368] definer data what gets lost from in my perspective and one of the reasons why i really like the approach
[1375] that you're taking here especially with atscale and databricks is that what if you could
[1381] automatically behind the scenes understand what these queries are doing
[1386] right and then create objects that accelerate the queries but if you still want to look at the
[1393] data like you want to drill down the data's still there that scale just kind of creates this
[1399] efficient layer behind the scenes you didn't have to do anything like it just kind of
[1404] builds precomputed aggregates but it doesn't actually replace what was there right it just gives you like this
[1409] performance layer you want to drill down you want to go deeper you want to get the detailed level it's all there it's
[1414] not like aggregating data in a warehouse so i really like the the approach that
[1420] you're taking here i do have a question for you putting a cube on hadoop
[1426] 10 years ago that was a crazy idea yeah so obviously it was a it was a it was a sql
[1432] server analysis services cube too frankly oh really so you hooked up ssas
[1438] i thought you built your own cube technology no no ssas pointed it to hadoop yes and you
[1444] basically built cubes that was the title that was that's what i did at yahoo and that's what i did at uh at cloud and um
[1451] and uh the pro though so first of all what was good about that what's good about that is it you you touched upon it
[1458] right what you just said a few seconds ago which is that you can't aggregate and aggregate the value away aggregate
[1464] the grain uh the details um and and for our advertising business at
[1469] yahoo the details were okay where did the ad show what site was it what was the placement meaning what part of the
[1476] page was it on what was the format of it was was it a banner on this or was it a
[1481] square uh was it a link um and then who clicked on it were they male with a
[1486] female uh were they interested in sports there's it's it's a highly dimensional problem so um so what i did is that i
[1494] put that cube on top of that data in hadoop um and that generate uh that
[1500] generated 50 million dollars of value um just with that one cube
[1505] um so the goodness is that by allowing our our ad optimizers to get that sort
[1510] of view of data they were able to tune those those campaigns and make a lot more money for our our advertisers and
[1518] and for our and for our publishers and make a lot more money and perhaps for um
[1523] yahoo as well um but you know the problem franco was that trying to pre-compute everything
[1529] um it's just it's an it's it's an exponential problem it's a logarithmic problem and um at the end of the day it
[1537] just couldn't scale um and so i still was left having to choose what data was
[1542] worthy um and uh and and it was uh it was clear that the
[1548] the semantic layer that comes built into a cube architecture
[1553] that's the value is the semantic layer meaning measures dimensions hierarchies
[1558] the ability to do crosstabs and anything by anything that is the value the tech behind it was
[1565] garbage now it wasn't garbage when it started it was actually really good it just couldn't scale to today's data and
[1572] so that's what we did we said don't throw the baby out with the bathwater which is what a lot of companies have
[1578] done right they said oh you don't need dimensions and measures anymore you can just write sql and i just think that's a
[1584] crime because i think that you know there's a there's a small amount of people who can be proficient enough to
[1590] ask a question in sql and our goal was to get data make all data like soham
[1596] said available to everyone not just a data engineer and to do that we needed
[1601] to have a semantic layer on top of big data and we needed to make it work um
[1606] and nobody's at the time everybody said we were crazy and we were never going to be able to make it work and that's all
[1613] you got to tell me is that it's not possible and i'll work extra hard to prove you
[1618] wrong i hear you when they told me you couldn't do data warehousing on a data lake three years ago i was like hold my
[1618] How much did you mess with proactive caching
[1623] beer all right one question for you one question about that whole story
[1630] how much did you mess with proactive caching before you got
[1636] frustrated and started thinking about how to do it better
[1641] um are you talking about in the in the olap world franco yeah so like ssas one of the things you touched on was like
[1647] it's it's a on problem to keep this thing up to date right and so one of the common ways that people in the ssas
[1655] world got like ability to stay ahead of it was to enable proactive caching which
[1660] actually brought up a whole slew of other things to actually keep track of right and it's like i could just in my
[1667] mind i was going back in time with my ssas days and being like i wonder how much dave messed before active caching
[1673] until he was like forget this i'm done we're gonna do something else franco it didn't didn't work um because
[1673] Why did you use Netapp
[1679] because dimensionality was too was too bad um but when you get too many dimensions
[1684] then you have also the depth of data because you know i don't know that i think that was a half a million dollars just for
[1690] that one computer right and i needed a couple of them because i needed failover um and um and then and then in terms of
[1696] disk i couldn't get enough disk so i had to use netapps um and netapp sounds sand so so what
[1702] would happen is that the way i had to update that is i had a cube a and a cube b
[1708] and cube a while that was serving all the queries i would be updating qb
[1713] with the latest data and then what would happen is that when q b's update was done and i could do this twice a day
[1720] um then i would do is i would do a swap so i would do an ip swap so that now the
[1725] traffic was pointed to qb and then i would start to update cube a so um
[1731] that was first of all anybody who was querying cube a when i did the switch they were
[1736] just their queries would just fail because it's like i had to cut them off of the knees nothing else i could do
[1742] um and that was actually okay people didn't complain too much about that but that switchover was uh was so scary that
[1750] um one of my engineers accidentally deleted one of the snapshots that we're using
[1755] for our netapp and that meant that there was no data for that cube for a whole
[1761] week and why was it a whole week because it took us one full week to build that cube
[1766] from scratch for three months of data one with seven days of 24 7 processing
[1771] so now i had the whole advertising business for yahoo having no analytics for one week so you want to know where
[1779] the idea for atscale came from what came from that very very painful experience of having to um you know not be the most
[1786] popular guy in the advertising business at yahoo
[1786] Data warehousing
[1792] this is no this reminds me of even in the data warehousing world it used to take so long to load proper data houses
[1799] even if we had netiza or ortera data that we used to create a copy of the
[1805] star schema or in business objects or cognos and same thing after the load is done
[1811] we rename the the table underscore backup and the the loading tables that we are
[1818] loading becomes the live table and like you said everything breaks thankfully with db sequels delta format you don't
[1825] have to do that anymore because internally we keep like two copies anyways so none of this happens but so
[1832] tell me this in the webinar to you and frank cording are you going to show us how you how at scale can
[1838] manage distributed cubes um yeah yeah tell me yeah for sure
[1844] how do you make that one giant cube in one computer and make it work on uh in a
[1850] distributed fashion well you know well here's the thing right it's like the whole architecture is we're always going to leverage the
[1850] Ecosystem
[1857] ecosystem we're gonna i call it standing on the shoulders of giants and guess what you guys are the giants
[1863] and we're standing on the shoulders of you so we're standing on the shoulders of lake house that means that you know don't try to be the compute layer we
[1870] don't want to be the compute layer we want to be the router uh we want to be the business the the intelligence router
[1876] um and gets people the data they want so the way we do that is that we take uh
[1881] you know we publish the semantic layer in a number you know we publish a semantic layer and it can be consumed in
[1886] a number of different dialects if you are a data scientist your dialect's probably python or sql and you can talk
[1893] to the semantic layer with python or sql but if you're power bi it's dax if
[1898] you're excel it's mdx if you're an application developer it's probably rest so for semantic layer to
[1905] work you've got to be able to handle all those different inbound dialects and then so on what we do is we take that
[1911] logical those logical queries and we translate them to physical queries and generate data bricks sql sql
[1919] um and we let you do the work so there is um i don't worry about you know scaling at scale or our customers don't
[1926] scale at scale they scale data bricks and they let data bricks scale data
[1931] bricks so that was always the idea as like i don't want to be in the scale business you shouldn't have to scale
[1937] your analytics platform you just need to scale your data platform and then your analytics should
[1943] scale with it awesome awesome so databricks equal endpoints will scale
[1948] scale up scale down when there's not going on and and you got you guys
[1954] what i loved about atscale is you pass the queries that customers are writing and you figure out whether a cube or an
[1961] aggregate is needed or not so no one people don't even have to predefine all the materialized views
[1968] right because you do it for them so in that sense you are almost like auto etl
[1974] creating materials on the flies and you analyze oh well no one is using some of the cubes so you
[1980] delete them as well that's fantastic awesome yeah and you know it's like it's even though it may look like a cube to a
[1980] Aggregate Tables
[1986] tool like power bi or excel it's not a cube at all um it's a it's it's a set of
[1992] aggregate tables and those aggregate tables are delta delta tables stored in on data bricks like house so the data
[1998] never leaves the platform and that's the other part right it's like you know you don't want data leaving the data
[2003] platform you spend all this time not just curating this awesome data set but also securing it and then now it's going
[2009] to go and like fly away and fly away into somebody else's system who you don't know what the
[2016] security model is um and it doesn't matter because it's another security model so the whole point is to secure it
[2023] once um and if you screw it once then you should be able to read it many and depending on who you are if you're
[2029] in finance with the upscale semantic layer you're going to see the finance fields and and revenue fields uh if
[2035] you're an hr you can see social security number but if you're in marketing you're not going to see you know revenue or
[2041] social security numbers because you don't have rights to see that so you should be able to secure that and secure
[2046] that once in one place and that's really the value that's really the extra added value of
[2053] going for an integration first approach versus trying to do everything ourselves
[2053] Improved Refresh Process
[2059] so uh if i understand you correctly then if your your system utilizes the underlying compute so as databricks
[2066] makes databrick sql endpoints more efficient your q your your processing
[2071] kind of your your refresh process actually will get sped up as well so by leveraging the the kind of the the
[2077] standing on the shoulders of giants if you will as like the whole stack improves it's
[2082] kind of like it just goes all the way down it's improvements all the way down the stack which is really nice
[2087] one question to you is you so we heard that refreshing uh how many hundreds of terabytes took a
[2094] week rebuilding it back then 24 terabytes 24 terabytes right 24 terabytes what
[2101] what is one of the biggest cubes you've seen at scale today and then how what's
[2106] the typical loading time with today's kind of compute technologies i don't know if you've done one on data brick
[2112] sql but just in general like what like what's the difference to so we know just like how much this technology has
[2117] matured over the years to do like a 24 terabyte cube nowadays well so first so first of all we don't
[2123] have to build a cube so we don't have to actually do any pre-processing so as soon as i define a semantic model and
[2129] they publish it we're querying um we're occurring in one second later um and
[2134] you're requiring live data so that's the very different from the architecture of old where you pre-calculate and you
[2140] build a cube before you can actually query it so um so but but it's about aggregates right and refreshing the
[2146] aggregates and so we're refreshing the aggregates behind the scenes uh when uh you know whenever the data
[2151] changes and so uh a good rule of thumb like actually i just did a i just did a
[2156] benchmark on databricks sql um and um we we did um uh we did 10 terabytes right
[2164] for the tpcds we did your we did you we used your data you had we did your test
[2169] 10 terabytes of tpc ds data that's um about 55 billion rows of data
[2176] and we can update aggregates in less than 20 minutes uh fuller full refresh
[2181] so not even incremental refresh so rather than it taking seven days to do 24 terabytes you know we can do um 10
[2189] terabytes in 20 minutes so um and that's for a full refresh which you never do
[2194] you only you only do an incremental refresh with just the newly added data so it's lightning fast and the queries
[2201] against that um are fast or faster than what we got out of analysis services so
[2206] uh that's that that's really the state of the technology is that you know again keep keep the good stuff the semantic
[2212] layer toss out the bad stuff the you know the physical architecture
[2217] so what you did was basically take all the definitions of the semantic layer
[2223] and then you built your own back end basically just almost like just-in-time semantic layer where it will build the
[2230] objects as they're coming in so the reason why you can query it right away is because the protocol in which comes
[2235] over the wire you're interpreting the kind of the cube command but it will
[2240] build the constructs kind of like as you're clearing it so you don't have to do like something like a proactive
[2246] caching or figure out your schedule and when your cube is going to refresh because it's always working in the background is that right
[2246] Aggregates
[2252] that's right yeah so so we're we're creating aggregates on the fly based on user query behavior so so
[2258] franco if you come in and you say i want to see uh i publish a model and it has uh 10
[2264] different dimensions and of those 10 dimensions you say show me revenue by region um for um
[2272] for last month that's that's basically two dimensions and one measure right so revenue is the measure time is and uh
[2280] region is other two dimensions and so based on that we'll create a a reusable
[2286] aggregate table based on those dimensions but we'll do we'll do something better than that we won't just say
[2291] it's not a query cache so we don't just say let's just we're just going to do the franco query and make that table we'll actually see
[2298] what's around it and when we'll create an aggregate that's going to be much more useful than just that query so so
[2305] if you're not just asking for region you're asking for um you know you asked for i want by country which is a region
[2312] and then i want to drill down to a state and then from state to city um and then some city to zip code that's all going
[2318] to be satisfied by that single aggregate and if i want to buy go by time i don't
[2324] want to use by last month i want to do it by quarter and do it by quarter back to 2000 you know it's 15. again that
[2331] aggregate is going to serve that query um and you know by by revenue i don't want revenue now i want gross margin as
[2337] well again that aggregate will serve that so we're really smart about you say
[2343] proactive caching we're very smart about proactively understanding the intent of the query and then expanding it and
[2349] creating an aggregate structure and having a table behind the scenes a materialized view that's going to be
[2354] much more useful and um than just what you asked for almost like proactive aggregating
[2361] it is that's exactly what it is and it's not just that we just don't have we don't have to wait for your signal
[2366] meaning a query we also know by the structure of the model so um that we can
[2371] actually proactively build aggregates based on things like when you build a dashboard when you're building a
[2377] dashboard in tableau you can imagine you're dragging over dimensions and tableau is filling in all the the values
[2384] in that dimension so if you drag over let's say country that's going to show you all the different countries in your
[2389] world well that's a distinct query that has to be generated against the platform and if you're dealing with um you know
[2396] like our like our our customers have literally hundreds of billions of rows that means that's going to be a query
[2403] that's going to do a distinct on country against 100 billion rows you can't build
[2408] that dashboard because that that query is just going to time out in uh in tableau what that scale will do is we'll
[2414] understand that's a dimension and we'll have that ready and set and serve that from an aggregate so
[2420] dave so in instant one when you're building that dashboard you're going to have lightning fast performance because
[2426] we already knew what you were about to do that's interesting
[2432] yeah so we're getting we're geeking out here
[2437] guys i i i think that's that's that's excellent so essentially you kind of
[2437] Dimensions
[2443] like parse the the model and then you're already aggregating your dimensions because i can't tell you like it is a
[2450] super common task did you count your dimensions like and you just kind of know that and you're like all right you know what so it's like the
[2457] the industry experience not just the industry experience but the the business experience that you have with these things that you implemented into the
[2463] model is kind of the real value proposition here is that you've you've been designing these cube cube without a
[2470] cube let's call it semantic layer right but uh but but cube without the cube technology like how would we rebuild
[2476] this thing from scratch using modern technology and you're like what all of the things that i liked about it and one
[2482] of the things i didn't like about it kind of like what we did with lake house we we knew we liked databases and
[2487] warehouses we knew we liked data lakes but there were things we didn't like and we kind of brought the best of both worlds yeah
[2487] No more loading the data warehouse
[2494] yeah i mean nobody likes to load the data warehouse right so you've like taken away the loading of the data warehouse that's freaking awesome
[2501] you know who likes to load it you don't have to load it you just want to be when it gets written you want to query it instantly
[2506] um and and you know just on your point franco like that the reason why we knew we can we know to
[2512] do that is that if we just had a bucket of tables you had just a catalog of all these raw tables we don't know what the
[2519] dimension is we don't know which columns are what so we don't know what to do but when somebody when a subject matter
[2525] expert says that this is time and i and this is my hierarchy that i want to use
[2530] with time um and this is where my my my location is and this is the rollup we
[2536] want for our location they told us everything we need to know um and so it doesn't work without the
[2543] data model so if you can't just take a raw set of tables and think that somehow
[2549] the machine can can can work it out we're working on that i'm working on that so that one day we don't need the
[2555] human to build a semantic model but darn it we still need humans because they're
[2561] pretty smart about being able to help us identify uh what's interesting and what's not
[2561] Business domain
[2569] so one of the questions i have about your product uh we've been talking about uh business domain and how
[2575] this technology really needs to enable the business to do what they need to do almost like
[2581] as technology practitioners it's our goal to to to give them the tools they need
[2587] to get their job done and they don't even know our name right like that that would be like ultimate success is if i
[2593] could just implement the things and they're off and running and they're being successful in the business they're
[2599] they're they're making great uh business value decisions kind of like they did back in yahoo with with ad optimizations
[2606] who knows what it is um looks like we're running out of time so this will be this could be one of the
[2612] last questions if we're running out of time but uh who uses at scale because i'm a
[2617] technology practitioner a lot of times cubes had to be built by an engineer right like you needed it to
[2625] hire like a consultancy to build your cube or engineers and developers to build your cube when you're talking
[2631] about like atscale it kind of seems like these aren't engineers these are business people going into the ui and
[2636] building these models can you talk a little bit about who uses that scale and kind of like how that works in the the
[2642] product life cycle and delivering business value yeah that's a great question frank and
[2642] Author
[2647] you touched upon a couple ideas here first of all there's the author of the model there's a subject matter expert
[2654] that's me and so it goes back to that whole the shipping the people of the business unit that own shipping on or
[2660] the finance team they understand their data they understand the shape of the data and they understand what what's
[2665] what revenue is and what gross margin is if you're in finance so so it's up to them to create that semantic model
[2671] because they're the domain expert so if you take that whole data mesh concept you know they're the they're the domain
[2676] owners and so they can create and they can use that semantic model to express their business logic and that's how they
[2683] can share that business logic with everyone else so they're the publisher they're the author and then you have the
[2689] consumers and the consumers can be it can be a business analyst as a persona it could be a data scientist it could be
[2695] an application developer and they're the consumers so uh so you can think of it as like when you create data products
[2702] you have the subject matter expert who's adding their knowledge to that to that
[2707] semantic model and that's the way they communicate with the rest of the business and then those those subject
[2713] matter experts can then put together those domain models to create composite views so you have even more power into
[2721] seeing different interactions across the business without again having to understand the whole business
[2728] so um you you there is no shortcut you still need to have somebody a subject matter expert in the equation but it
[2735] doesn't have to be a data engineer franco to your point it can be a business person who's going to use a ui
[2741] to define or code if they're come more comfortable to use their knowledge and to express it as a
[2748] model and share it with others um so i think it's it's it is author once and it's used many um yeah and you
[2757] know that's what it is yeah and and this is a great question by franco right and a lot of time people
[2757] Everyone will write SQL
[2763] sometimes come and say well everyone will write sql i don't think that's practical uh a couple of reasons right when you
[2770] have thousands of tables or even within your subject area you got to understand the relationships between them right so
[2777] concept of modeling relationship hierarchies definitely but some real life examples right so for
[2784] example i work for some pharma companies and they have thousands of uh medical
[2789] pharma reps right their job is actually sales so they have to go and visit doctors drop the drug samples figure out
[2797] whether the doctors are writing their prescription or someone else's and so on and then for for to do their job they
[2804] need to see the data right and they're not sql experts they are like traveling meeting doctors and so on so in this
[2811] particular example they have a dashboard from like our data warehouse where they
[2816] will cut across the dimensions of you know it could be region drug doctors their specialties and so on so
[2823] they use the the semantic model to make decisions to get their job done same thing look
[2831] look at all the warehouse workers in in some big companies or thousands like there are restaurant
[2837] companies with thousands of restaurants and the managers want to either input some data or look at some report make
[2842] some decisions right so semantic layer need is super real and while the
[2849] business analyst and the data engineers can write sql this is a one more layer
[2854] of abstraction on top of it which makes the data uh accessible
[2861] for the entire company so it's super important concept you shouldn't forget when we build a modern modern data stack
[2861] Databricks and Data Lakehouse
[2868] yeah and when you look at sort of the combination of our two companies right where when you have a great platform
[2873] like databricks where you're able to take data from collection and put it into a repository in a lake
[2879] house and then you have the the engines and tools to be able to do super fast queries against that lake house um then
[2887] you know we're just the where the sugar right um or the semantic sugar that we can sprinkle on top to make i think a
[2894] really delicious dessert oh sorry sorry no sorry for that sorry
[2901] awesome semantic sugar i love it i'm using it well i i've got one last question after
[2906] i just heard you guys talking about that something just clicked in my head so what you're saying is with your with at
[2912] scale that you can have domain smees domain subject matter experts across your
[2918] company and essentially they're enabled with your software they can build they can put all their business knowledge for
[2924] their expertise into into the software and then somebody else can use it but
[2930] not only that uh i think i think i wanted you to show me this maybe in our webinar how do you
[2935] connect can you connect up maybe like the models from across the organization and bring
[2941] them together is that possible absolutely because we you have a library of models
[2941] Conform Dimensions
[2946] and those those models can be joined together with conformed dimensions this
[2952] is your old can this is your old kimball days so this is like this is what kills me it's like we can't forget about this
[2957] stuff these are important concepts and a conform dimension is time is the most common conform dimension so everybody
[2965] reports on time so i can take my finance which is on my revenue and i can take my shipping uh details and i can and i can
[2972] go ahead and lay them side by side and connect them up just using a time dimension
[2977] because that's the conform dimension and that's the glue that allows you to connect these lego blocks of these different data models which were
[2984] authored by different smes now smees can then join those models and those views together with their own models and
[2992] create composite views that that really replicate the business create that digital twin of the business that
[2998] everybody always likes to talk about but do that with software that's awesome
[3004] yeah awesome so it's like databricks is that three layered cake with bronze silver and gold and then you split
[3010] at sugar on top i like it
[3019] i love it so awesome this enables us to do data warehousing directly uh on on on the
[3025] databricks lake house awesome looking forward to these books
[3033] we got a jam so uh look everybody listeners uh uh pl please join us on on thursday april 21st 2 p.m eastern and uh
[3041] soham and franco thanks so much for uh joining and franco it's going to be fun so let's uh let's go geek out and show
[3048] show everybody what we can do together thanks for having us thank you
