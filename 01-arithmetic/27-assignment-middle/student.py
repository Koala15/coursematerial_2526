def middle(a, b, c):
    sum = a + b + c
    middle = sum - max(a, b, c) - min(a, b, c)
    return middle