---
id: pdf-c9b8f466ea39
type: pdf
title: akash-position
url: ''
authors: []
ingested_at: '2026-04-29T16:11:26Z'
content_hash: sha256:3807cfda181eaed4c345f4d2106e7b1bbc5e74f2d61041b6aa217850cf1d357d
source_path: raw/pdf/pdf-c9b8f466ea39.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 15
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/akash-position.pdf
published_at: '2018'
---
Akash Network: Decentralized Cloud
Infrastructure Marketplace
Overclock Labs
May 13, 2018
Version 0.0.3
Note: The Akash Network is an active research project and new versions of this
paper will manifest at akash.network. For comments and suggestions please reach
out at research@akash.network
Abstract
Cloudcomputing—theprocessofoffloadingworktoremoteservers
– is inherently broken. While it mostly works as advertised, we’ve
found that inefficiencies still plague the system. The products pro-
duced by the major cloud providers are usable but they are limited
to shortcomings that can be solved today with advancements in con-
tainer technology and a powerful token economy. The purpose of this
white paper is to put forward our plan for a cloud services market
called Akash Network, the worlds first global spot market for cloud
computing.
We see a future where the global cloud infrastructure of the world
is decentralized and distributed between all cloud service providers; a
market that deploys and liquidates (increasingly commoditized) data
centercomputeinasecure,fastandtransparentlyspotpricedmanner.
Services are sold in a democratic but unified ecosystem that anyone
can use.
In this paper, we presentAkash, cloud infrastructure network that
is decentralized, competitive, and able to distribute applications be-
tween multiple cloud service providers around the globe. The paper
will introduce the state of the existing market, outline how we are
usinglatestdevelopmentsinserverlesscontainerorchestrationtocom-
bat these issues,the basics of and the necessity of the networksnative
token, AKASH, and finally our roadmap for launch.
1

Contents
1 Introduction 4
1.1 A Troubled Industry . . . . . . . . . . . . . . . . . . . . 4
2 The Akash Network 6
2.1 The Akash Blockchain . . . . . . . . . . . . . . . . . . . 6
2.2 The Akash Token, AKASH . . . . . . . . . . . . . . . . 7
3 Marketplace 8
4 Deployment 10
4.1 Manifest Distribution . . . . . . . . . . . . . . . . . . . 10
4.2 Overlay Network . . . . . . . . . . . . . . . . . . . . . . 10
5 Automation 11
5.1 Example: Latency-Optimized Deployment . . . . . . . . 12
5.2 Example: Machine Learning Deployment. . . . . . . . . 13
2

List of Figures
1 Illustrationofon-chainandoff-chaininteractionsamongst
various participants in the Akash network . . . . . . . . 7
2 Summary of procurement from Marketplace. (1) User’s
deployment order is posted to the orderbook (2) Dat-
acenters posts eligible fulfillment orders for the deploy-
ment order (3) The best fulfillment order is matched
with the deployment order, creating a new lease. . . . . 9
3 Illustration of Akash’s overlaynetwork . . . . . . . . . . 11
4 Illustration of slower performance due to higher laten-
ciesforend-usersdistributedacrosstheglobeforasingle
datacenter deployment . . . . . . . . . . . . . . . . . . . 12
5 Illustration of improved network performance by dy-
namically distributing workloads and their state across
datacenters in close proximity to the end-users . . . . . 13
6 A machine learning batchjob under less loadrunning a
single master and single worker node . . . . . . . . . . . 14
7 A machine learningbatch jobunder loadrunning a sin-
gle master and multiple worker nodes . . . . . . . . . . 14
3

1 Introduction
TheAkashNetwork(Akash)isasecure,transparent,anddecentralized
cloudcomputingmarketplacethatconnectsthosewhoneedcomputing
resources (clients) with those that have computing capacity to lease
(providers).
Akash acts as a "super" cloud platform (supercloud) - providing a
unified layer above all providers on the marketplace so as to present
clients with a single cloud platform, regardless of which particular
provider they may be using.
ClientsuseAkashbecauseofitscostadvantage,usability, andflex-
ibility to move between cloud providers,and the performance benefits
of global deployments. Providers use Akash because it allows them to
earn profits from either dedicated or temporarily-unused capacity.
1.1 A Troubled Industry
By2020,cloudinfrastructureproviderswill accountfor 53%ofglobal
internet traffic[Cisco(2016)], out of which Amazon, Google, and Mi-
crosoft will deliver 80% of the payload[Forrester(2017)].
While the cloud will deliver the majority of the workloads, the
futureoftheinternetstandsatariskofbeingconsolidated,centralized,
and at the mercy of these three providers.
The primary driver for cloud adoption is the promise of flexibility
andcostadvantage,buttherealityisthattheproductsofferedbycloud
providersareoverpriced,complicated,andlockclientsintoecosystems
thatlimittheirabilitytoinnovate,compete,andhavesovereigntyover
their infrastructure needs.
The difference in capital expenditure of purchasing hardware and
leasing datacenters between running in the cloud and self managing
(on-premise) is marginal; however, the cloud providers have a signif-
icant advantage with operating expenditure because of their invest-
ments in automation with minimal human touch.
Even though running computing on-premise can offer much bet-
terflexibility,performance,andsecurity,organizationsareabandoning
their datacenter operations and migrating to the cloud because they
arefindingitincreasinglyhardtojustifytheoperatingcostsduetolack
of adequate automation along with low utilization footprint. Idle, un-
derutilized servers prove to be costly and wasteful. Analysts estimate
thatasmany as85%ofserversin practicehaveunderutilized capacity
[Glanz(2012)][Kaplan et al.(2008)Kaplan,Forrest, and Kindler][Liu(2011)]
[Koomey and Taylor(2015)].
Cloudprovidersdrivemarginsbybuildinghyper-scaleinstallations,
i.e, consolidating resources in few datacenters for economic efficiency,
4

and cross-selling fully managed backend services, such as databases,
cache stores, API gateways,etc.
Being hyper-scale allows them to oversubscribe their customers,
hencedrivinghighermarginsbutcreatessingle-pointsforfailures. Ge-
ographically distributed workloads offer much reliability and end-user
performance; however,the cloud providers make it extremely hard for
clients to be multi-regionalbecause it doesn’t workin their best inter-
est.
The cloud providers prefer customers to deploy their applications
in a single datacenter and penalize them for being cross-regional or
multi-zonal,usuallythroughheftybandwidthfeesandvariableregional
pricing. This is why AWS’ pricing model is different for each region
for the same exact resource.
Even though selling instances is lucrative, Cloud Providersusually
charge a small amount for instances compared to the premium they
charge for managed backend services (PaaS); analogous to the old
burgers-and-fries model where a restaurant needs to sell burgers at a
loss so that they can sell the more addictive fries at a high margin.
The PaaS services sold by the providers tend to be white-labeled
opensourceprojectswheretheoriginalauthorsareneverincentivized,
and the cloud providers have no incentive to evolve the product. For
example, AWS’ ElastiCache is a white-labeled open source software
called Redis. Redis is an open source project — much loved by de-
velopers — written by Salvatore Sanfilippo and maintained by Redis
Labs.
Asofthewritingofthispaper,amanagedRedisserver,inUSEast
(Ohio)running onr3.8xlarge is priced at$31,449/yr[Amazon(2017a)]
whereasthesameinstancewithoutRediscosts$18,385/yr[Amazon(2017b)].
The extra $13,064just for a "piece of mind" to the customer. Neither
Sanfilippo or Redis Labs are incentivized for the efforts.
Also, more services mean more dependent the customer is on the
cloud provider. The complexity introduced by increasing amounts of
features,serviceavailability,andcodificationusingnon-standardAPIs
lead to customers being locked in by the cloud vendors, preventing
clients from exploring other better options in the marketplace while
inhibiting innovation.
Thismodeladoptedbytheprovidersstiflesinnovationasitdramat-
ically reduces the chance of an open source project from succeeding.
Cloud providers effectively act as middle-men that set the rules of en-
gagement for the industry while making a no contribution to society
on the whole.
5

2 The Akash Network
ThefoundationaldesignobjectiveoftheAkashNetworkistomaintain
alowbarriertoentryforproviderswhileatthesametimeensuringthat
clientscantrusttheresourcesthattheplatformoffersthem. Toachieve
this, the system requires a publicly-verifiable record of transactions
within the network. To that end, the Akash Network is implemented
usingblockchaintechnologiesasameansofachievingconsensusonthe
veracity of a distributed database.
Akash is, first and foremost, a platform that allows clients to pro-
cureresourcesfromproviders. Thisisenabledbyablockchain-powered
distributed exchange where clients post their desired resources for
providers to bid on. The currency of this marketplace is a digital
token, the Akash (AKASH), whose ledger is stored on a blockchain.
Akash is a cloud platformfor real-worldapplications. The require-
ments of such applications include:
• Many workloads deployed across any number of datacenters.
• Connectivityrestrictionswhichpreventunwantedaccesstowork-
loads.
• Self-managed so that operators do not need to constantly tend
to deployments.
To support running workloads on procured resources, Akash in-
cludes a peer-to-peer protocol for distributing workloads and deploy-
ment configuration to and between a client’s providers.
Workloadsin Akash are defined as Docker containers. Docker con-
tainers allow for highly-isolated and configurable execution environ-
ments, and are already part of many cloud-based deployments today.
2.1 The Akash Blockchain
The Akash blockchain provides a layer of trust in a decentralized and
trustless environment. Clients inherently trust today’s large infras-
tructure Providers based primarily on the brand equity they’ve built
over years.Akash does not and should not require that same leap of
faith, since any Provider with capacity can compete to offer services
on Akash. Instead, the blockchain earns trust via an open and trans-
parentplatform. Dataonthe chainis animmutable andpublic record
of all transactions, including each Provider’s fulfillment history.
Akash is also politically decentralized. No single entity controls
thenetworkandnointermediaryfacilitatestransactions. Thereforeno
entity is incentivized to control or to extract marginal revenue from
the network. As an example, a large company such as Coca-Cola can
6

Delegate Delegate
consensus
Delegate
new blocks
Photon Blockchain
Provider
peer-to-peer
http / tcp End
Client Provider User
Provider
private overlay network
Figure 1: Illustration of on-chain and off-chain interactions amongst various
participants in the Akash network
participateinthenetworkasaProvider,providingcomputetoanother
large company or to an individual developer, yet all three parties are
on equal footing in the network.
2.2 The Akash Token, AKASH
The Akash Token (AKASH) is used to simplify the exchange of value
and align economic incentives with proper user behavior. The Akash
token is the marketplace currency used to pay for leased compute in-
frastructure on Akash’s decentralized network. Our token serves two
primary functions in Akash’s ecosystem.
In a market that is expected to be $737 billion, with well over
21% annual growth [Gartner(2017)], the liquidity of AKASH will be
matchedbythedemandforcomputepower. Alongthislineofthought,
7

we have full confidence in the network and for AKASH to achieve
maximum liquidity for its early adopters and end state user.
2.2.1 Staking
ThestabilityoftheAkashnetworkreliesonastakingsystemthatpre-
vents bad actors from abusing our system. A staking system provides
a prohibitive monetary disincentive for bad actors who consider par-
ticipating in our network. The risk of fraudulent behavior is highest
when new, unknown providers join our network. Rather than requir-
ing a centralized or federated approval process for new accounts, the
Akash network allows anyone to join.
When a new provider chooses to offer its resources on the Akash
network,ratherthanbeingapproved,itmuststakeameaningfulvalue
on the network in Akash tokens. There is no minimum stake amount,
but participation in Akash Network governance is proportional to a
providerâĂŹs stake, taken as a fraction of the sum of all stakes. Ad-
ditionally, stake contribution is factored into a provider’s reputation
score, which tenants may use as a deployment criterion.
2.2.2 Global Payments
Akash tokens mitigate the foreign exchange risk that usually results
fromcross-borderpayments. Takingtheplaceoffiatforthesetransac-
tions, Akash tokens simplify the exchange of value in the cloud infras-
tructureindustry. Ourmatchingenginecompetitivelypriceseachcon-
tainer compute against a prevailing market amount of Akash tokens.
When a tenant is matched with a provider, the tenant pays Akash
tokens to the network, which are subsequently paid to the provider
according to the terms of the lease.
3 Marketplace
Infrastructure procurement — the process through which clients lease
infrastructure from providers — on Akash is implemented through a
decentralized exchange (marketplace).
Themarketplaceconsistsofapublicorderbookandamatchingal-
gorithm. Clientsplacedeployment orders,whichcontainaspecification
oftheclient’sserviceneeds,anddatacentersplacefulfillment ordersto
bid on deployment orders. Deployment orders include the maximum
amount the client is willing to pay for a fixed number of computing
units (as measured by memory, cpu, storage, and bandwidth) for a
specific amount of time; fulfillment orders declare the price that the
provider will provide the resources for.
8

Deployment orders are open for a client-defined length of time, as
measuredtothesecond. Whilethedeploymentorderisopen,providers
may post fulfillment orders to bid on it.
A fulfilment order is eligible to match with a deployment order if
the fulfillment ordersatisfies allminimum specificationsof the deploy-
ment order. Given a deployment order and a set of eligible fulfilment
orders, the fulfilment order offering the lowest price will be matched
withthedeploymentorder. Ifmultiplefulfilmentordersareeligiblefor
a match and offer the same price, the fulfilment order placed first will
be matched with the deployment order.
Businessesandindividualconsumerswillwantandneedtoprotect
howtheyarepubliclydisplayingtheiruseofcomputepower. Toguard
againstcompetitor data mining and other attack vectors,a homomor-
phic encryption layer is added.
A lease is createdwhen a matchoccurs between a deploymentand
fulfillment order. The lease contains references to the deployment and
fulfilment orders. Leases will be the binding agent in fulfilling a de-
ployment.
datacenter
2
1 2
user orderbook datacenter
2
3
lease datacenter
Figure 2: Summary of procurement from Marketplace. (1) User’s deploy-
ment order is posted to the orderbook (2) Datacenters posts eligible ful-
fillment orders for the deployment order (3) The best fulfillment order is
matched with the deployment order, creating a new lease.
9

4 Deployment
Onceresourceshavebeenprocured,clientsmustdistributetheirwork-
loads to providers so that they can execute on the leased resources.
We refer to the current state of the client’s workloads on the Akash
Network as a deployment.
Auser describestheir desireddeploymentina manifest. The man-
ifest is written in a declarative file format that contains workloaddef-
initions, configuration, and connection rules. Providers use workload
definitionsandconfigurationtoexecutetheworkloadsontheresources
they are providing, and use the connection rules to build an overlay
network and firewall configurations.
A hash of the manifest is known as the deployment version and is
stored on the blockchain-baseddistributed database.
4.1 Manifest Distribution
Themanifestcontainssensitiveinformationwhichshouldonlybeshared
with participants of the deployment. This poses a problem for self-
manageddeployments- Akashmustdistribute the workloaddefinition
autonomously, without revealing its contents to unnecessary partici-
pants.
Toaddresstheseissues,wedevisedapeer-to-peerfilesharingscheme
in which lease participants distribute the manifest to one another as
needed. The protocol runs off-chain over a TLS connection; each par-
ticipant can verify the manifest they received by computing its hash
and comparing this with the deployment version that is stored on the
blockchain-backeddistributed database.
In addition to providing private, secure, autonomous manifest dis-
tribution, the peer-to-peer protocol also enables fast distribution of
large manifests to a large number of datacenters.
4.2 Overlay Network
By default, a workload’s network is isolated - nothing can connect to
it. While this is secure, it is not practical for real-world applications.
For example, consider a simple web application: end-user browsers
should have access to the web tier workload, and the web tier needs
to communicate to the database workload. Furthermore, the web tier
may not be hosted in the same datacenter as the database.
On the Akash Network, clients can selectively allow communica-
tions to and between workloads by defining a connection topology
withinthemanifest. Datacentersusethistopologytoconfigurefirewall
rules and to create a secure network between individual workloads as
needed.
10

Datacenter Datacenter
APP
APP
health checker
health checker
APP
shared state replicated
using a private
peer-to-peer overlay
network
health checker
Datacenter
Figure 3: Illustration of Akash’s overlay network
To support secure cross-datacenter communications, providers ex-
poseworkloadstoeachotherthroughamTLStunnel. Eachworkload-
to-workloadconnection uses a distinct tunnel.
Before establishing these tunnels, providersgenerate a TLS certifi-
cate for each required tunnel and exchange these certificates with the
necessary peer providers. Each provider’s root certificate is stored on
theblockchain-baseddistributeddatabase,enablingpeerstoverifythe
authenticity of the certificates it receives.
Once certificates are exchanged, providers establish an authenti-
cated tunnel and connect the workload’s network to it. All of this
is transparent to the workloads themselves - they can connect to one
another through stable addresses and standard protocols.
5 Automation
The dynamic nature of cloud infrastructure is both a blessing and a
curse for operations management. That new resources can be provi-
sioned at will is a blessing; the exploding management overhead and
complexity of said resources is a curse. The goal of DevOps — the
practice of managing deployments programmatically — is to alleviate
the pain points of cloud infrastructure by leveraging its strengths.
The Akash Network was built from the ground up to provide De-
vOps engineers with a simple but powerfultoolset for creating highly-
automated deployments. The toolset is comprised of the primitives
that enable non-management applications — generic workloads and
11

overlay networks — and can be leveraged to create autonomous, self-
managed systems.
Self-manageddeploymentsonAkashareasimplematterofcreating
workloads that manage their own deployment themselves. A DevOps
engineermayemployaworkloadthatupdatesDNSentriesasproviders
join or leave the deployment; tests response times of web tier appli-
cations; and scales up and down infrastructure (in accordance with
permissions and constraints defined by the client) as needed based on
any number of input metrics. The "management tier" may be spread
across all datacenters for a deployment, with global state maintained
by a distributed database running over the secure overlay network.
5.1 Example: Latency-Optimized Deployment
Figure 4: Illustration of slower performance due to higher latencies for end-
users distributed across the globe for a single datacenter deployment
Manyweb-basedapplicationsarelatency-sensitive -lowerresponse
times fromapplicationserverstranslatesinto a dramaticallyimproved
end-userexperience. Moderndeploymentsofsuchapplicationsemploy
content delivery networks (CDNs) to deliver static content such as
images to end users quickly.
CDNs provide reduced latency by distributing content so that it is
geographicallyclosetotheusersthatareaccessingit. Deploymentson
the Akash Network can not only replicate this approach, but beat it
- Akash gives clients the ability to place dynamic content close to an
application’s users.
Toimplementaself-manageddynamicdeliverynetwork onAkash,a
DevOpsengineerwouldincludeamanagementtierintheirdeployment
whichmonitorsthe geographicallocationofclients. This management
12

Figure 5: Illustration of improved network performance by dynamically dis-
tributing workloads and their state across datacenters in close proximity to
the end-users
tier would add and remove datacenters across the globe, provisioning
moreresourcesinregionswhereuseractivityishigh,andlessresources
in regions where user participation is low.
5.2 Example: Machine Learning Deployment
Machine learning applications employ a large number of nodes to par-
allelize computations involving large datasets. They do their work in
"batches" - there is no "steady state" of capacity that is required.
A machine learning application on Akash may use a management
tier to proactively procure resources within a single datacenter. As a
machine learningtask begins, the managementtier can "scaleup" the
number of nodes for it; when a task completes, the resources provi-
sioned for it can be relinquished.
13

DATACENTER
MASTER WORKER
Figure 6: A machine learning batch job under less load running a single
master and single worker node
DATACENTER
WORKER
MASTER
WORKER
WORKER
Figure 7: A machine learning batch job under load running a single master
and multiple worker nodes
14

References
[Amazon(2017a)] Amazon. Amazon elasticache pricing. 2017a. URL
https://aws.amazon.com/elasticache/pricing/.
[Amazon(2017b)] Amazon. Amazon ec2 pricing. 2017b. URL
https://aws.amazon.com/ec2/pricing/.
[Cisco(2016)] Cisco. Cisco global cloud index: Fore-
cast and methodology, 2015 - 2020. 2016. URL
https://www.cisco.com/c/dam/en/us/solutions/collateral/service-provider/global-cloud-
[Forrester(2017)] Forrester. Predictions 2018: Cloud computing
accelerates enterprise transformation everywhere. 2017. URL
https://www.forrester.com/report/Predictions+2018+Cloud+Computing+Accelerates+Enterpri
[Gartner(2017)] Gartner. Forecast analysis: Public cloud
services, worldwide, 2q17 update. 2017. URL
https://www.gartner.com/doc/3803517.
[Glanz(2012)] James Glanz. Power, pollu-
tion and the internet. 2012. URL
http://www.nytimes.com/2012/09/23/technology/data-centers-waste-vast-amounts-of-energy
[Kaplan et al.(2008)Kaplan,Forrest, and Kindler] James Ka-
plan, William Forrest, and Noah Kindler. Revolu-
tionizing data center energy efficiency. 2008. URL
https://www.sallan.org/pdf-docs/McKinsey_Data_Center_Efficiency.pdf.
[Koomey and Taylor(2015)] Jonathan Koomey and Jon Tay-
lor. New data supports finding that 30 percent of servers
are ’comatose’, indicating that nearly a third of capi-
tal in enterprise data centers is wasted. 2015. URL
https://anthesisgroup.com/wp-content/uploads/2015/06/Case-Study_DataSupports30PercentC
[Liu(2011)] Huan Liu. A measurement study of
server utilization in public clouds. 2011. URL
http://ieeexplore.ieee.org/document/6118751/.
15
