name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
word = []
my_dict = {}
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):continue
    word = line.split()

    if word[1] not in my_dict:
       my_dict[word[1]] = 1
    else:
       my_dict[word[1]] += 1

my_max = 0
my_max_str = ""

for key in my_dict:
    if my_dict[key] > my_max:
         my_max = my_dict[key]
         my_max_str = key
print my_max
print my_max_str 
#maximum = max(my_dict, key=my_dict.get) 
#print(maximum, my_dict[maximum])
