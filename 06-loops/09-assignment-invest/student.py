def invest(amount, rate, goal):
    year = 0

    while amount < goal:
        amount += amount *  rate / 100
        year +=1
    
    return year