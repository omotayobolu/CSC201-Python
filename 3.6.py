score = float(input("Enter your score: "))
if score > 100:
    print("Your score can't be above 100")
elif score >= 70 :
    print("Your grade is A")
elif score >= 60 and score < 70:
    print("Your grade is B")   
elif score >= 50 and score < 60:
    print("Your grade is C")
elif score >= 45 and score < 50:
    print("Your grade is D")
elif score >= 40 and score < 45:
    print("Your grade is E")
elif score < 40 and score >= 0 : 
    print("Your grade is F")
else:
    print("Your score is invalid, your score has to be between 0 and 100")                     