---
id: pdf-dce04675e7ba
type: pdf
title: FallbackPDF__dce04675
url: ''
authors:
- richard galvan
ingested_at: '2026-04-29T16:18:59Z'
content_hash: sha256:2208a46410079f6e1040ee0daf78c40d68799f437035b4327fef24daa3626ac3
source_path: raw/pdf/pdf-dce04675e7ba.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 2
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__dce04675.pdf
published_at: '2025'
---
Microsoft Edge and Dolby Audio
Web browsers have been steadily improving in all facets of their capabilities; performance, text
rendering and formatting, graphics support, and of course media playback capabilities. Recently
Microsoft announced their new Browser, Edge, and with it they announced some of its new
media capabilities. Apart from being the first browser with HEVC (H.265) support it will be the
first browser to support Dolby Audio.
So, what does Dolby Audio support mean? It short, it means that the Edge browser can take
advantage of the Dolby Audio decoder that is part of Windows 10. Windows has had support
for Dolby Audio since windows 7; however, In Windows 8, Microsoft provided access of the
decoder to third party applications and now in Windows 10 they have provided Edge with that
same level of access. The result is that now Microsoft’s Edge browser can play back media
content of all types with Dolby Digital and Dolby Digital Plus audio tracks. These media types
include MP4 files, DASH and HLS Streams.
In order to take advantage of this all one had to do is either use the address bar in Edge to
submit an HLS or DASH manifest file or use the same HTML 5 and JavaScript media features
available in any browser today. These media features included the video and audio tags and as
well as JavaScript when using Media Source Extensions APIs or the Web Audio APIs.
The Edge browser has a built in HLS and DASH player, which will allow a user to just point to any
valid HLS and DASH manifest link and the browser will automatically start playing the content,
including any Dolby Audio. This provides an easy mechanism to playback streams but may limit
the functionality for developers. So, in order to take advantage of Dolby Audio in an HTML5
web application all one had to do is use the video or audio tags.
For example to play back and HLS stream one can use:
<video id="video" controls width=640 height=360 src="myvideo.m3u8"></video>
Since Microsoft’s Edge Browser will unique in its support for not only Dolby Audio, but also
HEVC, and in some cases HLS and DASH. It will be necessary to detect support for any of these
capabilities before using them.
Using JavaScript to provide feature detection will inform the client application that it is running
on a browser capable of any of these features.
Websites that choose to use Dolby Audio should feature detect on the format and be prepared
to stream alternative audio formats on systems that don’t support Dolby Audio.

Javascript examples to check for format support are listed below.
For HTML5:
• Dolby EC-3: test = myvideo.canPlayType(‘audio/mp4; codecs=”ec-3″‘);
• Dolby AC-3: test = myvideo.canPlayType(‘audio/mp4; codecs=”ac-3″‘);
• 264(AVC1): test = myvideo.canPlayType(‘video/mp4; codecs=”avc1.42E01E”‘);
• 264(AVC3): test = myvideo.canPlayType(‘video/mp4; codecs=”avc3”’);
For MSE:
• Dolby EC-3: test = MediaSource.isTypeSupported (‘audio/mp4; codecs=”ec-3″‘);
• Dolby AC-3: test = MediaSource.isTypeSupported (‘audio/mp4; codecs=”ac-3″‘);
• 264(AVC1): test = MediaSource.isTypeSupported (‘video/mp4; codecs=”avc1.42E01E”‘);
• 264(AVC3): test = MediaSource.isTypeSupported (‘video/mp4; codecs=”avc3″‘);
For EME:
• Dolby EC-3: test = MSMediaKeys.isTypeSupported (‘com.microsoft.playready’,
‘audio/mp4; codecs=”ec-3″‘);
• Dolby AC-3: test = MSMediaKeys.isTypeSupported (‘com.microsoft.playready’,
‘audio/mp4; codecs=”ac-3″‘);
• 264(AVC1): test = MSMediaKeys.isTypeSupported (‘com.microsoft.playready’,
‘video/mp4; codecs=”avc1.42E01E”‘);
• 264(AVC3): test = MSMediaKeys.isTypeSupported (‘com.microsoft.playready’,
‘video/mp4; codecs=”avc3″‘);
