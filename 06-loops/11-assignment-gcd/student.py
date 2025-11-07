def gcd(x, y):
    i = min(abs(x), abs(y))

    for j in range(i + 1, 1, -1):
        if x % j == 0 and y % j == 0:
            return j
        
    return 1