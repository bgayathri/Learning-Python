count = 0
total = 0
largest = None
smallest = None
while True:
	#Get input
	inp = raw_input("Enter a number: ")
	
	#handle the edge cases
	if inp == "done" : break
	if len(inp) < 1 : break
	
	#DO the work
	try:
		
		num = float(inp)
	
	except:
		
		print "Invalid Input"
		
		continue
		
	count = count + 1
	total = total + num
	
	print num, total
	
print "avg", total /count
