'''
Hailstone algorithm
start with an integer n
if n is even, divide by 2
if n is odd, multiply n by 3 nd add 1 to it.
Repeat the process and terminate when n==1 
'''

n = int(input("Enter your number: "))

sequence=[]
sequence.append(int(n))

while n!=1:
    if n % 2 == 0:
        n = n/2
        sequence.append(int(n))
    else:
        n = (3*n)+1
        sequence.append(int(n))

print(sequence)        