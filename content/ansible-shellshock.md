Title: Update hosts via Ansible to mitigate bash "Shellshock" vulnerability
Date: 2014-09-29 10:40
Category: Linux
Tags: linux, ansible, bash, security
Slug: ansible-shellshock
Author: Alan Orth
Summary: Patching your systems is painlessly easy if you manage your server infrastructure with something like Ansible.

On September 24, 2014 someone [posted](http://seclists.org/oss-sec/2014/q3/649 "CVE-2014-6271: remote code execution through bash") on the oss-sec mailing list about a `bash` vulnerability that likely affects several decades of `bash`  versions (something like `1.14` - `4.3`!).  The vulnerability — aptly named "Shellshock" — can lead to remote code execution on un-patched hosts, for example [web servers parsing HTTP environment variables via CGI GET requests](http://www.nimbo.com/blog/shellshock-heartbleed-2-0), [sshd configurations using `ForceCommand`](https://community.qualys.com/blogs/laws-of-vulnerabilities/2014/09/24/bash-shellshock-vulnerability "BASH Shellshock vulnerability - Update3"), [DHCP clients](https://www.trustedsec.com/september-2014/shellshock-dhcp-rce-proof-concept/ "Shellshock DHCP RCE PoC"), etc.

Anyways, I'll leave the infosec community to [expound on attack vectors](https://www.dfranke.us/posts/2014-09-27-shell-shock-exploitation-vectors.html "Shell Shock Exploitation Vectors").  The point of this post is really to illustrate that you should be using an infrastructure orchestration tool like [Ansible](http://www.ansible.com/home "Ansible homepage") to manage your servers.

### Painless patching with Ansible

Patching your systems is painlessly easy if you manage your server infrastructure with something like Ansible.  Using a one-off command you can easily update all "web" servers, for example:

    :::console
    $ ansible web -m apt -a "name=bash state=latest update_cache=yes" -K -s

That's great, but what if you have both Ubuntu and CentOS hosts in the "web" group?  CentOS doesn't use `apt` for package management, so this has effectively only updated hosts running Debian-family GNU/Linux distros.

### Playbooks: the power of Ansible

When you have more than a handful of servers, the combinations of DNS names, IP addresses, roles, and distros becomes overwhelming.  With Ansible you define your inventory of hosts, allocate them into groups, and then write "playbooks" to mold your servers into functional roles, ie web, database, compute, proxy, etc servers; the [personal relationship](https://xkcd.com/910/ "XKCD coming about naming servers") between sysadmin and server is gone.

Here's a simple playbook I wrote which takes into account the different OS families in our infrastructure and updates the `bash` package on each host.

_shellshock.yml_:

    :::yaml
    ---
    # To update hosts for "Shellshock" bash vulnerability
    # See: https://en.wikipedia.org/wiki/Shellshock_(software_bug)

    - hosts: all
      sudo: yes
      tasks:
        - name: Update on Debian-based distros
          apt: name=bash state=latest update_cache=yes
          when: ansible_os_family == "Debian"

        - name: Update on RedHat-based distros
          yum: name=bash state=latest
          when: ansible_os_family == "RedHat"

    # vim: set sw=2 ts=2:

And then run the playbook with:

    :::console
    $ ansible-playbook shellshock.yml -K -s

In our case we patched twenty-five CentOS 6.x, Debian 6, Debian 7, Ubuntu 12.04, and Ubuntu 14.04 hosts living locally, in Amazon EC2, and in Linode.  With one command.  In less than five minutes!

### Stay vigilant!

Vendors started pushing patched versions of `bash` on September 26th, two days after the initial disclosure.  Two days after those patched versions were released there were [new variations of this bug discovered](http://lcamtuf.blogspot.com/2014/09/bash-bug-apply-unofficial-patch-now.html "Bash bug: apply Florian"), and new packages issued (and we patched our systems again!).

As of now, five days after initial disclosure, there exist five <abbr title="Common Vulnerabilities and Exposures">CVE</abbr> identifiers for this bug!  So keep an eye on social media ([#shellshock](https://twitter.com/search?q=%23shellshock "#shellshock on Twitter")?), [Hacker News](https://news.ycombinator.com/ "Hacker News"), and [sites monitoring this bug](https://shellshocker.net/ "Shellshock monitoring"), because more new vectors may emerge!

This was [originally posted](https://mjanja.ch/2014/09/update-hosts-via-ansible-to-mitigate-bash-shellshock-vulnerability/) on my personal blog; re-posted here for posterity.
