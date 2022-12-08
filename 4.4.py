'''
write a program to read a sequence of integer from the keyboard. The reading should stop when the user inputs a zero. Your program should print the sum and average of the numbers with appropriate messages.
'''

count = 0
sum = 0
num=1
while num != 0:
    num = int(input("Enter number: "))
    sum += num
    count +=1
    average = sum/count        

print("The average of the integers is: ", average)
print("The sum of the integers is: ", sum)
