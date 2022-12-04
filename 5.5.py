''''
Write a python function that takes a prime number, the function should return the 
lower and upper prime of that inputed prime number
'''

def primeNumber(numbers):
    for n in numbers:
        if n > 1 and n % n == 0 and n/n == 1:
                return n - 1 , n + 1
        else:
            return "Not a prime number."

entered_numbers = int(float(input("Enter your numbers: ")))
primeNumber(entered_numbers)            