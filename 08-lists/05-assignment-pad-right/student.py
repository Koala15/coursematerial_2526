def pad_right(xs, length, padding):
    while len(xs) < length:
        xs.append(padding)