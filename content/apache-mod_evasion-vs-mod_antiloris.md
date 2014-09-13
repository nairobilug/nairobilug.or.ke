Title: APACHE (mod_evasion vs mod_antiloris)
Date: 2014-09-13 18:28
Category: Linux
Tags: Linux, Tech, Security
Slug: apache-and-DOS-attacks
Author: John Troon
Summary: Analyzing how Apache is crippled by a DOS tools like Slowloris and a side note for Nginx...


Slowloris is among the well known Denial of service [tools](http://resources.infosecinstitute.com/dos-attacks-free-dos-attacking-tools/) used by both experienced attackers and script kidos. This evening, have been testing *mod_evasion* and *mod_antiloris* on Apache/2.2.15 (Oracle Linux 6.5 using Redhat built Kernel).

First Setup:
-----------

> ####Server: 192.168.43.221 (running Apache with *mod_evasion* loaded)
> ####Attacking Machine: 192.168.43.39 (Slowloris "DOSing" the server)

**Apache error logs**

![Reading Error from bad requests](/images/badheader.png "Apache error logs")

The loaded module (*mod_evasion*), can not save Apache from the DOS attack, accessing the web server from the browser is somehow even impossible.

![Apache DOSed](/images/apachedown.png "Can not access via Browser")

But this module can prevent brute-force attack in a web server (eg automated attack to guess a password).

![mod_evasion can prevent Brute-force..](/images/bruteforce.png "mod_evasion can prevent Brute-force attack")

Just to make a interesting comparison, I replaced Apache with Nginx on the same Server (192.168.43.221) and **ta! da!..**
![Nginx is not DOSed by Slowloris](/images/nginxup.png "Nginx is not DOSed by Slowloris") Nginx gracefully made it by ignoring the request made Slowloris. But I noticed brute-force attacks are possible by default settings! ![Nginx Brute-forced](/images/bfnginx.png "Nginx can be Brute-forced")


Second Setup:
------------

> ####Server: 192.168.43.221 (running Apache with mod_antiloris loaded)
> ####Attacking Machine: 192.168.43.39 (slowloris "DOSing" the server)

*mod_antiloris* played it nice by monitoring the requests send by the client and rejected extra connections. Accessing the web services from the browser was not interfered.

![mod_antiloris logs](/images/antiloris.png "mod_antiloris logs")

*mod_evasion* is over-hyped but can not save Apache from Slowloris. on the other hand, *mod_antiloris* worked fine and denied Slowloris a chance to fuck-up with Apache.

 
Explanation:
------------

**Putting the Lens on the Logs...**

```
<snip>
192.168.43.39 - - [13/Sep/2014:15:12:55 +0300] "GET / HTTP/1.1" 400 0 "-" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)" "-"
<snip>
```

Apache waits for a complete header to be received which makes it good to serve web-content even in slow connections. So, by default the timeout value is 300 seconds and it's reset each time the client sends more packets. Slowloris takes advantage by sending incomplete HTTP requests headers and maintains the connection by sending more bad requests headers which reset time-out counter.

Slowloris is written in perl, it plays around with **CR (Carriage Return)** and **LF (Line Feed)** at the end of every incomplete HTTP request. A blank line after the header is used to represent the completion of the header in HTTP. Since the request is incomplete and the timeout is 300 seconds, Apache will keep the connection alive waiting for the remaining data, while Slowloris keeps on sending the incomplete requests resetting the timeout counter.

As a result, all available connections will be sucked up by Slowloris and cause a Denial of Service. mod_antiloris helped Apache beat Slowloris but you can also use IPtables by setting connection limit or putting Apache behind Varnish. Another solution I've not tested is using Hardware Load Balances that only accept full HTTP connections.

Nginx uses a much more event-driven (asynchronous) architecture that can be scaled instead of the "Maximum Connections" as in Apache. So in a nutshell, Nginx ignores the requests send by Slowloris and processes other "full" connections.

This is not to claim that Nginx is bullet proof by default, tools like [golris](https://github.com/valyala/goloris) can mess with your Nginx though you can always protect this from happening by using Nginx "Http limit conn" module / IPtables / deny POST requests or patch Nginx, so it drops connection if the client sends POST body at very slow rate.

**But I'll always go with Nginx whenever possible!**

```html
I think Apache should find a way of prioritizing clients sending full HTTP request to minimise the DOS attack.

```

####Chao!