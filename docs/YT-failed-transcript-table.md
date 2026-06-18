# YouTube transcripts to recover (IP-throttle fallback)

These videos were **accepted** by the `semantic-models` research filter (streams 3 & 4,
2026-06-17) but their transcripts could not be fetched: YouTube IP-throttled this
connection (HTTP 429) across both `youtube-transcript-api` and `yt-dlp`, authenticated
or not.

## How to recover each one

1. Open the video URL.
2. Click **·· more → Show transcript** (below the video). If timestamps show, that's fine.
3. Select-all the transcript panel text, copy it.
4. Save it as a plain-text file named **`<video_id>.txt`** in:
   `/Users/andrewgrant/code/knowledge/.knowledge/transcripts/`
   (the `Save-as` column gives the exact filename.)
5. When done, tell me — I'll ingest them via `wiki ingest <url> --force-include`
   (the converter now reads this cache dir before the network).

You don't have to do all 29 — any you save will be picked up; the rest stay queued
for a later automated re-run once the IP unthrottles.

| # | Video | Channel | URL | Save-as |
|---|-------|---------|-----|---------|
| 1 | Semantic Layers w/ Artyom Keydunov & Pavel Tiunov (Cube.dev) | Joe Reis | https://www.youtube.com/watch?v=-30LcwdEIz8 | `-30LcwdEIz8.txt` |
| 2 | KGC 2022 Talk: 'How To Build A Customer 360 Knowledge Graph for FinTech!' — Gupta & Jere, Intuit | The Knowledge Graph Conference | https://www.youtube.com/watch?v=0jDIYzPqZ28 | `0jDIYzPqZ28.txt` |
| 3 | RDF Data Shape Use Statistics: SHACL use on GitHub | IDLabResearch | https://www.youtube.com/watch?v=6-OdjYdEpeU | `6-OdjYdEpeU.txt` |
| 4 | RDF vs. Property Graph: Is your Graph Semantic? - Jesús Barrasa, Neo4j | Connected Data | https://www.youtube.com/watch?v=8cl9IGY4A9E | `8cl9IGY4A9E.txt` |
| 5 | KGC 2022: 'UBS Knowledge Graph —  Connecting The Banks Data' by Gregor Wobbe | The Knowledge Graph Conference | https://www.youtube.com/watch?v=9G4539pngVM | `9G4539pngVM.txt` |
| 6 | Neo4j Cypher: Getting started! \| Neo4j Tutorial | AmpCode | https://www.youtube.com/watch?v=9Y4AlAVtREI | `9Y4AlAVtREI.txt` |
| 7 | Whence Whyis? Creating Knowledge Graphs from Documents — Jamie McCusker \| KGC | The Knowledge Graph Conference | https://www.youtube.com/watch?v=a83gfDqgeuE | `a83gfDqgeuE.txt` |
| 8 | How to handle data about what does not exist | Barry Smith | https://www.youtube.com/watch?v=ai4YdLiCGNM | `ai4YdLiCGNM.txt` |
| 9 | Using CIDOC CRM for dynamically querying ArSol, a relational database, from the semantic web. | TALE: The Archaeology Lecture E-library | https://www.youtube.com/watch?v=Arx3N8tu1Go | `Arx3N8tu1Go.txt` |
| 10 | Building knowledge graphs in the real world. Expert panel at Connected Data London 2018 | Connected Data | https://www.youtube.com/watch?v=e4D0CH8eiv0 | `e4D0CH8eiv0.txt` |
| 11 | Shapes applications and tools Part 1: Introduction to RDF data model and motivation | Jose Emilio Labra Gayo | https://www.youtube.com/watch?v=FowtXinAAF8 | `FowtXinAAF8.txt` |
| 12 | Lecture 07: Uplift - Mapping Relational Databases to RDF | Christophe Debruyne | https://www.youtube.com/watch?v=fS_020V6po8 | `fS_020V6po8.txt` |
| 13 | KGC 2022 Panel: 'Knowledge Graph Architecture: Where Are We and Where Are We Going?' | The Knowledge Graph Conference | https://www.youtube.com/watch?v=H4BbWdhhuEE | `H4BbWdhhuEE.txt` |
| 14 | KGC 2023 Keynote: Knowledge Graphs in Today’s Evolving Landscape & Beyond — Deborah McGuinness, RPI | The Knowledge Graph Conference | https://www.youtube.com/watch?v=hILYM9oBI0M | `hILYM9oBI0M.txt` |
| 15 | The Semantics of a Semantic Layer by Dave Mariani | AtScale | https://www.youtube.com/watch?v=igUnkgp_l14 | `igUnkgp_l14.txt` |
| 16 | KGC 2023 Talk — The EU Knowledge Graph by Dennis Diefenbach, The QA Company | The Knowledge Graph Conference | https://www.youtube.com/watch?v=jn5j0vlqmlk | `jn5j0vlqmlk.txt` |
| 17 | Designing and Building Enterprise Knowledge Graphs from Relational Databases in the Real World | Columbia SPS | https://www.youtube.com/watch?v=JohxmsHE4dI | `JohxmsHE4dI.txt` |
| 18 | Semantic similarity for faster Knowledge Graph delivery at scale. Vassil Momtchev | Connected Data | https://www.youtube.com/watch?v=MXiVLwN8lho | `MXiVLwN8lho.txt` |
| 19 | Masterclass Shapes Constraint Language KGC 2023 | The Knowledge Graph Conference | https://www.youtube.com/watch?v=NP_XCZCPUw4 | `NP_XCZCPUw4.txt` |
| 20 | How to use a Semantic Layer and Data Lakehouse | AtScale | https://www.youtube.com/watch?v=p3TLEV3oIBY | `p3TLEV3oIBY.txt` |
| 21 | KGC 2023 Talk — Using Knowledge Graphs for Navigating Data Assets by RelationalAI's Márton Búr | The Knowledge Graph Conference | https://www.youtube.com/watch?v=Q1aji4uJJgc | `Q1aji4uJJgc.txt` |
| 22 | Knowledge Architecture: Strategy+Data Science+Information Architecture - NASA Data to Knowledge | Connected Data | https://www.youtube.com/watch?v=QEBVoultYJg | `QEBVoultYJg.txt` |
| 23 | Ontology-based Data Access made Practical, by Diego Calvanese | EDBT-INTENDED Summer School 2022 | https://www.youtube.com/watch?v=qGp_Mort9Dg | `qGp_Mort9Dg.txt` |
| 24 | Wikidata Knowledge Graph to Enable Equitable and Validated Ge... - Jonathan Fraine & Lydia Pintscher | The Linux Foundation | https://www.youtube.com/watch?v=r7Qbb1yuLkE | `r7Qbb1yuLkE.txt` |
| 25 | Shapes applications and tools: Part 4. ShEx and SHACL compared | Jose Emilio Labra Gayo | https://www.youtube.com/watch?v=THekUSlGMyo | `THekUSlGMyo.txt` |
| 26 | Sir Tim Berners-Lee on AI and the Semantic Web \| KGC 2026 Lifetime Achievement Award | The Knowledge Graph Conference | https://www.youtube.com/watch?v=Ve6lavTtnQ8 | `Ve6lavTtnQ8.txt` |
| 27 | The Year of the Graph: Evaluating graph databases. Panel discussion at Connected Data London | Connected Data | https://www.youtube.com/watch?v=WH3fVJHM0A4 | `WH3fVJHM0A4.txt` |
| 28 | Headless BI Architecture and Trade-offs - Pavel Tiunov, Cube Dev | Presto Foundation | https://www.youtube.com/watch?v=Z6Yy1xxWQ_0 | `Z6Yy1xxWQ_0.txt` |
| 29 | KGC 2022: 'Yes, You Can Use Knowledge Graphs in Real Life!' — Amazon Web Services & Lexis Nexis | The Knowledge Graph Conference | https://www.youtube.com/watch?v=ZpxIKeVvc08 | `ZpxIKeVvc08.txt` |
