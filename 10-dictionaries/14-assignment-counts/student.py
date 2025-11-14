def counts(xs):
    result = {}
    for i in xs:
        result[i] = result.get(i, 0) + 1
    return  result