'''
    Write a program that computes the real roots of a quadratic function. User should
    input values of a,b,c. Then it should display a message indicationg the number of real roots, along with the values of the real roots.
'''

def quadraticFormula():
    a = float(input("value of A: "))
    b = float(input("value of B: "))
    c = float(input("value of C: "))
    d = (b**2 - 4*a*c)**0.5
    root1 = complex((-b+d)/(2*a))
    root2 = complex((-b-d)/(2*a))
    print(f"The real roots are {root1.real} and {root2.real}")

quadraticFormula()