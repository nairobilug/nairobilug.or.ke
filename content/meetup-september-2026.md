Title:SN1 EPS2 Onlinug
Date: 2026-09-05 15:00  
Category: meetups  
Tags: meetups, Nairobilug, RTOS, IPC, android, omarchy, linux 
Slug: meetup-september-2026  
Authors: Steve Nyasimi, Paul Mayero
Summary: Meetup locations, Interprocess communication on same board, from linux kernel contributions to confidential computing at Microsoft, developer worlflow using AI-agents, Your android device is vulnerable! 


# Hey, You there, I've got tricks

Yes, pretty neat tricks for a developer who wants to maximize resource utilization on an embedded device, patching the linux kernel? boost productivity on your laravel developmet ENV? or breaking into an android phone? No problemo, I've got you. 

Nairobi linux user group, that's the secret sauce.. Who are we? *avengers, cough cough*. We are a lively community of FOSS enjoyers, from OS' to software tools and anything cool or fascinating. We usually meet on the first Saturday of every month. Let me brief you on what went down on the previous meet-up.
> *scene*
In part two of our online series, we had amazing speakers talking about interesting topics, topics that left you flipping bits. The lineup was packed with interesting topics, with one standing out: Dorcas, our first female speaker. The line up;

- "[Meet up locations](#meet-up-locations)" By Benson Muite
- "[Hello IPC](#hello-ipc)" by Chrispine Tinega 
- "[From kernel contributions to confidential computing](#from-kernel-contributions-to-confidential-computing)" by Dorcas Litunya 
- "[Optimizing developer workflow with AI and Omarchy](#Optimizing-developer-productivity-with-AI-agents-and-Omarchy)" by Norman Bii 
- "[Hacking android](#hacking-android)" by Danfold Mosongo 

## Meet up locations

Without you, there's no NaiLUG, To make physical meet ups a success, Nailug has had some awesome contributors who help with securing venues and making the event happen. We appreciate you :heart: . We also thank you; community members attendies, visitors and fresh souls who have joined us. For always showing up for the events.

> *Without you guys, there's no NaiLUG*

Benson Muite, who was our first speaker. Has really helped us find a venue. He also researched on cool places where the Nailug community can and will be able to host meet-ups. Since we are a community, hosting these events at these locations, will help the community to give back and grow the community. Benson has been able to scout and visit the different places, He's been able to curate a list of possible locations that we can host the events and he has shared with us. You can check them them out in this [pull request](https://github.com/nairobilug/nairobilug.or.ke/pull/239/changes). Feel free to add on the list or leave a comment. 

Thank you Benson, we appreciate the efforts, God bless you. :heart: .


## Hello IPC

Chrispine Tinega,who's an embedded developer for energy applications and a zephyr contributor/maintainer, took us through on how to make two processes running on different platforms and cores within the same board communicate through Interprocess communication using shared memory.  
To understand why we need this, we need to see which problem this will solve, [zephyr](https://docs.zephyrproject.org/latest/introduction/index.html) a Real time operating system and [Linux](https://en.wikipedia.org/wiki/Linux) a general purpose OS fails at performing tasks that require a degree of determinism that only an RTOS can solve, and an RTOS can be lacking some functionality that a general purpose OS offers, for instance a nework stack. To get the best of both worlds in an embedded device, you can have one core running your linux and another core running RTOS like zephyr and have applications running in these cores communicate using a form of IPC such as shared memory.  

To demonstrate this Chrispine made use of the AM62X_M4_BL350 board which supports

- 4x Cortex - A53@164GHz - Where linux will be installed
- 1x cortex - M4F@400MHz - where zephyr will be installed
- Shared memory region 1MB 

You can read more on [AM62X_M4_BL350 board](https://docs.zephyrproject.org/latest/boards/bliiot/am62x_m4_bl350/doc/index.html)

![AM62X M4 BL350 board](./images/meetup-september-2026/am62x_m4_bl350.webp "AM62X M4 BL350 board" )

Also an intersting fact, Chrispine is the maintainer of this board.

To view the full demonstration, kindly visit this link.
[link hereYT]()

### How did it start?

2 lines of code, that's all, it doesn't matter how small your contribution is what matters is that you have made a contribution, for the benefit of everyone. Even if it's a typo, just contribute. *One simple fix* goes a long way.

Chrispine's contribution journey started by fixing compiler warnings by moving ownership, from this small contribution he is now a core maintainer of the AM62X_M4_BL350 board which he added upstream to the zephyr repository and he is currently maintainig it, this goes to show that you do not need to be aseasoned expert to contribute to the open source community. A typo? fix it.  
Perharps he will also need collaborators to help maintain the board.


## From kernel contributions to confidential computing.

Yes, you heard me right, for the first time in Nailug, we had the pleasure of introducing our first female speaker [Dorcas Litunya](https://www.linkedin.com/in/dorcaslitunya/) she's an expert in confidential computing, a core linux contributor and a C-Chad. 

With a background in electrical engineering, Dorcas took the initiative to learn C during the COVID pandemic and leveled up. Currently, she works at Microsoft as a software engineer focusing on identity and access management. Before that, She has contributed to the linux kernel, specifically to the V4L2 subsystem, a linux kernel framework for managing video capture and output devices. Read more on the [V4L2 subsystem](https://wiki.st.com/stm32mpu/wiki/STM32MP13_V4L2_camera_overview#Framework_purpose).


### How does one contribute to the kernel?

Dorcas found herself contributing to the kernel through the [outreachy internship program](https://www.outreachy.org/). She chose to contribut to the linux kernel, because she was interested in learning more about interface between hardware and software, and she found herself in the perfect spot to learn how hardware interfaces with software. 

During the internship, she made core contributions: one by her self and one co-authored by her mentor [Hans Verkuil](https://osseu2024.sched.com/speaker/hverkuil) V4L2 subsystem maintainer. One of the patches included emulating the HDMI interface for userspace appliactions to communicate [Patch link here](). The second patch was working in the deep OS internals, multithreading, media interfaces, while we did not delve deeper, she shared a link to the patch which is linked [here](). Her prowess and skill got her to present a patch; Improving support for the Vivid Test Driver, during the [Open source summit 2024](https://osseu2024.sched.com/event/1ej1w/panel-discussion-outreachy-linux-kernel-internship-report-julia-lawall-inria-hans-verkuil-cisco-systems-norway-tahera-fahimi-university-of-calgary-khadija-kamran-and-dorcas-litunya-jomo-kenyatta-university). I'm sure you might be having questions whether you need to be an expert in order to start. Before she started this internship, Dorcas only knew C and had a thirst for knowledge. This goes to show that you do not need a computer science degree in order to get started, just determination and hardwork.
 
To contribute to the kernel, you submit [patches](https://kernelnewbies.org/PatchPhilosophy) instead of a PR. But it is similar to a pull request. Once you have submitted your patch, you send it to the reviewers via mail. 	

### Why contribute?
One of the points she highlighted was, *you learn by reading code and writing code*. The linux kernel code is one of the best reviewed projects by hundreds of thousands of open source developers, reading this code will help you learn coding standards and some neat tricks while programming. Contributing to the kernel has a *low barrier to a first patch*, be it code clean up,typo fixes or adding comments then slowly build up. Another advantage is geting *mentorship*, real mentorship. Having someone show you the ropes is a good thing, that's how you end up sailing your own ship. Last but not least *It's a durable credential*, Just ask Dorcas, through her contributions, she found herself helping keeping our computers safe by contributing to the world of [cofidential computing](https://www.redhat.com/en/topics/security/what-is-confidential-computing).

 Confidential computing is a branch of computer and data security that majorly focuses on protecting data in use, as compared to data in tansit or data at rest, which can be secured using encryption. Data in use introduces a new attack vector, while you might encrypt your data at rest, eg in a hard-drive by encrypting the data, use of encryption for data in transit by encryption and authentication, this data will also neet to be decrypted while being processed, this means that the decryption keys and the plain data need be loaded in memory for the CPU to perform operations on it.
 
 Confidential computing aims to close this vector and reduce the attack surface by providing mechanisms that protect this data while it's in use. This is achieved by use of trusted execution environments(TEE),  secure enclaves in which code runs protected from the host. And use of specialized chips such as AMD-SEV which protect data at the memory level by encrypting memory pages *this is so cool btw!*. This means you can run your workloads in secure spaces without having to worry about someone reading your data or attacks such as data replay and memory re-mapping.[learn more about AMD-SEV environments](https://www.amd.com/en/developer/sev.html).

 Please visit our youtube to watch the whole session

 [insert video link with timestamp here]()

## Optimizing developer productivity with AI-agents and Omarchy

Norman Bii, took us through a session on how we can optimize our workflow with AI, OS and key-maps in the linux environment without ever leaving the terminal, or touching the mousepad. Yes, I know you're worried about your tokens, here's the best part, you can be able to run these tools without breaking your wallet, or you company's wallet :). Just imagine opening up to your AI in the terminal, what a time to be alive. 

This is made possible by various tools like;

- Herdr
- Opencode
- Tmux
- Omarchy

Herdr is a terminal workspace manager, kind of like [tmux](https://tmux.app/). Tmux allows you to multiplex your terminal, allowing you to open windows, tabs, panes and allows you to split these windows to as many subsections your screen will allow. Herdr upgrades this by allowing you to run multiple agents in different panes, gives you a workspace which contains tabs and panes, which allow you  to view agent sessions that you have started. Now imagine combining this with voice models, you can delete the /boot dir with just a voice command *hehe*.

I'm sure you're wondering where you'll get an agent to do that for you. This is where [openCode](https://opencode.ai/v2/docs) comes in. OpenCode is an opensource AI coding agent that's available for the CLI-interface, desktop and web. To fine-tune your agent, you make use of a file called SKILLS.md. This file can be used in projects to give the AI context and assist you without hallucinating.

Combining this with an agentic-OS like [Omarchy](https://omarchy.org/manual/), you'll be moving around in your workspace like a ninja. *Look guys, no hands! exclaimed the terminal ninja* 

But with great power? yes, there are somethings that you shouldn't let you AI  have access to or view. these include ENV vars, secrets and the database password :). To help with this, Norman shared a cool tool called [infisical](https://infisical.com/docs), an all-in-one open-source security platform that helps you manage your secrets. It's Agent vault allows you to only share credentials that your agent needs while running, nothing more.

To see how Norman intergrates these tools, watch the [youtube video]().


## Hacking Android

Your android device might be spying on you, here's why

Danfold Mosongo, a familiar name in breaking kernels and taking devices, a cybersecurity engineer and a red team operative, took us through [CVE-2026-0073](https://vuldb.com/cve/CVE-2026-0073). Making his third appearance on the NaiLug monthly-community meetups, he always gets us up to speed on matters of securing our devices and avoiding critical exploits that might render our devices useless or hostage by malicious actors.

CVE-2026-0073 a RCE found in the ADB module (*Android Debug Bridge*) for android. ADB allows developers to test their appliactions on their mobile devices. ADB supports multiple connection methods such as 

* Debugging via cable
* wireless debugging via a network

The exploit takes advantage of a code logic error during authentication, while running the wireless debugging option. You see, the wireless ADB protocol uses certificates to authenticate clients and exchange abitarty debugging information. But due to the logical error, an attacker is able to bypass the certificate verification step that allows the server and the client to authenticate before establishing a connection.  

When wireless ADB is open on an adroid device, the server should validate that the connecting device has a valid certificate issued by the device;s certificate authority, however, the flawed logic allows an attacker to forge these certificates and pass the verification routine, even if the attacker presents an invalid certificate. This might not look much, but once the attacker gains access, they will be able to execute code remotely on the victim's device as a shell user. Remember, all this occured without touching the victim's device; they only need to be present on the same network as the vulnerable device. Once the attacker is in your phone, the attacker is able to access system level cabilities like process control, file manipulation and access to sensitive data. the attacker is basically running with the same privileges as the kernel.


### Vulns everywhere

Danfold also took us through some recently discovered vulnerabilities, these include;
	* Ghost lock [CVE-2026-43499](https://www.openwall.com/lists/oss-security/2026/07/08/12) - a classic use-after-free bug
	* Dolby-out-of-bounds [CVE-2025-54957](https://project-zero.issues.chromium.org/issues/428075495) - an out of bounds write

This goes to show that security starts with the developer, at all times we should enforce secure coding practices.



## Our next meet up

Our next meet up will be held in [Kariokor community hall](https://maps.app.goo.gl/5RAWWySDQRNa4VmN8) on the 3^rd^ of October 2026 from 3:00-6:00 pm EAT(UTC+3). We will also be celebrating Software freedom day, read about [software freedom day](https://en.wikipedia.org/wiki/Software_Freedom_Day). We will be having an interesting talk about [Golly](https://golly.sourceforge.io/), a talk by Brian Muhia. 

Uhuru, uhuru, uhuru.

Tell a friend to tell a friend, can't wait to see you again.

![October meet up flyer](./images/meetup-september-2026/SFD2026-NairobiLUG.svg)	
