Title: Mounting Partitions Using systemd
Date: 2015-09-02 11:00
Category: Linux
Tags: linux, systemd
Slug: systemd-mount-partition
Author: James Oguya
Summary: Recently, I discovered you can mount partitions using systemd.mount by writing a mount unit file. In this blog post, we'll talk about systemd.mount & how you can use it to mount partitions.

[systemd](http://www.freedesktop.org/wiki/Software/systemd) is gradually becoming the de facto init system & service manager replacing the old sysV init scripts & upstart. Recently, I discovered you can mount partitions using [systemd.mount](http://www.freedesktop.org/software/systemd/man/systemd.mount.html) by writing your own `.mount` [systemd unit file](http://www.freedesktop.org/software/systemd/man/systemd.unit.html).

![super suprised]({static}/images/systemd-mount-partition/suprised-cat.jpg)

After _RTFM'ing_, I realized, under the hood, systemd just runs [mount command](http://linux.die.net/man/8/mount) to mount the specified partition with the specified mount options listed in the mount unit file. Basically, you need to specify the following options in your unit file:

- `What=` a partition name, path or UUID to mount
- `Where=` an absolute path of a directory i.e. path to a mount point. If the mount point is non-existent, it will be created
- `Type=` file system type. In most cases [mount command](http://linux.die.net/man/8/mount) auto-detects the file system
- `Options=` Mount options to use when mounting

In the end, you can convert your typical fstab entry such as this:

```
UUID=86fef3b2-bdc9-47fa-bbb1-4e528a89d222 /mnt/backups    ext4    defaults      0 0
```

to:

```ini
[Mount]
What=/dev/disk/by-uuid/86fef3b2-bdc9-47fa-bbb1-4e528a89d222
Where=/mnt/backups
Type=ext4
Options=defaults
```

![I Got This!]({static}/images/systemd-mount-partition/i-got-this.gif)

So I wrote a simple systemd mount unit file — `/etc/systemd/system/mnt-backups.mount` — which didn't work at first because I fell victim to one of the `systemd.mount` pitfalls:

> Mount units must be named after the mount point directories they control. Example: the mount point /home/lennart must be configured in a unit file home-lennart.mount.

Huh? Yes that's right! The unit filename should match the mount point path.

`mnt-backups.mount` mount unit file:

```ini
[Unit]
Description=Mount System Backups Directory

[Mount]
What=/dev/disk/by-uuid/86fef3b2-bdc9-47fa-bbb1-4e528a89d222
Where=/mnt/backups
Type=ext4
Options=defaults
```

Reload systemd daemon & start the unit.

```sh
systemctl daemon-reload
systemctl start mnt-backups.mount
```

And just like any other unit, you can view its status using `systemctl status mnt-backups.mount`:

```
root@vast ~ # systemctl status mnt-backups.mount
● mnt-backups.mount - Mount System Backups Directory
   Loaded: loaded (/etc/systemd/system/mnt-backups.mount; enabled; vendor preset: disabled)
   Active: active (mounted) since Mon 2015-08-31 08:09:15 EAT; 2 days ago
    Where: /mnt/backups
     What: /dev/sdc
  Process: 744 ExecMount=/bin/mount /dev/disk/by-uuid/86fef3b2-bdc9-47fa-bbb1-4e528a89d222 /mnt/backups -n -t ext4 -o defaults (code=exited, status=0/SUCCESS)

Aug 31 08:09:15 vast systemd[1]: Mounting Mount System Backups Directory...
Aug 31 08:09:15 vast systemd[1]: Mounted Mount System Backups Directory.
```

## Gotchas!!

After a reboot, I noticed the unit wasn't started & as result the mount point dir. was empty. The unit file was missing an `[Install]` section which contains installation information such as unit dependencies(`WantedBy=, RequiredBy=`), aliases(`Alias=`), additional units(`Also=`), e.t.c for the specified unit. In this case, I set the unit to start in multi-user runlevel a.k.a `multi-user.target`. Oh, did you know you can change runlevel using `systemctl isolate $RUN_LEVEL.target`? [Read more](https://wiki.archlinux.org/index.php/Systemd#Targets_table) about systemd runlevels/targets.

Here's the complete `/etc/systemd/system/mnt-backups.mount` unit file with an `[Install]` section:

```ini
[Unit]
Description=Mount System Backups Directory

[Mount]
What=/dev/disk/by-uuid/86fef3b2-bdc9-47fa-bbb1-4e528a89d222
Where=/mnt/backups
Type=ext4
Options=defaults

[Install]
WantedBy=multi-user.target
```

As always, enable the unit to start automatically during boot.

```sh
systemctl enable mnt-backups.mount
```
