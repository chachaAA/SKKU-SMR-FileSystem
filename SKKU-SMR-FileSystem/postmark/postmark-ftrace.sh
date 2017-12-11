#!/bin/bash
./pm < pm.conf >> ./result/ftrace/ext4/pm_new_ext4_1
pkill -2 -f trace-cmd

cd result/ftrace/ext4
trace-cmd report >> ext4.complete.ftrace1
cd ../../../

python trace2sect.py ./result/ftrace/ext4/ext4.complete.ftrace temp-data
python makeFigure.py temp-data ./graph/ftrace-ext4


echo "benchmark is completed" | mutt -s "benchmark complete" yhcha77@gmail.com
