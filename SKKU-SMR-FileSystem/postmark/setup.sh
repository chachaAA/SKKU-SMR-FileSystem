#!/bin/bash

sudo apt-get install blktrace trace-cmd xfsprogs btrfs-tools python-matplotlib -y
sudo apt-get install uuid-dev pkg-config libtool autoconf libselinux1-dev -y
cd f2fs-tools1.9.0
sudo ./autogen.sh
sudo ./configure
sudo make
sudo make install
cd ..