Title: Video Encoding for the Web in 2016
Date: 2016-07-21 17:42
Category: Video
Tags: ffmpeg, H.264, VP8, VP9
Slug: video-encoding-for-the-web-in-2016
Author: Alan Orth
Summary: Understanding video encoding technology is like trying to hit a moving target. I spent time reading the ffmpeg docs and decided you should use VP9!

Understanding the tools and technology related to video encoding is like trying to hit a moving target — every few years the scene changes entirely and you have to learn all the latest best practices over again. I recently spent more time than I should have preparing a video of [some tanks rolling down the street near my house](https://englishbulgaria.net/2016/05/tanks-rolling-streets-sofia/) and figured I'd compile my notes into a sort of guide so that someone else could benefit as well.

<abbr title="Too long, didn't read">TL;DR</abbr>: Use VP9 with Vorbis audio and fall back to H.264 for Apple devices and corner cases. Read on for code snippets and rationale.

## VP9

VP9 is the newer of two related open and royalty-free video codecs developed by Google. It delivers seriously impressive quality at very low file sizes, but takes _fucking forever_ to encode. At this point in time there is [pretty good support of VP9 in web browsers](http://caniuse.com/#feat=webm), though generally not [hardware accelerated](http://wiki.webmproject.org/hardware/socs). The following is a two-pass encode using the "constrained quality" mode from the [WebM VP9 encoding guide](http://wiki.webmproject.org/ffmpeg/vp9-encoding-guide):

```
$ ffmpeg -i input.mp4 -c:v libvpx-vp9 -pass 1 -b:v 1400K -crf 23 -threads 4 -speed 4 -tile-columns 6 -frame-parallel 1 -an -f webm /dev/null
$ ffmpeg -i input.mp4 -c:v libvpx-vp9 -pass 2 -b:v 1400K -crf 23 -threads 4 -speed 2 -tile-columns 6 -frame-parallel 1 -auto-alt-ref 1 -lag-in-frames 25 -c:a libvorbis -f webm output.webm
```

The constrained quality mode gives you more control over the target bitrate. If you want higher quality, bump up the bitrate or reduce the CRF value a bit. Pay attention to the `threads` option and adjust for how many CPU cores your computer has. Also note that I'm encoding the audio with the older `vorbis` codec because [`opus` isn't well supported yet](http://caniuse.com/#feat=opus). You can read more about the other options on the [ffmpeg VP9 encoding guide](https://trac.ffmpeg.org/wiki/Encode/VP9).

For reference, these two passes took 206 and 2419 seconds to complete respectively, and the file size of the resulting video was 3.2 megabytes. The VP9 encoder seems to be able to use multiple CPU cores, but I only noticed them being used in the second pass.

## H.264

H.264 is a slightly older video codec that delivers good quality at small file sizes, is [supported almost everywhere](http://caniuse.com/#search=h.264), and often has hardware-accelerated decoding which is good for battery life on mobile devices. There's one massive caveat, though: H.264 is [patent encumbered](http://en.swpat.org/wiki/MPEG_LA) and requires paying license fees if you want to show the video to anyone other than your cat.

In any case, the following will produce a video with decent quality that is playable on basically any device on the planet right now:

```
$ ffmpeg -i input.mp4 -movflags +faststart -c:a aac -c:v libx264 -preset veryslow -b:v 2000k -profile:v baseline -level 3.0 output.mp4
```

Note the adherence to the baseline profile at level 3.0, which the [Android developer docs](https://developer.android.com/guide/appendix/media-formats.html#recommendations) recommend for compatibility with current Android devices. If you only need to support Apple devices then you can target a higher profile, which will allow the encoder to use more of H.264's advanced features — read about that and more on the [ffmpeg H.264 encoding guide](https://trac.ffmpeg.org/wiki/Encode/H.264).

Software patents and licensing issues aside, H.264 is actually very impressive. The encoder is fast on multi-core CPUs, video quality is great, and file sizes are low for the standards we had five to ten years ago. For reference, this encode took 132 seconds and the resulting file size was 4.5 megabytes.

## VP8

VP8 is the older of Google's two open and royalty-free video codecs. It is a contemporary of H.264 and provides decent video quality at relatively low file sizes. Sadly, in retrospect, I think VP8 might have been too little, too late (but that's water under the bridge, and we have VP9 now).

If you find yourself needing to target older Android or something where VP9 isn't supported, then this one-liner from the [ffmpeg VP8 encoding guide](https://trac.ffmpeg.org/wiki/Encode/VP8) will do the trick:

```
$ ffmpeg -i input.mp4 -c:v libvpx -qmin 0 -qmax 50 -crf 5 -b:v 2000k -c:a libvorbis output.webm
```
In this example it's worth noting that 2000 kilobits/sec is the "target bitrate," but the effective bitrate ended up being about 3000k because I enabled "constant quality" mode by specifying the crf, qmin, and qmax options. Also, VP8 apparently supports multi-threaded encoding, but in my tests it was actually _slower_ and produced a larger file! This single-threaded encode took 691 seconds and the resulting file size was 5.1 megabytes.

## For the Love of the Open Web: Use VP9

Ten years ago you didn't really have much of a choice for video codec providing both very high quality and low file sizes. H.264 came on the scene and set the bar very high with a fast encoder, amazing video quality, and fantastic hardware and software support. VP8 was an honest attempt to bring an open royalty-free and high-quality video codec to the market but it never really stood a chance.

The good news is that we have VP9 now. The bad news is that the successor to H.264 — H.265 aka "HEVC" — is almost as impressive as H.264 was ten years ago (minus the fast encoder and install base), but the patent pool representing it has [announced more aggressive royalty terms](http://blog.streamingmedia.com/2015/07/new-patent-pool-wants-share-of-revenue-from-content-owners.html) for using it. I think this time is different, though, as you can already [play VP9 in any major web browser](http://caniuse.com/#feat=webm), and video streaming sites like [YouTube have content available in VP9](https://youtube-eng.blogspot.bg/2015/04/vp9-faster-better-buffer-free-youtube.html). Ubiquitous hardware-accelerated decoding of VP9 would be nice, but it's not a deal breaker (I was decoding DivX in software like a hundred years ago and I never complained!).

So, for the love of the open web: use VP9! Maybe the 2017 or 2018 edition of this blog post will recommend [Daala](https://wiki.xiph.org/Daala)?

### Technical Notes

I was using ffmpeg version 3.1.1 on a 2015 MacBook Pro with a dual-core [2.7 GHz Core i5 (I5-5257U)](http://ark.intel.com/products/84985/Intel-Core-i5-5257U-Processor-3M-Cache-up-to-3_10-GHz) processor. Now that I think about it I should run the VP9 encode again with two threads instead of four, as I only realized just now that my processor was dual core. :)

This was [originally posted](https://mjanja.ch/2016/07/video-encoding-for-the-web-in-2016/) on my personal blog; re-posted here for posterity.
