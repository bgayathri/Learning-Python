score = raw_input("Enter Score: ")
score = float(score)
Grade = "not defined"
if score < 0.0 or score > 1.0:
    print "Please enter a valid score"
elif score >= 0.9:
    Grade="A"
elif score >= 0.8:
    Grade="B"
elif score >= 0.7:
    Grade="C"
elif score >= 0.6:
    Grade="D"
elif score < 0.6:
    Grade="F"
print "The student's grade is %s" % Grade