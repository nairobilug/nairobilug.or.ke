Title: BRCK in violation of the GPL
Date: 2015-05-18 15:21
Category: Licensing
Tags: licensing, gpl
Slug: brck-violating-gpl
Author: Alan Orth
Summary: BRCK is distributing binaries derived from GPL-licensed programs and fails to comply with the copyleft obligations of the license.

During a recent meeting of the Nairobi GNU/Linux Users Group we discussed [BRCK](https://www.brck.com "BRCK | Rugged, Portable WiFi Hotspot & Battery Extender"), the Kenya-based makers of a slick, "rugged", battery-powered-GSM-router thing of the same name, and their apparent violation of the GNU General
Public License (GPL). The lively discussion ended up making its way to the web in the form of a [blog
post](https://nairobilug.or.ke/2015/05/meetup-may-2015.html) on the group's blog.

Their product is based on [OpenWRT](https://openwrt.org/) — the GNU/Linux distribution geared towards embedded systems — which is [licensed](http://wiki.openwrt.org/about/license) under the GPL v2. I believe this is problematic for BRCK for a number of reasons that I will enumerate below. When we reached out to BRCK they claimed that they were not in violation because they use "stock unmodified OpenWRT" source code. This claim is repeated verbatim in a [thread on their forum](http://forums.brck.com/t/where-is-the-openwrt-fork-source-at/482/8).

I had intended this post to be a discussion of the spirit of the GPL ending with me expressing disappointment in BRCK for cowering behind perceived technicalities of the license. After sitting down to read the license, however, it became immediately apparent to me that they are indeed in violation. *\*sigh\**

## The GNU General Public License

I'll save the discussion about the spirit of the GPL for later, but here's the gist:

> [...] if you distribute copies of such a program, whether gratis or
> for a fee, you must give the recipients all the rights that you have.
> You must make sure that they, too, receive or can get the source code.
> And you must show them these terms so they know their rights.

That's from the preamble of the [GPL Version 2](https://www.gnu.org/licenses/gpl2.txt). The license goes on to outline the terms and conditions for copying, distribution and modification.

After several readings of the text it is my opinion that BRCK is *in violation of Sections 1, 2, and 3* of the GPL v2 and that *their rights to distribute OpenWRT-derived works should be terminated under Section 4*.

My analysis follows.

### Section 1

Section 1 deals with the distribution of source code. Specifically:

> You may copy and distribute verbatim copies of the Program's source
> code as you receive it, in any medium, provided that you conspicuously
> and appropriately publish on each copy an appropriate copyright notice
> and disclaimer of warranty; keep intact all the notices that refer to
> this License and to the absence of any warranty; and give any other
> recipients of the Program a copy of this License along with the
> Program.

This is very important because compliance with Section 1 is required by subsequent Sections of the license. Use of the language "*may copy*" merely grants BRCK the permission to distribute program source code which is explicitly required by Sections 2 and 3. In addition, Section 1 states that the copyright notice and license from the original work must be preserved.

While BRCK does not provide source code for their work, they do offer public [downloads of their firmware binaries](https://www.brck.com/firmware/). Unfortunately there is neither a `LICENSE.txt` file nor any mention of the the GPL in the archive provided:

    $ ls -l brckv1_20141114.zip
    -rw-r----- 1 aorth staff 5547580 May 17 14:01 brckv1_20141114.zip
    $ shasum brckv1_20141114.zip
    d6dcbb1d61e99bf2b35133c5e6897a352518da0c  brckv1_20141114.zip
    $ unzip brckv1_20141114.zip
    $ grep -r -E 'gpl|GPL' brckv1_20141114/* | wc -l
           0

`brckv1_20141114.zip` was retrieved on May 17, 2015 and had the file size and SHA1 fingerprint shown above.

### Section 2

Section 2 deals with modifications to the program. Specifically:

> a) You must cause the modified files to carry prominent notices
> stating that you changed the files and the date of any change.

At first this Section doesn't seem to apply, as BRCK claims to be using "stock unmodified OpenWRT", but I find their claim dubious for two reasons:

1.  The OpenWRT project doesn't provide source code producing firmware for any device called "BRCK", so it is unclear from which source code the firmware builds are created.
2.  BRCK themselves allude to "optimizing" for a 4MB image size, which implies modification.

Nevertheless, if BRCK does indeed use "stock unmodified OpenWRT" source code then the [Linux kernel's GPL v2 compliance guide](https://www.kernel.org/doc/pending/gplv2-howto.html) suggests:

> The minimum sufficient answer includes the version number, whether or
> not it was modified, and where we can get it from. I.E. something
> like: "We used Linux 2.6.22.4, from www.kernel.org, and we didn't
> modify it." If you didn't modify a package, say so. Even when you used
> unmodified source code, the GPL requires you to \_identify\_ the
> source code you used, clearly and explicitly, at least in response to
> direct questions about it.

One [popular interpretation](https://copyleft.org/guide/comprehensive-gpl-guidech6.html) of the GPL v2 states that Section 2 "*[...] seeks to ensure that those receiving modified versions know the history of changes to the software.*"

As BRCK neither publishes the corresponding source code for their modified binaries, nor explicitly states the exact "unmodified" versions used, they are in clear violation of Section 2.

### Section 3

Section 3 deals with the distribution of derived works in object code or executable form. Specifically:

> a) Accompany it with the complete corresponding machine-readable
> source code, which must be distributed under the terms of Sections 1
> and 2 above

It goes on to state:

> For an executable work, complete source code means all the source code
> for all modules it contains, plus any associated interface definition
> files, plus the scripts used to control compilation and installation
> of the executable.

Not only does BRCK need to provide the complete source code for their OpenWRT-derived work itself, they need to provide the bits used to produce their firmware builds *from* that source code.

### Sections 4 and 5

Section 5 stipulates implicit acceptance of the license terms upon distribution of the work, and Section 4 is crystal clear on the termination of the rights in case of non-compliance:

> 4. You may not copy, modify, sublicense, or distribute the Program
> except as expressly provided under this License. Any attempt otherwise
> to copy, modify, sublicense or distribute the Program is void, and
> will automatically terminate your rights under this License. [...]

By my reading this means BRCK's rights to distribute OpenWRT-derived works are void.

## Compliance

Interpretation of the license is a bit confusing at first, but very accessible if you actually read it. Put simply: copyleft obligations of the GPL v2 are triggered upon *distribution* of binary works derived from a GPL-licensed program.

As BRCK is distributing an OpenWRT-derived work in object code form, Section 3 requires that they provide *complete corresponding machine-readable source code* used to produce the object code they are distributing. Section 1 grants them the permission to provide this code and stipulates that it must preserve the copyright notice and license of the original work.

The implications of Section 2 are less clear, depending on whether or not BRCK is actually using "stock unmodified OpenWRT" source code. I suppose that's up to them to decide, but I would urge them to keep in mind the spirit of the GPL v2 when making that decision.

## BRCK should know better

BRCK is not the "enemy", but they — of all people — should know better. We expect this behavior from large corporations, but not from quasi-community-based organizations operating in the technical sector.

In the end none of this matters unless someone is willing to take BRCK to court over non-compliance. Even if someone was willing to do so, I think it would be sad if it had to come to that. Instead, I hope this serves as a lesson in GPL v2 compliance for Kenyan organizations in the future, and indeed a public record of my findings.

**Update (2015-05-19):** BRCK has [responded](http://forums.brck.com/t/where-is-the-openwrt-fork-source-at/482/11) and posted [licensing information and source code](https://www.brck.com/open-source-compliance/) on their website.

This was [originally posted](https://mjanja.ch/2015/05/brck-in-violation-of-the-gpl/) on my personal blog; re-posted here for posterity.
