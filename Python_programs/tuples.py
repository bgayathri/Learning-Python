name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
word = dict()
for line in handle:
		line = line.rstrip()
		if not line.startswith('From '):continue
		tmp = line.split()
		if not word.has_key(tmp[5][:2]):
				word[tmp[5][:2]] = 1
		else:
				word[tmp[5][:2]] += 1
                
key = sorted(word)
for i in key:
    print "%s %d" % (i,word[i])
