def contains_duplicates(xs):
    copy = set()
    for i in xs:
        copy.add(i)
    return len(xs) > len(copy)