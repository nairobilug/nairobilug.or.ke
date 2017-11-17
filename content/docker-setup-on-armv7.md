Title: Setting up Docker on an ARMv7 processor that runs Fedora 22
Date: 2017-11-17 20:00
Category: Linux
Tags: docker, linux
Slug: setting-up-docker-on-arm
Author: Bonface Munyoki
Summary: This is a short post on my docker set up on an ARM processor that runs Fedora 22

Docker has come in handy for some dev work I've been doing. It has provided a clear way to avoid polluting the global namespace with unnecessary programs in addition to availing a simple way for easy and fast simulation of a target environment without much hassle.

Setting up docker on my main workstation machine that runs `Arch linux` on an AMD A6 processor was painlessly easy. Things however were not smooth when I wanted to deploy the whole setup(for demo purposes) on my droplet which runs `Fedora 22` on an ARMv7 processor.

I naively installed docker and `docker-compose` from Fedora's official repositories. However, running a simple `docker-compose up -d` kept bringing this annoying error:

```
Can't connect to docker daemon
```

Even running docker as sudo did not alleviate the problem. After alot of searching on github issues and stackoverflow, I tried changing the `user` to the docker group and restarting the docker service like so:

```
sudo usermod -aG docker $(whoami)
sudo service docker start
```

Permissions were however not the problem. It was far from it. Had they- the permissions- been the problem, I would have been able to run docker as sudo. It's interesting to note that resolving permissions solved alot of people's problems. The docker daemon(which is binded to unix sockets instead of tcp ports) operates with root privileges. Adding users to the group `Docker` gives *that* user root r/w operations, hence you don't need to append your commands with `sudo`.

My problem was that docker is not officially supported on ARM processors that run Fedora. You can see that [here](https://docs.docker.com/engine/installation/#server). Thanks to the good people at the #docker channel, I was able to try out several things and eventually solve my problems. What I had not done was install the `devicemapper` storage driver and map it to docker's storage-drive. Doing this was as simple as editing(or creating) the daemon conf file(`/etc/docker/daemon.json`) and adding the following:

```
{
    "storage-driver": "devicemapper"
}
```

I've come to appreciate how well supported docker has become across various devices in addition to a strong community behind it. You can read more about installing, running, and using docker on ARM devices [here](https://github.com/umiddelb/armhf/wiki/Installing,-running,-using-docker-on-armhf-(ARMv7)-devices#installing-docker-on-fedora-22-armhfp ). You can read more the Device Mapper storage driver [here](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/ ).
