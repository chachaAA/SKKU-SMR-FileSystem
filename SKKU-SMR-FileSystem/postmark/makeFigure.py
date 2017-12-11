import matplotlib.pyplot as plt
import numpy as np
import sys


metadata_size = 0
data_size = 0
journal_size = 0
start_time = 0

# [0]: start_sect [1]: size_sect [2]: time_stamp
# return value : time(x), sect(y)
def parse(data) :
	ret = list()
	ret = data.split() 

	x = float(ret[2][:-1:])

	global start_time
	if start_time == 0 :
		start_time = x
	x -= start_time

	y = int(ret[0])/2/1024

	if 'M' in ret[3] :
		c = 'r'
	else :
		c = 'b'

	return x, y, c

x_data = list()
y_data = list()
c_data = list()

x_lim = 0
y_lim = 0

if len(sys.argv) == 1:
	print "NO ARGUMENT ERROR"
	exit(1)


f = open(sys.argv[1])
plt.figure(num=1, figsize=(32, 16), dpi=100)

while 1 :
	line_data = f.readline()
	if len(line_data) < 2 :
		break

	x, y, c = parse(line_data)
	if (x == -1) :
		continue

	if float(x) > float(x_lim) :
		x_lim = x

	if float(y) > float(y_lim) :
		y_lim = y

	x_data.append(x)
	y_data.append(y)
	c_data.append(c)

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 18,
        }

plt.xlim(0, x_lim)
plt.ylim(0, y_lim)
plt.scatter(x_data, y_data, s=1, color=c_data, alpha=1, marker='s')
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Disk Offset (KiB)', fontdict=font)

plt.savefig(sys.argv[2] + '.png', format='png')