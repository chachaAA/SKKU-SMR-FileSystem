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

	y = int(ret[0])

	if 'M' in ret[3] :
		c = 'r'
	else :
		c = 'b'

	return x, y, c

x_data = list()
y_data = list()
c_data = list()

x_data1 = list()
y_data1 = list()
c_data1 = list()

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

	#if y < 83886080 :
	x_data.append(x)
	y_data.append(y/2/1024)
	c_data.append(c)
	# else :
	# 	x_data1.append(x)
	# 	y_data1.append(y/2/1024)

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 18,
        }

# plt.subplot(211)
plt.xlim(0, 3000)
plt.scatter(x_data, y_data, s=1, color=c_data, alpha=1, marker='s')
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Disk Offset (KiB)', fontdict=font)

# plt.subplot(212)
# plt.xlim(0, 280)
# plt.scatter(x_data1, y_data1, s=1, c='k', alpha=1, marker='s')
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Disk Offset (KiB)', fontdict=font)

#plt.show()
plt.savefig(sys.argv[2] + '.png', format='png')

# print "data size :", data_size*512/1024/1024.0
# print "metadata size :", metadata_size*512/1024/1024.0
# print "journal size :", journal_size*512/1024/1024.0

# print ""
# print "x :", x_lim[0], ":", x_lim[1] 