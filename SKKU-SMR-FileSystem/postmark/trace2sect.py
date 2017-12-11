import sys

# [0]: process, [1]:?, [2]:time, [3]:event, [4]:major,minor, [5]:RWBS, [6]:(), [7-9]:start blk+#of blk [10]:?? --> queue

if len(sys.argv) == 1:
	print "NO ARGUMENT ERROR"
	exit(1)

f = open(sys.argv[1])
out = open(sys.argv[2], 'w')

while 1 :
	line_data = f.readline()
	if len(line_data) < 2 :
		break

	ret = list()
	ret = line_data.split()
	if len(ret) < 11 :
		continue

	if 'W' in ret[5] and ret[4] == '8,0' and not 'F' in ret[5] :
		my_str = str(ret[7]) + '\t' + str(ret[9]) + '\t' + str(ret[2][:-1:]) + '\t' + str(ret[5]) + '\n'
		out.write(my_str)

f.close()
out.close()