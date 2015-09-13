Title: Replacing cron jobs with systemd timers
Date: 2015-06-08 15:21
Category: Linux
Tags: linux, systemd, cron
Slug: cron-systemd-timers
Author: Alan Orth
Summary: Using systemd's timer functionality to to replace (and improve) cron jobs

systemd has a timer function that can be used to run tasks periodically — yes, like `cron`. There's nothing really wrong with cron, but have you ever tried to debug a cron job on a server? The script runs fine from the command line, but nothing seems to happen when it runs from cron. You quickly type `date` to see how many seconds until the next minute, adjust the cron job, and wait. Nothing. Repeat. _\*facedesk\*_

This is the systemd value proposition in this context: _timers can be run on demand_ from the command line, and _their output is logged to the systemd journal_ where you can see it like any other systemd units.

## System backups using a timer
As an example, I have a simple shell script — `system-backup.sh` — that uses `rsync` to back up my system to an external USB hard drive once per day. Converting this job to use systemd timers requires the creation of both a _timer_ and a _service_.

_/etc/systemd/system/system-backup.timer_:

```
[Unit]
Description=Perform system backup

[Timer]
OnCalendar=daily

[Install]
WantedBy=timers.target
```

_/etc/systemd/system/system-backup.service_:

```
[Unit]
Description=Perform system backup

[Service]
Type=simple
Nice=19
IOSchedulingClass=2
IOSchedulingPriority=7
ExecStart=/root/system-backup.sh
```

Start and enable the timer:

    $ sudo systemctl start system-backup.timer
    $ sudo systemctl enable system-backup.timer

Starting the timer is necessary because otherwise it wouldn't be active until the next time you rebooted (assuming it was enabled, that is). You can verify that the timer has been started using either of the following commands:

    $ sudo systemctl status system-backup.timer
    $ sudo systemctl list-timers --all

## What this gets you
Using `OnCalendar=daily` this job will run every day at midnight, similar to cron's `@daily` keyword. If you ever want to run the job manually you can invoke its service on demand:

    $ sudo systemctl start system-backup.service

Unless you're handling stdout manually in your script (like appending to a log file), any output from will go to the systemd journal. You can see the logs just like you'd do for any other system unit file using `journalctl`.

For example, to see logs from this timer since yesterday:

    $ sudo journalctl -u system-backup --since="yesterday"

I find this much more elegant than appending to, looking through, and rotating log files manually. Furthermore, I like the ability to set CPU and I/O scheduling priorities in the service itself rather than relying on external `nice` and `ionice` binaries in the script. :)

## More information
See the following for more information:

- `man systemd.timer`
- `man systemd.service`
- `man journalctl`

This was [originally posted](https://mjanja.ch/2015/06/replacing-cron-jobs-with-systemd-timers/) on my personal blog; re-posted here for posterity.
