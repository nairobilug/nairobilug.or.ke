Title: March 2026 Meetup - Learning to Contribute to Open Source
Date: 2026-03-07 15:00
Category: Meetups
Tags: meetup, open-source, contributions, mozilla, fedora
Slug: meetup-march-2026-learning-to-contribute-to-open-source
Author: Cornelius Emase
Summary: Highlights from the March 2026 meetup on getting started with open source contributions.


Our second meetup of the year happened on **7th March**, and it was a great improvement from the [previous one](/2026/02/meetup-february-2026.html). More new faces this time, more than double those who attended last time. It's both promising and exciting to see the community reawaken like this.

We had initially planned to have two sessions, '**Self-hosting series: How to host your website on an android phone**' by **Paul Mayero** and '**how to start contributing to open source projects**' by **Cornelius Emase** but ended up with the latter one due to time.


## My journey into Open Source

Engaging the audience with a personal example felt like a good approach, so I started by sharing my journey into open source. Even though I had already contributed to small open projects and had an idea of how things work, joining bigger communities was a somewhat smoother transition for me. In my case, I joined the **Fedora Project** through an Open Source program, [**Outreachy**](https://www.outreachy.org/), which can be quite competitive.

I also mentioned other programs that help people get into open source such as:

* [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/)
* [LFX](https://mentorship.lfx.linuxfoundation.org/)
* [MLH Fellowship](https://fellowship.mlh.io/)
* [Igalia](https://www.igalia.com/coding-experience/)
* [Season of KDE](https://mentorship.kde.org/sok/)
* [FSF Internships](https://fsf.org/volunteer/internships)
* and other mentorship and community programs

These programs help new contributors learn the workflow and gain experience while working with real projects.

However, joining a program is **not the only path**.

Some people start contributing simply by finding a bug in a product they use every day. If they have the technical skills, they try to fix it themselves. If not, they can still report the problem so the team can fix it. I believe people have their own reasons for contributing to a given project, either you want to gain skills, or want an in/get hired by the company or even, your curiosity to contribute just for fun or when you're bored.


## How to start contributing

One of the simplest ways to start is surprisingly straightforward. You open a browser and type:

> **"How to contribute to (project name)"** For example: how to contribute to Mozilla/Fedora/Gentoo etc.

Most large open source organizations have detailed documentation explaining how to get started. That said, documentation quality can vary a lot from one project to another. Some communities invest heavily in newcomer guides (for example, [Kernel Newbies](https://kernelnewbies.org/)), while others expect you to learn more by interacting with maintainers and existing contributors.

It is also worth looking at organization culture when choosing where and how to contribute. Smaller organizations can be a good place to start too, since core developers may have more time to work with new contributors, even if they do not always have a structured onboarding program.

Before doing that though, it is important to know **why you want to contribute**.

Your motivation might be:

* Passion for open source
* Learning new skills
* Building experience
* Contributing to software you use
* Or simply doing something fun when you are bored

All of the above reasons are valid.


## Exploring Mozilla’s contribution guide

We walked through the [Mozilla contribution documentation](https://firefox-source-docs.mozilla.org/setup/contributing_code.html) together.

Mozilla has many projects and components that people can contribute to. Within these projects you will find things called **bugs** tracked in [Mozilla Bugzilla](https://bugzilla.mozilla.org/) just like any other projects (eg. [RedHat & Fedora Bugzilla](https://bugzilla.redhat.com/)).

A **bug** is simply a task that needs work. In different teams this might also be called an **issue**, a **ticket**, or a **task**.

Mozilla also labels some tasks as [**student bugs**](https://bugzilla.mozilla.org/buglist.cgi?quicksearch=kw%3Astudent-project&list_id=17882273), which are beginner-friendly issues designed to help new contributors get started.

Contributors, including students, can solve these bugs and get recognition for their work, and for students this may also count toward academic credit.

Using Mozilla's guide, we discussed how this is similar to any other open source project out there.


## How contributions are reviewed

We also talked about how large organizations manage code contributions.

Most projects follow a similar process:

1. A bug or issue is created
2. A contributor works on a fix
3. The fix is submitted as a [**patch**](https://en.wikipedia.org/wiki/Patch_(computing))
4. Maintainers review the change
5. The change is revised until it is ready to merge

In Mozilla’s case, they use a review platform called **[MozPhab(Phabricator)](https://wiki.mozilla.org/MozPhab)** to manage patches and code reviews.

To make the discussion practical, we looked at a small example optimization from the **SpiderMonkey JavaScript engine** and discussed what the change was doing.

Example reference:
https://gist.github.com/Lochipi/651a69fcbad5a65d86e15b22486ef1e1

The note explains a small but important optimization in object allocation. Even small improvements can matter when the code runs millions of times.

We also solved one bug together during the meetup.


## Can you get paid while contributing?

One interesting question that came up was this. 

One of the members in the group explained that many people actually do get paid for open source work.

Some common ways include:

* Security bug bounty programs
* Being employed by companies that maintain open source projects
* Working for organizations that build products on top of open source

We also talked about computer hacking contests like [Pwn2Own](https://en.wikipedia.org/wiki/Pwn2Own), where security researchers report vulnerabilities and get paid when the issue is confirmed.


## AI and Open Source

AI also came up during the conversation. Different open source communities have different policies regarding AI-generated contributions.

Some communities allow it under specific rules. Others discourage or restrict it.

Projects like **Fedora** and **Firefox (Mozilla)** allow contributors to use AI tools under policy guidelines, while **Gentoo** does not allow AI-generated contributions.

- [Fedora AI-Assisted Contributions Policy](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/)
- [Firefox AI Coding Policy](https://firefox-source-docs.mozilla.org/contributing/ai-coding.html)
- [Gentoo Project:Council/AI policy](https://wiki.gentoo.org/wiki/Project:Council/AI_policy)


## What helps you succeed in Open Source

We also discussed what someone needs to succeed when contributing to open source.

Some important things are:

* Curiosity and willingness to learn
* Reading documentation
* Patience with code reviews
* Communication with maintainers
* Consistency in contributing

The big part about this is collaboration, and not all about code.


## Community contributions and experiences

The conversation became more engaging as other members shared their experiences with different projects.

Members talked about their work in projects such as [**Gentoo**](https://www.gentoo.org/) and other open source initiatives they are involved in.

It was great to see people exchanging ideas and learning from each other. We hope you join us next time, and speak about your community or even do a presentation and show us some tricks about open source. This is open to all Enthusiasts.


## Open Source in Government

We also had an interesting contribution from **Evanson Ikua**, an open source evangelist working in government.

He shared about initiatives being done in collaboration with partners from Germany to promote the adoption of open source technologies within government institutions.

He also highlighted opportunities that might be available for community members.

We hope some of our members will be able to benefit from those opportunities.

More details on that topic will be covered in a future blog post.


## Networking and tea

There is a saying that **a meetup without food is just a meeting**.

Thankfully, we had tea and mandazi. :)

This gave everyone a chance to relax, network, and continue conversations with other members of the community.


## Next meetup

We meet **every first Saturday of the month**.

Details about the next meetup will be updated here soon, so stay tuned.

It was a fun and engaging session, and we hope to see even more of you at the next meetup.
