def drop_last_digit(n):
    last_digit = n % 10
    drop_digit = (n - last_digit) / 10
    return drop_digit