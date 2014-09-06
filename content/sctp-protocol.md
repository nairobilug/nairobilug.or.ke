Title: The "SCTP" protocol
Date: 2014-09-04 18:37
Category: Tech
Tags: Tech, Linux, programming
Slug: SCTP-protocol
Author: John Troon
Summary: In the Know: Stream Control Transmission Protocol (SCTP)

TCP and UDP protocols have been in around for approximately 20+ years now. Even though they have helped in building nice Internet applications since inception, things are changing in the techie world and they will always change. TCP being a connection state protocol while UDP a connectionless state protocol, there have been attempts to build a general purpose protocol above the IP layer, SCTP so far is the only one endorsed by  the IETF.

SCTP combines concepts from TCP and UDP for even better control over the transport of packets (with additional API calls for SCTP). TCP applications can be ported to SCTP.

##Some Cool Features:

1. **More Support for multi-homed devices:** 
Laptops these days can come with more than one in-built Ethernet cards, wireless cards, wiMAX cards and Bluetooth... Hence, a minimal laptop can at-least have 3 distinct IP network interfaces. SCTP support selective choosing of interfaces with ability to add and drop interfaces dynamically. You can unplug your machine from an Ethernet network, and an Internet application immediately pick up with existing  wifi connection etc.

2. **Whoo! Multi-streaming:** 
An application doesn't need multiple sockets rather a single socket that can be used for multiple streams to a connected host! Let's say the X Window System is connecting on multiple ports, with SCTP, these could all be separate streams on a single association. *Fast-Browsing!*, HTML docs containing referenced image files or other media files, they will load faster with SCTP compared in TCP. HTTP use separate TCP connection per downloaded URL, even with HTTP 1.1 "persistent connections" it's still expensive. With SCTP, the separate media files could be downloaded concurrently in separate streams on a single association.

3. **No “out of band”... :** 
SCTP has no “out of band” messages, but a large number of events can be interleaved onto a single association, so that an application can monitor the state of the association (e.g. when the other end adds another interface to the association).

4. **Greater socket range:** 
The range of socket options is greater than TCP or UDP. These also can be used to control individual associations or individual streams
 within a single association. For example, messages on one stream can be given a longer time-to-live than messages on other streams, increasing the likelihood of their delivery.

5. **Do more with single socket:**
A single socket can support multiple associations, that is, a computer can use a single socket to talk to more than one computer. This is not multicast, but it could be useful in peer-to-peer situations

6. **Still message-oriented.. :** 
TCP is a byte-oriented protocol, and UDP is message-oriented. The majority of applications are message-oriented, and applications using TCP have to jump through hoops, such as sending the message length as a first parameter. SCTP is message-oriented, so such tricks are not so necessary.

> It is no longer necessary to open up multiple sockets; instead, a single socket can be used for multiple streams to a connected host. SCTP tries to provide a more reliable and robust protocol than either TCP or UDP. Btw, SCTP is not in any Microsoft release, another reason to love Linux? :)



##Resources
[The Main  Site for SCTP ](http://www.sctp.de)

[The Linux Kernel Project Home Page](https://lists.sourceforge.net/lists/listinfo/lksctp-developers)

[Stream Control Transmission Protocol(SCTP)](http://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol)

[Overview of SCTP (Stream Control Transmission Protocol)](http://www.slideshare.net/PeterREgli/overview-of-sctp-transport-protocol)







