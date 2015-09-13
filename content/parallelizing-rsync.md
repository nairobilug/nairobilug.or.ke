Title: Parallelizing rsync
Date: 2014-07-11 16:40
Category: Linux
Tags: linux, rsync
Slug: parallelizing-rsync
Author: Alan Orth
Summary: Using find and xargs to parallelize rsync and speed up transfers of large directory hierarchies

Last week I had a massive hardware failure on one of the GlusterFS storage nodes in the [ILRI, Kenya Research Computing cluster](http://hpc.ilri.cgiar.org/); two drives failed simultaneously on the underlying RAID5. As RAID5 can only withstand one drive failure, the entire 31TB array was toast. FML.

After replacing the failed disks, rebuilding the array, and formatting my bricks, I decided I would use `rsync` to pre-seed my bricks from the good node before bringing `glusterd` back up.

*tl;dr*: `rsync` is amazing, but it’s single threaded and struggles when you tell it to sync large directory hierarchies.  [Here's how you can speed it up](#sync_bricks).

### rsync #fail
I figured syncing the brick hierarchy from the good node to the bad node was simple enough, so I stopped the `glusterd` service on the bad node and invoked:

    :::console
    # rsync -aAXv --delete --exclude=.glusterfs storage0:/path/to/bricks/homes/ storage1:/path/to/bricks/homes/

After a day or so I noticed I had only copied ~1.5TB (over 1 hop on a dedicated 10GbE switch!), and I realized something must be wrong.  I attached to the `rsync` process with `strace -p` and saw a bunch of system calls in one particular user’s directory. I dug deeper:

    :::console
    # find /path/to/bricks/homes/ukenyatta/maker/genN_datastore/ -type d | wc -l
    1398640

So this one particular directory in one user's home contained over a million *other* directories and $god knows how many files, and this command itself took several hours to finish!  To make matters worse, careful trial and error inspection of other user home directories revealed more massive directory structures as well.

- rsync is single threaded
- rsync generates a list of files to be synced before it starts the sync
- MAKER creates a ton of output files/directories

It's pretty clear (now) that a recursive `rsync` on my huge directory hierarchy is out of the question!

### rsync #win
I had a look around and saw lots of people complaining about `rsync` being "slow" and others suggesting tips to speed it up.  One very promising strategy was described on [this wiki](https://wiki.ncsa.illinois.edu/display/~wglick/Parallel+Rsync) and there's a great discussion in the comments.

Basically, he describes a clever use of `find` and `xargs` to split up the problem set into smaller pieces that `rsync` can process more quickly.

### sync_brick.sh
So here's my adaptation of his script for the purpose of syncing failed GlusterFS bricks, `sync_brick.sh`:

    :::bash
    #!/bin/env bash
    # borrowed / adapted from: https://wiki.ncsa.illinois.edu/display/~wglick/Parallel+Rsync

    # RSYNC SETUP
    RSYNC_PROG=/usr/bin/rsync
    # note the important use of --relative to use relative paths so we don't have to specify the exact path on dest
    RSYNC_OPTS="-aAXv --numeric-ids --progress --human-readable --delete --exclude=.glusterfs --relative"
    export RSYNC_RSH="ssh -T -c arcfour -o Compression=no -x"

    # ENV SETUP
    SRCDIR=/path/to/good/brick
    DESTDIR=/path/to/bad/brick
    # Recommend to match # of CPUs
    THREADS=4
    BAD_NODE=server1

    cd $SRCDIR

    # COPY
    # note the combination of -print0 and -0!
    find {a..z}* {A..Z}* {0..9}* -mindepth 1 -maxdepth 1 -print0 | \
        xargs -0 -n1 -P$THREADS -I% \
            $RSYNC_PROG $RSYNC_OPTS "%" $BAD_NODE:$DESTDIR

Pay attention to the source/destination paths, the number of `THREADS`, and the `BAD_NODE` name, then you should be ready to roll.

### The magic, explained
It's a bit of magic, but here are the important parts:

- The `-aAXv` options to `rsync` tell it to **archive**, preserve **ACLs**, and preserve **eXtended** attributes.  Extended attributes are [critically important in GlusterFS >= 3.3](http://joejulian.name/blog/what-is-this-new-glusterfs-directory-in-33), and also if you're using SELinux.
- The `--exclude=.glusterfs` option to `rsync` tells it to ignore this directory at the root of the directory, as the self-heal daemon — `glustershd` — will rebuild it based on the files' extended attributes once we restart the `glusterd` service.
- The `--relative` option to `rsync` is so we don't have to bother constructing the destination path, as `rsync` will imply the path is relative to our destination's top.
- The `RSYNC_RSH` options influence `rsync`'s use of SSH, basically telling it to use very weak encryption and disable any unnecessary features for non-interactive sessions (tty, X11, etc).
- Using `find` with `-mindepth 1` and `-maxdepth 1` just means we concentrate on files/directories 1 level below each directory in our immediate hierarchy.
-Using `xargs` with `-n1` and `-P` tells it to use 1 argument per command line, and to launch `$THREADS` number of processes at a time.

Hope this helps!

This was [originally posted](https://mjanja.ch/2014/07/parallelizing-rsync/) on my personal blog; re-posted here for posterity.
