def close_enough(x, y):
    if x - y <= 0.1 and y - x <= 0.1:
        return True
    return False