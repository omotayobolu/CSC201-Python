'''
    nested counting loop to do 
          1
        1 2 1
      1 2 4 2 1
    1 2 4 8 4 2 1
  1 2 4 8 16 8 4 2 1
'''

for i in range(0,5):
    if i == 0:
        i = [str(2**j) for j in range(i+1)]
    else:
        n = [str(2**j) for j in range(i+1)]
        n.pop()
        l = [str(2**j) for j in range(i+1)] + n[::-1]
        print(" ".join(l).center(18))        
