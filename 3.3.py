for t in range(-9, 99, 3):
    if t < 0:
        y = -3*t**2 + 3*t - 5
        print("y:", y)
    elif t == 0:
        y = 3*t**2 - 3*t + 5
        print("y:", y)
    elif t > 0:
        y = 3*t**2 -3*t -5
        print("y:", y)
