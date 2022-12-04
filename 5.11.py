'''
Writea python program using function name swap() that takes in two intwgers and 
swap their values.
'''

def swap(a,b):                          
    c = a
    a = b
    b = c

    print(a,b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

swap(a,b)