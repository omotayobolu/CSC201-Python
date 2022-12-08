'''
Write a function that takes 3 real numbers as arguments and determines whether the
numbers represents the length of the sides of a triangle (none of them is greater than
or equal to the sum of other two)
'''

def valid_triangle(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        return True
    else:
        return False

length_a = float(input("Enter the length of side a: "))
length_b = float(input("Enter the length of side b: "))
length_c = float(input("Enter the length of side c: "))

if valid_triangle(length_a, length_b, length_c):
    print("Triangle is valid")
else:
    print("Triangle is not valid")    
