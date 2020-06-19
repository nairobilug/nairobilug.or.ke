Title: Building a Pentest Lab With Docker
Date: 2020-06-13 14:30
Modified: 2020-06-13 14:30
Category: Linux
Tags: Docker, Infosec
Slug: Lightweight lab entirely in Docker without Vmware or VirtualBox
Authors: Ian Muchina
Summary: Lightweight penetration testing lab inside docker GUI support
## What is Docker?

![Docker Logo]({filename}/images/docker-pentest-lab/docker.svg)
Docker is a container platform that is similar to a Hypervisor like Virtualbox. Docker uses less storage and RAM and are portable.

Docker can run on: 
- Linux
- Windows
- Mac OS

In this article I will go over how to set up a penetration testing lab entirely in docker

It will consist of two types of containers.

* Attacker Machine
* Target Machine

## Installation on Linux

#### The Convenience Script

Update: You can install Docker quickly and non interactively when you use the convenience scripts provided by Docker at [get.docker.com](https://get.docker.com)

Installation is then done by :

```console
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

#### Debian based distros

Anything that uses `apt` to install software is Debian based.
Find a complete list [here](https://en.wikipedia.org/wiki/List_of_Linux_distributions#Debian-based)

To install on Ubuntu :

```console
$ sudo apt install docker.io
```
----
 
## Docker on Windows
To run docker in windows, install [Docker desktop](https://docs.docker.com/docker-for-windows/install/).

![Windows 10 Logo]({filename}/images/docker-pentest-lab/windows10.svg)

 Docker Desktop is an awesome app with a graphical interface. It can run Linux containers from windows. However, there's one major deal-breaker.

Docker Desktop cannot co-exist with VirtualBox or VMware, because it requires Hyper-V to run Linux containers😤[^1].

> Hyper-V is Microsoft's hardware virtualization product

As a workaround. 
 * Use [Docker Toolbox](Use https://docs.docker.com/toolbox/) 👨‍💻
 * Learn Hyper-V 📚
 * Install Linux 🤷‍♀️ 

>This is also the same reason [WSL](https://blogs.windows.com/windowsdeveloper/2016/07/22/fun-with-the-windows-subsystem-for-linux/) cannot co-exist with VMware/Virtualbox.

Now I'm starting to see why people hate Microsoft. They lock users to their ecosystem.

----

## Hello World

After you have installed docker, run this command as a test

```console
$ sudo docker run hello-world
```

If it completes successfully, you can follow along

![Server status]({filename}/images/docker-pentest-lab/Server status-pana.svg)

## The Network

The network will be called `vulnerable`. It will have a 10.0.0/24 subnet

Create it with this command
```console
$ sudo docker network create vulnerable --attachable --subnet 10.0.0.0/24
```

## Attacker Container

For this, I will use Parrot OS. It's docker images are better Kali Linux Images.

![Cyber photo]({filename}/images/docker-pentest-lab/cyberr.svg)


First download the Parrot OS Docker image. This command will take a while depending on your internet connection. 

```console
$ docker pull parrotsec/security:latest
```

Create and run the container .

```bash
sudo docker run \
    --name parrot \
    -it \
    --hostname parrot \
    --network vulnerable \
    --ip="10.0.0.2" \
    --env DISPLAY=$DISPLAY \
    -v /dev/shm:/dev/shm \
    --device /dev/snd \
    --device /dev/dri \
    --mount type=bind,src=/tmp/.X11-unix,dst=/tmp/.X11-unix \
    parrotsec/security:latest \
    /bin/bash 
```

All tools available in Parrot OS are now an `apt-get` away.

Use this command to restart the parrot OS container after a reboot.

```console
$ sudo docker start -a parrot
```

### Target container:Metasploitable2

![Target]({filename}/images/docker-pentest-lab/Target-pana.svg)


This is a very vulnerable test machine. It is what I recommend for anyone starting out.

Open another terminal and pull the metasploitable image. The image is around 500MB.

```console
$ docker pull tleemcjr/metasploitable2
```
To run a metasploitable container:

```bash
docker run \
    -it \
    --network vulnerable \
    --ip="10.0.0.3" \
    --name metasploitable \
    --hostname metasploitable2 \
    tleemcjr/metasploitable2 \
    bash
```

You should see a terminal prompt like this

```console
root@metasploitable2:/#
```

Start the vulnerable services

```console
root@metasploitable2:/# services.sh
```

You can now access metasploitable from [10.0.0.3](http://10.0.0.3)

If you want to stop the container, close the terminal with `CTRL + D`

Run this command to start metasploitable again

```console
$ sudo docker start -a parrot
```

Then start the vulnerable services. 
```console
root@metasploitable2:/# services.sh
```

#### Guides & Tutorials


There are tons of free guides out there on metasploitable. 

![Image of person Studying]({filename}/images/docker-pentest-lab/read.svg)

1. [The Easiest Metasploit Guide You’ll Ever Read](https://www.exploit-db.com/docs/english/44040-the-easiest-metasploit-guide-you%E2%80%99ll-ever-read.pdf)
2. [Metasploit Unleashed](https://www.offensive-security.com/metasploit-unleashed/)
3. [Metasploitable 2 Exploitability Guide](https://metasploit.help.rapid7.com/docs/metasploitable-2-exploitability-guide)
4. [Youtube Tutorials](https://www.youtube.com/results?search_query=metasploitable)

If you don't know what guide to use, I recommend [this one](https://metasploit.help.rapid7.com/docs/metasploitable-2-exploitability-guide).


## More vulnerable containers 🧑‍💻
![More Cyber]({filename}/images/docker-pentest-lab/hacker.svg)

You can extend the lab with any of these containers depending on your learning goal.


### OWASP Juiceshop
This container focusses on web application security.

![Juiceshop Logo]({filename}/images/docker-pentest-lab/juiceshop.svg)

To create and start the juiceshop container for the first time

```bash
docker run -d \
    --name juiceshop \
    --network vulnerable \
    --ip="10.0.0.6" \
    bkimminich/juice-shop
```

Check if it is running

```console
$ docker ps 
```

Access the web interface from this URL

[http://10.0.0.6:3000/](http://10.0.0.6:3000/)

Stop the container when you're done

```console
docker stop juiceshop
```

Start the container again
```console
docker start juiceshop
```
##### Juiceshop Guides
* [Pwning Juiceshop](https://pwning.owasp-juice.shop/)
* [Youtube Videos](https://www.youtube.com/results?search_query=owasp+juiceshop)

#### OWASP Webgoat 🐐

[Webgoat]((https://owasp.org/www-project-webgoat/)) is a ctf-style vulnerable container focused on web application security.

![goat-svg]({filename}/images/docker-pentest-lab/goat.svg)

Create and run the container for the first time

```bash
docker run  -d \
    --name webgoat \
    --network vulnerable \
    --ip="10.0.0.4" \
    -e TZ=$(cat /etc/timezone) \
    webgoat/goatandwolf
```


Access Webgoat and Webwolf from these URLs

[10.0.0.4:8080/WebGoat](http://10.0.0.4:8080/WebGoat)



[10.0.0.4:9090/WebWolf](http://10.0.0.4:9090/WebWolf)

To stop the container

```console
docker stop webgoat
```

To Start the container again.

```console
docker start webgoat
```
If you can't access the url, check if it is running.

```console
$ docker ps -a
```

### Why I use docker for a pentest lab

Two Operating systems make my computer painfully slow. Containers aren't resource-intensive and perform well. This fits my use case.

![Lab.svg]({filename}/images/docker-pentest-lab/lab.svg)

If you have RAM to spare then it's really not that much of a difference. 

## When not to use Docker

If you want to run Windows containers from a linux host, you are out of luck. You can run linux containers on Windows though

### Common Docker Commands

Stop a container:

```console
$ sudo docker stop containerName
```

Start a container 

```console
$ sudo docker start containerName 
```

List running  and stopped containers

```console
$ sudo docker ps -a
```
Spawn a bash shell in a running container
```console
$ sudo docker exec -it containerName bash
```

Docker has tab completion for each of these commands.

### Graphical apps inside docker
Sometimes you may want to run a GUI tool like firefox or burpsuite.


The Parrot OS commands above are already set for running graphical apps. You only need to install these packages

```console
$ apt install hicolor-icon-theme \
    libcanberra-gtk* libgl1-mesa-dri \
    libgl1-mesa-glx libpangox-1.0-0 \
    libpulse0 libv4l-0 fonts-symbola \ 
```

You can run a few commands to avoid some errors encountered when running GUI apps

#### Burpsuite
Burp Suite is a web app pentesting tool for monitoring http requests and responses.

![Burpsuite Logo]({filename}/images/docker-pentest-lab/burp.svg)

To install and run burpsuite inside the parrot os container.

```console
# sudo apt update
# sudo apt install burpsuite
# java -jar -Xmx2G /usr/bin/burpsuite
```
You can then point your browser to use `10.0.0.2:8080` as the proxy and burp will intercept everything

#### Firefox

Firefox, is a free and open-source web browser.

![Firefox Logo]({filename}/images/docker-pentest-lab/firefox.svg)

To install and run firefox:

```console
$ apt install firefox ca-certificates 
```
### Credits
* Illustrations from [Freepik](https://stories.freepik.com/)

![Stories by freepik](https://ianmuchina.com/assets/img/posts/freepik.svg)

This was originaly posted on my blog at [ianmuchina.com](https://ianmuchina.com/)
### Further reading/research

Jess Frazelle has written an awesome [blog post](https://blog.jessfraz.com/post/docker-containers-on-the-desktop/) with details on running graphical apps inside Docker containers. She's also given this awesome [Talk/Demo](https://youtu.be/cYsVvV1aVss) on running various applications and retro games inside docker containers.


## Footnotes

[^1]: Docker requires a Linux kernel to run Linux containers on Windows. Docker accomplishes this by running a Linux Virtual Machine inside Hyper-V. This is still more resource-efficient than full VM's. Plus there's the added benefit of running both Windows and Linux containers. This is not possible on Linux


