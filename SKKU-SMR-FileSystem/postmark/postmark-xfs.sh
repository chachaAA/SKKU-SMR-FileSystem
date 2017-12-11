#!/bin/bash

umount /mnt/smr
umount /dev/sda1

mkfs.xfs -f /dev/sda1
mount -t xfs /dev/sda1 /mnt/smr
echo 50 > /sys/class/bdi/8\:0/max_ratio
echo 50 > /sys/class/bdi/8\:0/min_ratio
echo 3 > /proc/sys/vm/drop_caches

sleep 2h


echo "benchmark is completed" | mutt -s "benchmark complete" yhcha77@gmail.com
