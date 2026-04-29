---
id: pdf-722fa9c1c3ec
type: pdf
title: 2022-Streaming-Summit-Netflix
url: ''
authors: []
ingested_at: '2026-04-29T16:09:58Z'
content_hash: sha256:7a6c3a8c8f67811084c5b1395f9300c91f01305db0a9e505b4e2cecdf28052be
source_path: raw/pdf/pdf-722fa9c1c3ec.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 99
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/2022-Streaming-Summit-Netflix.pdf
published_at: '2022'
---
Serving Netflix Video
Traffic at 400Gb/s and
Beyond
Drew Gallatin
NAB Show, April 2022

Serving Netflix Video
Traffic at 400Gb/s and
Beyond
800Gb/s
Drew Gallatin
NAB Show, April 2022

Netflix Workload:
● Serve only static media files
● Pre-encoded for all codecs/bitrates
○ Video quality is of the utmost
importance, so we don’t transcode on
the server
● Greatly simplifies server workload

Netflix Video Serving Stack
● FreeBSD-current
● NGINX web server
● Video served via asynchronous
sendfile(2) and encrypted using kTLS

Timeline:
● Asynchronous Sendfile (2014)
● Kernel TLS (2016)
● Network-centric NUMA (2019)
● Inline Hardware (NIC) kTLS (2022)
● 800G initial results

Sendfile
● Since we are serving static files, we can
use sendfile(2)
● Sendfile directs the kernel to send data
from a file descriptor to a TCP socket
● This eliminates the need to copy data
into or out of the kernel

Netflix Video Serving Data Flow
CPU
Disks Memory Network Card
Bulk Data
Using sendfile, data is sent directly
from disk to network and not
Metadata
touched by the host CPU.
100GB/s
100GB/s

Problem: Disk reads can block
sendfile
● When an nginx worker is blocked, it
cannot service other requests
● Solutions to prevent nginx from blocking
like aio or thread pools scale poorly

Solution: Asynchronous sendfile
● sendfile() becomes “fire and forget”
● Empty buffers are appended to the TCP
socket buffer. TCP stops when it sees
an empty buffer.
● When disk read completes, disk
interrupt handler informs TCP it is ready
to send

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous Sendfile Performance
● Intel Xeon E5-2697v2
○ 12 cores @ 2.7GHz
○ 256GB DDR3-800
○ Chelsio T580 40GbE
● 23Gbs -> 36Gb/s

Timeline:
● Asynchronous Sendfile (2014)
● Kernel TLS (2016)
● Network-centric NUMA (2019)
● Inline Hardware (NIC) kTLS (2022)
● 800G initial results

What’s TLS?
● Transport Layer Security
● TLS encrypts traffic between clients and the OCA

TLS Prevents Sendfile & Triples Memory BW
Disks Memory Network Card
Bulk Data
Data is touched by CPU:
1. Copy from kernel to userspace
Metadata
2. Read data to encrypt
3. Write encrypted data to memory
4. Copy from userspace to kernel
100GB/s
100GB/s
s/BG001
s/BG001
s/BG001
s/BG001

Solution: Move TLS into the kernel
● Eliminates copies between userspace and kernel
● Restores sendfile dataflow
● TLS handshakes (eg, session setup, session
resumption) handled in userspace.
● TLS state handed to the kernel
● Kernel does bulk crypto as part of sendfile pipeline

Asynchronous sendfile + kTLS
Socket Buffer
Internet
Disks

Asynchronous sendfile
Socket Buffer
Internet
Disks

Asynchronous sendfile + kTLS
Socket Buffer
Internet
Disks

Asynchronous sendfile + kTLS
Socket Buffer
Internet
Disks

Asynchronous sendfile + kTLS
Socket Buffer
Internet
Disks

Asynchronous sendfile + kTLS
Socket Buffer
Internet
Disks

Asynchronous sendfile + kTLS
Socket Buffer
Internet
Disks

Netflix 800Gb/s Video Serving Data Flow
Disks Memory Network Card
s/BG001
s/BG001
Bulk Data
Using sendfile and software kTLS,
data is encrypted by the host CPU.
Metadata
800Gb/s == 100GB/s
~400GB/sec of memory bandwidth
is needed to serve 800Gb/s
100GB/s
100GB/s

Timeline:
● Asynchronous Sendfile (2014)
● Kernel TLS (2016)
NUMA (2019)
●
● Inline Hardware (NIC) kTLS (2022)
● 800G initial results

What is NUMA?
Non Uniform Memory Architecture
That means memory and/or devices can
be “closer” to some CPU cores

Multi CPU Before NUMA
Memory access
was UNIFORM:
Memory Memory
Disks
Each core had
Disks
equal and direct
access to all
CPU
memory and IO
Network Card
devices.
CPU
North Bridge
Network Card

Multi Socket system with NUMA:
Memory access can be
Disks Disks
NUMA Bus
NON-UNIFORM
● Each core has
Memory Memory
unequal access to
CPU CPU
memory
● Each core has
unequal access to
Network Card Network Card
I/O devices

Present day NUMA:
Node 0 Node 1
Each locality zone
Disks Disks
NUMA Bus
called a
“NUMA Domain” or
Memory Memory
“NUMA Node”
CPU CPU
Network Card Network Card

Strategy: Keep as much of our
400GB/sec of bulk data off the
NUMA fabric as possible
● Bulk data congests NUMA fabric and leads to
CPU stalls.

Dual AMD: Worst Case Data Flow
Steps to send data: Disks Memory Network
Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
● CPU reads data for encryption
○ Second NUMA crossing
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
● CPU reads data for encryption
○ Second NUMA crossing
CPU
● CPU writes encrypted data
○ Third NUMA crossing
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
● CPU reads data for encryption
○ Second NUMA crossing
CPU
● CPU writes encrypted data
○ Third NUMA crossing
● DMA from memory to network
○ Fourth NUMA crossing
CPU
Disks
Memory Network
Card

Worst Case Summary:
● 4 NUMA crossings
● 400GB/s of data on the NUMA fabric
○ Fabric saturates, cannot handle the load.
○ CPU Stalls, saturates early

Dual AMD: Best Case Data Flow
Steps to send data: Disks Memory Network
Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Best Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Best Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Best Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
● CPU Writes encrypted data
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Best Case Data Flow
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
● CPU Writes encrypted data
● DMA from memory to Network
CPU
0 NUMA crossings!
CPU
Disks
Memory Network
Card

Best Case Summary:
● 0 NUMA crossings
● 0GB/s of data on the NUMA
fabric

Impose order on the chaos..
somehow:
● Disk centric siloing
○ Try to do everything on the NUMA node where
the content is stored
● Network centric siloing
○ Try to do as much as we can on the NUMA
node that the LACP partner chose for us

Dual AMD: Worst Case Data Flow
With Network Centric NUMA Siloing
Steps to send data: Disks Memory Network
Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Network Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Network Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
● CPU Reads data for encryption
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Network Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
● CPU Reads data for encryption
● CPU Writes encrypted data
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Network Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
○ First NUMA bus crossing
● CPU Reads data for encryption
● CPU Writes encrypted data
CPU
● DMA from memory to Network
CPU
Disks
Memory Network
Card

Worst Case Summary:
● 1 NUMA crossing on average
○ 100% of disk reads across NUMA
● 100GB/s of data on the NUMA fabric
○ Still less than fabric bandwidth

Dual AMD: Worst Case Data Flow
With Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
● CPU Writes encrypted data
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
● CPU Writes encrypted data
● NIC Reads data for transmit
CPU
○ First NUMA bus crossing
CPU
Disks
Memory Network
Card

Worst Case Summary:
● 1 NUMA crossing on average
○ 100% of disk reads across NUMA
● 100GB/s of data on the NUMA fabric
○ Less than theoretical fabric bandwidth

Dual AMD: Worst Case Data Flow
With Strict Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Strict Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Strict Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Strict Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
● CPU Writes encrypted data
CPU
CPU
Disks
Memory Network
Card

Dual AMD: Worst Case Data Flow
With Strict Disk Centric NUMA Siloing
Steps to send data: Disks Memory Network
● DMA data from disk to memory Card
● CPU Reads data for encryption
● CPU Writes encrypted data
● NIC Reads data for transmit
CPU
CPU
Disks
Memory Network
Card

Worst Case Summary:
● 0 NUMA crossing on average
○ 0% of disk reads across NUMA
● 0GB/s of data on the NUMA fabric

Timeline:
● Asynchronous Sendfile (2014)
● Kernel TLS (2016)
●
NUMA (2019)
● Inline Hardware (NIC)
kTLS (2022)
● 800G initial results

Why offload kTLS?
● kTLS uses almost half of our CPU cycles

Netflix 800Gb/s Video Serving Data Flow
CPU
Disks Memory Network Card
s/BG001
s/BG001
Bulk Data
Using sendfile and software kTLS,
data is encrypted by the host CPU.
Metadata
800Gb/s == 100GB/s
~400GB/sec of memory bandwidth
is needed to serve 800Gb/s
100GB/s
100GB/s

Mellanox (NVIDIA) NIC kTLS
● Discussed with Mellanox starting in 2016
● First prototypes of CX6-DX in early 2020
● Iterated for 2+ years to make it production ready
●
kTLS offload enabled in production last quarter

What is NIC kTLS?:
● Hardware Inline TLS
● TLS session is established in userspace.
● When crypto is moved to the kernel, the kernel
passes crypto keys to the NIC
● TLS records are encrypted by NIC as the data
flows through it on transmit
○ No more detour through the CPU for crypto
○ This cuts memory BW & CPU use in half!

Netflix 800Gb/s Video Serving Data Flow
Disks Memory Network Card
s/BG001
s/BG001
Bulk Data
Using sendfile and software kTLS,
data is encrypted by the host CPU.
Metadata
800Gb/s == 100GB/s
~400GB/sec of memory bandwidth
is needed to serve 800Gb/s
100GB/s
100GB/s

Netflix 800Gb/s Video Serving Data Flow
CPU
Disks Memory Network Card
s/BG001
s/BG001
Bulk Data
Using sendfile and software kTLS,
data is encrypted by the host CPU.
Metadata
800Gb/s == 100GB/s
~400GB/sec of memory bandwidth
is needed to serve 800Gb/s
100GB/s
100GB/s

Netflix 800Gb/s Video Serving Data Flow
CPU
Disks Memory Network Card
Bulk Data
Using sendfile and NIC kTLS, data
is encrypted by the NIC.
Metadata
800Gb/s == 100GB/s
~200GB/sec of memory bandwidth
is needed to serve 800Gb/s
100GB/s
100GB/s

Mellanox ConnectX-6 Dx
● Offloads TLS 1.2 and 1.3 for AES GCM cipher
● Retains crypto state within a TLS record
○ Means that the TCP stack can send partial
TLS records without performance loss
● If a packet is sent out of order (eg, a TCP
retransmit), it must re-DMA the record containing
the out of order packet

CX6-DX: In-order Transmit

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network
TCP segments of Encrypted TLS Record

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
7240 1570902Gb4E34 N4 etw28o9r6k 1448 0
TCP segments of Encrypted TLS Record

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network
TCP segments of Encrypted TLS Record

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
15298 144810001G30b3E2 N1e15tw84ork10136 8688
TCP segments of Encrypted TLS Record

CX6-DX: TCP Retransmit

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network
TCP segments of Encrypted TLS Record

Host Memory
15928 14480 13032 11584 10136 8688 7240 5792 4344 2896 1448 0
TCP segments of Plaintext TLS Record
PCIe
Bus
NIC
100GbE Network
14480
TCP segments of Encrypted TLS Record

Timeline:
● Asynchronous Sendfile (2014)
● Kernel TLS (2016)
● NUMA (2019)
● Inline Hardware (NIC) kTLS (2022)
● 800G initial results

800G Prototype Details
● Dell R7525
● 2x AMD EPYC 7713 64c / 128t (128c / 256t total)
● 3x xGMI links between sockets
● 512 GB RAM
● 4x Mellanox ConnectX-6 Dx (8x 100GbE ports)
● 16x Intel Gen4 x4 14TB NVME

Initial Results: 420Gb/s
● Ran in 1NPS mode
● Network Siloing mode
● CPUs mostly idle
○ AMD guessed that xGMI was down-linking to x2
○ Set xGMI speed to 18GT/s and forced link width to
x16, and disabled dynamic link width management

Results with DLWM forced: 500Gb/s
● Ran in 1NPS mode
● Network Siloing mode
○ NVME data DMA’ed to NIC’s NUMA Node
● xGMI link usage very uneven:
○ 15GB/s, 4GB/s and 2GB/s
○ Turns out that NVME is not evenly distributed by
IO Quadrants
○ Even hashing of cross-socket to xGMI depends on
evenly distributed IO

How to Improve xGMI Hashing
● Hashing based on device doing DMA
○ NVME is very uneven
○ NICs are much less uneven
○ “Network Siloing” normally does DMA from NVME
to remote node, local to NIC
● Flip things, and do DMA from NVME to local buffers
○ “Disk centric siloing”
● The NICs are now doing DMA across xGMI

Results with Disk Centric Siloing:
670Gb/s
● Much more even xGMI hashing:
○ 10/10/7 GB/s
● Problematic because:
○ Daemon that “locks” content into memory is not
NUMA aware & can lead to page daemon
thrashing.
○ Still pressure on xGMI links

Strict Disk Centric Siloing
● Move Egress NIC to be local to NUMA node with disk
○ No bulk data crosses NUMA Bus
● Incoming TCP traffic still uses original NIC
○ Metadata crosses NUMA bus

“Strict Disk Centric Siloing” Results:
720Gb/s
● Much less xGMI traffic
● Limited by NIC output drops, not CPU.
● Cause of drops is now largely due to:
○ Page daemon interfering with nginx on popular
node
○ Uneven loading on NICs due to content popularity
differences. (NICs on popular node doing 94Gb/s,
others doing 84Gb/s)

Credits
● Async Sendfile
○
Gleb Smirnoff, Konstantin Belousov, Igor Sysoev, Jeff Roberson, Scott Long
● kTLS
○
Scott Long, Randall Stewart, Drew Gallatin, John Mark Gurney, John Baldwin
● NUMA
○
Drew Gallatin, Jeff Roberson, Mark Johnston
● Inline Hardware (NIC) kTLS
○
John Baldwin, Drew Gallatin, Hans Petter Seleaski, Boris Pismenny, Navdeep Parhar

Credits
Experimental 800GbE Hos
● t
○ Warren Harrop and the Netflix hardware team
○ MBX (integrator)
○ AMD (EPYC 7713 CPUs)
○ Dell (PowerEdge R7525)
○ Mellanox/NVIDIA (ConnectX-6 Dx NICS)
○ Intel (P5316 NVME)

Thank you!
