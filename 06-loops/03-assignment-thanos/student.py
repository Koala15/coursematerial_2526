from math import floor

def thanos(queue_size, target_size):
    i = queue_size
    count = 0

    while i > target_size:
        i = floor( i / 2)
        count += 1

    return count