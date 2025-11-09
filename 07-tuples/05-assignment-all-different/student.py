def all_different(xs):
    for i in range(0, len(xs)):
        for j in range(0, i):
            if xs[i] == xs[j]:
                return False
     
    return True