'''
    to calculate both arithmetic and geometric mean of inputted +ve integer numbers.
'''
# terminate input if a user enters -1

sum=0
product=1
count=0
number= int(input("Enter a number greater than 0: "))
while number >0:
    sum += number
    product *= number
    count += 1
    number = int(input("Enter a number greater than 0: "))
arithmetic_mean = sum/count
geometric_mean = product ** (1/count)
print("Arithmetic mean is: ", arithmetic_mean)
print("Geometric mean is: ", geometric_mean)