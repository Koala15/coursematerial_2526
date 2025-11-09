def remove_all(xs, item_to_remove):
    for index in range(len(xs) - 1 , -1, -1):
        if xs[index] == item_to_remove:
            del xs[index] 