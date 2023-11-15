Title: Exploring Anti-DOS Tools for Apache Httpd
Date: 2014-09-13 18:28
Category: Linux
Tags: linux, security, httpd, nginx
Slug: exploring-anti-dos-tools-for-apache-httpd
Author: John Troon
Summary: Analyzing how Apache can be crippled by a DOS tool like Slowloris and a side note on Nginx...

Slowloris is among the well known "Denial Of Service" (or DOS) [tool](http://resources.infosecinstitute.com/dos-attacks-free-dos-attacking-tools/) used by both experienced attackers and script kiddies. This evening, I've been testing *mod_evasion* and *mod_antiloris* on Apache httpd /2.2.15 (Oracle Linux 6.5 using Redhat built Kernel).

First Setup
-----------

- Server: 192.168.43.221 (running Apache httpd with *mod_evasion* loaded)
- Attacking Machine: 192.168.43.39 (Slowloris "DOSing" the server)

**Apache httpd error logs**

![Error from bad requests]({static}/images/exploring-anti-dos-tools-for-apache-httpd/badheader.png "Apache error logs")

The loaded module (*mod_evasion*), can't save Apache httpd from the DOS attack, even loading the site from a browser is somehow impossible.

![Apache DOSed]({static}/images/exploring-anti-dos-tools-for-apache-httpd/apachedown.png "Can't access via Browser")

But this module can prevent a brute-force attack (*e.g. an automated script to guess a password field in a web-form*) in a web server (running Apache httpd).

![mod_evasion can prevent Brute-force..]({static}/images/exploring-anti-dos-tools-for-apache-httpd/bruteforce.png "mod_evasion can prevent Brute-force attack")

Just to make an interesting comparison, I replaced Apache httpd with Nginx on the same Server (192.168.43.221) and **ta! da!..**

![Nginx is not DOSed by Slowloris]({static}/images/exploring-anti-dos-tools-for-apache-httpd/nginxup.png "Nginx is not DOSed by Slowloris") Nginx gracefully made it by ignoring the request from Slowloris. But I noticed a brute-force attack is possible while using Nginx default settings! **Nginx access logs**
![Nginx Brute-forced]({static}/images/exploring-anti-dos-tools-for-apache-httpd/bfnginx.png "Nginx can be Brute-forced")

Second Setup
------------

- Server: 192.168.43.221 (running Apache httpd with mod_antiloris loaded)
- Attacking Machine: 192.168.43.39 (Sowloris "DOSing" the server)

*mod_antiloris* played it nice by monitoring the requests coming from the client and rejected extra connections. Accessing the web services from the browser was not interfered.

![mod_antiloris logs]({static}/images/exploring-anti-dos-tools-for-apache-httpd/antiloris.png "mod_antiloris logs")

*mod_evasion* is cool but can't save Apache httpd from Slowloris. On the other hand, *mod_antiloris* worked fine and denied Slowloris a chance to mess up with the Apache httpd server.

Explanation
-----------

**Putting the Lens on the Logs...** (Apache httpd access log)

![Apache-httpd access log]({static}/images/exploring-anti-dos-tools-for-apache-httpd/accesslog.png "Apache httpd access logs")

*Why did mod_antiloris pass the test and mod_evasion fail?..* *Why did Slowloris work on Apache httpd and not on Nginx?*

Apache httpd waits for a **complete HTTP request header** to be received, this makes it good to serve web-content even in slow connections. So, by default, the timeout value is 300 seconds and it's reset each time the client sends more packets. Slowloris takes advantage by sending incomplete HTTP request headers and maintains the connection by sending more incomplete request headers resetting the time-out counter.

Slowloris is written in Perl, it simply plays around with **CR (Carriage Return)** and **LF (Line Feed)** at the end of every incomplete HTTP request header. A blank line after the request header is used to represent the completion of the header in HTTP. Since the request is incomplete and the timeout is 300 seconds, Apache httpd will keep the connection alive waiting for the remaining data, while Slowloris keeps on sending the incomplete HTTP requests resetting the timeout counter.

As a result, all available connections will be sucked up by Slowloris and cause a Denial of Service. mod_antiloris helped Apache httpd beat Slowloris but you can also use IPtables by setting a connection limit or putting Apache httpd behind Varnish. Another solution I've not tested is using a Hardware Load Balancer that only accepts full HTTP connections.

Nginx uses a much more event-driven (asynchronous) architecture that can be scaled, instead of the "Maximum Connections" as in Apache httpd. So, in a nutshell, Nginx ignores the requests from Slowloris and processes other "full" connections.

This is not to claim that Nginx is bullet proof by default, tools like [golris](https://github.com/valyala/goloris) can mess with your Nginx server (when running with default settings), though you can always protect this from happening by using Nginx "Http limit connection" module / IPtables / deny POST requests or patch Nginx, so it drops connection if the client sends POST body at a very slow rate.

**But I'll always go with Nginx whenever possible!**

### Conclusion

I think Apache httpd should find a way of prioritizing clients sending full HTTP requests to minimize DOS attacks of the (above) described nature...

Ciao!
