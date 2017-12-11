import matplotlib.pyplot as plt
import numpy as np
import sys



# [0]: "major:minor", [1]:cpu, [2]:seq_num, [3]:time_stamp, [4]:pid, [5]:event, [6]:RWBS_field, [7-9]:start blk+#of blk
# return value : time(x), sect(y), color(RWBS)
def parse(data) :
	ret = list()
	ret = data.split() 

	if len(ret) != 11 :
		return -1, -1, -1

	# if not write(W) and complete(C), return trash value  
	if (not 'C' in ret[5] and 'W' in ret[6] ) :
		return -1, -1, -1

	# X axis : timestamp
	x = float(ret[3])

	# Y axis : data offset (sect -> MiB)
	y = int(ret[7])*512/1024/1024


	# color : metadata write -> red OR data write -> blue 
	if 'M' in ret[6] :
		c = 'r'
	else :
		c = 'b'

	return x, y, c

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 18,
        }


x_data = list()
y_data = list()
c_data = list()


# 1st argument : input file name, 2nd argument : output file name
if len(sys.argv) < 3:
	print "ARGUMENT SIZE ERROR"
	exit(1)

f = open(sys.argv[1])
plt.figure(num=1, figsize=(32, 16), dpi=100)


ex_line_data = 0
x_lim = 0
y_lim = 0

while 1 :
	line_data = f.readline()
	if ex_line_data == line_data :
		continue
	ex_line_data = line_data


	if len(line_data) < 2 :
		break

	x, y, c = parse(line_data)
	if x == -1 :
		continue

	if float(x) > float(x_lim) :
		x_lim = x

	if float(y) > float(y_lim) :
		y_lim = y

	x_data.append(x)
	y_data.append(y)
	c_data.append(c)

plt.xlim(0, x_lim)
plt.ylim(0, y_lim)
plt.scatter(x_data, y_data, s=1, color=c_data, alpha=1, marker='s')
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Disk Offset (MiB)', fontdict=font)

# plt.show()
plt.savefig(sys.argv[2] + '.png', format='png')