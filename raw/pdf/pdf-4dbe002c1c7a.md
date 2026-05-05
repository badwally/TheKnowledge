---
id: pdf-4dbe002c1c7a
type: pdf
title: w29874
url: ''
authors: []
ingested_at: '2026-04-29T16:27:24Z'
content_hash: sha256:78bacc9c091d348694c39f829c5848c5d598ea83381749b917df3b848845c7fa
source_path: raw/pdf/pdf-4dbe002c1c7a.pdf
domains:
- trading-and-markets
nlm_corpus_ids:
- ccbda94f-7251-42bb-864f-0e1c9850f7ad
wiki_pages:
- wiki/entities/daron-acemoglu.md
- wiki/entities/alex-he.md
- wiki/entities/daniel-le-maire.md
- wiki/entities/nber.md
- wiki/concepts/business-manager-effect.md
- wiki/concepts/rent-sharing.md
- wiki/concepts/labor-share-decline.md
- wiki/concepts/manager-diffusion-iv.md
- wiki/concepts/role-model-college-major-iv.md
- wiki/concepts/business-education-socialization.md
meta:
  page_count: 92
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/w29874.pdf
published_at: '2022'
---
NBER WORKING PAPER SERIES
ECLIPSE OF RENT-SHARING:
THE EFFECTS OF MANAGERS' BUSINESS EDUCATION
ON WAGES AND THE LABOR SHARE IN THE US AND DENMARK
Daron Acemoglu
Alex He
Daniel le Maire
Working Paper 29874
http://www.nber.org/papers/w29874
NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
March 2022
We thank David Autor, Mike Faulkender, Simon Jaeger, Pat Kline, Max Maksimovic, Richard
Marens, Suresh Naidu, Harris Sondak, Anna Stansbury, Geoff Tate, David Thesmar, Liu Yang,
Luigi Zingales, and seminar participants at the University of Maryland and POLECONUK for
helpful discussions and comments. We are grateful to Jakob Munch for sharing the data on trade
shocks and to Marco Tabellini and Guglielmo Zappala for help with the BoardEx data. Any
views expressed are those of the authors and not those of the U.S. Census Bureau. The Census
Bureau's Disclosure Review Board and Disclosure Avoidance Officers have reviewed this
information product for unauthorized disclosure of confidential information and have approved
the disclosure avoidance practices applied to this release. This research was performed at a
Federal Statistical Research Data Center under FSRDC Project Number 1680 (CBDRB-FY22-
P1680-R9236). We thank the Smith Richardson Foundation and the Hewlett Foundation for
financial support. The views expressed herein are those of the authors and do not necessarily
reflect the views of the National Bureau of Economic Research.
NBER working papers are circulated for discussion and comment purposes. They have not been
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies
official NBER publications.
© 2022 by Daron Acemoglu, Alex He, and Daniel le Maire. All rights reserved. Short sections of
text, not to exceed two paragraphs, may be quoted without explicit permission provided that full
credit, including © notice, is given to the source.

Eclipse of Rent-Sharing: The Effects of Managers' Business Education on Wages and the
Labor Share in the US and Denmarkˆ
Daron Acemoglu, Alex He, and Daniel le Maire
NBER Working Paper No. 29874
March 2022
JEL No. G30,J30,J31,J53,M52
ABSTRACT
This paper provides evidence from the US and Denmark that managers with a business degree
(“business managers”) reduce their employees' wages. Within five years of the appointment of a
business manager, wages decline by 6% and the labor share by 5 percentage points in the US, and
by 3% and 3 percentage points in Denmark. Firms appointing business managers are not on
differential trends and do not enjoy higher output, investment, or employment growth thereafter.
Using manager retirements and deaths and an IV strategy based on the diffusion of the practice of
appointing business managers within industry, region and size quartile cells, we provide
additional evidence that these are causal effects. We establish that the proximate cause of these
(relative) wage effects are changes in rent-sharing practices following the appointment of
business managers. Exploiting exogenous export demand shocks, we show that non-business
managers share profits with their workers, whereas business managers do not. But consistent with
our first set of results, these business managers show no greater ability to increase sales or profits
in response to exporting opportunities. Finally, we use the influence of role models on college
major choice to instrument for the decision to enroll in a business degree in Denmark and show
that our estimates correspond to causal effects of practices and values acquired in business
education - rather than the differential selection into business education of individuals unlikely to
share rents with workers.
Daron Acemoglu Daniel le Maire
Department of Economics, E52-446 University of Copenhagen
Massachusetts Institute of Technology Department of Economics
77 Massachusetts Avenue Cambridge, Copenhagen, Denmark
MA 02139 1719V
and NBER Daniel.le.Maire@econ.ku.dk
daron@mit.edu
Alex He
4411 Van Munching Hall
Robert H. Smith School of Business
University of Maryland
College Park, MD 20742
axhe@umd.edu

1 Introduction
Thelaborshareofnationalincomehasfalleninseveralindustrializednationsoverthelastthreedecades
(Karabarbounis and Neiman, 2014). In the US, the labor share in the private nonagricultural business
sector used to hover around 65% between the 1950s and the 1980s but now stands at below 60%.
Concurrently, the annual growth rate of median (real) wages, which was typically above 2% between
the 1950s and the 1970s, has been only 0.3% since 1980, despite significant productivity growth. The
bargainingpoweroflaborhasnotrecededasmuchinNordiccountries, whichhaveatraditionofstrong
trade unions and various pro-labor institutions (Hall and Soskice, 2001; Freeman, 2007). Nevertheless,
the Danish corporate sector labor share has also fallen from 69% in 1999 to 65% in 2014 (H´emous and
Olsen, 2020). Many factors have been proposed as potential drivers of these pervasive changes in the
nature of labor markets, including capital accumulation (Blanchard, 1997; Piketty and Zucman, 2014),
automation (Acemoglu and Restrepo, 2019; Acemoglu et al., 2020), the rise of superstar firms (Autor
et al., 2020), growing concentration and market power (Guti´errez and Philippon, 2017; De Loecker et
al., 2020), and the declining power of unions (DiNardo et al., 1996; Farber et al., 2021).
In this paper, we argue that changing managerial attitudes and practices towards rent-sharing
have been a major contributing factor to the decline in the labor share and slowdown of wage growth.
We provide evidence from the US and Denmark suggesting that CEOs with business-school degrees
(business undergraduates or MBAs), who have been managing a growing share of firms over time,
have significantly reduced wage growth and the share of labor. Combining evidence from the US and
Denmark is useful for our agenda for two reasons. First, it highlights that the mechanism we focus on
is not just a US phenomenon and operates under diverse institutional conditions. Second, the Danish
data enable us to explore some of the mechanisms via which these effects are realized.
We present three main findings. The first is our headline result: in both the US and Denmark,
when a chief executive officer with a business degree (“business manager” for short) takes over from a
non-business manager, there is a significant decline in wages and the labor share of the firm (relative
to non-business-manager firms). With our event-study design, we find a 5 percentage point decline in
the labor share and a 6% decline in wages in the five years following the appointment of a business
manager in the US. The same approach in Denmark yields similar and only slightly smaller results:
a 3 percentage point decline in the labor share and a 3% decline in wages. In neither country do we
see any differential trends in the labor share, wages, employment, output, or investment before the
term of the business manager begins. Nor do we detect much of an employment, output, investment,
or productivity response, which suggests that business managers are not more productive than their
non-business peers.
1

Taken at face value, our estimates suggest that the effects of business managers are sizable but not
implausiblylarge. IntheUS,forexample,wherethefractionofworkersemployedbybusinessmanagers
has increased from 26% to 43% between 1980 and 2020, our estimates indicate that business managers
can explain about 20% of the decline in the labor share. They also account for approximately 15% of
the slowdown of wage growth since 1980. In Denmark, where the increase in the fraction of workers
employed by business managers is smaller (rising from 11% in 1995 to 19% in 2011), our mechanism
accounts for 6% of the decline in the labor share. The reduction in wages following the accession of a
business manager leads to an increase in profits: the return on assets (ROA) increases by 3 percentage
points in the US and by 1.5 percentage points in Denmark. In the US, we also find an increase of
about 5% in the stock market values of companies that appoint business managers. We further show
that all else equal, managers with business degrees earn more than non-business managers.1
In addition to the lack of pre-trends in various firm outcomes, we augment our event-study and
difference-in-differences estimates by showing that a switch from one non-business manager to another
non-business manager has zero impact on all of the outcomes we focus on. We also find no impact
on these outcomes due to a switch from a non-college manager to one with a college degree. Hence,
our estimates are not capturing mechanical “Hawthorne” effects associated with the arrival of a new
manager or the reign of a more educated leader.
These checks notwithstanding, an obvious concern with our estimates is the endogeneity of the
decision to appoint a business manager—perhaps firms turn to business managers when they need to
cut labor costs. To bolster the argument that our results capture causal effects of business managers
on wages and the labor share, we use two strategies. First, we obtain very similar estimates when we
focusonmanagerretirementsanddeaths, whicharearguablylessendogenousthanotherswitchesfrom
non-business to business managers. Second, we develop an instrumental variable (IV) strategy. We
document a clear pattern of “diffusion” of the appointment of business managers within peer groups of
firms in both the US and Denmark. We define peer groups as region-industry-size class cells and show
that after a first business manager is appointed within a cell, its peers become significantly more likely
to appoint business managers as well.2 We control for differential trends by industry, region, and size
class to ensure that this strategy exploits within-group variation. We also confirm that the IV effects
are robust to controlling for correlation in output and wages across peers. Although this IV strategy
is not a panacea against all endogeneity concerns and may be confounded with cross-cell trends, it
is conceptually attractive in part because it exploits a completely different source of variation than
1There are a few other differences between managers with and without a business degree. For example, in Denmark
thosewithabusinessdegreeusemoredebtfinancingandarealittlemorelikelytoadoptrobots. Weconfirmthatthese
are not major channels for our effects.
2ThisissimilartothestrategyusedinAcemogluetal.(2019)toisolatepotentiallyexogenousvariationincountry-level
democracy based on the idea that there are regional democratization waves.
2

our non-IV estimates. Using this approach, we estimate similar—about 50% larger than our baseline
results—effects of business managers in both Denmark and the US.3
We additionally show that the negative wage effects apply throughout the wage and skill
distribution. In Denmark, we show this using both education and wage percentiles of workers, whereas
in the US, where we do not have accurate information on worker education, we establish this pattern
using variation by worker wage percentile. In both the US and Denmark, the effects are larger for
low-skilled workers than for high-skilled ones.
The (relative) wage cuts following the start of the term of a business manager are not without costs
to the company. In both the US and Denmark, we find that worker quits increase, especially for more
skilled workers (though these estimates are less precise than our main results). This finding suggests
that, although business managers are not reducing overall employment, some of the more valuable
employees leave after their reign starts.
Our second major result identifies changes in rent-sharing as the major mechanism for our results.
To identify how rent-sharing differs in companies run by business managers, we focus on plausibly
exogenous variation in firm profits driven by firm-specific export demand shocks in Denmark. In
particular, we adopt a strategy first proposed by Hummels et al. (2014) and isolate changes in a
firm’s export demand driven by differential changes in the imports of six-digit products by their main
exporting destinations. Put differently, this strategy focuses on firms that export to different foreign
markets and exploits the differential evolution of overall (non-Danish) imports in these markets. Using
this strategy, we explore how business-manager and non-business-manager firms respond to export
shocks. We find no major differences in terms of productivity, sales, employment, or investment
responses to export demand shocks—thus no compelling evidence that business managers are more
productive or adaptable in this context either. Consistent with our previous results, non-business
managers share the resulting rents with their workers. Our rent-sharing elasticity estimates suggest
that a 10% increase in value added per worker is associated with a 1.9% increase in wages. Alternately,
a 10% increase in profit per worker is associated with a 1% increase in wages.
In contrast, business managers do not share these export-driven rents with their employees, and
for the firms they run, we find a precise zero impact on wages following such an increase in exports.
This differential rent-sharing response explains the entirety of our event-study estimates. Further
explorationsrevealthatthiseffectitselfisalmostcompletelydrivenbypositiveexportshocks: following
an exogenous decline in exports, business and non-business managers behave similarly, presumably
3Our interpretation for this difference in magnitude is that practices associated with business managers diffuse more
broadly within our cells, so that firms without business managers might also become more likely to adopt the same
managerial practices and those with already-existing business managers might use them more intensively. Consequently,
our IV strategy may be estimating more systemic effects of practices associated with business education. This reasoning
also suggests that the quantitative effects reported above should be considered as lower bounds.
3

because cutting wages is challenging even for business managers who prioritize cost reductions.
However, following a positive export shock, non-business managers share the resulting rents and raise
wages, whereas business managers do not.4
Third, in the Danish data we explore whether business manager effects are due to the selection of
individuals who are more prone to take a hard line against labor into business degrees, or whether
instruction and socialization in business degree programs produce managers who do not share rents
with their employees. To answer this question, we exploit the presence of “role model” effects in the
choice of college majors—whereby individuals are more likely to follow the choices of their role models
(e.g., see Lockwood and Kunda, 1997; Lockwood, 2006 for general discussion, and Arcidiacono and
Nicholson, 2005; Rask and Bailey, 2002; Poldin et al., 2015; Wiswall and Zafar, 2015). We collect the
high school records of Danish managers and define the role models for each individual as students in
the same high school and with similar academic performance, but one year ahead. We confirm that
role models matter for college choice, with a 10% increase in the fraction of role models pursuing a
business degree associated with a 1%–3% increase in a student’s likelihood of enrolling in a business
program. Exploitingthis sourceof variation, weestimate thatmostof thewage and labor shareresults
we present can be explained as the treatment effect of business education rather than a selection effect.
Stepping back, we interpret these findings as capturing the impact of management practices and
values imparted by business schools and business degrees. Although we do not have direct evidence
on these channels, two ideas commonly propagated in business schools may significantly affect the
priorities and approaches adopted by managers with business degrees. The first is the emphasis on
shareholdervalues,asadvocatedin1970byMiltonFriedman,whostatedthat“Thesocialresponsibility
of business is to increase profits.”Following Friedman, other economists and business school scholars
started arguing that managers were not sufficiently devoted to maximizing shareholder value (e.g.,
Jensen and Meckling, 1976; Jensen and Murphy, 1990). These ideas became popular and started
being taught in business schools (Bennis and O’Toole, 2005; Ghoshal, 2005; Marens, 2014), and classic
textbooks in corporate finance, such as Brealey and Myers (1980) and Copeland and Weston (1979),
espoused that the goal of managers should be to maximize shareholder value. Under their influence,
(some) managers started viewing workers not as stakeholders in the corporation but rather as sources
of costs to be reduced (Freeman and Reed, 1983; Rappaport, 1999; Freeman, 2010). The second idea
is the emergence of a business school doctrine advocating reengineering and creating lean corporations
(Hammer and Champy, 1993; Davenport, 1993; Womack and Jones, 2003). Although the emphasis
4We also adapt the strategy of Hummels et al. (2014) to intermediate input imports, exploiting exports of six-digit
productsofcountriesfromwhichafirmsourcesitsintermediates. Forourpurposes,suchintermediateimportshocksare
less attractive than export demand shocks, because they may not be Hicks-neutral and may affect (some types of) labor
directly. Nevertheless,usingthissourceofvariation,wefindanalogousresults—positiveintermediateimportshockslead
to significant rent-sharing for non-business managers and zero rent-sharing for business managers.
4

was not on wage cuts per se, identifying and removing “unnecessary” costs started being viewed as an
integral part of successful management (Marens, 2011; Holt, 2020; Hassard and Morris, 2021). The
dual emphasis on shareholder value and corporate leanness may have made managers unwilling to
share rents with their workers.
To the extent that business schools were the vanguard of these ideas that became more widely
held among managers and were further propagated by management consultants, our estimates should
be viewed as lower bounds on the effects of these management practices. If so, in both the US and
Denmark management practices prioritizing shareholder value and cost cutting may have contributed
significantly even more to the decline in the labor share and the slowdown in wages than our range of
estimates (see also footnote 3).
Our paper is related to several distinct literatures. First, we directly contribute to the literature on
the decline of the labor share (and thus the slower growth of wages than productivity) in industrialized
nations. (The first paragraph of this paper cites several of the leading publications in this stream
of literature.) Second, this paper is connected to the literature on business ethics concerning what
business schools teach and how it has changed over time, and several of the relevant papers in this
literature were just cited as well.
In economics, our paper is most closely linked to the literature on rent-sharing in corporations.
Several papers present evidence of rent-sharing, documenting, for example, that workers in industries
with greater profits, rents, or capital investments receive higher wages (e.g., Blanchflower et al., 1996;
Van Reenen, 1996; Hildreth and Oswald, 1997). The recent paper by Kline et al. (2019), for instance,
exploits exogenous changes in profitability resulting from patent grants and shows significant wage
gains for workers, though emphasizing that these gains are quite unequally distributed. Caldwell and
Harmon (2019) provide evidence from Denmark on the importance of workers’ outside options in rent
sharing. More broadly, several recent papers emphasize the (growing) importance of firm effects in
wages and wage inequality (e.g., Card et al., 2013, 2016; Song et al., 2019; Garin and Silv´erio, 2019).
Tothebestofourknowledge, thisliteraturehasnotinvestigatedtheroleofmanagers, andparticularly
their education and values, in rent-sharing.
Another important literature on which we build is that of management styles. The idea that
managers and their approaches matter for corporations is commonplace in the management literature
(e.g., Hambrick and Mason, 1984) and has been emphasized in theoretical discussions (e.g., Jensen and
Meckling, 1979; Hermalin and Weisbach, 1998). Systematic evidence on this was provided by Bertrand
and Schoar’s (2003) pioneering study, and several papers before and since then have documented the
role of managerial characteristics in various corporate decisions (e.g., Chevalier and Ellison, 1999;
Malmendier and Tate, 2005, 2008; Kaplan et al., 2012; Graham et al., 2013; Cust´odio and Metzger,
5

2014). Several papers have looked at CEOs’ MBA education and find mixed evidence on the effect
of business managers on firm performance (Bhagat et al., 2010; Miller and Xu, 2016, 2019). With
the notable exception of He and le Maire (2020), who document significant manager effects in Danish
wages, this literature does not focus on worker outcomes and, to the best of our knowledge, has not
investigated either the role of business school education or general managerial approaches in corporate
wagepolicies. Norareweawareofstudiesinthisliteraturethatattempttoisolateexogenousvariation,
which is a key aspect of our empirical strategy. Similar to Bertrand and Schoar (2003), we find that
business managers lead to better accounting performance, and our analysis suggests that this positive
effect is largely driven by lower labor costs.
Last but not least, we build on and contribute to the literature on the effects of economics and
business educations on ethical behavior (e.g., Frank et al., 1993, 1996; Frey and Meier, 2003; Bauman
and Rose, 2011). Unlike much of this literature, which focuses on lab experiments and surveys, we
investigate the implications of the appointment of a manager with a business degree on some of the
mostimportantcorporateoutcomes—andfindnoeffectsonoutputorproductivity,butamajorimpact
on rent-sharing. Interestingly, in this context, Wang and Murnighan (2011) and Wang et al. (2011)
arguethatbusinessschoolcurriculahaveadversesocialconsequencesbecausetheyemphasizeeconomic
incentives. In contrast to this argument, we do not find similar effects from Danish managers with
only economics degrees.
The rest of the paper is organized as follows. Section 2 describes our data. Section 3 outlines our
empirical strategy. In Section 4, we analyze the causal effects of business managers on wages and the
labor share using event studies and IV strategies. Section 5 exploits exogenous variation due to export
demand shocks in Denmark to explore the role of rent-sharing in our wage and labor share results.
Section 6 uses another IV strategy to address the question of selection into business education. Section
7 concludes. The online Appendix contains additional results.
2 Data and Context
In this section, we present the various data sets we use and provide details on sample construction.
We also discuss the relevant institutional context in Denmark and the US.
2.1 US Managers with Business Degrees
We obtain biographical information for CEOs of publicly traded US companies from the BoardEx
database of Management Diagnostics Ltd. For each CEO, we observe the name of the school and
the degree earned for all post-secondary schools attended. We classify MBAs and any degrees from
6

a business school as business degrees.5 We then match the CEOs in BoardEx to Compustat firms
between 1980 and 2020. Our final sample contains around 9,900 US publicly listed firms with complete
information on CEOs, and throughout we have a single CEO/manager per firm in each year.6
Figure 1 plots the share of Compustat firms with business-degree CEOs from 1980. In 1980, only
26% of the Compustat firms had CEOs with business degrees, but by 2020, this figure had grown to
43%. Almost all of the increase comes from the share of CEOs with MBAs, which rose from 24%
in 1980 to 37% in 2020. Harvard Business School contributed 19% of the business degrees of CEOs,
followed by Wharton (8%) and Stanford (5%).
Among the US public firms, CEOs are appointed by the board of directors and are responsible
for making major corporate decisions. While boards are expected to oversee and monitor managers
on behalf of shareholders, CEOs have a substantial degree of freedom in operations, and their vision
and styles are important determinants of firm policies (Bertrand and Schoar, 2003). Past research
has shown that CEOs are not homogeneous and differ in terms of overconfidence (Malmendier and
Tate, 2005, 2008), risk aversion (Malmendier et al., 2011; Benmelech and Frydman, 2015; Schoar and
Zuo, 2017), time preference (Graham et al., 2015), resoluteness (Kaplan et al., 2012), and gender bias
(Duchin et al., 2021).
2.2 US Data on Firm and Worker Outcomes
We use firm- and worker-level data from the US Census Bureau to estimate the impact of business
managers (CEOs with business degrees) on firm outcomes and worker wages. We match Compustat
firms to the Longitudinal Business Database (LBD), which covers all non-farm establishments with
paid employees in the US from 1987 to 2018. It provides information on plant-level owner (firm),
geographic location (state and county), industry (six-digit NAICS), employment, and payroll. We
aggregate this information to the firm level. Our sample excludes firms that change their IDs, such as
those involved in mergers and acquisitions or buyouts.
Wemergethefirm-leveldatawithindividualworker-levelinformation,includingemployment,wage,
gender,race,andage,fromtheLongitudinalEmployerHouseholdDynamics(LEHD)data. TheLEHD
data are constructed using administrative records from the state unemployment insurance (UI) system
and the associated ES-202 program. Wages include bonuses, stock options, profit distributions, the
cash value of meals and lodging, tips and other gratuities in most states, and, in some states, employer
contributions to certain deferred compensation plans such as 401(k) plans. We have access to LEHD
5Business schools are schools with “Business School”, “School of Business”, “College of Business”, or “School of
Management” in the school name (with a few exceptions such as Wharton and INSEAD). Business degrees include
bachelors, masters and executive programs of business schools.
6The coverage of BoardEx expanded over time, and after 2000, the majority of publicly listed firms can be found in
BoardEx. As a result, our sample includes 2,500 firms in 1995, 5,300 firms in 2005, and 5,200 firms in 2015.
7

worker-level data from 22 states and the District of Columbia, which covers about half of the US
population.7 The LEHD wage data are currently available from 1992 through 2014. We also merge
the LBD firm-level data with the Business Register (SSEL) data on annual firm sales.
2.3 Danish Matched Employer-Employee Data
For Danish firms and workers, we use data from several administrative registers at Statistics Denmark.
Our firm data come from the Firm Statistics Register (FirmStat), which covers the universe of private-
sector Danish firms from 1995 to 2011. FirmStat assigns each firm a unique identifier and provides
annual data on many of the firm’s activities, such as the number of full-time employees, value added,
and industry affiliation. We also use other firm registers to obtain financial data from balance sheets
and income statements.8 For all of our analyses, we exclude firms with 5 or fewer employees. As in
the US, our data exclude firms involved in mergers and acquisitions.
The worker data are extracted from the Integrated Database for Labor Market Research (IDA),
which covers the entire Danish population between the ages of 15 and 74, including the unemployed
and those who do not participate in the labor force. Each person has a unique identifier, and the
IDA database provides annual data on many of the individual’s socioeconomic characteristics, such as
annual income, education, and occupation. We measure the hourly wage rate as annual labor income
plus mandatory pension fund payments divided by annual hours. Each employed worker is matched
to an establishment, which is a unique physical work location such as an office, store, or factory, and
each establishment has a unique identifier. To match firms to workers, we draw on the Firm-Integrated
Database for Labor Market Research, or FIDA, which links every firm in FirmStat to its workers in
IDA who are employed by that firm in the last week of November.
Denmarkhasahighunionmembershiprate(70%–75%), andmorethan80%ofworkersarecovered
byacollectiveagreement. Whilewagebargaininghasbeenhistoricallycentralized, itwasdecentralized
duringtheperiodwestudy. Inthebeginningofoursamplein1995,lessthan10%ofworkersarecovered
by the standard rate system (where wages are set by the industry collective agreement). The wages
of the rest of the workers are mostly negotiated at the firm or individual level, with a wage floor set
by the industry collective agreement, which is binding only for the least experienced workers (Dahl et
al., 2013). In many cases, the bargaining at the firm or establishment level occurs between managers
and shop stewards, and agreements cover wage increases but not employment levels (Ilsøe, 2012). In
7The 22 states are: Arizona, Arkansas, California, Colorado, Delaware, Illinois, Indiana, Iowa, Kansas, Maryland,
Missouri, Montana, Nebraska, Nevada, New Jersey, New Mexico, North Dakota, Ohio, Oklahoma, Pennsylvania,
Tennessee, and Virginia.
8The survey from which we draw the accounting data (e.g., profits, investments) has a rolling panel structure where
firmsareselectedbasedontheiremploymentasofNovemberinthepreviousyear. Firmswith50ormoreemployeesare
always sampled. Information on sales and employment is available for all firms.
8

general, managers play an important role in wage bargaining and shaping firms’ wage policy (He and
le Maire, 2020).
To identify CEOs/top managers, we use a combination of occupation codes (ISCO) and job
hierarchy(PSTILL).Afirm’smanagerisdefinedasanemployeewithoccupationcode1210(“Directors
and Chief Executives”) and the highest job hierarchy category.9 We are also able to link managers
over time. Using this link, if a person is the manager at firm A in year t and year t+2, and there is
no manager at firm A at year t+1, we assume the same person is the manager in year t+1. Over
85% of worker-year observations in our sample period have at least one manager in the firm. For firms
with multiple employees that meet these criteria in a given year, we define the manager as the one
with the highest wage income. As in the US data, we have one manager per firm-year in the Danish
data. We also obtain data on managers’ education histories. A manager has a business degree if he
or she has business major at any level of education, including short education, professional BA, BA,
MA, and PhD.10
Figure 2 plots the fraction of managers in Denmark with business degrees over time. Panel (a)
shows that the share of firms with business-degree managers has increased by two thirds from 1995 to
2011. Panel (b) shows that, similar to the US, this increase is mostly driven by an increase in business
MA degrees. The top three Danish business schools—Copenhagen Business School, Aarhus University
SchoolofBusinessandSocialSciences, andUniversityofSouthernDenmarkBusinessSchool—account
for over 50% of all business degrees and over 70% of managers with business degrees.
3 Empirical Strategy
We are interested in the causal effects on firm and worker outcomes after a firm appoints a manager
(CEO) with a business degree (“business manager” for short). We also explore the mechanisms via
which managers influence wages and the labor share (and other outcomes). Additionally, we are
interested in identifying whether the effects of managers with business degrees are driven by the fact
thatindividualswithcertaincharacteristicsandapproachestomanagementselectintobusinessschools,
or whether these effects are related to the values and ideas students learn in business schools.
9If a firm has no worker with both the occupation code 1210 and the highest job hierarchy category, managers are
defined as the workers with occupation code 1210. If there is no worker with the occupation code 1210, managers are
defined as those with other managerial occupation codes (1221-1339) and the highest job hierarchy code. Finally, if a
firmhasnoworkerwithmanagerialoccupationcodes,managersaredefinedasthosewiththehighestjobhierarchycode.
In practice, over 80% of our managers are identified from observations that have both managerial occupation codes and
the highest job hierarchy category.
10About 75% of managers with business MAs also have a business BA or a business professional BA. In Denmark,
professional BA programs consist of both theoretical and practical teaching. The practical teaching takes place as an
internship at a workplace.
9

The key relationship we are interested in estimating can be summarized as:
y = γB +X(cid:48) β +λ +δ +ε , (1)
it it it t i t it
where B is an indicator variable for whether the manager at firm i in year t has a business degree.
it
In addition, X denotes a vector of covariates, λ summarizes the firm fixed effects, δ corresponds to
it i t
time effects, and ε is an error term. The coefficient of interest is γ, which is the effect of business
it
managers on firm and worker outcomes. In our event studies, we allow the effects to vary by event
time, and in some of the specifications we allow these effects to vary by worker skill or wage percentile.
Weuseanumberofdifferentstrategiestoestimateequation(1). Ourfirstandmostcentralstrategy
is a series of event studies, focusing on firms that transition from being run by non-business managers
to being run by business managers. These event studies enable us to confirm that firms switching to
business managers are not on differential trends before the events and provide a transparent way of
estimating and displaying our results.
Throughout, we follow Borusyak et al. (2021) and use an “imputation” estimator to compute the
event-study estimates. This estimator ensures consistency in the presence of two-way fixed effects and
avoids issues of spurious identification and negative weights on some observations (de Chaisemartin
and D’Haultfœuille, 2020). In practice, this estimator is constructed in three steps. First, the unit
fixed effects, time fixed effects, and the coefficients of other control variables are estimated from
regressionsusinguntreatedobservationsonly. Second,thetreatmenteffectforeachtreatedobservation
iscomputedfromthefirst-stepregressionasthedifferencebetweentheactualoutcomeandthepotential
untreatedoutcome. Finally, usingthesecond-stepestimatedeffects, wecomputetheaveragetreatment
effect on the treated.
Our main events are transitions from non-business managers to business managers. We restrict
treated firms to those that have never hired a business manager before the event and have only one
event during the sample period. The control group consists of firms that have non-business managers
throughout our sample period. The identifying assumption is that, absent the event, wages and other
outcomes would have followed parallel trends in treated and control firms. In all specifications, we
control for industry × year fixed effects, firm size quintile × year fixed effects, and region(state) × year
fixed effects.
In Danish worker-level regressions, the control group comprises workers employed by the
aforementioned control group of firms, and we additionally include time-varying worker characteristics
(experience, experience squared, marital status, union membership) and worker × firm fixed effects to
track the same worker over time and filter out changes in worker composition. Standard errors are
clustered at the firm level.
10

In the US worker-level regressions, because the total number of workers is very large (over 100
million), we adopt a matching procedure for implementing worker-level regressions. Following Smith
et al. (2019), we match each treated firm that switches from a non-business manager to a business
manager to control firms that are in the same industry, state, employment decile, and wage decile
and have never had a business manager before the event. The effect of business manager on wages
is estimated from the differential evolution of wages of staying workers between treated firms and
matched control firms.
Although we verify that there are no pre-trends among firms appointing business managers, there
are two additional endogeneity concerns. First, there may be other organizational, economic, or
financial changes implemented at the same time as new business managers are appointed, confounding
the impact of business managers with the effects of these other changes. Second, there may be time-
varying omitted factors changing at the same time as the managers (and potentially causing the
replacement of the existing manager). We deal with the first problem by verifying that there are no
other major changes at the time of managerial transitions (we discuss a few minor changes and why
they are unlikely to account for our results in the next section).
To confront the second problem, we adopt two complementary strategies. We confirm that the
results are similar when we focus on the subsample in which previous non-business managers die or
“retire” (where we define retirement as separations by CEOs over the age of 62).
We additionally develop an instrumental variable (IV) strategy based on the idea that hiring a
manager with a business degree becomes popular among certain types of firms at different times. This
is similar to the strategy of Acemoglu et al. (2019), who exploited regional democratization waves as
an instrument for a country switching from nondemocracy to democracy. In our context, we create
region × industry × initial size quartile cells, and document that after the appointment of the first
business manager within a cell, the likelihood of other firms in the cell also appointing a business
manager increases significantly. We then use this relationship as the first stage of a two-stage least
squares (2SLS) strategy. The first-stage equation is:
3
(cid:88)
B = θ Z +X(cid:48) βF +λF +δF +(cid:15) , (2)
it k i,t−k it i t it
k=1
where Z = 1 (cid:80) B is the instrument, defined as the jackknifed average of
it |Ii| j∈{Ii:j(cid:54)=i,Cj=Ci,Bjt0 =0} jt
business managers among firms in the same region × industry × size peer group that did not have a
business manager at the beginning of the sample.11 In the first stage, we include lags of the instrument
up to three years, because the influence of peer firms may be felt with a lag. In practice, we find that
11In the IV analysis, we exclude firms that already had business managers at the start of our sample so that we only
estimate the impact of hiring a business manager, which our event-study estimates suggest is different from the effect of
firing a business manager.
11

lags beyond three years do not predict business manager hiring significantly. In all specifications, we
control for year and firm fixed effects. We also include region, size quintile, and industry fixed effects
interacted with year fixed effects, ensuring that we exploit only within-cell variation in the diffusion of
business managers.
Our second-stage equation is the same as (1). The exclusion restriction in this case is that,
conditionalonourcovariates, thetimingofthefirstswitchtoabusinessmanagerinacellisorthogonal
to future outcomes of other firms in that cell. We provide a number of placebo exercises to bolster
confidence in this exclusion restriction.
Toexploretheroleofchangesinrentsharinginmediatingtheeffectsofbusinessmanagersonlabor
outcomes, we focus on the sample of exporting firms in Denmark. In this sample, we follow Hummels
et al. (2014) and develop a source of exogenous variation in firm sales and profits driven by changes in
firm-specific demand for exports. Specifically, we use differences in exporting destination by six-digit
product for each firm and exploit the fact that the demand for exports from Danish firms is changing
differentially across these destinations (proxied by their total non-Danish imports of the focal six-digit
product). The reasoning for this source of variation is that the relationship between an exporter and
its customers is specific and is typically built over time. As a result, a change in demand for a product
in, say, Germany will disproportionately impact Danish firms exporting that product to the German
market, and we proxy for German demand by using variation in the overall German imports for the
product in question (except from Denmark).
More concretely, the predicted firm-specific exports are defined as
(cid:88)
WID = se WID , (3)
jt jck ckt
c,k
where se is the pre-sample share of exports to country c and six-digit product k of firm j, and
jct
WID is country c’s total purchases of product k from other countries at time t. Imports from
ckt
Denmark are left out in order to avoid any mechanical correlation between WID and the exports of
ckt
thefirminquestion. Insomespecifications,weadditionallycontrolforproduct-levelvariationinoverall
exports (namely, (cid:80) se WID , where se is firm j total exports of six-digit product k) to focus solely
k jk kt jk
on the comparison of firms exporting similar products to different destinations. Because our main
regressions are in levels with worker fixed effects, as in (1), we explore the effects of export-driven
rents by including the level of predicted firm-specific exports, WID , on the right-hand side of our
jt
wage regressions with worker × firm fixed effects. This is analogous to including the change in WID
jt
on the right-hand side of regressions for change in (log) wages. With a slight abuse of terminology,
we will refer to WID as “export shock”. To explore the asymmetric rent-sharing implications of
jt
positive and negative export shocks, we also create two additional variables: WID+ = WID+ +
jt jt−1
12

max{WID −WID ,0}andWID− = WID− +min{WID −WID ,0}(bothinitializedat
jt jt−1 jt jt−1 jt jt−1
0 at the beginning of the sample). We then estimate their separate effects (in levels, this is analogous
to including ∆WID+ = max{WID −WID ,0} and ∆WID− = min{WID −WID ,0}
jt jt jt−1 jt jt jt−1
in regressions for wage changes). In the Appendix we also use the same strategies and similarly
constructed variables to exploit exogenous variation in intermediate imports.
Finally, to study whether the effects of business managers are due to selection of who studies
business or driven by the causal impact of business programs, we develop another IV strategy. We
leverage the idea that choices of college majors are often influenced by the decisions of peers and role
models. We focus on role model effects, from the previous cohort, in order to avoid the most severe
form of common shocks affecting students in the same class. We thus construct the role model group
for each student based on the preceding cohort from the same high school in the same GPA quartile
(we also experiment with using the previous three cohorts rather than just the preceding one). The
restriction to the same GPA quartile is motivated by the prior literature in this area, which finds
that students with similar achievements have greater effects on each other (e.g., Poldin et al., 2015).
Furthermore, since admission to different study programs is based on high-school GPA, students with
similar GPAs have roughly the same programs to select from (Daly et al., 2022).
Specifically, the first stage for this IV strategy is
BM = βBMPeer +α +ω +(cid:15) , (4)
i si,ci−1,qi sici qi i
wherethedependentvariableisadummyforwhetherpersonifromhighschools ,graduatingincohort
i
c and in GPA quartile q , chooses to study business. Our key right-hand side variable, BMPeer ,
i i si,ci−1,qi
is the share of students in high school s , cohort c −1, and GPA quartile q who enroll in a business
i i i
program. The presence of cohort × school fixed effects α and GPA quartile fixed effects ω ensures
sici qi
that this equation exploits only within-cohort, within-high school, and within-GPA quartile variation.
Our second-stage equation in this case is at the level of individual managers and can be written as:
y˜ = γ˜BM +α +ω +ε . (5)
i i sici qi i
Here y˜ is the average firm outcome of the firms managed by person i. Because our key outcomes
i
are at the firm or individual worker level (such as the labor share or wages), while this regression is
at the level of individual managers, we now first residualize the dependent variables using the same
covariates as in our main models (industry × year fixed effects, firm size quintile × year fixed effects,
and state/region × year fixed effects) and firm fixed effects.
Our exclusion restriction in this last IV strategy is that, conditional on high school, cohort, and
GPAquartile, theoutcomesatthefirmwhereastudentislateremployedasamanagerarenotaffected
13

by the college major choice of the manager’s high school model group. This exclusion restriction could
beviolatediftherearecorrelatedshocksthataffecttheskillsorothercharacteristicsofseveraladjacent
cohorts in a given high school that may then impact their future firms. To build confidence in this
exclusion restriction, we perform a number of placebo tests and show that students in previous cohorts
in the same high school but in different GPA quartiles have no effect on major choice or future firm
outcomes. Nor do students in the same GPA quartile but at different high schools, and nor do cohorts
farther apart than three years.
4 The Effects of Business Managers on Wages and the Labor Share
In this section, we provide evidence on the effects of business managers on wages and the labor share
in the US and Denmark.
4.1 Event-Study Evidence from the US
Figure 3 presents our main event-study figures for the US, using specifications that control for industry
× year fixed effects, firm size quintile × year fixed effects, and state × year fixed effects. The first
panel shows a negative impact of a switch from a non-business manager to a business manager on log
annualwage. Thesenegativeeffectsaresignificant,andfiveyearsaftertheswitch,theannualincomeof
affected workers has declined by 6.7% (standard error = 2.5%). Notice that this specification includes
worker × firm fixed effects, and thus the wage impacts are not driven by compositional changes.
The second panel depicts a similarly large and negative impact on the labor share. Since we do not
observe value added in the US Census data, the labor share is defined as wage bill divided by sales.
Five years after the switch to a business manager, the share of labor in sales is 1.8 percentage points
lower, whichisa9%declinerelativetotheaveragesales-basedlaborshareof20%, or, ifweconvertthis
to the standard labor share in value added, it is equivalent to a 5 percentage point decline. Notably,
before the switch, there is no differential pre-trend in either wages or the labor share.
The bottom two panels show that the switch from a non-business to a business manager is not
associated with an increase in sales, employment, or investment. Some of the estimates are less precise
than our wage results, but in all cases we find no evidence of either differential trends before or any
divergence after the switch to a business manager. Similar changes in employment and output also
imply no significant changes in labor productivity. This may be either because business managers
implement no meaningful improvements, or because any positive effects they have are canceled by
other negative consequences of their wage policies (such as less cooperation with workers or greater
quits by some high-skilled workers, which we document later). In any case, the absence of any firm
growth or productivity effects make the interpretation of our wage results more straightforward.
14

Some of the individual estimates in Figure 3, especially for the labor share, are imprecise because
we allow the effect of business managers to be completely unrestricted over time. In Panel B of Table
1 below, we impose a constant coefficient for all post-treatment periods and estimate it by OLS in the
same sample of firms experiencing a single transition from non-business manager to business manager.
Wenowseepreciselyestimatedeffectsbothforaveragewageandthelaborshare: -0.063(standarderror
=0.011)fortheformerand-0.023(standarderror=0.003)forthelatterinourbaselinespecification.12
These results are robust across a range of specifications (that are not disclosed). In the Appendix,
we show that they are unchanged although less significant when we look at changes in firm average
wage (Figure A1).
4.2 Event-Study Evidence from Denmark
Figure 4 presents analogous results for Denmark. Panel (a) depicts precise and sizable effects on the
hourlywage. InDenmark, wealsohavedataonworkers’annualincome, showingverysimilarpatterns.
In particular, five years after the switch to a business manager, the annual income of affected workers
is 3.6% lower (standard error = 0.6%). Likewise, hourly wages are lower by 2.8% (standard error =
0.5%). The second panel shows that the labor share also declines, though the estimates are less precise
in this case. Our point estimate after five years indicates a 2.9 percentage point impact on the labor
share (equivalent to a 4% decline starting from a base of 68%).
The bottom two panels again confirm that business managers appear to have no impact on
productivity or other economic outcomes—we see no differential trends in value added, sales,
employment, and investment. In addition, in all cases, there are no differential pre-trends before
the switch to a business manager.
Panel B of Table 2 shows even more precisely estimated and strongly significant results when we
impose constant effects: -0.029 (standard error = 0.006) for average wage and -0.024 (standard error
= 0.007) for the labor share. The results are robust to using firm average wage (Figure A1 in the
Appendix) and varying the fixed effects we control for (Table A1).
4.3 Quantitative Magnitudes
How large are these effects? To answer this question, we take the point estimates for the wage and
laborshareeffectsfiveyearsaftertheswitchtoabusinessmanagerand, inlinewiththeevidenceinthe
previous subsection, assume that these are permanent. We then compute the aggregate consequences
of these impacts by measuring the increase in the fraction of employees in our sample operating under
12The interpretation of the quantitative magnitudes in Table 1 is slightly different, since it summarizes the average
effect after a switch to a business manager, whereas the numbers we report from our event studies are for the impact
after five years, and the figures show that the effects of business managers on wages and the labor share grow over time.
15

business managers.
This calculation implies that in the US the change towards business managers is responsible for a
1 percentage point decline in the labor share (in value added) between 1980 and 2017,13 explaining
20% of the total decline in the labor share between these dates. Likewise, the same switch explains
15% of the slowdown in wage growth in the US. In particular, average real wage growth declined from
2% growth per annum before 1980 to 0.3% growth per annum after 1980, and our estimates imply
that without the increase in the fraction of business managers, it would have declined only to 0.6% per
annum.14
The numbers for Denmark, where the fraction of the workforce working under business managers
has grown by less, are smaller, but still meaningful. Specifically, we find that the increase in the
fraction of business managers has led to a 0.2 percentage point decline in the labor share from 1995 to
2011, which accounts for 6% of the overall 4 percentage point decline in labor share over this period.
Weviewthesenumbersaslowerbounds, sincebusinessmanagers’attitudesandpracticesmayhave
also become more common among non-business managers during this period, and business managers
themselves may have started using these methods more intensively, as we discuss later.
4.4 Reversals
Wealsolookedattheeffectsofaswitchfromabusinessmanagertoanon-businessmanagerinDenmark
(which is much rarer, as suggested in Figure 2 above).15 Figure A2 in the Appendix confirms that
these switches have no impact on wages or the labor share. These results suggest that the effects of
business managers on management-labor relations may be permanent and are not reversed even after
a non-business manager takes the reins later.
4.5 Placebos
In addition to the pre-trend checks and our further exploration of endogeneity concerns, we also
conducted two placebo exercises. Figure 5 presents the results of a switch from one non-business
manager to another non-business manager in the US (Panel A) and the same exercise in Denmark
(Panel B). Reassuringly, in both cases we estimate precise zero effects. This confirms that our results
are not driven by mechanical Hawthorne effects, whereby the arrival of a new manager shakes things
up and changes wages, regardless of whether he or she has a business degree.
13The share of business managers increased by 17% from 1980 to 2020 (Figure 1), and its contribution to the decline
of the labor share is computed as 63% × 9% × 17% ≈1 percentage point.
14Ourestimatessuggestthattheeffectsofbusinessmanagersonwagesandthelaborsharecontinuetogrowafterfive
years. Ifweinsteaduseestimatesaftereightyears(whicharelessprecisebutlarger),theimpliedquantitativemagnitudes
would be 26% of the total decline in labor share in the US and 9% in Denmark. This provides an additional reason why
our quantitative magnitudes should be viewed as lower bounds.
15Such transitions are even rarer in the US, and hence we estimate this specification only on Danish data.
16

We also explore wage and labor share changes following a switch from a manager without a college
degree of any sort to one with any college degree (Panel C),16 or a switch from a manager without
a master’s degree to a manager with a master’s degree (Panel D). We find no evidence of a negative
impact on wages or the labor share from these transitions. If anything, some specifications show a
small positive (albeit insignificant) impact. This evidence suggests that the estimates reported so far
are tightly linked to managers having a business degree and are not driven just by managers having
college or higher education in general.
In Appendix Figure A3, we also show that economics degrees are not associated with similar
negative effects on wages and the labor share, so our estimated wage and labor share effects appear to
bedrivenbymanagementpracticesorwagepoliciesofmanagerswhohavereceivedbusinesseducation,
and not by selection into or education in economics-related fields more broadly.
4.6 Endogeneity Concerns I: Confounding Factors
A first endogeneity concern centers on whether other, concurrent changes might be responsible for the
patterns we document. To examine firm-level confounds, we look at the differences between business
and non-business managers across a wide range of firm-level outcomes in Denmark in Table A2. The
only notable differences between business and non-business managers concern robot purchases and
leverage (liability). As Figure A4 in the Appendix shows, these changes occur after the manager
changes, and thus we interpret them not as confounding factors, but as potential outcomes of new
business managers’ overall strategies.17
In addition, the changes are not large enough to account for the wage and labor share declines
we observe. For example, in the case of robots, Acemoglu et al. (2020) estimate a 4 percentage point
fall in the labor share following the adoption of robots in French manufacturing (see also Koch et
al., 2021, for an almost identical estimate in Spanish manufacturing). Using Danish data, Humlum
(2019) estimates a 6% decline in the wages of production workers. Using these numbers, the increase
in robot purchases associated with business managers would lead to much smaller effects than those we
estimate. For example, they can account for at most 4% of the reduced labor share that we estimate
and at most 5% of the reduction in wages that we estimate.
The empirical relationship between leverage and wages, on the other hand, is ambiguous. Berk et
al. (2010) show that an increase in leverage should lead to an increase in wages because firms need
to pay workers more to compensate them for the higher unemployment risk associated with leverage.
16WecannotdothisexerciseintheUS,sinceBoardExdatadonotdistinguishworkerswithjustacollegedegreefrom
those without a college degree.
17Thereasonwhy,despitegreaterrobotadoption,investmentisnothigheramongfirmsmanagedbybusinessgraduates
maybethatrobotsarestillasmallpartoftheoverallcapitalstockofmanycompaniesorbecauserobotsmaysubstitute
some other worker-complementary investments (see Acemoglu and Restrepo, 2021).
17

On the other hand, Michaels et al. (2019) find a negative empirical relationship between leverage and
wages: a 10 percentage point increase in leverage is associated with average wages that are lower by
1.4%. According to their estimates, the increase in leverage can account for at most 6% of the wage
decline we find.
The hiring of business managers may also coincide with changes in firms’ occupational or
organizationalstructure. Businessmanagersmayalsoadoptdifferentorganizationalformsoroutsource
certain tasks and change workers’ wages as a result. In Appendix Figure A5, we plot the average
hierarchy level and occupational wage, as well as the share of workers in low-wage occupations around
non-businesstobusinessmanagertransitionsinDenmark. Wefindnosignificantchangeinanyofthese
outcomes, suggesting that organizational changes are unlikely to be a major confound or mechanism.
The appointment of business managers may be correlated with other management changes. First,
business degrees are more prevalent among younger cohorts, raising the concern that the effects may
be driven by differences in manager ages. However, Appendix Figure A6 shows that results are similar
for switches from younger non-business managers to older business managers and for switches from
older non-business managers to younger business managers. Second, business managers who take over
family firms may renege on previous implicit contracts between family CEOs and workers. Appendix
Figure A7 shows that our results are robust to excluding firms with family CEOs in Denmark (we
define “family CEOs” as managers who are related by blood or marriage to the managers who precede
or succeed them at their firms).18
4.7 Endogeneity Concerns II: Evidence from Manager Retirements and Deaths
Thesecondthreattoourinterpretationisthatfirmsthatappointbusinessmanagersarefundamentally
different from those with non-business managers. Although our event-study graphs are reassuring and
shownopre-trendsbeforemanagertransitions,onemightstillbeconcernedaboutendogenousswitches
to business managers and time-varying omitted factors. In this subsection, we adopt our first strategy
to deal with this concern.
In the Danish data, we can determine whether the switch to a business manager is due to the
retirement or death of a previous non-business manager.19 Specifically, we define retirement as the
cessationofemploymentofapreviousmanagerwhowas62orolderuponthearrivalofanewmanager.
We also directly observe the deaths of managers (we drop deaths after the age of 65 for this exercise).
Figure 6 is analogous Figure 4, but focuses only on retirements and deaths. The results in the
18Another concern is that business managers are hired due to activist campaigns. We find that a small fraction (less
than10%)offirmswithnon-businesstobusinessmanagertransitionsaretargetedbyactivistsduringthefiveyearsbefore
the manager transitions in the US, and that our results are robust to excluding those firms.
19Becauseourmatchedemployer-employeedataintheUSisasubsample,wearenotabletodothisexerciseintheUS
case.
18

top and bottom panels are very similar, both qualitatively and quantitatively. For example, after five
years, a switch to a business manager following the retirement of a non-business manager is associated
with a 3.2% decline in workers’ annual income and a 3.4 percentage point decline in the labor share.
4.8 Endogeneity Concerns III: Evidence from the Diffusion of Business Managers
Oursecondstrategyfordealingwithtime-varyingomittedfactorsistoestimateIVmodelsasexplained
in Section 3. The first-stage relationships for the US and Denmark, which follow equation (2), are
presented in Appendix Tables A3 and A4, while the two panels of Figure 7 depict the first-stage results
visually. In these figures, we can see that the blue line, corresponding to firms in a cell following the
first hiring of business manager, starts out lower than the average of other cells, as shown by the red
line (which is by definition, since firms in the former cell initially had no business managers). However,
we also see fast convergence of the two lines, indicating that the practice of hiring managers with a
business degree diffuses rapidly across companies in the same industry, region, and size quartile. Our
identification interprets this diffusion as resulting from a “fad” or from learning from peers. What we
require for our exclusion restriction is that this diffusion driven by first adoption is orthogonal to other
factors subsequently affecting wages and the labor share in the same cell.
Tables 1 and 2 present IV estimates exploiting this source of variation for the US and Denmark,
respectively. The first three columns in each table show the effects on sales/value added, which are
insignificant, although not precisely zero as in our event studies. The next six columns in each table
depict robust negative effects on average firm wage and labor share in both countries.
The bottom panel of both tables presents the OLS estimates in the same sample, exploiting the
switch from a non-business to a business manager, essentially replicating the event-study design.
Broadly, theIVestimatesinPanelAareabout50%largerthantheOLSestimates. Ourinterpretation
of this difference between OLS and IV is related to the preceding discussion on management practices
and attitudes associated with the increasing popularity of business programs over time. For example,
suppose that, in a given cell, business managers and thus business management methods become more
popular. This will lead to the hiring of more business managers, but simultaneously there will also be
some adoption of these methods by existing non-business managers and their more intensive use by
business managers relative to other cells.
If this interpretation is correct, then the IV estimates will capture some of the systemic impacts
of business school doctrines on changes in management-labor relations. Reflecting this, if we use the
IV estimates, the implied magnitudes are correspondingly larger. In the US, with the IV estimates,
the switch towards management practices associated with business schools would explain close to 40%
of the decline of the labor share (as opposed to 20% in our baseline case). In Denmark, this number
19

would be 9% (as opposed to 6% in our baseline).
The main concern with our IV estimates is that economic shocks correlated within firm cells might
simultaneously affect the hiring of business managers and firm wages. While the industry × year fixed
effects, region × year fixed effects, and size quintile × year fixed effects already absorb industry-level
and region-level shocks and shocks related to initial firm size, we conduct several robustness tests to
furtheraddressthisconcern. Incolumns1, 4, and7inTableA5, wecontrolforafullsetofinteractions
between wage quintile in 1995 and year dummies, which should take out common shocks related to
the initial wage level. In columns 2, 5, and 8 of this table, we include cell-specific trends to deal with
unobserved heterogeneity across industry-region-size cells. In columns 3, 6, and 9, we control for three
lags of value added and wages of other firms in the same cell to allow value added and wages to be
flexibly correlated within cells. In all columns, we estimate very similar first-stage F-statistics, and
the IV estimates of the effect on wages and labor share remain negative, significant, and close to our
baseline estimates. These robustness checks increase confidence that our estimates correspond to the
causal effects of business managers on wages and the labor share.
4.9 Heterogeneous Effects
In Appendix Figures A8 and A9, we look at whether the effects are heterogeneous across worker types.
In the US, we can do this only by worker wage percentile (because we do not have precise information
on education). In this case, we estimate negative impacts on both workers above or below the median
wage, but the effects on lower-wage workers are about twice as large as the ones for higher-wage
workers. In Denmark, we find that the effects are again larger for low-skilled workers, regardless of
whether we classify them by wage percentiles or education. Appendix Figure A10 shows that workers
at the top tail of the wage distribution experience smaller yet still significant wage losses.
In Appendix Figure A11, we also look at heterogeneous effects by the level of managers’ business
degrees in Denmark. We find negative and significant wage effects for managers with business BAs and
professional BAs and for those with business MAs, with the effects being slightly larger for business
MAs. In additional (unreported) results, we also find slightly larger, but not significantly different,
effects for larger firms (which are much more likely to employ business managers).
We suggested in the Introduction that our business manager effects may reflect the impact of ideas
related to shareholder value and reengineering the corporation. If so, we should expect such effects to
be concentrated among managers who received their business education after 1980, when these ideas
were more popular and widespread in business schools. Consistent with this expectation, Appendix
Figure A12 shows that the effects are almost twice larger for Danish managers who received their
business degrees after 1980: wages decline by 4.9% and the labor share declines by 3.4 percentage
20

point within five years after transitions to business managers in the post-1980 cohorts, compared to a
2.7% decline in wages and a 1.9 percentage point decline in labor share for business managers in the
pre-1980 cohorts (the results for the US are similar, but not reported).
Finally, Appendix Figure A13 shows very similar wage effects for union and non-union workers,
confirming that the impact of business managers is not confined to unionized workers, while Figure
A14 depicts a small and statistically insignificant negative effect on unionization rates.
4.10 Who Benefits?
The results presented so far indicate that business managers reduce wages and the labor share, and
these effects are felt by workers in different parts of the skill distribution. An important question
remains: Who benefits from having a business manager? We start by looking at changes in firm
profitability, measured by return on assets (ROA). Since business managers do not change the growth
or productivity of firms, lower wages paid to workers should imply higher profits. Figure 8 shows that
following a switch to business manager, ROA increases by about 3 percentage points in the US, and
by about 1.5 percentage point in Denmark.
Higher profits also translate into higher stock market prices. We match our US firms to Compustat
and explore the effects of appointing a business manager on stock market valuations.20 Panel C of
Figure 8 shows a significant increase in shareholder returns following the appointment of a business
manager. Hence,onecleargroupofbeneficiariesfromthepracticesbroughtaboutbybusinessmanagers
are shareholders.21
Table A6 and A7 in the Appendix look at whether business managers earn more than non-business
managers in the US and Denmark, respectively. In the US, we obtain CEOs’ total compensation,
including salary, bonus, stocks and stock options, and incentive payouts, from the Compustat
Execucomp data. The results point to a significant premium for business managers, who earn at
least 5%–8% more than their non-business-school peers. In Panel B of Table A6, we also look at
the composition of compensation for business CEOs. Business CEOs receive a higher percentage of
their earnings from options, and a lower percentage of their earnings from salary and bonus, but the
differences are small and insignificant. This suggests that the differences between business and non-
business managers cannot be explained by differences in incentive pay. There is also no difference in
the percentage of earnings from stocks, suggesting that the higher compensation of business CEOs is
20In principle, we can do the same in Denmark, but this would leave us with a tiny sample, consisting of fewer than
200 firms, and hence for this exercise, we focus on the US sample.
21This result is consistent with recent work by Greenwald et al. (2019), who estimate that 44% of the increase in the
USstockmarketvaluebetween1989and2017wasduetoreallocationfromworkerstoshareholders,andwithStansbury
and Summers (2020), who document an association between declining worker power, lower wages and higher profits.
21

not mechanically driven by the higher value of the company’s stocks they own.22
Overall, although other reasons may explain why business managers earn more than their peers
without a business education, our evidence implies that their ability to reduce wages may be an
importantcomponentoftheir“success”(especiallysincetheydonotseemtohavegreaterproductivity
or achieve higher sales).
4.11 Costs of Business Managers
Management and wage policies associated with business managers may have some costs for the firm
as well. Figure 9 and Appendix Table A8 explore the effects of business managers on worker quits.
Consistent with the notion that workers are unhappy with policies and practices that lead to lower
wages and labor share, we find that quits increase following a switch to a business manager in both the
US and Denmark. For example, our estimate for Denmark in Table A8 is a 3.7 percentage point rise
in worker quits once a business manager takes over. This does not merely reflect a Hawthorne effect:
Appendix Figure A16 shows that the arrival of a non-business manager is not associated with higher
quit rates.
The results also show that quit effects are slightly larger for higher-skilled workers, despite the fact
that they suffer smaller (relative) wage reductions than low-skilled workers. This differential effect
presumably reflects these workers’ access to better outside options.
In summary, our quit findings indicate that the switch to business managers has noteworthy costs
associated with increased quits, especially among the more skilled workers.
Overall, the evidence in this section documents that business managers pay lower wages to their
employees and reduce the labor share of their firm. Several exercises suggest that these are the causal
effects of appointing a manager with a business degree. There is no evidence that business managers
are more productive or increase sales relative to non-business managers. Rather, it is their differential
wagepoliciesthattranslateintohigherprofitsandhigherreturnsforshareholders, andtheythemselves
appear to be paid more as well. In the next section, we provide evidence that their effects on wages
and the labor share are a consequence of their different rent-sharing practices.
5 Business Managers and Rent-Sharing
In this section, we provide evidence that the negative impact of business managers on wages and the
labor share is driven by their unwillingness to share rents with workers. This section focuses on results
from Denmark, where we can construct firm-level export demand shocks.
22Wealsofindnosignificantchangeinthestockoptionpaymentsreceivedbyworkers,showninAppendixFigureA15.
22

5.1 Exports, Rents, and Wages
Our main estimates, which follow the methodology outlined in Section 3, are presented in Table 3.
The table shows that positive export (demand) shocks lead to higher hourly wages and higher annual
income when a non-business manager is in charge, but not when the company is run by a business
manager. Relatedly,positiveexportshocksunderbusinessmanagersareassociatedwithdeclinesinthe
labor share. We compute rent-sharing elasticities for non-business managers as follows: in Appendix
Table A9, we show that export shocks increase profits per worker by 16%–17% and raise value added
per worker by 9%, and thus the point estimates in column 1 of Table 3 imply that a 10% increase in
profits (value added) per worker is associated with a 1% (1.9%) increase in hourly wages in firms run
by non-business managers. This elasticity is in the ballpark of the estimates in the literature.23 The
analogous elasticities for business managers are zero. These results indicate that business managers
significantly change rent-sharing patterns, moving away from sharing some of the increases in profits
and sales with workers.
Quantitatively, these estimates suggest that most of the business manager effects we have
documented so far are due to their lower propensity of sharing rents. In particular, the value added
per worker increases by 13% on average in the five years following the accession of business managers
in the event study sample. If these managers continued to share rents in the same way as non-business
managers, we would have seen 2.3% faster wage growth and a 2.5 percentage point higher labor share
during the same period. These effects thus explain the bulk of business manager effects in the Danish
sample (3% slower wage growth and a 3 percentage point lower labor share within five years).
Table 4 explores this issue further by distinguishing between positive and negative export shocks,
constructed as described in Section 3. The estimates from this exercise reveal another interesting
pattern: neither business managers nor non-business managers appear to cut wages in response to
negative export shocks. This likely reflects the fact that wage cuts are difficult to impose on workers.24
However, there is a notable difference between the behaviors of business and non-business managers
after a positive export shock: business managers do not increase wages following an (exogenous)
increase in exports, whereas non-business managers share the resulting rents. This asymmetry of
positive export shocks explains the patterns shown in Table 3 and adds nuance to them, suggesting
that the differences between business and non-business managers are more pronounced during good
times, when there are more rents to be shared.
23Inparticular,Ja¨geretal.(2020)provideanoverviewoftherent-sharingelasticitiesintheliterature. Mostestimates
of the elasticity of wages to value added per worker lie between 0.05 and 0.2.
24Downward wage rigidity is in line with the patterns documented in several works on the US and European labor
markets. See,forexample,Grigsbyetal.(2021)andHazellandTaska(2020)fortheUS,NickellandQuintini(2003)for
the UK, and Fehr and Goette (2005) for Switzerland.
23

Panel A of Table 5 adds to these results by focusing on switches from non-business to business
managers. It separately estimates the effects of export shocks on value added per worker, the
hourly wage, log annual income, and the labor share before and after such manager transitions.
It demonstrates that there is rent-sharing before the switch, which ceases after a business manager
takes office. Panel B performs a version of the same placebo exercises we reported in the previous
section, focusing on switches from a non-business manager to another non-business manager. In
comparison with the results in Panel A, we now see very similar elasticities, which is reassuring for our
interpretation.
Appendix Table A9 and Figure A17 provide a number of additional results that bolster our
confidence in these estimates. First, we show that there are no major differential responses to export
shocks in terms of increases in value added, employment, and investment between non-business and
business managers. In particular, both firms with business managers and firms with non-business
managers experience a similar increase in exports, profits, value added, employment, and investment
following these shocks. Second, we do not detect effects from leads and lags of export shocks on value
added or wages, which is also reassuring for our identification strategy.
Table 6 further supports our interpretation by estimating a version of the models in Table 3, but
now instrumenting for whether firms have business managers (based on the first stage from equation
(2) using the peer firms’ hiring of business managers). The instrumented business manager effect is
once again associated with a reduced rent-sharing elasticity, further building the case for a causal
relationship between business managers and reduced rent sharing.
The rent-sharing results are robust as well. In Table A10, we obtain very similar results when
we control for overall variation in product level exports and thus focus only on variation across firms
exporting similar products to different destinations. In Table A11, we present similar estimates for a
balanced panel of firms. In Table A12, we bolster our interpretation by confirming that our results
are driven by managers with a business degree, and there are no analogous effects for managers with
non-business college degrees, who continue to share rents just as intensively as managers without a
college degree. In Table A13, we again confirm that the difference between business and non-business
managers is present for both union and non-union workers, though the rent-sharing estimates for firms
with non-business managers is less precise in the much smaller non-union sample.
Consistentwiththerent-sharingmechanism,wefindthattheeffectsofbusinessmanagersarelarger
in industries with higher concentration where there are, Presumably, more rents to be shared. Figure
A18 repeats our event-study specification from Section 4 for industries with high vs. low concentration
(as measured by the Herfindahl-Hirschman index). We find that declines in wages and the labor share
following non-business to business manager transitions are about twice as large in highly concentrated
24

industries than in low-concentration ones, which is consistent with the notion that business managers
reduce wages primarily through sharing less rents with the workers.
5.2 Intermediate Imports and Wages
Export shocks are particularly attractive because they generate a source of variation in the demand
for a firm’s products without directly impacting its production technology or costs. A complementary
source of variation comes from the supply of internationally sourced intermediate inputs.25 These
could be interpreted as a favorable cost shock for the firm (as greater availability or cheaper supply of
importedintermediateslikelyreducecosts). Comparedtotheexportshocks,thedrawbackisthatsome
of these intermediates may be associated with automation technologies, such as numerically controlled
machineryorroboticperipherals, thusdirectlycompetingagainstsometypesofworkers(seeAcemoglu
and Restrepo, 2021). For this reason, these results should be interpreted with caution.
Nevertheless, consistent with our export results, Table A16 shows that rent-sharing responses
are very different between these two types of firms (Table A15 in the Appendix confirms that these
shocks are associated with similar increases in value added for firms run by business and non-business
managers). Non-business managers share the resulting increase in sales and profits with their workers,
with an elasticity of about 0.12 (computed in the same way as in the previous subsection). In contrast,
there is again no evidence of rent-sharing for business managers.
TablesA17,A18,andA19carryoutthesameadditionalspecificationsandchecksasintheprevious
subsection, confirming broadly similar results for intermediate imports as well.
Overall, the evidence in this section indicates that business managers are much less likely to share
with their employees rents that result either from exogenous demand shocks or from the availability
of cheaper or better intermediate inputs. In contrast, there is a stable pattern of rent-sharing among
non-business managers.
6 Selection vs. Causal Effect of Business Education
The results presented so far paint a picture in which managers with a business education reduce wages
and the labor share, and this effect seems to go hand-in-hand with a significantly reduced proclivity
to share rents with workers. Our various placebo checks and results from CEO retirements and IV
models suggest that these are the causal effects of having a manager with a business education.
25WealsolookedattheimplicationsofcompetitionfromChineseimportsattheproductlevel,asinAutoretal.(2013).
TableA14intheAppendix,however,showsdifferentialexiteffectsforfirmsimpactedbytheChineseshock,regardlessof
whether they are led by a business or non-business manager. These exit effects complicate the interpretation of Chinese
importshocksonwagesandthelaborshare,andwedonotfindconsistentrent-sharingdifferencesbetweenthetwotypes
ofmanagersinresponsetoChineseimportshocks. TableA14alsoshowsthat,reassuringly,therearenoexiteffectsfrom
export or intermediate input shocks.
25

These results still leave open the possibility that the causal effects on wages and labor share we
estimate are associated with the selection of individuals with certain characteristics into business
programs and do not reflect the impact of acquiring a business education per se. These two types
of causal effects lead us, of course, to very different interpretations. If the former is true, our results
would suggest that some managers have different styles, and they just happen to also go to business
programs. If the latter is true, our estimates would imply that the consequences we detect originate
from business education itself—either because of the curricula of these programs or some other values
individuals acquire in the process. In this section, we attempt to distinguish this selection channel
from a true causal effect of business education.
We build on the prior literature on college major choice, which suggests a powerful influence of
peers and role models (see the references in the Introduction). Specifically, we use the Danish data
to construct a role model group for our sample of managers as students who attended the same high
school, graduated one year (or in some specifications two or three years) prior, and were in the same
GPA quartile. This role model group helps us focus on the influence of older individuals (thus avoiding
the most direct common shocks that influence students in the same class/cohort). It leverages the
notion that individuals are more heavily influenced by others in their school and those ahead of them,
whom they may know or can directly observe. It also factors in the idea that high-performing students
are more likely to be influenced by the choices of other high-performing students (Poldin et al., 2015).
As noted in Section 3, our exclusion restriction is that conditional on a manager’s high school, cohort,
and GPA quartile, the outcomes at firms that he or she will later run are not affected by the college
choice of his or her role model group.
Table 7 Panel A presents our first-stage relationship. Columns 1 and 2 are for the full sample of
individuals we observe in high school and both control for a full set of school fixed effects, cohort fixed
effects, andGPAquartilefixedeffects. Column2additionallycontrolsforschool×cohortfixedeffects.
Both columns show a strong association between the share of the role model group studying business
and the share of the current cohort enrolling in a business degree. The highly significant coefficients
and the F-statistics, which hover above 100, confirm that the hypothesized role model effects are quite
strong. Columns 3 and 4 restrict the sample to individuals who later become company managers. In
this sample, too, we find strong role model effects, but F-statistics are now lower, reflecting the much
smaller sample, though still above 10.
Panel B of the same table shows that the effects are stronger for role models one or two years older
than for those three years older. This is plausible, since high school students are less likely to know
and interact with students three cohorts ahead of them than those in less distant cohorts.
Our main results, from estimates of equation (5), are presented in Table 8. Column 1 reports the
26

impact of business school education on the likelihood of ever becoming a manager (again for the full
sample, withthefirststagegivenbycolumn2ofTable7). Weseethattherole-model-inducedbusiness
education increases the likelihood of an individual becoming a manager by about 9 percentage points.
Columns 2–4 report the causal effects of role-model-induced business major choice among managers on
worker and firm outcomes. In these columns, we focus on the sample of individuals who later become
managers, and the first-stage relationship is now given in column 4 of Table 7. In these specifications,
we additionally control for the average probability of becoming a manager in each school-cohort-GPA
quartile, since students in different schools, cohorts, or GPA quartiles have different likelihoods of
becoming managers, as shown in column 1.26 In each case, the estimated effects of business managers
are very similar to our event-study results. For example, in these IV regressions, a manager with a
businessdegreereducesaverageannualwagesby3.9%andthelaborshareby2.8%. Ontheotherhand,
Table A21 confirms that role-model-induced business education does not lead to significant differences
in other firm outcomes including employment, sales, value added, and investment. Therefore, most of
our baseline effect of business managers on wages and the labor share is due to the effect of having a
business education itself rather than selection into business degrees.
Table A22 in the Appendix confirms the robustness of these results by varying the set of fixed
effects we control for. We find very similar, though somewhat less precisely estimated, effects when we
include separate high school and cohort fixed effects, rather than a full set of school × cohort effects.
Table A23 reports a number of Falsification exercises to support our exclusion restriction. First,
we look at the effects of placebo role models, constructed as students who are in the same high school
and in same cohort but in different GPA quartiles (Panel A), or in the same GPA quartile and the
same cohort but in a different high school (Panel B). These placebo role models’ major choices do not
predict the choice of business major significantly conditional on our controls, confirming that the first
stage of the IV is indeed driven by the influence of a close group of role models—one or two years
ahead and in the same GPA quartile. Perhaps more important, we show that this placebo source of
variation does not predict the wages or the labor share of firms later led by these managers, further
bolstering our argument.
In Panel C of Table A23, we report similar results using another group of placebo role models —
students in the same high school and same GPA quartile, but more than three years ahead of the
current cohort. Once again, the estimates support our exclusion restriction and interpretation.
Overall, these estimates suggest that our results capture the causal effect of obtaining a business
education, and are not driven by the fact that individuals less likely to share rents with workers select
into business education.
26The results are essentially identical when this variable is not included; see Table A20 in the Appendix.
27

7 Conclusion
Wage growth has slowed down and the labor share in national income has declined in many advanced
economies over the last three decades. We argue that a contributing factor has been changes in wage
policies of firms associated with business education of their managers/CEOs. We explore the effect
of business managers on wages and the labor share using matched employer-employee datasets from
the US and Denmark. In both countries, business managers reduce the wages of their employees. For
example, five years after the appointment of a business manager, wages decline by 6% and the labor
share by 5 percentage points in the US, and 3% and 3 percentage points in Denmark (relative to firms
operated by non-business managers).
Our evidence suggests that business managers are not more productive: firms appointing business
managers are not on differential trends and do not enjoy higher sales, productivity, investment, or
employment growth following their accession. Using manager retirements and deaths and an IV
strategy based on the diffusion of the practice of appointing business managers within industry, region,
and size quartile cells, we provide additional evidence that our results correspond to the causal effects
of managers with a business degree. Our IV strategy is appealing not just because our instrument
is orthogonal to changes in our core outcomes before the appointment of business managers or in
other variables before or after managerial transitions; it is also attractive because it captures the
broader spread of practices associated with business education within groups of firms with similar
characteristics. Arguably reflecting this broader spread, our IV estimates are about 50% larger than
our event-study or OLS estimates. Both sets of estimates imply that the contribution of managers
with business education to the decline in the labor share in Denmark and in the US is sizable, but still
no more than 20%-30% of the overall change.
We establish that the proximate cause of these (relative) wage effects are changes in rent-sharing
practicesfollowingtheappointmentofbusinessmanagers. Inthispartoftheanalysis,weuseexogenous
export demand shocks and establish that they lead to similar-sized output effects for firms run by
business and non-business managers. However, while non-business managers share greater sales and
profits with their workers (in fact with fairly high elasticities), business managers do not.
Finally, we use the influence of role models on college major choice to instrument the decision to
enrollinabusinessdegreeinDenmarkanddemonstratethatourestimatescorrespondtocausaleffects
of practices and values acquired in business education—rather than the selection of individuals averse
to rent-sharing into business education.
In line with this last set of estimates, we interpret our results as reflecting the business-school-
led shift towards emphasizing shareholder values (following Milton Friedman, 1970) and attempts to
28

reengineer corporations by making them leaner (Hammer and Champy, 1993). Unfortunately, in the
current paper, this is no more than an interpretation, since we do not have any direct evidence on
the micro channels through which business education changes managers’ overall approach and wage
policies.
We view our paper as a first step in understanding how different management practices and
ideologies might affect the labor market, wages, and inequality. Within this agenda, there are many
fruitful areas for future research.
First, our US and Danish results are remarkably similar. Although there are significant differences
in labor market institutions between the two countries, perhaps the most important of those, industry-
level wage bargaining, had already declined in Denmark and was fairly limited during our study
window. It would be valuable to investigate the effects of business education on wages and labor
market outcomes in other countries, especially in those where centralized union bargaining is still
prevalent, in order to obtain a more holistic understanding of how management practices interact with
labor market institutions.
Second, our methodology is silent on exactly what practices business managers are changing and
how these impact wages. An interesting next step would be to combine our approach with those in
studies such as Bloom and Van Reenen (2007), which measure management practices at a granular
level. Such an exercise might shed more light on what aspects of management practices matter for
wage policies and inequality.
Third, more research is needed to bolster the case that estimates such as ours correspond to causal
effects of business schools, rather than the selection of different types of individuals into business
education. Our strategy based on role models on business major choice provided evidence that most
of our estimates are due to the causal effect of business education. Nonetheless, it is important to
supplement this finding with alternative approaches.
Fourth, we conjectured that our results may be related to the spread via business schools of
shareholder values and ideas about corporation reengineering. Business schools are, of course, not
the only institutions pushing firms in this direction. The other major nexus where the same effect has
emerged over the last four decades has been management consulting, and it would be interesting to
explore the effects of management consulting advice on firms’ wage policies.
Finally, and relatedly, our study does not address what types of values and practices managers
acquireinbusinesseducation. Itwouldbeveryinterestingtomatchemployeeandmanagerinformation
to the curriculum and networking practices of specific business schools to shed more light on this
question.
29

References
Acemoglu, Daron and Pascual Restrepo, “Automation and New Tasks: How Technology
Displaces and Reinstates Labor,” Journal of Economic Perspectives, May 2019, 33 (2), 3–30.
and , “Demographics and Automation,” The Review of Economic Studies, June 2021.
, Claire Lelarge, and Pascual Restrepo, “Competing with Robots: Firm-Level Evidence from
France,” AEA Papers and Proceedings, May 2020, 110, 383–388.
, Suresh Naidu, Pascual Restrepo, and James A. Robinson, “Democracy Does Cause
Growth,” Journal of Political Economy, February 2019, 127 (1), 47–100.
Arcidiacono, Peter and Sean Nicholson, “Peer effects in medical school,” Journal of Public
Economics, February 2005, 89 (2), 327–350.
Autor, David, David Dorn, Lawrence F Katz, Christina Patterson, and John Van Reenen,
“TheFalloftheLaborShareandtheRiseofSuperstarFirms,”The Quarterly Journal of Economics,
May 2020, 135 (2), 645–709.
Autor, David H. and David Dorn, “The Growth of Low-Skill Service Jobs and the Polarization
of the US Labor Market,” American Economic Review, August 2013, 103 (5), 1553–1597.
, , and Gordon H. Hanson, “The China Syndrome: Local Labor Market Effects of Import
Competition in the United States,” American Economic Review, October 2013, 103 (6), 2121–2168.
Bauman, Yoram and Elaina Rose, “Selection or indoctrination: Why do economics students
donate less than the rest?,” Journal of Economic Behavior & Organization, August 2011, 79 (3),
318–327.
Benmelech, Efraim and Carola Frydman, “Military CEOs,” Journal of Financial Economics,
July 2015, 117 (1), 43–59.
Bennis, Warren G. and Jim O’Toole,“Howbusinessschoolshavelosttheirway,”Harvard business
review, 2005, 83 (5), 96–104.
Berk, Jonathan B., Richard Stanton, and Josef Zechner, “Human Capital, Bankruptcy, and
Capital Structure,” The Journal of Finance, 2010, 65 (3), 891–926.
Bertrand, Marianne and Antoinette Schoar, “Managing with Style: The Effect of Managers on
Firm Policies,” The Quarterly Journal of Economics, November 2003, 118 (4), 1169–1208.
Bhagat, Sanjai, BrianJ.Bolton, andAjaySubramanian,“CEOEducation,CEOTurnover,and
FirmPerformance,”SSRNScholarlyPaperID1670219,SocialScienceResearchNetwork,Rochester,
NY August 2010.
Blanchard, Olivier, “The Medium Run,” Brookings Papers on Economic Activity, 1997.
Blanchflower, David G., Andrew J. Oswald, and Peter Sanfey, “Wages, Profits, and Rent-
Sharing,” The Quarterly Journal of Economics, February 1996, 111 (1), 227–251.
Bloom, Nicholas and John Van Reenen, “Measuring and Explaining Management Practices
Across Firms and Countries,” The Quarterly Journal of Economics, November 2007, 122 (4), 1351–
1408.
Borusyak, Kirill, Xavier Jaravel, and Jann Spiess, “Revisiting Event Study Designs: Robust
and Efficient Estimation,” arXiv:2108.12419 [econ], August 2021. arXiv: 2108.12419.
Brealey, Richard A. and Stewart C. Myers, Principles of Corporate Finance, McGraw-Hill,
October 1980.
Caldwell, Sydnee and Nikolaj Harmon, “Outside options, bargaining, and wages: Evidence from
30

coworker networks,” Unpublished manuscript, Univ. Copenhagen, 2019, pp. 203–207.
Card, David, AnaRuteCardoso, andPatrickKline,“Bargaining,Sorting,andtheGenderWage
Gap: Quantifying the Impact of Firms on the Relative Pay of Women,” The Quarterly Journal of
Economics, May 2016, 131 (2), 633–686.
, J¨org Heining, and Patrick Kline, “Workplace Heterogeneity and the Rise of West German
Wage Inequality,” The Quarterly Journal of Economics, August 2013, 128 (3), 967–1015.
Chevalier, JudithandGlennEllison,“CareerConcernsofMutualFundManagers,”TheQuarterly
Journal of Economics, May 1999, 114 (2), 389–432.
Copeland, Thomas E. and Fred J. Weston, Financial Theory and Corporate Policy, Addison-
Wesley, January 1979.
Cust´odio, Cl´audia and Daniel Metzger, “Financial expert CEOs: CEO’s work experience and
firm’s financial policies,” Journal of Financial Economics, October 2014, 114 (1), 125–154.
Dahl, Christian M., Daniel le Maire, and Jakob R. Munch, “Wage Dispersion and
Decentralization of Wage Bargaining,” Journal of Labor Economics, July 2013, 31 (3), 501–533.
Daly, Moira, Mathias Fjællegaard Jensen, and Daniel le Maire, “University Admission and
the Similarity of Fields of Study: Effects on Earnings and Skill Usage,” Labour Economics, January
2022, p. 102118.
Davenport, Thomas H., Process Innovation: Reengineering Work Through Information Technology,
Harvard Business Press, February 1993.
de Chaisemartin, Cl´ement and Xavier D’Haultfœuille, “Two-Way Fixed Effects Estimators
with Heterogeneous Treatment Effects,” American Economic Review, September 2020, 110 (9),
2964–2996.
DiNardo, John, Nicole M. Fortin, and Thomas Lemieux, “Labor Market Institutions and
the Distribution of Wages, 1973-1992: A Semiparametric Approach,” Econometrica, 1996, 64 (5),
1001–1044.
Duchin, Ran, Mikhail Simutin, and Denis Sosyura,“TheOriginsandRealEffectsoftheGender
Gap: Evidence from CEOs’ Formative Years,” The Review of Financial Studies, February 2021, 34
(2), 700–762.
Farber, Henry S, Daniel Herbst, Ilyana Kuziemko, and Suresh Naidu, “Unions and
Inequality over the Twentieth Century: New Evidence from Survey Data,” The Quarterly Journal
of Economics, August 2021, 136 (3), 1325–1385.
Fehr, Ernst and Lorenz Goette, “Robustness and Real Consequences of Nominal Wage Rigidity,”
Journal of Monetary Economics, May 2005, 52 (4), 779–804.
Frank, Robert H., Thomas D. Gilovich, and Dennis T. Regan, “Do Economists Make Bad
Citizens?,” Journal of Economic Perspectives, March 1996, 10 (1), 187–192.
, Thomas Gilovich, and Dennis T. Regan, “Does Studying Economics Inhibit Cooperation?,”
Journal of Economic Perspectives, June 1993, 7 (2), 159–171.
Freeman, R. Edward,Strategic Management: A Stakeholder Approach,CambridgeUniversityPress,
March 2010.
and David L. Reed, “Stockholders and Stakeholders: A New Perspective on Corporate
Governance,” California Management Review, April 1983, 25 (3), 88–106.
Freeman, Richard B., “Labor Market Institutions Around the World,” Working Paper 13242,
National Bureau of Economic Research July 2007. Series: Working Paper Series.
31

Frey, Bruno S. and Stephan Meier,“ArePoliticalEconomistsSelfishandIndoctrinated? Evidence
from a Natural Experiment,” Economic Inquiry, 2003, 41 (3), 448–462.
Garin, Andrew and Filipe Silv´erio, “How responsive are wages to demand within the firm?
evidence from idiosyncratic export demand shocks,” Technical Report 2019.
Ghoshal, Sumantra, “Bad Management Theories Are Destroying Good Management Practices,”
Academy of Management Learning & Education, March 2005, 4 (1), 75–91.
Graham, John R., Campbell R. Harvey, and Manju Puri, “Managerialattitudesandcorporate
actions,” Journal of Financial Economics, July 2013, 109 (1), 103–121.
, , and , “Capital allocation and delegation of decision-making authority within firms,” Journal
of Financial Economics, March 2015, 115 (3), 449–470.
Greenwald, Daniel L., Martin Lettau, and Sydney C. Ludvigson, “How the Wealth Was
Won: FactorsSharesasMarketFundamentals,”WorkingPaper25769,NationalBureauofEconomic
Research April 2019.
Grigsby, John, Erik Hurst, and Ahu Yildirmaz, “Aggregate Nominal Wage Adjustments: New
Evidence from Administrative Payroll Data,” American Economic Review, February 2021, 111 (2),
428–471.
Guti´errez, Germ´an and Thomas Philippon,“DecliningCompetitionandInvestmentintheU.S.,”
Working Paper 23583, National Bureau of Economic Research July 2017. Series: Working Paper
Series.
Hall, Peter A. and David Soskice, “An Introduction to Varieties of Capitalism,” op. cit, 2001,
pp. 21–27.
Hambrick, Donald C. and Phyllis A. Mason, “UpperEchelons: TheOrganizationasaReflection
of Its Top Managers,” Academy of Management Review, April 1984, 9 (2), 193–206.
Hammer, Michael and James Champy, “Business process reengineering,” London: Nicholas
Brealey, 1993, 444 (10), 730–755.
Hassard, John and Jonathan Morris, “The Extensification of Managerial Work in the Digital
Age: Middle Managers, Spatio-temporal Boundaries and Control,” Human Relations, March 2021.
Hazell, Jonathon and Bledi Taska, “Downward Rigidity in the Wage for New Hires,” SSRN
Scholarly Paper ID 3728939, Social Science Research Network, Rochester, NY November 2020.
He, Alex Xi and Daniel le Maire, “Mergers and Managers: Manager-Specific Wage Premiums and
Rent Extraction in M&As,” SSRN Scholarly Paper ID 3481262, Social Science Research Network,
Rochester, NY October 2020.
H´emous, David and Morten Olsen, “The Dynamics of the Labor Share: Evidence from Danish
Microdata,” Unpublished manuscript, 2020.
Hermalin, Benjamin E. and Michael S. Weisbach, “Endogenously Chosen Boards of Directors
and Their Monitoring of the CEO,” The American Economic Review, 1998, 88 (1), 96–118.
Hildreth, Andrew and Andrew J. Oswald, “Rent-Sharing and Wages: Evidence from Company
and Establishment Panels,” Journal of Labor Economics, April 1997, 15 (2), 318–337.
Holt, Robin, “Hannah Arendt and the Raising of Conscience in Business Schools,” Academy of
Management Learning & Education, December 2020, 19 (4), 584–599.
Humlum, Anders, “Robot adoption and labor market dynamics,” Princeton University, 2019.
Hummels, David, Rasmus Jørgensen, Jakob Munch, and Chong Xiang, “The Wage Effects
32

of Offshoring: Evidence from Danish Matched Worker-Firm Data,” American Economic Review,
June 2014, 104 (6), 1597–1629.
Ilsøe, Anna, “TheFlipSideofOrganizedDecentralization: Company-LevelBargaininginDenmark,”
British Journal of Industrial Relations, 2012, 50 (4), 760–781.
Jensen, Michael C. and Kevin J. Murphy, “Performance Pay and Top-Management Incentives,”
Journal of Political Economy, April 1990, 98 (2), 225–264.
and William H. Meckling,“Theoryofthefirm: Managerialbehavior,agencycostsandownership
structure,” Journal of Financial Economics, October 1976, 3 (4), 305–360.
and , “Rights and Production Functions: An Application to Labor-Managed Firms and
Codetermination,” The Journal of Business, 1979, 52 (4), 469–506.
J¨ager, Simon, Benjamin Schoefer, Samuel Young, and Josef Zweimu¨ller, “Wages and the
Value of Nonemployment,” The Quarterly Journal of Economics, November 2020, 135 (4), 1905–
1963.
Kaplan, Steven N., Mark M. Klebanov, and Morten Sorensen, “Which CEO Characteristics
and Abilities Matter?,” The Journal of Finance, 2012, 67 (3), 973–1007.
Karabarbounis, Loukas and Brent Neiman, “The Global Decline of the Labor Share,” The
Quarterly Journal of Economics, February 2014, 129 (1), 61–103.
Kline, Patrick, Neviana Petkova, Heidi Williams, and Owen Zidar, “Who Profits from
Patents? Rent-Sharing at Innovative Firms,” The Quarterly Journal of Economics, August 2019,
134 (3), 1343–1404.
Koch, Michael, Ilya Manuylov, and Marcel Smolka, “Robots and Firms,” The Economic
Journal, August 2021, 131 (638), 2553–2584.
Lockwood, Penelope, ““Someone Like Me can be Successful”: Do College Students Need Same-
Gender Role Models?,” Psychology of Women Quarterly, March 2006, 30 (1), 36–46.
and Ziva Kunda, “Superstars and me: Predicting the impact of role models on the self.,” Journal
of personality and social psychology, 1997, 73 (1), 91.
Loecker, Jan De, Jan Eeckhout, and Gabriel Unger, “The Rise of Market Power and the
Macroeconomic Implications,” The Quarterly Journal of Economics, May 2020, 135 (2), 561–644.
Malmendier, Ulrike and Geoffrey Tate, “CEO Overconfidence and Corporate Investment,” The
Journal of Finance, 2005, 60 (6), 2661–2700.
and , “Who makes acquisitions? CEO overconfidence and the market’s reaction,” Journal of
Financial Economics, July 2008, 89 (1), 20–43.
, , and Jon Yan, “Overconfidence and Early-Life Experiences: The Effect of Managerial Traits
on Corporate Financial Policies,” The Journal of Finance, 2011, 66 (5), 1687–1733.
Marens, Richard,“WeDon’tNeedYouAnymore: CorporateSocialResponsibilities,ExecutiveClass
Interests, and Solving Mizruchi and Hirschman’s Paradox Berle III: Theory of the Firm: The Third
Annual Symposium of the Adolf A. Berle, Jr. Center on Corporations, Law & Society,” Seattle
University Law Review, 2011, 35 (4), 1189–1226.
, “The Second Time Farce: Business School Ethicists and the Emergence of Bastard Rawlsianism,”
Oxford Handbook of Sociology, Social Theory and Organization Studies: Contemporary Currents,
2014, p. 447.
Michaels, Ryan, T Beau Page, and Toni M Whited, “Labor and Capital Dynamics under
Financing Frictions,” Review of Finance, March 2019, 23 (2), 279–323.
33

Miller, Danny and Xiaowei Xu,“AFleetingGlory: Self-ServingBehaviorAmongCelebratedMBA
CEOs,” Journal of Management Inquiry, July 2016, 25 (3), 286–300. Publisher: SAGE Publications
Inc.
and , “MBA CEOs, Short-Term Management and Performance,” Journal of Business Ethics,
January 2019, 154 (2), 285–300.
Nickell, Stephen and Glenda Quintini, “Nominal Wage Rigidity and the Rate of Inflation,” The
Economic Journal, October 2003, 113 (490), 762–781.
Piketty, Thomas and Gabriel Zucman, “CapitalisBack: Wealth-IncomeRatiosinRichCountries
1700–2010,” The Quarterly Journal of Economics, August 2014, 129 (3), 1255–1310.
Poldin, O., D. Valeeva, and M. Yudkevich, “Choice of specialization: do peers matter?,” Applied
Economics, September 2015, 47 (44), 4728–4740.
Rappaport, Alfred, Creating Shareholder Value: A Guide For Managers And Investors, Simon and
Schuster, October 1999.
Rask, Kevin N. and Elizabeth M. Bailey, “Are Faculty Role Models? Evidence from Major
Choice in an Undergraduate Institution,” The Journal of Economic Education, January 2002, 33
(2), 99–124.
Reenen, John Van, “The Creation and Capture of Rents: Wages and Innovation in a Panel of U.
K. Companies,” The Quarterly Journal of Economics, February 1996, 111 (1), 195–226.
Schoar, Antoinette and Luo Zuo, “Shaped by Booms and Busts: How the Economy Impacts CEO
Careers and Management Styles,” The Review of Financial Studies, May 2017, 30 (5), 1425–1456.
Smith, Matthew, Danny Yagan, Owen Zidar, and Eric Zwick,“CapitalistsintheTwenty-First
Century,” The Quarterly Journal of Economics, November 2019, 134 (4), 1675–1745.
Song, Jae, David J Price, Fatih Guvenen, Nicholas Bloom, and Till von Wachter, “Firming
Up Inequality,” The Quarterly Journal of Economics, February 2019, 134 (1), 1–50.
Stansbury, Anna and Lawrence H. Summers, “The Declining Worker Power Hypothesis: An
Explanation for the Recent Evolution of the American Economy,” Brookings Papers on Economic
Activity, 2020, 2020 (1), 1–96.
Wang, Long and J. Keith Murnighan, “On Greed,” Academy of Management Annals, June 2011,
5 (1), 279–316.
, Deepak Malhotra, and J. Keith Murnighan, “Economics Education and Greed,” Academy
of Management Learning & Education, December 2011, 10 (4), 643–660.
Wiswall, Matthew and Basit Zafar, “Determinants of College Major Choice: Identification using
an Information Experiment,” The Review of Economic Studies, April 2015, 82 (2), 791–824.
Womack, James P. and Daniel T. Jones, “Banish waste and create wealth in your corporation,”
Recuperado de http://www. kvimis. co. in/sites/kvimis. co. in/files/ebook attachments/James, 2003.
34

Figure 1: Share of Compustat Firms with Business CEOs in the US
erahS
54.
4.
53.
3.
52.
2.
1980 1990 2000 2010 2020
Year
Share of firms with Business-Degree CEOs Share of firms with MBA CEOs
This figure plots the share of Compustat firms that have CEOs with business degrees (“business
managers”) and the share of Compustat firms that have CEOs with MBA degrees from 1980 to 2020.
The education information of CEOs is from the BoardEx dataset.
Figure 2: Share of Business Managers in Denmark
91.
71.
51.
31.
11.
1995 2000 2005 2010
year
80.
60.
40.
20.
0
1995 2000 2005 2010
year
Short Education Professional BA
University BA MA & PhD
(a) Share of Business Managers (b) by Degree Level
This figure plots the share of business managers in Denmark from 1995 to 2011. Panel (a) plots the
shareofallfirmswithover5employeesintheprivatesectorwhosemanagerhasabusinessdegree,while
Panel (b) plots the share of firms whose manager has a short-education business degree, a professional
BA in business, a university BA in business, and a MA or PhD degree in business (for each manager
with a business degree, only the highest business degree is recorded).
35

Figure 3: Changes in Firm and Worker Outcomes around Non-Business to Business Manager
Transitions in the US
egaw
goL
50.
0
50.-
1.-
51.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
erahs
robaL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Wage (b) Labor Share
eunever
goL
2.
1.
0
1.-
2.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
egnahc
goL
2.
1.
0
1.-
2.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Employment Investment
(c) Output (d) Employment and Investment
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in the US. The sample includes firms
thathavenon-businessmanagersinallyears,andfirmsthathaveonenon-businesstobusinessmanager
transitioneventduringthesampleperiod. Panel(a)usesworker-leveldataandthematchingestimator
is described in Section 3. Panels (b), (c), and (d) use firm-level data and include firm fixed effects,
industry×yearfixedeffects, state×yearfixedeffects, andinitialsizequintilebyyearfixedeffects. Firm-
level regressions are weighted by employment. The dependent variables are log hourly wage and log
annual income in Panel (a), the labor share in Panel (b), log sales in Panel (c), and log employment
and log capital expenditure in Panel (d). The labor share is defined as total wage bill divided by sales.
Investment rate is calculated from the Compustat data. All standard errors are clustered at the firm
level.
36

Figure 4: Changes in Firm and Worker Outcomes around Non-Business to Business Manager
Transitions in Denmark
egaw
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Hourly Wage Annual Income
erahs
robaL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Wage (b) Labor Share
egnahc
goL
2.
1.
0
1.-
2.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Output Value Added
egnahc
goL
3.
2.
1.
0
1.-
2.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Employment Investment
(c) Output and Value Added (d) Employment and Investment
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in Denmark. The sample includes
firms that have non-business managers in all years, and firms that have one non-business to business
manager transition event during the sample period. All regressions control for firm fixed effects, initial
sizequintilebyyearfixedeffects,region×yearfixedeffectsandindustry×yearfixedeffects. Worker-level
regressions in Panel (a) additionally control for firm×worker fixed effects, quadratic in experience, and
unionandmaritalstatusdummies. Firm-levelregressionsareweightedbyemployment. Thedependent
variables are log hourly wage and log annual income in Panel (a), the labor share in Panel (b), log
output and log value added in Panel (c), and log employment and log investment in Panel (d). The
labor share is defined as total wage bill divided by value added. All standard errors are clustered at
the firm level.
37

Figure 5: Changes in Wages and the Labor Share around Placebo Manager Transitions
1.
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Log Wage Labor Share
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Log Wage Labor Share
(a) Non-business to non-business, US (b) Non-business to non-business, Denmark
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Log Wage Labor Share
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Log Wage Labor Share
(c) Non-college to college, Denmark (d) Non-master to master, Denmark
This figure plots event-study estimates and 95% confidence intervals based on placebo manager
transitions. In Panel (a), events are manager transitions from a non-business manager to another non-
business manager in the US. In Panel (b), events are manager transitions from a non-business manager
to another non-business manager in the Denmark. In Panel (c), events are manager transitions from
a non-college-educated manager to a college-educated manager in Denmark. In Panel (d), events are
manager transitions from a manager without a master’s degree or PhD to a manager with a master’s
degree or PhD in Denmark. The dependent variables are log annual wage at the worker level and the
labor share at the firm level. Standard errors are clustered at the firm level.
38

Figure 6: Changes in Firm and Worker Outcomes around Transitions to Business Managers due to
Manager Retirements and Deaths in Denmark
egaw
goL
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager retirement/death
Hourly Wage Annual Income
erahs
robaL
40.
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Wage (b) Labor Share
egnahc
goL
60.
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager retirement/death
Output Value Added
egnahc
goL
1.
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager retirement/death
Employment Investment
(c) Output and Value Added (d) Employment and Investment
This figure plots event-study estimates and 95% confidence intervals, where events are retirements (as
defined in the text) or sudden deaths of non-business managers with the successor being a business
manager in Denmark. All regressions control for firm fixed effects, initial size quintile by year fixed
effects, region×year fixed effects and industry×year fixed effects. Worker-level regressions in Panel
(a) additionally control for firm×worker fixed effects, quadratic in experience, and union and marital
status dummies. Firm-level regressions are weighted by employment. The dependent variables are log
hourly wage and log annual income in Panel (a), the labor share in Panel (b), log output and log value
added in Panel (c), and log employment and log investment in Panel (d). The labor share is defined
as total wage bill divided by value added. All standard errors are clustered at the firm level.
39

Figure 7: Visual Representation of the First Stage for Business Manager Transitions
(a) US
(b) Denmark
This figure plots average fraction of firms in a region-industry-size cell with no past business manager
(blue), where zero is the year of first business manager hiring in the cell. For comparison, we also plot
average fraction of firms in other cells (red) in the same year. Panel (a) is for the US and Panel (b)
for Denmark. See text for further details.
40

Figure 8: Changes in Return on Assets and Market Value around Non-Business to Business Manager
Transitions
AOR
60.
40.
20.
0
20.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
AOR
30.
20.
10.
0
10.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) ROA, US firms (b) ROA, Danish firms
eulav
tekram
goL
1.
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(c) Market value, US firms
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager. Panels (a) and (c) use US Compsutat
data, and Panel (b) uses data from Denmark. In Panels (a) and (b), the dependent variable is return
on assets (ROA), defined as earnings before interests and taxes (or profits in Denmark) divided by
total assets. In Panel (c), the dependent variable is log market value, which is total assets minus the
common equity book value and adding back the market value of the common equity. All specifications
include firm fixed effects, industry×year fixed effects, state(region)×year fixed effects, and initial size
quintile by year fixed effects. Standard errors are clustered at the firm level.
41

Figure 9: Changes in Quit Rates around Non-Business to Business Manager Transitions
etar
tiuQ
1.
50.
0
50.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
etar
tiuQ
51.
1.
50.
0
50.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Quit rates of all workers, US (b) Quit rates of all workers, Denmark
etar
tiuQ
1.
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Low Wage High Wage
etaR
tiuQ
51.
1.
50.
0
50.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Low Wage High Wage
(c) Quit rates by wage level, US (d) Quit rates by wage level, Denmark
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager. Panels (a) and (b) use US data
and Panels (c) and (d) use data from Denmark. The dependent variable is the share of workers that
quit the firm to join another firm or become unemployed in the following year. In Panels (c) and
(d), the solid line is quit rate for workers below the median wage, and the dashed line is quit rate for
workers above the median wage. All regressions include firm fixed effects, industry×year fixed effects,
state(region)×year fixed effects, and initial size quintile by year fixed effects, and observations are
weighted by employment. Standard errors are clustered at the firm level.
42

Table 1: 2SLS and OLS Estimates of Business Managers on Firm Outcomes in the US
Panel A: IV
Log Sales Log Average Wage Labor Share
(1) (2) (3) (4) (5) (6) (7) (8) (9)
Business Manager -0.027 -0.051 -0.032 -0.094 -0.075 -0.105 -0.035 -0.023 -0.036
(0.052) (0.046) (0.043) (0.055) (0.044) (0.041) (0.019) (0.015) (0.016)
Log Average Wage t-1 x x x x x x x x x
Log Average Wage t-2 x x x x x x
Log Average Wage t-3 x x x
Log Sales t-1 x x x x x x x x x
Log Sales t-2 x x x x x x
Log Sales t-3 x x x
Size quintile-year FE Y Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y Y
Industry-year FE Y Y Y Y Y Y Y Y Y
State-year FE Y Y Y Y Y Y Y Y Y
F statistic 32.6 44.8 41.9 32.6 44.8 41.9 32.6 44.8 41.9
Panel B: OLS
Log Sales Log Average Wage Labor Share
(1) (2) (3) (4) (5) (6) (7) (8) (9)
Business Manager -0.006 -0.004 -0.012 -0.059 -0.047 -0.063 -0.021 -0.012 -0.023
(0.008) (0.008) (0.007) (0.013) (0.013) (0.011) (0.003) (0.003) (0.003)
Size quintile-year FE Y Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y Y
Industry-year FE Y Y Y Y Y Y Y Y Y
State-year FE Y Y Y Y Y Y Y Y Y
This table reports 2SLS (Panel A) and OLS (Panel B) estimates of business managers on log sales, log
average wage and the labor share in the US. The sample in both panels is the set of firms with a single
transition from non-business to business manager or firms with non-business managers as in our event-
study regressions. For the 2SLS models, the first stage is described in equation (2) and is based on the
average lagged business manager of peer firms (those in the same industry, region and size quartile).
Table A3 in the Appendix presents the first-stage estimates and Figure 7 shows them visually. In all
columns we control for firm fixed effects, initial size quintile by year fixed effects, region×year fixed
effects and industry×year fixed effects. Columns 1, 4 and 7 control for one-year lags of firm (log)
sales and (log) average wage, columns 2, 5 and 8 control for one and two-year lags of firm sales and
average wage, and columns 3, 6 and 9 control for one, two and three-year lags of firm sales and average
wage. The dependent variables are log sales in columns 1–3, log average annual wage in columns 4–6,
and the firm’s labor share (wage bill divided by sales) in columns 7–9. Observations are weighted by
firm employment and standard errors are clustered at the firm level. First-stage F-statistics for the
excluded instruments are reported at the bottom of Panel A.
43

Table 2: 2SLS and OLS Estimates of Business Managers on Firm Outcomes in Denmark
Panel A: IV
Log Value Added Log Average Wage Labor Share
(1) (2) (3) (4) (5) (6) (7) (8) (9)
Business Manager 0.105 0.091 0.078 -0.048 -0.038 -0.044 -0.037 -0.046 -0.052
(0.068) (0.068) (0.067) (0.024) (0.024) (0.024) (0.027) (0.027) (0.027)
Log Average Wage t-1 -0.179 -0.155 -0.157 0.129 0.128 0.125 0.002 0.010 0.011
(0.010) (0.010) (0.010) (0.005) (0.005) (0.005) (0.004) (0.004) (0.004)
Log Average Wage t-2 -0.028 -0.018 -0.011 -0.010 -0.018 -0.009
(0.011) (0.011) (0.005) (0.005) (0.005) (0.005)
Log Average Wage t-3 -0.066 -0.038 -0.020
(0.010) (0.005) (0.004)
Log Value Added t-1 0.479 0.441 0.440 0.006 0.006 0.006 -0.011 -0.019 -0.021
(0.004) (0.005) (0.005) (0.002) (0.002) (0.002) (0.002) (0.002) (0.002)
Log Value Added t-2 0.069 0.060 -0.001 0.002 0.018 0.005
(0.005) (0.005) (0.002) (0.003) (0.002) (0.002)
Log Value Added t-3 0.016 -0.007 0.026
(0.004) (0.002) (0.002)
Size quintile-year FE Y Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y Y
Industry-year FE Y Y Y Y Y Y Y Y Y
Region-year FE Y Y Y Y Y Y Y Y Y
F statistic 32.2 32.0 32.4 31.6 31.1 31.4 32.0 31.3 31.7
Obs 44,731 44,539 44,474 44,731 44,550 44,490 44,962 44,761 44,697
Panel B: OLS
Log Value Added Log Average Wage Labor Share
(1) (2) (3) (4) (5) (6) (7) (8) (9)
Business Manager 0.007 0.008 0.008 -0.028 -0.028 -0.029 -0.025 -0.024 -0.024
(0.015) (0.015) (0.015) (0.006) (0.006) (0.006) (0.007) (0.007) (0.007)
Size quintile-year FE Y Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y Y
Industry-year FE Y Y Y Y Y Y Y Y Y
Region-year FE Y Y Y Y Y Y Y Y Y
Obs 44,731 44,539 44,474 44,731 44,550 44,490 44,962 44,761 44,697
This table reports 2SLS (Panel A) and OLS (Panel B) estimates of business managers on log value
added, log average wage and the labor share in Denmark. For the 2SLS models, the first stage is
described in equation (2) and is based on the average lagged business manager of peer firms (those
in the same industry, region and size quartile). Table A4 in the Appendix presents the first-stage
estimates and Figure 7 shows them visually. In all columns we control for firm fixed effects, initial size
quintile by year fixed effects, region×year fixed effects and industry×year fixed effects. Columns 1, 4
and 7 control for one-year lags of firm (log) value added and (log) average wage, columns 2, 5 and 8
control for one and two-year lags of firm value added and average wage, and columns 3, 6 and 9 control
for one, two and three-year lags of firm value added and average wage. The dependent variables are
log value added in columns 1–3, log average annual wage in columns 4–6, and the firm’s labor share
(wage billdivided by value added) in columns7–9. Observations are weighted byfirm employment and
standard errors are clustered at the firm level. First-stage F-statistics for the excluded instruments are
reported at the bottom of Panel A.
44

Table 3: Business Managers and Wage Response to Export Shocks in Denmark
Log Hourly Wage Log Income Labor Share Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Export Shock*Non-Business Manager 0.017 0.022 -0.013 0.013 0.015 -0.001
(0.003) (0.004) (0.009) (0.003) (0.004) (0.008)
Export Shock*Business Manager 0.002 0.010 -0.027 -0.003 -0.001 -0.018
(0.007) (0.007) (0.012) (0.007) (0.006) (0.009)
Log Output 0.013 0.013 -0.163
(0.003) (0.005) (0.011)
Log Employment 0.014 0.045 0.164
(0.004) (0.005) (0.012)
Log Capital-labor Ratio 0.003 0.000 -0.010
(0.001) (0.001) (0.004)
Share of High-skilled Workers 0.088 0.076 0.224
(0.020) (0.025) (0.056)
Industry-year FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Firm FE Y Y
Obs 1,783,859 1,783,694 5,157 1,783,859 1,783,694 5,157
This table reports the coefficients from regressions of wages and the labor share on export shocks and their interactions with a firm-level
indicator for having a business manager. Export shocks are shocks to export demand from destination-product combinations the firm
exports to as defined in the text. In all columns we control for firm fixed effects, initial size quintile by year fixed effects, region×year fixed
effects and industry×year fixed effects. Worker-level regressions additionally control for firm×worker fixed effects, quadratic in experience,
and union and marital status dummies. Columns 3–6 also control for time-varying firm characteristics (log output, log employment, log
capital-labor ratio, share of high-skilled workers). The dependent variables are log hourly wage of workers in columns 1 and 4, log annual
income of workers in columns 2 and 5, and the labor share of firms (wage bill divided by value added) in columns 3 and 6. Firm-level
regressions in columns 3 and 6 are weighted by firm employment. Standard errors are clustered at the firm level.
45

Table 4: Response to Positive and Negative Export Shocks in Denmark
Log Hourly Wage Log Income Labor Share Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Pos Export Shock*Non-Business Manager 0.022 0.017 -0.006 0.020 0.022 -0.003
(0.005) (0.004) (0.012) (0.005) (0.004) (0.011)
Pos Export Shock*Business Manager 0.006 0.008 -0.033 0.005 0.008 -0.026
(0.011) (0.007) (0.013) (0.011) (0.007) (0.013)
Neg Export Shock*Non-Business Manager 0.004 0.001 -0.011 -0.006 0.005 -0.008
(0.004) (0.003) (0.008) (0.004) (0.004) (0.008)
Neg Export Shock*Business Manager 0.007 0.006 -0.016 0.003 0.010 -0.004
(0.010) (0.007) (0.014) (0.010) (0.007) (0.013)
Log Output 0.012 0.013 -0.164
(0.003) (0.005) (0.011)
Log Employment 0.013 0.044 0.165
(0.004) (0.005) (0.012)
Log Capital-labor Ratio 0.003 0.000 -0.010
(0.001) (0.001) (0.004)
Share of High-skilled Workers 0.079 0.072 0.228
(0.020) (0.028) (0.056)
Industry-year FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Firm FE Y Y
Obs 1,783,859 1,783,694 5,157 1,783,859 1,783,694 5,157
Thistablereportsthecoefficientsfromregressionsofwagesandthelaborshareonpositiveandnegativeexportshocksandtheirinteractions
with a firm-level indicator for having a business manager. Positive and negative export shocks are defined in section 3. In all columns we
controlforfirmfixedeffects, initialsizequintilebyyearfixedeffects, region×yearfixedeffectsandindustry×yearfixedeffects. Worker-level
regressions additionally control for firm×worker fixed effects, quadratic in experience, and union and marital status dummies. Columns
3–6 also control for time-varying firm characteristics (log output, log employment, log capital-labor ratio, share of high-skilled workers).
The dependent variables are log hourly wage of workers in columns 1 and 4, log annual income of workers in columns 2 and 5, and the
labor share of firms (wage bill divided by value added) in columns 3 and 6. Firm-level regressions in columns 3 and 6 are weighted by firm
employment. Standard errors are clustered at the firm level.
46

Table 5: Response to Export Shocks Before and After Manager Transitions in Denmark
Panel A: Non-Business to Business Manager Transitions
Value Added per Worker Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6) (7) (8)
Export Shock*Pre 0.084 0.074 0.031 0.017 0.030 0.021 0.006 -0.013
(0.042) (0.033) (0.007) (0.003) (0.009) (0.006) (0.009) (0.007)
Export Shock*Post 0.103 0.082 0.012 0.002 0.013 -0.012 -0.021 -0.028
(0.044) (0.039) (0.008) (0.008) (0.009) (0.010) (0.011) (0.010)
Industry-year FE Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Obs 1,582 6,296 544,119 1,303,209 544,117 1,303,050 1,402 5,504
Panel B: Placebo Non-Business to Non-Business Manager Transitions
Value Added per Worker Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6) (7) (8)
Export Shock*Pre 0.083 0.079 0.017 0.018 0.019 0.020 -0.012 -0.014
(0.032) (0.021) (0.003) (0.003) (0.004) (0.004) (0.009) (0.008)
Export Shock*Post 0.082 0.081 0.018 0.019 0.018 0.020 -0.010 -0.014
(0.031) (0.021) (0.003) (0.003) (0.004) (0.004) (0.009) (0.009)
Industry-year FE Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Obs 1,881 5,950 597,871 1,244,708 597,808 1,244,543 1,770 5,211
This table reports the coefficients from the regression of wages, value added per woker and the labor
share on export shocks before and after manager transitions. Pre is a dummy variable that equals
1 if the observation is before the manager transition, and Post is a dummy variable that equals 1
if the observation is after the manager transition. In Panel A, columns 1, 3, 5 include firms with
one manager transition from a non-business manager to a business manager, and columns 2, 4, 6
also include firms that always had non-business managers (for which Pre equals 1 for all years). In
Panel B, columns 1, 3, 5 include firms with one manager transition from a non-business manager to a
non-business manager, and columns 2, 4, 6 also include firms that always had non-business managers
and no manager transitions (for which Pre equals 1 for all years). In all columns we control for firm
fixed effects, initial size quintile by year fixed effects, region×year fixed effects and industry×year
fixed effects. Worker-level regressions additionally control for firm×worker fixed effects, quadratic in
experience,andunionandmaritalstatusdummies. Dependentvariablesarelogvalueaddedperworker
in columns 1 and 2, log hourly wage in columns 3 and 4, log annual income in columns 5 and 6, and the
labor share (wage bill divided by value added) in columns in columns 7 and 8. Firm-level regressions
in columns 1, 3, 7, 8 are weighted by firm employment. Standard errors are clustered at the firm level.
47

Table 6: IV Estimates of Wage Response to Export Shocks in Denmark
Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Export Shock*(1-Predicted Business Manager) 0.019 0.013 0.021 0.017 -0.002 -0.002
(0.002) (0.001) (0.004) (0.003) (0.012) (0.010)
Export Shock*Predicted Business Manager 0.001 -0.006 0.000 -0.001 -0.028 -0.019
(0.004) (0.003) (0.007) (0.004) (0.013) (0.011)
Log Output -0.004 0.011 -0.174
(0.003) (0.005) (0.016)
Log Employment 0.092 0.099 0.172
(0.006) (0.010) (0.017)
Log Capital-labor Ratio 0.002 -0.006 -0.011
(0.001) (0.001) (0.005)
Share of High-skilled Workers 0.395 0.277 0.322
(0.033) (0.058) (0.075)
Industry-year FE Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Obs 737,000 737,000 737,000 737,000 2,917 2,917
This table reports the IV estimates of the effect of business manager on the relationship between
export shocks and wages and the labor share. The predicted business manager in each column is
the predicted value from regressing whether a firm has a business manager on the lags of the share
of its peer firms in the same industry×region×size cell that have a business manager, controlling for
the same variables and fixed effects as that column. Export shocks are shocks to export demand
from destination-product combinations the firm exports to as defined in the text. In all columns we
control for firm fixed effects, initial size quintile by year fixed effects, region×year fixed effects and
industry×year fixed effects. Worker-level regressions additionally control for firm×worker fixed effects,
quadratic in experience, and union and marital status dummies. Columns 2, 4 and 6 also control for
time-varying firm characteristics (log output, log employment, log capital-labor ratio, share of high-
skilled workers). The dependent variables are log hourly wage of workers in columns 1 and 2, log
annual income of workers in columns 3 and 4, and the labor share of firms (wage bill divided by value
added) in columns 5 and 6. Standard errors are clustered at the firm level.
48

Table 7: First Stage for Role Model Effects in Business Major Choice in Denmark
Panel A:
Business Degree
(1) (2) (3) (4)
Share of Role Models with Business Degree 0.101 0.101 0.204 0.291
(0.007) (0.008) (0.062) (0.083)
School FE Y Y Y Y
Cohort FE Y Y Y Y
School-cohort FE N Y N Y
GPA Quartile FE Y Y Y Y
F statistic 187.2 141.3 10.7 12.4
Obs 505,971 505,970 13,736 13,076
Panel B:
Business Degree
(1) (2) (3) (4)
Share of Role Models with Business Degree (one year before) 0.087 0.093 0.246 0.280
(0.008) (0.009) (0.069) (0.092)
Share of Role Models with Business Degree (two years before) 0.083 0.083 0.115 0.133
(0.008) (0.009) (0.068) (0.091)
Share of Role Models with Business Degree (three years before) 0.056 0.055 0.074 0.092
(0.008) (0.009) (0.069) (0.091)
School FE Y Y Y Y
Cohort FE Y Y Y Y
School-cohort FE N Y N Y
GPA Quartile FE Y Y Y Y
Obs 469,527 469,526 11,570 10,931
This table reports the first stage for our role model effect regressions. The dependent variable is a
dummy for whether the person has a business degree. The key right hand side variable (instrument)
is the share of role models with a business degree, where role models are defined as students in the
previous cohort in the samehigh school and same GPA quartile. In Panel B, wealso look at role model
groups defined by students in the same high school and same GPA quartile but two and three cohorts
before. Columns 1 and 2 are for the sample of all students in our data set, while columns 3 and 4
are for the sample of all students who later become a manager in at least one firm in our data set.
All columns control for high school fixed effects, cohort fixed effects and GPA quartile fixed effects.
Columns 2 and 4 also control for high school×cohort fixed effects. Standard errors are clustered at the
high-school level.
49

Table 8: 2SLS Estimates of Business Major Choice on Firm and Worker Outcomes in Denmark
Becoming Residual Residual Residual
a manager log annual wage log hourly wage labor share
(1) (2) (3) (4)
Business Degree 0.087 -0.039 -0.045 -0.028
(0.043) (0.017) (0.022) (0.015)
School-cohort FE Y Y Y Y
GPA Quartile FE Y Y Y Y
F statistic 141.3 12.4 12.4 13.0
Obs 505,971 13,076 13,076 9,191
This table reports 2SLS estimates of the effect of business major choice of managers on workers annual
and hourly wages and the firm’s labor share. The first stage is provided in Table 7. Column 1 looks at
the effect of becoming a manager for the full sample of students (first stage corresponding to column
2 of Table 7) , while columns 2–4 are for the sample of managers (first stage corresponding to column
4 of Table 7). In column 2 the dependent variable is residualized log average annual wage of workers
employed under the manager. In column 3 the dependent variable is residualized log average hourly
wage of workers employed under the manager. In column 4, the dependent variable is residualized
labor share of the firm operated by the manager. These outcomes are residualized by regressing them
on industry×year fixed effects, firm fixed effects, region×year fixed effects, and initial size quintile by
year fixed effects. All columns control for high school×cohort fixed effects and GPA quartile fixed
effects. Columns 2–4 additionally control for the average propensity to become a manager within the
school-cohort-GPA quartile group. Standard errors are clustered at the high-school level. First-stage
F-statistics for the excluded instruments are reported at the bottom.
50

A Appendix (For Online Publication)
A.1 Additional Figures and Tables
Figure A1: Changes in Firm Average Wage around Non-Business to Business Manager Transitions
egaw
goL
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) US
egnahc
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Hourly Wage Annual Income
(b) Denmark
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager. Panel (a) is based on US data and the
dependent variable is log average annual income. Panel (b) is based on Danish data and the dependent
variables are log average hourly wage and log average annual income. All regressions include firm fixed
effects, industry×year fixed effects, region(state)×year fixed effects, and initial size quintile by year
fixed effects. Observations are weighted by firm employment and standard errors are clustered at the
firm level.
51

Figure A2: Changes in Firm and Worker Outcomes around Business to Non-Business Manager
Transitions in Denmark
egaw
goL
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Hourly Wage Annual Income
erahs
robaL
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Wage (b) Labor Share
egnahc
goL
51.
1.
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Output Value Added
egnahc
goL
1.
0
1.-
2.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Employment Investment
(c) Output and Value Added (d) Employment and Investment
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitionsfromabusinessmanagertoanon-businessmanagerinDenmark. Thesampleincludesfirms
that have business managers in all years, and firms that have one business to non-business manager
transition event during the sample period. All regressions control for firm fixed effects, initial size
quintile by year fixed effects, region×year fixed effects and industry×year fixed effects. Worker-level
regressions in Panel (a) additionally control for firm×worker fixed effects, quadratic in experience,
and union and marital status dummies. Firm-level regressions are weighted by employment. The
dependent variables are log hourly wage and log annual income in Panel (a), the labor share in Panel
(b), log output and log value added in Panel (c), and log employment and log investment in Panel (d).
The labor share is defined as total wage bill divided by value added. All standard errors are clustered
at the firm level.
52

Figure A3: Changes in Firm and Worker Outcomes around Non-Economics to Economics Manager
Transitions in Denmark
egaw
goL
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Hourly Wage Annual Income
erahs
robaL
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Wage (b) Labor Share
egnahc
goL
4.
2.
0
2.-
4.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Output Value Added
egnahc
goL
4.
2.
0
2.-
4.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Employment Investment
(c) Output and Value Added (d) Employment and Investment
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a manager without an economics degree to a manager with an economics degree
in Denmark. All regressions control for firm fixed effects, initial size quintile by year fixed effects,
region×year fixed effects and industry×year fixed effects. Worker-level regressions in Panel (a)
additionally control for firm×worker fixed effects, quadratic in experience, and union and marital
status dummies. Firm-level regressions are weighted by employment. The dependent variables are log
hourly wage and log annual income in Panel (a), the labor share in Panel (b), log output and log value
added in Panel (c), and log employment and log investment in Panel (d). The labor share is defined
as total wage bill divided by value added. All standard errors are clustered at the firm level.
53

Figure A4: Changes in Robot Purchases and Leverage around Non-Business to Business Manager
Transitions in Denmark
noitpodA
toboR
1.
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Robot Adoption
egareveL
60.
40.
20.
0
20.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(b) Leverage
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in Denmark. The dependent variables
are a dummy variable for robot adoption in Panel (a), and leverage (total debt divided by total assets)
in Panel (b). Robot adoption is proxied by positive imports of robots. All regressions include firm
fixedeffects, industry×yearfixedeffects, region×yearfixedeffects, andinitialsizequintilebyyearfixed
effects, and observations are weighted by employment. Standard errors are clustered at the firm level.
54

Figure A5: Changes in Organization and Occupation Structure around Non-Business to Business
Manager Transitions in Denmark
level
yhcrareih
egarevA
50.
0
50.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(a) Average Hierarchy Level
30.
20.
10.
0
10.-
20.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Average occupation wage Share of low-wage occupations
(b) Occupation Average Wage and Share of Low-skilled Occupations
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in Denmark. In Panel (a), the
dependent variable is the average hierarchy level of workers of the firm. In Panel (b), the dependent
variables are mean occupation-level average wage and the share of workers in low-wage occupations
(occupations in the lowest quartile of the wage distribution). All regressions include firm fixed effects,
industry×year fixed effects, region×year fixed effects, and initial size quintile by year fixed effects, and
observations are weighted by employment. Standard errors are clustered at the firm level.
55

FigureA6: ChangesinWagesandtheLaborSharearoundNon-BusinesstoYoungerorOlderBusiness
Manager Transitions in Denmark
egaw
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Transitions to Younger Business Managers Transitions to Older Business Managers
(a) Wage
erahs
robaL
40.
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Transitions to Younger Business Managers Transitions to Older Business Managers
(b) Labor Share
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitionsfromanon-businessmanagertoayoungerbusinessmanager(solidlines)oranolderbusiness
manager (dashed lines) in Denmark. All regressions control for firm fixed effects, initial size quintile by
year fixed effects, region×year fixed effects and industry×year fixed effects. Worker-level regressions
in Panel (a) additionally control for firm×worker fixed effects, quadratic in experience, and union and
marital status dummies. Firm-level regressions are weighted by employment. The dependent variables
are log annual income in Panel (a) and the labor share in Panel (b). The labor share is defined as total
wage bill divided by value added. All standard errors are clustered at the firm level.
56

Figure A7: Changes in Wages and the Labor Share around Non-Business to Business Manager
Transitions Excluding Family CEOs in Denmark
egaw
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Hourly Wage Annual Income
(a) Wage
erahs
robaL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
(b) Labor Share
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in Denmark. We exclude manager
transitions involving family CEOs, who are related by blood or marriage to the previous or successor
CEOs at their firms. All regressions control for firm fixed effects, initial size quintile by year fixed
effects, region×year fixed effects and industry×year fixed effects. Worker-level regressions in Panel
(a) additionally control for firm×worker fixed effects, quadratic in experience, and union and marital
status dummies. Firm-level regressions are weighted by employment. The dependent variables are log
hourly wage and log annual income in Panel (a) and the labor share in Panel (b). The labor share is
defined as total wage bill divided by value added. All standard errors are clustered at the firm level.
57

Figure A8: Heterogeneous Effects of Business Managers on Wages in the US
egaw
goL
50.
0
50.-
1.-
51.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Low Wage High Wage
This figure plots event-study estimates and 95% confidence intervals separately by different worker
groups, where events are manager transitions from a non-business manager to a business manager in
the US. The blue line plots wage effects for workers with initial wage above the median (“high wage”
workers), and the red line plots wage effects for workers with initial wage below the median (“low
wage” workers). The dependent variable is log annual wage.
58

Figure A9: Heterogeneous Effects of Business Managers on Wages in Denmark
egnahc
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Basic Education Vocational Education
College Education
(a) By Education
egnahc
goL
20.
0
20.-
40.-
60.-
80.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Low Wage High Wage
(b) By Wage Level
This figure plots event-study estimates and 95% confidence intervals separately by different worker
groups, where events are manager transitions from a non-business manager to a business manager in
Denmark. Panel(a)separatelyestimatestheevent-studyregressionsbyworkers’educationlevel(basic
education, vocational education, and college education). Panel (b) splits the workers into two groups
based on their initial wage level (“high wage” workers are workers with initial wage above the median,
and “low wage” workers are workers with initial wage below the median). The dependent variable is
log annual wage.
59

Figure A10: Changes in Wage Percentiles around Non-Business to Business Manager Transitions in
Denmark
egaw
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
median 90th percentile
95th percentile
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in Denmark. The dependent variables
are percentiles of the wage distribution (median, 90th percentile, 95th percentile) within the firm in
a given year. All regressions include firm fixed effects, industry×year fixed effects, state(region)×year
fixedeffects,andinitialsizequintilebyyearfixedeffects,andobservationsareweightedbyemployment.
Standard errors are clustered at the firm level.
60

Figure A11: Heterogeneous Effects on Wages by the Degree Level of Business Managers in Denmark
egaw
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Business BA & Professional BA Business MA
This figure plots event-study estimates and 95% confidence intervals from separate regressions for
manager transitions from a non-business manager to a business manager who has a business BA or
professional BA degree but doesn’t have a business MA degree (red line) and manager transitions from
a non-business manager to a business manager with a business MA degree (blue line) in Denmark.
The dependent variable is log annual wage. Standard errors are clustered at the firm level.
61

Figure A12: Changes in Wages and the Labor Share around Non-Business to Business Manager
Transitions for Business Managers in Different Cohorts in Denmark
egaw
goL
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Cohort Before 1980 Cohort After 1980
(a) Wage
erahs
robaL
40.
20.
0
20.-
40.-
60.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Cohort Before 1980 Cohort After 1980
(b) Labor Share
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager who gets the business degree before
1980 (solid line) or after 1980 (dashed line) in Denmark. All regressions control for firm fixed effects,
initial size quintile by year fixed effects, region×year fixed effects and industry×year fixed effects.
Worker-level regressions in Panel (a) additionally control for firm×worker fixed effects, quadratic in
experience,andunionandmaritalstatusdummies. Firm-levelregressionsareweightedbyemployment.
The dependent variables are log hourly wage and log annual income in Panel (a) and the labor share
in Panel (b). The labor share is defined as total wage bill divided by value added. All standard errors
are clustered at the firm level.
62

Figure A13: Changes in Wages around Non-Business to Business Manager Transitions for Union and
Non-Union Workers in Denmark
egaw
goL
10.
0
10.-
20.-
30.-
40.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Non-union Workers Union Workers
This figure plots event-study estimates and 95% confidence intervals separately for workers who are
union members and workers who are not union members, where events are manager transitions from a
non-business manager to a business manager in Denmark. The dependent variable is log annual wage.
Standard errors are clustered at the firm level.
63

Figure A14: Changes in Unionization Rates around Non-Business to Business Manager Transitions in
Denmark
etar
noinU
510.
10.
500.
0
500.-
10.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitionsfromanon-businessmanagertoabusinessmanagerinDenmark. Theregressioncontrolsfor
firm fixed effects, initial size quintile by year fixed effects, region×year fixed effects and industry×year
fixed effects, and observations are weighted by firm employment. The dependent variable is the share
of workers at the firm who are union members. Standard errors are clustered at the firm level.
64

Figure A15: Changes in Stock Options around Non-Business to Business Manager Transitions in
Denmark
snoitpo
kcotS
005
0
005-
0001-
0051-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in Denmark. The sample includes
firms that have non-business managers in all years, and firms that have one non-business to business
manager transition event during the sample period. All regressions control for firm fixed effects, initial
size quintile by year fixed effects, region×year fixed effects, industry×year fixed effects, firm×worker
fixed effects, quadratic in experience, and union and marital status dummies. The dependent variable
is the value of stock option payments. Standard errors are clustered at the firm level.
65

Figure A16: Changes in Quit Rates around Placebo Manager Transitions in Denmark
etar
tiuQ
1.
50.
0
50.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Thisfigureplotsevent-studyestimatesand95%confidenceintervals,whereeventsareplacebomanager
transitions from a non-business manager to a non-business manager in Denmark. The dependent
variable is the share of workers that quit the firm to join another firm or become unemployed in the
followingyear. Allregressionsincludefirmfixedeffects,industry×yearfixedeffects,state(region)×year
fixedeffects,andinitialsizequintilebyyearfixedeffects,andobservationsareweightedbyemployment.
Standard errors are clustered at the firm level.
66

Figure A17: Output and Wage Response to Leads and Lags of Trade Shocks in Denmark
3.
2.
1.
0
1.-
-2 -1 0 1 2
Year relative to export shocks
Non-Business Manager Business Manager
(a) Value Added
40.
20.
0
20.-
40.-
-2 -1 0 1 2
Year relative to export shocks
Non-Business Manager Business Manager
(b) Wage
This figure reports the coefficients and 95% confidence intervals from regressing log value added (in
Panel (a)) and log annual income (in Panel (b)) on the leads and lags of export shocks interacted with
business manager. The blue bars are coefficients for leads and lags of export shocks interacted with
business manager dummy, and red bars are coefficients for leads and lags of export shocks interacted
with non-business manager dummy. All regressions control for firm fixed effects, initial size quintile by
year fixed effects, region×year fixed effects and industry×year fixed effects. Worker-level regressions
in Panel (b) additionally control for firm×worker fixed effects, quadratic in experience, and union and
marital status dummies. In Panel (a), observations are weighted by firm employment. Standard errors
are clustered at the firm level.
67

Figure A18: Changes in Wages and the Labor Share around Non-Business to Business Manager
Transitions in High-Concentration and Low Concentration Industries in Denmark
egaw
goL
20.
0
20.-
40.-
60.-
80.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Low Cocentration High Concentration
(a) Wage
erahs
robaL
50.
0
50.-
1.-
-5 -4 -3 -2 -1 0 1 2 3 4 5
Year relative to manager turnover
Low Cocentration High Concentration
(b) Labor Share
This figure plots event-study estimates and 95% confidence intervals, where events are manager
transitions from a non-business manager to a business manager in Denmark. The dependent variables
are log annual income in Panel (a) and the labor share in Panel (b). In each panel, the solid lines use
thesampleoffirmsinlow-concentrationindustries,andthedashedlinesusethesampleoffirmsinhigh-
concentration industries. High-concentration (low-concentration) industries are industries with above-
median (or below-median) Herfindahl–Hirschman index. All regressions control for firm fixed effects,
initial size quintile by year fixed effects, region×year fixed effects and industry×year fixed effects.
Worker-level regressions in Panel (a) additionally control for firm×worker fixed effects, quadratic in
experience,andunionandmaritalstatusdummies. Firm-levelregressionsareweightedbyemployment.
The labor share is defined as total wage bill divided by value added. All standard errors are clustered
at the firm level.
68

Table A1: OLS Estimates of Business Managers on Firm Outcomes with Varying Fixed Effects in Denmark
Log Value Added Log Average Wage Labor Share
(1) (2) (3) (4) (5) (6) (7) (8) (9)
Business Manager 0.007 0.009 0.013 -0.026 -0.029 -0.033 -0.023 -0.021 -0.019
(0.022) (0.021) (0.017) (0.005) (0.005) (0.005) (0.007) (0.007) (0.006)
Year FE Y Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y Y
Industry-year FE N Y Y N Y Y N Y Y
Region-year FE N Y Y N Y Y N Y Y
Size quintile-year FE N N Y N N Y N N Y
Obs 44,731 44,731 44,731 44,731 44,731 44,731 44,962 44,962 44,962
ThistablereportstheOLSestimatesregressingfirm-levelvalueadded,averagewage,andthelaborshareonadummyforbusinessmanager
using the same sample as Table 2 in Denmark. All columns control for firm fixed effects and year fixed effects. Columns 2, 3, 5, 6, 7, and
9 additionally control for industry×year fixed effects and region×year fixed effects, and columns 3, 6, and 9 additionally control for initial
size quintile by year fixed effects. The dependent variables are log sales in columns 1–3, log average annual wage in columns 4–6, and the
labor share (wage bill divided by value added) in columns 7–9. Observations are weighted by firm employment and standard errors are
clustered at the firm level.
69

Table A2: The Effect of Business Managers on Other Firm Outcomes in Denmark
Log Log Log Avg Routine Purchase
Payout Cash Rent Liability Leverage Index Robot
(1) (2) (3) (4) (5) (6) (7)
Business Manager 0.009 -0.028 0.015 0.009 0.014 -0.005 0.024
(0.005) (0.016) (0.009) (0.002) (0.003) (0.004) (0.008)
Firm FE Y Y Y Y Y Y Y
Industry-year FE Y Y Y Y Y Y Y
Region-year FE Y Y Y Y Y Y Y
Size quintile-year FE Y Y Y Y Y Y Y
Obs 267,472 267,472 267,472 267,472 267,472 267,472 267,472
This table reports the coefficients from regressions of firm outcomes on an indicator for having a business manager for the sample of all
firms in Denmark from 1995 to 2011. All regressions control for firm fixed effects and industry×year fixed effects, region×year fixed effects,
and initial size quintile by year fixed effects. Payout is a dummy variable that equals one if the divided payment is positive. Leverage is
total debt divided by total assets. The routine index is defined as in Autor and Dorn (2013). Purchase of robots is measured using the
imports of robot as in Humlum (2019). Observations are weighted by firm employment and standard errors are clustered at the firm level.
70

Table A3: First Stage of Diffusion IV in the US
Business Manager
(1) (2) (3) (4) (5) (6) (7) (8)
Peer Firm Business Manager t-1 0.160 0.083 0.158 0.081 0.164 0.066 0.149 0.053
(0.039) (0.059) (0.039) (0.059) (0.047) (0.065) (0.047) (0.065)
Peer Firm Business Manager t-2 0.270 0.274 0.285 0.291
(0.058) (0.058) (0.065) (0.065)
Peer Firm Business Manager t-3 0.242 0.239 0.411 0.394
(0.052) (0.052) (0.059) (0.059)
Firm FE Y Y Y Y Y Y Y Y
Year FE Y Y Y Y Y Y Y Y
Size quintile-year FE Y Y Y Y Y Y
Industry*year FE Y Y Y Y
Lagged sales and wages Y Y
F statistic 16.7 30.2 16.2 29.8 12.3 43.6 9.9 41.9
This table reports the first stage estimates instrumenting business manager with up to three lags of average business manager of peer
firms (those in the same industry, region and size quartile) in the US. The first stage equation is described in equation (2). The dependent
variable is a dummy for business manager. Odd columns regress on one-year lag of the average business manager of peer firms, and even
columns include three years’ lags of the average business manager of peer firms. All columns control for firm fixed effects and year fixed
effects. We add initial size quintile by year fixed effects in columns 3 and 4, industry×year fixed effects and region×year fixed effects
in columns 5 and 6, and lags of firm value added and average wage as controls in columns 7 and 8. Observations are weighted by firm
employment and standard errors are clustered at the firm level. First-stage F-statistics for the excluded instruments are reported at the
bottom.
71

Table A4: First Stage of Diffusion IV in Denmark
Business Manager
(1) (2) (3) (4) (5) (6) (7) (8)
Peer Firm Business Manager t-1 0.115 0.098 0.166 0.095 0.277 0.226 0.324 0.326
(0.035) (0.040) (0.034) (0.040) (0.038) (0.042) (0.049) (0.052)
Peer Firm Business Manager t-2 0.258 0.255 0.331 0.141
(0.045) (0.045) (0.045) (0.054)
Peer Firm Business Manager t-3 0.225 0.219 0.216 0.361
(0.047) (0.047) (0.048) (0.057)
Firm FE Y Y Y Y Y Y Y Y
Year FE Y Y Y Y Y Y Y Y
Size quintile-year FE Y Y Y Y Y Y
Industry*year FE Y Y Y Y
Region*year FE Y Y Y Y
Lagged value added and wages Y Y
F statistic 11.0 30.6 23.5 28.9 52.8 44.4 43.8 32.9
Obs 82,805 76,516 82,805 76,516 82,805 76,516 51,246 48,649
This table reports the first stage estimates instrumenting business manager with up to three lags of average business manager of peer firms
(those in the same industry, region and size quartile) in Denmark. The first stage equation is described in equation (2). The dependent
variable is a dummy for business manager. Odd columns regress on one-year lag of the average business manager of peer firms, and even
columns include three years’ lags of the average business manager of peer firms. All columns control for firm fixed effects and year fixed
effects. We add initial size quintile by year fixed effects in columns 3 and 4, industry×year fixed effects and region×year fixed effects in
columns 5 and 6, and lags of firm sales and average wage as controls in columns 7 and 8. Observations are weighted by firm employment
and standard errors are clustered at the firm level. First-stage F-statistics for the excluded instruments are reported at the bottom.
72

Table A5: Robustness of 2SLS Estimates of Business Managers on Firm Outcomes in Denmark
Log Value Added Log Average Wage Labor Share
(1) (2) (3) (4) (5) (6) (7) (8) (9)
Business Manager 0.064 0.029 0.046 -0.040 -0.063 -0.046 -0.053 -0.066 -0.056
(0.067) (0.083) (0.075) (0.024) (0.031) (0.027) (0.027) (0.032) (0.029)
Log Average Wage t-1 -0.152 -0.156 -0.157 0.122 0.139 0.125 0.008 0.003 0.012
(0.010) (0.011) (0.010) (0.005) (0.005) (0.005) (0.005) (0.005) (0.005)
Log Average Wage t-2 -0.020 0.007 -0.025 -0.012 -0.007 -0.008 -0.011 -0.021 -0.008
(0.011) (0.013) (0.011) (0.005) (0.006) (0.006) (0.005) (0.006) (0.005)
Log Average Wage t-3 -0.067 -0.050 -0.066 -0.040 -0.034 -0.035 -0.020 -0.033 -0.019
(0.010) (0.010) (0.010) (0.005) (0.005) (0.005) (0.004) (0.005) (0.005)
Log Value Added t-1 0.436 0.468 0.434 0.007 0.006 0.006 -0.020 -0.031 -0.020
(0.005) (0.005) (0.005) (0.002) (0.003) (0.002) (0.002) (0.002) (0.002)
Log Value Added t-2 0.062 0.068 0.064 0.003 0.003 0.002 0.004 -0.001 0.004
(0.005) (0.005) (0.005) (0.003) (0.003) (0.003) (0.002) (0.002) (0.002)
Log Value Added t-3 0.015 0.004 0.016 -0.009 -0.007 -0.007 0.024 0.034 0.026
(0.004) (0.005) (0.004) (0.002) (0.002) (0.002) (0.002) (0.002) (0.002)
Size quintile-year FE Y Y Y Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y Y Y Y
Industry-year FE Y Y Y Y Y Y Y Y Y
Region-year FE Y Y Y Y Y Y Y Y Y
F statistic 32.3 28.1 25.5 31.2 27.8 24.6 31.6 28.2 24.8
Obs 44,474 44,474 43,631 44,490 44,490 43,650 44,697 44,697 43,853
This table reports 2SLS estimates of business managers on log value added, log average wage and the labor share in Denmark. The first
stage is described in equation (2) and is based on the average lagged business manager of peer firms (those in the same industry, region
and size quartile). Table A4 in the Appendix presents the first-stage estimates and Figure 7 shows them visually. In all columns we control
for firm fixed effects, initial size quintile by year fixed effects, region×year fixed effects and industry×year fixed effects, and one, two and
three-year lags of firm value added and average wage. Columns 1, 4, and 7 control for a full set of interactions between wage quintile
in 1995 and year dummies. Columns 2, 5, and 8 control for cell-specific trends (year interacted with dummies for each cell). Columns
3, 6, and 9 control for three lags of value added and wages of other firms in the same cell. The dependent variables are log value added
in columns 1–3, log average annual wage in columns 4–6, and the firm’s labor share (wage bill divided by value added) in columns 7–9.
Observations are weighted by firm employment and standard errors are clustered at the firm level. First-stage F-statistics for the excluded
instruments are reported at the bottom of Panel A.
73

Table A6: Compensation of Business Managers in the US
Panel A: Compensation Level
Log Wage of Managers
(1) (2) (3) (4)
Business Degree 0.164 0.137 0.065 0.048
(0.012) (0.012) (0.010) (0.013)
Year FE Y Y Y Y
Manager Characteristics N Y Y Y
Firm Characteristics N N Y Y
Firm FE N N N Y
Obs 37,873 36,495 36,049 35,971
Panel B: Composition of Compensation
Percent Percent Percent Percent Percent Percent
Salary Bonus Stock Options Incentive Plan Other
(1) (2) (3) (4) (5) (6)
Business Major -0.004 -0.005 -0.001 0.006 0.002 0.002
(0.003) (0.003) (0.003) (0.004) (0.002) (0.003)
Year FE Y Y Y Y Y Y
Manager Characteristics Y Y Y Y Y Y
Firm Characteristics Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y
Obs 35,971 35,971 35,971 35,971 35,971 35,971
This table reports the coefficients from regressions of compensation of CEOs from the Execucomp
dataset on an indicator for having a business degree. The sample includes all CEOs from 1992 to
2019. In Panel A, the dependent variable is log total compensation (including salary, bonus, total
value of restricted stock granted, total value of stock options granted using Black-Scholes, incentive
plan payouts, and other compensation). All columns include year fixed effects, column 2 additionally
controls for manager characteristics (gender, experience, age), column 3 additionally controls for firm
characteristics (log employment and log value added), and column 4 additionally controls for firm
fixed effects. In Panel B, the dependent variable is each form of compensation as a percentage of total
compensation, and all columns include year and firm fixed effects, manager characteristics (gender,
experience, age), firm characteristics (log employment and log value added). Standard errors are
clustered at person level.
74

Table A7: Compensation of Business Managers in Denmark
Log Wage of Managers
(1) (2) (3) (4)
Business Degree 0.451 0.142 0.105 0.084
(0.005) (0.005) (0.004) (0.005)
Year FE Y Y Y Y
Manager Characteristics N Y Y Y
Firm Characteristics N N Y Y
Firm FE N N N Y
Obs 280,389 280,012 280,012 267,850
This table reports the coefficients from regressions of log annual wage of managers on an indicator for
having a business degree. The sample includes all managers from 1995 to 2011. All columns include
year fixed effects, column 2 additionally controls for manager characteristics (gender, education level,
experience, age), column 3 additionally controls for firm characteristics (log employment and log value
added), and column 4 additionally controls for firm fixed effects. Standard errors are clustered at
person level.
Table A8: The Effect of Business Managers on Quit Rates in Denmark
All workers High-wage workers Low-wage workers
(1) (2) (3)
Business Manager 0.037 0.039 0.035
(0.021) (0.022) (0.021)
Firm FE Y Y Y
Industry-year FE Y Y Y
Region-year FE Y Y Y
Size quintile-year FE Y Y Y
Obs 44,731 44,731 44,731
This table reports the OLS estimates regressing firm-level quit rates on business manager using the
same sample as Table 2 in Denmark. All columns control for firm fixed effects, industry×year fixed
effects,region×yearfixedeffects,andinitialsizequintilebyyearfixedeffects. Thedependentvariableis
theshareofworkerswholeavethefirminthenextyear. Observationsareweightedbyfirmemployment
and standard errors are clustered at the firm level.
75

Table A9: Business Managers and Firm Output Response to Export Shocks in Denmark
Log Profit Log Value Added
Per Worker Per Worker Log Export Log Value Added Log Employment Log Investment
(1) (2) (3) (4) (5) (6)
Export Shock*Non-Business Manager 0.157 0.093 0.384 0.243 0.150 0.457
(0.086) (0.031) (0.084) (0.065) (0.030) (0.101)
Export Shock*Business Manager 0.171 0.086 0.424 0.265 0.179 0.491
(0.093) (0.040) (0.122) (0.077) (0.049) (0.142)
Industry-year FE Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y
Obs 6,686 8,285 8,285 8,285 8,285 8,173
Thistablereportsthecoefficientsfromregressionsoffirm-leveloutcomesonexportshocksandtheirinteractionswithafirm-levelindicator
for having a business manager. Export shocks are shocks to export demand from destination-product combinations the firm exports to
as defined in the text. All regressions control for firm fixed effects, initial size quintile by year fixed effects, region×year fixed effects, and
industry×year fixed effects. The dependent variables are log profits per worker in column 1, log value added per worker in column 2, log
value of exports in column 3, log value added in column 4, log employment in column 5, and log investment in column 6. Regressions are
weighted by firm employment, and standard errors are clustered at the firm level.
76

Table A10: Wage Response to Export Shocks Controlling for Product Export Shocks in Denmark
Log Hourly Wage Log Income Labor Share Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Export Shock*Non-Business Manager 0.019 0.022 -0.005 0.016 0.016 -0.003
(0.004) (0.005) (0.011) (0.004) (0.005) (0.011)
Export Shock*Business Manager 0.002 0.008 -0.025 -0.003 0.000 -0.015
(0.009) (0.008) (0.015) (0.009) (0.008) (0.014)
Log Output 0.012 0.011 -0.182
(0.004) (0.005) (0.015)
Log Employment 0.017 0.051 0.163
(0.004) (0.006) (0.016)
Log Capital-labor Ratio 0.005 0.001 -0.013
(0.002) (0.002) (0.005)
Share of High-skilled Workers 0.082 0.058 0.156
(0.025) (0.028) (0.067)
Product Export Shocks 0.010 0.016 -0.016 0.012 0.012 -0.014
(0.005) (0.005) (0.013) (0.005) (0.005) (0.010)
Industry-year FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Firm FE Y Y
Obs 1,783,859 1,783,694 5,157 1,783,859 1,783,694 5,157
This table reports the coefficients from regressions of wages and the labor share on export shocks and their interactions with a firm-level
indicator for having a business manager. All regressions control for product demand shocks at the firm level, constructed as the weighted
average of total imports (excluding imports from Denmark) at six-digit product level, with the weights being the ex-ante shares of sales in
eachsix-digitproduct. Inallcolumnswecontrolforfirmfixedeffects, initialsizequintilebyyearfixedeffects, region×yearfixedeffectsand
industry×year fixed effects. Worker-level regressions additionally control for firm×worker fixed effects, quadratic in experience, and union
and marital status dummies. Columns 3–6 also control for time-varying firm characteristics (log output, log employment, log capital-labor
ratio, share of high-skilled workers). The dependent variables are log hourly wage of workers in columns 1 and 4, log annual income of
workers in columns 2 and 5, and the labor share of firms (wage bill divided by value added) in columns 3 and 6. Firm-level regressions in
columns 3 and 6 are weighted by firm employment. Standard errors are clustered at the firm level.
77

Table A11: Wage Response to Export Shocks Using a Balanced Panel of Firms in Denmark
Log Hourly Wage Log Income Labor Share Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Export Shock*Non-Business Manager 0.020 0.033 -0.012 0.014 0.024 -0.008
(0.004) (0.005) (0.012) (0.004) (0.004) (0.011)
Export Shock*Business Manager 0.006 0.013 -0.024 0.002 0.001 -0.019
(0.007) (0.008) (0.013) (0.007) (0.007) (0.012)
Log Output 0.013 0.009 -0.148
(0.004) (0.004) (0.014)
Log Employment 0.019 0.047 0.168
(0.005) (0.005) (0.015)
Log Capital-labor Ratio 0.002 -0.001 -0.020
(0.001) (0.001) (0.005)
Share of High-skilled Workers 0.085 0.111 0.216
(0.024) (0.029) (0.072)
Industry-year FE Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Obs 1,082,559 1,082,553 3,156 1,082,559 1,082,553 3,156
This table reports the coefficients from regressions of wages and the labor share on export shocks and their interactions with a firm-level
indicator for having a business manager. The sample is a balanced sample of firms between 1995 and 2006 (i.e. firms that exit in every
single year of that period). In all columns we control for firm fixed effects, initial size quintile by year fixed effects, region×year fixed
effects and industry×year fixed effects. Worker-level regressions additionally control for firm×worker fixed effects, quadratic in experience,
and union and marital status dummies. Columns 3–6 also control for time-varying firm characteristics (log output, log employment, log
capital-labor ratio, share of high-skilled workers). The dependent variables are log hourly wage of workers in columns 1 and 4, log annual
income of workers in columns 2 and 5, and the labor share of firms (wage bill divided by value added) in columns 3 and 6. Firm-level
regressions in columns 3 and 6 are weighted by firm employment. Standard errors are clustered at the firm level.
78

Table A12: College-Degree Managers and Wage Response to Trade Shocks in Denmark
Log Hourly Wage Log Income Labor Share Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Export Shock*Non-College Non-Business Manager 0.016 0.030 -0.016 0.014 0.025 -0.000
(0.005) (0.005) (0.012) (0.005) (0.005) (0.011)
Export Shock*College Non-Business Manager 0.017 0.016 -0.011 0.014 0.010 -0.004
(0.003) (0.005) (0.013) (0.003) (0.004) (0.012)
Export Shock*Business Manager 0.001 0.009 -0.025 -0.004 -0.001 -0.018
(0.007) (0.007) (0.015) (0.007) (0.006) (0.013)
Log Output 0.012 0.013 -0.163
(0.003) (0.005) (0.012)
Log Employment 0.013 0.045 0.165
(0.004) (0.005) (0.012)
Log Capital-labor Ratio 0.003 0.000 -0.010
(0.001) (0.001) (0.004)
Share of High-skilled Workers 0.076 0.075 0.208
(0.021) (0.026) (0.057)
Industry-year FE Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Obs 1,783,859 1,783,694 5,157 1,783,859 1,783,694 5,157
This table reports the coefficients from regressions of wages and the labor share on export shocks and their interactions with whether the
manager has no college degree, has a college degree but no business degree, or has a business degree. Export shocks are shocks to export
demand from destination-product combinations the firm exports to as defined in the text. In all columns we control for firm fixed effects,
initial size quintile by year fixed effects, region×year fixed effects and industry×year fixed effects. Worker-level regressions additionally
control for firm×worker fixed effects, quadratic in experience, and union and marital status dummies. Columns 3–6 also control for time-
varying firm characteristics (log output, log employment, log capital-labor ratio, share of high-skilled workers). The dependent variables
are log hourly wage of workers in columns 1 and 4, log annual income of workers in columns 2 and 5, and the labor share of firms (wage
bill divided by value added) in columns 3 and 6. Firm-level regressions in columns 3 and 6 are weighted by firm employment. Standard
errors are clustered at the firm level.
79

Table A13: Wage Response to Export Shocks for Union and Non-Union Workers in Denmark
Union Non-Union
Log Hourly Wage Log Income Log Hourly Wage Log Income
(1) (2) (3) (4)
Export Shock*Non-Business Manager 0.018 0.024 0.010 0.016
(0.003) (0.005) (0.004) (0.007)
Export Shock*Business Manager 0.001 0.009 0.002 -0.001
(0.007) (0.007) (0.008) (0.010)
Industry-year FE Y Y Y Y
Worker-firm FE Y Y Y Y
Obs 1,555,089 1,554,942 197,545 197,528
Thistablereportsthecoefficientsfromregressionsofwagesonexportshocksandtheirinteractionswith
a firm-level indicator for having a business manager. Columns 1 and 2 only include union workers, and
columns 3 and 4 include only non-union workers. In all columns we control for firm fixed effects, initial
size quintile by year fixed effects, region×year fixed effects, industry×year fixed effects, firm×worker
fixed effects, quadratic in experience, and union and marital status dummies. The dependent variables
are log hourly wage in columns 1 and 3, and log annual income in columns 2 and 4. Standard errors
are clustered at the firm level.
80

Table A14: Effects of Trade Shocks on Firm Exit in Denmark
Exit - 1 year Exit - 3 years
(1) (2) (3) (4) (5) (6)
Export Shock*Non-Business Manager -0.003 0.026
(0.021) (0.023)
Export Shock*Business Manager -0.045 -0.028
(0.028) (0.029)
Intermediate Import Shock*Non-Business Manager 0.014 0.001
(0.012) (0.017)
Intermediate Import Shock*Business Manager 0.008 0.001
(0.020) (0.024)
Chinese Import Shock*Non-Business Manager 0.000 0.033
(0.011) (0.016)
Chinese Import Shock*Business Manager 0.006 0.035
(0.010) (0.020)
Industry-year FE Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y
Obs 8,286 8,286 6,380 8,286 8,286 6,380
This table reports the coefficients from regressions of firm exit on trade shocks (export shocks, intermediate import shocks, and Chinese
import shocks) and their interactions with a firm-level indicator for having a business manager. All regressions control for firm fixed
effects, initial size quintile by year fixed effects, region×year fixed effects and industry×year fixed effects. The dependent variable is an
indicator variable for firm exit in next year in columns 1–3, and an indicator variable for firm exit in the next 3 years in columns 4–6.
Regressions are weighted by firm employment, and standard errors are clustered at the firm level.
81

Table A15: Business Managers and Firm Response to Intermediate Import Shocks in Denmark
Log Profit Log Value Added Log Intermediate
Per Worker Per Worker Imports Log Value Added Log Employment Log Investment
(1) (2) (3) (4) (5) (6)
Intermediate Import Shock*Non-Business Manager 0.101 0.043 0.309 0.136 0.093 0.152
(0.067) (0.026) (0.102) (0.045) (0.024) (0.094)
Intermediate Import Shock*Business Manager 0.115 0.049 0.370 0.137 0.088 0.126
(0.070) (0.033) (0.146) (0.064) (0.042) (0.142)
Industry-year FE Y Y Y Y Y Y
Firm FE Y Y Y Y Y Y
Obs 6,686 8,285 8,072 8,285 8,285 8,173
This table reports the coefficients from regressions of firm-level outcomes on intermediate import shocks and their interactions with a
firm-level indicator for having a business manager. Intermediate import shocks are shocks to intermediate imports supply from origin
country-product combinations the firm imports from as defined in the text. All regressions control for firm fixed effects, initial size quintile
by year fixed effects, region×year fixed effects and industry×year fixed effects. The dependent variables are log profits per worker in
column 1, log value added per worker in column 2, log value of exports in column 3, log value added in column 4, log employment in
column 5, and log investment in column 6. Regressions are weighted by firm employment, and standard errors are clustered at the firm
level.
82

Table A16: Business Managers and Wage Response to Intermediate Import Shocks in Denmark
Log Hourly Wage Log Income Labor Share Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Intermediate Import Shock*Non-Business Manager 0.012 0.011 -0.005 0.009 0.005 -0.000
(0.003) (0.003) (0.009) (0.003) (0.003) (0.008)
Intermediate Import Shock*Business Manager -0.000 0.007 -0.016 -0.004 0.001 -0.012
(0.005) (0.005) (0.014) (0.005) (0.005) (0.014)
Log Output 0.013 0.013 -0.163
(0.003) (0.005) (0.011)
Log Employment 0.014 0.045 0.164
(0.004) (0.005) (0.012)
Log Capital-labor Ratio 0.003 0.000 -0.010
(0.001) (0.001) (0.004)
Share of High-skilled Workers 0.088 0.076 0.224
(0.020) (0.025) (0.056)
Industry-year FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Firm FE Y Y
Obs 1,783,859 1,783,694 5,157 1,783,859 1,783,694 5,157
This table reports the coefficients from regressions of wages and the labor share on intermediate import shocks and their interactions with
a firm-level indicator for having a business manager. Intermediate import shocks are shocks to intermediate imports supply from origin
country-product combinations the firm imports from as defined in the text. In all columns we control for firm fixed effects, initial size
quintile by year fixed effects, region×year fixed effects and industry×year fixed effects. Worker-level regressions additionally control for
firm×worker fixed effects, quadratic in experience, and union and marital status dummies. Columns 3–6 also control for time-varying firm
characteristics (log output, log employment, log capital-labor ratio, share of high-skilled workers). The dependent variables are log hourly
wage of workers in columns 1 and 4, log annual income of workers in columns 2 and 5, and the labor share of firms (wage bill divided
by value added) in columns 3 and 6. Firm-level regressions in columns 3 and 6 are weighted by firm employment. Standard errors are
clustered at the firm level.
83

Table A17: Response to Positive and Negative Intermediate Import Shocks in Denmark
Log Hourly Wage Log Income Labor Share Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Pos Intermediate Import Shock*Non-Business Manager 0.025 0.017 0.007 0.023 0.011 0.009
(0.005) (0.004) (0.013) (0.005) (0.005) (0.012)
Pos Intermediate Import Shock*Business Manager -0.002 0.009 -0.015 0.006 0.002 -0.014
(0.010) (0.005) (0.014) (0.010) (0.006) (0.013)
Neg Intermediate Import Shock*Non-Business Manager -0.004 0.006 -0.004 0.007 0.008 -0.010
(0.005) (0.005) (0.012) (0.005) (0.005) (0.011)
Neg Intermediate Import Shock*Business Manager 0.002 0.010 -0.002 0.011 0.008 -0.011
(0.008) (0.006) (0.012) (0.009) (0.006) (0.015)
Log Output 0.012 0.013 -0.164
(0.003) (0.005) (0.011)
Log Employment 0.013 0.044 0.165
(0.004) (0.005) (0.012)
Log Capital-labor Ratio 0.003 0.000 -0.010
(0.001) (0.001) (0.004)
Share of High-skilled Workers 0.079 0.072 0.228
(0.020) (0.028) (0.056)
Industry-year FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Firm FE Y Y
Obs 1,783,859 1,783,694 5,157 1,783,859 1,783,694 5,157
This table reports the coefficients from regressions of wages and the labor share on positive and negative intermediate import shocks
and their interactions with a firm-level indicator for having a business manager. Positive and negative intermediate import shocks are
defined in the text. In all columns we control for firm fixed effects, initial size quintile by year fixed effects, region×year fixed effects and
industry×year fixed effects. Worker-level regressions additionally control for firm×worker fixed effects, quadratic in experience, and union
and marital status dummies. Columns 3–6 also control for time-varying firm characteristics (log output, log employment, log capital-labor
ratio, share of high-skilled workers). The dependent variables are log hourly wage of workers in columns 1 and 4, log annual income of
workers in columns 2 and 5, and the labor share of firms (wage bill divided by value added) in columns 3 and 6. Firm-level regressions in
columns 3 and 6 are weighted by firm employment. Standard errors are clustered at the firm level.
84

Table A18: Response to Intermediate Import Shocks Before and After Non-Business to Business
Manager Turnovers in Denmark
Panel A: Non-Business to Business Manager Transitions
ValueAddedperWorker LogHourlyWage LogIncome LaborShare
(1) (2) (3) (4) (5) (6) (7) (8)
IntermediateImportShock*Pre 0.034 0.021 0.018 0.016 0.026 0.023 -0.005 -0.006
(0.037) (0.034) (0.010) (0.003) (0.011) (0.004) (0.010) (0.008)
IntermediateImportShock*Post 0.061 0.026 -0.001 -0.004 -0.007 -0.016 -0.015 -0.017
(0.039) (0.038) (0.005) (0.006) (0.005) (0.008) (0.012) (0.0011)
Industry-yearFE Y Y Y Y Y Y Y Y
FirmFE Y Y Y Y Y Y Y Y
Worker-firmFE Y Y Y Y
Obs 1,582 6,296 544,119 1,303,209 544,117 1,303,050 1,402 5,504
Panel B: Placebo Non-Business to Non-Business Manager Transitions
ValueAddedperWorker LogHourlyWage LogIncome LaborShare
(1) (2) (3) (4) (5) (6) (7) (8)
IntermediateImportShock*Pre 0.054 0.019 0.013 0.016 0.011 0.016 -0.006 -0.006
(0.041) (0.022) (0.004) (0.003) (0.004) (0.004) (0.014) (0.009)
IntermediateImportShock*Post 0.052 0.018 0.013 0.015 0.014 0.017 -0.004 -0.006
(0.041) (0.022) (0.004) (0.003) (0.004) (0.003) (0.013) (0.009)
Industry-yearFE Y Y Y Y Y Y Y Y
FirmFE Y Y Y Y Y Y Y Y
Worker-firmFE Y Y Y Y
Obs 1,881 5,950 597,871 1,244,708 597,808 1,244,543 1,770 5,211
This table reports the coefficients from the regression of wages, value added per woker and the labor
share on intermediate import shocks before and after manager transitions. Pre is a dummy variable
that equals 1 if the observation is before the manager transition, and Post is a dummy variable that
equals 1 if the observation is after the manager transition. In Panel A, columns 1, 3, 5 include firms
with one manager transition from a non-business manager to a business manager, and columns 2, 4,
6 also include firms that always had non-business managers (for which Pre equals 1 for all years). In
Panel B, columns 1, 3, 5 include firms with one manager transition from a non-business manager to a
non-business manager, and columns 2, 4, 6 also include firms that always had non-business managers
and no manager transitions (for which Pre equals 1 for all years). In all columns we control for firm
fixed effects, initial size quintile by year fixed effects, region×year fixed effects and industry×year
fixed effects. Worker-level regressions additionally control for firm×worker fixed effects, quadratic in
experience,andunionandmaritalstatusdummies. Dependentvariablesarelogvalueaddedperworker
in columns 1 and 2, log hourly wage in columns 3 and 4, log annual income in columns 5 and 6, and the
labor share (wage bill divided by value added) in columns in columns 7 and 8. Firm-level regressions
in columns 1, 3, 7, 8 are weighted by firm employment. Standard errors are clustered at the firm level.
85

Table A19: IV Estimates of Response to Intermediate Import Shocks in Denmark
Log Hourly Wage Log Income Labor Share
(1) (2) (3) (4) (5) (6)
Log Intermediate Shock*(1-Predicted Business Manager) 0.010 0.011 0.007 0.008 -0.014 -0.007
(0.002) (0.001) (0.003) (0.002) (0.011) (0.010)
Log Intermediate Shock*Predicted Business Manager -0.001 0.002 -0.005 -0.003 -0.026 -0.019
(0.004) (0.002) (0.007) (0.004) (0.011) (0.012)
Log Output 0.047 0.066 -0.176
(0.003) (0.005) (0.016)
Log Employment -0.021 -0.022 0.173
(0.005) (0.009) (0.017)
Log Capital-labor Ratio 0.001 -0.007 -0.011
(0.001) (0.001) (0.005)
Share of High-skilled Workers -0.251 -0.418 0.328
(0.031) (0.054) (0.075)
Industry-year FE Y Y Y Y Y Y
Worker-firm FE Y Y Y Y
Firm FE Y Y Y Y Y Y
Obs 737,000 737,000 737,000 737,000 2,917 2,917
This table reports the IV estimates of the effect of business manager on the relationship between
intermediate import shocks and wages and the labor share. The predicted business manager in each
column is the predicted value from regressing whether a firm has a business manager on the lags
of the share of its peer firms in the same industry×region×size cell that have a business manager,
controlling for the same variables and fixed effects as that column. Intermediate import shocks are
shockstointermediateimportssupplyfromorigincountry-productcombinationsthefirmimportsfrom
as defined in the text. In all columns we control for firm fixed effects, initial size quintile by year fixed
effects, region×year fixed effects and industry×year fixed effects. Worker-level regressions additionally
control for firm×worker fixed effects, quadratic in experience, and union and marital status dummies.
Columns 2, 4 and 6 also control for time-varying firm characteristics (log output, log employment,
log capital-labor ratio, share of high-skilled workers). The dependent variables are log hourly wage of
workers in columns 1 and 2, log annual income of workers in columns 3 and 4, and the labor share of
firms (wage bill divided by value added) in columns 5 and 6. Standard errors are clustered at the firm
level.
86

Table A20: 2SLS Estimates of Business Major Choice on Firm Outcomes Without Controlling for
Probability of Becoming a Manager in Denmark
Residual Residual Residual
log annual wage log hourly wage labor share
(1) (2) (3)
Business Degree -0.038 -0.046 -0.027
(0.017) (0.023) (0.015)
School-cohort FE Y Y Y
GPA Quartile FE Y Y Y
F statistic 12.1 12.1 12.8
Obs 13,076 13,076 9,191
This table reports 2SLS estimates of the effect of business major choice of managers on workers annual
and hourly wages and the firm’s labor share. The first stage is provided in Table 7. Column 1 looks at
the effect of becoming a manager for the full sample of students (first stage corresponding to column
2 of Table 7) , while columns 2–4 are for the sample of managers (first stage corresponding to column
4 of Table 7). In column 2 the dependent variable is residualized log average annual wage of workers
employed under the manager. In column 3 the dependent variable is residualized log average hourly
wage of workers employed under the manager. In column 4, the dependent variable is residualized
labor share of the firm operated by the manager. These outcomes are residualized by regressing them
on industry×year fixed effects, firm fixed effects, region×year fixed effects, and initial size quintile by
year fixed effects. All columns control for high school×cohort fixed effects and GPA quartile fixed
effects. Standard errors are clustered at the high-school level. First-stage F-statistics for the excluded
instruments are reported at the bottom.
87

Table A21: 2SLS Estimates of Business Major Choice on Firm Performance Measures in Denmark
Residual Residual Residual Residual
log employment log sales log value added log investment
(1) (2) (3) (4)
Business Degree 0.061 -0.064 -0.029 -0.044
(0.104) (0.161) (0.144) (0.182)
School-cohort FE Y Y Y Y
GPA Quartile FE Y Y Y Y
F statistic 12.4 13.0 13.0 13.0
Obs 13,076 9,191 9,191 9,191
This table reports 2SLS estimates of the effect of business major choice of managers on workers annual
andhourlywagesandthefirm’slaborshare. ThefirststageisprovidedinTable7. Thesampleincludes
allstudentswholaterbecomeamanagerinatleastonefirminourdataset(firststagecorrespondingto
column 4 of Table 7). In column 1 the dependent variable is residualized log employment of the firm(s)
operated by the manager. In column 2 the dependent variable is residualized log sales of the firm(s)
operated by the manager. In column 3 the dependent variable is residualized log value added of the
firm(s) operated by the manager. In column 4 the dependent variable is residualized log investment
of the firm(s) operated by the manager. These outcomes are residualized by regressing them on
industry×year fixed effects, firm fixed effects, region×year fixed effects, and initial size quintile by year
fixedeffects. Allcolumnscontrolforhighschool×cohortfixedeffects,GPAquartilefixedeffects,aswell
astheaveragepropensitytobecomeamanagerwithintheschool-cohort-GPAquartilegroup. Standard
errors are clustered at the high-school level. First-stage F-statistics for the excluded instruments are
reported at the bottom.
88

Table A22: 2SLS Estimates of Business Major Choice on Firm and Worker Outcomes with School and
Cohort Fixed Effects in Denmark
Becoming Residual Residual Residual
a manager log annual wage log hourly wage labor share
(1) (2) (3) (4)
Business Degree 0.064 -0.035 -0.039 -0.022
(0.037) (0.021) (0.028) (0.017)
School FE Y Y Y Y
Cohort FE Y Y Y Y
GPA Quartile FE Y Y Y Y
F statistic 187.2 10.7 10.7 10.9
Obs 505,971 13,076 13,076 9,191
This table reports 2SLS estimates of the effect of business major choice of managers on workers annual
and hourly wages and the firm’s labor share. The first stage is provided in Table 7. Column 1 looks at
the effect of becoming a manager for the full sample of students (first stage corresponding to column
2 of Table 7) , while columns 2–4 are for the sample of managers (first stage corresponding to column
4 of Table 7). In column 2 the dependent variable is residualized log average annual wage of workers
employed under the manager. In column 3 the dependent variable is residualized log average hourly
wage of workers employed under the manager. In column 4, the dependent variable is residualized
labor share of the firm operated by the manager. These outcomes are residualized by regressing them
on industry×year fixed effects, firm fixed effects, region×year fixed effects, and initial size quintile
by year fixed effects. All columns control for high school fixed effects, cohort fixed effects, and GPA
quartilefixedeffects. Columns2–4additionallycontrolfortheaveragepropensitytobecomeamanager
within the school-cohort-GPA quartile group. Standard errors are clustered at the high-school level.
First-stage F-statistics for the excluded instruments are reported at the bottom.
89

Table A23: First Stage and Reduced Form Estimates of Business Major Choice Based on Placebo Role
Models in Denmark
Panel A: Placebo peers in same high school and different GPA quartile
Becoming Residual Residual Residual
Businessdegree amanager logannualwage loghourlywage laborshare
(1) (2) (3) (4) (5) (6)
ShareofBusinessDegreesinSameHighSchool 0.010 -0.052 -0.010 0.006 0.032 0.010
andDifferentGPAQuartiles (0.012) (0.108) (0.006) (0.039) (0.044) (0.044)
SchoolFE Y Y Y Y Y Y
CohortFE Y Y Y Y Y Y
GPAQuartileFE Y Y Y Y Y Y
Obs 505,963 13,076 505,963 13,076 13,076 9,191
Panel B: Placebo peers in different high school and same GPA quartile
Becoming Residual Residual Residual
Businessdegree amanager logannualwage loghourlywage laborshare
(1) (2) (3) (4) (5) (6)
ShareofBusinessDegreesinSameGPAQuartile 0.046 0.042 0.027 -0.029 -0.055 0.011
andDifferentHighSchools (0.036) (0.332) (0.019) (0.121) (0.136) (0.137)
SchoolFE Y Y Y Y Y Y
CohortFE Y Y Y Y Y Y
GPAQuartileFE Y Y Y Y Y Y
Obs 505,970 13,076 505,970 13,076 13,076 9,191
Panel C: Placebo peers in same high school, GPA quartile, but more than three cohorts
ahead
Becoming Residual Residual Residual
Businessdegree amanager logannualwage loghourlywage laborshare
(1) (2) (3) (4) (5) (6)
ShareofBusinessDegreesinSameHighSchool, 0.018 0.051 0.007 0.005 -0.014 0.019
GPAQuartile,andThreeCohortsAhead (0.008) (0.059) (0.005) (0.021) (0.024) (0.024)
SchoolFE Y Y Y Y Y Y
CohortFE Y Y Y Y Y Y
GPAQuartileFE Y Y Y Y Y Y
Obs 504,138 13,076 504,138 13,076 13,076 9,191
This table reports the placebo first stage and reduced form of the role model IV. The dependent
variable is whether a person has a business degree in columns 1 and 2, whether a person becomes a
manager in column 3, residualized log average annual wage of workers employed under the manager
in column 4, residualized log average hourly wage of workers employed under the manager in column
5, and residualized labor share of the firm operated by the manager in column 6. These outcomes
are residualized by regressing them on industry×year fixed effects, firm fixed effects, region×year fixed
effects, and initial size quintile by year fixed effects. Columns 3–6 include only individuals who end
up becoming a manager in at least one firm during our sample period. In Panel A, the independent
variable is the share of students in the same school, previous cohort, but different GPA quartile who
have business degrees. In Panel B, the independent variable is the share of students in the previous
cohort, same GPA quartile, but a different high school who have business degrees. In Panel C, the
independent variable is the share of students in the same high school and same GPA quartile, but more
than three cohorts ahead who have business degrees. All columns control for high school fixed effects,
cohort fixed effects, and GPA quartile fixed effects. Columns 4–6 additionally control for the average
propensity to become a manager within the school-cohort-GPA quartile group. Standard errors are
clustered at the high-school level.
90
