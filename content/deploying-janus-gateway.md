Title: Deploying Janus Gateway 
Date: 2023-09-21 12:45
Category: Video
Tags: streaming, video conferencing,
Slug: deploying-janus-gateway
Author: Benson Muite
Summary: Steps to deploy a highly configurable real time streaming server on Fedora linux

# Introduction

[Janus Gateway](https://github.com/meetecho/janus-gateway) is an open source
GPL licensed [WebRTC](https://webrtc.org/) server developed by
[Meetecho](https://www.meetecho.com/). It is written in C and can
enable video conferencing when running on low resource devices such
as single board computers. It can use 
[http](https://en.wikipedia.org/wiki/HTTP),
[web sockets](https://en.wikipedia.org/wiki/WebSocket),
[rabbitMQ](https://en.wikipedia.org/wiki/RabbitMQ),
[MQTT](https://mqtt.org/) and 
[Unix Sockets](https://en.wikipedia.org/wiki/Unix_domain_socket) as transports.
It is distributed with example programs
to enable video conferencing, audio conferencing and real time chat, but
is designed primarily as a platform to enable creation of custom
video conferencing and messaging solutions.  As such it has a
plugin architecture to
enable easy customization and minimize resource requirements. Projects
using Janus Gateway include:
* [A Flutter Janus Client](https://github.com/flutterjanus/flutter_janus_client)
* [A Qt Client](https://github.com/ouxianghui/janus-client)
* [PiKVM](https://pikvm.org)
* [A Game Server](https://github.com/webrtcventures/webrtc-tic-tac-toe)
* [Janus Cloud](https://pypi.org/project/janus-cloud/)
* [Nethserver](https://www.nethserver.org/)
* [Jangouts](https://github.com/jangouts/jangouts)

This tutorial will describe installation of Janus Gateway from
source on Fedora 38 with [Nginx](https://nginx.org/en/)
as a reverse proxy and using
[uacme](https://github.com/ndilieto/uacme) to manage certificates.
A package for Fedora should soon be available,
thanks to [Renich Ciric](https://bugzilla.redhat.com/show_bug.cgi?id=2121585).
these steps mostly follow Renich Ciric's build procedure.
Packages are already available for other distribution such as
[Arch Linux](https://aur.archlinux.org/packages/janus-gateway) and
[Ubuntu Linux](https://packages.ubuntu.com/jammy/janus).

## Installation Steps

Create a new Fedora 38 virtual machine and then install the
build dependencies
```
sudo dnf -y install wget uacme nginx lua-devel \
  cmake doxygen duktape-devel gcc glib2-devel graphviz \
  intltool jansson-devel libavcodec-free-devel \
  libavformat-free-devel libavutil-free-devel \
  libconfig-devel libcurl-devel libmicrohttpd-devel \
  libnice-devel libogg libpcap-devel librabbitmq-devel \
  libsrtp-devel libtool libwebsockets-devel lua-devel make \
  nanomsg nanomsg-devel openssl-devel opus-devel paho-c-devel \
  policycoreutils-python-utils sofia-sip-devel speexdsp-devel \
  usrsctp-devel zlib-devel
```

### Getting and Building Janus Gateway

Clone from GitHub directly and then build it
```
git clone https://github.com/meetecho/janus-gateway
cd janus-gateways
git checkout 9f03638
sh autogen.sh
./configure --prefix=/opt/janus
make
sudo make install
sudo make configs
```

Note that Janus is by default installed in `/opt/janus`
you may wish to change this to more standard locations for
Fedora such as `/usr/bin`.

Create a Janus user
```
sudo useradd -r janus
```
then create a Janus service file
```
sudo vi /etc/systemd/system/janus.service
```
with the following content
```
[Unit]
Description=Janus WebRTC Server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/opt/janus/bin/janus -o
Restart=on-abnormal
LimitNOFILE=65536
User=janus
Group=janus

[Install]
WantedBy=multi-user.target
```

### Setting up an SSL certificate

Use [uacme](https://github.com/ndilieto/uacme) to issue an SSL
certificate from [Let's Encrypt](https://letsencrypt.org/)
by first starting Ngnix

```
sudo systemctl enable nginx
sudo systemctl start nginx
```

The start the verification process

```
sudo mkdir /etc/ssl/private/
sudo mkdir -p /usr/share/nginx/html/.well-known/acme-challenge
sudo uacme -v -c /etc/ssl new
sudo uacme -v -c /etc/ssl issue my.domain.name
```

You will be asked to create the challenge file, do this using a separate
login

```
sudo vi /usr/share/nginx/html/.well-known/acme-challenge/long-token-sequence
```

and enter the key authorization as a plain text string. Check that the
authorization completes in the first terminal and then remove the challenge file.

```
sudo rm /usr/share/nginx/html/.well-known/acme-challenge/long-token-sequence
```

You can now log out of the second terminal. If you expect to
run Janus for a long time, you may wish to create a cron job
to automatically renew the SSL certificate.

## Configuration Steps

### Ports and Firewalls

[SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux)
has permissions on what Nginx can connect to. Enable Nginx to
connect to communication ports to be able to reverse proxy to them from
port 443:

```
sudo setsebool -P httpd_can_network_connect 1
sudo semanage port -a -t http_port_t -p tcp 8088
sudo semanage port -a -t http_port_t -p udp 10000-20000
sudo semanage port -a -t http_port_t -p tcp 10000-20000
```

You also need to enable your firewall to allow connections to
tcp and udp ports 10000-20000 for [STUN](https://en.wikipedia.org/wiki/STUN)
and to tcp ports 80 and 443 for [http](https://en.wikipedia.org/wiki/HTTP)
and [https](https://en.wikipedia.org/wiki/HTTPS) respectively.

### Reverse Proxy

Enable Nginx to serve content from the demo directory

```
sudo semange fcontext -a -t httpd_sys_content_t '/usr/share/janus/demos/(/.*)?'
sudo restorecon -R /usr/share/janus/demos/
```

As explained by
[Bagus Aginsa](https://facsiaginsa.com/janus/basic-janus-configuration-with-ssl),
edit the Nginx configuration file to route all http traffic to https
and to act as a reverse proxy for Janus

```
sudo vi /etc/nginx/nginx.conf
```

and enter the following content

```
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log notice;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    keepalive_timeout   65;
    types_hash_max_size 4096;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80;
        listen       [::]:80;
        server_name  my.domain.name;
        location / {
                    rewrite ^(.*) https://my.domain.name$1 permanent;
        }

    }
# Settings for a TLS enabled server.

    server {
        listen       443 ssl http2;
        listen       [::]:443 ssl http2;
        server_name  my.domain.name;
        root         /opt/janus/share/janus/demos/;

        ssl_certificate "/etc/ssl/my.domain.name/cert.pem";
        ssl_certificate_key "/etc/ssl/private/my.domain.name/key.pem";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_ciphers PROFILE=SYSTEM;
        ssl_prefer_server_ciphers on;

        location  /janus/ {
                proxy_pass http://127.0.0.1:8088/janus/;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }

    }
}
```

### Janus configuration

As explained by
[Bagus Aginsa](https://facsiaginsa.com/janus/configure-janus-behind-nat)
configure Janus to use Google STUN servers as many
virtual machines offered by cloud providers will
use network address translation

```
sudo vi /opt/janus/etc/janus/janus.jcfg
```

and ensure the lines for STUN configuration contain

```
        stun_server = "stun.l.google.com"
        stun_port = 19302
        nice_debug = false
        full_trickle = true
```

and the lines for media contain

```
        rtp_port_range = "10000-20000"
```

Configure the http transport

```
sudo vi /etc/janus/janus.transport.http.jcfg 
```

ensure that the http settings contain

```
        json = "indented"        # Whether the JSON messages should be indented (default),
                                 # plain (no indentation) or compact (no indentation and no spaces)
        base_path = "/janus"     # Base path to bind to in the web server (plain HTTP only)
        http = true              # Whether to enable the plain HTTP interface
        port = 8088              # Web server HTTP port
```

Then edit the client side javascript settings to enable connection to the server

```
sudo vi /opt/janus/share/janus/demos/settings.js
```

Ensure they contain

```
//var server = /janus/;
if(window.location.protocol === 'http:')
        server = "http://" + window.location.hostname + "/janus/";
else
        server = "https://" + window.location.hostname + "/janus/";
```

## Testing

Restart Nginx and start Janus

```
sudo systemctl enable janus
sudo systemctl start janus
sudo systemctl restart nginx
```

You can check the server configuration by using

```
curl localhost:8088/janus/info
```

on the server running Janus, and

```
curl https://my.domain.name/janus/info
```

on another machine.

If you now go to `https://my.domain.name/demos.html` you should
be able to try out the demos using the http transport.  To enable
other transports, see the [documentation](https://janus.conf.meetecho.com/docs/)
and setup appropriate firewall rules.

