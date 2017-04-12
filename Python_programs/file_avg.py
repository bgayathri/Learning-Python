fname = raw_input("Enter file name: ")
fh = open(fname)
line_list = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line[20:]
    line = line.rstrip()
    line = float(line)
    line_list.append(line)
    


count= 0
tot = 0
avg = 0

for number in line_list:
	count = count + 1
	tot += number
	avg = tot / count
	
print "Average spam confidence:", avg
