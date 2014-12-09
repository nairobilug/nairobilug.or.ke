Title: Maps and custom error pages in nginx
Date: 2014-12-09 17:00
Category: Linux
Tags: linux, nginx
Slug: maps-and-custom-error-pages-nginx
Author: Alan Orth
Summary: Using nginx maps to allow IP ranges during web server maintenance


During a recent web application upgrade I had to limit access to the the web servers; I wanted the administrators and myself to be able to access the site, but for everyone else to see an "_Under Construction_" page. My initial plan was to test if the `$remote_addr` was one of the allowed IPs, and then redirect those clients to a maintenance page, but I couldn't figure out how to test more than one IP address (seriously)!

I eventually stumbled upon the [nginx map module](http://nginx.org/en/docs/http/ngx_http_map_module.html) which, combined with a custom error page, ended up being an elegant, fun solution to this problem.

### Elegant maps
Here is a snippet from _/etc/nginx/conf.d/default.conf_ which shows the important bits:

```
server {
...

    location / {
        if ($denied != 0) {
            # HTTP 503: service unavailable
            return 503;
         }

         # Send requests to Tomcat
         proxy_pass http://127.0.0.1:8443;
    }

    error_page 503 @maintenance;

    location @maintenance {
        root /tmp;
        rewrite ^(.*)$ /maintenance.html break;
    }
}

map $remote_addr $denied {
    default 1;
    2.18.216.110 0;
    192.64.147.150 0;
}
```

By default all IP addresses are denied (ie, `$denied=1`), but depending on the client's IP address, the `$denied` variable can be set to 0. In the root location block I essentially test if the IP address is denied and conditionally return an HTTP 503 (_Service Unavailable_), which is handled by a custom `error_page` handler with a named location block. So cool!

### In retrospect
In retrospect I probably could have used a regex in the `$remote_addr` test, but maps are really a more flexible, efficient, and "nginx" way of accomplishing this. On that note, I'm using nginx more and more lately and, in addition to being fast as hell and having better TLS support, it's just more fun to use than Apache. ;)

Furthermore, to deploy this I wrote an Ansible playbook which included a list of allowed IPs and reconfigured the nginx vhost by using a Jinja2 template which iterated over the IPs to create the map block above. Very cool, and very easy to reverse when the maintenance was over!

This was originally [posted on](https://mjanja.ch/2014/12/maps-and-custom-error-pages-in-nginx/) on my personal blog; re-posted here for posterity.
