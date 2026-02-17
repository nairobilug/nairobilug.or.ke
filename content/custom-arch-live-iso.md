Title: Building a Custom Arch Linux Live ISO in the Cloud
Date: 2024-03-11
Updated: 2025-07-11
Category: Linux
Tags: AWS, Arch Linux, How-to
Slug: custom-live-arch-linux-iso
Author: Benson Muite
Summary: Build a live iso that can be booted from a USB stick

# Building a Custom Arch Linux Live ISO in the Cloud

[Arch Linux](https://archlinux.org/) has a number of packages that may not be available
in other distributions, in particular [Ink/Stitch](https://aur.archlinux.org/packages/inkstitch).
It can be helpful to be able to run such a program on another computer which may not have it
installed.  A live iso can help one do this. Building a bootable live ISO image on the cloud
can be convenient as it can be automated and allow saving on bytes needed to download build
dependencies to a local computer.  The following steps enable building on [AWS](https://aws.amazon.com)
using an [Arch Linux image](https://wiki.archlinux.org/title/Arch_Linux_AMIs_for_Amazon_Web_Services).

Log into the instance

```
ssh -i sshkey  arch@ip.address
```

After logging in, first repopulate the keys and update the system

```
sudo pacman -Scc
sudo rm -rf /etc/pacman.d/gnupg
sudo pacman-key --init
sudo pacman-key --populate
sudo pacman -Syu
```

Next install [archuseriso](https://github.com/laurent85v/archuseriso)
```
sudo pacman --needed -Sy git arch-install-scripts bash dosfstools e2fsprogs \
  erofs-utils grub libarchive libisoburn make mtools parted squashfs-tools syslinux
git clone https://github.com/laurent85v/archuseriso.git
sudo make -C archuseriso install
```

Inkstitch is available in [Aur](https://aur.archlinux.org/packages/inkstitch), but not
in the main Arch repositories.  To add it to the live iso image, first create a local
repository with a locally built Ink/Stitch package.

```
sudo pacman --noconfirm -S base-devel inkscape
git clone https://aur.archlinux.org/inkstitch.git
cd inkstitch
makepkg --install
cd ..
mkdir inkstitchdb
cd inkstitchdb
repo-add inkstitch.db.tar.zst ../inkstitch/*.pkg.tar.zst
cd ..
cp inkstitch/*.zst inkstitchdb/
```

Create a profile for the image using the lxqt image as the starting point
```
cd archuseriso
cd profiles
cp -r lxqt inkstitch
cd inkstitch
echo inkscape >> packages.x86_64
echo inkstitch >> packages.x86_64
sed -i 's/\#\[custom\]/\[inkstitch\]/g' pacman.conf
sed -i 's/\#SigLevel = Optional TrustAll/SigLevel = Optional TrustAll/g' \
pacman.conf
sed -i 's|\#Server = file:///home/custompkgs|Server = file:///home/arch/inkstitchdb|g' \
pacman.conf
sed -i 's|iso_name="aui-lxqt-inkstitch"|iso_name="aui-lxqt-inkstitch"|g' \
profiledef.sh
cd ../../..
```

Build the live iso image
```
sudo aui-mkiso archuseriso/profiles/inkstitch/
```
Once done, the resulting iso should be available at
```
/home/arch/out/aui-lxqt-linux_6_15_6-0711-x64.iso
```

## References

- https://wiki.archlinux.org/title/Install_Arch_Linux_on_a_removable_medium
- https://wiki.archlinux.org/title/Archiso
- https://mags.zone/help/arch-usb.html
- https://wiki.archlinux.org/title/Pacman/Tips_and_tricks#Custom_local_repository

*Available under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license*
