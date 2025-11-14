def combine(d1, d2):
    result = {}
    for key in d1.keys():
        if d1[key] in d2:
            result[key] = d2[d1[key]]
    return result