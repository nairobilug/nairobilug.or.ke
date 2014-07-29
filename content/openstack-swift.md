Title: Using swiftclient for object storage on OpenStack
Date: 2014-07-29 19:40
Category: Linux
Tags: linux, openstack, swift
Slug: swiftclient-openstack
Author: Alan Orth
Summary: Using swiftclient to backup data to OpenStack Swift object storage

I wanted to play with my new account on East African OpenStack provider [Kili.io](http://kili.io/), specifically to use the OpenStack Swift object storage to do periodic backups from my desktop.  I'd used tools like [s3cmd](http://s3tools.org/s3cmd) to do backups to Amazon S3 object storage, but it doesn't seem to work with OpenStack's [Swift](http://docs.openstack.org/developer/swift/).

[python-swiftclient](https://www.swiftstack.com/docs/integration/python-swiftclient.html) seems to be the answer. These are my notes from getting it set up to backup some data from my desktop to my shiny new OpenStack provider.

### See also
Related links and documentation:

- [Swift CLI Basic](http://docs.openstack.org/grizzly/openstack-object-storage/admin/content/swift-cli-basics.html)
- [Manage objects and containers](http://docs.openstack.org/user-guide/content/managing-openstack-object-storage-with-swift-cli.html)

## Download RC file
This is actually the trickiest part of this whole exercise (you're welcome!).  For an outsider, the OpenStack API jargon is a bit overwhelming.  Luckily, I found that OpenStack provides a shell init script which will set all the shell environment variables you need to get started with `swiftclient` (and presumably other OpenStack tools).

In the dashboard, navigate to `Project -> Compute -> Access & Security -> Download OpenStack RC File`.  We'll need this later.

## Create and prepare virtualenv
There's no `swiftclient` package in my GNU/Linux distribution, so I decided to just install it into a virtual environment straight from pypi/pip.

    :::console
    $ mkvirtualenv -p `which python2` swift
    $ pip install python-swiftclient python-keystoneclient

## Setup the environment
Source the environment RC script you downloaded from the OpenStack dashboard:

    :::console
    $ . ~/Downloads/aorth-openrc.sh

It will prompt you for your OpenStack dashboard password.

## Test
Check if the settings are correct:

    :::console
    $ swift stat
           Account: AUTH_8b0c9cff5d094829b0cf7606a0390c1a
        Containers: 0
           Objects: 0
             Bytes: 0
     Accept-Ranges: bytes
            Server: nginx/1.4.7
        Connection: keep-alive
       X-Timestamp: 1406586841.02692
        X-Trans-Id: tx5d47eff065074335a3a9f-0053d7c93e
      Content-Type: text/plain; charset=utf-8

This means the API key and all other settings are ok, and authentication was successful; you're now ready to use OpenStack CLI tools.

## Create a container
You could create a container in the OpenStack dashboard (`Object Store -> Containers -> Create Container`), but it's much nicer to be able to do this from the commandline using the API.

    :::console
    $ swift post Documents
    $ swift list
    Documents

## Upload files
My use case is to backup Documents from my desktop.

    :::console
    $ cd ~/Documents
    $ swift upload Documents *

**Note:** I `cd` into the directory I want to upload first, because I found that if I wasn't *inside* it, I would end up with another layer of hierarchy in my container itself, ie `Documents/Documents`.

Check the status of the container:

    :::console
    $ swift stat Documents
           Account: AUTH_9b0a8aff5d584828b5af7656c0385a1c
         Container: Documents
           Objects: 2691
             Bytes: 262663872
          Read ACL:
         Write ACL:
           Sync To:
          Sync Key:
     Accept-Ranges: bytes
            Server: nginx/1.4.7
        Connection: keep-alive
       X-Timestamp: 1406586841.13379
        X-Trans-Id: txbf31671156c64147bd9ad-0053d767c9
      Content-Type: text/plain; charset=utf-8

Looks good!  ~250MB of data in my `Documents` container now, which just about matches the size of the folder on my disk. 

## Bonus points
Bonus points and future research:

- If I want to call this from a cron job, how do I enter my password?
- How do I encrypt my backups?
- Use `--skip-identical` to only sync new files
- What other interfaces are there to this storage, ie can I point a music player at this?
- Play with public/private read/write ACLs
