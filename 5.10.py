'''
    Write a program that computes the real roots of a quadratic function. User should
    input values of a,b,c. Then it should display a message indicationg the number of real roots, along with the values of the real roots.
'''

a = float(input("value of A: "))
b = float(input("value of B: "))
c = float(input("value of C: "))

roots = -b+-((b**2 - 4*a*c)**0.5)/(2*a)
print(roots)