Title: Rebooting server(s) using Ansible
Date: 2015-03-03 12:35
Category: Linux
Tags: linux, ansible
Author: James Oguya
Slug: rebooting-server-using-ansible
Summary: Ansible provides useful tools which we can use to for various purposes.
In this blogpost, we'll talk about rebooting servers using ansible & pausing the
playbook by waiting for a given amount of time for a given service on a given
port to start.

Of late, I've seen a lot of guys on `#ansible` irc channel & google groups
asking questions about rebooting servers/nodes & temporarily pausing the
playbook for a given amount of time before continuing with the execution of the
playbook. In some cases, you'd want to set some kernel parameters which take
effect at boot time or perform major upgrades which might require a reboot
before configuring the server/node.

Using ansible's `wait_for` module[<sup>[1]</sup>](http://docs.ansible.com/wait_for_module.html),
we can temporarily stop running the playbook while we wait for the server to
finish rebooting or for a service to start & bind to a port. We can also use the
same module to wait for a port to become available which can be useful in
situations where services are not immediately available after their `init`
scripts finish running - as is the case with Java application server e.g. Tomcat.

### gettin' started
Basically, we can break our problem into 4 sections for easier conceptualization:


- Section 1: **Pre-reboot**: Run your pre-reboot task, it can be performing major
upgrades and/or performing some configuration which only take effect at boot time.
For example - upgrade all packages using `yum` module[<sup>[2]</sup>](http://docs.ansible.com/yum_module.html)

        - name: upgrade all packages
          yum: name=* state=latest


- Section 2: **Reboot**: In this stage we'll use the `command` module[<sup>[3]</sup>](http://docs.ansible.com/command_module.html)
to reboot the remote machine/server by running the `reboot` command  - nothing
fancy - you can also use `shutdown --reboot`.

        - name: reboot server
          command: /sbin/reboot


- Section 3: **Pause the playbook**: We'll use the `wait_for` module to wait for
300 seconds for port 22 to become available before resuming the playbook. I'm
using port 22 because most servers run openssh-server on port 22 & if we were to
telnet to that port we'd probably see something like :`SSH-2.0-OpenSSH_6.6.1`,
so we can use regex to check whether the output matches "OpenSSH". I'm also
using a `timeout` value of 300 seconds because most physical servers take
3 - 5 minutes to finish rebooting due to hardware checks e.t.c. but you can
use any value that suites you.
For example: - wait for 300 seconds for port 22 to become available & contain
`OpenSSH`

        - name: wait for the server to finish rebooting
          local_action: wait_for host="web01" search_regex=OpenSSH port=22 timeout=300



- Section 4: **Resume the playbook**: After we've got a response from port 22,
we can resume running the playbook. This step can be optional depending on your
needs.


### puttin' it all together
- We can merge all the above sections into one playbook as shown below:

        - hosts: all
          sudo: yes
          tasks:
            - name: Upgrade all packages in RedHat-based machines
              when: ansible_os_family == "Redhat"
              yum: name=* state=latest

            - name: Upgrade all packages in Debian-based machines
              when: ansible_os_family == "Debian"
              apt: upgrade=dist update_cache=yes

            - name: Reboot server
              command: /sbin/reboot

            - name: Wait for the server to finish rebooting
              sudo: no
              local_action: wait_for host="{{ inventory_hostname }}" search_regex=OpenSSH port=22 timeout=300


### stuff to note
- I know you might be wondering why we didn't use handlers. Well, `notify`
tasks[<sup>[4]</sup>](http://docs.ansible.com/playbooks_intro.html#handlers-running-operations-on-change)
are only executed at the end of the playbook regardless of their location in the
playbook - remember we're interested in rebooting the server & waiting for a
given amount of time for the server to finish rebooting.
- `inventory_hostname` variable[<sup>[5]</sup>](http://docs.ansible.com/playbooks_variables.html#magic-variables-and-how-to-access-information-about-other-hosts)
is the name of the remote server as stated in
the ansible hosts file
- `local_action` directive[<sup>[6]</sup>](http://docs.ansible.com/glossary.html#local-action)
runs the given step on the local machine, for example, it would run the
`wait_for` task on your local machine.
- `yum` module only works on RedHat based OS e.g. Fedora, CentOS & RHEL -
and so we'll also use the `apt` module for Debian based OS e.g. Ubuntu, Debian
e.t.c.


### links
1. [Ansible wait_for module](http://docs.ansible.com/wait_for_module.html)
2. [Ansible command module](http://docs.ansible.com/command_module.html)
3. [Ansible yum module](http://docs.ansible.com/yum_module.html)
3. [Ansible Handlers: Running operations on change](http://docs.ansible.com/playbooks_intro.html#handlers-running-operations-on-change)
4. [Playbook built-in variables](http://docs.ansible.com/playbooks_variables.html#magic-variables-and-how-to-access-information-about-other-hosts)
5. [Ansible local_action directives](http://docs.ansible.com/glossary.html#local-action)
