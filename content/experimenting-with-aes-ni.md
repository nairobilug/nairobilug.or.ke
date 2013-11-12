Title: Experimenting with AES-NI
Date: 2013-11-10 13:00
Category: Linux
Tags: linux, crypto
Slug: experimenting-with-aesni
Author: Alan Orth
Summary: Experimenting with hardware-accelerated AES on Sandy Bridge+ chipsets

Ever since the [Sandy Bridge microarchitecture](https://en.wikipedia.org/wiki/Sandy_Bridge), Intel CPUs have been coming with hardware-accelerated <abbr title="Advanced Encryption Standard">AES</abbr> support (aka "AES-NI", *new instructions*).  I figured it would be interesting see a comparison between AES with and without the hardware acceleration on my [Intel Core i5-3317U CPU](http://ark.intel.com/products/65707) (Ivy Bridge) on Arch Linux.

According to [a post](http://openssl.6102.n7.nabble.com/having-a-lot-of-troubles-trying-to-get-AES-NI-working-td44285.html) on the OpenSSL Users mailing list, you can force `openssl` to avoid hardware AES instructions using the `OPENSSL_ia32cap` environment variable.

## Benchmarks
First, with AES-NI enabled (the default, on hardware that supports it):

    :::console
    $ openssl speed -elapsed -evp aes-128-cbc
    You have chosen to measure elapsed time instead of user CPU time.
    Doing aes-128-cbc for 3s on 16 size blocks: 57196857 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 64 size blocks: 15343650 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 256 size blocks: 3897351 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 1024 size blocks: 978726 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 8192 size blocks: 122310 aes-128-cbc's in 3.00s
    OpenSSL 1.0.1e 11 Feb 2013
    built on: Sun Oct 20 14:49:13 CEST 2013
    options:bn(64,64) rc4(16x,int) des(idx,cisc,16,int) aes(partial) idea(int) blowfish(idx) 
    compiler: gcc -fPIC -DOPENSSL_PIC -DZLIB -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -march=x86-64 -mtune=generic -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -m64 -DL_ENDIAN -DTERMIO -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM
    The 'numbers' are in 1000s of bytes per second processed.
    type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes
    aes-128-cbc     305049.90k   327331.20k   332573.95k   334071.81k   333987.84k

Then, setting the capability mask to turn off the hardware AES features:

    :::console
    $ OPENSSL_ia32cap="~0x200000200000000" openssl speed -elapsed -evp aes-128-cbc
    You have chosen to measure elapsed time instead of user CPU time.
    Doing aes-128-cbc for 3s on 16 size blocks: 27883366 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 64 size blocks: 7736907 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 256 size blocks: 1949328 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 1024 size blocks: 498847 aes-128-cbc's in 3.00s
    Doing aes-128-cbc for 3s on 8192 size blocks: 62446 aes-128-cbc's in 3.00s
    OpenSSL 1.0.1e 11 Feb 2013
    built on: Sun Oct 20 14:49:13 CEST 2013
    options:bn(64,64) rc4(16x,int) des(idx,cisc,16,int) aes(partial) idea(int) blowfish(idx) 
    compiler: gcc -fPIC -DOPENSSL_PIC -DZLIB -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -march=x86-64 -mtune=generic -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -m64 -DL_ENDIAN -DTERMIO -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM
    The 'numbers' are in 1000s of bytes per second processed.
    type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes
    aes-128-cbc     148711.29k   165054.02k   166342.66k   170273.11k   170519.21k

You can see that hardware-accelerated AES is pretty consistently **twice** as fast as the implementation without *aesni*.  So it's not an exponential win, but getting **twice** the performance is certainly very serious!  This is great for not only for servers using AES encryption (SSL/TLS, hello!), but also for consumers wanting to connect to said servers as well as things like full-disk encryption.

**Note:** It seems Arch Linux's OpenSSL is built with AES-NI support but not as an *engine*, so `openssl speed` could be misleading (ie, you'd see no difference with or without the capabilities masked).  To get the AES-NI support you need to use `-evp` ("envelope") mode, which is some sort of [high-level interface](http://wiki.openssl.org/index.php/EVP) for crypto functions in OpenSSL.

This was originally [posted on](http://mjanja.co.ke/2013/11/disabling-aes-ni-on-linux-openssl/) on my personal blog; re-posted here for posterity.
