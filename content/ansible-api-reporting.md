Title: Leveraging the Ansible Python API for infrastructure reporting
Date: 2015-01-21 16:40
Category: Linux
Tags: linux, ansible
Slug: ansible-api-reporting
Author: Alan Orth
Summary: Leveraging Ansible's Python API to generate infrastructure reports

A few days ago I had to get some basic information from a handful of servers for an inventory report; just basic stuff like hostname, IP address, storage capacity, distro version, etc. I already manage all of my servers with Ansible, and there's a wealth of information available in Ansible's `setup` module, so I knew there had to be a clever way to do this.

Somehow I stumbled upon [Ansible's Python API](http://docs.ansible.com/developing_api.html), which solves this problem elegantly! It helped that other people are doing cool things and [writing about their experiences](http://jpmens.net/2012/12/13/obtaining-remote-data-with-ansible-s-api/) too.

## Enter ansible.runner
According to the documentation, the Python API is:
<blockquote>[...] very powerful, and is how the ansible CLI and ansible-playbook are implemented.</blockquote>

Indeed! Using `ansible.runner` I whipped something up and extracted data from several dozen servers in just a few minutes (and I don't even know Python!):

```
$ ./ansible-runner.py
mjanjavm10, 2, 30, Ubuntu 14.04, 192.168.7.34
mjanjavm14, 2, 30, Ubuntu 14.04, 192.168.7.37
```

I had to massage the data a bit to get clean numbers for RAM and storage capacity, but other than that it was extremely straightforward (as most things with Ansible generally are).

## The code
Here's the source code for the *ansible-runner.py* script above:

```
#!/usr/bin/env python

import ansible.runner

# hosts to contact
hostlist = ['virtual']

# MiB -> GiB
def mibs_to_gibs(mibs):
    return float(mibs) / 1024.0

# KiB -> GiB
def kibs_to_gibs(kibs):
    return float(kibs) / 1024.0 / 1024.0

# bytes -> GiB
def bytes_to_gibs(num_bytes):
    return float(num_bytes) / 1024.0 / 1024.0 / 1024.0

def parse_results(results):
    for (hostname, result) in results['contacted'].items():
        memory = mibs_to_gibs(result['ansible_facts']['ansible_memtotal_mb'])

        # enumerate all disk devices to get total capacity
        disk_total_capacity = 0
        for disk_device in result['ansible_facts']['ansible_devices'].iterkeys():
            disk_sectors = float(result['ansible_facts']['ansible_devices'][disk_device]['sectors'])
            disk_sectors_size = float(result['ansible_facts']['ansible_devices'][disk_device]['sectorsize'])
            disk_bytes = disk_sectors * disk_sectors_size

            disk_total_capacity += bytes_to_gibs(disk_bytes)

        os = "%s %s" % (result['ansible_facts']['ansible_distribution'], result['ansible_facts']['ansible_distribution_version'])
        ip = "%s" % (result['ansible_facts']['ansible_default_ipv4']['address'])

        print "%s, %.0f, %2.0f, %s, %s" % (hostname, memory, disk_total_capacity, os, ip)

if __name__ == '__main__':
    results = ansible.runner.Runner(
        module_name='setup',
        module_args='',
        remote_user='provisioning',
        sudo=False,
        pattern=hostlist,
        forks=5
    ).run()

    parse_results(results)

# vim: set sw=4 ts=4:
```

Feel free to use, improve, and share it.

This was [originally posted](https://mjanja.ch/2015/01/leveraging-the-ansible-python-api-for-infrastructure-reporting/) on my personal blog; re-posted here for posterity.
