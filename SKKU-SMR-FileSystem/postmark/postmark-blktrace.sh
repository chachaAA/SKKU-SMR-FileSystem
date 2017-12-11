#!/bin/bash

./pm < pm.conf >> ./result/blktrace/ext4-lazy/pm_ext4-lazy_2
kill -2 `ps -ef | grep "trace-cmd" | grep -v grep | awk '{print $2}'`

cd result/blktrace/ext4-lazy
blkparse -t sda.blktrace.* >> ext4-lazy.blktrace
cd ../../../

python trace2sect.py ./result/blktrace/ext4/ext4.blktrace temp-data
python mkfigure.py temp-data ./graph/blktrace-ext4-lazy


echo "benchmark is completed" | mutt -s "benchmark complete" yhcha77@gmail.com
