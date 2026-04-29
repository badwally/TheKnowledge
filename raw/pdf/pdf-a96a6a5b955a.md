---
id: pdf-a96a6a5b955a
type: pdf
title: Hino_Burke_2020
url: ''
authors: []
ingested_at: '2026-04-29T16:21:54Z'
content_hash: sha256:53dcab30041689834dd46358ea02dac13d353f2a1a54b3a6209d490feb62db57
source_path: raw/pdf/pdf-a96a6a5b955a.pdf
domains:
- cycling-and-fitness
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 31
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/Hino_Burke_2020.pdf
published_at: '2020'
---
NBER WORKING PAPER SERIES
DOES INFORMATION ABOUT CLIMATE RISK AFFECT PROPERTY VALUES?
Miyuki Hino
Marshall Burke
Working Paper 26807
http://www.nber.org/papers/w26807
NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
February 2020
M.H. was supported by the Sykes Family Fellowship in E-IPER. We thank C. Field, K. Mach, D.
Lobell, S. Heft-Neal, R. Molina and seminar participants at Stanford and UNC for helpful
comments, the Stanford Geospatial Center for assistance with historical floodplain maps, and
Stanford Libraries for providing the Corelogic data. The views expressed herein are those of the
authors and do not necessarily reflect the views of the National Bureau of Economic Research.
NBER working papers are circulated for discussion and comment purposes. They have not been
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies
official NBER publications.
© 2020 by Miyuki Hino and Marshall Burke. All rights reserved. Short sections of text, not to
exceed two paragraphs, may be quoted without explicit permission provided that full credit,
including © notice, is given to the source.

Does Information About Climate Risk Affect Property Values?
Miyuki Hino and Marshall Burke
NBER Working Paper No. 26807
February 2020
JEL No. Q54,R3
ABSTRACT
Floods and other climate hazards pose a widespread and growing threat to housing and
infrastructure around the world. By incorporating climate risk into asset prices, markets can
discourage excessive development in hazardous areas. However, the extent to which markets
actually price these risks remains poorly understood. Here we measure the effect of information
about flood risk on residential property values in the United States. Using multiple empirical
approaches and two decades of sales data covering the universe of homes in the US, we find little
evidence that housing markets fully price information about flood risk in aggregate. However, the
price penalty for flood risk is larger for commercial buyers and in states where sellers must
disclose information about flood risk to potential buyers, suggesting that policies to improve risk
communication could influence market outcomes. Our findings indicate that floodplain homes in
the US are currently overvalued by a total of $34B, raising concerns about the stability of real
estate markets as climate risks become more salient and severe.
Miyuki Hino
University of North Carolina at Chapel Hill
mhino@unc.edu
Marshall Burke
Department of Earth System Science
Stanford University
Stanford, CA 94305
and NBER
mburke@stanford.edu

1 Introduction
Global economic losses from natural hazards have increased nearly ten-fold since the 1970s, with
the United States experiencing $300 billion in losses in 2017 alone [Bouwer, 2011, Swiss RE, 2019,
NCEI, 2019]. This trend is primarily driven by an increase in the number of people and amount
of wealth concentrated in locations at risk from tropical cyclones, floods, and other hazards
[IPCC, 2012]. Managing development in risky areas is therefore critical to limiting losses from nat-
ural hazards, particularly as climate change alters the frequency and intensity of extreme weather
events.
Oneviewisthatmarketsshouldbeabletomanagethisriskefficiently. Withcompleteinformation,
efficient real estate markets capitalize flood risk: the potential flood damage reduces the value of
flood-prone property relative to otherwise identical low-risk properties, which in turn reduces the
incentive to develop in flood-prone locations. In the United States, to support market efficiency,
thefederal government produces publicly-available mapsthatdelineate areaswitha>1%chanceof
flooding in any given year, referred to as the Special Flood Hazard Area or the “floodplain.” These
Flood Insurance Rate Maps are the primary source of information on flood risk for individuals and
communities, and they are often used as the basis for other local land use regulations. Accord-
ingly, the federal government regularly budgets over $100M annually for floodplain mapping activ-
ities, with FY2018 funding of $262.5M [115th Congress, 2018, Congressional Budget Office, 2017].
Properties purchased with a federally-backed mortgage in the floodplain are required to carry
flood insurance, which is overwhelmingly provided by the National Flood Insurance Program
(NFIP).NFIPpricingdependsheavilyonwhetherthepropertyisinsideoroutsideofthefloodplain
[Kousky et al., 2016].
Past research offers mixed evidence on whether markets efficiently capitalize the flood risk infor-
mation in these maps. While the majority of studies suggest a price penalty for being in the
floodplain, point estimates range from a -75.5% penalty to a 61.0% bonus [Beltr´an et al., 2018].
This large range likely reflects the narrow geographic scope of past work, with individual estimates
often based on data from a single county or city (Figure 1). In addition, the vast majority of these
studies are cross-sectional and thus vulnerable to bias if researchers cannot control for the many
factors that are correlated with both flood risk and prices. Of the few non-cross sectional studies,
results are mixed: in Centre County, PA, rezoning into a floodplain reduced property values, but
rezoning out of a floodplain had no effect [Shr and Zipp, 2019]. In New York City, NY, the release
of preliminary new flood maps reduced property values, but the effect differed sharply between
properties that had and had not flooded during Hurricane Sandy [Gibson et al., 2019].
Here we conduct the first nationwide evaluation of the effect of floodplain presence on property
values, whichwerefertoasthe“floodzonediscount.” Weconstructanoveltimeseriesoffloodplain
maps by gathering CDs containing historical floodplain data from multiple libraries, converting the
2

data into shapefiles, and overlaying them with current floodplain maps. We isolate the effect of the
floodplain maps on property values by taking advantage of both spatial and temporal variation in
flood zone assignment. The floodplain maps are highly spatially granular, such that the floodplain
often splits houses on the same block or divides one side of the street from another (Figure S1). In
addition, the maps are updated at different times around the country (Figure S2) based on factors
including the age of the current floodplain map, the amount of population and assets located in the
area, recent rates of development, and availability of new data [National Research Council, 2009].
We combine these changes in floodplain maps with detailed proprietary data on the universe of real
estate transactions in the US to implement three methods for estimating the flood zone discount:
panel, difference-in-difference, and cross-section. In the panel approach, our preferred method,
we estimate the flood zone discount by comparing individual houses to themselves over time as
they are rezoned from outside to within the floodplain due to map updates, controlling flexibly
for changes in local market conditions. The difference-in-difference mimics this approach, but in-
stead of comparing a single house to itself, compares small geographic areas over time. Finally, for
the sake of comparison to earlier work, we compare floodplain houses to non-floodplain houses in
a cross-sectional analysis, controlling for a suite of location- and property-specific characteristics.
This latter method, while common in the historical literature on flood risk, is no longer considered
areliableapproachforcausalinferenceintheappliedeconometricsliterature, giventhenearimpos-
sibility of controlling for all characteristics that might be different across properties but correlated
with flood risk.
Importantly,thefloodzonediscountcapturestheimpactoftheinformationembeddedinfloodplain
maps and differs from the flood risk discount for multiple reasons. For example, flood risk is
continuous, not categorical as depicted in the maps. In addition, the map updates often capture
changes in flood risk that pre-date the map itself, such as large-scale development that increased
impervious surface cover. The map update changes key information available to the market about
the level of risk, rather than changing the “true” risk. For most buyers, the flood zone designation
also introduces the mandatory insurance requirement and thus affects their total financial costs.
Becausewefocusonthefloodzonediscount,wedonotaimtoevaluatehowaccuratelythefloodplain
maps capture “true” flood risk; rather, we take the floodplain maps as provided and estimate the
effectoftheinformationtheycontain. Thesemapsaretheonlynationwide,publicly-availablesource
of information on flood risk, and they have been shown to positively affect voluntary insurance
purchase [Shao et al., 2017].
In the second part of our analysis, we examine spatial heterogeneity in our estimated effects to
evaluate drivers of the flood zone discount, relying solely on our preferred panel specification. We
focus on the role of information about flood risk, as it has previously been identified as an obstacle
for real estate market participants. For example, in a survey of Colorado floodplain homeowners,
only 8% found out about flood risk to the property before they made an offer, and 69% said they
3

would have changed their offer had they known about flood risk and insurance prices beforehand
[Chivers and Flores, 2002]. In addition, the passage of a stringent law in California that required
disclosure of flood risk during real estate transactions was found to increase the price penalty for
flood risk [Troy and Romm, 2004]. We study two plausible sources of variation in information
about flood risk: whether the buyer is a commercial buyer, a group likely to have more experience
purchasing real estate and greater resources to seek out flood-related information than individuals
and households, and the stringency with which states require sellers to disclose information about
flood risk and flood history to buyers. In both cases, we hypothesize that increased information on
the part of the buyer will lead to a larger flood zone discount.
2 Data and empirical approach
2.1 Data
Floodplain maps For current floodplain maps (officially “Digital Flood Insurance Rate Maps”),
we downloaded state-level extracts of the National Flood Hazard Layer (NFHL) from FEMA’s
Flood Map Service Center in March 2018. The NFHL is a continuously updated digital dataset
thatrepresentsthecurrenteffectivefloodplainmapsforthosepartsofthecountrywheremapshave
been digitized. For historical floodplain maps, we obtained Q3 Flood Data, the first digitization of
floodplain maps. These were initially produced in 1996 and updated through May 1998. The Q3
data cover 1,289 counties.
Each property (and thus, each transaction) was overlaid on both the current and historical flood
maps and assigned one of three conditions for each time period: in a Special Flood Hazard Area
(SFHA, equivalent to the 1% floodplain), outside of the SFHA, or unmapped.
Dates of map updates FEMA’s floodplain maps are updated sporadically and at various geo-
graphicscales,rangingfromaportionofacountybeingupdatedtomultiplecountiesbeingupdated
at once. The current maps include the date they went into effect, so they are taken to be in effect
from that date until the present. The Q3 maps are assumed to be effective from 1996. To identify
map updates that took place between the Q3 maps and the current maps, we use the FEMA-issued
Compendia of Flood Map Changes from 1998-2013.
We matched the map updates to properties based on the Community or County ID in the Com-
pendium of Flood Map Changes. Earlier floodplain maps were issued by Community, which is a
sub-county level, and more recent maps have been issued by county. We searched the compendia
for updates that matched either a property’s community or county and assigned the associated
map update date to the property. Because we do not observe exactly which portion of the county
4

map is updated, we conservatively assumed that any map update within the county affected the
entire county.
We only have access to the floodplain maps as published in the Q3 data and the current effective
maps. Depending on the frequency of map updates, we observe different portions of a property’s
floodplain status over time. If a property has never experienced a map update, or if there has been
only one update between 1996 and the present, then we observe its floodplain status throughout.
If there are multiple updates, for instance in 2004 and again in 2008, then we can use the historical
map until 2004 and the current maps from 2008 to the present, but we do not know the property’s
floodplain status from 2004-2008 and any sales during that time are omitted.
Real estate data Property sales and characteristics data are sourced from CoreLogic (cid:13)R, a data
vendorwhichcompilesdeedtransactionrecordsandpropertytaxrollinformationfromU.S.County
Assessor and Recorder offices. We included the deed transaction records for all 50 states and the
District of Columbia in our analysis. Matching the time period of the flood maps, we included sales
beginning in 1996 and ending in 2017.
Transactions missing a parcel identifier, sale price, or location coordinates were removed. We
also removed transactions that were part of a split or multiple parcel sale, instances of a parcel
transacting multiple times on one day, and non-arms-length transactions, such as foreclosures.
Transactions were assigned, if possible, to the month and year of the sale date. If transactions were
missing a sale date, we used the date that the sale was recorded. If there was no month and year
listed for either the sale date or the record date, the transaction was eliminated from the data set.
Only parcels identified as single-family homes were included in this analysis. Property characteris-
tics such as the year the property was built or substantially renovated, bedrooms, bathrooms, and
square footage were also sourced from CoreLogic (cid:13)R. These are taken from the most recent tax
assessment available, typically 2016 or 2017, and thus reflect approximately present-day property
characteristics. We removed sales that occurred before the property’s most recent renovation date
toensurethatthepropertycharacteristicsapplytothepropertyatthetimeofsale,andweremoved
properties with a most recent renovation date either unknown or before 1968.
Summary statistics for our data are available in Table S2. Property records cannot be released
under the data use agreement with CoreLogic.
Other property characteristics To obtain the distance from the property to the nearest river,
lake, or ocean, we used the US Geological Survey’s National Hydrography Dataset1. Feature code
566 from the Flowline layer was used to map distance to the coast, features codes 390 and 493 from
1Available at https://www.usgs.gov/core-science-systems/ngp/national-hydrography/
access-national-hydrography-products
5

the Waterbody layer were used to map distance to the nearest lake, and feature code 460 was used
to map distance to the nearest stream or river. We calculated the minimum distance from each
property to these water features in R.
Properties were mapped to their corresponding census block group and tract using the US Census
Bureau’s TIGER/Line shapefiles2. The TIGER/Line shapefiles were also used to map the distance
from each property to the nearest primary road and secondary road.
2.2 Benchmarks for the flood zone discount
Efficient market discount We estimated the efficient flood zone discount as the present value
of a future stream of insurance payments as a fraction of the home’s total value:
(cid:80)∞ P
t=0 (1+r)t
FRD =
V
whereP representstheannualpremium,r isthediscountrate,andV isthetotalvalueofthehome.
National Flood Insurance Program premia depend on numerous factors, including the elevation of
thehome,ifithasabasement,andwhetherornotitisexposedtowaves. Weuseddataoninsurance
premia from Kousky et al. for houses that are not exposed to waves, built at or two feet above
base flood elevation, and have at least two floors with no basement [Kousky et al., 2016]. These
policies approximate a lower bound for non-subsidized insurance costs as premia are substantially
higher for houses exposed to waves and at lower elevations. While many communities now have
building codes that require floodplain properties to be constructed at or slightly above the base
flood elevation, many older buildings are lower.
We considered households insuring for either $250,000 or $125,000 of coverage. To most closely
approximatetheefficientfloodzonediscount,weassumedthatthehouseholdsarefullyinsuredwith
the lowest possible deductible of $1,250 and that the insurance coverage is equal to the value of the
structure,suchthattherewouldbeminimaluninsuredcosts. Wecalculatedthetotalpropertyvalue
V based on the structure value. On average in the US in 2016, the structure comprised 71% of the
total home value, with land making up the remaining 29% [Lincoln Institute of Land Policy, 2016].
We then averaged our four estimates of the flood risk discount: for coverage amounts of $250,000
and $125,000, at elevations equal to and two feet above the base flood elevation. We repeated this
process under three discount rates r of 3%, 5%, and 7%.
Present value of insurance Numerous past studies report data on housing prices and the
average insurance premium in the study location. To estimate the price penalty associated with
2Available at https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.
html
6

theinsurancecostsinthesestudylocations,wecalculatedthepresentvalueofastreamofinsurance
payments, again using three different discount rates of 3%, 5%, and 7%, and divided by the average
sale price. These studies do not always report important characteristics of the insurance prices,
such as whether houses tend to under-insure and if any of the properties benefit from subsidized
insurance prices. For those reasons among others, these estimates may diverge from our estimates
of the efficient flood zone discount.
2.3 Empirical approaches
We implemented three different empirical approaches to estimate the flood zone discount: panel
repeat sales, difference-in-difference, and cross-sectional.
Our first method, panel repeat sales, identifies the effect of floodplain status on property value by
comparing a single property to itself over time, as its flood zone status (FP ) can change as the
it
floodplain map is updated. We estimate the following regression:
log(p ) = δFP +γ +µ Age +η +(cid:15)
ict it i c it ct ict
where δ is the estimated effect of being in the floodplain on prices (p ). FP is a binary variable
ict it
equal to 1 if the property is in the floodplain at the time of sale, and 0 otherwise. The property
fixed effect, (γ ), accounts for the time-invariant confounds including property characteristics, such
i
as proximity to water. We also control for the age of the property at sale by county. η is a
ct
fixed effect for each county-year (c and t), which flexibly absorbs local market trends. Errors are
clustered by county in all specifications.
Thekeyassumptionsforthisapproacharetwo-fold. First,weassumethat,afteraccountingflexibly
for time trends or shocks at the county level, that any remaining time-varying unobservables are
not correlated with both rezoning into the floodplain and price. Second, we assume that the
value of time-invariant characteristics that are correlated with rezoning into the floodplain, such
as proximity to the coast, are not changing over time. In additional robustness tests, we include
census tract-by-year fixed effects and allow for properties at different proximity to water and in
different price tiers to experience different time trends (Figure S3).
To be included in the panel sample, a property must be outside of the floodplain in the old map,
it must have a known floodplain status in the new map, and it must be sold more than once while
its floodplain status is known. Sales that occur while the floodplain status is unknown are dropped
from the dataset. The treated properties are those that are zoned into the floodplain when the
map is updated. We filter for outliers by removing properties that exhibit more than 50% annual
growth or decline in sale price between observed transactions. Inclusion of these outliers does not
affect our results, yielding an estimating flood zone discount of -2.2% rather than -2.1%.
7

Similar to the panel approach, our difference-in-difference strategy uses a map update that zones
certain houses into the floodplain to measure the impact of floodplain status on property value.
However, it does not require that a single parcel is sold more than once during the observational
period. Instead, we compare two properties within the same county or census tract, where both
begin outside of the floodplain and one house is then zoned into the floodplain. We assume that
absent the floodplain map changing, prices would trend similarly between the two properties. Pre-
and post-treatment price trends are shown in Figure S4. Our estimating equation is the following:
log(p ) = β NewFP +β NewMap
icqst 1 i 2 it
+δNewFP ∗NewMap +λ Z
i it s it
+η +α +(cid:15)
ct sq icqst
δ is the effect of being zoned into the floodplain on prices. NewFP is a binary variable equal to 1
i
if the property is located in the new floodplain, regardless of whether the old or new flood map is in
effect at the time of sale. β , the coefficient on NewFP , represents the pre-map change difference
1 i
between property values in the two regions. NewMap is a binary variable equal to 1 if the sale
it
occurs after the map has been updated, and its coefficient β represents any change in property
2
values common to both regions that occurred after the map was updated. The estimation is at the
property level because different locations experienced map changes at different times. As with the
panel method, errors are clustered at the county level.
To account for differences in the composition of houses sold at different times, we flexibly account
for a number of property-specific characteristics in Z : age of property at the time of sale, land
it
area, living area, and number of baths (all binned), as well as geographic characteristics: census
tract, distance to coast, river, lake, primary road, and secondary road. All of the distance variables
are binned at 0-100 m, 100-500 m, 500 m-1 km, 1 km-2 km, 2 km-3 km, 3km-4km, 4 km-5 km, 5
km-10 km, and greater than 10 km. α is a fixed effect for the quarter of sale by state to account
sq
for seasonal market changes, and η is again a fixed effect for each county-year, which flexibly
ct
absorbs local market trends. We also implement this model with census tract-year fixed effects,
shown in Figure S5.
To be included in the sample for this method, a property must be outside of the floodplain in the
old map, its floodplain status must be known in the new map, and the switch from the old map to
the new map must be a direct change. The switch from old to new is not always a direct change
because some places have a map version we do not observe that was in effect between our old map
and our new map. We drop these observations from our sample. In addition, we remove outliers
by filtering the highest- and lowest-priced 1% of sales from each county.
As an additional measure to maximize the similarity between control houses and rezoned houses,
we test our results when limiting the control group to only houses in counties or census tracts with
8

rezoned houses. Our primary estimates use a time period of ten years on either side of the map
update. We test the sensitivity to shorter time windows as well. Results of these sensitivity tests
are shown in Figure S5.
To compare to earlier estimates in the literature, we implement a cross-sectional analysis that
decomposes the sales price into property characteristics, location characteristics, and floodplain
presence. This approach pools all sales for which the floodplain status is known. To estimate
the flood zone discount, this method relies on the (in our view unlikely) assumption that we have
controlled for every property characteristic that is correlated with floodplain status and price.
log(p ) = λ Z +δFP +η +α +(cid:15)
icqst s it it ct sq icqst
Z is a vector of property characteristics identical to the one described in the spatial difference-in-
it
difference section. δ is once again the effect of being in the floodplain on property prices. Errors
are clustered at the county level.
All sales when the floodplain status of the property is known are included in the cross-sectional
regressions. We remove outliers by filtering the highest- and lowest-priced 1% of sales from each
county.
2.4 Estimating heterogeneous effects
Business buyers We test whether business buyers respond to the floodplain designation dif-
ferently than individuals and couples by modifying our panel regression to include an interaction
term:
log(p ) = δ FP +δ (FP ∗B )+ρB +γ +µ Age +η +(cid:15)
ict 1 it 2 it it it i c it ct ict
B isequalto1ifthebuyerismarkedasabusinessbuyerandiszerootherwise. Buyersaredefined
it
by CoreLogic as either a business or a individual/couple. The determination is based on the name;
for instance, all buyers ending in “LLC” are tagged as businesses. As a result, family LLCs or
family trusts are typically designated as businesses. The business designation also captures other
organizations that are not businesses, such as non-profits and government agencies. However, all
of these buyers — whether a family with an LLC, a large corporation, or a non-profit — are likely
to be better-resourced than a typical individual or couple purchasing a home.
Real estate disclosure laws Real estate disclosure laws vary widely in what they address, how
theyareimplemented,therequiredtimingofdisclosure,andtheconsequencesforfailuretodisclose.
To simplify these many dimensions, we consider three common types of flood-related disclosures:
• Floodplain location. These disclosures ask if the property is located in the floodplain or ask
9

for the flood zone designation of the property.
• Flood damage. This disclosure type includes any disclosures about drainage, leakage, water
intrusion, standing water, and flooding problems, both past and present.
• Flood insurance. This disclosure type includes whether flood insurance is currently carried
on the property, if it is required to be carried, if claims have been made recently, and the cost
of insurance.
To then explore the relationship between the flood zone discount and real estate disclosure laws,
we run our panel regression with an interaction term D :
s
log(p ) = δ FP +δ (FP ∗D )+γ +µ Age +η +(cid:15)
icst 1 it 2 it s i c it ct icst
where D is a categorical variable with levels 0-3 representing the number of types of disclosures
s
coveredinthatstate. Weuseatime-invariantvalue(representingthecurrentrequirements)because
although state real estate disclosures vary over time, the changes over time are difficult to track.
Some states give a real estate association authority to create a mandatory disclosure form, but the
content of the form can change without any legislative action. We treat disclosures as mandatory
even if sellers can avoid them in certain instances, such as by paying a fee (Connecticut and New
York) or by filing a disclaimer form rather than a disclosure form (Maryland).
TheinventoryofstaterealestatedisclosurelawswascompiledbasedoninformationfromtheNatu-
ralResourcesDefenseCouncilandtheNationalAssociationofRealtors[NRDC, 2018,NAR, 2019]3.
2.5 Overvaluation
To estimate current overvaluation of houses in the floodplain, we compare our estimates of the
observed floodplain discount to the efficient flood zone discount under a 5% discount rate. We sum
the total assessed value of houses in the floodplain from across the United States. Assessed values
are available for over 98% of the floodplain houses in our data, and they date from either 2016
or 2017. For each state, we obtain “undiscounted” values by treating observed values as currently
discounted by the results in Figure 3. Then, we re-discount with the efficient value (-6.9%, based
on a 5% discount rate) and take the difference between the observed values and efficient values.
Our estimate serves as a lower bound as sale prices frequently exceed assessed values.
3Available at https://www.nrdc.org/flood-disclosure-map and https://www.nar.realtor/sites/default/
files/documents/2019_State_Flood_Disclosures_Table_final.pdf
10

3 Results
3.1 Pooled sample
Acrosstheuniverseofsingle-familyhomesalesintheUS,wefindinourpreferredpanelspecification
(n = 5.65M sales) that being zoned into the floodplain reduces property values by -2.1% (95% CI
of [-4.9%, 0.8%]) (Figure 2). The difference-in-difference estimate (n = 5.64M) is similar at -1.4%
[-3.0%, 0.2%], while the cross-sectional estimate (n = 17.6M), which is again unlikely to represent
an unbiased estimate of the flood zone discount, is positive at 1.7% [0.6%, 2.8%].
To provide context for these estimates, we compare our results to two different benchmarks. First,
we benchmark against estimates of the present value of a future stream of insurance costs as a
percentage of total property value, using past papers that report both an average insurance cost
and an average property price for the study area. These estimates are frequently used as the
relevant benchmark in the literature. At a 5% discount rate, these estimates average -9%, ranging
from -4% to -20% (Figure 2, blue lines).
However, the present value of insurance costs may not equal the full pricing of presence in the
floodplain. We aim to estimate the present value of expected flood damages to the property, and
insurance costs may not equal the expected flood damage if households are under-insured or if the
policy carries a large deductible. Accordingly, as our second benchmark, we use data on insurance
prices from the NFIP to estimate expected flood damage: we assume that houses are fully insured
with the minimum deductible, such that virtually all the costs from flooding would be covered by
theinsurancepolicy. Usingthisapproach, weestimatethatfullpricingofpresenceinthefloodplain
would affect property values by -5.1% to -10.7%, depending on the discount rate (Figure 2, black
diamonds). We use these numbers as our best estimate of the flood zone discount in an efficient
market — one that fully reflects publicly available information — but recognize that the precise
value of the efficient flood zone discount will vary by property.
To test the robustness of our results, we examine several aspects of the rezoning process. First,
there is potential for manipulation by local officials, such that only certain types of homes and
neighborhoods are zoned into the floodplain. While the maps are subject to political pressure,
the deliberation requires engineering and flood modeling studies to adjust FEMA’s initial maps
[Pralle, 2019, Davis, 2010]. As such, while local politicians can invest in new studies or data
collection efforts, adjustments must have some evidence base. We do not find a larger flood zone
discount when we include census tract-by-year time controls, which would account for finer-scale
timetrendsandthepossibilitythatonlycertainneighborhoodsareaffectedbymapupdates(Figure
S3).
Second, because the flood map updating process often takes multiple years, it is possible that
11

the market has already adjusted to that information by the time the maps become official (which
is the date observed in our data). We evaluate this possibility using the difference-in-difference
specification to test if the flood zone discount emerges earlier in time than the official flood map
update. Ifweassumethenewinformationisreleasedtwoyearspriortotheofficialdate, ourcentral
estimate shrinks from -1.4% to -0.7%. Given that a small fraction of homeowners learn about being
inafloodplainbeforetheymakeanofferonthehouse, thelackofananticipatoryreaction—which
would require extremely well-informed buyers — is not surprising [Chivers and Flores, 2002].
3.2 Access to information
While aggregate nationwide results show little evidence that information about flood risk is fully
priced in property markets, we find much stronger evidence that markets with better-informed
buyers discount floodplain properties relative to safer properties.
First, evidence for a flood zone discount is strongest in states with strict real estate disclosure laws
concerning flood risk (Figure 3). States have adopted widely varying policies on what information
a seller must disclose to a potential buyer and when. Some states require no disclosures at all,
while Louisiana, a state with an extremely comprehensive policy, requires a disclosure form that
includesiffloodinghaseverbeenexperienced, thefloodzoneclassification(andthesourceanddate
of the information), if there is flood insurance on the property, if the seller has a flood elevation
certificate, if the seller or previous owner received any form of federal flood assistance, and if there
are any requirements to maintain flood insurance on the property. We classify the states based on
three types of flood-related disclosures: (1) location in the floodplain, (2) flood damage, and (3)
flood insurance. We find the strongest evidence of a flood zone discount in states requiring all three
typesofdisclosures. Inthosestrictstates, theestimatedfloodzonediscountis-4.1%[-7.3%, -0.7%],
compared to our nationwide average of -2.1%. None of the other groupings offer strong evidence of
afloodzonediscount, butourcentralestimatesdobecomemorenegativewithadditionaldisclosure
laws when Florida (which has a very high share of properties in the floodplain) is omitted from the
“no disclosure” grouping.
Second, we observe that more sophisticated commercial buyers also discount flood zone properties
(Figure 4). “Business” buyers, as labeled in our data, range from large corporations that own and
rentoutsingle-familyhomestofamilyLLCs. Whenbusinessespurchasefloodzonehomes,theprice
penalty of -6.9% [-11.7%, -1.7%] aligns with our estimate of the efficient flood zone discount using
a 5% discount rate. On the other hand, when non-business buyers purchase flood zone homes, we
estimate a flood zone discount of -1.8% [-4.4%, 1.0%].
Our findings indicate that there are at least 3.8M floodplain homes in the US, assessed at nearly
$700B in total, that are discounted in practice by anywhere from -0.6% to -4.0% (Figure 3). To
12

estimate the total overvaluation of these homes, for each home we calculate the difference between
theefficientfloodzonediscount(whichwesetat-6.9%, ouraverageestimateata5%discountrate)
and the estimated discount in each home’s disclosure-based state groupings in Figure 3. Based on
assessed property values in 2016 and 2017, we estimate that these floodplain homes are overvalued
by a total of $34B. This estimate is very likely a lower bound because it relies on assessed values
that are often much lower than sale prices (and missing for about 1% of properties), and because
it does not include the small fraction of properties in communities that rely on paper maps.
4 Discussion
Our findings suggest that many of the 3.8 million floodplain homes in the US are over-valued
and that development in the floodplain likely exceeds what would be observed if asset prices fully
reflected information about flood risk. The additional risk created by these investments is likely
growing due to climate change and the long-lived nature of housing and infrastructure. Such con-
cerns extend to other climate hazards as well: both flood-prone and fire-prone locations have
experienced substantial development in recent years [Lazarus et al., 2018, Radeloff et al., 2018,
Climate Central and Zillow, 2018].
The inconsistent pricing of risk in property values may be due to specific features of the real estate
market that distinguish it from the theoretical market in which asset prices reflect all relevant
information. Realestatetransactioncostsarehigh,manyoftheinvestorsareamateurs(particularly
for residential property), and assets are rarely perfect substitutes for one another. In real estate
markets, even a fraction of uninformed or optimistic buyers can lead to inflated property valuations
because sellers can wait until they receive an offer from that group [Glaeser and Nathanson, 2015,
Pope, 2008]. Surveys have demonstrated the presence of both uninformed and optimistic buyers
when it comes to flood risk [Chivers and Flores, 2002, Bakkensen et al., 2017]. Accordingly, we
find that markets with better-informed and sophisticated buyers exhibit stronger evidence of an
efficientfloodzonediscount, whichisconsistentwithpricingofotherenvironmentalattributessuch
as exposure to sea level rise [Bernstein et al., 2019, Myers et al., 2019].
Our findings indicate that market efficiency may be improved by enhancing communication of
climate risk to buyers, for instance through stricter real estate disclosure laws or by directly com-
municating flood risk information to buyers early in their search process. Studies have found that
severe floods and storms that bring attention to these risks can trigger price adjustments, even in
areasthatwerenotdamagedbythefloodevent[Bin and Landry, 2013,Hallstrom and Smith, 2005,
Kousky, 2010]. The vast majority of states currently only require disclosures by the time the con-
tract is signed, which means that very few buyers would know about flood risk before they make
their offer. Only two states require that the seller disclose the cost of their insurance policy, which
would allow the buyer to evaluate the additional cost burden.
13

The panel and difference-in-difference approaches yield similar estimates of the flood zone discount
of -1 to -2%, while the cross-sectional estimate implies a flood zone bonus for property values.
The differences across methods demonstrates that cross-sectional estimates are likely affected by
unobserved characteristics that are correlated with both floodplain presence and property value,
preventingusfromisolatingthefloodzonediscount. Incontrast, becauseourpanelanalysisfocuses
on a single property over time, it allows us to account for all time-invariant characteristics of a
home, including its proximity to waterfront amenities. Our panel estimate relies on the assumption
thattherearenotime-varyingfactorswithinacountythatarecorrelatedwithbothpriceandbeing
rezoned into a floodplain, which appears reasonable in our context.
While our estimates of the effect of the floodplain maps are robust to many specifications, it is
theoreticallypossiblethatrealestatemarketsarerespondingtoadifferentmeasureoffloodriskthan
what these public maps provide. Given the widespread use of the government-produced floodplain
maps in regulation at local, state, and federal levels and the lack of widely available alternatives,
the use of other measures of flood risk seems unlikely. Further, even if certain market participants
rely on other sources of information, the influence of the maps themselves is still important to
investigate, given the substantial public investment they represent. Additional research is needed
to better understand the use of local knowledge and the extent to which it diverges from the
floodplain maps.
This analysis is limited by several data constraints. First, our benchmarks for efficient market
pricing are based on data available on NFIP insurance premia. It is possible that buyers are in-
suring at lower rates, which would explain a smaller flood zone discount. The NFIP dominates
the residential flood insurance market, and it has generally been found to be comparable or less
expensivethanprivatesectoralternatives[Kousky et al., 2016]. Whilecertainpropertiesdobenefit
from subsidized insurance rates under the NFIP, policies to eliminate those subsidies were imple-
mented in 2012 and in 2014, and the flood zone discount has remained steady during that time
period (Figure S6). Another data constraint stems from the accuracy of existing digital floodplain
maps and property location data. Property owners can appeal their flood zone designation through
a structure-specific elevation study and eliminate their requirement to purchase insurance; such
amendments are not recorded in the floodplain maps used in this study. In addition, the spatial
resolution of the floodplain maps and location information may lead to some properties near the
boundaries being mis-classified as inside or outside of the floodplain.
Our results demonstrate that markets do not respond uniformly to new information about flood
risk; rather, markets with better-informed buyers exhibit stronger responses. These findings point
to an opportunity for both researchers and policymakers to identify and implement practices to
ensure timely and effective communication of climate risk. These lessons are also relevant to
markets beyond real estate where information asymmetries are likely present, as recognized by
recent proposals to require corporations to disclose climate risk. Such measures are critical for
14

enabling investments in resilient assets and ultimately limiting damages in a changing climate.
References
[115th Congress, 2018] 115th Congress (2018). H.B. 1625 Consolidated Appropriations Act.
[Bakkensen et al., 2017] Bakkensen, L. A., Fox-Lent, C., Read, L. K., and Linkov, I. (2017). Vali-
dating Resilience and Vulnerability Indices in the Context of Natural Disasters. Risk Analysis,
37(5):982–1004.
[Beltr´an et al., 2018] Beltr´an,A.,Maddison,D.,andElliott,R.J.(2018). IsFloodRiskCapitalised
Into Property Values? Ecological Economics, 146(September 2017):668–685.
[Bernstein et al., 2019] Bernstein, A., Gustafson, M. T., and Lewis, R. (2019). Disaster on the
horizon: The price effect of sea level rise. Journal of Financial Economics, 134(2):253–272.
[Bin and Landry, 2013] Bin, O. and Landry, C. E. (2013). Changes in implicit flood risk premi-
ums: Empirical evidence from the housing market. Journal of Environmental Economics and
Management, 65(3):361–376.
[Bouwer, 2011] Bouwer, L. M. (2011). Have disaster losses increased due to anthropogenic climate
change? Bulletin of the American Meteorological Society, 92(6):791.
[Chivers and Flores, 2002] Chivers, J. and Flores, N. E. (2002). Market Failure in Information:
The National Flood Insurance Program. Land Economics, 78(4):515–521.
[Climate Central and Zillow, 2018] Climate Central and Zillow (2018). Ocean at the Door: New
Homes and the Rising Sea. Technical report.
[Congressional Budget Office, 2017] Congressional Budget Office (2017). The National Flood In-
surance Program: Financial Soundness and Affordability. Technical Report September.
[Davis, 2010] Davis, W. (2010). Lessons learned from the flood insurance re-mapping controversy
in Portland, Maine. Ocean and Coastal Law Journal, 16(1):181–209.
[Gibson et al., 2019] Gibson, M., Mullins, J. T., and Hill, A. (2019). Climate risk and beliefs :
Evidence from New York floodplains.
[Glaeser and Nathanson, 2015] Glaeser, E. L. and Nathanson, C. G. (2015). Housing Bubbles,
volume 5. Elsevier B.V., 1 edition.
[Hallstrom and Smith, 2005] Hallstrom, D. G. and Smith, V. K. (2005). Market responses to hur-
ricanes. Journal of Environmental Economics and Management, 50:541–561.
15

[IPCC, 2012] IPCC (2012). Summary for Policymakers. In Field, C. B., Barros, V., Stocker, T.,
Qin, D., Dokken, D., Ebi, K. L., Mastrandrea, M. D., Mach, K. J., Plattner, G.-K., Allen, S.,
Tignor, M., and Midgley, P., editors, Managing the Risks of Extreme Events and Disasters to
Advance Climate Change Adaptation, pages 1–19. Cambridge, UK and New York, NY, USA.
[Kousky, 2010] Kousky, C. (2010). Learning from Extreme Events: Risk Perceptions after the
Flood. Land Economics, 86(3):395–422.
[Kousky et al., 2016] Kousky, C., Lingle, B., and Shabman, L. (2016). NFIP Premiums for Single
- Family Residential Properties: Today and Tomorrow. Technical Report 16, Resources for the
Future.
[Lazarus et al., 2018] Lazarus, E. D., Limber, P. W., Goldstein, E. B., Dodd, R., and Armstrong,
S.B.(2018). Buildingbackbiggerinhurricanestrikezones. Nature Sustainability,1(12):759–762.
[Lincoln Institute of Land Policy, 2016] Lincoln Institute of Land Policy (2016). Land and Prop-
erty Values in the U.S.
[Myers et al., 2019] Myers, E., Puller, S. L., and West, J. D. (2019). Effects of mandatory energy
efficiency disclosure in housing markets.
[NAR, 2019] NAR (2019). National Association of Realtors, State Flood Hazard Disclosures Sur-
vey. Technical Report February.
[National Research Council, 2009] National Research Council (2009). Mapping the Zone: Improv-
ing Flood Map Accuracy. The National Academies Press, Washington, D.C.
[NCEI, 2019] NCEI (2019). NOAA National Centers for Environmental Information, U.S. Billion-
Dollar Weather and Climate Disasters.
[NRDC, 2018] NRDC (2018). How states stack up on flood disclosure.
[Pope, 2008] Pope, J. C. (2008). Do Seller Disclosures Affect Property Values? Buyer Information
and the Hedonic Model. Land Economics, 84(4):551–572.
[Pralle, 2019] Pralle, S. (2019). Drawing lines: FEMA and the politics of mapping flood zones.
Climatic Change, 152(2):227–237.
[Radeloff et al., 2018] Radeloff, V. C., Helmers, D. P., Kramer, H. A., Mockrin, M. H., Alexandre,
P. M., Bar-Massada, A., Butsic, V., Hawbaker, T. J., Martinuzzi, S., Syphard, A. D., and
Stewart, S. I. (2018). Rapid growth of the US wildland-urban interface raises wildfire risk.
Proceedings of the National Academy of Sciences, 115(13):3314–3319.
[Shao et al., 2017] Shao, W., Xian, S., Lin, N., Kunreuther, H., Jackson, N., andGoidel, K.(2017).
Understanding the effects of past flood events and perceived and estimated flood risks on indi-
viduals’ voluntary flood insurance purchase behavior. Water Research, 108:391–400.
16

[Shr and Zipp, 2019] Shr, Y.-H. J. and Zipp, K. Y. (2019). The Aftermath of Flood Zone Remap-
ping: TheAsymmetricImpactofFloodMapsonHousingPrices.LandEconomics,95(2):174–192.
[Swiss RE, 2019] Swiss RE (2019). Sigma Explorer.
[Troy and Romm, 2004] Troy, A. and Romm, J. (2004). Assessing the price effects of flood hazard
disclosure under the California natural hazard disclosure law (AB 1195). Journal of Environ-
mental Planning and Management, 47(1):137–162.
17

Figure 1: Geographic coverage of studies of the flood risk discount in the US. (A) Locations of
past studies. Existing studies have typically evaluated a single county or city at a time. Sources
included are listed in Table S1. (B) Geographic coverage of data used in this study, mapped on a
5 km by 5 km grid. The areas in white do not have a digitized floodplain map. Darker shades of
red indicate a higher proportion of single-family homes in the floodplain within the grid cell. Over
3.8M single-family homes are currently located in the floodplain.
18

Figure 2: Information about flood risk is not fully reflected in property values. The results of
each method are shown at left, with error bars marking 95% confidence intervals (n from left to
right: 5.65M, 5.64M, 17.6M). At right, the diamonds denote our estimates of the efficient flood
zone discount, approximated as the present value of insurance costs when the household is fully
insured as a percentage of the property’s total value. The rug plots show literature estimates of the
present value of reported insurance costs as a percentage of total property value. The diamonds
and rug plots are shown under different discount rates.
19

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Types of flood−related disclosures required 0 1 2 3
ecirp
no
sutats
nialpdoolf
fo
tceffE
0.08 B
0.06
0.04
0.02
0 l l
l
−0.02 l
−0.04 l
7%
−0.06
5%
−0.08
−0.1
3%
−0.12 all w/o FL
None 1 2 3
Types of flood−related disclosures required
Figure 3: The flood zone discount appears larger in states with very strict real estate disclosure
laws concerning flood risk. (A) The types of flood-related real estate disclosures required in each
state. Three types of disclosures are considered: floodplain location, flood damage, and flood
insurance. (B) Estimates of the flood zone discount based on the types of flood-related real estate
disclosures required (n = 5.65M). States are grouped based on coloring in (A). Error bars denote
95% confidence intervals.
20

0.02
0.00
−0.02 l
−0.04
7%
−0.06
l 5%
−0.08
−0.10
3%
−0.12
Non−business Business
ecirp
no
sutats
nialpdoolf
fo
tceffE
Figure 4: Businesses discount flood zone properties. The flood zone discount for business buyers is
estimatedat-6.9%,comparedto-1.8%fornon-businessbuyers(n=5.65M).Errorbarsdenote95%
confidence intervals. The diamonds, at right, mark estimates of the efficient flood zone discount
under different discount rates.
21

Appendix
Figure S1: Spatial variation in old and new floodplain maps. Dots represent parcels in our dataset
and are shaded based on their floodplain status under the old and new floodplain maps. The
floodplain in the old map is shaded blue, and the floodplain in the new map is shaded red. Purple
areas and black dots are in the floodplain under both maps. Parcels that remain outside of the
floodplaininbothtimeperiods(ourcontrolproperties)aregray. Parcelsrezonedintothefloodplain
(our treatment properties) are red.
22

Figure S2: Temporal variation in floodplain map updates. Color indicates the year of the newest
effective map in the county, based on maps produced at the county level (with DFIRMs ending in
”C”). Areas in white are home to sub-county level maps or do not have a digital floodplain map.
23

sutats
nialpdoolf
fo
tceffE
0.04
0.02
0 l
l
−0.02 l
l
−0.04
−0.06
−0.08
−0.1
Main Census Tract Price Water
Model
Figure S3: Panel regression results with alternative specifications. The main specification (n =
5.65M) on the left-hand side adjusts for the property, county-by-year, and age of the property
at the time of sale. The “Census Tract” specification (n = 1.70M) limits the sample to only
properties within census tracts with treated properties, and it replaces the county-by-year fixed
effects with census tract-by-year fixed effects. The “Price” specification (n = 5.65M) returns to the
main specification, but adds adjustments for price quintile-by-year, in case higher-value properties
trend differently than lower-value properties. Finally, the “Water” specification (n = 5.65M) adds
adjustments for distance to river-by-year, distance to coast-by-year, and distance to lake-by-year
to the main specification. These allow for houses at different distances to water to trend differently
over time.
24

280000
240000
200000
−20 −10 0 10 20
Quarters to Map Update
ecirP
0.050
0.025
0.000
−0.025
−0.050
−20 −10 0 10 20
Quarters to Map Update
New floodplain status In new FP Out of new FP
laudiseR
ecirP
New floodplain status In new FP Out of new FP
Figure S4: Pre-treatment prices of the control and treatment groups trend similarly. (A) shows
trends in price and (B) shows trends in price residual relative to the time of map update. The price
residualistheresidualofpriceregressedoncounty-by-yearfixedeffectsandpropertycharacteristics.
25

sutats
nialpdoolf
fo
tceffE
0.02
0
l
l l l l l
−0.02
−0.04
Main County Tract Tract−Yr 5 yr 3 yr
Model
Figure S5: Difference-in-difference regression results with alternative specifications. The main
specification on the left-hand side (n = 5.64M) adjusts for county-by-year time trends, the census
tract, and the following property characteristics (all at the state level): number of baths, living
area, land area, distance to river, distance to lake, distance to coast, distance to primary road,
distance to secondary road, property age, and quarter of sale. The “County” (n = 5.57M) and
“Tract”models(n=2.53M)usethesameregression,butremovepropertiesthatarenotinthesame
county or tract as a treated property (that is, a property that is rezoned into the floodplain), such
that the control properties are geographically proximate to the treated properties. The “Tract-Yr”
specification (n = 2.53M) uses the same sample as the “Tract” model, but uses tract-by-year fixed
effects rather than county-by-year. The “5-year” specification (n = 3.4M) uses only five years of
sales on either side of the map update, and the “3-year” specification (n = 2.23M) only uses three
years of sales on either side of the map update.
26

sutats
nialpdoolf
fo tceffE
0.10
0.05
l
l l
0.00 l
l
l l l l l l
l
l
l
−0.05
−0.10
2004 2006 2008 2010 2012 2014 2016
Figure S6: While policy changes in 2012 and 2014 phased out subsidies in NFIP pricing, estimates
of the flood zone discount changed little. These results are generated using the main specification
for the panel regression, interacting the floodplain variable with year (n = 5.65M). Because the
number of treated properties increases over time (as more map updates occur across the country),
only results for later years are shown.
27

Table S1: References included in Figure 1a. If references include information on average house and
insurance prices, then they are also included in the rug plot in Figure 2, as marked at right.
References In Fig. 2
Atreya, A. & Czajkowski, J. Graduated Flood Risks and Property Prices in Galve- N
ston County. Real Estate Econ. 1–38 (2016). doi:10.1111/1540-6229.12163
Atreya, A. & Ferreira, S. Seeing is Believing? Evidence from Property Prices in N
Inundated Areas. Risk Anal. 35, 828–849 (2015).
Atreya, A., Ferreira, S. & Kriesel, W. Forgetting the Flood? An Analysis of the Y
Flood Risk Discount over Time. Land Econ. 89, 577–596 (2013).
Bin, O. & Kruse, J. B. Real Estate Market Response to Coastal Flood Hazards. Y
Nat. Hazards Rev. 7, 137–144 (2006).
Bin,O.&Landry,C.E.Changesinimplicitfloodriskpremiums: Empiricalevidence N
from the housing market. J. Environ. Econ. Manage. 65, 361–376 (2013).
Bin, O.&Polasky, S.EffectsofFloodHazardsonPropertyValues: EvidenceBefore Y
and After Hurricane Floyd. Land Econ. 80, 490–500 (2004).
Bin, O., Crawford, T. W., Kruse, J. B. & Landry, C. E. Viewscapes and Flood N
Hazard: Coastal Housing Market Response to Amenities and Risk. Land Econ. 84,
434–448 (2008).
Bin, O., Landry, C. E. & Kruse, J. B. Flood Hazards, Insurance Rates, and Ameni- Y
ties: Evidence from the Coastal Housing Market. J. Risk Insur. 75, 63–82 (2008).
Carbone, J.C., Hallstrom, D.G.&Smith, V.K.CanNaturalExperimentsMeasure N
BehavioralResponsestoEnvironmentalRisks? Environ. Resour. Econ. 33,273–297
(2006).
Donnelly, W. A. Hedonic Price Analysis of the Effect of a Floodplain on Property Y
Values. J. Am. Water Resour. Assoc. 25, 581–586 (1989).
Fridgen, P. M. & Shultz, S. D. The Influence of the Threat of Flooding on Housing Y
Values in Fargo, North Dakota and Moorhead, Minnesota. (1999).
Gibson, M., Mullins, J. T. & Hill, A. Climate risk and beliefs: Evidence from New Y
York floodplains. (2019).
Hallstrom, D. G. & Smith, V. K. Market responses to hurricanes. J. Environ. Econ. Y
Manage. 50, 541–561 (2005).
Harrison, D. M., Smersh, G. T. & Schwartz, A. L. Environmental Determinants of Y
Housing Prices: The Impact of Flood Zone Status. J. Real Estate Res. 21, 3–20
(2001).
Kousky, C. Learning from Extreme Events: Risk Perceptions after the Flood. Land Y
Econ. 86, 395–422 (2010).
Macdonald, D. N., Murdoch, J. C. & White, H. L. Uncertain hazards, insurance, Y
and consumer choice: evidence from housing markets. Land Econ. 63, 361–371
(1987).
28

Macdonald,D.N.,White,H.L.&Taube,P.M.FloodHazardPricingandInsurance Y
Premium Differentials: Evidence from the Housing Market. J. Risk Insur. 57,
654–663 (1990).
Morgan, A. The impact of hurricane Ivan on expected flood losses, perceived flood Y
risk, and property values. J. Hous. Res. 16, 47–60 (2007).
Newsome, B. A. & Bialaszewski, D. Adjusting comparable sales for floodplain loca- N
tion: the case of Homewood, Alabama. Appraisal J. 58, 114–118 (1990).
Nyce,C.,Dumm,R.E.,Sirmans,G.S.&Smersh,G.Thecapitalizationofinsurance N
premiums in house prices. J. Risk Insur. 82, 891–919 (2015).
Pope, J. C. Do Seller Disclosures Affect Property Values? Buyer Information and Y
the Hedonic Model. Land Econ. 84, 551–572 (2008).
Posey, J. & Rogers, W. H. The impact of special flood hazard area designation on N
residential property values. Public Work. Manag. Policy 15, 81–90 (2010).
Shilling, J. D., Sirmans, C. F. & Benjamin, J. D. Flood insurance, wealth redistri- N
bution, and urban property values. J. Urban Econ. 26, 43–53 (1989).
Shr, Y.-H. (Jimmy) & Zipp, K. Y. The Aftermath of Flood Zone Remapping: The Y
Asymmetric Impact of Flood Maps on Housing Prices. Land Econ. 95, 174–192
(2019).
Speyrer, J. F. & Ragas, W. R. Housing prices and flood risk: An examination using Y
spline regression. J. Real Estate Financ. Econ. 4, 395–407 (1991).
Troy, A. & Romm, J. Assessing the price effects of flood hazard disclosure under the Y
California natural hazard disclosure law (AB 1195). J. Environ. Plan. Manag. 47,
137–162 (2004).
Turnbull, G. K., Zahirovic-Herbert, V. & Mothorpe, C. Flooding and liquidity on N
the bayou: The capitalization of flood risk into house Value and Ease-of-Sale. Real
Estate Econ. 41, 103–129 (2013).
US Army Corps of Engineers. Empirical Studies of the Effect of Flood Risk on N
Housing Prices. (1998).
29

Table S2: Summary statistics of sales included in each of the three empirical approaches. Sales are
grouped by location in current floodplain.
Non-floodplain Floodplain
Panel regression
Sales 5,592,881 58,639
Price 254,244 262,782
Effective Year Built 1988.30 1987.20
Share within 1km of river 0.12 0.20
Share within 1km of lake 0.65 0.55
Share within 1km of coast 0.03 0.12
Difference-in-difference regression
Sales 5,580,800 60,517
Price 247,808 229,115
Effective year built 1990.26 1989.45
Living area (sq ft) 1917.42 1811.71
Baths 2.44 2.25
Share within 1km of river 0.12 0.18
Share within 1km of lake 0.65 0.55
Share within 1km of coast 0.02 0.10
Cross-sectional regression
Sales 16,815,678 802,207
Price 247,309 268,798
Effective year built 1991.16 1989.85
Living area (sq ft) 1980.73 1856.17
Baths 2.51 2.29
Share within 1km of river 0.11 0.25
Share within 1km of lake 0.67 0.57
Share within 1km of coast 0.02 0.25
30
