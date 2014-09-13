Title: Exploring anti-DOS tools for Apache httpd
Date: 2014-09-13 18:28
Category: Linux
Tags: Linux, Tech, Security
Slug: exploring-anti-DOS-tools-or-Apache-httpd
Author: John Troon
Summary: Analyzing how Apache can be crippled by a DOS tools like Slowloris and a side note on Nginx...


Slowloris is among the well known "Denial Of Service" (or DOS) [tool](http://resources.infosecinstitute.com/dos-attacks-free-dos-attacking-tools/) used by both experienced attackers and script kidos. This evening, have been testing *mod_evasion* and *mod_antiloris* on Apache httpd /2.2.15 (Oracle Linux 6.5 using Redhat built Kernel).

First Setup:
-----------

- Server: 192.168.43.221 (running Apache httpd with *mod_evasion* loaded)
- Attacking Machine: 192.168.43.39 (Slowloris "DOSing" the server)

**Apache httpd error log**

![Reading Error from bad requests](/images/badheader.png "Apache error logs")

The loaded module (*mod_evasion*), can not save Apache httpd from the DOS attack, accessing the web server from the browser is somehow even impossible.

![Apache DOSed](/images/apachedown.png "Can not access via Browser")

But this module can prevent brute-force attack in a web server (eg automated attack to guess a password).

![mod_evasion can prevent Brute-force..](/images/bruteforce.png "mod_evasion can prevent Brute-force attack")

Just to make a interesting comparison, I replaced Apache httpd with Nginx on the same Server (192.168.43.221) and **ta! da!..**
![Nginx is not DOSed by Slowloris](/images/nginxup.png "Nginx is not DOSed by Slowloris") Nginx gracefully made it by ignoring the request made Slowloris. But I noticed brute-force attacks are possible while using Nginx default settings! **Nginx access log**
![Nginx Brute-forced](/images/bfnginx.png "Nginx can be Brute-forced")


Second Setup:
------------

- Server: 192.168.43.221 (running Apache httpd with mod_antiloris loaded)
- Attacking Machine: 192.168.43.39 (slowloris "DOSing" the server)

*mod_antiloris* played it nice by monitoring the requests coming in from the client and rejected extra connections. Accessing the web services from the browser was not interfered.

![mod_antiloris logs](/images/antiloris.png "mod_antiloris logs")

*mod_evasion* is over-hyped but can not save Apache httpd from Slowloris. On the other hand, *mod_antiloris* worked fine and denied Slowloris a chance to fuck-up with the Apache httpd server.

 
Explanation:
------------

**Putting the Lens on the Logs...** (Apache httpd access log)

![Apache-httpd access log](/images/accesslog.png "Apache httpd access log")


Apache httpd waits for a complete header to be received which makes it good to serve web-content even in slow connections. So, by default the timeout value is 300 seconds and it's reset each time the client sends more packets. Slowloris takes advantage by sending incomplete HTTP requests headers and maintains the connection by sending more bad requests headers which reset time-out counter.

Slowloris is written in Perl, it plays around with **CR (Carriage Return)** and **LF (Line Feed)** at the end of every incomplete HTTP request. A blank line after the header is used to represent the completion of the header in HTTP. Since the request is incomplete and the timeout is 300 seconds, Apache httpd will keep the connection alive waiting for the remaining data, while Slowloris keeps on sending the incomplete requests resetting the timeout counter.

As a result, all available connections will be sucked up by Slowloris and cause a Denial of Service. mod_antiloris helped Apache httpd beat Slowloris but you can also use IPtables by setting connection limit or putting Apache httpd behind Varnish. Another solution I've not tested is using a Hardware Load Balancer that only accept full HTTP connections.

Nginx uses a much more event-driven (asynchronous) architecture that can be scaled, instead of the "Maximum Connections" as in Apache httpd. So in a nutshell, Nginx ignores the requests send by Slowloris and processes other "full" connections.

This is not to claim that Nginx is bullet proof by default, tools like [golris](https://github.com/valyala/goloris) can mess with your Nginx though you can always protect this from happening by using Nginx "Http limit conn" module / IPtables / deny POST requests or patch Nginx, so it drops connection if the client sends POST body at very slow rate.

**But I'll always go with Nginx whenever possible!**

### Conclusion
I think Apache httpd should find a way of prioritizing clients sending full HTTP requests to minimise the DOS attack.

Ciao! 