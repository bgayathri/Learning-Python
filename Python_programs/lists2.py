fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
word = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):continue
    count = count + 1
    word = line.split()
    print word[1]
    


print "There were", count, "lines in the file with From as the first word"
