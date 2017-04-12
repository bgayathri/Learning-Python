number=raw_input("Guess a number between 1 and 10...")
number=int(number)
print number
birthday=raw_input("Have you already celebrated your birthday this year, enter Yes or No...")
print birthday
yob=raw_input("Enter the year you were born...")
yob=int(yob)
print yob
if birthday=="Yes":
	age = number * 2
	age = age + 5
	age = age * 50
	age = age + 1766
	age = age - yob
	age = str(age)
	print "your age is", age[1:]
	print "number you guessed is", age[0]
elif birthday=="No":
	age = number * 2
	age = age + 5
	age = age * 50
	age = age + 1766
	age = age - yob
	age = str(age)
	print "your age is", age[1:]
	print "number you guessed is", age[0]
else:
	print "please make sure you have your inputs right"

