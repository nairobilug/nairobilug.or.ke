Title: Setting up Docker on an ARMv7 processor
Date: 2017-11-17 20:00
Category: Linux
Tags: docker, linux
Slug: setting-up-docker-on-arm
Author: Bonface Munyoki
Summary: This is a short post on my docker set up on an ARM processor that runs Fedora 22

Docker has come in handy for some dev work I've been doing. It has provided a clear way to avoid polluting the global namespace with unnecessary programs in addition to availing a simple way for easy and fast simulation of a target environment without much hassle- I also just want to play around with it.

Setting up docker on my main workstation machine that runs Archlinux on an AMD A6 processor was painlessly easy. Things however were not smooth when I wanted to deploy the whole setup(for demo purposes) on my droplet which runs Fedora 22 on an ARMv7 processor.

I naively installed docker and `docker-compose` from Fedora's official repositories. However, running a simple `docker-compose up -d` kept bringing this annoying error:

```
Can't connect to docker daemon
```

Even running docker as sudo did not alleviate the problem. After alot of searching on github issues and stackoverflow, I tried changing the *user* to the docker group afterwhich I restarted the docker service like so:

```
sudo usermod -aG docker $(whoami)
sudo service docker start
```

Permissions were however not the problem. It was far from it. It's interesting to note that resolving permissions solved alot of people's problems. Here's why: Docker commands use unix sockets(instead of tcp ports) to talk to the Docker daemon. These unix sockets operate with root privileges. Since users can't access the unix socket, they won't be able to communicate with the docker daemon. Alot of people recommend adding the user to the Docker group which has the effect of giving *that* user root privileges, hence you don't need to append your commands with `sudo`. Ideally, a group called 'docker' is created when installing Docker. However, if this group does not exist when the docker daemon is started, the socket file is owned by root. A regular user won't have sufficient permissions to access the socket and running docker commands generates the `Can't connect to docker daemon` error. At this point, be warned of letting non-root users run Docker! There are some serious security concerns that you should be aware of. Read more about this [here](http://www.projectatomic.io/blog/2015/08/why-we-dont-let-non-root-users-run-docker-in-centos-fedora-or-rhel/).

Docker is not officially supported on ARM processors that run Fedora. You can see that [here](https://docs.docker.com/engine/installation/#server). Thanks to the good people at the #docker channel, I was able to try out several things and eventually make Docker run on my arm system. What I had not done was install the `devicemapper` storage driver and map it to docker's storage-driver. Doing this was as simple as editing(or creating) the daemon conf file(`/etc/docker/daemon.json`) and adding the following:

```
{
    "storage-driver": "devicemapper"
}
```

Docker uses storage drivers to control how images and containers are stored and managed on the Docker host. In the above case, I've used `devicemapper` storage driver as this is supported in Fedora running on ARM. The `devicemapper` storage driver uses the Device Mapper framework in image and container management. It uses block devices dedicated to Docker and operates at the block level, rather than the file level. The Device Mapper is a framework provided by the Linux Kernel for mapping physical block devices onto higher-level virtual block devices. It works by passing data from a virtual block device, which is provided by the device mapper itself, to another block device. Docker also supports several different storage drivers, using a pluggable architecture. In my case, I hadn't set up the devicemapper properly and this led to the `Can't connect to docker daemon` error. Take special care on how you configure your storage. You can read more about that [here](http://www.projectatomic.io/blog/2015/06/notes-on-fedora-centos-and-docker-storage-drivers/ ).

I've come to appreciate how well supported docker has become across various devices in addition to a strong community behind it. You can read more about installing, running, and using docker on ARM devices [here](https://github.com/umiddelb/armhf/wiki/Installing,-running,-using-docker-on-armhf-(ARMv7)-devices#installing-docker-on-fedora-22-armhfp ). You can read more the Device Mapper storage driver [here](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/ ). To use storage drivers effectively, a basic understanding of how Docker builds and stores images is vital- you can read about that [here](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/ ).

