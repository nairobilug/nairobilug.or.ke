Title: Using systemd Timers to Renew Let’s Encrypt Certificates
Date: 2016-07-11 14:42
Category: Linux
Tags: Let's Encrypt, systemd, Security
Slug: using-systemd-timers-to-renew-lets-encrypt-certificates
Author: Alan Orth
Summary: Automating the Let's Encrypt TLS certificate renewal process using systemd timers on GNU/Linux is easier and more flexible than using cron.

This is a quick blog post to share the systemd timers that I use to automate the renewal of my [Let's Encrypt](https://letsencrypt.org) certificates. I prefer [systemd timers to cron jobs](https://nairobilug.or.ke/2015/06/cron-systemd-timers.html) for task scheduling because they are more flexible and easier to debug. I assume that you know what Let's Encrypt is and that you already have some certificates. If not, I recommend that you check out [Certbot](https://certbot.eff.org) (the official reference client) and get some.

[![Let's Encrypt logo]({static}/images/letsencrypt-systemd-timers/lets-encrypt.png)](https://letsencrypt.org/ "Let's Encrypt homepage")

Because Let's Encrypt issues <abbr title="Transport Layer Security">TLS</abbr> certificates with much [shorter lifetimes](https://letsencrypt.org/2015/11/09/why-90-days.html) (currently ninety days) than traditional certificate authorities, they expect you to reduce the burden of the issuance and renewal processes by performing them programmatically and automating them.

## Check Early, Check Often

Your certificates are good for ninety days, but checking them for renewal on a daily or weekly basis allows for some margin of error in case of server downtime, network interruptions, beach holidays, etc. In the future Let's Encrypt might use even shorter lifespans so it's good to get familiar with this automation now. You will need to create both the `service` and `timer` unit files below.

_/etc/systemd/system/renew-letsencrypt.service_ :

    [Unit]
    Description=Renew Let's Encrypt certificates

    [Service]
    Type=oneshot
    # check for renewal, only start/stop nginx if certs need to be renewed
    ExecStart=/opt/certbot-auto renew --standalone --pre-hook "/bin/systemctl stop nginx" --post-hook "/bin/systemctl start nginx"

_/etc/systemd/system/renew-letsencrypt.timer_ :

    [Unit]
    Description=Daily renewal of Let's Encrypt's certificates

    [Timer]
    # once a day, at 2AM
    OnCalendar=*-*-* 02:00:00
    # Be kind to the Let's Encrypt servers: add a random delay of 0–3600 seconds
    RandomizedDelaySec=3600
    Persistent=true

    [Install]
    WantedBy=timers.target

This timer runs once a day at 2AM, but each execution is delayed by a random amount of time between zero and 3600 seconds using the `RandomizedDelaySec` option.

Pay attention to the location of the `certbot-auto` script in the service file and adjust accordingly for your setup. Also note that I'm using the `standalone` mode of execution because the `nginx` one isn't stable yet. See the [Certbot renewal documentation](https://certbot.eff.org/docs/using.html#renewal) for more examples.

## Activate and Enable the Timer

Tell systemd to read the system's unit files again, and then start and enable the timer:

    $ sudo systemctl daemon-reload
    $ sudo systemctl start renew-letsencrypt.timer
    $ sudo systemctl enable renew-letsencrypt.timer

Starting the timer is necessary because otherwise it wouldn't be active until the next time you rebooted (assuming it was enabled, that is). You can verify that the timer has been started, its planned execution times, service logs, etc using the following commands:

    $ sudo systemctl list-timers
    $ sudo journalctl -u renew-letsencrypt
    $ sudo journalctl -u renew-letsencrypt --since="yesterday"

## More Information

See the following for more information:

* [systemd timers on the Arch Linux wiki](https://wiki.archlinux.org/index.php/Systemd/Timers)
* `man systemd.timer`
* `man systemd.time`
* `man systemd.service`
* `man journalctl`

This was [originally posted](https://mjanja.ch/2016/07/using-systemd-timers-to-renew-lets-encrypt-certificates/) on my personal blog; re-posted here for posterity.
