''''
Write a python function that takes a prime number, the function should return the 
lower and upper prime of that inputed prime number
'''

def primeNumber(n):
    if n > 1 and n%2!=0:
        print(n - 1 , n + 1)
    else:
        print("Not a prime number.")

entered_number = int((input("Enter your number: ")))
primeNumber(entered_number)            