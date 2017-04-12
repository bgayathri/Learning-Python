fname = 'filelist.dat'

with open(fname) as f:
    for line in f:
        key = line
        print(key)
