def concatenate(xs, ys):
    fs = []
    fs += ys
    while len(fs) != 0:
        xs.append(fs[0])
        fs.pop(0)
    
    '''
    if (xs is ys):
        count = len(ys)
        for i in range(0,count):
            xs.append(ys[i])
    else:
        for y in ys:
            xs.append(y)
    '''