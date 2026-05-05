---
id: pdf-5add0d29d90b
type: pdf
title: FallbackPDF__5add0d29
url: ''
authors:
- Andy Wehmeyer
ingested_at: '2026-04-29T16:15:14Z'
content_hash: sha256:5ef6cba474a9725b60d483cf9b395fcb1a24098ee57a35c1752f027841e19b7b
source_path: raw/pdf/pdf-5add0d29d90b.pdf
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  page_count: 58
  extraction_tool: pdfplumber
  pdf_metadata_subject: ''
  pdf_metadata_keywords: ''
  original_path: /Users/andrewgrant/code/apple-notes/pdfs/FallbackPDF__5add0d29.pdf
published_at: '2025'
---
A Straightforward One-Seat Stereo
Tuning Process and Some Notes About
Why it Works

The Process
Note 1: This process assumes the input to your DSP is confirmed as a flat, two-channel and in phase
signal, like that of an aftermarket radio.
Note 2: In an active system in which your tweeters are driven by an amplifier directly, install a capacitor
in series with each tweeter to protect it from erroneous crossover settings, turn on and turn off pops and
other failures that may destroy them. Choose a capacitor value that provides a -3dB point about an
octave below the tweeter’s Fs.
Note 3: This is not an iterative process in which you listen and then make an adjustment or two and then
listen again to confirm an improvement. Once you’ve confirmed that all the speakers are connected and
playing, there’s no need to listen until after all of the settings have been made and you’ve put away the
RTA.
Polarity, delay, crossovers, level and EQ, confirmation and additional level adjustments. That’s the
order.
1. Confirm that electrical polarity is correct. Use the markings on the speakers and the amps, a polarity
checker or the UMI-1 and a scope. Do not set polarity by listening for a center image from speaker pairs!
2. Put the mic in the car.
3. Measure from the center of each speaker to the microphone. Estimate a straight line from the sub to
the mic no matter which way the sub is facing. If your system includes passive crossovers for the front
speakers, measure to the midbass driver in a 3-way system or the midrange in a 2-way system. Input the
distance or the delays depending on the DSP’s requirements. Some processors will allow you to enter
the delays as distance and some only in milliseconds. In those cases, you’ll need to do the math. Be
careful! Distance to the speakers and delays are not the same. See “Setting Delays” in a subsequent
section.
4. Set the crossovers. Use 24dB/octave slopes and Linkwitz-Riley alignments. Set the subwoofer low
pass filter ½ an octave below the midbass high pass. For example, if your midbass high pass is 80 Hz, set
the subwoofer at 60 Hz.
5. Equalize the left channel. Turn on the RTA, play the mono pink noise track from the Audiofrog Stereo
Tuning CD (included with the UMI-1). Start with the left channel, including the subwoofer, and adjust
the level controls on the amplifiers (or in the DSP) and the EQ to get as close to the target as you can.
Save the measurement in the RTA.
6. Match the right channel to the left channel using the same process.
7. Play mono pink noise through both channels at the same time. Look at the RTA display. This is the
frequency response of your center image. If you see a BIG dip or a series of big dips (9dB or more), then
your delay settings are incorrect or the signal into your processor includes delay or phase EQ. Go back

and check to see if the DSP needs the distances from the mic to the speaker or the delay settings. If your
delay settings are correct, check the input signal.
8. Use the bandwidth limited pink noise tracks on the Audiofrog Stereo Tuning CD included with your
UMI-1 (2-5) to check for center placement of the various bands. Don’t be too concerned about exact
placement. We’re not concerned with the details here. The pink noise should not seem to come from
either the left or the right speaker but from an area in between. The position of the high frequencies in
track 5 will be less defined. This is because of high frequency reflections from the dash and the
windshield. That’s OK.
9. Use tracks 6-20 to confirm image placement. The images should move smoothly and evenly across
the dash. Left and Right tracks should come from the left and right speakers. Center tracks should be in
the center of the dashboard. Left of Center and Right of Center tracks should appear halfway in between
the Left and Center or right and center locations. If the center is too far to the left, turn the entire left
channel down a little. If it’s too far to the right, turn the right channel down a little bit. Do not adjust
delays to move the image.
10. Check for noise using Track 38. If you hear a hissing sound from the tweeters and you don’t like it,
turn ALL the amplifier input sensitivity controls down by exactly the same amount until it goes away. If
the system isn’t loud enough, you’ll need to strike a balance between the presence of some noise and
appropriate system level.
That’s it.
Why This Process Works—Additional Explanation
“It’s all subjective and there’s no right or wrong.”
I hear this all the time, and it simply isn’t true. Stereo recordings are designed to do something specific
and there are some aspects of music reproduction that aren’t addressed in a simple stereo recording.
There are lots of misconceptions about what a stereo recording actually is, so we’ll cover some basics
before we get started with tuning automotive stereo systems.
Direct to Two-Channel
In a direct to 2-channel recording, a pair of microphones, arranged to capture the live event are placed
in the performance space as in the picture below (from Sweetwater):

Each of the mics is connected directly to one of two channels in a recording device. From here on out,
we will refer to that device as a “Digital Audio Workstation”, or “DAW”, which is usually a computer
program that receives its inputs from an audio interface. That audio interface converts the analog
signals from microphones and instruments connected directly to it into digital signals that the computer
program can use.
In a direct to 2-channel recording, the microphones capture the sound that arrives at the mic directly
from the instruments. They also capture the reflected sound that arrives at the mic after bouncing off
the floor, the ceiling and the walls surrounding the recording space. The level and phase at which the
direct sound arrives at the two microphones, and consequently in the two channels, determines their
placement from left to right in the recording. The reflected sound captured at the microphones helps to
place the musicians in a room—the recording space.
If the recording is played back over two speakers arranged in the same space as the recording in roughly
the position of the left and right most instruments, the reproduction will be believable. The sounds from
the speakers will be reflected in much the same way as the sound of the original instruments and we’ll
have reproduced the performance pretty well. The dispersion characteristics of the speakers will affect
the believability, but we’ll ignore that for this part.
If we play the recording over two speakers in a similar room, then the reproduction will be similar. The
degree to which the size and shape of the room in which we place the speakers is similar to the original
recording space will determine how close we get to the actual performance.
This is why some of the audiophile labels (see Mapleshade for an example) often bring musicians into a
residential space like a living room and make a direct to 2-channel recording to be played back over a
high quality pair of loudspeakers in a similar residential space.

The interior of a car is not similar to the original performance space. If the system is properly designed
and tuned, you’ll be able to hear the placement of the musicians from left to right between the
speakers. Because the ambient information from the original space is in the recording, you’ll also hear it
in the playback, but the image of the recording space will be limited somewhat by the size of the car—
the playback space.
Studio (Multitrack) Recordings
Studio recordings are more common. In this type of recording, performers may be located in the same
recording space. They may also be recorded separately, in different rooms and at different times. In
some cases, the performers may be in different countries and the recording times may be months apart.
The drums may be recorded in a separate room with room treatments designed to reduce the
contribution of the room reflections in the recording as in the picture below:

The piano may be recorded in another room with similar or dissimilar treatments:
The vocal tracks may be recorded in a reflection-free environment like the one here:

No matter the separate spaces in which the individual tracks are recorded, there is no real recording
space for the combination of the tracks, so in making a stereo recording of these events, the engineer
has to place those separate events on a virtual stage in a virtual room. He does this in the DAW (Digital
Audio Workstation).
Panning Images Across the Stage
Initially, the separate events are loaded into the DAW as separate tracks and the levels of each of those
tracks are set in the left and right channels to place them horizontally in the recording. The relative level
of each of the tracks sent to the left and right channels determine the point at which they’ll appear
between the left and right speakers in the playback system.
A sound sent only to the left channel will be played back only by the left speaker. A sound sent only to
the right channel will be played back only in the right speaker and the placement of the speakers will
determine the width of the image we hear. A sound sent equally to the left and right channels will
appear at a point halfway between the left and right speakers. A little more level in the right channel
moves the image to the right and vice versa for a sound recorded a little louder in the left channel than
in the right channel.
Placing Sounds from Front to Back and Creating a Virtual Room
Panning images from left to right only places them in the horizontal plane. Another technique is used to
place the instruments from front to back and to create a room. If we back up to the direct to 2-track
recording, we’ll remember that the reflections from the ceiling, floor and side walls were captured by

the stereo microphones. In the multitrack recording we’re talking about now, the rooms are different. In
some cases, the room has been treated to reduce the level of reflections and, in the case of the vocal
booth, may have been treated to remove them entirely. In order to create a virtual space, those
reflections have to be created.
If the engineer wanted to recreate a performance space like the one at the Jazz Factory in the picture
below, he would have to place the instruments in some arrangement in the recording to create a room.
The placement from left to right would be accomplished with the panning technique explained earlier.
For musicians located near the back wall, he would add some reflections to the recording—the sound of
the instruments arriving at the microphone a little later after bouncing off of that wall. For musicians in
the middle row, he’d add similar reflections that arrived a little later since the musicians located in the
center row are farther away from the back wall. He would probably increase the level of the direct
sound from the instruments in the middle row compared to those in the back row since they’re located
closer to the audience. A similar set of reflections would be added to sounds coming from instruments in
the first row. All of these are commonly referred to as “early reflections” and they define the space in
which the performers are located.
In order to create the sense of space that surrounds the audience, another set of reflections are often
added to the combination of direct sound and early reflections. Those reflections are the ones that
come from walls that surround the listeners. Those are called “late reflections” because the walls are
farther way and because both direct sound and the sound of the early reflections bounce off the rear

wall and the side walls near the listeners. The combination of early and late reflections define the entire
performance space.
All of those reflections are sometimes called “reverb”. Years ago, the tools for creating reverb were
simple. Early devices used a spring or a series of springs and a tensioner to create the sounds of
reflections. Fortunately, DAWs provide an opportunity to do a much better job.
Modern techniques often include a set of controls for creating and shaping reflected sound. Basic
settings include the length of the reflection, the loudness of the reflection and the frequency response
of the reflection. Convolution reverb allows the impulse response (recording of a recording space’s
reflections only) to be mixed with the direct sound to place the musicians in that space virtually. This is
very effective and can be very realistic.
Some recordings don’t include the sound of a recording space, whether real or virtual. Many EDM
recordings serve as good examples. Some are a mixture. Many recordings include drums or piano that
are panned to span from far left to far right with a vocalist and the rest of the instruments placed on a
virtual stage in between. In other recordings, instruments may move around, back and forth or may be
isolated to a single speaker without any reverb to place it on a virtual stage. Led Zeppelin’s “Whole Lotta
Love” is a good example of this.
Of course, for most recordings, none of this is documented and we are left to infer the artists’ original
intent by listening carefully to the recording.

What’s the Reference?
If we’re tuning a playback system to reproduce the recording in a believable way, how do we know
when it’s right? Which recording do we use? What if the guy doing the tuning uses one set of recordings
and the guy evaluating the system uses another? If everything is right and if both tuner and evaluator
know the recordings, then everything sort of works out. If either of them infer the intent incorrectly,
then we’re setting ourselves up for problems. It’s helpful to have a common reference that’s designed to
help us. The Audiofrog Stereo Tuning CD has been designed to make this easier and to remove the need
to infer placement from a recording that is undocumented.
Tuning the System
I don’t like the word “tuning” for this process because it suggests a subjective process or optimizing for
one’s preference. That’s part of the process, but it isn’t the whole process. “measuring the performance
of the system and addressing the issues” is a better description of a process designed for success.
Measuring the Performance of the System and Addressing the Issues
It’s important to be mindful of what is and isn’t possible from a playback system. Misunderstanding
what’s possible and attempting to extract performance that’s impossible is the enemy of a predictable
process that can be implemented consistently across many cars and systems.
If we expect the best possible performance from the stereo system, we have to configure it correctly.
Some of that configuring is part of designing and installing the system. Some ground rules for designing
systems that work well are presented below:
1. The placement of the left and right speakers define the left-most and right-most position of direct
sounds in the reproduction. A guitar recorded only in the left channel will seem to come from the left
speaker. Early reflections in the recording may provide a sense of space that extends outside the bounds
of the speakers, but the instrument won’t come from a point far outside the speaker location.
2. The distance from the listening position to the horizontal plane in which the speakers are mounted
will determine, for the most part, the apparent distance to the stage. Early and late reflections in the
recording may help to move some instruments rearward.
3. Creating an image that spans between the locations of the left and right speakers with a stable and
focused center image requires that the sound from the left and right speakers arrives at the listener at
the in phase and at the same level at all frequencies. Clearly, we’re going to need some help here since
the listener is not seated directly in between them. We’ll use delays to correct for the offset listening
position in the driver’s seat.
4. Since we are talking about a stereo system that’s comprised only of front speakers and probably a
subwoofer, there’s nothing in the system to reproduce the late reflections that would arrive from
surfaces far behind us in the real performance space. Since the interior of the car is undoubtedly

smaller than the space in the recording, the reflections from the rear and sides of the car’s interior are
going to define the size of the apparent recording space. That means it’s going to be “car-sized”.
Referring to the diagram above, the images you create with a 2-channel system are going to lie within
the triangle defined by the listening position and the speaker locations. Stage depth and the distance to
the stage are two different things. The distance from the listener to the apparent stage will depend
mostly on the distance from the listening position to the location of the speakers. Stage depth depends
on the ambient information about the recorded space that is included in the recording and not on your

settings. A recording that lacks information about the recording space will not reproduce depth that
extends far behind the horizontal plane defined by the speaker positions or width that extends past the
sides of the triangle.
Setting Delays
In order for the system to produce a stable phantom center image, the sound from the two front
speakers has to arrive at the listening positon in phase. Because we sit closer to one speaker than the
other, this doesn’t happen and that prevents the stereo system from creating a proper center image.
Delays are used to compensate for distance. Delay works by storing the signal that will be sent to the
nearest speaker and releasing it so the sound of the nearest speaker arrives at the listening position at
the same time the sound from the farthest speaker arrives. Delay doesn’t “align time”, but it does align
signals to that they arrive at the same time.
Delays don’t “move“ speakers. Delays don’t extend the width of the image past the speaker locations.
Delaying all the speakers in the front of the car doesn’t change the perception of stage depth nor does it
change the distance to the stage.
Here’s an example. Let’s say you live in Pasadena and you’re going to meet some friends who live in Mid
City Los Angeles at The Roxy in Hollywood for a concert. You have all the tickets, so meeting there at the
same time makes distributing the tickets easier. It’s an hour from Pasadena to the Roxy, but it’s only 25
minutes from Mid City. You leave home at 7:00 and you tell your friends to leave home at 7:35. Then,
you’ll both arrive at 8:00. Telling your friends to leave later doesn’t change the location of their house.
They aren’t, all-of-a-sudden, driving from East LA. Delays don’t “move“ speakers or change their
apparent location.

There’s a common misconception that delay settings are the only or, at least, the best way to set the
placement of the center image. This isn’t correct. Tuning cars under that misconception often leads to a
center image that wanders back and forth depending on the note that a singer (who is placed in the
center of the recording) sings.
When one speaker is closer to the listener than the other a comb filter is created. The frequency at
which ½ the wavelength is equal to the difference in distance from each of the speakers to the listening
position will determine the frequency where the comb filter begins.
Here’s how that works in a typical car stereo system with speakers mounted in the doors. Let’s say we
measure from the driver’s speaker to the microphone and the distance is 40”. When we measure from
the microphone to the passenger’s door speaker, the distance is 67”. The difference between them is
27”. 27” corresponds to half a wavelength at about 250 Hz. (The speed of sound is roughly 1132
feet/second or 13,582”/second. 13,582” divided by 2 times 27” is about 250 Hz.) The measurements in
different cars may differ slightly, but the concept is the same any time the speakers are not equidistant
from the listener.
In the example above, our front speakers are 180 degrees out of phase at 250 Hz. That means that at
250 Hz, the sound of the two speakers cancels. That creates a dip in our frequency response and it also
destroys our phantom center image at that frequency. Similar dips in the frequency response occur at
higher frequencies. The frequency response of the independent channels is on the left and the sum
(what we hear) is on the right.
At every point at which there is a dip in the frequency response, there’s also no center image. Delaying
the driver’s side speaker by 2 milliseconds to compensate for the difference in distance corrects all of
the problems at the microphone position, as shown in the next image.

If you read the basic description of this process on the first page, you may remember the suggestion
that listening to pairs of speakers to determine the right polarity is not the right process. Here’s why.
Let’s say you’re listening to the right and left midbass speakers to determine how to set polarity before
you’ve applied delays. Below is the response of the midbass drivers with crossovers applied but with no
delays implemented. Individual responses are on the left and what you hear with both speakers playing
is on the right.
Our dip at 250 Hz, caused by path length difference, creates a poor center image when we play a mono
vocal, so we flip the polarity of one channel—1980’s style (before we had DSP). Here’s the result:

The center image at 250 Hz is improved, but the low frequency response when both speakers are
playing is worse. Since we’re just listening for the center image using a female vocal, we assume that
this is the correct polarity setting. Then, we measure to our speakers, set our delays and this is what we
have:
Oops. Now our midbass drivers are 180 degrees out of phase at all frequencies. Our center image in the
midbass is gone (that’s the graph above and on the right) and we hear the location of the two midbass
speakers with no center image whatsoever.
Then, maybe we assume that the tape measure is wrong so we adjust delays by ear. We listen to a
vocalist in the center and we start adjusting delays until we get our image back. We arrive at 2.5
milliseconds while we’re listening to a center vocal, which is now centered, but we still have a bass
problem and the speakers still aren’t in phase.
If you’ll be using delays, which are designed to compensate for distance, set polarity according to the
markings on the amps and the speakers, use a polarity checker, or use the UMI-1 and a PC-based
oscilloscope program. We always use a tape measure to determine distance and it isn’t wrong this time.
Set delays using a tape measure. That puts the speakers in phase at a single listening position at all
frequencies.
Setting delays by ear using chirps, mono vocals, sine wave tracks or pink noise is possible, but that

process is fraught with potential for error. If we remember the explanation of panning an image to the
center of a recording, we might also remember that a sound recorded in the center has to be exactly the
same in the left and the right channels in order to appear in the center. That includes level and
frequency response. If you’re setting delays at the beginning of the process using your ears, but the
levels and the frequency response of the speakers haven’t been precisely matched, then there’s a good
chance that you will misalign the speakers using delays to center an image that appears off center due
to a poor frequency response and level match.
Measuring impulse responses to determine the “flight time” of the sound from the speaker to the
listening position is also possible. Interpreting the measurements is quite difficult and if the signal to the
speakers includes crossovers, then it’s even more difficult.
Finally, the suggestion that that fine adjustment of delays, ultra- precise measurements or ever-
increasing resolution of delay settings is important is also unfounded. Do you really need to account for
the exact position of the midbass driver’s acoustic center? What if our measurements are off by a little
bit? Let’s see…
In our example above, we’ve determined that the path length difference is exactly 27”. What if we make
a small error? What happens to our image? We can verify easily with our model of door mounted
midbass drivers. Here, I’ve delayed the left speaker by 26” instead of 27”—an error of one inch.
Hey! There’s no difference! Let’s see what’s going on. We’ve obviously made an error, but it doesn’t
seem to affect performance. Let’s remove the low pass filters to get a better look.

So, missing by an inch creates an error at 7.5 kHz, but our midbass speaker has a low pass filter at 300
Hz. So just how much accuracy is really required when measuring to the midbass speakers? Let’s
investigate further.
In this example, I’ve made an error of 6” and the problem still doesn’t appear within the band of
frequencies that the midbass drivers play.
So what does all of this mean? It means that you should use the tape measure carefully. Measure from
the grilles or the dust caps of each speaker to the microphone. Get as close as you can. Input the right
numbers and your results will be great. There are other ways to measure, but none are necessarily more
accurate and none are as quick and simple. Once you’ve set your delays to correctly compensate for
distance, leave them alone. They aren’t wrong.
Entering the Right Numbers in the DSP’s Control Panel
Depending on the DSP you’re using, you may need to enter the distances from the microphone to each
speaker or you may need to enter the delays to be implemented. You may be able to enter the delays as
distance or in milliseconds. The difference between entering the distance and entering the delays is not
trivial and getting this wrong will wreck the performance of the system.
If the DSP’s control panel requires you to enter the distances from the mic to each speaker, simply

measure from the tip of the microphone to the center of the speaker grille. The actual origin of the
sound for this purpose is the voice coil. You can estimate that distance using the speaker or a side view
drawing of the speaker. If those aren’t available to you, don’t worry. Just measure to the grille. This
won’t affect the center image at all.
If your DSP requires you to enter the delays rather than the distance to the speakers, you can figure out
the delay values easily. Measure from the microphone to all of the speakers and write down the values.
Then, find the largest value (the distance to the speaker that’s furthest from the microphone) and
subtract all of the other values from that one. Enter those values for each speaker.
For example, if the subwoofer is 70” away from the microphone and the driver’s side tweeter is 32”
away from the microphone, you would subtract 32 from 70 and enter the result (38”) for the tweeter.
Since the subwoofer in this system is the furthest away, you’d enter 0 for the subwoofer.
If the DSP requires you to enter the delay in milliseconds (mS), then after you’ve done the subtraction
above, you have to convert those number to milliseconds. You can divide the pathlength differences
you’ve found by 13,584” (the speed of sound in inches per second) and then multiply by 1000 (to
convert from seconds to milliseconds. If you have Microsoft excel or Google Sheets, you can download
the spreadsheet “Basic Delay Calculator.xlsx” from https://testgear.audiofrog.com. Enter the distance
from the mic to each speaker in the yellow boxes and the spreadsheet will calculate the rest for you. If
there is a speaker location that you aren’t using, be sure to enter a zero in that box.

Setting Crossovers
Crossovers limit the signals sent to speakers so that they work within the range of frequencies for which
they are intended and for which they are optimized. In order to make tuning systems easier and, to
make them sound their best, it’s a good idea to follow the three most basic rules:
1) speakers should be used in regions in which they make the least distortion,
2) Crossovers should be set to prevent too much excursion, which can damage speakers and
3) To simplify equalization in near field reflective environments, speakers should be used in regions
where the dispersion of sound is wide so the direct sound and the reflected sound are as similar as
possible.
How Crossovers Work
High-pass filters and low-pass filters work by attenuating the signal below or above a frequency that we
can select. The rate of attenuation is determined by the slope of the crossover that we choose. The
slope is usually referred to as a rate of some number of decibels per octave. At the frequency we select,
a Butterworth filter is -3 dB at the filter frequency (the level is reduced by 3dB). Other crossover slopes
are also possible. The graph below shows Butterworth high-pass filters of 6dB/oct, 12dB/oct,
18dB/octave and a 24dB/octave Linkwitz-Riley filter. The Linkwitz-Riley filter is -6dB at 3 kHz. Filters are
often referred to as acronyms, as in the graphs below. BW1 is a first order (6 dB/oct) Butterworth filter.
BW2 is second order (12 dB/oct). BW3 is third order (18 dB/oct) and LR4 is a fourth order (24 dB/oct)
filter. Each 6 dB is an “order”.

The graph below shows Butterworth 3 kHz low-pass filters of 6dB/octave, 12dB/octave, 18dB/octave
and a Linkwitz-Riley 24dB/octave. Like the Linkwitz-Riley high-pass filter, the low-pass filter is -6 dB at 3
kHz.
When we combine a high pass filter with a low pass filter, the result is a crossover. A Butterworth 1st
order crossover is shown (BW1). The combination of the high-pass and low-pass filters is the “sum”,
labeled BW1 Sum in the graph legend.

“Don’t crossovers shift phase and shouldn’t we avoid them?” I hear this question all the time. The
answers are “yes, they shift phase” and “no, we shouldn’t avoid them”. Phase shift is how filters work.
Phase shift determines how the response from the two speakers, with filters applied, add together at
our ears or at the microphone. For every 6dB/octave, the phase changes by 45 degrees. In a high pass
filter, the phase leads and in a low pass filter, the phase lags. For a crossover to work properly, the
frequency response and the phase response of the high- and low-pass sections should be
complementary.
Basic crossover design assumes that the sound from each speaker arrives at the listening position at the
same time and that they originate from the same point in space. Obviously, this isn’t possible. We use
delay to satisfy the first of those criteria. The it isn’t possible to completely satisfy the second one, so
we won’t bother with that one. Since our crossover performance depends on correct delay settings, we
should always set the delays before the crossovers.
First order Crossovers
Below is the graph of a first order crossover including the sum (what we should hear). In a first order
crossover, the sum is flat regardless of the polarity of the speakers because the speakers are 90 degrees
out of phase at all frequencies. That’s cool, but the slopes are so gradual that they don’t remove bass

from small speakers fast enough to be useful in car audio systems that have to play loudly. In addition,
the transition band (the range of frequencies that both speakers play) is so big that the performance of
the crossover is degraded by timing errors or baffle placement and shapes that deviate from the ideal
flat baffle. We should avoid first order crossovers.
Second Order Crossovers
Below is a graph of a second order Butterworth crossover with the speakers connected in the correct
electrical polarity. With a second order crossover applied to the speakers, they are 180 degrees out of
phase at all frequencies and that condition causes cancellation in the range of frequencies that both
speakers play. That makes a deep dip in the frequency response around the crossover frequency and
degrades the image of all the sound coming from single point.

If we swap the polarity of either the high frequency speaker or the low frequency speaker, we can trade
the big dip for a small peak at the crossover. Swapping the polarity of one speaker puts the two speakers
back in phase at all frequencies and because the crossover point is -3dB and the sum of two identical
signals is +6db, that leaves us with a 3db peak.

12dB per octave is a steeper slope than the 6dB per octave slope and, therefore, provides better
protection for small speakers. Second order crossover performance still relies on almost exact
placement and delay settings for optimum performance. We can use our EQ later to remove the hump,
but why do the additional work?
We can do better than a second order filter.
Third Order Crossovers
An 18dB/octave Butterworth crossover is a better choice. The slopes are steeper and the sum of the
high pass and the low pass filters is flat regardless of polarity. Because the slopes are steeper, the
performance of a third order Butterworth filter a little less dependent on perfect placement or delay
than first order or second order Butterworth crossovers. This is a much better choice, but we can still do
better.

Fourth Order Crossovers
A 24dB/octave Linkwitz-Riley crossover (LR4) is the slope and alignment I recommend. Because the
slopes are so steep, the performance is almost the same regardless of the positioning of the speakers
and the LR4 is more forgiving of delay errors and changing listening positions. They also provide the
maximum protection for smaller speakers. Fourth order Linkwitz-Riley filters sum flat when the electrical
polarity is correct and they include a big dip when the polarity is incorrect. If you see the big dip, you
know to go back and correct your polarity settings.
A fourth order Linkwitz-Riley crossover in the correct polarity is indicated in the graph below.

And with one of the speakers inverted, it looks like the graph below. If we see this, then we know our
polarity settings are incorrect.

Crossover filters are applied to the speaker in order that the output of the speaker matches the target
response—the output of the speaker is what you hear. One additional advantage of the steeper LR4
crossover is that so long as you’re filtering the speaker in a region where the its response is relatively flat
and the response extends past the crossover by about an octave, the acoustic response will follow the
crossover’s electrical response and that ensures good acoustic performance. All Audiofrog speakers are
designed this way and the crossover recommendations are included to make this process easier.
Since this process is designed to be implemented from start to finish without a bunch of subjective
analysis and backtracking, the LR4 is the right choice because,
1) It provides maximum protection for small speakers and tweeters,
2) The performance of the crossovers is less dependent on small errors in delay and different
seating positions for listeners of different height
3) We’ve already connected our speakers in proper electrical polarity, which is the optimum
connection for this crossover
4) This crossover provides an automatic check for our polarity settings
5) The acoustic output of the speaker is more likely to match the electrical response of the filter,
which makes equalization easier.

Choosing Crossover Frequencies
As I mentioned at the beginning of this section about crossovers, there are three main criteria for
choosing a crossover point. First, the crossover should be chosen to keep bass out of small speakers.
This keeps them safe from over excursion and it reduces distortion. Free air resonance (“Fs” in the
Thiele and Small parameter sheet) is the frequency at which the speaker makes the most distortion. It’s
also the frequency below which the suspension has to do a lot of work in preventing damage to the
speaker. We should avoid driving the speaker at or below Fs. For tweeters, 1.5 to 2 times Fs is a good
choice. For midrange and midbass speakers, crossing at Fs (ideally a little higher) is OK so long as you’re
using steep crossover slopes.
Crossing midbass drivers over well below Fs is often thought to contribute to a better image of bass in
the front of the car, but it isn’t necessary. It also contributes to higher distortion. Don’t cross below Fs.
We don’t have any choice but to use subwoofers at and below Fs. Fortunately, we don’t hear distortion
as easily at really low frequencies.
The other important criteria for choosing a crossover frequency is to choose a low pass filter frequency
at a point at which the dispersion from the driver is wide. Since we can’t equalize the reflected sound in
the car separately from the speaker’s direct sound, it’s helpful in making equalization easy for the direct
sound and the reflected sound to be as similar as possible.
System Design Implications
To better understand this, let’s look at how sounds travels from a speaker.
The plot below is a polar plot for an 8” woofer, which shows the pattern of sound radiation at several
frequencies from 10 Hz through 12 kHz. The closer to the outside of the circle the graph appears, the
louder the sound.
First, look for the small green circle in the middle. That’s 10Hz. The graph of 10 Hz is nearly a perfect
circle and that indicates that the dispersion of sound is equal in all directions—forward, rearward and to
the sides. The circle is small and that indicates that the woofer doesn’t play very loudly at 10 Hz. That’s
to be expected.
Now, look for the red line for 80Hz. The graph of 80 Hz is much farther away from the center of the
circle, which indicates that the woofer plays 80 Hz much louder than it plays 10 Hz. That’s also to be
expected. The shape of the red graph indicates that the sound traveling from the speaker at 80 H also
travels in all directions—forward, rearward and to the sides.
As we move up in the spectrum, we can see that as frequency increases the pattern of sound leaving the
speaker begins to be more and more focused into the forward angles and at the highest frequency in
the graph, 12.8 kHz, the sound is radiated only on-axis sound.

In summary, this graph indicates that at low frequencies, you can hear the sound of the speaker no
matter which way it’s pointed, but at high frequencies, you can only hear the speaker if it’s pointed
directly at you. The transition from wider dispersion (a circular pattern) to narrow dispersion (the lobe at
0 degrees) is a gradual one. This narrowing of dispersion is a rule and it depends almost entirely on the
diameter of the speaker. Dispersion from larger speakers begins to narrow at a lower frequency than
from a smaller speaker.
We can view this same performance characteristic with a standard frequency response graph, too, so
long as we have measurements at several axes. In the frequency response graph of a 6” speaker, below,
the frequency at which the dispersion begins to narrow is evident. The three graphs represent the
frequency response at 0 degrees (red), 30 degrees (blue) and 60 degrees (black). The graphs begin to
diverge at about 2 kHz. Below that the shapes are similar.

Why does this affect our crossover frequency choice in a car (or even in a room)? Because we hear the
on axis sound directly from the speaker and also the off axis sound that’s reflected from all the surfaces
in the car’s interior. Our ears and our brains are able to discern direct from reflected sound, but only if
the reflections arrive much later than the direct sound. That’s how we can tell if we’re in a large space
like a concert hall or a small space like a smaller club. The reflecting surfaces very near the speaker and
very near our ears in a car arrive too soon after the direct sound for us to discern them as separate
events (echoes). Instead, we hear them mostly as frequency response coloration and a broadening of
the image. We still hear the direct sound as the primary location of the sound—the speaker location.
That’s because the direct sound is louder than the reflected sound and the difference in level depends
on the distance to the reflecting surface and then to our ears. Sound is attenuated by 6 dB for every
doubling of distance.
So, let’s say that we have our 8” woofer and a 1” tweeter with a resonance (Fs) of 3 kHz. We need to
cross the tweeter at 1.5 or 2 times the resonance frequency, so we choose 5 kHz. The direct sound is
fine, as you can see in the graphs below. The sum is and flat and that provides good performance
through our 24dB/octave Linkwitz-Riley crossover.

What if we move the microphone to 45 degrees off axis? What does our response look like then?
This matters because the reflected sound includes a big dip at the crossover. Now, our direct sound is
great, but the reflected sound colors the overall frequency response and removes energy from the what
we hear around the crossover point.
The biggest problem caused by this condition is that it makes the system very difficult to tune. The RTA
“hears” and displays the combination of the direct sound and the reflected sound and this is what we’ll
see on the RTA with the microphone in the listening position:
So, our RTA shows us a dip in the response and we “fix” it by adjusting the crossover points or by using
the EQ. If we use the EQ to boost a bit so the measured response is closer to our target curve, this is
what the RTA will show us:

That looks much better—it’s nice and flat and should provide great performance, right? Well, not so
fast. Remember that we hear the direct sound from the speaker a little louder than the reflections and
that direct sound is where we perceive the image. What does the direct sound look like now that we’ve
equalized the total sound? It looks like this:
We hate that. It sounds too bright. It’s “peaky” and fatiguing. Too often, we remove the microphone,
claim that the RTA doesn’t work and that what the RTA displays isn’t what we hear. Then, we finish the
tune by ear. That takes hours and is never quite right because we’re constantly looking for the right
compromise. It’s not the RTA’s fault. It’s our fault because the system design is poor.
The problem is caused by not considering the off axis response of our woofer in the choice of crossover
frequency. Since we hear the direct sound from the speaker and the reflected sound, our poor choice
left a big hole in the reflected sound.
The chart below can serve as a useful guideline for designing systems and selecting crossovers. The
column to the left indicates the diameter of the driver. The graphs at the top of each column indicate
the dispersion pattern of sound from the speaker at the frequencies listed in the column below. Ideally,
we choose a crossover point in the green zone. Yellow is not optimum, but won’t be a big problem.
Orange is worse than yellow and red should be avoided.

So, using the chart above, we can prevent tuning hassles by choosing the right speaker complement. We
have to keep the tweeter safe. Our 24dB/octave Linkwitz Riley crossover helps with that because it
removes low frequency energy from the signal sent to the tweeter really quickly. If we choose a 6”
speaker to go with our 1” tweeter that has a resonance of 3 kHz, we’re in for a bit of trouble. If we cross
the tweeter at 5 kH to keep it safe, then we’re in the red zone and we’re building a big hole in the
response that will be difficult, if not impossible, to tune.
If the 6” speakers are mounted far off axis in the doors, this is going to be an even bigger problem. The
direct sound from the near speaker will include a big hole, and the reflected sound will be flatter. The
sound of the speaker on the opposite side of the car will be the reverse.
If we can find a larger tweeter with a lower resonance frequency, we can move the crossover point
down so that the off- axis sound will be more similar to the on-axis sound. Crossing these speakers over
at 1.5 kHz will be much better, but even a 2 kHz crossover is a big improvement. Aiming the 6” speakers
so that they’re both a little off axis at the listening position will improve symmetry, but that’s a much
more difficult installation.
To make installing and tuning the system even easier, we could consider a 3-way speaker system in the
front. If we add a 2.5” speaker to cover the gap between the woofer and the tweeter, we fix a bunch of
problems. We can cross between the 6” speaker and the smaller midrange below 500 Hz. Now, we don’t
have to aim the midbass driver at all. We can continue to keep our tweeter happy at 5 kHz (and be
between yellow and orange). If we find a tweeter we can cross at 2.5 kHz, then we’re in the green and
we don’t have to aim the midrange either. The off-axis sound will contain the same frequency content
as the direct sound, and we’ve avoided most of the problem highlighted above. A properly designed 3-
way system is often much easier to tune than a 2-way system.

A Note About Systems Without Tweeters:
There’s no magic here. Eliminating the tweeter from the system removes high frequencies from the
reflected sound. Using the dispersion chart above, it’s easy to see that for a 3” midrange, dispersion
begins to narrow at about 3 kHz. Above 3 kHz, the high frequencies from the speaker will be radiated on
axis only. Positioning the midranges so that they point at the listener will maintain high frequency
content in the direct sound and remove it from the reflected sound. You may want to boost high
frequencies a bit with the EQ.
The performance differences between systems with tweeters and those without (so long as the full
range speakers point directly at the listener) will be tighter and more focused images from the
tweeterless system because of less image spread at high frequencies. This tighter focus will come at the
expense of some spaciousness. You may or may not prefer this sound.
Full-range speakers mounted in the dashboard so that they point directly into the windshield can also
work. The on-axis high frequencies will be reflected from the glass and the performance will be more
similar to a system with tweeters. This isn’t better, but in OE systems, it saves the cost of a pair of
tweeters.
Subwoofer and Midbass Crossovers and Getting the Bass Up Front
The illusion of bass in the front of the car depends on a couple of things: the output of the subwoofer
has to be in phase with the output of the front speakers at the crossover and the sub can’t make a
bunch of distortion or rattles.
There are a lot of differing opinions about how to do this and a lot of “rules of thumb”. Some include
delaying the front speakers to get a better phase match at the crossover. Crossing the front speakers
over at absurdly low frequencies or allowing the front speakers to play all the way down to 20 Hz and
using the subwoofer to just enhance the bass are both suggestions that I’ve heard over the years. I’ve
tried them all at various points and none of them work as well as the process that follows here.
Because cars are small spaces, they reinforce bass. We expect to hear more bass in small spaces, so the
target frequency response curve for cars includes about 10dB more bass than midrange and high
frequency content. The amount of bass boost is also a matter of personal preference and can be
adjusted up or down. I suggest starting with about 10 dB of bass boost below 60 Hz.
The target curve for a home audio system in a much larger room doesn’t include this bass boost and
most discussions of crossover settings for subwoofers are written from the perspective of setting
crossovers for bigger rooms. For home audio speakers with a target that is flat from 20 Hz to 20 kHz
using a symmetrical crossover point and symmetrical slopes is a good practice.
The graphs below show the result of a 24 dB/octave crossover with a Linkwitz-Riley alignment and the
delays for the speakers set to correctly compensate for the differing distance from the subwoofer to the
listening position and the distance from the main speakers to the listening position. The resulting
frequency response graph is just as it should be. The crossovers in the graph below have complementary

slopes and complementary phase and they sum flat.
Because this is a 24dB/octave Linkwitz Riley alignment, the subwoofer phase is -180 degrees at the
crossover point of 80 Hz and the front speakers are +180 degrees at the crossover point. The resulting
phase is 0 degrees and that provides the flat frequency response sum.
Since we’re tuning a car and since cars need more bass in order to sound natural, we boost the bass,
which changes the crossover point (we’re using 12dB in this explanation because it makes the math
easy).
Notice that the actual crossover point has moved up to 120 Hz. That may or may not be a problem from
a frequency response perspective because the curve matches our target response pretty well, but from
a phase perspective it’s a big problem. The crossover slopes and the phase of the subwoofer compared
to the front speakers are no longer complementary. That creates an out of phase condition around the
crossover. Just like the phantom center image is degraded when two main speakers aren’t in phase and
we hear the location of each speaker, the poor sum of this crossover makes it easy to hear the location
of the subwoofer and the front speakers.
Since the phase problem is hard to see in the graph above because there’s so much boost at low

frequencies, here’s what it would look like if we crossed the sub at 120 Hz and reduced the level. Now
we can see the cancellation easily.
We can use delay settings to improve this condition by listening to a midbass track and readjusting
delays to improve the phase, but there’s a much simpler way. Because our 12dB/octave bass boost has
raised the crossover point, we can simply set the subwoofer crossover a half an octave below the
midbass crossover.
Now our crossover point is back to 80 Hz and the phase is complementary. The midbass response
doesn’t quite hit our target, but a single band of EQ boost at about 80Hz applied to both the subwoofer
and the front speakers fixes that and maintains the appropriate phase relationship. The bass sounds like
it comes from the front and we don’t have to do any messing around with the delay settings.

Frequency Response and Equalization
Because cars are small spaces, they reinforce bass. We expect to hear more bass in small spaces, so the
target frequency response curve for cars includes about 10dB more bass than midrange and high
frequency content.
The bass boost should transition to flat midrange response between 60 Hz and 160 Hz. This can be
adjusted for personal preference. Some listeners and competition organizations prefer this transition to
extend to 300 Hz or beyond. Extending the transition may provide more impact, but that often comes at
the expense of midrange definition and detail. I suggest the curve below as a starting point.
The high frequency roll-off can also be changed as a matter of preference or system design. If you are
not using tweeters, you’ll want a flatter response at high frequencies due to less high frequency content
in the reflected sound field.
Once you’ve measured from the microphone to the speakers and set the crossovers, the next part of
measuring the system and addressing the issues is to correct the frequency response. The tools for that

are channel level controls and the equalizer. Don’t change the delays. Don’t change the crossover unless
it’s absolutely necessary.
Using Room EQ Wizard and the UMI-1
After following the instructions for setting up the UMI-1 with Room EQ Wizard, download the CSV File
called “Audiofrog Target Curve for REW.csv” and save it to a folder in your computer.
Start REW and click on “File” in the upper left.
Then, click on “Import Frequency Response” in the drop down menu. Navigate to the folder in which
you’ve saved the target curve.

Choose the file and click “Open”. Click “No” when this box opens:
You should see the target curve in the measurement window and the flat part of the response in the
midrange should appear at 0dB.

Now, turn on the system and play the mono pink noise track through the left front speaker and the
subwoofer. The system doesn’t need to play loudly—choose a normal listening level. Click on the RTA
button at the top and you should see the response of your system in the RTA window.
Notice that at the bottom, there’s a check box to display the active measurement and also a check box
for the target curve to the left. Adjust the resolution of the RTA window to show 5dB per division using
the “+” and “-“ buttons in the top left corner of the graph. Also, be sure that “dB” rather than dBFS” is
chosen in the top left corner. Use the scroll bar on the left to center your measurement in the display.
Look for a point in the measurement that’s about halfway between the loudest frequency and the
quietest frequency. For this one, I’m going to choose 75dB.

Now, minimize the RTA screen and go back to the measurement screen. The target curve should appear
in the measurement window.
Click on “All SPL” in the gray boxes just above the graph.
Then, click on the wheel in the upper right to open the controls.

In the controls box, be sure that “Audiofrog Target Curve” is listed in the “Measurement Offsets” box.
Enter the level of the measurement from the RTA screen. Here, I’m entering 75 in the offset box. Then,
click on “Add Offset to Data” in the box to the right.
Next, maximize the RTA window again. It will be in the taskbar at the bottom of your screen, or you can
click on the “RTA” button at the top. After a few seconds and so long as the check box next to
“Audiofrog Target Curve” is checked, the target curve will appear in the RTA display. If you get tired of
waiting, click the box next to “Audiofrog Target Curve” and then click it again. The curve should appear.

Click on the wheel in the upper right to open the control panel.
Check the boxes next to “Use bars on spectrum” and “Use bars on RTA”. Uncheck the boxes next to
“Adjust RTA levels” and “Show phase of harmonics”.
Mode: You can click the down arrow to display the measurement at higher or lower resolution. Choose
“RTA 1/3 octave” for now.
FFT Length: This box controls the actual resolution of the measurement. Choose 16384. That’s plenty of
resolution and this setting should keep even basic computers happy.
Averages: This tells the analyzer how many measurement samples it should take before averaging them
together and displaying the results. Choosing fewer samples will make the display move faster. Choosing
more samples will make the display move more slowly. 16 is good for now.
Window: This allows you to optimize the window depending on the type of stimulus you’re using. For
pink noise, always select “Rectangular”.
Max Overlap: Choose 50% to prevent the measurement sequence from overloading the computer as it
processes the measurements.

Update Interval: This tells the analyzer how often to update the display. Choosing 1 updates the display
for every block of data. Choosing 4 updates every 4 blocks. Choose 2 to keep the computer running
happily.
You can leave the control window open or you can close it by clicking on the wheel again. If you leave it
open, you should see something like this in the RTA window:
If the horizontal scale at the bottom isn’t 20Hz-20kHz, click on the Graph Limits button next to the wheel
and set the limits by typing into the boxes. You can use this box to reset the display at any time.
If the target curve doesn’t appear in between the highest peak and the lowest point of your
measurement, or if you want to adjust it, you can go back to the “ALL SPL” screen and increase or
decrease the offset or you can adjust the level of the system in the car using the volume control. Once
you set the volume control, don’t change it until all of the level setting and equalization is complete.
Now we’re ready to begin matching our measured response to the target curve.

In the 3-way front speaker system we’re going to optimize in this example, the crossover between the
midrange and the tweeter is 2.2 kHz. The crossover between the midrange and the midbass is 300 Hz.
The high pass filter for the midbass is 80 Hz and the subwoofer low pass filter is at 60 Hz. The delays
have been set using the tape measure and all of the electrical polarity has been confirmed. All of the
crossovers are LR4 types.
Looking from left to right, we can see that we need more low frequency energy (20-35 Hz) to meet the
target. We also need a little more 50 Hz to 90 Hz. We need a little less midbass between 200 Hz and 300
Hz. We’ll need to eliminate the giant peak at 500 H and the smaller and narrower peak at about 1.6 kHz.
We need a lot more output from our tweeter everywhere except about 14 kHz.
We’ll start by increasing the level of the output to the subwoofer amplifier by about 3.5 dB. Now, we’re
pretty closely matched at 60 Hz. We have a little too much bass at 40-50 Hz. Midbass between 100 and
160 Hz looks about right.

Moving to the right, and thinking about the level of the midrange, we can see that at between 300 Hz
and 2 kHz, we have a couple of big peaks to remove, but at the base of the big peaks, the level is about
right. We’ll leave the midrange level control alone.
Above 2 kHz, we don’t have enough tweeter level. We’ll turn up the level of the tweeter channel on this
side by about 6 dB to get closer to the target curve.
Now, we’ve about as close as we’re going to get to the target curve using just the level controls for the
individual channels and we’ll use our equalizer to finish the job.
There are a couple of different kinds of equalizers you may have available: graphic and parametric.
These may be configured in your DSP so that you have one equalizer per output channel or you may
have one equalizer for all of the front speakers. This process assumes that you have a separate equalizer
for left and right. If you don’t, this process isn’t going to work very well and I suggest considering a
different processor.

If you have a single graphic EQ for the entire channel (subwoofer, midbass, midrange and tweeter), then
this process is pretty easy. Your EQ might look something like this:
We just need to adjust the sliders to remove the peaks and fill in the small dips, like this:
We’re not trying to draw a smooth curve on the equalizer, we’re using the individual bands on the
equalizer to match the measurement to the target.
In a graphic equalizer, adjusting one slider will often adjust several adjacent bands on the display. You
may have to turn one up and the two adjacent ones down in order to target a specific frequency. In
some cases, you may not be able to fix every problem with a graphic EQ, but you should be able to get
close. That’s the case with the original peak at 1.6 kHz in this measurement. Reducing the slider at 1.6
kHz also reduced the level at 1.25 kHz and at 2 kHz. I’ve boosted both of those a little in order to achieve
the best compromise possible. With this tool I can’t get any closer.
If you have a separate 31 band EQ for each of the output channels, then fixing problems that occur near
crossover frequencies is a little more difficult. You can try making the same adjustments in both
equalizers. If that isn’t straightforward, mute one output and then the other to determine which

speaker is contributing most to the problem and address the problem accordingly. Be careful about
boosting too much near the crossover in the channel that has the high pass filter. That will potentially
damage the speaker if your EQ settings provide too much power. Boost the low pass channel a bit
instead.
If you have a parametric equalizer, the overall process is similar, but the tools are a little different. A
parametric EQ has two controls in addition to a boost/cut control you’ll use in a graphic EQ. Those two
additional controls are a frequency control and a Q control. The frequency control allows you to
precisely target a problem frequency. The Q control allows you to adjust the number of adjacent
analysis bands are affected by allowing you to adjust the width of the boost or cut that you apply.
For this single band of parametric EQ, I’ve selected a frequency of 1 kHz, a cut of 10 dB and a Q of 1.
A lower Q makes the filter wider, affecting more adjacent bands. Here is a Q of 0.5.

And finally, I’ve selected a Q of 10. The filter is much narrower—it affects fewer adjacent bands.
It should be evident that this is much more powerful than the graphic EQ because it allows the user to
fix wide peaks and dips with a single band of EQ, rather than adjusting several sliders. The user can also
target a problem that’s narrower than a single slider on a graphic EQ will allow—as was the case with
the peak at 1.6 kHz in our measurement.
Many of the parametric EQ interfaces in today’s DSPs will allow you to click and drag to set the filter
frequency and to pinch or drag some handles to adjust the Q. If that’s convenient for you, then you can
use the graphic UI to do the work.
With some practice, and if the EQ includes text entry boxes, there’s a faster way. Choosing the filter
frequency and the amount of boost or cut should be pretty straightforward. You can read that directly
from the RTA screen. Let’s look at our wide peak in the midrange in our system, as an example:

if you click on the display at the top of the peak, REW will display a cross hatch and in the blue boxes,
the program will tell you the frequency and the level. So, in the example above, we can see that the
peak in our response is about 500 Hz. We can also see that the level of the peak is 11.6 dB higher than
our target level of 75 dB. So, in our text entry box for our filter, we can enter 500 H for the frequency
and -11.6 dB for the amount of cut.
But what about Q? You can pinch or drag some handles until your correction filter fits and you match
the target curve, or you can use a little math to get started.
Q = Frequency / Bandwidth
We already know the frequency—500 Hz. To find the bandwidth, we need to find the points on either
side of the peak where the response is 3 dB lower. We can use REW to help. Click on the control wheel
in the top right and change the mode setting to 1/12 octave. Don’t worry about the target, for now.
Now, we can see the peak a little more clearly. Move the cursor to the center frequency if it now
appears slightly to the left orf to the right. I’ve moved it to 474 Hz. Notice that the level at that peak is
81 dB. We’re looking for the point to the left and to the right at which the level is 3 dB lower—78 dB.
Move you’re the cursor to the left until you see 78dB and read the frequency. In this case, it’s 398 Hz.

Then, move the cursor to the right and do the same thing. This time, it’s 571 Hz.
Bandwidth is the higher frequency at which the level is down by 3 dB minus the lower frequency at
which the level is down by 3 dB. In this case,
Bandwidth = 571-398 = 173
Q = 474/173 = 2.73
So, in our text boxes, we type 474 Hz for the frequency, -11.6 dB for the boost/cut and 2.73 for the Q.
In the control window in REW, go back to 1/3 octave and view the result.

That gets us pretty close. Now we can just adjust the level and the Q a little bit. I’ve changed the level to
-12 dB and the Q to 1.9 to arrive at the result below.
Next, we can apply a single band at 1.6 kHz to get rid of that peak. We know that the Q of this filter
should be high, so we’ll try 10.

Now, that peak is gone. Let’s work on the high frequencies a bit. Let’s try a filter at 10 kHz with a cut of
-4.5 dB and a Q of 1.4.
Finally, another filter at about 15 kHz with a cut of -4 dB and a Q of 1.4 should do it.

We can go on using additional bands to finish smoothing the curve.
Now, the left side is done. We can click “Save” in the top center of the window to store the left channel.

Then, we can turn off the left side, and use the same process to match the right side to the left side.
Once they match closely, we’re done.
If one channel plays louder than the other at some frequency or range of frequencies, that will cause the
image at that frequency to move toward the louder channel. If there’s a dip on one side that you can’t
fix with the EQ, put a matching dip in the other side. This will degrade the frequency response a little bit,
but it will preserve your center image. Matching the channels within a couple of dB is sufficient. If you
have more time, keep working until they match exactly.
Once you have the channels matched, turn them both on. What you see in the RTA screen now will be
the frequency response of the center image. Resist the urge to equalize with both channels playing, but
look for big dips in the response that don’t occur when only one channel is playing. These dips, if there
are any, are phase problems and unless they are caused by an error in your delay settings, you can’t fix
them. If there’s a big peak (more than 6dB), you can remove it by equalizing both channels equally.
If you see something that looks like this, go back and check your delay settings. There’s a good chance
that they’re incorrect.

Once you’ve confirmed that there are no big errors in the response with both the left and the right
channels playing at the same time, turn off the pink noise and remove the microphone from the car. Put
away the tape measure and turn off the RTA.
Confirming the Performance
Using the Audiofrog Stereo Tuning CD (and not your favorite song), listen to the bandwidth limited pink
noise in tracks 2-5. The pink noise should seem to come from a point in between the two front speakers
and not from either the right or the left speaker. Don’t focus too much on the exact placement. The high
frequency pink noise in track 5 will be more spread out between the left and the right speakers. That’s
OK.
Next, use tracks 6-10 to check that the pink noise moves across the dashboard evenly. Check the center
placement of the pink noise in track 8. It should seem to come from a point halfway in between the left
and right speakers-in the center of the dashboard. If it seems to be off center, make a mental note, but
don’t adjust anything. If you hear the pink noise come mostly from one channel or the other, you’ve
probably input the delays incorrectly. Go back and check.
Next use tracks 11-15. The bass guitar should be located entirely in the front of the car and it should
move evenly from left to right. The bass guitar in track 12 should be halfway between the left speaker
and the center of the dashboard. The bass guitar in track 13 should be in the center of the dashboard.
The bass guitar in track 14 should be halfway between the center of the dashboard and the right
speaker. If the guitar is too far to the left, reduce the levels of the entire left channel (subwoofer, if
there are two channels of input to the sub amp, midbass, midrange and tweeters) slightly until it moves
to the center. If the bass guitar is too far right, reduce the levels of all of the right channel speakers until
it appears in the center of the dashboard.
Finally, use the piano in tracks to 16-20 to check the placement of the high frequencies. The sound of
the piano should be more spread out than the sound of the bass guitar. If the center placement of the
piano is way off, go back and check the frequency response match of the left and right channel with the

RTA. If they don’t match, adjust the EQ so they do.
Do not adjust the delay settings to move the image if you’ve set them correctly with the tape measure.
Delay corrects for distance, it’s not an image panning tool. That’s what level controls are for.
Chances are, if you’ve followed these steps, you may only have to adjust the level of the channels
slightly to center the image.
If you prefer the center image to be directly in front of you, turn the levels of the far side speakers down
by 6dB, including the sub, if your sub amplifier has two inputs from the DSP. A 6dB adjustment should
move the center image to a point halfway in between the center of the dashboard and the left channel.
If the sound of the bass isn’t in the front of the car, check the transition region between 60 Hz and 160
Hz. Be sure there are no big dips in the response. Reduce the level of the subwoofer slightly until the
bass moves to the front. If that doesn’t work to move the bass to the front, then listen to track 25 and
delay all of the front speakers gradually and by exactly the same amount until the bass moves to the
front. This should be done only as a last resort.
Noise
Finally, listen to track 38. It’s an empty track. Check for noise. If you hear a hissing sound that you can’t
live with, turn all the channel levels or all of the gain controls in the system down by the same amount
until it’s gone. If you don’t hear a hissing noise and you’d like the system to play louder, turn all the level
controls up until you hear a hiss and then turn them down slightly.
Adjustments for Personal Preference
If you like a little more or less bass, a little more or less midrange or a little more or less high frequency,
adjust the target curve to reflect those preferences.
Adding a lot more bass will make creating an illusion of bass in the front of the car more difficult.
Changing the transition region from bass to midrange may add some impact, but it may come at the
expense of midrange detail. If you like more high frequency content, adjust the downward tilt at high
frequency so it ends at -3 dB at 20 kHz instead of -6dB. If you aren’t using tweeters in your system,
eliminate the downward tilt altogether.
None of these adjustments will affect the process, they just call for a different target curve for
equalization.
In Conclusion
This process is designed to prevent back- tracking and interminable adjustments made using subjective
analysis. Resist the urge to insert some other tips and tricks that you may have learned over the years. In
many cases, those tips and tricks were developed before DSPs were available and before channel delay
adjustments were commonly available. Many of those tips and tricks break this process.

If this process isn’t the one you use currently, try it just as it’s explained here. With a little practice, you
may find that it’s quicker, provides better results and is more predictable than other processes you may
have tried.
Happy Tuning! —oops—Happy measuring the performance of the system and addressing the issues.
--Andy
