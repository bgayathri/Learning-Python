def computepay(h,r):
    if h > 40:
    	gross_pay = r * 40 + ((r * 1.5) * (h - 40))
    else:
    	gross_pay = h * r
	return gross_pay
    
hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Enter Rate:")
r = float(rph)
p = computepay(h,r)
print p