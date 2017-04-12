num_list=[]
while True:
    num = raw_input('Enter a number: ')
    if num == "done":
    	break
   
    
    else:
        try:
            	num = int(num)
            	num_list.append(num)
        except:
            	print "Invalid Input"
		
largest = max(num_list)
smallest = min(num_list)


print "Maximum is", largest
print "Minimum is", smallest
