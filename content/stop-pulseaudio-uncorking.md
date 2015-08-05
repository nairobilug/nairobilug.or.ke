Title: Stop Skype and PulseAudio from "uncorking" media players
Date: 2015-08-02 15:21
Category: Linux
Tags: linux, pulseaudio, skype, nsa
Slug: stop-pulseaudio-uncorking
Author: Alan Orth
Summary: Stop Skype from interrupting your media player when chat events fire

PulseAudio has a neat feature that allows applications to "uncork" media players like Rhythmbox, Banshee, etc when certain events happen. For example: when a call comes in Skype pauses your music so you can answer without fiddling around to pause manually. Unfortunately Skype also deems the "contact coming online" and "contact going offline" events as worthy of uncorking, so your music gets interrupted for several seconds when these events fire (aka all the time).

## Unload the "cork" module
A short term solution is to unload the corking module from your user's PulseAudio session:

```
$ pactl unload-module module-role-cork
```

That will take effect immediately for the remainder of the current user's session. A more permanent solution would be to comment out the loading of the "cork" module in PulseAudio's configuration file.

*/etc/pulse/default.pa*:

```
### Cork music/video streams when a phone stream is active
#load-module module-role-cork
```

## Other annoyances
Now if only there were a way to address some other Skype annoyances like requiring the installation of a bunch of 32-bit libraries or how chat windows hijack the desktop environment's alt-tab ordering when there is a new message. Oh, it would also be nice if there wasn't massive, gaping [backdoor giving the NSA access to your chats](http://www.theguardian.com/world/2013/jul/11/microsoft-nsa-collaboration-user-data). _\*sigh\*_

This was [originally posted](https://mjanja.ch/2015/08/stop-skype-and-pulseaudio-from-uncorking-media-players/) on my personal blog; re-posted here for posterity.
