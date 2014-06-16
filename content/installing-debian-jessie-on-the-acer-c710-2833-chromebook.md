Title: Installing Debian Jessie on the Acer C710-2833 Chromebook
Date: 2014-03-19 19:15
Category: Tech
Tags: hardware, Chromebook, Debian
Slug: installing-debian-jessie-on-the-acer-c710-2833-chromebook
Author: Muriithi Frederick Muriuki
Summary: Making my 'new' chromebook useful

## Introduction

Hey there.

I have recently had need to get a machine for work that is easy to lug around, affordable and has a decent battery life. While I already have a laptop (Presario CQ62), it has grown old and its battery life is in the shitter.

After shopping around, I settled for the Acer C710-2833 Chromebook (I would have picked a newer model, but there is not one in our market yet, and importing one would have made it quickly unaffordable - thank the new government).

Now, while Chrome OS - the operating system that comes with the machines - is a nice (great?) operating system, for a freelance developer like me, it renders the machine useless for much of my day to day work. I found the need therefore to make it useful for me.

## Preparation

**DISCLAIMER**: FROM THIS POINT FORWARD, ANYTHING YOU DO WITH YOUR MACHINE IS YOUR FAULT. IF IT BREAKS, OR YOU BRICK IT, OR CAUSE A NUCLEAR HOLOCAUST, OR ANYTHING ELSE FOR THAT MATTER, YOU CAN ONLY BLAME YOURSELF.

Now that that is out of the way, shall we proceed.

First off, let us start with where you can acquire the machine in Kenya. I got my machine at Ebrahim Electronics Limited along Kimathi Street. The machine costs a whooping Kshs 19,000. Also, do not forget to carry the manuals with you like I did.

I would recommend you also get yourself a flash-disk at this point.

So now you have your spanking new machine. Make sure to claim your free 100GB storage on google drive before you proceed. Also, BACKUP any user data you might have put on the machine

## Reading Material

The process that is involved is tricky, and while I try to give a roadmap, I will not give the instructions, rather, I will point to the various resources I found useful

SERIOUSLY, DO NOT JUST JUMP IN AND START COPYING AND PASTING COMMANDS! YOU WILL BRICK YOUR MACHINE. YOU HAVE BEEN WARNED.

### Getting to Developer Mode

The chromebooks have two modes:

* Normal user mode
* Developer mode

Read [this](http://www.chromium.org/chromium-os/chromiumos-design-docs/developer-mode), and [this](http://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/acer-c7-chromebook) for more information on developer mode

### CoreBoot

These links are about coreboot. PLEASE READ THROUGH THEM A COUPLE OF TIMES before attempting anything
For an introduction to coreboot see [here](https://johnlewis.ie/mediawiki/index.php?title=Coreboot_on_Chromebooks).

[Here](http://johnlewis.ie/coreboot-on-chromebooks/pre-built-firmware/) you can find a list of the existing coreboot firmware. DO NOT RUSH JUST YET. Read on.

##Installing

### Getting the ISO

We now need to download an iso image to use as the installation source. It is important that you research and figure out what processor your machine uses. For the C710-2833, it uses the [Intel Celeron 847](http://ark.intel.com/products/56056/Intel-Celeron-Processor-847-2M-Cache-1_10-GHz). This is an x86_64 architecture, otherwise known as amd64.

Armed with that knowledge, get to [http://www.debian.org](http://www.debian.org/) and get the relevant image.

At this time, it is recommended that you get Debian Jessie [here](http://www.debian.org/devel/debian-installer/)

### Ready To Go

Now, you have read up on coreboot, you have the image all that remains is the process.

Start off [here](https://wiki.debian.org/InstallingDebianOn/Acer/C710-2615-Chromebook) - you will get some information on the current status of your machine. It is also where you will finish your journey.

Once you have read through that at least twice, now start the actual installation. The process to follow is [here](https://johnlewis.ie/mediawiki/index.php?title=Flashing_stock_firmware_to_a_coreboot_build_on_Acer_C7_%28C710%29)

For the core boot, I used the 'Grub2 for Intel Celeron 847' with an md5 sum of `9c5993518ddf97ab4c4cf7e0a2f84570`. I picked it because I have used grub2 before and felt comfortable starting off in a farmiliar place. You are welcome to try a different one if you know what you are doing.

If you follow the instructions carefully, you should get through without problems.

### Finally

Now you have Debian on your system, it is time to do the post-installation steps. As I told you, those are found on the page you [started off with](https://wiki.debian.org/InstallingDebianOn/Acer/C710-2615-Chromebook).

Great! Now go ye and be productive!

---

## EDITS

April 21, 2014: Sometimes the trackpad does not work - to correct that, you could do the following (from [marstella.net](http://marstella.net/?p=278) also, thanks to eebrah)

1. Edit `/etc/modprobe.d/blacklist.conf` and include the following line

        blacklist chromeos_laptop

2. Edit `/etc/modules` and include the following lines:

        i2c-i801
        i2c-dev
        chromeos_laptop
        cyapa
