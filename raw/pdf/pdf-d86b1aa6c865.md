---
id: pdf-d86b1aa6c865
type: pdf
title: PowerPoint
url: ''
authors: []
ingested_at: '2026-04-29T16:18:57Z'
content_hash: sha256:5d81a1033fbfe078ac00bdc283be127d2f98b32035ec1e4ad3536632932d4942
source_path: raw/pdf/pdf-d86b1aa6c865.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 44
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__d86b1aa6.pdf
published_at: '2025'
---
Dolby Vision Summary for Comcast
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 1

Document Scope & Objectives
Purpose of this document is to provide a compilation summary of all the messaging
and demos (regarding Dolby Vision) that Dolby has presented to Comcast in the last 8
weeks
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 2

Agenda
1. What is Dolby Vision ?
2. Dolby Vision Benefits
3. Dolby Vision Industry/Ecosystem Momentum Summary
4. Demos Summary
5. Conclusion/Wrap Up
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 3

1. What is Dolby Vision ?
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 4

Dolby Vision is the most advanced end-to-end
HDR solution, enabling Operators & TVs to
deliver unparalleled imaging—
incredible brightness, contrast, color and
detail that bring entertainment to life
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 5

Consumers recognize the difference in Dolby Vision
Best visual experiences
More realistic and moving
content
Access to best entertainment
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

Better visual experiences
GREATER CONTRAST
Delivers much brighter highlights
and deeper darks to create
greater contrast through powerful
high dynamic range (HDR)
technology
TRUE TO LIFE COLOR
Provides a fuller palette of colors
never before seen on TV through
innovative wide color gamut
technology
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

More realistic and moving content
Maintains more information
through transmission / processing
for more true to intent imagery
Better pixels mimic real viewing
experiences to excite senses,
physical and emotional responses
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

Access to the best entertainment
Deep ecosystem [capture,
processing, display] relationships
to create a pipeline of re-
mastered and new content
including top movies, serial
shows, games, etc.
Content just as the director
imagined it, with all the color
and contrast that the camera
actually captured
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

The Technology Behind Dolby Vision
• End-to-End ecosystem solution
– Content Capture: Dolby Vision enables fewer creative trade-offs through maintaining more of
the information that is captured with today’s cameras
– Post Production: New tools and processes to color grade and encode, creating master
grades that can then be translated into various playback formats
– Distribution: content is sent to the home through various distribution channels, first with OTT
services and extending to other formats
– Playback: Ingredient technology integrated into playback devices to support translation of
the Dolby Vision signal to the consumer viewing experience
• Intelligent & Adaptive meta-data based playback engine
– Optimal mapping of video based on content and panel characteristics on a per-scene basis
– Panel BLU (Back Light Unit) control on a frame by frame basis (Global Dimming)
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 10

End-to-End Ecosystem Solution
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 11

Dolby Vision is a Superset of HDR10 with Higher Performance
HDR10 = 10-bit Video (HEVC) + SMPTE 2084 + SMPTE 2086
(Typically mastered at 1000NITs, P3 Color and relies on TV SoC to tone map w/o guidance)
Dolby Vision = 12 Bit Video (HEVC Based) + SMPTE 2084 + SMPTE 2086 + Dynamic Meta Data (SMPTE 2094) +
Intelligent Display Mapping Engine (embedded into SoC)
Note :
• Dolby Supports multiple profiles (Example 12-bit signal encased in 10-bit HEVC Container).
It’s up to the service provider to select the profile they want
• SMPTE 2084 = EOTF
• SMPTE 2086 = Static Metadata
• Dolby Vision is typically mastered at 4000NITs, is BT2020 Color capable and deploys an
• SMPTE 2094 = Dynamic Metadata
intelligent closed loop mapping system based on metadata and panel characteristic data
base, scene by scene, frame by frame
• Dolby Vision content is already mastered for Cinema in BT2020
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

Dolby Vision Metadata : More Comprehensive & Complete
Dolby Vision metadata (2094-10) is distinguished from other HDR metadata (e.g.
2094-30 (TCH) or 2094-20 (Philips) :
• Their metadata is about the mapping from one A to one B (i.e.: SDR to HDR).
• Dolby Vision metadata describes the content and thus enables any A to any B,
forward or inverse
• Also, only 2094-10 (our metadata) has a path via HDMI to a TV panel. Their
metadata stops at the STB and this inhibits their ability to dynamically affect panel
behavior as we do
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 13

Dolby Vision Metadata Usage
• Dolby Vision metadata is created and inserted into the stream in every frame as part of Dolby
Vision content creation workflow
• In OTT use case, Dolby Vision metadata is sent as part of the video elementary stream
• In case of HDMI use case the Dolby Vision Source Device sends the metadata as part of the
LSB of the chroma samples in the first 3 or 4 video lines
• The metadata contains parameters which help in the following areas :
– Dynamic Mapping of the decoded image to the optimal performance of specific display while retaining the
creative intent (color accuracy)
– Detail preservation
– Metadata also contains parameters which are used by Dolby Vision global dimming algorithm to adjust the
back light of the panel on a frame by frame basis, enabling improved contrast, specially in dark scenes
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

Net Result : Dolby Vision Enables Scaling HDR to Lower Cost
HW w/o Loss of Image Quality & Image Integrity
P3
10% 700Nits+
High-End Local Dimming (LD)
$$$
REC 709
350 –500 Nits
30% Mid-Range Mix of LD &
$$
Global Dimming
REC 709
Mainstream 250 –400 Nits
$
Global Dimming
60%
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.
01SV
noisiV
ybloD
HDR10
Vizio 50” P-Series (Dolby Vision) Samsung 50” HDR10
Playback : Vudu, Playback : UHD BD Player
Content : Mad Max in Dolby Vision Content Mad Max in HDR10

The Best Possible Home Entertainment Experience
Dolby Vision is the most widely supported HDR technology with an ecosystem of
partners including creatives, post production, delivery and display partners.
+ =
Specifically mastered Innovative HDR Dramatic imaging
creative content display technology experience
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 16

2. Dolby Vision Benefits
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 17

Dolby Vision Unique Advantages
4. Minimized Distortion & Highest
1. Scene-by-Scene Optimization
Fidelity
2. Scalable Solution 5. Universal HDR Playback
3. Future proof 6. Larger Content Choice
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 18

Dolby Vision Unique Advantages
4. Minimized Distortion & Highest
1. Scene-by-Scene Optimization
Fidelity
2. Scalable Solution 5. Universal HDR Playback
3. Future proof 6. Larger Content Choice
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 19

Scene by Scene Optimization
Luminance
Effective
Range
Contrast Range
Light
TVs with
HDR10
TV with
with
Dolby
Vision Static
Metadata
Dynamic
Metadata
Black
Scene by Scene Contrast
CCOONNFFIIDDEENNTTIIAALL IINNFFOORRMMAATTIOIONN © © 2 021061 D6 oDlbOyL LBaYb LoAraBtoOriReAsT, OInRc.I ES, INC. 20

Dolby Vision Unique Advantages
4. Minimized Distortion & Highest
1. Scene-by-Scene Optimization
Fidelity
2. Scalable Solution 5. Universal HDR Playback
3. Future proof 6. Larger Content Choice
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 21

Scalable Solution
HDR10
P3
1000 –700 Nits+
High-End Local Dimming (LD)
REC 709
350 –500 Nits
Mid-Range Mix of LD &
Global Dimming
REC 709
Mainstream <400 Nits
Global Dimming
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 22
noisiV
ybloD
HDR10 = 10-bit HEVC + SMPTE 2084 + SMPTE
2086
Dolby Vision = 12 Bit Video + SMPTE 2084 +
SMPTE 2086 + Dynamic Meta Data (SMPTE 2094)
+ Intelligent Display Mapping Engine (embedded
into SoC)
Dynamic metadata + Intelligent Mapping
Engine in Dolby Vision enables color
accuracy, improved dynamic contrast and
overall detail retention down to
mainstream panels

Dolby Vision Unique Advantages
4. Minimized Distortion & Highest
1. Scene-by-Scene Optimization
Fidelity
2. Scalable Solution 5. Universal HDR Playback
3. Future proof 6. Larger Content Choice
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 23

Future Proofed
• 10000 Nits Container ensures that as color grading techniques and panel peak
brightness advance, the HDR Signal is still capable to deliver a non-compromised
solution
• 12-bit Video ensures that image fidelity is maintained as panel’s WCG capabilities
improve over time
• BT2020 support capability
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 24

Dolby Vision Unique Advantages
4. Minimized Distortion & Highest
1. Scene-by-Scene Optimization
Fidelity
2. Scalable Solution 5. Universal HDR Playback
3. Future proof 6. Larger Content Choice
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 25

Minimized Distortion
Dolby Vision Dynamic
Metadata, 12-bit Signal
and Display
Management
With Dolby Vision
Creative Intent
Static Metadata, 10-
bit Signal and TV
Processing
TV with Generic HDR
CCOONNFIFDIEDNETNIATL IIANLF OIRNMFOATRIOMNA ©TI O20N1 6© D o2lb0y1 L6a bDoOraLtBoYri eLsA, IBnOc. RATORIES, INC. 26

Dolby Vision Unique Advantages
4. Minimized Distortion & Highest
1. Scene-by-Scene Optimization
Fidelity
2. Scalable Solution 5. VS10 Playback system
3. Future proof 6. Larger Content Choice
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 27

VS10 Benefits to Comcast
• Built-in support for and PQ-based HDR format to any HDMI connected TV
• Simultaneous gamut and dynamic range conversion
• Delivers an improved SDR experience from HDR signals
• Seamless accommodation of content switches prior to HDMI transmission
• Maintains consistent brightness across programs and channels
• Adaptable to encompass additional proposed HDR delivery mechanisms
– Once they mature into stable commercially viable specifications
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

Backwards Compatible to HDR10 Signal
Dolby Vision TV
• Best viewing
experience
HDR10 TV
Dolby Vision Single-Layer BC Signal
• Better HDR10 than
(HDR10 + Metadata) – UHD/FHD Xi6
generic
implementation
(Dolby Vision UHD VS10 STB)
SDR TV
• Better SDR than
current TVs
Dolby Vision Single-Layer BC Signal
(HDR10 + Metadata) – FHD Only
HDR10 TV
• Generic HDR10
Xi5 Experience
(Non-Dolby Vision HDR10 FHD STB)
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 29

Any content service format to any HDMI connected TV & Better SDR
• Dolby Vision VS10 Playback
solution on Comcast STB
Dolby Vision
ensures that same box may
Content
connect to any type of TV
– Content is re-mapped to
maximize target TV’s best
image quality.
SDR Content
• Delivers an improved SDR
experience from HDR signals. HDR10
HDR10 Content
– Retains detail, especially in dark SDR
shadows, when compared with
today’s SDR.
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 30

Simultaneous Gamut and Dynamic Range Conversion
Dolby Vision has its own color space that fully decouples luminance and
color which has a variety of advantages :
• Guarantees preservation of artistic intent within stringent CIE color
difference (dE2000)
• Works with any or no metadata
• Ensures accurate mapping and blending (OSD and Video)
• Ensures stable behavior when blending HDR and SDR content
(accurate graphics blending) – ensures that OSD color is accurate
and consistent, as background video varies from SDR to HDR
• Enables both forward (SDR to HDR) and inverse (HDR to SDR)
capabilities
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 31

Seamless Accommodation of Content Switching Prior to HDMI
Transmission & Maintains Consistent Brightness Across
Programs and Channels
• Eliminates the need for fast switching on the display
• Brightness leveling enables a consistent viewing experience on HDR displays
Net Result is there is no annoying “blanking reset” of TV when surfing between SDR & HDR content and
there is no brightness “pulsing” when surfing between SDR & HDR content
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 32

3. Dolby Vision Industry/Ecosystem Momentum Summary
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 33

Dolby Vision Momentum Wrap Up
• All 7 major Hollywood Studios have released and are committed to Dolby Vision in the cinema – Content
• To date, 4 of them are also committed to bring same content to the home
• Several Netflix originals are committed to be mastered and released in Dolby Vision – Content
• Netflix, VUDU, and Amazon Video are all committed to delivering Dolby Vision content, making it the most widely available HDR
format for North American households- Distribution to homes
• Dolby Vision has been specified in TVs with 7 of the Top 10 NA TV OEMs - Playback/Display
• TV OEMs are implementing Dolby Vision into a range of TV SKUs, from the highest end TVs, to mainstream, high volume products
that are retailing for less than $600 – High Coverage
• Dolby & partners are targeting Q1 2017 to bring Dolby Vision UHD Blu-ray discs and players to market– More Distribution to
homes
• Consumers are also experiencing Dolby Vision in the cinema, which solidifies the expectation for the best HDR experience, and
provides a brand halo when those consumers are shopping for TVs for the home – High Performance Expectation & Quality Bar
Any non-Dolby Vision HDR solution/service would deliver a relatively inferior viewing experience (relative to consumer expectation),
and would also face challenges when competing for VOD revenue against the wealth of Dolby Vision content on OTT services on
growing number of NA smart TVs
DOLBY VISION - CONFIDENTIAL INFORMATION © 2015 Dolby Laboratories, Inc. CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

Dolby Vision is an ecosystem solution with major partners already on board

STB SoC Momentum
Dolby Vision VS10 is actively being integrated into
2017 DMA/STB SoCs that undergo stringent
certification testing prior to MP
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC.

TV SoC Momentum
Dolby Vision is enabled on chips with partners that
account for 75% of the global TV SoC market
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 37

4. Demo Summary
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 38

Dolby Vision vs HDR10 (Phase 1, Demo @ Comcast
Philadelphia, March 2016 )
• Dolby used two programmable PRMs (Professional
Reference Monitor) and PC source (with Netsync)
• Panel capabilities were lowered (Lower Peak Brightness
from 1000NITs to 400NITs), transition from local dimming
to global dimming , color gamut from P3 down to
REC709), to show how a Dolby Vision based system
retains color accuracy, detail and contrast compared to ref
image, where as the HDR10 system loses color accuracy
and detail as the panel capability strays from 1000 NITs
(peak brightness of HDR10 content grading).
Furthermore, the HDR10 image appears washed out
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 39

Dolby Vision vs HDR10 (Phase 2 Demo , Planned for
demo to Comcast Denver on 5/3)
• Plan is to bring two identical LG TVs (400NITs – LLGG DDoollbbyy VViissiioonn TTVV LG Dolby Vision TV
360NITs peak Brightness & RC709)
• On TV will playback (from USB port) content mastered
in Dolby Vision
• The other TV will playback HDR10 version of same
content (Utilizing LG’s in-house developed HDR10
decode & mapping blocks) Dolby Vision HDR10 Content
Content
• We intend to show that real TVs show equal or more
dramatic diff in picture quality , compared to the PRM
demos
• Note, similar results are observed in Dolby Sunnyvale
lab using Samsung HDR10 TV & Vizio P50 Dolby Vision
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 40

VS10 Key Benefits (Demos Shown to Comcast @ NAB 2016)
Set Up : Samsung SDR TV connected to HiSilicon Dolby Vision STB, SDR TV Dolby Vision TV
next to LG Dolby Vision TV connected to HiSilicon Dolby Vision STB
SDR HDMI Dolby Vision
• Demonstrated derived SDR from Dolby Vision signal Output HDMI Output
HiSilicon Dolby HiSilicon Dolby
• Demonstrated graphics blending in Dolby Vision VS10 STB –
Vision STB Vision STB
stable and no pulsing
• Demonstrated Dolby Vision seamless switching & brightness
Dolby Vision Single Layer Profile Stream
leveling function as content to HiSilicon Dolby Vision STB
alternated between SDR & HDR
– Note : We also demonstrated how the screen blanks out for a short
time when feature is disabled
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 41

Dolby Vision Scales to Mainstream Panel Spec (Demo to
Comcast During NAB 2016)
Set Up : Dolby PRM (1000 NITs, 1500 Zones Local Dimming
LG Mainstream
P3 Color Gamut) and LG (Mainstream) Dolby Vision TV Dolby PRM
Dolby Vision TV
(400NITs – 360 NITs Peak Brightness, Edge-lit Global
Dimming, REC709) connected to 2 “netsynched” PCs playing
back same Dolby Vision content (Lego Movie & Man of Steel
clips)
Playback PC1 Playback PC2
• Demonstrated Dolby Vision metadata + Display Mapping
Engine enable closeness of LG TV playback image to NetSynch
reference image (PRM)
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 42

5. Conclusion / Wrap Up
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 43

Conclusion/Wrap-up
• Dolby Vision delivers the highest quality HDR viewing experience for any given playback device
• Dolby Vision has a strong following with TV OEMs selling into NA. Because of its metadata based scaling capability, TV
OEMs are deploying Dolby Vision into mainstream TVs (as well as high-end)
• All 8 major Hollywood studios are committed to Dolby Vision, as are the top 3 NA OTT service providers
• Comcast service in Dolby Vision would ensure that subscribers are getting the same quality of VOD (& live) playback as they
get from OTT & Cinema – Best in class HDR Video
• Dolby Vision service from Comcast would be non-disruptive as our advanced HDR signal is backwards compatible to HDR10
(Comcast Xi5 STB)
• Dolby Vision VS10 addresses all the technical challenges Comcast would encounter with HDR & SDR hybrid environment,
ensuring that there is no compromise in the user experience that Comcast delivers
– Universal HDR playback solution including support for HDR10
– Smooth transition in & out of HDR/SDR
– Consistent Graphics & Video Blending
– Better SDR
– SDR to HDR up-conversion
CONFIDENTIAL INFORMATION © 2016 DOLBY LABORATORIES, INC. 44
