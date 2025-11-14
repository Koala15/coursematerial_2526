def find_duplicates(xs):
    new_set = set()
    current_set = set()
    for i in xs:
        if (len(current_set) > 0) and (i in current_set):
            new_set.add(i)
        else:
            current_set.add(i)
    return list(new_set)