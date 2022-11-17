number_one = float(input("Enter first number: "))
number_two = float(input("Enter second number: "))

golden_ratio1 = round((number_one + number_two) / number_one, 3)
golden_ratio2 = round(number_one / number_two, 3)

if golden_ratio1 == golden_ratio2 and golden_ratio1 == 1.618:
    print("The numbers are in golden ratio")
else:
    print("The numbers are not in golden ratio")